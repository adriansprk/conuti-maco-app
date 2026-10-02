# Bestellung einer Änderung von Abrechnungsdaten zur Bilanzkreisabrechnung von ÜNB an NB — Sicht NB

<Kopf rolle="NB" beteiligter="NB" festlegung="GPKE" dokument="GPKE Teil 2" kapitel="3.1.3.3" sparte="Strom" schritte={2} suchtitel="Bestellung einer Änderung von Abrechnungsdaten zur Bilanzkreisabrechnung von ÜNB an NB — Sicht NB · GPKE Teil 2 · Formatversion 202604" abschnitte={[{"id": "abschnitt-ablauf", "label": "Prozessablauf"}, {"id": "abschnitt-schritte", "label": "Prozessschritte"}, {"id": "abschnitt-informationen", "label": "Prozess-Informationen"}, {"id": "abschnitt-sichten", "label": "Andere Sichten des Prozesses"}]} />

<Kurzfassung>

Der LF bzw. ÜNB übermittelt dem NB die Bestellung einer Änderung von Abrechnungsdaten. Der NB prüft die Bestellung und teilt dem LF bzw. ÜNB den Bearbeitungsstand mit.

</Kurzfassung>

<a id="abschnitt-ablauf"></a>

## Prozessablauf aus Sicht des NB

<Systembild svg={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1004 1022\" width=\"1004\" height=\"1022\" role=\"img\" aria-labelledby=\"sb-title\" class=\"maco-systembild\">\n<title id=\"sb-title\">Systembild: Bestellung einer Änderung von Abrechnungsdaten zur Bilanzkreisabrechnung von ÜNB an NB aus Sicht NB</title>\n<defs><marker id=\"sb-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect class=\"sb-lane-kopf\" x=\"16\" y=\"12\" width=\"232\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend-System des Kunden</text>\n<rect class=\"sb-lane-kopf\" x=\"398\" y=\"12\" width=\"264\" height=\"46\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · NB</text>\n<rect class=\"sb-lane-kopf\" x=\"812\" y=\"12\" width=\"176\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"900\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Marktpartner</text>\n<line x1=\"323\" y1=\"58\" x2=\"323\" y2=\"1010\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"737\" y1=\"58\" x2=\"737\" y2=\"1010\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"80\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">1. Bestellung einer Änderung</text>\n<text x=\"530\" y=\"115\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">von Abrechnungsdaten zur</text>\n<text x=\"530\" y=\"130\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Bilanzkr…</text>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"93\" r=\"5\"/><line x1=\"900\" y1=\"98\" x2=\"900\" y2=\"110\"/><line x1=\"893\" y1=\"102\" x2=\"907\" y2=\"102\"/><line x1=\"900\" y1=\"110\" x2=\"894\" y2=\"120\"/><line x1=\"900\" y1=\"110\" x2=\"906\" y2=\"120\"/></g>\n<text x=\"900\" y=\"142\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">ÜNB</text>\n<line x1=\"878\" y1=\"111\" x2=\"628\" y2=\"111\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"103\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"127\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">55614, 55675</text>\n<rect class=\"sb-kasten sb-aperak_lesen\" x=\"432\" y=\"169\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"189\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Daten für die</text>\n<text x=\"530\" y=\"204\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Eingangsprüfung laden</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"143\" x2=\"530\" y2=\"169\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-aperak_lesen\" x=\"34\" y=\"177\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"197\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Marktlokation lesen</text>\n<line x1=\"432\" y1=\"193\" x2=\"230\" y2=\"193\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"185\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-aperak\" x=\"432\" y=\"243\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"263\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Aperak prüfen: Z10, Z16,</text>\n<text x=\"530\" y=\"278\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Z43, Z33</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"217\" x2=\"530\" y2=\"243\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-schreiben\" x=\"432\" y=\"317\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"337\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"291\" x2=\"530\" y2=\"317\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-schreiben\" x=\"34\" y=\"317\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"337\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten erstellen</text>\n<line x1=\"432\" y1=\"333\" x2=\"230\" y2=\"333\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"325\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"381\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"401\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"350\" x2=\"530\" y2=\"381\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"381\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"401\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"397\" x2=\"230\" y2=\"397\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"389\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<text x=\"331\" y=\"413\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">PI 55614</text>\n<rect class=\"sb-kasten sb-ebd\" x=\"432\" y=\"445\" width=\"196\" height=\"168\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"465\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">EBD prüfen: E_0618, E_0613</text>\n<text x=\"530\" y=\"480\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label-2, #424245)\">E_0618 — Rückmeldung</text>\n<text x=\"530\" y=\"495\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label-2, #424245)\">verarbeiten (Basiert auf EBD:</text>\n<text x=\"530\" y=\"510\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label-2, #424245)\">E_0626_Rückmeldung auf</text>\n<text x=\"530\" y=\"525\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label-2, #424245)\">Änderung prüfen)</text>\n<text x=\"530\" y=\"540\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label-2, #424245)\">E_0613 — Bestellung prüfen</text>\n<text x=\"530\" y=\"555\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label-2, #424245)\">(Basiert auf EBD:</text>\n<text x=\"530\" y=\"570\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label-2, #424245)\">E_0573_Bestellung zur</text>\n<text x=\"530\" y=\"585\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label-2, #424245)\">Stammdatenänderung</text>\n<text x=\"530\" y=\"600\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label-2, #424245)\">prüfen)</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"414\" x2=\"530\" y2=\"445\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-folgeprozess\" x=\"432\" y=\"639\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"659\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Folgeprozess auslösen:</text>\n<text x=\"530\" y=\"674\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">21047</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"613\" x2=\"530\" y2=\"639\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-folge_ausloeser\" x=\"432\" y=\"713\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"733\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Ausgelöst durch Eingang:</text>\n<text x=\"530\" y=\"748\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">55614</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"687\" x2=\"530\" y2=\"713\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-trigger\" x=\"432\" y=\"787\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"807\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessauslöser empfangen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"761\" x2=\"530\" y2=\"787\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-trigger\" x=\"34\" y=\"787\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"807\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">2 Ereignisse, alternativ</text>\n<line x1=\"230\" y1=\"803\" x2=\"432\" y2=\"803\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"795\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"851\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"871\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">2. Bearbeitungsstand zur</text>\n<text x=\"530\" y=\"886\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Bestellung</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"820\" x2=\"530\" y2=\"851\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"857\" r=\"5\"/><line x1=\"900\" y1=\"862\" x2=\"900\" y2=\"874\"/><line x1=\"893\" y1=\"866\" x2=\"907\" y2=\"866\"/><line x1=\"900\" y1=\"874\" x2=\"894\" y2=\"884\"/><line x1=\"900\" y1=\"874\" x2=\"906\" y2=\"884\"/></g>\n<text x=\"900\" y=\"906\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">ÜNB</text>\n<line x1=\"628\" y1=\"875\" x2=\"878\" y2=\"875\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"867\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"891\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">21047</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"934\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"954\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"899\" x2=\"530\" y2=\"934\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"934\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"954\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"950\" x2=\"230\" y2=\"950\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"942\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n</svg>"} gesamt={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 730 486\" width=\"730\" height=\"486\" role=\"img\" aria-labelledby=\"sd-title\" class=\"maco-sequence\">\n<title id=\"sd-title\">Sequenzdiagramm: Bestellung einer Änderung von Abrechnungsdaten zur Bilanzkreisabrechnung von ÜNB an NB aus Sicht NB</title>\n<defs><marker id=\"sd-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect x=\"16\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"121\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend (Kunde)</text>\n<line x1=\"121\" y1=\"64\" x2=\"121\" y2=\"474\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"260\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"365\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · NB</text>\n<line x1=\"365\" y1=\"64\" x2=\"365\" y2=\"474\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"504\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"609\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">ÜNB</text>\n<line x1=\"609\" y1=\"64\" x2=\"609\" y2=\"474\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"609\" y1=\"90\" x2=\"365\" y2=\"90\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"81\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">1. Bestellung einer Änderung von Abrechnungsdate…</text>\n<text x=\"487\" y=\"105\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55614, 55675</text>\n<line x1=\"365\" y1=\"152\" x2=\"121\" y2=\"152\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"143\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<text x=\"243\" y=\"167\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten erstellen</text>\n<line x1=\"365\" y1=\"214\" x2=\"121\" y2=\"214\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"205\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"229\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren · PI 55614</text>\n<line x1=\"121\" y1=\"276\" x2=\"365\" y2=\"276\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"267\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">2 Ereignisse, alternativ</text>\n<text x=\"243\" y=\"291\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Trigger-Event</text>\n<line x1=\"365\" y1=\"338\" x2=\"609\" y2=\"338\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"329\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">2. Bearbeitungsstand zur Bestellung</text>\n<text x=\"487\" y=\"353\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 21047 · E_0613</text>\n<text x=\"487\" y=\"366\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0613 — Bestellung prüfen</text>\n<line x1=\"365\" y1=\"400\" x2=\"121\" y2=\"400\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"391\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"415\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n</svg>"} titel="NB" />

<a id="abschnitt-schritte"></a>

## Prozessschritte

<Schritt nr="1" anker="schritt-1" richtung="eingehend" kopf={{"links": {"label": "NB", "eigen": true}, "rechts": {"label": "ÜNB"}}}>

### Bestellung einer Änderung von Abrechnungsdaten zur Bilanzkreisabrechnung

<Schrittskizze sicht={{"label": "NB"}} zeilen={[{"art": "empfangen", "label": "ÜNB", "weg": "AS4", "nachrichten": [{"nr": "55614", "titel": "Rückmeldung/Anfrage Abr.-Daten BK-Abr. verb. MaLo"}, {"nr": "55675", "titel": "Rückmeldung/Anfrage Abr.-Daten BK-Abr. erz. Malo"}]}, {"art": "lesen_aperak", "schnittstellen": [{"label": "Marktlokation lesen"}]}, {"art": "aperak", "werte": ["Z10", "Z16", "Z43", "Z33"]}, {"art": "erstellen"}, {"art": "fortschreiben", "nummern": ["55614"]}, {"art": "ebd", "baeume": [{"code": "E_0618", "titel": "Rückmeldung verarbeiten (Basiert auf EBD: E_0626_Rückmeldung auf Änderung prüfen)"}, {"code": "E_0613", "titel": "Bestellung prüfen (Basiert auf EBD: E_0573_Bestellung zur Stammdatenänderung prüfen)"}]}, {"art": "folgeprozess", "werte": ["21047"]}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55614](/schnittstellen/202604/pruefi/UTILMD/PI_55614) — Rückmeldung/Anfrage Abr.-Daten BK-Abr. verb. MaLo · AS4
- [55675](/schnittstellen/202604/pruefi/UTILMD/PI_55675) — Rückmeldung/Anfrage Abr.-Daten BK-Abr. erz. Malo · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **ÜNB** · AS4

</li>

<li data-teil="lesen" data-stufe="aperak">

**Daten für die Eingangsprüfung laden**
- [Marktlokation lesen](/api/202604/backend-lesen/getmarketlocationbasic#marktlokation-lesen) `GET /getMarketLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getMarketLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": false, "defaultValue": "MALO", "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": false, "defaultValue": "2024-06-28T12:18:00Z", "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_MARKTLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

</li>

<li data-teil="aperak">

**Aperak-Prüfungen**
- `55614`, `55675` → `Z10`
- `55614`, `55675` → `Z16`
- `55614`, `55675` → `Z43` — Aperak Prüfung: Stimmt Objekteigenschaft überein?
- `55614`, `55675` → `Z33`

</li>

<li data-teil="schnittstelle" data-art="schreiben">

**Schreibende Schnittstelle**
- Vorgang angelegt — [Prozessdaten erstellen](/api/202604/backend-schreiben-nb/createprocessdata#prozessdaten-erstellen) `POST /createProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/createProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "ERSTELLEN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"BILANZIERUNG\": [\n      {\n        \"bilanzkreis\": \"11XEONBAYERN---I\",\n        \"boTyp\": \"BILANZIERUNG\",\n        \"datenqualitaet\": \"ERWARTETE_DATEN\",\n        \"detailsPrognosegrundlage\": [\n          \"SLP_SEP\"\n        ],\n        \"gueltigkeitszeitraum\": {\n          \"enddatum\": \"2025-07-23T22:00:00Z\",\n          \"startdatum\": \"2025-06-23T22:00:00Z\",\n          \"zeitraumId\": 1\n        },\n        \"jahresverbrauchsprognose\": {\n          \"einheit\": \"KWH\",\n          \"wert\": 4100\n        },\n        \"lastprofile\": [\n          {\n            \"bezeichnung\": \"H0\",\n            \"einspeisung\": false,\n            \"herausgeber\": \"NB\",\n            \"profilart\": \"ART_STANDARDLASTPROFIL\",\n            \"verfahren\": \"SYNTHETISCH\"\n          }\n        ],\n        \"prognosegrundlage\": \"PROFILE\",\n        \"versionStruktur\": \"1\",\n        \"zeitreihentyp\": \"SLS\"\n      },\n      {\n        \"bilanzkreis\": \"11XEONBAYERN---I\",\n        \"boTyp\": \"BILANZIERUNG\",\n        \"datenqualitaet\": \"ERWARTETE_DATEN\",\n        \"detailsPrognosegrundlage\": [\n          \"SLP_SEP\"\n        ],\n        \"gueltigkeitszeitraum\": {\n          \"startdatum\": \"2025-07-23T22:00:00Z\",\n          \"zeitraumId\": 2\n        },\n        \"jahresverbrauchsprognose\": {\n          \"einheit\": \"KWH\",\n          \"wert\": 4200\n        },\n        \"lastprofile\": [\n          {\n            \"bezeichnung\": \"H0\",\n            \"einspeisung\": false,\n            \"herausgeber\": \"NB\",\n            \"profilart\": \"ART_STANDARDLASTPROFIL\",\n            \"verfahren\": \"SYNTHETISCH\"\n          }\n        ],\n        \"prognosegrundlage\": \"PROFILE\",\n        \"versionStruktur\": \"1\",\n        \"zeitreihentyp\": \"SLS\"\n      }\n    ],\n    \"MARKTLOKATION\": [\n      {\n        \"bilanzierungsgebiet\": \"11YV000000007509\",\n        \"boTyp\": \"MARKTLOKATION\",\n        \"datenqualitaet\": \"ERWARTETE_DATEN\",\n        \"gueltigkeitszeitraum\": {\n          \"enddatum\": \"2025-07-23T22:00:00Z\",\n          \"startdatum\": \"2025-06-23T22:00:00Z\",\n          \"zeitraumId\": 1\n        },\n        \"marktlokationsId\": \"20072281644\",\n        \"marktrollen\": [\n          {\n            \"boTyp\": \"MARKTTEILNEHMER\",\n            \"gewerbekennzeichnung\": true,\n            \"marktrolle\": \"LF\",\n            \"rollencodenummer\": \"9903729000007\",\n            \"rollencodetyp\": \"BDEW\",\n            \"versionStruktur\": \"1\"\n          }\n        ],\n        \"netzebene\": \"NSP\",\n        \"regelzone\": \"10YDE-ENBW-----N\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      },\n      {\n        \"bilanzierungsgebiet\": \"11YV000000007509\",\n        \"boTyp\": \"MARKTLOKATION\",\n        \"datenqualitaet\": \"ERWARTETE_DATEN\",\n        \"gueltigkeitszeitraum\": {\n          \"startdatum\": \"2025-07-23T22:00:00Z\",\n          \"zeitraumId\": 2\n        },\n        \"marktlokationsId\": \"20072281644\",\n        \"marktrollen\": [\n          {\n            \"boTyp\": \"MARKTTEILNEHMER\",\n            \"gewerbekennzeichnung\": true,\n            \"marktrolle\": \"LF\",\n            \"rollencodenummer\": \"9903729000007\",\n            \"rollencodetyp\": \"BDEW\",\n            \"versionStruktur\": \"1\"\n          }\n        ],\n        \"netzebene\": \"NSP\",\n        \"regelzone\": \"10YDE-ENBW-----N\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"VERWENDUNGSZEITRAUM\": [\n      {\n        \"boTyp\": \"VERWENDUNGSZEITRAUM\",\n        \"datenqualitaet\": \"ERWARTETE_DATEN\",\n        \"versionStruktur\": \"1\",\n        \"verwendungAb\": \"2025-06-23T22:00:00Z\",\n        \"verwendungBis\": \"2025-07-23T22:00:00Z\",\n        \"zeitraumId\": 1\n      },\n      {\n        \"boTyp\": \"VERWENDUNGSZEITRAUM\",\n        \"datenqualitaet\": \"ERWARTETE_DATEN\",\n        \"versionStruktur\": \"1\",\n        \"verwendungAb\": \"2025-07-23T22:00:00Z\",\n        \"zeitraumId\": 2\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"ansprechpartner\": {\n        \"boTyp\": \"ANSPRECHPARTNER\",\n        \"nachname\": \"P GETTY\",\n        \"rufnummern\": [\n          {\n            \"nummerntyp\": \"RUF_DURCHWAHL\",\n            \"rufnummer\": \"+3222271020\"\n          }\n        ],\n        \"versionStruktur\": \"1\"\n      },\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9911835000001\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"anfragereferenznummer\": \"BKA4321\",\n    \"antwortStatusZeitraum\": [\n      {\n        \"code\": \"A99\",\n        \"liste\": \"E_0612\",\n        \"zeitraumId\": 1\n      },\n      {\n        \"code\": \"A99\",\n        \"liste\": \"E_0612\",\n        \"zeitraumId\": 2\n      }\n    ],\n    \"datenaustauschreferenz\": \"002351596028\",\n    \"dokumentennummer\": \"002351596028\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9900750000006\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"freitext\": \"Im Zeitraum 1 und 2 werden andere Daten erwartet\",\n    \"kategorie\": \"E03\",\n    \"nachrichtendatum\": \"2025-06-24T12:31:00Z\",\n    \"nachrichtenreferenznummer\": \"002351596028\",\n    \"pruefidentifikator\": \"55614\",\n    \"sparte\": \"STROM\",\n    \"transaktionsgrund\": \"ZX3\",\n    \"vorgangsnummer\": \"24062416225400000000000102159662011\"\n  },\n  \"zusatzdaten\": {}\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Legt im Backend einen neuen Vorgang mit den Daten der eingegangenen Nachricht an.

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- `55614` → Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202604/backend-schreiben-nb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"BILANZIERUNG\": [\n      {\n        \"bilanzkreis\": \"11XEONBAYERN---I\",\n        \"boTyp\": \"BILANZIERUNG\",\n        \"datenqualitaet\": \"ERWARTETE_DATEN\",\n        \"detailsPrognosegrundlage\": [\n          \"SLP_SEP\"\n        ],\n        \"gueltigkeitszeitraum\": {\n          \"enddatum\": \"2025-07-23T22:00:00Z\",\n          \"startdatum\": \"2025-06-23T22:00:00Z\",\n          \"zeitraumId\": 1\n        },\n        \"jahresverbrauchsprognose\": {\n          \"einheit\": \"KWH\",\n          \"wert\": 4100\n        },\n        \"lastprofile\": [\n          {\n            \"bezeichnung\": \"H0\",\n            \"einspeisung\": false,\n            \"herausgeber\": \"NB\",\n            \"profilart\": \"ART_STANDARDLASTPROFIL\",\n            \"verfahren\": \"SYNTHETISCH\"\n          }\n        ],\n        \"prognosegrundlage\": \"PROFILE\",\n        \"versionStruktur\": \"1\",\n        \"zeitreihentyp\": \"SLS\"\n      },\n      {\n        \"bilanzkreis\": \"11XEONBAYERN---I\",\n        \"boTyp\": \"BILANZIERUNG\",\n        \"datenqualitaet\": \"ERWARTETE_DATEN\",\n        \"detailsPrognosegrundlage\": [\n          \"SLP_SEP\"\n        ],\n        \"gueltigkeitszeitraum\": {\n          \"startdatum\": \"2025-07-23T22:00:00Z\",\n          \"zeitraumId\": 2\n        },\n        \"jahresverbrauchsprognose\": {\n          \"einheit\": \"KWH\",\n          \"wert\": 4200\n        },\n        \"lastprofile\": [\n          {\n            \"bezeichnung\": \"H0\",\n            \"einspeisung\": false,\n            \"herausgeber\": \"NB\",\n            \"profilart\": \"ART_STANDARDLASTPROFIL\",\n            \"verfahren\": \"SYNTHETISCH\"\n          }\n        ],\n        \"prognosegrundlage\": \"PROFILE\",\n        \"versionStruktur\": \"1\",\n        \"zeitreihentyp\": \"SLS\"\n      }\n    ],\n    \"MARKTLOKATION\": [\n      {\n        \"bilanzierungsgebiet\": \"11YV000000007509\",\n        \"boTyp\": \"MARKTLOKATION\",\n        \"datenqualitaet\": \"ERWARTETE_DATEN\",\n        \"gueltigkeitszeitraum\": {\n          \"enddatum\": \"2025-07-23T22:00:00Z\",\n          \"startdatum\": \"2025-06-23T22:00:00Z\",\n          \"zeitraumId\": 1\n        },\n        \"marktlokationsId\": \"20072281644\",\n        \"marktrollen\": [\n          {\n            \"boTyp\": \"MARKTTEILNEHMER\",\n            \"gewerbekennzeichnung\": true,\n            \"marktrolle\": \"LF\",\n            \"rollencodenummer\": \"9903729000007\",\n            \"rollencodetyp\": \"BDEW\",\n            \"versionStruktur\": \"1\"\n          }\n        ],\n        \"netzebene\": \"NSP\",\n        \"regelzone\": \"10YDE-ENBW-----N\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      },\n      {\n        \"bilanzierungsgebiet\": \"11YV000000007509\",\n        \"boTyp\": \"MARKTLOKATION\",\n        \"datenqualitaet\": \"ERWARTETE_DATEN\",\n        \"gueltigkeitszeitraum\": {\n          \"startdatum\": \"2025-07-23T22:00:00Z\",\n          \"zeitraumId\": 2\n        },\n        \"marktlokationsId\": \"20072281644\",\n        \"marktrollen\": [\n          {\n            \"boTyp\": \"MARKTTEILNEHMER\",\n            \"gewerbekennzeichnung\": true,\n            \"marktrolle\": \"LF\",\n            \"rollencodenummer\": \"9903729000007\",\n            \"rollencodetyp\": \"BDEW\",\n            \"versionStruktur\": \"1\"\n          }\n        ],\n        \"netzebene\": \"NSP\",\n        \"regelzone\": \"10YDE-ENBW-----N\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"VERWENDUNGSZEITRAUM\": [\n      {\n        \"boTyp\": \"VERWENDUNGSZEITRAUM\",\n        \"datenqualitaet\": \"ERWARTETE_DATEN\",\n        \"versionStruktur\": \"1\",\n        \"verwendungAb\": \"2025-06-23T22:00:00Z\",\n        \"verwendungBis\": \"2025-07-23T22:00:00Z\",\n        \"zeitraumId\": 1\n      },\n      {\n        \"boTyp\": \"VERWENDUNGSZEITRAUM\",\n        \"datenqualitaet\": \"ERWARTETE_DATEN\",\n        \"versionStruktur\": \"1\",\n        \"verwendungAb\": \"2025-07-23T22:00:00Z\",\n        \"zeitraumId\": 2\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"ansprechpartner\": {\n        \"boTyp\": \"ANSPRECHPARTNER\",\n        \"nachname\": \"P GETTY\",\n        \"rufnummern\": [\n          {\n            \"nummerntyp\": \"RUF_DURCHWAHL\",\n            \"rufnummer\": \"+3222271020\"\n          }\n        ],\n        \"versionStruktur\": \"1\"\n      },\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9911835000001\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"anfragereferenznummer\": \"BKA4321\",\n    \"antwortStatusZeitraum\": [\n      {\n        \"code\": \"A99\",\n        \"liste\": \"E_0612\",\n        \"zeitraumId\": 1\n      },\n      {\n        \"code\": \"A99\",\n        \"liste\": \"E_0612\",\n        \"zeitraumId\": 2\n      }\n    ],\n    \"datenaustauschreferenz\": \"002351596028\",\n    \"dokumentennummer\": \"002351596028\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"gewerbekennzeichnung\": true,\n      \"rollencodenummer\": \"9900750000006\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"freitext\": \"Im Zeitraum 1 und 2 werden andere Daten erwartet\",\n    \"kategorie\": \"E03\",\n    \"nachrichtendatum\": \"2025-06-24T12:31:00Z\",\n    \"nachrichtenreferenznummer\": \"002351596028\",\n    \"pruefidentifikator\": \"55614\",\n    \"sparte\": \"STROM\",\n    \"transaktionsgrund\": \"ZX3\",\n    \"vorgangsnummer\": \"24062416225400000000000102159662011\"\n  },\n  \"zusatzdaten\": {}\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend mit den Daten der eingegangenen Nachricht fort.

</li>

<li data-teil="baum">

**Entscheidungsbaum**
- `55614`, `55675` → [E_0618](/referenz/202604/ebd/E_0618) — Rückmeldung verarbeiten (Basiert auf EBD: E_0626_Rückmeldung auf Änderung prüfen)
- `55675` → [E_0613](/referenz/202604/ebd/E_0613) — Bestellung prüfen (Basiert auf EBD: E_0573_Bestellung zur Stammdatenänderung prüfen)

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

<Schritt nr="2" anker="schritt-2" richtung="ausgehend" kopf={{"links": {"label": "NB", "eigen": true}, "rechts": {"label": "ÜNB"}}}>

### Bearbeitungsstand zur Bestellung

<Schrittskizze sicht={{"label": "NB"}} zeilen={[{"art": "folge_ausloeser", "werte": ["55614"]}, {"art": "ausloeser", "werte": ["START_VERSAND_BEARB_MELDUNG", "START_VERSAND_STATUSMELDUNG"]}, {"art": "senden", "label": "ÜNB", "weg": "AS4", "nachrichten": [{"nr": "21047", "titel": "Bearbeitungsstandsmeldung"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [21047](/schnittstellen/202604/pruefi/IFTSTA/PI_21047) — Bearbeitungsstandsmeldung · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="folge_ausloeser">

**Ausgelöst durch Eingang**
- [55614](/schnittstellen/202604/pruefi/UTILMD/PI_55614) — Rückmeldung/Anfrage Abr.-Daten BK-Abr. verb. MaLo

Die MACO APP sendet diese Nachricht selbst, als Folgeprozess nach diesem Eingang. Daneben kann das Backend diesen Schritt mit einem Ereignis anstoßen — der nächste Punkt.

</li>

<li data-teil="ausloeser">

**Prozessauslöser**
- [`START_VERSAND_BEARB_MELDUNG`](/schnittstellen/202604/trigger/events/NB-START_VERSAND_BEARB_MELDUNG) · [Im Playground ausprobieren](/api/202604/ausloeser-nb/start-versand-bearb-meldung)
- [`START_VERSAND_STATUSMELDUNG`](/schnittstellen/202604/trigger/events/NB-START_VERSAND_STATUSMELDUNG) · [Im Playground ausprobieren](/api/202604/ausloeser-nb/start-versand-statusmeldung)

Das Backend stößt diesen Schritt mit einem dieser Ereignisse an.

</li>

<li data-teil="nachricht">

Nachricht an **ÜNB** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `21047` → [E_0613](/referenz/202604/ebd/E_0613) · NB · Bestellung prüfen (Basiert auf EBD: E_0573_Bestellung zur Stammdatenänderung prüfen)

</div>

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202604/backend-schreiben-nb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"STATUSMITTEILUNG\": [\n      {\n        \"auftragsstatus\": \"KEINE_AENDERUNG_DER_DATEN\",\n        \"boTyp\": \"STATUSMITTEILUNG\",\n        \"positionsdaten\": [\n          {\n            \"positionsnummer\": 1\n          }\n        ],\n        \"statusObjekt\": \"VERAENDERUNGSSTATUS_DER_DATEN\",\n        \"versionStruktur\": \"1\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"marktrolle\": \"LF\",\n      \"rollencodenummer\": \"9900321000005\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"antwortstatus\": \"A01\",\n    \"antwortstatusCodeliste\": \"E_0588\",\n    \"datenaustauschreferenz\": \"M0M56B09\",\n    \"dokumentennummer\": \"BGMM0M7F86Z\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"marktrolle\": \"NB\",\n      \"rollencodenummer\": \"9903790000002\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"Z33\",\n    \"nachrichtendatum\": \"2025-04-04T12:00:00Z\",\n    \"nachrichtenreferenznummer\": \"UNHM09Y0DVP\",\n    \"pruefidentifikator\": \"21047\",\n    \"sparte\": \"STROM\",\n    \"vorgangsreferenznummer\": \"ABC12345\"\n  },\n  \"zusatzdaten\": {}\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

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
| [E_0613](/referenz/202604/ebd/E_0613) | Bestellung prüfen (Basiert auf EBD: E_0573_Bestellung zur Stammdatenänderung prüfen) |

</details>

<a id="abschnitt-informationen"></a>

## Prozess-Informationen

Wortlaut der Lesefassung, Steckbrief Kap. 3.1.3.1, S. 77–79.

<Stepper>
<ol>

<li data-blatt="vorbedingungen">

### Vorbedingungen

- Die zum bestellten Zeitpunkt vorhandene Gerätetechnik ermöglicht die Änderung.
- Im Fall der Bestellung einer Änderung von Abrechnungsdaten zur Netznutzungsabrechnung:
  - Sofern der Bedarf der Anwendung einer Zählzeitdefinition des NB mit Zählzeitenanwendungszweck „Netznutzung“ vorliegt, muss eine entsprechende Konfiguration fristgerecht und erfolgreich über die Use-Cases im Kapitel „Bestellung einer Konfiguration“ (GPKE Teil 3) eingerichtet worden sein.
  - Es handelt sich um eine verbrauchende Marktlokation.
  - Dem LF liegen Abrechnungsdaten aufgrund des Use-Cases „[Abrechnungsdaten Netznutzungsabrechnung](/prozessdoku/202604/NB/GPKE-Teil2-abrechnungsdaten-netznutzungsabrechnung)“ vor.
  - Im Fall der Bestellung einer Änderung der Konzessionsabgabe:
    - Im Fall der Bestellung einer Schwachlast-Konzessionsabgabe:
- Es besteht ein Stromliefervertrag, der die Voraussetzungen zur Abrechnung der niedrigen Konzessionsabgabe an der Marktlokation erfüllt.
    - Im Fall einer Schwachlast-Konzessionsabgabe, für die die vertragliche Voraussetzung für die Schwachlast-Konzessionsabgabe zwischen LF und Letztverbraucher entfallen wird/ist, muss der LF eine Änderung der Konzessionsabgabe ungleich der Schwachlast-Konzessionsabgabe bestellen.
- Im Fall der Bestellung einer Änderung von Abrechnungsdaten zur Bilanzkreisabrechnung:
  - Dem LF liegen Abrechnungsdaten aufgrund des Use-Cases „[Abrechnungsdaten Bilanzkreisabrechnung](/prozessdoku/202604/NB/GPKE-Teil2-abrechnungsdaten-bilanzkreisabrechnung)“ vor bzw.
  - dem ÜNB liegen Abrechnungsdaten aufgrund des Use-Cases „[Abrechnungsdaten Bilanzkreisabrechnung](/prozessdoku/202604/NB/GPKE-Teil2-abrechnungsdaten-bilanzkreisabrechnung)“ vor.

</li>

<li data-blatt="ergebnisse">

### Ergebnisse

- Im Fall der Bestellung einer Änderung von Abrechnungsdaten zur Netznutzungsabrechnung: Der NB führt den Use-Case „[Abrechnungsdaten Netznutzungsabrechnung](/prozessdoku/202604/NB/GPKE-Teil2-abrechnungsdaten-netznutzungsabrechnung)“ aus.
- Im Fall der Bestellung einer Änderung von Abrechnungsdaten zur Bilanzkreisabrechnung: Der NB führt den Use-Case „[Abrechnungsdaten Bilanzkreisabrechnung](/prozessdoku/202604/NB/GPKE-Teil2-abrechnungsdaten-bilanzkreisabrechnung)“ aus.

</li>

<li data-blatt="fehlerfall">

### Fehlerfall

#### Ergebnis im Fehlerfall

Der LF bzw. ÜNB prüft, ob eine erneute Bestellung erforderlich ist.

#### Fehlerfälle

- Die zum bestellten Zeitpunkt vorhandene Gerätetechnik ermöglicht die Änderung nicht.
- Im Fall der Bestellung einer Änderung von Abrechnungsdaten zur Netznutzungsabrechnung: Es handelt sich um eine erzeugende Marktlokation bzw. eine Tranche.

</li>

<li data-blatt="anforderungen">

### Weitere Anforderungen

- Hinweis: Die Bestellung einer Änderung des Bilanzierungsverfahrens ist nicht über diesen Use-Case, sondern über den Use-Case „[Bestellung einer Konfiguration vom LF an NB](/prozessdoku/202604/NB/GPKE-Teil3-bestellung-einer-konfiguration-vom-lf-an-nb)“ (GPKE Teil 3) zu bestellen.
- Hinweise zu erzeugenden Marktlokationen bzw. zu Tranchen:
  - Der LF wendet für eine Änderung der Veräußerungsform und gleichzeitiger Zuordnung des LF zur Marktlokation bzw. Tranche den Use-Case “Lieferbeginn“ an.
  - Der LF wendet für eine Änderung der Tranchengröße den Use-Case “Lieferbeginn“ (s. Geschäftsvorfall 3) an.
- Hinweis: Sofern die zum bestellten Zeitpunkt vorhandene Gerätetechnik die Bestellung nicht ermöglicht, ist die Änderung der Gerätetechnik nicht über diesen Use-Case zu bestellen. Eine entsprechende Änderung der Gerätetechnik kann im Rahmen eines Gerätewechsels bzw. über die Use-Cases zur Messlokationsänderung (WiM Teil 1) beauftragt werden.
- Bzgl. der Festlegung zu Netzentgelten für steuerbare Anschlüsse und Verbrauchseinrichtungen (NSAVER) nach § 14a EnWG (BK8-22/010-A) gilt: Im Fall der Bestellung einer Änderung von Abrechnungsdaten zur Netznutzungsabrechnung werden ergänzende Vorgaben (wie z.B. Vorbedingungen und Fristen) durch die beim BDEW angesiedelte Expertengruppe EDI@Energy unter Beteiligung der Bundesnetzagentur veröffentlicht und gepflegt.

</li>

<li data-blatt="anlass">

### Anlass

- Der LF hat den Bedarf einer Änderung von Abrechnungsdaten zur Netznutzungsabrechnung (z.B. Änderung des Netznutzungsabrechnungsmodells von Arbeitspreis/Grundpreis auf Arbeitspreis/Leistungspreis oder Änderung des Zahlers der Netznutzung von Letztverbraucher auf LF).
- Der LF hat den Bedarf einer Änderung von Abrechnungsdaten zur Bilanzkreisabrechnung (z.B. Änderung der Jahresverbrauchprognose oder Änderung der Veräußerungsform)
- Der ÜNB hat den Bedarf einer Änderung von Abrechnungsdaten zur Bilanzkreisabrechnung.
- Der LF bzw. ÜNB geht von einem Datenschiefstand aus.

</li>

<li data-blatt="erste-nachricht">

### Erste Nachricht

**ÜNB** sendet „Bestellung einer Änderung von Abrechnungsdaten zur Bilanzkreisabrechnung“ (Schritt 1). Ab hier ist der Beteiligte dieser Seite am Zug.

</li>

<li data-blatt="ziel">

### Ziel

Der Bearbeitungsstand zur vom LF bzw. ÜNB bestellten Änderung von Abrechnungsdaten liegt dem LF bzw. ÜNB vom NB vor.

</li>

</ol>
</Stepper>

<a id="abschnitt-sichten"></a>

## Andere Sichten des Prozesses

Derselbe Prozess, aus den Augen der anderen Beteiligten: dieselben Schritte, jeweils aus deren Sicht gelesen.

- [Sicht ÜNB](/prozessdoku/202604/UENB/GPKE-Teil2-bestellung-einer-aenderung-von-abrechnungsdaten-zur-bilanzkreisabrechnung-von-uenb-an-nb) — ÜNB · Marktrolle UENB

<Hinweisbereich>

*Die Schritte sind die **möglichen** Nachrichten dieses Prozesses, keine Abfolge — die Quelle führt weder Bedingungen noch Alternativen. Das Kästchen am Schritt nennt links die eigene Sicht: **←** empfängt sie, **→** sendet sie. Zugeklappte Schritte laufen zwischen anderen Marktpartnern.*

</Hinweisbereich>
