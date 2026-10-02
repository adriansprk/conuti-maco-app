# [LF] START_VERSAND_STOERUNGSMELDUNG
<span hidden data-pagefind-meta={"title:Trigger-Ereignis START_VERSAND_STOERUNGSMELDUNG — Marktrolle LF (FV 202610)"} />

Marktrolle **LF** · Formatversion **202610** · BO4E-Schema **1.7.8**

## Stammdaten

Unter diesem Topic ist genau einer der folgenden 1 Prüfidentifikatoren zulässig — welcher, entscheidet der Event-Prozess.

| Prüfi | Scope | Anwendungsfall | Festlegung | Kommunikation |
|---|---|---|---|---|
| [PI_23001](/schnittstellen/202610/pruefi/INSRPT/PI_23001) | INSRPT | Störungsmeldung | WiM Strom Teil 2 | Störungsmelder → MSB (entspricht MSB am Objekt Messlokation) |

Die Stammdaten der 1 Prüfidentifikatoren in **einer** Struktur — eine Spalte je Prüfidentifikator, wie im Anwendungshandbuch. Ein Wert in der Spalte heißt, dass das Feld zu diesem Prüfidentifikator gehört: **Muss**, wenn seine Spezifikation es verlangt, sonst **Kann**. Eine leere Zelle heißt »gehört nicht dazu«, nicht »unbekannt«. Vorausgewählt ist der erste; die übrigen schaltet die Leiste über der Tabelle zu.

<Handbuchsatz>

<div className="maco-tabellenrahmen">

| Struktur (BO4E) | Beschreibung | Format | <span className="hbs-p" title="Störungsmeldung">23001</span> | Bedingung |
|---|---|---|---|---|
| <span className="hbs-g hbs-e0">**stammdaten**</span> | — | object | Kann | — |
| <span className="hbs-g hbs-e1">**STATUSMITTEILUNG** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | — |
| <span className="hbs-g hbs-e2">**positionsdaten** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | — |
| <span className="hbs-f hbs-e3">[auftragsstatus](/bo4e/202610/com/StatusmitteilungPosition#auftragsstatus) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00010</span> | Auftragsstatus | [Enum Auftragsstatus](/bo4e/202610/enum/Auftragsstatus) | Muss | — |
| <span className="hbs-w hbs-e4">`GESCHEITERT`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`ERFOLGREICH`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`LIEFERUNG_GEPLANT`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`GEPLANT`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`ZUGESTIMMT`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`WIDERSPROCHEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`STOERUNGSFREI`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`GESTOERT`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`FESTGESTELLTE_STOERUNG`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`VERMUTETE_STOERUNG`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`ABGELEHNT`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`BEENDET`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`ANTWORT_DRITTER`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`BESTAETIGT`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`UMGESETZT`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`ENFG_STROMSPEICHER_UND_VERLUSTENERGIE`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`ENFG_ELEKTRISCH_ANGETRIEBENE_WAERMEPUMPEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`ENFG_UMLAGEERHEBUNG_BEI_ANLAGEN_ZUR_VERSTROMUNG_VON_KUPPELGASEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`ENFG_HERSTELLUNG_VON_GRUENEN_WASSERSTOFF`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`ENFG_STROMKOSTENINTENSIVE_UNTERNEHMEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`ENFG_HERSTELLUNG_VON_WASSERSTOFF_IN_STROMKOSTENINTENSIVEN_UNTERNEHMEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`ENFG_SCHIENENBAHNEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`ENFG_ELEKTRISCHE_BETRIEBENE_BUSSEN_IM_LINIENVERKEHR`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`ENFG_LANDSTROMANLAGEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`AENDERUNG_DER_DATEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`KEINE_AENDERUNG_DER_DATEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`ZEITREIHE_AKZEPTIERT`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`ZEITREIHE_NICHT_AKZEPTIERT`</span> | — | — | Muss | — |
| <span className="hbs-f hbs-e3">[lokationsId](/bo4e/202610/com/StatusmitteilungPosition#lokationsid) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00020</span> | lokationsId | string | Muss | — |
| <span className="hbs-f hbs-e3">[positionsnummer](/bo4e/202610/com/StatusmitteilungPosition#positionsnummer) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00030</span> | positionsnummer | integer | Muss | — |
| <span className="hbs-f hbs-e3">[verwendungAb](/bo4e/202610/com/StatusmitteilungPosition#verwendungab)</span><span className="hbs-nr">00040</span> | verwendungAb | string (date-time) | Kann | — |
| <span className="hbs-g hbs-e3">**begruendung**</span> | — | object | Kann | — |
| <span className="hbs-f hbs-e4">[begruendung1](/bo4e/202610/com/Begruendung#begruendung1)</span><span className="hbs-nr">00050</span> | Begruendung Zeile 1 | string | Kann | — |
| <span className="hbs-f hbs-e4">[begruendung2](/bo4e/202610/com/Begruendung#begruendung2)</span><span className="hbs-nr">00060</span> | Begruendung Zeile 2 | string | Kann | — |
| <span className="hbs-f hbs-e4">[begruendung3](/bo4e/202610/com/Begruendung#begruendung3)</span><span className="hbs-nr">00070</span> | Begruendung Zeile 3 | string | Kann | — |
| <span className="hbs-f hbs-e4">[begruendung4](/bo4e/202610/com/Begruendung#begruendung4)</span><span className="hbs-nr">00080</span> | Begruendung Zeile 4 | string | Kann | — |
| <span className="hbs-f hbs-e4">[begruendung5](/bo4e/202610/com/Begruendung#begruendung5)</span><span className="hbs-nr">00090</span> | Begruendung Zeile 5 | string | Kann | — |

</div>

</Handbuchsatz>

## Kette dieses Auslösers

Das Ereignis löst die Nachricht aus. Der Marktpartner antwortet mit einer der genannten Antworten, und danach schreibt die MACO APP den Vorgang in Ihr Backendsystem.

| Nachricht | Antworten | Schreibaufruf nach der Antwort |
|---|---|---|
| [23001](/schnittstellen/202610/pruefi/INSRPT/PI_23001) | [23003](/schnittstellen/202610/pruefi/INSRPT/PI_23003), [23004](/schnittstellen/202610/pruefi/INSRPT/PI_23004) | `POST /updateProcessData` (abgeleitet) |

Dieses Ereignis löst einen Schritt in dieser Rollensicht aus:

| Prozess | Beteiligter | Regelwerk | Sparte |
|---|---|---|---|
| [Störungsbehebung in der Messlokation](/prozessdoku/202610/LF/awh-wim-gas-2-0-storungsbehebung-in-der-messlokation) | LF | AWH WiM Gas 2.0 | Gas |

## Transaktionsdaten

Der Umschlag der Nachricht. Pflichtfelder müssen beim Trigger-Aufruf gesetzt sein.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| [kategorie](/bo4e/202610/cdoc/Transaktionsdaten#kategorie) | string | **ja** | Qualifier aus dem Beginn der EDIFact Nachricht / BGM |
| [sparte](/bo4e/202610/cdoc/Transaktionsdaten#sparte) | [Enum Sparte](/bo4e/202610/enum/Sparte) | **ja** | Enthält Informationen über die Sparte Werte: `STROM`, `GAS`, `FERNWAERME`, `NAHWAERME`, `WASSER`, `ABWASSER` |
| `pruefidentifikator` | — | nein | Wird dynamisch im Event-Prozess ermittelt. Ein vom Sender mitgegebener Wert wird ignoriert. Im Topic mögliche Prüfis — 23001. Mögliche Werte: `23001` |
| [absender › rollencodenummer](/bo4e/202610/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |
| [empfaenger › rollencodenummer](/bo4e/202610/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |

## Zusatzdaten

`eventname` ist auf **START_VERSAND_STOERUNGSMELDUNG** festgelegt. Dieser Wert bleibt auch in der englischen Fassung deutsch, weil Camunda darüber korreliert.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `prozessId` | string | **ja** | — |
| `eventname` | const `START_VERSAND_STOERUNGSMELDUNG` | **ja** | — |

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
