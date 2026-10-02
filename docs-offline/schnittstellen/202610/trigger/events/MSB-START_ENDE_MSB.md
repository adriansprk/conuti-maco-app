# [MSB] START_ENDE_MSB
<span hidden data-pagefind-meta={"title:Trigger-Ereignis START_ENDE_MSB — Marktrolle MSB (FV 202610)"} />

Marktrolle **MSB** · Formatversion **202610** · BO4E-Schema **1.7.8**

:::caution{title="Noch nicht abgebildete Prüfidentifikatoren"}

Für dieses Topic sind die folgenden Prüfidentifikatoren fachlich vorgesehen, aber in der aktuellen Formatversion noch nicht als Spezifikation vorhanden: `44051`.

Die Angabe stammt aus der Generator-Pipeline und wird hier bewusst sichtbar gemacht, statt sie zu verschweigen.

:::

## Stammdaten

Unter diesem Topic ist genau einer der folgenden 1 Prüfidentifikatoren zulässig — welcher, entscheidet der Event-Prozess.

| Prüfi | Scope | Anwendungsfall | Festlegung | Kommunikation |
|---|---|---|---|---|
| [PI_55051](/schnittstellen/202610/pruefi/UTILMD/PI_55051) | UTILMD | Ende MSB | WiM Strom Teil 1 | MSB (entspricht MSBA am Objekt Messlokation) → NB |

Die Stammdaten der 1 Prüfidentifikatoren in **einer** Struktur — eine Spalte je Prüfidentifikator, wie im Anwendungshandbuch. Ein Wert in der Spalte heißt, dass das Feld zu diesem Prüfidentifikator gehört: **Muss**, wenn seine Spezifikation es verlangt, sonst **Kann**. Eine leere Zelle heißt »gehört nicht dazu«, nicht »unbekannt«. Vorausgewählt ist der erste; die übrigen schaltet die Leiste über der Tabelle zu.

<Handbuchsatz>

<div className="maco-tabellenrahmen">

| Struktur (BO4E) | Beschreibung | Format | <span className="hbs-p" title="Ende MSB">55051</span> | Bedingung |
|---|---|---|---|---|
| <span className="hbs-g hbs-e0">**stammdaten**</span> | — | object | Kann | — |
| <span className="hbs-g hbs-e1">**MESSLOKATION** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | — |
| <span className="hbs-f hbs-e2">[messlokationsId](/bo4e/202610/bo/Messlokation#messlokationsid) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00010</span> | Die Messlokations-Identifikation. Das ist die frühere Zählpunktbezeichnung,<br/>z.B. DE 47108151234567 | string | Muss | — |
| <span className="hbs-g hbs-e1">**NETZNUTZUNGSVERTRAG** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-f hbs-e2">[vertragsbeginn](/bo4e/202610/bo/Vertrag#vertragsbeginn)</span><span className="hbs-nr">00020</span> | Gibt an, wann der Vertrag beginnt. | string (date-time) | Kann | — |
| <span className="hbs-f hbs-e2">[vertragsende](/bo4e/202610/bo/Vertrag#vertragsende)</span><span className="hbs-nr">00030</span> | Gibt an, wann der Vertrag (voraussichtlich) endet oder beendet wurde. | string (date-time) | Kann | — |

</div>

</Handbuchsatz>

## Kette dieses Auslösers

Das Ereignis löst die Nachricht aus. Der Marktpartner antwortet mit einer der genannten Antworten, und danach schreibt die MACO APP den Vorgang in Ihr Backendsystem.

| Nachricht | Antworten | Schreibaufruf nach der Antwort |
|---|---|---|
| [55051](/schnittstellen/202610/pruefi/UTILMD/PI_55051) | [55052](/schnittstellen/202610/pruefi/UTILMD/PI_55052), [55053](/schnittstellen/202610/pruefi/UTILMD/PI_55053) | `POST /updateProcessData` |
| `44051` | — | — |

Dieses Ereignis löst einen Schritt in dieser Rollensicht aus:

| Prozess | Beteiligter | Regelwerk | Sparte |
|---|---|---|---|
| [Ende Messstellenbetrieb](/prozessdoku/202610/MSB--MSBA/WiM-Teil1-ende-messstellenbetrieb) | MSBA | WiM Strom Teil 1 | Strom |

## Transaktionsdaten

Der Umschlag der Nachricht. Pflichtfelder müssen beim Trigger-Aufruf gesetzt sein.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `pruefidentifikator` | — | nein | Wird dynamisch im Event-Prozess ermittelt (Entscheidungsgrundlage: sparte). Ein vom Sender mitgegebener Wert wird ignoriert. Im Topic mögliche Prüfis — 44051, 55051. Mögliche Werte: `44051`, `55051` |

## Zusatzdaten

`eventname` ist auf **START_ENDE_MSB** festgelegt. Dieser Wert bleibt auch in der englischen Fassung deutsch, weil Camunda darüber korreliert.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `prozessId` | string | **ja** | — |
| `eventname` | const `START_ENDE_MSB` | **ja** | — |

## Antwort

**Der Auslöser vergibt einen eigenen `businessKey`.** Die MACO APP übernimmt **weder** den `businessKey` **noch** die `prozessId` des aufrufenden Systems als Kennung der Prozessinstanz. Der `businessKey` der Antwort entsteht beim Start des Prozesses und ist neu. Der Rumpf dieses Aufrufs führt kein Feld `businessKey`; es gibt also keine Stelle, an der ein eigener Schlüssel mitgegeben werden könnte. Die mitgegebene `prozessId` (Pflichtfeld dieses Aufrufs) bleibt die Belegnummer des Backends: sie kommt in `zusatzdaten.prozessId` der Callbacks zurück — dort Pflicht nur bei MaloIdent (03002/03003), sonst optional.

**201 — Erfolg.** Erfolgsmeldung auf Prozessdaten API Aufruf.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `businessKey` | string (uuid) | **ja** | Einzigartige Kennung des Geschäftsprozesses |
| `message` | string | **ja** | Nachricht mit Details zum ausgelösten Event — Beispiel der Quelle: `received event XXXXXXXXXXXX with id at 2024-08-08T12:58:22Z and started process with businessKey 4c7170ed-3518-41ee-8582-39ab65b00107` |

**400 — Fehler.** Fehlermeldung auf Prozessdaten API Aufruf.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `errorCode` | string | nein | Error identifier — Beispiel der Quelle: `400` |
| `message` | string | nein | Technische Meldung — Beispiel der Quelle: `Validation Failed` |

Die Antwortschemata (`event_responses_success`, `event_response_fail`) stammen aus `macoapp-trigger.json`, Fassung 1.2.5 (20. Januar 2025), außerhalb der Zeitscheibe: die Datei wird nicht je Formatversion geführt, beide Fassungen lesen dieselbe.

Welchen Rumpf die Callbacks `updateProcessData` und `createProcessData` senden, ist am NiFi-Fluss der MACO APP gemessen: `{stammdaten, transaktionsdaten, zusatzdaten}` ohne Umschlag, der `businessKey` innerhalb von `zusatzdaten`. Nicht gemessen ist das an einem mitgeschnittenen Aufruf, und nicht für MaloIdent (03002/03003).

Was `businessKey`, `prozessId` und `targetBusinessKey` unterscheidet, steht auf [Schlüssel und Zuordnung](/schnittstellen/schluessel).
