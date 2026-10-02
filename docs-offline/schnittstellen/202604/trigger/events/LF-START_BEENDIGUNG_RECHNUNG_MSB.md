# [LF] START_BEENDIGUNG_RECHNUNG_MSB
<span hidden data-pagefind-meta={"title:Trigger-Ereignis START_BEENDIGUNG_RECHNUNG_MSB — Marktrolle LF (FV 202604)"} />

Marktrolle **LF** · Formatversion **202604** · BO4E-Schema **1.7.8**

## Stammdaten

Unter diesem Topic ist genau einer der folgenden 1 Prüfidentifikatoren zulässig — welcher, entscheidet der Event-Prozess.

| Prüfi | Scope | Anwendungsfall | Festlegung | Kommunikation |
|---|---|---|---|---|
| [PI_17006](/schnittstellen/202604/pruefi/ORDERS/PI_17006) | ORDERS | Beendigung Rechnungsabwicklung MSB über LF | WiM Strom Teil 1 | MSB (entspricht MSB am Objekt Marktlokation) → LF |

Die Stammdaten der 1 Prüfidentifikatoren in **einer** Struktur — eine Spalte je Prüfidentifikator, wie im Anwendungshandbuch. Ein Wert in der Spalte heißt, dass das Feld zu diesem Prüfidentifikator gehört: **Muss**, wenn seine Spezifikation es verlangt, sonst **Kann**. Eine leere Zelle heißt »gehört nicht dazu«, nicht »unbekannt«. Vorausgewählt ist der erste; die übrigen schaltet die Leiste über der Tabelle zu.

<Handbuchsatz>

<div className="maco-tabellenrahmen">

| Struktur (BO4E) | Beschreibung | Format | <span className="hbs-p" title="Beendigung Rechnungsabwicklung MSB über LF">17006</span> | Bedingung |
|---|---|---|---|---|
| <span className="hbs-g hbs-e0">**stammdaten**</span> | — | object | Kann | — |
| <span className="hbs-g hbs-e1">**ANFRAGE** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | — |
| <span className="hbs-f hbs-e2">[abonnement](/bo4e/202604/bo/Anfrage#abonnement) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00010</span> | Start oder Ende Abo | [Enum Abonnement](/bo4e/202604/enum/Abonnement) | Muss | — |
| <span className="hbs-w hbs-e3">`START_ABO`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`ENDE_ABO`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`OHNE_ABO`</span> | — | — | Muss | — |
| <span className="hbs-f hbs-e2">[lokationsId](/bo4e/202604/bo/Anfrage#lokationsid) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00020</span> | Für welche Markt- oder Messlokation gilt diese Anfrage. | string | Muss | — |
| <span className="hbs-g hbs-e1">**AUFTRAG** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | — |
| <span className="hbs-f hbs-e2">[ausfuehrungsdatum](/bo4e/202604/bo/Auftrag#ausfuehrungsdatum) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00030</span> | Das Ausführungsdatum beschreibt zu welchem Zeitpunkt ein Auftrag ausgeführt werden soll. | string (date-time) | Muss | — |
| <span className="hbs-g hbs-e2">**positionsdaten** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-f hbs-e3">[anfragegrund](/bo4e/202604/com/AuftragPosition#anfragegrund)</span><span className="hbs-nr">00040</span> | Anfragegrund | [Enum Anfragegrund](/bo4e/202604/enum/Anfragegrund) | Kann | — |
| <span className="hbs-w hbs-e4">`ABGRENZUNG_VON_ENERGIEMENGEN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`ABGRENZUNG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`WECHSELEREIGNIS`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`ZWISCHENABLESUNG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`DIREKTER_VERTRAG_MSB_AN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`DIREKTER_VERTRAG_MSB_ANN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`AENDERUNG_IM_LOKATIONSBUENDEL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`NEUKONFIGURATION`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`KONFIGURATION_UNVERAENDERT`</span> | — | — | Kann | — |

</div>

</Handbuchsatz>

## Kette dieses Auslösers

Das Ereignis löst die Nachricht aus. Der Marktpartner antwortet mit einer der genannten Antworten, und danach schreibt die MACO APP den Vorgang in Ihr Backendsystem.

| Nachricht | Antworten | Schreibaufruf nach der Antwort |
|---|---|---|
| [17006](/schnittstellen/202604/pruefi/ORDERS/PI_17006) | [19009](/schnittstellen/202604/pruefi/ORDRSP/PI_19009), [19010](/schnittstellen/202604/pruefi/ORDRSP/PI_19010) | `POST /updateProcessData` (abgeleitet) |

Dieses Ereignis löst einen Schritt in dieser Rollensicht aus:

| Prozess | Beteiligter | Regelwerk | Sparte |
|---|---|---|---|
| [Beendigung Rechnungsabwicklung des Messstellenbetriebes über den LF durch den LF](/prozessdoku/202604/LF/WiM-Teil1-beendigung-rechnungsabwicklung-des-messstellenbetriebes-ueber-den-lf-durch-den-lf) | LF | WiM Strom Teil 1 | Strom |

## Transaktionsdaten

Der Umschlag der Nachricht. Pflichtfelder müssen beim Trigger-Aufruf gesetzt sein.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `pruefidentifikator` | — | nein | Wird dynamisch im Event-Prozess ermittelt. Ein vom Sender mitgegebener Wert wird ignoriert. Im Topic mögliche Prüfis — 17006. Mögliche Werte: `17006` |

## Zusatzdaten

`eventname` ist auf **START_BEENDIGUNG_RECHNUNG_MSB** festgelegt. Dieser Wert bleibt auch in der englischen Fassung deutsch, weil Camunda darüber korreliert.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `prozessId` | string | **ja** | — |
| `eventname` | const `START_BEENDIGUNG_RECHNUNG_MSB` | **ja** | — |

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
