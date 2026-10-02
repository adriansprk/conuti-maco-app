# Anfrage und Bestellung von Werten durch den ESA — Sicht ESA

<Kopf rolle="ESA" beteiligter="ESA" festlegung="WiM" dokument="WiM Strom Teil 2" kapitel="4.1.2" sparte="Strom" schritte={6} suchtitel="Anfrage und Bestellung von Werten durch den ESA — Sicht ESA · WiM Strom Teil 2 · Formatversion 202610" abschnitte={[{"id": "abschnitt-ablauf", "label": "Prozessablauf"}, {"id": "abschnitt-schritte", "label": "Prozessschritte"}, {"id": "abschnitt-informationen", "label": "Prozess-Informationen"}, {"id": "abschnitt-sichten", "label": "Andere Sichten des Prozesses"}]} />

<Kurzfassung>

Der ESA fragt die Übermittlung von Werten und die damit verbundenen Kosten beim MSB an. Sofern die Werte in der bestellten Granularität und dem bestellten Umfang durch den MSB (aus dem Back-End-System oder direkt aus dem iMS) zur Verfügung gestellt werden können, erstellt der MSB ein Angebot für diese Übermittlung von Werten, das er dem ESA zur Verfügung stellt. Der ESA kann daraufhin die Übermittlung von Werten bestellen. Möchte der ESA die Werte auf Ebene der Marktlokation erhalten, richtet er seine Anfrage und Bestellung an den MSB der Marktlokation. Möchte der ESA die Werte auf Ebene der Messlokation erhalten, richtet er seine Anfrage und Bestellung an den MSB der Messlokation. Möchte der ESA die Werte auf Ebene der Netzlokation erhalten, richtet er seine Anfrage und Bestellung an den MSB der Netzlokation.

</Kurzfassung>

<a id="abschnitt-ablauf"></a>

## Prozessablauf aus Sicht des ESA

<Systembild svg={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1004 986\" width=\"1004\" height=\"986\" role=\"img\" aria-labelledby=\"sb-title\" class=\"maco-systembild\">\n<title id=\"sb-title\">Systembild: Anfrage und Bestellung von Werten durch den ESA aus Sicht ESA</title>\n<defs><marker id=\"sb-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect class=\"sb-lane-kopf\" x=\"16\" y=\"12\" width=\"232\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend-System des Kunden</text>\n<rect class=\"sb-lane-kopf\" x=\"398\" y=\"12\" width=\"264\" height=\"46\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · ESA</text>\n<rect class=\"sb-lane-kopf\" x=\"812\" y=\"12\" width=\"176\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"900\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Marktpartner</text>\n<line x1=\"323\" y1=\"58\" x2=\"323\" y2=\"974\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"737\" y1=\"58\" x2=\"737\" y2=\"974\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"80\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">1. Anfrage von Werten</text>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"78\" r=\"5\"/><line x1=\"900\" y1=\"83\" x2=\"900\" y2=\"95\"/><line x1=\"893\" y1=\"87\" x2=\"907\" y2=\"87\"/><line x1=\"900\" y1=\"95\" x2=\"894\" y2=\"105\"/><line x1=\"900\" y1=\"95\" x2=\"906\" y2=\"105\"/></g>\n<text x=\"900\" y=\"127\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">MSB</text>\n<line x1=\"628\" y1=\"96\" x2=\"878\" y2=\"96\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"88\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"112\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">35003</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"163\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"183\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"113\" x2=\"530\" y2=\"163\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"163\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"183\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"179\" x2=\"230\" y2=\"179\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"171\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"227\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"247\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">2. Angebot zur / Ablehnung</text>\n<text x=\"530\" y=\"262\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">der Anfrage</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"196\" x2=\"530\" y2=\"227\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"233\" r=\"5\"/><line x1=\"900\" y1=\"238\" x2=\"900\" y2=\"250\"/><line x1=\"893\" y1=\"242\" x2=\"907\" y2=\"242\"/><line x1=\"900\" y1=\"250\" x2=\"894\" y2=\"260\"/><line x1=\"900\" y1=\"250\" x2=\"906\" y2=\"260\"/></g>\n<text x=\"900\" y=\"282\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">MSB</text>\n<line x1=\"878\" y1=\"251\" x2=\"628\" y2=\"251\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"243\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"267\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">15003, 21033</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"310\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"330\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"275\" x2=\"530\" y2=\"310\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben sb-abgeleitet\" x=\"34\" y=\"310\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"330\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"326\" x2=\"230\" y2=\"326\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"318\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"374\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"394\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">3. Bestellung</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"343\" x2=\"530\" y2=\"374\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"372\" r=\"5\"/><line x1=\"900\" y1=\"377\" x2=\"900\" y2=\"389\"/><line x1=\"893\" y1=\"381\" x2=\"907\" y2=\"381\"/><line x1=\"900\" y1=\"389\" x2=\"894\" y2=\"399\"/><line x1=\"900\" y1=\"389\" x2=\"906\" y2=\"399\"/></g>\n<text x=\"900\" y=\"421\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">MSB</text>\n<line x1=\"628\" y1=\"390\" x2=\"878\" y2=\"390\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"382\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"406\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">17007</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"457\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"477\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"407\" x2=\"530\" y2=\"457\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"457\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"477\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"473\" x2=\"230\" y2=\"473\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"465\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"521\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"541\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">4. Antwort auf Bestellung</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"490\" x2=\"530\" y2=\"521\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"519\" r=\"5\"/><line x1=\"900\" y1=\"524\" x2=\"900\" y2=\"536\"/><line x1=\"893\" y1=\"528\" x2=\"907\" y2=\"528\"/><line x1=\"900\" y1=\"536\" x2=\"894\" y2=\"546\"/><line x1=\"900\" y1=\"536\" x2=\"906\" y2=\"546\"/></g>\n<text x=\"900\" y=\"568\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">MSB</text>\n<line x1=\"878\" y1=\"537\" x2=\"628\" y2=\"537\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"529\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"553\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">19011, 19012</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"604\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"624\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"554\" x2=\"530\" y2=\"604\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben sb-abgeleitet\" x=\"34\" y=\"604\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"624\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"620\" x2=\"230\" y2=\"620\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"612\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"668\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"688\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">5. Stornierung einer</text>\n<text x=\"530\" y=\"703\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">bestätigten Bestellung</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"637\" x2=\"530\" y2=\"668\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"674\" r=\"5\"/><line x1=\"900\" y1=\"679\" x2=\"900\" y2=\"691\"/><line x1=\"893\" y1=\"683\" x2=\"907\" y2=\"683\"/><line x1=\"900\" y1=\"691\" x2=\"894\" y2=\"701\"/><line x1=\"900\" y1=\"691\" x2=\"906\" y2=\"701\"/></g>\n<text x=\"900\" y=\"723\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">MSB</text>\n<line x1=\"628\" y1=\"692\" x2=\"878\" y2=\"692\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"684\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"708\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">39002</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"751\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"771\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"716\" x2=\"530\" y2=\"751\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"751\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"771\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"767\" x2=\"230\" y2=\"767\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"759\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"815\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"835\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">6. Antwort auf Stornierung</text>\n<text x=\"530\" y=\"850\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">einer bestätigten Bestellung</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"784\" x2=\"530\" y2=\"815\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"821\" r=\"5\"/><line x1=\"900\" y1=\"826\" x2=\"900\" y2=\"838\"/><line x1=\"893\" y1=\"830\" x2=\"907\" y2=\"830\"/><line x1=\"900\" y1=\"838\" x2=\"894\" y2=\"848\"/><line x1=\"900\" y1=\"838\" x2=\"906\" y2=\"848\"/></g>\n<text x=\"900\" y=\"870\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">MSB</text>\n<line x1=\"878\" y1=\"839\" x2=\"628\" y2=\"839\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"831\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"855\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">19013, 19014</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"898\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"918\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"863\" x2=\"530\" y2=\"898\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben sb-abgeleitet\" x=\"34\" y=\"898\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"918\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"914\" x2=\"230\" y2=\"914\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"906\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n</svg>"} gesamt={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 730 858\" width=\"730\" height=\"858\" role=\"img\" aria-labelledby=\"sd-title\" class=\"maco-sequence\">\n<title id=\"sd-title\">Sequenzdiagramm: Anfrage und Bestellung von Werten durch den ESA aus Sicht ESA</title>\n<defs><marker id=\"sd-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect x=\"16\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"121\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend (Kunde)</text>\n<line x1=\"121\" y1=\"64\" x2=\"121\" y2=\"846\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"260\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"365\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · ESA</text>\n<line x1=\"365\" y1=\"64\" x2=\"365\" y2=\"846\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"504\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"609\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">MSB</text>\n<line x1=\"609\" y1=\"64\" x2=\"609\" y2=\"846\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"365\" y1=\"90\" x2=\"609\" y2=\"90\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"81\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">1. Anfrage von Werten</text>\n<text x=\"487\" y=\"105\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 35003</text>\n<line x1=\"365\" y1=\"152\" x2=\"121\" y2=\"152\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"143\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"167\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"609\" y1=\"214\" x2=\"365\" y2=\"214\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"205\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">2. Angebot zur / Ablehnung der Anfrage</text>\n<text x=\"487\" y=\"229\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 15003, 21033 · E_0252</text>\n<text x=\"487\" y=\"242\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0252 — Anfrage prüfen</text>\n<line x1=\"365\" y1=\"276\" x2=\"121\" y2=\"276\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"267\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"291\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"365\" y1=\"338\" x2=\"609\" y2=\"338\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"329\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">3. Bestellung</text>\n<text x=\"487\" y=\"353\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 17007</text>\n<line x1=\"365\" y1=\"400\" x2=\"121\" y2=\"400\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"391\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"415\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"609\" y1=\"462\" x2=\"365\" y2=\"462\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"453\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">4. Antwort auf Bestellung</text>\n<text x=\"487\" y=\"477\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 19011, 19012 · E_0256</text>\n<text x=\"487\" y=\"490\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0256 — Bestellung prüfen</text>\n<line x1=\"365\" y1=\"524\" x2=\"121\" y2=\"524\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"515\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"539\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"365\" y1=\"586\" x2=\"609\" y2=\"586\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"577\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">5. Stornierung einer bestätigten Bestellung</text>\n<text x=\"487\" y=\"601\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 39002</text>\n<line x1=\"365\" y1=\"648\" x2=\"121\" y2=\"648\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"639\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"663\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"609\" y1=\"710\" x2=\"365\" y2=\"710\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"701\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">6. Antwort auf Stornierung einer bestätigten Bes…</text>\n<text x=\"487\" y=\"725\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 19013, 19014 · E_0257</text>\n<text x=\"487\" y=\"738\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0257 — Stornierung prüfen</text>\n<line x1=\"365\" y1=\"772\" x2=\"121\" y2=\"772\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"763\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"787\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n</svg>"} titel="ESA" />

<a id="abschnitt-schritte"></a>

## Prozessschritte

<Schritt nr="1" anker="schritt-1" richtung="ausgehend" kopf={{"links": {"label": "ESA", "eigen": true}, "rechts": {"label": "MSB"}}}>

### Anfrage von Werten

<Schrittskizze sicht={{"label": "ESA"}} zeilen={[{"art": "senden", "label": "MSB", "weg": "AS4", "nachrichten": [{"nr": "35003", "titel": "Anfrage von Werten"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [35003](/schnittstellen/202610/pruefi/REQOTE/PI_35003) — Anfrage von Werten · AS4

</div>

**Ablauf**

<div data-ablauf data-offen="ja">

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht an **MSB** · AS4

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

<Schritt nr="2" anker="schritt-2" richtung="eingehend" kopf={{"links": {"label": "ESA", "eigen": true}, "rechts": {"label": "MSB"}}}>

### Angebot zur / Ablehnung der Anfrage

<Schrittskizze sicht={{"label": "ESA"}} zeilen={[{"art": "empfangen", "label": "MSB", "weg": "AS4", "nachrichten": [{"nr": "15003", "titel": "Angebot zur Anfrage von Werten"}, {"nr": "21033", "titel": "Ablehnung der Anfrage"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [15003](/schnittstellen/202610/pruefi/QUOTES/PI_15003) — Angebot zur Anfrage von Werten · AS4
- [21033](/schnittstellen/202610/pruefi/IFTSTA/PI_21033) — Ablehnung der Anfrage · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **MSB** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `21033` → [E_0252](/referenz/202610/ebd/E_0252) · MSB · Anfrage prüfen

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

<Schritt nr="3" anker="schritt-3" richtung="ausgehend" kopf={{"links": {"label": "ESA", "eigen": true}, "rechts": {"label": "MSB"}}}>

### Bestellung

<Schrittskizze sicht={{"label": "ESA"}} zeilen={[{"art": "senden", "label": "MSB", "weg": "AS4", "nachrichten": [{"nr": "17007", "titel": "Bestellung von Werten"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [17007](/schnittstellen/202610/pruefi/ORDERS/PI_17007) — Bestellung von Werten · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht an **MSB** · AS4

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

<Schritt nr="4" anker="schritt-4" richtung="eingehend" kopf={{"links": {"label": "ESA", "eigen": true}, "rechts": {"label": "MSB"}}}>

### Antwort auf Bestellung

<Schrittskizze sicht={{"label": "ESA"}} zeilen={[{"art": "empfangen", "label": "MSB", "weg": "AS4", "nachrichten": [{"nr": "19011", "titel": "Bestätigung der Ab-/Bestellung von Werten"}, {"nr": "19012", "titel": "Ablehnung der Ab-/Bestellung von Werten"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [19011](/schnittstellen/202610/pruefi/ORDRSP/PI_19011) — Bestätigung der Ab-/Bestellung von Werten · AS4
- [19012](/schnittstellen/202610/pruefi/ORDRSP/PI_19012) — Ablehnung der Ab-/Bestellung von Werten · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **MSB** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `19011`, `19012` → [E_0256](/referenz/202610/ebd/E_0256) · MSB · Bestellung prüfen

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

<Schritt nr="5" anker="schritt-5" richtung="ausgehend" kopf={{"links": {"label": "ESA", "eigen": true}, "rechts": {"label": "MSB"}}}>

### Stornierung einer bestätigten Bestellung

<Schrittskizze sicht={{"label": "ESA"}} zeilen={[{"art": "senden", "label": "MSB", "weg": "AS4", "nachrichten": [{"nr": "39002", "titel": "Stornierung der Bestellung"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [39002](/schnittstellen/202610/pruefi/ORDCHG/PI_39002) — Stornierung der Bestellung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht an **MSB** · AS4

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

<Schritt nr="6" anker="schritt-6" richtung="eingehend" kopf={{"links": {"label": "ESA", "eigen": true}, "rechts": {"label": "MSB"}}}>

### Antwort auf Stornierung einer bestätigten Bestellung

<Schrittskizze sicht={{"label": "ESA"}} zeilen={[{"art": "empfangen", "label": "MSB", "weg": "AS4", "nachrichten": [{"nr": "19013", "titel": "Bestätigung der Stornierung einer Bestellung"}, {"nr": "19014", "titel": "Ablehnung der Stornierung einer Bestellung"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [19013](/schnittstellen/202610/pruefi/ORDRSP/PI_19013) — Bestätigung der Stornierung einer Bestellung · AS4
- [19014](/schnittstellen/202610/pruefi/ORDRSP/PI_19014) — Ablehnung der Stornierung einer Bestellung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **MSB** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `19013`, `19014` → [E_0257](/referenz/202610/ebd/E_0257) · MSB · Stornierung prüfen

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
| [E_0252](/referenz/202610/ebd/E_0252) | Anfrage prüfen |
| [E_0256](/referenz/202610/ebd/E_0256) | Bestellung prüfen |
| [E_0257](/referenz/202610/ebd/E_0257) | Stornierung prüfen |

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

Der Beteiligte dieser Seite sendet selbst: „Anfrage von Werten“ an **MSB** (Schritt 1).

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

- [Sicht MSB](/prozessdoku/202610/MSB/WiM-Teil2-anfrage-und-bestellung-von-werten-durch-den-esa) — MSB

<Hinweisbereich>

*Die Schritte sind die **möglichen** Nachrichten dieses Prozesses, keine Abfolge — die Quelle führt weder Bedingungen noch Alternativen. Das Kästchen am Schritt nennt links die eigene Sicht: **←** empfängt sie, **→** sendet sie. Zugeklappte Schritte laufen zwischen anderen Marktpartnern.*

Welches Ereignis diese Schritte anstößt, benennt die Quelle noch nicht.

Betrifft: [1](#schritt-1)

Die Konnektortabelle führt für diese Schritte keinen Schreibaufruf. Abgeleitet aus dem Prozessverlauf: Die eigene Rolle war an diesem Prozess schon beteiligt, der Vorgang besteht also.

Betrifft: [2](#schritt-2), [4](#schritt-4), [6](#schritt-6)

Für diese Marktrolle liegt kein Schreibkatalog vor; am Schritt steht deshalb nur das Kommando des Schreibaufrufs, ohne Adresse und ohne Knopf.

Betrifft: [1](#schritt-1), [2](#schritt-2), [3](#schritt-3), [4](#schritt-4), [5](#schritt-5), [6](#schritt-6)

</Hinweisbereich>
