# [LF] START_UEBERSICHT_LEISTUNGSKURVENDEF
<span hidden data-pagefind-meta={"title:Trigger-Ereignis START_UEBERSICHT_LEISTUNGSKURVENDEF — Marktrolle LF (FV 202604)"} />

Marktrolle **LF** · Formatversion **202604** · BO4E-Schema **1.7.8**

## Stammdaten

Unter diesem Topic ist genau einer der folgenden 1 Prüfidentifikatoren zulässig — welcher, entscheidet der Event-Prozess.

| Prüfi | Scope | Anwendungsfall | Festlegung | Kommunikation |
|---|---|---|---|---|
| [PI_25007](/schnittstellen/202604/pruefi/UTILTS/PI_25007) | UTILTS | Übermittlung Übersicht Leistungskurvendefinitionen | GPKE Teil 3 | NB → LF |

Die Stammdaten der 1 Prüfidentifikatoren in **einer** Struktur — eine Spalte je Prüfidentifikator, wie im Anwendungshandbuch. Ein Wert in der Spalte heißt, dass das Feld zu diesem Prüfidentifikator gehört: **Muss**, wenn seine Spezifikation es verlangt, sonst **Kann**. Eine leere Zelle heißt »gehört nicht dazu«, nicht »unbekannt«. Vorausgewählt ist der erste; die übrigen schaltet die Leiste über der Tabelle zu.

<Handbuchsatz>

<div className="maco-tabellenrahmen">

| Struktur (BO4E) | Beschreibung | Format | <span className="hbs-p" title="Übermittlung Übersicht Leistungskurvendefinitionen">25007</span> | Bedingung |
|---|---|---|---|---|
| <span className="hbs-g hbs-e0">**stammdaten**</span> | — | object | Kann | — |
| <span className="hbs-g hbs-e1">**LEISTUNGSKURVENDEFINITION** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | — |
| <span className="hbs-f hbs-e2">[beginndatum](/bo4e/202604/bo/Leistungskurvendefinition#beginndatum) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00010</span> | beginndatum | string (date-time) | Muss | — |
| <span className="hbs-f hbs-e2">[notwendigkeit](/bo4e/202604/bo/Leistungskurvendefinition#notwendigkeit) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00020</span> | DefinitionenNotwendigkeit | [Enum DefinitionenNotwendigkeit](/bo4e/202604/enum/DefinitionenNotwendigkeit) | Muss | — |
| <span className="hbs-w hbs-e3">`ZAEHLZEITDEFINITIONEN_WERDEN_VERWENDET`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`ZAEHLZEITDEFINITIONEN_WERDEN_NICHT_VERWENDET`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`DEFINITIONEN_WERDEN_VERWENDET`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`DEFINITIONEN_WERDEN_NICHT_VERWENDET`</span> | — | — | Muss | — |
| <span className="hbs-f hbs-e2">[version](/bo4e/202604/bo/Leistungskurvendefinition#version) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00030</span> | version | string (date-time) | Muss | — |
| <span className="hbs-g hbs-e2">**leistungskurven** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-f hbs-e3">[code](/bo4e/202604/com/Leistungskurve#code)</span><span className="hbs-nr">00040</span> | Code der Leistungskurve | string | Kann | — |
| <span className="hbs-f hbs-e3">[haeufigkeit](/bo4e/202604/com/Leistungskurve#haeufigkeit)</span><span className="hbs-nr">00050</span> | HaeufigkeitLeistungskurve | [Enum HaeufigkeitLeistungskurve](/bo4e/202604/enum/HaeufigkeitLeistungskurve) | Kann | — |
| <span className="hbs-w hbs-e4">`EINMALIG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`JAEHRLICH`</span> | — | — | Kann | — |
| <span className="hbs-f hbs-e3">[uebermittelbarkeit](/bo4e/202604/com/Leistungskurve#uebermittelbarkeit)</span><span className="hbs-nr">00060</span> | UebermittelbarkeitLeistungskurve | [Enum UebermittelbarkeitLeistungskurve](/bo4e/202604/enum/UebermittelbarkeitLeistungskurve) | Kann | — |
| <span className="hbs-w hbs-e4">`ELEKTRONISCH`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`NICHT_ELEKTRONISCH`</span> | — | — | Kann | — |

</div>

</Handbuchsatz>

## Kette dieses Auslösers

Das Ereignis löst die Nachricht aus.

| Nachricht | Antworten | Schreibaufruf nach der Antwort |
|---|---|---|
| [25007](/schnittstellen/202604/pruefi/UTILTS/PI_25007) | — | — |

Dieses Ereignis löst einen Schritt in dieser Rollensicht aus:

| Prozess | Beteiligter | Regelwerk | Sparte |
|---|---|---|---|
| [Übermittlung der Übersicht der Definitionen des LF durch den LF](/prozessdoku/202604/LF/GPKE-Teil3-uebermittlung-der-uebersicht-der-definitionen-des-lf-durch-den-lf) | LF | GPKE Teil 3 | Strom |

## Transaktionsdaten

Der Umschlag der Nachricht. Pflichtfelder müssen beim Trigger-Aufruf gesetzt sein.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| [anfrageReferenz](/bo4e/202604/cdoc/Transaktionsdaten#anfragereferenz) | string | **ja** | Beantragungsnummer / RFF+AGI |
| [kategorie](/bo4e/202604/cdoc/Transaktionsdaten#kategorie) | string | **ja** | Qualifier aus dem Beginn der EDIFact Nachricht / BGM |
| [sparte](/bo4e/202604/cdoc/Transaktionsdaten#sparte) | [Enum Sparte](/bo4e/202604/enum/Sparte) | **ja** | Enthält Informationen über die Sparte Werte: `STROM`, `GAS`, `FERNWAERME`, `NAHWAERME`, `WASSER`, `ABWASSER` |
| `pruefidentifikator` | — | nein | Wird dynamisch im Event-Prozess ermittelt. Ein vom Sender mitgegebener Wert wird ignoriert. Im Topic mögliche Prüfis — 25007. Mögliche Werte: `25007` |
| [absender › rollencodenummer](/bo4e/202604/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |
| [empfaenger › rollencodenummer](/bo4e/202604/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |

## Zusatzdaten

`eventname` ist auf **START_UEBERSICHT_LEISTUNGSKURVENDEF** festgelegt. Dieser Wert bleibt auch in der englischen Fassung deutsch, weil Camunda darüber korreliert.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `prozessId` | string | **ja** | — |
| `eventname` | const `START_UEBERSICHT_LEISTUNGSKURVENDEF` | **ja** | — |

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
