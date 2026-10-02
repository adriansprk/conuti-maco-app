# MarktlokationsTypisierung
<span hidden data-pagefind-meta={"title:MarktlokationsTypisierung — BO4E-Komponente (FV 202604)"} />

BO4E-Komponente · 3 Felder · 4 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="typ"></a>`typ` | [Enum MarktlokationsTyp](/bo4e/202604/enum/MarktlokationsTyp)<br/><Werte>`STANDARD_MARKTLOKATION`, `RUHENDE_MARKTLOKATION`, `KUNDENANLAGE`</Werte> | Typisierung der Marktlokation als standard Marktlokation, ruhende Marktlokation oder Kundenanlage |
| <a id="gueltigab"></a>`gueltigAb` | string (date-time) | Startdatum der Typisierung der Marktlokation |
| <a id="gueltigbis"></a>`gueltigBis` | string (date-time) | Enddatum der Typisierung der Marktlokation |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[typ](/bo4e/202604/com/MarktlokationsTypisierung#typ)</span> | Typisierung der Marktlokation als standard Marktlokation, ruhende Marktlokation oder Kundenanlage | [Enum MarktlokationsTyp](/bo4e/202604/enum/MarktlokationsTyp)<br/><Werte>`STANDARD_MARKTLOKATION`, `RUHENDE_MARKTLOKATION`, `KUNDENANLAGE`</Werte> |
| <span className="hbs-f hbs-e0">[gueltigAb](/bo4e/202604/com/MarktlokationsTypisierung#gueltigab)</span> | Startdatum der Typisierung der Marktlokation | string (date-time) |
| <span className="hbs-f hbs-e0">[gueltigBis](/bo4e/202604/com/MarktlokationsTypisierung#gueltigbis)</span> | Enddatum der Typisierung der Marktlokation | string (date-time) |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### typ

4 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55001](/schnittstellen/202604/pruefi/UTILMD/PI_55001) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktlokationsTyp |
| [PI_55004](/schnittstellen/202604/pruefi/UTILMD/PI_55004) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktlokationsTyp |
| [PI_55007](/schnittstellen/202604/pruefi/UTILMD/PI_55007) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktlokationsTyp |
| [PI_55010](/schnittstellen/202604/pruefi/UTILMD/PI_55010) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktlokationsTyp |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
