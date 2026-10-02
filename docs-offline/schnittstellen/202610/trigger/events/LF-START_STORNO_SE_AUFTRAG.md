# [LF] START_STORNO_SE_AUFTRAG
<span hidden data-pagefind-meta={"title:Trigger-Ereignis START_STORNO_SE_AUFTRAG — Marktrolle LF (FV 202610)"} />

Marktrolle **LF** · Formatversion **202610** · BO4E-Schema **1.7.8**

## Stammdaten

Unter diesem Topic ist genau einer der folgenden 1 Prüfidentifikatoren zulässig — welcher, entscheidet der Event-Prozess.

| Prüfi | Scope | Anwendungsfall | Festlegung | Kommunikation |
|---|---|---|---|---|
| [PI_39000](/schnittstellen/202610/pruefi/ORDCHG/PI_39000) | ORDCHG | Stornierung Sperr-/Entsperrauftrag | AWH Sperrprozesse Gas | LF → NB |

Die Stammdaten der 1 Prüfidentifikatoren in **einer** Struktur — eine Spalte je Prüfidentifikator, wie im Anwendungshandbuch. Ein Wert in der Spalte heißt, dass das Feld zu diesem Prüfidentifikator gehört: **Muss**, wenn seine Spezifikation es verlangt, sonst **Kann**. Eine leere Zelle heißt »gehört nicht dazu«, nicht »unbekannt«. Vorausgewählt ist der erste; die übrigen schaltet die Leiste über der Tabelle zu.

<Handbuchsatz>

<div className="maco-tabellenrahmen">

| Struktur (BO4E) | Beschreibung | Format | <span className="hbs-p" title="Stornierung Sperr-/Entsperrauftrag">39000</span> | Bedingung |
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

</div>

</Handbuchsatz>

## Kette dieses Auslösers

Das Ereignis löst die Nachricht aus. Der Marktpartner antwortet mit einer der genannten Antworten, und danach schreibt die MACO APP den Vorgang in Ihr Backendsystem.

| Nachricht | Antworten | Schreibaufruf nach der Antwort |
|---|---|---|
| [39000](/schnittstellen/202610/pruefi/ORDCHG/PI_39000) | [19128](/schnittstellen/202610/pruefi/ORDRSP/PI_19128), [19129](/schnittstellen/202610/pruefi/ORDRSP/PI_19129) | `POST /updateProcessData` |

Dieses Ereignis löst Schritte in diesen Rollensichten aus:

| Prozess | Beteiligter | Regelwerk | Sparte |
|---|---|---|---|
| [Stornieren der Unterbrechung und Wiederherstellung der Anschlussnutzung auf Anweisung des LF](/prozessdoku/202610/LF/awh-sperrprozesse-gas-stornieren-der-unterbrechung-und-wiederherstellung-der-anschlussnutzung-auf-anweisung-des-lf) | LF | AWH Sperrprozesse Gas | Gas |
| [Stornieren der Unterbrechung und Wiederherstellung der Anschlussnutzung auf Anweisung des LF](/prozessdoku/202610/LF/GPKE-Teil2-stornieren-der-unterbrechung-und-wiederherstellung-der-anschlussnutzung-auf-anweisung-des-lf) | LF | GPKE Teil 2 | Strom |

## Transaktionsdaten

Der Umschlag der Nachricht. Pflichtfelder müssen beim Trigger-Aufruf gesetzt sein.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| [auftragsReferenz](/bo4e/202610/cdoc/Transaktionsdaten#auftragsreferenz) | string | **ja** | Auftragsnummer 'Einkauf' / RFF+ON |
| [kategorie](/bo4e/202610/cdoc/Transaktionsdaten#kategorie) | string | **ja** | Qualifier aus dem Beginn der EDIFact Nachricht / BGM |
| [sparte](/bo4e/202610/cdoc/Transaktionsdaten#sparte) | [Enum Sparte](/bo4e/202610/enum/Sparte) | **ja** | Enthält Informationen über die Sparte Werte: `STROM`, `GAS`, `FERNWAERME`, `NAHWAERME`, `WASSER`, `ABWASSER` |
| `pruefidentifikator` | — | nein | Wird dynamisch im Event-Prozess ermittelt. Ein vom Sender mitgegebener Wert wird ignoriert. Im Topic mögliche Prüfis — 39000. Mögliche Werte: `39000` |
| [absender › rollencodenummer](/bo4e/202610/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |
| [empfaenger › marktrolle](/bo4e/202610/bo/Marktteilnehmer#marktrolle) | [Enum Marktrolle](/bo4e/202610/enum/Marktrolle) | nein | Gibt im Klartext die Bezeichnung der Marktrolle an. Werte: `NB`, `LF`, `MSB`, `MSBA`, `GMSB`, `MDL`, `DL`, `BKV`, `UENB`, `KUNDE-SELBST-NN` … (+9) |
| [empfaenger › rollencodenummer](/bo4e/202610/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |

## Zusatzdaten

`eventname` ist auf **START_STORNO_SE_AUFTRAG** festgelegt. Dieser Wert bleibt auch in der englischen Fassung deutsch, weil Camunda darüber korreliert.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `prozessId` | string | **ja** | — |
| `eventname` | const `START_STORNO_SE_AUFTRAG` | **ja** | — |

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
