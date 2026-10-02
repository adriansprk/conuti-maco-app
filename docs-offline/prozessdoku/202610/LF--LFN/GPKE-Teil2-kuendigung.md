# Kündigung — Sicht LFN

<Kopf rolle="LF" beteiligter="LFN" festlegung="GPKE" dokument="GPKE Teil 2" kapitel="1.2.2" sparte="Strom" schritte={2} suchtitel="Kündigung — Sicht LFN (Marktrolle LF) · GPKE Teil 2 · Formatversion 202610" stichworte="Lieferantenwechsel" abschnitte={[{"id": "abschnitt-ablauf", "label": "Prozessablauf"}, {"id": "abschnitt-schritte", "label": "Prozessschritte"}, {"id": "abschnitt-informationen", "label": "Prozess-Informationen"}, {"id": "abschnitt-sichten", "label": "Andere Sichten des Prozesses"}]} />

<Kurzfassung>

Der LFN sendet an den LFA eine Kündigung. Der LFA prüft die Kündigung und teilt dem LFN das Ergebnis mit.

</Kurzfassung>

<a id="abschnitt-ablauf"></a>

## Prozessablauf aus Sicht des LF (LFN)

<Systembild svg={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1004 600\" width=\"1004\" height=\"600\" role=\"img\" aria-labelledby=\"sb-title\" class=\"maco-systembild\">\n<title id=\"sb-title\">Systembild: Kündigung aus Sicht LF</title>\n<defs><marker id=\"sb-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect class=\"sb-lane-kopf\" x=\"16\" y=\"12\" width=\"232\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend-System des Kunden</text>\n<rect class=\"sb-lane-kopf\" x=\"398\" y=\"12\" width=\"264\" height=\"46\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · LFN</text>\n<rect class=\"sb-lane-kopf\" x=\"812\" y=\"12\" width=\"176\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"900\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Marktpartner</text>\n<line x1=\"323\" y1=\"58\" x2=\"323\" y2=\"588\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"737\" y1=\"58\" x2=\"737\" y2=\"588\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect class=\"sb-kasten sb-trigger\" x=\"432\" y=\"80\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessauslöser empfangen</text>\n<rect class=\"sb-kasten sb-backend sb-trigger\" x=\"34\" y=\"80\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">START_KUENDIGUNG</text>\n<line x1=\"230\" y1=\"96\" x2=\"432\" y2=\"96\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"88\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"144\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"164\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">1. Kündigung</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"113\" x2=\"530\" y2=\"144\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"142\" r=\"5\"/><line x1=\"900\" y1=\"147\" x2=\"900\" y2=\"159\"/><line x1=\"893\" y1=\"151\" x2=\"907\" y2=\"151\"/><line x1=\"900\" y1=\"159\" x2=\"894\" y2=\"169\"/><line x1=\"900\" y1=\"159\" x2=\"906\" y2=\"169\"/></g>\n<text x=\"900\" y=\"191\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">LFA</text>\n<line x1=\"628\" y1=\"160\" x2=\"878\" y2=\"160\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"152\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"176\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">55016</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"227\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"247\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"177\" x2=\"530\" y2=\"227\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"227\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"247\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"243\" x2=\"230\" y2=\"243\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"235\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"291\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"311\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">2. Antwort auf Kündigung</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"260\" x2=\"530\" y2=\"291\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"289\" r=\"5\"/><line x1=\"900\" y1=\"294\" x2=\"900\" y2=\"306\"/><line x1=\"893\" y1=\"298\" x2=\"907\" y2=\"298\"/><line x1=\"900\" y1=\"306\" x2=\"894\" y2=\"316\"/><line x1=\"900\" y1=\"306\" x2=\"906\" y2=\"316\"/></g>\n<text x=\"900\" y=\"338\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">LFA</text>\n<line x1=\"878\" y1=\"307\" x2=\"628\" y2=\"307\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"299\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"323\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">55017, 55018</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"374\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"394\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z33</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"324\" x2=\"530\" y2=\"374\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"438\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"458\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"407\" x2=\"530\" y2=\"438\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"438\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"458\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"454\" x2=\"230\" y2=\"454\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"446\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-lesen_verarbeitung\" x=\"432\" y=\"502\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"522\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Daten für die Verarbeitung</text>\n<text x=\"530\" y=\"537\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">laden</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"471\" x2=\"530\" y2=\"502\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-lesen_verarbeitung\" x=\"34\" y=\"502\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"522\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">3 Lese-Schnittstellen</text>\n<text x=\"132\" y=\"537\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">aufgerufen</text>\n<line x1=\"432\" y1=\"526\" x2=\"230\" y2=\"526\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"518\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<text x=\"331\" y=\"542\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">je einzeln am Schritt</text>\n</svg>"} gesamt={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 730 424\" width=\"730\" height=\"424\" role=\"img\" aria-labelledby=\"sd-title\" class=\"maco-sequence\">\n<title id=\"sd-title\">Sequenzdiagramm: Kündigung aus Sicht LF</title>\n<defs><marker id=\"sd-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect x=\"16\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"121\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend (Kunde)</text>\n<line x1=\"121\" y1=\"64\" x2=\"121\" y2=\"412\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"260\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"365\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · LFN</text>\n<line x1=\"365\" y1=\"64\" x2=\"365\" y2=\"412\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"504\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"609\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">LFA</text>\n<line x1=\"609\" y1=\"64\" x2=\"609\" y2=\"412\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"121\" y1=\"90\" x2=\"365\" y2=\"90\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"81\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">START_KUENDIGUNG</text>\n<text x=\"243\" y=\"105\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Trigger-Event</text>\n<line x1=\"365\" y1=\"152\" x2=\"609\" y2=\"152\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"143\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">1. Kündigung</text>\n<text x=\"487\" y=\"167\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55016</text>\n<line x1=\"365\" y1=\"214\" x2=\"121\" y2=\"214\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"205\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"229\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"609\" y1=\"276\" x2=\"365\" y2=\"276\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"267\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">2. Antwort auf Kündigung</text>\n<text x=\"487\" y=\"291\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55017, 55018 · E_0614</text>\n<text x=\"487\" y=\"304\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0614 — Kündigung Vertrag prüfen</text>\n<line x1=\"365\" y1=\"338\" x2=\"121\" y2=\"338\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"329\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"353\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n</svg>"} titel="LFN" />

<a id="abschnitt-schritte"></a>

## Prozessschritte

<Schritt nr="1" anker="schritt-1" richtung="ausgehend" kopf={{"links": {"label": "LFN", "eigen": true}, "rechts": {"label": "LFA"}}}>

### Kündigung

<Schrittskizze sicht={{"label": "LFN"}} zeilen={[{"art": "ausloeser", "werte": ["START_KUENDIGUNG"]}, {"art": "senden", "label": "LFA", "weg": "AS4", "nachrichten": [{"nr": "55016", "titel": "Kündigung"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55016](/schnittstellen/202610/pruefi/UTILMD/PI_55016) — Kündigung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="ausloeser">

**Prozessauslöser** [`START_KUENDIGUNG`](/schnittstellen/202610/trigger/events/LF-START_KUENDIGUNG) · [Im Playground ausprobieren](/api/202610/ausloeser-lf/start-kuendigung)

Das Backend stößt diesen Schritt mit diesem Ereignis an.

</li>

<li data-teil="nachricht">

Nachricht an **LFA** · AS4

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202610/backend-schreiben-lf/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": false, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend fort, nachdem die Nachricht erstellt ist.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="2" anker="schritt-2" richtung="eingehend" kopf={{"links": {"label": "LFN", "eigen": true}, "rechts": {"label": "LFA"}}}>

### Antwort auf Kündigung

<Schrittskizze sicht={{"label": "LFN"}} zeilen={[{"art": "empfangen", "label": "LFA", "weg": "AS4", "nachrichten": [{"nr": "55017", "titel": "Bestätigung Kündigung"}, {"nr": "55018", "titel": "Ablehnung Kündigung"}]}, {"art": "aperak", "werte": ["Z33"]}, {"art": "fortschreiben"}, {"art": "lesen_verarbeitung", "schnittstellen": [{"label": "Bilanzierung lesen"}, {"label": "Netznutzungsvertrag lesen"}, {"label": "Energieliefervertrag lesen"}]}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55017](/schnittstellen/202610/pruefi/UTILMD/PI_55017) — Bestätigung Kündigung · AS4
- [55018](/schnittstellen/202610/pruefi/UTILMD/PI_55018) — Ablehnung Kündigung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **LFA** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `55017`, `55018` → [E_0614](/referenz/202610/ebd/E_0614) · LF · Kündigung Vertrag prüfen

</div>

</li>

<li data-teil="aperak">

**Aperak-Prüfungen**
- `55017`, `55018` → `Z33` — Aperak Prüfung: Ist referenzierte Nachricht bekannt ?

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202610/backend-schreiben-lf/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": false, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"BILANZIERUNG\": [\n      {\n        \"boTyp\": \"BILANZIERUNG\",\n        \"versionStruktur\": \"1\",\n        \"vorjahresverbrauch\": {\n          \"einheit\": \"KWH\",\n          \"wert\": 6460\n        }\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9903448000007\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"anfragereferenznummer\": \"PCL09023100613515599116940000022246\",\n    \"antwortstatus\": \"A09\",\n    \"antwortstatusCodeliste\": \"E_0614\",\n    \"datenaustauschreferenz\": \"P102845739A\",\n    \"dokumentennummer\": \"P102845739A-1\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9911694000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"endezumtermin\": \"2025-11-30T23:00:00Z\",\n    \"kategorie\": \"E35\",\n    \"nachrichtendatum\": \"2024-04-01T15:47:00Z\",\n    \"nachrichtenreferenznummer\": \"1\",\n    \"pruefidentifikator\": \"55017\",\n    \"sparte\": \"STROM\",\n    \"transaktionsgrund\": \"E03\",\n    \"transaktionsgrundergaenzung\": \"ZW4\",\n    \"vorgangsnummer\": \"ECOUNT_207917572\"\n  }\n}"} examples={[{"mediaType": "application/json", "examples": [{"name": "55017", "summary": "55017 — Bestätigung Kündigung", "value": {"stammdaten": {"BILANZIERUNG": [{"boTyp": "BILANZIERUNG", "versionStruktur": "1", "vorjahresverbrauch": {"wert": 6460, "einheit": "KWH"}}]}, "transaktionsdaten": {"datenaustauschreferenz": "P102845739A", "sparte": "STROM", "transaktionsgrund": "E03", "transaktionsgrundergaenzung": "ZW4", "vorgangsnummer": "ECOUNT_207917572", "pruefidentifikator": "55017", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9903448000007", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9911694000002", "rollencodetyp": "BDEW"}, "dokumentennummer": "P102845739A-1", "kategorie": "E35", "nachrichtendatum": "2024-04-01T15:47:00Z", "nachrichtenreferenznummer": "1", "anfragereferenznummer": "PCL09023100613515599116940000022246", "antwortstatus": "A09", "antwortstatusCodeliste": "E_0614", "endezumtermin": "2025-11-30T23:00:00Z"}}}, {"name": "55018", "summary": "55018 — Ablehnung Kündigung", "value": {"stammdaten": {"ENERGIELIEFERVERTRAG": [{"boTyp": "VERTRAG", "versionStruktur": "1", "vertragsart": "ENERGIELIEFERVERTRAG", "sparte": "STROM", "vertragskonditionen": {"kuendigungsfrist": {"zeitraumText": "03MQ"}}}]}, "transaktionsdaten": {"datenaustauschreferenz": "DAFCWAEUJDPLAJ", "sparte": "STROM", "transaktionsgrund": "E03", "vorgangsnummer": "24062416225400000000000102159662022", "pruefidentifikator": "55018", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9903729000007", "rollencodetyp": "BDEW", "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "nachname": "P GETTY", "rufnummern": [{"nummerntyp": "RUF_DURCHWAHL", "rufnummer": "+3222271020"}]}}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9977842000004", "rollencodetyp": "BDEW"}, "dokumentennummer": "DA342411041308449903323000007541014", "kategorie": "E35", "nachrichtendatum": "2025-06-05T12:31:00Z", "nachrichtenreferenznummer": "DAKLKYLSHQPTDN", "anfragereferenznummer": "KDG123456", "gueltigAb": "2025-09-30T22:00:00Z", "antwortstatus": "A14", "antwortstatusCodeliste": "E_0614", "datumKuendigungLf": "2025-10-31T23:00:00Z"}, "zusatzdaten": {}}}]}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend mit den Daten der eingegangenen Nachricht fort.

</li>

<li data-teil="lesen" data-stufe="verarbeitung">

**Daten für die Verarbeitung laden**
- [Bilanzierung lesen](/api/202610/backend-lesen/getaccountingbasic#bilanzierung-lesen) `GET /getAccountingBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getAccountingBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_BILANZIERUNG_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Netznutzungsvertrag lesen](/api/202610/backend-lesen/getgridusagecontractbasic#netznutzungsvertrag-lesen) `GET /getGridUsageContractBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getGridUsageContractBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": false, "defaultValue": "MALO", "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": false, "defaultValue": "2024-06-28T12:18:00Z", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Energieliefervertrag lesen](/api/202610/backend-lesen/getenergysupplycontractbasic#energieliefervertrag-lesen) `GET /getEnergySupplyContractBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getEnergySupplyContractBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_ENERGIELIEFERVERTRAG_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

</li>

</ol>
</Stepper>

</div>

</Schritt>

<details>
<summary>Entscheidungsbäume dieses Prozesses</summary>

| EBD | Name |
|---|---|
| [E_0614](/referenz/202610/ebd/E_0614) | Kündigung Vertrag prüfen |

</details>

<a id="abschnitt-informationen"></a>

## Prozess-Informationen

Wortlaut der Lesefassung, Steckbrief Kap. 1.2.1, S. 7–8.

<Stepper>
<ol>

<li data-blatt="vorbedingungen">

### Vorbedingungen

- Im Fall einer verbrauchenden Marktlokation: Der LFN besitzt die Vollmacht des Letztverbrauchers in dessen Namen die Kündigung vornehmen zu dürfen.
- Im Fall einer erzeugenden Marktlokation bzw. einer Tranche: Der LFN besitzt die Vollmacht des EZ in dessen Namen die Kündigung vornehmen zu dürfen.
- Die MaLo-ID der Marktlokation ist bekannt bzw. im Falleiner tranchierten Marktlokation ist die MaLo-ID der Tranche bekannt.

</li>

<li data-blatt="ergebnisse">

### Ergebnisse

Der LFA ist verpflichtet, unmittelbar mit Bestätigung der Kündigung gegenüber dem LFN auch den Use-Case „[Lieferende von LF an NB](/prozessdoku/202610/LF/GPKE-Teil2-lieferende-von-lf-an-nb)“ gegenüber dem NB anzustoßen.

</li>

<li data-blatt="fehlerfall">

### Fehlerfall

#### Ergebnis im Fehlerfall

- Im Fall einer verbrauchenden Marktlokation: Der zwischen Letztverbraucher und LFA abgeschlossene Stromliefervertrag für die genannte verbrauchende Marktlokation ist nicht gekündigt.
- Im Fall einer erzeugenden Marktlokation bzw. einer Tranche: der zwischen EZ und LFA abgeschlossene Stromabnahmevertrag für die genannte, erzeugende Marktlokation bzw. die genannte Tranche ist nicht gekündigt.
- Der LFN sendet bei Bedarf erneut eine Kündigung an den LFA.

#### Fehlerfälle

- Der LFA ist der vom LFN angegebenen Marktlokation bzw. Tranche zum Kündigungstermin nicht zugeordnet.
- Die Vertragssituation des LFA lässt die gewünschte Kündigung des LFN nicht zu.

</li>

<li data-blatt="anforderungen">

### Weitere Anforderungen

- Im Fall einer verbrauchenden Marktlokation:
  - Bei einer Ersatzversorgung handelt es sich um kein kündigungspflichtiges Vertragsverhältnis; es ist daher keine Kündigung erforderlich (vgl. § 38 Abs. 4 EnWG). Sofern ein LFN dem E/G trotzdem eine Kündigung zum nächstmöglichen Zeitpunkt oder zu einem fixen Zeitpunkt in die Zukunft übermittelt, stimmt der E/G der Kündigung zu, sofern keine Ablehnungsgründe vorliegen.
  - Ungeachtet der jederzeit bestehenden Möglichkeit des Letztverbrauchers, seinen Stromliefervertrag schriftlich zu kündigen, darf der LFA eine nach diesem Use-Case gemeldete Kündigung nicht allein unter Berufung auf die fehlende Einhaltung einer vertraglich vereinbarten Form zurückweisen. In diesem Fall hat er eine Kündigung auch in elektronischer Form unter Anwendung dieses Use-Case entgegenzunehmen und zu bearbeiten.
  - Hinweis: Der Use-Case behandelt nicht den Fall, dass der Letztverbraucher selbst gegenüber dem LFA den Stromliefervertrag kündigt. Wenn der Letztverbraucher vorab selbst kündigt, ist der Use-Case „[Lieferende von LF an NB](/prozessdoku/202610/LF/GPKE-Teil2-lieferende-von-lf-an-nb)“ vom LFA gegenüber dem NB unmittelbar mit Verfassen der Kündigungsbestätigung an den Letztverbraucher anzustoßen.
- Im Fall einer erzeugenden Marktlokation bzw. einer Tranche:
  - Ungeachtet der jederzeit bestehenden Möglichkeit des EZ, seinen Stromabnahmevertrag schriftlich zu kündigen, darf der LFA eine nach diesem Use-Case gemeldete Kündigung nicht allein unter Berufung auf die fehlende Einhaltung einer vertraglich vereinbarten Form zurückweisen. In diesem Fall hat er eine Kündigung auch in elektronischer Form unter Anwendung dieses Use-Case entgegenzunehmen und zu bearbeiten.
  - Hinweis: Der Use-Case behandelt nicht den Fall, dass der EZ selbst gegenüber dem LFA den Stromabnahmevertrag kündigt. Wenn der EZ vorab selbst kündigt, ist der Use-Case „[Lieferende von LF an NB](/prozessdoku/202610/LF/GPKE-Teil2-lieferende-von-lf-an-nb)“ vom LFA gegenüber dem NB unmittelbar mit Verfassen der Kündigungsbestätigung an den EZ anzustoßen.
- Im Sinne eines reibungslosen Wechselprozesses und zur Vermeidung von späteren Klärungsfällen empfiehlt es sich, den Use-Case „Kündigung“ generell einem Use-Case „[Lieferbeginn](/prozessdoku/202610/LF--LFN/GPKE-Teil2-lieferbeginn)“ vorzuschalten.

</li>

<li data-blatt="anlass">

### Anlass

- Im Fall einer verbrauchenden Marktlokation: Der LFN erhält vom Letztverbraucher den Auftrag zur Kündigung des bestehenden Stromliefervertrags.
- Im Fall einer erzeugenden Marktlokation bzw. einer Tranche: Der LFN erhält vom EZ den Auftrag zur Kündigung des bestehenden Stromabnahmevertrags.

**Vorher läuft:** [Ermittlung der MaLo-ID der Marktlokation](/prozessdoku/202610/LF/GPKE-Teil2-ermittlung-der-malo-id-der-marktlokation) — diese Prozesse nennen den hier gezeigten in ihrem Ergebnis.

</li>

<li data-blatt="erste-nachricht">

### Erste Nachricht

Der Beteiligte dieser Seite sendet selbst: „Kündigung“ an **LFA** (Schritt 1).

</li>

<li data-blatt="ziel">

### Ziel

- Der zwischen Letztverbraucher und LFA abgeschlossene Stromliefervertrag für die genannte, verbrauchende Marktlokation ist gekündigt bzw.
- der zwischen EZ und LFA abgeschlossene Stromabnahmevertrag für die genannte erzeugende Marktlokation bzw. die genannte Tranche ist gekündigt.

</li>

</ol>
</Stepper>

<a id="abschnitt-sichten"></a>

## Andere Sichten des Prozesses

Derselbe Prozess, aus den Augen der anderen Beteiligten: dieselben Schritte, jeweils aus deren Sicht gelesen.

- [Sicht LFA](/prozessdoku/202610/LF--LFA/GPKE-Teil2-kuendigung) — der abgebende Lieferant · Marktrolle LF

<Hinweisbereich>

*Die Schritte sind die **möglichen** Nachrichten dieses Prozesses, keine Abfolge — die Quelle führt weder Bedingungen noch Alternativen. Das Kästchen am Schritt nennt links die eigene Sicht: **←** empfängt sie, **→** sendet sie. Zugeklappte Schritte laufen zwischen anderen Marktpartnern.*

Zu den Prüfidentifikatoren dieser Schritte liegt kein Testfall im Testbestand; der Knopf »Ausprobieren« der schreibenden Schnittstelle bietet deshalb keinen Rumpf an.

Betrifft: [1](#schritt-1)

</Hinweisbereich>
