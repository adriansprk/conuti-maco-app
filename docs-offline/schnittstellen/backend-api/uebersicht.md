# Backend-API

Die MACO APP führt die Marktkommunikation, hält die Daten aber nicht. Sie liest sie aus dem Backend des Kunden und schreibt die Ergebnisse dorthin zurück. Diese Seite und die vier Rollenseiten daneben beschreiben, was dieses Backend dafür bereitstellen muss.

Der Bestand: **42 Operationen**, davon **10 an eine Marktrolle gebunden** und **32 für alle Rollen gleich**. Die abzulösende Doku doc.macoapp.de widmet ihnen 38 Seiten — 64,2 % ihres gesamten Umfangs.

## Zwei Namen für denselben Aufruf

Die Quellen benennen dieselbe Operation verschieden, und keine der Benennungen ist falsch. Diese Doku zeigt beide und schreibt dazu, welche Quelle welche nennt.

| deutsche Benennung | ausgelieferte Benennung |
|---|---|
| `/core/inbound` | `/inbound` |
| `/lesenAvisBasis` | `/getAvisBasic` |
| `/lesenBerechnungsformelBasis` | `/getCalculationFormulaBasic` |
| `/lesenBilanzierungBasis` | `/getAccountingBasic` |
| `/lesenEnergieliefervertragBasis` | `/getEnergySupplyContractBasic` |
| `/lesenEnergiemengeEnergiemenge` | `/getEnergyAmount` |
| `/lesenEnergiemengeLastgang` | `/getEnergyAmountLoadCurve` |
| `/lesenEnergiemengeZaehlerstand` | `/getEnergyAmountMeterReading` |
| `/lesenKommunikationsdatenBasis` | `/getCommunicationDataBasic` |
| `/lesenLokationsbundBasis` | `/getLocationBundleBasic` |
| `/lesenMaloidentBasis` | `/identifyMarketlocation` |
| `/lesenMaloidentMarktlokation` | `/getMaloidentMarketlocation` |
| `/lesenMarktlokationBasis` | `/getMarketLocationBasic` |
| `/lesenMesslokationBasis` | `/getMeterLocationBasic` |
| `/lesenMessstellenbetriebsvertragBasis` | `/getMeasuringPointOperationContractBasic` |
| `/lesenNetzlokationBasis` | `/getGridLocationBasic` |
| `/lesenNetznutzungsvertragBasis` | `/getGridUsageContractBasic` |
| `/lesenSteuerbareRessourceBasis` | `/getControllableResourceBasic` |
| `/lesenTechnischeRessourceBasis` | `/getTechnicalResourceBasic` |
| `/lesenTrancheBasis` | `/getTrancheBasic` |
| `/lesenZaehlerBasis` | `/getCounterBasic` |

21 Paare, verbunden über die identische `operationId` — kein Namensabgleich, kein Schätzverfahren.

## Drei Namen für einen Aufruf

Für 3 Operationen nennt jede der drei Quellen einen eigenen Pfad. Verbindlich für die BPMN-Diagramme dieser Doku ist die deutsche Benennung: die Diagramme sind mit ihr beschriftet.

| Operation | Rolle | deutsch | ausgeliefert | rollengegliedert |
|---|---|---|---|---|
| Prozessdaten erstellen | LF | `/erstellenProzessdaten` | `/createProcessData` | `/prozessdaten/lf/create` |
| Prozessdaten erstellen | MSB | `/erstellenProzessdaten` | `/createProcessData` | `/prozessdaten/msb/create` |
| Prozessdaten erstellen | NB | `/erstellenProzessdaten` | `/createProcessData` | `/prozessdaten/nb/create` |

## Woher die Rollengliederung stammt

Nicht aus den `_build`-Specs. Von ihren 29 Operationen nennt genau **2** überhaupt ein Rollenwort, und beide nur in der Prosa. Die Rolle steht in `maco-api.yaml` — als Tag `Trigger-LF/NB/MSB` und als Pfadschnitt `/prozessdaten/{lf,nb,msb}/` — und in den Zweignamen der abzulösenden Doku. Beide werden gelesen; zurückgerechnet wird nichts.

## Das Kommando

Jede Leseoperation nimmt zusätzlich einen Parameter `command`. Sein Wert ist die `operationId` — und die ist zugleich das Kommando des Camunda-Konnektors. `maco-api.yaml` führt 50 solche Kommandos. Ein Backend, das einen generischen Endpunkt anbietet, unterscheidet daran, welche Operation gemeint ist.

## Wo nur die abzulösende Doku eine Spezifikation führt

Für 4 Operationen führt **keine gepflegte Spezifikation** einen Pfad — weder `maco-api.yaml` noch die `_build`-Specs. Bis zur Runde des Katalogs stand hier deshalb »Lücke«. Gemessen ist das zu viel gesagt: der gesicherte Export von doc.macoapp.de trägt für **alle vier** eine vollständige eingebettete OpenAPI, und der [Schnittstellen-Katalog](/api) liefert sie daraus aus.

| Operation | in doc.macoapp.de | im Katalog | Beinahetreffer |
|---|---|---|---|
| Leistungskurvendefinition lesen | `GET /getDefinitionPerformance` | [`/getDefinitionPerformance`](/api/202604/backend-lesen) | — |
| Schaltzeitdefinition lesen | `GET /getDefinitionSwitch` | [`/getDefinitionSwitch`](/api/202604/backend-lesen) | — |
| Zaehlzeitdefinition lesen | `GET /getDefinitionCounting` | [`/getDefinitionCounting`](/api/202604/backend-lesen) | — |
| Zuordnungsemächtigung lesen | `GET /getAllocationAuthorization` | [`/getAllocationAuthorization`](/api/202604/backend-lesen) | `POST /prozessdaten/unknown/update` |

Was bleibt, ist eine **Pflegelücke, keine Wissenslücke**: die beiden gepflegten Quellen kennen diese Aufrufe nicht, der ausgeliefernde Bestand schon. Zusammengelegt wird trotzdem nichts — der Beinahetreffer steht als Beinahetreffer da.

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

## Quellen dieser Seiten

| Quelle | Was sie beiträgt |
|---|---|
| `maco-api.yaml` | Rolle, ausgelieferte Benennung, Parameter, Schemata, Kommandos |
| die `_build`-Specs | die deutsche Benennung |
| doc.macoapp.de (gesicherter Export) | der Maßstab der Ablösung und die Brücke zwischen beiden Benennungen |
| die Konnektortabellen der Prozess-Repositorien | wie oft eine Rolle eine Operation tatsächlich aufruft |
