# Bilanzierung
<span hidden data-pagefind-meta={"title:Bilanzierung — BO4E-Geschäftsobjekt (FV 202604)"} />

BO4E-Geschäftsobjekt · 28 Felder · 125 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="botyp"></a>`boTyp` <span className="hbs-pflicht">\*</span> | [Enum BOTyp](/bo4e/202604/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> | Typ des BO |
| <a id="versionstruktur"></a>`versionStruktur` <span className="hbs-pflicht">\*</span> | string | versionStruktur |
| <a id="marktlokationsid"></a>`marktlokationsId` | string | Für welche Marktlokation gelten diese Bilanzierungsdaten |
| <a id="aggregationsverantwortung"></a>`aggregationsverantwortung` | [Enum Aggregationsverantwortung](/bo4e/202604/enum/Aggregationsverantwortung)<br/><Werte>`UENB`, `VNB`</Werte> | Aggregationsverantwortung |
| <a id="zeitreihentyp"></a>`zeitreihentyp` | [Enum Zeitreihentyp](/bo4e/202604/enum/Zeitreihentyp)<br/><Werte>`EGS`, `LGS`, `NZR`, `SES`, `SLS`, `TES`, `TLS`, `SLS_TLS`, `SES_TES`, `AUS`, `BAS`, `DBA`, `DZR`, `DZÜ`, `FPE`, `FPI`, `SRE`, `SRI`, `VZR`, `BIL`, `BIP`, `BIT`, `GAL`, `GAP`, `GAT`, `GEL`, `GEP`, `GET`, `SOL`, `SOP`, `SOT`, `WFL`, `WFP`, `WNL`, `WNP`, `WNT`, `WAL`, `WAP`, `WAT`, `AU1`, `BI1`, `BI2`, `BI3`, `GAA`, `GAB`, `GAC`, `GE1`, `GE2`, `GE3`, `SO1`, `SO2`, `SO3`, `WF1`, `WF2`, `WF3`, `WN1`, `WN2`, `WN3`, `WAA`, `WAB`, `WAC`, `AUSFALLARBEITSSUMME`, `BILANZKREISABWEICHUNGSSALDO`, `DIFFERENZZEITREIHE`, `DELTAZEITREIHE`, `DELTAZEITREIHENUEBERTRAG`, `FAHRPLANENTNAHMESUMME`, `FAHRPLANEINSPEISESUMME`, `UEBERFUEHRUNGSZEITREIHE_SEKUNDAERREGELLEISTUNG_EXPORT`, `UEBERFUEHRUNGSZEITREIHE_SEKUNDAERREGELLEISTUNG_IMPORT`, `VERLUSTZEITREIHE`, `EE_EINSPEISESUMME_BIOMASSE_BIOGAS_GEMESSEN`, `EE_EINSPEISESUMME_BIOMASSE_BIOGAS_EINSPEISEPROFIL`, `EE_EINSPEISESUMME_BIOMASSE_BIOGAS_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`, `EE_EINSPEISESUMME_DEPONIE_KLAER_GRUBENGAS_GEMESSEN`, `EE_EINSPEISESUMME_DEPONIE_KLAER_GRUBENGAS_EINSPEISEPROFIL`, `EE_EINSPEISESUMME_DEPONIE_KLAER_GRUBENGAS_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`, `EE_EINSPEISESUMME_GEOTHERMIE_GEMESSEN`, `EE_EINSPEISESUMME_GEOTHERMIE_EINSPEISEPROFIL`, `EE_EINSPEISESUMME_GEOTHERMIE_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`, `EE_EINSPEISESUMME_SOLAR_GEMESSEN`, `EE_EINSPEISESUMME_SOLAR_EINSPEISEPROFIL`, `EE_EINSPEISESUMME_SOLAR_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`, `EE_EINSPEISESUMME_WIND_OFFSHORE_GEMESSEN`, `EE_EINSPEISESUMME_WIND_OFFSHORE_EINSPEISEPROFIL`, `EE_EINSPEISESUMME_WIND_OFFSHORE_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`, `EE_EINSPEISESUMME_WIND_ONSHORE_GEMESSEN`, `EE_EINSPEISESUMME_WIND_ONSHORE_EINSPEISEPROFIL`, `EE_EINSPEISESUMME_WIND_ONSHORE_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`, `EE_EINSPEISESUMME_WASSERKRAFT_GEMESSEN`, `EE_EINSPEISESUMME_WASSERKRAFT_EINSPEISEPROFIL`, `EE_EINSPEISESUMME_WASSERKRAFT_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`, `EEG_UEBERFUEHRUNG_AUSFALLARBEIT`, `EEG_UEBERFUEHRUNG_BIOMASSE_BIOGAS_WERTE`, `EEG_UEBERFUEHRUNG_BIOMASSE_BIOGAS_STANDARDEINSPEISEPROFIL`, `EEG_UEBERFUEHRUNG_BIOMASSE_BIOGAS_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`, `EEG_UEBERFUEHRUNG_DEPONIE_KLAER_GRUBENGAS_WERTE`, `EEG_UEBERFUEHRUNG_DEPONIE_KLAER_GRUBENGAS_STANDARDEINSPEISEPROFIL`, `EEG_UEBERFUEHRUNG_DEPONIE_KLAER_GRUBENGAS_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`, `EEG_UEBERFUEHRUNG_GEOTHERMIE_WERTE`, `EEG_UEBERFUEHRUNG_GEOTHERMIE_STANDARDEINSPEISEPROFIL`, `EEG_UEBERFUEHRUNG_GEOTHERMIE_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`, `EEG_UEBERFUEHRUNG_SOLAR_WERTE`, `EEG_UEBERFUEHRUNG_SOLAR_STANDARDEINSPEISEPROFIL`, `EEG_UEBERFUEHRUNG_SOLAR_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`, `EEG_UEBERFUEHRUNG_WIND_OFFSHORE_WERTE`, `EEG_UEBERFUEHRUNG_WIND_OFFSHORE_STANDARDEINSPEISEPROFIL`, `EEG_UEBERFUEHRUNG_WIND_OFFSHORE_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`, `EEG_UEBERFUEHRUNG_WIND_ONSHORE_WERTE`, `EEG_UEBERFUEHRUNG_WIND_ONSHORE_STANDARDEINSPEISEPROFIL`, `EEG_UEBERFUEHRUNG_WIND_ONSHORE_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`, `EEG_UEBERFUEHRUNG_WASSERKRAFT_WERTE`, `EEG_UEBERFUEHRUNG_WASSERKRAFT_STANDARDEINSPEISEPROFIL`, `EEG_UEBERFUEHRUNG_WASSERKRAFT_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</Werte> | Zeitreihentyp |
| <a id="prognosegrundlage"></a>`prognosegrundlage` | [Enum Prognosegrundlage](/bo4e/202604/enum/Prognosegrundlage)<br/><Werte>`WERTE`, `PROFILE`</Werte> | Prognosegrundlage |
| <a id="bilanzierungsbeginn"></a>`bilanzierungsbeginn` | string (date-time) | Inklusiver Start der Bilanzierung |
| <a id="bilanzierungsende"></a>`bilanzierungsende` | string (date-time) | Exklusives Ende der Bilanzierung |
| <a id="bilanzkreis"></a>`bilanzkreis` | string | Bilanzkreis |
| <a id="bilanzkreise"></a>`bilanzkreise` | [Bilanzkreis[]](/bo4e/202604/bo/Bilanzkreis) | Bilanzkreis |
| <a id="fallgruppenzuordnung"></a>`fallgruppenzuordnung` | [Enum Fallgruppenzuordnung](/bo4e/202604/enum/Fallgruppenzuordnung)<br/><Werte>`GABI_RLMmT`, `GABI_RLMoT`, `GABI_RLMNEV`</Werte> | Fallgruppenzuordnung (für gas RLM) |
| <a id="temperaturarbeit"></a>`temperaturarbeit` | [Menge](/bo4e/202604/com/Menge) | Kundenwert TLP |
| <a id="jahresverbrauchsprognose"></a>`jahresverbrauchsprognose` | [Menge](/bo4e/202604/com/Menge) | Jahresverbrauchsprognose |
| <a id="kundenwert"></a>`kundenwert` | [Menge](/bo4e/202604/com/Menge) | Kundenwert |
| <a id="verbrauchsaufteilung"></a>`verbrauchsaufteilung` | [Menge](/bo4e/202604/com/Menge) | Verbrauchsaufteilung |
| <a id="wahlrechtprognosegrundlage"></a>`wahlrechtPrognosegrundlage` | [Enum WahlrechtPrognosegrundlage](/bo4e/202604/enum/WahlrechtPrognosegrundlage)<br/><Werte>`DURCH_LF`, `DURCH_LF_NICHT_GEGEBEN`, `NICHT_WEGEN_GROSSEN_VERBRAUCHS`, `NICHT_WEGEN_EIGENVERBRAUCH`, `NICHT_WEGEN_TAGES_VERBRAUCH`, `NICHT_WEGEN_ENWG`</Werte> | Wahlrecht der Prognosegrundlage (true = Wahlrecht beim Lieferanten vorhanden) |
| <a id="grundwahlrechtprognosegrundlage"></a>`grundWahlrechtPrognosegrundlage` | [Enum WahlrechtPrognosegrundlage](/bo4e/202604/enum/WahlrechtPrognosegrundlage)<br/><Werte>`DURCH_LF`, `DURCH_LF_NICHT_GEGEBEN`, `NICHT_WEGEN_GROSSEN_VERBRAUCHS`, `NICHT_WEGEN_EIGENVERBRAUCH`, `NICHT_WEGEN_TAGES_VERBRAUCH`, `NICHT_WEGEN_ENWG`</Werte> | Grund Wahlrecht der Prognosegrundlage (true = Wahlrecht beim Lieferanten vorhanden) |
| <a id="abwicklungsmodell"></a>`abwicklungsmodell` | [Enum Abwicklungsmodell](/bo4e/202604/enum/Abwicklungsmodell)<br/><Werte>`MODELL_1_BILANZIERUNG_AN_MARKTLOKATION`, `MODELL_2_BILANZIERUNG_IM_BILANZIERUNGSGEBIET`</Werte> | Abwicklungsmodell |
| <a id="vorjahresverbrauch"></a>`vorjahresverbrauch` | [Menge](/bo4e/202604/com/Menge) | Vorjahresverbrauch |
| <a id="datenqualitaet"></a>`datenqualitaet` | [Enum Datenqualitaet](/bo4e/202604/enum/Datenqualitaet)<br/><Werte>`ERWARTETE_DATEN`, `IM_SYSTEM_VORHANDENE_DATEN`, `INFORMATIVE_DATEN`, `GUELTIGE_DATEN`, `KEINE_DATEN`, `IM_SYSTEM_KEINE_DATEN_VORHANDEN`, `KEINE_DATEN_ERWARTET`, `DIFFERENZ_DATEN`, `DIFFERENZ_ERWARTETE_DATEN`, `DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</Werte> | Datenqualität |
| <a id="gueltigkeitszeitraum"></a>`gueltigkeitszeitraum` | [Zeitraum](/bo4e/202604/com/Zeitraum) | Gültigkeitszeitraum |
| <a id="datenstanduenb"></a>`datenstandUENB` | [Datenstand](/bo4e/202604/com/Datenstand) | Datenstand ÜNB |
| <a id="datenstandnb"></a>`datenstandNB` | [Datenstand](/bo4e/202604/com/Datenstand) | Datenstand NB |
| <a id="datenderbeteiligtenmarktrolle"></a>`datenDerBeteiligtenMarktrolle` | [DatenDerBeteiligtenMarktrolle](/bo4e/202604/com/DatenDerBeteiligtenMarktrolle) | Daten der Beteiligten Marktrollen |
| <a id="bilanzierteenergiemenge"></a>`bilanzierteEnergiemenge` | [Menge](/bo4e/202604/com/Menge) | Bilanzierte Energiemenge |
| <a id="lastprofile"></a>`lastprofile` | [Lastprofil[]](/bo4e/202604/com/Lastprofil) | Eine Liste der verwendeten Lastprofile (SLP, SLP/TLP, ALP etc.) |
| <a id="lastprofilebilanzierungsbeteiligter"></a>`lastprofileBilanzierungsbeteiligter` | [Lastprofil[]](/bo4e/202604/com/Lastprofil) | Lastprofile des Bilanzierungsbeteiligten |
| <a id="detailsprognosegrundlage"></a>`detailsPrognosegrundlage` | [Enum Profiltyp[]](/bo4e/202604/enum/Profiltyp)<br/><Werte>`SLP_SEP`, `TLP_TEP`, `TEP`, `GEWERBE_ALLGEMEIN`, `GEWERBE_WERKTAGS_8_18_UHR`, `GEWERBE_MIT_STARKEM_BIS_UEBERWIEGENDEM_VERBRAUCH_IN_DEN_ABENDSTUNDEN`, `GEWERBE_DURCHLAUFEND`, `GEWERBE_LADEN_FRISEUR`, `GEWERBE_BAECKEREI_MIT_BACKSTUBE`, `GEWERBE_WOCHENENDBETRIEB`, `LANDWIRTSCHAFTSBETRIEBE_ALLGEMEIN`, `LANDWIRTSCHAFTSBETRIEBE_MIT_MILCHWIRTSCHAFT_NEBENERWERBS_TIERZUCHT`, `LANDWIRTSCHAFT_OHNE_MILCHVIEH`, `HAUSHALT`, `BANDLAST`, `UNTERBRECHBARE_VERBRAUCHSEINRICHTUNG`, `HEIZWAERMESPEICHER`, `STRASSENBELEUCHTUNG`, `PHOTOVOLTAIK_MARKTLOKATION`, `BLOCKHEIZKRAFTWERK`, `SONSTIGE_VERBRAUCHENDE_MARKTLOKATION`, `SONSTIGE_ERZEUGENDE_MARKTLOKATION`, `E_MOBILITAET_LADEPUNKT_IM_OEFFENTLICHEN_BEREICH`, `E_MOBILITAET_LADEPUNKT_EINES_HAUSHALTS`, `E_MOBILITAET_LADEPUNKT_EINES_GEWERBES`</Werte> | Prognosegrundlage - Besteht der Bedarf ein tagesparameteräbhängiges Lastprofil mit gemeinsamer Messung anzugeben, so ist dies über die 2 -malige Wiederholung des CAV Segments mit der Angabe der Codes E02 und E14 möglich. |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[boTyp](/bo4e/202604/bo/Bilanzierung#botyp) <span className="hbs-pflicht">\*</span></span> | Typ des BO | [Enum BOTyp](/bo4e/202604/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> |
| <span className="hbs-f hbs-e0">[versionStruktur](/bo4e/202604/bo/Bilanzierung#versionstruktur) <span className="hbs-pflicht">\*</span></span> | versionStruktur | string |
| <span className="hbs-f hbs-e0">[marktlokationsId](/bo4e/202604/bo/Bilanzierung#marktlokationsid)</span> | Für welche Marktlokation gelten diese Bilanzierungsdaten | string |
| <span className="hbs-f hbs-e0">[aggregationsverantwortung](/bo4e/202604/bo/Bilanzierung#aggregationsverantwortung)</span> | Aggregationsverantwortung | [Enum Aggregationsverantwortung](/bo4e/202604/enum/Aggregationsverantwortung)<br/><Werte>`UENB`, `VNB`</Werte> |
| <span className="hbs-f hbs-e0">[zeitreihentyp](/bo4e/202604/bo/Bilanzierung#zeitreihentyp)</span> | Zeitreihentyp | [Enum Zeitreihentyp](/bo4e/202604/enum/Zeitreihentyp)<br/><Werte>`EGS`, `LGS`, `NZR`, `SES`, `SLS`, `TES`, `TLS`, `SLS_TLS`, `SES_TES`, `AUS`, `BAS`, `DBA`, `DZR`, `DZÜ`, `FPE`, `FPI`, `SRE`, `SRI`, `VZR`, `BIL`, `BIP`, `BIT`, `GAL`, `GAP`, `GAT`, `GEL`, `GEP`, `GET`, `SOL`, `SOP`, `SOT`, `WFL`, `WFP`, `WNL`, `WNP`, `WNT`, `WAL`, `WAP`, `WAT`, `AU1`, `BI1`, `BI2`, `BI3`, `GAA`, `GAB`, `GAC`, `GE1`, `GE2`, `GE3`, `SO1`, `SO2`, `SO3`, `WF1`, `WF2`, `WF3`, `WN1`, `WN2`, `WN3`, `WAA`, `WAB`, `WAC`, `AUSFALLARBEITSSUMME`, `BILANZKREISABWEICHUNGSSALDO`, `DIFFERENZZEITREIHE`, `DELTAZEITREIHE`, `DELTAZEITREIHENUEBERTRAG`, `FAHRPLANENTNAHMESUMME`, `FAHRPLANEINSPEISESUMME`, `UEBERFUEHRUNGSZEITREIHE_SEKUNDAERREGELLEISTUNG_EXPORT`, `UEBERFUEHRUNGSZEITREIHE_SEKUNDAERREGELLEISTUNG_IMPORT`, `VERLUSTZEITREIHE`, `EE_EINSPEISESUMME_BIOMASSE_BIOGAS_GEMESSEN`, `EE_EINSPEISESUMME_BIOMASSE_BIOGAS_EINSPEISEPROFIL`, `EE_EINSPEISESUMME_BIOMASSE_BIOGAS_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`, `EE_EINSPEISESUMME_DEPONIE_KLAER_GRUBENGAS_GEMESSEN`, `EE_EINSPEISESUMME_DEPONIE_KLAER_GRUBENGAS_EINSPEISEPROFIL`, `EE_EINSPEISESUMME_DEPONIE_KLAER_GRUBENGAS_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`, `EE_EINSPEISESUMME_GEOTHERMIE_GEMESSEN`, `EE_EINSPEISESUMME_GEOTHERMIE_EINSPEISEPROFIL`, `EE_EINSPEISESUMME_GEOTHERMIE_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`, `EE_EINSPEISESUMME_SOLAR_GEMESSEN`, `EE_EINSPEISESUMME_SOLAR_EINSPEISEPROFIL`, `EE_EINSPEISESUMME_SOLAR_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`, `EE_EINSPEISESUMME_WIND_OFFSHORE_GEMESSEN`, `EE_EINSPEISESUMME_WIND_OFFSHORE_EINSPEISEPROFIL`, `EE_EINSPEISESUMME_WIND_OFFSHORE_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`, `EE_EINSPEISESUMME_WIND_ONSHORE_GEMESSEN`, `EE_EINSPEISESUMME_WIND_ONSHORE_EINSPEISEPROFIL`, `EE_EINSPEISESUMME_WIND_ONSHORE_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`, `EE_EINSPEISESUMME_WASSERKRAFT_GEMESSEN`, `EE_EINSPEISESUMME_WASSERKRAFT_EINSPEISEPROFIL`, `EE_EINSPEISESUMME_WASSERKRAFT_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`, `EEG_UEBERFUEHRUNG_AUSFALLARBEIT`, `EEG_UEBERFUEHRUNG_BIOMASSE_BIOGAS_WERTE`, `EEG_UEBERFUEHRUNG_BIOMASSE_BIOGAS_STANDARDEINSPEISEPROFIL`, `EEG_UEBERFUEHRUNG_BIOMASSE_BIOGAS_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`, `EEG_UEBERFUEHRUNG_DEPONIE_KLAER_GRUBENGAS_WERTE`, `EEG_UEBERFUEHRUNG_DEPONIE_KLAER_GRUBENGAS_STANDARDEINSPEISEPROFIL`, `EEG_UEBERFUEHRUNG_DEPONIE_KLAER_GRUBENGAS_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`, `EEG_UEBERFUEHRUNG_GEOTHERMIE_WERTE`, `EEG_UEBERFUEHRUNG_GEOTHERMIE_STANDARDEINSPEISEPROFIL`, `EEG_UEBERFUEHRUNG_GEOTHERMIE_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`, `EEG_UEBERFUEHRUNG_SOLAR_WERTE`, `EEG_UEBERFUEHRUNG_SOLAR_STANDARDEINSPEISEPROFIL`, `EEG_UEBERFUEHRUNG_SOLAR_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`, `EEG_UEBERFUEHRUNG_WIND_OFFSHORE_WERTE`, `EEG_UEBERFUEHRUNG_WIND_OFFSHORE_STANDARDEINSPEISEPROFIL`, `EEG_UEBERFUEHRUNG_WIND_OFFSHORE_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`, `EEG_UEBERFUEHRUNG_WIND_ONSHORE_WERTE`, `EEG_UEBERFUEHRUNG_WIND_ONSHORE_STANDARDEINSPEISEPROFIL`, `EEG_UEBERFUEHRUNG_WIND_ONSHORE_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`, `EEG_UEBERFUEHRUNG_WASSERKRAFT_WERTE`, `EEG_UEBERFUEHRUNG_WASSERKRAFT_STANDARDEINSPEISEPROFIL`, `EEG_UEBERFUEHRUNG_WASSERKRAFT_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</Werte> |
| <span className="hbs-f hbs-e0">[prognosegrundlage](/bo4e/202604/bo/Bilanzierung#prognosegrundlage)</span> | Prognosegrundlage | [Enum Prognosegrundlage](/bo4e/202604/enum/Prognosegrundlage)<br/><Werte>`WERTE`, `PROFILE`</Werte> |
| <span className="hbs-f hbs-e0">[bilanzierungsbeginn](/bo4e/202604/bo/Bilanzierung#bilanzierungsbeginn)</span> | Inklusiver Start der Bilanzierung | string (date-time) |
| <span className="hbs-f hbs-e0">[bilanzierungsende](/bo4e/202604/bo/Bilanzierung#bilanzierungsende)</span> | Exklusives Ende der Bilanzierung | string (date-time) |
| <span className="hbs-f hbs-e0">[bilanzkreis](/bo4e/202604/bo/Bilanzierung#bilanzkreis)</span> | Bilanzkreis | string |
| <span className="hbs-g hbs-e0">[bilanzkreise](/bo4e/202604/bo/Bilanzierung#bilanzkreise) <span className="hbs-liste">[ ]</span></span> | Bilanzkreis | [Bilanzkreis[]](/bo4e/202604/bo/Bilanzkreis) |
| <span className="hbs-f hbs-e1">[boTyp](/bo4e/202604/bo/Bilanzkreis#botyp)</span> | Typ des BO | [Enum BOTyp](/bo4e/202604/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> |
| <span className="hbs-f hbs-e1">[versionStruktur](/bo4e/202604/bo/Bilanzkreis#versionstruktur)</span> | versionStruktur | string |
| <span className="hbs-f hbs-e1">[bezeichnung](/bo4e/202604/bo/Bilanzkreis#bezeichnung)</span> | Externe Bezeichnung | string |
| <span className="hbs-f hbs-e1">[prioritaet](/bo4e/202604/bo/Bilanzkreis#prioritaet)</span> | prioritaet | integer |
| <span className="hbs-f hbs-e0">[fallgruppenzuordnung](/bo4e/202604/bo/Bilanzierung#fallgruppenzuordnung)</span> | Fallgruppenzuordnung (für gas RLM) | [Enum Fallgruppenzuordnung](/bo4e/202604/enum/Fallgruppenzuordnung)<br/><Werte>`GABI_RLMmT`, `GABI_RLMoT`, `GABI_RLMNEV`</Werte> |
| <span className="hbs-g hbs-e0">[temperaturarbeit](/bo4e/202604/bo/Bilanzierung#temperaturarbeit)</span> | Kundenwert TLP | [Menge](/bo4e/202604/com/Menge) |
| <span className="hbs-f hbs-e1">[wert](/bo4e/202604/com/Menge#wert)</span> | Wert | number (float) |
| <span className="hbs-f hbs-e1">[einheit](/bo4e/202604/com/Menge#einheit)</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202604/enum/Mengeneinheit)<br/><Werte>`W`, `WH`, `KW`, `KWH`, `KVARH`, `MW`, `MWH`, `STUECK`, `KUBIKMETER`, `STUNDE`, `TAG`, `MONAT`, `JAHR`, `PROZENT`, `ANZAHL`, `VAR`, `KVAR`, `VARH`, `KWHK`, `Z16`, `KWT`, `WATT_PRO_QUADRATMETER`, `METER_PRO_SEKUNDE`</Werte> |
| <span className="hbs-f hbs-e1">[startdatum](/bo4e/202604/com/Menge#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e1">[enddatum](/bo4e/202604/com/Menge#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-g hbs-e0">[jahresverbrauchsprognose](/bo4e/202604/bo/Bilanzierung#jahresverbrauchsprognose)</span> | Jahresverbrauchsprognose | [Menge](/bo4e/202604/com/Menge) |
| <span className="hbs-f hbs-e1">[wert](/bo4e/202604/com/Menge#wert)</span> | Wert | number (float) |
| <span className="hbs-f hbs-e1">[einheit](/bo4e/202604/com/Menge#einheit)</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202604/enum/Mengeneinheit)<br/><Werte>`W`, `WH`, `KW`, `KWH`, `KVARH`, `MW`, `MWH`, `STUECK`, `KUBIKMETER`, `STUNDE`, `TAG`, `MONAT`, `JAHR`, `PROZENT`, `ANZAHL`, `VAR`, `KVAR`, `VARH`, `KWHK`, `Z16`, `KWT`, `WATT_PRO_QUADRATMETER`, `METER_PRO_SEKUNDE`</Werte> |
| <span className="hbs-f hbs-e1">[startdatum](/bo4e/202604/com/Menge#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e1">[enddatum](/bo4e/202604/com/Menge#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-g hbs-e0">[kundenwert](/bo4e/202604/bo/Bilanzierung#kundenwert)</span> | Kundenwert | [Menge](/bo4e/202604/com/Menge) |
| <span className="hbs-f hbs-e1">[wert](/bo4e/202604/com/Menge#wert)</span> | Wert | number (float) |
| <span className="hbs-f hbs-e1">[einheit](/bo4e/202604/com/Menge#einheit)</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202604/enum/Mengeneinheit)<br/><Werte>`W`, `WH`, `KW`, `KWH`, `KVARH`, `MW`, `MWH`, `STUECK`, `KUBIKMETER`, `STUNDE`, `TAG`, `MONAT`, `JAHR`, `PROZENT`, `ANZAHL`, `VAR`, `KVAR`, `VARH`, `KWHK`, `Z16`, `KWT`, `WATT_PRO_QUADRATMETER`, `METER_PRO_SEKUNDE`</Werte> |
| <span className="hbs-f hbs-e1">[startdatum](/bo4e/202604/com/Menge#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e1">[enddatum](/bo4e/202604/com/Menge#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-g hbs-e0">[verbrauchsaufteilung](/bo4e/202604/bo/Bilanzierung#verbrauchsaufteilung)</span> | Verbrauchsaufteilung | [Menge](/bo4e/202604/com/Menge) |
| <span className="hbs-f hbs-e1">[wert](/bo4e/202604/com/Menge#wert)</span> | Wert | number (float) |
| <span className="hbs-f hbs-e1">[einheit](/bo4e/202604/com/Menge#einheit)</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202604/enum/Mengeneinheit)<br/><Werte>`W`, `WH`, `KW`, `KWH`, `KVARH`, `MW`, `MWH`, `STUECK`, `KUBIKMETER`, `STUNDE`, `TAG`, `MONAT`, `JAHR`, `PROZENT`, `ANZAHL`, `VAR`, `KVAR`, `VARH`, `KWHK`, `Z16`, `KWT`, `WATT_PRO_QUADRATMETER`, `METER_PRO_SEKUNDE`</Werte> |
| <span className="hbs-f hbs-e1">[startdatum](/bo4e/202604/com/Menge#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e1">[enddatum](/bo4e/202604/com/Menge#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-f hbs-e0">[wahlrechtPrognosegrundlage](/bo4e/202604/bo/Bilanzierung#wahlrechtprognosegrundlage)</span> | Wahlrecht der Prognosegrundlage (true = Wahlrecht beim Lieferanten vorhanden) | [Enum WahlrechtPrognosegrundlage](/bo4e/202604/enum/WahlrechtPrognosegrundlage)<br/><Werte>`DURCH_LF`, `DURCH_LF_NICHT_GEGEBEN`, `NICHT_WEGEN_GROSSEN_VERBRAUCHS`, `NICHT_WEGEN_EIGENVERBRAUCH`, `NICHT_WEGEN_TAGES_VERBRAUCH`, `NICHT_WEGEN_ENWG`</Werte> |
| <span className="hbs-f hbs-e0">[grundWahlrechtPrognosegrundlage](/bo4e/202604/bo/Bilanzierung#grundwahlrechtprognosegrundlage)</span> | Grund Wahlrecht der Prognosegrundlage (true = Wahlrecht beim Lieferanten vorhanden) | [Enum WahlrechtPrognosegrundlage](/bo4e/202604/enum/WahlrechtPrognosegrundlage)<br/><Werte>`DURCH_LF`, `DURCH_LF_NICHT_GEGEBEN`, `NICHT_WEGEN_GROSSEN_VERBRAUCHS`, `NICHT_WEGEN_EIGENVERBRAUCH`, `NICHT_WEGEN_TAGES_VERBRAUCH`, `NICHT_WEGEN_ENWG`</Werte> |
| <span className="hbs-f hbs-e0">[abwicklungsmodell](/bo4e/202604/bo/Bilanzierung#abwicklungsmodell)</span> | Abwicklungsmodell | [Enum Abwicklungsmodell](/bo4e/202604/enum/Abwicklungsmodell)<br/><Werte>`MODELL_1_BILANZIERUNG_AN_MARKTLOKATION`, `MODELL_2_BILANZIERUNG_IM_BILANZIERUNGSGEBIET`</Werte> |
| <span className="hbs-g hbs-e0">[vorjahresverbrauch](/bo4e/202604/bo/Bilanzierung#vorjahresverbrauch)</span> | Vorjahresverbrauch | [Menge](/bo4e/202604/com/Menge) |
| <span className="hbs-f hbs-e1">[wert](/bo4e/202604/com/Menge#wert)</span> | Wert | number (float) |
| <span className="hbs-f hbs-e1">[einheit](/bo4e/202604/com/Menge#einheit)</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202604/enum/Mengeneinheit)<br/><Werte>`W`, `WH`, `KW`, `KWH`, `KVARH`, `MW`, `MWH`, `STUECK`, `KUBIKMETER`, `STUNDE`, `TAG`, `MONAT`, `JAHR`, `PROZENT`, `ANZAHL`, `VAR`, `KVAR`, `VARH`, `KWHK`, `Z16`, `KWT`, `WATT_PRO_QUADRATMETER`, `METER_PRO_SEKUNDE`</Werte> |
| <span className="hbs-f hbs-e1">[startdatum](/bo4e/202604/com/Menge#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e1">[enddatum](/bo4e/202604/com/Menge#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-f hbs-e0">[datenqualitaet](/bo4e/202604/bo/Bilanzierung#datenqualitaet)</span> | Datenqualität | [Enum Datenqualitaet](/bo4e/202604/enum/Datenqualitaet)<br/><Werte>`ERWARTETE_DATEN`, `IM_SYSTEM_VORHANDENE_DATEN`, `INFORMATIVE_DATEN`, `GUELTIGE_DATEN`, `KEINE_DATEN`, `IM_SYSTEM_KEINE_DATEN_VORHANDEN`, `KEINE_DATEN_ERWARTET`, `DIFFERENZ_DATEN`, `DIFFERENZ_ERWARTETE_DATEN`, `DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</Werte> |
| <span className="hbs-g hbs-e0">[gueltigkeitszeitraum](/bo4e/202604/bo/Bilanzierung#gueltigkeitszeitraum)</span> | Gültigkeitszeitraum | [Zeitraum](/bo4e/202604/com/Zeitraum) |
| <span className="hbs-f hbs-e1">[zeiteinheit](/bo4e/202604/com/Zeitraum#zeiteinheit)</span> | Zeiteinheit | [Enum Zeiteinheit](/bo4e/202604/enum/Zeiteinheit)<br/><Werte>`SEKUNDE`, `MINUTE`, `STUNDE`, `VIERTEL_STUNDE`, `TAG`, `WOCHE`, `MONAT`, `QUARTAL`, `HALBJAHR`, `JAHR`</Werte> |
| <span className="hbs-f hbs-e1">[dauer](/bo4e/202604/com/Zeitraum#dauer)</span> | dauer | integer |
| <span className="hbs-f hbs-e1">[startdatum](/bo4e/202604/com/Zeitraum#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e1">[enddatum](/bo4e/202604/com/Zeitraum#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-f hbs-e1">[einheit](/bo4e/202604/com/Zeitraum#einheit)</span> | Zeiteinheit | [Enum Zeiteinheit](/bo4e/202604/enum/Zeiteinheit)<br/><Werte>`SEKUNDE`, `MINUTE`, `STUNDE`, `VIERTEL_STUNDE`, `TAG`, `WOCHE`, `MONAT`, `QUARTAL`, `HALBJAHR`, `JAHR`</Werte> |
| <span className="hbs-f hbs-e1">[ableseZeitraum](/bo4e/202604/com/Zeitraum#ablesezeitraum)</span> | ableseZeitraum | string |
| <span className="hbs-f hbs-e1">[abrechnungsZeitraum](/bo4e/202604/com/Zeitraum#abrechnungszeitraum)</span> | abrechnungsZeitraum | string |
| <span className="hbs-f hbs-e1">[zeitraumText](/bo4e/202604/com/Zeitraum#zeitraumtext)</span> | zeitraumText | string |
| <span className="hbs-f hbs-e1">[zeitraumId](/bo4e/202604/com/Zeitraum#zeitraumid)</span> | zeitraumId | integer |
| <span className="hbs-g hbs-e0">[datenstandUENB](/bo4e/202604/bo/Bilanzierung#datenstanduenb)</span> | Datenstand ÜNB | [Datenstand](/bo4e/202604/com/Datenstand) |
| <span className="hbs-g hbs-e1">[jahresverbrauchsprognose](/bo4e/202604/com/Datenstand#jahresverbrauchsprognose)</span> | — | [Menge](/bo4e/202604/com/Menge) |
| <span className="hbs-f hbs-e2">[wert](/bo4e/202604/com/Menge#wert)</span> | Wert | number (float) |
| <span className="hbs-f hbs-e2">[einheit](/bo4e/202604/com/Menge#einheit)</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202604/enum/Mengeneinheit)<br/><Werte>`W`, `WH`, `KW`, `KWH`, `KVARH`, `MW`, `MWH`, `STUECK`, `KUBIKMETER`, `STUNDE`, `TAG`, `MONAT`, `JAHR`, `PROZENT`, `ANZAHL`, `VAR`, `KVAR`, `VARH`, `KWHK`, `Z16`, `KWT`, `WATT_PRO_QUADRATMETER`, `METER_PRO_SEKUNDE`</Werte> |
| <span className="hbs-f hbs-e2">[startdatum](/bo4e/202604/com/Menge#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e2">[enddatum](/bo4e/202604/com/Menge#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-g hbs-e1">[tatsaechlichBilanzierteEnergiemenge](/bo4e/202604/com/Datenstand#tatsaechlichbilanzierteenergiemenge)</span> | — | [Menge](/bo4e/202604/com/Menge) |
| <span className="hbs-f hbs-e2">[wert](/bo4e/202604/com/Menge#wert)</span> | Wert | number (float) |
| <span className="hbs-f hbs-e2">[einheit](/bo4e/202604/com/Menge#einheit)</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202604/enum/Mengeneinheit)<br/><Werte>`W`, `WH`, `KW`, `KWH`, `KVARH`, `MW`, `MWH`, `STUECK`, `KUBIKMETER`, `STUNDE`, `TAG`, `MONAT`, `JAHR`, `PROZENT`, `ANZAHL`, `VAR`, `KVAR`, `VARH`, `KWHK`, `Z16`, `KWT`, `WATT_PRO_QUADRATMETER`, `METER_PRO_SEKUNDE`</Werte> |
| <span className="hbs-f hbs-e2">[startdatum](/bo4e/202604/com/Menge#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e2">[enddatum](/bo4e/202604/com/Menge#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-g hbs-e1">[zuBilanzierendeEnergiemenge](/bo4e/202604/com/Datenstand#zubilanzierendeenergiemenge)</span> | — | [Menge](/bo4e/202604/com/Menge) |
| <span className="hbs-f hbs-e2">[wert](/bo4e/202604/com/Menge#wert)</span> | Wert | number (float) |
| <span className="hbs-f hbs-e2">[einheit](/bo4e/202604/com/Menge#einheit)</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202604/enum/Mengeneinheit)<br/><Werte>`W`, `WH`, `KW`, `KWH`, `KVARH`, `MW`, `MWH`, `STUECK`, `KUBIKMETER`, `STUNDE`, `TAG`, `MONAT`, `JAHR`, `PROZENT`, `ANZAHL`, `VAR`, `KVAR`, `VARH`, `KWHK`, `Z16`, `KWT`, `WATT_PRO_QUADRATMETER`, `METER_PRO_SEKUNDE`</Werte> |
| <span className="hbs-f hbs-e2">[startdatum](/bo4e/202604/com/Menge#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e2">[enddatum](/bo4e/202604/com/Menge#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-f hbs-e1">[bilanzkreis](/bo4e/202604/com/Datenstand#bilanzkreis)</span> | Bilanzkreis | string |
| <span className="hbs-f hbs-e1">[bilanzierungsgebiet](/bo4e/202604/com/Datenstand#bilanzierungsgebiet)</span> | Bilanzierungsgebiet | string |
| <span className="hbs-g hbs-e1">[lastprofile](/bo4e/202604/com/Datenstand#lastprofile) <span className="hbs-liste">[ ]</span></span> | Eine Liste der verwendeten Lastprofile (SLP, SLP/TLP, ALP etc.) | [Lastprofil[]](/bo4e/202604/com/Lastprofil) |
| <span className="hbs-f hbs-e2">[bezeichnung](/bo4e/202604/com/Lastprofil#bezeichnung)</span> | Bezeichnung des Profils | string |
| <span className="hbs-f hbs-e2">[verfahren](/bo4e/202604/com/Lastprofil#verfahren)</span> | Profilverfahren | [Enum Profilverfahren](/bo4e/202604/enum/Profilverfahren)<br/><Werte>`SYNTHETISCH`, `ANALYTISCH`</Werte> |
| <span className="hbs-f hbs-e2">[profilart](/bo4e/202604/com/Lastprofil#profilart)</span> | Profilart | [Enum Profilart](/bo4e/202604/enum/Profilart)<br/><Werte>`ART_STANDARDLASTPROFIL`, `ART_TAGESPARAMETERABHAENGIGES_LASTPROFIL`, `ART_LASTPROFIL`</Werte> |
| <span className="hbs-f hbs-e2">[profilschar](/bo4e/202604/com/Lastprofil#profilschar)</span> | Profilschar des Profils | string |
| <span className="hbs-f hbs-e2">[einspeisung](/bo4e/202604/com/Lastprofil#einspeisung)</span> | Kennzeichen Einspeisung | boolean |
| <span className="hbs-f hbs-e2">[herausgeber](/bo4e/202604/com/Lastprofil#herausgeber)</span> | Herausgeber des Lastprofils | string |
| <span className="hbs-g hbs-e2">[tagesparameter](/bo4e/202604/com/Lastprofil#tagesparameter)</span> | — | [Tagesparameter](/bo4e/202604/com/Tagesparameter) |
| <span className="hbs-f hbs-e3">[klimazone](/bo4e/202604/com/Tagesparameter#klimazone)</span> | klimazone | string |
| <span className="hbs-f hbs-e3">[temperaturmessstelle](/bo4e/202604/com/Tagesparameter#temperaturmessstelle)</span> | temperaturmessstelle | string |
| <span className="hbs-f hbs-e3">[dienstanbieter](/bo4e/202604/com/Tagesparameter#dienstanbieter)</span> | dienstanbieter | string |
| <span className="hbs-f hbs-e3">[herausgeber](/bo4e/202604/com/Tagesparameter#herausgeber)</span> | Herausgeber | [Enum Herausgeber](/bo4e/202604/enum/Herausgeber)<br/><Werte>`NB`, `BDEW`, `TUM`</Werte> |
| <span className="hbs-f hbs-e2">[referenzprofilbezeichnung](/bo4e/202604/com/Lastprofil#referenzprofilbezeichnung)</span> | Bezeichnung des Referenzprofils | string |
| <span className="hbs-f hbs-e2">[referenzprofil](/bo4e/202604/com/Lastprofil#referenzprofil)</span> | Referenzprofil | string |
| <span className="hbs-f hbs-e2">[profiltyp](/bo4e/202604/com/Lastprofil#profiltyp)</span> | Profiltyp | [Enum Profiltyp](/bo4e/202604/enum/Profiltyp)<br/><Werte>`SLP_SEP`, `TLP_TEP`, `TEP`, `GEWERBE_ALLGEMEIN`, `GEWERBE_WERKTAGS_8_18_UHR`, `GEWERBE_MIT_STARKEM_BIS_UEBERWIEGENDEM_VERBRAUCH_IN_DEN_ABENDSTUNDEN`, `GEWERBE_DURCHLAUFEND`, `GEWERBE_LADEN_FRISEUR`, `GEWERBE_BAECKEREI_MIT_BACKSTUBE`, `GEWERBE_WOCHENENDBETRIEB`, `LANDWIRTSCHAFTSBETRIEBE_ALLGEMEIN`, `LANDWIRTSCHAFTSBETRIEBE_MIT_MILCHWIRTSCHAFT_NEBENERWERBS_TIERZUCHT`, `LANDWIRTSCHAFT_OHNE_MILCHVIEH`, `HAUSHALT`, `BANDLAST`, `UNTERBRECHBARE_VERBRAUCHSEINRICHTUNG`, `HEIZWAERMESPEICHER`, `STRASSENBELEUCHTUNG`, `PHOTOVOLTAIK_MARKTLOKATION`, `BLOCKHEIZKRAFTWERK`, `SONSTIGE_VERBRAUCHENDE_MARKTLOKATION`, `SONSTIGE_ERZEUGENDE_MARKTLOKATION`, `E_MOBILITAET_LADEPUNKT_IM_OEFFENTLICHEN_BEREICH`, `E_MOBILITAET_LADEPUNKT_EINES_HAUSHALTS`, `E_MOBILITAET_LADEPUNKT_EINES_GEWERBES`</Werte> |
| <span className="hbs-f hbs-e2">[normierungsfaktor](/bo4e/202604/com/Lastprofil#normierungsfaktor)</span> | Normierungsfaktor | [Enum Normierungsfaktor](/bo4e/202604/enum/Normierungsfaktor)<br/><Werte>`NORMIERUNGSFAKTOR_1_000_000_KWH_A`, `NORMIERUNGSFAKTOR_300_KWH_K`, `NORMIERUNGSFAKTOR_1_000_000_KW`</Werte> |
| <span className="hbs-g hbs-e2">[tagesmitteltemperatur](/bo4e/202604/com/Lastprofil#tagesmitteltemperatur)</span> | — | [Tagesmitteltemperatur](/bo4e/202604/com/Tagesmitteltemperatur) |
| <span className="hbs-f hbs-e3">[berechnungTagesmitteltemperatur](/bo4e/202604/com/Tagesmitteltemperatur#berechnungtagesmitteltemperatur)</span> | Berechnungsmethode | [Enum Berechnungsmethode](/bo4e/202604/enum/Berechnungsmethode)<br/><Werte>`24H_MITTELWERT`, `VOM_ANBIETER_ZUR_VERFUEGUNG_GESTELLTE_AEQUIVALENTE_TAGESMITTELTEMPERATUR`, `AEQUIVALENTE_TAGESMITTELTEMPERATUR`</Werte> |
| <span className="hbs-f hbs-e3">[anteilA](/bo4e/202604/com/Tagesmitteltemperatur#anteila)</span> | Anteil A | number (float) |
| <span className="hbs-f hbs-e3">[anteilB](/bo4e/202604/com/Tagesmitteltemperatur#anteilb)</span> | Anteil B | number (float) |
| <span className="hbs-f hbs-e3">[anteilC](/bo4e/202604/com/Tagesmitteltemperatur#anteilc)</span> | Anteil C | number (float) |
| <span className="hbs-f hbs-e3">[anteilD](/bo4e/202604/com/Tagesmitteltemperatur#anteild)</span> | Anteil D | number (float) |
| <span className="hbs-f hbs-e3">[begrenzungstemperatur](/bo4e/202604/com/Tagesmitteltemperatur#begrenzungstemperatur)</span> | Begrenzungstemperatur | string |
| <span className="hbs-f hbs-e2">[begrenzungskonstante](/bo4e/202604/com/Lastprofil#begrenzungskonstante)</span> | Begrenzungskonstante | [Enum Begrenzungskonstante](/bo4e/202604/enum/Begrenzungskonstante)<br/><Werte>`BEGRENZUNGSKONSTANTE_0`, `BEGRENZUNGSKONSTANTE_1`</Werte> |
| <span className="hbs-f hbs-e1">[aggregationsverantwortung](/bo4e/202604/com/Datenstand#aggregationsverantwortung)</span> | Aggregationsverantwortung | [Enum Aggregationsverantwortung](/bo4e/202604/enum/Aggregationsverantwortung)<br/><Werte>`UENB`, `VNB`</Werte> |
| <span className="hbs-g hbs-e0">[datenstandNB](/bo4e/202604/bo/Bilanzierung#datenstandnb)</span> | Datenstand NB | [Datenstand](/bo4e/202604/com/Datenstand) |
| <span className="hbs-g hbs-e1">[jahresverbrauchsprognose](/bo4e/202604/com/Datenstand#jahresverbrauchsprognose)</span> | — | [Menge](/bo4e/202604/com/Menge) |
| <span className="hbs-f hbs-e2">[wert](/bo4e/202604/com/Menge#wert)</span> | Wert | number (float) |
| <span className="hbs-f hbs-e2">[einheit](/bo4e/202604/com/Menge#einheit)</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202604/enum/Mengeneinheit)<br/><Werte>`W`, `WH`, `KW`, `KWH`, `KVARH`, `MW`, `MWH`, `STUECK`, `KUBIKMETER`, `STUNDE`, `TAG`, `MONAT`, `JAHR`, `PROZENT`, `ANZAHL`, `VAR`, `KVAR`, `VARH`, `KWHK`, `Z16`, `KWT`, `WATT_PRO_QUADRATMETER`, `METER_PRO_SEKUNDE`</Werte> |
| <span className="hbs-f hbs-e2">[startdatum](/bo4e/202604/com/Menge#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e2">[enddatum](/bo4e/202604/com/Menge#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-g hbs-e1">[tatsaechlichBilanzierteEnergiemenge](/bo4e/202604/com/Datenstand#tatsaechlichbilanzierteenergiemenge)</span> | — | [Menge](/bo4e/202604/com/Menge) |
| <span className="hbs-f hbs-e2">[wert](/bo4e/202604/com/Menge#wert)</span> | Wert | number (float) |
| <span className="hbs-f hbs-e2">[einheit](/bo4e/202604/com/Menge#einheit)</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202604/enum/Mengeneinheit)<br/><Werte>`W`, `WH`, `KW`, `KWH`, `KVARH`, `MW`, `MWH`, `STUECK`, `KUBIKMETER`, `STUNDE`, `TAG`, `MONAT`, `JAHR`, `PROZENT`, `ANZAHL`, `VAR`, `KVAR`, `VARH`, `KWHK`, `Z16`, `KWT`, `WATT_PRO_QUADRATMETER`, `METER_PRO_SEKUNDE`</Werte> |
| <span className="hbs-f hbs-e2">[startdatum](/bo4e/202604/com/Menge#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e2">[enddatum](/bo4e/202604/com/Menge#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-g hbs-e1">[zuBilanzierendeEnergiemenge](/bo4e/202604/com/Datenstand#zubilanzierendeenergiemenge)</span> | — | [Menge](/bo4e/202604/com/Menge) |
| <span className="hbs-f hbs-e2">[wert](/bo4e/202604/com/Menge#wert)</span> | Wert | number (float) |
| <span className="hbs-f hbs-e2">[einheit](/bo4e/202604/com/Menge#einheit)</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202604/enum/Mengeneinheit)<br/><Werte>`W`, `WH`, `KW`, `KWH`, `KVARH`, `MW`, `MWH`, `STUECK`, `KUBIKMETER`, `STUNDE`, `TAG`, `MONAT`, `JAHR`, `PROZENT`, `ANZAHL`, `VAR`, `KVAR`, `VARH`, `KWHK`, `Z16`, `KWT`, `WATT_PRO_QUADRATMETER`, `METER_PRO_SEKUNDE`</Werte> |
| <span className="hbs-f hbs-e2">[startdatum](/bo4e/202604/com/Menge#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e2">[enddatum](/bo4e/202604/com/Menge#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-f hbs-e1">[bilanzkreis](/bo4e/202604/com/Datenstand#bilanzkreis)</span> | Bilanzkreis | string |
| <span className="hbs-f hbs-e1">[bilanzierungsgebiet](/bo4e/202604/com/Datenstand#bilanzierungsgebiet)</span> | Bilanzierungsgebiet | string |
| <span className="hbs-g hbs-e1">[lastprofile](/bo4e/202604/com/Datenstand#lastprofile) <span className="hbs-liste">[ ]</span></span> | Eine Liste der verwendeten Lastprofile (SLP, SLP/TLP, ALP etc.) | [Lastprofil[]](/bo4e/202604/com/Lastprofil) |
| <span className="hbs-f hbs-e2">[bezeichnung](/bo4e/202604/com/Lastprofil#bezeichnung)</span> | Bezeichnung des Profils | string |
| <span className="hbs-f hbs-e2">[verfahren](/bo4e/202604/com/Lastprofil#verfahren)</span> | Profilverfahren | [Enum Profilverfahren](/bo4e/202604/enum/Profilverfahren)<br/><Werte>`SYNTHETISCH`, `ANALYTISCH`</Werte> |
| <span className="hbs-f hbs-e2">[profilart](/bo4e/202604/com/Lastprofil#profilart)</span> | Profilart | [Enum Profilart](/bo4e/202604/enum/Profilart)<br/><Werte>`ART_STANDARDLASTPROFIL`, `ART_TAGESPARAMETERABHAENGIGES_LASTPROFIL`, `ART_LASTPROFIL`</Werte> |
| <span className="hbs-f hbs-e2">[profilschar](/bo4e/202604/com/Lastprofil#profilschar)</span> | Profilschar des Profils | string |
| <span className="hbs-f hbs-e2">[einspeisung](/bo4e/202604/com/Lastprofil#einspeisung)</span> | Kennzeichen Einspeisung | boolean |
| <span className="hbs-f hbs-e2">[herausgeber](/bo4e/202604/com/Lastprofil#herausgeber)</span> | Herausgeber des Lastprofils | string |
| <span className="hbs-g hbs-e2">[tagesparameter](/bo4e/202604/com/Lastprofil#tagesparameter)</span> | — | [Tagesparameter](/bo4e/202604/com/Tagesparameter) |
| <span className="hbs-f hbs-e3">[klimazone](/bo4e/202604/com/Tagesparameter#klimazone)</span> | klimazone | string |
| <span className="hbs-f hbs-e3">[temperaturmessstelle](/bo4e/202604/com/Tagesparameter#temperaturmessstelle)</span> | temperaturmessstelle | string |
| <span className="hbs-f hbs-e3">[dienstanbieter](/bo4e/202604/com/Tagesparameter#dienstanbieter)</span> | dienstanbieter | string |
| <span className="hbs-f hbs-e3">[herausgeber](/bo4e/202604/com/Tagesparameter#herausgeber)</span> | Herausgeber | [Enum Herausgeber](/bo4e/202604/enum/Herausgeber)<br/><Werte>`NB`, `BDEW`, `TUM`</Werte> |
| <span className="hbs-f hbs-e2">[referenzprofilbezeichnung](/bo4e/202604/com/Lastprofil#referenzprofilbezeichnung)</span> | Bezeichnung des Referenzprofils | string |
| <span className="hbs-f hbs-e2">[referenzprofil](/bo4e/202604/com/Lastprofil#referenzprofil)</span> | Referenzprofil | string |
| <span className="hbs-f hbs-e2">[profiltyp](/bo4e/202604/com/Lastprofil#profiltyp)</span> | Profiltyp | [Enum Profiltyp](/bo4e/202604/enum/Profiltyp)<br/><Werte>`SLP_SEP`, `TLP_TEP`, `TEP`, `GEWERBE_ALLGEMEIN`, `GEWERBE_WERKTAGS_8_18_UHR`, `GEWERBE_MIT_STARKEM_BIS_UEBERWIEGENDEM_VERBRAUCH_IN_DEN_ABENDSTUNDEN`, `GEWERBE_DURCHLAUFEND`, `GEWERBE_LADEN_FRISEUR`, `GEWERBE_BAECKEREI_MIT_BACKSTUBE`, `GEWERBE_WOCHENENDBETRIEB`, `LANDWIRTSCHAFTSBETRIEBE_ALLGEMEIN`, `LANDWIRTSCHAFTSBETRIEBE_MIT_MILCHWIRTSCHAFT_NEBENERWERBS_TIERZUCHT`, `LANDWIRTSCHAFT_OHNE_MILCHVIEH`, `HAUSHALT`, `BANDLAST`, `UNTERBRECHBARE_VERBRAUCHSEINRICHTUNG`, `HEIZWAERMESPEICHER`, `STRASSENBELEUCHTUNG`, `PHOTOVOLTAIK_MARKTLOKATION`, `BLOCKHEIZKRAFTWERK`, `SONSTIGE_VERBRAUCHENDE_MARKTLOKATION`, `SONSTIGE_ERZEUGENDE_MARKTLOKATION`, `E_MOBILITAET_LADEPUNKT_IM_OEFFENTLICHEN_BEREICH`, `E_MOBILITAET_LADEPUNKT_EINES_HAUSHALTS`, `E_MOBILITAET_LADEPUNKT_EINES_GEWERBES`</Werte> |
| <span className="hbs-f hbs-e2">[normierungsfaktor](/bo4e/202604/com/Lastprofil#normierungsfaktor)</span> | Normierungsfaktor | [Enum Normierungsfaktor](/bo4e/202604/enum/Normierungsfaktor)<br/><Werte>`NORMIERUNGSFAKTOR_1_000_000_KWH_A`, `NORMIERUNGSFAKTOR_300_KWH_K`, `NORMIERUNGSFAKTOR_1_000_000_KW`</Werte> |
| <span className="hbs-g hbs-e2">[tagesmitteltemperatur](/bo4e/202604/com/Lastprofil#tagesmitteltemperatur)</span> | — | [Tagesmitteltemperatur](/bo4e/202604/com/Tagesmitteltemperatur) |
| <span className="hbs-f hbs-e3">[berechnungTagesmitteltemperatur](/bo4e/202604/com/Tagesmitteltemperatur#berechnungtagesmitteltemperatur)</span> | Berechnungsmethode | [Enum Berechnungsmethode](/bo4e/202604/enum/Berechnungsmethode)<br/><Werte>`24H_MITTELWERT`, `VOM_ANBIETER_ZUR_VERFUEGUNG_GESTELLTE_AEQUIVALENTE_TAGESMITTELTEMPERATUR`, `AEQUIVALENTE_TAGESMITTELTEMPERATUR`</Werte> |
| <span className="hbs-f hbs-e3">[anteilA](/bo4e/202604/com/Tagesmitteltemperatur#anteila)</span> | Anteil A | number (float) |
| <span className="hbs-f hbs-e3">[anteilB](/bo4e/202604/com/Tagesmitteltemperatur#anteilb)</span> | Anteil B | number (float) |
| <span className="hbs-f hbs-e3">[anteilC](/bo4e/202604/com/Tagesmitteltemperatur#anteilc)</span> | Anteil C | number (float) |
| <span className="hbs-f hbs-e3">[anteilD](/bo4e/202604/com/Tagesmitteltemperatur#anteild)</span> | Anteil D | number (float) |
| <span className="hbs-f hbs-e3">[begrenzungstemperatur](/bo4e/202604/com/Tagesmitteltemperatur#begrenzungstemperatur)</span> | Begrenzungstemperatur | string |
| <span className="hbs-f hbs-e2">[begrenzungskonstante](/bo4e/202604/com/Lastprofil#begrenzungskonstante)</span> | Begrenzungskonstante | [Enum Begrenzungskonstante](/bo4e/202604/enum/Begrenzungskonstante)<br/><Werte>`BEGRENZUNGSKONSTANTE_0`, `BEGRENZUNGSKONSTANTE_1`</Werte> |
| <span className="hbs-f hbs-e1">[aggregationsverantwortung](/bo4e/202604/com/Datenstand#aggregationsverantwortung)</span> | Aggregationsverantwortung | [Enum Aggregationsverantwortung](/bo4e/202604/enum/Aggregationsverantwortung)<br/><Werte>`UENB`, `VNB`</Werte> |
| <span className="hbs-g hbs-e0">[datenDerBeteiligtenMarktrolle](/bo4e/202604/bo/Bilanzierung#datenderbeteiligtenmarktrolle)</span> | Daten der Beteiligten Marktrollen | [DatenDerBeteiligtenMarktrolle](/bo4e/202604/com/DatenDerBeteiligtenMarktrolle) |
| <span className="hbs-f hbs-e1">[bilanzierungsbeginn](/bo4e/202604/com/DatenDerBeteiligtenMarktrolle#bilanzierungsbeginn)</span> | Bilanzierungsbeginn | string (date-time) |
| <span className="hbs-f hbs-e1">[bilanzierungsende](/bo4e/202604/com/DatenDerBeteiligtenMarktrolle#bilanzierungsende)</span> | Bilanzierungsende | string (date-time) |
| <span className="hbs-g hbs-e0">[bilanzierteEnergiemenge](/bo4e/202604/bo/Bilanzierung#bilanzierteenergiemenge)</span> | Bilanzierte Energiemenge | [Menge](/bo4e/202604/com/Menge) |
| <span className="hbs-f hbs-e1">[wert](/bo4e/202604/com/Menge#wert)</span> | Wert | number (float) |
| <span className="hbs-f hbs-e1">[einheit](/bo4e/202604/com/Menge#einheit)</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202604/enum/Mengeneinheit)<br/><Werte>`W`, `WH`, `KW`, `KWH`, `KVARH`, `MW`, `MWH`, `STUECK`, `KUBIKMETER`, `STUNDE`, `TAG`, `MONAT`, `JAHR`, `PROZENT`, `ANZAHL`, `VAR`, `KVAR`, `VARH`, `KWHK`, `Z16`, `KWT`, `WATT_PRO_QUADRATMETER`, `METER_PRO_SEKUNDE`</Werte> |
| <span className="hbs-f hbs-e1">[startdatum](/bo4e/202604/com/Menge#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e1">[enddatum](/bo4e/202604/com/Menge#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-g hbs-e0">[lastprofile](/bo4e/202604/bo/Bilanzierung#lastprofile) <span className="hbs-liste">[ ]</span></span> | Eine Liste der verwendeten Lastprofile (SLP, SLP/TLP, ALP etc.) | [Lastprofil[]](/bo4e/202604/com/Lastprofil) |
| <span className="hbs-f hbs-e1">[bezeichnung](/bo4e/202604/com/Lastprofil#bezeichnung)</span> | Bezeichnung des Profils | string |
| <span className="hbs-f hbs-e1">[verfahren](/bo4e/202604/com/Lastprofil#verfahren)</span> | Profilverfahren | [Enum Profilverfahren](/bo4e/202604/enum/Profilverfahren)<br/><Werte>`SYNTHETISCH`, `ANALYTISCH`</Werte> |
| <span className="hbs-f hbs-e1">[profilart](/bo4e/202604/com/Lastprofil#profilart)</span> | Profilart | [Enum Profilart](/bo4e/202604/enum/Profilart)<br/><Werte>`ART_STANDARDLASTPROFIL`, `ART_TAGESPARAMETERABHAENGIGES_LASTPROFIL`, `ART_LASTPROFIL`</Werte> |
| <span className="hbs-f hbs-e1">[profilschar](/bo4e/202604/com/Lastprofil#profilschar)</span> | Profilschar des Profils | string |
| <span className="hbs-f hbs-e1">[einspeisung](/bo4e/202604/com/Lastprofil#einspeisung)</span> | Kennzeichen Einspeisung | boolean |
| <span className="hbs-f hbs-e1">[herausgeber](/bo4e/202604/com/Lastprofil#herausgeber)</span> | Herausgeber des Lastprofils | string |
| <span className="hbs-g hbs-e1">[tagesparameter](/bo4e/202604/com/Lastprofil#tagesparameter)</span> | — | [Tagesparameter](/bo4e/202604/com/Tagesparameter) |
| <span className="hbs-f hbs-e2">[klimazone](/bo4e/202604/com/Tagesparameter#klimazone)</span> | klimazone | string |
| <span className="hbs-f hbs-e2">[temperaturmessstelle](/bo4e/202604/com/Tagesparameter#temperaturmessstelle)</span> | temperaturmessstelle | string |
| <span className="hbs-f hbs-e2">[dienstanbieter](/bo4e/202604/com/Tagesparameter#dienstanbieter)</span> | dienstanbieter | string |
| <span className="hbs-f hbs-e2">[herausgeber](/bo4e/202604/com/Tagesparameter#herausgeber)</span> | Herausgeber | [Enum Herausgeber](/bo4e/202604/enum/Herausgeber)<br/><Werte>`NB`, `BDEW`, `TUM`</Werte> |
| <span className="hbs-f hbs-e1">[referenzprofilbezeichnung](/bo4e/202604/com/Lastprofil#referenzprofilbezeichnung)</span> | Bezeichnung des Referenzprofils | string |
| <span className="hbs-f hbs-e1">[referenzprofil](/bo4e/202604/com/Lastprofil#referenzprofil)</span> | Referenzprofil | string |
| <span className="hbs-f hbs-e1">[profiltyp](/bo4e/202604/com/Lastprofil#profiltyp)</span> | Profiltyp | [Enum Profiltyp](/bo4e/202604/enum/Profiltyp)<br/><Werte>`SLP_SEP`, `TLP_TEP`, `TEP`, `GEWERBE_ALLGEMEIN`, `GEWERBE_WERKTAGS_8_18_UHR`, `GEWERBE_MIT_STARKEM_BIS_UEBERWIEGENDEM_VERBRAUCH_IN_DEN_ABENDSTUNDEN`, `GEWERBE_DURCHLAUFEND`, `GEWERBE_LADEN_FRISEUR`, `GEWERBE_BAECKEREI_MIT_BACKSTUBE`, `GEWERBE_WOCHENENDBETRIEB`, `LANDWIRTSCHAFTSBETRIEBE_ALLGEMEIN`, `LANDWIRTSCHAFTSBETRIEBE_MIT_MILCHWIRTSCHAFT_NEBENERWERBS_TIERZUCHT`, `LANDWIRTSCHAFT_OHNE_MILCHVIEH`, `HAUSHALT`, `BANDLAST`, `UNTERBRECHBARE_VERBRAUCHSEINRICHTUNG`, `HEIZWAERMESPEICHER`, `STRASSENBELEUCHTUNG`, `PHOTOVOLTAIK_MARKTLOKATION`, `BLOCKHEIZKRAFTWERK`, `SONSTIGE_VERBRAUCHENDE_MARKTLOKATION`, `SONSTIGE_ERZEUGENDE_MARKTLOKATION`, `E_MOBILITAET_LADEPUNKT_IM_OEFFENTLICHEN_BEREICH`, `E_MOBILITAET_LADEPUNKT_EINES_HAUSHALTS`, `E_MOBILITAET_LADEPUNKT_EINES_GEWERBES`</Werte> |
| <span className="hbs-f hbs-e1">[normierungsfaktor](/bo4e/202604/com/Lastprofil#normierungsfaktor)</span> | Normierungsfaktor | [Enum Normierungsfaktor](/bo4e/202604/enum/Normierungsfaktor)<br/><Werte>`NORMIERUNGSFAKTOR_1_000_000_KWH_A`, `NORMIERUNGSFAKTOR_300_KWH_K`, `NORMIERUNGSFAKTOR_1_000_000_KW`</Werte> |
| <span className="hbs-g hbs-e1">[tagesmitteltemperatur](/bo4e/202604/com/Lastprofil#tagesmitteltemperatur)</span> | — | [Tagesmitteltemperatur](/bo4e/202604/com/Tagesmitteltemperatur) |
| <span className="hbs-f hbs-e2">[berechnungTagesmitteltemperatur](/bo4e/202604/com/Tagesmitteltemperatur#berechnungtagesmitteltemperatur)</span> | Berechnungsmethode | [Enum Berechnungsmethode](/bo4e/202604/enum/Berechnungsmethode)<br/><Werte>`24H_MITTELWERT`, `VOM_ANBIETER_ZUR_VERFUEGUNG_GESTELLTE_AEQUIVALENTE_TAGESMITTELTEMPERATUR`, `AEQUIVALENTE_TAGESMITTELTEMPERATUR`</Werte> |
| <span className="hbs-f hbs-e2">[anteilA](/bo4e/202604/com/Tagesmitteltemperatur#anteila)</span> | Anteil A | number (float) |
| <span className="hbs-f hbs-e2">[anteilB](/bo4e/202604/com/Tagesmitteltemperatur#anteilb)</span> | Anteil B | number (float) |
| <span className="hbs-f hbs-e2">[anteilC](/bo4e/202604/com/Tagesmitteltemperatur#anteilc)</span> | Anteil C | number (float) |
| <span className="hbs-f hbs-e2">[anteilD](/bo4e/202604/com/Tagesmitteltemperatur#anteild)</span> | Anteil D | number (float) |
| <span className="hbs-f hbs-e2">[begrenzungstemperatur](/bo4e/202604/com/Tagesmitteltemperatur#begrenzungstemperatur)</span> | Begrenzungstemperatur | string |
| <span className="hbs-f hbs-e1">[begrenzungskonstante](/bo4e/202604/com/Lastprofil#begrenzungskonstante)</span> | Begrenzungskonstante | [Enum Begrenzungskonstante](/bo4e/202604/enum/Begrenzungskonstante)<br/><Werte>`BEGRENZUNGSKONSTANTE_0`, `BEGRENZUNGSKONSTANTE_1`</Werte> |
| <span className="hbs-g hbs-e0">[lastprofileBilanzierungsbeteiligter](/bo4e/202604/bo/Bilanzierung#lastprofilebilanzierungsbeteiligter) <span className="hbs-liste">[ ]</span></span> | Lastprofile des Bilanzierungsbeteiligten | [Lastprofil[]](/bo4e/202604/com/Lastprofil) |
| <span className="hbs-f hbs-e1">[bezeichnung](/bo4e/202604/com/Lastprofil#bezeichnung)</span> | Bezeichnung des Profils | string |
| <span className="hbs-f hbs-e1">[verfahren](/bo4e/202604/com/Lastprofil#verfahren)</span> | Profilverfahren | [Enum Profilverfahren](/bo4e/202604/enum/Profilverfahren)<br/><Werte>`SYNTHETISCH`, `ANALYTISCH`</Werte> |
| <span className="hbs-f hbs-e1">[profilart](/bo4e/202604/com/Lastprofil#profilart)</span> | Profilart | [Enum Profilart](/bo4e/202604/enum/Profilart)<br/><Werte>`ART_STANDARDLASTPROFIL`, `ART_TAGESPARAMETERABHAENGIGES_LASTPROFIL`, `ART_LASTPROFIL`</Werte> |
| <span className="hbs-f hbs-e1">[profilschar](/bo4e/202604/com/Lastprofil#profilschar)</span> | Profilschar des Profils | string |
| <span className="hbs-f hbs-e1">[einspeisung](/bo4e/202604/com/Lastprofil#einspeisung)</span> | Kennzeichen Einspeisung | boolean |
| <span className="hbs-f hbs-e1">[herausgeber](/bo4e/202604/com/Lastprofil#herausgeber)</span> | Herausgeber des Lastprofils | string |
| <span className="hbs-g hbs-e1">[tagesparameter](/bo4e/202604/com/Lastprofil#tagesparameter)</span> | — | [Tagesparameter](/bo4e/202604/com/Tagesparameter) |
| <span className="hbs-f hbs-e2">[klimazone](/bo4e/202604/com/Tagesparameter#klimazone)</span> | klimazone | string |
| <span className="hbs-f hbs-e2">[temperaturmessstelle](/bo4e/202604/com/Tagesparameter#temperaturmessstelle)</span> | temperaturmessstelle | string |
| <span className="hbs-f hbs-e2">[dienstanbieter](/bo4e/202604/com/Tagesparameter#dienstanbieter)</span> | dienstanbieter | string |
| <span className="hbs-f hbs-e2">[herausgeber](/bo4e/202604/com/Tagesparameter#herausgeber)</span> | Herausgeber | [Enum Herausgeber](/bo4e/202604/enum/Herausgeber)<br/><Werte>`NB`, `BDEW`, `TUM`</Werte> |
| <span className="hbs-f hbs-e1">[referenzprofilbezeichnung](/bo4e/202604/com/Lastprofil#referenzprofilbezeichnung)</span> | Bezeichnung des Referenzprofils | string |
| <span className="hbs-f hbs-e1">[referenzprofil](/bo4e/202604/com/Lastprofil#referenzprofil)</span> | Referenzprofil | string |
| <span className="hbs-f hbs-e1">[profiltyp](/bo4e/202604/com/Lastprofil#profiltyp)</span> | Profiltyp | [Enum Profiltyp](/bo4e/202604/enum/Profiltyp)<br/><Werte>`SLP_SEP`, `TLP_TEP`, `TEP`, `GEWERBE_ALLGEMEIN`, `GEWERBE_WERKTAGS_8_18_UHR`, `GEWERBE_MIT_STARKEM_BIS_UEBERWIEGENDEM_VERBRAUCH_IN_DEN_ABENDSTUNDEN`, `GEWERBE_DURCHLAUFEND`, `GEWERBE_LADEN_FRISEUR`, `GEWERBE_BAECKEREI_MIT_BACKSTUBE`, `GEWERBE_WOCHENENDBETRIEB`, `LANDWIRTSCHAFTSBETRIEBE_ALLGEMEIN`, `LANDWIRTSCHAFTSBETRIEBE_MIT_MILCHWIRTSCHAFT_NEBENERWERBS_TIERZUCHT`, `LANDWIRTSCHAFT_OHNE_MILCHVIEH`, `HAUSHALT`, `BANDLAST`, `UNTERBRECHBARE_VERBRAUCHSEINRICHTUNG`, `HEIZWAERMESPEICHER`, `STRASSENBELEUCHTUNG`, `PHOTOVOLTAIK_MARKTLOKATION`, `BLOCKHEIZKRAFTWERK`, `SONSTIGE_VERBRAUCHENDE_MARKTLOKATION`, `SONSTIGE_ERZEUGENDE_MARKTLOKATION`, `E_MOBILITAET_LADEPUNKT_IM_OEFFENTLICHEN_BEREICH`, `E_MOBILITAET_LADEPUNKT_EINES_HAUSHALTS`, `E_MOBILITAET_LADEPUNKT_EINES_GEWERBES`</Werte> |
| <span className="hbs-f hbs-e1">[normierungsfaktor](/bo4e/202604/com/Lastprofil#normierungsfaktor)</span> | Normierungsfaktor | [Enum Normierungsfaktor](/bo4e/202604/enum/Normierungsfaktor)<br/><Werte>`NORMIERUNGSFAKTOR_1_000_000_KWH_A`, `NORMIERUNGSFAKTOR_300_KWH_K`, `NORMIERUNGSFAKTOR_1_000_000_KW`</Werte> |
| <span className="hbs-g hbs-e1">[tagesmitteltemperatur](/bo4e/202604/com/Lastprofil#tagesmitteltemperatur)</span> | — | [Tagesmitteltemperatur](/bo4e/202604/com/Tagesmitteltemperatur) |
| <span className="hbs-f hbs-e2">[berechnungTagesmitteltemperatur](/bo4e/202604/com/Tagesmitteltemperatur#berechnungtagesmitteltemperatur)</span> | Berechnungsmethode | [Enum Berechnungsmethode](/bo4e/202604/enum/Berechnungsmethode)<br/><Werte>`24H_MITTELWERT`, `VOM_ANBIETER_ZUR_VERFUEGUNG_GESTELLTE_AEQUIVALENTE_TAGESMITTELTEMPERATUR`, `AEQUIVALENTE_TAGESMITTELTEMPERATUR`</Werte> |
| <span className="hbs-f hbs-e2">[anteilA](/bo4e/202604/com/Tagesmitteltemperatur#anteila)</span> | Anteil A | number (float) |
| <span className="hbs-f hbs-e2">[anteilB](/bo4e/202604/com/Tagesmitteltemperatur#anteilb)</span> | Anteil B | number (float) |
| <span className="hbs-f hbs-e2">[anteilC](/bo4e/202604/com/Tagesmitteltemperatur#anteilc)</span> | Anteil C | number (float) |
| <span className="hbs-f hbs-e2">[anteilD](/bo4e/202604/com/Tagesmitteltemperatur#anteild)</span> | Anteil D | number (float) |
| <span className="hbs-f hbs-e2">[begrenzungstemperatur](/bo4e/202604/com/Tagesmitteltemperatur#begrenzungstemperatur)</span> | Begrenzungstemperatur | string |
| <span className="hbs-f hbs-e1">[begrenzungskonstante](/bo4e/202604/com/Lastprofil#begrenzungskonstante)</span> | Begrenzungskonstante | [Enum Begrenzungskonstante](/bo4e/202604/enum/Begrenzungskonstante)<br/><Werte>`BEGRENZUNGSKONSTANTE_0`, `BEGRENZUNGSKONSTANTE_1`</Werte> |
| <span className="hbs-f hbs-e0">[detailsPrognosegrundlage](/bo4e/202604/bo/Bilanzierung#detailsprognosegrundlage) <span className="hbs-liste">[ ]</span></span> | Prognosegrundlage - Besteht der Bedarf ein tagesparameteräbhängiges Lastprofil mit gemeinsamer Messung anzugeben, so ist dies über die 2 -malige Wiederholung des CAV Segments mit der Angabe der Codes E02 und E14 möglich. | [Enum Profiltyp[]](/bo4e/202604/enum/Profiltyp)<br/><Werte>`SLP_SEP`, `TLP_TEP`, `TEP`, `GEWERBE_ALLGEMEIN`, `GEWERBE_WERKTAGS_8_18_UHR`, `GEWERBE_MIT_STARKEM_BIS_UEBERWIEGENDEM_VERBRAUCH_IN_DEN_ABENDSTUNDEN`, `GEWERBE_DURCHLAUFEND`, `GEWERBE_LADEN_FRISEUR`, `GEWERBE_BAECKEREI_MIT_BACKSTUBE`, `GEWERBE_WOCHENENDBETRIEB`, `LANDWIRTSCHAFTSBETRIEBE_ALLGEMEIN`, `LANDWIRTSCHAFTSBETRIEBE_MIT_MILCHWIRTSCHAFT_NEBENERWERBS_TIERZUCHT`, `LANDWIRTSCHAFT_OHNE_MILCHVIEH`, `HAUSHALT`, `BANDLAST`, `UNTERBRECHBARE_VERBRAUCHSEINRICHTUNG`, `HEIZWAERMESPEICHER`, `STRASSENBELEUCHTUNG`, `PHOTOVOLTAIK_MARKTLOKATION`, `BLOCKHEIZKRAFTWERK`, `SONSTIGE_VERBRAUCHENDE_MARKTLOKATION`, `SONSTIGE_ERZEUGENDE_MARKTLOKATION`, `E_MOBILITAET_LADEPUNKT_IM_OEFFENTLICHEN_BEREICH`, `E_MOBILITAET_LADEPUNKT_EINES_HAUSHALTS`, `E_MOBILITAET_LADEPUNKT_EINES_GEWERBES`</Werte> |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### marktlokationsId

5 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55074](/schnittstellen/202604/pruefi/UTILMD/PI_55074) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55075](/schnittstellen/202604/pruefi/UTILMD/PI_55075) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |

### aggregationsverantwortung

7 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55126](/schnittstellen/202604/pruefi/UTILMD/PI_55126) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55156](/schnittstellen/202604/pruefi/UTILMD/PI_55156) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55672](/schnittstellen/202604/pruefi/UTILMD/PI_55672) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55673](/schnittstellen/202604/pruefi/UTILMD/PI_55673) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |

### zeitreihentyp

10 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55074](/schnittstellen/202604/pruefi/UTILMD/PI_55074) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55075](/schnittstellen/202604/pruefi/UTILMD/PI_55075) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55126](/schnittstellen/202604/pruefi/UTILMD/PI_55126) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55156](/schnittstellen/202604/pruefi/UTILMD/PI_55156) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55613](/schnittstellen/202604/pruefi/UTILMD/PI_55613) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55614](/schnittstellen/202604/pruefi/UTILMD/PI_55614) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55670](/schnittstellen/202604/pruefi/UTILMD/PI_55670) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55672](/schnittstellen/202604/pruefi/UTILMD/PI_55672) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55673](/schnittstellen/202604/pruefi/UTILMD/PI_55673) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55674](/schnittstellen/202604/pruefi/UTILMD/PI_55674) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |

### prognosegrundlage

31 Verwendung(en) in den Nachrichtentypen ORDERS, UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_17120](/schnittstellen/202604/pruefi/ORDERS/PI_17120) | Prüfi | ORDERS | stammdaten › BILANZIERUNG |
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG |
| [PI_44019](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44019) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG |
| [PI_44020](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44020) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG |
| [PI_44021](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44021) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG |
| [PI_44035](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44035) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG |
| [PI_44103](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44103) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG |
| [PI_44104](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44104) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG |
| [PI_44123](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44123) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG |
| [PI_44139](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44139) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG |
| [PI_44142](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44142) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG |
| [PI_44156](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44156) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG |
| [PI_44157](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44157) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG |
| [PI_55013](/schnittstellen/202604/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55035](/schnittstellen/202604/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55060](/schnittstellen/202604/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55095](/schnittstellen/202604/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55126](/schnittstellen/202604/pruefi/UTILMD/PI_55126) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55156](/schnittstellen/202604/pruefi/UTILMD/PI_55156) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55613](/schnittstellen/202604/pruefi/UTILMD/PI_55613) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55614](/schnittstellen/202604/pruefi/UTILMD/PI_55614) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55628](/schnittstellen/202604/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55634](/schnittstellen/202604/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55672](/schnittstellen/202604/pruefi/UTILMD/PI_55672) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55673](/schnittstellen/202604/pruefi/UTILMD/PI_55673) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55674](/schnittstellen/202604/pruefi/UTILMD/PI_55674) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |

### bilanzierungsbeginn

8 Verwendung(en) in den Nachrichtentypen UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG |
| [PI_44019](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44019) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG |
| [PI_44020](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44020) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG |
| [PI_44021](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44021) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG |
| [PI_44103](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44103) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG |
| [PI_44104](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44104) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG |

### bilanzierungsende

13 Verwendung(en) in den Nachrichtentypen UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG |
| [PI_44005](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44005) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG |
| [PI_44007](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44007) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG |
| [PI_44008](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44008) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG |
| [PI_44019](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44019) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG |
| [PI_44020](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44020) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG |
| [PI_44021](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44021) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG |
| [PI_44037](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44037) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG |
| [PI_44038](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44038) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG |
| [PI_44103](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44103) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG |
| [PI_44104](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44104) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG |

### bilanzkreis

10 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55074](/schnittstellen/202604/pruefi/UTILMD/PI_55074) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55075](/schnittstellen/202604/pruefi/UTILMD/PI_55075) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55126](/schnittstellen/202604/pruefi/UTILMD/PI_55126) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55156](/schnittstellen/202604/pruefi/UTILMD/PI_55156) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55613](/schnittstellen/202604/pruefi/UTILMD/PI_55613) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55614](/schnittstellen/202604/pruefi/UTILMD/PI_55614) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55670](/schnittstellen/202604/pruefi/UTILMD/PI_55670) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55672](/schnittstellen/202604/pruefi/UTILMD/PI_55672) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55673](/schnittstellen/202604/pruefi/UTILMD/PI_55673) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55674](/schnittstellen/202604/pruefi/UTILMD/PI_55674) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |

### fallgruppenzuordnung

13 Verwendung(en) in den Nachrichtentypen UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_44001](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44001) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG |
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG |
| [PI_44019](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44019) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG |
| [PI_44020](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44020) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG |
| [PI_44021](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44021) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG |
| [PI_44035](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44035) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG |
| [PI_44103](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44103) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG |
| [PI_44104](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44104) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG |
| [PI_44123](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44123) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG |
| [PI_44156](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44156) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG |
| [PI_44157](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44157) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG |

### abwicklungsmodell

5 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55628](/schnittstellen/202604/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55634](/schnittstellen/202604/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |

### datenqualitaet

8 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55126](/schnittstellen/202604/pruefi/UTILMD/PI_55126) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55156](/schnittstellen/202604/pruefi/UTILMD/PI_55156) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55613](/schnittstellen/202604/pruefi/UTILMD/PI_55613) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55614](/schnittstellen/202604/pruefi/UTILMD/PI_55614) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55628](/schnittstellen/202604/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55634](/schnittstellen/202604/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55672](/schnittstellen/202604/pruefi/UTILMD/PI_55672) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55673](/schnittstellen/202604/pruefi/UTILMD/PI_55673) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |

### detailsPrognosegrundlage

15 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55013](/schnittstellen/202604/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55035](/schnittstellen/202604/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55060](/schnittstellen/202604/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55095](/schnittstellen/202604/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55126](/schnittstellen/202604/pruefi/UTILMD/PI_55126) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55156](/schnittstellen/202604/pruefi/UTILMD/PI_55156) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55613](/schnittstellen/202604/pruefi/UTILMD/PI_55613) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55614](/schnittstellen/202604/pruefi/UTILMD/PI_55614) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55628](/schnittstellen/202604/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55634](/schnittstellen/202604/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55672](/schnittstellen/202604/pruefi/UTILMD/PI_55672) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |
| [PI_55673](/schnittstellen/202604/pruefi/UTILMD/PI_55673) | Prüfi | UTILMD | stammdaten › BILANZIERUNG |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
