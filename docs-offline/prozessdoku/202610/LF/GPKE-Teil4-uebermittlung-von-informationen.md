# Übermittlung von Informationen — Sicht LF

<Kopf rolle="LF" beteiligter="LF" festlegung="GPKE" dokument="GPKE Teil 4" kapitel="4.2" sparte="Strom" schritte={1} suchtitel="Übermittlung von Informationen — Sicht LF · GPKE Teil 4 · Formatversion 202610" abschnitte={[{"id": "abschnitt-ablauf", "label": "Prozessablauf"}, {"id": "abschnitt-schritte", "label": "Prozessschritte"}, {"id": "abschnitt-informationen", "label": "Prozess-Informationen"}, {"id": "abschnitt-sichten", "label": "Andere Sichten des Prozesses"}]} />

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

## Prozessablauf aus Sicht des LF

<Systembild svg={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1004 315\" width=\"1004\" height=\"315\" role=\"img\" aria-labelledby=\"sb-title\" class=\"maco-systembild\">\n<title id=\"sb-title\">Systembild: Übermittlung von Informationen aus Sicht LF</title>\n<defs><marker id=\"sb-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect class=\"sb-lane-kopf\" x=\"16\" y=\"12\" width=\"232\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend-System des Kunden</text>\n<rect class=\"sb-lane-kopf\" x=\"398\" y=\"12\" width=\"264\" height=\"46\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · LF</text>\n<rect class=\"sb-lane-kopf\" x=\"812\" y=\"12\" width=\"176\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"900\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Marktpartner</text>\n<line x1=\"323\" y1=\"58\" x2=\"323\" y2=\"303\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"737\" y1=\"58\" x2=\"737\" y2=\"303\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect class=\"sb-kasten sb-trigger\" x=\"432\" y=\"80\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessauslöser empfangen</text>\n<rect class=\"sb-kasten sb-backend sb-trigger\" x=\"34\" y=\"80\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">2 Ereignisse, alternativ</text>\n<line x1=\"230\" y1=\"96\" x2=\"432\" y2=\"96\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"88\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"144\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"164\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">1. Information</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"113\" x2=\"530\" y2=\"144\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"142\" r=\"5\"/><line x1=\"900\" y1=\"147\" x2=\"900\" y2=\"159\"/><line x1=\"893\" y1=\"151\" x2=\"907\" y2=\"151\"/><line x1=\"900\" y1=\"159\" x2=\"894\" y2=\"169\"/><line x1=\"900\" y1=\"159\" x2=\"906\" y2=\"169\"/></g>\n<text x=\"900\" y=\"191\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"628\" y1=\"160\" x2=\"878\" y2=\"160\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"152\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"176\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">21045, 37000, 37000…</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"227\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"247\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"177\" x2=\"530\" y2=\"227\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"227\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"247\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"243\" x2=\"230\" y2=\"243\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"235\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n</svg>"} gesamt={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 730 300\" width=\"730\" height=\"300\" role=\"img\" aria-labelledby=\"sd-title\" class=\"maco-sequence\">\n<title id=\"sd-title\">Sequenzdiagramm: Übermittlung von Informationen aus Sicht LF</title>\n<defs><marker id=\"sd-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect x=\"16\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"121\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend (Kunde)</text>\n<line x1=\"121\" y1=\"64\" x2=\"121\" y2=\"288\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"260\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"365\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · LF</text>\n<line x1=\"365\" y1=\"64\" x2=\"365\" y2=\"288\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"504\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"609\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"609\" y1=\"64\" x2=\"609\" y2=\"288\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"121\" y1=\"90\" x2=\"365\" y2=\"90\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"81\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">2 Ereignisse, alternativ</text>\n<text x=\"243\" y=\"105\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Trigger-Event</text>\n<line x1=\"365\" y1=\"152\" x2=\"609\" y2=\"152\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"143\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">1. Information</text>\n<text x=\"487\" y=\"167\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 21045, 37000, 37000…</text>\n<line x1=\"365\" y1=\"214\" x2=\"121\" y2=\"214\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"205\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"229\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n</svg>"} titel="LF" />

<a id="abschnitt-schritte"></a>

## Prozessschritte

<Schritt nr="1" anker="schritt-1" richtung="ausgehend" kopf={{"links": {"label": "LF", "eigen": true}, "rechts": {"label": "NB"}}}>

### Information

<Schrittskizze sicht={{"label": "LF"}} zeilen={[{"art": "ausloeser", "werte": ["START_PARTIN", "START_UEBERMITTLUNG_ENFG"]}, {"art": "senden", "label": "NB", "weg": "AS4", "nachrichten": [{"nr": "21045", "titel": "EnFG Informationen"}, {"nr": "37000", "titel": "Kommunikationsdaten des LF Strom"}, {"nr": "37001", "titel": "Kommunikationsdaten des NB Strom"}, {"nr": "37002", "titel": "Kommunikationsdaten des MSB Strom"}, {"nr": "37003", "titel": "Kommunikationsdaten des BKV Strom"}, {"nr": "37004", "titel": "Kommunikationsdaten des BIKO Strom"}, {"nr": "37005", "titel": "Kommunikationsdaten des ÜNB Strom"}, {"nr": "37006", "titel": "Kommunikationsdaten des ESA Strom"}, {"nr": "13028", "titel": "Grundlage POG-Ermittlung"}]}, {"art": "fortschreiben"}]} />

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

<li data-teil="ausloeser">

**Prozessauslöser**
- [`START_PARTIN`](/schnittstellen/202610/trigger/events/LF-START_PARTIN) · [Im Playground ausprobieren](/api/202610/ausloeser-lf/start-partin)
- [`START_UEBERMITTLUNG_ENFG`](/schnittstellen/202610/trigger/events/LF-START_UEBERMITTLUNG_ENFG) · [Im Playground ausprobieren](/api/202610/ausloeser-lf/start-uebermittlung-enfg)

Das Backend stößt diesen Schritt mit einem dieser Ereignisse an.

</li>

<li data-teil="nachricht">

Nachricht an **NB** · AS4

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202610/backend-schreiben-lf/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": false, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"KOMMUNIKATIONSDATEN\": [\n      {\n        \"boTyp\": \"KOMMUNIKATIONSDATEN\",\n        \"gueltigkeit\": \"2025-06-06T22:00:00Z\",\n        \"kommunikationsDatenBlattInaktiv\": true,\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9903790000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"anwendungsreferenznummer\": \"2\",\n    \"datenaustauschreferenz\": \"113601\",\n    \"dokumentennummer\": \"CS356455854555\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9900321000005\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"10\",\n    \"nachrichtendatum\": \"2026-10-01T11:00:00Z\",\n    \"nachrichtenreferenznummer\": \"298012\",\n    \"pruefidentifikator\": \"37000\",\n    \"sparte\": \"STROM\",\n    \"vorgangsreferenznummer\": \"1\"\n  },\n  \"zusatzdaten\": {}\n}"} examples={[{"mediaType": "application/json", "examples": [{"name": "37000", "summary": "37000 — Kommunikationsdaten des LF Strom", "value": {"stammdaten": {"KOMMUNIKATIONSDATEN": [{"boTyp": "KOMMUNIKATIONSDATEN", "versionStruktur": "1", "gueltigkeit": "2025-06-06T22:00:00Z", "kommunikationsDatenBlattInaktiv": true}]}, "transaktionsdaten": {"datenaustauschreferenz": "113601", "sparte": "STROM", "pruefidentifikator": "37000", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9903790000002", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900321000005", "rollencodetyp": "BDEW"}, "dokumentennummer": "CS356455854555", "kategorie": "10", "nachrichtendatum": "2026-10-01T11:00:00Z", "nachrichtenreferenznummer": "298012", "vorgangsreferenznummer": "1", "anwendungsreferenznummer": "2"}, "zusatzdaten": {}}}, {"name": "37001", "summary": "37001 — Kommunikationsdaten des NB Strom", "value": {"stammdaten": {"KOMMUNIKATIONSDATEN": [{"boTyp": "KOMMUNIKATIONSDATEN", "versionStruktur": "1", "gueltigkeit": "2025-06-30T22:00:00Z", "kommunikationsDatenBlattInaktiv": true}]}, "transaktionsdaten": {"datenaustauschreferenz": "113601", "sparte": "STROM", "pruefidentifikator": "37001", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9903790000002", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900321000005", "rollencodetyp": "BDEW"}, "dokumentennummer": "CS356455854555", "kategorie": "10", "nachrichtendatum": "2026-10-01T11:00:00Z", "nachrichtenreferenznummer": "298012", "vorgangsreferenznummer": "1", "anwendungsreferenznummer": "2"}, "zusatzdaten": {}}}, {"name": "37002", "summary": "37002 — Kommunikationsdaten des MSB Strom", "value": {"stammdaten": {"KOMMUNIKATIONSDATEN": [{"boTyp": "KOMMUNIKATIONSDATEN", "versionStruktur": "1", "gueltigkeit": "2024-06-30T22:00:00Z", "kommunikationsDatenBlattInaktiv": true}]}, "transaktionsdaten": {"datenaustauschreferenz": "113601", "sparte": "STROM", "pruefidentifikator": "37002", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9903790000002", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900321000005", "rollencodetyp": "BDEW"}, "dokumentennummer": "CS356455854555", "kategorie": "10", "nachrichtendatum": "2026-10-01T11:00:00Z", "nachrichtenreferenznummer": "298012", "vorgangsreferenznummer": "1", "anwendungsreferenznummer": "2"}, "zusatzdaten": {}}}, {"name": "13028", "summary": "13028 — Grundlage POG-Ermittlung", "value": {"stammdaten": {"ENERGIEMENGE": [{"boTyp": "ENERGIEMENGE", "versionStruktur": "1", "lokationsId": "50074561188", "lokationsTyp": "MALO", "energieverbrauch": [{"startdatum": "2025-04-01T22:00:00Z", "enddatum": "2025-04-02T22:00:00Z", "messwertstatus": "GRUNDLAGE_POG_ERMITTLUNG", "obiskennzahl": "1-1:1.9.0", "wert": 500, "position": 1}, {"startdatum": "2025-04-15T22:00:00Z", "enddatum": "2025-04-16T22:00:00Z", "messwertstatus": "GRUNDLAGE_POG_ERMITTLUNG", "obiskennzahl": "1-1:1.9.0", "wert": 750, "position": 1}, {"startdatum": "2025-04-30T22:00:00Z", "enddatum": "2025-05-01T22:00:00Z", "messwertstatus": "GRUNDLAGE_POG_ERMITTLUNG", "obiskennzahl": "1-1:1.9.0", "wert": 1000.123, "position": 2}]}]}, "transaktionsdaten": {"datenaustauschreferenz": "161201", "sparte": "STROM", "pruefidentifikator": "13028", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9900321000005", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9904446000007", "rollencodetyp": "BDEW"}, "dokumentennummer": "726947BGM", "kategorie": "Z85", "nachrichtenfunktion": "9", "nachrichtendatum": "2026-10-01T11:00:00Z", "nachrichtenreferenznummer": "726947", "typ": "EM"}, "zusatzdaten": {}}}]}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend fort, nachdem die Nachricht erstellt ist.

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

Der Beteiligte dieser Seite sendet selbst: „Information“ an **NB** (Schritt 1).

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

- [Sicht NB](/prozessdoku/202610/NB/GPKE-Teil4-uebermittlung-von-informationen) — NB

<Hinweisbereich>

*Die Schritte sind die **möglichen** Nachrichten dieses Prozesses, keine Abfolge — die Quelle führt weder Bedingungen noch Alternativen. Das Kästchen am Schritt nennt links die eigene Sicht: **←** empfängt sie, **→** sendet sie. Zugeklappte Schritte laufen zwischen anderen Marktpartnern.*

</Hinweisbereich>
