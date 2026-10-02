# [LF] START_VERSAND_BEST_BEEND_KONFIG
<span hidden data-pagefind-meta={"title:Trigger-Ereignis START_VERSAND_BEST_BEEND_KONFIG — Marktrolle LF (FV 202604)"} />

Marktrolle **LF** · Formatversion **202604** · BO4E-Schema **1.7.8**

## Stammdaten

Unter diesem Topic ist genau einer der folgenden 1 Prüfidentifikatoren zulässig — welcher, entscheidet der Event-Prozess.

| Prüfi | Scope | Anwendungsfall | Festlegung | Kommunikation |
|---|---|---|---|---|
| [PI_17129](/schnittstellen/202604/pruefi/ORDERS/PI_17129) | ORDERS | Bestellung Beendigung einer Konfiguration | GPKE Teil 3 | NB → MSB |

Die Stammdaten der 1 Prüfidentifikatoren in **einer** Struktur — eine Spalte je Prüfidentifikator, wie im Anwendungshandbuch. Ein Wert in der Spalte heißt, dass das Feld zu diesem Prüfidentifikator gehört: **Muss**, wenn seine Spezifikation es verlangt, sonst **Kann**. Eine leere Zelle heißt »gehört nicht dazu«, nicht »unbekannt«. Vorausgewählt ist der erste; die übrigen schaltet die Leiste über der Tabelle zu.

<Handbuchsatz>

<div className="maco-tabellenrahmen">

| Struktur (BO4E) | Beschreibung | Format | <span className="hbs-p" title="Bestellung Beendigung einer Konfiguration">17129</span> | Bedingung |
|---|---|---|---|---|
| <span className="hbs-g hbs-e0">**stammdaten**</span> | — | object | Kann | — |
| <span className="hbs-g hbs-e1">**AUFTRAG** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | — |
| <span className="hbs-f hbs-e2">[ausfuehrungsdatum](/bo4e/202604/bo/Auftrag#ausfuehrungsdatum) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00010</span> | Das Ausführungsdatum beschreibt zu welchem Zeitpunkt ein Auftrag ausgeführt werden soll. | string (date-time) | Muss | — |

</div>

</Handbuchsatz>

## Kette dieses Auslösers

Das Ereignis löst die Nachricht aus.

| Nachricht | Antworten | Schreibaufruf nach der Antwort |
|---|---|---|
| [17129](/schnittstellen/202604/pruefi/ORDERS/PI_17129) | — | — |

Dieses Ereignis löst einen Schritt in dieser Rollensicht aus:

| Prozess | Beteiligter | Regelwerk | Sparte |
|---|---|---|---|
| [Bestellung Beendigung einer Konfiguration vom LF an MSB](/prozessdoku/202604/LF/GPKE-Teil3-bestellung-beendigung-einer-konfiguration-vom-lf-an-msb) | LF | GPKE Teil 3 | Strom |

## Transaktionsdaten

Der Umschlag der Nachricht. Pflichtfelder müssen beim Trigger-Aufruf gesetzt sein.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| [kategorie](/bo4e/202604/cdoc/Transaktionsdaten#kategorie) | string | **ja** | Qualifier aus dem Beginn der EDIFact Nachricht / BGM |
| [nachrichtenReferenzBestellbestaetigung](/bo4e/202604/cdoc/Transaktionsdaten#nachrichtenreferenzbestellbestaetigung) | string | **ja** | Referenznummer der Nachricht der betroffenen Antwort auf Bestellung 'Bestellbestätigung' / ORDERS RFF+Z42 |
| [sparte](/bo4e/202604/cdoc/Transaktionsdaten#sparte) | [Enum Sparte](/bo4e/202604/enum/Sparte) | **ja** | Enthält Informationen über die Sparte Werte: `STROM`, `GAS`, `FERNWAERME`, `NAHWAERME`, `WASSER`, `ABWASSER` |
| [vorgangsReferenzBestellbestaetigung](/bo4e/202604/cdoc/Transaktionsdaten#vorgangsreferenzbestellbestaetigung) | string | **ja** | Referenznummer des Vorgangs der betroffenen Antwort auf Bestellung 'Bestellbestätigung' / ORDERS RFF+Z43 |
| `pruefidentifikator` | — | nein | Wird dynamisch im Event-Prozess ermittelt. Ein vom Sender mitgegebener Wert wird ignoriert. Im Topic mögliche Prüfis — 17129. Mögliche Werte: `17129` |
| [absender › rollencodenummer](/bo4e/202604/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |
| [empfaenger › rollencodenummer](/bo4e/202604/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |

## Zusatzdaten

`eventname` ist auf **START_VERSAND_BEST_BEEND_KONFIG** festgelegt. Dieser Wert bleibt auch in der englischen Fassung deutsch, weil Camunda darüber korreliert.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `prozessId` | string | **ja** | — |
| `eventname` | const `START_VERSAND_BEST_BEEND_KONFIG` | **ja** | — |

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
