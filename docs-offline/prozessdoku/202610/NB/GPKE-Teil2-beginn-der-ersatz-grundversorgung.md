# Beginn der Ersatz-/Grundversorgung — Sicht NB

<Kopf rolle="NB" beteiligter="NB" festlegung="GPKE" dokument="GPKE Teil 2" kapitel="2.3.2.2" sparte="Strom" schritte={3} suchtitel="Beginn der Ersatz-/Grundversorgung — Sicht NB · GPKE Teil 2 · Formatversion 202610" abschnitte={[{"id": "abschnitt-ablauf", "label": "Prozessablauf"}, {"id": "abschnitt-schritte", "label": "Prozessschritte"}, {"id": "abschnitt-informationen", "label": "Prozess-Informationen"}, {"id": "abschnitt-sichten", "label": "Andere Sichten des Prozesses"}]} />

<Kurzfassung>

Der NB kündigt dem E/G die Zuordnung des E/G zur Marktlokation an.

</Kurzfassung>

<a id="abschnitt-ablauf"></a>

## Prozessablauf aus Sicht des NB

<Systembild svg={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1004 755\" width=\"1004\" height=\"755\" role=\"img\" aria-labelledby=\"sb-title\" class=\"maco-systembild\">\n<title id=\"sb-title\">Systembild: Beginn der Ersatz-/Grundversorgung aus Sicht NB</title>\n<defs><marker id=\"sb-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect class=\"sb-lane-kopf\" x=\"16\" y=\"12\" width=\"232\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend-System des Kunden</text>\n<rect class=\"sb-lane-kopf\" x=\"398\" y=\"12\" width=\"264\" height=\"46\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · NB</text>\n<rect class=\"sb-lane-kopf\" x=\"812\" y=\"12\" width=\"176\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"900\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Marktpartner</text>\n<line x1=\"323\" y1=\"58\" x2=\"323\" y2=\"743\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"737\" y1=\"58\" x2=\"737\" y2=\"743\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect class=\"sb-kasten sb-trigger\" x=\"432\" y=\"80\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessauslöser empfangen</text>\n<rect class=\"sb-kasten sb-backend sb-trigger\" x=\"34\" y=\"80\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">START_EOG</text>\n<line x1=\"230\" y1=\"96\" x2=\"432\" y2=\"96\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"88\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"144\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"164\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">1. Ankündigung der</text>\n<text x=\"530\" y=\"179\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Zuordnung des E/G zur</text>\n<text x=\"530\" y=\"194\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Marktlokation</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"113\" x2=\"530\" y2=\"144\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"157\" r=\"5\"/><line x1=\"900\" y1=\"162\" x2=\"900\" y2=\"174\"/><line x1=\"893\" y1=\"166\" x2=\"907\" y2=\"166\"/><line x1=\"900\" y1=\"174\" x2=\"894\" y2=\"184\"/><line x1=\"900\" y1=\"174\" x2=\"906\" y2=\"184\"/></g>\n<text x=\"900\" y=\"206\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">LF (Notiz \"entspricht…</text>\n<line x1=\"628\" y1=\"175\" x2=\"878\" y2=\"175\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"167\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"191\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">55013</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"233\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"253\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"207\" x2=\"530\" y2=\"233\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"233\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"253\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"249\" x2=\"230\" y2=\"249\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"241\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"297\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"317\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">2. Antwort auf Ankündigung</text>\n<text x=\"530\" y=\"332\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">der Zuordnung des E/G zur</text>\n<text x=\"530\" y=\"347\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Marktloka…</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"266\" x2=\"530\" y2=\"297\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"310\" r=\"5\"/><line x1=\"900\" y1=\"315\" x2=\"900\" y2=\"327\"/><line x1=\"893\" y1=\"319\" x2=\"907\" y2=\"319\"/><line x1=\"900\" y1=\"327\" x2=\"894\" y2=\"337\"/><line x1=\"900\" y1=\"327\" x2=\"906\" y2=\"337\"/></g>\n<text x=\"900\" y=\"359\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">LF (Notiz \"entspricht…</text>\n<line x1=\"878\" y1=\"328\" x2=\"628\" y2=\"328\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"320\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"344\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">55014, 55015</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"386\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"406\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z33</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"360\" x2=\"530\" y2=\"386\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"450\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"470\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"419\" x2=\"530\" y2=\"450\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"450\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"470\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"466\" x2=\"230\" y2=\"466\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"458\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-trigger\" x=\"432\" y=\"514\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"534\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessauslöser empfangen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"483\" x2=\"530\" y2=\"514\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-trigger\" x=\"34\" y=\"514\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"534\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">START_EOG</text>\n<line x1=\"230\" y1=\"530\" x2=\"432\" y2=\"530\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"522\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"578\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"598\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">3. Zuordnung des E/G zur</text>\n<text x=\"530\" y=\"613\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Marktlokation aufgrund</text>\n<text x=\"530\" y=\"628\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">fehlender Antw…</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"547\" x2=\"530\" y2=\"578\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"591\" r=\"5\"/><line x1=\"900\" y1=\"596\" x2=\"900\" y2=\"608\"/><line x1=\"893\" y1=\"600\" x2=\"907\" y2=\"600\"/><line x1=\"900\" y1=\"608\" x2=\"894\" y2=\"618\"/><line x1=\"900\" y1=\"608\" x2=\"906\" y2=\"618\"/></g>\n<text x=\"900\" y=\"640\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">LF (Notiz \"entspricht…</text>\n<line x1=\"628\" y1=\"609\" x2=\"878\" y2=\"609\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"601\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"625\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">55013</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"667\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"687\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"641\" x2=\"530\" y2=\"667\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"667\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"687\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"683\" x2=\"230\" y2=\"683\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"675\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n</svg>"} gesamt={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 730 610\" width=\"730\" height=\"610\" role=\"img\" aria-labelledby=\"sd-title\" class=\"maco-sequence\">\n<title id=\"sd-title\">Sequenzdiagramm: Beginn der Ersatz-/Grundversorgung aus Sicht NB</title>\n<defs><marker id=\"sd-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect x=\"16\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"121\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend (Kunde)</text>\n<line x1=\"121\" y1=\"64\" x2=\"121\" y2=\"598\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"260\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"365\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · NB</text>\n<line x1=\"365\" y1=\"64\" x2=\"365\" y2=\"598\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"504\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"609\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">LF (Notiz \"entspricht E/G…</text>\n<line x1=\"609\" y1=\"64\" x2=\"609\" y2=\"598\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"121\" y1=\"90\" x2=\"365\" y2=\"90\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"81\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">START_EOG</text>\n<text x=\"243\" y=\"105\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Trigger-Event</text>\n<line x1=\"365\" y1=\"152\" x2=\"609\" y2=\"152\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"143\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">1. Ankündigung der Zuordnung des E/G zur Marktlo…</text>\n<text x=\"487\" y=\"167\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55013</text>\n<line x1=\"365\" y1=\"214\" x2=\"121\" y2=\"214\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"205\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"229\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"609\" y1=\"276\" x2=\"365\" y2=\"276\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"267\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">2. Antwort auf Ankündigung der Zuordnung des E/G…</text>\n<text x=\"487\" y=\"291\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55014, 55015 · E_0615</text>\n<text x=\"487\" y=\"304\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0615 — Anmeldung E/G prüfen</text>\n<line x1=\"365\" y1=\"338\" x2=\"121\" y2=\"338\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"329\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"353\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"121\" y1=\"400\" x2=\"365\" y2=\"400\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"391\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">START_EOG</text>\n<text x=\"243\" y=\"415\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Trigger-Event</text>\n<line x1=\"365\" y1=\"462\" x2=\"609\" y2=\"462\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"453\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">3. Zuordnung des E/G zur Marktlokation aufgrund…</text>\n<text x=\"487\" y=\"477\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55013</text>\n<line x1=\"365\" y1=\"524\" x2=\"121\" y2=\"524\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"515\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"539\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n</svg>"} titel="NB" />

<a id="abschnitt-schritte"></a>

## Prozessschritte

<Schritt nr="1" anker="schritt-1" richtung="ausgehend" kopf={{"links": {"label": "NB", "eigen": true}, "rechts": {"label": "LF (Notiz „entspricht E/G“)"}}}>

### Ankündigung der Zuordnung des E/G zur Marktlokation

<Schrittskizze sicht={{"label": "NB"}} zeilen={[{"art": "ausloeser", "werte": ["START_EOG"]}, {"art": "senden", "label": "LF (Notiz „entspricht E/G“)", "weg": "AS4", "nachrichten": [{"nr": "55013", "titel": "Anmeldung / Zuordnung EOG"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55013](/schnittstellen/202610/pruefi/UTILMD/PI_55013) — Anmeldung / Zuordnung EOG · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="ausloeser">

**Prozessauslöser** [`START_EOG`](/schnittstellen/202610/trigger/events/NB-START_EOG) · [Im Playground ausprobieren](/api/202610/ausloeser-nb/start-eog)

Das Backend stößt diesen Schritt mit diesem Ereignis an.

</li>

<li data-teil="nachricht">

Nachricht an **LF (Notiz "entspricht E/G")** · AS4

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202610/backend-schreiben-nb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"BILANZIERUNG\": [\n      {\n        \"boTyp\": \"BILANZIERUNG\",\n        \"datenqualitaet\": \"INFORMATIVE_DATEN\",\n        \"detailsPrognosegrundlage\": [\n          \"TLP_TEP\"\n        ],\n        \"jahresverbrauchsprognose\": {\n          \"einheit\": \"KWH\",\n          \"wert\": 4100\n        },\n        \"prognosegrundlage\": \"PROFILE\",\n        \"temperaturarbeit\": {\n          \"einheit\": \"KWHK\",\n          \"wert\": 3\n        },\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"ENERGIELIEFERVERTRAG\": [\n      {\n        \"boTyp\": \"VERTRAG\",\n        \"datenqualitaet\": \"INFORMATIVE_DATEN\",\n        \"korrespondenzpartner\": {\n          \"ansprechpartner\": {\n            \"boTyp\": \"ANSPRECHPARTNER\",\n            \"eMailAdresse\": \"max@mustermann.de\",\n            \"versionStruktur\": \"1\"\n          },\n          \"boTyp\": \"GESCHAEFTSPARTNER\",\n          \"gewerbekennzeichnung\": false,\n          \"name1\": \"Fank Müller\",\n          \"partneradresse\": {\n            \"hausnummer\": \"25\",\n            \"landescode\": \"DE\",\n            \"ort\": \"Musterstadt\",\n            \"ortsteil\": \"Musterortsteil\",\n            \"postleitzahl\": \"55555\",\n            \"strasse\": \"Wohnstrasse\"\n          },\n          \"versionStruktur\": \"1\"\n        },\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\",\n        \"vertragsart\": \"ENERGIELIEFERVERTRAG\",\n        \"vertragspartner2\": [\n          {\n            \"boTyp\": \"GESCHAEFTSPARTNER\",\n            \"geschaeftspartnerrolle\": [\n              \"KUNDE\"\n            ],\n            \"gewerbekennzeichnung\": true,\n            \"name1\": \"Firma AG\",\n            \"name2\": \"Musterfirma\",\n            \"versionStruktur\": \"1\"\n          }\n        ]\n      }\n    ],\n    \"MARKTLOKATION\": [\n      {\n        \"boTyp\": \"MARKTLOKATION\",\n        \"datenqualitaet\": \"INFORMATIVE_DATEN\",\n        \"eigentuemer\": {\n          \"anrede\": \"Dr.\",\n          \"boTyp\": \"GESCHAEFTSPARTNER\",\n          \"geschaeftspartnerrolle\": [\n            \"EIGENTUEMER\"\n          ],\n          \"gewerbekennzeichnung\": false,\n          \"name1\": \"Huber\",\n          \"name2\": \"Karlheinz\",\n          \"partneradresse\": {\n            \"hausnummer\": \"815b\",\n            \"landescode\": \"DE\",\n            \"ort\": \"Entenhausen\",\n            \"ortsteil\": \"X\",\n            \"postleitzahl\": \"10010\",\n            \"strasse\": \"Teststraße\"\n          },\n          \"versionStruktur\": \"1\"\n        },\n        \"hausverwalter\": {\n          \"anrede\": \"Dr.\",\n          \"boTyp\": \"GESCHAEFTSPARTNER\",\n          \"geschaeftspartnerrolle\": [\n            \"HAUSVERWALTER\"\n          ],\n          \"gewerbekennzeichnung\": false,\n          \"name1\": \"Huber\",\n          \"name2\": \"Karlheinz\",\n          \"partneradresse\": {\n            \"hausnummer\": \"815b\",\n            \"landescode\": \"DE\",\n            \"ort\": \"Entenhausen\",\n            \"ortsteil\": \"X\",\n            \"postleitzahl\": \"10010\",\n            \"strasse\": \"Teststraße\"\n          },\n          \"versionStruktur\": \"1\"\n        },\n        \"lokationsadresse\": {\n          \"hausnummer\": \"36\",\n          \"landescode\": \"DE\",\n          \"ort\": \"Musterstadt\",\n          \"ortsteil\": \"Musterortsteil\",\n          \"postleitzahl\": \"55555\",\n          \"strasse\": \"Eichelbergstr.\",\n          \"zusatzInformation\": {\n            \"zusatz1\": \"Die Marktlokation befindet sich i\",\n            \"zusatz2\": \"m Hinterhaus im u\",\n            \"zusatz3\": \"nteren K\",\n            \"zusatz4\": \"eller recht\",\n            \"zusatz5\": \"s\"\n          }\n        },\n        \"marktlokationsId\": \"20072281644\",\n        \"marktlokationsTyp\": [\n          {\n            \"typ\": \"STANDARD_MARKTLOKATION\"\n          }\n        ],\n        \"marktrollen\": [\n          {\n            \"boTyp\": \"MARKTTEILNEHMER\",\n            \"gewerbekennzeichnung\": true,\n            \"marktrolle\": \"MSB\",\n            \"messstellenbetreiberEigenschaft\": \"GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER\",\n            \"rollencodenummer\": \"9910812000000\",\n            \"rollencodetyp\": \"BDEW\",\n            \"versionStruktur\": \"1\",\n            \"weiterverpflichtet\": false\n          }\n        ],\n        \"messtechnischeEinordnung\": \"KME_MME\",\n        \"netzebene\": \"NSP\",\n        \"sparte\": \"STROM\",\n        \"sperrstatus\": \"ENTSPERRT\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"MESSLOKATION\": [\n      {\n        \"boTyp\": \"MESSLOKATION\",\n        \"datenqualitaet\": \"INFORMATIVE_DATEN\",\n        \"marktrollen\": [\n          {\n            \"boTyp\": \"MARKTTEILNEHMER\",\n            \"gewerbekennzeichnung\": true,\n            \"marktrolle\": \"MSB\",\n            \"messstellenbetreiberEigenschaft\": \"GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER\",\n            \"rollencodenummer\": \"9910812000000\",\n            \"rollencodetyp\": \"BDEW\",\n            \"versionStruktur\": \"1\",\n            \"weiterverpflichtet\": false\n          },\n          {\n            \"boTyp\": \"MARKTTEILNEHMER\",\n            \"gewerbekennzeichnung\": true,\n            \"marktrolle\": \"GMSB\",\n            \"rollencodenummer\": \"9910812000000\",\n            \"rollencodetyp\": \"BDEW\",\n            \"versionStruktur\": \"1\"\n          }\n        ],\n        \"messlokationsId\": \"DE00713739359S0000000000001222221\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"NETZLOKATION\": [\n      {\n        \"boTyp\": \"NETZLOKATION\",\n        \"datenqualitaet\": \"INFORMATIVE_DATEN\",\n        \"marktrollen\": [\n          {\n            \"boTyp\": \"MARKTTEILNEHMER\",\n            \"gewerbekennzeichnung\": true,\n            \"marktrolle\": \"MSB\",\n            \"messstellenbetreiberEigenschaft\": \"GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER\",\n            \"rollencodenummer\": \"9910812000000\",\n            \"rollencodetyp\": \"BDEW\",\n            \"versionStruktur\": \"1\"\n          }\n        ],\n        \"netzlokationsId\": \"E1688117482\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"NETZNUTZUNGSVERTRAG\": [\n      {\n        \"boTyp\": \"VERTRAG\",\n        \"datenqualitaet\": \"INFORMATIVE_DATEN\",\n        \"korrespondenzpartner\": {\n          \"ansprechpartner\": {\n            \"boTyp\": \"ANSPRECHPARTNER\",\n            \"eMailAdresse\": \"max@mustermann.de\",\n            \"versionStruktur\": \"1\"\n          },\n          \"boTyp\": \"GESCHAEFTSPARTNER\",\n          \"gewerbekennzeichnung\": false,\n          \"name1\": \"Fank Müller\",\n          \"partneradresse\": {\n            \"hausnummer\": \"25\",\n            \"landescode\": \"DE\",\n            \"ort\": \"Musterstadt\",\n            \"ortsteil\": \"Musterortsteil\",\n            \"postleitzahl\": \"55555\",\n            \"strasse\": \"Wohnstrasse\"\n          },\n          \"versionStruktur\": \"1\"\n        },\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\",\n        \"vertragsart\": \"NETZNUTZUNGSVERTRAG\",\n        \"vertragsbeginn\": \"2025-11-01T23:00:00Z\",\n        \"vertragsende\": \"2025-11-30T23:00:00Z\",\n        \"vertragskonditionen\": {\n          \"haushaltskunde\": true\n        },\n        \"vertragspartner2\": [\n          {\n            \"boTyp\": \"GESCHAEFTSPARTNER\",\n            \"geschaeftspartnerrolle\": [\n              \"KUNDE\"\n            ],\n            \"gewerbekennzeichnung\": true,\n            \"name1\": \"Firma AG\",\n            \"name2\": \"Musterfirma\",\n            \"versionStruktur\": \"1\"\n          }\n        ]\n      }\n    ],\n    \"STEUERBARE_RESSOURCE\": [\n      {\n        \"boTyp\": \"STEUERBARE_RESSOURCE\",\n        \"datenqualitaet\": \"INFORMATIVE_DATEN\",\n        \"marktrollen\": [\n          {\n            \"boTyp\": \"MARKTTEILNEHMER\",\n            \"gewerbekennzeichnung\": true,\n            \"marktrolle\": \"MSB\",\n            \"messstellenbetreiberEigenschaft\": \"GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER\",\n            \"rollencodenummer\": \"9910812000000\",\n            \"rollencodetyp\": \"BDEW\",\n            \"versionStruktur\": \"1\"\n          }\n        ],\n        \"ressourcenId\": \"C816417ST77\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"TECHNISCHE_RESSOURCE\": [\n      {\n        \"boTyp\": \"TECHNISCHE_RESSOURCE\",\n        \"ressourcenId\": \"D417MLM8164\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9900327000009\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"datenaustauschreferenz\": \"DAICICNIOLJRFB\",\n    \"dokumentennummer\": \"DA942410151442459903323000007118027\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9903729000007\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"E01\",\n    \"nachrichtendatum\": \"2026-10-02T11:00:00Z\",\n    \"nachrichtenreferenznummer\": \"DACYYXETQZIAPR\",\n    \"pruefidentifikator\": \"55013\",\n    \"sparte\": \"STROM\",\n    \"transaktionsgrund\": \"Z36\",\n    \"transaktionsgrundergaenzung\": \"ZW7\",\n    \"transaktionsgrundergaenzungBefristeteAnmeldung\": \"E01\",\n    \"vertragsbeginn\": \"2025-11-01T23:00:00Z\",\n    \"vertragsende\": \"2025-11-30T23:00:00Z\",\n    \"vorgangsnummer\": \"24062416225400000000000102159662022\"\n  },\n  \"zusatzdaten\": {}\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend fort, nachdem die Nachricht erstellt ist.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="2" anker="schritt-2" richtung="eingehend" kopf={{"links": {"label": "NB", "eigen": true}, "rechts": {"label": "LF (Notiz „entspricht E/G“)"}}}>

### Antwort auf Ankündigung der Zuordnung des E/G zur Marktlokation

<Schrittskizze sicht={{"label": "NB"}} zeilen={[{"art": "empfangen", "label": "LF (Notiz „entspricht E/G“)", "weg": "AS4", "nachrichten": [{"nr": "55014", "titel": "Bestätigung EOG Anmeldung"}, {"nr": "55015", "titel": "Ablehung EOG Anmeldung"}]}, {"art": "aperak", "werte": ["Z33"]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55014](/schnittstellen/202610/pruefi/UTILMD/PI_55014) — Bestätigung EOG Anmeldung · AS4
- [55015](/schnittstellen/202610/pruefi/UTILMD/PI_55015) — Ablehung EOG Anmeldung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **LF (Notiz "entspricht E/G")** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `55014`, `55015` → [E_0615](/referenz/202610/ebd/E_0615) · LF · Anmeldung E/G prüfen

</div>

</li>

<li data-teil="aperak">

**Aperak-Prüfungen**
- `55014`, `55015` → `Z33`

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202610/backend-schreiben-nb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"ENERGIELIEFERVERTRAG\": [\n      {\n        \"boTyp\": \"VERTRAG\",\n        \"enFG\": [\n          {\n            \"grund\": [\n              \"ENFG_ELEKTRISCH_ANGETRIEBENE_WAERMEPUMPEN\"\n            ],\n            \"grundlageVerringerungUmlagen\": \"ERFUELLT_VORAUSSETZUNG_NACH_ENFG\"\n          }\n        ],\n        \"korrespondenzpartner\": {\n          \"ansprechpartner\": {\n            \"boTyp\": \"ANSPRECHPARTNER\",\n            \"eMailAdresse\": \"max@mustermann.de\",\n            \"versionStruktur\": \"1\"\n          },\n          \"boTyp\": \"GESCHAEFTSPARTNER\",\n          \"gewerbekennzeichnung\": false,\n          \"name1\": \"Fank Müller\",\n          \"partneradresse\": {\n            \"hausnummer\": \"25\",\n            \"landescode\": \"DE\",\n            \"ort\": \"Musterstadt\",\n            \"ortsteil\": \"Musterortsteil\",\n            \"postleitzahl\": \"55555\",\n            \"strasse\": \"Wohnstrasse\"\n          },\n          \"versionStruktur\": \"1\"\n        },\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\",\n        \"vertragsart\": \"ENERGIELIEFERVERTRAG\",\n        \"vertragspartner2\": [\n          {\n            \"boTyp\": \"GESCHAEFTSPARTNER\",\n            \"geschaeftspartnerrolle\": [\n              \"KUNDE\"\n            ],\n            \"gewerbekennzeichnung\": true,\n            \"name1\": \"Firma AG\",\n            \"name2\": \"Musterfirma\",\n            \"versionStruktur\": \"1\"\n          }\n        ]\n      }\n    ],\n    \"MARKTLOKATION\": [\n      {\n        \"boTyp\": \"MARKTLOKATION\",\n        \"erforderlichesProduktpaket\": [\n          {\n            \"priorisierung\": \"PRIORITAET1\",\n            \"produkt\": [\n              {\n                \"produktCode\": \"9991000002082\",\n                \"wertedetails\": \"11XBKA---------I\"\n              }\n            ],\n            \"produktpaketId\": 1,\n            \"umsetzungsgradvorgabe\": \"ZUORDNUNG_NUR_WENN_PRODUKTPAKET_UMSETZBAR\"\n          },\n          {\n            \"priorisierung\": \"PRIORITAET2\",\n            \"produkt\": [\n              {\n                \"produktCode\": \"9991000002082\",\n                \"wertedetails\": \"11XBKA--------II\"\n              }\n            ],\n            \"produktpaketId\": 2,\n            \"umsetzungsgradvorgabe\": \"ZUORDNUNG_NUR_WENN_PRODUKTPAKET_UMSETZBAR\"\n          }\n        ],\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\",\n        \"versorgungsart\": \"GRUNDVERSORGUNG\"\n      }\n    ],\n    \"NETZNUTZUNGSVERTRAG\": [\n      {\n        \"boTyp\": \"VERTRAG\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\",\n        \"vertragsart\": \"NETZNUTZUNGSVERTRAG\",\n        \"vertragsbeginn\": \"2025-11-01T23:00:00Z\",\n        \"vertragsende\": \"2025-12-01T23:00:00Z\",\n        \"vertragskonditionen\": {\n          \"haushaltskunde\": true\n        }\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9903729000007\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"anfragereferenznummer\": \"EOG123\",\n    \"antwortstatus\": \"A09\",\n    \"antwortstatusCodeliste\": \"E_0615\",\n    \"datenaustauschreferenz\": \"DAMRZIKWLWYZOU\",\n    \"dokumentennummer\": \"DA542411040919029903323000007222681\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9900327000009\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"E01\",\n    \"nachrichtendatum\": \"2026-10-02T11:00:00Z\",\n    \"nachrichtenreferenznummer\": \"DAPUNRHUZFPOHW\",\n    \"pruefidentifikator\": \"55014\",\n    \"sparte\": \"STROM\",\n    \"transaktionsgrund\": \"Z39\",\n    \"transaktionsgrundergaenzung\": \"ZW4\",\n    \"transaktionsgrundergaenzungBefristeteAnmeldung\": \"E01\",\n    \"vertragsbeginn\": \"2025-11-01T23:00:00Z\",\n    \"vertragsende\": \"2025-12-01T23:00:00Z\",\n    \"vorgangsnummer\": \"24062416225400000000000102159662022\"\n  },\n  \"zusatzdaten\": {}\n}"} examples={[{"mediaType": "application/json", "examples": [{"name": "55014", "summary": "55014 — Bestätigung EOG Anmeldung", "value": {"stammdaten": {"MARKTLOKATION": [{"boTyp": "MARKTLOKATION", "versionStruktur": "1", "sparte": "STROM", "versorgungsart": "GRUNDVERSORGUNG", "erforderlichesProduktpaket": [{"produktpaketId": 1, "produkt": [{"produktCode": "9991000002082", "wertedetails": "11XBKA---------I"}], "umsetzungsgradvorgabe": "ZUORDNUNG_NUR_WENN_PRODUKTPAKET_UMSETZBAR", "priorisierung": "PRIORITAET1"}, {"produktpaketId": 2, "produkt": [{"produktCode": "9991000002082", "wertedetails": "11XBKA--------II"}], "umsetzungsgradvorgabe": "ZUORDNUNG_NUR_WENN_PRODUKTPAKET_UMSETZBAR", "priorisierung": "PRIORITAET2"}]}], "NETZNUTZUNGSVERTRAG": [{"boTyp": "VERTRAG", "versionStruktur": "1", "vertragsart": "NETZNUTZUNGSVERTRAG", "sparte": "STROM", "vertragsbeginn": "2025-11-01T23:00:00Z", "vertragsende": "2025-12-01T23:00:00Z", "vertragskonditionen": {"haushaltskunde": true}}], "ENERGIELIEFERVERTRAG": [{"boTyp": "VERTRAG", "versionStruktur": "1", "vertragsart": "ENERGIELIEFERVERTRAG", "sparte": "STROM", "vertragspartner2": [{"boTyp": "GESCHAEFTSPARTNER", "versionStruktur": "1", "name1": "Firma AG", "name2": "Musterfirma", "gewerbekennzeichnung": true, "geschaeftspartnerrolle": ["KUNDE"]}], "korrespondenzpartner": {"boTyp": "GESCHAEFTSPARTNER", "versionStruktur": "1", "name1": "Fank Müller", "gewerbekennzeichnung": false, "partneradresse": {"postleitzahl": "55555", "ort": "Musterstadt", "strasse": "Wohnstrasse", "hausnummer": "25", "landescode": "DE", "ortsteil": "Musterortsteil"}, "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "eMailAdresse": "max@mustermann.de"}}, "enFG": [{"grundlageVerringerungUmlagen": "ERFUELLT_VORAUSSETZUNG_NACH_ENFG", "grund": ["ENFG_ELEKTRISCH_ANGETRIEBENE_WAERMEPUMPEN"]}]}]}, "transaktionsdaten": {"datenaustauschreferenz": "DAMRZIKWLWYZOU", "sparte": "STROM", "transaktionsgrund": "Z39", "transaktionsgrundergaenzung": "ZW4", "transaktionsgrundergaenzungBefristeteAnmeldung": "E01", "vorgangsnummer": "24062416225400000000000102159662022", "pruefidentifikator": "55014", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9903729000007", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900327000009", "rollencodetyp": "BDEW"}, "dokumentennummer": "DA542411040919029903323000007222681", "kategorie": "E01", "nachrichtendatum": "2026-10-02T11:00:00Z", "nachrichtenreferenznummer": "DAPUNRHUZFPOHW", "anfragereferenznummer": "EOG123", "antwortstatus": "A09", "antwortstatusCodeliste": "E_0615", "vertragsbeginn": "2025-11-01T23:00:00Z", "vertragsende": "2025-12-01T23:00:00Z"}, "zusatzdaten": {}}}, {"name": "55015", "summary": "55015 — Ablehung EOG Anmeldung", "value": {"stammdaten": [], "transaktionsdaten": {"datenaustauschreferenz": "LZ6VM2S4", "sparte": "STROM", "transaktionsgrund": "ZT6", "transaktionsgrundergaenzung": "ZW4", "vorgangsnummer": "12345", "pruefidentifikator": "55015", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9903790000002", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9900321000005", "rollencodetyp": "BDEW"}, "dokumentennummer": "BGMLZ16WKMS", "kategorie": "E01", "nachrichtendatum": "2026-10-02T11:00:00Z", "nachrichtenreferenznummer": "UNHLZWNRLJA", "anfragereferenznummer": "ABC123456", "antwortstatus": "A02", "antwortstatusCodeliste": "E_0615"}}}]}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend mit den Daten der eingegangenen Nachricht fort.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="3" anker="schritt-3" richtung="ausgehend" kopf={{"links": {"label": "NB", "eigen": true}, "rechts": {"label": "LF (Notiz „entspricht E/G“)"}}}>

### Zuordnung des E/G zur Marktlokation aufgrund fehlender Antwort

<Schrittskizze sicht={{"label": "NB"}} zeilen={[{"art": "ausloeser", "werte": ["START_EOG"]}, {"art": "senden", "label": "LF (Notiz „entspricht E/G“)", "weg": "AS4", "nachrichten": [{"nr": "55013", "titel": "Anmeldung / Zuordnung EOG"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55013](/schnittstellen/202610/pruefi/UTILMD/PI_55013) — Anmeldung / Zuordnung EOG · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="ausloeser">

**Prozessauslöser** [`START_EOG`](/schnittstellen/202610/trigger/events/NB-START_EOG) · [Im Playground ausprobieren](/api/202610/ausloeser-nb/start-eog)

Das Backend stößt diesen Schritt mit diesem Ereignis an.

</li>

<li data-teil="nachricht">

Nachricht an **LF (Notiz "entspricht E/G")** · AS4

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202610/backend-schreiben-nb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"BILANZIERUNG\": [\n      {\n        \"boTyp\": \"BILANZIERUNG\",\n        \"datenqualitaet\": \"INFORMATIVE_DATEN\",\n        \"detailsPrognosegrundlage\": [\n          \"TLP_TEP\"\n        ],\n        \"jahresverbrauchsprognose\": {\n          \"einheit\": \"KWH\",\n          \"wert\": 4100\n        },\n        \"prognosegrundlage\": \"PROFILE\",\n        \"temperaturarbeit\": {\n          \"einheit\": \"KWHK\",\n          \"wert\": 3\n        },\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"ENERGIELIEFERVERTRAG\": [\n      {\n        \"boTyp\": \"VERTRAG\",\n        \"datenqualitaet\": \"INFORMATIVE_DATEN\",\n        \"korrespondenzpartner\": {\n          \"ansprechpartner\": {\n            \"boTyp\": \"ANSPRECHPARTNER\",\n            \"eMailAdresse\": \"max@mustermann.de\",\n            \"versionStruktur\": \"1\"\n          },\n          \"boTyp\": \"GESCHAEFTSPARTNER\",\n          \"gewerbekennzeichnung\": false,\n          \"name1\": \"Fank Müller\",\n          \"partneradresse\": {\n            \"hausnummer\": \"25\",\n            \"landescode\": \"DE\",\n            \"ort\": \"Musterstadt\",\n            \"ortsteil\": \"Musterortsteil\",\n            \"postleitzahl\": \"55555\",\n            \"strasse\": \"Wohnstrasse\"\n          },\n          \"versionStruktur\": \"1\"\n        },\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\",\n        \"vertragsart\": \"ENERGIELIEFERVERTRAG\",\n        \"vertragspartner2\": [\n          {\n            \"boTyp\": \"GESCHAEFTSPARTNER\",\n            \"geschaeftspartnerrolle\": [\n              \"KUNDE\"\n            ],\n            \"gewerbekennzeichnung\": true,\n            \"name1\": \"Firma AG\",\n            \"name2\": \"Musterfirma\",\n            \"versionStruktur\": \"1\"\n          }\n        ]\n      }\n    ],\n    \"MARKTLOKATION\": [\n      {\n        \"boTyp\": \"MARKTLOKATION\",\n        \"datenqualitaet\": \"INFORMATIVE_DATEN\",\n        \"eigentuemer\": {\n          \"anrede\": \"Dr.\",\n          \"boTyp\": \"GESCHAEFTSPARTNER\",\n          \"geschaeftspartnerrolle\": [\n            \"EIGENTUEMER\"\n          ],\n          \"gewerbekennzeichnung\": false,\n          \"name1\": \"Huber\",\n          \"name2\": \"Karlheinz\",\n          \"partneradresse\": {\n            \"hausnummer\": \"815b\",\n            \"landescode\": \"DE\",\n            \"ort\": \"Entenhausen\",\n            \"ortsteil\": \"X\",\n            \"postleitzahl\": \"10010\",\n            \"strasse\": \"Teststraße\"\n          },\n          \"versionStruktur\": \"1\"\n        },\n        \"hausverwalter\": {\n          \"anrede\": \"Dr.\",\n          \"boTyp\": \"GESCHAEFTSPARTNER\",\n          \"geschaeftspartnerrolle\": [\n            \"HAUSVERWALTER\"\n          ],\n          \"gewerbekennzeichnung\": false,\n          \"name1\": \"Huber\",\n          \"name2\": \"Karlheinz\",\n          \"partneradresse\": {\n            \"hausnummer\": \"815b\",\n            \"landescode\": \"DE\",\n            \"ort\": \"Entenhausen\",\n            \"ortsteil\": \"X\",\n            \"postleitzahl\": \"10010\",\n            \"strasse\": \"Teststraße\"\n          },\n          \"versionStruktur\": \"1\"\n        },\n        \"lokationsadresse\": {\n          \"hausnummer\": \"36\",\n          \"landescode\": \"DE\",\n          \"ort\": \"Musterstadt\",\n          \"ortsteil\": \"Musterortsteil\",\n          \"postleitzahl\": \"55555\",\n          \"strasse\": \"Eichelbergstr.\",\n          \"zusatzInformation\": {\n            \"zusatz1\": \"Die Marktlokation befindet sich i\",\n            \"zusatz2\": \"m Hinterhaus im u\",\n            \"zusatz3\": \"nteren K\",\n            \"zusatz4\": \"eller recht\",\n            \"zusatz5\": \"s\"\n          }\n        },\n        \"marktlokationsId\": \"20072281644\",\n        \"marktlokationsTyp\": [\n          {\n            \"typ\": \"STANDARD_MARKTLOKATION\"\n          }\n        ],\n        \"marktrollen\": [\n          {\n            \"boTyp\": \"MARKTTEILNEHMER\",\n            \"gewerbekennzeichnung\": true,\n            \"marktrolle\": \"MSB\",\n            \"messstellenbetreiberEigenschaft\": \"GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER\",\n            \"rollencodenummer\": \"9910812000000\",\n            \"rollencodetyp\": \"BDEW\",\n            \"versionStruktur\": \"1\",\n            \"weiterverpflichtet\": false\n          }\n        ],\n        \"messtechnischeEinordnung\": \"KME_MME\",\n        \"netzebene\": \"NSP\",\n        \"sparte\": \"STROM\",\n        \"sperrstatus\": \"ENTSPERRT\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"MESSLOKATION\": [\n      {\n        \"boTyp\": \"MESSLOKATION\",\n        \"datenqualitaet\": \"INFORMATIVE_DATEN\",\n        \"marktrollen\": [\n          {\n            \"boTyp\": \"MARKTTEILNEHMER\",\n            \"gewerbekennzeichnung\": true,\n            \"marktrolle\": \"MSB\",\n            \"messstellenbetreiberEigenschaft\": \"GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER\",\n            \"rollencodenummer\": \"9910812000000\",\n            \"rollencodetyp\": \"BDEW\",\n            \"versionStruktur\": \"1\",\n            \"weiterverpflichtet\": false\n          },\n          {\n            \"boTyp\": \"MARKTTEILNEHMER\",\n            \"gewerbekennzeichnung\": true,\n            \"marktrolle\": \"GMSB\",\n            \"rollencodenummer\": \"9910812000000\",\n            \"rollencodetyp\": \"BDEW\",\n            \"versionStruktur\": \"1\"\n          }\n        ],\n        \"messlokationsId\": \"DE00713739359S0000000000001222221\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"NETZLOKATION\": [\n      {\n        \"boTyp\": \"NETZLOKATION\",\n        \"datenqualitaet\": \"INFORMATIVE_DATEN\",\n        \"marktrollen\": [\n          {\n            \"boTyp\": \"MARKTTEILNEHMER\",\n            \"gewerbekennzeichnung\": true,\n            \"marktrolle\": \"MSB\",\n            \"messstellenbetreiberEigenschaft\": \"GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER\",\n            \"rollencodenummer\": \"9910812000000\",\n            \"rollencodetyp\": \"BDEW\",\n            \"versionStruktur\": \"1\"\n          }\n        ],\n        \"netzlokationsId\": \"E1688117482\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"NETZNUTZUNGSVERTRAG\": [\n      {\n        \"boTyp\": \"VERTRAG\",\n        \"datenqualitaet\": \"INFORMATIVE_DATEN\",\n        \"korrespondenzpartner\": {\n          \"ansprechpartner\": {\n            \"boTyp\": \"ANSPRECHPARTNER\",\n            \"eMailAdresse\": \"max@mustermann.de\",\n            \"versionStruktur\": \"1\"\n          },\n          \"boTyp\": \"GESCHAEFTSPARTNER\",\n          \"gewerbekennzeichnung\": false,\n          \"name1\": \"Fank Müller\",\n          \"partneradresse\": {\n            \"hausnummer\": \"25\",\n            \"landescode\": \"DE\",\n            \"ort\": \"Musterstadt\",\n            \"ortsteil\": \"Musterortsteil\",\n            \"postleitzahl\": \"55555\",\n            \"strasse\": \"Wohnstrasse\"\n          },\n          \"versionStruktur\": \"1\"\n        },\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\",\n        \"vertragsart\": \"NETZNUTZUNGSVERTRAG\",\n        \"vertragsbeginn\": \"2025-11-01T23:00:00Z\",\n        \"vertragsende\": \"2025-11-30T23:00:00Z\",\n        \"vertragskonditionen\": {\n          \"haushaltskunde\": true\n        },\n        \"vertragspartner2\": [\n          {\n            \"boTyp\": \"GESCHAEFTSPARTNER\",\n            \"geschaeftspartnerrolle\": [\n              \"KUNDE\"\n            ],\n            \"gewerbekennzeichnung\": true,\n            \"name1\": \"Firma AG\",\n            \"name2\": \"Musterfirma\",\n            \"versionStruktur\": \"1\"\n          }\n        ]\n      }\n    ],\n    \"STEUERBARE_RESSOURCE\": [\n      {\n        \"boTyp\": \"STEUERBARE_RESSOURCE\",\n        \"datenqualitaet\": \"INFORMATIVE_DATEN\",\n        \"marktrollen\": [\n          {\n            \"boTyp\": \"MARKTTEILNEHMER\",\n            \"gewerbekennzeichnung\": true,\n            \"marktrolle\": \"MSB\",\n            \"messstellenbetreiberEigenschaft\": \"GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER\",\n            \"rollencodenummer\": \"9910812000000\",\n            \"rollencodetyp\": \"BDEW\",\n            \"versionStruktur\": \"1\"\n          }\n        ],\n        \"ressourcenId\": \"C816417ST77\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"TECHNISCHE_RESSOURCE\": [\n      {\n        \"boTyp\": \"TECHNISCHE_RESSOURCE\",\n        \"ressourcenId\": \"D417MLM8164\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9900327000009\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"datenaustauschreferenz\": \"DAICICNIOLJRFB\",\n    \"dokumentennummer\": \"DA942410151442459903323000007118027\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9903729000007\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"E01\",\n    \"nachrichtendatum\": \"2026-10-02T11:00:00Z\",\n    \"nachrichtenreferenznummer\": \"DACYYXETQZIAPR\",\n    \"pruefidentifikator\": \"55013\",\n    \"sparte\": \"STROM\",\n    \"transaktionsgrund\": \"Z36\",\n    \"transaktionsgrundergaenzung\": \"ZW7\",\n    \"transaktionsgrundergaenzungBefristeteAnmeldung\": \"E01\",\n    \"vertragsbeginn\": \"2025-11-01T23:00:00Z\",\n    \"vertragsende\": \"2025-11-30T23:00:00Z\",\n    \"vorgangsnummer\": \"24062416225400000000000102159662022\"\n  },\n  \"zusatzdaten\": {}\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

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
| [E_0615](/referenz/202610/ebd/E_0615) | Anmeldung E/G prüfen |

</details>

<a id="abschnitt-informationen"></a>

## Prozess-Informationen

Wortlaut der Lesefassung, Steckbrief Kap. 2.3.2.1, S. 33–34.

<Stepper>
<ol>

<li data-blatt="vorbedingungen">

### Vorbedingungen

- Es handelt sich um eine verbrauchende Marktlokation.
- Für die Marktlokation besteht eine gesetzliche Ersatzversorgungspflicht oder
- für die Marktlokation besteht eine gesetzliche Grundversorgungspflicht.
- Eine Zuordnungsermächtigung nach den Prozessen der MaBiS für die vom E/G genutzten BK liegt beim NB vor.

</li>

<li data-blatt="ergebnisse">

### Ergebnisse

- Der NB versendet die Berechnungsformel an den E/G.
- Der NB führt die Use-Cases „[Abrechnungsdaten Netznutzungsabrechnung](/prozessdoku/202610/NB/GPKE-Teil2-abrechnungsdaten-netznutzungsabrechnung)“ und „[Abrechnungsdaten Bilanzkreisabrechnung](/prozessdoku/202610/NB/GPKE-Teil2-abrechnungsdaten-bilanzkreisabrechnung)“ aus.
- Der NB führt den Use-Case „Stammdatenänderung“ (hier: SD „[Stammdatenänderung vom NB (verantwortlich) ausgehend](/prozessdoku/202610/NB/GPKE-Teil4-stammdatenaenderung-vom-nb-verantwortlich-ausgehend)“) (GPKE Teil 4) durch.
- Der NB führt den Use-Case „[Einrichtung der Konfigurationen aufgrund einer Zuordnung eines LF zu einer Marktlokation bzw. Tranche](/prozessdoku/202610/NB/GPKE-Teil3-einrichtung-der-konfigurationen-aufgrund-einer-zuordnung-eines-lf-zu-einer-marktlokation-bzw-tranche)“ (GPKE Teil 3) aus.
- Der LF führt den Use-Case „Stammdatenänderung“ (hier: SD „[Stammdatenänderung vom LF (verantwortlich) ausgehend](/prozessdoku/202610/NB/GPKE-Teil4-stammdatenaenderung-vom-lf-verantwortlich-ausgehend)“) (GPKE Teil 4) durch.

</li>

<li data-blatt="fehlerfall">

### Fehlerfall

#### Ergebnis im Fehlerfall

Der E/G wurde der Marktlokation nicht zugeordnet:
- Der NB muss sicherstellen, dass die von der Marktlokation entnommene Energie einem BK zugeordnet ist oder
- der NB muss die Unterbrechung der Anschlussnutzung an der Marktlokation durchführen. •

#### Fehlerfälle

- Es handelt sich um eine erzeugende Marktlokation bzw. eine Tranche.

</li>

<li data-blatt="anforderungen">

### Weitere Anforderungen

- Hat der NB ein Zuordnungsende eines LF erfasst, dem ein Zuordnungsbeginn eines LF folgt, wobei Zuordnungsende und Zuordnungsbeginn nicht kongruent sind, ist die Lücke zwischen dem Zuordnungsende und dem Zuordnungsbeginn durch eine befristete Zuordnung des E/G zur Marktlokation zu schließen. Dies kann z.B. aus der Versendung einer „Anfrage zur Beendigung der Zuordnung des LFA zur Marktlokation bzw. Tranche“ im Rahmen des Use-Cases „[Lieferbeginn](/prozessdoku/202610/NB/GPKE-Teil2-lieferbeginn)“ resultieren.
- Hinweis: Der Wechsel von der Ersatzversorgung in die Grundversorgung findet nach drei Monaten automatisch statt, sofern der E/G zu diesem Zeitpunkt der Marktlokation noch zugeordnet ist. Die Angabe, ob sich der Kunde in einer Ersatzversorgung oder Grundversorgung befindet, ist keine stammdatenänderungsrelevante Angabe, so dass durch den Wechsel von der Ersatzversorgung in die Grundversorgung keine Stammdatenänderung vom E/G an den NB erfolgt.
- Hinweis: Der E/G kann mit Hilfe des Use-Cases „[Lieferende von LF an NB](/prozessdoku/202610/NB/GPKE-Teil2-lieferende-von-lf-an-nb)“ das Grundversorgungsverhältnis bzw. Ersatzversorgungsverhältnis beenden.
- Für Fälle der vertraglich vereinbarten Ersatzbelieferung oder der vertraglich vereinbarten Fortsetzung der Ersatzversorgung (Ersatzfolgeversorgung) ist dieser Prozess analog anwendbar.

</li>

<li data-blatt="anlass">

### Anlass

- Der Marktlokation ist kein LF zugeordnet. Gründe können insbesondere sein:
- Beendigung der Zuordnung des LF zur Marktlokation aufgrund
  - Abmeldung der Zuordnung des LF zur Marklokation wegen Kündigung des Energieliefervertrages; ohne Folgebelieferung
  - Kündigung des Lieferantenrahmenvertrags
  - Information über die erfolgte Kündigung des Bilanzkreisvertrags durch den ÜNB
  - Erlöschen der durch den BKV gegenüber dem LF erteilten Zuordnungsermächtigung
  - geändertem Zeitreihentyp und keiner gültigen Zuordnungsermächtigung für den neuen Zeitreihentyp
- erstmalige Inbetriebnahme einer Marktlokation (Neuanlage)

**Vorher läuft:** [Abrechnungsdaten Netznutzungsabrechnung](/prozessdoku/202610/NB/GPKE-Teil2-abrechnungsdaten-netznutzungsabrechnung), [Lieferbeginn](/prozessdoku/202610/NB/GPKE-Teil2-lieferbeginn), [Lieferende von LF an NB](/prozessdoku/202610/NB/GPKE-Teil2-lieferende-von-lf-an-nb), [Lieferende von NB an LF](/prozessdoku/202610/NB/GPKE-Teil2-lieferende-von-nb-an-lf), [Neuanlage](/prozessdoku/202610/NB/GPKE-Teil2-neuanlage) — diese Prozesse nennen den hier gezeigten in ihrem Ergebnis.

</li>

<li data-blatt="erste-nachricht">

### Erste Nachricht

Der Beteiligte dieser Seite sendet selbst: „Ankündigung der Zuordnung des E/G zur Marktlokation“ an **LF (Notiz "entspricht E/G")** (Schritt 1).

</li>

<li data-blatt="ziel">

### Ziel

Der LF (im Nachfolgenden E/G genannt) ist der Marktlokation zugeordnet.

</li>

</ol>
</Stepper>

<a id="abschnitt-sichten"></a>

## Andere Sichten des Prozesses

Derselbe Prozess, aus den Augen der anderen Beteiligten: dieselben Schritte, jeweils aus deren Sicht gelesen.

- [Sicht LF](/prozessdoku/202610/LF/GPKE-Teil2-beginn-der-ersatz-grundversorgung) — LF

<Hinweisbereich>

*Die Schritte sind die **möglichen** Nachrichten dieses Prozesses, keine Abfolge — die Quelle führt weder Bedingungen noch Alternativen. Das Kästchen am Schritt nennt links die eigene Sicht: **←** empfängt sie, **→** sendet sie. Zugeklappte Schritte laufen zwischen anderen Marktpartnern.*

</Hinweisbereich>
