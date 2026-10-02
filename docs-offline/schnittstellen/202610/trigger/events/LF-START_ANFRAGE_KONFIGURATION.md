# [LF] START_ANFRAGE_KONFIGURATION
<span hidden data-pagefind-meta={"title:Trigger-Ereignis START_ANFRAGE_KONFIGURATION — Marktrolle LF (FV 202610)"} />

Marktrolle **LF** · Formatversion **202610** · BO4E-Schema **1.7.8**

## Stammdaten

Unter diesem Topic ist genau einer der folgenden 1 Prüfidentifikatoren zulässig — welcher, entscheidet der Event-Prozess.

| Prüfi | Scope | Anwendungsfall | Festlegung | Kommunikation |
|---|---|---|---|---|
| [PI_35004](/schnittstellen/202610/pruefi/REQOTE/PI_35004) | REQOTE | Anfrage einer Konfiguration | GPKE Teil 3 | NB → MSB |

Die Stammdaten der 1 Prüfidentifikatoren in **einer** Struktur — eine Spalte je Prüfidentifikator, wie im Anwendungshandbuch. Ein Wert in der Spalte heißt, dass das Feld zu diesem Prüfidentifikator gehört: **Muss**, wenn seine Spezifikation es verlangt, sonst **Kann**. Eine leere Zelle heißt »gehört nicht dazu«, nicht »unbekannt«. Vorausgewählt ist der erste; die übrigen schaltet die Leiste über der Tabelle zu.

<Handbuchsatz>

<div className="maco-tabellenrahmen">

| Struktur (BO4E) | Beschreibung | Format | <span className="hbs-p" title="Anfrage einer Konfiguration">35004</span> | Bedingung |
|---|---|---|---|---|
| <span className="hbs-g hbs-e0">**stammdaten**</span> | — | object | Kann | — |
| <span className="hbs-g hbs-e1">**AD_HOC_STEUERKANAL** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-f hbs-e2">[konfigurationsprodukt](/bo4e/202610/bo/AdHocSteuerkanal#konfigurationsprodukt)</span><span className="hbs-nr">00010</span> | konfigurationsprodukt | string | Kann | — |
| <span className="hbs-g hbs-e1">**ANFRAGE** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | — |
| <span className="hbs-f hbs-e2">[anfragetyp](/bo4e/202610/bo/Anfrage#anfragetyp) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00020</span> | Typ/Art der Anfrage (ORDERS ORDRSP IMD 7081) | [Enum Anfragetyp](/bo4e/202610/enum/Anfragetyp) | Muss | — |
| <span className="hbs-w hbs-e3">`KAUF`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`NUTZUNGSUEBERLASSUNG`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`ABRECHNUNGSBRENNWERT_UND_ZUSTANDSZAHL`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`LASTGANGDATEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`ZAEHLERSTAENDE`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`WERTEERMITTLUNG`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`ENERGIEMENGE_EINZELWERT`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`INNERHALB_DER_ARBEITSZEIT`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`AUCH_AUSSERHALB_DER_ARBEITSZEIT`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`WECHSEL_SAEMTLICHER_EINRICHTUNGEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`TEILWEISER_WECHSEL`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`AENDERUNG_ZAEHLZEITDEFINITION`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`ABBESTELLUNG_ZAEHLZEITEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`ABBESTELLUNG_MESSPRODUKT`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`ANGEBOT_AUF_BASIS_PREISBLATT`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`INDIVIDUELLES_ANGEBOT`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`AENDERUNG_KONFIGURATION`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`KANN_NICHT_ANGEBOTEN_WERDEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`NEUKONFIGURATION`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`BEENDIGUNG_KONFIGURATION`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`AKTIVIERUNG_KONFIGURATION`</span> | — | — | Muss | — |
| <span className="hbs-g hbs-e1">**LEISTUNGSKURVENDEFINITION** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-g hbs-e2">**leistungskurven** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-f hbs-e3">[code](/bo4e/202610/com/Leistungskurve#code)</span><span className="hbs-nr">00030</span> | Code der Leistungskurve | string | Kann | — |
| <span className="hbs-f hbs-e3">[konfigurationsprodukt](/bo4e/202610/com/Leistungskurve#konfigurationsprodukt)</span><span className="hbs-nr">00040</span> | Konfigurationsprodukt | string | Kann | — |
| <span className="hbs-g hbs-e1">**MARKTLOKATION** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-f hbs-e2">[marktlokationsId](/bo4e/202610/bo/Marktlokation#marktlokationsid)</span><span className="hbs-nr">00050</span> | Identifikationsnummer einer Marktlokation, an der Energie entweder<br/>verbraucht, oder erzeugt wird | string | Kann | — |
| <span className="hbs-g hbs-e1">**MESSLOKATION** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-f hbs-e2">[messlokationsId](/bo4e/202610/bo/Messlokation#messlokationsid)</span><span className="hbs-nr">00060</span> | Die Messlokations-Identifikation. Das ist die frühere Zählpunktbezeichnung,<br/>z.B. DE 47108151234567 | string | Kann | — |
| <span className="hbs-g hbs-e1">**NETZLOKATION** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-f hbs-e2">[netzlokationsId](/bo4e/202610/bo/Netzlokation#netzlokationsid)</span><span className="hbs-nr">00070</span> | Identifikationsnummer einer Netzlokation, an der Energie entweder<br/>verbraucht, oder erzeugt wird (Like MarktlokationsId Marktlokation) | string | Kann | — |
| <span className="hbs-g hbs-e1">**SCHALTZEITDEFINITION** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-g hbs-e2">**schaltzeiten** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-f hbs-e3">[code](/bo4e/202610/com/Schaltzeit#code)</span><span className="hbs-nr">00080</span> | code | string | Kann | — |
| <span className="hbs-f hbs-e3">[konfigurationsprodukt](/bo4e/202610/com/Schaltzeit#konfigurationsprodukt)</span><span className="hbs-nr">00090</span> | konfigurationsprodukt | string | Kann | — |
| <span className="hbs-g hbs-e1">**STEUERBARE_RESSOURCE** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-f hbs-e2">[ressourcenId](/bo4e/202610/bo/SteuerbareRessource#ressourcenid)</span><span className="hbs-nr">00100</span> | ressourcenId | string | Kann | — |
| <span className="hbs-g hbs-e1">**TECHNISCHE_RESSOURCE** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-f hbs-e2">[ressourcenId](/bo4e/202610/bo/TechnischeRessource#ressourcenid)</span><span className="hbs-nr">00110</span> | ressourcenId | string | Kann | — |
| <span className="hbs-g hbs-e1">**WERTE_NACH_TYP2** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-f hbs-e2">[aenderungsmoeglichkeitKonfiguration](/bo4e/202610/bo/WerteNachTyp2#aenderungsmoeglichkeitkonfiguration)</span><span className="hbs-nr">00120</span> | AenderungsmoeglichkeitKonfiguration | [Enum AenderungsmoeglichkeitKonfiguration](/bo4e/202610/enum/AenderungsmoeglichkeitKonfiguration) | Kann | — |
| <span className="hbs-w hbs-e3">`ERFORDERLICH`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`NICHT_ERFORDERLICH`</span> | — | — | Kann | — |
| <span className="hbs-f hbs-e2">[konfigurationsprodukt](/bo4e/202610/bo/WerteNachTyp2#konfigurationsprodukt)</span><span className="hbs-nr">00130</span> | konfigurationsprodukt | string | Kann | — |
| <span className="hbs-f hbs-e2">[messprodukt](/bo4e/202610/bo/WerteNachTyp2#messprodukt)</span><span className="hbs-nr">00140</span> | messprodukt | string | Kann | — |
| <span className="hbs-g hbs-e2">**aussteller**</span> | — | object | Kann | — |
| <span className="hbs-f hbs-e3">[aussteller1](/bo4e/202610/com/Aussteller#aussteller1)</span><span className="hbs-nr">00150</span> | aussteller1 | string | Kann | — |
| <span className="hbs-f hbs-e3">[aussteller2](/bo4e/202610/com/Aussteller#aussteller2)</span><span className="hbs-nr">00160</span> | aussteller2 | string | Kann | — |
| <span className="hbs-f hbs-e3">[aussteller3](/bo4e/202610/com/Aussteller#aussteller3)</span><span className="hbs-nr">00170</span> | aussteller3 | string | Kann | — |
| <span className="hbs-f hbs-e3">[aussteller4](/bo4e/202610/com/Aussteller#aussteller4)</span><span className="hbs-nr">00180</span> | aussteller4 | string | Kann | — |
| <span className="hbs-f hbs-e3">[aussteller5](/bo4e/202610/com/Aussteller#aussteller5)</span><span className="hbs-nr">00190</span> | aussteller5 | string | Kann | — |
| <span className="hbs-g hbs-e2">**schwellwerte** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-f hbs-e3">[konfigurationsprodukt](/bo4e/202610/com/Schwellwert#konfigurationsprodukt)</span><span className="hbs-nr">00200</span> | konfigurationsprodukt | string | Kann | — |
| <span className="hbs-f hbs-e3">[obererSchwellwert](/bo4e/202610/com/Schwellwert#obererschwellwert)</span><span className="hbs-nr">00210</span> | obererSchwellwert | number (float) | Kann | — |
| <span className="hbs-f hbs-e3">[untererSchwellwert](/bo4e/202610/com/Schwellwert#untererschwellwert)</span><span className="hbs-nr">00220</span> | untererSchwellwert | number (float) | Kann | — |
| <span className="hbs-g hbs-e2">**zertifikatsNutzer**</span> | — | object | Kann | — |
| <span className="hbs-f hbs-e3">[zertifikatsNutzer1](/bo4e/202610/com/ZertifikatsNutzer#zertifikatsnutzer1)</span><span className="hbs-nr">00230</span> | zertifikatsNutzer1 | string | Kann | — |
| <span className="hbs-f hbs-e3">[zertifikatsNutzer2](/bo4e/202610/com/ZertifikatsNutzer#zertifikatsnutzer2)</span><span className="hbs-nr">00240</span> | zertifikatsNutzer2 | string | Kann | — |
| <span className="hbs-f hbs-e3">[zertifikatsNutzer3](/bo4e/202610/com/ZertifikatsNutzer#zertifikatsnutzer3)</span><span className="hbs-nr">00250</span> | zertifikatsNutzer3 | string | Kann | — |
| <span className="hbs-f hbs-e3">[zertifikatsNutzer4](/bo4e/202610/com/ZertifikatsNutzer#zertifikatsnutzer4)</span><span className="hbs-nr">00260</span> | zertifikatsNutzer4 | string | Kann | — |
| <span className="hbs-f hbs-e3">[zertifikatsNutzer5](/bo4e/202610/com/ZertifikatsNutzer#zertifikatsnutzer5)</span><span className="hbs-nr">00270</span> | zertifikatsNutzer5 | string | Kann | — |
| <span className="hbs-g hbs-e2">**zieladresse**</span> | — | object | Kann | — |
| <span className="hbs-f hbs-e3">[zieladresse1](/bo4e/202610/com/Zieladresse#zieladresse1)</span><span className="hbs-nr">00280</span> | zieladresse1 | string | Kann | — |
| <span className="hbs-f hbs-e3">[zieladresse2](/bo4e/202610/com/Zieladresse#zieladresse2)</span><span className="hbs-nr">00290</span> | zieladresse2 | string | Kann | — |
| <span className="hbs-f hbs-e3">[zieladresse3](/bo4e/202610/com/Zieladresse#zieladresse3)</span><span className="hbs-nr">00300</span> | zieladresse3 | string | Kann | — |
| <span className="hbs-f hbs-e3">[zieladresse4](/bo4e/202610/com/Zieladresse#zieladresse4)</span><span className="hbs-nr">00310</span> | zieladresse4 | string | Kann | — |
| <span className="hbs-f hbs-e3">[zieladresse5](/bo4e/202610/com/Zieladresse#zieladresse5)</span><span className="hbs-nr">00320</span> | zieladresse5 | string | Kann | — |

</div>

</Handbuchsatz>

## Kette dieses Auslösers

Das Ereignis löst die Nachricht aus. Der Marktpartner antwortet mit einer der genannten Antworten, und danach schreibt die MACO APP den Vorgang in Ihr Backendsystem.

| Nachricht | Antworten | Schreibaufruf nach der Antwort |
|---|---|---|
| [35004](/schnittstellen/202610/pruefi/REQOTE/PI_35004) | [21033](/schnittstellen/202610/pruefi/IFTSTA/PI_21033) | `POST /createProcessData` |

Dieses Ereignis löst einen Schritt in dieser Rollensicht aus:

| Prozess | Beteiligter | Regelwerk | Sparte |
|---|---|---|---|
| [Bestellung einer Konfiguration vom LF an MSB](/prozessdoku/202610/LF/GPKE-Teil3-bestellung-einer-konfiguration-vom-lf-an-msb) | LF | GPKE Teil 3 | Strom |

## Transaktionsdaten

Der Umschlag der Nachricht. Pflichtfelder müssen beim Trigger-Aufruf gesetzt sein.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| [kategorie](/bo4e/202610/cdoc/Transaktionsdaten#kategorie) | string | **ja** | Qualifier aus dem Beginn der EDIFact Nachricht / BGM |
| [lieferdatum](/bo4e/202610/cdoc/Transaktionsdaten#lieferdatum) | string (date-time) | **ja** | Lieferdatum DTM+76 |
| [sparte](/bo4e/202610/cdoc/Transaktionsdaten#sparte) | [Enum Sparte](/bo4e/202610/enum/Sparte) | **ja** | Enthält Informationen über die Sparte Werte: `STROM`, `GAS`, `FERNWAERME`, `NAHWAERME`, `WASSER`, `ABWASSER` |
| `pruefidentifikator` | — | nein | Wird dynamisch im Event-Prozess ermittelt. Ein vom Sender mitgegebener Wert wird ignoriert. Im Topic mögliche Prüfis — 35004. Mögliche Werte: `35004` |
| [absender › rollencodenummer](/bo4e/202610/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |
| [empfaenger › rollencodenummer](/bo4e/202610/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |

## Zusatzdaten

`eventname` ist auf **START_ANFRAGE_KONFIGURATION** festgelegt. Dieser Wert bleibt auch in der englischen Fassung deutsch, weil Camunda darüber korreliert.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `prozessId` | string | **ja** | — |
| `eventname` | const `START_ANFRAGE_KONFIGURATION` | **ja** | — |

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
