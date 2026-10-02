# Bestellung Beendigung einer Konfiguration vom NB an MSB — Sicht NB

<Kopf rolle="NB" beteiligter="NB" festlegung="GPKE" dokument="GPKE Teil 3" kapitel="1.3.5.2" sparte="Strom" schritte={4} suchtitel="Bestellung Beendigung einer Konfiguration vom NB an MSB — Sicht NB · GPKE Teil 3 · Formatversion 202610" abschnitte={[{"id": "abschnitt-ablauf", "label": "Prozessablauf"}, {"id": "abschnitt-schritte", "label": "Prozessschritte"}, {"id": "abschnitt-informationen", "label": "Prozess-Informationen"}, {"id": "abschnitt-sichten", "label": "Andere Sichten des Prozesses"}]} />

<Kurzfassung>

Der NB bzw. LF bestellt beim MSB der direkt betroffenen Lokation eine Beendigung einer Konfiguration für die direkt betroffene Lokation. Sofern weitere Lokationen der direkt betroffenen Lokation von der Beendigung der Konfiguration betroffen sind, gibt der NB bzw. LF diese weiter betroffenen Lokationen in der Bestellung ebenfalls an (möchte der LF z.B. keine eigene Zählzeitdefinition des LF mehr anwenden, hat der LF in der Bestellung zur Beendigung der entsprechenden Konfiguration auf der Ebene der Marktlokation, neben der Marktlokation auch die Beendigung für alle Messlokationen der Marktlokation zu bestellen). Der MSB prüft die Bestellung. Ist die Beendigung der Konfiguration für die betroffenen Lokationen grundsätzlich möglich, bestätigt der MSB dem NB bzw. LF die Bestellung, andernfalls lehnt er die Bestellung ab. Sofern weitere Lokationen der direkt betroffenen Lokation von der Beendigung der Konfiguration betroffen sind, für die der MSB der direkt betroffenen Lokation nicht den Messstellenbetrieb durchführt, bindet er für diese weiter betroffenen Lokationen die jeweiligen weiteren MSB ein. Über diesen Use-Case kann auch ein weiterer MSB eine Beendigung einer Konfiguration beim MSB der direkt betroffenen Lokation bestellen. Ist die Beendigung der Konfiguration für die betroffenen Lokationen grundsätzlich möglich, bestätigt der MSB der direkt betroffenen Lokation dem weiteren MSB die Bestellung, bindet ggf. weiter betroffene MSB mit ein und informiert den NB bzw. LF über die Beendigung der Konfiguration.

</Kurzfassung>

<a id="abschnitt-ablauf"></a>

## Prozessablauf aus Sicht des NB

<Systembild svg={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1004 542\" width=\"1004\" height=\"542\" role=\"img\" aria-labelledby=\"sb-title\" class=\"maco-systembild\">\n<title id=\"sb-title\">Systembild: Bestellung Beendigung einer Konfiguration vom NB an MSB aus Sicht NB</title>\n<defs><marker id=\"sb-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect class=\"sb-lane-kopf\" x=\"16\" y=\"12\" width=\"232\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend-System des Kunden</text>\n<rect class=\"sb-lane-kopf\" x=\"398\" y=\"12\" width=\"264\" height=\"46\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · NB</text>\n<rect class=\"sb-lane-kopf\" x=\"812\" y=\"12\" width=\"176\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"900\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Marktpartner</text>\n<line x1=\"323\" y1=\"58\" x2=\"323\" y2=\"530\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"737\" y1=\"58\" x2=\"737\" y2=\"530\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect class=\"sb-kasten sb-lesen_verarbeitung\" x=\"432\" y=\"80\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Daten für die Verarbeitung</text>\n<text x=\"530\" y=\"115\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">laden</text>\n<rect class=\"sb-kasten sb-backend sb-lesen_verarbeitung\" x=\"34\" y=\"80\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">2 Lese-Schnittstellen</text>\n<text x=\"132\" y=\"115\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">aufgerufen</text>\n<line x1=\"432\" y1=\"104\" x2=\"230\" y2=\"104\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"96\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<text x=\"331\" y=\"120\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">je einzeln am Schritt</text>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"154\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"174\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">1. Bestellung Beendigung</text>\n<text x=\"530\" y=\"189\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">einer Konfiguration auf</text>\n<text x=\"530\" y=\"204\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Ebene der dir…</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"128\" x2=\"530\" y2=\"154\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"167\" r=\"5\"/><line x1=\"900\" y1=\"172\" x2=\"900\" y2=\"184\"/><line x1=\"893\" y1=\"176\" x2=\"907\" y2=\"176\"/><line x1=\"900\" y1=\"184\" x2=\"894\" y2=\"194\"/><line x1=\"900\" y1=\"184\" x2=\"906\" y2=\"194\"/></g>\n<text x=\"900\" y=\"216\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">MSB</text>\n<line x1=\"628\" y1=\"185\" x2=\"878\" y2=\"185\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"177\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"201\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">17129</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"243\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"263\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"217\" x2=\"530\" y2=\"243\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"243\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"263\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"259\" x2=\"230\" y2=\"259\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"251\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"307\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"327\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">2. Antwort auf Bestellung</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"276\" x2=\"530\" y2=\"307\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"305\" r=\"5\"/><line x1=\"900\" y1=\"310\" x2=\"900\" y2=\"322\"/><line x1=\"893\" y1=\"314\" x2=\"907\" y2=\"314\"/><line x1=\"900\" y1=\"322\" x2=\"894\" y2=\"332\"/><line x1=\"900\" y1=\"322\" x2=\"906\" y2=\"332\"/></g>\n<text x=\"900\" y=\"354\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">MSB</text>\n<line x1=\"878\" y1=\"323\" x2=\"628\" y2=\"323\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"315\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"339\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">19131</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"390\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"410\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z33</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"340\" x2=\"530\" y2=\"390\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"454\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"474\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"423\" x2=\"530\" y2=\"454\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben sb-abgeleitet\" x=\"34\" y=\"454\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"474\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"470\" x2=\"230\" y2=\"470\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"462\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n</svg>"} gesamt={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 974 486\" width=\"974\" height=\"486\" role=\"img\" aria-labelledby=\"sd-title\" class=\"maco-sequence\">\n<title id=\"sd-title\">Sequenzdiagramm: Bestellung Beendigung einer Konfiguration vom NB an MSB aus Sicht NB</title>\n<defs><marker id=\"sd-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect x=\"16\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"121\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend (Kunde)</text>\n<line x1=\"121\" y1=\"64\" x2=\"121\" y2=\"474\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"260\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"365\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · NB</text>\n<line x1=\"365\" y1=\"64\" x2=\"365\" y2=\"474\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"504\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"609\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">MSB</text>\n<line x1=\"609\" y1=\"64\" x2=\"609\" y2=\"474\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"748\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"853\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">weiterer MSB</text>\n<line x1=\"853\" y1=\"64\" x2=\"853\" y2=\"474\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"365\" y1=\"90\" x2=\"609\" y2=\"90\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"81\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">1. Bestellung Beendigung einer Konfiguration auf…</text>\n<text x=\"487\" y=\"105\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 17129</text>\n<line x1=\"365\" y1=\"152\" x2=\"121\" y2=\"152\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"143\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"167\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"609\" y1=\"214\" x2=\"365\" y2=\"214\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"205\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">2. Antwort auf Bestellung</text>\n<text x=\"487\" y=\"229\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 19131 · E_0538</text>\n<text x=\"487\" y=\"242\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0538 — Bestellung Beendigung prüfen</text>\n<line x1=\"365\" y1=\"276\" x2=\"121\" y2=\"276\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"267\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"291\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"609\" y1=\"338\" x2=\"853\" y2=\"338\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"731\" y=\"329\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">3. Beendigung einer Konfiguration für weiter bet…</text>\n<text x=\"731\" y=\"353\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 17129, 17118</text>\n<line x1=\"853\" y1=\"400\" x2=\"609\" y2=\"400\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"731\" y=\"391\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">4. Antwort</text>\n<text x=\"731\" y=\"415\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 19131, 19127 · E_0539</text>\n<text x=\"731\" y=\"428\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0539 — Beendigung prüfen</text>\n</svg>"} titel="NB" />

<a id="abschnitt-schritte"></a>

## Prozessschritte

<Schritt nr="1" anker="schritt-1" richtung="ausgehend" kopf={{"links": {"label": "NB", "eigen": true}, "rechts": {"label": "MSB"}}}>

### Bestellung Beendigung einer Konfiguration auf Ebene der direkt betroffenen Lokation

<Schrittskizze sicht={{"label": "NB"}} zeilen={[{"art": "lesen_verarbeitung", "schnittstellen": [{"label": "LESEN_ANFRAGE_BASIS"}, {"label": "LESEN_AUFTRAG_BASIS"}]}, {"art": "senden", "label": "MSB", "weg": "AS4", "nachrichten": [{"nr": "17129", "titel": "Bestellung Beendigung einer Konfiguration"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [17129](/schnittstellen/202610/pruefi/ORDERS/PI_17129) — Bestellung Beendigung einer Konfiguration · AS4

</div>

**Ablauf**

<div data-ablauf data-offen="ja">

<Stepper>
<ol>

<li data-teil="lesen" data-stufe="verarbeitung">

**Daten für die Verarbeitung laden**
- `LESEN_ANFRAGE_BASIS`
- `LESEN_AUFTRAG_BASIS`

</li>

<li data-teil="nachricht">

Nachricht an **MSB** · AS4

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202610/backend-schreiben-nb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"ANFRAGE\": [\n      {\n        \"anfragekategorie\": \"BEENDIGUNG_EINER_KONFIGURATION\",\n        \"boTyp\": \"ANFRAGE\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"AUFTRAG\": [\n      {\n        \"ausfuehrungsdatum\": \"2026-08-29T22:00:00Z\",\n        \"boTyp\": \"AUFTRAG\",\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"marktrolle\": \"LF\",\n      \"rollencodenummer\": \"9903111000003\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"datenaustauschreferenz\": \"M0J5JXHB\",\n    \"dokumentennummer\": \"M0HJUOQJ\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9904629000006\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"nachrichtenReferenzBestellbestaetigung\": \"AS123\",\n    \"nachrichtendatum\": \"2026-10-01T11:00:00Z\",\n    \"nachrichtenreferenznummer\": \"M06YGP6N\",\n    \"pruefidentifikator\": \"17129\",\n    \"sparte\": \"STROM\",\n    \"vorgangsReferenzBestellbestaetigung\": \"45123\"\n  },\n  \"zusatzdaten\": {}\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend fort, nachdem die Nachricht erstellt ist.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="2" anker="schritt-2" richtung="eingehend" kopf={{"links": {"label": "NB", "eigen": true}, "rechts": {"label": "MSB"}}}>

### Antwort auf Bestellung

<Schrittskizze sicht={{"label": "NB"}} zeilen={[{"art": "empfangen", "label": "MSB", "weg": "AS4", "nachrichten": [{"nr": "19131", "titel": "Mitteilung zur Beendigung Konfiguration"}]}, {"art": "aperak", "werte": ["Z33"]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [19131](/schnittstellen/202610/pruefi/ORDRSP/PI_19131) — Mitteilung zur Beendigung Konfiguration · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **MSB** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `19131` → [E_0538](/referenz/202610/ebd/E_0538) · MSB · Bestellung Beendigung prüfen

</div>

</li>

<li data-teil="aperak">

**Aperak-Prüfungen**
- `19131` → `Z33`

</li>

<li data-teil="schnittstelle" data-art="fortschreiben" data-abgeleitet="ja">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202610/backend-schreiben-nb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend mit den Daten der eingegangenen Nachricht fort.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="3" anker="schritt-3" richtung="fremd" kopf={{"links": {"label": "MSB", "eigen": false}, "rechts": {"label": "weiterer MSB"}}}>

### Beendigung einer Konfiguration für weiter betroffene Lokationen

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [17129](/schnittstellen/202610/pruefi/ORDERS/PI_17129) — Bestellung Beendigung einer Konfiguration · AS4
- [17118](/schnittstellen/202610/pruefi/ORDERS/PI_17118) — Bestellung einer Konfigurationsänderung · AS4

</div>

</Schritt>

<Schritt nr="4" anker="schritt-4" richtung="fremd" kopf={{"links": {"label": "weiterer MSB", "eigen": false}, "rechts": {"label": "MSB"}}}>

### Antwort

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [19131](/schnittstellen/202610/pruefi/ORDRSP/PI_19131) — Mitteilung zur Beendigung Konfiguration · AS4
- [19127](/schnittstellen/202610/pruefi/ORDRSP/PI_19127) — Mitteilung zur Konfigurationsänderung · AS4

</div>

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `19131`, `19127` → [E_0539](/referenz/202610/ebd/E_0539) · MSB · Beendigung prüfen

</div>

</Schritt>

<details>
<summary>Entscheidungsbäume dieses Prozesses</summary>

| EBD | Name |
|---|---|
| [E_0538](/referenz/202610/ebd/E_0538) | Bestellung Beendigung prüfen |
| [E_0539](/referenz/202610/ebd/E_0539) | Beendigung prüfen |

</details>

<a id="abschnitt-informationen"></a>

## Prozess-Informationen

Wortlaut der Lesefassung, Steckbrief Kap. 1.3.5.1, S. 65–68.

<Stepper>
<ol>

<li data-blatt="vorbedingungen">

### Vorbedingungen

- Bei Bestellung der Beendigung einer Konfiguration vom NB an den MSB:
  - Bei der zu beendenden Konfiguration handelt es sich um eine Konfiguration, die
    - der NB über den Use-Case „Bestellung einer Konfiguration vom NB oder LF an MSB“ erfolgreich bestellt hat und
    - über diesen Use-Case zu beenden ist (z.B. Steuererlaubnis des NB).
  - Die Bestellung der Beendigung einer Konfiguration beinhaltet nur die Lokationen, die in der Bestellung des NB für diese nun zu beendende Konfiguration an den MSB enthalten waren.
- Bei Bestellung der Beendigung einer Konfiguration vom LF an den MSB:
  - Bei der zu beendenden Konfiguration handelt es sich um eine Konfiguration, die
    - der LF über den Use-Case „Bestellung einer Konfiguration vom NB oder LF an MSB“ erfolgreich bestellt hat und
    - über diesen Use-Case zu beenden ist (z.B. eine Steuererlaubnis des LF oder eine Konfiguration, die eine Zählzeitdefinition des LF enthält).
  - Die Bestellung der Beendigung einer Konfiguration beinhaltet nur die Lokationen, die in der Bestellung des LF für diese nun zu beendende Konfiguration an den MSB enthalten waren.
- Bei Bestellung der Beendigung einer Konfiguration vom weiteren MSB an den MSB:
  - Bei der zu beendenden Konfiguration handelt es sich um eine Konfiguration, die
    - über den Use-Case „Bestellung einer Konfiguration vom NB oder LF an MSB“ erfolgreich bestellt wurde und
    - über diesen Use-Case zu beenden ist (z.B. eine Steuererlaubnis oder eine Konfiguration, die eine Zählzeitdefinition des LF enthält).
  - Die Bestellung der Beendigung einer Konfiguration beinhaltet nur die Lokationen, die in der Bestellung des NB bzw. LF für diese nun zu beendende Konfiguration an den MSB enthalten waren.

</li>

<li data-blatt="ergebnisse">

### Ergebnisse

- Der MSB der jeweils betroffenen Lokation führt den Use-Case „Stammdatenänderung“ (hier: SD „[Stammdatenänderung vom MSB (verantwortlich) ausgehend](/prozessdoku/202610/NB/GPKE-Teil4-stammdatenaenderung-vom-msb-verantwortlich-ausgehend)“) (GPKE Teil 4) durch, sofern für die jeweilige Lokation eine Stammdatenänderung aufgrund der Beendigung der Konfiguration erforderlich ist.
- Im Fall einer kostenpflichtigen Konfiguration: Die Schlussrechnung kann über den Use-Case „Abrechnung Leistungen des Preisblatts A des MSB" vom MSB an den NB bzw. LF erfolgen.

</li>

<li data-blatt="fehlerfall">

### Fehlerfall

#### Ergebnis im Fehlerfall

Der NB bzw. LF bzw. weitere MSB prüft, ob eine erneute Beauftragung der Beendigung der Konfiguration erforderlich ist.

#### Fehlerfälle

- Bei der zu beendenden Konfiguration handelt es sich um eine Konfiguration, die
  - nicht über den Use-Case „Bestellung einer Konfiguration vom NB oder LF an MSB“ erfolgreich bestellt wurde oder
  - nicht über diesen Use-Case zu beenden ist.
- Die Bestellung der Beendigung einer Konfiguration beinhaltet nicht exakt die in der Bestellung des NB bzw. LF an den MSB enthaltenen Lokationen
- Der Marktpartner ist zum bestellten Ende des Wirkungszeitraums der betroffenen Lokation nicht zugeordnet.
- Es liegen nicht alle Parameter oder falsche Parameter für die Beendigung der Konfiguration vor.

</li>

<li data-blatt="anforderungen">

### Weitere Anforderungen

- Hinweis: Im Fall, dass der MSB der direkt betroffenen Lokation eine Konfiguration beenden möchte, beendet der MSB der direkt betroffenen Lokation die Konfiguration über den Use-Case „[Beendigung einer Konfiguration vom MSB](/prozessdoku/202610/NB/GPKE-Teil3-beendigung-einer-konfiguration-vom-msb)“.
- Bei Beendigung einer Übermittlung von Werten: Gehen nach dem Ende des Wirkungszeitraums beim MSB der direkt betroffenen Lokation bzw. NB bzw. LF Werte ein, sind diese Werte nicht zu verarbeiten.

</li>

<li data-blatt="anlass">

### Anlass

- Der NB bzw. LF bzw. weitere MSB hat den Bedarf einer Beendigung einer Konfiguration, die im Zuge dieses Use-Cases zu beenden ist. Dies kann z.B. sein:
- Im Fall der Bestellung einer Beendigung einer Konfiguration, die eine Zählzeitdefinition des LF enthält: Der LF möchte in der Bestellung mitteilen, dass eine bereits umgesetzte Zählzeitdefinition des LF für den Zählzeitenanwendungszweck „Endkunde“ mit der Zählzeitdefinition des NB mit dem Zählzeitenanwendungszweck „Netznutzung“ abgebildet werden soll. Dies ist z.B. dann der Fall, wenn der LF keine eigene Zählzeitdefinition des LF für den Zählzeitenanwendungszweck „Endkunde“ mehr nutzen möchte.
- Im Fall der Bestellung einer Beendigung durch einen weiteren MSB: Für eine von der Konfiguration betroffene Lokation, für die der weitere MSB den Messstellenbetrieb durchführt, ergibt sich z.B.:
  - Die vorhandene Gerätetechnik ermöglicht die Konfiguration zukünftig nicht mehr.
  - Der weitere MSB erhält im Rahmen des Use-Cases „[Beginn Messstellenbetrieb](/prozessdoku/202610/NB/WiM-Teil1-beginn-messstellenbetrieb)“ oder Use-Cases „[Verpflichtung gMSB](/prozessdoku/202610/NB/WiM-Teil1-verpflichtung-gmsb)“ (WiM Teil 1) vom NB die Information über die Neuzuordnung der Messlokation zu einem anderen MSB zu einem bestimmten Zeitpunkt.
  - Der Vertrag über die Durchführung des Messstellenbetriebs zwischen dem weiteren MSB und AN bzw. ANN wurde beendet.

</li>

<li data-blatt="erste-nachricht">

### Erste Nachricht

Der Beteiligte dieser Seite sendet selbst: „Bestellung Beendigung einer Konfiguration auf Ebene der direkt betroffenen Lokation“ an **MSB** (Schritt 1).

</li>

<li data-blatt="ziel">

### Ziel

Die Bestellung der Beendigung der Konfiguration (z.B. Messprodukt, Steuererlaubnis) für die betroffenen Lokationen (z.B. Messlokation, Marktlokation, Steuerbare Ressource, Netzlokation) wurde vom MSB der direkt betroffenen Lokation bestätigt.

</li>

</ol>
</Stepper>

<a id="abschnitt-sichten"></a>

## Andere Sichten des Prozesses

Derselbe Prozess, aus den Augen der anderen Beteiligten: dieselben Schritte, jeweils aus deren Sicht gelesen.

- [Sicht MSB](/prozessdoku/202610/MSB/GPKE-Teil3-bestellung-beendigung-einer-konfiguration-vom-nb-an-msb) — MSB
- [Sicht WMSB](/prozessdoku/202610/MSB--WMSB/GPKE-Teil3-bestellung-beendigung-einer-konfiguration-vom-nb-an-msb) — weiterer Messstellenbetreiber · Marktrolle MSB

<Hinweisbereich>

*Die Schritte sind die **möglichen** Nachrichten dieses Prozesses, keine Abfolge — die Quelle führt weder Bedingungen noch Alternativen. Das Kästchen am Schritt nennt links die eigene Sicht: **←** empfängt sie, **→** sendet sie. Zugeklappte Schritte laufen zwischen anderen Marktpartnern.*

Welches Ereignis diese Schritte anstößt, benennt die Quelle noch nicht.

Betrifft: [1](#schritt-1)

Diese Lesezugriffe sind im API-Katalog dieser Formatversion nicht geführt; am Schritt steht deshalb nur ihr Kommando, ohne Adresse und ohne Knopf.

Betrifft: [1](#schritt-1)

Die Konnektortabelle führt für diese Schritte keinen Schreibaufruf. Abgeleitet aus dem Prozessverlauf: Die eigene Rolle war an diesem Prozess schon beteiligt, der Vorgang besteht also.

Betrifft: [2](#schritt-2)

Zu den Prüfidentifikatoren dieser Schritte liegt kein Testfall im Testbestand; der Knopf »Ausprobieren« der schreibenden Schnittstelle bietet deshalb keinen Rumpf an.

Betrifft: [2](#schritt-2)

</Hinweisbereich>
