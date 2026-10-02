# Bestellung zur Stammdatenänderung an MSB (verantwortlich) — Sicht LF

<Kopf rolle="LF" beteiligter="LF" festlegung="GPKE" dokument="GPKE Teil 4" kapitel="1.5.4" sparte="Strom" schritte={8} suchtitel="Bestellung zur Stammdatenänderung an MSB (verantwortlich) — Sicht LF · GPKE Teil 4 · Formatversion 202610" abschnitte={[{"id": "abschnitt-ablauf", "label": "Prozessablauf"}, {"id": "abschnitt-schritte", "label": "Prozessschritte"}, {"id": "abschnitt-informationen", "label": "Prozess-Informationen"}, {"id": "abschnitt-sichten", "label": "Andere Sichten des Prozesses"}]} />

<Kurzfassung>

Der Prozess beschreibt die Anfrage/ Bestellung von Werten von Stammdaten durch einen Berechtigten beim Verantwortlichen der Stammdaten. Der Verantwortiche prüft die Bestellung und teilt dem Berechtigten den Bearbeitungsstand mit.

</Kurzfassung>

<a id="abschnitt-ablauf"></a>

## Prozessablauf aus Sicht des LF

<Systembild svg={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1004 695\" width=\"1004\" height=\"695\" role=\"img\" aria-labelledby=\"sb-title\" class=\"maco-systembild\">\n<title id=\"sb-title\">Systembild: Bestellung zur Stammdatenänderung an MSB (verantwortlich) aus Sicht LF</title>\n<defs><marker id=\"sb-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect class=\"sb-lane-kopf\" x=\"16\" y=\"12\" width=\"232\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend-System des Kunden</text>\n<rect class=\"sb-lane-kopf\" x=\"398\" y=\"12\" width=\"264\" height=\"46\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · LF</text>\n<rect class=\"sb-lane-kopf\" x=\"812\" y=\"12\" width=\"176\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"900\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Marktpartner</text>\n<line x1=\"323\" y1=\"58\" x2=\"323\" y2=\"683\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"737\" y1=\"58\" x2=\"737\" y2=\"683\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect class=\"sb-kasten sb-folge_ausloeser\" x=\"432\" y=\"80\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Ausgelöst durch Eingang:</text>\n<text x=\"530\" y=\"115\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">55553, 55649, 55650,</text>\n<text x=\"530\" y=\"130\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">55651, 55652,…</text>\n<rect class=\"sb-kasten sb-trigger\" x=\"432\" y=\"169\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"189\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessauslöser empfangen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"143\" x2=\"530\" y2=\"169\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-trigger\" x=\"34\" y=\"169\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"189\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">START_BESTELLUNG_SDAE</text>\n<line x1=\"230\" y1=\"185\" x2=\"432\" y2=\"185\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"177\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-lesen_verarbeitung\" x=\"432\" y=\"233\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"253\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Daten für die Verarbeitung</text>\n<text x=\"530\" y=\"268\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">laden</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"202\" x2=\"530\" y2=\"233\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-lesen_verarbeitung\" x=\"34\" y=\"233\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"253\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">8 Lese-Schnittstellen</text>\n<text x=\"132\" y=\"268\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">aufgerufen</text>\n<line x1=\"432\" y1=\"257\" x2=\"230\" y2=\"257\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"249\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<text x=\"331\" y=\"273\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">je einzeln am Schritt</text>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"307\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"327\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">3. Bestellung einer Änderung</text>\n<text x=\"530\" y=\"342\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">von Stammdaten vom LF an</text>\n<text x=\"530\" y=\"357\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">MSB</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"281\" x2=\"530\" y2=\"307\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"320\" r=\"5\"/><line x1=\"900\" y1=\"325\" x2=\"900\" y2=\"337\"/><line x1=\"893\" y1=\"329\" x2=\"907\" y2=\"329\"/><line x1=\"900\" y1=\"337\" x2=\"894\" y2=\"347\"/><line x1=\"900\" y1=\"337\" x2=\"906\" y2=\"347\"/></g>\n<text x=\"900\" y=\"369\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">MSB</text>\n<line x1=\"628\" y1=\"338\" x2=\"878\" y2=\"338\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"330\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"354\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">55654, 55555, 55655…</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"396\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"416\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"370\" x2=\"530\" y2=\"396\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"396\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"416\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"412\" x2=\"230\" y2=\"412\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"404\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"460\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"480\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">4. Bearbeitungsstand zur</text>\n<text x=\"530\" y=\"495\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Bestellung</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"429\" x2=\"530\" y2=\"460\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"466\" r=\"5\"/><line x1=\"900\" y1=\"471\" x2=\"900\" y2=\"483\"/><line x1=\"893\" y1=\"475\" x2=\"907\" y2=\"475\"/><line x1=\"900\" y1=\"483\" x2=\"894\" y2=\"493\"/><line x1=\"900\" y1=\"483\" x2=\"906\" y2=\"493\"/></g>\n<text x=\"900\" y=\"515\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">MSB</text>\n<line x1=\"878\" y1=\"484\" x2=\"628\" y2=\"484\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"476\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"500\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">21047</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"543\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"563\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z33</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"508\" x2=\"530\" y2=\"543\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"607\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"627\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"576\" x2=\"530\" y2=\"607\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"607\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"627\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"623\" x2=\"230\" y2=\"623\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"615\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n</svg>"} gesamt={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1462 796\" width=\"1462\" height=\"796\" role=\"img\" aria-labelledby=\"sd-title\" class=\"maco-sequence\">\n<title id=\"sd-title\">Sequenzdiagramm: Bestellung zur Stammdatenänderung an MSB (verantwortlich) aus Sicht LF</title>\n<defs><marker id=\"sd-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect x=\"16\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"121\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend (Kunde)</text>\n<line x1=\"121\" y1=\"64\" x2=\"121\" y2=\"784\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"260\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"365\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · LF</text>\n<line x1=\"365\" y1=\"64\" x2=\"365\" y2=\"784\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"504\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"609\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"609\" y1=\"64\" x2=\"609\" y2=\"784\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"748\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"853\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">MSB</text>\n<line x1=\"853\" y1=\"64\" x2=\"853\" y2=\"784\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"992\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"1097\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">weiterer MSB</text>\n<line x1=\"1097\" y1=\"64\" x2=\"1097\" y2=\"784\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"1236\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"1341\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">ÜNB</text>\n<line x1=\"1341\" y1=\"64\" x2=\"1341\" y2=\"784\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"609\" y1=\"90\" x2=\"853\" y2=\"90\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"731\" y=\"81\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">1. Bestellung einer Änderung von Stammdaten vom…</text>\n<text x=\"731\" y=\"105\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55559, 55555, 55644…</text>\n<line x1=\"853\" y1=\"152\" x2=\"609\" y2=\"152\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"731\" y=\"143\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">2. Bearbeitungsstand zur Bestellung</text>\n<text x=\"731\" y=\"167\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 21047 · E_0586</text>\n<text x=\"731\" y=\"180\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0586 — Bestellung zur Stammdatenänderung prüfen</text>\n<line x1=\"121\" y1=\"214\" x2=\"365\" y2=\"214\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"205\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">START_BESTELLUNG_SDAE</text>\n<text x=\"243\" y=\"229\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Trigger-Event</text>\n<line x1=\"365\" y1=\"276\" x2=\"853\" y2=\"276\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"609\" y=\"267\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">3. Bestellung einer Änderung von Stammdaten vom…</text>\n<text x=\"609\" y=\"291\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55654, 55555, 55655…</text>\n<line x1=\"365\" y1=\"338\" x2=\"121\" y2=\"338\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"329\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"353\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"853\" y1=\"400\" x2=\"365\" y2=\"400\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"609\" y=\"391\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">4. Bearbeitungsstand zur Bestellung</text>\n<text x=\"609\" y=\"415\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 21047 · E_0585</text>\n<text x=\"609\" y=\"428\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0585 — Bestellung zur Stammdatenänderung prüfen</text>\n<line x1=\"365\" y1=\"462\" x2=\"121\" y2=\"462\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"453\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"477\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"1097\" y1=\"524\" x2=\"853\" y2=\"524\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"975\" y=\"515\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">5. Bestellung einer Änderung von Stammdaten vom…</text>\n<text x=\"975\" y=\"539\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55664, 55555, 55665…</text>\n<line x1=\"853\" y1=\"586\" x2=\"1097\" y2=\"586\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"975\" y=\"577\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">6. Bearbeitungsstand zur Bestellung</text>\n<text x=\"975\" y=\"601\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 21047 · E_0584</text>\n<text x=\"975\" y=\"614\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0584 — Bestellung zur Stammdatenänderung prüfen</text>\n<line x1=\"1341\" y1=\"648\" x2=\"853\" y2=\"648\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"1097\" y=\"639\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">7. Bestellung einer Änderung von Stammdaten vom…</text>\n<text x=\"1097\" y=\"663\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55685, 55687</text>\n<line x1=\"853\" y1=\"710\" x2=\"1341\" y2=\"710\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"1097\" y=\"701\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">8. Bearbeitungsstand zur Bestellung</text>\n<text x=\"1097\" y=\"725\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 21047 · E_0587</text>\n<text x=\"1097\" y=\"738\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0587 — Bestellung zur Stammdatenänderung prüfen</text>\n</svg>"} titel="LF" />

<a id="abschnitt-schritte"></a>

## Prozessschritte

<Schritt nr="1" anker="schritt-1" richtung="fremd" kopf={{"links": {"label": "NB", "eigen": false}, "rechts": {"label": "MSB"}}}>

### Bestellung einer Änderung von Stammdaten vom NB an MSB

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55559](/schnittstellen/202610/pruefi/UTILMD/PI_55559) — Rückmeldung/Anfrage MSB-Abr.-Daten der MaLo · AS4
- [55555](/schnittstellen/202610/pruefi/UTILMD/PI_55555) — Anfrage Daten der individuellen Bestellung · AS4
- [55644](/schnittstellen/202610/pruefi/UTILMD/PI_55644) — Rückmeldung/Anfrage Daten der NeLo · AS4
- [55645](/schnittstellen/202610/pruefi/UTILMD/PI_55645) — Rückmeldung/Anfrage Daten der MaLo · AS4
- [55646](/schnittstellen/202610/pruefi/UTILMD/PI_55646) — Rückmeldung/Anfrage Daten der SR · AS4
- [55647](/schnittstellen/202610/pruefi/UTILMD/PI_55647) — Rückmeldung/Anfrage Daten der Tranche · AS4
- [55648](/schnittstellen/202610/pruefi/UTILMD/PI_55648) — Rückmeldung/Anfrage Daten der MeLo · AS4

</div>

</Schritt>

<Schritt nr="2" anker="schritt-2" richtung="fremd" kopf={{"links": {"label": "MSB", "eigen": false}, "rechts": {"label": "NB"}}}>

### Bearbeitungsstand zur Bestellung

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [21047](/schnittstellen/202610/pruefi/IFTSTA/PI_21047) — Bearbeitungsstandsmeldung · AS4

</div>

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `21047` → [E_0586](/referenz/202610/ebd/E_0586) · MSB · Bestellung zur Stammdatenänderung prüfen (Basiert auf EBD: E_0573_Bestellung zur Stammdatenänderung prüfen)

</div>

</Schritt>

<Schritt nr="3" anker="schritt-3" richtung="ausgehend" kopf={{"links": {"label": "LF", "eigen": true}, "rechts": {"label": "MSB"}}}>

### Bestellung einer Änderung von Stammdaten vom LF an MSB

<Schrittskizze sicht={{"label": "LF"}} zeilen={[{"art": "folge_ausloeser", "werte": ["55553", "55649", "55650", "55651", "55652", "55653"]}, {"art": "ausloeser", "werte": ["START_BESTELLUNG_SDAE"]}, {"art": "lesen_verarbeitung", "schnittstellen": [{"label": "Netzlokation lesen"}, {"label": "Bilanzierung lesen"}, {"label": "Marktlokation lesen"}, {"label": "Messlokation lesen"}, {"label": "Netznutzungsvertrag lesen"}, {"label": "Zähler lesen"}, {"label": "Steuerbare Ressource lesen"}, {"label": "Tranche lesen"}]}, {"art": "senden", "label": "MSB", "weg": "AS4", "nachrichten": [{"nr": "55654", "titel": "Rückmeldung/Anfrage Daten der NeLo"}, {"nr": "55555", "titel": "Anfrage Daten der individuellen Bestellung"}, {"nr": "55655", "titel": "Rückmeldung/Anfrage Daten der MaLo"}, {"nr": "55656", "titel": "Rückmeldung/Anfrage Daten der SR"}, {"nr": "55657", "titel": "Rückmeldung/Anfrage Daten der Tranche"}, {"nr": "55658", "titel": "Rückmeldung/Anfrage Daten der MeLo"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55654](/schnittstellen/202610/pruefi/UTILMD/PI_55654) — Rückmeldung/Anfrage Daten der NeLo · AS4
- [55555](/schnittstellen/202610/pruefi/UTILMD/PI_55555) — Anfrage Daten der individuellen Bestellung · AS4
- [55655](/schnittstellen/202610/pruefi/UTILMD/PI_55655) — Rückmeldung/Anfrage Daten der MaLo · AS4
- [55656](/schnittstellen/202610/pruefi/UTILMD/PI_55656) — Rückmeldung/Anfrage Daten der SR · AS4
- [55657](/schnittstellen/202610/pruefi/UTILMD/PI_55657) — Rückmeldung/Anfrage Daten der Tranche · AS4
- [55658](/schnittstellen/202610/pruefi/UTILMD/PI_55658) — Rückmeldung/Anfrage Daten der MeLo · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="folge_ausloeser">

**Ausgelöst durch Eingang**
- [55553](/schnittstellen/202610/pruefi/UTILMD/PI_55553)
- [55649](/schnittstellen/202610/pruefi/UTILMD/PI_55649)
- [55650](/schnittstellen/202610/pruefi/UTILMD/PI_55650)
- [55651](/schnittstellen/202610/pruefi/UTILMD/PI_55651)
- [55652](/schnittstellen/202610/pruefi/UTILMD/PI_55652)
- [55653](/schnittstellen/202610/pruefi/UTILMD/PI_55653)

Die MACO APP sendet diese Nachricht selbst, als Folgeprozess nach einem dieser Eingänge. Daneben kann das Backend diesen Schritt mit einem Ereignis anstoßen — der nächste Punkt.

</li>

<li data-teil="ausloeser">

**Prozessauslöser** [`START_BESTELLUNG_SDAE`](/schnittstellen/202610/trigger/events/LF-START_BESTELLUNG_SDAE) · [Im Playground ausprobieren](/api/202610/ausloeser-lf/start-bestellung-sdae)

Das Backend stößt diesen Schritt mit diesem Ereignis an.

</li>

<li data-teil="lesen" data-stufe="verarbeitung">

**Daten für die Verarbeitung laden**
- [Netzlokation lesen](/api/202610/backend-lesen/getgridlocationbasic#netzlokation-lesen) `GET /getGridLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getGridLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_NETZLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Bilanzierung lesen](/api/202610/backend-lesen/getaccountingbasic#bilanzierung-lesen) `GET /getAccountingBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getAccountingBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_BILANZIERUNG_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Marktlokation lesen](/api/202610/backend-lesen/getmarketlocationbasic#marktlokation-lesen) `GET /getMarketLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getMarketLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": false, "defaultValue": "MALO", "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": false, "defaultValue": "2024-06-28T12:18:00Z", "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_MARKTLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Messlokation lesen](/api/202610/backend-lesen/getmeterlocationbasic#messlokation-lesen) `GET /getMeterLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getMeterLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_MESSLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Netznutzungsvertrag lesen](/api/202610/backend-lesen/getgridusagecontractbasic#netznutzungsvertrag-lesen) `GET /getGridUsageContractBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getGridUsageContractBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": false, "defaultValue": "MALO", "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": false, "defaultValue": "2024-06-28T12:18:00Z", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Zähler lesen](/api/202610/backend-lesen/getcounterbasic#zahler-lesen) `GET /getCounterBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getCounterBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Steuerbare Ressource lesen](/api/202610/backend-lesen/getcontrollableresourcebasic#steuerbare-ressource-lesen) `GET /getControllableResourceBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getControllableResourceBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Tranche lesen](/api/202610/backend-lesen/gettranchebasic#tranche-lesen) `GET /getTrancheBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getTrancheBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

</li>

<li data-teil="nachricht">

Nachricht an **MSB** · AS4

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202610/backend-schreiben-lf/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": false, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"NETZLOKATION\": [\n      {\n        \"boTyp\": \"NETZLOKATION\",\n        \"netzlokationsId\": \"E1688117482\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9903790000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"anfragereferenznummer\": \"ABC123456\",\n    \"antwortStatusZeitraum\": [\n      {\n        \"code\": \"A01\",\n        \"liste\": \"E_0412\",\n        \"zeitraumId\": 1\n      }\n    ],\n    \"datenaustauschreferenz\": \"M06SVKIZ\",\n    \"dokumentennummer\": \"BGMLZR6HFYA\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9904446000007\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"E03\",\n    \"nachrichtendatum\": \"2026-10-02T11:00:00Z\",\n    \"nachrichtenreferenznummer\": \"UNHM0390WIB\",\n    \"pruefidentifikator\": \"55654\",\n    \"sparte\": \"STROM\",\n    \"transaktionsgrund\": \"ZX8\",\n    \"verwendungAb\": \"2025-04-02T22:00:00Z\",\n    \"vorgangsnummer\": \"123456\"\n  },\n  \"zusatzdaten\": {}\n}"} examples={[{"mediaType": "application/json", "examples": [{"name": "55654", "summary": "55654 — Rückmeldung/Anfrage Daten der NeLo", "value": {"stammdaten": {"NETZLOKATION": [{"boTyp": "NETZLOKATION", "versionStruktur": "1", "netzlokationsId": "E1688117482", "sparte": "STROM"}]}, "transaktionsdaten": {"datenaustauschreferenz": "M06SVKIZ", "sparte": "STROM", "transaktionsgrund": "ZX8", "vorgangsnummer": "123456", "pruefidentifikator": "55654", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9903790000002", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9904446000007", "rollencodetyp": "BDEW"}, "dokumentennummer": "BGMLZR6HFYA", "kategorie": "E03", "nachrichtendatum": "2026-10-02T11:00:00Z", "nachrichtenreferenznummer": "UNHM0390WIB", "anfragereferenznummer": "ABC123456", "verwendungAb": "2025-04-02T22:00:00Z", "antwortStatusZeitraum": [{"code": "A01", "liste": "E_0412", "zeitraumId": 1}]}, "zusatzdaten": {}}}, {"name": "55555", "summary": "55555 — Anfrage Daten der individuellen Bestellung", "value": {"stammdaten": {"AD_HOC_STEUERKANAL": [{"boTyp": "AD_HOC_STEUERKANAL", "versionStruktur": "1", "zieladresse": {"zieladresse1": "X"}, "aussteller": {"aussteller1": "SERIALNUMBER = 3, C = DE, O = SM-PKI-DE, CN = T-Systems-EnergyCA.CA", "aussteller2": "X", "aussteller3": "X", "aussteller4": "X", "aussteller5": "X"}, "zertifikatsNutzer": {"zertifikatsNutzer1": "X", "zertifikatsNutzer2": "X", "zertifikatsNutzer3": "X", "zertifikatsNutzer4": "X", "zertifikatsNutzer5": "X"}, "IPAdresseCLSDevice": {"IPAdresseCLSDevice1": "123.222.345.876", "IPAdresseCLSDevice2": "X", "IPAdresseCLSDevice3": "X", "IPAdresseCLSDevice4": "X", "IPAdresseCLSDevice5": "X"}}], "VERWENDUNGSZEITRAUM": [{"boTyp": "VERWENDUNGSZEITRAUM", "versionStruktur": "1", "zeitraumId": 1, "datenqualitaet": "ERWARTETE_DATEN", "verwendungAb": "2025-06-23T22:00:00Z", "verwendungBis": "2025-07-23T22:00:00Z"}, {"boTyp": "VERWENDUNGSZEITRAUM", "versionStruktur": "1", "zeitraumId": 2, "datenqualitaet": "ERWARTETE_DATEN", "verwendungAb": "2025-07-23T22:00:00Z"}], "MARKTLOKATION": [{"boTyp": "MARKTLOKATION", "versionStruktur": "1", "sparte": "STROM", "gueltigkeitszeitraum": {"zeitraumId": 1, "startdatum": "2025-06-23T22:00:00Z", "enddatum": "2025-07-23T22:00:00Z"}, "datenqualitaet": "ERWARTETE_DATEN", "zaehlwerke": [{"obisKennzahl": "1-1:1.9.1", "zaehlzeiten": {"zaehlzeitDefinition": "ABC", "register": "XYZ"}, "wertegranularitaet": "JAEHRLICH"}]}, {"boTyp": "MARKTLOKATION", "versionStruktur": "1", "sparte": "STROM", "gueltigkeitszeitraum": {"zeitraumId": 2, "startdatum": "2025-07-23T22:00:00Z"}, "datenqualitaet": "ERWARTETE_DATEN", "zaehlwerke": [{"obisKennzahl": "1-1:1.9.1", "zaehlzeiten": {"zaehlzeitDefinition": "ABC", "register": "XYZ"}, "wertegranularitaet": "JAEHRLICH"}]}], "ZAEHLER": [{"boTyp": "ZAEHLER", "versionStruktur": "1", "zaehlernummer": "12345667891", "sparte": "STROM", "gueltigkeitszeitraum": {"zeitraumId": 1, "startdatum": "2025-06-23T22:00:00Z", "enddatum": "2025-07-23T22:00:00Z"}, "datenqualitaet": "ERWARTETE_DATEN", "zaehlwerke": [{"bezeichnung": "HT", "obisKennzahl": "1-1:1.8.1", "vorkommastelle": 8, "nachkommastelle": 3, "zaehlzeiten": {"zaehlzeitDefinition": "ABC", "register": "XYZ"}, "konfiguration": "34590456ujdfsdghdlktztwqq-053trg", "wertegranularitaet": "JAEHRLICH"}], "gateway": "1234567890", "geraete": [{"geraetenummer": "1234567890", "geraeteeigenschaften": {"geraetetyp": "SMARTMETERGATEWAY"}}]}, {"boTyp": "ZAEHLER", "versionStruktur": "1", "zaehlernummer": "12345667891", "sparte": "STROM", "gueltigkeitszeitraum": {"zeitraumId": 2, "startdatum": "2025-07-23T22:00:00Z"}, "datenqualitaet": "ERWARTETE_DATEN", "zaehlwerke": [{"bezeichnung": "HT", "obisKennzahl": "1-1:1.8.1", "vorkommastelle": 8, "nachkommastelle": 3, "zaehlzeiten": {"zaehlzeitDefinition": "ABC", "register": "XYZ"}, "konfiguration": "34590456ujdfsdghdlktztwqq-053trg", "wertegranularitaet": "JAEHRLICH"}], "gateway": "1234567890", "geraete": [{"geraetenummer": "1234567890", "geraeteeigenschaften": {"geraetetyp": "SMARTMETERGATEWAY"}}]}]}, "transaktionsdaten": {"datenaustauschreferenz": "DAXOXILSWLJTQB", "sparte": "STROM", "transaktionsgrund": "ZY9", "anfragereferenznummer": "64739202", "vorgangsnummer": "24062416225400000000000102159662011", "pruefidentifikator": "55555", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9903729000007", "rollencodetyp": "BDEW", "ipAdresse": "X", "ipRange": {"untereGrenze": "X", "obereGrenze": "X"}, "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "nachname": "P GETTY", "rufnummern": [{"nummerntyp": "RUF_DURCHWAHL", "rufnummer": "+3222271020"}]}}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9904990000008", "rollencodetyp": "BDEW"}, "dokumentennummer": "DA882411080716289903323000007541914", "kategorie": "E03", "nachrichtendatum": "2025-06-24T12:31:00Z", "nachrichtenreferenznummer": "DAESNJTWNDGGFS", "antwortStatusZeitraum": [{"code": "A02", "liste": "E_0412", "zeitraumId": 1}, {"code": "A02", "liste": "E_0412", "zeitraumId": 2}], "nachrichtenReferenzBestellbestaetigung": "98786423423435", "vorgangsReferenzBestellbestaetigung": "12"}, "zusatzdaten": {}}}, {"name": "55655", "summary": "55655 — Rückmeldung/Anfrage Daten der MaLo", "value": {"stammdaten": {"MARKTLOKATION": [{"boTyp": "MARKTLOKATION", "versionStruktur": "1", "marktlokationsId": "50074561188", "marktlokationsTyp": [{"typ": "STANDARD_MARKTLOKATION"}], "sparte": "STROM"}]}, "transaktionsdaten": {"datenaustauschreferenz": "M0MCOKU7", "sparte": "STROM", "transaktionsgrund": "ZX6", "transaktionsgrundergaenzung": "ZW4", "vorgangsnummer": "123456", "pruefidentifikator": "55655", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9903790000002", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9904446000007", "rollencodetyp": "BDEW"}, "dokumentennummer": "BGMM0G8KNAH", "kategorie": "E03", "nachrichtendatum": "2026-10-02T11:00:00Z", "nachrichtenreferenznummer": "UNHM04IMMLI", "anfragereferenznummer": "ABC123456", "verwendungAb": "2025-04-02T22:00:00Z", "antwortStatusZeitraum": [{"code": "A01", "liste": "E_0412", "zeitraumId": 1}]}, "zusatzdaten": {}}}, {"name": "55656", "summary": "55656 — Rückmeldung/Anfrage Daten der SR", "value": {"stammdaten": {"STEUERBARE_RESSOURCE": [{"boTyp": "STEUERBARE_RESSOURCE", "versionStruktur": "1", "ressourcenId": "C816417ST77", "sparte": "STROM"}]}, "transaktionsdaten": {"datenaustauschreferenz": "M0M0RQ8N", "sparte": "STROM", "transaktionsgrund": "ZX9", "vorgangsnummer": "123456", "pruefidentifikator": "55656", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9903790000002", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9904446000007", "rollencodetyp": "BDEW"}, "dokumentennummer": "BGMM06P2PF5", "kategorie": "E03", "nachrichtendatum": "2026-10-02T11:00:00Z", "nachrichtenreferenznummer": "UNHM0QBQIBF", "anfragereferenznummer": "ABC123456", "antwortStatusZeitraum": [{"code": "A01", "liste": "E_0412", "zeitraumId": 1}]}, "zusatzdaten": {}}}, {"name": "55657", "summary": "55657 — Rückmeldung/Anfrage Daten der Tranche", "value": {"stammdaten": {"TRANCHE": [{"boTyp": "TRANCHE", "versionStruktur": "1", "tranchenId": "50074561189", "sparte": "STROM"}]}, "transaktionsdaten": {"datenaustauschreferenz": "LZU6I5XQ", "sparte": "STROM", "transaktionsgrund": "ZY1", "vorgangsnummer": "123456", "pruefidentifikator": "55657", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9903790000002", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9904446000007", "rollencodetyp": "BDEW"}, "dokumentennummer": "BGMLZW5R6XV", "kategorie": "E03", "nachrichtendatum": "2026-10-02T11:00:00Z", "nachrichtenreferenznummer": "UNHLZZ3QVVC", "anfragereferenznummer": "ABC123456", "antwortStatusZeitraum": [{"code": "A01", "liste": "E_0412", "zeitraumId": 1}]}, "zusatzdaten": {}}}, {"name": "55658", "summary": "55658 — Rückmeldung/Anfrage Daten der MeLo", "value": {"stammdaten": {"VERWENDUNGSZEITRAUM": [{"boTyp": "VERWENDUNGSZEITRAUM", "versionStruktur": "1", "zeitraumId": 1, "datenqualitaet": "ERWARTETE_DATEN", "verwendungAb": "2024-12-31T23:00:00Z"}], "MESSLOKATION": [{"boTyp": "MESSLOKATION", "versionStruktur": "1", "messlokationsId": "DE0032106765712000000000000001217", "sparte": "STROM", "gueltigkeitszeitraum": {"zeitraumId": 1, "startdatum": "2024-12-31T23:00:00Z"}, "datenqualitaet": "ERWARTETE_DATEN", "netzebenemessung": "NSP", "ablesekartenempfaenger": {"boTyp": "GESCHAEFTSPARTNER", "versionStruktur": "1", "name1": "Max", "name2": "Musterman", "gewerbekennzeichnung": false, "geschaeftspartnerrolle": ["ABLESEKARTENEMPFAENGER"], "partneradresse": {"postleitzahl": "99423", "ort": "Weimar", "strasse": "Erfurter Str.", "postfach": "46", "landescode": "DE"}}}], "ZAEHLER": [{"boTyp": "ZAEHLER", "versionStruktur": "1", "zaehlernummer": "1LOG0067003468", "sparte": "STROM", "gueltigkeitszeitraum": {"zeitraumId": 1, "startdatum": "2024-12-31T23:00:00Z"}, "datenqualitaet": "ERWARTETE_DATEN", "zaehlerauspraegung": "EINRICHTUNGSZAEHLER", "zaehlertyp": "MODERNEMESSEINRICHTUNG", "tarifart": "ZWEITARIF", "zaehlwerke": [{"bezeichnung": "HT", "obisKennzahl": "1-0:1.8.0", "vorkommastelle": 7, "nachkommastelle": 3, "konfiguration": "34590456ujdfsdghdlktztwqq-053trg", "wertegranularitaet": "JAEHRLICH"}], "gateway": "1ESY0012345678", "zaehlertypspezifikation": "MME_STANDARD", "geraete": [{"geraetenummer": "1ESY0012345678", "geraeteeigenschaften": {"geraetetyp": "SMARTMETERGATEWAY"}}, {"geraetenummer": "1LOG0067003000", "geraeteeigenschaften": {"geraetetyp": "WANDLER", "geraetemerkmal": "KOMBIMESSWANDLER", "faktor": 1}}]}]}, "transaktionsdaten": {"datenaustauschreferenz": "M3C4Q0HK", "sparte": "STROM", "transaktionsgrund": "ZX7", "vorgangsnummer": "KBG27094210000000000929931413171000", "pruefidentifikator": "55658", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900496000001", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900496000002", "rollencodetyp": "BDEW"}, "dokumentennummer": "BGMM303C8J7", "kategorie": "E03", "nachrichtendatum": "2026-10-02T11:00:00Z", "nachrichtenreferenznummer": "UNHM30L6XWP", "anfragereferenznummer": "NNV1230", "antwortStatusZeitraum": [{"code": "A02", "liste": "E_0412", "zeitraumId": 1}]}, "zusatzdaten": {}}}]}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend fort, nachdem die Nachricht erstellt ist.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="4" anker="schritt-4" richtung="eingehend" kopf={{"links": {"label": "LF", "eigen": true}, "rechts": {"label": "MSB"}}}>

### Bearbeitungsstand zur Bestellung

<Schrittskizze sicht={{"label": "LF"}} zeilen={[{"art": "empfangen", "label": "MSB", "weg": "AS4", "nachrichten": [{"nr": "21047", "titel": "Bearbeitungsstandsmeldung"}]}, {"art": "aperak", "werte": ["Z33"]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [21047](/schnittstellen/202610/pruefi/IFTSTA/PI_21047) — Bearbeitungsstandsmeldung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **MSB** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `21047` → [E_0585](/referenz/202610/ebd/E_0585) · MSB · Bestellung zur Stammdatenänderung prüfen (Basiert auf EBD: E_0573_Bestellung zur Stammdatenänderung prüfen)

</div>

</li>

<li data-teil="aperak">

**Aperak-Prüfungen**
- `21047` → `Z33` — Aperak Prüfung: Ist referenzierte Nachricht bekannt ?

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202610/backend-schreiben-lf/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": false, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend mit den Daten der eingegangenen Nachricht fort.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="5" anker="schritt-5" richtung="fremd" kopf={{"links": {"label": "weiterer MSB", "eigen": false}, "rechts": {"label": "MSB"}}}>

### Bestellung einer Änderung von Stammdaten vom weiteren MSB an MSB

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55664](/schnittstellen/202610/pruefi/UTILMD/PI_55664) — Rückmeldung/Anfrage Daten der NeLo · AS4
- [55555](/schnittstellen/202610/pruefi/UTILMD/PI_55555) — Anfrage Daten der individuellen Bestellung · AS4
- [55665](/schnittstellen/202610/pruefi/UTILMD/PI_55665) — Rückmeldung/Anfrage Daten der MaLo · AS4
- [55666](/schnittstellen/202610/pruefi/UTILMD/PI_55666) — Rückmeldung/Anfrage Daten der SR · AS4
- [55667](/schnittstellen/202610/pruefi/UTILMD/PI_55667) — Rückmeldung/Anfrage Daten der Tranche · AS4
- [55669](/schnittstellen/202610/pruefi/UTILMD/PI_55669) — Rückmeldung/Anfrage Daten der MeLo · AS4

</div>

</Schritt>

<Schritt nr="6" anker="schritt-6" richtung="fremd" kopf={{"links": {"label": "MSB", "eigen": false}, "rechts": {"label": "weiterer MSB"}}}>

### Bearbeitungsstand zur Bestellung

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [21047](/schnittstellen/202610/pruefi/IFTSTA/PI_21047) — Bearbeitungsstandsmeldung · AS4

</div>

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `21047` → [E_0584](/referenz/202610/ebd/E_0584) · MSB · Bestellung zur Stammdatenänderung prüfen (Basiert auf EBD: E_0573_Bestellung zur Stammdatenänderung prüfen)

</div>

</Schritt>

<Schritt nr="7" anker="schritt-7" richtung="fremd" kopf={{"links": {"label": "ÜNB", "eigen": false}, "rechts": {"label": "MSB"}}}>

### Bestellung einer Änderung von Stammdaten vom ÜNB an MSB

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55685](/schnittstellen/202610/pruefi/UTILMD/PI_55685) — Rückmeldung/Anfrage Daten der MaLo · AS4
- [55687](/schnittstellen/202610/pruefi/UTILMD/PI_55687) — Rückmeldung/Anfrage Daten der Tranche · AS4

</div>

</Schritt>

<Schritt nr="8" anker="schritt-8" richtung="fremd" kopf={{"links": {"label": "MSB", "eigen": false}, "rechts": {"label": "ÜNB"}}}>

### Bearbeitungsstand zur Bestellung

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [21047](/schnittstellen/202610/pruefi/IFTSTA/PI_21047) — Bearbeitungsstandsmeldung · AS4

</div>

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `21047` → [E_0587](/referenz/202610/ebd/E_0587) · MSB · Bestellung zur Stammdatenänderung prüfen (Basiert auf EBD: E_0573_Bestellung zur Stammdatenänderung prüfen)

</div>

</Schritt>

<details>
<summary>Entscheidungsbäume dieses Prozesses</summary>

| EBD | Name |
|---|---|
| [E_0585](/referenz/202610/ebd/E_0585) | Bestellung zur Stammdatenänderung prüfen (Basiert auf EBD: E_0573_Bestellung zur Stammdatenänderung prüfen) |
| [E_0584](/referenz/202610/ebd/E_0584) | Bestellung zur Stammdatenänderung prüfen (Basiert auf EBD: E_0573_Bestellung zur Stammdatenänderung prüfen) |
| [E_0586](/referenz/202610/ebd/E_0586) | Bestellung zur Stammdatenänderung prüfen (Basiert auf EBD: E_0573_Bestellung zur Stammdatenänderung prüfen) |
| [E_0587](/referenz/202610/ebd/E_0587) | Bestellung zur Stammdatenänderung prüfen (Basiert auf EBD: E_0573_Bestellung zur Stammdatenänderung prüfen) |

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

- Im Fall des SD „Bestellung zur Stammdatenänderung an MSB (verantwortlich)“ gilt: Der verantwortliche MSB einer Messlokation ist immer der MSB, der zum Zeitpunkt, zu dem die Änderung des Werts des Stammdatums erfolgt, der Messlokation zugeordnet ist. Dabei gilt folgende Ausnahme: Findet an der Messlokation der Use-Case „[Geräteübernahme](/prozessdoku/202610/MSB--MSBA/WiM-Teil1-geraeteuebernahme)“ (WiM Teil 1) statt, ist neben dem vorgenannten MSB (im Use-Case „[Geräteübernahme](/prozessdoku/202610/MSB--MSBA/WiM-Teil1-geraeteuebernahme)“ als MSBA bezeichnet) auch der MSBN berechtigt für diese Messlokation das SD „[Stammdatenänderung vom MSB (verantwortlich) ausgehend](/prozessdoku/202610/LF/GPKE-Teil4-stammdatenaenderung-vom-msb-verantwortlich-ausgehend)“ als verantwortlicher MSB anzuwenden. Demensprechend können die Berechtigten wiederum eine Bestellung zur Stammdatenänderung an den MSBN senden.

</li>

<li data-blatt="anlass">

### Anlass

- Dem Berechtigten liegt für ein Stammdatum ein neuer Wert vor.
- Der Berechtigte geht von einem Datenschiefstand zwischen den Berechtigten und dem Verantwortlichen aus.

</li>

<li data-blatt="erste-nachricht">

### Erste Nachricht

Der Beteiligte dieser Seite sendet selbst: „Bestellung einer Änderung von Stammdaten vom LF an MSB“ an **MSB** (Schritt 3).

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

- [Sicht NB](/prozessdoku/202610/NB/GPKE-Teil4-bestellung-zur-stammdatenaenderung-an-msb-verantwortlich) — NB
- [Sicht MSB](/prozessdoku/202610/MSB/GPKE-Teil4-bestellung-zur-stammdatenaenderung-an-msb-verantwortlich) — MSB
- [Sicht WMSB](/prozessdoku/202610/MSB--WMSB/GPKE-Teil4-bestellung-zur-stammdatenaenderung-an-msb-verantwortlich) — weiterer Messstellenbetreiber · Marktrolle MSB
- [Sicht ÜNB](/prozessdoku/202610/UENB/GPKE-Teil4-bestellung-zur-stammdatenaenderung-an-msb-verantwortlich) — ÜNB · Marktrolle UENB

<Hinweisbereich>

*Die Schritte sind die **möglichen** Nachrichten dieses Prozesses, keine Abfolge — die Quelle führt weder Bedingungen noch Alternativen. Das Kästchen am Schritt nennt links die eigene Sicht: **←** empfängt sie, **→** sendet sie. Zugeklappte Schritte laufen zwischen anderen Marktpartnern.*

Zu den Prüfidentifikatoren dieser Schritte liegt kein Testfall im Testbestand; der Knopf »Ausprobieren« der schreibenden Schnittstelle bietet deshalb keinen Rumpf an.

Betrifft: [4](#schritt-4)

</Hinweisbereich>
