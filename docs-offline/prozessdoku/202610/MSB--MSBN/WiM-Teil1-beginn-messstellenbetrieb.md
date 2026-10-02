# Beginn Messstellenbetrieb — Sicht MSBN

<Kopf rolle="MSB" beteiligter="MSBN" festlegung="WiM" dokument="WiM Strom Teil 1" kapitel="2.3.2" sparte="Strom" schritte={11} suchtitel="Beginn Messstellenbetrieb — Sicht MSBN (Marktrolle MSB) · WiM Strom Teil 1 · Formatversion 202610" abschnitte={[{"id": "abschnitt-ablauf", "label": "Prozessablauf"}, {"id": "abschnitt-schritte", "label": "Prozessschritte"}, {"id": "abschnitt-informationen", "label": "Prozess-Informationen"}, {"id": "abschnitt-sichten", "label": "Andere Sichten des Prozesses"}]} />

<Kurzfassung>

Der Prozess beschreibt die Interaktionen zwischen den Marktteilnehmern für den Fall, dass eine einzelne Messlokation dem anmeldenden MSB für die Durchführung des Messstellenbetriebes zugeordnet werden soll. Dies gilt insbesondere, wenn
- es sich um die erstmalige Inbetriebnahme oder um die Wiederinbetriebnahme einer einzelnen Messlokation handelt,
- der Messstellenbetrieb für diese Messlokation erstmals einem wMSB zugeordnet werden soll oder
- die einzelne Messlokation einem anderen als dem bisherigen MSB zugeordnet werden soll.

</Kurzfassung>

<a id="abschnitt-ablauf"></a>

## Prozessablauf aus Sicht des MSB (MSBN)

<Systembild svg={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1004 1303\" width=\"1004\" height=\"1303\" role=\"img\" aria-labelledby=\"sb-title\" class=\"maco-systembild\">\n<title id=\"sb-title\">Systembild: Beginn Messstellenbetrieb aus Sicht MSB</title>\n<defs><marker id=\"sb-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect class=\"sb-lane-kopf\" x=\"16\" y=\"12\" width=\"232\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend-System des Kunden</text>\n<rect class=\"sb-lane-kopf\" x=\"398\" y=\"12\" width=\"264\" height=\"46\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · MSBN</text>\n<rect class=\"sb-lane-kopf\" x=\"812\" y=\"12\" width=\"176\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"900\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Marktpartner</text>\n<line x1=\"323\" y1=\"58\" x2=\"323\" y2=\"1291\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"737\" y1=\"58\" x2=\"737\" y2=\"1291\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect class=\"sb-kasten sb-trigger\" x=\"432\" y=\"80\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessauslöser empfangen</text>\n<rect class=\"sb-kasten sb-backend sb-trigger\" x=\"34\" y=\"80\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">START_BEGINN_MSB</text>\n<line x1=\"230\" y1=\"96\" x2=\"432\" y2=\"96\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"88\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"144\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"164\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">1. Anmeldung</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"113\" x2=\"530\" y2=\"144\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"142\" r=\"5\"/><line x1=\"900\" y1=\"147\" x2=\"900\" y2=\"159\"/><line x1=\"893\" y1=\"151\" x2=\"907\" y2=\"151\"/><line x1=\"900\" y1=\"159\" x2=\"894\" y2=\"169\"/><line x1=\"900\" y1=\"159\" x2=\"906\" y2=\"169\"/></g>\n<text x=\"900\" y=\"191\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"628\" y1=\"160\" x2=\"878\" y2=\"160\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"152\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"176\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">55042</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"227\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"247\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"177\" x2=\"530\" y2=\"227\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"227\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"247\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"243\" x2=\"230\" y2=\"243\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"235\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"291\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"311\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">2. Antwort auf Anmeldung</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"260\" x2=\"530\" y2=\"291\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"289\" r=\"5\"/><line x1=\"900\" y1=\"294\" x2=\"900\" y2=\"306\"/><line x1=\"893\" y1=\"298\" x2=\"907\" y2=\"298\"/><line x1=\"900\" y1=\"306\" x2=\"894\" y2=\"316\"/><line x1=\"900\" y1=\"306\" x2=\"906\" y2=\"316\"/></g>\n<text x=\"900\" y=\"338\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"878\" y1=\"307\" x2=\"628\" y2=\"307\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"299\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"323\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">55043, 55044</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"374\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"394\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z33</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"324\" x2=\"530\" y2=\"374\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"438\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"458\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"407\" x2=\"530\" y2=\"438\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"438\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"458\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"454\" x2=\"230\" y2=\"454\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"446\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-lesen\" x=\"432\" y=\"502\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"522\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Daten für die Prüfung laden</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"471\" x2=\"530\" y2=\"502\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-lesen\" x=\"34\" y=\"502\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"522\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Messlokation lesen</text>\n<line x1=\"432\" y1=\"518\" x2=\"230\" y2=\"518\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"510\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"566\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"586\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">7. Mitteilung über</text>\n<text x=\"530\" y=\"601\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Gesamtvorgang</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"535\" x2=\"530\" y2=\"566\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"572\" r=\"5\"/><line x1=\"900\" y1=\"577\" x2=\"900\" y2=\"589\"/><line x1=\"893\" y1=\"581\" x2=\"907\" y2=\"581\"/><line x1=\"900\" y1=\"589\" x2=\"894\" y2=\"599\"/><line x1=\"900\" y1=\"589\" x2=\"906\" y2=\"599\"/></g>\n<text x=\"900\" y=\"621\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"628\" y1=\"590\" x2=\"878\" y2=\"590\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"582\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"606\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">21009, 21010</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"649\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"669\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"614\" x2=\"530\" y2=\"649\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"649\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"669\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"665\" x2=\"230\" y2=\"665\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"657\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"713\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"733\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">8. Antwort auf Mitteilung</text>\n<text x=\"530\" y=\"748\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">über Gesamtvorgang</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"682\" x2=\"530\" y2=\"713\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"719\" r=\"5\"/><line x1=\"900\" y1=\"724\" x2=\"900\" y2=\"736\"/><line x1=\"893\" y1=\"728\" x2=\"907\" y2=\"728\"/><line x1=\"900\" y1=\"736\" x2=\"894\" y2=\"746\"/><line x1=\"900\" y1=\"736\" x2=\"906\" y2=\"746\"/></g>\n<text x=\"900\" y=\"768\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"878\" y1=\"737\" x2=\"628\" y2=\"737\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"729\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"753\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">21011, 21012</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"796\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"816\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z33</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"761\" x2=\"530\" y2=\"796\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"860\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"880\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"829\" x2=\"530\" y2=\"860\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"860\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"880\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"876\" x2=\"230\" y2=\"876\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"868\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-lesen\" x=\"432\" y=\"924\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"944\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Daten für die Prüfung laden</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"893\" x2=\"530\" y2=\"924\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-lesen\" x=\"34\" y=\"924\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"944\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Messlokation lesen</text>\n<line x1=\"432\" y1=\"940\" x2=\"230\" y2=\"940\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"932\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"988\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1008\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">16. Mitteilung über das</text>\n<text x=\"530\" y=\"1023\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Scheitern des</text>\n<text x=\"530\" y=\"1038\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Gesamtvorgangs</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"957\" x2=\"530\" y2=\"988\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"1001\" r=\"5\"/><line x1=\"900\" y1=\"1006\" x2=\"900\" y2=\"1018\"/><line x1=\"893\" y1=\"1010\" x2=\"907\" y2=\"1010\"/><line x1=\"900\" y1=\"1018\" x2=\"894\" y2=\"1028\"/><line x1=\"900\" y1=\"1018\" x2=\"906\" y2=\"1028\"/></g>\n<text x=\"900\" y=\"1050\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"878\" y1=\"1019\" x2=\"628\" y2=\"1019\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"1011\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"1035\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">21013, 21013</text>\n<rect class=\"sb-kasten sb-aperak_lesen\" x=\"432\" y=\"1077\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1097\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Daten für die</text>\n<text x=\"530\" y=\"1112\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Eingangsprüfung laden</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1051\" x2=\"530\" y2=\"1077\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-aperak_lesen\" x=\"34\" y=\"1085\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"1105\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Messlokation lesen</text>\n<line x1=\"432\" y1=\"1101\" x2=\"230\" y2=\"1101\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"1093\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"1151\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1171\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z10, Z17, Z18</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1125\" x2=\"530\" y2=\"1151\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"1215\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1235\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1184\" x2=\"530\" y2=\"1215\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"1215\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"1235\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"1231\" x2=\"230\" y2=\"1231\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"1223\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n</svg>"} gesamt={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1218 1168\" width=\"1218\" height=\"1168\" role=\"img\" aria-labelledby=\"sd-title\" class=\"maco-sequence\">\n<title id=\"sd-title\">Sequenzdiagramm: Beginn Messstellenbetrieb aus Sicht MSB</title>\n<defs><marker id=\"sd-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect x=\"16\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"121\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend (Kunde)</text>\n<line x1=\"121\" y1=\"64\" x2=\"121\" y2=\"1156\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"260\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"365\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · MSBN</text>\n<line x1=\"365\" y1=\"64\" x2=\"365\" y2=\"1156\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"504\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"609\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"609\" y1=\"64\" x2=\"609\" y2=\"1156\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"748\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"853\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">MSBA</text>\n<line x1=\"853\" y1=\"64\" x2=\"853\" y2=\"1156\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"992\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"1097\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">LF</text>\n<line x1=\"1097\" y1=\"64\" x2=\"1097\" y2=\"1156\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"121\" y1=\"90\" x2=\"365\" y2=\"90\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"81\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">START_BEGINN_MSB</text>\n<text x=\"243\" y=\"105\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Trigger-Event</text>\n<line x1=\"365\" y1=\"152\" x2=\"609\" y2=\"152\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"143\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">1. Anmeldung</text>\n<text x=\"487\" y=\"167\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55042</text>\n<line x1=\"365\" y1=\"214\" x2=\"121\" y2=\"214\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"205\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"229\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"609\" y1=\"276\" x2=\"365\" y2=\"276\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"267\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">2. Antwort auf Anmeldung</text>\n<text x=\"487\" y=\"291\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55043, 55044 · E_0201</text>\n<text x=\"487\" y=\"304\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0201 — Anmeldung Messstellenbetrieb prüfen</text>\n<line x1=\"365\" y1=\"338\" x2=\"121\" y2=\"338\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"329\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"353\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"609\" y1=\"400\" x2=\"853\" y2=\"400\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"731\" y=\"391\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">3. Information über vorläufige Anmeldebestätigung</text>\n<text x=\"731\" y=\"415\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 21007</text>\n<line x1=\"609\" y1=\"462\" x2=\"1097\" y2=\"462\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"853\" y=\"453\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">4. Information über vorläufige Anmeldebestätigung</text>\n<text x=\"853\" y=\"477\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 21007</text>\n<line x1=\"365\" y1=\"524\" x2=\"609\" y2=\"524\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"515\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">7. Mitteilung über Gesamtvorgang</text>\n<text x=\"487\" y=\"539\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 21009, 21010</text>\n<line x1=\"365\" y1=\"586\" x2=\"121\" y2=\"586\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"577\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"601\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"609\" y1=\"648\" x2=\"365\" y2=\"648\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"639\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">8. Antwort auf Mitteilung über Gesamtvorgang</text>\n<text x=\"487\" y=\"663\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 21011, 21012 · E_0232</text>\n<text x=\"487\" y=\"676\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0232 — Mitteilung über Gesamtvorgang prüfen</text>\n<line x1=\"365\" y1=\"710\" x2=\"121\" y2=\"710\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"701\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"725\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"609\" y1=\"772\" x2=\"853\" y2=\"772\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"731\" y=\"763\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">14. Information über Scheitern der Zuordnung</text>\n<text x=\"731\" y=\"787\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 21011 · E_0232</text>\n<text x=\"731\" y=\"800\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0232 — Mitteilung über Gesamtvorgang prüfen</text>\n<line x1=\"609\" y1=\"834\" x2=\"1097\" y2=\"834\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"853\" y=\"825\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">15. Information über Scheitern der Zuordnung</text>\n<text x=\"853\" y=\"849\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 21011 · E_0232</text>\n<text x=\"853\" y=\"862\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0232 — Mitteilung über Gesamtvorgang prüfen</text>\n<line x1=\"609\" y1=\"896\" x2=\"365\" y2=\"896\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"887\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">16. Mitteilung über das Scheitern des Gesamtvorga…</text>\n<text x=\"487\" y=\"911\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 21013, 21013</text>\n<line x1=\"365\" y1=\"958\" x2=\"121\" y2=\"958\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"949\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"973\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"609\" y1=\"1020\" x2=\"853\" y2=\"1020\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"731\" y=\"1011\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">17. Information über Scheitern der Zuordnung</text>\n<text x=\"731\" y=\"1035\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 21013</text>\n<line x1=\"609\" y1=\"1082\" x2=\"1097\" y2=\"1082\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"853\" y=\"1073\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">18. Information über Scheitern der Zuordnung</text>\n<text x=\"853\" y=\"1097\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 21013</text>\n</svg>"} titel="MSBN" />

<a id="abschnitt-schritte"></a>

## Prozessschritte

<Schritt nr="1" anker="schritt-1" richtung="ausgehend" kopf={{"links": {"label": "MSBN", "eigen": true}, "rechts": {"label": "NB"}}}>

### Anmeldung

<Schrittskizze sicht={{"label": "MSBN"}} zeilen={[{"art": "ausloeser", "werte": ["START_BEGINN_MSB"]}, {"art": "senden", "label": "NB", "weg": "AS4", "nachrichten": [{"nr": "55042", "titel": "Anmeldung MSB"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55042](/schnittstellen/202610/pruefi/UTILMD/PI_55042) — Anmeldung MSB · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="ausloeser">

**Prozessauslöser** [`START_BEGINN_MSB`](/schnittstellen/202610/trigger/events/MSB-START_BEGINN_MSB) · [Im Playground ausprobieren](/api/202610/ausloeser-msb/start-beginn-msb)

Das Backend stößt diesen Schritt mit diesem Ereignis an.

</li>

<li data-teil="nachricht">

Nachricht an **NB** · AS4

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202610/backend-schreiben-msb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"MESSLOKATION\": [\n      {\n        \"ablesekartenempfaenger\": {\n          \"boTyp\": \"GESCHAEFTSPARTNER\",\n          \"geschaeftspartnerrolle\": [\n            \"ABLESEKARTENEMPFAENGER\"\n          ],\n          \"gewerbekennzeichnung\": false,\n          \"name1\": \"Mustermann\",\n          \"partneradresse\": {\n            \"hausnummer\": \"1\",\n            \"landescode\": \"DE\",\n            \"ort\": \"Ort\",\n            \"postleitzahl\": \"12345\",\n            \"strasse\": \"Str\"\n          },\n          \"versionStruktur\": \"1\"\n        },\n        \"boTyp\": \"MESSLOKATION\",\n        \"messlokationsId\": \"DE0032106765712000000000000000037\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"MESSSTELLENBETRIEBSVERTRAG\": [\n      {\n        \"boTyp\": \"VERTRAG\",\n        \"korrespondenzpartner\": {\n          \"ansprechpartner\": {\n            \"boTyp\": \"ANSPRECHPARTNER\",\n            \"eMailAdresse\": \"max@mustermann.de\",\n            \"versionStruktur\": \"1\"\n          },\n          \"boTyp\": \"GESCHAEFTSPARTNER\",\n          \"gewerbekennzeichnung\": false,\n          \"name1\": \"Mustermann\",\n          \"partneradresse\": {\n            \"hausnummer\": \"1\",\n            \"landescode\": \"DE\",\n            \"ort\": \"Ort\",\n            \"postleitzahl\": \"12345\",\n            \"strasse\": \"Str\"\n          },\n          \"versionStruktur\": \"1\"\n        },\n        \"lokationsId\": \"DE0032106765712000000000000000037\",\n        \"lokationsTyp\": \"MELO\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\",\n        \"vertragsart\": \"MESSSTELLENBETRIEBSVERTRAG\",\n        \"vertragskonditionen\": {\n          \"beauftragungMsb\": \"VERTRAG_AN_MSB\"\n        },\n        \"vertragspartner2\": [\n          {\n            \"boTyp\": \"GESCHAEFTSPARTNER\",\n            \"geschaeftspartnerrolle\": [\n              \"KUNDE\"\n            ],\n            \"gewerbekennzeichnung\": false,\n            \"name1\": \"Mustermann\",\n            \"versionStruktur\": \"1\"\n          }\n        ]\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9904446000007\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"datenaustauschreferenz\": \"948706\",\n    \"datumleistungsbeginn\": \"2026-06-30T22:00:00Z\",\n    \"dokumentennummer\": \"664913BGM\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9900321000005\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"E01\",\n    \"nachrichtendatum\": \"2026-10-02T11:00:00Z\",\n    \"nachrichtenreferenznummer\": \"664913\",\n    \"pruefidentifikator\": \"55042\",\n    \"sparte\": \"STROM\",\n    \"transaktionsgrund\": \"E03\",\n    \"vorgangsnummer\": \"1587543437\"\n  }\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend fort, nachdem die Nachricht erstellt ist.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="2" anker="schritt-2" richtung="eingehend" kopf={{"links": {"label": "MSBN", "eigen": true}, "rechts": {"label": "NB"}}}>

### Antwort auf Anmeldung

<Schrittskizze sicht={{"label": "MSBN"}} zeilen={[{"art": "empfangen", "label": "NB", "weg": "AS4", "nachrichten": [{"nr": "55043", "titel": "Bestätigung Anmeldung MSB"}, {"nr": "55044", "titel": "Ablehnung Anmeldung MSB"}]}, {"art": "aperak", "werte": ["Z33"]}, {"art": "fortschreiben"}, {"art": "lesen_ebd", "schnittstellen": [{"label": "Messlokation lesen"}]}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) — Bestätigung Anmeldung MSB · AS4
- [55044](/schnittstellen/202610/pruefi/UTILMD/PI_55044) — Ablehnung Anmeldung MSB · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **NB** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `55043`, `55044` → [E_0201](/referenz/202610/ebd/E_0201) · Anmeldung Messstellenbetrieb prüfen

</div>

</li>

<li data-teil="aperak">

**Aperak-Prüfungen**
- `55043`, `55044` → `Z33`

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202610/backend-schreiben-msb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"BILANZIERUNG\": [\n      {\n        \"abwicklungsmodell\": \"MODELL_1_BILANZIERUNG_AN_MARKTLOKATION\",\n        \"aggregationsverantwortung\": \"VNB\",\n        \"boTyp\": \"BILANZIERUNG\",\n        \"marktlokationsId\": \"50363191616\",\n        \"prognosegrundlage\": \"WERTE\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"LOKATIONSBUENDEL\": [\n      {\n        \"boTyp\": \"LOKATIONSBUENDEL\",\n        \"lokationsbuendelstrukturId\": \"9992000000026\",\n        \"standardisierteLokationsbuendelstruktur\": true,\n        \"versionStruktur\": \"1\",\n        \"zuordnungObjectcode\": [\n          {\n            \"objectcode\": [\n              {\n                \"objectcode\": \"9992000001016\"\n              }\n            ],\n            \"referenzLokationsId\": \"50363191616\",\n            \"referenzLokationsTyp\": \"MALO\"\n          },\n          {\n            \"objectcode\": [\n              {\n                \"objectcode\": \"9992000001032\"\n              }\n            ],\n            \"referenzLokationsId\": \"DE0032106765712000000000000001717\",\n            \"referenzLokationsTyp\": \"MELO\"\n          }\n        ]\n      }\n    ],\n    \"MARKTLOKATION\": [\n      {\n        \"boTyp\": \"MARKTLOKATION\",\n        \"energierichtung\": \"AUSSP\",\n        \"marktlokationsId\": \"50363191616\",\n        \"marktlokationsTyp\": [\n          {\n            \"typ\": \"STANDARD_MARKTLOKATION\"\n          }\n        ],\n        \"marktrollen\": [\n          {\n            \"boTyp\": \"MARKTTEILNEHMER\",\n            \"gewerbekennzeichnung\": true,\n            \"marktrolle\": \"UENB\",\n            \"rollencodenummer\": \"9900496003333\",\n            \"rollencodetyp\": \"BDEW\",\n            \"versionStruktur\": \"1\"\n          },\n          {\n            \"boTyp\": \"MARKTTEILNEHMER\",\n            \"gewerbekennzeichnung\": true,\n            \"marktrolle\": \"MSB\",\n            \"messstellenbetreiberEigenschaft\": \"GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER\",\n            \"rollencodenummer\": \"9900496000002\",\n            \"rollencodetyp\": \"BDEW\",\n            \"versionStruktur\": \"1\",\n            \"weiterverpflichtet\": false\n          }\n        ],\n        \"messtechnischeEinordnung\": \"IMS\",\n        \"netzebene\": \"HSP\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\",\n        \"zaehlwerke\": [\n          {\n            \"messprodukt\": \"9991000000078\",\n            \"verwendungszwecke\": [\n              {\n                \"marktrolle\": \"NB\",\n                \"zweck\": [\n                  \"NETZNUTZUNGSABRECHNUNG\"\n                ]\n              },\n              {\n                \"marktrolle\": \"LF\",\n                \"zweck\": [\n                  \"NETZNUTZUNGSABRECHNUNG\"\n                ]\n              },\n              {\n                \"marktrolle\": \"UENB\",\n                \"zweck\": [\n                  \"BILANZKREISABRECHNUNG\"\n                ]\n              }\n            ]\n          }\n        ]\n      }\n    ],\n    \"MESSLOKATION\": [\n      {\n        \"ablesekartenempfaenger\": {\n          \"boTyp\": \"GESCHAEFTSPARTNER\",\n          \"geschaeftspartnerrolle\": [\n            \"ABLESEKARTENEMPFAENGER\"\n          ],\n          \"gewerbekennzeichnung\": false,\n          \"name1\": \"Max\",\n          \"name2\": \"Mustermann\",\n          \"partneradresse\": {\n            \"hausnummer\": \"46\",\n            \"landescode\": \"DE\",\n            \"ort\": \"Weimar\",\n            \"postleitzahl\": \"99423\",\n            \"strasse\": \"Erfurter str.\"\n          },\n          \"versionStruktur\": \"1\"\n        },\n        \"betriebszustand\": \"GESPERRT_NICHT_ENTSPERREN\",\n        \"boTyp\": \"MESSLOKATION\",\n        \"marktrollen\": [\n          {\n            \"boTyp\": \"MARKTTEILNEHMER\",\n            \"gewerbekennzeichnung\": true,\n            \"marktrolle\": \"MSB\",\n            \"messstellenbetreiberEigenschaft\": \"GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER\",\n            \"rollencodenummer\": \"9900496000002\",\n            \"rollencodetyp\": \"BDEW\",\n            \"versionStruktur\": \"1\",\n            \"weiterverpflichtet\": false\n          },\n          {\n            \"boTyp\": \"MARKTTEILNEHMER\",\n            \"gewerbekennzeichnung\": true,\n            \"marktrolle\": \"GMSB\",\n            \"rollencodenummer\": \"9900496000022\",\n            \"rollencodetyp\": \"BDEW\",\n            \"versionStruktur\": \"1\"\n          }\n        ],\n        \"messadresse\": {\n          \"hausnummer\": \"46\",\n          \"landescode\": \"DE\",\n          \"ort\": \"Weimar\",\n          \"postleitzahl\": \"99423\",\n          \"strasse\": \"Erfurter str.\",\n          \"zusatzInformation\": {\n            \"zusatz1\": \"Hinter\",\n            \"zusatz2\": \"Hof\"\n          }\n        },\n        \"messlokationsId\": \"DE0032106765712000000000000001717\",\n        \"netzebenemessung\": \"HSS\",\n        \"referenzMarktlokationsId\": \"50363191616\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\",\n        \"verwendungsumfang\": \"MESSLOKATION_PROZESSUAL_BEHANDELT\",\n        \"zaehlwerke\": [\n          {\n            \"messprodukt\": \"9991000000218\",\n            \"notwendigkeitZweiteMessung\": \"VORHANDEN\",\n            \"werteuebermittlungVerwendungszweck\": \"VORHANDEN\",\n            \"zaehlzeiten\": {\n              \"zaehlzeitDefinition\": \"ABC\"\n            }\n          }\n        ]\n      }\n    ],\n    \"MESSSTELLENBETRIEBSVERTRAG\": [\n      {\n        \"boTyp\": \"VERTRAG\",\n        \"korrespondenzpartner\": {\n          \"ansprechpartner\": {\n            \"boTyp\": \"ANSPRECHPARTNER\",\n            \"eMailAdresse\": \"max@mustermann.de\",\n            \"versionStruktur\": \"1\"\n          },\n          \"boTyp\": \"GESCHAEFTSPARTNER\",\n          \"gewerbekennzeichnung\": false,\n          \"name1\": \"Jan\",\n          \"name2\": \"Schoeler\",\n          \"partneradresse\": {\n            \"hausnummer\": \"36\",\n            \"landescode\": \"DE\",\n            \"ort\": \"Berlin\",\n            \"postleitzahl\": \"10435\",\n            \"strasse\": \"Schönhauser Allee\"\n          },\n          \"versionStruktur\": \"1\"\n        },\n        \"lokationsId\": \"DE0032106765712000000000000001717\",\n        \"lokationsTyp\": \"MELO\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\",\n        \"vertragsart\": \"MESSSTELLENBETRIEBSVERTRAG\",\n        \"vertragspartner2\": [\n          {\n            \"boTyp\": \"GESCHAEFTSPARTNER\",\n            \"geschaeftspartnerrolle\": [\n              \"KUNDE\"\n            ],\n            \"gewerbekennzeichnung\": false,\n            \"name1\": \"Hans\",\n            \"name2\": \"Muller\",\n            \"versionStruktur\": \"1\"\n          }\n        ]\n      }\n    ],\n    \"NETZNUTZUNGSVERTRAG\": [\n      {\n        \"boTyp\": \"VERTRAG\",\n        \"lokationsId\": \"50363191616\",\n        \"lokationsTyp\": \"MALO\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\",\n        \"vertragsart\": \"NETZNUTZUNGSVERTRAG\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9900496000001\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"anfragereferenznummer\": \"NV12372\",\n    \"antwortstatus\": \"E15\",\n    \"antwortstatusCodeliste\": \"S_0055\",\n    \"datenaustauschreferenz\": \"M3CJAXK5\",\n    \"datumleistungsbeginn\": \"2026-12-05T23:00:00Z\",\n    \"dokumentennummer\": \"BGMM2F84HWH\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9900496000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"E01\",\n    \"nachrichtendatum\": \"2026-10-02T11:00:00Z\",\n    \"nachrichtenreferenznummer\": \"UNHM33TKB5W\",\n    \"pruefidentifikator\": \"55043\",\n    \"sparte\": \"STROM\",\n    \"transaktionsgrund\": \"E02\",\n    \"vorgangsnummer\": \"KBG27094210000000000929931413171000\"\n  },\n  \"zusatzdaten\": {}\n}"} examples={[{"mediaType": "application/json", "examples": [{"name": "55043", "summary": "55043 — Bestätigung Anmeldung MSB", "value": {"stammdaten": {"MARKTLOKATION": [{"boTyp": "MARKTLOKATION", "versionStruktur": "1", "marktlokationsId": "50363191616", "marktlokationsTyp": [{"typ": "STANDARD_MARKTLOKATION"}], "sparte": "STROM", "energierichtung": "AUSSP", "netzebene": "HSP", "marktrollen": [{"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "marktrolle": "UENB", "gewerbekennzeichnung": true, "rollencodenummer": "9900496003333", "rollencodetyp": "BDEW"}, {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "marktrolle": "MSB", "gewerbekennzeichnung": true, "rollencodenummer": "9900496000002", "rollencodetyp": "BDEW", "weiterverpflichtet": false, "messstellenbetreiberEigenschaft": "GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER"}], "zaehlwerke": [{"verwendungszwecke": [{"marktrolle": "NB", "zweck": ["NETZNUTZUNGSABRECHNUNG"]}, {"marktrolle": "LF", "zweck": ["NETZNUTZUNGSABRECHNUNG"]}, {"marktrolle": "UENB", "zweck": ["BILANZKREISABRECHNUNG"]}], "messprodukt": "9991000000078"}], "messtechnischeEinordnung": "IMS"}], "MESSLOKATION": [{"boTyp": "MESSLOKATION", "versionStruktur": "1", "messlokationsId": "DE0032106765712000000000000001717", "sparte": "STROM", "netzebenemessung": "HSS", "messadresse": {"postleitzahl": "99423", "ort": "Weimar", "strasse": "Erfurter str.", "hausnummer": "46", "landescode": "DE", "zusatzInformation": {"zusatz1": "Hinter", "zusatz2": "Hof"}}, "zaehlwerke": [{"zaehlzeiten": {"zaehlzeitDefinition": "ABC"}, "messprodukt": "9991000000218", "notwendigkeitZweiteMessung": "VORHANDEN", "werteuebermittlungVerwendungszweck": "VORHANDEN"}], "betriebszustand": "GESPERRT_NICHT_ENTSPERREN", "ablesekartenempfaenger": {"boTyp": "GESCHAEFTSPARTNER", "versionStruktur": "1", "name1": "Max", "name2": "Mustermann", "gewerbekennzeichnung": false, "geschaeftspartnerrolle": ["ABLESEKARTENEMPFAENGER"], "partneradresse": {"postleitzahl": "99423", "ort": "Weimar", "strasse": "Erfurter str.", "hausnummer": "46", "landescode": "DE"}}, "marktrollen": [{"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "marktrolle": "MSB", "gewerbekennzeichnung": true, "rollencodenummer": "9900496000002", "rollencodetyp": "BDEW", "weiterverpflichtet": false, "messstellenbetreiberEigenschaft": "GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER"}, {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "marktrolle": "GMSB", "gewerbekennzeichnung": true, "rollencodenummer": "9900496000022", "rollencodetyp": "BDEW"}], "referenzMarktlokationsId": "50363191616", "verwendungsumfang": "MESSLOKATION_PROZESSUAL_BEHANDELT"}], "LOKATIONSBUENDEL": [{"boTyp": "LOKATIONSBUENDEL", "versionStruktur": "1", "lokationsbuendelstrukturId": "9992000000026", "standardisierteLokationsbuendelstruktur": true, "zuordnungObjectcode": [{"referenzLokationsTyp": "MALO", "referenzLokationsId": "50363191616", "objectcode": [{"objectcode": "9992000001016"}]}, {"referenzLokationsTyp": "MELO", "referenzLokationsId": "DE0032106765712000000000000001717", "objectcode": [{"objectcode": "9992000001032"}]}]}], "NETZNUTZUNGSVERTRAG": [{"boTyp": "VERTRAG", "versionStruktur": "1", "vertragsart": "NETZNUTZUNGSVERTRAG", "sparte": "STROM", "lokationsId": "50363191616", "lokationsTyp": "MALO"}], "MESSSTELLENBETRIEBSVERTRAG": [{"boTyp": "VERTRAG", "versionStruktur": "1", "vertragsart": "MESSSTELLENBETRIEBSVERTRAG", "sparte": "STROM", "vertragspartner2": [{"boTyp": "GESCHAEFTSPARTNER", "versionStruktur": "1", "name1": "Hans", "name2": "Muller", "gewerbekennzeichnung": false, "geschaeftspartnerrolle": ["KUNDE"]}], "korrespondenzpartner": {"boTyp": "GESCHAEFTSPARTNER", "versionStruktur": "1", "name1": "Jan", "name2": "Schoeler", "gewerbekennzeichnung": false, "partneradresse": {"postleitzahl": "10435", "ort": "Berlin", "strasse": "Schönhauser Allee", "hausnummer": "36", "landescode": "DE"}, "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "eMailAdresse": "max@mustermann.de"}}, "lokationsId": "DE0032106765712000000000000001717", "lokationsTyp": "MELO"}], "BILANZIERUNG": [{"boTyp": "BILANZIERUNG", "versionStruktur": "1", "marktlokationsId": "50363191616", "aggregationsverantwortung": "VNB", "prognosegrundlage": "WERTE", "abwicklungsmodell": "MODELL_1_BILANZIERUNG_AN_MARKTLOKATION"}]}, "transaktionsdaten": {"datenaustauschreferenz": "M3CJAXK5", "sparte": "STROM", "transaktionsgrund": "E02", "vorgangsnummer": "KBG27094210000000000929931413171000", "pruefidentifikator": "55043", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9900496000001", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9900496000002", "rollencodetyp": "BDEW"}, "dokumentennummer": "BGMM2F84HWH", "kategorie": "E01", "nachrichtendatum": "2026-10-02T11:00:00Z", "nachrichtenreferenznummer": "UNHM33TKB5W", "anfragereferenznummer": "NV12372", "antwortstatus": "E15", "antwortstatusCodeliste": "S_0055", "datumleistungsbeginn": "2026-12-05T23:00:00Z"}, "zusatzdaten": {}}}, {"name": "55044", "summary": "55044 — Ablehnung Anmeldung MSB", "value": {"stammdaten": {"MESSLOKATION": [{"boTyp": "MESSLOKATION", "versionStruktur": "1", "messlokationsId": "DE0032106765712000000000000000037"}]}, "transaktionsdaten": {"datenaustauschreferenz": "826946", "sparte": "STROM", "transaktionsgrund": "E03", "vorgangsnummer": "1539948277", "pruefidentifikator": "55044", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9900321000005", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9904446000007", "rollencodetyp": "BDEW"}, "dokumentennummer": "211900BGM", "kategorie": "E01", "nachrichtendatum": "2025-10-01T11:17:00Z", "nachrichtenreferenznummer": "211900", "anfragereferenznummer": "12345678910", "antwortstatus": "E17", "antwortstatusCodeliste": "S_0056"}}}]}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend mit den Daten der eingegangenen Nachricht fort.

</li>

<li data-teil="lesen" data-stufe="ebd">

**Daten für die Prüfung laden**
- [Messlokation lesen](/api/202610/backend-lesen/getmeterlocationbasic#messlokation-lesen) `GET /getMeterLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getMeterLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_MESSLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="3" anker="schritt-3" richtung="fremd" kopf={{"links": {"label": "NB", "eigen": false}, "rechts": {"label": "MSBA"}}}>

### Information über vorläufige Anmeldebestätigung

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [21007](/schnittstellen/202610/pruefi/IFTSTA/PI_21007) — Statusmeldung · AS4

</div>

</Schritt>

<Schritt nr="4" anker="schritt-4" richtung="fremd" kopf={{"links": {"label": "NB", "eigen": false}, "rechts": {"label": "LF"}}}>

### Information über vorläufige Anmeldebestätigung

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [21007](/schnittstellen/202610/pruefi/IFTSTA/PI_21007) — Statusmeldung · AS4

</div>

</Schritt>

<Schritt nr="7" anker="schritt-7" richtung="ausgehend" kopf={{"links": {"label": "MSBN", "eigen": true}, "rechts": {"label": "NB"}}}>

### Mitteilung über Gesamtvorgang

<Schrittskizze sicht={{"label": "MSBN"}} zeilen={[{"art": "senden", "label": "NB", "weg": "AS4", "nachrichten": [{"nr": "21009", "titel": "Statusmeldung"}, {"nr": "21010", "titel": "Statusmeldung"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [21009](/schnittstellen/202610/pruefi/IFTSTA/PI_21009) — Statusmeldung · AS4
- [21010](/schnittstellen/202610/pruefi/IFTSTA/PI_21010) — Statusmeldung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht an **NB** · AS4

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202610/backend-schreiben-msb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend fort, nachdem die Nachricht erstellt ist.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="8" anker="schritt-8" richtung="eingehend" kopf={{"links": {"label": "MSBN", "eigen": true}, "rechts": {"label": "NB"}}}>

### Antwort auf Mitteilung über Gesamtvorgang

<Schrittskizze sicht={{"label": "MSBN"}} zeilen={[{"art": "empfangen", "label": "NB", "weg": "AS4", "nachrichten": [{"nr": "21011", "titel": "Statusmeldung"}, {"nr": "21012", "titel": "Statusmeldung"}]}, {"art": "aperak", "werte": ["Z33"]}, {"art": "fortschreiben"}, {"art": "lesen_ebd", "schnittstellen": [{"label": "Messlokation lesen"}]}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [21011](/schnittstellen/202610/pruefi/IFTSTA/PI_21011) — Statusmeldung · AS4
- [21012](/schnittstellen/202610/pruefi/IFTSTA/PI_21012) — Statusmeldung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **NB** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `21011` → [E_0232](/referenz/202610/ebd/E_0232) · Mitteilung über Gesamtvorgang prüfen

</div>

</li>

<li data-teil="aperak">

**Aperak-Prüfungen**
- `21011`, `21012` → `Z33`

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202610/backend-schreiben-msb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend mit den Daten der eingegangenen Nachricht fort.

</li>

<li data-teil="lesen" data-stufe="ebd">

**Daten für die Prüfung laden**
- [Messlokation lesen](/api/202610/backend-lesen/getmeterlocationbasic#messlokation-lesen) `GET /getMeterLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getMeterLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_MESSLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="14" anker="schritt-14" richtung="fremd" kopf={{"links": {"label": "NB", "eigen": false}, "rechts": {"label": "MSBA"}}}>

### Information über Scheitern der Zuordnung

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [21011](/schnittstellen/202610/pruefi/IFTSTA/PI_21011) — Statusmeldung · AS4

</div>

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `21011` → [E_0232](/referenz/202610/ebd/E_0232) · Mitteilung über Gesamtvorgang prüfen

</div>

</Schritt>

<Schritt nr="15" anker="schritt-15" richtung="fremd" kopf={{"links": {"label": "NB", "eigen": false}, "rechts": {"label": "LF"}}}>

### Information über Scheitern der Zuordnung

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [21011](/schnittstellen/202610/pruefi/IFTSTA/PI_21011) — Statusmeldung · AS4

</div>

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `21011` → [E_0232](/referenz/202610/ebd/E_0232) · Mitteilung über Gesamtvorgang prüfen

</div>

</Schritt>

<Schritt nr="16" anker="schritt-16" richtung="eingehend" kopf={{"links": {"label": "MSBN", "eigen": true}, "rechts": {"label": "NB"}}}>

### Mitteilung über das Scheitern des Gesamtvorgangs

<Schrittskizze sicht={{"label": "MSBN"}} zeilen={[{"art": "empfangen", "label": "NB", "weg": "AS4", "nachrichten": [{"nr": "21013", "titel": "Statusmeldung"}]}, {"art": "lesen_aperak", "schnittstellen": [{"label": "Messlokation lesen"}]}, {"art": "aperak", "werte": ["Z10", "Z17", "Z18"]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [21013](/schnittstellen/202610/pruefi/IFTSTA/PI_21013) — Statusmeldung · AS4

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
- [Messlokation lesen](/api/202610/backend-lesen/getmeterlocationbasic#messlokation-lesen) `GET /getMeterLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getMeterLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_MESSLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

</li>

<li data-teil="aperak">

**Aperak-Prüfungen**
- `21013` → `Z10`
- `21013` → `Z17`
- `21013` → `Z18`

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202610/backend-schreiben-msb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend mit den Daten der eingegangenen Nachricht fort.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="17" anker="schritt-17" richtung="fremd" kopf={{"links": {"label": "NB", "eigen": false}, "rechts": {"label": "MSBA"}}}>

### Information über Scheitern der Zuordnung

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [21013](/schnittstellen/202610/pruefi/IFTSTA/PI_21013) — Statusmeldung · AS4

</div>

</Schritt>

<Schritt nr="18" anker="schritt-18" richtung="fremd" kopf={{"links": {"label": "NB", "eigen": false}, "rechts": {"label": "LF"}}}>

### Information über Scheitern der Zuordnung

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [21013](/schnittstellen/202610/pruefi/IFTSTA/PI_21013) — Statusmeldung · AS4

</div>

</Schritt>

<details>
<summary>Entscheidungsbäume dieses Prozesses</summary>

| EBD | Name |
|---|---|
| [E_0201](/referenz/202610/ebd/E_0201) | Anmeldung Messstellenbetrieb prüfen |
| [E_0232](/referenz/202610/ebd/E_0232) | Mitteilung über Gesamtvorgang prüfen |

</details>

<a id="abschnitt-informationen"></a>

## Prozess-Informationen

Wortlaut der Lesefassung, Steckbrief Kap. 2.3.1, S. 22.

<Stepper>
<ol>

<li data-blatt="vorbedingungen">

### Vorbedingungen

Abschluss eines MSB-Vertrages.

</li>

<li data-blatt="ergebnisse">

### Ergebnisse

- Der NB kann die daraus veränderten Stammdaten an der Mess- bzw. Marktlokation eines Lokationsbündels an die Berechtigten verteilen.
- Der NB versendet die Berechnungsformel an den MSBN.
- Sofern die Übermittlung von Werten an den ESA durchgeführt wird, beendet der MSBA die Übermittlung von Werten an den ESA.
- Sofern der MSBA eine von einem NB oder LF bestellte Konfiguration zu beenden hat,
  - und der MSBA der MSB der direkt betroffenen Lokation der zu beendenden Konfiguration ist, führt der MSBA den Use-Case „[Beendigung einer Konfiguration vom MSB](/prozessdoku/202610/LF/GPKE-Teil3-beendigung-einer-konfiguration-vom-msb)“ (GPKE Teil 3) aus.
  - und im Fall, dass der MSBA ein „weiterer MSB“ der zu beendenden Konfiguration ist, führt der MSBA den Use-Case „Bestellung Beendigung einer Konfiguration an MSB“ (GPKE Teil 3) aus.

</li>

<li data-blatt="erste-nachricht">

### Erste Nachricht

Der Beteiligte dieser Seite sendet selbst: „Anmeldung“ an **NB** (Schritt 1).

</li>

<li data-blatt="ziel">

### Ziel

Der MSB ist einer Messlokation ( als Bestandteil eines Lokationsbündels) zugeordnet.

</li>

</ol>
</Stepper>

<a id="abschnitt-sichten"></a>

## Andere Sichten des Prozesses

Derselbe Prozess, aus den Augen der anderen Beteiligten: dieselben Schritte, jeweils aus deren Sicht gelesen.

- [Sicht MSBA](/prozessdoku/202610/MSB--MSBA/WiM-Teil1-beginn-messstellenbetrieb) — der abgebende MSB · Marktrolle MSB
- [Sicht LF](/prozessdoku/202610/LF/WiM-Teil1-beginn-messstellenbetrieb) — LF
- [Sicht NB](/prozessdoku/202610/NB/WiM-Teil1-beginn-messstellenbetrieb) — NB

<Hinweisbereich>

*Die Schritte sind die **möglichen** Nachrichten dieses Prozesses, keine Abfolge — die Quelle führt weder Bedingungen noch Alternativen. Das Kästchen am Schritt nennt links die eigene Sicht: **←** empfängt sie, **→** sendet sie. Zugeklappte Schritte laufen zwischen anderen Marktpartnern. Die Nummern sind die der Quelle; wo eine fehlt, fehlt sie dort.*

Zu den Prüfidentifikatoren dieser Schritte liegt kein Testfall im Testbestand; der Knopf »Ausprobieren« der schreibenden Schnittstelle bietet deshalb keinen Rumpf an.

Betrifft: [7](#schritt-7), [8](#schritt-8), [16](#schritt-16)

</Hinweisbereich>
