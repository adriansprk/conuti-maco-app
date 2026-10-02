# Lieferbeginn — Sicht LFZ

<Kopf rolle="LF" beteiligter="LFZ" festlegung="GPKE" dokument="GPKE Teil 2" kapitel="2.1.2" sparte="Strom" schritte={8} suchtitel="Lieferbeginn — Sicht LFZ (Marktrolle LF) · GPKE Teil 2 · Formatversion 202610" stichworte="Lieferantenwechsel" abschnitte={[{"id": "abschnitt-ablauf", "label": "Prozessablauf"}, {"id": "abschnitt-schritte", "label": "Prozessschritte"}, {"id": "abschnitt-informationen", "label": "Prozess-Informationen"}, {"id": "abschnitt-sichten", "label": "Andere Sichten des Prozesses"}]} />

<Kurzfassung>

Ein LFN meldet beim NB eine Zuordnung des LFN zu einer Marktlokation bzw. Tranche an. Im Zuge des Prozesses
- beendet der NB ggf. die Zuordnung des LFA zur Marktlokation bzw. Tranche.
- hebt der NB ggf. die Zuordnung des LFZ zur Marktlokation bzw. Tranche auf.

</Kurzfassung>

<a id="abschnitt-ablauf"></a>

## Prozessablauf aus Sicht des LF (LFZ)

<Systembild svg={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1004 405\" width=\"1004\" height=\"405\" role=\"img\" aria-labelledby=\"sb-title\" class=\"maco-systembild\">\n<title id=\"sb-title\">Systembild: Lieferbeginn aus Sicht LF</title>\n<defs><marker id=\"sb-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect class=\"sb-lane-kopf\" x=\"16\" y=\"12\" width=\"232\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend-System des Kunden</text>\n<rect class=\"sb-lane-kopf\" x=\"398\" y=\"12\" width=\"264\" height=\"46\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · LFZ</text>\n<rect class=\"sb-lane-kopf\" x=\"812\" y=\"12\" width=\"176\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"900\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Marktpartner</text>\n<line x1=\"323\" y1=\"58\" x2=\"323\" y2=\"393\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"737\" y1=\"58\" x2=\"737\" y2=\"393\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"80\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">13. Aufhebung der</text>\n<text x=\"530\" y=\"115\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Zuordnung des LFZ zur</text>\n<text x=\"530\" y=\"130\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Marklokation bzw. Tranc…</text>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"93\" r=\"5\"/><line x1=\"900\" y1=\"98\" x2=\"900\" y2=\"110\"/><line x1=\"893\" y1=\"102\" x2=\"907\" y2=\"102\"/><line x1=\"900\" y1=\"110\" x2=\"894\" y2=\"120\"/><line x1=\"900\" y1=\"110\" x2=\"906\" y2=\"120\"/></g>\n<text x=\"900\" y=\"142\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"878\" y1=\"111\" x2=\"628\" y2=\"111\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"103\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"127\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">55038</text>\n<rect class=\"sb-kasten sb-aperak_lesen\" x=\"432\" y=\"169\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"189\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Daten für die</text>\n<text x=\"530\" y=\"204\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Eingangsprüfung laden</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"143\" x2=\"530\" y2=\"169\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-aperak_lesen\" x=\"34\" y=\"169\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"189\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">2 Lese-Schnittstellen</text>\n<text x=\"132\" y=\"204\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">aufgerufen</text>\n<line x1=\"432\" y1=\"193\" x2=\"230\" y2=\"193\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"185\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<text x=\"331\" y=\"209\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">je einzeln am Schritt</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"243\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"263\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z10, Z17,</text>\n<text x=\"530\" y=\"278\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Z18, Z44</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"217\" x2=\"530\" y2=\"243\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-schreiben\" x=\"432\" y=\"317\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"337\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"291\" x2=\"530\" y2=\"317\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-schreiben\" x=\"34\" y=\"317\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"337\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten erstellen</text>\n<line x1=\"432\" y1=\"333\" x2=\"230\" y2=\"333\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"325\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n</svg>"} gesamt={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1218 685\" width=\"1218\" height=\"685\" role=\"img\" aria-labelledby=\"sd-title\" class=\"maco-sequence\">\n<title id=\"sd-title\">Sequenzdiagramm: Lieferbeginn aus Sicht LF</title>\n<defs><marker id=\"sd-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect x=\"16\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"121\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend (Kunde)</text>\n<line x1=\"121\" y1=\"64\" x2=\"121\" y2=\"673\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"260\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"365\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · LFZ</text>\n<line x1=\"365\" y1=\"64\" x2=\"365\" y2=\"673\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"504\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"609\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">LFN</text>\n<line x1=\"609\" y1=\"64\" x2=\"609\" y2=\"673\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"748\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"853\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"853\" y1=\"64\" x2=\"853\" y2=\"673\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"992\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"1097\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">LFA</text>\n<line x1=\"1097\" y1=\"64\" x2=\"1097\" y2=\"673\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"609\" y1=\"90\" x2=\"853\" y2=\"90\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"731\" y=\"81\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">1. Anmeldung einer Zuordnung des LFN zur Marktlo…</text>\n<text x=\"731\" y=\"105\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55001, 55077</text>\n<line x1=\"853\" y1=\"152\" x2=\"609\" y2=\"152\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"731\" y=\"143\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">2. Information über existierende Zuordnung</text>\n<text x=\"731\" y=\"167\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55036</text>\n<line x1=\"853\" y1=\"214\" x2=\"1097\" y2=\"214\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"975\" y=\"205\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">3. Anfrage zur Beendigung der Zuordnung des LFA…</text>\n<text x=\"975\" y=\"229\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55010</text>\n<line x1=\"1097\" y1=\"276\" x2=\"853\" y2=\"276\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"975\" y=\"267\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">4. Antwort auf Anfrage zur Beendigung der Zuordn…</text>\n<text x=\"975\" y=\"291\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55011, 55012 · E_0624</text>\n<text x=\"975\" y=\"304\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0624 — Anfrage zur Beendigung der Zuordnung prüfen</text>\n<line x1=\"853\" y1=\"338\" x2=\"609\" y2=\"338\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"731\" y=\"329\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">5. Zuordnung des LFN zur Marktlokation bzw. Tran…</text>\n<text x=\"731\" y=\"353\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55002, 55078 · E_0623</text>\n<text x=\"731\" y=\"366\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0623 — Lieferbeginn prüfen</text>\n<line x1=\"853\" y1=\"400\" x2=\"609\" y2=\"400\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"731\" y=\"391\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">6. Ablehnung der Anmeldung einer Zuordnung des L…</text>\n<text x=\"731\" y=\"415\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55003, 55080 · E_0622, E_0623</text>\n<text x=\"731\" y=\"428\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0622 — Prüfen, ob Anmeldung direkt ablehnbar</text>\n<text x=\"731\" y=\"441\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0623 — Lieferbeginn prüfen</text>\n<line x1=\"853\" y1=\"475\" x2=\"1097\" y2=\"475\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"975\" y=\"466\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">10. Beendigung der Zuordnung des LFA zur Marktlok…</text>\n<text x=\"975\" y=\"490\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55037</text>\n<line x1=\"853\" y1=\"537\" x2=\"365\" y2=\"537\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"609\" y=\"528\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">13. Aufhebung der Zuordnung des LFZ zur Marklokat…</text>\n<text x=\"609\" y=\"552\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55038</text>\n<line x1=\"365\" y1=\"599\" x2=\"121\" y2=\"599\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"590\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<text x=\"243\" y=\"614\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten erstellen</text>\n</svg>"} titel="LFZ" />

<a id="abschnitt-schritte"></a>

## Prozessschritte

<Schritt nr="1" anker="schritt-1" richtung="fremd" kopf={{"links": {"label": "LFN", "eigen": false}, "rechts": {"label": "NB"}}}>

### Anmeldung einer Zuordnung des LFN zur Marktlokation bzw. Tranche

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55001](/schnittstellen/202610/pruefi/UTILMD/PI_55001) — Anmeldung verb. MaLo · AS4
- [55077](/schnittstellen/202610/pruefi/UTILMD/PI_55077) — Anmeldung erz. MaLo · AS4

</div>

</Schritt>

<Schritt nr="2" anker="schritt-2" richtung="fremd" kopf={{"links": {"label": "NB", "eigen": false}, "rechts": {"label": "LFN"}}}>

### Information über existierende Zuordnung

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55036](/schnittstellen/202610/pruefi/UTILMD/PI_55036) — Existierende Zuordnung · AS4

</div>

</Schritt>

<Schritt nr="3" anker="schritt-3" richtung="fremd" kopf={{"links": {"label": "NB", "eigen": false}, "rechts": {"label": "LFA"}}}>

### Anfrage zur Beendigung der Zuordnung des LFA zur Marktlokation bzw. Tranche

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55010](/schnittstellen/202610/pruefi/UTILMD/PI_55010) — Anfrage zur Beendigung der Zuordnung · AS4

</div>

</Schritt>

<Schritt nr="4" anker="schritt-4" richtung="fremd" kopf={{"links": {"label": "LFA", "eigen": false}, "rechts": {"label": "NB"}}}>

### Antwort auf Anfrage zur Beendigung der Zuordnung des LFA zur Marktlokation bzw. Tranche

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55011](/schnittstellen/202610/pruefi/UTILMD/PI_55011) — Bestätigung Beendigung der Zuordnung · AS4
- [55012](/schnittstellen/202610/pruefi/UTILMD/PI_55012) — Ablehnung Beendigung der Zuordnung · AS4

</div>

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `55011`, `55012` → [E_0624](/referenz/202610/ebd/E_0624) · LF · Anfrage zur Beendigung der Zuordnung prüfen

</div>

</Schritt>

<Schritt nr="5" anker="schritt-5" richtung="fremd" kopf={{"links": {"label": "NB", "eigen": false}, "rechts": {"label": "LFN"}}}>

### Zuordnung des LFN zur Marktlokation bzw. Tranche

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55002](/schnittstellen/202610/pruefi/UTILMD/PI_55002) — Bestätigung Anmeldung verb. MaLo · AS4
- [55078](/schnittstellen/202610/pruefi/UTILMD/PI_55078) — Bestätigung Anmeldung erz. MaLo · AS4

</div>

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `55002`, `55078` → [E_0623](/referenz/202610/ebd/E_0623) · NB · Lieferbeginn prüfen

</div>

</Schritt>

<Schritt nr="6" anker="schritt-6" richtung="fremd" kopf={{"links": {"label": "NB", "eigen": false}, "rechts": {"label": "LFN"}}}>

### Ablehnung der Anmeldung einer Zuordnung des LFN zur Marktlokation bzw. Tranche

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55003](/schnittstellen/202610/pruefi/UTILMD/PI_55003) — Ablehnung Anmeldung verb. MaLo · AS4
- [55080](/schnittstellen/202610/pruefi/UTILMD/PI_55080) — Ablehnung Anmeldung erz. MaLo · AS4

</div>

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `55003`, `55080` → [E_0622](/referenz/202610/ebd/E_0622) · NB · Prüfen, ob Anmeldung direkt ablehnbar
- `55003`, `55080` → [E_0623](/referenz/202610/ebd/E_0623) · NB · Lieferbeginn prüfen

</div>

</Schritt>

<Schritt nr="10" anker="schritt-10" richtung="fremd" kopf={{"links": {"label": "NB", "eigen": false}, "rechts": {"label": "LFA"}}}>

### Beendigung der Zuordnung des LFA zur Marktlokation bzw. Tranche

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55037](/schnittstellen/202610/pruefi/UTILMD/PI_55037) — Beendigung der Zuordnung · AS4

</div>

</Schritt>

<Schritt nr="13" anker="schritt-13" richtung="eingehend" kopf={{"links": {"label": "LFZ", "eigen": true}, "rechts": {"label": "NB"}}}>

### Aufhebung der Zuordnung des LFZ zur Marklokation bzw. Tranche

<Schrittskizze sicht={{"label": "LFZ"}} zeilen={[{"art": "empfangen", "label": "NB", "weg": "AS4", "nachrichten": [{"nr": "55038", "titel": "Aufhebung einer zuk. Zuordnung"}]}, {"art": "lesen_aperak", "schnittstellen": [{"label": "Marktlokation lesen"}, {"label": "Tranche lesen"}]}, {"art": "aperak", "werte": ["Z10", "Z17", "Z18", "Z44"]}, {"art": "erstellen"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55038](/schnittstellen/202610/pruefi/UTILMD/PI_55038) — Aufhebung einer zuk. Zuordnung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **NB** · AS4

</li>

<li data-teil="lesen" data-stufe="aperak">

**Daten für die Eingangsprüfung laden**
- [Marktlokation lesen](/api/202610/backend-lesen/getmarketlocationbasic#marktlokation-lesen) `GET /getMarketLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getMarketLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": false, "defaultValue": "MALO", "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": false, "defaultValue": "2024-06-28T12:18:00Z", "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_MARKTLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Tranche lesen](/api/202610/backend-lesen/gettranchebasic#tranche-lesen) `GET /getTrancheBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getTrancheBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

</li>

<li data-teil="aperak">

**Aperak-Prüfungen**
- `55038` → `Z10` — Aperak Prüfung: Ist Lokation bekannt ?
- `55038` → `Z17`
- `55038` → `Z18`
- `55038` → `Z44` — Aperak Prüfung: Stimmt Objekteigenschaft überein?

</li>

<li data-teil="schnittstelle" data-art="schreiben">

**Schreibende Schnittstelle**
- Vorgang angelegt — [Prozessdaten erstellen](/api/202610/backend-schreiben-lf/createprocessdata#prozessdaten-erstellen) `POST /createProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/createProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": false, "defaultValue": "ERSTELLEN_PROZESSDATEN", "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"MARKTLOKATION\": [\n      {\n        \"beteiligterMarktpartner\": {\n          \"boTyp\": \"MARKTTEILNEHMER\",\n          \"rollencodenummer\": \"9903790000002\",\n          \"rollencodetyp\": \"BDEW\",\n          \"versionStruktur\": \"1\"\n        },\n        \"boTyp\": \"MARKTLOKATION\",\n        \"marktlokationsId\": \"10017211334\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"NETZNUTZUNGSVERTRAG\": [\n      {\n        \"boTyp\": \"VERTRAG\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\",\n        \"vertragsart\": \"NETZNUTZUNGSVERTRAG\",\n        \"vertragsbeginn\": \"2026-04-30T22:00:00Z\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9900321000005\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"datenaustauschreferenz\": \"607048\",\n    \"dokumentennummer\": \"893296BGM\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9903790000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"E02\",\n    \"nachrichtendatum\": \"2026-10-02T11:00:00Z\",\n    \"nachrichtenreferenznummer\": \"893296\",\n    \"pruefidentifikator\": \"55038\",\n    \"sparte\": \"STROM\",\n    \"transaktionsgrund\": \"ZH1\",\n    \"transaktionsgrundergaenzung\": \"ZW4\",\n    \"vertragsbeginn\": \"2026-04-30T22:00:00Z\",\n    \"vorgangsnummer\": \"1631102530\"\n  }\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Legt im Backend einen neuen Vorgang mit den Daten der eingegangenen Nachricht an.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<details>
<summary>Entscheidungsbäume der anderen Beteiligten</summary>

| EBD | Name |
|---|---|
| [E_0622](/referenz/202610/ebd/E_0622) | Prüfen, ob Anmeldung direkt ablehnbar |
| [E_0623](/referenz/202610/ebd/E_0623) | Lieferbeginn prüfen |
| [E_0624](/referenz/202610/ebd/E_0624) | Anfrage zur Beendigung der Zuordnung prüfen |

</details>

<a id="abschnitt-informationen"></a>

## Prozess-Informationen

Wortlaut der Lesefassung, Steckbrief Kap. 2.1.1, S. 12–15.

<Stepper>
<ol>

<li data-blatt="vorbedingungen">

### Vorbedingungen

- Im Fall einer verbrauchenden Marktlokation:
  - Abschluss eines Energieliefervertrags zwischen LFN und dem Letztverbraucher.
- Im Fall einer erzeugenden Marktlokation bzw. einer Tranche:
  - Abschluss eines Stromabnahmevertrags zwischen LFN und dem EZ. Es werden dabei drei Geschäftsvorfälle betrachtet:
    - Geschäftsvorfall 1: Der LFN wird einer Marktlokation vollständig zugeordnet (vollständige (100%ige) Zuordnung). Dieser Geschäftsvorfall ist auch für die Änderung von einer tranchierten Marktlokation in eine nicht tranchierte Marktlokation anzuwenden.
    - Geschäftsvorfall 2: Der LFN wird einer bestehenden Tranche vollständig zugeordnet (vollständige (100%ige) Zuordnung). Dieser Geschäftsvorfall ist bei einem direkten Übergang, d. h. lückenlosem Zuordnungsende und -beginn und unter Beibehaltung der Tranche, anzuwenden.
    - Geschäftsvorfall 3: Der LFN wird einer neu zu bildenden Tranche zugeordnet (anteiliger Zuordnungsvorgang unter Bildung neuer Tranchen). Zudem ist eine Änderung der dem LF zugeordneten Tranchengröße mit diesem Prozess/Geschäftsvorfall 3 zu melden.
  - Der bisherige und neue EZ müssen identisch sein.
  - Die Energie einer Marktlokation, die vollständig oder anteilig zur Veräußerungsform einer DV zugeordnet werden soll, ist mit einer viertelstündlichen Auflösung zu messen.
  - Der Use-Case ist nicht durch das Unternehmen Netzbetreiber in seiner Rolle als LF zu starten.
- Eine Zuordnungsermächtigung nach den Prozessen der MaBiS für den vom LFN genutzten BK liegt beim NB vor.
- Es handelt sich nicht um die erstmalige Inbetriebnahme einer Marktlokation (Neuanlage).
- Die MaLo-ID der Marktlokation ist bekannt bzw. im Geschäftsvorfall 2 ist die MaLo-ID der Tranche bekannt.

</li>

<li data-blatt="ergebnisse">

### Ergebnisse

- Im Fall einer verbrauchenden Marktlokation:
  - Der NB führt die Use-Cases „[Abrechnungsdaten Netznutzungsabrechnung](/prozessdoku/202610/LF/GPKE-Teil2-abrechnungsdaten-netznutzungsabrechnung)“ und „[Abrechnungsdaten Bilanzkreisabrechnung](/prozessdoku/202610/LF/GPKE-Teil2-abrechnungsdaten-bilanzkreisabrechnung)“ aus.
  - Etwa entstehende Zuordnungslücken werden vom NB durch Zuordnung des E/G zur Marktlokation in Anwendung des Use-Cases „[Beginn der Ersatz-/Grundversorgung](/prozessdoku/202610/LF/GPKE-Teil2-beginn-der-ersatz-grundversorgung)“ geschlossen.
  - Sofern die Marktlokation gesperrt ist, führt der NB den Use-Case „[Wiederherstellung der Anschlussnutzung bei Lieferbeginn](/prozessdoku/202610/MSB/GPKE-Teil2-wiederherstellung-der-anschlussnutzung-bei-lieferbeginn)“ aus.
- Im Fall einer erzeugenden Marktlokation bzw. einer Tranche:
  - Der NB führt den Use-Case „[Abrechnungsdaten Bilanzkreisabrechnung](/prozessdoku/202610/LF/GPKE-Teil2-abrechnungsdaten-bilanzkreisabrechnung)“ aus.
  - Etwa entstehende Zuordnungslücken werden vom NB im Rahmen des Use-Cases „Herstellung einer 100% LF-Zuordnung zu einer erzeugenden Marktlokation“ geschlossen.
- Der NB führt den Use-Case „Stammdatenänderung“ (hier: SD „[Stammdatenänderung vom NB (verantwortlich) ausgehend](/prozessdoku/202610/LF/GPKE-Teil4-stammdatenaenderung-vom-nb-verantwortlich-ausgehend)“) (GPKE Teil 4) durch.
- Der NB versendet die Berechnungsformel an den LFN.
- Der NB führt den Use-Case „[Einrichtung der Konfigurationen aufgrund einer Zuordnung eines LF zu einer Marktlokation bzw. Tranche](/prozessdoku/202610/MSB/GPKE-Teil3-einrichtung-der-konfigurationen-aufgrund-einer-zuordnung-eines-lf-zu-einer-marktlokation-bzw-tranche)“ (GPKE Teil 3) aus.
- Der LFN führt den Use-Case „Stammdatenänderung“ (hier: SD „[Stammdatenänderung vom LF (verantwortlich) ausgehend](/prozessdoku/202610/LF/GPKE-Teil4-stammdatenaenderung-vom-lf-verantwortlich-ausgehend)“) (GPKE Teil 4) durch.

</li>

<li data-blatt="fehlerfall">

### Fehlerfall

#### Ergebnis im Fehlerfall

- Der LFN wurde der Marktlokation bzw. Tranche nicht zugeordnet.
- Der LFA bleibt der Marktlokation bzw. Tranche zugeordnet, sofern für diesen nicht bereits die Zuordnung im Rahmen eines anderen Use-Cases (z.B. „Lieferende von LF an NB) beendet wurde.
- Im Fall einer verbrauchenden Marktlokation: Der NB führt ggf. den Use-Case „[Beginn der Ersatz-/Grundversorgung](/prozessdoku/202610/LF/GPKE-Teil2-beginn-der-ersatz-grundversorgung)“ aus.
- Im Fall einer erzeugenden Marktlokation bzw. einer Tranche: Der NB führt ggf. den Use-Case „Herstellung einer 100% LF-Zuordnung zu einer erzeugenden Marktlokation“ aus.
- Der LFN sendet bei Bedarf erneut eine Anmeldung an den NB.

#### Fehlerfälle

- Es handelt sich um die erstmalige Inbetriebnahme einer Marktlokation (Neuanlage).
- Im Fall einer erzeugenden Marktlokation bzw. einer Tranche:
  - Der bisherige und neue EZ sind nicht identisch.
  - Die Energie einer Marktlokation, die vollständig oder anteilig zur Veräußerungsform einer DV zugeordnet werden soll, ist nicht mit einer viertelstündlichen Auflösung messbar.
  - Der Use-Case wird durch das Unternehmen Netzbetreiber in seiner Rolle als LF gestartet.
- Eine Zuordnungsermächtigung nach den Prozessen der MaBiS für den vom LFN genutzten BK liegt beim NB nicht vor.

</li>

<li data-blatt="anforderungen">

### Weitere Anforderungen

- Zuordnungslücken sind dadurch zu vermeiden, dass An- und Abmeldung zeitlich aufeinander abgestimmt werden.
- Hinweis: Ein Erzeugerwechsel an einer erzeugenden Marktlokation oder Anlagenbetreiberwechsel an einer technischen Ressource wird nicht im Rahmen der hier beschriebenen Prozesse abgewickelt. Deren bilaterale Abwicklung zwischen NB und EZ erfolgt gemäß den einschlägigen Bestimmungen der NB.
- Hinweis: Die Zuordnung des LF zur Marktlokation bzw. Tranche bei einer Inbetriebnahme einer Marktlokation (Neuanlage) findet über den Use-Case „[Neuanlage](/prozessdoku/202610/LF/GPKE-Teil2-neuanlage)“, „[Beginn der Ersatz-/Grundversorgung](/prozessdoku/202610/LF/GPKE-Teil2-beginn-der-ersatz-grundversorgung)“ oder „Herstellung einer 100% LF-Zuordnung zu einer erzeugenden Marktlokation“ statt.
- Hinweis: Sofern die zum Zuordnungsbeginn vorhandene Gerätetechnik die Anmeldung nicht ermöglicht, ist eine entsprechende Änderung der Gerätetechnik durch den LFN bzw. Letztverbraucher bzw. EZ beim MSB zu veranlassen. Der LFN kann die Änderung der Gerätetechnik über den WiM-Use-Case zur Messlokationsänderung (WiM Teil 1) beauftragen.
- Hinweis zu erzeugenden Marktlokationen bzw. zu Tranchen: Der LF wendet für eine Änderung der Veräußerungsform (ohne gleichzeitige Zuordnung des LF zur erzeugenden Marktlokation bzw. zur Tranche) den Use-Case "Bestellung einer Änderung von Abrechnungsdaten" an.

</li>

<li data-blatt="anlass">

### Anlass

- Im Fall einer verbrauchenden Marktlokation:
  - Lieferantenwechsel ohne gleichzeitigen Einzug des Letztverbrauchers
  - Lieferantenwechsel mit gleichzeitigem Einzug des Letztverbrauchers
  - Zuordnung des bisherigen LF ohne gleichzeitigen Einzug des Letztverbrauchers (nach einer Beendigung der Zuordnung des LF zur Marktlokation, z.B. aufgrund des Use-Cases "Lieferende von LF an NB")
  - Zuordnung des bisherigen LF mit gleichzeitigem Einzug des Letztverbrauchers.
- Im Fall einer erzeugenden Marktlokation bzw. einer Tranche:
  - Lieferantenwechsel ohne Erzeugerwechsel
  - Zuordnung des bisherigen LF ohne Erzeugerwechsel (nach einer Beendigung der Zuordnung des LF zur Marktlokation bzw. Tranche, z.B. aufgrund des Use-Cases "Lieferende von LF an NB").

**Vorher läuft:** [Abrechnungsdaten Netznutzungsabrechnung](/prozessdoku/202610/LF/GPKE-Teil2-abrechnungsdaten-netznutzungsabrechnung), [Ermittlung der MaLo-ID der Marktlokation](/prozessdoku/202610/LF/GPKE-Teil2-ermittlung-der-malo-id-der-marktlokation), [Neuanlage](/prozessdoku/202610/LF/GPKE-Teil2-neuanlage) — diese Prozesse nennen den hier gezeigten in ihrem Ergebnis.

</li>

<li data-blatt="erste-nachricht">

### Erste Nachricht

**NB** sendet „Aufhebung der Zuordnung des LFZ zur Marklokation bzw. Tranche“ (Schritt 13). Ab hier ist der Beteiligte dieser Seite am Zug.

</li>

<li data-blatt="ziel">

### Ziel

Der LFN ist der Marktlokation bzw. Tranche zugeordnet.

</li>

</ol>
</Stepper>

<a id="abschnitt-sichten"></a>

## Andere Sichten des Prozesses

Derselbe Prozess, aus den Augen der anderen Beteiligten: dieselben Schritte, jeweils aus deren Sicht gelesen.

- [Sicht LFA](/prozessdoku/202610/LF--LFA/GPKE-Teil2-lieferbeginn) — der abgebende Lieferant · Marktrolle LF
- [Sicht LFN](/prozessdoku/202610/LF--LFN/GPKE-Teil2-lieferbeginn) — der aufnehmende Lieferant · Marktrolle LF
- [Sicht NB](/prozessdoku/202610/NB/GPKE-Teil2-lieferbeginn) — NB

<Hinweisbereich>

*Die Schritte sind die **möglichen** Nachrichten dieses Prozesses, keine Abfolge — die Quelle führt weder Bedingungen noch Alternativen. Das Kästchen am Schritt nennt links die eigene Sicht: **←** empfängt sie, **→** sendet sie. Zugeklappte Schritte laufen zwischen anderen Marktpartnern. Die Nummern sind die der Quelle; wo eine fehlt, fehlt sie dort.*

</Hinweisbereich>
