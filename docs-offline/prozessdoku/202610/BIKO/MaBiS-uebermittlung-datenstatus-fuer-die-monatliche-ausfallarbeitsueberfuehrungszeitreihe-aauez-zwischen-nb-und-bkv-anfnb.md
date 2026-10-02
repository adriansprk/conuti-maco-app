# Übermittlung Datenstatus für die monatliche Ausfallarbeitsüberführungszeitreihe (AAÜZ) zwischen NB und BKV (anfNB) — Sicht BIKO

<Kopf rolle="BIKO" beteiligter="BIKO" festlegung="MaBiS" dokument="MaBiS" kapitel="17.3.5.5.2" sparte="Strom" schritte={2} suchtitel="Übermittlung Datenstatus für die monatliche Ausfallarbeitsüberführungszeitreihe (AAÜZ) zwischen NB und BKV (anfNB) — Sicht BIKO · MaBiS · Formatversion 202610" abschnitte={[{"id": "abschnitt-ablauf", "label": "Prozessablauf"}, {"id": "abschnitt-schritte", "label": "Prozessschritte"}, {"id": "abschnitt-informationen", "label": "Prozess-Informationen"}, {"id": "abschnitt-sichten", "label": "Andere Sichten des Prozesses"}]} />

<Kurzfassung>

Der BIKO übermittelt den Datenstatus für die AAÜZ an den BKV (des anfNB) und an den ANB.
- nach Eingang der AAÜZ vom NB oder
- nach Eingang der Prüfmitteilung vom BKV (anfNB) oder
- nach Verwendung der AAÜZ für die BKA (ohne KBKA) oder die KBKA.

</Kurzfassung>

<a id="abschnitt-ablauf"></a>

## Prozessablauf aus Sicht des BIKO

<Systembild svg={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1004 398\" width=\"1004\" height=\"398\" role=\"img\" aria-labelledby=\"sb-title\" class=\"maco-systembild\">\n<title id=\"sb-title\">Systembild: Übermittlung Datenstatus für die monatliche Ausfallarbeitsüberführungszeitreihe (AAÜZ) zwischen NB und BKV (anfNB) aus Sicht BIKO</title>\n<defs><marker id=\"sb-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect class=\"sb-lane-kopf\" x=\"16\" y=\"12\" width=\"232\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend-System des Kunden</text>\n<rect class=\"sb-lane-kopf\" x=\"398\" y=\"12\" width=\"264\" height=\"46\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · BIKO</text>\n<rect class=\"sb-lane-kopf\" x=\"812\" y=\"12\" width=\"176\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"900\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Marktpartner</text>\n<line x1=\"323\" y1=\"58\" x2=\"323\" y2=\"386\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"737\" y1=\"58\" x2=\"737\" y2=\"386\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"80\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">1. Datenstatus für die</text>\n<text x=\"530\" y=\"115\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">monatliche AAÜZ</text>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"86\" r=\"5\"/><line x1=\"900\" y1=\"91\" x2=\"900\" y2=\"103\"/><line x1=\"893\" y1=\"95\" x2=\"907\" y2=\"95\"/><line x1=\"900\" y1=\"103\" x2=\"894\" y2=\"113\"/><line x1=\"900\" y1=\"103\" x2=\"906\" y2=\"113\"/></g>\n<text x=\"900\" y=\"135\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">BKV (des anfNB)</text>\n<line x1=\"628\" y1=\"104\" x2=\"878\" y2=\"104\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"96\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"120\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">21004</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"163\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"183\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"128\" x2=\"530\" y2=\"163\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"163\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"183\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"179\" x2=\"230\" y2=\"179\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"171\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"227\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"247\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">2. Datenstatus für die</text>\n<text x=\"530\" y=\"262\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">monatliche AAÜZ</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"196\" x2=\"530\" y2=\"227\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"233\" r=\"5\"/><line x1=\"900\" y1=\"238\" x2=\"900\" y2=\"250\"/><line x1=\"893\" y1=\"242\" x2=\"907\" y2=\"242\"/><line x1=\"900\" y1=\"250\" x2=\"894\" y2=\"260\"/><line x1=\"900\" y1=\"250\" x2=\"906\" y2=\"260\"/></g>\n<text x=\"900\" y=\"282\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">NB (ANB)</text>\n<line x1=\"628\" y1=\"251\" x2=\"878\" y2=\"251\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"243\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"267\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">21003</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"310\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"330\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"275\" x2=\"530\" y2=\"310\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"310\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"330\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"326\" x2=\"230\" y2=\"326\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"318\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n</svg>"} gesamt={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 974 414\" width=\"974\" height=\"414\" role=\"img\" aria-labelledby=\"sd-title\" class=\"maco-sequence\">\n<title id=\"sd-title\">Sequenzdiagramm: Übermittlung Datenstatus für die monatliche Ausfallarbeitsüberführungszeitreihe (AAÜZ) zwischen NB und BKV (anfNB) aus Sicht BIKO</title>\n<defs><marker id=\"sd-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect x=\"16\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"121\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend (Kunde)</text>\n<line x1=\"121\" y1=\"64\" x2=\"121\" y2=\"402\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"260\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"365\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · BIKO</text>\n<line x1=\"365\" y1=\"64\" x2=\"365\" y2=\"402\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"504\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"609\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">BKV (des anfNB)</text>\n<line x1=\"609\" y1=\"64\" x2=\"609\" y2=\"402\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"748\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"853\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">NB (ANB)</text>\n<line x1=\"853\" y1=\"64\" x2=\"853\" y2=\"402\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"365\" y1=\"90\" x2=\"609\" y2=\"90\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"81\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">1. Datenstatus für die monatliche AAÜZ</text>\n<text x=\"487\" y=\"105\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 21004 · E_0082, E_0083…</text>\n<text x=\"487\" y=\"118\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0082 — Datenstatus AAÜZ nach erfolgter BKA vergeben</text>\n<text x=\"487\" y=\"131\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0083 — Datenstatus nach Eingang einer AAÜZ vergeben</text>\n<text x=\"487\" y=\"144\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0084 — Datenstatus nach Vorliegen einer Prüfmitteilung zur AAÜZ verge…</text>\n<line x1=\"365\" y1=\"178\" x2=\"121\" y2=\"178\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"169\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"193\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"365\" y1=\"240\" x2=\"853\" y2=\"240\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"609\" y=\"231\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">2. Datenstatus für die monatliche AAÜZ</text>\n<text x=\"609\" y=\"255\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 21003 · E_0082, E_0083…</text>\n<text x=\"609\" y=\"268\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0082 — Datenstatus AAÜZ nach erfolgter BKA vergeben</text>\n<text x=\"609\" y=\"281\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0083 — Datenstatus nach Eingang einer AAÜZ vergeben</text>\n<text x=\"609\" y=\"294\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0084 — Datenstatus nach Vorliegen einer Prüfmitteilung zur AAÜZ verge…</text>\n<line x1=\"365\" y1=\"328\" x2=\"121\" y2=\"328\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"319\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"343\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n</svg>"} titel="BIKO" />

<a id="abschnitt-schritte"></a>

## Prozessschritte

<Schritt nr="1" anker="schritt-1" richtung="ausgehend" kopf={{"links": {"label": "BIKO", "eigen": true}, "rechts": {"label": "BKV (des anfNB)"}}}>

### Datenstatus für die monatliche AAÜZ

<Schrittskizze sicht={{"label": "BIKO"}} zeilen={[{"art": "senden", "label": "BKV (des anfNB)", "weg": "AS4", "nachrichten": [{"nr": "21004", "titel": "Statusmeldung"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [21004](/schnittstellen/202610/pruefi/IFTSTA/PI_21004) — Statusmeldung · AS4

</div>

**Ablauf**

<div data-ablauf data-offen="ja">

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht an **BKV (des anfNB)** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `21004` → [E_0082](/referenz/202610/ebd/E_0082) · BIKO · Datenstatus AAÜZ nach erfolgter BKA vergeben
- `21004` → [E_0083](/referenz/202610/ebd/E_0083) · BIKO · Datenstatus nach Eingang einer AAÜZ vergeben
- `21004` → [E_0084](/referenz/202610/ebd/E_0084) · BIKO · Datenstatus nach Vorliegen einer Prüfmitteilung zur AAÜZ vergeben

</div>

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — `AKTUALISIEREN_PROZESSDATEN`

Schreibt den bestehenden Vorgang im Backend fort, nachdem die Nachricht erstellt ist.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="2" anker="schritt-2" richtung="ausgehend" kopf={{"links": {"label": "BIKO", "eigen": true}, "rechts": {"label": "NB (ANB)"}}}>

### Datenstatus für die monatliche AAÜZ

<Schrittskizze sicht={{"label": "BIKO"}} zeilen={[{"art": "senden", "label": "NB (ANB)", "weg": "AS4", "nachrichten": [{"nr": "21003", "titel": "Statusmeldung"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [21003](/schnittstellen/202610/pruefi/IFTSTA/PI_21003) — Statusmeldung · AS4

</div>

**Ablauf**

<div data-ablauf data-offen="ja">

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht an **NB (ANB)** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `21003` → [E_0082](/referenz/202610/ebd/E_0082) · BIKO · Datenstatus AAÜZ nach erfolgter BKA vergeben
- `21003` → [E_0083](/referenz/202610/ebd/E_0083) · BIKO · Datenstatus nach Eingang einer AAÜZ vergeben
- `21003` → [E_0084](/referenz/202610/ebd/E_0084) · BIKO · Datenstatus nach Vorliegen einer Prüfmitteilung zur AAÜZ vergeben

</div>

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — `AKTUALISIEREN_PROZESSDATEN`

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
| [E_0082](/referenz/202610/ebd/E_0082) | Datenstatus AAÜZ nach erfolgter BKA vergeben |
| [E_0083](/referenz/202610/ebd/E_0083) | Datenstatus nach Eingang einer AAÜZ vergeben |
| [E_0084](/referenz/202610/ebd/E_0084) | Datenstatus nach Vorliegen einer Prüfmitteilung zur AAÜZ vergeben |

</details>

<a id="abschnitt-informationen"></a>

## Prozess-Informationen

Wortlaut der Lesefassung, Steckbrief Kap. 17.3.5.5.1, S. 280–281.

<Stepper>
<ol>

<li data-blatt="ergebnisse">

### Ergebnisse

Alle Systeme von BKV, ANB und BIKO führen den gleichen Datenstatus zu einer Version der AAÜZ.

</li>

<li data-blatt="fehlerfall">

### Fehlerfall

#### Ergebnis im Fehlerfall

Der BIKO informiert alle betroffenen Marktteilnehmer und sorgt nach Korrektur des Fehlers für die Zuweisung des richtigen Datenstatus zu allen betroffenen AAÜZ.

#### Fehlerfälle

Der vom BIKO angewandte Algorithmus zur Vergabe des Datenstatus ist fehlerhaft.

</li>

<li data-blatt="erste-nachricht">

### Erste Nachricht

Der Beteiligte dieser Seite sendet selbst: „Datenstatus für die monatliche AAÜZ“ an **BKV (des anfNB)** (Schritt 1).

</li>

<li data-blatt="ziel">

### Ziel

Der vom BIKO verwaltete Datenstatus liegt den BKV (des anfNB und des ANB) für die AAÜZ vor.

</li>

</ol>
</Stepper>

<a id="abschnitt-sichten"></a>

## Andere Sichten des Prozesses

Derselbe Prozess, aus den Augen der anderen Beteiligten: dieselben Schritte, jeweils aus deren Sicht gelesen.

- [Sicht ANB](/prozessdoku/202610/NB/MaBiS-uebermittlung-datenstatus-fuer-die-monatliche-ausfallarbeitsueberfuehrungszeitreihe-aauez-zwischen-nb-und-bkv-anfnb) — Anschlussnetzbetreiber · Marktrolle NB
- [Sicht BKV-ANFNB](/prozessdoku/202610/BKV/MaBiS-uebermittlung-datenstatus-fuer-die-monatliche-ausfallarbeitsueberfuehrungszeitreihe-aauez-zwischen-nb-und-bkv-anfnb) — Bilanzkreisverantwortlicher des anfordernden Netzbetreibers · Marktrolle BKV

<Hinweisbereich>

*Die Schritte sind die **möglichen** Nachrichten dieses Prozesses, keine Abfolge — die Quelle führt weder Bedingungen noch Alternativen. Das Kästchen am Schritt nennt links die eigene Sicht: **←** empfängt sie, **→** sendet sie. Zugeklappte Schritte laufen zwischen anderen Marktpartnern.*

Welches Ereignis diese Schritte anstößt, benennt die Quelle noch nicht.

Betrifft: [1](#schritt-1), [2](#schritt-2)

Für diese Marktrolle liegt kein Schreibkatalog vor; am Schritt steht deshalb nur das Kommando des Schreibaufrufs, ohne Adresse und ohne Knopf.

Betrifft: [1](#schritt-1), [2](#schritt-2)

</Hinweisbereich>
