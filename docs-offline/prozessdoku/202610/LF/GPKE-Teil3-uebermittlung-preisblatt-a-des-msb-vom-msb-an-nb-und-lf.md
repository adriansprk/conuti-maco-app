# Übermittlung Preisblatt A des MSB vom MSB an NB und LF — Sicht LF

<Kopf rolle="LF" beteiligter="LF" festlegung="GPKE" dokument="GPKE Teil 3" kapitel="3.4.2" sparte="Strom" schritte={2} suchtitel="Übermittlung Preisblatt A des MSB vom MSB an NB und LF — Sicht LF · GPKE Teil 3 · Formatversion 202610" abschnitte={[{"id": "abschnitt-ablauf", "label": "Prozessablauf"}, {"id": "abschnitt-schritte", "label": "Prozessschritte"}, {"id": "abschnitt-informationen", "label": "Prozess-Informationen"}, {"id": "abschnitt-sichten", "label": "Andere Sichten des Prozesses"}]} />

<Kurzfassung>

Der MSB übermittelt dem NB bzw. LF sein elektronisches Preisblatt A, wenn dem NB bzw. LF das elektronische Preisblatt A nicht vorliegt oder sich mindestens eine Preiskomponente des Preisblatts A geändert hat.

</Kurzfassung>

<a id="abschnitt-ablauf"></a>

## Prozessablauf aus Sicht des LF

<Systembild svg={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1004 315\" width=\"1004\" height=\"315\" role=\"img\" aria-labelledby=\"sb-title\" class=\"maco-systembild\">\n<title id=\"sb-title\">Systembild: Übermittlung Preisblatt A des MSB vom MSB an NB und LF aus Sicht LF</title>\n<defs><marker id=\"sb-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect class=\"sb-lane-kopf\" x=\"16\" y=\"12\" width=\"232\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend-System des Kunden</text>\n<rect class=\"sb-lane-kopf\" x=\"398\" y=\"12\" width=\"264\" height=\"46\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · LF</text>\n<rect class=\"sb-lane-kopf\" x=\"812\" y=\"12\" width=\"176\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"900\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Marktpartner</text>\n<line x1=\"323\" y1=\"58\" x2=\"323\" y2=\"303\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"737\" y1=\"58\" x2=\"737\" y2=\"303\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"80\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">2. Preisblatt A des MSB</text>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"78\" r=\"5\"/><line x1=\"900\" y1=\"83\" x2=\"900\" y2=\"95\"/><line x1=\"893\" y1=\"87\" x2=\"907\" y2=\"87\"/><line x1=\"900\" y1=\"95\" x2=\"894\" y2=\"105\"/><line x1=\"900\" y1=\"95\" x2=\"906\" y2=\"105\"/></g>\n<text x=\"900\" y=\"127\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">MSB</text>\n<line x1=\"878\" y1=\"96\" x2=\"628\" y2=\"96\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"88\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"112\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">27002</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"163\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"183\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z33</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"113\" x2=\"530\" y2=\"163\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-schreiben\" x=\"432\" y=\"227\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"247\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"196\" x2=\"530\" y2=\"227\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-schreiben sb-abgeleitet\" x=\"34\" y=\"227\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"247\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten erstellen</text>\n<line x1=\"432\" y1=\"243\" x2=\"230\" y2=\"243\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"235\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n</svg>"} gesamt={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 974 300\" width=\"974\" height=\"300\" role=\"img\" aria-labelledby=\"sd-title\" class=\"maco-sequence\">\n<title id=\"sd-title\">Sequenzdiagramm: Übermittlung Preisblatt A des MSB vom MSB an NB und LF aus Sicht LF</title>\n<defs><marker id=\"sd-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect x=\"16\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"121\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend (Kunde)</text>\n<line x1=\"121\" y1=\"64\" x2=\"121\" y2=\"288\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"260\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"365\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · LF</text>\n<line x1=\"365\" y1=\"64\" x2=\"365\" y2=\"288\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"504\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"609\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">MSB</text>\n<line x1=\"609\" y1=\"64\" x2=\"609\" y2=\"288\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"748\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"853\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"853\" y1=\"64\" x2=\"853\" y2=\"288\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"609\" y1=\"90\" x2=\"853\" y2=\"90\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"731\" y=\"81\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">1. Preisblatt A des MSB</text>\n<text x=\"731\" y=\"105\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 27002</text>\n<line x1=\"609\" y1=\"152\" x2=\"365\" y2=\"152\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"143\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">2. Preisblatt A des MSB</text>\n<text x=\"487\" y=\"167\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 27002</text>\n<line x1=\"365\" y1=\"214\" x2=\"121\" y2=\"214\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"205\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<text x=\"243\" y=\"229\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten erstellen</text>\n</svg>"} titel="LF" />

<a id="abschnitt-schritte"></a>

## Prozessschritte

<Schritt nr="1" anker="schritt-1" richtung="fremd" kopf={{"links": {"label": "MSB", "eigen": false}, "rechts": {"label": "NB"}}}>

### Preisblatt A des MSB

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [27002](/schnittstellen/202610/pruefi/PRICAT/PI_27002) — Preisblätter MSB-Leistungen · AS4

</div>

</Schritt>

<Schritt nr="2" anker="schritt-2" richtung="eingehend" kopf={{"links": {"label": "LF", "eigen": true}, "rechts": {"label": "MSB"}}}>

### Preisblatt A des MSB

<Schrittskizze sicht={{"label": "LF"}} zeilen={[{"art": "empfangen", "label": "MSB", "weg": "AS4", "nachrichten": [{"nr": "27002", "titel": "Preisblätter MSB-Leistungen"}]}, {"art": "aperak", "werte": ["Z33"]}, {"art": "erstellen"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [27002](/schnittstellen/202610/pruefi/PRICAT/PI_27002) — Preisblätter MSB-Leistungen · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **MSB** · AS4

</li>

<li data-teil="aperak">

**Aperak-Prüfungen**
- `27002` → `Z33` — Aperak Prüfung: Ist referenzierte Nachricht bekannt ?

</li>

<li data-teil="schnittstelle" data-art="schreiben" data-abgeleitet="ja">

**Schreibende Schnittstelle**
- Vorgang angelegt — [Prozessdaten erstellen](/api/202610/backend-schreiben-lf/createprocessdata#prozessdaten-erstellen) `POST /createProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/createProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": false, "defaultValue": "ERSTELLEN_PROZESSDATEN", "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"PREISBLATT\": [\n      {\n        \"boTyp\": \"PREISBLATT\",\n        \"gueltigkeit\": {\n          \"startdatum\": \"2025-12-31T23:00:00Z\"\n        },\n        \"preispositionen\": [\n          {\n            \"artikelId\": \"9991000002305-02\",\n            \"beschreibung\": \"Kosten für den Einbau eines sehr sehr schweren Zählers\",\n            \"beschreibungsformat\": \"FREIER_TEXT\",\n            \"positionsnummer\": 1,\n            \"preiseinheit\": \"EUR\",\n            \"preisstaffeln\": [\n              {\n                \"einheit\": \"KWH\",\n                \"einheitspreis\": 0,\n                \"staffelgrenzeBis\": 3,\n                \"staffelgrenzeVon\": 0\n              }\n            ]\n          },\n          {\n            \"artikelId\": \"9991000002305-03\",\n            \"beschreibung\": \"Kosten für den Einbau eines noch schwereren Zählers\",\n            \"beschreibungsformat\": \"FREIER_TEXT\",\n            \"positionsnummer\": 2,\n            \"preiseinheit\": \"EUR\",\n            \"preisstaffeln\": [\n              {\n                \"einheit\": \"KWH\",\n                \"einheitspreis\": 0,\n                \"staffelgrenzeBis\": 4,\n                \"staffelgrenzeVon\": 3\n              }\n            ]\n          },\n          {\n            \"artikelId\": \"9991000002313-02\",\n            \"beschreibung\": \"Einbau kME / rLM\",\n            \"beschreibungsformat\": \"FREIER_TEXT\",\n            \"positionsnummer\": 3,\n            \"preiseinheit\": \"EUR\",\n            \"preisstaffeln\": [\n              {\n                \"einheit\": \"KWH\",\n                \"einheitspreis\": 0,\n                \"staffelgrenzeBis\": 3,\n                \"staffelgrenzeVon\": 0\n              }\n            ]\n          },\n          {\n            \"artikelId\": \"9991000002313-03\",\n            \"beschreibung\": \"Einbau kME / rLM\",\n            \"beschreibungsformat\": \"FREIER_TEXT\",\n            \"positionsnummer\": 4,\n            \"preiseinheit\": \"EUR\",\n            \"preisstaffeln\": [\n              {\n                \"einheit\": \"KWH\",\n                \"einheitspreis\": 0,\n                \"staffelgrenzeBis\": 4,\n                \"staffelgrenzeVon\": 3\n              }\n            ]\n          },\n          {\n            \"artikelId\": \"9991000002321-01\",\n            \"positionsnummer\": 5,\n            \"preiseinheit\": \"EUR\",\n            \"preisstaffeln\": [\n              {\n                \"einheitspreis\": 1337\n              }\n            ]\n          },\n          {\n            \"artikelId\": \"9991000003030-01\",\n            \"positionsnummer\": 6,\n            \"preiseinheit\": \"EUR\",\n            \"preisstaffeln\": [\n              {\n                \"einheitspreis\": 666\n              }\n            ]\n          }\n        ],\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9904446000007\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"datenaustauschreferenz\": \"5576673PF\",\n    \"dokumentennummer\": \"990562800000505102023000001733337\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9903790000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"Z94\",\n    \"nachrichtendatum\": \"2026-10-01T11:00:00Z\",\n    \"nachrichtenreferenznummer\": \"5576674PF\",\n    \"pruefidentifikator\": \"27002\",\n    \"sparte\": \"STROM\"\n  },\n  \"zusatzdaten\": {}\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Legt im Backend einen neuen Vorgang mit den Daten der eingegangenen Nachricht an.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<a id="abschnitt-informationen"></a>

## Prozess-Informationen

Wortlaut der Lesefassung, Steckbrief Kap. 3.4.1, S. 93.

<Stepper>
<ol>

<li data-blatt="vorbedingungen">

### Vorbedingungen

Die EDIFACT-Kommunikation zwischen MSB und NB bzw. LF ist aufgebaut und dem NB bzw. LF liegt das aktuelle oder aktualisierte Preisblatt A des MSB nicht vor.

</li>

<li data-blatt="ergebnisse">

### Ergebnisse

- Gegenüber dem NB gilt: Die Abrechnung über den Use-Case „Abrechnung Leistungen des Preisblatts A des MSB“ kann ggü. dem NB erfolgen, sofern der NB über den
  - Use-Case „Bestellung einer Konfiguration vom NB oder LF an MSB“ eine kostenpflichtige Konfiguration bestellt hat und die Bestellung vom MSB bestätigt wurde oder
  - Use-Case „Steuerbefehl vom NB oder LF an MSB“ einen kostenpflichtigen Steuerbefehl angewiesen hat und die Anweisung vom MSB bestätigt wurde. Hinweis: Sind im Preisblatt A des MSB zum angewiesenen Steuerbefehl Kriterien angegeben, in welchem Fall der Steuerbefehl kostenpflichtig ist, müssen diese Kriterien zudem erfüllt sein.
- Gegenüber dem LF gilt: Die Abrechnung über den Use-Case „Abrechnung Leistungen des Preisblatts A des MSB“ kann ggü. dem LF erfolgen, sofern der LF über den
  - Use-Case „Bestellung einer Konfiguration vom NB oder LF an MSB“ eine kostenpflichtige Konfiguration bestellt hat und die Bestellung vom MSB bestätigt wurde oder
  - Use-Case „Steuerbefehl vom NB oder LF an MSB“ einen kostenpflichtigen Steuerbefehl bestellt hat und die Bestellung vom MSB bestätigt wurde. Hinweis: Sind im Preisblatt A des MSB zum bestellten Steuerbefehl Kriterien angegeben, in welchem Fall der Steuerbefehl kostenpflichtig ist, müssen diese Kriterien zudem erfüllt sein.

</li>

<li data-blatt="fehlerfall">

### Fehlerfall

#### Ergebnis im Fehlerfall

In den Fehlerfällen erfolgt eine erneute Übermittlung des Preisblatts A des MSB.

#### Fehlerfälle

- Preisblatt enthält einen Fehler
- Preisblatt wurde nicht in der aktuellen Version übermittelt
- Preisblatt wurde nicht vollständig übermittelt
- Preisblatt beginnt nicht um 00:00 Uhr eines Kalendertages.

</li>

<li data-blatt="erste-nachricht">

### Erste Nachricht

**MSB** sendet „Preisblatt A des MSB“ (Schritt 2). Ab hier ist der Beteiligte dieser Seite am Zug.

</li>

<li data-blatt="ziel">

### Ziel

Dem NB und LF liegt das Preisblatt A des MSB vor.

</li>

</ol>
</Stepper>

<a id="abschnitt-sichten"></a>

## Andere Sichten des Prozesses

Derselbe Prozess, aus den Augen der anderen Beteiligten: dieselben Schritte, jeweils aus deren Sicht gelesen.

- [Sicht NB](/prozessdoku/202610/NB/GPKE-Teil3-uebermittlung-preisblatt-a-des-msb-vom-msb-an-nb-und-lf) — NB
- [Sicht MSB](/prozessdoku/202610/MSB/GPKE-Teil3-uebermittlung-preisblatt-a-des-msb-vom-msb-an-nb-und-lf) — MSB

<Hinweisbereich>

*Die Schritte sind die **möglichen** Nachrichten dieses Prozesses, keine Abfolge — die Quelle führt weder Bedingungen noch Alternativen. Das Kästchen am Schritt nennt links die eigene Sicht: **←** empfängt sie, **→** sendet sie. Zugeklappte Schritte laufen zwischen anderen Marktpartnern.*

Die Konnektortabelle führt für diese Schritte keinen Schreibaufruf. Abgeleitet aus dem Prozessverlauf: Mit ihrer Nachricht beginnt der Prozess für die eigene Rolle, der Vorgang entsteht also neu.

Betrifft: [2](#schritt-2)

</Hinweisbereich>
