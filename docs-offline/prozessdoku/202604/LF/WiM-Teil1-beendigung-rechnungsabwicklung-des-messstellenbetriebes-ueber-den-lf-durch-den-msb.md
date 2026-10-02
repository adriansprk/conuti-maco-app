# Beendigung Rechnungsabwicklung des Messstellenbetriebes über den LF durch den MSB — Sicht LF

<Kopf rolle="LF" beteiligter="LF" festlegung="WiM" dokument="WiM Strom Teil 1" kapitel="3.6.3.5.2" sparte="Strom" schritte={2} suchtitel="Beendigung Rechnungsabwicklung des Messstellenbetriebes über den LF durch den MSB — Sicht LF · WiM Strom Teil 1 · Formatversion 202604" abschnitte={[{"id": "abschnitt-ablauf", "label": "Prozessablauf"}, {"id": "abschnitt-schritte", "label": "Prozessschritte"}, {"id": "abschnitt-informationen", "label": "Prozess-Informationen"}, {"id": "abschnitt-sichten", "label": "Andere Sichten des Prozesses"}]} />

<Kurzfassung>

Der MSB der Marktlokation stellt eine Beendigungsanfrage und erhält nach Prüfung durch den LF eine Antwort.

</Kurzfassung>

<a id="abschnitt-ablauf"></a>

## Prozessablauf aus Sicht des LF

<Systembild svg={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1004 542\" width=\"1004\" height=\"542\" role=\"img\" aria-labelledby=\"sb-title\" class=\"maco-systembild\">\n<title id=\"sb-title\">Systembild: Beendigung Rechnungsabwicklung des Messstellenbetriebes über den LF durch den MSB aus Sicht LF</title>\n<defs><marker id=\"sb-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect class=\"sb-lane-kopf\" x=\"16\" y=\"12\" width=\"232\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend-System des Kunden</text>\n<rect class=\"sb-lane-kopf\" x=\"398\" y=\"12\" width=\"264\" height=\"46\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · LF</text>\n<rect class=\"sb-lane-kopf\" x=\"812\" y=\"12\" width=\"176\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"900\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Marktpartner</text>\n<line x1=\"323\" y1=\"58\" x2=\"323\" y2=\"530\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"737\" y1=\"58\" x2=\"737\" y2=\"530\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"80\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">1. Beendigung</text>\n<text x=\"530\" y=\"115\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Rechnungs-abwicklung des</text>\n<text x=\"530\" y=\"130\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Messstellenbetriebes üb…</text>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"93\" r=\"5\"/><line x1=\"900\" y1=\"98\" x2=\"900\" y2=\"110\"/><line x1=\"893\" y1=\"102\" x2=\"907\" y2=\"102\"/><line x1=\"900\" y1=\"110\" x2=\"894\" y2=\"120\"/><line x1=\"900\" y1=\"110\" x2=\"906\" y2=\"120\"/></g>\n<text x=\"900\" y=\"142\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">MSB (entspricht MSB a…</text>\n<line x1=\"878\" y1=\"111\" x2=\"628\" y2=\"111\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"103\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"127\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">17006</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"169\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"189\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z14</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"143\" x2=\"530\" y2=\"169\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-schreiben\" x=\"432\" y=\"233\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"253\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"202\" x2=\"530\" y2=\"233\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-schreiben sb-abgeleitet\" x=\"34\" y=\"233\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"253\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten erstellen</text>\n<line x1=\"432\" y1=\"249\" x2=\"230\" y2=\"249\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"241\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-ebd\" x=\"432\" y=\"297\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"317\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">EBD prüfen: E_0206</text>\n<text x=\"530\" y=\"332\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label-2, #424245)\">Beendigung prüfen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"266\" x2=\"530\" y2=\"297\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"371\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"391\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">2. Antwort auf Beendigung</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"345\" x2=\"530\" y2=\"371\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"369\" r=\"5\"/><line x1=\"900\" y1=\"374\" x2=\"900\" y2=\"386\"/><line x1=\"893\" y1=\"378\" x2=\"907\" y2=\"378\"/><line x1=\"900\" y1=\"386\" x2=\"894\" y2=\"396\"/><line x1=\"900\" y1=\"386\" x2=\"906\" y2=\"396\"/></g>\n<text x=\"900\" y=\"418\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">MSB (entspricht MSB a…</text>\n<line x1=\"628\" y1=\"387\" x2=\"878\" y2=\"387\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"379\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"403\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">19009, 19010</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"454\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"474\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"404\" x2=\"530\" y2=\"454\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"454\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"474\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"470\" x2=\"230\" y2=\"470\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"462\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n</svg>"} gesamt={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 730 362\" width=\"730\" height=\"362\" role=\"img\" aria-labelledby=\"sd-title\" class=\"maco-sequence\">\n<title id=\"sd-title\">Sequenzdiagramm: Beendigung Rechnungsabwicklung des Messstellenbetriebes über den LF durch den MSB aus Sicht LF</title>\n<defs><marker id=\"sd-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect x=\"16\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"121\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend (Kunde)</text>\n<line x1=\"121\" y1=\"64\" x2=\"121\" y2=\"350\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"260\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"365\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · LF</text>\n<line x1=\"365\" y1=\"64\" x2=\"365\" y2=\"350\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"504\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"609\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">MSB (entspricht MSB am Ob…</text>\n<line x1=\"609\" y1=\"64\" x2=\"609\" y2=\"350\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"609\" y1=\"90\" x2=\"365\" y2=\"90\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"81\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">1. Beendigung Rechnungs-abwicklung des Messstell…</text>\n<text x=\"487\" y=\"105\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 17006</text>\n<line x1=\"365\" y1=\"152\" x2=\"121\" y2=\"152\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"143\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<text x=\"243\" y=\"167\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten erstellen</text>\n<line x1=\"365\" y1=\"214\" x2=\"609\" y2=\"214\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"205\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">2. Antwort auf Beendigung</text>\n<text x=\"487\" y=\"229\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 19009, 19010 · E_0206</text>\n<text x=\"487\" y=\"242\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0206 — Beendigung prüfen</text>\n<line x1=\"365\" y1=\"276\" x2=\"121\" y2=\"276\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"267\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"291\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n</svg>"} titel="LF" />

<a id="abschnitt-schritte"></a>

## Prozessschritte

<Schritt nr="1" anker="schritt-1" richtung="eingehend" kopf={{"links": {"label": "LF", "eigen": true}, "rechts": {"label": "MSB (entspricht MSB am Objekt Marktlokation)"}}}>

### Beendigung Rechnungs-abwicklung des Messstellenbetriebes über den LF

<Schrittskizze sicht={{"label": "LF"}} zeilen={[{"art": "empfangen", "label": "MSB (entspricht MSB am Objekt Marktlokation)", "weg": "AS4", "nachrichten": [{"nr": "17006", "titel": "Beendigung Rechnungsabwicklung MSB über LF"}]}, {"art": "aperak", "werte": ["Z14"]}, {"art": "erstellen"}, {"art": "ebd", "baeume": [{"code": "E_0206", "titel": "Beendigung prüfen"}]}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [17006](/schnittstellen/202604/pruefi/ORDERS/PI_17006) — Beendigung Rechnungsabwicklung MSB über LF · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **MSB (entspricht MSB am Objekt Marktlokation)** · AS4

</li>

<li data-teil="aperak">

**Aperak-Prüfungen**
- `17006` → `Z14`

</li>

<li data-teil="schnittstelle" data-art="schreiben" data-abgeleitet="ja">

**Schreibende Schnittstelle**
- Vorgang angelegt — [Prozessdaten erstellen](/api/202604/backend-schreiben-lf/createprocessdata#prozessdaten-erstellen) `POST /createProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/createProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": false, "defaultValue": "ERSTELLEN_PROZESSDATEN", "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"ANFRAGE\": [\n      {\n        \"abonnement\": \"ENDE_ABO\",\n        \"anfragekategorie\": \"ABRECHNUNG_MESSSTELLENBETRIEB_MSB_AN_LF\",\n        \"boTyp\": \"ANFRAGE\",\n        \"lokationsId\": \"55123678945\",\n        \"lokationsTyp\": \"MALO\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"AUFTRAG\": [\n      {\n        \"ausfuehrungsdatum\": \"2025-03-28T23:00:00Z\",\n        \"boTyp\": \"AUFTRAG\",\n        \"positionsdaten\": [\n          {\n            \"anfragegrund\": \"DIREKTER_VERTRAG_MSB_AN\",\n            \"positionsnummer\": 1\n          }\n        ],\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"ansprechpartner\": {\n        \"boTyp\": \"ANSPRECHPARTNER\",\n        \"eMailAdresse\": \"mako@enercity.de\",\n        \"nachname\": \"Laue\",\n        \"versionStruktur\": \"1\"\n      },\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"marktrolle\": \"MSB\",\n      \"rollencodenummer\": \"9903111000003\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"datenaustauschreferenz\": \"LZX9TCGL\",\n    \"dokumentennummer\": \"M0S9VUBM\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9904629000006\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"nachrichtendatum\": \"2024-08-15T06:00:00Z\",\n    \"nachrichtenreferenznummer\": \"M06DSCB1\",\n    \"pruefidentifikator\": \"17006\",\n    \"sparte\": \"STROM\"\n  },\n  \"zusatzdaten\": {}\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Legt im Backend einen neuen Vorgang mit den Daten der eingegangenen Nachricht an.

</li>

<li data-teil="baum">

**Entscheidungsbaum**
- `17006` → [E_0206](/referenz/202604/ebd/E_0206) — Beendigung prüfen

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="2" anker="schritt-2" richtung="ausgehend" kopf={{"links": {"label": "LF", "eigen": true}, "rechts": {"label": "MSB (entspricht MSB am Objekt Marktlokation)"}}}>

### Antwort auf Beendigung

<Schrittskizze sicht={{"label": "LF"}} zeilen={[{"art": "senden", "label": "MSB (entspricht MSB am Objekt Marktlokation)", "weg": "AS4", "nachrichten": [{"nr": "19009", "titel": "Bestätigung Beendigung Rechnungsabwicklung MSB"}, {"nr": "19010", "titel": "Ablehnung Beendigung Rechnungsabwicklung MSB"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [19009](/schnittstellen/202604/pruefi/ORDRSP/PI_19009) — Bestätigung Beendigung Rechnungsabwicklung MSB · AS4
- [19010](/schnittstellen/202604/pruefi/ORDRSP/PI_19010) — Ablehnung Beendigung Rechnungsabwicklung MSB · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht an **MSB (entspricht MSB am Objekt Marktlokation)** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `19009`, `19010` → [E_0206](/referenz/202604/ebd/E_0206) · LF · Beendigung prüfen

</div>

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202604/backend-schreiben-lf/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": false, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"ANFRAGE\": [\n      {\n        \"abonnement\": \"ENDE_ABO\",\n        \"anfragekategorie\": \"ABRECHNUNG_MESSSTELLENBETRIEB_MSB_AN_LF\",\n        \"boTyp\": \"ANFRAGE\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"AUFTRAG\": [\n      {\n        \"ausfuehrungsdatum\": \"2011-04-08T22:00:00Z\",\n        \"boTyp\": \"AUFTRAG\",\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"ansprechpartner\": {\n        \"boTyp\": \"ANSPRECHPARTNER\",\n        \"nachname\": \"P GETTY\",\n        \"rufnummern\": [\n          {\n            \"nummerntyp\": \"RUF_DURCHWAHL\",\n            \"rufnummer\": \"+3222271020\"\n          }\n        ],\n        \"versionStruktur\": \"1\"\n      },\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9904990000008\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"antwortstatus\": \"A02\",\n    \"antwortstatusCodeliste\": \"E_0206\",\n    \"auftragsReferenz\": \"AFN9523\",\n    \"datenaustauschreferenz\": \"DAZSOKGWDJQFSP\",\n    \"dokumentennummer\": \"DA402411190821089903323000007476878\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9903729000007\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"Z29\",\n    \"nachrichtendatum\": \"2025-06-24T12:31:00Z\",\n    \"nachrichtenreferenznummer\": \"DAVXMWIOPHBYIA\",\n    \"pruefidentifikator\": \"19009\",\n    \"sparte\": \"STROM\"\n  },\n  \"zusatzdaten\": {}\n}"} examples={[{"mediaType": "application/json", "examples": [{"name": "19009", "summary": "19009 — Bestätigung Beendigung Rechnungsabwicklung MSB", "value": {"stammdaten": {"ANFRAGE": [{"boTyp": "ANFRAGE", "versionStruktur": "1", "anfragekategorie": "ABRECHNUNG_MESSSTELLENBETRIEB_MSB_AN_LF", "abonnement": "ENDE_ABO"}], "AUFTRAG": [{"boTyp": "AUFTRAG", "versionStruktur": "1", "ausfuehrungsdatum": "2011-04-08T22:00:00Z"}]}, "transaktionsdaten": {"datenaustauschreferenz": "DAZSOKGWDJQFSP", "sparte": "STROM", "pruefidentifikator": "19009", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9904990000008", "rollencodetyp": "BDEW", "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "nachname": "P GETTY", "rufnummern": [{"nummerntyp": "RUF_DURCHWAHL", "rufnummer": "+3222271020"}]}}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9903729000007", "rollencodetyp": "BDEW"}, "dokumentennummer": "DA402411190821089903323000007476878", "kategorie": "Z29", "nachrichtendatum": "2025-06-24T12:31:00Z", "nachrichtenreferenznummer": "DAVXMWIOPHBYIA", "auftragsReferenz": "AFN9523", "antwortstatus": "A02", "antwortstatusCodeliste": "E_0206"}, "zusatzdaten": {}}}, {"name": "19010", "summary": "19010 — Ablehnung Beendigung Rechnungsabwicklung MSB", "value": {"stammdaten": {"ANFRAGE": [{"boTyp": "ANFRAGE", "versionStruktur": "1", "anfragekategorie": "ABRECHNUNG_MESSSTELLENBETRIEB_MSB_AN_LF", "abonnement": "ENDE_ABO"}], "AUFTRAG": [{"boTyp": "AUFTRAG", "versionStruktur": "1", "ausfuehrungsdatum": "2011-04-08T22:00:00Z"}]}, "transaktionsdaten": {"datenaustauschreferenz": "DAWICXZSNXVCPQ", "sparte": "STROM", "pruefidentifikator": "19010", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9904990000008", "rollencodetyp": "BDEW", "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "nachname": "P GETTY", "rufnummern": [{"nummerntyp": "RUF_DURCHWAHL", "rufnummer": "+3222271020"}]}}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9903729000007", "rollencodetyp": "BDEW"}, "dokumentennummer": "DA972411190822429903323000007927565", "kategorie": "Z29", "nachrichtendatum": "2025-06-24T12:31:00Z", "nachrichtenreferenznummer": "DAQQJZODEEONNL", "auftragsReferenz": "AFN9523", "antwortstatus": "A01", "antwortstatusCodeliste": "E_0206"}, "zusatzdaten": {}}}]}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend fort, nachdem die Nachricht erstellt ist.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<details>
<summary>Entscheidungsbäume dieses Prozesses</summary>

| EBD | Name |
|---|---|
| [E_0206](/referenz/202604/ebd/E_0206) | Beendigung prüfen |

</details>

<a id="abschnitt-informationen"></a>

## Prozess-Informationen

Wortlaut der Lesefassung, Steckbrief Kap. 3.6.3.5.1, S. 72–73.

<Stepper>
<ol>

<li data-blatt="vorbedingungen">

### Vorbedingungen

Der LF ist der Marktlokation zum Anfragetermin der Nachricht zugeordnet. Es besteht zwischen LF und MSB der Marktlokation eine Vereinbarung über die Abrechnung des Messstellenbetriebes über den LF.

</li>

<li data-blatt="ergebnisse">

### Ergebnisse

Der LF ist bzgl. der Abwicklung des Entgelts für den Messstellenbetrieb der Messlokation nicht mehr zugeordnet. Ggf. wird eine Endrechnung gestellt.

</li>

<li data-blatt="fehlerfall">

### Fehlerfall

#### Ergebnis im Fehlerfall

Der LF ist als Zahler des Entgelts für den Messstellenbetrieb weiterhin zugeordnet.

</li>

<li data-blatt="anforderungen">

### Weitere Anforderungen

Hinweis: Die Beendigung der Rechnungsabwicklung kann auch eine zukünftig beginnende Abrechnung des MSB der Marktlokation betreffen, welche zum Abrechnungsbeginn obsolet wird.

</li>

<li data-blatt="anlass">

### Anlass

- Abschluss eines direkten Vertrags zwischen MSB der Marktlokation und AN,
- Abschluss eines direkten Vertrags zwischen MSB der Marktlokation und ANN,
- Aufgrund von Änderungen im Lokationsbündel erfolgt die Abrechnung der Messentgelte über eine andere Marktlokation im Lokationsbündel.

</li>

<li data-blatt="erste-nachricht">

### Erste Nachricht

**MSB (entspricht MSB am Objekt Marktlokation)** sendet „Beendigung Rechnungs-abwicklung des Messstellenbetriebes über den LF“ (Schritt 1). Ab hier ist der Beteiligte dieser Seite am Zug.

</li>

<li data-blatt="ziel">

### Ziel

Die Vereinbarung zwischen MSB der Marktlokation und LF über die Abrechnung des Messstellenbetriebes an den LF ist zum genannten Zeitpunkt beendet.

</li>

</ol>
</Stepper>

<a id="abschnitt-sichten"></a>

## Andere Sichten des Prozesses

Derselbe Prozess, aus den Augen der anderen Beteiligten: dieselben Schritte, jeweils aus deren Sicht gelesen.

- [Sicht MSB-MALO](/prozessdoku/202604/MSB/WiM-Teil1-beendigung-rechnungsabwicklung-des-messstellenbetriebes-ueber-den-lf-durch-den-msb) — MSB am Objekt Marktlokation · Marktrolle MSB

<Hinweisbereich>

*Die Schritte sind die **möglichen** Nachrichten dieses Prozesses, keine Abfolge — die Quelle führt weder Bedingungen noch Alternativen. Das Kästchen am Schritt nennt links die eigene Sicht: **←** empfängt sie, **→** sendet sie. Zugeklappte Schritte laufen zwischen anderen Marktpartnern.*

Die Konnektortabelle führt für diese Schritte keinen Schreibaufruf. Abgeleitet aus dem Prozessverlauf: Mit ihrer Nachricht beginnt der Prozess für die eigene Rolle, der Vorgang entsteht also neu.

Betrifft: [1](#schritt-1)

</Hinweisbereich>
