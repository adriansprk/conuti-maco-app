# [NB] START_REKLAMATION_DEFINITION
<span hidden data-pagefind-meta={"title:Trigger-Ereignis START_REKLAMATION_DEFINITION — Marktrolle NB (FV 202604)"} />

Marktrolle **NB** · Formatversion **202604** · BO4E-Schema **1.7.8**

## Stammdaten

Unter diesem Topic ist genau einer der folgenden 1 Prüfidentifikatoren zulässig — welcher, entscheidet der Event-Prozess.

| Prüfi | Scope | Anwendungsfall | Festlegung | Kommunikation |
|---|---|---|---|---|
| [PI_17122](/schnittstellen/202604/pruefi/ORDERS/PI_17122) | ORDERS | Reklamation einer Definition | GPKE Teil 3 | LF → NB |

Die Stammdaten der 1 Prüfidentifikatoren in **einer** Struktur — eine Spalte je Prüfidentifikator, wie im Anwendungshandbuch. Ein Wert in der Spalte heißt, dass das Feld zu diesem Prüfidentifikator gehört: **Muss**, wenn seine Spezifikation es verlangt, sonst **Kann**. Eine leere Zelle heißt »gehört nicht dazu«, nicht »unbekannt«. Vorausgewählt ist der erste; die übrigen schaltet die Leiste über der Tabelle zu.

<Handbuchsatz>

<div className="maco-tabellenrahmen">

| Struktur (BO4E) | Beschreibung | Format | <span className="hbs-p" title="Reklamation einer Definition">17122</span> | Bedingung |
|---|---|---|---|---|
| <span className="hbs-g hbs-e0">**stammdaten**</span> | — | object | Kann | — |
| <span className="hbs-g hbs-e1">**AUFTRAG** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | — |
| <span className="hbs-g hbs-e2">**positionsdaten** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | — |
| <span className="hbs-f hbs-e3">[definitionsTyp](/bo4e/202604/com/AuftragPosition#definitionstyp) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00010</span> | DefinitionsTyp | [Enum DefinitionsTyp](/bo4e/202604/enum/DefinitionsTyp) | Muss | — |
| <span className="hbs-w hbs-e4">`ZAEHLZEIT`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`SCHALTZEIT`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`LEISTUNGSKURVEN`</span> | — | — | Muss | — |
| <span className="hbs-f hbs-e3">[positionsnummer](/bo4e/202604/com/AuftragPosition#positionsnummer) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00020</span> | Positionsnummer | integer | Muss | — |
| <span className="hbs-g hbs-e1">**LEISTUNGSKURVENDEFINITION** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-g hbs-e2">**leistungskurven** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-f hbs-e3">[code](/bo4e/202604/com/Leistungskurve#code)</span><span className="hbs-nr">00030</span> | Code der Leistungskurve | string | Kann | — |
| <span className="hbs-g hbs-e1">**REKLAMATION** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | — |
| <span className="hbs-f hbs-e2">[reklamationsgrund](/bo4e/202604/bo/Reklamation#reklamationsgrund) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00040</span> | Hier wird für die Reklamation von Werten der Reklamationsgrund angegeben. | [Enum Reklamationsgrund](/bo4e/202604/enum/Reklamationsgrund) | Muss | — |
| <span className="hbs-w hbs-e3">`WERTE_ZU_HOCH`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`WERTE_ZU_NIEDRIG`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`WERTE_FEHLEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`KONFIGURATION_WIRKT_NICHT`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`KONFIGURATION_WIRKT_TEILWEISE`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`WERTE_WERDEN_NICHT_NACH_VORGABEN_UEBERMITTELT`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`UEBERSICHT_FEHLT`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`UEBERSICHT_UNPLAUSIBEL`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`AUSGEROLLTE_DEFINITION_FEHLT`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`AUSGEROLLTE_DEFINITION_UNPLAUSIBEL`</span> | — | — | Muss | — |
| <span className="hbs-g hbs-e2">**reklamationsgrundBemerkung**</span> | — | object | Kann | — |
| <span className="hbs-f hbs-e3">[bemerkung1](/bo4e/202604/com/ReklamationsgrundBemerkung#bemerkung1)</span><span className="hbs-nr">00050</span> | bemerkung1 | string | Kann | — |
| <span className="hbs-f hbs-e3">[bemerkung2](/bo4e/202604/com/ReklamationsgrundBemerkung#bemerkung2)</span><span className="hbs-nr">00060</span> | bemerkung2 | string | Kann | — |
| <span className="hbs-f hbs-e3">[bemerkung3](/bo4e/202604/com/ReklamationsgrundBemerkung#bemerkung3)</span><span className="hbs-nr">00070</span> | bemerkung3 | string | Kann | — |
| <span className="hbs-f hbs-e3">[bemerkung4](/bo4e/202604/com/ReklamationsgrundBemerkung#bemerkung4)</span><span className="hbs-nr">00080</span> | bemerkung4 | string | Kann | — |
| <span className="hbs-f hbs-e3">[bemerkung5](/bo4e/202604/com/ReklamationsgrundBemerkung#bemerkung5)</span><span className="hbs-nr">00090</span> | bemerkung5 | string | Kann | — |
| <span className="hbs-g hbs-e1">**SCHALTZEITDEFINITION** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-g hbs-e2">**schaltzeiten** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-f hbs-e3">[code](/bo4e/202604/com/Schaltzeit#code)</span><span className="hbs-nr">00100</span> | code | string | Kann | — |
| <span className="hbs-g hbs-e1">**ZAEHLZEITDEFINITION** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-g hbs-e2">**zaehlzeiten** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-f hbs-e3">[code](/bo4e/202604/com/Zaehlzeit#code)</span><span className="hbs-nr">00110</span> | Zählzeitdefinition | string | Kann | — |

</div>

</Handbuchsatz>

## Kette dieses Auslösers

Das Ereignis löst die Nachricht aus. Der Marktpartner antwortet mit einer der genannten Antworten, und danach schreibt die MACO APP den Vorgang in Ihr Backendsystem.

| Nachricht | Antworten | Schreibaufruf nach der Antwort |
|---|---|---|
| [17122](/schnittstellen/202604/pruefi/ORDERS/PI_17122) | [19123](/schnittstellen/202604/pruefi/ORDRSP/PI_19123) | `POST /updateProcessData` (abgeleitet) |

Dieses Ereignis löst Schritte in diesen Rollensichten aus:

| Prozess | Beteiligter | Regelwerk | Sparte |
|---|---|---|---|
| [Reklamation der Übersicht der Definitionen des LF vom NB an LF](/prozessdoku/202604/NB/GPKE-Teil3-reklamation-der-uebersicht-der-definitionen-des-lf-vom-nb-an-lf) | NB | GPKE Teil 3 | Strom |
| [Reklamation einer Definition des LF vom NB an LF](/prozessdoku/202604/NB/GPKE-Teil3-reklamation-einer-definition-des-lf-vom-nb-an-lf) | NB | GPKE Teil 3 | Strom |

## Transaktionsdaten

Der Umschlag der Nachricht. Pflichtfelder müssen beim Trigger-Aufruf gesetzt sein.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| [anfragereferenznummer](/bo4e/202604/cdoc/Transaktionsdaten#anfragereferenznummer) | string | **ja** | Referenz Vorgangsnummer 'aus Anfragenachricht' / ORDERS RFF+TN / IFTSTA RFF+AAV / INSRPT RFF+TN RFF+AAV |
| [kategorie](/bo4e/202604/cdoc/Transaktionsdaten#kategorie) | string | **ja** | Qualifier aus dem Beginn der EDIFact Nachricht / BGM |
| [sparte](/bo4e/202604/cdoc/Transaktionsdaten#sparte) | [Enum Sparte](/bo4e/202604/enum/Sparte) | **ja** | Enthält Informationen über die Sparte Werte: `STROM`, `GAS`, `FERNWAERME`, `NAHWAERME`, `WASSER`, `ABWASSER` |
| `pruefidentifikator` | — | nein | Wird dynamisch im Event-Prozess ermittelt. Ein vom Sender mitgegebener Wert wird ignoriert. Im Topic mögliche Prüfis — 17122. Mögliche Werte: `17122` |
| [absender › rollencodenummer](/bo4e/202604/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |
| [empfaenger › rollencodenummer](/bo4e/202604/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |

## Zusatzdaten

`eventname` ist auf **START_REKLAMATION_DEFINITION** festgelegt. Dieser Wert bleibt auch in der englischen Fassung deutsch, weil Camunda darüber korreliert.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `prozessId` | string | **ja** | — |
| `eventname` | const `START_REKLAMATION_DEFINITION` | **ja** | — |

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
