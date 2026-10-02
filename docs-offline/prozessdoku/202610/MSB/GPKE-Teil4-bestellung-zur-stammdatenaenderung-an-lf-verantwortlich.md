# Bestellung zur Stammdatenänderung an LF (verantwortlich) — Sicht MSB

<Kopf rolle="MSB" beteiligter="MSB" festlegung="GPKE" dokument="GPKE Teil 4" kapitel="1.5.3" sparte="Strom" schritte={6} suchtitel="Bestellung zur Stammdatenänderung an LF (verantwortlich) — Sicht MSB · GPKE Teil 4 · Formatversion 202610" abschnitte={[{"id": "abschnitt-ablauf", "label": "Prozessablauf"}, {"id": "abschnitt-schritte", "label": "Prozessschritte"}, {"id": "abschnitt-informationen", "label": "Prozess-Informationen"}, {"id": "abschnitt-sichten", "label": "Andere Sichten des Prozesses"}]} />

<Kurzfassung>

Der Prozess beschreibt die Anfrage/ Bestellung von Werten von Stammdaten durch einen Berechtigten beim Verantwortlichen der Stammdaten. Der Verantwortiche prüft die Bestellung und teilt dem Berechtigten den Bearbeitungsstand mit.

</Kurzfassung>

<a id="abschnitt-ablauf"></a>

## Prozessablauf aus Sicht des MSB

<Systembild svg={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1004 690\" width=\"1004\" height=\"690\" role=\"img\" aria-labelledby=\"sb-title\" class=\"maco-systembild\">\n<title id=\"sb-title\">Systembild: Bestellung zur Stammdatenänderung an LF (verantwortlich) aus Sicht MSB</title>\n<defs><marker id=\"sb-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect class=\"sb-lane-kopf\" x=\"16\" y=\"12\" width=\"232\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend-System des Kunden</text>\n<rect class=\"sb-lane-kopf\" x=\"398\" y=\"12\" width=\"264\" height=\"46\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · MSB</text>\n<rect class=\"sb-lane-kopf\" x=\"812\" y=\"12\" width=\"176\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"900\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Marktpartner</text>\n<line x1=\"323\" y1=\"58\" x2=\"323\" y2=\"678\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"737\" y1=\"58\" x2=\"737\" y2=\"678\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect class=\"sb-kasten sb-folge_ausloeser\" x=\"432\" y=\"80\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Ausgelöst durch Eingang:</text>\n<text x=\"530\" y=\"115\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">55110</text>\n<rect class=\"sb-kasten sb-lesen_verarbeitung\" x=\"432\" y=\"154\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"174\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Daten für die Verarbeitung</text>\n<text x=\"530\" y=\"189\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">laden</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"128\" x2=\"530\" y2=\"154\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-lesen_verarbeitung\" x=\"34\" y=\"162\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"182\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Marktlokation lesen</text>\n<line x1=\"432\" y1=\"178\" x2=\"230\" y2=\"178\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"170\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"228\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"248\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">3. Bestellung einer Änderung</text>\n<text x=\"530\" y=\"263\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">von Stammdaten vom MSB</text>\n<text x=\"530\" y=\"278\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">an LF</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"202\" x2=\"530\" y2=\"228\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"241\" r=\"5\"/><line x1=\"900\" y1=\"246\" x2=\"900\" y2=\"258\"/><line x1=\"893\" y1=\"250\" x2=\"907\" y2=\"250\"/><line x1=\"900\" y1=\"258\" x2=\"894\" y2=\"268\"/><line x1=\"900\" y1=\"258\" x2=\"906\" y2=\"268\"/></g>\n<text x=\"900\" y=\"290\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">LF</text>\n<line x1=\"628\" y1=\"259\" x2=\"878\" y2=\"259\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"251\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"275\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">55136</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"317\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"337\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"291\" x2=\"530\" y2=\"317\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"317\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"337\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"333\" x2=\"230\" y2=\"333\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"325\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"381\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"401\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">4. Bearbeitungsstand zur</text>\n<text x=\"530\" y=\"416\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Bestellung</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"350\" x2=\"530\" y2=\"381\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"387\" r=\"5\"/><line x1=\"900\" y1=\"392\" x2=\"900\" y2=\"404\"/><line x1=\"893\" y1=\"396\" x2=\"907\" y2=\"396\"/><line x1=\"900\" y1=\"404\" x2=\"894\" y2=\"414\"/><line x1=\"900\" y1=\"404\" x2=\"906\" y2=\"414\"/></g>\n<text x=\"900\" y=\"436\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">LF</text>\n<line x1=\"878\" y1=\"405\" x2=\"628\" y2=\"405\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"397\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"421\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">21047</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"464\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"484\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z33</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"429\" x2=\"530\" y2=\"464\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"528\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"548\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"497\" x2=\"530\" y2=\"528\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben sb-abgeleitet\" x=\"34\" y=\"528\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"548\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"544\" x2=\"230\" y2=\"544\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"536\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-lesen_verarbeitung\" x=\"432\" y=\"592\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"612\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Daten für die Verarbeitung</text>\n<text x=\"530\" y=\"627\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">laden</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"561\" x2=\"530\" y2=\"592\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-lesen_verarbeitung\" x=\"34\" y=\"592\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"612\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">LESEN_STATUSMITTEILUNG_</text>\n<text x=\"132\" y=\"627\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">BASIS</text>\n<line x1=\"432\" y1=\"616\" x2=\"230\" y2=\"616\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"608\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n</svg>"} gesamt={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1218 610\" width=\"1218\" height=\"610\" role=\"img\" aria-labelledby=\"sd-title\" class=\"maco-sequence\">\n<title id=\"sd-title\">Sequenzdiagramm: Bestellung zur Stammdatenänderung an LF (verantwortlich) aus Sicht MSB</title>\n<defs><marker id=\"sd-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect x=\"16\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"121\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend (Kunde)</text>\n<line x1=\"121\" y1=\"64\" x2=\"121\" y2=\"598\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"260\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"365\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · MSB</text>\n<line x1=\"365\" y1=\"64\" x2=\"365\" y2=\"598\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"504\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"609\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"609\" y1=\"64\" x2=\"609\" y2=\"598\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"748\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"853\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">LF</text>\n<line x1=\"853\" y1=\"64\" x2=\"853\" y2=\"598\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"992\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"1097\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">ÜNB</text>\n<line x1=\"1097\" y1=\"64\" x2=\"1097\" y2=\"598\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"609\" y1=\"90\" x2=\"853\" y2=\"90\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"731\" y=\"81\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">1. Bestellung einer Änderung von Stammdaten vom…</text>\n<text x=\"731\" y=\"105\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55137, 55232</text>\n<line x1=\"853\" y1=\"152\" x2=\"609\" y2=\"152\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"731\" y=\"143\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">2. Bearbeitungsstand zur Bestellung</text>\n<text x=\"731\" y=\"167\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 21047 · E_0588</text>\n<text x=\"731\" y=\"180\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0588 — Bestellung zur Stammdatenänderung prüfen</text>\n<line x1=\"365\" y1=\"214\" x2=\"853\" y2=\"214\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"609\" y=\"205\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">3. Bestellung einer Änderung von Stammdaten vom…</text>\n<text x=\"609\" y=\"229\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55136</text>\n<line x1=\"365\" y1=\"276\" x2=\"121\" y2=\"276\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"267\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"291\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"853\" y1=\"338\" x2=\"365\" y2=\"338\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"609\" y=\"329\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">4. Bearbeitungsstand zur Bestellung</text>\n<text x=\"609\" y=\"353\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 21047 · E_0589</text>\n<text x=\"609\" y=\"366\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0589 — Bestellung zur Stammdatenänderung prüfen</text>\n<line x1=\"365\" y1=\"400\" x2=\"121\" y2=\"400\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"391\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"415\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"1097\" y1=\"462\" x2=\"853\" y2=\"462\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"975\" y=\"453\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">5. Bestellung einer Änderung von Stammdaten vom…</text>\n<line x1=\"853\" y1=\"524\" x2=\"1097\" y2=\"524\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"975\" y=\"515\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">6. Bearbeitungsstand zur Bestellung</text>\n</svg>"} titel="MSB" />

<a id="abschnitt-schritte"></a>

## Prozessschritte

<Schritt nr="1" anker="schritt-1" richtung="fremd" kopf={{"links": {"label": "NB", "eigen": false}, "rechts": {"label": "LF"}}}>

### Bestellung einer Änderung von Stammdaten vom NB an LF

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55137](/schnittstellen/202610/pruefi/UTILMD/PI_55137) — Rückmeldung/Anfrage Daten der MaLo · AS4
- [55232](/schnittstellen/202610/pruefi/UTILMD/PI_55232) — Rückmeldung/Anfrage Blindabr.-Daten der NeLo · AS4

</div>

</Schritt>

<Schritt nr="2" anker="schritt-2" richtung="fremd" kopf={{"links": {"label": "LF", "eigen": false}, "rechts": {"label": "NB"}}}>

### Bearbeitungsstand zur Bestellung

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [21047](/schnittstellen/202610/pruefi/IFTSTA/PI_21047) — Bearbeitungsstandsmeldung · AS4

</div>

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `21047` → [E_0588](/referenz/202610/ebd/E_0588) · LF · Bestellung zur Stammdatenänderung prüfen (Basiert auf EBD: E_0573_Bestellung zur Stammdatenänderung prüfen)

</div>

</Schritt>

<Schritt nr="3" anker="schritt-3" richtung="ausgehend" kopf={{"links": {"label": "MSB", "eigen": true}, "rechts": {"label": "LF"}}}>

### Bestellung einer Änderung von Stammdaten vom MSB an LF

<Schrittskizze sicht={{"label": "MSB"}} zeilen={[{"art": "folge_ausloeser", "werte": ["55110"]}, {"art": "lesen_verarbeitung", "schnittstellen": [{"label": "Marktlokation lesen"}]}, {"art": "senden", "label": "LF", "weg": "AS4", "nachrichten": [{"nr": "55136", "titel": "Rückmeldung/Anfrage Daten der MaLo"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55136](/schnittstellen/202610/pruefi/UTILMD/PI_55136) — Rückmeldung/Anfrage Daten der MaLo · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="folge_ausloeser">

**Ausgelöst durch Eingang**
- [55110](/schnittstellen/202610/pruefi/UTILMD/PI_55110)

Die MACO APP sendet diese Nachricht selbst, als Folgeprozess nach diesem Eingang.

</li>

<li data-teil="lesen" data-stufe="verarbeitung">

**Daten für die Verarbeitung laden**
- [Marktlokation lesen](/api/202610/backend-lesen/getmarketlocationbasic#marktlokation-lesen) `GET /getMarketLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getMarketLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": false, "defaultValue": "MALO", "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": false, "defaultValue": "2024-06-28T12:18:00Z", "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_MARKTLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

</li>

<li data-teil="nachricht">

Nachricht an **LF** · AS4

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202610/backend-schreiben-msb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"ENERGIELIEFERVERTRAG\": [\n      {\n        \"boTyp\": \"VERTRAG\",\n        \"datenqualitaet\": \"IM_SYSTEM_VORHANDENE_DATEN\",\n        \"gueltigkeitszeitraum\": {\n          \"enddatum\": \"2026-07-23T22:00:00Z\",\n          \"startdatum\": \"2026-06-23T22:00:00Z\",\n          \"zeitraumId\": 1\n        },\n        \"korrespondenzpartner\": {\n          \"ansprechpartner\": {\n            \"boTyp\": \"ANSPRECHPARTNER\",\n            \"eMailAdresse\": \"max@mustermann.de\",\n            \"versionStruktur\": \"1\"\n          },\n          \"boTyp\": \"GESCHAEFTSPARTNER\",\n          \"gewerbekennzeichnung\": false,\n          \"name1\": \"Fank Müller\",\n          \"partneradresse\": {\n            \"hausnummer\": \"25\",\n            \"landescode\": \"DE\",\n            \"ort\": \"Musterstadt\",\n            \"ortsteil\": \"Musterortsteil\",\n            \"postleitzahl\": \"55555\",\n            \"strasse\": \"Wohnstrasse\"\n          },\n          \"versionStruktur\": \"1\"\n        },\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\",\n        \"vertragsart\": \"ENERGIELIEFERVERTRAG\",\n        \"vertragspartner2\": [\n          {\n            \"boTyp\": \"GESCHAEFTSPARTNER\",\n            \"geschaeftspartnerrolle\": [\n              \"KUNDE\"\n            ],\n            \"gewerbekennzeichnung\": true,\n            \"name1\": \"Firma AG\",\n            \"name2\": \"Musterfirma\",\n            \"versionStruktur\": \"1\"\n          }\n        ]\n      },\n      {\n        \"boTyp\": \"VERTRAG\",\n        \"datenqualitaet\": \"IM_SYSTEM_VORHANDENE_DATEN\",\n        \"gueltigkeitszeitraum\": {\n          \"startdatum\": \"2026-07-23T22:00:00Z\",\n          \"zeitraumId\": 2\n        },\n        \"korrespondenzpartner\": {\n          \"ansprechpartner\": {\n            \"boTyp\": \"ANSPRECHPARTNER\",\n            \"eMailAdresse\": \"max@mustermann.de\",\n            \"versionStruktur\": \"1\"\n          },\n          \"boTyp\": \"GESCHAEFTSPARTNER\",\n          \"gewerbekennzeichnung\": false,\n          \"name1\": \"Fank Müller\",\n          \"partneradresse\": {\n            \"hausnummer\": \"25\",\n            \"landescode\": \"DE\",\n            \"ort\": \"Musterstadt\",\n            \"ortsteil\": \"Musterortsteil\",\n            \"postleitzahl\": \"55555\",\n            \"strasse\": \"Wohnstrasse\"\n          },\n          \"versionStruktur\": \"1\"\n        },\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\",\n        \"vertragsart\": \"ENERGIELIEFERVERTRAG\",\n        \"vertragspartner2\": [\n          {\n            \"boTyp\": \"GESCHAEFTSPARTNER\",\n            \"geschaeftspartnerrolle\": [\n              \"KUNDE\"\n            ],\n            \"gewerbekennzeichnung\": true,\n            \"name1\": \"Firma AG\",\n            \"name2\": \"Musterfirma\",\n            \"versionStruktur\": \"1\"\n          }\n        ]\n      }\n    ],\n    \"MARKTLOKATION\": [\n      {\n        \"boTyp\": \"MARKTLOKATION\",\n        \"marktlokationsId\": \"20072281644\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"VERWENDUNGSZEITRAUM\": [\n      {\n        \"boTyp\": \"VERWENDUNGSZEITRAUM\",\n        \"datenqualitaet\": \"ERWARTETE_DATEN\",\n        \"versionStruktur\": \"1\",\n        \"verwendungAb\": \"2026-06-23T22:00:00Z\",\n        \"verwendungBis\": \"2026-07-23T22:00:00Z\",\n        \"zeitraumId\": 1\n      },\n      {\n        \"boTyp\": \"VERWENDUNGSZEITRAUM\",\n        \"datenqualitaet\": \"ERWARTETE_DATEN\",\n        \"versionStruktur\": \"1\",\n        \"verwendungAb\": \"2026-07-23T22:00:00Z\",\n        \"zeitraumId\": 2\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9904990000008\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"anfragereferenznummer\": \"ANFRAGE1234\",\n    \"antwortStatusZeitraum\": [\n      {\n        \"code\": \"A02\",\n        \"liste\": \"E_0578\",\n        \"zeitraumId\": 1\n      },\n      {\n        \"code\": \"A02\",\n        \"liste\": \"E_0578\",\n        \"zeitraumId\": 2\n      }\n    ],\n    \"datenaustauschreferenz\": \"DAEPJOOFDZHKCW\",\n    \"dokumentennummer\": \"DA912411051009499903323000007124387\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9903729000007\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"E03\",\n    \"nachrichtendatum\": \"2026-10-02T11:00:00Z\",\n    \"nachrichtenreferenznummer\": \"DAQXHBCTNCYPVJ\",\n    \"pruefidentifikator\": \"55136\",\n    \"sparte\": \"STROM\",\n    \"transaktionsgrund\": \"ZX6\",\n    \"vorgangsnummer\": \"24062416225400000000000102159662011\"\n  },\n  \"zusatzdaten\": {}\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend fort, nachdem die Nachricht erstellt ist.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="4" anker="schritt-4" richtung="eingehend" kopf={{"links": {"label": "MSB", "eigen": true}, "rechts": {"label": "LF"}}}>

### Bearbeitungsstand zur Bestellung

<Schrittskizze sicht={{"label": "MSB"}} zeilen={[{"art": "empfangen", "label": "LF", "weg": "AS4", "nachrichten": [{"nr": "21047", "titel": "Bearbeitungsstandsmeldung"}]}, {"art": "aperak", "werte": ["Z33"]}, {"art": "fortschreiben"}, {"art": "lesen_verarbeitung", "schnittstellen": [{"label": "LESEN_STATUSMITTEILUNG_BASIS"}]}]} />

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
- `21047` → [E_0589](/referenz/202610/ebd/E_0589) · LF · Bestellung zur Stammdatenänderung prüfen (Basiert auf EBD: E_0573_Bestellung zur Stammdatenänderung prüfen)

</div>

</li>

<li data-teil="aperak">

**Aperak-Prüfungen**
- `21047` → `Z33`

</li>

<li data-teil="schnittstelle" data-art="fortschreiben" data-abgeleitet="ja">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202610/backend-schreiben-msb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend mit den Daten der eingegangenen Nachricht fort.

</li>

<li data-teil="lesen" data-stufe="verarbeitung">

**Daten für die Verarbeitung laden**
- `LESEN_STATUSMITTEILUNG_BASIS`

</li>

</ol>
</Stepper>

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
| [E_0589](/referenz/202610/ebd/E_0589) | Bestellung zur Stammdatenänderung prüfen (Basiert auf EBD: E_0573_Bestellung zur Stammdatenänderung prüfen) |
| [E_0588](/referenz/202610/ebd/E_0588) | Bestellung zur Stammdatenänderung prüfen (Basiert auf EBD: E_0573_Bestellung zur Stammdatenänderung prüfen) |

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

- Im Fall des SD „[Bestellung zur Stammdatenänderung an MSB (verantwortlich)](/prozessdoku/202610/MSB/GPKE-Teil4-bestellung-zur-stammdatenaenderung-an-msb-verantwortlich)“ gilt: Der verantwortliche MSB einer Messlokation ist immer der MSB, der zum Zeitpunkt, zu dem die Änderung des Werts des Stammdatums erfolgt, der Messlokation zugeordnet ist. Dabei gilt folgende Ausnahme: Findet an der Messlokation der Use-Case „[Geräteübernahme](/prozessdoku/202610/MSB--MSBA/WiM-Teil1-geraeteuebernahme)“ (WiM Teil 1) statt, ist neben dem vorgenannten MSB (im Use-Case „[Geräteübernahme](/prozessdoku/202610/MSB--MSBA/WiM-Teil1-geraeteuebernahme)“ als MSBA bezeichnet) auch der MSBN berechtigt für diese Messlokation das SD „[Stammdatenänderung vom MSB (verantwortlich) ausgehend](/prozessdoku/202610/MSB/GPKE-Teil4-stammdatenaenderung-vom-msb-verantwortlich-ausgehend)“ als verantwortlicher MSB anzuwenden. Demensprechend können die Berechtigten wiederum eine Bestellung zur Stammdatenänderung an den MSBN senden.

</li>

<li data-blatt="anlass">

### Anlass

- Dem Berechtigten liegt für ein Stammdatum ein neuer Wert vor.
- Der Berechtigte geht von einem Datenschiefstand zwischen den Berechtigten und dem Verantwortlichen aus.

</li>

<li data-blatt="erste-nachricht">

### Erste Nachricht

Der Beteiligte dieser Seite sendet selbst: „Bestellung einer Änderung von Stammdaten vom MSB an LF“ an **LF** (Schritt 3).

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
- [Sicht NB](/prozessdoku/202610/NB/GPKE-Teil4-bestellung-zur-stammdatenaenderung-an-lf-verantwortlich) — NB
- [Sicht ÜNB](/prozessdoku/202610/UENB/GPKE-Teil4-bestellung-zur-stammdatenaenderung-an-lf-verantwortlich) — ÜNB · Marktrolle UENB

<Hinweisbereich>

*Die Schritte sind die **möglichen** Nachrichten dieses Prozesses, keine Abfolge — die Quelle führt weder Bedingungen noch Alternativen. Das Kästchen am Schritt nennt links die eigene Sicht: **←** empfängt sie, **→** sendet sie. Zugeklappte Schritte laufen zwischen anderen Marktpartnern.*

Diese Lesezugriffe sind im API-Katalog dieser Formatversion nicht geführt; am Schritt steht deshalb nur ihr Kommando, ohne Adresse und ohne Knopf.

Betrifft: [4](#schritt-4)

Die Konnektortabelle führt für diese Schritte keinen Schreibaufruf. Abgeleitet aus dem Prozessverlauf: Die eigene Rolle war an diesem Prozess schon beteiligt, der Vorgang besteht also.

Betrifft: [4](#schritt-4)

Zu den Prüfidentifikatoren dieser Schritte liegt kein Testfall im Testbestand; der Knopf »Ausprobieren« der schreibenden Schnittstelle bietet deshalb keinen Rumpf an.

Betrifft: [4](#schritt-4)

</Hinweisbereich>
