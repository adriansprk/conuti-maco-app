# Angebot zur Rechnungsabwicklung des Messstellenbetriebes über den LF durch den MSB — Sicht LF

<Kopf rolle="LF" beteiligter="LF" festlegung="WiM" dokument="WiM Strom Teil 1" kapitel="3.6.3.4.2" sparte="Strom" schritte={2} suchtitel="Angebot zur Rechnungsabwicklung des Messstellenbetriebes über den LF durch den MSB — Sicht LF · WiM Strom Teil 1 · Formatversion 202604" abschnitte={[{"id": "abschnitt-ablauf", "label": "Prozessablauf"}, {"id": "abschnitt-schritte", "label": "Prozessschritte"}, {"id": "abschnitt-informationen", "label": "Prozess-Informationen"}, {"id": "abschnitt-sichten", "label": "Andere Sichten des Prozesses"}]} />

<Kurzfassung>

Der MSB der Marktlokation hat die Möglichkeit,
- nach erfolgtem Gerätewechsel, in dessen Rahmen ein iMS oder mME in die Messlokation/en einer Marktlokation eingebaut wurde, oder
- nachdem ein neuer LF der Marklokation zugeordnet ist, für dessen Messlokation/en der MSB den Messstellenbetrieb mittels iMS oder mME durchführt, oder
- wenn sich die Anzahl der Leistungen bzw. die Verbrauchsgruppe der POG für den Messstellenbetrieb, der mit iMS oder mME ausgestattet ist, ändert oder
- als gMSB im Fall, dass er den bisherigen wMSB weiterverpflichtet hat (Hinweis: der wMSB rechnet direkt mit dem gMSB ab) dem LF ein Angebot über die Abwicklung der Abrechnung über den LF vorzulegen. Macht der MSB der Marktlokation von dieser Möglichkeit Gebrauch, hat der LF das Angebot innerhalb von 8 WT entweder anzunehmen oder abzulehnen.

</Kurzfassung>

<a id="abschnitt-ablauf"></a>

## Prozessablauf aus Sicht des LF

<Systembild svg={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1004 838\" width=\"1004\" height=\"838\" role=\"img\" aria-labelledby=\"sb-title\" class=\"maco-systembild\">\n<title id=\"sb-title\">Systembild: Angebot zur Rechnungsabwicklung des Messstellenbetriebes über den LF durch den MSB aus Sicht LF</title>\n<defs><marker id=\"sb-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect class=\"sb-lane-kopf\" x=\"16\" y=\"12\" width=\"232\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend-System des Kunden</text>\n<rect class=\"sb-lane-kopf\" x=\"398\" y=\"12\" width=\"264\" height=\"46\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · LF</text>\n<rect class=\"sb-lane-kopf\" x=\"812\" y=\"12\" width=\"176\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"900\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Marktpartner</text>\n<line x1=\"323\" y1=\"58\" x2=\"323\" y2=\"826\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"737\" y1=\"58\" x2=\"737\" y2=\"826\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"80\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">1. Angebot zur</text>\n<text x=\"530\" y=\"115\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Rechnungs-abwicklung des</text>\n<text x=\"530\" y=\"130\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Messstellenbetriebes ü…</text>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"93\" r=\"5\"/><line x1=\"900\" y1=\"98\" x2=\"900\" y2=\"110\"/><line x1=\"893\" y1=\"102\" x2=\"907\" y2=\"102\"/><line x1=\"900\" y1=\"110\" x2=\"894\" y2=\"120\"/><line x1=\"900\" y1=\"110\" x2=\"906\" y2=\"120\"/></g>\n<text x=\"900\" y=\"142\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">MSB (entspricht MSB a…</text>\n<line x1=\"878\" y1=\"111\" x2=\"628\" y2=\"111\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"103\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"127\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">15002</text>\n<rect class=\"sb-kasten sb-aperak_lesen\" x=\"432\" y=\"169\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"189\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Daten für die</text>\n<text x=\"530\" y=\"204\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Eingangsprüfung laden</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"143\" x2=\"530\" y2=\"169\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-aperak_lesen\" x=\"34\" y=\"177\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"197\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Marktlokation lesen</text>\n<line x1=\"432\" y1=\"193\" x2=\"230\" y2=\"193\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"185\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"243\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"263\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z10</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"217\" x2=\"530\" y2=\"243\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-schreiben\" x=\"432\" y=\"307\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"327\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"276\" x2=\"530\" y2=\"307\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-schreiben\" x=\"34\" y=\"307\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"327\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten erstellen</text>\n<line x1=\"432\" y1=\"323\" x2=\"230\" y2=\"323\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"315\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-lesen\" x=\"432\" y=\"371\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"391\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Daten für die Prüfung laden</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"340\" x2=\"530\" y2=\"371\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-lesen\" x=\"34\" y=\"363\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"383\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">3 Lese-Schnittstellen</text>\n<text x=\"132\" y=\"398\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">aufgerufen</text>\n<line x1=\"432\" y1=\"387\" x2=\"230\" y2=\"387\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"379\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<text x=\"331\" y=\"403\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">je einzeln am Schritt</text>\n<rect class=\"sb-kasten sb-ebd\" x=\"432\" y=\"445\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"465\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">EBD prüfen: E_0205</text>\n<text x=\"530\" y=\"480\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label-2, #424245)\">Angebot prüfen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"404\" x2=\"530\" y2=\"445\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-folgeprozess\" x=\"432\" y=\"519\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"539\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Folgeprozess auslösen:</text>\n<text x=\"530\" y=\"554\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">17005, 21032</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"493\" x2=\"530\" y2=\"519\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-folge_ausloeser\" x=\"432\" y=\"593\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"613\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Ausgelöst durch Eingang:</text>\n<text x=\"530\" y=\"628\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">15002</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"567\" x2=\"530\" y2=\"593\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"667\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"687\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">2. Antwort auf das Angebot</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"641\" x2=\"530\" y2=\"667\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"665\" r=\"5\"/><line x1=\"900\" y1=\"670\" x2=\"900\" y2=\"682\"/><line x1=\"893\" y1=\"674\" x2=\"907\" y2=\"674\"/><line x1=\"900\" y1=\"682\" x2=\"894\" y2=\"692\"/><line x1=\"900\" y1=\"682\" x2=\"906\" y2=\"692\"/></g>\n<text x=\"900\" y=\"714\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">MSB (entspricht MSB a…</text>\n<line x1=\"628\" y1=\"683\" x2=\"878\" y2=\"683\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"675\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"699\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">17005, 21032</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"750\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"770\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"700\" x2=\"530\" y2=\"750\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"750\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"770\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"766\" x2=\"230\" y2=\"766\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"758\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n</svg>"} gesamt={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 730 362\" width=\"730\" height=\"362\" role=\"img\" aria-labelledby=\"sd-title\" class=\"maco-sequence\">\n<title id=\"sd-title\">Sequenzdiagramm: Angebot zur Rechnungsabwicklung des Messstellenbetriebes über den LF durch den MSB aus Sicht LF</title>\n<defs><marker id=\"sd-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect x=\"16\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"121\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend (Kunde)</text>\n<line x1=\"121\" y1=\"64\" x2=\"121\" y2=\"350\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"260\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"365\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · LF</text>\n<line x1=\"365\" y1=\"64\" x2=\"365\" y2=\"350\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"504\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"609\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">MSB (entspricht MSB am Ob…</text>\n<line x1=\"609\" y1=\"64\" x2=\"609\" y2=\"350\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"609\" y1=\"90\" x2=\"365\" y2=\"90\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"81\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">1. Angebot zur Rechnungs-abwicklung des Messstel…</text>\n<text x=\"487\" y=\"105\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 15002</text>\n<line x1=\"365\" y1=\"152\" x2=\"121\" y2=\"152\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"143\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<text x=\"243\" y=\"167\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten erstellen</text>\n<line x1=\"365\" y1=\"214\" x2=\"609\" y2=\"214\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"205\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">2. Antwort auf das Angebot</text>\n<text x=\"487\" y=\"229\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 17005, 21032 · E_0205</text>\n<text x=\"487\" y=\"242\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0205 — Angebot prüfen</text>\n<line x1=\"365\" y1=\"276\" x2=\"121\" y2=\"276\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"267\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"291\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n</svg>"} titel="LF" />

<a id="abschnitt-schritte"></a>

## Prozessschritte

<Schritt nr="1" anker="schritt-1" richtung="eingehend" kopf={{"links": {"label": "LF", "eigen": true}, "rechts": {"label": "MSB (entspricht MSB am Objekt Marktlokation)"}}}>

### Angebot zur Rechnungs-abwicklung des Messstellenbetriebes über den LF

<Schrittskizze sicht={{"label": "LF"}} zeilen={[{"art": "empfangen", "label": "MSB (entspricht MSB am Objekt Marktlokation)", "weg": "AS4", "nachrichten": [{"nr": "15002", "titel": "Angebot Abrechnung Messstellenbetrieb MSB"}]}, {"art": "lesen_aperak", "schnittstellen": [{"label": "Marktlokation lesen"}]}, {"art": "aperak", "werte": ["Z10"]}, {"art": "erstellen"}, {"art": "lesen_ebd", "schnittstellen": [{"label": "Energieliefervertrag lesen"}, {"label": "Messstellenbetriebsvertrag lesen"}, {"label": "Preisblatt lesen"}]}, {"art": "ebd", "baeume": [{"code": "E_0205", "titel": "Angebot prüfen"}]}, {"art": "folgeprozess", "werte": ["17005", "21032"]}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [15002](/schnittstellen/202604/pruefi/QUOTES/PI_15002) — Angebot Abrechnung Messstellenbetrieb MSB · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **MSB (entspricht MSB am Objekt Marktlokation)** · AS4

</li>

<li data-teil="lesen" data-stufe="aperak">

**Daten für die Eingangsprüfung laden**
- [Marktlokation lesen](/api/202604/backend-lesen/getmarketlocationbasic#marktlokation-lesen) `GET /getMarketLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getMarketLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": false, "defaultValue": "MALO", "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": false, "defaultValue": "2024-06-28T12:18:00Z", "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_MARKTLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

</li>

<li data-teil="aperak">

**Aperak-Prüfungen**
- `15002` → `Z10` — Aperak Prüfung: Ist Lokation bekannt ?

</li>

<li data-teil="schnittstelle" data-art="schreiben">

**Schreibende Schnittstelle**
- Vorgang angelegt — [Prozessdaten erstellen](/api/202604/backend-schreiben-lf/createprocessdata#prozessdaten-erstellen) `POST /createProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/createProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": false, "defaultValue": "ERSTELLEN_PROZESSDATEN", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Legt im Backend einen neuen Vorgang mit den Daten der eingegangenen Nachricht an.

</li>

<li data-teil="lesen" data-stufe="ebd">

**Daten für die Prüfung laden**
- [Energieliefervertrag lesen](/api/202604/backend-lesen/getenergysupplycontractbasic#energieliefervertrag-lesen) `GET /getEnergySupplyContractBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getEnergySupplyContractBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_ENERGIELIEFERVERTRAG_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Messstellenbetriebsvertrag lesen](/api/202604/backend-lesen/getmeasuringpointoperationcontractbasic#messstellenbetriebsvertrag-lesen) `GET /getMeasuringPointOperationContractBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getMeasuringPointOperationContractBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_MESSSTELLENBETRIEBSVERTRAG_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Preisblatt lesen](/api/202604/backend-lesen/getpricesheetbasic#preisblatt-lesen) `GET /getPriceSheetBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getPriceSheetBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": false, "defaultValue": "74018657187", "type": "string"}, {"name": "parameter2", "isRequired": false, "defaultValue": "MALO", "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": false, "defaultValue": "2024-06-28T12:18:00Z", "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_PREISBLATT_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

</li>

<li data-teil="baum">

**Entscheidungsbaum**
- `15002` → [E_0205](/referenz/202604/ebd/E_0205) — Angebot prüfen

</li>

<li data-teil="folgeprozess">

**Folgeprozess auslösen**
- [17005](/schnittstellen/202604/pruefi/ORDERS/PI_17005) — Bestellung Rechnungsabwicklung MSB über LF
- [21032](/schnittstellen/202604/pruefi/IFTSTA/PI_21032) — Antwort auf das Angebot

Nach der Verarbeitung startet die MACO APP den Folgeprozess selbst; welcher davon läuft, hängt vom Ergebnis der Verarbeitung ab.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="2" anker="schritt-2" richtung="ausgehend" kopf={{"links": {"label": "LF", "eigen": true}, "rechts": {"label": "MSB (entspricht MSB am Objekt Marktlokation)"}}}>

### Antwort auf das Angebot

<Schrittskizze sicht={{"label": "LF"}} zeilen={[{"art": "folge_ausloeser", "werte": ["15002"]}, {"art": "senden", "label": "MSB (entspricht MSB am Objekt Marktlokation)", "weg": "AS4", "nachrichten": [{"nr": "17005", "titel": "Bestellung Rechnungsabwicklung MSB über LF"}, {"nr": "21032", "titel": "Antwort auf das Angebot"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [17005](/schnittstellen/202604/pruefi/ORDERS/PI_17005) — Bestellung Rechnungsabwicklung MSB über LF · AS4
- [21032](/schnittstellen/202604/pruefi/IFTSTA/PI_21032) — Antwort auf das Angebot · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="folge_ausloeser">

**Ausgelöst durch Eingang**
- [15002](/schnittstellen/202604/pruefi/QUOTES/PI_15002) — Angebot Abrechnung Messstellenbetrieb MSB

Die MACO APP sendet diese Nachricht selbst, als Folgeprozess nach diesem Eingang.

</li>

<li data-teil="nachricht">

Nachricht an **MSB (entspricht MSB am Objekt Marktlokation)** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `21032` → [E_0205](/referenz/202604/ebd/E_0205) · LF · Angebot prüfen

</div>

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202604/backend-schreiben-lf/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": false, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"ANFRAGE\": [\n      {\n        \"abonnement\": \"START_ABO\",\n        \"anfragekategorie\": \"ABRECHNUNG_MESSSTELLENBETRIEB_MSB_AN_LF\",\n        \"boTyp\": \"ANFRAGE\",\n        \"lokationsId\": \"52345678901\",\n        \"lokationsTyp\": \"MALO\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"AUFTRAG\": [\n      {\n        \"ausfuehrungsdatum\": \"2025-10-15T22:00:00Z\",\n        \"boTyp\": \"AUFTRAG\",\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9903692000001\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"angebotsnummer\": \"UNHM2LD5555\",\n    \"datenaustauschreferenz\": \"M27ZKAJL\",\n    \"dokumentennummer\": \"BGMM32GNEP9\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9904733000009\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"nachrichtendatum\": \"2025-10-05T09:45:00Z\",\n    \"nachrichtenreferenznummer\": \"UNHM2LDYGU8\",\n    \"pruefidentifikator\": \"17005\",\n    \"sparte\": \"STROM\"\n  },\n  \"zusatzdaten\": {}\n}"} examples={[{"mediaType": "application/json", "examples": [{"name": "17005", "summary": "17005 — Bestellung Rechnungsabwicklung MSB über LF", "value": {"stammdaten": {"ANFRAGE": [{"boTyp": "ANFRAGE", "versionStruktur": "1", "lokationsId": "52345678901", "lokationsTyp": "MALO", "anfragekategorie": "ABRECHNUNG_MESSSTELLENBETRIEB_MSB_AN_LF", "abonnement": "START_ABO"}], "AUFTRAG": [{"boTyp": "AUFTRAG", "versionStruktur": "1", "ausfuehrungsdatum": "2025-10-15T22:00:00Z"}]}, "transaktionsdaten": {"datenaustauschreferenz": "M27ZKAJL", "sparte": "STROM", "pruefidentifikator": "17005", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9903692000001", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9904733000009", "rollencodetyp": "BDEW"}, "dokumentennummer": "BGMM32GNEP9", "nachrichtendatum": "2025-10-05T09:45:00Z", "nachrichtenreferenznummer": "UNHM2LDYGU8", "angebotsnummer": "UNHM2LD5555"}, "zusatzdaten": {}}}, {"name": "21032", "summary": "21032 — Antwort auf das Angebot", "value": {"stammdaten": {"MARKTLOKATION": [{"boTyp": "MARKTLOKATION", "versionStruktur": "1", "marktlokationsId": "44152365487", "sparte": "STROM"}], "STATUSMITTEILUNG": [{"boTyp": "STATUSMITTEILUNG", "versionStruktur": "1", "statusObjekt": "ANGEBOTANFRAGE", "auftragsstatus": "ABGELEHNT", "positionsdaten": [{"positionsnummer": 1}]}]}, "transaktionsdaten": {"datenaustauschreferenz": "M0FOXT1T", "sparte": "STROM", "pruefidentifikator": "21032", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "marktrolle": "LF", "rollencodenummer": "9903323000007", "rollencodetyp": "BDEW", "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "nachname": "laue", "eMailAdresse": "lieferantenwechsel@eon-energie.com"}}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "marktrolle": "MSB", "rollencodenummer": "9978414000000", "rollencodetyp": "BDEW"}, "dokumentennummer": "M0GA75EU", "kategorie": "Z09", "nachrichtendatum": "2024-08-21T06:34:00Z", "nachrichtenreferenznummer": "M069PO9R", "antwortstatus": "A02", "antwortstatusCodeliste": "E_0205", "angebotsnummer": "4536985"}, "zusatzdaten": {}}}]}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

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
| [E_0205](/referenz/202604/ebd/E_0205) | Angebot prüfen |

</details>

<a id="abschnitt-informationen"></a>

## Prozess-Informationen

Wortlaut der Lesefassung, Steckbrief Kap. 3.6.3.4.1, S. 70–71.

<Stepper>
<ol>

<li data-blatt="vorbedingungen">

### Vorbedingungen

- Bei einer Marktlokation mit einer zugeordneten Messlokation muss diese mit einer mME oder iMS ausgestattet sein.
- Bei einer Marktlokation mit mindestens zwei zugeordneten Messlokationen muss mindestens eine Messlokation mit einer mME/einem iMS ausgestattet sein
- Der LF ist der Marktlokation der Messlokation/en zugeordnet.
- Es besteht noch keine Vereinbarung zum Zeitpunkt der Angebotsgültigkeit.

</li>

<li data-blatt="ergebnisse">

### Ergebnisse

- Der MSB der Marktlokation kann dem LF den Messstellenbetrieb in Rechnung stellen oder
- der MSB der Marktlokation kann Kontakt zum AN aufnehmen oder
- bei iMS hat der MSB der Marktlokation die Abrechnung des Messstellenbetriebes bereits über einem anderen LF einer von der POG Ermittlung betroffenen Marktlokation aufgebaut.
- Die Rechnungsabwicklung gilt ab der Bestätigung des Angebotes, mit Wirkung zum angefragten Abrechnungsbeginn, unbefristet. Ggf. bereits vorher bestätigte Rechnungsabwicklungen gegenüber demselben LF, welche nach dem Abrechnungsbeginn beginnen würden, sind somit gegenstandslos.

</li>

<li data-blatt="fehlerfall">

### Fehlerfall

#### Fehlerfälle

- Die Messlokation konnte nicht identifiziert werden.
- Der LF ist nicht der Marktlokation zugeordnet.

</li>

<li data-blatt="anforderungen">

### Weitere Anforderungen

Ändert sich im Rahmen eines Lieferbeginn- bzw. E/G-Prozesses (GPKE Teil 2) der AN, jedoch nicht der LF, wird auf Grund dieses Sachverhalts durch den MSB der Marktlokation kein neues Angebot an den LF versendet, da diese Änderung für den MSB der Marktlokation nicht ersichtlich ist.

</li>

<li data-blatt="erste-nachricht">

### Erste Nachricht

**MSB (entspricht MSB am Objekt Marktlokation)** sendet „Angebot zur Rechnungs-abwicklung des Messstellenbetriebes über den LF“ (Schritt 1). Ab hier ist der Beteiligte dieser Seite am Zug.

</li>

<li data-blatt="ziel">

### Ziel

Der LF ist Zahler des Messstellenbetriebes oder der LF ist nicht Zahler des Messstellenbetriebes.

</li>

</ol>
</Stepper>

<a id="abschnitt-sichten"></a>

## Andere Sichten des Prozesses

Derselbe Prozess, aus den Augen der anderen Beteiligten: dieselben Schritte, jeweils aus deren Sicht gelesen.

- [Sicht MSB-MALO](/prozessdoku/202604/MSB/WiM-Teil1-angebot-zur-rechnungsabwicklung-des-messstellenbetriebes-ueber-den-lf-durch-den-msb) — MSB am Objekt Marktlokation · Marktrolle MSB

<Hinweisbereich>

*Die Schritte sind die **möglichen** Nachrichten dieses Prozesses, keine Abfolge — die Quelle führt weder Bedingungen noch Alternativen. Das Kästchen am Schritt nennt links die eigene Sicht: **←** empfängt sie, **→** sendet sie. Zugeklappte Schritte laufen zwischen anderen Marktpartnern.*

Zu den Prüfidentifikatoren dieser Schritte liegt kein Testfall im Testbestand; der Knopf »Ausprobieren« der schreibenden Schnittstelle bietet deshalb keinen Rumpf an.

Betrifft: [1](#schritt-1)

</Hinweisbereich>
