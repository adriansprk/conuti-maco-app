# [LF] START_ERHEBUNG_MESSWERTE
<span hidden data-pagefind-meta={"title:Trigger-Ereignis START_ERHEBUNG_MESSWERTE — Marktrolle LF (FV 202604)"} />

Marktrolle **LF** · Formatversion **202604** · BO4E-Schema **1.7.8**

## Stammdaten

Unter diesem Topic ist genau einer der folgenden 2 Prüfidentifikatoren zulässig — welcher, entscheidet der Event-Prozess.

| Prüfi | Scope | Anwendungsfall | Festlegung | Kommunikation |
|---|---|---|---|---|
| [PI_13002](/schnittstellen/202604/pruefi/MSCONS/PI_13002) | MSCONS | Zählerstand (Gas) | WiM Gas | MSBN → NB |
| [PI_13017](/schnittstellen/202604/pruefi/MSCONS/PI_13017) | MSCONS | Zählerstand (Strom) | Prozesse zum Informationsaustausch zwischen Netzbetreiber und Herkunftsnachweis-register (HKN-R) des Umweltbundesamts (UBA) | NB → RB HKN-R |

Die Stammdaten der 2 Prüfidentifikatoren in **einer** Struktur — eine Spalte je Prüfidentifikator, wie im Anwendungshandbuch. Ein Wert in der Spalte heißt, dass das Feld zu diesem Prüfidentifikator gehört: **Muss**, wenn seine Spezifikation es verlangt, sonst **Kann**. Eine leere Zelle heißt »gehört nicht dazu«, nicht »unbekannt«. Vorausgewählt ist der erste; die übrigen schaltet die Leiste über der Tabelle zu.

<Handbuchsatz>

<div className="maco-tabellenrahmen">

| Struktur (BO4E) | Beschreibung | Format | <span className="hbs-p" title="Zählerstand (Gas)">13002</span> | <span className="hbs-p" title="Zählerstand (Strom)">13017</span> | Bedingung |
|---|---|---|---|---|---|
| <span className="hbs-g hbs-e0">**stammdaten**</span> | — | object | Kann | Kann | — |
| <span className="hbs-g hbs-e1">**ENERGIEMENGE** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | Muss | — |
| <span className="hbs-f hbs-e2">[konfiguration](/bo4e/202604/bo/Energiemenge#konfiguration)</span><span className="hbs-nr">00010</span> | konfiguration | string | Kann | Kann | — |
| <span className="hbs-f hbs-e2">[lokationsId](/bo4e/202604/bo/Energiemenge#lokationsid) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00020</span> | Eindeutige Nummer der Marktlokation bzw. der Messlokation, zu der die Energiemenge gehört | string | Muss | Muss | — |
| <span className="hbs-f hbs-e2">[referenzStammdatenmeldungMsb](/bo4e/202604/bo/Energiemenge#referenzstammdatenmeldungmsb)</span><span className="hbs-nr">00030</span> | referenzStammdatenmeldungMsb | string | Kann | — | — |
| <span className="hbs-g hbs-e2">**energieverbrauch** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | Muss | — |
| <span className="hbs-f hbs-e3">[ablesedatum](/bo4e/202604/com/Verbrauch#ablesedatum)</span><span className="hbs-nr">00040</span> | ablesedatum | string (date-time) | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[ausfuehrungszeitpunkt](/bo4e/202604/com/Verbrauch#ausfuehrungszeitpunkt)</span><span className="hbs-nr">00050</span> | ausfuehrungszeitpunkt | string (date-time) | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[enddatum](/bo4e/202604/com/Verbrauch#enddatum)</span><span className="hbs-nr">00060</span> | enddatum | string (date-time) | Kann | — | — |
| <span className="hbs-f hbs-e3">[messwertstatus](/bo4e/202604/com/Verbrauch#messwertstatus) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00070</span> | Der Status eines Zählerstandes | [Enum Messwertstatus](/bo4e/202604/enum/Messwertstatus) | Muss | Muss | — |
| <span className="hbs-w hbs-e4">`ABGELESEN`</span> | — | — | Muss | Muss | — |
| <span className="hbs-w hbs-e4">`ERSATZWERT`</span> | — | — | Muss | Muss | — |
| <span className="hbs-w hbs-e4">`VORSCHLAGSWERT`</span> | — | — | Muss | Muss | — |
| <span className="hbs-w hbs-e4">`NICHT_VERWENDBAR`</span> | — | — | Muss | Muss | — |
| <span className="hbs-w hbs-e4">`PROGNOSEWERT`</span> | — | — | Muss | Muss | — |
| <span className="hbs-w hbs-e4">`ENERGIEMENGESUMMIERT`</span> | — | — | Muss | Muss | — |
| <span className="hbs-w hbs-e4">`VOLAEUFIGERWERT`</span> | — | — | Muss | Muss | — |
| <span className="hbs-w hbs-e4">`FEHLT`</span> | — | — | Muss | Muss | — |
| <span className="hbs-w hbs-e4">`ANGABE_FUER_LIEFERSCHEIN`</span> | — | — | Muss | Muss | — |
| <span className="hbs-w hbs-e4">`GRUNDLAGE_POG_ERMITTLUNG`</span> | — | — | Muss | Muss | — |
| <span className="hbs-f hbs-e3">[nutzungszeitpunkt](/bo4e/202604/com/Verbrauch#nutzungszeitpunkt)</span><span className="hbs-nr">00080</span> | nutzungszeitpunkt | string (date-time) | Kann | Muss | — |
| <span className="hbs-f hbs-e3">[obiskennzahl](/bo4e/202604/com/Verbrauch#obiskennzahl) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00090</span> | obiskennzahl | string | Muss | Muss | — |
| <span className="hbs-f hbs-e3">[position](/bo4e/202604/com/Verbrauch#position) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00100</span> | position | integer | Muss | Muss | — |
| <span className="hbs-f hbs-e3">[startdatum](/bo4e/202604/com/Verbrauch#startdatum)</span><span className="hbs-nr">00110</span> | startdatum | string (date-time) | Kann | — | — |
| <span className="hbs-f hbs-e3">[wert](/bo4e/202604/com/Verbrauch#wert) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00120</span> | wert | number (float) | Muss | Muss | — |
| <span className="hbs-g hbs-e3">**statuszusatzinformationen** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[art](/bo4e/202604/com/StatusZusatzInformation#art)</span><span className="hbs-nr">00130</span> | StatusArt | [Enum StatusArt](/bo4e/202604/enum/StatusArt) | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`PLAUSIBILISIERUNGSHINWEIS`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`ERSATZWERTBILDUNGSVERFAHREN`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`KORREKTURGRUND`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GRUND_ERSATZWERTBILDUNGSVERFAHREN`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GASQUALITAET`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MESSKLASSIFIZIERUNG`</span> | — | — | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[status](/bo4e/202604/com/StatusZusatzInformation#status)</span><span className="hbs-nr">00140</span> | Status | [Enum Status](/bo4e/202604/enum/Status) | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`KUNDENSELBSTABLESUNG`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`LEERSTAND`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`REALER_ZAEHLERUEBERLAUF_GEPRUEFT`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`PLAUSIBEL_WG_KONTROLLABLESUNG`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`PLAUSIBEL_WG_KUNDENHINWEIS`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`AUSTAUSCH_DES_ERSATZWERTES`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`RECHENWERT`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BASIS_MME`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`VERGLEICHSMESSUNG_GEEICHT`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`VERGLEICHSMESSUNG_NICHT_GEEICHT`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MESSWERTNACHBILDUNG_AUS_GEEICHTEN_WERTEN`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MESSWERTNACHBILDUNG_AUS_NICHT_GEEICHTEN_WERTEN`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`INTERPOLATION`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`HALTEWERT`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BILANZIERUNG_NETZABSCHNITT`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`HISTORISCHE_MESSWERTE`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`STATISTISCHE_METHODE`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`AUFTEILUNG`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`VERWENDUNG_VON_WERTEN_DES_STOERMENGENZAEHLWERKS`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`UMGANGS_UND_KORREKTURMENGEN`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`ANGABEN_MESSLOKATION`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`KEIN_ZUGANG`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`KOMMUNIKATIONSSTOERUNG`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`NETZAUSFALL`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SPANNUNGSAUSFALL`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`STATUS_GERAETEWECHSEL`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`KALIBRIERUNG`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GERAET_ARBEITET_AUSSERHALB_DER_BETRIEBSBEDINGUNGEN`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MESSEINRICHTUNG_GESTOERT_DEFEKT`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`UNSICHERHEIT_MESSUNG`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BERUECKSICHTIGUNG_STOERMENGENZAEHLWERK`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MENGENUMWERTUNG_VOLLSTAENDIG`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`UHRZEIT_GESTELLT_SYNCHRONISATION`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MESSWERT_UNPLAUSIBEL`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`FALSCHER_WANDLERFAKTOR`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`FEHLERHAFTE_ABLESUNG`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`AENDERUNG_DER_BERECHNUNG`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`UMBAU_DER_MESSLOKATION`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`DATENBEARBEITUNGSFEHLER`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BRENNWERTKORREKTUR`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`Z_ZAHL_KORREKTUR`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`STOERUNG_DEFEKT_MESSEINRICHTUNG`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`AENDERUNG_TARIFSCHALTZEITEN`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`TARIFSCHALTGERAET_DEFEKT`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`IMPULSWERTIGKEIT_NICHT_AUSREICHEND`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`ENERGIEMENGE_IN_UNGEMESSENEM_ZEITINTERVALL`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`ENERGIEMENGE_AUS_DEM_UNGEPAIRTEN_ZEITINTERVALL`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`WARTUNGSARBEITEN_AN_GEEICHTEM_MESSGERAET`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GESTOERTE_WERTE`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`WARTUNGSARBEITEN_AN_EICHRECHTSKONFORMEN_MESSGERAETEN`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`KONSISTENZ_UND_SYNCHRONPRUEFUNG`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GRUND_ANGABEN_MESSLOKATION`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`ANFORDERUNG_IN_DIE_VERGANGENHEIT_ZUM_ANGEFORDERTEN_ZEITPUNKT_LIEGT_KEIN_WERT_VOR`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`UMSTELLUNG_GASQUALITAET`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`ZAEHLERSTAND_ZUM_BEGINN_DER_ANGEGEBENEN_ENERGIEMENGE_VORHANDEN_UND_KOMMUNIZIERT`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`ZAEHLERSTAND_ZUM_ENDE_DER_ANGEGEBENEN_ENERGIEMENGE_VORHANDEN_UND_KOMMUNIZIERT`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`ZAEHLERSTAND_ZUM_BEGINN_DER_ANGEGEBENEN_ENERGIEMENGE_NICHT_VORHANDEN_DA_MENGENABGRENZUNG`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`ZAEHLERSTAND_ZUM_ENDE_DER_ANGEGEBENEN_ENERGIEMENGE_NICHT_VORHANDEN_DA_MENGENABGRENZUNG`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GESCHEITERT`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`AUSGEBAUT`</span> | — | — | Kann | Kann | — |
| <span className="hbs-g hbs-e1">**ZAEHLER** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | Kann | — |
| <span className="hbs-f hbs-e2">[zaehlernummer](/bo4e/202604/bo/Zaehler#zaehlernummer) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00150</span> | Nummerierung des Zählers, vergeben durch den Messstellenbetreiber | string | Muss | Kann | — |

</div>

</Handbuchsatz>

## Kette dieses Auslösers

Das Ereignis löst die Nachricht aus.

| Nachricht | Antworten | Schreibaufruf nach der Antwort |
|---|---|---|
| [13002](/schnittstellen/202604/pruefi/MSCONS/PI_13002) | — | — |
| [13017](/schnittstellen/202604/pruefi/MSCONS/PI_13017) | — | — |

Dieses Ereignis löst Schritte in diesen Rollensichten aus:

| Prozess | Beteiligter | Regelwerk | Sparte |
|---|---|---|---|
| [Übermittlung von Werten vom LF an NB](/prozessdoku/202604/LF/awh-wim-gas-2-0-ubermittlung-von-werten-vom-lf-an-nb) | LF | AWH WiM Gas 2.0 | Gas |
| [GeLi_Gas 2.0 Kap. 4.1.1.1 Erhebung von Messwerten](/prozessdoku/202604/LF/geli-gas-2-0-geli-gas-2-0-kap-4-1-1-1-erhebung-von-messwerten) | LF | GeLi Gas 2.0 | Gas |
| [Übermittlung von Zählerständen vom LF](/prozessdoku/202604/LF/WiM-Teil2-uebermittlung-von-zaehlerstaenden-vom-lf) | LF | WiM Strom Teil 2 | Strom |

## Transaktionsdaten

Der Umschlag der Nachricht. Pflichtfelder müssen beim Trigger-Aufruf gesetzt sein.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| [anfrageReferenz](/bo4e/202604/cdoc/Transaktionsdaten#anfragereferenz) | string | **ja** | Beantragungsnummer / RFF+AGI |
| [kategorie](/bo4e/202604/cdoc/Transaktionsdaten#kategorie) | string | **ja** | Qualifier aus dem Beginn der EDIFact Nachricht / BGM |
| [sparte](/bo4e/202604/cdoc/Transaktionsdaten#sparte) | [Enum Sparte](/bo4e/202604/enum/Sparte) | **ja** | Enthält Informationen über die Sparte Werte: `STROM`, `GAS`, `FERNWAERME`, `NAHWAERME`, `WASSER`, `ABWASSER` |
| `pruefidentifikator` | — | nein | Wird dynamisch im Event-Prozess ermittelt (Entscheidungsgrundlage: sparte). Ein vom Sender mitgegebener Wert wird ignoriert. Im Topic mögliche Prüfis — 13002, 13017. Mögliche Werte: `13002`, `13017` |
| [absender › rollencodenummer](/bo4e/202604/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |
| [empfaenger › rollencodenummer](/bo4e/202604/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |

## Zusatzdaten

`eventname` ist auf **START_ERHEBUNG_MESSWERTE** festgelegt. Dieser Wert bleibt auch in der englischen Fassung deutsch, weil Camunda darüber korreliert.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `prozessId` | string | **ja** | — |
| `eventname` | const `START_ERHEBUNG_MESSWERTE` | **ja** | — |

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
