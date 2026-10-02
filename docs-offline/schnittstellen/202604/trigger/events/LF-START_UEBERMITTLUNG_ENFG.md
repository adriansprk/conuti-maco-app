# [LF] START_UEBERMITTLUNG_ENFG
<span hidden data-pagefind-meta={"title:Trigger-Ereignis START_UEBERMITTLUNG_ENFG — Marktrolle LF (FV 202604)"} />

Marktrolle **LF** · Formatversion **202604** · BO4E-Schema **1.7.8**

## Stammdaten

Unter diesem Topic ist genau einer der folgenden 1 Prüfidentifikatoren zulässig — welcher, entscheidet der Event-Prozess.

| Prüfi | Scope | Anwendungsfall | Festlegung | Kommunikation |
|---|---|---|---|---|
| [PI_21045](/schnittstellen/202604/pruefi/IFTSTA/PI_21045) | IFTSTA | EnFG Informationen | GPKE Teil 4 | LF → NB |

Die Stammdaten der 1 Prüfidentifikatoren in **einer** Struktur — eine Spalte je Prüfidentifikator, wie im Anwendungshandbuch. Ein Wert in der Spalte heißt, dass das Feld zu diesem Prüfidentifikator gehört: **Muss**, wenn seine Spezifikation es verlangt, sonst **Kann**. Eine leere Zelle heißt »gehört nicht dazu«, nicht »unbekannt«. Vorausgewählt ist der erste; die übrigen schaltet die Leiste über der Tabelle zu.

<Handbuchsatz>

<div className="maco-tabellenrahmen">

| Struktur (BO4E) | Beschreibung | Format | <span className="hbs-p" title="EnFG Informationen">21045</span> | Bedingung |
|---|---|---|---|---|
| <span className="hbs-g hbs-e0">**stammdaten**</span> | — | object | Kann | — |
| <span className="hbs-g hbs-e1">**ENERGIELIEFERVERTRAG** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-g hbs-e2">**vertragspartner2** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-f hbs-e3">[anrede](/bo4e/202604/bo/Geschaeftspartner#anrede)</span><span className="hbs-nr">00010</span> | Die Anrede für den GePa, Z.B. Herr. | string | Kann | — |
| <span className="hbs-f hbs-e3">[geschaeftspartnerrolle](/bo4e/202604/bo/Geschaeftspartner#geschaeftspartnerrolle)</span><span className="hbs-nr">00020</span> | Rolle, die der Geschäftspartner hat (z.B. Interessent, Kunde). | array | Kann | — |
| <span className="hbs-f hbs-e3">[gewerbekennzeichnung](/bo4e/202604/bo/Geschaeftspartner#gewerbekennzeichnung)</span><span className="hbs-nr">00030</span> | Kennzeichnung ob es sich um einen Gewerbe/Unternehmen (gewerbeKennzeichnung = true)<br/>oder eine Privatperson handelt. (gewerbeKennzeichnung = false) | boolean | Kann | — |
| <span className="hbs-f hbs-e3">[name1](/bo4e/202604/bo/Geschaeftspartner#name1)</span><span className="hbs-nr">00040</span> | Erster Teil des Namens. Hier kann der Firmenname oder bei Privatpersonen<br/>beispielsweise der Nachname dargestellt werden. Beispiele: Yellow Strom GmbH<br/>oder Hagen | string | Kann | — |
| <span className="hbs-f hbs-e3">[name2](/bo4e/202604/bo/Geschaeftspartner#name2)</span><span className="hbs-nr">00050</span> | Zweiter Teil des Namens. Hier kann der eine Erweiterung zum Firmennamen oder<br/>bei Privatpersonen beispielsweise der Vorname dargestellt werden. Beispiele:<br/>Bereich Süd oder Nina | string | Kann | — |
| <span className="hbs-f hbs-e3">[name3](/bo4e/202604/bo/Geschaeftspartner#name3)</span><span className="hbs-nr">00060</span> | Dritter Teil des Namens. Hier können weitere Ergänzungen zum Firmennamen oder<br/>bei Privatpersonen Zusätze zum Namen dargestellt werden. Beispiele: und Afrika<br/>oder Sängerin | string | Kann | — |
| <span className="hbs-f hbs-e3">[name4](/bo4e/202604/bo/Geschaeftspartner#name4)</span><span className="hbs-nr">00070</span> | name4 | string | Kann | — |
| <span className="hbs-g hbs-e1">**MARKTLOKATION** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | — |
| <span className="hbs-f hbs-e2">[marktlokationsId](/bo4e/202604/bo/Marktlokation#marktlokationsid) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00080</span> | Identifikationsnummer einer Marktlokation, an der Energie entweder<br/>verbraucht, oder erzeugt wird | string | Muss | — |
| <span className="hbs-g hbs-e1">**STATUSMITTEILUNG** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | — |
| <span className="hbs-g hbs-e2">**positionsdaten** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | — |
| <span className="hbs-f hbs-e3">[auftragsStatusListe](/bo4e/202604/com/StatusmitteilungPosition#auftragsstatusliste) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00090</span> | auftragsStatusListe | array | Muss | — |
| <span className="hbs-f hbs-e3">[positionsnummer](/bo4e/202604/com/StatusmitteilungPosition#positionsnummer) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00100</span> | positionsnummer | integer | Muss | — |
| <span className="hbs-g hbs-e3">**allgemeineInformationen**</span> | — | object | Kann | — |
| <span className="hbs-f hbs-e4">[info1](/bo4e/202604/com/AllgemeineInformationen#info1)</span><span className="hbs-nr">00110</span> | Allgemeine Info 1 | string | Kann | — |
| <span className="hbs-f hbs-e4">[info2](/bo4e/202604/com/AllgemeineInformationen#info2)</span><span className="hbs-nr">00120</span> | Allgemeine Info 2 | string | Kann | — |
| <span className="hbs-f hbs-e4">[info3](/bo4e/202604/com/AllgemeineInformationen#info3)</span><span className="hbs-nr">00130</span> | Allgemeine Info 3 | string | Kann | — |
| <span className="hbs-f hbs-e4">[info4](/bo4e/202604/com/AllgemeineInformationen#info4)</span><span className="hbs-nr">00140</span> | Allgemeine Info 4 | string | Kann | — |
| <span className="hbs-f hbs-e4">[info5](/bo4e/202604/com/AllgemeineInformationen#info5)</span><span className="hbs-nr">00150</span> | Allgemeine Info 5 | string | Kann | — |

</div>

</Handbuchsatz>

## Kette dieses Auslösers

Das Ereignis löst die Nachricht aus.

| Nachricht | Antworten | Schreibaufruf nach der Antwort |
|---|---|---|
| [21045](/schnittstellen/202604/pruefi/IFTSTA/PI_21045) | — | — |

Dieses Ereignis löst einen Schritt in dieser Rollensicht aus:

| Prozess | Beteiligter | Regelwerk | Sparte |
|---|---|---|---|
| [Übermittlung von Informationen](/prozessdoku/202604/LF/GPKE-Teil4-uebermittlung-von-informationen) | LF | GPKE Teil 4 | Strom |

## Transaktionsdaten

Der Umschlag der Nachricht. Pflichtfelder müssen beim Trigger-Aufruf gesetzt sein.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| [kategorie](/bo4e/202604/cdoc/Transaktionsdaten#kategorie) | string | **ja** | Qualifier aus dem Beginn der EDIFact Nachricht / BGM |
| [sparte](/bo4e/202604/cdoc/Transaktionsdaten#sparte) | [Enum Sparte](/bo4e/202604/enum/Sparte) | **ja** | Enthält Informationen über die Sparte Werte: `STROM`, `GAS`, `FERNWAERME`, `NAHWAERME`, `WASSER`, `ABWASSER` |
| [verwendungAb](/bo4e/202604/cdoc/Transaktionsdaten#verwendungab) | string (date-time) | **ja** | Verarbeitung, Beginndatum/-zeit / DTM+163 |
| `pruefidentifikator` | — | nein | Wird dynamisch im Event-Prozess ermittelt. Ein vom Sender mitgegebener Wert wird ignoriert. Im Topic mögliche Prüfis — 21045. Mögliche Werte: `21045` |
| [absender › rollencodenummer](/bo4e/202604/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |
| [empfaenger › rollencodenummer](/bo4e/202604/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |

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
