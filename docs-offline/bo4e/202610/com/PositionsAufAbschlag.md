# PositionsAufAbschlag
<span hidden data-pagefind-meta={"title:PositionsAufAbschlag — BO4E-Komponente (FV 202610)"} />

BO4E-Komponente · 5 Felder · 0 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="bezeichnung"></a>`bezeichnung` | string | bezeichnung |
| <a id="beschreibung"></a>`beschreibung` | string | beschreibung |
| <a id="aufabschlagstyp"></a>`aufAbschlagstyp` | [Enum AufAbschlagstyp](/bo4e/202610/enum/AufAbschlagstyp)<br/><Werte>`RELATIV`, `ABSOLUT`</Werte> | Festlegung, ob der Auf- oder Abschlag mit relativen oder absoluten Werten erfolgt |
| <a id="aufabschlagswert"></a>`aufAbschlagswert` | number (float) | aufAbschlagswert |
| <a id="aufabschlagswaehrung"></a>`aufAbschlagswaehrung` | [Enum Waehrungseinheit](/bo4e/202610/enum/Waehrungseinheit)<br/><Werte>`EUR`, `CT`</Werte> | Waehrungseinheit |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[bezeichnung](/bo4e/202610/com/PositionsAufAbschlag#bezeichnung)</span> | bezeichnung | string |
| <span className="hbs-f hbs-e0">[beschreibung](/bo4e/202610/com/PositionsAufAbschlag#beschreibung)</span> | beschreibung | string |
| <span className="hbs-f hbs-e0">[aufAbschlagstyp](/bo4e/202610/com/PositionsAufAbschlag#aufabschlagstyp)</span> | Festlegung, ob der Auf- oder Abschlag mit relativen oder absoluten Werten erfolgt | [Enum AufAbschlagstyp](/bo4e/202610/enum/AufAbschlagstyp)<br/><Werte>`RELATIV`, `ABSOLUT`</Werte> |
| <span className="hbs-f hbs-e0">[aufAbschlagswert](/bo4e/202610/com/PositionsAufAbschlag#aufabschlagswert)</span> | aufAbschlagswert | number (float) |
| <span className="hbs-f hbs-e0">[aufAbschlagswaehrung](/bo4e/202610/com/PositionsAufAbschlag#aufabschlagswaehrung)</span> | Waehrungseinheit | [Enum Waehrungseinheit](/bo4e/202610/enum/Waehrungseinheit)<br/><Werte>`EUR`, `CT`</Werte> |

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
