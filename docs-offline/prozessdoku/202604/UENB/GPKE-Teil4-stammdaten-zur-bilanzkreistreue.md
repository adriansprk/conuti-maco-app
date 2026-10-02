# Stammdaten zur Bilanzkreistreue — Sicht ÜNB

<Kopf rolle="UENB" beteiligter="ÜNB" festlegung="GPKE" dokument="GPKE Teil 4" kapitel="2.2" sparte="Strom" schritte={3} suchtitel="Stammdaten zur Bilanzkreistreue — Sicht ÜNB (Marktrolle UENB) · GPKE Teil 4 · Formatversion 202604" abschnitte={[{"id": "abschnitt-ablauf", "label": "Prozessablauf"}, {"id": "abschnitt-schritte", "label": "Prozessschritte"}, {"id": "abschnitt-informationen", "label": "Prozess-Informationen"}, {"id": "abschnitt-sichten", "label": "Andere Sichten des Prozesses"}]} />

<Kurzfassung>

Der NB übermittelt dem ÜNB die Stammdaten zur Bilanzkreistreue. Der ÜNB prüft die Daten und gibt dem NB eine Qualitätsrückmeldung zum Inhalt der Daten. Sofern der ÜNB einen anderen Inhalt der Daten erwartet, gibt er dies in der Rückmeldung an. Der NB teilt dem ÜNB in diesem Fall den Bearbeitungstand zu dessen Rückmeldung mit.

</Kurzfassung>

<a id="abschnitt-ablauf"></a>

## Prozessablauf aus Sicht des ÜNB

<Systembild svg={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1004 545\" width=\"1004\" height=\"545\" role=\"img\" aria-labelledby=\"sb-title\" class=\"maco-systembild\">\n<title id=\"sb-title\">Systembild: Stammdaten zur Bilanzkreistreue aus Sicht ÜNB</title>\n<defs><marker id=\"sb-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect class=\"sb-lane-kopf\" x=\"16\" y=\"12\" width=\"232\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend-System des Kunden</text>\n<rect class=\"sb-lane-kopf\" x=\"398\" y=\"12\" width=\"264\" height=\"46\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · ÜNB</text>\n<rect class=\"sb-lane-kopf\" x=\"812\" y=\"12\" width=\"176\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"900\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Marktpartner</text>\n<line x1=\"323\" y1=\"58\" x2=\"323\" y2=\"533\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"737\" y1=\"58\" x2=\"737\" y2=\"533\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"80\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">1. Stammdaten</text>\n<text x=\"530\" y=\"115\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Bilanzkreistreue</text>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"86\" r=\"5\"/><line x1=\"900\" y1=\"91\" x2=\"900\" y2=\"103\"/><line x1=\"893\" y1=\"95\" x2=\"907\" y2=\"95\"/><line x1=\"900\" y1=\"103\" x2=\"894\" y2=\"113\"/><line x1=\"900\" y1=\"103\" x2=\"906\" y2=\"113\"/></g>\n<text x=\"900\" y=\"135\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"878\" y1=\"104\" x2=\"628\" y2=\"104\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"96\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"120\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">55670</text>\n<rect class=\"sb-kasten sb-schreiben\" x=\"432\" y=\"163\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"183\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"128\" x2=\"530\" y2=\"163\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-schreiben sb-abgeleitet\" x=\"34\" y=\"163\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"183\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten erstellen</text>\n<line x1=\"432\" y1=\"179\" x2=\"230\" y2=\"179\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"171\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"227\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"247\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">2. Rückmeldung auf</text>\n<text x=\"530\" y=\"262\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Stammdaten</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"196\" x2=\"530\" y2=\"227\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"233\" r=\"5\"/><line x1=\"900\" y1=\"238\" x2=\"900\" y2=\"250\"/><line x1=\"893\" y1=\"242\" x2=\"907\" y2=\"242\"/><line x1=\"900\" y1=\"250\" x2=\"894\" y2=\"260\"/><line x1=\"900\" y1=\"250\" x2=\"906\" y2=\"260\"/></g>\n<text x=\"900\" y=\"282\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"628\" y1=\"251\" x2=\"878\" y2=\"251\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"243\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"267\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">55671</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"310\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"330\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"275\" x2=\"530\" y2=\"310\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"310\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"330\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"326\" x2=\"230\" y2=\"326\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"318\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"374\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"394\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">3. Bearbeitungsstand zur</text>\n<text x=\"530\" y=\"409\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Rückmeldung</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"343\" x2=\"530\" y2=\"374\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"380\" r=\"5\"/><line x1=\"900\" y1=\"385\" x2=\"900\" y2=\"397\"/><line x1=\"893\" y1=\"389\" x2=\"907\" y2=\"389\"/><line x1=\"900\" y1=\"397\" x2=\"894\" y2=\"407\"/><line x1=\"900\" y1=\"397\" x2=\"906\" y2=\"407\"/></g>\n<text x=\"900\" y=\"429\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"878\" y1=\"398\" x2=\"628\" y2=\"398\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"390\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"414\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">21047</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"457\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"477\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"422\" x2=\"530\" y2=\"457\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben sb-abgeleitet\" x=\"34\" y=\"457\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"477\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"473\" x2=\"230\" y2=\"473\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"465\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n</svg>"} gesamt={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 730 486\" width=\"730\" height=\"486\" role=\"img\" aria-labelledby=\"sd-title\" class=\"maco-sequence\">\n<title id=\"sd-title\">Sequenzdiagramm: Stammdaten zur Bilanzkreistreue aus Sicht ÜNB</title>\n<defs><marker id=\"sd-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect x=\"16\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"121\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend (Kunde)</text>\n<line x1=\"121\" y1=\"64\" x2=\"121\" y2=\"474\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"260\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"365\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · ÜNB</text>\n<line x1=\"365\" y1=\"64\" x2=\"365\" y2=\"474\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"504\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"609\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"609\" y1=\"64\" x2=\"609\" y2=\"474\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"609\" y1=\"90\" x2=\"365\" y2=\"90\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"81\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">1. Stammdaten Bilanzkreistreue</text>\n<text x=\"487\" y=\"105\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55670</text>\n<line x1=\"365\" y1=\"152\" x2=\"121\" y2=\"152\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"143\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<text x=\"243\" y=\"167\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten erstellen</text>\n<line x1=\"365\" y1=\"214\" x2=\"609\" y2=\"214\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"205\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">2. Rückmeldung auf Stammdaten</text>\n<text x=\"487\" y=\"229\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55671 · E_0574</text>\n<text x=\"487\" y=\"242\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0574 — Stammdaten zur Bilanzkreistreue prüfen</text>\n<line x1=\"365\" y1=\"276\" x2=\"121\" y2=\"276\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"267\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"291\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"609\" y1=\"338\" x2=\"365\" y2=\"338\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"329\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">3. Bearbeitungsstand zur Rückmeldung</text>\n<text x=\"487\" y=\"353\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 21047 · E_0616</text>\n<text x=\"487\" y=\"366\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0616 — Rückmeldung auf Änderung prüfen</text>\n<line x1=\"365\" y1=\"400\" x2=\"121\" y2=\"400\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"391\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"415\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n</svg>"} titel="ÜNB" />

<a id="abschnitt-schritte"></a>

## Prozessschritte

<Schritt nr="1" anker="schritt-1" richtung="eingehend" kopf={{"links": {"label": "ÜNB", "eigen": true}, "rechts": {"label": "NB"}}}>

### Stammdaten Bilanzkreistreue

<Schrittskizze sicht={{"label": "ÜNB"}} zeilen={[{"art": "empfangen", "label": "NB", "weg": "AS4", "nachrichten": [{"nr": "55670", "titel": "Stammdaten BK-Treue"}]}, {"art": "erstellen"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55670](/schnittstellen/202604/pruefi/UTILMD/PI_55670) — Stammdaten BK-Treue · AS4

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
- Vorgang angelegt — `ERSTELLEN_PROZESSDATEN`

Legt im Backend einen neuen Vorgang mit den Daten der eingegangenen Nachricht an.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="2" anker="schritt-2" richtung="ausgehend" kopf={{"links": {"label": "ÜNB", "eigen": true}, "rechts": {"label": "NB"}}}>

### Rückmeldung auf Stammdaten

<Schrittskizze sicht={{"label": "ÜNB"}} zeilen={[{"art": "senden", "label": "NB", "weg": "AS4", "nachrichten": [{"nr": "55671", "titel": "Rückmeldung auf Stammdaten BK-Treue"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55671](/schnittstellen/202604/pruefi/UTILMD/PI_55671) — Rückmeldung auf Stammdaten BK-Treue · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht an **NB** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `55671` → [E_0574](/referenz/202604/ebd/E_0574) · ÜNB · Stammdaten zur Bilanzkreistreue prüfen

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

<Schritt nr="3" anker="schritt-3" richtung="eingehend" kopf={{"links": {"label": "ÜNB", "eigen": true}, "rechts": {"label": "NB"}}}>

### Bearbeitungsstand zur Rückmeldung

<Schrittskizze sicht={{"label": "ÜNB"}} zeilen={[{"art": "empfangen", "label": "NB", "weg": "AS4", "nachrichten": [{"nr": "21047", "titel": "Bearbeitungsstandsmeldung"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [21047](/schnittstellen/202604/pruefi/IFTSTA/PI_21047) — Bearbeitungsstandsmeldung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **NB** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `21047` → [E_0616](/referenz/202604/ebd/E_0616) · NB · Rückmeldung auf Änderung prüfen

</div>

</li>

<li data-teil="schnittstelle" data-art="fortschreiben" data-abgeleitet="ja">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — `AKTUALISIEREN_PROZESSDATEN`

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
| [E_0574](/referenz/202604/ebd/E_0574) | Stammdaten zur Bilanzkreistreue prüfen |
| [E_0616](/referenz/202604/ebd/E_0616) | Rückmeldung auf Änderung prüfen |

</details>

<a id="abschnitt-informationen"></a>

## Prozess-Informationen

Wortlaut der Lesefassung, Steckbrief Kap. 2.1, S. 27.

<Stepper>
<ol>

<li data-blatt="anlass">

### Anlass

Im Fall des Use-Cases „[Abrechnungsdaten Bilanzkreisabrechnung](/prozessdoku/202604/UENB/GPKE-Teil2-abrechnungsdaten-bilanzkreisabrechnung)“ handelt es sich um eine Marktlokation bzw. Tranche
- die ab der erstmaligen Inbetriebnahme der Marktlokation (Neuanlage) mit Bilanzierung auf Basis von Viertelstundenwerten abgebildet wird oder
- bei der von einer Bilanzierung auf Basis von Profilen auf eine Bilanzierung auf Basis von Viertelstundenwerten gewechselt wird oder
- mit Bilanzierung auf Basis von Viertelstundenwerten und Stammdaten zur Bilanzkreistreue haben sich geändert oder
- bei der von einer Bilanzierung auf Basis von Viertelstundenwerten auf eine Bilanzierung auf Basis von Profilen gewechselt wird oder
- mit Bilanzierung auf Basis von Viertelstundenwerten und die Marktlokation wird stillgelegt.

**Vorher läuft:** [Abrechnungsdaten Bilanzkreisabrechnung](/prozessdoku/202604/UENB/GPKE-Teil2-abrechnungsdaten-bilanzkreisabrechnung) — diese Prozesse nennen den hier gezeigten in ihrem Ergebnis.

</li>

<li data-blatt="erste-nachricht">

### Erste Nachricht

**NB** sendet „Stammdaten Bilanzkreistreue“ (Schritt 1). Ab hier ist der Beteiligte dieser Seite am Zug.

</li>

<li data-blatt="ziel">

### Ziel

Die Stammdaten zur Bilanzkreistreue sind ausgetauscht.

</li>

</ol>
</Stepper>

<a id="abschnitt-sichten"></a>

## Andere Sichten des Prozesses

Derselbe Prozess, aus den Augen der anderen Beteiligten: dieselben Schritte, jeweils aus deren Sicht gelesen.

- [Sicht NB](/prozessdoku/202604/NB/GPKE-Teil4-stammdaten-zur-bilanzkreistreue) — NB

<Hinweisbereich>

*Die Schritte sind die **möglichen** Nachrichten dieses Prozesses, keine Abfolge — die Quelle führt weder Bedingungen noch Alternativen. Das Kästchen am Schritt nennt links die eigene Sicht: **←** empfängt sie, **→** sendet sie. Zugeklappte Schritte laufen zwischen anderen Marktpartnern.*

Die Konnektortabelle führt für diese Schritte keinen Schreibaufruf. Abgeleitet aus dem Prozessverlauf: Mit ihrer Nachricht beginnt der Prozess für die eigene Rolle, der Vorgang entsteht also neu.

Betrifft: [1](#schritt-1)

Die Konnektortabelle führt für diese Schritte keinen Schreibaufruf. Abgeleitet aus dem Prozessverlauf: Die eigene Rolle war an diesem Prozess schon beteiligt, der Vorgang besteht also.

Betrifft: [3](#schritt-3)

Für diese Marktrolle liegt kein Schreibkatalog vor; am Schritt steht deshalb nur das Kommando des Schreibaufrufs, ohne Adresse und ohne Knopf.

Betrifft: [1](#schritt-1), [2](#schritt-2), [3](#schritt-3)

</Hinweisbereich>
