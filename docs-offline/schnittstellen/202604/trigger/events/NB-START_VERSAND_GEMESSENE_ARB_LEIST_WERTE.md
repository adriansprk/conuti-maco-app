# [NB] START_VERSAND_GEMESSENE_ARB_LEIST_WERTE
<span hidden data-pagefind-meta={"title:Trigger-Ereignis START_VERSAND_GEMESSENE_ARB_LEIST_WERTE — Marktrolle NB (FV 202604)"} />

Marktrolle **NB** · Formatversion **202604** · BO4E-Schema **1.7.8**

## Stammdaten

Unter diesem Topic ist genau einer der folgenden 1 Prüfidentifikatoren zulässig — welcher, entscheidet der Event-Prozess.

| Prüfi | Scope | Anwendungsfall | Festlegung | Kommunikation |
|---|---|---|---|---|
| [PI_13015](/schnittstellen/202604/pruefi/MSCONS/PI_13015) | MSCONS | Arbeit Leistungsmax. Kalenderjahr vor Lieferbeginn | GPKE Teil 2 | NB → LF |

Die Stammdaten der 1 Prüfidentifikatoren in **einer** Struktur — eine Spalte je Prüfidentifikator, wie im Anwendungshandbuch. Ein Wert in der Spalte heißt, dass das Feld zu diesem Prüfidentifikator gehört: **Muss**, wenn seine Spezifikation es verlangt, sonst **Kann**. Eine leere Zelle heißt »gehört nicht dazu«, nicht »unbekannt«. Vorausgewählt ist der erste; die übrigen schaltet die Leiste über der Tabelle zu.

<Handbuchsatz>

<div className="maco-tabellenrahmen">

| Struktur (BO4E) | Beschreibung | Format | <span className="hbs-p" title="Arbeit Leistungsmax. Kalenderjahr vor Lieferbeginn">13015</span> | Bedingung |
|---|---|---|---|---|
| <span className="hbs-g hbs-e0">**stammdaten**</span> | — | object | Kann | — |
| <span className="hbs-g hbs-e1">**ENERGIEMENGE** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | — |
| <span className="hbs-f hbs-e2">[konfiguration](/bo4e/202604/bo/Energiemenge#konfiguration)</span><span className="hbs-nr">00010</span> | konfiguration | string | Kann | — |
| <span className="hbs-f hbs-e2">[lokationsId](/bo4e/202604/bo/Energiemenge#lokationsid) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00020</span> | Eindeutige Nummer der Marktlokation bzw. der Messlokation, zu der die Energiemenge gehört | string | Muss | — |
| <span className="hbs-g hbs-e2">**energieverbrauch** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | — |
| <span className="hbs-f hbs-e3">[enddatum](/bo4e/202604/com/Verbrauch#enddatum)</span><span className="hbs-nr">00030</span> | enddatum | string (date-time) | Kann | — |
| <span className="hbs-f hbs-e3">[leistungsperiode](/bo4e/202604/com/Verbrauch#leistungsperiode)</span><span className="hbs-nr">00040</span> | leistungsperiode | string | Kann | — |
| <span className="hbs-f hbs-e3">[messwertstatus](/bo4e/202604/com/Verbrauch#messwertstatus) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00050</span> | Der Status eines Zählerstandes | [Enum Messwertstatus](/bo4e/202604/enum/Messwertstatus) | Muss | — |
| <span className="hbs-w hbs-e4">`ABGELESEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`ERSATZWERT`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`VORSCHLAGSWERT`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`NICHT_VERWENDBAR`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`PROGNOSEWERT`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`ENERGIEMENGESUMMIERT`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`VOLAEUFIGERWERT`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`FEHLT`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`ANGABE_FUER_LIEFERSCHEIN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`GRUNDLAGE_POG_ERMITTLUNG`</span> | — | — | Muss | — |
| <span className="hbs-f hbs-e3">[obiskennzahl](/bo4e/202604/com/Verbrauch#obiskennzahl) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00060</span> | obiskennzahl | string | Muss | — |
| <span className="hbs-f hbs-e3">[position](/bo4e/202604/com/Verbrauch#position) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00070</span> | position | integer | Muss | — |
| <span className="hbs-f hbs-e3">[startdatum](/bo4e/202604/com/Verbrauch#startdatum)</span><span className="hbs-nr">00080</span> | startdatum | string (date-time) | Kann | — |
| <span className="hbs-f hbs-e3">[wert](/bo4e/202604/com/Verbrauch#wert) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00090</span> | wert | number (float) | Muss | — |
| <span className="hbs-g hbs-e3">**statuszusatzinformationen** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-f hbs-e4">[art](/bo4e/202604/com/StatusZusatzInformation#art)</span><span className="hbs-nr">00100</span> | StatusArt | [Enum StatusArt](/bo4e/202604/enum/StatusArt) | Kann | — |
| <span className="hbs-w hbs-e5">`PLAUSIBILISIERUNGSHINWEIS`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`ERSATZWERTBILDUNGSVERFAHREN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`KORREKTURGRUND`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GRUND_ERSATZWERTBILDUNGSVERFAHREN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GASQUALITAET`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MESSKLASSIFIZIERUNG`</span> | — | — | Kann | — |
| <span className="hbs-f hbs-e4">[status](/bo4e/202604/com/StatusZusatzInformation#status)</span><span className="hbs-nr">00110</span> | Status | [Enum Status](/bo4e/202604/enum/Status) | Kann | — |
| <span className="hbs-w hbs-e5">`KUNDENSELBSTABLESUNG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`LEERSTAND`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`REALER_ZAEHLERUEBERLAUF_GEPRUEFT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`PLAUSIBEL_WG_KONTROLLABLESUNG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`PLAUSIBEL_WG_KUNDENHINWEIS`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`AUSTAUSCH_DES_ERSATZWERTES`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`RECHENWERT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`BASIS_MME`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`VERGLEICHSMESSUNG_GEEICHT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`VERGLEICHSMESSUNG_NICHT_GEEICHT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MESSWERTNACHBILDUNG_AUS_GEEICHTEN_WERTEN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MESSWERTNACHBILDUNG_AUS_NICHT_GEEICHTEN_WERTEN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`INTERPOLATION`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`HALTEWERT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`BILANZIERUNG_NETZABSCHNITT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`HISTORISCHE_MESSWERTE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`STATISTISCHE_METHODE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`AUFTEILUNG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`VERWENDUNG_VON_WERTEN_DES_STOERMENGENZAEHLWERKS`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`UMGANGS_UND_KORREKTURMENGEN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`ANGABEN_MESSLOKATION`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`KEIN_ZUGANG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`KOMMUNIKATIONSSTOERUNG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`NETZAUSFALL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`SPANNUNGSAUSFALL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`STATUS_GERAETEWECHSEL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`KALIBRIERUNG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GERAET_ARBEITET_AUSSERHALB_DER_BETRIEBSBEDINGUNGEN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MESSEINRICHTUNG_GESTOERT_DEFEKT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`UNSICHERHEIT_MESSUNG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`BERUECKSICHTIGUNG_STOERMENGENZAEHLWERK`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MENGENUMWERTUNG_VOLLSTAENDIG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`UHRZEIT_GESTELLT_SYNCHRONISATION`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MESSWERT_UNPLAUSIBEL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`FALSCHER_WANDLERFAKTOR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`FEHLERHAFTE_ABLESUNG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`AENDERUNG_DER_BERECHNUNG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`UMBAU_DER_MESSLOKATION`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`DATENBEARBEITUNGSFEHLER`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`BRENNWERTKORREKTUR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`Z_ZAHL_KORREKTUR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`STOERUNG_DEFEKT_MESSEINRICHTUNG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`AENDERUNG_TARIFSCHALTZEITEN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`TARIFSCHALTGERAET_DEFEKT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`IMPULSWERTIGKEIT_NICHT_AUSREICHEND`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`ENERGIEMENGE_IN_UNGEMESSENEM_ZEITINTERVALL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`ENERGIEMENGE_AUS_DEM_UNGEPAIRTEN_ZEITINTERVALL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`WARTUNGSARBEITEN_AN_GEEICHTEM_MESSGERAET`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GESTOERTE_WERTE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`WARTUNGSARBEITEN_AN_EICHRECHTSKONFORMEN_MESSGERAETEN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`KONSISTENZ_UND_SYNCHRONPRUEFUNG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GRUND_ANGABEN_MESSLOKATION`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`ANFORDERUNG_IN_DIE_VERGANGENHEIT_ZUM_ANGEFORDERTEN_ZEITPUNKT_LIEGT_KEIN_WERT_VOR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`UMSTELLUNG_GASQUALITAET`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`ZAEHLERSTAND_ZUM_BEGINN_DER_ANGEGEBENEN_ENERGIEMENGE_VORHANDEN_UND_KOMMUNIZIERT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`ZAEHLERSTAND_ZUM_ENDE_DER_ANGEGEBENEN_ENERGIEMENGE_VORHANDEN_UND_KOMMUNIZIERT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`ZAEHLERSTAND_ZUM_BEGINN_DER_ANGEGEBENEN_ENERGIEMENGE_NICHT_VORHANDEN_DA_MENGENABGRENZUNG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`ZAEHLERSTAND_ZUM_ENDE_DER_ANGEGEBENEN_ENERGIEMENGE_NICHT_VORHANDEN_DA_MENGENABGRENZUNG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GESCHEITERT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`AUSGEBAUT`</span> | — | — | Kann | — |

</div>

</Handbuchsatz>

## Kette dieses Auslösers

Das Ereignis löst die Nachricht aus.

| Nachricht | Antworten | Schreibaufruf nach der Antwort |
|---|---|---|
| [13015](/schnittstellen/202604/pruefi/MSCONS/PI_13015) | — | — |

Dieses Ereignis löst einen Schritt in dieser Rollensicht aus:

| Prozess | Beteiligter | Regelwerk | Sparte |
|---|---|---|---|
| [Übermittlung der bisher gemessenen Arbeits- und Leistungswerte](/prozessdoku/202604/NB/GPKE-Teil2-uebermittlung-der-bisher-gemessenen-arbeits-und-leistungswerte) | NB | GPKE Teil 2 | Strom |

## Transaktionsdaten

Der Umschlag der Nachricht. Pflichtfelder müssen beim Trigger-Aufruf gesetzt sein.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| [anfrageReferenz](/bo4e/202604/cdoc/Transaktionsdaten#anfragereferenz) | string | **ja** | Beantragungsnummer / RFF+AGI |
| [sparte](/bo4e/202604/cdoc/Transaktionsdaten#sparte) | [Enum Sparte](/bo4e/202604/enum/Sparte) | **ja** | Enthält Informationen über die Sparte Werte: `STROM`, `GAS`, `FERNWAERME`, `NAHWAERME`, `WASSER`, `ABWASSER` |
| `pruefidentifikator` | — | nein | Wird dynamisch im Event-Prozess ermittelt. Ein vom Sender mitgegebener Wert wird ignoriert. Im Topic mögliche Prüfis — 13015. Mögliche Werte: `13015` |
| [absender › rollencodenummer](/bo4e/202604/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |
| [empfaenger › rollencodenummer](/bo4e/202604/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |

## Zusatzdaten

`eventname` ist auf **START_VERSAND_GEMESSENE_ARB_LEIST_WERTE** festgelegt. Dieser Wert bleibt auch in der englischen Fassung deutsch, weil Camunda darüber korreliert.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `prozessId` | string | **ja** | — |
| `eventname` | const `START_VERSAND_GEMESSENE_ARB_LEIST_WERTE` | **ja** | — |

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
