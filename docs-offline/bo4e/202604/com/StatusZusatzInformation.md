# StatusZusatzInformation
<span hidden data-pagefind-meta={"title:StatusZusatzInformation — BO4E-Komponente (FV 202604)"} />

BO4E-Komponente · 2 Felder · 20 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="art"></a>`art` | [Enum StatusArt](/bo4e/202604/enum/StatusArt)<br/><Werte>`PLAUSIBILISIERUNGSHINWEIS`, `ERSATZWERTBILDUNGSVERFAHREN`, `KORREKTURGRUND`, `GRUND_ERSATZWERTBILDUNGSVERFAHREN`, `GASQUALITAET`, `MESSKLASSIFIZIERUNG`</Werte> | StatusArt |
| <a id="status"></a>`status` | [Enum Status](/bo4e/202604/enum/Status)<br/><Werte>`KUNDENSELBSTABLESUNG`, `LEERSTAND`, `REALER_ZAEHLERUEBERLAUF_GEPRUEFT`, `PLAUSIBEL_WG_KONTROLLABLESUNG`, `PLAUSIBEL_WG_KUNDENHINWEIS`, `AUSTAUSCH_DES_ERSATZWERTES`, `RECHENWERT`, `BASIS_MME`, `VERGLEICHSMESSUNG_GEEICHT`, `VERGLEICHSMESSUNG_NICHT_GEEICHT`, `MESSWERTNACHBILDUNG_AUS_GEEICHTEN_WERTEN`, `MESSWERTNACHBILDUNG_AUS_NICHT_GEEICHTEN_WERTEN`, `INTERPOLATION`, `HALTEWERT`, `BILANZIERUNG_NETZABSCHNITT`, `HISTORISCHE_MESSWERTE`, `STATISTISCHE_METHODE`, `AUFTEILUNG`, `VERWENDUNG_VON_WERTEN_DES_STOERMENGENZAEHLWERKS`, `UMGANGS_UND_KORREKTURMENGEN`, `ANGABEN_MESSLOKATION`, `KEIN_ZUGANG`, `KOMMUNIKATIONSSTOERUNG`, `NETZAUSFALL`, `SPANNUNGSAUSFALL`, `STATUS_GERAETEWECHSEL`, `KALIBRIERUNG`, `GERAET_ARBEITET_AUSSERHALB_DER_BETRIEBSBEDINGUNGEN`, `MESSEINRICHTUNG_GESTOERT_DEFEKT`, `UNSICHERHEIT_MESSUNG`, `BERUECKSICHTIGUNG_STOERMENGENZAEHLWERK`, `MENGENUMWERTUNG_VOLLSTAENDIG`, `UHRZEIT_GESTELLT_SYNCHRONISATION`, `MESSWERT_UNPLAUSIBEL`, `FALSCHER_WANDLERFAKTOR`, `FEHLERHAFTE_ABLESUNG`, `AENDERUNG_DER_BERECHNUNG`, `UMBAU_DER_MESSLOKATION`, `DATENBEARBEITUNGSFEHLER`, `BRENNWERTKORREKTUR`, `Z_ZAHL_KORREKTUR`, `STOERUNG_DEFEKT_MESSEINRICHTUNG`, `AENDERUNG_TARIFSCHALTZEITEN`, `TARIFSCHALTGERAET_DEFEKT`, `IMPULSWERTIGKEIT_NICHT_AUSREICHEND`, `ENERGIEMENGE_IN_UNGEMESSENEM_ZEITINTERVALL`, `ENERGIEMENGE_AUS_DEM_UNGEPAIRTEN_ZEITINTERVALL`, `WARTUNGSARBEITEN_AN_GEEICHTEM_MESSGERAET`, `GESTOERTE_WERTE`, `WARTUNGSARBEITEN_AN_EICHRECHTSKONFORMEN_MESSGERAETEN`, `KONSISTENZ_UND_SYNCHRONPRUEFUNG`, `GRUND_ANGABEN_MESSLOKATION`, `ANFORDERUNG_IN_DIE_VERGANGENHEIT_ZUM_ANGEFORDERTEN_ZEITPUNKT_LIEGT_KEIN_WERT_VOR`, `UMSTELLUNG_GASQUALITAET`, `ZAEHLERSTAND_ZUM_BEGINN_DER_ANGEGEBENEN_ENERGIEMENGE_VORHANDEN_UND_KOMMUNIZIERT`, `ZAEHLERSTAND_ZUM_ENDE_DER_ANGEGEBENEN_ENERGIEMENGE_VORHANDEN_UND_KOMMUNIZIERT`, `ZAEHLERSTAND_ZUM_BEGINN_DER_ANGEGEBENEN_ENERGIEMENGE_NICHT_VORHANDEN_DA_MENGENABGRENZUNG`, `ZAEHLERSTAND_ZUM_ENDE_DER_ANGEGEBENEN_ENERGIEMENGE_NICHT_VORHANDEN_DA_MENGENABGRENZUNG`, `GESCHEITERT`, `AUSGEBAUT`</Werte> | Status |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[art](/bo4e/202604/com/StatusZusatzInformation#art)</span> | StatusArt | [Enum StatusArt](/bo4e/202604/enum/StatusArt)<br/><Werte>`PLAUSIBILISIERUNGSHINWEIS`, `ERSATZWERTBILDUNGSVERFAHREN`, `KORREKTURGRUND`, `GRUND_ERSATZWERTBILDUNGSVERFAHREN`, `GASQUALITAET`, `MESSKLASSIFIZIERUNG`</Werte> |
| <span className="hbs-f hbs-e0">[status](/bo4e/202604/com/StatusZusatzInformation#status)</span> | Status | [Enum Status](/bo4e/202604/enum/Status)<br/><Werte>`KUNDENSELBSTABLESUNG`, `LEERSTAND`, `REALER_ZAEHLERUEBERLAUF_GEPRUEFT`, `PLAUSIBEL_WG_KONTROLLABLESUNG`, `PLAUSIBEL_WG_KUNDENHINWEIS`, `AUSTAUSCH_DES_ERSATZWERTES`, `RECHENWERT`, `BASIS_MME`, `VERGLEICHSMESSUNG_GEEICHT`, `VERGLEICHSMESSUNG_NICHT_GEEICHT`, `MESSWERTNACHBILDUNG_AUS_GEEICHTEN_WERTEN`, `MESSWERTNACHBILDUNG_AUS_NICHT_GEEICHTEN_WERTEN`, `INTERPOLATION`, `HALTEWERT`, `BILANZIERUNG_NETZABSCHNITT`, `HISTORISCHE_MESSWERTE`, `STATISTISCHE_METHODE`, `AUFTEILUNG`, `VERWENDUNG_VON_WERTEN_DES_STOERMENGENZAEHLWERKS`, `UMGANGS_UND_KORREKTURMENGEN`, `ANGABEN_MESSLOKATION`, `KEIN_ZUGANG`, `KOMMUNIKATIONSSTOERUNG`, `NETZAUSFALL`, `SPANNUNGSAUSFALL`, `STATUS_GERAETEWECHSEL`, `KALIBRIERUNG`, `GERAET_ARBEITET_AUSSERHALB_DER_BETRIEBSBEDINGUNGEN`, `MESSEINRICHTUNG_GESTOERT_DEFEKT`, `UNSICHERHEIT_MESSUNG`, `BERUECKSICHTIGUNG_STOERMENGENZAEHLWERK`, `MENGENUMWERTUNG_VOLLSTAENDIG`, `UHRZEIT_GESTELLT_SYNCHRONISATION`, `MESSWERT_UNPLAUSIBEL`, `FALSCHER_WANDLERFAKTOR`, `FEHLERHAFTE_ABLESUNG`, `AENDERUNG_DER_BERECHNUNG`, `UMBAU_DER_MESSLOKATION`, `DATENBEARBEITUNGSFEHLER`, `BRENNWERTKORREKTUR`, `Z_ZAHL_KORREKTUR`, `STOERUNG_DEFEKT_MESSEINRICHTUNG`, `AENDERUNG_TARIFSCHALTZEITEN`, `TARIFSCHALTGERAET_DEFEKT`, `IMPULSWERTIGKEIT_NICHT_AUSREICHEND`, `ENERGIEMENGE_IN_UNGEMESSENEM_ZEITINTERVALL`, `ENERGIEMENGE_AUS_DEM_UNGEPAIRTEN_ZEITINTERVALL`, `WARTUNGSARBEITEN_AN_GEEICHTEM_MESSGERAET`, `GESTOERTE_WERTE`, `WARTUNGSARBEITEN_AN_EICHRECHTSKONFORMEN_MESSGERAETEN`, `KONSISTENZ_UND_SYNCHRONPRUEFUNG`, `GRUND_ANGABEN_MESSLOKATION`, `ANFORDERUNG_IN_DIE_VERGANGENHEIT_ZUM_ANGEFORDERTEN_ZEITPUNKT_LIEGT_KEIN_WERT_VOR`, `UMSTELLUNG_GASQUALITAET`, `ZAEHLERSTAND_ZUM_BEGINN_DER_ANGEGEBENEN_ENERGIEMENGE_VORHANDEN_UND_KOMMUNIZIERT`, `ZAEHLERSTAND_ZUM_ENDE_DER_ANGEGEBENEN_ENERGIEMENGE_VORHANDEN_UND_KOMMUNIZIERT`, `ZAEHLERSTAND_ZUM_BEGINN_DER_ANGEGEBENEN_ENERGIEMENGE_NICHT_VORHANDEN_DA_MENGENABGRENZUNG`, `ZAEHLERSTAND_ZUM_ENDE_DER_ANGEGEBENEN_ENERGIEMENGE_NICHT_VORHANDEN_DA_MENGENABGRENZUNG`, `GESCHEITERT`, `AUSGEBAUT`</Werte> |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### art

10 Verwendung(en) in den Nachrichtentypen MSCONS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_13002](/schnittstellen/202604/pruefi/MSCONS/PI_13002) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch › statuszusatzinformationen |
| [PI_13007](/schnittstellen/202604/pruefi/MSCONS/PI_13007) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch › statuszusatzinformationen |
| [PI_13008](/schnittstellen/202604/pruefi/MSCONS/PI_13008) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch › statuszusatzinformationen |
| [PI_13009](/schnittstellen/202604/pruefi/MSCONS/PI_13009) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch › statuszusatzinformationen |
| [PI_13015](/schnittstellen/202604/pruefi/MSCONS/PI_13015) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch › statuszusatzinformationen |
| [PI_13016](/schnittstellen/202604/pruefi/MSCONS/PI_13016) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch › statuszusatzinformationen |
| [PI_13017](/schnittstellen/202604/pruefi/MSCONS/PI_13017) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch › statuszusatzinformationen |
| [PI_13018](/schnittstellen/202604/pruefi/MSCONS/PI_13018) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch › statuszusatzinformationen |
| [PI_13019](/schnittstellen/202604/pruefi/MSCONS/PI_13019) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch › statuszusatzinformationen |
| [PI_13025](/schnittstellen/202604/pruefi/MSCONS/PI_13025) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch › statuszusatzinformationen |

### status

10 Verwendung(en) in den Nachrichtentypen MSCONS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_13002](/schnittstellen/202604/pruefi/MSCONS/PI_13002) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch › statuszusatzinformationen |
| [PI_13007](/schnittstellen/202604/pruefi/MSCONS/PI_13007) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch › statuszusatzinformationen |
| [PI_13008](/schnittstellen/202604/pruefi/MSCONS/PI_13008) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch › statuszusatzinformationen |
| [PI_13009](/schnittstellen/202604/pruefi/MSCONS/PI_13009) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch › statuszusatzinformationen |
| [PI_13015](/schnittstellen/202604/pruefi/MSCONS/PI_13015) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch › statuszusatzinformationen |
| [PI_13016](/schnittstellen/202604/pruefi/MSCONS/PI_13016) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch › statuszusatzinformationen |
| [PI_13017](/schnittstellen/202604/pruefi/MSCONS/PI_13017) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch › statuszusatzinformationen |
| [PI_13018](/schnittstellen/202604/pruefi/MSCONS/PI_13018) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch › statuszusatzinformationen |
| [PI_13019](/schnittstellen/202604/pruefi/MSCONS/PI_13019) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch › statuszusatzinformationen |
| [PI_13025](/schnittstellen/202604/pruefi/MSCONS/PI_13025) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch › statuszusatzinformationen |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
