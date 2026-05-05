# Prüfidentifikator pairing patterns

Source: `.cursor/rules/validation-rules/pruefidentifikator-verification-mandatory-always.mdc`.

Use these patterns to derive the **paired response Prüfis** for any request PI before writing the doc. Every doc must list all of them.

## Pairing rules

```
Request XX001 → Success XX002 (even)  + Rejection XX003 (odd)
Request XX077 → Success XX078 (even)  + Rejection XX080 (next odd after 078)
Request XX600 → Success XX602 (even)  + Rejection XX603 (odd)
Request XX601 → Success XX604 (even)  + Rejection XX605 (odd)
```

**Response format always matches request format** — payloads differ, so the NB can correlate only if the response PI pairs with the request PI. Send 55077 → never get 55002; send 55001 → never get 55078.

## Known flows (verify against `ahb-tables/INDEX.md` before citing)

| Flow | Request 1 | Succ 1 | Rej 1 | Request 2 | Succ 2 | Rej 2 | Notes |
|---|---|---|---|---|---|---|---|
| LIEFERBEGINN (detailed vs simplified) | 55001 | 55002 | 55003 | 55077 | 55078 | 55080 | `START_LIEFERBEGINN` has `oneOf` both |
| LIEFERENDE / Abmeldung (LF → NB) | 55004 | 55005 | 55006 | — | — | — | plus 55037 follow-up (*Beendigung der Zuordnung*) |
| LIEFERENDE (NB → LF) | 55007 | 55008 | 55009 | — | — | — | NB-initiated |
| 600/601 Module 3 registration | 55600 | 55602 | 55604 | 55601 | 55603 | 55605 | 55600 = new consuming MaLo, 55601 = new generating MaLo; verified against AHB/processinfo |

## How to derive for an arbitrary PI

1. Read the row in `ahb-tables/INDEX.md` for the given PI — note its **description** and **direction**.
2. If the PI is in the **Known flows** table above, use the listed pairing and still verify every related PI in `INDEX.md`.
3. If the PI is not in the Known flows table, derive relationships from sources only: `maco-api-documentation/pythons/processinfo.json`, `docs-offline/*`, AHB metadata, and fixtures. Do **not** compute `PI+1` / `PI+2` from the number.
4. ORDERS/ORDRSP/IFTSTA flows are especially not numeric-pairing flows. For example, `17123` relates to `19124`, `21043`, and `21033`; `17133` relates to `19133`.
5. Check the trigger schema (`maco-api-documentation/macoapp-trigger/components/schemas/START_*.yml`) for `oneOf` / `allOf` — find sibling request PIs sharing the same trigger.
6. Cross-verify on the NB side: `grep -r "Übergabe der erzeugten Rückmeldung" docs-offline/` — those lines explicitly list which PIs the NB generates.
7. If a process diagram exists (`docs-offline/prozessdiagramme-png/INDEX.md`), view the MCS-layer swimlane — success path and rejection path are drawn with their PI numbers.

## Trigger ↔ Prüfi mapping (mandatory verification)

A trigger event name is **not** evidence of which Prüfi it generates. Always prove the mapping before listing a trigger in the doc.

The authoritative source for trigger ↔ Prüfi mapping is **`docs-offline/trigger-events-14016919e0.md`**: each trigger declares its OpenAPI schema as `[LF] START_X` / `[NB] START_X` with an `allOf $ref: PI_NNNNN`. The `$ref` points at the actual generated Prüfi.

To verify trigger `START_X`:

1. `grep -A 20 "'\\[LF\\] START_X '" docs-offline/trigger-events-14016919e0.md` — read the `allOf $ref: PI_NNNNN`. That `NNNNN` is what the LF-side trigger generates.
2. Same for the NB-side arm: `grep -A 20 "'\\[NB\\] START_X'"`. Often the same trigger name carries different Prüfis on the two sides (e.g. `[LF] START_LIEFERENDE` → 55004, `[NB] START_LIEFERENDE` → 55007).
3. Or open the trigger schema directly (`macoapp-trigger/components/schemas/START_X.yml`) and follow the `allOf $ref`.

### Known confusions (verified)

| Trigger | Generates | NOT the trigger for |
|---|---|---|
| `[LF] START_LIEFERENDE` | **PI_55004** | — |
| `[NB] START_LIEFERENDE` | **PI_55007** (NB → LF Abmeldung) | not 55004 |
| `START_AUFHEBUNG_ZUK_ZUORDNUNG_LF` | **PI_55038** (NB → LF *Aufhebung einer zuk. Zuordnung*) | **NOT 55004** — the topic is similar but the message is different. 55004's future-cancellation case (`ZG9/ZH1/ZH2`) lives **inside** the `START_LIEFERENDE` trigger, with `vertragsbeginn` instead of `vertragsende`. |
| `START_AUFHEBUNG_ZUK_ZUORDNUNG_MSB` | (MSB-side equivalent) | not the LF flow |
| `[LF] START_LIEFERBEGINN` | **PI_55001** *and* **PI_55077** (request format `oneOf` discriminates by payload shape) | — |

When listing triggers in a doc:

- One row per `(trigger, role)` arm that actually generates **this** PI.
- Add a `## Trigger scope (disambiguation)` section listing near-namesakes that generate **other** PIs, so the next reader doesn't make the same wrong inference.

## Flag discrepancies

Some offline docs reference *follow-up* PIs (e.g. 55037 "Informationsmeldung zur Beendigung der Zuordnung") as if they were the direct success response. They're not — 55037 arrives **after** a successful 55005 and is a separate message in the flow. The UTILMD MIG calls it `Informationsmeldung zur Beendigung der Zuordnung` (note "Informationsmeldung" — it doesn't expect a reply). Document both, don't conflate.
