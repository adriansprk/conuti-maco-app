# Störungsbehebung in der Messlokation — Sicht NB

<Kopf rolle="NB" beteiligter="NB" festlegung="WiM" dokument="WiM Strom Teil 2" kapitel="1.2" sparte="Strom" schritte={11} suchtitel="Störungsbehebung in der Messlokation — Sicht NB · WiM Strom Teil 2 · Formatversion 202610" abschnitte={[{"id": "abschnitt-ablauf", "label": "Prozessablauf"}, {"id": "abschnitt-schritte", "label": "Prozessschritte"}, {"id": "abschnitt-informationen", "label": "Prozess-Informationen"}, {"id": "abschnitt-sichten", "label": "Andere Sichten des Prozesses"}]} />

<Kurzfassung>

Der Prozess beschreibt die Interaktionen zwischen den Marktakteuren im Falle einer festgestellten oder vermuteten Störung an den technischen Einrichtungen der Messlokation. Der Störungsmelder teilt dem MSB der Messlokation eine Störung der Messung mit. Der MSB der Messlokation informiert bei einer vorhandenen Störung die MSB der betroffenen Marktlokationen. Der MSB der jeweilig betroffenen Marktlokation muss nach Vorliegen der Informationen alle berechtigten Rollen für diese Marktlokation berechtigten Marktteilnehmer über die Störung informieren. Der MSB ist verpflichtet, die Störung an der Messlokation unverzüglich zu beseitigen und so einen den Regeln der Technik entsprechenden Betrieb derselben zu gewährleisten. Das gleiche Prozedere ist ebenfalls durchzuführen, nachdem die Störung behoben wurde.

</Kurzfassung>

<a id="abschnitt-ablauf"></a>

## Prozessablauf aus Sicht des NB

<Systembild svg={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1004 542\" width=\"1004\" height=\"542\" role=\"img\" aria-labelledby=\"sb-title\" class=\"maco-systembild\">\n<title id=\"sb-title\">Systembild: Störungsbehebung in der Messlokation aus Sicht NB</title>\n<defs><marker id=\"sb-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect class=\"sb-lane-kopf\" x=\"16\" y=\"12\" width=\"232\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend-System des Kunden</text>\n<rect class=\"sb-lane-kopf\" x=\"398\" y=\"12\" width=\"264\" height=\"46\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · NB</text>\n<rect class=\"sb-lane-kopf\" x=\"812\" y=\"12\" width=\"176\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"900\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Marktpartner</text>\n<line x1=\"323\" y1=\"58\" x2=\"323\" y2=\"530\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"737\" y1=\"58\" x2=\"737\" y2=\"530\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"80\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">4. Information über Störung</text>\n<text x=\"530\" y=\"115\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">an betroffener Marktlokation</text>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"86\" r=\"5\"/><line x1=\"900\" y1=\"91\" x2=\"900\" y2=\"103\"/><line x1=\"893\" y1=\"95\" x2=\"907\" y2=\"95\"/><line x1=\"900\" y1=\"103\" x2=\"894\" y2=\"113\"/><line x1=\"900\" y1=\"103\" x2=\"906\" y2=\"113\"/></g>\n<text x=\"900\" y=\"135\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">MSB (entspricht MSB a…</text>\n<line x1=\"878\" y1=\"104\" x2=\"628\" y2=\"104\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"96\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"120\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">23011</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"163\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"183\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z10, Z16,</text>\n<text x=\"530\" y=\"198\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Z17, Z18</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"128\" x2=\"530\" y2=\"163\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-schreiben\" x=\"432\" y=\"237\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"257\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"211\" x2=\"530\" y2=\"237\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-schreiben sb-abgeleitet\" x=\"34\" y=\"237\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"257\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten erstellen</text>\n<line x1=\"432\" y1=\"253\" x2=\"230\" y2=\"253\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"245\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"301\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"321\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">9. Information über Ergebnis</text>\n<text x=\"530\" y=\"336\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">der betroffenen</text>\n<text x=\"530\" y=\"351\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Marktlokation</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"270\" x2=\"530\" y2=\"301\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"314\" r=\"5\"/><line x1=\"900\" y1=\"319\" x2=\"900\" y2=\"331\"/><line x1=\"893\" y1=\"323\" x2=\"907\" y2=\"323\"/><line x1=\"900\" y1=\"331\" x2=\"894\" y2=\"341\"/><line x1=\"900\" y1=\"331\" x2=\"906\" y2=\"341\"/></g>\n<text x=\"900\" y=\"363\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">MSB (entspricht MSB a…</text>\n<line x1=\"878\" y1=\"332\" x2=\"628\" y2=\"332\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"324\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"348\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">23012</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"390\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"410\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z33</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"364\" x2=\"530\" y2=\"390\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"454\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"474\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"423\" x2=\"530\" y2=\"454\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben sb-abgeleitet\" x=\"34\" y=\"454\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"474\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"470\" x2=\"230\" y2=\"470\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"462\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n</svg>"} gesamt={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1706 920\" width=\"1706\" height=\"920\" role=\"img\" aria-labelledby=\"sd-title\" class=\"maco-sequence\">\n<title id=\"sd-title\">Sequenzdiagramm: Störungsbehebung in der Messlokation aus Sicht NB</title>\n<defs><marker id=\"sd-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect x=\"16\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"121\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend (Kunde)</text>\n<line x1=\"121\" y1=\"64\" x2=\"121\" y2=\"908\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"260\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"365\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · NB</text>\n<line x1=\"365\" y1=\"64\" x2=\"365\" y2=\"908\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"504\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"609\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Störungsmelder</text>\n<line x1=\"609\" y1=\"64\" x2=\"609\" y2=\"908\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"748\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"853\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">MSB (entspricht MSB am Ob…</text>\n<line x1=\"853\" y1=\"64\" x2=\"853\" y2=\"908\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"992\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"1097\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">MSB (entspricht MSB am Ob…</text>\n<line x1=\"1097\" y1=\"64\" x2=\"1097\" y2=\"908\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"1236\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"1341\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">LF</text>\n<line x1=\"1341\" y1=\"64\" x2=\"1341\" y2=\"908\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"1480\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"1585\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">ÜNB</text>\n<line x1=\"1585\" y1=\"64\" x2=\"1585\" y2=\"908\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"609\" y1=\"90\" x2=\"853\" y2=\"90\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"731\" y=\"81\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">1. Meldung einer Störung</text>\n<text x=\"731\" y=\"105\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 23001</text>\n<line x1=\"853\" y1=\"152\" x2=\"609\" y2=\"152\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"731\" y=\"143\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">2. Antwort</text>\n<text x=\"731\" y=\"167\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 23003, 23004</text>\n<line x1=\"853\" y1=\"214\" x2=\"1097\" y2=\"214\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"975\" y=\"205\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">3. Information über Störung an Messlokation</text>\n<text x=\"975\" y=\"229\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 23005</text>\n<line x1=\"1097\" y1=\"276\" x2=\"365\" y2=\"276\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"731\" y=\"267\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">4. Information über Störung an betroffener Markt…</text>\n<text x=\"731\" y=\"291\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 23011</text>\n<line x1=\"365\" y1=\"338\" x2=\"121\" y2=\"338\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"329\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<text x=\"243\" y=\"353\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten erstellen</text>\n<line x1=\"1097\" y1=\"400\" x2=\"1341\" y2=\"400\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"1219\" y=\"391\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">5. Information über Störung an betroffener Markt…</text>\n<text x=\"1219\" y=\"415\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 23011</text>\n<line x1=\"1097\" y1=\"462\" x2=\"1585\" y2=\"462\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"1341\" y=\"453\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">6. Information über Störung an betroffener Markt…</text>\n<text x=\"1341\" y=\"477\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 23011</text>\n<line x1=\"853\" y1=\"524\" x2=\"609\" y2=\"524\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"731\" y=\"515\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">7. Mitteilung Ergebnis</text>\n<text x=\"731\" y=\"539\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 23008</text>\n<line x1=\"853\" y1=\"586\" x2=\"1097\" y2=\"586\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"975\" y=\"577\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">8. Information über Ergebnis an Messlokation</text>\n<text x=\"975\" y=\"601\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 23009</text>\n<line x1=\"1097\" y1=\"648\" x2=\"365\" y2=\"648\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"731\" y=\"639\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">9. Information über Ergebnis der betroffenen Mar…</text>\n<text x=\"731\" y=\"663\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 23012</text>\n<line x1=\"365\" y1=\"710\" x2=\"121\" y2=\"710\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"701\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"725\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"1097\" y1=\"772\" x2=\"1341\" y2=\"772\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"1219\" y=\"763\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">10. Information über Ergebnis der betroffenen Mar…</text>\n<text x=\"1219\" y=\"787\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 23012</text>\n<line x1=\"1097\" y1=\"834\" x2=\"1585\" y2=\"834\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"1341\" y=\"825\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">11. Information über Ergebnis der betroffenen Mar…</text>\n<text x=\"1341\" y=\"849\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 23012</text>\n</svg>"} titel="NB" />

<a id="abschnitt-schritte"></a>

## Prozessschritte

<Schritt nr="1" anker="schritt-1" richtung="fremd" kopf={{"links": {"label": "Störungsmelder", "eigen": false}, "rechts": {"label": "MSB (entspricht MSB am Objekt Messlokation)"}}}>

### Meldung einer Störung

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [23001](/schnittstellen/202610/pruefi/INSRPT/PI_23001) — Störungsmeldung · AS4

</div>

</Schritt>

<Schritt nr="2" anker="schritt-2" richtung="fremd" kopf={{"links": {"label": "MSB (entspricht MSB am Objekt Messlokation)", "eigen": false}, "rechts": {"label": "Störungsmelder"}}}>

### Antwort

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [23003](/schnittstellen/202610/pruefi/INSRPT/PI_23003) — Ablehnung · AS4
- [23004](/schnittstellen/202610/pruefi/INSRPT/PI_23004) — Bestätigung · AS4

</div>

</Schritt>

<Schritt nr="3" anker="schritt-3" richtung="fremd" kopf={{"links": {"label": "MSB (entspricht MSB am Objekt Messlokation)", "eigen": false}, "rechts": {"label": "MSB (entspricht MSB am Objekt Marktlokation)"}}}>

### Information über Störung an Messlokation

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [23005](/schnittstellen/202610/pruefi/INSRPT/PI_23005) — Informationsmeldung · AS4

</div>

</Schritt>

<Schritt nr="4" anker="schritt-4" richtung="eingehend" kopf={{"links": {"label": "NB", "eigen": true}, "rechts": {"label": "MSB (entspricht MSB am Objekt Marktlokation)"}}}>

### Information über Störung an betroffener Marktlokation

<Schrittskizze sicht={{"label": "NB"}} zeilen={[{"art": "empfangen", "label": "MSB (entspricht MSB am Objekt Marktlokation)", "weg": "AS4", "nachrichten": [{"nr": "23011", "titel": "Informationsmeldung"}]}, {"art": "aperak", "werte": ["Z10", "Z16", "Z17", "Z18"]}, {"art": "erstellen"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [23011](/schnittstellen/202610/pruefi/INSRPT/PI_23011) — Informationsmeldung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **MSB (entspricht MSB am Objekt Marktlokation)** · AS4

</li>

<li data-teil="aperak">

**Aperak-Prüfungen**
- `23011` → `Z10`
- `23011` → `Z16`
- `23011` → `Z17`
- `23011` → `Z18`

</li>

<li data-teil="schnittstelle" data-art="schreiben" data-abgeleitet="ja">

**Schreibende Schnittstelle**
- Vorgang angelegt — [Prozessdaten erstellen](/api/202610/backend-schreiben-nb/createprocessdata#prozessdaten-erstellen) `POST /createProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/createProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "ERSTELLEN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"STATUSMITTEILUNG\": [\n      {\n        \"boTyp\": \"STATUSMITTEILUNG\",\n        \"positionsdaten\": [\n          {\n            \"auftragsstatus\": \"GESTOERT\",\n            \"enddatum\": \"2023-03-30T15:47:00Z\",\n            \"fehlerbeschreibung\": {\n              \"beschreibung1\": \"Test123456\"\n            },\n            \"lokationsId\": \"50074561222\",\n            \"positionsnummer\": 1,\n            \"referenzMelo\": \"DE0032106765712000000000000000054\",\n            \"verwendungAb\": \"2023-03-30T15:47:00Z\"\n          }\n        ],\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"marktrolle\": \"MSB\",\n      \"rollencodenummer\": \"9904446000007\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"datenaustauschreferenz\": \"LGO8FPVF\",\n    \"dokumentennummer\": \"BGMLGO2Q0VF\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"marktrolle\": \"NB\",\n      \"rollencodenummer\": \"9900321000005\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"4\",\n    \"nachrichtendatum\": \"2023-03-30T15:47:00Z\",\n    \"nachrichtenreferenznummer\": \"UNHLGGEOGSZ\",\n    \"pruefidentifikator\": \"23011\",\n    \"sparte\": \"STROM\",\n    \"vorgangsnummer\": \"202303301531\"\n  },\n  \"zusatzdaten\": {}\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Legt im Backend einen neuen Vorgang mit den Daten der eingegangenen Nachricht an.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="5" anker="schritt-5" richtung="fremd" kopf={{"links": {"label": "MSB (entspricht MSB am Objekt Marktlokation)", "eigen": false}, "rechts": {"label": "LF"}}}>

### Information über Störung an betroffener Marktlokation

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [23011](/schnittstellen/202610/pruefi/INSRPT/PI_23011) — Informationsmeldung · AS4

</div>

</Schritt>

<Schritt nr="6" anker="schritt-6" richtung="fremd" kopf={{"links": {"label": "MSB (entspricht MSB am Objekt Marktlokation)", "eigen": false}, "rechts": {"label": "ÜNB"}}}>

### Information über Störung an betroffener Marktlokation

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [23011](/schnittstellen/202610/pruefi/INSRPT/PI_23011) — Informationsmeldung · AS4

</div>

</Schritt>

<Schritt nr="7" anker="schritt-7" richtung="fremd" kopf={{"links": {"label": "MSB (entspricht MSB am Objekt Messlokation)", "eigen": false}, "rechts": {"label": "Störungsmelder"}}}>

### Mitteilung Ergebnis

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [23008](/schnittstellen/202610/pruefi/INSRPT/PI_23008) — Ergebnisbericht · AS4

</div>

</Schritt>

<Schritt nr="8" anker="schritt-8" richtung="fremd" kopf={{"links": {"label": "MSB (entspricht MSB am Objekt Messlokation)", "eigen": false}, "rechts": {"label": "MSB (entspricht MSB am Objekt Marktlokation)"}}}>

### Information über Ergebnis an Messlokation

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [23009](/schnittstellen/202610/pruefi/INSRPT/PI_23009) — Informationsmeldung · AS4

</div>

</Schritt>

<Schritt nr="9" anker="schritt-9" richtung="eingehend" kopf={{"links": {"label": "NB", "eigen": true}, "rechts": {"label": "MSB (entspricht MSB am Objekt Marktlokation)"}}}>

### Information über Ergebnis der betroffenen Marktlokation

<Schrittskizze sicht={{"label": "NB"}} zeilen={[{"art": "empfangen", "label": "MSB (entspricht MSB am Objekt Marktlokation)", "weg": "AS4", "nachrichten": [{"nr": "23012", "titel": "Informationsmeldung"}]}, {"art": "aperak", "werte": ["Z33"]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [23012](/schnittstellen/202610/pruefi/INSRPT/PI_23012) — Informationsmeldung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **MSB (entspricht MSB am Objekt Marktlokation)** · AS4

</li>

<li data-teil="aperak">

**Aperak-Prüfungen**
- `23012` → `Z33`

</li>

<li data-teil="schnittstelle" data-art="fortschreiben" data-abgeleitet="ja">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202610/backend-schreiben-nb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"STATUSMITTEILUNG\": [\n      {\n        \"boTyp\": \"STATUSMITTEILUNG\",\n        \"positionsdaten\": [\n          {\n            \"auftragsstatus\": \"GESTOERT\",\n            \"bearbeitungsdatum\": \"2023-02-19T23:00:00Z\",\n            \"fehlerbeschreibung\": {\n              \"beschreibung1\": \"Freier Text\"\n            },\n            \"lokationsId\": \"50188881541\",\n            \"positionsnummer\": 1,\n            \"referenzMelo\": \"DE0073395252733953513649640711234\",\n            \"statusanlass\": \"STOERUNGSBEHEBUNG_NICHT_MOEGLICH\",\n            \"verwendungAb\": \"2023-02-17T23:00:00Z\",\n            \"verwendungBis\": \"2023-02-19T23:00:00Z\"\n          }\n        ],\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"marktrolle\": \"MSB\",\n      \"rollencodenummer\": \"9900599000001\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"anfragereferenznummer\": \"109876543210\",\n    \"datenaustauschreferenz\": \"LETNEGNG\",\n    \"dokumentennummer\": \"BGMLF0CRAA0\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"marktrolle\": \"NB\",\n      \"rollencodenummer\": \"9905058000005\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"4\",\n    \"nachrichtendatum\": \"2023-02-21T10:47:00Z\",\n    \"nachrichtenreferenznummer\": \"UNHLF18893F\",\n    \"pruefidentifikator\": \"23012\",\n    \"sparte\": \"STROM\",\n    \"vorgangsnummer\": \"012345678910\"\n  },\n  \"zusatzdaten\": {}\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend mit den Daten der eingegangenen Nachricht fort.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="10" anker="schritt-10" richtung="fremd" kopf={{"links": {"label": "MSB (entspricht MSB am Objekt Marktlokation)", "eigen": false}, "rechts": {"label": "LF"}}}>

### Information über Ergebnis der betroffenen Marktlokation

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [23012](/schnittstellen/202610/pruefi/INSRPT/PI_23012) — Informationsmeldung · AS4

</div>

</Schritt>

<Schritt nr="11" anker="schritt-11" richtung="fremd" kopf={{"links": {"label": "MSB (entspricht MSB am Objekt Marktlokation)", "eigen": false}, "rechts": {"label": "ÜNB"}}}>

### Information über Ergebnis der betroffenen Marktlokation

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [23012](/schnittstellen/202610/pruefi/INSRPT/PI_23012) — Informationsmeldung · AS4

</div>

</Schritt>

<a id="abschnitt-informationen"></a>

## Prozess-Informationen

Wortlaut der Lesefassung, Steckbrief Kap. 1.1, S. 5–6.

<Stepper>
<ol>

<li data-blatt="vorbedingungen">

### Vorbedingungen

Der Störungsmelder stellt eine Störung fest.

</li>

<li data-blatt="ergebnisse">

### Ergebnisse

Funktionierende technische Einrichtung der Messlokation.

</li>

<li data-blatt="anforderungen">

### Weitere Anforderungen

Ergänzende Hinweise:
- Dieser Prozess ist auch zu durchlaufen, wenn der MSB der Messlokation die Störung selbst feststellt. Dabei werden die Prozessschritte 1, 2 und 7 nicht durchlaufen.
- Sofern dem ÜNB Werte fehlen, findet nicht der Use-Case „Störungsbehebung in der Messlokation“ statt, sondern der Use-Case „Reklamation von Werten beim MSB“.
- Ergänzender Hinweis: Liegt bei einer kME oder einer mME ein Zählwerksfehler (z. B. Zählwerksstillstand, -verlangsamung, -manipulation) vor, ist für den zu korrigierenden Verbrauch vom MSB eine Korrekturenergiemenge auf Ebene der Messlokation zu übermitteln. Die Ersatzwertbildung zur Ermittlung der Korrekturenergiemenge erfolgt nach der VDE-AR-N 4400 („Metering Code“). Der von der Messeinrichtung abgelesene Zählerstand wird nicht korrigiert. Es werden der abgelesene Zählerstand und die Korrekturenergiemengen nach den Vorgaben des Use-Cases „Aufbereitung und Übermittlung von Werten“ übermittelt. Außerdem ist vom MSB der Marktlokation eine Energiemenge für die abzurechnende Energiemenge auf Ebene der Marktlokation zu übermitteln.

</li>

<li data-blatt="erste-nachricht">

### Erste Nachricht

**MSB (entspricht MSB am Objekt Marktlokation)** sendet „Information über Störung an betroffener Marktlokation“ (Schritt 4). Ab hier ist der Beteiligte dieser Seite am Zug.

</li>

<li data-blatt="ziel">

### Ziel

Behebung einer Störung an den technischen Einrichtungen der Messlokation.

</li>

</ol>
</Stepper>

<a id="abschnitt-sichten"></a>

## Andere Sichten des Prozesses

Derselbe Prozess, aus den Augen der anderen Beteiligten: dieselben Schritte, jeweils aus deren Sicht gelesen.

- [Sicht LF](/prozessdoku/202610/LF/WiM-Teil2-stoerungsbehebung-in-der-messlokation) — LF
- [Sicht MSB-MALO](/prozessdoku/202610/MSB--MSB-MALO/WiM-Teil2-stoerungsbehebung-in-der-messlokation) — MSB am Objekt Marktlokation · Marktrolle MSB
- [Sicht MSB-MELO](/prozessdoku/202610/MSB--MSB-MELO/WiM-Teil2-stoerungsbehebung-in-der-messlokation) — MSB am Objekt Messlokation · Marktrolle MSB
- [Sicht ÜNB](/prozessdoku/202610/UENB/WiM-Teil2-stoerungsbehebung-in-der-messlokation) — ÜNB · Marktrolle UENB

<Hinweisbereich>

*Die Schritte sind die **möglichen** Nachrichten dieses Prozesses, keine Abfolge — die Quelle führt weder Bedingungen noch Alternativen. Das Kästchen am Schritt nennt links die eigene Sicht: **←** empfängt sie, **→** sendet sie. Zugeklappte Schritte laufen zwischen anderen Marktpartnern.*

Die Konnektortabelle führt für diese Schritte keinen Schreibaufruf. Abgeleitet aus dem Prozessverlauf: Mit ihrer Nachricht beginnt der Prozess für die eigene Rolle, der Vorgang entsteht also neu.

Betrifft: [4](#schritt-4)

Die Konnektortabelle führt für diese Schritte keinen Schreibaufruf. Abgeleitet aus dem Prozessverlauf: Die eigene Rolle war an diesem Prozess schon beteiligt, der Vorgang besteht also.

Betrifft: [9](#schritt-9)

</Hinweisbereich>
