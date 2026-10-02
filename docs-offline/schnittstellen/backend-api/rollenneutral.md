# Backend-API — für alle Rollen

Diese 32 Operationen nennt **keine** der drei Quellen rollengebunden. Das ist der Kern des Befunds: die Backend-API der MACO APP ist fast vollständig rollenneutral — ein LF, ein NB und ein MSB stellen dieselben Aufrufe bereit. Unterschiedlich ist nur, wie oft eine Rolle sie braucht, und das steht auf den Rollenseiten.

| Operation | Bereich | Aufruf | deutsche Benennung | Quellen |
|---|---|---|---|---|
| Avis lesen | BO4E Lesen (Backend) | `GET /getAvisBasic` | `/lesenAvisBasis` | maco-api.yaml · macoapp-lesen.json · doc.macoapp.de |
| Berechnungsformel lesen | BO4E Lesen (Backend) | `GET /getCalculationFormulaBasic` | `/lesenBerechnungsformelBasis` | maco-api.yaml · macoapp-lesen.json · doc.macoapp.de |
| Bilanzierung lesen | BO4E Lesen (Backend) | `GET /getAccountingBasic` | `/lesenBilanzierungBasis` | maco-api.yaml · macoapp-lesen.json · doc.macoapp.de |
| Energieliefervertrag lesen | BO4E Lesen (Backend) | `GET /getEnergySupplyContractBasic` | `/lesenEnergieliefervertragBasis` | maco-api.yaml · macoapp-lesen.json · doc.macoapp.de |
| Energiemengen aus Abrechnungskontext lesen | BO4E Lesen (Backend) | `GET /getEnergyAmount` | `/lesenEnergiemengeEnergiemenge` | maco-api.yaml · macoapp-lesen.json · doc.macoapp.de |
| Kommunikationsdaten des Serviceanbieters lesen | BO4E Lesen (Backend) | `GET /getCommunicationDataBasic` | `/lesenKommunikationsdatenBasis` | maco-api.yaml · macoapp-lesen.json · doc.macoapp.de |
| Lastgangs einer Lokation lesen | BO4E Lesen (Backend) | `GET /getEnergyAmountLoadCurve` | `/lesenEnergiemengeLastgang` | maco-api.yaml · macoapp-lesen.json · doc.macoapp.de |
| Leistungskurvendefinition lesen | BO4E Lesen (Backend) | `GET /getDefinitionPerformance` | — | doc.macoapp.de |
| Lokationsbündel lesen | BO4E Lesen (Backend) | `GET /getLocationBundleBasic` | `/lesenLokationsbundBasis` | maco-api.yaml · macoapp-lesen.json · doc.macoapp.de |
| Marktlokation lesen | BO4E Lesen (Backend) | `GET /getMarketLocationBasic` | `/lesenMarktlokationBasis` | maco-api.yaml · macoapp-lesen.json · doc.macoapp.de |
| Messlokation lesen | BO4E Lesen (Backend) | `GET /getMeterLocationBasic` | `/lesenMesslokationBasis` | maco-api.yaml · macoapp-lesen.json · doc.macoapp.de |
| Messstellenbetriebsvertrag lesen | BO4E Lesen (Backend) | `GET /getMeasuringPointOperationContractBasic` | `/lesenMessstellenbetriebsvertragBasis` | maco-api.yaml · macoapp-lesen.json · doc.macoapp.de |
| Netzlokation lesen | BO4E Lesen (Backend) | `GET /getGridLocationBasic` | `/lesenNetzlokationBasis` | maco-api.yaml · macoapp-lesen.json · doc.macoapp.de |
| Netznutzungsvertrag lesen | BO4E Lesen (Backend) | `GET /getGridUsageContractBasic` | `/lesenNetznutzungsvertragBasis` | maco-api.yaml · macoapp-lesen.json · doc.macoapp.de |
| Preisblatt lesen | BO4E Lesen (Backend) | `GET /getPriceSheetBasic` | — | maco-api.yaml · doc.macoapp.de |
| Schaltzeitdefinition lesen | BO4E Lesen (Backend) | `GET /getDefinitionSwitch` | — | doc.macoapp.de |
| Steuerbare Ressource lesen | BO4E Lesen (Backend) | `GET /getControllableResourceBasic` | `/lesenSteuerbareRessourceBasis` | maco-api.yaml · macoapp-lesen.json · doc.macoapp.de |
| Technische Ressource lesen | BO4E Lesen (Backend) | `GET /getTechnicalResourceBasic` | `/lesenTechnischeRessourceBasis` | maco-api.yaml · macoapp-lesen.json · doc.macoapp.de |
| Tranche lesen | BO4E Lesen (Backend) | `GET /getTrancheBasic` | `/lesenTrancheBasis` | maco-api.yaml · macoapp-lesen.json · doc.macoapp.de |
| Zaehlzeitdefinition lesen | BO4E Lesen (Backend) | `GET /getDefinitionCounting` | — | doc.macoapp.de |
| Zähler lesen | BO4E Lesen (Backend) | `GET /getCounterBasic` | `/lesenZaehlerBasis` | maco-api.yaml · macoapp-lesen.json · doc.macoapp.de |
| Zählerstand einer Lokation lesen | BO4E Lesen (Backend) | `GET /getEnergyAmountMeterReading` | `/lesenEnergiemengeZaehlerstand` | maco-api.yaml · macoapp-lesen.json · doc.macoapp.de |
| Empfang einer Marktnachricht | MCS-Eingang | `POST /receive` | — | maco-api.yaml |
| Absenderdaten lesen | Obsolet | `GET /lesenMarktteilnehmerAbsender` | `/lesenMarktteilnehmerAbsender` | maco-api.yaml · macoapp-lesen.json |
| Empfängerdaten lesen | Obsolet | `GET /lesenMarktteilnehmerEmpfaenger` | `/lesenMarktteilnehmerEmpfaenger` | maco-api.yaml · macoapp-lesen.json |
| Verwendungszeitraum einer Marktlokation ermitteln | Obsolet | `GET /getMarketlokationAllocationPeriod` | — | maco-api.yaml |
| Zuordnungsemächtigung lesen (UNKNOWN) | Prozessdaten | `POST /prozessdaten/unknown/update` | — | maco-api.yaml |
| Zuordnungsemächtigung lesen | Prozessdaten lesen (Backend) | `GET /getAllocationAuthorization` | — | doc.macoapp.de |
| LESEN_MARKTLOKATION_VERWENDUNGSZEITRAUM | nur macoapp-lesen.json | `GET /lesenMarktlokationVerwendungszeitraum` | `/lesenMarktlokationVerwendungszeitraum` | macoapp-lesen.json |
| AKTUALISIEREN_MDOC_BASIS | nur macoapp-schreiben.json | `POST /aktualisierenMdocBasis` | `/aktualisierenMdocBasis` | macoapp-schreiben.json |
| ERSTELLEN_PROZESSDATEN_MALOIDENTANTWORT_NEGATIV | nur maloident-lieferant.json | `POST /erstellenProzessdatenMaloidentantwortNegativ` | `/erstellenProzessdatenMaloidentantwortNegativ` | maloident-lieferant.json |
| ERSTELLEN_PROZESSDATEN_MALOIDENTANTWORT_POSITIV | nur maloident-lieferant.json | `POST /erstellenProzessdatenMaloidentantwortPositiv` | `/erstellenProzessdatenMaloidentantwortPositiv` | maloident-lieferant.json |

### Avis lesen

Lesen des Avises mittels Avisnummer (Parameter1) zum Zeitpunkt (Parameter2) Reading the avis via avisnumber (Parameter1) at the time (Parameter2)

| Was | Aufruf | Kommando | Quelle |
|---|---|---|---|
| deutsche Benennung | `GET /lesenAvisBasis` | `LESEN_AVIS_BASIS` | `macoapp-lesen.json` |
| ausgelieferte Benennung | `GET /getAvisBasic` | `LESEN_AVIS_BASIS` | `doc.macoapp.de` |
| rollengegliederte Benennung | `GET /getAvisBasic` | `LESEN_AVIS` | `maco-api.yaml` |

| Parameter | Ort | Pflicht | Bedeutung |
|---|---|---|---|
| parameter1 | query | ja | avisNummer \| avis Number |
| command | query | nein | Entspricht der operationId dieser Schnittstelle. Diese Operation Id entspricht dem Command im Camunda Konnektor Prozess. Wenn das Backend einen generischen Endpunkt bereitstellt, kann dieses Command gentutzt werden um zu definieren welche Operation ausgeführt werden soll. |

**Antwort (200):** `Avis`

**Regeln der Konnektortabellen, die diesen Aufruf auslösen:** NB 1

*Entspricht in doc.macoapp.de:* „Avis lesen“ im Zweig „BO4E Lesen (Backend)“ (`avis-lesen-14017011e0`)

### Berechnungsformel lesen

Lesen des Berechnunungsformel einer Lokation (Parameter1) vom Typ (Parameter2 - default MALO) zum Stichtag (Parameter3)

| Was | Aufruf | Kommando | Quelle |
|---|---|---|---|
| deutsche Benennung | `GET /lesenBerechnungsformelBasis` | `LESEN_BRECHNUNGSFORMEL_BASIS` | `macoapp-lesen.json` |
| ausgelieferte Benennung | `GET /getCalculationFormulaBasic` | `LESEN_BRECHNUNGSFORMEL_BASIS` | `doc.macoapp.de` |
| rollengegliederte Benennung | `GET /getCalculationFormulaBasic` | `LESEN_BERECHNUNGSFORMEL` | `maco-api.yaml` |

| Parameter | Ort | Pflicht | Bedeutung |
|---|---|---|---|
| parameter1 | query | ja | LokationsId |
| parameter2 | query | ja | LokationsTyp |
| parameter3 | query | ja | Datum (Gültig ab) oder Stichtag, wenn parameter4 nicht gesetzt |
| parameter4 | query | nein | Datum (Gültig bis) |
| command | query | nein | Entspricht der operationId dieser Schnittstelle. Diese Operation Id entspricht dem Command im Camunda Konnektor Prozess. Wenn das Backend einen generischen Endpunkt bereitstellt, kann dieses Command gentutzt werden um zu definieren welche Operation ausgeführt werden soll. |

**Antwort (200):** `Berechnungsformel`

**Regeln der Konnektortabellen, die diesen Aufruf auslösen:** LF 1

*Entspricht in doc.macoapp.de:* „Berechnungsformel lesen“ im Zweig „BO4E Lesen (Backend)“ (`berechnungsformel-lesen-14017012e0`)

### Bilanzierung lesen

Lesen einer Bilanzierung mittels LokationsId (Parameter1) zum Zeitpunkt (Parameter3)

| Was | Aufruf | Kommando | Quelle |
|---|---|---|---|
| deutsche Benennung | `GET /lesenBilanzierungBasis` | `LESEN_BILANZIERUNG_BASIS` | `macoapp-lesen.json` |
| ausgelieferte Benennung | `GET /getAccountingBasic` | `LESEN_BILANZIERUNG_BASIS` | `doc.macoapp.de` |
| rollengegliederte Benennung | `GET /getAccountingBasic` | `LESEN_BILANZIERUNG` | `maco-api.yaml` |

| Parameter | Ort | Pflicht | Bedeutung |
|---|---|---|---|
| parameter1 | query | ja | LokationsId |
| parameter2 | query | ja | LokationsTyp |
| parameter3 | query | ja | Datum (Gültig ab) oder Stichtag, wenn parameter4 nicht gesetzt |
| parameter4 | query | ja | Datum (Gültig bis) |
| command | query | nein | Entspricht der operationId dieser Schnittstelle. Diese Operation Id entspricht dem Command im Camunda Konnektor Prozess. Wenn das Backend einen generischen Endpunkt bereitstellt, kann dieses Command gentutzt werden um zu definieren welche Operation ausgeführt werden soll. |

**Antwort (200):** `Bilanzierung`

**Regeln der Konnektortabellen, die diesen Aufruf auslösen:** LF 13 · MSB 1 · NB 25

*Entspricht in doc.macoapp.de:* „Bilanzierung lesen“ im Zweig „BO4E Lesen (Backend)“ (`bilanzierung-lesen-14017013e0`)

### Energieliefervertrag lesen

Lesen des Energieliefervertrages einer Lokation (Parameter1) vom Typ (Parameter2 - default MALO) zum Stichtag (Parameter3) | Reading the energy delivery contract of a location (Parameter1) at the time (Parameter2)

| Was | Aufruf | Kommando | Quelle |
|---|---|---|---|
| deutsche Benennung | `GET /lesenEnergieliefervertragBasis` | `LESEN_ENERGIELIEFERVERTRAG_BASIS` | `macoapp-lesen.json` |
| ausgelieferte Benennung | `GET /getEnergySupplyContractBasic` | `LESEN_ENERGIELIEFERVERTRAG_BASIS` | `doc.macoapp.de` |
| rollengegliederte Benennung | `GET /getEnergySupplyContractBasic` | `LESEN_VERTRAG` | `maco-api.yaml` |

| Parameter | Ort | Pflicht | Bedeutung |
|---|---|---|---|
| parameter1 | query | ja | LokationsId |
| parameter2 | query | ja | LokationsTyp |
| parameter3 | query | ja | Datum (Gültig ab) oder Stichtag, wenn parameter4 nicht gesetzt |
| parameter4 | query | ja | Datum (Gültig bis) |
| command | query | nein | Entspricht der operationId dieser Schnittstelle. Diese Operation Id entspricht dem Command im Camunda Konnektor Prozess. Wenn das Backend einen generischen Endpunkt bereitstellt, kann dieses Command gentutzt werden um zu definieren welche Operation ausgeführt werden soll. |

**Antwort (200):** `Vertrag`

*Entspricht in doc.macoapp.de:* „Energieliefervertrag lesen“ im Zweig „BO4E Lesen (Backend)“ (`energieliefervertrag-lesen-14017014e0`)

### Energiemengen aus Abrechnungskontext lesen

Lesen der Energiemengen aus Abrechnungskontext über eine LokationId (Parameter1) udn LokationsTyp (Parameter2) in einer Range (Parameter3/Parameter4) und einer OBIS Kennzahl (Parameter5 optional) | Reading an energy quantity for a location (Parameter1) in a range (Parameter2/Parameter3) and an OBIS code (Parameter4 optional)

| Was | Aufruf | Kommando | Quelle |
|---|---|---|---|
| deutsche Benennung | `GET /lesenEnergiemengeEnergiemenge` | `LESEN_ENERGIEMENGE_ENERGIEMENGE` | `macoapp-lesen.json` |
| ausgelieferte Benennung | `GET /getEnergyAmount` | `LESEN_ENERGIEMENGE_ENERGIEMENGE` | `doc.macoapp.de` |
| rollengegliederte Benennung | `GET /getEnergyAmount` | `LESEN_ENERGIEMENGE` | `maco-api.yaml` |

| Parameter | Ort | Pflicht | Bedeutung |
|---|---|---|---|
| parameter1 | query | ja | LokationsId |
| parameter2 | query | ja | LokationsTyp |
| parameter3 | query | ja | Datum (Gültig ab) oder Stichtag, wenn parameter4 nicht gesetzt |
| parameter4 | query | ja | Datum (Gültig bis) |
| parameter5 | query | nein | OBIS Kennzahl |
| command | query | nein | Entspricht der operationId dieser Schnittstelle. Diese Operation Id entspricht dem Command im Camunda Konnektor Prozess. Wenn das Backend einen generischen Endpunkt bereitstellt, kann dieses Command gentutzt werden um zu definieren welche Operation ausgeführt werden soll. |

**Antwort (200):** `Energiemenge`

**Regeln der Konnektortabellen, die diesen Aufruf auslösen:** LF 2

*Entspricht in doc.macoapp.de:* „Energiemengen aus Abrechnungskontext lesen“ im Zweig „BO4E Lesen (Backend)“ (`energiemengen-aus-abrechnungskontext-lesen-14017015e0`)

### Kommunikationsdaten des Serviceanbieters lesen

Lesen der Kommunikationsdaten des Serviceanbieters (Parameter1) zum Zeitpunkt (Parameter2) | Reading the communication data of the service provider (Parameter1) at the time (Parameter2)

| Was | Aufruf | Kommando | Quelle |
|---|---|---|---|
| deutsche Benennung | `GET /lesenKommunikationsdatenBasis` | `LESEN_KOMMUNIKATIONSDATEN_BASIS` | `macoapp-lesen.json` |
| ausgelieferte Benennung | `GET /getCommunicationDataBasic` | `LESEN_KOMMUNIKATIONSDATEN_BASIS` | `doc.macoapp.de` |
| rollengegliederte Benennung | `GET /getCommunicationDataBasic` | `LESEN_KOMMUNIKATIONSDATEN` | `maco-api.yaml` |

| Parameter | Ort | Pflicht | Bedeutung |
|---|---|---|---|
| parameter1 | query | ja | ILN Nummer |
| parameter2 | query | ja | Stichtag |
| command | query | nein | Entspricht der operationId dieser Schnittstelle. Diese Operation Id entspricht dem Command im Camunda Konnektor Prozess. Wenn das Backend einen generischen Endpunkt bereitstellt, kann dieses Command gentutzt werden um zu definieren welche Operation ausgeführt werden soll. |

**Antwort (200):** `Kommunikationsdaten`

**Regeln der Konnektortabellen, die diesen Aufruf auslösen:** NB 2

*Entspricht in doc.macoapp.de:* „Kommunikationsdaten des Serviceanbieters lesen“ im Zweig „BO4E Lesen (Backend)“ (`kommunikationsdaten-des-serviceanbieters-lesen-14017018e0`)

### Lastgangs einer Lokation lesen

Lesen eines Lastgangs einer Lokation (Parameter1) mit LokationsTyp (parameter2) zum Start- und Endezeitpunkt (Parameter3/Parameter4) und einer OBIS Kennzahl (Parameter4 optional) | Reading a profile for a location (Parameter1) at the start and end time (Parameter2/Parameter3) and an OBIS code (Parameter4 optional)

| Was | Aufruf | Kommando | Quelle |
|---|---|---|---|
| deutsche Benennung | `GET /lesenEnergiemengeLastgang` | `LESEN_ENERGIEMENGE_LASTGANG` | `macoapp-lesen.json` |
| ausgelieferte Benennung | `GET /getEnergyAmountLoadCurve` | `LESEN_ENERGIEMENGE_LASTGANG` | `doc.macoapp.de` |
| rollengegliederte Benennung | `GET /getEnergyAmountLoadCurve` | `LESEN_ENERGIEMENGE` | `maco-api.yaml` |

| Parameter | Ort | Pflicht | Bedeutung |
|---|---|---|---|
| parameter1 | query | ja | LokationsId |
| parameter2 | query | ja | LokationsTyp |
| parameter3 | query | ja | Datum (Gültig ab) oder Stichtag, wenn parameter4 nicht gesetzt |
| parameter4 | query | ja | Datum (Gültig bis) |
| parameter5 | query | ja | OBIS Kennzahl |
| parameter6 | query | ja | abrechnungsrevant? [true/false = default null) Wenn Parameter null ist, soll dieser in der Abfage ignoriert werden, wenn true soll explizit geprüft werden ob Lastgang abrechnungsrelevant ist, wenn false soll explizit geprüft werden ob nicht Lastgang NICHT abrechnungsrelevant ist |
| parameter7 | query | ja | bilanzierungsrelevant) [true/false = default null) WennParameter null ist, soll dieser in der Abfage ignoriert werden, wenn true soll explizit geprüft werden ob Lastgang bilanzierungsrelevant ist, wenn false soll explizit geprüft werden ob nicht Lastgang NICHT bilanzierungsrelevant ist |
| command | query | nein | Entspricht der operationId dieser Schnittstelle. Diese Operation Id entspricht dem Command im Camunda Konnektor Prozess. Wenn das Backend einen generischen Endpunkt bereitstellt, kann dieses Command gentutzt werden um zu definieren welche Operation ausgeführt werden soll. |

**Antwort (200):** `Energiemenge`

**Regeln der Konnektortabellen, die diesen Aufruf auslösen:** LF 2

*Entspricht in doc.macoapp.de:* „Lastgangs einer Lokation lesen“ im Zweig „BO4E Lesen (Backend)“ (`lastgangs-einer-lokation-lesen-14017016e0`)

### Leistungskurvendefinition lesen

:::note{title="Nur die abzulösende Doku führt sie"}

Für diese Operation führt **keine gepflegte Spezifikation** einen Pfad — weder `maco-api.yaml` noch die `_build`-Specs. Belegt ist, dass doc.macoapp.de sie als `GET /getDefinitionPerformance` mit dem Kommando `LESEN_DEFINITION_LEISTUNGSKURVE` ausliefert, und zwar mit einer vollständigen eingebetteten OpenAPI: Parameter, Antwortcodes und Schemata stehen dort. Der [Schnittstellen-Katalog](/api/202604/backend-lesen) liefert sie daraus aus.

:::

### Lokationsbündel lesen

Lesen eines Lokationsbündels mittels LokationsId (Parameter1) zum Zeitpunkt (Parameter2) | Reading a location bundle using location ID (Parameter1) at the time (Parameter2)

| Was | Aufruf | Kommando | Quelle |
|---|---|---|---|
| deutsche Benennung | `GET /lesenLokationsbundBasis` | `LESEN_LOKATIONSBUENDEL_BASIS` | `macoapp-lesen.json` |
| ausgelieferte Benennung | `GET /getLocationBundleBasic` | `LESEN_LOKATIONSBUENDEL_BASIS` | `doc.macoapp.de` |
| rollengegliederte Benennung | `GET /getLocationBundleBasic` | `LESEN_LOKATIONSBUENDEL` | `maco-api.yaml` |

| Parameter | Ort | Pflicht | Bedeutung |
|---|---|---|---|
| parameter1 | query | ja | LokationsId |
| parameter2 | query | ja | LokationsTyp |
| parameter3 | query | ja | Datum (Gültig ab) oder Stichtag, wenn parameter4 nicht gesetzt |
| parameter4 | query | ja | Datum (Gültig bis) |
| command | query | nein | Entspricht der operationId dieser Schnittstelle. Diese Operation Id entspricht dem Command im Camunda Konnektor Prozess. Wenn das Backend einen generischen Endpunkt bereitstellt, kann dieses Command gentutzt werden um zu definieren welche Operation ausgeführt werden soll. |

**Antwort (200):** `Lokationsbuendel`

**Regeln der Konnektortabellen, die diesen Aufruf auslösen:** LF 2 · MSB 2 · NB 10

*Entspricht in doc.macoapp.de:* „Lokationsbündel lesen“ im Zweig „BO4E Lesen (Backend)“ (`lokationsbündel-lesen-14017019e0`)

### Marktlokation lesen

Lesen einer MaLo mittels LokationsId (Parameter1) zum Zeitpunkt (Parameter2)  
Reading a MaLo using location ID (Parameter1) at the time (Parameter2)

| Was | Aufruf | Kommando | Quelle |
|---|---|---|---|
| deutsche Benennung | `GET /lesenMarktlokationBasis` | `LESEN_MARKTLOKATION_BASIS` | `macoapp-lesen.json` |
| ausgelieferte Benennung | `GET /getMarketLocationBasic` | `LESEN_MARKTLOKATION_BASIS` | `doc.macoapp.de` |
| rollengegliederte Benennung | `GET /getMarketLocationBasic` | `LESEN_MARKTLOKATION` | `maco-api.yaml` |

| Parameter | Ort | Pflicht | Bedeutung |
|---|---|---|---|
| parameter1 | query | ja | LokationsId der Marklokation |
| parameter2 | query | nein | LokationsTyp, wenn nicht gesetzt, immer MALO |
| parameter3 | query | ja | Datum (Gültig ab) oder Stichtag, wenn parameter4 nicht gesetzt |
| parameter4 | query | nein | Datum (Gültig bis) |
| command | query | nein | Entspricht der operationId dieser Schnittstelle. Diese Operation Id entspricht dem Command im Camunda Konnektor Prozess. Wenn das Backend einen generischen Endpunkt bereitstellt, kann dieses Command gentutzt werden um zu definieren welche Operation ausgeführt werden soll. |

**Antwort (200):** `Marktlokation`

**Regeln der Konnektortabellen, die diesen Aufruf auslösen:** LF 65 · MSB 38 · NB 101

*Entspricht in doc.macoapp.de:* „Marktlokation lesen“ im Zweig „BO4E Lesen (Backend)“ (`marktlokation-lesen-14017020e0`)

### Messlokation lesen

Lesen einer MeLo mittels LokationsId (Parameter1) zum Zeitpunkt (Parameter2)  
Reading a MeLo using location ID (Parameter1) at the time (Parameter2)

| Was | Aufruf | Kommando | Quelle |
|---|---|---|---|
| deutsche Benennung | `GET /lesenMesslokationBasis` | `LESEN_MESSLOKATION_BASIS` | `macoapp-lesen.json` |
| ausgelieferte Benennung | `GET /getMeterLocationBasic` | `LESEN_MESSLOKATION_BASIS` | `doc.macoapp.de` |
| rollengegliederte Benennung | `GET /getMeterLocationBasic` | `LESEN_MESSLOKATION` | `maco-api.yaml` |

| Parameter | Ort | Pflicht | Bedeutung |
|---|---|---|---|
| parameter1 | query | ja | LokationsId |
| parameter2 | query | ja | LokationsTyp |
| parameter3 | query | ja | Datum (Gültig ab) oder Stichtag, wenn parameter4 nicht gesetzt |
| parameter4 | query | ja | Datum (Gültig bis) |
| command | query | nein | Entspricht der operationId dieser Schnittstelle. Diese Operation Id entspricht dem Command im Camunda Konnektor Prozess. Wenn das Backend einen generischen Endpunkt bereitstellt, kann dieses Command gentutzt werden um zu definieren welche Operation ausgeführt werden soll. |

**Antwort (200):** `Messlokation`

**Regeln der Konnektortabellen, die diesen Aufruf auslösen:** LF 18 · MSB 54 · NB 50

*Entspricht in doc.macoapp.de:* „Messlokation lesen“ im Zweig „BO4E Lesen (Backend)“ (`messlokation-lesen-14017024e0`)

### Messstellenbetriebsvertrag lesen

Lesen des Messstellenbetriebsvertrages einer Lokation (Parameter1) zum Zeitpunkt (Parameter2) | Reading the metering contract of a location (Parameter1) at the time (Parameter2)

| Was | Aufruf | Kommando | Quelle |
|---|---|---|---|
| deutsche Benennung | `GET /lesenMessstellenbetriebsvertragBasis` | `LESEN_MESSSTELLENBETRIEBSVERTRAG_BASIS` | `macoapp-lesen.json` |
| ausgelieferte Benennung | `GET /getMeasuringPointOperationContractBasic` | `LESEN_MESSSTELLENBETRIEBSVERTRAG_BASIS` | `doc.macoapp.de` |
| rollengegliederte Benennung | `GET /getMeasuringPointOperationContractBasic` | `LESEN_VERTRAG` | `maco-api.yaml` |

| Parameter | Ort | Pflicht | Bedeutung |
|---|---|---|---|
| parameter1 | query | ja | LokationsId |
| parameter2 | query | ja | LokationsTyp |
| parameter3 | query | ja | Datum (Gültig ab) oder Stichtag, wenn parameter4 nicht gesetzt |
| parameter4 | query | ja | Datum (Gültig bis) |
| command | query | nein | Entspricht der operationId dieser Schnittstelle. Diese Operation Id entspricht dem Command im Camunda Konnektor Prozess. Wenn das Backend einen generischen Endpunkt bereitstellt, kann dieses Command gentutzt werden um zu definieren welche Operation ausgeführt werden soll. |

**Antwort (200):** `Vertrag`

*Entspricht in doc.macoapp.de:* „Messstellenbetriebsvertrag lesen“ im Zweig „BO4E Lesen (Backend)“ (`messstellenbetriebsvertrag-lesen-14017025e0`)

### Netzlokation lesen

Lesen einer NeLo mittels LokationsId (Parameter1) zum Zeitpunkt (Parameter2)  
Reading a NeLo using location ID (Parameter1) at the time (Parameter2)

| Was | Aufruf | Kommando | Quelle |
|---|---|---|---|
| deutsche Benennung | `GET /lesenNetzlokationBasis` | `LESEN_NETZLOKATION_BASIS` | `macoapp-lesen.json` |
| ausgelieferte Benennung | `GET /getGridLocationBasic` | `LESEN_NETZLOKATION_BASIS` | `doc.macoapp.de` |
| rollengegliederte Benennung | `GET /getGridLocationBasic` | `LESEN_NETZLOKATION` | `maco-api.yaml` |

| Parameter | Ort | Pflicht | Bedeutung |
|---|---|---|---|
| parameter1 | query | ja | LokationsId |
| parameter2 | query | ja | LokationsTyp |
| parameter3 | query | ja | Datum (Gültig ab) oder Stichtag, wenn parameter4 nicht gesetzt |
| parameter4 | query | ja | Datum (Gültig bis) |
| command | query | nein | Entspricht der operationId dieser Schnittstelle. Diese Operation Id entspricht dem Command im Camunda Konnektor Prozess. Wenn das Backend einen generischen Endpunkt bereitstellt, kann dieses Command gentutzt werden um zu definieren welche Operation ausgeführt werden soll. |

**Antwort (200):** `Netzlokation`

**Regeln der Konnektortabellen, die diesen Aufruf auslösen:** LF 15 · MSB 11 · NB 19

*Entspricht in doc.macoapp.de:* „Netzlokation lesen“ im Zweig „BO4E Lesen (Backend)“ (`netzlokation-lesen-14017026e0`)

### Netznutzungsvertrag lesen

Ändert einen Liefervertrag mittels LokationsId (Parameter1) zum Zeitpunkt (Parameter2) | Changes a delivery contract using LocationId (Parameter1) at time (Parameter2)

| Was | Aufruf | Kommando | Quelle |
|---|---|---|---|
| deutsche Benennung | `GET /lesenNetznutzungsvertragBasis` | `LESEN_NETZNUTZUNGSVERTRAG_BASIS` | `macoapp-lesen.json` |
| ausgelieferte Benennung | `GET /getGridUsageContractBasic` | `LESEN_NETZNUTZUNGSVERTRAG_BASIS` | `doc.macoapp.de` |
| rollengegliederte Benennung | `GET /getGridUsageContractBasic` | `LESEN_VERTRAG` | `maco-api.yaml` |

| Parameter | Ort | Pflicht | Bedeutung |
|---|---|---|---|
| parameter1 | query | ja | LokationsId |
| parameter2 | query | nein | LokationsTyp |
| parameter3 | query | ja | Datum (Gültig ab) oder Stichtag, wenn parameter4 nicht gesetzt |
| parameter4 | query | nein | Datum (Gültig bis) |

**Antwort (200):** `Vertrag`

*Entspricht in doc.macoapp.de:* „Netznutzungsvertrag lesen“ im Zweig „BO4E Lesen (Backend)“ (`netznutzungsvertrag-lesen-14017027e0`)

### Preisblatt lesen

| Was | Aufruf | Kommando | Quelle |
|---|---|---|---|
| ausgelieferte Benennung | `GET /getPriceSheetBasic` | `LESEN_PREISBLATT_BASIS` | `doc.macoapp.de` |
| rollengegliederte Benennung | `GET /getPriceSheetBasic` | `LESEN_PREISBLATT` | `maco-api.yaml` |

| Parameter | Ort | Pflicht | Bedeutung |
|---|---|---|---|
| parameter1 | query | nein | LokationsId |
| parameter2 | query | nein | LokationsTyp |
| parameter3 | query | ja | Datum (Gültig ab) oder Stichtag, wenn parameter4 nicht gesetzt |
| parameter4 | query | nein | Datum (Gültig bis) |
| command | query | nein | Entspricht der operationId dieser Schnittstelle. Diese Operation Id entspricht dem Command im Camunda Konnektor Prozess. Wenn das Backend einen generischen Endpunkt bereitstellt, kann dieses Command gentutzt werden um zu definieren welche Operation ausgeführt werden soll. |

**Antwort (200):** `Preisblatt`

**Regeln der Konnektortabellen, die diesen Aufruf auslösen:** LF 1 · MSB 4 · NB 1

*Entspricht in doc.macoapp.de:* „Preisblatt lesen“ im Zweig „BO4E Lesen (Backend)“ (`preisblatt-lesen-24422191e0`)

### Schaltzeitdefinition lesen

:::note{title="Nur die abzulösende Doku führt sie"}

Für diese Operation führt **keine gepflegte Spezifikation** einen Pfad — weder `maco-api.yaml` noch die `_build`-Specs. Belegt ist, dass doc.macoapp.de sie als `GET /getDefinitionSwitch` mit dem Kommando `LESEN_DEFINITION_SCHALTZEIT` ausliefert, und zwar mit einer vollständigen eingebetteten OpenAPI: Parameter, Antwortcodes und Schemata stehen dort. Der [Schnittstellen-Katalog](/api/202604/backend-lesen) liefert sie daraus aus.

:::

### Steuerbare Ressource lesen

Lesen einer steuerbaren Ressource mittels LokationsId (Parameter1) zum Zeitpunkt (Parameter2) | Reading a controllable resource using location ID (Parameter1) at the time (Parameter2)

| Was | Aufruf | Kommando | Quelle |
|---|---|---|---|
| deutsche Benennung | `GET /lesenSteuerbareRessourceBasis` | `LESEN_STEUERBARE_RESSOURCE_BASIS` | `macoapp-lesen.json` |
| ausgelieferte Benennung | `GET /getControllableResourceBasic` | `LESEN_STEUERBARE_RESSOURCE_BASIS` | `doc.macoapp.de` |
| rollengegliederte Benennung | `GET /getControllableResourceBasic` | `LESEN_STEUERBARERESSOURCE` | `maco-api.yaml` |

| Parameter | Ort | Pflicht | Bedeutung |
|---|---|---|---|
| parameter1 | query | ja | LokationsId \| Location ID |
| parameter2 | query | ja | LokationsTyp \| Location type |
| parameter3 | query | ja | Datum (Gültig ab) \| Date (Valid from) |
| parameter4 | query | ja | Datum (Gültig bis) \| Date (Valid until) |

**Antwort (200):** `SteuerbareRessource`

**Regeln der Konnektortabellen, die diesen Aufruf auslösen:** LF 4 · MSB 6 · NB 10

*Entspricht in doc.macoapp.de:* „Steuerbare Ressource lesen“ im Zweig „BO4E Lesen (Backend)“ (`steuerbare-ressource-lesen-14017028e0`)

### Technische Ressource lesen

Lesen einer technischen Ressource mittels LokationsId (Parameter1) zum Zeitpunkt (Parameter2) | Reading a technical resource using location ID (Parameter1) at the time (Parameter2)

| Was | Aufruf | Kommando | Quelle |
|---|---|---|---|
| deutsche Benennung | `GET /lesenTechnischeRessourceBasis` | `LESEN_TECHNISCHE_RESSOURCE_BASIS` | `macoapp-lesen.json` |
| ausgelieferte Benennung | `GET /getTechnicalResourceBasic` | `LESEN_TECHNISCHE_RESSOURCE_BASIS` | `doc.macoapp.de` |
| rollengegliederte Benennung | `GET /getTechnicalResourceBasic` | `LESEN_TECHNISCHERESSOURCE` | `maco-api.yaml` |

| Parameter | Ort | Pflicht | Bedeutung |
|---|---|---|---|
| parameter1 | query | ja | LokationsId \| Location ID |
| parameter2 | query | ja | LokationsTyp \| Location type |
| parameter3 | query | ja | Datum (Gültig ab) \| Date (Valid from) |
| parameter4 | query | ja | Datum (Gültig bis) \| Date (Valid until) |

**Antwort (200):** `TechnischeRessource`

**Regeln der Konnektortabellen, die diesen Aufruf auslösen:** LF 3 · MSB 2 · NB 10

*Entspricht in doc.macoapp.de:* „Technische Ressource lesen“ im Zweig „BO4E Lesen (Backend)“ (`technische-ressource-lesen-14017029e0`)

### Tranche lesen

Lesen einer Tranche mittels LokationsId (Parameter1) zum Zeitpunkt (Parameter2) | Reading a tranche using location ID (Parameter1) at the time (Parameter2)

| Was | Aufruf | Kommando | Quelle |
|---|---|---|---|
| deutsche Benennung | `GET /lesenTrancheBasis` | `LESEN_TRANCHE_BASIS` | `macoapp-lesen.json` |
| ausgelieferte Benennung | `GET /getTrancheBasic` | `LESEN_TRANCHE_BASIS` | `doc.macoapp.de` |
| rollengegliederte Benennung | `GET /getTrancheBasic` | `LESEN_TRANCHE` | `maco-api.yaml` |

| Parameter | Ort | Pflicht | Bedeutung |
|---|---|---|---|
| parameter1 | query | ja | LokationsId \| Location ID |
| parameter2 | query | ja | LokationsTyp \| Location type |
| parameter3 | query | ja | Datum (Gültig ab) \| Date (Valid from) |
| parameter4 | query | ja | Datum (Gültig bis) \| Date (Valid until) |

**Antwort (200):** `Tranche`

**Regeln der Konnektortabellen, die diesen Aufruf auslösen:** LF 12 · MSB 8 · NB 15

*Entspricht in doc.macoapp.de:* „Tranche lesen“ im Zweig „BO4E Lesen (Backend)“ (`tranche-lesen-14017030e0`)

### Zaehlzeitdefinition lesen

:::note{title="Nur die abzulösende Doku führt sie"}

Für diese Operation führt **keine gepflegte Spezifikation** einen Pfad — weder `maco-api.yaml` noch die `_build`-Specs. Belegt ist, dass doc.macoapp.de sie als `GET /getDefinitionCounting` mit dem Kommando `LESEN_DEFINITION_ZAEHLZEIT` ausliefert, und zwar mit einer vollständigen eingebetteten OpenAPI: Parameter, Antwortcodes und Schemata stehen dort. Der [Schnittstellen-Katalog](/api/202604/backend-lesen) liefert sie daraus aus.

:::

### Zähler lesen

Lesen einer Zaehlers mittels LokationsId (Parameter1) und lokationsTyp (Parameter2 - default MELO) zum Zeitpunkt (Parameter3) | Reading a tranche using location ID (Parameter1) at the time (Parameter2)

| Was | Aufruf | Kommando | Quelle |
|---|---|---|---|
| deutsche Benennung | `GET /lesenZaehlerBasis` | `LESEN_ZAEHLER_BASIS` | `macoapp-lesen.json` |
| ausgelieferte Benennung | `GET /getCounterBasic` | `LESEN_ZAEHLER_BASIS` | `doc.macoapp.de` |
| rollengegliederte Benennung | `GET /getCounterBasic` | `LESEN_ZAEHLER` | `maco-api.yaml` |

| Parameter | Ort | Pflicht | Bedeutung |
|---|---|---|---|
| parameter1 | query | ja | LokationsId \| Location ID |
| parameter2 | query | ja | LokationsTyp \| Location type |
| parameter3 | query | ja | Datum (Gültig ab) \| Date (Valid from) |
| parameter4 | query | ja | Datum (Gültig bis) \| Date (Valid until) |

**Antwort (200):** `Zaehler`

**Regeln der Konnektortabellen, die diesen Aufruf auslösen:** LF 14 · MSB 12 · NB 24

*Entspricht in doc.macoapp.de:* „Zähler lesen“ im Zweig „BO4E Lesen (Backend)“ (`zähler-lesen-14017031e0`)

### Zählerstand einer Lokation lesen

Lesen eines oder mehrerer Zählerstände über eine Lokation (Parameter1) in einer Range (Parameter2/Parameter3) und einer OBIS Kennzahl (Parameter4 optional) | Reading one or more meter readings for a location (Parameter1) in a range (Parameter2/Parameter3) and an OBIS code (Parameter4 optional)

| Was | Aufruf | Kommando | Quelle |
|---|---|---|---|
| deutsche Benennung | `GET /lesenEnergiemengeZaehlerstand` | `LESEN_ENERGIEMENGE_ZAEHLERSTAND` | `macoapp-lesen.json` |
| ausgelieferte Benennung | `GET /getEnergyAmountMeterReading` | `LESEN_ENERGIEMENGE_ZAEHLERSTAND` | `doc.macoapp.de` |
| rollengegliederte Benennung | `GET /getEnergyAmountMeterReading` | `LESEN_ENERGIEMENGE` | `maco-api.yaml` |

| Parameter | Ort | Pflicht | Bedeutung |
|---|---|---|---|
| parameter1 | query | ja | LokationsId |
| parameter2 | query | ja | LokationsTyp |
| parameter3 | query | ja | Datum (Gültig ab) oder Stichtag, wenn parameter4 nicht gesetzt |
| parameter4 | query | ja | Datum (Gültig bis) |
| parameter5 | query | ja | OBIS Kennzah |
| command | query | nein | Entspricht der operationId dieser Schnittstelle. Diese Operation Id entspricht dem Command im Camunda Konnektor Prozess. Wenn das Backend einen generischen Endpunkt bereitstellt, kann dieses Command gentutzt werden um zu definieren welche Operation ausgeführt werden soll. |

**Antwort (200):** `Energiemenge`

**Regeln der Konnektortabellen, die diesen Aufruf auslösen:** LF 2

*Entspricht in doc.macoapp.de:* „Zählerstand einer Lokation lesen“ im Zweig „BO4E Lesen (Backend)“ (`zählerstand-einer-lokation-lesen-14017017e0`)

### Empfang einer Marktnachricht

Empfang einer Marktnachricht über MCS

| Was | Aufruf | Kommando | Quelle |
|---|---|---|---|
| rollengegliederte Benennung | `POST /receive` | `MCS_RECEIVE` | `maco-api.yaml` |

**Anfragekörper:** `Message`

**Antwort (200):** `object`

### Absenderdaten lesen

:::warning{title="Veraltet"}

`maco-api.yaml` führt diese Operation als `deprecated`.

:::

Lesen einen absender(marktteilnehmer) mit LokationsId (Parameter1) zum Zeitpunkt (Parameter2) | Read a sender (market participant) (parameter 1) at time (parameter 2)

| Was | Aufruf | Kommando | Quelle |
|---|---|---|---|
| deutsche Benennung | `GET /lesenMarktteilnehmerAbsender` | `LESEN_MARKTTEILNEHMER_ABSENDER` | `macoapp-lesen.json` |
| rollengegliederte Benennung | `GET /lesenMarktteilnehmerAbsender` | `OBSOLET_ABSENDERDATEN_LESEN` | `maco-api.yaml` |

**Antwort (200):** `object`

### Empfängerdaten lesen

:::warning{title="Veraltet"}

`maco-api.yaml` führt diese Operation als `deprecated`.

:::

Lesen einen recipient(marktteilnehmer) mit LokationsId (Parameter1) zum Zeitpunkt (Parameter2) | Read a recipient (market participant) (parameter 1) at time (parameter 2)

| Was | Aufruf | Kommando | Quelle |
|---|---|---|---|
| deutsche Benennung | `GET /lesenMarktteilnehmerEmpfaenger` | `LESEN_MARKTTEILNEHMER_EMPFAENGER` | `macoapp-lesen.json` |
| rollengegliederte Benennung | `GET /lesenMarktteilnehmerEmpfaenger` | `OBSOLET_EMPFÄNGERDATEN_LESEN` | `maco-api.yaml` |

**Antwort (200):** `object`

### Verwendungszeitraum einer Marktlokation ermitteln

:::warning{title="Veraltet"}

`maco-api.yaml` führt diese Operation als `deprecated`.

:::

| Was | Aufruf | Kommando | Quelle |
|---|---|---|---|
| rollengegliederte Benennung | `GET /getMarketlokationAllocationPeriod` | `OBSOLET_VERWENDUNGSZEITRAUM_EINER_MARKTLOKATION_ERMITTELN` | `maco-api.yaml` |

**Antwort (200):** `object`

### Zuordnungsemächtigung lesen (UNKNOWN)

Zuordnungsemächtigung lesen

| Was | Aufruf | Kommando | Quelle |
|---|---|---|---|
| rollengegliederte Benennung | `POST /prozessdaten/unknown/update` | `PROZESSDATEN_UPDATE_UNKNOWN` | `maco-api.yaml` |

**Anfragekörper:** `ProcessData`

**Antwort (200):** `object`

### Zuordnungsemächtigung lesen

:::note{title="Nur die abzulösende Doku führt sie"}

Für diese Operation führt **keine gepflegte Spezifikation** einen Pfad — weder `maco-api.yaml` noch die `_build`-Specs. Belegt ist, dass doc.macoapp.de sie als `GET /getAllocationAuthorization` mit dem Kommando `LESEN_PROZESSDATEN_ZUORDNUNGERMAECHTIGUNG` ausliefert, und zwar mit einer vollständigen eingebetteten OpenAPI: Parameter, Antwortcodes und Schemata stehen dort. Der [Schnittstellen-Katalog](/api/202604/backend-lesen) liefert sie daraus aus.

`maco-api.yaml` führt dieselbe Bezeichnung unter `POST /prozessdaten/unknown/update` — anderer Pfad, andere Methode. Ob das derselbe Aufruf ist, sagt keine Quelle; hier wird es deshalb nicht gleichgesetzt.

:::

### LESEN_MARKTLOKATION_VERWENDUNGSZEITRAUM

Lesen MaLos mittels LokationsId (Parameter1) und businessKey  
Reading MaLos using LocationId (Parameter1) and businessKey

| Was | Aufruf | Kommando | Quelle |
|---|---|---|---|
| deutsche Benennung | `GET /lesenMarktlokationVerwendungszeitraum` | `LESEN_MARKTLOKATION_VERWENDUNGSZEITRAUM` | `macoapp-lesen.json` |

### AKTUALISIEREN_MDOC_BASIS

Aktualisieren des MDOCS anhand des BusinessKey. Neben der Aktualisierung des Status kann eine generische Liste von Object, Attribute_Name und Attribute_value übergeben werden, um zusätzliche Transaktionsinformationen wie Antwortstatus, Codeliste, etc. zu übergeben.

| Was | Aufruf | Kommando | Quelle |
|---|---|---|---|
| deutsche Benennung | `POST /aktualisierenMdocBasis` | `AKTUALISIEREN_MDOC_BASIS` | `macoapp-schreiben.json` |

### ERSTELLEN_PROZESSDATEN_MALOIDENTANTWORT_NEGATIV

Negative Antwort des Netzbetreibers mit den Informationen der Transaktion inklusive Ablehngrund, sowie Referenz auf ursprüngliche Anfrage, die im Backend verbucht werden sollen.

| Was | Aufruf | Kommando | Quelle |
|---|---|---|---|
| deutsche Benennung | `POST /erstellenProzessdatenMaloidentantwortNegativ` | `ERSTELLEN_PROZESSDATEN_MALOIDENTANTWORT_NEGATIV` | `maloident-lieferant.json` |

### ERSTELLEN_PROZESSDATEN_MALOIDENTANTWORT_POSITIV

Positive Antwort des Netzbetreibers mit den Stammdaten der identifizierten Marktlokation, den Informationen der Transaktion, sowie Referenz auf ursprüngliche Anfrage, die im Backend verbucht werden sollen.

| Was | Aufruf | Kommando | Quelle |
|---|---|---|---|
| deutsche Benennung | `POST /erstellenProzessdatenMaloidentantwortPositiv` | `ERSTELLEN_PROZESSDATEN_MALOIDENTANTWORT_POSITIV` | `maloident-lieferant.json` |
