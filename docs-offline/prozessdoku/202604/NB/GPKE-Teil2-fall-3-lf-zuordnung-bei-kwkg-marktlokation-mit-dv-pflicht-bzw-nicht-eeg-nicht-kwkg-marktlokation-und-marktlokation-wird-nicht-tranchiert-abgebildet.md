# Fall 3: LF-Zuordnung bei KWKG-Marktlokation mit DV-Pflicht bzw. Nicht-EEG-/Nicht-KWKG-Marktlokation und Marktlokation wird nicht-tranchiert abgebildet — Sicht NB

<Kopf rolle="NB" beteiligter="NB" festlegung="GPKE" dokument="GPKE Teil 2" kapitel="2.4.2.4" sparte="Strom" schritte={4} suchtitel="Fall 3: LF-Zuordnung bei KWKG-Marktlokation mit DV-Pflicht bzw. Nicht-EEG-/Nicht-KWKG-Marktlokation und Marktlokation wird nicht-tranchiert abgebildet — Sicht NB · GPKE Teil 2 · Formatversion 202604" abschnitte={[{"id": "abschnitt-ablauf", "label": "Prozessablauf"}, {"id": "abschnitt-schritte", "label": "Prozessschritte"}, {"id": "abschnitt-informationen", "label": "Prozess-Informationen"}, {"id": "abschnitt-sichten", "label": "Andere Sichten des Prozesses"}]} />

<Kurzfassung>

Der NB kündigt dem LFN bei
- einer EEG-Marktlokation ohne DV-Pflicht bzw. KWKG-Marktlokation ohne DV-Pflicht die Zuordnung des LFN (hier: LF des Unternehmens Netzbetreiber) zur Marktlokation bzw. Tranche (Restmenge) an (s. Fall 1 der SD).
- einer EEG-Marktlokation mit DV-Pflicht die Zuordnung des LFN (hier: LF des Unternehmens Netzbetreiber) zur Marktlokation an (s. Fall 2 der SD). Im Fall einer bisher tranchierten Marktlokation beendet der NB die Zuordnung der LFA zur jeweiligen Tranche aufgrund des Verbots der anteiligen Zuordnung zu § 38 EEG 2014 bzw. zu § 21 Abs. 1 Nr. 2 EEG 2017, 21b Abs. 2 Satz 2 EEG 2021 bzw. EEG 2023.
- einer KWKG-Marktlokation mit DV-Pflicht bzw. Nicht-EEG-/Nicht-KWKG-Marktlokation nach der bilateralen Klärung
  - die Zuordnung des LFN zur Marktlokation an (s. Fall 3 der SD) oder
  - die Zuordnung des LFN zur Tranche an (s. Fall 4 der SD). Hierbei muss Fall 4 der SD je LFN zu einer Tranche der Marktlokation separat durchgeführt werden. Im Zuge des Prozesses beendet der NB ggf. die Zuordnung eines LFA zu einer Tranche. Hinweis: Der LFN kann nach der bilateralen Klärung der LF des Unternehmens Netzbetreiber sein.

</Kurzfassung>

<a id="abschnitt-ablauf"></a>

## Prozessablauf aus Sicht des NB

<Systembild svg={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1004 1130\" width=\"1004\" height=\"1130\" role=\"img\" aria-labelledby=\"sb-title\" class=\"maco-systembild\">\n<title id=\"sb-title\">Systembild: Fall 3: LF-Zuordnung bei KWKG-Marktlokation mit DV-Pflicht bzw. Nicht-EEG-/Nicht-KWKG-Marktlokation und Marktlokation wird nicht-tranchiert abgebildet aus Sicht NB</title>\n<defs><marker id=\"sb-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect class=\"sb-lane-kopf\" x=\"16\" y=\"12\" width=\"232\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend-System des Kunden</text>\n<rect class=\"sb-lane-kopf\" x=\"398\" y=\"12\" width=\"264\" height=\"46\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · NB</text>\n<rect class=\"sb-lane-kopf\" x=\"812\" y=\"12\" width=\"176\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"900\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Marktpartner</text>\n<line x1=\"323\" y1=\"58\" x2=\"323\" y2=\"1118\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"737\" y1=\"58\" x2=\"737\" y2=\"1118\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect class=\"sb-kasten sb-trigger\" x=\"432\" y=\"80\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessauslöser empfangen</text>\n<rect class=\"sb-kasten sb-backend sb-trigger\" x=\"34\" y=\"72\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"92\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">START_ZUORDNUNG_ERZ_M</text>\n<text x=\"132\" y=\"107\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">ALO_TRANCHE</text>\n<line x1=\"230\" y1=\"96\" x2=\"432\" y2=\"96\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"88\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"154\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"174\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">1. Ankündigung der</text>\n<text x=\"530\" y=\"189\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Zuordnung des LFN zur</text>\n<text x=\"530\" y=\"204\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Marktlokation</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"113\" x2=\"530\" y2=\"154\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"167\" r=\"5\"/><line x1=\"900\" y1=\"172\" x2=\"900\" y2=\"184\"/><line x1=\"893\" y1=\"176\" x2=\"907\" y2=\"176\"/><line x1=\"900\" y1=\"184\" x2=\"894\" y2=\"194\"/><line x1=\"900\" y1=\"184\" x2=\"906\" y2=\"194\"/></g>\n<text x=\"900\" y=\"216\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">LFN</text>\n<line x1=\"628\" y1=\"185\" x2=\"878\" y2=\"185\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"177\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"201\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">55607</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"243\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"263\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"217\" x2=\"530\" y2=\"243\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"243\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"263\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"259\" x2=\"230\" y2=\"259\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"251\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"307\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"327\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">2. Antwort auf Ankündigung</text>\n<text x=\"530\" y=\"342\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">der Zuordnung des LFN zur</text>\n<text x=\"530\" y=\"357\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Marktloka…</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"276\" x2=\"530\" y2=\"307\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"320\" r=\"5\"/><line x1=\"900\" y1=\"325\" x2=\"900\" y2=\"337\"/><line x1=\"893\" y1=\"329\" x2=\"907\" y2=\"329\"/><line x1=\"900\" y1=\"337\" x2=\"894\" y2=\"347\"/><line x1=\"900\" y1=\"337\" x2=\"906\" y2=\"347\"/></g>\n<text x=\"900\" y=\"369\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">LFN</text>\n<line x1=\"878\" y1=\"338\" x2=\"628\" y2=\"338\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"330\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"354\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">55608, 55609</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"396\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"416\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z33</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"370\" x2=\"530\" y2=\"396\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-schreiben\" x=\"432\" y=\"460\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"480\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"429\" x2=\"530\" y2=\"460\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-schreiben\" x=\"34\" y=\"460\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"480\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten erstellen</text>\n<line x1=\"432\" y1=\"476\" x2=\"230\" y2=\"476\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"468\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"524\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"544\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"493\" x2=\"530\" y2=\"524\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"524\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"544\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"540\" x2=\"230\" y2=\"540\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"532\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-trigger\" x=\"432\" y=\"588\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"608\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessauslöser empfangen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"557\" x2=\"530\" y2=\"588\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-trigger\" x=\"34\" y=\"580\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"600\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">START_ZUORDNUNG_ERZ_M</text>\n<text x=\"132\" y=\"615\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">ALO_TRANCHE</text>\n<line x1=\"230\" y1=\"604\" x2=\"432\" y2=\"604\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"596\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"662\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"682\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">3. Zuordnung des LFN zur</text>\n<text x=\"530\" y=\"697\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Marktlokation aufgrund</text>\n<text x=\"530\" y=\"712\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">fehlender Antw…</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"621\" x2=\"530\" y2=\"662\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"675\" r=\"5\"/><line x1=\"900\" y1=\"680\" x2=\"900\" y2=\"692\"/><line x1=\"893\" y1=\"684\" x2=\"907\" y2=\"684\"/><line x1=\"900\" y1=\"692\" x2=\"894\" y2=\"702\"/><line x1=\"900\" y1=\"692\" x2=\"906\" y2=\"702\"/></g>\n<text x=\"900\" y=\"724\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">LFN</text>\n<line x1=\"628\" y1=\"693\" x2=\"878\" y2=\"693\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"685\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"709\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">55607</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"751\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"771\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"725\" x2=\"530\" y2=\"751\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"751\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"771\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"767\" x2=\"230\" y2=\"767\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"759\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-folge_ausloeser\" x=\"432\" y=\"815\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"835\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Ausgelöst durch Eingang:</text>\n<text x=\"530\" y=\"850\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">55001, 55011</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"784\" x2=\"530\" y2=\"815\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-trigger\" x=\"432\" y=\"889\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"909\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessauslöser empfangen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"863\" x2=\"530\" y2=\"889\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-trigger\" x=\"34\" y=\"889\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"909\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">START_ENDE_ZUORDNUNG</text>\n<line x1=\"230\" y1=\"905\" x2=\"432\" y2=\"905\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"897\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"953\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"973\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">8. Beendigung der</text>\n<text x=\"530\" y=\"988\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Zuordnung des LFA zur</text>\n<text x=\"530\" y=\"1003\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Tranche</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"922\" x2=\"530\" y2=\"953\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"966\" r=\"5\"/><line x1=\"900\" y1=\"971\" x2=\"900\" y2=\"983\"/><line x1=\"893\" y1=\"975\" x2=\"907\" y2=\"975\"/><line x1=\"900\" y1=\"983\" x2=\"894\" y2=\"993\"/><line x1=\"900\" y1=\"983\" x2=\"906\" y2=\"993\"/></g>\n<text x=\"900\" y=\"1015\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">LFA</text>\n<line x1=\"628\" y1=\"984\" x2=\"878\" y2=\"984\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"976\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"1000\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">55037</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"1042\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"1062\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"1016\" x2=\"530\" y2=\"1042\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"1042\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"1062\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"1058\" x2=\"230\" y2=\"1058\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"1050\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n</svg>"} gesamt={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 974 858\" width=\"974\" height=\"858\" role=\"img\" aria-labelledby=\"sd-title\" class=\"maco-sequence\">\n<title id=\"sd-title\">Sequenzdiagramm: Fall 3: LF-Zuordnung bei KWKG-Marktlokation mit DV-Pflicht bzw. Nicht-EEG-/Nicht-KWKG-Marktlokation und Marktlokation wird nicht-tranchiert abgebildet aus Sicht NB</title>\n<defs><marker id=\"sd-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect x=\"16\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"121\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend (Kunde)</text>\n<line x1=\"121\" y1=\"64\" x2=\"121\" y2=\"846\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"260\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"365\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · NB</text>\n<line x1=\"365\" y1=\"64\" x2=\"365\" y2=\"846\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"504\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"609\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">LFN</text>\n<line x1=\"609\" y1=\"64\" x2=\"609\" y2=\"846\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"748\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"853\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">LFA</text>\n<line x1=\"853\" y1=\"64\" x2=\"853\" y2=\"846\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"121\" y1=\"90\" x2=\"365\" y2=\"90\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"81\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">START_ZUORDNUNG_ERZ_MALO_TRANCHE</text>\n<text x=\"243\" y=\"105\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Trigger-Event</text>\n<line x1=\"365\" y1=\"152\" x2=\"609\" y2=\"152\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"143\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">1. Ankündigung der Zuordnung des LFN zur Marktlo…</text>\n<text x=\"487\" y=\"167\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55607</text>\n<line x1=\"365\" y1=\"214\" x2=\"121\" y2=\"214\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"205\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"229\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"609\" y1=\"276\" x2=\"365\" y2=\"276\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"267\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">2. Antwort auf Ankündigung der Zuordnung des LFN…</text>\n<text x=\"487\" y=\"291\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55608, 55609 · E_0605</text>\n<text x=\"487\" y=\"304\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0605 — Zuordnung prüfen</text>\n<line x1=\"365\" y1=\"338\" x2=\"121\" y2=\"338\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"329\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<text x=\"243\" y=\"353\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten erstellen</text>\n<line x1=\"365\" y1=\"400\" x2=\"121\" y2=\"400\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"391\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"415\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"121\" y1=\"462\" x2=\"365\" y2=\"462\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"453\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">START_ZUORDNUNG_ERZ_MALO_TRANCHE</text>\n<text x=\"243\" y=\"477\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Trigger-Event</text>\n<line x1=\"365\" y1=\"524\" x2=\"609\" y2=\"524\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"515\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">3. Zuordnung des LFN zur Marktlokation aufgrund…</text>\n<text x=\"487\" y=\"539\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55607</text>\n<line x1=\"365\" y1=\"586\" x2=\"121\" y2=\"586\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"577\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"601\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"121\" y1=\"648\" x2=\"365\" y2=\"648\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"639\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">START_ENDE_ZUORDNUNG</text>\n<text x=\"243\" y=\"663\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Trigger-Event</text>\n<line x1=\"365\" y1=\"710\" x2=\"853\" y2=\"710\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"609\" y=\"701\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">8. Beendigung der Zuordnung des LFA zur Tranche</text>\n<text x=\"609\" y=\"725\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55037</text>\n<line x1=\"365\" y1=\"772\" x2=\"121\" y2=\"772\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"763\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"787\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n</svg>"} titel="NB" />

<a id="abschnitt-schritte"></a>

## Prozessschritte

<Schritt nr="1" anker="schritt-1" richtung="ausgehend" kopf={{"links": {"label": "NB", "eigen": true}, "rechts": {"label": "LFN"}}}>

### Ankündigung der Zuordnung des LFN zur Marktlokation

<Schrittskizze sicht={{"label": "NB"}} zeilen={[{"art": "ausloeser", "werte": ["START_ZUORDNUNG_ERZ_MALO_TRANCHE"]}, {"art": "senden", "label": "LFN", "weg": "AS4", "nachrichten": [{"nr": "55607", "titel": "Ankündigung Zuordnung / Zuordnung des LF zur MaLo/ Tranche"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55607](/schnittstellen/202604/pruefi/UTILMD/PI_55607) — Ankündigung Zuordnung / Zuordnung des LF zur MaLo/ Tranche · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="ausloeser">

**Prozessauslöser** [`START_ZUORDNUNG_ERZ_MALO_TRANCHE`](/schnittstellen/202604/trigger/events/NB-START_ZUORDNUNG_ERZ_MALO_TRANCHE) · [Im Playground ausprobieren](/api/202604/ausloeser-nb/start-zuordnung-erz-malo-tranche)

Das Backend stößt diesen Schritt mit diesem Ereignis an.

</li>

<li data-teil="nachricht">

Nachricht an **LFN** · AS4

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202604/backend-schreiben-nb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"MARKTLOKATION\": [\n      {\n        \"boTyp\": \"MARKTLOKATION\",\n        \"datenqualitaet\": \"INFORMATIVE_DATEN\",\n        \"energieherkunft\": [\n          {\n            \"erzeugungsart\": \"EEG_DV\"\n          }\n        ],\n        \"marktlokationsId\": \"50074561188\",\n        \"marktrollen\": [\n          {\n            \"boTyp\": \"MARKTTEILNEHMER\",\n            \"marktrolle\": \"MSB\",\n            \"messstellenbetreiberEigenschaft\": \"GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER\",\n            \"rollencodenummer\": \"9904446000007\",\n            \"versionStruktur\": \"1\",\n            \"weiterverpflichtet\": true\n          }\n        ],\n        \"sparte\": \"STROM\",\n        \"statusErzeugendeMalo\": \"GEFOERDERTE_DIREKTVERMARKTUNG\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"MESSLOKATION\": [\n      {\n        \"boTyp\": \"MESSLOKATION\",\n        \"datenqualitaet\": \"INFORMATIVE_DATEN\",\n        \"marktrollen\": [\n          {\n            \"boTyp\": \"MARKTTEILNEHMER\",\n            \"marktrolle\": \"MSB\",\n            \"messstellenbetreiberEigenschaft\": \"GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER\",\n            \"rollencodenummer\": \"9904446000007\",\n            \"versionStruktur\": \"1\",\n            \"weiterverpflichtet\": true\n          },\n          {\n            \"boTyp\": \"MARKTTEILNEHMER\",\n            \"marktrolle\": \"GMSB\",\n            \"rollencodenummer\": \"9904446000007\",\n            \"versionStruktur\": \"1\"\n          }\n        ],\n        \"messlokationsId\": \"DE0032106765712000000000000000037\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"NETZNUTZUNGSVERTRAG\": [\n      {\n        \"boTyp\": \"VERTRAG\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\",\n        \"vertragsart\": \"NETZNUTZUNGSVERTRAG\",\n        \"vertragsbeginn\": \"2025-06-30T22:00:00Z\",\n        \"vertragsende\": \"2025-07-31T22:00:00Z\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9900321000005\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"anfragereferenznummer\": \"ABC123456\",\n    \"datenaustauschreferenz\": \"LZ1WFAML\",\n    \"dokumentennummer\": \"BGMLZRDFFEI\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9903790000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"E01\",\n    \"nachrichtendatum\": \"2025-04-04T12:00:00Z\",\n    \"nachrichtenreferenznummer\": \"UNHLZ8FI7XO\",\n    \"pruefidentifikator\": \"55607\",\n    \"sparte\": \"STROM\",\n    \"transaktionsgrund\": \"E03\",\n    \"transaktionsgrundergaenzung\": \"ZW8\",\n    \"transaktionsgrundergaenzungBefristeteAnmeldung\": \"E03\",\n    \"vertragsbeginn\": \"2025-06-30T22:00:00Z\",\n    \"vertragsende\": \"2025-07-31T22:00:00Z\",\n    \"vorgangsnummer\": \"12345\"\n  }\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend fort, nachdem die Nachricht erstellt ist.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="2" anker="schritt-2" richtung="eingehend" kopf={{"links": {"label": "NB", "eigen": true}, "rechts": {"label": "LFN"}}}>

### Antwort auf Ankündigung der Zuordnung des LFN zur Marktlokation

<Schrittskizze sicht={{"label": "NB"}} zeilen={[{"art": "empfangen", "label": "LFN", "weg": "AS4", "nachrichten": [{"nr": "55608", "titel": "Bestätigung Zuordnung des LF zur MaLo/ Tranche"}, {"nr": "55609", "titel": "Ablehnung Zuordnung des LF zur MaLo/ Tranche"}]}, {"art": "aperak", "werte": ["Z33"]}, {"art": "erstellen"}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55608](/schnittstellen/202604/pruefi/UTILMD/PI_55608) — Bestätigung Zuordnung des LF zur MaLo/ Tranche · AS4
- [55609](/schnittstellen/202604/pruefi/UTILMD/PI_55609) — Ablehnung Zuordnung des LF zur MaLo/ Tranche · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **LFN** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `55608`, `55609` → [E_0605](/referenz/202604/ebd/E_0605) · LF · Zuordnung prüfen

</div>

</li>

<li data-teil="aperak">

**Aperak-Prüfungen**
- `55608`, `55609` → `Z33`

</li>

<li data-teil="schnittstelle" data-art="schreiben">

**Schreibende Schnittstelle**
- Vorgang angelegt — [Prozessdaten erstellen](/api/202604/backend-schreiben-nb/createprocessdata#prozessdaten-erstellen) `POST /createProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/createProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "ERSTELLEN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"MARKTLOKATION\": [\n      {\n        \"boTyp\": \"MARKTLOKATION\",\n        \"erforderlichesProduktpaket\": [\n          {\n            \"priorisierung\": \"PRIORITAET1\",\n            \"produkt\": [\n              {\n                \"produktCode\": \"9991000002082\",\n                \"wertedetails\": \"11XBKA---------I\"\n              }\n            ],\n            \"produktpaketId\": 1,\n            \"umsetzungsgradvorgabe\": \"ZUORDNUNG_AUCH_WENN_PRODUKTPAKET_NICHT_UMSETZBAR\"\n          },\n          {\n            \"priorisierung\": \"PRIORITAET2\",\n            \"produkt\": [\n              {\n                \"produktCode\": \"9991000002082\",\n                \"wertedetails\": \"11XBKA--------II\"\n              }\n            ],\n            \"produktpaketId\": 2,\n            \"umsetzungsgradvorgabe\": \"ZUORDNUNG_AUCH_WENN_PRODUKTPAKET_NICHT_UMSETZBAR\"\n          }\n        ],\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"NETZNUTZUNGSVERTRAG\": [\n      {\n        \"boTyp\": \"VERTRAG\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\",\n        \"vertragsart\": \"NETZNUTZUNGSVERTRAG\",\n        \"vertragsbeginn\": \"2025-06-30T22:00:00Z\",\n        \"vertragsende\": \"2025-08-31T22:00:00Z\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"ansprechpartner\": {\n        \"boTyp\": \"ANSPRECHPARTNER\",\n        \"nachname\": \"P GETTY\",\n        \"rufnummern\": [\n          {\n            \"nummerntyp\": \"RUF_DURCHWAHL\",\n            \"rufnummer\": \"+3222271020\"\n          }\n        ],\n        \"versionStruktur\": \"1\"\n      },\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9903729000007\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"anfragereferenznummer\": \"ANMPI55607\",\n    \"antwortstatus\": \"A01\",\n    \"antwortstatusCodeliste\": \"E_0603\",\n    \"datenaustauschreferenz\": \"DATVPDPWLQIOEX\",\n    \"dokumentennummer\": \"DA602410171124559903323000007476821\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9900327000009\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"E01\",\n    \"nachrichtendatum\": \"2025-06-05T12:31:00Z\",\n    \"nachrichtenreferenznummer\": \"DARHJQXMUFOZIJ\",\n    \"pruefidentifikator\": \"55608\",\n    \"sparte\": \"STROM\",\n    \"transaktionsgrund\": \"E03\",\n    \"transaktionsgrundergaenzung\": \"ZW8\",\n    \"transaktionsgrundergaenzungBefristeteAnmeldung\": \"E03\",\n    \"vertragsbeginn\": \"2025-06-30T22:00:00Z\",\n    \"vertragsende\": \"2025-08-31T22:00:00Z\",\n    \"vorgangsnummer\": \"24062416225400000000000102159662011\"\n  },\n  \"zusatzdaten\": {}\n}"} examples={[{"mediaType": "application/json", "examples": [{"name": "55608", "summary": "55608 — Bestätigung Zuordnung des LF zur MaLo/ Tranche", "value": {"stammdaten": {"MARKTLOKATION": [{"boTyp": "MARKTLOKATION", "versionStruktur": "1", "sparte": "STROM", "erforderlichesProduktpaket": [{"produktpaketId": 1, "produkt": [{"produktCode": "9991000002082", "wertedetails": "11XBKA---------I"}], "umsetzungsgradvorgabe": "ZUORDNUNG_AUCH_WENN_PRODUKTPAKET_NICHT_UMSETZBAR", "priorisierung": "PRIORITAET1"}, {"produktpaketId": 2, "produkt": [{"produktCode": "9991000002082", "wertedetails": "11XBKA--------II"}], "umsetzungsgradvorgabe": "ZUORDNUNG_AUCH_WENN_PRODUKTPAKET_NICHT_UMSETZBAR", "priorisierung": "PRIORITAET2"}]}], "NETZNUTZUNGSVERTRAG": [{"boTyp": "VERTRAG", "versionStruktur": "1", "vertragsart": "NETZNUTZUNGSVERTRAG", "sparte": "STROM", "vertragsbeginn": "2025-06-30T22:00:00Z", "vertragsende": "2025-08-31T22:00:00Z"}]}, "transaktionsdaten": {"datenaustauschreferenz": "DATVPDPWLQIOEX", "sparte": "STROM", "transaktionsgrund": "E03", "transaktionsgrundergaenzung": "ZW8", "transaktionsgrundergaenzungBefristeteAnmeldung": "E03", "vorgangsnummer": "24062416225400000000000102159662011", "pruefidentifikator": "55608", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9903729000007", "rollencodetyp": "BDEW", "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "nachname": "P GETTY", "rufnummern": [{"nummerntyp": "RUF_DURCHWAHL", "rufnummer": "+3222271020"}]}}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900327000009", "rollencodetyp": "BDEW"}, "dokumentennummer": "DA602410171124559903323000007476821", "kategorie": "E01", "nachrichtendatum": "2025-06-05T12:31:00Z", "nachrichtenreferenznummer": "DARHJQXMUFOZIJ", "anfragereferenznummer": "ANMPI55607", "antwortstatus": "A01", "antwortstatusCodeliste": "E_0603", "vertragsbeginn": "2025-06-30T22:00:00Z", "vertragsende": "2025-08-31T22:00:00Z"}, "zusatzdaten": {}}}, {"name": "55609", "summary": "55609 — Ablehnung Zuordnung des LF zur MaLo/ Tranche", "value": {"stammdaten": {}, "transaktionsdaten": {"datenaustauschreferenz": "LZO4M6BS", "sparte": "STROM", "transaktionsgrund": "E01", "transaktionsgrundergaenzung": "ZW8", "vorgangsnummer": "12345", "pruefidentifikator": "55609", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9903790000002", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900321000005", "rollencodetyp": "BDEW"}, "dokumentennummer": "BGMLZOX29W6", "kategorie": "E01", "nachrichtendatum": "2025-06-05T12:00:00Z", "nachrichtenreferenznummer": "UNHLZXXPU0O", "anfragereferenznummer": "ABC123456", "antwortstatus": "A99", "antwortstatusCodeliste": "E_0603", "freitext": "Bla"}, "zusatzdaten": {}}}]}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Legt im Backend einen neuen Vorgang mit den Daten der eingegangenen Nachricht an.

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202604/backend-schreiben-nb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"MARKTLOKATION\": [\n      {\n        \"boTyp\": \"MARKTLOKATION\",\n        \"erforderlichesProduktpaket\": [\n          {\n            \"priorisierung\": \"PRIORITAET1\",\n            \"produkt\": [\n              {\n                \"produktCode\": \"9991000002082\",\n                \"wertedetails\": \"11XBKA---------I\"\n              }\n            ],\n            \"produktpaketId\": 1,\n            \"umsetzungsgradvorgabe\": \"ZUORDNUNG_AUCH_WENN_PRODUKTPAKET_NICHT_UMSETZBAR\"\n          },\n          {\n            \"priorisierung\": \"PRIORITAET2\",\n            \"produkt\": [\n              {\n                \"produktCode\": \"9991000002082\",\n                \"wertedetails\": \"11XBKA--------II\"\n              }\n            ],\n            \"produktpaketId\": 2,\n            \"umsetzungsgradvorgabe\": \"ZUORDNUNG_AUCH_WENN_PRODUKTPAKET_NICHT_UMSETZBAR\"\n          }\n        ],\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"NETZNUTZUNGSVERTRAG\": [\n      {\n        \"boTyp\": \"VERTRAG\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\",\n        \"vertragsart\": \"NETZNUTZUNGSVERTRAG\",\n        \"vertragsbeginn\": \"2025-06-30T22:00:00Z\",\n        \"vertragsende\": \"2025-08-31T22:00:00Z\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"ansprechpartner\": {\n        \"boTyp\": \"ANSPRECHPARTNER\",\n        \"nachname\": \"P GETTY\",\n        \"rufnummern\": [\n          {\n            \"nummerntyp\": \"RUF_DURCHWAHL\",\n            \"rufnummer\": \"+3222271020\"\n          }\n        ],\n        \"versionStruktur\": \"1\"\n      },\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9903729000007\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"anfragereferenznummer\": \"ANMPI55607\",\n    \"antwortstatus\": \"A01\",\n    \"antwortstatusCodeliste\": \"E_0603\",\n    \"datenaustauschreferenz\": \"DATVPDPWLQIOEX\",\n    \"dokumentennummer\": \"DA602410171124559903323000007476821\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9900327000009\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"E01\",\n    \"nachrichtendatum\": \"2025-06-05T12:31:00Z\",\n    \"nachrichtenreferenznummer\": \"DARHJQXMUFOZIJ\",\n    \"pruefidentifikator\": \"55608\",\n    \"sparte\": \"STROM\",\n    \"transaktionsgrund\": \"E03\",\n    \"transaktionsgrundergaenzung\": \"ZW8\",\n    \"transaktionsgrundergaenzungBefristeteAnmeldung\": \"E03\",\n    \"vertragsbeginn\": \"2025-06-30T22:00:00Z\",\n    \"vertragsende\": \"2025-08-31T22:00:00Z\",\n    \"vorgangsnummer\": \"24062416225400000000000102159662011\"\n  },\n  \"zusatzdaten\": {}\n}"} examples={[{"mediaType": "application/json", "examples": [{"name": "55608", "summary": "55608 — Bestätigung Zuordnung des LF zur MaLo/ Tranche", "value": {"stammdaten": {"MARKTLOKATION": [{"boTyp": "MARKTLOKATION", "versionStruktur": "1", "sparte": "STROM", "erforderlichesProduktpaket": [{"produktpaketId": 1, "produkt": [{"produktCode": "9991000002082", "wertedetails": "11XBKA---------I"}], "umsetzungsgradvorgabe": "ZUORDNUNG_AUCH_WENN_PRODUKTPAKET_NICHT_UMSETZBAR", "priorisierung": "PRIORITAET1"}, {"produktpaketId": 2, "produkt": [{"produktCode": "9991000002082", "wertedetails": "11XBKA--------II"}], "umsetzungsgradvorgabe": "ZUORDNUNG_AUCH_WENN_PRODUKTPAKET_NICHT_UMSETZBAR", "priorisierung": "PRIORITAET2"}]}], "NETZNUTZUNGSVERTRAG": [{"boTyp": "VERTRAG", "versionStruktur": "1", "vertragsart": "NETZNUTZUNGSVERTRAG", "sparte": "STROM", "vertragsbeginn": "2025-06-30T22:00:00Z", "vertragsende": "2025-08-31T22:00:00Z"}]}, "transaktionsdaten": {"datenaustauschreferenz": "DATVPDPWLQIOEX", "sparte": "STROM", "transaktionsgrund": "E03", "transaktionsgrundergaenzung": "ZW8", "transaktionsgrundergaenzungBefristeteAnmeldung": "E03", "vorgangsnummer": "24062416225400000000000102159662011", "pruefidentifikator": "55608", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9903729000007", "rollencodetyp": "BDEW", "ansprechpartner": {"boTyp": "ANSPRECHPARTNER", "versionStruktur": "1", "nachname": "P GETTY", "rufnummern": [{"nummerntyp": "RUF_DURCHWAHL", "rufnummer": "+3222271020"}]}}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900327000009", "rollencodetyp": "BDEW"}, "dokumentennummer": "DA602410171124559903323000007476821", "kategorie": "E01", "nachrichtendatum": "2025-06-05T12:31:00Z", "nachrichtenreferenznummer": "DARHJQXMUFOZIJ", "anfragereferenznummer": "ANMPI55607", "antwortstatus": "A01", "antwortstatusCodeliste": "E_0603", "vertragsbeginn": "2025-06-30T22:00:00Z", "vertragsende": "2025-08-31T22:00:00Z"}, "zusatzdaten": {}}}, {"name": "55609", "summary": "55609 — Ablehnung Zuordnung des LF zur MaLo/ Tranche", "value": {"stammdaten": {}, "transaktionsdaten": {"datenaustauschreferenz": "LZO4M6BS", "sparte": "STROM", "transaktionsgrund": "E01", "transaktionsgrundergaenzung": "ZW8", "vorgangsnummer": "12345", "pruefidentifikator": "55609", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9903790000002", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "gewerbekennzeichnung": true, "rollencodenummer": "9900321000005", "rollencodetyp": "BDEW"}, "dokumentennummer": "BGMLZOX29W6", "kategorie": "E01", "nachrichtendatum": "2025-06-05T12:00:00Z", "nachrichtenreferenznummer": "UNHLZXXPU0O", "anfragereferenznummer": "ABC123456", "antwortstatus": "A99", "antwortstatusCodeliste": "E_0603", "freitext": "Bla"}, "zusatzdaten": {}}}]}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend mit den Daten der eingegangenen Nachricht fort.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="3" anker="schritt-3" richtung="ausgehend" kopf={{"links": {"label": "NB", "eigen": true}, "rechts": {"label": "LFN"}}}>

### Zuordnung des LFN zur Marktlokation aufgrund fehlender Antwort

<Schrittskizze sicht={{"label": "NB"}} zeilen={[{"art": "ausloeser", "werte": ["START_ZUORDNUNG_ERZ_MALO_TRANCHE"]}, {"art": "senden", "label": "LFN", "weg": "AS4", "nachrichten": [{"nr": "55607", "titel": "Ankündigung Zuordnung / Zuordnung des LF zur MaLo/ Tranche"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55607](/schnittstellen/202604/pruefi/UTILMD/PI_55607) — Ankündigung Zuordnung / Zuordnung des LF zur MaLo/ Tranche · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="ausloeser">

**Prozessauslöser** [`START_ZUORDNUNG_ERZ_MALO_TRANCHE`](/schnittstellen/202604/trigger/events/NB-START_ZUORDNUNG_ERZ_MALO_TRANCHE) · [Im Playground ausprobieren](/api/202604/ausloeser-nb/start-zuordnung-erz-malo-tranche)

Das Backend stößt diesen Schritt mit diesem Ereignis an.

</li>

<li data-teil="nachricht">

Nachricht an **LFN** · AS4

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202604/backend-schreiben-nb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"MARKTLOKATION\": [\n      {\n        \"boTyp\": \"MARKTLOKATION\",\n        \"datenqualitaet\": \"INFORMATIVE_DATEN\",\n        \"energieherkunft\": [\n          {\n            \"erzeugungsart\": \"EEG_DV\"\n          }\n        ],\n        \"marktlokationsId\": \"50074561188\",\n        \"marktrollen\": [\n          {\n            \"boTyp\": \"MARKTTEILNEHMER\",\n            \"marktrolle\": \"MSB\",\n            \"messstellenbetreiberEigenschaft\": \"GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER\",\n            \"rollencodenummer\": \"9904446000007\",\n            \"versionStruktur\": \"1\",\n            \"weiterverpflichtet\": true\n          }\n        ],\n        \"sparte\": \"STROM\",\n        \"statusErzeugendeMalo\": \"GEFOERDERTE_DIREKTVERMARKTUNG\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"MESSLOKATION\": [\n      {\n        \"boTyp\": \"MESSLOKATION\",\n        \"datenqualitaet\": \"INFORMATIVE_DATEN\",\n        \"marktrollen\": [\n          {\n            \"boTyp\": \"MARKTTEILNEHMER\",\n            \"marktrolle\": \"MSB\",\n            \"messstellenbetreiberEigenschaft\": \"GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER\",\n            \"rollencodenummer\": \"9904446000007\",\n            \"versionStruktur\": \"1\",\n            \"weiterverpflichtet\": true\n          },\n          {\n            \"boTyp\": \"MARKTTEILNEHMER\",\n            \"marktrolle\": \"GMSB\",\n            \"rollencodenummer\": \"9904446000007\",\n            \"versionStruktur\": \"1\"\n          }\n        ],\n        \"messlokationsId\": \"DE0032106765712000000000000000037\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"NETZNUTZUNGSVERTRAG\": [\n      {\n        \"boTyp\": \"VERTRAG\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\",\n        \"vertragsart\": \"NETZNUTZUNGSVERTRAG\",\n        \"vertragsbeginn\": \"2025-06-30T22:00:00Z\",\n        \"vertragsende\": \"2025-07-31T22:00:00Z\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9900321000005\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"anfragereferenznummer\": \"ABC123456\",\n    \"datenaustauschreferenz\": \"LZ1WFAML\",\n    \"dokumentennummer\": \"BGMLZRDFFEI\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9903790000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"E01\",\n    \"nachrichtendatum\": \"2025-04-04T12:00:00Z\",\n    \"nachrichtenreferenznummer\": \"UNHLZ8FI7XO\",\n    \"pruefidentifikator\": \"55607\",\n    \"sparte\": \"STROM\",\n    \"transaktionsgrund\": \"E03\",\n    \"transaktionsgrundergaenzung\": \"ZW8\",\n    \"transaktionsgrundergaenzungBefristeteAnmeldung\": \"E03\",\n    \"vertragsbeginn\": \"2025-06-30T22:00:00Z\",\n    \"vertragsende\": \"2025-07-31T22:00:00Z\",\n    \"vorgangsnummer\": \"12345\"\n  }\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend fort, nachdem die Nachricht erstellt ist.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="8" anker="schritt-8" richtung="ausgehend" kopf={{"links": {"label": "NB", "eigen": true}, "rechts": {"label": "LFA"}}}>

### Beendigung der Zuordnung des LFA zur Tranche

<Schrittskizze sicht={{"label": "NB"}} zeilen={[{"art": "folge_ausloeser", "werte": ["55001", "55011"]}, {"art": "ausloeser", "werte": ["START_ENDE_ZUORDNUNG"]}, {"art": "senden", "label": "LFA", "weg": "AS4", "nachrichten": [{"nr": "55037", "titel": "Beendigung der Zuordnung"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55037](/schnittstellen/202604/pruefi/UTILMD/PI_55037) — Beendigung der Zuordnung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="folge_ausloeser">

**Ausgelöst durch Eingang**
- [55001](/schnittstellen/202604/pruefi/UTILMD/PI_55001)
- [55011](/schnittstellen/202604/pruefi/UTILMD/PI_55011)

Die MACO APP sendet diese Nachricht selbst, als Folgeprozess nach einem dieser Eingänge. Daneben kann das Backend diesen Schritt mit einem Ereignis anstoßen — der nächste Punkt.

</li>

<li data-teil="ausloeser">

**Prozessauslöser** [`START_ENDE_ZUORDNUNG`](/schnittstellen/202604/trigger/events/NB-START_ENDE_ZUORDNUNG) · [Im Playground ausprobieren](/api/202604/ausloeser-nb/start-ende-zuordnung)

Das Backend stößt diesen Schritt mit diesem Ereignis an.

</li>

<li data-teil="nachricht">

Nachricht an **LFA** · AS4

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202604/backend-schreiben-nb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"MARKTLOKATION\": [\n      {\n        \"boTyp\": \"MARKTLOKATION\",\n        \"marktlokationsId\": \"10017211334\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"NETZNUTZUNGSVERTRAG\": [\n      {\n        \"boTyp\": \"VERTRAG\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\",\n        \"vertragsart\": \"NETZNUTZUNGSVERTRAG\",\n        \"vertragsende\": \"2025-04-30T22:00:00Z\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9900321000005\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"datenaustauschreferenz\": \"002001528776\",\n    \"dokumentennummer\": \"002001528776\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9903790000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"E02\",\n    \"nachrichtendatum\": \"2024-04-01T22:01:00Z\",\n    \"nachrichtenreferenznummer\": \"002001528776\",\n    \"pruefidentifikator\": \"55037\",\n    \"sparte\": \"STROM\",\n    \"transaktionsgrund\": \"ZC8\",\n    \"transaktionsgrundergaenzung\": \"ZW4\",\n    \"vertragsende\": \"2025-04-30T22:00:00Z\",\n    \"vorgangsnummer\": \"051MlNQB7jwRfnYJzb71SW\"\n  }\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

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
| [E_0605](/referenz/202604/ebd/E_0605) | Zuordnung prüfen |

</details>

<a id="abschnitt-informationen"></a>

## Prozess-Informationen

Wortlaut der Lesefassung, Steckbrief Kap. 2.4.2.1, S. 38–40.

<Stepper>
<ol>

<li data-blatt="vorbedingungen">

### Vorbedingungen

- Es handelt sich um eine erzeugende Marktlokation bzw. eine Tranche.
- Die Energie einer Marktlokation, die vollständig oder anteilig zur Veräußerungsform einer DV zugeordnet werden soll, ist mit einer viertelstündlichen Auflösung zu messen.
- Eine Zuordnungsermächtigung nach den Prozessen der MaBiS für den vom LFN genutzten BK liegt beim NB vor.

</li>

<li data-blatt="ergebnisse">

### Ergebnisse

- Der NB versendet die Berechnungsformel an den LFN.
- Der NB führt den Use-Case „[Abrechnungsdaten Bilanzkreisabrechnung](/prozessdoku/202604/NB/GPKE-Teil2-abrechnungsdaten-bilanzkreisabrechnung)“ aus.
- Der NB führt den Use-Case „Stammdatenänderung“ (hier: SD „[Stammdatenänderung vom NB (verantwortlich) ausgehend](/prozessdoku/202604/NB/GPKE-Teil4-stammdatenaenderung-vom-nb-verantwortlich-ausgehend)“) (GPKE Teil 4) durch.
- Der NB führt den Use-Case „[Einrichtung der Konfigurationen aufgrund einer Zuordnung eines LF zu einer Marktlokation bzw. Tranche](/prozessdoku/202604/NB/GPKE-Teil3-einrichtung-der-konfigurationen-aufgrund-einer-zuordnung-eines-lf-zu-einer-marktlokation-bzw-tranche)“ (GPKE Teil 3) aus.
- Der LF führt den Use-Case „Stammdatenänderung“ (hier: SD „[Stammdatenänderung vom LF (verantwortlich) ausgehend](/prozessdoku/202604/NB/GPKE-Teil4-stammdatenaenderung-vom-lf-verantwortlich-ausgehend)“) (GPKE Teil 4) durch.

</li>

<li data-blatt="fehlerfall">

### Fehlerfall

#### Ergebnis im Fehlerfall

- Der NB muss sicherstellen, dass die von der Marktlokation erzeugte Energie einem BK zugeordnet ist oder
- der NB muss die Unterbrechung der Anschlussnutzung an der Marktlokation durchführen.
- Der LFN wurde der Marktlokation bzw. Tranche nicht zugeordnet. Im Fall einer tranchierten Marktlokation ist nicht jede Tranche einem LF zugeordnet.

#### Fehlerfälle

- Es handelt sich um eine verbrauchende Marktlokation.
- Die Energie einer Marktlokation, die vollständig oder anteilig zur Veräußerungsform einer DV zugeordnet werden soll, ist nicht mit einer viertelstündlichen Auflösung messbar.
- Eine Zuordnungsermächtigung nach den Prozessen der MaBiS für den vom LFN genutzten BK liegt beim NB nicht vor.

</li>

<li data-blatt="anforderungen">

### Weitere Anforderungen

- Bei einer KWKG-Marktlokation mit DV-Pflicht bzw. Nicht-EEG-/Nicht-KWKG-Marktlokation kann im Rahmen der bilateralen Klärung auch die Unterbrechung der Anschlussnutzung an der Marktlokation durch den NB in Betracht gezogen werden. Eine Pflicht des NB zur kaufmännischen Abnahme der elektrischen Energie besteht nicht.
- Im Fall das LFZ der Marktlokation bzw. Tranche zugeordnet sind, gilt: Das Zuordnungsende des LFN wird von dem Zuordnungsbeginn des LFZ bestimmt, dessen Zuordnungsbeginn dem Zuordnungsbeginn des LFN zeitlich am nächsten liegt und dessen Anteil (hier: 1 bis 100 %) der Energiemenge der erzeugenden Marktlokation von dem Anteil des LFN betroffen ist. Das Zuordnungsende des LFN entspricht in diesem Fall dem Zuordnungsbeginn dieses LFZ.

</li>

<li data-blatt="anlass">

### Anlass

- Bei einer EEG-Marktlokation ohne DV-Pflicht bzw. KWKG-Marktlokation ohne DV-Pflicht bzw. EEG-Marktlokation mit DV-Pflicht ergibt sich:
  - Der nicht-tranchierten Marktlokation ist kein LF zugeordnet oder
  - die Tranchen einer Marktlokation sind in Summe nicht genau 100% LF zugeordnet.
- Bei einer KWKG-Marktlokation mit DV-Pflicht bzw. einer Nicht-EEG-/Nicht-KWKG-Marktlokation ergibt sich:
  - Der nicht-tranchierten Marktlokation ist kein LF zugeordnet oder
  - die Tranchen einer Marktlokation sind in Summe nicht genau 100% LF zugeordnet und die bilaterale Klärung des NB mit dem EZ ergibt, dass der NB
  - die (tranchierte oder nicht-tranchierte) Marktlokation nicht-tranchiert abbildet oder
  - die (tranchierte oder nicht-tranchierte) Marktlokation tranchiert abbildet. Gründe können insbesondere sein:
- Beendigung der Zuordnung des LF zur Marktlokation bzw. Tranche aufgrund
  - Abmeldung der Zuordnung des LF zur Marklokation bzw. Tranche wegen Kündigung des Stromabnahmevertrags; ohne Folgebelieferung
  - Information über die erfolgte Kündigung des Bilanzkreisvertrags durch den ÜNB
  - Erlöschen der durch den BKV gegenüber dem LF erteilten Zuordnungsermächtigung
  - geändertem Zeitreihentyp und keiner gültigen Zuordnungsermächtigung für den neuen Zeitreihentyp
- erstmalige Inbetriebnahme einer Marktlokation (Neuanlage)

</li>

<li data-blatt="erste-nachricht">

### Erste Nachricht

Der Beteiligte dieser Seite sendet selbst: „Ankündigung der Zuordnung des LFN zur Marktlokation“ an **LFN** (Schritt 1).

</li>

<li data-blatt="ziel">

### Ziel

Der LFN ist der Marktlokation bzw. Tranche zugeordnet. Im Fall einer tranchierten Marktlokation ist jede Tranche einem LF zugeordnet.

</li>

</ol>
</Stepper>

<a id="abschnitt-sichten"></a>

## Andere Sichten des Prozesses

Derselbe Prozess, aus den Augen der anderen Beteiligten: dieselben Schritte, jeweils aus deren Sicht gelesen.

- [Sicht LFA](/prozessdoku/202604/LF--LFA/GPKE-Teil2-fall-3-lf-zuordnung-bei-kwkg-marktlokation-mit-dv-pflicht-bzw-nicht-eeg-nicht-kwkg-marktlokation-und-marktlokation-wird-nicht-tranchiert-abgebildet) — der abgebende Lieferant · Marktrolle LF
- [Sicht LFN](/prozessdoku/202604/LF--LFN/GPKE-Teil2-fall-3-lf-zuordnung-bei-kwkg-marktlokation-mit-dv-pflicht-bzw-nicht-eeg-nicht-kwkg-marktlokation-und-marktlokation-wird-nicht-tranchiert-abgebildet) — der aufnehmende Lieferant · Marktrolle LF

<Hinweisbereich>

*Die Schritte sind die **möglichen** Nachrichten dieses Prozesses, keine Abfolge — die Quelle führt weder Bedingungen noch Alternativen. Das Kästchen am Schritt nennt links die eigene Sicht: **←** empfängt sie, **→** sendet sie. Zugeklappte Schritte laufen zwischen anderen Marktpartnern. Die Nummern sind die der Quelle; wo eine fehlt, fehlt sie dort.*

</Hinweisbereich>
