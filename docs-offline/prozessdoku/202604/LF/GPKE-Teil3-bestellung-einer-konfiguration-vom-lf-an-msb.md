# Bestellung einer Konfiguration vom LF an MSB — Sicht LF

<Kopf rolle="LF" beteiligter="LF" festlegung="GPKE" dokument="GPKE Teil 3" kapitel="1.3.3.3" sparte="Strom" schritte={10} suchtitel="Bestellung einer Konfiguration vom LF an MSB — Sicht LF · GPKE Teil 3 · Formatversion 202604" abschnitte={[{"id": "abschnitt-ablauf", "label": "Prozessablauf"}, {"id": "abschnitt-schritte", "label": "Prozessschritte"}, {"id": "abschnitt-informationen", "label": "Prozess-Informationen"}, {"id": "abschnitt-sichten", "label": "Andere Sichten des Prozesses"}]} />

<Kurzfassung>

Der NB bzw. LF bestellt beim MSB der direkt betroffenen Lokation eine Konfiguration für die direkt betroffene Lokation. Sofern weitere Lokationen der direkt betroffenen Lokation von der Konfiguration betroffen sind, gibt der NB bzw. LF diese weiter betroffenen Lokationen in der Bestellung ebenfalls an (z.B. hat der NB in der Bestellung der Änderung des Bilanzierungsverfahrens auf der Ebene der Marktlokation, neben der Marktlokation auch alle Messlokationen der Marktlokation beim MSB der Marktlokation zu bestellen). Bevor eine kostenpflichtige Bestellung erfolgen kann, hat der NB bzw. LF ein Angebot beim MSB der direkt betroffenen Lokation für die Einrichtung der Konfiguration anzufragen. Der MSB prüft die Bestellung und teilt dem NB bzw. LF das weitere Vorgehen zur Bestellung mit. Sofern weitere Lokationen der direkt betroffenen Lokation von der Konfiguration betroffen sind, für die der MSB der direkt betroffenen Lokation nicht den Messstellenbetrieb durchführt, bindet er für diese weiter betroffenen Lokationen die jeweiligen weiteren MSB ein.

</Kurzfassung>

<a id="abschnitt-ablauf"></a>

## Prozessablauf aus Sicht des LF

<Systembild svg={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1004 1408\" width=\"1004\" height=\"1408\" role=\"img\" aria-labelledby=\"sb-title\" class=\"maco-systembild\">\n<title id=\"sb-title\">Systembild: Bestellung einer Konfiguration vom LF an MSB aus Sicht LF</title>\n<defs><marker id=\"sb-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect class=\"sb-lane-kopf\" x=\"16\" y=\"12\" width=\"232\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend-System des Kunden</text>\n<rect class=\"sb-lane-kopf\" x=\"398\" y=\"12\" width=\"264\" height=\"46\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · LF</text>\n<rect class=\"sb-lane-kopf\" x=\"812\" y=\"12\" width=\"176\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"900\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Marktpartner</text>\n<line x1=\"323\" y1=\"58\" x2=\"323\" y2=\"1396\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"737\" y1=\"58\" x2=\"737\" y2=\"1396\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect class=\"sb-kasten sb-trigger\" x=\"432\" y=\"80\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessauslöser empfangen</text>\n<rect class=\"sb-kasten sb-backend sb-trigger\" x=\"34\" y=\"72\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"92\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">START_ANFRAGE_KONFIGUR</text>\n<text x=\"132\" y=\"107\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">ATION</text>\n<line x1=\"230\" y1=\"96\" x2=\"432\" y2=\"96\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"88\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"154\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"174\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">1. Anfrage einer</text>\n<text x=\"530\" y=\"189\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Konfiguration auf Ebene der</text>\n<text x=\"530\" y=\"204\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">direkt betroffene…</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"113\" x2=\"530\" y2=\"154\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"167\" r=\"5\"/><line x1=\"900\" y1=\"172\" x2=\"900\" y2=\"184\"/><line x1=\"893\" y1=\"176\" x2=\"907\" y2=\"176\"/><line x1=\"900\" y1=\"184\" x2=\"894\" y2=\"194\"/><line x1=\"900\" y1=\"184\" x2=\"906\" y2=\"194\"/></g>\n<text x=\"900\" y=\"216\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">MSB</text>\n<line x1=\"628\" y1=\"185\" x2=\"878\" y2=\"185\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"177\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"201\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">35004</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"243\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"263\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"217\" x2=\"530\" y2=\"243\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"243\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"263\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"259\" x2=\"230\" y2=\"259\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"251\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"307\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"327\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">2. Angebot zur / Ablehnung</text>\n<text x=\"530\" y=\"342\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">der Anfrage</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"276\" x2=\"530\" y2=\"307\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"313\" r=\"5\"/><line x1=\"900\" y1=\"318\" x2=\"900\" y2=\"330\"/><line x1=\"893\" y1=\"322\" x2=\"907\" y2=\"322\"/><line x1=\"900\" y1=\"330\" x2=\"894\" y2=\"340\"/><line x1=\"900\" y1=\"330\" x2=\"906\" y2=\"340\"/></g>\n<text x=\"900\" y=\"362\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">MSB</text>\n<line x1=\"878\" y1=\"331\" x2=\"628\" y2=\"331\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"323\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"347\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">15004, 21033</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"390\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"410\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z33</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"355\" x2=\"530\" y2=\"390\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-schreiben\" x=\"432\" y=\"454\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"474\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"423\" x2=\"530\" y2=\"454\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-schreiben\" x=\"34\" y=\"454\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"474\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten erstellen</text>\n<line x1=\"432\" y1=\"470\" x2=\"230\" y2=\"470\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"462\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"518\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"538\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">3. Bestellung einer</text>\n<text x=\"530\" y=\"553\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Konfiguration auf Ebene der</text>\n<text x=\"530\" y=\"568\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">direkt betroff…</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"487\" x2=\"530\" y2=\"518\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"531\" r=\"5\"/><line x1=\"900\" y1=\"536\" x2=\"900\" y2=\"548\"/><line x1=\"893\" y1=\"540\" x2=\"907\" y2=\"540\"/><line x1=\"900\" y1=\"548\" x2=\"894\" y2=\"558\"/><line x1=\"900\" y1=\"548\" x2=\"906\" y2=\"558\"/></g>\n<text x=\"900\" y=\"580\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">MSB</text>\n<line x1=\"628\" y1=\"549\" x2=\"878\" y2=\"549\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"541\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"565\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">17131</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"607\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"627\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"581\" x2=\"530\" y2=\"607\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"607\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"627\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"623\" x2=\"230\" y2=\"623\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"615\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-trigger\" x=\"432\" y=\"671\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"691\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessauslöser empfangen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"640\" x2=\"530\" y2=\"671\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-trigger\" x=\"34\" y=\"671\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"691\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">2 Ereignisse, alternativ</text>\n<line x1=\"230\" y1=\"687\" x2=\"432\" y2=\"687\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"679\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-lesen_verarbeitung\" x=\"432\" y=\"735\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"755\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Daten für die Verarbeitung</text>\n<text x=\"530\" y=\"770\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">laden</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"704\" x2=\"530\" y2=\"735\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-lesen_verarbeitung\" x=\"34\" y=\"743\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"763\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Netzlokation lesen</text>\n<line x1=\"432\" y1=\"759\" x2=\"230\" y2=\"759\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"751\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"809\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"829\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">4. Bestellung einer</text>\n<text x=\"530\" y=\"844\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Konfiguration auf Ebene der</text>\n<text x=\"530\" y=\"859\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">direkt betroff…</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"783\" x2=\"530\" y2=\"809\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"822\" r=\"5\"/><line x1=\"900\" y1=\"827\" x2=\"900\" y2=\"839\"/><line x1=\"893\" y1=\"831\" x2=\"907\" y2=\"831\"/><line x1=\"900\" y1=\"839\" x2=\"894\" y2=\"849\"/><line x1=\"900\" y1=\"839\" x2=\"906\" y2=\"849\"/></g>\n<text x=\"900\" y=\"871\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">MSB</text>\n<line x1=\"628\" y1=\"840\" x2=\"878\" y2=\"840\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"832\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"856\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">17130, 17123</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"898\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"918\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"872\" x2=\"530\" y2=\"898\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"898\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"918\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"914\" x2=\"230\" y2=\"914\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"906\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"962\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"982\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">5. Mitteilung zum weiteren</text>\n<text x=\"530\" y=\"997\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgehen zur Bestellung</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"931\" x2=\"530\" y2=\"962\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"968\" r=\"5\"/><line x1=\"900\" y1=\"973\" x2=\"900\" y2=\"985\"/><line x1=\"893\" y1=\"977\" x2=\"907\" y2=\"977\"/><line x1=\"900\" y1=\"985\" x2=\"894\" y2=\"995\"/><line x1=\"900\" y1=\"985\" x2=\"906\" y2=\"995\"/></g>\n<text x=\"900\" y=\"1017\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">MSB</text>\n<line x1=\"878\" y1=\"986\" x2=\"628\" y2=\"986\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"978\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"1002\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">19132, 19124</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"1045\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1065\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z33</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1010\" x2=\"530\" y2=\"1045\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-schreiben\" x=\"432\" y=\"1109\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1129\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1078\" x2=\"530\" y2=\"1109\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-schreiben\" x=\"34\" y=\"1109\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"1129\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten erstellen</text>\n<line x1=\"432\" y1=\"1125\" x2=\"230\" y2=\"1125\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"1117\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"1173\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1193\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">9. Antwort auf Bestellung</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1142\" x2=\"530\" y2=\"1173\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"1171\" r=\"5\"/><line x1=\"900\" y1=\"1176\" x2=\"900\" y2=\"1188\"/><line x1=\"893\" y1=\"1180\" x2=\"907\" y2=\"1180\"/><line x1=\"900\" y1=\"1188\" x2=\"894\" y2=\"1198\"/><line x1=\"900\" y1=\"1188\" x2=\"906\" y2=\"1198\"/></g>\n<text x=\"900\" y=\"1220\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">MSB</text>\n<line x1=\"878\" y1=\"1189\" x2=\"628\" y2=\"1189\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"1181\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"1205\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">21043</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"1256\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1276\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z33</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1206\" x2=\"530\" y2=\"1256\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-schreiben\" x=\"432\" y=\"1320\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1340\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1289\" x2=\"530\" y2=\"1320\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-schreiben\" x=\"34\" y=\"1320\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"1340\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten erstellen</text>\n<line x1=\"432\" y1=\"1336\" x2=\"230\" y2=\"1336\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"1328\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n</svg>"} gesamt={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 974 1230\" width=\"974\" height=\"1230\" role=\"img\" aria-labelledby=\"sd-title\" class=\"maco-sequence\">\n<title id=\"sd-title\">Sequenzdiagramm: Bestellung einer Konfiguration vom LF an MSB aus Sicht LF</title>\n<defs><marker id=\"sd-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect x=\"16\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"121\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend (Kunde)</text>\n<line x1=\"121\" y1=\"64\" x2=\"121\" y2=\"1218\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"260\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"365\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · LF</text>\n<line x1=\"365\" y1=\"64\" x2=\"365\" y2=\"1218\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"504\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"609\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">MSB</text>\n<line x1=\"609\" y1=\"64\" x2=\"609\" y2=\"1218\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"748\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"853\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">weiterer MSB</text>\n<line x1=\"853\" y1=\"64\" x2=\"853\" y2=\"1218\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"121\" y1=\"90\" x2=\"365\" y2=\"90\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"81\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">START_ANFRAGE_KONFIGURATION</text>\n<text x=\"243\" y=\"105\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Trigger-Event</text>\n<line x1=\"365\" y1=\"152\" x2=\"609\" y2=\"152\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"143\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">1. Anfrage einer Konfiguration auf Ebene der dir…</text>\n<text x=\"487\" y=\"167\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 35004</text>\n<line x1=\"365\" y1=\"214\" x2=\"121\" y2=\"214\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"205\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"229\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"609\" y1=\"276\" x2=\"365\" y2=\"276\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"267\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">2. Angebot zur / Ablehnung der Anfrage</text>\n<text x=\"487\" y=\"291\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 15004, 21033 · E_0531</text>\n<text x=\"487\" y=\"304\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0531 — Anfrage prüfen</text>\n<line x1=\"365\" y1=\"338\" x2=\"121\" y2=\"338\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"329\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<text x=\"243\" y=\"353\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten erstellen</text>\n<line x1=\"365\" y1=\"400\" x2=\"609\" y2=\"400\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"391\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">3. Bestellung einer Konfiguration auf Ebene der…</text>\n<text x=\"487\" y=\"415\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 17131</text>\n<line x1=\"365\" y1=\"462\" x2=\"121\" y2=\"462\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"453\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"477\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"121\" y1=\"524\" x2=\"365\" y2=\"524\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"515\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">2 Ereignisse, alternativ</text>\n<text x=\"243\" y=\"539\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Trigger-Event</text>\n<line x1=\"365\" y1=\"586\" x2=\"609\" y2=\"586\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"577\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">4. Bestellung einer Konfiguration auf Ebene der…</text>\n<text x=\"487\" y=\"601\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 17130, 17123</text>\n<line x1=\"365\" y1=\"648\" x2=\"121\" y2=\"648\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"639\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"663\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"609\" y1=\"710\" x2=\"365\" y2=\"710\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"701\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">5. Mitteilung zum weiteren Vorgehen zur Bestellu…</text>\n<text x=\"487\" y=\"725\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 19132, 19124 · E_0533</text>\n<text x=\"487\" y=\"738\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0533 — Bestellung prüfen</text>\n<line x1=\"365\" y1=\"772\" x2=\"121\" y2=\"772\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"763\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<text x=\"243\" y=\"787\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten erstellen</text>\n<line x1=\"609\" y1=\"834\" x2=\"853\" y2=\"834\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"731\" y=\"825\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">6. Bestellung einer Konfiguration für weiter bet…</text>\n<text x=\"731\" y=\"849\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 17130, 17118</text>\n<line x1=\"853\" y1=\"896\" x2=\"609\" y2=\"896\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"731\" y=\"887\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">7. Mitteilung zum weiteren Vorgehen zur Bestellu…</text>\n<text x=\"731\" y=\"911\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 19132, 19127 · E_0527</text>\n<text x=\"731\" y=\"924\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0527 — Bestellung</text>\n<line x1=\"853\" y1=\"958\" x2=\"609\" y2=\"958\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"731\" y=\"949\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">8. Antwort auf Bestellung</text>\n<text x=\"731\" y=\"973\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 21043 · E_0535</text>\n<text x=\"731\" y=\"986\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0535 — Umsetzung der Konfiguration prüfen</text>\n<line x1=\"609\" y1=\"1020\" x2=\"365\" y2=\"1020\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"1011\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">9. Antwort auf Bestellung</text>\n<text x=\"487\" y=\"1035\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 21043 · E_0536</text>\n<text x=\"487\" y=\"1048\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0536 — Bewertung des Gesamtvorgangs</text>\n<line x1=\"365\" y1=\"1082\" x2=\"121\" y2=\"1082\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"1073\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<text x=\"243\" y=\"1097\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten erstellen</text>\n<line x1=\"609\" y1=\"1144\" x2=\"853\" y2=\"1144\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"731\" y=\"1135\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">10. Mitteilung über Gesamtvorgang</text>\n<text x=\"731\" y=\"1159\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 21043 · E_0536</text>\n<text x=\"731\" y=\"1172\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0536 — Bewertung des Gesamtvorgangs</text>\n</svg>"} titel="LF" />

<a id="abschnitt-schritte"></a>

## Prozessschritte

<Schritt nr="1" anker="schritt-1" richtung="ausgehend" kopf={{"links": {"label": "LF", "eigen": true}, "rechts": {"label": "MSB"}}}>

### Anfrage einer Konfiguration auf Ebene der direkt betroffenen Lokation

<Schrittskizze sicht={{"label": "LF"}} zeilen={[{"art": "ausloeser", "werte": ["START_ANFRAGE_KONFIGURATION"]}, {"art": "senden", "label": "MSB", "weg": "AS4", "nachrichten": [{"nr": "35004", "titel": "Anfrage einer Konfiguration"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [35004](/schnittstellen/202604/pruefi/REQOTE/PI_35004) — Anfrage einer Konfiguration · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="ausloeser">

**Prozessauslöser** [`START_ANFRAGE_KONFIGURATION`](/schnittstellen/202604/trigger/events/LF-START_ANFRAGE_KONFIGURATION) · [Im Playground ausprobieren](/api/202604/ausloeser-lf/start-anfrage-konfiguration)

Das Backend stößt diesen Schritt mit diesem Ereignis an.

</li>

<li data-teil="nachricht">

Nachricht an **MSB** · AS4

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202604/backend-schreiben-lf/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": false, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"ANFRAGE\": [\n      {\n        \"anfragetyp\": \"AENDERUNG_KONFIGURATION\",\n        \"boTyp\": \"ANFRAGE\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"LEISTUNGSKURVENDEFINITION\": [\n      {\n        \"boTyp\": \"LEISTUNGSKURVENDEFINITION\",\n        \"leistungskurven\": [\n          {\n            \"code\": \"MMA\",\n            \"konfigurationsprodukt\": \"9991000000721\"\n          }\n        ],\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"MARKTLOKATION\": [\n      {\n        \"boTyp\": \"MARKTLOKATION\",\n        \"marktlokationsId\": \"50444001616\",\n        \"marktlokationsTyp\": [\n          {\n            \"typ\": \"STANDARD_MARKTLOKATION\"\n          }\n        ],\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"ansprechpartner\": {\n        \"boTyp\": \"ANSPRECHPARTNER\",\n        \"eMailAdresse\": \"Max.Mustermann@conuti.de\",\n        \"nachname\": \"Max Mustermann\",\n        \"versionStruktur\": \"1\"\n      },\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9900496000001\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"datenaustauschreferenz\": \"M3VQCXCY\",\n    \"dokumentennummer\": \"BGMM3TJAKY3\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9900496000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"Z82\",\n    \"lieferdatum\": \"2025-01-05T23:00:00Z\",\n    \"nachrichtenReferenzBestellbestaetigung\": \"BGMM44X6WGM\",\n    \"nachrichtendatum\": \"2024-10-16T09:45:00Z\",\n    \"nachrichtenreferenznummer\": \"UNHM3Q4M8YM\",\n    \"positionsnummer\": 1,\n    \"pruefidentifikator\": \"35004\",\n    \"sparte\": \"STROM\",\n    \"vorgangsReferenzBestellbestaetigung\": \"45261\"\n  },\n  \"zusatzdaten\": {}\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend fort, nachdem die Nachricht erstellt ist.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="2" anker="schritt-2" richtung="eingehend" kopf={{"links": {"label": "LF", "eigen": true}, "rechts": {"label": "MSB"}}}>

### Angebot zur / Ablehnung der Anfrage

<Schrittskizze sicht={{"label": "LF"}} zeilen={[{"art": "empfangen", "label": "MSB", "weg": "AS4", "nachrichten": [{"nr": "15004", "titel": "Angebot  einer Konfiguration"}, {"nr": "21033", "titel": "Ablehnung der Anfrage"}]}, {"art": "aperak", "werte": ["Z33"]}, {"art": "erstellen"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [15004](/schnittstellen/202604/pruefi/QUOTES/PI_15004) — Angebot  einer Konfiguration · AS4
- [21033](/schnittstellen/202604/pruefi/IFTSTA/PI_21033) — Ablehnung der Anfrage · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **MSB** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `21033` → [E_0531](/referenz/202604/ebd/E_0531) · MSB · Anfrage prüfen

</div>

</li>

<li data-teil="aperak">

**Aperak-Prüfungen**
- `15004`, `21033` → `Z33` — Aperak Prüfung: Ist referenzierte Nachricht bekannt ?

</li>

<li data-teil="schnittstelle" data-art="schreiben">

**Schreibende Schnittstelle**
- Vorgang angelegt — [Prozessdaten erstellen](/api/202604/backend-schreiben-lf/createprocessdata#prozessdaten-erstellen) `POST /createProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/createProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": false, "defaultValue": "ERSTELLEN_PROZESSDATEN", "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"ANFRAGE\": [\n      {\n        \"anfragetyp\": \"NEUKONFIGURATION\",\n        \"boTyp\": \"ANFRAGE\",\n        \"lokationsId\": \"50074561188\",\n        \"lokationsTyp\": \"MALO\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"ANGEBOT\": [\n      {\n        \"anfragereferenz\": \"AVV12345\",\n        \"boTyp\": \"ANGEBOT\",\n        \"positionsdaten\": [\n          {\n            \"artikelId\": [\n              \"9991000000721-01\",\n              \"9991000000721-02\",\n              \"9991000000721-03\"\n            ],\n            \"positionsbezeichnung\": \"1\"\n          }\n        ],\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"LEISTUNGSKURVENDEFINITION\": [\n      {\n        \"boTyp\": \"LEISTUNGSKURVENDEFINITION\",\n        \"leistungskurven\": [\n          {\n            \"code\": \"NBF\",\n            \"konfigurationsprodukt\": \"9991000000721\"\n          }\n        ],\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"MARKTLOKATION\": [\n      {\n        \"boTyp\": \"MARKTLOKATION\",\n        \"marktlokationsId\": \"50074561188\",\n        \"marktlokationsTyp\": [\n          {\n            \"typ\": \"STANDARD_MARKTLOKATION\"\n          }\n        ],\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"ansprechpartner\": {\n        \"boTyp\": \"ANSPRECHPARTNER\",\n        \"nachname\": \"Max Mustermann\",\n        \"rufnummern\": [\n          {\n            \"nummerntyp\": \"FAX_DURCHWAHL\",\n            \"rufnummer\": \"+001234567\"\n          }\n        ],\n        \"versionStruktur\": \"1\"\n      },\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9904446000007\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"datenaustauschreferenz\": \"MCH0IOL1\",\n    \"dokumentennummer\": \"BGMMC2WCO3K\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9903790000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"Z74\",\n    \"nachrichtendatum\": \"2025-10-10T08:00:00Z\",\n    \"nachrichtenreferenznummer\": \"UNHMC75CA7G\",\n    \"pruefidentifikator\": \"15004\",\n    \"sparte\": \"STROM\"\n  },\n  \"zusatzdaten\": {}\n}"} examples={[{"mediaType": "application/json", "examples": [{"name": "15004", "summary": "15004 — Angebot  einer Konfiguration", "value": {"stammdaten": {"MARKTLOKATION": [{"boTyp": "MARKTLOKATION", "versionStruktur": "1", "marktlokationsId": "50074561188", "marktlokationsTyp": [{"typ": "STANDARD_MARKTLOKATION"}], "sparte": "STROM"}], "ANFRAGE": [{"boTyp": "ANFRAGE", "versionStruktur": "1", "lokationsId": "50074561188", "lokationsTyp": "MALO", "anfragetyp": "NEUKONFIGURATION"}], "ANGEBOT": [{"boTyp": "ANGEBOT", "versionStruktur": "1", "anfragereferenz": "AVV12345", "sparte": "STROM", "positionsdaten": [{"positionsbezeichnung": "1", "artikelId": ["9991000000721-01", "9991000000721-02", "9991000000721-03"]}]}], "LEISTUNGSKURVENDEFINITION": [{"boTyp": "LEISTUNGSKURVENDEFINITION", "versionStruktur": "1", "sparte": "STROM", "leistungskurven": [{"code": "NBF", "konfigurationsprodukt": "9991000000721"}]}]}, "transaktionsdaten": {"datenaustauschreferenz": "MCH0IOL1", "sparte": "STROM", "pruefidentifikator": "15004", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9904446000007", "rollencodetyp": "BDEW", "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "nachname": "Max Mustermann", "rufnummern": [{"nummerntyp": "FAX_DURCHWAHL", "rufnummer": "+001234567"}]}}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9903790000002", "rollencodetyp": "BDEW"}, "dokumentennummer": "BGMMC2WCO3K", "kategorie": "Z74", "nachrichtendatum": "2025-10-10T08:00:00Z", "nachrichtenreferenznummer": "UNHMC75CA7G"}, "zusatzdaten": {}}}, {"name": "21033", "summary": "21033 — Ablehnung der Anfrage", "value": {"stammdaten": {"MARKTLOKATION": [{"boTyp": "MARKTLOKATION", "versionStruktur": "1", "marktlokationsId": "44152365487", "marktlokationsTyp": [{"typ": "STANDARD_MARKTLOKATION"}], "sparte": "STROM"}], "STATUSMITTEILUNG": [{"boTyp": "STATUSMITTEILUNG", "versionStruktur": "1", "statusObjekt": "ANGEBOTANFRAGE", "auftragsstatus": "ABGELEHNT", "positionsdaten": [{"positionsnummer": 1}]}]}, "transaktionsdaten": {"datenaustauschreferenz": "M0KXRR1W", "sparte": "STROM", "pruefidentifikator": "21033", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9904733000009", "rollencodetyp": "BDEW", "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "nachname": "Laue", "eMailAdresse": "lieferantenwechsel@eon-energie.com"}}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900244000009", "rollencodetyp": "BDEW"}, "dokumentennummer": "M0YOR4X5", "kategorie": "Z09", "nachrichtendatum": "2025-10-17T06:36:00Z", "nachrichtenreferenznummer": "M11I1RWQ", "anfragereferenznummer": "7584", "antwortstatus": "A01", "antwortstatusCodeliste": "E_0524"}, "zusatzdaten": {}}}]}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Legt im Backend einen neuen Vorgang mit den Daten der eingegangenen Nachricht an.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="3" anker="schritt-3" richtung="ausgehend" kopf={{"links": {"label": "LF", "eigen": true}, "rechts": {"label": "MSB"}}}>

### Bestellung einer Konfiguration auf Ebene der direkt betroffenen Lokation

<Schrittskizze sicht={{"label": "LF"}} zeilen={[{"art": "senden", "label": "MSB", "weg": "AS4", "nachrichten": [{"nr": "17131", "titel": "Bestellung Angebot einer Konfiguration"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [17131](/schnittstellen/202604/pruefi/ORDERS/PI_17131) — Bestellung Angebot einer Konfiguration · AS4

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
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202604/backend-schreiben-lf/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": false, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"ANFRAGE\": [\n      {\n        \"anfragekategorie\": \"BESTELLUNG_EINES_ANGEBOTS_EINER_KONFIGURATION\",\n        \"boTyp\": \"ANFRAGE\",\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"ansprechpartner\": {\n        \"boTyp\": \"ANSPRECHPARTNER\",\n        \"eMailAdresse\": \"andre.l@conuti.de\",\n        \"nachname\": \"A. Laue\",\n        \"versionStruktur\": \"1\"\n      },\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9904733000009\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"angebotsnummer\": \"12474\",\n    \"datenaustauschreferenz\": \"M03UGIN5\",\n    \"dokumentennummer\": \"M0ACK2J3\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9900244000009\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"nachrichtendatum\": \"2025-10-27T08:06:00Z\",\n    \"nachrichtenreferenznummer\": \"M01KAXGA\",\n    \"pruefidentifikator\": \"17131\",\n    \"sparte\": \"STROM\"\n  },\n  \"zusatzdaten\": {}\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend fort, nachdem die Nachricht erstellt ist.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="4" anker="schritt-4" richtung="ausgehend" kopf={{"links": {"label": "LF", "eigen": true}, "rechts": {"label": "MSB"}}}>

### Bestellung einer Konfiguration auf Ebene der direkt betroffenen Lokation

<Schrittskizze sicht={{"label": "LF"}} zeilen={[{"art": "ausloeser", "werte": ["START_BESTELLUNG_KONFIGURATION", "START_BESTELLUNG_ZAEHLZEITDEFINITION"]}, {"art": "lesen_verarbeitung", "schnittstellen": [{"label": "Netzlokation lesen"}]}, {"art": "senden", "label": "MSB", "weg": "AS4", "nachrichten": [{"nr": "17130", "titel": "Bestellung einer Konfiguration"}, {"nr": "17123", "titel": "Bestellung Änderung Zählzeitdefinition"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [17130](/schnittstellen/202604/pruefi/ORDERS/PI_17130) — Bestellung einer Konfiguration · AS4
- [17123](/schnittstellen/202604/pruefi/ORDERS/PI_17123) — Bestellung Änderung Zählzeitdefinition · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="ausloeser">

**Prozessauslöser**
- [`START_BESTELLUNG_KONFIGURATION`](/schnittstellen/202604/trigger/events/LF-START_BESTELLUNG_KONFIGURATION) · [Im Playground ausprobieren](/api/202604/ausloeser-lf/start-bestellung-konfiguration)
- [`START_BESTELLUNG_ZAEHLZEITDEFINITION`](/schnittstellen/202604/trigger/events/LF-START_BESTELLUNG_ZAEHLZEITDEFINITION) · [Im Playground ausprobieren](/api/202604/ausloeser-lf/start-bestellung-zaehlzeitdefinition)

Das Backend stößt diesen Schritt mit einem dieser Ereignisse an.

</li>

<li data-teil="lesen" data-stufe="verarbeitung">

**Daten für die Verarbeitung laden**
- [Netzlokation lesen](/api/202604/backend-lesen/getgridlocationbasic#netzlokation-lesen) `GET /getGridLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getGridLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_NETZLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

</li>

<li data-teil="nachricht">

Nachricht an **MSB** · AS4

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202604/backend-schreiben-lf/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": false, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"ANFRAGE\": [\n      {\n        \"anfragekategorie\": \"BESTELLUNG_EINER_KONFIGURATION\",\n        \"boTyp\": \"ANFRAGE\",\n        \"lokationsId\": \"C4897654121\",\n        \"lokationsTyp\": \"STEUERBARE_RESSOURCE\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"AUFTRAG\": [\n      {\n        \"boTyp\": \"AUFTRAG\",\n        \"positionsdaten\": [\n          {\n            \"positionsnummer\": 1\n          }\n        ],\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"SCHALTZEITDEFINITION\": [\n      {\n        \"boTyp\": \"SCHALTZEITDEFINITION\",\n        \"schaltzeiten\": [\n          {\n            \"code\": \"AAL\",\n            \"konfigurationsprodukt\": \"9991000000713\"\n          }\n        ],\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"STEUERBARE_RESSOURCE\": [\n      {\n        \"boTyp\": \"STEUERBARE_RESSOURCE\",\n        \"ressourcenId\": \"C4897654121\",\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"ansprechpartner\": {\n        \"boTyp\": \"ANSPRECHPARTNER\",\n        \"eMailAdresse\": \"a.l@cinuti.de\",\n        \"nachname\": \"A\",\n        \"versionStruktur\": \"1\"\n      },\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9903111000003\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"beteiligterMarktpartner\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9903111000003\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"datenaustauschreferenz\": \"M0OU3NLP\",\n    \"dokumentennummer\": \"M0O1YVAK\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9904629000006\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"nachrichtendatum\": \"2024-08-19T08:03:00Z\",\n    \"nachrichtenreferenznummer\": \"M08MHOSC\",\n    \"pruefidentifikator\": \"17130\",\n    \"sparte\": \"STROM\",\n    \"vorgangsreferenznummer\": \"AS1234\"\n  },\n  \"zusatzdaten\": {}\n}"} examples={[{"mediaType": "application/json", "examples": [{"name": "17130", "summary": "17130 — Bestellung einer Konfiguration", "value": {"stammdaten": {"ANFRAGE": [{"boTyp": "ANFRAGE", "versionStruktur": "1", "anfragekategorie": "BESTELLUNG_EINER_KONFIGURATION", "lokationsId": "C4897654121", "lokationsTyp": "STEUERBARE_RESSOURCE"}], "AUFTRAG": [{"boTyp": "AUFTRAG", "versionStruktur": "1", "positionsdaten": [{"positionsnummer": 1}]}], "STEUERBARE_RESSOURCE": [{"boTyp": "STEUERBARE_RESSOURCE", "versionStruktur": "1", "ressourcenId": "C4897654121"}], "SCHALTZEITDEFINITION": [{"boTyp": "SCHALTZEITDEFINITION", "versionStruktur": "1", "schaltzeiten": [{"code": "AAL", "konfigurationsprodukt": "9991000000713"}]}]}, "transaktionsdaten": {"datenaustauschreferenz": "M0OU3NLP", "sparte": "STROM", "pruefidentifikator": "17130", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9903111000003", "rollencodetyp": "BDEW", "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "nachname": "A", "eMailAdresse": "a.l@cinuti.de"}}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9904629000006", "rollencodetyp": "BDEW"}, "dokumentennummer": "M0O1YVAK", "nachrichtendatum": "2024-08-19T08:03:00Z", "nachrichtenreferenznummer": "M08MHOSC", "vorgangsreferenznummer": "AS1234", "beteiligterMarktpartner": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9903111000003", "rollencodetyp": "BDEW"}}, "zusatzdaten": {}}}, {"name": "17123", "summary": "17123 — Bestellung Änderung Zählzeitdefinition", "value": {"stammdaten": {"ANFRAGE": [{"boTyp": "ANFRAGE", "versionStruktur": "1", "anfragekategorie": "AENDERUNG_INDIVIDUELLER_KONFIGURATION", "anfragetyp": "AENDERUNG_KONFIGURATION", "lokationsId": "44897654121", "lokationsTyp": "MALO"}], "AUFTRAG": [{"boTyp": "AUFTRAG", "versionStruktur": "1", "ausfuehrungsdatum": "2024-08-22T22:00:00Z", "positionsdaten": [{"positionsnummer": 1}]}], "MARKTLOKATION": [{"boTyp": "MARKTLOKATION", "versionStruktur": "1", "zaehlwerke": [{"messprodukt": "9991000000052", "zaehlzeiten": {"zaehlzeitDefinition": "AAL"}}]}]}, "transaktionsdaten": {"datenaustauschreferenz": "M0E47OMP", "sparte": "STROM", "pruefidentifikator": "17123", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9903111000003", "rollencodetyp": "BDEW", "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "nachname": "Laue", "eMailAdresse": "a.l@conuti.de"}}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9903111000003", "rollencodetyp": "BDEW"}, "dokumentennummer": "M0RAU7GV", "nachrichtendatum": "2024-08-19T07:34:00Z", "nachrichtenreferenznummer": "M0CYKMGN"}, "zusatzdaten": {}}}]}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend fort, nachdem die Nachricht erstellt ist.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="5" anker="schritt-5" richtung="eingehend" kopf={{"links": {"label": "LF", "eigen": true}, "rechts": {"label": "MSB"}}}>

### Mitteilung zum weiteren Vorgehen zur Bestellung

<Schrittskizze sicht={{"label": "LF"}} zeilen={[{"art": "empfangen", "label": "MSB", "weg": "AS4", "nachrichten": [{"nr": "19132", "titel": "Mitteilung zur Bestellung Konfiguration"}, {"nr": "19124", "titel": "Mitteilung zur Änderung Zählzeitdefinition"}]}, {"art": "aperak", "werte": ["Z33"]}, {"art": "erstellen"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [19132](/schnittstellen/202604/pruefi/ORDRSP/PI_19132) — Mitteilung zur Bestellung Konfiguration · AS4
- [19124](/schnittstellen/202604/pruefi/ORDRSP/PI_19124) — Mitteilung zur Änderung Zählzeitdefinition · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **MSB** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `19132`, `19124` → [E_0533](/referenz/202604/ebd/E_0533) · MSB · Bestellung prüfen

</div>

</li>

<li data-teil="aperak">

**Aperak-Prüfungen**
- `19132`, `19124` → `Z33` — Aperak Prüfung: Ist referenzierte Nachricht bekannt ?

</li>

<li data-teil="schnittstelle" data-art="schreiben">

**Schreibende Schnittstelle**
- Vorgang angelegt — [Prozessdaten erstellen](/api/202604/backend-schreiben-lf/createprocessdata#prozessdaten-erstellen) `POST /createProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/createProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": false, "defaultValue": "ERSTELLEN_PROZESSDATEN", "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"ANFRAGE\": [\n      {\n        \"anfragekategorie\": \"AENDERUNG_INDIVIDUELLER_KONFIGURATION\",\n        \"boTyp\": \"ANFRAGE\",\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"ansprechpartner\": {\n        \"boTyp\": \"ANSPRECHPARTNER\",\n        \"nachname\": \"P GETTY\",\n        \"rufnummern\": [\n          {\n            \"nummerntyp\": \"RUF_DURCHWAHL\",\n            \"rufnummer\": \"+3222271020\"\n          }\n        ],\n        \"versionStruktur\": \"1\"\n      },\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9900244000009\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"antwortstatus\": \"A99\",\n    \"antwortstatusCodeliste\": \"E_0523\",\n    \"auftragsReferenz\": \"AFN9523\",\n    \"datenaustauschreferenz\": \"DASFTZWAIAUQDZ\",\n    \"dokumentennummer\": \"DA862411200724399903323000007189649\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9903692000001\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"freitext\": \"Stell keine Fragen\",\n    \"nachrichtendatum\": \"2026-04-01T12:31:00Z\",\n    \"nachrichtenreferenznummer\": \"DALRTRVYCPSLBA\",\n    \"pruefidentifikator\": \"19124\",\n    \"sparte\": \"STROM\"\n  },\n  \"zusatzdaten\": {}\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Legt im Backend einen neuen Vorgang mit den Daten der eingegangenen Nachricht an.

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
- [17130](/schnittstellen/202604/pruefi/ORDERS/PI_17130) — Bestellung einer Konfiguration · AS4
- [17118](/schnittstellen/202604/pruefi/ORDERS/PI_17118) — Bestellung einer Konfigurationsänderung · AS4

</div>

</Schritt>

<Schritt nr="7" anker="schritt-7" richtung="fremd" kopf={{"links": {"label": "weiterer MSB", "eigen": false}, "rechts": {"label": "MSB"}}}>

### Mitteilung zum weiteren Vorgehen zur Bestellung

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [19132](/schnittstellen/202604/pruefi/ORDRSP/PI_19132) — Mitteilung zur Bestellung Konfiguration · AS4
- [19127](/schnittstellen/202604/pruefi/ORDRSP/PI_19127) — Mitteilung zur Konfigurationsänderung · AS4

</div>

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `19132`, `19127` → [E_0527](/referenz/202604/ebd/E_0527) · MSB · Bestellung

</div>

</Schritt>

<Schritt nr="8" anker="schritt-8" richtung="fremd" kopf={{"links": {"label": "weiterer MSB", "eigen": false}, "rechts": {"label": "MSB"}}}>

### Antwort auf Bestellung

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [21043](/schnittstellen/202604/pruefi/IFTSTA/PI_21043) — Bestellungsantwort / -mitteilung · AS4

</div>

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `21043` → [E_0535](/referenz/202604/ebd/E_0535) · Umsetzung der Konfiguration prüfen

</div>

</Schritt>

<Schritt nr="9" anker="schritt-9" richtung="eingehend" kopf={{"links": {"label": "LF", "eigen": true}, "rechts": {"label": "MSB"}}}>

### Antwort auf Bestellung

<Schrittskizze sicht={{"label": "LF"}} zeilen={[{"art": "empfangen", "label": "MSB", "weg": "AS4", "nachrichten": [{"nr": "21043", "titel": "Bestellungsantwort / -mitteilung"}]}, {"art": "aperak", "werte": ["Z33"]}, {"art": "erstellen"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [21043](/schnittstellen/202604/pruefi/IFTSTA/PI_21043) — Bestellungsantwort / -mitteilung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **MSB** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `21043` → [E_0536](/referenz/202604/ebd/E_0536) · MSB · Bewertung des Gesamtvorgangs

</div>

</li>

<li data-teil="aperak">

**Aperak-Prüfungen**
- `21043` → `Z33` — Aperak Prüfung: Ist referenzierte Nachricht bekannt ?

</li>

<li data-teil="schnittstelle" data-art="schreiben">

**Schreibende Schnittstelle**
- Vorgang angelegt — [Prozessdaten erstellen](/api/202604/backend-schreiben-lf/createprocessdata#prozessdaten-erstellen) `POST /createProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/createProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": false, "defaultValue": "ERSTELLEN_PROZESSDATEN", "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"STATUSMITTEILUNG\": [\n      {\n        \"auftragsstatus\": \"ABGELEHNT\",\n        \"boTyp\": \"STATUSMITTEILUNG\",\n        \"positionsdaten\": [\n          {\n            \"positionsnummer\": 1,\n            \"statusVeraenderungsZeitpunkt\": \"2025-01-15T23:00:00Z\"\n          }\n        ],\n        \"statusObjekt\": \"STATUSBESTELLUNG\",\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"marktrolle\": \"LF\",\n      \"rollencodenummer\": \"9903790000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"anfrageReferenz\": \"BGM12345\",\n    \"antwortstatus\": \"A01\",\n    \"antwortstatusCodeliste\": \"E_0529\",\n    \"datenaustauschreferenz\": \"M0STR69K\",\n    \"dokumentennummer\": \"BGMM0UQI60K\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"marktrolle\": \"NB\",\n      \"rollencodenummer\": \"9900321000005\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"Z73\",\n    \"nachrichtendatum\": \"2025-04-04T12:00:00Z\",\n    \"nachrichtenreferenznummer\": \"UNHM0N3XSGK\",\n    \"pruefidentifikator\": \"21043\",\n    \"sparte\": \"STROM\"\n  },\n  \"zusatzdaten\": {}\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Legt im Backend einen neuen Vorgang mit den Daten der eingegangenen Nachricht an.

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
- [21043](/schnittstellen/202604/pruefi/IFTSTA/PI_21043) — Bestellungsantwort / -mitteilung · AS4

</div>

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `21043` → [E_0536](/referenz/202604/ebd/E_0536) · MSB · Bewertung des Gesamtvorgangs

</div>

</Schritt>

<details>
<summary>Entscheidungsbäume dieses Prozesses</summary>

| EBD | Name |
|---|---|
| [E_0531](/referenz/202604/ebd/E_0531) | Anfrage prüfen |
| [E_0533](/referenz/202604/ebd/E_0533) | Bestellung prüfen |
| [E_0536](/referenz/202604/ebd/E_0536) | Bewertung des Gesamtvorgangs |
| [E_0527](/referenz/202604/ebd/E_0527) | Bestellung |
| [E_0535](/referenz/202604/ebd/E_0535) | Umsetzung der Konfiguration prüfen |

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

- Sofern die Konfiguration für alle betroffenen Lokationen erfolgreich eingerichtet wurde, führt der MSB der jeweils betroffenen Lokation den Use-Case „Stammdatenänderung“ (hier: SD „[Stammdatenänderung vom MSB (verantwortlich) ausgehend](/prozessdoku/202604/LF/GPKE-Teil4-stammdatenaenderung-vom-msb-verantwortlich-ausgehend)“) (GPKE Teil 4) durch, sofern für die jeweilige Lokation eine Stammdatenänderung aufgrund der Einrichtung der Konfiguration erforderlich ist.
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
- Konfigurationen des NB werden im Use-Case „[Beginn Messstellenbetrieb](/prozessdoku/202604/LF/WiM-Teil1-beginn-messstellenbetrieb)“ (WiM Teil 1) in Prozessschritt 2 im Rahmen der Mindestparameter für die Messlokation(en) vom NB dem MSB mitgeteilt. Eine Bestellung einer in den Mindestparametern enthaltenen Konfiguration ist nicht über den hier beschriebenen Use-Case notwendig. Ergänzend zu den in den Mindestparametern mitgeteilten Konfigurationen, kann der NB mit Hilfe des hier beschriebenen Use-Cases eine Bestellung einer Konfiguration an den zukünftigen MSB übermitteln. Hinweis: Wird dem MSB im Rahmen der Mindestparameter im Use-Case „[Beginn Messstellenbetrieb](/prozessdoku/202604/LF/WiM-Teil1-beginn-messstellenbetrieb)“ (WiM Teil 1) eine Zählzeitdefinition des NB mitgeteilt, die der MSB vorab nicht über den Use-Case „[Übermittlung einer Definition des NB durch den NB](/prozessdoku/202604/LF/GPKE-Teil3-uebermittlung-einer-definition-des-nb-durch-den-nb)“ übermittelt bekommen hat, so ist die Energie in einem Register an der/den Messlokation(en) und der zugehörigen Marktlokation für den Zählzeitenanwendungszweck „Netznutzung“ zu erfassen.

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

- [Sicht MSB](/prozessdoku/202604/MSB/GPKE-Teil3-bestellung-einer-konfiguration-vom-lf-an-msb) — MSB
- [Sicht WMSB](/prozessdoku/202604/MSB--WMSB/GPKE-Teil3-bestellung-einer-konfiguration-vom-lf-an-msb) — weiterer Messstellenbetreiber · Marktrolle MSB

<Hinweisbereich>

*Die Schritte sind die **möglichen** Nachrichten dieses Prozesses, keine Abfolge — die Quelle führt weder Bedingungen noch Alternativen. Das Kästchen am Schritt nennt links die eigene Sicht: **←** empfängt sie, **→** sendet sie. Zugeklappte Schritte laufen zwischen anderen Marktpartnern.*

</Hinweisbereich>
