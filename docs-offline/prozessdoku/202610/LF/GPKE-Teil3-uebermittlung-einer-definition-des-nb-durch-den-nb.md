# Übermittlung einer Definition des NB durch den NB — Sicht LF

<Kopf rolle="LF" beteiligter="LF" festlegung="GPKE" dokument="GPKE Teil 3" kapitel="1.2.3.2" sparte="Strom" schritte={2} suchtitel="Übermittlung einer Definition des NB durch den NB — Sicht LF · GPKE Teil 3 · Formatversion 202610" abschnitte={[{"id": "abschnitt-ablauf", "label": "Prozessablauf"}, {"id": "abschnitt-schritte", "label": "Prozessschritte"}, {"id": "abschnitt-informationen", "label": "Prozess-Informationen"}, {"id": "abschnitt-sichten", "label": "Andere Sichten des Prozesses"}]} />

<Kurzfassung>

Alle LF und MSB erhalten immer die aktuellen
- Zählzeitdefinitionen des NB bzw.
- Schaltzeitdefinitionen des NB bzw.
- Leistungskurvendefinitionen des NB. Ändert sich eine Definition des NB, wird diese an die LF und MSB übermittelt.

</Kurzfassung>

<a id="abschnitt-ablauf"></a>

## Prozessablauf aus Sicht des LF

<Systembild svg={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1004 453\" width=\"1004\" height=\"453\" role=\"img\" aria-labelledby=\"sb-title\" class=\"maco-systembild\">\n<title id=\"sb-title\">Systembild: Übermittlung einer Definition des NB durch den NB aus Sicht LF</title>\n<defs><marker id=\"sb-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect class=\"sb-lane-kopf\" x=\"16\" y=\"12\" width=\"232\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend-System des Kunden</text>\n<rect class=\"sb-lane-kopf\" x=\"398\" y=\"12\" width=\"264\" height=\"46\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · LF</text>\n<rect class=\"sb-lane-kopf\" x=\"812\" y=\"12\" width=\"176\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"900\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Marktpartner</text>\n<line x1=\"323\" y1=\"58\" x2=\"323\" y2=\"441\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"737\" y1=\"58\" x2=\"737\" y2=\"441\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"80\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">1. Definition des NB</text>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"78\" r=\"5\"/><line x1=\"900\" y1=\"83\" x2=\"900\" y2=\"95\"/><line x1=\"893\" y1=\"87\" x2=\"907\" y2=\"87\"/><line x1=\"900\" y1=\"95\" x2=\"894\" y2=\"105\"/><line x1=\"900\" y1=\"95\" x2=\"906\" y2=\"105\"/></g>\n<text x=\"900\" y=\"127\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"878\" y1=\"96\" x2=\"628\" y2=\"96\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"88\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"112\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">25005, 25008, 25009</text>\n<rect class=\"sb-kasten sb-aperak_lesen\" x=\"432\" y=\"163\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"183\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Daten für die</text>\n<text x=\"530\" y=\"198\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Eingangsprüfung laden</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"113\" x2=\"530\" y2=\"163\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-aperak_lesen\" x=\"34\" y=\"163\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"183\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">3 Lese-Schnittstellen</text>\n<text x=\"132\" y=\"198\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">aufgerufen</text>\n<line x1=\"432\" y1=\"187\" x2=\"230\" y2=\"187\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"179\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<text x=\"331\" y=\"203\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">je einzeln am Schritt</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"237\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"257\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z10</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"211\" x2=\"530\" y2=\"237\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-schreiben\" x=\"432\" y=\"301\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"321\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"270\" x2=\"530\" y2=\"301\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-schreiben\" x=\"34\" y=\"301\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"321\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten erstellen</text>\n<line x1=\"432\" y1=\"317\" x2=\"230\" y2=\"317\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"309\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<text x=\"331\" y=\"333\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">referenzAufAnfragenachricht = null</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"365\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"385\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"334\" x2=\"530\" y2=\"365\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"365\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"385\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"381\" x2=\"230\" y2=\"381\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"373\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<text x=\"331\" y=\"397\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">referenzAufAnfragenachricht != null</text>\n</svg>"} gesamt={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 974 362\" width=\"974\" height=\"362\" role=\"img\" aria-labelledby=\"sd-title\" class=\"maco-sequence\">\n<title id=\"sd-title\">Sequenzdiagramm: Übermittlung einer Definition des NB durch den NB aus Sicht LF</title>\n<defs><marker id=\"sd-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect x=\"16\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"121\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend (Kunde)</text>\n<line x1=\"121\" y1=\"64\" x2=\"121\" y2=\"350\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"260\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"365\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · LF</text>\n<line x1=\"365\" y1=\"64\" x2=\"365\" y2=\"350\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"504\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"609\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"609\" y1=\"64\" x2=\"609\" y2=\"350\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"748\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"853\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">MSB</text>\n<line x1=\"853\" y1=\"64\" x2=\"853\" y2=\"350\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"609\" y1=\"90\" x2=\"365\" y2=\"90\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"81\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">1. Definition des NB</text>\n<text x=\"487\" y=\"105\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 25005, 25008, 25009</text>\n<line x1=\"365\" y1=\"152\" x2=\"121\" y2=\"152\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"143\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<text x=\"243\" y=\"167\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten erstellen · referenzAufAnfragenachricht = null</text>\n<line x1=\"365\" y1=\"214\" x2=\"121\" y2=\"214\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"205\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"229\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren · referenzAufAnfragenachricht != null</text>\n<line x1=\"609\" y1=\"276\" x2=\"853\" y2=\"276\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"731\" y=\"267\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">2. Definition des NB</text>\n<text x=\"731\" y=\"291\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 25009, 25005, 25008</text>\n</svg>"} titel="LF" />

<a id="abschnitt-schritte"></a>

## Prozessschritte

<Schritt nr="1" anker="schritt-1" richtung="eingehend" kopf={{"links": {"label": "LF", "eigen": true}, "rechts": {"label": "NB"}}}>

### Definition des NB

<Schrittskizze sicht={{"label": "LF"}} zeilen={[{"art": "empfangen", "label": "NB", "weg": "AS4", "nachrichten": [{"nr": "25005", "titel": "Übermittlung einer ausgerollten Zählzeitdefinition"}, {"nr": "25008", "titel": "Übermittlung einer ausgerollten Schaltzeitdefinition"}, {"nr": "25009", "titel": "Übermittlung einer ausgerollten Leistungskurvendefinition"}]}, {"art": "lesen_aperak", "schnittstellen": [{"label": "Zaehlzeitdefinition lesen"}, {"label": "Schaltzeitdefinition lesen"}, {"label": "Leistungskurvendefinition lesen"}]}, {"art": "aperak", "werte": ["Z10"]}, {"art": "erstellen", "bedingung": "referenzAufAnfragenachricht = null"}, {"art": "fortschreiben", "bedingung": "referenzAufAnfragenachricht != null"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [25005](/schnittstellen/202610/pruefi/UTILTS/PI_25005) — Übermittlung einer ausgerollten Zählzeitdefinition · AS4
- [25008](/schnittstellen/202610/pruefi/UTILTS/PI_25008) — Übermittlung einer ausgerollten Schaltzeitdefinition · AS4
- [25009](/schnittstellen/202610/pruefi/UTILTS/PI_25009) — Übermittlung einer ausgerollten Leistungskurvendefinition · AS4

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
- [Zaehlzeitdefinition lesen ](/api/202610/backend-lesen/getdefinitioncounting#zaehlzeitdefinition-lesen) `GET /getDefinitionCounting` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getDefinitionCounting"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": false, "defaultValue": "MALO", "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": false, "defaultValue": "2024-06-28T12:18:00Z", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Schaltzeitdefinition lesen](/api/202610/backend-lesen/getdefinitionswitch#schaltzeitdefinition-lesen) `GET /getDefinitionSwitch` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getDefinitionSwitch"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": false, "defaultValue": "MALO", "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": false, "defaultValue": "2024-06-28T12:18:00Z", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Leistungskurvendefinition lesen](/api/202610/backend-lesen/getdefinitionperformance#leistungskurvendefinition-lesen) `GET /getDefinitionPerformance` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getDefinitionPerformance"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": false, "defaultValue": "MALO", "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": false, "defaultValue": "2024-06-28T12:18:00Z", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

</li>

<li data-teil="aperak">

**Aperak-Prüfungen**
- `25005`, `25008`, `25009` → `Z10` — Aperak Prüfung: Ist Lokation bekannt ?

</li>

<li data-teil="schnittstelle" data-art="schreiben">

**Schreibende Schnittstelle**
- `referenzAufAnfragenachricht = null` → Vorgang angelegt — [Prozessdaten erstellen](/api/202610/backend-schreiben-lf/createprocessdata#prozessdaten-erstellen) `POST /createProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/createProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": false, "defaultValue": "ERSTELLEN_PROZESSDATEN", "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"ZAEHLZEITDEFINITION\": [\n      {\n        \"beginndatum\": \"2023-12-31T23:00:00Z\",\n        \"boTyp\": \"ZAEHLZEITDEFINITION\",\n        \"code\": \"AAL\",\n        \"endedatum\": \"2024-12-31T23:00:00Z\",\n        \"version\": \"2024-08-01T17:15:46Z\",\n        \"versionStruktur\": \"1\",\n        \"zaehlzeiten\": [\n          {\n            \"aenderungszeitpunkt\": \"2024-08-14T22:00:00Z\",\n            \"haeufigkeit\": \"JAEHRLICH\",\n            \"register\": \"AAL\"\n          }\n        ]\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9900259000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"datenaustauschreferenz\": \"M07FXHJ3\",\n    \"dokumentennummer\": \"LZWFSX5B\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9903111000003\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"Z59\",\n    \"nachrichtendatum\": \"2026-10-01T11:00:00Z\",\n    \"nachrichtenreferenznummer\": \"M0N5UZ83\",\n    \"pruefidentifikator\": \"25005\",\n    \"sparte\": \"STROM\",\n    \"vorgangsnummer\": \"Vorgang7\"\n  },\n  \"zusatzdaten\": {}\n}"} examples={[{"mediaType": "application/json", "examples": [{"name": "25005", "summary": "25005 — Übermittlung einer ausgerollten Zählzeitdefinition", "value": {"stammdaten": {"ZAEHLZEITDEFINITION": [{"boTyp": "ZAEHLZEITDEFINITION", "versionStruktur": "1", "code": "AAL", "beginndatum": "2023-12-31T23:00:00Z", "endedatum": "2024-12-31T23:00:00Z", "version": "2024-08-01T17:15:46Z", "zaehlzeiten": [{"aenderungszeitpunkt": "2024-08-14T22:00:00Z", "haeufigkeit": "JAEHRLICH", "register": "AAL"}]}]}, "transaktionsdaten": {"datenaustauschreferenz": "M07FXHJ3", "sparte": "STROM", "vorgangsnummer": "Vorgang7", "pruefidentifikator": "25005", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9900259000002", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9903111000003", "rollencodetyp": "BDEW"}, "dokumentennummer": "LZWFSX5B", "kategorie": "Z59", "nachrichtendatum": "2026-10-01T11:00:00Z", "nachrichtenreferenznummer": "M0N5UZ83"}, "zusatzdaten": {}}}, {"name": "25008", "summary": "25008 — Übermittlung einer ausgerollten Schaltzeitdefinition", "value": {"stammdaten": {"SCHALTZEITDEFINITION": [{"boTyp": "SCHALTZEITDEFINITION", "versionStruktur": "1", "code": "ZZ1", "beginndatum": "2023-07-31T23:00:00Z", "endedatum": "2024-12-31T23:00:00Z", "version": "2024-08-08T05:30:44Z", "schaltzeiten": [{"aenderungszeitpunkt": "2024-10-14T05:30:00Z", "schalthandlung": "LEISTUNG_AN"}]}]}, "transaktionsdaten": {"datenaustauschreferenz": "M0FVEWKW", "sparte": "STROM", "vorgangsnummer": "Vorgang12", "pruefidentifikator": "25008", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9900259000002", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9904629000006", "rollencodetyp": "BDEW"}, "dokumentennummer": "M00U0AH4", "kategorie": "Z80", "nachrichtendatum": "2026-10-01T11:00:00Z", "nachrichtenreferenznummer": "M05E0LJJ"}, "zusatzdaten": {}}}, {"name": "25009", "summary": "25009 — Übermittlung einer ausgerollten Leistungskurvendefinition", "value": {"stammdaten": {"LEISTUNGSKURVENDEFINITION": [{"boTyp": "LEISTUNGSKURVENDEFINITION", "versionStruktur": "1", "code": "AL", "beginndatum": "2023-12-31T23:00:00Z", "endedatum": "2024-12-31T23:00:00Z", "version": "2024-08-01T13:45:18Z", "leistungskurven": [{"aenderungszeitpunkt": "2024-12-14T23:00:00Z", "haeufigkeit": "JAEHRLICH", "schwellwert": {"obererSchwellwert": 20}}]}]}, "transaktionsdaten": {"datenaustauschreferenz": "M0GA80AJ", "sparte": "STROM", "vorgangsnummer": "Vorgang6", "pruefidentifikator": "25009", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9900259000002", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9903111000003", "rollencodetyp": "BDEW"}, "dokumentennummer": "M0B9Z35W", "kategorie": "Z81", "nachrichtendatum": "2026-10-01T11:00:00Z", "nachrichtenreferenznummer": "M0291ML2"}, "zusatzdaten": {}}}]}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Legt im Backend einen neuen Vorgang mit den Daten der eingegangenen Nachricht an.

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- `referenzAufAnfragenachricht != null` → Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202610/backend-schreiben-lf/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": false, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"ZAEHLZEITDEFINITION\": [\n      {\n        \"beginndatum\": \"2023-12-31T23:00:00Z\",\n        \"boTyp\": \"ZAEHLZEITDEFINITION\",\n        \"code\": \"AAL\",\n        \"endedatum\": \"2024-12-31T23:00:00Z\",\n        \"version\": \"2024-08-01T17:15:46Z\",\n        \"versionStruktur\": \"1\",\n        \"zaehlzeiten\": [\n          {\n            \"aenderungszeitpunkt\": \"2024-08-14T22:00:00Z\",\n            \"haeufigkeit\": \"JAEHRLICH\",\n            \"register\": \"AAL\"\n          }\n        ]\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9900259000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"datenaustauschreferenz\": \"M07FXHJ3\",\n    \"dokumentennummer\": \"LZWFSX5B\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9903111000003\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"Z59\",\n    \"nachrichtendatum\": \"2026-10-01T11:00:00Z\",\n    \"nachrichtenreferenznummer\": \"M0N5UZ83\",\n    \"pruefidentifikator\": \"25005\",\n    \"sparte\": \"STROM\",\n    \"vorgangsnummer\": \"Vorgang7\"\n  },\n  \"zusatzdaten\": {}\n}"} examples={[{"mediaType": "application/json", "examples": [{"name": "25005", "summary": "25005 — Übermittlung einer ausgerollten Zählzeitdefinition", "value": {"stammdaten": {"ZAEHLZEITDEFINITION": [{"boTyp": "ZAEHLZEITDEFINITION", "versionStruktur": "1", "code": "AAL", "beginndatum": "2023-12-31T23:00:00Z", "endedatum": "2024-12-31T23:00:00Z", "version": "2024-08-01T17:15:46Z", "zaehlzeiten": [{"aenderungszeitpunkt": "2024-08-14T22:00:00Z", "haeufigkeit": "JAEHRLICH", "register": "AAL"}]}]}, "transaktionsdaten": {"datenaustauschreferenz": "M07FXHJ3", "sparte": "STROM", "vorgangsnummer": "Vorgang7", "pruefidentifikator": "25005", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9900259000002", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9903111000003", "rollencodetyp": "BDEW"}, "dokumentennummer": "LZWFSX5B", "kategorie": "Z59", "nachrichtendatum": "2026-10-01T11:00:00Z", "nachrichtenreferenznummer": "M0N5UZ83"}, "zusatzdaten": {}}}, {"name": "25008", "summary": "25008 — Übermittlung einer ausgerollten Schaltzeitdefinition", "value": {"stammdaten": {"SCHALTZEITDEFINITION": [{"boTyp": "SCHALTZEITDEFINITION", "versionStruktur": "1", "code": "ZZ1", "beginndatum": "2023-07-31T23:00:00Z", "endedatum": "2024-12-31T23:00:00Z", "version": "2024-08-08T05:30:44Z", "schaltzeiten": [{"aenderungszeitpunkt": "2024-10-14T05:30:00Z", "schalthandlung": "LEISTUNG_AN"}]}]}, "transaktionsdaten": {"datenaustauschreferenz": "M0FVEWKW", "sparte": "STROM", "vorgangsnummer": "Vorgang12", "pruefidentifikator": "25008", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9900259000002", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9904629000006", "rollencodetyp": "BDEW"}, "dokumentennummer": "M00U0AH4", "kategorie": "Z80", "nachrichtendatum": "2026-10-01T11:00:00Z", "nachrichtenreferenznummer": "M05E0LJJ"}, "zusatzdaten": {}}}, {"name": "25009", "summary": "25009 — Übermittlung einer ausgerollten Leistungskurvendefinition", "value": {"stammdaten": {"LEISTUNGSKURVENDEFINITION": [{"boTyp": "LEISTUNGSKURVENDEFINITION", "versionStruktur": "1", "code": "AL", "beginndatum": "2023-12-31T23:00:00Z", "endedatum": "2024-12-31T23:00:00Z", "version": "2024-08-01T13:45:18Z", "leistungskurven": [{"aenderungszeitpunkt": "2024-12-14T23:00:00Z", "haeufigkeit": "JAEHRLICH", "schwellwert": {"obererSchwellwert": 20}}]}]}, "transaktionsdaten": {"datenaustauschreferenz": "M0GA80AJ", "sparte": "STROM", "vorgangsnummer": "Vorgang6", "pruefidentifikator": "25009", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9900259000002", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9903111000003", "rollencodetyp": "BDEW"}, "dokumentennummer": "M0B9Z35W", "kategorie": "Z81", "nachrichtendatum": "2026-10-01T11:00:00Z", "nachrichtenreferenznummer": "M0291ML2"}, "zusatzdaten": {}}}]}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend mit den Daten der eingegangenen Nachricht fort.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="2" anker="schritt-2" richtung="fremd" kopf={{"links": {"label": "NB", "eigen": false}, "rechts": {"label": "MSB"}}}>

### Definition des NB

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [25009](/schnittstellen/202610/pruefi/UTILTS/PI_25009) — Übermittlung einer ausgerollten Leistungskurvendefinition · AS4
- [25005](/schnittstellen/202610/pruefi/UTILTS/PI_25005) — Übermittlung einer ausgerollten Zählzeitdefinition · AS4
- [25008](/schnittstellen/202610/pruefi/UTILTS/PI_25008) — Übermittlung einer ausgerollten Schaltzeitdefinition · AS4

</div>

</Schritt>

<a id="abschnitt-informationen"></a>

## Prozess-Informationen

Wortlaut der Lesefassung, Steckbrief Kap. 1.2.3.1, S. 13–14.

<Stepper>
<ol>

<li data-blatt="vorbedingungen">

### Vorbedingungen

- Die
  - Übersicht der Zählzeitdefinition des NB bzw.
  - Übersicht der Schaltzeitdefinitionen des NB bzw.
  - Übersicht der Leistungskurvendefinitionen des NB liegt den LF und MSB vor.

</li>

<li data-blatt="ergebnisse">

### Ergebnisse

- Der LF kann eine einer Lokation zugeordnete Definition nachvollziehen (z.B. kann der LF eine einer Marktlokation zugeordnete Zählzeitdefinition des NB nachvollziehen).
- Der MSB kann eine Konfiguration, für die eine Definition erforderlich ist, für eine Lokation einrichten.
- Im Fall der Bestellung einer Konfiguration, für die eine Definition erforderlich ist:
  - Der LF kann den Use-Case „[Bestellung einer Konfiguration vom LF an NB](/prozessdoku/202610/LF/GPKE-Teil3-bestellung-einer-konfiguration-vom-lf-an-nb)“ durchführen (z.B. für die Bestellung einer Konfiguration, für die eine Zählzeitdefinition des NB erforderlich ist).
  - Der NB kann den Use-Case „Bestellung einer Konfiguration vom NB oder LF an MSB“ durchführen (z.B. für die Bestellung einer Konfiguration für die eine Zählzeitdefinition des NB erforderlich ist).

</li>

<li data-blatt="anforderungen">

### Weitere Anforderungen

- Der NB übermittelt für jeden Zeitraum Definitionen mit der höchsten Versionsnummer.
- Für einen Zeitraum ist die Definition mit der höchsten Versionsnummer gültig.
- Bei der erstmaligen Versendung sind alle genutzten Definitionen in der jeweils gültigen Version zu versenden. Dies gilt auch, wenn diese auf die Folgejahre erstmalig ausgerollt werden.
- Die Definition des NB ist immer für ein komplettes Kalenderjahr anzugeben. Bei Korrekturen ist nur die korrigierte Definition für das gesamte Kalenderjahr zu versenden.
- Im Fall der Zählzeitdefinition des NB:
  - Eine Zählzeitdefinition des NB ist vom NB auch an den Letztverbraucher in seiner Rolle als LF zu übermitteln, wenn im Rahmen der Netznutzungsabrechnung der Letztverbraucher in die Rolle des LF tritt, soweit diese Regelungen sinngemäß auf ihn anwendbar sind.
  - Wird dem MSB im Rahmen der Mindestparameter im Use-Case „[Beginn Messstellenbetrieb](/prozessdoku/202610/LF/WiM-Teil1-beginn-messstellenbetrieb)“ (WiM Teil 1) eine Zählzeitdefinition des NB mitgeteilt, die der MSB vorab nicht über den Use-Case „Übermittlung einer Definition des NB durch den NB“ übermittelt bekommen hat, so ist die Energie in einem Register an der/den Messlokation(en) und zugehörigen Marktlokation für den Zählzeitenanwendungszweck „Netznutzung“ zu erfassen.

</li>

<li data-blatt="anlass">

### Anlass

- Eine bereits übermittelte Definition hat sich geändert oder
- eine Definition ist in der dazugehörigen Übersicht neu hinzugekommen oder
- der NB hat für das Folgejahr Definitionen erstellt.

**Vorher läuft:** [Reklamation einer Definition des NB vom LF an NB](/prozessdoku/202610/LF/GPKE-Teil3-reklamation-einer-definition-des-nb-vom-lf-an-nb), [Reklamation einer Definition des NB vom MSB an NB](/prozessdoku/202610/MSB/GPKE-Teil3-reklamation-einer-definition-des-nb-vom-msb-an-nb), [Übermittlung der Übersicht der Definitionen des NB durch den NB](/prozessdoku/202610/LF/GPKE-Teil3-uebermittlung-der-uebersicht-der-definitionen-des-nb-durch-den-nb) — diese Prozesse nennen den hier gezeigten in ihrem Ergebnis.

</li>

<li data-blatt="erste-nachricht">

### Erste Nachricht

**NB** sendet „Definition des NB“ (Schritt 1). Ab hier ist der Beteiligte dieser Seite am Zug.

</li>

<li data-blatt="ziel">

### Ziel

Die LF und MSB kennen die
- Zählzeitdefinitionen des NB bzw.
- Schaltzeitdefinitionen des NB bzw.
- Leistungskurvendefinitionen des NB

</li>

</ol>
</Stepper>

<a id="abschnitt-sichten"></a>

## Andere Sichten des Prozesses

Derselbe Prozess, aus den Augen der anderen Beteiligten: dieselben Schritte, jeweils aus deren Sicht gelesen.

- [Sicht NB](/prozessdoku/202610/NB/GPKE-Teil3-uebermittlung-einer-definition-des-nb-durch-den-nb) — NB
- [Sicht MSB](/prozessdoku/202610/MSB/GPKE-Teil3-uebermittlung-einer-definition-des-nb-durch-den-nb) — MSB

<Hinweisbereich>

*Die Schritte sind die **möglichen** Nachrichten dieses Prozesses, keine Abfolge — die Quelle führt weder Bedingungen noch Alternativen. Das Kästchen am Schritt nennt links die eigene Sicht: **←** empfängt sie, **→** sendet sie. Zugeklappte Schritte laufen zwischen anderen Marktpartnern.*

</Hinweisbereich>
