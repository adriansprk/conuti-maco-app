# [NB] START_VERSAND_COMDIS
<span hidden data-pagefind-meta={"title:Trigger-Ereignis START_VERSAND_COMDIS — Marktrolle NB (FV 202610)"} />

Marktrolle **NB** · Formatversion **202610** · BO4E-Schema **1.7.8**

## Stammdaten

Unter diesem Topic ist genau einer der folgenden 1 Prüfidentifikatoren zulässig — welcher, entscheidet der Event-Prozess.

| Prüfi | Scope | Anwendungsfall | Festlegung | Kommunikation |
|---|---|---|---|---|
| [PI_29002](/schnittstellen/202610/pruefi/COMDIS/PI_29002) | COMDIS | Ablehnung IFTSTA | GPKE Teil 2 | NB → LF |

Die Stammdaten der 1 Prüfidentifikatoren in **einer** Struktur — eine Spalte je Prüfidentifikator, wie im Anwendungshandbuch. Ein Wert in der Spalte heißt, dass das Feld zu diesem Prüfidentifikator gehört: **Muss**, wenn seine Spezifikation es verlangt, sonst **Kann**. Eine leere Zelle heißt »gehört nicht dazu«, nicht »unbekannt«. Vorausgewählt ist der erste; die übrigen schaltet die Leiste über der Tabelle zu.

<Handbuchsatz>

<div className="maco-tabellenrahmen">

| Struktur (BO4E) | Beschreibung | Format | <span className="hbs-p" title="Ablehnung IFTSTA">29002</span> | Bedingung |
|---|---|---|---|---|
| <span className="hbs-g hbs-e0">**stammdaten**</span> | — | object | Kann | — |
| <span className="hbs-g hbs-e1">**HANDELSUNSTIMMIGKEIT** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | — |
| <span className="hbs-f hbs-e2">[nummer](/bo4e/202610/bo/Handelsunstimmigkeit#nummer) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00010</span> | Handelsunstimmigkeitsnummer | string | Muss | — |
| <span className="hbs-f hbs-e2">[typ](/bo4e/202610/bo/Handelsunstimmigkeit#typ) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00020</span> | Gibt den Typ der Handelsunstimmigkeit an. | [Enum Handelsunstimmigkeitstyp](/bo4e/202610/enum/Handelsunstimmigkeitstyp) | Muss | — |
| <span className="hbs-w hbs-e3">`HANDELSRECHNUNG`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`LIEFERSCHEIN_HANDELSUNSTIMMIGKEITSTYP`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`LIEFERSCHEIN_GRUND_ARBEITSPREIS`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`LIEFERSCHEIN_ARBEITS_LEISTUNGSPREIS`</span> | — | — | Muss | — |
| <span className="hbs-g hbs-e2">**begruendung** <span className="hbs-pflicht">\*</span></span> | — | object | Muss | — |
| <span className="hbs-f hbs-e3">[grund](/bo4e/202610/com/Handelsunstimmigkeitsbegruendung#grund) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00030</span> | Angabe des Handelsunstimmigkeitsgrunds | [Enum Handelsunstimmigkeitsgrund](/bo4e/202610/enum/Handelsunstimmigkeitsgrund) | Muss | — |
| <span className="hbs-w hbs-e4">`ANMELDUNG_BESTAETIGT`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`ABRECHNUNGSBEGINN_GLEICH_BESTAETIGTEM_VERTRAGSBEGINN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`ABRECHNUNGSENDE_GLEICH_BESTAETIGTEM_VERTRAGSENDE`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`NN_MSCONS_UEBERSENDET`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`RICHTIGE_MESSWERTE_ENERGIEMENGEN_UEBERSENDET`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`SONSTIGES_SIEHE_BEGRUENDUNG`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`GUELTIGES_PREISBLATT_VERSENDET`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`GUELTIGER_SPERRAUFTRAG_VORHANDEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`KORREKTE_ARTIKEL_ID_IN_RECHNUNG`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`KORREKTER_PREIS_ZU_GUELTIGEM_PREISBLATT_IN_RECHNUNG`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`RECHNUNG_KORREKT_A05`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`RECHNUNG_KORREKT_A10`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`RECHNUNG_KORREKT_A11`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`GUELTIGES_PREISBLATT_FRISTGERECHT_VERSENDET`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`GUELTIGE_RECHNUNG_VORHANDEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`ARTIKEL_ID_FUER_VERZUGSKOSTEN_VERWENDET`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`KORREKTER_PREIS_IN_RECHNUNG_ABGERECHNET`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`GUELTIGES_PREISBLATT_BLINDARBEIT_VERSENDET`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`KORREKTE_ARTIKEL_ID_IST_ANGEGEBEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`RECHNUNG_BREGRUENDET_KORREKT`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`KORREKTE_ARTIKEL_ID_FUER_ABRECHNUNG_STORNIERTER_SPERRAUFTRAG_ANGEGEBEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`ABRECHNUNG_BLINDARBEIT_SPARTE_GAS_NICHT_RELEVANT`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`SONSTIGES`</span> | — | — | Muss | — |
| <span className="hbs-f hbs-e3">[hinweis](/bo4e/202610/com/Handelsunstimmigkeitsbegruendung#hinweis) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00040</span> | Hinweis zum Grund | string | Muss | — |

</div>

</Handbuchsatz>

## Kette dieses Auslösers

Das Ereignis löst die Nachricht aus.

| Nachricht | Antworten | Schreibaufruf nach der Antwort |
|---|---|---|
| [29002](/schnittstellen/202610/pruefi/COMDIS/PI_29002) | — | — |

Dieses Ereignis löst einen Schritt in dieser Rollensicht aus:

| Prozess | Beteiligter | Regelwerk | Sparte |
|---|---|---|---|
| [Übermittlung des Lieferscheins zur Netznutzungsabrechnung](/prozessdoku/202610/NB/GPKE-Teil2-uebermittlung-des-lieferscheins-zur-netznutzungsabrechnung) | NB | GPKE Teil 2 | Strom |

## Transaktionsdaten

Der Umschlag der Nachricht. Pflichtfelder müssen beim Trigger-Aufruf gesetzt sein.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| [kategorie](/bo4e/202610/cdoc/Transaktionsdaten#kategorie) | string | **ja** | Qualifier aus dem Beginn der EDIFact Nachricht / BGM |
| [sparte](/bo4e/202610/cdoc/Transaktionsdaten#sparte) | [Enum Sparte](/bo4e/202610/enum/Sparte) | **ja** | Enthält Informationen über die Sparte Werte: `STROM`, `GAS`, `FERNWAERME`, `NAHWAERME`, `WASSER`, `ABWASSER` |
| `pruefidentifikator` | — | nein | Wird dynamisch im Event-Prozess ermittelt. Ein vom Sender mitgegebener Wert wird ignoriert. Im Topic mögliche Prüfis — 29002. Mögliche Werte: `29002` |
| [absender › rollencodenummer](/bo4e/202610/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |
| [empfaenger › rollencodenummer](/bo4e/202610/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |

## Zusatzdaten

`eventname` ist auf **START_VERSAND_COMDIS** festgelegt. Dieser Wert bleibt auch in der englischen Fassung deutsch, weil Camunda darüber korreliert.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `prozessId` | string | **ja** | — |
| `eventname` | const `START_VERSAND_COMDIS` | **ja** | — |

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
