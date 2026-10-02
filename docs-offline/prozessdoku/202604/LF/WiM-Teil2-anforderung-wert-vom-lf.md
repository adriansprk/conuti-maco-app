# Anforderung Wert vom LF — Sicht LF

<Kopf rolle="LF" beteiligter="LF" festlegung="WiM" dokument="WiM Strom Teil 2" kapitel="2.6.4" sparte="Strom" schritte={5} suchtitel="Anforderung Wert vom LF — Sicht LF · WiM Strom Teil 2 · Formatversion 202604" abschnitte={[{"id": "abschnitt-ablauf", "label": "Prozessablauf"}, {"id": "abschnitt-schritte", "label": "Prozessschritte"}, {"id": "abschnitt-informationen", "label": "Prozess-Informationen"}, {"id": "abschnitt-sichten", "label": "Andere Sichten des Prozesses"}]} />

<Kurzfassung>

Der NB oder LF fordert über einen Bestellprozess Zwischenablesungswerte beim MSB der Marktlokation an, der zu dem Zeitraum, für den die Werte benötigt werden, der Marktlokation zugeordnet war. Der MSB der Marktlokation prüft die Anforderung und erfüllt diese oder lehnt diese ggf. ab. Der MSB der Marktlokation fordert über einen Bestellprozess Zwischenablesungswerte der Messlokation bei dem MSB der Messlokation an, der zu dem Zeitraum, für den die Werte benötigt werden, der Messlokation zugeordnet war. Der MSB der Messlokation prüft die Anforderung und erfüllt diese oder lehnt diese ggf. ab.

</Kurzfassung>

<a id="abschnitt-ablauf"></a>

## Prozessablauf aus Sicht des LF

<Systembild svg={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1004 747\" width=\"1004\" height=\"747\" role=\"img\" aria-labelledby=\"sb-title\" class=\"maco-systembild\">\n<title id=\"sb-title\">Systembild: Anforderung Wert vom LF aus Sicht LF</title>\n<defs><marker id=\"sb-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect class=\"sb-lane-kopf\" x=\"16\" y=\"12\" width=\"232\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend-System des Kunden</text>\n<rect class=\"sb-lane-kopf\" x=\"398\" y=\"12\" width=\"264\" height=\"46\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · LF</text>\n<rect class=\"sb-lane-kopf\" x=\"812\" y=\"12\" width=\"176\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"900\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Marktpartner</text>\n<line x1=\"323\" y1=\"58\" x2=\"323\" y2=\"735\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"737\" y1=\"58\" x2=\"737\" y2=\"735\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect class=\"sb-kasten sb-trigger\" x=\"432\" y=\"80\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessauslöser empfangen</text>\n<rect class=\"sb-kasten sb-backend sb-trigger\" x=\"34\" y=\"72\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"92\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">START_ANFORDERUNG_VON</text>\n<text x=\"132\" y=\"107\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">_WERTEN</text>\n<line x1=\"230\" y1=\"96\" x2=\"432\" y2=\"96\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"88\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"154\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"174\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">1. Anforderung Wert</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"113\" x2=\"530\" y2=\"154\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"152\" r=\"5\"/><line x1=\"900\" y1=\"157\" x2=\"900\" y2=\"169\"/><line x1=\"893\" y1=\"161\" x2=\"907\" y2=\"161\"/><line x1=\"900\" y1=\"169\" x2=\"894\" y2=\"179\"/><line x1=\"900\" y1=\"169\" x2=\"906\" y2=\"179\"/></g>\n<text x=\"900\" y=\"201\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">MSB (entspricht MSB a…</text>\n<line x1=\"628\" y1=\"170\" x2=\"878\" y2=\"170\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"162\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"186\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">17004</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"237\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"257\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"187\" x2=\"530\" y2=\"237\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"237\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"257\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"253\" x2=\"230\" y2=\"253\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"245\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"301\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"321\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">2. Bearbeitungsstand bei</text>\n<text x=\"530\" y=\"336\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Beendigung des Prozesses</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"270\" x2=\"530\" y2=\"301\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"307\" r=\"5\"/><line x1=\"900\" y1=\"312\" x2=\"900\" y2=\"324\"/><line x1=\"893\" y1=\"316\" x2=\"907\" y2=\"316\"/><line x1=\"900\" y1=\"324\" x2=\"894\" y2=\"334\"/><line x1=\"900\" y1=\"324\" x2=\"906\" y2=\"334\"/></g>\n<text x=\"900\" y=\"356\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">MSB (entspricht MSB a…</text>\n<line x1=\"878\" y1=\"325\" x2=\"628\" y2=\"325\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"317\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"341\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">19007</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"384\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"404\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z33</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"349\" x2=\"530\" y2=\"384\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"448\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"468\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"417\" x2=\"530\" y2=\"448\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben sb-abgeleitet\" x=\"34\" y=\"448\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"468\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"464\" x2=\"230\" y2=\"464\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"456\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"512\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"532\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">6. Bearbeitungsstand bei</text>\n<text x=\"530\" y=\"547\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Beendigung des Prozesses</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"481\" x2=\"530\" y2=\"512\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"518\" r=\"5\"/><line x1=\"900\" y1=\"523\" x2=\"900\" y2=\"535\"/><line x1=\"893\" y1=\"527\" x2=\"907\" y2=\"527\"/><line x1=\"900\" y1=\"535\" x2=\"894\" y2=\"545\"/><line x1=\"900\" y1=\"535\" x2=\"906\" y2=\"545\"/></g>\n<text x=\"900\" y=\"567\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">MSB (entspricht MSB a…</text>\n<line x1=\"878\" y1=\"536\" x2=\"628\" y2=\"536\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"528\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"552\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">19007</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"595\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"615\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z33</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"560\" x2=\"530\" y2=\"595\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"659\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"679\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"628\" x2=\"530\" y2=\"659\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben sb-abgeleitet\" x=\"34\" y=\"659\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"679\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"675\" x2=\"230\" y2=\"675\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"667\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n</svg>"} gesamt={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 974 672\" width=\"974\" height=\"672\" role=\"img\" aria-labelledby=\"sd-title\" class=\"maco-sequence\">\n<title id=\"sd-title\">Sequenzdiagramm: Anforderung Wert vom LF aus Sicht LF</title>\n<defs><marker id=\"sd-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect x=\"16\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"121\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend (Kunde)</text>\n<line x1=\"121\" y1=\"64\" x2=\"121\" y2=\"660\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"260\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"365\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · LF</text>\n<line x1=\"365\" y1=\"64\" x2=\"365\" y2=\"660\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"504\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"609\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">MSB (entspricht MSB am Ob…</text>\n<line x1=\"609\" y1=\"64\" x2=\"609\" y2=\"660\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"748\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"853\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">MSB (entspricht MSB am Ob…</text>\n<line x1=\"853\" y1=\"64\" x2=\"853\" y2=\"660\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"121\" y1=\"90\" x2=\"365\" y2=\"90\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"81\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">START_ANFORDERUNG_VON_WERTEN</text>\n<text x=\"243\" y=\"105\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Trigger-Event</text>\n<line x1=\"365\" y1=\"152\" x2=\"609\" y2=\"152\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"143\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">1. Anforderung Wert</text>\n<text x=\"487\" y=\"167\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 17004</text>\n<line x1=\"365\" y1=\"214\" x2=\"121\" y2=\"214\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"205\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"229\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"609\" y1=\"276\" x2=\"365\" y2=\"276\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"267\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">2. Bearbeitungsstand bei Beendigung des Prozesses</text>\n<text x=\"487\" y=\"291\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 19007 · E_0221</text>\n<text x=\"487\" y=\"304\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0221 — Anforderung Wert prüfen</text>\n<line x1=\"365\" y1=\"338\" x2=\"121\" y2=\"338\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"329\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"353\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"609\" y1=\"400\" x2=\"853\" y2=\"400\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"731\" y=\"391\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">4. Anforderung Wert einer Messlokation</text>\n<text x=\"731\" y=\"415\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 17004</text>\n<line x1=\"853\" y1=\"462\" x2=\"609\" y2=\"462\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"731\" y=\"453\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">5. Bearbeitungsstand bei Beendigung des Prozesses</text>\n<text x=\"731\" y=\"477\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 19007 · E_0222</text>\n<text x=\"731\" y=\"490\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0222 — Anforderung Wert prüfen</text>\n<line x1=\"609\" y1=\"524\" x2=\"365\" y2=\"524\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"515\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">6. Bearbeitungsstand bei Beendigung des Prozesses</text>\n<text x=\"487\" y=\"539\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 19007</text>\n<line x1=\"365\" y1=\"586\" x2=\"121\" y2=\"586\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"577\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"601\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n</svg>"} titel="LF" />

<a id="abschnitt-schritte"></a>

## Prozessschritte

<Schritt nr="1" anker="schritt-1" richtung="ausgehend" kopf={{"links": {"label": "LF", "eigen": true}, "rechts": {"label": "MSB (entspricht MSB am Objekt Marktlokation)"}}}>

### Anforderung Wert

<Schrittskizze sicht={{"label": "LF"}} zeilen={[{"art": "ausloeser", "werte": ["START_ANFORDERUNG_VON_WERTEN"]}, {"art": "senden", "label": "MSB (entspricht MSB am Objekt Marktlokation)", "weg": "AS4", "nachrichten": [{"nr": "17004", "titel": "Anforderung von Werten"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [17004](/schnittstellen/202604/pruefi/ORDERS/PI_17004) — Anforderung von Werten · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="ausloeser">

**Prozessauslöser** [`START_ANFORDERUNG_VON_WERTEN`](/schnittstellen/202604/trigger/events/LF-START_ANFORDERUNG_VON_WERTEN) · [Im Playground ausprobieren](/api/202604/ausloeser-lf/start-anforderung-von-werten)

Das Backend stößt diesen Schritt mit diesem Ereignis an.

</li>

<li data-teil="nachricht">

Nachricht an **MSB (entspricht MSB am Objekt Marktlokation)** · AS4

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202604/backend-schreiben-lf/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": false, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"ANFRAGE\": [\n      {\n        \"anfragekategorie\": \"PROZESSDATENBERICHT\",\n        \"anfragetyp\": \"WERTEERMITTLUNG\",\n        \"boTyp\": \"ANFRAGE\",\n        \"gueltigAb\": \"2024-07-31T22:00:00Z\",\n        \"lokationsId\": \"DE00014545768S0000000000000003054\",\n        \"lokationsTyp\": \"MELO\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"AUFTRAG\": [\n      {\n        \"boTyp\": \"AUFTRAG\",\n        \"positionsdaten\": [\n          {\n            \"anfragegrund\": \"ZWISCHENABLESUNG\",\n            \"positionsnummer\": 1\n          }\n        ],\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"ansprechpartner\": {\n        \"boTyp\": \"ANSPRECHPARTNER\",\n        \"eMailAdresse\": \"marktpartner@stromnetz-hamburg.de\",\n        \"nachname\": \"Laue\",\n        \"versionStruktur\": \"1\"\n      },\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9900259000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"datenaustauschreferenz\": \"M03UH94L\",\n    \"dokumentennummer\": \"LZWOTR6A\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9904629000006\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"nachrichtendatum\": \"2024-08-14T06:01:00Z\",\n    \"nachrichtenreferenznummer\": \"M01QMYIF\",\n    \"pruefidentifikator\": \"17004\",\n    \"sparte\": \"STROM\"\n  },\n  \"zusatzdaten\": {}\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend fort, nachdem die Nachricht erstellt ist.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="2" anker="schritt-2" richtung="eingehend" kopf={{"links": {"label": "LF", "eigen": true}, "rechts": {"label": "MSB (entspricht MSB am Objekt Marktlokation)"}}}>

### Bearbeitungsstand bei Beendigung des Prozesses

<Schrittskizze sicht={{"label": "LF"}} zeilen={[{"art": "empfangen", "label": "MSB (entspricht MSB am Objekt Marktlokation)", "weg": "AS4", "nachrichten": [{"nr": "19007", "titel": "Ablehnung Anforderung Werte"}]}, {"art": "aperak", "werte": ["Z33"]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [19007](/schnittstellen/202604/pruefi/ORDRSP/PI_19007) — Ablehnung Anforderung Werte · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **MSB (entspricht MSB am Objekt Marktlokation)** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `19007` → [E_0221](/referenz/202604/ebd/E_0221) · Anforderung Wert prüfen

</div>

</li>

<li data-teil="aperak">

**Aperak-Prüfungen**
- `19007` → `Z33` — Aperak Prüfung: Ist referenzierte Nachricht bekannt ?

</li>

<li data-teil="schnittstelle" data-art="fortschreiben" data-abgeleitet="ja">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202604/backend-schreiben-lf/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": false, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"ANFRAGE\": [\n      {\n        \"anfragekategorie\": \"PROZESSDATENBERICHT\",\n        \"anfragetyp\": \"WERTEERMITTLUNG\",\n        \"boTyp\": \"ANFRAGE\",\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"ansprechpartner\": {\n        \"boTyp\": \"ANSPRECHPARTNER\",\n        \"nachname\": \"P GETTY\",\n        \"rufnummern\": [\n          {\n            \"nummerntyp\": \"RUF_DURCHWAHL\",\n            \"rufnummer\": \"+3222271020\"\n          }\n        ],\n        \"versionStruktur\": \"1\"\n      },\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9904990000008\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"antwortstatus\": \"Z19\",\n    \"antwortstatusCodeliste\": \"S_0075\",\n    \"auftragsReferenz\": \"AFN9523\",\n    \"datenaustauschreferenz\": \"DAWGHBTXASFTUF\",\n    \"dokumentennummer\": \"DA482411190816469903323000007540816\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9903729000007\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"7\",\n    \"nachrichtendatum\": \"2025-06-24T12:31:00Z\",\n    \"nachrichtenreferenznummer\": \"DADAGQTLWLKLYJ\",\n    \"pruefidentifikator\": \"19007\",\n    \"sparte\": \"STROM\"\n  },\n  \"zusatzdaten\": {}\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend mit den Daten der eingegangenen Nachricht fort.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="4" anker="schritt-4" richtung="fremd" kopf={{"links": {"label": "MSB (entspricht MSB am Objekt Marktlokation)", "eigen": false}, "rechts": {"label": "MSB (entspricht MSB am Objekt Messlokation)"}}}>

### Anforderung Wert einer Messlokation

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [17004](/schnittstellen/202604/pruefi/ORDERS/PI_17004) — Anforderung von Werten · AS4

</div>

</Schritt>

<Schritt nr="5" anker="schritt-5" richtung="fremd" kopf={{"links": {"label": "MSB (entspricht MSB am Objekt Messlokation)", "eigen": false}, "rechts": {"label": "MSB (entspricht MSB am Objekt Marktlokation)"}}}>

### Bearbeitungsstand bei Beendigung des Prozesses

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [19007](/schnittstellen/202604/pruefi/ORDRSP/PI_19007) — Ablehnung Anforderung Werte · AS4

</div>

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `19007` → [E_0222](/referenz/202604/ebd/E_0222) · Anforderung Wert prüfen

</div>

</Schritt>

<Schritt nr="6" anker="schritt-6" richtung="eingehend" kopf={{"links": {"label": "LF", "eigen": true}, "rechts": {"label": "MSB (entspricht MSB am Objekt Marktlokation)"}}}>

### Bearbeitungsstand bei Beendigung des Prozesses

<Schrittskizze sicht={{"label": "LF"}} zeilen={[{"art": "empfangen", "label": "MSB (entspricht MSB am Objekt Marktlokation)", "weg": "AS4", "nachrichten": [{"nr": "19007", "titel": "Ablehnung Anforderung Werte"}]}, {"art": "aperak", "werte": ["Z33"]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [19007](/schnittstellen/202604/pruefi/ORDRSP/PI_19007) — Ablehnung Anforderung Werte · AS4

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
- `19007` → `Z33` — Aperak Prüfung: Ist referenzierte Nachricht bekannt ?

</li>

<li data-teil="schnittstelle" data-art="fortschreiben" data-abgeleitet="ja">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202604/backend-schreiben-lf/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": false, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"ANFRAGE\": [\n      {\n        \"anfragekategorie\": \"PROZESSDATENBERICHT\",\n        \"anfragetyp\": \"WERTEERMITTLUNG\",\n        \"boTyp\": \"ANFRAGE\",\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"ansprechpartner\": {\n        \"boTyp\": \"ANSPRECHPARTNER\",\n        \"nachname\": \"P GETTY\",\n        \"rufnummern\": [\n          {\n            \"nummerntyp\": \"RUF_DURCHWAHL\",\n            \"rufnummer\": \"+3222271020\"\n          }\n        ],\n        \"versionStruktur\": \"1\"\n      },\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9904990000008\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"antwortstatus\": \"Z19\",\n    \"antwortstatusCodeliste\": \"S_0075\",\n    \"auftragsReferenz\": \"AFN9523\",\n    \"datenaustauschreferenz\": \"DAWGHBTXASFTUF\",\n    \"dokumentennummer\": \"DA482411190816469903323000007540816\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9903729000007\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"7\",\n    \"nachrichtendatum\": \"2025-06-24T12:31:00Z\",\n    \"nachrichtenreferenznummer\": \"DADAGQTLWLKLYJ\",\n    \"pruefidentifikator\": \"19007\",\n    \"sparte\": \"STROM\"\n  },\n  \"zusatzdaten\": {}\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

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
| [E_0221](/referenz/202604/ebd/E_0221) | Anforderung Wert prüfen |
| [E_0222](/referenz/202604/ebd/E_0222) | Anforderung Wert prüfen |

</details>

<a id="abschnitt-informationen"></a>

## Prozess-Informationen

Wortlaut der Lesefassung, Steckbrief Kap. 2.6.1, S. 38.

<Stepper>
<ol>

<li data-blatt="vorbedingungen">

### Vorbedingungen

- Der MSB kennt die Messlokationen und Marktlokation.
- Der Anfragende ist berechtigt, zur Anfrage und zum Erhalt von Zwischenablesungswerten.

</li>

<li data-blatt="ergebnisse">

### Ergebnisse

Übermittlung der Zwischenablesungswerte an die Berechtigten.

</li>

<li data-blatt="anforderungen">

### Weitere Anforderungen

Findet bei einer in die Zukunft gerichteten Bestellung bis zum Bestelldatum ein Wechsel des MSB statt, ist die versendete Bestellung obsolet. Die Bestellung muss erneut an den dann zuständigen MSB versendet werden.

</li>

<li data-blatt="anlass">

### Anlass

Auslöser einer Bestellung vom NB oder LF an den MSB der Marktlokation kann für Marktlokationen, deren Messlokationen mit kME mit Wirkarbeitsmessung, mME oder iMS ausgestattet sind, eine Zwischenablesung (s. dazu unter Nr. 4 in der Tabelle „Darstellung der zu übermittelnden Werte“) sein. Auslöser einer Bestellung vom NB an den MSB der Marktlokation kann für gemessene Marktlokationen, deren Messlokationen mit kME mit Wirkarbeitsmessung oder mME ausgestattet sind, ein Abgrenzungsverfahren sein (s. dazu die Vorgaben des Kapitels 2.2.2. „Aufbereitung und Übermittlung von Werten“ zum Thema Abgrenzung).

</li>

<li data-blatt="erste-nachricht">

### Erste Nachricht

Der Beteiligte dieser Seite sendet selbst: „Anforderung Wert“ an **MSB (entspricht MSB am Objekt Marktlokation)** (Schritt 1).

</li>

<li data-blatt="ziel">

### Ziel

Der NB oder LF hat Zwischenablesungswerte beim MSB der Marktlokation angefordert oder der MSB der Marktlokation hat Zwischenablesungswerte beim MSB der Messlokation angefordert.

</li>

</ol>
</Stepper>

<a id="abschnitt-sichten"></a>

## Andere Sichten des Prozesses

Derselbe Prozess, aus den Augen der anderen Beteiligten: dieselben Schritte, jeweils aus deren Sicht gelesen.

- [Sicht MSB-MALO](/prozessdoku/202604/MSB--MSB-MALO/WiM-Teil2-anforderung-wert-vom-lf) — MSB am Objekt Marktlokation · Marktrolle MSB
- [Sicht MSB-MELO](/prozessdoku/202604/MSB--MSB-MELO/WiM-Teil2-anforderung-wert-vom-lf) — MSB am Objekt Messlokation · Marktrolle MSB

<Hinweisbereich>

*Die Schritte sind die **möglichen** Nachrichten dieses Prozesses, keine Abfolge — die Quelle führt weder Bedingungen noch Alternativen. Das Kästchen am Schritt nennt links die eigene Sicht: **←** empfängt sie, **→** sendet sie. Zugeklappte Schritte laufen zwischen anderen Marktpartnern. Die Nummern sind die der Quelle; wo eine fehlt, fehlt sie dort.*

Die Konnektortabelle führt für diese Schritte keinen Schreibaufruf. Abgeleitet aus dem Prozessverlauf: Die eigene Rolle war an diesem Prozess schon beteiligt, der Vorgang besteht also.

Betrifft: [2](#schritt-2), [6](#schritt-6)

</Hinweisbereich>
