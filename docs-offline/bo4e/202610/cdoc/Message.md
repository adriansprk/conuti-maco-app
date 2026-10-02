# Message
<span hidden data-pagefind-meta={"title:Message — BO4E-Dokumentobjekt (FV 202610)"} />

BO4E-Dokumentobjekt · 1 Felder · 0 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="processes"></a>`processes` | [Process[]](/bo4e/202610/cdoc/Process) | — |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[processes](/bo4e/202610/cdoc/Message#processes) <span className="hbs-liste">[ ]</span></span> | — | [Process[]](/bo4e/202610/cdoc/Process) |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

:::note{title="Umschlag der Prozessdaten"}

`Message` ist die Hülle um eine Liste von `processes` — mehr trägt das Objekt nicht.

Die Prüfi- und Event-Spezifikationen dieser Formatversion beginnen beim *Inhalt* (`stammdaten`, `transaktionsdaten`, `zusatzdaten`) und referenzieren kein Feld des Umschlags per `$ref`. Die 0 Verwendungen in der Kennzeile oben messen deshalb den `$ref`-Graphen dieser Schemata und sagen nichts darüber, ob der Umschlag gesendet wird.

**Gemessen am 05.09.2026:** `updateProcessData` und `createProcessData` senden `{stammdaten, transaktionsdaten, zusatzdaten}` — **ohne** diesen Umschlag. Der `businessKey` steht dabei *in* `zusatzdaten`, nicht am Rumpf. Belegt an der Konstruktionsvorschrift des Senders im Konnektor-Fluss; die Gegenkontrolle ist derselbe Fluss, der für die Nachricht an die Prozess-Engine sehr wohl einen Umschlag baut. **Nicht gemessen:** ein mitgeschnittener echter Aufruf, und der MaloIdent-Zweig (03002/03003), der eigenständig läuft.

Die Schnittstellen-Spezifikation zeigt denselben Rumpf. Der eine Ausreißer mit einem Feld `data` an der Wurzel ist genau **1 von 112** Gliedern des `updateProcessData`-Schemas der Rolle LF und keine zweite Rumpfform.

Die Schlüssel `businessKey`, `prozessId` und `targetBusinessKey` sind im Zusammenhang unter [Schlüssel](/schnittstellen/schluessel) beschrieben.

:::

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

</Hinweisbereich>
