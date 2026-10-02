# Verbrauch
<span hidden data-pagefind-meta={"title:Verbrauch — BO4E-Komponente (FV 202610)"} />

BO4E-Komponente · 15 Felder · 96 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="startdatum"></a>`startdatum` | string (date-time) | startdatum |
| <a id="enddatum"></a>`enddatum` | string (date-time) | enddatum |
| <a id="wertermittlungsverfahren"></a>`wertermittlungsverfahren` | [Enum Wertermittlungsverfahren](/bo4e/202610/enum/Wertermittlungsverfahren)<br/><Werte>`PROGNOSE`, `MESSUNG`</Werte> | Wertermittlungsverfahren |
| <a id="messwertstatus"></a>`messwertstatus` | [Enum Messwertstatus](/bo4e/202610/enum/Messwertstatus)<br/><Werte>`ABGELESEN`, `ERSATZWERT`, `VORSCHLAGSWERT`, `NICHT_VERWENDBAR`, `PROGNOSEWERT`, `ENERGIEMENGESUMMIERT`, `VOLAEUFIGERWERT`, `FEHLT`, `ANGABE_FUER_LIEFERSCHEIN`, `GRUNDLAGE_POG_ERMITTLUNG`</Werte> | Der Status eines Zählerstandes |
| <a id="obiskennzahl"></a>`obiskennzahl` | string | obiskennzahl |
| <a id="wert"></a>`wert` | number (float) | wert |
| <a id="einheit"></a>`einheit` | [Enum Mengeneinheit](/bo4e/202610/enum/Mengeneinheit)<br/><Werte>`W`, `WH`, `KW`, `KWH`, `KVARH`, `MW`, `MWH`, `STUECK`, `KUBIKMETER`, `STUNDE`, `TAG`, `MONAT`, `JAHR`, `PROZENT`, `ANZAHL`, `VAR`, `KVAR`, `VARH`, `KWHK`, `Z16`, `KWT`, `WATT_PRO_QUADRATMETER`, `METER_PRO_SEKUNDE`</Werte> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können |
| <a id="type"></a>`type` | [Enum Verbrauchsmengetyp](/bo4e/202610/enum/Verbrauchsmengetyp)<br/><Werte>`ARBEITLEISTUNGTAGESPARAMETERABHMALO`, `VERANSCHLAGTEJAHRESMENGE`, `TUMKUNDENWERT`</Werte> | Verbrauchsmengetyp |
| <a id="tarifstufe"></a>`tarifstufe` | [Enum Tarifstufe](/bo4e/202610/enum/Tarifstufe)<br/><Werte>`TARIFSTUFE_0`, `TARIFSTUFE_1`, `TARIFSTUFE_2`, `TARIFSTUFE_3`, `TARIFSTUFE_4`, `TARIFSTUFE_5`, `TARIFSTUFE_6`, `TARIFSTUFE_7`, `TARIFSTUFE_8`, `TARIFSTUFE_9`</Werte> | Tarifstufe |
| <a id="nutzungszeitpunkt"></a>`nutzungszeitpunkt` | string (date-time) | nutzungszeitpunkt |
| <a id="ausfuehrungszeitpunkt"></a>`ausfuehrungszeitpunkt` | string (date-time) | ausfuehrungszeitpunkt |
| <a id="position"></a>`position` | integer | position |
| <a id="ablesedatum"></a>`ablesedatum` | string (date-time) | ablesedatum |
| <a id="leistungsperiode"></a>`leistungsperiode` | string | leistungsperiode |
| <a id="statuszusatzinformationen"></a>`statuszusatzinformationen` | [StatusZusatzInformation[]](/bo4e/202610/com/StatusZusatzInformation) | statuszusatzinformationen |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[startdatum](/bo4e/202610/com/Verbrauch#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e0">[enddatum](/bo4e/202610/com/Verbrauch#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-f hbs-e0">[wertermittlungsverfahren](/bo4e/202610/com/Verbrauch#wertermittlungsverfahren)</span> | Wertermittlungsverfahren | [Enum Wertermittlungsverfahren](/bo4e/202610/enum/Wertermittlungsverfahren)<br/><Werte>`PROGNOSE`, `MESSUNG`</Werte> |
| <span className="hbs-f hbs-e0">[messwertstatus](/bo4e/202610/com/Verbrauch#messwertstatus)</span> | Der Status eines Zählerstandes | [Enum Messwertstatus](/bo4e/202610/enum/Messwertstatus)<br/><Werte>`ABGELESEN`, `ERSATZWERT`, `VORSCHLAGSWERT`, `NICHT_VERWENDBAR`, `PROGNOSEWERT`, `ENERGIEMENGESUMMIERT`, `VOLAEUFIGERWERT`, `FEHLT`, `ANGABE_FUER_LIEFERSCHEIN`, `GRUNDLAGE_POG_ERMITTLUNG`</Werte> |
| <span className="hbs-f hbs-e0">[obiskennzahl](/bo4e/202610/com/Verbrauch#obiskennzahl)</span> | obiskennzahl | string |
| <span className="hbs-f hbs-e0">[wert](/bo4e/202610/com/Verbrauch#wert)</span> | wert | number (float) |
| <span className="hbs-f hbs-e0">[einheit](/bo4e/202610/com/Verbrauch#einheit)</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202610/enum/Mengeneinheit)<br/><Werte>`W`, `WH`, `KW`, `KWH`, `KVARH`, `MW`, `MWH`, `STUECK`, `KUBIKMETER`, `STUNDE`, `TAG`, `MONAT`, `JAHR`, `PROZENT`, `ANZAHL`, `VAR`, `KVAR`, `VARH`, `KWHK`, `Z16`, `KWT`, `WATT_PRO_QUADRATMETER`, `METER_PRO_SEKUNDE`</Werte> |
| <span className="hbs-f hbs-e0">[type](/bo4e/202610/com/Verbrauch#type)</span> | Verbrauchsmengetyp | [Enum Verbrauchsmengetyp](/bo4e/202610/enum/Verbrauchsmengetyp)<br/><Werte>`ARBEITLEISTUNGTAGESPARAMETERABHMALO`, `VERANSCHLAGTEJAHRESMENGE`, `TUMKUNDENWERT`</Werte> |
| <span className="hbs-f hbs-e0">[tarifstufe](/bo4e/202610/com/Verbrauch#tarifstufe)</span> | Tarifstufe | [Enum Tarifstufe](/bo4e/202610/enum/Tarifstufe)<br/><Werte>`TARIFSTUFE_0`, `TARIFSTUFE_1`, `TARIFSTUFE_2`, `TARIFSTUFE_3`, `TARIFSTUFE_4`, `TARIFSTUFE_5`, `TARIFSTUFE_6`, `TARIFSTUFE_7`, `TARIFSTUFE_8`, `TARIFSTUFE_9`</Werte> |
| <span className="hbs-f hbs-e0">[nutzungszeitpunkt](/bo4e/202610/com/Verbrauch#nutzungszeitpunkt)</span> | nutzungszeitpunkt | string (date-time) |
| <span className="hbs-f hbs-e0">[ausfuehrungszeitpunkt](/bo4e/202610/com/Verbrauch#ausfuehrungszeitpunkt)</span> | ausfuehrungszeitpunkt | string (date-time) |
| <span className="hbs-f hbs-e0">[position](/bo4e/202610/com/Verbrauch#position)</span> | position | integer |
| <span className="hbs-f hbs-e0">[ablesedatum](/bo4e/202610/com/Verbrauch#ablesedatum)</span> | ablesedatum | string (date-time) |
| <span className="hbs-f hbs-e0">[leistungsperiode](/bo4e/202610/com/Verbrauch#leistungsperiode)</span> | leistungsperiode | string |
| <span className="hbs-g hbs-e0">[statuszusatzinformationen](/bo4e/202610/com/Verbrauch#statuszusatzinformationen) <span className="hbs-liste">[ ]</span></span> | statuszusatzinformationen | [StatusZusatzInformation[]](/bo4e/202610/com/StatusZusatzInformation) |
| <span className="hbs-f hbs-e1">[art](/bo4e/202610/com/StatusZusatzInformation#art)</span> | StatusArt | [Enum StatusArt](/bo4e/202610/enum/StatusArt)<br/><Werte>`PLAUSIBILISIERUNGSHINWEIS`, `ERSATZWERTBILDUNGSVERFAHREN`, `KORREKTURGRUND`, `GRUND_ERSATZWERTBILDUNGSVERFAHREN`, `GASQUALITAET`, `MESSKLASSIFIZIERUNG`</Werte> |
| <span className="hbs-f hbs-e1">[status](/bo4e/202610/com/StatusZusatzInformation#status)</span> | Status | [Enum Status](/bo4e/202610/enum/Status)<br/><Werte>`KUNDENSELBSTABLESUNG`, `LEERSTAND`, `REALER_ZAEHLERUEBERLAUF_GEPRUEFT`, `PLAUSIBEL_WG_KONTROLLABLESUNG`, `PLAUSIBEL_WG_KUNDENHINWEIS`, `AUSTAUSCH_DES_ERSATZWERTES`, `RECHENWERT`, `BASIS_MME`, `VERGLEICHSMESSUNG_GEEICHT`, `VERGLEICHSMESSUNG_NICHT_GEEICHT`, `MESSWERTNACHBILDUNG_AUS_GEEICHTEN_WERTEN`, `MESSWERTNACHBILDUNG_AUS_NICHT_GEEICHTEN_WERTEN`, `INTERPOLATION`, `HALTEWERT`, `BILANZIERUNG_NETZABSCHNITT`, `HISTORISCHE_MESSWERTE`, `STATISTISCHE_METHODE`, `AUFTEILUNG`, `VERWENDUNG_VON_WERTEN_DES_STOERMENGENZAEHLWERKS`, `UMGANGS_UND_KORREKTURMENGEN`, `ANGABEN_MESSLOKATION`, `KEIN_ZUGANG`, `KOMMUNIKATIONSSTOERUNG`, `NETZAUSFALL`, `SPANNUNGSAUSFALL`, `STATUS_GERAETEWECHSEL`, `KALIBRIERUNG`, `GERAET_ARBEITET_AUSSERHALB_DER_BETRIEBSBEDINGUNGEN`, `MESSEINRICHTUNG_GESTOERT_DEFEKT`, `UNSICHERHEIT_MESSUNG`, `BERUECKSICHTIGUNG_STOERMENGENZAEHLWERK`, `MENGENUMWERTUNG_VOLLSTAENDIG`, `UHRZEIT_GESTELLT_SYNCHRONISATION`, `MESSWERT_UNPLAUSIBEL`, `FALSCHER_WANDLERFAKTOR`, `FEHLERHAFTE_ABLESUNG`, `AENDERUNG_DER_BERECHNUNG`, `UMBAU_DER_MESSLOKATION`, `DATENBEARBEITUNGSFEHLER`, `BRENNWERTKORREKTUR`, `Z_ZAHL_KORREKTUR`, `STOERUNG_DEFEKT_MESSEINRICHTUNG`, `AENDERUNG_TARIFSCHALTZEITEN`, `TARIFSCHALTGERAET_DEFEKT`, `IMPULSWERTIGKEIT_NICHT_AUSREICHEND`, `ENERGIEMENGE_IN_UNGEMESSENEM_ZEITINTERVALL`, `ENERGIEMENGE_AUS_DEM_UNGEPAIRTEN_ZEITINTERVALL`, `WARTUNGSARBEITEN_AN_GEEICHTEM_MESSGERAET`, `GESTOERTE_WERTE`, `WARTUNGSARBEITEN_AN_EICHRECHTSKONFORMEN_MESSGERAETEN`, `KONSISTENZ_UND_SYNCHRONPRUEFUNG`, `GRUND_ANGABEN_MESSLOKATION`, `ANFORDERUNG_IN_DIE_VERGANGENHEIT_ZUM_ANGEFORDERTEN_ZEITPUNKT_LIEGT_KEIN_WERT_VOR`, `UMSTELLUNG_GASQUALITAET`, `ZAEHLERSTAND_ZUM_BEGINN_DER_ANGEGEBENEN_ENERGIEMENGE_VORHANDEN_UND_KOMMUNIZIERT`, `ZAEHLERSTAND_ZUM_ENDE_DER_ANGEGEBENEN_ENERGIEMENGE_VORHANDEN_UND_KOMMUNIZIERT`, `ZAEHLERSTAND_ZUM_BEGINN_DER_ANGEGEBENEN_ENERGIEMENGE_NICHT_VORHANDEN_DA_MENGENABGRENZUNG`, `ZAEHLERSTAND_ZUM_ENDE_DER_ANGEGEBENEN_ENERGIEMENGE_NICHT_VORHANDEN_DA_MENGENABGRENZUNG`, `GESCHEITERT`, `AUSGEBAUT`</Werte> |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### startdatum

13 Verwendung(en) in den Nachrichtentypen MSCONS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_13002](/schnittstellen/202610/pruefi/MSCONS/PI_13002) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13003](/schnittstellen/202610/pruefi/MSCONS/PI_13003) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13007](/schnittstellen/202610/pruefi/MSCONS/PI_13007) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13008](/schnittstellen/202610/pruefi/MSCONS/PI_13008) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13009](/schnittstellen/202610/pruefi/MSCONS/PI_13009) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13010](/schnittstellen/202610/pruefi/MSCONS/PI_13010) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13015](/schnittstellen/202610/pruefi/MSCONS/PI_13015) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13016](/schnittstellen/202610/pruefi/MSCONS/PI_13016) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13018](/schnittstellen/202610/pruefi/MSCONS/PI_13018) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13019](/schnittstellen/202610/pruefi/MSCONS/PI_13019) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13025](/schnittstellen/202610/pruefi/MSCONS/PI_13025) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13027](/schnittstellen/202610/pruefi/MSCONS/PI_13027) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13028](/schnittstellen/202610/pruefi/MSCONS/PI_13028) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |

### enddatum

13 Verwendung(en) in den Nachrichtentypen MSCONS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_13002](/schnittstellen/202610/pruefi/MSCONS/PI_13002) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13003](/schnittstellen/202610/pruefi/MSCONS/PI_13003) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13007](/schnittstellen/202610/pruefi/MSCONS/PI_13007) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13008](/schnittstellen/202610/pruefi/MSCONS/PI_13008) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13009](/schnittstellen/202610/pruefi/MSCONS/PI_13009) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13010](/schnittstellen/202610/pruefi/MSCONS/PI_13010) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13015](/schnittstellen/202610/pruefi/MSCONS/PI_13015) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13016](/schnittstellen/202610/pruefi/MSCONS/PI_13016) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13018](/schnittstellen/202610/pruefi/MSCONS/PI_13018) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13019](/schnittstellen/202610/pruefi/MSCONS/PI_13019) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13025](/schnittstellen/202610/pruefi/MSCONS/PI_13025) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13027](/schnittstellen/202610/pruefi/MSCONS/PI_13027) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13028](/schnittstellen/202610/pruefi/MSCONS/PI_13028) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |

### messwertstatus

15 Verwendung(en) in den Nachrichtentypen MSCONS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_13002](/schnittstellen/202610/pruefi/MSCONS/PI_13002) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13003](/schnittstellen/202610/pruefi/MSCONS/PI_13003) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13007](/schnittstellen/202610/pruefi/MSCONS/PI_13007) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13008](/schnittstellen/202610/pruefi/MSCONS/PI_13008) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13009](/schnittstellen/202610/pruefi/MSCONS/PI_13009) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13010](/schnittstellen/202610/pruefi/MSCONS/PI_13010) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13011](/schnittstellen/202610/pruefi/MSCONS/PI_13011) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13015](/schnittstellen/202610/pruefi/MSCONS/PI_13015) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13016](/schnittstellen/202610/pruefi/MSCONS/PI_13016) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13017](/schnittstellen/202610/pruefi/MSCONS/PI_13017) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13018](/schnittstellen/202610/pruefi/MSCONS/PI_13018) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13019](/schnittstellen/202610/pruefi/MSCONS/PI_13019) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13025](/schnittstellen/202610/pruefi/MSCONS/PI_13025) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13027](/schnittstellen/202610/pruefi/MSCONS/PI_13027) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13028](/schnittstellen/202610/pruefi/MSCONS/PI_13028) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |

### obiskennzahl

15 Verwendung(en) in den Nachrichtentypen MSCONS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_13002](/schnittstellen/202610/pruefi/MSCONS/PI_13002) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13003](/schnittstellen/202610/pruefi/MSCONS/PI_13003) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13007](/schnittstellen/202610/pruefi/MSCONS/PI_13007) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13008](/schnittstellen/202610/pruefi/MSCONS/PI_13008) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13009](/schnittstellen/202610/pruefi/MSCONS/PI_13009) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13010](/schnittstellen/202610/pruefi/MSCONS/PI_13010) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13011](/schnittstellen/202610/pruefi/MSCONS/PI_13011) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13015](/schnittstellen/202610/pruefi/MSCONS/PI_13015) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13016](/schnittstellen/202610/pruefi/MSCONS/PI_13016) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13017](/schnittstellen/202610/pruefi/MSCONS/PI_13017) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13018](/schnittstellen/202610/pruefi/MSCONS/PI_13018) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13019](/schnittstellen/202610/pruefi/MSCONS/PI_13019) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13025](/schnittstellen/202610/pruefi/MSCONS/PI_13025) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13027](/schnittstellen/202610/pruefi/MSCONS/PI_13027) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13028](/schnittstellen/202610/pruefi/MSCONS/PI_13028) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |

### wert

15 Verwendung(en) in den Nachrichtentypen MSCONS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_13002](/schnittstellen/202610/pruefi/MSCONS/PI_13002) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13003](/schnittstellen/202610/pruefi/MSCONS/PI_13003) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13007](/schnittstellen/202610/pruefi/MSCONS/PI_13007) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13008](/schnittstellen/202610/pruefi/MSCONS/PI_13008) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13009](/schnittstellen/202610/pruefi/MSCONS/PI_13009) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13010](/schnittstellen/202610/pruefi/MSCONS/PI_13010) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13011](/schnittstellen/202610/pruefi/MSCONS/PI_13011) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13015](/schnittstellen/202610/pruefi/MSCONS/PI_13015) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13016](/schnittstellen/202610/pruefi/MSCONS/PI_13016) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13017](/schnittstellen/202610/pruefi/MSCONS/PI_13017) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13018](/schnittstellen/202610/pruefi/MSCONS/PI_13018) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13019](/schnittstellen/202610/pruefi/MSCONS/PI_13019) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13025](/schnittstellen/202610/pruefi/MSCONS/PI_13025) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13027](/schnittstellen/202610/pruefi/MSCONS/PI_13027) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13028](/schnittstellen/202610/pruefi/MSCONS/PI_13028) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |

### nutzungszeitpunkt

3 Verwendung(en) in den Nachrichtentypen MSCONS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_13002](/schnittstellen/202610/pruefi/MSCONS/PI_13002) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13017](/schnittstellen/202610/pruefi/MSCONS/PI_13017) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13027](/schnittstellen/202610/pruefi/MSCONS/PI_13027) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |

### ausfuehrungszeitpunkt

2 Verwendung(en) in den Nachrichtentypen MSCONS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_13002](/schnittstellen/202610/pruefi/MSCONS/PI_13002) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13017](/schnittstellen/202610/pruefi/MSCONS/PI_13017) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |

### position

15 Verwendung(en) in den Nachrichtentypen MSCONS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_13002](/schnittstellen/202610/pruefi/MSCONS/PI_13002) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13003](/schnittstellen/202610/pruefi/MSCONS/PI_13003) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13007](/schnittstellen/202610/pruefi/MSCONS/PI_13007) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13008](/schnittstellen/202610/pruefi/MSCONS/PI_13008) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13009](/schnittstellen/202610/pruefi/MSCONS/PI_13009) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13010](/schnittstellen/202610/pruefi/MSCONS/PI_13010) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13011](/schnittstellen/202610/pruefi/MSCONS/PI_13011) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13015](/schnittstellen/202610/pruefi/MSCONS/PI_13015) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13016](/schnittstellen/202610/pruefi/MSCONS/PI_13016) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13017](/schnittstellen/202610/pruefi/MSCONS/PI_13017) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13018](/schnittstellen/202610/pruefi/MSCONS/PI_13018) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13019](/schnittstellen/202610/pruefi/MSCONS/PI_13019) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13025](/schnittstellen/202610/pruefi/MSCONS/PI_13025) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13027](/schnittstellen/202610/pruefi/MSCONS/PI_13027) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13028](/schnittstellen/202610/pruefi/MSCONS/PI_13028) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |

### ablesedatum

2 Verwendung(en) in den Nachrichtentypen MSCONS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_13002](/schnittstellen/202610/pruefi/MSCONS/PI_13002) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13017](/schnittstellen/202610/pruefi/MSCONS/PI_13017) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |

### leistungsperiode

3 Verwendung(en) in den Nachrichtentypen MSCONS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_13009](/schnittstellen/202610/pruefi/MSCONS/PI_13009) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13015](/schnittstellen/202610/pruefi/MSCONS/PI_13015) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |
| [PI_13016](/schnittstellen/202610/pruefi/MSCONS/PI_13016) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE › energieverbrauch |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
