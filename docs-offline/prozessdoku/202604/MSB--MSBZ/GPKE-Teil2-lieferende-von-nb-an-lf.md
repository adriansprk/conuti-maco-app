# Lieferende von NB an LF — Sicht MSBZ

<Kopf rolle="MSB" beteiligter="MSBZ" festlegung="GPKE" dokument="GPKE Teil 2" kapitel="2.5.2.2" sparte="Strom" schritte={6} suchtitel="Lieferende von NB an LF — Sicht MSBZ (Marktrolle MSB) · GPKE Teil 2 · Formatversion 202604" stichworte="Lieferantenwechsel" abschnitte={[{"id": "abschnitt-ablauf", "label": "Prozessablauf"}, {"id": "abschnitt-schritte", "label": "Prozessschritte"}, {"id": "abschnitt-informationen", "label": "Prozess-Informationen"}, {"id": "abschnitt-sichten", "label": "Andere Sichten des Prozesses"}]} />

<Kurzfassung>

Der NB kündigt dem LF die Beendigung der Zuordnung des LF zur Marktlokation bzw. Tranche an. Im Zuge des Prozesses
- beendet der NB bei einer Stilllegung der Marktlokation die Zuordnung des MSB zur Marktlokation bzw. Messlokation.
- hebt der NB bei einer Stilllegung der Marktlokation
  - ggf. die Zuordnung des LFZ zur Marktlokation bzw. Tranche auf.
  - ggf. die Zuordnung des MSBZ zur Marktlokation bzw. Messlokation auf.

</Kurzfassung>

<a id="abschnitt-ablauf"></a>

## Prozessablauf aus Sicht des MSB (MSBZ)

<Systembild svg={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1004 257\" width=\"1004\" height=\"257\" role=\"img\" aria-labelledby=\"sb-title\" class=\"maco-systembild\">\n<title id=\"sb-title\">Systembild: Lieferende von NB an LF aus Sicht MSB</title>\n<defs><marker id=\"sb-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect class=\"sb-lane-kopf\" x=\"16\" y=\"12\" width=\"232\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend-System des Kunden</text>\n<rect class=\"sb-lane-kopf\" x=\"398\" y=\"12\" width=\"264\" height=\"46\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · MSBZ</text>\n<rect class=\"sb-lane-kopf\" x=\"812\" y=\"12\" width=\"176\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"900\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Marktpartner</text>\n<line x1=\"323\" y1=\"58\" x2=\"323\" y2=\"245\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"737\" y1=\"58\" x2=\"737\" y2=\"245\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"80\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">13. Aufhebung der</text>\n<text x=\"530\" y=\"115\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Zuordnung des MSBZ zur</text>\n<text x=\"530\" y=\"130\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Marktlokation bzw. Mes…</text>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"93\" r=\"5\"/><line x1=\"900\" y1=\"98\" x2=\"900\" y2=\"110\"/><line x1=\"893\" y1=\"102\" x2=\"907\" y2=\"102\"/><line x1=\"900\" y1=\"110\" x2=\"894\" y2=\"120\"/><line x1=\"900\" y1=\"110\" x2=\"906\" y2=\"120\"/></g>\n<text x=\"900\" y=\"142\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"878\" y1=\"111\" x2=\"628\" y2=\"111\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"103\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"127\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">55611</text>\n<rect class=\"sb-kasten sb-schreiben\" x=\"432\" y=\"169\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"189\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"143\" x2=\"530\" y2=\"169\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-schreiben sb-abgeleitet\" x=\"34\" y=\"169\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"189\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten erstellen</text>\n<line x1=\"432\" y1=\"185\" x2=\"230\" y2=\"185\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"177\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n</svg>"} gesamt={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1462 548\" width=\"1462\" height=\"548\" role=\"img\" aria-labelledby=\"sd-title\" class=\"maco-sequence\">\n<title id=\"sd-title\">Sequenzdiagramm: Lieferende von NB an LF aus Sicht MSB</title>\n<defs><marker id=\"sd-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect x=\"16\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"121\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend (Kunde)</text>\n<line x1=\"121\" y1=\"64\" x2=\"121\" y2=\"536\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"260\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"365\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · MSBZ</text>\n<line x1=\"365\" y1=\"64\" x2=\"365\" y2=\"536\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"504\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"609\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"609\" y1=\"64\" x2=\"609\" y2=\"536\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"748\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"853\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">LF</text>\n<line x1=\"853\" y1=\"64\" x2=\"853\" y2=\"536\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"992\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"1097\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">LFZ</text>\n<line x1=\"1097\" y1=\"64\" x2=\"1097\" y2=\"536\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"1236\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"1341\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">MSB</text>\n<line x1=\"1341\" y1=\"64\" x2=\"1341\" y2=\"536\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"609\" y1=\"90\" x2=\"853\" y2=\"90\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"731\" y=\"81\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">1. Ankündigung der Beendigung der Zuordnung des…</text>\n<text x=\"731\" y=\"105\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55007</text>\n<line x1=\"853\" y1=\"152\" x2=\"609\" y2=\"152\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"731\" y=\"143\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">2. Antwort auf Ankündigung der Beendigung der Zu…</text>\n<text x=\"731\" y=\"167\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55008, 55009 · E_0609</text>\n<text x=\"731\" y=\"180\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0609 — Abmeldung prüfen</text>\n<line x1=\"609\" y1=\"214\" x2=\"853\" y2=\"214\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"731\" y=\"205\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">3. Beendigung der Zuordnung des LF zur Marktloka…</text>\n<text x=\"731\" y=\"229\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55007</text>\n<line x1=\"609\" y1=\"276\" x2=\"1097\" y2=\"276\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"853\" y=\"267\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">8. Aufhebung der Zuordnung des LFZ zur Marklokat…</text>\n<text x=\"853\" y=\"291\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55038</text>\n<line x1=\"609\" y1=\"338\" x2=\"1341\" y2=\"338\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"975\" y=\"329\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">11. Beendigung der Zuordnung des MSB zur Markloka…</text>\n<text x=\"975\" y=\"353\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55611</text>\n<line x1=\"609\" y1=\"400\" x2=\"365\" y2=\"400\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"391\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">13. Aufhebung der Zuordnung des MSBZ zur Marktlok…</text>\n<text x=\"487\" y=\"415\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55611</text>\n<line x1=\"365\" y1=\"462\" x2=\"121\" y2=\"462\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"453\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<text x=\"243\" y=\"477\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten erstellen</text>\n</svg>"} titel="MSBZ" />

<a id="abschnitt-schritte"></a>

## Prozessschritte

<Schritt nr="1" anker="schritt-1" richtung="fremd" kopf={{"links": {"label": "NB", "eigen": false}, "rechts": {"label": "LF"}}}>

### Ankündigung der Beendigung der Zuordnung des LF zur Marktlokation bzw. Tranche

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55007](/schnittstellen/202604/pruefi/UTILMD/PI_55007) — Abmeldung / Beendigung der Zuordnung · AS4

</div>

</Schritt>

<Schritt nr="2" anker="schritt-2" richtung="fremd" kopf={{"links": {"label": "LF", "eigen": false}, "rechts": {"label": "NB"}}}>

### Antwort auf Ankündigung der Beendigung der Zuordnung des LF zur Marktlokation bzw. Tranche

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55008](/schnittstellen/202604/pruefi/UTILMD/PI_55008) — Bestätigung Abmeldung · AS4
- [55009](/schnittstellen/202604/pruefi/UTILMD/PI_55009) — Ablehnung Abmeldung · AS4

</div>

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `55008`, `55009` → [E_0609](/referenz/202604/ebd/E_0609) · LF · Abmeldung prüfen

</div>

</Schritt>

<Schritt nr="3" anker="schritt-3" richtung="fremd" kopf={{"links": {"label": "NB", "eigen": false}, "rechts": {"label": "LF"}}}>

### Beendigung der Zuordnung des LF zur Marktlokation bzw. Tranche aufgrund fehlender Antwort

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55007](/schnittstellen/202604/pruefi/UTILMD/PI_55007) — Abmeldung / Beendigung der Zuordnung · AS4

</div>

</Schritt>

<Schritt nr="8" anker="schritt-8" richtung="fremd" kopf={{"links": {"label": "NB", "eigen": false}, "rechts": {"label": "LFZ"}}}>

### Aufhebung der Zuordnung des LFZ zur Marklokation bzw. Tranche

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55038](/schnittstellen/202604/pruefi/UTILMD/PI_55038) — Aufhebung einer zuk. Zuordnung · AS4

</div>

</Schritt>

<Schritt nr="11" anker="schritt-11" richtung="fremd" kopf={{"links": {"label": "NB", "eigen": false}, "rechts": {"label": "MSB"}}}>

### Beendigung der Zuordnung des MSB zur Marklokation bzw. Messlokation

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55611](/schnittstellen/202604/pruefi/UTILMD/PI_55611) — Beendigung der Zuordnung · AS4

</div>

</Schritt>

<Schritt nr="13" anker="schritt-13" richtung="eingehend" kopf={{"links": {"label": "MSBZ", "eigen": true}, "rechts": {"label": "NB"}}}>

### Aufhebung der Zuordnung des MSBZ zur Marktlokation bzw. Messlokation

<Schrittskizze sicht={{"label": "MSBZ"}} zeilen={[{"art": "empfangen", "label": "NB", "weg": "AS4", "nachrichten": [{"nr": "55611", "titel": "Beendigung der Zuordnung"}]}, {"art": "erstellen"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55611](/schnittstellen/202604/pruefi/UTILMD/PI_55611) — Beendigung der Zuordnung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **NB** · AS4

</li>

<li data-teil="schnittstelle" data-art="schreiben" data-abgeleitet="ja">

**Schreibende Schnittstelle**
- Vorgang angelegt — [Prozessdaten erstellen](/api/202604/backend-schreiben-msb/createprocessdata#prozessdaten-erstellen) `POST /createProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/createProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "ERSTELLEN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"MARKTLOKATION\": [\n      {\n        \"boTyp\": \"MARKTLOKATION\",\n        \"marktlokationsId\": \"50263791178\",\n        \"marktlokationsTyp\": [\n          {\n            \"typ\": \"STANDARD_MARKTLOKATION\"\n          }\n        ],\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"NETZNUTZUNGSVERTRAG\": [\n      {\n        \"boTyp\": \"VERTRAG\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\",\n        \"vertragsart\": \"NETZNUTZUNGSVERTRAG\",\n        \"vertragsende\": \"2025-06-30T22:00:00Z\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9900321000005\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"datenaustauschreferenz\": \"M07HQ72J\",\n    \"dokumentennummer\": \"BGMLZB8RKIK\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9904446000007\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"E02\",\n    \"nachrichtendatum\": \"2025-04-04T12:00:00Z\",\n    \"nachrichtenreferenznummer\": \"UNHM02KY709\",\n    \"pruefidentifikator\": \"55611\",\n    \"sparte\": \"STROM\",\n    \"transaktionsgrund\": \"ZC8\",\n    \"vertragsende\": \"2025-06-30T22:00:00Z\",\n    \"vorgangsnummer\": \"123456\"\n  },\n  \"zusatzdaten\": {}\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Legt im Backend einen neuen Vorgang mit den Daten der eingegangenen Nachricht an.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<details>
<summary>Entscheidungsbäume der anderen Beteiligten</summary>

| EBD | Name |
|---|---|
| [E_0609](/referenz/202604/ebd/E_0609) | Abmeldung prüfen |

</details>

<a id="abschnitt-informationen"></a>

## Prozess-Informationen

Wortlaut der Lesefassung, Steckbrief Kap. 2.5.2.1, S. 57–58.

<Stepper>
<ol>

<li data-blatt="vorbedingungen">

### Vorbedingungen

- Im Fall einer verbrauchenden Marktlokation: Der LF ist der Marktlokation zugeordnet.
- Im Fall einer erzeugenden Marktlokation bzw. einer Tranche: Der LF ist der Marktlokation bzw. Tranche zugeordnet. Die folgenden Fälle sind dabei möglich:
  - Beendigung der Zuordnung des LF zu einer Marktlokation
  - Beendigung der Zuordnung des LF zu einer Tranche einer Marktlokation
  - Beendigung der Zuordnung der LF zu allen Tranchen einer Marktlokation. Hierbei muss der Use-Case „Lieferende von NB an LF“ je Tranche separat durchgeführt werden.

</li>

<li data-blatt="ergebnisse">

### Ergebnisse

- Im Fall einer verbrauchenden Marktlokation:
  - Der NB führt die Use-Cases „[Abrechnungsdaten Netznutzungsabrechnung](/prozessdoku/202604/LF/GPKE-Teil2-abrechnungsdaten-netznutzungsabrechnung)“ und „[Abrechnungsdaten Bilanzkreisabrechnung](/prozessdoku/202604/LF/GPKE-Teil2-abrechnungsdaten-bilanzkreisabrechnung)“ aus.
  - Der NB führt ggf. den Use-Case „[Beginn der Ersatz-/Grundversorgung](/prozessdoku/202604/LF/GPKE-Teil2-beginn-der-ersatz-grundversorgung)“ aus.
  - Im Fall der Stilllegung: Wenn die Marktlokation dem Modell 2 zugeordnet ist, beendet der NB den Zählpunkt für die NGZ.
- Im Fall einer erzeugenden Marktlokation bzw. einer Tranche:
  - Der NB führt den Use-Case „[Abrechnungsdaten Bilanzkreisabrechnung](/prozessdoku/202604/LF/GPKE-Teil2-abrechnungsdaten-bilanzkreisabrechnung)“ aus.
  - Der NB führt ggf. den Use-Case „Herstellung einer 100% LF-Zuordnung zu einer erzeugenden Marktlokation“ aus.
- Im Fall der Stilllegung einer Marktlokation: Sofern das Lokationsbündel nicht stillgelegt wird, informiert der NB die Marktpartner der weiterhin aktiven Lokationen über die Änderung des Lokationsbündels mit dem Use-Case "Stammdatenänderung" (hier: „[Stammdatenänderung vom NB (verantwortlich) ausgehend](/prozessdoku/202604/LF/GPKE-Teil4-stammdatenaenderung-vom-nb-verantwortlich-ausgehend)“) (GPKE Teil 4).

</li>

<li data-blatt="fehlerfall">

### Fehlerfall

#### Ergebnis im Fehlerfall

Der LF bleibt der Marktlokation bzw. Tranche zugeordnet.

</li>

<li data-blatt="anforderungen">

### Weitere Anforderungen

- Hinweis: Eine Marktlokation, die keinem LF zugeordnet werden kann und für die eine gesetzliche Grund- oder Ersatzversorgungspflicht nach § 36 und § 38 EnWG bestehen kann, ordnet der NB über den Use-Case „[Beginn der Ersatz-/Grundversorgung](/prozessdoku/202604/LF/GPKE-Teil2-beginn-der-ersatz-grundversorgung)“ dem E/G zu.
- Wenn eine Marktlokation infolge der Beendigung der Zuordnung künftig weder dem E/G noch einem vertraglich bestimmten Ersatzbelieferer oder einem sonstigen LF zuordenbar ist, hat eine Unterbrechung der Anschlussnutzung an der Marktlokation durch den NB zu erfolgen.

</li>

<li data-blatt="anlass">

### Anlass

- Stilllegung einer Marktlokation
- der Use-Case „[Deaktivierung einer Zuordnungsermächtigung des BKV beim NB](/prozessdoku/202604/BKV/MaBiS-deaktivierung-einer-zuordnungsermaechtigung-des-bkv-beim-nb)“ wurde durchgeführt und für die betroffene Marktlokation bzw. Tranche liegt für den Zeitraum, der sich unmittelbar an die Deaktivierung anschließt, keine Zuordnung zu einem BK vor, für den eine aktive Zuordnungsermächtigung vorhanden ist
- für die Marktlokation hat sich ab dem genannten Zeitpunkt der Zeitreihentyp geändert, für den keine gültige Zuordnungsermächtigung vorhanden ist

**Vorher läuft:** [Lieferende von LF an NB](/prozessdoku/202604/LF/GPKE-Teil2-lieferende-von-lf-an-nb) — diese Prozesse nennen den hier gezeigten in ihrem Ergebnis.

</li>

<li data-blatt="erste-nachricht">

### Erste Nachricht

**NB** sendet „Aufhebung der Zuordnung des MSBZ zur Marktlokation bzw. Messlokation“ (Schritt 13). Ab hier ist der Beteiligte dieser Seite am Zug.

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

- [Sicht MSB](/prozessdoku/202604/MSB/GPKE-Teil2-lieferende-von-nb-an-lf) — MSB
- [Sicht LF](/prozessdoku/202604/LF/GPKE-Teil2-lieferende-von-nb-an-lf) — LF
- [Sicht LFZ](/prozessdoku/202604/LF--LFZ/GPKE-Teil2-lieferende-von-nb-an-lf) — Lieferant zukünftig · Marktrolle LF
- [Sicht NB](/prozessdoku/202604/NB/GPKE-Teil2-lieferende-von-nb-an-lf) — NB

<Hinweisbereich>

*Die Schritte sind die **möglichen** Nachrichten dieses Prozesses, keine Abfolge — die Quelle führt weder Bedingungen noch Alternativen. Das Kästchen am Schritt nennt links die eigene Sicht: **←** empfängt sie, **→** sendet sie. Zugeklappte Schritte laufen zwischen anderen Marktpartnern. Die Nummern sind die der Quelle; wo eine fehlt, fehlt sie dort.*

Die Konnektortabelle führt für diese Schritte keinen Schreibaufruf. Abgeleitet aus dem Prozessverlauf: Mit ihrer Nachricht beginnt der Prozess für die eigene Rolle, der Vorgang entsteht also neu.

Betrifft: [13](#schritt-13)

</Hinweisbereich>
