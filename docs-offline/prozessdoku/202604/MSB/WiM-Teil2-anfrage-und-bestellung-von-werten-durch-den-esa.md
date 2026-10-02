# Anfrage und Bestellung von Werten durch den ESA — Sicht MSB

<Kopf rolle="MSB" beteiligter="MSB" festlegung="WiM" dokument="WiM Strom Teil 2" kapitel="4.1.2" sparte="Strom" schritte={6} suchtitel="Anfrage und Bestellung von Werten durch den ESA — Sicht MSB · WiM Strom Teil 2 · Formatversion 202604" abschnitte={[{"id": "abschnitt-ablauf", "label": "Prozessablauf"}, {"id": "abschnitt-schritte", "label": "Prozessschritte"}, {"id": "abschnitt-informationen", "label": "Prozess-Informationen"}, {"id": "abschnitt-sichten", "label": "Andere Sichten des Prozesses"}]} />

<Kurzfassung>

Der ESA fragt die Übermittlung von Werten und die damit verbundenen Kosten beim MSB an. Sofern die Werte in der bestellten Granularität und dem bestellten Umfang durch den MSB (aus dem Back-End-System oder direkt aus dem iMS) zur Verfügung gestellt werden können, erstellt der MSB ein Angebot für diese Übermittlung von Werten, das er dem ESA zur Verfügung stellt. Der ESA kann daraufhin die Übermittlung von Werten bestellen. Möchte der ESA die Werte auf Ebene der Marktlokation erhalten, richtet er seine Anfrage und Bestellung an den MSB der Marktlokation. Möchte der ESA die Werte auf Ebene der Messlokation erhalten, richtet er seine Anfrage und Bestellung an den MSB der Messlokation. Möchte der ESA die Werte auf Ebene der Netzlokation erhalten, richtet er seine Anfrage und Bestellung an den MSB der Netzlokation.

</Kurzfassung>

<a id="abschnitt-ablauf"></a>

## Prozessablauf aus Sicht des MSB

<Systembild svg={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1004 1060\" width=\"1004\" height=\"1060\" role=\"img\" aria-labelledby=\"sb-title\" class=\"maco-systembild\">\n<title id=\"sb-title\">Systembild: Anfrage und Bestellung von Werten durch den ESA aus Sicht MSB</title>\n<defs><marker id=\"sb-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect class=\"sb-lane-kopf\" x=\"16\" y=\"12\" width=\"232\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend-System des Kunden</text>\n<rect class=\"sb-lane-kopf\" x=\"398\" y=\"12\" width=\"264\" height=\"46\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · MSB</text>\n<rect class=\"sb-lane-kopf\" x=\"812\" y=\"12\" width=\"176\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"900\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Marktpartner</text>\n<line x1=\"323\" y1=\"58\" x2=\"323\" y2=\"1048\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"737\" y1=\"58\" x2=\"737\" y2=\"1048\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"80\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">1. Anfrage von Werten</text>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"78\" r=\"5\"/><line x1=\"900\" y1=\"83\" x2=\"900\" y2=\"95\"/><line x1=\"893\" y1=\"87\" x2=\"907\" y2=\"87\"/><line x1=\"900\" y1=\"95\" x2=\"894\" y2=\"105\"/><line x1=\"900\" y1=\"95\" x2=\"906\" y2=\"105\"/></g>\n<text x=\"900\" y=\"127\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">ESA</text>\n<line x1=\"878\" y1=\"96\" x2=\"628\" y2=\"96\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"88\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"112\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">35003</text>\n<rect class=\"sb-kasten sb-schreiben\" x=\"432\" y=\"163\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"183\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"113\" x2=\"530\" y2=\"163\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-schreiben sb-abgeleitet\" x=\"34\" y=\"163\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"183\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten erstellen</text>\n<line x1=\"432\" y1=\"179\" x2=\"230\" y2=\"179\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"171\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-folge_ausloeser\" x=\"432\" y=\"227\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"247\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Ausgelöst durch Eingang:</text>\n<text x=\"530\" y=\"262\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">35004</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"196\" x2=\"530\" y2=\"227\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"301\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"321\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">2. Angebot zur / Ablehnung</text>\n<text x=\"530\" y=\"336\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">der Anfrage</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"275\" x2=\"530\" y2=\"301\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"307\" r=\"5\"/><line x1=\"900\" y1=\"312\" x2=\"900\" y2=\"324\"/><line x1=\"893\" y1=\"316\" x2=\"907\" y2=\"316\"/><line x1=\"900\" y1=\"324\" x2=\"894\" y2=\"334\"/><line x1=\"900\" y1=\"324\" x2=\"906\" y2=\"334\"/></g>\n<text x=\"900\" y=\"356\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">ESA</text>\n<line x1=\"628\" y1=\"325\" x2=\"878\" y2=\"325\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"317\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"341\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">15003, 21033</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"384\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"404\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"349\" x2=\"530\" y2=\"384\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"384\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"404\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"400\" x2=\"230\" y2=\"400\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"392\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"448\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"468\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">3. Bestellung</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"417\" x2=\"530\" y2=\"448\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"446\" r=\"5\"/><line x1=\"900\" y1=\"451\" x2=\"900\" y2=\"463\"/><line x1=\"893\" y1=\"455\" x2=\"907\" y2=\"455\"/><line x1=\"900\" y1=\"463\" x2=\"894\" y2=\"473\"/><line x1=\"900\" y1=\"463\" x2=\"906\" y2=\"473\"/></g>\n<text x=\"900\" y=\"495\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">ESA</text>\n<line x1=\"878\" y1=\"464\" x2=\"628\" y2=\"464\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"456\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"480\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">17007</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"531\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"551\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"481\" x2=\"530\" y2=\"531\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben sb-abgeleitet\" x=\"34\" y=\"531\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"551\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"547\" x2=\"230\" y2=\"547\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"539\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"595\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"615\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">4. Antwort auf Bestellung</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"564\" x2=\"530\" y2=\"595\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"593\" r=\"5\"/><line x1=\"900\" y1=\"598\" x2=\"900\" y2=\"610\"/><line x1=\"893\" y1=\"602\" x2=\"907\" y2=\"602\"/><line x1=\"900\" y1=\"610\" x2=\"894\" y2=\"620\"/><line x1=\"900\" y1=\"610\" x2=\"906\" y2=\"620\"/></g>\n<text x=\"900\" y=\"642\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">ESA</text>\n<line x1=\"628\" y1=\"611\" x2=\"878\" y2=\"611\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"603\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"627\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">19011, 19012</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"678\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"698\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"628\" x2=\"530\" y2=\"678\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"678\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"698\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"694\" x2=\"230\" y2=\"694\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"686\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"742\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"762\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">5. Stornierung einer</text>\n<text x=\"530\" y=\"777\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">bestätigten Bestellung</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"711\" x2=\"530\" y2=\"742\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"748\" r=\"5\"/><line x1=\"900\" y1=\"753\" x2=\"900\" y2=\"765\"/><line x1=\"893\" y1=\"757\" x2=\"907\" y2=\"757\"/><line x1=\"900\" y1=\"765\" x2=\"894\" y2=\"775\"/><line x1=\"900\" y1=\"765\" x2=\"906\" y2=\"775\"/></g>\n<text x=\"900\" y=\"797\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">ESA</text>\n<line x1=\"878\" y1=\"766\" x2=\"628\" y2=\"766\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"758\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"782\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">39002</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"825\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"845\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"790\" x2=\"530\" y2=\"825\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben sb-abgeleitet\" x=\"34\" y=\"825\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"845\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"841\" x2=\"230\" y2=\"841\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"833\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"889\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"909\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">6. Antwort auf Stornierung</text>\n<text x=\"530\" y=\"924\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">einer bestätigten Bestellung</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"858\" x2=\"530\" y2=\"889\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"895\" r=\"5\"/><line x1=\"900\" y1=\"900\" x2=\"900\" y2=\"912\"/><line x1=\"893\" y1=\"904\" x2=\"907\" y2=\"904\"/><line x1=\"900\" y1=\"912\" x2=\"894\" y2=\"922\"/><line x1=\"900\" y1=\"912\" x2=\"906\" y2=\"922\"/></g>\n<text x=\"900\" y=\"944\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">ESA</text>\n<line x1=\"628\" y1=\"913\" x2=\"878\" y2=\"913\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"905\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"929\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">19013, 19014</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"972\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"992\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"937\" x2=\"530\" y2=\"972\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"972\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"992\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"988\" x2=\"230\" y2=\"988\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"980\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n</svg>"} gesamt={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 730 858\" width=\"730\" height=\"858\" role=\"img\" aria-labelledby=\"sd-title\" class=\"maco-sequence\">\n<title id=\"sd-title\">Sequenzdiagramm: Anfrage und Bestellung von Werten durch den ESA aus Sicht MSB</title>\n<defs><marker id=\"sd-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect x=\"16\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"121\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend (Kunde)</text>\n<line x1=\"121\" y1=\"64\" x2=\"121\" y2=\"846\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"260\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"365\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · MSB</text>\n<line x1=\"365\" y1=\"64\" x2=\"365\" y2=\"846\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"504\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"609\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">ESA</text>\n<line x1=\"609\" y1=\"64\" x2=\"609\" y2=\"846\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"609\" y1=\"90\" x2=\"365\" y2=\"90\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"81\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">1. Anfrage von Werten</text>\n<text x=\"487\" y=\"105\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 35003</text>\n<line x1=\"365\" y1=\"152\" x2=\"121\" y2=\"152\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"143\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<text x=\"243\" y=\"167\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten erstellen</text>\n<line x1=\"365\" y1=\"214\" x2=\"609\" y2=\"214\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"205\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">2. Angebot zur / Ablehnung der Anfrage</text>\n<text x=\"487\" y=\"229\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 15003, 21033 · E_0252</text>\n<text x=\"487\" y=\"242\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0252 — Anfrage prüfen</text>\n<line x1=\"365\" y1=\"276\" x2=\"121\" y2=\"276\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"267\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"291\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"609\" y1=\"338\" x2=\"365\" y2=\"338\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"329\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">3. Bestellung</text>\n<text x=\"487\" y=\"353\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 17007</text>\n<line x1=\"365\" y1=\"400\" x2=\"121\" y2=\"400\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"391\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"415\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"365\" y1=\"462\" x2=\"609\" y2=\"462\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"453\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">4. Antwort auf Bestellung</text>\n<text x=\"487\" y=\"477\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 19011, 19012 · E_0256</text>\n<text x=\"487\" y=\"490\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0256 — Bestellung prüfen</text>\n<line x1=\"365\" y1=\"524\" x2=\"121\" y2=\"524\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"515\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"539\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"609\" y1=\"586\" x2=\"365\" y2=\"586\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"577\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">5. Stornierung einer bestätigten Bestellung</text>\n<text x=\"487\" y=\"601\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 39002</text>\n<line x1=\"365\" y1=\"648\" x2=\"121\" y2=\"648\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"639\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"663\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"365\" y1=\"710\" x2=\"609\" y2=\"710\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"701\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">6. Antwort auf Stornierung einer bestätigten Bes…</text>\n<text x=\"487\" y=\"725\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 19013, 19014 · E_0257</text>\n<text x=\"487\" y=\"738\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0257 — Stornierung prüfen</text>\n<line x1=\"365\" y1=\"772\" x2=\"121\" y2=\"772\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"763\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"787\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n</svg>"} titel="MSB" />

<a id="abschnitt-schritte"></a>

## Prozessschritte

<Schritt nr="1" anker="schritt-1" richtung="eingehend" kopf={{"links": {"label": "MSB", "eigen": true}, "rechts": {"label": "ESA"}}}>

### Anfrage von Werten

<Schrittskizze sicht={{"label": "MSB"}} zeilen={[{"art": "empfangen", "label": "ESA", "weg": "AS4", "nachrichten": [{"nr": "35003", "titel": "Anfrage von Werten"}]}, {"art": "erstellen"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [35003](/schnittstellen/202604/pruefi/REQOTE/PI_35003) — Anfrage von Werten · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **ESA** · AS4

</li>

<li data-teil="schnittstelle" data-art="schreiben" data-abgeleitet="ja">

**Schreibende Schnittstelle**
- Vorgang angelegt — [Prozessdaten erstellen](/api/202604/backend-schreiben-msb/createprocessdata#prozessdaten-erstellen) `POST /createProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/createProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "ERSTELLEN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Legt im Backend einen neuen Vorgang mit den Daten der eingegangenen Nachricht an.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="2" anker="schritt-2" richtung="ausgehend" kopf={{"links": {"label": "MSB", "eigen": true}, "rechts": {"label": "ESA"}}}>

### Angebot zur / Ablehnung der Anfrage

<Schrittskizze sicht={{"label": "MSB"}} zeilen={[{"art": "folge_ausloeser", "werte": ["35004"]}, {"art": "senden", "label": "ESA", "weg": "AS4", "nachrichten": [{"nr": "15003", "titel": "Angebot zur Anfrage von Werten"}, {"nr": "21033", "titel": "Ablehnung der Anfrage"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [15003](/schnittstellen/202604/pruefi/QUOTES/PI_15003) — Angebot zur Anfrage von Werten · AS4
- [21033](/schnittstellen/202604/pruefi/IFTSTA/PI_21033) — Ablehnung der Anfrage · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="folge_ausloeser">

**Ausgelöst durch Eingang**
- [35004](/schnittstellen/202604/pruefi/REQOTE/PI_35004)

Die MACO APP sendet diese Nachricht selbst, als Folgeprozess nach diesem Eingang.

</li>

<li data-teil="nachricht">

Nachricht an **ESA** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `21033` → [E_0252](/referenz/202604/ebd/E_0252) · MSB · Anfrage prüfen

</div>

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202604/backend-schreiben-msb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"ANFRAGE\": [\n      {\n        \"boTyp\": \"ANFRAGE\",\n        \"lokationsId\": \"24471812600\",\n        \"lokationsTyp\": \"MALO\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"ANGEBOT\": [\n      {\n        \"anfragereferenz\": \"123456789\",\n        \"bindefristAngebot\": {\n          \"dauer\": 2,\n          \"einheit\": \"MONAT\"\n        },\n        \"boTyp\": \"ANGEBOT\",\n        \"gesamtkosten\": {\n          \"waehrung\": \"EUR\"\n        },\n        \"positionsdaten\": [\n          {\n            \"artikelId\": [\n              \"9991000000747-01\",\n              \"9991000000747-02\"\n            ],\n            \"positionsbezeichnung\": \"1\",\n            \"positionspreis\": [\n              {\n                \"bezugswert\": \"STUECK\",\n                \"menge\": 1,\n                \"preisart\": \"EINRICHTUNGSPREIS\",\n                \"wert\": 5.1234\n              },\n              {\n                \"bezugswert\": \"STUECK\",\n                \"menge\": 1,\n                \"preisart\": \"TRANSAKTIONSPREIS\",\n                \"wert\": 5.1234\n              }\n            ]\n          }\n        ],\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\",\n        \"zeitspanneEinrichtungUebermittlungWerte\": {\n          \"dauer\": 4,\n          \"einheit\": \"WOCHE\"\n        }\n      }\n    ],\n    \"MARKTLOKATION\": [\n      {\n        \"boTyp\": \"MARKTLOKATION\",\n        \"marktlokationsId\": \"24471812600\",\n        \"marktlokationsTyp\": [\n          {\n            \"typ\": \"STANDARD_MARKTLOKATION\"\n          }\n        ],\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"WERTE_NACH_TYP2\": [\n      {\n        \"boTyp\": \"WERTE_NACH_TYP2\",\n        \"messprodukt\": \"9991000000747\",\n        \"versionStruktur\": \"1\",\n        \"zaehlwerke\": [\n          {\n            \"obisKennzahl\": \"1-1:1.29.0\"\n          }\n        ]\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"ansprechpartner\": {\n        \"boTyp\": \"ANSPRECHPARTNER\",\n        \"nachname\": \"Max Mustermann\",\n        \"rufnummern\": [\n          {\n            \"nummerntyp\": \"FAX_DURCHWAHL\",\n            \"rufnummer\": \"+012345678910\"\n          }\n        ],\n        \"versionStruktur\": \"1\"\n      },\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9904733000009\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"datenaustauschreferenz\": \"131253\",\n    \"dokumentennummer\": \"BGM12345\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9984778000008\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"freitext\": \"Blabla\",\n    \"kategorie\": \"Z57\",\n    \"nachrichtendatum\": \"2025-10-30T07:15:00Z\",\n    \"nachrichtenreferenznummer\": \"647809\",\n    \"pruefidentifikator\": \"15003\",\n    \"sparte\": \"STROM\",\n    \"startdatum\": \"2026-06-30T22:00:00Z\"\n  },\n  \"zusatzdaten\": {}\n}"} examples={[{"mediaType": "application/json", "examples": [{"name": "15003", "summary": "15003 — Angebot zur Anfrage von Werten", "value": {"stammdaten": {"WERTE_NACH_TYP2": [{"boTyp": "WERTE_NACH_TYP2", "versionStruktur": "1", "messprodukt": "9991000000747", "zaehlwerke": [{"obisKennzahl": "1-1:1.29.0"}]}], "MARKTLOKATION": [{"boTyp": "MARKTLOKATION", "versionStruktur": "1", "marktlokationsId": "24471812600", "marktlokationsTyp": [{"typ": "STANDARD_MARKTLOKATION"}], "sparte": "STROM"}], "ANFRAGE": [{"boTyp": "ANFRAGE", "versionStruktur": "1", "lokationsId": "24471812600", "lokationsTyp": "MALO"}], "ANGEBOT": [{"boTyp": "ANGEBOT", "versionStruktur": "1", "zeitspanneEinrichtungUebermittlungWerte": {"dauer": 4, "einheit": "WOCHE"}, "bindefristAngebot": {"dauer": 2, "einheit": "MONAT"}, "anfragereferenz": "123456789", "sparte": "STROM", "gesamtkosten": {"waehrung": "EUR"}, "positionsdaten": [{"positionsbezeichnung": "1", "positionspreis": [{"wert": 5.1234, "menge": 1, "bezugswert": "STUECK", "preisart": "EINRICHTUNGSPREIS"}, {"wert": 5.1234, "menge": 1, "bezugswert": "STUECK", "preisart": "TRANSAKTIONSPREIS"}], "artikelId": ["9991000000747-01", "9991000000747-02"]}]}]}, "transaktionsdaten": {"datenaustauschreferenz": "131253", "sparte": "STROM", "pruefidentifikator": "15003", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9904733000009", "rollencodetyp": "BDEW", "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "nachname": "Max Mustermann", "rufnummern": [{"nummerntyp": "FAX_DURCHWAHL", "rufnummer": "+012345678910"}]}}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9984778000008", "rollencodetyp": "BDEW"}, "dokumentennummer": "BGM12345", "kategorie": "Z57", "nachrichtendatum": "2025-10-30T07:15:00Z", "nachrichtenreferenznummer": "647809", "startdatum": "2026-06-30T22:00:00Z", "freitext": "Blabla"}, "zusatzdaten": {}}}, {"name": "21033", "summary": "21033 — Ablehnung der Anfrage", "value": {"stammdaten": {"MARKTLOKATION": [{"boTyp": "MARKTLOKATION", "versionStruktur": "1", "marktlokationsId": "44152365487", "marktlokationsTyp": [{"typ": "STANDARD_MARKTLOKATION"}], "sparte": "STROM"}], "STATUSMITTEILUNG": [{"boTyp": "STATUSMITTEILUNG", "versionStruktur": "1", "statusObjekt": "ANGEBOTANFRAGE", "auftragsstatus": "ABGELEHNT", "positionsdaten": [{"positionsnummer": 1}]}]}, "transaktionsdaten": {"datenaustauschreferenz": "M0KXRR1W", "sparte": "STROM", "pruefidentifikator": "21033", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9904733000009", "rollencodetyp": "BDEW", "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "nachname": "Laue", "eMailAdresse": "lieferantenwechsel@eon-energie.com"}}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900244000009", "rollencodetyp": "BDEW"}, "dokumentennummer": "M0YOR4X5", "kategorie": "Z09", "nachrichtendatum": "2025-10-17T06:36:00Z", "nachrichtenreferenznummer": "M11I1RWQ", "anfragereferenznummer": "7584", "antwortstatus": "A01", "antwortstatusCodeliste": "E_0524"}, "zusatzdaten": {}}}]}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend fort, nachdem die Nachricht erstellt ist.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="3" anker="schritt-3" richtung="eingehend" kopf={{"links": {"label": "MSB", "eigen": true}, "rechts": {"label": "ESA"}}}>

### Bestellung

<Schrittskizze sicht={{"label": "MSB"}} zeilen={[{"art": "empfangen", "label": "ESA", "weg": "AS4", "nachrichten": [{"nr": "17007", "titel": "Bestellung von Werten"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [17007](/schnittstellen/202604/pruefi/ORDERS/PI_17007) — Bestellung von Werten · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **ESA** · AS4

</li>

<li data-teil="schnittstelle" data-art="fortschreiben" data-abgeleitet="ja">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202604/backend-schreiben-msb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend mit den Daten der eingegangenen Nachricht fort.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="4" anker="schritt-4" richtung="ausgehend" kopf={{"links": {"label": "MSB", "eigen": true}, "rechts": {"label": "ESA"}}}>

### Antwort auf Bestellung

<Schrittskizze sicht={{"label": "MSB"}} zeilen={[{"art": "senden", "label": "ESA", "weg": "AS4", "nachrichten": [{"nr": "19011", "titel": "Bestätigung der Ab-/Bestellung von Werten"}, {"nr": "19012", "titel": "Ablehnung der Ab-/Bestellung von Werten"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [19011](/schnittstellen/202604/pruefi/ORDRSP/PI_19011) — Bestätigung der Ab-/Bestellung von Werten · AS4
- [19012](/schnittstellen/202604/pruefi/ORDRSP/PI_19012) — Ablehnung der Ab-/Bestellung von Werten · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht an **ESA** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `19011`, `19012` → [E_0256](/referenz/202604/ebd/E_0256) · MSB · Bestellung prüfen

</div>

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202604/backend-schreiben-msb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"ANFRAGE\": [\n      {\n        \"abonnement\": \"START_ABO\",\n        \"anfragekategorie\": \"UEBERMITTLUNG_WERTE_AN_ESA\",\n        \"boTyp\": \"ANFRAGE\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"AUFTRAG\": [\n      {\n        \"boTyp\": \"AUFTRAG\",\n        \"positionsdaten\": [\n          {\n            \"positionsnummer\": 1\n          }\n        ],\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"ansprechpartner\": {\n        \"boTyp\": \"ANSPRECHPARTNER\",\n        \"nachname\": \"P GETTY\",\n        \"rufnummern\": [\n          {\n            \"nummerntyp\": \"RUF_DURCHWAHL\",\n            \"rufnummer\": \"+3222271020\"\n          }\n        ],\n        \"versionStruktur\": \"1\"\n      },\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"ipAdresse\": \"2001:db8:85a3::8a2e:370:7344\",\n      \"ipRange\": {\n        \"obereGrenze\": \"203.0.113.255\",\n        \"untereGrenze\": \"203.0.113.195\"\n      },\n      \"rollencodenummer\": \"9904990000008\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"antwortstatus\": \"A11\",\n    \"antwortstatusCodeliste\": \"E_0256\",\n    \"auftragsReferenz\": \"AFN9523\",\n    \"datenaustauschreferenz\": \"DAZCCWFCMJGIFF\",\n    \"dokumentennummer\": \"DA632411190833439903323000007216138\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9984778000008\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"Z57\",\n    \"nachrichtendatum\": \"2025-06-24T12:31:00Z\",\n    \"nachrichtenreferenznummer\": \"DAIEHVOXSZEDBE\",\n    \"pruefidentifikator\": \"19011\",\n    \"sparte\": \"STROM\"\n  },\n  \"zusatzdaten\": {}\n}"} examples={[{"mediaType": "application/json", "examples": [{"name": "19011", "summary": "19011 — Bestätigung der Ab-/Bestellung von Werten", "value": {"stammdaten": {"ANFRAGE": [{"boTyp": "ANFRAGE", "versionStruktur": "1", "anfragekategorie": "UEBERMITTLUNG_WERTE_AN_ESA", "abonnement": "START_ABO"}], "AUFTRAG": [{"boTyp": "AUFTRAG", "versionStruktur": "1", "positionsdaten": [{"positionsnummer": 1}]}]}, "transaktionsdaten": {"datenaustauschreferenz": "DAZCCWFCMJGIFF", "sparte": "STROM", "pruefidentifikator": "19011", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9904990000008", "rollencodetyp": "BDEW", "ipAdresse": "2001:db8:85a3::8a2e:370:7344", "ipRange": {"untereGrenze": "203.0.113.195", "obereGrenze": "203.0.113.255"}, "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "nachname": "P GETTY", "rufnummern": [{"nummerntyp": "RUF_DURCHWAHL", "rufnummer": "+3222271020"}]}}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9984778000008", "rollencodetyp": "BDEW"}, "dokumentennummer": "DA632411190833439903323000007216138", "kategorie": "Z57", "nachrichtendatum": "2025-06-24T12:31:00Z", "nachrichtenreferenznummer": "DAIEHVOXSZEDBE", "auftragsReferenz": "AFN9523", "antwortstatus": "A11", "antwortstatusCodeliste": "E_0256"}, "zusatzdaten": {}}}, {"name": "19012", "summary": "19012 — Ablehnung der Ab-/Bestellung von Werten", "value": {"stammdaten": {"ANFRAGE": [{"boTyp": "ANFRAGE", "versionStruktur": "1", "anfragekategorie": "UEBERMITTLUNG_WERTE_AN_ESA", "abonnement": "START_ABO"}]}, "transaktionsdaten": {"datenaustauschreferenz": "DAZPYQWBJFRLWQ", "sparte": "STROM", "pruefidentifikator": "19012", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9904990000008", "rollencodetyp": "BDEW", "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "nachname": "P GETTY", "rufnummern": [{"nummerntyp": "RUF_DURCHWAHL", "rufnummer": "+3222271020"}]}}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9984778000008", "rollencodetyp": "BDEW"}, "dokumentennummer": "DA112411190836049903323000007441962", "kategorie": "Z57", "nachrichtendatum": "2025-06-24T12:31:00Z", "nachrichtenreferenznummer": "DATPOASVFMJOMG", "auftragsReferenz": "AFN9523", "antwortstatus": "A01", "antwortstatusCodeliste": "E_0256"}, "zusatzdaten": {}}}]}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend fort, nachdem die Nachricht erstellt ist.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="5" anker="schritt-5" richtung="eingehend" kopf={{"links": {"label": "MSB", "eigen": true}, "rechts": {"label": "ESA"}}}>

### Stornierung einer bestätigten Bestellung

<Schrittskizze sicht={{"label": "MSB"}} zeilen={[{"art": "empfangen", "label": "ESA", "weg": "AS4", "nachrichten": [{"nr": "39002", "titel": "Stornierung der Bestellung"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [39002](/schnittstellen/202604/pruefi/ORDCHG/PI_39002) — Stornierung der Bestellung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **ESA** · AS4

</li>

<li data-teil="schnittstelle" data-art="fortschreiben" data-abgeleitet="ja">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202604/backend-schreiben-msb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend mit den Daten der eingegangenen Nachricht fort.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="6" anker="schritt-6" richtung="ausgehend" kopf={{"links": {"label": "MSB", "eigen": true}, "rechts": {"label": "ESA"}}}>

### Antwort auf Stornierung einer bestätigten Bestellung

<Schrittskizze sicht={{"label": "MSB"}} zeilen={[{"art": "senden", "label": "ESA", "weg": "AS4", "nachrichten": [{"nr": "19013", "titel": "Bestätigung der Stornierung einer Bestellung"}, {"nr": "19014", "titel": "Ablehnung der Stornierung einer Bestellung"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [19013](/schnittstellen/202604/pruefi/ORDRSP/PI_19013) — Bestätigung der Stornierung einer Bestellung · AS4
- [19014](/schnittstellen/202604/pruefi/ORDRSP/PI_19014) — Ablehnung der Stornierung einer Bestellung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht an **ESA** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `19013`, `19014` → [E_0257](/referenz/202604/ebd/E_0257) · MSB · Stornierung prüfen

</div>

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202604/backend-schreiben-msb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"ANFRAGE\": [\n      {\n        \"anfragekategorie\": \"UEBERMITTLUNG_WERTE_AN_ESA\",\n        \"boTyp\": \"ANFRAGE\",\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"ansprechpartner\": {\n        \"boTyp\": \"ANSPRECHPARTNER\",\n        \"nachname\": \"P GETTY\",\n        \"rufnummern\": [\n          {\n            \"nummerntyp\": \"RUF_DURCHWAHL\",\n            \"rufnummer\": \"+3222271020\"\n          }\n        ],\n        \"versionStruktur\": \"1\"\n      },\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9904990000008\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"antwortstatus\": \"A04\",\n    \"antwortstatusCodeliste\": \"E_0257\",\n    \"datenaustauschreferenz\": \"DAPTYEAIUMDWUQ\",\n    \"dokumentennummer\": \"DA752411190838209903323000007411105\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9984778000008\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"Z57\",\n    \"nachrichtendatum\": \"2025-06-24T12:31:00Z\",\n    \"nachrichtenreferenznummer\": \"DAJJXWXMCXHABP\",\n    \"pruefidentifikator\": \"19013\",\n    \"sparte\": \"STROM\",\n    \"vorgangsreferenznummer\": \"REF32412\"\n  },\n  \"zusatzdaten\": {}\n}"} examples={[{"mediaType": "application/json", "examples": [{"name": "19013", "summary": "19013 — Bestätigung der Stornierung einer Bestellung", "value": {"stammdaten": {"ANFRAGE": [{"boTyp": "ANFRAGE", "versionStruktur": "1", "anfragekategorie": "UEBERMITTLUNG_WERTE_AN_ESA"}]}, "transaktionsdaten": {"datenaustauschreferenz": "DAPTYEAIUMDWUQ", "sparte": "STROM", "pruefidentifikator": "19013", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9904990000008", "rollencodetyp": "BDEW", "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "nachname": "P GETTY", "rufnummern": [{"nummerntyp": "RUF_DURCHWAHL", "rufnummer": "+3222271020"}]}}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9984778000008", "rollencodetyp": "BDEW"}, "dokumentennummer": "DA752411190838209903323000007411105", "kategorie": "Z57", "nachrichtendatum": "2025-06-24T12:31:00Z", "nachrichtenreferenznummer": "DAJJXWXMCXHABP", "vorgangsreferenznummer": "REF32412", "antwortstatus": "A04", "antwortstatusCodeliste": "E_0257"}, "zusatzdaten": {}}}, {"name": "19014", "summary": "19014 — Ablehnung der Stornierung einer Bestellung", "value": {"stammdaten": {"ANFRAGE": [{"boTyp": "ANFRAGE", "versionStruktur": "1", "anfragekategorie": "UEBERMITTLUNG_WERTE_AN_ESA"}]}, "transaktionsdaten": {"datenaustauschreferenz": "DAASVJZSQPKXWU", "sparte": "STROM", "pruefidentifikator": "19014", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9904990000008", "rollencodetyp": "BDEW", "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "nachname": "P GETTY", "rufnummern": [{"nummerntyp": "RUF_DURCHWAHL", "rufnummer": "+3222271020"}]}}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9984778000008", "rollencodetyp": "BDEW"}, "dokumentennummer": "DA702411190839419903323000007874247", "kategorie": "Z57", "nachrichtendatum": "2025-06-24T12:31:00Z", "nachrichtenreferenznummer": "DABVDIWYHATKZT", "vorgangsreferenznummer": "REF32412", "antwortstatus": "A01", "antwortstatusCodeliste": "E_0257"}, "zusatzdaten": {}}}]}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

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
| [E_0252](/referenz/202604/ebd/E_0252) | Anfrage prüfen |
| [E_0256](/referenz/202604/ebd/E_0256) | Bestellung prüfen |
| [E_0257](/referenz/202604/ebd/E_0257) | Stornierung prüfen |

</details>

<a id="abschnitt-informationen"></a>

## Prozess-Informationen

Wortlaut der Lesefassung, Steckbrief Kap. 4.1.1, S. 69–71.

<Stepper>
<ol>

<li data-blatt="vorbedingungen">

### Vorbedingungen

- Die Zusicherung des ESA zur Einhaltung der rechtlichen Vorgaben zum Datenschutz liegt beim MSB vor.
- Die vertragliche Grundlage zur Anfrage und Übermittlung der Werte und Abrechnung der erbrachten Dienstleistung vom MSB an den ESA liegt beim MSB vor.
- Bei Anfrage von Werten auf Ebene der Marktlokation:
  - Der Messstellenbetrieb wird an allen Messlokationen der Marktlokation von demselben MSB durchgeführt; d.h. der MSB der Marktlokation ist der MSB der Messlokation(en).
- Bei Anfrage von Werten auf Ebene der Netzlokation:
  - Der Messstellenbetrieb wird an allen Messlokationen der Netzlokation von demselben MSB durchgeführt; d.h. der MSB der Netzlokation ist der MSB der Messlokation(en).
- Die EDIFACT-Kommunikation zwischen dem MSB und dem ESA ist aufgebaut.
- Die vorhandene Gerätetechnik ermöglicht die Übermittlung der angefragten Werte.
- Bei Übermittlung von Werten aus dem iMS: Alle für die Erbringung der Übermittlung von Werten benötigten Messlokationen sind mit einem iMS ausgestattet.

</li>

<li data-blatt="ergebnisse">

### Ergebnisse

- Der MSB erbringt die vom ESA bestellte Übermittlung von Werten (aus dem Back-End-System oder direkt aus dem iMS).
- Im Fall, dass die Messlokation mit iMS ausgestattet ist: Sofern eine Parametrierung der Messeinrichtung für die Erbringung der Übermittlung von Werten notwendig ist, führt der MSB die Parametrierung der Messeinrichtung durch.

</li>

<li data-blatt="fehlerfall">

### Fehlerfall

#### Ergebnis im Fehlerfall

- Die Übermittlung von Werten kann nicht erbracht werden.

#### Fehlerfälle

- Der MSB ist für den angefragten Zeitraum der Marktlokation /Messlokation/Netzlokation nicht zugeordnet.
- Die vorhandene Gerätetechnik ermöglicht die Übermittlung der angefragten Werte nicht.
- Die rechtliche Grundlage zur Übermittlung von Werten ist nicht gegeben.

</li>

<li data-blatt="anforderungen">

### Weitere Anforderungen

- Die Anfrage von Werten hat immer an den der Messlokation /Marktlokation/Netzlokation zugeordneten MSB zu erfolgen, der zu dem Zeitraum, für den die Werte benötigt werden, der Marktlokation/Messlokation/Netzlokation zugeordnet ist. Dies gilt auch für Vergangenheitswerte.
- Die Anfrage von Werten kann nur für den Zeitraum erfolgen, für den der AN der Marktlokation/Messlokation/Netzlokation zugeordnet ist.
- Die Bestellung anderweitiger, von diesem Use-Case nicht erfasster Arten der Werte/Übermittlung von Werten durch den ESA gegenüber dem MSB im Wege einer NON-EDIFACT-Kommunikation (Textform) bleiben weiterhin jederzeit möglich.
- Sofern die vorhandene Gerätetechnik die angefragte Übermittlung von Werten nicht ermöglicht, ist die Änderung der Gerätetechnik nicht über diesen Use-Case zu bestellen. Diesen Wunsch hat der ESA unter Einbeziehung des AN außerhalb der Prozessstandardisierung (somit via NON-EDIFACT) an den MSB zu übermitteln.

</li>

<li data-blatt="erste-nachricht">

### Erste Nachricht

**ESA** sendet „Anfrage von Werten“ (Schritt 1). Ab hier ist der Beteiligte dieser Seite am Zug.

</li>

<li data-blatt="ziel">

### Ziel

Der ESA hat beim MSB die Übermittlung von Werten bestellt.

</li>

</ol>
</Stepper>

<a id="abschnitt-sichten"></a>

## Andere Sichten des Prozesses

Derselbe Prozess, aus den Augen der anderen Beteiligten: dieselben Schritte, jeweils aus deren Sicht gelesen.

- [Sicht ESA](/prozessdoku/202604/ESA/WiM-Teil2-anfrage-und-bestellung-von-werten-durch-den-esa) — ESA

<Hinweisbereich>

*Die Schritte sind die **möglichen** Nachrichten dieses Prozesses, keine Abfolge — die Quelle führt weder Bedingungen noch Alternativen. Das Kästchen am Schritt nennt links die eigene Sicht: **←** empfängt sie, **→** sendet sie. Zugeklappte Schritte laufen zwischen anderen Marktpartnern.*

Die Konnektortabelle führt für diese Schritte keinen Schreibaufruf. Abgeleitet aus dem Prozessverlauf: Mit ihrer Nachricht beginnt der Prozess für die eigene Rolle, der Vorgang entsteht also neu.

Betrifft: [1](#schritt-1)

Die Konnektortabelle führt für diese Schritte keinen Schreibaufruf. Abgeleitet aus dem Prozessverlauf: Die eigene Rolle war an diesem Prozess schon beteiligt, der Vorgang besteht also.

Betrifft: [3](#schritt-3), [5](#schritt-5)

Zu den Prüfidentifikatoren dieser Schritte liegt kein Testfall im Testbestand; der Knopf »Ausprobieren« der schreibenden Schnittstelle bietet deshalb keinen Rumpf an.

Betrifft: [1](#schritt-1), [3](#schritt-3), [5](#schritt-5)

</Hinweisbereich>
