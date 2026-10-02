#!/usr/bin/env bash
# Mirror the published Markdown twins from dokumentation.macoapp.de.
set -euo pipefail

root="$(cd "$(dirname "$0")/.." && pwd)"
index_dir="$root/docs/dokumentation"
output_dir="$root/docs-offline"
mkdir -p "$index_dir" "$output_dir"

host="dokumentation.macoapp.de"
resolve_args=()
if [[ -n "${DOKUMENTATION_IP:-}" ]]; then
  resolve_args=(--resolve "$host:443:$DOKUMENTATION_IP")
fi

for name in llms.txt llms-index.txt; do
  tmp="$index_dir/$name.tmp"
  curl -fsSL --retry 3 --retry-all-errors --max-time 60 "${resolve_args[@]}" "https://$host/$name" -o "$tmp"
  mv "$tmp" "$index_dir/$name"
done

python3 "$root/scripts/documentation_scope.py" --index-dir "$index_dir" --mirror-dir "$output_dir"

mkdir -p "$output_dir/apis"
for version in 202604 202610; do
  tmp="$output_dir/apis/trigger-$version.json.tmp"
  curl -fsSL --retry 3 --retry-all-errors --max-time 60 "${resolve_args[@]}" "https://$host/apis/trigger-$version.json" -o "$tmp"
  python3 -m json.tool "$tmp" >/dev/null
  mv "$tmp" "$output_dir/apis/trigger-$version.json"
done

manifest="$index_dir/download-manifest.tsv"
build_manifest() {
python3 - "$index_dir/llms-index.txt" "$manifest" <<'PY'
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit, unquote

source = Path(sys.argv[1]).read_text(encoding="utf-8")
links = re.findall(r"\]\((https://dokumentation\.macoapp\.de/[^)]+)\)", source)
rows = []
for url in dict.fromkeys(links):
    path = unquote(urlsplit(url).path.lstrip("/"))
    if path.endswith(".md") and ".." not in Path(path).parts:
        rows.append((url, path))
Path(sys.argv[2]).write_text("".join(f"{url}\t{path}\n" for url, path in rows), encoding="utf-8")
print(f"Indexed {len(rows)} Markdown twins")
PY
}
build_manifest

failures="$index_dir/download-failures.txt"
: > "$failures"
changes="$index_dir/download-changes.tsv"
: > "$changes"
export output_dir failures changes DOKUMENTATION_IP

download_one() {
  local url="$1" path="$2" target tmp
  target="$output_dir/$path"
  mkdir -p "$(dirname "$target")"
  tmp="$target.tmp.$$"
  local args=()
  if [[ -n "${DOKUMENTATION_IP:-}" ]]; then
    args=(--resolve "dokumentation.macoapp.de:443:$DOKUMENTATION_IP")
  fi
  if curl -fsSL --retry 3 --retry-all-errors --retry-delay 1 --max-time 45 "${args[@]}" "$url" -o "$tmp" 2>/dev/null && [[ -s "$tmp" ]] && ! head -c 20 "$tmp" | grep -q '<!DOCTYPE html'; then
    if [[ -f "$target" ]] && cmp -s "$tmp" "$target"; then
      rm -f "$tmp"
    else
      local status="added"
      [[ -f "$target" ]] && status="changed"
      mv "$tmp" "$target"
      printf '%s\t%s\n' "$status" "$path" >> "$changes"
    fi
  else
    rm -f "$tmp"
    printf '%s\n' "$url" >> "$failures"
  fi
}
export -f download_one

cut -f1,2 "$manifest" | tr '\t' '\n' | xargs -P "${PARALLEL_JOBS:-12}" -n 2 bash -c 'download_one "$1" "$2"' _

failed="$(wc -l < "$failures" | tr -d ' ')"
[[ "$failed" -eq 0 ]] || { echo "Failed downloads: $failed" >&2; exit 1; }
python3 "$root/scripts/documentation_scope.py" --index-dir "$index_dir" --mirror-dir "$output_dir" --prune
build_manifest

expected="$(wc -l < "$manifest" | tr -d ' ')"
downloaded="$(find "$output_dir" -name '*.md' -type f ! -name README.md | wc -l | tr -d ' ')"
printf 'Expected: %s; downloaded: %s; failed: %s\n' "$expected" "$downloaded" "$failed"
printf 'Added/changed: %s (see %s)\n' "$(wc -l < "$changes" | tr -d ' ')" "$changes"
[[ "$failed" -eq 0 && "$downloaded" -eq "$expected" ]]
python3 "$root/scripts/rebuild-documentation-indexes.py"
