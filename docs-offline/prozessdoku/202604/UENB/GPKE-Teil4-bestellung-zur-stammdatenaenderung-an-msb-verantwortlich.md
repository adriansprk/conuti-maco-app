# Bestellung zur Stammdatenänderung an MSB (verantwortlich) — Sicht ÜNB

<Kopf rolle="UENB" beteiligter="ÜNB" festlegung="GPKE" dokument="GPKE Teil 4" kapitel="1.5.4" sparte="Strom" schritte={8} suchtitel="Bestellung zur Stammdatenänderung an MSB (verantwortlich) — Sicht ÜNB (Marktrolle UENB) · GPKE Teil 4 · Formatversion 202604" abschnitte={[{"id": "abschnitt-ablauf", "label": "Prozessablauf"}, {"id": "abschnitt-schritte", "label": "Prozessschritte"}, {"id": "abschnitt-informationen", "label": "Prozess-Informationen"}, {"id": "abschnitt-sichten", "label": "Andere Sichten des Prozesses"}]} />

<Kurzfassung>

Der Prozess beschreibt die Anfrage/ Bestellung von Werten von Stammdaten durch einen Berechtigten beim Verantwortlichen der Stammdaten. Der Verantwortiche prüft die Bestellung und teilt dem Berechtigten den Bearbeitungsstand mit.

</Kurzfassung>

<a id="abschnitt-ablauf"></a>

## Prozessablauf aus Sicht des ÜNB

<Systembild svg={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1004 404\" width=\"1004\" height=\"404\" role=\"img\" aria-labelledby=\"sb-title\" class=\"maco-systembild\">\n<title id=\"sb-title\">Systembild: Bestellung zur Stammdatenänderung an MSB (verantwortlich) aus Sicht ÜNB</title>\n<defs><marker id=\"sb-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect class=\"sb-lane-kopf\" x=\"16\" y=\"12\" width=\"232\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend-System des Kunden</text>\n<rect class=\"sb-lane-kopf\" x=\"398\" y=\"12\" width=\"264\" height=\"46\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · ÜNB</text>\n<rect class=\"sb-lane-kopf\" x=\"812\" y=\"12\" width=\"176\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"900\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Marktpartner</text>\n<line x1=\"323\" y1=\"58\" x2=\"323\" y2=\"392\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"737\" y1=\"58\" x2=\"737\" y2=\"392\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"80\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">7. Bestellung einer Änderung</text>\n<text x=\"530\" y=\"115\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">von Stammdaten vom ÜNB</text>\n<text x=\"530\" y=\"130\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">an MSB</text>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"93\" r=\"5\"/><line x1=\"900\" y1=\"98\" x2=\"900\" y2=\"110\"/><line x1=\"893\" y1=\"102\" x2=\"907\" y2=\"102\"/><line x1=\"900\" y1=\"110\" x2=\"894\" y2=\"120\"/><line x1=\"900\" y1=\"110\" x2=\"906\" y2=\"120\"/></g>\n<text x=\"900\" y=\"142\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">MSB</text>\n<line x1=\"628\" y1=\"111\" x2=\"878\" y2=\"111\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"103\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"127\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">55685, 55687</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"169\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"189\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"143\" x2=\"530\" y2=\"169\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"169\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"189\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"185\" x2=\"230\" y2=\"185\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"177\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"233\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"253\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">8. Bearbeitungsstand zur</text>\n<text x=\"530\" y=\"268\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Bestellung</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"202\" x2=\"530\" y2=\"233\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"239\" r=\"5\"/><line x1=\"900\" y1=\"244\" x2=\"900\" y2=\"256\"/><line x1=\"893\" y1=\"248\" x2=\"907\" y2=\"248\"/><line x1=\"900\" y1=\"256\" x2=\"894\" y2=\"266\"/><line x1=\"900\" y1=\"256\" x2=\"906\" y2=\"266\"/></g>\n<text x=\"900\" y=\"288\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">MSB</text>\n<line x1=\"878\" y1=\"257\" x2=\"628\" y2=\"257\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"249\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"273\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">21047</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"316\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"336\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"281\" x2=\"530\" y2=\"316\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben sb-abgeleitet\" x=\"34\" y=\"316\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"336\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"332\" x2=\"230\" y2=\"332\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"324\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n</svg>"} gesamt={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1462 734\" width=\"1462\" height=\"734\" role=\"img\" aria-labelledby=\"sd-title\" class=\"maco-sequence\">\n<title id=\"sd-title\">Sequenzdiagramm: Bestellung zur Stammdatenänderung an MSB (verantwortlich) aus Sicht ÜNB</title>\n<defs><marker id=\"sd-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect x=\"16\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"121\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend (Kunde)</text>\n<line x1=\"121\" y1=\"64\" x2=\"121\" y2=\"722\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"260\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"365\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · ÜNB</text>\n<line x1=\"365\" y1=\"64\" x2=\"365\" y2=\"722\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"504\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"609\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"609\" y1=\"64\" x2=\"609\" y2=\"722\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"748\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"853\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">MSB</text>\n<line x1=\"853\" y1=\"64\" x2=\"853\" y2=\"722\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"992\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"1097\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">LF</text>\n<line x1=\"1097\" y1=\"64\" x2=\"1097\" y2=\"722\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"1236\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"1341\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">weiterer MSB</text>\n<line x1=\"1341\" y1=\"64\" x2=\"1341\" y2=\"722\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"609\" y1=\"90\" x2=\"853\" y2=\"90\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"731\" y=\"81\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">1. Bestellung einer Änderung von Stammdaten vom…</text>\n<text x=\"731\" y=\"105\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55559, 55555, 55644…</text>\n<line x1=\"853\" y1=\"152\" x2=\"609\" y2=\"152\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"731\" y=\"143\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">2. Bearbeitungsstand zur Bestellung</text>\n<text x=\"731\" y=\"167\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 21047 · E_0586</text>\n<text x=\"731\" y=\"180\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0586 — Bestellung zur Stammdatenänderung prüfen</text>\n<line x1=\"1097\" y1=\"214\" x2=\"853\" y2=\"214\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"975\" y=\"205\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">3. Bestellung einer Änderung von Stammdaten vom…</text>\n<text x=\"975\" y=\"229\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55654, 55555, 55655…</text>\n<line x1=\"853\" y1=\"276\" x2=\"1097\" y2=\"276\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"975\" y=\"267\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">4. Bearbeitungsstand zur Bestellung</text>\n<text x=\"975\" y=\"291\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 21047 · E_0585</text>\n<text x=\"975\" y=\"304\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0585 — Bestellung zur Stammdatenänderung prüfen</text>\n<line x1=\"1341\" y1=\"338\" x2=\"853\" y2=\"338\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"1097\" y=\"329\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">5. Bestellung einer Änderung von Stammdaten vom…</text>\n<text x=\"1097\" y=\"353\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55664, 55555, 55665…</text>\n<line x1=\"853\" y1=\"400\" x2=\"1341\" y2=\"400\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"1097\" y=\"391\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">6. Bearbeitungsstand zur Bestellung</text>\n<text x=\"1097\" y=\"415\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 21047 · E_0584</text>\n<text x=\"1097\" y=\"428\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0584 — Bestellung zur Stammdatenänderung prüfen</text>\n<line x1=\"365\" y1=\"462\" x2=\"853\" y2=\"462\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"609\" y=\"453\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">7. Bestellung einer Änderung von Stammdaten vom…</text>\n<text x=\"609\" y=\"477\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55685, 55687</text>\n<line x1=\"365\" y1=\"524\" x2=\"121\" y2=\"524\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"515\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"539\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"853\" y1=\"586\" x2=\"365\" y2=\"586\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"609\" y=\"577\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">8. Bearbeitungsstand zur Bestellung</text>\n<text x=\"609\" y=\"601\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 21047 · E_0587</text>\n<text x=\"609\" y=\"614\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0587 — Bestellung zur Stammdatenänderung prüfen</text>\n<line x1=\"365\" y1=\"648\" x2=\"121\" y2=\"648\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"639\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"663\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n</svg>"} titel="ÜNB" />

<a id="abschnitt-schritte"></a>

## Prozessschritte

<Schritt nr="1" anker="schritt-1" richtung="fremd" kopf={{"links": {"label": "NB", "eigen": false}, "rechts": {"label": "MSB"}}}>

### Bestellung einer Änderung von Stammdaten vom NB an MSB

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55559](/schnittstellen/202604/pruefi/UTILMD/PI_55559) — Rückmeldung/Anfrage MSB-Abr.-Daten der MaLo · AS4
- [55555](/schnittstellen/202604/pruefi/UTILMD/PI_55555) — Anfrage Daten der individuellen Bestellung · AS4
- [55644](/schnittstellen/202604/pruefi/UTILMD/PI_55644) — Rückmeldung/Anfrage Daten der NeLo · AS4
- [55645](/schnittstellen/202604/pruefi/UTILMD/PI_55645) — Rückmeldung/Anfrage Daten der MaLo · AS4
- [55646](/schnittstellen/202604/pruefi/UTILMD/PI_55646) — Rückmeldung/Anfrage Daten der SR · AS4
- [55647](/schnittstellen/202604/pruefi/UTILMD/PI_55647) — Rückmeldung/Anfrage Daten der Tranche · AS4
- [55648](/schnittstellen/202604/pruefi/UTILMD/PI_55648) — Rückmeldung/Anfrage Daten der MeLo · AS4

</div>

</Schritt>

<Schritt nr="2" anker="schritt-2" richtung="fremd" kopf={{"links": {"label": "MSB", "eigen": false}, "rechts": {"label": "NB"}}}>

### Bearbeitungsstand zur Bestellung

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [21047](/schnittstellen/202604/pruefi/IFTSTA/PI_21047) — Bearbeitungsstandsmeldung · AS4

</div>

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `21047` → [E_0586](/referenz/202604/ebd/E_0586) · MSB · Bestellung zur Stammdatenänderung prüfen (Basiert auf EBD: E_0573_Bestellung zur Stammdatenänderung prüfen)

</div>

</Schritt>

<Schritt nr="3" anker="schritt-3" richtung="fremd" kopf={{"links": {"label": "LF", "eigen": false}, "rechts": {"label": "MSB"}}}>

### Bestellung einer Änderung von Stammdaten vom LF an MSB

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55654](/schnittstellen/202604/pruefi/UTILMD/PI_55654) — Rückmeldung/Anfrage Daten der NeLo · AS4
- [55555](/schnittstellen/202604/pruefi/UTILMD/PI_55555) — Anfrage Daten der individuellen Bestellung · AS4
- [55655](/schnittstellen/202604/pruefi/UTILMD/PI_55655) — Rückmeldung/Anfrage Daten der MaLo · AS4
- [55656](/schnittstellen/202604/pruefi/UTILMD/PI_55656) — Rückmeldung/Anfrage Daten der SR · AS4
- [55657](/schnittstellen/202604/pruefi/UTILMD/PI_55657) — Rückmeldung/Anfrage Daten der Tranche · AS4
- [55658](/schnittstellen/202604/pruefi/UTILMD/PI_55658) — Rückmeldung/Anfrage Daten der MeLo · AS4

</div>

</Schritt>

<Schritt nr="4" anker="schritt-4" richtung="fremd" kopf={{"links": {"label": "MSB", "eigen": false}, "rechts": {"label": "LF"}}}>

### Bearbeitungsstand zur Bestellung

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [21047](/schnittstellen/202604/pruefi/IFTSTA/PI_21047) — Bearbeitungsstandsmeldung · AS4

</div>

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `21047` → [E_0585](/referenz/202604/ebd/E_0585) · MSB · Bestellung zur Stammdatenänderung prüfen (Basiert auf EBD: E_0573_Bestellung zur Stammdatenänderung prüfen)

</div>

</Schritt>

<Schritt nr="5" anker="schritt-5" richtung="fremd" kopf={{"links": {"label": "weiterer MSB", "eigen": false}, "rechts": {"label": "MSB"}}}>

### Bestellung einer Änderung von Stammdaten vom weiteren MSB an MSB

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55664](/schnittstellen/202604/pruefi/UTILMD/PI_55664) — Rückmeldung/Anfrage Daten der NeLo · AS4
- [55555](/schnittstellen/202604/pruefi/UTILMD/PI_55555) — Anfrage Daten der individuellen Bestellung · AS4
- [55665](/schnittstellen/202604/pruefi/UTILMD/PI_55665) — Rückmeldung/Anfrage Daten der MaLo · AS4
- [55666](/schnittstellen/202604/pruefi/UTILMD/PI_55666) — Rückmeldung/Anfrage Daten der SR · AS4
- [55667](/schnittstellen/202604/pruefi/UTILMD/PI_55667) — Rückmeldung/Anfrage Daten der Tranche · AS4
- [55669](/schnittstellen/202604/pruefi/UTILMD/PI_55669) — Rückmeldung/Anfrage Daten der MeLo · AS4

</div>

</Schritt>

<Schritt nr="6" anker="schritt-6" richtung="fremd" kopf={{"links": {"label": "MSB", "eigen": false}, "rechts": {"label": "weiterer MSB"}}}>

### Bearbeitungsstand zur Bestellung

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [21047](/schnittstellen/202604/pruefi/IFTSTA/PI_21047) — Bearbeitungsstandsmeldung · AS4

</div>

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `21047` → [E_0584](/referenz/202604/ebd/E_0584) · MSB · Bestellung zur Stammdatenänderung prüfen (Basiert auf EBD: E_0573_Bestellung zur Stammdatenänderung prüfen)

</div>

</Schritt>

<Schritt nr="7" anker="schritt-7" richtung="ausgehend" kopf={{"links": {"label": "ÜNB", "eigen": true}, "rechts": {"label": "MSB"}}}>

### Bestellung einer Änderung von Stammdaten vom ÜNB an MSB

<Schrittskizze sicht={{"label": "ÜNB"}} zeilen={[{"art": "senden", "label": "MSB", "weg": "AS4", "nachrichten": [{"nr": "55685", "titel": "Rückmeldung/Anfrage Daten der MaLo"}, {"nr": "55687", "titel": "Rückmeldung/Anfrage Daten der Tranche"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55685](/schnittstellen/202604/pruefi/UTILMD/PI_55685) — Rückmeldung/Anfrage Daten der MaLo · AS4
- [55687](/schnittstellen/202604/pruefi/UTILMD/PI_55687) — Rückmeldung/Anfrage Daten der Tranche · AS4

</div>

**Ablauf**

<div data-ablauf data-offen="ja">

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht an **MSB** · AS4

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

<Schritt nr="8" anker="schritt-8" richtung="eingehend" kopf={{"links": {"label": "ÜNB", "eigen": true}, "rechts": {"label": "MSB"}}}>

### Bearbeitungsstand zur Bestellung

<Schrittskizze sicht={{"label": "ÜNB"}} zeilen={[{"art": "empfangen", "label": "MSB", "weg": "AS4", "nachrichten": [{"nr": "21047", "titel": "Bearbeitungsstandsmeldung"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [21047](/schnittstellen/202604/pruefi/IFTSTA/PI_21047) — Bearbeitungsstandsmeldung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **MSB** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `21047` → [E_0587](/referenz/202604/ebd/E_0587) · MSB · Bestellung zur Stammdatenänderung prüfen (Basiert auf EBD: E_0573_Bestellung zur Stammdatenänderung prüfen)

</div>

</li>

<li data-teil="schnittstelle" data-art="fortschreiben" data-abgeleitet="ja">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — `AKTUALISIEREN_PROZESSDATEN`

Schreibt den bestehenden Vorgang im Backend mit den Daten der eingegangenen Nachricht fort.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<details>
<summary>Entscheidungsbäume dieses Prozesses</summary>

| EBD | Name |
|---|---|
| [E_0587](/referenz/202604/ebd/E_0587) | Bestellung zur Stammdatenänderung prüfen (Basiert auf EBD: E_0573_Bestellung zur Stammdatenänderung prüfen) |
| [E_0584](/referenz/202604/ebd/E_0584) | Bestellung zur Stammdatenänderung prüfen (Basiert auf EBD: E_0573_Bestellung zur Stammdatenänderung prüfen) |
| [E_0585](/referenz/202604/ebd/E_0585) | Bestellung zur Stammdatenänderung prüfen (Basiert auf EBD: E_0573_Bestellung zur Stammdatenänderung prüfen) |
| [E_0586](/referenz/202604/ebd/E_0586) | Bestellung zur Stammdatenänderung prüfen (Basiert auf EBD: E_0573_Bestellung zur Stammdatenänderung prüfen) |

</details>

<a id="abschnitt-informationen"></a>

## Prozess-Informationen

Wortlaut der Lesefassung, Steckbrief Kap. 1.5.1, S. 18–19.

<Stepper>
<ol>

<li data-blatt="vorbedingungen">

### Vorbedingungen

- Es besteht eine aktuelle oder zukünftig abgestimmte Zuordnung der Marktpartner in der jeweiligen Rolle zur Lokation.

</li>

<li data-blatt="ergebnisse">

### Ergebnisse

- Sofern der Verantwortliche davon ausgehen muss, dass die bestellten Werte von Stammdaten einem/mehreren Berechtigten nicht vorliegen, übermittelt er diese im Rahmen des Use-Cases „Stammdatenänderung“ an diese/n, so dass allen Berechtigten die gleichen Werte der Stammdaten vorliegen.
- Sofern der Verantwortliche davon ausgehen kann, dass das fachliche Ergebnis jedem Berechtigten vorliegt: Die Folgeprozesse setzen auf abgeglichenen und synchronen Werten der Stammdaten auf.

</li>

<li data-blatt="fehlerfall">

### Fehlerfall

#### Fehlerfälle

- Ein Bearbeitungsstand auf die Bestellung liegt nicht fristgerecht vor.

</li>

<li data-blatt="anforderungen">

### Weitere Anforderungen

- Im Fall des SD „Bestellung zur Stammdatenänderung an MSB (verantwortlich)“ gilt: Der verantwortliche MSB einer Messlokation ist immer der MSB, der zum Zeitpunkt, zu dem die Änderung des Werts des Stammdatums erfolgt, der Messlokation zugeordnet ist. Dabei gilt folgende Ausnahme: Findet an der Messlokation der Use-Case „[Geräteübernahme](/prozessdoku/202604/MSB--MSBA/WiM-Teil1-geraeteuebernahme)“ (WiM Teil 1) statt, ist neben dem vorgenannten MSB (im Use-Case „[Geräteübernahme](/prozessdoku/202604/MSB--MSBA/WiM-Teil1-geraeteuebernahme)“ als MSBA bezeichnet) auch der MSBN berechtigt für diese Messlokation das SD „[Stammdatenänderung vom MSB (verantwortlich) ausgehend](/prozessdoku/202604/UENB/GPKE-Teil4-stammdatenaenderung-vom-msb-verantwortlich-ausgehend)“ als verantwortlicher MSB anzuwenden. Demensprechend können die Berechtigten wiederum eine Bestellung zur Stammdatenänderung an den MSBN senden.

</li>

<li data-blatt="anlass">

### Anlass

- Dem Berechtigten liegt für ein Stammdatum ein neuer Wert vor.
- Der Berechtigte geht von einem Datenschiefstand zwischen den Berechtigten und dem Verantwortlichen aus.

</li>

<li data-blatt="erste-nachricht">

### Erste Nachricht

Der Beteiligte dieser Seite sendet selbst: „Bestellung einer Änderung von Stammdaten vom ÜNB an MSB“ an **MSB** (Schritt 7).

</li>

<li data-blatt="ziel">

### Ziel

Der Bearbeitungsstand zur Bestellung des Berechtigten liegt dem Berechtigten vom Verantwortlichen vor.

</li>

</ol>
</Stepper>

<a id="abschnitt-sichten"></a>

## Andere Sichten des Prozesses

Derselbe Prozess, aus den Augen der anderen Beteiligten: dieselben Schritte, jeweils aus deren Sicht gelesen.

- [Sicht LF](/prozessdoku/202604/LF/GPKE-Teil4-bestellung-zur-stammdatenaenderung-an-msb-verantwortlich) — LF
- [Sicht NB](/prozessdoku/202604/NB/GPKE-Teil4-bestellung-zur-stammdatenaenderung-an-msb-verantwortlich) — NB
- [Sicht MSB](/prozessdoku/202604/MSB/GPKE-Teil4-bestellung-zur-stammdatenaenderung-an-msb-verantwortlich) — MSB
- [Sicht WMSB](/prozessdoku/202604/MSB--WMSB/GPKE-Teil4-bestellung-zur-stammdatenaenderung-an-msb-verantwortlich) — weiterer Messstellenbetreiber · Marktrolle MSB

<Hinweisbereich>

*Die Schritte sind die **möglichen** Nachrichten dieses Prozesses, keine Abfolge — die Quelle führt weder Bedingungen noch Alternativen. Das Kästchen am Schritt nennt links die eigene Sicht: **←** empfängt sie, **→** sendet sie. Zugeklappte Schritte laufen zwischen anderen Marktpartnern.*

Welches Ereignis diese Schritte anstößt, benennt die Quelle noch nicht.

Betrifft: [7](#schritt-7)

Die Konnektortabelle führt für diese Schritte keinen Schreibaufruf. Abgeleitet aus dem Prozessverlauf: Die eigene Rolle war an diesem Prozess schon beteiligt, der Vorgang besteht also.

Betrifft: [8](#schritt-8)

Für diese Marktrolle liegt kein Schreibkatalog vor; am Schritt steht deshalb nur das Kommando des Schreibaufrufs, ohne Adresse und ohne Knopf.

Betrifft: [7](#schritt-7), [8](#schritt-8)

</Hinweisbereich>
