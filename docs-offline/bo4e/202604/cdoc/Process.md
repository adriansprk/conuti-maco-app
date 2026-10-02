# Process
<span hidden data-pagefind-meta={"title:Process — BO4E-Dokumentobjekt (FV 202604)"} />

BO4E-Dokumentobjekt · 7 Felder · 0 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="businesskey"></a>`businessKey` | string | BusinessKey · Id des Prozesses, welcher aktuell den Aufruf durchführt. *(nicht aus der Zeitscheibe; Quelle: api-definitionen/schema-eigen/backend-schreiben-lf.yaml)* Dort als `zusatzdaten.businessKey`, Pflicht in „ZUSATZDATEN ( SST erstellen)" und „ZUSATZDATEN ( SST Aktualisieren)"; wortgleich in `backend-schreiben-msb.yaml` und `backend-schreiben-nb.yaml`. In den Erfolgsantworten der Auslöser (`site-d/apis/trigger-<fv>.json`, Schema `event_responses_success`) trägt ein Feld desselben Namens den Text „Einzigartige Kennung des Geschäftsprozesses" (`format: uuid`, Pflicht). Beides sind namensgleiche Felder in API-Schemata, keine Verwendung des cdoc-Objekts `Process`. |
| <a id="datasource"></a>`dataSource` | [DataSource](/bo4e/202604/cdoc/DataSource)<br/><Werte>`INBOUND`, `OUTBOUND`</Werte> | CDOC DataSource |
| <a id="version"></a>`version` | integer | Versionierung des JSON Schemas |
| <a id="edifactversion"></a>`edifactVersion` | integer | Angabe der EDIFACT Formatversion in Format YYYYMM, Beispiel 202504 |
| <a id="data"></a>`data` | [ProcessData](/bo4e/202604/cdoc/ProcessData) | — |
| <a id="tenantid"></a>`tenantId` | string | Identifikation des Mandanten, NONE bei System ohne Mandanten |
| <a id="processdate"></a>`processDate` | string (date-time) | Prozessdatum |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[businessKey](/bo4e/202604/cdoc/Process#businesskey)</span> | BusinessKey · Id des Prozesses, welcher aktuell den Aufruf durchführt. *(nicht aus der Zeitscheibe; Quelle: api-definitionen/schema-eigen/backend-schreiben-lf.yaml)* Dort als `zusatzdaten.businessKey`, Pflicht in „ZUSATZDATEN ( SST erstellen)" und „ZUSATZDATEN ( SST Aktualisieren)"; wortgleich in `backend-schreiben-msb.yaml` und `backend-schreiben-nb.yaml`. In den Erfolgsantworten der Auslöser (`site-d/apis/trigger-<fv>.json`, Schema `event_responses_success`) trägt ein Feld desselben Namens den Text „Einzigartige Kennung des Geschäftsprozesses" (`format: uuid`, Pflicht). Beides sind namensgleiche Felder in API-Schemata, keine Verwendung des cdoc-Objekts `Process`. | string |
| <span className="hbs-f hbs-e0">[dataSource](/bo4e/202604/cdoc/Process#datasource)</span> | CDOC DataSource | [DataSource](/bo4e/202604/cdoc/DataSource)<br/><Werte>`INBOUND`, `OUTBOUND`</Werte> |
| <span className="hbs-f hbs-e0">[version](/bo4e/202604/cdoc/Process#version)</span> | Versionierung des JSON Schemas | integer |
| <span className="hbs-f hbs-e0">[edifactVersion](/bo4e/202604/cdoc/Process#edifactversion)</span> | Angabe der EDIFACT Formatversion in Format YYYYMM, Beispiel 202504 | integer |
| <span className="hbs-f hbs-e0">[data](/bo4e/202604/cdoc/Process#data)</span> | — | [ProcessData](/bo4e/202604/cdoc/ProcessData) |
| <span className="hbs-f hbs-e0">[tenantId](/bo4e/202604/cdoc/Process#tenantid)</span> | Identifikation des Mandanten, NONE bei System ohne Mandanten | string |
| <span className="hbs-f hbs-e0">[processDate](/bo4e/202604/cdoc/Process#processdate)</span> | Prozessdatum | string (date-time) |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

:::note{title="Umschlag der Prozessdaten"}

`Process` trägt den `businessKey` der Prozessinstanz, die Herkunft (`dataSource`), die Fassungen (`version`, `edifactVersion`), den Mandanten (`tenantId`), das `processDate` und in `data` die eigentlichen Prozessdaten.

Die Prüfi- und Event-Spezifikationen dieser Formatversion beginnen beim *Inhalt* (`stammdaten`, `transaktionsdaten`, `zusatzdaten`) und referenzieren kein Feld des Umschlags per `$ref`. Die 0 Verwendungen in der Kennzeile oben messen deshalb den `$ref`-Graphen dieser Schemata und sagen nichts darüber, ob der Umschlag gesendet wird.

**Gemessen am 05.09.2026:** `updateProcessData` und `createProcessData` senden `{stammdaten, transaktionsdaten, zusatzdaten}` — **ohne** diesen Umschlag. Der `businessKey` steht dabei *in* `zusatzdaten`, nicht am Rumpf. Belegt an der Konstruktionsvorschrift des Senders im Konnektor-Fluss; die Gegenkontrolle ist derselbe Fluss, der für die Nachricht an die Prozess-Engine sehr wohl einen Umschlag baut. **Nicht gemessen:** ein mitgeschnittener echter Aufruf, und der MaloIdent-Zweig (03002/03003), der eigenständig läuft.

Die Schnittstellen-Spezifikation zeigt denselben Rumpf. Der eine Ausreißer mit einem Feld `data` an der Wurzel ist genau **1 von 112** Gliedern des `updateProcessData`-Schemas der Rolle LF und keine zweite Rumpfform.

Die Schlüssel `businessKey`, `prozessId` und `targetBusinessKey` sind im Zusammenhang unter [Schlüssel](/schnittstellen/schluessel) beschrieben.

:::

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Die mit *nicht aus der Zeitscheibe* gekennzeichneten Beschreibungen stehen nicht in `_sources/v202604/bo4e`, sondern in der jeweils genannten Quelle; sie sind redaktionell übernommen und nicht aus den Schemata dieser Seite abgeleitet. Im Zusammenhang beschreibt die Schlüssel die Seite [Schlüssel](/schnittstellen/schluessel).

</Hinweisbereich>
