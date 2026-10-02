# Deaktivierung eines MaBiS-ZP für die monatliche Ausfallarbeitsüberführungszeitreihe (AAÜZ) zwischen NB und BKV (anfNB) — Sicht BIKO

<Kopf rolle="BIKO" beteiligter="BIKO" festlegung="MaBiS" dokument="MaBiS" kapitel="17.3.5.2.2" sparte="Strom" schritte={3} suchtitel="Deaktivierung eines MaBiS-ZP für die monatliche Ausfallarbeitsüberführungszeitreihe (AAÜZ) zwischen NB und BKV (anfNB) — Sicht BIKO · MaBiS · Formatversion 202610" abschnitte={[{"id": "abschnitt-ablauf", "label": "Prozessablauf"}, {"id": "abschnitt-schritte", "label": "Prozessschritte"}, {"id": "abschnitt-informationen", "label": "Prozess-Informationen"}, {"id": "abschnitt-sichten", "label": "Andere Sichten des Prozesses"}]} />

<Kurzfassung>

Der ANB deaktiviert den aktivierten MaBiS-ZP für eine AAÜZ und sendet die entsprechende Information an den BIKO, die vom BIKO angenommen bzw. abgelehnt wird. Der BIKO leitet die Deaktivierung eines MaBiS-ZP für eine AAÜZ nach Erhalt an den BKV (des anfNB) weiter, sofern er die Deaktivierung angenommen hat. Der BKV (des anfNB) kann den ANB über eine seines Erachtens fehlerhafte Deaktivierung informieren. Bei einer Fehlermeldung des BKV (des anfNB) klären ANB und BKV (des anfNB) wo der Fehler vorliegt und sorgen – falls nötig – für eine Korrektur des Fehlers.

</Kurzfassung>

<a id="abschnitt-ablauf"></a>

## Prozessablauf aus Sicht des BIKO

<Systembild svg={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1004 551\" width=\"1004\" height=\"551\" role=\"img\" aria-labelledby=\"sb-title\" class=\"maco-systembild\">\n<title id=\"sb-title\">Systembild: Deaktivierung eines MaBiS-ZP für die monatliche Ausfallarbeitsüberführungszeitreihe (AAÜZ) zwischen NB und BKV (anfNB) aus Sicht BIKO</title>\n<defs><marker id=\"sb-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect class=\"sb-lane-kopf\" x=\"16\" y=\"12\" width=\"232\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend-System des Kunden</text>\n<rect class=\"sb-lane-kopf\" x=\"398\" y=\"12\" width=\"264\" height=\"46\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · BIKO</text>\n<rect class=\"sb-lane-kopf\" x=\"812\" y=\"12\" width=\"176\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"900\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Marktpartner</text>\n<line x1=\"323\" y1=\"58\" x2=\"323\" y2=\"539\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"737\" y1=\"58\" x2=\"737\" y2=\"539\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"80\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">1. Deaktivierung eines</text>\n<text x=\"530\" y=\"115\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">MABIS-ZP für die monatliche</text>\n<text x=\"530\" y=\"130\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">AAÜZ</text>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"93\" r=\"5\"/><line x1=\"900\" y1=\"98\" x2=\"900\" y2=\"110\"/><line x1=\"893\" y1=\"102\" x2=\"907\" y2=\"102\"/><line x1=\"900\" y1=\"110\" x2=\"894\" y2=\"120\"/><line x1=\"900\" y1=\"110\" x2=\"906\" y2=\"120\"/></g>\n<text x=\"900\" y=\"142\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">NB (ANB)</text>\n<line x1=\"878\" y1=\"111\" x2=\"628\" y2=\"111\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"103\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"127\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">55212</text>\n<rect class=\"sb-kasten sb-schreiben\" x=\"432\" y=\"169\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"189\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"143\" x2=\"530\" y2=\"169\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-schreiben sb-abgeleitet\" x=\"34\" y=\"169\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"189\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten erstellen</text>\n<line x1=\"432\" y1=\"185\" x2=\"230\" y2=\"185\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"177\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"233\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"253\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">2. Antwort</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"202\" x2=\"530\" y2=\"233\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"231\" r=\"5\"/><line x1=\"900\" y1=\"236\" x2=\"900\" y2=\"248\"/><line x1=\"893\" y1=\"240\" x2=\"907\" y2=\"240\"/><line x1=\"900\" y1=\"248\" x2=\"894\" y2=\"258\"/><line x1=\"900\" y1=\"248\" x2=\"906\" y2=\"258\"/></g>\n<text x=\"900\" y=\"280\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">NB (ANB)</text>\n<line x1=\"628\" y1=\"249\" x2=\"878\" y2=\"249\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"241\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"265\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">55213</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"316\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"336\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"266\" x2=\"530\" y2=\"316\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"316\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"336\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"332\" x2=\"230\" y2=\"332\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"324\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"380\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"400\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">4. Weiterleitung der</text>\n<text x=\"530\" y=\"415\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Deaktivierung</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"349\" x2=\"530\" y2=\"380\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"386\" r=\"5\"/><line x1=\"900\" y1=\"391\" x2=\"900\" y2=\"403\"/><line x1=\"893\" y1=\"395\" x2=\"907\" y2=\"395\"/><line x1=\"900\" y1=\"403\" x2=\"894\" y2=\"413\"/><line x1=\"900\" y1=\"403\" x2=\"906\" y2=\"413\"/></g>\n<text x=\"900\" y=\"435\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">BKV (des anfNB)</text>\n<line x1=\"628\" y1=\"404\" x2=\"878\" y2=\"404\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"396\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"420\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">55214</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"463\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"483\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"428\" x2=\"530\" y2=\"463\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"463\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"483\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"479\" x2=\"230\" y2=\"479\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"471\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n</svg>"} gesamt={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 974 486\" width=\"974\" height=\"486\" role=\"img\" aria-labelledby=\"sd-title\" class=\"maco-sequence\">\n<title id=\"sd-title\">Sequenzdiagramm: Deaktivierung eines MaBiS-ZP für die monatliche Ausfallarbeitsüberführungszeitreihe (AAÜZ) zwischen NB und BKV (anfNB) aus Sicht BIKO</title>\n<defs><marker id=\"sd-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect x=\"16\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"121\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend (Kunde)</text>\n<line x1=\"121\" y1=\"64\" x2=\"121\" y2=\"474\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"260\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"365\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · BIKO</text>\n<line x1=\"365\" y1=\"64\" x2=\"365\" y2=\"474\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"504\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"609\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">NB (ANB)</text>\n<line x1=\"609\" y1=\"64\" x2=\"609\" y2=\"474\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"748\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"853\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">BKV (des anfNB)</text>\n<line x1=\"853\" y1=\"64\" x2=\"853\" y2=\"474\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"609\" y1=\"90\" x2=\"365\" y2=\"90\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"81\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">1. Deaktivierung eines MABIS-ZP für die monatlic…</text>\n<text x=\"487\" y=\"105\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55212</text>\n<line x1=\"365\" y1=\"152\" x2=\"121\" y2=\"152\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"143\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<text x=\"243\" y=\"167\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten erstellen</text>\n<line x1=\"365\" y1=\"214\" x2=\"609\" y2=\"214\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"205\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">2. Antwort</text>\n<text x=\"487\" y=\"229\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55213 · E_0079</text>\n<text x=\"487\" y=\"242\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0079 — MaBiS-ZP AAÜZ Deaktivierung prüfen</text>\n<line x1=\"365\" y1=\"276\" x2=\"121\" y2=\"276\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"267\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"291\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"365\" y1=\"338\" x2=\"853\" y2=\"338\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"609\" y=\"329\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">4. Weiterleitung der Deaktivierung</text>\n<text x=\"609\" y=\"353\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55214</text>\n<line x1=\"365\" y1=\"400\" x2=\"121\" y2=\"400\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"391\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"415\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n</svg>"} titel="BIKO" />

<a id="abschnitt-schritte"></a>

## Prozessschritte

<Schritt nr="1" anker="schritt-1" richtung="eingehend" kopf={{"links": {"label": "BIKO", "eigen": true}, "rechts": {"label": "NB (ANB)"}}}>

### Deaktivierung eines MABIS-ZP für die monatliche AAÜZ

<Schrittskizze sicht={{"label": "BIKO"}} zeilen={[{"art": "empfangen", "label": "NB (ANB)", "weg": "AS4", "nachrichten": [{"nr": "55212", "titel": "Deaktivierung ZP monatliche AAÜZ"}]}, {"art": "erstellen"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55212](/schnittstellen/202610/pruefi/UTILMD/PI_55212) — Deaktivierung ZP monatliche AAÜZ · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **NB (ANB)** · AS4

</li>

<li data-teil="schnittstelle" data-art="schreiben" data-abgeleitet="ja">

**Schreibende Schnittstelle**
- Vorgang angelegt — `ERSTELLEN_PROZESSDATEN`

Legt im Backend einen neuen Vorgang mit den Daten der eingegangenen Nachricht an.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="2" anker="schritt-2" richtung="ausgehend" kopf={{"links": {"label": "BIKO", "eigen": true}, "rechts": {"label": "NB (ANB)"}}}>

### Antwort

<Schrittskizze sicht={{"label": "BIKO"}} zeilen={[{"art": "senden", "label": "NB (ANB)", "weg": "AS4", "nachrichten": [{"nr": "55213", "titel": "Antwort auf Deaktivierung ZP"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55213](/schnittstellen/202610/pruefi/UTILMD/PI_55213) — Antwort auf Deaktivierung ZP · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht an **NB (ANB)** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `55213` → [E_0079](/referenz/202610/ebd/E_0079) · BIKO · MaBiS-ZP AAÜZ Deaktivierung prüfen

</div>

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — `AKTUALISIEREN_PROZESSDATEN`

Schreibt den bestehenden Vorgang im Backend fort, nachdem die Nachricht erstellt ist.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="4" anker="schritt-4" richtung="ausgehend" kopf={{"links": {"label": "BIKO", "eigen": true}, "rechts": {"label": "BKV (des anfNB)"}}}>

### Weiterleitung der Deaktivierung

<Schrittskizze sicht={{"label": "BIKO"}} zeilen={[{"art": "senden", "label": "BKV (des anfNB)", "weg": "AS4", "nachrichten": [{"nr": "55214", "titel": "Weiterleitung Deaktivierung ZP"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55214](/schnittstellen/202610/pruefi/UTILMD/PI_55214) — Weiterleitung Deaktivierung ZP · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht an **BKV (des anfNB)** · AS4

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — `AKTUALISIEREN_PROZESSDATEN`

Schreibt den bestehenden Vorgang im Backend fort, nachdem die Nachricht erstellt ist.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<details>
<summary>Entscheidungsbäume dieses Prozesses</summary>

| EBD | Name |
|---|---|
| [E_0079](/referenz/202610/ebd/E_0079) | MaBiS-ZP AAÜZ Deaktivierung prüfen |

</details>

<a id="abschnitt-informationen"></a>

## Prozess-Informationen

Wortlaut der Lesefassung, Steckbrief Kap. 17.3.5.2.1, S. 271–272.

<Stepper>
<ol>

<li data-blatt="vorbedingungen">

### Vorbedingungen

- Der ANB hat keine Redispatch-Maßnahme im Netzgebiet, die der BKV (des anfNB) angefordert hat, allerdings ist noch ein MaBiS-ZP für die AAÜZ aktiviert.

</li>

<li data-blatt="ergebnisse">

### Ergebnisse

- Der BIKO kann die Weiterleitung des deaktivierten MaBiS-ZP an den BKV (des anfNB) anstoßen.

</li>

<li data-blatt="fehlerfall">

### Fehlerfall

#### Ergebnis im Fehlerfall

- Im Fehlerfall kann der BKV (des anfNB) den Clearingprozess mit dem ANB einleiten.

</li>

<li data-blatt="anforderungen">

### Weitere Anforderungen

Der MaBiS-ZP kann bis zu einer erneuten Aktivierung für die AAÜZ nach dem Deaktivierungszeitpunkt nicht mehr verwendet werden.

</li>

<li data-blatt="erste-nachricht">

### Erste Nachricht

**NB (ANB)** sendet „Deaktivierung eines MABIS-ZP für die monatliche AAÜZ“ (Schritt 1). Ab hier ist der Beteiligte dieser Seite am Zug.

</li>

<li data-blatt="ziel">

### Ziel

- Der NB hat den MaBiS-ZP für die AAÜZ beim BIKO deaktiviert.
- Der BIKO hat die Deaktivierung des MaBiS-ZP für die AAÜZ zu dem BKV (des anfNB) weitergeleitet und der BKV (des anfNB) hat diese übernommen. Fehlerfälle konnten zwischen den BKV (des anfNB) und NB über ein Clearing geklärt werden.

</li>

</ol>
</Stepper>

<a id="abschnitt-sichten"></a>

## Andere Sichten des Prozesses

Derselbe Prozess, aus den Augen der anderen Beteiligten: dieselben Schritte, jeweils aus deren Sicht gelesen.

- [Sicht ANB](/prozessdoku/202610/NB/MaBiS-deaktivierung-eines-mabis-zp-fuer-die-monatliche-ausfallarbeitsueberfuehrungszeitreihe-aauez-zwischen-nb-und-bkv-anfnb) — Anschlussnetzbetreiber · Marktrolle NB
- [Sicht BKV-ANFNB](/prozessdoku/202610/BKV/MaBiS-deaktivierung-eines-mabis-zp-fuer-die-monatliche-ausfallarbeitsueberfuehrungszeitreihe-aauez-zwischen-nb-und-bkv-anfnb) — Bilanzkreisverantwortlicher des anfordernden Netzbetreibers · Marktrolle BKV

<Hinweisbereich>

*Die Schritte sind die **möglichen** Nachrichten dieses Prozesses, keine Abfolge — die Quelle führt weder Bedingungen noch Alternativen. Das Kästchen am Schritt nennt links die eigene Sicht: **←** empfängt sie, **→** sendet sie. Zugeklappte Schritte laufen zwischen anderen Marktpartnern. Die Nummern sind die der Quelle; wo eine fehlt, fehlt sie dort.*

Die Konnektortabelle führt für diese Schritte keinen Schreibaufruf. Abgeleitet aus dem Prozessverlauf: Mit ihrer Nachricht beginnt der Prozess für die eigene Rolle, der Vorgang entsteht also neu.

Betrifft: [1](#schritt-1)

Für diese Marktrolle liegt kein Schreibkatalog vor; am Schritt steht deshalb nur das Kommando des Schreibaufrufs, ohne Adresse und ohne Knopf.

Betrifft: [1](#schritt-1), [2](#schritt-2), [4](#schritt-4)

</Hinweisbereich>
