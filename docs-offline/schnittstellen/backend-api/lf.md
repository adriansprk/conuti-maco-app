# Backend-API — LF

Das Backend eines LF bedient zwei Gruppen von Aufrufen. Die erste gilt nur für diese Rolle; die zweite ist für LF, NB und MSB wortgleich dieselbe und steht vollständig unter [Für alle Rollen](/schnittstellen/backend-api/rollenneutral).

## Nur für LF

| Operation | Bereich | Aufruf | deutsche Benennung | Quellen | Regeln LF |
|---|---|---|---|---|---|
| Identifikation einer Marktlokation | MaloIdent LF (Backend) | `POST /inbound` | `/core/inbound` | maco-api.yaml · maloident-macoapp.json · doc.macoapp.de | — |
| Prozessdaten aktualisieren | MaloIdent LF (Backend) | `POST /updateProcessData` | — | maco-api.yaml · doc.macoapp.de | — |
| Prozessdaten aktualiseren | Prozessdaten LF (Backend) | `POST /prozessdaten/lf/update` | — | maco-api.yaml · doc.macoapp.de | — |
| Prozessdaten erstellen | Prozessdaten LF (Backend) | `POST /prozessdaten/lf/create` | `/erstellenProzessdaten` | maco-api.yaml · macoapp-schreiben.json · doc.macoapp.de | — |

### Identifikation einer Marktlokation

Triggert den Versand einer MaloIdent Anfrage via API-Webdienst an den Netzbetreiber durch die MaloIdent APP. Die Anfrage wird identifiziert durch den Eventnamen **START_MALOIDENT**. Zusätzlich ist eine eindeutige ID **prozessId** aus dem Backend mit zu übergeben, mit der die spätere Antwort vom Netzbetreiber wieder an das Backend übergeben werden kann.

| Was | Aufruf | Kommando | Quelle |
|---|---|---|---|
| deutsche Benennung | `POST /core/inbound` | `START_MALOIDENT` | `maloident-macoapp.json` |
| ausgelieferte Benennung | `POST /inbound` | `START_MALOIDENT` | `doc.macoapp.de` |
| rollengegliederte Benennung | `POST /inbound` | `MALOIDENT_IDENTIFIKATION_EINER_MARKTLOKATION` | `maco-api.yaml` |

**Rolle:** LF — belegt durch doc.macoapp.de.

**Anfragekörper:** `object`

**Antwort (200):** `object`

*Entspricht in doc.macoapp.de:* „Identifikation einer Marktlokation“ im Zweig „MaloIdent LF (Backend)“ (`identifikation-einer-marktlokation-16024919e0`)

### Prozessdaten aktualisieren

| Was | Aufruf | Kommando | Quelle |
|---|---|---|---|
| ausgelieferte Benennung | `POST /updateProcessData` | `AKTUALISIEREN_PROZESSDATEN` | `doc.macoapp.de` |
| rollengegliederte Benennung | `POST /updateProcessData` | `MALOIDENT_PROZESSDATEN_AKTUALISIEREN` | `maco-api.yaml` |

**Rolle:** LF — belegt durch doc.macoapp.de.

**Anfragekörper:** `object`

**Antwort (200):** `object`

*Entspricht in doc.macoapp.de:* „Prozessdaten aktualisieren“ im Zweig „MaloIdent LF (Backend)“ (`prozessdaten-aktualisieren-15106071e0`)

### Prozessdaten aktualiseren

| Was | Aufruf | Kommando | Quelle |
|---|---|---|---|
| ausgelieferte Benennung | `POST /updateProcessData` | `AKTUALISIEREN_PROZESSDATEN` | `doc.macoapp.de` |
| rollengegliederte Benennung | `POST /prozessdaten/lf/update` | `PROZESSDATEN_UPDATE_LF` | `maco-api.yaml` |

**Rolle:** LF — belegt durch doc.macoapp.de und maco-api.yaml.

**Anfragekörper:** `ProcessData`

**Antwort (200):** `object`

*Entspricht in doc.macoapp.de:* „Prozessdaten aktualiseren“ im Zweig „Prozessdaten LF (Backend)“ (`prozessdaten-aktualiseren-14017182e0`)

### Prozessdaten erstellen

Verbuchung von Daten aus Marktprozesen im Backend

| Was | Aufruf | Kommando | Quelle |
|---|---|---|---|
| deutsche Benennung | `POST /erstellenProzessdaten` | `ERSTELLEN_PROZESSDATEN` | `macoapp-schreiben.json` |
| ausgelieferte Benennung | `POST /createProcessData` | `ERSTELLEN_PROZESSDATEN` | `doc.macoapp.de` |
| rollengegliederte Benennung | `POST /prozessdaten/lf/create` | `PROZESSDATEN_CREATE_LF` | `maco-api.yaml` |

**Rolle:** LF — belegt durch doc.macoapp.de und maco-api.yaml.

:::note{title="Drei Namen für einen Aufruf"}

Die drei Quellen benennen diesen Aufruf verschieden. Verbindlich für die BPMN-Diagramme dieser Doku ist die deutsche Benennung: die Diagramme sind mit ihr beschriftet.

:::

**Anfragekörper:** `ProcessData`

**Antwort (200):** `object`

*Entspricht in doc.macoapp.de:* „Prozessdaten erstellen“ im Zweig „Prozessdaten LF (Backend)“ (`prozessdaten-erstellen-14017183e0`)

## Für alle Rollen gleich

Diese 32 Operationen nennt keine Quelle rollengebunden — ein LF stellt sie genauso bereit wie jede andere Rolle. Die letzte Spalte zählt, an wie vielen Regeln der LF-Konnektortabelle sie tatsächlich aufgerufen werden (Formatversion 202604).

| Operation | Bereich | Aufruf | deutsche Benennung | Quellen | Regeln LF |
|---|---|---|---|---|---|
| Avis lesen | BO4E Lesen (Backend) | `GET /getAvisBasic` | `/lesenAvisBasis` | maco-api.yaml · macoapp-lesen.json · doc.macoapp.de | — |
| Berechnungsformel lesen | BO4E Lesen (Backend) | `GET /getCalculationFormulaBasic` | `/lesenBerechnungsformelBasis` | maco-api.yaml · macoapp-lesen.json · doc.macoapp.de | 1 |
| Bilanzierung lesen | BO4E Lesen (Backend) | `GET /getAccountingBasic` | `/lesenBilanzierungBasis` | maco-api.yaml · macoapp-lesen.json · doc.macoapp.de | 13 |
| Energieliefervertrag lesen | BO4E Lesen (Backend) | `GET /getEnergySupplyContractBasic` | `/lesenEnergieliefervertragBasis` | maco-api.yaml · macoapp-lesen.json · doc.macoapp.de | — |
| Energiemengen aus Abrechnungskontext lesen | BO4E Lesen (Backend) | `GET /getEnergyAmount` | `/lesenEnergiemengeEnergiemenge` | maco-api.yaml · macoapp-lesen.json · doc.macoapp.de | 2 |
| Kommunikationsdaten des Serviceanbieters lesen | BO4E Lesen (Backend) | `GET /getCommunicationDataBasic` | `/lesenKommunikationsdatenBasis` | maco-api.yaml · macoapp-lesen.json · doc.macoapp.de | — |
| Lastgangs einer Lokation lesen | BO4E Lesen (Backend) | `GET /getEnergyAmountLoadCurve` | `/lesenEnergiemengeLastgang` | maco-api.yaml · macoapp-lesen.json · doc.macoapp.de | 2 |
| Leistungskurvendefinition lesen | BO4E Lesen (Backend) | `GET /getDefinitionPerformance` | — | doc.macoapp.de | — |
| Lokationsbündel lesen | BO4E Lesen (Backend) | `GET /getLocationBundleBasic` | `/lesenLokationsbundBasis` | maco-api.yaml · macoapp-lesen.json · doc.macoapp.de | 2 |
| Marktlokation lesen | BO4E Lesen (Backend) | `GET /getMarketLocationBasic` | `/lesenMarktlokationBasis` | maco-api.yaml · macoapp-lesen.json · doc.macoapp.de | 65 |
| Messlokation lesen | BO4E Lesen (Backend) | `GET /getMeterLocationBasic` | `/lesenMesslokationBasis` | maco-api.yaml · macoapp-lesen.json · doc.macoapp.de | 18 |
| Messstellenbetriebsvertrag lesen | BO4E Lesen (Backend) | `GET /getMeasuringPointOperationContractBasic` | `/lesenMessstellenbetriebsvertragBasis` | maco-api.yaml · macoapp-lesen.json · doc.macoapp.de | — |
| Netzlokation lesen | BO4E Lesen (Backend) | `GET /getGridLocationBasic` | `/lesenNetzlokationBasis` | maco-api.yaml · macoapp-lesen.json · doc.macoapp.de | 15 |
| Netznutzungsvertrag lesen | BO4E Lesen (Backend) | `GET /getGridUsageContractBasic` | `/lesenNetznutzungsvertragBasis` | maco-api.yaml · macoapp-lesen.json · doc.macoapp.de | — |
| Preisblatt lesen | BO4E Lesen (Backend) | `GET /getPriceSheetBasic` | — | maco-api.yaml · doc.macoapp.de | 1 |
| Schaltzeitdefinition lesen | BO4E Lesen (Backend) | `GET /getDefinitionSwitch` | — | doc.macoapp.de | — |
| Steuerbare Ressource lesen | BO4E Lesen (Backend) | `GET /getControllableResourceBasic` | `/lesenSteuerbareRessourceBasis` | maco-api.yaml · macoapp-lesen.json · doc.macoapp.de | 4 |
| Technische Ressource lesen | BO4E Lesen (Backend) | `GET /getTechnicalResourceBasic` | `/lesenTechnischeRessourceBasis` | maco-api.yaml · macoapp-lesen.json · doc.macoapp.de | 3 |
| Tranche lesen | BO4E Lesen (Backend) | `GET /getTrancheBasic` | `/lesenTrancheBasis` | maco-api.yaml · macoapp-lesen.json · doc.macoapp.de | 12 |
| Zaehlzeitdefinition lesen | BO4E Lesen (Backend) | `GET /getDefinitionCounting` | — | doc.macoapp.de | — |
| Zähler lesen | BO4E Lesen (Backend) | `GET /getCounterBasic` | `/lesenZaehlerBasis` | maco-api.yaml · macoapp-lesen.json · doc.macoapp.de | 14 |
| Zählerstand einer Lokation lesen | BO4E Lesen (Backend) | `GET /getEnergyAmountMeterReading` | `/lesenEnergiemengeZaehlerstand` | maco-api.yaml · macoapp-lesen.json · doc.macoapp.de | 2 |
| Empfang einer Marktnachricht | MCS-Eingang | `POST /receive` | — | maco-api.yaml | — |
| Absenderdaten lesen | Obsolet | `GET /lesenMarktteilnehmerAbsender` | `/lesenMarktteilnehmerAbsender` | maco-api.yaml · macoapp-lesen.json | — |
| Empfängerdaten lesen | Obsolet | `GET /lesenMarktteilnehmerEmpfaenger` | `/lesenMarktteilnehmerEmpfaenger` | maco-api.yaml · macoapp-lesen.json | — |
| Verwendungszeitraum einer Marktlokation ermitteln | Obsolet | `GET /getMarketlokationAllocationPeriod` | — | maco-api.yaml | — |
| Zuordnungsemächtigung lesen (UNKNOWN) | Prozessdaten | `POST /prozessdaten/unknown/update` | — | maco-api.yaml | — |
| Zuordnungsemächtigung lesen | Prozessdaten lesen (Backend) | `GET /getAllocationAuthorization` | — | doc.macoapp.de | — |
| LESEN_MARKTLOKATION_VERWENDUNGSZEITRAUM | nur macoapp-lesen.json | `GET /lesenMarktlokationVerwendungszeitraum` | `/lesenMarktlokationVerwendungszeitraum` | macoapp-lesen.json | — |
| AKTUALISIEREN_MDOC_BASIS | nur macoapp-schreiben.json | `POST /aktualisierenMdocBasis` | `/aktualisierenMdocBasis` | macoapp-schreiben.json | — |
| ERSTELLEN_PROZESSDATEN_MALOIDENTANTWORT_NEGATIV | nur maloident-lieferant.json | `POST /erstellenProzessdatenMaloidentantwortNegativ` | `/erstellenProzessdatenMaloidentantwortNegativ` | maloident-lieferant.json | — |
| ERSTELLEN_PROZESSDATEN_MALOIDENTANTWORT_POSITIV | nur maloident-lieferant.json | `POST /erstellenProzessdatenMaloidentantwortPositiv` | `/erstellenProzessdatenMaloidentantwortPositiv` | maloident-lieferant.json | — |

## Fehler und Wiederholung

Die sechste der Fragen, die diese Seiten ausgeloest haben: was geschieht, wenn euer Backend auf einen Callback mit einem Fehler antwortet.

### Was euer Backend antwortet

Die Spezifikation kennt genau drei Antworten, und sie kennt sie fuer `createProcessData` und `updateProcessData` gleichermassen — gemessen ueber alle drei Rollen und beide Formatversionen:

| Code | Bedeutung | Rumpf |
|---|---|---|
| `200` | angenommen | **keiner** — „200 ok“ heißt kein Rumpf |
| `400` | die Anfrage ist fehlerhaft | `ProblemDetails` nach RFC 9457 |
| `422` | die Anfrage ist verstanden, aber fachlich nicht verarbeitbar | `ProblemDetails` nach RFC 9457 |

Alle 24 Fehlerantworten der sechs Kataloge tragen `ProblemDetails`; der Medientyp bleibt `application/json`.

### Ob die MACO APP wiederholt

**Beim Schreiben ins Backend nicht.** Gemessen am 05.09.2026 an der Verdrahtung des Konnektor-Flusses: in die Wiederholung laeuft dort allein der **Transportfehler** (Verbindung nicht zustande gekommen, Zeitueberschreitung), und zwar hoechstens dreimal. Eine **5xx**- und eine **4xx**-Antwort gehen ohne Wiederholung in die Fehlerbehandlung.

:::caution{title="Hier weicht die Messung von der muendlichen Auskunft ab"}

Auskunft des Betriebs: „bei 5xx drei Wiederholungen“. Das trifft nach dieser Messung auf den **lesenden** Aufruf ins Backend zu — dort laeuft die 5xx-Antwort ausdruecklich in dieselbe Wiederholung wie der Transportfehler, ebenfalls dreimal. Beim **schreibenden** Aufruf, also bei `createProcessData` und `updateProcessData`, tut sie es nicht.

Der lesende Fluss ist zugleich die Gegenkontrolle: dieselbe Auswertung findet die Wiederholungsbeziehung dort, die Abwesenheit im schreibenden Fluss ist also ein gemessener Unterschied und kein blinder Messfuehler.

**Wer auf eine Wiederholung baut, plant hier eine ein, die es nicht gibt.** Bis das gegen die laufende Instanz gegengeprueft ist, gilt die Messung.

:::

### Was stattdessen passiert

Was ein Fehler ausloest, ist **je Pruefidentifikator und je Schnittstelle** konfiguriert. Die Entscheidung steht in der Konnektortabelle `S_NACHRICHTEN_KONNEKTOR` der Prozess-Repositorien, in der Spalte „Verhalten, wenn Fehler von API“.

| Wert | Wirkung | Wie oft er tatsaechlich gesetzt ist |
|---|---|---|
| `IGNORIEREN` | der Prozess laeuft weiter | 9 837 Regeln |
| `AUFGABE-SB` | eine Aufgabe fuer die Sachbearbeitung entsteht | 3 364 Regeln |
| `AUFGABE-PC` | eine Aufgabe fuer die Prozesscontrolle entsteht | 25 Regeln |
| `ABBRECHEN` | der Prozess bricht ab | **0 Regeln** — der Wert ist zugelassen und wird nirgends benutzt |

Gemessen ueber die 15 Konnektortabellen der drei Rollen und aller Fassungen. Dass `ABBRECHEN` in der Werteliste steht, sagt also nur, dass es moeglich waere; gesetzt ist es an keiner einzigen Regel. Was nicht ignoriert wird, wird zur **Aufgabe**.

Die Aufgabe erscheint im **Klaerfallmonitor** der Oberflaeche (`/clearcaseMonitorOpen`, Gruppe „Sachbearbeitung“), wo sie ein Mensch entscheidet — wiederholen, abbrechen oder beenden. Der Abbruch ist damit die Wahl eines Sachbearbeiters in der Aufgabe und keine Voreinstellung der Tabelle.

:::note{title="Sichtbarkeit der Fehlerantwort"}

Die Fehlerantwort ist am Vorgang sichtbar. Auskunft des Betriebs, gegen die laufende Instanz ungeprueft. Der Absprung auf den Vorgang steht unter [Schluessel und Zuordnung](/schnittstellen/schluessel).

:::
