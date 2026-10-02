# Zaehler
<span hidden data-pagefind-meta={"title:Zaehler — BO4E-Geschäftsobjekt (FV 202604)"} />

BO4E-Geschäftsobjekt · 28 Felder · 244 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="botyp"></a>`boTyp` <span className="hbs-pflicht">\*</span> | [Enum BOTyp](/bo4e/202604/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> | Typ des BO |
| <a id="versionstruktur"></a>`versionStruktur` <span className="hbs-pflicht">\*</span> | string | versionStruktur |
| <a id="zaehlernummer"></a>`zaehlernummer` | string | Nummerierung des Zählers, vergeben durch den Messstellenbetreiber |
| <a id="sparte"></a>`sparte` | [Enum Sparte](/bo4e/202604/enum/Sparte)<br/><Werte>`STROM`, `GAS`, `FERNWAERME`, `NAHWAERME`, `WASSER`, `ABWASSER`</Werte> | Strom oder Gas. |
| <a id="zaehlerauspraegung"></a>`zaehlerauspraegung` | [Enum Zaehlerauspraegung](/bo4e/202604/enum/Zaehlerauspraegung)<br/><Werte>`EINRICHTUNGSZAEHLER`, `ZWEIRICHTUNGSZAEHLER`</Werte> | Spezifikation die Richtung des Zählers betreffend. |
| <a id="zaehlertyp"></a>`zaehlertyp` | [Enum Zaehlertyp](/bo4e/202604/enum/Zaehlertyp)<br/><Werte>`DREHSTROMZAEHLER`, `BALGENGASZAEHLER`, `DREHKOLBENZAEHLER`, `SMARTMETER`, `LEISTUNGSZAEHLER`, `MAXIMUMZAEHLER`, `TURBINENRADGASZAEHLER`, `ULTRASCHALLGASZAEHLER`, `WECHSELSTROMZAEHLER`, `WIRBELGASZAEHLER`, `MESSDATENREGISTRIERGERAET`, `ELEKTRONISCHERHAUSHALTSZAEHLER`, `SONDERAUSSTATTUNG`, `WASSERZAEHLER`, `MODERNEMESSEINRICHTUNG`</Werte> | Typisierung des Zählers |
| <a id="tarifart"></a>`tarifart` | [Enum Tarifart](/bo4e/202604/enum/Tarifart)<br/><Werte>`EINTARIF`, `ZWEITARIF`, `MEHRTARIF`, `SMART_METER`, `LEISTUNGSGEMESSEN`</Werte> | Spezifikation bezüglich unterstützter Tarifarten. |
| <a id="zaehlerkonstante"></a>`zaehlerkonstante` | number (float) | Zählerkonstante auf dem Zähler. |
| <a id="eichungbis"></a>`eichungBis` | string | Bis zu diesem Datum ist der Zähler geeicht. |
| <a id="zaehlerhersteller"></a>`zaehlerhersteller` | [Geschaeftspartner](/bo4e/202604/bo/Geschaeftspartner) | Der Hersteller des Zählers. Details Geschaeftspartner |
| <a id="gateway"></a>`gateway` | string | Angabe eines SMGW, mit dem der Zaehler parametrisiert ist |
| <a id="fernschaltung"></a>`fernschaltung` | [Enum Fernschaltung](/bo4e/202604/enum/Fernschaltung)<br/><Werte>`VORHANDEN`, `NICHT_VORHANDEN`</Werte> | Fernschaltung |
| <a id="messwerterfassung"></a>`messwerterfassung` | [Enum Messwerterfassung](/bo4e/202604/enum/Messwerterfassung)<br/><Werte>`FERNAUSLESBAR`, `MANUELL_AUSGELESENE`</Werte> | Messwerterfassung am Zählpunkt |
| <a id="zaehlertypspezifikation"></a>`zaehlertypspezifikation` | [Enum ZaehlertypSpezifikation](/bo4e/202604/enum/ZaehlertypSpezifikation)<br/><Werte>`EDL40`, `EDL21`, `SONSTIGER_EHZ`, `MME_STANDARD`, `MME_MEDA`</Werte> | Typisierung des Zählers (spezifikation für EHZ und MME) |
| <a id="befestigungsart"></a>`befestigungsart` | [Enum Befestigungsart](/bo4e/202604/enum/Befestigungsart)<br/><Werte>`STECKTECHNIK`, `DREIPUNKT`, `HUTSCHIENE`, `EINSTUTZEN`, `ZWEISTUTZEN`</Werte> | Befestigungsart |
| <a id="zaehlergroesse"></a>`zaehlergroesse` | [Enum Geraetemerkmal](/bo4e/202604/enum/Geraetemerkmal)<br/><Werte>`EINTARIF`, `ZWEITARIF`, `MEHRTARIF`, `GAS_G2P5`, `GAS_G4`, `GAS_G6`, `GAS_G10`, `GAS_G16`, `GAS_G25`, `GAS_G40`, `GAS_G65`, `GAS_G100`, `GAS_G160`, `GAS_G250`, `GAS_G350`, `GAS_G400`, `GAS_G4000`, `GAS_G650`, `GAS_G6500`, `GAS_G1000`, `GAS_G10000`, `GAS_G12500`, `GAS_G1600`, `GAS_G16000`, `GAS_G2500`, `IMPULSGEBER_G4_G100`, `IMPULSGEBER_G100`, `MODEM_GSM`, `MODEM_GPRS`, `MODEM_FUNK`, `MODEM_GSM_O_LG`, `MODEM_GSM_M_LG`, `MODEM_FESTNETZ`, `MODEM_GPRS_M_LG`, `PLC_COM`, `ETHERNET_KOM`, `DSL_KOM`, `LTE_KOM`, `RUNDSTEUEREMPFAENGER`, `TARIFSCHALTGERAET`, `ZUSTANDS_MU`, `TEMPERATUR_MU`, `KOMPAKT_MU`, `SYSTEM_MU`, `UNBESTIMMT`, `WASSER_MWZW`, `WASSER_WZWW`, `WASSER_WZ01`, `WASSER_WZ02`, `WASSER_WZ03`, `WASSER_WZ04`, `WASSER_WZ05`, `WASSER_WZ06`, `WASSER_WZ07`, `WASSER_WZ08`, `WASSER_WZ09`, `WASSER_WZ10`, `WASSER_VWZ04`, `WASSER_VWZ05`, `WASSER_VWZ06`, `WASSER_VWZ07`, `WASSER_VWZ10`, `DICHTEMENGENUMWERTER`, `TEMPERATURMENGENUMWERTER`, `ZUSTANDSMENGENUMWERTER`, `BLOCKSTROMWANDLER`, `MESSWANDLERSATZ_IMS_MME`, `KOMBIMESSWANDLER`, `SPANNUNGSWANDLER`</Werte> | Zaehlergroesse |
| <a id="mengenumwertertyp"></a>`mengenumwertertyp` | [Enum Mengenumwertertyp](/bo4e/202604/enum/Mengenumwertertyp)<br/><Werte>`DICHTEMENGENUMWERTER`, `TEMPERATURMENGENUMWERTER`, `ZUSTANDSMENGENUMWERTER`</Werte> | Mengenumwertertyp |
| <a id="volumenerfassung"></a>`volumenerfassung` | [Enum Volumenerfassung](/bo4e/202604/enum/Volumenerfassung)<br/><Werte>`HOCHFREQUENZSONDE`, `KENNLINIENKORREKTUR`, `SCHLEICHMENGENUNTERDRUECKUNG`</Werte> | Volumenerfassung |
| <a id="serialnummer"></a>`serialnummer` | string | serialnummer |
| <a id="geraetemerkmal"></a>`geraetemerkmal` | [Enum Geraetemerkmal](/bo4e/202604/enum/Geraetemerkmal)<br/><Werte>`EINTARIF`, `ZWEITARIF`, `MEHRTARIF`, `GAS_G2P5`, `GAS_G4`, `GAS_G6`, `GAS_G10`, `GAS_G16`, `GAS_G25`, `GAS_G40`, `GAS_G65`, `GAS_G100`, `GAS_G160`, `GAS_G250`, `GAS_G350`, `GAS_G400`, `GAS_G4000`, `GAS_G650`, `GAS_G6500`, `GAS_G1000`, `GAS_G10000`, `GAS_G12500`, `GAS_G1600`, `GAS_G16000`, `GAS_G2500`, `IMPULSGEBER_G4_G100`, `IMPULSGEBER_G100`, `MODEM_GSM`, `MODEM_GPRS`, `MODEM_FUNK`, `MODEM_GSM_O_LG`, `MODEM_GSM_M_LG`, `MODEM_FESTNETZ`, `MODEM_GPRS_M_LG`, `PLC_COM`, `ETHERNET_KOM`, `DSL_KOM`, `LTE_KOM`, `RUNDSTEUEREMPFAENGER`, `TARIFSCHALTGERAET`, `ZUSTANDS_MU`, `TEMPERATUR_MU`, `KOMPAKT_MU`, `SYSTEM_MU`, `UNBESTIMMT`, `WASSER_MWZW`, `WASSER_WZWW`, `WASSER_WZ01`, `WASSER_WZ02`, `WASSER_WZ03`, `WASSER_WZ04`, `WASSER_WZ05`, `WASSER_WZ06`, `WASSER_WZ07`, `WASSER_WZ08`, `WASSER_WZ09`, `WASSER_WZ10`, `WASSER_VWZ04`, `WASSER_VWZ05`, `WASSER_VWZ06`, `WASSER_VWZ07`, `WASSER_VWZ10`, `DICHTEMENGENUMWERTER`, `TEMPERATURMENGENUMWERTER`, `ZUSTANDSMENGENUMWERTER`, `BLOCKSTROMWANDLER`, `MESSWANDLERSATZ_IMS_MME`, `KOMBIMESSWANDLER`, `SPANNUNGSWANDLER`</Werte> | Weitere Merkmale des Geräts, zum Beispiel Mehrtarif, Eintarif etc.. Details Geraetemerkmal |
| <a id="herstellungsdatum"></a>`herstellungsdatum` | string | herstellungsdatum |
| <a id="baujahr"></a>`baujahr` | string | baujahr |
| <a id="messlokationsid"></a>`messlokationsId` | string | messlokationsId |
| <a id="marktlokationsid"></a>`marktlokationsId` | string | marktlokationsId |
| <a id="geraete"></a>`geraete` | [Geraet[]](/bo4e/202604/com/Geraet) | Liste der Geräte, die zu diesem Zähler gehören. |
| <a id="zaehlwerke"></a>`zaehlwerke` | [Zaehlwerk[]](/bo4e/202604/com/Zaehlwerk) | Die Zählwerke des Zählers. |
| <a id="datenqualitaet"></a>`datenqualitaet` | [Enum Datenqualitaet](/bo4e/202604/enum/Datenqualitaet)<br/><Werte>`ERWARTETE_DATEN`, `IM_SYSTEM_VORHANDENE_DATEN`, `INFORMATIVE_DATEN`, `GUELTIGE_DATEN`, `KEINE_DATEN`, `IM_SYSTEM_KEINE_DATEN_VORHANDEN`, `KEINE_DATEN_ERWARTET`, `DIFFERENZ_DATEN`, `DIFFERENZ_ERWARTETE_DATEN`, `DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</Werte> | Datenqualitaet |
| <a id="gueltigkeitszeitraum"></a>`gueltigkeitszeitraum` | [Zeitraum](/bo4e/202604/com/Zeitraum) | — |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[boTyp](/bo4e/202604/bo/Zaehler#botyp) <span className="hbs-pflicht">\*</span></span> | Typ des BO | [Enum BOTyp](/bo4e/202604/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> |
| <span className="hbs-f hbs-e0">[versionStruktur](/bo4e/202604/bo/Zaehler#versionstruktur) <span className="hbs-pflicht">\*</span></span> | versionStruktur | string |
| <span className="hbs-f hbs-e0">[zaehlernummer](/bo4e/202604/bo/Zaehler#zaehlernummer)</span> | Nummerierung des Zählers, vergeben durch den Messstellenbetreiber | string |
| <span className="hbs-f hbs-e0">[sparte](/bo4e/202604/bo/Zaehler#sparte)</span> | Strom oder Gas. | [Enum Sparte](/bo4e/202604/enum/Sparte)<br/><Werte>`STROM`, `GAS`, `FERNWAERME`, `NAHWAERME`, `WASSER`, `ABWASSER`</Werte> |
| <span className="hbs-f hbs-e0">[zaehlerauspraegung](/bo4e/202604/bo/Zaehler#zaehlerauspraegung)</span> | Spezifikation die Richtung des Zählers betreffend. | [Enum Zaehlerauspraegung](/bo4e/202604/enum/Zaehlerauspraegung)<br/><Werte>`EINRICHTUNGSZAEHLER`, `ZWEIRICHTUNGSZAEHLER`</Werte> |
| <span className="hbs-f hbs-e0">[zaehlertyp](/bo4e/202604/bo/Zaehler#zaehlertyp)</span> | Typisierung des Zählers | [Enum Zaehlertyp](/bo4e/202604/enum/Zaehlertyp)<br/><Werte>`DREHSTROMZAEHLER`, `BALGENGASZAEHLER`, `DREHKOLBENZAEHLER`, `SMARTMETER`, `LEISTUNGSZAEHLER`, `MAXIMUMZAEHLER`, `TURBINENRADGASZAEHLER`, `ULTRASCHALLGASZAEHLER`, `WECHSELSTROMZAEHLER`, `WIRBELGASZAEHLER`, `MESSDATENREGISTRIERGERAET`, `ELEKTRONISCHERHAUSHALTSZAEHLER`, `SONDERAUSSTATTUNG`, `WASSERZAEHLER`, `MODERNEMESSEINRICHTUNG`</Werte> |
| <span className="hbs-f hbs-e0">[tarifart](/bo4e/202604/bo/Zaehler#tarifart)</span> | Spezifikation bezüglich unterstützter Tarifarten. | [Enum Tarifart](/bo4e/202604/enum/Tarifart)<br/><Werte>`EINTARIF`, `ZWEITARIF`, `MEHRTARIF`, `SMART_METER`, `LEISTUNGSGEMESSEN`</Werte> |
| <span className="hbs-f hbs-e0">[zaehlerkonstante](/bo4e/202604/bo/Zaehler#zaehlerkonstante)</span> | Zählerkonstante auf dem Zähler. | number (float) |
| <span className="hbs-f hbs-e0">[eichungBis](/bo4e/202604/bo/Zaehler#eichungbis)</span> | Bis zu diesem Datum ist der Zähler geeicht. | string |
| <span className="hbs-g hbs-e0">[zaehlerhersteller](/bo4e/202604/bo/Zaehler#zaehlerhersteller)</span> | Der Hersteller des Zählers. Details Geschaeftspartner | [Geschaeftspartner](/bo4e/202604/bo/Geschaeftspartner) |
| <span className="hbs-f hbs-e1">[boTyp](/bo4e/202604/bo/Geschaeftspartner#botyp) <span className="hbs-pflicht">\*</span></span> | Typ des BO | [Enum BOTyp](/bo4e/202604/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> |
| <span className="hbs-f hbs-e1">[versionStruktur](/bo4e/202604/bo/Geschaeftspartner#versionstruktur) <span className="hbs-pflicht">\*</span></span> | versionStruktur | string |
| <span className="hbs-f hbs-e1">[anrede](/bo4e/202604/bo/Geschaeftspartner#anrede)</span> | Die Anrede für den GePa, Z.B. Herr. | string |
| <span className="hbs-f hbs-e1">[name1](/bo4e/202604/bo/Geschaeftspartner#name1)</span> | Erster Teil des Namens. Hier kann der Firmenname oder bei Privatpersonen<br/>beispielsweise der Nachname dargestellt werden. Beispiele: Yellow Strom GmbH<br/>oder Hagen | string |
| <span className="hbs-f hbs-e1">[name2](/bo4e/202604/bo/Geschaeftspartner#name2)</span> | Zweiter Teil des Namens. Hier kann der eine Erweiterung zum Firmennamen oder<br/>bei Privatpersonen beispielsweise der Vorname dargestellt werden. Beispiele:<br/>Bereich Süd oder Nina | string |
| <span className="hbs-f hbs-e1">[name3](/bo4e/202604/bo/Geschaeftspartner#name3)</span> | Dritter Teil des Namens. Hier können weitere Ergänzungen zum Firmennamen oder<br/>bei Privatpersonen Zusätze zum Namen dargestellt werden. Beispiele: und Afrika<br/>oder Sängerin | string |
| <span className="hbs-f hbs-e1">[name4](/bo4e/202604/bo/Geschaeftspartner#name4)</span> | name4 | string |
| <span className="hbs-f hbs-e1">[umsatzsteuerId](/bo4e/202604/bo/Geschaeftspartner#umsatzsteuerid)</span> | Die Umsatzsteuer-ID des Geschäftspartners. Beispiel: DE 813281825 | string |
| <span className="hbs-f hbs-e1">[glaeubigerId](/bo4e/202604/bo/Geschaeftspartner#glaeubigerid)</span> | * Die Gläubiger-ID welche im Zahlungsverkehr verwendet wird- Z.B. DE 47116789 | string |
| <span className="hbs-f hbs-e1">[emailAdresse](/bo4e/202604/bo/Geschaeftspartner#emailadresse)</span> | emailAdresse | string |
| <span className="hbs-f hbs-e1">[website](/bo4e/202604/bo/Geschaeftspartner#website)</span> | Internetseite des Marktpartners. Beispiel: www.mp-energie.de | string |
| <span className="hbs-f hbs-e1">[gewerbekennzeichnung](/bo4e/202604/bo/Geschaeftspartner#gewerbekennzeichnung)</span> | Kennzeichnung ob es sich um einen Gewerbe/Unternehmen (gewerbeKennzeichnung = true)<br/>oder eine Privatperson handelt. (gewerbeKennzeichnung = false) | boolean |
| <span className="hbs-f hbs-e1">[hrnummer](/bo4e/202604/bo/Geschaeftspartner#hrnummer)</span> | Handelsregisternummer des Geschäftspartners | string |
| <span className="hbs-f hbs-e1">[amtsgericht](/bo4e/202604/bo/Geschaeftspartner#amtsgericht)</span> | Amtsgericht bzw Handelsregistergericht, das die Handelsregisternummer herausgegeben hat | string |
| <span className="hbs-g hbs-e1">[partneradresse](/bo4e/202604/bo/Geschaeftspartner#partneradresse)</span> | Adresse des Geschäftspartners, an der sich der Hauptsitz befindet. Details | [Adresse](/bo4e/202604/com/Adresse) |
| <span className="hbs-f hbs-e2">[postleitzahl](/bo4e/202604/com/Adresse#postleitzahl)</span> | Postleitzahl | string |
| <span className="hbs-f hbs-e2">[ort](/bo4e/202604/com/Adresse#ort)</span> | Ort | string |
| <span className="hbs-f hbs-e2">[strasse](/bo4e/202604/com/Adresse#strasse)</span> | Strasse | string |
| <span className="hbs-f hbs-e2">[hausnummer](/bo4e/202604/com/Adresse#hausnummer)</span> | Hausnummer und Ergänzung | string |
| <span className="hbs-f hbs-e2">[postfach](/bo4e/202604/com/Adresse#postfach)</span> | Postfach | string |
| <span className="hbs-f hbs-e2">[adresszusatz](/bo4e/202604/com/Adresse#adresszusatz)</span> | Adresszusatz | string |
| <span className="hbs-f hbs-e2">[coErgaenzung](/bo4e/202604/com/Adresse#coergaenzung)</span> | coErgaenzung | string |
| <span className="hbs-f hbs-e2">[landescode](/bo4e/202604/com/Adresse#landescode)</span> | Landescode | [Enum Landescode](/bo4e/202604/enum/Landescode)<br/><Werte>`AC`, `AD`, `AE`, `AF`, `AG`, `AI`, `AL`, `AM`, `AN`, `AO`, `AQ`, `AR`, `AS`, `AT`, `AU`, `AW`, `AX`, `AZ`, `BA`, `BB`, `BD`, `BE`, `BF`, `BG`, `BH`, `BI`, `BJ`, `BL`, `BM`, `BN`, `BO`, `BQ`, `BR`, `BS`, `BT`, `BU`, `BV`, `BW`, `BY`, `BZ`, `CA`, `CC`, `CD`, `CF`, `CG`, `CH`, `CI`, `CK`, `CL`, `CM`, `CN`, `CO`, `CP`, `CR`, `CS`, `CU`, `CV`, `CW`, `CX`, `CY`, `CZ`, `DE`, `DG`, `DJ`, `DK`, `DM`, `DO`, `DZ`, `EA`, `EC`, `EE`, `EG`, `EH`, `ER`, `ES`, `ET`, `EU`, `FI`, `FJ`, `FK`, `FM`, `FO`, `FR`, `FX`, `GA`, `GB`, `GD`, `GE`, `GF`, `GG`, `GH`, `GI`, `GL`, `GM`, `GN`, `GP`, `GQ`, `GR`, `GS`, `GT`, `GU`, `GW`, `GY`, `HK`, `HM`, `HN`, `HR`, `HT`, `HU`, `IC`, `ID`, `IE`, `IL`, `IM`, `IN`, `IO`, `IQ`, `IR`, `IS`, `IT`, `JE`, `JM`, `JO`, `JP`, `KE`, `KG`, `KH`, `KI`, `KM`, `KN`, `KP`, `KR`, `KW`, `KY`, `KZ`, `LA`, `LB`, `LC`, `LI`, `LK`, `LR`, `LS`, `LT`, `LU`, `LV`, `LY`, `MA`, `MC`, `MD`, `ME`, `MF`, `MG`, `MH`, `MK`, `ML`, `MM`, `MN`, `MO`, `MP`, `MQ`, `MR`, `MS`, `MT`, `MU`, `MV`, `MW`, `MX`, `MY`, `MZ`, `NA`, `NC`, `NE`, `NF`, `NG`, `NI`, `NL`, `NO`, `NP`, `NR`, `NT`, `NU`, `NZ`, `OM`, `PA`, `PE`, `PF`, `PG`, `PH`, `PK`, `PL`, `PM`, `PN`, `PR`, `PS`, `PT`, `PW`, `PY`, `QA`, `RE`, `RO`, `RS`, `RU`, `RW`, `SA`, `SB`, `SC`, `SD`, `SE`, `SF`, `SG`, `SH`, `SI`, `SJ`, `SK`, `SL`, `SM`, `SN`, `SO`, `SR`, `SS`, `ST`, `SU`, `SV`, `SX`, `SY`, `SZ`, `TA`, `TC`, `TD`, `TF`, `TG`, `TJ`, `TK`, `TL`, `TM`, `TN`, `TO`, `TP`, `TR`, `TT`, `TV`, `TW`, `TZ`, `UA`, `UG`, `UK`, `UM`, `US`, `UY`, `UZ`, `VA`, `VC`, `VE`, `VG`, `VI`, `VN`, `VU`, `WF`, `WS`, `XK`, `YE`, `YT`, `YU`, `ZA`, `ZM`, `ZR`, `ZW`</Werte> |
| <span className="hbs-f hbs-e2">[ortsteil](/bo4e/202604/com/Adresse#ortsteil)</span> | Ortsteil | string |
| <span className="hbs-g hbs-e2">[zusatzInformation](/bo4e/202604/com/Adresse#zusatzinformation)</span> | — | [AdresszusatzInformation](/bo4e/202604/com/AdresszusatzInformation) |
| <span className="hbs-f hbs-e3">[zusatz1](/bo4e/202604/com/AdresszusatzInformation#zusatz1)</span> | Adresszusatz 1 | string |
| <span className="hbs-f hbs-e3">[zusatz2](/bo4e/202604/com/AdresszusatzInformation#zusatz2)</span> | Adresszusatz 2 | string |
| <span className="hbs-f hbs-e3">[zusatz3](/bo4e/202604/com/AdresszusatzInformation#zusatz3)</span> | Adresszusatz 3 | string |
| <span className="hbs-f hbs-e3">[zusatz4](/bo4e/202604/com/AdresszusatzInformation#zusatz4)</span> | Adresszusatz 4 | string |
| <span className="hbs-f hbs-e3">[zusatz5](/bo4e/202604/com/AdresszusatzInformation#zusatz5)</span> | Adresszusatz 5 | string |
| <span className="hbs-f hbs-e1">[externeKundenummerLieferant](/bo4e/202604/bo/Geschaeftspartner#externekundenummerlieferant)</span> | externeKundenummerLieferant | string |
| <span className="hbs-g hbs-e1">[externeReferenzen](/bo4e/202604/bo/Geschaeftspartner#externereferenzen) <span className="hbs-liste">[ ]</span></span> | Hier können IDs anderer Systeme hinterlegt werden (z.B. eine SAP-GP-Nummer) (Details siehe<br/>ExterneReferenz) | [ExterneReferenz[]](/bo4e/202604/com/ExterneReferenz) |
| <span className="hbs-f hbs-e2">[exRefName](/bo4e/202604/com/ExterneReferenz#exrefname)</span> | Bezeichnung der externen Referenz (z.B. "hochfrequenz integration services") | string<br/><Werte>`Kundennummer beim Lieferanten`, `Kundennummer beim Altlieferanten`</Werte> |
| <span className="hbs-f hbs-e2">[exRefWert](/bo4e/202604/com/ExterneReferenz#exrefwert)</span> | Wert der externen Referenz (z.B. "123456"; "4711") | string |
| <span className="hbs-f hbs-e1">[geschaeftspartnerrolle](/bo4e/202604/bo/Geschaeftspartner#geschaeftspartnerrolle) <span className="hbs-liste">[ ]</span></span> | Rolle, die der Geschäftspartner hat (z.B. Interessent, Kunde). | [Enum Geschaeftspartnerrolle[]](/bo4e/202604/enum/Geschaeftspartnerrolle)<br/><Werte>`KUNDE`, `LIEFERANT`, `DIENSTLEISTER`, `INTERESSENT`, `MARKTPARTNER`, `EIGENTUEMER`, `HAUSVERWALTER`, `KORRESPONDENZEMPFAENGER`, `ABLESEKARTENEMPFAENGER`</Werte> |
| <span className="hbs-f hbs-e1">[kontaktweg](/bo4e/202604/bo/Geschaeftspartner#kontaktweg) <span className="hbs-liste">[ ]</span></span> | Bevorzugter Kontaktweg des Geschäftspartners. | [Enum Kontaktart[]](/bo4e/202604/enum/Kontaktart)<br/><Werte>`ANSCHREIBEN`, `TELEFONAT`, `FAX`, `E_MAIL`, `SMS`</Werte> |
| <span className="hbs-g hbs-e1">[ansprechpartner](/bo4e/202604/bo/Geschaeftspartner#ansprechpartner)</span> | Ansprechpartner as in EDIFACT CTA+IC' COM+?+3222271020:TE', that includes e.g. the phone number of customer. | [Ansprechpartner](/bo4e/202604/bo/Ansprechpartner) |
| <span className="hbs-f hbs-e2">[boTyp](/bo4e/202604/bo/Ansprechpartner#botyp) <span className="hbs-pflicht">\*</span></span> | Typ des BO | [Enum BOTyp](/bo4e/202604/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> |
| <span className="hbs-f hbs-e2">[versionStruktur](/bo4e/202604/bo/Ansprechpartner#versionstruktur) <span className="hbs-pflicht">\*</span></span> | versionStruktur | string |
| <span className="hbs-f hbs-e2">[nachname](/bo4e/202604/bo/Ansprechpartner#nachname)</span> | Nachname (Familienname) des Ansprechpartners | string |
| <span className="hbs-f hbs-e2">[eMailAdresse](/bo4e/202604/bo/Ansprechpartner#emailadresse)</span> | E-Mail Adresse | string |
| <span className="hbs-g hbs-e2">[rufnummern](/bo4e/202604/bo/Ansprechpartner#rufnummern) <span className="hbs-liste">[ ]</span></span> | Liste der Telefonnummern, unter denen der Ansprechpartner erreichbar ist. | [Rufnummer[]](/bo4e/202604/com/Rufnummer) |
| <span className="hbs-f hbs-e3">[nummerntyp](/bo4e/202604/com/Rufnummer#nummerntyp)</span> | Rufnummernart | [Enum Rufnummernart](/bo4e/202604/enum/Rufnummernart)<br/><Werte>`RUF_ZENTRALE`, `FAX_ZENTRALE`, `SAMMELRUF`, `SAMMELFAX`, `ABTEILUNGRUF`, `ABTEILUNGFAX`, `RUF_DURCHWAHL`, `FAX_DURCHWAHL`, `MOBIL_NUMMER`</Werte> |
| <span className="hbs-f hbs-e3">[rufnummer](/bo4e/202604/com/Rufnummer#rufnummer)</span> | rufnummer | string |
| <span className="hbs-f hbs-e0">[gateway](/bo4e/202604/bo/Zaehler#gateway)</span> | Angabe eines SMGW, mit dem der Zaehler parametrisiert ist | string |
| <span className="hbs-f hbs-e0">[fernschaltung](/bo4e/202604/bo/Zaehler#fernschaltung)</span> | Fernschaltung | [Enum Fernschaltung](/bo4e/202604/enum/Fernschaltung)<br/><Werte>`VORHANDEN`, `NICHT_VORHANDEN`</Werte> |
| <span className="hbs-f hbs-e0">[messwerterfassung](/bo4e/202604/bo/Zaehler#messwerterfassung)</span> | Messwerterfassung am Zählpunkt | [Enum Messwerterfassung](/bo4e/202604/enum/Messwerterfassung)<br/><Werte>`FERNAUSLESBAR`, `MANUELL_AUSGELESENE`</Werte> |
| <span className="hbs-f hbs-e0">[zaehlertypspezifikation](/bo4e/202604/bo/Zaehler#zaehlertypspezifikation)</span> | Typisierung des Zählers (spezifikation für EHZ und MME) | [Enum ZaehlertypSpezifikation](/bo4e/202604/enum/ZaehlertypSpezifikation)<br/><Werte>`EDL40`, `EDL21`, `SONSTIGER_EHZ`, `MME_STANDARD`, `MME_MEDA`</Werte> |
| <span className="hbs-f hbs-e0">[befestigungsart](/bo4e/202604/bo/Zaehler#befestigungsart)</span> | Befestigungsart | [Enum Befestigungsart](/bo4e/202604/enum/Befestigungsart)<br/><Werte>`STECKTECHNIK`, `DREIPUNKT`, `HUTSCHIENE`, `EINSTUTZEN`, `ZWEISTUTZEN`</Werte> |
| <span className="hbs-f hbs-e0">[zaehlergroesse](/bo4e/202604/bo/Zaehler#zaehlergroesse)</span> | Zaehlergroesse | [Enum Geraetemerkmal](/bo4e/202604/enum/Geraetemerkmal)<br/><Werte>`EINTARIF`, `ZWEITARIF`, `MEHRTARIF`, `GAS_G2P5`, `GAS_G4`, `GAS_G6`, `GAS_G10`, `GAS_G16`, `GAS_G25`, `GAS_G40`, `GAS_G65`, `GAS_G100`, `GAS_G160`, `GAS_G250`, `GAS_G350`, `GAS_G400`, `GAS_G4000`, `GAS_G650`, `GAS_G6500`, `GAS_G1000`, `GAS_G10000`, `GAS_G12500`, `GAS_G1600`, `GAS_G16000`, `GAS_G2500`, `IMPULSGEBER_G4_G100`, `IMPULSGEBER_G100`, `MODEM_GSM`, `MODEM_GPRS`, `MODEM_FUNK`, `MODEM_GSM_O_LG`, `MODEM_GSM_M_LG`, `MODEM_FESTNETZ`, `MODEM_GPRS_M_LG`, `PLC_COM`, `ETHERNET_KOM`, `DSL_KOM`, `LTE_KOM`, `RUNDSTEUEREMPFAENGER`, `TARIFSCHALTGERAET`, `ZUSTANDS_MU`, `TEMPERATUR_MU`, `KOMPAKT_MU`, `SYSTEM_MU`, `UNBESTIMMT`, `WASSER_MWZW`, `WASSER_WZWW`, `WASSER_WZ01`, `WASSER_WZ02`, `WASSER_WZ03`, `WASSER_WZ04`, `WASSER_WZ05`, `WASSER_WZ06`, `WASSER_WZ07`, `WASSER_WZ08`, `WASSER_WZ09`, `WASSER_WZ10`, `WASSER_VWZ04`, `WASSER_VWZ05`, `WASSER_VWZ06`, `WASSER_VWZ07`, `WASSER_VWZ10`, `DICHTEMENGENUMWERTER`, `TEMPERATURMENGENUMWERTER`, `ZUSTANDSMENGENUMWERTER`, `BLOCKSTROMWANDLER`, `MESSWANDLERSATZ_IMS_MME`, `KOMBIMESSWANDLER`, `SPANNUNGSWANDLER`</Werte> |
| <span className="hbs-f hbs-e0">[mengenumwertertyp](/bo4e/202604/bo/Zaehler#mengenumwertertyp)</span> | Mengenumwertertyp | [Enum Mengenumwertertyp](/bo4e/202604/enum/Mengenumwertertyp)<br/><Werte>`DICHTEMENGENUMWERTER`, `TEMPERATURMENGENUMWERTER`, `ZUSTANDSMENGENUMWERTER`</Werte> |
| <span className="hbs-f hbs-e0">[volumenerfassung](/bo4e/202604/bo/Zaehler#volumenerfassung)</span> | Volumenerfassung | [Enum Volumenerfassung](/bo4e/202604/enum/Volumenerfassung)<br/><Werte>`HOCHFREQUENZSONDE`, `KENNLINIENKORREKTUR`, `SCHLEICHMENGENUNTERDRUECKUNG`</Werte> |
| <span className="hbs-f hbs-e0">[serialnummer](/bo4e/202604/bo/Zaehler#serialnummer)</span> | serialnummer | string |
| <span className="hbs-f hbs-e0">[geraetemerkmal](/bo4e/202604/bo/Zaehler#geraetemerkmal)</span> | Weitere Merkmale des Geräts, zum Beispiel Mehrtarif, Eintarif etc.. Details Geraetemerkmal | [Enum Geraetemerkmal](/bo4e/202604/enum/Geraetemerkmal)<br/><Werte>`EINTARIF`, `ZWEITARIF`, `MEHRTARIF`, `GAS_G2P5`, `GAS_G4`, `GAS_G6`, `GAS_G10`, `GAS_G16`, `GAS_G25`, `GAS_G40`, `GAS_G65`, `GAS_G100`, `GAS_G160`, `GAS_G250`, `GAS_G350`, `GAS_G400`, `GAS_G4000`, `GAS_G650`, `GAS_G6500`, `GAS_G1000`, `GAS_G10000`, `GAS_G12500`, `GAS_G1600`, `GAS_G16000`, `GAS_G2500`, `IMPULSGEBER_G4_G100`, `IMPULSGEBER_G100`, `MODEM_GSM`, `MODEM_GPRS`, `MODEM_FUNK`, `MODEM_GSM_O_LG`, `MODEM_GSM_M_LG`, `MODEM_FESTNETZ`, `MODEM_GPRS_M_LG`, `PLC_COM`, `ETHERNET_KOM`, `DSL_KOM`, `LTE_KOM`, `RUNDSTEUEREMPFAENGER`, `TARIFSCHALTGERAET`, `ZUSTANDS_MU`, `TEMPERATUR_MU`, `KOMPAKT_MU`, `SYSTEM_MU`, `UNBESTIMMT`, `WASSER_MWZW`, `WASSER_WZWW`, `WASSER_WZ01`, `WASSER_WZ02`, `WASSER_WZ03`, `WASSER_WZ04`, `WASSER_WZ05`, `WASSER_WZ06`, `WASSER_WZ07`, `WASSER_WZ08`, `WASSER_WZ09`, `WASSER_WZ10`, `WASSER_VWZ04`, `WASSER_VWZ05`, `WASSER_VWZ06`, `WASSER_VWZ07`, `WASSER_VWZ10`, `DICHTEMENGENUMWERTER`, `TEMPERATURMENGENUMWERTER`, `ZUSTANDSMENGENUMWERTER`, `BLOCKSTROMWANDLER`, `MESSWANDLERSATZ_IMS_MME`, `KOMBIMESSWANDLER`, `SPANNUNGSWANDLER`</Werte> |
| <span className="hbs-f hbs-e0">[herstellungsdatum](/bo4e/202604/bo/Zaehler#herstellungsdatum)</span> | herstellungsdatum | string |
| <span className="hbs-f hbs-e0">[baujahr](/bo4e/202604/bo/Zaehler#baujahr)</span> | baujahr | string |
| <span className="hbs-f hbs-e0">[messlokationsId](/bo4e/202604/bo/Zaehler#messlokationsid)</span> | messlokationsId | string |
| <span className="hbs-f hbs-e0">[marktlokationsId](/bo4e/202604/bo/Zaehler#marktlokationsid)</span> | marktlokationsId | string |
| <span className="hbs-g hbs-e0">[geraete](/bo4e/202604/bo/Zaehler#geraete) <span className="hbs-liste">[ ]</span></span> | Liste der Geräte, die zu diesem Zähler gehören. | [Geraet[]](/bo4e/202604/com/Geraet) |
| <span className="hbs-f hbs-e1">[geraetetyp](/bo4e/202604/com/Geraet#geraetetyp)</span> | Auflistung möglicher abzurechnender Gerätetypen | [Enum Geraetetyp](/bo4e/202604/enum/Geraetetyp)<br/><Werte>`WECHSELSTROMZAEHLER`, `DREHSTROMZAEHLER`, `ZWEIRICHTUNGSZAEHLER`, `RLM_ZAEHLER`, `IMS_ZAEHLER`, `BALGENGASZAEHLER`, `MAXIMUMZAEHLER`, `MULTIPLEXANLAGE`, `PAUSCHALANLAGE`, `VERSTAERKERANLAGE`, `SUMMATIONSGERAET`, `IMPULSGEBER`, `EDL_21_ZAEHLERAUFSATZ`, `VIER_QUADRANTEN_LASTGANGZAEHLER`, `MENGENUMWERTER`, `STROMWANDLER`, `SPANNUNGSWANDLER`, `DATENLOGGER`, `KOMMUNIKATIONSANSCHLUSS`, `MODEM`, `TELEKOMMUNIKATIONSEINRICHTUNG`, `KOMMUNIKATIONSEINRICHTUNG`, `DREHKOLBENGASZAEHLER`, `TURBINENRADGASZAEHLER`, `ULTRASCHALLZAEHLER`, `WIRBELGASZAEHLER`, `MODERNE_MESSEINRICHTUNG`, `ELEKTRONISCHER_HAUSHALTSZAEHLER`, `STEUEREINRICHTUNG`, `TECHNISCHESTEUEREINRICHTUNG`, `TARIFSCHALTGERAET`, `RUNDSTEUEREMPFAENGER`, `OPTIONALE_ZUS_ZAEHLEINRICHTUNG`, `MESSWANDLERSATZ_IMS_MME`, `KOMBIMESSWANDLER_IMS_MME`, `TARIFSCHALTGERAET_IMS_MME`, `RUNDSTEUEREMPFAENGER_IMS_MME`, `TEMPERATUR_KOMPENSATION`, `HOECHSTBELASTUNGS_ANZEIGER`, `SONSTIGES_GERAET`, `SMARTMETERGATEWAY`, `STEUERBOX`, `BLOCKSTROMWANDLER`, `KOMBIMESSWANDLER`, `MODEM_GSM`, `ETHERNET_KOM`, `PLC_COM`, `MODEM_FESTNETZ`, `DSL_KOM`, `LTE_KOM`, `DICHTEMENGENUMWERTER`, `TEMPERATURMENGENUMWERTER`, `ZUSTANDSMENGENUMWERTER`, `MESSDATENREGISTRIERGERAET`, `WANDLER`, `BEFESTIGUNGSEINRICHTUNG`</Werte> |
| <span className="hbs-f hbs-e1">[bezeichnung](/bo4e/202604/com/Geraet#bezeichnung)</span> | Bezeichnung des Gerätes | string |
| <span className="hbs-f hbs-e1">[geraetenummer](/bo4e/202604/com/Geraet#geraetenummer)</span> | Die auf dem Geräte aufgedruckte Nummer, die vom MSB vergeben wird. | string |
| <span className="hbs-f hbs-e1">[geraetereferenz](/bo4e/202604/com/Geraet#geraetereferenz)</span> | geraetereferenz | string |
| <span className="hbs-g hbs-e1">[geraeteeigenschaften](/bo4e/202604/com/Geraet#geraeteeigenschaften)</span> | Festlegung der Eigenschaften des Gerätes. Z.B. Wandler MS/NS. | [Geraeteeigenschaften](/bo4e/202604/com/Geraeteeigenschaften) |
| <span className="hbs-f hbs-e2">[geraetetyp](/bo4e/202604/com/Geraeteeigenschaften#geraetetyp)</span> | Auflistung möglicher abzurechnender Gerätetypen | [Enum Geraetetyp](/bo4e/202604/enum/Geraetetyp)<br/><Werte>`WECHSELSTROMZAEHLER`, `DREHSTROMZAEHLER`, `ZWEIRICHTUNGSZAEHLER`, `RLM_ZAEHLER`, `IMS_ZAEHLER`, `BALGENGASZAEHLER`, `MAXIMUMZAEHLER`, `MULTIPLEXANLAGE`, `PAUSCHALANLAGE`, `VERSTAERKERANLAGE`, `SUMMATIONSGERAET`, `IMPULSGEBER`, `EDL_21_ZAEHLERAUFSATZ`, `VIER_QUADRANTEN_LASTGANGZAEHLER`, `MENGENUMWERTER`, `STROMWANDLER`, `SPANNUNGSWANDLER`, `DATENLOGGER`, `KOMMUNIKATIONSANSCHLUSS`, `MODEM`, `TELEKOMMUNIKATIONSEINRICHTUNG`, `KOMMUNIKATIONSEINRICHTUNG`, `DREHKOLBENGASZAEHLER`, `TURBINENRADGASZAEHLER`, `ULTRASCHALLZAEHLER`, `WIRBELGASZAEHLER`, `MODERNE_MESSEINRICHTUNG`, `ELEKTRONISCHER_HAUSHALTSZAEHLER`, `STEUEREINRICHTUNG`, `TECHNISCHESTEUEREINRICHTUNG`, `TARIFSCHALTGERAET`, `RUNDSTEUEREMPFAENGER`, `OPTIONALE_ZUS_ZAEHLEINRICHTUNG`, `MESSWANDLERSATZ_IMS_MME`, `KOMBIMESSWANDLER_IMS_MME`, `TARIFSCHALTGERAET_IMS_MME`, `RUNDSTEUEREMPFAENGER_IMS_MME`, `TEMPERATUR_KOMPENSATION`, `HOECHSTBELASTUNGS_ANZEIGER`, `SONSTIGES_GERAET`, `SMARTMETERGATEWAY`, `STEUERBOX`, `BLOCKSTROMWANDLER`, `KOMBIMESSWANDLER`, `MODEM_GSM`, `ETHERNET_KOM`, `PLC_COM`, `MODEM_FESTNETZ`, `DSL_KOM`, `LTE_KOM`, `DICHTEMENGENUMWERTER`, `TEMPERATURMENGENUMWERTER`, `ZUSTANDSMENGENUMWERTER`, `MESSDATENREGISTRIERGERAET`, `WANDLER`, `BEFESTIGUNGSEINRICHTUNG`</Werte> |
| <span className="hbs-f hbs-e2">[geraetemerkmal](/bo4e/202604/com/Geraeteeigenschaften#geraetemerkmal)</span> | Geraetemerkmal | [Enum Geraetemerkmal](/bo4e/202604/enum/Geraetemerkmal)<br/><Werte>`EINTARIF`, `ZWEITARIF`, `MEHRTARIF`, `GAS_G2P5`, `GAS_G4`, `GAS_G6`, `GAS_G10`, `GAS_G16`, `GAS_G25`, `GAS_G40`, `GAS_G65`, `GAS_G100`, `GAS_G160`, `GAS_G250`, `GAS_G350`, `GAS_G400`, `GAS_G4000`, `GAS_G650`, `GAS_G6500`, `GAS_G1000`, `GAS_G10000`, `GAS_G12500`, `GAS_G1600`, `GAS_G16000`, `GAS_G2500`, `IMPULSGEBER_G4_G100`, `IMPULSGEBER_G100`, `MODEM_GSM`, `MODEM_GPRS`, `MODEM_FUNK`, `MODEM_GSM_O_LG`, `MODEM_GSM_M_LG`, `MODEM_FESTNETZ`, `MODEM_GPRS_M_LG`, `PLC_COM`, `ETHERNET_KOM`, `DSL_KOM`, `LTE_KOM`, `RUNDSTEUEREMPFAENGER`, `TARIFSCHALTGERAET`, `ZUSTANDS_MU`, `TEMPERATUR_MU`, `KOMPAKT_MU`, `SYSTEM_MU`, `UNBESTIMMT`, `WASSER_MWZW`, `WASSER_WZWW`, `WASSER_WZ01`, `WASSER_WZ02`, `WASSER_WZ03`, `WASSER_WZ04`, `WASSER_WZ05`, `WASSER_WZ06`, `WASSER_WZ07`, `WASSER_WZ08`, `WASSER_WZ09`, `WASSER_WZ10`, `WASSER_VWZ04`, `WASSER_VWZ05`, `WASSER_VWZ06`, `WASSER_VWZ07`, `WASSER_VWZ10`, `DICHTEMENGENUMWERTER`, `TEMPERATURMENGENUMWERTER`, `ZUSTANDSMENGENUMWERTER`, `BLOCKSTROMWANDLER`, `MESSWANDLERSATZ_IMS_MME`, `KOMBIMESSWANDLER`, `SPANNUNGSWANDLER`</Werte> |
| <span className="hbs-f hbs-e2">[volumenerfassung](/bo4e/202604/com/Geraeteeigenschaften#volumenerfassung)</span> | Volumenerfassung | [Enum Volumenerfassung](/bo4e/202604/enum/Volumenerfassung)<br/><Werte>`HOCHFREQUENZSONDE`, `KENNLINIENKORREKTUR`, `SCHLEICHMENGENUNTERDRUECKUNG`</Werte> |
| <span className="hbs-f hbs-e2">[serialnummer](/bo4e/202604/com/Geraeteeigenschaften#serialnummer)</span> | serialnummer | string |
| <span className="hbs-f hbs-e2">[herstellungsdatum](/bo4e/202604/com/Geraeteeigenschaften#herstellungsdatum)</span> | Produktions-/Herstellungsdatum | string |
| <span className="hbs-f hbs-e2">[baujahr](/bo4e/202604/com/Geraeteeigenschaften#baujahr)</span> | Baujahr/Jahr des in Verkehrs bringens | string |
| <span className="hbs-f hbs-e2">[eichungBis](/bo4e/202604/com/Geraeteeigenschaften#eichungbis)</span> | Eichgültigkeit | string |
| <span className="hbs-f hbs-e2">[faktor](/bo4e/202604/com/Geraeteeigenschaften#faktor)</span> | faktor | number (float) |
| <span className="hbs-f hbs-e2">[firmwareVersion](/bo4e/202604/com/Geraeteeigenschaften#firmwareversion)</span> | Firmware-Version | string |
| <span className="hbs-f hbs-e2">[herstellerTypbezeichnung](/bo4e/202604/com/Geraeteeigenschaften#herstellertypbezeichnung)</span> | Hersteller-Typbezeichnung | string |
| <span className="hbs-f hbs-e2">[simKartenNummer](/bo4e/202604/com/Geraeteeigenschaften#simkartennummer)</span> | SIM-Kartennummer | string |
| <span className="hbs-f hbs-e2">[modemKennungIMSI](/bo4e/202604/com/Geraeteeigenschaften#modemkennungimsi)</span> | Modem-Kennung (IMSI) | string |
| <span className="hbs-f hbs-e2">[tkProvider](/bo4e/202604/com/Geraeteeigenschaften#tkprovider)</span> | Telekommunikationsanbieter | string |
| <span className="hbs-f hbs-e2">[ipVersion](/bo4e/202604/com/Geraeteeigenschaften#ipversion)</span> | IP-Version | string |
| <span className="hbs-f hbs-e1">[volumenerfassung](/bo4e/202604/com/Geraet#volumenerfassung)</span> | Volumenerfassung | [Enum Volumenerfassung](/bo4e/202604/enum/Volumenerfassung)<br/><Werte>`HOCHFREQUENZSONDE`, `KENNLINIENKORREKTUR`, `SCHLEICHMENGENUNTERDRUECKUNG`</Werte> |
| <span className="hbs-f hbs-e1">[weitereGeraetenummern](/bo4e/202604/com/Geraet#weiteregeraetenummern) <span className="hbs-liste">[ ]</span></span> | weitereGeraetenummern | string[] |
| <span className="hbs-g hbs-e0">[zaehlwerke](/bo4e/202604/bo/Zaehler#zaehlwerke) <span className="hbs-liste">[ ]</span></span> | Die Zählwerke des Zählers. | [Zaehlwerk[]](/bo4e/202604/com/Zaehlwerk) |
| <span className="hbs-f hbs-e1">[zaehlwerkId](/bo4e/202604/com/Zaehlwerk#zaehlwerkid)</span> | Identifikation des Zählwerks (Registers) innerhalb des Zählers. Oftmals eine laufende Nummer hinter der<br/>Zählernummer. Z.B. 47110815_1 | string |
| <span className="hbs-f hbs-e1">[bezeichnung](/bo4e/202604/com/Zaehlwerk#bezeichnung)</span> | Zusätzliche Bezeichnung, z.B. Zählwerk_Wirkarbeit. | string |
| <span className="hbs-f hbs-e1">[richtung](/bo4e/202604/com/Zaehlwerk#richtung)</span> | Die Energierichtung, Einspeisung oder Ausspeisung. Details Energierichtung | [Enum Energierichtung](/bo4e/202604/enum/Energierichtung)<br/><Werte>`AUSSP`, `EINSP`</Werte> |
| <span className="hbs-f hbs-e1">[obisKennzahl](/bo4e/202604/com/Zaehlwerk#obiskennzahl)</span> | Die OBIS-Kennzahl für das Zählwerk, die festlegt, welche auf die gemessene Größe mit dem Stand gemeldet wird.<br/>Nur Zählwerkstände mit dieser OBIS-Kennzahl werden an diesem Zählwerk registriert. Beispiel:1-0:1.8.1 für<br/>elektrische Wirkarbeit. | string |
| <span className="hbs-f hbs-e1">[wandlerfaktor](/bo4e/202604/com/Zaehlwerk#wandlerfaktor)</span> | Mit diesem Faktor wird eine Zählerstandsdifferenz multipliziert, um zum eigentlichen Verbrauch im Zeitraum zu<br/>kommen. | number (float) |
| <span className="hbs-f hbs-e1">[einheit](/bo4e/202604/com/Zaehlwerk#einheit)</span> | Die Einheit der gemessenen Größe, z.B. kWh. Details Mengeneinheit | [Enum Mengeneinheit](/bo4e/202604/enum/Mengeneinheit)<br/><Werte>`W`, `WH`, `KW`, `KWH`, `KVARH`, `MW`, `MWH`, `STUECK`, `KUBIKMETER`, `STUNDE`, `TAG`, `MONAT`, `JAHR`, `PROZENT`, `ANZAHL`, `VAR`, `KVAR`, `VARH`, `KWHK`, `Z16`, `KWT`, `WATT_PRO_QUADRATMETER`, `METER_PRO_SEKUNDE`</Werte> |
| <span className="hbs-f hbs-e1">[schwachlastfaehig](/bo4e/202604/com/Zaehlwerk#schwachlastfaehig)</span> | schwachlastfaehig | [Enum Schwachlastfaehig](/bo4e/202604/enum/Schwachlastfaehig)<br/><Werte>`SCHWACHLASTFAEHIG`, `NICHT_SCHWACHLASTFAEHIG`</Werte> |
| <span className="hbs-f hbs-e1">[verbrauchsart](/bo4e/202604/com/Zaehlwerk#verbrauchsart) <span className="hbs-liste">[ ]</span></span> | Stromverbrauchsart/Verbrauchsart Marktlokation | [Enum Verbrauchsart[]](/bo4e/202604/enum/Verbrauchsart)<br/><Werte>`KL`, `W`, `EMOB`, `SB`, `SW`, `WK`</Werte> |
| <span className="hbs-f hbs-e1">[unterbrechbarkeit](/bo4e/202604/com/Zaehlwerk#unterbrechbarkeit)</span> | Stromverbrauchsart/Unterbrechbarkeit Marktlokation | [Enum Unterbrechbarkeit](/bo4e/202604/enum/Unterbrechbarkeit)<br/><Werte>`UV`, `NUV`</Werte> |
| <span className="hbs-f hbs-e1">[waermenutzung](/bo4e/202604/com/Zaehlwerk#waermenutzung)</span> | Stromverbrauchsart/Wärmenutzung Marktlokation | [Enum Waermenutzung](/bo4e/202604/enum/Waermenutzung)<br/><Werte>`SPEICHERHEIZUNG`, `WAERMEPUMPE`, `DIREKTHEIZUNG`, `WAERMEPUMPE_WAERME_KAELTE`, `WAERMEPUMPE_KAELTE`, `WAERMEPUMPE_WAERME`</Werte> |
| <span className="hbs-g hbs-e1">[konzessionsabgabe](/bo4e/202604/com/Zaehlwerk#konzessionsabgabe)</span> | — | [Konzessionsabgabe](/bo4e/202604/com/Konzessionsabgabe) |
| <span className="hbs-f hbs-e2">[satz](/bo4e/202604/com/Konzessionsabgabe#satz)</span> | Art der Konzessionsabgabe | [Enum AbgabeArt](/bo4e/202604/enum/AbgabeArt)<br/><Werte>`KAS`, `SA`, `SAS`, `TA`, `TAS`, `TK`, `TKS`, `TS`, `TSS`</Werte> |
| <span className="hbs-f hbs-e2">[kosten](/bo4e/202604/com/Konzessionsabgabe#kosten)</span> | Kosten | number (float) |
| <span className="hbs-f hbs-e2">[kategorie](/bo4e/202604/com/Konzessionsabgabe#kategorie)</span> | Kategorie | string |
| <span className="hbs-f hbs-e1">[steuerbefreit](/bo4e/202604/com/Zaehlwerk#steuerbefreit)</span> | steuerbefreit | boolean |
| <span className="hbs-f hbs-e1">[vorkommastelle](/bo4e/202604/com/Zaehlwerk#vorkommastelle)</span> | vorkommastelle | integer |
| <span className="hbs-f hbs-e1">[nachkommastelle](/bo4e/202604/com/Zaehlwerk#nachkommastelle)</span> | nachkommastelle | integer |
| <span className="hbs-f hbs-e1">[abrechnungsrelevant](/bo4e/202604/com/Zaehlwerk#abrechnungsrelevant)</span> | abrechnungsrelevant | boolean |
| <span className="hbs-f hbs-e1">[anzahlAblesungen](/bo4e/202604/com/Zaehlwerk#anzahlablesungen)</span> | anzahlAblesungen | integer |
| <span className="hbs-g hbs-e1">[zaehlzeiten](/bo4e/202604/com/Zaehlwerk#zaehlzeiten)</span> | — | [Zaehlzeitregister](/bo4e/202604/com/Zaehlzeitregister) |
| <span className="hbs-f hbs-e2">[register](/bo4e/202604/com/Zaehlzeitregister#register)</span> | Zählzeitregister | string |
| <span className="hbs-f hbs-e2">[zaehlzeitDefinition](/bo4e/202604/com/Zaehlzeitregister#zaehlzeitdefinition)</span> | Zählzeitdefinition | string |
| <span className="hbs-f hbs-e2">[schwachlastfaehig](/bo4e/202604/com/Zaehlzeitregister#schwachlastfaehig)</span> | Schwachlastfähigkeit des Registers | [Enum Schwachlastfaehig](/bo4e/202604/enum/Schwachlastfaehig)<br/><Werte>`SCHWACHLASTFAEHIG`, `NICHT_SCHWACHLASTFAEHIG`</Werte> |
| <span className="hbs-f hbs-e1">[konfiguration](/bo4e/202604/com/Zaehlwerk#konfiguration)</span> | Konfiguration (iMSys) des Zählwerks | string |
| <span className="hbs-f hbs-e1">[messprodukt](/bo4e/202604/com/Zaehlwerk#messprodukt)</span> | messprodukt | string |
| <span className="hbs-f hbs-e1">[wertegranularitaet](/bo4e/202604/com/Zaehlwerk#wertegranularitaet)</span> | Wertegranularitaet | [Enum Wertegranularitaet](/bo4e/202604/enum/Wertegranularitaet)<br/><Werte>`JAEHRLICH`, `HALBJAEHRLICH`, `QUARTALSWEISE`, `MONATLICH`</Werte> |
| <span className="hbs-f hbs-e1">[notwendigkeitZweiteMessung](/bo4e/202604/com/Zaehlwerk#notwendigkeitzweitemessung)</span> | NotwendigkeitZweiteMessung | [Enum NotwendigkeitZweiteMessung](/bo4e/202604/enum/NotwendigkeitZweiteMessung)<br/><Werte>`VORHANDEN`, `NICHT_VORHANDEN`</Werte> |
| <span className="hbs-f hbs-e1">[werteuebermittlungVerwendungszweck](/bo4e/202604/com/Zaehlwerk#werteuebermittlungverwendungszweck)</span> | WerteuebermittlungVerwendungszweck | [Enum WerteuebermittlungVerwendungszweck](/bo4e/202604/enum/WerteuebermittlungVerwendungszweck)<br/><Werte>`VORHANDEN`, `NICHT_VORHANDEN`</Werte> |
| <span className="hbs-f hbs-e1">[artEMobilitaet](/bo4e/202604/com/Zaehlwerk#artemobilitaet)</span> | ArtEmobilitaet | [Enum ArtEmobilitaet](/bo4e/202604/enum/ArtEmobilitaet)<br/><Werte>`WB`, `LS`, `LP`</Werte> |
| <span className="hbs-f hbs-e1">[konfigurationsprodukt](/bo4e/202604/com/Zaehlwerk#konfigurationsprodukt)</span> | konfigurationsprodukt | string |
| <span className="hbs-f hbs-e1">[keinKonfigurationsprodukt](/bo4e/202604/com/Zaehlwerk#keinkonfigurationsprodukt)</span> | keinKonfigurationsprodukt | boolean |
| <span className="hbs-f hbs-e1">[leistungskurvendefinition](/bo4e/202604/com/Zaehlwerk#leistungskurvendefinition)</span> | leistungskurvendefinition | string |
| <span className="hbs-g hbs-e1">[verwendungszwecke](/bo4e/202604/com/Zaehlwerk#verwendungszwecke) <span className="hbs-liste">[ ]</span></span> | Verwendungungszweck der Werte Marktlokation | [Verwendungszweck[]](/bo4e/202604/com/Verwendungszweck) |
| <span className="hbs-f hbs-e2">[marktrolle](/bo4e/202604/com/Verwendungszweck#marktrolle)</span> | Diese Rollen kann ein Marktteilnehmer einnehmen | [Enum Marktrolle](/bo4e/202604/enum/Marktrolle)<br/><Werte>`NB`, `LF`, `MSB`, `MSBA`, `GMSB`, `MDL`, `DL`, `BKV`, `UENB`, `KUNDE-SELBST-NN`, `MGV`, `EIV`, `RB`, `KUNDE`, `INTERESSENT`, `KN`, `UBA`, `BIKO`, `ESA`</Werte> |
| <span className="hbs-f hbs-e2">[zweck](/bo4e/202604/com/Verwendungszweck#zweck) <span className="hbs-liste">[ ]</span></span> | zweck | [Enum VerwendungszweckValue[]](/bo4e/202604/enum/VerwendungszweckValue)<br/><Werte>`NETZNUTZUNGSABRECHNUNG`, `BILANZKREISABRECHNUNG`, `MEHRMINDERMENGENABRECHNUNG`, `ENDKUNDENABRECHNUNG`, `UEBERMITTLUNG_AN_DAS_HKNR`, `BLINDARBEITSABRECHNUNG`, `ERMITTLUNG_AUSGEGLICHENHEIT_BILANZKREIS`, `BLINDARBEITABRECHNUNG_BETRIEBSFUEHRUNG`, `ES_LIEGT_KEIN_VERWENDUNGSZWECK_VOR`</Werte> |
| <span className="hbs-f hbs-e1">[verwendungszweckNB](/bo4e/202604/com/Zaehlwerk#verwendungszwecknb)</span> | Codes gemäß Codeliste der Verwendungszwecke Verwendungszweck NB | string |
| <span className="hbs-f hbs-e1">[verwendungszweckLF](/bo4e/202604/com/Zaehlwerk#verwendungszwecklf)</span> | Codes gemäß Codeliste der Verwendungszwecke Verwendungszweck LF | string |
| <span className="hbs-f hbs-e1">[verwendungszweckUENB](/bo4e/202604/com/Zaehlwerk#verwendungszweckuenb)</span> | Codes gemäß Codeliste der Verwendungszwecke Verwendungszweck ÜNB | string |
| <span className="hbs-f hbs-e1">[keinProdukt](/bo4e/202604/com/Zaehlwerk#keinprodukt)</span> | CCI+11++ZF6: keinProdukt zugeordnet | boolean |
| <span className="hbs-f hbs-e0">[datenqualitaet](/bo4e/202604/bo/Zaehler#datenqualitaet)</span> | Datenqualitaet | [Enum Datenqualitaet](/bo4e/202604/enum/Datenqualitaet)<br/><Werte>`ERWARTETE_DATEN`, `IM_SYSTEM_VORHANDENE_DATEN`, `INFORMATIVE_DATEN`, `GUELTIGE_DATEN`, `KEINE_DATEN`, `IM_SYSTEM_KEINE_DATEN_VORHANDEN`, `KEINE_DATEN_ERWARTET`, `DIFFERENZ_DATEN`, `DIFFERENZ_ERWARTETE_DATEN`, `DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</Werte> |
| <span className="hbs-g hbs-e0">[gueltigkeitszeitraum](/bo4e/202604/bo/Zaehler#gueltigkeitszeitraum)</span> | — | [Zeitraum](/bo4e/202604/com/Zeitraum) |
| <span className="hbs-f hbs-e1">[zeiteinheit](/bo4e/202604/com/Zeitraum#zeiteinheit)</span> | Zeiteinheit | [Enum Zeiteinheit](/bo4e/202604/enum/Zeiteinheit)<br/><Werte>`SEKUNDE`, `MINUTE`, `STUNDE`, `VIERTEL_STUNDE`, `TAG`, `WOCHE`, `MONAT`, `QUARTAL`, `HALBJAHR`, `JAHR`</Werte> |
| <span className="hbs-f hbs-e1">[dauer](/bo4e/202604/com/Zeitraum#dauer)</span> | dauer | integer |
| <span className="hbs-f hbs-e1">[startdatum](/bo4e/202604/com/Zeitraum#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e1">[enddatum](/bo4e/202604/com/Zeitraum#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-f hbs-e1">[einheit](/bo4e/202604/com/Zeitraum#einheit)</span> | Zeiteinheit | [Enum Zeiteinheit](/bo4e/202604/enum/Zeiteinheit)<br/><Werte>`SEKUNDE`, `MINUTE`, `STUNDE`, `VIERTEL_STUNDE`, `TAG`, `WOCHE`, `MONAT`, `QUARTAL`, `HALBJAHR`, `JAHR`</Werte> |
| <span className="hbs-f hbs-e1">[ableseZeitraum](/bo4e/202604/com/Zeitraum#ablesezeitraum)</span> | ableseZeitraum | string |
| <span className="hbs-f hbs-e1">[abrechnungsZeitraum](/bo4e/202604/com/Zeitraum#abrechnungszeitraum)</span> | abrechnungsZeitraum | string |
| <span className="hbs-f hbs-e1">[zeitraumText](/bo4e/202604/com/Zeitraum#zeitraumtext)</span> | zeitraumText | string |
| <span className="hbs-f hbs-e1">[zeitraumId](/bo4e/202604/com/Zeitraum#zeitraumid)</span> | zeitraumId | integer |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### zaehlernummer

41 Verwendung(en) in den Nachrichtentypen MSCONS, UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_13002](/schnittstellen/202604/pruefi/MSCONS/PI_13002) | Prüfi | MSCONS | stammdaten › ZAEHLER |
| [PI_13017](/schnittstellen/202604/pruefi/MSCONS/PI_13017) | Prüfi | MSCONS | stammdaten › ZAEHLER |
| [PI_44001](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44001) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44016](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44016) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44035](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44035) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44039](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44039) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44040](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44040) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44043](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44043) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44060](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44060) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44116](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44116) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44117](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44117) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44143](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44143) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44145](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44145) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44147](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44147) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44148](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44148) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44149](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44149) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44168](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_55035](/schnittstellen/202604/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55039](/schnittstellen/202604/pruefi/UTILMD/PI_55039) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55040](/schnittstellen/202604/pruefi/UTILMD/PI_55040) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55042](/schnittstellen/202604/pruefi/UTILMD/PI_55042) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55060](/schnittstellen/202604/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55074](/schnittstellen/202604/pruefi/UTILMD/PI_55074) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55075](/schnittstellen/202604/pruefi/UTILMD/PI_55075) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55095](/schnittstellen/202604/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55553](/schnittstellen/202604/pruefi/UTILMD/PI_55553) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55555](/schnittstellen/202604/pruefi/UTILMD/PI_55555) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55600](/schnittstellen/202604/pruefi/UTILMD/PI_55600) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55601](/schnittstellen/202604/pruefi/UTILMD/PI_55601) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55643](/schnittstellen/202604/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55648](/schnittstellen/202604/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55653](/schnittstellen/202604/pruefi/UTILMD/PI_55653) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55658](/schnittstellen/202604/pruefi/UTILMD/PI_55658) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55663](/schnittstellen/202604/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55669](/schnittstellen/202604/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | stammdaten › ZAEHLER |

### zaehlerauspraegung

12 Verwendung(en) in den Nachrichtentypen QUOTES, UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_15001](/schnittstellen/202604/pruefi/QUOTES/PI_15001) | Prüfi | QUOTES | stammdaten › ZAEHLER |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55074](/schnittstellen/202604/pruefi/UTILMD/PI_55074) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55075](/schnittstellen/202604/pruefi/UTILMD/PI_55075) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55643](/schnittstellen/202604/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55648](/schnittstellen/202604/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55653](/schnittstellen/202604/pruefi/UTILMD/PI_55653) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55658](/schnittstellen/202604/pruefi/UTILMD/PI_55658) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55663](/schnittstellen/202604/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55669](/schnittstellen/202604/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | stammdaten › ZAEHLER |

### zaehlertyp

29 Verwendung(en) in den Nachrichtentypen QUOTES, UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_15001](/schnittstellen/202604/pruefi/QUOTES/PI_15001) | Prüfi | QUOTES | stammdaten › ZAEHLER |
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44035](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44035) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44043](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44043) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44060](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44060) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44116](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44116) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44117](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44117) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44143](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44143) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44145](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44145) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44147](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44147) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44148](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44148) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44149](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44149) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44168](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_55035](/schnittstellen/202604/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55060](/schnittstellen/202604/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55074](/schnittstellen/202604/pruefi/UTILMD/PI_55074) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55075](/schnittstellen/202604/pruefi/UTILMD/PI_55075) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55095](/schnittstellen/202604/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55643](/schnittstellen/202604/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55648](/schnittstellen/202604/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55653](/schnittstellen/202604/pruefi/UTILMD/PI_55653) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55658](/schnittstellen/202604/pruefi/UTILMD/PI_55658) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55663](/schnittstellen/202604/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55669](/schnittstellen/202604/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | stammdaten › ZAEHLER |

### tarifart

12 Verwendung(en) in den Nachrichtentypen QUOTES, UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_15001](/schnittstellen/202604/pruefi/QUOTES/PI_15001) | Prüfi | QUOTES | stammdaten › ZAEHLER |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55074](/schnittstellen/202604/pruefi/UTILMD/PI_55074) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55075](/schnittstellen/202604/pruefi/UTILMD/PI_55075) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55643](/schnittstellen/202604/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55648](/schnittstellen/202604/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55653](/schnittstellen/202604/pruefi/UTILMD/PI_55653) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55658](/schnittstellen/202604/pruefi/UTILMD/PI_55658) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55663](/schnittstellen/202604/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55669](/schnittstellen/202604/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | stammdaten › ZAEHLER |

### eichungBis

1 Verwendung(en) in den Nachrichtentypen QUOTES.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_15001](/schnittstellen/202604/pruefi/QUOTES/PI_15001) | Prüfi | QUOTES | stammdaten › ZAEHLER |

### gateway

16 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55035](/schnittstellen/202604/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55060](/schnittstellen/202604/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55074](/schnittstellen/202604/pruefi/UTILMD/PI_55074) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55075](/schnittstellen/202604/pruefi/UTILMD/PI_55075) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55095](/schnittstellen/202604/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55553](/schnittstellen/202604/pruefi/UTILMD/PI_55553) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55555](/schnittstellen/202604/pruefi/UTILMD/PI_55555) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55643](/schnittstellen/202604/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55648](/schnittstellen/202604/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55653](/schnittstellen/202604/pruefi/UTILMD/PI_55653) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55658](/schnittstellen/202604/pruefi/UTILMD/PI_55658) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55663](/schnittstellen/202604/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55669](/schnittstellen/202604/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | stammdaten › ZAEHLER |

### fernschaltung

7 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55643](/schnittstellen/202604/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55648](/schnittstellen/202604/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55663](/schnittstellen/202604/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55669](/schnittstellen/202604/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | stammdaten › ZAEHLER |

### messwerterfassung

25 Verwendung(en) in den Nachrichtentypen QUOTES, UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_15001](/schnittstellen/202604/pruefi/QUOTES/PI_15001) | Prüfi | QUOTES | stammdaten › ZAEHLER |
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44035](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44035) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44043](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44043) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44060](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44060) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44116](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44116) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44117](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44117) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44143](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44143) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44145](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44145) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44147](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44147) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44148](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44148) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44149](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44149) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44168](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_55035](/schnittstellen/202604/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55060](/schnittstellen/202604/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55095](/schnittstellen/202604/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55643](/schnittstellen/202604/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55648](/schnittstellen/202604/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55663](/schnittstellen/202604/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55669](/schnittstellen/202604/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | stammdaten › ZAEHLER |

### zaehlertypspezifikation

29 Verwendung(en) in den Nachrichtentypen QUOTES, UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_15001](/schnittstellen/202604/pruefi/QUOTES/PI_15001) | Prüfi | QUOTES | stammdaten › ZAEHLER |
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44035](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44035) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44043](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44043) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44060](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44060) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44116](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44116) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44117](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44117) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44143](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44143) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44145](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44145) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44147](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44147) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44148](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44148) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44149](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44149) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44168](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_55035](/schnittstellen/202604/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55060](/schnittstellen/202604/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55074](/schnittstellen/202604/pruefi/UTILMD/PI_55074) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55075](/schnittstellen/202604/pruefi/UTILMD/PI_55075) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55095](/schnittstellen/202604/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55643](/schnittstellen/202604/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55648](/schnittstellen/202604/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55653](/schnittstellen/202604/pruefi/UTILMD/PI_55653) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55658](/schnittstellen/202604/pruefi/UTILMD/PI_55658) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55663](/schnittstellen/202604/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55669](/schnittstellen/202604/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | stammdaten › ZAEHLER |

### befestigungsart

14 Verwendung(en) in den Nachrichtentypen QUOTES, UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_15001](/schnittstellen/202604/pruefi/QUOTES/PI_15001) | Prüfi | QUOTES | stammdaten › ZAEHLER |
| [PI_44043](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44043) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44060](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44060) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44116](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44116) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44148](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44148) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44149](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44149) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44168](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55643](/schnittstellen/202604/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55648](/schnittstellen/202604/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55663](/schnittstellen/202604/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55669](/schnittstellen/202604/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | stammdaten › ZAEHLER |

### zaehlergroesse

15 Verwendung(en) in den Nachrichtentypen QUOTES, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_15001](/schnittstellen/202604/pruefi/QUOTES/PI_15001) | Prüfi | QUOTES | stammdaten › ZAEHLER |
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44035](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44035) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44043](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44043) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44060](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44060) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44116](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44116) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44117](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44117) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44143](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44143) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44145](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44145) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44147](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44147) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44148](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44148) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44149](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44149) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44168](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |

### volumenerfassung

6 Verwendung(en) in den Nachrichtentypen UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_44043](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44043) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44060](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44060) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44116](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44116) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44148](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44148) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44149](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44149) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44168](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |

### messlokationsId

24 Verwendung(en) in den Nachrichtentypen UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44035](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44035) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44040](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44040) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44043](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44043) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44060](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44060) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44116](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44116) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44117](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44117) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44143](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44143) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44145](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44145) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44147](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44147) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44148](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44148) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44149](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44149) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_44168](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER |
| [PI_55035](/schnittstellen/202604/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55040](/schnittstellen/202604/pruefi/UTILMD/PI_55040) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55060](/schnittstellen/202604/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55074](/schnittstellen/202604/pruefi/UTILMD/PI_55074) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55075](/schnittstellen/202604/pruefi/UTILMD/PI_55075) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55095](/schnittstellen/202604/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › ZAEHLER |

### marktlokationsId

5 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55074](/schnittstellen/202604/pruefi/UTILMD/PI_55074) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55075](/schnittstellen/202604/pruefi/UTILMD/PI_55075) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › ZAEHLER |

### datenqualitaet

8 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55553](/schnittstellen/202604/pruefi/UTILMD/PI_55553) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55555](/schnittstellen/202604/pruefi/UTILMD/PI_55555) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55643](/schnittstellen/202604/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55648](/schnittstellen/202604/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55653](/schnittstellen/202604/pruefi/UTILMD/PI_55653) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55658](/schnittstellen/202604/pruefi/UTILMD/PI_55658) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55663](/schnittstellen/202604/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | stammdaten › ZAEHLER |
| [PI_55669](/schnittstellen/202604/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | stammdaten › ZAEHLER |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
