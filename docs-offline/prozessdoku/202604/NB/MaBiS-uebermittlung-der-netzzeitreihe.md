# Übermittlung der Netzzeitreihe — Sicht NB

<Kopf rolle="NB" beteiligter="NB" festlegung="MaBiS" dokument="MaBiS" kapitel="5.5.2" sparte="Strom" schritte={2} suchtitel="Übermittlung der Netzzeitreihe — Sicht NB · MaBiS · Formatversion 202604" abschnitte={[{"id": "abschnitt-ablauf", "label": "Prozessablauf"}, {"id": "abschnitt-schritte", "label": "Prozessschritte"}, {"id": "abschnitt-informationen", "label": "Prozess-Informationen"}, {"id": "abschnitt-sichten", "label": "Andere Sichten des Prozesses"}]} />

<Kurzfassung>

Der verantwortliche NB übermittelt die zwischen den beiden NB abgestimmte NZR auf Ebene BG an den BIKO.

</Kurzfassung>

<a id="abschnitt-ablauf"></a>

## Prozessablauf aus Sicht des NB

<Systembild svg={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1004 398\" width=\"1004\" height=\"398\" role=\"img\" aria-labelledby=\"sb-title\" class=\"maco-systembild\">\n<title id=\"sb-title\">Systembild: Übermittlung der Netzzeitreihe aus Sicht NB</title>\n<defs><marker id=\"sb-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect class=\"sb-lane-kopf\" x=\"16\" y=\"12\" width=\"232\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend-System des Kunden</text>\n<rect class=\"sb-lane-kopf\" x=\"398\" y=\"12\" width=\"264\" height=\"46\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · NB</text>\n<rect class=\"sb-lane-kopf\" x=\"812\" y=\"12\" width=\"176\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"900\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Marktpartner</text>\n<line x1=\"323\" y1=\"58\" x2=\"323\" y2=\"386\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"737\" y1=\"58\" x2=\"737\" y2=\"386\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"80\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">1. Übermittlung NZR</text>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"78\" r=\"5\"/><line x1=\"900\" y1=\"83\" x2=\"900\" y2=\"95\"/><line x1=\"893\" y1=\"87\" x2=\"907\" y2=\"87\"/><line x1=\"900\" y1=\"95\" x2=\"894\" y2=\"105\"/><line x1=\"900\" y1=\"95\" x2=\"906\" y2=\"105\"/></g>\n<text x=\"900\" y=\"127\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">BIKO</text>\n<line x1=\"628\" y1=\"96\" x2=\"878\" y2=\"96\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"88\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"112\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">13003</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"163\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"183\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"113\" x2=\"530\" y2=\"163\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"163\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"183\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"179\" x2=\"230\" y2=\"179\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"171\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"227\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"247\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">2. Antwort</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"196\" x2=\"530\" y2=\"227\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"225\" r=\"5\"/><line x1=\"900\" y1=\"230\" x2=\"900\" y2=\"242\"/><line x1=\"893\" y1=\"234\" x2=\"907\" y2=\"234\"/><line x1=\"900\" y1=\"242\" x2=\"894\" y2=\"252\"/><line x1=\"900\" y1=\"242\" x2=\"906\" y2=\"252\"/></g>\n<text x=\"900\" y=\"274\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">BIKO</text>\n<line x1=\"878\" y1=\"243\" x2=\"628\" y2=\"243\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"235\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"259\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">21002</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"310\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"330\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"260\" x2=\"530\" y2=\"310\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben sb-abgeleitet\" x=\"34\" y=\"310\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"330\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"326\" x2=\"230\" y2=\"326\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"318\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n</svg>"} gesamt={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 730 362\" width=\"730\" height=\"362\" role=\"img\" aria-labelledby=\"sd-title\" class=\"maco-sequence\">\n<title id=\"sd-title\">Sequenzdiagramm: Übermittlung der Netzzeitreihe aus Sicht NB</title>\n<defs><marker id=\"sd-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect x=\"16\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"121\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend (Kunde)</text>\n<line x1=\"121\" y1=\"64\" x2=\"121\" y2=\"350\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"260\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"365\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · NB</text>\n<line x1=\"365\" y1=\"64\" x2=\"365\" y2=\"350\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"504\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"609\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">BIKO</text>\n<line x1=\"609\" y1=\"64\" x2=\"609\" y2=\"350\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"365\" y1=\"90\" x2=\"609\" y2=\"90\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"81\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">1. Übermittlung NZR</text>\n<text x=\"487\" y=\"105\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 13003</text>\n<line x1=\"365\" y1=\"152\" x2=\"121\" y2=\"152\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"143\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"167\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"609\" y1=\"214\" x2=\"365\" y2=\"214\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"205\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">2. Antwort</text>\n<text x=\"487\" y=\"229\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 21002 · E_0008</text>\n<text x=\"487\" y=\"242\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0008 — NZR prüfen</text>\n<line x1=\"365\" y1=\"276\" x2=\"121\" y2=\"276\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"267\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"291\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n</svg>"} titel="NB" />

<a id="abschnitt-schritte"></a>

## Prozessschritte

<Schritt nr="1" anker="schritt-1" richtung="ausgehend" kopf={{"links": {"label": "NB", "eigen": true}, "rechts": {"label": "BIKO"}}}>

### Übermittlung NZR

<Schrittskizze sicht={{"label": "NB"}} zeilen={[{"art": "senden", "label": "BIKO", "weg": "AS4", "nachrichten": [{"nr": "13003", "titel": "Summenzeitreihe"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [13003](/schnittstellen/202604/pruefi/MSCONS/PI_13003) — Summenzeitreihe · AS4

</div>

**Ablauf**

<div data-ablauf data-offen="ja">

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht an **BIKO** · AS4

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202604/backend-schreiben-nb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend fort, nachdem die Nachricht erstellt ist.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="2" anker="schritt-2" richtung="eingehend" kopf={{"links": {"label": "NB", "eigen": true}, "rechts": {"label": "BIKO"}}}>

### Antwort

<Schrittskizze sicht={{"label": "NB"}} zeilen={[{"art": "empfangen", "label": "BIKO", "weg": "AS4", "nachrichten": [{"nr": "21002", "titel": "Abweisung"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [21002](/schnittstellen/202604/pruefi/IFTSTA/PI_21002) — Abweisung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **BIKO** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `21002` → [E_0008](/referenz/202604/ebd/E_0008) · BIKO · NZR prüfen

</div>

</li>

<li data-teil="schnittstelle" data-art="fortschreiben" data-abgeleitet="ja">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202604/backend-schreiben-nb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

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
| [E_0008](/referenz/202604/ebd/E_0008) | NZR prüfen |

</details>

<a id="abschnitt-informationen"></a>

## Prozess-Informationen

Wortlaut der Lesefassung, Steckbrief Kap. 5.5.1, S. 52.

<Stepper>
<ol>

<li data-blatt="vorbedingungen">

### Vorbedingungen

- Der MaBiS-ZP für die NZR ist vom verantwortlichen NB beim BIKO für den betreffenden Zeitraum aktiviert.
- Die Abstimmung der NZR zwischen den beiden NB ist erfolgt.
- Die zwischen den NB abgestimmte Version der NZR ist dem verantwortlichen NB bekannt.

</li>

<li data-blatt="ergebnisse">

### Ergebnisse

Der BIKO kann die NZR für die Berechnung der NB-DZR berücksichtigen und den Datenstatus (Abrechnungsdaten/Abrechnungsdaten KBKA) an die beiden NB übermitteln.

</li>

<li data-blatt="anforderungen">

### Weitere Anforderungen

Die Darstellung der Energieflussrichtungen bei der NZR wird immer aus Sicht des BG des verantwortlichen NB übermittelt. Die an den BIKO übermittelte NZR gilt im Rahmen der BKA als unter den beiden NB abgestimmte Version. Sollten zwischen der abgestimmten und der an den BIKO übermittelten NZR Differenzen vorhanden sein, ist dies bilateral zwischen den beiden NB zu klären.

</li>

<li data-blatt="erste-nachricht">

### Erste Nachricht

Der Beteiligte dieser Seite sendet selbst: „Übermittlung NZR“ an **BIKO** (Schritt 1).

</li>

<li data-blatt="ziel">

### Ziel

Dem BIKO liegt die zwischen den beiden NB abgestimmte Version der NZR vor.

</li>

</ol>
</Stepper>

<a id="abschnitt-sichten"></a>

## Andere Sichten des Prozesses

Derselbe Prozess, aus den Augen der anderen Beteiligten: dieselben Schritte, jeweils aus deren Sicht gelesen.

- [Sicht BIKO](/prozessdoku/202604/BIKO/MaBiS-uebermittlung-der-netzzeitreihe) — BIKO

<Hinweisbereich>

*Die Schritte sind die **möglichen** Nachrichten dieses Prozesses, keine Abfolge — die Quelle führt weder Bedingungen noch Alternativen. Das Kästchen am Schritt nennt links die eigene Sicht: **←** empfängt sie, **→** sendet sie. Zugeklappte Schritte laufen zwischen anderen Marktpartnern.*

Welches Ereignis diese Schritte anstößt, benennt die Quelle noch nicht.

Betrifft: [1](#schritt-1)

Die Konnektortabelle führt für diese Schritte keinen Schreibaufruf. Abgeleitet aus dem Prozessverlauf: Die eigene Rolle war an diesem Prozess schon beteiligt, der Vorgang besteht also.

Betrifft: [2](#schritt-2)

Zu den Prüfidentifikatoren dieser Schritte liegt kein Testfall im Testbestand; der Knopf »Ausprobieren« der schreibenden Schnittstelle bietet deshalb keinen Rumpf an.

Betrifft: [1](#schritt-1), [2](#schritt-2)

</Hinweisbereich>
