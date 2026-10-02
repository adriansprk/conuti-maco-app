# [NB] START_PREISBLATT
<span hidden data-pagefind-meta={"title:Trigger-Ereignis START_PREISBLATT — Marktrolle NB (FV 202604)"} />

Marktrolle **NB** · Formatversion **202604** · BO4E-Schema **1.7.8**

## Stammdaten

Unter diesem Topic ist genau einer der folgenden 1 Prüfidentifikatoren zulässig — welcher, entscheidet der Event-Prozess.

| Prüfi | Scope | Anwendungsfall | Festlegung | Kommunikation |
|---|---|---|---|---|
| [PI_27003](/schnittstellen/202604/pruefi/PRICAT/PI_27003) | PRICAT | Preisblätter NB-Leistungen | AWH Sperrprozesse Gas | NB → LF |

Die Stammdaten der 1 Prüfidentifikatoren in **einer** Struktur — eine Spalte je Prüfidentifikator, wie im Anwendungshandbuch. Ein Wert in der Spalte heißt, dass das Feld zu diesem Prüfidentifikator gehört: **Muss**, wenn seine Spezifikation es verlangt, sonst **Kann**. Eine leere Zelle heißt »gehört nicht dazu«, nicht »unbekannt«. Vorausgewählt ist der erste; die übrigen schaltet die Leiste über der Tabelle zu.

<Handbuchsatz>

<div className="maco-tabellenrahmen">

| Struktur (BO4E) | Beschreibung | Format | <span className="hbs-p" title="Preisblätter NB-Leistungen">27003</span> | Bedingung |
|---|---|---|---|---|
| <span className="hbs-g hbs-e0">**stammdaten**</span> | — | object | Kann | — |
| <span className="hbs-g hbs-e1">**PREISBLATT** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | — |
| <span className="hbs-f hbs-e2">[preisNetzbetreiberCodenummer](/bo4e/202604/bo/Preisblatt#preisnetzbetreibercodenummer)</span><span className="hbs-nr">00010</span> | Preise des Netzbetreibers | string | Kann | — |
| <span className="hbs-g hbs-e2">**gueltigkeit** <span className="hbs-pflicht">\*</span></span> | — | object | Muss | — |
| <span className="hbs-f hbs-e3">[startdatum](/bo4e/202604/com/Zeitraum#startdatum) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00020</span> | startdatum | string (date-time) | Muss | — |
| <span className="hbs-g hbs-e2">**preispositionen** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-f hbs-e3">[artikelId](/bo4e/202604/com/Preisposition#artikelid)</span><span className="hbs-nr">00030</span> | Die genauen Bedeutungen der einzelnen Artikel-IDs sind in der EDI@Energy Codeliste der Artikelnummern<br/>und Artikel-IDs zu finden, die in der Spalte "PRICAT Codeverwendung" ein X haben | string | Kann | — |
| <span className="hbs-f hbs-e3">[positionsnummer](/bo4e/202604/com/Preisposition#positionsnummer)</span><span className="hbs-nr">00040</span> | Fortlaufende Nummer für die Preisposition | integer | Kann | — |
| <span className="hbs-f hbs-e3">[zeitbasis](/bo4e/202604/com/Preisposition#zeitbasis)</span><span className="hbs-nr">00050</span> | Die Zeit(dauer) auf die sich der Preis bezieht. Z.B. ein Jahr für einen Leistungspreis der in €/kW/Jahr<br/>ausgegeben wird. | [Enum Zeiteinheit](/bo4e/202604/enum/Zeiteinheit) | Kann | — |
| <span className="hbs-w hbs-e4">`SEKUNDE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MINUTE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`STUNDE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`VIERTEL_STUNDE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`TAG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`WOCHE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MONAT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`QUARTAL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`HALBJAHR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`JAHR`</span> | — | — | Kann | — |
| <span className="hbs-g hbs-e3">**preisstaffeln** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-f hbs-e4">[einheitspreis](/bo4e/202604/com/Preisstaffel#einheitspreis)</span><span className="hbs-nr">00060</span> | einheitspreis | number (float) | Kann | — |
| <span className="hbs-f hbs-e4">[staffelgrenzeBis](/bo4e/202604/com/Preisstaffel#staffelgrenzebis)</span><span className="hbs-nr">00070</span> | staffelgrenzeBis | number (float) | Kann | — |
| <span className="hbs-f hbs-e4">[staffelgrenzeVon](/bo4e/202604/com/Preisstaffel#staffelgrenzevon)</span><span className="hbs-nr">00080</span> | staffelgrenzeVon | number (float) | Kann | — |

</div>

</Handbuchsatz>

## Kette dieses Auslösers

Das Ereignis löst die Nachricht aus.

| Nachricht | Antworten | Schreibaufruf nach der Antwort |
|---|---|---|
| [27003](/schnittstellen/202604/pruefi/PRICAT/PI_27003) | — | — |

Dieses Ereignis löst Schritte in diesen Rollensichten aus:

| Prozess | Beteiligter | Regelwerk | Sparte |
|---|---|---|---|
| [Übermittlung Preisblatt NB an LF](/prozessdoku/202604/NB/awh-sperrprozesse-gas-ubermittlung-preisblatt-nb-an-lf) | NB | AWH Sperrprozesse Gas | Gas |
| [Übermittlung Preisblatt NB an LF](/prozessdoku/202604/NB/GPKE-Teil2-uebermittlung-preisblatt-nb-an-lf) | NB | GPKE Teil 2 | Strom |

## Transaktionsdaten

Der Umschlag der Nachricht. Pflichtfelder müssen beim Trigger-Aufruf gesetzt sein.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| [kategorie](/bo4e/202604/cdoc/Transaktionsdaten#kategorie) | string | **ja** | Qualifier aus dem Beginn der EDIFact Nachricht / BGM |
| [sparte](/bo4e/202604/cdoc/Transaktionsdaten#sparte) | [Enum Sparte](/bo4e/202604/enum/Sparte) | **ja** | Enthält Informationen über die Sparte Werte: `STROM`, `GAS`, `FERNWAERME`, `NAHWAERME`, `WASSER`, `ABWASSER` |
| `pruefidentifikator` | — | nein | Wird dynamisch im Event-Prozess ermittelt. Ein vom Sender mitgegebener Wert wird ignoriert. Im Topic mögliche Prüfis — 27003. Mögliche Werte: `27003` |
| [absender › rollencodenummer](/bo4e/202604/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |
| [empfaenger › rollencodenummer](/bo4e/202604/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |

## Zusatzdaten

`eventname` ist auf **START_PREISBLATT** festgelegt. Dieser Wert bleibt auch in der englischen Fassung deutsch, weil Camunda darüber korreliert.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `prozessId` | string | **ja** | — |
| `eventname` | const `START_PREISBLATT` | **ja** | — |

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
