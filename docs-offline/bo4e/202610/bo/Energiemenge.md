# Energiemenge
<span hidden data-pagefind-meta={"title:Energiemenge — BO4E-Geschäftsobjekt (FV 202610)"} />

BO4E-Geschäftsobjekt · 12 Felder · 41 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="botyp"></a>`boTyp` <span className="hbs-pflicht">\*</span> | [Enum BOTyp](/bo4e/202610/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> | Typ des BO |
| <a id="versionstruktur"></a>`versionStruktur` <span className="hbs-pflicht">\*</span> | string | versionStruktur |
| <a id="lokationsid"></a>`lokationsId` | string | Eindeutige Nummer der Marktlokation bzw. der Messlokation, zu der die Energiemenge gehört |
| <a id="lokationstyp"></a>`lokationsTyp` | [Enum Lokationstyp](/bo4e/202610/enum/Lokationstyp)<br/><Werte>`MALO`, `MELO`, `NELO`, `TECHNISCHE_RESSOURCE`, `STEUERBARE_RESSOURCE`, `TRANCHE`, `MABIS_ZAEHLPUNKT`</Werte> | Gibt an, ob es sich um eine Markt- oder Messlokation handelt. |
| <a id="fertigstellungsdatum"></a>`fertigstellungsdatum` | string (date-time) | fertigstellungsdatum |
| <a id="startdatum"></a>`startdatum` | string (date-time) | Gibt Tag und Uhrzeit (falls vorhanden) an, wann der Zeitraum startet. |
| <a id="enddatum"></a>`enddatum` | string (date-time) | Gibt Tag und Uhrzeit (falls vorhanden) an, wann der Zeitraum endet. |
| <a id="bilanzierungsdatum"></a>`bilanzierungsdatum` | string (date-time) | bilanzierungsdatum |
| <a id="beginndatum"></a>`beginndatum` | string (date-time) | beginndatum |
| <a id="referenzstammdatenmeldungmsb"></a>`referenzStammdatenmeldungMsb` | string | referenzStammdatenmeldungMsb |
| <a id="konfiguration"></a>`konfiguration` | string | konfiguration |
| <a id="energieverbrauch"></a>`energieverbrauch` | [Verbrauch[]](/bo4e/202610/com/Verbrauch) | Gibt den Verbrauch in einer Zeiteinheit an. |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[boTyp](/bo4e/202610/bo/Energiemenge#botyp) <span className="hbs-pflicht">\*</span></span> | Typ des BO | [Enum BOTyp](/bo4e/202610/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> |
| <span className="hbs-f hbs-e0">[versionStruktur](/bo4e/202610/bo/Energiemenge#versionstruktur) <span className="hbs-pflicht">\*</span></span> | versionStruktur | string |
| <span className="hbs-f hbs-e0">[lokationsId](/bo4e/202610/bo/Energiemenge#lokationsid)</span> | Eindeutige Nummer der Marktlokation bzw. der Messlokation, zu der die Energiemenge gehört | string |
| <span className="hbs-f hbs-e0">[lokationsTyp](/bo4e/202610/bo/Energiemenge#lokationstyp)</span> | Gibt an, ob es sich um eine Markt- oder Messlokation handelt. | [Enum Lokationstyp](/bo4e/202610/enum/Lokationstyp)<br/><Werte>`MALO`, `MELO`, `NELO`, `TECHNISCHE_RESSOURCE`, `STEUERBARE_RESSOURCE`, `TRANCHE`, `MABIS_ZAEHLPUNKT`</Werte> |
| <span className="hbs-f hbs-e0">[fertigstellungsdatum](/bo4e/202610/bo/Energiemenge#fertigstellungsdatum)</span> | fertigstellungsdatum | string (date-time) |
| <span className="hbs-f hbs-e0">[startdatum](/bo4e/202610/bo/Energiemenge#startdatum)</span> | Gibt Tag und Uhrzeit (falls vorhanden) an, wann der Zeitraum startet. | string (date-time) |
| <span className="hbs-f hbs-e0">[enddatum](/bo4e/202610/bo/Energiemenge#enddatum)</span> | Gibt Tag und Uhrzeit (falls vorhanden) an, wann der Zeitraum endet. | string (date-time) |
| <span className="hbs-f hbs-e0">[bilanzierungsdatum](/bo4e/202610/bo/Energiemenge#bilanzierungsdatum)</span> | bilanzierungsdatum | string (date-time) |
| <span className="hbs-f hbs-e0">[beginndatum](/bo4e/202610/bo/Energiemenge#beginndatum)</span> | beginndatum | string (date-time) |
| <span className="hbs-f hbs-e0">[referenzStammdatenmeldungMsb](/bo4e/202610/bo/Energiemenge#referenzstammdatenmeldungmsb)</span> | referenzStammdatenmeldungMsb | string |
| <span className="hbs-f hbs-e0">[konfiguration](/bo4e/202610/bo/Energiemenge#konfiguration)</span> | konfiguration | string |
| <span className="hbs-g hbs-e0">[energieverbrauch](/bo4e/202610/bo/Energiemenge#energieverbrauch) <span className="hbs-liste">[ ]</span></span> | Gibt den Verbrauch in einer Zeiteinheit an. | [Verbrauch[]](/bo4e/202610/com/Verbrauch) |
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

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### lokationsId

13 Verwendung(en) in den Nachrichtentypen MSCONS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_13002](/schnittstellen/202610/pruefi/MSCONS/PI_13002) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE |
| [PI_13003](/schnittstellen/202610/pruefi/MSCONS/PI_13003) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE |
| [PI_13007](/schnittstellen/202610/pruefi/MSCONS/PI_13007) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE |
| [PI_13008](/schnittstellen/202610/pruefi/MSCONS/PI_13008) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE |
| [PI_13009](/schnittstellen/202610/pruefi/MSCONS/PI_13009) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE |
| [PI_13015](/schnittstellen/202610/pruefi/MSCONS/PI_13015) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE |
| [PI_13016](/schnittstellen/202610/pruefi/MSCONS/PI_13016) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE |
| [PI_13017](/schnittstellen/202610/pruefi/MSCONS/PI_13017) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE |
| [PI_13018](/schnittstellen/202610/pruefi/MSCONS/PI_13018) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE |
| [PI_13019](/schnittstellen/202610/pruefi/MSCONS/PI_13019) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE |
| [PI_13025](/schnittstellen/202610/pruefi/MSCONS/PI_13025) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE |
| [PI_13027](/schnittstellen/202610/pruefi/MSCONS/PI_13027) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE |
| [PI_13028](/schnittstellen/202610/pruefi/MSCONS/PI_13028) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE |

### fertigstellungsdatum

4 Verwendung(en) in den Nachrichtentypen MSCONS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_13003](/schnittstellen/202610/pruefi/MSCONS/PI_13003) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE |
| [PI_13007](/schnittstellen/202610/pruefi/MSCONS/PI_13007) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE |
| [PI_13010](/schnittstellen/202610/pruefi/MSCONS/PI_13010) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE |
| [PI_13011](/schnittstellen/202610/pruefi/MSCONS/PI_13011) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE |

### startdatum

4 Verwendung(en) in den Nachrichtentypen MSCONS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_13007](/schnittstellen/202610/pruefi/MSCONS/PI_13007) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE |
| [PI_13008](/schnittstellen/202610/pruefi/MSCONS/PI_13008) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE |
| [PI_13018](/schnittstellen/202610/pruefi/MSCONS/PI_13018) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE |
| [PI_13025](/schnittstellen/202610/pruefi/MSCONS/PI_13025) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE |

### enddatum

4 Verwendung(en) in den Nachrichtentypen MSCONS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_13007](/schnittstellen/202610/pruefi/MSCONS/PI_13007) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE |
| [PI_13008](/schnittstellen/202610/pruefi/MSCONS/PI_13008) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE |
| [PI_13018](/schnittstellen/202610/pruefi/MSCONS/PI_13018) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE |
| [PI_13025](/schnittstellen/202610/pruefi/MSCONS/PI_13025) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE |

### bilanzierungsdatum

1 Verwendung(en) in den Nachrichtentypen MSCONS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_13003](/schnittstellen/202610/pruefi/MSCONS/PI_13003) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE |

### beginndatum

1 Verwendung(en) in den Nachrichtentypen MSCONS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_13011](/schnittstellen/202610/pruefi/MSCONS/PI_13011) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE |

### referenzStammdatenmeldungMsb

1 Verwendung(en) in den Nachrichtentypen MSCONS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_13002](/schnittstellen/202610/pruefi/MSCONS/PI_13002) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE |

### konfiguration

13 Verwendung(en) in den Nachrichtentypen MSCONS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_13002](/schnittstellen/202610/pruefi/MSCONS/PI_13002) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE |
| [PI_13003](/schnittstellen/202610/pruefi/MSCONS/PI_13003) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE |
| [PI_13007](/schnittstellen/202610/pruefi/MSCONS/PI_13007) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE |
| [PI_13008](/schnittstellen/202610/pruefi/MSCONS/PI_13008) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE |
| [PI_13009](/schnittstellen/202610/pruefi/MSCONS/PI_13009) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE |
| [PI_13015](/schnittstellen/202610/pruefi/MSCONS/PI_13015) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE |
| [PI_13016](/schnittstellen/202610/pruefi/MSCONS/PI_13016) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE |
| [PI_13017](/schnittstellen/202610/pruefi/MSCONS/PI_13017) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE |
| [PI_13018](/schnittstellen/202610/pruefi/MSCONS/PI_13018) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE |
| [PI_13019](/schnittstellen/202610/pruefi/MSCONS/PI_13019) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE |
| [PI_13025](/schnittstellen/202610/pruefi/MSCONS/PI_13025) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE |
| [PI_13027](/schnittstellen/202610/pruefi/MSCONS/PI_13027) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE |
| [PI_13028](/schnittstellen/202610/pruefi/MSCONS/PI_13028) | Prüfi | MSCONS | stammdaten › ENERGIEMENGE |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
