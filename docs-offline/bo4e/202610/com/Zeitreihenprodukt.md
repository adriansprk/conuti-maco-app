# Zeitreihenprodukt
<span hidden data-pagefind-meta={"title:Zeitreihenprodukt — BO4E-Komponente (FV 202610)"} />

BO4E-Komponente · 4 Felder · 0 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="identifikation"></a>`identifikation` | string | Identifikation des Zeitreihenprodukts, z.B. OBIS-Kennzahl |
| <a id="korrekturfaktor"></a>`korrekturfaktor` | number (float) | Gibt ggf. einen Korrekturfaktor für die Menge an. |
| <a id="energiemenge"></a>`energiemenge` | [Verbrauch](/bo4e/202610/com/Verbrauch) | Energiemenge des Zeitreihenprodukts im Bezugszeitraum |
| <a id="jahresverbrauchsprognose"></a>`jahresverbrauchsprognose` | [Menge](/bo4e/202610/com/Menge) | Jahresverbrauchsprognose |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[identifikation](/bo4e/202610/com/Zeitreihenprodukt#identifikation)</span> | Identifikation des Zeitreihenprodukts, z.B. OBIS-Kennzahl | string |
| <span className="hbs-f hbs-e0">[korrekturfaktor](/bo4e/202610/com/Zeitreihenprodukt#korrekturfaktor)</span> | Gibt ggf. einen Korrekturfaktor für die Menge an. | number (float) |
| <span className="hbs-g hbs-e0">[energiemenge](/bo4e/202610/com/Zeitreihenprodukt#energiemenge)</span> | Energiemenge des Zeitreihenprodukts im Bezugszeitraum | [Verbrauch](/bo4e/202610/com/Verbrauch) |
| <span className="hbs-f hbs-e1">[startdatum](/bo4e/202610/com/Verbrauch#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e1">[enddatum](/bo4e/202610/com/Verbrauch#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-f hbs-e1">[wertermittlungsverfahren](/bo4e/202610/com/Verbrauch#wertermittlungsverfahren)</span> | Wertermittlungsverfahren | [Enum Wertermittlungsverfahren](/bo4e/202610/enum/Wertermittlungsverfahren)<br/><Werte>`PROGNOSE`, `MESSUNG`</Werte> |
| <span className="hbs-f hbs-e1">[messwertstatus](/bo4e/202610/com/Verbrauch#messwertstatus)</span> | Der Status eines Zählerstandes | [Enum Messwertstatus](/bo4e/202610/enum/Messwertstatus)<br/><Werte>`ABGELESEN`, `ERSATZWERT`, `VORSCHLAGSWERT`, `NICHT_VERWENDBAR`, `PROGNOSEWERT`, `ENERGIEMENGESUMMIERT`, `VOLAEUFIGERWERT`, `FEHLT`, `ANGABE_FUER_LIEFERSCHEIN`, `GRUNDLAGE_POG_ERMITTLUNG`</Werte> |
| <span className="hbs-f hbs-e1">[obiskennzahl](/bo4e/202610/com/Verbrauch#obiskennzahl)</span> | obiskennzahl | string |
| <span className="hbs-f hbs-e1">[wert](/bo4e/202610/com/Verbrauch#wert)</span> | wert | number (float) |
| <span className="hbs-f hbs-e1">[einheit](/bo4e/202610/com/Verbrauch#einheit)</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202610/enum/Mengeneinheit)<br/><Werte>`W`, `WH`, `KW`, `KWH`, `KVARH`, `MW`, `MWH`, `STUECK`, `KUBIKMETER`, `STUNDE`, `TAG`, `MONAT`, `JAHR`, `PROZENT`, `ANZAHL`, `VAR`, `KVAR`, `VARH`, `KWHK`, `Z16`, `KWT`, `WATT_PRO_QUADRATMETER`, `METER_PRO_SEKUNDE`</Werte> |
| <span className="hbs-f hbs-e1">[type](/bo4e/202610/com/Verbrauch#type)</span> | Verbrauchsmengetyp | [Enum Verbrauchsmengetyp](/bo4e/202610/enum/Verbrauchsmengetyp)<br/><Werte>`ARBEITLEISTUNGTAGESPARAMETERABHMALO`, `VERANSCHLAGTEJAHRESMENGE`, `TUMKUNDENWERT`</Werte> |
| <span className="hbs-f hbs-e1">[tarifstufe](/bo4e/202610/com/Verbrauch#tarifstufe)</span> | Tarifstufe | [Enum Tarifstufe](/bo4e/202610/enum/Tarifstufe)<br/><Werte>`TARIFSTUFE_0`, `TARIFSTUFE_1`, `TARIFSTUFE_2`, `TARIFSTUFE_3`, `TARIFSTUFE_4`, `TARIFSTUFE_5`, `TARIFSTUFE_6`, `TARIFSTUFE_7`, `TARIFSTUFE_8`, `TARIFSTUFE_9`</Werte> |
| <span className="hbs-f hbs-e1">[nutzungszeitpunkt](/bo4e/202610/com/Verbrauch#nutzungszeitpunkt)</span> | nutzungszeitpunkt | string (date-time) |
| <span className="hbs-f hbs-e1">[ausfuehrungszeitpunkt](/bo4e/202610/com/Verbrauch#ausfuehrungszeitpunkt)</span> | ausfuehrungszeitpunkt | string (date-time) |
| <span className="hbs-f hbs-e1">[position](/bo4e/202610/com/Verbrauch#position)</span> | position | integer |
| <span className="hbs-f hbs-e1">[ablesedatum](/bo4e/202610/com/Verbrauch#ablesedatum)</span> | ablesedatum | string (date-time) |
| <span className="hbs-f hbs-e1">[leistungsperiode](/bo4e/202610/com/Verbrauch#leistungsperiode)</span> | leistungsperiode | string |
| <span className="hbs-g hbs-e1">[statuszusatzinformationen](/bo4e/202610/com/Verbrauch#statuszusatzinformationen) <span className="hbs-liste">[ ]</span></span> | statuszusatzinformationen | [StatusZusatzInformation[]](/bo4e/202610/com/StatusZusatzInformation) |
| <span className="hbs-f hbs-e2">[art](/bo4e/202610/com/StatusZusatzInformation#art)</span> | StatusArt | [Enum StatusArt](/bo4e/202610/enum/StatusArt)<br/><Werte>`PLAUSIBILISIERUNGSHINWEIS`, `ERSATZWERTBILDUNGSVERFAHREN`, `KORREKTURGRUND`, `GRUND_ERSATZWERTBILDUNGSVERFAHREN`, `GASQUALITAET`, `MESSKLASSIFIZIERUNG`</Werte> |
| <span className="hbs-f hbs-e2">[status](/bo4e/202610/com/StatusZusatzInformation#status)</span> | Status | [Enum Status](/bo4e/202610/enum/Status)<br/><Werte>`KUNDENSELBSTABLESUNG`, `LEERSTAND`, `REALER_ZAEHLERUEBERLAUF_GEPRUEFT`, `PLAUSIBEL_WG_KONTROLLABLESUNG`, `PLAUSIBEL_WG_KUNDENHINWEIS`, `AUSTAUSCH_DES_ERSATZWERTES`, `RECHENWERT`, `BASIS_MME`, `VERGLEICHSMESSUNG_GEEICHT`, `VERGLEICHSMESSUNG_NICHT_GEEICHT`, `MESSWERTNACHBILDUNG_AUS_GEEICHTEN_WERTEN`, `MESSWERTNACHBILDUNG_AUS_NICHT_GEEICHTEN_WERTEN`, `INTERPOLATION`, `HALTEWERT`, `BILANZIERUNG_NETZABSCHNITT`, `HISTORISCHE_MESSWERTE`, `STATISTISCHE_METHODE`, `AUFTEILUNG`, `VERWENDUNG_VON_WERTEN_DES_STOERMENGENZAEHLWERKS`, `UMGANGS_UND_KORREKTURMENGEN`, `ANGABEN_MESSLOKATION`, `KEIN_ZUGANG`, `KOMMUNIKATIONSSTOERUNG`, `NETZAUSFALL`, `SPANNUNGSAUSFALL`, `STATUS_GERAETEWECHSEL`, `KALIBRIERUNG`, `GERAET_ARBEITET_AUSSERHALB_DER_BETRIEBSBEDINGUNGEN`, `MESSEINRICHTUNG_GESTOERT_DEFEKT`, `UNSICHERHEIT_MESSUNG`, `BERUECKSICHTIGUNG_STOERMENGENZAEHLWERK`, `MENGENUMWERTUNG_VOLLSTAENDIG`, `UHRZEIT_GESTELLT_SYNCHRONISATION`, `MESSWERT_UNPLAUSIBEL`, `FALSCHER_WANDLERFAKTOR`, `FEHLERHAFTE_ABLESUNG`, `AENDERUNG_DER_BERECHNUNG`, `UMBAU_DER_MESSLOKATION`, `DATENBEARBEITUNGSFEHLER`, `BRENNWERTKORREKTUR`, `Z_ZAHL_KORREKTUR`, `STOERUNG_DEFEKT_MESSEINRICHTUNG`, `AENDERUNG_TARIFSCHALTZEITEN`, `TARIFSCHALTGERAET_DEFEKT`, `IMPULSWERTIGKEIT_NICHT_AUSREICHEND`, `ENERGIEMENGE_IN_UNGEMESSENEM_ZEITINTERVALL`, `ENERGIEMENGE_AUS_DEM_UNGEPAIRTEN_ZEITINTERVALL`, `WARTUNGSARBEITEN_AN_GEEICHTEM_MESSGERAET`, `GESTOERTE_WERTE`, `WARTUNGSARBEITEN_AN_EICHRECHTSKONFORMEN_MESSGERAETEN`, `KONSISTENZ_UND_SYNCHRONPRUEFUNG`, `GRUND_ANGABEN_MESSLOKATION`, `ANFORDERUNG_IN_DIE_VERGANGENHEIT_ZUM_ANGEFORDERTEN_ZEITPUNKT_LIEGT_KEIN_WERT_VOR`, `UMSTELLUNG_GASQUALITAET`, `ZAEHLERSTAND_ZUM_BEGINN_DER_ANGEGEBENEN_ENERGIEMENGE_VORHANDEN_UND_KOMMUNIZIERT`, `ZAEHLERSTAND_ZUM_ENDE_DER_ANGEGEBENEN_ENERGIEMENGE_VORHANDEN_UND_KOMMUNIZIERT`, `ZAEHLERSTAND_ZUM_BEGINN_DER_ANGEGEBENEN_ENERGIEMENGE_NICHT_VORHANDEN_DA_MENGENABGRENZUNG`, `ZAEHLERSTAND_ZUM_ENDE_DER_ANGEGEBENEN_ENERGIEMENGE_NICHT_VORHANDEN_DA_MENGENABGRENZUNG`, `GESCHEITERT`, `AUSGEBAUT`</Werte> |
| <span className="hbs-g hbs-e0">[jahresverbrauchsprognose](/bo4e/202610/com/Zeitreihenprodukt#jahresverbrauchsprognose)</span> | Jahresverbrauchsprognose | [Menge](/bo4e/202610/com/Menge) |
| <span className="hbs-f hbs-e1">[wert](/bo4e/202610/com/Menge#wert)</span> | Wert | number (float) |
| <span className="hbs-f hbs-e1">[einheit](/bo4e/202610/com/Menge#einheit)</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202610/enum/Mengeneinheit)<br/><Werte>`W`, `WH`, `KW`, `KWH`, `KVARH`, `MW`, `MWH`, `STUECK`, `KUBIKMETER`, `STUNDE`, `TAG`, `MONAT`, `JAHR`, `PROZENT`, `ANZAHL`, `VAR`, `KVAR`, `VARH`, `KWHK`, `Z16`, `KWT`, `WATT_PRO_QUADRATMETER`, `METER_PRO_SEKUNDE`</Werte> |
| <span className="hbs-f hbs-e1">[startdatum](/bo4e/202610/com/Menge#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e1">[enddatum](/bo4e/202610/com/Menge#enddatum)</span> | enddatum | string (date-time) |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

:::note{title="Keine Verwendung gefunden"}

Kein Feld dieses Objekts wird in den Prüfi- oder Event-Spezifikationen dieser Formatversion referenziert. Das Objekt gehört zum BO4E-Schema, ist in der Marktkommunikation dieser Formatversion aber nicht im Einsatz.

:::

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

</Hinweisbereich>
