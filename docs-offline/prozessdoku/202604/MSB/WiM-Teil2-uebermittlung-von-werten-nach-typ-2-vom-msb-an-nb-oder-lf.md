# Übermittlung von Werten nach Typ 2 vom MSB an NB oder LF — Sicht MSB

<Kopf rolle="MSB" beteiligter="MSB" festlegung="WiM" dokument="WiM Strom Teil 2" kapitel="3.2.2" sparte="Strom" schritte={2} suchtitel="Übermittlung von Werten nach Typ 2 vom MSB an NB oder LF — Sicht MSB · WiM Strom Teil 2 · Formatversion 202604" abschnitte={[{"id": "abschnitt-ablauf", "label": "Prozessablauf"}, {"id": "abschnitt-schritte", "label": "Prozessschritte"}, {"id": "abschnitt-informationen", "label": "Prozess-Informationen"}, {"id": "abschnitt-sichten", "label": "Andere Sichten des Prozesses"}]} />

<Kurzfassung>

Bei der Übermittlung von Werten aus dem Back-End-System: Der MSB der direkt betroffenen Lokation übermittelt die Werte der bestellten Konfiguration für die direkt betroffene Lokation an den NB bzw. LF. Sofern weitere Lokationen der direkt betroffenen Lokation von der Konfiguration betroffen sind, übermittelt der MSB der direkt betroffenen Lokation die Werte für die weiter betroffenen Lokationen ebenfalls an den NB bzw. LF. Bei der Übermittlung von Werten direkt aus dem iMS an den NB bzw. LF: Der MSB der direkt betroffenen Lokation (hier das iMS) übermittelt die Werte der bestellten Konfiguration für die direkt betroffene Lokation an den NB bzw. LF.

</Kurzfassung>

<a id="abschnitt-ablauf"></a>

## Prozessablauf aus Sicht des MSB

<Systembild svg={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1004 546\" width=\"1004\" height=\"546\" role=\"img\" aria-labelledby=\"sb-title\" class=\"maco-systembild\">\n<title id=\"sb-title\">Systembild: Übermittlung von Werten nach Typ 2 vom MSB an NB oder LF aus Sicht MSB</title>\n<defs><marker id=\"sb-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect class=\"sb-lane-kopf\" x=\"16\" y=\"12\" width=\"232\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend-System des Kunden</text>\n<rect class=\"sb-lane-kopf\" x=\"398\" y=\"12\" width=\"264\" height=\"46\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · MSB</text>\n<rect class=\"sb-lane-kopf\" x=\"812\" y=\"12\" width=\"176\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"900\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Marktpartner</text>\n<line x1=\"323\" y1=\"58\" x2=\"323\" y2=\"534\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"737\" y1=\"58\" x2=\"737\" y2=\"534\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect class=\"sb-kasten sb-trigger\" x=\"432\" y=\"80\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessauslöser empfangen</text>\n<rect class=\"sb-kasten sb-backend sb-trigger\" x=\"34\" y=\"72\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"92\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">START_ERHEBUNG_MESSWE</text>\n<text x=\"132\" y=\"107\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">RTE</text>\n<line x1=\"230\" y1=\"96\" x2=\"432\" y2=\"96\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"88\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"154\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"174\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">1. Werte an NB</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"113\" x2=\"530\" y2=\"154\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"152\" r=\"5\"/><line x1=\"900\" y1=\"157\" x2=\"900\" y2=\"169\"/><line x1=\"893\" y1=\"161\" x2=\"907\" y2=\"161\"/><line x1=\"900\" y1=\"169\" x2=\"894\" y2=\"179\"/><line x1=\"900\" y1=\"169\" x2=\"906\" y2=\"179\"/></g>\n<text x=\"900\" y=\"201\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"628\" y1=\"170\" x2=\"878\" y2=\"170\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"162\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"186\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">13027</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"237\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"257\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"187\" x2=\"530\" y2=\"237\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"237\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"257\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"253\" x2=\"230\" y2=\"253\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"245\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-trigger\" x=\"432\" y=\"301\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"321\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessauslöser empfangen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"270\" x2=\"530\" y2=\"301\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-trigger\" x=\"34\" y=\"293\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"313\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">START_ERHEBUNG_MESSWE</text>\n<text x=\"132\" y=\"328\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">RTE</text>\n<line x1=\"230\" y1=\"317\" x2=\"432\" y2=\"317\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"309\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"375\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"395\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">2. Werte an LF</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"334\" x2=\"530\" y2=\"375\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"373\" r=\"5\"/><line x1=\"900\" y1=\"378\" x2=\"900\" y2=\"390\"/><line x1=\"893\" y1=\"382\" x2=\"907\" y2=\"382\"/><line x1=\"900\" y1=\"390\" x2=\"894\" y2=\"400\"/><line x1=\"900\" y1=\"390\" x2=\"906\" y2=\"400\"/></g>\n<text x=\"900\" y=\"422\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">LF</text>\n<line x1=\"628\" y1=\"391\" x2=\"878\" y2=\"391\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"383\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"407\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">13027</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"458\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"478\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"408\" x2=\"530\" y2=\"458\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"458\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"478\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"474\" x2=\"230\" y2=\"474\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"466\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n</svg>"} gesamt={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 974 486\" width=\"974\" height=\"486\" role=\"img\" aria-labelledby=\"sd-title\" class=\"maco-sequence\">\n<title id=\"sd-title\">Sequenzdiagramm: Übermittlung von Werten nach Typ 2 vom MSB an NB oder LF aus Sicht MSB</title>\n<defs><marker id=\"sd-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect x=\"16\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"121\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend (Kunde)</text>\n<line x1=\"121\" y1=\"64\" x2=\"121\" y2=\"474\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"260\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"365\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · MSB</text>\n<line x1=\"365\" y1=\"64\" x2=\"365\" y2=\"474\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"504\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"609\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"609\" y1=\"64\" x2=\"609\" y2=\"474\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"748\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"853\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">LF</text>\n<line x1=\"853\" y1=\"64\" x2=\"853\" y2=\"474\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"121\" y1=\"90\" x2=\"365\" y2=\"90\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"81\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">START_ERHEBUNG_MESSWERTE</text>\n<text x=\"243\" y=\"105\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Trigger-Event</text>\n<line x1=\"365\" y1=\"152\" x2=\"609\" y2=\"152\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"143\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">1. Werte an NB</text>\n<text x=\"487\" y=\"167\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 13027</text>\n<line x1=\"365\" y1=\"214\" x2=\"121\" y2=\"214\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"205\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"229\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"121\" y1=\"276\" x2=\"365\" y2=\"276\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"267\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">START_ERHEBUNG_MESSWERTE</text>\n<text x=\"243\" y=\"291\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Trigger-Event</text>\n<line x1=\"365\" y1=\"338\" x2=\"853\" y2=\"338\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"609\" y=\"329\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">2. Werte an LF</text>\n<text x=\"609\" y=\"353\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 13027</text>\n<line x1=\"365\" y1=\"400\" x2=\"121\" y2=\"400\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"391\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"415\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n</svg>"} titel="MSB" />

<a id="abschnitt-schritte"></a>

## Prozessschritte

<Schritt nr="1" anker="schritt-1" richtung="ausgehend" kopf={{"links": {"label": "MSB", "eigen": true}, "rechts": {"label": "NB"}}}>

### Werte an NB

<Schrittskizze sicht={{"label": "MSB"}} zeilen={[{"art": "ausloeser", "werte": ["START_ERHEBUNG_MESSWERTE"]}, {"art": "senden", "label": "NB", "weg": "AS4", "nachrichten": [{"nr": "13027", "titel": "Werte nach Typ 2"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [13027](/schnittstellen/202604/pruefi/MSCONS/PI_13027) — Werte nach Typ 2 · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="ausloeser">

**Prozessauslöser** [`START_ERHEBUNG_MESSWERTE`](/schnittstellen/202604/trigger/events/MSB-START_ERHEBUNG_MESSWERTE) · [Im Playground ausprobieren](/api/202604/ausloeser-msb/start-erhebung-messwerte)

Das Backend stößt diesen Schritt mit diesem Ereignis an.

</li>

<li data-teil="nachricht">

Nachricht an **NB** · AS4

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202604/backend-schreiben-msb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"ENERGIEMENGE\": [\n      {\n        \"boTyp\": \"ENERGIEMENGE\",\n        \"energieverbrauch\": [\n          {\n            \"enddatum\": \"2024-08-02T04:00:00Z\",\n            \"messwertstatus\": \"ERSATZWERT\",\n            \"obiskennzahl\": \"1-0:1.29.0\",\n            \"position\": 1,\n            \"startdatum\": \"2023-12-22T05:00:00Z\",\n            \"wert\": 1223\n          }\n        ],\n        \"lokationsId\": \"50375312838\",\n        \"lokationsTyp\": \"MALO\",\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9979100000001\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"anfrageReferenz\": \"PP172409301012154888888888888563413\",\n    \"datenaustauschreferenz\": \"P1001099269230\",\n    \"dokumentennummer\": \"BGMM2B120EC\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9904400000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"Z83\",\n    \"nachrichtendatum\": \"2024-10-01T06:07:00Z\",\n    \"nachrichtenfunktion\": \"9\",\n    \"nachrichtenreferenznummer\": \"UNHM2BQ4A83\",\n    \"pruefidentifikator\": \"13027\",\n    \"sparte\": \"STROM\",\n    \"typ\": \"TL\"\n  },\n  \"zusatzdaten\": {}\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend fort, nachdem die Nachricht erstellt ist.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="2" anker="schritt-2" richtung="ausgehend" kopf={{"links": {"label": "MSB", "eigen": true}, "rechts": {"label": "LF"}}}>

### Werte an LF

<Schrittskizze sicht={{"label": "MSB"}} zeilen={[{"art": "ausloeser", "werte": ["START_ERHEBUNG_MESSWERTE"]}, {"art": "senden", "label": "LF", "weg": "AS4", "nachrichten": [{"nr": "13027", "titel": "Werte nach Typ 2"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [13027](/schnittstellen/202604/pruefi/MSCONS/PI_13027) — Werte nach Typ 2 · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="ausloeser">

**Prozessauslöser** [`START_ERHEBUNG_MESSWERTE`](/schnittstellen/202604/trigger/events/MSB-START_ERHEBUNG_MESSWERTE) · [Im Playground ausprobieren](/api/202604/ausloeser-msb/start-erhebung-messwerte)

Das Backend stößt diesen Schritt mit diesem Ereignis an.

</li>

<li data-teil="nachricht">

Nachricht an **LF** · AS4

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202604/backend-schreiben-msb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"ENERGIEMENGE\": [\n      {\n        \"boTyp\": \"ENERGIEMENGE\",\n        \"energieverbrauch\": [\n          {\n            \"enddatum\": \"2024-08-02T04:00:00Z\",\n            \"messwertstatus\": \"ERSATZWERT\",\n            \"obiskennzahl\": \"1-0:1.29.0\",\n            \"position\": 1,\n            \"startdatum\": \"2023-12-22T05:00:00Z\",\n            \"wert\": 1223\n          }\n        ],\n        \"lokationsId\": \"50375312838\",\n        \"lokationsTyp\": \"MALO\",\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9979100000001\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"anfrageReferenz\": \"PP172409301012154888888888888563413\",\n    \"datenaustauschreferenz\": \"P1001099269230\",\n    \"dokumentennummer\": \"BGMM2B120EC\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9904400000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"Z83\",\n    \"nachrichtendatum\": \"2024-10-01T06:07:00Z\",\n    \"nachrichtenfunktion\": \"9\",\n    \"nachrichtenreferenznummer\": \"UNHM2BQ4A83\",\n    \"pruefidentifikator\": \"13027\",\n    \"sparte\": \"STROM\",\n    \"typ\": \"TL\"\n  },\n  \"zusatzdaten\": {}\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend fort, nachdem die Nachricht erstellt ist.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<a id="abschnitt-informationen"></a>

## Prozess-Informationen

Wortlaut der Lesefassung, Steckbrief Kap. 3.2.1, S. 66–67.

<Stepper>
<ol>

<li data-blatt="vorbedingungen">

### Vorbedingungen

- Der Messstellenbetrieb wird an allen betroffenen Lokationen vom selben MSB durchgeführt; d.h. der MSB der direkt betroffenen Lokation ist der MSB aller ggf. weiter betroffenen Lokationen.
- Gegenüber dem NB gilt: Der NB hat über den Use-Case „Bestellung einer Konfiguration vom NB oder LF an MSB“ (GPKE Teil 3) eine Konfiguration bestellt und die Bestellung wurde vom MSB bestätigt.
- Gegenüber dem LF gilt: Der LF hat über den Use-Case „Bestellung einer Konfiguration vom NB oder LF an MSB“ (GPKE Teil 3) eine Konfiguration bestellt und die Bestellung wurde vom MSB bestätigt.

</li>

<li data-blatt="ergebnisse">

### Ergebnisse

Die Abrechnung über den Use-Case „Abrechnung Leistungen des Preisblatt A des MSB“ (GPKE Teil 3) kann ggü. dem NB bzw. LF erfolgen, sofern es sich um eine kostenpflichtige Konfiguration handelt.

</li>

<li data-blatt="fehlerfall">

### Fehlerfall

#### Ergebnis im Fehlerfall

Die Übermittlung von Werten kann nicht erbracht werden.

</li>

<li data-blatt="anforderungen">

### Weitere Anforderungen

Eine Reklamation der Konfiguration ist über den Use-Case „Reklamation einer Konfiguration“ (GPKE Teil 3) möglich.

</li>

<li data-blatt="anlass">

### Anlass

- Beginn des Wirkungszeitraums der bestellten Konfiguration.

</li>

<li data-blatt="erste-nachricht">

### Erste Nachricht

Der Beteiligte dieser Seite sendet selbst: „Werte an NB“ an **NB** (Schritt 1).

</li>

<li data-blatt="ziel">

### Ziel

Der NB bzw. LF erhält die Werte der bestellten Konfiguration für die betroffenen Lokationen (z.B. Messlokation, Marktlokation).

</li>

</ol>
</Stepper>

<a id="abschnitt-sichten"></a>

## Andere Sichten des Prozesses

Derselbe Prozess, aus den Augen der anderen Beteiligten: dieselben Schritte, jeweils aus deren Sicht gelesen.

- [Sicht LF](/prozessdoku/202604/LF/WiM-Teil2-uebermittlung-von-werten-nach-typ-2-vom-msb-an-nb-oder-lf) — LF
- [Sicht NB](/prozessdoku/202604/NB/WiM-Teil2-uebermittlung-von-werten-nach-typ-2-vom-msb-an-nb-oder-lf) — NB

<Hinweisbereich>

*Die Schritte sind die **möglichen** Nachrichten dieses Prozesses, keine Abfolge — die Quelle führt weder Bedingungen noch Alternativen. Das Kästchen am Schritt nennt links die eigene Sicht: **←** empfängt sie, **→** sendet sie. Zugeklappte Schritte laufen zwischen anderen Marktpartnern.*

</Hinweisbereich>
