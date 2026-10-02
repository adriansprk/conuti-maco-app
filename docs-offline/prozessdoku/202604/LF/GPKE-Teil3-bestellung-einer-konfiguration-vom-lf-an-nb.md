# Bestellung einer Konfiguration vom LF an NB — Sicht LF

<Kopf rolle="LF" beteiligter="LF" festlegung="GPKE" dokument="GPKE Teil 3" kapitel="1.3.2.2" sparte="Strom" schritte={4} suchtitel="Bestellung einer Konfiguration vom LF an NB — Sicht LF · GPKE Teil 3 · Formatversion 202604" abschnitte={[{"id": "abschnitt-ablauf", "label": "Prozessablauf"}, {"id": "abschnitt-schritte", "label": "Prozessschritte"}, {"id": "abschnitt-informationen", "label": "Prozess-Informationen"}, {"id": "abschnitt-sichten", "label": "Andere Sichten des Prozesses"}]} />

<Kurzfassung>

Der LF bestellt beim NB eine Konfiguration für die direkt betroffene Lokation. Der NB prüft die Bestellung, teilt dem LF das weitere Vorgehen zur Bestellung mit und beauftragt beim MSB der direkt betroffenen Lokation mit dem Use-Case „Bestellung einer Konfiguration vom NB oder LF an MSB“ ggf. die erforderliche Konfiguration. Der NB leitet die Rückmeldung des MSB an den LF weiter.

</Kurzfassung>

<a id="abschnitt-ablauf"></a>

## Prozessablauf aus Sicht des LF

<Systembild svg={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1004 1030\" width=\"1004\" height=\"1030\" role=\"img\" aria-labelledby=\"sb-title\" class=\"maco-systembild\">\n<title id=\"sb-title\">Systembild: Bestellung einer Konfiguration vom LF an NB aus Sicht LF</title>\n<defs><marker id=\"sb-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect class=\"sb-lane-kopf\" x=\"16\" y=\"12\" width=\"232\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend-System des Kunden</text>\n<rect class=\"sb-lane-kopf\" x=\"398\" y=\"12\" width=\"264\" height=\"46\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · LF</text>\n<rect class=\"sb-lane-kopf\" x=\"812\" y=\"12\" width=\"176\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"900\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Marktpartner</text>\n<line x1=\"323\" y1=\"58\" x2=\"323\" y2=\"1018\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"737\" y1=\"58\" x2=\"737\" y2=\"1018\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect class=\"sb-kasten sb-trigger\" x=\"432\" y=\"80\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessauslöser empfangen</text>\n<rect class=\"sb-kasten sb-backend sb-trigger\" x=\"34\" y=\"80\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">2 Ereignisse, alternativ</text>\n<line x1=\"230\" y1=\"96\" x2=\"432\" y2=\"96\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"88\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"144\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"164\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">1. Bestellung einer</text>\n<text x=\"530\" y=\"179\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Konfiguration auf Ebene der</text>\n<text x=\"530\" y=\"194\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">direkt betroff…</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"113\" x2=\"530\" y2=\"144\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"157\" r=\"5\"/><line x1=\"900\" y1=\"162\" x2=\"900\" y2=\"174\"/><line x1=\"893\" y1=\"166\" x2=\"907\" y2=\"166\"/><line x1=\"900\" y1=\"174\" x2=\"894\" y2=\"184\"/><line x1=\"900\" y1=\"174\" x2=\"906\" y2=\"184\"/></g>\n<text x=\"900\" y=\"206\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"628\" y1=\"175\" x2=\"878\" y2=\"175\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"167\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"191\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">17123, 17120</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"233\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"253\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"207\" x2=\"530\" y2=\"233\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"233\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"253\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"249\" x2=\"230\" y2=\"249\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"241\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"297\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"317\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">2. Mitteilung zum weiteren</text>\n<text x=\"530\" y=\"332\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgehen zur Bestellung</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"266\" x2=\"530\" y2=\"297\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"303\" r=\"5\"/><line x1=\"900\" y1=\"308\" x2=\"900\" y2=\"320\"/><line x1=\"893\" y1=\"312\" x2=\"907\" y2=\"312\"/><line x1=\"900\" y1=\"320\" x2=\"894\" y2=\"330\"/><line x1=\"900\" y1=\"320\" x2=\"906\" y2=\"330\"/></g>\n<text x=\"900\" y=\"352\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"878\" y1=\"321\" x2=\"628\" y2=\"321\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"313\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"337\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">19121, 19124</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"380\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"400\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z33</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"345\" x2=\"530\" y2=\"380\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-schreiben\" x=\"432\" y=\"444\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"464\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"413\" x2=\"530\" y2=\"444\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-schreiben\" x=\"34\" y=\"444\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"464\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten erstellen</text>\n<line x1=\"432\" y1=\"460\" x2=\"230\" y2=\"460\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"452\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<text x=\"331\" y=\"476\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">PI 19124</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"508\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"528\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"477\" x2=\"530\" y2=\"508\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben sb-abgeleitet\" x=\"34\" y=\"508\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"528\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"524\" x2=\"230\" y2=\"524\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"516\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<text x=\"331\" y=\"540\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">PI 19121</text>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"572\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"592\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">4. Weiterleitung der</text>\n<text x=\"530\" y=\"607\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Mitteilung zum weiteren</text>\n<text x=\"530\" y=\"622\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgehen zur Best…</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"541\" x2=\"530\" y2=\"572\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"585\" r=\"5\"/><line x1=\"900\" y1=\"590\" x2=\"900\" y2=\"602\"/><line x1=\"893\" y1=\"594\" x2=\"907\" y2=\"594\"/><line x1=\"900\" y1=\"602\" x2=\"894\" y2=\"612\"/><line x1=\"900\" y1=\"602\" x2=\"906\" y2=\"612\"/></g>\n<text x=\"900\" y=\"634\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"878\" y1=\"603\" x2=\"628\" y2=\"603\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"595\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"619\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">21043</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"661\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"681\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z33</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"635\" x2=\"530\" y2=\"661\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-schreiben\" x=\"432\" y=\"725\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"745\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"694\" x2=\"530\" y2=\"725\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-schreiben\" x=\"34\" y=\"725\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"745\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten erstellen</text>\n<line x1=\"432\" y1=\"741\" x2=\"230\" y2=\"741\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"733\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"789\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"809\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">5. Weiterleitung der Antwort</text>\n<text x=\"530\" y=\"824\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">auf Bestellung vom MSB der</text>\n<text x=\"530\" y=\"839\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">direkt…</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"758\" x2=\"530\" y2=\"789\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"802\" r=\"5\"/><line x1=\"900\" y1=\"807\" x2=\"900\" y2=\"819\"/><line x1=\"893\" y1=\"811\" x2=\"907\" y2=\"811\"/><line x1=\"900\" y1=\"819\" x2=\"894\" y2=\"829\"/><line x1=\"900\" y1=\"819\" x2=\"906\" y2=\"829\"/></g>\n<text x=\"900\" y=\"851\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"878\" y1=\"820\" x2=\"628\" y2=\"820\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"812\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"836\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">21043</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"878\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"898\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z33</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"852\" x2=\"530\" y2=\"878\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-schreiben\" x=\"432\" y=\"942\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"962\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"911\" x2=\"530\" y2=\"942\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-schreiben\" x=\"34\" y=\"942\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"962\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten erstellen</text>\n<line x1=\"432\" y1=\"958\" x2=\"230\" y2=\"958\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"950\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n</svg>"} gesamt={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 730 734\" width=\"730\" height=\"734\" role=\"img\" aria-labelledby=\"sd-title\" class=\"maco-sequence\">\n<title id=\"sd-title\">Sequenzdiagramm: Bestellung einer Konfiguration vom LF an NB aus Sicht LF</title>\n<defs><marker id=\"sd-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect x=\"16\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"121\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend (Kunde)</text>\n<line x1=\"121\" y1=\"64\" x2=\"121\" y2=\"722\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"260\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"365\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · LF</text>\n<line x1=\"365\" y1=\"64\" x2=\"365\" y2=\"722\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"504\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"609\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"609\" y1=\"64\" x2=\"609\" y2=\"722\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"121\" y1=\"90\" x2=\"365\" y2=\"90\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"81\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">2 Ereignisse, alternativ</text>\n<text x=\"243\" y=\"105\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Trigger-Event</text>\n<line x1=\"365\" y1=\"152\" x2=\"609\" y2=\"152\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"143\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">1. Bestellung einer Konfiguration auf Ebene der…</text>\n<text x=\"487\" y=\"167\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 17123, 17120</text>\n<line x1=\"365\" y1=\"214\" x2=\"121\" y2=\"214\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"205\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"229\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"609\" y1=\"276\" x2=\"365\" y2=\"276\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"267\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">2. Mitteilung zum weiteren Vorgehen zur Bestellu…</text>\n<text x=\"487\" y=\"291\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 19121, 19124 · E_0523</text>\n<text x=\"487\" y=\"304\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0523 — Bestellung prüfen</text>\n<line x1=\"365\" y1=\"338\" x2=\"121\" y2=\"338\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"329\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<text x=\"243\" y=\"353\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten erstellen · PI 19124</text>\n<line x1=\"365\" y1=\"400\" x2=\"121\" y2=\"400\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"391\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"415\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren · PI 19121</text>\n<line x1=\"609\" y1=\"462\" x2=\"365\" y2=\"462\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"453\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">4. Weiterleitung der Mitteilung zum weiteren Vor…</text>\n<text x=\"487\" y=\"477\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 21043 · E_0526</text>\n<text x=\"487\" y=\"490\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0526 — Bestellung prüfen</text>\n<line x1=\"365\" y1=\"524\" x2=\"121\" y2=\"524\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"515\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<text x=\"243\" y=\"539\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten erstellen</text>\n<line x1=\"609\" y1=\"586\" x2=\"365\" y2=\"586\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"577\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">5. Weiterleitung der Antwort auf Bestellung vom…</text>\n<text x=\"487\" y=\"601\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 21043 · E_0529</text>\n<text x=\"487\" y=\"614\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0529 — Bewertung des Gesamtvorgangs</text>\n<line x1=\"365\" y1=\"648\" x2=\"121\" y2=\"648\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"639\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<text x=\"243\" y=\"663\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten erstellen</text>\n</svg>"} titel="LF" />

<a id="abschnitt-schritte"></a>

## Prozessschritte

<Schritt nr="1" anker="schritt-1" richtung="ausgehend" kopf={{"links": {"label": "LF", "eigen": true}, "rechts": {"label": "NB"}}}>

### Bestellung einer Konfiguration auf Ebene der direkt betroffenen Lokation

<Schrittskizze sicht={{"label": "LF"}} zeilen={[{"art": "ausloeser", "werte": ["START_BESTELLUNG_AEND_PROGNOSEGRUNDLAGE", "START_BESTELLUNG_ZAEHLZEITDEFINITION"]}, {"art": "senden", "label": "NB", "weg": "AS4", "nachrichten": [{"nr": "17123", "titel": "Bestellung Änderung Zählzeitdefinition"}, {"nr": "17120", "titel": "Bestellung Änderung Prognosegrundlage"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [17123](/schnittstellen/202604/pruefi/ORDERS/PI_17123) — Bestellung Änderung Zählzeitdefinition · AS4
- [17120](/schnittstellen/202604/pruefi/ORDERS/PI_17120) — Bestellung Änderung Prognosegrundlage · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="ausloeser">

**Prozessauslöser**
- [`START_BESTELLUNG_AEND_PROGNOSEGRUNDLAGE`](/schnittstellen/202604/trigger/events/LF-START_BESTELLUNG_AEND_PROGNOSEGRUNDLAGE) · [Im Playground ausprobieren](/api/202604/ausloeser-lf/start-bestellung-aend-prognosegrundlage)
- [`START_BESTELLUNG_ZAEHLZEITDEFINITION`](/schnittstellen/202604/trigger/events/LF-START_BESTELLUNG_ZAEHLZEITDEFINITION) · [Im Playground ausprobieren](/api/202604/ausloeser-lf/start-bestellung-zaehlzeitdefinition)

Das Backend stößt diesen Schritt mit einem dieser Ereignisse an.

</li>

<li data-teil="nachricht">

Nachricht an **NB** · AS4

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202604/backend-schreiben-lf/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": false, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"ANFRAGE\": [\n      {\n        \"anfragekategorie\": \"AENDERUNG_INDIVIDUELLER_KONFIGURATION\",\n        \"anfragetyp\": \"AENDERUNG_KONFIGURATION\",\n        \"boTyp\": \"ANFRAGE\",\n        \"lokationsId\": \"44897654121\",\n        \"lokationsTyp\": \"MALO\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"AUFTRAG\": [\n      {\n        \"ausfuehrungsdatum\": \"2024-08-22T22:00:00Z\",\n        \"boTyp\": \"AUFTRAG\",\n        \"positionsdaten\": [\n          {\n            \"positionsnummer\": 1\n          }\n        ],\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"MARKTLOKATION\": [\n      {\n        \"boTyp\": \"MARKTLOKATION\",\n        \"versionStruktur\": \"1\",\n        \"zaehlwerke\": [\n          {\n            \"messprodukt\": \"9991000000052\",\n            \"zaehlzeiten\": {\n              \"zaehlzeitDefinition\": \"AAL\"\n            }\n          }\n        ]\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"ansprechpartner\": {\n        \"boTyp\": \"ANSPRECHPARTNER\",\n        \"eMailAdresse\": \"a.l@conuti.de\",\n        \"nachname\": \"Laue\",\n        \"versionStruktur\": \"1\"\n      },\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9903111000003\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"datenaustauschreferenz\": \"M0E47OMP\",\n    \"dokumentennummer\": \"M0RAU7GV\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9903111000003\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"nachrichtendatum\": \"2024-08-19T07:34:00Z\",\n    \"nachrichtenreferenznummer\": \"M0CYKMGN\",\n    \"pruefidentifikator\": \"17123\",\n    \"sparte\": \"STROM\"\n  },\n  \"zusatzdaten\": {}\n}"} examples={[{"mediaType": "application/json", "examples": [{"name": "17123", "summary": "17123 — Bestellung Änderung Zählzeitdefinition", "value": {"stammdaten": {"ANFRAGE": [{"boTyp": "ANFRAGE", "versionStruktur": "1", "anfragekategorie": "AENDERUNG_INDIVIDUELLER_KONFIGURATION", "anfragetyp": "AENDERUNG_KONFIGURATION", "lokationsId": "44897654121", "lokationsTyp": "MALO"}], "AUFTRAG": [{"boTyp": "AUFTRAG", "versionStruktur": "1", "ausfuehrungsdatum": "2024-08-22T22:00:00Z", "positionsdaten": [{"positionsnummer": 1}]}], "MARKTLOKATION": [{"boTyp": "MARKTLOKATION", "versionStruktur": "1", "zaehlwerke": [{"messprodukt": "9991000000052", "zaehlzeiten": {"zaehlzeitDefinition": "AAL"}}]}]}, "transaktionsdaten": {"datenaustauschreferenz": "M0E47OMP", "sparte": "STROM", "pruefidentifikator": "17123", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9903111000003", "rollencodetyp": "BDEW", "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "nachname": "Laue", "eMailAdresse": "a.l@conuti.de"}}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9903111000003", "rollencodetyp": "BDEW"}, "dokumentennummer": "M0RAU7GV", "nachrichtendatum": "2024-08-19T07:34:00Z", "nachrichtenreferenznummer": "M0CYKMGN"}, "zusatzdaten": {}}}, {"name": "17120", "summary": "17120 — Bestellung Änderung Prognosegrundlage", "value": {"stammdaten": {"ANFRAGE": [{"boTyp": "ANFRAGE", "versionStruktur": "1", "anfragekategorie": "AENDERUNG_PROGNOSEGRUNDLAGE_GERAETEKONFIGURATION", "lokationsId": "44897654121", "lokationsTyp": "MALO"}], "AUFTRAG": [{"boTyp": "AUFTRAG", "versionStruktur": "1", "ausfuehrungsdatum": "2024-08-18T22:00:00Z", "positionsdaten": [{"positionsnummer": 1}]}], "BILANZIERUNG": [{"boTyp": "BILANZIERUNG", "versionStruktur": "1", "prognosegrundlage": "PROFILE"}]}, "transaktionsdaten": {"datenaustauschreferenz": "M0C301JD", "sparte": "STROM", "pruefidentifikator": "17120", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9903111000003", "rollencodetyp": "BDEW", "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "nachname": "Laue", "eMailAdresse": "a.l@conuti.de"}}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9900259000002", "rollencodetyp": "BDEW"}, "dokumentennummer": "M0F3L98J", "nachrichtendatum": "2024-08-19T07:17:00Z", "nachrichtenreferenznummer": "M0HHR9A1"}, "zusatzdaten": {}}}]}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend fort, nachdem die Nachricht erstellt ist.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="2" anker="schritt-2" richtung="eingehend" kopf={{"links": {"label": "LF", "eigen": true}, "rechts": {"label": "NB"}}}>

### Mitteilung zum weiteren Vorgehen zur Bestellung

<Schrittskizze sicht={{"label": "LF"}} zeilen={[{"art": "empfangen", "label": "NB", "weg": "AS4", "nachrichten": [{"nr": "19121", "titel": "Mitteilung zur Änderung Prognosegrundlage"}, {"nr": "19124", "titel": "Mitteilung zur Änderung Zählzeitdefinition"}]}, {"art": "aperak", "werte": ["Z33"]}, {"art": "erstellen", "nummern": ["19124"]}, {"art": "fortschreiben", "nummern": ["19121"]}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [19121](/schnittstellen/202604/pruefi/ORDRSP/PI_19121) — Mitteilung zur Änderung Prognosegrundlage · AS4
- [19124](/schnittstellen/202604/pruefi/ORDRSP/PI_19124) — Mitteilung zur Änderung Zählzeitdefinition · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **NB** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `19121`, `19124` → [E_0523](/referenz/202604/ebd/E_0523) · NB · Bestellung prüfen

</div>

</li>

<li data-teil="aperak">

**Aperak-Prüfungen**
- `19121`, `19124` → `Z33` — Aperak Prüfung: Ist referenzierte Nachricht bekannt ?

</li>

<li data-teil="schnittstelle" data-art="schreiben">

**Schreibende Schnittstelle**
- `19124` → Vorgang angelegt — [Prozessdaten erstellen](/api/202604/backend-schreiben-lf/createprocessdata#prozessdaten-erstellen) `POST /createProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/createProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": false, "defaultValue": "ERSTELLEN_PROZESSDATEN", "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"ANFRAGE\": [\n      {\n        \"anfragekategorie\": \"AENDERUNG_PROGNOSEGRUNDLAGE_GERAETEKONFIGURATION\",\n        \"boTyp\": \"ANFRAGE\",\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"ansprechpartner\": {\n        \"boTyp\": \"ANSPRECHPARTNER\",\n        \"nachname\": \"P GETTY\",\n        \"rufnummern\": [\n          {\n            \"nummerntyp\": \"RUF_DURCHWAHL\",\n            \"rufnummer\": \"+3222271020\"\n          }\n        ],\n        \"versionStruktur\": \"1\"\n      },\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9900244000009\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"antwortstatus\": \"A99\",\n    \"antwortstatusCodeliste\": \"E_0523\",\n    \"auftragsReferenz\": \"AFN9523\",\n    \"datenaustauschreferenz\": \"DAQRPLETMTPRWU\",\n    \"dokumentennummer\": \"DA012411191116599903323000007252883\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9903692000001\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"freitext\": \"Ist so Olli\",\n    \"nachrichtendatum\": \"2026-04-01T12:31:00Z\",\n    \"nachrichtenreferenznummer\": \"DASYTDSJACCSVU\",\n    \"pruefidentifikator\": \"19121\",\n    \"sparte\": \"STROM\"\n  },\n  \"zusatzdaten\": {}\n}"} examples={[{"mediaType": "application/json", "examples": [{"name": "19121", "summary": "19121 — Mitteilung zur Änderung Prognosegrundlage", "value": {"stammdaten": {"ANFRAGE": [{"boTyp": "ANFRAGE", "versionStruktur": "1", "anfragekategorie": "AENDERUNG_PROGNOSEGRUNDLAGE_GERAETEKONFIGURATION"}]}, "transaktionsdaten": {"datenaustauschreferenz": "DAQRPLETMTPRWU", "sparte": "STROM", "pruefidentifikator": "19121", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9900244000009", "rollencodetyp": "BDEW", "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "nachname": "P GETTY", "rufnummern": [{"nummerntyp": "RUF_DURCHWAHL", "rufnummer": "+3222271020"}]}}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9903692000001", "rollencodetyp": "BDEW"}, "dokumentennummer": "DA012411191116599903323000007252883", "nachrichtendatum": "2026-04-01T12:31:00Z", "nachrichtenreferenznummer": "DASYTDSJACCSVU", "auftragsReferenz": "AFN9523", "antwortstatus": "A99", "antwortstatusCodeliste": "E_0523", "freitext": "Ist so Olli"}, "zusatzdaten": {}}}, {"name": "19124", "summary": "19124 — Mitteilung zur Änderung Zählzeitdefinition", "value": {"stammdaten": {"ANFRAGE": [{"boTyp": "ANFRAGE", "versionStruktur": "1", "anfragekategorie": "AENDERUNG_INDIVIDUELLER_KONFIGURATION"}]}, "transaktionsdaten": {"datenaustauschreferenz": "DASFTZWAIAUQDZ", "sparte": "STROM", "pruefidentifikator": "19124", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9900244000009", "rollencodetyp": "BDEW", "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "nachname": "P GETTY", "rufnummern": [{"nummerntyp": "RUF_DURCHWAHL", "rufnummer": "+3222271020"}]}}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9903692000001", "rollencodetyp": "BDEW"}, "dokumentennummer": "DA862411200724399903323000007189649", "nachrichtendatum": "2026-04-01T12:31:00Z", "nachrichtenreferenznummer": "DALRTRVYCPSLBA", "auftragsReferenz": "AFN9523", "antwortstatus": "A99", "antwortstatusCodeliste": "E_0523", "freitext": "Stell keine Fragen"}, "zusatzdaten": {}}}]}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Legt im Backend einen neuen Vorgang mit den Daten der eingegangenen Nachricht an.

</li>

<li data-teil="schnittstelle" data-art="fortschreiben" data-abgeleitet="ja">

**Schreibende Schnittstelle**
- `19121` → Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202604/backend-schreiben-lf/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": false, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"ANFRAGE\": [\n      {\n        \"anfragekategorie\": \"AENDERUNG_PROGNOSEGRUNDLAGE_GERAETEKONFIGURATION\",\n        \"boTyp\": \"ANFRAGE\",\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"ansprechpartner\": {\n        \"boTyp\": \"ANSPRECHPARTNER\",\n        \"nachname\": \"P GETTY\",\n        \"rufnummern\": [\n          {\n            \"nummerntyp\": \"RUF_DURCHWAHL\",\n            \"rufnummer\": \"+3222271020\"\n          }\n        ],\n        \"versionStruktur\": \"1\"\n      },\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9900244000009\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"antwortstatus\": \"A99\",\n    \"antwortstatusCodeliste\": \"E_0523\",\n    \"auftragsReferenz\": \"AFN9523\",\n    \"datenaustauschreferenz\": \"DAQRPLETMTPRWU\",\n    \"dokumentennummer\": \"DA012411191116599903323000007252883\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9903692000001\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"freitext\": \"Ist so Olli\",\n    \"nachrichtendatum\": \"2026-04-01T12:31:00Z\",\n    \"nachrichtenreferenznummer\": \"DASYTDSJACCSVU\",\n    \"pruefidentifikator\": \"19121\",\n    \"sparte\": \"STROM\"\n  },\n  \"zusatzdaten\": {}\n}"} examples={[{"mediaType": "application/json", "examples": [{"name": "19121", "summary": "19121 — Mitteilung zur Änderung Prognosegrundlage", "value": {"stammdaten": {"ANFRAGE": [{"boTyp": "ANFRAGE", "versionStruktur": "1", "anfragekategorie": "AENDERUNG_PROGNOSEGRUNDLAGE_GERAETEKONFIGURATION"}]}, "transaktionsdaten": {"datenaustauschreferenz": "DAQRPLETMTPRWU", "sparte": "STROM", "pruefidentifikator": "19121", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9900244000009", "rollencodetyp": "BDEW", "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "nachname": "P GETTY", "rufnummern": [{"nummerntyp": "RUF_DURCHWAHL", "rufnummer": "+3222271020"}]}}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9903692000001", "rollencodetyp": "BDEW"}, "dokumentennummer": "DA012411191116599903323000007252883", "nachrichtendatum": "2026-04-01T12:31:00Z", "nachrichtenreferenznummer": "DASYTDSJACCSVU", "auftragsReferenz": "AFN9523", "antwortstatus": "A99", "antwortstatusCodeliste": "E_0523", "freitext": "Ist so Olli"}, "zusatzdaten": {}}}, {"name": "19124", "summary": "19124 — Mitteilung zur Änderung Zählzeitdefinition", "value": {"stammdaten": {"ANFRAGE": [{"boTyp": "ANFRAGE", "versionStruktur": "1", "anfragekategorie": "AENDERUNG_INDIVIDUELLER_KONFIGURATION"}]}, "transaktionsdaten": {"datenaustauschreferenz": "DASFTZWAIAUQDZ", "sparte": "STROM", "pruefidentifikator": "19124", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9900244000009", "rollencodetyp": "BDEW", "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "nachname": "P GETTY", "rufnummern": [{"nummerntyp": "RUF_DURCHWAHL", "rufnummer": "+3222271020"}]}}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9903692000001", "rollencodetyp": "BDEW"}, "dokumentennummer": "DA862411200724399903323000007189649", "nachrichtendatum": "2026-04-01T12:31:00Z", "nachrichtenreferenznummer": "DALRTRVYCPSLBA", "auftragsReferenz": "AFN9523", "antwortstatus": "A99", "antwortstatusCodeliste": "E_0523", "freitext": "Stell keine Fragen"}, "zusatzdaten": {}}}]}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend mit den Daten der eingegangenen Nachricht fort.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="4" anker="schritt-4" richtung="eingehend" kopf={{"links": {"label": "LF", "eigen": true}, "rechts": {"label": "NB"}}}>

### Weiterleitung der Mitteilung zum weiteren Vorgehen zur Bestellung vom MSB der direkt betroffenen Lokation

<Schrittskizze sicht={{"label": "LF"}} zeilen={[{"art": "empfangen", "label": "NB", "weg": "AS4", "nachrichten": [{"nr": "21043", "titel": "Bestellungsantwort / -mitteilung"}]}, {"art": "aperak", "werte": ["Z33"]}, {"art": "erstellen"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [21043](/schnittstellen/202604/pruefi/IFTSTA/PI_21043) — Bestellungsantwort / -mitteilung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **NB** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `21043` → [E_0526](/referenz/202604/ebd/E_0526) · MSB · Bestellung prüfen

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

<Schritt nr="5" anker="schritt-5" richtung="eingehend" kopf={{"links": {"label": "LF", "eigen": true}, "rechts": {"label": "NB"}}}>

### Weiterleitung der Antwort auf Bestellung vom MSB der direkt betroffenen Lokation

<Schrittskizze sicht={{"label": "LF"}} zeilen={[{"art": "empfangen", "label": "NB", "weg": "AS4", "nachrichten": [{"nr": "21043", "titel": "Bestellungsantwort / -mitteilung"}]}, {"art": "aperak", "werte": ["Z33"]}, {"art": "erstellen"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [21043](/schnittstellen/202604/pruefi/IFTSTA/PI_21043) — Bestellungsantwort / -mitteilung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **NB** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `21043` → [E_0529](/referenz/202604/ebd/E_0529) · MSB · Bewertung des Gesamtvorgangs

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

<details>
<summary>Entscheidungsbäume dieses Prozesses</summary>

| EBD | Name |
|---|---|
| [E_0523](/referenz/202604/ebd/E_0523) | Bestellung prüfen |
| [E_0526](/referenz/202604/ebd/E_0526) | Bestellung prüfen |
| [E_0529](/referenz/202604/ebd/E_0529) | Bewertung des Gesamtvorgangs |

</details>

<a id="abschnitt-informationen"></a>

## Prozess-Informationen

Wortlaut der Lesefassung, Steckbrief Kap. 1.3.2.1, S. 37–38.

<Stepper>
<ol>

<li data-blatt="vorbedingungen">

### Vorbedingungen

- Es handelt sich um keine kostenpflichtige Konfiguration.
- Die zum bestellten Zeitpunkt vorhandene Gerätetechnik ermöglicht die Einrichtung der Konfiguration. Dies bedeutet z. B. im Fall der Änderung des Bilanzierungsverfahrens, dass alle Messlokationen der Marktlokation mit kME mit RLM ausgestattet sind.
- Im Fall der Bestellung einer Konfiguration, für die eine Zählzeitdefinition, Schaltzeitdefinition oder Leistungskurvendefinition erforderlich ist: Die für die Konfiguration relevante Definition (z.B. Zählzeitdefinition des NB) wurde im Rahmen der Use-Cases des Kapitels „Austausch zu Zählzeit-, Schaltzeit-, Leistungskurvendefinitionen“ ausgetauscht.
  - Im Fall der Bestellung einer Konfiguration, für die eine Zählzeitdefinition des NB erforderlich ist:
    - Die vom LF gewünschte Zählzeitdefinition des NB ist als „bestellbar“ gekennzeichnet worden.
    - Es handelt sich um eine verbrauchende Marktlokation.

</li>

<li data-blatt="ergebnisse">

### Ergebnisse

- Sofern durch die Einrichtung der Konfiguration eine Änderung der Abrechnungsdaten (z.B. Änderung des Bilanzierungsverfahrens) (GPKE Teil 2) oder weiterer Stammdaten (GPKE Teil 4) erforderlich wird, führt der NB den entsprechenden Use-Case aus.

</li>

<li data-blatt="fehlerfall">

### Fehlerfall

#### Ergebnis im Fehlerfall

- Der LF prüft, ob eine erneute Beauftragung der Konfiguration erforderlich ist.
- Die bisher vorhandene Konfiguration bleibt bestehen.

#### Fehlerfälle

- Es handelt sich um eine kostenpflichtige Konfiguration.
- Der Marktpartner ist zum bestellten Beginn des Wirkungszeitraums der betroffenen Lokation nicht zugeordnet.
- Die zum bestellten Zeitpunkt vorhandene Gerätetechnik ermöglicht die Einrichtung der Konfiguration nicht. Dies bedeutet z.B. im Fall der Änderung des Bilanzierungsverfahrens, dass nicht alle Messlokationen der Marktlokation mit kME mit RLM ausgestattet sind.
- Im Fall der Bestellung einer Konfiguration, für die eine Zählzeitdefinition, Schaltzeitdefinition oder Leistungskurvendefinition erforderlich ist: Die für die Konfiguration relevante Definition (z.B. Zählzeitdefinition des NB) wurde im Rahmen der Use-Cases des Kapitels „Austausch zu Zählzeit-, Schaltzeit-, Leistungskurvendefinitionen“ nicht ausgetauscht.
- Im Fall der Bestellung einer Konfiguration, für die eine Zählzeitdefinition des NB erforderlich ist:
  - Die vom LF gewünschte Zählzeitdefinition des NB ist nicht als „bestellbar“ gekennzeichnet worden.
  - Es handelt sich um eine erzeugende Marktlokation bzw. eine Tranche.
- Der LF möchte eine Zählzeitdefinition des LF bestellen.
- Es liegen nicht alle Parameter oder falsche Parameter für die Konfiguration vor.

</li>

<li data-blatt="anforderungen">

### Weitere Anforderungen

Sofern die zum bestellten Zeitpunkt vorhandene Gerätetechnik die Einrichtung der Konfiguration nicht ermöglicht, ist die Änderung der Gerätetechnik nicht über diesen Use-Case zu bestellen. Eine entsprechende Änderung der Gerätetechnik kann im Rahmen eines Gerätewechsels bzw. über die WiM Use-Cases zur Messlokationsänderung (WiM Teil 1) beauftragt werden.

</li>

<li data-blatt="anlass">

### Anlass

- Der LF hat den Bedarf eine Konfiguration einrichten zu lassen, die der NB verantwortet.
- Im Fall der Bestellung einer Konfiguration, für die eine Zählzeitdefinition des NB erforderlich ist: Der LF möchte für den Zählzeitenanwendungszweck „Netznutzung“ die bisher vorhandene Konfiguration einer Marktlokation ändern (inkl. Rückkehr zur Eintariflogik).

**Vorher läuft:** [Übermittlung einer Definition des NB durch den NB](/prozessdoku/202604/LF/GPKE-Teil3-uebermittlung-einer-definition-des-nb-durch-den-nb) — diese Prozesse nennen den hier gezeigten in ihrem Ergebnis.

</li>

<li data-blatt="erste-nachricht">

### Erste Nachricht

Der Beteiligte dieser Seite sendet selbst: „Bestellung einer Konfiguration auf Ebene der direkt betroffenen Lokation“ an **NB** (Schritt 1).

</li>

<li data-blatt="ziel">

### Ziel

Die Bestellung der Konfiguration (z.B. Messprodukt) für die betroffenen Lokationen (z.B. Messlokation, Marktlokation) wurde vom NB bestätigt.

</li>

</ol>
</Stepper>

<a id="abschnitt-sichten"></a>

## Andere Sichten des Prozesses

Derselbe Prozess, aus den Augen der anderen Beteiligten: dieselben Schritte, jeweils aus deren Sicht gelesen.

- [Sicht NB](/prozessdoku/202604/NB/GPKE-Teil3-bestellung-einer-konfiguration-vom-lf-an-nb) — NB

<Hinweisbereich>

*Die Schritte sind die **möglichen** Nachrichten dieses Prozesses, keine Abfolge — die Quelle führt weder Bedingungen noch Alternativen. Das Kästchen am Schritt nennt links die eigene Sicht: **←** empfängt sie, **→** sendet sie. Zugeklappte Schritte laufen zwischen anderen Marktpartnern. Die Nummern sind die der Quelle; wo eine fehlt, fehlt sie dort.*

Die Konnektortabelle führt für diese Schritte keinen Schreibaufruf. Abgeleitet aus dem Prozessverlauf: Die eigene Rolle war an diesem Prozess schon beteiligt, der Vorgang besteht also.

Betrifft: [2](#schritt-2)

</Hinweisbereich>
