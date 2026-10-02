# Übermittlung der Übersicht der Definitionen des NB durch den NB — Sicht LF

<Kopf rolle="LF" beteiligter="LF" festlegung="GPKE" dokument="GPKE Teil 3" kapitel="1.2.1.2" sparte="Strom" schritte={2} suchtitel="Übermittlung der Übersicht der Definitionen des NB durch den NB — Sicht LF · GPKE Teil 3 · Formatversion 202604" abschnitte={[{"id": "abschnitt-ablauf", "label": "Prozessablauf"}, {"id": "abschnitt-schritte", "label": "Prozessschritte"}, {"id": "abschnitt-informationen", "label": "Prozess-Informationen"}, {"id": "abschnitt-sichten", "label": "Andere Sichten des Prozesses"}]} />

<Kurzfassung>

Der NB versendet
- die Übersicht der Zählzeitdefinitionen des NB, die alle vom NB verwendeten Zählzeitdefinitionen des NB enthält, bzw.
- die Übersicht der Schaltzeitdefinitionen des NB, die alle vom NB verwendeten Schaltzeitdefinitionen des NB enthält bzw.
- die Übersicht der Leistungskurvendefinitionen des NB, die alle vom NB verwendeten Leistungskurvendefinitionen des NB enthält, an alle LF und MSB. Bei Änderung der Übersicht (z.B. bei der Übersicht der Zählzeitdefinitionen des NB kommen Zählzeitdefinitionen des NB hinzu oder entfallen Zählzeitdefinitionen des NB) wird die aktualisierte Übersicht an alle LF und MSB versendet.

</Kurzfassung>

<a id="abschnitt-ablauf"></a>

## Prozessablauf aus Sicht des LF

<Systembild svg={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1004 389\" width=\"1004\" height=\"389\" role=\"img\" aria-labelledby=\"sb-title\" class=\"maco-systembild\">\n<title id=\"sb-title\">Systembild: Übermittlung der Übersicht der Definitionen des NB durch den NB aus Sicht LF</title>\n<defs><marker id=\"sb-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect class=\"sb-lane-kopf\" x=\"16\" y=\"12\" width=\"232\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend-System des Kunden</text>\n<rect class=\"sb-lane-kopf\" x=\"398\" y=\"12\" width=\"264\" height=\"46\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · LF</text>\n<rect class=\"sb-lane-kopf\" x=\"812\" y=\"12\" width=\"176\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"900\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Marktpartner</text>\n<line x1=\"323\" y1=\"58\" x2=\"323\" y2=\"377\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"737\" y1=\"58\" x2=\"737\" y2=\"377\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"80\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">1. Übersicht der Definitionen</text>\n<text x=\"530\" y=\"115\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">des NB</text>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"86\" r=\"5\"/><line x1=\"900\" y1=\"91\" x2=\"900\" y2=\"103\"/><line x1=\"893\" y1=\"95\" x2=\"907\" y2=\"95\"/><line x1=\"900\" y1=\"103\" x2=\"894\" y2=\"113\"/><line x1=\"900\" y1=\"103\" x2=\"906\" y2=\"113\"/></g>\n<text x=\"900\" y=\"135\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"878\" y1=\"104\" x2=\"628\" y2=\"104\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"96\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"120\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">25004, 25006, 25007</text>\n<rect class=\"sb-kasten sb-schreiben\" x=\"432\" y=\"163\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"183\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"128\" x2=\"530\" y2=\"163\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-schreiben\" x=\"34\" y=\"163\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"183\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten erstellen</text>\n<line x1=\"432\" y1=\"179\" x2=\"230\" y2=\"179\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"171\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<text x=\"331\" y=\"195\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">referenzAufAnfragenachricht = null</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"227\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"247\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"196\" x2=\"530\" y2=\"227\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"227\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"247\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"243\" x2=\"230\" y2=\"243\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"235\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<text x=\"331\" y=\"259\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">referenzAufAnfragenachricht != null</text>\n<rect class=\"sb-kasten sb-lesen_verarbeitung\" x=\"432\" y=\"291\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"311\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Daten für die Verarbeitung</text>\n<text x=\"530\" y=\"326\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">laden</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"260\" x2=\"530\" y2=\"291\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-lesen_verarbeitung\" x=\"34\" y=\"291\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"311\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">LESEN_BERECHNUNGSFORM</text>\n<text x=\"132\" y=\"326\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">EL_BASIS</text>\n<line x1=\"432\" y1=\"315\" x2=\"230\" y2=\"315\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"307\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n</svg>"} gesamt={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 974 362\" width=\"974\" height=\"362\" role=\"img\" aria-labelledby=\"sd-title\" class=\"maco-sequence\">\n<title id=\"sd-title\">Sequenzdiagramm: Übermittlung der Übersicht der Definitionen des NB durch den NB aus Sicht LF</title>\n<defs><marker id=\"sd-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect x=\"16\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"121\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend (Kunde)</text>\n<line x1=\"121\" y1=\"64\" x2=\"121\" y2=\"350\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"260\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"365\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · LF</text>\n<line x1=\"365\" y1=\"64\" x2=\"365\" y2=\"350\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"504\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"609\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"609\" y1=\"64\" x2=\"609\" y2=\"350\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"748\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"853\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">MSB</text>\n<line x1=\"853\" y1=\"64\" x2=\"853\" y2=\"350\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"609\" y1=\"90\" x2=\"365\" y2=\"90\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"81\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">1. Übersicht der Definitionen des NB</text>\n<text x=\"487\" y=\"105\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 25004, 25006, 25007</text>\n<line x1=\"365\" y1=\"152\" x2=\"121\" y2=\"152\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"143\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<text x=\"243\" y=\"167\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten erstellen · referenzAufAnfragenachricht = null</text>\n<line x1=\"365\" y1=\"214\" x2=\"121\" y2=\"214\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"205\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"229\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren · referenzAufAnfragenachricht != null</text>\n<line x1=\"609\" y1=\"276\" x2=\"853\" y2=\"276\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"731\" y=\"267\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">2. Übersicht der Definitionen des NB</text>\n<text x=\"731\" y=\"291\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 25006, 25007, 25004</text>\n</svg>"} titel="LF" />

<a id="abschnitt-schritte"></a>

## Prozessschritte

<Schritt nr="1" anker="schritt-1" richtung="eingehend" kopf={{"links": {"label": "LF", "eigen": true}, "rechts": {"label": "NB"}}}>

### Übersicht der Definitionen des NB

<Schrittskizze sicht={{"label": "LF"}} zeilen={[{"art": "empfangen", "label": "NB", "weg": "AS4", "nachrichten": [{"nr": "25004", "titel": "Übermittlung Übersicht Zählzeitdefinitionen"}, {"nr": "25006", "titel": "Übermittlung Übersicht Schaltzeitdefinitionen"}, {"nr": "25007", "titel": "Übermittlung Übersicht Leistungskurvendefinitionen"}]}, {"art": "erstellen", "bedingung": "referenzAufAnfragenachricht = null"}, {"art": "fortschreiben", "bedingung": "referenzAufAnfragenachricht != null"}, {"art": "lesen_verarbeitung", "schnittstellen": [{"label": "LESEN_BERECHNUNGSFORMEL_BASIS"}]}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [25004](/schnittstellen/202604/pruefi/UTILTS/PI_25004) — Übermittlung Übersicht Zählzeitdefinitionen · AS4
- [25006](/schnittstellen/202604/pruefi/UTILTS/PI_25006) — Übermittlung Übersicht Schaltzeitdefinitionen · AS4
- [25007](/schnittstellen/202604/pruefi/UTILTS/PI_25007) — Übermittlung Übersicht Leistungskurvendefinitionen · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **NB** · AS4

</li>

<li data-teil="schnittstelle" data-art="schreiben">

**Schreibende Schnittstelle**
- `referenzAufAnfragenachricht = null` → Vorgang angelegt — [Prozessdaten erstellen](/api/202604/backend-schreiben-lf/createprocessdata#prozessdaten-erstellen) `POST /createProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/createProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": false, "defaultValue": "ERSTELLEN_PROZESSDATEN", "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"ZAEHLZEITDEFINITION\": [\n      {\n        \"beginndatum\": \"2024-09-27T22:00:00Z\",\n        \"boTyp\": \"ZAEHLZEITDEFINITION\",\n        \"notwendigkeit\": \"DEFINITIONEN_WERDEN_VERWENDET\",\n        \"version\": \"2024-09-28T13:30:15Z\",\n        \"versionStruktur\": \"1\",\n        \"zaehlzeiten\": [\n          {\n            \"code\": \"AL\",\n            \"ermittlungLeistungsmaximum\": \"KEINE_VERWENDUNG_HOCHLASTFENSTER\",\n            \"haeufigkeit\": \"EINMALIG\",\n            \"istBestellbar\": true,\n            \"typ\": \"WAERMEPUMPE\",\n            \"uebermittelbarkeit\": \"ELEKTRONISCH\"\n          }\n        ],\n        \"zaehlzeitregister\": [\n          {\n            \"register\": \"AL\",\n            \"schwachlastfaehig\": \"SCHWACHLASTFAEHIG\",\n            \"zaehlzeitDefinition\": \"AL\"\n          }\n        ]\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"ansprechpartner\": {\n        \"boTyp\": \"ANSPRECHPARTNER\",\n        \"eMailAdresse\": \"marktpartner@stromnetz-hamburg.de\",\n        \"nachname\": \"Andre Laue\",\n        \"versionStruktur\": \"1\"\n      },\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"marktrolle\": \"NB\",\n      \"rollencodenummer\": \"9900259000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"datenaustauschreferenz\": \"LZWDBZDB\",\n    \"dokumentennummer\": \"M0FLEUCL\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"marktrolle\": \"LF\",\n      \"rollencodenummer\": \"9903111000003\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"Z60\",\n    \"nachrichtendatum\": \"2024-08-13T13:38:00Z\",\n    \"nachrichtenreferenznummer\": \"LZYNBYE1\",\n    \"pruefidentifikator\": \"25004\",\n    \"sparte\": \"STROM\",\n    \"vorgangsnummer\": \"Vorgang3\"\n  },\n  \"zusatzdaten\": {}\n}"} examples={[{"mediaType": "application/json", "examples": [{"name": "25004", "summary": "25004 — Übermittlung Übersicht Zählzeitdefinitionen", "value": {"stammdaten": {"ZAEHLZEITDEFINITION": [{"boTyp": "ZAEHLZEITDEFINITION", "versionStruktur": "1", "beginndatum": "2024-09-27T22:00:00Z", "version": "2024-09-28T13:30:15Z", "notwendigkeit": "DEFINITIONEN_WERDEN_VERWENDET", "zaehlzeiten": [{"code": "AL", "haeufigkeit": "EINMALIG", "uebermittelbarkeit": "ELEKTRONISCH", "ermittlungLeistungsmaximum": "KEINE_VERWENDUNG_HOCHLASTFENSTER", "istBestellbar": true, "typ": "WAERMEPUMPE"}], "zaehlzeitregister": [{"zaehlzeitDefinition": "AL", "register": "AL", "schwachlastfaehig": "SCHWACHLASTFAEHIG"}]}]}, "transaktionsdaten": {"datenaustauschreferenz": "LZWDBZDB", "sparte": "STROM", "vorgangsnummer": "Vorgang3", "pruefidentifikator": "25004", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9900259000002", "rollencodetyp": "BDEW", "marktrolle": "NB", "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "nachname": "Andre Laue", "eMailAdresse": "marktpartner@stromnetz-hamburg.de"}}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9903111000003", "rollencodetyp": "BDEW", "marktrolle": "LF"}, "dokumentennummer": "M0FLEUCL", "kategorie": "Z60", "nachrichtendatum": "2024-08-13T13:38:00Z", "nachrichtenreferenznummer": "LZYNBYE1"}, "zusatzdaten": {}}}, {"name": "25006", "summary": "25006 — Übermittlung Übersicht Schaltzeitdefinitionen", "value": {"stammdaten": {"SCHALTZEITDEFINITION": [{"boTyp": "SCHALTZEITDEFINITION", "versionStruktur": "1", "beginndatum": "2024-07-31T22:00:00Z", "version": "2024-08-13T13:52:04Z", "notwendigkeit": "DEFINITIONEN_WERDEN_VERWENDET", "schaltzeiten": [{"code": "ALL", "haeufigkeit": "EINMALIG", "uebermittelbarkeit": "ELEKTRONISCH"}]}]}, "transaktionsdaten": {"datenaustauschreferenz": "M0QNMPZJ", "sparte": "STROM", "vorgangsnummer": "Vorgang4", "pruefidentifikator": "25006", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9900259000002", "rollencodetyp": "BDEW", "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "nachname": "Andre Laue", "eMailAdresse": "marktpartner@stromnetz-hamburg.de"}}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9903111000003", "rollencodetyp": "BDEW"}, "dokumentennummer": "M0M3IIPU", "kategorie": "Z78", "nachrichtendatum": "2024-08-13T13:50:00Z", "nachrichtenreferenznummer": "M0L512HS"}, "zusatzdaten": {}}}, {"name": "25007", "summary": "25007 — Übermittlung Übersicht Leistungskurvendefinitionen", "value": {"stammdaten": {"LEISTUNGSKURVENDEFINITION": [{"boTyp": "LEISTUNGSKURVENDEFINITION", "versionStruktur": "1", "beginndatum": "2024-07-31T22:00:00Z", "version": "2024-08-13T13:52:04Z", "notwendigkeit": "DEFINITIONEN_WERDEN_VERWENDET", "leistungskurven": [{"code": "AAL", "haeufigkeit": "EINMALIG", "uebermittelbarkeit": "ELEKTRONISCH"}]}]}, "transaktionsdaten": {"datenaustauschreferenz": "M0ORZ5SZ", "sparte": "STROM", "vorgangsnummer": "Vorgang5", "pruefidentifikator": "25007", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9900259000002", "rollencodetyp": "BDEW", "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "nachname": "Andre Laue", "eMailAdresse": "marktpartner@stromnetz-hamburg.de"}}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9903111000003", "rollencodetyp": "BDEW"}, "dokumentennummer": "M0H6RJMU", "kategorie": "Z79", "nachrichtendatum": "2024-08-20T13:45:00Z", "nachrichtenreferenznummer": "M0OEXW3E"}, "zusatzdaten": {}}}]}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Legt im Backend einen neuen Vorgang mit den Daten der eingegangenen Nachricht an.

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- `referenzAufAnfragenachricht != null` → Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202604/backend-schreiben-lf/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": false, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"ZAEHLZEITDEFINITION\": [\n      {\n        \"beginndatum\": \"2024-09-27T22:00:00Z\",\n        \"boTyp\": \"ZAEHLZEITDEFINITION\",\n        \"notwendigkeit\": \"DEFINITIONEN_WERDEN_VERWENDET\",\n        \"version\": \"2024-09-28T13:30:15Z\",\n        \"versionStruktur\": \"1\",\n        \"zaehlzeiten\": [\n          {\n            \"code\": \"AL\",\n            \"ermittlungLeistungsmaximum\": \"KEINE_VERWENDUNG_HOCHLASTFENSTER\",\n            \"haeufigkeit\": \"EINMALIG\",\n            \"istBestellbar\": true,\n            \"typ\": \"WAERMEPUMPE\",\n            \"uebermittelbarkeit\": \"ELEKTRONISCH\"\n          }\n        ],\n        \"zaehlzeitregister\": [\n          {\n            \"register\": \"AL\",\n            \"schwachlastfaehig\": \"SCHWACHLASTFAEHIG\",\n            \"zaehlzeitDefinition\": \"AL\"\n          }\n        ]\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"ansprechpartner\": {\n        \"boTyp\": \"ANSPRECHPARTNER\",\n        \"eMailAdresse\": \"marktpartner@stromnetz-hamburg.de\",\n        \"nachname\": \"Andre Laue\",\n        \"versionStruktur\": \"1\"\n      },\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"marktrolle\": \"NB\",\n      \"rollencodenummer\": \"9900259000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"datenaustauschreferenz\": \"LZWDBZDB\",\n    \"dokumentennummer\": \"M0FLEUCL\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"marktrolle\": \"LF\",\n      \"rollencodenummer\": \"9903111000003\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"Z60\",\n    \"nachrichtendatum\": \"2024-08-13T13:38:00Z\",\n    \"nachrichtenreferenznummer\": \"LZYNBYE1\",\n    \"pruefidentifikator\": \"25004\",\n    \"sparte\": \"STROM\",\n    \"vorgangsnummer\": \"Vorgang3\"\n  },\n  \"zusatzdaten\": {}\n}"} examples={[{"mediaType": "application/json", "examples": [{"name": "25004", "summary": "25004 — Übermittlung Übersicht Zählzeitdefinitionen", "value": {"stammdaten": {"ZAEHLZEITDEFINITION": [{"boTyp": "ZAEHLZEITDEFINITION", "versionStruktur": "1", "beginndatum": "2024-09-27T22:00:00Z", "version": "2024-09-28T13:30:15Z", "notwendigkeit": "DEFINITIONEN_WERDEN_VERWENDET", "zaehlzeiten": [{"code": "AL", "haeufigkeit": "EINMALIG", "uebermittelbarkeit": "ELEKTRONISCH", "ermittlungLeistungsmaximum": "KEINE_VERWENDUNG_HOCHLASTFENSTER", "istBestellbar": true, "typ": "WAERMEPUMPE"}], "zaehlzeitregister": [{"zaehlzeitDefinition": "AL", "register": "AL", "schwachlastfaehig": "SCHWACHLASTFAEHIG"}]}]}, "transaktionsdaten": {"datenaustauschreferenz": "LZWDBZDB", "sparte": "STROM", "vorgangsnummer": "Vorgang3", "pruefidentifikator": "25004", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9900259000002", "rollencodetyp": "BDEW", "marktrolle": "NB", "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "nachname": "Andre Laue", "eMailAdresse": "marktpartner@stromnetz-hamburg.de"}}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9903111000003", "rollencodetyp": "BDEW", "marktrolle": "LF"}, "dokumentennummer": "M0FLEUCL", "kategorie": "Z60", "nachrichtendatum": "2024-08-13T13:38:00Z", "nachrichtenreferenznummer": "LZYNBYE1"}, "zusatzdaten": {}}}, {"name": "25006", "summary": "25006 — Übermittlung Übersicht Schaltzeitdefinitionen", "value": {"stammdaten": {"SCHALTZEITDEFINITION": [{"boTyp": "SCHALTZEITDEFINITION", "versionStruktur": "1", "beginndatum": "2024-07-31T22:00:00Z", "version": "2024-08-13T13:52:04Z", "notwendigkeit": "DEFINITIONEN_WERDEN_VERWENDET", "schaltzeiten": [{"code": "ALL", "haeufigkeit": "EINMALIG", "uebermittelbarkeit": "ELEKTRONISCH"}]}]}, "transaktionsdaten": {"datenaustauschreferenz": "M0QNMPZJ", "sparte": "STROM", "vorgangsnummer": "Vorgang4", "pruefidentifikator": "25006", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9900259000002", "rollencodetyp": "BDEW", "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "nachname": "Andre Laue", "eMailAdresse": "marktpartner@stromnetz-hamburg.de"}}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9903111000003", "rollencodetyp": "BDEW"}, "dokumentennummer": "M0M3IIPU", "kategorie": "Z78", "nachrichtendatum": "2024-08-13T13:50:00Z", "nachrichtenreferenznummer": "M0L512HS"}, "zusatzdaten": {}}}, {"name": "25007", "summary": "25007 — Übermittlung Übersicht Leistungskurvendefinitionen", "value": {"stammdaten": {"LEISTUNGSKURVENDEFINITION": [{"boTyp": "LEISTUNGSKURVENDEFINITION", "versionStruktur": "1", "beginndatum": "2024-07-31T22:00:00Z", "version": "2024-08-13T13:52:04Z", "notwendigkeit": "DEFINITIONEN_WERDEN_VERWENDET", "leistungskurven": [{"code": "AAL", "haeufigkeit": "EINMALIG", "uebermittelbarkeit": "ELEKTRONISCH"}]}]}, "transaktionsdaten": {"datenaustauschreferenz": "M0ORZ5SZ", "sparte": "STROM", "vorgangsnummer": "Vorgang5", "pruefidentifikator": "25007", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9900259000002", "rollencodetyp": "BDEW", "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "nachname": "Andre Laue", "eMailAdresse": "marktpartner@stromnetz-hamburg.de"}}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9903111000003", "rollencodetyp": "BDEW"}, "dokumentennummer": "M0H6RJMU", "kategorie": "Z79", "nachrichtendatum": "2024-08-20T13:45:00Z", "nachrichtenreferenznummer": "M0OEXW3E"}, "zusatzdaten": {}}}]}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend mit den Daten der eingegangenen Nachricht fort.

</li>

<li data-teil="lesen" data-stufe="verarbeitung">

**Daten für die Verarbeitung laden**
- `LESEN_BERECHNUNGSFORMEL_BASIS`

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="2" anker="schritt-2" richtung="fremd" kopf={{"links": {"label": "NB", "eigen": false}, "rechts": {"label": "MSB"}}}>

### Übersicht der Definitionen des NB

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [25006](/schnittstellen/202604/pruefi/UTILTS/PI_25006) — Übermittlung Übersicht Schaltzeitdefinitionen · AS4
- [25007](/schnittstellen/202604/pruefi/UTILTS/PI_25007) — Übermittlung Übersicht Leistungskurvendefinitionen · AS4
- [25004](/schnittstellen/202604/pruefi/UTILTS/PI_25004) — Übermittlung Übersicht Zählzeitdefinitionen · AS4

</div>

</Schritt>

<a id="abschnitt-informationen"></a>

## Prozess-Informationen

Wortlaut der Lesefassung, Steckbrief Kap. 1.2.1.1, S. 6–7.

<Stepper>
<ol>

<li data-blatt="vorbedingungen">

### Vorbedingungen

- Die EDIFACT-Kommunikation zwischen NB und LF bzw. MSB ist aufgebaut.

</li>

<li data-blatt="ergebnisse">

### Ergebnisse

Der LF bzw. MSB kann die Übersicht nutzen, um die später vom NB an den LF bzw. MSB über den Use-Case „[Übermittlung einer Definition des NB durch den NB](/prozessdoku/202604/LF/GPKE-Teil3-uebermittlung-einer-definition-des-nb-durch-den-nb)“ übermittelte Definition zuzuordnen.

</li>

<li data-blatt="anforderungen">

### Weitere Anforderungen

- Verwendet der NB keine Zählzeitdefinitionen des NB oder keine Schaltzeitdefinitionen des NB oder keine Leistungskurvendefinitionen des NB, wird dies in der Übersicht mitgeteilt.
- Verwendet der NB eine Zählzeitdefinition des NB, Schaltzeitdefinition des NB oder Leistungskurvendefinition des NB, die sich nicht im Rahmen des Use-Cases „[Übermittlung einer Definition des NB durch den NB](/prozessdoku/202604/LF/GPKE-Teil3-uebermittlung-einer-definition-des-nb-durch-den-nb)“ übermitteln lässt, wird diese in der jeweiligen Übersicht als „nicht elektronisch übermittelbar“ gekennzeichnet.
- Im Fall der Übersicht der Zählzeitdefinitionen des NB:
  - Verwendet der NB Hochlastzeitfenster zur Ermittlung des Leistungsmaximums bei atypischer Netznutzung (nach § 19 Absatz 2 Satz 1 StromNEV), werden diese im Use-Case „Übermittlung der Übersicht der Definitionen des NB durch den NB“ und im Use-Case „[Übermittlung einer Definition des NB durch den NB](/prozessdoku/202604/LF/GPKE-Teil3-uebermittlung-einer-definition-des-nb-durch-den-nb)“ vom NB mitgeteilt.
  - Die Übersicht der Zählzeitdefinitionen des NB ist vom NB auch an den Letztverbraucher in seiner Rolle als LF zu übermitteln, wenn im Rahmen der Netznutzungsabrechnung der Letztverbraucher in die Rolle des LF tritt, soweit diese Regelungen sinngemäß auf ihn anwendbar sind.
  - Der NB übermittelt in der Übersicht der Zählzeitdefinitionen des NB zu jeder Zählzeitdefinition des NB, ob diese Zählzeitdefinition des NB vom LF bestellbar ist oder nicht mehr bestellbar ist, sofern diese Zählzeitdefinition des NB für eine zukünftige Einrichtung einer Zählzeitdefinition des NB nicht mehr in Frage kommt, jedoch noch an einzelnen Marktlokationen genutzt wird. Ist eine Zählzeitdefinition des NB nicht mehr bestellbar, kann diese durch den LF über den Use-Case „[Bestellung einer Konfiguration vom LF an NB](/prozessdoku/202604/LF/GPKE-Teil3-bestellung-einer-konfiguration-vom-lf-an-nb)“ nicht mehr bestellt werden.

</li>

<li data-blatt="anlass">

### Anlass

Dem LF bzw. MSB liegt die aktuelle
- Übersicht der Zählzeitdefinitionen des NB bzw.
- Übersicht der Schaltzeitdefinitionen des NB bzw.
- Übersicht der Leistungskurvendefinitionen des NB nicht vor.

**Vorher läuft:** [Reklamation der Übersicht der Definitionen des NB vom LF an NB](/prozessdoku/202604/LF/GPKE-Teil3-reklamation-der-uebersicht-der-definitionen-des-nb-vom-lf-an-nb), [Reklamation der Übersicht der Definitionen des NB vom MSB an NB](/prozessdoku/202604/MSB/GPKE-Teil3-reklamation-der-uebersicht-der-definitionen-des-nb-vom-msb-an-nb) — diese Prozesse nennen den hier gezeigten in ihrem Ergebnis.

</li>

<li data-blatt="erste-nachricht">

### Erste Nachricht

**NB** sendet „Übersicht der Definitionen des NB“ (Schritt 1). Ab hier ist der Beteiligte dieser Seite am Zug.

</li>

<li data-blatt="ziel">

### Ziel

Die LF und MSB haben die aktuelle
- Übersicht der Zählzeitdefinitionen des NB bzw.
- Übersicht der Schaltzeitdefinitionen des NB bzw.
- Übersicht der Leistungskurvendefinitionen des NB vorliegen.

</li>

</ol>
</Stepper>

<a id="abschnitt-sichten"></a>

## Andere Sichten des Prozesses

Derselbe Prozess, aus den Augen der anderen Beteiligten: dieselben Schritte, jeweils aus deren Sicht gelesen.

- [Sicht NB](/prozessdoku/202604/NB/GPKE-Teil3-uebermittlung-der-uebersicht-der-definitionen-des-nb-durch-den-nb) — NB
- [Sicht MSB](/prozessdoku/202604/MSB/GPKE-Teil3-uebermittlung-der-uebersicht-der-definitionen-des-nb-durch-den-nb) — MSB

<Hinweisbereich>

*Die Schritte sind die **möglichen** Nachrichten dieses Prozesses, keine Abfolge — die Quelle führt weder Bedingungen noch Alternativen. Das Kästchen am Schritt nennt links die eigene Sicht: **←** empfängt sie, **→** sendet sie. Zugeklappte Schritte laufen zwischen anderen Marktpartnern.*

Diese Lesezugriffe sind im API-Katalog dieser Formatversion nicht geführt; am Schritt steht deshalb nur ihr Kommando, ohne Adresse und ohne Knopf.

Betrifft: [1](#schritt-1)

</Hinweisbereich>
