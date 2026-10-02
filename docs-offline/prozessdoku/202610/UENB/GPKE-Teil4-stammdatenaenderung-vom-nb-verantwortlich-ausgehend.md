# Stammdatenänderung vom NB (verantwortlich) ausgehend — Sicht ÜNB

<Kopf rolle="UENB" beteiligter="ÜNB" festlegung="GPKE" dokument="GPKE Teil 4" kapitel="1.4.2" sparte="Strom" schritte={9} suchtitel="Stammdatenänderung vom NB (verantwortlich) ausgehend — Sicht ÜNB (Marktrolle UENB) · GPKE Teil 4 · Formatversion 202610" abschnitte={[{"id": "abschnitt-ablauf", "label": "Prozessablauf"}, {"id": "abschnitt-schritte", "label": "Prozessschritte"}, {"id": "abschnitt-informationen", "label": "Prozess-Informationen"}, {"id": "abschnitt-sichten", "label": "Andere Sichten des Prozesses"}]} />

<Kurzfassung>

Der Prozess beschreibt die Übermittlung von geänderten Werten von Stammdaten vom Verantwortlichen an die Berechtigten. Der Berechtigte prüft die Daten und gibt dem Verantwortlichen eine Qualitätsrückmeldung zum Inhalt der Daten. Sofern der Berechtigte einen anderen Inhalt der Daten erwartet, gibt er dies in der Rückmeldung an. Der Verantwortliche teilt dem Berechtigten in diesem Fall den Bearbeitungstand zu dessen Rückmeldung mit.

</Kurzfassung>

<a id="abschnitt-ablauf"></a>

## Prozessablauf aus Sicht des ÜNB

<Systembild svg={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1004 545\" width=\"1004\" height=\"545\" role=\"img\" aria-labelledby=\"sb-title\" class=\"maco-systembild\">\n<title id=\"sb-title\">Systembild: Stammdatenänderung vom NB (verantwortlich) ausgehend aus Sicht ÜNB</title>\n<defs><marker id=\"sb-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect class=\"sb-lane-kopf\" x=\"16\" y=\"12\" width=\"232\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend-System des Kunden</text>\n<rect class=\"sb-lane-kopf\" x=\"398\" y=\"12\" width=\"264\" height=\"46\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · ÜNB</text>\n<rect class=\"sb-lane-kopf\" x=\"812\" y=\"12\" width=\"176\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"900\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Marktpartner</text>\n<line x1=\"323\" y1=\"58\" x2=\"323\" y2=\"533\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"737\" y1=\"58\" x2=\"737\" y2=\"533\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"80\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">8. Änderung vom NB an ÜNB</text>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"78\" r=\"5\"/><line x1=\"900\" y1=\"83\" x2=\"900\" y2=\"95\"/><line x1=\"893\" y1=\"87\" x2=\"907\" y2=\"87\"/><line x1=\"900\" y1=\"95\" x2=\"894\" y2=\"105\"/><line x1=\"900\" y1=\"95\" x2=\"906\" y2=\"105\"/></g>\n<text x=\"900\" y=\"127\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"878\" y1=\"96\" x2=\"628\" y2=\"96\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"88\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"112\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">55688, 55691</text>\n<rect class=\"sb-kasten sb-schreiben\" x=\"432\" y=\"163\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"183\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"113\" x2=\"530\" y2=\"163\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-schreiben sb-abgeleitet\" x=\"34\" y=\"163\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"183\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten erstellen</text>\n<line x1=\"432\" y1=\"179\" x2=\"230\" y2=\"179\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"171\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"227\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"247\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">9. Rückmeldung auf</text>\n<text x=\"530\" y=\"262\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Änderung</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"196\" x2=\"530\" y2=\"227\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"233\" r=\"5\"/><line x1=\"900\" y1=\"238\" x2=\"900\" y2=\"250\"/><line x1=\"893\" y1=\"242\" x2=\"907\" y2=\"242\"/><line x1=\"900\" y1=\"250\" x2=\"894\" y2=\"260\"/><line x1=\"900\" y1=\"250\" x2=\"906\" y2=\"260\"/></g>\n<text x=\"900\" y=\"282\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"628\" y1=\"251\" x2=\"878\" y2=\"251\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"243\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"267\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">55689, 55692</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"310\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"330\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"275\" x2=\"530\" y2=\"310\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"310\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"330\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"326\" x2=\"230\" y2=\"326\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"318\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"374\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"394\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">10. Bearbeitungsstand zur</text>\n<text x=\"530\" y=\"409\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Rückmeldung</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"343\" x2=\"530\" y2=\"374\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"380\" r=\"5\"/><line x1=\"900\" y1=\"385\" x2=\"900\" y2=\"397\"/><line x1=\"893\" y1=\"389\" x2=\"907\" y2=\"389\"/><line x1=\"900\" y1=\"397\" x2=\"894\" y2=\"407\"/><line x1=\"900\" y1=\"397\" x2=\"906\" y2=\"407\"/></g>\n<text x=\"900\" y=\"429\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"878\" y1=\"398\" x2=\"628\" y2=\"398\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"390\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"414\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">21047</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"457\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"477\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"422\" x2=\"530\" y2=\"457\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben sb-abgeleitet\" x=\"34\" y=\"457\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"477\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"473\" x2=\"230\" y2=\"473\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"465\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n</svg>"} gesamt={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1218 858\" width=\"1218\" height=\"858\" role=\"img\" aria-labelledby=\"sd-title\" class=\"maco-sequence\">\n<title id=\"sd-title\">Sequenzdiagramm: Stammdatenänderung vom NB (verantwortlich) ausgehend aus Sicht ÜNB</title>\n<defs><marker id=\"sd-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect x=\"16\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"121\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend (Kunde)</text>\n<line x1=\"121\" y1=\"64\" x2=\"121\" y2=\"846\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"260\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"365\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · ÜNB</text>\n<line x1=\"365\" y1=\"64\" x2=\"365\" y2=\"846\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"504\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"609\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"609\" y1=\"64\" x2=\"609\" y2=\"846\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"748\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"853\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">LF</text>\n<line x1=\"853\" y1=\"64\" x2=\"853\" y2=\"846\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"992\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"1097\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">MSB</text>\n<line x1=\"1097\" y1=\"64\" x2=\"1097\" y2=\"846\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"609\" y1=\"90\" x2=\"853\" y2=\"90\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"731\" y=\"81\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">1. Änderung vom NB an LF</text>\n<text x=\"731\" y=\"105\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55615, 55620, 55175…</text>\n<line x1=\"853\" y1=\"152\" x2=\"609\" y2=\"152\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"731\" y=\"143\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">2. Rückmeldung auf Änderung</text>\n<text x=\"731\" y=\"167\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55621, 55180, 55227… · E_0408</text>\n<text x=\"731\" y=\"180\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0408 — Änderung vom NB prüfen</text>\n<line x1=\"609\" y1=\"214\" x2=\"853\" y2=\"214\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"731\" y=\"205\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">3. Bearbeitungsstand zur Rückmeldung</text>\n<text x=\"731\" y=\"229\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 21047 · E_0626</text>\n<text x=\"731\" y=\"242\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0626 — Rückmeldung auf Änderung prüfen</text>\n<line x1=\"609\" y1=\"276\" x2=\"1097\" y2=\"276\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"853\" y=\"267\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">4. Änderung vom NB an MSB</text>\n<text x=\"853\" y=\"291\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55627, 55173, 55628…</text>\n<line x1=\"1097\" y1=\"338\" x2=\"609\" y2=\"338\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"853\" y=\"329\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">5. Rückmeldung auf Änderung</text>\n<text x=\"853\" y=\"353\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55633, 55177, 55634… · E_0409</text>\n<text x=\"853\" y=\"366\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0409 — Änderung vom NB prüfen</text>\n<line x1=\"609\" y1=\"400\" x2=\"1097\" y2=\"400\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"853\" y=\"391\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">6. Bearbeitungsstand zur Rückmeldung</text>\n<text x=\"853\" y=\"415\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 21047 · E_0627</text>\n<text x=\"853\" y=\"428\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0627 — Rückmeldung auf Änderung prüfen</text>\n<line x1=\"609\" y1=\"462\" x2=\"365\" y2=\"462\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"453\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">8. Änderung vom NB an ÜNB</text>\n<text x=\"487\" y=\"477\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55688, 55691</text>\n<line x1=\"365\" y1=\"524\" x2=\"121\" y2=\"524\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"515\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<text x=\"243\" y=\"539\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten erstellen</text>\n<line x1=\"365\" y1=\"586\" x2=\"609\" y2=\"586\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"577\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">9. Rückmeldung auf Änderung</text>\n<text x=\"487\" y=\"601\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55689, 55692 · E_0572</text>\n<text x=\"487\" y=\"614\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0572 — Änderung vom NB prüfen</text>\n<line x1=\"365\" y1=\"648\" x2=\"121\" y2=\"648\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"639\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"663\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"609\" y1=\"710\" x2=\"365\" y2=\"710\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"701\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">10. Bearbeitungsstand zur Rückmeldung</text>\n<text x=\"487\" y=\"725\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 21047 · E_0628</text>\n<text x=\"487\" y=\"738\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0628 — Rückmeldung auf Änderung prüfen</text>\n<line x1=\"365\" y1=\"772\" x2=\"121\" y2=\"772\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"763\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"787\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n</svg>"} titel="ÜNB" />

<a id="abschnitt-schritte"></a>

## Prozessschritte

<Schritt nr="1" anker="schritt-1" richtung="fremd" kopf={{"links": {"label": "NB", "eigen": false}, "rechts": {"label": "LF"}}}>

### Änderung vom NB an LF

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55615](/schnittstellen/202610/pruefi/UTILMD/PI_55615) — Änderung Daten der NeLo · AS4
- [55620](/schnittstellen/202610/pruefi/UTILMD/PI_55620) — Änderung Daten der MeLo · AS4
- [55175](/schnittstellen/202610/pruefi/UTILMD/PI_55175) — Änderung der Lokationsbündelstruktur · AS4
- [55225](/schnittstellen/202610/pruefi/UTILMD/PI_55225) — Änderung Blindabr.-Daten der NeLo · AS4
- [55616](/schnittstellen/202610/pruefi/UTILMD/PI_55616) — Änderung Daten der MaLo · AS4
- [55617](/schnittstellen/202610/pruefi/UTILMD/PI_55617) — Änderung Daten der TR · AS4
- [55618](/schnittstellen/202610/pruefi/UTILMD/PI_55618) — Änderung Daten der SR · AS4
- [55619](/schnittstellen/202610/pruefi/UTILMD/PI_55619) — Änderung Daten der Tranche · AS4
- [55691](/schnittstellen/202610/pruefi/UTILMD/PI_55691) — Änderung Paket-ID der MaLo · AS4

</div>

</Schritt>

<Schritt nr="2" anker="schritt-2" richtung="fremd" kopf={{"links": {"label": "LF", "eigen": false}, "rechts": {"label": "NB"}}}>

### Rückmeldung auf Änderung

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55621](/schnittstellen/202610/pruefi/UTILMD/PI_55621) — Rückmeldung/Anfrage Daten zur NeLo · AS4
- [55180](/schnittstellen/202610/pruefi/UTILMD/PI_55180) — Rückmeldung/Anfrage Lokationsbündelstruktur · AS4
- [55227](/schnittstellen/202610/pruefi/UTILMD/PI_55227) — Rückmeldung/Anfrage Blindabr.-Daten der NeLo · AS4
- [55622](/schnittstellen/202610/pruefi/UTILMD/PI_55622) — Rückmeldung/Anfrage Daten der MaLo · AS4
- [55623](/schnittstellen/202610/pruefi/UTILMD/PI_55623) — Rückmeldung/Anfrage Daten der TR · AS4
- [55624](/schnittstellen/202610/pruefi/UTILMD/PI_55624) — Rückmeldung/Anfrage Daten der SR · AS4
- [55625](/schnittstellen/202610/pruefi/UTILMD/PI_55625) — Rückmeldung/Anfrage Daten der Tranche · AS4
- [55626](/schnittstellen/202610/pruefi/UTILMD/PI_55626) — Rückmeldung/Anfrage Daten der MeLo · AS4
- [55692](/schnittstellen/202610/pruefi/UTILMD/PI_55692) — Rückmeldung/Anfrage Paket-ID der MaLo · AS4

</div>

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `55621`, `55180`, `55227`, `55622`, `55623`, `55624`, `55625`, `55626`, `55692` → [E_0408](/referenz/202610/ebd/E_0408) · LF · Änderung vom NB prüfen

</div>

</Schritt>

<Schritt nr="3" anker="schritt-3" richtung="fremd" kopf={{"links": {"label": "NB", "eigen": false}, "rechts": {"label": "LF"}}}>

### Bearbeitungsstand zur Rückmeldung

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [21047](/schnittstellen/202610/pruefi/IFTSTA/PI_21047) — Bearbeitungsstandsmeldung · AS4

</div>

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `21047` → [E_0626](/referenz/202610/ebd/E_0626) · NB · Rückmeldung auf Änderung prüfen

</div>

</Schritt>

<Schritt nr="4" anker="schritt-4" richtung="fremd" kopf={{"links": {"label": "NB", "eigen": false}, "rechts": {"label": "MSB"}}}>

### Änderung vom NB an MSB

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55627](/schnittstellen/202610/pruefi/UTILMD/PI_55627) — Änderung Daten der NeLo · AS4
- [55173](/schnittstellen/202610/pruefi/UTILMD/PI_55173) — Änderung der Lokationsbündelstruktur · AS4
- [55628](/schnittstellen/202610/pruefi/UTILMD/PI_55628) — Änderung Daten der MaLo · AS4
- [55629](/schnittstellen/202610/pruefi/UTILMD/PI_55629) — Änderung Daten der TR · AS4
- [55630](/schnittstellen/202610/pruefi/UTILMD/PI_55630) — Änderung Daten der SR · AS4
- [55632](/schnittstellen/202610/pruefi/UTILMD/PI_55632) — Änderung Daten der MeLo · AS4
- [55691](/schnittstellen/202610/pruefi/UTILMD/PI_55691) — Änderung Paket-ID der MaLo · AS4

</div>

</Schritt>

<Schritt nr="5" anker="schritt-5" richtung="fremd" kopf={{"links": {"label": "MSB", "eigen": false}, "rechts": {"label": "NB"}}}>

### Rückmeldung auf Änderung

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55633](/schnittstellen/202610/pruefi/UTILMD/PI_55633) — Rückmeldung/Anfrage Daten zur NeLo · AS4
- [55177](/schnittstellen/202610/pruefi/UTILMD/PI_55177) — Rückmeldung/Anfrage Lokationsbündelstruktur · AS4
- [55634](/schnittstellen/202610/pruefi/UTILMD/PI_55634) — Rückmeldung/Anfrage Daten der MaLo · AS4
- [55635](/schnittstellen/202610/pruefi/UTILMD/PI_55635) — Rückmeldung/Anfrage Daten der TR · AS4
- [55636](/schnittstellen/202610/pruefi/UTILMD/PI_55636) — Rückmeldung/Anfrage Daten der SR · AS4
- [55638](/schnittstellen/202610/pruefi/UTILMD/PI_55638) — Rückmeldung/Anfrage Daten der MeLo · AS4
- [55692](/schnittstellen/202610/pruefi/UTILMD/PI_55692) — Rückmeldung/Anfrage Paket-ID der MaLo · AS4

</div>

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `55633`, `55177`, `55634`, `55635`, `55636`, `55638`, `55692` → [E_0409](/referenz/202610/ebd/E_0409) · MSB · Änderung vom NB prüfen (Basiert auf EBD: E_0408_Änderung vom NB prüfen)

</div>

</Schritt>

<Schritt nr="6" anker="schritt-6" richtung="fremd" kopf={{"links": {"label": "NB", "eigen": false}, "rechts": {"label": "MSB"}}}>

### Bearbeitungsstand zur Rückmeldung

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [21047](/schnittstellen/202610/pruefi/IFTSTA/PI_21047) — Bearbeitungsstandsmeldung · AS4

</div>

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `21047` → [E_0627](/referenz/202610/ebd/E_0627) · NB · Rückmeldung auf Änderung prüfen (Basiert auf EBD: E_0626_Rückmeldung auf Änderung prüfen)

</div>

</Schritt>

<Schritt nr="8" anker="schritt-8" richtung="eingehend" kopf={{"links": {"label": "ÜNB", "eigen": true}, "rechts": {"label": "NB"}}}>

### Änderung vom NB an ÜNB

<Schrittskizze sicht={{"label": "ÜNB"}} zeilen={[{"art": "empfangen", "label": "NB", "weg": "AS4", "nachrichten": [{"nr": "55688", "titel": "Änderung Daten der MaLo"}, {"nr": "55691", "titel": "Änderung Paket-ID der MaLo"}]}, {"art": "erstellen"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55688](/schnittstellen/202610/pruefi/UTILMD/PI_55688) — Änderung Daten der MaLo · AS4
- [55691](/schnittstellen/202610/pruefi/UTILMD/PI_55691) — Änderung Paket-ID der MaLo · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **NB** · AS4

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

<Schritt nr="9" anker="schritt-9" richtung="ausgehend" kopf={{"links": {"label": "ÜNB", "eigen": true}, "rechts": {"label": "NB"}}}>

### Rückmeldung auf Änderung

<Schrittskizze sicht={{"label": "ÜNB"}} zeilen={[{"art": "senden", "label": "NB", "weg": "AS4", "nachrichten": [{"nr": "55689", "titel": "Rückmeldung/Anfrage Daten der MaLo"}, {"nr": "55692", "titel": "Rückmeldung/Anfrage Paket-ID der MaLo"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55689](/schnittstellen/202610/pruefi/UTILMD/PI_55689) — Rückmeldung/Anfrage Daten der MaLo · AS4
- [55692](/schnittstellen/202610/pruefi/UTILMD/PI_55692) — Rückmeldung/Anfrage Paket-ID der MaLo · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht an **NB** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `55689`, `55692` → [E_0572](/referenz/202610/ebd/E_0572) · ÜNB · Änderung vom NB prüfen (Basiert auf EBD: E_0408_Änderung vom NB prüfen)

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

<Schritt nr="10" anker="schritt-10" richtung="eingehend" kopf={{"links": {"label": "ÜNB", "eigen": true}, "rechts": {"label": "NB"}}}>

### Bearbeitungsstand zur Rückmeldung

<Schrittskizze sicht={{"label": "ÜNB"}} zeilen={[{"art": "empfangen", "label": "NB", "weg": "AS4", "nachrichten": [{"nr": "21047", "titel": "Bearbeitungsstandsmeldung"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [21047](/schnittstellen/202610/pruefi/IFTSTA/PI_21047) — Bearbeitungsstandsmeldung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **NB** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `21047` → [E_0628](/referenz/202610/ebd/E_0628) · NB · Rückmeldung auf Änderung prüfen (Basiert auf EBD: E_0626_Rückmeldung auf Änderung prüfen)

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
| [E_0572](/referenz/202610/ebd/E_0572) | Änderung vom NB prüfen (Basiert auf EBD: E_0408_Änderung vom NB prüfen) |
| [E_0628](/referenz/202610/ebd/E_0628) | Rückmeldung auf Änderung prüfen (Basiert auf EBD: E_0626_Rückmeldung auf Änderung prüfen) |
| [E_0408](/referenz/202610/ebd/E_0408) | Änderung vom NB prüfen |
| [E_0409](/referenz/202610/ebd/E_0409) | Änderung vom NB prüfen (Basiert auf EBD: E_0408_Änderung vom NB prüfen) |
| [E_0626](/referenz/202610/ebd/E_0626) | Rückmeldung auf Änderung prüfen |
| [E_0627](/referenz/202610/ebd/E_0627) | Rückmeldung auf Änderung prüfen (Basiert auf EBD: E_0626_Rückmeldung auf Änderung prüfen) |

</details>

<a id="abschnitt-informationen"></a>

## Prozess-Informationen

Wortlaut der Lesefassung, Steckbrief Kap. 1.4.1, S. 5.

<Stepper>
<ol>

<li data-blatt="vorbedingungen">

### Vorbedingungen

- Es besteht eine aktuelle oder zukünftig abgestimmte Zuordnung der Marktpartner in der jeweiligen Rolle zur Lokation.

</li>

<li data-blatt="ergebnisse">

### Ergebnisse

- Die Folgeprozesse setzen auf abgeglichenen und synchronen Werten der Stammdaten ab dem Änderungsdatum auf.
- Durch die in diesem Use-Case durchgeführte Änderung kann es unter anderem dazu kommen, dass eine Wertübermittlung vom MSB erforderlich ist. Die Beauftragung der Werteübermittlung ergibt sich aus den Werten des entsprechenden Stammdatums. Es erfolgt keine weitere Beauftragung gegenüber dem MSB.

</li>

<li data-blatt="fehlerfall">

### Fehlerfall

#### Ergebnis im Fehlerfall

Der Verantwortliche muss in ein bilaterales Clearing mit den Beteiligten einsteigen und ggf. den Prozess erneut anstoßen.

#### Fehlerfälle

Die Rückmeldung ergibt den Rückschluss, dass die Daten nicht synchron im Markt vorliegen.

</li>

<li data-blatt="anforderungen">

### Weitere Anforderungen

- Im Fall des SD „[Stammdatenänderung vom MSB (verantwortlich) ausgehend](/prozessdoku/202610/UENB/GPKE-Teil4-stammdatenaenderung-vom-msb-verantwortlich-ausgehend)“ gilt: Der verantwortliche MSB einer Messlokation ist immer der MSB, der zum Zeitpunkt, zu dem die Änderung des Werts des Stammdatums erfolgt, der Messlokation zugeordnet ist. Dabei gilt folgende Ausnahme: Findet an der Messlokation der Use-Case „[Geräteübernahme](/prozessdoku/202610/MSB--MSBA/WiM-Teil1-geraeteuebernahme)“ (WiM Teil 1) statt, ist neben dem vorgenannten MSB (im Use-Case „[Geräteübernahme](/prozessdoku/202610/MSB--MSBA/WiM-Teil1-geraeteuebernahme)“ als MSBA bezeichnet) auch der MSBN berechtigt für diese Messlokation das SD „[Stammdatenänderung vom MSB (verantwortlich) ausgehend](/prozessdoku/202610/UENB/GPKE-Teil4-stammdatenaenderung-vom-msb-verantwortlich-ausgehend)“ als verantwortlicher MSB anzuwenden.

</li>

<li data-blatt="anlass">

### Anlass

- Bei dem für ein Stammdatum Verantwortlichen liegt ein neuer Wert für das Stammdatum vor. Diese Erkenntnis erhält der Verantwortliche z.B. aufgrund vorangehender Prozesse oder Nachrichten, die die Änderung eines Wertes eines Stammdatums für ein oder mehrere Berechtigte verursachen.
- Der Verantwortliche geht von einem Datenschiefstand zwischen den Berechtigten und dem Verantwortlichen aus.

**Vorher läuft:** [Abrechnungsdaten Bilanzkreisabrechnung](/prozessdoku/202610/UENB/GPKE-Teil2-abrechnungsdaten-bilanzkreisabrechnung), [Beginn der Ersatz-/Grundversorgung](/prozessdoku/202610/LF/GPKE-Teil2-beginn-der-ersatz-grundversorgung), [Fall 1: LF-Zuordnung bei EEG-Marktlokation ohne DV-Pflicht bzw. KWKG-Marktlokation ohne DV-Pflicht](/prozessdoku/202610/LF/GPKE-Teil2-fall-1-lf-zuordnung-bei-eeg-marktlokation-ohne-dv-pflicht-bzw-kwkg-marktlokation-ohne-dv-pflicht), [Fall 2: LF-Zuordnung bei EEG-Marktlokation mit DV-Pflicht](/prozessdoku/202610/LF--LFA/GPKE-Teil2-fall-2-lf-zuordnung-bei-eeg-marktlokation-mit-dv-pflicht), [Fall 3: LF-Zuordnung bei KWKG-Marktlokation mit DV-Pflicht bzw. Nicht-EEG-/Nicht-KWKG-Marktlokation und Marktlokation wird nicht-tranchiert abgebildet](/prozessdoku/202610/LF--LFA/GPKE-Teil2-fall-3-lf-zuordnung-bei-kwkg-marktlokation-mit-dv-pflicht-bzw-nicht-eeg-nicht-kwkg-marktlokation-und-marktlokation-wird-nicht-tranchiert-abgebildet), [Fall 4: LF-Zuordnung bei KWKG-Marktlokation mit DV-Pflicht bzw. Nicht-EEG-/Nicht-KWKG-Marktlokation und Marktlokation wird tranchiert abgebildet](/prozessdoku/202610/LF--LFA/GPKE-Teil2-fall-4-lf-zuordnung-bei-kwkg-marktlokation-mit-dv-pflicht-bzw-nicht-eeg-nicht-kwkg-marktlokation-und-marktlokation-wird-tranchiert-abgebildet), [Lieferbeginn](/prozessdoku/202610/LF--LFA/GPKE-Teil2-lieferbeginn), [Lieferende von NB an LF](/prozessdoku/202610/LF/GPKE-Teil2-lieferende-von-nb-an-lf), [Neuanlage](/prozessdoku/202610/LF/GPKE-Teil2-neuanlage), [Übermittlung der Berechnungsformel](/prozessdoku/202610/LF/WiM-Teil2-uebermittlung-der-berechnungsformel) — diese Prozesse nennen den hier gezeigten in ihrem Ergebnis.

</li>

<li data-blatt="erste-nachricht">

### Erste Nachricht

**NB** sendet „Änderung vom NB an ÜNB“ (Schritt 8). Ab hier ist der Beteiligte dieser Seite am Zug.

</li>

<li data-blatt="ziel">

### Ziel

Dem Verantwortlichen und den Berechtigten liegen die gleichen Werte der Stammdaten vor.

</li>

</ol>
</Stepper>

<a id="abschnitt-sichten"></a>

## Andere Sichten des Prozesses

Derselbe Prozess, aus den Augen der anderen Beteiligten: dieselben Schritte, jeweils aus deren Sicht gelesen.

- [Sicht LF](/prozessdoku/202610/LF/GPKE-Teil4-stammdatenaenderung-vom-nb-verantwortlich-ausgehend) — LF
- [Sicht NB](/prozessdoku/202610/NB/GPKE-Teil4-stammdatenaenderung-vom-nb-verantwortlich-ausgehend) — NB
- [Sicht MSB](/prozessdoku/202610/MSB/GPKE-Teil4-stammdatenaenderung-vom-nb-verantwortlich-ausgehend) — MSB

<Hinweisbereich>

*Die Schritte sind die **möglichen** Nachrichten dieses Prozesses, keine Abfolge — die Quelle führt weder Bedingungen noch Alternativen. Das Kästchen am Schritt nennt links die eigene Sicht: **←** empfängt sie, **→** sendet sie. Zugeklappte Schritte laufen zwischen anderen Marktpartnern. Die Nummern sind die der Quelle; wo eine fehlt, fehlt sie dort.*

Die Konnektortabelle führt für diese Schritte keinen Schreibaufruf. Abgeleitet aus dem Prozessverlauf: Mit ihrer Nachricht beginnt der Prozess für die eigene Rolle, der Vorgang entsteht also neu.

Betrifft: [8](#schritt-8)

Die Konnektortabelle führt für diese Schritte keinen Schreibaufruf. Abgeleitet aus dem Prozessverlauf: Die eigene Rolle war an diesem Prozess schon beteiligt, der Vorgang besteht also.

Betrifft: [10](#schritt-10)

Für diese Marktrolle liegt kein Schreibkatalog vor; am Schritt steht deshalb nur das Kommando des Schreibaufrufs, ohne Adresse und ohne Knopf.

Betrifft: [8](#schritt-8), [9](#schritt-9), [10](#schritt-10)

</Hinweisbereich>
