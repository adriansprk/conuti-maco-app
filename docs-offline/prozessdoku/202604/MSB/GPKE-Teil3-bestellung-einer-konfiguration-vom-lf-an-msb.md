# Bestellung einer Konfiguration vom LF an MSB — Sicht MSB

<Kopf rolle="MSB" beteiligter="MSB" festlegung="GPKE" dokument="GPKE Teil 3" kapitel="1.3.3.3" sparte="Strom" schritte={10} suchtitel="Bestellung einer Konfiguration vom LF an MSB — Sicht MSB · GPKE Teil 3 · Formatversion 202604" abschnitte={[{"id": "abschnitt-ablauf", "label": "Prozessablauf"}, {"id": "abschnitt-schritte", "label": "Prozessschritte"}, {"id": "abschnitt-informationen", "label": "Prozess-Informationen"}, {"id": "abschnitt-sichten", "label": "Andere Sichten des Prozesses"}]} />

<Kurzfassung>

Der NB bzw. LF bestellt beim MSB der direkt betroffenen Lokation eine Konfiguration für die direkt betroffene Lokation. Sofern weitere Lokationen der direkt betroffenen Lokation von der Konfiguration betroffen sind, gibt der NB bzw. LF diese weiter betroffenen Lokationen in der Bestellung ebenfalls an (z.B. hat der NB in der Bestellung der Änderung des Bilanzierungsverfahrens auf der Ebene der Marktlokation, neben der Marktlokation auch alle Messlokationen der Marktlokation beim MSB der Marktlokation zu bestellen). Bevor eine kostenpflichtige Bestellung erfolgen kann, hat der NB bzw. LF ein Angebot beim MSB der direkt betroffenen Lokation für die Einrichtung der Konfiguration anzufragen. Der MSB prüft die Bestellung und teilt dem NB bzw. LF das weitere Vorgehen zur Bestellung mit. Sofern weitere Lokationen der direkt betroffenen Lokation von der Konfiguration betroffen sind, für die der MSB der direkt betroffenen Lokation nicht den Messstellenbetrieb durchführt, bindet er für diese weiter betroffenen Lokationen die jeweiligen weiteren MSB ein.

</Kurzfassung>

<a id="abschnitt-ablauf"></a>

## Prozessablauf aus Sicht des MSB

<Systembild svg={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1004 2969\" width=\"1004\" height=\"2969\" role=\"img\" aria-labelledby=\"sb-title\" class=\"maco-systembild\">\n<title id=\"sb-title\">Systembild: Bestellung einer Konfiguration vom LF an MSB aus Sicht MSB</title>\n<defs><marker id=\"sb-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect class=\"sb-lane-kopf\" x=\"16\" y=\"12\" width=\"232\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend-System des Kunden</text>\n<rect class=\"sb-lane-kopf\" x=\"398\" y=\"12\" width=\"264\" height=\"46\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · MSB</text>\n<rect class=\"sb-lane-kopf\" x=\"812\" y=\"12\" width=\"176\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"900\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Marktpartner</text>\n<line x1=\"323\" y1=\"58\" x2=\"323\" y2=\"2957\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"737\" y1=\"58\" x2=\"737\" y2=\"2957\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"80\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">1. Anfrage einer</text>\n<text x=\"530\" y=\"115\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Konfiguration auf Ebene der</text>\n<text x=\"530\" y=\"130\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">direkt betroffene…</text>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"93\" r=\"5\"/><line x1=\"900\" y1=\"98\" x2=\"900\" y2=\"110\"/><line x1=\"893\" y1=\"102\" x2=\"907\" y2=\"102\"/><line x1=\"900\" y1=\"110\" x2=\"894\" y2=\"120\"/><line x1=\"900\" y1=\"110\" x2=\"906\" y2=\"120\"/></g>\n<text x=\"900\" y=\"142\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">LF</text>\n<line x1=\"878\" y1=\"111\" x2=\"628\" y2=\"111\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"103\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"127\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">35004</text>\n<rect class=\"sb-kasten sb-aperak_lesen\" x=\"432\" y=\"169\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"189\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Daten für die</text>\n<text x=\"530\" y=\"204\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Eingangsprüfung laden</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"143\" x2=\"530\" y2=\"169\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-aperak_lesen\" x=\"34\" y=\"169\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"189\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">4 Lese-Schnittstellen</text>\n<text x=\"132\" y=\"204\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">aufgerufen</text>\n<line x1=\"432\" y1=\"193\" x2=\"230\" y2=\"193\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"185\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<text x=\"331\" y=\"209\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">je einzeln am Schritt</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"243\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"263\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z10</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"217\" x2=\"530\" y2=\"243\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-schreiben\" x=\"432\" y=\"307\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"327\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"276\" x2=\"530\" y2=\"307\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-schreiben\" x=\"34\" y=\"307\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"327\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten erstellen</text>\n<line x1=\"432\" y1=\"323\" x2=\"230\" y2=\"323\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"315\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-lesen\" x=\"432\" y=\"371\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"391\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Daten für die Prüfung laden</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"340\" x2=\"530\" y2=\"371\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-lesen\" x=\"34\" y=\"363\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"383\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">4 Lese-Schnittstellen</text>\n<text x=\"132\" y=\"398\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">aufgerufen</text>\n<line x1=\"432\" y1=\"387\" x2=\"230\" y2=\"387\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"379\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<text x=\"331\" y=\"403\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">je einzeln am Schritt</text>\n<rect class=\"sb-kasten sb-ebd\" x=\"432\" y=\"445\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"465\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">EBD prüfen: E_0524</text>\n<text x=\"530\" y=\"480\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label-2, #424245)\">Anfrage prüfen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"404\" x2=\"530\" y2=\"445\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-folgeprozess\" x=\"432\" y=\"519\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"539\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Folgeprozess auslösen:</text>\n<text x=\"530\" y=\"554\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">15004, 21033</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"493\" x2=\"530\" y2=\"519\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-folge_ausloeser\" x=\"432\" y=\"593\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"613\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Ausgelöst durch Eingang:</text>\n<text x=\"530\" y=\"628\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">35004</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"567\" x2=\"530\" y2=\"593\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"667\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"687\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">2. Angebot zur / Ablehnung</text>\n<text x=\"530\" y=\"702\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">der Anfrage</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"641\" x2=\"530\" y2=\"667\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"673\" r=\"5\"/><line x1=\"900\" y1=\"678\" x2=\"900\" y2=\"690\"/><line x1=\"893\" y1=\"682\" x2=\"907\" y2=\"682\"/><line x1=\"900\" y1=\"690\" x2=\"894\" y2=\"700\"/><line x1=\"900\" y1=\"690\" x2=\"906\" y2=\"700\"/></g>\n<text x=\"900\" y=\"722\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">LF</text>\n<line x1=\"628\" y1=\"691\" x2=\"878\" y2=\"691\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"683\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"707\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">15004, 21033</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"750\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"770\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"715\" x2=\"530\" y2=\"750\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"750\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"770\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"766\" x2=\"230\" y2=\"766\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"758\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"814\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"834\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">3. Bestellung einer</text>\n<text x=\"530\" y=\"849\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Konfiguration auf Ebene der</text>\n<text x=\"530\" y=\"864\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">direkt betroff…</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"783\" x2=\"530\" y2=\"814\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"827\" r=\"5\"/><line x1=\"900\" y1=\"832\" x2=\"900\" y2=\"844\"/><line x1=\"893\" y1=\"836\" x2=\"907\" y2=\"836\"/><line x1=\"900\" y1=\"844\" x2=\"894\" y2=\"854\"/><line x1=\"900\" y1=\"844\" x2=\"906\" y2=\"854\"/></g>\n<text x=\"900\" y=\"876\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">LF</text>\n<line x1=\"878\" y1=\"845\" x2=\"628\" y2=\"845\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"837\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"861\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">17131</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"903\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"923\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z33</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"877\" x2=\"530\" y2=\"903\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"967\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"987\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"936\" x2=\"530\" y2=\"967\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"967\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"987\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"983\" x2=\"230\" y2=\"983\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"975\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-lesen\" x=\"432\" y=\"1031\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1051\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Daten für die Prüfung laden</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1000\" x2=\"530\" y2=\"1031\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-lesen\" x=\"34\" y=\"1023\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"1043\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">9 Lese-Schnittstellen</text>\n<text x=\"132\" y=\"1058\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">aufgerufen</text>\n<line x1=\"432\" y1=\"1047\" x2=\"230\" y2=\"1047\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"1039\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<text x=\"331\" y=\"1063\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">je einzeln am Schritt</text>\n<rect class=\"sb-kasten sb-ebd\" x=\"432\" y=\"1105\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1125\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">EBD prüfen: E_0526</text>\n<text x=\"530\" y=\"1140\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label-2, #424245)\">Bestellung prüfen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1064\" x2=\"530\" y2=\"1105\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-folgeprozess\" x=\"432\" y=\"1179\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1199\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Folgeprozess auslösen:</text>\n<text x=\"530\" y=\"1214\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">19132</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1153\" x2=\"530\" y2=\"1179\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"1253\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1273\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">4. Bestellung einer</text>\n<text x=\"530\" y=\"1288\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Konfiguration auf Ebene der</text>\n<text x=\"530\" y=\"1303\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">direkt betroff…</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1227\" x2=\"530\" y2=\"1253\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"1266\" r=\"5\"/><line x1=\"900\" y1=\"1271\" x2=\"900\" y2=\"1283\"/><line x1=\"893\" y1=\"1275\" x2=\"907\" y2=\"1275\"/><line x1=\"900\" y1=\"1283\" x2=\"894\" y2=\"1293\"/><line x1=\"900\" y1=\"1283\" x2=\"906\" y2=\"1293\"/></g>\n<text x=\"900\" y=\"1315\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">LF</text>\n<line x1=\"878\" y1=\"1284\" x2=\"628\" y2=\"1284\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"1276\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"1300\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">17130, 17123</text>\n<rect class=\"sb-kasten sb-aperak_lesen\" x=\"432\" y=\"1342\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1362\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Daten für die</text>\n<text x=\"530\" y=\"1377\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Eingangsprüfung laden</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1316\" x2=\"530\" y2=\"1342\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-aperak_lesen\" x=\"34\" y=\"1342\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"1362\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">4 Lese-Schnittstellen</text>\n<text x=\"132\" y=\"1377\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">aufgerufen</text>\n<line x1=\"432\" y1=\"1366\" x2=\"230\" y2=\"1366\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"1358\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<text x=\"331\" y=\"1382\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">je einzeln am Schritt</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"1416\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1436\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z10, Z33</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1390\" x2=\"530\" y2=\"1416\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-schreiben\" x=\"432\" y=\"1480\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1500\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1449\" x2=\"530\" y2=\"1480\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-schreiben\" x=\"34\" y=\"1480\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"1500\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten erstellen</text>\n<line x1=\"432\" y1=\"1496\" x2=\"230\" y2=\"1496\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"1488\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<text x=\"331\" y=\"1512\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">PI 17130</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"1544\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1564\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1513\" x2=\"530\" y2=\"1544\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben sb-abgeleitet\" x=\"34\" y=\"1544\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"1564\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"1560\" x2=\"230\" y2=\"1560\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"1552\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<text x=\"331\" y=\"1576\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">PI 17123</text>\n<rect class=\"sb-kasten sb-lesen\" x=\"432\" y=\"1608\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1628\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Daten für die Prüfung laden</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1577\" x2=\"530\" y2=\"1608\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-lesen\" x=\"34\" y=\"1600\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"1620\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">4 Lese-Schnittstellen</text>\n<text x=\"132\" y=\"1635\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">aufgerufen</text>\n<line x1=\"432\" y1=\"1624\" x2=\"230\" y2=\"1624\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"1616\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<text x=\"331\" y=\"1640\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">je einzeln am Schritt</text>\n<rect class=\"sb-kasten sb-ebd\" x=\"432\" y=\"1682\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1702\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">EBD prüfen: E_0526, E_0533</text>\n<text x=\"530\" y=\"1717\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label-2, #424245)\">E_0526 — Bestellung prüfen</text>\n<text x=\"530\" y=\"1732\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label-2, #424245)\">E_0533 — Bestellung prüfen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1641\" x2=\"530\" y2=\"1682\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-folgeprozess\" x=\"432\" y=\"1771\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1791\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Folgeprozess auslösen:</text>\n<text x=\"530\" y=\"1806\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">19132</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1745\" x2=\"530\" y2=\"1771\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-folge_ausloeser\" x=\"432\" y=\"1845\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1865\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Ausgelöst durch Eingang:</text>\n<text x=\"530\" y=\"1880\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">17130, 17131</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1819\" x2=\"530\" y2=\"1845\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"1919\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1939\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">5. Mitteilung zum weiteren</text>\n<text x=\"530\" y=\"1954\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgehen zur Bestellung</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1893\" x2=\"530\" y2=\"1919\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"1925\" r=\"5\"/><line x1=\"900\" y1=\"1930\" x2=\"900\" y2=\"1942\"/><line x1=\"893\" y1=\"1934\" x2=\"907\" y2=\"1934\"/><line x1=\"900\" y1=\"1942\" x2=\"894\" y2=\"1952\"/><line x1=\"900\" y1=\"1942\" x2=\"906\" y2=\"1952\"/></g>\n<text x=\"900\" y=\"1974\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">LF</text>\n<line x1=\"628\" y1=\"1943\" x2=\"878\" y2=\"1943\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"1935\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"1959\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">19132, 19124</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"2002\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"2022\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1967\" x2=\"530\" y2=\"2002\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"2002\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"2022\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"2018\" x2=\"230\" y2=\"2018\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"2010\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-folge_ausloeser\" x=\"432\" y=\"2066\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"2086\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Ausgelöst durch Eingang:</text>\n<text x=\"530\" y=\"2101\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">17121</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"2035\" x2=\"530\" y2=\"2066\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"2140\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"2160\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">6. Bestellung einer</text>\n<text x=\"530\" y=\"2175\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Konfiguration für weiter</text>\n<text x=\"530\" y=\"2190\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">betroffene Lokati…</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"2114\" x2=\"530\" y2=\"2140\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"2153\" r=\"5\"/><line x1=\"900\" y1=\"2158\" x2=\"900\" y2=\"2170\"/><line x1=\"893\" y1=\"2162\" x2=\"907\" y2=\"2162\"/><line x1=\"900\" y1=\"2170\" x2=\"894\" y2=\"2180\"/><line x1=\"900\" y1=\"2170\" x2=\"906\" y2=\"2180\"/></g>\n<text x=\"900\" y=\"2202\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">weiterer MSB</text>\n<line x1=\"628\" y1=\"2171\" x2=\"878\" y2=\"2171\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"2163\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"2187\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">17130, 17118</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"2229\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"2249\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"2203\" x2=\"530\" y2=\"2229\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"2229\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"2249\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"2245\" x2=\"230\" y2=\"2245\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"2237\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"2293\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"2313\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">7. Mitteilung zum weiteren</text>\n<text x=\"530\" y=\"2328\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgehen zur Bestellung</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"2262\" x2=\"530\" y2=\"2293\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"2299\" r=\"5\"/><line x1=\"900\" y1=\"2304\" x2=\"900\" y2=\"2316\"/><line x1=\"893\" y1=\"2308\" x2=\"907\" y2=\"2308\"/><line x1=\"900\" y1=\"2316\" x2=\"894\" y2=\"2326\"/><line x1=\"900\" y1=\"2316\" x2=\"906\" y2=\"2326\"/></g>\n<text x=\"900\" y=\"2348\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">weiterer MSB</text>\n<line x1=\"878\" y1=\"2317\" x2=\"628\" y2=\"2317\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"2309\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"2333\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">19132, 19127</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"2376\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"2396\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"2341\" x2=\"530\" y2=\"2376\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben sb-abgeleitet\" x=\"34\" y=\"2376\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"2396\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"2392\" x2=\"230\" y2=\"2392\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"2384\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"2440\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"2460\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">8. Antwort auf Bestellung</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"2409\" x2=\"530\" y2=\"2440\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"2438\" r=\"5\"/><line x1=\"900\" y1=\"2443\" x2=\"900\" y2=\"2455\"/><line x1=\"893\" y1=\"2447\" x2=\"907\" y2=\"2447\"/><line x1=\"900\" y1=\"2455\" x2=\"894\" y2=\"2465\"/><line x1=\"900\" y1=\"2455\" x2=\"906\" y2=\"2465\"/></g>\n<text x=\"900\" y=\"2487\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">weiterer MSB</text>\n<line x1=\"878\" y1=\"2456\" x2=\"628\" y2=\"2456\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"2448\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"2472\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">21043</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"2523\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"2543\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z33</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"2473\" x2=\"530\" y2=\"2523\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"2587\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"2607\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"2556\" x2=\"530\" y2=\"2587\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben sb-abgeleitet\" x=\"34\" y=\"2587\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"2607\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"2603\" x2=\"230\" y2=\"2603\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"2595\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"2651\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"2671\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">9. Antwort auf Bestellung</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"2620\" x2=\"530\" y2=\"2651\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"2649\" r=\"5\"/><line x1=\"900\" y1=\"2654\" x2=\"900\" y2=\"2666\"/><line x1=\"893\" y1=\"2658\" x2=\"907\" y2=\"2658\"/><line x1=\"900\" y1=\"2666\" x2=\"894\" y2=\"2676\"/><line x1=\"900\" y1=\"2666\" x2=\"906\" y2=\"2676\"/></g>\n<text x=\"900\" y=\"2698\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">LF</text>\n<line x1=\"628\" y1=\"2667\" x2=\"878\" y2=\"2667\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"2659\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"2683\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">21043</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"2734\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"2754\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"2684\" x2=\"530\" y2=\"2734\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"2734\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"2754\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"2750\" x2=\"230\" y2=\"2750\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"2742\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"2798\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"2818\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">10. Mitteilung über</text>\n<text x=\"530\" y=\"2833\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Gesamtvorgang</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"2767\" x2=\"530\" y2=\"2798\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"2804\" r=\"5\"/><line x1=\"900\" y1=\"2809\" x2=\"900\" y2=\"2821\"/><line x1=\"893\" y1=\"2813\" x2=\"907\" y2=\"2813\"/><line x1=\"900\" y1=\"2821\" x2=\"894\" y2=\"2831\"/><line x1=\"900\" y1=\"2821\" x2=\"906\" y2=\"2831\"/></g>\n<text x=\"900\" y=\"2853\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">weiterer MSB</text>\n<line x1=\"628\" y1=\"2822\" x2=\"878\" y2=\"2822\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"2814\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"2838\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">21043</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"2881\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"2901\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"2846\" x2=\"530\" y2=\"2881\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"2881\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"2901\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"2897\" x2=\"230\" y2=\"2897\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"2889\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n</svg>"} gesamt={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 974 1416\" width=\"974\" height=\"1416\" role=\"img\" aria-labelledby=\"sd-title\" class=\"maco-sequence\">\n<title id=\"sd-title\">Sequenzdiagramm: Bestellung einer Konfiguration vom LF an MSB aus Sicht MSB</title>\n<defs><marker id=\"sd-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect x=\"16\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"121\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend (Kunde)</text>\n<line x1=\"121\" y1=\"64\" x2=\"121\" y2=\"1404\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"260\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"365\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · MSB</text>\n<line x1=\"365\" y1=\"64\" x2=\"365\" y2=\"1404\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"504\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"609\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">LF</text>\n<line x1=\"609\" y1=\"64\" x2=\"609\" y2=\"1404\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"748\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"853\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">weiterer MSB</text>\n<line x1=\"853\" y1=\"64\" x2=\"853\" y2=\"1404\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"609\" y1=\"90\" x2=\"365\" y2=\"90\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"81\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">1. Anfrage einer Konfiguration auf Ebene der dir…</text>\n<text x=\"487\" y=\"105\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 35004</text>\n<line x1=\"365\" y1=\"152\" x2=\"121\" y2=\"152\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"143\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<text x=\"243\" y=\"167\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten erstellen</text>\n<line x1=\"365\" y1=\"214\" x2=\"609\" y2=\"214\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"205\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">2. Angebot zur / Ablehnung der Anfrage</text>\n<text x=\"487\" y=\"229\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 15004, 21033 · E_0531</text>\n<text x=\"487\" y=\"242\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0531 — Anfrage prüfen</text>\n<line x1=\"365\" y1=\"276\" x2=\"121\" y2=\"276\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"267\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"291\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"609\" y1=\"338\" x2=\"365\" y2=\"338\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"329\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">3. Bestellung einer Konfiguration auf Ebene der…</text>\n<text x=\"487\" y=\"353\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 17131</text>\n<line x1=\"365\" y1=\"400\" x2=\"121\" y2=\"400\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"391\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"415\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"609\" y1=\"462\" x2=\"365\" y2=\"462\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"453\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">4. Bestellung einer Konfiguration auf Ebene der…</text>\n<text x=\"487\" y=\"477\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 17130, 17123</text>\n<line x1=\"365\" y1=\"524\" x2=\"121\" y2=\"524\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"515\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<text x=\"243\" y=\"539\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten erstellen · PI 17130</text>\n<line x1=\"365\" y1=\"586\" x2=\"121\" y2=\"586\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"577\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"601\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren · PI 17123</text>\n<line x1=\"365\" y1=\"648\" x2=\"609\" y2=\"648\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"639\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">5. Mitteilung zum weiteren Vorgehen zur Bestellu…</text>\n<text x=\"487\" y=\"663\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 19132, 19124 · E_0533</text>\n<text x=\"487\" y=\"676\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0533 — Bestellung prüfen</text>\n<line x1=\"365\" y1=\"710\" x2=\"121\" y2=\"710\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"701\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"725\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"365\" y1=\"772\" x2=\"853\" y2=\"772\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"609\" y=\"763\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">6. Bestellung einer Konfiguration für weiter bet…</text>\n<text x=\"609\" y=\"787\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 17130, 17118</text>\n<line x1=\"365\" y1=\"834\" x2=\"121\" y2=\"834\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"825\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"849\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"853\" y1=\"896\" x2=\"365\" y2=\"896\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"609\" y=\"887\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">7. Mitteilung zum weiteren Vorgehen zur Bestellu…</text>\n<text x=\"609\" y=\"911\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 19132, 19127 · E_0527</text>\n<text x=\"609\" y=\"924\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0527 — Bestellung</text>\n<line x1=\"365\" y1=\"958\" x2=\"121\" y2=\"958\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"949\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"973\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"853\" y1=\"1020\" x2=\"365\" y2=\"1020\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"609\" y=\"1011\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">8. Antwort auf Bestellung</text>\n<text x=\"609\" y=\"1035\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 21043 · E_0535</text>\n<text x=\"609\" y=\"1048\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0535 — Umsetzung der Konfiguration prüfen</text>\n<line x1=\"365\" y1=\"1082\" x2=\"121\" y2=\"1082\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"1073\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"1097\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"365\" y1=\"1144\" x2=\"609\" y2=\"1144\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"1135\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">9. Antwort auf Bestellung</text>\n<text x=\"487\" y=\"1159\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 21043 · E_0536</text>\n<text x=\"487\" y=\"1172\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0536 — Bewertung des Gesamtvorgangs</text>\n<line x1=\"365\" y1=\"1206\" x2=\"121\" y2=\"1206\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"1197\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"1221\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"365\" y1=\"1268\" x2=\"853\" y2=\"1268\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"609\" y=\"1259\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">10. Mitteilung über Gesamtvorgang</text>\n<text x=\"609\" y=\"1283\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 21043 · E_0536</text>\n<text x=\"609\" y=\"1296\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0536 — Bewertung des Gesamtvorgangs</text>\n<line x1=\"365\" y1=\"1330\" x2=\"121\" y2=\"1330\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"1321\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"1345\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n</svg>"} titel="MSB" />

<a id="abschnitt-schritte"></a>

## Prozessschritte

<Schritt nr="1" anker="schritt-1" richtung="eingehend" kopf={{"links": {"label": "MSB", "eigen": true}, "rechts": {"label": "LF"}}}>

### Anfrage einer Konfiguration auf Ebene der direkt betroffenen Lokation

<Schrittskizze sicht={{"label": "MSB"}} zeilen={[{"art": "empfangen", "label": "LF", "weg": "AS4", "nachrichten": [{"nr": "35004", "titel": "Anfrage einer Konfiguration"}]}, {"art": "lesen_aperak", "schnittstellen": [{"label": "Marktlokation lesen"}, {"label": "Messlokation lesen"}, {"label": "Netzlokation lesen"}, {"label": "Steuerbare Ressource lesen"}]}, {"art": "aperak", "werte": ["Z10"]}, {"art": "erstellen"}, {"art": "lesen_ebd", "schnittstellen": [{"label": "Messlokation lesen"}, {"label": "Netzlokation lesen"}, {"label": "Preisblatt lesen"}, {"label": "LESEN_STEUERBARE_RESOURCE_BASIS"}]}, {"art": "ebd", "baeume": [{"code": "E_0524", "titel": "Anfrage prüfen"}]}, {"art": "folgeprozess", "werte": ["15004", "21033"]}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [35004](/schnittstellen/202604/pruefi/REQOTE/PI_35004) — Anfrage einer Konfiguration · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **LF** · AS4

</li>

<li data-teil="lesen" data-stufe="aperak">

**Daten für die Eingangsprüfung laden**
- [Marktlokation lesen](/api/202604/backend-lesen/getmarketlocationbasic#marktlokation-lesen) `GET /getMarketLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getMarketLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": false, "defaultValue": "MALO", "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": false, "defaultValue": "2024-06-28T12:18:00Z", "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_MARKTLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Messlokation lesen](/api/202604/backend-lesen/getmeterlocationbasic#messlokation-lesen) `GET /getMeterLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getMeterLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_MESSLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Netzlokation lesen](/api/202604/backend-lesen/getgridlocationbasic#netzlokation-lesen) `GET /getGridLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getGridLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_NETZLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Steuerbare Ressource lesen](/api/202604/backend-lesen/getcontrollableresourcebasic#steuerbare-ressource-lesen) `GET /getControllableResourceBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getControllableResourceBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

</li>

<li data-teil="aperak">

**Aperak-Prüfungen**
- `35004` → `Z10`

</li>

<li data-teil="schnittstelle" data-art="schreiben">

**Schreibende Schnittstelle**
- Vorgang angelegt — [Prozessdaten erstellen](/api/202604/backend-schreiben-msb/createprocessdata#prozessdaten-erstellen) `POST /createProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/createProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "ERSTELLEN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"ANFRAGE\": [\n      {\n        \"anfragetyp\": \"AENDERUNG_KONFIGURATION\",\n        \"boTyp\": \"ANFRAGE\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"LEISTUNGSKURVENDEFINITION\": [\n      {\n        \"boTyp\": \"LEISTUNGSKURVENDEFINITION\",\n        \"leistungskurven\": [\n          {\n            \"code\": \"MMA\",\n            \"konfigurationsprodukt\": \"9991000000721\"\n          }\n        ],\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"MARKTLOKATION\": [\n      {\n        \"boTyp\": \"MARKTLOKATION\",\n        \"marktlokationsId\": \"50444001616\",\n        \"marktlokationsTyp\": [\n          {\n            \"typ\": \"STANDARD_MARKTLOKATION\"\n          }\n        ],\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"ansprechpartner\": {\n        \"boTyp\": \"ANSPRECHPARTNER\",\n        \"eMailAdresse\": \"Max.Mustermann@conuti.de\",\n        \"nachname\": \"Max Mustermann\",\n        \"versionStruktur\": \"1\"\n      },\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9900496000001\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"datenaustauschreferenz\": \"M3VQCXCY\",\n    \"dokumentennummer\": \"BGMM3TJAKY3\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9900496000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"Z82\",\n    \"lieferdatum\": \"2025-01-05T23:00:00Z\",\n    \"nachrichtenReferenzBestellbestaetigung\": \"BGMM44X6WGM\",\n    \"nachrichtendatum\": \"2024-10-16T09:45:00Z\",\n    \"nachrichtenreferenznummer\": \"UNHM3Q4M8YM\",\n    \"positionsnummer\": 1,\n    \"pruefidentifikator\": \"35004\",\n    \"sparte\": \"STROM\",\n    \"vorgangsReferenzBestellbestaetigung\": \"45261\"\n  },\n  \"zusatzdaten\": {}\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Legt im Backend einen neuen Vorgang mit den Daten der eingegangenen Nachricht an.

</li>

<li data-teil="lesen" data-stufe="ebd">

**Daten für die Prüfung laden**
- [Messlokation lesen](/api/202604/backend-lesen/getmeterlocationbasic#messlokation-lesen) `GET /getMeterLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getMeterLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_MESSLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Netzlokation lesen](/api/202604/backend-lesen/getgridlocationbasic#netzlokation-lesen) `GET /getGridLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getGridLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_NETZLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Preisblatt lesen](/api/202604/backend-lesen/getpricesheetbasic#preisblatt-lesen) `GET /getPriceSheetBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getPriceSheetBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": false, "defaultValue": "74018657187", "type": "string"}, {"name": "parameter2", "isRequired": false, "defaultValue": "MALO", "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": false, "defaultValue": "2024-06-28T12:18:00Z", "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_PREISBLATT_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- `LESEN_STEUERBARE_RESOURCE_BASIS`

</li>

<li data-teil="baum">

**Entscheidungsbaum**
- `35004` → [E_0524](/referenz/202604/ebd/E_0524) — Anfrage prüfen

</li>

<li data-teil="folgeprozess">

**Folgeprozess auslösen**
- [15004](/schnittstellen/202604/pruefi/QUOTES/PI_15004) — Angebot  einer Konfiguration
- [21033](/schnittstellen/202604/pruefi/IFTSTA/PI_21033) — Ablehnung der Anfrage

Nach der Verarbeitung startet die MACO APP den Folgeprozess selbst; welcher davon läuft, hängt vom Ergebnis der Verarbeitung ab.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="2" anker="schritt-2" richtung="ausgehend" kopf={{"links": {"label": "MSB", "eigen": true}, "rechts": {"label": "LF"}}}>

### Angebot zur / Ablehnung der Anfrage

<Schrittskizze sicht={{"label": "MSB"}} zeilen={[{"art": "folge_ausloeser", "werte": ["35004"]}, {"art": "senden", "label": "LF", "weg": "AS4", "nachrichten": [{"nr": "15004", "titel": "Angebot  einer Konfiguration"}, {"nr": "21033", "titel": "Ablehnung der Anfrage"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [15004](/schnittstellen/202604/pruefi/QUOTES/PI_15004) — Angebot  einer Konfiguration · AS4
- [21033](/schnittstellen/202604/pruefi/IFTSTA/PI_21033) — Ablehnung der Anfrage · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="folge_ausloeser">

**Ausgelöst durch Eingang**
- [35004](/schnittstellen/202604/pruefi/REQOTE/PI_35004) — Anfrage einer Konfiguration

Die MACO APP sendet diese Nachricht selbst, als Folgeprozess nach diesem Eingang.

</li>

<li data-teil="nachricht">

Nachricht an **LF** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `21033` → [E_0531](/referenz/202604/ebd/E_0531) · MSB · Anfrage prüfen

</div>

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202604/backend-schreiben-msb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"ANFRAGE\": [\n      {\n        \"anfragetyp\": \"NEUKONFIGURATION\",\n        \"boTyp\": \"ANFRAGE\",\n        \"lokationsId\": \"50074561188\",\n        \"lokationsTyp\": \"MALO\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"ANGEBOT\": [\n      {\n        \"anfragereferenz\": \"AVV12345\",\n        \"boTyp\": \"ANGEBOT\",\n        \"positionsdaten\": [\n          {\n            \"artikelId\": [\n              \"9991000000721-01\",\n              \"9991000000721-02\",\n              \"9991000000721-03\"\n            ],\n            \"positionsbezeichnung\": \"1\"\n          }\n        ],\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"LEISTUNGSKURVENDEFINITION\": [\n      {\n        \"boTyp\": \"LEISTUNGSKURVENDEFINITION\",\n        \"leistungskurven\": [\n          {\n            \"code\": \"NBF\",\n            \"konfigurationsprodukt\": \"9991000000721\"\n          }\n        ],\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"MARKTLOKATION\": [\n      {\n        \"boTyp\": \"MARKTLOKATION\",\n        \"marktlokationsId\": \"50074561188\",\n        \"marktlokationsTyp\": [\n          {\n            \"typ\": \"STANDARD_MARKTLOKATION\"\n          }\n        ],\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"ansprechpartner\": {\n        \"boTyp\": \"ANSPRECHPARTNER\",\n        \"nachname\": \"Max Mustermann\",\n        \"rufnummern\": [\n          {\n            \"nummerntyp\": \"FAX_DURCHWAHL\",\n            \"rufnummer\": \"+001234567\"\n          }\n        ],\n        \"versionStruktur\": \"1\"\n      },\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9904446000007\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"datenaustauschreferenz\": \"MCH0IOL1\",\n    \"dokumentennummer\": \"BGMMC2WCO3K\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9903790000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"Z74\",\n    \"nachrichtendatum\": \"2025-10-10T08:00:00Z\",\n    \"nachrichtenreferenznummer\": \"UNHMC75CA7G\",\n    \"pruefidentifikator\": \"15004\",\n    \"sparte\": \"STROM\"\n  },\n  \"zusatzdaten\": {}\n}"} examples={[{"mediaType": "application/json", "examples": [{"name": "15004", "summary": "15004 — Angebot  einer Konfiguration", "value": {"stammdaten": {"MARKTLOKATION": [{"boTyp": "MARKTLOKATION", "versionStruktur": "1", "marktlokationsId": "50074561188", "marktlokationsTyp": [{"typ": "STANDARD_MARKTLOKATION"}], "sparte": "STROM"}], "ANFRAGE": [{"boTyp": "ANFRAGE", "versionStruktur": "1", "lokationsId": "50074561188", "lokationsTyp": "MALO", "anfragetyp": "NEUKONFIGURATION"}], "ANGEBOT": [{"boTyp": "ANGEBOT", "versionStruktur": "1", "anfragereferenz": "AVV12345", "sparte": "STROM", "positionsdaten": [{"positionsbezeichnung": "1", "artikelId": ["9991000000721-01", "9991000000721-02", "9991000000721-03"]}]}], "LEISTUNGSKURVENDEFINITION": [{"boTyp": "LEISTUNGSKURVENDEFINITION", "versionStruktur": "1", "sparte": "STROM", "leistungskurven": [{"code": "NBF", "konfigurationsprodukt": "9991000000721"}]}]}, "transaktionsdaten": {"datenaustauschreferenz": "MCH0IOL1", "sparte": "STROM", "pruefidentifikator": "15004", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9904446000007", "rollencodetyp": "BDEW", "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "nachname": "Max Mustermann", "rufnummern": [{"nummerntyp": "FAX_DURCHWAHL", "rufnummer": "+001234567"}]}}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9903790000002", "rollencodetyp": "BDEW"}, "dokumentennummer": "BGMMC2WCO3K", "kategorie": "Z74", "nachrichtendatum": "2025-10-10T08:00:00Z", "nachrichtenreferenznummer": "UNHMC75CA7G"}, "zusatzdaten": {}}}, {"name": "21033", "summary": "21033 — Ablehnung der Anfrage", "value": {"stammdaten": {"MARKTLOKATION": [{"boTyp": "MARKTLOKATION", "versionStruktur": "1", "marktlokationsId": "44152365487", "marktlokationsTyp": [{"typ": "STANDARD_MARKTLOKATION"}], "sparte": "STROM"}], "STATUSMITTEILUNG": [{"boTyp": "STATUSMITTEILUNG", "versionStruktur": "1", "statusObjekt": "ANGEBOTANFRAGE", "auftragsstatus": "ABGELEHNT", "positionsdaten": [{"positionsnummer": 1}]}]}, "transaktionsdaten": {"datenaustauschreferenz": "M0KXRR1W", "sparte": "STROM", "pruefidentifikator": "21033", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9904733000009", "rollencodetyp": "BDEW", "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "nachname": "Laue", "eMailAdresse": "lieferantenwechsel@eon-energie.com"}}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900244000009", "rollencodetyp": "BDEW"}, "dokumentennummer": "M0YOR4X5", "kategorie": "Z09", "nachrichtendatum": "2025-10-17T06:36:00Z", "nachrichtenreferenznummer": "M11I1RWQ", "anfragereferenznummer": "7584", "antwortstatus": "A01", "antwortstatusCodeliste": "E_0524"}, "zusatzdaten": {}}}]}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend fort, nachdem die Nachricht erstellt ist.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="3" anker="schritt-3" richtung="eingehend" kopf={{"links": {"label": "MSB", "eigen": true}, "rechts": {"label": "LF"}}}>

### Bestellung einer Konfiguration auf Ebene der direkt betroffenen Lokation

<Schrittskizze sicht={{"label": "MSB"}} zeilen={[{"art": "empfangen", "label": "LF", "weg": "AS4", "nachrichten": [{"nr": "17131", "titel": "Bestellung Angebot einer Konfiguration"}]}, {"art": "aperak", "werte": ["Z33"]}, {"art": "fortschreiben"}, {"art": "lesen_ebd", "schnittstellen": [{"label": "LESEN_ANGEBOT_BASIS"}, {"label": "LESEN_DEFINITION_LST_KURVEN"}, {"label": "Schaltzeitdefinition lesen"}, {"label": "Zaehlzeitdefinition lesen"}, {"label": "Marktlokation lesen"}, {"label": "Messlokation lesen"}, {"label": "Netzlokation lesen"}, {"label": "Preisblatt lesen"}, {"label": "LESEN_STEUERBARE_RESOURCE_BASIS"}]}, {"art": "ebd", "baeume": [{"code": "E_0526", "titel": "Bestellung prüfen"}]}, {"art": "folgeprozess", "werte": ["19132"]}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [17131](/schnittstellen/202604/pruefi/ORDERS/PI_17131) — Bestellung Angebot einer Konfiguration · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **LF** · AS4

</li>

<li data-teil="aperak">

**Aperak-Prüfungen**
- `17131` → `Z33`

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202604/backend-schreiben-msb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"ANFRAGE\": [\n      {\n        \"anfragekategorie\": \"BESTELLUNG_EINES_ANGEBOTS_EINER_KONFIGURATION\",\n        \"boTyp\": \"ANFRAGE\",\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"ansprechpartner\": {\n        \"boTyp\": \"ANSPRECHPARTNER\",\n        \"eMailAdresse\": \"andre.l@conuti.de\",\n        \"nachname\": \"A. Laue\",\n        \"versionStruktur\": \"1\"\n      },\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9904733000009\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"angebotsnummer\": \"12474\",\n    \"datenaustauschreferenz\": \"M03UGIN5\",\n    \"dokumentennummer\": \"M0ACK2J3\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9900244000009\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"nachrichtendatum\": \"2025-10-27T08:06:00Z\",\n    \"nachrichtenreferenznummer\": \"M01KAXGA\",\n    \"pruefidentifikator\": \"17131\",\n    \"sparte\": \"STROM\"\n  },\n  \"zusatzdaten\": {}\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend mit den Daten der eingegangenen Nachricht fort.

</li>

<li data-teil="lesen" data-stufe="ebd">

**Daten für die Prüfung laden**
- `LESEN_ANGEBOT_BASIS`
- `LESEN_DEFINITION_LST_KURVEN`
- [Schaltzeitdefinition lesen](/api/202604/backend-lesen/getdefinitionswitch#schaltzeitdefinition-lesen) `GET /getDefinitionSwitch` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getDefinitionSwitch"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": false, "defaultValue": "MALO", "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": false, "defaultValue": "2024-06-28T12:18:00Z", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Zaehlzeitdefinition lesen ](/api/202604/backend-lesen/getdefinitioncounting#zaehlzeitdefinition-lesen) `GET /getDefinitionCounting` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getDefinitionCounting"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": false, "defaultValue": "MALO", "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": false, "defaultValue": "2024-06-28T12:18:00Z", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Marktlokation lesen](/api/202604/backend-lesen/getmarketlocationbasic#marktlokation-lesen) `GET /getMarketLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getMarketLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": false, "defaultValue": "MALO", "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": false, "defaultValue": "2024-06-28T12:18:00Z", "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_MARKTLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Messlokation lesen](/api/202604/backend-lesen/getmeterlocationbasic#messlokation-lesen) `GET /getMeterLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getMeterLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_MESSLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Netzlokation lesen](/api/202604/backend-lesen/getgridlocationbasic#netzlokation-lesen) `GET /getGridLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getGridLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_NETZLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Preisblatt lesen](/api/202604/backend-lesen/getpricesheetbasic#preisblatt-lesen) `GET /getPriceSheetBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getPriceSheetBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": false, "defaultValue": "74018657187", "type": "string"}, {"name": "parameter2", "isRequired": false, "defaultValue": "MALO", "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": false, "defaultValue": "2024-06-28T12:18:00Z", "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_PREISBLATT_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- `LESEN_STEUERBARE_RESOURCE_BASIS`

</li>

<li data-teil="baum">

**Entscheidungsbaum**
- `17131` → [E_0526](/referenz/202604/ebd/E_0526) — Bestellung prüfen

</li>

<li data-teil="folgeprozess">

**Folgeprozess auslösen**
- [19132](/schnittstellen/202604/pruefi/ORDRSP/PI_19132) — Mitteilung zur Bestellung Konfiguration

Nach der Verarbeitung startet die MACO APP diesen Folgeprozess selbst.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="4" anker="schritt-4" richtung="eingehend" kopf={{"links": {"label": "MSB", "eigen": true}, "rechts": {"label": "LF"}}}>

### Bestellung einer Konfiguration auf Ebene der direkt betroffenen Lokation

<Schrittskizze sicht={{"label": "MSB"}} zeilen={[{"art": "empfangen", "label": "LF", "weg": "AS4", "nachrichten": [{"nr": "17130", "titel": "Bestellung einer Konfiguration"}, {"nr": "17123", "titel": "Bestellung Änderung Zählzeitdefinition"}]}, {"art": "lesen_aperak", "schnittstellen": [{"label": "Marktlokation lesen"}, {"label": "Messlokation lesen"}, {"label": "Netzlokation lesen"}, {"label": "Steuerbare Ressource lesen"}]}, {"art": "aperak", "werte": ["Z10", "Z33"]}, {"art": "erstellen", "nummern": ["17130"]}, {"art": "fortschreiben", "nummern": ["17123"]}, {"art": "lesen_ebd", "schnittstellen": [{"label": "LESEN_DEFINITION_LST_KURVEN"}, {"label": "Schaltzeitdefinition lesen"}, {"label": "Zaehlzeitdefinition lesen"}, {"label": "Preisblatt lesen"}]}, {"art": "ebd", "baeume": [{"code": "E_0526", "titel": "Bestellung prüfen"}, {"code": "E_0533", "titel": "Bestellung prüfen"}]}, {"art": "folgeprozess", "werte": ["19132"]}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [17130](/schnittstellen/202604/pruefi/ORDERS/PI_17130) — Bestellung einer Konfiguration · AS4
- [17123](/schnittstellen/202604/pruefi/ORDERS/PI_17123) — Bestellung Änderung Zählzeitdefinition · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **LF** · AS4

</li>

<li data-teil="lesen" data-stufe="aperak">

**Daten für die Eingangsprüfung laden**
- [Marktlokation lesen](/api/202604/backend-lesen/getmarketlocationbasic#marktlokation-lesen) `GET /getMarketLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getMarketLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": false, "defaultValue": "MALO", "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": false, "defaultValue": "2024-06-28T12:18:00Z", "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_MARKTLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Messlokation lesen](/api/202604/backend-lesen/getmeterlocationbasic#messlokation-lesen) `GET /getMeterLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getMeterLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_MESSLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Netzlokation lesen](/api/202604/backend-lesen/getgridlocationbasic#netzlokation-lesen) `GET /getGridLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getGridLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_NETZLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Steuerbare Ressource lesen](/api/202604/backend-lesen/getcontrollableresourcebasic#steuerbare-ressource-lesen) `GET /getControllableResourceBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getControllableResourceBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

</li>

<li data-teil="aperak">

**Aperak-Prüfungen**
- `17130` → `Z10`
- `17130` → `Z33`

</li>

<li data-teil="schnittstelle" data-art="schreiben">

**Schreibende Schnittstelle**
- `17130` → Vorgang angelegt — [Prozessdaten erstellen](/api/202604/backend-schreiben-msb/createprocessdata#prozessdaten-erstellen) `POST /createProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/createProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "ERSTELLEN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"ANFRAGE\": [\n      {\n        \"anfragekategorie\": \"BESTELLUNG_EINER_KONFIGURATION\",\n        \"boTyp\": \"ANFRAGE\",\n        \"lokationsId\": \"C4897654121\",\n        \"lokationsTyp\": \"STEUERBARE_RESSOURCE\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"AUFTRAG\": [\n      {\n        \"boTyp\": \"AUFTRAG\",\n        \"positionsdaten\": [\n          {\n            \"positionsnummer\": 1\n          }\n        ],\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"SCHALTZEITDEFINITION\": [\n      {\n        \"boTyp\": \"SCHALTZEITDEFINITION\",\n        \"schaltzeiten\": [\n          {\n            \"code\": \"AAL\",\n            \"konfigurationsprodukt\": \"9991000000713\"\n          }\n        ],\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"STEUERBARE_RESSOURCE\": [\n      {\n        \"boTyp\": \"STEUERBARE_RESSOURCE\",\n        \"ressourcenId\": \"C4897654121\",\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"ansprechpartner\": {\n        \"boTyp\": \"ANSPRECHPARTNER\",\n        \"eMailAdresse\": \"a.l@cinuti.de\",\n        \"nachname\": \"A\",\n        \"versionStruktur\": \"1\"\n      },\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9903111000003\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"beteiligterMarktpartner\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9903111000003\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"datenaustauschreferenz\": \"M0OU3NLP\",\n    \"dokumentennummer\": \"M0O1YVAK\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9904629000006\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"nachrichtendatum\": \"2024-08-19T08:03:00Z\",\n    \"nachrichtenreferenznummer\": \"M08MHOSC\",\n    \"pruefidentifikator\": \"17130\",\n    \"sparte\": \"STROM\",\n    \"vorgangsreferenznummer\": \"AS1234\"\n  },\n  \"zusatzdaten\": {}\n}"} examples={[{"mediaType": "application/json", "examples": [{"name": "17130", "summary": "17130 — Bestellung einer Konfiguration", "value": {"stammdaten": {"ANFRAGE": [{"boTyp": "ANFRAGE", "versionStruktur": "1", "anfragekategorie": "BESTELLUNG_EINER_KONFIGURATION", "lokationsId": "C4897654121", "lokationsTyp": "STEUERBARE_RESSOURCE"}], "AUFTRAG": [{"boTyp": "AUFTRAG", "versionStruktur": "1", "positionsdaten": [{"positionsnummer": 1}]}], "STEUERBARE_RESSOURCE": [{"boTyp": "STEUERBARE_RESSOURCE", "versionStruktur": "1", "ressourcenId": "C4897654121"}], "SCHALTZEITDEFINITION": [{"boTyp": "SCHALTZEITDEFINITION", "versionStruktur": "1", "schaltzeiten": [{"code": "AAL", "konfigurationsprodukt": "9991000000713"}]}]}, "transaktionsdaten": {"datenaustauschreferenz": "M0OU3NLP", "sparte": "STROM", "pruefidentifikator": "17130", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9903111000003", "rollencodetyp": "BDEW", "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "nachname": "A", "eMailAdresse": "a.l@cinuti.de"}}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9904629000006", "rollencodetyp": "BDEW"}, "dokumentennummer": "M0O1YVAK", "nachrichtendatum": "2024-08-19T08:03:00Z", "nachrichtenreferenznummer": "M08MHOSC", "vorgangsreferenznummer": "AS1234", "beteiligterMarktpartner": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9903111000003", "rollencodetyp": "BDEW"}}, "zusatzdaten": {}}}, {"name": "17123", "summary": "17123 — Bestellung Änderung Zählzeitdefinition", "value": {"stammdaten": {"ANFRAGE": [{"boTyp": "ANFRAGE", "versionStruktur": "1", "anfragekategorie": "AENDERUNG_INDIVIDUELLER_KONFIGURATION", "anfragetyp": "AENDERUNG_KONFIGURATION", "lokationsId": "44897654121", "lokationsTyp": "MALO"}], "AUFTRAG": [{"boTyp": "AUFTRAG", "versionStruktur": "1", "ausfuehrungsdatum": "2024-08-22T22:00:00Z", "positionsdaten": [{"positionsnummer": 1}]}], "MARKTLOKATION": [{"boTyp": "MARKTLOKATION", "versionStruktur": "1", "zaehlwerke": [{"messprodukt": "9991000000052", "zaehlzeiten": {"zaehlzeitDefinition": "AAL"}}]}]}, "transaktionsdaten": {"datenaustauschreferenz": "M0E47OMP", "sparte": "STROM", "pruefidentifikator": "17123", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9903111000003", "rollencodetyp": "BDEW", "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "nachname": "Laue", "eMailAdresse": "a.l@conuti.de"}}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9903111000003", "rollencodetyp": "BDEW"}, "dokumentennummer": "M0RAU7GV", "nachrichtendatum": "2024-08-19T07:34:00Z", "nachrichtenreferenznummer": "M0CYKMGN"}, "zusatzdaten": {}}}]}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Legt im Backend einen neuen Vorgang mit den Daten der eingegangenen Nachricht an.

</li>

<li data-teil="schnittstelle" data-art="fortschreiben" data-abgeleitet="ja">

**Schreibende Schnittstelle**
- `17123` → Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202604/backend-schreiben-msb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"ANFRAGE\": [\n      {\n        \"anfragekategorie\": \"BESTELLUNG_EINER_KONFIGURATION\",\n        \"boTyp\": \"ANFRAGE\",\n        \"lokationsId\": \"C4897654121\",\n        \"lokationsTyp\": \"STEUERBARE_RESSOURCE\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"AUFTRAG\": [\n      {\n        \"boTyp\": \"AUFTRAG\",\n        \"positionsdaten\": [\n          {\n            \"positionsnummer\": 1\n          }\n        ],\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"SCHALTZEITDEFINITION\": [\n      {\n        \"boTyp\": \"SCHALTZEITDEFINITION\",\n        \"schaltzeiten\": [\n          {\n            \"code\": \"AAL\",\n            \"konfigurationsprodukt\": \"9991000000713\"\n          }\n        ],\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"STEUERBARE_RESSOURCE\": [\n      {\n        \"boTyp\": \"STEUERBARE_RESSOURCE\",\n        \"ressourcenId\": \"C4897654121\",\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"ansprechpartner\": {\n        \"boTyp\": \"ANSPRECHPARTNER\",\n        \"eMailAdresse\": \"a.l@cinuti.de\",\n        \"nachname\": \"A\",\n        \"versionStruktur\": \"1\"\n      },\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9903111000003\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"beteiligterMarktpartner\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9903111000003\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"datenaustauschreferenz\": \"M0OU3NLP\",\n    \"dokumentennummer\": \"M0O1YVAK\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9904629000006\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"nachrichtendatum\": \"2024-08-19T08:03:00Z\",\n    \"nachrichtenreferenznummer\": \"M08MHOSC\",\n    \"pruefidentifikator\": \"17130\",\n    \"sparte\": \"STROM\",\n    \"vorgangsreferenznummer\": \"AS1234\"\n  },\n  \"zusatzdaten\": {}\n}"} examples={[{"mediaType": "application/json", "examples": [{"name": "17130", "summary": "17130 — Bestellung einer Konfiguration", "value": {"stammdaten": {"ANFRAGE": [{"boTyp": "ANFRAGE", "versionStruktur": "1", "anfragekategorie": "BESTELLUNG_EINER_KONFIGURATION", "lokationsId": "C4897654121", "lokationsTyp": "STEUERBARE_RESSOURCE"}], "AUFTRAG": [{"boTyp": "AUFTRAG", "versionStruktur": "1", "positionsdaten": [{"positionsnummer": 1}]}], "STEUERBARE_RESSOURCE": [{"boTyp": "STEUERBARE_RESSOURCE", "versionStruktur": "1", "ressourcenId": "C4897654121"}], "SCHALTZEITDEFINITION": [{"boTyp": "SCHALTZEITDEFINITION", "versionStruktur": "1", "schaltzeiten": [{"code": "AAL", "konfigurationsprodukt": "9991000000713"}]}]}, "transaktionsdaten": {"datenaustauschreferenz": "M0OU3NLP", "sparte": "STROM", "pruefidentifikator": "17130", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9903111000003", "rollencodetyp": "BDEW", "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "nachname": "A", "eMailAdresse": "a.l@cinuti.de"}}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9904629000006", "rollencodetyp": "BDEW"}, "dokumentennummer": "M0O1YVAK", "nachrichtendatum": "2024-08-19T08:03:00Z", "nachrichtenreferenznummer": "M08MHOSC", "vorgangsreferenznummer": "AS1234", "beteiligterMarktpartner": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9903111000003", "rollencodetyp": "BDEW"}}, "zusatzdaten": {}}}, {"name": "17123", "summary": "17123 — Bestellung Änderung Zählzeitdefinition", "value": {"stammdaten": {"ANFRAGE": [{"boTyp": "ANFRAGE", "versionStruktur": "1", "anfragekategorie": "AENDERUNG_INDIVIDUELLER_KONFIGURATION", "anfragetyp": "AENDERUNG_KONFIGURATION", "lokationsId": "44897654121", "lokationsTyp": "MALO"}], "AUFTRAG": [{"boTyp": "AUFTRAG", "versionStruktur": "1", "ausfuehrungsdatum": "2024-08-22T22:00:00Z", "positionsdaten": [{"positionsnummer": 1}]}], "MARKTLOKATION": [{"boTyp": "MARKTLOKATION", "versionStruktur": "1", "zaehlwerke": [{"messprodukt": "9991000000052", "zaehlzeiten": {"zaehlzeitDefinition": "AAL"}}]}]}, "transaktionsdaten": {"datenaustauschreferenz": "M0E47OMP", "sparte": "STROM", "pruefidentifikator": "17123", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9903111000003", "rollencodetyp": "BDEW", "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "nachname": "Laue", "eMailAdresse": "a.l@conuti.de"}}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9903111000003", "rollencodetyp": "BDEW"}, "dokumentennummer": "M0RAU7GV", "nachrichtendatum": "2024-08-19T07:34:00Z", "nachrichtenreferenznummer": "M0CYKMGN"}, "zusatzdaten": {}}}]}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend mit den Daten der eingegangenen Nachricht fort.

</li>

<li data-teil="lesen" data-stufe="ebd">

**Daten für die Prüfung laden**
- `LESEN_DEFINITION_LST_KURVEN`
- [Schaltzeitdefinition lesen](/api/202604/backend-lesen/getdefinitionswitch#schaltzeitdefinition-lesen) `GET /getDefinitionSwitch` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getDefinitionSwitch"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": false, "defaultValue": "MALO", "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": false, "defaultValue": "2024-06-28T12:18:00Z", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Zaehlzeitdefinition lesen ](/api/202604/backend-lesen/getdefinitioncounting#zaehlzeitdefinition-lesen) `GET /getDefinitionCounting` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getDefinitionCounting"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": false, "defaultValue": "MALO", "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": false, "defaultValue": "2024-06-28T12:18:00Z", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Preisblatt lesen](/api/202604/backend-lesen/getpricesheetbasic#preisblatt-lesen) `GET /getPriceSheetBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getPriceSheetBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": false, "defaultValue": "74018657187", "type": "string"}, {"name": "parameter2", "isRequired": false, "defaultValue": "MALO", "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": false, "defaultValue": "2024-06-28T12:18:00Z", "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_PREISBLATT_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

</li>

<li data-teil="baum">

**Entscheidungsbaum**
- `17130` → [E_0526](/referenz/202604/ebd/E_0526) — Bestellung prüfen
- `17123` → [E_0533](/referenz/202604/ebd/E_0533) — Bestellung prüfen

</li>

<li data-teil="folgeprozess">

**Folgeprozess auslösen**
- [19132](/schnittstellen/202604/pruefi/ORDRSP/PI_19132) — Mitteilung zur Bestellung Konfiguration

Nach der Verarbeitung startet die MACO APP diesen Folgeprozess selbst.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="5" anker="schritt-5" richtung="ausgehend" kopf={{"links": {"label": "MSB", "eigen": true}, "rechts": {"label": "LF"}}}>

### Mitteilung zum weiteren Vorgehen zur Bestellung

<Schrittskizze sicht={{"label": "MSB"}} zeilen={[{"art": "folge_ausloeser", "werte": ["17130", "17131"]}, {"art": "senden", "label": "LF", "weg": "AS4", "nachrichten": [{"nr": "19132", "titel": "Mitteilung zur Bestellung Konfiguration"}, {"nr": "19124", "titel": "Mitteilung zur Änderung Zählzeitdefinition"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [19132](/schnittstellen/202604/pruefi/ORDRSP/PI_19132) — Mitteilung zur Bestellung Konfiguration · AS4
- [19124](/schnittstellen/202604/pruefi/ORDRSP/PI_19124) — Mitteilung zur Änderung Zählzeitdefinition · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="folge_ausloeser">

**Ausgelöst durch Eingang**
- [17130](/schnittstellen/202604/pruefi/ORDERS/PI_17130) — Bestellung einer Konfiguration
- [17131](/schnittstellen/202604/pruefi/ORDERS/PI_17131) — Bestellung Angebot einer Konfiguration

Die MACO APP sendet diese Nachricht selbst, als Folgeprozess nach einem dieser Eingänge.

</li>

<li data-teil="nachricht">

Nachricht an **LF** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `19132`, `19124` → [E_0533](/referenz/202604/ebd/E_0533) · MSB · Bestellung prüfen

</div>

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202604/backend-schreiben-msb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"ANFRAGE\": [\n      {\n        \"anfragekategorie\": \"AENDERUNG_INDIVIDUELLER_KONFIGURATION\",\n        \"boTyp\": \"ANFRAGE\",\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"ansprechpartner\": {\n        \"boTyp\": \"ANSPRECHPARTNER\",\n        \"nachname\": \"P GETTY\",\n        \"rufnummern\": [\n          {\n            \"nummerntyp\": \"RUF_DURCHWAHL\",\n            \"rufnummer\": \"+3222271020\"\n          }\n        ],\n        \"versionStruktur\": \"1\"\n      },\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9900244000009\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"antwortstatus\": \"A99\",\n    \"antwortstatusCodeliste\": \"E_0523\",\n    \"auftragsReferenz\": \"AFN9523\",\n    \"datenaustauschreferenz\": \"DASFTZWAIAUQDZ\",\n    \"dokumentennummer\": \"DA862411200724399903323000007189649\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9903692000001\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"freitext\": \"Stell keine Fragen\",\n    \"nachrichtendatum\": \"2026-04-01T12:31:00Z\",\n    \"nachrichtenreferenznummer\": \"DALRTRVYCPSLBA\",\n    \"pruefidentifikator\": \"19124\",\n    \"sparte\": \"STROM\"\n  },\n  \"zusatzdaten\": {}\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

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
- [17130](/schnittstellen/202604/pruefi/ORDERS/PI_17130) — Bestellung einer Konfiguration · AS4
- [17118](/schnittstellen/202604/pruefi/ORDERS/PI_17118) — Bestellung einer Konfigurationsänderung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="folge_ausloeser">

**Ausgelöst durch Eingang**
- [17121](/schnittstellen/202604/pruefi/ORDERS/PI_17121)

Die MACO APP sendet diese Nachricht selbst, als Folgeprozess nach diesem Eingang.

</li>

<li data-teil="nachricht">

Nachricht an **weiterer MSB** · AS4

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202604/backend-schreiben-msb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"ANFRAGE\": [\n      {\n        \"anfragekategorie\": \"BESTELLUNG_EINER_KONFIGURATION\",\n        \"boTyp\": \"ANFRAGE\",\n        \"lokationsId\": \"C4897654121\",\n        \"lokationsTyp\": \"STEUERBARE_RESSOURCE\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"AUFTRAG\": [\n      {\n        \"boTyp\": \"AUFTRAG\",\n        \"positionsdaten\": [\n          {\n            \"positionsnummer\": 1\n          }\n        ],\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"SCHALTZEITDEFINITION\": [\n      {\n        \"boTyp\": \"SCHALTZEITDEFINITION\",\n        \"schaltzeiten\": [\n          {\n            \"code\": \"AAL\",\n            \"konfigurationsprodukt\": \"9991000000713\"\n          }\n        ],\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"STEUERBARE_RESSOURCE\": [\n      {\n        \"boTyp\": \"STEUERBARE_RESSOURCE\",\n        \"ressourcenId\": \"C4897654121\",\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"ansprechpartner\": {\n        \"boTyp\": \"ANSPRECHPARTNER\",\n        \"eMailAdresse\": \"a.l@cinuti.de\",\n        \"nachname\": \"A\",\n        \"versionStruktur\": \"1\"\n      },\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9903111000003\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"beteiligterMarktpartner\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9903111000003\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"datenaustauschreferenz\": \"M0OU3NLP\",\n    \"dokumentennummer\": \"M0O1YVAK\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9904629000006\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"nachrichtendatum\": \"2024-08-19T08:03:00Z\",\n    \"nachrichtenreferenznummer\": \"M08MHOSC\",\n    \"pruefidentifikator\": \"17130\",\n    \"sparte\": \"STROM\",\n    \"vorgangsreferenznummer\": \"AS1234\"\n  },\n  \"zusatzdaten\": {}\n}"} examples={[{"mediaType": "application/json", "examples": [{"name": "17130", "summary": "17130 — Bestellung einer Konfiguration", "value": {"stammdaten": {"ANFRAGE": [{"boTyp": "ANFRAGE", "versionStruktur": "1", "anfragekategorie": "BESTELLUNG_EINER_KONFIGURATION", "lokationsId": "C4897654121", "lokationsTyp": "STEUERBARE_RESSOURCE"}], "AUFTRAG": [{"boTyp": "AUFTRAG", "versionStruktur": "1", "positionsdaten": [{"positionsnummer": 1}]}], "STEUERBARE_RESSOURCE": [{"boTyp": "STEUERBARE_RESSOURCE", "versionStruktur": "1", "ressourcenId": "C4897654121"}], "SCHALTZEITDEFINITION": [{"boTyp": "SCHALTZEITDEFINITION", "versionStruktur": "1", "schaltzeiten": [{"code": "AAL", "konfigurationsprodukt": "9991000000713"}]}]}, "transaktionsdaten": {"datenaustauschreferenz": "M0OU3NLP", "sparte": "STROM", "pruefidentifikator": "17130", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9903111000003", "rollencodetyp": "BDEW", "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "nachname": "A", "eMailAdresse": "a.l@cinuti.de"}}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9904629000006", "rollencodetyp": "BDEW"}, "dokumentennummer": "M0O1YVAK", "nachrichtendatum": "2024-08-19T08:03:00Z", "nachrichtenreferenznummer": "M08MHOSC", "vorgangsreferenznummer": "AS1234", "beteiligterMarktpartner": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9903111000003", "rollencodetyp": "BDEW"}}, "zusatzdaten": {}}}, {"name": "17118", "summary": "17118 — Bestellung einer Konfigurationsänderung", "value": {"stammdaten": {"ANFRAGE": [{"boTyp": "ANFRAGE", "versionStruktur": "1", "anfragekategorie": "AENDERUNG_GERAETEKONFIGURATION", "anfragetyp": "ABBESTELLUNG_MESSPRODUKT", "lokationsId": "DE00014545768S0000000000000003054", "lokationsTyp": "MELO"}], "AUFTRAG": [{"boTyp": "AUFTRAG", "versionStruktur": "1", "ausfuehrungsdatum": "2024-08-29T22:00:00Z", "positionsdaten": [{"lokationsId": "DE0032106765712000000000000000037", "positionsnummer": 1}]}], "MESSLOKATION": [{"boTyp": "MESSLOKATION", "versionStruktur": "1", "messlokationsId": "DE0032106765712000000000000000037", "zaehlwerke": [{"messprodukt": "9991000000169", "notwendigkeitZweiteMessung": "NICHT_VORHANDEN", "werteuebermittlungVerwendungszweck": "VORHANDEN", "zaehlzeiten": {"zaehlzeitDefinition": "AAI"}}]}]}, "transaktionsdaten": {"datenaustauschreferenz": "M0JPDOTZ", "sparte": "STROM", "pruefidentifikator": "17118", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9904629000006", "rollencodetyp": "BDEW", "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "nachname": "Laue", "eMailAdresse": "a.laue@conuti.de"}}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9904629000008", "rollencodetyp": "BDEW"}, "dokumentennummer": "M0DAA51T", "nachrichtendatum": "2024-08-19T07:02:00Z", "nachrichtenreferenznummer": "M0L4YRVR", "beteiligterMarktpartner": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900259000002", "rollencodetyp": "BDEW"}}, "zusatzdaten": {}}}]}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend fort, nachdem die Nachricht erstellt ist.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="7" anker="schritt-7" richtung="eingehend" kopf={{"links": {"label": "MSB", "eigen": true}, "rechts": {"label": "weiterer MSB"}}}>

### Mitteilung zum weiteren Vorgehen zur Bestellung

<Schrittskizze sicht={{"label": "MSB"}} zeilen={[{"art": "empfangen", "label": "weiterer MSB", "weg": "AS4", "nachrichten": [{"nr": "19132", "titel": "Mitteilung zur Bestellung Konfiguration"}, {"nr": "19127", "titel": "Mitteilung zur Konfigurationsänderung"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [19132](/schnittstellen/202604/pruefi/ORDRSP/PI_19132) — Mitteilung zur Bestellung Konfiguration · AS4
- [19127](/schnittstellen/202604/pruefi/ORDRSP/PI_19127) — Mitteilung zur Konfigurationsänderung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **weiterer MSB** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `19132`, `19127` → [E_0527](/referenz/202604/ebd/E_0527) · MSB · Bestellung

</div>

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

<Schritt nr="8" anker="schritt-8" richtung="eingehend" kopf={{"links": {"label": "MSB", "eigen": true}, "rechts": {"label": "weiterer MSB"}}}>

### Antwort auf Bestellung

<Schrittskizze sicht={{"label": "MSB"}} zeilen={[{"art": "empfangen", "label": "weiterer MSB", "weg": "AS4", "nachrichten": [{"nr": "21043", "titel": "Bestellungsantwort / -mitteilung"}]}, {"art": "aperak", "werte": ["Z33"]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [21043](/schnittstellen/202604/pruefi/IFTSTA/PI_21043) — Bestellungsantwort / -mitteilung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **weiterer MSB** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `21043` → [E_0535](/referenz/202604/ebd/E_0535) · Umsetzung der Konfiguration prüfen

</div>

</li>

<li data-teil="aperak">

**Aperak-Prüfungen**
- `21043` → `Z33`

</li>

<li data-teil="schnittstelle" data-art="fortschreiben" data-abgeleitet="ja">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202604/backend-schreiben-msb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"STATUSMITTEILUNG\": [\n      {\n        \"auftragsstatus\": \"ABGELEHNT\",\n        \"boTyp\": \"STATUSMITTEILUNG\",\n        \"positionsdaten\": [\n          {\n            \"positionsnummer\": 1,\n            \"statusVeraenderungsZeitpunkt\": \"2025-01-15T23:00:00Z\"\n          }\n        ],\n        \"statusObjekt\": \"STATUSBESTELLUNG\",\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"marktrolle\": \"LF\",\n      \"rollencodenummer\": \"9903790000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"anfrageReferenz\": \"BGM12345\",\n    \"antwortstatus\": \"A01\",\n    \"antwortstatusCodeliste\": \"E_0529\",\n    \"datenaustauschreferenz\": \"M0STR69K\",\n    \"dokumentennummer\": \"BGMM0UQI60K\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"marktrolle\": \"NB\",\n      \"rollencodenummer\": \"9900321000005\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"Z73\",\n    \"nachrichtendatum\": \"2025-04-04T12:00:00Z\",\n    \"nachrichtenreferenznummer\": \"UNHM0N3XSGK\",\n    \"pruefidentifikator\": \"21043\",\n    \"sparte\": \"STROM\"\n  },\n  \"zusatzdaten\": {}\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend mit den Daten der eingegangenen Nachricht fort.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="9" anker="schritt-9" richtung="ausgehend" kopf={{"links": {"label": "MSB", "eigen": true}, "rechts": {"label": "LF"}}}>

### Antwort auf Bestellung

<Schrittskizze sicht={{"label": "MSB"}} zeilen={[{"art": "senden", "label": "LF", "weg": "AS4", "nachrichten": [{"nr": "21043", "titel": "Bestellungsantwort / -mitteilung"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [21043](/schnittstellen/202604/pruefi/IFTSTA/PI_21043) — Bestellungsantwort / -mitteilung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht an **LF** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `21043` → [E_0536](/referenz/202604/ebd/E_0536) · MSB · Bewertung des Gesamtvorgangs

</div>

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202604/backend-schreiben-msb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"STATUSMITTEILUNG\": [\n      {\n        \"auftragsstatus\": \"ABGELEHNT\",\n        \"boTyp\": \"STATUSMITTEILUNG\",\n        \"positionsdaten\": [\n          {\n            \"positionsnummer\": 1,\n            \"statusVeraenderungsZeitpunkt\": \"2025-01-15T23:00:00Z\"\n          }\n        ],\n        \"statusObjekt\": \"STATUSBESTELLUNG\",\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"marktrolle\": \"LF\",\n      \"rollencodenummer\": \"9903790000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"anfrageReferenz\": \"BGM12345\",\n    \"antwortstatus\": \"A01\",\n    \"antwortstatusCodeliste\": \"E_0529\",\n    \"datenaustauschreferenz\": \"M0STR69K\",\n    \"dokumentennummer\": \"BGMM0UQI60K\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"marktrolle\": \"NB\",\n      \"rollencodenummer\": \"9900321000005\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"Z73\",\n    \"nachrichtendatum\": \"2025-04-04T12:00:00Z\",\n    \"nachrichtenreferenznummer\": \"UNHM0N3XSGK\",\n    \"pruefidentifikator\": \"21043\",\n    \"sparte\": \"STROM\"\n  },\n  \"zusatzdaten\": {}\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

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
- [21043](/schnittstellen/202604/pruefi/IFTSTA/PI_21043) — Bestellungsantwort / -mitteilung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht an **weiterer MSB** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `21043` → [E_0536](/referenz/202604/ebd/E_0536) · MSB · Bewertung des Gesamtvorgangs

</div>

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202604/backend-schreiben-msb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"STATUSMITTEILUNG\": [\n      {\n        \"auftragsstatus\": \"ABGELEHNT\",\n        \"boTyp\": \"STATUSMITTEILUNG\",\n        \"positionsdaten\": [\n          {\n            \"positionsnummer\": 1,\n            \"statusVeraenderungsZeitpunkt\": \"2025-01-15T23:00:00Z\"\n          }\n        ],\n        \"statusObjekt\": \"STATUSBESTELLUNG\",\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"marktrolle\": \"LF\",\n      \"rollencodenummer\": \"9903790000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"anfrageReferenz\": \"BGM12345\",\n    \"antwortstatus\": \"A01\",\n    \"antwortstatusCodeliste\": \"E_0529\",\n    \"datenaustauschreferenz\": \"M0STR69K\",\n    \"dokumentennummer\": \"BGMM0UQI60K\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"marktrolle\": \"NB\",\n      \"rollencodenummer\": \"9900321000005\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"Z73\",\n    \"nachrichtendatum\": \"2025-04-04T12:00:00Z\",\n    \"nachrichtenreferenznummer\": \"UNHM0N3XSGK\",\n    \"pruefidentifikator\": \"21043\",\n    \"sparte\": \"STROM\"\n  },\n  \"zusatzdaten\": {}\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

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
| [E_0527](/referenz/202604/ebd/E_0527) | Bestellung |
| [E_0531](/referenz/202604/ebd/E_0531) | Anfrage prüfen |
| [E_0533](/referenz/202604/ebd/E_0533) | Bestellung prüfen |
| [E_0535](/referenz/202604/ebd/E_0535) | Umsetzung der Konfiguration prüfen |
| [E_0536](/referenz/202604/ebd/E_0536) | Bewertung des Gesamtvorgangs |

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
  - Im Fall der Bestellung einer Konfiguration vom LF an den NB: Der NB hat vom LF eine Bestellung der Konfiguration über den Use-Case „[Bestellung einer Konfiguration vom LF an NB](/prozessdoku/202604/LF/GPKE-Teil3-bestellung-einer-konfiguration-vom-lf-an-nb)“ (z.B. die Bestellung einer Änderung des Bilanzierungsverfahrens oder Bestellung einer Konfiguration, für die eine Zählzeitdefinition des NB erforderlich ist) erhalten, bei der die Einrichtung der Konfiguration aus Sicht des NB grundsätzlich möglich ist.
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

- Sofern die Konfiguration für alle betroffenen Lokationen erfolgreich eingerichtet wurde, führt der MSB der jeweils betroffenen Lokation den Use-Case „Stammdatenänderung“ (hier: SD „[Stammdatenänderung vom MSB (verantwortlich) ausgehend](/prozessdoku/202604/MSB/GPKE-Teil4-stammdatenaenderung-vom-msb-verantwortlich-ausgehend)“) (GPKE Teil 4) durch, sofern für die jeweilige Lokation eine Stammdatenänderung aufgrund der Einrichtung der Konfiguration erforderlich ist.
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
- Konfigurationen des NB werden im Use-Case „[Beginn Messstellenbetrieb](/prozessdoku/202604/LF/WiM-Teil1-beginn-messstellenbetrieb)“ (WiM Teil 1) in Prozessschritt 2 im Rahmen der Mindestparameter für die Messlokation(en) vom NB dem MSB mitgeteilt. Eine Bestellung einer in den Mindestparametern enthaltenen Konfiguration ist nicht über den hier beschriebenen Use-Case notwendig. Ergänzend zu den in den Mindestparametern mitgeteilten Konfigurationen, kann der NB mit Hilfe des hier beschriebenen Use-Cases eine Bestellung einer Konfiguration an den zukünftigen MSB übermitteln. Hinweis: Wird dem MSB im Rahmen der Mindestparameter im Use-Case „[Beginn Messstellenbetrieb](/prozessdoku/202604/LF/WiM-Teil1-beginn-messstellenbetrieb)“ (WiM Teil 1) eine Zählzeitdefinition des NB mitgeteilt, die der MSB vorab nicht über den Use-Case „[Übermittlung einer Definition des NB durch den NB](/prozessdoku/202604/MSB/GPKE-Teil3-uebermittlung-einer-definition-des-nb-durch-den-nb)“ übermittelt bekommen hat, so ist die Energie in einem Register an der/den Messlokation(en) und der zugehörigen Marktlokation für den Zählzeitenanwendungszweck „Netznutzung“ zu erfassen.

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

**LF** sendet „Anfrage einer Konfiguration auf Ebene der direkt betroffenen Lokation“ (Schritt 1). Ab hier ist der Beteiligte dieser Seite am Zug.

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

- [Sicht WMSB](/prozessdoku/202604/MSB--WMSB/GPKE-Teil3-bestellung-einer-konfiguration-vom-lf-an-msb) — weiterer Messstellenbetreiber · Marktrolle MSB
- [Sicht LF](/prozessdoku/202604/LF/GPKE-Teil3-bestellung-einer-konfiguration-vom-lf-an-msb) — LF

<Hinweisbereich>

*Die Schritte sind die **möglichen** Nachrichten dieses Prozesses, keine Abfolge — die Quelle führt weder Bedingungen noch Alternativen. Das Kästchen am Schritt nennt links die eigene Sicht: **←** empfängt sie, **→** sendet sie. Zugeklappte Schritte laufen zwischen anderen Marktpartnern.*

Diese Lesezugriffe sind im API-Katalog dieser Formatversion nicht geführt; am Schritt steht deshalb nur ihr Kommando, ohne Adresse und ohne Knopf.

Betrifft: [1](#schritt-1), [3](#schritt-3), [4](#schritt-4)

Die Konnektortabelle führt für diese Schritte keinen Schreibaufruf. Abgeleitet aus dem Prozessverlauf: Die eigene Rolle war an diesem Prozess schon beteiligt, der Vorgang besteht also.

Betrifft: [4](#schritt-4), [7](#schritt-7), [8](#schritt-8)

Zu den Prüfidentifikatoren dieser Schritte liegt kein Testfall im Testbestand; der Knopf »Ausprobieren« der schreibenden Schnittstelle bietet deshalb keinen Rumpf an.

Betrifft: [7](#schritt-7)

</Hinweisbereich>
