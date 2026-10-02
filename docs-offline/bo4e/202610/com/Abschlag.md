# Abschlag
<span hidden data-pagefind-meta={"title:Abschlag — BO4E-Komponente (FV 202610)"} />

BO4E-Komponente · 2 Felder · 2 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="typ"></a>`typ` | [Enum AbschlagTyp](/bo4e/202610/enum/AbschlagTyp)<br/><Werte>`GEMEINDERABATT_KAV`, `ANPASSUNG_P19_STROM_NEV`</Werte> | AbschlagTyp |
| <a id="prozent"></a>`prozent` | number (float) | Prozentuale Angabe zum Auf-/Abschlag |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[typ](/bo4e/202610/com/Abschlag#typ)</span> | AbschlagTyp | [Enum AbschlagTyp](/bo4e/202610/enum/AbschlagTyp)<br/><Werte>`GEMEINDERABATT_KAV`, `ANPASSUNG_P19_STROM_NEV`</Werte> |
| <span className="hbs-f hbs-e0">[prozent](/bo4e/202610/com/Abschlag#prozent)</span> | Prozentuale Angabe zum Auf-/Abschlag | number (float) |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### typ

1 Verwendung(en) in den Nachrichtentypen INVOIC.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_31002](/schnittstellen/202610/pruefi/INVOIC/PI_31002) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen › abschlag |

### prozent

1 Verwendung(en) in den Nachrichtentypen INVOIC.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_31002](/schnittstellen/202610/pruefi/INVOIC/PI_31002) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen › abschlag |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
