# [NB] START_UEBERM_DEFINITION
<span hidden data-pagefind-meta={"title:Trigger-Ereignis START_UEBERM_DEFINITION — Marktrolle NB (FV 202610)"} />

Marktrolle **NB** · Formatversion **202610** · BO4E-Schema **1.7.8**

## Stammdaten

Unter diesem Topic ist genau einer der folgenden 3 Prüfidentifikatoren zulässig — welcher, entscheidet der Event-Prozess.

| Prüfi | Scope | Anwendungsfall | Festlegung | Kommunikation |
|---|---|---|---|---|
| [PI_25005](/schnittstellen/202610/pruefi/UTILTS/PI_25005) | UTILTS | Übermittlung einer ausgerollten Zählzeitdefinition | GPKE Teil 3 | NB → LF |
| [PI_25008](/schnittstellen/202610/pruefi/UTILTS/PI_25008) | UTILTS | Übermittlung einer ausgerollten Schaltzeitdefinition | GPKE Teil 3 | NB → LF |
| [PI_25009](/schnittstellen/202610/pruefi/UTILTS/PI_25009) | UTILTS | Übermittlung einer ausgerollten Leistungskurvendefinition | GPKE Teil 3 | NB → LF |

Die Stammdaten der 3 Prüfidentifikatoren in **einer** Struktur — eine Spalte je Prüfidentifikator, wie im Anwendungshandbuch. Ein Wert in der Spalte heißt, dass das Feld zu diesem Prüfidentifikator gehört: **Muss**, wenn seine Spezifikation es verlangt, sonst **Kann**. Eine leere Zelle heißt »gehört nicht dazu«, nicht »unbekannt«. Vorausgewählt ist der erste; die übrigen schaltet die Leiste über der Tabelle zu.

<Handbuchsatz>

<div className="maco-tabellenrahmen">

| Struktur (BO4E) | Beschreibung | Format | <span className="hbs-p" title="Übermittlung einer ausgerollten Zählzeitdefinition">25005</span> | <span className="hbs-p" title="Übermittlung einer ausgerollten Schaltzeitdefinition">25008</span> | <span className="hbs-p" title="Übermittlung einer ausgerollten Leistungskurvendefinition">25009</span> | Bedingung |
|---|---|---|---|---|---|---|
| <span className="hbs-g hbs-e0">**stammdaten**</span> | — | object | Kann | Kann | Kann | — |
| <span className="hbs-g hbs-e1">**ZAEHLZEITDEFINITION** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | — | — | — |
| <span className="hbs-f hbs-e2">[beginndatum](/bo4e/202610/bo/Zaehlzeitdefinition#beginndatum) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00010</span> | Der inklusive Zeitpunkt ab dem die Zaehlzeitdefinitionen ausgerollt sind | string (date-time) | Muss | — | — | — |
| <span className="hbs-f hbs-e2">[code](/bo4e/202610/bo/Zaehlzeitdefinition#code) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00020</span> | Zählzeitdefinition | string | Muss | — | — | — |
| <span className="hbs-f hbs-e2">[endedatum](/bo4e/202610/bo/Zaehlzeitdefinition#endedatum)</span><span className="hbs-nr">00030</span> | Der exklusive Zeitpunkt bis zu dem die Zaehlzeitdefinitionen ausgerollt sind | string (date-time) | Kann | — | — | — |
| <span className="hbs-f hbs-e2">[version](/bo4e/202610/bo/Zaehlzeitdefinition#version) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00040</span> | Version der Zählzeitdefinition als Datum | string (date-time) | Muss | — | — | — |
| <span className="hbs-g hbs-e2">**zaehlzeiten** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | — | — | — |
| <span className="hbs-f hbs-e3">[aenderungszeitpunkt](/bo4e/202610/com/Zaehlzeit#aenderungszeitpunkt) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00050</span> | aenderungszeitpunkt | string (date-time) | Muss | — | — | — |
| <span className="hbs-f hbs-e3">[haeufigkeit](/bo4e/202610/com/Zaehlzeit#haeufigkeit)</span><span className="hbs-nr">00060</span> | Häufigkeit der Übermittlung | [Enum HaeufigkeitZaehlzeit](/bo4e/202610/enum/HaeufigkeitZaehlzeit) | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`EINMALIG`</span> | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`JAEHRLICH`</span> | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[register](/bo4e/202610/com/Zaehlzeit#register) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00070</span> | register | string | Muss | — | — | — |
| <span className="hbs-g hbs-e1">**SCHALTZEITDEFINITION** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | — | Muss | — | — |
| <span className="hbs-f hbs-e2">[beginndatum](/bo4e/202610/bo/Schaltzeitdefinition#beginndatum) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00080</span> | beginndatum | string (date-time) | — | Muss | — | — |
| <span className="hbs-f hbs-e2">[code](/bo4e/202610/bo/Schaltzeitdefinition#code) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00090</span> | code | string | — | Muss | — | — |
| <span className="hbs-f hbs-e2">[endedatum](/bo4e/202610/bo/Schaltzeitdefinition#endedatum)</span><span className="hbs-nr">00100</span> | endedatum | string (date-time) | — | Kann | — | — |
| <span className="hbs-f hbs-e2">[version](/bo4e/202610/bo/Schaltzeitdefinition#version) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00110</span> | version | string (date-time) | — | Muss | — | — |
| <span className="hbs-g hbs-e2">**schaltzeiten** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | — | Muss | — | — |
| <span className="hbs-f hbs-e3">[aenderungszeitpunkt](/bo4e/202610/com/Schaltzeit#aenderungszeitpunkt) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00120</span> | aenderungszeitpunkt | string (date-time) | — | Muss | — | — |
| <span className="hbs-f hbs-e3">[haeufigkeit](/bo4e/202610/com/Schaltzeit#haeufigkeit)</span><span className="hbs-nr">00130</span> | HaeufigkeitSchaltzeit | [Enum HaeufigkeitSchaltzeit](/bo4e/202610/enum/HaeufigkeitSchaltzeit) | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`EINMALIG`</span> | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`JAEHRLICH`</span> | — | — | — | Kann | — | — |
| <span className="hbs-f hbs-e3">[schalthandlung](/bo4e/202610/com/Schaltzeit#schalthandlung) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00140</span> | Schalthandlung | [Enum Schalthandlung](/bo4e/202610/enum/Schalthandlung) | — | Muss | — | — |
| <span className="hbs-w hbs-e4">`LEISTUNG_AN`</span> | — | — | — | Muss | — | — |
| <span className="hbs-w hbs-e4">`LEISTUNG_AUS`</span> | — | — | — | Muss | — | — |
| <span className="hbs-g hbs-e1">**LEISTUNGSKURVENDEFINITION** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | — | — | Muss | — |
| <span className="hbs-f hbs-e2">[beginndatum](/bo4e/202610/bo/Leistungskurvendefinition#beginndatum) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00150</span> | beginndatum | string (date-time) | — | — | Muss | — |
| <span className="hbs-f hbs-e2">[code](/bo4e/202610/bo/Leistungskurvendefinition#code) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00160</span> | code | string | — | — | Muss | — |
| <span className="hbs-f hbs-e2">[endedatum](/bo4e/202610/bo/Leistungskurvendefinition#endedatum)</span><span className="hbs-nr">00170</span> | endedatum | string (date-time) | — | — | Kann | — |
| <span className="hbs-f hbs-e2">[version](/bo4e/202610/bo/Leistungskurvendefinition#version) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00180</span> | version | string (date-time) | — | — | Muss | — |
| <span className="hbs-g hbs-e2">**leistungskurven** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | — | — | Muss | — |
| <span className="hbs-f hbs-e3">[aenderungszeitpunkt](/bo4e/202610/com/Leistungskurve#aenderungszeitpunkt) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00190</span> | Änderungszeitpunkt | string (date-time) | — | — | Muss | — |
| <span className="hbs-f hbs-e3">[haeufigkeit](/bo4e/202610/com/Leistungskurve#haeufigkeit)</span><span className="hbs-nr">00200</span> | HaeufigkeitLeistungskurve | [Enum HaeufigkeitLeistungskurve](/bo4e/202610/enum/HaeufigkeitLeistungskurve) | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`EINMALIG`</span> | — | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`JAEHRLICH`</span> | — | — | — | — | Kann | — |
| <span className="hbs-g hbs-e3">**schwellwert** <span className="hbs-pflicht">\*</span></span> | — | object | — | — | Muss | — |
| <span className="hbs-f hbs-e4">[obererSchwellwert](/bo4e/202610/com/Schwellwert#obererschwellwert) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00210</span> | obererSchwellwert | number (float) | — | — | Muss | — |

</div>

</Handbuchsatz>

## Kette dieses Auslösers

Das Ereignis löst die Nachricht aus.

| Nachricht | Antworten | Schreibaufruf nach der Antwort |
|---|---|---|
| [25005](/schnittstellen/202610/pruefi/UTILTS/PI_25005) | — | — |
| [25008](/schnittstellen/202610/pruefi/UTILTS/PI_25008) | — | — |
| [25009](/schnittstellen/202610/pruefi/UTILTS/PI_25009) | — | — |

Dieses Ereignis löst einen Schritt in dieser Rollensicht aus:

| Prozess | Beteiligter | Regelwerk | Sparte |
|---|---|---|---|
| [Übermittlung einer Definition des NB durch den NB](/prozessdoku/202610/NB/GPKE-Teil3-uebermittlung-einer-definition-des-nb-durch-den-nb) | NB | GPKE Teil 3 | Strom |

## Transaktionsdaten

Der Umschlag der Nachricht. Pflichtfelder müssen beim Trigger-Aufruf gesetzt sein.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `pruefidentifikator` | — | nein | Wird dynamisch im Event-Prozess ermittelt (Entscheidungsgrundlage: kategorie). Ein vom Sender mitgegebener Wert wird ignoriert. Im Topic mögliche Prüfis — 25005, 25008, 25009. Mögliche Werte: `25005`, `25008`, `25009` |

## Zusatzdaten

`eventname` ist auf **START_UEBERM_DEFINITION** festgelegt. Dieser Wert bleibt auch in der englischen Fassung deutsch, weil Camunda darüber korreliert.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `prozessId` | string | **ja** | — |
| `eventname` | const `START_UEBERM_DEFINITION` | **ja** | — |

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
