# [LF] START_BESTELLUNG_ZAEHLZEITDEFINITION
<span hidden data-pagefind-meta={"title:Trigger-Ereignis START_BESTELLUNG_ZAEHLZEITDEFINITION — Marktrolle LF (FV 202604)"} />

Marktrolle **LF** · Formatversion **202604** · BO4E-Schema **1.7.8**

## Stammdaten

Unter diesem Topic ist genau einer der folgenden 1 Prüfidentifikatoren zulässig — welcher, entscheidet der Event-Prozess.

| Prüfi | Scope | Anwendungsfall | Festlegung | Kommunikation |
|---|---|---|---|---|
| [PI_17123](/schnittstellen/202604/pruefi/ORDERS/PI_17123) | ORDERS | Bestellung Änderung Zählzeitdefinition | GPKE Teil 3 | LF → NB |

Die Stammdaten der 1 Prüfidentifikatoren in **einer** Struktur — eine Spalte je Prüfidentifikator, wie im Anwendungshandbuch. Ein Wert in der Spalte heißt, dass das Feld zu diesem Prüfidentifikator gehört: **Muss**, wenn seine Spezifikation es verlangt, sonst **Kann**. Eine leere Zelle heißt »gehört nicht dazu«, nicht »unbekannt«. Vorausgewählt ist der erste; die übrigen schaltet die Leiste über der Tabelle zu.

<Handbuchsatz>

<div className="maco-tabellenrahmen">

| Struktur (BO4E) | Beschreibung | Format | <span className="hbs-p" title="Bestellung Änderung Zählzeitdefinition">17123</span> | Bedingung |
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
| <span className="hbs-f hbs-e2">[lokationsId](/bo4e/202604/bo/Anfrage#lokationsid) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00020</span> | Für welche Markt- oder Messlokation gilt diese Anfrage. | string | Muss | — |
| <span className="hbs-g hbs-e1">**AUFTRAG** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | — |
| <span className="hbs-f hbs-e2">[ausfuehrungsdatum](/bo4e/202604/bo/Auftrag#ausfuehrungsdatum) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00030</span> | Das Ausführungsdatum beschreibt zu welchem Zeitpunkt ein Auftrag ausgeführt werden soll. | string (date-time) | Muss | — |
| <span className="hbs-g hbs-e1">**MARKTLOKATION** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-g hbs-e2">**zaehlwerke** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-f hbs-e3">[messprodukt](/bo4e/202604/com/Zaehlwerk#messprodukt)</span><span className="hbs-nr">00040</span> | messprodukt | string | Kann | — |
| <span className="hbs-g hbs-e3">**zaehlzeiten**</span> | — | object | Kann | — |
| <span className="hbs-f hbs-e4">[zaehlzeitDefinition](/bo4e/202604/com/Zaehlzeitregister#zaehlzeitdefinition)</span><span className="hbs-nr">00050</span> | Zählzeitdefinition | string | Kann | — |

</div>

</Handbuchsatz>

## Kette dieses Auslösers

Das Ereignis löst die Nachricht aus. Der Marktpartner antwortet mit einer der genannten Antworten, und danach schreibt die MACO APP den Vorgang in Ihr Backendsystem.

| Nachricht | Antworten | Schreibaufruf nach der Antwort |
|---|---|---|
| [17123](/schnittstellen/202604/pruefi/ORDERS/PI_17123) | [19124](/schnittstellen/202604/pruefi/ORDRSP/PI_19124) | `POST /createProcessData` |

Dieses Ereignis löst Schritte in diesen Rollensichten aus:

| Prozess | Beteiligter | Regelwerk | Sparte |
|---|---|---|---|
| [Bestellung einer Konfiguration vom LF an MSB](/prozessdoku/202604/LF/GPKE-Teil3-bestellung-einer-konfiguration-vom-lf-an-msb) | LF | GPKE Teil 3 | Strom |
| [Bestellung einer Konfiguration vom LF an NB](/prozessdoku/202604/LF/GPKE-Teil3-bestellung-einer-konfiguration-vom-lf-an-nb) | LF | GPKE Teil 3 | Strom |

## Transaktionsdaten

Der Umschlag der Nachricht. Pflichtfelder müssen beim Trigger-Aufruf gesetzt sein.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| [kategorie](/bo4e/202604/cdoc/Transaktionsdaten#kategorie) | string | **ja** | Qualifier aus dem Beginn der EDIFact Nachricht / BGM |
| [sparte](/bo4e/202604/cdoc/Transaktionsdaten#sparte) | [Enum Sparte](/bo4e/202604/enum/Sparte) | **ja** | Enthält Informationen über die Sparte Werte: `STROM`, `GAS`, `FERNWAERME`, `NAHWAERME`, `WASSER`, `ABWASSER` |
| `pruefidentifikator` | — | nein | Wird dynamisch im Event-Prozess ermittelt. Ein vom Sender mitgegebener Wert wird ignoriert. Im Topic mögliche Prüfis — 17123. Mögliche Werte: `17123` |
| [absender › rollencodenummer](/bo4e/202604/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |
| [empfaenger › rollencodenummer](/bo4e/202604/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |

## Zusatzdaten

`eventname` ist auf **START_BESTELLUNG_ZAEHLZEITDEFINITION** festgelegt. Dieser Wert bleibt auch in der englischen Fassung deutsch, weil Camunda darüber korreliert.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `prozessId` | string | **ja** | — |
| `eventname` | const `START_BESTELLUNG_ZAEHLZEITDEFINITION` | **ja** | — |

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
