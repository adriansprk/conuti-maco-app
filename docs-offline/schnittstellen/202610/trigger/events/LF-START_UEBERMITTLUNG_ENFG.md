# [LF] START_UEBERMITTLUNG_ENFG
<span hidden data-pagefind-meta={"title:Trigger-Ereignis START_UEBERMITTLUNG_ENFG — Marktrolle LF (FV 202610)"} />

Marktrolle **LF** · Formatversion **202610** · BO4E-Schema **1.7.8**

## Stammdaten

Unter diesem Topic ist genau einer der folgenden 1 Prüfidentifikatoren zulässig — welcher, entscheidet der Event-Prozess.

| Prüfi | Scope | Anwendungsfall | Festlegung | Kommunikation |
|---|---|---|---|---|
| [PI_21045](/schnittstellen/202610/pruefi/IFTSTA/PI_21045) | IFTSTA | EnFG Informationen | GPKE Teil 4 | LF → NB |

Die Stammdaten der 1 Prüfidentifikatoren in **einer** Struktur — eine Spalte je Prüfidentifikator, wie im Anwendungshandbuch. Ein Wert in der Spalte heißt, dass das Feld zu diesem Prüfidentifikator gehört: **Muss**, wenn seine Spezifikation es verlangt, sonst **Kann**. Eine leere Zelle heißt »gehört nicht dazu«, nicht »unbekannt«. Vorausgewählt ist der erste; die übrigen schaltet die Leiste über der Tabelle zu.

<Handbuchsatz>

<div className="maco-tabellenrahmen">

| Struktur (BO4E) | Beschreibung | Format | <span className="hbs-p" title="EnFG Informationen">21045</span> | Bedingung |
|---|---|---|---|---|
| <span className="hbs-g hbs-e0">**stammdaten**</span> | — | object | Kann | — |
| <span className="hbs-g hbs-e1">**ENERGIELIEFERVERTRAG** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-g hbs-e2">**vertragspartner2** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-f hbs-e3">[anrede](/bo4e/202610/bo/Geschaeftspartner#anrede)</span><span className="hbs-nr">00010</span> | Die Anrede für den GePa, Z.B. Herr. | string | Kann | — |
| <span className="hbs-f hbs-e3">[geschaeftspartnerrolle](/bo4e/202610/bo/Geschaeftspartner#geschaeftspartnerrolle)</span><span className="hbs-nr">00020</span> | Rolle, die der Geschäftspartner hat (z.B. Interessent, Kunde). | array | Kann | — |
| <span className="hbs-f hbs-e3">[gewerbekennzeichnung](/bo4e/202610/bo/Geschaeftspartner#gewerbekennzeichnung)</span><span className="hbs-nr">00030</span> | Kennzeichnung ob es sich um einen Gewerbe/Unternehmen (gewerbeKennzeichnung = true)<br/>oder eine Privatperson handelt. (gewerbeKennzeichnung = false) | boolean | Kann | — |
| <span className="hbs-f hbs-e3">[name1](/bo4e/202610/bo/Geschaeftspartner#name1)</span><span className="hbs-nr">00040</span> | Erster Teil des Namens. Hier kann der Firmenname oder bei Privatpersonen<br/>beispielsweise der Nachname dargestellt werden. Beispiele: Yellow Strom GmbH<br/>oder Hagen | string | Kann | — |
| <span className="hbs-f hbs-e3">[name2](/bo4e/202610/bo/Geschaeftspartner#name2)</span><span className="hbs-nr">00050</span> | Zweiter Teil des Namens. Hier kann der eine Erweiterung zum Firmennamen oder<br/>bei Privatpersonen beispielsweise der Vorname dargestellt werden. Beispiele:<br/>Bereich Süd oder Nina | string | Kann | — |
| <span className="hbs-f hbs-e3">[name3](/bo4e/202610/bo/Geschaeftspartner#name3)</span><span className="hbs-nr">00060</span> | Dritter Teil des Namens. Hier können weitere Ergänzungen zum Firmennamen oder<br/>bei Privatpersonen Zusätze zum Namen dargestellt werden. Beispiele: und Afrika<br/>oder Sängerin | string | Kann | — |
| <span className="hbs-f hbs-e3">[name4](/bo4e/202610/bo/Geschaeftspartner#name4)</span><span className="hbs-nr">00070</span> | name4 | string | Kann | — |
| <span className="hbs-g hbs-e1">**STATUSMITTEILUNG** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | — |
| <span className="hbs-g hbs-e2">**positionsdaten** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | — |
| <span className="hbs-f hbs-e3">[allgemeineInformationenText](/bo4e/202610/com/StatusmitteilungPosition#allgemeineinformationentext)</span><span className="hbs-nr">00080</span> | Allgemeine Informationen | string | Kann | — |
| <span className="hbs-f hbs-e3">[auftragsStatusListe](/bo4e/202610/com/StatusmitteilungPosition#auftragsstatusliste) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00090</span> | auftragsStatusListe | array | Muss | — |
| <span className="hbs-f hbs-e3">[gueltigkeitsZeitspanne](/bo4e/202610/com/StatusmitteilungPosition#gueltigkeitszeitspanne) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00100</span> | gueltigkeitsZeitspanne | string | Muss | — |
| <span className="hbs-f hbs-e3">[lokationsId](/bo4e/202610/com/StatusmitteilungPosition#lokationsid) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00110</span> | lokationsId | string | Muss | — |
| <span className="hbs-f hbs-e3">[positionsnummer](/bo4e/202610/com/StatusmitteilungPosition#positionsnummer) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00120</span> | positionsnummer | integer | Muss | — |
| <span className="hbs-f hbs-e3">[sendungsposition](/bo4e/202610/com/StatusmitteilungPosition#sendungsposition)</span><span className="hbs-nr">00130</span> | sendungsposition | integer | Kann | — |
| <span className="hbs-g hbs-e3">**privilegierteEnergiemenge** <span className="hbs-pflicht">\*</span></span> | — | object | Muss | — |
| <span className="hbs-f hbs-e4">[verwendungAb](/bo4e/202610/com/ZeitintervallMenge#verwendungab) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00140</span> | verwendungAb | string (date-time) | Muss | — |
| <span className="hbs-f hbs-e4">[verwendungBis](/bo4e/202610/com/ZeitintervallMenge#verwendungbis) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00150</span> | verwendungBis | string (date-time) | Muss | — |
| <span className="hbs-g hbs-e4">**menge** <span className="hbs-pflicht">\*</span></span> | — | object | Muss | — |
| <span className="hbs-f hbs-e5">[einheit](/bo4e/202610/com/Menge#einheit) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00160</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202610/enum/Mengeneinheit) | Muss | — |
| <span className="hbs-w hbs-e5">`W`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`WH`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`KW`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`KWH`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`KVARH`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`MW`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`MWH`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`STUECK`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`KUBIKMETER`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`STUNDE`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`TAG`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`MONAT`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`JAHR`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`PROZENT`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`ANZAHL`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`VAR`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`KVAR`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`VARH`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`KWHK`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`Z16`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`KWT`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`WATT_PRO_QUADRATMETER`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`METER_PRO_SEKUNDE`</span> | — | — | Muss | — |
| <span className="hbs-f hbs-e5">[wert](/bo4e/202610/com/Menge#wert) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00170</span> | Wert | number (float) | Muss | — |

</div>

</Handbuchsatz>

## Kette dieses Auslösers

Das Ereignis löst die Nachricht aus.

| Nachricht | Antworten | Schreibaufruf nach der Antwort |
|---|---|---|
| [21045](/schnittstellen/202610/pruefi/IFTSTA/PI_21045) | — | — |

Dieses Ereignis löst einen Schritt in dieser Rollensicht aus:

| Prozess | Beteiligter | Regelwerk | Sparte |
|---|---|---|---|
| [Übermittlung von Informationen](/prozessdoku/202610/LF/GPKE-Teil4-uebermittlung-von-informationen) | LF | GPKE Teil 4 | Strom |

## Transaktionsdaten

Der Umschlag der Nachricht. Pflichtfelder müssen beim Trigger-Aufruf gesetzt sein.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| [kategorie](/bo4e/202610/cdoc/Transaktionsdaten#kategorie) | string | **ja** | Qualifier aus dem Beginn der EDIFact Nachricht / BGM |
| [sparte](/bo4e/202610/cdoc/Transaktionsdaten#sparte) | [Enum Sparte](/bo4e/202610/enum/Sparte) | **ja** | Enthält Informationen über die Sparte Werte: `STROM`, `GAS`, `FERNWAERME`, `NAHWAERME`, `WASSER`, `ABWASSER` |
| `pruefidentifikator` | — | nein | Wird dynamisch im Event-Prozess ermittelt. Ein vom Sender mitgegebener Wert wird ignoriert. Im Topic mögliche Prüfis — 21045. Mögliche Werte: `21045` |
| [absender › rollencodenummer](/bo4e/202610/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |
| [empfaenger › rollencodenummer](/bo4e/202610/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |

## Zusatzdaten

`eventname` ist auf **START_UEBERMITTLUNG_ENFG** festgelegt. Dieser Wert bleibt auch in der englischen Fassung deutsch, weil Camunda darüber korreliert.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `prozessId` | string | **ja** | — |
| `eventname` | const `START_UEBERMITTLUNG_ENFG` | **ja** | — |

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
