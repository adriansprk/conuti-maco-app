# [MSB] START_ANFORDERUNG_MESSWERTE
<span hidden data-pagefind-meta={"title:Trigger-Ereignis START_ANFORDERUNG_MESSWERTE — Marktrolle MSB (FV 202604)"} />

Marktrolle **MSB** · Formatversion **202604** · BO4E-Schema **1.7.8**

## Stammdaten

Unter diesem Topic ist genau einer der folgenden 1 Prüfidentifikatoren zulässig — welcher, entscheidet der Event-Prozess.

| Prüfi | Scope | Anwendungsfall | Festlegung | Kommunikation |
|---|---|---|---|---|
| [PI_17004](/schnittstellen/202604/pruefi/ORDERS/PI_17004) | ORDERS | Anforderung von Werten | WiM Strom Teil 2 | NB → MSB (entspricht MSB am Objekt Marktlokation) |

Die Stammdaten der 1 Prüfidentifikatoren in **einer** Struktur — eine Spalte je Prüfidentifikator, wie im Anwendungshandbuch. Ein Wert in der Spalte heißt, dass das Feld zu diesem Prüfidentifikator gehört: **Muss**, wenn seine Spezifikation es verlangt, sonst **Kann**. Eine leere Zelle heißt »gehört nicht dazu«, nicht »unbekannt«. Vorausgewählt ist der erste; die übrigen schaltet die Leiste über der Tabelle zu.

<Handbuchsatz>

<div className="maco-tabellenrahmen">

| Struktur (BO4E) | Beschreibung | Format | <span className="hbs-p" title="Anforderung von Werten">17004</span> | Bedingung |
|---|---|---|---|---|
| <span className="hbs-g hbs-e0">**stammdaten**</span> | — | object | Kann | — |
| <span className="hbs-g hbs-e1">**ANFRAGE** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | — |
| <span className="hbs-f hbs-e2">[anfragetyp](/bo4e/202604/bo/Anfrage#anfragetyp) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00010</span> | Typ/Art der Anfrage (ORDERS ORDRSP IMD 7081) | [Enum Anfragetyp](/bo4e/202604/enum/Anfragetyp) | Muss | — |
| <span className="hbs-w hbs-e3">`KAUF`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`NUTZUNGSUEBERLASSUNG`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`ABRECHNUNGSBRENNWERT_UND_ZUSTANDSZAHL`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`LASTGANGDATEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`ZAEHLERSTAENDE`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`WERTEERMITTLUNG`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`ENERGIEMENGE_EINZELWERT`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`INNERHALB_DER_ARBEITSZEIT`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`AUCH_AUSSERHALB_DER_ARBEITSZEIT`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`WECHSEL_SAEMTLICHER_EINRICHTUNGEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`TEILWEISER_WECHSEL`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`AENDERUNG_ZAEHLZEITDEFINITION`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`ABBESTELLUNG_ZAEHLZEITEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`ABBESTELLUNG_MESSPRODUKT`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`ANGEBOT_AUF_BASIS_PREISBLATT`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`INDIVIDUELLES_ANGEBOT`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`AENDERUNG_KONFIGURATION`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`KANN_NICHT_ANGEBOTEN_WERDEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`NEUKONFIGURATION`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`BEENDIGUNG_KONFIGURATION`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`AKTIVIERUNG_KONFIGURATION`</span> | — | — | Muss | — |
| <span className="hbs-f hbs-e2">[gueltigAb](/bo4e/202604/bo/Anfrage#gueltigab) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00020</span> | gueltigAb | string (date-time) | Muss | — |
| <span className="hbs-f hbs-e2">[lokationsId](/bo4e/202604/bo/Anfrage#lokationsid) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00030</span> | Für welche Markt- oder Messlokation gilt diese Anfrage. | string | Muss | — |
| <span className="hbs-g hbs-e1">**AUFTRAG** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | — |
| <span className="hbs-g hbs-e2">**positionsdaten** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | — |
| <span className="hbs-f hbs-e3">[anfragegrund](/bo4e/202604/com/AuftragPosition#anfragegrund) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00040</span> | Anfragegrund | [Enum Anfragegrund](/bo4e/202604/enum/Anfragegrund) | Muss | — |
| <span className="hbs-w hbs-e4">`ABGRENZUNG_VON_ENERGIEMENGEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`ABGRENZUNG`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`WECHSELEREIGNIS`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`ZWISCHENABLESUNG`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`DIREKTER_VERTRAG_MSB_AN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`DIREKTER_VERTRAG_MSB_ANN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`AENDERUNG_IM_LOKATIONSBUENDEL`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`NEUKONFIGURATION`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`KONFIGURATION_UNVERAENDERT`</span> | — | — | Muss | — |

</div>

</Handbuchsatz>

## Kette dieses Auslösers

Das Ereignis löst die Nachricht aus. Der Marktpartner antwortet mit einer der genannten Antworten, und danach schreibt die MACO APP den Vorgang in Ihr Backendsystem.

| Nachricht | Antworten | Schreibaufruf nach der Antwort |
|---|---|---|
| [17004](/schnittstellen/202604/pruefi/ORDERS/PI_17004) | [19007](/schnittstellen/202604/pruefi/ORDRSP/PI_19007) | `POST /updateProcessData` (abgeleitet) |

Dieses Ereignis löst Schritte in diesen Rollensichten aus:

| Prozess | Beteiligter | Regelwerk | Sparte |
|---|---|---|---|
| [Anforderung Wert vom LF](/prozessdoku/202604/MSB--MSB-MALO/WiM-Teil2-anforderung-wert-vom-lf) | MSB-MALO | WiM Strom Teil 2 | Strom |
| [Anforderung Wert vom MSB der Marktlokation](/prozessdoku/202604/MSB--MSB-MALO/WiM-Teil2-anforderung-wert-vom-msb-der-marktlokation) | MSB-MALO | WiM Strom Teil 2 | Strom |
| [Anforderung Wert vom NB](/prozessdoku/202604/MSB--MSB-MALO/WiM-Teil2-anforderung-wert-vom-nb) | MSB-MALO | WiM Strom Teil 2 | Strom |

## Transaktionsdaten

Der Umschlag der Nachricht. Pflichtfelder müssen beim Trigger-Aufruf gesetzt sein.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `pruefidentifikator` | — | nein | Wird dynamisch im Event-Prozess ermittelt. Ein vom Sender mitgegebener Wert wird ignoriert. Im Topic mögliche Prüfis — 17004. Mögliche Werte: `17004` |

## Zusatzdaten

`eventname` ist auf **START_ANFORDERUNG_MESSWERTE** festgelegt. Dieser Wert bleibt auch in der englischen Fassung deutsch, weil Camunda darüber korreliert.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `prozessId` | string | **ja** | — |
| `eventname` | const `START_ANFORDERUNG_MESSWERTE` | **ja** | — |

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
