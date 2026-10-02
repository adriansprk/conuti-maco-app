# Bestellung einer Konfiguration vom NB an MSB — Sicht MSB

<Kopf rolle="MSB" beteiligter="MSB" festlegung="GPKE" dokument="GPKE Teil 3" kapitel="1.3.3.2" sparte="Strom" schritte={10} suchtitel="Bestellung einer Konfiguration vom NB an MSB — Sicht MSB · GPKE Teil 3 · Formatversion 202610" abschnitte={[{"id": "abschnitt-ablauf", "label": "Prozessablauf"}, {"id": "abschnitt-schritte", "label": "Prozessschritte"}, {"id": "abschnitt-informationen", "label": "Prozess-Informationen"}, {"id": "abschnitt-sichten", "label": "Andere Sichten des Prozesses"}]} />

<Kurzfassung>

Der NB bzw. LF bestellt beim MSB der direkt betroffenen Lokation eine Konfiguration für die direkt betroffene Lokation. Sofern weitere Lokationen der direkt betroffenen Lokation von der Konfiguration betroffen sind, gibt der NB bzw. LF diese weiter betroffenen Lokationen in der Bestellung ebenfalls an (z.B. hat der NB in der Bestellung der Änderung des Bilanzierungsverfahrens auf der Ebene der Marktlokation, neben der Marktlokation auch alle Messlokationen der Marktlokation beim MSB der Marktlokation zu bestellen). Bevor eine kostenpflichtige Bestellung erfolgen kann, hat der NB bzw. LF ein Angebot beim MSB der direkt betroffenen Lokation für die Einrichtung der Konfiguration anzufragen. Der MSB prüft die Bestellung und teilt dem NB bzw. LF das weitere Vorgehen zur Bestellung mit. Sofern weitere Lokationen der direkt betroffenen Lokation von der Konfiguration betroffen sind, für die der MSB der direkt betroffenen Lokation nicht den Messstellenbetrieb durchführt, bindet er für diese weiter betroffenen Lokationen die jeweiligen weiteren MSB ein.

</Kurzfassung>

<a id="abschnitt-ablauf"></a>

## Prozessablauf aus Sicht des MSB

<Systembild svg={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1004 2900\" width=\"1004\" height=\"2900\" role=\"img\" aria-labelledby=\"sb-title\" class=\"maco-systembild\">\n<title id=\"sb-title\">Systembild: Bestellung einer Konfiguration vom NB an MSB aus Sicht MSB</title>\n<defs><marker id=\"sb-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect class=\"sb-lane-kopf\" x=\"16\" y=\"12\" width=\"232\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend-System des Kunden</text>\n<rect class=\"sb-lane-kopf\" x=\"398\" y=\"12\" width=\"264\" height=\"46\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · MSB</text>\n<rect class=\"sb-lane-kopf\" x=\"812\" y=\"12\" width=\"176\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"900\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Marktpartner</text>\n<line x1=\"323\" y1=\"58\" x2=\"323\" y2=\"2888\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"737\" y1=\"58\" x2=\"737\" y2=\"2888\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"80\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">1. Anfrage einer</text>\n<text x=\"530\" y=\"115\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Konfiguration auf Ebene der</text>\n<text x=\"530\" y=\"130\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">direkt betroffene…</text>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"93\" r=\"5\"/><line x1=\"900\" y1=\"98\" x2=\"900\" y2=\"110\"/><line x1=\"893\" y1=\"102\" x2=\"907\" y2=\"102\"/><line x1=\"900\" y1=\"110\" x2=\"894\" y2=\"120\"/><line x1=\"900\" y1=\"110\" x2=\"906\" y2=\"120\"/></g>\n<text x=\"900\" y=\"142\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"878\" y1=\"111\" x2=\"628\" y2=\"111\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"103\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"127\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">35004</text>\n<rect class=\"sb-kasten sb-aperak_lesen\" x=\"432\" y=\"169\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"189\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Daten für die</text>\n<text x=\"530\" y=\"204\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Eingangsprüfung laden</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"143\" x2=\"530\" y2=\"169\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-aperak_lesen\" x=\"34\" y=\"169\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"189\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">4 Lese-Schnittstellen</text>\n<text x=\"132\" y=\"204\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">aufgerufen</text>\n<line x1=\"432\" y1=\"193\" x2=\"230\" y2=\"193\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"185\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<text x=\"331\" y=\"209\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">je einzeln am Schritt</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"243\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"263\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z10, Z17, Z18</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"217\" x2=\"530\" y2=\"243\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-schreiben\" x=\"432\" y=\"307\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"327\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"276\" x2=\"530\" y2=\"307\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-schreiben\" x=\"34\" y=\"307\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"327\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten erstellen</text>\n<line x1=\"432\" y1=\"323\" x2=\"230\" y2=\"323\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"315\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-lesen\" x=\"432\" y=\"371\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"391\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Daten für die Prüfung laden</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"340\" x2=\"530\" y2=\"371\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-lesen\" x=\"34\" y=\"363\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"383\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">4 Lese-Schnittstellen</text>\n<text x=\"132\" y=\"398\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">aufgerufen</text>\n<line x1=\"432\" y1=\"387\" x2=\"230\" y2=\"387\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"379\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<text x=\"331\" y=\"403\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">je einzeln am Schritt</text>\n<rect class=\"sb-kasten sb-ebd\" x=\"432\" y=\"445\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"465\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">EBD prüfen: E_0524</text>\n<text x=\"530\" y=\"480\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label-2, #424245)\">Anfrage prüfen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"404\" x2=\"530\" y2=\"445\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-folgeprozess\" x=\"432\" y=\"519\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"539\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Folgeprozess auslösen:</text>\n<text x=\"530\" y=\"554\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">15004, 21033</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"493\" x2=\"530\" y2=\"519\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-folge_ausloeser\" x=\"432\" y=\"593\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"613\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Ausgelöst durch Eingang:</text>\n<text x=\"530\" y=\"628\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">35004</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"567\" x2=\"530\" y2=\"593\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"667\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"687\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">2. Angebot zur/ Ablehnung</text>\n<text x=\"530\" y=\"702\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">der Anfrage</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"641\" x2=\"530\" y2=\"667\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"673\" r=\"5\"/><line x1=\"900\" y1=\"678\" x2=\"900\" y2=\"690\"/><line x1=\"893\" y1=\"682\" x2=\"907\" y2=\"682\"/><line x1=\"900\" y1=\"690\" x2=\"894\" y2=\"700\"/><line x1=\"900\" y1=\"690\" x2=\"906\" y2=\"700\"/></g>\n<text x=\"900\" y=\"722\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"628\" y1=\"691\" x2=\"878\" y2=\"691\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"683\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"707\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">15004, 21033</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"750\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"770\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"715\" x2=\"530\" y2=\"750\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"750\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"770\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"766\" x2=\"230\" y2=\"766\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"758\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"814\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"834\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">3. Bestellung einer</text>\n<text x=\"530\" y=\"849\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Konfiguration auf Ebene der</text>\n<text x=\"530\" y=\"864\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">direkt betroff…</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"783\" x2=\"530\" y2=\"814\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"827\" r=\"5\"/><line x1=\"900\" y1=\"832\" x2=\"900\" y2=\"844\"/><line x1=\"893\" y1=\"836\" x2=\"907\" y2=\"836\"/><line x1=\"900\" y1=\"844\" x2=\"894\" y2=\"854\"/><line x1=\"900\" y1=\"844\" x2=\"906\" y2=\"854\"/></g>\n<text x=\"900\" y=\"876\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"878\" y1=\"845\" x2=\"628\" y2=\"845\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"837\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"861\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">17131</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"903\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"923\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z33</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"877\" x2=\"530\" y2=\"903\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"967\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"987\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"936\" x2=\"530\" y2=\"967\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"967\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"987\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"983\" x2=\"230\" y2=\"983\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"975\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-lesen\" x=\"432\" y=\"1031\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1051\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Daten für die Prüfung laden</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1000\" x2=\"530\" y2=\"1031\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-lesen\" x=\"34\" y=\"1023\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"1043\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">9 Lese-Schnittstellen</text>\n<text x=\"132\" y=\"1058\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">aufgerufen</text>\n<line x1=\"432\" y1=\"1047\" x2=\"230\" y2=\"1047\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"1039\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<text x=\"331\" y=\"1063\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">je einzeln am Schritt</text>\n<rect class=\"sb-kasten sb-ebd\" x=\"432\" y=\"1105\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1125\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">EBD prüfen: E_0526</text>\n<text x=\"530\" y=\"1140\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label-2, #424245)\">Bestellung prüfen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1064\" x2=\"530\" y2=\"1105\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-folgeprozess\" x=\"432\" y=\"1179\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1199\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Folgeprozess auslösen:</text>\n<text x=\"530\" y=\"1214\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">19132</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1153\" x2=\"530\" y2=\"1179\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"1253\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1273\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">4. Bestellung einer</text>\n<text x=\"530\" y=\"1288\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Konfiguration auf Ebene der</text>\n<text x=\"530\" y=\"1303\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">direkt betroff…</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1227\" x2=\"530\" y2=\"1253\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"1266\" r=\"5\"/><line x1=\"900\" y1=\"1271\" x2=\"900\" y2=\"1283\"/><line x1=\"893\" y1=\"1275\" x2=\"907\" y2=\"1275\"/><line x1=\"900\" y1=\"1283\" x2=\"894\" y2=\"1293\"/><line x1=\"900\" y1=\"1283\" x2=\"906\" y2=\"1293\"/></g>\n<text x=\"900\" y=\"1315\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"878\" y1=\"1284\" x2=\"628\" y2=\"1284\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"1276\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"1300\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">17130, 17121</text>\n<rect class=\"sb-kasten sb-aperak_lesen\" x=\"432\" y=\"1342\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1362\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Daten für die</text>\n<text x=\"530\" y=\"1377\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Eingangsprüfung laden</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1316\" x2=\"530\" y2=\"1342\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-aperak_lesen\" x=\"34\" y=\"1342\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"1362\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">4 Lese-Schnittstellen</text>\n<text x=\"132\" y=\"1377\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">aufgerufen</text>\n<line x1=\"432\" y1=\"1366\" x2=\"230\" y2=\"1366\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"1358\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<text x=\"331\" y=\"1382\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">je einzeln am Schritt</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"1416\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1436\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z10, Z17,</text>\n<text x=\"530\" y=\"1451\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Z18, Z33</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1390\" x2=\"530\" y2=\"1416\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-schreiben\" x=\"432\" y=\"1490\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1510\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1464\" x2=\"530\" y2=\"1490\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-schreiben\" x=\"34\" y=\"1490\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"1510\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten erstellen</text>\n<line x1=\"432\" y1=\"1506\" x2=\"230\" y2=\"1506\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"1498\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-lesen\" x=\"432\" y=\"1554\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1574\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Daten für die Prüfung laden</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1523\" x2=\"530\" y2=\"1554\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-lesen\" x=\"34\" y=\"1546\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"1566\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">6 Lese-Schnittstellen</text>\n<text x=\"132\" y=\"1581\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">aufgerufen</text>\n<line x1=\"432\" y1=\"1570\" x2=\"230\" y2=\"1570\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"1562\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<text x=\"331\" y=\"1586\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">je einzeln am Schritt</text>\n<rect class=\"sb-kasten sb-ebd\" x=\"432\" y=\"1628\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1648\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">EBD prüfen: E_0526</text>\n<text x=\"530\" y=\"1663\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label-2, #424245)\">Bestellung prüfen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1587\" x2=\"530\" y2=\"1628\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-folgeprozess\" x=\"432\" y=\"1702\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1722\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Folgeprozess auslösen:</text>\n<text x=\"530\" y=\"1737\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">17118, 19120, 19132</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1676\" x2=\"530\" y2=\"1702\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-folge_ausloeser\" x=\"432\" y=\"1776\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1796\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Ausgelöst durch Eingang:</text>\n<text x=\"530\" y=\"1811\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">17121, 17130, 17131</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1750\" x2=\"530\" y2=\"1776\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"1850\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1870\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">5. Mitteilung zum weiteren</text>\n<text x=\"530\" y=\"1885\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgehen zur Bestellung</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1824\" x2=\"530\" y2=\"1850\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"1856\" r=\"5\"/><line x1=\"900\" y1=\"1861\" x2=\"900\" y2=\"1873\"/><line x1=\"893\" y1=\"1865\" x2=\"907\" y2=\"1865\"/><line x1=\"900\" y1=\"1873\" x2=\"894\" y2=\"1883\"/><line x1=\"900\" y1=\"1873\" x2=\"906\" y2=\"1883\"/></g>\n<text x=\"900\" y=\"1905\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"628\" y1=\"1874\" x2=\"878\" y2=\"1874\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"1866\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"1890\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">19132, 19120</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"1933\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1953\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1898\" x2=\"530\" y2=\"1933\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"1933\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"1953\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"1949\" x2=\"230\" y2=\"1949\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"1941\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-folge_ausloeser\" x=\"432\" y=\"1997\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"2017\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Ausgelöst durch Eingang:</text>\n<text x=\"530\" y=\"2032\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">17121</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1966\" x2=\"530\" y2=\"1997\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"2071\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"2091\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">6. Bestellung einer</text>\n<text x=\"530\" y=\"2106\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Konfiguration für weiter</text>\n<text x=\"530\" y=\"2121\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">betroffene Lokati…</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"2045\" x2=\"530\" y2=\"2071\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"2084\" r=\"5\"/><line x1=\"900\" y1=\"2089\" x2=\"900\" y2=\"2101\"/><line x1=\"893\" y1=\"2093\" x2=\"907\" y2=\"2093\"/><line x1=\"900\" y1=\"2101\" x2=\"894\" y2=\"2111\"/><line x1=\"900\" y1=\"2101\" x2=\"906\" y2=\"2111\"/></g>\n<text x=\"900\" y=\"2133\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">weiterer MSB</text>\n<line x1=\"628\" y1=\"2102\" x2=\"878\" y2=\"2102\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"2094\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"2118\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">17130, 17118</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"2160\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"2180\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"2134\" x2=\"530\" y2=\"2160\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"2160\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"2180\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"2176\" x2=\"230\" y2=\"2176\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"2168\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"2224\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"2244\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">7. Mitteilung zum weiteren</text>\n<text x=\"530\" y=\"2259\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgehen zur Bestellung</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"2193\" x2=\"530\" y2=\"2224\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"2230\" r=\"5\"/><line x1=\"900\" y1=\"2235\" x2=\"900\" y2=\"2247\"/><line x1=\"893\" y1=\"2239\" x2=\"907\" y2=\"2239\"/><line x1=\"900\" y1=\"2247\" x2=\"894\" y2=\"2257\"/><line x1=\"900\" y1=\"2247\" x2=\"906\" y2=\"2257\"/></g>\n<text x=\"900\" y=\"2279\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">weiterer MSB</text>\n<line x1=\"878\" y1=\"2248\" x2=\"628\" y2=\"2248\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"2240\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"2264\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">19132, 19127</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"2307\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"2327\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z33</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"2272\" x2=\"530\" y2=\"2307\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"2371\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"2391\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"2340\" x2=\"530\" y2=\"2371\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben sb-abgeleitet\" x=\"34\" y=\"2371\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"2391\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"2387\" x2=\"230\" y2=\"2387\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"2379\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"2435\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"2455\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">8. Antwort auf Bestellung</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"2404\" x2=\"530\" y2=\"2435\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"2433\" r=\"5\"/><line x1=\"900\" y1=\"2438\" x2=\"900\" y2=\"2450\"/><line x1=\"893\" y1=\"2442\" x2=\"907\" y2=\"2442\"/><line x1=\"900\" y1=\"2450\" x2=\"894\" y2=\"2460\"/><line x1=\"900\" y1=\"2450\" x2=\"906\" y2=\"2460\"/></g>\n<text x=\"900\" y=\"2482\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">weiterer MSB</text>\n<line x1=\"628\" y1=\"2451\" x2=\"878\" y2=\"2451\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"2443\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"2467\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">21043</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"2518\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"2538\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"2468\" x2=\"530\" y2=\"2518\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"2518\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"2538\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"2534\" x2=\"230\" y2=\"2534\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"2526\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"2582\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"2602\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">9. Antwort auf Bestellung</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"2551\" x2=\"530\" y2=\"2582\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"2580\" r=\"5\"/><line x1=\"900\" y1=\"2585\" x2=\"900\" y2=\"2597\"/><line x1=\"893\" y1=\"2589\" x2=\"907\" y2=\"2589\"/><line x1=\"900\" y1=\"2597\" x2=\"894\" y2=\"2607\"/><line x1=\"900\" y1=\"2597\" x2=\"906\" y2=\"2607\"/></g>\n<text x=\"900\" y=\"2629\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"628\" y1=\"2598\" x2=\"878\" y2=\"2598\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"2590\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"2614\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">21043</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"2665\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"2685\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"2615\" x2=\"530\" y2=\"2665\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"2665\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"2685\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"2681\" x2=\"230\" y2=\"2681\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"2673\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"2729\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"2749\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">10. Mitteilung über</text>\n<text x=\"530\" y=\"2764\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Gesamtvorgang</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"2698\" x2=\"530\" y2=\"2729\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"2735\" r=\"5\"/><line x1=\"900\" y1=\"2740\" x2=\"900\" y2=\"2752\"/><line x1=\"893\" y1=\"2744\" x2=\"907\" y2=\"2744\"/><line x1=\"900\" y1=\"2752\" x2=\"894\" y2=\"2762\"/><line x1=\"900\" y1=\"2752\" x2=\"906\" y2=\"2762\"/></g>\n<text x=\"900\" y=\"2784\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">weiterer MSB</text>\n<line x1=\"628\" y1=\"2753\" x2=\"878\" y2=\"2753\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"2745\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"2769\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">21043</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"2812\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"2832\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"2777\" x2=\"530\" y2=\"2812\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"2812\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"2832\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"2828\" x2=\"230\" y2=\"2828\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"2820\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n</svg>"} gesamt={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 974 1354\" width=\"974\" height=\"1354\" role=\"img\" aria-labelledby=\"sd-title\" class=\"maco-sequence\">\n<title id=\"sd-title\">Sequenzdiagramm: Bestellung einer Konfiguration vom NB an MSB aus Sicht MSB</title>\n<defs><marker id=\"sd-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect x=\"16\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"121\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend (Kunde)</text>\n<line x1=\"121\" y1=\"64\" x2=\"121\" y2=\"1342\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"260\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"365\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · MSB</text>\n<line x1=\"365\" y1=\"64\" x2=\"365\" y2=\"1342\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"504\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"609\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"609\" y1=\"64\" x2=\"609\" y2=\"1342\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"748\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"853\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">weiterer MSB</text>\n<line x1=\"853\" y1=\"64\" x2=\"853\" y2=\"1342\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"609\" y1=\"90\" x2=\"365\" y2=\"90\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"81\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">1. Anfrage einer Konfiguration auf Ebene der dir…</text>\n<text x=\"487\" y=\"105\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 35004</text>\n<line x1=\"365\" y1=\"152\" x2=\"121\" y2=\"152\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"143\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<text x=\"243\" y=\"167\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten erstellen</text>\n<line x1=\"365\" y1=\"214\" x2=\"609\" y2=\"214\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"205\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">2. Angebot zur/ Ablehnung der Anfrage</text>\n<text x=\"487\" y=\"229\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 15004, 21033 · E_0524</text>\n<text x=\"487\" y=\"242\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0524 — Anfrage prüfen</text>\n<line x1=\"365\" y1=\"276\" x2=\"121\" y2=\"276\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"267\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"291\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"609\" y1=\"338\" x2=\"365\" y2=\"338\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"329\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">3. Bestellung einer Konfiguration auf Ebene der…</text>\n<text x=\"487\" y=\"353\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 17131</text>\n<line x1=\"365\" y1=\"400\" x2=\"121\" y2=\"400\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"391\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"415\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"609\" y1=\"462\" x2=\"365\" y2=\"462\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"453\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">4. Bestellung einer Konfiguration auf Ebene der…</text>\n<text x=\"487\" y=\"477\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 17130, 17121</text>\n<line x1=\"365\" y1=\"524\" x2=\"121\" y2=\"524\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"515\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<text x=\"243\" y=\"539\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten erstellen</text>\n<line x1=\"365\" y1=\"586\" x2=\"609\" y2=\"586\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"577\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">5. Mitteilung zum weiteren Vorgehen zur Bestellu…</text>\n<text x=\"487\" y=\"601\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 19132, 19120 · E_0526</text>\n<text x=\"487\" y=\"614\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0526 — Bestellung prüfen</text>\n<line x1=\"365\" y1=\"648\" x2=\"121\" y2=\"648\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"639\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"663\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"365\" y1=\"710\" x2=\"853\" y2=\"710\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"609\" y=\"701\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">6. Bestellung einer Konfiguration für weiter bet…</text>\n<text x=\"609\" y=\"725\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 17130, 17118</text>\n<line x1=\"365\" y1=\"772\" x2=\"121\" y2=\"772\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"763\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"787\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"853\" y1=\"834\" x2=\"365\" y2=\"834\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"609\" y=\"825\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">7. Mitteilung zum weiteren Vorgehen zur Bestellu…</text>\n<text x=\"609\" y=\"849\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 19132, 19127 · E_0527</text>\n<text x=\"609\" y=\"862\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0527 — Bestellung</text>\n<line x1=\"365\" y1=\"896\" x2=\"121\" y2=\"896\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"887\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"911\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"365\" y1=\"958\" x2=\"853\" y2=\"958\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"609\" y=\"949\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">8. Antwort auf Bestellung</text>\n<text x=\"609\" y=\"973\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 21043 · E_0528</text>\n<text x=\"609\" y=\"986\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0528 — Umsetzung der Konfiguration prüfen</text>\n<line x1=\"365\" y1=\"1020\" x2=\"121\" y2=\"1020\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"1011\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"1035\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"365\" y1=\"1082\" x2=\"609\" y2=\"1082\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"1073\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">9. Antwort auf Bestellung</text>\n<text x=\"487\" y=\"1097\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 21043 · E_0529</text>\n<text x=\"487\" y=\"1110\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0529 — Bewertung des Gesamtvorgangs</text>\n<line x1=\"365\" y1=\"1144\" x2=\"121\" y2=\"1144\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"1135\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"1159\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"365\" y1=\"1206\" x2=\"853\" y2=\"1206\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"609\" y=\"1197\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">10. Mitteilung über Gesamtvorgang</text>\n<text x=\"609\" y=\"1221\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 21043 · E_0529</text>\n<text x=\"609\" y=\"1234\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0529 — Bewertung des Gesamtvorgangs</text>\n<line x1=\"365\" y1=\"1268\" x2=\"121\" y2=\"1268\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"1259\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"1283\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n</svg>"} titel="MSB" />

<a id="abschnitt-schritte"></a>

## Prozessschritte

<Schritt nr="1" anker="schritt-1" richtung="eingehend" kopf={{"links": {"label": "MSB", "eigen": true}, "rechts": {"label": "NB"}}}>

### Anfrage einer Konfiguration auf Ebene der direkt betroffenen Lokation

<Schrittskizze sicht={{"label": "MSB"}} zeilen={[{"art": "empfangen", "label": "NB", "weg": "AS4", "nachrichten": [{"nr": "35004", "titel": "Anfrage einer Konfiguration"}]}, {"art": "lesen_aperak", "schnittstellen": [{"label": "Marktlokation lesen"}, {"label": "Messlokation lesen"}, {"label": "Netzlokation lesen"}, {"label": "Steuerbare Ressource lesen"}]}, {"art": "aperak", "werte": ["Z10", "Z17", "Z18"]}, {"art": "erstellen"}, {"art": "lesen_ebd", "schnittstellen": [{"label": "Messlokation lesen"}, {"label": "Netzlokation lesen"}, {"label": "Preisblatt lesen"}, {"label": "LESEN_STEUERBARE_RESOURCE_BASIS"}]}, {"art": "ebd", "baeume": [{"code": "E_0524", "titel": "Anfrage prüfen"}]}, {"art": "folgeprozess", "werte": ["15004", "21033"]}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [35004](/schnittstellen/202610/pruefi/REQOTE/PI_35004) — Anfrage einer Konfiguration · AS4

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
- [Messlokation lesen](/api/202610/backend-lesen/getmeterlocationbasic#messlokation-lesen) `GET /getMeterLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getMeterLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_MESSLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Netzlokation lesen](/api/202610/backend-lesen/getgridlocationbasic#netzlokation-lesen) `GET /getGridLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getGridLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_NETZLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Steuerbare Ressource lesen](/api/202610/backend-lesen/getcontrollableresourcebasic#steuerbare-ressource-lesen) `GET /getControllableResourceBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getControllableResourceBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

</li>

<li data-teil="aperak">

**Aperak-Prüfungen**
- `35004` → `Z10`
- `35004` → `Z17`
- `35004` → `Z18`

</li>

<li data-teil="schnittstelle" data-art="schreiben">

**Schreibende Schnittstelle**
- Vorgang angelegt — [Prozessdaten erstellen](/api/202610/backend-schreiben-msb/createprocessdata#prozessdaten-erstellen) `POST /createProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/createProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "ERSTELLEN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"ANFRAGE\": [\n      {\n        \"anfragetyp\": \"AENDERUNG_KONFIGURATION\",\n        \"boTyp\": \"ANFRAGE\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"LEISTUNGSKURVENDEFINITION\": [\n      {\n        \"boTyp\": \"LEISTUNGSKURVENDEFINITION\",\n        \"leistungskurven\": [\n          {\n            \"code\": \"MMA\",\n            \"konfigurationsprodukt\": \"9991000000721\"\n          }\n        ],\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"MARKTLOKATION\": [\n      {\n        \"boTyp\": \"MARKTLOKATION\",\n        \"marktlokationsId\": \"50444001616\",\n        \"marktlokationsTyp\": [\n          {\n            \"typ\": \"STANDARD_MARKTLOKATION\"\n          }\n        ],\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"ansprechpartner\": {\n        \"boTyp\": \"ANSPRECHPARTNER\",\n        \"eMailAdresse\": \"Max.Mustermann@conuti.de\",\n        \"nachname\": \"Max Mustermann\",\n        \"versionStruktur\": \"1\"\n      },\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9900496000001\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"datenaustauschreferenz\": \"M3VQCXCY\",\n    \"dokumentennummer\": \"BGMM3TJAKY3\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9900496000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"Z82\",\n    \"lieferdatum\": \"2025-01-05T23:00:00Z\",\n    \"nachrichtenReferenzBestellbestaetigung\": \"BGMM44X6WGM\",\n    \"nachrichtendatum\": \"2026-10-01T11:00:00Z\",\n    \"nachrichtenreferenznummer\": \"UNHM3Q4M8YM\",\n    \"positionsnummer\": 1,\n    \"pruefidentifikator\": \"35004\",\n    \"sparte\": \"STROM\",\n    \"vorgangsReferenzBestellbestaetigung\": \"45261\"\n  },\n  \"zusatzdaten\": {}\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Legt im Backend einen neuen Vorgang mit den Daten der eingegangenen Nachricht an.

</li>

<li data-teil="lesen" data-stufe="ebd">

**Daten für die Prüfung laden**
- [Messlokation lesen](/api/202610/backend-lesen/getmeterlocationbasic#messlokation-lesen) `GET /getMeterLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getMeterLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_MESSLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Netzlokation lesen](/api/202610/backend-lesen/getgridlocationbasic#netzlokation-lesen) `GET /getGridLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getGridLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_NETZLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Preisblatt lesen](/api/202610/backend-lesen/getpricesheetbasic#preisblatt-lesen) `GET /getPriceSheetBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getPriceSheetBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": false, "defaultValue": "74018657187", "type": "string"}, {"name": "parameter2", "isRequired": false, "defaultValue": "MALO", "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": false, "defaultValue": "2024-06-28T12:18:00Z", "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_PREISBLATT_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- `LESEN_STEUERBARE_RESOURCE_BASIS`

</li>

<li data-teil="baum">

**Entscheidungsbaum**
- `35004` → [E_0524](/referenz/202610/ebd/E_0524) — Anfrage prüfen

</li>

<li data-teil="folgeprozess">

**Folgeprozess auslösen**
- [15004](/schnittstellen/202610/pruefi/QUOTES/PI_15004) — Angebot  einer Konfiguration
- [21033](/schnittstellen/202610/pruefi/IFTSTA/PI_21033) — Ablehnung der Anfrage

Nach der Verarbeitung startet die MACO APP den Folgeprozess selbst; welcher davon läuft, hängt vom Ergebnis der Verarbeitung ab.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="2" anker="schritt-2" richtung="ausgehend" kopf={{"links": {"label": "MSB", "eigen": true}, "rechts": {"label": "NB"}}}>

### Angebot zur/ Ablehnung der Anfrage

<Schrittskizze sicht={{"label": "MSB"}} zeilen={[{"art": "folge_ausloeser", "werte": ["35004"]}, {"art": "senden", "label": "NB", "weg": "AS4", "nachrichten": [{"nr": "15004", "titel": "Angebot  einer Konfiguration"}, {"nr": "21033", "titel": "Ablehnung der Anfrage"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [15004](/schnittstellen/202610/pruefi/QUOTES/PI_15004) — Angebot  einer Konfiguration · AS4
- [21033](/schnittstellen/202610/pruefi/IFTSTA/PI_21033) — Ablehnung der Anfrage · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="folge_ausloeser">

**Ausgelöst durch Eingang**
- [35004](/schnittstellen/202610/pruefi/REQOTE/PI_35004) — Anfrage einer Konfiguration

Die MACO APP sendet diese Nachricht selbst, als Folgeprozess nach diesem Eingang.

</li>

<li data-teil="nachricht">

Nachricht an **NB** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `21033` → [E_0524](/referenz/202610/ebd/E_0524) · MSB · Anfrage prüfen

</div>

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202610/backend-schreiben-msb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"ANFRAGE\": [\n      {\n        \"anfragetyp\": \"NEUKONFIGURATION\",\n        \"boTyp\": \"ANFRAGE\",\n        \"lokationsId\": \"50074561188\",\n        \"lokationsTyp\": \"MALO\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"ANGEBOT\": [\n      {\n        \"anfragereferenz\": \"AVV12345\",\n        \"boTyp\": \"ANGEBOT\",\n        \"positionsdaten\": [\n          {\n            \"artikelId\": [\n              \"9991000000721-01\",\n              \"9991000000721-02\",\n              \"9991000000721-03\"\n            ],\n            \"positionsbezeichnung\": \"1\"\n          }\n        ],\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"LEISTUNGSKURVENDEFINITION\": [\n      {\n        \"boTyp\": \"LEISTUNGSKURVENDEFINITION\",\n        \"leistungskurven\": [\n          {\n            \"code\": \"NBF\",\n            \"konfigurationsprodukt\": \"9991000000721\"\n          }\n        ],\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"MARKTLOKATION\": [\n      {\n        \"boTyp\": \"MARKTLOKATION\",\n        \"marktlokationsId\": \"50074561188\",\n        \"marktlokationsTyp\": [\n          {\n            \"typ\": \"STANDARD_MARKTLOKATION\"\n          }\n        ],\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"ansprechpartner\": {\n        \"boTyp\": \"ANSPRECHPARTNER\",\n        \"nachname\": \"Max Mustermann\",\n        \"rufnummern\": [\n          {\n            \"nummerntyp\": \"FAX_DURCHWAHL\",\n            \"rufnummer\": \"+001234567\"\n          }\n        ],\n        \"versionStruktur\": \"1\"\n      },\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9904446000007\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"datenaustauschreferenz\": \"MCH0IOL1\",\n    \"dokumentennummer\": \"BGMMC2WCO3K\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9903790000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"Z74\",\n    \"nachrichtendatum\": \"2026-10-01T11:00:00Z\",\n    \"nachrichtenreferenznummer\": \"UNHMC75CA7G\",\n    \"pruefidentifikator\": \"15004\",\n    \"sparte\": \"STROM\"\n  },\n  \"zusatzdaten\": {}\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend fort, nachdem die Nachricht erstellt ist.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="3" anker="schritt-3" richtung="eingehend" kopf={{"links": {"label": "MSB", "eigen": true}, "rechts": {"label": "NB"}}}>

### Bestellung einer Konfiguration auf Ebene der direkt betroffenen Lokation

<Schrittskizze sicht={{"label": "MSB"}} zeilen={[{"art": "empfangen", "label": "NB", "weg": "AS4", "nachrichten": [{"nr": "17131", "titel": "Bestellung Angebot einer Konfiguration"}]}, {"art": "aperak", "werte": ["Z33"]}, {"art": "fortschreiben"}, {"art": "lesen_ebd", "schnittstellen": [{"label": "LESEN_ANGEBOT_BASIS"}, {"label": "LESEN_DEFINITION_LST_KURVEN"}, {"label": "Schaltzeitdefinition lesen"}, {"label": "Zaehlzeitdefinition lesen"}, {"label": "Marktlokation lesen"}, {"label": "Messlokation lesen"}, {"label": "Netzlokation lesen"}, {"label": "Preisblatt lesen"}, {"label": "LESEN_STEUERBARE_RESOURCE_BASIS"}]}, {"art": "ebd", "baeume": [{"code": "E_0526", "titel": "Bestellung prüfen"}]}, {"art": "folgeprozess", "werte": ["19132"]}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [17131](/schnittstellen/202610/pruefi/ORDERS/PI_17131) — Bestellung Angebot einer Konfiguration · AS4

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
- `17131` → `Z33`

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202610/backend-schreiben-msb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"ANFRAGE\": [\n      {\n        \"anfragekategorie\": \"BESTELLUNG_EINES_ANGEBOTS_EINER_KONFIGURATION\",\n        \"boTyp\": \"ANFRAGE\",\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"marktrolle\": \"LF\",\n      \"rollencodenummer\": \"9979309000006\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"angebotsnummer\": \"12474\",\n    \"datenaustauschreferenz\": \"M03UGIN5\",\n    \"dokumentennummer\": \"M0ACK2J3\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9904733000009\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"nachrichtendatum\": \"2026-10-01T11:00:00Z\",\n    \"nachrichtenreferenznummer\": \"M01KAXGA\",\n    \"pruefidentifikator\": \"17131\",\n    \"sparte\": \"STROM\"\n  },\n  \"zusatzdaten\": {}\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend mit den Daten der eingegangenen Nachricht fort.

</li>

<li data-teil="lesen" data-stufe="ebd">

**Daten für die Prüfung laden**
- `LESEN_ANGEBOT_BASIS`
- `LESEN_DEFINITION_LST_KURVEN`
- [Schaltzeitdefinition lesen](/api/202610/backend-lesen/getdefinitionswitch#schaltzeitdefinition-lesen) `GET /getDefinitionSwitch` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getDefinitionSwitch"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": false, "defaultValue": "MALO", "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": false, "defaultValue": "2024-06-28T12:18:00Z", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Zaehlzeitdefinition lesen ](/api/202610/backend-lesen/getdefinitioncounting#zaehlzeitdefinition-lesen) `GET /getDefinitionCounting` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getDefinitionCounting"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": false, "defaultValue": "MALO", "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": false, "defaultValue": "2024-06-28T12:18:00Z", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Marktlokation lesen](/api/202610/backend-lesen/getmarketlocationbasic#marktlokation-lesen) `GET /getMarketLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getMarketLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": false, "defaultValue": "MALO", "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": false, "defaultValue": "2024-06-28T12:18:00Z", "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_MARKTLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Messlokation lesen](/api/202610/backend-lesen/getmeterlocationbasic#messlokation-lesen) `GET /getMeterLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getMeterLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_MESSLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Netzlokation lesen](/api/202610/backend-lesen/getgridlocationbasic#netzlokation-lesen) `GET /getGridLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getGridLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_NETZLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Preisblatt lesen](/api/202610/backend-lesen/getpricesheetbasic#preisblatt-lesen) `GET /getPriceSheetBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getPriceSheetBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": false, "defaultValue": "74018657187", "type": "string"}, {"name": "parameter2", "isRequired": false, "defaultValue": "MALO", "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": false, "defaultValue": "2024-06-28T12:18:00Z", "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_PREISBLATT_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- `LESEN_STEUERBARE_RESOURCE_BASIS`

</li>

<li data-teil="baum">

**Entscheidungsbaum**
- `17131` → [E_0526](/referenz/202610/ebd/E_0526) — Bestellung prüfen

</li>

<li data-teil="folgeprozess">

**Folgeprozess auslösen**
- [19132](/schnittstellen/202610/pruefi/ORDRSP/PI_19132) — Mitteilung zur Bestellung Konfiguration

Nach der Verarbeitung startet die MACO APP diesen Folgeprozess selbst.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="4" anker="schritt-4" richtung="eingehend" kopf={{"links": {"label": "MSB", "eigen": true}, "rechts": {"label": "NB"}}}>

### Bestellung einer Konfiguration auf Ebene der direkt betroffenen Lokation

<Schrittskizze sicht={{"label": "MSB"}} zeilen={[{"art": "empfangen", "label": "NB", "weg": "AS4", "nachrichten": [{"nr": "17130", "titel": "Bestellung einer Konfiguration"}, {"nr": "17121", "titel": "Bestellung Änderung"}]}, {"art": "lesen_aperak", "schnittstellen": [{"label": "Marktlokation lesen"}, {"label": "Messlokation lesen"}, {"label": "Netzlokation lesen"}, {"label": "Steuerbare Ressource lesen"}]}, {"art": "aperak", "werte": ["Z10", "Z17", "Z18", "Z33"]}, {"art": "erstellen"}, {"art": "lesen_ebd", "schnittstellen": [{"label": "LESEN_DEFINITION_LST_KURVEN"}, {"label": "Schaltzeitdefinition lesen"}, {"label": "Zaehlzeitdefinition lesen"}, {"label": "Messlokation lesen"}, {"label": "Preisblatt lesen"}, {"label": "Tranche lesen"}]}, {"art": "ebd", "baeume": [{"code": "E_0526", "titel": "Bestellung prüfen"}]}, {"art": "folgeprozess", "werte": ["17118", "19120", "19132"]}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [17130](/schnittstellen/202610/pruefi/ORDERS/PI_17130) — Bestellung einer Konfiguration · AS4
- [17121](/schnittstellen/202610/pruefi/ORDERS/PI_17121) — Bestellung Änderung · AS4

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
- [Messlokation lesen](/api/202610/backend-lesen/getmeterlocationbasic#messlokation-lesen) `GET /getMeterLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getMeterLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_MESSLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Netzlokation lesen](/api/202610/backend-lesen/getgridlocationbasic#netzlokation-lesen) `GET /getGridLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getGridLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_NETZLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Steuerbare Ressource lesen](/api/202610/backend-lesen/getcontrollableresourcebasic#steuerbare-ressource-lesen) `GET /getControllableResourceBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getControllableResourceBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

</li>

<li data-teil="aperak">

**Aperak-Prüfungen**
- `17130`, `17121` → `Z10`
- `17130`, `17121` → `Z17`
- `17130`, `17121` → `Z18`
- `17130` → `Z33`

</li>

<li data-teil="schnittstelle" data-art="schreiben">

**Schreibende Schnittstelle**
- Vorgang angelegt — [Prozessdaten erstellen](/api/202610/backend-schreiben-msb/createprocessdata#prozessdaten-erstellen) `POST /createProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/createProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "ERSTELLEN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"ANFRAGE\": [\n      {\n        \"anfragekategorie\": \"BESTELLUNG_EINER_KONFIGURATION\",\n        \"boTyp\": \"ANFRAGE\",\n        \"lokationsId\": \"C4897654121\",\n        \"lokationsTyp\": \"STEUERBARE_RESSOURCE\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"AUFTRAG\": [\n      {\n        \"boTyp\": \"AUFTRAG\",\n        \"positionsdaten\": [\n          {\n            \"positionsnummer\": 1\n          }\n        ],\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"SCHALTZEITDEFINITION\": [\n      {\n        \"boTyp\": \"SCHALTZEITDEFINITION\",\n        \"schaltzeiten\": [\n          {\n            \"code\": \"AAL\",\n            \"konfigurationsprodukt\": \"9991000000713\"\n          }\n        ],\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"STEUERBARE_RESSOURCE\": [\n      {\n        \"boTyp\": \"STEUERBARE_RESSOURCE\",\n        \"ressourcenId\": \"C4897654121\",\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"marktrolle\": \"LF\",\n      \"rollencodenummer\": \"9903111000003\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"beteiligterMarktpartner\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9903111000003\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"datenaustauschreferenz\": \"M0OU3NLP\",\n    \"dokumentennummer\": \"M0O1YVAK\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9904629000006\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"nachrichtendatum\": \"2026-10-01T11:00:00Z\",\n    \"nachrichtenreferenznummer\": \"M08MHOSC\",\n    \"pruefidentifikator\": \"17130\",\n    \"sparte\": \"STROM\",\n    \"vorgangsreferenznummer\": \"AS1234\"\n  },\n  \"zusatzdaten\": {}\n}"} examples={[{"mediaType": "application/json", "examples": [{"name": "17130", "summary": "17130 — Bestellung einer Konfiguration", "value": {"stammdaten": {"ANFRAGE": [{"boTyp": "ANFRAGE", "versionStruktur": "1", "anfragekategorie": "BESTELLUNG_EINER_KONFIGURATION", "lokationsId": "C4897654121", "lokationsTyp": "STEUERBARE_RESSOURCE"}], "AUFTRAG": [{"boTyp": "AUFTRAG", "versionStruktur": "1", "positionsdaten": [{"positionsnummer": 1}]}], "STEUERBARE_RESSOURCE": [{"boTyp": "STEUERBARE_RESSOURCE", "versionStruktur": "1", "ressourcenId": "C4897654121"}], "SCHALTZEITDEFINITION": [{"boTyp": "SCHALTZEITDEFINITION", "versionStruktur": "1", "schaltzeiten": [{"code": "AAL", "konfigurationsprodukt": "9991000000713"}]}]}, "transaktionsdaten": {"datenaustauschreferenz": "M0OU3NLP", "sparte": "STROM", "pruefidentifikator": "17130", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "marktrolle": "LF", "rollencodenummer": "9903111000003", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9904629000006", "rollencodetyp": "BDEW"}, "dokumentennummer": "M0O1YVAK", "nachrichtendatum": "2026-10-01T11:00:00Z", "nachrichtenreferenznummer": "M08MHOSC", "vorgangsreferenznummer": "AS1234", "beteiligterMarktpartner": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9903111000003", "rollencodetyp": "BDEW"}}, "zusatzdaten": {}}}, {"name": "17121", "summary": "17121 — Bestellung Änderung", "value": {"stammdaten": {"ANFRAGE": [{"boTyp": "ANFRAGE", "versionStruktur": "1", "anfragekategorie": "AENDERUNG", "energierichtung": "AUSSP", "lokationsId": "44897654121", "lokationsTyp": "MALO"}], "AUFTRAG": [{"boTyp": "AUFTRAG", "versionStruktur": "1", "ausfuehrungsdatum": "2026-09-29T22:00:00Z", "positionsdaten": [{"positionsnummer": 1, "lokationsId": "44897654121", "lokationsTyp": "MALO"}]}], "MARKTLOKATION": [{"boTyp": "MARKTLOKATION", "versionStruktur": "1", "marktlokationsId": "44897654121", "zaehlwerke": [{"messprodukt": "9991000000044", "verwendungszweckNB": "V01", "verwendungszweckLF": "V01", "verwendungszweckUENB": "V15", "zaehlzeiten": {"zaehlzeitDefinition": "Aal"}}]}]}, "transaktionsdaten": {"datenaustauschreferenz": "M0LI678W", "sparte": "STROM", "pruefidentifikator": "17121", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9900259000002", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9904629000006", "rollencodetyp": "BDEW"}, "dokumentennummer": "M05AQP3S", "nachrichtendatum": "2026-10-01T11:00:00Z", "nachrichtenreferenznummer": "M0V0OCVO"}, "zusatzdaten": {}}}]}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Legt im Backend einen neuen Vorgang mit den Daten der eingegangenen Nachricht an.

</li>

<li data-teil="lesen" data-stufe="ebd">

**Daten für die Prüfung laden**
- `LESEN_DEFINITION_LST_KURVEN`
- [Schaltzeitdefinition lesen](/api/202610/backend-lesen/getdefinitionswitch#schaltzeitdefinition-lesen) `GET /getDefinitionSwitch` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getDefinitionSwitch"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": false, "defaultValue": "MALO", "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": false, "defaultValue": "2024-06-28T12:18:00Z", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Zaehlzeitdefinition lesen ](/api/202610/backend-lesen/getdefinitioncounting#zaehlzeitdefinition-lesen) `GET /getDefinitionCounting` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getDefinitionCounting"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": false, "defaultValue": "MALO", "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": false, "defaultValue": "2024-06-28T12:18:00Z", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Messlokation lesen](/api/202610/backend-lesen/getmeterlocationbasic#messlokation-lesen) `GET /getMeterLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getMeterLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_MESSLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Preisblatt lesen](/api/202610/backend-lesen/getpricesheetbasic#preisblatt-lesen) `GET /getPriceSheetBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getPriceSheetBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": false, "defaultValue": "74018657187", "type": "string"}, {"name": "parameter2", "isRequired": false, "defaultValue": "MALO", "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": false, "defaultValue": "2024-06-28T12:18:00Z", "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_PREISBLATT_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Tranche lesen](/api/202610/backend-lesen/gettranchebasic#tranche-lesen) `GET /getTrancheBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getTrancheBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

</li>

<li data-teil="baum">

**Entscheidungsbaum**
- `17130`, `17121` → [E_0526](/referenz/202610/ebd/E_0526) — Bestellung prüfen

</li>

<li data-teil="folgeprozess">

**Folgeprozess auslösen**
- [17118](/schnittstellen/202610/pruefi/ORDERS/PI_17118) — Bestellung einer Konfigurationsänderung
- [19120](/schnittstellen/202610/pruefi/ORDRSP/PI_19120) — Mitteilung zur Änderung
- [19132](/schnittstellen/202610/pruefi/ORDRSP/PI_19132) — Mitteilung zur Bestellung Konfiguration

Nach der Verarbeitung startet die MACO APP den Folgeprozess selbst; welcher davon läuft, hängt vom Ergebnis der Verarbeitung ab.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="5" anker="schritt-5" richtung="ausgehend" kopf={{"links": {"label": "MSB", "eigen": true}, "rechts": {"label": "NB"}}}>

### Mitteilung zum weiteren Vorgehen zur Bestellung

<Schrittskizze sicht={{"label": "MSB"}} zeilen={[{"art": "folge_ausloeser", "werte": ["17121", "17130", "17131"]}, {"art": "senden", "label": "NB", "weg": "AS4", "nachrichten": [{"nr": "19132", "titel": "Mitteilung zur Bestellung Konfiguration"}, {"nr": "19120", "titel": "Mitteilung zur Änderung"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [19132](/schnittstellen/202610/pruefi/ORDRSP/PI_19132) — Mitteilung zur Bestellung Konfiguration · AS4
- [19120](/schnittstellen/202610/pruefi/ORDRSP/PI_19120) — Mitteilung zur Änderung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="folge_ausloeser">

**Ausgelöst durch Eingang**
- [17121](/schnittstellen/202610/pruefi/ORDERS/PI_17121) — Bestellung Änderung
- [17130](/schnittstellen/202610/pruefi/ORDERS/PI_17130) — Bestellung einer Konfiguration
- [17131](/schnittstellen/202610/pruefi/ORDERS/PI_17131) — Bestellung Angebot einer Konfiguration

Die MACO APP sendet diese Nachricht selbst, als Folgeprozess nach einem dieser Eingänge.

</li>

<li data-teil="nachricht">

Nachricht an **NB** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `19132`, `19120` → [E_0526](/referenz/202610/ebd/E_0526) · MSB · Bestellung prüfen

</div>

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

<Schritt nr="6" anker="schritt-6" richtung="ausgehend" kopf={{"links": {"label": "MSB", "eigen": true}, "rechts": {"label": "weiterer MSB"}}}>

### Bestellung einer Konfiguration für weiter betroffene Lokationen

<Schrittskizze sicht={{"label": "MSB"}} zeilen={[{"art": "folge_ausloeser", "werte": ["17121"]}, {"art": "senden", "label": "weiterer MSB", "weg": "AS4", "nachrichten": [{"nr": "17130", "titel": "Bestellung einer Konfiguration"}, {"nr": "17118", "titel": "Bestellung einer Konfigurationsänderung"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [17130](/schnittstellen/202610/pruefi/ORDERS/PI_17130) — Bestellung einer Konfiguration · AS4
- [17118](/schnittstellen/202610/pruefi/ORDERS/PI_17118) — Bestellung einer Konfigurationsänderung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="folge_ausloeser">

**Ausgelöst durch Eingang**
- [17121](/schnittstellen/202610/pruefi/ORDERS/PI_17121) — Bestellung Änderung

Die MACO APP sendet diese Nachricht selbst, als Folgeprozess nach diesem Eingang.

</li>

<li data-teil="nachricht">

Nachricht an **weiterer MSB** · AS4

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202610/backend-schreiben-msb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"ANFRAGE\": [\n      {\n        \"anfragekategorie\": \"BESTELLUNG_EINER_KONFIGURATION\",\n        \"boTyp\": \"ANFRAGE\",\n        \"lokationsId\": \"C4897654121\",\n        \"lokationsTyp\": \"STEUERBARE_RESSOURCE\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"AUFTRAG\": [\n      {\n        \"boTyp\": \"AUFTRAG\",\n        \"positionsdaten\": [\n          {\n            \"positionsnummer\": 1\n          }\n        ],\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"SCHALTZEITDEFINITION\": [\n      {\n        \"boTyp\": \"SCHALTZEITDEFINITION\",\n        \"schaltzeiten\": [\n          {\n            \"code\": \"AAL\",\n            \"konfigurationsprodukt\": \"9991000000713\"\n          }\n        ],\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"STEUERBARE_RESSOURCE\": [\n      {\n        \"boTyp\": \"STEUERBARE_RESSOURCE\",\n        \"ressourcenId\": \"C4897654121\",\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"marktrolle\": \"LF\",\n      \"rollencodenummer\": \"9903111000003\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"beteiligterMarktpartner\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9903111000003\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"datenaustauschreferenz\": \"M0OU3NLP\",\n    \"dokumentennummer\": \"M0O1YVAK\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9904629000006\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"nachrichtendatum\": \"2026-10-01T11:00:00Z\",\n    \"nachrichtenreferenznummer\": \"M08MHOSC\",\n    \"pruefidentifikator\": \"17130\",\n    \"sparte\": \"STROM\",\n    \"vorgangsreferenznummer\": \"AS1234\"\n  },\n  \"zusatzdaten\": {}\n}"} examples={[{"mediaType": "application/json", "examples": [{"name": "17130", "summary": "17130 — Bestellung einer Konfiguration", "value": {"stammdaten": {"ANFRAGE": [{"boTyp": "ANFRAGE", "versionStruktur": "1", "anfragekategorie": "BESTELLUNG_EINER_KONFIGURATION", "lokationsId": "C4897654121", "lokationsTyp": "STEUERBARE_RESSOURCE"}], "AUFTRAG": [{"boTyp": "AUFTRAG", "versionStruktur": "1", "positionsdaten": [{"positionsnummer": 1}]}], "STEUERBARE_RESSOURCE": [{"boTyp": "STEUERBARE_RESSOURCE", "versionStruktur": "1", "ressourcenId": "C4897654121"}], "SCHALTZEITDEFINITION": [{"boTyp": "SCHALTZEITDEFINITION", "versionStruktur": "1", "schaltzeiten": [{"code": "AAL", "konfigurationsprodukt": "9991000000713"}]}]}, "transaktionsdaten": {"datenaustauschreferenz": "M0OU3NLP", "sparte": "STROM", "pruefidentifikator": "17130", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "marktrolle": "LF", "rollencodenummer": "9903111000003", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9904629000006", "rollencodetyp": "BDEW"}, "dokumentennummer": "M0O1YVAK", "nachrichtendatum": "2026-10-01T11:00:00Z", "nachrichtenreferenznummer": "M08MHOSC", "vorgangsreferenznummer": "AS1234", "beteiligterMarktpartner": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9903111000003", "rollencodetyp": "BDEW"}}, "zusatzdaten": {}}}, {"name": "17118", "summary": "17118 — Bestellung einer Konfigurationsänderung", "value": {"stammdaten": {"ANFRAGE": [{"boTyp": "ANFRAGE", "versionStruktur": "1", "anfragekategorie": "AENDERUNG_GERAETEKONFIGURATION", "lokationsId": "DE00014545768S0000000000000003054", "lokationsTyp": "MELO"}], "AUFTRAG": [{"boTyp": "AUFTRAG", "versionStruktur": "1", "ausfuehrungsdatum": "2026-08-29T22:00:00Z", "positionsdaten": [{"lokationsId": "DE00014545768S0000000000000003054", "positionsnummer": 1}]}], "MESSLOKATION": [{"boTyp": "MESSLOKATION", "versionStruktur": "1", "messlokationsId": "DE00014545768S0000000000000003054", "zaehlwerke": [{"messprodukt": "9991000000169", "notwendigkeitZweiteMessung": "NICHT_VORHANDEN", "werteuebermittlungVerwendungszweck": "VORHANDEN", "zaehlzeiten": {"zaehlzeitDefinition": "AAI"}}]}]}, "transaktionsdaten": {"datenaustauschreferenz": "M0JPDOTZ", "sparte": "STROM", "pruefidentifikator": "17118", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9904629000006", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9904629000008", "rollencodetyp": "BDEW"}, "dokumentennummer": "M0DAA51T", "nachrichtendatum": "2026-10-01T11:00:00Z", "nachrichtenreferenznummer": "M0L4YRVR", "beteiligterMarktpartner": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900259000002", "rollencodetyp": "BDEW"}}, "zusatzdaten": {}}}]}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend fort, nachdem die Nachricht erstellt ist.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="7" anker="schritt-7" richtung="eingehend" kopf={{"links": {"label": "MSB", "eigen": true}, "rechts": {"label": "weiterer MSB"}}}>

### Mitteilung zum weiteren Vorgehen zur Bestellung

<Schrittskizze sicht={{"label": "MSB"}} zeilen={[{"art": "empfangen", "label": "weiterer MSB", "weg": "AS4", "nachrichten": [{"nr": "19132", "titel": "Mitteilung zur Bestellung Konfiguration"}, {"nr": "19127", "titel": "Mitteilung zur Konfigurationsänderung"}]}, {"art": "aperak", "werte": ["Z33"]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [19132](/schnittstellen/202610/pruefi/ORDRSP/PI_19132) — Mitteilung zur Bestellung Konfiguration · AS4
- [19127](/schnittstellen/202610/pruefi/ORDRSP/PI_19127) — Mitteilung zur Konfigurationsänderung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **weiterer MSB** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `19132`, `19127` → [E_0527](/referenz/202610/ebd/E_0527) · MSB · Bestellung

</div>

</li>

<li data-teil="aperak">

**Aperak-Prüfungen**
- `19132`, `19127` → `Z33`

</li>

<li data-teil="schnittstelle" data-art="fortschreiben" data-abgeleitet="ja">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202610/backend-schreiben-msb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend mit den Daten der eingegangenen Nachricht fort.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="8" anker="schritt-8" richtung="ausgehend" kopf={{"links": {"label": "MSB", "eigen": true}, "rechts": {"label": "weiterer MSB"}}}>

### Antwort auf Bestellung

<Schrittskizze sicht={{"label": "MSB"}} zeilen={[{"art": "senden", "label": "weiterer MSB", "weg": "AS4", "nachrichten": [{"nr": "21043", "titel": "Bestellungsantwort / -mitteilung"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [21043](/schnittstellen/202610/pruefi/IFTSTA/PI_21043) — Bestellungsantwort / -mitteilung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht an **weiterer MSB** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `21043` → [E_0528](/referenz/202610/ebd/E_0528) · MSB · Umsetzung der Konfiguration prüfen

</div>

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

<Schritt nr="9" anker="schritt-9" richtung="ausgehend" kopf={{"links": {"label": "MSB", "eigen": true}, "rechts": {"label": "NB"}}}>

### Antwort auf Bestellung

<Schrittskizze sicht={{"label": "MSB"}} zeilen={[{"art": "senden", "label": "NB", "weg": "AS4", "nachrichten": [{"nr": "21043", "titel": "Bestellungsantwort / -mitteilung"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [21043](/schnittstellen/202610/pruefi/IFTSTA/PI_21043) — Bestellungsantwort / -mitteilung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht an **NB** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `21043` → [E_0529](/referenz/202610/ebd/E_0529) · MSB · Bewertung des Gesamtvorgangs

</div>

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

<Schritt nr="10" anker="schritt-10" richtung="ausgehend" kopf={{"links": {"label": "MSB", "eigen": true}, "rechts": {"label": "weiterer MSB"}}}>

### Mitteilung über Gesamtvorgang

<Schrittskizze sicht={{"label": "MSB"}} zeilen={[{"art": "senden", "label": "weiterer MSB", "weg": "AS4", "nachrichten": [{"nr": "21043", "titel": "Bestellungsantwort / -mitteilung"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [21043](/schnittstellen/202610/pruefi/IFTSTA/PI_21043) — Bestellungsantwort / -mitteilung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht an **weiterer MSB** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `21043` → [E_0529](/referenz/202610/ebd/E_0529) · MSB · Bewertung des Gesamtvorgangs

</div>

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

<details>
<summary>Entscheidungsbäume dieses Prozesses</summary>

| EBD | Name |
|---|---|
| [E_0524](/referenz/202610/ebd/E_0524) | Anfrage prüfen |
| [E_0526](/referenz/202610/ebd/E_0526) | Bestellung prüfen |
| [E_0527](/referenz/202610/ebd/E_0527) | Bestellung |
| [E_0528](/referenz/202610/ebd/E_0528) | Umsetzung der Konfiguration prüfen |
| [E_0529](/referenz/202610/ebd/E_0529) | Bewertung des Gesamtvorgangs |

</details>

<a id="abschnitt-informationen"></a>

## Prozess-Informationen

Wortlaut der Lesefassung, Steckbrief Kap. 1.3.3.1, S. 42–46.

<Stepper>
<ol>

<li data-blatt="vorbedingungen">

### Vorbedingungen

- Im Fall, dass der Bestellung ein Angebotsprozess vorausgeht:
  - Es handelt sich um eine kostenpflichtige Konfiguration.
  - Die für die Konfiguration relevanten Artikel-ID sind im Preisblatt A des MSB aufgeführt.
  - Der Messstellenbetrieb wird an allen betroffenen Lokationen vom selben MSB durchgeführt; d.h. der MSB der direkt betroffenen Lokation ist der MSB aller ggf. weiter betroffenen Lokationen.
- Im Fall, dass der Bestellung kein Angebotsprozess vorausgeht:
  - Es handelt sich um keine kostenpflichtige Konfiguration. Dies wäre z.B. bei einer Bestellung einer Übermittlung von Werten nach Typ 1 der Fall.
  - Im Fall der Bestellung einer Konfiguration vom LF an den NB: Der NB hat vom LF eine Bestellung der Konfiguration über den Use-Case „[Bestellung einer Konfiguration vom LF an NB](/prozessdoku/202610/LF/GPKE-Teil3-bestellung-einer-konfiguration-vom-lf-an-nb)“ (z.B. die Bestellung einer Änderung des Bilanzierungsverfahrens oder Bestellung einer Konfiguration, für die eine Zählzeitdefinition des NB erforderlich ist) erhalten, bei der die Einrichtung der Konfiguration aus Sicht des NB grundsätzlich möglich ist.
- Die zum bestellten Zeitpunkt vorhandene Gerätetechnik ermöglicht die Einrichtung der Konfiguration. Dies bedeutet z. B. im Fall der Bestellung einer Konfiguration, für die eine Zählzeitdefinition des LF erforderlich ist, dass alle Messlokationen der Marktlokation mit iMS ausgestattet sind.
- Im Fall der Bestellung einer Steuererlaubnis:
  - Die Bestellung ist nur für eine Lokation (Steuerbare Ressource, Netzlokation) möglich.
  - Die Lokation ist mit einem iMS und einer Steuerungseinrichtung, die über das SMGW kommuniziert, ausgestattet.
- Im Fall der Bestellung einer Konfiguration, die die Übermittlung von Werten direkt aus dem iMS an den NB oder LF ermöglicht:
  - Die Bestellung ist nur für eine Lokation möglich.
  - Die Lokation ist mit einem iMS ausgestattet.
- Im Fall der Bestellung einer Konfiguration, für die eine Zählzeitdefinition, Schaltzeitdefinition oder Leistungskurvendefinition erforderlich ist: Die für die Konfiguration relevante Definition (z.B. Zählzeitdefinition des NB) wurde im Rahmen der Use-Cases des Kapitels „Austausch zu Zählzeit-, Schaltzeit-, Leistungskurvendefinitionen“ ausgetauscht.
  - Im Fall der Bestellung einer Konfiguration, für die eine Zählzeitdefinition erforderlich ist: Es handelt sich um eine verbrauchende Marktlokation.

</li>

<li data-blatt="ergebnisse">

### Ergebnisse

- Sofern die Konfiguration für alle betroffenen Lokationen erfolgreich eingerichtet wurde, führt der MSB der jeweils betroffenen Lokation den Use-Case „Stammdatenänderung“ (hier: SD „[Stammdatenänderung vom MSB (verantwortlich) ausgehend](/prozessdoku/202610/MSB/GPKE-Teil4-stammdatenaenderung-vom-msb-verantwortlich-ausgehend)“) (GPKE Teil 4) durch, sofern für die jeweilige Lokation eine Stammdatenänderung aufgrund der Einrichtung der Konfiguration erforderlich ist.
- Im Fall der Bestellung einer Konfiguration vom LF an den NB: Der NB leitet die Bestätigung an den LF weiter.
- Im Fall, dass der Bestellung ein Angebotsprozess vorausgegangen ist: Die Abrechnung der Artikel-ID kann über den Use-Case „Abrechnung Leistungen des Preisblatts A des MSB" vom MSB an den NB bzw. LF erfolgen.

</li>

<li data-blatt="fehlerfall">

### Fehlerfall

#### Ergebnis im Fehlerfall

- Der NB bzw. LF prüft, ob eine erneute Beauftragung der Konfiguration erforderlich ist.
- Im Fall der Bestellung einer Konfiguration vom LF an den NB: Der NB leitet die Ablehnung an den LF weiter.
- Die bisher vorhandene Konfiguration bleibt bestehen. Wurde für eine betroffene Lokation die bestellte Konfiguration bereits eingerichtet, wird für diese Lokation der ursprüngliche Zustand vor der Bestellung wieder hergestellt.

#### Fehlerfälle

- Im Fall, dass der Bestellung ein Angebotsprozess vorausgeht:
  - Es handelt sich um keine kostenpflichtige Konfiguration oder
  - die für die Konfiguration relevanten Artikel-ID sind im Preisblatt A des MSB nicht aufgeführt oder
  - der Messstellenbetrieb wird nicht an allen betroffenen Lokationen vom selben MSB durchgeführt; d.h. der MSB der direkt betroffenen Lokation ist nicht der MSB aller ggf. weiter betroffenen Lokationen.
- Im Fall, dass der Bestellung kein Angebotsprozess vorausgeht: Es handelt sich um eine kostenpflichtige Konfiguration.
- Der Marktpartner ist zum bestellten Beginn des Wirkungszeitraums der betroffenen Lokation nicht zugeordnet.
- Die zum bestellten Zeitpunkt vorhandene Gerätetechnik ermöglicht die Einrichtung der Konfiguration nicht. Dies bedeutet z.B. im Fall der Bestellung einer Konfiguration, für die eine Zählzeitdefinition des LF erforderlich ist: Es sind nicht alle Messlokationen der Marktlokation mit iMS ausgestattet.
- Im Fall der Bestellung einer Steuererlaubnis:
  - In der Bestellung ist mehr als eine Lokation angegeben oder
  - Die Lokation ist nicht mit einem iMS und einer Steuerungseinrichtung, die über das SMGW kommuniziert, ausgestattet.
- Im Fall der Bestellung einer Konfiguration, die die Übermittlung von Werten direkt aus dem iMS an den NB oder LF ermöglicht:
  - In der Bestellung ist mehr als eine Lokation angegeben oder
  - Die Lokation ist nicht mit einem iMS ausgestattet.
- Im Fall der Bestellung einer Konfiguration, für die eine Zählzeitdefinition, Schaltzeitdefinition oder Leistungskurvendefinitionen erforderlich ist: Die für die Konfiguration relevante Definition (z.B. Zählzeitdefinition des NB) wurde im Rahmen der Use-Cases des Kapitels „Austausch zu Zählzeit-, Schaltzeit-, Leistungskurvendefinition“ nicht ausgetauscht.
- Im Fall der Bestellung einer Konfiguration, für die eine Zählzeitdefinition erforderlich ist: Es handelt sich um eine erzeugende Marktlokation bzw. eine Tranche.
- Es liegen nicht alle Parameter oder falsche Parameter für die Einrichtung der Konfiguration vor.

</li>

<li data-blatt="anforderungen">

### Weitere Anforderungen

- Sofern die zum bestellten Zeitpunkt vorhandene Gerätetechnik die Einrichtung der Konfiguration nicht ermöglicht, ist die Änderung der Gerätetechnik nicht über diesen Use-Case zu bestellen. Eine entsprechende Änderung der Gerätetechnik kann im Rahmen eines Gerätewechsels bzw. über die Use-Cases zur Messlokationsänderung (WiM Teil 1) beauftragt werden.
- Der LF kann über diesen Use-Case auch eine Bestellung einer Konfiguration an den zukünftigen MSB übermitteln.
- Konfigurationen des NB werden im Use-Case „[Beginn Messstellenbetrieb](/prozessdoku/202610/LF/WiM-Teil1-beginn-messstellenbetrieb)“ (WiM Teil 1) in Prozessschritt 2 im Rahmen der Mindestparameter für die Messlokation(en) vom NB dem MSB mitgeteilt. Eine Bestellung einer in den Mindestparametern enthaltenen Konfiguration ist nicht über den hier beschriebenen Use-Case notwendig. Ergänzend zu den in den Mindestparametern mitgeteilten Konfigurationen, kann der NB mit Hilfe des hier beschriebenen Use-Cases eine Bestellung einer Konfiguration an den zukünftigen MSB übermitteln. Hinweis: Wird dem MSB im Rahmen der Mindestparameter im Use-Case „[Beginn Messstellenbetrieb](/prozessdoku/202610/LF/WiM-Teil1-beginn-messstellenbetrieb)“ (WiM Teil 1) eine Zählzeitdefinition des NB mitgeteilt, die der MSB vorab nicht über den Use-Case „[Übermittlung einer Definition des NB durch den NB](/prozessdoku/202610/MSB/GPKE-Teil3-uebermittlung-einer-definition-des-nb-durch-den-nb)“ übermittelt bekommen hat, so ist die Energie in einem Register an der/den Messlokation(en) und der zugehörigen Marktlokation für den Zählzeitenanwendungszweck „Netznutzung“ zu erfassen.

</li>

<li data-blatt="anlass">

### Anlass

- Der NB hat den Bedarf eine Konfiguration einrichten zu lassen bzw.
- Der LF hat den Bedarf eine Konfiguration einrichten zu lassen, die der LF direkt beim MSB und nicht über den NB zu bestellen hat. Dies kann z.B. sein:
- Im Fall der Bestellung einer Konfiguration, für die eine Zählzeitdefinition des NB erforderlich ist: Der NB möchte für den Zählzeitenanwendungszweck „Netznutzung“ die bisher vorhandene Konfiguration einer Marktlokation und deren zugehörigen Messlokationen ändern.
- Im Fall der Bestellung einer Konfiguration, für die eine Zählzeitdefinition des LF erforderlich ist: Der LF möchte in der Bestellung mitteilen,
  - dass er eine zur bisher vorhandenen Konfiguration mit dem Zählzeitenanwendungszweck „Netznutzung“ abweichende Zählzeitdefinition des LF mit dem Zählzeitenanwendungszweck „Endkunde“ bestellen möchte oder
  - dass er die bisher vorhandene Konfiguration für den Zählzeitenanwendungszweck „Endkunde“ auf eine andere Zählzeitdefinition des LF ändern möchte.

</li>

<li data-blatt="erste-nachricht">

### Erste Nachricht

**NB** sendet „Anfrage einer Konfiguration auf Ebene der direkt betroffenen Lokation“ (Schritt 1). Ab hier ist der Beteiligte dieser Seite am Zug.

</li>

<li data-blatt="ziel">

### Ziel

Die Bestellung der Konfiguration (z.B. Messprodukt, Steuererlaubnis) für die betroffenen Lokationen (z.B. Messlokation, Marktlokation, Steuerbare Ressource, Netzlokation) wurde vom MSB der direkt betroffenen Lokation bestätigt.

</li>

</ol>
</Stepper>

<a id="abschnitt-sichten"></a>

## Andere Sichten des Prozesses

Derselbe Prozess, aus den Augen der anderen Beteiligten: dieselben Schritte, jeweils aus deren Sicht gelesen.

- [Sicht WMSB](/prozessdoku/202610/MSB--WMSB/GPKE-Teil3-bestellung-einer-konfiguration-vom-nb-an-msb) — weiterer Messstellenbetreiber · Marktrolle MSB
- [Sicht NB](/prozessdoku/202610/NB/GPKE-Teil3-bestellung-einer-konfiguration-vom-nb-an-msb) — NB

<Hinweisbereich>

*Die Schritte sind die **möglichen** Nachrichten dieses Prozesses, keine Abfolge — die Quelle führt weder Bedingungen noch Alternativen. Das Kästchen am Schritt nennt links die eigene Sicht: **←** empfängt sie, **→** sendet sie. Zugeklappte Schritte laufen zwischen anderen Marktpartnern.*

Diese Lesezugriffe sind im API-Katalog dieser Formatversion nicht geführt; am Schritt steht deshalb nur ihr Kommando, ohne Adresse und ohne Knopf.

Betrifft: [1](#schritt-1), [3](#schritt-3), [4](#schritt-4)

Die Konnektortabelle führt für diese Schritte keinen Schreibaufruf. Abgeleitet aus dem Prozessverlauf: Die eigene Rolle war an diesem Prozess schon beteiligt, der Vorgang besteht also.

Betrifft: [7](#schritt-7)

Zu den Prüfidentifikatoren dieser Schritte liegt kein Testfall im Testbestand; der Knopf »Ausprobieren« der schreibenden Schnittstelle bietet deshalb keinen Rumpf an.

Betrifft: [5](#schritt-5), [7](#schritt-7), [8](#schritt-8), [9](#schritt-9), [10](#schritt-10)

</Hinweisbereich>
