# [NB] START_AUFH_ZUK_ZUORDNUNG
<span hidden data-pagefind-meta={"title:Trigger-Ereignis START_AUFH_ZUK_ZUORDNUNG — Marktrolle NB (FV 202604)"} />

Marktrolle **NB** · Formatversion **202604** · BO4E-Schema **1.7.8**

## Stammdaten

Unter diesem Topic ist genau einer der folgenden 2 Prüfidentifikatoren zulässig — welcher, entscheidet der Event-Prozess.

| Prüfi | Scope | Anwendungsfall | Festlegung | Kommunikation |
|---|---|---|---|---|
| [PI_44038](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44038) | UTILMD_GAS | Informationsmeldung zur Aufhebung einer zuk. Zuordnung | GeLi Gas 2.0 | NB → LF (zukünfitge LF) |
| [PI_55038](/schnittstellen/202604/pruefi/UTILMD/PI_55038) | UTILMD | Aufhebung einer zuk. Zuordnung | GPKE Teil 2 | NB → LFZ |

Die Stammdaten der 2 Prüfidentifikatoren in **einer** Struktur — eine Spalte je Prüfidentifikator, wie im Anwendungshandbuch. Ein Wert in der Spalte heißt, dass das Feld zu diesem Prüfidentifikator gehört: **Muss**, wenn seine Spezifikation es verlangt, sonst **Kann**. Eine leere Zelle heißt »gehört nicht dazu«, nicht »unbekannt«. Vorausgewählt ist der erste; die übrigen schaltet die Leiste über der Tabelle zu.

<Handbuchsatz>

<div className="maco-tabellenrahmen">

| Struktur (BO4E) | Beschreibung | Format | <span className="hbs-p" title="Informationsmeldung zur Aufhebung einer zuk. Zuordnung">44038</span> | <span className="hbs-p" title="Aufhebung einer zuk. Zuordnung">55038</span> | Bedingung |
|---|---|---|---|---|---|
| <span className="hbs-g hbs-e0">**stammdaten**</span> | — | object | Kann | Kann | — |
| <span className="hbs-g hbs-e1">**BILANZIERUNG** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — | — |
| <span className="hbs-f hbs-e2">[bilanzierungsende](/bo4e/202604/bo/Bilanzierung#bilanzierungsende)</span><span className="hbs-nr">00010</span> | Exklusives Ende der Bilanzierung | string (date-time) | Kann | — | — |
| <span className="hbs-g hbs-e1">**MARKTLOKATION** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | Kann | — |
| <span className="hbs-f hbs-e2">[marktlokationsId](/bo4e/202604/bo/Marktlokation#marktlokationsid) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00020</span> | Identifikationsnummer einer Marktlokation, an der Energie entweder<br/>verbraucht, oder erzeugt wird | string | Muss | Kann | — |
| <span className="hbs-g hbs-e1">**NETZNUTZUNGSVERTRAG** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | Kann | — |
| <span className="hbs-f hbs-e2">[vertragsbeginn](/bo4e/202604/bo/Vertrag#vertragsbeginn)</span><span className="hbs-nr">00030</span> | Gibt an, wann der Vertrag beginnt. | string (date-time) | Kann | Kann | — |
| <span className="hbs-g hbs-e1">**TRANCHE** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | Kann | — |
| <span className="hbs-f hbs-e2">[tranchenId](/bo4e/202604/bo/Tranche#tranchenid)</span><span className="hbs-nr">00040</span> | tranchenId | string | — | Kann | — |

</div>

</Handbuchsatz>

## Kette dieses Auslösers

Das Ereignis löst die Nachricht aus.

| Nachricht | Antworten | Schreibaufruf nach der Antwort |
|---|---|---|
| [44038](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44038) | — | — |
| [55038](/schnittstellen/202604/pruefi/UTILMD/PI_55038) | — | — |

Dieses Ereignis löst Schritte in diesen Rollensichten aus:

| Prozess | Beteiligter | Regelwerk | Sparte |
|---|---|---|---|
| [Lieferbeginn](/prozessdoku/202604/NB/GPKE-Teil2-lieferbeginn) | NB | GPKE Teil 2 | Strom |
| [Lieferende von NB an LF](/prozessdoku/202604/NB/GPKE-Teil2-lieferende-von-nb-an-lf) | NB | GPKE Teil 2 | Strom |
| [Lieferbeginn](/prozessdoku/202604/NB/geli-gas-2-0-lieferbeginn) | NB | GeLi Gas 2.0 | Gas |

## Transaktionsdaten

Der Umschlag der Nachricht. Pflichtfelder müssen beim Trigger-Aufruf gesetzt sein.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| [sparte](/bo4e/202604/cdoc/Transaktionsdaten#sparte) | [Enum Sparte](/bo4e/202604/enum/Sparte) | **ja** | Enthält Informationen über die Sparte Werte: `STROM`, `GAS`, `FERNWAERME`, `NAHWAERME`, `WASSER`, `ABWASSER` |
| [transaktionsgrund](/bo4e/202604/cdoc/Transaktionsdaten#transaktionsgrund) | string | **ja** | Der Transaktionsgrund beschreibt den Geschäftsvorfall zur Kategorie genauer / UTILMD STS+7++###+ZW4+E03 |
| [transaktionsgrundergaenzung](/bo4e/202604/cdoc/Transaktionsdaten#transaktionsgrundergaenzung) | string | **ja** | Ergänzung zum Transaktionsgrund / UTILMD STS+7++E01+###+E03 |
| [vertragsbeginn](/bo4e/202604/cdoc/Transaktionsdaten#vertragsbeginn) | string (date-time) | **ja** | Datum Vertragsbeginn / DTM+92 |
| `pruefidentifikator` | — | nein | Wird dynamisch im Event-Prozess ermittelt (Entscheidungsgrundlage: sparte). Ein vom Sender mitgegebener Wert wird ignoriert. Im Topic mögliche Prüfis — 44038, 55038. Mögliche Werte: `44038`, `55038` |
| [absender › rollencodenummer](/bo4e/202604/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |
| [empfaenger › rollencodenummer](/bo4e/202604/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |

## Zusatzdaten

`eventname` ist auf **START_AUFH_ZUK_ZUORDNUNG** festgelegt. Dieser Wert bleibt auch in der englischen Fassung deutsch, weil Camunda darüber korreliert.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `prozessId` | string | **ja** | — |
| `eventname` | const `START_AUFH_ZUK_ZUORDNUNG` | **ja** | — |

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
