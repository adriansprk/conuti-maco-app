# Abrechnungsdaten Netznutzungsabrechnung — Sicht NB

<Kopf rolle="NB" beteiligter="NB" festlegung="GPKE" dokument="GPKE Teil 2" kapitel="3.1.1.2" sparte="Strom" schritte={3} suchtitel="Abrechnungsdaten Netznutzungsabrechnung — Sicht NB · GPKE Teil 2 · Formatversion 202604" abschnitte={[{"id": "abschnitt-ablauf", "label": "Prozessablauf"}, {"id": "abschnitt-schritte", "label": "Prozessschritte"}, {"id": "abschnitt-informationen", "label": "Prozess-Informationen"}, {"id": "abschnitt-sichten", "label": "Andere Sichten des Prozesses"}]} />

<Kurzfassung>

Der NB übermittelt dem LF die Abrechnungsdaten zur Netznutzungsabrechnung. Der LF prüft die Daten und gibt dem NB eine Qualitätsrückmeldung zum Inhalt der Daten. Sofern der LF einen anderen Inhalt der Daten erwartet, gibt er dies in der Rückmeldung an. Der NB teilt dem LF in diesem Fall den Bearbeitungstand zu dessen Rückmeldung mit.

</Kurzfassung>

<a id="abschnitt-ablauf"></a>

## Prozessablauf aus Sicht des NB

<Systembild svg={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1004 1107\" width=\"1004\" height=\"1107\" role=\"img\" aria-labelledby=\"sb-title\" class=\"maco-systembild\">\n<title id=\"sb-title\">Systembild: Abrechnungsdaten Netznutzungsabrechnung aus Sicht NB</title>\n<defs><marker id=\"sb-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect class=\"sb-lane-kopf\" x=\"16\" y=\"12\" width=\"232\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend-System des Kunden</text>\n<rect class=\"sb-lane-kopf\" x=\"398\" y=\"12\" width=\"264\" height=\"46\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · NB</text>\n<rect class=\"sb-lane-kopf\" x=\"812\" y=\"12\" width=\"176\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"900\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Marktpartner</text>\n<line x1=\"323\" y1=\"58\" x2=\"323\" y2=\"1095\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"737\" y1=\"58\" x2=\"737\" y2=\"1095\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect class=\"sb-kasten sb-trigger\" x=\"432\" y=\"80\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessauslöser empfangen</text>\n<rect class=\"sb-kasten sb-backend sb-trigger\" x=\"34\" y=\"80\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">START_ABR_NN</text>\n<line x1=\"230\" y1=\"96\" x2=\"432\" y2=\"96\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"88\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"144\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"164\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">1. Abrechnungsdaten</text>\n<text x=\"530\" y=\"179\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Netznutzungsabrechnung</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"113\" x2=\"530\" y2=\"144\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"150\" r=\"5\"/><line x1=\"900\" y1=\"155\" x2=\"900\" y2=\"167\"/><line x1=\"893\" y1=\"159\" x2=\"907\" y2=\"159\"/><line x1=\"900\" y1=\"167\" x2=\"894\" y2=\"177\"/><line x1=\"900\" y1=\"167\" x2=\"906\" y2=\"177\"/></g>\n<text x=\"900\" y=\"199\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">LF</text>\n<line x1=\"628\" y1=\"168\" x2=\"878\" y2=\"168\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"160\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"184\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">55218</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"227\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"247\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"192\" x2=\"530\" y2=\"227\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"227\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"247\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"243\" x2=\"230\" y2=\"243\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"235\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"291\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"311\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">2. Rückmeldung auf</text>\n<text x=\"530\" y=\"326\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Abrechnungsdaten</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"260\" x2=\"530\" y2=\"291\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"297\" r=\"5\"/><line x1=\"900\" y1=\"302\" x2=\"900\" y2=\"314\"/><line x1=\"893\" y1=\"306\" x2=\"907\" y2=\"306\"/><line x1=\"900\" y1=\"314\" x2=\"894\" y2=\"324\"/><line x1=\"900\" y1=\"314\" x2=\"906\" y2=\"324\"/></g>\n<text x=\"900\" y=\"346\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">LF</text>\n<line x1=\"878\" y1=\"315\" x2=\"628\" y2=\"315\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"307\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"331\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">55220</text>\n<rect class=\"sb-kasten sb-aperak_lesen\" x=\"432\" y=\"374\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"394\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Daten für die</text>\n<text x=\"530\" y=\"409\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Eingangsprüfung laden</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"339\" x2=\"530\" y2=\"374\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-aperak_lesen\" x=\"34\" y=\"382\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"402\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Marktlokation lesen</text>\n<line x1=\"432\" y1=\"398\" x2=\"230\" y2=\"398\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"390\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"448\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"468\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z10, Z16,</text>\n<text x=\"530\" y=\"483\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Z43, Z33</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"422\" x2=\"530\" y2=\"448\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-schreiben\" x=\"432\" y=\"522\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"542\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"496\" x2=\"530\" y2=\"522\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-schreiben\" x=\"34\" y=\"522\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"542\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten erstellen</text>\n<line x1=\"432\" y1=\"538\" x2=\"230\" y2=\"538\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"530\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"586\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"606\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"555\" x2=\"530\" y2=\"586\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"586\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"606\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"602\" x2=\"230\" y2=\"602\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"594\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-ebd\" x=\"432\" y=\"650\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"670\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">EBD prüfen: E_0595</text>\n<text x=\"530\" y=\"685\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label-2, #424245)\">Bestellung prüfen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"619\" x2=\"530\" y2=\"650\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-folgeprozess\" x=\"432\" y=\"724\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"744\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Folgeprozess auslösen:</text>\n<text x=\"530\" y=\"759\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">21047</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"698\" x2=\"530\" y2=\"724\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-folge_ausloeser\" x=\"432\" y=\"798\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"818\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Ausgelöst durch Eingang:</text>\n<text x=\"530\" y=\"833\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">55220</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"772\" x2=\"530\" y2=\"798\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-trigger\" x=\"432\" y=\"872\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"892\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessauslöser empfangen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"846\" x2=\"530\" y2=\"872\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-trigger\" x=\"34\" y=\"872\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"892\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">2 Ereignisse, alternativ</text>\n<line x1=\"230\" y1=\"888\" x2=\"432\" y2=\"888\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"880\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"936\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"956\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">3. Bearbeitungsstand zur</text>\n<text x=\"530\" y=\"971\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Rückmeldung</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"905\" x2=\"530\" y2=\"936\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"942\" r=\"5\"/><line x1=\"900\" y1=\"947\" x2=\"900\" y2=\"959\"/><line x1=\"893\" y1=\"951\" x2=\"907\" y2=\"951\"/><line x1=\"900\" y1=\"959\" x2=\"894\" y2=\"969\"/><line x1=\"900\" y1=\"959\" x2=\"906\" y2=\"969\"/></g>\n<text x=\"900\" y=\"991\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">LF</text>\n<line x1=\"628\" y1=\"960\" x2=\"878\" y2=\"960\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"952\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"976\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">21047</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"1019\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1039\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"984\" x2=\"530\" y2=\"1019\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"1019\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"1039\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"1035\" x2=\"230\" y2=\"1035\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"1027\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n</svg>"} gesamt={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 730 672\" width=\"730\" height=\"672\" role=\"img\" aria-labelledby=\"sd-title\" class=\"maco-sequence\">\n<title id=\"sd-title\">Sequenzdiagramm: Abrechnungsdaten Netznutzungsabrechnung aus Sicht NB</title>\n<defs><marker id=\"sd-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect x=\"16\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"121\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend (Kunde)</text>\n<line x1=\"121\" y1=\"64\" x2=\"121\" y2=\"660\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"260\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"365\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · NB</text>\n<line x1=\"365\" y1=\"64\" x2=\"365\" y2=\"660\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"504\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"609\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">LF</text>\n<line x1=\"609\" y1=\"64\" x2=\"609\" y2=\"660\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"121\" y1=\"90\" x2=\"365\" y2=\"90\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"81\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">START_ABR_NN</text>\n<text x=\"243\" y=\"105\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Trigger-Event</text>\n<line x1=\"365\" y1=\"152\" x2=\"609\" y2=\"152\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"143\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">1. Abrechnungsdaten Netznutzungsabrechnung</text>\n<text x=\"487\" y=\"167\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55218</text>\n<line x1=\"365\" y1=\"214\" x2=\"121\" y2=\"214\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"205\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"229\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"609\" y1=\"276\" x2=\"365\" y2=\"276\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"267\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">2. Rückmeldung auf Abrechnungsdaten</text>\n<text x=\"487\" y=\"291\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55220 · E_0610</text>\n<text x=\"487\" y=\"304\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0610 — Abrechnungsdaten Netznutzungsabrechnung prüfen</text>\n<line x1=\"365\" y1=\"338\" x2=\"121\" y2=\"338\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"329\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<text x=\"243\" y=\"353\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten erstellen</text>\n<line x1=\"365\" y1=\"400\" x2=\"121\" y2=\"400\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"391\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"415\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"121\" y1=\"462\" x2=\"365\" y2=\"462\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"453\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">2 Ereignisse, alternativ</text>\n<text x=\"243\" y=\"477\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Trigger-Event</text>\n<line x1=\"365\" y1=\"524\" x2=\"609\" y2=\"524\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"515\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">3. Bearbeitungsstand zur Rückmeldung</text>\n<text x=\"487\" y=\"539\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 21047 · E_0620</text>\n<text x=\"487\" y=\"552\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0620 — Rückmeldung prüfen</text>\n<line x1=\"365\" y1=\"586\" x2=\"121\" y2=\"586\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"577\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"601\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n</svg>"} titel="NB" />

<a id="abschnitt-schritte"></a>

## Prozessschritte

<Schritt nr="1" anker="schritt-1" richtung="ausgehend" kopf={{"links": {"label": "NB", "eigen": true}, "rechts": {"label": "LF"}}}>

### Abrechnungsdaten Netznutzungsabrechnung

<Schrittskizze sicht={{"label": "NB"}} zeilen={[{"art": "ausloeser", "werte": ["START_ABR_NN"]}, {"art": "senden", "label": "LF", "weg": "AS4", "nachrichten": [{"nr": "55218", "titel": "Abr.-Daten NNA"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55218](/schnittstellen/202604/pruefi/UTILMD/PI_55218) — Abr.-Daten NNA · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="ausloeser">

**Prozessauslöser** [`START_ABR_NN`](/schnittstellen/202604/trigger/events/NB-START_ABR_NN) · [Im Playground ausprobieren](/api/202604/ausloeser-nb/start-abr-nn)

Das Backend stößt diesen Schritt mit diesem Ereignis an.

</li>

<li data-teil="nachricht">

Nachricht an **LF** · AS4

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202604/backend-schreiben-nb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"BILANZIERUNG\": [\n      {\n        \"boTyp\": \"BILANZIERUNG\",\n        \"datenqualitaet\": \"GUELTIGE_DATEN\",\n        \"gueltigkeitszeitraum\": {\n          \"startdatum\": \"2025-04-02T22:00:00Z\",\n          \"zeitraumId\": 2\n        },\n        \"verbrauchsaufteilung\": {\n          \"einheit\": \"PROZENT\",\n          \"wert\": 50\n        },\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"MARKTLOKATION\": [\n      {\n        \"boTyp\": \"MARKTLOKATION\",\n        \"datenqualitaet\": \"GUELTIGE_DATEN\",\n        \"gueltigkeitszeitraum\": {\n          \"startdatum\": \"2025-04-02T22:00:00Z\",\n          \"zeitraumId\": 2\n        },\n        \"marktlokationsId\": \"50074561188\",\n        \"marktlokationsTyp\": [\n          {\n            \"typ\": \"STANDARD_MARKTLOKATION\"\n          }\n        ],\n        \"netzbetreiberCodeNr\": \"9900321000005\",\n        \"netznutzungsabrechnungsdaten\": [\n          {\n            \"anzahl\": 1,\n            \"artikelId\": \"1-06-1-001\",\n            \"artikelIdTyp\": \"ARTIKELID\",\n            \"gemeinderabatt\": 5\n          }\n        ],\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"NETZNUTZUNGSVERTRAG\": [\n      {\n        \"boTyp\": \"VERTRAG\",\n        \"datenqualitaet\": \"GUELTIGE_DATEN\",\n        \"gueltigkeitszeitraum\": {\n          \"startdatum\": \"2025-04-02T22:00:00Z\",\n          \"zeitraumId\": 2\n        },\n        \"lokationsId\": \"50074561188\",\n        \"lokationsTyp\": \"MALO\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\",\n        \"vertragsart\": \"NETZNUTZUNGSVERTRAG\",\n        \"vertragskonditionen\": {\n          \"naechstenetznutzungsabrechnung\": \"2026\",\n          \"netznutzungsabrechnung\": {\n            \"abrechnungsZeitraum\": \"0101\"\n          },\n          \"netznutzungsabrechnungIntervall\": 12,\n          \"netznutzungsabrechnungsgrundlage\": \"LIEFERSCHEIN\",\n          \"netznutzungsvertrag\": \"LIEFERANTEN_NB\",\n          \"netznutzungszahler\": \"LIEFERANT\"\n        }\n      }\n    ],\n    \"VERWENDUNGSZEITRAUM\": [\n      {\n        \"boTyp\": \"VERWENDUNGSZEITRAUM\",\n        \"datenqualitaet\": \"KEINE_DATEN\",\n        \"versionStruktur\": \"1\",\n        \"verwendungAb\": \"2024-04-02T22:00:00Z\",\n        \"verwendungBis\": \"2025-04-02T22:00:00Z\",\n        \"zeitraumId\": 1\n      },\n      {\n        \"boTyp\": \"VERWENDUNGSZEITRAUM\",\n        \"datenqualitaet\": \"GUELTIGE_DATEN\",\n        \"versionStruktur\": \"1\",\n        \"verwendungAb\": \"2025-04-02T22:00:00Z\",\n        \"zeitraumId\": 2\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9900321000005\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"datenaustauschreferenz\": \"M3FEEF2D\",\n    \"dokumentennummer\": \"BGMM3SITZJ9\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9903790000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"E03\",\n    \"nachrichtendatum\": \"2025-04-04T12:00:00Z\",\n    \"nachrichtenreferenznummer\": \"UNHM3XTW8A0\",\n    \"pruefidentifikator\": \"55218\",\n    \"sparte\": \"STROM\",\n    \"transaktionsgrund\": \"ZX4\",\n    \"vorgangsnummer\": \"123456\"\n  },\n  \"zusatzdaten\": {}\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend fort, nachdem die Nachricht erstellt ist.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="2" anker="schritt-2" richtung="eingehend" kopf={{"links": {"label": "NB", "eigen": true}, "rechts": {"label": "LF"}}}>

### Rückmeldung auf Abrechnungsdaten

<Schrittskizze sicht={{"label": "NB"}} zeilen={[{"art": "empfangen", "label": "LF", "weg": "AS4", "nachrichten": [{"nr": "55220", "titel": "Rückmeldung/Anfrage Abr.-Daten NNA"}]}, {"art": "lesen_aperak", "schnittstellen": [{"label": "Marktlokation lesen"}]}, {"art": "aperak", "werte": ["Z10", "Z16", "Z43", "Z33"]}, {"art": "erstellen"}, {"art": "fortschreiben"}, {"art": "ebd", "baeume": [{"code": "E_0595", "titel": "Bestellung prüfen"}]}, {"art": "folgeprozess", "werte": ["21047"]}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55220](/schnittstellen/202604/pruefi/UTILMD/PI_55220) — Rückmeldung/Anfrage Abr.-Daten NNA · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **LF** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `55220` → [E_0610](/referenz/202604/ebd/E_0610) · LF · Abrechnungsdaten Netznutzungsabrechnung prüfen (Basiert auf EBD: E_0408_Änderung vom NB prüfen)

</div>

</li>

<li data-teil="lesen" data-stufe="aperak">

**Daten für die Eingangsprüfung laden**
- [Marktlokation lesen](/api/202604/backend-lesen/getmarketlocationbasic#marktlokation-lesen) `GET /getMarketLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getMarketLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": false, "defaultValue": "MALO", "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": false, "defaultValue": "2024-06-28T12:18:00Z", "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_MARKTLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

</li>

<li data-teil="aperak">

**Aperak-Prüfungen**
- `55220` → `Z10`
- `55220` → `Z16`
- `55220` → `Z43` — Aperak Prüfung: Stimmt Objekteigenschaft überein?
- `55220` → `Z33`

</li>

<li data-teil="schnittstelle" data-art="schreiben">

**Schreibende Schnittstelle**
- Vorgang angelegt — [Prozessdaten erstellen](/api/202604/backend-schreiben-nb/createprocessdata#prozessdaten-erstellen) `POST /createProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/createProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "ERSTELLEN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"BILANZIERUNG\": [\n      {\n        \"boTyp\": \"BILANZIERUNG\",\n        \"datenqualitaet\": \"ERWARTETE_DATEN\",\n        \"gueltigkeitszeitraum\": {\n          \"enddatum\": \"2025-07-23T22:00:00Z\",\n          \"startdatum\": \"2025-06-23T22:00:00Z\",\n          \"zeitraumId\": 1\n        },\n        \"verbrauchsaufteilung\": {\n          \"einheit\": \"PROZENT\",\n          \"wert\": 25\n        },\n        \"versionStruktur\": \"1\"\n      },\n      {\n        \"boTyp\": \"BILANZIERUNG\",\n        \"datenqualitaet\": \"ERWARTETE_DATEN\",\n        \"gueltigkeitszeitraum\": {\n          \"startdatum\": \"2025-07-23T22:00:00Z\",\n          \"zeitraumId\": 2\n        },\n        \"verbrauchsaufteilung\": {\n          \"einheit\": \"PROZENT\",\n          \"wert\": 25\n        },\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"MARKTLOKATION\": [\n      {\n        \"boTyp\": \"MARKTLOKATION\",\n        \"datenqualitaet\": \"ERWARTETE_DATEN\",\n        \"gueltigkeitszeitraum\": {\n          \"enddatum\": \"2025-07-23T22:00:00Z\",\n          \"startdatum\": \"2025-06-23T22:00:00Z\",\n          \"zeitraumId\": 1\n        },\n        \"marktlokationsId\": \"20072281644\",\n        \"netzbetreiberCodeNr\": \"9900327000009\",\n        \"netznutzungsabrechnungsdaten\": [\n          {\n            \"artikelId\": \"1-02-0-001\",\n            \"artikelIdTyp\": \"ARTIKELID\",\n            \"gemeinderabatt\": 0\n          }\n        ],\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      },\n      {\n        \"boTyp\": \"MARKTLOKATION\",\n        \"datenqualitaet\": \"ERWARTETE_DATEN\",\n        \"gueltigkeitszeitraum\": {\n          \"startdatum\": \"2025-07-23T22:00:00Z\",\n          \"zeitraumId\": 2\n        },\n        \"marktlokationsId\": \"20072281644\",\n        \"netzbetreiberCodeNr\": \"9900327000009\",\n        \"netznutzungsabrechnungsdaten\": [\n          {\n            \"anzahl\": 1,\n            \"artikelId\": \"1-06-5-001\",\n            \"artikelIdTyp\": \"ARTIKELID\",\n            \"gemeinderabatt\": 0\n          }\n        ],\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"NETZNUTZUNGSVERTRAG\": [\n      {\n        \"boTyp\": \"VERTRAG\",\n        \"datenqualitaet\": \"ERWARTETE_DATEN\",\n        \"gueltigkeitszeitraum\": {\n          \"enddatum\": \"2025-07-23T22:00:00Z\",\n          \"startdatum\": \"2025-06-23T22:00:00Z\",\n          \"zeitraumId\": 1\n        },\n        \"lokationsId\": \"20072281644\",\n        \"lokationsTyp\": \"MALO\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\",\n        \"vertragsart\": \"NETZNUTZUNGSVERTRAG\",\n        \"vertragskonditionen\": {\n          \"naechstenetznutzungsabrechnung\": \"2025\",\n          \"netznutzungsabrechnung\": {\n            \"abrechnungsZeitraum\": \"10051005\"\n          },\n          \"netznutzungsabrechnungIntervall\": 12,\n          \"netznutzungsabrechnungsgrundlage\": \"LIEFERSCHEIN\",\n          \"netznutzungsvertrag\": \"LIEFERANTEN_NB\",\n          \"netznutzungszahler\": \"LIEFERANT\"\n        }\n      },\n      {\n        \"boTyp\": \"VERTRAG\",\n        \"datenqualitaet\": \"ERWARTETE_DATEN\",\n        \"gueltigkeitszeitraum\": {\n          \"startdatum\": \"2025-07-23T22:00:00Z\",\n          \"zeitraumId\": 2\n        },\n        \"lokationsId\": \"20072281644\",\n        \"lokationsTyp\": \"MALO\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\",\n        \"vertragsart\": \"NETZNUTZUNGSVERTRAG\",\n        \"vertragskonditionen\": {\n          \"naechstenetznutzungsabrechnung\": \"2025\",\n          \"netznutzungsabrechnung\": {\n            \"abrechnungsZeitraum\": \"10051005\"\n          },\n          \"netznutzungsabrechnungIntervall\": 12,\n          \"netznutzungsabrechnungsgrundlage\": \"LIEFERSCHEIN\",\n          \"netznutzungsvertrag\": \"LIEFERANTEN_NB\",\n          \"netznutzungszahler\": \"LIEFERANT\"\n        }\n      }\n    ],\n    \"VERWENDUNGSZEITRAUM\": [\n      {\n        \"boTyp\": \"VERWENDUNGSZEITRAUM\",\n        \"datenqualitaet\": \"ERWARTETE_DATEN\",\n        \"versionStruktur\": \"1\",\n        \"verwendungAb\": \"2025-06-23T22:00:00Z\",\n        \"verwendungBis\": \"2025-07-23T22:00:00Z\",\n        \"zeitraumId\": 1\n      },\n      {\n        \"boTyp\": \"VERWENDUNGSZEITRAUM\",\n        \"datenqualitaet\": \"ERWARTETE_DATEN\",\n        \"versionStruktur\": \"1\",\n        \"verwendungAb\": \"2025-07-23T22:00:00Z\",\n        \"zeitraumId\": 2\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9903729000007\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"anfragereferenznummer\": \"NNV1234\",\n    \"antwortStatusZeitraum\": [\n      {\n        \"code\": \"A02\",\n        \"liste\": \"E_0610\",\n        \"zeitraumId\": 1\n      },\n      {\n        \"code\": \"A02\",\n        \"liste\": \"E_0610\",\n        \"zeitraumId\": 2\n      }\n    ],\n    \"datenaustauschreferenz\": \"M4882AWT\",\n    \"dokumentennummer\": \"BGMM49EB0JE\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9900327000009\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"E03\",\n    \"nachrichtendatum\": \"2025-06-24T12:31:00Z\",\n    \"nachrichtenreferenznummer\": \"UNHM3PYBDP9\",\n    \"pruefidentifikator\": \"55220\",\n    \"sparte\": \"STROM\",\n    \"transaktionsgrund\": \"ZX4\",\n    \"vorgangsnummer\": \"24062416225400000000000102159662011\"\n  },\n  \"zusatzdaten\": {}\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Legt im Backend einen neuen Vorgang mit den Daten der eingegangenen Nachricht an.

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202604/backend-schreiben-nb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"BILANZIERUNG\": [\n      {\n        \"boTyp\": \"BILANZIERUNG\",\n        \"datenqualitaet\": \"ERWARTETE_DATEN\",\n        \"gueltigkeitszeitraum\": {\n          \"enddatum\": \"2025-07-23T22:00:00Z\",\n          \"startdatum\": \"2025-06-23T22:00:00Z\",\n          \"zeitraumId\": 1\n        },\n        \"verbrauchsaufteilung\": {\n          \"einheit\": \"PROZENT\",\n          \"wert\": 25\n        },\n        \"versionStruktur\": \"1\"\n      },\n      {\n        \"boTyp\": \"BILANZIERUNG\",\n        \"datenqualitaet\": \"ERWARTETE_DATEN\",\n        \"gueltigkeitszeitraum\": {\n          \"startdatum\": \"2025-07-23T22:00:00Z\",\n          \"zeitraumId\": 2\n        },\n        \"verbrauchsaufteilung\": {\n          \"einheit\": \"PROZENT\",\n          \"wert\": 25\n        },\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"MARKTLOKATION\": [\n      {\n        \"boTyp\": \"MARKTLOKATION\",\n        \"datenqualitaet\": \"ERWARTETE_DATEN\",\n        \"gueltigkeitszeitraum\": {\n          \"enddatum\": \"2025-07-23T22:00:00Z\",\n          \"startdatum\": \"2025-06-23T22:00:00Z\",\n          \"zeitraumId\": 1\n        },\n        \"marktlokationsId\": \"20072281644\",\n        \"netzbetreiberCodeNr\": \"9900327000009\",\n        \"netznutzungsabrechnungsdaten\": [\n          {\n            \"artikelId\": \"1-02-0-001\",\n            \"artikelIdTyp\": \"ARTIKELID\",\n            \"gemeinderabatt\": 0\n          }\n        ],\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      },\n      {\n        \"boTyp\": \"MARKTLOKATION\",\n        \"datenqualitaet\": \"ERWARTETE_DATEN\",\n        \"gueltigkeitszeitraum\": {\n          \"startdatum\": \"2025-07-23T22:00:00Z\",\n          \"zeitraumId\": 2\n        },\n        \"marktlokationsId\": \"20072281644\",\n        \"netzbetreiberCodeNr\": \"9900327000009\",\n        \"netznutzungsabrechnungsdaten\": [\n          {\n            \"anzahl\": 1,\n            \"artikelId\": \"1-06-5-001\",\n            \"artikelIdTyp\": \"ARTIKELID\",\n            \"gemeinderabatt\": 0\n          }\n        ],\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"NETZNUTZUNGSVERTRAG\": [\n      {\n        \"boTyp\": \"VERTRAG\",\n        \"datenqualitaet\": \"ERWARTETE_DATEN\",\n        \"gueltigkeitszeitraum\": {\n          \"enddatum\": \"2025-07-23T22:00:00Z\",\n          \"startdatum\": \"2025-06-23T22:00:00Z\",\n          \"zeitraumId\": 1\n        },\n        \"lokationsId\": \"20072281644\",\n        \"lokationsTyp\": \"MALO\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\",\n        \"vertragsart\": \"NETZNUTZUNGSVERTRAG\",\n        \"vertragskonditionen\": {\n          \"naechstenetznutzungsabrechnung\": \"2025\",\n          \"netznutzungsabrechnung\": {\n            \"abrechnungsZeitraum\": \"10051005\"\n          },\n          \"netznutzungsabrechnungIntervall\": 12,\n          \"netznutzungsabrechnungsgrundlage\": \"LIEFERSCHEIN\",\n          \"netznutzungsvertrag\": \"LIEFERANTEN_NB\",\n          \"netznutzungszahler\": \"LIEFERANT\"\n        }\n      },\n      {\n        \"boTyp\": \"VERTRAG\",\n        \"datenqualitaet\": \"ERWARTETE_DATEN\",\n        \"gueltigkeitszeitraum\": {\n          \"startdatum\": \"2025-07-23T22:00:00Z\",\n          \"zeitraumId\": 2\n        },\n        \"lokationsId\": \"20072281644\",\n        \"lokationsTyp\": \"MALO\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\",\n        \"vertragsart\": \"NETZNUTZUNGSVERTRAG\",\n        \"vertragskonditionen\": {\n          \"naechstenetznutzungsabrechnung\": \"2025\",\n          \"netznutzungsabrechnung\": {\n            \"abrechnungsZeitraum\": \"10051005\"\n          },\n          \"netznutzungsabrechnungIntervall\": 12,\n          \"netznutzungsabrechnungsgrundlage\": \"LIEFERSCHEIN\",\n          \"netznutzungsvertrag\": \"LIEFERANTEN_NB\",\n          \"netznutzungszahler\": \"LIEFERANT\"\n        }\n      }\n    ],\n    \"VERWENDUNGSZEITRAUM\": [\n      {\n        \"boTyp\": \"VERWENDUNGSZEITRAUM\",\n        \"datenqualitaet\": \"ERWARTETE_DATEN\",\n        \"versionStruktur\": \"1\",\n        \"verwendungAb\": \"2025-06-23T22:00:00Z\",\n        \"verwendungBis\": \"2025-07-23T22:00:00Z\",\n        \"zeitraumId\": 1\n      },\n      {\n        \"boTyp\": \"VERWENDUNGSZEITRAUM\",\n        \"datenqualitaet\": \"ERWARTETE_DATEN\",\n        \"versionStruktur\": \"1\",\n        \"verwendungAb\": \"2025-07-23T22:00:00Z\",\n        \"zeitraumId\": 2\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9903729000007\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"anfragereferenznummer\": \"NNV1234\",\n    \"antwortStatusZeitraum\": [\n      {\n        \"code\": \"A02\",\n        \"liste\": \"E_0610\",\n        \"zeitraumId\": 1\n      },\n      {\n        \"code\": \"A02\",\n        \"liste\": \"E_0610\",\n        \"zeitraumId\": 2\n      }\n    ],\n    \"datenaustauschreferenz\": \"M4882AWT\",\n    \"dokumentennummer\": \"BGMM49EB0JE\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9900327000009\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"E03\",\n    \"nachrichtendatum\": \"2025-06-24T12:31:00Z\",\n    \"nachrichtenreferenznummer\": \"UNHM3PYBDP9\",\n    \"pruefidentifikator\": \"55220\",\n    \"sparte\": \"STROM\",\n    \"transaktionsgrund\": \"ZX4\",\n    \"vorgangsnummer\": \"24062416225400000000000102159662011\"\n  },\n  \"zusatzdaten\": {}\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend mit den Daten der eingegangenen Nachricht fort.

</li>

<li data-teil="baum">

**Entscheidungsbaum**
- `55220` → [E_0595](/referenz/202604/ebd/E_0595) — Bestellung prüfen

</li>

<li data-teil="folgeprozess">

**Folgeprozess auslösen**
- [21047](/schnittstellen/202604/pruefi/IFTSTA/PI_21047) — Bearbeitungsstandsmeldung

Nach der Verarbeitung startet die MACO APP diesen Folgeprozess selbst.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="3" anker="schritt-3" richtung="ausgehend" kopf={{"links": {"label": "NB", "eigen": true}, "rechts": {"label": "LF"}}}>

### Bearbeitungsstand zur Rückmeldung

<Schrittskizze sicht={{"label": "NB"}} zeilen={[{"art": "folge_ausloeser", "werte": ["55220"]}, {"art": "ausloeser", "werte": ["START_VERSAND_BEARB_MELDUNG", "START_VERSAND_STATUSMELDUNG"]}, {"art": "senden", "label": "LF", "weg": "AS4", "nachrichten": [{"nr": "21047", "titel": "Bearbeitungsstandsmeldung"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [21047](/schnittstellen/202604/pruefi/IFTSTA/PI_21047) — Bearbeitungsstandsmeldung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="folge_ausloeser">

**Ausgelöst durch Eingang**
- [55220](/schnittstellen/202604/pruefi/UTILMD/PI_55220) — Rückmeldung/Anfrage Abr.-Daten NNA

Die MACO APP sendet diese Nachricht selbst, als Folgeprozess nach diesem Eingang. Daneben kann das Backend diesen Schritt mit einem Ereignis anstoßen — der nächste Punkt.

</li>

<li data-teil="ausloeser">

**Prozessauslöser**
- [`START_VERSAND_BEARB_MELDUNG`](/schnittstellen/202604/trigger/events/NB-START_VERSAND_BEARB_MELDUNG) · [Im Playground ausprobieren](/api/202604/ausloeser-nb/start-versand-bearb-meldung)
- [`START_VERSAND_STATUSMELDUNG`](/schnittstellen/202604/trigger/events/NB-START_VERSAND_STATUSMELDUNG) · [Im Playground ausprobieren](/api/202604/ausloeser-nb/start-versand-statusmeldung)

Das Backend stößt diesen Schritt mit einem dieser Ereignisse an.

</li>

<li data-teil="nachricht">

Nachricht an **LF** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `21047` → [E_0620](/referenz/202604/ebd/E_0620) · NB · Rückmeldung prüfen (Basiert auf EBD: E_0626_Rückmeldung auf Änderung prüfen)

</div>

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202604/backend-schreiben-nb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"STATUSMITTEILUNG\": [\n      {\n        \"auftragsstatus\": \"KEINE_AENDERUNG_DER_DATEN\",\n        \"boTyp\": \"STATUSMITTEILUNG\",\n        \"positionsdaten\": [\n          {\n            \"positionsnummer\": 1\n          }\n        ],\n        \"statusObjekt\": \"VERAENDERUNGSSTATUS_DER_DATEN\",\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"marktrolle\": \"LF\",\n      \"rollencodenummer\": \"9900321000005\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"antwortstatus\": \"A01\",\n    \"antwortstatusCodeliste\": \"E_0588\",\n    \"datenaustauschreferenz\": \"M0M56B09\",\n    \"dokumentennummer\": \"BGMM0M7F86Z\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"marktrolle\": \"NB\",\n      \"rollencodenummer\": \"9903790000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"Z33\",\n    \"nachrichtendatum\": \"2025-04-04T12:00:00Z\",\n    \"nachrichtenreferenznummer\": \"UNHM09Y0DVP\",\n    \"pruefidentifikator\": \"21047\",\n    \"sparte\": \"STROM\",\n    \"vorgangsreferenznummer\": \"ABC12345\"\n  },\n  \"zusatzdaten\": {}\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

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
| [E_0610](/referenz/202604/ebd/E_0610) | Abrechnungsdaten Netznutzungsabrechnung prüfen (Basiert auf EBD: E_0408_Änderung vom NB prüfen) |
| [E_0620](/referenz/202604/ebd/E_0620) | Rückmeldung prüfen (Basiert auf EBD: E_0626_Rückmeldung auf Änderung prüfen) |

</details>

<a id="abschnitt-informationen"></a>

## Prozess-Informationen

Wortlaut der Lesefassung, Steckbrief Kap. 3.1.1.1, S. 65–66.

<Stepper>
<ol>

<li data-blatt="vorbedingungen">

### Vorbedingungen

- Es handelt sich um eine verbrauchende Marktlokation.

</li>

<li data-blatt="ergebnisse">

### Ergebnisse

Sofern eine Netznutzungsabrechnung gegenüber dem LF stattfindet, führt der NB bei unterjähriger Zuordnung des LFN bzw. E/G zur Marktlokation (über Use-Case „[Lieferbeginn](/prozessdoku/202604/NB/GPKE-Teil2-lieferbeginn)“ bzw. „[Beginn der Ersatz-/Grundversorgung](/prozessdoku/202604/NB/GPKE-Teil2-beginn-der-ersatz-grundversorgung)“) und wenn die Marktlokation mit Arbeits- und Leistungspreis im Rahmen der Netznutzungsabrechnung abgerechnet wird, den Use-Case "Übermittlung der bisher gemessenen Arbeits- und Leistungswerte" durch.

</li>

<li data-blatt="fehlerfall">

### Fehlerfall

#### Fehlerfälle

Es handelt sich um eine erzeugende Marktlokation bzw. eine Tranche.

</li>

<li data-blatt="anforderungen">

### Weitere Anforderungen

Hinweis: Es gibt Situationen, bei denen eine Rechnungskorrektur aufgrund des Austauschs der Abrechnungsdaten zur Netznutzungsabrechnung vorkommen kann. Dies ist z.B. der Fall, wenn bei einer Änderung (Fall b) in die Vergangenheit der Zeitraum einer Rechnung betroffen ist.

</li>

<li data-blatt="anlass">

### Anlass

- Durchführung nach dem Prozessschritt
  - zur Zuordnung des LFN zur Marktlokation im Rahmen des Use-Cases „[Lieferbeginn](/prozessdoku/202604/NB/GPKE-Teil2-lieferbeginn)“ (Fall a).
  - zur Zuordnung des LF zur Marktlokation im Rahmen des Use-Cases „[Neuanlage](/prozessdoku/202604/NB/GPKE-Teil2-neuanlage)“ (Fall a).
  - zur Zuordnung des E/G zur Marktlokation im Rahmen des Use-Cases „[Beginn der Ersatz-/Grundversorgung](/prozessdoku/202604/NB/GPKE-Teil2-beginn-der-ersatz-grundversorgung)“ (Fall a).
  - zur Beendigung der Zuordnung des LF zur Marktlokation im Rahmen des Use-Cases „[Lieferende von LF an NB](/prozessdoku/202604/NB/GPKE-Teil2-lieferende-von-lf-an-nb)“ (Fall a).
  - zur Beendigung der Zuordnung des LF zur Marktlokation im Rahmen des Use-Cases „[Lieferende von NB an LF](/prozessdoku/202604/NB/GPKE-Teil2-lieferende-von-nb-an-lf)“ (Fall a).
  - zum Bearbeitungsstand zur Bestellung im Rahmen des SD „[Bestellung einer Änderung von Abrechnungsdaten von LF an NB](/prozessdoku/202604/NB/GPKE-Teil2-bestellung-einer-aenderung-von-abrechnungsdaten-von-lf-an-nb)“, sofern eine Änderung der Abrechnungsdaten zur Netznutzungsabrechnung vorzunehmen ist (Fall b).
- Durchführung unabhängig der obigen Prozesse,
  - sofern der NB selbst feststellt, dass sich Abrechnungsdaten zur Netznutzungsabrechnung gegenüber dem LF geändert haben (Fall b) (z.B. Änderung des Netznutzungsabrechnungsmodells von Arbeitspreis/Grundpreis auf Arbeitspreis/Leistungspreis).
  - sofern der NB davon ausgeht, dass ein Datenschiefstand zwischen NB und LF vorliegt (Fall b).

**Vorher läuft:** [Beginn der Ersatz-/Grundversorgung](/prozessdoku/202604/NB/GPKE-Teil2-beginn-der-ersatz-grundversorgung), [Bestellung einer Änderung von Abrechnungsdaten von LF an NB](/prozessdoku/202604/NB/GPKE-Teil2-bestellung-einer-aenderung-von-abrechnungsdaten-von-lf-an-nb), [Bestellung einer Änderung von Abrechnungsdaten zur Bilanzkreisabrechnung von ÜNB an NB](/prozessdoku/202604/NB/GPKE-Teil2-bestellung-einer-aenderung-von-abrechnungsdaten-zur-bilanzkreisabrechnung-von-uenb-an-nb), [Lieferbeginn](/prozessdoku/202604/NB/GPKE-Teil2-lieferbeginn), [Lieferende von LF an NB](/prozessdoku/202604/NB/GPKE-Teil2-lieferende-von-lf-an-nb), [Lieferende von NB an LF](/prozessdoku/202604/NB/GPKE-Teil2-lieferende-von-nb-an-lf), [Neuanlage](/prozessdoku/202604/NB/GPKE-Teil2-neuanlage) — diese Prozesse nennen den hier gezeigten in ihrem Ergebnis.

</li>

<li data-blatt="erste-nachricht">

### Erste Nachricht

Der Beteiligte dieser Seite sendet selbst: „Abrechnungsdaten Netznutzungsabrechnung“ an **LF** (Schritt 1).

</li>

<li data-blatt="ziel">

### Ziel

Die Abrechnungsdaten zur Netznutzungsabrechnung sind ausgetauscht.

</li>

</ol>
</Stepper>

<a id="abschnitt-sichten"></a>

## Andere Sichten des Prozesses

Derselbe Prozess, aus den Augen der anderen Beteiligten: dieselben Schritte, jeweils aus deren Sicht gelesen.

- [Sicht LF](/prozessdoku/202604/LF/GPKE-Teil2-abrechnungsdaten-netznutzungsabrechnung) — LF

<Hinweisbereich>

*Die Schritte sind die **möglichen** Nachrichten dieses Prozesses, keine Abfolge — die Quelle führt weder Bedingungen noch Alternativen. Das Kästchen am Schritt nennt links die eigene Sicht: **←** empfängt sie, **→** sendet sie. Zugeklappte Schritte laufen zwischen anderen Marktpartnern.*

</Hinweisbereich>
