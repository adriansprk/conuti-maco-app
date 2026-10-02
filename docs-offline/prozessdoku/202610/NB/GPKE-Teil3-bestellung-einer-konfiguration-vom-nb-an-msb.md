# Bestellung einer Konfiguration vom NB an MSB — Sicht NB

<Kopf rolle="NB" beteiligter="NB" festlegung="GPKE" dokument="GPKE Teil 3" kapitel="1.3.3.2" sparte="Strom" schritte={10} suchtitel="Bestellung einer Konfiguration vom NB an MSB — Sicht NB · GPKE Teil 3 · Formatversion 202610" abschnitte={[{"id": "abschnitt-ablauf", "label": "Prozessablauf"}, {"id": "abschnitt-schritte", "label": "Prozessschritte"}, {"id": "abschnitt-informationen", "label": "Prozess-Informationen"}, {"id": "abschnitt-sichten", "label": "Andere Sichten des Prozesses"}]} />

<Kurzfassung>

Der NB bzw. LF bestellt beim MSB der direkt betroffenen Lokation eine Konfiguration für die direkt betroffene Lokation. Sofern weitere Lokationen der direkt betroffenen Lokation von der Konfiguration betroffen sind, gibt der NB bzw. LF diese weiter betroffenen Lokationen in der Bestellung ebenfalls an (z.B. hat der NB in der Bestellung der Änderung des Bilanzierungsverfahrens auf der Ebene der Marktlokation, neben der Marktlokation auch alle Messlokationen der Marktlokation beim MSB der Marktlokation zu bestellen). Bevor eine kostenpflichtige Bestellung erfolgen kann, hat der NB bzw. LF ein Angebot beim MSB der direkt betroffenen Lokation für die Einrichtung der Konfiguration anzufragen. Der MSB prüft die Bestellung und teilt dem NB bzw. LF das weitere Vorgehen zur Bestellung mit. Sofern weitere Lokationen der direkt betroffenen Lokation von der Konfiguration betroffen sind, für die der MSB der direkt betroffenen Lokation nicht den Messstellenbetrieb durchführt, bindet er für diese weiter betroffenen Lokationen die jeweiligen weiteren MSB ein.

</Kurzfassung>

<a id="abschnitt-ablauf"></a>

## Prozessablauf aus Sicht des NB

<Systembild svg={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1004 1270\" width=\"1004\" height=\"1270\" role=\"img\" aria-labelledby=\"sb-title\" class=\"maco-systembild\">\n<title id=\"sb-title\">Systembild: Bestellung einer Konfiguration vom NB an MSB aus Sicht NB</title>\n<defs><marker id=\"sb-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect class=\"sb-lane-kopf\" x=\"16\" y=\"12\" width=\"232\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend-System des Kunden</text>\n<rect class=\"sb-lane-kopf\" x=\"398\" y=\"12\" width=\"264\" height=\"46\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · NB</text>\n<rect class=\"sb-lane-kopf\" x=\"812\" y=\"12\" width=\"176\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"900\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Marktpartner</text>\n<line x1=\"323\" y1=\"58\" x2=\"323\" y2=\"1258\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"737\" y1=\"58\" x2=\"737\" y2=\"1258\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"80\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">1. Anfrage einer</text>\n<text x=\"530\" y=\"115\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Konfiguration auf Ebene der</text>\n<text x=\"530\" y=\"130\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">direkt betroffene…</text>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"93\" r=\"5\"/><line x1=\"900\" y1=\"98\" x2=\"900\" y2=\"110\"/><line x1=\"893\" y1=\"102\" x2=\"907\" y2=\"102\"/><line x1=\"900\" y1=\"110\" x2=\"894\" y2=\"120\"/><line x1=\"900\" y1=\"110\" x2=\"906\" y2=\"120\"/></g>\n<text x=\"900\" y=\"142\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">MSB</text>\n<line x1=\"628\" y1=\"111\" x2=\"878\" y2=\"111\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"103\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"127\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">35004</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"169\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"189\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"143\" x2=\"530\" y2=\"169\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"169\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"189\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"185\" x2=\"230\" y2=\"185\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"177\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"233\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"253\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">2. Angebot zur/ Ablehnung</text>\n<text x=\"530\" y=\"268\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">der Anfrage</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"202\" x2=\"530\" y2=\"233\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"239\" r=\"5\"/><line x1=\"900\" y1=\"244\" x2=\"900\" y2=\"256\"/><line x1=\"893\" y1=\"248\" x2=\"907\" y2=\"248\"/><line x1=\"900\" y1=\"256\" x2=\"894\" y2=\"266\"/><line x1=\"900\" y1=\"256\" x2=\"906\" y2=\"266\"/></g>\n<text x=\"900\" y=\"288\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">MSB</text>\n<line x1=\"878\" y1=\"257\" x2=\"628\" y2=\"257\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"249\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"273\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">15004, 21033</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"316\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"336\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z33</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"281\" x2=\"530\" y2=\"316\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"380\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"400\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"349\" x2=\"530\" y2=\"380\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben sb-abgeleitet\" x=\"34\" y=\"380\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"400\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"396\" x2=\"230\" y2=\"396\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"388\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"444\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"464\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">3. Bestellung einer</text>\n<text x=\"530\" y=\"479\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Konfiguration auf Ebene der</text>\n<text x=\"530\" y=\"494\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">direkt betroff…</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"413\" x2=\"530\" y2=\"444\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"457\" r=\"5\"/><line x1=\"900\" y1=\"462\" x2=\"900\" y2=\"474\"/><line x1=\"893\" y1=\"466\" x2=\"907\" y2=\"466\"/><line x1=\"900\" y1=\"474\" x2=\"894\" y2=\"484\"/><line x1=\"900\" y1=\"474\" x2=\"906\" y2=\"484\"/></g>\n<text x=\"900\" y=\"506\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">MSB</text>\n<line x1=\"628\" y1=\"475\" x2=\"878\" y2=\"475\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"467\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"491\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">17131</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"533\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"553\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"507\" x2=\"530\" y2=\"533\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"533\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"553\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"549\" x2=\"230\" y2=\"549\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"541\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-lesen_verarbeitung\" x=\"432\" y=\"597\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"617\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Daten für die Verarbeitung</text>\n<text x=\"530\" y=\"632\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">laden</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"566\" x2=\"530\" y2=\"597\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-lesen_verarbeitung\" x=\"34\" y=\"597\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"617\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">4 Lese-Schnittstellen</text>\n<text x=\"132\" y=\"632\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">aufgerufen</text>\n<line x1=\"432\" y1=\"621\" x2=\"230\" y2=\"621\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"613\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<text x=\"331\" y=\"637\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">je einzeln am Schritt</text>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"671\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"691\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">4. Bestellung einer</text>\n<text x=\"530\" y=\"706\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Konfiguration auf Ebene der</text>\n<text x=\"530\" y=\"721\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">direkt betroff…</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"645\" x2=\"530\" y2=\"671\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"684\" r=\"5\"/><line x1=\"900\" y1=\"689\" x2=\"900\" y2=\"701\"/><line x1=\"893\" y1=\"693\" x2=\"907\" y2=\"693\"/><line x1=\"900\" y1=\"701\" x2=\"894\" y2=\"711\"/><line x1=\"900\" y1=\"701\" x2=\"906\" y2=\"711\"/></g>\n<text x=\"900\" y=\"733\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">MSB</text>\n<line x1=\"628\" y1=\"702\" x2=\"878\" y2=\"702\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"694\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"718\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">17130, 17121</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"760\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"780\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"734\" x2=\"530\" y2=\"760\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"760\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"780\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"776\" x2=\"230\" y2=\"776\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"768\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"824\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"844\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">5. Mitteilung zum weiteren</text>\n<text x=\"530\" y=\"859\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgehen zur Bestellung</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"793\" x2=\"530\" y2=\"824\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"830\" r=\"5\"/><line x1=\"900\" y1=\"835\" x2=\"900\" y2=\"847\"/><line x1=\"893\" y1=\"839\" x2=\"907\" y2=\"839\"/><line x1=\"900\" y1=\"847\" x2=\"894\" y2=\"857\"/><line x1=\"900\" y1=\"847\" x2=\"906\" y2=\"857\"/></g>\n<text x=\"900\" y=\"879\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">MSB</text>\n<line x1=\"878\" y1=\"848\" x2=\"628\" y2=\"848\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"840\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"864\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">19132, 19120</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"907\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"927\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z33</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"872\" x2=\"530\" y2=\"907\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"971\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"991\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"940\" x2=\"530\" y2=\"971\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben sb-abgeleitet\" x=\"34\" y=\"971\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"991\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"987\" x2=\"230\" y2=\"987\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"979\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"1035\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1055\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">9. Antwort auf Bestellung</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1004\" x2=\"530\" y2=\"1035\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"1033\" r=\"5\"/><line x1=\"900\" y1=\"1038\" x2=\"900\" y2=\"1050\"/><line x1=\"893\" y1=\"1042\" x2=\"907\" y2=\"1042\"/><line x1=\"900\" y1=\"1050\" x2=\"894\" y2=\"1060\"/><line x1=\"900\" y1=\"1050\" x2=\"906\" y2=\"1060\"/></g>\n<text x=\"900\" y=\"1082\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">MSB</text>\n<line x1=\"878\" y1=\"1051\" x2=\"628\" y2=\"1051\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"1043\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"1067\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">21043</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"1118\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1138\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z33</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1068\" x2=\"530\" y2=\"1118\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"1182\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1202\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1151\" x2=\"530\" y2=\"1182\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben sb-abgeleitet\" x=\"34\" y=\"1182\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"1202\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"1198\" x2=\"230\" y2=\"1198\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"1190\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n</svg>"} gesamt={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 974 1106\" width=\"974\" height=\"1106\" role=\"img\" aria-labelledby=\"sd-title\" class=\"maco-sequence\">\n<title id=\"sd-title\">Sequenzdiagramm: Bestellung einer Konfiguration vom NB an MSB aus Sicht NB</title>\n<defs><marker id=\"sd-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect x=\"16\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"121\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend (Kunde)</text>\n<line x1=\"121\" y1=\"64\" x2=\"121\" y2=\"1094\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"260\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"365\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · NB</text>\n<line x1=\"365\" y1=\"64\" x2=\"365\" y2=\"1094\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"504\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"609\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">MSB</text>\n<line x1=\"609\" y1=\"64\" x2=\"609\" y2=\"1094\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"748\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"853\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">weiterer MSB</text>\n<line x1=\"853\" y1=\"64\" x2=\"853\" y2=\"1094\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"365\" y1=\"90\" x2=\"609\" y2=\"90\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"81\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">1. Anfrage einer Konfiguration auf Ebene der dir…</text>\n<text x=\"487\" y=\"105\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 35004</text>\n<line x1=\"365\" y1=\"152\" x2=\"121\" y2=\"152\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"143\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"167\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"609\" y1=\"214\" x2=\"365\" y2=\"214\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"205\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">2. Angebot zur/ Ablehnung der Anfrage</text>\n<text x=\"487\" y=\"229\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 15004, 21033 · E_0524</text>\n<text x=\"487\" y=\"242\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0524 — Anfrage prüfen</text>\n<line x1=\"365\" y1=\"276\" x2=\"121\" y2=\"276\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"267\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"291\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"365\" y1=\"338\" x2=\"609\" y2=\"338\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"329\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">3. Bestellung einer Konfiguration auf Ebene der…</text>\n<text x=\"487\" y=\"353\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 17131</text>\n<line x1=\"365\" y1=\"400\" x2=\"121\" y2=\"400\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"391\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"415\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"365\" y1=\"462\" x2=\"609\" y2=\"462\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"453\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">4. Bestellung einer Konfiguration auf Ebene der…</text>\n<text x=\"487\" y=\"477\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 17130, 17121</text>\n<line x1=\"365\" y1=\"524\" x2=\"121\" y2=\"524\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"515\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"539\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"609\" y1=\"586\" x2=\"365\" y2=\"586\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"577\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">5. Mitteilung zum weiteren Vorgehen zur Bestellu…</text>\n<text x=\"487\" y=\"601\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 19132, 19120 · E_0526</text>\n<text x=\"487\" y=\"614\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0526 — Bestellung prüfen</text>\n<line x1=\"365\" y1=\"648\" x2=\"121\" y2=\"648\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"639\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"663\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"609\" y1=\"710\" x2=\"853\" y2=\"710\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"731\" y=\"701\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">6. Bestellung einer Konfiguration für weiter bet…</text>\n<text x=\"731\" y=\"725\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 17130, 17118</text>\n<line x1=\"853\" y1=\"772\" x2=\"609\" y2=\"772\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"731\" y=\"763\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">7. Mitteilung zum weiteren Vorgehen zur Bestellu…</text>\n<text x=\"731\" y=\"787\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 19132, 19127 · E_0527</text>\n<text x=\"731\" y=\"800\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0527 — Bestellung</text>\n<line x1=\"609\" y1=\"834\" x2=\"853\" y2=\"834\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"731\" y=\"825\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">8. Antwort auf Bestellung</text>\n<text x=\"731\" y=\"849\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 21043 · E_0528</text>\n<text x=\"731\" y=\"862\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0528 — Umsetzung der Konfiguration prüfen</text>\n<line x1=\"609\" y1=\"896\" x2=\"365\" y2=\"896\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"887\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">9. Antwort auf Bestellung</text>\n<text x=\"487\" y=\"911\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 21043 · E_0529</text>\n<text x=\"487\" y=\"924\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0529 — Bewertung des Gesamtvorgangs</text>\n<line x1=\"365\" y1=\"958\" x2=\"121\" y2=\"958\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"949\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"973\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"609\" y1=\"1020\" x2=\"853\" y2=\"1020\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"731\" y=\"1011\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">10. Mitteilung über Gesamtvorgang</text>\n<text x=\"731\" y=\"1035\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 21043 · E_0529</text>\n<text x=\"731\" y=\"1048\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0529 — Bewertung des Gesamtvorgangs</text>\n</svg>"} titel="NB" />

<a id="abschnitt-schritte"></a>

## Prozessschritte

<Schritt nr="1" anker="schritt-1" richtung="ausgehend" kopf={{"links": {"label": "NB", "eigen": true}, "rechts": {"label": "MSB"}}}>

### Anfrage einer Konfiguration auf Ebene der direkt betroffenen Lokation

<Schrittskizze sicht={{"label": "NB"}} zeilen={[{"art": "senden", "label": "MSB", "weg": "AS4", "nachrichten": [{"nr": "35004", "titel": "Anfrage einer Konfiguration"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [35004](/schnittstellen/202610/pruefi/REQOTE/PI_35004) — Anfrage einer Konfiguration · AS4

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
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202610/backend-schreiben-nb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"ANFRAGE\": [\n      {\n        \"anfragetyp\": \"AENDERUNG_KONFIGURATION\",\n        \"boTyp\": \"ANFRAGE\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"LEISTUNGSKURVENDEFINITION\": [\n      {\n        \"boTyp\": \"LEISTUNGSKURVENDEFINITION\",\n        \"leistungskurven\": [\n          {\n            \"code\": \"MMA\",\n            \"konfigurationsprodukt\": \"9991000000721\"\n          }\n        ],\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"MARKTLOKATION\": [\n      {\n        \"boTyp\": \"MARKTLOKATION\",\n        \"marktlokationsId\": \"50444001616\",\n        \"marktlokationsTyp\": [\n          {\n            \"typ\": \"STANDARD_MARKTLOKATION\"\n          }\n        ],\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"ansprechpartner\": {\n        \"boTyp\": \"ANSPRECHPARTNER\",\n        \"eMailAdresse\": \"Max.Mustermann@conuti.de\",\n        \"nachname\": \"Max Mustermann\",\n        \"versionStruktur\": \"1\"\n      },\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9900496000001\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"datenaustauschreferenz\": \"M3VQCXCY\",\n    \"dokumentennummer\": \"BGMM3TJAKY3\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9900496000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"Z82\",\n    \"lieferdatum\": \"2025-01-05T23:00:00Z\",\n    \"nachrichtenReferenzBestellbestaetigung\": \"BGMM44X6WGM\",\n    \"nachrichtendatum\": \"2026-10-01T11:00:00Z\",\n    \"nachrichtenreferenznummer\": \"UNHM3Q4M8YM\",\n    \"positionsnummer\": 1,\n    \"pruefidentifikator\": \"35004\",\n    \"sparte\": \"STROM\",\n    \"vorgangsReferenzBestellbestaetigung\": \"45261\"\n  },\n  \"zusatzdaten\": {}\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend fort, nachdem die Nachricht erstellt ist.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="2" anker="schritt-2" richtung="eingehend" kopf={{"links": {"label": "NB", "eigen": true}, "rechts": {"label": "MSB"}}}>

### Angebot zur/ Ablehnung der Anfrage

<Schrittskizze sicht={{"label": "NB"}} zeilen={[{"art": "empfangen", "label": "MSB", "weg": "AS4", "nachrichten": [{"nr": "15004", "titel": "Angebot  einer Konfiguration"}, {"nr": "21033", "titel": "Ablehnung der Anfrage"}]}, {"art": "aperak", "werte": ["Z33"]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [15004](/schnittstellen/202610/pruefi/QUOTES/PI_15004) — Angebot  einer Konfiguration · AS4
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
- `21033` → [E_0524](/referenz/202610/ebd/E_0524) · MSB · Anfrage prüfen

</div>

</li>

<li data-teil="aperak">

**Aperak-Prüfungen**
- `15004`, `21033` → `Z33`

</li>

<li data-teil="schnittstelle" data-art="fortschreiben" data-abgeleitet="ja">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202610/backend-schreiben-nb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"ANFRAGE\": [\n      {\n        \"anfragetyp\": \"NEUKONFIGURATION\",\n        \"boTyp\": \"ANFRAGE\",\n        \"lokationsId\": \"50074561188\",\n        \"lokationsTyp\": \"MALO\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"ANGEBOT\": [\n      {\n        \"anfragereferenz\": \"AVV12345\",\n        \"boTyp\": \"ANGEBOT\",\n        \"positionsdaten\": [\n          {\n            \"artikelId\": [\n              \"9991000000721-01\",\n              \"9991000000721-02\",\n              \"9991000000721-03\"\n            ],\n            \"positionsbezeichnung\": \"1\"\n          }\n        ],\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"LEISTUNGSKURVENDEFINITION\": [\n      {\n        \"boTyp\": \"LEISTUNGSKURVENDEFINITION\",\n        \"leistungskurven\": [\n          {\n            \"code\": \"NBF\",\n            \"konfigurationsprodukt\": \"9991000000721\"\n          }\n        ],\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"MARKTLOKATION\": [\n      {\n        \"boTyp\": \"MARKTLOKATION\",\n        \"marktlokationsId\": \"50074561188\",\n        \"marktlokationsTyp\": [\n          {\n            \"typ\": \"STANDARD_MARKTLOKATION\"\n          }\n        ],\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"ansprechpartner\": {\n        \"boTyp\": \"ANSPRECHPARTNER\",\n        \"nachname\": \"Max Mustermann\",\n        \"rufnummern\": [\n          {\n            \"nummerntyp\": \"FAX_DURCHWAHL\",\n            \"rufnummer\": \"+001234567\"\n          }\n        ],\n        \"versionStruktur\": \"1\"\n      },\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9904446000007\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"datenaustauschreferenz\": \"MCH0IOL1\",\n    \"dokumentennummer\": \"BGMMC2WCO3K\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9903790000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"Z74\",\n    \"nachrichtendatum\": \"2026-10-01T11:00:00Z\",\n    \"nachrichtenreferenznummer\": \"UNHMC75CA7G\",\n    \"pruefidentifikator\": \"15004\",\n    \"sparte\": \"STROM\"\n  },\n  \"zusatzdaten\": {}\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend mit den Daten der eingegangenen Nachricht fort.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="3" anker="schritt-3" richtung="ausgehend" kopf={{"links": {"label": "NB", "eigen": true}, "rechts": {"label": "MSB"}}}>

### Bestellung einer Konfiguration auf Ebene der direkt betroffenen Lokation

<Schrittskizze sicht={{"label": "NB"}} zeilen={[{"art": "senden", "label": "MSB", "weg": "AS4", "nachrichten": [{"nr": "17131", "titel": "Bestellung Angebot einer Konfiguration"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [17131](/schnittstellen/202610/pruefi/ORDERS/PI_17131) — Bestellung Angebot einer Konfiguration · AS4

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
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202610/backend-schreiben-nb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"ANFRAGE\": [\n      {\n        \"anfragekategorie\": \"BESTELLUNG_EINES_ANGEBOTS_EINER_KONFIGURATION\",\n        \"boTyp\": \"ANFRAGE\",\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"marktrolle\": \"LF\",\n      \"rollencodenummer\": \"9979309000006\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"angebotsnummer\": \"12474\",\n    \"datenaustauschreferenz\": \"M03UGIN5\",\n    \"dokumentennummer\": \"M0ACK2J3\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9904733000009\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"nachrichtendatum\": \"2026-10-01T11:00:00Z\",\n    \"nachrichtenreferenznummer\": \"M01KAXGA\",\n    \"pruefidentifikator\": \"17131\",\n    \"sparte\": \"STROM\"\n  },\n  \"zusatzdaten\": {}\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend fort, nachdem die Nachricht erstellt ist.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="4" anker="schritt-4" richtung="ausgehend" kopf={{"links": {"label": "NB", "eigen": true}, "rechts": {"label": "MSB"}}}>

### Bestellung einer Konfiguration auf Ebene der direkt betroffenen Lokation

<Schrittskizze sicht={{"label": "NB"}} zeilen={[{"art": "lesen_verarbeitung", "schnittstellen": [{"label": "LESEN_ANFRAGE_BASIS"}, {"label": "LESEN_AUFTRAG_BASIS"}, {"label": "Netzlokation lesen"}, {"label": "Marktlokation lesen"}]}, {"art": "senden", "label": "MSB", "weg": "AS4", "nachrichten": [{"nr": "17130", "titel": "Bestellung einer Konfiguration"}, {"nr": "17121", "titel": "Bestellung Änderung"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [17130](/schnittstellen/202610/pruefi/ORDERS/PI_17130) — Bestellung einer Konfiguration · AS4
- [17121](/schnittstellen/202610/pruefi/ORDERS/PI_17121) — Bestellung Änderung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="lesen" data-stufe="verarbeitung">

**Daten für die Verarbeitung laden**
- `LESEN_ANFRAGE_BASIS`
- `LESEN_AUFTRAG_BASIS`
- [Netzlokation lesen](/api/202610/backend-lesen/getgridlocationbasic#netzlokation-lesen) `GET /getGridLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getGridLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_NETZLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Marktlokation lesen](/api/202610/backend-lesen/getmarketlocationbasic#marktlokation-lesen) `GET /getMarketLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getMarketLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": false, "defaultValue": "MALO", "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": false, "defaultValue": "2024-06-28T12:18:00Z", "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_MARKTLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

</li>

<li data-teil="nachricht">

Nachricht an **MSB** · AS4

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202610/backend-schreiben-nb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"ANFRAGE\": [\n      {\n        \"anfragekategorie\": \"BESTELLUNG_EINER_KONFIGURATION\",\n        \"boTyp\": \"ANFRAGE\",\n        \"lokationsId\": \"C4897654121\",\n        \"lokationsTyp\": \"STEUERBARE_RESSOURCE\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"AUFTRAG\": [\n      {\n        \"boTyp\": \"AUFTRAG\",\n        \"positionsdaten\": [\n          {\n            \"positionsnummer\": 1\n          }\n        ],\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"SCHALTZEITDEFINITION\": [\n      {\n        \"boTyp\": \"SCHALTZEITDEFINITION\",\n        \"schaltzeiten\": [\n          {\n            \"code\": \"AAL\",\n            \"konfigurationsprodukt\": \"9991000000713\"\n          }\n        ],\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"STEUERBARE_RESSOURCE\": [\n      {\n        \"boTyp\": \"STEUERBARE_RESSOURCE\",\n        \"ressourcenId\": \"C4897654121\",\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"marktrolle\": \"LF\",\n      \"rollencodenummer\": \"9903111000003\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"beteiligterMarktpartner\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9903111000003\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"datenaustauschreferenz\": \"M0OU3NLP\",\n    \"dokumentennummer\": \"M0O1YVAK\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9904629000006\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"nachrichtendatum\": \"2026-10-01T11:00:00Z\",\n    \"nachrichtenreferenznummer\": \"M08MHOSC\",\n    \"pruefidentifikator\": \"17130\",\n    \"sparte\": \"STROM\",\n    \"vorgangsreferenznummer\": \"AS1234\"\n  },\n  \"zusatzdaten\": {}\n}"} examples={[{"mediaType": "application/json", "examples": [{"name": "17130", "summary": "17130 — Bestellung einer Konfiguration", "value": {"stammdaten": {"ANFRAGE": [{"boTyp": "ANFRAGE", "versionStruktur": "1", "anfragekategorie": "BESTELLUNG_EINER_KONFIGURATION", "lokationsId": "C4897654121", "lokationsTyp": "STEUERBARE_RESSOURCE"}], "AUFTRAG": [{"boTyp": "AUFTRAG", "versionStruktur": "1", "positionsdaten": [{"positionsnummer": 1}]}], "STEUERBARE_RESSOURCE": [{"boTyp": "STEUERBARE_RESSOURCE", "versionStruktur": "1", "ressourcenId": "C4897654121"}], "SCHALTZEITDEFINITION": [{"boTyp": "SCHALTZEITDEFINITION", "versionStruktur": "1", "schaltzeiten": [{"code": "AAL", "konfigurationsprodukt": "9991000000713"}]}]}, "transaktionsdaten": {"datenaustauschreferenz": "M0OU3NLP", "sparte": "STROM", "pruefidentifikator": "17130", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "marktrolle": "LF", "rollencodenummer": "9903111000003", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9904629000006", "rollencodetyp": "BDEW"}, "dokumentennummer": "M0O1YVAK", "nachrichtendatum": "2026-10-01T11:00:00Z", "nachrichtenreferenznummer": "M08MHOSC", "vorgangsreferenznummer": "AS1234", "beteiligterMarktpartner": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9903111000003", "rollencodetyp": "BDEW"}}, "zusatzdaten": {}}}, {"name": "17121", "summary": "17121 — Bestellung Änderung", "value": {"stammdaten": {"ANFRAGE": [{"boTyp": "ANFRAGE", "versionStruktur": "1", "anfragekategorie": "AENDERUNG", "energierichtung": "AUSSP", "lokationsId": "44897654121", "lokationsTyp": "MALO"}], "AUFTRAG": [{"boTyp": "AUFTRAG", "versionStruktur": "1", "ausfuehrungsdatum": "2026-09-29T22:00:00Z", "positionsdaten": [{"positionsnummer": 1, "lokationsId": "44897654121", "lokationsTyp": "MALO"}]}], "MARKTLOKATION": [{"boTyp": "MARKTLOKATION", "versionStruktur": "1", "marktlokationsId": "44897654121", "zaehlwerke": [{"messprodukt": "9991000000044", "verwendungszweckNB": "V01", "verwendungszweckLF": "V01", "verwendungszweckUENB": "V15", "zaehlzeiten": {"zaehlzeitDefinition": "Aal"}}]}]}, "transaktionsdaten": {"datenaustauschreferenz": "M0LI678W", "sparte": "STROM", "pruefidentifikator": "17121", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9900259000002", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9904629000006", "rollencodetyp": "BDEW"}, "dokumentennummer": "M05AQP3S", "nachrichtendatum": "2026-10-01T11:00:00Z", "nachrichtenreferenznummer": "M0V0OCVO"}, "zusatzdaten": {}}}]}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend fort, nachdem die Nachricht erstellt ist.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="5" anker="schritt-5" richtung="eingehend" kopf={{"links": {"label": "NB", "eigen": true}, "rechts": {"label": "MSB"}}}>

### Mitteilung zum weiteren Vorgehen zur Bestellung

<Schrittskizze sicht={{"label": "NB"}} zeilen={[{"art": "empfangen", "label": "MSB", "weg": "AS4", "nachrichten": [{"nr": "19132", "titel": "Mitteilung zur Bestellung Konfiguration"}, {"nr": "19120", "titel": "Mitteilung zur Änderung"}]}, {"art": "aperak", "werte": ["Z33"]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [19132](/schnittstellen/202610/pruefi/ORDRSP/PI_19132) — Mitteilung zur Bestellung Konfiguration · AS4
- [19120](/schnittstellen/202610/pruefi/ORDRSP/PI_19120) — Mitteilung zur Änderung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **MSB** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `19132`, `19120` → [E_0526](/referenz/202610/ebd/E_0526) · MSB · Bestellung prüfen

</div>

</li>

<li data-teil="aperak">

**Aperak-Prüfungen**
- `19132`, `19120` → `Z33`

</li>

<li data-teil="schnittstelle" data-art="fortschreiben" data-abgeleitet="ja">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202610/backend-schreiben-nb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend mit den Daten der eingegangenen Nachricht fort.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="6" anker="schritt-6" richtung="fremd" kopf={{"links": {"label": "MSB", "eigen": false}, "rechts": {"label": "weiterer MSB"}}}>

### Bestellung einer Konfiguration für weiter betroffene Lokationen

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [17130](/schnittstellen/202610/pruefi/ORDERS/PI_17130) — Bestellung einer Konfiguration · AS4
- [17118](/schnittstellen/202610/pruefi/ORDERS/PI_17118) — Bestellung einer Konfigurationsänderung · AS4

</div>

</Schritt>

<Schritt nr="7" anker="schritt-7" richtung="fremd" kopf={{"links": {"label": "weiterer MSB", "eigen": false}, "rechts": {"label": "MSB"}}}>

### Mitteilung zum weiteren Vorgehen zur Bestellung

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [19132](/schnittstellen/202610/pruefi/ORDRSP/PI_19132) — Mitteilung zur Bestellung Konfiguration · AS4
- [19127](/schnittstellen/202610/pruefi/ORDRSP/PI_19127) — Mitteilung zur Konfigurationsänderung · AS4

</div>

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `19132`, `19127` → [E_0527](/referenz/202610/ebd/E_0527) · MSB · Bestellung

</div>

</Schritt>

<Schritt nr="8" anker="schritt-8" richtung="fremd" kopf={{"links": {"label": "MSB", "eigen": false}, "rechts": {"label": "weiterer MSB"}}}>

### Antwort auf Bestellung

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [21043](/schnittstellen/202610/pruefi/IFTSTA/PI_21043) — Bestellungsantwort / -mitteilung · AS4

</div>

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `21043` → [E_0528](/referenz/202610/ebd/E_0528) · MSB · Umsetzung der Konfiguration prüfen

</div>

</Schritt>

<Schritt nr="9" anker="schritt-9" richtung="eingehend" kopf={{"links": {"label": "NB", "eigen": true}, "rechts": {"label": "MSB"}}}>

### Antwort auf Bestellung

<Schrittskizze sicht={{"label": "NB"}} zeilen={[{"art": "empfangen", "label": "MSB", "weg": "AS4", "nachrichten": [{"nr": "21043", "titel": "Bestellungsantwort / -mitteilung"}]}, {"art": "aperak", "werte": ["Z33"]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [21043](/schnittstellen/202610/pruefi/IFTSTA/PI_21043) — Bestellungsantwort / -mitteilung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **MSB** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `21043` → [E_0529](/referenz/202610/ebd/E_0529) · MSB · Bewertung des Gesamtvorgangs

</div>

</li>

<li data-teil="aperak">

**Aperak-Prüfungen**
- `21043` → `Z33`

</li>

<li data-teil="schnittstelle" data-art="fortschreiben" data-abgeleitet="ja">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202610/backend-schreiben-nb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend mit den Daten der eingegangenen Nachricht fort.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="10" anker="schritt-10" richtung="fremd" kopf={{"links": {"label": "MSB", "eigen": false}, "rechts": {"label": "weiterer MSB"}}}>

### Mitteilung über Gesamtvorgang

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [21043](/schnittstellen/202610/pruefi/IFTSTA/PI_21043) — Bestellungsantwort / -mitteilung · AS4

</div>

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `21043` → [E_0529](/referenz/202610/ebd/E_0529) · MSB · Bewertung des Gesamtvorgangs

</div>

</Schritt>

<details>
<summary>Entscheidungsbäume dieses Prozesses</summary>

| EBD | Name |
|---|---|
| [E_0524](/referenz/202610/ebd/E_0524) | Anfrage prüfen |
| [E_0526](/referenz/202610/ebd/E_0526) | Bestellung prüfen |
| [E_0529](/referenz/202610/ebd/E_0529) | Bewertung des Gesamtvorgangs |
| [E_0527](/referenz/202610/ebd/E_0527) | Bestellung |
| [E_0528](/referenz/202610/ebd/E_0528) | Umsetzung der Konfiguration prüfen |

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
  - Im Fall der Bestellung einer Konfiguration vom LF an den NB: Der NB hat vom LF eine Bestellung der Konfiguration über den Use-Case „[Bestellung einer Konfiguration vom LF an NB](/prozessdoku/202610/NB/GPKE-Teil3-bestellung-einer-konfiguration-vom-lf-an-nb)“ (z.B. die Bestellung einer Änderung des Bilanzierungsverfahrens oder Bestellung einer Konfiguration, für die eine Zählzeitdefinition des NB erforderlich ist) erhalten, bei der die Einrichtung der Konfiguration aus Sicht des NB grundsätzlich möglich ist.
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

- Sofern die Konfiguration für alle betroffenen Lokationen erfolgreich eingerichtet wurde, führt der MSB der jeweils betroffenen Lokation den Use-Case „Stammdatenänderung“ (hier: SD „[Stammdatenänderung vom MSB (verantwortlich) ausgehend](/prozessdoku/202610/NB/GPKE-Teil4-stammdatenaenderung-vom-msb-verantwortlich-ausgehend)“) (GPKE Teil 4) durch, sofern für die jeweilige Lokation eine Stammdatenänderung aufgrund der Einrichtung der Konfiguration erforderlich ist.
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
- Konfigurationen des NB werden im Use-Case „[Beginn Messstellenbetrieb](/prozessdoku/202610/NB/WiM-Teil1-beginn-messstellenbetrieb)“ (WiM Teil 1) in Prozessschritt 2 im Rahmen der Mindestparameter für die Messlokation(en) vom NB dem MSB mitgeteilt. Eine Bestellung einer in den Mindestparametern enthaltenen Konfiguration ist nicht über den hier beschriebenen Use-Case notwendig. Ergänzend zu den in den Mindestparametern mitgeteilten Konfigurationen, kann der NB mit Hilfe des hier beschriebenen Use-Cases eine Bestellung einer Konfiguration an den zukünftigen MSB übermitteln. Hinweis: Wird dem MSB im Rahmen der Mindestparameter im Use-Case „[Beginn Messstellenbetrieb](/prozessdoku/202610/NB/WiM-Teil1-beginn-messstellenbetrieb)“ (WiM Teil 1) eine Zählzeitdefinition des NB mitgeteilt, die der MSB vorab nicht über den Use-Case „[Übermittlung einer Definition des NB durch den NB](/prozessdoku/202610/NB/GPKE-Teil3-uebermittlung-einer-definition-des-nb-durch-den-nb)“ übermittelt bekommen hat, so ist die Energie in einem Register an der/den Messlokation(en) und der zugehörigen Marktlokation für den Zählzeitenanwendungszweck „Netznutzung“ zu erfassen.

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

Der Beteiligte dieser Seite sendet selbst: „Anfrage einer Konfiguration auf Ebene der direkt betroffenen Lokation“ an **MSB** (Schritt 1).

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

- [Sicht MSB](/prozessdoku/202610/MSB/GPKE-Teil3-bestellung-einer-konfiguration-vom-nb-an-msb) — MSB
- [Sicht WMSB](/prozessdoku/202610/MSB--WMSB/GPKE-Teil3-bestellung-einer-konfiguration-vom-nb-an-msb) — weiterer Messstellenbetreiber · Marktrolle MSB

<Hinweisbereich>

*Die Schritte sind die **möglichen** Nachrichten dieses Prozesses, keine Abfolge — die Quelle führt weder Bedingungen noch Alternativen. Das Kästchen am Schritt nennt links die eigene Sicht: **←** empfängt sie, **→** sendet sie. Zugeklappte Schritte laufen zwischen anderen Marktpartnern.*

Welches Ereignis diese Schritte anstößt, benennt die Quelle noch nicht.

Betrifft: [1](#schritt-1)

Diese Lesezugriffe sind im API-Katalog dieser Formatversion nicht geführt; am Schritt steht deshalb nur ihr Kommando, ohne Adresse und ohne Knopf.

Betrifft: [4](#schritt-4)

Die Konnektortabelle führt für diese Schritte keinen Schreibaufruf. Abgeleitet aus dem Prozessverlauf: Die eigene Rolle war an diesem Prozess schon beteiligt, der Vorgang besteht also.

Betrifft: [2](#schritt-2), [5](#schritt-5), [9](#schritt-9)

Zu den Prüfidentifikatoren dieser Schritte liegt kein Testfall im Testbestand; der Knopf »Ausprobieren« der schreibenden Schnittstelle bietet deshalb keinen Rumpf an.

Betrifft: [5](#schritt-5), [9](#schritt-9)

</Hinweisbereich>
