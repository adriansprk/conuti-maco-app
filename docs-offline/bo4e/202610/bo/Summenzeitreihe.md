# Summenzeitreihe
<span hidden data-pagefind-meta={"title:Summenzeitreihe — BO4E-Geschäftsobjekt (FV 202610)"} />

BO4E-Geschäftsobjekt · 21 Felder · 4 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="botyp"></a>`boTyp` <span className="hbs-pflicht">\*</span> | [Enum BOTyp](/bo4e/202610/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> | Typ des BO |
| <a id="versionstruktur"></a>`versionStruktur` <span className="hbs-pflicht">\*</span> | string | versionStruktur |
| <a id="zaehlpunktid"></a>`zaehlpunktId` | string | ID des Zaehlpunkts |
| <a id="versionzeitreihe"></a>`versionZeitreihe` | string | Version der Zeitreihe |
| <a id="bilanzkreis"></a>`bilanzkreis` | string | Bilanzkreis |
| <a id="bilanzkreisan"></a>`bilanzkreisAn` | string | BilanzkreisAn |
| <a id="bilanzkreisvon"></a>`bilanzkreisVon` | string | BilanzkreisVon |
| <a id="bilanzierteenergiemenge"></a>`bilanzierteEnergiemenge` | [Menge](/bo4e/202610/com/Menge) | Bilanzierte Energiemenge |
| <a id="bilanzierteausfallmenge"></a>`bilanzierteAusfallmenge` | [Menge](/bo4e/202610/com/Menge) | Bilanzierte Ausfallmenge |
| <a id="bilanzierungsbeginn"></a>`bilanzierungsbeginn` | string (date-time) | bilanzierungsbeginn |
| <a id="bilanzierungsgebiet"></a>`bilanzierungsgebiet` | string[] | Bilanzierungsgebiet(e) |
| <a id="bezeichnung"></a>`bezeichnung` | [Enum Bezeichnung](/bo4e/202610/enum/Bezeichnung)<br/><Werte>`BG_SZR_B`, `BG_SZR_C`, `BK_SZR_A`, `BK_SZR_B_RZ`, `BK_SZR_B_BG`, `BK_SZR_C`, `LF_SZR_A`, `LF_SZR_B_RZ`, `LF_SZR_B_BG`, `DZUE`, `NZR`, `ASZR`, `NGZ`, `BK_SZR_EMOB`</Werte> | Bezeichnung |
| <a id="verantwortlichemarktrolle"></a>`verantwortlicheMarktrolle` | [Enum Marktrolle](/bo4e/202610/enum/Marktrolle)<br/><Werte>`NB`, `LF`, `MSB`, `MSBA`, `GMSB`, `MDL`, `DL`, `BKV`, `UENB`, `KUNDE-SELBST-NN`, `MGV`, `EIV`, `RB`, `KUNDE`, `INTERESSENT`, `KN`, `UBA`, `BIKO`, `ESA`</Werte> | Verantwortliche Marktrolle |
| <a id="regelzone"></a>`regelzone` | string | Regelzone |
| <a id="zeitreihentyp"></a>`zeitreihentyp` | [Enum Zeitreihentyp](/bo4e/202610/enum/Zeitreihentyp)<br/><Werte>`EGS`, `LGS`, `NZR`, `SES`, `SLS`, `TES`, `TLS`, `SLS_TLS`, `SES_TES`, `AUS`, `BAS`, `DBA`, `DZR`, `DZÜ`, `FPE`, `FPI`, `SRE`, `SRI`, `VZR`, `BIL`, `BIP`, `BIT`, `GAL`, `GAP`, `GAT`, `GEL`, `GEP`, `GET`, `SOL`, `SOP`, `SOT`, `WFL`, `WFP`, `WNL`, `WNP`, `WNT`, `WAL`, `WAP`, `WAT`, `AU1`, `BI1`, `BI2`, `BI3`, `GAA`, `GAB`, `GAC`, `GE1`, `GE2`, `GE3`, `SO1`, `SO2`, `SO3`, `WF1`, `WF2`, `WF3`, `WN1`, `WN2`, `WN3`, `WAA`, `WAB`, `WAC`, `AUSFALLARBEITSSUMME`, `BILANZKREISABWEICHUNGSSALDO`, `DIFFERENZZEITREIHE`, `DELTAZEITREIHE`, `DELTAZEITREIHENUEBERTRAG`, `FAHRPLANENTNAHMESUMME`, `FAHRPLANEINSPEISESUMME`, `UEBERFUEHRUNGSZEITREIHE_SEKUNDAERREGELLEISTUNG_EXPORT`, `UEBERFUEHRUNGSZEITREIHE_SEKUNDAERREGELLEISTUNG_IMPORT`, `VERLUSTZEITREIHE`, `EE_EINSPEISESUMME_BIOMASSE_BIOGAS_GEMESSEN`, `EE_EINSPEISESUMME_BIOMASSE_BIOGAS_EINSPEISEPROFIL`, `EE_EINSPEISESUMME_BIOMASSE_BIOGAS_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`, `EE_EINSPEISESUMME_DEPONIE_KLAER_GRUBENGAS_GEMESSEN`, `EE_EINSPEISESUMME_DEPONIE_KLAER_GRUBENGAS_EINSPEISEPROFIL`, `EE_EINSPEISESUMME_DEPONIE_KLAER_GRUBENGAS_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`, `EE_EINSPEISESUMME_GEOTHERMIE_GEMESSEN`, `EE_EINSPEISESUMME_GEOTHERMIE_EINSPEISEPROFIL`, `EE_EINSPEISESUMME_GEOTHERMIE_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`, `EE_EINSPEISESUMME_SOLAR_GEMESSEN`, `EE_EINSPEISESUMME_SOLAR_EINSPEISEPROFIL`, `EE_EINSPEISESUMME_SOLAR_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`, `EE_EINSPEISESUMME_WIND_OFFSHORE_GEMESSEN`, `EE_EINSPEISESUMME_WIND_OFFSHORE_EINSPEISEPROFIL`, `EE_EINSPEISESUMME_WIND_OFFSHORE_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`, `EE_EINSPEISESUMME_WIND_ONSHORE_GEMESSEN`, `EE_EINSPEISESUMME_WIND_ONSHORE_EINSPEISEPROFIL`, `EE_EINSPEISESUMME_WIND_ONSHORE_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`, `EE_EINSPEISESUMME_WASSERKRAFT_GEMESSEN`, `EE_EINSPEISESUMME_WASSERKRAFT_EINSPEISEPROFIL`, `EE_EINSPEISESUMME_WASSERKRAFT_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`, `EEG_UEBERFUEHRUNG_AUSFALLARBEIT`, `EEG_UEBERFUEHRUNG_BIOMASSE_BIOGAS_WERTE`, `EEG_UEBERFUEHRUNG_BIOMASSE_BIOGAS_STANDARDEINSPEISEPROFIL`, `EEG_UEBERFUEHRUNG_BIOMASSE_BIOGAS_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`, `EEG_UEBERFUEHRUNG_DEPONIE_KLAER_GRUBENGAS_WERTE`, `EEG_UEBERFUEHRUNG_DEPONIE_KLAER_GRUBENGAS_STANDARDEINSPEISEPROFIL`, `EEG_UEBERFUEHRUNG_DEPONIE_KLAER_GRUBENGAS_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`, `EEG_UEBERFUEHRUNG_GEOTHERMIE_WERTE`, `EEG_UEBERFUEHRUNG_GEOTHERMIE_STANDARDEINSPEISEPROFIL`, `EEG_UEBERFUEHRUNG_GEOTHERMIE_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`, `EEG_UEBERFUEHRUNG_SOLAR_WERTE`, `EEG_UEBERFUEHRUNG_SOLAR_STANDARDEINSPEISEPROFIL`, `EEG_UEBERFUEHRUNG_SOLAR_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`, `EEG_UEBERFUEHRUNG_WIND_OFFSHORE_WERTE`, `EEG_UEBERFUEHRUNG_WIND_OFFSHORE_STANDARDEINSPEISEPROFIL`, `EEG_UEBERFUEHRUNG_WIND_OFFSHORE_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`, `EEG_UEBERFUEHRUNG_WIND_ONSHORE_WERTE`, `EEG_UEBERFUEHRUNG_WIND_ONSHORE_STANDARDEINSPEISEPROFIL`, `EEG_UEBERFUEHRUNG_WIND_ONSHORE_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`, `EEG_UEBERFUEHRUNG_WASSERKRAFT_WERTE`, `EEG_UEBERFUEHRUNG_WASSERKRAFT_STANDARDEINSPEISEPROFIL`, `EEG_UEBERFUEHRUNG_WASSERKRAFT_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</Werte> | Zeitreihentyp |
| <a id="bezugszeitraum"></a>`bezugszeitraum` | [Enum Bezugszeitraum](/bo4e/202610/enum/Bezugszeitraum)<br/><Werte>`TAG`, `MONAT`</Werte> | Bezugszeitraum der Zeitreihe |
| <a id="netzebene"></a>`netzebene` | [Enum Netzebene](/bo4e/202610/enum/Netzebene)<br/><Werte>`NSP`, `MSP`, `HSP`, `HSS`, `MSP_NSP_UMSP`, `HSP_MSP_UMSP`, `HSS_HSP_UMSP`, `HD`, `MD`, `ND`</Werte> | Netzebene |
| <a id="umspannung"></a>`umspannung` | [Enum Netzebene](/bo4e/202610/enum/Netzebene)<br/><Werte>`NSP`, `MSP`, `HSP`, `HSS`, `MSP_NSP_UMSP`, `HSP_MSP_UMSP`, `HSS_HSP_UMSP`, `HD`, `MD`, `ND`</Werte> | Umspannung |
| <a id="datenstatuszeitreihe"></a>`datenstatusZeitreihe` | [Enum DatenstatusZeitreihe](/bo4e/202610/enum/DatenstatusZeitreihe)<br/><Werte>`ABRECHNUNGSDATEN`, `ABGERECHNETE_DATEN`, `ABRECHNUNGSDATEN_KORREKTUR_BKA`, `ABGERECHNETE_DATEN_KORREKTUR_BKA`</Werte> | Datenstatus der Zeitreihe |
| <a id="zuordnungsregel"></a>`zuordnungsregel` | [Enum Zuordnungsregel](/bo4e/202610/enum/Zuordnungsregel)<br/><Werte>`SELBE_LIEFERRICHTUNG`, `ENTGEGENGESETZTE_LIEFERRICHTUNG`</Werte> | Zuordnungsregel der Summenzeitreihe |
| <a id="zeitreihenprodukt"></a>`zeitreihenprodukt` | [Zeitreihenprodukt[]](/bo4e/202610/com/Zeitreihenprodukt) | Liste der Zeitreihenprodukte |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[boTyp](/bo4e/202610/bo/Summenzeitreihe#botyp) <span className="hbs-pflicht">\*</span></span> | Typ des BO | [Enum BOTyp](/bo4e/202610/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> |
| <span className="hbs-f hbs-e0">[versionStruktur](/bo4e/202610/bo/Summenzeitreihe#versionstruktur) <span className="hbs-pflicht">\*</span></span> | versionStruktur | string |
| <span className="hbs-f hbs-e0">[zaehlpunktId](/bo4e/202610/bo/Summenzeitreihe#zaehlpunktid)</span> | ID des Zaehlpunkts | string |
| <span className="hbs-f hbs-e0">[versionZeitreihe](/bo4e/202610/bo/Summenzeitreihe#versionzeitreihe)</span> | Version der Zeitreihe | string |
| <span className="hbs-f hbs-e0">[bilanzkreis](/bo4e/202610/bo/Summenzeitreihe#bilanzkreis)</span> | Bilanzkreis | string |
| <span className="hbs-f hbs-e0">[bilanzkreisAn](/bo4e/202610/bo/Summenzeitreihe#bilanzkreisan)</span> | BilanzkreisAn | string |
| <span className="hbs-f hbs-e0">[bilanzkreisVon](/bo4e/202610/bo/Summenzeitreihe#bilanzkreisvon)</span> | BilanzkreisVon | string |
| <span className="hbs-g hbs-e0">[bilanzierteEnergiemenge](/bo4e/202610/bo/Summenzeitreihe#bilanzierteenergiemenge)</span> | Bilanzierte Energiemenge | [Menge](/bo4e/202610/com/Menge) |
| <span className="hbs-f hbs-e1">[wert](/bo4e/202610/com/Menge#wert)</span> | Wert | number (float) |
| <span className="hbs-f hbs-e1">[einheit](/bo4e/202610/com/Menge#einheit)</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202610/enum/Mengeneinheit)<br/><Werte>`W`, `WH`, `KW`, `KWH`, `KVARH`, `MW`, `MWH`, `STUECK`, `KUBIKMETER`, `STUNDE`, `TAG`, `MONAT`, `JAHR`, `PROZENT`, `ANZAHL`, `VAR`, `KVAR`, `VARH`, `KWHK`, `Z16`, `KWT`, `WATT_PRO_QUADRATMETER`, `METER_PRO_SEKUNDE`</Werte> |
| <span className="hbs-f hbs-e1">[startdatum](/bo4e/202610/com/Menge#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e1">[enddatum](/bo4e/202610/com/Menge#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-g hbs-e0">[bilanzierteAusfallmenge](/bo4e/202610/bo/Summenzeitreihe#bilanzierteausfallmenge)</span> | Bilanzierte Ausfallmenge | [Menge](/bo4e/202610/com/Menge) |
| <span className="hbs-f hbs-e1">[wert](/bo4e/202610/com/Menge#wert)</span> | Wert | number (float) |
| <span className="hbs-f hbs-e1">[einheit](/bo4e/202610/com/Menge#einheit)</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202610/enum/Mengeneinheit)<br/><Werte>`W`, `WH`, `KW`, `KWH`, `KVARH`, `MW`, `MWH`, `STUECK`, `KUBIKMETER`, `STUNDE`, `TAG`, `MONAT`, `JAHR`, `PROZENT`, `ANZAHL`, `VAR`, `KVAR`, `VARH`, `KWHK`, `Z16`, `KWT`, `WATT_PRO_QUADRATMETER`, `METER_PRO_SEKUNDE`</Werte> |
| <span className="hbs-f hbs-e1">[startdatum](/bo4e/202610/com/Menge#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e1">[enddatum](/bo4e/202610/com/Menge#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-f hbs-e0">[bilanzierungsbeginn](/bo4e/202610/bo/Summenzeitreihe#bilanzierungsbeginn)</span> | bilanzierungsbeginn | string (date-time) |
| <span className="hbs-f hbs-e0">[bilanzierungsgebiet](/bo4e/202610/bo/Summenzeitreihe#bilanzierungsgebiet) <span className="hbs-liste">[ ]</span></span> | Bilanzierungsgebiet(e) | string[] |
| <span className="hbs-f hbs-e0">[bezeichnung](/bo4e/202610/bo/Summenzeitreihe#bezeichnung)</span> | Bezeichnung | [Enum Bezeichnung](/bo4e/202610/enum/Bezeichnung)<br/><Werte>`BG_SZR_B`, `BG_SZR_C`, `BK_SZR_A`, `BK_SZR_B_RZ`, `BK_SZR_B_BG`, `BK_SZR_C`, `LF_SZR_A`, `LF_SZR_B_RZ`, `LF_SZR_B_BG`, `DZUE`, `NZR`, `ASZR`, `NGZ`, `BK_SZR_EMOB`</Werte> |
| <span className="hbs-f hbs-e0">[verantwortlicheMarktrolle](/bo4e/202610/bo/Summenzeitreihe#verantwortlichemarktrolle)</span> | Verantwortliche Marktrolle | [Enum Marktrolle](/bo4e/202610/enum/Marktrolle)<br/><Werte>`NB`, `LF`, `MSB`, `MSBA`, `GMSB`, `MDL`, `DL`, `BKV`, `UENB`, `KUNDE-SELBST-NN`, `MGV`, `EIV`, `RB`, `KUNDE`, `INTERESSENT`, `KN`, `UBA`, `BIKO`, `ESA`</Werte> |
| <span className="hbs-f hbs-e0">[regelzone](/bo4e/202610/bo/Summenzeitreihe#regelzone)</span> | Regelzone | string |
| <span className="hbs-f hbs-e0">[zeitreihentyp](/bo4e/202610/bo/Summenzeitreihe#zeitreihentyp)</span> | Zeitreihentyp | [Enum Zeitreihentyp](/bo4e/202610/enum/Zeitreihentyp)<br/><Werte>`EGS`, `LGS`, `NZR`, `SES`, `SLS`, `TES`, `TLS`, `SLS_TLS`, `SES_TES`, `AUS`, `BAS`, `DBA`, `DZR`, `DZÜ`, `FPE`, `FPI`, `SRE`, `SRI`, `VZR`, `BIL`, `BIP`, `BIT`, `GAL`, `GAP`, `GAT`, `GEL`, `GEP`, `GET`, `SOL`, `SOP`, `SOT`, `WFL`, `WFP`, `WNL`, `WNP`, `WNT`, `WAL`, `WAP`, `WAT`, `AU1`, `BI1`, `BI2`, `BI3`, `GAA`, `GAB`, `GAC`, `GE1`, `GE2`, `GE3`, `SO1`, `SO2`, `SO3`, `WF1`, `WF2`, `WF3`, `WN1`, `WN2`, `WN3`, `WAA`, `WAB`, `WAC`, `AUSFALLARBEITSSUMME`, `BILANZKREISABWEICHUNGSSALDO`, `DIFFERENZZEITREIHE`, `DELTAZEITREIHE`, `DELTAZEITREIHENUEBERTRAG`, `FAHRPLANENTNAHMESUMME`, `FAHRPLANEINSPEISESUMME`, `UEBERFUEHRUNGSZEITREIHE_SEKUNDAERREGELLEISTUNG_EXPORT`, `UEBERFUEHRUNGSZEITREIHE_SEKUNDAERREGELLEISTUNG_IMPORT`, `VERLUSTZEITREIHE`, `EE_EINSPEISESUMME_BIOMASSE_BIOGAS_GEMESSEN`, `EE_EINSPEISESUMME_BIOMASSE_BIOGAS_EINSPEISEPROFIL`, `EE_EINSPEISESUMME_BIOMASSE_BIOGAS_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`, `EE_EINSPEISESUMME_DEPONIE_KLAER_GRUBENGAS_GEMESSEN`, `EE_EINSPEISESUMME_DEPONIE_KLAER_GRUBENGAS_EINSPEISEPROFIL`, `EE_EINSPEISESUMME_DEPONIE_KLAER_GRUBENGAS_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`, `EE_EINSPEISESUMME_GEOTHERMIE_GEMESSEN`, `EE_EINSPEISESUMME_GEOTHERMIE_EINSPEISEPROFIL`, `EE_EINSPEISESUMME_GEOTHERMIE_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`, `EE_EINSPEISESUMME_SOLAR_GEMESSEN`, `EE_EINSPEISESUMME_SOLAR_EINSPEISEPROFIL`, `EE_EINSPEISESUMME_SOLAR_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`, `EE_EINSPEISESUMME_WIND_OFFSHORE_GEMESSEN`, `EE_EINSPEISESUMME_WIND_OFFSHORE_EINSPEISEPROFIL`, `EE_EINSPEISESUMME_WIND_OFFSHORE_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`, `EE_EINSPEISESUMME_WIND_ONSHORE_GEMESSEN`, `EE_EINSPEISESUMME_WIND_ONSHORE_EINSPEISEPROFIL`, `EE_EINSPEISESUMME_WIND_ONSHORE_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`, `EE_EINSPEISESUMME_WASSERKRAFT_GEMESSEN`, `EE_EINSPEISESUMME_WASSERKRAFT_EINSPEISEPROFIL`, `EE_EINSPEISESUMME_WASSERKRAFT_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`, `EEG_UEBERFUEHRUNG_AUSFALLARBEIT`, `EEG_UEBERFUEHRUNG_BIOMASSE_BIOGAS_WERTE`, `EEG_UEBERFUEHRUNG_BIOMASSE_BIOGAS_STANDARDEINSPEISEPROFIL`, `EEG_UEBERFUEHRUNG_BIOMASSE_BIOGAS_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`, `EEG_UEBERFUEHRUNG_DEPONIE_KLAER_GRUBENGAS_WERTE`, `EEG_UEBERFUEHRUNG_DEPONIE_KLAER_GRUBENGAS_STANDARDEINSPEISEPROFIL`, `EEG_UEBERFUEHRUNG_DEPONIE_KLAER_GRUBENGAS_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`, `EEG_UEBERFUEHRUNG_GEOTHERMIE_WERTE`, `EEG_UEBERFUEHRUNG_GEOTHERMIE_STANDARDEINSPEISEPROFIL`, `EEG_UEBERFUEHRUNG_GEOTHERMIE_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`, `EEG_UEBERFUEHRUNG_SOLAR_WERTE`, `EEG_UEBERFUEHRUNG_SOLAR_STANDARDEINSPEISEPROFIL`, `EEG_UEBERFUEHRUNG_SOLAR_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`, `EEG_UEBERFUEHRUNG_WIND_OFFSHORE_WERTE`, `EEG_UEBERFUEHRUNG_WIND_OFFSHORE_STANDARDEINSPEISEPROFIL`, `EEG_UEBERFUEHRUNG_WIND_OFFSHORE_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`, `EEG_UEBERFUEHRUNG_WIND_ONSHORE_WERTE`, `EEG_UEBERFUEHRUNG_WIND_ONSHORE_STANDARDEINSPEISEPROFIL`, `EEG_UEBERFUEHRUNG_WIND_ONSHORE_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`, `EEG_UEBERFUEHRUNG_WASSERKRAFT_WERTE`, `EEG_UEBERFUEHRUNG_WASSERKRAFT_STANDARDEINSPEISEPROFIL`, `EEG_UEBERFUEHRUNG_WASSERKRAFT_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</Werte> |
| <span className="hbs-f hbs-e0">[bezugszeitraum](/bo4e/202610/bo/Summenzeitreihe#bezugszeitraum)</span> | Bezugszeitraum der Zeitreihe | [Enum Bezugszeitraum](/bo4e/202610/enum/Bezugszeitraum)<br/><Werte>`TAG`, `MONAT`</Werte> |
| <span className="hbs-f hbs-e0">[netzebene](/bo4e/202610/bo/Summenzeitreihe#netzebene)</span> | Netzebene | [Enum Netzebene](/bo4e/202610/enum/Netzebene)<br/><Werte>`NSP`, `MSP`, `HSP`, `HSS`, `MSP_NSP_UMSP`, `HSP_MSP_UMSP`, `HSS_HSP_UMSP`, `HD`, `MD`, `ND`</Werte> |
| <span className="hbs-f hbs-e0">[umspannung](/bo4e/202610/bo/Summenzeitreihe#umspannung)</span> | Umspannung | [Enum Netzebene](/bo4e/202610/enum/Netzebene)<br/><Werte>`NSP`, `MSP`, `HSP`, `HSS`, `MSP_NSP_UMSP`, `HSP_MSP_UMSP`, `HSS_HSP_UMSP`, `HD`, `MD`, `ND`</Werte> |
| <span className="hbs-f hbs-e0">[datenstatusZeitreihe](/bo4e/202610/bo/Summenzeitreihe#datenstatuszeitreihe)</span> | Datenstatus der Zeitreihe | [Enum DatenstatusZeitreihe](/bo4e/202610/enum/DatenstatusZeitreihe)<br/><Werte>`ABRECHNUNGSDATEN`, `ABGERECHNETE_DATEN`, `ABRECHNUNGSDATEN_KORREKTUR_BKA`, `ABGERECHNETE_DATEN_KORREKTUR_BKA`</Werte> |
| <span className="hbs-f hbs-e0">[zuordnungsregel](/bo4e/202610/bo/Summenzeitreihe#zuordnungsregel)</span> | Zuordnungsregel der Summenzeitreihe | [Enum Zuordnungsregel](/bo4e/202610/enum/Zuordnungsregel)<br/><Werte>`SELBE_LIEFERRICHTUNG`, `ENTGEGENGESETZTE_LIEFERRICHTUNG`</Werte> |
| <span className="hbs-g hbs-e0">[zeitreihenprodukt](/bo4e/202610/bo/Summenzeitreihe#zeitreihenprodukt) <span className="hbs-liste">[ ]</span></span> | Liste der Zeitreihenprodukte | [Zeitreihenprodukt[]](/bo4e/202610/com/Zeitreihenprodukt) |
| <span className="hbs-f hbs-e1">[identifikation](/bo4e/202610/com/Zeitreihenprodukt#identifikation)</span> | Identifikation des Zeitreihenprodukts, z.B. OBIS-Kennzahl | string |
| <span className="hbs-f hbs-e1">[korrekturfaktor](/bo4e/202610/com/Zeitreihenprodukt#korrekturfaktor)</span> | Gibt ggf. einen Korrekturfaktor für die Menge an. | number (float) |
| <span className="hbs-g hbs-e1">[energiemenge](/bo4e/202610/com/Zeitreihenprodukt#energiemenge)</span> | Energiemenge des Zeitreihenprodukts im Bezugszeitraum | [Verbrauch](/bo4e/202610/com/Verbrauch) |
| <span className="hbs-f hbs-e2">[startdatum](/bo4e/202610/com/Verbrauch#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e2">[enddatum](/bo4e/202610/com/Verbrauch#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-f hbs-e2">[wertermittlungsverfahren](/bo4e/202610/com/Verbrauch#wertermittlungsverfahren)</span> | Wertermittlungsverfahren | [Enum Wertermittlungsverfahren](/bo4e/202610/enum/Wertermittlungsverfahren)<br/><Werte>`PROGNOSE`, `MESSUNG`</Werte> |
| <span className="hbs-f hbs-e2">[messwertstatus](/bo4e/202610/com/Verbrauch#messwertstatus)</span> | Der Status eines Zählerstandes | [Enum Messwertstatus](/bo4e/202610/enum/Messwertstatus)<br/><Werte>`ABGELESEN`, `ERSATZWERT`, `VORSCHLAGSWERT`, `NICHT_VERWENDBAR`, `PROGNOSEWERT`, `ENERGIEMENGESUMMIERT`, `VOLAEUFIGERWERT`, `FEHLT`, `ANGABE_FUER_LIEFERSCHEIN`, `GRUNDLAGE_POG_ERMITTLUNG`</Werte> |
| <span className="hbs-f hbs-e2">[obiskennzahl](/bo4e/202610/com/Verbrauch#obiskennzahl)</span> | obiskennzahl | string |
| <span className="hbs-f hbs-e2">[wert](/bo4e/202610/com/Verbrauch#wert)</span> | wert | number (float) |
| <span className="hbs-f hbs-e2">[einheit](/bo4e/202610/com/Verbrauch#einheit)</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202610/enum/Mengeneinheit)<br/><Werte>`W`, `WH`, `KW`, `KWH`, `KVARH`, `MW`, `MWH`, `STUECK`, `KUBIKMETER`, `STUNDE`, `TAG`, `MONAT`, `JAHR`, `PROZENT`, `ANZAHL`, `VAR`, `KVAR`, `VARH`, `KWHK`, `Z16`, `KWT`, `WATT_PRO_QUADRATMETER`, `METER_PRO_SEKUNDE`</Werte> |
| <span className="hbs-f hbs-e2">[type](/bo4e/202610/com/Verbrauch#type)</span> | Verbrauchsmengetyp | [Enum Verbrauchsmengetyp](/bo4e/202610/enum/Verbrauchsmengetyp)<br/><Werte>`ARBEITLEISTUNGTAGESPARAMETERABHMALO`, `VERANSCHLAGTEJAHRESMENGE`, `TUMKUNDENWERT`</Werte> |
| <span className="hbs-f hbs-e2">[tarifstufe](/bo4e/202610/com/Verbrauch#tarifstufe)</span> | Tarifstufe | [Enum Tarifstufe](/bo4e/202610/enum/Tarifstufe)<br/><Werte>`TARIFSTUFE_0`, `TARIFSTUFE_1`, `TARIFSTUFE_2`, `TARIFSTUFE_3`, `TARIFSTUFE_4`, `TARIFSTUFE_5`, `TARIFSTUFE_6`, `TARIFSTUFE_7`, `TARIFSTUFE_8`, `TARIFSTUFE_9`</Werte> |
| <span className="hbs-f hbs-e2">[nutzungszeitpunkt](/bo4e/202610/com/Verbrauch#nutzungszeitpunkt)</span> | nutzungszeitpunkt | string (date-time) |
| <span className="hbs-f hbs-e2">[ausfuehrungszeitpunkt](/bo4e/202610/com/Verbrauch#ausfuehrungszeitpunkt)</span> | ausfuehrungszeitpunkt | string (date-time) |
| <span className="hbs-f hbs-e2">[position](/bo4e/202610/com/Verbrauch#position)</span> | position | integer |
| <span className="hbs-f hbs-e2">[ablesedatum](/bo4e/202610/com/Verbrauch#ablesedatum)</span> | ablesedatum | string (date-time) |
| <span className="hbs-f hbs-e2">[leistungsperiode](/bo4e/202610/com/Verbrauch#leistungsperiode)</span> | leistungsperiode | string |
| <span className="hbs-g hbs-e2">[statuszusatzinformationen](/bo4e/202610/com/Verbrauch#statuszusatzinformationen) <span className="hbs-liste">[ ]</span></span> | statuszusatzinformationen | [StatusZusatzInformation[]](/bo4e/202610/com/StatusZusatzInformation) |
| <span className="hbs-f hbs-e3">[art](/bo4e/202610/com/StatusZusatzInformation#art)</span> | StatusArt | [Enum StatusArt](/bo4e/202610/enum/StatusArt)<br/><Werte>`PLAUSIBILISIERUNGSHINWEIS`, `ERSATZWERTBILDUNGSVERFAHREN`, `KORREKTURGRUND`, `GRUND_ERSATZWERTBILDUNGSVERFAHREN`, `GASQUALITAET`, `MESSKLASSIFIZIERUNG`</Werte> |
| <span className="hbs-f hbs-e3">[status](/bo4e/202610/com/StatusZusatzInformation#status)</span> | Status | [Enum Status](/bo4e/202610/enum/Status)<br/><Werte>`KUNDENSELBSTABLESUNG`, `LEERSTAND`, `REALER_ZAEHLERUEBERLAUF_GEPRUEFT`, `PLAUSIBEL_WG_KONTROLLABLESUNG`, `PLAUSIBEL_WG_KUNDENHINWEIS`, `AUSTAUSCH_DES_ERSATZWERTES`, `RECHENWERT`, `BASIS_MME`, `VERGLEICHSMESSUNG_GEEICHT`, `VERGLEICHSMESSUNG_NICHT_GEEICHT`, `MESSWERTNACHBILDUNG_AUS_GEEICHTEN_WERTEN`, `MESSWERTNACHBILDUNG_AUS_NICHT_GEEICHTEN_WERTEN`, `INTERPOLATION`, `HALTEWERT`, `BILANZIERUNG_NETZABSCHNITT`, `HISTORISCHE_MESSWERTE`, `STATISTISCHE_METHODE`, `AUFTEILUNG`, `VERWENDUNG_VON_WERTEN_DES_STOERMENGENZAEHLWERKS`, `UMGANGS_UND_KORREKTURMENGEN`, `ANGABEN_MESSLOKATION`, `KEIN_ZUGANG`, `KOMMUNIKATIONSSTOERUNG`, `NETZAUSFALL`, `SPANNUNGSAUSFALL`, `STATUS_GERAETEWECHSEL`, `KALIBRIERUNG`, `GERAET_ARBEITET_AUSSERHALB_DER_BETRIEBSBEDINGUNGEN`, `MESSEINRICHTUNG_GESTOERT_DEFEKT`, `UNSICHERHEIT_MESSUNG`, `BERUECKSICHTIGUNG_STOERMENGENZAEHLWERK`, `MENGENUMWERTUNG_VOLLSTAENDIG`, `UHRZEIT_GESTELLT_SYNCHRONISATION`, `MESSWERT_UNPLAUSIBEL`, `FALSCHER_WANDLERFAKTOR`, `FEHLERHAFTE_ABLESUNG`, `AENDERUNG_DER_BERECHNUNG`, `UMBAU_DER_MESSLOKATION`, `DATENBEARBEITUNGSFEHLER`, `BRENNWERTKORREKTUR`, `Z_ZAHL_KORREKTUR`, `STOERUNG_DEFEKT_MESSEINRICHTUNG`, `AENDERUNG_TARIFSCHALTZEITEN`, `TARIFSCHALTGERAET_DEFEKT`, `IMPULSWERTIGKEIT_NICHT_AUSREICHEND`, `ENERGIEMENGE_IN_UNGEMESSENEM_ZEITINTERVALL`, `ENERGIEMENGE_AUS_DEM_UNGEPAIRTEN_ZEITINTERVALL`, `WARTUNGSARBEITEN_AN_GEEICHTEM_MESSGERAET`, `GESTOERTE_WERTE`, `WARTUNGSARBEITEN_AN_EICHRECHTSKONFORMEN_MESSGERAETEN`, `KONSISTENZ_UND_SYNCHRONPRUEFUNG`, `GRUND_ANGABEN_MESSLOKATION`, `ANFORDERUNG_IN_DIE_VERGANGENHEIT_ZUM_ANGEFORDERTEN_ZEITPUNKT_LIEGT_KEIN_WERT_VOR`, `UMSTELLUNG_GASQUALITAET`, `ZAEHLERSTAND_ZUM_BEGINN_DER_ANGEGEBENEN_ENERGIEMENGE_VORHANDEN_UND_KOMMUNIZIERT`, `ZAEHLERSTAND_ZUM_ENDE_DER_ANGEGEBENEN_ENERGIEMENGE_VORHANDEN_UND_KOMMUNIZIERT`, `ZAEHLERSTAND_ZUM_BEGINN_DER_ANGEGEBENEN_ENERGIEMENGE_NICHT_VORHANDEN_DA_MENGENABGRENZUNG`, `ZAEHLERSTAND_ZUM_ENDE_DER_ANGEGEBENEN_ENERGIEMENGE_NICHT_VORHANDEN_DA_MENGENABGRENZUNG`, `GESCHEITERT`, `AUSGEBAUT`</Werte> |
| <span className="hbs-g hbs-e1">[jahresverbrauchsprognose](/bo4e/202610/com/Zeitreihenprodukt#jahresverbrauchsprognose)</span> | Jahresverbrauchsprognose | [Menge](/bo4e/202610/com/Menge) |
| <span className="hbs-f hbs-e2">[wert](/bo4e/202610/com/Menge#wert)</span> | Wert | number (float) |
| <span className="hbs-f hbs-e2">[einheit](/bo4e/202610/com/Menge#einheit)</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202610/enum/Mengeneinheit)<br/><Werte>`W`, `WH`, `KW`, `KWH`, `KVARH`, `MW`, `MWH`, `STUECK`, `KUBIKMETER`, `STUNDE`, `TAG`, `MONAT`, `JAHR`, `PROZENT`, `ANZAHL`, `VAR`, `KVAR`, `VARH`, `KWHK`, `Z16`, `KWT`, `WATT_PRO_QUADRATMETER`, `METER_PRO_SEKUNDE`</Werte> |
| <span className="hbs-f hbs-e2">[startdatum](/bo4e/202610/com/Menge#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e2">[enddatum](/bo4e/202610/com/Menge#enddatum)</span> | enddatum | string (date-time) |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### versionZeitreihe

2 Verwendung(en) in den Nachrichtentypen ORDERS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_17202](/schnittstellen/202610/pruefi/ORDERS/PI_17202) | Prüfi | ORDERS | stammdaten › SUMMENZEITREIHE |
| [PI_17204](/schnittstellen/202610/pruefi/ORDERS/PI_17204) | Prüfi | ORDERS | stammdaten › SUMMENZEITREIHE |

### bilanzierungsgebiet

1 Verwendung(en) in den Nachrichtentypen ORDERS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_17203](/schnittstellen/202610/pruefi/ORDERS/PI_17203) | Prüfi | ORDERS | stammdaten › SUMMENZEITREIHE |

### regelzone

1 Verwendung(en) in den Nachrichtentypen ORDERS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_17203](/schnittstellen/202610/pruefi/ORDERS/PI_17203) | Prüfi | ORDERS | stammdaten › SUMMENZEITREIHE |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
