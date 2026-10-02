# [NB] START_BERECHNUNGSFORMEL
<span hidden data-pagefind-meta={"title:Trigger-Ereignis START_BERECHNUNGSFORMEL — Marktrolle NB (FV 202604)"} />

Marktrolle **NB** · Formatversion **202604** · BO4E-Schema **1.7.8**

## Stammdaten

Unter diesem Topic ist genau einer der folgenden 1 Prüfidentifikatoren zulässig — welcher, entscheidet der Event-Prozess.

| Prüfi | Scope | Anwendungsfall | Festlegung | Kommunikation |
|---|---|---|---|---|
| [PI_25001](/schnittstellen/202604/pruefi/UTILTS/PI_25001) | UTILTS | Berechnungsformel | WiM Strom Teil 2 | NB → MSB (entspricht dem MSB am Objekt Messlokation) |

Die Stammdaten der 1 Prüfidentifikatoren in **einer** Struktur — eine Spalte je Prüfidentifikator, wie im Anwendungshandbuch. Ein Wert in der Spalte heißt, dass das Feld zu diesem Prüfidentifikator gehört: **Muss**, wenn seine Spezifikation es verlangt, sonst **Kann**. Eine leere Zelle heißt »gehört nicht dazu«, nicht »unbekannt«. Vorausgewählt ist der erste; die übrigen schaltet die Leiste über der Tabelle zu.

<Handbuchsatz>

<div className="maco-tabellenrahmen">

| Struktur (BO4E) | Beschreibung | Format | <span className="hbs-p" title="Berechnungsformel">25001</span> | Bedingung |
|---|---|---|---|---|
| <span className="hbs-g hbs-e0">**stammdaten**</span> | — | object | Kann | — |
| <span className="hbs-g hbs-e1">**BERECHNUNGSFORMEL** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-f hbs-e2">[notwendigkeit](/bo4e/202604/bo/Berechnungsformel#notwendigkeit)</span><span className="hbs-nr">00010</span> | Beschreibt ob eine Berechnungsformel notwendig ist | [Enum BerechnungsformelNotwendigkeit](/bo4e/202604/enum/BerechnungsformelNotwendigkeit) | Kann | — |
| <span className="hbs-w hbs-e3">`BERECHNUNGSFORMEL_NOTWENDIG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`BERECHNUNGSFORMEL_MUSS_ANGEFRAGT_WERDEN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`BERECHNUNGSFORMEL_TRIVIAL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`BERECHNUNGSFORMEL_NICHT_NOTWENDIG`</span> | — | — | Kann | — |
| <span className="hbs-f hbs-e2">[rechenschrittId](/bo4e/202604/bo/Berechnungsformel#rechenschrittid)</span><span className="hbs-nr">00020</span> | ID des Rechenschritts [1 - 99999] | integer | Kann | — |
| <span className="hbs-g hbs-e2">**gueltigkeitszeitraum**</span> | — | object | Kann | — |
| <span className="hbs-f hbs-e3">[zeitraumId](/bo4e/202604/com/Zeitraum#zeitraumid)</span><span className="hbs-nr">00030</span> | zeitraumId | integer | Kann | — |
| <span className="hbs-g hbs-e2">**rechenschritte** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-f hbs-e3">[aufteilungsfaktorEnergiemenge](/bo4e/202604/com/Rechenschritt#aufteilungsfaktorenergiemenge)</span><span className="hbs-nr">00040</span> | aufteilungsfaktorEnergiemenge | number (float) | Kann | — |
| <span className="hbs-f hbs-e3">[energieflussrichtung](/bo4e/202604/com/Rechenschritt#energieflussrichtung)</span><span className="hbs-nr">00050</span> | Spezifiziert die Energierichtung einer Markt- und/oder Messlokation | [Enum Energierichtung](/bo4e/202604/enum/Energierichtung) | Kann | — |
| <span className="hbs-w hbs-e4">`AUSSP`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`EINSP`</span> | — | — | Kann | — |
| <span className="hbs-f hbs-e3">[messlokationsId](/bo4e/202604/com/Rechenschritt#messlokationsid)</span><span className="hbs-nr">00060</span> | messlokationsId | string | Kann | — |
| <span className="hbs-f hbs-e3">[operation](/bo4e/202604/com/Rechenschritt#operation)</span><span className="hbs-nr">00070</span> | Mit dieser Aufzählung können arithmetische Operationen festgelegt werden | [Enum ArithmetischeOperation](/bo4e/202604/enum/ArithmetischeOperation) | Kann | — |
| <span className="hbs-w hbs-e4">`ADDITION`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`SUBTRAKTION`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`DIVISION`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`DIVIDEND`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MULTIPLIKATION`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`POSITIVWERT`</span> | — | — | Kann | — |
| <span className="hbs-f hbs-e3">[rechenschrittBestandteilId](/bo4e/202604/com/Rechenschritt#rechenschrittbestandteilid)</span><span className="hbs-nr">00080</span> | rechenschrittBestandteilId | integer | Kann | — |
| <span className="hbs-f hbs-e3">[referenzRechenschrittId](/bo4e/202604/com/Rechenschritt#referenzrechenschrittid)</span><span className="hbs-nr">00090</span> | referenzRechenschrittId | integer | Kann | — |
| <span className="hbs-f hbs-e3">[verlustfaktorLeitung](/bo4e/202604/com/Rechenschritt#verlustfaktorleitung)</span><span className="hbs-nr">00100</span> | verlustfaktorLeitung | number (float) | Kann | — |
| <span className="hbs-f hbs-e3">[verlustfaktorTrafo](/bo4e/202604/com/Rechenschritt#verlustfaktortrafo)</span><span className="hbs-nr">00110</span> | verlustfaktorTrafo | number (float) | Kann | — |
| <span className="hbs-g hbs-e1">**VERWENDUNGSZEITRAUM** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | — |
| <span className="hbs-f hbs-e2">[datenqualitaet](/bo4e/202604/bo/Verwendungszeitraum#datenqualitaet) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00120</span> | Datenqualitaet | [Enum Datenqualitaet](/bo4e/202604/enum/Datenqualitaet) | Muss | — |
| <span className="hbs-w hbs-e3">`ERWARTETE_DATEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`INFORMATIVE_DATEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`GUELTIGE_DATEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_KEINE_DATEN_VORHANDEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN_ERWARTET`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_DATEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_ERWARTETE_DATEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | Muss | — |
| <span className="hbs-f hbs-e2">[verwendungAb](/bo4e/202604/bo/Verwendungszeitraum#verwendungab) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00130</span> | verwendungAb | string (date-time) | Muss | — |
| <span className="hbs-f hbs-e2">[verwendungBis](/bo4e/202604/bo/Verwendungszeitraum#verwendungbis)</span><span className="hbs-nr">00140</span> | verwendungBis | string (date-time) | Kann | — |
| <span className="hbs-f hbs-e2">[zeitraumId](/bo4e/202604/bo/Verwendungszeitraum#zeitraumid) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00150</span> | zeitraumId | integer | Muss | — |

</div>

</Handbuchsatz>

## Kette dieses Auslösers

Das Ereignis löst die Nachricht aus. Der Marktpartner antwortet mit einer der genannten Antworten, und danach schreibt die MACO APP den Vorgang in Ihr Backendsystem.

| Nachricht | Antworten | Schreibaufruf nach der Antwort |
|---|---|---|
| [25001](/schnittstellen/202604/pruefi/UTILTS/PI_25001) | [25010](/schnittstellen/202604/pruefi/UTILTS/PI_25010) | `POST /updateProcessData` |

Dieses Ereignis löst Schritte in diesen Rollensichten aus:

| Prozess | Beteiligter | Regelwerk | Sparte |
|---|---|---|---|
| [Ergänzende Daten zum Lokationsbündel von NBA an NBN](/prozessdoku/202604/NB--NBA/awh-netzbetreiberwechsel-erganzende-daten-zum-lokationsbundel-von-nba-an-nbn) | NBA | AWH Netzbetreiberwechsel | Strom |
| [Übermittlung der Berechnungsformel](/prozessdoku/202604/NB/WiM-Teil2-uebermittlung-der-berechnungsformel) | NB | WiM Strom Teil 2 | Strom |

## Transaktionsdaten

Der Umschlag der Nachricht. Pflichtfelder müssen beim Trigger-Aufruf gesetzt sein.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| [kategorie](/bo4e/202604/cdoc/Transaktionsdaten#kategorie) | string | **ja** | Qualifier aus dem Beginn der EDIFact Nachricht / BGM |
| [lokationsId](/bo4e/202604/cdoc/Transaktionsdaten#lokationsid) | string | **ja** | Referenz auf die Lokation / LOC |
| [lokationsTyp](/bo4e/202604/cdoc/Transaktionsdaten#lokationstyp) | [Enum Lokationstyp](/bo4e/202604/enum/Lokationstyp) | **ja** | Typ der Lokation Werte: `MALO`, `MELO`, `NELO`, `TECHNISCHE_RESSOURCE`, `STEUERBARE_RESSOURCE`, `TRANCHE`, `MABIS_ZAEHLPUNKT` |
| [sparte](/bo4e/202604/cdoc/Transaktionsdaten#sparte) | [Enum Sparte](/bo4e/202604/enum/Sparte) | **ja** | Enthält Informationen über die Sparte Werte: `STROM`, `GAS`, `FERNWAERME`, `NAHWAERME`, `WASSER`, `ABWASSER` |
| `pruefidentifikator` | — | nein | Wird dynamisch im Event-Prozess ermittelt. Ein vom Sender mitgegebener Wert wird ignoriert. Im Topic mögliche Prüfis — 25001. Mögliche Werte: `25001` |
| [absender › rollencodenummer](/bo4e/202604/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |
| [empfaenger › rollencodenummer](/bo4e/202604/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |

## Zusatzdaten

`eventname` ist auf **START_BERECHNUNGSFORMEL** festgelegt. Dieser Wert bleibt auch in der englischen Fassung deutsch, weil Camunda darüber korreliert.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `prozessId` | string | **ja** | — |
| `eventname` | const `START_BERECHNUNGSFORMEL` | **ja** | — |

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
