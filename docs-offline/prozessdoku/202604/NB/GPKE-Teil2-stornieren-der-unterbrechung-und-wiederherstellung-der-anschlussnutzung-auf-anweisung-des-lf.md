# Stornieren der Unterbrechung und Wiederherstellung der Anschlussnutzung auf Anweisung des LF — Sicht NB

<Kopf rolle="NB" beteiligter="NB" festlegung="GPKE" dokument="GPKE Teil 2" kapitel="3.5.3.2" sparte="Strom" schritte={3} suchtitel="Stornieren der Unterbrechung und Wiederherstellung der Anschlussnutzung auf Anweisung des LF — Sicht NB · GPKE Teil 2 · Formatversion 202604" abschnitte={[{"id": "abschnitt-ablauf", "label": "Prozessablauf"}, {"id": "abschnitt-schritte", "label": "Prozessschritte"}, {"id": "abschnitt-informationen", "label": "Prozess-Informationen"}, {"id": "abschnitt-sichten", "label": "Andere Sichten des Prozesses"}]} />

<Kurzfassung>

Der LF sendet
- eine Stornierung des Auftrags zur Sperrung (Fall a) oder
- eine Stornierung des Auftrags zur Entsperrung (Fall b) einer Marktlokation, so dass
- die Anschlussnutzung an der Marktlokation weiterhin möglich ist (erfolgreiche Stornierung von Fall a) bzw.
- die Marktlokation weiterhin gesperrt bleibt (erfolgreiche Stornierung von Fall b). Sofern der MSB bereits eingebunden war, ist dieser ebenfalls zu informieren.

</Kurzfassung>

<a id="abschnitt-ablauf"></a>

## Prozessablauf aus Sicht des NB

<Systembild svg={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1004 683\" width=\"1004\" height=\"683\" role=\"img\" aria-labelledby=\"sb-title\" class=\"maco-systembild\">\n<title id=\"sb-title\">Systembild: Stornieren der Unterbrechung und Wiederherstellung der Anschlussnutzung auf Anweisung des LF aus Sicht NB</title>\n<defs><marker id=\"sb-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect class=\"sb-lane-kopf\" x=\"16\" y=\"12\" width=\"232\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend-System des Kunden</text>\n<rect class=\"sb-lane-kopf\" x=\"398\" y=\"12\" width=\"264\" height=\"46\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · NB</text>\n<rect class=\"sb-lane-kopf\" x=\"812\" y=\"12\" width=\"176\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"900\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Marktpartner</text>\n<line x1=\"323\" y1=\"58\" x2=\"323\" y2=\"671\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"737\" y1=\"58\" x2=\"737\" y2=\"671\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"80\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">1. Stornierung</text>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"78\" r=\"5\"/><line x1=\"900\" y1=\"83\" x2=\"900\" y2=\"95\"/><line x1=\"893\" y1=\"87\" x2=\"907\" y2=\"87\"/><line x1=\"900\" y1=\"95\" x2=\"894\" y2=\"105\"/><line x1=\"900\" y1=\"95\" x2=\"906\" y2=\"105\"/></g>\n<text x=\"900\" y=\"127\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">LF</text>\n<line x1=\"878\" y1=\"96\" x2=\"628\" y2=\"96\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"88\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"112\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">39000</text>\n<rect class=\"sb-kasten sb-schreiben\" x=\"432\" y=\"163\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"183\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"113\" x2=\"530\" y2=\"163\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-schreiben sb-abgeleitet\" x=\"34\" y=\"163\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"183\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten erstellen</text>\n<line x1=\"432\" y1=\"179\" x2=\"230\" y2=\"179\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"171\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-lesen\" x=\"432\" y=\"227\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"247\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Daten für die Prüfung laden</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"196\" x2=\"530\" y2=\"227\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-lesen\" x=\"34\" y=\"227\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"247\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Marktlokation lesen</text>\n<line x1=\"432\" y1=\"243\" x2=\"230\" y2=\"243\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"235\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-ebd\" x=\"432\" y=\"291\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"311\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">EBD prüfen: E_0468</text>\n<text x=\"530\" y=\"326\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label-2, #424245)\">Stornierung prüfen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"260\" x2=\"530\" y2=\"291\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"365\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"385\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">2. Antwort auf Stornierung</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"339\" x2=\"530\" y2=\"365\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"363\" r=\"5\"/><line x1=\"900\" y1=\"368\" x2=\"900\" y2=\"380\"/><line x1=\"893\" y1=\"372\" x2=\"907\" y2=\"372\"/><line x1=\"900\" y1=\"380\" x2=\"894\" y2=\"390\"/><line x1=\"900\" y1=\"380\" x2=\"906\" y2=\"390\"/></g>\n<text x=\"900\" y=\"412\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">LF</text>\n<line x1=\"628\" y1=\"381\" x2=\"878\" y2=\"381\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"373\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"397\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">19128, 19129</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"448\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"468\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"398\" x2=\"530\" y2=\"448\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"448\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"468\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"464\" x2=\"230\" y2=\"464\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"456\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"512\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"532\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">3. Weiterleitung der</text>\n<text x=\"530\" y=\"547\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Stornierung</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"481\" x2=\"530\" y2=\"512\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"518\" r=\"5\"/><line x1=\"900\" y1=\"523\" x2=\"900\" y2=\"535\"/><line x1=\"893\" y1=\"527\" x2=\"907\" y2=\"527\"/><line x1=\"900\" y1=\"535\" x2=\"894\" y2=\"545\"/><line x1=\"900\" y1=\"535\" x2=\"906\" y2=\"545\"/></g>\n<text x=\"900\" y=\"567\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">MSB</text>\n<line x1=\"628\" y1=\"536\" x2=\"878\" y2=\"536\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"528\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"552\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">39001</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"595\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"615\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"560\" x2=\"530\" y2=\"595\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"595\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"615\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"611\" x2=\"230\" y2=\"611\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"603\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n</svg>"} gesamt={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 974 486\" width=\"974\" height=\"486\" role=\"img\" aria-labelledby=\"sd-title\" class=\"maco-sequence\">\n<title id=\"sd-title\">Sequenzdiagramm: Stornieren der Unterbrechung und Wiederherstellung der Anschlussnutzung auf Anweisung des LF aus Sicht NB</title>\n<defs><marker id=\"sd-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect x=\"16\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"121\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend (Kunde)</text>\n<line x1=\"121\" y1=\"64\" x2=\"121\" y2=\"474\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"260\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"365\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · NB</text>\n<line x1=\"365\" y1=\"64\" x2=\"365\" y2=\"474\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"504\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"609\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">LF</text>\n<line x1=\"609\" y1=\"64\" x2=\"609\" y2=\"474\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"748\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"853\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">MSB</text>\n<line x1=\"853\" y1=\"64\" x2=\"853\" y2=\"474\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"609\" y1=\"90\" x2=\"365\" y2=\"90\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"81\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">1. Stornierung</text>\n<text x=\"487\" y=\"105\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 39000</text>\n<line x1=\"365\" y1=\"152\" x2=\"121\" y2=\"152\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"143\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<text x=\"243\" y=\"167\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten erstellen</text>\n<line x1=\"365\" y1=\"214\" x2=\"609\" y2=\"214\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"205\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">2. Antwort auf Stornierung</text>\n<text x=\"487\" y=\"229\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 19128, 19129 · E_0468</text>\n<text x=\"487\" y=\"242\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0468 — Stornierung prüfen</text>\n<line x1=\"365\" y1=\"276\" x2=\"121\" y2=\"276\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"267\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"291\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"365\" y1=\"338\" x2=\"853\" y2=\"338\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"609\" y=\"329\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">3. Weiterleitung der Stornierung</text>\n<text x=\"609\" y=\"353\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 39001</text>\n<line x1=\"365\" y1=\"400\" x2=\"121\" y2=\"400\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"391\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"415\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n</svg>"} titel="NB" />

<a id="abschnitt-schritte"></a>

## Prozessschritte

<Schritt nr="1" anker="schritt-1" richtung="eingehend" kopf={{"links": {"label": "NB", "eigen": true}, "rechts": {"label": "LF"}}}>

### Stornierung

<Schrittskizze sicht={{"label": "NB"}} zeilen={[{"art": "empfangen", "label": "LF", "weg": "AS4", "nachrichten": [{"nr": "39000", "titel": "Stornierung Sperr-/Entsperrauftrag"}]}, {"art": "erstellen"}, {"art": "lesen_ebd", "schnittstellen": [{"label": "Marktlokation lesen"}]}, {"art": "ebd", "baeume": [{"code": "E_0468", "titel": "Stornierung prüfen"}]}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [39000](/schnittstellen/202604/pruefi/ORDCHG/PI_39000) — Stornierung Sperr-/Entsperrauftrag · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **LF** · AS4

</li>

<li data-teil="schnittstelle" data-art="schreiben" data-abgeleitet="ja">

**Schreibende Schnittstelle**
- Vorgang angelegt — [Prozessdaten erstellen](/api/202604/backend-schreiben-nb/createprocessdata#prozessdaten-erstellen) `POST /createProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/createProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "ERSTELLEN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"ANFRAGE\": [\n      {\n        \"anfragekategorie\": \"ENTSPERRUNG\",\n        \"boTyp\": \"ANFRAGE\",\n        \"storno\": true,\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"ansprechpartner\": {\n        \"boTyp\": \"ANSPRECHPARTNER\",\n        \"eMailAdresse\": \"Max.Mustermann@conuti.de\",\n        \"nachname\": \"Max Mustermann\",\n        \"versionStruktur\": \"1\"\n      },\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9900496000001\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"auftragsReferenz\": \"BGMM2T7DSBY\",\n    \"datenaustauschreferenz\": \"M48RTTM6\",\n    \"dokumentennummer\": \"BGMM3XEABD2\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9900496000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"Z52\",\n    \"nachrichtendatum\": \"2024-10-16T09:45:00Z\",\n    \"nachrichtenfunktion\": \"1\",\n    \"nachrichtenreferenznummer\": \"UNHM3QWZ6ZB\",\n    \"pruefidentifikator\": \"39000\",\n    \"sparte\": \"STROM\"\n  },\n  \"zusatzdaten\": {}\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Legt im Backend einen neuen Vorgang mit den Daten der eingegangenen Nachricht an.

</li>

<li data-teil="lesen" data-stufe="ebd">

**Daten für die Prüfung laden**
- [Marktlokation lesen](/api/202604/backend-lesen/getmarketlocationbasic#marktlokation-lesen) `GET /getMarketLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getMarketLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": false, "defaultValue": "MALO", "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": false, "defaultValue": "2024-06-28T12:18:00Z", "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_MARKTLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

</li>

<li data-teil="baum">

**Entscheidungsbaum**
- `39000` → [E_0468](/referenz/202604/ebd/E_0468) — Stornierung prüfen

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="2" anker="schritt-2" richtung="ausgehend" kopf={{"links": {"label": "NB", "eigen": true}, "rechts": {"label": "LF"}}}>

### Antwort auf Stornierung

<Schrittskizze sicht={{"label": "NB"}} zeilen={[{"art": "senden", "label": "LF", "weg": "AS4", "nachrichten": [{"nr": "19128", "titel": "Bestätigung Stornierung Sperr-/Entsperrauftrag"}, {"nr": "19129", "titel": "Ablehnung Stornierung Sperr-/Entsperrauftrag"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [19128](/schnittstellen/202604/pruefi/ORDRSP/PI_19128) — Bestätigung Stornierung Sperr-/Entsperrauftrag · AS4
- [19129](/schnittstellen/202604/pruefi/ORDRSP/PI_19129) — Ablehnung Stornierung Sperr-/Entsperrauftrag · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht an **LF** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `19128`, `19129` → [E_0468](/referenz/202604/ebd/E_0468) · NB · Stornierung prüfen

</div>

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202604/backend-schreiben-nb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"ANFRAGE\": [\n      {\n        \"anfragekategorie\": \"SPERRUNG\",\n        \"boTyp\": \"ANFRAGE\",\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"ansprechpartner\": {\n        \"boTyp\": \"ANSPRECHPARTNER\",\n        \"nachname\": \"P GETTY\",\n        \"rufnummern\": [\n          {\n            \"nummerntyp\": \"RUF_DURCHWAHL\",\n            \"rufnummer\": \"+3222271020\"\n          }\n        ],\n        \"versionStruktur\": \"1\"\n      },\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9900327000009\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"antwortstatus\": \"A04\",\n    \"antwortstatusCodeliste\": \"E_0468\",\n    \"datenaustauschreferenz\": \"DAFDPMFOIKVPQS\",\n    \"dokumentennummer\": \"DA732411200727379903323000007169554\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9979015000001\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"Z51\",\n    \"nachrichtendatum\": \"2025-06-24T12:31:00Z\",\n    \"nachrichtenreferenznummer\": \"DAMSTEKKECNMTB\",\n    \"pruefidentifikator\": \"19128\",\n    \"sparte\": \"STROM\",\n    \"vorgangsreferenznummer\": \"REF32412\"\n  },\n  \"zusatzdaten\": {}\n}"} examples={[{"mediaType": "application/json", "examples": [{"name": "19128", "summary": "19128 — Bestätigung Stornierung Sperr-/Entsperrauftrag", "value": {"stammdaten": {"ANFRAGE": [{"boTyp": "ANFRAGE", "versionStruktur": "1", "anfragekategorie": "SPERRUNG"}]}, "transaktionsdaten": {"datenaustauschreferenz": "DAFDPMFOIKVPQS", "sparte": "STROM", "pruefidentifikator": "19128", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900327000009", "rollencodetyp": "BDEW", "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "nachname": "P GETTY", "rufnummern": [{"nummerntyp": "RUF_DURCHWAHL", "rufnummer": "+3222271020"}]}}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9979015000001", "rollencodetyp": "BDEW"}, "dokumentennummer": "DA732411200727379903323000007169554", "kategorie": "Z51", "nachrichtendatum": "2025-06-24T12:31:00Z", "nachrichtenreferenznummer": "DAMSTEKKECNMTB", "vorgangsreferenznummer": "REF32412", "antwortstatus": "A04", "antwortstatusCodeliste": "E_0468"}, "zusatzdaten": {}}}, {"name": "19129", "summary": "19129 — Ablehnung Stornierung Sperr-/Entsperrauftrag", "value": {"stammdaten": {"ANFRAGE": [{"boTyp": "ANFRAGE", "versionStruktur": "1", "anfragekategorie": "SPERRUNG"}]}, "transaktionsdaten": {"datenaustauschreferenz": "DARRMSWPWFCUFR", "sparte": "STROM", "pruefidentifikator": "19129", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900327000009", "rollencodetyp": "BDEW", "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "nachname": "P GETTY", "rufnummern": [{"nummerntyp": "RUF_DURCHWAHL", "rufnummer": "+3222271020"}]}}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9979015000001", "rollencodetyp": "BDEW"}, "dokumentennummer": "DA462411200729119903323000007362119", "kategorie": "Z51", "nachrichtendatum": "2025-06-24T12:31:00Z", "nachrichtenreferenznummer": "DAHABOXNVNJSQH", "vorgangsreferenznummer": "REF32412", "antwortstatus": "A02", "antwortstatusCodeliste": "E_0468"}, "zusatzdaten": {}}}]}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend fort, nachdem die Nachricht erstellt ist.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="3" anker="schritt-3" richtung="ausgehend" kopf={{"links": {"label": "NB", "eigen": true}, "rechts": {"label": "MSB"}}}>

### Weiterleitung der Stornierung

<Schrittskizze sicht={{"label": "NB"}} zeilen={[{"art": "senden", "label": "MSB", "weg": "AS4", "nachrichten": [{"nr": "39001", "titel": "Weiterleitung der Stornierung"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [39001](/schnittstellen/202604/pruefi/ORDCHG/PI_39001) — Weiterleitung der Stornierung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht an **MSB** · AS4

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202604/backend-schreiben-nb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"ANFRAGE\": [\n      {\n        \"anfragekategorie\": \"ENTSPERRUNG\",\n        \"boTyp\": \"ANFRAGE\",\n        \"storno\": true,\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"ansprechpartner\": {\n        \"boTyp\": \"ANSPRECHPARTNER\",\n        \"eMailAdresse\": \"Max.Mustermann@conuti.de\",\n        \"nachname\": \"Max Mustermann\",\n        \"versionStruktur\": \"1\"\n      },\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9900496000001\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"anfragereferenznummer\": \"51230\",\n    \"auftragsReferenz\": \"BGMM2T7DSBY\",\n    \"datenaustauschreferenz\": \"M4115M6T\",\n    \"dokumentennummer\": \"BGMM3SNGJRB\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9900496000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"Z52\",\n    \"nachrichtendatum\": \"2025-06-06T09:45:00Z\",\n    \"nachrichtenfunktion\": \"1\",\n    \"nachrichtenreferenznummer\": \"UNHM42HAHBJ\",\n    \"pruefidentifikator\": \"39001\",\n    \"sparte\": \"STROM\"\n  },\n  \"zusatzdaten\": {}\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

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
| [E_0468](/referenz/202604/ebd/E_0468) | Stornierung prüfen |

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
  - zu unterbrechen (Fall a: Use-Case „[Unterbrechung der Anschlussnutzung (Sperren) auf Anweisung des LF](/prozessdoku/202604/NB/GPKE-Teil2-unterbrechung-der-anschlussnutzung-sperren-auf-anweisung-des-lf)“) oder
  - zu entsperren (Fall b: Use-Case „[Wiederherstellung der Anschlussnutzung (Entsperren) auf Anweisung des LF](/prozessdoku/202604/NB/GPKE-Teil2-wiederherstellung-der-anschlussnutzung-entsperren-auf-anweisung-des-lf)“).
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
  - Um die Sperrung der Marktlokation aufzuheben, startet der LF den Use-Case „[Wiederherstellung der Anschlussnutzung (Entsperren) auf Anweisung des LF](/prozessdoku/202604/NB/GPKE-Teil2-wiederherstellung-der-anschlussnutzung-entsperren-auf-anweisung-des-lf)“ (Fall b).
- Bei erfolgloser Stornierung von Fall b:
  - Für die Sperrung der Marktlokation, startet der LF den Use-Case „[Unterbrechung der Anschlussnutzung (Sperren) auf Anweisung des LF](/prozessdoku/202604/NB/GPKE-Teil2-unterbrechung-der-anschlussnutzung-sperren-auf-anweisung-des-lf)“ (Fall a).

</li>

<li data-blatt="anforderungen">

### Weitere Anforderungen

- Die Stornierung eines Auftrags kann jederzeit durch den LF unabhängig des Status beim NB erfolgen, solange der Sperrauftrag bzw. Entsperrauftrag vom NB beim AN noch nicht durchgeführt wurde.
- Bei einer erfolgreichen Stornierung eines Sperrauftrags wird der Use-Case „[Unterbrechung der Anschlussnutzung (Sperren) auf Anweisung des LF](/prozessdoku/202604/NB/GPKE-Teil2-unterbrechung-der-anschlussnutzung-sperren-auf-anweisung-des-lf)“ mit dem SD-Schritt "ref Abrechnung einer sonstigen Leistung" fortgesetzt, um die bis dahin ggf. angefallenen Leistungen abrechnen zu können.

</li>

<li data-blatt="erste-nachricht">

### Erste Nachricht

**LF** sendet „Stornierung“ (Schritt 1). Ab hier ist der Beteiligte dieser Seite am Zug.

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

- [Sicht LF](/prozessdoku/202604/LF/GPKE-Teil2-stornieren-der-unterbrechung-und-wiederherstellung-der-anschlussnutzung-auf-anweisung-des-lf) — LF
- [Sicht MSB](/prozessdoku/202604/MSB/GPKE-Teil2-stornieren-der-unterbrechung-und-wiederherstellung-der-anschlussnutzung-auf-anweisung-des-lf) — MSB

<Hinweisbereich>

*Die Schritte sind die **möglichen** Nachrichten dieses Prozesses, keine Abfolge — die Quelle führt weder Bedingungen noch Alternativen. Das Kästchen am Schritt nennt links die eigene Sicht: **←** empfängt sie, **→** sendet sie. Zugeklappte Schritte laufen zwischen anderen Marktpartnern.*

Die Konnektortabelle führt für diese Schritte keinen Schreibaufruf. Abgeleitet aus dem Prozessverlauf: Mit ihrer Nachricht beginnt der Prozess für die eigene Rolle, der Vorgang entsteht also neu.

Betrifft: [1](#schritt-1)

</Hinweisbereich>
