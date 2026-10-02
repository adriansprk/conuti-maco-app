# [MSB] START_BESTELLUNG_GERAETEUEBERNAHME
<span hidden data-pagefind-meta={"title:Trigger-Ereignis START_BESTELLUNG_GERAETEUEBERNAHME — Marktrolle MSB (FV 202610)"} />

Marktrolle **MSB** · Formatversion **202610** · BO4E-Schema **1.7.8**

## Stammdaten

Unter diesem Topic ist genau einer der folgenden 1 Prüfidentifikatoren zulässig — welcher, entscheidet der Event-Prozess.

| Prüfi | Scope | Anwendungsfall | Festlegung | Kommunikation |
|---|---|---|---|---|
| [PI_17001](/schnittstellen/202610/pruefi/ORDERS/PI_17001) | ORDERS | Bestellung Geräteübernahmeangebot | WiM Strom Teil 1 | MSB (entspricht MSBN am Objekt Messlokation) → MSB (entspricht MSBA am Objekt Messlokation) |

Die Stammdaten der 1 Prüfidentifikatoren in **einer** Struktur — eine Spalte je Prüfidentifikator, wie im Anwendungshandbuch. Ein Wert in der Spalte heißt, dass das Feld zu diesem Prüfidentifikator gehört: **Muss**, wenn seine Spezifikation es verlangt, sonst **Kann**. Eine leere Zelle heißt »gehört nicht dazu«, nicht »unbekannt«. Vorausgewählt ist der erste; die übrigen schaltet die Leiste über der Tabelle zu.

<Handbuchsatz>

<div className="maco-tabellenrahmen">

| Struktur (BO4E) | Beschreibung | Format | <span className="hbs-p" title="Bestellung Geräteübernahmeangebot">17001</span> | Bedingung |
|---|---|---|---|---|
| <span className="hbs-g hbs-e0">**stammdaten**</span> | — | object | Kann | — |
| <span className="hbs-g hbs-e1">**AUFTRAG** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | — |
| <span className="hbs-f hbs-e2">[ausfuehrungsdatum](/bo4e/202610/bo/Auftrag#ausfuehrungsdatum) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00010</span> | Das Ausführungsdatum beschreibt zu welchem Zeitpunkt ein Auftrag ausgeführt werden soll. | string (date-time) | Muss | — |
| <span className="hbs-g hbs-e2">**positionsdaten** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | — |
| <span className="hbs-f hbs-e3">[apnKommunikationsdaten](/bo4e/202610/com/AuftragPosition#apnkommunikationsdaten)</span><span className="hbs-nr">00020</span> | APN der Kommunikationsdaten | string | Kann | — |
| <span className="hbs-f hbs-e3">[positionsnummer](/bo4e/202610/com/AuftragPosition#positionsnummer) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00030</span> | Positionsnummer | integer | Muss | — |
| <span className="hbs-f hbs-e3">[positionsnummerAngebot](/bo4e/202610/com/AuftragPosition#positionsnummerangebot) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00040</span> | laufende Positionsnummer des Angebot | string | Muss | — |
| <span className="hbs-f hbs-e3">[wakeUpPort](/bo4e/202610/com/AuftragPosition#wakeupport)</span><span className="hbs-nr">00050</span> | Wake-Up-Port der Kommunikationseinheit | string | Kann | — |
| <span className="hbs-g hbs-e3">**endpunktAdresse**</span> | — | object | Kann | — |
| <span className="hbs-f hbs-e4">[gwaAdminService](/bo4e/202610/com/EndpunktAdresse#gwaadminservice)</span><span className="hbs-nr">00060</span> | Endpunktadresse GWA Admin-Service | string | Kann | — |
| <span className="hbs-f hbs-e4">[gwaManagement](/bo4e/202610/com/EndpunktAdresse#gwamanagement)</span><span className="hbs-nr">00070</span> | Endpunktadresse GWA Management | string | Kann | — |
| <span className="hbs-f hbs-e4">[gwaNTP](/bo4e/202610/com/EndpunktAdresse#gwantp)</span><span className="hbs-nr">00080</span> | Endpunktadresse GWA NTP (Zeitserver) | string | Kann | — |
| <span className="hbs-g hbs-e3">**zertifikatsInformationen**</span> | — | object | Kann | — |
| <span className="hbs-f hbs-e4">[commonNameZertifikat](/bo4e/202610/com/Zertifikatsinformationen#commonnamezertifikat)</span><span className="hbs-nr">00090</span> | Common Name (CN) des Zertifikats | string | Kann | — |
| <span className="hbs-f hbs-e4">[seriennummerZertifikat](/bo4e/202610/com/Zertifikatsinformationen#seriennummerzertifikat)</span><span className="hbs-nr">00100</span> | Seriennummer des Zertifikats | string | Kann | — |
| <span className="hbs-f hbs-e4">[uriSubCA](/bo4e/202610/com/Zertifikatsinformationen#urisubca)</span><span className="hbs-nr">00110</span> | URI der Sub-CA | string | Kann | — |

</div>

</Handbuchsatz>

## Kette dieses Auslösers

Das Ereignis löst die Nachricht aus. Der Marktpartner antwortet mit einer der genannten Antworten, und danach schreibt die MACO APP den Vorgang in Ihr Backendsystem.

| Nachricht | Antworten | Schreibaufruf nach der Antwort |
|---|---|---|
| [17001](/schnittstellen/202610/pruefi/ORDERS/PI_17001) | [19001](/schnittstellen/202610/pruefi/ORDRSP/PI_19001), [19002](/schnittstellen/202610/pruefi/ORDRSP/PI_19002) | `POST /updateProcessData` |

Dieses Ereignis löst Schritte in diesen Rollensichten aus:

| Prozess | Beteiligter | Regelwerk | Sparte |
|---|---|---|---|
| [Geräteübernahme](/prozessdoku/202610/MSB--MSBN/awh-wim-gas-2-0-gerateubernahme) | MSBN | AWH WiM Gas 2.0 | Gas |
| [Geräteübernahme](/prozessdoku/202610/MSB--MSBN/WiM-Teil1-geraeteuebernahme) | MSBN | WiM Strom Teil 1 | Strom |

## Transaktionsdaten

Der Umschlag der Nachricht. Pflichtfelder müssen beim Trigger-Aufruf gesetzt sein.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| [kategorie](/bo4e/202610/cdoc/Transaktionsdaten#kategorie) | string | **ja** | Qualifier aus dem Beginn der EDIFact Nachricht / BGM |
| [sparte](/bo4e/202610/cdoc/Transaktionsdaten#sparte) | [Enum Sparte](/bo4e/202610/enum/Sparte) | **ja** | Enthält Informationen über die Sparte Werte: `STROM`, `GAS`, `FERNWAERME`, `NAHWAERME`, `WASSER`, `ABWASSER` |
| `pruefidentifikator` | — | nein | Wird dynamisch im Event-Prozess ermittelt. Ein vom Sender mitgegebener Wert wird ignoriert. Im Topic mögliche Prüfis — 17001. Mögliche Werte: `17001` |
| [absender › marktrolle](/bo4e/202610/bo/Marktteilnehmer#marktrolle) | [Enum Marktrolle](/bo4e/202610/enum/Marktrolle) | nein | Gibt im Klartext die Bezeichnung der Marktrolle an. Werte: `NB`, `LF`, `MSB`, `MSBA`, `GMSB`, `MDL`, `DL`, `BKV`, `UENB`, `KUNDE-SELBST-NN` … (+9) |
| [absender › rollencodenummer](/bo4e/202610/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |
| [empfaenger › marktrolle](/bo4e/202610/bo/Marktteilnehmer#marktrolle) | [Enum Marktrolle](/bo4e/202610/enum/Marktrolle) | nein | Gibt im Klartext die Bezeichnung der Marktrolle an. Werte: `NB`, `LF`, `MSB`, `MSBA`, `GMSB`, `MDL`, `DL`, `BKV`, `UENB`, `KUNDE-SELBST-NN` … (+9) |
| [empfaenger › rollencodenummer](/bo4e/202610/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |

## Zusatzdaten

`eventname` ist auf **START_BESTELLUNG_GERAETEUEBERNAHME** festgelegt. Dieser Wert bleibt auch in der englischen Fassung deutsch, weil Camunda darüber korreliert.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `prozessId` | string | **ja** | — |
| `eventname` | const `START_BESTELLUNG_GERAETEUEBERNAHME` | **ja** | — |

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
