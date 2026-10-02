# [LF] START_ANFRAGE_MESSWERTE
<span hidden data-pagefind-meta={"title:Trigger-Ereignis START_ANFRAGE_MESSWERTE — Marktrolle LF (FV 202610)"} />

Marktrolle **LF** · Formatversion **202610** · BO4E-Schema **1.7.8**

## Stammdaten

Unter diesem Topic ist genau einer der folgenden 1 Prüfidentifikatoren zulässig — welcher, entscheidet der Event-Prozess.

| Prüfi | Scope | Anwendungsfall | Festlegung | Kommunikation |
|---|---|---|---|---|
| [PI_17102](/schnittstellen/202610/pruefi/ORDERS/PI_17102) | ORDERS | Anfrage von Werten | GPKE Teil 4 | LF → MSB |

Die Stammdaten der 1 Prüfidentifikatoren in **einer** Struktur — eine Spalte je Prüfidentifikator, wie im Anwendungshandbuch. Ein Wert in der Spalte heißt, dass das Feld zu diesem Prüfidentifikator gehört: **Muss**, wenn seine Spezifikation es verlangt, sonst **Kann**. Eine leere Zelle heißt »gehört nicht dazu«, nicht »unbekannt«. Vorausgewählt ist der erste; die übrigen schaltet die Leiste über der Tabelle zu.

<Handbuchsatz>

<div className="maco-tabellenrahmen">

| Struktur (BO4E) | Beschreibung | Format | <span className="hbs-p" title="Anfrage von Werten">17102</span> | Bedingung |
|---|---|---|---|---|
| <span className="hbs-g hbs-e0">**stammdaten**</span> | — | object | Kann | — |
| <span className="hbs-g hbs-e1">**ANFRAGE** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | — |
| <span className="hbs-f hbs-e2">[anfragekategorie](/bo4e/202610/bo/Anfrage#anfragekategorie) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00010</span> | Kategorie der Anfrage (ORDERS ORDRSP BGM 1001) | [Enum Anfragekategorie](/bo4e/202610/enum/Anfragekategorie) | Muss | — |
| <span className="hbs-w hbs-e3">`PROZESSDATENBERICHT`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`GERAETEUEBERNAHME`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`WEITERVERPFLICHTUNG_BETRIEB_MELO`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`AENDERUNG_MELO`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`STAMMDATEN_MALO_ODER_MELO`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`BILANZIERTE_MENGE_MEHR_MINDER_MENGEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`ALLOKATIONSLISTE_MEHR_MINDER_MENGEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`ENERGIEMENGE_UND_LEISTUNGSMAXIMUM`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`ABRECHNUNG_MESSSTELLENBETRIEB_MSB_AN_LF`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`AENDERUNG_PROGNOSEGRUNDLAGE_GERAETEKONFIGURATION`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`AENDERUNG_GERAETEKONFIGURATION`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`REKLAMATION_VON_WERTEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`LASTGANG_MALO_TRANCHE`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`SPERRUNG`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`ENTSPERRUNG`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`REKLAMATION_ZAEHLZEITDEFINITION`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`ZEITREIHEN_IM_RAHMEN_BILANZKREISABRECHNUNG`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`GERAETEWECHSELABSICHT`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`AENDERUNG_KONZESSIONSABGABE`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`AENDERUNG_ZAEHLZEITDEFINITION`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`UEBERMITTLUNG_WERTE_AN_ESA`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`AENDERUNG`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`BILANZKREISZUORDNUNGSLISTE`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`CLEARINGLISTE`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`NORMIERTES_PROFIL_PROFILSCHAR`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`REDISPATCH_EINZELZEITREIHE_AUSFALLARBEIT`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`REKLAMATION_PROFIL_PROFILSCHAR`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`STAMMDATEN_MALO`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`STAMMDATEN_MELO`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`STAMMDATEN_TRANCHE`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`BEENDIGUNG_EINER_KONFIGURATION`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`BESTELLUNG_EINER_KONFIGURATION`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`BESTELLUNG_EINES_ANGEBOTS_EINER_KONFIGURATION`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`REKLAMATION_EINER_KONFIGURATION`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`BESTELLUNG_AENDERUNG_NETZENTGELTE_NETZORIENTIERTER_STEUERUNGSMOEGLICHKEIT`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`AENDERUNG_DER_TECHNIK_DER_LOKATION`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`AENDERUNG_INDIVIDUELLER_KONFIGURATION`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`BESTELLUNG_AENDERUNG_ABRECHNUNGSDATEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`EINRICHTUNG_KONFIGURATION_AUFGRUND_ZUORDNUNG_LF`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`REKLAMATION_DEFINITION`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`BESTELLUNG_ANGEBOT_AENDERUNG_TECHNIK_LOKATION`</span> | — | — | Muss | — |
| <span className="hbs-f hbs-e2">[anfragetyp](/bo4e/202610/bo/Anfrage#anfragetyp)</span><span className="hbs-nr">00020</span> | Typ/Art der Anfrage (ORDERS ORDRSP IMD 7081) | [Enum Anfragetyp](/bo4e/202610/enum/Anfragetyp) | Kann | — |
| <span className="hbs-w hbs-e3">`KAUF`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`NUTZUNGSUEBERLASSUNG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`ABRECHNUNGSBRENNWERT_UND_ZUSTANDSZAHL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`LASTGANGDATEN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`ZAEHLERSTAENDE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`WERTEERMITTLUNG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`ENERGIEMENGE_EINZELWERT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`INNERHALB_DER_ARBEITSZEIT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`AUCH_AUSSERHALB_DER_ARBEITSZEIT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`WECHSEL_SAEMTLICHER_EINRICHTUNGEN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`TEILWEISER_WECHSEL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`AENDERUNG_ZAEHLZEITDEFINITION`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`ABBESTELLUNG_ZAEHLZEITEN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`ABBESTELLUNG_MESSPRODUKT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`ANGEBOT_AUF_BASIS_PREISBLATT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`INDIVIDUELLES_ANGEBOT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`AENDERUNG_KONFIGURATION`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`KANN_NICHT_ANGEBOTEN_WERDEN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`NEUKONFIGURATION`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`BEENDIGUNG_KONFIGURATION`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`AKTIVIERUNG_KONFIGURATION`</span> | — | — | Kann | — |
| <span className="hbs-f hbs-e2">[lokationsId](/bo4e/202610/bo/Anfrage#lokationsid) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00030</span> | Für welche Markt- oder Messlokation gilt diese Anfrage. | string | Muss | — |
| <span className="hbs-g hbs-e1">**AUFTRAG** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | — |
| <span className="hbs-g hbs-e2">**positionsdaten** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | — |
| <span className="hbs-f hbs-e3">[enddatum](/bo4e/202610/com/AuftragPosition#enddatum) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00040</span> | enddatum | string (date-time) | Muss | — |
| <span className="hbs-f hbs-e3">[startdatum](/bo4e/202610/com/AuftragPosition#startdatum) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00050</span> | startdatum | string (date-time) | Muss | — |

</div>

</Handbuchsatz>

## Kette dieses Auslösers

Das Ereignis löst die Nachricht aus. Der Marktpartner antwortet mit einer der genannten Antworten, und danach schreibt die MACO APP den Vorgang in Ihr Backendsystem.

| Nachricht | Antworten | Schreibaufruf nach der Antwort |
|---|---|---|
| [17102](/schnittstellen/202610/pruefi/ORDERS/PI_17102) | [13002](/schnittstellen/202610/pruefi/MSCONS/PI_13002), [13008](/schnittstellen/202610/pruefi/MSCONS/PI_13008), [13009](/schnittstellen/202610/pruefi/MSCONS/PI_13009), [13016](/schnittstellen/202610/pruefi/MSCONS/PI_13016), [13017](/schnittstellen/202610/pruefi/MSCONS/PI_13017), [13018](/schnittstellen/202610/pruefi/MSCONS/PI_13018), [13019](/schnittstellen/202610/pruefi/MSCONS/PI_13019), [13025](/schnittstellen/202610/pruefi/MSCONS/PI_13025), [19102](/schnittstellen/202610/pruefi/ORDRSP/PI_19102) | `POST /createProcessData` nach 13002, 13008, 13009, 13016, 13017, 13018, 13019, 13025; `POST /updateProcessData` (abgeleitet) nach 19102 |

Dieses Ereignis löst Schritte in diesen Rollensichten aus:

| Prozess | Beteiligter | Regelwerk | Sparte |
|---|---|---|---|
| [Geschäftsdatenanfrage](/prozessdoku/202610/LF/GPKE-Teil4-geschaeftsdatenanfrage) | LF | GPKE Teil 4 | Strom |
| [Geschäftsdatenanfrage vom LF an NB](/prozessdoku/202610/LF/geli-gas-2-0-geschaftsdatenanfrage-vom-lf-an-nb) | LF | GeLi Gas 2.0 | Gas |

## Transaktionsdaten

Der Umschlag der Nachricht. Pflichtfelder müssen beim Trigger-Aufruf gesetzt sein.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| [kategorie](/bo4e/202610/cdoc/Transaktionsdaten#kategorie) | string | **ja** | Qualifier aus dem Beginn der EDIFact Nachricht / BGM |
| [sparte](/bo4e/202610/cdoc/Transaktionsdaten#sparte) | [Enum Sparte](/bo4e/202610/enum/Sparte) | **ja** | Enthält Informationen über die Sparte Werte: `STROM`, `GAS`, `FERNWAERME`, `NAHWAERME`, `WASSER`, `ABWASSER` |
| `pruefidentifikator` | — | nein | Wird dynamisch im Event-Prozess ermittelt. Ein vom Sender mitgegebener Wert wird ignoriert. Im Topic mögliche Prüfis — 17102. Mögliche Werte: `17102` |
| [absender › rollencodenummer](/bo4e/202610/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |
| [empfaenger › rollencodenummer](/bo4e/202610/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |

## Zusatzdaten

`eventname` ist auf **START_ANFRAGE_MESSWERTE** festgelegt. Dieser Wert bleibt auch in der englischen Fassung deutsch, weil Camunda darüber korreliert.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `prozessId` | string | **ja** | — |
| `eventname` | const `START_ANFRAGE_MESSWERTE` | **ja** | — |

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
