# Bestellung zur Stammdatenänderung an LF (verantwortlich) — Sicht NB

<Kopf rolle="NB" beteiligter="NB" festlegung="GPKE" dokument="GPKE Teil 4" kapitel="1.5.3" sparte="Strom" schritte={6} suchtitel="Bestellung zur Stammdatenänderung an LF (verantwortlich) — Sicht NB · GPKE Teil 4 · Formatversion 202610" abschnitte={[{"id": "abschnitt-ablauf", "label": "Prozessablauf"}, {"id": "abschnitt-schritte", "label": "Prozessschritte"}, {"id": "abschnitt-informationen", "label": "Prozess-Informationen"}, {"id": "abschnitt-sichten", "label": "Andere Sichten des Prozesses"}]} />

<Kurzfassung>

Der Prozess beschreibt die Anfrage/ Bestellung von Werten von Stammdaten durch einen Berechtigten beim Verantwortlichen der Stammdaten. Der Verantwortiche prüft die Bestellung und teilt dem Berechtigten den Bearbeitungsstand mit.

</Kurzfassung>

<a id="abschnitt-ablauf"></a>

## Prozessablauf aus Sicht des NB

<Systembild svg={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1004 754\" width=\"1004\" height=\"754\" role=\"img\" aria-labelledby=\"sb-title\" class=\"maco-systembild\">\n<title id=\"sb-title\">Systembild: Bestellung zur Stammdatenänderung an LF (verantwortlich) aus Sicht NB</title>\n<defs><marker id=\"sb-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect class=\"sb-lane-kopf\" x=\"16\" y=\"12\" width=\"232\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend-System des Kunden</text>\n<rect class=\"sb-lane-kopf\" x=\"398\" y=\"12\" width=\"264\" height=\"46\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · NB</text>\n<rect class=\"sb-lane-kopf\" x=\"812\" y=\"12\" width=\"176\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"900\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Marktpartner</text>\n<line x1=\"323\" y1=\"58\" x2=\"323\" y2=\"742\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"737\" y1=\"58\" x2=\"737\" y2=\"742\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect class=\"sb-kasten sb-folge_ausloeser\" x=\"432\" y=\"80\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Ausgelöst durch Eingang:</text>\n<text x=\"530\" y=\"115\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">55109, 55230</text>\n<rect class=\"sb-kasten sb-trigger\" x=\"432\" y=\"154\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"174\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessauslöser empfangen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"128\" x2=\"530\" y2=\"154\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-trigger\" x=\"34\" y=\"154\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"174\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">START_BESTELLUNG_SDAE</text>\n<line x1=\"230\" y1=\"170\" x2=\"432\" y2=\"170\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"162\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-lesen_verarbeitung\" x=\"432\" y=\"218\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"238\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Daten für die Verarbeitung</text>\n<text x=\"530\" y=\"253\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">laden</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"187\" x2=\"530\" y2=\"218\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-lesen_verarbeitung\" x=\"34\" y=\"218\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"238\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">2 Lese-Schnittstellen</text>\n<text x=\"132\" y=\"253\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">aufgerufen</text>\n<line x1=\"432\" y1=\"242\" x2=\"230\" y2=\"242\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"234\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<text x=\"331\" y=\"258\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">je einzeln am Schritt</text>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"292\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"312\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">1. Bestellung einer Änderung</text>\n<text x=\"530\" y=\"327\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">von Stammdaten vom NB an</text>\n<text x=\"530\" y=\"342\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">LF</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"266\" x2=\"530\" y2=\"292\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"305\" r=\"5\"/><line x1=\"900\" y1=\"310\" x2=\"900\" y2=\"322\"/><line x1=\"893\" y1=\"314\" x2=\"907\" y2=\"314\"/><line x1=\"900\" y1=\"322\" x2=\"894\" y2=\"332\"/><line x1=\"900\" y1=\"322\" x2=\"906\" y2=\"332\"/></g>\n<text x=\"900\" y=\"354\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">LF</text>\n<line x1=\"628\" y1=\"323\" x2=\"878\" y2=\"323\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"315\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"339\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">55137, 55232</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"381\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"401\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"355\" x2=\"530\" y2=\"381\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"381\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"401\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"397\" x2=\"230\" y2=\"397\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"389\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"445\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"465\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">2. Bearbeitungsstand zur</text>\n<text x=\"530\" y=\"480\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Bestellung</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"414\" x2=\"530\" y2=\"445\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"451\" r=\"5\"/><line x1=\"900\" y1=\"456\" x2=\"900\" y2=\"468\"/><line x1=\"893\" y1=\"460\" x2=\"907\" y2=\"460\"/><line x1=\"900\" y1=\"468\" x2=\"894\" y2=\"478\"/><line x1=\"900\" y1=\"468\" x2=\"906\" y2=\"478\"/></g>\n<text x=\"900\" y=\"500\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">LF</text>\n<line x1=\"878\" y1=\"469\" x2=\"628\" y2=\"469\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"461\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"485\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">21047</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"528\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"548\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z33</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"493\" x2=\"530\" y2=\"528\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"592\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"612\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"561\" x2=\"530\" y2=\"592\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"592\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"612\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"608\" x2=\"230\" y2=\"608\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"600\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-folgeprozess\" x=\"432\" y=\"656\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"676\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Folgeprozess auslösen:</text>\n<text x=\"530\" y=\"691\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">21047</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"625\" x2=\"530\" y2=\"656\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n</svg>"} gesamt={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1218 672\" width=\"1218\" height=\"672\" role=\"img\" aria-labelledby=\"sd-title\" class=\"maco-sequence\">\n<title id=\"sd-title\">Sequenzdiagramm: Bestellung zur Stammdatenänderung an LF (verantwortlich) aus Sicht NB</title>\n<defs><marker id=\"sd-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect x=\"16\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"121\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend (Kunde)</text>\n<line x1=\"121\" y1=\"64\" x2=\"121\" y2=\"660\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"260\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"365\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · NB</text>\n<line x1=\"365\" y1=\"64\" x2=\"365\" y2=\"660\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"504\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"609\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">LF</text>\n<line x1=\"609\" y1=\"64\" x2=\"609\" y2=\"660\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"748\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"853\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">MSB</text>\n<line x1=\"853\" y1=\"64\" x2=\"853\" y2=\"660\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"992\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"1097\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">ÜNB</text>\n<line x1=\"1097\" y1=\"64\" x2=\"1097\" y2=\"660\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"121\" y1=\"90\" x2=\"365\" y2=\"90\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"81\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">START_BESTELLUNG_SDAE</text>\n<text x=\"243\" y=\"105\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Trigger-Event</text>\n<line x1=\"365\" y1=\"152\" x2=\"609\" y2=\"152\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"143\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">1. Bestellung einer Änderung von Stammdaten vom…</text>\n<text x=\"487\" y=\"167\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55137, 55232</text>\n<line x1=\"365\" y1=\"214\" x2=\"121\" y2=\"214\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"205\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"229\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"609\" y1=\"276\" x2=\"365\" y2=\"276\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"267\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">2. Bearbeitungsstand zur Bestellung</text>\n<text x=\"487\" y=\"291\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 21047 · E_0588</text>\n<text x=\"487\" y=\"304\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0588 — Bestellung zur Stammdatenänderung prüfen</text>\n<line x1=\"365\" y1=\"338\" x2=\"121\" y2=\"338\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"329\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"353\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"853\" y1=\"400\" x2=\"609\" y2=\"400\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"731\" y=\"391\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">3. Bestellung einer Änderung von Stammdaten vom…</text>\n<text x=\"731\" y=\"415\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55136</text>\n<line x1=\"609\" y1=\"462\" x2=\"853\" y2=\"462\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"731\" y=\"453\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">4. Bearbeitungsstand zur Bestellung</text>\n<text x=\"731\" y=\"477\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 21047 · E_0589</text>\n<text x=\"731\" y=\"490\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0589 — Bestellung zur Stammdatenänderung prüfen</text>\n<line x1=\"1097\" y1=\"524\" x2=\"609\" y2=\"524\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"853\" y=\"515\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">5. Bestellung einer Änderung von Stammdaten vom…</text>\n<line x1=\"609\" y1=\"586\" x2=\"1097\" y2=\"586\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"853\" y=\"577\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">6. Bearbeitungsstand zur Bestellung</text>\n</svg>"} titel="NB" />

<a id="abschnitt-schritte"></a>

## Prozessschritte

<Schritt nr="1" anker="schritt-1" richtung="ausgehend" kopf={{"links": {"label": "NB", "eigen": true}, "rechts": {"label": "LF"}}}>

### Bestellung einer Änderung von Stammdaten vom NB an LF

<Schrittskizze sicht={{"label": "NB"}} zeilen={[{"art": "folge_ausloeser", "werte": ["55109", "55230"]}, {"art": "ausloeser", "werte": ["START_BESTELLUNG_SDAE"]}, {"art": "lesen_verarbeitung", "schnittstellen": [{"label": "Marktlokation lesen"}, {"label": "Netzlokation lesen"}]}, {"art": "senden", "label": "LF", "weg": "AS4", "nachrichten": [{"nr": "55137", "titel": "Rückmeldung/Anfrage Daten der MaLo"}, {"nr": "55232", "titel": "Rückmeldung/Anfrage Blindabr.-Daten der NeLo"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55137](/schnittstellen/202610/pruefi/UTILMD/PI_55137) — Rückmeldung/Anfrage Daten der MaLo · AS4
- [55232](/schnittstellen/202610/pruefi/UTILMD/PI_55232) — Rückmeldung/Anfrage Blindabr.-Daten der NeLo · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="folge_ausloeser">

**Ausgelöst durch Eingang**
- [55109](/schnittstellen/202610/pruefi/UTILMD/PI_55109)
- [55230](/schnittstellen/202610/pruefi/UTILMD/PI_55230)

Die MACO APP sendet diese Nachricht selbst, als Folgeprozess nach einem dieser Eingänge. Daneben kann das Backend diesen Schritt mit einem Ereignis anstoßen — der nächste Punkt.

</li>

<li data-teil="ausloeser">

**Prozessauslöser** [`START_BESTELLUNG_SDAE`](/schnittstellen/202610/trigger/events/NB-START_BESTELLUNG_SDAE) · [Im Playground ausprobieren](/api/202610/ausloeser-nb/start-bestellung-sdae)

Das Backend stößt diesen Schritt mit diesem Ereignis an.

</li>

<li data-teil="lesen" data-stufe="verarbeitung">

**Daten für die Verarbeitung laden**
- [Marktlokation lesen](/api/202610/backend-lesen/getmarketlocationbasic#marktlokation-lesen) `GET /getMarketLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getMarketLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": false, "defaultValue": "MALO", "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": false, "defaultValue": "2024-06-28T12:18:00Z", "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_MARKTLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Netzlokation lesen](/api/202610/backend-lesen/getgridlocationbasic#netzlokation-lesen) `GET /getGridLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getGridLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_NETZLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

</li>

<li data-teil="nachricht">

Nachricht an **LF** · AS4

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202610/backend-schreiben-nb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"ENERGIELIEFERVERTRAG\": [\n      {\n        \"boTyp\": \"VERTRAG\",\n        \"datenqualitaet\": \"IM_SYSTEM_VORHANDENE_DATEN\",\n        \"enFG\": [\n          {\n            \"grund\": [\n              \"ENFG_ELEKTRISCH_ANGETRIEBENE_WAERMEPUMPEN\"\n            ],\n            \"grundlageVerringerungUmlagen\": \"ERFUELLT_VORAUSSETZUNG_NACH_ENFG\"\n          }\n        ],\n        \"gueltigkeitszeitraum\": {\n          \"enddatum\": \"2026-07-23T22:00:00Z\",\n          \"startdatum\": \"2026-06-23T22:00:00Z\",\n          \"zeitraumId\": 1\n        },\n        \"korrespondenzpartner\": {\n          \"ansprechpartner\": {\n            \"boTyp\": \"ANSPRECHPARTNER\",\n            \"eMailAdresse\": \"max@mustermann.de\",\n            \"versionStruktur\": \"1\"\n          },\n          \"boTyp\": \"GESCHAEFTSPARTNER\",\n          \"gewerbekennzeichnung\": false,\n          \"name1\": \"Fank Müller\",\n          \"partneradresse\": {\n            \"hausnummer\": \"25\",\n            \"landescode\": \"DE\",\n            \"ort\": \"Musterstadt\",\n            \"ortsteil\": \"Musterortsteil\",\n            \"postleitzahl\": \"55555\",\n            \"strasse\": \"Wohnstrasse\"\n          },\n          \"versionStruktur\": \"1\"\n        },\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\",\n        \"vertragsart\": \"ENERGIELIEFERVERTRAG\",\n        \"vertragspartner2\": [\n          {\n            \"boTyp\": \"GESCHAEFTSPARTNER\",\n            \"geschaeftspartnerrolle\": [\n              \"KUNDE\"\n            ],\n            \"gewerbekennzeichnung\": true,\n            \"name1\": \"Firma AG\",\n            \"name2\": \"Musterfirma\",\n            \"versionStruktur\": \"1\"\n          }\n        ]\n      },\n      {\n        \"boTyp\": \"VERTRAG\",\n        \"datenqualitaet\": \"IM_SYSTEM_VORHANDENE_DATEN\",\n        \"enFG\": [\n          {\n            \"grund\": [\n              \"ENFG_ELEKTRISCH_ANGETRIEBENE_WAERMEPUMPEN\"\n            ],\n            \"grundlageVerringerungUmlagen\": \"ERFUELLT_VORAUSSETZUNG_NACH_ENFG\"\n          }\n        ],\n        \"gueltigkeitszeitraum\": {\n          \"startdatum\": \"2026-07-23T22:00:00Z\",\n          \"zeitraumId\": 2\n        },\n        \"korrespondenzpartner\": {\n          \"ansprechpartner\": {\n            \"boTyp\": \"ANSPRECHPARTNER\",\n            \"eMailAdresse\": \"max@mustermann.de\",\n            \"versionStruktur\": \"1\"\n          },\n          \"boTyp\": \"GESCHAEFTSPARTNER\",\n          \"gewerbekennzeichnung\": false,\n          \"name1\": \"Fank Müller\",\n          \"partneradresse\": {\n            \"hausnummer\": \"25\",\n            \"landescode\": \"DE\",\n            \"ort\": \"Musterstadt\",\n            \"ortsteil\": \"Musterortsteil\",\n            \"postleitzahl\": \"55555\",\n            \"strasse\": \"Wohnstrasse\"\n          },\n          \"versionStruktur\": \"1\"\n        },\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\",\n        \"vertragsart\": \"ENERGIELIEFERVERTRAG\",\n        \"vertragspartner2\": [\n          {\n            \"boTyp\": \"GESCHAEFTSPARTNER\",\n            \"externeReferenzen\": [\n              {\n                \"exRefName\": \"Kundennummer beim Lieferanten\",\n                \"exRefWert\": \"KD_NB_09881\"\n              }\n            ],\n            \"geschaeftspartnerrolle\": [\n              \"KUNDE\"\n            ],\n            \"gewerbekennzeichnung\": true,\n            \"name1\": \"Firma AG\",\n            \"name2\": \"Musterfirma\",\n            \"versionStruktur\": \"1\"\n          }\n        ]\n      }\n    ],\n    \"MARKTLOKATION\": [\n      {\n        \"boTyp\": \"MARKTLOKATION\",\n        \"datenqualitaet\": \"ERWARTETE_DATEN\",\n        \"gueltigkeitszeitraum\": {\n          \"enddatum\": \"2026-07-23T22:00:00Z\",\n          \"startdatum\": \"2026-06-23T22:00:00Z\",\n          \"zeitraumId\": 1\n        },\n        \"marktlokationsId\": \"20072281644\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      },\n      {\n        \"boTyp\": \"MARKTLOKATION\",\n        \"datenqualitaet\": \"ERWARTETE_DATEN\",\n        \"gueltigkeitszeitraum\": {\n          \"startdatum\": \"2026-07-23T22:00:00Z\",\n          \"zeitraumId\": 2\n        },\n        \"marktlokationsId\": \"20072281644\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"NETZNUTZUNGSVERTRAG\": [\n      {\n        \"boTyp\": \"VERTRAG\",\n        \"datenqualitaet\": \"ERWARTETE_DATEN\",\n        \"gueltigkeitszeitraum\": {\n          \"enddatum\": \"2026-07-23T22:00:00Z\",\n          \"startdatum\": \"2026-06-23T22:00:00Z\",\n          \"zeitraumId\": 1\n        },\n        \"lokationsId\": \"20072281644\",\n        \"lokationsTyp\": \"MALO\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\",\n        \"vertragsart\": \"NETZNUTZUNGSVERTRAG\",\n        \"vertragskonditionen\": {\n          \"haushaltskunde\": true\n        }\n      },\n      {\n        \"boTyp\": \"VERTRAG\",\n        \"datenqualitaet\": \"ERWARTETE_DATEN\",\n        \"gueltigkeitszeitraum\": {\n          \"startdatum\": \"2026-07-23T22:00:00Z\",\n          \"zeitraumId\": 2\n        },\n        \"lokationsId\": \"20072281644\",\n        \"lokationsTyp\": \"MALO\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\",\n        \"vertragsart\": \"NETZNUTZUNGSVERTRAG\",\n        \"vertragskonditionen\": {\n          \"haushaltskunde\": true\n        }\n      }\n    ],\n    \"VERWENDUNGSZEITRAUM\": [\n      {\n        \"boTyp\": \"VERWENDUNGSZEITRAUM\",\n        \"datenqualitaet\": \"ERWARTETE_DATEN\",\n        \"versionStruktur\": \"1\",\n        \"verwendungAb\": \"2026-06-23T22:00:00Z\",\n        \"verwendungBis\": \"2026-07-23T22:00:00Z\",\n        \"zeitraumId\": 1\n      },\n      {\n        \"boTyp\": \"VERWENDUNGSZEITRAUM\",\n        \"datenqualitaet\": \"ERWARTETE_DATEN\",\n        \"versionStruktur\": \"1\",\n        \"verwendungAb\": \"2026-07-23T22:00:00Z\",\n        \"zeitraumId\": 2\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9900327000009\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"anfragereferenznummer\": \"ANFRAGE1234\",\n    \"antwortStatusZeitraum\": [\n      {\n        \"code\": \"A02\",\n        \"liste\": \"E_0410\",\n        \"zeitraumId\": 1\n      },\n      {\n        \"code\": \"A02\",\n        \"liste\": \"E_0410\",\n        \"zeitraumId\": 2\n      }\n    ],\n    \"datenaustauschreferenz\": \"DAFNGBYOWMAHHK\",\n    \"dokumentennummer\": \"DA562411051029459903323000007131355\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9903729000007\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"E03\",\n    \"nachrichtendatum\": \"2026-10-02T11:00:00Z\",\n    \"nachrichtenreferenznummer\": \"DAMTEJVKUBPRZQ\",\n    \"pruefidentifikator\": \"55137\",\n    \"sparte\": \"STROM\",\n    \"transaktionsgrund\": \"ZX6\",\n    \"transaktionsgrundergaenzung\": \"ZW4\",\n    \"vorgangsnummer\": \"24062416225400000000000102159662011\"\n  },\n  \"zusatzdaten\": {}\n}"} examples={[{"mediaType": "application/json", "examples": [{"name": "55137", "summary": "55137 — Rückmeldung/Anfrage Daten der MaLo", "value": {"stammdaten": {"VERWENDUNGSZEITRAUM": [{"boTyp": "VERWENDUNGSZEITRAUM", "versionStruktur": "1", "zeitraumId": 1, "datenqualitaet": "ERWARTETE_DATEN", "verwendungAb": "2026-06-23T22:00:00Z", "verwendungBis": "2026-07-23T22:00:00Z"}, {"boTyp": "VERWENDUNGSZEITRAUM", "versionStruktur": "1", "zeitraumId": 2, "datenqualitaet": "ERWARTETE_DATEN", "verwendungAb": "2026-07-23T22:00:00Z"}], "MARKTLOKATION": [{"boTyp": "MARKTLOKATION", "versionStruktur": "1", "marktlokationsId": "20072281644", "sparte": "STROM", "gueltigkeitszeitraum": {"zeitraumId": 1, "startdatum": "2026-06-23T22:00:00Z", "enddatum": "2026-07-23T22:00:00Z"}, "datenqualitaet": "ERWARTETE_DATEN"}, {"boTyp": "MARKTLOKATION", "versionStruktur": "1", "marktlokationsId": "20072281644", "sparte": "STROM", "gueltigkeitszeitraum": {"zeitraumId": 2, "startdatum": "2026-07-23T22:00:00Z"}, "datenqualitaet": "ERWARTETE_DATEN"}], "NETZNUTZUNGSVERTRAG": [{"boTyp": "VERTRAG", "versionStruktur": "1", "vertragsart": "NETZNUTZUNGSVERTRAG", "sparte": "STROM", "gueltigkeitszeitraum": {"zeitraumId": 1, "startdatum": "2026-06-23T22:00:00Z", "enddatum": "2026-07-23T22:00:00Z"}, "datenqualitaet": "ERWARTETE_DATEN", "vertragskonditionen": {"haushaltskunde": true}, "lokationsId": "20072281644", "lokationsTyp": "MALO"}, {"boTyp": "VERTRAG", "versionStruktur": "1", "vertragsart": "NETZNUTZUNGSVERTRAG", "sparte": "STROM", "gueltigkeitszeitraum": {"zeitraumId": 2, "startdatum": "2026-07-23T22:00:00Z"}, "datenqualitaet": "ERWARTETE_DATEN", "vertragskonditionen": {"haushaltskunde": true}, "lokationsId": "20072281644", "lokationsTyp": "MALO"}], "ENERGIELIEFERVERTRAG": [{"boTyp": "VERTRAG", "versionStruktur": "1", "vertragsart": "ENERGIELIEFERVERTRAG", "sparte": "STROM", "gueltigkeitszeitraum": {"zeitraumId": 1, "startdatum": "2026-06-23T22:00:00Z", "enddatum": "2026-07-23T22:00:00Z"}, "datenqualitaet": "IM_SYSTEM_VORHANDENE_DATEN", "vertragspartner2": [{"boTyp": "GESCHAEFTSPARTNER", "versionStruktur": "1", "name1": "Firma AG", "name2": "Musterfirma", "gewerbekennzeichnung": true, "geschaeftspartnerrolle": ["KUNDE"]}], "korrespondenzpartner": {"boTyp": "GESCHAEFTSPARTNER", "versionStruktur": "1", "name1": "Fank Müller", "gewerbekennzeichnung": false, "partneradresse": {"postleitzahl": "55555", "ort": "Musterstadt", "strasse": "Wohnstrasse", "hausnummer": "25", "landescode": "DE", "ortsteil": "Musterortsteil"}, "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "eMailAdresse": "max@mustermann.de"}}, "enFG": [{"grundlageVerringerungUmlagen": "ERFUELLT_VORAUSSETZUNG_NACH_ENFG", "grund": ["ENFG_ELEKTRISCH_ANGETRIEBENE_WAERMEPUMPEN"]}]}, {"boTyp": "VERTRAG", "versionStruktur": "1", "vertragsart": "ENERGIELIEFERVERTRAG", "sparte": "STROM", "gueltigkeitszeitraum": {"zeitraumId": 2, "startdatum": "2026-07-23T22:00:00Z"}, "datenqualitaet": "IM_SYSTEM_VORHANDENE_DATEN", "vertragspartner2": [{"boTyp": "GESCHAEFTSPARTNER", "versionStruktur": "1", "name1": "Firma AG", "name2": "Musterfirma", "gewerbekennzeichnung": true, "geschaeftspartnerrolle": ["KUNDE"], "externeReferenzen": [{"exRefName": "Kundennummer beim Lieferanten", "exRefWert": "KD_NB_09881"}]}], "korrespondenzpartner": {"boTyp": "GESCHAEFTSPARTNER", "versionStruktur": "1", "name1": "Fank Müller", "gewerbekennzeichnung": false, "partneradresse": {"postleitzahl": "55555", "ort": "Musterstadt", "strasse": "Wohnstrasse", "hausnummer": "25", "landescode": "DE", "ortsteil": "Musterortsteil"}, "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "eMailAdresse": "max@mustermann.de"}}, "enFG": [{"grundlageVerringerungUmlagen": "ERFUELLT_VORAUSSETZUNG_NACH_ENFG", "grund": ["ENFG_ELEKTRISCH_ANGETRIEBENE_WAERMEPUMPEN"]}]}]}, "transaktionsdaten": {"datenaustauschreferenz": "DAFNGBYOWMAHHK", "sparte": "STROM", "transaktionsgrund": "ZX6", "transaktionsgrundergaenzung": "ZW4", "vorgangsnummer": "24062416225400000000000102159662011", "pruefidentifikator": "55137", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9900327000009", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9903729000007", "rollencodetyp": "BDEW"}, "dokumentennummer": "DA562411051029459903323000007131355", "kategorie": "E03", "nachrichtendatum": "2026-10-02T11:00:00Z", "nachrichtenreferenznummer": "DAMTEJVKUBPRZQ", "anfragereferenznummer": "ANFRAGE1234", "antwortStatusZeitraum": [{"code": "A02", "liste": "E_0410", "zeitraumId": 1}, {"code": "A02", "liste": "E_0410", "zeitraumId": 2}]}, "zusatzdaten": {}}}, {"name": "55232", "summary": "55232 — Rückmeldung/Anfrage Blindabr.-Daten der NeLo", "value": {"stammdaten": {"VERWENDUNGSZEITRAUM": [{"boTyp": "VERWENDUNGSZEITRAUM", "versionStruktur": "1", "zeitraumId": 1, "datenqualitaet": "ERWARTETE_DATEN", "verwendungAb": "2025-06-23T22:00:00Z", "verwendungBis": "2025-07-23T22:00:00Z"}, {"boTyp": "VERWENDUNGSZEITRAUM", "versionStruktur": "1", "zeitraumId": 2, "datenqualitaet": "ERWARTETE_DATEN", "verwendungAb": "2025-07-23T22:00:00Z"}], "NETZLOKATION": [{"boTyp": "NETZLOKATION", "versionStruktur": "1", "netzlokationsId": "E1688117482", "sparte": "STROM", "gueltigkeitszeitraum": {"zeitraumId": 1, "startdatum": "2025-06-23T22:00:00Z", "enddatum": "2025-07-23T22:00:00Z"}, "datenqualitaet": "ERWARTETE_DATEN", "abrechnungsdaten": [{"zahlerBlindarbeitLf": true}]}, {"boTyp": "NETZLOKATION", "versionStruktur": "1", "netzlokationsId": "E1688117482", "sparte": "STROM", "gueltigkeitszeitraum": {"zeitraumId": 2, "startdatum": "2025-07-23T22:00:00Z"}, "datenqualitaet": "ERWARTETE_DATEN", "abrechnungsdaten": [{"zahlerBlindarbeitLf": true}]}]}, "transaktionsdaten": {"datenaustauschreferenz": "DAYDCIOIMLGMSJ", "sparte": "STROM", "transaktionsgrund": "ZX5", "vorgangsnummer": "24062416225400000000000102159662011", "pruefidentifikator": "55232", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900327000009", "rollencodetyp": "BDEW", "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "nachname": "P GETTY", "rufnummern": [{"nummerntyp": "RUF_DURCHWAHL", "rufnummer": "+3222271020"}]}}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9903729000007", "rollencodetyp": "BDEW"}, "dokumentennummer": "DA282411080644049903323000007822937", "kategorie": "E03", "nachrichtendatum": "2025-06-24T12:31:00Z", "nachrichtenreferenznummer": "DAYNHRQTSJDZDM", "anfragereferenznummer": "RBL1234", "antwortStatusZeitraum": [{"code": "A02", "liste": "E_0410", "zeitraumId": 1}, {"code": "A02", "liste": "E_0410", "zeitraumId": 2}]}, "zusatzdaten": {}}}]}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend fort, nachdem die Nachricht erstellt ist.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="2" anker="schritt-2" richtung="eingehend" kopf={{"links": {"label": "NB", "eigen": true}, "rechts": {"label": "LF"}}}>

### Bearbeitungsstand zur Bestellung

<Schrittskizze sicht={{"label": "NB"}} zeilen={[{"art": "empfangen", "label": "LF", "weg": "AS4", "nachrichten": [{"nr": "21047", "titel": "Bearbeitungsstandsmeldung"}]}, {"art": "aperak", "werte": ["Z33"]}, {"art": "fortschreiben"}, {"art": "folgeprozess", "werte": ["21047"]}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [21047](/schnittstellen/202610/pruefi/IFTSTA/PI_21047) — Bearbeitungsstandsmeldung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **LF** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `21047` → [E_0588](/referenz/202610/ebd/E_0588) · LF · Bestellung zur Stammdatenänderung prüfen (Basiert auf EBD: E_0573_Bestellung zur Stammdatenänderung prüfen)

</div>

</li>

<li data-teil="aperak">

**Aperak-Prüfungen**
- `21047` → `Z33`

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202610/backend-schreiben-nb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend mit den Daten der eingegangenen Nachricht fort.

</li>

<li data-teil="folgeprozess">

**Folgeprozess auslösen**
- [21047](/schnittstellen/202610/pruefi/IFTSTA/PI_21047) — Bearbeitungsstandsmeldung

Nach der Verarbeitung startet die MACO APP diesen Folgeprozess selbst.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="3" anker="schritt-3" richtung="fremd" kopf={{"links": {"label": "MSB", "eigen": false}, "rechts": {"label": "LF"}}}>

### Bestellung einer Änderung von Stammdaten vom MSB an LF

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55136](/schnittstellen/202610/pruefi/UTILMD/PI_55136) — Rückmeldung/Anfrage Daten der MaLo · AS4

</div>

</Schritt>

<Schritt nr="4" anker="schritt-4" richtung="fremd" kopf={{"links": {"label": "LF", "eigen": false}, "rechts": {"label": "MSB"}}}>

### Bearbeitungsstand zur Bestellung

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [21047](/schnittstellen/202610/pruefi/IFTSTA/PI_21047) — Bearbeitungsstandsmeldung · AS4

</div>

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `21047` → [E_0589](/referenz/202610/ebd/E_0589) · LF · Bestellung zur Stammdatenänderung prüfen (Basiert auf EBD: E_0573_Bestellung zur Stammdatenänderung prüfen)

</div>

</Schritt>

<Schritt nr="5" anker="schritt-5" richtung="fremd" kopf={{"links": {"label": "ÜNB", "eigen": false}, "rechts": {"label": "LF"}}}>

### Bestellung einer Änderung von Stammdaten vom ÜNB an LF

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

</Schritt>

<Schritt nr="6" anker="schritt-6" richtung="fremd" kopf={{"links": {"label": "LF", "eigen": false}, "rechts": {"label": "ÜNB"}}}>

### Bearbeitungsstand zur Bestellung

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

</Schritt>

<details>
<summary>Entscheidungsbäume dieses Prozesses</summary>

| EBD | Name |
|---|---|
| [E_0588](/referenz/202610/ebd/E_0588) | Bestellung zur Stammdatenänderung prüfen (Basiert auf EBD: E_0573_Bestellung zur Stammdatenänderung prüfen) |
| [E_0589](/referenz/202610/ebd/E_0589) | Bestellung zur Stammdatenänderung prüfen (Basiert auf EBD: E_0573_Bestellung zur Stammdatenänderung prüfen) |

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

- Im Fall des SD „[Bestellung zur Stammdatenänderung an MSB (verantwortlich)](/prozessdoku/202610/NB/GPKE-Teil4-bestellung-zur-stammdatenaenderung-an-msb-verantwortlich)“ gilt: Der verantwortliche MSB einer Messlokation ist immer der MSB, der zum Zeitpunkt, zu dem die Änderung des Werts des Stammdatums erfolgt, der Messlokation zugeordnet ist. Dabei gilt folgende Ausnahme: Findet an der Messlokation der Use-Case „[Geräteübernahme](/prozessdoku/202610/MSB--MSBA/WiM-Teil1-geraeteuebernahme)“ (WiM Teil 1) statt, ist neben dem vorgenannten MSB (im Use-Case „[Geräteübernahme](/prozessdoku/202610/MSB--MSBA/WiM-Teil1-geraeteuebernahme)“ als MSBA bezeichnet) auch der MSBN berechtigt für diese Messlokation das SD „[Stammdatenänderung vom MSB (verantwortlich) ausgehend](/prozessdoku/202610/NB/GPKE-Teil4-stammdatenaenderung-vom-msb-verantwortlich-ausgehend)“ als verantwortlicher MSB anzuwenden. Demensprechend können die Berechtigten wiederum eine Bestellung zur Stammdatenänderung an den MSBN senden.

</li>

<li data-blatt="anlass">

### Anlass

- Dem Berechtigten liegt für ein Stammdatum ein neuer Wert vor.
- Der Berechtigte geht von einem Datenschiefstand zwischen den Berechtigten und dem Verantwortlichen aus.

</li>

<li data-blatt="erste-nachricht">

### Erste Nachricht

Der Beteiligte dieser Seite sendet selbst: „Bestellung einer Änderung von Stammdaten vom NB an LF“ an **LF** (Schritt 1).

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

- [Sicht LF](/prozessdoku/202610/LF/GPKE-Teil4-bestellung-zur-stammdatenaenderung-an-lf-verantwortlich) — LF
- [Sicht MSB](/prozessdoku/202610/MSB/GPKE-Teil4-bestellung-zur-stammdatenaenderung-an-lf-verantwortlich) — MSB
- [Sicht ÜNB](/prozessdoku/202610/UENB/GPKE-Teil4-bestellung-zur-stammdatenaenderung-an-lf-verantwortlich) — ÜNB · Marktrolle UENB

<Hinweisbereich>

*Die Schritte sind die **möglichen** Nachrichten dieses Prozesses, keine Abfolge — die Quelle führt weder Bedingungen noch Alternativen. Das Kästchen am Schritt nennt links die eigene Sicht: **←** empfängt sie, **→** sendet sie. Zugeklappte Schritte laufen zwischen anderen Marktpartnern.*

Zu den Prüfidentifikatoren dieser Schritte liegt kein Testfall im Testbestand; der Knopf »Ausprobieren« der schreibenden Schnittstelle bietet deshalb keinen Rumpf an.

Betrifft: [2](#schritt-2)

</Hinweisbereich>
