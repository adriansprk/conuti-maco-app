# Netznutzungsabrechnung — Sicht LF

<Kopf rolle="LF" beteiligter="LF" festlegung="GPKE" dokument="GPKE Teil 2" kapitel="3.3.2" sparte="Strom" schritte={6} suchtitel="Netznutzungsabrechnung — Sicht LF · GPKE Teil 2 · Formatversion 202610" abschnitte={[{"id": "abschnitt-ablauf", "label": "Prozessablauf"}, {"id": "abschnitt-schritte", "label": "Prozessschritte"}, {"id": "abschnitt-informationen", "label": "Prozess-Informationen"}, {"id": "abschnitt-sichten", "label": "Andere Sichten des Prozesses"}]} />

<Kurzfassung>

Der Prozess beschreibt die Kommunikation zwischen NB und LF zur Abrechnung der Netznutzung und ggf. dem automatisierten Reklamationsfall. Eine Rechnungskorrektur umfasst immer eine Stornorechnung und eine neue Rechnung. Insbesondere in den nachfolgend genannten Fällen kann eine Jahresrechnung korrigiert oder ergänzt werden, ohne dass dies durch Stornierung erfolgt:
- Änderung der Konzessionsabgabe durch Einreichung eines Testates: Prüfung des Grenzpreisvergleichs nach KAV
- Korrektur der Netzentgelte Strom aufgrund individueller Vereinbarung für atypische und energieintensive Netznutzung nach StromNEV
- Korrektur der Netzentgelte Strom aufgrund individueller Vereinbarung für singuläre Netznutzung nach StromNEV
- KWKG-Umlage
- Offshore-Netzumlage. In diesen Fällen kann eine separate, entsprechend gekennzeichnete Rechnung gestellt werden, in der die für das Abrechnungsjahr zu viel oder zu wenig gezahlten Entgelte korrigiert und gemäß Testat, individueller Vereinbarung oder Nachweis erhoben werden. Diese Rechnung hat sich eindeutig auf die Jahresrechnung zu beziehen, deren Position bzw. Positionen sie korrigiert.

</Kurzfassung>

<a id="abschnitt-ablauf"></a>

## Prozessablauf aus Sicht des LF

<Systembild svg={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1004 1352\" width=\"1004\" height=\"1352\" role=\"img\" aria-labelledby=\"sb-title\" class=\"maco-systembild\">\n<title id=\"sb-title\">Systembild: Netznutzungsabrechnung aus Sicht LF</title>\n<defs><marker id=\"sb-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect class=\"sb-lane-kopf\" x=\"16\" y=\"12\" width=\"232\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend-System des Kunden</text>\n<rect class=\"sb-lane-kopf\" x=\"398\" y=\"12\" width=\"264\" height=\"46\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · LF</text>\n<rect class=\"sb-lane-kopf\" x=\"812\" y=\"12\" width=\"176\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"900\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Marktpartner</text>\n<line x1=\"323\" y1=\"58\" x2=\"323\" y2=\"1340\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"737\" y1=\"58\" x2=\"737\" y2=\"1340\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"80\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">1. Netznutzungsrechnung</text>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"78\" r=\"5\"/><line x1=\"900\" y1=\"83\" x2=\"900\" y2=\"95\"/><line x1=\"893\" y1=\"87\" x2=\"907\" y2=\"87\"/><line x1=\"900\" y1=\"95\" x2=\"894\" y2=\"105\"/><line x1=\"900\" y1=\"95\" x2=\"906\" y2=\"105\"/></g>\n<text x=\"900\" y=\"127\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"878\" y1=\"96\" x2=\"628\" y2=\"96\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"88\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"112\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">31001, 31002</text>\n<rect class=\"sb-kasten sb-aperak_lesen\" x=\"432\" y=\"163\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"183\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Daten für die</text>\n<text x=\"530\" y=\"198\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Eingangsprüfung laden</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"113\" x2=\"530\" y2=\"163\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-aperak_lesen\" x=\"34\" y=\"171\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"191\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Marktlokation lesen</text>\n<line x1=\"432\" y1=\"187\" x2=\"230\" y2=\"187\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"179\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-schreiben\" x=\"432\" y=\"237\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"257\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"211\" x2=\"530\" y2=\"237\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-schreiben\" x=\"34\" y=\"237\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"257\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten erstellen</text>\n<line x1=\"432\" y1=\"253\" x2=\"230\" y2=\"253\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"245\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-trigger\" x=\"432\" y=\"301\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"321\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessauslöser empfangen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"270\" x2=\"530\" y2=\"301\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-trigger\" x=\"34\" y=\"293\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"313\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">START_VERSAND_ANTWORT</text>\n<text x=\"132\" y=\"328\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">_NNA</text>\n<line x1=\"230\" y1=\"317\" x2=\"432\" y2=\"317\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"309\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"375\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"395\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">2. Antwort</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"334\" x2=\"530\" y2=\"375\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"373\" r=\"5\"/><line x1=\"900\" y1=\"378\" x2=\"900\" y2=\"390\"/><line x1=\"893\" y1=\"382\" x2=\"907\" y2=\"382\"/><line x1=\"900\" y1=\"390\" x2=\"894\" y2=\"400\"/><line x1=\"900\" y1=\"390\" x2=\"906\" y2=\"400\"/></g>\n<text x=\"900\" y=\"422\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"628\" y1=\"391\" x2=\"878\" y2=\"391\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"383\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"407\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">33001, 33003, 33004</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"458\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"478\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"408\" x2=\"530\" y2=\"458\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"458\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"478\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"474\" x2=\"230\" y2=\"474\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"466\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"522\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"542\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">3. Mitteilung, dass die</text>\n<text x=\"530\" y=\"557\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">ursprüngliche</text>\n<text x=\"530\" y=\"572\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Netznutzungsrechnung kor…</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"491\" x2=\"530\" y2=\"522\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"535\" r=\"5\"/><line x1=\"900\" y1=\"540\" x2=\"900\" y2=\"552\"/><line x1=\"893\" y1=\"544\" x2=\"907\" y2=\"544\"/><line x1=\"900\" y1=\"552\" x2=\"894\" y2=\"562\"/><line x1=\"900\" y1=\"552\" x2=\"906\" y2=\"562\"/></g>\n<text x=\"900\" y=\"584\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"878\" y1=\"553\" x2=\"628\" y2=\"553\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"545\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"569\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">29001</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"611\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"631\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z33</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"585\" x2=\"530\" y2=\"611\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"675\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"695\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"644\" x2=\"530\" y2=\"675\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"675\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"695\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"691\" x2=\"230\" y2=\"691\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"683\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-trigger\" x=\"432\" y=\"739\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"759\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessauslöser empfangen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"708\" x2=\"530\" y2=\"739\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-trigger\" x=\"34\" y=\"731\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"751\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">START_VERSAND_ANTWORT</text>\n<text x=\"132\" y=\"766\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">_NNA</text>\n<line x1=\"230\" y1=\"755\" x2=\"432\" y2=\"755\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"747\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"813\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"833\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">4. Antwort</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"772\" x2=\"530\" y2=\"813\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"811\" r=\"5\"/><line x1=\"900\" y1=\"816\" x2=\"900\" y2=\"828\"/><line x1=\"893\" y1=\"820\" x2=\"907\" y2=\"820\"/><line x1=\"900\" y1=\"828\" x2=\"894\" y2=\"838\"/><line x1=\"900\" y1=\"828\" x2=\"906\" y2=\"838\"/></g>\n<text x=\"900\" y=\"860\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"628\" y1=\"829\" x2=\"878\" y2=\"829\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"821\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"845\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">33001, 33003, 33004</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"896\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"916\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"846\" x2=\"530\" y2=\"896\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"896\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"916\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"912\" x2=\"230\" y2=\"912\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"904\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"960\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"980\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">5. Storno der ursprünglichen</text>\n<text x=\"530\" y=\"995\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Rechnung</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"929\" x2=\"530\" y2=\"960\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"966\" r=\"5\"/><line x1=\"900\" y1=\"971\" x2=\"900\" y2=\"983\"/><line x1=\"893\" y1=\"975\" x2=\"907\" y2=\"975\"/><line x1=\"900\" y1=\"983\" x2=\"894\" y2=\"993\"/><line x1=\"900\" y1=\"983\" x2=\"906\" y2=\"993\"/></g>\n<text x=\"900\" y=\"1015\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"878\" y1=\"984\" x2=\"628\" y2=\"984\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"976\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"1000\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">31004</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"1043\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1063\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1008\" x2=\"530\" y2=\"1043\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"1043\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"1063\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"1059\" x2=\"230\" y2=\"1059\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"1051\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-trigger\" x=\"432\" y=\"1107\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1127\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessauslöser empfangen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1076\" x2=\"530\" y2=\"1107\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-trigger\" x=\"34\" y=\"1099\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"1119\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">START_VERSAND_ANTWORT</text>\n<text x=\"132\" y=\"1134\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">_NNA</text>\n<line x1=\"230\" y1=\"1123\" x2=\"432\" y2=\"1123\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"1115\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"1181\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1201\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">6. Antwort</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1140\" x2=\"530\" y2=\"1181\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"1179\" r=\"5\"/><line x1=\"900\" y1=\"1184\" x2=\"900\" y2=\"1196\"/><line x1=\"893\" y1=\"1188\" x2=\"907\" y2=\"1188\"/><line x1=\"900\" y1=\"1196\" x2=\"894\" y2=\"1206\"/><line x1=\"900\" y1=\"1196\" x2=\"906\" y2=\"1206\"/></g>\n<text x=\"900\" y=\"1228\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"628\" y1=\"1197\" x2=\"878\" y2=\"1197\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"1189\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"1213\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">33001, 33002</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"1264\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1284\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1214\" x2=\"530\" y2=\"1264\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"1264\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"1284\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"1280\" x2=\"230\" y2=\"1280\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"1272\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n</svg>"} gesamt={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 730 1044\" width=\"730\" height=\"1044\" role=\"img\" aria-labelledby=\"sd-title\" class=\"maco-sequence\">\n<title id=\"sd-title\">Sequenzdiagramm: Netznutzungsabrechnung aus Sicht LF</title>\n<defs><marker id=\"sd-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect x=\"16\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"121\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend (Kunde)</text>\n<line x1=\"121\" y1=\"64\" x2=\"121\" y2=\"1032\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"260\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"365\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · LF</text>\n<line x1=\"365\" y1=\"64\" x2=\"365\" y2=\"1032\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"504\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"609\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"609\" y1=\"64\" x2=\"609\" y2=\"1032\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"609\" y1=\"90\" x2=\"365\" y2=\"90\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"81\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">1. Netznutzungsrechnung</text>\n<text x=\"487\" y=\"105\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 31001, 31002</text>\n<line x1=\"365\" y1=\"152\" x2=\"121\" y2=\"152\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"143\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<text x=\"243\" y=\"167\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten erstellen</text>\n<line x1=\"121\" y1=\"214\" x2=\"365\" y2=\"214\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"205\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">START_VERSAND_ANTWORT_NNA</text>\n<text x=\"243\" y=\"229\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Trigger-Event</text>\n<line x1=\"365\" y1=\"276\" x2=\"609\" y2=\"276\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"267\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">2. Antwort</text>\n<text x=\"487\" y=\"291\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 33001, 33003, 33004 · E_0406</text>\n<text x=\"487\" y=\"304\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0406 — Netznutzungsrechnung prüfen</text>\n<line x1=\"365\" y1=\"338\" x2=\"121\" y2=\"338\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"329\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"353\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"609\" y1=\"400\" x2=\"365\" y2=\"400\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"391\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">3. Mitteilung, dass die ursprüngliche Netznutzun…</text>\n<text x=\"487\" y=\"415\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 29001 · E_0452</text>\n<text x=\"487\" y=\"428\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0452 — Nicht-Zahlungsavise prüfen</text>\n<line x1=\"365\" y1=\"462\" x2=\"121\" y2=\"462\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"453\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"477\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"121\" y1=\"524\" x2=\"365\" y2=\"524\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"515\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">START_VERSAND_ANTWORT_NNA</text>\n<text x=\"243\" y=\"539\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Trigger-Event</text>\n<line x1=\"365\" y1=\"586\" x2=\"609\" y2=\"586\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"577\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">4. Antwort</text>\n<text x=\"487\" y=\"601\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 33001, 33003, 33004 · E_0407</text>\n<text x=\"487\" y=\"614\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0407 — erneut Netznutzungsabrechnung prüfen</text>\n<line x1=\"365\" y1=\"648\" x2=\"121\" y2=\"648\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"639\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"663\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"609\" y1=\"710\" x2=\"365\" y2=\"710\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"701\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">5. Storno der ursprünglichen Rechnung</text>\n<text x=\"487\" y=\"725\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 31004</text>\n<line x1=\"365\" y1=\"772\" x2=\"121\" y2=\"772\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"763\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"787\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"121\" y1=\"834\" x2=\"365\" y2=\"834\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"825\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">START_VERSAND_ANTWORT_NNA</text>\n<text x=\"243\" y=\"849\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Trigger-Event</text>\n<line x1=\"365\" y1=\"896\" x2=\"609\" y2=\"896\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"887\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">6. Antwort</text>\n<text x=\"487\" y=\"911\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 33001, 33002 · E_0459</text>\n<text x=\"487\" y=\"924\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0459 — Prüfen, ob Antwort auf Stornierung erforderlich</text>\n<line x1=\"365\" y1=\"958\" x2=\"121\" y2=\"958\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"949\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"973\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n</svg>"} titel="LF" />

<a id="abschnitt-schritte"></a>

## Prozessschritte

<Schritt nr="1" anker="schritt-1" richtung="eingehend" kopf={{"links": {"label": "LF", "eigen": true}, "rechts": {"label": "NB"}}}>

### Netznutzungsrechnung

<Schrittskizze sicht={{"label": "LF"}} zeilen={[{"art": "empfangen", "label": "NB", "weg": "AS4", "nachrichten": [{"nr": "31001", "titel": "Abschlagsrechnung"}, {"nr": "31002", "titel": "NN-Rechnung"}]}, {"art": "lesen_aperak", "schnittstellen": [{"label": "Marktlokation lesen"}]}, {"art": "erstellen"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [31001](/schnittstellen/202610/pruefi/INVOIC/PI_31001) — Abschlagsrechnung · AS4
- [31002](/schnittstellen/202610/pruefi/INVOIC/PI_31002) — NN-Rechnung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **NB** · AS4

</li>

<li data-teil="lesen" data-stufe="aperak">

**Daten für die Eingangsprüfung laden**
- [Marktlokation lesen](/api/202610/backend-lesen/getmarketlocationbasic#marktlokation-lesen) `GET /getMarketLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getMarketLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": false, "defaultValue": "MALO", "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": false, "defaultValue": "2024-06-28T12:18:00Z", "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_MARKTLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

</li>

<li data-teil="schnittstelle" data-art="schreiben">

**Schreibende Schnittstelle**
- Vorgang angelegt — [Prozessdaten erstellen](/api/202610/backend-schreiben-lf/createprocessdata#prozessdaten-erstellen) `POST /createProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/createProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": false, "defaultValue": "ERSTELLEN_PROZESSDATEN", "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"MARKTLOKATION\": [\n      {\n        \"boTyp\": \"MARKTLOKATION\",\n        \"lokationsadresse\": {\n          \"hausnummer\": \"123\",\n          \"landescode\": \"DE\",\n          \"ort\": \"Ort\",\n          \"postleitzahl\": \"75395\",\n          \"strasse\": \"Str.\"\n        },\n        \"marktlokationsId\": \"50074561188\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"RECHNUNG\": [\n      {\n        \"bearbeitungsdatum\": \"2023-05-16T06:48:00Z\",\n        \"boTyp\": \"RECHNUNG\",\n        \"faelligkeitsdatum\": \"2023-06-05T22:00:00Z\",\n        \"gesamtbrutto\": {\n          \"waehrung\": \"EUR\",\n          \"wert\": 1000\n        },\n        \"istSelbstausgestellt\": false,\n        \"rechnungsdatum\": \"2026-10-01T11:00:00Z\",\n        \"rechnungspositionen\": [\n          {\n            \"artikelnummer\": \"ABSCHLAG\",\n            \"einzelpreis\": {\n              \"waehrung\": \"EUR\",\n              \"wert\": 1000\n            },\n            \"lieferungBis\": \"2023-03-31T22:00:00Z\",\n            \"lieferungVon\": \"2023-02-28T23:00:00Z\",\n            \"positionsMenge\": {\n              \"einheit\": \"STUECK\",\n              \"wert\": 1\n            },\n            \"positionsnummer\": 1,\n            \"teilsummeNetto\": {\n              \"waehrung\": \"EUR\",\n              \"wert\": 1000\n            },\n            \"teilsummeSteuer\": {\n              \"steuerkennzeichen\": \"UST_19\"\n            }\n          }\n        ],\n        \"rechnungsstatus\": \"ORIGINAL\",\n        \"rechnungstyp\": \"ABSCHLAGSRECHNUNG\",\n        \"steuerbetraege\": [\n          {\n            \"basiswert\": 1000,\n            \"steuerkennzeichen\": \"UST_19\",\n            \"steuerwert\": 190,\n            \"waehrung\": \"EUR\"\n          }\n        ],\n        \"storno\": false,\n        \"versionStruktur\": \"1\",\n        \"vorlaeufigerAbrechnungszeitraum\": {\n          \"enddatum\": \"2023-03-31T22:00:00Z\",\n          \"startdatum\": \"2023-02-28T23:00:00Z\"\n        },\n        \"zuZahlen\": {\n          \"waehrung\": \"EUR\",\n          \"wert\": 1000\n        }\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"ansprechpartner\": {\n        \"boTyp\": \"ANSPRECHPARTNER\",\n        \"eMailAdresse\": \"max@mustermann.de\",\n        \"nachname\": \"Max Mustermann\",\n        \"rufnummern\": [\n          {\n            \"nummerntyp\": \"RUF_ZENTRALE\",\n            \"rufnummer\": \"+02345678930\"\n          },\n          {\n            \"nummerntyp\": \"FAX_DURCHWAHL\",\n            \"rufnummer\": \"+02345678910\"\n          },\n          {\n            \"nummerntyp\": \"RUF_DURCHWAHL\",\n            \"rufnummer\": \"+02345678920\"\n          },\n          {\n            \"nummerntyp\": \"MOBIL_NUMMER\",\n            \"rufnummer\": \"+02345678940\"\n          }\n        ],\n        \"versionStruktur\": \"1\"\n      },\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"marktrolle\": \"NB\",\n      \"name1\": \"Stadtwerke\",\n      \"partneradresse\": {\n        \"hausnummer\": \"9\",\n        \"landescode\": \"DE\",\n        \"ort\": \"Ort\",\n        \"postleitzahl\": \"12345\",\n        \"strasse\": \"Str.\"\n      },\n      \"rollencodenummer\": \"9900321000005\",\n      \"rollencodetyp\": \"BDEW\",\n      \"steuernummer\": \"12345678910\",\n      \"versionStruktur\": \"1\"\n    },\n    \"datenaustauschreferenz\": \"168546\",\n    \"dokumentennummer\": \"714669BGM\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"marktrolle\": \"LF\",\n      \"name1\": \"Lieferant\",\n      \"partneradresse\": {\n        \"hausnummer\": \"1\",\n        \"landescode\": \"DE\",\n        \"ort\": \"Ort\",\n        \"postleitzahl\": \"54321\",\n        \"strasse\": \"Str.\"\n      },\n      \"rollencodenummer\": \"9903790000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"380\",\n    \"nachrichtenreferenznummer\": \"NIK KIRS714669\",\n    \"pruefidentifikator\": \"31001\",\n    \"sparte\": \"STROM\"\n  },\n  \"zusatzdaten\": {}\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Legt im Backend einen neuen Vorgang mit den Daten der eingegangenen Nachricht an.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="2" anker="schritt-2" richtung="ausgehend" kopf={{"links": {"label": "LF", "eigen": true}, "rechts": {"label": "NB"}}}>

### Antwort

<Schrittskizze sicht={{"label": "LF"}} zeilen={[{"art": "ausloeser", "werte": ["START_VERSAND_ANTWORT_NNA"]}, {"art": "senden", "label": "NB", "weg": "AS4", "nachrichten": [{"nr": "33001", "titel": "Bestätigung"}, {"nr": "33003", "titel": "Strom Abweisung Kopf und Summe"}, {"nr": "33004", "titel": "Strom Abweisung Position"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [33001](/schnittstellen/202610/pruefi/REMADV/PI_33001) — Bestätigung · AS4
- [33003](/schnittstellen/202610/pruefi/REMADV/PI_33003) — Strom Abweisung Kopf und Summe · AS4
- [33004](/schnittstellen/202610/pruefi/REMADV/PI_33004) — Strom Abweisung Position · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="ausloeser">

**Prozessauslöser** [`START_VERSAND_ANTWORT_NNA`](/schnittstellen/202610/trigger/events/LF-START_VERSAND_ANTWORT_NNA) · [Im Playground ausprobieren](/api/202610/ausloeser-lf/start-versand-antwort-nna)

Das Backend stößt diesen Schritt mit diesem Ereignis an.

</li>

<li data-teil="nachricht">

Nachricht an **NB** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `33003` → [E_0406](/referenz/202610/ebd/E_0406) · LF · Netznutzungsrechnung prüfen

</div>

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202610/backend-schreiben-lf/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": false, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"AVIS\": [\n      {\n        \"avisNummer\": \"BGM555555\",\n        \"avisTyp\": \"ZAHLUNGSAVIS\",\n        \"boTyp\": \"AVIS\",\n        \"positionen\": [\n          {\n            \"gesamtBrutto\": {\n              \"waehrung\": \"EUR\",\n              \"wert\": 5000\n            },\n            \"istSelbstausgestellt\": false,\n            \"istStorno\": false,\n            \"rechnungsDatum\": \"2024-03-15T12:00:00Z\",\n            \"rechnungsNummer\": \"BGM56151515\",\n            \"zuZahlen\": {\n              \"waehrung\": \"EUR\",\n              \"wert\": 5000\n            }\n          }\n        ],\n        \"versionStruktur\": \"1\",\n        \"zuZahlen\": {\n          \"waehrung\": \"EUR\",\n          \"wert\": 5000\n        }\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9903790000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"datenaustauschreferenz\": \"197691\",\n    \"dokumentennummer\": \"BGM555555\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9900321000005\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"481\",\n    \"nachrichtendatum\": \"2024-04-03T12:00:00Z\",\n    \"nachrichtenreferenznummer\": \"617415\",\n    \"pruefidentifikator\": \"33001\",\n    \"sparte\": \"STROM\"\n  },\n  \"zusatzdaten\": {}\n}"} examples={[{"mediaType": "application/json", "examples": [{"name": "33001", "summary": "33001 — Bestätigung", "value": {"stammdaten": {"AVIS": [{"boTyp": "AVIS", "versionStruktur": "1", "avisNummer": "BGM555555", "avisTyp": "ZAHLUNGSAVIS", "positionen": [{"zuZahlen": {"wert": 5000, "waehrung": "EUR"}, "gesamtBrutto": {"wert": 5000, "waehrung": "EUR"}, "rechnungsNummer": "BGM56151515", "rechnungsDatum": "2024-03-15T12:00:00Z", "istStorno": false, "istSelbstausgestellt": false}], "zuZahlen": {"wert": 5000, "waehrung": "EUR"}}]}, "transaktionsdaten": {"datenaustauschreferenz": "197691", "sparte": "STROM", "pruefidentifikator": "33001", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9903790000002", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900321000005", "rollencodetyp": "BDEW"}, "dokumentennummer": "BGM555555", "kategorie": "481", "nachrichtendatum": "2024-04-03T12:00:00Z", "nachrichtenreferenznummer": "617415"}, "zusatzdaten": {}}}, {"name": "33003", "summary": "33003 — Strom Abweisung Kopf und Summe", "value": {"stammdaten": {"AVIS": [{"boTyp": "AVIS", "versionStruktur": "1", "avisNummer": "MSI5422", "avisTyp": "ABGELEHNTE_FORDERUNG", "positionen": [{"zuZahlen": {"wert": 10000, "waehrung": "EUR"}, "gesamtBrutto": {"wert": 0, "waehrung": "EUR"}, "abweichung": [{"abweichungsgrundCodeliste": "E_0407", "abweichungsgrundCode": "A80", "zugehoerigeRechnung": "1234567890"}], "rechnungsNummer": "458011", "rechnungsDatum": "2023-06-03T22:00:00Z", "istStorno": false, "istSelbstausgestellt": false, "referenz": "COMDIS-123"}], "zuZahlen": {"wert": 0, "waehrung": "EUR"}}]}, "transaktionsdaten": {"datenaustauschreferenz": "SEBAS126271264", "sparte": "STROM", "pruefidentifikator": "33003", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900051000002", "rollencodetyp": "BDEW", "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "nachname": "D BOWEN", "rufnummern": [{"nummerntyp": "RUF_DURCHWAHL", "rufnummer": "+004922271020"}]}}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9910046000008", "rollencodetyp": "BDEW"}, "dokumentennummer": "MSI5422", "kategorie": "239", "nachrichtendatum": "2024-04-01T22:00:00Z", "nachrichtenreferenznummer": "1", "vorgangsreferenznummer": "COMDIS-123"}, "zusatzdaten": {}}}, {"name": "33004", "summary": "33004 — Strom Abweisung Position", "value": {"stammdaten": {"AVIS": [{"boTyp": "AVIS", "versionStruktur": "1", "avisNummer": "YASMINJA436082BGM", "avisTyp": "ABGELEHNTE_FORDERUNG", "positionen": [{"zuZahlen": {"wert": 10000.0, "waehrung": "EUR"}, "gesamtBrutto": {"wert": 0, "waehrung": "EUR"}, "rechnungsNummer": "87897485", "rechnungsDatum": "2023-03-28T00:00:00Z", "istStorno": false, "istSelbstausgestellt": false, "positionen": [{"positionsnummer": 1, "abweichung": [{"abweichungsgrundCodeliste": "E_0406", "abweichungsgrundCode": "A20"}]}]}], "zuZahlen": {"wert": 0, "waehrung": "EUR"}}]}, "transaktionsdaten": {"datenaustauschreferenz": "YASMINJA219556", "sparte": "STROM", "pruefidentifikator": "33004", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9903790000002", "rollencodetyp": "BDEW", "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "nachname": "Fleeberg", "rufnummern": [{"nummerntyp": "RUF_DURCHWAHL", "rufnummer": "+03044848548"}]}}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9900321000005", "rollencodetyp": "BDEW"}, "dokumentennummer": "YASMINJA436082BGM", "kategorie": "239", "nachrichtendatum": "2024-04-01T11:26:00Z", "nachrichtenreferenznummer": "YASMINJA436082", "vorgangsreferenznummer": "545848485"}, "zusatzdaten": {}}}]}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend fort, nachdem die Nachricht erstellt ist.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="3" anker="schritt-3" richtung="eingehend" kopf={{"links": {"label": "LF", "eigen": true}, "rechts": {"label": "NB"}}}>

### Mitteilung, dass die ursprüngliche Netznutzungsrechnung korrekt war

<Schrittskizze sicht={{"label": "LF"}} zeilen={[{"art": "empfangen", "label": "NB", "weg": "AS4", "nachrichten": [{"nr": "29001", "titel": "Ablehnung REMADV"}]}, {"art": "aperak", "werte": ["Z33"]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [29001](/schnittstellen/202610/pruefi/COMDIS/PI_29001) — Ablehnung REMADV · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **NB** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `29001` → [E_0452](/referenz/202610/ebd/E_0452) · Nicht-Zahlungsavise prüfen

</div>

</li>

<li data-teil="aperak">

**Aperak-Prüfungen**
- `29001` → `Z33` — Aperak Prüfung: Ist referenzierte Nachricht bekannt ?

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202610/backend-schreiben-lf/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": false, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"HANDELSUNSTIMMIGKEIT\": [\n      {\n        \"begruendung\": {\n          \"grund\": \"SONSTIGES\",\n          \"hinweis\": \"BLABLA\"\n        },\n        \"boTyp\": \"HANDELSUNSTIMMIGKEIT\",\n        \"nummer\": \"ABC123456\",\n        \"typ\": \"HANDELSRECHNUNG\",\n        \"versionStruktur\": \"1\",\n        \"zuZahlen\": {\n          \"waehrung\": \"EUR\",\n          \"wert\": 10000\n        }\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"ansprechpartner\": {\n        \"boTyp\": \"ANSPRECHPARTNER\",\n        \"eMailAdresse\": \"x@x.de\",\n        \"nachname\": \"Max Mustermann\",\n        \"versionStruktur\": \"1\"\n      },\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9900321000005\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"antwortstatusCodeliste\": \"S_0109\",\n    \"datenaustauschreferenz\": \"115436\",\n    \"dokumentennummer\": \"272460BGM\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9903790000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"456\",\n    \"nachrichtendatum\": \"2024-04-03T13:21:00Z\",\n    \"nachrichtenreferenznummer\": \"272460\",\n    \"pruefidentifikator\": \"29001\",\n    \"sparte\": \"STROM\"\n  },\n  \"zusatzdaten\": {}\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend mit den Daten der eingegangenen Nachricht fort.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="4" anker="schritt-4" richtung="ausgehend" kopf={{"links": {"label": "LF", "eigen": true}, "rechts": {"label": "NB"}}}>

### Antwort

<Schrittskizze sicht={{"label": "LF"}} zeilen={[{"art": "ausloeser", "werte": ["START_VERSAND_ANTWORT_NNA"]}, {"art": "senden", "label": "NB", "weg": "AS4", "nachrichten": [{"nr": "33001", "titel": "Bestätigung"}, {"nr": "33003", "titel": "Strom Abweisung Kopf und Summe"}, {"nr": "33004", "titel": "Strom Abweisung Position"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [33001](/schnittstellen/202610/pruefi/REMADV/PI_33001) — Bestätigung · AS4
- [33003](/schnittstellen/202610/pruefi/REMADV/PI_33003) — Strom Abweisung Kopf und Summe · AS4
- [33004](/schnittstellen/202610/pruefi/REMADV/PI_33004) — Strom Abweisung Position · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="ausloeser">

**Prozessauslöser** [`START_VERSAND_ANTWORT_NNA`](/schnittstellen/202610/trigger/events/LF-START_VERSAND_ANTWORT_NNA) · [Im Playground ausprobieren](/api/202610/ausloeser-lf/start-versand-antwort-nna)

Das Backend stößt diesen Schritt mit diesem Ereignis an.

</li>

<li data-teil="nachricht">

Nachricht an **NB** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `33003` → [E_0407](/referenz/202610/ebd/E_0407) · LF · erneut Netznutzungsabrechnung prüfen

</div>

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202610/backend-schreiben-lf/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": false, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"AVIS\": [\n      {\n        \"avisNummer\": \"BGM555555\",\n        \"avisTyp\": \"ZAHLUNGSAVIS\",\n        \"boTyp\": \"AVIS\",\n        \"positionen\": [\n          {\n            \"gesamtBrutto\": {\n              \"waehrung\": \"EUR\",\n              \"wert\": 5000\n            },\n            \"istSelbstausgestellt\": false,\n            \"istStorno\": false,\n            \"rechnungsDatum\": \"2024-03-15T12:00:00Z\",\n            \"rechnungsNummer\": \"BGM56151515\",\n            \"zuZahlen\": {\n              \"waehrung\": \"EUR\",\n              \"wert\": 5000\n            }\n          }\n        ],\n        \"versionStruktur\": \"1\",\n        \"zuZahlen\": {\n          \"waehrung\": \"EUR\",\n          \"wert\": 5000\n        }\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9903790000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"datenaustauschreferenz\": \"197691\",\n    \"dokumentennummer\": \"BGM555555\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9900321000005\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"481\",\n    \"nachrichtendatum\": \"2024-04-03T12:00:00Z\",\n    \"nachrichtenreferenznummer\": \"617415\",\n    \"pruefidentifikator\": \"33001\",\n    \"sparte\": \"STROM\"\n  },\n  \"zusatzdaten\": {}\n}"} examples={[{"mediaType": "application/json", "examples": [{"name": "33001", "summary": "33001 — Bestätigung", "value": {"stammdaten": {"AVIS": [{"boTyp": "AVIS", "versionStruktur": "1", "avisNummer": "BGM555555", "avisTyp": "ZAHLUNGSAVIS", "positionen": [{"zuZahlen": {"wert": 5000, "waehrung": "EUR"}, "gesamtBrutto": {"wert": 5000, "waehrung": "EUR"}, "rechnungsNummer": "BGM56151515", "rechnungsDatum": "2024-03-15T12:00:00Z", "istStorno": false, "istSelbstausgestellt": false}], "zuZahlen": {"wert": 5000, "waehrung": "EUR"}}]}, "transaktionsdaten": {"datenaustauschreferenz": "197691", "sparte": "STROM", "pruefidentifikator": "33001", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9903790000002", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900321000005", "rollencodetyp": "BDEW"}, "dokumentennummer": "BGM555555", "kategorie": "481", "nachrichtendatum": "2024-04-03T12:00:00Z", "nachrichtenreferenznummer": "617415"}, "zusatzdaten": {}}}, {"name": "33003", "summary": "33003 — Strom Abweisung Kopf und Summe", "value": {"stammdaten": {"AVIS": [{"boTyp": "AVIS", "versionStruktur": "1", "avisNummer": "MSI5422", "avisTyp": "ABGELEHNTE_FORDERUNG", "positionen": [{"zuZahlen": {"wert": 10000, "waehrung": "EUR"}, "gesamtBrutto": {"wert": 0, "waehrung": "EUR"}, "abweichung": [{"abweichungsgrundCodeliste": "E_0407", "abweichungsgrundCode": "A80", "zugehoerigeRechnung": "1234567890"}], "rechnungsNummer": "458011", "rechnungsDatum": "2023-06-03T22:00:00Z", "istStorno": false, "istSelbstausgestellt": false, "referenz": "COMDIS-123"}], "zuZahlen": {"wert": 0, "waehrung": "EUR"}}]}, "transaktionsdaten": {"datenaustauschreferenz": "SEBAS126271264", "sparte": "STROM", "pruefidentifikator": "33003", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900051000002", "rollencodetyp": "BDEW", "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "nachname": "D BOWEN", "rufnummern": [{"nummerntyp": "RUF_DURCHWAHL", "rufnummer": "+004922271020"}]}}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9910046000008", "rollencodetyp": "BDEW"}, "dokumentennummer": "MSI5422", "kategorie": "239", "nachrichtendatum": "2024-04-01T22:00:00Z", "nachrichtenreferenznummer": "1", "vorgangsreferenznummer": "COMDIS-123"}, "zusatzdaten": {}}}, {"name": "33004", "summary": "33004 — Strom Abweisung Position", "value": {"stammdaten": {"AVIS": [{"boTyp": "AVIS", "versionStruktur": "1", "avisNummer": "YASMINJA436082BGM", "avisTyp": "ABGELEHNTE_FORDERUNG", "positionen": [{"zuZahlen": {"wert": 10000.0, "waehrung": "EUR"}, "gesamtBrutto": {"wert": 0, "waehrung": "EUR"}, "rechnungsNummer": "87897485", "rechnungsDatum": "2023-03-28T00:00:00Z", "istStorno": false, "istSelbstausgestellt": false, "positionen": [{"positionsnummer": 1, "abweichung": [{"abweichungsgrundCodeliste": "E_0406", "abweichungsgrundCode": "A20"}]}]}], "zuZahlen": {"wert": 0, "waehrung": "EUR"}}]}, "transaktionsdaten": {"datenaustauschreferenz": "YASMINJA219556", "sparte": "STROM", "pruefidentifikator": "33004", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9903790000002", "rollencodetyp": "BDEW", "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "nachname": "Fleeberg", "rufnummern": [{"nummerntyp": "RUF_DURCHWAHL", "rufnummer": "+03044848548"}]}}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9900321000005", "rollencodetyp": "BDEW"}, "dokumentennummer": "YASMINJA436082BGM", "kategorie": "239", "nachrichtendatum": "2024-04-01T11:26:00Z", "nachrichtenreferenznummer": "YASMINJA436082", "vorgangsreferenznummer": "545848485"}, "zusatzdaten": {}}}]}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend fort, nachdem die Nachricht erstellt ist.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="5" anker="schritt-5" richtung="eingehend" kopf={{"links": {"label": "LF", "eigen": true}, "rechts": {"label": "NB"}}}>

### Storno der ursprünglichen Rechnung

<Schrittskizze sicht={{"label": "LF"}} zeilen={[{"art": "empfangen", "label": "NB", "weg": "AS4", "nachrichten": [{"nr": "31004", "titel": "Stornorechnung"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [31004](/schnittstellen/202610/pruefi/INVOIC/PI_31004) — Stornorechnung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **NB** · AS4

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202610/backend-schreiben-lf/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": false, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend mit den Daten der eingegangenen Nachricht fort.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="6" anker="schritt-6" richtung="ausgehend" kopf={{"links": {"label": "LF", "eigen": true}, "rechts": {"label": "NB"}}}>

### Antwort

<Schrittskizze sicht={{"label": "LF"}} zeilen={[{"art": "ausloeser", "werte": ["START_VERSAND_ANTWORT_NNA"]}, {"art": "senden", "label": "NB", "weg": "AS4", "nachrichten": [{"nr": "33001", "titel": "Bestätigung"}, {"nr": "33002", "titel": "Abweisung"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [33001](/schnittstellen/202610/pruefi/REMADV/PI_33001) — Bestätigung · AS4
- [33002](/schnittstellen/202610/pruefi/REMADV/PI_33002) — Abweisung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="ausloeser">

**Prozessauslöser** [`START_VERSAND_ANTWORT_NNA`](/schnittstellen/202610/trigger/events/LF-START_VERSAND_ANTWORT_NNA) · [Im Playground ausprobieren](/api/202610/ausloeser-lf/start-versand-antwort-nna)

Das Backend stößt diesen Schritt mit diesem Ereignis an.

</li>

<li data-teil="nachricht">

Nachricht an **NB** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `33002` → [E_0459](/referenz/202610/ebd/E_0459) · LF · Prüfen, ob Antwort auf Stornierung erforderlich

</div>

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202610/backend-schreiben-lf/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": false, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"AVIS\": [\n      {\n        \"avisNummer\": \"BGM555555\",\n        \"avisTyp\": \"ZAHLUNGSAVIS\",\n        \"boTyp\": \"AVIS\",\n        \"positionen\": [\n          {\n            \"gesamtBrutto\": {\n              \"waehrung\": \"EUR\",\n              \"wert\": 5000\n            },\n            \"istSelbstausgestellt\": false,\n            \"istStorno\": false,\n            \"rechnungsDatum\": \"2024-03-15T12:00:00Z\",\n            \"rechnungsNummer\": \"BGM56151515\",\n            \"zuZahlen\": {\n              \"waehrung\": \"EUR\",\n              \"wert\": 5000\n            }\n          }\n        ],\n        \"versionStruktur\": \"1\",\n        \"zuZahlen\": {\n          \"waehrung\": \"EUR\",\n          \"wert\": 5000\n        }\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9903790000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"datenaustauschreferenz\": \"197691\",\n    \"dokumentennummer\": \"BGM555555\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9900321000005\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"481\",\n    \"nachrichtendatum\": \"2024-04-03T12:00:00Z\",\n    \"nachrichtenreferenznummer\": \"617415\",\n    \"pruefidentifikator\": \"33001\",\n    \"sparte\": \"STROM\"\n  },\n  \"zusatzdaten\": {}\n}"} examples={[{"mediaType": "application/json", "examples": [{"name": "33001", "summary": "33001 — Bestätigung", "value": {"stammdaten": {"AVIS": [{"boTyp": "AVIS", "versionStruktur": "1", "avisNummer": "BGM555555", "avisTyp": "ZAHLUNGSAVIS", "positionen": [{"zuZahlen": {"wert": 5000, "waehrung": "EUR"}, "gesamtBrutto": {"wert": 5000, "waehrung": "EUR"}, "rechnungsNummer": "BGM56151515", "rechnungsDatum": "2024-03-15T12:00:00Z", "istStorno": false, "istSelbstausgestellt": false}], "zuZahlen": {"wert": 5000, "waehrung": "EUR"}}]}, "transaktionsdaten": {"datenaustauschreferenz": "197691", "sparte": "STROM", "pruefidentifikator": "33001", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9903790000002", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900321000005", "rollencodetyp": "BDEW"}, "dokumentennummer": "BGM555555", "kategorie": "481", "nachrichtendatum": "2024-04-03T12:00:00Z", "nachrichtenreferenznummer": "617415"}, "zusatzdaten": {}}}, {"name": "33002", "summary": "33002 — Abweisung", "value": {"stammdaten": {"AVIS": [{"boTyp": "AVIS", "versionStruktur": "1", "avisNummer": "BGM12345", "avisTyp": "ABGELEHNTE_FORDERUNG", "positionen": [{"zuZahlen": {"wert": 5000, "waehrung": "EUR"}, "gesamtBrutto": {"wert": 0, "waehrung": "EUR"}, "abweichung": [{"abweichungsgrundBemerkung1": "Rechnung entspricht nicht §14 UstG", "abweichungsgrundCodeliste": "E_0503", "abweichungsgrundCode": "A01"}, {"abweichungsgrundCodeliste": "E_0506", "abweichungsgrundCode": "A04"}], "rechnungsNummer": "BGM111111111", "rechnungsDatum": "2024-03-01T12:00:00Z", "istStorno": false, "istSelbstausgestellt": false, "referenz": "ABC123456"}, {"zuZahlen": {"wert": 7000, "waehrung": "EUR"}, "gesamtBrutto": {"wert": 0, "waehrung": "EUR"}, "abweichung": [{"abweichungsgrundBemerkung1": "Blabla", "abweichungsgrundCodeliste": "E_0503", "abweichungsgrundCode": "A01"}], "rechnungsNummer": "BGM235555", "rechnungsDatum": "2024-03-01T12:00:00Z", "istStorno": false, "istSelbstausgestellt": false}], "zuZahlen": {"wert": 0, "waehrung": "EUR"}}]}, "transaktionsdaten": {"datenaustauschreferenz": "166216", "sparte": "STROM", "pruefidentifikator": "33002", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9903790000002", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900321000005", "rollencodetyp": "BDEW"}, "dokumentennummer": "BGM12345", "kategorie": "239", "nachrichtendatum": "2024-04-03T11:48:00Z", "nachrichtenreferenznummer": "494930", "vorgangsreferenznummer": "ABC123456"}, "zusatzdaten": {}}}]}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

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
| [E_0406](/referenz/202610/ebd/E_0406) | Netznutzungsrechnung prüfen |
| [E_0407](/referenz/202610/ebd/E_0407) | erneut Netznutzungsabrechnung prüfen |
| [E_0452](/referenz/202610/ebd/E_0452) | Nicht-Zahlungsavise prüfen |
| [E_0459](/referenz/202610/ebd/E_0459) | Prüfen, ob Antwort auf Stornierung erforderlich |

</details>

<a id="abschnitt-informationen"></a>

## Prozess-Informationen

Wortlaut der Lesefassung, Steckbrief Kap. 3.3.1, S. 87–89.

<Stepper>
<ol>

<li data-blatt="vorbedingungen">

### Vorbedingungen

- Es handelt sich um eine verbrauchende Marktlokation.
- Die aktuellen Netznutzungsentgelte sind vom NB veröffentlicht und wurden im Rahmen des Use Cases „[Übermittlung Preisblatt NB an LF](/prozessdoku/202610/LF/GPKE-Teil2-uebermittlung-preisblatt-nb-an-lf)“ im Preisblatt Netznutzung an den LF übermittelt
- Der LF ist der Marktlokation zugeordnet.
- Die Netznutzungsrechnung enthält nur Positionen, die
  - als Artikel-ID im Preisblatt Netznutzung enthalten sind oder
  - als Zu-/Abschlag zu einer Artikel-ID des Preisblatts Netznutzung des NB vorab im Rahmen des Use-Cases „[Abrechnungsdaten Netznutzungsabrechnung](/prozessdoku/202610/LF/GPKE-Teil2-abrechnungsdaten-netznutzungsabrechnung)“ übermittelt wurden.
- Die für die Netznutzungsabrechnung notwendigen Informationen wurden über den Use-Case „[Abrechnungsdaten Netznutzungsabrechnung](/prozessdoku/202610/LF/GPKE-Teil2-abrechnungsdaten-netznutzungsabrechnung)“ übermittelt.
- Die Abrechnung der Netznutzung ist fällig (Turnus-, Abschlags- oder Schlussrechnung bzw. ereignisgesteuert).
- Der Lieferschein wurde vorher übermittelt (außer bei Abschlagsrechnungen) und im Fall der Ablehnung mit konkretem Grund durch den LF, wurde die Reklamation vom NB entkräftet.
- Der LF ist Zahler der Netznutzung.

</li>

<li data-blatt="ergebnisse">

### Ergebnisse

Der LF wird die vom NB gestellte Netznutzungsrechnung bezahlen.

</li>

<li data-blatt="fehlerfall">

### Fehlerfall

#### Fehlerfälle

- Die Netznutzungsrechnung enthält Positionen, die nicht
  - als Artikel-ID im Preisblatt Netznutzung des NB enthalten sind oder
  - als Zu-/Abschlag zu einer Artikel-ID des Preisblatts Netznutzung des NB vorab im Rahmen des Use-Cases „[Abrechnungsdaten Netznutzungsabrechnung](/prozessdoku/202610/LF/GPKE-Teil2-abrechnungsdaten-netznutzungsabrechnung)“ übermittelt wurden.
- Die für die Netznutzungsabrechnung notwendigen Informationen wurden nicht über den Use-Case „[Abrechnungsdaten Netznutzungsabrechnung](/prozessdoku/202610/LF/GPKE-Teil2-abrechnungsdaten-netznutzungsabrechnung)“ übermittelt.
- Die für die Netznutzungsabrechnung notwendigen Informationen wurden über den Use-Case „[Abrechnungsdaten Netznutzungsabrechnung](/prozessdoku/202610/LF/GPKE-Teil2-abrechnungsdaten-netznutzungsabrechnung)“ übermittelt, wurden jedoch in der Netznutzungsrechnung nicht entsprechend berücksichtigt.
- Die Abrechnungsenergiemengen/Leistungswerte der Netznutzungsrechnung entsprechen nicht denen des Lieferscheins.
- Der in der Netznutzungsrechnung angegebene Preis einer Artikel-ID entspricht nicht dem im Preisblatt Netznutzung des NB angegebenen Preis der entsprechenden Artikel-ID.

</li>

<li data-blatt="anforderungen">

### Weitere Anforderungen

- Der Fall einer reklamierten oder sich als falsch erweisenden Netznutzungsrechnung (Storno der ursprünglichen Rechnung wird ohne vorherige Reklamation des LF oder auf Grund einer vorherigen Reklamation des LF durchgeführt) stellt einen Teil des Regelprozesses dar und muss abgesehen von Klärungen vollumfänglich automatisch abgewickelt werden. Im Reklamationsfall kommt das sog. „Alles-oder-Nichts-Prinzip“ zur Anwendung, nach dem eine Rechnung entweder vollumfänglich als richtig akzeptiert oder vollumfänglich abgelehnt wird. Im Fall einer sich falsch erweisenden Netznutzungsrechnung (Storno der ursprünglichen Rechnung wird ohne vorherige Reklamation des LF oder auf Grund einer vorherigen Reklamation des LF durchgeführt) ist in diesem Zusammenhang auch der korrespondierende Lieferschein zu stornieren und ein korrigierter Lieferschein vor dem Versand der neuen Rechnung an den LF zu übermitteln, sofern die Korrektur der Abrechnungsenergie-mengen/Leistungswerte notwendig ist. Die im Konfliktfall abzuwickelnden Prozesse im Rahmen des Forderungsmanagements bzw. Mahnablaufs sind nicht dargestellt und sind bilateral zu lösen.
- Die Netznutzungsrechnung kann eindeutig über eine Referenz dem zuvor ausgetauschten Lieferschein zugeordnet werden.
- Die Schlussrechnung/ Jahresrechnung weist nachvollziehbar alle enthaltenen Abschlagsrechnungen der Abrechnungsperiode unter Bezeichnung der Rechnungsnummer aus.
- Eine Position in der Netznutzungsrechnung muss durch eine Position oder durch Addition von mehreren Positionen aus dem Lieferschein zeitlich eindeutig zugeordnet und geprüft werden können.

</li>

<li data-blatt="erste-nachricht">

### Erste Nachricht

**NB** sendet „Netznutzungsrechnung“ (Schritt 1). Ab hier ist der Beteiligte dieser Seite am Zug.

</li>

<li data-blatt="ziel">

### Ziel

Der NB ist informiert, dass der LF die Netznutzungsrechnung akzeptiert.

</li>

</ol>
</Stepper>

<a id="abschnitt-sichten"></a>

## Andere Sichten des Prozesses

Derselbe Prozess, aus den Augen der anderen Beteiligten: dieselben Schritte, jeweils aus deren Sicht gelesen.

- [Sicht NB](/prozessdoku/202610/NB/GPKE-Teil2-netznutzungsabrechnung) — NB

<Hinweisbereich>

*Die Schritte sind die **möglichen** Nachrichten dieses Prozesses, keine Abfolge — die Quelle führt weder Bedingungen noch Alternativen. Das Kästchen am Schritt nennt links die eigene Sicht: **←** empfängt sie, **→** sendet sie. Zugeklappte Schritte laufen zwischen anderen Marktpartnern.*

Zu den Prüfidentifikatoren dieser Schritte liegt kein Testfall im Testbestand; der Knopf »Ausprobieren« der schreibenden Schnittstelle bietet deshalb keinen Rumpf an.

Betrifft: [5](#schritt-5)

</Hinweisbereich>
