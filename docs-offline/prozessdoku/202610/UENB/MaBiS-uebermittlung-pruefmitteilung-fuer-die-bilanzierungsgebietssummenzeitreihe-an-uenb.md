# Übermittlung Prüfmitteilung für die Bilanzierungsgebietssummenzeitreihe an ÜNB — Sicht ÜNB

<Kopf rolle="UENB" beteiligter="ÜNB" festlegung="MaBiS" dokument="MaBiS" kapitel="9.8.2" sparte="Strom" schritte={3} suchtitel="Übermittlung Prüfmitteilung für die Bilanzierungsgebietssummenzeitreihe an ÜNB — Sicht ÜNB (Marktrolle UENB) · MaBiS · Formatversion 202610" abschnitte={[{"id": "abschnitt-ablauf", "label": "Prozessablauf"}, {"id": "abschnitt-schritte", "label": "Prozessschritte"}, {"id": "abschnitt-informationen", "label": "Prozess-Informationen"}, {"id": "abschnitt-sichten", "label": "Andere Sichten des Prozesses"}]} />

<Kurzfassung>

Der NB prüft eine vorliegende Version der BG-SZR (Kategorie B) und übermittelt die dazugehörige Prüfmitteilung an den BIKO. Dabei kann der NB dem ÜNB auch über das Ende der Clearingfrist der BKA (ohne KBKA) hinaus mittels einer negativen Prüfmitteilung anzeigen, dass er die für die BKA (ohne KBKA) verwendeten Daten für korrekturbedürftig hält und somit die Übermittlung korrigierter Daten für die KBKA erwartet. Eine positive Prüfmitteilung des NB für eine Version der BG-SZR (Kategorie B), die nach Ablauf der Clearingfrist der BKA (ohne KBKA) vom BIKO empfangen wird, wird an den ÜNB weitergegeben und der Datenstatus wird auf „Abrechnungsdaten KBKA“ gesetzt. Eine negative Prüfmitteilung des NB für eine Version der BG-SZR (Kategorie B), die nach Ablauf der Clearingfrist der BKA (ohne KBKA) vom BIKO empfangen wird, wird an den ÜNB weitergegeben und bewirkt aber keine Änderung des bestehenden Datenstatus. Der BIKO leitet die Prüfmitteilung an den ÜNB weiter, sofern diese nicht aufgrund von Überschreitung der Clearingfrist der KBKA abgelehnt wird.

</Kurzfassung>

<a id="abschnitt-ablauf"></a>

## Prozessablauf aus Sicht des ÜNB

<Systembild svg={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1004 257\" width=\"1004\" height=\"257\" role=\"img\" aria-labelledby=\"sb-title\" class=\"maco-systembild\">\n<title id=\"sb-title\">Systembild: Übermittlung Prüfmitteilung für die Bilanzierungsgebietssummenzeitreihe an ÜNB aus Sicht ÜNB</title>\n<defs><marker id=\"sb-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect class=\"sb-lane-kopf\" x=\"16\" y=\"12\" width=\"232\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend-System des Kunden</text>\n<rect class=\"sb-lane-kopf\" x=\"398\" y=\"12\" width=\"264\" height=\"46\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · ÜNB</text>\n<rect class=\"sb-lane-kopf\" x=\"812\" y=\"12\" width=\"176\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"900\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Marktpartner</text>\n<line x1=\"323\" y1=\"58\" x2=\"323\" y2=\"245\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"737\" y1=\"58\" x2=\"737\" y2=\"245\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"80\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">3. Weiterleitung</text>\n<text x=\"530\" y=\"115\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prüfmitteilung BG-SZR</text>\n<text x=\"530\" y=\"130\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">(Kategorie B)</text>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"93\" r=\"5\"/><line x1=\"900\" y1=\"98\" x2=\"900\" y2=\"110\"/><line x1=\"893\" y1=\"102\" x2=\"907\" y2=\"102\"/><line x1=\"900\" y1=\"110\" x2=\"894\" y2=\"120\"/><line x1=\"900\" y1=\"110\" x2=\"906\" y2=\"120\"/></g>\n<text x=\"900\" y=\"142\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">BIKO</text>\n<line x1=\"878\" y1=\"111\" x2=\"628\" y2=\"111\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"103\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"127\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">21003</text>\n<rect class=\"sb-kasten sb-schreiben\" x=\"432\" y=\"169\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"189\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"143\" x2=\"530\" y2=\"169\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-schreiben sb-abgeleitet\" x=\"34\" y=\"169\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"189\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten erstellen</text>\n<line x1=\"432\" y1=\"185\" x2=\"230\" y2=\"185\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"177\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n</svg>"} gesamt={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 974 362\" width=\"974\" height=\"362\" role=\"img\" aria-labelledby=\"sd-title\" class=\"maco-sequence\">\n<title id=\"sd-title\">Sequenzdiagramm: Übermittlung Prüfmitteilung für die Bilanzierungsgebietssummenzeitreihe an ÜNB aus Sicht ÜNB</title>\n<defs><marker id=\"sd-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect x=\"16\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"121\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend (Kunde)</text>\n<line x1=\"121\" y1=\"64\" x2=\"121\" y2=\"350\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"260\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"365\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · ÜNB</text>\n<line x1=\"365\" y1=\"64\" x2=\"365\" y2=\"350\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"504\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"609\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"609\" y1=\"64\" x2=\"609\" y2=\"350\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"748\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"853\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">BIKO</text>\n<line x1=\"853\" y1=\"64\" x2=\"853\" y2=\"350\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"609\" y1=\"90\" x2=\"853\" y2=\"90\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"731\" y=\"81\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">1. Prüfmitteilung BG-SZR (Kategorie B)</text>\n<text x=\"731\" y=\"105\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 21005 · E_0062</text>\n<text x=\"731\" y=\"118\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0062 — BG-SZR (Kategorie B) prüfen</text>\n<line x1=\"853\" y1=\"152\" x2=\"609\" y2=\"152\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"731\" y=\"143\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">2. Abweisung der Prüfmitteilung BG-SZR (Kategori…</text>\n<text x=\"731\" y=\"167\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 21004 · E_0019</text>\n<text x=\"731\" y=\"180\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0019 — Prüfmitteilung prüfen</text>\n<line x1=\"853\" y1=\"214\" x2=\"365\" y2=\"214\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"609\" y=\"205\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">3. Weiterleitung Prüfmitteilung BG-SZR (Kategori…</text>\n<text x=\"609\" y=\"229\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 21003 · E_0062</text>\n<text x=\"609\" y=\"242\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0062 — BG-SZR (Kategorie B) prüfen</text>\n<line x1=\"365\" y1=\"276\" x2=\"121\" y2=\"276\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"267\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<text x=\"243\" y=\"291\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten erstellen</text>\n</svg>"} titel="ÜNB" />

<a id="abschnitt-schritte"></a>

## Prozessschritte

<Schritt nr="1" anker="schritt-1" richtung="fremd" kopf={{"links": {"label": "NB", "eigen": false}, "rechts": {"label": "BIKO"}}}>

### Prüfmitteilung BG-SZR (Kategorie B)

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [21005](/schnittstellen/202610/pruefi/IFTSTA/PI_21005) — Statusmeldung · AS4

</div>

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `21005` → [E_0062](/referenz/202610/ebd/E_0062) · NB · BG-SZR (Kategorie B) prüfen

</div>

</Schritt>

<Schritt nr="2" anker="schritt-2" richtung="fremd" kopf={{"links": {"label": "BIKO", "eigen": false}, "rechts": {"label": "NB"}}}>

### Abweisung der Prüfmitteilung BG-SZR (Kategorie B)

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [21004](/schnittstellen/202610/pruefi/IFTSTA/PI_21004) — Statusmeldung · AS4

</div>

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `21004` → [E_0019](/referenz/202610/ebd/E_0019) · BIKO · Prüfmitteilung prüfen

</div>

</Schritt>

<Schritt nr="3" anker="schritt-3" richtung="eingehend" kopf={{"links": {"label": "ÜNB", "eigen": true}, "rechts": {"label": "BIKO"}}}>

### Weiterleitung Prüfmitteilung BG-SZR (Kategorie B)

<Schrittskizze sicht={{"label": "ÜNB"}} zeilen={[{"art": "empfangen", "label": "BIKO", "weg": "AS4", "nachrichten": [{"nr": "21003", "titel": "Statusmeldung"}]}, {"art": "erstellen"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [21003](/schnittstellen/202610/pruefi/IFTSTA/PI_21003) — Statusmeldung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **BIKO** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `21003` → [E_0062](/referenz/202610/ebd/E_0062) · NB · BG-SZR (Kategorie B) prüfen

</div>

</li>

<li data-teil="schnittstelle" data-art="schreiben" data-abgeleitet="ja">

**Schreibende Schnittstelle**
- Vorgang angelegt — `ERSTELLEN_PROZESSDATEN`

Legt im Backend einen neuen Vorgang mit den Daten der eingegangenen Nachricht an.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<details>
<summary>Entscheidungsbäume dieses Prozesses</summary>

| EBD | Name |
|---|---|
| [E_0062](/referenz/202610/ebd/E_0062) | BG-SZR (Kategorie B) prüfen |
| [E_0019](/referenz/202610/ebd/E_0019) | Prüfmitteilung prüfen |

</details>

<a id="abschnitt-informationen"></a>

## Prozess-Informationen

Wortlaut der Lesefassung, Steckbrief Kap. 9.8.1, S. 114–115.

<Stepper>
<ol>

<li data-blatt="vorbedingungen">

### Vorbedingungen

- Der ÜNB hat die BG-SZR (Kategorie B) gebildet und an den BIKO erfolgreich übermittelt.
- Der BIKO hat die BG-SZR (Kategorie B) in der Kette an den NB weitergeleitet.

</li>

<li data-blatt="ergebnisse">

### Ergebnisse

- Der ÜNB übermittelt bei Erhalt einer negativen Prüfmitteilung ggf. eine korrigierte BG-SZR (Kategorie B).
- Der BIKO kann den Datenstatus bilden und an den NB und ÜNB übermitteln.

</li>

<li data-blatt="erste-nachricht">

### Erste Nachricht

**BIKO** sendet „Weiterleitung Prüfmitteilung BG-SZR (Kategorie B)“ (Schritt 3). Ab hier ist der Beteiligte dieser Seite am Zug.

</li>

<li data-blatt="ziel">

### Ziel

- Der NB hat die BG-SZR (Kategorie B) gegen seine Daten geprüft und hat sein Prüfergebnis an den BIKO übermittelt.
- Der BIKO hat dieses an den ÜNB weitergeleitet.
- Der ÜNB kennt die Erwartungshaltung (Korrekturbedarf oder Akzeptanz) des NB für die BG-SZR (Kategorie B) des betrachteten Zeitraums.

</li>

</ol>
</Stepper>

<a id="abschnitt-sichten"></a>

## Andere Sichten des Prozesses

Derselbe Prozess, aus den Augen der anderen Beteiligten: dieselben Schritte, jeweils aus deren Sicht gelesen.

- [Sicht NB](/prozessdoku/202610/NB/MaBiS-uebermittlung-pruefmitteilung-fuer-die-bilanzierungsgebietssummenzeitreihe-an-uenb) — NB
- [Sicht BIKO](/prozessdoku/202610/BIKO/MaBiS-uebermittlung-pruefmitteilung-fuer-die-bilanzierungsgebietssummenzeitreihe-an-uenb) — BIKO

<Hinweisbereich>

*Die Schritte sind die **möglichen** Nachrichten dieses Prozesses, keine Abfolge — die Quelle führt weder Bedingungen noch Alternativen. Das Kästchen am Schritt nennt links die eigene Sicht: **←** empfängt sie, **→** sendet sie. Zugeklappte Schritte laufen zwischen anderen Marktpartnern.*

Die Konnektortabelle führt für diese Schritte keinen Schreibaufruf. Abgeleitet aus dem Prozessverlauf: Mit ihrer Nachricht beginnt der Prozess für die eigene Rolle, der Vorgang entsteht also neu.

Betrifft: [3](#schritt-3)

Für diese Marktrolle liegt kein Schreibkatalog vor; am Schritt steht deshalb nur das Kommando des Schreibaufrufs, ohne Adresse und ohne Knopf.

Betrifft: [3](#schritt-3)

</Hinweisbereich>
