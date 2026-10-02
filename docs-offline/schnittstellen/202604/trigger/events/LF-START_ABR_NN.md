# [LF] START_ABR_NN
<span hidden data-pagefind-meta={"title:Trigger-Ereignis START_ABR_NN — Marktrolle LF (FV 202604)"} />

Marktrolle **LF** · Formatversion **202604** · BO4E-Schema **1.7.8**

## Stammdaten

Unter diesem Topic ist genau einer der folgenden 1 Prüfidentifikatoren zulässig — welcher, entscheidet der Event-Prozess.

| Prüfi | Scope | Anwendungsfall | Festlegung | Kommunikation |
|---|---|---|---|---|
| [PI_55218](/schnittstellen/202604/pruefi/UTILMD/PI_55218) | UTILMD | Abr.-Daten NNA | GPKE Teil 2 | NB → LF |

Die Stammdaten der 1 Prüfidentifikatoren in **einer** Struktur — eine Spalte je Prüfidentifikator, wie im Anwendungshandbuch. Ein Wert in der Spalte heißt, dass das Feld zu diesem Prüfidentifikator gehört: **Muss**, wenn seine Spezifikation es verlangt, sonst **Kann**. Eine leere Zelle heißt »gehört nicht dazu«, nicht »unbekannt«. Vorausgewählt ist der erste; die übrigen schaltet die Leiste über der Tabelle zu.

<Handbuchsatz>

<div className="maco-tabellenrahmen">

| Struktur (BO4E) | Beschreibung | Format | <span className="hbs-p" title="Abr.-Daten NNA">55218</span> | Bedingung |
|---|---|---|---|---|
| <span className="hbs-g hbs-e0">**stammdaten**</span> | — | object | Kann | — |
| <span className="hbs-g hbs-e1">**BILANZIERUNG** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-g hbs-e2">**verbrauchsaufteilung**</span> | — | object | Kann | — |
| <span className="hbs-f hbs-e3">[einheit](/bo4e/202604/com/Menge#einheit)</span><span className="hbs-nr">00010</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202604/enum/Mengeneinheit) | Kann | — |
| <span className="hbs-w hbs-e4">`W`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`WH`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`KW`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`KWH`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`KVARH`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MW`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MWH`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`STUECK`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`KUBIKMETER`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`STUNDE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`TAG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MONAT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`JAHR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`PROZENT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`ANZAHL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`VAR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`KVAR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`VARH`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`KWHK`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`Z16`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`KWT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`WATT_PRO_QUADRATMETER`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`METER_PRO_SEKUNDE`</span> | — | — | Kann | — |
| <span className="hbs-f hbs-e3">[wert](/bo4e/202604/com/Menge#wert)</span><span className="hbs-nr">00020</span> | Wert | number (float) | Kann | — |
| <span className="hbs-g hbs-e1">**MARKTLOKATION** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-f hbs-e2">[datenqualitaet](/bo4e/202604/bo/Marktlokation#datenqualitaet)</span><span className="hbs-nr">00030</span> | Datenqualitaet | [Enum Datenqualitaet](/bo4e/202604/enum/Datenqualitaet) | Kann | — |
| <span className="hbs-w hbs-e3">`ERWARTETE_DATEN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`INFORMATIVE_DATEN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`GUELTIGE_DATEN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_KEINE_DATEN_VORHANDEN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN_ERWARTET`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_DATEN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_ERWARTETE_DATEN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | Kann | — |
| <span className="hbs-f hbs-e2">[marktlokationsId](/bo4e/202604/bo/Marktlokation#marktlokationsid)</span><span className="hbs-nr">00040</span> | Identifikationsnummer einer Marktlokation, an der Energie entweder<br/>verbraucht, oder erzeugt wird | string | Kann | — |
| <span className="hbs-f hbs-e2">[netzbetreiberCodeNr](/bo4e/202604/bo/Marktlokation#netzbetreibercodenr)</span><span className="hbs-nr">00050</span> | Codenummer des Netzbetreibers, an dessen Netz diese Marktlokation<br/>angeschlossen ist. | string | Kann | — |
| <span className="hbs-g hbs-e2">**gueltigkeitszeitraum**</span> | — | object | Kann | — |
| <span className="hbs-f hbs-e3">[zeitraumId](/bo4e/202604/com/Zeitraum#zeitraumid)</span><span className="hbs-nr">00060</span> | zeitraumId | integer | Kann | — |
| <span className="hbs-g hbs-e2">**netznutzungsabrechnungsdaten** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-f hbs-e3">[abschlag](/bo4e/202604/com/Netznutzungsabrechnungsdaten#abschlag)</span><span className="hbs-nr">00070</span> | Abschlag | number (float) | Kann | — |
| <span className="hbs-f hbs-e3">[anzahl](/bo4e/202604/com/Netznutzungsabrechnungsdaten#anzahl)</span><span className="hbs-nr">00080</span> | Anzahl | integer | Kann | — |
| <span className="hbs-f hbs-e3">[artikelId](/bo4e/202604/com/Netznutzungsabrechnungsdaten#artikelid)</span><span className="hbs-nr">00090</span> | artikelId | string | Kann | — |
| <span className="hbs-f hbs-e3">[artikelIdTyp](/bo4e/202604/com/Netznutzungsabrechnungsdaten#artikelidtyp)</span><span className="hbs-nr">00100</span> | Liste von Artikel-IDs, z.B. für standardisierte vom BDEW herausgegebene Artikel, die im Strommarkt die BDEW-Artikelnummer ablösen | [Enum ArtikelIdTyp](/bo4e/202604/enum/ArtikelIdTyp) | Kann | — |
| <span className="hbs-w hbs-e4">`ARTIKELID`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`GRUPPENARTIKELID`</span> | — | — | Kann | — |
| <span className="hbs-f hbs-e3">[gemeinderabatt](/bo4e/202604/com/Netznutzungsabrechnungsdaten#gemeinderabatt)</span><span className="hbs-nr">00110</span> | Gemeinderabatt | number (float) | Kann | — |
| <span className="hbs-f hbs-e3">[zuschlag](/bo4e/202604/com/Netznutzungsabrechnungsdaten#zuschlag)</span><span className="hbs-nr">00120</span> | Zuschlag | number (float) | Kann | — |
| <span className="hbs-g hbs-e3">**preisSingulaereBetriebsmittel**</span> | — | object | Kann | — |
| <span className="hbs-f hbs-e4">[wert](/bo4e/202604/com/Preis#wert)</span><span className="hbs-nr">00130</span> | wert | number (float) | Kann | — |
| <span className="hbs-g hbs-e3">**singulaereBetriebsmittel**</span> | — | object | Kann | — |
| <span className="hbs-f hbs-e4">[wert](/bo4e/202604/com/Menge#wert)</span><span className="hbs-nr">00140</span> | Wert | number (float) | Kann | — |
| <span className="hbs-g hbs-e3">**zaehlzeiten**</span> | — | object | Kann | — |
| <span className="hbs-f hbs-e4">[register](/bo4e/202604/com/Zaehlzeitregister#register)</span><span className="hbs-nr">00150</span> | Zählzeitregister | string | Kann | — |
| <span className="hbs-f hbs-e4">[zaehlzeitDefinition](/bo4e/202604/com/Zaehlzeitregister#zaehlzeitdefinition)</span><span className="hbs-nr">00160</span> | Zählzeitdefinition | string | Kann | — |
| <span className="hbs-g hbs-e1">**NETZNUTZUNGSVERTRAG** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-g hbs-e2">**vertragskonditionen**</span> | — | object | Kann | — |
| <span className="hbs-f hbs-e3">[naechstenetznutzungsabrechnung](/bo4e/202604/com/Vertragskonditionen#naechstenetznutzungsabrechnung)</span><span className="hbs-nr">00170</span> | naechstenetznutzungsabrechnung | string | Kann | — |
| <span className="hbs-f hbs-e3">[netznutzungsabrechnungIntervall](/bo4e/202604/com/Vertragskonditionen#netznutzungsabrechnungintervall)</span><span className="hbs-nr">00180</span> | netznutzungsabrechnungIntervall | integer | Kann | — |
| <span className="hbs-f hbs-e3">[netznutzungsabrechnungsgrundlage](/bo4e/202604/com/Vertragskonditionen#netznutzungsabrechnungsgrundlage)</span><span className="hbs-nr">00190</span> | Netznutzungsabrechnungsgrundlage | [Enum Netznutzungsabrechnungsgrundlage](/bo4e/202604/enum/Netznutzungsabrechnungsgrundlage) | Kann | — |
| <span className="hbs-w hbs-e4">`LIEFERSCHEIN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`ABWEICHENDE_GRUNDLAGE`</span> | — | — | Kann | — |
| <span className="hbs-f hbs-e3">[netznutzungsvertrag](/bo4e/202604/com/Vertragskonditionen#netznutzungsvertrag)</span><span className="hbs-nr">00200</span> | Netznutzungsvertrag | [Enum Netznutzungsvertrag](/bo4e/202604/enum/Netznutzungsvertrag) | Kann | — |
| <span className="hbs-w hbs-e4">`KUNDEN_NB`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`LIEFERANTEN_NB`</span> | — | — | Kann | — |
| <span className="hbs-f hbs-e3">[netznutzungszahler](/bo4e/202604/com/Vertragskonditionen#netznutzungszahler)</span><span className="hbs-nr">00210</span> | Netznutzungszahler | [Enum Netznutzungszahler](/bo4e/202604/enum/Netznutzungszahler) | Kann | — |
| <span className="hbs-w hbs-e4">`KUNDE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`LIEFERANT`</span> | — | — | Kann | — |
| <span className="hbs-g hbs-e3">**netznutzungsabrechnung**</span> | — | object | Kann | — |
| <span className="hbs-f hbs-e4">[abrechnungsZeitraum](/bo4e/202604/com/Zeitraum#abrechnungszeitraum)</span><span className="hbs-nr">00220</span> | abrechnungsZeitraum | string | Kann | — |
| <span className="hbs-g hbs-e1">**VERWENDUNGSZEITRAUM** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | — |
| <span className="hbs-f hbs-e2">[datenqualitaet](/bo4e/202604/bo/Verwendungszeitraum#datenqualitaet) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00230</span> | Datenqualitaet | [Enum Datenqualitaet](/bo4e/202604/enum/Datenqualitaet) | Muss | — |
| <span className="hbs-w hbs-e3">`ERWARTETE_DATEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`INFORMATIVE_DATEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`GUELTIGE_DATEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_KEINE_DATEN_VORHANDEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN_ERWARTET`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_DATEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_ERWARTETE_DATEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | Muss | — |
| <span className="hbs-f hbs-e2">[verwendungAb](/bo4e/202604/bo/Verwendungszeitraum#verwendungab) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00240</span> | verwendungAb | string (date-time) | Muss | — |
| <span className="hbs-f hbs-e2">[verwendungBis](/bo4e/202604/bo/Verwendungszeitraum#verwendungbis)</span><span className="hbs-nr">00250</span> | verwendungBis | string (date-time) | Kann | — |
| <span className="hbs-f hbs-e2">[zeitraumId](/bo4e/202604/bo/Verwendungszeitraum#zeitraumid) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00260</span> | zeitraumId | integer | Muss | — |

</div>

</Handbuchsatz>

## Kette dieses Auslösers

Das Ereignis löst die Nachricht aus.

| Nachricht | Antworten | Schreibaufruf nach der Antwort |
|---|---|---|
| [55218](/schnittstellen/202604/pruefi/UTILMD/PI_55218) | — | — |

## Transaktionsdaten

Der Umschlag der Nachricht. Pflichtfelder müssen beim Trigger-Aufruf gesetzt sein.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| [kategorie](/bo4e/202604/cdoc/Transaktionsdaten#kategorie) | string | **ja** | Qualifier aus dem Beginn der EDIFact Nachricht / BGM |
| `pruefidentifikator` | — | nein | Wird dynamisch im Event-Prozess ermittelt. Ein vom Sender mitgegebener Wert wird ignoriert. Im Topic mögliche Prüfis — 55218. Mögliche Werte: `55218` |
| [absender › rollencodenummer](/bo4e/202604/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |
| [empfaenger › rollencodenummer](/bo4e/202604/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |

## Zusatzdaten

`eventname` ist auf **START_ABR_NN** festgelegt. Dieser Wert bleibt auch in der englischen Fassung deutsch, weil Camunda darüber korreliert.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `prozessId` | string | **ja** | — |
| `eventname` | const `START_ABR_NN` | **ja** | — |

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
