# Bestellung einer Änderung von Abrechnungsdaten von LF an NB — Sicht LF

<Kopf rolle="LF" beteiligter="LF" festlegung="GPKE" dokument="GPKE Teil 2" kapitel="3.1.3.2" sparte="Strom" schritte={2} suchtitel="Bestellung einer Änderung von Abrechnungsdaten von LF an NB — Sicht LF · GPKE Teil 2 · Formatversion 202610" abschnitte={[{"id": "abschnitt-ablauf", "label": "Prozessablauf"}, {"id": "abschnitt-schritte", "label": "Prozessschritte"}, {"id": "abschnitt-informationen", "label": "Prozess-Informationen"}, {"id": "abschnitt-sichten", "label": "Andere Sichten des Prozesses"}]} />

<Kurzfassung>

Der LF bzw. ÜNB übermittelt dem NB die Bestellung einer Änderung von Abrechnungsdaten. Der NB prüft die Bestellung und teilt dem LF bzw. ÜNB den Bearbeitungsstand mit.

</Kurzfassung>

<a id="abschnitt-ablauf"></a>

## Prozessablauf aus Sicht des LF

<Systembild svg={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1004 674\" width=\"1004\" height=\"674\" role=\"img\" aria-labelledby=\"sb-title\" class=\"maco-systembild\">\n<title id=\"sb-title\">Systembild: Bestellung einer Änderung von Abrechnungsdaten von LF an NB aus Sicht LF</title>\n<defs><marker id=\"sb-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect class=\"sb-lane-kopf\" x=\"16\" y=\"12\" width=\"232\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend-System des Kunden</text>\n<rect class=\"sb-lane-kopf\" x=\"398\" y=\"12\" width=\"264\" height=\"46\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · LF</text>\n<rect class=\"sb-lane-kopf\" x=\"812\" y=\"12\" width=\"176\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"900\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Marktpartner</text>\n<line x1=\"323\" y1=\"58\" x2=\"323\" y2=\"662\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"737\" y1=\"58\" x2=\"737\" y2=\"662\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect class=\"sb-kasten sb-folge_ausloeser\" x=\"432\" y=\"80\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Ausgelöst durch Eingang:</text>\n<text x=\"530\" y=\"115\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">55126, 55218, 55672</text>\n<rect class=\"sb-kasten sb-trigger\" x=\"432\" y=\"154\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"174\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessauslöser empfangen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"128\" x2=\"530\" y2=\"154\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-trigger\" x=\"34\" y=\"154\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"174\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">2 Ereignisse, alternativ</text>\n<line x1=\"230\" y1=\"170\" x2=\"432\" y2=\"170\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"162\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-lesen_verarbeitung\" x=\"432\" y=\"218\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"238\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Daten für die Verarbeitung</text>\n<text x=\"530\" y=\"253\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">laden</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"187\" x2=\"530\" y2=\"218\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-lesen_verarbeitung\" x=\"34\" y=\"226\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"246\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Marktlokation lesen</text>\n<line x1=\"432\" y1=\"242\" x2=\"230\" y2=\"242\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"234\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"292\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"312\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">1. Bestellung einer Änderung</text>\n<text x=\"530\" y=\"327\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">von Abrechnungsdaten</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"266\" x2=\"530\" y2=\"292\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"298\" r=\"5\"/><line x1=\"900\" y1=\"303\" x2=\"900\" y2=\"315\"/><line x1=\"893\" y1=\"307\" x2=\"907\" y2=\"307\"/><line x1=\"900\" y1=\"315\" x2=\"894\" y2=\"325\"/><line x1=\"900\" y1=\"315\" x2=\"906\" y2=\"325\"/></g>\n<text x=\"900\" y=\"347\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"628\" y1=\"316\" x2=\"878\" y2=\"316\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"308\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"332\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">55156, 55220, 55673…</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"375\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"395\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"340\" x2=\"530\" y2=\"375\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"375\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"395\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"391\" x2=\"230\" y2=\"391\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"383\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"439\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"459\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">2. Bearbeitungsstand zur</text>\n<text x=\"530\" y=\"474\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Bestellung</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"408\" x2=\"530\" y2=\"439\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"445\" r=\"5\"/><line x1=\"900\" y1=\"450\" x2=\"900\" y2=\"462\"/><line x1=\"893\" y1=\"454\" x2=\"907\" y2=\"454\"/><line x1=\"900\" y1=\"462\" x2=\"894\" y2=\"472\"/><line x1=\"900\" y1=\"462\" x2=\"906\" y2=\"472\"/></g>\n<text x=\"900\" y=\"494\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"878\" y1=\"463\" x2=\"628\" y2=\"463\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"455\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"479\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">19133, 21047</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"522\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"542\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z33</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"487\" x2=\"530\" y2=\"522\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"586\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"606\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"555\" x2=\"530\" y2=\"586\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"586\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"606\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"602\" x2=\"230\" y2=\"602\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"594\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n</svg>"} gesamt={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 730 424\" width=\"730\" height=\"424\" role=\"img\" aria-labelledby=\"sd-title\" class=\"maco-sequence\">\n<title id=\"sd-title\">Sequenzdiagramm: Bestellung einer Änderung von Abrechnungsdaten von LF an NB aus Sicht LF</title>\n<defs><marker id=\"sd-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect x=\"16\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"121\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend (Kunde)</text>\n<line x1=\"121\" y1=\"64\" x2=\"121\" y2=\"412\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"260\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"365\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · LF</text>\n<line x1=\"365\" y1=\"64\" x2=\"365\" y2=\"412\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"504\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"609\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"609\" y1=\"64\" x2=\"609\" y2=\"412\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"121\" y1=\"90\" x2=\"365\" y2=\"90\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"81\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">2 Ereignisse, alternativ</text>\n<text x=\"243\" y=\"105\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Trigger-Event</text>\n<line x1=\"365\" y1=\"152\" x2=\"609\" y2=\"152\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"143\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">1. Bestellung einer Änderung von Abrechnungsdaten</text>\n<text x=\"487\" y=\"167\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55156, 55220, 55673…</text>\n<line x1=\"365\" y1=\"214\" x2=\"121\" y2=\"214\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"205\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"229\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"609\" y1=\"276\" x2=\"365\" y2=\"276\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"267\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">2. Bearbeitungsstand zur Bestellung</text>\n<text x=\"487\" y=\"291\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 19133, 21047 · E_0595</text>\n<text x=\"487\" y=\"304\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0595 — Bestellung prüfen</text>\n<line x1=\"365\" y1=\"338\" x2=\"121\" y2=\"338\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"329\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"353\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n</svg>"} titel="LF" />

<a id="abschnitt-schritte"></a>

## Prozessschritte

<Schritt nr="1" anker="schritt-1" richtung="ausgehend" kopf={{"links": {"label": "LF", "eigen": true}, "rechts": {"label": "NB"}}}>

### Bestellung einer Änderung von Abrechnungsdaten

<Schrittskizze sicht={{"label": "LF"}} zeilen={[{"art": "folge_ausloeser", "werte": ["55126", "55218", "55672"]}, {"art": "ausloeser", "werte": ["START_BESTELLUNG_ABRECHNUNGSDATEN", "START_BESTELLUNG_SDAE"]}, {"art": "lesen_verarbeitung", "schnittstellen": [{"label": "Marktlokation lesen"}]}, {"art": "senden", "label": "NB", "weg": "AS4", "nachrichten": [{"nr": "55156", "titel": "Rückmeldung/Anfrage Abr.-Daten BK-Abr. verb. MaLo"}, {"nr": "55220", "titel": "Rückmeldung/Anfrage Abr.-Daten NNA"}, {"nr": "55673", "titel": "Rückmeldung/Anfrage Abr.-Daten BK-Abr. erz. Malo"}, {"nr": "17133", "titel": "Bestellung Änderung Abrechnungsdaten"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55156](/schnittstellen/202610/pruefi/UTILMD/PI_55156) — Rückmeldung/Anfrage Abr.-Daten BK-Abr. verb. MaLo · AS4
- [55220](/schnittstellen/202610/pruefi/UTILMD/PI_55220) — Rückmeldung/Anfrage Abr.-Daten NNA · AS4
- [55673](/schnittstellen/202610/pruefi/UTILMD/PI_55673) — Rückmeldung/Anfrage Abr.-Daten BK-Abr. erz. Malo · AS4
- [17133](/schnittstellen/202610/pruefi/ORDERS/PI_17133) — Bestellung Änderung Abrechnungsdaten · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="folge_ausloeser">

**Ausgelöst durch Eingang**
- [55126](/schnittstellen/202610/pruefi/UTILMD/PI_55126)
- [55218](/schnittstellen/202610/pruefi/UTILMD/PI_55218)
- [55672](/schnittstellen/202610/pruefi/UTILMD/PI_55672)

Die MACO APP sendet diese Nachricht selbst, als Folgeprozess nach einem dieser Eingänge. Daneben kann das Backend diesen Schritt mit einem Ereignis anstoßen — der nächste Punkt.

</li>

<li data-teil="ausloeser">

**Prozessauslöser**
- [`START_BESTELLUNG_ABRECHNUNGSDATEN`](/schnittstellen/202610/trigger/events/LF-START_BESTELLUNG_ABRECHNUNGSDATEN) · [Im Playground ausprobieren](/api/202610/ausloeser-lf/start-bestellung-abrechnungsdaten)
- [`START_BESTELLUNG_SDAE`](/schnittstellen/202610/trigger/events/LF-START_BESTELLUNG_SDAE) · [Im Playground ausprobieren](/api/202610/ausloeser-lf/start-bestellung-sdae)

Das Backend stößt diesen Schritt mit einem dieser Ereignisse an.

</li>

<li data-teil="lesen" data-stufe="verarbeitung">

**Daten für die Verarbeitung laden**
- [Marktlokation lesen](/api/202610/backend-lesen/getmarketlocationbasic#marktlokation-lesen) `GET /getMarketLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getMarketLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": false, "defaultValue": "MALO", "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": false, "defaultValue": "2024-06-28T12:18:00Z", "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_MARKTLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

</li>

<li data-teil="nachricht">

Nachricht an **NB** · AS4

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202610/backend-schreiben-lf/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": false, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"BILANZIERUNG\": [\n      {\n        \"aggregationsverantwortung\": \"VNB\",\n        \"bilanzkreis\": \"11XBKA---------I\",\n        \"boTyp\": \"BILANZIERUNG\",\n        \"datenqualitaet\": \"ERWARTETE_DATEN\",\n        \"detailsPrognosegrundlage\": [\n          \"SLP_SEP\"\n        ],\n        \"gueltigkeitszeitraum\": {\n          \"enddatum\": \"2025-07-23T22:00:00Z\",\n          \"startdatum\": \"2025-06-23T22:00:00Z\",\n          \"zeitraumId\": 1\n        },\n        \"prognosegrundlage\": \"PROFILE\",\n        \"versionStruktur\": \"1\",\n        \"zeitreihentyp\": \"SLS\"\n      },\n      {\n        \"aggregationsverantwortung\": \"VNB\",\n        \"bilanzkreis\": \"11XBKA---------I\",\n        \"boTyp\": \"BILANZIERUNG\",\n        \"datenqualitaet\": \"ERWARTETE_DATEN\",\n        \"detailsPrognosegrundlage\": [\n          \"SLP_SEP\"\n        ],\n        \"gueltigkeitszeitraum\": {\n          \"startdatum\": \"2025-07-23T22:00:00Z\",\n          \"zeitraumId\": 2\n        },\n        \"prognosegrundlage\": \"PROFILE\",\n        \"versionStruktur\": \"1\",\n        \"zeitreihentyp\": \"SLS\"\n      }\n    ],\n    \"MARKTLOKATION\": [\n      {\n        \"bilanzierungsgebiet\": \"11YDE-DSONET---I\",\n        \"boTyp\": \"MARKTLOKATION\",\n        \"datenqualitaet\": \"ERWARTETE_DATEN\",\n        \"gueltigkeitszeitraum\": {\n          \"enddatum\": \"2025-07-23T22:00:00Z\",\n          \"startdatum\": \"2025-06-23T22:00:00Z\",\n          \"zeitraumId\": 1\n        },\n        \"marktlokationsId\": \"20072281644\",\n        \"marktlokationsTyp\": [\n          {\n            \"typ\": \"STANDARD_MARKTLOKATION\"\n          }\n        ],\n        \"marktrollen\": [\n          {\n            \"boTyp\": \"MARKTTEILNEHMER\",\n            \"gewerbekennzeichnung\": true,\n            \"marktrolle\": \"UENB\",\n            \"rollencodenummer\": \"9911835000001\",\n            \"rollencodetyp\": \"BDEW\",\n            \"versionStruktur\": \"1\"\n          }\n        ],\n        \"regelzone\": \"10YDE-TSONET---I\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      },\n      {\n        \"bilanzierungsgebiet\": \"11YDE-DSONET---I\",\n        \"boTyp\": \"MARKTLOKATION\",\n        \"datenqualitaet\": \"ERWARTETE_DATEN\",\n        \"gueltigkeitszeitraum\": {\n          \"startdatum\": \"2025-07-23T22:00:00Z\",\n          \"zeitraumId\": 2\n        },\n        \"marktlokationsId\": \"20072281644\",\n        \"marktlokationsTyp\": [\n          {\n            \"typ\": \"STANDARD_MARKTLOKATION\"\n          }\n        ],\n        \"marktrollen\": [\n          {\n            \"boTyp\": \"MARKTTEILNEHMER\",\n            \"gewerbekennzeichnung\": true,\n            \"marktrolle\": \"UENB\",\n            \"rollencodenummer\": \"9911835000001\",\n            \"rollencodetyp\": \"BDEW\",\n            \"versionStruktur\": \"1\"\n          }\n        ],\n        \"regelzone\": \"10YDE-TSONET---I\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"VERWENDUNGSZEITRAUM\": [\n      {\n        \"boTyp\": \"VERWENDUNGSZEITRAUM\",\n        \"datenqualitaet\": \"ERWARTETE_DATEN\",\n        \"versionStruktur\": \"1\",\n        \"verwendungAb\": \"2025-06-23T22:00:00Z\",\n        \"verwendungBis\": \"2025-07-23T22:00:00Z\",\n        \"zeitraumId\": 1\n      },\n      {\n        \"boTyp\": \"VERWENDUNGSZEITRAUM\",\n        \"datenqualitaet\": \"ERWARTETE_DATEN\",\n        \"versionStruktur\": \"1\",\n        \"verwendungAb\": \"2025-07-23T22:00:00Z\",\n        \"zeitraumId\": 2\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"ansprechpartner\": {\n        \"boTyp\": \"ANSPRECHPARTNER\",\n        \"nachname\": \"P GETTY\",\n        \"rufnummern\": [\n          {\n            \"nummerntyp\": \"RUF_DURCHWAHL\",\n            \"rufnummer\": \"+3222271020\"\n          }\n        ],\n        \"versionStruktur\": \"1\"\n      },\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9903729000007\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"anfragereferenznummer\": \"NNV1234\",\n    \"antwortStatusZeitraum\": [\n      {\n        \"code\": \"A02\",\n        \"liste\": \"E_0611\",\n        \"zeitraumId\": 1\n      },\n      {\n        \"code\": \"A02\",\n        \"liste\": \"E_0611\",\n        \"zeitraumId\": 2\n      }\n    ],\n    \"datenaustauschreferenz\": \"DANXAGAAOOBGLF\",\n    \"dokumentennummer\": \"DA582411070841339903323000007433702\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9900327000009\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"E03\",\n    \"nachrichtendatum\": \"2025-06-24T12:31:00Z\",\n    \"nachrichtenreferenznummer\": \"DAWIJLVJWSUDJK\",\n    \"pruefidentifikator\": \"55156\",\n    \"sparte\": \"STROM\",\n    \"transaktionsgrund\": \"ZX3\",\n    \"vorgangsnummer\": \"24062416225400000000000102159662011\"\n  },\n  \"zusatzdaten\": {}\n}"} examples={[{"mediaType": "application/json", "examples": [{"name": "55156", "summary": "55156 — Rückmeldung/Anfrage Abr.-Daten BK-Abr. verb. MaLo", "value": {"stammdaten": {"VERWENDUNGSZEITRAUM": [{"boTyp": "VERWENDUNGSZEITRAUM", "versionStruktur": "1", "zeitraumId": 1, "datenqualitaet": "ERWARTETE_DATEN", "verwendungAb": "2025-06-23T22:00:00Z", "verwendungBis": "2025-07-23T22:00:00Z"}, {"boTyp": "VERWENDUNGSZEITRAUM", "versionStruktur": "1", "zeitraumId": 2, "datenqualitaet": "ERWARTETE_DATEN", "verwendungAb": "2025-07-23T22:00:00Z"}], "MARKTLOKATION": [{"boTyp": "MARKTLOKATION", "versionStruktur": "1", "marktlokationsId": "20072281644", "marktlokationsTyp": [{"typ": "STANDARD_MARKTLOKATION"}], "sparte": "STROM", "gueltigkeitszeitraum": {"zeitraumId": 1, "startdatum": "2025-06-23T22:00:00Z", "enddatum": "2025-07-23T22:00:00Z"}, "datenqualitaet": "ERWARTETE_DATEN", "bilanzierungsgebiet": "11YDE-DSONET---I", "marktrollen": [{"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "marktrolle": "UENB", "gewerbekennzeichnung": true, "rollencodenummer": "9911835000001", "rollencodetyp": "BDEW"}], "regelzone": "10YDE-TSONET---I"}, {"boTyp": "MARKTLOKATION", "versionStruktur": "1", "marktlokationsId": "20072281644", "marktlokationsTyp": [{"typ": "STANDARD_MARKTLOKATION"}], "sparte": "STROM", "gueltigkeitszeitraum": {"zeitraumId": 2, "startdatum": "2025-07-23T22:00:00Z"}, "datenqualitaet": "ERWARTETE_DATEN", "bilanzierungsgebiet": "11YDE-DSONET---I", "marktrollen": [{"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "marktrolle": "UENB", "gewerbekennzeichnung": true, "rollencodenummer": "9911835000001", "rollencodetyp": "BDEW"}], "regelzone": "10YDE-TSONET---I"}], "BILANZIERUNG": [{"boTyp": "BILANZIERUNG", "versionStruktur": "1", "gueltigkeitszeitraum": {"zeitraumId": 1, "startdatum": "2025-06-23T22:00:00Z", "enddatum": "2025-07-23T22:00:00Z"}, "datenqualitaet": "ERWARTETE_DATEN", "bilanzkreis": "11XBKA---------I", "aggregationsverantwortung": "VNB", "zeitreihentyp": "SLS", "prognosegrundlage": "PROFILE", "detailsPrognosegrundlage": ["SLP_SEP"]}, {"boTyp": "BILANZIERUNG", "versionStruktur": "1", "gueltigkeitszeitraum": {"zeitraumId": 2, "startdatum": "2025-07-23T22:00:00Z"}, "datenqualitaet": "ERWARTETE_DATEN", "bilanzkreis": "11XBKA---------I", "aggregationsverantwortung": "VNB", "zeitreihentyp": "SLS", "prognosegrundlage": "PROFILE", "detailsPrognosegrundlage": ["SLP_SEP"]}]}, "transaktionsdaten": {"datenaustauschreferenz": "DANXAGAAOOBGLF", "sparte": "STROM", "transaktionsgrund": "ZX3", "vorgangsnummer": "24062416225400000000000102159662011", "pruefidentifikator": "55156", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9903729000007", "rollencodetyp": "BDEW", "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "nachname": "P GETTY", "rufnummern": [{"nummerntyp": "RUF_DURCHWAHL", "rufnummer": "+3222271020"}]}}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900327000009", "rollencodetyp": "BDEW"}, "dokumentennummer": "DA582411070841339903323000007433702", "kategorie": "E03", "nachrichtendatum": "2025-06-24T12:31:00Z", "nachrichtenreferenznummer": "DAWIJLVJWSUDJK", "anfragereferenznummer": "NNV1234", "antwortStatusZeitraum": [{"code": "A02", "liste": "E_0611", "zeitraumId": 1}, {"code": "A02", "liste": "E_0611", "zeitraumId": 2}]}, "zusatzdaten": {}}}, {"name": "55220", "summary": "55220 — Rückmeldung/Anfrage Abr.-Daten NNA", "value": {"stammdaten": {"VERWENDUNGSZEITRAUM": [{"boTyp": "VERWENDUNGSZEITRAUM", "versionStruktur": "1", "zeitraumId": 1, "datenqualitaet": "ERWARTETE_DATEN", "verwendungAb": "2025-06-23T22:00:00Z", "verwendungBis": "2025-07-23T22:00:00Z"}, {"boTyp": "VERWENDUNGSZEITRAUM", "versionStruktur": "1", "zeitraumId": 2, "datenqualitaet": "ERWARTETE_DATEN", "verwendungAb": "2025-07-23T22:00:00Z"}], "MARKTLOKATION": [{"boTyp": "MARKTLOKATION", "versionStruktur": "1", "marktlokationsId": "20072281644", "sparte": "STROM", "gueltigkeitszeitraum": {"zeitraumId": 1, "startdatum": "2025-06-23T22:00:00Z", "enddatum": "2025-07-23T22:00:00Z"}, "datenqualitaet": "ERWARTETE_DATEN", "netzbetreiberCodeNr": "9900327000009", "netznutzungsabrechnungsdaten": [{"artikelId": "1-02-0-001", "artikelIdTyp": "ARTIKELID", "gemeinderabatt": 0}]}, {"boTyp": "MARKTLOKATION", "versionStruktur": "1", "marktlokationsId": "20072281644", "sparte": "STROM", "gueltigkeitszeitraum": {"zeitraumId": 2, "startdatum": "2025-07-23T22:00:00Z"}, "datenqualitaet": "ERWARTETE_DATEN", "netzbetreiberCodeNr": "9900327000009", "netznutzungsabrechnungsdaten": [{"artikelId": "1-06-5-001", "artikelIdTyp": "ARTIKELID", "anzahl": 1, "gemeinderabatt": 0}]}], "NETZNUTZUNGSVERTRAG": [{"boTyp": "VERTRAG", "versionStruktur": "1", "vertragsart": "NETZNUTZUNGSVERTRAG", "sparte": "STROM", "gueltigkeitszeitraum": {"zeitraumId": 1, "startdatum": "2025-06-23T22:00:00Z", "enddatum": "2025-07-23T22:00:00Z"}, "datenqualitaet": "ERWARTETE_DATEN", "vertragskonditionen": {"netznutzungsabrechnung": {"abrechnungsZeitraum": "10051005"}, "netznutzungsabrechnungIntervall": 12, "netznutzungsvertrag": "LIEFERANTEN_NB", "netznutzungszahler": "LIEFERANT", "netznutzungsabrechnungsgrundlage": "LIEFERSCHEIN", "naechstenetznutzungsabrechnung": "2025"}, "lokationsId": "20072281644", "lokationsTyp": "MALO"}, {"boTyp": "VERTRAG", "versionStruktur": "1", "vertragsart": "NETZNUTZUNGSVERTRAG", "sparte": "STROM", "gueltigkeitszeitraum": {"zeitraumId": 2, "startdatum": "2025-07-23T22:00:00Z"}, "datenqualitaet": "ERWARTETE_DATEN", "vertragskonditionen": {"netznutzungsabrechnung": {"abrechnungsZeitraum": "10051005"}, "netznutzungsabrechnungIntervall": 12, "netznutzungsvertrag": "LIEFERANTEN_NB", "netznutzungszahler": "LIEFERANT", "netznutzungsabrechnungsgrundlage": "LIEFERSCHEIN", "naechstenetznutzungsabrechnung": "2025"}, "lokationsId": "20072281644", "lokationsTyp": "MALO"}], "BILANZIERUNG": [{"boTyp": "BILANZIERUNG", "versionStruktur": "1", "gueltigkeitszeitraum": {"zeitraumId": 1, "startdatum": "2025-06-23T22:00:00Z", "enddatum": "2025-07-23T22:00:00Z"}, "datenqualitaet": "ERWARTETE_DATEN", "verbrauchsaufteilung": {"wert": 25, "einheit": "PROZENT"}}, {"boTyp": "BILANZIERUNG", "versionStruktur": "1", "gueltigkeitszeitraum": {"zeitraumId": 2, "startdatum": "2025-07-23T22:00:00Z"}, "datenqualitaet": "ERWARTETE_DATEN", "verbrauchsaufteilung": {"wert": 25, "einheit": "PROZENT"}}]}, "transaktionsdaten": {"datenaustauschreferenz": "M4882AWT", "sparte": "STROM", "transaktionsgrund": "ZX4", "vorgangsnummer": "24062416225400000000000102159662011", "pruefidentifikator": "55220", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9903729000007", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900327000009", "rollencodetyp": "BDEW"}, "dokumentennummer": "BGMM49EB0JE", "kategorie": "E03", "nachrichtendatum": "2025-06-24T12:31:00Z", "nachrichtenreferenznummer": "UNHM3PYBDP9", "anfragereferenznummer": "NNV1234", "antwortStatusZeitraum": [{"code": "A02", "liste": "E_0610", "zeitraumId": 1}, {"code": "A02", "liste": "E_0610", "zeitraumId": 2}]}, "zusatzdaten": {}}}, {"name": "55673", "summary": "55673 — Rückmeldung/Anfrage Abr.-Daten BK-Abr. erz. Malo", "value": {"stammdaten": {"VERWENDUNGSZEITRAUM": [{"boTyp": "VERWENDUNGSZEITRAUM", "versionStruktur": "1", "zeitraumId": 1, "datenqualitaet": "ERWARTETE_DATEN", "verwendungAb": "2025-04-02T22:00:00Z"}], "MARKTLOKATION": [{"boTyp": "MARKTLOKATION", "versionStruktur": "1", "marktlokationsId": "50074561188", "marktlokationsTyp": [{"typ": "STANDARD_MARKTLOKATION"}], "sparte": "STROM", "gueltigkeitszeitraum": {"zeitraumId": 1, "startdatum": "2025-04-02T22:00:00Z"}, "datenqualitaet": "ERWARTETE_DATEN", "bilanzierungsgebiet": "11YR00000002596Z", "marktrollen": [{"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "marktrolle": "UENB", "gewerbekennzeichnung": true, "rollencodenummer": "4045399000077", "rollencodetyp": "BDEW"}], "regelzone": "10YDE-RWENET---I"}], "BILANZIERUNG": [{"boTyp": "BILANZIERUNG", "versionStruktur": "1", "gueltigkeitszeitraum": {"zeitraumId": 1, "startdatum": "2025-04-02T22:00:00Z"}, "datenqualitaet": "ERWARTETE_DATEN", "bilanzkreis": "11Y0-0000-0076-N", "aggregationsverantwortung": "UENB", "zeitreihentyp": "SES", "prognosegrundlage": "WERTE"}]}, "transaktionsdaten": {"datenaustauschreferenz": "M2YK1CNP", "sparte": "STROM", "transaktionsgrund": "ZX2", "transaktionsgrundergaenzung": "ZW3", "vorgangsnummer": "123456", "pruefidentifikator": "55673", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9903790000002", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900321000005", "rollencodetyp": "BDEW"}, "dokumentennummer": "BGMM3CXOLW4", "kategorie": "E03", "nachrichtendatum": "2025-04-04T12:00:00Z", "nachrichtenreferenznummer": "UNHM2PVLSIA", "anfragereferenznummer": "ABC123456", "antwortStatusZeitraum": [{"code": "A01", "liste": "E_0611", "zeitraumId": 1}, {"code": "A02", "liste": "E_0611", "zeitraumId": 2}]}, "zusatzdaten": {}}}, {"name": "17133", "summary": "17133 — Bestellung Änderung Abrechnungsdaten", "value": {"stammdaten": {"ANFRAGE": [{"boTyp": "ANFRAGE", "versionStruktur": "1", "anfragekategorie": "BESTELLUNG_AENDERUNG_ABRECHNUNGSDATEN", "lokationsId": "44153874533", "lokationsTyp": "MALO"}], "AUFTRAG": [{"boTyp": "AUFTRAG", "versionStruktur": "1", "startdatum": "2026-09-22T22:00:00Z", "positionsdaten": [{"positionsnummer": 1}]}], "MARKTLOKATION": [{"boTyp": "MARKTLOKATION", "versionStruktur": "1", "erforderlichesProduktpaket": [{"produkt": [{"produktCode": "9991000002545", "codeProdukteigenschaft": "9991000002719"}]}]}]}, "transaktionsdaten": {"datenaustauschreferenz": "M0WI8UR0", "sparte": "STROM", "pruefidentifikator": "17133", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9903111000003", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9903111000003", "rollencodetyp": "BDEW"}, "dokumentennummer": "M0ST4B5B", "nachrichtendatum": "2026-10-01T11:00:00Z", "nachrichtenreferenznummer": "M0RX30W4", "abtretungserklaerung": {"passwort": "sdfghjkmnbcgfdfgh", "link1": "https://stadt.de"}}, "zusatzdaten": {}}}]}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend fort, nachdem die Nachricht erstellt ist.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="2" anker="schritt-2" richtung="eingehend" kopf={{"links": {"label": "LF", "eigen": true}, "rechts": {"label": "NB"}}}>

### Bearbeitungsstand zur Bestellung

<Schrittskizze sicht={{"label": "LF"}} zeilen={[{"art": "empfangen", "label": "NB", "weg": "AS4", "nachrichten": [{"nr": "19133", "titel": "Bearbeitungsstand Bestellung Änderung Abrechnungsdaten"}, {"nr": "21047", "titel": "Bearbeitungsstandsmeldung"}]}, {"art": "aperak", "werte": ["Z33"]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [19133](/schnittstellen/202610/pruefi/ORDRSP/PI_19133) — Bearbeitungsstand Bestellung Änderung Abrechnungsdaten · AS4
- [21047](/schnittstellen/202610/pruefi/IFTSTA/PI_21047) — Bearbeitungsstandsmeldung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **NB** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `19133`, `21047` → [E_0595](/referenz/202610/ebd/E_0595) · NB · Bestellung prüfen

</div>

</li>

<li data-teil="aperak">

**Aperak-Prüfungen**
- `19133`, `21047` → `Z33` — Aperak Prüfung: Ist referenzierte Nachricht bekannt ?

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202610/backend-schreiben-lf/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": false, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"ANFRAGE\": [\n      {\n        \"anfragekategorie\": \"BESTELLUNG_AENDERUNG_ABRECHNUNGSDATEN\",\n        \"boTyp\": \"ANFRAGE\",\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9900327000009\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"antwortstatus\": \"A99\",\n    \"antwortstatusCodeliste\": \"E_0595\",\n    \"auftragsReferenz\": \"AFN9523\",\n    \"datenaustauschreferenz\": \"DAMVHRSKSYYZLQ\",\n    \"dokumentennummer\": \"DA002411200745569903323000007876291\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9979015000001\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"freitext\": \"Keine Zeit\",\n    \"kategorie\": \"Z91\",\n    \"nachrichtendatum\": \"2026-10-01T11:00:00Z\",\n    \"nachrichtenreferenznummer\": \"DAMBPCRKTKVXFQ\",\n    \"pruefidentifikator\": \"19133\",\n    \"sparte\": \"STROM\"\n  },\n  \"zusatzdaten\": {}\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

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
| [E_0595](/referenz/202610/ebd/E_0595) | Bestellung prüfen |

</details>

<a id="abschnitt-informationen"></a>

## Prozess-Informationen

Wortlaut der Lesefassung, Steckbrief Kap. 3.1.3.1, S. 77–79.

<Stepper>
<ol>

<li data-blatt="vorbedingungen">

### Vorbedingungen

- Die zum bestellten Zeitpunkt vorhandene Gerätetechnik ermöglicht die Änderung.
- Im Fall der Bestellung einer Änderung von Abrechnungsdaten zur Netznutzungsabrechnung:
  - Sofern der Bedarf der Anwendung einer Zählzeitdefinition des NB mit Zählzeitenanwendungszweck „Netznutzung“ vorliegt, muss eine entsprechende Konfiguration fristgerecht und erfolgreich über die Use-Cases im Kapitel „Bestellung einer Konfiguration“ (GPKE Teil 3) eingerichtet worden sein.
  - Es handelt sich um eine verbrauchende Marktlokation.
  - Dem LF liegen Abrechnungsdaten aufgrund des Use-Cases „[Abrechnungsdaten Netznutzungsabrechnung](/prozessdoku/202610/LF/GPKE-Teil2-abrechnungsdaten-netznutzungsabrechnung)“ vor.
  - Im Fall der Bestellung einer Änderung der Konzessionsabgabe:
    - Im Fall der Bestellung einer Schwachlast-Konzessionsabgabe:
- Es besteht ein Stromliefervertrag, der die Voraussetzungen zur Abrechnung der niedrigen Konzessionsabgabe an der Marktlokation erfüllt.
    - Im Fall einer Schwachlast-Konzessionsabgabe, für die die vertragliche Voraussetzung für die Schwachlast-Konzessionsabgabe zwischen LF und Letztverbraucher entfallen wird/ist, muss der LF eine Änderung der Konzessionsabgabe ungleich der Schwachlast-Konzessionsabgabe bestellen.
- Im Fall der Bestellung einer Änderung von Abrechnungsdaten zur Bilanzkreisabrechnung:
  - Dem LF liegen Abrechnungsdaten aufgrund des Use-Cases „[Abrechnungsdaten Bilanzkreisabrechnung](/prozessdoku/202610/LF/GPKE-Teil2-abrechnungsdaten-bilanzkreisabrechnung)“ vor bzw.
  - dem ÜNB liegen Abrechnungsdaten aufgrund des Use-Cases „[Abrechnungsdaten Bilanzkreisabrechnung](/prozessdoku/202610/LF/GPKE-Teil2-abrechnungsdaten-bilanzkreisabrechnung)“ vor.

</li>

<li data-blatt="ergebnisse">

### Ergebnisse

- Im Fall der Bestellung einer Änderung von Abrechnungsdaten zur Netznutzungsabrechnung: Der NB führt den Use-Case „[Abrechnungsdaten Netznutzungsabrechnung](/prozessdoku/202610/LF/GPKE-Teil2-abrechnungsdaten-netznutzungsabrechnung)“ aus.
- Im Fall der Bestellung einer Änderung von Abrechnungsdaten zur Bilanzkreisabrechnung: Der NB führt den Use-Case „[Abrechnungsdaten Bilanzkreisabrechnung](/prozessdoku/202610/LF/GPKE-Teil2-abrechnungsdaten-bilanzkreisabrechnung)“ aus.

</li>

<li data-blatt="fehlerfall">

### Fehlerfall

#### Ergebnis im Fehlerfall

Der LF bzw. ÜNB prüft, ob eine erneute Bestellung erforderlich ist.

#### Fehlerfälle

- Die zum bestellten Zeitpunkt vorhandene Gerätetechnik ermöglicht die Änderung nicht.
- Im Fall der Bestellung einer Änderung von Abrechnungsdaten zur Netznutzungsabrechnung: Es handelt sich um eine erzeugende Marktlokation bzw. eine Tranche.

</li>

<li data-blatt="anforderungen">

### Weitere Anforderungen

- Hinweis: Die Bestellung einer Änderung des Bilanzierungsverfahrens ist nicht über diesen Use-Case, sondern über den Use-Case „[Bestellung einer Konfiguration vom LF an NB](/prozessdoku/202610/LF/GPKE-Teil3-bestellung-einer-konfiguration-vom-lf-an-nb)“ (GPKE Teil 3) zu bestellen.
- Hinweise zu erzeugenden Marktlokationen bzw. zu Tranchen:
  - Der LF wendet für eine Änderung der Veräußerungsform und gleichzeitiger Zuordnung des LF zur Marktlokation bzw. Tranche den Use-Case “Lieferbeginn“ an.
  - Der LF wendet für eine Änderung der Tranchengröße den Use-Case “Lieferbeginn“ (s. Geschäftsvorfall 3) an.
- Hinweis: Sofern die zum bestellten Zeitpunkt vorhandene Gerätetechnik die Bestellung nicht ermöglicht, ist die Änderung der Gerätetechnik nicht über diesen Use-Case zu bestellen. Eine entsprechende Änderung der Gerätetechnik kann im Rahmen eines Gerätewechsels bzw. über die Use-Cases zur Messlokationsänderung (WiM Teil 1) beauftragt werden.
- Bzgl. der Festlegung zu Netzentgelten für steuerbare Anschlüsse und Verbrauchseinrichtungen (NSAVER) nach § 14a EnWG (BK8-22/010-A) gilt: Im Fall der Bestellung einer Änderung von Abrechnungsdaten zur Netznutzungsabrechnung werden ergänzende Vorgaben (wie z.B. Vorbedingungen und Fristen) durch die beim BDEW angesiedelte Expertengruppe EDI@Energy unter Beteiligung der Bundesnetzagentur veröffentlicht und gepflegt.

</li>

<li data-blatt="anlass">

### Anlass

- Der LF hat den Bedarf einer Änderung von Abrechnungsdaten zur Netznutzungsabrechnung (z.B. Änderung des Netznutzungsabrechnungsmodells von Arbeitspreis/Grundpreis auf Arbeitspreis/Leistungspreis oder Änderung des Zahlers der Netznutzung von Letztverbraucher auf LF).
- Der LF hat den Bedarf einer Änderung von Abrechnungsdaten zur Bilanzkreisabrechnung (z.B. Änderung der Jahresverbrauchprognose oder Änderung der Veräußerungsform)
- Der ÜNB hat den Bedarf einer Änderung von Abrechnungsdaten zur Bilanzkreisabrechnung.
- Der LF bzw. ÜNB geht von einem Datenschiefstand aus.

</li>

<li data-blatt="erste-nachricht">

### Erste Nachricht

Der Beteiligte dieser Seite sendet selbst: „Bestellung einer Änderung von Abrechnungsdaten“ an **NB** (Schritt 1).

</li>

<li data-blatt="ziel">

### Ziel

Der Bearbeitungsstand zur vom LF bzw. ÜNB bestellten Änderung von Abrechnungsdaten liegt dem LF bzw. ÜNB vom NB vor.

</li>

</ol>
</Stepper>

<a id="abschnitt-sichten"></a>

## Andere Sichten des Prozesses

Derselbe Prozess, aus den Augen der anderen Beteiligten: dieselben Schritte, jeweils aus deren Sicht gelesen.

- [Sicht NB](/prozessdoku/202610/NB/GPKE-Teil2-bestellung-einer-aenderung-von-abrechnungsdaten-von-lf-an-nb) — NB

<Hinweisbereich>

*Die Schritte sind die **möglichen** Nachrichten dieses Prozesses, keine Abfolge — die Quelle führt weder Bedingungen noch Alternativen. Das Kästchen am Schritt nennt links die eigene Sicht: **←** empfängt sie, **→** sendet sie. Zugeklappte Schritte laufen zwischen anderen Marktpartnern.*

</Hinweisbereich>
