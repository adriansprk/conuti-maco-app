# Lieferbeginn — Sicht LFN

<Kopf rolle="LF" beteiligter="LFN" festlegung="GPKE" dokument="GPKE Teil 2" kapitel="2.1.2" sparte="Strom" schritte={8} suchtitel="Lieferbeginn — Sicht LFN (Marktrolle LF) · GPKE Teil 2 · Formatversion 202604" stichworte="Lieferantenwechsel" abschnitte={[{"id": "abschnitt-ablauf", "label": "Prozessablauf"}, {"id": "abschnitt-schritte", "label": "Prozessschritte"}, {"id": "abschnitt-informationen", "label": "Prozess-Informationen"}, {"id": "abschnitt-sichten", "label": "Andere Sichten des Prozesses"}]} />

<Kurzfassung>

Ein LFN meldet beim NB eine Zuordnung des LFN zu einer Marktlokation bzw. Tranche an. Im Zuge des Prozesses
- beendet der NB ggf. die Zuordnung des LFA zur Marktlokation bzw. Tranche.
- hebt der NB ggf. die Zuordnung des LFZ zur Marktlokation bzw. Tranche auf.

</Kurzfassung>

<a id="abschnitt-ablauf"></a>

## Prozessablauf aus Sicht des LF (LFN)

<Systembild svg={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1004 1034\" width=\"1004\" height=\"1034\" role=\"img\" aria-labelledby=\"sb-title\" class=\"maco-systembild\">\n<title id=\"sb-title\">Systembild: Lieferbeginn aus Sicht LF</title>\n<defs><marker id=\"sb-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect class=\"sb-lane-kopf\" x=\"16\" y=\"12\" width=\"232\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend-System des Kunden</text>\n<rect class=\"sb-lane-kopf\" x=\"398\" y=\"12\" width=\"264\" height=\"46\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · LFN</text>\n<rect class=\"sb-lane-kopf\" x=\"812\" y=\"12\" width=\"176\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"900\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Marktpartner</text>\n<line x1=\"323\" y1=\"58\" x2=\"323\" y2=\"1022\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"737\" y1=\"58\" x2=\"737\" y2=\"1022\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect class=\"sb-kasten sb-trigger\" x=\"432\" y=\"80\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessauslöser empfangen</text>\n<rect class=\"sb-kasten sb-backend sb-trigger\" x=\"34\" y=\"80\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">START_LIEFERBEGINN</text>\n<line x1=\"230\" y1=\"96\" x2=\"432\" y2=\"96\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"88\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"144\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"164\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">1. Anmeldung einer</text>\n<text x=\"530\" y=\"179\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Zuordnung des LFN zur</text>\n<text x=\"530\" y=\"194\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Marktlokation bzw. Tr…</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"113\" x2=\"530\" y2=\"144\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"157\" r=\"5\"/><line x1=\"900\" y1=\"162\" x2=\"900\" y2=\"174\"/><line x1=\"893\" y1=\"166\" x2=\"907\" y2=\"166\"/><line x1=\"900\" y1=\"174\" x2=\"894\" y2=\"184\"/><line x1=\"900\" y1=\"174\" x2=\"906\" y2=\"184\"/></g>\n<text x=\"900\" y=\"206\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"628\" y1=\"175\" x2=\"878\" y2=\"175\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"167\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"191\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">55001, 55077</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"233\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"253\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"207\" x2=\"530\" y2=\"233\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"233\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"253\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"249\" x2=\"230\" y2=\"249\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"241\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"297\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"317\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">2. Information über</text>\n<text x=\"530\" y=\"332\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">existierende Zuordnung</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"266\" x2=\"530\" y2=\"297\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"303\" r=\"5\"/><line x1=\"900\" y1=\"308\" x2=\"900\" y2=\"320\"/><line x1=\"893\" y1=\"312\" x2=\"907\" y2=\"312\"/><line x1=\"900\" y1=\"320\" x2=\"894\" y2=\"330\"/><line x1=\"900\" y1=\"320\" x2=\"906\" y2=\"330\"/></g>\n<text x=\"900\" y=\"352\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"878\" y1=\"321\" x2=\"628\" y2=\"321\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"313\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"337\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">55036</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"380\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"400\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z33</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"345\" x2=\"530\" y2=\"380\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"444\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"464\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"413\" x2=\"530\" y2=\"444\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"444\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"464\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"460\" x2=\"230\" y2=\"460\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"452\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"508\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"528\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">5. Zuordnung des LFN zur</text>\n<text x=\"530\" y=\"543\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Marktlokation bzw. Tranche</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"477\" x2=\"530\" y2=\"508\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"514\" r=\"5\"/><line x1=\"900\" y1=\"519\" x2=\"900\" y2=\"531\"/><line x1=\"893\" y1=\"523\" x2=\"907\" y2=\"523\"/><line x1=\"900\" y1=\"531\" x2=\"894\" y2=\"541\"/><line x1=\"900\" y1=\"531\" x2=\"906\" y2=\"541\"/></g>\n<text x=\"900\" y=\"563\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"878\" y1=\"532\" x2=\"628\" y2=\"532\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"524\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"548\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">55002, 55078</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"591\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"611\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z33</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"556\" x2=\"530\" y2=\"591\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"655\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"675\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"624\" x2=\"530\" y2=\"655\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"655\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"675\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"671\" x2=\"230\" y2=\"671\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"663\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-lesen_verarbeitung\" x=\"432\" y=\"719\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"739\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Daten für die Verarbeitung</text>\n<text x=\"530\" y=\"754\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">laden</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"688\" x2=\"530\" y2=\"719\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-lesen_verarbeitung\" x=\"34\" y=\"719\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"739\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">7 Lese-Schnittstellen</text>\n<text x=\"132\" y=\"754\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">aufgerufen</text>\n<line x1=\"432\" y1=\"743\" x2=\"230\" y2=\"743\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"735\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<text x=\"331\" y=\"759\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">je einzeln am Schritt</text>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"793\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"813\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">6. Ablehnung der Anmeldung</text>\n<text x=\"530\" y=\"828\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">einer Zuordnung des LFN zur</text>\n<text x=\"530\" y=\"843\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Marktlo…</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"767\" x2=\"530\" y2=\"793\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"806\" r=\"5\"/><line x1=\"900\" y1=\"811\" x2=\"900\" y2=\"823\"/><line x1=\"893\" y1=\"815\" x2=\"907\" y2=\"815\"/><line x1=\"900\" y1=\"823\" x2=\"894\" y2=\"833\"/><line x1=\"900\" y1=\"823\" x2=\"906\" y2=\"833\"/></g>\n<text x=\"900\" y=\"855\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"878\" y1=\"824\" x2=\"628\" y2=\"824\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"816\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"840\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">55003, 55080</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"882\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"902\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z33</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"856\" x2=\"530\" y2=\"882\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"946\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"966\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"915\" x2=\"530\" y2=\"946\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"946\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"966\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"962\" x2=\"230\" y2=\"962\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"954\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n</svg>"} gesamt={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1218 933\" width=\"1218\" height=\"933\" role=\"img\" aria-labelledby=\"sd-title\" class=\"maco-sequence\">\n<title id=\"sd-title\">Sequenzdiagramm: Lieferbeginn aus Sicht LF</title>\n<defs><marker id=\"sd-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect x=\"16\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"121\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend (Kunde)</text>\n<line x1=\"121\" y1=\"64\" x2=\"121\" y2=\"921\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"260\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"365\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · LFN</text>\n<line x1=\"365\" y1=\"64\" x2=\"365\" y2=\"921\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"504\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"609\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">NB</text>\n<line x1=\"609\" y1=\"64\" x2=\"609\" y2=\"921\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"748\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"853\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">LFA</text>\n<line x1=\"853\" y1=\"64\" x2=\"853\" y2=\"921\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"992\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"1097\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">LFZ</text>\n<line x1=\"1097\" y1=\"64\" x2=\"1097\" y2=\"921\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"121\" y1=\"90\" x2=\"365\" y2=\"90\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"81\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">START_LIEFERBEGINN</text>\n<text x=\"243\" y=\"105\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Trigger-Event</text>\n<line x1=\"365\" y1=\"152\" x2=\"609\" y2=\"152\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"143\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">1. Anmeldung einer Zuordnung des LFN zur Marktlo…</text>\n<text x=\"487\" y=\"167\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55001, 55077</text>\n<line x1=\"365\" y1=\"214\" x2=\"121\" y2=\"214\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"205\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"229\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"609\" y1=\"276\" x2=\"365\" y2=\"276\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"267\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">2. Information über existierende Zuordnung</text>\n<text x=\"487\" y=\"291\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55036</text>\n<line x1=\"365\" y1=\"338\" x2=\"121\" y2=\"338\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"329\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"353\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"609\" y1=\"400\" x2=\"853\" y2=\"400\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"731\" y=\"391\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">3. Anfrage zur Beendigung der Zuordnung des LFA…</text>\n<text x=\"731\" y=\"415\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55010</text>\n<line x1=\"853\" y1=\"462\" x2=\"609\" y2=\"462\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"731\" y=\"453\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">4. Antwort auf Anfrage zur Beendigung der Zuordn…</text>\n<text x=\"731\" y=\"477\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55011, 55012 · E_0624</text>\n<text x=\"731\" y=\"490\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0624 — Anfrage zur Beendigung der Zuordnung prüfen</text>\n<line x1=\"609\" y1=\"524\" x2=\"365\" y2=\"524\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"515\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">5. Zuordnung des LFN zur Marktlokation bzw. Tran…</text>\n<text x=\"487\" y=\"539\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55002, 55078 · E_0623</text>\n<text x=\"487\" y=\"552\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0623 — Lieferbeginn prüfen</text>\n<line x1=\"365\" y1=\"586\" x2=\"121\" y2=\"586\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"577\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"601\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"609\" y1=\"648\" x2=\"365\" y2=\"648\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"639\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">6. Ablehnung der Anmeldung einer Zuordnung des L…</text>\n<text x=\"487\" y=\"663\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55003, 55080 · E_0622, E_0623</text>\n<text x=\"487\" y=\"676\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0622 — Prüfen, ob Anmeldung direkt ablehnbar</text>\n<text x=\"487\" y=\"689\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0623 — Lieferbeginn prüfen</text>\n<line x1=\"365\" y1=\"723\" x2=\"121\" y2=\"723\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"714\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"738\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"609\" y1=\"785\" x2=\"853\" y2=\"785\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"731\" y=\"776\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">10. Beendigung der Zuordnung des LFA zur Marktlok…</text>\n<text x=\"731\" y=\"800\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55037</text>\n<line x1=\"609\" y1=\"847\" x2=\"1097\" y2=\"847\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"853\" y=\"838\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">13. Aufhebung der Zuordnung des LFZ zur Marklokat…</text>\n<text x=\"853\" y=\"862\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55038</text>\n</svg>"} titel="LFN" />

<a id="abschnitt-schritte"></a>

## Prozessschritte

<Schritt nr="1" anker="schritt-1" richtung="ausgehend" kopf={{"links": {"label": "LFN", "eigen": true}, "rechts": {"label": "NB"}}}>

### Anmeldung einer Zuordnung des LFN zur Marktlokation bzw. Tranche

<Schrittskizze sicht={{"label": "LFN"}} zeilen={[{"art": "ausloeser", "werte": ["START_LIEFERBEGINN"]}, {"art": "senden", "label": "NB", "weg": "AS4", "nachrichten": [{"nr": "55001", "titel": "Anmeldung verb. MaLo"}, {"nr": "55077", "titel": "Anmeldung erz. MaLo"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55001](/schnittstellen/202604/pruefi/UTILMD/PI_55001) — Anmeldung verb. MaLo · AS4
- [55077](/schnittstellen/202604/pruefi/UTILMD/PI_55077) — Anmeldung erz. MaLo · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="ausloeser">

**Prozessauslöser** [`START_LIEFERBEGINN`](/schnittstellen/202604/trigger/events/LF-START_LIEFERBEGINN) · [Im Playground ausprobieren](/api/202604/ausloeser-lf/start-lieferbeginn)

Das Backend stößt diesen Schritt mit diesem Ereignis an.

</li>

<li data-teil="nachricht">

Nachricht an **NB** · AS4

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202604/backend-schreiben-lf/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": false, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"ENERGIELIEFERVERTRAG\": [\n      {\n        \"boTyp\": \"VERTRAG\",\n        \"enFG\": [\n          {\n            \"grund\": [\n              \"ENFG_STROMSPEICHER_UND_VERLUSTENERGIE\"\n            ],\n            \"grundlageVerringerungUmlagen\": \"ERFUELLT_VORAUSSETZUNG_NACH_ENFG\"\n          }\n        ],\n        \"korrespondenzpartner\": {\n          \"boTyp\": \"GESCHAEFTSPARTNER\",\n          \"gewerbekennzeichnung\": false,\n          \"name1\": \"Max\",\n          \"partneradresse\": {\n            \"hausnummer\": \"46\",\n            \"landescode\": \"DE\",\n            \"ort\": \"Weimar\",\n            \"postfach\": \"Str\",\n            \"postleitzahl\": \"99423\",\n            \"strasse\": \"Erfurter\"\n          },\n          \"versionStruktur\": \"1\"\n        },\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\",\n        \"vertragsart\": \"ENERGIELIEFERVERTRAG\",\n        \"vertragspartner2\": [\n          {\n            \"boTyp\": \"GESCHAEFTSPARTNER\",\n            \"geschaeftspartnerrolle\": [\n              \"KUNDE\"\n            ],\n            \"gewerbekennzeichnung\": false,\n            \"name1\": \"Max\",\n            \"name2\": \"Mustermann\",\n            \"versionStruktur\": \"1\"\n          }\n        ]\n      }\n    ],\n    \"MARKTLOKATION\": [\n      {\n        \"boTyp\": \"MARKTLOKATION\",\n        \"erforderlichesProduktpaket\": [\n          {\n            \"produkt\": [\n              {\n                \"codeProdukteigenschaft\": \"9991000002131\",\n                \"produktCode\": \"9991000002016\"\n              },\n              {\n                \"produktCode\": \"9991000002082\",\n                \"wertedetails\": \"11XEONBAYERN---I\"\n              },\n              {\n                \"codeProdukteigenschaft\": \"9991000002115\",\n                \"produktCode\": \"9991000002008\"\n              },\n              {\n                \"codeProdukteigenschaft\": \"9991000002785\",\n                \"produktCode\": \"9991000002727\"\n              }\n            ],\n            \"produktpaketId\": 1,\n            \"umsetzungsgradvorgabe\": \"ZUORDNUNG_NUR_WENN_PRODUKTPAKET_UMSETZBAR\"\n          }\n        ],\n        \"marktlokationsId\": \"50363198100\",\n        \"marktlokationsTyp\": [\n          {\n            \"typ\": \"STANDARD_MARKTLOKATION\"\n          }\n        ],\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"NETZNUTZUNGSVERTRAG\": [\n      {\n        \"boTyp\": \"VERTRAG\",\n        \"lokationsId\": \"50363198100\",\n        \"lokationsTyp\": \"MALO\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\",\n        \"vertragsart\": \"NETZNUTZUNGSVERTRAG\",\n        \"vertragsbeginn\": \"2024-12-01T23:00:00Z\",\n        \"vertragsende\": \"2024-12-02T23:00:00Z\",\n        \"vertragskonditionen\": {\n          \"haushaltskunde\": true\n        }\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9980000000001\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"datenaustauschreferenz\": \"M2N2K9NH\",\n    \"dokumentennummer\": \"BGMM2RS5P0Q\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9980000000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"E01\",\n    \"nachrichtendatum\": \"2024-10-14T09:45:00Z\",\n    \"nachrichtenreferenznummer\": \"UNHM2M4CSVV\",\n    \"pruefidentifikator\": \"55001\",\n    \"sparte\": \"STROM\",\n    \"transaktionsgrund\": \"E01\",\n    \"transaktionsgrundergaenzung\": \"ZW4\",\n    \"transaktionsgrundergaenzungBefristeteAnmeldung\": \"E01\",\n    \"vertragsbeginn\": \"2024-12-01T23:00:00Z\",\n    \"vertragsende\": \"2024-12-02T23:00:00Z\",\n    \"vorgangsnummer\": \"KBG27094210000000000929931413171000\"\n  },\n  \"zusatzdaten\": {}\n}"} examples={[{"mediaType": "application/json", "examples": [{"name": "55001", "summary": "55001 — Anmeldung verb. MaLo", "value": {"stammdaten": {"MARKTLOKATION": [{"boTyp": "MARKTLOKATION", "versionStruktur": "1", "marktlokationsId": "50363198100", "marktlokationsTyp": [{"typ": "STANDARD_MARKTLOKATION"}], "sparte": "STROM", "erforderlichesProduktpaket": [{"produktpaketId": 1, "produkt": [{"produktCode": "9991000002016", "codeProdukteigenschaft": "9991000002131"}, {"produktCode": "9991000002082", "wertedetails": "11XEONBAYERN---I"}, {"produktCode": "9991000002008", "codeProdukteigenschaft": "9991000002115"}, {"produktCode": "9991000002727", "codeProdukteigenschaft": "9991000002785"}], "umsetzungsgradvorgabe": "ZUORDNUNG_NUR_WENN_PRODUKTPAKET_UMSETZBAR"}]}], "NETZNUTZUNGSVERTRAG": [{"boTyp": "VERTRAG", "versionStruktur": "1", "vertragsart": "NETZNUTZUNGSVERTRAG", "sparte": "STROM", "vertragsbeginn": "2024-12-01T23:00:00Z", "vertragsende": "2024-12-02T23:00:00Z", "vertragskonditionen": {"haushaltskunde": true}, "lokationsId": "50363198100", "lokationsTyp": "MALO"}], "ENERGIELIEFERVERTRAG": [{"boTyp": "VERTRAG", "versionStruktur": "1", "vertragsart": "ENERGIELIEFERVERTRAG", "sparte": "STROM", "vertragspartner2": [{"boTyp": "GESCHAEFTSPARTNER", "versionStruktur": "1", "name1": "Max", "name2": "Mustermann", "gewerbekennzeichnung": false, "geschaeftspartnerrolle": ["KUNDE"]}], "korrespondenzpartner": {"boTyp": "GESCHAEFTSPARTNER", "versionStruktur": "1", "name1": "Max", "gewerbekennzeichnung": false, "partneradresse": {"postleitzahl": "99423", "ort": "Weimar", "strasse": "Erfurter", "hausnummer": "46", "postfach": "Str", "landescode": "DE"}}, "enFG": [{"grundlageVerringerungUmlagen": "ERFUELLT_VORAUSSETZUNG_NACH_ENFG", "grund": ["ENFG_STROMSPEICHER_UND_VERLUSTENERGIE"]}]}]}, "transaktionsdaten": {"datenaustauschreferenz": "M2N2K9NH", "sparte": "STROM", "transaktionsgrund": "E01", "transaktionsgrundergaenzung": "ZW4", "transaktionsgrundergaenzungBefristeteAnmeldung": "E01", "vorgangsnummer": "KBG27094210000000000929931413171000", "pruefidentifikator": "55001", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9980000000001", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9980000000002", "rollencodetyp": "BDEW"}, "dokumentennummer": "BGMM2RS5P0Q", "kategorie": "E01", "nachrichtendatum": "2024-10-14T09:45:00Z", "nachrichtenreferenznummer": "UNHM2M4CSVV", "vertragsbeginn": "2024-12-01T23:00:00Z", "vertragsende": "2024-12-02T23:00:00Z"}, "zusatzdaten": {}}}, {"name": "55077", "summary": "55077 — Anmeldung erz. MaLo", "value": {"stammdaten": {"MARKTLOKATION": [{"boTyp": "MARKTLOKATION", "versionStruktur": "1", "marktlokationsId": "20072281644", "sparte": "STROM", "foerderungsLand": "DE", "erforderlichesProduktpaket": [{"produktpaketId": 1, "produkt": [{"produktCode": "9991000002082", "wertedetails": "11XBKA---------I"}, {"produktCode": "9991000002090", "codeProdukteigenschaft": "9991000003014", "wertedetails": "50"}, {"produktCode": "9991000002066", "codeProdukteigenschaft": "9991000002272"}], "umsetzungsgradvorgabe": "ZUORDNUNG_NUR_WENN_PRODUKTPAKET_UMSETZBAR", "priorisierung": "PRIORITAET1"}, {"produktpaketId": 2, "produkt": [{"produktCode": "9991000002404", "codeProdukteigenschaft": "9991000002420"}, {"produktCode": "9991000002082", "wertedetails": "22XBKA---------I"}, {"produktCode": "9991000002090", "codeProdukteigenschaft": "9991000003014", "wertedetails": "50"}, {"produktCode": "9991000002066", "codeProdukteigenschaft": "9991000002272"}, {"produktCode": "9991000002404", "codeProdukteigenschaft": "9991000002420"}], "umsetzungsgradvorgabe": "ZUORDNUNG_NUR_WENN_PRODUKTPAKET_UMSETZBAR", "priorisierung": "PRIORITAET2"}]}], "NETZNUTZUNGSVERTRAG": [{"boTyp": "VERTRAG", "versionStruktur": "1", "vertragsart": "NETZNUTZUNGSVERTRAG", "sparte": "STROM", "vertragsbeginn": "2025-11-01T23:00:00Z", "lokationsId": "20072281644", "lokationsTyp": "MALO"}]}, "transaktionsdaten": {"datenaustauschreferenz": "DAZBHQXEUJALSE", "sparte": "STROM", "transaktionsgrund": "E03", "transaktionsgrundergaenzung": "ZW2", "vorgangsnummer": "24062416225400000000000102159662022", "pruefidentifikator": "55077", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9903729000007", "rollencodetyp": "BDEW", "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "nachname": "P GETTY", "rufnummern": [{"nummerntyp": "RUF_DURCHWAHL", "rufnummer": "+3222271020"}]}}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900327000009", "rollencodetyp": "BDEW"}, "dokumentennummer": "DA672410170839449903323000007966941", "kategorie": "E01", "nachrichtendatum": "2025-06-24T12:31:00Z", "nachrichtenreferenznummer": "DAOHDSWRBRFDIO", "abtretungserklaerung": {"passwort": "KNSG5674?\"§", "link1": "https://www.Stadtwerk_xy.de/...", "link2": "X", "link3": "X", "link4": "X", "link5": "X"}}, "zusatzdaten": {}}}]}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend fort, nachdem die Nachricht erstellt ist.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="2" anker="schritt-2" richtung="eingehend" kopf={{"links": {"label": "LFN", "eigen": true}, "rechts": {"label": "NB"}}}>

### Information über existierende Zuordnung

<Schrittskizze sicht={{"label": "LFN"}} zeilen={[{"art": "empfangen", "label": "NB", "weg": "AS4", "nachrichten": [{"nr": "55036", "titel": "Existierende Zuordnung"}]}, {"art": "aperak", "werte": ["Z33"]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55036](/schnittstellen/202604/pruefi/UTILMD/PI_55036) — Existierende Zuordnung · AS4

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
- `55036` → `Z33` — Aperak Prüfung: Ist referenzierte Nachricht bekannt ?

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202604/backend-schreiben-lf/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": false, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"MARKTLOKATION\": [\n      {\n        \"beteiligterMarktpartner\": {\n          \"boTyp\": \"MARKTTEILNEHMER\",\n          \"rollencodenummer\": \"4041409000006\",\n          \"rollencodetyp\": \"BDEW\",\n          \"versionStruktur\": \"1\"\n        },\n        \"boTyp\": \"MARKTLOKATION\",\n        \"marktlokationsId\": \"50226146170\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9900321000005\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"anfragereferenznummer\": \"PCL53523092914504899116940000022575\",\n    \"beteiligterMarktpartner\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"4041409000006\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"datenaustauschreferenz\": \"041391878572\",\n    \"dokumentennummer\": \"041391878573\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9903790000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"E01\",\n    \"nachrichtendatum\": \"2024-04-01T15:35:00Z\",\n    \"nachrichtenreferenznummer\": \"041391878573\",\n    \"pruefidentifikator\": \"55036\",\n    \"sparte\": \"STROM\",\n    \"transaktionsgrund\": \"Z26\",\n    \"vorgangsnummer\": \"XX5056854C0F1EDE98A6A597473530A3\"\n  },\n  \"zusatzdaten\": {}\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend mit den Daten der eingegangenen Nachricht fort.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="3" anker="schritt-3" richtung="fremd" kopf={{"links": {"label": "NB", "eigen": false}, "rechts": {"label": "LFA"}}}>

### Anfrage zur Beendigung der Zuordnung des LFA zur Marktlokation bzw. Tranche

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55010](/schnittstellen/202604/pruefi/UTILMD/PI_55010) — Anfrage zur Beendigung der Zuordnung · AS4

</div>

</Schritt>

<Schritt nr="4" anker="schritt-4" richtung="fremd" kopf={{"links": {"label": "LFA", "eigen": false}, "rechts": {"label": "NB"}}}>

### Antwort auf Anfrage zur Beendigung der Zuordnung des LFA zur Marktlokation bzw. Tranche

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55011](/schnittstellen/202604/pruefi/UTILMD/PI_55011) — Bestätigung Beendigung der Zuordnung · AS4
- [55012](/schnittstellen/202604/pruefi/UTILMD/PI_55012) — Ablehnung Beendigung der Zuordnung · AS4

</div>

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `55011`, `55012` → [E_0624](/referenz/202604/ebd/E_0624) · LF · Anfrage zur Beendigung der Zuordnung prüfen

</div>

</Schritt>

<Schritt nr="5" anker="schritt-5" richtung="eingehend" kopf={{"links": {"label": "LFN", "eigen": true}, "rechts": {"label": "NB"}}}>

### Zuordnung des LFN zur Marktlokation bzw. Tranche

<Schrittskizze sicht={{"label": "LFN"}} zeilen={[{"art": "empfangen", "label": "NB", "weg": "AS4", "nachrichten": [{"nr": "55002", "titel": "Bestätigung Anmeldung verb. MaLo"}, {"nr": "55078", "titel": "Bestätigung Anmeldung erz. MaLo"}]}, {"art": "aperak", "werte": ["Z33"]}, {"art": "fortschreiben"}, {"art": "lesen_verarbeitung", "schnittstellen": [{"label": "Energieliefervertrag lesen"}, {"label": "Lokationsbündel lesen"}, {"label": "Messlokation lesen"}, {"label": "Messstellenbetriebsvertrag lesen"}, {"label": "Netzlokation lesen"}, {"label": "Netznutzungsvertrag lesen"}, {"label": "Zähler lesen"}]}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55002](/schnittstellen/202604/pruefi/UTILMD/PI_55002) — Bestätigung Anmeldung verb. MaLo · AS4
- [55078](/schnittstellen/202604/pruefi/UTILMD/PI_55078) — Bestätigung Anmeldung erz. MaLo · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **NB** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `55002`, `55078` → [E_0623](/referenz/202604/ebd/E_0623) · NB · Lieferbeginn prüfen

</div>

</li>

<li data-teil="aperak">

**Aperak-Prüfungen**
- `55002`, `55078` → `Z33` — Aperak Prüfung: Ist referenzierte Nachricht bekannt ?

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202604/backend-schreiben-lf/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": false, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"MARKTLOKATION\": [\n      {\n        \"boTyp\": \"MARKTLOKATION\",\n        \"marktlokationsId\": \"50363198100\",\n        \"marktlokationsTyp\": [\n          {\n            \"typ\": \"STANDARD_MARKTLOKATION\"\n          }\n        ],\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      },\n      {\n        \"boTyp\": \"MARKTLOKATION\",\n        \"marktlokationsId\": \"50363198102\",\n        \"marktlokationsTyp\": [\n          {\n            \"typ\": \"RUHENDE_MARKTLOKATION\"\n          }\n        ],\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"MESSLOKATION\": [\n      {\n        \"boTyp\": \"MESSLOKATION\",\n        \"datenqualitaet\": \"INFORMATIVE_DATEN\",\n        \"marktrollen\": [\n          {\n            \"boTyp\": \"MARKTTEILNEHMER\",\n            \"gewerbekennzeichnung\": true,\n            \"marktrolle\": \"MSB\",\n            \"messstellenbetreiberEigenschaft\": \"GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER\",\n            \"rollencodenummer\": \"9980000000027\",\n            \"rollencodetyp\": \"BDEW\",\n            \"versionStruktur\": \"1\",\n            \"weiterverpflichtet\": false\n          },\n          {\n            \"boTyp\": \"MARKTTEILNEHMER\",\n            \"gewerbekennzeichnung\": true,\n            \"marktrolle\": \"GMSB\",\n            \"rollencodenummer\": \"9980000000023\",\n            \"rollencodetyp\": \"BDEW\",\n            \"versionStruktur\": \"1\"\n          }\n        ],\n        \"messlokationsId\": \"DE0032106765712000000000000001234\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"NETZLOKATION\": [\n      {\n        \"boTyp\": \"NETZLOKATION\",\n        \"datenqualitaet\": \"INFORMATIVE_DATEN\",\n        \"marktrollen\": [\n          {\n            \"boTyp\": \"MARKTTEILNEHMER\",\n            \"gewerbekennzeichnung\": true,\n            \"marktrolle\": \"MSB\",\n            \"messstellenbetreiberEigenschaft\": \"GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER\",\n            \"rollencodenummer\": \"9980000000024\",\n            \"rollencodetyp\": \"BDEW\",\n            \"versionStruktur\": \"1\"\n          }\n        ],\n        \"netzlokationsId\": \"E1688117482\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"NETZNUTZUNGSVERTRAG\": [\n      {\n        \"boTyp\": \"VERTRAG\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\",\n        \"vertragsart\": \"NETZNUTZUNGSVERTRAG\",\n        \"vertragsbeginn\": \"2024-12-01T23:00:00Z\",\n        \"vertragsende\": \"2024-12-02T23:00:00Z\"\n      }\n    ],\n    \"STEUERBARE_RESSOURCE\": [\n      {\n        \"boTyp\": \"STEUERBARE_RESSOURCE\",\n        \"datenqualitaet\": \"INFORMATIVE_DATEN\",\n        \"marktrollen\": [\n          {\n            \"boTyp\": \"MARKTTEILNEHMER\",\n            \"gewerbekennzeichnung\": true,\n            \"marktrolle\": \"MSB\",\n            \"messstellenbetreiberEigenschaft\": \"GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER\",\n            \"rollencodenummer\": \"9980000000026\",\n            \"rollencodetyp\": \"BDEW\",\n            \"versionStruktur\": \"1\"\n          }\n        ],\n        \"ressourcenId\": \"C81641SBT77\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"TECHNISCHE_RESSOURCE\": [\n      {\n        \"boTyp\": \"TECHNISCHE_RESSOURCE\",\n        \"ressourcenId\": \"D417MLM8164\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9980000000001\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"anfragereferenznummer\": \"NNV1230\",\n    \"antwortstatus\": \"A51\",\n    \"antwortstatusCodeliste\": \"E_0623\",\n    \"datenaustauschreferenz\": \"M38VVWXF\",\n    \"dokumentennummer\": \"BGMM2XZHIOV\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9980000000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"geplantesProduktpaket\": 1,\n    \"kategorie\": \"E01\",\n    \"nachrichtendatum\": \"2024-10-15T09:45:00Z\",\n    \"nachrichtenreferenznummer\": \"UNHM2SC7URW\",\n    \"pruefidentifikator\": \"55002\",\n    \"sparte\": \"STROM\",\n    \"transaktionsgrund\": \"E01\",\n    \"transaktionsgrundergaenzung\": \"ZAP\",\n    \"transaktionsgrundergaenzungBefristeteAnmeldung\": \"E01\",\n    \"vertragsbeginn\": \"2024-12-01T23:00:00Z\",\n    \"vertragsende\": \"2024-12-02T23:00:00Z\",\n    \"vorgangsnummer\": \"KBG27094210000000000929931413171000\"\n  },\n  \"zusatzdaten\": {}\n}"} examples={[{"mediaType": "application/json", "examples": [{"name": "55002", "summary": "55002 — Bestätigung Anmeldung verb. MaLo", "value": {"stammdaten": {"MARKTLOKATION": [{"boTyp": "MARKTLOKATION", "versionStruktur": "1", "marktlokationsId": "50363198100", "marktlokationsTyp": [{"typ": "STANDARD_MARKTLOKATION"}], "sparte": "STROM"}, {"boTyp": "MARKTLOKATION", "versionStruktur": "1", "marktlokationsId": "50363198102", "marktlokationsTyp": [{"typ": "RUHENDE_MARKTLOKATION"}], "sparte": "STROM"}], "NETZLOKATION": [{"boTyp": "NETZLOKATION", "versionStruktur": "1", "netzlokationsId": "E1688117482", "sparte": "STROM", "datenqualitaet": "INFORMATIVE_DATEN", "marktrollen": [{"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "marktrolle": "MSB", "gewerbekennzeichnung": true, "rollencodenummer": "9980000000024", "rollencodetyp": "BDEW", "messstellenbetreiberEigenschaft": "GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER"}]}], "MESSLOKATION": [{"boTyp": "MESSLOKATION", "versionStruktur": "1", "messlokationsId": "DE0032106765712000000000000001234", "sparte": "STROM", "datenqualitaet": "INFORMATIVE_DATEN", "marktrollen": [{"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "marktrolle": "MSB", "gewerbekennzeichnung": true, "rollencodenummer": "9980000000027", "rollencodetyp": "BDEW", "weiterverpflichtet": false, "messstellenbetreiberEigenschaft": "GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER"}, {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "marktrolle": "GMSB", "gewerbekennzeichnung": true, "rollencodenummer": "9980000000023", "rollencodetyp": "BDEW"}]}], "TECHNISCHE_RESSOURCE": [{"boTyp": "TECHNISCHE_RESSOURCE", "versionStruktur": "1", "ressourcenId": "D417MLM8164", "sparte": "STROM"}], "STEUERBARE_RESSOURCE": [{"boTyp": "STEUERBARE_RESSOURCE", "versionStruktur": "1", "ressourcenId": "C81641SBT77", "sparte": "STROM", "datenqualitaet": "INFORMATIVE_DATEN", "marktrollen": [{"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "marktrolle": "MSB", "gewerbekennzeichnung": true, "rollencodenummer": "9980000000026", "rollencodetyp": "BDEW", "messstellenbetreiberEigenschaft": "GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER"}]}], "NETZNUTZUNGSVERTRAG": [{"boTyp": "VERTRAG", "versionStruktur": "1", "vertragsart": "NETZNUTZUNGSVERTRAG", "sparte": "STROM", "vertragsbeginn": "2024-12-01T23:00:00Z", "vertragsende": "2024-12-02T23:00:00Z"}]}, "transaktionsdaten": {"datenaustauschreferenz": "M38VVWXF", "sparte": "STROM", "transaktionsgrund": "E01", "transaktionsgrundergaenzung": "ZAP", "transaktionsgrundergaenzungBefristeteAnmeldung": "E01", "vorgangsnummer": "KBG27094210000000000929931413171000", "pruefidentifikator": "55002", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9980000000001", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9980000000002", "rollencodetyp": "BDEW"}, "dokumentennummer": "BGMM2XZHIOV", "kategorie": "E01", "nachrichtendatum": "2024-10-15T09:45:00Z", "nachrichtenreferenznummer": "UNHM2SC7URW", "anfragereferenznummer": "NNV1230", "antwortstatus": "A51", "antwortstatusCodeliste": "E_0623", "geplantesProduktpaket": 1, "vertragsbeginn": "2024-12-01T23:00:00Z", "vertragsende": "2024-12-02T23:00:00Z"}, "zusatzdaten": {}}}, {"name": "55078", "summary": "55078 — Bestätigung Anmeldung erz. MaLo", "value": {"stammdaten": {"MARKTLOKATION": [{"boTyp": "MARKTLOKATION", "versionStruktur": "1", "datenqualitaet": "INFORMATIVE_DATEN", "marktlokationsId": "50074561188", "sparte": "STROM", "marktrollen": [{"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "marktrolle": "MSB", "rollencodenummer": "9904446000007", "weiterverpflichtet": false, "messstellenbetreiberEigenschaft": "GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER"}]}], "MESSLOKATION": [{"boTyp": "MESSLOKATION", "versionStruktur": "1", "datenqualitaet": "INFORMATIVE_DATEN", "messlokationsId": "DE0032106765712000000000000000037", "sparte": "STROM", "marktrollen": [{"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "marktrolle": "MSB", "rollencodenummer": "9904446000007", "weiterverpflichtet": false, "messstellenbetreiberEigenschaft": "GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER"}, {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "marktrolle": "GMSB", "rollencodenummer": "9904446000007"}]}], "NETZNUTZUNGSVERTRAG": [{"boTyp": "VERTRAG", "versionStruktur": "1", "vertragsart": "NETZNUTZUNGSVERTRAG", "sparte": "STROM", "vertragsbeginn": "2025-04-30T22:00:00Z"}]}, "transaktionsdaten": {"datenaustauschreferenz": "LZECUKCK", "sparte": "STROM", "transaktionsgrund": "E03", "transaktionsgrundergaenzung": "ZW0", "vorgangsnummer": "1829631672", "pruefidentifikator": "55078", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9900321000005", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9903790000002", "rollencodetyp": "BDEW"}, "dokumentennummer": "BGMLZULMI89", "kategorie": "E01", "nachrichtendatum": "2025-04-01T07:59:00Z", "nachrichtenreferenznummer": "UNHLZBUIWW9", "anfragereferenznummer": "REF12345678910", "antwortstatus": "A51", "antwortstatusCodeliste": "E_0623", "geplantesProduktpaket": 1, "vertragsbeginn": "2025-04-30T22:00:00Z"}}}]}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend mit den Daten der eingegangenen Nachricht fort.

</li>

<li data-teil="lesen" data-stufe="verarbeitung">

**Daten für die Verarbeitung laden**
- [Energieliefervertrag lesen](/api/202604/backend-lesen/getenergysupplycontractbasic#energieliefervertrag-lesen) `GET /getEnergySupplyContractBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getEnergySupplyContractBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_ENERGIELIEFERVERTRAG_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Lokationsbündel lesen](/api/202604/backend-lesen/getlocationbundlebasic#lokationsbundel-lesen) `GET /getLocationBundleBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getLocationBundleBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_LOKATIONSBUENDEL_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Messlokation lesen](/api/202604/backend-lesen/getmeterlocationbasic#messlokation-lesen) `GET /getMeterLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getMeterLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_MESSLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Messstellenbetriebsvertrag lesen](/api/202604/backend-lesen/getmeasuringpointoperationcontractbasic#messstellenbetriebsvertrag-lesen) `GET /getMeasuringPointOperationContractBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getMeasuringPointOperationContractBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_MESSSTELLENBETRIEBSVERTRAG_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Netzlokation lesen](/api/202604/backend-lesen/getgridlocationbasic#netzlokation-lesen) `GET /getGridLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getGridLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_NETZLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Netznutzungsvertrag lesen](/api/202604/backend-lesen/getgridusagecontractbasic#netznutzungsvertrag-lesen) `GET /getGridUsageContractBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getGridUsageContractBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": false, "defaultValue": "MALO", "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": false, "defaultValue": "2024-06-28T12:18:00Z", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Zähler lesen](/api/202604/backend-lesen/getcounterbasic#zahler-lesen) `GET /getCounterBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getCounterBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="6" anker="schritt-6" richtung="eingehend" kopf={{"links": {"label": "LFN", "eigen": true}, "rechts": {"label": "NB"}}}>

### Ablehnung der Anmeldung einer Zuordnung des LFN zur Marktlokation bzw. Tranche

<Schrittskizze sicht={{"label": "LFN"}} zeilen={[{"art": "empfangen", "label": "NB", "weg": "AS4", "nachrichten": [{"nr": "55003", "titel": "Ablehnung Anmeldung verb. MaLo"}, {"nr": "55080", "titel": "Ablehnung Anmeldung erz. MaLo"}]}, {"art": "aperak", "werte": ["Z33"]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55003](/schnittstellen/202604/pruefi/UTILMD/PI_55003) — Ablehnung Anmeldung verb. MaLo · AS4
- [55080](/schnittstellen/202604/pruefi/UTILMD/PI_55080) — Ablehnung Anmeldung erz. MaLo · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **NB** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `55003`, `55080` → [E_0622](/referenz/202604/ebd/E_0622) · NB · Prüfen, ob Anmeldung direkt ablehnbar
- `55003`, `55080` → [E_0623](/referenz/202604/ebd/E_0623) · NB · Lieferbeginn prüfen

</div>

</li>

<li data-teil="aperak">

**Aperak-Prüfungen**
- `55003`, `55080` → `Z33` — Aperak Prüfung: Ist referenzierte Nachricht bekannt ?

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202604/backend-schreiben-lf/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": false, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {},\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9980000000001\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"anfragereferenznummer\": \"NNV1230\",\n    \"antwortstatus\": \"A06\",\n    \"antwortstatusCodeliste\": \"E_0622\",\n    \"datenaustauschreferenz\": \"M2UMD16C\",\n    \"dokumentennummer\": \"BGMM2OW5IYM\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9980000000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"E01\",\n    \"lieferbeginndatuminbearbeitung\": \"2025-04-02T22:00:00Z\",\n    \"nachrichtendatum\": \"2024-10-21T09:45:00Z\",\n    \"nachrichtenreferenznummer\": \"UNHM3FFAZNS\",\n    \"naechsteBearbeitung\": \"2025-04-02T22:00:00Z\",\n    \"pruefidentifikator\": \"55003\",\n    \"sparte\": \"STROM\",\n    \"transaktionsgrund\": \"E01\",\n    \"transaktionsgrundergaenzung\": \"ZW4\",\n    \"vorgangsnummer\": \"KBG27094210000000000929931413171000\"\n  },\n  \"zusatzdaten\": {}\n}"} examples={[{"mediaType": "application/json", "examples": [{"name": "55003", "summary": "55003 — Ablehnung Anmeldung verb. MaLo", "value": {"stammdaten": {}, "transaktionsdaten": {"datenaustauschreferenz": "M2UMD16C", "sparte": "STROM", "transaktionsgrund": "E01", "transaktionsgrundergaenzung": "ZW4", "vorgangsnummer": "KBG27094210000000000929931413171000", "pruefidentifikator": "55003", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9980000000001", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9980000000002", "rollencodetyp": "BDEW"}, "dokumentennummer": "BGMM2OW5IYM", "kategorie": "E01", "nachrichtendatum": "2024-10-21T09:45:00Z", "nachrichtenreferenznummer": "UNHM3FFAZNS", "anfragereferenznummer": "NNV1230", "antwortstatus": "A06", "antwortstatusCodeliste": "E_0622", "lieferbeginndatuminbearbeitung": "2025-04-02T22:00:00Z", "naechsteBearbeitung": "2025-04-02T22:00:00Z"}, "zusatzdaten": {}}}, {"name": "55080", "summary": "55080 — Ablehnung Anmeldung erz. MaLo", "value": {"stammdaten": {"MARKTLOKATION": [{"boTyp": "MARKTLOKATION", "versionStruktur": "1", "marktlokationsId": "20072281644", "sparte": "STROM", "beteiligterMarktpartner": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9977842000004", "rollencodetyp": "BDEW"}}], "NETZNUTZUNGSVERTRAG": [{"boTyp": "VERTRAG", "versionStruktur": "1", "vertragsart": "NETZNUTZUNGSVERTRAG", "sparte": "STROM", "lokationsId": "20072281644", "lokationsTyp": "MALO"}]}, "transaktionsdaten": {"datenaustauschreferenz": "DAWAGCZDOWMGAU", "sparte": "STROM", "transaktionsgrund": "E03", "transaktionsgrundergaenzung": "ZW3", "vorgangsnummer": "24062416225400000000000102159662022", "pruefidentifikator": "55080", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900327000009", "rollencodetyp": "BDEW", "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "nachname": "P GETTY", "rufnummern": [{"nummerntyp": "RUF_DURCHWAHL", "rufnummer": "+3222271020"}]}}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9903729000007", "rollencodetyp": "BDEW"}, "dokumentennummer": "DA382410161537339903323000007610102", "kategorie": "E01", "nachrichtendatum": "2025-06-24T12:31:00Z", "nachrichtenreferenznummer": "DAMDDBRNVTSFAR", "anfragereferenznummer": "NNV1234", "antwortstatus": "A57", "antwortstatusCodeliste": "E_0623", "antwortstatusdritter": "A30", "antwortstatusdritterCodeliste": "E_0624", "antwortstatusdritterBetroffeneLokation": "ZW3", "antwortstatusdritterReferenz": "20072281644"}, "zusatzdaten": {}}}]}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend mit den Daten der eingegangenen Nachricht fort.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="10" anker="schritt-10" richtung="fremd" kopf={{"links": {"label": "NB", "eigen": false}, "rechts": {"label": "LFA"}}}>

### Beendigung der Zuordnung des LFA zur Marktlokation bzw. Tranche

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55037](/schnittstellen/202604/pruefi/UTILMD/PI_55037) — Beendigung der Zuordnung · AS4

</div>

</Schritt>

<Schritt nr="13" anker="schritt-13" richtung="fremd" kopf={{"links": {"label": "NB", "eigen": false}, "rechts": {"label": "LFZ"}}}>

### Aufhebung der Zuordnung des LFZ zur Marklokation bzw. Tranche

Dieser Schritt läuft zwischen anderen Marktpartnern und ist für diese Sicht nicht relevant.

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55038](/schnittstellen/202604/pruefi/UTILMD/PI_55038) — Aufhebung einer zuk. Zuordnung · AS4

</div>

</Schritt>

<details>
<summary>Entscheidungsbäume dieses Prozesses</summary>

| EBD | Name |
|---|---|
| [E_0622](/referenz/202604/ebd/E_0622) | Prüfen, ob Anmeldung direkt ablehnbar |
| [E_0623](/referenz/202604/ebd/E_0623) | Lieferbeginn prüfen |
| [E_0624](/referenz/202604/ebd/E_0624) | Anfrage zur Beendigung der Zuordnung prüfen |

</details>

<a id="abschnitt-informationen"></a>

## Prozess-Informationen

Wortlaut der Lesefassung, Steckbrief Kap. 2.1.1, S. 12–15.

<Stepper>
<ol>

<li data-blatt="vorbedingungen">

### Vorbedingungen

- Im Fall einer verbrauchenden Marktlokation:
  - Abschluss eines Energieliefervertrags zwischen LFN und dem Letztverbraucher.
- Im Fall einer erzeugenden Marktlokation bzw. einer Tranche:
  - Abschluss eines Stromabnahmevertrags zwischen LFN und dem EZ. Es werden dabei drei Geschäftsvorfälle betrachtet:
    - Geschäftsvorfall 1: Der LFN wird einer Marktlokation vollständig zugeordnet (vollständige (100%ige) Zuordnung). Dieser Geschäftsvorfall ist auch für die Änderung von einer tranchierten Marktlokation in eine nicht tranchierte Marktlokation anzuwenden.
    - Geschäftsvorfall 2: Der LFN wird einer bestehenden Tranche vollständig zugeordnet (vollständige (100%ige) Zuordnung). Dieser Geschäftsvorfall ist bei einem direkten Übergang, d. h. lückenlosem Zuordnungsende und -beginn und unter Beibehaltung der Tranche, anzuwenden.
    - Geschäftsvorfall 3: Der LFN wird einer neu zu bildenden Tranche zugeordnet (anteiliger Zuordnungsvorgang unter Bildung neuer Tranchen). Zudem ist eine Änderung der dem LF zugeordneten Tranchengröße mit diesem Prozess/Geschäftsvorfall 3 zu melden.
  - Der bisherige und neue EZ müssen identisch sein.
  - Die Energie einer Marktlokation, die vollständig oder anteilig zur Veräußerungsform einer DV zugeordnet werden soll, ist mit einer viertelstündlichen Auflösung zu messen.
  - Der Use-Case ist nicht durch das Unternehmen Netzbetreiber in seiner Rolle als LF zu starten.
- Eine Zuordnungsermächtigung nach den Prozessen der MaBiS für den vom LFN genutzten BK liegt beim NB vor.
- Es handelt sich nicht um die erstmalige Inbetriebnahme einer Marktlokation (Neuanlage).
- Die MaLo-ID der Marktlokation ist bekannt bzw. im Geschäftsvorfall 2 ist die MaLo-ID der Tranche bekannt.

</li>

<li data-blatt="ergebnisse">

### Ergebnisse

- Im Fall einer verbrauchenden Marktlokation:
  - Der NB führt die Use-Cases „[Abrechnungsdaten Netznutzungsabrechnung](/prozessdoku/202604/LF/GPKE-Teil2-abrechnungsdaten-netznutzungsabrechnung)“ und „[Abrechnungsdaten Bilanzkreisabrechnung](/prozessdoku/202604/LF/GPKE-Teil2-abrechnungsdaten-bilanzkreisabrechnung)“ aus.
  - Etwa entstehende Zuordnungslücken werden vom NB durch Zuordnung des E/G zur Marktlokation in Anwendung des Use-Cases „[Beginn der Ersatz-/Grundversorgung](/prozessdoku/202604/LF/GPKE-Teil2-beginn-der-ersatz-grundversorgung)“ geschlossen.
  - Sofern die Marktlokation gesperrt ist, führt der NB den Use-Case „[Wiederherstellung der Anschlussnutzung bei Lieferbeginn](/prozessdoku/202604/MSB/GPKE-Teil2-wiederherstellung-der-anschlussnutzung-bei-lieferbeginn)“ aus.
- Im Fall einer erzeugenden Marktlokation bzw. einer Tranche:
  - Der NB führt den Use-Case „[Abrechnungsdaten Bilanzkreisabrechnung](/prozessdoku/202604/LF/GPKE-Teil2-abrechnungsdaten-bilanzkreisabrechnung)“ aus.
  - Etwa entstehende Zuordnungslücken werden vom NB im Rahmen des Use-Cases „Herstellung einer 100% LF-Zuordnung zu einer erzeugenden Marktlokation“ geschlossen.
- Der NB führt den Use-Case „Stammdatenänderung“ (hier: SD „[Stammdatenänderung vom NB (verantwortlich) ausgehend](/prozessdoku/202604/LF/GPKE-Teil4-stammdatenaenderung-vom-nb-verantwortlich-ausgehend)“) (GPKE Teil 4) durch.
- Der NB versendet die Berechnungsformel an den LFN.
- Der NB führt den Use-Case „[Einrichtung der Konfigurationen aufgrund einer Zuordnung eines LF zu einer Marktlokation bzw. Tranche](/prozessdoku/202604/MSB/GPKE-Teil3-einrichtung-der-konfigurationen-aufgrund-einer-zuordnung-eines-lf-zu-einer-marktlokation-bzw-tranche)“ (GPKE Teil 3) aus.
- Der LFN führt den Use-Case „Stammdatenänderung“ (hier: SD „[Stammdatenänderung vom LF (verantwortlich) ausgehend](/prozessdoku/202604/LF/GPKE-Teil4-stammdatenaenderung-vom-lf-verantwortlich-ausgehend)“) (GPKE Teil 4) durch.

</li>

<li data-blatt="fehlerfall">

### Fehlerfall

#### Ergebnis im Fehlerfall

- Der LFN wurde der Marktlokation bzw. Tranche nicht zugeordnet.
- Der LFA bleibt der Marktlokation bzw. Tranche zugeordnet, sofern für diesen nicht bereits die Zuordnung im Rahmen eines anderen Use-Cases (z.B. „Lieferende von LF an NB) beendet wurde.
- Im Fall einer verbrauchenden Marktlokation: Der NB führt ggf. den Use-Case „[Beginn der Ersatz-/Grundversorgung](/prozessdoku/202604/LF/GPKE-Teil2-beginn-der-ersatz-grundversorgung)“ aus.
- Im Fall einer erzeugenden Marktlokation bzw. einer Tranche: Der NB führt ggf. den Use-Case „Herstellung einer 100% LF-Zuordnung zu einer erzeugenden Marktlokation“ aus.
- Der LFN sendet bei Bedarf erneut eine Anmeldung an den NB.

#### Fehlerfälle

- Es handelt sich um die erstmalige Inbetriebnahme einer Marktlokation (Neuanlage).
- Im Fall einer erzeugenden Marktlokation bzw. einer Tranche:
  - Der bisherige und neue EZ sind nicht identisch.
  - Die Energie einer Marktlokation, die vollständig oder anteilig zur Veräußerungsform einer DV zugeordnet werden soll, ist nicht mit einer viertelstündlichen Auflösung messbar.
  - Der Use-Case wird durch das Unternehmen Netzbetreiber in seiner Rolle als LF gestartet.
- Eine Zuordnungsermächtigung nach den Prozessen der MaBiS für den vom LFN genutzten BK liegt beim NB nicht vor.

</li>

<li data-blatt="anforderungen">

### Weitere Anforderungen

- Zuordnungslücken sind dadurch zu vermeiden, dass An- und Abmeldung zeitlich aufeinander abgestimmt werden.
- Hinweis: Ein Erzeugerwechsel an einer erzeugenden Marktlokation oder Anlagenbetreiberwechsel an einer technischen Ressource wird nicht im Rahmen der hier beschriebenen Prozesse abgewickelt. Deren bilaterale Abwicklung zwischen NB und EZ erfolgt gemäß den einschlägigen Bestimmungen der NB.
- Hinweis: Die Zuordnung des LF zur Marktlokation bzw. Tranche bei einer Inbetriebnahme einer Marktlokation (Neuanlage) findet über den Use-Case „[Neuanlage](/prozessdoku/202604/LF/GPKE-Teil2-neuanlage)“, „[Beginn der Ersatz-/Grundversorgung](/prozessdoku/202604/LF/GPKE-Teil2-beginn-der-ersatz-grundversorgung)“ oder „Herstellung einer 100% LF-Zuordnung zu einer erzeugenden Marktlokation“ statt.
- Hinweis: Sofern die zum Zuordnungsbeginn vorhandene Gerätetechnik die Anmeldung nicht ermöglicht, ist eine entsprechende Änderung der Gerätetechnik durch den LFN bzw. Letztverbraucher bzw. EZ beim MSB zu veranlassen. Der LFN kann die Änderung der Gerätetechnik über den WiM-Use-Case zur Messlokationsänderung (WiM Teil 1) beauftragen.
- Hinweis zu erzeugenden Marktlokationen bzw. zu Tranchen: Der LF wendet für eine Änderung der Veräußerungsform (ohne gleichzeitige Zuordnung des LF zur erzeugenden Marktlokation bzw. zur Tranche) den Use-Case "Bestellung einer Änderung von Abrechnungsdaten" an.

</li>

<li data-blatt="anlass">

### Anlass

- Im Fall einer verbrauchenden Marktlokation:
  - Lieferantenwechsel ohne gleichzeitigen Einzug des Letztverbrauchers
  - Lieferantenwechsel mit gleichzeitigem Einzug des Letztverbrauchers
  - Zuordnung des bisherigen LF ohne gleichzeitigen Einzug des Letztverbrauchers (nach einer Beendigung der Zuordnung des LF zur Marktlokation, z.B. aufgrund des Use-Cases "Lieferende von LF an NB")
  - Zuordnung des bisherigen LF mit gleichzeitigem Einzug des Letztverbrauchers.
- Im Fall einer erzeugenden Marktlokation bzw. einer Tranche:
  - Lieferantenwechsel ohne Erzeugerwechsel
  - Zuordnung des bisherigen LF ohne Erzeugerwechsel (nach einer Beendigung der Zuordnung des LF zur Marktlokation bzw. Tranche, z.B. aufgrund des Use-Cases "Lieferende von LF an NB").

**Vorher läuft:** [Abrechnungsdaten Netznutzungsabrechnung](/prozessdoku/202604/LF/GPKE-Teil2-abrechnungsdaten-netznutzungsabrechnung), [Ermittlung der MaLo-ID der Marktlokation](/prozessdoku/202604/LF/GPKE-Teil2-ermittlung-der-malo-id-der-marktlokation), [Neuanlage](/prozessdoku/202604/LF/GPKE-Teil2-neuanlage) — diese Prozesse nennen den hier gezeigten in ihrem Ergebnis.

</li>

<li data-blatt="erste-nachricht">

### Erste Nachricht

Der Beteiligte dieser Seite sendet selbst: „Anmeldung einer Zuordnung des LFN zur Marktlokation bzw. Tranche“ an **NB** (Schritt 1).

</li>

<li data-blatt="ziel">

### Ziel

Der LFN ist der Marktlokation bzw. Tranche zugeordnet.

</li>

</ol>
</Stepper>

<a id="abschnitt-sichten"></a>

## Andere Sichten des Prozesses

Derselbe Prozess, aus den Augen der anderen Beteiligten: dieselben Schritte, jeweils aus deren Sicht gelesen.

- [Sicht LFA](/prozessdoku/202604/LF--LFA/GPKE-Teil2-lieferbeginn) — der abgebende Lieferant · Marktrolle LF
- [Sicht LFZ](/prozessdoku/202604/LF--LFZ/GPKE-Teil2-lieferbeginn) — Lieferant zukünftig · Marktrolle LF
- [Sicht NB](/prozessdoku/202604/NB/GPKE-Teil2-lieferbeginn) — NB

<Hinweisbereich>

*Die Schritte sind die **möglichen** Nachrichten dieses Prozesses, keine Abfolge — die Quelle führt weder Bedingungen noch Alternativen. Das Kästchen am Schritt nennt links die eigene Sicht: **←** empfängt sie, **→** sendet sie. Zugeklappte Schritte laufen zwischen anderen Marktpartnern. Die Nummern sind die der Quelle; wo eine fehlt, fehlt sie dort.*

</Hinweisbereich>
