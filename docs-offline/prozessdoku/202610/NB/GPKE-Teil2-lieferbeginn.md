# Lieferbeginn — Sicht NB

<Kopf rolle="NB" beteiligter="NB" festlegung="GPKE" dokument="GPKE Teil 2" kapitel="2.1.2" sparte="Strom" schritte={8} suchtitel="Lieferbeginn — Sicht NB · GPKE Teil 2 · Formatversion 202610" stichworte="Lieferantenwechsel" abschnitte={[{"id": "abschnitt-ablauf", "label": "Prozessablauf"}, {"id": "abschnitt-schritte", "label": "Prozessschritte"}, {"id": "abschnitt-informationen", "label": "Prozess-Informationen"}, {"id": "abschnitt-sichten", "label": "Andere Sichten des Prozesses"}]} />

<Kurzfassung>

Ein LFN meldet beim NB eine Zuordnung des LFN zu einer Marktlokation bzw. Tranche an. Im Zuge des Prozesses
- beendet der NB ggf. die Zuordnung des LFA zur Marktlokation bzw. Tranche.
- hebt der NB ggf. die Zuordnung des LFZ zur Marktlokation bzw. Tranche auf.

</Kurzfassung>

<a id="abschnitt-ablauf"></a>

## Prozessablauf aus Sicht des NB

<Systembild svg={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1004 2600\" width=\"1004\" height=\"2600\" role=\"img\" aria-labelledby=\"sb-title\" class=\"maco-systembild\">\n<title id=\"sb-title\">Systembild: Lieferbeginn aus Sicht NB</title>\n<defs><marker id=\"sb-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect class=\"sb-lane-kopf\" x=\"16\" y=\"12\" width=\"232\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend-System des Kunden</text>\n<rect class=\"sb-lane-kopf\" x=\"398\" y=\"12\" width=\"264\" height=\"46\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · NB</text>\n<rect class=\"sb-lane-kopf\" x=\"812\" y=\"12\" width=\"176\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"900\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Marktpartner</text>\n<line x1=\"323\" y1=\"58\" x2=\"323\" y2=\"2588\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"737\" y1=\"58\" x2=\"737\" y2=\"2588\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"80\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">1. Anmeldung einer</text>\n<text x=\"530\" y=\"115\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Zuordnung des LFN zur</text>\n<text x=\"530\" y=\"130\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Marktlokation bzw. Tr…</text>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"93\" r=\"5\"/><line x1=\"900\" y1=\"98\" x2=\"900\" y2=\"110\"/><line x1=\"893\" y1=\"102\" x2=\"907\" y2=\"102\"/><line x1=\"900\" y1=\"110\" x2=\"894\" y2=\"120\"/><line x1=\"900\" y1=\"110\" x2=\"906\" y2=\"120\"/></g>\n<text x=\"900\" y=\"142\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">LFN</text>\n<line x1=\"878\" y1=\"111\" x2=\"628\" y2=\"111\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"103\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"127\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">55001, 55077</text>\n<rect class=\"sb-kasten sb-aperak_lesen\" x=\"432\" y=\"169\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"189\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Daten für die</text>\n<text x=\"530\" y=\"204\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Eingangsprüfung laden</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"143\" x2=\"530\" y2=\"169\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-aperak_lesen\" x=\"34\" y=\"177\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"197\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Marktlokation lesen</text>\n<line x1=\"432\" y1=\"193\" x2=\"230\" y2=\"193\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"185\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"243\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"263\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z10, Z16,</text>\n<text x=\"530\" y=\"278\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Z18, Z43</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"217\" x2=\"530\" y2=\"243\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-schreiben\" x=\"432\" y=\"317\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"337\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"291\" x2=\"530\" y2=\"317\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-schreiben\" x=\"34\" y=\"317\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"337\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten erstellen</text>\n<line x1=\"432\" y1=\"333\" x2=\"230\" y2=\"333\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"325\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-lesen\" x=\"432\" y=\"381\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"401\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Daten für die Prüfung laden</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"350\" x2=\"530\" y2=\"381\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-lesen\" x=\"34\" y=\"373\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"393\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">7 Lese-Schnittstellen</text>\n<text x=\"132\" y=\"408\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">aufgerufen</text>\n<line x1=\"432\" y1=\"397\" x2=\"230\" y2=\"397\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"389\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<text x=\"331\" y=\"413\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">je einzeln am Schritt</text>\n<rect class=\"sb-kasten sb-ebd\" x=\"432\" y=\"455\" width=\"196\" height=\"153\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"475\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">EBD prüfen: E_0622, E_0621,</text>\n<text x=\"530\" y=\"490\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">E_0623</text>\n<text x=\"530\" y=\"505\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label-2, #424245)\">E_0622 — Prüfen, ob</text>\n<text x=\"530\" y=\"520\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label-2, #424245)\">Anmeldung direkt ablehnbar</text>\n<text x=\"530\" y=\"535\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label-2, #424245)\">E_0621 — Prüfen, ob</text>\n<text x=\"530\" y=\"550\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label-2, #424245)\">Anfrage zur Beendigung der</text>\n<text x=\"530\" y=\"565\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label-2, #424245)\">Zuordnung erforderlich</text>\n<text x=\"530\" y=\"580\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label-2, #424245)\">E_0623 — Lieferbeginn</text>\n<text x=\"530\" y=\"595\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label-2, #424245)\">prüfen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"414\" x2=\"530\" y2=\"455\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-folgeprozess\" x=\"432\" y=\"634\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"654\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Folgeprozess auslösen:</text>\n<text x=\"530\" y=\"669\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">17134, 55002, 55003,</text>\n<text x=\"530\" y=\"684\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">55037, 55078, 5…</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"608\" x2=\"530\" y2=\"634\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-lesen_verarbeitung\" x=\"432\" y=\"723\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"743\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Daten für die Verarbeitung</text>\n<text x=\"530\" y=\"758\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">laden</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"697\" x2=\"530\" y2=\"723\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-lesen_verarbeitung\" x=\"34\" y=\"723\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"743\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">2 Lese-Schnittstellen</text>\n<text x=\"132\" y=\"758\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">aufgerufen</text>\n<line x1=\"432\" y1=\"747\" x2=\"230\" y2=\"747\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"739\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<text x=\"331\" y=\"763\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">je einzeln am Schritt</text>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"797\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"817\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">2. Information über</text>\n<text x=\"530\" y=\"832\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">existierende Zuordnung</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"771\" x2=\"530\" y2=\"797\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"803\" r=\"5\"/><line x1=\"900\" y1=\"808\" x2=\"900\" y2=\"820\"/><line x1=\"893\" y1=\"812\" x2=\"907\" y2=\"812\"/><line x1=\"900\" y1=\"820\" x2=\"894\" y2=\"830\"/><line x1=\"900\" y1=\"820\" x2=\"906\" y2=\"830\"/></g>\n<text x=\"900\" y=\"852\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">LFN</text>\n<line x1=\"628\" y1=\"821\" x2=\"878\" y2=\"821\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"813\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"837\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">55036</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"880\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"900\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"845\" x2=\"530\" y2=\"880\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"880\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"900\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"896\" x2=\"230\" y2=\"896\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"888\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-lesen_verarbeitung\" x=\"432\" y=\"944\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"964\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Daten für die Verarbeitung</text>\n<text x=\"530\" y=\"979\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">laden</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"913\" x2=\"530\" y2=\"944\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-lesen_verarbeitung\" x=\"34\" y=\"952\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"972\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Marktlokation lesen</text>\n<line x1=\"432\" y1=\"968\" x2=\"230\" y2=\"968\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"960\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"1018\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1038\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">3. Anfrage zur Beendigung</text>\n<text x=\"530\" y=\"1053\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">der Zuordnung des LFA zur</text>\n<text x=\"530\" y=\"1068\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Marktlokat…</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"992\" x2=\"530\" y2=\"1018\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"1031\" r=\"5\"/><line x1=\"900\" y1=\"1036\" x2=\"900\" y2=\"1048\"/><line x1=\"893\" y1=\"1040\" x2=\"907\" y2=\"1040\"/><line x1=\"900\" y1=\"1048\" x2=\"894\" y2=\"1058\"/><line x1=\"900\" y1=\"1048\" x2=\"906\" y2=\"1058\"/></g>\n<text x=\"900\" y=\"1080\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">LFA</text>\n<line x1=\"628\" y1=\"1049\" x2=\"878\" y2=\"1049\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"1041\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"1065\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">55010</text>\n<rect class=\"sb-kasten sb-schreiben\" x=\"432\" y=\"1107\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1127\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1081\" x2=\"530\" y2=\"1107\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-schreiben\" x=\"34\" y=\"1107\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"1127\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten erstellen</text>\n<line x1=\"432\" y1=\"1123\" x2=\"230\" y2=\"1123\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"1115\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"1171\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1191\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">4. Antwort auf Anfrage zur</text>\n<text x=\"530\" y=\"1206\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Beendigung der Zuordnung</text>\n<text x=\"530\" y=\"1221\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">des LFA zu…</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1140\" x2=\"530\" y2=\"1171\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"1184\" r=\"5\"/><line x1=\"900\" y1=\"1189\" x2=\"900\" y2=\"1201\"/><line x1=\"893\" y1=\"1193\" x2=\"907\" y2=\"1193\"/><line x1=\"900\" y1=\"1201\" x2=\"894\" y2=\"1211\"/><line x1=\"900\" y1=\"1201\" x2=\"906\" y2=\"1211\"/></g>\n<text x=\"900\" y=\"1233\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">LFA</text>\n<line x1=\"878\" y1=\"1202\" x2=\"628\" y2=\"1202\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"1194\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"1218\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">55011, 55012</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"1260\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1280\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z33</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1234\" x2=\"530\" y2=\"1260\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"1324\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1344\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1293\" x2=\"530\" y2=\"1324\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"1324\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"1344\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"1340\" x2=\"230\" y2=\"1340\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"1332\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-folgeprozess\" x=\"432\" y=\"1388\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1408\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Folgeprozess auslösen:</text>\n<text x=\"530\" y=\"1423\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">55037</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1357\" x2=\"530\" y2=\"1388\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-folge_ausloeser\" x=\"432\" y=\"1462\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1482\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Ausgelöst durch Eingang:</text>\n<text x=\"530\" y=\"1497\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">55001, 55077</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1436\" x2=\"530\" y2=\"1462\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-lesen_verarbeitung\" x=\"432\" y=\"1536\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1556\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Daten für die Verarbeitung</text>\n<text x=\"530\" y=\"1571\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">laden</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1510\" x2=\"530\" y2=\"1536\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-lesen_verarbeitung\" x=\"34\" y=\"1536\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"1556\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">9 Lese-Schnittstellen</text>\n<text x=\"132\" y=\"1571\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">aufgerufen</text>\n<line x1=\"432\" y1=\"1560\" x2=\"230\" y2=\"1560\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"1552\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<text x=\"331\" y=\"1576\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">je einzeln am Schritt</text>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"1610\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1630\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">5. Zuordnung des LFN zur</text>\n<text x=\"530\" y=\"1645\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Marktlokation bzw. Tranche</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1584\" x2=\"530\" y2=\"1610\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"1616\" r=\"5\"/><line x1=\"900\" y1=\"1621\" x2=\"900\" y2=\"1633\"/><line x1=\"893\" y1=\"1625\" x2=\"907\" y2=\"1625\"/><line x1=\"900\" y1=\"1633\" x2=\"894\" y2=\"1643\"/><line x1=\"900\" y1=\"1633\" x2=\"906\" y2=\"1643\"/></g>\n<text x=\"900\" y=\"1665\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">LFN</text>\n<line x1=\"628\" y1=\"1634\" x2=\"878\" y2=\"1634\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"1626\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"1650\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">55002, 55078</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"1693\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1713\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1658\" x2=\"530\" y2=\"1693\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"1693\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"1713\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"1709\" x2=\"230\" y2=\"1709\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"1701\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-folge_ausloeser\" x=\"432\" y=\"1757\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1777\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Ausgelöst durch Eingang:</text>\n<text x=\"530\" y=\"1792\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">55001, 55077</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1726\" x2=\"530\" y2=\"1757\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"1831\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1851\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">6. Ablehnung der Anmeldung</text>\n<text x=\"530\" y=\"1866\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">einer Zuordnung des LFN zur</text>\n<text x=\"530\" y=\"1881\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Marktlo…</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1805\" x2=\"530\" y2=\"1831\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"1844\" r=\"5\"/><line x1=\"900\" y1=\"1849\" x2=\"900\" y2=\"1861\"/><line x1=\"893\" y1=\"1853\" x2=\"907\" y2=\"1853\"/><line x1=\"900\" y1=\"1861\" x2=\"894\" y2=\"1871\"/><line x1=\"900\" y1=\"1861\" x2=\"906\" y2=\"1871\"/></g>\n<text x=\"900\" y=\"1893\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">LFN</text>\n<line x1=\"628\" y1=\"1862\" x2=\"878\" y2=\"1862\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"1854\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"1878\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">55003, 55080</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"1920\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1940\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1894\" x2=\"530\" y2=\"1920\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"1920\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"1940\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"1936\" x2=\"230\" y2=\"1936\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"1928\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-folge_ausloeser\" x=\"432\" y=\"1984\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"2004\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Ausgelöst durch Eingang:</text>\n<text x=\"530\" y=\"2019\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">55001, 55011</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1953\" x2=\"530\" y2=\"1984\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-trigger\" x=\"432\" y=\"2058\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"2078\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessauslöser empfangen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"2032\" x2=\"530\" y2=\"2058\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-trigger\" x=\"34\" y=\"2058\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"2078\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">START_ENDE_ZUORDNUNG</text>\n<line x1=\"230\" y1=\"2074\" x2=\"432\" y2=\"2074\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"2066\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"2122\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"2142\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">10. Beendigung der</text>\n<text x=\"530\" y=\"2157\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Zuordnung des LFA zur</text>\n<text x=\"530\" y=\"2172\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Marktlokation bzw. Tra…</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"2091\" x2=\"530\" y2=\"2122\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"2135\" r=\"5\"/><line x1=\"900\" y1=\"2140\" x2=\"900\" y2=\"2152\"/><line x1=\"893\" y1=\"2144\" x2=\"907\" y2=\"2144\"/><line x1=\"900\" y1=\"2152\" x2=\"894\" y2=\"2162\"/><line x1=\"900\" y1=\"2152\" x2=\"906\" y2=\"2162\"/></g>\n<text x=\"900\" y=\"2184\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">LFA</text>\n<line x1=\"628\" y1=\"2153\" x2=\"878\" y2=\"2153\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"2145\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"2169\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">55037</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"2211\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"2231\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"2185\" x2=\"530\" y2=\"2211\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"2211\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"2231\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"2227\" x2=\"230\" y2=\"2227\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"2219\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-trigger\" x=\"432\" y=\"2275\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"2295\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessauslöser empfangen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"2244\" x2=\"530\" y2=\"2275\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-trigger\" x=\"34\" y=\"2267\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"2287\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">START_AUFH_ZUK_ZUORDN</text>\n<text x=\"132\" y=\"2302\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">UNG</text>\n<line x1=\"230\" y1=\"2291\" x2=\"432\" y2=\"2291\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"2283\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-lesen_verarbeitung\" x=\"432\" y=\"2349\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"2369\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Daten für die Verarbeitung</text>\n<text x=\"530\" y=\"2384\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">laden</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"2308\" x2=\"530\" y2=\"2349\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-lesen_verarbeitung\" x=\"34\" y=\"2349\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"2369\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">3 Lese-Schnittstellen</text>\n<text x=\"132\" y=\"2384\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">aufgerufen</text>\n<line x1=\"432\" y1=\"2373\" x2=\"230\" y2=\"2373\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"2365\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<text x=\"331\" y=\"2389\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">je einzeln am Schritt</text>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"2423\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"2443\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">13. Aufhebung der</text>\n<text x=\"530\" y=\"2458\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Zuordnung des LFZ zur</text>\n<text x=\"530\" y=\"2473\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Marklokation bzw. Tranc…</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"2397\" x2=\"530\" y2=\"2423\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"2436\" r=\"5\"/><line x1=\"900\" y1=\"2441\" x2=\"900\" y2=\"2453\"/><line x1=\"893\" y1=\"2445\" x2=\"907\" y2=\"2445\"/><line x1=\"900\" y1=\"2453\" x2=\"894\" y2=\"2463\"/><line x1=\"900\" y1=\"2453\" x2=\"906\" y2=\"2463\"/></g>\n<text x=\"900\" y=\"2485\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">LFZ</text>\n<line x1=\"628\" y1=\"2454\" x2=\"878\" y2=\"2454\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"2446\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"2470\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">55038</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"2512\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"2532\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"2486\" x2=\"530\" y2=\"2512\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"2512\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"2532\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"2528\" x2=\"230\" y2=\"2528\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"2520\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n</svg>"} gesamt={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1218 1243\" width=\"1218\" height=\"1243\" role=\"img\" aria-labelledby=\"sd-title\" class=\"maco-sequence\">\n<title id=\"sd-title\">Sequenzdiagramm: Lieferbeginn aus Sicht NB</title>\n<defs><marker id=\"sd-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect x=\"16\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"121\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend (Kunde)</text>\n<line x1=\"121\" y1=\"64\" x2=\"121\" y2=\"1231\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"260\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"365\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · NB</text>\n<line x1=\"365\" y1=\"64\" x2=\"365\" y2=\"1231\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"504\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"609\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">LFN</text>\n<line x1=\"609\" y1=\"64\" x2=\"609\" y2=\"1231\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"748\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"853\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">LFA</text>\n<line x1=\"853\" y1=\"64\" x2=\"853\" y2=\"1231\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"992\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"1097\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">LFZ</text>\n<line x1=\"1097\" y1=\"64\" x2=\"1097\" y2=\"1231\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"609\" y1=\"90\" x2=\"365\" y2=\"90\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"81\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">1. Anmeldung einer Zuordnung des LFN zur Marktlo…</text>\n<text x=\"487\" y=\"105\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55001, 55077</text>\n<line x1=\"365\" y1=\"152\" x2=\"121\" y2=\"152\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"143\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<text x=\"243\" y=\"167\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten erstellen</text>\n<line x1=\"365\" y1=\"214\" x2=\"609\" y2=\"214\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"205\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">2. Information über existierende Zuordnung</text>\n<text x=\"487\" y=\"229\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55036</text>\n<line x1=\"365\" y1=\"276\" x2=\"121\" y2=\"276\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"267\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"291\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"365\" y1=\"338\" x2=\"853\" y2=\"338\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"609\" y=\"329\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">3. Anfrage zur Beendigung der Zuordnung des LFA…</text>\n<text x=\"609\" y=\"353\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55010</text>\n<line x1=\"365\" y1=\"400\" x2=\"121\" y2=\"400\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"391\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<text x=\"243\" y=\"415\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten erstellen</text>\n<line x1=\"853\" y1=\"462\" x2=\"365\" y2=\"462\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"609\" y=\"453\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">4. Antwort auf Anfrage zur Beendigung der Zuordn…</text>\n<text x=\"609\" y=\"477\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55011, 55012 · E_0624</text>\n<text x=\"609\" y=\"490\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0624 — Anfrage zur Beendigung der Zuordnung prüfen</text>\n<line x1=\"365\" y1=\"524\" x2=\"121\" y2=\"524\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"515\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"539\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"365\" y1=\"586\" x2=\"609\" y2=\"586\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"577\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">5. Zuordnung des LFN zur Marktlokation bzw. Tran…</text>\n<text x=\"487\" y=\"601\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55002, 55078 · E_0623</text>\n<text x=\"487\" y=\"614\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0623 — Lieferbeginn prüfen</text>\n<line x1=\"365\" y1=\"648\" x2=\"121\" y2=\"648\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"639\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"663\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"365\" y1=\"710\" x2=\"609\" y2=\"710\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"701\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">6. Ablehnung der Anmeldung einer Zuordnung des L…</text>\n<text x=\"487\" y=\"725\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55003, 55080 · E_0622, E_0623</text>\n<text x=\"487\" y=\"738\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0622 — Prüfen, ob Anmeldung direkt ablehnbar</text>\n<text x=\"487\" y=\"751\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0623 — Lieferbeginn prüfen</text>\n<line x1=\"365\" y1=\"785\" x2=\"121\" y2=\"785\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"776\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"800\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"121\" y1=\"847\" x2=\"365\" y2=\"847\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"838\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">START_ENDE_ZUORDNUNG</text>\n<text x=\"243\" y=\"862\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Trigger-Event</text>\n<line x1=\"365\" y1=\"909\" x2=\"853\" y2=\"909\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"609\" y=\"900\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">10. Beendigung der Zuordnung des LFA zur Marktlok…</text>\n<text x=\"609\" y=\"924\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55037</text>\n<line x1=\"365\" y1=\"971\" x2=\"121\" y2=\"971\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"962\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"986\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"121\" y1=\"1033\" x2=\"365\" y2=\"1033\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"1024\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">START_AUFH_ZUK_ZUORDNUNG</text>\n<text x=\"243\" y=\"1048\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Trigger-Event</text>\n<line x1=\"365\" y1=\"1095\" x2=\"1097\" y2=\"1095\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"731\" y=\"1086\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">13. Aufhebung der Zuordnung des LFZ zur Marklokat…</text>\n<text x=\"731\" y=\"1110\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55038</text>\n<line x1=\"365\" y1=\"1157\" x2=\"121\" y2=\"1157\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"1148\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"1172\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n</svg>"} titel="NB" />

<a id="abschnitt-schritte"></a>

## Prozessschritte

<Schritt nr="1" anker="schritt-1" richtung="eingehend" kopf={{"links": {"label": "NB", "eigen": true}, "rechts": {"label": "LFN"}}}>

### Anmeldung einer Zuordnung des LFN zur Marktlokation bzw. Tranche

<Schrittskizze sicht={{"label": "NB"}} zeilen={[{"art": "empfangen", "label": "LFN", "weg": "AS4", "nachrichten": [{"nr": "55001", "titel": "Anmeldung verb. MaLo"}, {"nr": "55077", "titel": "Anmeldung erz. MaLo"}]}, {"art": "lesen_aperak", "schnittstellen": [{"label": "Marktlokation lesen"}]}, {"art": "aperak", "werte": ["Z10", "Z16", "Z18", "Z43"]}, {"art": "erstellen"}, {"art": "lesen_ebd", "schnittstellen": [{"label": "Energieliefervertrag lesen"}, {"label": "Lokationsbündel lesen"}, {"label": "Marktlokation lesen"}, {"label": "Netznutzungsvertrag lesen"}, {"label": "Steuerbare Ressource lesen"}, {"label": "Bilanzierung lesen"}, {"label": "Tranche lesen"}]}, {"art": "ebd", "baeume": [{"code": "E_0622", "titel": "Prüfen, ob Anmeldung direkt ablehnbar"}, {"code": "E_0621", "titel": "Prüfen, ob Anfrage zur Beendigung der Zuordnung erforderlich"}, {"code": "E_0623", "titel": "Lieferbeginn prüfen"}]}, {"art": "folgeprozess", "werte": ["17134", "55002", "55003", "55037", "55078", "55080"]}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55001](/schnittstellen/202610/pruefi/UTILMD/PI_55001) — Anmeldung verb. MaLo · AS4
- [55077](/schnittstellen/202610/pruefi/UTILMD/PI_55077) — Anmeldung erz. MaLo · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **LFN** · AS4

</li>

<li data-teil="lesen" data-stufe="aperak">

**Daten für die Eingangsprüfung laden**
- [Marktlokation lesen](/api/202610/backend-lesen/getmarketlocationbasic#marktlokation-lesen) `GET /getMarketLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getMarketLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": false, "defaultValue": "MALO", "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": false, "defaultValue": "2024-06-28T12:18:00Z", "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_MARKTLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

</li>

<li data-teil="aperak">

**Aperak-Prüfungen**
- `55001`, `55077` → `Z10`
- `55001`, `55077` → `Z16`
- `55001`, `55077` → `Z18`
- `55001`, `55077` → `Z43` — Aperak Prüfung: Stimmt Objekteigenschaft überein?

</li>

<li data-teil="schnittstelle" data-art="schreiben">

**Schreibende Schnittstelle**
- Vorgang angelegt — [Prozessdaten erstellen](/api/202610/backend-schreiben-nb/createprocessdata#prozessdaten-erstellen) `POST /createProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/createProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "ERSTELLEN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"ENERGIELIEFERVERTRAG\": [\n      {\n        \"boTyp\": \"VERTRAG\",\n        \"enFG\": [\n          {\n            \"grund\": [\n              \"ENFG_STROMSPEICHER_UND_VERLUSTENERGIE\"\n            ],\n            \"grundlageVerringerungUmlagen\": \"ERFUELLT_VORAUSSETZUNG_NACH_ENFG\"\n          }\n        ],\n        \"korrespondenzpartner\": {\n          \"ansprechpartner\": {\n            \"boTyp\": \"ANSPRECHPARTNER\",\n            \"rufnummern\": [\n              {\n                \"nummerntyp\": \"RUF_DURCHWAHL\",\n                \"rufnummer\": \"3222271020\"\n              }\n            ],\n            \"versionStruktur\": \"1\"\n          },\n          \"boTyp\": \"GESCHAEFTSPARTNER\",\n          \"gewerbekennzeichnung\": false,\n          \"name1\": \"Max\",\n          \"partneradresse\": {\n            \"hausnummer\": \"46\",\n            \"landescode\": \"DE\",\n            \"ort\": \"Weimar\",\n            \"postfach\": \"Str\",\n            \"postleitzahl\": \"99423\",\n            \"strasse\": \"Erfurter\"\n          },\n          \"versionStruktur\": \"1\"\n        },\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\",\n        \"vertragsart\": \"ENERGIELIEFERVERTRAG\",\n        \"vertragspartner2\": [\n          {\n            \"boTyp\": \"GESCHAEFTSPARTNER\",\n            \"geschaeftspartnerrolle\": [\n              \"KUNDE\"\n            ],\n            \"gewerbekennzeichnung\": false,\n            \"name1\": \"Max\",\n            \"name2\": \"Mustermann\",\n            \"versionStruktur\": \"1\"\n          }\n        ]\n      }\n    ],\n    \"MARKTLOKATION\": [\n      {\n        \"boTyp\": \"MARKTLOKATION\",\n        \"erforderlichesProduktpaket\": [\n          {\n            \"produkt\": [\n              {\n                \"codeProdukteigenschaft\": \"9991000002131\",\n                \"produktCode\": \"9991000002016\"\n              },\n              {\n                \"produktCode\": \"9991000002082\",\n                \"wertedetails\": \"11XEONBAYERN---I\"\n              },\n              {\n                \"codeProdukteigenschaft\": \"9991000002115\",\n                \"produktCode\": \"9991000002008\"\n              },\n              {\n                \"codeProdukteigenschaft\": \"9991000002785\",\n                \"produktCode\": \"9991000002727\"\n              }\n            ],\n            \"produktpaketId\": 1,\n            \"umsetzungsgradvorgabe\": \"ZUORDNUNG_NUR_WENN_PRODUKTPAKET_UMSETZBAR\"\n          }\n        ],\n        \"marktlokationsId\": \"50363198100\",\n        \"marktlokationsTyp\": [\n          {\n            \"typ\": \"STANDARD_MARKTLOKATION\"\n          }\n        ],\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"NETZNUTZUNGSVERTRAG\": [\n      {\n        \"boTyp\": \"VERTRAG\",\n        \"lokationsId\": \"50363198100\",\n        \"lokationsTyp\": \"MALO\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\",\n        \"vertragsart\": \"NETZNUTZUNGSVERTRAG\",\n        \"vertragsbeginn\": \"2026-12-01T23:00:00Z\",\n        \"vertragsende\": \"2026-12-02T23:00:00Z\",\n        \"vertragskonditionen\": {\n          \"haushaltskunde\": true\n        }\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9980000000001\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"datenaustauschreferenz\": \"M2N2K9NH\",\n    \"dokumentennummer\": \"BGMM2RS5P0Q\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9980000000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"E01\",\n    \"nachrichtendatum\": \"2026-10-02T11:00:00Z\",\n    \"nachrichtenreferenznummer\": \"UNHM2M4CSVV\",\n    \"pruefidentifikator\": \"55001\",\n    \"sparte\": \"STROM\",\n    \"transaktionsgrund\": \"E01\",\n    \"transaktionsgrundergaenzung\": \"ZW4\",\n    \"transaktionsgrundergaenzungBefristeteAnmeldung\": \"E01\",\n    \"vertragsbeginn\": \"2026-12-01T23:00:00Z\",\n    \"vertragsende\": \"2026-12-02T23:00:00Z\",\n    \"vorgangsnummer\": \"KBG27094210000000000929931413171000\"\n  },\n  \"zusatzdaten\": {}\n}"} examples={[{"mediaType": "application/json", "examples": [{"name": "55001", "summary": "55001 — Anmeldung verb. MaLo", "value": {"stammdaten": {"MARKTLOKATION": [{"boTyp": "MARKTLOKATION", "versionStruktur": "1", "marktlokationsId": "50363198100", "marktlokationsTyp": [{"typ": "STANDARD_MARKTLOKATION"}], "sparte": "STROM", "erforderlichesProduktpaket": [{"produktpaketId": 1, "produkt": [{"produktCode": "9991000002016", "codeProdukteigenschaft": "9991000002131"}, {"produktCode": "9991000002082", "wertedetails": "11XEONBAYERN---I"}, {"produktCode": "9991000002008", "codeProdukteigenschaft": "9991000002115"}, {"produktCode": "9991000002727", "codeProdukteigenschaft": "9991000002785"}], "umsetzungsgradvorgabe": "ZUORDNUNG_NUR_WENN_PRODUKTPAKET_UMSETZBAR"}]}], "NETZNUTZUNGSVERTRAG": [{"boTyp": "VERTRAG", "versionStruktur": "1", "vertragsart": "NETZNUTZUNGSVERTRAG", "sparte": "STROM", "vertragsbeginn": "2026-12-01T23:00:00Z", "vertragsende": "2026-12-02T23:00:00Z", "vertragskonditionen": {"haushaltskunde": true}, "lokationsId": "50363198100", "lokationsTyp": "MALO"}], "ENERGIELIEFERVERTRAG": [{"boTyp": "VERTRAG", "versionStruktur": "1", "vertragsart": "ENERGIELIEFERVERTRAG", "sparte": "STROM", "vertragspartner2": [{"boTyp": "GESCHAEFTSPARTNER", "versionStruktur": "1", "name1": "Max", "name2": "Mustermann", "gewerbekennzeichnung": false, "geschaeftspartnerrolle": ["KUNDE"]}], "korrespondenzpartner": {"boTyp": "GESCHAEFTSPARTNER", "versionStruktur": "1", "name1": "Max", "gewerbekennzeichnung": false, "partneradresse": {"postleitzahl": "99423", "ort": "Weimar", "strasse": "Erfurter", "hausnummer": "46", "postfach": "Str", "landescode": "DE"}, "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "rufnummern": [{"nummerntyp": "RUF_DURCHWAHL", "rufnummer": "3222271020"}]}}, "enFG": [{"grundlageVerringerungUmlagen": "ERFUELLT_VORAUSSETZUNG_NACH_ENFG", "grund": ["ENFG_STROMSPEICHER_UND_VERLUSTENERGIE"]}]}]}, "transaktionsdaten": {"datenaustauschreferenz": "M2N2K9NH", "sparte": "STROM", "transaktionsgrund": "E01", "transaktionsgrundergaenzung": "ZW4", "transaktionsgrundergaenzungBefristeteAnmeldung": "E01", "vorgangsnummer": "KBG27094210000000000929931413171000", "pruefidentifikator": "55001", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9980000000001", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9980000000002", "rollencodetyp": "BDEW"}, "dokumentennummer": "BGMM2RS5P0Q", "kategorie": "E01", "nachrichtendatum": "2026-10-02T11:00:00Z", "nachrichtenreferenznummer": "UNHM2M4CSVV", "vertragsbeginn": "2026-12-01T23:00:00Z", "vertragsende": "2026-12-02T23:00:00Z"}, "zusatzdaten": {}}}, {"name": "55077", "summary": "55077 — Anmeldung erz. MaLo", "value": {"stammdaten": {"MARKTLOKATION": [{"boTyp": "MARKTLOKATION", "versionStruktur": "1", "marktlokationsId": "20072281644", "sparte": "STROM", "foerderungsLand": "DE", "erforderlichesProduktpaket": [{"produktpaketId": 1, "produkt": [{"produktCode": "9991000002082", "wertedetails": "11XBKA---------I"}, {"produktCode": "9991000002090", "codeProdukteigenschaft": "9991000003014", "wertedetails": "50"}, {"produktCode": "9991000002066", "codeProdukteigenschaft": "9991000002272"}], "umsetzungsgradvorgabe": "ZUORDNUNG_NUR_WENN_PRODUKTPAKET_UMSETZBAR", "priorisierung": "PRIORITAET1"}, {"produktpaketId": 2, "produkt": [{"produktCode": "9991000002404", "codeProdukteigenschaft": "9991000002420"}, {"produktCode": "9991000002082", "wertedetails": "22XBKA---------I"}, {"produktCode": "9991000002090", "codeProdukteigenschaft": "9991000003014", "wertedetails": "50"}, {"produktCode": "9991000002066", "codeProdukteigenschaft": "9991000002272"}, {"produktCode": "9991000002404", "codeProdukteigenschaft": "9991000002420"}], "umsetzungsgradvorgabe": "ZUORDNUNG_NUR_WENN_PRODUKTPAKET_UMSETZBAR", "priorisierung": "PRIORITAET2"}]}], "NETZNUTZUNGSVERTRAG": [{"boTyp": "VERTRAG", "versionStruktur": "1", "vertragsart": "NETZNUTZUNGSVERTRAG", "sparte": "STROM", "vertragsbeginn": "2025-11-01T23:00:00Z", "lokationsId": "20072281644", "lokationsTyp": "MALO"}]}, "transaktionsdaten": {"datenaustauschreferenz": "DAZBHQXEUJALSE", "sparte": "STROM", "transaktionsgrund": "E03", "transaktionsgrundergaenzung": "ZW2", "vorgangsnummer": "24062416225400000000000102159662022", "pruefidentifikator": "55077", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9903729000007", "rollencodetyp": "BDEW", "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "nachname": "P GETTY", "rufnummern": [{"nummerntyp": "RUF_DURCHWAHL", "rufnummer": "+3222271020"}]}}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900327000009", "rollencodetyp": "BDEW"}, "dokumentennummer": "DA672410170839449903323000007966941", "kategorie": "E01", "nachrichtendatum": "2025-06-24T12:31:00Z", "nachrichtenreferenznummer": "DAOHDSWRBRFDIO", "abtretungserklaerung": {"passwort": "KNSG5674?\"§", "link1": "https://www.Stadtwerk_xy.de/...", "link2": "X", "link3": "X", "link4": "X", "link5": "X"}}, "zusatzdaten": {}}}]}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Legt im Backend einen neuen Vorgang mit den Daten der eingegangenen Nachricht an.

</li>

<li data-teil="lesen" data-stufe="ebd">

**Daten für die Prüfung laden**
- [Energieliefervertrag lesen](/api/202610/backend-lesen/getenergysupplycontractbasic#energieliefervertrag-lesen) `GET /getEnergySupplyContractBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getEnergySupplyContractBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_ENERGIELIEFERVERTRAG_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Lokationsbündel lesen](/api/202610/backend-lesen/getlocationbundlebasic#lokationsbundel-lesen) `GET /getLocationBundleBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getLocationBundleBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_LOKATIONSBUENDEL_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Marktlokation lesen](/api/202610/backend-lesen/getmarketlocationbasic#marktlokation-lesen) `GET /getMarketLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getMarketLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": false, "defaultValue": "MALO", "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": false, "defaultValue": "2024-06-28T12:18:00Z", "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_MARKTLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Netznutzungsvertrag lesen](/api/202610/backend-lesen/getgridusagecontractbasic#netznutzungsvertrag-lesen) `GET /getGridUsageContractBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getGridUsageContractBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": false, "defaultValue": "MALO", "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": false, "defaultValue": "2024-06-28T12:18:00Z", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Steuerbare Ressource lesen](/api/202610/backend-lesen/getcontrollableresourcebasic#steuerbare-ressource-lesen) `GET /getControllableResourceBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getControllableResourceBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Bilanzierung lesen](/api/202610/backend-lesen/getaccountingbasic#bilanzierung-lesen) `GET /getAccountingBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getAccountingBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_BILANZIERUNG_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Tranche lesen](/api/202610/backend-lesen/gettranchebasic#tranche-lesen) `GET /getTrancheBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getTrancheBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

</li>

<li data-teil="baum">

**Entscheidungsbaum**
- `55001`, `55077` → [E_0622](/referenz/202610/ebd/E_0622) — Prüfen, ob Anmeldung direkt ablehnbar
- `55001`, `55077` → [E_0621](/referenz/202610/ebd/E_0621) — Prüfen, ob Anfrage zur Beendigung der Zuordnung erforderlich
- `55001`, `55077` → [E_0623](/referenz/202610/ebd/E_0623) — Lieferbeginn prüfen

</li>

<li data-teil="folgeprozess">

**Folgeprozess auslösen**
- [17134](/schnittstellen/202610/pruefi/ORDERS/PI_17134)
- [55002](/schnittstellen/202610/pruefi/UTILMD/PI_55002) — Bestätigung Anmeldung verb. MaLo
- [55003](/schnittstellen/202610/pruefi/UTILMD/PI_55003) — Ablehnung Anmeldung verb. MaLo
- [55037](/schnittstellen/202610/pruefi/UTILMD/PI_55037) — Beendigung der Zuordnung
- [55078](/schnittstellen/202610/pruefi/UTILMD/PI_55078) — Bestätigung Anmeldung erz. MaLo
- [55080](/schnittstellen/202610/pruefi/UTILMD/PI_55080) — Ablehnung Anmeldung erz. MaLo

Nach der Verarbeitung startet die MACO APP den Folgeprozess selbst; welcher davon läuft, hängt vom Ergebnis der Verarbeitung ab.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="2" anker="schritt-2" richtung="ausgehend" kopf={{"links": {"label": "NB", "eigen": true}, "rechts": {"label": "LFN"}}}>

### Information über existierende Zuordnung

<Schrittskizze sicht={{"label": "NB"}} zeilen={[{"art": "lesen_verarbeitung", "schnittstellen": [{"label": "Bilanzierung lesen"}, {"label": "Marktlokation lesen"}]}, {"art": "senden", "label": "LFN", "weg": "AS4", "nachrichten": [{"nr": "55036", "titel": "Existierende Zuordnung"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55036](/schnittstellen/202610/pruefi/UTILMD/PI_55036) — Existierende Zuordnung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="lesen" data-stufe="verarbeitung">

**Daten für die Verarbeitung laden**
- [Bilanzierung lesen](/api/202610/backend-lesen/getaccountingbasic#bilanzierung-lesen) `GET /getAccountingBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getAccountingBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_BILANZIERUNG_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Marktlokation lesen](/api/202610/backend-lesen/getmarketlocationbasic#marktlokation-lesen) `GET /getMarketLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getMarketLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": false, "defaultValue": "MALO", "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": false, "defaultValue": "2024-06-28T12:18:00Z", "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_MARKTLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

</li>

<li data-teil="nachricht">

Nachricht an **LFN** · AS4

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202610/backend-schreiben-nb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"MARKTLOKATION\": [\n      {\n        \"beteiligterMarktpartner\": {\n          \"boTyp\": \"MARKTTEILNEHMER\",\n          \"rollencodenummer\": \"4041409000006\",\n          \"rollencodetyp\": \"BDEW\",\n          \"versionStruktur\": \"1\"\n        },\n        \"boTyp\": \"MARKTLOKATION\",\n        \"marktlokationsId\": \"50226146170\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9900321000005\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"anfragereferenznummer\": \"PCL53523092914504899116940000022575\",\n    \"beteiligterMarktpartner\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"4041409000006\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"datenaustauschreferenz\": \"041391878572\",\n    \"dokumentennummer\": \"041391878573\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9903790000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"E01\",\n    \"nachrichtendatum\": \"2024-04-01T15:35:00Z\",\n    \"nachrichtenreferenznummer\": \"041391878573\",\n    \"pruefidentifikator\": \"55036\",\n    \"sparte\": \"STROM\",\n    \"transaktionsgrund\": \"Z26\",\n    \"vorgangsnummer\": \"XX5056854C0F1EDE98A6A597473530A3\"\n  },\n  \"zusatzdaten\": {}\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend fort, nachdem die Nachricht erstellt ist.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="3" anker="schritt-3" richtung="ausgehend" kopf={{"links": {"label": "NB", "eigen": true}, "rechts": {"label": "LFA"}}}>

### Anfrage zur Beendigung der Zuordnung des LFA zur Marktlokation bzw. Tranche

<Schrittskizze sicht={{"label": "NB"}} zeilen={[{"art": "lesen_verarbeitung", "schnittstellen": [{"label": "Marktlokation lesen"}]}, {"art": "senden", "label": "LFA", "weg": "AS4", "nachrichten": [{"nr": "55010", "titel": "Anfrage zur Beendigung der Zuordnung"}]}, {"art": "erstellen"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55010](/schnittstellen/202610/pruefi/UTILMD/PI_55010) — Anfrage zur Beendigung der Zuordnung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="lesen" data-stufe="verarbeitung">

**Daten für die Verarbeitung laden**
- [Marktlokation lesen](/api/202610/backend-lesen/getmarketlocationbasic#marktlokation-lesen) `GET /getMarketLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getMarketLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": false, "defaultValue": "MALO", "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": false, "defaultValue": "2024-06-28T12:18:00Z", "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_MARKTLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

</li>

<li data-teil="nachricht">

Nachricht an **LFA** · AS4

</li>

<li data-teil="schnittstelle" data-art="schreiben">

**Schreibende Schnittstelle**
- Vorgang angelegt — [Prozessdaten erstellen](/api/202610/backend-schreiben-nb/createprocessdata#prozessdaten-erstellen) `POST /createProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/createProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "ERSTELLEN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"ENERGIELIEFERVERTRAG\": [\n      {\n        \"boTyp\": \"VERTRAG\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\",\n        \"vertragsart\": \"ENERGIELIEFERVERTRAG\",\n        \"vertragspartner2\": [\n          {\n            \"anrede\": \"Dr.\",\n            \"boTyp\": \"GESCHAEFTSPARTNER\",\n            \"geschaeftspartnerrolle\": [\n              \"KUNDE\"\n            ],\n            \"gewerbekennzeichnung\": false,\n            \"name1\": \"Mustermann\",\n            \"name2\": \"Max\",\n            \"name3\": \"von\",\n            \"name4\": \"zu\",\n            \"versionStruktur\": \"1\"\n          }\n        ]\n      }\n    ],\n    \"MARKTLOKATION\": [\n      {\n        \"beteiligterMarktpartner\": {\n          \"boTyp\": \"MARKTTEILNEHMER\",\n          \"rollencodenummer\": \"9903790000002\",\n          \"rollencodetyp\": \"BDEW\",\n          \"versionStruktur\": \"1\"\n        },\n        \"boTyp\": \"MARKTLOKATION\",\n        \"marktlokationsId\": \"50074561188\",\n        \"marktlokationsTyp\": [\n          {\n            \"typ\": \"STANDARD_MARKTLOKATION\"\n          }\n        ],\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"NETZNUTZUNGSVERTRAG\": [\n      {\n        \"boTyp\": \"VERTRAG\",\n        \"lokationsId\": \"50074561188\",\n        \"lokationsTyp\": \"MALO\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\",\n        \"vertragsart\": \"NETZNUTZUNGSVERTRAG\",\n        \"vertragsende\": \"2025-06-30T22:00:00Z\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9900321000005\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"annahmedatum\": \"2025-06-30T00:00:00Z\",\n    \"beteiligterMarktpartner\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9903790000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"datenaustauschreferenz\": \"M3LY4HGT\",\n    \"dokumentennummer\": \"BGMM36GGSLJ\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9903790000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"E02\",\n    \"nachrichtendatum\": \"2025-04-04T12:00:00Z\",\n    \"nachrichtenreferenznummer\": \"UNHM2PVOC8K\",\n    \"pruefidentifikator\": \"55010\",\n    \"sparte\": \"STROM\",\n    \"transaktionsgrund\": \"E01\",\n    \"transaktionsgrundergaenzung\": \"ZW4\",\n    \"vertragsende\": \"2025-06-30T22:00:00Z\",\n    \"vorgangsnummer\": \"123456\"\n  },\n  \"zusatzdaten\": {}\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Legt im Backend einen neuen Vorgang an, nachdem die Nachricht erstellt ist.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="4" anker="schritt-4" richtung="eingehend" kopf={{"links": {"label": "NB", "eigen": true}, "rechts": {"label": "LFA"}}}>

### Antwort auf Anfrage zur Beendigung der Zuordnung des LFA zur Marktlokation bzw. Tranche

<Schrittskizze sicht={{"label": "NB"}} zeilen={[{"art": "empfangen", "label": "LFA", "weg": "AS4", "nachrichten": [{"nr": "55011", "titel": "Bestätigung Beendigung der Zuordnung"}, {"nr": "55012", "titel": "Ablehnung Beendigung der Zuordnung"}]}, {"art": "aperak", "werte": ["Z33"]}, {"art": "fortschreiben"}, {"art": "folgeprozess", "werte": ["55037"]}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55011](/schnittstellen/202610/pruefi/UTILMD/PI_55011) — Bestätigung Beendigung der Zuordnung · AS4
- [55012](/schnittstellen/202610/pruefi/UTILMD/PI_55012) — Ablehnung Beendigung der Zuordnung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **LFA** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `55011`, `55012` → [E_0624](/referenz/202610/ebd/E_0624) · LF · Anfrage zur Beendigung der Zuordnung prüfen

</div>

</li>

<li data-teil="aperak">

**Aperak-Prüfungen**
- `55011`, `55012` → `Z33`

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202610/backend-schreiben-nb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"NETZNUTZUNGSVERTRAG\": [\n      {\n        \"boTyp\": \"VERTRAG\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\",\n        \"vertragsart\": \"NETZNUTZUNGSVERTRAG\",\n        \"vertragsende\": \"2025-06-30T22:00:00Z\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9903790000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"anfragereferenznummer\": \"ABC123456\",\n    \"antwortstatus\": \"A36\",\n    \"antwortstatusCodeliste\": \"E_0624\",\n    \"datenaustauschreferenz\": \"104842\",\n    \"dokumentennummer\": \"353010BGM\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9900321000005\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"E02\",\n    \"nachrichtendatum\": \"2024-04-03T08:46:00Z\",\n    \"nachrichtenreferenznummer\": \"353010\",\n    \"pruefidentifikator\": \"55011\",\n    \"sparte\": \"STROM\",\n    \"transaktionsgrund\": \"E03\",\n    \"vertragsende\": \"2025-06-30T22:00:00Z\",\n    \"vorgangsnummer\": \"913628752\"\n  },\n  \"zusatzdaten\": {}\n}"} examples={[{"mediaType": "application/json", "examples": [{"name": "55011", "summary": "55011 — Bestätigung Beendigung der Zuordnung", "value": {"stammdaten": {"NETZNUTZUNGSVERTRAG": [{"boTyp": "VERTRAG", "versionStruktur": "1", "vertragsart": "NETZNUTZUNGSVERTRAG", "sparte": "STROM", "vertragsende": "2025-06-30T22:00:00Z"}]}, "transaktionsdaten": {"datenaustauschreferenz": "104842", "sparte": "STROM", "transaktionsgrund": "E03", "vorgangsnummer": "913628752", "pruefidentifikator": "55011", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9903790000002", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900321000005", "rollencodetyp": "BDEW"}, "dokumentennummer": "353010BGM", "kategorie": "E02", "nachrichtendatum": "2024-04-03T08:46:00Z", "nachrichtenreferenznummer": "353010", "anfragereferenznummer": "ABC123456", "antwortstatus": "A36", "antwortstatusCodeliste": "E_0624", "vertragsende": "2025-06-30T22:00:00Z"}, "zusatzdaten": {}}}, {"name": "55012", "summary": "55012 — Ablehnung Beendigung der Zuordnung", "value": {"stammdaten": {}, "transaktionsdaten": {"datenaustauschreferenz": "104842", "sparte": "STROM", "transaktionsgrund": "E03", "vorgangsnummer": "913628752", "pruefidentifikator": "55012", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9903790000002", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900321000005", "rollencodetyp": "BDEW"}, "dokumentennummer": "353010BGM", "kategorie": "E02", "nachrichtendatum": "2024-04-03T08:46:00Z", "nachrichtenreferenznummer": "353010", "anfragereferenznummer": "ABC123456", "antwortstatus": "A30", "antwortstatusCodeliste": "E_0624"}, "zusatzdaten": {}}}]}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend mit den Daten der eingegangenen Nachricht fort.

</li>

<li data-teil="folgeprozess">

**Folgeprozess auslösen**
- [55037](/schnittstellen/202610/pruefi/UTILMD/PI_55037) — Beendigung der Zuordnung

Nach der Verarbeitung startet die MACO APP diesen Folgeprozess selbst.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="5" anker="schritt-5" richtung="ausgehend" kopf={{"links": {"label": "NB", "eigen": true}, "rechts": {"label": "LFN"}}}>

### Zuordnung des LFN zur Marktlokation bzw. Tranche

<Schrittskizze sicht={{"label": "NB"}} zeilen={[{"art": "folge_ausloeser", "werte": ["55001", "55077"]}, {"art": "lesen_verarbeitung", "schnittstellen": [{"label": "Marktlokation lesen"}, {"label": "Messlokation lesen"}, {"label": "Netzlokation lesen"}, {"label": "Steuerbare Ressource lesen"}, {"label": "Technische Ressource lesen"}, {"label": "Bilanzierung lesen"}, {"label": "Messstellenbetriebsvertrag lesen"}, {"label": "Tranche lesen"}, {"label": "Zähler lesen"}]}, {"art": "senden", "label": "LFN", "weg": "AS4", "nachrichten": [{"nr": "55002", "titel": "Bestätigung Anmeldung verb. MaLo"}, {"nr": "55078", "titel": "Bestätigung Anmeldung erz. MaLo"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55002](/schnittstellen/202610/pruefi/UTILMD/PI_55002) — Bestätigung Anmeldung verb. MaLo · AS4
- [55078](/schnittstellen/202610/pruefi/UTILMD/PI_55078) — Bestätigung Anmeldung erz. MaLo · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="folge_ausloeser">

**Ausgelöst durch Eingang**
- [55001](/schnittstellen/202610/pruefi/UTILMD/PI_55001) — Anmeldung verb. MaLo
- [55077](/schnittstellen/202610/pruefi/UTILMD/PI_55077) — Anmeldung erz. MaLo

Die MACO APP sendet diese Nachricht selbst, als Folgeprozess nach einem dieser Eingänge.

</li>

<li data-teil="lesen" data-stufe="verarbeitung">

**Daten für die Verarbeitung laden**
- [Marktlokation lesen](/api/202610/backend-lesen/getmarketlocationbasic#marktlokation-lesen) `GET /getMarketLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getMarketLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": false, "defaultValue": "MALO", "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": false, "defaultValue": "2024-06-28T12:18:00Z", "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_MARKTLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Messlokation lesen](/api/202610/backend-lesen/getmeterlocationbasic#messlokation-lesen) `GET /getMeterLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getMeterLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_MESSLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Netzlokation lesen](/api/202610/backend-lesen/getgridlocationbasic#netzlokation-lesen) `GET /getGridLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getGridLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_NETZLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Steuerbare Ressource lesen](/api/202610/backend-lesen/getcontrollableresourcebasic#steuerbare-ressource-lesen) `GET /getControllableResourceBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getControllableResourceBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Technische Ressource lesen](/api/202610/backend-lesen/gettechnicalresourcebasic#technische-ressource-lesen) `GET /getTechnicalResourceBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getTechnicalResourceBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Bilanzierung lesen](/api/202610/backend-lesen/getaccountingbasic#bilanzierung-lesen) `GET /getAccountingBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getAccountingBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_BILANZIERUNG_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Messstellenbetriebsvertrag lesen](/api/202610/backend-lesen/getmeasuringpointoperationcontractbasic#messstellenbetriebsvertrag-lesen) `GET /getMeasuringPointOperationContractBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getMeasuringPointOperationContractBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_MESSSTELLENBETRIEBSVERTRAG_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Tranche lesen](/api/202610/backend-lesen/gettranchebasic#tranche-lesen) `GET /getTrancheBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getTrancheBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Zähler lesen](/api/202610/backend-lesen/getcounterbasic#zahler-lesen) `GET /getCounterBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getCounterBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

</li>

<li data-teil="nachricht">

Nachricht an **LFN** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `55002`, `55078` → [E_0623](/referenz/202610/ebd/E_0623) · NB · Lieferbeginn prüfen

</div>

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202610/backend-schreiben-nb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"MARKTLOKATION\": [\n      {\n        \"boTyp\": \"MARKTLOKATION\",\n        \"marktlokationsId\": \"50363198100\",\n        \"marktlokationsTyp\": [\n          {\n            \"typ\": \"STANDARD_MARKTLOKATION\"\n          }\n        ],\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      },\n      {\n        \"boTyp\": \"MARKTLOKATION\",\n        \"marktlokationsId\": \"50363198102\",\n        \"marktlokationsTyp\": [\n          {\n            \"typ\": \"RUHENDE_MARKTLOKATION\"\n          }\n        ],\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"MESSLOKATION\": [\n      {\n        \"boTyp\": \"MESSLOKATION\",\n        \"datenqualitaet\": \"INFORMATIVE_DATEN\",\n        \"marktrollen\": [\n          {\n            \"boTyp\": \"MARKTTEILNEHMER\",\n            \"gewerbekennzeichnung\": true,\n            \"marktrolle\": \"MSB\",\n            \"messstellenbetreiberEigenschaft\": \"GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER\",\n            \"rollencodenummer\": \"9980000000027\",\n            \"rollencodetyp\": \"BDEW\",\n            \"versionStruktur\": \"1\",\n            \"weiterverpflichtet\": false\n          },\n          {\n            \"boTyp\": \"MARKTTEILNEHMER\",\n            \"gewerbekennzeichnung\": true,\n            \"marktrolle\": \"GMSB\",\n            \"rollencodenummer\": \"9980000000023\",\n            \"rollencodetyp\": \"BDEW\",\n            \"versionStruktur\": \"1\"\n          }\n        ],\n        \"messlokationsId\": \"DE0032106765712000000000000001234\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"NETZLOKATION\": [\n      {\n        \"boTyp\": \"NETZLOKATION\",\n        \"datenqualitaet\": \"INFORMATIVE_DATEN\",\n        \"marktrollen\": [\n          {\n            \"boTyp\": \"MARKTTEILNEHMER\",\n            \"gewerbekennzeichnung\": true,\n            \"marktrolle\": \"MSB\",\n            \"messstellenbetreiberEigenschaft\": \"GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER\",\n            \"rollencodenummer\": \"9980000000024\",\n            \"rollencodetyp\": \"BDEW\",\n            \"versionStruktur\": \"1\"\n          }\n        ],\n        \"netzlokationsId\": \"E1688117482\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"NETZNUTZUNGSVERTRAG\": [\n      {\n        \"boTyp\": \"VERTRAG\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\",\n        \"vertragsart\": \"NETZNUTZUNGSVERTRAG\",\n        \"vertragsbeginn\": \"2024-12-01T23:00:00Z\",\n        \"vertragsende\": \"2024-12-02T23:00:00Z\"\n      }\n    ],\n    \"STEUERBARE_RESSOURCE\": [\n      {\n        \"boTyp\": \"STEUERBARE_RESSOURCE\",\n        \"datenqualitaet\": \"INFORMATIVE_DATEN\",\n        \"marktrollen\": [\n          {\n            \"boTyp\": \"MARKTTEILNEHMER\",\n            \"gewerbekennzeichnung\": true,\n            \"marktrolle\": \"MSB\",\n            \"messstellenbetreiberEigenschaft\": \"GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER\",\n            \"rollencodenummer\": \"9980000000026\",\n            \"rollencodetyp\": \"BDEW\",\n            \"versionStruktur\": \"1\"\n          }\n        ],\n        \"ressourcenId\": \"C81641SBT77\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"TECHNISCHE_RESSOURCE\": [\n      {\n        \"boTyp\": \"TECHNISCHE_RESSOURCE\",\n        \"ressourcenId\": \"D417MLM8164\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9980000000001\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"anfragereferenznummer\": \"NNV1230\",\n    \"antwortstatus\": \"A51\",\n    \"antwortstatusCodeliste\": \"E_0623\",\n    \"datenaustauschreferenz\": \"M38VVWXF\",\n    \"dokumentennummer\": \"BGMM2XZHIOV\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9980000000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"geplantesProduktpaket\": 1,\n    \"kategorie\": \"E01\",\n    \"nachrichtendatum\": \"2024-10-15T09:45:00Z\",\n    \"nachrichtenreferenznummer\": \"UNHM2SC7URW\",\n    \"pruefidentifikator\": \"55002\",\n    \"sparte\": \"STROM\",\n    \"transaktionsgrund\": \"E01\",\n    \"transaktionsgrundergaenzung\": \"ZAP\",\n    \"transaktionsgrundergaenzungBefristeteAnmeldung\": \"E01\",\n    \"vertragsbeginn\": \"2024-12-01T23:00:00Z\",\n    \"vertragsende\": \"2024-12-02T23:00:00Z\",\n    \"vorgangsnummer\": \"KBG27094210000000000929931413171000\"\n  },\n  \"zusatzdaten\": {}\n}"} examples={[{"mediaType": "application/json", "examples": [{"name": "55002", "summary": "55002 — Bestätigung Anmeldung verb. MaLo", "value": {"stammdaten": {"MARKTLOKATION": [{"boTyp": "MARKTLOKATION", "versionStruktur": "1", "marktlokationsId": "50363198100", "marktlokationsTyp": [{"typ": "STANDARD_MARKTLOKATION"}], "sparte": "STROM"}, {"boTyp": "MARKTLOKATION", "versionStruktur": "1", "marktlokationsId": "50363198102", "marktlokationsTyp": [{"typ": "RUHENDE_MARKTLOKATION"}], "sparte": "STROM"}], "NETZLOKATION": [{"boTyp": "NETZLOKATION", "versionStruktur": "1", "netzlokationsId": "E1688117482", "sparte": "STROM", "datenqualitaet": "INFORMATIVE_DATEN", "marktrollen": [{"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "marktrolle": "MSB", "gewerbekennzeichnung": true, "rollencodenummer": "9980000000024", "rollencodetyp": "BDEW", "messstellenbetreiberEigenschaft": "GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER"}]}], "MESSLOKATION": [{"boTyp": "MESSLOKATION", "versionStruktur": "1", "messlokationsId": "DE0032106765712000000000000001234", "sparte": "STROM", "datenqualitaet": "INFORMATIVE_DATEN", "marktrollen": [{"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "marktrolle": "MSB", "gewerbekennzeichnung": true, "rollencodenummer": "9980000000027", "rollencodetyp": "BDEW", "weiterverpflichtet": false, "messstellenbetreiberEigenschaft": "GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER"}, {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "marktrolle": "GMSB", "gewerbekennzeichnung": true, "rollencodenummer": "9980000000023", "rollencodetyp": "BDEW"}]}], "TECHNISCHE_RESSOURCE": [{"boTyp": "TECHNISCHE_RESSOURCE", "versionStruktur": "1", "ressourcenId": "D417MLM8164", "sparte": "STROM"}], "STEUERBARE_RESSOURCE": [{"boTyp": "STEUERBARE_RESSOURCE", "versionStruktur": "1", "ressourcenId": "C81641SBT77", "sparte": "STROM", "datenqualitaet": "INFORMATIVE_DATEN", "marktrollen": [{"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "marktrolle": "MSB", "gewerbekennzeichnung": true, "rollencodenummer": "9980000000026", "rollencodetyp": "BDEW", "messstellenbetreiberEigenschaft": "GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER"}]}], "NETZNUTZUNGSVERTRAG": [{"boTyp": "VERTRAG", "versionStruktur": "1", "vertragsart": "NETZNUTZUNGSVERTRAG", "sparte": "STROM", "vertragsbeginn": "2024-12-01T23:00:00Z", "vertragsende": "2024-12-02T23:00:00Z"}]}, "transaktionsdaten": {"datenaustauschreferenz": "M38VVWXF", "sparte": "STROM", "transaktionsgrund": "E01", "transaktionsgrundergaenzung": "ZAP", "transaktionsgrundergaenzungBefristeteAnmeldung": "E01", "vorgangsnummer": "KBG27094210000000000929931413171000", "pruefidentifikator": "55002", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9980000000001", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9980000000002", "rollencodetyp": "BDEW"}, "dokumentennummer": "BGMM2XZHIOV", "kategorie": "E01", "nachrichtendatum": "2024-10-15T09:45:00Z", "nachrichtenreferenznummer": "UNHM2SC7URW", "anfragereferenznummer": "NNV1230", "antwortstatus": "A51", "antwortstatusCodeliste": "E_0623", "geplantesProduktpaket": 1, "vertragsbeginn": "2024-12-01T23:00:00Z", "vertragsende": "2024-12-02T23:00:00Z"}, "zusatzdaten": {}}}, {"name": "55078", "summary": "55078 — Bestätigung Anmeldung erz. MaLo", "value": {"stammdaten": {"MARKTLOKATION": [{"boTyp": "MARKTLOKATION", "versionStruktur": "1", "datenqualitaet": "INFORMATIVE_DATEN", "marktlokationsId": "50074561188", "sparte": "STROM", "marktrollen": [{"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "marktrolle": "MSB", "rollencodenummer": "9904446000007", "weiterverpflichtet": false, "messstellenbetreiberEigenschaft": "GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER"}]}], "MESSLOKATION": [{"boTyp": "MESSLOKATION", "versionStruktur": "1", "datenqualitaet": "INFORMATIVE_DATEN", "messlokationsId": "DE0032106765712000000000000000037", "sparte": "STROM", "marktrollen": [{"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "marktrolle": "MSB", "rollencodenummer": "9904446000007", "weiterverpflichtet": false, "messstellenbetreiberEigenschaft": "GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER"}, {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "marktrolle": "GMSB", "rollencodenummer": "9904446000007"}]}], "NETZNUTZUNGSVERTRAG": [{"boTyp": "VERTRAG", "versionStruktur": "1", "vertragsart": "NETZNUTZUNGSVERTRAG", "sparte": "STROM", "vertragsbeginn": "2025-04-30T22:00:00Z"}]}, "transaktionsdaten": {"datenaustauschreferenz": "LZECUKCK", "sparte": "STROM", "transaktionsgrund": "E03", "transaktionsgrundergaenzung": "ZW0", "vorgangsnummer": "1829631672", "pruefidentifikator": "55078", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9900321000005", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9903790000002", "rollencodetyp": "BDEW"}, "dokumentennummer": "BGMLZULMI89", "kategorie": "E01", "nachrichtendatum": "2025-04-01T07:59:00Z", "nachrichtenreferenznummer": "UNHLZBUIWW9", "anfragereferenznummer": "REF12345678910", "antwortstatus": "A51", "antwortstatusCodeliste": "E_0623", "geplantesProduktpaket": 1, "vertragsbeginn": "2025-04-30T22:00:00Z"}}}]}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend fort, nachdem die Nachricht erstellt ist.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="6" anker="schritt-6" richtung="ausgehend" kopf={{"links": {"label": "NB", "eigen": true}, "rechts": {"label": "LFN"}}}>

### Ablehnung der Anmeldung einer Zuordnung des LFN zur Marktlokation bzw. Tranche

<Schrittskizze sicht={{"label": "NB"}} zeilen={[{"art": "folge_ausloeser", "werte": ["55001", "55077"]}, {"art": "senden", "label": "LFN", "weg": "AS4", "nachrichten": [{"nr": "55003", "titel": "Ablehnung Anmeldung verb. MaLo"}, {"nr": "55080", "titel": "Ablehnung Anmeldung erz. MaLo"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55003](/schnittstellen/202610/pruefi/UTILMD/PI_55003) — Ablehnung Anmeldung verb. MaLo · AS4
- [55080](/schnittstellen/202610/pruefi/UTILMD/PI_55080) — Ablehnung Anmeldung erz. MaLo · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="folge_ausloeser">

**Ausgelöst durch Eingang**
- [55001](/schnittstellen/202610/pruefi/UTILMD/PI_55001) — Anmeldung verb. MaLo
- [55077](/schnittstellen/202610/pruefi/UTILMD/PI_55077) — Anmeldung erz. MaLo

Die MACO APP sendet diese Nachricht selbst, als Folgeprozess nach einem dieser Eingänge.

</li>

<li data-teil="nachricht">

Nachricht an **LFN** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `55003`, `55080` → [E_0622](/referenz/202610/ebd/E_0622) · NB · Prüfen, ob Anmeldung direkt ablehnbar
- `55003`, `55080` → [E_0623](/referenz/202610/ebd/E_0623) · NB · Lieferbeginn prüfen

</div>

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202610/backend-schreiben-nb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {},\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9980000000001\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"anfragereferenznummer\": \"NNV1230\",\n    \"antwortstatus\": \"A45\",\n    \"antwortstatusCodeliste\": \"E_0622\",\n    \"datenaustauschreferenz\": \"M2QSI98I\",\n    \"dokumentennummer\": \"BGMM37574AD\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9980000000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"E01\",\n    \"nachrichtendatum\": \"2026-10-02T11:00:00Z\",\n    \"nachrichtenreferenznummer\": \"UNHM2FDVMMI\",\n    \"pruefidentifikator\": \"55003\",\n    \"sparte\": \"STROM\",\n    \"transaktionsgrund\": \"E01\",\n    \"transaktionsgrundergaenzung\": \"ZW4\",\n    \"vorgangsnummer\": \"KBG27094210000000000929931413171000\"\n  },\n  \"zusatzdaten\": {}\n}"} examples={[{"mediaType": "application/json", "examples": [{"name": "55003", "summary": "55003 — Ablehnung Anmeldung verb. MaLo", "value": {"stammdaten": {}, "transaktionsdaten": {"datenaustauschreferenz": "M2QSI98I", "sparte": "STROM", "transaktionsgrund": "E01", "transaktionsgrundergaenzung": "ZW4", "vorgangsnummer": "KBG27094210000000000929931413171000", "pruefidentifikator": "55003", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9980000000001", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9980000000002", "rollencodetyp": "BDEW"}, "dokumentennummer": "BGMM37574AD", "kategorie": "E01", "nachrichtendatum": "2026-10-02T11:00:00Z", "nachrichtenreferenznummer": "UNHM2FDVMMI", "anfragereferenznummer": "NNV1230", "antwortstatus": "A45", "antwortstatusCodeliste": "E_0622"}, "zusatzdaten": {}}}, {"name": "55080", "summary": "55080 — Ablehnung Anmeldung erz. MaLo", "value": {"stammdaten": {}, "transaktionsdaten": {"datenaustauschreferenz": "DAGQKITMEGKDRX", "sparte": "STROM", "transaktionsgrund": "E03", "transaktionsgrundergaenzung": "ZW3", "vorgangsnummer": "24062416225400000000000102159662022", "pruefidentifikator": "55080", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9900327000009", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9903729000007", "rollencodetyp": "BDEW"}, "dokumentennummer": "DA582410161540539903323000007307618", "kategorie": "E01", "nachrichtendatum": "2026-10-02T11:00:00Z", "nachrichtenreferenznummer": "DAPTYGIPXPUJXS", "anfragereferenznummer": "NNV1234", "antwortstatus": "A99", "antwortstatusCodeliste": "E_0623", "freitext": "Weil"}, "zusatzdaten": {}}}]}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend fort, nachdem die Nachricht erstellt ist.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="10" anker="schritt-10" richtung="ausgehend" kopf={{"links": {"label": "NB", "eigen": true}, "rechts": {"label": "LFA"}}}>

### Beendigung der Zuordnung des LFA zur Marktlokation bzw. Tranche

<Schrittskizze sicht={{"label": "NB"}} zeilen={[{"art": "folge_ausloeser", "werte": ["55001", "55011"]}, {"art": "ausloeser", "werte": ["START_ENDE_ZUORDNUNG"]}, {"art": "senden", "label": "LFA", "weg": "AS4", "nachrichten": [{"nr": "55037", "titel": "Beendigung der Zuordnung"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55037](/schnittstellen/202610/pruefi/UTILMD/PI_55037) — Beendigung der Zuordnung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="folge_ausloeser">

**Ausgelöst durch Eingang**
- [55001](/schnittstellen/202610/pruefi/UTILMD/PI_55001) — Anmeldung verb. MaLo
- [55011](/schnittstellen/202610/pruefi/UTILMD/PI_55011) — Bestätigung Beendigung der Zuordnung

Die MACO APP sendet diese Nachricht selbst, als Folgeprozess nach einem dieser Eingänge. Daneben kann das Backend diesen Schritt mit einem Ereignis anstoßen — der nächste Punkt.

</li>

<li data-teil="ausloeser">

**Prozessauslöser** [`START_ENDE_ZUORDNUNG`](/schnittstellen/202610/trigger/events/NB-START_ENDE_ZUORDNUNG) · [Im Playground ausprobieren](/api/202610/ausloeser-nb/start-ende-zuordnung)

Das Backend stößt diesen Schritt mit diesem Ereignis an.

</li>

<li data-teil="nachricht">

Nachricht an **LFA** · AS4

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202610/backend-schreiben-nb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"MARKTLOKATION\": [\n      {\n        \"boTyp\": \"MARKTLOKATION\",\n        \"marktlokationsId\": \"10017211334\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"NETZNUTZUNGSVERTRAG\": [\n      {\n        \"boTyp\": \"VERTRAG\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\",\n        \"vertragsart\": \"NETZNUTZUNGSVERTRAG\",\n        \"vertragsende\": \"2025-04-30T22:00:00Z\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9900321000005\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"datenaustauschreferenz\": \"002001528776\",\n    \"dokumentennummer\": \"002001528776\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9903790000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"E02\",\n    \"nachrichtendatum\": \"2024-04-01T22:01:00Z\",\n    \"nachrichtenreferenznummer\": \"002001528776\",\n    \"pruefidentifikator\": \"55037\",\n    \"sparte\": \"STROM\",\n    \"transaktionsgrund\": \"ZC8\",\n    \"transaktionsgrundergaenzung\": \"ZW4\",\n    \"vertragsende\": \"2025-04-30T22:00:00Z\",\n    \"vorgangsnummer\": \"051MlNQB7jwRfnYJzb71SW\"\n  }\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend fort, nachdem die Nachricht erstellt ist.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="13" anker="schritt-13" richtung="ausgehend" kopf={{"links": {"label": "NB", "eigen": true}, "rechts": {"label": "LFZ"}}}>

### Aufhebung der Zuordnung des LFZ zur Marklokation bzw. Tranche

<Schrittskizze sicht={{"label": "NB"}} zeilen={[{"art": "ausloeser", "werte": ["START_AUFH_ZUK_ZUORDNUNG"]}, {"art": "lesen_verarbeitung", "schnittstellen": [{"label": "Bilanzierung lesen"}, {"label": "Marktlokation lesen"}, {"label": "Netznutzungsvertrag lesen"}]}, {"art": "senden", "label": "LFZ", "weg": "AS4", "nachrichten": [{"nr": "55038", "titel": "Aufhebung einer zuk. Zuordnung"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55038](/schnittstellen/202610/pruefi/UTILMD/PI_55038) — Aufhebung einer zuk. Zuordnung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="ausloeser">

**Prozessauslöser** [`START_AUFH_ZUK_ZUORDNUNG`](/schnittstellen/202610/trigger/events/NB-START_AUFH_ZUK_ZUORDNUNG) · [Im Playground ausprobieren](/api/202610/ausloeser-nb/start-aufh-zuk-zuordnung)

Das Backend stößt diesen Schritt mit diesem Ereignis an.

</li>

<li data-teil="lesen" data-stufe="verarbeitung">

**Daten für die Verarbeitung laden**
- [Bilanzierung lesen](/api/202610/backend-lesen/getaccountingbasic#bilanzierung-lesen) `GET /getAccountingBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getAccountingBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_BILANZIERUNG_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Marktlokation lesen](/api/202610/backend-lesen/getmarketlocationbasic#marktlokation-lesen) `GET /getMarketLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getMarketLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": false, "defaultValue": "MALO", "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": false, "defaultValue": "2024-06-28T12:18:00Z", "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_MARKTLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Netznutzungsvertrag lesen](/api/202610/backend-lesen/getgridusagecontractbasic#netznutzungsvertrag-lesen) `GET /getGridUsageContractBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getGridUsageContractBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": false, "defaultValue": "MALO", "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": false, "defaultValue": "2024-06-28T12:18:00Z", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

</li>

<li data-teil="nachricht">

Nachricht an **LFZ** · AS4

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202610/backend-schreiben-nb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"MARKTLOKATION\": [\n      {\n        \"beteiligterMarktpartner\": {\n          \"boTyp\": \"MARKTTEILNEHMER\",\n          \"rollencodenummer\": \"9903790000002\",\n          \"rollencodetyp\": \"BDEW\",\n          \"versionStruktur\": \"1\"\n        },\n        \"boTyp\": \"MARKTLOKATION\",\n        \"marktlokationsId\": \"10017211334\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"NETZNUTZUNGSVERTRAG\": [\n      {\n        \"boTyp\": \"VERTRAG\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\",\n        \"vertragsart\": \"NETZNUTZUNGSVERTRAG\",\n        \"vertragsbeginn\": \"2026-04-30T22:00:00Z\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9900321000005\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"datenaustauschreferenz\": \"607048\",\n    \"dokumentennummer\": \"893296BGM\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9903790000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"E02\",\n    \"nachrichtendatum\": \"2026-10-02T11:00:00Z\",\n    \"nachrichtenreferenznummer\": \"893296\",\n    \"pruefidentifikator\": \"55038\",\n    \"sparte\": \"STROM\",\n    \"transaktionsgrund\": \"ZH1\",\n    \"transaktionsgrundergaenzung\": \"ZW4\",\n    \"vertragsbeginn\": \"2026-04-30T22:00:00Z\",\n    \"vorgangsnummer\": \"1631102530\"\n  }\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

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
| [E_0622](/referenz/202610/ebd/E_0622) | Prüfen, ob Anmeldung direkt ablehnbar |
| [E_0623](/referenz/202610/ebd/E_0623) | Lieferbeginn prüfen |
| [E_0624](/referenz/202610/ebd/E_0624) | Anfrage zur Beendigung der Zuordnung prüfen |

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
  - Der NB führt die Use-Cases „[Abrechnungsdaten Netznutzungsabrechnung](/prozessdoku/202610/NB/GPKE-Teil2-abrechnungsdaten-netznutzungsabrechnung)“ und „[Abrechnungsdaten Bilanzkreisabrechnung](/prozessdoku/202610/NB/GPKE-Teil2-abrechnungsdaten-bilanzkreisabrechnung)“ aus.
  - Etwa entstehende Zuordnungslücken werden vom NB durch Zuordnung des E/G zur Marktlokation in Anwendung des Use-Cases „[Beginn der Ersatz-/Grundversorgung](/prozessdoku/202610/NB/GPKE-Teil2-beginn-der-ersatz-grundversorgung)“ geschlossen.
  - Sofern die Marktlokation gesperrt ist, führt der NB den Use-Case „[Wiederherstellung der Anschlussnutzung bei Lieferbeginn](/prozessdoku/202610/NB/GPKE-Teil2-wiederherstellung-der-anschlussnutzung-bei-lieferbeginn)“ aus.
- Im Fall einer erzeugenden Marktlokation bzw. einer Tranche:
  - Der NB führt den Use-Case „[Abrechnungsdaten Bilanzkreisabrechnung](/prozessdoku/202610/NB/GPKE-Teil2-abrechnungsdaten-bilanzkreisabrechnung)“ aus.
  - Etwa entstehende Zuordnungslücken werden vom NB im Rahmen des Use-Cases „Herstellung einer 100% LF-Zuordnung zu einer erzeugenden Marktlokation“ geschlossen.
- Der NB führt den Use-Case „Stammdatenänderung“ (hier: SD „[Stammdatenänderung vom NB (verantwortlich) ausgehend](/prozessdoku/202610/NB/GPKE-Teil4-stammdatenaenderung-vom-nb-verantwortlich-ausgehend)“) (GPKE Teil 4) durch.
- Der NB versendet die Berechnungsformel an den LFN.
- Der NB führt den Use-Case „[Einrichtung der Konfigurationen aufgrund einer Zuordnung eines LF zu einer Marktlokation bzw. Tranche](/prozessdoku/202610/NB/GPKE-Teil3-einrichtung-der-konfigurationen-aufgrund-einer-zuordnung-eines-lf-zu-einer-marktlokation-bzw-tranche)“ (GPKE Teil 3) aus.
- Der LFN führt den Use-Case „Stammdatenänderung“ (hier: SD „[Stammdatenänderung vom LF (verantwortlich) ausgehend](/prozessdoku/202610/NB/GPKE-Teil4-stammdatenaenderung-vom-lf-verantwortlich-ausgehend)“) (GPKE Teil 4) durch.

</li>

<li data-blatt="fehlerfall">

### Fehlerfall

#### Ergebnis im Fehlerfall

- Der LFN wurde der Marktlokation bzw. Tranche nicht zugeordnet.
- Der LFA bleibt der Marktlokation bzw. Tranche zugeordnet, sofern für diesen nicht bereits die Zuordnung im Rahmen eines anderen Use-Cases (z.B. „Lieferende von LF an NB) beendet wurde.
- Im Fall einer verbrauchenden Marktlokation: Der NB führt ggf. den Use-Case „[Beginn der Ersatz-/Grundversorgung](/prozessdoku/202610/NB/GPKE-Teil2-beginn-der-ersatz-grundversorgung)“ aus.
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
- Hinweis: Die Zuordnung des LF zur Marktlokation bzw. Tranche bei einer Inbetriebnahme einer Marktlokation (Neuanlage) findet über den Use-Case „[Neuanlage](/prozessdoku/202610/NB/GPKE-Teil2-neuanlage)“, „[Beginn der Ersatz-/Grundversorgung](/prozessdoku/202610/NB/GPKE-Teil2-beginn-der-ersatz-grundversorgung)“ oder „Herstellung einer 100% LF-Zuordnung zu einer erzeugenden Marktlokation“ statt.
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

**Vorher läuft:** [Abrechnungsdaten Netznutzungsabrechnung](/prozessdoku/202610/NB/GPKE-Teil2-abrechnungsdaten-netznutzungsabrechnung), [Ermittlung der MaLo-ID der Marktlokation](/prozessdoku/202610/NB/GPKE-Teil2-ermittlung-der-malo-id-der-marktlokation), [Neuanlage](/prozessdoku/202610/NB/GPKE-Teil2-neuanlage) — diese Prozesse nennen den hier gezeigten in ihrem Ergebnis.

</li>

<li data-blatt="erste-nachricht">

### Erste Nachricht

**LFN** sendet „Anmeldung einer Zuordnung des LFN zur Marktlokation bzw. Tranche“ (Schritt 1). Ab hier ist der Beteiligte dieser Seite am Zug.

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

- [Sicht LFA](/prozessdoku/202610/LF--LFA/GPKE-Teil2-lieferbeginn) — der abgebende Lieferant · Marktrolle LF
- [Sicht LFN](/prozessdoku/202610/LF--LFN/GPKE-Teil2-lieferbeginn) — der aufnehmende Lieferant · Marktrolle LF
- [Sicht LFZ](/prozessdoku/202610/LF--LFZ/GPKE-Teil2-lieferbeginn) — Lieferant zukünftig · Marktrolle LF

<Hinweisbereich>

*Die Schritte sind die **möglichen** Nachrichten dieses Prozesses, keine Abfolge — die Quelle führt weder Bedingungen noch Alternativen. Das Kästchen am Schritt nennt links die eigene Sicht: **←** empfängt sie, **→** sendet sie. Zugeklappte Schritte laufen zwischen anderen Marktpartnern. Die Nummern sind die der Quelle; wo eine fehlt, fehlt sie dort.*

</Hinweisbereich>
