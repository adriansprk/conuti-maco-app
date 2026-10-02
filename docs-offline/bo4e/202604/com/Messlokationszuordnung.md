# Messlokationszuordnung
<span hidden data-pagefind-meta={"title:Messlokationszuordnung — BO4E-Komponente (FV 202604)"} />

BO4E-Komponente · 4 Felder · 0 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="messlokationsid"></a>`messlokationsId` | string | MesslokationsId |
| <a id="arithmetik"></a>`arithmetik` | [Enum ArithmetischeOperation](/bo4e/202604/enum/ArithmetischeOperation)<br/><Werte>`ADDITION`, `SUBTRAKTION`, `DIVISION`, `DIVIDEND`, `MULTIPLIKATION`, `POSITIVWERT`</Werte> | Mit dieser Aufzählung können arithmetische Operationen festgelegt werden |
| <a id="gueltigseit"></a>`gueltigSeit` | string (date-time) | Zuordnung gültig ab |
| <a id="gueltigbis"></a>`gueltigBis` | string (date-time) | Zuordnung gültig bis |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[messlokationsId](/bo4e/202604/com/Messlokationszuordnung#messlokationsid)</span> | MesslokationsId | string |
| <span className="hbs-f hbs-e0">[arithmetik](/bo4e/202604/com/Messlokationszuordnung#arithmetik)</span> | Mit dieser Aufzählung können arithmetische Operationen festgelegt werden | [Enum ArithmetischeOperation](/bo4e/202604/enum/ArithmetischeOperation)<br/><Werte>`ADDITION`, `SUBTRAKTION`, `DIVISION`, `DIVIDEND`, `MULTIPLIKATION`, `POSITIVWERT`</Werte> |
| <span className="hbs-f hbs-e0">[gueltigSeit](/bo4e/202604/com/Messlokationszuordnung#gueltigseit)</span> | Zuordnung gültig ab | string (date-time) |
| <span className="hbs-f hbs-e0">[gueltigBis](/bo4e/202604/com/Messlokationszuordnung#gueltigbis)</span> | Zuordnung gültig bis | string (date-time) |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

:::note{title="Keine Verwendung gefunden"}

Kein Feld dieses Objekts wird in den Prüfi- oder Event-Spezifikationen dieser Formatversion referenziert. Das Objekt gehört zum BO4E-Schema, ist in der Marktkommunikation dieser Formatversion aber nicht im Einsatz.

:::

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

</Hinweisbereich>
