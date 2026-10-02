# Rechenschritt
<span hidden data-pagefind-meta={"title:Rechenschritt — BO4E-Komponente (FV 202610)"} />

BO4E-Komponente · 10 Felder · 8 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="rechenschrittbestandteilid"></a>`rechenschrittBestandteilId` | integer | rechenschrittBestandteilId |
| <a id="referenzrechenschrittid"></a>`referenzRechenschrittId` | integer | referenzRechenschrittId |
| <a id="operation"></a>`operation` | [Enum ArithmetischeOperation](/bo4e/202610/enum/ArithmetischeOperation)<br/><Werte>`ADDITION`, `SUBTRAKTION`, `DIVISION`, `DIVIDEND`, `MULTIPLIKATION`, `POSITIVWERT`</Werte> | Mit dieser Aufzählung können arithmetische Operationen festgelegt werden |
| <a id="verlustfaktortrafo"></a>`verlustfaktorTrafo` | number (float) | verlustfaktorTrafo |
| <a id="verlustfaktorleitung"></a>`verlustfaktorLeitung` | number (float) | verlustfaktorLeitung |
| <a id="aufteilungsfaktorenergiemenge"></a>`aufteilungsfaktorEnergiemenge` | number (float) | aufteilungsfaktorEnergiemenge |
| <a id="messlokationsid"></a>`messlokationsId` | string | messlokationsId |
| <a id="marktlokationsid"></a>`marktlokationsId` | string | marktlokationsId |
| <a id="energieflussrichtung"></a>`energieflussrichtung` | [Enum Energierichtung](/bo4e/202610/enum/Energierichtung)<br/><Werte>`AUSSP`, `EINSP`</Werte> | Spezifiziert die Energierichtung einer Markt- und/oder Messlokation |
| <a id="bezeichnungoperanden"></a>`bezeichnungOperanden` | string | Bezeichnung der Operanden |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[rechenschrittBestandteilId](/bo4e/202610/com/Rechenschritt#rechenschrittbestandteilid)</span> | rechenschrittBestandteilId | integer |
| <span className="hbs-f hbs-e0">[referenzRechenschrittId](/bo4e/202610/com/Rechenschritt#referenzrechenschrittid)</span> | referenzRechenschrittId | integer |
| <span className="hbs-f hbs-e0">[operation](/bo4e/202610/com/Rechenschritt#operation)</span> | Mit dieser Aufzählung können arithmetische Operationen festgelegt werden | [Enum ArithmetischeOperation](/bo4e/202610/enum/ArithmetischeOperation)<br/><Werte>`ADDITION`, `SUBTRAKTION`, `DIVISION`, `DIVIDEND`, `MULTIPLIKATION`, `POSITIVWERT`</Werte> |
| <span className="hbs-f hbs-e0">[verlustfaktorTrafo](/bo4e/202610/com/Rechenschritt#verlustfaktortrafo)</span> | verlustfaktorTrafo | number (float) |
| <span className="hbs-f hbs-e0">[verlustfaktorLeitung](/bo4e/202610/com/Rechenschritt#verlustfaktorleitung)</span> | verlustfaktorLeitung | number (float) |
| <span className="hbs-f hbs-e0">[aufteilungsfaktorEnergiemenge](/bo4e/202610/com/Rechenschritt#aufteilungsfaktorenergiemenge)</span> | aufteilungsfaktorEnergiemenge | number (float) |
| <span className="hbs-f hbs-e0">[messlokationsId](/bo4e/202610/com/Rechenschritt#messlokationsid)</span> | messlokationsId | string |
| <span className="hbs-f hbs-e0">[marktlokationsId](/bo4e/202610/com/Rechenschritt#marktlokationsid)</span> | marktlokationsId | string |
| <span className="hbs-f hbs-e0">[energieflussrichtung](/bo4e/202610/com/Rechenschritt#energieflussrichtung)</span> | Spezifiziert die Energierichtung einer Markt- und/oder Messlokation | [Enum Energierichtung](/bo4e/202610/enum/Energierichtung)<br/><Werte>`AUSSP`, `EINSP`</Werte> |
| <span className="hbs-f hbs-e0">[bezeichnungOperanden](/bo4e/202610/com/Rechenschritt#bezeichnungoperanden)</span> | Bezeichnung der Operanden | string |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### rechenschrittBestandteilId

1 Verwendung(en) in den Nachrichtentypen UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_25001](/schnittstellen/202610/pruefi/UTILTS/PI_25001) | Prüfi | UTILTS | stammdaten › BERECHNUNGSFORMEL › rechenschritte |

### referenzRechenschrittId

1 Verwendung(en) in den Nachrichtentypen UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_25001](/schnittstellen/202610/pruefi/UTILTS/PI_25001) | Prüfi | UTILTS | stammdaten › BERECHNUNGSFORMEL › rechenschritte |

### operation

1 Verwendung(en) in den Nachrichtentypen UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_25001](/schnittstellen/202610/pruefi/UTILTS/PI_25001) | Prüfi | UTILTS | stammdaten › BERECHNUNGSFORMEL › rechenschritte |

### verlustfaktorTrafo

1 Verwendung(en) in den Nachrichtentypen UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_25001](/schnittstellen/202610/pruefi/UTILTS/PI_25001) | Prüfi | UTILTS | stammdaten › BERECHNUNGSFORMEL › rechenschritte |

### verlustfaktorLeitung

1 Verwendung(en) in den Nachrichtentypen UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_25001](/schnittstellen/202610/pruefi/UTILTS/PI_25001) | Prüfi | UTILTS | stammdaten › BERECHNUNGSFORMEL › rechenschritte |

### aufteilungsfaktorEnergiemenge

1 Verwendung(en) in den Nachrichtentypen UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_25001](/schnittstellen/202610/pruefi/UTILTS/PI_25001) | Prüfi | UTILTS | stammdaten › BERECHNUNGSFORMEL › rechenschritte |

### messlokationsId

1 Verwendung(en) in den Nachrichtentypen UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_25001](/schnittstellen/202610/pruefi/UTILTS/PI_25001) | Prüfi | UTILTS | stammdaten › BERECHNUNGSFORMEL › rechenschritte |

### energieflussrichtung

1 Verwendung(en) in den Nachrichtentypen UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_25001](/schnittstellen/202610/pruefi/UTILTS/PI_25001) | Prüfi | UTILTS | stammdaten › BERECHNUNGSFORMEL › rechenschritte |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
