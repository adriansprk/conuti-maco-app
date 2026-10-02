# Lieferende von LF an NB — Sicht LF

<Kopf rolle="LF" beteiligter="LF" festlegung="GPKE" dokument="GPKE Teil 2" kapitel="2.5.1.2" sparte="Strom" schritte={3} suchtitel="Lieferende von LF an NB — Sicht LF · GPKE Teil 2 · Formatversion 202610" stichworte="Lieferantenwechsel" abschnitte={[{"id": "abschnitt-ablauf", "label": "Prozessablauf"}, {"id": "abschnitt-schritte", "label": "Prozessschritte"}, {"id": "abschnitt-informationen", "label": "Prozess-Informationen"}, {"id": "abschnitt-sichten", "label": "Andere Sichten des Prozesses"}]} />

<Kurzfassung>

Ein LF meldet beim NB eine Zuordnung des LF zu einer Marktlokation bzw. Tranche ab.

</Kurzfassung>

<a id="abschnitt-ablauf"></a>

## Prozessablauf aus Sicht des LF

<Systembild svg={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1004 755\" width=\"1004\" height=\"755\" role=\"img\" aria-labelledby=\"sb-title\" class=\"maco-systembild\">\n<title id=\"sb-title\">Systembild: Lieferende von LF an NB aus Sicht LF</title>\n<defs><marker id=\"sb-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect class=\"sb-lane-kopf\" x=\"16\" y=\"12\" width=\"232\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend-System des Kunden</text>\n<rect class=\"sb-lane-kopf\" x=\"398\" y=\"12\" width=\"264\" height=\"46\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · LF</text>\n<rect class=\"sb-lane-kopf\" x=\"812\" y=\"12\" width=\"176\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"900\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Marktpartner</text>\n<line x1=\"323\" y1=\"58\" x2=\"323\" y2=\"743\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"737\" y1=\"58\" x2=\"737\" y2=\"743\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect class=\"sb-kasten sb-trigger\" x=\"432\" y=\"80\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessauslöser empfangen</text>\n<rect class=\"sb-kasten sb-backend sb-trigger\" x=\"34\" y=\"80\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">START_LIEFERENDE</text>\n<line x1=\"230\" y1=\"96\" x2=\"432\" y2=\"96\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"88\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"144\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"164\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">1. Abmeldung einer</text>\n<text x=\"530\" y=\"179\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Zuordnung des LF zur</text>\n<text x=\"530\" y=\"194\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Marktlokation bzw. Tra…</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"113\" x2=\"530\" y2=\"144\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"157\" r=\"5\"/><line x1=\"900\" y1=\"162\" x2=\"900\" y2=\"174\"/><line x1=\"893\" y1=\"166\" x2=\"907\" y2=\"166\"/><line x1=\"900\" y1=\"174\" x2=\"894\" y2=\"184\"/><line x1=\"900\" y1=\"174\" x2=\"906\" y2=\"184\"/></g>\n<text x=\"900\" y=\"206\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"628\" y1=\"175\" x2=\"878\" y2=\"175\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"167\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"191\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">55004</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"233\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"253\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"207\" x2=\"530\" y2=\"233\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"233\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"253\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"249\" x2=\"230\" y2=\"249\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"241\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"297\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"317\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">2. Beendigung der</text>\n<text x=\"530\" y=\"332\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Zuordnung des LF zur</text>\n<text x=\"530\" y=\"347\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Marktlokation bzw. Tran…</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"266\" x2=\"530\" y2=\"297\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"310\" r=\"5\"/><line x1=\"900\" y1=\"315\" x2=\"900\" y2=\"327\"/><line x1=\"893\" y1=\"319\" x2=\"907\" y2=\"319\"/><line x1=\"900\" y1=\"327\" x2=\"894\" y2=\"337\"/><line x1=\"900\" y1=\"327\" x2=\"906\" y2=\"337\"/></g>\n<text x=\"900\" y=\"359\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"878\" y1=\"328\" x2=\"628\" y2=\"328\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"320\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"344\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">55005</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"386\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"406\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z33</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"360\" x2=\"530\" y2=\"386\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"450\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"470\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"419\" x2=\"530\" y2=\"450\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"450\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"470\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"466\" x2=\"230\" y2=\"466\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"458\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"514\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"534\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">3. Ablehnung der Abmeldung</text>\n<text x=\"530\" y=\"549\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">einer Zuordnung des LF zur</text>\n<text x=\"530\" y=\"564\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Marktlok…</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"483\" x2=\"530\" y2=\"514\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"527\" r=\"5\"/><line x1=\"900\" y1=\"532\" x2=\"900\" y2=\"544\"/><line x1=\"893\" y1=\"536\" x2=\"907\" y2=\"536\"/><line x1=\"900\" y1=\"544\" x2=\"894\" y2=\"554\"/><line x1=\"900\" y1=\"544\" x2=\"906\" y2=\"554\"/></g>\n<text x=\"900\" y=\"576\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"878\" y1=\"545\" x2=\"628\" y2=\"545\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"537\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"561\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">55006</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"603\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"623\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z33</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"577\" x2=\"530\" y2=\"603\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"667\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"687\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"636\" x2=\"530\" y2=\"667\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"667\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"687\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"683\" x2=\"230\" y2=\"683\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"675\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n</svg>"} gesamt={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 730 548\" width=\"730\" height=\"548\" role=\"img\" aria-labelledby=\"sd-title\" class=\"maco-sequence\">\n<title id=\"sd-title\">Sequenzdiagramm: Lieferende von LF an NB aus Sicht LF</title>\n<defs><marker id=\"sd-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect x=\"16\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"121\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend (Kunde)</text>\n<line x1=\"121\" y1=\"64\" x2=\"121\" y2=\"536\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"260\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"365\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · LF</text>\n<line x1=\"365\" y1=\"64\" x2=\"365\" y2=\"536\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"504\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"609\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"609\" y1=\"64\" x2=\"609\" y2=\"536\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"121\" y1=\"90\" x2=\"365\" y2=\"90\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"81\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">START_LIEFERENDE</text>\n<text x=\"243\" y=\"105\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Trigger-Event</text>\n<line x1=\"365\" y1=\"152\" x2=\"609\" y2=\"152\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"143\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">1. Abmeldung einer Zuordnung des LF zur Marktlok…</text>\n<text x=\"487\" y=\"167\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55004</text>\n<line x1=\"365\" y1=\"214\" x2=\"121\" y2=\"214\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"205\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"229\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"609\" y1=\"276\" x2=\"365\" y2=\"276\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"267\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">2. Beendigung der Zuordnung des LF zur Marktloka…</text>\n<text x=\"487\" y=\"291\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55005 · E_0607</text>\n<text x=\"487\" y=\"304\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0607 — Abmeldung prüfen</text>\n<line x1=\"365\" y1=\"338\" x2=\"121\" y2=\"338\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"329\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"353\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"609\" y1=\"400\" x2=\"365\" y2=\"400\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"391\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">3. Ablehnung der Abmeldung einer Zuordnung des L…</text>\n<text x=\"487\" y=\"415\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55006 · E_0607</text>\n<text x=\"487\" y=\"428\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0607 — Abmeldung prüfen</text>\n<line x1=\"365\" y1=\"462\" x2=\"121\" y2=\"462\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"453\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"477\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n</svg>"} titel="LF" />

<a id="abschnitt-schritte"></a>

## Prozessschritte

<Schritt nr="1" anker="schritt-1" richtung="ausgehend" kopf={{"links": {"label": "LF", "eigen": true}, "rechts": {"label": "NB"}}}>

### Abmeldung einer Zuordnung des LF zur Marktlokation bzw. Tranche

<Schrittskizze sicht={{"label": "LF"}} zeilen={[{"art": "ausloeser", "werte": ["START_LIEFERENDE"]}, {"art": "senden", "label": "NB", "weg": "AS4", "nachrichten": [{"nr": "55004", "titel": "Abmeldung"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55004](/schnittstellen/202610/pruefi/UTILMD/PI_55004) — Abmeldung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="ausloeser">

**Prozessauslöser** [`START_LIEFERENDE`](/schnittstellen/202610/trigger/events/LF-START_LIEFERENDE) · [Im Playground ausprobieren](/api/202610/ausloeser-lf/start-lieferende)

Das Backend stößt diesen Schritt mit diesem Ereignis an.

</li>

<li data-teil="nachricht">

Nachricht an **NB** · AS4

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202610/backend-schreiben-lf/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": false, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"MARKTLOKATION\": [\n      {\n        \"boTyp\": \"MARKTLOKATION\",\n        \"marktlokationsId\": \"50363198100\",\n        \"marktlokationsTyp\": [\n          {\n            \"typ\": \"RUHENDE_MARKTLOKATION\"\n          }\n        ],\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"NETZNUTZUNGSVERTRAG\": [\n      {\n        \"boTyp\": \"VERTRAG\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\",\n        \"vertragsart\": \"NETZNUTZUNGSVERTRAG\",\n        \"vertragsende\": \"2026-11-01T23:00:00Z\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9903729000007\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"datenaustauschreferenz\": \"DASHVGXANGXCUT\",\n    \"dokumentennummer\": \"DA392410151057009903323000007497785\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9900327000009\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"E02\",\n    \"nachrichtendatum\": \"2026-10-02T11:00:00Z\",\n    \"nachrichtenreferenznummer\": \"DARDSNUVZLGQHG\",\n    \"pruefidentifikator\": \"55004\",\n    \"sparte\": \"STROM\",\n    \"transaktionsgrund\": \"E01\",\n    \"transaktionsgrundergaenzung\": \"ZAP\",\n    \"vertragsende\": \"2026-11-01T23:00:00Z\",\n    \"vorgangsnummer\": \"24062416225400000000000102159662022\"\n  },\n  \"zusatzdaten\": {}\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend fort, nachdem die Nachricht erstellt ist.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="2" anker="schritt-2" richtung="eingehend" kopf={{"links": {"label": "LF", "eigen": true}, "rechts": {"label": "NB"}}}>

### Beendigung der Zuordnung des LF zur Marktlokation bzw. Tranche

<Schrittskizze sicht={{"label": "LF"}} zeilen={[{"art": "empfangen", "label": "NB", "weg": "AS4", "nachrichten": [{"nr": "55005", "titel": "Bestätigung Abmeldung"}]}, {"art": "aperak", "werte": ["Z33"]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55005](/schnittstellen/202610/pruefi/UTILMD/PI_55005) — Bestätigung Abmeldung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **NB** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `55005` → [E_0607](/referenz/202610/ebd/E_0607) · NB · Abmeldung prüfen

</div>

</li>

<li data-teil="aperak">

**Aperak-Prüfungen**
- `55005` → `Z33` — Aperak Prüfung: Ist referenzierte Nachricht bekannt ?

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202610/backend-schreiben-lf/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": false, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"NETZNUTZUNGSVERTRAG\": [\n      {\n        \"boTyp\": \"VERTRAG\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\",\n        \"vertragsart\": \"NETZNUTZUNGSVERTRAG\",\n        \"vertragsende\": \"2026-09-30T22:00:00Z\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"ansprechpartner\": {\n        \"boTyp\": \"ANSPRECHPARTNER\",\n        \"nachname\": \"P GETTY\",\n        \"rufnummern\": [\n          {\n            \"nummerntyp\": \"RUF_DURCHWAHL\",\n            \"rufnummer\": \"+3222271020\"\n          }\n        ],\n        \"versionStruktur\": \"1\"\n      },\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9903729000007\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"anfragereferenznummer\": \"Abmeldung55004\",\n    \"antwortstatus\": \"A27\",\n    \"antwortstatusCodeliste\": \"E_0607\",\n    \"datenaustauschreferenz\": \"002351596028\",\n    \"dokumentennummer\": \"002351596028\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9903323000007\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"E02\",\n    \"nachrichtendatum\": \"2026-10-02T11:00:00Z\",\n    \"nachrichtenreferenznummer\": \"002351596028\",\n    \"pruefidentifikator\": \"55005\",\n    \"sparte\": \"STROM\",\n    \"transaktionsgrund\": \"E01\",\n    \"vorgangsnummer\": \"24062416225400000000000102159662022\"\n  },\n  \"zusatzdaten\": {}\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend mit den Daten der eingegangenen Nachricht fort.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="3" anker="schritt-3" richtung="eingehend" kopf={{"links": {"label": "LF", "eigen": true}, "rechts": {"label": "NB"}}}>

### Ablehnung der Abmeldung einer Zuordnung des LF zur Marktlokation bzw. Tranche

<Schrittskizze sicht={{"label": "LF"}} zeilen={[{"art": "empfangen", "label": "NB", "weg": "AS4", "nachrichten": [{"nr": "55006", "titel": "Ablehnung Abmeldung"}]}, {"art": "aperak", "werte": ["Z33"]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55006](/schnittstellen/202610/pruefi/UTILMD/PI_55006) — Ablehnung Abmeldung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **NB** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `55006` → [E_0607](/referenz/202610/ebd/E_0607) · NB · Abmeldung prüfen

</div>

</li>

<li data-teil="aperak">

**Aperak-Prüfungen**
- `55006` → `Z33` — Aperak Prüfung: Ist referenzierte Nachricht bekannt ?

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202610/backend-schreiben-lf/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": false, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "type": "string"}]} defaultBody={"{\n  \"stammdaten\": [],\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9900321000005\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"anfragereferenznummer\": \"PCL_7823101008565599050790000006659\",\n    \"antwortstatus\": \"A01\",\n    \"antwortstatusCodeliste\": \"E_0607\",\n    \"datenaustauschreferenz\": \"D0000000762312\",\n    \"dokumentennummer\": \"UT0000377481\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9903790000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"E02\",\n    \"nachrichtendatum\": \"2026-10-02T11:00:00Z\",\n    \"nachrichtenreferenznummer\": \"UT0000377481\",\n    \"pruefidentifikator\": \"55006\",\n    \"sparte\": \"STROM\",\n    \"transaktionsgrund\": \"ZT4\",\n    \"vorgangsnummer\": \"VID00000000002244135231010104605000\"\n  }\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

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
| [E_0607](/referenz/202610/ebd/E_0607) | Abmeldung prüfen |

</details>

<a id="abschnitt-informationen"></a>

## Prozess-Informationen

Wortlaut der Lesefassung, Steckbrief Kap. 2.5.1.1, S. 53–54.

<Stepper>
<ol>

<li data-blatt="vorbedingungen">

### Vorbedingungen

- Im Fall einer verbrauchenden Marktlokation:
  - Der LF ist der Marktlokation zugeordnet.
  - Beendigung eines Energieliefervertrags zwischen LF und dem Letztverbraucher.
- Im Fall einer erzeugenden Marktlokation bzw. einer Tranche:
  - Der LF ist der Marktlokation bzw. Tranche zugeordnet.
  - Beendigung eines Stromabnahmevertrags zwischen LF und dem EZ. Die folgenden Fälle sind dabei möglich:
    - Abmeldung der Zuordnung des LF zu einer Marktlokation
    - Abmeldung der Zuordnung des LF zu einer Tranche einer Marktlokation
  - Der Use-Case ist nicht durch das Unternehmen Netzbetreiber in seiner Rolle als LF zu starten.

</li>

<li data-blatt="ergebnisse">

### Ergebnisse

- Im Fall einer verbrauchenden Marktlokation:
  - Der NB führt die Use-Cases „[Abrechnungsdaten Netznutzungsabrechnung](/prozessdoku/202610/LF/GPKE-Teil2-abrechnungsdaten-netznutzungsabrechnung)“ und „[Abrechnungsdaten Bilanzkreisabrechnung](/prozessdoku/202610/LF/GPKE-Teil2-abrechnungsdaten-bilanzkreisabrechnung)“ aus.
  - Der NB führt ggf. den Use-Case „[Beginn der Ersatz-/Grundversorgung](/prozessdoku/202610/LF/GPKE-Teil2-beginn-der-ersatz-grundversorgung)“ aus.
- Im Fall einer erzeugenden Marktlokation bzw. einer Tranche:
  - Der NB führt den Use-Case „[Abrechnungsdaten Bilanzkreisabrechnung](/prozessdoku/202610/LF/GPKE-Teil2-abrechnungsdaten-bilanzkreisabrechnung)“ aus.
  - Der NB führt ggf. den Use-Case „Herstellung einer 100% LF-Zuordnung zu einer erzeugenden Marktlokation“ aus.
- Sofern eine Stilllegung der Marktlokation vorliegen sollte, führt der NB den Use-Case „[Lieferende von NB an LF](/prozessdoku/202610/LF/GPKE-Teil2-lieferende-von-nb-an-lf)“ durch.

</li>

<li data-blatt="fehlerfall">

### Fehlerfall

#### Ergebnis im Fehlerfall

- Der LF bleibt der Marktlokation bzw. Tranche zugeordnet.
- Der LF sendet bei Bedarf erneut eine Abmeldung an den NB.

#### Fehlerfälle

- Im Fall einer erzeugenden Marktlokation bzw. einer Tranche: Der Use-Case wird durch das Unternehmen Netzbetreiber in seiner Rolle als LF gestartet.

</li>

<li data-blatt="anforderungen">

### Weitere Anforderungen

- Hinweis: Eine Marktlokation, die keinem LF zugeordnet werden kann und für die eine gesetzliche Grund- oder Ersatzversorgungspflicht nach § 36 und § 38 EnWG bestehen kann, ordnet der NB über den Use-Case „[Beginn der Ersatz-/Grundversorgung](/prozessdoku/202610/LF/GPKE-Teil2-beginn-der-ersatz-grundversorgung)“ dem E/G zu.
- Wenn eine Marktlokation infolge der Beendigung der Zuordnung künftig weder dem E/G noch einem vertraglich bestimmten Ersatzbelieferer oder einem sonstigen LF zuordenbar ist, hat eine Unterbrechung der Anschlussnutzung an der Marktlokation durch den NB zu erfolgen.

</li>

<li data-blatt="anlass">

### Anlass

- Im Fall einer verbrauchenden Marktlokation:
  - Bestätigung der Kündigung des Energieliefervertrags gegenüber dem LFN im Rahmen des Use-Cases „[Kündigung](/prozessdoku/202610/LF--LFA/GPKE-Teil2-kuendigung)“
  - Bestätigung der Kündigung des Energieliefervertrags gegenüber dem Letztverbraucher (z.B. aufgrund Auszug des Letztverbrauchers aus der Marktlokation, Lieferantenwechsel, Stilllegung der Marktlokation)
- Im Fall einer erzeugenden Marktlokation bzw. einer Tranche:
  - Bestätigung der Kündigung des Stromabnahmevertrags gegenüber dem LFN im Rahmen des Use-Cases „[Kündigung](/prozessdoku/202610/LF--LFA/GPKE-Teil2-kuendigung)“
  - Bestätigung der Kündigung des Stromabnahmevertrags gegenüber dem EZ (z.B. aufgrund Lieferantenwechsel, Stilllegung der Marktlokation)

**Vorher läuft:** [Kündigung](/prozessdoku/202610/LF--LFA/GPKE-Teil2-kuendigung) — diese Prozesse nennen den hier gezeigten in ihrem Ergebnis.

</li>

<li data-blatt="erste-nachricht">

### Erste Nachricht

Der Beteiligte dieser Seite sendet selbst: „Abmeldung einer Zuordnung des LF zur Marktlokation bzw. Tranche“ an **NB** (Schritt 1).

</li>

<li data-blatt="ziel">

### Ziel

Die Zuordnung des LF zur Marktlokation bzw. Tranche ist beendet.

</li>

</ol>
</Stepper>

<a id="abschnitt-sichten"></a>

## Andere Sichten des Prozesses

Derselbe Prozess, aus den Augen der anderen Beteiligten: dieselben Schritte, jeweils aus deren Sicht gelesen.

- [Sicht NB](/prozessdoku/202610/NB/GPKE-Teil2-lieferende-von-lf-an-nb) — NB

<Hinweisbereich>

*Die Schritte sind die **möglichen** Nachrichten dieses Prozesses, keine Abfolge — die Quelle führt weder Bedingungen noch Alternativen. Das Kästchen am Schritt nennt links die eigene Sicht: **←** empfängt sie, **→** sendet sie. Zugeklappte Schritte laufen zwischen anderen Marktpartnern.*

</Hinweisbereich>
