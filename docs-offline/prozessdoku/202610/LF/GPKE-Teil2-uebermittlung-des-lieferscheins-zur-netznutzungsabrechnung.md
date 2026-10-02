# Übermittlung des Lieferscheins zur Netznutzungsabrechnung — Sicht LF

<Kopf rolle="LF" beteiligter="LF" festlegung="GPKE" dokument="GPKE Teil 2" kapitel="3.2.3.2" sparte="Strom" schritte={4} suchtitel="Übermittlung des Lieferscheins zur Netznutzungsabrechnung — Sicht LF · GPKE Teil 2 · Formatversion 202610" abschnitte={[{"id": "abschnitt-ablauf", "label": "Prozessablauf"}, {"id": "abschnitt-schritte", "label": "Prozessschritte"}, {"id": "abschnitt-informationen", "label": "Prozess-Informationen"}, {"id": "abschnitt-sichten", "label": "Andere Sichten des Prozesses"}]} />

<Kurzfassung>

Vor dem Versand der Netznutzungsrechnung übermittelt der NB an den LF die zugrundeliegenden Werte der Netznutzungsrechnung auf Ebene der Marktlokation. Je nach Auslöser kann es sich dabei um einen turnusmäßigen oder ereignisgesteuerten Versand eines Lieferscheines handeln. Sollten sich für den Zeitraum, der von einem Lieferschein umfasst wird, für den Lieferschein relevante Werte ändern, ist der bereits versendete Lieferschein, der die entsprechende Abrechnungsenergiemenge/Leistungswert enthält, vom NB zu stornieren. Anschließend ist ein neuer Lieferschein mit korrigierter Abrechnungsenergiemenge und ggf. korrigierten Leistungswerten an den LF zu versenden. Der Lieferschein enthält die Energiemenge(n) und das aufgetretene Jahresleistungsmaximum, welche auf der zugehörigen Netznutzungsrechnung abgerechnet werden. Ist nur die Abrechnungsenergiemenge oder der Leistungswert zu korrigieren, hat der neue Lieferschein die weiterhin richtige, nicht korrigierte Größe zu enthalten.

</Kurzfassung>

<a id="abschnitt-ablauf"></a>

## Prozessablauf aus Sicht des LF

<Systembild svg={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1004 1264\" width=\"1004\" height=\"1264\" role=\"img\" aria-labelledby=\"sb-title\" class=\"maco-systembild\">\n<title id=\"sb-title\">Systembild: Übermittlung des Lieferscheins zur Netznutzungsabrechnung aus Sicht LF</title>\n<defs><marker id=\"sb-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect class=\"sb-lane-kopf\" x=\"16\" y=\"12\" width=\"232\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend-System des Kunden</text>\n<rect class=\"sb-lane-kopf\" x=\"398\" y=\"12\" width=\"264\" height=\"46\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · LF</text>\n<rect class=\"sb-lane-kopf\" x=\"812\" y=\"12\" width=\"176\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"900\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Marktpartner</text>\n<line x1=\"323\" y1=\"58\" x2=\"323\" y2=\"1252\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"737\" y1=\"58\" x2=\"737\" y2=\"1252\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"80\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">1. Lieferschein</text>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"78\" r=\"5\"/><line x1=\"900\" y1=\"83\" x2=\"900\" y2=\"95\"/><line x1=\"893\" y1=\"87\" x2=\"907\" y2=\"87\"/><line x1=\"900\" y1=\"95\" x2=\"894\" y2=\"105\"/><line x1=\"900\" y1=\"95\" x2=\"906\" y2=\"105\"/></g>\n<text x=\"900\" y=\"127\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"878\" y1=\"96\" x2=\"628\" y2=\"96\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"88\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"112\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">13016, 13019</text>\n<rect class=\"sb-kasten sb-aperak_lesen\" x=\"432\" y=\"163\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"183\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Daten für die</text>\n<text x=\"530\" y=\"198\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Eingangsprüfung laden</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"113\" x2=\"530\" y2=\"163\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-aperak_lesen\" x=\"34\" y=\"163\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"183\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">3 Lese-Schnittstellen</text>\n<text x=\"132\" y=\"198\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">aufgerufen</text>\n<line x1=\"432\" y1=\"187\" x2=\"230\" y2=\"187\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"179\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<text x=\"331\" y=\"203\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">je einzeln am Schritt</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"237\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"257\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z33,</text>\n<text x=\"530\" y=\"272\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">MSCONS</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"211\" x2=\"530\" y2=\"237\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-schreiben\" x=\"432\" y=\"311\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"331\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"285\" x2=\"530\" y2=\"311\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-schreiben\" x=\"34\" y=\"311\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"331\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten erstellen</text>\n<line x1=\"432\" y1=\"327\" x2=\"230\" y2=\"327\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"319\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-lesen\" x=\"432\" y=\"375\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"395\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Daten für die Prüfung laden</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"344\" x2=\"530\" y2=\"375\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-lesen\" x=\"34\" y=\"367\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"387\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">2 Lese-Schnittstellen</text>\n<text x=\"132\" y=\"402\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">aufgerufen</text>\n<line x1=\"432\" y1=\"391\" x2=\"230\" y2=\"391\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"383\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<text x=\"331\" y=\"407\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">je einzeln am Schritt</text>\n<rect class=\"sb-kasten sb-ebd\" x=\"432\" y=\"449\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"469\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">EBD prüfen: E_0456</text>\n<text x=\"530\" y=\"484\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label-2, #424245)\">Lieferschein prüfen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"408\" x2=\"530\" y2=\"449\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-folgeprozess\" x=\"432\" y=\"523\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"543\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Folgeprozess auslösen:</text>\n<text x=\"530\" y=\"558\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">21035</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"497\" x2=\"530\" y2=\"523\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-folge_ausloeser\" x=\"432\" y=\"597\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"617\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Ausgelöst durch Eingang:</text>\n<text x=\"530\" y=\"632\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">13016, 13019</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"571\" x2=\"530\" y2=\"597\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"671\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"691\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">2. Rückmeldung auf</text>\n<text x=\"530\" y=\"706\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Lieferschein</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"645\" x2=\"530\" y2=\"671\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"677\" r=\"5\"/><line x1=\"900\" y1=\"682\" x2=\"900\" y2=\"694\"/><line x1=\"893\" y1=\"686\" x2=\"907\" y2=\"686\"/><line x1=\"900\" y1=\"694\" x2=\"894\" y2=\"704\"/><line x1=\"900\" y1=\"694\" x2=\"906\" y2=\"704\"/></g>\n<text x=\"900\" y=\"726\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"628\" y1=\"695\" x2=\"878\" y2=\"695\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"687\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"711\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">21035</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"754\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"774\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"719\" x2=\"530\" y2=\"754\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"754\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"774\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"770\" x2=\"230\" y2=\"770\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"762\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"818\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"838\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">3. Widerspruch gegen</text>\n<text x=\"530\" y=\"853\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Ablehnung</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"787\" x2=\"530\" y2=\"818\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"824\" r=\"5\"/><line x1=\"900\" y1=\"829\" x2=\"900\" y2=\"841\"/><line x1=\"893\" y1=\"833\" x2=\"907\" y2=\"833\"/><line x1=\"900\" y1=\"841\" x2=\"894\" y2=\"851\"/><line x1=\"900\" y1=\"841\" x2=\"906\" y2=\"851\"/></g>\n<text x=\"900\" y=\"873\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"878\" y1=\"842\" x2=\"628\" y2=\"842\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"834\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"858\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">29002</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"901\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"921\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z33</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"866\" x2=\"530\" y2=\"901\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"965\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"985\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"934\" x2=\"530\" y2=\"965\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"965\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"985\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"981\" x2=\"230\" y2=\"981\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"973\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"1029\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1049\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">4. Stornierung Lieferschein</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"998\" x2=\"530\" y2=\"1029\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"1027\" r=\"5\"/><line x1=\"900\" y1=\"1032\" x2=\"900\" y2=\"1044\"/><line x1=\"893\" y1=\"1036\" x2=\"907\" y2=\"1036\"/><line x1=\"900\" y1=\"1044\" x2=\"894\" y2=\"1054\"/><line x1=\"900\" y1=\"1044\" x2=\"906\" y2=\"1054\"/></g>\n<text x=\"900\" y=\"1076\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"878\" y1=\"1045\" x2=\"628\" y2=\"1045\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"1037\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"1061\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">13006</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"1112\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1132\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z33</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1062\" x2=\"530\" y2=\"1112\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-schreiben\" x=\"432\" y=\"1176\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1196\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1145\" x2=\"530\" y2=\"1176\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-schreiben\" x=\"34\" y=\"1176\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"1196\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten erstellen</text>\n<line x1=\"432\" y1=\"1192\" x2=\"230\" y2=\"1192\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"1184\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n</svg>"} gesamt={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 730 610\" width=\"730\" height=\"610\" role=\"img\" aria-labelledby=\"sd-title\" class=\"maco-sequence\">\n<title id=\"sd-title\">Sequenzdiagramm: Übermittlung des Lieferscheins zur Netznutzungsabrechnung aus Sicht LF</title>\n<defs><marker id=\"sd-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect x=\"16\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"121\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend (Kunde)</text>\n<line x1=\"121\" y1=\"64\" x2=\"121\" y2=\"598\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"260\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"365\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · LF</text>\n<line x1=\"365\" y1=\"64\" x2=\"365\" y2=\"598\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"504\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"609\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"609\" y1=\"64\" x2=\"609\" y2=\"598\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"609\" y1=\"90\" x2=\"365\" y2=\"90\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"81\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">1. Lieferschein</text>\n<text x=\"487\" y=\"105\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 13016, 13019</text>\n<line x1=\"365\" y1=\"152\" x2=\"121\" y2=\"152\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"143\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<text x=\"243\" y=\"167\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten erstellen</text>\n<line x1=\"365\" y1=\"214\" x2=\"609\" y2=\"214\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"205\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">2. Rückmeldung auf Lieferschein</text>\n<text x=\"487\" y=\"229\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 21035 · E_0456</text>\n<text x=\"487\" y=\"242\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0456 — Lieferschein prüfen</text>\n<line x1=\"365\" y1=\"276\" x2=\"121\" y2=\"276\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"267\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"291\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"609\" y1=\"338\" x2=\"365\" y2=\"338\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"329\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">3. Widerspruch gegen Ablehnung</text>\n<text x=\"487\" y=\"353\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 29002 · E_0458</text>\n<text x=\"487\" y=\"366\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0458 — Weitere Bearbeitung prüfen</text>\n<line x1=\"365\" y1=\"400\" x2=\"121\" y2=\"400\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"391\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"415\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"609\" y1=\"462\" x2=\"365\" y2=\"462\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"453\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">4. Stornierung Lieferschein</text>\n<text x=\"487\" y=\"477\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 13006</text>\n<line x1=\"365\" y1=\"524\" x2=\"121\" y2=\"524\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"515\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<text x=\"243\" y=\"539\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten erstellen</text>\n</svg>"} titel="LF" />

<a id="abschnitt-schritte"></a>

## Prozessschritte

<Schritt nr="1" anker="schritt-1" richtung="eingehend" kopf={{"links": {"label": "LF", "eigen": true}, "rechts": {"label": "NB"}}}>

### Lieferschein

<Schrittskizze sicht={{"label": "LF"}} zeilen={[{"art": "empfangen", "label": "NB", "weg": "AS4", "nachrichten": [{"nr": "13016", "titel": "Energiemenge u. Leistungsmax. (Strom)"}, {"nr": "13019", "titel": "Energiemenge (Strom)"}]}, {"art": "lesen_aperak", "schnittstellen": [{"label": "Marktlokation lesen"}, {"label": "Zähler lesen"}, {"label": "Messlokation lesen"}]}, {"art": "aperak", "werte": ["Z33", "MSCONS"]}, {"art": "erstellen"}, {"art": "lesen_ebd", "schnittstellen": [{"label": "Energiemengen aus Abrechnungskontext  lesen"}, {"label": "Netznutzungsvertrag lesen"}]}, {"art": "ebd", "baeume": [{"code": "E_0456", "titel": "Lieferschein prüfen"}]}, {"art": "folgeprozess", "werte": ["21035"]}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [13016](/schnittstellen/202610/pruefi/MSCONS/PI_13016) — Energiemenge u. Leistungsmax. (Strom) · AS4
- [13019](/schnittstellen/202610/pruefi/MSCONS/PI_13019) — Energiemenge (Strom) · AS4

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
- [Zähler lesen](/api/202610/backend-lesen/getcounterbasic#zahler-lesen) `GET /getCounterBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getCounterBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Messlokation lesen](/api/202610/backend-lesen/getmeterlocationbasic#messlokation-lesen) `GET /getMeterLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getMeterLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_MESSLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

</li>

<li data-teil="aperak">

**Aperak-Prüfungen**
- `13016`, `13019` → `Z33` — Aperak Prüfung: Ist referenzierte Nachricht bekannt ?
- `13016`, `13019` → `MSCONS`

</li>

<li data-teil="schnittstelle" data-art="schreiben">

**Schreibende Schnittstelle**
- Vorgang angelegt — [Prozessdaten erstellen](/api/202610/backend-schreiben-lf/createprocessdata#prozessdaten-erstellen) `POST /createProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/createProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": false, "defaultValue": "ERSTELLEN_PROZESSDATEN", "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"ENERGIEMENGE\": [\n      {\n        \"boTyp\": \"ENERGIEMENGE\",\n        \"energieverbrauch\": [\n          {\n            \"leistungsperiode\": \"20250901\",\n            \"messwertstatus\": \"ANGABE_FUER_LIEFERSCHEIN\",\n            \"obiskennzahl\": \"1-1:1.6.0\",\n            \"position\": 1,\n            \"wert\": 5000\n          }\n        ],\n        \"lokationsId\": \"50074561188\",\n        \"lokationsTyp\": \"MALO\",\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"marktrolle\": \"NB\",\n      \"rollencodenummer\": \"9900321000005\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"datenaustauschreferenz\": \"927877\",\n    \"dokumentennummer\": \"780170BGM\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"marktrolle\": \"LF\",\n      \"rollencodenummer\": \"9903790000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"Z42\",\n    \"nachrichtendatum\": \"2026-10-01T11:00:00Z\",\n    \"nachrichtenfunktion\": \"9\",\n    \"nachrichtenreferenznummer\": \"780170\",\n    \"pruefidentifikator\": \"13016\",\n    \"sparte\": \"STROM\",\n    \"typ\": \"EM\"\n  },\n  \"zusatzdaten\": {}\n}"} examples={[{"mediaType": "application/json", "examples": [{"name": "13016", "summary": "13016 — Energiemenge u. Leistungsmax. (Strom)", "value": {"stammdaten": {"ENERGIEMENGE": [{"boTyp": "ENERGIEMENGE", "versionStruktur": "1", "lokationsId": "50074561188", "lokationsTyp": "MALO", "energieverbrauch": [{"messwertstatus": "ANGABE_FUER_LIEFERSCHEIN", "obiskennzahl": "1-1:1.6.0", "wert": 5000, "leistungsperiode": "20250901", "position": 1}]}]}, "transaktionsdaten": {"datenaustauschreferenz": "927877", "sparte": "STROM", "pruefidentifikator": "13016", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "marktrolle": "NB", "rollencodenummer": "9900321000005", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "marktrolle": "LF", "rollencodenummer": "9903790000002", "rollencodetyp": "BDEW"}, "dokumentennummer": "780170BGM", "kategorie": "Z42", "nachrichtenfunktion": "9", "nachrichtendatum": "2026-10-01T11:00:00Z", "nachrichtenreferenznummer": "780170", "typ": "EM"}, "zusatzdaten": {}}}, {"name": "13019", "summary": "13019 — Energiemenge (Strom)", "value": {"stammdaten": {"ENERGIEMENGE": [{"boTyp": "ENERGIEMENGE", "versionStruktur": "1", "lokationsId": "DE0032106765712000000000000000037", "lokationsTyp": "MELO", "energieverbrauch": [{"startdatum": "2024-12-31T23:00:00Z", "enddatum": "2025-03-15T23:00:00Z", "messwertstatus": "ERSATZWERT", "statuszusatzinformationen": [{"art": "ERSATZWERTBILDUNGSVERFAHREN", "status": "INTERPOLATION"}, {"art": "GRUND_ERSATZWERTBILDUNGSVERFAHREN", "status": "KEIN_ZUGANG"}], "obiskennzahl": "1-0:1.8.0", "wert": 2000, "position": 1}]}]}, "transaktionsdaten": {"datenaustauschreferenz": "177706", "sparte": "STROM", "pruefidentifikator": "13019", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "marktrolle": "MSB", "rollencodenummer": "9904446000007", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9900321000005", "marktrolle": "NB", "rollencodetyp": "BDEW"}, "dokumentennummer": "039126BGM", "kategorie": "7", "nachrichtenfunktion": "9", "nachrichtendatum": "2026-10-01T11:00:00Z", "nachrichtenreferenznummer": "039126", "typ": "EM", "anfrageReferenz": "REF12345678910"}, "zusatzdaten": {}}}]}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Legt im Backend einen neuen Vorgang mit den Daten der eingegangenen Nachricht an.

</li>

<li data-teil="lesen" data-stufe="ebd">

**Daten für die Prüfung laden**
- [Energiemengen aus Abrechnungskontext  lesen](/api/202610/backend-lesen/getenergyamount#energiemengen-aus-abrechnungskontext-lesen) `GET /getEnergyAmount` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getEnergyAmount"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter5", "isRequired": false, "defaultValue": "123456789", "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_ENERGIEMENGE_ENERGIEMENGE", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Netznutzungsvertrag lesen](/api/202610/backend-lesen/getgridusagecontractbasic#netznutzungsvertrag-lesen) `GET /getGridUsageContractBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getGridUsageContractBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": false, "defaultValue": "MALO", "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": false, "defaultValue": "2024-06-28T12:18:00Z", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

</li>

<li data-teil="baum">

**Entscheidungsbaum**
- `13016`, `13019` → [E_0456](/referenz/202610/ebd/E_0456) — Lieferschein prüfen

</li>

<li data-teil="folgeprozess">

**Folgeprozess auslösen**
- [21035](/schnittstellen/202610/pruefi/IFTSTA/PI_21035) — Rückmeld. a. Liefers.

Nach der Verarbeitung startet die MACO APP diesen Folgeprozess selbst.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="2" anker="schritt-2" richtung="ausgehend" kopf={{"links": {"label": "LF", "eigen": true}, "rechts": {"label": "NB"}}}>

### Rückmeldung auf Lieferschein

<Schrittskizze sicht={{"label": "LF"}} zeilen={[{"art": "folge_ausloeser", "werte": ["13016", "13019"]}, {"art": "senden", "label": "NB", "weg": "AS4", "nachrichten": [{"nr": "21035", "titel": "Rückmeld. a. Liefers."}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [21035](/schnittstellen/202610/pruefi/IFTSTA/PI_21035) — Rückmeld. a. Liefers. · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="folge_ausloeser">

**Ausgelöst durch Eingang**
- [13016](/schnittstellen/202610/pruefi/MSCONS/PI_13016) — Energiemenge u. Leistungsmax. (Strom)
- [13019](/schnittstellen/202610/pruefi/MSCONS/PI_13019) — Energiemenge (Strom)

Die MACO APP sendet diese Nachricht selbst, als Folgeprozess nach einem dieser Eingänge.

</li>

<li data-teil="nachricht">

Nachricht an **NB** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `21035` → [E_0456](/referenz/202610/ebd/E_0456) · LF · Lieferschein prüfen

</div>

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202610/backend-schreiben-lf/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": false, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend fort, nachdem die Nachricht erstellt ist.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="3" anker="schritt-3" richtung="eingehend" kopf={{"links": {"label": "LF", "eigen": true}, "rechts": {"label": "NB"}}}>

### Widerspruch gegen Ablehnung

<Schrittskizze sicht={{"label": "LF"}} zeilen={[{"art": "empfangen", "label": "NB", "weg": "AS4", "nachrichten": [{"nr": "29002", "titel": "Ablehnung IFTSTA"}]}, {"art": "aperak", "werte": ["Z33"]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [29002](/schnittstellen/202610/pruefi/COMDIS/PI_29002) — Ablehnung IFTSTA · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **NB** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `29002` → [E_0458](/referenz/202610/ebd/E_0458) · Weitere Bearbeitung prüfen

</div>

</li>

<li data-teil="aperak">

**Aperak-Prüfungen**
- `29002` → `Z33` — Aperak Prüfung: Ist referenzierte Nachricht bekannt ?

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202610/backend-schreiben-lf/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": false, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"HANDELSUNSTIMMIGKEIT\": [\n      {\n        \"begruendung\": {\n          \"grund\": \"SONSTIGES_SIEHE_BEGRUENDUNG\",\n          \"hinweis\": \"Nach unserer Pruefung stimmen die Energiemengen ueberein.\"\n        },\n        \"boTyp\": \"HANDELSUNSTIMMIGKEIT\",\n        \"nummer\": \"P1000947628969\",\n        \"typ\": \"LIEFERSCHEIN_GRUND_ARBEITSPREIS\",\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"ansprechpartner\": {\n        \"boTyp\": \"ANSPRECHPARTNER\",\n        \"eMailAdresse\": \"Marktpartnerservice@ewe-netz.de\",\n        \"nachname\": \"Marktpartnerservice EWE NETZ GmbH\",\n        \"rufnummern\": [\n          {\n            \"nummerntyp\": \"FAX_DURCHWAHL\",\n            \"rufnummer\": \"+044148081195\"\n          },\n          {\n            \"nummerntyp\": \"RUF_DURCHWAHL\",\n            \"rufnummer\": \"+044148085454\"\n          }\n        ],\n        \"versionStruktur\": \"1\"\n      },\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9900496000005\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"antwortstatusCodeliste\": \"S_0108\",\n    \"datenaustauschreferenz\": \"P1000947962141\",\n    \"dokumentennummer\": \"P1000947962142\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9905079000000\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"739\",\n    \"nachrichtendatum\": \"2024-04-03T21:12:00Z\",\n    \"nachrichtenreferenznummer\": \"P1000947962142\",\n    \"pruefidentifikator\": \"29002\",\n    \"sparte\": \"STROM\"\n  },\n  \"zusatzdaten\": {}\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend mit den Daten der eingegangenen Nachricht fort.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="4" anker="schritt-4" richtung="eingehend" kopf={{"links": {"label": "LF", "eigen": true}, "rechts": {"label": "NB"}}}>

### Stornierung Lieferschein

<Schrittskizze sicht={{"label": "LF"}} zeilen={[{"art": "empfangen", "label": "NB", "weg": "AS4", "nachrichten": [{"nr": "13006", "titel": "Messwert Storno"}]}, {"art": "aperak", "werte": ["Z33"]}, {"art": "erstellen"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [13006](/schnittstellen/202610/pruefi/MSCONS/PI_13006) — Messwert Storno · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **NB** · AS4

</li>

<li data-teil="aperak">

**Aperak-Prüfungen**
- `13006` → `Z33` — Aperak Prüfung: Ist referenzierte Nachricht bekannt ?

</li>

<li data-teil="schnittstelle" data-art="schreiben">

**Schreibende Schnittstelle**
- Vorgang angelegt — [Prozessdaten erstellen](/api/202610/backend-schreiben-lf/createprocessdata#prozessdaten-erstellen) `POST /createProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/createProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": false, "defaultValue": "ERSTELLEN_PROZESSDATEN", "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {},\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9904446000007\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"datenaustauschreferenz\": \"978509\",\n    \"dokumentennummer\": \"542637BGM\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9900321000005\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"7\",\n    \"nachrichtendatum\": \"2026-10-01T11:00:00Z\",\n    \"nachrichtenfunktion\": \"1\",\n    \"nachrichtenreferenznummer\": \"542637\",\n    \"pruefidentifikator\": \"13006\",\n    \"sparte\": \"STROM\",\n    \"typ\": \"VL\",\n    \"vorgangsreferenznummer\": \"REF123456789\"\n  },\n  \"zusatzdaten\": {}\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

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
| [E_0456](/referenz/202610/ebd/E_0456) | Lieferschein prüfen |
| [E_0458](/referenz/202610/ebd/E_0458) | Weitere Bearbeitung prüfen |

</details>

<a id="abschnitt-informationen"></a>

## Prozess-Informationen

Wortlaut der Lesefassung, Steckbrief Kap. 3.2.3.1, S. 84–86.

<Stepper>
<ol>

<li data-blatt="vorbedingungen">

### Vorbedingungen

- Es handelt sich um eine verbrauchende Marktlokation.
- Der LF ist Zahler der Netznutzung.
- Werte vom MSB liegen vor.
- Die bisher gemessenen Arbeits- und Leistungswerte bei unterjährigem Zuordnungsbeginn und wenn die Marktlokation mit Arbeits- und Leistungspreis abgerechnet wird, sind vom NB an den LF übermittelt.
- Die Abrechnung der Netznutzung soll gestellt werden.
- Sofern der Bedarf der Anwendung einer Zählzeitdefinition des NB mit Zählzeitenanwendungszweck „Netznutzung“ vorliegt, muss eine entsprechende Konfiguration fristgerecht und erfolgreich über die Use-Cases im Kapitel „Bestellung einer Konfiguration“ (GPKE Teil 3) eingerichtet worden sein. Dies gilt nur, wenn die bestellte Einrichtung einer Konfiguration in den abrechnungsrelevanten Zeitraum des zu erstellenden Lieferscheines fällt.
- Die für die Netznutzungsabrechnung notwendigen Informationen wurden über den Use-Case „[Abrechnungsdaten Netznutzungsabrechnung](/prozessdoku/202610/LF/GPKE-Teil2-abrechnungsdaten-netznutzungsabrechnung)“ übermittelt.

</li>

<li data-blatt="ergebnisse">

### Ergebnisse

Eine Netznutzungsrechnung kann gestellt werden.

</li>

<li data-blatt="fehlerfall">

### Fehlerfall

#### Ergebnis im Fehlerfall

Ein Lieferschein muss erneut übermittelt werden.

</li>

<li data-blatt="anforderungen">

### Weitere Anforderungen

Eine Position in der Netznutzungsrechnung muss durch eine Position oder durch Addition von mehreren Positionen aus dem Lieferschein zeitlich eindeutig zugeordnet und geprüft werden können. Dies ist vom NB beim Aufbau des Lieferscheins zu berücksichtigen.

</li>

<li data-blatt="anlass">

### Anlass

- Das Ende des Abrechnungszeitraums ist erreicht oder
- ein Lieferendeprozess wurde durchgeführt oder
- eine Änderung des Zahlers der Netznutzung liegt vor oder
- ein Netzbetreiberwechsel wurde durchgeführt oder
- der Wechsel zwischen dem Modell Grundpreis/Arbeitspreis und Arbeitspreis/Leistungspreis wurde vorgenommen.

</li>

<li data-blatt="erste-nachricht">

### Erste Nachricht

**NB** sendet „Lieferschein“ (Schritt 1). Ab hier ist der Beteiligte dieser Seite am Zug.

</li>

<li data-blatt="ziel">

### Ziel

Dem LF liegt der Lieferschein der Abrechnungsenergiemengen/Leistungswerte vor, welcher eine der Grundlagen für die Netznutzungsabrechnung bildet.

</li>

</ol>
</Stepper>

<a id="abschnitt-sichten"></a>

## Andere Sichten des Prozesses

Derselbe Prozess, aus den Augen der anderen Beteiligten: dieselben Schritte, jeweils aus deren Sicht gelesen.

- [Sicht NB](/prozessdoku/202610/NB/GPKE-Teil2-uebermittlung-des-lieferscheins-zur-netznutzungsabrechnung) — NB

<Hinweisbereich>

*Die Schritte sind die **möglichen** Nachrichten dieses Prozesses, keine Abfolge — die Quelle führt weder Bedingungen noch Alternativen. Das Kästchen am Schritt nennt links die eigene Sicht: **←** empfängt sie, **→** sendet sie. Zugeklappte Schritte laufen zwischen anderen Marktpartnern.*

Zu den Prüfidentifikatoren dieser Schritte liegt kein Testfall im Testbestand; der Knopf »Ausprobieren« der schreibenden Schnittstelle bietet deshalb keinen Rumpf an.

Betrifft: [2](#schritt-2)

</Hinweisbereich>
