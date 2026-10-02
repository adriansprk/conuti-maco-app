# Stammdatenänderung vom MSB (verantwortlich) ausgehend — Sicht NB

<Kopf rolle="NB" beteiligter="NB" festlegung="GPKE" dokument="GPKE Teil 4" kapitel="1.4.4" sparte="Strom" schritte={12} suchtitel="Stammdatenänderung vom MSB (verantwortlich) ausgehend — Sicht NB · GPKE Teil 4 · Formatversion 202604" abschnitte={[{"id": "abschnitt-ablauf", "label": "Prozessablauf"}, {"id": "abschnitt-schritte", "label": "Prozessschritte"}, {"id": "abschnitt-informationen", "label": "Prozess-Informationen"}, {"id": "abschnitt-sichten", "label": "Andere Sichten des Prozesses"}]} />

<Kurzfassung>

Der Prozess beschreibt die Übermittlung von geänderten Werten von Stammdaten vom Verantwortlichen an die Berechtigten. Der Berechtigte prüft die Daten und gibt dem Verantwortlichen eine Qualitätsrückmeldung zum Inhalt der Daten. Sofern der Berechtigte einen anderen Inhalt der Daten erwartet, gibt er dies in der Rückmeldung an. Der Verantwortliche teilt dem Berechtigten in diesem Fall den Bearbeitungstand zu dessen Rückmeldung mit.

</Kurzfassung>

<a id="abschnitt-ablauf"></a>

## Prozessablauf aus Sicht des NB

<Systembild svg={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1004 1330\" width=\"1004\" height=\"1330\" role=\"img\" aria-labelledby=\"sb-title\" class=\"maco-systembild\">\n<title id=\"sb-title\">Systembild: Stammdatenänderung vom MSB (verantwortlich) ausgehend aus Sicht NB</title>\n<defs><marker id=\"sb-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect class=\"sb-lane-kopf\" x=\"16\" y=\"12\" width=\"232\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend-System des Kunden</text>\n<rect class=\"sb-lane-kopf\" x=\"398\" y=\"12\" width=\"264\" height=\"46\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · NB</text>\n<rect class=\"sb-lane-kopf\" x=\"812\" y=\"12\" width=\"176\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"900\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Marktpartner</text>\n<line x1=\"323\" y1=\"58\" x2=\"323\" y2=\"1318\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"737\" y1=\"58\" x2=\"737\" y2=\"1318\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"80\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">1. Änderung vom MSB an NB</text>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"78\" r=\"5\"/><line x1=\"900\" y1=\"83\" x2=\"900\" y2=\"95\"/><line x1=\"893\" y1=\"87\" x2=\"907\" y2=\"87\"/><line x1=\"900\" y1=\"95\" x2=\"894\" y2=\"105\"/><line x1=\"900\" y1=\"95\" x2=\"906\" y2=\"105\"/></g>\n<text x=\"900\" y=\"127\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">MSB</text>\n<line x1=\"878\" y1=\"96\" x2=\"628\" y2=\"96\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"88\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"112\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">55557, 55553, 55639…</text>\n<rect class=\"sb-kasten sb-aperak_lesen\" x=\"432\" y=\"163\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"183\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Daten für die</text>\n<text x=\"530\" y=\"198\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Eingangsprüfung laden</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"113\" x2=\"530\" y2=\"163\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-aperak_lesen\" x=\"34\" y=\"163\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"183\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">5 Lese-Schnittstellen</text>\n<text x=\"132\" y=\"198\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">aufgerufen</text>\n<line x1=\"432\" y1=\"187\" x2=\"230\" y2=\"187\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"179\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<text x=\"331\" y=\"203\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">je einzeln am Schritt</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"237\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"257\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z10, Z16,</text>\n<text x=\"530\" y=\"272\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Z33</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"211\" x2=\"530\" y2=\"237\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-schreiben\" x=\"432\" y=\"311\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"331\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"285\" x2=\"530\" y2=\"311\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-schreiben\" x=\"34\" y=\"311\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"331\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten erstellen</text>\n<line x1=\"432\" y1=\"327\" x2=\"230\" y2=\"327\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"319\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"375\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"395\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"344\" x2=\"530\" y2=\"375\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"375\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"395\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"391\" x2=\"230\" y2=\"391\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"383\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<text x=\"331\" y=\"407\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">PI 55553</text>\n<rect class=\"sb-kasten sb-ebd\" x=\"432\" y=\"439\" width=\"196\" height=\"93\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"459\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">EBD prüfen: E_0415</text>\n<text x=\"530\" y=\"474\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label-2, #424245)\">Änderung vom MSB prüfen</text>\n<text x=\"530\" y=\"489\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label-2, #424245)\">(Basiert auf EBD:</text>\n<text x=\"530\" y=\"504\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label-2, #424245)\">E_0408_Änderung vom NB</text>\n<text x=\"530\" y=\"519\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label-2, #424245)\">prüfen)</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"408\" x2=\"530\" y2=\"439\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-folgeprozess\" x=\"432\" y=\"558\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"578\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Folgeprozess auslösen:</text>\n<text x=\"530\" y=\"593\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">55555, 55559, 55644,</text>\n<text x=\"530\" y=\"608\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">55645, 55646, 5…</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"532\" x2=\"530\" y2=\"558\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-folge_ausloeser\" x=\"432\" y=\"647\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"667\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Ausgelöst durch Eingang:</text>\n<text x=\"530\" y=\"682\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">55553, 55557, 55639,</text>\n<text x=\"530\" y=\"697\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">55640, 55641,…</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"621\" x2=\"530\" y2=\"647\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-trigger\" x=\"432\" y=\"736\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"756\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessauslöser empfangen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"710\" x2=\"530\" y2=\"736\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-trigger\" x=\"34\" y=\"736\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"756\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">START_BESTELLUNG_SDAE</text>\n<line x1=\"230\" y1=\"752\" x2=\"432\" y2=\"752\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"744\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-lesen_verarbeitung\" x=\"432\" y=\"800\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"820\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Daten für die Verarbeitung</text>\n<text x=\"530\" y=\"835\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">laden</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"769\" x2=\"530\" y2=\"800\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-lesen_verarbeitung\" x=\"34\" y=\"800\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"820\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">5 Lese-Schnittstellen</text>\n<text x=\"132\" y=\"835\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">aufgerufen</text>\n<line x1=\"432\" y1=\"824\" x2=\"230\" y2=\"824\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"816\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<text x=\"331\" y=\"840\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">je einzeln am Schritt</text>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"874\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"894\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">2. Rückmeldung auf</text>\n<text x=\"530\" y=\"909\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Änderung</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"848\" x2=\"530\" y2=\"874\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"880\" r=\"5\"/><line x1=\"900\" y1=\"885\" x2=\"900\" y2=\"897\"/><line x1=\"893\" y1=\"889\" x2=\"907\" y2=\"889\"/><line x1=\"900\" y1=\"897\" x2=\"894\" y2=\"907\"/><line x1=\"900\" y1=\"897\" x2=\"906\" y2=\"907\"/></g>\n<text x=\"900\" y=\"929\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">MSB</text>\n<line x1=\"628\" y1=\"898\" x2=\"878\" y2=\"898\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"890\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"914\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">55559, 55555, 55644…</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"957\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"977\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"922\" x2=\"530\" y2=\"957\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"957\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"977\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"973\" x2=\"230\" y2=\"973\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"965\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"1021\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1041\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">3. Bearbeitungsstand zur</text>\n<text x=\"530\" y=\"1056\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Rückmeldung</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"990\" x2=\"530\" y2=\"1021\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"1027\" r=\"5\"/><line x1=\"900\" y1=\"1032\" x2=\"900\" y2=\"1044\"/><line x1=\"893\" y1=\"1036\" x2=\"907\" y2=\"1036\"/><line x1=\"900\" y1=\"1044\" x2=\"894\" y2=\"1054\"/><line x1=\"900\" y1=\"1044\" x2=\"906\" y2=\"1054\"/></g>\n<text x=\"900\" y=\"1076\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">MSB</text>\n<line x1=\"878\" y1=\"1045\" x2=\"628\" y2=\"1045\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"1037\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"1061\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">21047</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"1104\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1124\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z33</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1069\" x2=\"530\" y2=\"1104\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"1168\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1188\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1137\" x2=\"530\" y2=\"1168\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"1168\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"1188\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"1184\" x2=\"230\" y2=\"1184\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"1176\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-folgeprozess\" x=\"432\" y=\"1232\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1252\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Folgeprozess auslösen:</text>\n<text x=\"530\" y=\"1267\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">21047</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1201\" x2=\"530\" y2=\"1232\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n</svg>"} gesamt={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1462 1168\" width=\"1462\" height=\"1168\" role=\"img\" aria-labelledby=\"sd-title\" class=\"maco-sequence\">\n<title id=\"sd-title\">Sequenzdiagramm: Stammdatenänderung vom MSB (verantwortlich) ausgehend aus Sicht NB</title>\n<defs><marker id=\"sd-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect x=\"16\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"121\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend (Kunde)</text>\n<line x1=\"121\" y1=\"64\" x2=\"121\" y2=\"1156\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"260\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"365\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · NB</text>\n<line x1=\"365\" y1=\"64\" x2=\"365\" y2=\"1156\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"504\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"609\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">MSB</text>\n<line x1=\"609\" y1=\"64\" x2=\"609\" y2=\"1156\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"748\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"853\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">LF</text>\n<line x1=\"853\" y1=\"64\" x2=\"853\" y2=\"1156\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"992\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"1097\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">weiterer MSB</text>\n<line x1=\"1097\" y1=\"64\" x2=\"1097\" y2=\"1156\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"1236\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"1341\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">ÜNB</text>\n<line x1=\"1341\" y1=\"64\" x2=\"1341\" y2=\"1156\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"609\" y1=\"90\" x2=\"365\" y2=\"90\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"81\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">1. Änderung vom MSB an NB</text>\n<text x=\"487\" y=\"105\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55557, 55553, 55639…</text>\n<line x1=\"365\" y1=\"152\" x2=\"121\" y2=\"152\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"143\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<text x=\"243\" y=\"167\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten erstellen</text>\n<line x1=\"365\" y1=\"214\" x2=\"121\" y2=\"214\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"205\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"229\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren · PI 55553</text>\n<line x1=\"121\" y1=\"276\" x2=\"365\" y2=\"276\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"267\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">START_BESTELLUNG_SDAE</text>\n<text x=\"243\" y=\"291\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Trigger-Event</text>\n<line x1=\"365\" y1=\"338\" x2=\"609\" y2=\"338\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"329\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">2. Rückmeldung auf Änderung</text>\n<text x=\"487\" y=\"353\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55559, 55555, 55644… · E_0415</text>\n<text x=\"487\" y=\"366\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0415 — Änderung vom MSB prüfen</text>\n<line x1=\"365\" y1=\"400\" x2=\"121\" y2=\"400\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"391\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"415\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"609\" y1=\"462\" x2=\"365\" y2=\"462\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"453\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">3. Bearbeitungsstand zur Rückmeldung</text>\n<text x=\"487\" y=\"477\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 21047 · E_0632</text>\n<text x=\"487\" y=\"490\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0632 — Rückmeldung auf Änderung prüfen</text>\n<line x1=\"365\" y1=\"524\" x2=\"121\" y2=\"524\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"515\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"539\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"609\" y1=\"586\" x2=\"853\" y2=\"586\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"731\" y=\"577\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">4. Änderung vom MSB an LF</text>\n<text x=\"731\" y=\"601\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55649, 55553, 55650…</text>\n<line x1=\"853\" y1=\"648\" x2=\"609\" y2=\"648\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"731\" y=\"639\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">5. Rückmeldung auf Änderung</text>\n<text x=\"731\" y=\"663\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55654, 55555, 55655… · E_0412</text>\n<text x=\"731\" y=\"676\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0412 — Änderung vom MSB prüfen</text>\n<line x1=\"609\" y1=\"710\" x2=\"853\" y2=\"710\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"731\" y=\"701\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">6. Bearbeitungsstand zur Rückmeldung</text>\n<text x=\"731\" y=\"725\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 21047 · E_0633</text>\n<text x=\"731\" y=\"738\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0633 — Rückmeldung auf Änderung prüfen</text>\n<line x1=\"609\" y1=\"772\" x2=\"1097\" y2=\"772\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"853\" y=\"763\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">7. Änderung vom MSB an weiteren MSB</text>\n<text x=\"853\" y=\"787\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55659, 55553, 55660…</text>\n<line x1=\"1097\" y1=\"834\" x2=\"609\" y2=\"834\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"853\" y=\"825\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">8. Rückmeldung auf Änderung</text>\n<text x=\"853\" y=\"849\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55664, 55555, 55665… · E_0583</text>\n<text x=\"853\" y=\"862\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0583 — Änderung vom MSB prüfen</text>\n<line x1=\"609\" y1=\"896\" x2=\"1097\" y2=\"896\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"853\" y=\"887\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">9. Bearbeitungsstand zur Rückmeldung</text>\n<text x=\"853\" y=\"911\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 21047 · E_0634</text>\n<text x=\"853\" y=\"924\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0634 — Rückmeldung auf Änderung prüfen</text>\n<line x1=\"609\" y1=\"958\" x2=\"1341\" y2=\"958\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"975\" y=\"949\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">11. Änderung vom MSB an ÜNB</text>\n<text x=\"975\" y=\"973\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55684, 55686</text>\n<line x1=\"1341\" y1=\"1020\" x2=\"609\" y2=\"1020\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"975\" y=\"1011\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">12. Rückmeldung auf Änderung</text>\n<text x=\"975\" y=\"1035\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55685, 55687 · E_0639</text>\n<text x=\"975\" y=\"1048\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0639 — Änderung vom MSB prüfen</text>\n<line x1=\"609\" y1=\"1082\" x2=\"1341\" y2=\"1082\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"975\" y=\"1073\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">13. Bearbeitungsstand zur Rückmeldung</text>\n<text x=\"975\" y=\"1097\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 21047 · E_0635</text>\n<text x=\"975\" y=\"1110\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0635 — Rückmeldung auf Änderung prüfen</text>\n</svg>"} titel="NB" />

<a id="abschnitt-schritte"></a>

## Prozessschritte

<Schritt nr="1" anker="schritt-1" richtung="eingehend" kopf={{"links": {"label": "NB", "eigen": true}, "rechts": {"label": "MSB"}}}>

### Änderung vom MSB an NB

<Schrittskizze sicht={{"label": "NB"}} zeilen={[{"art": "empfangen", "label": "MSB", "weg": "AS4", "nachrichten": [{"nr": "55557", "titel": "Änderung MSB-Abr.-Daten der MaLo"}, {"nr": "55553", "titel": "Daten auf individuelle Bestellung"}, {"nr": "55639", "titel": "Änderung Daten der NeLo"}, {"nr": "55640", "titel": "Änderung Daten der MaLo"}, {"nr": "55641", "titel": "Änderung Daten der SR"}, {"nr": "55642", "titel": "Änderung Daten der Tranche"}, {"nr": "55643", "titel": "Änderung Daten der MeLo"}]}, {"art": "lesen_aperak", "schnittstellen": [{"label": "Marktlokation lesen"}, {"label": "Netzlokation lesen"}, {"label": "Steuerbare Ressource lesen"}, {"label": "Tranche lesen"}, {"label": "Messlokation lesen"}]}, {"art": "aperak", "werte": ["Z10", "Z16", "Z33"]}, {"art": "erstellen"}, {"art": "fortschreiben", "nummern": ["55553"]}, {"art": "ebd", "baeume": [{"code": "E_0415", "titel": "Änderung vom MSB prüfen (Basiert auf EBD: E_0408_Änderung vom NB prüfen)"}]}, {"art": "folgeprozess", "werte": ["55555", "55559", "55644", "55645", "55646", "55647", "55648"]}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55557](/schnittstellen/202604/pruefi/UTILMD/PI_55557) — Änderung MSB-Abr.-Daten der MaLo · AS4
- [55553](/schnittstellen/202604/pruefi/UTILMD/PI_55553) — Daten auf individuelle Bestellung · AS4
- [55639](/schnittstellen/202604/pruefi/UTILMD/PI_55639) — Änderung Daten der NeLo · AS4
- [55640](/schnittstellen/202604/pruefi/UTILMD/PI_55640) — Änderung Daten der MaLo · AS4
- [55641](/schnittstellen/202604/pruefi/UTILMD/PI_55641) — Änderung Daten der SR · AS4
- [55642](/schnittstellen/202604/pruefi/UTILMD/PI_55642) — Änderung Daten der Tranche · AS4
- [55643](/schnittstellen/202604/pruefi/UTILMD/PI_55643) — Änderung Daten der MeLo · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **MSB** · AS4

</li>

<li data-teil="lesen" data-stufe="aperak">

**Daten für die Eingangsprüfung laden**
- [Marktlokation lesen](/api/202604/backend-lesen/getmarketlocationbasic#marktlokation-lesen) `GET /getMarketLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getMarketLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": false, "defaultValue": "MALO", "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": false, "defaultValue": "2024-06-28T12:18:00Z", "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_MARKTLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Netzlokation lesen](/api/202604/backend-lesen/getgridlocationbasic#netzlokation-lesen) `GET /getGridLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getGridLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_NETZLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Steuerbare Ressource lesen](/api/202604/backend-lesen/getcontrollableresourcebasic#steuerbare-ressource-lesen) `GET /getControllableResourceBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getControllableResourceBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Tranche lesen](/api/202604/backend-lesen/gettranchebasic#tranche-lesen) `GET /getTrancheBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getTrancheBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Messlokation lesen](/api/202604/backend-lesen/getmeterlocationbasic#messlokation-lesen) `GET /getMeterLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getMeterLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_MESSLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

</li>

<li data-teil="aperak">

**Aperak-Prüfungen**
- `55557`, `55639`, `55640`, `55641`, `55642`, `55643` → `Z10`
- `55557`, `55639`, `55640`, `55641`, `55642`, `55643` → `Z16`
- `55553` → `Z33`

</li>

<li data-teil="schnittstelle" data-art="schreiben">

**Schreibende Schnittstelle**
- Vorgang angelegt — [Prozessdaten erstellen](/api/202604/backend-schreiben-nb/createprocessdata#prozessdaten-erstellen) `POST /createProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/createProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "ERSTELLEN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"MARKTLOKATION\": [\n      {\n        \"boTyp\": \"MARKTLOKATION\",\n        \"datenqualitaet\": \"GUELTIGE_DATEN\",\n        \"gueltigkeitszeitraum\": {\n          \"startdatum\": \"2025-06-30T22:00:00Z\",\n          \"zeitraumId\": 1\n        },\n        \"marktlokationsId\": \"50074561188\",\n        \"marktlokationsTyp\": [\n          {\n            \"typ\": \"STANDARD_MARKTLOKATION\"\n          }\n        ],\n        \"messstellenbetriebsabrechnungsdaten\": [\n          {\n            \"anzahl\": 1,\n            \"artikelId\": \"1-06-7-004\",\n            \"artikelIdTyp\": \"ARTIKELID\",\n            \"messstellenbetriebsabrechnung\": true\n          }\n        ],\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"VERWENDUNGSZEITRAUM\": [\n      {\n        \"boTyp\": \"VERWENDUNGSZEITRAUM\",\n        \"datenqualitaet\": \"GUELTIGE_DATEN\",\n        \"versionStruktur\": \"1\",\n        \"verwendungAb\": \"2025-06-30T22:00:00Z\",\n        \"zeitraumId\": 1\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9904446000007\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"datenaustauschreferenz\": \"LZQV1FTH\",\n    \"dokumentennummer\": \"BGMM097DLXC\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9900321000005\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"E03\",\n    \"nachrichtendatum\": \"2025-04-04T12:00:00Z\",\n    \"nachrichtenreferenznummer\": \"UNHLZPSZ8H2\",\n    \"pruefidentifikator\": \"55557\",\n    \"sparte\": \"STROM\",\n    \"transaktionsgrund\": \"ZU1\",\n    \"verwendungAb\": \"2025-04-04T22:00:00Z\",\n    \"vorgangsnummer\": \"123456\"\n  },\n  \"zusatzdaten\": {}\n}"} examples={[{"mediaType": "application/json", "examples": [{"name": "55557", "summary": "55557 — Änderung MSB-Abr.-Daten der MaLo", "value": {"stammdaten": {"VERWENDUNGSZEITRAUM": [{"boTyp": "VERWENDUNGSZEITRAUM", "versionStruktur": "1", "verwendungAb": "2025-06-30T22:00:00Z", "zeitraumId": 1, "datenqualitaet": "GUELTIGE_DATEN"}], "MARKTLOKATION": [{"boTyp": "MARKTLOKATION", "versionStruktur": "1", "marktlokationsId": "50074561188", "marktlokationsTyp": [{"typ": "STANDARD_MARKTLOKATION"}], "sparte": "STROM", "gueltigkeitszeitraum": {"zeitraumId": 1, "startdatum": "2025-06-30T22:00:00Z"}, "datenqualitaet": "GUELTIGE_DATEN", "messstellenbetriebsabrechnungsdaten": [{"messstellenbetriebsabrechnung": true, "artikelId": "1-06-7-004", "artikelIdTyp": "ARTIKELID", "anzahl": 1}]}]}, "transaktionsdaten": {"datenaustauschreferenz": "LZQV1FTH", "sparte": "STROM", "transaktionsgrund": "ZU1", "vorgangsnummer": "123456", "pruefidentifikator": "55557", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9904446000007", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9900321000005", "rollencodetyp": "BDEW"}, "dokumentennummer": "BGMM097DLXC", "kategorie": "E03", "nachrichtendatum": "2025-04-04T12:00:00Z", "nachrichtenreferenznummer": "UNHLZPSZ8H2", "verwendungAb": "2025-04-04T22:00:00Z"}, "zusatzdaten": {}}}, {"name": "55553", "summary": "55553 — Daten auf individuelle Bestellung", "value": {"stammdaten": {"VERWENDUNGSZEITRAUM": [{"boTyp": "VERWENDUNGSZEITRAUM", "versionStruktur": "1", "verwendungAb": "2025-04-02T22:00:00Z", "zeitraumId": 1, "datenqualitaet": "GUELTIGE_DATEN"}], "AD_HOC_STEUERKANAL": [{"boTyp": "AD_HOC_STEUERKANAL", "versionStruktur": "1", "zieladresse": {"zieladresse1": "X"}, "aussteller": {"aussteller1": "SERIALNUMBER = 3, C = DE, O = SM PKI DE, CN = T Systems EnergyCA.CA", "aussteller2": "X", "aussteller3": "X", "aussteller4": "X", "aussteller5": "X"}, "zertifikatsNutzer": {"zertifikatsNutzer1": "SERIALNUMBER = 3, C = DE, O = SM PKI DE, CN = T Systems EnergyCA.CA", "zertifikatsNutzer2": "X", "zertifikatsNutzer3": "X", "zertifikatsNutzer4": "X", "zertifikatsNutzer5": "X"}, "IPAdresseCLSDevice": {"IPAdresseCLSDevice1": "123.222.345.876", "IPAdresseCLSDevice2": "X", "IPAdresseCLSDevice3": "X", "IPAdresseCLSDevice4": "X", "IPAdresseCLSDevice5": "X"}}]}, "transaktionsdaten": {"datenaustauschreferenz": "M05QXJ3A", "sparte": "STROM", "transaktionsgrund": "ZY9", "vorgangsnummer": "123456", "pruefidentifikator": "55553", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9904446000007", "rollencodetyp": "BDEW", "ipAdresse": "X"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9903790000002", "rollencodetyp": "BDEW", "marktrolle": "LF"}, "dokumentennummer": "BGMLZMVFERR", "kategorie": "E03", "nachrichtendatum": "2025-04-04T12:00:00Z", "nachrichtenreferenznummer": "UNHM0IFAV2X", "verwendungAb": "2025-04-02T22:00:00Z", "nachrichtenReferenzBestellbestaetigung": "ABC123456", "vorgangsReferenzBestellbestaetigung": "123", "vertragsende": "2025-06-30T22:00:00Z"}, "zusatzdaten": {}}}, {"name": "55639", "summary": "55639 — Änderung Daten der NeLo", "value": {"stammdaten": {"VERWENDUNGSZEITRAUM": [{"boTyp": "VERWENDUNGSZEITRAUM", "versionStruktur": "1", "verwendungAb": "2025-04-02T22:00:00Z", "zeitraumId": 1, "datenqualitaet": "GUELTIGE_DATEN"}], "NETZLOKATION": [{"boTyp": "NETZLOKATION", "versionStruktur": "1", "netzlokationsId": "E1688117482", "sparte": "STROM", "datenqualitaet": "GUELTIGE_DATEN", "gueltigkeitszeitraum": {"zeitraumId": 1, "startdatum": "2025-04-02T22:00:00Z"}, "steuerkanal": true, "produktdatenRelevanteRolle": "NB", "keinKonfigurationsprodukt": true, "auftraggebenderMarktpartner": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "marktrolle": "NB", "rollencodenummer": "9900321000005"}, "zaehlwerke": [{"obisKennzahl": "1-1:5.29.0", "verwendungszwecke": [{"marktrolle": "NB", "zweck": ["BLINDARBEITABRECHNUNG_BETRIEBSFUEHRUNG"]}]}]}]}, "transaktionsdaten": {"datenaustauschreferenz": "LZQZZMUB", "sparte": "STROM", "transaktionsgrund": "ZX8", "vorgangsnummer": "123456", "pruefidentifikator": "55639", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9904446000007", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900321000005", "rollencodetyp": "BDEW"}, "dokumentennummer": "BGMM04N7618", "kategorie": "E03", "nachrichtendatum": "2025-04-04T12:00:00Z", "nachrichtenreferenznummer": "UNHLZOTCRQR", "verwendungAb": "2025-04-02T22:00:00Z"}, "zusatzdaten": {}}}, {"name": "55640", "summary": "55640 — Änderung Daten der MaLo", "value": {"stammdaten": {"VERWENDUNGSZEITRAUM": [{"boTyp": "VERWENDUNGSZEITRAUM", "versionStruktur": "1", "zeitraumId": 1, "datenqualitaet": "GUELTIGE_DATEN", "verwendungAb": "2025-04-02T22:00:00Z"}], "MARKTLOKATION": [{"boTyp": "MARKTLOKATION", "versionStruktur": "1", "marktlokationsId": "50074561188", "marktlokationsTyp": [{"typ": "STANDARD_MARKTLOKATION"}], "sparte": "STROM", "gueltigkeitszeitraum": {"zeitraumId": 1, "startdatum": "2025-04-02T22:00:00Z"}, "datenqualitaet": "GUELTIGE_DATEN", "zaehlwerke": [{"obisKennzahl": "1-1:1.9.1", "verwendungszwecke": [{"marktrolle": "NB", "zweck": ["NETZNUTZUNGSABRECHNUNG", "MEHRMINDERMENGENABRECHNUNG"]}], "zaehlzeiten": {"zaehlzeitDefinition": "ABC", "register": "XYZ"}, "wertegranularitaet": "JAEHRLICH"}, {"obisKennzahl": "1-1:1.9.2", "verwendungszwecke": [{"marktrolle": "NB", "zweck": ["NETZNUTZUNGSABRECHNUNG", "MEHRMINDERMENGENABRECHNUNG"]}], "zaehlzeiten": {"zaehlzeitDefinition": "ABC", "register": "XYZ"}, "wertegranularitaet": "JAEHRLICH"}], "konfigurationsprodukt": null, "produktdatenRelevanteRolle": "NB"}], "MESSSTELLENBETRIEBSVERTRAG": [{"boTyp": "VERTRAG", "versionStruktur": "1", "vertragsart": "MESSSTELLENBETRIEBSVERTRAG", "gueltigkeitszeitraum": {"zeitraumId": 1, "startdatum": "2025-04-02T22:00:00Z"}, "datenqualitaet": "GUELTIGE_DATEN", "vertragskonditionen": {"geplanteTurnusablesung": {"ableseZeitraum": "0101"}}, "lokationsId": "50074561188", "lokationsTyp": "MALO"}]}, "transaktionsdaten": {"datenaustauschreferenz": "LZU87CWO", "sparte": "STROM", "transaktionsgrund": "ZX6", "transaktionsgrundergaenzung": "ZW4", "vorgangsnummer": "123456", "pruefidentifikator": "55640", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9904446000007", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900321000005", "rollencodetyp": "BDEW"}, "dokumentennummer": "BGMM0GM77SR", "kategorie": "E03", "nachrichtendatum": "2025-06-05T12:00:00Z", "nachrichtenreferenznummer": "UNHM0B24EP6"}, "zusatzdaten": {}}}, {"name": "55641", "summary": "55641 — Änderung Daten der SR", "value": {"stammdaten": {"VERWENDUNGSZEITRAUM": [{"boTyp": "VERWENDUNGSZEITRAUM", "versionStruktur": "1", "verwendungAb": "2025-04-02T22:00:00Z", "zeitraumId": 1, "datenqualitaet": "GUELTIGE_DATEN"}], "STEUERBARE_RESSOURCE": [{"boTyp": "STEUERBARE_RESSOURCE", "versionStruktur": "1", "gueltigkeitszeitraum": {"zeitraumId": 1}, "datenqualitaet": "GUELTIGE_DATEN", "ressourcenId": "C816417ST77", "sparte": "STROM", "steuerkanal": "AN_AUS", "produktdatenRelevanteRolle": "NB", "konfigurationsprodukt": "9991000000713", "zugeordneteDefinition": {"schaltzeitdefinition": "ABC"}, "auftraggebenderMarktpartner": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "marktrolle": "NB", "rollencodenummer": "9900321000005"}}]}, "transaktionsdaten": {"datenaustauschreferenz": "LZOTU1J9", "sparte": "STROM", "transaktionsgrund": "ZX9", "vorgangsnummer": "123456", "pruefidentifikator": "55641", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9904446000007", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900321000005", "rollencodetyp": "BDEW"}, "dokumentennummer": "BGMM0EX83TG", "kategorie": "E03", "nachrichtendatum": "2025-04-04T12:00:00Z", "nachrichtenreferenznummer": "UNHM0GC43AB"}, "zusatzdaten": {}}}, {"name": "55642", "summary": "55642 — Änderung Daten der Tranche", "value": {"stammdaten": {"VERWENDUNGSZEITRAUM": [{"boTyp": "VERWENDUNGSZEITRAUM", "versionStruktur": "1", "verwendungAb": "2025-04-02T22:00:00Z", "zeitraumId": 1, "datenqualitaet": "GUELTIGE_DATEN"}], "TRANCHE": [{"boTyp": "TRANCHE", "versionStruktur": "1", "gueltigkeitszeitraum": {"zeitraumId": 1}, "datenqualitaet": "GUELTIGE_DATEN", "tranchenId": "50074561189", "sparte": "STROM", "zaehlwerke": [{"obisKennzahl": "1-1:2.9.0", "verwendungszwecke": [{"marktrolle": "NB", "zweck": ["BILANZKREISABRECHNUNG"]}]}]}]}, "transaktionsdaten": {"datenaustauschreferenz": "M0BB1BV1", "sparte": "STROM", "transaktionsgrund": "ZY1", "vorgangsnummer": "123456", "pruefidentifikator": "55642", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9904446000007", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900321000005", "rollencodetyp": "BDEW"}, "dokumentennummer": "BGMM095LV34", "kategorie": "E03", "nachrichtendatum": "2025-04-04T12:00:00Z", "nachrichtenreferenznummer": "UNHLZY0VLA0", "verwendungAb": "2025-04-02T22:00:00Z"}, "zusatzdaten": {}}}, {"name": "55643", "summary": "55643 — Änderung Daten der MeLo", "value": {"stammdaten": {"VERWENDUNGSZEITRAUM": [{"boTyp": "VERWENDUNGSZEITRAUM", "versionStruktur": "1", "verwendungAb": "2025-04-02T22:00:00Z", "zeitraumId": 1, "datenqualitaet": "GUELTIGE_DATEN"}], "MESSLOKATION": [{"boTyp": "MESSLOKATION", "versionStruktur": "1", "gueltigkeitszeitraum": {"zeitraumId": 1, "startdatum": "2025-04-02T22:00:00Z"}, "datenqualitaet": "GUELTIGE_DATEN", "netzebenemessung": "NSP", "messlokationsId": "DE0032106765712000000000000000037", "sparte": "STROM", "messadresse": {"postleitzahl": "12345", "ort": "Ort", "strasse": "Straße", "hausnummer": "1", "landescode": "DE", "zusatzInformation": {"zusatz1": "Mustermann", "zusatz2": "Max"}}, "ablesekartenempfaenger": {"boTyp": "GESCHAEFTSPARTNER", "geschaeftspartnerrolle": ["ABLESEKARTENEMPFAENGER"], "versionStruktur": "1", "gewerbekennzeichnung": false, "name1": "Mustermann", "name2": "Max", "partneradresse": {"postleitzahl": "12345", "ort": "Ort", "strasse": "Straße", "hausnummer": "1", "landescode": "DE"}}}], "MESSSTELLENBETRIEBSVERTRAG": [{"boTyp": "VERTRAG", "versionStruktur": "1", "gueltigkeitszeitraum": {"zeitraumId": 1, "startdatum": "2025-04-02T22:00:00Z"}, "datenqualitaet": "GUELTIGE_DATEN", "netzebenemessung": "NSP", "vertragsart": "MESSSTELLENBETRIEBSVERTRAG", "sparte": "STROM", "vertragspartner2": [{"boTyp": "GESCHAEFTSPARTNER", "versionStruktur": "1", "name1": "Mustermann", "name2": "Max", "gewerbekennzeichnung": false, "geschaeftspartnerrolle": ["KUNDE"]}], "korrespondenzpartner": {"boTyp": "GESCHAEFTSPARTNER", "versionStruktur": "1", "name1": "Mustermann", "name2": "Max", "gewerbekennzeichnung": false, "partneradresse": {"postleitzahl": "12345", "ort": "Ort", "strasse": "Straße", "hausnummer": "1", "landescode": "DE"}}}], "ZAEHLER": [{"boTyp": "ZAEHLER", "versionStruktur": "1", "gueltigkeitszeitraum": {"zeitraumId": 1, "startdatum": "2025-04-02T22:00:00Z"}, "datenqualitaet": "GUELTIGE_DATEN", "zaehlerauspraegung": "EINRICHTUNGSZAEHLER", "zaehlertyp": "DREHSTROMZAEHLER", "tarifart": "EINTARIF", "zaehlwerke": [{"obisKennzahl": "1-1:1.8.0", "schwachlastfaehig": "NICHT_SCHWACHLASTFAEHIG", "vorkommastelle": 7, "nachkommastelle": 3, "wertegranularitaet": "JAEHRLICH"}], "zaehlernummer": "ABC123456", "sparte": "STROM", "fernschaltung": "NICHT_VORHANDEN", "messwerterfassung": "MANUELL_AUSGELESENE", "befestigungsart": "STECKTECHNIK", "geraete": [{"geraetenummer": "ABC123456"}]}]}, "transaktionsdaten": {"datenaustauschreferenz": "M0BGVSSM", "sparte": "STROM", "transaktionsgrund": "ZX7", "vorgangsnummer": "123456", "pruefidentifikator": "55643", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9904446000007", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900321000005", "rollencodetyp": "BDEW"}, "dokumentennummer": "BGMM0G8GT0G", "kategorie": "E03", "nachrichtendatum": "2025-06-05T12:00:00Z", "nachrichtenreferenznummer": "UNHLZRA72YM"}, "zusatzdaten": {}}}]}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Legt im Backend einen neuen Vorgang mit den Daten der eingegangenen Nachricht an.

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- `55553` → Vorgang fortgeschrieben — `AKTUALISIEREN_PROZESSDATEN_BASIS`

Schreibt den bestehenden Vorgang im Backend mit den Daten der eingegangenen Nachricht fort.

</li>

<li data-teil="baum">

**Entscheidungsbaum**
- `55557`, `55553`, `55639`, `55640`, `55641`, `55642`, `55643` → [E_0415](/referenz/202604/ebd/E_0415) — Änderung vom MSB prüfen (Basiert auf EBD: E_0408_Änderung vom NB prüfen)

</li>

<li data-teil="folgeprozess">

**Folgeprozess auslösen**
- [55555](/schnittstellen/202604/pruefi/UTILMD/PI_55555) — Anfrage Daten der individuellen Bestellung
- [55559](/schnittstellen/202604/pruefi/UTILMD/PI_55559) — Rückmeldung/Anfrage MSB-Abr.-Daten der MaLo
- [55644](/schnittstellen/202604/pruefi/UTILMD/PI_55644) — Rückmeldung/Anfrage Daten der NeLo
- [55645](/schnittstellen/202604/pruefi/UTILMD/PI_55645) — Rückmeldung/Anfrage Daten der MaLo
- [55646](/schnittstellen/202604/pruefi/UTILMD/PI_55646) — Rückmeldung/Anfrage Daten der SR
- [55647](/schnittstellen/202604/pruefi/UTILMD/PI_55647) — Rückmeldung/Anfrage Daten der Tranche
- [55648](/schnittstellen/202604/pruefi/UTILMD/PI_55648) — Rückmeldung/Anfrage Daten der MeLo

Nach der Verarbeitung startet die MACO APP den Folgeprozess selbst; welcher davon läuft, hängt vom Ergebnis der Verarbeitung ab.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="2" anker="schritt-2" richtung="ausgehend" kopf={{"links": {"label": "NB", "eigen": true}, "rechts": {"label": "MSB"}}}>

### Rückmeldung auf Änderung

<Schrittskizze sicht={{"label": "NB"}} zeilen={[{"art": "folge_ausloeser", "werte": ["55553", "55557", "55639", "55640", "55641", "55642", "55643"]}, {"art": "ausloeser", "werte": ["START_BESTELLUNG_SDAE"]}, {"art": "lesen_verarbeitung", "schnittstellen": [{"label": "Marktlokation lesen"}, {"label": "Netzlokation lesen"}, {"label": "Steuerbare Ressource lesen"}, {"label": "Tranche lesen"}, {"label": "Messlokation lesen"}]}, {"art": "senden", "label": "MSB", "weg": "AS4", "nachrichten": [{"nr": "55559", "titel": "Rückmeldung/Anfrage MSB-Abr.-Daten der MaLo"}, {"nr": "55555", "titel": "Anfrage Daten der individuellen Bestellung"}, {"nr": "55644", "titel": "Rückmeldung/Anfrage Daten der NeLo"}, {"nr": "55645", "titel": "Rückmeldung/Anfrage Daten der MaLo"}, {"nr": "55646", "titel": "Rückmeldung/Anfrage Daten der SR"}, {"nr": "55647", "titel": "Rückmeldung/Anfrage Daten der Tranche"}, {"nr": "55648", "titel": "Rückmeldung/Anfrage Daten der MeLo"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55559](/schnittstellen/202604/pruefi/UTILMD/PI_55559) — Rückmeldung/Anfrage MSB-Abr.-Daten der MaLo · AS4
- [55555](/schnittstellen/202604/pruefi/UTILMD/PI_55555) — Anfrage Daten der individuellen Bestellung · AS4
- [55644](/schnittstellen/202604/pruefi/UTILMD/PI_55644) — Rückmeldung/Anfrage Daten der NeLo · AS4
- [55645](/schnittstellen/202604/pruefi/UTILMD/PI_55645) — Rückmeldung/Anfrage Daten der MaLo · AS4
- [55646](/schnittstellen/202604/pruefi/UTILMD/PI_55646) — Rückmeldung/Anfrage Daten der SR · AS4
- [55647](/schnittstellen/202604/pruefi/UTILMD/PI_55647) — Rückmeldung/Anfrage Daten der Tranche · AS4
- [55648](/schnittstellen/202604/pruefi/UTILMD/PI_55648) — Rückmeldung/Anfrage Daten der MeLo · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="folge_ausloeser">

**Ausgelöst durch Eingang**
- [55553](/schnittstellen/202604/pruefi/UTILMD/PI_55553) — Daten auf individuelle Bestellung
- [55557](/schnittstellen/202604/pruefi/UTILMD/PI_55557) — Änderung MSB-Abr.-Daten der MaLo
- [55639](/schnittstellen/202604/pruefi/UTILMD/PI_55639) — Änderung Daten der NeLo
- [55640](/schnittstellen/202604/pruefi/UTILMD/PI_55640) — Änderung Daten der MaLo
- [55641](/schnittstellen/202604/pruefi/UTILMD/PI_55641) — Änderung Daten der SR
- [55642](/schnittstellen/202604/pruefi/UTILMD/PI_55642) — Änderung Daten der Tranche
- [55643](/schnittstellen/202604/pruefi/UTILMD/PI_55643) — Änderung Daten der MeLo

Die MACO APP sendet diese Nachricht selbst, als Folgeprozess nach einem dieser Eingänge. Daneben kann das Backend diesen Schritt mit einem Ereignis anstoßen — der nächste Punkt.

</li>

<li data-teil="ausloeser">

**Prozessauslöser** [`START_BESTELLUNG_SDAE`](/schnittstellen/202604/trigger/events/NB-START_BESTELLUNG_SDAE) · [Im Playground ausprobieren](/api/202604/ausloeser-nb/start-bestellung-sdae)

Das Backend stößt diesen Schritt mit diesem Ereignis an.

</li>

<li data-teil="lesen" data-stufe="verarbeitung">

**Daten für die Verarbeitung laden**
- [Marktlokation lesen](/api/202604/backend-lesen/getmarketlocationbasic#marktlokation-lesen) `GET /getMarketLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getMarketLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": false, "defaultValue": "MALO", "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": false, "defaultValue": "2024-06-28T12:18:00Z", "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_MARKTLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Netzlokation lesen](/api/202604/backend-lesen/getgridlocationbasic#netzlokation-lesen) `GET /getGridLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getGridLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_NETZLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Steuerbare Ressource lesen](/api/202604/backend-lesen/getcontrollableresourcebasic#steuerbare-ressource-lesen) `GET /getControllableResourceBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getControllableResourceBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Tranche lesen](/api/202604/backend-lesen/gettranchebasic#tranche-lesen) `GET /getTrancheBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getTrancheBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Messlokation lesen](/api/202604/backend-lesen/getmeterlocationbasic#messlokation-lesen) `GET /getMeterLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getMeterLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_MESSLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

</li>

<li data-teil="nachricht">

Nachricht an **MSB** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `55559`, `55555`, `55644`, `55645`, `55646`, `55647`, `55648` → [E_0415](/referenz/202604/ebd/E_0415) · NB · Änderung vom MSB prüfen (Basiert auf EBD: E_0408_Änderung vom NB prüfen)

</div>

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202604/backend-schreiben-nb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"MARKTLOKATION\": [\n      {\n        \"boTyp\": \"MARKTLOKATION\",\n        \"datenqualitaet\": \"ERWARTETE_DATEN\",\n        \"gueltigkeitszeitraum\": {\n          \"enddatum\": \"2025-07-23T22:00:00Z\",\n          \"startdatum\": \"2025-06-23T22:00:00Z\",\n          \"zeitraumId\": 1\n        },\n        \"marktlokationsId\": \"20072281644\",\n        \"messstellenbetriebsabrechnungsdaten\": [\n          {\n            \"anzahl\": 1,\n            \"artikelId\": \"1-06-1-001\",\n            \"artikelIdTyp\": \"ARTIKELID\",\n            \"messstellenbetriebsabrechnung\": true,\n            \"zuschlag\": 0\n          }\n        ],\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      },\n      {\n        \"boTyp\": \"MARKTLOKATION\",\n        \"datenqualitaet\": \"ERWARTETE_DATEN\",\n        \"gueltigkeitszeitraum\": {\n          \"startdatum\": \"2025-07-23T22:00:00Z\",\n          \"zeitraumId\": 2\n        },\n        \"marktlokationsId\": \"20072281644\",\n        \"messstellenbetriebsabrechnungsdaten\": [\n          {\n            \"anzahl\": 1,\n            \"artikelId\": \"1-06-1-001\",\n            \"artikelIdTyp\": \"ARTIKELID\",\n            \"messstellenbetriebsabrechnung\": true,\n            \"zuschlag\": 0\n          }\n        ],\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"VERWENDUNGSZEITRAUM\": [\n      {\n        \"boTyp\": \"VERWENDUNGSZEITRAUM\",\n        \"datenqualitaet\": \"ERWARTETE_DATEN\",\n        \"versionStruktur\": \"1\",\n        \"verwendungAb\": \"2025-06-23T22:00:00Z\",\n        \"verwendungBis\": \"2025-07-23T22:00:00Z\",\n        \"zeitraumId\": 1\n      },\n      {\n        \"boTyp\": \"VERWENDUNGSZEITRAUM\",\n        \"datenqualitaet\": \"ERWARTETE_DATEN\",\n        \"versionStruktur\": \"1\",\n        \"verwendungAb\": \"2025-07-23T22:00:00Z\",\n        \"zeitraumId\": 2\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"ansprechpartner\": {\n        \"boTyp\": \"ANSPRECHPARTNER\",\n        \"nachname\": \"P GETTY\",\n        \"rufnummern\": [\n          {\n            \"nummerntyp\": \"RUF_DURCHWAHL\",\n            \"rufnummer\": \"+3222271020\"\n          }\n        ],\n        \"versionStruktur\": \"1\"\n      },\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9900327000009\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"anfragereferenznummer\": \"64739202\",\n    \"antwortStatusZeitraum\": [\n      {\n        \"code\": \"A02\",\n        \"liste\": \"E_0415\",\n        \"zeitraumId\": 1\n      },\n      {\n        \"code\": \"A02\",\n        \"liste\": \"E_0415\",\n        \"zeitraumId\": 2\n      }\n    ],\n    \"datenaustauschreferenz\": \"DAHXSSRXIQVLPY\",\n    \"dokumentennummer\": \"DA102411080843469903323000007705139\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9910812000000\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"E03\",\n    \"nachrichtendatum\": \"2025-06-24T12:31:00Z\",\n    \"nachrichtenreferenznummer\": \"DALZTXEQIIHGMY\",\n    \"pruefidentifikator\": \"55559\",\n    \"sparte\": \"STROM\",\n    \"transaktionsgrund\": \"ZU1\",\n    \"vorgangsnummer\": \"24062416225400000000000102159662011\"\n  },\n  \"zusatzdaten\": {}\n}"} examples={[{"mediaType": "application/json", "examples": [{"name": "55559", "summary": "55559 — Rückmeldung/Anfrage MSB-Abr.-Daten der MaLo", "value": {"stammdaten": {"VERWENDUNGSZEITRAUM": [{"boTyp": "VERWENDUNGSZEITRAUM", "versionStruktur": "1", "zeitraumId": 1, "datenqualitaet": "ERWARTETE_DATEN", "verwendungAb": "2025-06-23T22:00:00Z", "verwendungBis": "2025-07-23T22:00:00Z"}, {"boTyp": "VERWENDUNGSZEITRAUM", "versionStruktur": "1", "zeitraumId": 2, "datenqualitaet": "ERWARTETE_DATEN", "verwendungAb": "2025-07-23T22:00:00Z"}], "MARKTLOKATION": [{"boTyp": "MARKTLOKATION", "versionStruktur": "1", "marktlokationsId": "20072281644", "sparte": "STROM", "gueltigkeitszeitraum": {"zeitraumId": 1, "startdatum": "2025-06-23T22:00:00Z", "enddatum": "2025-07-23T22:00:00Z"}, "datenqualitaet": "ERWARTETE_DATEN", "messstellenbetriebsabrechnungsdaten": [{"messstellenbetriebsabrechnung": true, "artikelId": "1-06-1-001", "artikelIdTyp": "ARTIKELID", "anzahl": 1, "zuschlag": 0}]}, {"boTyp": "MARKTLOKATION", "versionStruktur": "1", "marktlokationsId": "20072281644", "sparte": "STROM", "gueltigkeitszeitraum": {"zeitraumId": 2, "startdatum": "2025-07-23T22:00:00Z"}, "datenqualitaet": "ERWARTETE_DATEN", "messstellenbetriebsabrechnungsdaten": [{"messstellenbetriebsabrechnung": true, "artikelId": "1-06-1-001", "artikelIdTyp": "ARTIKELID", "anzahl": 1, "zuschlag": 0}]}]}, "transaktionsdaten": {"datenaustauschreferenz": "DAHXSSRXIQVLPY", "sparte": "STROM", "transaktionsgrund": "ZU1", "vorgangsnummer": "24062416225400000000000102159662011", "anfragereferenznummer": "64739202", "pruefidentifikator": "55559", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900327000009", "rollencodetyp": "BDEW", "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "nachname": "P GETTY", "rufnummern": [{"nummerntyp": "RUF_DURCHWAHL", "rufnummer": "+3222271020"}]}}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9910812000000", "rollencodetyp": "BDEW"}, "dokumentennummer": "DA102411080843469903323000007705139", "kategorie": "E03", "nachrichtendatum": "2025-06-24T12:31:00Z", "nachrichtenreferenznummer": "DALZTXEQIIHGMY", "antwortStatusZeitraum": [{"code": "A02", "liste": "E_0415", "zeitraumId": 1}, {"code": "A02", "liste": "E_0415", "zeitraumId": 2}]}, "zusatzdaten": {}}}, {"name": "55555", "summary": "55555 — Anfrage Daten der individuellen Bestellung", "value": {"stammdaten": {"AD_HOC_STEUERKANAL": [{"boTyp": "AD_HOC_STEUERKANAL", "versionStruktur": "1", "zieladresse": {"zieladresse1": "X"}, "aussteller": {"aussteller1": "SERIALNUMBER = 3, C = DE, O = SM-PKI-DE, CN = T-Systems-EnergyCA.CA", "aussteller2": "X", "aussteller3": "X", "aussteller4": "X", "aussteller5": "X"}, "zertifikatsNutzer": {"zertifikatsNutzer1": "X", "zertifikatsNutzer2": "X", "zertifikatsNutzer3": "X", "zertifikatsNutzer4": "X", "zertifikatsNutzer5": "X"}, "IPAdresseCLSDevice": {"IPAdresseCLSDevice1": "123.222.345.876", "IPAdresseCLSDevice2": "X", "IPAdresseCLSDevice3": "X", "IPAdresseCLSDevice4": "X", "IPAdresseCLSDevice5": "X"}}], "VERWENDUNGSZEITRAUM": [{"boTyp": "VERWENDUNGSZEITRAUM", "versionStruktur": "1", "zeitraumId": 1, "datenqualitaet": "ERWARTETE_DATEN", "verwendungAb": "2025-06-23T22:00:00Z", "verwendungBis": "2025-07-23T22:00:00Z"}, {"boTyp": "VERWENDUNGSZEITRAUM", "versionStruktur": "1", "zeitraumId": 2, "datenqualitaet": "ERWARTETE_DATEN", "verwendungAb": "2025-07-23T22:00:00Z"}], "MARKTLOKATION": [{"boTyp": "MARKTLOKATION", "versionStruktur": "1", "sparte": "STROM", "gueltigkeitszeitraum": {"zeitraumId": 1, "startdatum": "2025-06-23T22:00:00Z", "enddatum": "2025-07-23T22:00:00Z"}, "datenqualitaet": "ERWARTETE_DATEN", "zaehlwerke": [{"obisKennzahl": "1-1:1.9.1", "zaehlzeiten": {"zaehlzeitDefinition": "ABC", "register": "XYZ"}, "wertegranularitaet": "JAEHRLICH"}]}, {"boTyp": "MARKTLOKATION", "versionStruktur": "1", "sparte": "STROM", "gueltigkeitszeitraum": {"zeitraumId": 2, "startdatum": "2025-07-23T22:00:00Z"}, "datenqualitaet": "ERWARTETE_DATEN", "zaehlwerke": [{"obisKennzahl": "1-1:1.9.1", "zaehlzeiten": {"zaehlzeitDefinition": "ABC", "register": "XYZ"}, "wertegranularitaet": "JAEHRLICH"}]}], "ZAEHLER": [{"boTyp": "ZAEHLER", "versionStruktur": "1", "zaehlernummer": "12345667891", "sparte": "STROM", "gueltigkeitszeitraum": {"zeitraumId": 1, "startdatum": "2025-06-23T22:00:00Z", "enddatum": "2025-07-23T22:00:00Z"}, "datenqualitaet": "ERWARTETE_DATEN", "zaehlwerke": [{"bezeichnung": "HT", "obisKennzahl": "1-1:1.8.1", "vorkommastelle": 8, "nachkommastelle": 3, "zaehlzeiten": {"zaehlzeitDefinition": "ABC", "register": "XYZ"}, "konfiguration": "34590456ujdfsdghdlktztwqq-053trg", "wertegranularitaet": "JAEHRLICH"}], "gateway": "1234567890", "geraete": [{"geraetenummer": "1234567890", "geraeteeigenschaften": {"geraetetyp": "SMARTMETERGATEWAY"}}]}, {"boTyp": "ZAEHLER", "versionStruktur": "1", "zaehlernummer": "12345667891", "sparte": "STROM", "gueltigkeitszeitraum": {"zeitraumId": 2, "startdatum": "2025-07-23T22:00:00Z"}, "datenqualitaet": "ERWARTETE_DATEN", "zaehlwerke": [{"bezeichnung": "HT", "obisKennzahl": "1-1:1.8.1", "vorkommastelle": 8, "nachkommastelle": 3, "zaehlzeiten": {"zaehlzeitDefinition": "ABC", "register": "XYZ"}, "konfiguration": "34590456ujdfsdghdlktztwqq-053trg", "wertegranularitaet": "JAEHRLICH"}], "gateway": "1234567890", "geraete": [{"geraetenummer": "1234567890", "geraeteeigenschaften": {"geraetetyp": "SMARTMETERGATEWAY"}}]}]}, "transaktionsdaten": {"datenaustauschreferenz": "DAXOXILSWLJTQB", "sparte": "STROM", "transaktionsgrund": "ZY9", "anfragereferenznummer": "64739202", "vorgangsnummer": "24062416225400000000000102159662011", "pruefidentifikator": "55555", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9903729000007", "rollencodetyp": "BDEW", "ipAdresse": "X", "ipRange": {"untereGrenze": "X", "obereGrenze": "X"}, "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "nachname": "P GETTY", "rufnummern": [{"nummerntyp": "RUF_DURCHWAHL", "rufnummer": "+3222271020"}]}}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9904990000008", "rollencodetyp": "BDEW"}, "dokumentennummer": "DA882411080716289903323000007541914", "kategorie": "E03", "nachrichtendatum": "2025-06-24T12:31:00Z", "nachrichtenreferenznummer": "DAESNJTWNDGGFS", "antwortStatusZeitraum": [{"code": "A02", "liste": "E_0412", "zeitraumId": 1}, {"code": "A02", "liste": "E_0412", "zeitraumId": 2}], "nachrichtenReferenzBestellbestaetigung": "98786423423435", "vorgangsReferenzBestellbestaetigung": "12"}, "zusatzdaten": {}}}, {"name": "55644", "summary": "55644 — Rückmeldung/Anfrage Daten der NeLo", "value": {"stammdaten": {"VERWENDUNGSZEITRAUM": [{"boTyp": "VERWENDUNGSZEITRAUM", "versionStruktur": "1", "verwendungAb": "2025-04-02T22:00:00Z", "zeitraumId": 1, "datenqualitaet": "ERWARTETE_DATEN"}], "NETZLOKATION": [{"boTyp": "NETZLOKATION", "versionStruktur": "1", "netzlokationsId": "E1688117482", "sparte": "STROM"}]}, "transaktionsdaten": {"datenaustauschreferenz": "M0FDKMKD", "sparte": "STROM", "transaktionsgrund": "ZX8", "vorgangsnummer": "123456", "pruefidentifikator": "55644", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900321000005", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9904446000007", "rollencodetyp": "BDEW"}, "dokumentennummer": "BGMM074XRBN", "kategorie": "E03", "nachrichtendatum": "2025-04-04T12:00:00Z", "nachrichtenreferenznummer": "UNHLZYMFJZF", "anfragereferenznummer": "ABC123456", "antwortStatusZeitraum": [{"code": "A01", "liste": "E_0415", "zeitraumId": 1}]}, "zusatzdaten": {}}}, {"name": "55645", "summary": "55645 — Rückmeldung/Anfrage Daten der MaLo", "value": {"stammdaten": {"VERWENDUNGSZEITRAUM": [{"boTyp": "VERWENDUNGSZEITRAUM", "versionStruktur": "1", "verwendungAb": "2025-04-02T22:00:00Z", "zeitraumId": 1, "datenqualitaet": "ERWARTETE_DATEN"}], "MARKTLOKATION": [{"boTyp": "MARKTLOKATION", "versionStruktur": "1", "marktlokationsId": "50074561188", "marktlokationsTyp": [{"typ": "STANDARD_MARKTLOKATION"}], "sparte": "STROM"}]}, "transaktionsdaten": {"datenaustauschreferenz": "M0KOJB5I", "sparte": "STROM", "transaktionsgrund": "ZX6", "transaktionsgrundergaenzung": "ZW4", "vorgangsnummer": "123456", "pruefidentifikator": "55645", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900321000005", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9904446000007", "rollencodetyp": "BDEW"}, "dokumentennummer": "BGMM0REVZHH", "kategorie": "E03", "nachrichtendatum": "2025-06-05T12:00:00Z", "nachrichtenreferenznummer": "UNHM076RBF8", "anfragereferenznummer": "ABC123456", "antwortStatusZeitraum": [{"code": "A01", "liste": "E_0415", "zeitraumId": 1}]}, "zusatzdaten": {}}}, {"name": "55646", "summary": "55646 — Rückmeldung/Anfrage Daten der SR", "value": {"stammdaten": {"VERWENDUNGSZEITRAUM": [{"boTyp": "VERWENDUNGSZEITRAUM", "versionStruktur": "1", "verwendungAb": "2025-04-02T22:00:00Z", "zeitraumId": 1, "datenqualitaet": "ERWARTETE_DATEN"}], "STEUERBARE_RESSOURCE": [{"boTyp": "STEUERBARE_RESSOURCE", "versionStruktur": "1", "ressourcenId": "C816417ST77", "sparte": "STROM"}]}, "transaktionsdaten": {"datenaustauschreferenz": "M0JQ15FK", "sparte": "STROM", "transaktionsgrund": "ZX9", "vorgangsnummer": "123456", "pruefidentifikator": "55646", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900321000005", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9904446000007", "rollencodetyp": "BDEW"}, "dokumentennummer": "BGMM027DHWU", "kategorie": "E03", "nachrichtendatum": "2025-04-04T12:00:00Z", "nachrichtenreferenznummer": "UNHM03BDQVB", "anfragereferenznummer": "ABC123456", "antwortStatusZeitraum": [{"code": "A01", "liste": "E_0415", "zeitraumId": 1}]}, "zusatzdaten": {}}}, {"name": "55647", "summary": "55647 — Rückmeldung/Anfrage Daten der Tranche", "value": {"stammdaten": {"VERWENDUNGSZEITRAUM": [{"boTyp": "VERWENDUNGSZEITRAUM", "versionStruktur": "1", "verwendungAb": "2025-04-02T22:00:00Z", "zeitraumId": 1, "datenqualitaet": "ERWARTETE_DATEN"}], "TRANCHE": [{"boTyp": "TRANCHE", "versionStruktur": "1", "tranchenId": "50074561189", "sparte": "STROM"}]}, "transaktionsdaten": {"datenaustauschreferenz": "M0NDZVLJ", "sparte": "STROM", "transaktionsgrund": "ZY1", "vorgangsnummer": "123456", "pruefidentifikator": "55647", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900321000005", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9904446000007", "rollencodetyp": "BDEW"}, "dokumentennummer": "BGMM00LJWUE", "kategorie": "E03", "nachrichtendatum": "2025-04-04T12:00:00Z", "nachrichtenreferenznummer": "UNHM0P3VX74", "anfragereferenznummer": "ABC123456", "antwortStatusZeitraum": [{"code": "A01", "liste": "E_0415", "zeitraumId": 1}]}, "zusatzdaten": {}}}, {"name": "55648", "summary": "55648 — Rückmeldung/Anfrage Daten der MeLo", "value": {"stammdaten": {"VERWENDUNGSZEITRAUM": [{"boTyp": "VERWENDUNGSZEITRAUM", "versionStruktur": "1", "verwendungAb": "2025-04-02T22:00:00Z", "zeitraumId": 1, "datenqualitaet": "ERWARTETE_DATEN"}], "MESSLOKATION": [{"boTyp": "MESSLOKATION", "versionStruktur": "1", "messlokationsId": "DE0032106765712000000000000000037", "sparte": "STROM"}]}, "transaktionsdaten": {"datenaustauschreferenz": "M0PUPYQ6", "sparte": "STROM", "transaktionsgrund": "ZX7", "vorgangsnummer": "123456", "pruefidentifikator": "55648", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900321000005", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9904446000007", "rollencodetyp": "BDEW"}, "dokumentennummer": "BGMLZWK81WD", "kategorie": "E03", "nachrichtendatum": "2025-06-05T12:00:00Z", "nachrichtenreferenznummer": "UNHM0IYUYB2", "anfragereferenznummer": "ABC123456", "antwortStatusZeitraum": [{"code": "A01", "liste": "E_0415", "zeitraumId": 1}]}, "zusatzdaten": {}}}]}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend fort, nachdem die Nachricht erstellt ist.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="3" anker="schritt-3" richtung="eingehend" kopf={{"links": {"label": "NB", "eigen": true}, "rechts": {"label": "MSB"}}}>

### Bearbeitungsstand zur Rückmeldung

<Schrittskizze sicht={{"label": "NB"}} zeilen={[{"art": "empfangen", "label": "MSB", "weg": "AS4", "nachrichten": [{"nr": "21047", "titel": "Bearbeitungsstandsmeldung"}]}, {"art": "aperak", "werte": ["Z33"]}, {"art": "fortschreiben"}, {"art": "folgeprozess", "werte": ["21047"]}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [21047](/schnittstellen/202604/pruefi/IFTSTA/PI_21047) — Bearbeitungsstandsmeldung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **MSB** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `21047` → [E_0632](/referenz/202604/ebd/E_0632) · MSB · Rückmeldung auf Änderung prüfen (Basiert auf EBD: E_0626_Rückmeldung auf Änderung prüfen)

</div>

</li>

<li data-teil="aperak">

**Aperak-Prüfungen**
- `21047` → `Z33`

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202604/backend-schreiben-nb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"STATUSMITTEILUNG\": [\n      {\n        \"auftragsstatus\": \"KEINE_AENDERUNG_DER_DATEN\",\n        \"boTyp\": \"STATUSMITTEILUNG\",\n        \"positionsdaten\": [\n          {\n            \"positionsnummer\": 1\n          }\n        ],\n        \"statusObjekt\": \"VERAENDERUNGSSTATUS_DER_DATEN\",\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"marktrolle\": \"LF\",\n      \"rollencodenummer\": \"9900321000005\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"antwortstatus\": \"A01\",\n    \"antwortstatusCodeliste\": \"E_0588\",\n    \"datenaustauschreferenz\": \"M0M56B09\",\n    \"dokumentennummer\": \"BGMM0M7F86Z\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"marktrolle\": \"NB\",\n      \"rollencodenummer\": \"9903790000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"Z33\",\n    \"nachrichtendatum\": \"2025-04-04T12:00:00Z\",\n    \"nachrichtenreferenznummer\": \"UNHM09Y0DVP\",\n    \"pruefidentifikator\": \"21047\",\n    \"sparte\": \"STROM\",\n    \"vorgangsreferenznummer\": \"ABC12345\"\n  },\n  \"zusatzdaten\": {}\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend mit den Daten der eingegangenen Nachricht fort.

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

<Schritt nr="4" anker="schritt-4" richtung="fremd" kopf={{"links": {"label": "MSB", "eigen": false}, "rechts": {"label": "LF"}}}>

### Änderung vom MSB an LF

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55649](/schnittstellen/202604/pruefi/UTILMD/PI_55649) — Änderung Daten der NeLo · AS4
- [55553](/schnittstellen/202604/pruefi/UTILMD/PI_55553) — Daten auf individuelle Bestellung · AS4
- [55650](/schnittstellen/202604/pruefi/UTILMD/PI_55650) — Änderung Daten der MaLo · AS4
- [55651](/schnittstellen/202604/pruefi/UTILMD/PI_55651) — Änderung Daten der SR · AS4
- [55652](/schnittstellen/202604/pruefi/UTILMD/PI_55652) — Änderung Daten der Tranche · AS4
- [55653](/schnittstellen/202604/pruefi/UTILMD/PI_55653) — Änderung Daten der MeLo · AS4

</div>

</Schritt>

<Schritt nr="5" anker="schritt-5" richtung="fremd" kopf={{"links": {"label": "LF", "eigen": false}, "rechts": {"label": "MSB"}}}>

### Rückmeldung auf Änderung

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55654](/schnittstellen/202604/pruefi/UTILMD/PI_55654) — Rückmeldung/Anfrage Daten der NeLo · AS4
- [55555](/schnittstellen/202604/pruefi/UTILMD/PI_55555) — Anfrage Daten der individuellen Bestellung · AS4
- [55655](/schnittstellen/202604/pruefi/UTILMD/PI_55655) — Rückmeldung/Anfrage Daten der MaLo · AS4
- [55656](/schnittstellen/202604/pruefi/UTILMD/PI_55656) — Rückmeldung/Anfrage Daten der SR · AS4
- [55657](/schnittstellen/202604/pruefi/UTILMD/PI_55657) — Rückmeldung/Anfrage Daten der Tranche · AS4
- [55658](/schnittstellen/202604/pruefi/UTILMD/PI_55658) — Rückmeldung/Anfrage Daten der MeLo · AS4

</div>

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `55654`, `55555`, `55655`, `55656`, `55657`, `55658` → [E_0412](/referenz/202604/ebd/E_0412) · LF · Änderung vom MSB prüfen (Basiert auf EBD: E_0408_Änderung vom NB prüfen)

</div>

</Schritt>

<Schritt nr="6" anker="schritt-6" richtung="fremd" kopf={{"links": {"label": "MSB", "eigen": false}, "rechts": {"label": "LF"}}}>

### Bearbeitungsstand zur Rückmeldung

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [21047](/schnittstellen/202604/pruefi/IFTSTA/PI_21047) — Bearbeitungsstandsmeldung · AS4

</div>

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `21047` → [E_0633](/referenz/202604/ebd/E_0633) · MSB · Rückmeldung auf Änderung prüfen (Basiert auf EBD: E_0626_Rückmeldung auf Änderung prüfen)

</div>

</Schritt>

<Schritt nr="7" anker="schritt-7" richtung="fremd" kopf={{"links": {"label": "MSB", "eigen": false}, "rechts": {"label": "weiterer MSB"}}}>

### Änderung vom MSB an weiteren MSB

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55659](/schnittstellen/202604/pruefi/UTILMD/PI_55659) — Änderung Daten der NeLo · AS4
- [55553](/schnittstellen/202604/pruefi/UTILMD/PI_55553) — Daten auf individuelle Bestellung · AS4
- [55660](/schnittstellen/202604/pruefi/UTILMD/PI_55660) — Änderung Daten der MaLo · AS4
- [55661](/schnittstellen/202604/pruefi/UTILMD/PI_55661) — Änderung Daten der SR · AS4
- [55662](/schnittstellen/202604/pruefi/UTILMD/PI_55662) — Änderung Daten der Tranche · AS4
- [55663](/schnittstellen/202604/pruefi/UTILMD/PI_55663) — Änderung Daten der MeLo · AS4

</div>

</Schritt>

<Schritt nr="8" anker="schritt-8" richtung="fremd" kopf={{"links": {"label": "weiterer MSB", "eigen": false}, "rechts": {"label": "MSB"}}}>

### Rückmeldung auf Änderung

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55664](/schnittstellen/202604/pruefi/UTILMD/PI_55664) — Rückmeldung/Anfrage Daten der NeLo · AS4
- [55555](/schnittstellen/202604/pruefi/UTILMD/PI_55555) — Anfrage Daten der individuellen Bestellung · AS4
- [55665](/schnittstellen/202604/pruefi/UTILMD/PI_55665) — Rückmeldung/Anfrage Daten der MaLo · AS4
- [55666](/schnittstellen/202604/pruefi/UTILMD/PI_55666) — Rückmeldung/Anfrage Daten der SR · AS4
- [55667](/schnittstellen/202604/pruefi/UTILMD/PI_55667) — Rückmeldung/Anfrage Daten der Tranche · AS4
- [55669](/schnittstellen/202604/pruefi/UTILMD/PI_55669) — Rückmeldung/Anfrage Daten der MeLo · AS4

</div>

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `55664`, `55555`, `55665`, `55666`, `55667`, `55669` → [E_0583](/referenz/202604/ebd/E_0583) · MSB · Änderung vom MSB prüfen (Basiert auf EBD: E_0408_Änderung vom NB prüfen)

</div>

</Schritt>

<Schritt nr="9" anker="schritt-9" richtung="fremd" kopf={{"links": {"label": "MSB", "eigen": false}, "rechts": {"label": "weiterer MSB"}}}>

### Bearbeitungsstand zur Rückmeldung

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [21047](/schnittstellen/202604/pruefi/IFTSTA/PI_21047) — Bearbeitungsstandsmeldung · AS4

</div>

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `21047` → [E_0634](/referenz/202604/ebd/E_0634) · MSB · Rückmeldung auf Änderung prüfen (Basiert auf EBD: E_0626_Rückmeldung auf Änderung prüfen)

</div>

</Schritt>

<Schritt nr="11" anker="schritt-11" richtung="fremd" kopf={{"links": {"label": "MSB", "eigen": false}, "rechts": {"label": "ÜNB"}}}>

### Änderung vom MSB an ÜNB

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55684](/schnittstellen/202604/pruefi/UTILMD/PI_55684) — Änderung Daten der MaLo · AS4
- [55686](/schnittstellen/202604/pruefi/UTILMD/PI_55686) — Änderung Daten der Tranche · AS4

</div>

</Schritt>

<Schritt nr="12" anker="schritt-12" richtung="fremd" kopf={{"links": {"label": "ÜNB", "eigen": false}, "rechts": {"label": "MSB"}}}>

### Rückmeldung auf Änderung

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55685](/schnittstellen/202604/pruefi/UTILMD/PI_55685) — Rückmeldung/Anfrage Daten der MaLo · AS4
- [55687](/schnittstellen/202604/pruefi/UTILMD/PI_55687) — Rückmeldung/Anfrage Daten der Tranche · AS4

</div>

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `55685`, `55687` → [E_0639](/referenz/202604/ebd/E_0639) · ÜNB · Änderung vom MSB prüfen (Basiert auf EBD: E_0408_Änderung vom NB prüfen)

</div>

</Schritt>

<Schritt nr="13" anker="schritt-13" richtung="fremd" kopf={{"links": {"label": "MSB", "eigen": false}, "rechts": {"label": "ÜNB"}}}>

### Bearbeitungsstand zur Rückmeldung

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [21047](/schnittstellen/202604/pruefi/IFTSTA/PI_21047) — Bearbeitungsstandsmeldung · AS4

</div>

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `21047` → [E_0635](/referenz/202604/ebd/E_0635) · MSB · Rückmeldung auf Änderung prüfen (Basiert auf EBD: E_0626_Rückmeldung auf Änderung prüfen)

</div>

</Schritt>

<details>
<summary>Entscheidungsbäume dieses Prozesses</summary>

| EBD | Name |
|---|---|
| [E_0415](/referenz/202604/ebd/E_0415) | Änderung vom MSB prüfen (Basiert auf EBD: E_0408_Änderung vom NB prüfen) |
| [E_0632](/referenz/202604/ebd/E_0632) | Rückmeldung auf Änderung prüfen (Basiert auf EBD: E_0626_Rückmeldung auf Änderung prüfen) |
| [E_0412](/referenz/202604/ebd/E_0412) | Änderung vom MSB prüfen (Basiert auf EBD: E_0408_Änderung vom NB prüfen) |
| [E_0583](/referenz/202604/ebd/E_0583) | Änderung vom MSB prüfen (Basiert auf EBD: E_0408_Änderung vom NB prüfen) |
| [E_0633](/referenz/202604/ebd/E_0633) | Rückmeldung auf Änderung prüfen (Basiert auf EBD: E_0626_Rückmeldung auf Änderung prüfen) |
| [E_0634](/referenz/202604/ebd/E_0634) | Rückmeldung auf Änderung prüfen (Basiert auf EBD: E_0626_Rückmeldung auf Änderung prüfen) |
| [E_0635](/referenz/202604/ebd/E_0635) | Rückmeldung auf Änderung prüfen (Basiert auf EBD: E_0626_Rückmeldung auf Änderung prüfen) |
| [E_0639](/referenz/202604/ebd/E_0639) | Änderung vom MSB prüfen (Basiert auf EBD: E_0408_Änderung vom NB prüfen) |

</details>

<a id="abschnitt-informationen"></a>

## Prozess-Informationen

Wortlaut der Lesefassung, Steckbrief Kap. 1.4.1, S. 5.

<Stepper>
<ol>

<li data-blatt="vorbedingungen">

### Vorbedingungen

- Es besteht eine aktuelle oder zukünftig abgestimmte Zuordnung der Marktpartner in der jeweiligen Rolle zur Lokation.

</li>

<li data-blatt="ergebnisse">

### Ergebnisse

- Die Folgeprozesse setzen auf abgeglichenen und synchronen Werten der Stammdaten ab dem Änderungsdatum auf.
- Durch die in diesem Use-Case durchgeführte Änderung kann es unter anderem dazu kommen, dass eine Wertübermittlung vom MSB erforderlich ist. Die Beauftragung der Werteübermittlung ergibt sich aus den Werten des entsprechenden Stammdatums. Es erfolgt keine weitere Beauftragung gegenüber dem MSB.

</li>

<li data-blatt="fehlerfall">

### Fehlerfall

#### Ergebnis im Fehlerfall

Der Verantwortliche muss in ein bilaterales Clearing mit den Beteiligten einsteigen und ggf. den Prozess erneut anstoßen.

#### Fehlerfälle

Die Rückmeldung ergibt den Rückschluss, dass die Daten nicht synchron im Markt vorliegen.

</li>

<li data-blatt="anforderungen">

### Weitere Anforderungen

- Im Fall des SD „Stammdatenänderung vom MSB (verantwortlich) ausgehend“ gilt: Der verantwortliche MSB einer Messlokation ist immer der MSB, der zum Zeitpunkt, zu dem die Änderung des Werts des Stammdatums erfolgt, der Messlokation zugeordnet ist. Dabei gilt folgende Ausnahme: Findet an der Messlokation der Use-Case „[Geräteübernahme](/prozessdoku/202604/MSB--MSBA/WiM-Teil1-geraeteuebernahme)“ (WiM Teil 1) statt, ist neben dem vorgenannten MSB (im Use-Case „[Geräteübernahme](/prozessdoku/202604/MSB--MSBA/WiM-Teil1-geraeteuebernahme)“ als MSBA bezeichnet) auch der MSBN berechtigt für diese Messlokation das SD „Stammdatenänderung vom MSB (verantwortlich) ausgehend“ als verantwortlicher MSB anzuwenden.

</li>

<li data-blatt="anlass">

### Anlass

- Bei dem für ein Stammdatum Verantwortlichen liegt ein neuer Wert für das Stammdatum vor. Diese Erkenntnis erhält der Verantwortliche z.B. aufgrund vorangehender Prozesse oder Nachrichten, die die Änderung eines Wertes eines Stammdatums für ein oder mehrere Berechtigte verursachen.
- Der Verantwortliche geht von einem Datenschiefstand zwischen den Berechtigten und dem Verantwortlichen aus.

**Vorher läuft:** [Beendigung einer Konfiguration vom MSB](/prozessdoku/202604/NB/GPKE-Teil3-beendigung-einer-konfiguration-vom-msb), [Bestellung Beendigung einer Konfiguration vom LF an MSB](/prozessdoku/202604/LF/GPKE-Teil3-bestellung-beendigung-einer-konfiguration-vom-lf-an-msb), [Bestellung Beendigung einer Konfiguration vom NB an MSB](/prozessdoku/202604/NB/GPKE-Teil3-bestellung-beendigung-einer-konfiguration-vom-nb-an-msb), [Bestellung Beendigung einer Konfiguration vom weiteren MSB an MSB](/prozessdoku/202604/NB/GPKE-Teil3-bestellung-beendigung-einer-konfiguration-vom-weiteren-msb-an-msb), [Bestellung einer Konfiguration vom LF an MSB](/prozessdoku/202604/LF/GPKE-Teil3-bestellung-einer-konfiguration-vom-lf-an-msb), [Bestellung einer Konfiguration vom NB an MSB](/prozessdoku/202604/NB/GPKE-Teil3-bestellung-einer-konfiguration-vom-nb-an-msb), [Einrichtung der Konfigurationen aufgrund einer Zuordnung eines LF zu einer Marktlokation bzw. Tranche](/prozessdoku/202604/NB/GPKE-Teil3-einrichtung-der-konfigurationen-aufgrund-einer-zuordnung-eines-lf-zu-einer-marktlokation-bzw-tranche) — diese Prozesse nennen den hier gezeigten in ihrem Ergebnis.

</li>

<li data-blatt="erste-nachricht">

### Erste Nachricht

**MSB** sendet „Änderung vom MSB an NB“ (Schritt 1). Ab hier ist der Beteiligte dieser Seite am Zug.

</li>

<li data-blatt="ziel">

### Ziel

Dem Verantwortlichen und den Berechtigten liegen die gleichen Werte der Stammdaten vor.

</li>

</ol>
</Stepper>

<a id="abschnitt-sichten"></a>

## Andere Sichten des Prozesses

Derselbe Prozess, aus den Augen der anderen Beteiligten: dieselben Schritte, jeweils aus deren Sicht gelesen.

- [Sicht LF](/prozessdoku/202604/LF/GPKE-Teil4-stammdatenaenderung-vom-msb-verantwortlich-ausgehend) — LF
- [Sicht MSB](/prozessdoku/202604/MSB/GPKE-Teil4-stammdatenaenderung-vom-msb-verantwortlich-ausgehend) — MSB
- [Sicht WMSB](/prozessdoku/202604/MSB--WMSB/GPKE-Teil4-stammdatenaenderung-vom-msb-verantwortlich-ausgehend) — weiterer Messstellenbetreiber · Marktrolle MSB
- [Sicht ÜNB](/prozessdoku/202604/UENB/GPKE-Teil4-stammdatenaenderung-vom-msb-verantwortlich-ausgehend) — ÜNB · Marktrolle UENB

<Hinweisbereich>

*Die Schritte sind die **möglichen** Nachrichten dieses Prozesses, keine Abfolge — die Quelle führt weder Bedingungen noch Alternativen. Das Kästchen am Schritt nennt links die eigene Sicht: **←** empfängt sie, **→** sendet sie. Zugeklappte Schritte laufen zwischen anderen Marktpartnern. Die Nummern sind die der Quelle; wo eine fehlt, fehlt sie dort.*

Diese Schreibaufrufe sind im API-Katalog dieser Formatversion nicht geführt; am Schritt steht deshalb nur ihr Kommando, ohne Adresse und ohne Knopf.

Betrifft: [1](#schritt-1)

</Hinweisbereich>
