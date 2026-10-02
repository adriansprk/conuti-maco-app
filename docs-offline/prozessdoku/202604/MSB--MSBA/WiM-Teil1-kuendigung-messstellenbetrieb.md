# Kündigung Messstellenbetrieb — Sicht MSBA

<Kopf rolle="MSB" beteiligter="MSBA" festlegung="WiM" dokument="WiM Strom Teil 1" kapitel="2.2.2" sparte="Strom" schritte={2} suchtitel="Kündigung Messstellenbetrieb — Sicht MSBA (Marktrolle MSB) · WiM Strom Teil 1 · Formatversion 202604" abschnitte={[{"id": "abschnitt-ablauf", "label": "Prozessablauf"}, {"id": "abschnitt-schritte", "label": "Prozessschritte"}, {"id": "abschnitt-informationen", "label": "Prozess-Informationen"}, {"id": "abschnitt-sichten", "label": "Andere Sichten des Prozesses"}]} />

<Kurzfassung>

Der MSBN kündigt im Auftrag des AN bzw. ANN den für die genannte Messlokation bestehenden Messstellenbetriebsvertrag. In der Kündigung kann ein beliebiger in der Zukunft liegender Kündigungstermin (auch untermonatlich) angegeben werden. Der Kündigungstermin kann sich
- auf einen fixen Zeitpunkt 00:00 Uhr oder
- auf einen nächstmöglichen Zeitpunkt 00:00 Uhr beziehen. Der Kündigungstermin ist der Zeitpunkt, zu dem die zu kündigende Dienstleistung enden soll. Der MSBA prüft die Kündigung und teilt dem MSBN das Ergebnis mit. Dabei sind folgende Regeln einzuhalten:
- Hat der MSBN auf einen fixen Zeitpunkt gekündigt und wird dieser vom MSBA nicht bestätigt, so teilt der MSBA den nächstmöglichen Zeitpunkt, zu dem eine Kündigung erfolgen kann, und die Kündigungsfrist in der Ablehnung mit.
- Hat der MSBN auf den nächstmöglichen Zeitpunktgekündigt, so bestätigt der MSBA die Kündigung unter Angabe dieses Zeitpunkts.
- Liegt dem MSBA bereits eine wirksame Kündigung vor (durch einen MSBN oder den AN bzw. ANN) sind die entsprechenden Konstellationen im Kapitel 2.2.3 „Antwort MSBA bei Kündigung eines bereits wirksam gekündigten Vertrages“ beschrieben.

</Kurzfassung>

<a id="abschnitt-ablauf"></a>

## Prozessablauf aus Sicht des MSB (MSBA)

<Systembild svg={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1004 921\" width=\"1004\" height=\"921\" role=\"img\" aria-labelledby=\"sb-title\" class=\"maco-systembild\">\n<title id=\"sb-title\">Systembild: Kündigung Messstellenbetrieb aus Sicht MSB</title>\n<defs><marker id=\"sb-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect class=\"sb-lane-kopf\" x=\"16\" y=\"12\" width=\"232\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend-System des Kunden</text>\n<rect class=\"sb-lane-kopf\" x=\"398\" y=\"12\" width=\"264\" height=\"46\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · MSB (entsprich…</text>\n<rect class=\"sb-lane-kopf\" x=\"812\" y=\"12\" width=\"176\" height=\"46\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"900\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Marktpartner</text>\n<line x1=\"323\" y1=\"58\" x2=\"323\" y2=\"909\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"737\" y1=\"58\" x2=\"737\" y2=\"909\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect class=\"sb-kasten sb-eingehend\" x=\"432\" y=\"80\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"100\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">1. Kündigung</text>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"78\" r=\"5\"/><line x1=\"900\" y1=\"83\" x2=\"900\" y2=\"95\"/><line x1=\"893\" y1=\"87\" x2=\"907\" y2=\"87\"/><line x1=\"900\" y1=\"95\" x2=\"894\" y2=\"105\"/><line x1=\"900\" y1=\"95\" x2=\"906\" y2=\"105\"/></g>\n<text x=\"900\" y=\"127\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">MSB (entspricht MSBN…</text>\n<line x1=\"878\" y1=\"96\" x2=\"628\" y2=\"96\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"88\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"112\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">55039</text>\n<rect class=\"sb-kasten sb-schreiben\" x=\"432\" y=\"163\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"183\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"113\" x2=\"530\" y2=\"163\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-schreiben\" x=\"34\" y=\"163\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"183\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten erstellen</text>\n<line x1=\"432\" y1=\"179\" x2=\"230\" y2=\"179\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"171\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"227\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"247\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"196\" x2=\"530\" y2=\"227\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"227\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"247\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"243\" x2=\"230\" y2=\"243\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"235\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-lesen\" x=\"432\" y=\"291\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"311\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Daten für die Prüfung laden</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"260\" x2=\"530\" y2=\"291\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-lesen\" x=\"34\" y=\"283\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"303\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">2 Lese-Schnittstellen</text>\n<text x=\"132\" y=\"318\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">aufgerufen</text>\n<line x1=\"432\" y1=\"307\" x2=\"230\" y2=\"307\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"299\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<text x=\"331\" y=\"323\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">je einzeln am Schritt</text>\n<rect class=\"sb-kasten sb-ebd\" x=\"432\" y=\"365\" width=\"196\" height=\"63\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"385\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">EBD prüfen: E_0200</text>\n<text x=\"530\" y=\"400\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label-2, #424245)\">Kündigung</text>\n<text x=\"530\" y=\"415\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label-2, #424245)\">Messstellenbetrieb prüfen</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"324\" x2=\"530\" y2=\"365\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-lesen_verarbeitung\" x=\"432\" y=\"454\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"474\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Daten für die Verarbeitung</text>\n<text x=\"530\" y=\"489\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">laden</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"428\" x2=\"530\" y2=\"454\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-lesen_verarbeitung\" x=\"34\" y=\"462\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"482\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Marktlokation lesen</text>\n<line x1=\"432\" y1=\"478\" x2=\"230\" y2=\"478\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"470\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<rect class=\"sb-kasten sb-folgeprozess\" x=\"432\" y=\"528\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"548\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Folgeprozess auslösen:</text>\n<text x=\"530\" y=\"563\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">55040, 55041</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"502\" x2=\"530\" y2=\"528\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-folge_ausloeser\" x=\"432\" y=\"602\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"622\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Ausgelöst durch Eingang:</text>\n<text x=\"530\" y=\"637\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">55039</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"576\" x2=\"530\" y2=\"602\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-lesen_verarbeitung\" x=\"432\" y=\"676\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"696\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Daten für die Verarbeitung</text>\n<text x=\"530\" y=\"711\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">laden</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"650\" x2=\"530\" y2=\"676\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-lesen_verarbeitung\" x=\"34\" y=\"676\" width=\"196\" height=\"48\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"696\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">4 Lese-Schnittstellen</text>\n<text x=\"132\" y=\"711\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">aufgerufen</text>\n<line x1=\"432\" y1=\"700\" x2=\"230\" y2=\"700\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"692\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n<text x=\"331\" y=\"716\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">je einzeln am Schritt</text>\n<rect class=\"sb-kasten sb-ausgehend\" x=\"432\" y=\"750\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"770\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">2. Antwort der Kündigung</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"724\" x2=\"530\" y2=\"750\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<g class=\"sb-akteur\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.4\" fill=\"none\"><circle cx=\"900\" cy=\"748\" r=\"5\"/><line x1=\"900\" y1=\"753\" x2=\"900\" y2=\"765\"/><line x1=\"893\" y1=\"757\" x2=\"907\" y2=\"757\"/><line x1=\"900\" y1=\"765\" x2=\"894\" y2=\"775\"/><line x1=\"900\" y1=\"765\" x2=\"906\" y2=\"775\"/></g>\n<text x=\"900\" y=\"797\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">MSB (entspricht MSBN…</text>\n<line x1=\"628\" y1=\"766\" x2=\"878\" y2=\"766\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"753\" y=\"758\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">AS4</text>\n<text x=\"753\" y=\"782\" text-anchor=\"middle\" font-size=\"10.5\" fill=\"var(--prn-label-2, #424245)\">55040, 55041</text>\n<rect class=\"sb-kasten sb-fortschreiben\" x=\"432\" y=\"833\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"530\" y=\"853\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<line class=\"sb-fluss\" x1=\"530\" y1=\"783\" x2=\"530\" y2=\"833\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1.4\" marker-end=\"url(#sb-arrow)\"/>\n<rect class=\"sb-kasten sb-backend sb-fortschreiben\" x=\"34\" y=\"833\" width=\"196\" height=\"33\" rx=\"8\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"132\" y=\"853\" text-anchor=\"middle\" font-size=\"12\" fill=\"var(--prn-label, #1d1d1f)\">Prozessdaten aktualisieren</text>\n<line x1=\"432\" y1=\"849\" x2=\"230\" y2=\"849\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" stroke-dasharray=\"6 3\" marker-end=\"url(#sb-arrow)\"/>\n<text x=\"331\" y=\"841\" text-anchor=\"middle\" font-size=\"11.5\" fill=\"var(--prn-label, #1d1d1f)\">API</text>\n</svg>"} gesamt={"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 730 424\" width=\"730\" height=\"424\" role=\"img\" aria-labelledby=\"sd-title\" class=\"maco-sequence\">\n<title id=\"sd-title\">Sequenzdiagramm: Kündigung Messstellenbetrieb aus Sicht MSB</title>\n<defs><marker id=\"sd-arrow\" viewBox=\"0 0 14 14\" refX=\"13\" refY=\"7\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0 0 L14 7 L0 14 z\" fill=\"var(--prn-label-2, #424245)\"/></marker></defs>\n<rect x=\"16\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"121\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">Backend (Kunde)</text>\n<line x1=\"121\" y1=\"64\" x2=\"121\" y2=\"412\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"260\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-accent-soft, #e4f2eb)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"365\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"var(--prn-label, #1d1d1f)\">MACO APP · MSB (entsprich…</text>\n<line x1=\"365\" y1=\"64\" x2=\"365\" y2=\"412\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<rect x=\"504\" y=\"12\" width=\"210\" height=\"52\" rx=\"10\" fill=\"var(--prn-bg-elevated, #f5f5f7)\" stroke=\"var(--prn-separator, #d2d2d7)\"/>\n<text x=\"609\" y=\"43\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"500\" fill=\"var(--prn-label, #1d1d1f)\">MSB (entspricht MSBN am O…</text>\n<line x1=\"609\" y1=\"64\" x2=\"609\" y2=\"412\" stroke=\"var(--prn-label-3, #6e6e73)\" stroke-width=\"1\" stroke-dasharray=\"4 4\"/>\n<line x1=\"609\" y1=\"90\" x2=\"365\" y2=\"90\" stroke=\"var(--prn-label-2, #424245)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"81\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">1. Kündigung</text>\n<text x=\"487\" y=\"105\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55039</text>\n<line x1=\"365\" y1=\"152\" x2=\"121\" y2=\"152\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"143\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang anlegen</text>\n<text x=\"243\" y=\"167\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten erstellen</text>\n<line x1=\"365\" y1=\"214\" x2=\"121\" y2=\"214\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"205\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"229\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n<line x1=\"365\" y1=\"276\" x2=\"609\" y2=\"276\" stroke=\"var(--prn-accent, #2f7d5c)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\"/>\n<text x=\"487\" y=\"267\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">2. Antwort der Kündigung</text>\n<text x=\"487\" y=\"291\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">AS4 · PI 55040, 55041 · E_0200</text>\n<text x=\"487\" y=\"304\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">E_0200 — Kündigung Messstellenbetrieb prüfen</text>\n<line x1=\"365\" y1=\"338\" x2=\"121\" y2=\"338\" stroke=\"var(--prn-blue, #0071e3)\" stroke-width=\"1.6\" marker-end=\"url(#sd-arrow)\" stroke-dasharray=\"6 3\"/>\n<text x=\"243\" y=\"329\" text-anchor=\"middle\" font-size=\"12.5\" fill=\"var(--prn-label, #1d1d1f)\">Vorgang fortschreiben</text>\n<text x=\"243\" y=\"353\" text-anchor=\"middle\" font-size=\"11\" fill=\"var(--prn-label-2, #424245)\">Prozessdaten aktualisieren</text>\n</svg>"} titel="MSBA" />

<a id="abschnitt-schritte"></a>

## Prozessschritte

<Schritt nr="1" anker="schritt-1" richtung="eingehend" kopf={{"links": {"label": "MSB (entspricht MSBA am Objekt Messlokation)", "eigen": true}, "rechts": {"label": "MSB (entspricht MSBN am Objekt Messlokation)"}}}>

### Kündigung

<Schrittskizze sicht={{"label": "MSBA"}} zeilen={[{"art": "empfangen", "label": "MSB (entspricht MSBN am Objekt Messlokation)", "weg": "AS4", "nachrichten": [{"nr": "55039", "titel": "Kündigung MSB"}]}, {"art": "erstellen"}, {"art": "fortschreiben"}, {"art": "lesen_ebd", "schnittstellen": [{"label": "Messlokation lesen"}, {"label": "Messstellenbetriebsvertrag lesen"}]}, {"art": "ebd", "baeume": [{"code": "E_0200", "titel": "Kündigung Messstellenbetrieb prüfen"}]}, {"art": "lesen_verarbeitung", "schnittstellen": [{"label": "Marktlokation lesen"}]}, {"art": "folgeprozess", "werte": ["55040", "55041"]}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55039](/schnittstellen/202604/pruefi/UTILMD/PI_55039) — Kündigung MSB · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="nachricht">

Nachricht von **MSB (entspricht MSBN am Objekt Messlokation)** · AS4

</li>

<li data-teil="schnittstelle" data-art="schreiben">

**Schreibende Schnittstelle**
- Vorgang angelegt — [Prozessdaten erstellen](/api/202604/backend-schreiben-msb/createprocessdata#prozessdaten-erstellen) `POST /createProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/createProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "ERSTELLEN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"MESSLOKATION\": [\n      {\n        \"boTyp\": \"MESSLOKATION\",\n        \"messlokationsId\": \"DE0032106765712000000000000000037\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"MESSSTELLENBETRIEBSVERTRAG\": [\n      {\n        \"boTyp\": \"VERTRAG\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\",\n        \"vertragsart\": \"MESSSTELLENBETRIEBSVERTRAG\",\n        \"vertragspartner2\": [\n          {\n            \"boTyp\": \"GESCHAEFTSPARTNER\",\n            \"geschaeftspartnerrolle\": [\n              \"KUNDE\"\n            ],\n            \"gewerbekennzeichnung\": false,\n            \"name1\": \"Mustermann\",\n            \"versionStruktur\": \"1\"\n          }\n        ]\n      }\n    ],\n    \"NETZNUTZUNGSVERTRAG\": [\n      {\n        \"boTyp\": \"VERTRAG\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\",\n        \"vertragsart\": \"NETZNUTZUNGSVERTRAG\",\n        \"vertragsende\": \"2025-06-30T22:00:00Z\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9904446000007\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"datenaustauschreferenz\": \"105431\",\n    \"dokumentennummer\": \"643428BGM\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9904446000007\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"E35\",\n    \"nachrichtendatum\": \"2025-04-04T08:21:00Z\",\n    \"nachrichtenreferenznummer\": \"643428\",\n    \"pruefidentifikator\": \"55039\",\n    \"sparte\": \"STROM\",\n    \"transaktionsgrund\": \"E03\",\n    \"vertragsende\": \"2025-06-30T22:00:00Z\",\n    \"vorgangsnummer\": \"1814631075\"\n  },\n  \"zusatzdaten\": {}\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Legt im Backend einen neuen Vorgang mit den Daten der eingegangenen Nachricht an.

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202604/backend-schreiben-msb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"MESSLOKATION\": [\n      {\n        \"boTyp\": \"MESSLOKATION\",\n        \"messlokationsId\": \"DE0032106765712000000000000000037\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"MESSSTELLENBETRIEBSVERTRAG\": [\n      {\n        \"boTyp\": \"VERTRAG\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\",\n        \"vertragsart\": \"MESSSTELLENBETRIEBSVERTRAG\",\n        \"vertragspartner2\": [\n          {\n            \"boTyp\": \"GESCHAEFTSPARTNER\",\n            \"geschaeftspartnerrolle\": [\n              \"KUNDE\"\n            ],\n            \"gewerbekennzeichnung\": false,\n            \"name1\": \"Mustermann\",\n            \"versionStruktur\": \"1\"\n          }\n        ]\n      }\n    ],\n    \"NETZNUTZUNGSVERTRAG\": [\n      {\n        \"boTyp\": \"VERTRAG\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\",\n        \"vertragsart\": \"NETZNUTZUNGSVERTRAG\",\n        \"vertragsende\": \"2025-06-30T22:00:00Z\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9904446000007\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"datenaustauschreferenz\": \"105431\",\n    \"dokumentennummer\": \"643428BGM\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9904446000007\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"E35\",\n    \"nachrichtendatum\": \"2025-04-04T08:21:00Z\",\n    \"nachrichtenreferenznummer\": \"643428\",\n    \"pruefidentifikator\": \"55039\",\n    \"sparte\": \"STROM\",\n    \"transaktionsgrund\": \"E03\",\n    \"vertragsende\": \"2025-06-30T22:00:00Z\",\n    \"vorgangsnummer\": \"1814631075\"\n  },\n  \"zusatzdaten\": {}\n}"} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

Schreibt den bestehenden Vorgang im Backend mit den Daten der eingegangenen Nachricht fort.

</li>

<li data-teil="lesen" data-stufe="ebd">

**Daten für die Prüfung laden**
- [Messlokation lesen](/api/202604/backend-lesen/getmeterlocationbasic#messlokation-lesen) `GET /getMeterLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getMeterLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_MESSLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Messstellenbetriebsvertrag lesen](/api/202604/backend-lesen/getmeasuringpointoperationcontractbasic#messstellenbetriebsvertrag-lesen) `GET /getMeasuringPointOperationContractBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getMeasuringPointOperationContractBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_MESSSTELLENBETRIEBSVERTRAG_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

</li>

<li data-teil="baum">

**Entscheidungsbaum**
- `55039` → [E_0200](/referenz/202604/ebd/E_0200) — Kündigung Messstellenbetrieb prüfen

</li>

<li data-teil="lesen" data-stufe="verarbeitung">

**Daten für die Verarbeitung laden**
- [Marktlokation lesen](/api/202604/backend-lesen/getmarketlocationbasic#marktlokation-lesen) `GET /getMarketLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getMarketLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": false, "defaultValue": "MALO", "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": false, "defaultValue": "2024-06-28T12:18:00Z", "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_MARKTLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

</li>

<li data-teil="folgeprozess">

**Folgeprozess auslösen**
- [55040](/schnittstellen/202604/pruefi/UTILMD/PI_55040) — Bestätigung Kündigung MSB
- [55041](/schnittstellen/202604/pruefi/UTILMD/PI_55041) — Ablehnung Kündigung MSB

Nach der Verarbeitung startet die MACO APP den Folgeprozess selbst; welcher davon läuft, hängt vom Ergebnis der Verarbeitung ab.

</li>

</ol>
</Stepper>

</div>

</Schritt>

<Schritt nr="2" anker="schritt-2" richtung="ausgehend" kopf={{"links": {"label": "MSB (entspricht MSBA am Objekt Messlokation)", "eigen": true}, "rechts": {"label": "MSB (entspricht MSBN am Objekt Messlokation)"}}}>

### Antwort der Kündigung

<Schrittskizze sicht={{"label": "MSBA"}} zeilen={[{"art": "folge_ausloeser", "werte": ["55039"]}, {"art": "lesen_verarbeitung", "schnittstellen": [{"label": "Messlokation lesen"}, {"label": "Messstellenbetriebsvertrag lesen"}, {"label": "Zähler lesen"}, {"label": "Energieliefervertrag lesen"}]}, {"art": "senden", "label": "MSB (entspricht MSBN am Objekt Messlokation)", "weg": "AS4", "nachrichten": [{"nr": "55040", "titel": "Bestätigung Kündigung MSB"}, {"nr": "55041", "titel": "Ablehnung Kündigung MSB"}]}, {"art": "fortschreiben"}]} />

<div data-teil="pruefis">

**Prüfidentifikatoren**
- [55040](/schnittstellen/202604/pruefi/UTILMD/PI_55040) — Bestätigung Kündigung MSB · AS4
- [55041](/schnittstellen/202604/pruefi/UTILMD/PI_55041) — Ablehnung Kündigung MSB · AS4

</div>

**Ablauf**

<div data-ablauf>

<Stepper>
<ol>

<li data-teil="folge_ausloeser">

**Ausgelöst durch Eingang**
- [55039](/schnittstellen/202604/pruefi/UTILMD/PI_55039) — Kündigung MSB

Die MACO APP sendet diese Nachricht selbst, als Folgeprozess nach diesem Eingang.

</li>

<li data-teil="lesen" data-stufe="verarbeitung">

**Daten für die Verarbeitung laden**
- [Messlokation lesen](/api/202604/backend-lesen/getmeterlocationbasic#messlokation-lesen) `GET /getMeterLocationBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getMeterLocationBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_MESSLOKATION_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Messstellenbetriebsvertrag lesen](/api/202604/backend-lesen/getmeasuringpointoperationcontractbasic#messstellenbetriebsvertrag-lesen) `GET /getMeasuringPointOperationContractBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getMeasuringPointOperationContractBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_MESSSTELLENBETRIEBSVERTRAG_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Zähler lesen](/api/202604/backend-lesen/getcounterbasic#zahler-lesen) `GET /getCounterBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getCounterBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>
- [Energieliefervertrag lesen](/api/202604/backend-lesen/getenergysupplycontractbasic#energieliefervertrag-lesen) `GET /getEnergySupplyContractBasic` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/getEnergySupplyContractBasic"} method={"get"} queryParams={[{"name": "parameter1", "isRequired": true, "defaultValue": "74018657187", "defaultActive": true, "type": "string"}, {"name": "parameter2", "isRequired": true, "defaultValue": "MALO", "defaultActive": true, "enum": ["MALO", "MELO", "NELO", "TECHNISCHE_RESSOURCE", "STEUERBARE_RESOURCE", "TRANCHE"], "type": "string"}, {"name": "parameter3", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "parameter4", "isRequired": true, "defaultValue": "2024-06-28T12:18:00Z", "defaultActive": true, "type": "string"}, {"name": "command", "isRequired": false, "defaultValue": "SAP_LESEN_ENERGIELIEFERVERTRAG_BASIS", "type": "string"}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

</li>

<li data-teil="nachricht">

Nachricht an **MSB (entspricht MSBN am Objekt Messlokation)** · AS4

<div data-teil="antwortbaum">

**Antwort nach Entscheidungsbaum**
- `55040`, `55041` → [E_0200](/referenz/202604/ebd/E_0200) · Kündigung Messstellenbetrieb prüfen

</div>

</li>

<li data-teil="schnittstelle" data-art="fortschreiben">

**Schreibende Schnittstelle**
- Vorgang fortgeschrieben — [Prozessdaten aktualiseren](/api/202604/backend-schreiben-msb/updateprocessdata#prozessdaten-aktualiseren) `POST /updateProcessData` <OpenPlaygroundButton server={"https://mock.macoapp.de"} url={"/updateProcessData"} method={"post"} queryParams={[{"name": "command", "isRequired": true, "defaultValue": "AKTUALISIEREN_PROZESSDATEN", "defaultActive": true, "type": "string"}]} defaultBody={"{\n  \"stammdaten\": {\n    \"MESSLOKATION\": [\n      {\n        \"boTyp\": \"MESSLOKATION\",\n        \"messadresse\": {\n          \"gewerbekennzeichnung\": true,\n          \"hausnummer\": \"1\",\n          \"landescode\": \"DE\",\n          \"ort\": \"Ort\",\n          \"postleitzahl\": \"12345\",\n          \"strasse\": \"Str\",\n          \"zusatzInformation\": {\n            \"zusatz1\": \"Mustermann\"\n          }\n        },\n        \"messlokationsId\": \"DE0032106765712000000000000000037\",\n        \"versionStruktur\": \"1\"\n      }\n    ],\n    \"MESSSTELLENBETRIEBSVERTRAG\": [\n      {\n        \"boTyp\": \"VERTRAG\",\n        \"lokationsId\": \"DE0032106765712000000000000000037\",\n        \"lokationsTyp\": \"MELO\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\",\n        \"vertragsart\": \"MESSSTELLENBETRIEBSVERTRAG\",\n        \"vertragspartner2\": [\n          {\n            \"boTyp\": \"GESCHAEFTSPARTNER\",\n            \"geschaeftspartnerrolle\": [\n              \"KUNDE\"\n            ],\n            \"gewerbekennzeichnung\": false,\n            \"name1\": \"Mustermann\",\n            \"versionStruktur\": \"1\"\n          }\n        ]\n      }\n    ],\n    \"NETZNUTZUNGSVERTRAG\": [\n      {\n        \"boTyp\": \"VERTRAG\",\n        \"lokationsId\": \"DE0032106765712000000000000000037\",\n        \"lokationsTyp\": \"MELO\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\",\n        \"vertragsart\": \"NETZNUTZUNGSVERTRAG\",\n        \"vertragsende\": \"2025-06-30T22:00:00Z\"\n      }\n    ],\n    \"ZAEHLER\": [\n      {\n        \"boTyp\": \"ZAEHLER\",\n        \"messlokationsId\": \"DE0032106765712000000000000000037\",\n        \"sparte\": \"STROM\",\n        \"versionStruktur\": \"1\",\n        \"zaehlernummer\": \"EL001IK01013852469\"\n      }\n    ]\n  },\n  \"transaktionsdaten\": {\n    \"absender\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9904446000007\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"anfragereferenznummer\": \"12345678910\",\n    \"antwortstatus\": \"E15\",\n    \"antwortstatusCodeliste\": \"S_0090\",\n    \"datenaustauschreferenz\": \"371440\",\n    \"dokumentennummer\": \"242129BGM\",\n    \"empfaenger\": {\n      \"boTyp\": \"MARKTTEILNEHMER\",\n      \"rollencodenummer\": \"9904446000007\",\n      \"rollencodetyp\": \"BDEW\",\n      \"versionStruktur\": \"1\"\n    },\n    \"kategorie\": \"E35\",\n    \"nachrichtendatum\": \"2025-04-04T09:44:00Z\",\n    \"nachrichtenreferenznummer\": \"242129\",\n    \"pruefidentifikator\": \"55040\",\n    \"sparte\": \"STROM\",\n    \"transaktionsgrund\": \"E03\",\n    \"vertragsende\": \"2025-06-30T22:00:00Z\",\n    \"vorgangsnummer\": \"582426784\"\n  }\n}"} examples={[{"mediaType": "application/json", "examples": [{"name": "55040", "summary": "55040 — Bestätigung Kündigung MSB", "value": {"stammdaten": {"MESSLOKATION": [{"boTyp": "MESSLOKATION", "versionStruktur": "1", "messlokationsId": "DE0032106765712000000000000000037", "messadresse": {"postleitzahl": "12345", "ort": "Ort", "strasse": "Str", "hausnummer": "1", "gewerbekennzeichnung": true, "landescode": "DE", "zusatzInformation": {"zusatz1": "Mustermann"}}}], "NETZNUTZUNGSVERTRAG": [{"boTyp": "VERTRAG", "versionStruktur": "1", "vertragsart": "NETZNUTZUNGSVERTRAG", "sparte": "STROM", "vertragsende": "2025-06-30T22:00:00Z", "lokationsId": "DE0032106765712000000000000000037", "lokationsTyp": "MELO"}], "MESSSTELLENBETRIEBSVERTRAG": [{"boTyp": "VERTRAG", "versionStruktur": "1", "vertragsart": "MESSSTELLENBETRIEBSVERTRAG", "sparte": "STROM", "vertragspartner2": [{"boTyp": "GESCHAEFTSPARTNER", "geschaeftspartnerrolle": ["KUNDE"], "versionStruktur": "1", "gewerbekennzeichnung": false, "name1": "Mustermann"}], "lokationsId": "DE0032106765712000000000000000037", "lokationsTyp": "MELO"}], "ZAEHLER": [{"boTyp": "ZAEHLER", "versionStruktur": "1", "zaehlernummer": "EL001IK01013852469", "messlokationsId": "DE0032106765712000000000000000037", "sparte": "STROM"}]}, "transaktionsdaten": {"datenaustauschreferenz": "371440", "sparte": "STROM", "transaktionsgrund": "E03", "vorgangsnummer": "582426784", "pruefidentifikator": "55040", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9904446000007", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9904446000007", "rollencodetyp": "BDEW"}, "dokumentennummer": "242129BGM", "kategorie": "E35", "nachrichtendatum": "2025-04-04T09:44:00Z", "nachrichtenreferenznummer": "242129", "anfragereferenznummer": "12345678910", "antwortstatus": "E15", "antwortstatusCodeliste": "S_0090", "vertragsende": "2025-06-30T22:00:00Z"}}}, {"name": "55041", "summary": "55041 — Ablehnung Kündigung MSB", "value": {"stammdaten": {"MESSLOKATION": [{"boTyp": "MESSLOKATION", "versionStruktur": "1", "messlokationsId": "DE0032106765712000000000000000037"}], "ENERGIELIEFERVERTRAG": [{"boTyp": "ENERGIELIEFERVERTRAG", "versionStruktur": "1", "sparte": "STROM", "vertragskonditionen": {"kuendigungsfrist": {"zeitraumText": "30TM"}}}]}, "transaktionsdaten": {"datenaustauschreferenz": "132921", "sparte": "STROM", "transaktionsgrund": "E03", "vorgangsnummer": "4444444", "pruefidentifikator": "55041", "absender": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9904446000007", "rollencodetyp": "BDEW"}, "empfaenger": {"boTyp": "MARKTTEILNEHMER", "versionStruktur": "1", "rollencodenummer": "9906687000002", "rollencodetyp": "BDEW"}, "dokumentennummer": "838326BGM", "kategorie": "E35", "nachrichtendatum": "2025-10-05T10:38:00Z", "nachrichtenreferenznummer": "838326", "anfragereferenznummer": "12345678910", "antwortstatus": "Z12", "antwortstatusCodeliste": "S_0054", "gueltigAb": "2025-06-30T22:00:00Z"}}}]}]} security={[{"bearer": []}]}>Ausprobieren</OpenPlaygroundButton>

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
| [E_0200](/referenz/202604/ebd/E_0200) | Kündigung Messstellenbetrieb prüfen |

</details>

<a id="abschnitt-informationen"></a>

## Prozess-Informationen

Wortlaut der Lesefassung, Steckbrief Kap. 2.2.1, S. 18–19.

<Stepper>
<ol>

<li data-blatt="vorbedingungen">

### Vorbedingungen

Der MSBN besitzt die Vollmacht des AN bzw. ANN in dessen Namen die Kündigung vornehmen zu dürfen.

</li>

<li data-blatt="ergebnisse">

### Ergebnisse

- Bestätigung der Kündigung:
  - Der MSBA ist verpflichtet, unmittelbar mit Bestätigung der Kündigung gegenüber dem MSBN auch den Use-Case „[Ende Messstellenbetrieb](/prozessdoku/202604/MSB--MSBA/WiM-Teil1-ende-messstellenbetrieb)“ gegenüber dem NB anzustoßen.
  - Sofern die Übermittlung von Werten an den ESA durchgeführt wird, beendet der MSBA die Übermittlung von Werten an den ESA.
- Ablehnung der Kündigung: MSBA sieht den Messstellenbetriebsvertrag als nicht wirksam gekündigt an.

</li>

<li data-blatt="anforderungen">

### Weitere Anforderungen

- Ungeachtet der jederzeit bestehenden Möglichkeit des AN bzw. ANN, seinen Messstellenbetriebsvertrag schriftlich zu kündigen, darf der MSBA eine nach diesem Use-Case gemeldete Kündigung nicht allein unter Berufung auf die fehlende Einhaltung einer vertraglich vereinbarten Form zurückweisen. In diesem Fall hat er eine Kündigung auch in elektronischer Form unter Anwendung dieses Use-Case entgegenzunehmen und zu bearbeiten. Hinweis:
- Der Use-Case behandelt nicht den Fall, dass der AN bzw. ANN selbst gegenüber dem MSBA den Messstellenbetriebsvertrag kündigt.
- Wenn der AN bzw. ANN vorab selbst kündigt, ist der Use-Case „[Ende Messstellenbetrieb](/prozessdoku/202604/MSB--MSBA/WiM-Teil1-ende-messstellenbetrieb)“ vom MSBA gegenüber dem NB unmittelbar mit Verfassen der Kündigungsbestätigung an den AN bzw. ANN anzustoßen.

</li>

<li data-blatt="erste-nachricht">

### Erste Nachricht

**MSB (entspricht MSBN am Objekt Messlokation)** sendet „Kündigung“ (Schritt 1). Ab hier ist der Beteiligte dieser Seite am Zug.

</li>

<li data-blatt="ziel">

### Ziel

Der zwischen AN bzw. ANN und MSBA abgeschlossene Messstellenbetriebsvertrag für die genannte Messlokation ist gekündigt.

</li>

</ol>
</Stepper>

<a id="abschnitt-sichten"></a>

## Andere Sichten des Prozesses

Derselbe Prozess, aus den Augen der anderen Beteiligten: dieselben Schritte, jeweils aus deren Sicht gelesen.

- [Sicht MSBN](/prozessdoku/202604/MSB--MSBN/WiM-Teil1-kuendigung-messstellenbetrieb) — der aufnehmende MSB · Marktrolle MSB

<Hinweisbereich>

*Die Schritte sind die **möglichen** Nachrichten dieses Prozesses, keine Abfolge — die Quelle führt weder Bedingungen noch Alternativen. Das Kästchen am Schritt nennt links die eigene Sicht: **←** empfängt sie, **→** sendet sie. Zugeklappte Schritte laufen zwischen anderen Marktpartnern.*

</Hinweisbereich>
