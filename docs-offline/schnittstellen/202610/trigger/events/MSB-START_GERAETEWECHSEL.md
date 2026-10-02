# [MSB] START_GERAETEWECHSEL
<span hidden data-pagefind-meta={"title:Trigger-Ereignis START_GERAETEWECHSEL — Marktrolle MSB (FV 202610)"} />

Marktrolle **MSB** · Formatversion **202610** · BO4E-Schema **1.7.8**

## Stammdaten

Unter diesem Topic ist genau einer der folgenden 1 Prüfidentifikatoren zulässig — welcher, entscheidet der Event-Prozess.

| Prüfi | Scope | Anwendungsfall | Festlegung | Kommunikation |
|---|---|---|---|---|
| [PI_17009](/schnittstellen/202610/pruefi/ORDERS/PI_17009) | ORDERS | Anzeige Gerätewechselabsicht | WiM Strom Teil 1 | MSB (entspricht MSBN am Objekt Messlokation) → MSB (entspricht MSBA am Objekt Messlokation) |

Die Stammdaten der 1 Prüfidentifikatoren in **einer** Struktur — eine Spalte je Prüfidentifikator, wie im Anwendungshandbuch. Ein Wert in der Spalte heißt, dass das Feld zu diesem Prüfidentifikator gehört: **Muss**, wenn seine Spezifikation es verlangt, sonst **Kann**. Eine leere Zelle heißt »gehört nicht dazu«, nicht »unbekannt«. Vorausgewählt ist der erste; die übrigen schaltet die Leiste über der Tabelle zu.

<Handbuchsatz>

<div className="maco-tabellenrahmen">

| Struktur (BO4E) | Beschreibung | Format | <span className="hbs-p" title="Anzeige Gerätewechselabsicht">17009</span> | Bedingung |
|---|---|---|---|---|
| <span className="hbs-g hbs-e0">**stammdaten**</span> | — | object | Kann | — |
| <span className="hbs-g hbs-e1">**ANFRAGE** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | — |
| <span className="hbs-f hbs-e2">[anfragetyp](/bo4e/202610/bo/Anfrage#anfragetyp) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00010</span> | Typ/Art der Anfrage (ORDERS ORDRSP IMD 7081) | [Enum Anfragetyp](/bo4e/202610/enum/Anfragetyp) | Muss | — |
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
| <span className="hbs-f hbs-e2">[lokationsId](/bo4e/202610/bo/Anfrage#lokationsid) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00020</span> | Für welche Markt- oder Messlokation gilt diese Anfrage. | string | Muss | — |
| <span className="hbs-g hbs-e1">**AUFTRAG** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | — |
| <span className="hbs-f hbs-e2">[ausfuehrungsdatum](/bo4e/202610/bo/Auftrag#ausfuehrungsdatum) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00030</span> | Das Ausführungsdatum beschreibt zu welchem Zeitpunkt ein Auftrag ausgeführt werden soll. | string (date-time) | Muss | — |
| <span className="hbs-g hbs-e1">**ZAEHLER** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | — |
| <span className="hbs-g hbs-e2">**geraete** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | — |
| <span className="hbs-f hbs-e3">[geraetenummer](/bo4e/202610/com/Geraet#geraetenummer) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00040</span> | Die auf dem Geräte aufgedruckte Nummer, die vom MSB vergeben wird. | string | Muss | — |
| <span className="hbs-f hbs-e3">[weitereGeraetenummern](/bo4e/202610/com/Geraet#weiteregeraetenummern)</span><span className="hbs-nr">00050</span> | weitereGeraetenummern | array | Kann | — |
| <span className="hbs-g hbs-e3">**geraeteeigenschaften** <span className="hbs-pflicht">\*</span></span> | — | object | Muss | — |
| <span className="hbs-f hbs-e4">[geraetetyp](/bo4e/202610/com/Geraeteeigenschaften#geraetetyp) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00060</span> | Auflistung möglicher abzurechnender Gerätetypen | [Enum Geraetetyp](/bo4e/202610/enum/Geraetetyp) | Muss | — |
| <span className="hbs-w hbs-e5">`WECHSELSTROMZAEHLER`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`DREHSTROMZAEHLER`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`ZWEIRICHTUNGSZAEHLER`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`RLM_ZAEHLER`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`IMS_ZAEHLER`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`BALGENGASZAEHLER`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`MAXIMUMZAEHLER`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`MULTIPLEXANLAGE`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`PAUSCHALANLAGE`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`VERSTAERKERANLAGE`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`SUMMATIONSGERAET`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`IMPULSGEBER`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`EDL_21_ZAEHLERAUFSATZ`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`VIER_QUADRANTEN_LASTGANGZAEHLER`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`MENGENUMWERTER`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`STROMWANDLER`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`SPANNUNGSWANDLER`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`DATENLOGGER`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`KOMMUNIKATIONSANSCHLUSS`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`MODEM`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`TELEKOMMUNIKATIONSEINRICHTUNG`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`KOMMUNIKATIONSEINRICHTUNG`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`DREHKOLBENGASZAEHLER`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`TURBINENRADGASZAEHLER`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`ULTRASCHALLZAEHLER`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`WIRBELGASZAEHLER`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`MODERNE_MESSEINRICHTUNG`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`ELEKTRONISCHER_HAUSHALTSZAEHLER`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`STEUEREINRICHTUNG`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`TECHNISCHESTEUEREINRICHTUNG`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`TARIFSCHALTGERAET`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`RUNDSTEUEREMPFAENGER`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`OPTIONALE_ZUS_ZAEHLEINRICHTUNG`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`MESSWANDLERSATZ_IMS_MME`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`KOMBIMESSWANDLER_IMS_MME`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`TARIFSCHALTGERAET_IMS_MME`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`RUNDSTEUEREMPFAENGER_IMS_MME`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`TEMPERATUR_KOMPENSATION`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`HOECHSTBELASTUNGS_ANZEIGER`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`SONSTIGES_GERAET`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`SMARTMETERGATEWAY`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`STEUERBOX`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`BLOCKSTROMWANDLER`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`KOMBIMESSWANDLER`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`MODEM_GSM`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`ETHERNET_KOM`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`PLC_COM`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`MODEM_FESTNETZ`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`DSL_KOM`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`LTE_KOM`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`DICHTEMENGENUMWERTER`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`TEMPERATURMENGENUMWERTER`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`ZUSTANDSMENGENUMWERTER`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`MESSDATENREGISTRIERGERAET`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`WANDLER`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e5">`BEFESTIGUNGSEINRICHTUNG`</span> | — | — | Muss | — |

</div>

</Handbuchsatz>

## Kette dieses Auslösers

Das Ereignis löst die Nachricht aus. Der Marktpartner antwortet mit einer der genannten Antworten, und danach schreibt die MACO APP den Vorgang in Ihr Backendsystem.

| Nachricht | Antworten | Schreibaufruf nach der Antwort |
|---|---|---|
| [17009](/schnittstellen/202610/pruefi/ORDERS/PI_17009) | [19015](/schnittstellen/202610/pruefi/ORDRSP/PI_19015), [19016](/schnittstellen/202610/pruefi/ORDRSP/PI_19016) | `AKTUALISIEREN_PROZESSDATEN_BASIS` |

Dieses Ereignis löst Schritte in diesen Rollensichten aus:

| Prozess | Beteiligter | Regelwerk | Sparte |
|---|---|---|---|
| [Gerätewechsel](/prozessdoku/202610/MSB--MSBN/awh-wim-gas-2-0-geratewechsel) | MSBN | AWH WiM Gas 2.0 | Gas |
| [Gerätewechsel](/prozessdoku/202610/MSB--MSBN/WiM-Teil1-geraetewechsel) | MSBN | WiM Strom Teil 1 | Strom |

## Transaktionsdaten

Der Umschlag der Nachricht. Pflichtfelder müssen beim Trigger-Aufruf gesetzt sein.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| [kategorie](/bo4e/202610/cdoc/Transaktionsdaten#kategorie) | string | **ja** | Qualifier aus dem Beginn der EDIFact Nachricht / BGM |
| [sparte](/bo4e/202610/cdoc/Transaktionsdaten#sparte) | [Enum Sparte](/bo4e/202610/enum/Sparte) | **ja** | Enthält Informationen über die Sparte Werte: `STROM`, `GAS`, `FERNWAERME`, `NAHWAERME`, `WASSER`, `ABWASSER` |
| `pruefidentifikator` | — | nein | Wird dynamisch im Event-Prozess ermittelt. Ein vom Sender mitgegebener Wert wird ignoriert. Im Topic mögliche Prüfis — 17009. Mögliche Werte: `17009` |
| [absender › marktrolle](/bo4e/202610/bo/Marktteilnehmer#marktrolle) | [Enum Marktrolle](/bo4e/202610/enum/Marktrolle) | nein | Gibt im Klartext die Bezeichnung der Marktrolle an. Werte: `NB`, `LF`, `MSB`, `MSBA`, `GMSB`, `MDL`, `DL`, `BKV`, `UENB`, `KUNDE-SELBST-NN` … (+9) |
| [absender › rollencodenummer](/bo4e/202610/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |
| [empfaenger › marktrolle](/bo4e/202610/bo/Marktteilnehmer#marktrolle) | [Enum Marktrolle](/bo4e/202610/enum/Marktrolle) | nein | Gibt im Klartext die Bezeichnung der Marktrolle an. Werte: `NB`, `LF`, `MSB`, `MSBA`, `GMSB`, `MDL`, `DL`, `BKV`, `UENB`, `KUNDE-SELBST-NN` … (+9) |
| [empfaenger › rollencodenummer](/bo4e/202610/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |

## Zusatzdaten

`eventname` ist auf **START_GERAETEWECHSEL** festgelegt. Dieser Wert bleibt auch in der englischen Fassung deutsch, weil Camunda darüber korreliert.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `prozessId` | string | **ja** | — |
| `eventname` | const `START_GERAETEWECHSEL` | **ja** | — |

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
