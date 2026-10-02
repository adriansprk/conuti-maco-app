# Reklamation vom LF — Sicht LF

<Kopf rolle="LF" beteiligter="LF" festlegung="WiM" dokument="WiM Strom Teil 2" kapitel="2.7.4" sparte="Strom" schritte={5} suchtitel="Reklamation vom LF — Sicht LF · WiM Strom Teil 2 · Formatversion 202610" abschnitte={[{"id": "abschnitt-ablauf", "label": "Prozessablauf"}, {"id": "abschnitt-schritte", "label": "Prozessschritte"}, {"id": "abschnitt-informationen", "label": "Prozess-Informationen"}, {"id": "abschnitt-sichten", "label": "Andere Sichten des Prozesses"}]} />

<Kurzfassung>

Der NB, LF oder ÜNB reklamiert bei dem MSB der Marktlokation unplausible oder fehlende Werte (Marktlokation / Messlokation), der zu dem Zeitraum, für den die Werte zu reklamieren sind, der Marktlokation zugeordnet war oder der MSB der Marktlokation reklamiert bei dem MSB der Messlokation unplausible oder fehlende Werte der Messlokation, der zu dem Zeitraum, für den die Werte zu reklamieren sind, der Messlokation zugeordnet war oder der MSB der Marktlokation bzw. der MSB der Messlokation erkennt, dass Werte durch ihn nicht versendet wurden oder durch ihn korrigiert werden müssen, ohne dass eine Reklamation einer anderen Marktrolle eingegangen ist. Der entsprechende MSB prüft die Reklamation der betroffenen Werte. Entsprechend der Prüfergebnisse übermittelt der MSB Werte (inklusive verbindlicher Information zur Begründung der Änderung der Werte), sofern diese noch nicht übermittelt wurden (bei nichtvorhandenen Werten) bzw. korrigierte Werte (bei fehlerhaften Werten) und storniert ggf. fehlerhafte Werte oder lehnt die Reklamation ab.

</Kurzfassung>

<a id="abschnitt-ablauf"></a>

## Prozessablauf aus Sicht des LF

<Systembild svg={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1004 737\" width=\"1004\" height=\"737\" role=\"img\" aria-labelledby=\"sb-title\" class=\"maco-systembild\">\n<title id=\"sb-title\">Systembild: Reklamation vom LF aus Sicht LF</title>\n<defs><marker id=\"sb-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect class=\"sb-lane-kopf\" x=\"16\" y=\"12\" width=\"232\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend-System des Kunden</text>\n<rect class=\"sb-lane-kopf\" x=\"398\" y=\"12\" width=\"264\" height=\"46\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · LF</text>\n<rect class=\"sb-lane-kopf\" x=\"812\" y=\"12\" width=\"176\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"900\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Marktpartner</text>\n<line x1=\"323\" y1=\"58\" x2=\"323\" y2=\"725\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"737\" y1=\"58\" x2=\"737\" y2=\"725\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect class=\"sb-kasten sb-trigger\" x=\"432\" y=\"80\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessauslöser empfangen</text>\n<rect class=\"sb-kasten sb-backend sb-trigger\" x=\"34\" y=\"80\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">2 Ereignisse, alternativ</text>\n<line x1=\"230\" y1=\"96\" x2=\"432\" y2=\"96\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"88\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"144\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"164\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">1. Reklamation Wert</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"113\" x2=\"530\" y2=\"144\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"142\" r=\"5\"/><line x1=\"900\" y1=\"147\" x2=\"900\" y2=\"159\"/><line x1=\"893\" y1=\"151\" x2=\"907\" y2=\"151\"/><line x1=\"900\" y1=\"159\" x2=\"894\" y2=\"169\"/><line x1=\"900\" y1=\"159\" x2=\"906\" y2=\"169\"/></g>\n<text x=\"900\" y=\"191\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">MSB (entspricht MSB a…</text>\n<line x1=\"628\" y1=\"160\" x2=\"878\" y2=\"160\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"152\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"176\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">17113</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"227\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"247\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"177\" x2=\"530\" y2=\"227\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"227\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"247\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"243\" x2=\"230\" y2=\"243\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"235\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"291\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"311\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">2. Bearbeitungsstand bei</text>\n<text x=\"530\" y=\"326\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Beendigung des Prozesses</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"260\" x2=\"530\" y2=\"291\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"297\" r=\"5\"/><line x1=\"900\" y1=\"302\" x2=\"900\" y2=\"314\"/><line x1=\"893\" y1=\"306\" x2=\"907\" y2=\"306\"/><line x1=\"900\" y1=\"314\" x2=\"894\" y2=\"324\"/><line x1=\"900\" y1=\"314\" x2=\"906\" y2=\"324\"/></g>\n<text x=\"900\" y=\"346\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">MSB (entspricht MSB a…</text>\n<line x1=\"878\" y1=\"315\" x2=\"628\" y2=\"315\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"307\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"331\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">19114</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"374\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"394\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z33</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"339\" x2=\"530\" y2=\"374\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-schreiben\" x=\"432\" y=\"438\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"458\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"407\" x2=\"530\" y2=\"438\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-schreiben\" x=\"34\" y=\"438\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"458\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten erstellen</text>\n<line x1=\"432\" y1=\"454\" x2=\"230\" y2=\"454\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"446\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"502\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"522\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">7. Bearbeitungsstand bei</text>\n<text x=\"530\" y=\"537\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Beendigung des Prozesses</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"471\" x2=\"530\" y2=\"502\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"508\" r=\"5\"/><line x1=\"900\" y1=\"513\" x2=\"900\" y2=\"525\"/><line x1=\"893\" y1=\"517\" x2=\"907\" y2=\"517\"/><line x1=\"900\" y1=\"525\" x2=\"894\" y2=\"535\"/><line x1=\"900\" y1=\"525\" x2=\"906\" y2=\"535\"/></g>\n<text x=\"900\" y=\"557\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">MSB (entspricht MSB a…</text>\n<line x1=\"878\" y1=\"526\" x2=\"628\" y2=\"526\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"518\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"542\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">19114</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"585\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"605\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z33</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"550\" x2=\"530\" y2=\"585\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-schreiben\" x=\"432\" y=\"649\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"669\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"618\" x2=\"530\" y2=\"649\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-schreiben\" x=\"34\" y=\"649\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"669\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten erstellen</text>\n<line x1=\"432\" y1=\"665\" x2=\"230\" y2=\"665\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"657\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n</svg>"} gesamt={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 974 672\" width=\"974\" height=\"672\" role=\"img\" aria-labelledby=\"sd-title\" class=\"maco-sequence\">\n<title id=\"sd-title\">Sequenzdiagramm: Reklamation vom LF aus Sicht LF</title>\n<defs><marker id=\"sd-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect x=\"16\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"121\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend (Kunde)</text>\n<line x1=\"121\" y1=\"64\" x2=\"121\" y2=\"660\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"260\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"365\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · LF</text>\n<line x1=\"365\" y1=\"64\" x2=\"365\" y2=\"660\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"504\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"609\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">MSB (entspricht MSB am Ob…</text>\n<line x1=\"609\" y1=\"64\" x2=\"609\" y2=\"660\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"748\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"853\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">MSB (entspricht MSB am Ob…</text>\n<line x1=\"853\" y1=\"64\" x2=\"853\" y2=\"660\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"121\" y1=\"90\" x2=\"365\" y2=\"90\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"81\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">2 Ereignisse, alternativ</text>\n<text x=\"243\" y=\"105\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Trigger-Event</text>\n<line x1=\"365\" y1=\"152\" x2=\"609\" y2=\"152\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"143\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">1. Reklamation Wert</text>\n<text x=\"487\" y=\"167\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 17113</text>\n<line x1=\"365\" y1=\"214\" x2=\"121\" y2=\"214\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"205\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"229\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"609\" y1=\"276\" x2=\"365\" y2=\"276\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"267\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">2. Bearbeitungsstand bei Beendigung des Prozesses</text>\n<text x=\"487\" y=\"291\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 19114 · E_0228</text>\n<text x=\"487\" y=\"304\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0228 — Reklamation prüfen</text>\n<line x1=\"365\" y1=\"338\" x2=\"121\" y2=\"338\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"329\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<text x=\"243\" y=\"353\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten erstellen</text>\n<line x1=\"609\" y1=\"400\" x2=\"853\" y2=\"400\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"731\" y=\"391\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">5. Reklamation Wert einer Messlokation</text>\n<text x=\"731\" y=\"415\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 17113</text>\n<line x1=\"853\" y1=\"462\" x2=\"609\" y2=\"462\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"731\" y=\"453\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">6. Bearbeitungsstand bei Beendigung des Prozesses</text>\n<text x=\"731\" y=\"477\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 19114 · E_0029</text>\n<text x=\"731\" y=\"490\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0029 — Deltazeitreihenübertrag prüfen</text>\n<line x1=\"609\" y1=\"524\" x2=\"365\" y2=\"524\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"515\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">7. Bearbeitungsstand bei Beendigung des Prozesses</text>\n<text x=\"487\" y=\"539\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 19114</text>\n<line x1=\"365\" y1=\"586\" x2=\"121\" y2=\"586\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"577\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<text x=\"243\" y=\"601\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten erstellen</text>\n</svg>"} titel="LF" />

<a id="abschnitt-schritte"></a>

## Prozessschritte

<Schritt nr="1" anker="schritt-1" richtung="ausgehend" kopf={{"links": {"label": "LF", "eigen": true}, "rechts": {"label": "MSB (entspricht MSB am Objekt Marktlokation)"}}}>

### Reklamation Wert

<Schrittskizze sicht={{"label": "LF"}} zeilen={[{"art": "ausloeser", "werte": ["START_REKLAMATION_VON_WERTEN", "START_REKLAMATION_WERTE"]}, {"art": "senden", "label": "MSB (entspricht MSB am Objekt Marktlokation)", "weg": "AS4", "nachrichten": [{"nr": "17113", "titel": "Reklamation von Werten"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [17113](/schnittstellen/202610/pruefi/ORDERS/PI_17113) — Reklamation von Werten · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="ausloeser">

**Prozessauslöser**
- [`START_REKLAMATION_VON_WERTEN`](/schnittstellen/202610/trigger/events/LF-START_REKLAMATION_VON_WERTEN) · [Im Playground ausprobieren](/api/202610/ausloeser-lf/start-reklamation-von-werten)
- [`START_REKLAMATION_WERTE`](/schnittstellen/202610/trigger/events/LF-START_REKLAMATION_WERTE) · [Im Playground ausprobieren](/api/202610/ausloeser-lf/start-reklamation-werte)

Das Backend stößt diesen Schritt mit einem dieser Ereignisse an.

</li>

<li data-teil="nachricht">

Nachricht an **MSB (entspricht MSB am Objekt Marktlokation)** · AS4

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202610/backend-schreiben-lf/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": false, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"ANFRAGE\": [\n      {\n        \"anfragekategorie\": \"REKLAMATION_VON_WERTEN\",\n        \"anfragetyp\": \"LASTGANGDATEN\",\n        \"boTyp\": \"ANFRAGE\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"AUFTRAG\": [\n      {\n        \"boTyp\": \"AUFTRAG\",\n        \"positionsdaten\": [\n          {\n            \"positionsnummer\": 1\n          }\n        ],\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"REKLAMATION\": [\n      {\n        \"boTyp\": \"REKLAMATION\",\n        \"lokationsId\": \"55123678945\",\n        \"lokationsTyp\": \"MALO\",\n        \"obiskennzahl\": \"1:1.1.9.0\",\n        \"reklamationsgrund\": \"WERTE_ZU_HOCH\",\n        \"versionStruktur\": \"1\",\n        \"zeitraumMesswertanfrage\": {\n          \"enddatum\": \"2026-08-11T22:00:00Z\",\n          \"startdatum\": \"2026-04-28T22:00:00Z\"\n        }\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"ansprechpartner\": {\n        \"boTyp\": \"ANSPRECHPARTNER\",\n        \"eMailAdresse\": \"marktpartner @stromnetz-hamburg.de\",\n        \"nachname\": \"Andre Laue\",\n        \"versionStruktur\": \"1\"\n      },\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"marktrolle\": \"LF\",\n      \"rollencodenummer\": \"9903111000003\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"angebotsreferenz\": \"12345\",\n    \"datenaustauschreferenz\": \"M0OYS007\",\n    \"dokumentennummer\": \"M0HC9M6V\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"marktrolle\": \"MSB\",\n      \"rollencodenummer\": \"9904629000006\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"nachrichtendatum\": \"2026-10-01T11:00:00Z\",\n    \"nachrichtenreferenznummer\": \"M104QEDN\",\n    \"pruefidentifikator\": \"17113\",\n    \"sparte\": \"STROM\"\n  },\n  \"zusatzdaten\": {}\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend fort, nachdem die Nachricht erstellt ist.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="2" anker="schritt-2" richtung="eingehend" kopf={{"links": {"label": "LF", "eigen": true}, "rechts": {"label": "MSB (entspricht MSB am Objekt Marktlokation)"}}}>

### Bearbeitungsstand bei Beendigung des Prozesses

<Schrittskizze sicht={{"label": "LF"}} zeilen={[{"art": "empfangen", "label": "MSB (entspricht MSB am Objekt Marktlokation)", "weg": "AS4", "nachrichten": [{"nr": "19114", "titel": "Ablehnung Reklamation"}]}, {"art": "aperak", "werte": ["Z33"]}, {"art": "erstellen"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [19114](/schnittstellen/202610/pruefi/ORDRSP/PI_19114) — Ablehnung Reklamation · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **MSB (entspricht MSB am Objekt Marktlokation)** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `19114` → [E_0228](/referenz/202610/ebd/E_0228) · Reklamation prüfen

</div>

</li>

<li data-teil="aperak">

**Aperak-Prüfungen**
- `19114` → `Z33` — Aperak Prüfung: Ist referenzierte Nachricht bekannt ?

</li>

<li data-teil="schnittstelle" data-art="schreiben">

**Schreibende Schnittstelle**
- Vorgang angelegt — [Prozessdaten erstellen](/api/202610/backend-schreiben-lf/createprocessdata#prozessdaten-erstellen) `POST /createProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/createProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": false, "defaultValue": "ERSTELLEN_PROZESSDATEN", "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"ANFRAGE\": [\n      {\n        \"anfragekategorie\": \"REKLAMATION_VON_WERTEN\",\n        \"anfragetyp\": \"ZAEHLERSTAENDE\",\n        \"boTyp\": \"ANFRAGE\",\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"ansprechpartner\": {\n        \"boTyp\": \"ANSPRECHPARTNER\",\n        \"nachname\": \"P GETTY\",\n        \"rufnummern\": [\n          {\n            \"nummerntyp\": \"RUF_DURCHWAHL\",\n            \"rufnummer\": \"+3222271020\"\n          }\n        ],\n        \"versionStruktur\": \"1\"\n      },\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"marktrolle\": \"MSB\",\n      \"rollencodenummer\": \"9910812000000\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"antwortstatus\": \"Z55\",\n    \"antwortstatusCodeliste\": \"S_0078\",\n    \"auftragsReferenz\": \"AFN9523\",\n    \"datenaustauschreferenz\": \"DADNDXKQFQOVJR\",\n    \"dokumentennummer\": \"DA732411191049589903323000007806667\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"marktrolle\": \"LF\",\n      \"rollencodenummer\": \"9979015000001\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"Z34\",\n    \"nachrichtendatum\": \"2026-10-01T11:00:00Z\",\n    \"nachrichtenreferenznummer\": \"DAQYOKMOVSHFGS\",\n    \"pruefidentifikator\": \"19114\",\n    \"sparte\": \"STROM\"\n  },\n  \"zusatzdaten\": {}\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Legt im Backend einen neuen Vorgang mit den Daten der eingegangenen Nachricht an.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="5" anker="schritt-5" richtung="fremd" kopf={{"links": {"label": "MSB (entspricht MSB am Objekt Marktlokation)", "eigen": false}, "rechts": {"label": "MSB (entspricht MSB am Objekt Messlokation)"}}}>

### Reklamation Wert einer Messlokation

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [17113](/schnittstellen/202610/pruefi/ORDERS/PI_17113) — Reklamation von Werten · AS4

</div>

</Schritt>

<Schritt nr="6" anker="schritt-6" richtung="fremd" kopf={{"links": {"label": "MSB (entspricht MSB am Objekt Messlokation)", "eigen": false}, "rechts": {"label": "MSB (entspricht MSB am Objekt Marktlokation)"}}}>

### Bearbeitungsstand bei Beendigung des Prozesses

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [19114](/schnittstellen/202610/pruefi/ORDRSP/PI_19114) — Ablehnung Reklamation · AS4

</div>

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `19114` → [E_0029](/referenz/202610/ebd/E_0029) · BIKO · Deltazeitreihenübertrag prüfen

</div>

</Schritt>

<Schritt nr="7" anker="schritt-7" richtung="eingehend" kopf={{"links": {"label": "LF", "eigen": true}, "rechts": {"label": "MSB (entspricht MSB am Objekt Marktlokation)"}}}>

### Bearbeitungsstand bei Beendigung des Prozesses

<Schrittskizze sicht={{"label": "LF"}} zeilen={[{"art": "empfangen", "label": "MSB (entspricht MSB am Objekt Marktlokation)", "weg": "AS4", "nachrichten": [{"nr": "19114", "titel": "Ablehnung Reklamation"}]}, {"art": "aperak", "werte": ["Z33"]}, {"art": "erstellen"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [19114](/schnittstellen/202610/pruefi/ORDRSP/PI_19114) — Ablehnung Reklamation · AS4

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
- `19114` → `Z33` — Aperak Prüfung: Ist referenzierte Nachricht bekannt ?

</li>

<li data-teil="schnittstelle" data-art="schreiben">

**Schreibende Schnittstelle**
- Vorgang angelegt — [Prozessdaten erstellen](/api/202610/backend-schreiben-lf/createprocessdata#prozessdaten-erstellen) `POST /createProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/createProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": false, "defaultValue": "ERSTELLEN_PROZESSDATEN", "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"ANFRAGE\": [\n      {\n        \"anfragekategorie\": \"REKLAMATION_VON_WERTEN\",\n        \"anfragetyp\": \"ZAEHLERSTAENDE\",\n        \"boTyp\": \"ANFRAGE\",\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"ansprechpartner\": {\n        \"boTyp\": \"ANSPRECHPARTNER\",\n        \"nachname\": \"P GETTY\",\n        \"rufnummern\": [\n          {\n            \"nummerntyp\": \"RUF_DURCHWAHL\",\n            \"rufnummer\": \"+3222271020\"\n          }\n        ],\n        \"versionStruktur\": \"1\"\n      },\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"marktrolle\": \"MSB\",\n      \"rollencodenummer\": \"9910812000000\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"antwortstatus\": \"Z55\",\n    \"antwortstatusCodeliste\": \"S_0078\",\n    \"auftragsReferenz\": \"AFN9523\",\n    \"datenaustauschreferenz\": \"DADNDXKQFQOVJR\",\n    \"dokumentennummer\": \"DA732411191049589903323000007806667\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"marktrolle\": \"LF\",\n      \"rollencodenummer\": \"9979015000001\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"Z34\",\n    \"nachrichtendatum\": \"2026-10-01T11:00:00Z\",\n    \"nachrichtenreferenznummer\": \"DAQYOKMOVSHFGS\",\n    \"pruefidentifikator\": \"19114\",\n    \"sparte\": \"STROM\"\n  },\n  \"zusatzdaten\": {}\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

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
| [E_0228](/referenz/202610/ebd/E_0228) | Reklamation prüfen |
| [E_0029](/referenz/202610/ebd/E_0029) | Deltazeitreihenübertrag prüfen |

</details>

<a id="abschnitt-informationen"></a>

## Prozess-Informationen

Wortlaut der Lesefassung, Steckbrief Kap. 2.7.1, S. 44–45.

<Stepper>
<ol>

<li data-blatt="vorbedingungen">

### Vorbedingungen

- Der MSB kennt die Messlokationen und Marktlokation
- Der MSB kennt die Berechnungsvorschriften zur Bildung der Werte der Marklokation.
- LF, NB, ÜNB bzw. MSB ist zur Reklamation von Werten berechtigt.

</li>

<li data-blatt="ergebnisse">

### Ergebnisse

Übermittlung der Werte an die Berechtigten.

</li>

<li data-blatt="anforderungen">

### Weitere Anforderungen

- Sofern der MSB der Marktlokation bei fehlenden Werten feststellt, dass diese Werte nur an einzelne Berechtigte nicht versendet wurden, müssen die Werte auch nur an diese Berechtigten übermittelt werden.
- Der GPKE Use-Case "Geschäftsdatenanfrage" (GPKE Teil 4) darf nicht für die Reklamation unplausibler oder fehlender Werte verwendet werden.
- Eine Reklamation fehlender Werte ist erst möglich, wenn die Frist der zu übermittelnden Werte aus der Tabelle 2.5.5 überschritten ist. Ausgenommen davon ist folgender Sachverhalt: Geht beim LF ein Lieferschein vom NB ein und hat der LF vom MSB der Marktlokation noch keine Energiemengen für den Lieferscheinzeitraum erhalten, ist unabhängig der Fristen der Tabelle 2.5.5 unverzüglich eine Reklamation zu fehlenden Werten vom LF an den MSB der Marktlokation durchzuführen.

</li>

<li data-blatt="anlass">

### Anlass

- Dem LF, NB, ÜNB oder MSB erscheint ein vorliegender Wert unplausibel oder
- dem LF, NB, ÜNB oder MSB liegen erforderliche Werte in der entsprechenden Qualität nicht fristgerecht vor oder
- dem LF liegen zur Prüfung des Lieferscheins keine Energiemengen für die betroffene Marktlokation vor.

</li>

<li data-blatt="erste-nachricht">

### Erste Nachricht

Der Beteiligte dieser Seite sendet selbst: „Reklamation Wert“ an **MSB (entspricht MSB am Objekt Marktlokation)** (Schritt 1).

</li>

<li data-blatt="ziel">

### Ziel

Der NB, LF oder ÜNB hat unplausible oder fehlende Werte beim MSB der Marktlokation reklamiert oder der MSB der Marktlokation hat unplausible oder fehlende Werte beim MSB der Messlokation reklamiert oder der MSB der Marktlokation bzw. der MSB der Messlokation hat erkannt, dass Werte durch ihn nicht versendet wurden oder durch ihn korrigiert werden müssen, ohne dass eine Reklamation einer anderen Marktrolle eingegangen ist.

</li>

</ol>
</Stepper>

<a id="abschnitt-sichten"></a>

## Andere Sichten des Prozesses

Derselbe Prozess, aus den Augen der anderen Beteiligten: dieselben Schritte, jeweils aus deren Sicht gelesen.

- [Sicht MSB-MALO](/prozessdoku/202610/MSB--MSB-MALO/WiM-Teil2-reklamation-vom-lf) — MSB am Objekt Marktlokation · Marktrolle MSB
- [Sicht MSB-MELO](/prozessdoku/202610/MSB--MSB-MELO/WiM-Teil2-reklamation-vom-lf) — MSB am Objekt Messlokation · Marktrolle MSB

<Hinweisbereich>

*Die Schritte sind die **möglichen** Nachrichten dieses Prozesses, keine Abfolge — die Quelle führt weder Bedingungen noch Alternativen. Das Kästchen am Schritt nennt links die eigene Sicht: **←** empfängt sie, **→** sendet sie. Zugeklappte Schritte laufen zwischen anderen Marktpartnern. Die Nummern sind die der Quelle; wo eine fehlt, fehlt sie dort.*

</Hinweisbereich>
