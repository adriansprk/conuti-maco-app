# Produktpaket
<span hidden data-pagefind-meta={"title:Produktpaket — BO4E-Komponente (FV 202610)"} />

BO4E-Komponente · 4 Felder · 22 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="produktpaketid"></a>`produktpaketId` | integer | produktpaketId |
| <a id="produkt"></a>`produkt` | [Produkt[]](/bo4e/202610/com/Produkt) | produkt |
| <a id="umsetzungsgradvorgabe"></a>`umsetzungsgradvorgabe` | [Enum Umsetzungsgradvorgabe](/bo4e/202610/enum/Umsetzungsgradvorgabe)<br/><Werte>`ZUORDNUNG_NUR_WENN_PRODUKTPAKET_UMSETZBAR`, `ZUORDNUNG_AUCH_WENN_PRODUKTPAKET_NICHT_UMSETZBAR`</Werte> | Umsetzungsgradvorgabe |
| <a id="priorisierung"></a>`priorisierung` | [Enum Priorisierung](/bo4e/202610/enum/Priorisierung)<br/><Werte>`PRIORITAET1`, `PRIORITAET2`, `PRIORITAET3`, `PRIORITAET4`, `PRIORITAET5`</Werte> | Priorisierung |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[produktpaketId](/bo4e/202610/com/Produktpaket#produktpaketid)</span> | produktpaketId | integer |
| <span className="hbs-g hbs-e0">[produkt](/bo4e/202610/com/Produktpaket#produkt) <span className="hbs-liste">[ ]</span></span> | produkt | [Produkt[]](/bo4e/202610/com/Produkt) |
| <span className="hbs-f hbs-e1">[produktCode](/bo4e/202610/com/Produkt#produktcode)</span> | produktCode | string |
| <span className="hbs-f hbs-e1">[codeProdukteigenschaft](/bo4e/202610/com/Produkt#codeprodukteigenschaft)</span> | codeProdukteigenschaft | string |
| <span className="hbs-f hbs-e1">[wertedetails](/bo4e/202610/com/Produkt#wertedetails)</span> | wertedetails | string |
| <span className="hbs-f hbs-e0">[umsetzungsgradvorgabe](/bo4e/202610/com/Produktpaket#umsetzungsgradvorgabe)</span> | Umsetzungsgradvorgabe | [Enum Umsetzungsgradvorgabe](/bo4e/202610/enum/Umsetzungsgradvorgabe)<br/><Werte>`ZUORDNUNG_NUR_WENN_PRODUKTPAKET_UMSETZBAR`, `ZUORDNUNG_AUCH_WENN_PRODUKTPAKET_NICHT_UMSETZBAR`</Werte> |
| <span className="hbs-f hbs-e0">[priorisierung](/bo4e/202610/com/Produktpaket#priorisierung)</span> | Priorisierung | [Enum Priorisierung](/bo4e/202610/enum/Priorisierung)<br/><Werte>`PRIORITAET1`, `PRIORITAET2`, `PRIORITAET3`, `PRIORITAET4`, `PRIORITAET5`</Werte> |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### produktpaketId

10 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55001](/schnittstellen/202610/pruefi/UTILMD/PI_55001) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › erforderlichesProduktpaket |
| [PI_55003](/schnittstellen/202610/pruefi/UTILMD/PI_55003) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › erforderlichesProduktpaket |
| [PI_55014](/schnittstellen/202610/pruefi/UTILMD/PI_55014) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › erforderlichesProduktpaket |
| [PI_55077](/schnittstellen/202610/pruefi/UTILMD/PI_55077) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › erforderlichesProduktpaket |
| [PI_55080](/schnittstellen/202610/pruefi/UTILMD/PI_55080) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › erforderlichesProduktpaket |
| [PI_55600](/schnittstellen/202610/pruefi/UTILMD/PI_55600) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › erforderlichesProduktpaket |
| [PI_55601](/schnittstellen/202610/pruefi/UTILMD/PI_55601) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › erforderlichesProduktpaket |
| [PI_55604](/schnittstellen/202610/pruefi/UTILMD/PI_55604) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › erforderlichesProduktpaket |
| [PI_55605](/schnittstellen/202610/pruefi/UTILMD/PI_55605) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › erforderlichesProduktpaket |
| [PI_55608](/schnittstellen/202610/pruefi/UTILMD/PI_55608) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › erforderlichesProduktpaket |

### umsetzungsgradvorgabe

6 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55001](/schnittstellen/202610/pruefi/UTILMD/PI_55001) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › erforderlichesProduktpaket |
| [PI_55014](/schnittstellen/202610/pruefi/UTILMD/PI_55014) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › erforderlichesProduktpaket |
| [PI_55077](/schnittstellen/202610/pruefi/UTILMD/PI_55077) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › erforderlichesProduktpaket |
| [PI_55600](/schnittstellen/202610/pruefi/UTILMD/PI_55600) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › erforderlichesProduktpaket |
| [PI_55601](/schnittstellen/202610/pruefi/UTILMD/PI_55601) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › erforderlichesProduktpaket |
| [PI_55608](/schnittstellen/202610/pruefi/UTILMD/PI_55608) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › erforderlichesProduktpaket |

### priorisierung

6 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55001](/schnittstellen/202610/pruefi/UTILMD/PI_55001) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › erforderlichesProduktpaket |
| [PI_55014](/schnittstellen/202610/pruefi/UTILMD/PI_55014) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › erforderlichesProduktpaket |
| [PI_55077](/schnittstellen/202610/pruefi/UTILMD/PI_55077) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › erforderlichesProduktpaket |
| [PI_55600](/schnittstellen/202610/pruefi/UTILMD/PI_55600) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › erforderlichesProduktpaket |
| [PI_55601](/schnittstellen/202610/pruefi/UTILMD/PI_55601) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › erforderlichesProduktpaket |
| [PI_55608](/schnittstellen/202610/pruefi/UTILMD/PI_55608) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › erforderlichesProduktpaket |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
