# Stornieren der Unterbrechung und Wiederherstellung der Anschlussnutzung auf Anweisung des LF — Sicht LF

<Kopf rolle="LF" beteiligter="LF" festlegung="GPKE" dokument="GPKE Teil 2" kapitel="3.5.3.2" sparte="Strom" schritte={3} suchtitel="Stornieren der Unterbrechung und Wiederherstellung der Anschlussnutzung auf Anweisung des LF — Sicht LF · GPKE Teil 2 · Formatversion 202610" abschnitte={[{"id": "abschnitt-ablauf", "label": "Prozessablauf"}, {"id": "abschnitt-schritte", "label": "Prozessschritte"}, {"id": "abschnitt-informationen", "label": "Prozess-Informationen"}, {"id": "abschnitt-sichten", "label": "Andere Sichten des Prozesses"}]} />

<Kurzfassung>

Der LF sendet
- eine Stornierung des Auftrags zur Sperrung (Fall a) oder
- eine Stornierung des Auftrags zur Entsperrung (Fall b) einer Marktlokation, so dass
- die Anschlussnutzung an der Marktlokation weiterhin möglich ist (erfolgreiche Stornierung von Fall a) bzw.
- die Marktlokation weiterhin gesperrt bleibt (erfolgreiche Stornierung von Fall b). Sofern der MSB bereits eingebunden war, ist dieser ebenfalls zu informieren.

</Kurzfassung>

<a id="abschnitt-ablauf"></a>

## Prozessablauf aus Sicht des LF

<Systembild svg={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1004 526\" width=\"1004\" height=\"526\" role=\"img\" aria-labelledby=\"sb-title\" class=\"maco-systembild\">\n<title id=\"sb-title\">Systembild: Stornieren der Unterbrechung und Wiederherstellung der Anschlussnutzung auf Anweisung des LF aus Sicht LF</title>\n<defs><marker id=\"sb-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect class=\"sb-lane-kopf\" x=\"16\" y=\"12\" width=\"232\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend-System des Kunden</text>\n<rect class=\"sb-lane-kopf\" x=\"398\" y=\"12\" width=\"264\" height=\"46\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · LF</text>\n<rect class=\"sb-lane-kopf\" x=\"812\" y=\"12\" width=\"176\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"900\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Marktpartner</text>\n<line x1=\"323\" y1=\"58\" x2=\"323\" y2=\"514\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"737\" y1=\"58\" x2=\"737\" y2=\"514\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect class=\"sb-kasten sb-trigger\" x=\"432\" y=\"80\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessauslöser empfangen</text>\n<rect class=\"sb-kasten sb-backend sb-trigger\" x=\"34\" y=\"80\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">2 Ereignisse, alternativ</text>\n<line x1=\"230\" y1=\"96\" x2=\"432\" y2=\"96\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"88\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"144\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"164\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">1. Stornierung</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"113\" x2=\"530\" y2=\"144\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"142\" r=\"5\"/><line x1=\"900\" y1=\"147\" x2=\"900\" y2=\"159\"/><line x1=\"893\" y1=\"151\" x2=\"907\" y2=\"151\"/><line x1=\"900\" y1=\"159\" x2=\"894\" y2=\"169\"/><line x1=\"900\" y1=\"159\" x2=\"906\" y2=\"169\"/></g>\n<text x=\"900\" y=\"191\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"628\" y1=\"160\" x2=\"878\" y2=\"160\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"152\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"176\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">39000</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"227\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"247\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"177\" x2=\"530\" y2=\"227\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"227\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"247\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"243\" x2=\"230\" y2=\"243\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"235\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"291\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"311\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">2. Antwort auf Stornierung</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"260\" x2=\"530\" y2=\"291\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"289\" r=\"5\"/><line x1=\"900\" y1=\"294\" x2=\"900\" y2=\"306\"/><line x1=\"893\" y1=\"298\" x2=\"907\" y2=\"298\"/><line x1=\"900\" y1=\"306\" x2=\"894\" y2=\"316\"/><line x1=\"900\" y1=\"306\" x2=\"906\" y2=\"316\"/></g>\n<text x=\"900\" y=\"338\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"878\" y1=\"307\" x2=\"628\" y2=\"307\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"299\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"323\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">19128, 19129</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"374\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"394\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z33</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"324\" x2=\"530\" y2=\"374\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"438\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"458\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"407\" x2=\"530\" y2=\"438\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"438\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"458\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"454\" x2=\"230\" y2=\"454\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"446\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n</svg>"} gesamt={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 974 486\" width=\"974\" height=\"486\" role=\"img\" aria-labelledby=\"sd-title\" class=\"maco-sequence\">\n<title id=\"sd-title\">Sequenzdiagramm: Stornieren der Unterbrechung und Wiederherstellung der Anschlussnutzung auf Anweisung des LF aus Sicht LF</title>\n<defs><marker id=\"sd-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect x=\"16\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"121\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend (Kunde)</text>\n<line x1=\"121\" y1=\"64\" x2=\"121\" y2=\"474\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"260\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"365\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · LF</text>\n<line x1=\"365\" y1=\"64\" x2=\"365\" y2=\"474\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"504\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"609\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"609\" y1=\"64\" x2=\"609\" y2=\"474\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"748\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"853\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">MSB</text>\n<line x1=\"853\" y1=\"64\" x2=\"853\" y2=\"474\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"121\" y1=\"90\" x2=\"365\" y2=\"90\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"81\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">2 Ereignisse, alternativ</text>\n<text x=\"243\" y=\"105\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Trigger-Event</text>\n<line x1=\"365\" y1=\"152\" x2=\"609\" y2=\"152\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"143\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">1. Stornierung</text>\n<text x=\"487\" y=\"167\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 39000</text>\n<line x1=\"365\" y1=\"214\" x2=\"121\" y2=\"214\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"205\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"229\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"609\" y1=\"276\" x2=\"365\" y2=\"276\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"267\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">2. Antwort auf Stornierung</text>\n<text x=\"487\" y=\"291\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 19128, 19129 · E_0468</text>\n<text x=\"487\" y=\"304\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0468 — Stornierung prüfen</text>\n<line x1=\"365\" y1=\"338\" x2=\"121\" y2=\"338\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"329\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"353\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"609\" y1=\"400\" x2=\"853\" y2=\"400\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"731\" y=\"391\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">3. Weiterleitung der Stornierung</text>\n<text x=\"731\" y=\"415\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 39001</text>\n</svg>"} titel="LF" />

<a id="abschnitt-schritte"></a>

## Prozessschritte

<Schritt nr="1" anker="schritt-1" richtung="ausgehend" kopf={{"links": {"label": "LF", "eigen": true}, "rechts": {"label": "NB"}}}>

### Stornierung

<Schrittskizze sicht={{"label": "LF"}} zeilen={[{"art": "ausloeser", "werte": ["START_STORNO_AUFTRAG", "START_STORNO_SE_AUFTRAG"]}, {"art": "senden", "label": "NB", "weg": "AS4", "nachrichten": [{"nr": "39000", "titel": "Stornierung Sperr-/Entsperrauftrag"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [39000](/schnittstellen/202610/pruefi/ORDCHG/PI_39000) — Stornierung Sperr-/Entsperrauftrag · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="ausloeser">

**Prozessauslöser**
- [`START_STORNO_AUFTRAG`](/schnittstellen/202610/trigger/events/LF-START_STORNO_AUFTRAG) · [Im Playground ausprobieren](/api/202610/ausloeser-lf/start-storno-auftrag)
- [`START_STORNO_SE_AUFTRAG`](/schnittstellen/202610/trigger/events/LF-START_STORNO_SE_AUFTRAG) · [Im Playground ausprobieren](/api/202610/ausloeser-lf/start-storno-se-auftrag)

Das Backend stößt diesen Schritt mit einem dieser Ereignisse an.

</li>

<li data-teil="nachricht">

Nachricht an **NB** · AS4

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202610/backend-schreiben-lf/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": false, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"ANFRAGE\": [\n      {\n        \"anfragekategorie\": \"ENTSPERRUNG\",\n        \"boTyp\": \"ANFRAGE\",\n        \"storno\": true,\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9900496000001\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"auftragsReferenz\": \"BGMM2T7DSBY\",\n    \"datenaustauschreferenz\": \"M48RTTM6\",\n    \"dokumentennummer\": \"BGMM3XEABD2\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9900496000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"Z52\",\n    \"nachrichtendatum\": \"2026-10-01T11:00:00Z\",\n    \"nachrichtenfunktion\": \"1\",\n    \"nachrichtenreferenznummer\": \"UNHM3QWZ6ZB\",\n    \"pruefidentifikator\": \"39000\",\n    \"sparte\": \"STROM\"\n  },\n  \"zusatzdaten\": {}\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend fort, nachdem die Nachricht erstellt ist.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="2" anker="schritt-2" richtung="eingehend" kopf={{"links": {"label": "LF", "eigen": true}, "rechts": {"label": "NB"}}}>

### Antwort auf Stornierung

<Schrittskizze sicht={{"label": "LF"}} zeilen={[{"art": "empfangen", "label": "NB", "weg": "AS4", "nachrichten": [{"nr": "19128", "titel": "Bestätigung Stornierung Sperr-/Entsperrauftrag"}, {"nr": "19129", "titel": "Ablehnung Stornierung Sperr-/Entsperrauftrag"}]}, {"art": "aperak", "werte": ["Z33"]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [19128](/schnittstellen/202610/pruefi/ORDRSP/PI_19128) — Bestätigung Stornierung Sperr-/Entsperrauftrag · AS4
- [19129](/schnittstellen/202610/pruefi/ORDRSP/PI_19129) — Ablehnung Stornierung Sperr-/Entsperrauftrag · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **NB** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `19128`, `19129` → [E_0468](/referenz/202610/ebd/E_0468) · NB · Stornierung prüfen

</div>

</li>

<li data-teil="aperak">

**Aperak-Prüfungen**
- `19128`, `19129` → `Z33` — Aperak Prüfung: Ist referenzierte Nachricht bekannt ?

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202610/backend-schreiben-lf/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": false, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"ANFRAGE\": [\n      {\n        \"anfragekategorie\": \"SPERRUNG\",\n        \"boTyp\": \"ANFRAGE\",\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9900327000009\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"antwortstatus\": \"A04\",\n    \"antwortstatusCodeliste\": \"E_0468\",\n    \"datenaustauschreferenz\": \"DAFDPMFOIKVPQS\",\n    \"dokumentennummer\": \"DA732411200727379903323000007169554\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9979015000001\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"Z51\",\n    \"nachrichtendatum\": \"2026-10-01T11:00:00Z\",\n    \"nachrichtenreferenznummer\": \"DAMSTEKKECNMTB\",\n    \"pruefidentifikator\": \"19128\",\n    \"sparte\": \"STROM\",\n    \"vorgangsreferenznummer\": \"REF32412\"\n  },\n  \"zusatzdaten\": {}\n}"} examples={[{"mediaType": "application/json", "examples": [{"name": "19128", "summary": "19128 — Bestätigung Stornierung Sperr-/Entsperrauftrag", "value": {"stammdaten": {"ANFRAGE": [{"boTyp": "ANFRAGE", "versionStruktur": "1", "anfragekategorie": "SPERRUNG"}]}, "transaktionsdaten": {"datenaustauschreferenz": "DAFDPMFOIKVPQS", "sparte": "STROM", "pruefidentifikator": "19128", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9900327000009", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9979015000001", "rollencodetyp": "BDEW"}, "dokumentennummer": "DA732411200727379903323000007169554", "kategorie": "Z51", "nachrichtendatum": "2026-10-01T11:00:00Z", "nachrichtenreferenznummer": "DAMSTEKKECNMTB", "vorgangsreferenznummer": "REF32412", "antwortstatus": "A04", "antwortstatusCodeliste": "E_0468"}, "zusatzdaten": {}}}, {"name": "19129", "summary": "19129 — Ablehnung Stornierung Sperr-/Entsperrauftrag", "value": {"stammdaten": {"ANFRAGE": [{"boTyp": "ANFRAGE", "versionStruktur": "1", "anfragekategorie": "SPERRUNG"}]}, "transaktionsdaten": {"datenaustauschreferenz": "DARRMSWPWFCUFR", "sparte": "STROM", "pruefidentifikator": "19129", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9900327000009", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9979015000001", "rollencodetyp": "BDEW"}, "dokumentennummer": "DA462411200729119903323000007362119", "kategorie": "Z51", "nachrichtendatum": "2026-10-01T11:00:00Z", "nachrichtenreferenznummer": "DAHABOXNVNJSQH", "vorgangsreferenznummer": "REF32412", "antwortstatus": "A02", "antwortstatusCodeliste": "E_0468"}, "zusatzdaten": {}}}]}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend mit den Daten der eingegangenen Nachricht fort.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="3" anker="schritt-3" richtung="fremd" kopf={{"links": {"label": "NB", "eigen": false}, "rechts": {"label": "MSB"}}}>

### Weiterleitung der Stornierung

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [39001](/schnittstellen/202610/pruefi/ORDCHG/PI_39001) — Weiterleitung der Stornierung · AS4

</div>

</Schritt>

<details>
<summary>Entscheidungsbäume dieses Prozesses</summary>

| EBD | Name |
|---|---|
| [E_0468](/referenz/202610/ebd/E_0468) | Stornierung prüfen |

</details>

<a id="abschnitt-informationen"></a>

## Prozess-Informationen

Wortlaut der Lesefassung, Steckbrief Kap. 3.5.3.1, S. 111–112.

<Stepper>
<ol>

<li data-blatt="vorbedingungen">

### Vorbedingungen

- Die betroffene Marktlokation ist dem LF zugeordnet.
- Der LF hat den NB nach Maßgabe des zwischen LF und NB geschlossen Netznutzungsvertrags (Lieferantenrahmenvertrags) beauftragt, die Anschlussnutzung an der genannten Marktlokation des vom LF belieferten AN
  - zu unterbrechen (Fall a: Use-Case „[Unterbrechung der Anschlussnutzung (Sperren) auf Anweisung des LF](/prozessdoku/202610/LF/GPKE-Teil2-unterbrechung-der-anschlussnutzung-sperren-auf-anweisung-des-lf)“) oder
  - zu entsperren (Fall b: Use-Case „[Wiederherstellung der Anschlussnutzung (Entsperren) auf Anweisung des LF](/prozessdoku/202610/LF/GPKE-Teil2-wiederherstellung-der-anschlussnutzung-entsperren-auf-anweisung-des-lf)“).
- Es handelt sich somit um eine verbrauchende Marktlokation.
- Der Grund für den Sperrauftrag bzw. Entsperrauftrag ist entfallen, da z. B. der Kunde die Forderung des LF ausgeglichen hat oder der LF den Widerspruch des AN akzeptiert hat.
- Die Unterbrechung der Anschlussnutzung (Fall a) oder Wiederherstellung der Anschlussnutzung (Fall b) über die betroffene Marktlokation ist bislang noch nicht erfolgt.

</li>

<li data-blatt="ergebnisse">

### Ergebnisse

- Die Anschlussnutzung über die betroffene Marktlokation ist weiterhin möglich (erfolgreiche Stornierung von Fall a: Sperrauftrag wurde erfolgreich storniert) oder
- die Marktlokation ist weiterhin gesperrt (erfolgreiche Stornierung von Fall b: Entsperrauftrag wurde erfolgreich storniert).

</li>

<li data-blatt="fehlerfall">

### Fehlerfall

#### Ergebnis im Fehlerfall

- Bei erfolgloser Stornierung von Fall a:
  - Um die Sperrung der Marktlokation aufzuheben, startet der LF den Use-Case „[Wiederherstellung der Anschlussnutzung (Entsperren) auf Anweisung des LF](/prozessdoku/202610/LF/GPKE-Teil2-wiederherstellung-der-anschlussnutzung-entsperren-auf-anweisung-des-lf)“ (Fall b).
- Bei erfolgloser Stornierung von Fall b:
  - Für die Sperrung der Marktlokation, startet der LF den Use-Case „[Unterbrechung der Anschlussnutzung (Sperren) auf Anweisung des LF](/prozessdoku/202610/LF/GPKE-Teil2-unterbrechung-der-anschlussnutzung-sperren-auf-anweisung-des-lf)“ (Fall a).

</li>

<li data-blatt="anforderungen">

### Weitere Anforderungen

- Die Stornierung eines Auftrags kann jederzeit durch den LF unabhängig des Status beim NB erfolgen, solange der Sperrauftrag bzw. Entsperrauftrag vom NB beim AN noch nicht durchgeführt wurde.
- Bei einer erfolgreichen Stornierung eines Sperrauftrags wird der Use-Case „[Unterbrechung der Anschlussnutzung (Sperren) auf Anweisung des LF](/prozessdoku/202610/LF/GPKE-Teil2-unterbrechung-der-anschlussnutzung-sperren-auf-anweisung-des-lf)“ mit dem SD-Schritt "ref Abrechnung einer sonstigen Leistung" fortgesetzt, um die bis dahin ggf. angefallenen Leistungen abrechnen zu können.

</li>

<li data-blatt="erste-nachricht">

### Erste Nachricht

Der Beteiligte dieser Seite sendet selbst: „Stornierung“ an **NB** (Schritt 1).

</li>

<li data-blatt="ziel">

### Ziel

Der LF storniert einen Auftrag zur Sperrung oder Entsperrung einer Marktlokation, bevor dieser vom NB ausgeführt wurde.

</li>

</ol>
</Stepper>

<a id="abschnitt-sichten"></a>

## Andere Sichten des Prozesses

Derselbe Prozess, aus den Augen der anderen Beteiligten: dieselben Schritte, jeweils aus deren Sicht gelesen.

- [Sicht NB](/prozessdoku/202610/NB/GPKE-Teil2-stornieren-der-unterbrechung-und-wiederherstellung-der-anschlussnutzung-auf-anweisung-des-lf) — NB
- [Sicht MSB](/prozessdoku/202610/MSB/GPKE-Teil2-stornieren-der-unterbrechung-und-wiederherstellung-der-anschlussnutzung-auf-anweisung-des-lf) — MSB

<Hinweisbereich>

*Die Schritte sind die **möglichen** Nachrichten dieses Prozesses, keine Abfolge — die Quelle führt weder Bedingungen noch Alternativen. Das Kästchen am Schritt nennt links die eigene Sicht: **←** empfängt sie, **→** sendet sie. Zugeklappte Schritte laufen zwischen anderen Marktpartnern.*

</Hinweisbereich>
