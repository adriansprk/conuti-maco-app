# Übermittlung von Informationen — Sicht NB

<Kopf rolle="NB" beteiligter="NB" festlegung="GPKE" dokument="GPKE Teil 4" kapitel="4.2" sparte="Strom" schritte={1} suchtitel="Übermittlung von Informationen — Sicht NB · GPKE Teil 4 · Formatversion 202610" abschnitte={[{"id": "abschnitt-ablauf", "label": "Prozessablauf"}, {"id": "abschnitt-schritte", "label": "Prozessschritte"}, {"id": "abschnitt-informationen", "label": "Prozess-Informationen"}, {"id": "abschnitt-sichten", "label": "Andere Sichten des Prozesses"}]} />

<Kurzfassung>

Der sendende Marktakteur übermittelt alle Informationen an den empfangenden Marktakteur. Die Übermittlung der Informationen kann dabei zwischen
- vom NB an LF
- vom LF an NB
- vom NB an MSB
- vom MSB an NB
- vom NB an NB
- vom NB an BIKO
- vom BIKO an NB
- vom NB an BKV
- vom BKV an NB
- vom NB an ÜNB
- vom ÜNB an NB
- vom LF an LF
- vom LF an MSB
- vom MSB an LF
- vom LF an ÜNB
- vom ÜNB an LF
- vom BIKO an BKV
- vom BKV an BIKO
- vom ÜNB an BKV
- vom BKV an ÜNB
- vom ÜNB an MSB
- vom MSB an ÜNB
- vom ÜNB an BIKO
- vom BIKO an ÜNB
- vom MSB an MSB
- vom ESA an MSB
- vom MSB an ESA stattfinden und wird im Use-Case mit „sendender Marktakteur“ und „empfangender Marktakteur“ bezeichnet und im SD abgebildet.

</Kurzfassung>

<a id="abschnitt-ablauf"></a>

## Prozessablauf aus Sicht des NB

<Systembild svg={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1004 537\" width=\"1004\" height=\"537\" role=\"img\" aria-labelledby=\"sb-title\" class=\"maco-systembild\">\n<title id=\"sb-title\">Systembild: Übermittlung von Informationen aus Sicht NB</title>\n<defs><marker id=\"sb-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect class=\"sb-lane-kopf\" x=\"16\" y=\"12\" width=\"232\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend-System des Kunden</text>\n<rect class=\"sb-lane-kopf\" x=\"398\" y=\"12\" width=\"264\" height=\"46\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · NB</text>\n<rect class=\"sb-lane-kopf\" x=\"812\" y=\"12\" width=\"176\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"900\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Marktpartner</text>\n<line x1=\"323\" y1=\"58\" x2=\"323\" y2=\"525\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"737\" y1=\"58\" x2=\"737\" y2=\"525\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"80\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">1. Information</text>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"78\" r=\"5\"/><line x1=\"900\" y1=\"83\" x2=\"900\" y2=\"95\"/><line x1=\"893\" y1=\"87\" x2=\"907\" y2=\"87\"/><line x1=\"900\" y1=\"95\" x2=\"894\" y2=\"105\"/><line x1=\"900\" y1=\"95\" x2=\"906\" y2=\"105\"/></g>\n<text x=\"900\" y=\"127\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">LF</text>\n<line x1=\"878\" y1=\"96\" x2=\"628\" y2=\"96\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"88\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"112\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">21045, 37000, 37000…</text>\n<rect class=\"sb-kasten sb-aperak_lesen\" x=\"432\" y=\"163\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"183\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Daten für die</text>\n<text x=\"530\" y=\"198\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Eingangsprüfung laden</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"113\" x2=\"530\" y2=\"163\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-aperak_lesen\" x=\"34\" y=\"171\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"191\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Marktlokation lesen</text>\n<line x1=\"432\" y1=\"187\" x2=\"230\" y2=\"187\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"179\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"237\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"257\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z10, Z16,</text>\n<text x=\"530\" y=\"272\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Z17, Z18</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"211\" x2=\"530\" y2=\"237\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-schreiben\" x=\"432\" y=\"311\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"331\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"285\" x2=\"530\" y2=\"311\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-schreiben\" x=\"34\" y=\"311\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"331\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten erstellen</text>\n<line x1=\"432\" y1=\"327\" x2=\"230\" y2=\"327\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"319\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<text x=\"331\" y=\"343\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">PI 21045</text>\n<rect class=\"sb-kasten sb-schreiben\" x=\"432\" y=\"375\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"395\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"344\" x2=\"530\" y2=\"375\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-schreiben sb-abgeleitet\" x=\"34\" y=\"375\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"395\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten erstellen</text>\n<line x1=\"432\" y1=\"391\" x2=\"230\" y2=\"391\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"383\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<text x=\"331\" y=\"407\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">PI 37000, 37001, 37002, 37003, 37…</text>\n<rect class=\"sb-kasten sb-lesen_verarbeitung\" x=\"432\" y=\"439\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"459\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Daten für die Verarbeitung</text>\n<text x=\"530\" y=\"474\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">laden</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"408\" x2=\"530\" y2=\"439\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-lesen_verarbeitung\" x=\"34\" y=\"439\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"459\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Kommunikationsdaten des</text>\n<text x=\"132\" y=\"474\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Servicean…</text>\n<line x1=\"432\" y1=\"463\" x2=\"230\" y2=\"463\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"455\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n</svg>"} gesamt={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 730 300\" width=\"730\" height=\"300\" role=\"img\" aria-labelledby=\"sd-title\" class=\"maco-sequence\">\n<title id=\"sd-title\">Sequenzdiagramm: Übermittlung von Informationen aus Sicht NB</title>\n<defs><marker id=\"sd-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect x=\"16\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"121\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend (Kunde)</text>\n<line x1=\"121\" y1=\"64\" x2=\"121\" y2=\"288\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"260\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"365\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · NB</text>\n<line x1=\"365\" y1=\"64\" x2=\"365\" y2=\"288\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"504\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"609\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">LF</text>\n<line x1=\"609\" y1=\"64\" x2=\"609\" y2=\"288\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"609\" y1=\"90\" x2=\"365\" y2=\"90\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"81\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">1. Information</text>\n<text x=\"487\" y=\"105\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 21045, 37000, 37000…</text>\n<line x1=\"365\" y1=\"152\" x2=\"121\" y2=\"152\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"143\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<text x=\"243\" y=\"167\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten erstellen · PI 21045</text>\n<line x1=\"365\" y1=\"214\" x2=\"121\" y2=\"214\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"205\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<text x=\"243\" y=\"229\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten erstellen · PI 37000, 37001, 37002, 37003, 37…</text>\n</svg>"} titel="NB" />

<a id="abschnitt-schritte"></a>

## Prozessschritte

<Schritt nr="1" anker="schritt-1" richtung="eingehend" kopf={{"links": {"label": "NB", "eigen": true}, "rechts": {"label": "LF"}}}>

### Information

<Schrittskizze sicht={{"label": "NB"}} zeilen={[{"art": "empfangen", "label": "LF", "weg": "AS4", "nachrichten": [{"nr": "21045", "titel": "EnFG Informationen"}, {"nr": "37000", "titel": "Kommunikationsdaten des LF Strom"}, {"nr": "37001", "titel": "Kommunikationsdaten des NB Strom"}, {"nr": "37002", "titel": "Kommunikationsdaten des MSB Strom"}, {"nr": "37003", "titel": "Kommunikationsdaten des BKV Strom"}, {"nr": "37004", "titel": "Kommunikationsdaten des BIKO Strom"}, {"nr": "37005", "titel": "Kommunikationsdaten des ÜNB Strom"}, {"nr": "37006", "titel": "Kommunikationsdaten des ESA Strom"}, {"nr": "13028", "titel": "Grundlage POG-Ermittlung"}]}, {"art": "lesen_aperak", "schnittstellen": [{"label": "Marktlokation lesen"}]}, {"art": "aperak", "werte": ["Z10", "Z16", "Z17", "Z18"]}, {"art": "erstellen", "nummern": ["21045"]}, {"art": "erstellen", "nummern": ["37000", "37001", "37002", "37003", "37004", "37005", "37006", "13028"]}, {"art": "lesen_verarbeitung", "schnittstellen": [{"label": "Kommunikationsdaten des Serviceanbieters lesen"}]}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [21045](/schnittstellen/202610/pruefi/IFTSTA/PI_21045) — EnFG Informationen · AS4
- [37000](/schnittstellen/202610/pruefi/PARTIN/PI_37000) — Kommunikationsdaten des LF Strom · AS4
- [37001](/schnittstellen/202610/pruefi/PARTIN/PI_37001) — Kommunikationsdaten des NB Strom · AS4
- [37002](/schnittstellen/202610/pruefi/PARTIN/PI_37002) — Kommunikationsdaten des MSB Strom · AS4
- [37003](/schnittstellen/202610/pruefi/PARTIN/PI_37003) — Kommunikationsdaten des BKV Strom · AS4
- [37004](/schnittstellen/202610/pruefi/PARTIN/PI_37004) — Kommunikationsdaten des BIKO Strom · AS4
- [37005](/schnittstellen/202610/pruefi/PARTIN/PI_37005) — Kommunikationsdaten des ÜNB Strom · AS4
- [37006](/schnittstellen/202610/pruefi/PARTIN/PI_37006) — Kommunikationsdaten des ESA Strom · AS4
- [13028](/schnittstellen/202610/pruefi/MSCONS/PI_13028) — Grundlage POG-Ermittlung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **LF** · AS4

</li>

<li data-teil="lesen" data-stufe="aperak">

**Daten für die Eingangsprüfung laden**
- [Marktlokation lesen](/api/202610/backend-lesen/getmarketlocationbasic#marktlokation-lesen) `GET /getMarketLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getMarketLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": false, "defaultValue": "MALO", "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": false, "defaultValue": "2024-06-28T12:18:00Z", "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_MARKTLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

</li>

<li data-teil="aperak">

**Aperak-Prüfungen**
- `21045` → `Z10`
- `21045` → `Z16`
- `21045` → `Z17`
- `21045` → `Z18`

</li>

<li data-teil="schnittstelle" data-art="schreiben">

**Schreibende Schnittstelle**
- `21045` → Vorgang angelegt — [Prozessdaten erstellen](/api/202610/backend-schreiben-nb/createprocessdata#prozessdaten-erstellen) `POST /createProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/createProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "ERSTELLEN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"KOMMUNIKATIONSDATEN\": [\n      {\n        \"boTyp\": \"KOMMUNIKATIONSDATEN\",\n        \"gueltigkeit\": \"2025-06-06T22:00:00Z\",\n        \"kommunikationsDatenBlattInaktiv\": true,\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9903790000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"anwendungsreferenznummer\": \"2\",\n    \"datenaustauschreferenz\": \"113601\",\n    \"dokumentennummer\": \"CS356455854555\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9900321000005\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"10\",\n    \"nachrichtendatum\": \"2026-10-01T11:00:00Z\",\n    \"nachrichtenreferenznummer\": \"298012\",\n    \"pruefidentifikator\": \"37000\",\n    \"sparte\": \"STROM\",\n    \"vorgangsreferenznummer\": \"1\"\n  },\n  \"zusatzdaten\": {}\n}"} examples={[{"mediaType": "application/json", "examples": [{"name": "37000", "summary": "37000 — Kommunikationsdaten des LF Strom", "value": {"stammdaten": {"KOMMUNIKATIONSDATEN": [{"boTyp": "KOMMUNIKATIONSDATEN", "versionStruktur": "1", "gueltigkeit": "2025-06-06T22:00:00Z", "kommunikationsDatenBlattInaktiv": true}]}, "transaktionsdaten": {"datenaustauschreferenz": "113601", "sparte": "STROM", "pruefidentifikator": "37000", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9903790000002", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900321000005", "rollencodetyp": "BDEW"}, "dokumentennummer": "CS356455854555", "kategorie": "10", "nachrichtendatum": "2026-10-01T11:00:00Z", "nachrichtenreferenznummer": "298012", "vorgangsreferenznummer": "1", "anwendungsreferenznummer": "2"}, "zusatzdaten": {}}}, {"name": "37001", "summary": "37001 — Kommunikationsdaten des NB Strom", "value": {"stammdaten": {"KOMMUNIKATIONSDATEN": [{"boTyp": "KOMMUNIKATIONSDATEN", "versionStruktur": "1", "gueltigkeit": "2025-06-30T22:00:00Z", "kommunikationsDatenBlattInaktiv": true}]}, "transaktionsdaten": {"datenaustauschreferenz": "113601", "sparte": "STROM", "pruefidentifikator": "37001", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9903790000002", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900321000005", "rollencodetyp": "BDEW"}, "dokumentennummer": "CS356455854555", "kategorie": "10", "nachrichtendatum": "2026-10-01T11:00:00Z", "nachrichtenreferenznummer": "298012", "vorgangsreferenznummer": "1", "anwendungsreferenznummer": "2"}, "zusatzdaten": {}}}, {"name": "37002", "summary": "37002 — Kommunikationsdaten des MSB Strom", "value": {"stammdaten": {"KOMMUNIKATIONSDATEN": [{"boTyp": "KOMMUNIKATIONSDATEN", "versionStruktur": "1", "gueltigkeit": "2024-06-30T22:00:00Z", "kommunikationsDatenBlattInaktiv": true}]}, "transaktionsdaten": {"datenaustauschreferenz": "113601", "sparte": "STROM", "pruefidentifikator": "37002", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9903790000002", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900321000005", "rollencodetyp": "BDEW"}, "dokumentennummer": "CS356455854555", "kategorie": "10", "nachrichtendatum": "2026-10-01T11:00:00Z", "nachrichtenreferenznummer": "298012", "vorgangsreferenznummer": "1", "anwendungsreferenznummer": "2"}, "zusatzdaten": {}}}, {"name": "13028", "summary": "13028 — Grundlage POG-Ermittlung", "value": {"stammdaten": {"ENERGIEMENGE": [{"boTyp": "ENERGIEMENGE", "versionStruktur": "1", "lokationsId": "50074561188", "lokationsTyp": "MALO", "energieverbrauch": [{"startdatum": "2025-04-01T22:00:00Z", "enddatum": "2025-04-02T22:00:00Z", "messwertstatus": "GRUNDLAGE_POG_ERMITTLUNG", "obiskennzahl": "1-1:1.9.0", "wert": 500, "position": 1}, {"startdatum": "2025-04-15T22:00:00Z", "enddatum": "2025-04-16T22:00:00Z", "messwertstatus": "GRUNDLAGE_POG_ERMITTLUNG", "obiskennzahl": "1-1:1.9.0", "wert": 750, "position": 1}, {"startdatum": "2025-04-30T22:00:00Z", "enddatum": "2025-05-01T22:00:00Z", "messwertstatus": "GRUNDLAGE_POG_ERMITTLUNG", "obiskennzahl": "1-1:1.9.0", "wert": 1000.123, "position": 2}]}]}, "transaktionsdaten": {"datenaustauschreferenz": "161201", "sparte": "STROM", "pruefidentifikator": "13028", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9900321000005", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9904446000007", "rollencodetyp": "BDEW"}, "dokumentennummer": "726947BGM", "kategorie": "Z85", "nachrichtenfunktion": "9", "nachrichtendatum": "2026-10-01T11:00:00Z", "nachrichtenreferenznummer": "726947", "typ": "EM"}, "zusatzdaten": {}}}]}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Legt im Backend einen neuen Vorgang mit den Daten der eingegangenen Nachricht an.

</li>

<li data-teil="schnittstelle" data-art="schreiben" data-abgeleitet="ja">

**Schreibende Schnittstelle**
- `37000`, `37001`, `37002`, `37003`, `37004`, `37005`, `37006`, `13028` → Vorgang angelegt — [Prozessdaten erstellen](/api/202610/backend-schreiben-nb/createprocessdata#prozessdaten-erstellen) `POST /createProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/createProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "ERSTELLEN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"KOMMUNIKATIONSDATEN\": [\n      {\n        \"boTyp\": \"KOMMUNIKATIONSDATEN\",\n        \"gueltigkeit\": \"2025-06-06T22:00:00Z\",\n        \"kommunikationsDatenBlattInaktiv\": true,\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9903790000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"anwendungsreferenznummer\": \"2\",\n    \"datenaustauschreferenz\": \"113601\",\n    \"dokumentennummer\": \"CS356455854555\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9900321000005\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"10\",\n    \"nachrichtendatum\": \"2026-10-01T11:00:00Z\",\n    \"nachrichtenreferenznummer\": \"298012\",\n    \"pruefidentifikator\": \"37000\",\n    \"sparte\": \"STROM\",\n    \"vorgangsreferenznummer\": \"1\"\n  },\n  \"zusatzdaten\": {}\n}"} examples={[{"mediaType": "application/json", "examples": [{"name": "37000", "summary": "37000 — Kommunikationsdaten des LF Strom", "value": {"stammdaten": {"KOMMUNIKATIONSDATEN": [{"boTyp": "KOMMUNIKATIONSDATEN", "versionStruktur": "1", "gueltigkeit": "2025-06-06T22:00:00Z", "kommunikationsDatenBlattInaktiv": true}]}, "transaktionsdaten": {"datenaustauschreferenz": "113601", "sparte": "STROM", "pruefidentifikator": "37000", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9903790000002", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900321000005", "rollencodetyp": "BDEW"}, "dokumentennummer": "CS356455854555", "kategorie": "10", "nachrichtendatum": "2026-10-01T11:00:00Z", "nachrichtenreferenznummer": "298012", "vorgangsreferenznummer": "1", "anwendungsreferenznummer": "2"}, "zusatzdaten": {}}}, {"name": "37001", "summary": "37001 — Kommunikationsdaten des NB Strom", "value": {"stammdaten": {"KOMMUNIKATIONSDATEN": [{"boTyp": "KOMMUNIKATIONSDATEN", "versionStruktur": "1", "gueltigkeit": "2025-06-30T22:00:00Z", "kommunikationsDatenBlattInaktiv": true}]}, "transaktionsdaten": {"datenaustauschreferenz": "113601", "sparte": "STROM", "pruefidentifikator": "37001", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9903790000002", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900321000005", "rollencodetyp": "BDEW"}, "dokumentennummer": "CS356455854555", "kategorie": "10", "nachrichtendatum": "2026-10-01T11:00:00Z", "nachrichtenreferenznummer": "298012", "vorgangsreferenznummer": "1", "anwendungsreferenznummer": "2"}, "zusatzdaten": {}}}, {"name": "37002", "summary": "37002 — Kommunikationsdaten des MSB Strom", "value": {"stammdaten": {"KOMMUNIKATIONSDATEN": [{"boTyp": "KOMMUNIKATIONSDATEN", "versionStruktur": "1", "gueltigkeit": "2024-06-30T22:00:00Z", "kommunikationsDatenBlattInaktiv": true}]}, "transaktionsdaten": {"datenaustauschreferenz": "113601", "sparte": "STROM", "pruefidentifikator": "37002", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9903790000002", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900321000005", "rollencodetyp": "BDEW"}, "dokumentennummer": "CS356455854555", "kategorie": "10", "nachrichtendatum": "2026-10-01T11:00:00Z", "nachrichtenreferenznummer": "298012", "vorgangsreferenznummer": "1", "anwendungsreferenznummer": "2"}, "zusatzdaten": {}}}, {"name": "13028", "summary": "13028 — Grundlage POG-Ermittlung", "value": {"stammdaten": {"ENERGIEMENGE": [{"boTyp": "ENERGIEMENGE", "versionStruktur": "1", "lokationsId": "50074561188", "lokationsTyp": "MALO", "energieverbrauch": [{"startdatum": "2025-04-01T22:00:00Z", "enddatum": "2025-04-02T22:00:00Z", "messwertstatus": "GRUNDLAGE_POG_ERMITTLUNG", "obiskennzahl": "1-1:1.9.0", "wert": 500, "position": 1}, {"startdatum": "2025-04-15T22:00:00Z", "enddatum": "2025-04-16T22:00:00Z", "messwertstatus": "GRUNDLAGE_POG_ERMITTLUNG", "obiskennzahl": "1-1:1.9.0", "wert": 750, "position": 1}, {"startdatum": "2025-04-30T22:00:00Z", "enddatum": "2025-05-01T22:00:00Z", "messwertstatus": "GRUNDLAGE_POG_ERMITTLUNG", "obiskennzahl": "1-1:1.9.0", "wert": 1000.123, "position": 2}]}]}, "transaktionsdaten": {"datenaustauschreferenz": "161201", "sparte": "STROM", "pruefidentifikator": "13028", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9900321000005", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9904446000007", "rollencodetyp": "BDEW"}, "dokumentennummer": "726947BGM", "kategorie": "Z85", "nachrichtenfunktion": "9", "nachrichtendatum": "2026-10-01T11:00:00Z", "nachrichtenreferenznummer": "726947", "typ": "EM"}, "zusatzdaten": {}}}]}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Legt im Backend einen neuen Vorgang mit den Daten der eingegangenen Nachricht an.

</li>

<li data-teil="lesen" data-stufe="verarbeitung">

**Daten für die Verarbeitung laden**
- [Kommunikationsdaten des Serviceanbieters lesen](/api/202610/backend-lesen/getcommunicationdatabasic#kommunikationsdaten-des-serviceanbieters-lesen) `GET /getCommunicationDataBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getCommunicationDataBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "9903790000002", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_KOMMUNIKATIONSDATEN_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

</li>

</ol>
</Stepper>

</div>

</Schritt>

<a id="abschnitt-informationen"></a>

## Prozess-Informationen

Wortlaut der Lesefassung, Steckbrief Kap. 4.1, S. 31–32.

<Stepper>
<ol>

<li data-blatt="vorbedingungen">

### Vorbedingungen

- Bei dem Marktakteur handelt es sich um keine natürliche Person.
- Bei dem sendenden Marktakteur liegen neue oder geänderte Informationen vor.
- Die EDIFACT-Kommunikation zwischen den Marktakteuren ist aufgebaut. Vor dem Aufbau der EDIFACT-Kommunikation findet eine Kontaktaufnahme bilateral statt.
- Im Falle der Privilegierung nach Energiefinanzierungsgesetz: Es handelt sich um eine verbrauchende Marktlokation.

</li>

<li data-blatt="ergebnisse">

### Ergebnisse

- Für die weitere Geschäftsbeziehung und eventuelle Clearingfälle wird auf die Informationen zurückgegriffen oder
- der Empfänger verarbeitet die übermittelten Informationen und löst ggfs. weitere Schritte (wie z.B. die Berücksichtigung der EnFG-Privilegierungsberechtigung in der Netznutzungsabrechnung) aus.

</li>

<li data-blatt="fehlerfall">

### Fehlerfall

#### Ergebnis im Fehlerfall

In den Fehlerfällen wird der Use-Case erneut gestartet und die Information übermittelt.

#### Fehlerfälle

- die Informationen enthalten einen Fehler;
- die Informationen sind nicht aktuell;
- die Informationen wurden nicht vollständig übermittelt.

</li>

<li data-blatt="anforderungen">

### Weitere Anforderungen

Dieser Use-Case wird für die Übermittlung von Informationen verwendet und beinhaltet insbesondere
- die Initialübermittlung und Aktualisierung von Kontaktdaten:
  - Bei einer Aktualisierung werden alle Kommunikationsdaten des sendenden Marktakteurs an den empfangenden Marktakteur übermittelt.
  - Die Kommunikationsdaten sind eindeutig zu versionieren. Es ist die aktuelle Versionskennzeichnung, der Gültigkeitsbeginn und die Kennzeichnung der Vorgängerversion anzugeben. Ausnahme: Bei der Initialbefüllung ist kein Gültigkeitsbeginn anzugeben, da die Kommunikationsdaten ab sofort gelten. Des Weiteren ist bei der Initialbefüllung keine Vorgängerversion anzugeben.
  - Die Gültigkeit von Kommunikationsdaten endet mit der Übermittlung der Kommunikationsdaten mit identischem Gültigkeitsbeginn und einer höheren Versionskennzeichnung oder mit dem Inkrafttreten von Kommunikationsdaten mit einem späteren Gültigkeitsbeginn und einer höheren Versionskennzeichnung oder durch Übermittlung des Kennzeichens "inaktiv" für die Kommunikationsdaten. Kommunikationsdaten beginnen und enden immer zu 00:00 Uhr eines Kalendertages.
  - Die erste Kontaktaufnahme zwischen den Marktakteuren, d.h. vor Aufbau einer EDIFACT-Beziehung, erfolgt bilateral.
  - Ist der Letztverbraucher selbst Netznutzer (= Netznutzer ohne All-Inklusiv-Vertrag), so tritt er in die Rolle des LF i. S. dieser Prozessbeschreibung, soweit diese Regelungen sinngemäß auf ihn anwendbar sind.
- und die Übermittlung der Privilegierung nach dem Energiefinanzierungsgesetz durch den LF an den NB:
  - Bei Änderung der EnFG-Privilegierungsberechtigung in die Vergangenheit wird ggf. eine Rechnungskorrektur notwendig, wenn der Zeitraum einer Rechnung betroffen ist.

</li>

<li data-blatt="erste-nachricht">

### Erste Nachricht

**LF** sendet „Information“ (Schritt 1). Ab hier ist der Beteiligte dieser Seite am Zug.

</li>

<li data-blatt="ziel">

### Ziel

Dem empfangenden Marktakteur liegen die gültigen Informationen des sendenden Marktakteurs vollständig vor.

</li>

</ol>
</Stepper>

<a id="abschnitt-sichten"></a>

## Andere Sichten des Prozesses

Derselbe Prozess, aus den Augen der anderen Beteiligten: dieselben Schritte, jeweils aus deren Sicht gelesen.

- [Sicht LF](/prozessdoku/202610/LF/GPKE-Teil4-uebermittlung-von-informationen) — LF

<Hinweisbereich>

*Die Schritte sind die **möglichen** Nachrichten dieses Prozesses, keine Abfolge — die Quelle führt weder Bedingungen noch Alternativen. Das Kästchen am Schritt nennt links die eigene Sicht: **←** empfängt sie, **→** sendet sie. Zugeklappte Schritte laufen zwischen anderen Marktpartnern.*

Die Konnektortabelle führt für diese Schritte keinen Schreibaufruf. Abgeleitet aus dem Prozessverlauf: Mit ihrer Nachricht beginnt der Prozess für die eigene Rolle, der Vorgang entsteht also neu.

Betrifft: [1](#schritt-1)

</Hinweisbereich>
