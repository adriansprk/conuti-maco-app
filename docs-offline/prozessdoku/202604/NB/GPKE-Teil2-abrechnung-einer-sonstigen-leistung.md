# Abrechnung einer sonstigen Leistung — Sicht NB

<Kopf rolle="NB" beteiligter="NB" festlegung="GPKE" dokument="GPKE Teil 2" kapitel="3.4.5.2" sparte="Strom" schritte={6} suchtitel="Abrechnung einer sonstigen Leistung — Sicht NB · GPKE Teil 2 · Formatversion 202604" abschnitte={[{"id": "abschnitt-ablauf", "label": "Prozessablauf"}, {"id": "abschnitt-schritte", "label": "Prozessschritte"}, {"id": "abschnitt-informationen", "label": "Prozess-Informationen"}, {"id": "abschnitt-sichten", "label": "Andere Sichten des Prozesses"}]} />

<Kurzfassung>

Der Prozess beschreibt die Kommunikation zwischen NB und LF zur Abrechnung einer sonstigen Leistung, die in den Preisblättern Sperrkosten, Verzugskosten oder Blindarbeit des NB enthalten ist und ggf. den automatisierten Reklamationsfall. Eine Rechnungskorrektur umfasst immer eine Stornorechnung und eine neue Rechnung.

</Kurzfassung>

<a id="abschnitt-ablauf"></a>

## Prozessablauf aus Sicht des NB

<Systembild svg={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1004 992\" width=\"1004\" height=\"992\" role=\"img\" aria-labelledby=\"sb-title\" class=\"maco-systembild\">\n<title id=\"sb-title\">Systembild: Abrechnung einer sonstigen Leistung aus Sicht NB</title>\n<defs><marker id=\"sb-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect class=\"sb-lane-kopf\" x=\"16\" y=\"12\" width=\"232\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend-System des Kunden</text>\n<rect class=\"sb-lane-kopf\" x=\"398\" y=\"12\" width=\"264\" height=\"46\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · NB</text>\n<rect class=\"sb-lane-kopf\" x=\"812\" y=\"12\" width=\"176\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"900\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Marktpartner</text>\n<line x1=\"323\" y1=\"58\" x2=\"323\" y2=\"980\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"737\" y1=\"58\" x2=\"737\" y2=\"980\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"80\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">1. Rechnung einer sonstigen</text>\n<text x=\"530\" y=\"115\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Leistung</text>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"86\" r=\"5\"/><line x1=\"900\" y1=\"91\" x2=\"900\" y2=\"103\"/><line x1=\"893\" y1=\"95\" x2=\"907\" y2=\"95\"/><line x1=\"900\" y1=\"103\" x2=\"894\" y2=\"113\"/><line x1=\"900\" y1=\"103\" x2=\"906\" y2=\"113\"/></g>\n<text x=\"900\" y=\"135\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">LF</text>\n<line x1=\"628\" y1=\"104\" x2=\"878\" y2=\"104\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"96\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"120\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">31011</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"163\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"183\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"128\" x2=\"530\" y2=\"163\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"163\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"183\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"179\" x2=\"230\" y2=\"179\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"171\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"227\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"247\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">2. Antwort</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"196\" x2=\"530\" y2=\"227\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"225\" r=\"5\"/><line x1=\"900\" y1=\"230\" x2=\"900\" y2=\"242\"/><line x1=\"893\" y1=\"234\" x2=\"907\" y2=\"234\"/><line x1=\"900\" y1=\"242\" x2=\"894\" y2=\"252\"/><line x1=\"900\" y1=\"242\" x2=\"906\" y2=\"252\"/></g>\n<text x=\"900\" y=\"274\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">LF</text>\n<line x1=\"878\" y1=\"243\" x2=\"628\" y2=\"243\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"235\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"259\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">33001, 33002</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"310\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"330\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"260\" x2=\"530\" y2=\"310\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben sb-abgeleitet\" x=\"34\" y=\"310\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"330\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"326\" x2=\"230\" y2=\"326\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"318\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"374\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"394\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">3. Mitteilung, dass die</text>\n<text x=\"530\" y=\"409\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">ursprüngliche Rechnung</text>\n<text x=\"530\" y=\"424\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">einer sonstigen…</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"343\" x2=\"530\" y2=\"374\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"387\" r=\"5\"/><line x1=\"900\" y1=\"392\" x2=\"900\" y2=\"404\"/><line x1=\"893\" y1=\"396\" x2=\"907\" y2=\"396\"/><line x1=\"900\" y1=\"404\" x2=\"894\" y2=\"414\"/><line x1=\"900\" y1=\"404\" x2=\"906\" y2=\"414\"/></g>\n<text x=\"900\" y=\"436\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">LF</text>\n<line x1=\"628\" y1=\"405\" x2=\"878\" y2=\"405\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"397\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"421\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">29001</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"463\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"483\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"437\" x2=\"530\" y2=\"463\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"463\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"483\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"479\" x2=\"230\" y2=\"479\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"471\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"527\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"547\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">4. Antwort</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"496\" x2=\"530\" y2=\"527\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"525\" r=\"5\"/><line x1=\"900\" y1=\"530\" x2=\"900\" y2=\"542\"/><line x1=\"893\" y1=\"534\" x2=\"907\" y2=\"534\"/><line x1=\"900\" y1=\"542\" x2=\"894\" y2=\"552\"/><line x1=\"900\" y1=\"542\" x2=\"906\" y2=\"552\"/></g>\n<text x=\"900\" y=\"574\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">LF</text>\n<line x1=\"878\" y1=\"543\" x2=\"628\" y2=\"543\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"535\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"559\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">33002, 33001</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"610\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"630\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"560\" x2=\"530\" y2=\"610\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben sb-abgeleitet\" x=\"34\" y=\"610\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"630\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"626\" x2=\"230\" y2=\"626\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"618\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"674\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"694\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">5. Storno der ursprünglichen</text>\n<text x=\"530\" y=\"709\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Rechnung</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"643\" x2=\"530\" y2=\"674\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"680\" r=\"5\"/><line x1=\"900\" y1=\"685\" x2=\"900\" y2=\"697\"/><line x1=\"893\" y1=\"689\" x2=\"907\" y2=\"689\"/><line x1=\"900\" y1=\"697\" x2=\"894\" y2=\"707\"/><line x1=\"900\" y1=\"697\" x2=\"906\" y2=\"707\"/></g>\n<text x=\"900\" y=\"729\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">LF</text>\n<line x1=\"628\" y1=\"698\" x2=\"878\" y2=\"698\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"690\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"714\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">31004</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"757\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"777\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"722\" x2=\"530\" y2=\"757\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"757\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"777\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"773\" x2=\"230\" y2=\"773\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"765\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"821\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"841\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">6. Antwort</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"790\" x2=\"530\" y2=\"821\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"819\" r=\"5\"/><line x1=\"900\" y1=\"824\" x2=\"900\" y2=\"836\"/><line x1=\"893\" y1=\"828\" x2=\"907\" y2=\"828\"/><line x1=\"900\" y1=\"836\" x2=\"894\" y2=\"846\"/><line x1=\"900\" y1=\"836\" x2=\"906\" y2=\"846\"/></g>\n<text x=\"900\" y=\"868\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">LF</text>\n<line x1=\"878\" y1=\"837\" x2=\"628\" y2=\"837\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"829\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"853\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">33001, 33002</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"904\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"924\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"854\" x2=\"530\" y2=\"904\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben sb-abgeleitet\" x=\"34\" y=\"904\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"924\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"920\" x2=\"230\" y2=\"920\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"912\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n</svg>"} gesamt={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 730 858\" width=\"730\" height=\"858\" role=\"img\" aria-labelledby=\"sd-title\" class=\"maco-sequence\">\n<title id=\"sd-title\">Sequenzdiagramm: Abrechnung einer sonstigen Leistung aus Sicht NB</title>\n<defs><marker id=\"sd-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect x=\"16\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"121\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend (Kunde)</text>\n<line x1=\"121\" y1=\"64\" x2=\"121\" y2=\"846\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"260\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"365\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · NB</text>\n<line x1=\"365\" y1=\"64\" x2=\"365\" y2=\"846\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"504\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"609\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">LF</text>\n<line x1=\"609\" y1=\"64\" x2=\"609\" y2=\"846\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"365\" y1=\"90\" x2=\"609\" y2=\"90\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"81\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">1. Rechnung einer sonstigen Leistung</text>\n<text x=\"487\" y=\"105\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 31011</text>\n<line x1=\"365\" y1=\"152\" x2=\"121\" y2=\"152\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"143\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"167\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"609\" y1=\"214\" x2=\"365\" y2=\"214\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"205\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">2. Antwort</text>\n<text x=\"487\" y=\"229\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 33001, 33002 · E_0503</text>\n<text x=\"487\" y=\"242\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0503 — Rechnung einer sonstigen Leistung prüfen</text>\n<line x1=\"365\" y1=\"276\" x2=\"121\" y2=\"276\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"267\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"291\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"365\" y1=\"338\" x2=\"609\" y2=\"338\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"329\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">3. Mitteilung, dass die ursprüngliche Rechnung e…</text>\n<text x=\"487\" y=\"353\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 29001 · E_0504</text>\n<text x=\"487\" y=\"366\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0504 — Nicht-Zahlungsavis prüfen</text>\n<line x1=\"365\" y1=\"400\" x2=\"121\" y2=\"400\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"391\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"415\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"609\" y1=\"462\" x2=\"365\" y2=\"462\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"453\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">4. Antwort</text>\n<text x=\"487\" y=\"477\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 33002, 33001 · E_0505</text>\n<text x=\"487\" y=\"490\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0505 — erneut Rechnung einer sonstigen Leistung prüfen</text>\n<line x1=\"365\" y1=\"524\" x2=\"121\" y2=\"524\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"515\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"539\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"365\" y1=\"586\" x2=\"609\" y2=\"586\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"577\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">5. Storno der ursprünglichen Rechnung</text>\n<text x=\"487\" y=\"601\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 31004</text>\n<line x1=\"365\" y1=\"648\" x2=\"121\" y2=\"648\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"639\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"663\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"609\" y1=\"710\" x2=\"365\" y2=\"710\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"701\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">6. Antwort</text>\n<text x=\"487\" y=\"725\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 33001, 33002 · E_0506</text>\n<text x=\"487\" y=\"738\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0506 — Prüfen, ob Antwort auf Stornierung erforderlich</text>\n<line x1=\"365\" y1=\"772\" x2=\"121\" y2=\"772\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"763\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"787\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n</svg>"} titel="NB" />

<a id="abschnitt-schritte"></a>

## Prozessschritte

<Schritt nr="1" anker="schritt-1" richtung="ausgehend" kopf={{"links": {"label": "NB", "eigen": true}, "rechts": {"label": "LF"}}}>

### Rechnung einer sonstigen Leistung

<Schrittskizze sicht={{"label": "NB"}} zeilen={[{"art": "senden", "label": "LF", "weg": "AS4", "nachrichten": [{"nr": "31011", "titel": "Rechnung sonstige Leistung"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [31011](/schnittstellen/202604/pruefi/INVOIC/PI_31011) — Rechnung sonstige Leistung · AS4

</div>

**Ablauf**

<div data-ablauf data-offen="ja">

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht an **LF** · AS4

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

<Schritt nr="2" anker="schritt-2" richtung="eingehend" kopf={{"links": {"label": "NB", "eigen": true}, "rechts": {"label": "LF"}}}>

### Antwort

<Schrittskizze sicht={{"label": "NB"}} zeilen={[{"art": "empfangen", "label": "LF", "weg": "AS4", "nachrichten": [{"nr": "33001", "titel": "Bestätigung"}, {"nr": "33002", "titel": "Abweisung"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [33001](/schnittstellen/202604/pruefi/REMADV/PI_33001) — Bestätigung · AS4
- [33002](/schnittstellen/202604/pruefi/REMADV/PI_33002) — Abweisung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **LF** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `33002` → [E_0503](/referenz/202604/ebd/E_0503) · LF · Rechnung einer sonstigen Leistung prüfen

</div>

</li>

<li data-teil="schnittstelle" data-art="fortschreiben" data-abgeleitet="ja">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202604/backend-schreiben-nb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"AVIS\": [\n      {\n        \"avisNummer\": \"BGM555555\",\n        \"avisTyp\": \"ZAHLUNGSAVIS\",\n        \"boTyp\": \"AVIS\",\n        \"positionen\": [\n          {\n            \"gesamtBrutto\": {\n              \"waehrung\": \"EUR\",\n              \"wert\": 5000\n            },\n            \"istSelbstausgestellt\": false,\n            \"istStorno\": false,\n            \"rechnungsDatum\": \"2024-03-15T12:00:00Z\",\n            \"rechnungsNummer\": \"BGM56151515\",\n            \"zuZahlen\": {\n              \"waehrung\": \"EUR\",\n              \"wert\": 5000\n            }\n          }\n        ],\n        \"versionStruktur\": \"1\",\n        \"zuZahlen\": {\n          \"waehrung\": \"EUR\",\n          \"wert\": 5000\n        }\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9903790000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"datenaustauschreferenz\": \"197691\",\n    \"dokumentennummer\": \"BGM555555\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9900321000005\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"481\",\n    \"nachrichtendatum\": \"2024-04-03T12:00:00Z\",\n    \"nachrichtenreferenznummer\": \"617415\",\n    \"pruefidentifikator\": \"33001\",\n    \"sparte\": \"STROM\"\n  },\n  \"zusatzdaten\": {}\n}"} examples={[{"mediaType": "application/json", "examples": [{"name": "33001", "summary": "33001 — Bestätigung", "value": {"stammdaten": {"AVIS": [{"boTyp": "AVIS", "versionStruktur": "1", "avisNummer": "BGM555555", "avisTyp": "ZAHLUNGSAVIS", "positionen": [{"zuZahlen": {"wert": 5000, "waehrung": "EUR"}, "gesamtBrutto": {"wert": 5000, "waehrung": "EUR"}, "rechnungsNummer": "BGM56151515", "rechnungsDatum": "2024-03-15T12:00:00Z", "istStorno": false, "istSelbstausgestellt": false}], "zuZahlen": {"wert": 5000, "waehrung": "EUR"}}]}, "transaktionsdaten": {"datenaustauschreferenz": "197691", "sparte": "STROM", "pruefidentifikator": "33001", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9903790000002", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900321000005", "rollencodetyp": "BDEW"}, "dokumentennummer": "BGM555555", "kategorie": "481", "nachrichtendatum": "2024-04-03T12:00:00Z", "nachrichtenreferenznummer": "617415"}, "zusatzdaten": {}}}, {"name": "33002", "summary": "33002 — Abweisung", "value": {"stammdaten": {"AVIS": [{"boTyp": "AVIS", "versionStruktur": "1", "avisNummer": "BGM12345", "avisTyp": "ABGELEHNTE_FORDERUNG", "positionen": [{"zuZahlen": {"wert": 5000, "waehrung": "EUR"}, "gesamtBrutto": {"wert": 0, "waehrung": "EUR"}, "abweichung": [{"abweichungsgrundBemerkung1": "Rechnung entspricht nicht §14 UstG", "abweichungsgrundCodeliste": "E_0503", "abweichungsgrundCode": "A01"}, {"abweichungsgrundCodeliste": "E_0506", "abweichungsgrundCode": "A04"}], "rechnungsNummer": "BGM111111111", "rechnungsDatum": "2024-03-01T12:00:00Z", "istStorno": false, "istSelbstausgestellt": false, "referenz": "ABC123456"}, {"zuZahlen": {"wert": 7000, "waehrung": "EUR"}, "gesamtBrutto": {"wert": 0, "waehrung": "EUR"}, "abweichung": [{"abweichungsgrundBemerkung1": "Blabla", "abweichungsgrundCodeliste": "E_0503", "abweichungsgrundCode": "A01"}], "rechnungsNummer": "BGM235555", "rechnungsDatum": "2024-03-01T12:00:00Z", "istStorno": false, "istSelbstausgestellt": false}], "zuZahlen": {"wert": 0, "waehrung": "EUR"}}]}, "transaktionsdaten": {"datenaustauschreferenz": "166216", "sparte": "STROM", "pruefidentifikator": "33002", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9903790000002", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900321000005", "rollencodetyp": "BDEW"}, "dokumentennummer": "BGM12345", "kategorie": "239", "nachrichtendatum": "2024-04-03T11:48:00Z", "nachrichtenreferenznummer": "494930", "vorgangsreferenznummer": "ABC123456"}, "zusatzdaten": {}}}]}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend mit den Daten der eingegangenen Nachricht fort.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="3" anker="schritt-3" richtung="ausgehend" kopf={{"links": {"label": "NB", "eigen": true}, "rechts": {"label": "LF"}}}>

### Mitteilung, dass die ursprüngliche Rechnung einer sonstigen Leistung korrekt war

<Schrittskizze sicht={{"label": "NB"}} zeilen={[{"art": "senden", "label": "LF", "weg": "AS4", "nachrichten": [{"nr": "29001", "titel": "Ablehnung REMADV"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [29001](/schnittstellen/202604/pruefi/COMDIS/PI_29001) — Ablehnung REMADV · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht an **LF** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `29001` → [E_0504](/referenz/202604/ebd/E_0504) · NB · Nicht-Zahlungsavis prüfen

</div>

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202604/backend-schreiben-nb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"HANDELSUNSTIMMIGKEIT\": [\n      {\n        \"begruendung\": {\n          \"grund\": \"SONSTIGES\",\n          \"hinweis\": \"BLABLA\"\n        },\n        \"boTyp\": \"HANDELSUNSTIMMIGKEIT\",\n        \"nummer\": \"ABC123456\",\n        \"typ\": \"HANDELSRECHNUNG\",\n        \"versionStruktur\": \"1\",\n        \"zuZahlen\": {\n          \"waehrung\": \"EUR\",\n          \"wert\": 10000\n        }\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"ansprechpartner\": {\n        \"boTyp\": \"ANSPRECHPARTNER\",\n        \"eMailAdresse\": \"x@x.de\",\n        \"nachname\": \"Max Mustermann\",\n        \"versionStruktur\": \"1\"\n      },\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9900321000005\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"antwortstatusCodeliste\": \"S_0109\",\n    \"datenaustauschreferenz\": \"115436\",\n    \"dokumentennummer\": \"272460BGM\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9903790000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"456\",\n    \"nachrichtendatum\": \"2024-04-03T13:21:00Z\",\n    \"nachrichtenreferenznummer\": \"272460\",\n    \"pruefidentifikator\": \"29001\",\n    \"sparte\": \"STROM\"\n  },\n  \"zusatzdaten\": {}\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend fort, nachdem die Nachricht erstellt ist.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="4" anker="schritt-4" richtung="eingehend" kopf={{"links": {"label": "NB", "eigen": true}, "rechts": {"label": "LF"}}}>

### Antwort

<Schrittskizze sicht={{"label": "NB"}} zeilen={[{"art": "empfangen", "label": "LF", "weg": "AS4", "nachrichten": [{"nr": "33002", "titel": "Abweisung"}, {"nr": "33001", "titel": "Bestätigung"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [33002](/schnittstellen/202604/pruefi/REMADV/PI_33002) — Abweisung · AS4
- [33001](/schnittstellen/202604/pruefi/REMADV/PI_33001) — Bestätigung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **LF** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `33002` → [E_0505](/referenz/202604/ebd/E_0505) · LF · erneut Rechnung einer sonstigen Leistung prüfen

</div>

</li>

<li data-teil="schnittstelle" data-art="fortschreiben" data-abgeleitet="ja">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202604/backend-schreiben-nb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"AVIS\": [\n      {\n        \"avisNummer\": \"BGM12345\",\n        \"avisTyp\": \"ABGELEHNTE_FORDERUNG\",\n        \"boTyp\": \"AVIS\",\n        \"positionen\": [\n          {\n            \"abweichung\": [\n              {\n                \"abweichungsgrundBemerkung1\": \"Rechnung entspricht nicht §14 UstG\",\n                \"abweichungsgrundCode\": \"A01\",\n                \"abweichungsgrundCodeliste\": \"E_0503\"\n              },\n              {\n                \"abweichungsgrundCode\": \"A04\",\n                \"abweichungsgrundCodeliste\": \"E_0506\"\n              }\n            ],\n            \"gesamtBrutto\": {\n              \"waehrung\": \"EUR\",\n              \"wert\": 0\n            },\n            \"istSelbstausgestellt\": false,\n            \"istStorno\": false,\n            \"rechnungsDatum\": \"2024-03-01T12:00:00Z\",\n            \"rechnungsNummer\": \"BGM111111111\",\n            \"referenz\": \"ABC123456\",\n            \"zuZahlen\": {\n              \"waehrung\": \"EUR\",\n              \"wert\": 5000\n            }\n          },\n          {\n            \"abweichung\": [\n              {\n                \"abweichungsgrundBemerkung1\": \"Blabla\",\n                \"abweichungsgrundCode\": \"A01\",\n                \"abweichungsgrundCodeliste\": \"E_0503\"\n              }\n            ],\n            \"gesamtBrutto\": {\n              \"waehrung\": \"EUR\",\n              \"wert\": 0\n            },\n            \"istSelbstausgestellt\": false,\n            \"istStorno\": false,\n            \"rechnungsDatum\": \"2024-03-01T12:00:00Z\",\n            \"rechnungsNummer\": \"BGM235555\",\n            \"zuZahlen\": {\n              \"waehrung\": \"EUR\",\n              \"wert\": 7000\n            }\n          }\n        ],\n        \"versionStruktur\": \"1\",\n        \"zuZahlen\": {\n          \"waehrung\": \"EUR\",\n          \"wert\": 0\n        }\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9903790000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"datenaustauschreferenz\": \"166216\",\n    \"dokumentennummer\": \"BGM12345\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9900321000005\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"239\",\n    \"nachrichtendatum\": \"2024-04-03T11:48:00Z\",\n    \"nachrichtenreferenznummer\": \"494930\",\n    \"pruefidentifikator\": \"33002\",\n    \"sparte\": \"STROM\",\n    \"vorgangsreferenznummer\": \"ABC123456\"\n  },\n  \"zusatzdaten\": {}\n}"} examples={[{"mediaType": "application/json", "examples": [{"name": "33002", "summary": "33002 — Abweisung", "value": {"stammdaten": {"AVIS": [{"boTyp": "AVIS", "versionStruktur": "1", "avisNummer": "BGM12345", "avisTyp": "ABGELEHNTE_FORDERUNG", "positionen": [{"zuZahlen": {"wert": 5000, "waehrung": "EUR"}, "gesamtBrutto": {"wert": 0, "waehrung": "EUR"}, "abweichung": [{"abweichungsgrundBemerkung1": "Rechnung entspricht nicht §14 UstG", "abweichungsgrundCodeliste": "E_0503", "abweichungsgrundCode": "A01"}, {"abweichungsgrundCodeliste": "E_0506", "abweichungsgrundCode": "A04"}], "rechnungsNummer": "BGM111111111", "rechnungsDatum": "2024-03-01T12:00:00Z", "istStorno": false, "istSelbstausgestellt": false, "referenz": "ABC123456"}, {"zuZahlen": {"wert": 7000, "waehrung": "EUR"}, "gesamtBrutto": {"wert": 0, "waehrung": "EUR"}, "abweichung": [{"abweichungsgrundBemerkung1": "Blabla", "abweichungsgrundCodeliste": "E_0503", "abweichungsgrundCode": "A01"}], "rechnungsNummer": "BGM235555", "rechnungsDatum": "2024-03-01T12:00:00Z", "istStorno": false, "istSelbstausgestellt": false}], "zuZahlen": {"wert": 0, "waehrung": "EUR"}}]}, "transaktionsdaten": {"datenaustauschreferenz": "166216", "sparte": "STROM", "pruefidentifikator": "33002", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9903790000002", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900321000005", "rollencodetyp": "BDEW"}, "dokumentennummer": "BGM12345", "kategorie": "239", "nachrichtendatum": "2024-04-03T11:48:00Z", "nachrichtenreferenznummer": "494930", "vorgangsreferenznummer": "ABC123456"}, "zusatzdaten": {}}}, {"name": "33001", "summary": "33001 — Bestätigung", "value": {"stammdaten": {"AVIS": [{"boTyp": "AVIS", "versionStruktur": "1", "avisNummer": "BGM555555", "avisTyp": "ZAHLUNGSAVIS", "positionen": [{"zuZahlen": {"wert": 5000, "waehrung": "EUR"}, "gesamtBrutto": {"wert": 5000, "waehrung": "EUR"}, "rechnungsNummer": "BGM56151515", "rechnungsDatum": "2024-03-15T12:00:00Z", "istStorno": false, "istSelbstausgestellt": false}], "zuZahlen": {"wert": 5000, "waehrung": "EUR"}}]}, "transaktionsdaten": {"datenaustauschreferenz": "197691", "sparte": "STROM", "pruefidentifikator": "33001", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9903790000002", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900321000005", "rollencodetyp": "BDEW"}, "dokumentennummer": "BGM555555", "kategorie": "481", "nachrichtendatum": "2024-04-03T12:00:00Z", "nachrichtenreferenznummer": "617415"}, "zusatzdaten": {}}}]}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend mit den Daten der eingegangenen Nachricht fort.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="5" anker="schritt-5" richtung="ausgehend" kopf={{"links": {"label": "NB", "eigen": true}, "rechts": {"label": "LF"}}}>

### Storno der ursprünglichen Rechnung

<Schrittskizze sicht={{"label": "NB"}} zeilen={[{"art": "senden", "label": "LF", "weg": "AS4", "nachrichten": [{"nr": "31004", "titel": "Stornorechnung"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [31004](/schnittstellen/202604/pruefi/INVOIC/PI_31004) — Stornorechnung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht an **LF** · AS4

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

<Schritt nr="6" anker="schritt-6" richtung="eingehend" kopf={{"links": {"label": "NB", "eigen": true}, "rechts": {"label": "LF"}}}>

### Antwort

<Schrittskizze sicht={{"label": "NB"}} zeilen={[{"art": "empfangen", "label": "LF", "weg": "AS4", "nachrichten": [{"nr": "33001", "titel": "Bestätigung"}, {"nr": "33002", "titel": "Abweisung"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [33001](/schnittstellen/202604/pruefi/REMADV/PI_33001) — Bestätigung · AS4
- [33002](/schnittstellen/202604/pruefi/REMADV/PI_33002) — Abweisung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **LF** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `33002` → [E_0506](/referenz/202604/ebd/E_0506) · LF · Prüfen, ob Antwort auf Stornierung erforderlich

</div>

</li>

<li data-teil="schnittstelle" data-art="fortschreiben" data-abgeleitet="ja">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202604/backend-schreiben-nb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"AVIS\": [\n      {\n        \"avisNummer\": \"BGM555555\",\n        \"avisTyp\": \"ZAHLUNGSAVIS\",\n        \"boTyp\": \"AVIS\",\n        \"positionen\": [\n          {\n            \"gesamtBrutto\": {\n              \"waehrung\": \"EUR\",\n              \"wert\": 5000\n            },\n            \"istSelbstausgestellt\": false,\n            \"istStorno\": false,\n            \"rechnungsDatum\": \"2024-03-15T12:00:00Z\",\n            \"rechnungsNummer\": \"BGM56151515\",\n            \"zuZahlen\": {\n              \"waehrung\": \"EUR\",\n              \"wert\": 5000\n            }\n          }\n        ],\n        \"versionStruktur\": \"1\",\n        \"zuZahlen\": {\n          \"waehrung\": \"EUR\",\n          \"wert\": 5000\n        }\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9903790000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"datenaustauschreferenz\": \"197691\",\n    \"dokumentennummer\": \"BGM555555\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9900321000005\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"481\",\n    \"nachrichtendatum\": \"2024-04-03T12:00:00Z\",\n    \"nachrichtenreferenznummer\": \"617415\",\n    \"pruefidentifikator\": \"33001\",\n    \"sparte\": \"STROM\"\n  },\n  \"zusatzdaten\": {}\n}"} examples={[{"mediaType": "application/json", "examples": [{"name": "33001", "summary": "33001 — Bestätigung", "value": {"stammdaten": {"AVIS": [{"boTyp": "AVIS", "versionStruktur": "1", "avisNummer": "BGM555555", "avisTyp": "ZAHLUNGSAVIS", "positionen": [{"zuZahlen": {"wert": 5000, "waehrung": "EUR"}, "gesamtBrutto": {"wert": 5000, "waehrung": "EUR"}, "rechnungsNummer": "BGM56151515", "rechnungsDatum": "2024-03-15T12:00:00Z", "istStorno": false, "istSelbstausgestellt": false}], "zuZahlen": {"wert": 5000, "waehrung": "EUR"}}]}, "transaktionsdaten": {"datenaustauschreferenz": "197691", "sparte": "STROM", "pruefidentifikator": "33001", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9903790000002", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900321000005", "rollencodetyp": "BDEW"}, "dokumentennummer": "BGM555555", "kategorie": "481", "nachrichtendatum": "2024-04-03T12:00:00Z", "nachrichtenreferenznummer": "617415"}, "zusatzdaten": {}}}, {"name": "33002", "summary": "33002 — Abweisung", "value": {"stammdaten": {"AVIS": [{"boTyp": "AVIS", "versionStruktur": "1", "avisNummer": "BGM12345", "avisTyp": "ABGELEHNTE_FORDERUNG", "positionen": [{"zuZahlen": {"wert": 5000, "waehrung": "EUR"}, "gesamtBrutto": {"wert": 0, "waehrung": "EUR"}, "abweichung": [{"abweichungsgrundBemerkung1": "Rechnung entspricht nicht §14 UstG", "abweichungsgrundCodeliste": "E_0503", "abweichungsgrundCode": "A01"}, {"abweichungsgrundCodeliste": "E_0506", "abweichungsgrundCode": "A04"}], "rechnungsNummer": "BGM111111111", "rechnungsDatum": "2024-03-01T12:00:00Z", "istStorno": false, "istSelbstausgestellt": false, "referenz": "ABC123456"}, {"zuZahlen": {"wert": 7000, "waehrung": "EUR"}, "gesamtBrutto": {"wert": 0, "waehrung": "EUR"}, "abweichung": [{"abweichungsgrundBemerkung1": "Blabla", "abweichungsgrundCodeliste": "E_0503", "abweichungsgrundCode": "A01"}], "rechnungsNummer": "BGM235555", "rechnungsDatum": "2024-03-01T12:00:00Z", "istStorno": false, "istSelbstausgestellt": false}], "zuZahlen": {"wert": 0, "waehrung": "EUR"}}]}, "transaktionsdaten": {"datenaustauschreferenz": "166216", "sparte": "STROM", "pruefidentifikator": "33002", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9903790000002", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900321000005", "rollencodetyp": "BDEW"}, "dokumentennummer": "BGM12345", "kategorie": "239", "nachrichtendatum": "2024-04-03T11:48:00Z", "nachrichtenreferenznummer": "494930", "vorgangsreferenznummer": "ABC123456"}, "zusatzdaten": {}}}]}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

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
| [E_0503](/referenz/202604/ebd/E_0503) | Rechnung einer sonstigen Leistung prüfen |
| [E_0504](/referenz/202604/ebd/E_0504) | Nicht-Zahlungsavis prüfen |
| [E_0505](/referenz/202604/ebd/E_0505) | erneut Rechnung einer sonstigen Leistung prüfen |
| [E_0506](/referenz/202604/ebd/E_0506) | Prüfen, ob Antwort auf Stornierung erforderlich |

</details>

<a id="abschnitt-informationen"></a>

## Prozess-Informationen

Wortlaut der Lesefassung, Steckbrief Kap. 3.4.5.1, S. 98–99.

<Stepper>
<ol>

<li data-blatt="vorbedingungen">

### Vorbedingungen

- Die aktuellen Entgelte für sonstige Leistungen (Preisblätter Sperrkosten, Verzugskosten und Blindarbeit) wurden vom NB im Rahmen des Use Cases „[Übermittlung Preisblatt NB an LF](/prozessdoku/202604/NB/GPKE-Teil2-uebermittlung-preisblatt-nb-an-lf)“ an den LF übermittelt.
- Eine sonstige Leistung ist mit einer der Artikel-ID der Preisblätter Sperrkosten, Verzugskosten oder Blindarbeit des NB abbildbar.

</li>

<li data-blatt="ergebnisse">

### Ergebnisse

Der LF wird die vom NB gestellte Rechnung der sonstigen Leistung bezahlen.

</li>

<li data-blatt="fehlerfall">

### Fehlerfall

#### Fehlerfälle

- Die Rechnung enthält Positionen, die nicht als Artikel-ID in einem der Preisblätter Sperrkosten, Verzugskosten oder Blindarbeit des NB enthalten sind.
- Der in der Rechnung angegebene Preis einer Artikel-ID entspricht nicht dem im relevanten Preisblatt angegebenen Preis der entsprechenden Artikel-ID.

</li>

<li data-blatt="anforderungen">

### Weitere Anforderungen

- Der Fall einer reklamierten oder sich als falsch erweisenden Rechnung der sonstigen Leistung (Storno der ursprünglichen Rechnung wird ohne vorherige Reklamation des LF oder auf Grund einer vorherigen Reklamation des LF durchgeführt) stellt einen Teil des Regelprozesses dar und muss abgesehen von Klärungen vollumfänglich automatisch abgewickelt werden. Im Reklamationsfall kommt das sog. „Alles-oder-Nichts-Prinzip“ zur Anwendung, nach dem eine Rechnung entweder vollumfänglich als richtig akzeptiert oder vollumfänglich abgelehnt wird. Die im Konfliktfall abzuwickelnden Prozesse im Rahmen des Forderungsmanagements bzw. Mahnablaufs sind nicht dargestellt und sind bilateral zu lösen.
- Eine Rechnung im Rahmen der Unterbrechung und Wiederherstellung der Anschlussnutzung referenziert auf den zugrundeliegenden Sperrauftrag.
- Über den Use-Case „Abrechnung einer sonstigen Leistung“ können Verzugskosten,
  - die im Zusammenhang mit einer Netznutzungsrechnung entstanden sind,
  - als auch im Zusammenhang mit einer Rechnung einer sonstigen Leistung entstanden sind, in Rechnung gestellt werden. Eine eindeutige Referenz auf die zugrundeliegende Rechnung ist anzugeben.
- Ist der Letztverbraucher selbst Netznutzer (= Netznutzer ohne All-Inklusiv-Vertrag), so tritt er in die Rolle des LF i. S. dieser Prozessbeschreibung, soweit diese Regelungen sinngemäß auf ihn anwendbar sind.

</li>

<li data-blatt="anlass">

### Anlass

- Eine sonstige Leistung wurde über den Use-Case „[Unterbrechung der Anschlussnutzung (Sperren) auf Anweisung des LF](/prozessdoku/202604/NB/GPKE-Teil2-unterbrechung-der-anschlussnutzung-sperren-auf-anweisung-des-lf)“ beauftragt oder
- es sind bei dem NB Verzugskosten entstanden oder
- der LF übernimmt freiwillig die Abrechnung der Artikel-ID Blindarbeit gegenüber dem AN.

</li>

<li data-blatt="erste-nachricht">

### Erste Nachricht

Der Beteiligte dieser Seite sendet selbst: „Rechnung einer sonstigen Leistung“ an **LF** (Schritt 1).

</li>

<li data-blatt="ziel">

### Ziel

Der NB ist informiert, dass der LF die Rechnung der sonstigen Leistung akzeptiert.

</li>

</ol>
</Stepper>

<a id="abschnitt-sichten"></a>

## Andere Sichten des Prozesses

Derselbe Prozess, aus den Augen der anderen Beteiligten: dieselben Schritte, jeweils aus deren Sicht gelesen.

- [Sicht LF](/prozessdoku/202604/LF/GPKE-Teil2-abrechnung-einer-sonstigen-leistung) — LF

<Hinweisbereich>

*Die Schritte sind die **möglichen** Nachrichten dieses Prozesses, keine Abfolge — die Quelle führt weder Bedingungen noch Alternativen. Das Kästchen am Schritt nennt links die eigene Sicht: **←** empfängt sie, **→** sendet sie. Zugeklappte Schritte laufen zwischen anderen Marktpartnern.*

Welches Ereignis diese Schritte anstößt, benennt die Quelle noch nicht.

Betrifft: [1](#schritt-1)

Die Konnektortabelle führt für diese Schritte keinen Schreibaufruf. Abgeleitet aus dem Prozessverlauf: Die eigene Rolle war an diesem Prozess schon beteiligt, der Vorgang besteht also.

Betrifft: [2](#schritt-2), [4](#schritt-4), [6](#schritt-6)

Zu den Prüfidentifikatoren dieser Schritte liegt kein Testfall im Testbestand; der Knopf »Ausprobieren« der schreibenden Schnittstelle bietet deshalb keinen Rumpf an.

Betrifft: [1](#schritt-1), [5](#schritt-5)

</Hinweisbereich>
