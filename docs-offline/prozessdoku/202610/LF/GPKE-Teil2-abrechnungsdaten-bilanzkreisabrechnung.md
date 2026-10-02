# Abrechnungsdaten Bilanzkreisabrechnung — Sicht LF

<Kopf rolle="LF" beteiligter="LF" festlegung="GPKE" dokument="GPKE Teil 2" kapitel="3.1.2.2" sparte="Strom" schritte={6} suchtitel="Abrechnungsdaten Bilanzkreisabrechnung — Sicht LF · GPKE Teil 2 · Formatversion 202610" abschnitte={[{"id": "abschnitt-ablauf", "label": "Prozessablauf"}, {"id": "abschnitt-schritte", "label": "Prozessschritte"}, {"id": "abschnitt-informationen", "label": "Prozess-Informationen"}, {"id": "abschnitt-sichten", "label": "Andere Sichten des Prozesses"}]} />

<Kurzfassung>

Der NB übermittelt dem LF und ggf. dem ÜNB die Abrechnungsdaten zur Bilanzkreisabrechnung. Der LF bzw. ÜNB prüft die Daten und gibt dem NB eine Qualitätsrückmeldung zum Inhalt der Daten. Sofern der LF bzw. ÜNB einen anderen Inhalt der Daten erwartet, gibt er dies in der Rückmeldung an. Der NB teilt dem LF bzw. ÜNB in diesem Fall den Bearbeitungstand zu dessen Rückmeldung mit.

</Kurzfassung>

<a id="abschnitt-ablauf"></a>

## Prozessablauf aus Sicht des LF

<Systembild svg={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1004 1173\" width=\"1004\" height=\"1173\" role=\"img\" aria-labelledby=\"sb-title\" class=\"maco-systembild\">\n<title id=\"sb-title\">Systembild: Abrechnungsdaten Bilanzkreisabrechnung aus Sicht LF</title>\n<defs><marker id=\"sb-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect class=\"sb-lane-kopf\" x=\"16\" y=\"12\" width=\"232\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend-System des Kunden</text>\n<rect class=\"sb-lane-kopf\" x=\"398\" y=\"12\" width=\"264\" height=\"46\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · LF</text>\n<rect class=\"sb-lane-kopf\" x=\"812\" y=\"12\" width=\"176\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"900\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Marktpartner</text>\n<line x1=\"323\" y1=\"58\" x2=\"323\" y2=\"1161\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"737\" y1=\"58\" x2=\"737\" y2=\"1161\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"80\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">1. Abrechnungsdaten</text>\n<text x=\"530\" y=\"115\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Bilanzkreis-abrechnung vom</text>\n<text x=\"530\" y=\"130\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">NB an LF</text>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"93\" r=\"5\"/><line x1=\"900\" y1=\"98\" x2=\"900\" y2=\"110\"/><line x1=\"893\" y1=\"102\" x2=\"907\" y2=\"102\"/><line x1=\"900\" y1=\"110\" x2=\"894\" y2=\"120\"/><line x1=\"900\" y1=\"110\" x2=\"906\" y2=\"120\"/></g>\n<text x=\"900\" y=\"142\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"878\" y1=\"111\" x2=\"628\" y2=\"111\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"103\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"127\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">55126, 55672</text>\n<rect class=\"sb-kasten sb-aperak_lesen\" x=\"432\" y=\"169\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"189\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Daten für die</text>\n<text x=\"530\" y=\"204\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Eingangsprüfung laden</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"143\" x2=\"530\" y2=\"169\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-aperak_lesen\" x=\"34\" y=\"177\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"197\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Marktlokation lesen</text>\n<line x1=\"432\" y1=\"193\" x2=\"230\" y2=\"193\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"185\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"243\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"263\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z10, Z43</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"217\" x2=\"530\" y2=\"243\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-schreiben\" x=\"432\" y=\"307\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"327\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"276\" x2=\"530\" y2=\"307\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-schreiben\" x=\"34\" y=\"307\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"327\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten erstellen</text>\n<line x1=\"432\" y1=\"323\" x2=\"230\" y2=\"323\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"315\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-ebd\" x=\"432\" y=\"371\" width=\"196\" height=\"108\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"391\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">EBD prüfen: E_0611</text>\n<text x=\"530\" y=\"406\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label-2, #424245)\">Abrechnungsdaten</text>\n<text x=\"530\" y=\"421\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label-2, #424245)\">Bilanzkreisabrechnung</text>\n<text x=\"530\" y=\"436\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label-2, #424245)\">prüfen (Basiert auf EBD:</text>\n<text x=\"530\" y=\"451\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label-2, #424245)\">E_0408_Änderung vom NB</text>\n<text x=\"530\" y=\"466\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label-2, #424245)\">prüfen)</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"340\" x2=\"530\" y2=\"371\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-folgeprozess\" x=\"432\" y=\"505\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"525\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Folgeprozess auslösen:</text>\n<text x=\"530\" y=\"540\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">55156, 55673</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"479\" x2=\"530\" y2=\"505\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-folge_ausloeser\" x=\"432\" y=\"579\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"599\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Ausgelöst durch Eingang:</text>\n<text x=\"530\" y=\"614\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">55126, 55672</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"553\" x2=\"530\" y2=\"579\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-trigger\" x=\"432\" y=\"653\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"673\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessauslöser empfangen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"627\" x2=\"530\" y2=\"653\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-trigger\" x=\"34\" y=\"653\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"673\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">START_BESTELLUNG_SDAE</text>\n<line x1=\"230\" y1=\"669\" x2=\"432\" y2=\"669\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"661\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-lesen_verarbeitung\" x=\"432\" y=\"717\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"737\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Daten für die Verarbeitung</text>\n<text x=\"530\" y=\"752\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">laden</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"686\" x2=\"530\" y2=\"717\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-lesen_verarbeitung\" x=\"34\" y=\"725\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"745\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Marktlokation lesen</text>\n<line x1=\"432\" y1=\"741\" x2=\"230\" y2=\"741\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"733\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"791\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"811\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">2. Rückmeldung auf</text>\n<text x=\"530\" y=\"826\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Abrechnungsdaten</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"765\" x2=\"530\" y2=\"791\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"797\" r=\"5\"/><line x1=\"900\" y1=\"802\" x2=\"900\" y2=\"814\"/><line x1=\"893\" y1=\"806\" x2=\"907\" y2=\"806\"/><line x1=\"900\" y1=\"814\" x2=\"894\" y2=\"824\"/><line x1=\"900\" y1=\"814\" x2=\"906\" y2=\"824\"/></g>\n<text x=\"900\" y=\"846\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"628\" y1=\"815\" x2=\"878\" y2=\"815\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"807\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"831\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">55156, 55673</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"874\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"894\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"839\" x2=\"530\" y2=\"874\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"874\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"894\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"890\" x2=\"230\" y2=\"890\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"882\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"938\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"958\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">3. Bearbeitungsstand zur</text>\n<text x=\"530\" y=\"973\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Rückmeldung</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"907\" x2=\"530\" y2=\"938\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"944\" r=\"5\"/><line x1=\"900\" y1=\"949\" x2=\"900\" y2=\"961\"/><line x1=\"893\" y1=\"953\" x2=\"907\" y2=\"953\"/><line x1=\"900\" y1=\"961\" x2=\"894\" y2=\"971\"/><line x1=\"900\" y1=\"961\" x2=\"906\" y2=\"971\"/></g>\n<text x=\"900\" y=\"993\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"878\" y1=\"962\" x2=\"628\" y2=\"962\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"954\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"978\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">21047</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"1021\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1041\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z33</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"986\" x2=\"530\" y2=\"1021\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"1085\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1105\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1054\" x2=\"530\" y2=\"1085\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"1085\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"1105\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"1101\" x2=\"230\" y2=\"1101\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"1093\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n</svg>"} gesamt={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 974 734\" width=\"974\" height=\"734\" role=\"img\" aria-labelledby=\"sd-title\" class=\"maco-sequence\">\n<title id=\"sd-title\">Sequenzdiagramm: Abrechnungsdaten Bilanzkreisabrechnung aus Sicht LF</title>\n<defs><marker id=\"sd-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect x=\"16\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"121\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend (Kunde)</text>\n<line x1=\"121\" y1=\"64\" x2=\"121\" y2=\"722\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"260\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"365\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · LF</text>\n<line x1=\"365\" y1=\"64\" x2=\"365\" y2=\"722\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"504\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"609\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"609\" y1=\"64\" x2=\"609\" y2=\"722\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"748\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"853\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">ÜNB</text>\n<line x1=\"853\" y1=\"64\" x2=\"853\" y2=\"722\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"609\" y1=\"90\" x2=\"365\" y2=\"90\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"81\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">1. Abrechnungsdaten Bilanzkreis-abrechnung vom N…</text>\n<text x=\"487\" y=\"105\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55126, 55672</text>\n<line x1=\"365\" y1=\"152\" x2=\"121\" y2=\"152\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"143\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<text x=\"243\" y=\"167\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten erstellen</text>\n<line x1=\"121\" y1=\"214\" x2=\"365\" y2=\"214\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"205\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">START_BESTELLUNG_SDAE</text>\n<text x=\"243\" y=\"229\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Trigger-Event</text>\n<line x1=\"365\" y1=\"276\" x2=\"609\" y2=\"276\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"267\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">2. Rückmeldung auf Abrechnungsdaten</text>\n<text x=\"487\" y=\"291\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55156, 55673 · E_0611</text>\n<text x=\"487\" y=\"304\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0611 — Abrechnungsdaten Bilanzkreisabrechnung prüfen</text>\n<line x1=\"365\" y1=\"338\" x2=\"121\" y2=\"338\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"329\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"353\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"609\" y1=\"400\" x2=\"365\" y2=\"400\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"391\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">3. Bearbeitungsstand zur Rückmeldung</text>\n<text x=\"487\" y=\"415\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 21047 · E_0619</text>\n<text x=\"487\" y=\"428\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0619 — Rückmeldung prüfen</text>\n<line x1=\"365\" y1=\"462\" x2=\"121\" y2=\"462\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"453\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"477\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"609\" y1=\"524\" x2=\"853\" y2=\"524\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"731\" y=\"515\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">4. Abrechnungsdaten Bilanzkreis-abrechnung vom N…</text>\n<text x=\"731\" y=\"539\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55613, 55674</text>\n<line x1=\"853\" y1=\"586\" x2=\"609\" y2=\"586\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"731\" y=\"577\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">5. Rückmeldung auf Abrechnungsdaten</text>\n<text x=\"731\" y=\"601\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55614, 55675 · E_0612</text>\n<text x=\"731\" y=\"614\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0612 — Abrechnungsdaten Bilanzkreisabrechnung prüfen</text>\n<line x1=\"609\" y1=\"648\" x2=\"853\" y2=\"648\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"731\" y=\"639\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">6. Bearbeitungsstand zur Rückmeldung</text>\n<text x=\"731\" y=\"663\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 21047 · E_0618</text>\n<text x=\"731\" y=\"676\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0618 — Rückmeldung verarbeiten</text>\n</svg>"} titel="LF" />

<a id="abschnitt-schritte"></a>

## Prozessschritte

<Schritt nr="1" anker="schritt-1" richtung="eingehend" kopf={{"links": {"label": "LF", "eigen": true}, "rechts": {"label": "NB"}}}>

### Abrechnungsdaten Bilanzkreis-abrechnung vom NB an LF

<Schrittskizze sicht={{"label": "LF"}} zeilen={[{"art": "empfangen", "label": "NB", "weg": "AS4", "nachrichten": [{"nr": "55126", "titel": "Abr.-Daten BK-Abr. verb. MaLo"}, {"nr": "55672", "titel": "Abr.-Daten BK-Abr. erz. Malo"}]}, {"art": "lesen_aperak", "schnittstellen": [{"label": "Marktlokation lesen"}]}, {"art": "aperak", "werte": ["Z10", "Z43"]}, {"art": "erstellen"}, {"art": "ebd", "baeume": [{"code": "E_0611", "titel": "Abrechnungsdaten Bilanzkreisabrechnung prüfen (Basiert auf EBD: E_0408_Änderung vom NB prüfen)"}]}, {"art": "folgeprozess", "werte": ["55156", "55673"]}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55126](/schnittstellen/202610/pruefi/UTILMD/PI_55126) — Abr.-Daten BK-Abr. verb. MaLo · AS4
- [55672](/schnittstellen/202610/pruefi/UTILMD/PI_55672) — Abr.-Daten BK-Abr. erz. Malo · AS4

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

<li data-teil="aperak">

**Aperak-Prüfungen**
- `55126`, `55672` → `Z10` — Aperak Prüfung: Ist Lokation bekannt ?
- `55126`, `55672` → `Z43` — Aperak Prüfung: Stimmt Objekteigenschaft überein?

</li>

<li data-teil="schnittstelle" data-art="schreiben">

**Schreibende Schnittstelle**
- Vorgang angelegt — [Prozessdaten erstellen](/api/202610/backend-schreiben-lf/createprocessdata#prozessdaten-erstellen) `POST /createProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/createProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": false, "defaultValue": "ERSTELLEN_PROZESSDATEN", "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"BILANZIERUNG\": [\n      {\n        \"aggregationsverantwortung\": \"VNB\",\n        \"bilanzkreis\": \"NCHB999123220000\",\n        \"boTyp\": \"BILANZIERUNG\",\n        \"datenqualitaet\": \"GUELTIGE_DATEN\",\n        \"detailsPrognosegrundlage\": [\n          \"SLP_SEP\"\n        ],\n        \"gueltigkeitszeitraum\": {\n          \"startdatum\": \"2024-12-31T23:00:00Z\",\n          \"zeitraumId\": 1\n        },\n        \"jahresverbrauchsprognose\": {\n          \"einheit\": \"KWH\",\n          \"wert\": 10000\n        },\n        \"lastprofile\": [\n          {\n            \"bezeichnung\": \"XYA\",\n            \"einspeisung\": false,\n            \"herausgeber\": \"NB\",\n            \"profilart\": \"ART_STANDARDLASTPROFIL\",\n            \"verfahren\": \"ANALYTISCH\"\n          }\n        ],\n        \"prognosegrundlage\": \"PROFILE\",\n        \"versionStruktur\": \"1\",\n        \"zeitreihentyp\": \"SLS\"\n      }\n    ],\n    \"MARKTLOKATION\": [\n      {\n        \"bilanzierungsgebiet\": \"10YDE-VNBNET---I\",\n        \"boTyp\": \"MARKTLOKATION\",\n        \"datenqualitaet\": \"GUELTIGE_DATEN\",\n        \"gueltigkeitszeitraum\": {\n          \"startdatum\": \"2024-12-31T23:00:00Z\",\n          \"zeitraumId\": 1\n        },\n        \"marktlokationsId\": \"50363198116\",\n        \"marktrollen\": [\n          {\n            \"boTyp\": \"MARKTTEILNEHMER\",\n            \"gewerbekennzeichnung\": true,\n            \"marktrolle\": \"UENB\",\n            \"rollencodenummer\": \"9900496000003\",\n            \"rollencodetyp\": \"BDEW\",\n            \"versionStruktur\": \"1\"\n          }\n        ],\n        \"regelzone\": \"10YDE-VNBNET---I\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"VERWENDUNGSZEITRAUM\": [\n      {\n        \"boTyp\": \"VERWENDUNGSZEITRAUM\",\n        \"datenqualitaet\": \"GUELTIGE_DATEN\",\n        \"versionStruktur\": \"1\",\n        \"verwendungAb\": \"2024-12-31T23:00:00Z\",\n        \"zeitraumId\": 1\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9900496000001\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"datenaustauschreferenz\": \"M3LYMHT8\",\n    \"dokumentennummer\": \"BGMM30ZB57S\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9900496000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"E03\",\n    \"nachrichtendatum\": \"2024-10-29T09:45:00Z\",\n    \"nachrichtenreferenznummer\": \"UNHM375KFCF\",\n    \"pruefidentifikator\": \"55126\",\n    \"sparte\": \"STROM\",\n    \"transaktionsgrund\": \"ZX3\",\n    \"vorgangsnummer\": \"KBG27094210000000000929931413171000\"\n  },\n  \"zusatzdaten\": {}\n}"} examples={[{"mediaType": "application/json", "examples": [{"name": "55126", "summary": "55126 — Abr.-Daten BK-Abr. verb. MaLo", "value": {"stammdaten": {"VERWENDUNGSZEITRAUM": [{"boTyp": "VERWENDUNGSZEITRAUM", "versionStruktur": "1", "zeitraumId": 1, "datenqualitaet": "GUELTIGE_DATEN", "verwendungAb": "2024-12-31T23:00:00Z"}], "MARKTLOKATION": [{"boTyp": "MARKTLOKATION", "versionStruktur": "1", "marktlokationsId": "50363198116", "sparte": "STROM", "gueltigkeitszeitraum": {"zeitraumId": 1, "startdatum": "2024-12-31T23:00:00Z"}, "datenqualitaet": "GUELTIGE_DATEN", "bilanzierungsgebiet": "10YDE-VNBNET---I", "marktrollen": [{"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "marktrolle": "UENB", "gewerbekennzeichnung": true, "rollencodenummer": "9900496000003", "rollencodetyp": "BDEW"}], "regelzone": "10YDE-VNBNET---I"}], "BILANZIERUNG": [{"boTyp": "BILANZIERUNG", "versionStruktur": "1", "gueltigkeitszeitraum": {"zeitraumId": 1, "startdatum": "2024-12-31T23:00:00Z"}, "datenqualitaet": "GUELTIGE_DATEN", "lastprofile": [{"bezeichnung": "XYA", "verfahren": "ANALYTISCH", "einspeisung": false, "profilart": "ART_STANDARDLASTPROFIL", "herausgeber": "NB"}], "bilanzkreis": "NCHB999123220000", "jahresverbrauchsprognose": {"wert": 10000, "einheit": "KWH"}, "aggregationsverantwortung": "VNB", "zeitreihentyp": "SLS", "prognosegrundlage": "PROFILE", "detailsPrognosegrundlage": ["SLP_SEP"]}]}, "transaktionsdaten": {"datenaustauschreferenz": "M3LYMHT8", "sparte": "STROM", "transaktionsgrund": "ZX3", "vorgangsnummer": "KBG27094210000000000929931413171000", "pruefidentifikator": "55126", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900496000001", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900496000002", "rollencodetyp": "BDEW"}, "dokumentennummer": "BGMM30ZB57S", "kategorie": "E03", "nachrichtendatum": "2024-10-29T09:45:00Z", "nachrichtenreferenznummer": "UNHM375KFCF"}, "zusatzdaten": {}}}, {"name": "55672", "summary": "55672 — Abr.-Daten BK-Abr. erz. Malo", "value": {"stammdaten": {"VERWENDUNGSZEITRAUM": [{"boTyp": "VERWENDUNGSZEITRAUM", "versionStruktur": "1", "zeitraumId": 1, "datenqualitaet": "KEINE_DATEN", "verwendungAb": "2024-04-02T22:00:00Z", "verwendungBis": "2025-04-02T22:00:00Z"}, {"boTyp": "VERWENDUNGSZEITRAUM", "versionStruktur": "1", "zeitraumId": 2, "datenqualitaet": "GUELTIGE_DATEN", "verwendungAb": "2025-04-02T22:00:00Z"}], "MARKTLOKATION": [{"boTyp": "MARKTLOKATION", "versionStruktur": "1", "marktlokationsId": "50074561188", "marktlokationsTyp": [{"typ": "STANDARD_MARKTLOKATION"}], "sparte": "STROM", "gueltigkeitszeitraum": {"zeitraumId": 2, "startdatum": "2025-04-02T22:00:00Z"}, "datenqualitaet": "GUELTIGE_DATEN", "bilanzierungsgebiet": "11YR00000002596Z", "marktrollen": [{"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "marktrolle": "UENB", "gewerbekennzeichnung": true, "rollencodenummer": "4045399000077", "rollencodetyp": "BDEW"}], "regelzone": "10YDE-RWENET---I"}], "BILANZIERUNG": [{"boTyp": "BILANZIERUNG", "versionStruktur": "1", "gueltigkeitszeitraum": {"zeitraumId": 2, "startdatum": "2025-04-02T22:00:00Z"}, "datenqualitaet": "GUELTIGE_DATEN", "bilanzkreis": "11Y0-0000-0076-N", "aggregationsverantwortung": "UENB", "zeitreihentyp": "SES", "prognosegrundlage": "WERTE"}]}, "transaktionsdaten": {"datenaustauschreferenz": "M35DQT4Q", "sparte": "STROM", "transaktionsgrund": "ZX2", "transaktionsgrundergaenzung": "ZW3", "vorgangsnummer": "123456", "pruefidentifikator": "55672", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900321000005", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9903790000002", "rollencodetyp": "BDEW"}, "dokumentennummer": "BGMM3I8WQ6R", "kategorie": "E03", "nachrichtendatum": "2025-04-04T12:00:00Z", "nachrichtenreferenznummer": "UNHM31XN0MU"}, "zusatzdaten": {}}}]}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Legt im Backend einen neuen Vorgang mit den Daten der eingegangenen Nachricht an.

</li>

<li data-teil="baum">

**Entscheidungsbaum**
- `55126`, `55672` → [E_0611](/referenz/202610/ebd/E_0611) — Abrechnungsdaten Bilanzkreisabrechnung prüfen (Basiert auf EBD: E_0408_Änderung vom NB prüfen)

</li>

<li data-teil="folgeprozess">

**Folgeprozess auslösen**
- [55156](/schnittstellen/202610/pruefi/UTILMD/PI_55156) — Rückmeldung/Anfrage Abr.-Daten BK-Abr. verb. MaLo
- [55673](/schnittstellen/202610/pruefi/UTILMD/PI_55673) — Rückmeldung/Anfrage Abr.-Daten BK-Abr. erz. Malo

Nach der Verarbeitung startet die MACO APP den Folgeprozess selbst; welcher davon läuft, hängt vom Ergebnis der Verarbeitung ab.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="2" anker="schritt-2" richtung="ausgehend" kopf={{"links": {"label": "LF", "eigen": true}, "rechts": {"label": "NB"}}}>

### Rückmeldung auf Abrechnungsdaten

<Schrittskizze sicht={{"label": "LF"}} zeilen={[{"art": "folge_ausloeser", "werte": ["55126", "55672"]}, {"art": "ausloeser", "werte": ["START_BESTELLUNG_SDAE"]}, {"art": "lesen_verarbeitung", "schnittstellen": [{"label": "Marktlokation lesen"}]}, {"art": "senden", "label": "NB", "weg": "AS4", "nachrichten": [{"nr": "55156", "titel": "Rückmeldung/Anfrage Abr.-Daten BK-Abr. verb. MaLo"}, {"nr": "55673", "titel": "Rückmeldung/Anfrage Abr.-Daten BK-Abr. erz. Malo"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55156](/schnittstellen/202610/pruefi/UTILMD/PI_55156) — Rückmeldung/Anfrage Abr.-Daten BK-Abr. verb. MaLo · AS4
- [55673](/schnittstellen/202610/pruefi/UTILMD/PI_55673) — Rückmeldung/Anfrage Abr.-Daten BK-Abr. erz. Malo · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="folge_ausloeser">

**Ausgelöst durch Eingang**
- [55126](/schnittstellen/202610/pruefi/UTILMD/PI_55126) — Abr.-Daten BK-Abr. verb. MaLo
- [55672](/schnittstellen/202610/pruefi/UTILMD/PI_55672) — Abr.-Daten BK-Abr. erz. Malo

Die MACO APP sendet diese Nachricht selbst, als Folgeprozess nach einem dieser Eingänge. Daneben kann das Backend diesen Schritt mit einem Ereignis anstoßen — der nächste Punkt.

</li>

<li data-teil="ausloeser">

**Prozessauslöser** [`START_BESTELLUNG_SDAE`](/schnittstellen/202610/trigger/events/LF-START_BESTELLUNG_SDAE) · [Im Playground ausprobieren](/api/202610/ausloeser-lf/start-bestellung-sdae)

Das Backend stößt diesen Schritt mit diesem Ereignis an.

</li>

<li data-teil="lesen" data-stufe="verarbeitung">

**Daten für die Verarbeitung laden**
- [Marktlokation lesen](/api/202610/backend-lesen/getmarketlocationbasic#marktlokation-lesen) `GET /getMarketLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getMarketLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": false, "defaultValue": "MALO", "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": false, "defaultValue": "2024-06-28T12:18:00Z", "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_MARKTLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

</li>

<li data-teil="nachricht">

Nachricht an **NB** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `55156`, `55673` → [E_0611](/referenz/202610/ebd/E_0611) · LF · Abrechnungsdaten Bilanzkreisabrechnung prüfen (Basiert auf EBD: E_0408_Änderung vom NB prüfen)

</div>

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202610/backend-schreiben-lf/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": false, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"BILANZIERUNG\": [\n      {\n        \"aggregationsverantwortung\": \"VNB\",\n        \"bilanzkreis\": \"11XBKA---------I\",\n        \"boTyp\": \"BILANZIERUNG\",\n        \"datenqualitaet\": \"ERWARTETE_DATEN\",\n        \"detailsPrognosegrundlage\": [\n          \"SLP_SEP\"\n        ],\n        \"gueltigkeitszeitraum\": {\n          \"enddatum\": \"2025-07-23T22:00:00Z\",\n          \"startdatum\": \"2025-06-23T22:00:00Z\",\n          \"zeitraumId\": 1\n        },\n        \"prognosegrundlage\": \"PROFILE\",\n        \"versionStruktur\": \"1\",\n        \"zeitreihentyp\": \"SLS\"\n      },\n      {\n        \"aggregationsverantwortung\": \"VNB\",\n        \"bilanzkreis\": \"11XBKA---------I\",\n        \"boTyp\": \"BILANZIERUNG\",\n        \"datenqualitaet\": \"ERWARTETE_DATEN\",\n        \"detailsPrognosegrundlage\": [\n          \"SLP_SEP\"\n        ],\n        \"gueltigkeitszeitraum\": {\n          \"startdatum\": \"2025-07-23T22:00:00Z\",\n          \"zeitraumId\": 2\n        },\n        \"prognosegrundlage\": \"PROFILE\",\n        \"versionStruktur\": \"1\",\n        \"zeitreihentyp\": \"SLS\"\n      }\n    ],\n    \"MARKTLOKATION\": [\n      {\n        \"bilanzierungsgebiet\": \"11YDE-DSONET---I\",\n        \"boTyp\": \"MARKTLOKATION\",\n        \"datenqualitaet\": \"ERWARTETE_DATEN\",\n        \"gueltigkeitszeitraum\": {\n          \"enddatum\": \"2025-07-23T22:00:00Z\",\n          \"startdatum\": \"2025-06-23T22:00:00Z\",\n          \"zeitraumId\": 1\n        },\n        \"marktlokationsId\": \"20072281644\",\n        \"marktlokationsTyp\": [\n          {\n            \"typ\": \"STANDARD_MARKTLOKATION\"\n          }\n        ],\n        \"marktrollen\": [\n          {\n            \"boTyp\": \"MARKTTEILNEHMER\",\n            \"gewerbekennzeichnung\": true,\n            \"marktrolle\": \"UENB\",\n            \"rollencodenummer\": \"9911835000001\",\n            \"rollencodetyp\": \"BDEW\",\n            \"versionStruktur\": \"1\"\n          }\n        ],\n        \"regelzone\": \"10YDE-TSONET---I\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      },\n      {\n        \"bilanzierungsgebiet\": \"11YDE-DSONET---I\",\n        \"boTyp\": \"MARKTLOKATION\",\n        \"datenqualitaet\": \"ERWARTETE_DATEN\",\n        \"gueltigkeitszeitraum\": {\n          \"startdatum\": \"2025-07-23T22:00:00Z\",\n          \"zeitraumId\": 2\n        },\n        \"marktlokationsId\": \"20072281644\",\n        \"marktlokationsTyp\": [\n          {\n            \"typ\": \"STANDARD_MARKTLOKATION\"\n          }\n        ],\n        \"marktrollen\": [\n          {\n            \"boTyp\": \"MARKTTEILNEHMER\",\n            \"gewerbekennzeichnung\": true,\n            \"marktrolle\": \"UENB\",\n            \"rollencodenummer\": \"9911835000001\",\n            \"rollencodetyp\": \"BDEW\",\n            \"versionStruktur\": \"1\"\n          }\n        ],\n        \"regelzone\": \"10YDE-TSONET---I\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"VERWENDUNGSZEITRAUM\": [\n      {\n        \"boTyp\": \"VERWENDUNGSZEITRAUM\",\n        \"datenqualitaet\": \"ERWARTETE_DATEN\",\n        \"versionStruktur\": \"1\",\n        \"verwendungAb\": \"2025-06-23T22:00:00Z\",\n        \"verwendungBis\": \"2025-07-23T22:00:00Z\",\n        \"zeitraumId\": 1\n      },\n      {\n        \"boTyp\": \"VERWENDUNGSZEITRAUM\",\n        \"datenqualitaet\": \"ERWARTETE_DATEN\",\n        \"versionStruktur\": \"1\",\n        \"verwendungAb\": \"2025-07-23T22:00:00Z\",\n        \"zeitraumId\": 2\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"ansprechpartner\": {\n        \"boTyp\": \"ANSPRECHPARTNER\",\n        \"nachname\": \"P GETTY\",\n        \"rufnummern\": [\n          {\n            \"nummerntyp\": \"RUF_DURCHWAHL\",\n            \"rufnummer\": \"+3222271020\"\n          }\n        ],\n        \"versionStruktur\": \"1\"\n      },\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9903729000007\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"anfragereferenznummer\": \"NNV1234\",\n    \"antwortStatusZeitraum\": [\n      {\n        \"code\": \"A02\",\n        \"liste\": \"E_0611\",\n        \"zeitraumId\": 1\n      },\n      {\n        \"code\": \"A02\",\n        \"liste\": \"E_0611\",\n        \"zeitraumId\": 2\n      }\n    ],\n    \"datenaustauschreferenz\": \"DANXAGAAOOBGLF\",\n    \"dokumentennummer\": \"DA582411070841339903323000007433702\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9900327000009\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"E03\",\n    \"nachrichtendatum\": \"2025-06-24T12:31:00Z\",\n    \"nachrichtenreferenznummer\": \"DAWIJLVJWSUDJK\",\n    \"pruefidentifikator\": \"55156\",\n    \"sparte\": \"STROM\",\n    \"transaktionsgrund\": \"ZX3\",\n    \"vorgangsnummer\": \"24062416225400000000000102159662011\"\n  },\n  \"zusatzdaten\": {}\n}"} examples={[{"mediaType": "application/json", "examples": [{"name": "55156", "summary": "55156 — Rückmeldung/Anfrage Abr.-Daten BK-Abr. verb. MaLo", "value": {"stammdaten": {"VERWENDUNGSZEITRAUM": [{"boTyp": "VERWENDUNGSZEITRAUM", "versionStruktur": "1", "zeitraumId": 1, "datenqualitaet": "ERWARTETE_DATEN", "verwendungAb": "2025-06-23T22:00:00Z", "verwendungBis": "2025-07-23T22:00:00Z"}, {"boTyp": "VERWENDUNGSZEITRAUM", "versionStruktur": "1", "zeitraumId": 2, "datenqualitaet": "ERWARTETE_DATEN", "verwendungAb": "2025-07-23T22:00:00Z"}], "MARKTLOKATION": [{"boTyp": "MARKTLOKATION", "versionStruktur": "1", "marktlokationsId": "20072281644", "marktlokationsTyp": [{"typ": "STANDARD_MARKTLOKATION"}], "sparte": "STROM", "gueltigkeitszeitraum": {"zeitraumId": 1, "startdatum": "2025-06-23T22:00:00Z", "enddatum": "2025-07-23T22:00:00Z"}, "datenqualitaet": "ERWARTETE_DATEN", "bilanzierungsgebiet": "11YDE-DSONET---I", "marktrollen": [{"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "marktrolle": "UENB", "gewerbekennzeichnung": true, "rollencodenummer": "9911835000001", "rollencodetyp": "BDEW"}], "regelzone": "10YDE-TSONET---I"}, {"boTyp": "MARKTLOKATION", "versionStruktur": "1", "marktlokationsId": "20072281644", "marktlokationsTyp": [{"typ": "STANDARD_MARKTLOKATION"}], "sparte": "STROM", "gueltigkeitszeitraum": {"zeitraumId": 2, "startdatum": "2025-07-23T22:00:00Z"}, "datenqualitaet": "ERWARTETE_DATEN", "bilanzierungsgebiet": "11YDE-DSONET---I", "marktrollen": [{"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "marktrolle": "UENB", "gewerbekennzeichnung": true, "rollencodenummer": "9911835000001", "rollencodetyp": "BDEW"}], "regelzone": "10YDE-TSONET---I"}], "BILANZIERUNG": [{"boTyp": "BILANZIERUNG", "versionStruktur": "1", "gueltigkeitszeitraum": {"zeitraumId": 1, "startdatum": "2025-06-23T22:00:00Z", "enddatum": "2025-07-23T22:00:00Z"}, "datenqualitaet": "ERWARTETE_DATEN", "bilanzkreis": "11XBKA---------I", "aggregationsverantwortung": "VNB", "zeitreihentyp": "SLS", "prognosegrundlage": "PROFILE", "detailsPrognosegrundlage": ["SLP_SEP"]}, {"boTyp": "BILANZIERUNG", "versionStruktur": "1", "gueltigkeitszeitraum": {"zeitraumId": 2, "startdatum": "2025-07-23T22:00:00Z"}, "datenqualitaet": "ERWARTETE_DATEN", "bilanzkreis": "11XBKA---------I", "aggregationsverantwortung": "VNB", "zeitreihentyp": "SLS", "prognosegrundlage": "PROFILE", "detailsPrognosegrundlage": ["SLP_SEP"]}]}, "transaktionsdaten": {"datenaustauschreferenz": "DANXAGAAOOBGLF", "sparte": "STROM", "transaktionsgrund": "ZX3", "vorgangsnummer": "24062416225400000000000102159662011", "pruefidentifikator": "55156", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9903729000007", "rollencodetyp": "BDEW", "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "nachname": "P GETTY", "rufnummern": [{"nummerntyp": "RUF_DURCHWAHL", "rufnummer": "+3222271020"}]}}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900327000009", "rollencodetyp": "BDEW"}, "dokumentennummer": "DA582411070841339903323000007433702", "kategorie": "E03", "nachrichtendatum": "2025-06-24T12:31:00Z", "nachrichtenreferenznummer": "DAWIJLVJWSUDJK", "anfragereferenznummer": "NNV1234", "antwortStatusZeitraum": [{"code": "A02", "liste": "E_0611", "zeitraumId": 1}, {"code": "A02", "liste": "E_0611", "zeitraumId": 2}]}, "zusatzdaten": {}}}, {"name": "55673", "summary": "55673 — Rückmeldung/Anfrage Abr.-Daten BK-Abr. erz. Malo", "value": {"stammdaten": {"VERWENDUNGSZEITRAUM": [{"boTyp": "VERWENDUNGSZEITRAUM", "versionStruktur": "1", "zeitraumId": 1, "datenqualitaet": "ERWARTETE_DATEN", "verwendungAb": "2025-04-02T22:00:00Z"}], "MARKTLOKATION": [{"boTyp": "MARKTLOKATION", "versionStruktur": "1", "marktlokationsId": "50074561188", "marktlokationsTyp": [{"typ": "STANDARD_MARKTLOKATION"}], "sparte": "STROM", "gueltigkeitszeitraum": {"zeitraumId": 1, "startdatum": "2025-04-02T22:00:00Z"}, "datenqualitaet": "ERWARTETE_DATEN", "bilanzierungsgebiet": "11YR00000002596Z", "marktrollen": [{"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "marktrolle": "UENB", "gewerbekennzeichnung": true, "rollencodenummer": "4045399000077", "rollencodetyp": "BDEW"}], "regelzone": "10YDE-RWENET---I"}], "BILANZIERUNG": [{"boTyp": "BILANZIERUNG", "versionStruktur": "1", "gueltigkeitszeitraum": {"zeitraumId": 1, "startdatum": "2025-04-02T22:00:00Z"}, "datenqualitaet": "ERWARTETE_DATEN", "bilanzkreis": "11Y0-0000-0076-N", "aggregationsverantwortung": "UENB", "zeitreihentyp": "SES", "prognosegrundlage": "WERTE"}]}, "transaktionsdaten": {"datenaustauschreferenz": "M2YK1CNP", "sparte": "STROM", "transaktionsgrund": "ZX2", "transaktionsgrundergaenzung": "ZW3", "vorgangsnummer": "123456", "pruefidentifikator": "55673", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9903790000002", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900321000005", "rollencodetyp": "BDEW"}, "dokumentennummer": "BGMM3CXOLW4", "kategorie": "E03", "nachrichtendatum": "2025-04-04T12:00:00Z", "nachrichtenreferenznummer": "UNHM2PVLSIA", "anfragereferenznummer": "ABC123456", "antwortStatusZeitraum": [{"code": "A01", "liste": "E_0611", "zeitraumId": 1}, {"code": "A02", "liste": "E_0611", "zeitraumId": 2}]}, "zusatzdaten": {}}}]}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend fort, nachdem die Nachricht erstellt ist.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="3" anker="schritt-3" richtung="eingehend" kopf={{"links": {"label": "LF", "eigen": true}, "rechts": {"label": "NB"}}}>

### Bearbeitungsstand zur Rückmeldung

<Schrittskizze sicht={{"label": "LF"}} zeilen={[{"art": "empfangen", "label": "NB", "weg": "AS4", "nachrichten": [{"nr": "21047", "titel": "Bearbeitungsstandsmeldung"}]}, {"art": "aperak", "werte": ["Z33"]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [21047](/schnittstellen/202610/pruefi/IFTSTA/PI_21047) — Bearbeitungsstandsmeldung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **NB** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `21047` → [E_0619](/referenz/202610/ebd/E_0619) · NB · Rückmeldung prüfen (Basiert auf EBD: E_0626_Rückmeldung auf Änderung prüfen)

</div>

</li>

<li data-teil="aperak">

**Aperak-Prüfungen**
- `21047` → `Z33` — Aperak Prüfung: Ist referenzierte Nachricht bekannt ?

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

<Schritt nr="4" anker="schritt-4" richtung="fremd" kopf={{"links": {"label": "NB", "eigen": false}, "rechts": {"label": "ÜNB"}}}>

### Abrechnungsdaten Bilanzkreis-abrechnung vom NB an ÜNB

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55613](/schnittstellen/202610/pruefi/UTILMD/PI_55613) — Abr.-Daten BK-Abr. verb. MaLo · AS4
- [55674](/schnittstellen/202610/pruefi/UTILMD/PI_55674) — Abr.-Daten BK-Abr. erz. Malo · AS4

</div>

</Schritt>

<Schritt nr="5" anker="schritt-5" richtung="fremd" kopf={{"links": {"label": "ÜNB", "eigen": false}, "rechts": {"label": "NB"}}}>

### Rückmeldung auf Abrechnungsdaten

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55614](/schnittstellen/202610/pruefi/UTILMD/PI_55614) — Rückmeldung/Anfrage Abr.-Daten BK-Abr. verb. MaLo · AS4
- [55675](/schnittstellen/202610/pruefi/UTILMD/PI_55675) — Rückmeldung/Anfrage Abr.-Daten BK-Abr. erz. Malo · AS4

</div>

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `55614`, `55675` → [E_0612](/referenz/202610/ebd/E_0612) · ÜNB · Abrechnungsdaten Bilanzkreisabrechnung prüfen

</div>

</Schritt>

<Schritt nr="6" anker="schritt-6" richtung="fremd" kopf={{"links": {"label": "NB", "eigen": false}, "rechts": {"label": "ÜNB"}}}>

### Bearbeitungsstand zur Rückmeldung

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [21047](/schnittstellen/202610/pruefi/IFTSTA/PI_21047) — Bearbeitungsstandsmeldung · AS4

</div>

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `21047` → [E_0618](/referenz/202610/ebd/E_0618) · NB · Rückmeldung verarbeiten (Basiert auf EBD: E_0626_Rückmeldung auf Änderung prüfen)

</div>

</Schritt>

<details>
<summary>Entscheidungsbäume dieses Prozesses</summary>

| EBD | Name |
|---|---|
| [E_0611](/referenz/202610/ebd/E_0611) | Abrechnungsdaten Bilanzkreisabrechnung prüfen (Basiert auf EBD: E_0408_Änderung vom NB prüfen) |
| [E_0619](/referenz/202610/ebd/E_0619) | Rückmeldung prüfen (Basiert auf EBD: E_0626_Rückmeldung auf Änderung prüfen) |
| [E_0612](/referenz/202610/ebd/E_0612) | Abrechnungsdaten Bilanzkreisabrechnung prüfen |
| [E_0618](/referenz/202610/ebd/E_0618) | Rückmeldung verarbeiten (Basiert auf EBD: E_0626_Rückmeldung auf Änderung prüfen) |

</details>

<a id="abschnitt-informationen"></a>

## Prozess-Informationen

Wortlaut der Lesefassung, Steckbrief Kap. 3.1.2.1, S. 69–70.

<Stepper>
<ol>

<li data-blatt="vorbedingungen">

### Vorbedingungen

- Für die Übermittlung der Abrechnungsdaten zur Bilanzkreisabrechnung an den ÜNB gilt: Übermittlung, sofern die Aggregationsverantwortung
  - vom NB auf den ÜNB übergeht oder
  - beim ÜNB liegt und die Daten für den ÜNB relevant sind oder
  - vom ÜNB auf den NB übergeht.

</li>

<li data-blatt="ergebnisse">

### Ergebnisse

- Evtl. ist die Aktivierung von MaBiS-Zählpunkten für die Übermittlung von Summenzeitreihen nach MaBiS erforderlich.
- Sofern eine Stammdatenänderung erforderlich ist, führt der NB den Use-Case "Stammdatenänderung" (hier: SD „[Stammdatenänderung vom NB (verantwortlich) ausgehend](/prozessdoku/202610/LF/GPKE-Teil4-stammdatenaenderung-vom-nb-verantwortlich-ausgehend)“) (GPKE Teil 4) aus.
- Sofern es sich um eine Marktlokation bzw. Tranche mit Bilanzierung auf Basis von Viertelstundenwerten handelt: Der NB führt den Use-Case „[Stammdaten zur Bilanzkreistreue](/prozessdoku/202610/NB/GPKE-Teil4-stammdaten-zur-bilanzkreistreue)“ (GPKE Teil 4) aus.

</li>

<li data-blatt="anlass">

### Anlass

- Durchführung nach dem Prozessschritt
  - zur Zuordnung des LFN zur Marktlokation bzw. Tranche im Rahmen des Use-Cases „[Lieferbeginn](/prozessdoku/202610/LF--LFA/GPKE-Teil2-lieferbeginn)“ (Fall a).
  - zur Zuordnung des LF zur Marktlokation bzw. Tranche im Rahmen des Use-Cases „[Neuanlage](/prozessdoku/202610/LF/GPKE-Teil2-neuanlage)“ (Fall a).
  - zur Zuordnung des E/G zur verbrauchenden Marktlokation im Rahmen des Use-Cases „[Beginn der Ersatz-/Grundversorgung](/prozessdoku/202610/LF/GPKE-Teil2-beginn-der-ersatz-grundversorgung)“ (Fall a).
  - zur Zuordnung des LFN zur erzeugenden Marktlokation bzw. zur Tranche im Rahmen des Use-Cases „Herstellung einer 100% LF-Zuordnung zu einer erzeugenden Marktlokation“ (Fall a).
  - zur Beendigung der Zuordnung des LF zur Marktlokation bzw. Tranche im Rahmen des Use-Cases „[Lieferende von LF an NB](/prozessdoku/202610/LF/GPKE-Teil2-lieferende-von-lf-an-nb)“ (Fall a).
  - zur Beendigung der Zuordnung des LF zur Marktlokation bzw. Tranche im Rahmen des Use-Cases „[Lieferende von NB an LF](/prozessdoku/202610/LF/GPKE-Teil2-lieferende-von-nb-an-lf)“ (Fall a).
  - zum Bearbeitungsstand zur Bestellung im Rahmen des SD „[Bestellung einer Änderung von Abrechnungsdaten von LF an NB](/prozessdoku/202610/LF/GPKE-Teil2-bestellung-einer-aenderung-von-abrechnungsdaten-von-lf-an-nb)“, sofern eine Änderung der Abrechnungsdaten zur Bilanzkreisabrechnung vorzunehmen ist (Fall b).
  - zum Bearbeitungsstand zur Bestellung im Rahmen des SD „[Bestellung einer Änderung von Abrechnungsdaten zur Bilanzkreisabrechnung von ÜNB an NB](/prozessdoku/202610/NB/GPKE-Teil2-bestellung-einer-aenderung-von-abrechnungsdaten-zur-bilanzkreisabrechnung-von-uenb-an-nb)“, sofern eine Änderung der Abrechnungsdaten zur Bilanzkreisabrechnung vorzunehmen ist (Fall b).
- Durchführung unabhängig der obigen Prozesse,
  - sofern der NB selbst feststellt, dass sich Abrechnungsdaten zur Bilanzkreisabrechnung geändert haben (Fall b) (z.B. Änderung der Jahresverbrauchprognose). Dies gilt nicht für einen Wechsel des MSB im Rahmen der WiM Teil1.
  - sofern der NB davon ausgeht, dass ein Datenschiefstand zwischen NB und LF bzw. NB und ÜNB vorliegt (Fall b).
  - sofern der NB die Aggregationsverantwortung auf den ÜNB überträgt (Fall b).
  - sofern der NB die Aggregationsverantwortung auf den NB überträgt (Fall b).

**Vorher läuft:** [Beginn der Ersatz-/Grundversorgung](/prozessdoku/202610/LF/GPKE-Teil2-beginn-der-ersatz-grundversorgung), [Bestellung einer Änderung von Abrechnungsdaten von LF an NB](/prozessdoku/202610/LF/GPKE-Teil2-bestellung-einer-aenderung-von-abrechnungsdaten-von-lf-an-nb), [Bestellung einer Änderung von Abrechnungsdaten zur Bilanzkreisabrechnung von ÜNB an NB](/prozessdoku/202610/NB/GPKE-Teil2-bestellung-einer-aenderung-von-abrechnungsdaten-zur-bilanzkreisabrechnung-von-uenb-an-nb), [Fall 1: LF-Zuordnung bei EEG-Marktlokation ohne DV-Pflicht bzw. KWKG-Marktlokation ohne DV-Pflicht](/prozessdoku/202610/LF/GPKE-Teil2-fall-1-lf-zuordnung-bei-eeg-marktlokation-ohne-dv-pflicht-bzw-kwkg-marktlokation-ohne-dv-pflicht), [Fall 2: LF-Zuordnung bei EEG-Marktlokation mit DV-Pflicht](/prozessdoku/202610/LF--LFA/GPKE-Teil2-fall-2-lf-zuordnung-bei-eeg-marktlokation-mit-dv-pflicht), [Fall 3: LF-Zuordnung bei KWKG-Marktlokation mit DV-Pflicht bzw. Nicht-EEG-/Nicht-KWKG-Marktlokation und Marktlokation wird nicht-tranchiert abgebildet](/prozessdoku/202610/LF--LFA/GPKE-Teil2-fall-3-lf-zuordnung-bei-kwkg-marktlokation-mit-dv-pflicht-bzw-nicht-eeg-nicht-kwkg-marktlokation-und-marktlokation-wird-nicht-tranchiert-abgebildet), [Fall 4: LF-Zuordnung bei KWKG-Marktlokation mit DV-Pflicht bzw. Nicht-EEG-/Nicht-KWKG-Marktlokation und Marktlokation wird tranchiert abgebildet](/prozessdoku/202610/LF--LFA/GPKE-Teil2-fall-4-lf-zuordnung-bei-kwkg-marktlokation-mit-dv-pflicht-bzw-nicht-eeg-nicht-kwkg-marktlokation-und-marktlokation-wird-tranchiert-abgebildet), [Lieferbeginn](/prozessdoku/202610/LF--LFA/GPKE-Teil2-lieferbeginn), [Lieferende von LF an NB](/prozessdoku/202610/LF/GPKE-Teil2-lieferende-von-lf-an-nb), [Lieferende von NB an LF](/prozessdoku/202610/LF/GPKE-Teil2-lieferende-von-nb-an-lf), [Neuanlage](/prozessdoku/202610/LF/GPKE-Teil2-neuanlage) — diese Prozesse nennen den hier gezeigten in ihrem Ergebnis.

</li>

<li data-blatt="erste-nachricht">

### Erste Nachricht

**NB** sendet „Abrechnungsdaten Bilanzkreis-abrechnung vom NB an LF“ (Schritt 1). Ab hier ist der Beteiligte dieser Seite am Zug.

</li>

<li data-blatt="ziel">

### Ziel

Die Abrechnungsdaten zur Bilanzkreisabrechnung sind ausgetauscht.

</li>

</ol>
</Stepper>

<a id="abschnitt-sichten"></a>

## Andere Sichten des Prozesses

Derselbe Prozess, aus den Augen der anderen Beteiligten: dieselben Schritte, jeweils aus deren Sicht gelesen.

- [Sicht NB](/prozessdoku/202610/NB/GPKE-Teil2-abrechnungsdaten-bilanzkreisabrechnung) — NB
- [Sicht ÜNB](/prozessdoku/202610/UENB/GPKE-Teil2-abrechnungsdaten-bilanzkreisabrechnung) — ÜNB · Marktrolle UENB

<Hinweisbereich>

*Die Schritte sind die **möglichen** Nachrichten dieses Prozesses, keine Abfolge — die Quelle führt weder Bedingungen noch Alternativen. Das Kästchen am Schritt nennt links die eigene Sicht: **←** empfängt sie, **→** sendet sie. Zugeklappte Schritte laufen zwischen anderen Marktpartnern.*

Zu den Prüfidentifikatoren dieser Schritte liegt kein Testfall im Testbestand; der Knopf »Ausprobieren« der schreibenden Schnittstelle bietet deshalb keinen Rumpf an.

Betrifft: [3](#schritt-3)

</Hinweisbereich>
