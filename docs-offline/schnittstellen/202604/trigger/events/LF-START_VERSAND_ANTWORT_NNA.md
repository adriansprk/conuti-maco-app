# [LF] START_VERSAND_ANTWORT_NNA
<span hidden data-pagefind-meta={"title:Trigger-Ereignis START_VERSAND_ANTWORT_NNA — Marktrolle LF (FV 202604)"} />

Marktrolle **LF** · Formatversion **202604** · BO4E-Schema **1.7.8**

## Stammdaten

Unter diesem Topic ist genau einer der folgenden 4 Prüfidentifikatoren zulässig — welcher, entscheidet der Event-Prozess.

| Prüfi | Scope | Anwendungsfall | Festlegung | Kommunikation |
|---|---|---|---|---|
| [PI_33001](/schnittstellen/202604/pruefi/REMADV/PI_33001) | REMADV | Bestätigung | WiM Gas | NB → MSBA |
| [PI_33002](/schnittstellen/202604/pruefi/REMADV/PI_33002) | REMADV | Abweisung | WiM Gas | NB → MSBA |
| [PI_33003](/schnittstellen/202604/pruefi/REMADV/PI_33003) | REMADV | Strom Abweisung Kopf und Summe | GPKE Teil 2 | LF → NB |
| [PI_33004](/schnittstellen/202604/pruefi/REMADV/PI_33004) | REMADV | Strom Abweisung Position | GPKE Teil 2 | LF → NB |

Die Stammdaten der 4 Prüfidentifikatoren in **einer** Struktur — eine Spalte je Prüfidentifikator, wie im Anwendungshandbuch. Ein Wert in der Spalte heißt, dass das Feld zu diesem Prüfidentifikator gehört: **Muss**, wenn seine Spezifikation es verlangt, sonst **Kann**. Eine leere Zelle heißt »gehört nicht dazu«, nicht »unbekannt«. Vorausgewählt ist der erste; die übrigen schaltet die Leiste über der Tabelle zu.

<Handbuchsatz>

<div className="maco-tabellenrahmen">

| Struktur (BO4E) | Beschreibung | Format | <span className="hbs-p" title="Bestätigung">33001</span> | <span className="hbs-p" title="Abweisung">33002</span> | <span className="hbs-p" title="Strom Abweisung Kopf und Summe">33003</span> | <span className="hbs-p" title="Strom Abweisung Position">33004</span> | Bedingung |
|---|---|---|---|---|---|---|---|
| <span className="hbs-g hbs-e0">**stammdaten**</span> | — | object | Kann | Kann | Kann | Kann | — |
| <span className="hbs-g hbs-e1">**AVIS** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | Muss | Muss | Muss | — |
| <span className="hbs-f hbs-e2">[avisNummer](/bo4e/202604/bo/Avis#avisnummer) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00010</span> | Eine im Verwendungskontext eindeutige Nummer für das Avis. | string | Muss | Muss | Muss | Muss | — |
| <span className="hbs-f hbs-e2">[avisTyp](/bo4e/202604/bo/Avis#avistyp) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00020</span> | Gibt den Typ des Avis an. | [Enum AvisTyp](/bo4e/202604/enum/AvisTyp) | Muss | Muss | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`ABGELEHNTE_FORDERUNG`</span> | — | — | Muss | Muss | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`ZAHLUNGSAVIS`</span> | — | — | Muss | Muss | Muss | Muss | — |
| <span className="hbs-g hbs-e2">**positionen** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | Muss | Muss | Muss | — |
| <span className="hbs-f hbs-e3">[istSelbstausgestellt](/bo4e/202604/com/Avisposition#istselbstausgestellt) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00030</span> | istSelbstausgestellt | boolean | Muss | Muss | Muss | Muss | — |
| <span className="hbs-f hbs-e3">[istStorno](/bo4e/202604/com/Avisposition#iststorno) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00040</span> | istStorno | boolean | Muss | Muss | Muss | Muss | — |
| <span className="hbs-f hbs-e3">[rechnungsDatum](/bo4e/202604/com/Avisposition#rechnungsdatum) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00050</span> | rechnungsDatum | string (date-time) | Muss | Muss | Muss | Muss | — |
| <span className="hbs-f hbs-e3">[rechnungsNummer](/bo4e/202604/com/Avisposition#rechnungsnummer) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00060</span> | rechnungsNummer | string | Muss | Muss | Muss | Muss | — |
| <span className="hbs-g hbs-e3">**gesamtBrutto** <span className="hbs-pflicht">\*</span></span> | — | object | Muss | Muss | Muss | Muss | — |
| <span className="hbs-f hbs-e4">[wert](/bo4e/202604/com/Betrag#wert) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00070</span> | Gibt den Betrag des Preises an. | number (float) | Muss | Muss | Muss | Muss | — |
| <span className="hbs-g hbs-e3">**zuZahlen** <span className="hbs-pflicht">\*</span></span> | — | object | Muss | Muss | Muss | Muss | — |
| <span className="hbs-f hbs-e4">[wert](/bo4e/202604/com/Betrag#wert) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00080</span> | Gibt den Betrag des Preises an. | number (float) | Muss | Muss | Muss | Muss | — |
| <span className="hbs-f hbs-e3">[referenz](/bo4e/202604/com/Avisposition#referenz)</span><span className="hbs-nr">00090</span> | referenz | string | — | Kann | Kann | Kann | — |
| <span className="hbs-g hbs-e3">**abweichung** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | — | Muss | Muss | — | — |
| <span className="hbs-f hbs-e4">[abweichungsgrundBemerkung1](/bo4e/202604/com/Abweichung#abweichungsgrundbemerkung1)</span><span className="hbs-nr">00100</span> | Abweichungsgrund Bemerkung 1 | string | — | Kann | Kann | — | — |
| <span className="hbs-f hbs-e4">[abweichungsgrundBemerkung2](/bo4e/202604/com/Abweichung#abweichungsgrundbemerkung2)</span><span className="hbs-nr">00110</span> | Abweichungsgrund Bemerkung 2 | string | — | Kann | Kann | — | — |
| <span className="hbs-f hbs-e4">[abweichungsgrundBemerkung3](/bo4e/202604/com/Abweichung#abweichungsgrundbemerkung3)</span><span className="hbs-nr">00120</span> | Abweichungsgrund Bemerkung 3 | string | — | Kann | Kann | — | — |
| <span className="hbs-f hbs-e4">[abweichungsgrundBemerkung4](/bo4e/202604/com/Abweichung#abweichungsgrundbemerkung4)</span><span className="hbs-nr">00130</span> | Abweichungsgrund Bemerkung 4 | string | — | Kann | Kann | — | — |
| <span className="hbs-f hbs-e4">[abweichungsgrundBemerkung5](/bo4e/202604/com/Abweichung#abweichungsgrundbemerkung5)</span><span className="hbs-nr">00140</span> | Abweichungsgrund Bemerkung 5 | string | — | Kann | Kann | — | — |
| <span className="hbs-f hbs-e4">[abweichungsgrundCode](/bo4e/202604/com/Abweichung#abweichungsgrundcode) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00150</span> | Code des Abweichungsgrundes | string | — | Muss | Muss | — | — |
| <span className="hbs-f hbs-e4">[abweichungsgrundCodeliste](/bo4e/202604/com/Abweichung#abweichungsgrundcodeliste) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00160</span> | Codeliste des Abweichungsgrund | string | — | Muss | Muss | — | — |
| <span className="hbs-f hbs-e4">[abschlagsrechnungen](/bo4e/202604/com/Abweichung#abschlagsrechnungen)</span><span className="hbs-nr">00170</span> | Abschlagsrechnungen | array | — | — | Kann | — | — |
| <span className="hbs-f hbs-e4">[fehlendePositionen1](/bo4e/202604/com/Abweichung#fehlendepositionen1)</span><span className="hbs-nr">00180</span> | fehlende Positionen 1 | string | — | — | Kann | — | — |
| <span className="hbs-f hbs-e4">[fehlendePositionen2](/bo4e/202604/com/Abweichung#fehlendepositionen2)</span><span className="hbs-nr">00190</span> | fehlende Positionen 2 | string | — | — | Kann | — | — |
| <span className="hbs-f hbs-e4">[fehlendePositionen3](/bo4e/202604/com/Abweichung#fehlendepositionen3)</span><span className="hbs-nr">00200</span> | fehlende Positionen 3 | string | — | — | Kann | — | — |
| <span className="hbs-f hbs-e4">[fehlendePositionen4](/bo4e/202604/com/Abweichung#fehlendepositionen4)</span><span className="hbs-nr">00210</span> | fehlende Positionen 4 | string | — | — | Kann | — | — |
| <span className="hbs-f hbs-e4">[fehlendePositionen5](/bo4e/202604/com/Abweichung#fehlendepositionen5)</span><span className="hbs-nr">00220</span> | fehlende Positionen 5 | string | — | — | Kann | — | — |
| <span className="hbs-f hbs-e4">[zugehoerigeRechnung](/bo4e/202604/com/Abweichung#zugehoerigerechnung)</span><span className="hbs-nr">00230</span> | Angabe der Rechnungsnummer, auf die sich diese Abweichung bezieht | string | — | — | Kann | — | — |
| <span className="hbs-g hbs-e3">**positionen** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | — | — | — | Muss | — |
| <span className="hbs-f hbs-e4">[positionsnummer](/bo4e/202604/com/Rueckmeldungsposition#positionsnummer) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00240</span> | positionsnummer | integer | — | — | — | Muss | — |
| <span className="hbs-g hbs-e4">**abweichung** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | — | — | — | Muss | — |
| <span className="hbs-f hbs-e5">[abweichungsgrundBemerkung1](/bo4e/202604/com/Abweichung#abweichungsgrundbemerkung1)</span><span className="hbs-nr">00250</span> | Abweichungsgrund Bemerkung 1 | string | — | — | — | Kann | — |
| <span className="hbs-f hbs-e5">[abweichungsgrundBemerkung2](/bo4e/202604/com/Abweichung#abweichungsgrundbemerkung2)</span><span className="hbs-nr">00260</span> | Abweichungsgrund Bemerkung 2 | string | — | — | — | Kann | — |
| <span className="hbs-f hbs-e5">[abweichungsgrundBemerkung3](/bo4e/202604/com/Abweichung#abweichungsgrundbemerkung3)</span><span className="hbs-nr">00270</span> | Abweichungsgrund Bemerkung 3 | string | — | — | — | Kann | — |
| <span className="hbs-f hbs-e5">[abweichungsgrundBemerkung4](/bo4e/202604/com/Abweichung#abweichungsgrundbemerkung4)</span><span className="hbs-nr">00280</span> | Abweichungsgrund Bemerkung 4 | string | — | — | — | Kann | — |
| <span className="hbs-f hbs-e5">[abweichungsgrundBemerkung5](/bo4e/202604/com/Abweichung#abweichungsgrundbemerkung5)</span><span className="hbs-nr">00290</span> | Abweichungsgrund Bemerkung 5 | string | — | — | — | Kann | — |
| <span className="hbs-f hbs-e5">[abweichungsgrundCode](/bo4e/202604/com/Abweichung#abweichungsgrundcode) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00300</span> | Code des Abweichungsgrundes | string | — | — | — | Muss | — |
| <span className="hbs-f hbs-e5">[abweichungsgrundCodeliste](/bo4e/202604/com/Abweichung#abweichungsgrundcodeliste) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00310</span> | Codeliste des Abweichungsgrund | string | — | — | — | Muss | — |
| <span className="hbs-f hbs-e5">[referenz](/bo4e/202604/com/Abweichung#referenz)</span><span className="hbs-nr">00320</span> | referenz | string | — | — | — | Kann | — |
| <span className="hbs-f hbs-e5">[zugehoerigeRechnung](/bo4e/202604/com/Abweichung#zugehoerigerechnung)</span><span className="hbs-nr">00330</span> | Angabe der Rechnungsnummer, auf die sich diese Abweichung bezieht | string | — | — | — | Kann | — |
| <span className="hbs-g hbs-e2">**zuZahlen** <span className="hbs-pflicht">\*</span></span> | — | object | Muss | Muss | Muss | Muss | — |
| <span className="hbs-f hbs-e3">[waehrung](/bo4e/202604/com/Betrag#waehrung) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00340</span> | Währung des Preises | string | Muss | Muss | Muss | Muss | — |
| <span className="hbs-f hbs-e3">[wert](/bo4e/202604/com/Betrag#wert) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00350</span> | Gibt den Betrag des Preises an. | number (float) | Muss | Muss | Muss | Muss | — |

</div>

</Handbuchsatz>

## Kette dieses Auslösers

Das Ereignis löst die Nachricht aus.

| Nachricht | Antworten | Schreibaufruf nach der Antwort |
|---|---|---|
| [33001](/schnittstellen/202604/pruefi/REMADV/PI_33001) | — | — |
| [33002](/schnittstellen/202604/pruefi/REMADV/PI_33002) | — | — |
| [33003](/schnittstellen/202604/pruefi/REMADV/PI_33003) | — | — |
| [33004](/schnittstellen/202604/pruefi/REMADV/PI_33004) | — | — |

Dieses Ereignis löst Schritte in diesen Rollensichten aus:

| Prozess | Beteiligter | Regelwerk | Sparte |
|---|---|---|---|
| [Abrechnung Leistungen des Preisblatts B des MSB zwischen MSB und LF](/prozessdoku/202604/LF/awh-prozesse-zur-anderung-der-technik-an-lokationen-abrechnung-leistungen-des-preisblatts-b-des-msb-zwischen-msb-und-lf) | LF | AWH Prozesse zur Änderung der Technik an Lokationen | Strom |
| [Abrechnung einer sonstigen Leistung](/prozessdoku/202604/LF/awh-sperrprozesse-gas-abrechnung-einer-sonstigen-leistung) | LF | AWH Sperrprozesse Gas | Gas |
| [Abrechnung einer sonstigen Leistung](/prozessdoku/202604/LF/GPKE-Teil2-abrechnung-einer-sonstigen-leistung) | LF | GPKE Teil 2 | Strom |
| [Netznutzungsabrechnung](/prozessdoku/202604/LF/GPKE-Teil2-netznutzungsabrechnung) | LF | GPKE Teil 2 | Strom |
| [Abrechnung Leistungen des Preisblatts A des MSB zwischen MSB und LF](/prozessdoku/202604/LF/GPKE-Teil3-abrechnung-leistungen-des-preisblatts-a-des-msb-zwischen-msb-und-lf) | LF | GPKE Teil 3 | Strom |
| [Abrechnung der Netznutzung](/prozessdoku/202604/LF/geli-gas-2-0-abrechnung-der-netznutzung) | LF | GeLi Gas 2.0 | Gas |
| [Mehr-/Mindermengenabrechnung zwischen NB und LF](/prozessdoku/202604/LF/prozesse-zur-ermittlung-und-abrechnung-von-mehr-mindermengen-strom-und-gas-mehr-mindermengenabrechnung-zwischen-nb-und-lf) | LF | Prozesse zur Ermittlung und Abrechnung von Mehr-/Mindermengen Strom und Gas | Strom und Gas |
| [Abrechnung Messstellenbetrieb gegenüber dem LF](/prozessdoku/202604/LF/WiM-Teil1-abrechnung-messstellenbetrieb-gegenueber-dem-lf) | LF | WiM Strom Teil 1 | Strom |

## Transaktionsdaten

Der Umschlag der Nachricht. Pflichtfelder müssen beim Trigger-Aufruf gesetzt sein.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| [kategorie](/bo4e/202604/cdoc/Transaktionsdaten#kategorie) | string | **ja** | Qualifier aus dem Beginn der EDIFact Nachricht / BGM |
| [nachrichtendatum](/bo4e/202604/cdoc/Transaktionsdaten#nachrichtendatum) | string (date-time) | **ja** | Erstellungdatum der EDIFact / DTM+137 |
| `pruefidentifikator` | — | **ja** | Wird dynamisch im Event-Prozess ermittelt (Entscheidungsgrundlage: kategorie, pruefi). Ein vom Sender mitgegebener Wert wird ignoriert. Im Topic mögliche Prüfis — 33001, 33002, 33003, 33004. Mögliche Werte: `33001`, `33002`, `33003`, `33004` |
| [sparte](/bo4e/202604/cdoc/Transaktionsdaten#sparte) | [Enum Sparte](/bo4e/202604/enum/Sparte) | **ja** | Enthält Informationen über die Sparte Werte: `STROM`, `GAS`, `FERNWAERME`, `NAHWAERME`, `WASSER`, `ABWASSER` |
| [absender › rollencodenummer](/bo4e/202604/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |
| [empfaenger › marktrolle](/bo4e/202604/bo/Marktteilnehmer#marktrolle) | [Enum Marktrolle](/bo4e/202604/enum/Marktrolle) | nein | Gibt im Klartext die Bezeichnung der Marktrolle an. Werte: `NB`, `LF`, `MSB`, `MSBA`, `GMSB`, `MDL`, `DL`, `BKV`, `UENB`, `KUNDE-SELBST-NN` … (+9) |
| [empfaenger › rollencodenummer](/bo4e/202604/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |

## Zusatzdaten

`eventname` ist auf **START_VERSAND_ANTWORT_NNA** festgelegt. Dieser Wert bleibt auch in der englischen Fassung deutsch, weil Camunda darüber korreliert.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `prozessId` | string | **ja** | — |
| `eventname` | const `START_VERSAND_ANTWORT_NNA` | **ja** | — |

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
