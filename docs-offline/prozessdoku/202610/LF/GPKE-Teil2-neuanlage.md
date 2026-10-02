# Neuanlage — Sicht LF

<Kopf rolle="LF" beteiligter="LF" festlegung="GPKE" dokument="GPKE Teil 2" kapitel="2.2.2" sparte="Strom" schritte={3} suchtitel="Neuanlage — Sicht LF · GPKE Teil 2 · Formatversion 202610" abschnitte={[{"id": "abschnitt-ablauf", "label": "Prozessablauf"}, {"id": "abschnitt-schritte", "label": "Prozessschritte"}, {"id": "abschnitt-informationen", "label": "Prozess-Informationen"}, {"id": "abschnitt-sichten", "label": "Andere Sichten des Prozesses"}]} />

<Kurzfassung>

Ein LF meldet beim NB eine Zuordnung des LF zu einer Marktlokation bzw. Tranche an.

</Kurzfassung>

<a id="abschnitt-ablauf"></a>

## Prozessablauf aus Sicht des LF

<Systembild svg={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1004 749\" width=\"1004\" height=\"749\" role=\"img\" aria-labelledby=\"sb-title\" class=\"maco-systembild\">\n<title id=\"sb-title\">Systembild: Neuanlage aus Sicht LF</title>\n<defs><marker id=\"sb-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect class=\"sb-lane-kopf\" x=\"16\" y=\"12\" width=\"232\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend-System des Kunden</text>\n<rect class=\"sb-lane-kopf\" x=\"398\" y=\"12\" width=\"264\" height=\"46\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · LF</text>\n<rect class=\"sb-lane-kopf\" x=\"812\" y=\"12\" width=\"176\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"900\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Marktpartner</text>\n<line x1=\"323\" y1=\"58\" x2=\"323\" y2=\"737\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"737\" y1=\"58\" x2=\"737\" y2=\"737\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect class=\"sb-kasten sb-trigger\" x=\"432\" y=\"80\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessauslöser empfangen</text>\n<rect class=\"sb-kasten sb-backend sb-trigger\" x=\"34\" y=\"80\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">START_LIEFERBEGINN</text>\n<line x1=\"230\" y1=\"96\" x2=\"432\" y2=\"96\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"88\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"144\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"164\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">1. Anmeldung einer</text>\n<text x=\"530\" y=\"179\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Zuordnung des LF zur</text>\n<text x=\"530\" y=\"194\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Marktlokation bzw. Tra…</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"113\" x2=\"530\" y2=\"144\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"157\" r=\"5\"/><line x1=\"900\" y1=\"162\" x2=\"900\" y2=\"174\"/><line x1=\"893\" y1=\"166\" x2=\"907\" y2=\"166\"/><line x1=\"900\" y1=\"174\" x2=\"894\" y2=\"184\"/><line x1=\"900\" y1=\"174\" x2=\"906\" y2=\"184\"/></g>\n<text x=\"900\" y=\"206\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"628\" y1=\"175\" x2=\"878\" y2=\"175\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"167\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"191\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">55600, 55601</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"233\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"253\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"207\" x2=\"530\" y2=\"233\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"233\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"253\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"249\" x2=\"230\" y2=\"249\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"241\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"297\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"317\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">2. Zuordnung des LF zur</text>\n<text x=\"530\" y=\"332\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Marktlokation bzw. Tranche</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"266\" x2=\"530\" y2=\"297\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"303\" r=\"5\"/><line x1=\"900\" y1=\"308\" x2=\"900\" y2=\"320\"/><line x1=\"893\" y1=\"312\" x2=\"907\" y2=\"312\"/><line x1=\"900\" y1=\"320\" x2=\"894\" y2=\"330\"/><line x1=\"900\" y1=\"320\" x2=\"906\" y2=\"330\"/></g>\n<text x=\"900\" y=\"352\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"878\" y1=\"321\" x2=\"628\" y2=\"321\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"313\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"337\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">55602, 55603</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"380\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"400\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z33</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"345\" x2=\"530\" y2=\"380\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"444\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"464\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"413\" x2=\"530\" y2=\"444\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"444\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"464\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"460\" x2=\"230\" y2=\"460\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"452\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"508\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"528\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">3. Ablehnung der Anmeldung</text>\n<text x=\"530\" y=\"543\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">einer Zuordnung des LF zur</text>\n<text x=\"530\" y=\"558\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Marktlok…</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"477\" x2=\"530\" y2=\"508\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"521\" r=\"5\"/><line x1=\"900\" y1=\"526\" x2=\"900\" y2=\"538\"/><line x1=\"893\" y1=\"530\" x2=\"907\" y2=\"530\"/><line x1=\"900\" y1=\"538\" x2=\"894\" y2=\"548\"/><line x1=\"900\" y1=\"538\" x2=\"906\" y2=\"548\"/></g>\n<text x=\"900\" y=\"570\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"878\" y1=\"539\" x2=\"628\" y2=\"539\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"531\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"555\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">55604, 55605</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"597\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"617\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z33</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"571\" x2=\"530\" y2=\"597\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"661\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"681\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"630\" x2=\"530\" y2=\"661\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"661\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"681\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"677\" x2=\"230\" y2=\"677\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"669\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n</svg>"} gesamt={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 730 548\" width=\"730\" height=\"548\" role=\"img\" aria-labelledby=\"sd-title\" class=\"maco-sequence\">\n<title id=\"sd-title\">Sequenzdiagramm: Neuanlage aus Sicht LF</title>\n<defs><marker id=\"sd-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect x=\"16\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"121\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend (Kunde)</text>\n<line x1=\"121\" y1=\"64\" x2=\"121\" y2=\"536\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"260\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"365\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · LF</text>\n<line x1=\"365\" y1=\"64\" x2=\"365\" y2=\"536\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"504\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"609\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"609\" y1=\"64\" x2=\"609\" y2=\"536\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"121\" y1=\"90\" x2=\"365\" y2=\"90\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"81\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">START_LIEFERBEGINN</text>\n<text x=\"243\" y=\"105\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Trigger-Event</text>\n<line x1=\"365\" y1=\"152\" x2=\"609\" y2=\"152\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"143\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">1. Anmeldung einer Zuordnung des LF zur Marktlok…</text>\n<text x=\"487\" y=\"167\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55600, 55601</text>\n<line x1=\"365\" y1=\"214\" x2=\"121\" y2=\"214\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"205\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"229\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"609\" y1=\"276\" x2=\"365\" y2=\"276\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"267\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">2. Zuordnung des LF zur Marktlokation bzw. Tranc…</text>\n<text x=\"487\" y=\"291\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55602, 55603 · E_0608</text>\n<text x=\"487\" y=\"304\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0608 — Anmeldung einer Zuordnung</text>\n<line x1=\"365\" y1=\"338\" x2=\"121\" y2=\"338\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"329\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"353\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"609\" y1=\"400\" x2=\"365\" y2=\"400\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"391\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">3. Ablehnung der Anmeldung einer Zuordnung des L…</text>\n<text x=\"487\" y=\"415\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55604, 55605 · E_0608</text>\n<text x=\"487\" y=\"428\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0608 — Anmeldung einer Zuordnung</text>\n<line x1=\"365\" y1=\"462\" x2=\"121\" y2=\"462\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"453\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"477\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n</svg>"} titel="LF" />

<a id="abschnitt-schritte"></a>

## Prozessschritte

<Schritt nr="1" anker="schritt-1" richtung="ausgehend" kopf={{"links": {"label": "LF", "eigen": true}, "rechts": {"label": "NB"}}}>

### Anmeldung einer Zuordnung des LF zur Marktlokation bzw. Tranche

<Schrittskizze sicht={{"label": "LF"}} zeilen={[{"art": "ausloeser", "werte": ["START_LIEFERBEGINN"]}, {"art": "senden", "label": "NB", "weg": "AS4", "nachrichten": [{"nr": "55600", "titel": "Anmeldung neuer verb. MaLo"}, {"nr": "55601", "titel": "Anmeldung neuer erz. MaLo"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55600](/schnittstellen/202610/pruefi/UTILMD/PI_55600) — Anmeldung neuer verb. MaLo · AS4
- [55601](/schnittstellen/202610/pruefi/UTILMD/PI_55601) — Anmeldung neuer erz. MaLo · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="ausloeser">

**Prozessauslöser** [`START_LIEFERBEGINN`](/schnittstellen/202610/trigger/events/LF-START_LIEFERBEGINN) · [Im Playground ausprobieren](/api/202610/ausloeser-lf/start-lieferbeginn)

Das Backend stößt diesen Schritt mit diesem Ereignis an.

</li>

<li data-teil="nachricht">

Nachricht an **NB** · AS4

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202610/backend-schreiben-lf/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": false, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"ENERGIELIEFERVERTRAG\": [\n      {\n        \"boTyp\": \"VERTRAG\",\n        \"korrespondenzpartner\": {\n          \"ansprechpartner\": {\n            \"boTyp\": \"ANSPRECHPARTNER\",\n            \"eMailAdresse\": \"max@mustermann.de\",\n            \"versionStruktur\": \"1\"\n          },\n          \"boTyp\": \"GESCHAEFTSPARTNER\",\n          \"gewerbekennzeichnung\": false,\n          \"name1\": \"Fank Müller\",\n          \"partneradresse\": {\n            \"hausnummer\": \"25\",\n            \"landescode\": \"DE\",\n            \"ort\": \"Musterstadt\",\n            \"ortsteil\": \"Musterortsteil\",\n            \"postleitzahl\": \"55555\",\n            \"strasse\": \"Wohnstrasse\"\n          },\n          \"versionStruktur\": \"1\"\n        },\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\",\n        \"vertragsart\": \"ENERGIELIEFERVERTRAG\",\n        \"vertragspartner2\": [\n          {\n            \"boTyp\": \"GESCHAEFTSPARTNER\",\n            \"geschaeftspartnerrolle\": [\n              \"KUNDE\"\n            ],\n            \"gewerbekennzeichnung\": true,\n            \"name1\": \"Firma AG\",\n            \"name2\": \"Musterfirma\",\n            \"versionStruktur\": \"1\"\n          }\n        ]\n      }\n    ],\n    \"MARKTLOKATION\": [\n      {\n        \"boTyp\": \"MARKTLOKATION\",\n        \"datenqualitaet\": \"IM_SYSTEM_VORHANDENE_DATEN\",\n        \"erforderlichesProduktpaket\": [\n          {\n            \"priorisierung\": \"PRIORITAET1\",\n            \"produkt\": [\n              {\n                \"produktCode\": \"9991000002082\",\n                \"wertedetails\": \"11XBKA---------I\"\n              }\n            ],\n            \"produktpaketId\": 1,\n            \"umsetzungsgradvorgabe\": \"ZUORDNUNG_NUR_WENN_PRODUKTPAKET_UMSETZBAR\"\n          },\n          {\n            \"priorisierung\": \"PRIORITAET2\",\n            \"produkt\": [\n              {\n                \"produktCode\": \"9991000002082\",\n                \"wertedetails\": \"22XBKA---------I\"\n              }\n            ],\n            \"produktpaketId\": 2,\n            \"umsetzungsgradvorgabe\": \"ZUORDNUNG_NUR_WENN_PRODUKTPAKET_UMSETZBAR\"\n          }\n        ],\n        \"lokationsadresse\": {\n          \"hausnummer\": \"36\",\n          \"landescode\": \"DE\",\n          \"ort\": \"Musterstadt\",\n          \"ortsteil\": \"Musterortsteil\",\n          \"postleitzahl\": \"55555\",\n          \"strasse\": \"Eichelbergstr.\",\n          \"zusatzInformation\": {\n            \"zusatz1\": \"Die Marktlokation befindet sich i\",\n            \"zusatz2\": \"m Hinterhaus im u\",\n            \"zusatz3\": \"nteren K\",\n            \"zusatz4\": \"eller recht\",\n            \"zusatz5\": \"s\"\n          }\n        },\n        \"marktlokationsId\": \"20072281644\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"MESSLOKATION\": [\n      {\n        \"boTyp\": \"MESSLOKATION\",\n        \"messlokationsId\": \"DE00713739359S0000000000001222221\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"NETZNUTZUNGSVERTRAG\": [\n      {\n        \"boTyp\": \"VERTRAG\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\",\n        \"vertragsart\": \"NETZNUTZUNGSVERTRAG\",\n        \"vertragsbeginn\": \"2025-11-01T23:00:00Z\",\n        \"vertragsende\": \"2025-12-01T23:00:00Z\",\n        \"vertragskonditionen\": {\n          \"haushaltskunde\": true\n        }\n      }\n    ],\n    \"STEUERBARE_RESSOURCE\": [\n      {\n        \"boTyp\": \"STEUERBARE_RESSOURCE\",\n        \"ressourcenId\": \"C816417ST77\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"TECHNISCHE_RESSOURCE\": [\n      {\n        \"boTyp\": \"TECHNISCHE_RESSOURCE\",\n        \"ressourcenId\": \"D417MLM8164\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"ZAEHLER\": [\n      {\n        \"boTyp\": \"ZAEHLER\",\n        \"datenqualitaet\": \"IM_SYSTEM_VORHANDENE_DATEN\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\",\n        \"zaehlernummer\": \"12345667890\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9903729000007\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"datenaustauschreferenz\": \"DAGQKITMEGKDRX\",\n    \"dokumentennummer\": \"DA582410161540539903323000007307618\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9900327000009\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"freitext\": \"Bitte\",\n    \"kategorie\": \"E01\",\n    \"nachrichtendatum\": \"2026-11-01T23:00:00Z\",\n    \"nachrichtenreferenznummer\": \"DAPTYGIPXPUJXS\",\n    \"pruefidentifikator\": \"55600\",\n    \"sparte\": \"STROM\",\n    \"transaktionsgrund\": \"E02\",\n    \"transaktionsgrundergaenzung\": \"ZW4\",\n    \"transaktionsgrundergaenzungBefristeteAnmeldung\": \"E01\",\n    \"vertragsbeginn\": \"2026-11-01T23:00:00Z\",\n    \"vertragsende\": \"2026-12-01T23:00:00Z\",\n    \"vorgangsnummer\": \"24062416225400000000000102159662022\"\n  },\n  \"zusatzdaten\": {}\n}"} examples={[{"mediaType": "application/json", "examples": [{"name": "55600", "summary": "55600 — Anmeldung neuer verb. MaLo", "value": {"stammdaten": {"MARKTLOKATION": [{"boTyp": "MARKTLOKATION", "versionStruktur": "1", "marktlokationsId": "20072281644", "datenqualitaet": "IM_SYSTEM_VORHANDENE_DATEN", "sparte": "STROM", "lokationsadresse": {"postleitzahl": "55555", "ort": "Musterstadt", "strasse": "Eichelbergstr.", "hausnummer": "36", "landescode": "DE", "ortsteil": "Musterortsteil", "zusatzInformation": {"zusatz1": "Die Marktlokation befindet sich i", "zusatz2": "m Hinterhaus im u", "zusatz3": "nteren K", "zusatz4": "eller recht", "zusatz5": "s"}}, "erforderlichesProduktpaket": [{"produktpaketId": 1, "produkt": [{"produktCode": "9991000002082", "wertedetails": "11XBKA---------I"}], "umsetzungsgradvorgabe": "ZUORDNUNG_NUR_WENN_PRODUKTPAKET_UMSETZBAR", "priorisierung": "PRIORITAET1"}, {"produktpaketId": 2, "produkt": [{"produktCode": "9991000002082", "wertedetails": "22XBKA---------I"}], "umsetzungsgradvorgabe": "ZUORDNUNG_NUR_WENN_PRODUKTPAKET_UMSETZBAR", "priorisierung": "PRIORITAET2"}]}], "MESSLOKATION": [{"boTyp": "MESSLOKATION", "versionStruktur": "1", "messlokationsId": "DE00713739359S0000000000001222221", "sparte": "STROM"}], "TECHNISCHE_RESSOURCE": [{"boTyp": "TECHNISCHE_RESSOURCE", "versionStruktur": "1", "ressourcenId": "D417MLM8164", "sparte": "STROM"}], "STEUERBARE_RESSOURCE": [{"boTyp": "STEUERBARE_RESSOURCE", "versionStruktur": "1", "ressourcenId": "C816417ST77", "sparte": "STROM"}], "NETZNUTZUNGSVERTRAG": [{"boTyp": "VERTRAG", "versionStruktur": "1", "vertragsart": "NETZNUTZUNGSVERTRAG", "sparte": "STROM", "vertragsbeginn": "2025-11-01T23:00:00Z", "vertragsende": "2025-12-01T23:00:00Z", "vertragskonditionen": {"haushaltskunde": true}}], "ENERGIELIEFERVERTRAG": [{"boTyp": "VERTRAG", "versionStruktur": "1", "vertragsart": "ENERGIELIEFERVERTRAG", "sparte": "STROM", "vertragspartner2": [{"boTyp": "GESCHAEFTSPARTNER", "versionStruktur": "1", "name1": "Firma AG", "name2": "Musterfirma", "gewerbekennzeichnung": true, "geschaeftspartnerrolle": ["KUNDE"]}], "korrespondenzpartner": {"boTyp": "GESCHAEFTSPARTNER", "versionStruktur": "1", "name1": "Fank Müller", "gewerbekennzeichnung": false, "partneradresse": {"postleitzahl": "55555", "ort": "Musterstadt", "strasse": "Wohnstrasse", "hausnummer": "25", "landescode": "DE", "ortsteil": "Musterortsteil"}, "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "eMailAdresse": "max@mustermann.de"}}}], "ZAEHLER": [{"boTyp": "ZAEHLER", "versionStruktur": "1", "zaehlernummer": "12345667890", "sparte": "STROM", "datenqualitaet": "IM_SYSTEM_VORHANDENE_DATEN"}]}, "transaktionsdaten": {"datenaustauschreferenz": "DAGQKITMEGKDRX", "sparte": "STROM", "transaktionsgrund": "E02", "transaktionsgrundergaenzung": "ZW4", "transaktionsgrundergaenzungBefristeteAnmeldung": "E01", "vorgangsnummer": "24062416225400000000000102159662022", "pruefidentifikator": "55600", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9903729000007", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900327000009", "rollencodetyp": "BDEW"}, "dokumentennummer": "DA582410161540539903323000007307618", "kategorie": "E01", "nachrichtendatum": "2026-11-01T23:00:00Z", "nachrichtenreferenznummer": "DAPTYGIPXPUJXS", "freitext": "Bitte", "vertragsbeginn": "2026-11-01T23:00:00Z", "vertragsende": "2026-12-01T23:00:00Z"}, "zusatzdaten": {}}}, {"name": "55601", "summary": "55601 — Anmeldung neuer erz. MaLo", "value": {"stammdaten": {"MARKTLOKATION": [{"boTyp": "MARKTLOKATION", "versionStruktur": "1", "marktlokationsId": "20072281644", "datenqualitaet": "GUELTIGE_DATEN", "marktlokationsTyp": [{"typ": "STANDARD_MARKTLOKATION"}], "sparte": "STROM", "foerderungsLand": "DE", "erforderlichesProduktpaket": [{"produktpaketId": 1, "produkt": [{"produktCode": "9991000002082", "wertedetails": "11XBKA---------I"}, {"produktCode": "9991000002008", "codeProdukteigenschaft": "9991000002115"}, {"produktCode": "9991000002066", "codeProdukteigenschaft": "9991000002272"}, {"produktCode": "9991000002404", "codeProdukteigenschaft": "9991000002420"}], "umsetzungsgradvorgabe": "ZUORDNUNG_NUR_WENN_PRODUKTPAKET_UMSETZBAR", "priorisierung": "PRIORITAET1"}, {"produktpaketId": 2, "produkt": [{"produktCode": "9991000002082", "wertedetails": "22XBKA---------I"}, {"produktCode": "9991000002008", "codeProdukteigenschaft": "9991000002115"}, {"produktCode": "9991000002066", "codeProdukteigenschaft": "9991000002272"}, {"produktCode": "9991000002404", "codeProdukteigenschaft": "9991000002420"}], "umsetzungsgradvorgabe": "ZUORDNUNG_NUR_WENN_PRODUKTPAKET_UMSETZBAR", "priorisierung": "PRIORITAET2"}]}, {"boTyp": "MARKTLOKATION", "versionStruktur": "1", "marktlokationsId": "20072281644", "marktlokationsTyp": [{"typ": "STANDARD_MARKTLOKATION"}], "sparte": "STROM", "datenqualitaet": "IM_SYSTEM_VORHANDENE_DATEN", "lokationsadresse": {"postleitzahl": "55555", "ort": "Musterstadt", "strasse": "Eichelbergstr.", "hausnummer": "36", "landescode": "DE", "ortsteil": "Musterortsteil", "zusatzInformation": {"zusatz1": "Die Marktlokation befindet sich i", "zusatz2": "m Hinterhaus im u", "zusatz3": "nteren K", "zusatz4": "eller recht", "zusatz5": "s"}}}], "MESSLOKATION": [{"boTyp": "MESSLOKATION", "versionStruktur": "1", "messlokationsId": "DE00713739359S0000000000001222221", "sparte": "STROM"}], "TECHNISCHE_RESSOURCE": [{"boTyp": "TECHNISCHE_RESSOURCE", "versionStruktur": "1", "ressourcenId": "D417MLM8164", "sparte": "STROM"}], "STEUERBARE_RESSOURCE": [{"boTyp": "STEUERBARE_RESSOURCE", "versionStruktur": "1", "ressourcenId": "C816417ST77", "sparte": "STROM"}], "NETZNUTZUNGSVERTRAG": [{"boTyp": "VERTRAG", "versionStruktur": "1", "vertragsart": "NETZNUTZUNGSVERTRAG", "sparte": "STROM", "vertragsbeginn": "2026-11-01T23:00:00Z"}], "ENERGIELIEFERVERTRAG": [{"boTyp": "VERTRAG", "versionStruktur": "1", "vertragsart": "ENERGIELIEFERVERTRAG", "sparte": "STROM", "vertragspartner2": [{"boTyp": "GESCHAEFTSPARTNER", "versionStruktur": "1", "name1": "Firma AG", "name2": "Musterfirma", "gewerbekennzeichnung": true, "geschaeftspartnerrolle": ["KUNDE"]}], "korrespondenzpartner": {"boTyp": "GESCHAEFTSPARTNER", "versionStruktur": "1", "name1": "Fank Müller", "gewerbekennzeichnung": false, "partneradresse": {"postleitzahl": "55555", "ort": "Musterstadt", "strasse": "Wohnstrasse", "hausnummer": "25", "landescode": "DE", "ortsteil": "Musterortsteil"}, "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "eMailAdresse": "max@mustermann.de"}}}], "ZAEHLER": [{"boTyp": "ZAEHLER", "versionStruktur": "1", "zaehlernummer": "12345667890", "sparte": "STROM", "datenqualitaet": "IM_SYSTEM_VORHANDENE_DATEN"}]}, "transaktionsdaten": {"datenaustauschreferenz": "DAQFULBRFEASQQ", "sparte": "STROM", "transaktionsgrund": "E02", "transaktionsgrundergaenzung": "ZW2", "vorgangsnummer": "24062416225400000000000102159662022", "pruefidentifikator": "55601", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9903729000007", "rollencodetyp": "BDEW", "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "nachname": "P GETTY", "rufnummern": [{"nummerntyp": "RUF_DURCHWAHL", "rufnummer": "+3222271020"}]}}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9900327000009", "rollencodetyp": "BDEW"}, "dokumentennummer": "DA062410170853319903323000007389284", "kategorie": "E01", "nachrichtendatum": "2026-10-02T11:00:00Z", "nachrichtenreferenznummer": "DAFAWAGSXUVWGU", "freitext": "Bitte", "abtretungserklaerung": {"passwort": "KNSG5674?\"Â§", "link1": "https://www.Stadtwerk_xy.de/...", "link2": "X", "link3": "X", "link4": "X", "link5": "X"}, "vertragsbeginn": "2026-11-01T23:00:00Z"}, "zusatzdaten": {}}}]}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend fort, nachdem die Nachricht erstellt ist.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="2" anker="schritt-2" richtung="eingehend" kopf={{"links": {"label": "LF", "eigen": true}, "rechts": {"label": "NB"}}}>

### Zuordnung des LF zur Marktlokation bzw. Tranche

<Schrittskizze sicht={{"label": "LF"}} zeilen={[{"art": "empfangen", "label": "NB", "weg": "AS4", "nachrichten": [{"nr": "55602", "titel": "Bestätigung Anmeldung neuer verb. MaLo"}, {"nr": "55603", "titel": "Bestätigung Anmeldung neuer erz. MaLo"}]}, {"art": "aperak", "werte": ["Z33"]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55602](/schnittstellen/202610/pruefi/UTILMD/PI_55602) — Bestätigung Anmeldung neuer verb. MaLo · AS4
- [55603](/schnittstellen/202610/pruefi/UTILMD/PI_55603) — Bestätigung Anmeldung neuer erz. MaLo · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **NB** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `55602`, `55603` → [E_0608](/referenz/202610/ebd/E_0608) · NB · Anmeldung einer Zuordnung

</div>

</li>

<li data-teil="aperak">

**Aperak-Prüfungen**
- `55602`, `55603` → `Z33` — Aperak Prüfung: Ist referenzierte Nachricht bekannt ?

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202610/backend-schreiben-lf/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": false, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"MARKTLOKATION\": [\n      {\n        \"boTyp\": \"MARKTLOKATION\",\n        \"datenqualitaet\": \"INFORMATIVE_DATEN\",\n        \"marktlokationsId\": \"20072281644\",\n        \"marktrollen\": [\n          {\n            \"boTyp\": \"MARKTTEILNEHMER\",\n            \"gewerbekennzeichnung\": true,\n            \"marktrolle\": \"MSB\",\n            \"messstellenbetreiberEigenschaft\": \"GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER\",\n            \"rollencodenummer\": \"9910812000000\",\n            \"rollencodetyp\": \"BDEW\",\n            \"versionStruktur\": \"1\",\n            \"weiterverpflichtet\": false\n          }\n        ],\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"MESSLOKATION\": [\n      {\n        \"boTyp\": \"MESSLOKATION\",\n        \"datenqualitaet\": \"INFORMATIVE_DATEN\",\n        \"marktrollen\": [\n          {\n            \"boTyp\": \"MARKTTEILNEHMER\",\n            \"gewerbekennzeichnung\": true,\n            \"marktrolle\": \"MSB\",\n            \"messstellenbetreiberEigenschaft\": \"GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER\",\n            \"rollencodenummer\": \"9910812000000\",\n            \"rollencodetyp\": \"BDEW\",\n            \"versionStruktur\": \"1\",\n            \"weiterverpflichtet\": false\n          },\n          {\n            \"boTyp\": \"MARKTTEILNEHMER\",\n            \"gewerbekennzeichnung\": true,\n            \"marktrolle\": \"GMSB\",\n            \"rollencodenummer\": \"9910812000000\",\n            \"rollencodetyp\": \"BDEW\",\n            \"versionStruktur\": \"1\"\n          }\n        ],\n        \"messlokationsId\": \"DE00713739359S0000000000001222221\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"NETZLOKATION\": [\n      {\n        \"boTyp\": \"NETZLOKATION\",\n        \"datenqualitaet\": \"INFORMATIVE_DATEN\",\n        \"marktrollen\": [\n          {\n            \"boTyp\": \"MARKTTEILNEHMER\",\n            \"gewerbekennzeichnung\": true,\n            \"marktrolle\": \"MSB\",\n            \"messstellenbetreiberEigenschaft\": \"GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER\",\n            \"rollencodenummer\": \"9910812000000\",\n            \"rollencodetyp\": \"BDEW\",\n            \"versionStruktur\": \"1\"\n          }\n        ],\n        \"netzlokationsId\": \"E1688117482\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"NETZNUTZUNGSVERTRAG\": [\n      {\n        \"boTyp\": \"VERTRAG\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\",\n        \"vertragsart\": \"NETZNUTZUNGSVERTRAG\",\n        \"vertragsbeginn\": \"2025-11-01T23:00:00Z\",\n        \"vertragsende\": \"2025-12-01T23:00:00Z\"\n      }\n    ],\n    \"STEUERBARE_RESSOURCE\": [\n      {\n        \"boTyp\": \"STEUERBARE_RESSOURCE\",\n        \"datenqualitaet\": \"INFORMATIVE_DATEN\",\n        \"marktrollen\": [\n          {\n            \"boTyp\": \"MARKTTEILNEHMER\",\n            \"gewerbekennzeichnung\": true,\n            \"marktrolle\": \"MSB\",\n            \"messstellenbetreiberEigenschaft\": \"GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER\",\n            \"rollencodenummer\": \"9910812000000\",\n            \"rollencodetyp\": \"BDEW\",\n            \"versionStruktur\": \"1\"\n          }\n        ],\n        \"ressourcenId\": \"C816417ST77\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"TECHNISCHE_RESSOURCE\": [\n      {\n        \"boTyp\": \"TECHNISCHE_RESSOURCE\",\n        \"ressourcenId\": \"D417MLM8164\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"ansprechpartner\": {\n        \"boTyp\": \"ANSPRECHPARTNER\",\n        \"nachname\": \"P GETTY\",\n        \"rufnummern\": [\n          {\n            \"nummerntyp\": \"RUF_DURCHWAHL\",\n            \"rufnummer\": \"+3222271020\"\n          }\n        ],\n        \"versionStruktur\": \"1\"\n      },\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9900327000009\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"anfragereferenznummer\": \"NNV1234\",\n    \"antwortstatus\": \"A09\",\n    \"antwortstatusCodeliste\": \"E_0608\",\n    \"datenaustauschreferenz\": \"DACQJFPMZCSHOE\",\n    \"dokumentennummer\": \"DA662410170909149903323000007531700\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9903729000007\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"geplantesProduktpaket\": 1,\n    \"kategorie\": \"E01\",\n    \"nachrichtendatum\": \"2025-06-24T12:31:00Z\",\n    \"nachrichtenreferenznummer\": \"DAUBVEOKLGICGS\",\n    \"pruefidentifikator\": \"55602\",\n    \"sparte\": \"STROM\",\n    \"transaktionsgrund\": \"E02\",\n    \"transaktionsgrundergaenzung\": \"ZW7\",\n    \"transaktionsgrundergaenzungBefristeteAnmeldung\": \"E01\",\n    \"vertragsbeginn\": \"2025-11-01T23:00:00Z\",\n    \"vertragsende\": \"2025-12-01T23:00:00Z\",\n    \"vorgangsnummer\": \"24062416225400000000000102159662022\"\n  },\n  \"zusatzdaten\": {}\n}"} examples={[{"mediaType": "application/json", "examples": [{"name": "55602", "summary": "55602 — Bestätigung Anmeldung neuer verb. MaLo", "value": {"stammdaten": {"MARKTLOKATION": [{"boTyp": "MARKTLOKATION", "versionStruktur": "1", "marktlokationsId": "20072281644", "sparte": "STROM", "datenqualitaet": "INFORMATIVE_DATEN", "marktrollen": [{"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "marktrolle": "MSB", "gewerbekennzeichnung": true, "rollencodenummer": "9910812000000", "rollencodetyp": "BDEW", "weiterverpflichtet": false, "messstellenbetreiberEigenschaft": "GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER"}]}], "NETZLOKATION": [{"boTyp": "NETZLOKATION", "versionStruktur": "1", "netzlokationsId": "E1688117482", "sparte": "STROM", "datenqualitaet": "INFORMATIVE_DATEN", "marktrollen": [{"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "marktrolle": "MSB", "gewerbekennzeichnung": true, "rollencodenummer": "9910812000000", "rollencodetyp": "BDEW", "messstellenbetreiberEigenschaft": "GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER"}]}], "MESSLOKATION": [{"boTyp": "MESSLOKATION", "versionStruktur": "1", "messlokationsId": "DE00713739359S0000000000001222221", "sparte": "STROM", "datenqualitaet": "INFORMATIVE_DATEN", "marktrollen": [{"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "marktrolle": "MSB", "gewerbekennzeichnung": true, "rollencodenummer": "9910812000000", "rollencodetyp": "BDEW", "weiterverpflichtet": false, "messstellenbetreiberEigenschaft": "GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER"}, {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "marktrolle": "GMSB", "gewerbekennzeichnung": true, "rollencodenummer": "9910812000000", "rollencodetyp": "BDEW"}]}], "TECHNISCHE_RESSOURCE": [{"boTyp": "TECHNISCHE_RESSOURCE", "versionStruktur": "1", "ressourcenId": "D417MLM8164", "sparte": "STROM"}], "STEUERBARE_RESSOURCE": [{"boTyp": "STEUERBARE_RESSOURCE", "versionStruktur": "1", "ressourcenId": "C816417ST77", "sparte": "STROM", "datenqualitaet": "INFORMATIVE_DATEN", "marktrollen": [{"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "marktrolle": "MSB", "gewerbekennzeichnung": true, "rollencodenummer": "9910812000000", "rollencodetyp": "BDEW", "messstellenbetreiberEigenschaft": "GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER"}]}], "NETZNUTZUNGSVERTRAG": [{"boTyp": "VERTRAG", "versionStruktur": "1", "vertragsart": "NETZNUTZUNGSVERTRAG", "sparte": "STROM", "vertragsbeginn": "2025-11-01T23:00:00Z", "vertragsende": "2025-12-01T23:00:00Z"}]}, "transaktionsdaten": {"datenaustauschreferenz": "DACQJFPMZCSHOE", "sparte": "STROM", "transaktionsgrund": "E02", "transaktionsgrundergaenzung": "ZW7", "transaktionsgrundergaenzungBefristeteAnmeldung": "E01", "vorgangsnummer": "24062416225400000000000102159662022", "pruefidentifikator": "55602", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900327000009", "rollencodetyp": "BDEW", "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "nachname": "P GETTY", "rufnummern": [{"nummerntyp": "RUF_DURCHWAHL", "rufnummer": "+3222271020"}]}}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9903729000007", "rollencodetyp": "BDEW"}, "dokumentennummer": "DA662410170909149903323000007531700", "kategorie": "E01", "nachrichtendatum": "2025-06-24T12:31:00Z", "nachrichtenreferenznummer": "DAUBVEOKLGICGS", "anfragereferenznummer": "NNV1234", "antwortstatus": "A09", "antwortstatusCodeliste": "E_0608", "geplantesProduktpaket": 1, "vertragsbeginn": "2025-11-01T23:00:00Z", "vertragsende": "2025-12-01T23:00:00Z"}, "zusatzdaten": {}}}, {"name": "55603", "summary": "55603 — Bestätigung Anmeldung neuer erz. MaLo", "value": {"stammdaten": {"MARKTLOKATION": [{"boTyp": "MARKTLOKATION", "versionStruktur": "1", "marktlokationsId": "50074561188", "datenqualitaet": "INFORMATIVE_DATEN", "marktrollen": [{"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "marktrolle": "MSB", "rollencodenummer": "9904446000007", "weiterverpflichtet": true, "messstellenbetreiberEigenschaft": "GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER"}]}], "MESSLOKATION": [{"boTyp": "MESSLOKATION", "versionStruktur": "1", "messlokationsId": "DE0032106765712000000000000000037", "datenqualitaet": "INFORMATIVE_DATEN", "marktrollen": [{"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "marktrolle": "MSB", "rollencodenummer": "9904446000007", "weiterverpflichtet": true, "messstellenbetreiberEigenschaft": "GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER"}, {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "marktrolle": "GMSB", "rollencodenummer": "9904446000007"}]}], "NETZNUTZUNGSVERTRAG": [{"boTyp": "VERTRAG", "versionStruktur": "1", "vertragsart": "NETZNUTZUNGSVERTRAG", "vertragsbeginn": "2026-06-30T22:00:00Z"}]}, "transaktionsdaten": {"datenaustauschreferenz": "LZYKL8IJ", "transaktionsgrund": "E02", "sparte": "STROM", "transaktionsgrundergaenzung": "ZW0", "vorgangsnummer": "12345", "pruefidentifikator": "55603", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodetyp": "BDEW", "rollencodenummer": "9900321000005"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodetyp": "BDEW", "rollencodenummer": "9903790000002"}, "dokumentennummer": "BGMLZ3F5OQI", "kategorie": "E01", "nachrichtendatum": "2026-10-02T11:00:00Z", "nachrichtenreferenznummer": "UNHLZC2Q77P", "anfragereferenznummer": "ABC123456", "antwortstatus": "A09", "antwortstatusCodeliste": "E_0608", "vertragsbeginn": "2026-06-30T22:00:00Z", "geplantesProduktpaket": 1}}}]}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend mit den Daten der eingegangenen Nachricht fort.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="3" anker="schritt-3" richtung="eingehend" kopf={{"links": {"label": "LF", "eigen": true}, "rechts": {"label": "NB"}}}>

### Ablehnung der Anmeldung einer Zuordnung des LF zur Marktlokation bzw. Tranche

<Schrittskizze sicht={{"label": "LF"}} zeilen={[{"art": "empfangen", "label": "NB", "weg": "AS4", "nachrichten": [{"nr": "55604", "titel": "Ablehnung Anmeldung neuer verb. MaLo"}, {"nr": "55605", "titel": "Ablehnung Anmeldung neuer erz. MaLo"}]}, {"art": "aperak", "werte": ["Z33"]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55604](/schnittstellen/202610/pruefi/UTILMD/PI_55604) — Ablehnung Anmeldung neuer verb. MaLo · AS4
- [55605](/schnittstellen/202610/pruefi/UTILMD/PI_55605) — Ablehnung Anmeldung neuer erz. MaLo · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **NB** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `55604`, `55605` → [E_0608](/referenz/202610/ebd/E_0608) · NB · Anmeldung einer Zuordnung

</div>

</li>

<li data-teil="aperak">

**Aperak-Prüfungen**
- `55604`, `55605` → `Z33` — Aperak Prüfung: Ist referenzierte Nachricht bekannt ?

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202610/backend-schreiben-lf/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": false, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"MARKTLOKATION\": [\n      {\n        \"boTyp\": \"MARKTLOKATION\",\n        \"marktlokationsId\": \"50074561188\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9900321000005\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"anfragereferenznummer\": \"ABC1234\",\n    \"antwortstatus\": \"A01\",\n    \"antwortstatusCodeliste\": \"E_0608\",\n    \"datenaustauschreferenz\": \"LZ5VMD3J\",\n    \"dokumentennummer\": \"BGMLZXL5QSH\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9903790000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"E01\",\n    \"nachrichtendatum\": \"2026-10-02T11:00:00Z\",\n    \"nachrichtenreferenznummer\": \"UNHLZ5RZVR9\",\n    \"pruefidentifikator\": \"55604\",\n    \"sparte\": \"STROM\",\n    \"transaktionsgrund\": \"E02\",\n    \"transaktionsgrundergaenzung\": \"ZW4\",\n    \"vorgangsnummer\": \"12345\"\n  }\n}"} examples={[{"mediaType": "application/json", "examples": [{"name": "55604", "summary": "55604 — Ablehnung Anmeldung neuer verb. MaLo", "value": {"stammdaten": {"MARKTLOKATION": [{"boTyp": "MARKTLOKATION", "versionStruktur": "1", "marktlokationsId": "50074561188", "sparte": "STROM"}]}, "transaktionsdaten": {"datenaustauschreferenz": "LZ5VMD3J", "sparte": "STROM", "transaktionsgrund": "E02", "transaktionsgrundergaenzung": "ZW4", "vorgangsnummer": "12345", "pruefidentifikator": "55604", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9900321000005", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9903790000002", "rollencodetyp": "BDEW"}, "dokumentennummer": "BGMLZXL5QSH", "kategorie": "E01", "nachrichtendatum": "2026-10-02T11:00:00Z", "nachrichtenreferenznummer": "UNHLZ5RZVR9", "anfragereferenznummer": "ABC1234", "antwortstatus": "A01", "antwortstatusCodeliste": "E_0608"}}}, {"name": "55605", "summary": "55605 — Ablehnung Anmeldung neuer erz. MaLo", "value": {"stammdaten": {}, "transaktionsdaten": {"datenaustauschreferenz": "LZIFBZAO", "sparte": "STROM", "transaktionsgrund": "E02", "transaktionsgrundergaenzung": "ZW3", "vorgangsnummer": "12345", "pruefidentifikator": "55605", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9900321000005", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9903790000002", "rollencodetyp": "BDEW"}, "dokumentennummer": "BGMLZU6DM9A", "kategorie": "E01", "nachrichtendatum": "2026-10-02T11:00:00Z", "nachrichtenreferenznummer": "UNHLZKUIZUY", "anfragereferenznummer": "ABC12345", "antwortstatus": "A03", "antwortstatusCodeliste": "E_0608"}}}]}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

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
| [E_0608](/referenz/202610/ebd/E_0608) | Anmeldung einer Zuordnung |

</details>

<a id="abschnitt-informationen"></a>

## Prozess-Informationen

Wortlaut der Lesefassung, Steckbrief Kap. 2.2.1, S. 25–27.

<Stepper>
<ol>

<li data-blatt="vorbedingungen">

### Vorbedingungen

- Im Fall einer verbrauchenden Marktlokation: Abschluss eines Energieliefervertrags zwischen LF und dem Letztverbraucher.
- Im Fall einer erzeugenden Marktlokation bzw. einer Tranche:
  - Abschluss eines Stromabnahmevertrags zwischen LF und dem EZ. Es werden dabei zwei Geschäftsvorfälle betrachtet:
    - Geschäftsvorfall A: Der LF wird einer Marktlokation vollständig zugeordnet.
    - Geschäftsvorfall B: Der LF wird einer Tranche (entsprechend der gewünschten Tranchengröße) zugeordnet.
  - Die Energie einer Marktlokation, die vollständig oder anteilig zur Veräußerungsform einer DV zugeordnet werden soll, ist mit einer viertelstündlichen Auflösung zu messen.
  - Der Use-Case ist nicht durch das Unternehmen Netzbetreiber in seiner Rolle als LF zu starten.
- Es handelt sich um die erstmalige Inbetriebnahme einer Marktlokation (Neuanlage). Dies bedeutet
  - im Fall einer verbrauchenden Marktlokation oder im Fall von Geschäftsvorfall A: Ein LF ist der neu angelegten Marktlokation noch nicht zugeordnet.
  - im Fall von Geschäftsvorfall B: Eine 100% LF-Zuordnung zu der neu angelegten Marktlokation wurde noch nicht hergestellt.
- Eine Zuordnungsermächtigung nach den Prozessen der MaBiS für den vom LF genutzten BK liegt beim NB vor.

</li>

<li data-blatt="ergebnisse">

### Ergebnisse

- Im Fall einer verbrauchenden Marktlokation: Der NB führt die Use-Cases „[Abrechnungsdaten Netznutzungsabrechnung](/prozessdoku/202610/LF/GPKE-Teil2-abrechnungsdaten-netznutzungsabrechnung)“ und „[Abrechnungsdaten Bilanzkreisabrechnung](/prozessdoku/202610/LF/GPKE-Teil2-abrechnungsdaten-bilanzkreisabrechnung)“ aus.
- Im Fall einer erzeugenden Marktlokation bzw. einer Tranche: Der NB führt den Use-Case „[Abrechnungsdaten Bilanzkreisabrechnung](/prozessdoku/202610/LF/GPKE-Teil2-abrechnungsdaten-bilanzkreisabrechnung)“ aus.
- Der NB führt den Use-Case „Stammdatenänderung“ (hier: SD „[Stammdatenänderung vom NB (verantwortlich) ausgehend](/prozessdoku/202610/LF/GPKE-Teil4-stammdatenaenderung-vom-nb-verantwortlich-ausgehend)“) (GPKE Teil 4) durch.
- Der NB versendet die Berechnungsformel an den LF.
- Der NB führt den Use-Case „[Einrichtung der Konfigurationen aufgrund einer Zuordnung eines LF zu einer Marktlokation bzw. Tranche](/prozessdoku/202610/MSB/GPKE-Teil3-einrichtung-der-konfigurationen-aufgrund-einer-zuordnung-eines-lf-zu-einer-marktlokation-bzw-tranche)“ (GPKE Teil 3) aus.
- Im Fall einer Tranche: Etwa entstehende Zuordnungslücken werden vom NB im Rahmen des Use-Cases „Herstellung einer 100% LF-Zuordnung zu einer erzeugenden Marktlokation“ geschlossen.
- Der LF führt den Use-Case „Stammdatenänderung“ (hier: SD „[Stammdatenänderung vom LF (verantwortlich) ausgehend](/prozessdoku/202610/LF/GPKE-Teil4-stammdatenaenderung-vom-lf-verantwortlich-ausgehend)“) (GPKE Teil 4) durch.

</li>

<li data-blatt="fehlerfall">

### Fehlerfall

#### Ergebnis im Fehlerfall

- Der LF wurde der Marktlokation bzw. Tranche nicht zugeordnet.
- Bei nicht-Identifikation der Marktlokation: Der LF geht mit dem Letztverbraucher bzw. EZ in ein bilaterales Clearing.
- Der LF startet bei Bedarf den Use-Case „Neuanlage“ erneut oder
- der LF startet bei Bedarf den Use-Case „[Lieferbeginn](/prozessdoku/202610/LF--LFA/GPKE-Teil2-lieferbeginn)“, sofern dem LF in der Ablehnung mitgeteilt wurde, dass
  - im Fall einer verbrauchenden Marktlokation oder im Fall von Geschäftsvorfall A bereits ein LF der Marktlokation zugeordnet ist.
  - im Fall von Geschäftsvorfall B bereits eine 100% LF-Zuordnung zur Marktlokation hergestellt wurde.
- Im Fall einer verbrauchenden Marktlokation: Der NB führt ggf. den Use-Case „[Beginn der Ersatz-/Grundversorgung](/prozessdoku/202610/LF/GPKE-Teil2-beginn-der-ersatz-grundversorgung)“ aus.
- Im Fall einer erzeugenden Marktlokation bzw. einer Tranche: Der NB führt ggf. den Use-Case „Herstellung einer 100% LF-Zuordnung zu einer erzeugenden Marktlokation“ aus.

#### Fehlerfälle

- Es handelt sich nicht um eine erstmalige Inbetriebnahme einer Marktlokation (Neuanlage). Dies bedeutet
  - im Fall einer verbrauchenden Marktlokation oder im Fall von Geschäftsvorfall A: Ein LF (dies schließt einen E/G mit ein) ist der Marktlokation bereits zugeordnet.
  - im Fall von Geschäftsvorfall B: Eine 100% LF-Zuordnung zur Marktlokation wurde bereits hergestellt (wobei ein LF auch das Unternehmen Netzbetreiber in seiner Rolle als LF sein kann).
- Die Marktlokation kann nicht oder nicht eindeutig durch den NB identifiziert werden.
- Im Fall einer erzeugenden Marktlokation bzw. einer Tranche:
  - Die Energie einer Marktlokation, die vollständig oder anteilig zur Veräußerungsform einer DV zugeordnet werden soll, ist nicht mit einer viertelstündlichen Auflösung messbar.
  - Der Use-Case wird durch das Unternehmen Netzbetreiber in seiner Rolle als LF gestartet.
- Eine Zuordnungsermächtigung nach den Prozessen der MaBiS für den vom LF genutzten BK liegt beim NB nicht vor.

</li>

<li data-blatt="anforderungen">

### Weitere Anforderungen

- Hinweis: Sofern die zum Zuordnungsbeginn vorhandene Gerätetechnik die Anmeldung nicht ermöglicht, ist eine entsprechende Änderung der Gerätetechnik durch den LF bzw. Letztverbraucher bzw. EZ beim MSB zu veranlassen. Der LF kann die Änderung der Gerätetechnik über den WiM-Use-Case zur Messlokationsänderung (WiM Teil 1) beauftragen.
- Hinweis: Im Fall einer erzeugenden Marktlokation bzw. einer Tranche: Das Formular nach Anlage 4 zum Beschluss BK6-16-200 kann für Clearingfälle weiterhin verwendet werden.

</li>

<li data-blatt="erste-nachricht">

### Erste Nachricht

Der Beteiligte dieser Seite sendet selbst: „Anmeldung einer Zuordnung des LF zur Marktlokation bzw. Tranche“ an **NB** (Schritt 1).

</li>

<li data-blatt="ziel">

### Ziel

Der LF ist der Marktlokation bzw. Tranche zum Inbetriebnahmedatum der Marktlokation zugeordnet.

</li>

</ol>
</Stepper>

<a id="abschnitt-sichten"></a>

## Andere Sichten des Prozesses

Derselbe Prozess, aus den Augen der anderen Beteiligten: dieselben Schritte, jeweils aus deren Sicht gelesen.

- [Sicht NB](/prozessdoku/202610/NB/GPKE-Teil2-neuanlage) — NB

<Hinweisbereich>

*Die Schritte sind die **möglichen** Nachrichten dieses Prozesses, keine Abfolge — die Quelle führt weder Bedingungen noch Alternativen. Das Kästchen am Schritt nennt links die eigene Sicht: **←** empfängt sie, **→** sendet sie. Zugeklappte Schritte laufen zwischen anderen Marktpartnern.*

</Hinweisbereich>
