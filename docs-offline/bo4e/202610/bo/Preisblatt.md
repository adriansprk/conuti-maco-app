# Preisblatt
<span hidden data-pagefind-meta={"title:Preisblatt — BO4E-Geschäftsobjekt (FV 202610)"} />

BO4E-Geschäftsobjekt · 12 Felder · 1 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="botyp"></a>`boTyp` <span className="hbs-pflicht">\*</span> | [Enum BOTyp](/bo4e/202610/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> | Typ des BO |
| <a id="versionstruktur"></a>`versionStruktur` <span className="hbs-pflicht">\*</span> | string | versionStruktur |
| <a id="bezeichnung"></a>`bezeichnung` | string | Bezeichnung des Auf-/Abschlags |
| <a id="gueltigkeit"></a>`gueltigkeit` | [Zeitraum](/bo4e/202610/com/Zeitraum) | Der Zeitraum für den der Preis festgelegt ist. Details siehe Zeitraum |
| <a id="preisstatus"></a>`preisstatus` | [Enum Preisstatus](/bo4e/202610/enum/Preisstatus)<br/><Werte>`VORLAEUFIG`, `ENDGUELTIG`</Werte> | Gibt den Status des veröffentlichten Preises an |
| <a id="sparte"></a>`sparte` | [Enum Sparte](/bo4e/202610/enum/Sparte)<br/><Werte>`STROM`, `GAS`, `FERNWAERME`, `NAHWAERME`, `WASSER`, `ABWASSER`</Werte> | Strom oder Gas. |
| <a id="preisnetzbetreibercodenummer"></a>`preisNetzbetreiberCodenummer` | string | Preise des Netzbetreibers |
| <a id="bilanzierungsdatum"></a>`bilanzierungsdatum` | string (date-time) | bilanzierungsdatum |
| <a id="regelzone"></a>`regelzone` | string | regelzone |
| <a id="leistungstyp"></a>`leistungstyp` | [Enum Leistungstyp](/bo4e/202610/enum/Leistungstyp)<br/><Werte>`ARBEITSPREIS_WIRKARBEIT`, `LEISTUNGSPREIS_WIRKLEISTUNG`, `ARBEITSPREIS_BLINDARBEIT_IND`, `ARBEITSPREIS_BLINDARBEIT_KAP`, `GRUNDPREIS`, `MEHRMINDERMENGE`, `MESSSTELLENBETRIEB`, `MESSDIENSTLEISTUNG`, `MESSDIENSTLEISTUNG_INKL_MESSUNG`, `ABRECHNUNG`, `KONZESSIONS_ABGABE`, `KWK_UMLAGE`, `OFFSHORE_UMLAGE`, `ABLAV_UMLAGE`, `REGELENERGIE_UMLAGE`, `BILANZIERUNG_UMLAGE`, `AUSLESUNG_ZUSAETZLICH`, `ABLESUNG_ZUSAETZLICH`, `ABRECHNUNG_ZUSAETZLICH`, `SPERRUNG`, `ENTSPERRUNG`, `MAHNKOSTEN`, `INKASSOKOSTEN`</Werte> | Standardisierte Bezeichnung für die abgerechnete Leistungserbringung. Details Leistungstyp |
| <a id="nichtgenutzt"></a>`nichtGenutzt` | boolean | nichtGenutzt |
| <a id="preispositionen"></a>`preispositionen` | [Preisposition[]](/bo4e/202610/com/Preisposition) | Die einzelnen Positionen, die mit dem Preisblatt abgerechnet werden können. Z.B. Arbeitspreis, Grundpreis etc. Details siehe Preisposition |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[boTyp](/bo4e/202610/bo/Preisblatt#botyp) <span className="hbs-pflicht">\*</span></span> | Typ des BO | [Enum BOTyp](/bo4e/202610/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> |
| <span className="hbs-f hbs-e0">[versionStruktur](/bo4e/202610/bo/Preisblatt#versionstruktur) <span className="hbs-pflicht">\*</span></span> | versionStruktur | string |
| <span className="hbs-f hbs-e0">[bezeichnung](/bo4e/202610/bo/Preisblatt#bezeichnung)</span> | Bezeichnung des Auf-/Abschlags | string |
| <span className="hbs-g hbs-e0">[gueltigkeit](/bo4e/202610/bo/Preisblatt#gueltigkeit)</span> | Der Zeitraum für den der Preis festgelegt ist. Details siehe Zeitraum | [Zeitraum](/bo4e/202610/com/Zeitraum) |
| <span className="hbs-f hbs-e1">[zeiteinheit](/bo4e/202610/com/Zeitraum#zeiteinheit)</span> | Zeiteinheit | [Enum Zeiteinheit](/bo4e/202610/enum/Zeiteinheit)<br/><Werte>`SEKUNDE`, `MINUTE`, `STUNDE`, `VIERTEL_STUNDE`, `TAG`, `WOCHE`, `MONAT`, `QUARTAL`, `HALBJAHR`, `JAHR`</Werte> |
| <span className="hbs-f hbs-e1">[dauer](/bo4e/202610/com/Zeitraum#dauer)</span> | dauer | integer |
| <span className="hbs-f hbs-e1">[startdatum](/bo4e/202610/com/Zeitraum#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e1">[enddatum](/bo4e/202610/com/Zeitraum#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-f hbs-e1">[einheit](/bo4e/202610/com/Zeitraum#einheit)</span> | Zeiteinheit | [Enum Zeiteinheit](/bo4e/202610/enum/Zeiteinheit)<br/><Werte>`SEKUNDE`, `MINUTE`, `STUNDE`, `VIERTEL_STUNDE`, `TAG`, `WOCHE`, `MONAT`, `QUARTAL`, `HALBJAHR`, `JAHR`</Werte> |
| <span className="hbs-f hbs-e1">[ableseZeitraum](/bo4e/202610/com/Zeitraum#ablesezeitraum)</span> | ableseZeitraum | string |
| <span className="hbs-f hbs-e1">[abrechnungsZeitraum](/bo4e/202610/com/Zeitraum#abrechnungszeitraum)</span> | abrechnungsZeitraum | string |
| <span className="hbs-f hbs-e1">[zeitraumText](/bo4e/202610/com/Zeitraum#zeitraumtext)</span> | zeitraumText | string |
| <span className="hbs-f hbs-e1">[zeitraumId](/bo4e/202610/com/Zeitraum#zeitraumid)</span> | zeitraumId | integer |
| <span className="hbs-f hbs-e0">[preisstatus](/bo4e/202610/bo/Preisblatt#preisstatus)</span> | Gibt den Status des veröffentlichten Preises an | [Enum Preisstatus](/bo4e/202610/enum/Preisstatus)<br/><Werte>`VORLAEUFIG`, `ENDGUELTIG`</Werte> |
| <span className="hbs-f hbs-e0">[sparte](/bo4e/202610/bo/Preisblatt#sparte)</span> | Strom oder Gas. | [Enum Sparte](/bo4e/202610/enum/Sparte)<br/><Werte>`STROM`, `GAS`, `FERNWAERME`, `NAHWAERME`, `WASSER`, `ABWASSER`</Werte> |
| <span className="hbs-f hbs-e0">[preisNetzbetreiberCodenummer](/bo4e/202610/bo/Preisblatt#preisnetzbetreibercodenummer)</span> | Preise des Netzbetreibers | string |
| <span className="hbs-f hbs-e0">[bilanzierungsdatum](/bo4e/202610/bo/Preisblatt#bilanzierungsdatum)</span> | bilanzierungsdatum | string (date-time) |
| <span className="hbs-f hbs-e0">[regelzone](/bo4e/202610/bo/Preisblatt#regelzone)</span> | regelzone | string |
| <span className="hbs-f hbs-e0">[leistungstyp](/bo4e/202610/bo/Preisblatt#leistungstyp)</span> | Standardisierte Bezeichnung für die abgerechnete Leistungserbringung. Details Leistungstyp | [Enum Leistungstyp](/bo4e/202610/enum/Leistungstyp)<br/><Werte>`ARBEITSPREIS_WIRKARBEIT`, `LEISTUNGSPREIS_WIRKLEISTUNG`, `ARBEITSPREIS_BLINDARBEIT_IND`, `ARBEITSPREIS_BLINDARBEIT_KAP`, `GRUNDPREIS`, `MEHRMINDERMENGE`, `MESSSTELLENBETRIEB`, `MESSDIENSTLEISTUNG`, `MESSDIENSTLEISTUNG_INKL_MESSUNG`, `ABRECHNUNG`, `KONZESSIONS_ABGABE`, `KWK_UMLAGE`, `OFFSHORE_UMLAGE`, `ABLAV_UMLAGE`, `REGELENERGIE_UMLAGE`, `BILANZIERUNG_UMLAGE`, `AUSLESUNG_ZUSAETZLICH`, `ABLESUNG_ZUSAETZLICH`, `ABRECHNUNG_ZUSAETZLICH`, `SPERRUNG`, `ENTSPERRUNG`, `MAHNKOSTEN`, `INKASSOKOSTEN`</Werte> |
| <span className="hbs-f hbs-e0">[nichtGenutzt](/bo4e/202610/bo/Preisblatt#nichtgenutzt)</span> | nichtGenutzt | boolean |
| <span className="hbs-g hbs-e0">[preispositionen](/bo4e/202610/bo/Preisblatt#preispositionen) <span className="hbs-liste">[ ]</span></span> | Die einzelnen Positionen, die mit dem Preisblatt abgerechnet werden können. Z.B. Arbeitspreis, Grundpreis etc.<br/>Details siehe Preisposition | [Preisposition[]](/bo4e/202610/com/Preisposition) |
| <span className="hbs-f hbs-e1">[berechnungsmethode](/bo4e/202610/com/Preisposition#berechnungsmethode)</span> | Das Modell, das der Preisbildung zugrunde liegt. Details Kalkulationsmethode | [Enum Kalkulationsmethode](/bo4e/202610/enum/Kalkulationsmethode)<br/><Werte>`KEINE`, `STAFFELN`, `ZONEN`, `VORZONEN_GP`, `SIGMOID`, `BLINDARBEIT_GT_50_PROZENT`, `BLINDARBEIT_GT_40_PROZENT`, `AP_GP_ZONEN`, `LP_INSTALL_LEISTUNG`, `AP_TRANSPORT_ODER_VERTEILNETZ`, `AP_TRANSPORT_ODER_VERTEILNETZ_ORTSVERTEILNETZ_SIGMOID`, `LP_JAHRESVERBRAUCH`, `LP_TRANSPORT_ODER_VERTEILNETZ`, `LP_TRANSPORT_ODER_VERTEILNETZ_ORTSVERTEILNETZ_SIGMOID`, `FUNKTIONEN`, `VERBRAUCH_UEBER_SLP_GRENZE_FUNKTIONSBEZOGEN_WEITERE_BERECHNUNG_ALS_LGK`</Werte> |
| <span className="hbs-f hbs-e1">[leistungstyp](/bo4e/202610/com/Preisposition#leistungstyp)</span> | Standardisierte Bezeichnung für die abgerechnete Leistungserbringung. Details Leistungstyp | [Enum Leistungstyp](/bo4e/202610/enum/Leistungstyp)<br/><Werte>`ARBEITSPREIS_WIRKARBEIT`, `LEISTUNGSPREIS_WIRKLEISTUNG`, `ARBEITSPREIS_BLINDARBEIT_IND`, `ARBEITSPREIS_BLINDARBEIT_KAP`, `GRUNDPREIS`, `MEHRMINDERMENGE`, `MESSSTELLENBETRIEB`, `MESSDIENSTLEISTUNG`, `MESSDIENSTLEISTUNG_INKL_MESSUNG`, `ABRECHNUNG`, `KONZESSIONS_ABGABE`, `KWK_UMLAGE`, `OFFSHORE_UMLAGE`, `ABLAV_UMLAGE`, `REGELENERGIE_UMLAGE`, `BILANZIERUNG_UMLAGE`, `AUSLESUNG_ZUSAETZLICH`, `ABLESUNG_ZUSAETZLICH`, `ABRECHNUNG_ZUSAETZLICH`, `SPERRUNG`, `ENTSPERRUNG`, `MAHNKOSTEN`, `INKASSOKOSTEN`</Werte> |
| <span className="hbs-f hbs-e1">[leistungsbezeichnung](/bo4e/202610/com/Preisposition#leistungsbezeichnung)</span> | Bezeichnung für die in der Position abgebildete Leistungserbringung | [Enum Leistungsbezeichnung](/bo4e/202610/enum/Leistungsbezeichnung)<br/><Werte>`POG_VERBRAUCH_IMS_UEBER_100K`, `POG_VERBRAUCH_IMS_50K_BIS_100K`, `POG_VERBRAUCH_IMS_20K_BIS_50K`, `POG_VERBRAUCH_IMS_10K_BIS_20K`, `POG_VERBRAUCH_IMS_UNTERBRECHBAR`, `POG_VERBRAUCH_IMS_6K_BIS_10K`, `POG_ERZEUGUNG_IMS_7_BIS_15`, `POG_ERZEUGUNG_IMS_15_BIS_30`, `POG_ERZEUGUNG_IMS_30_BIS_100`, `POG_ERZEUGUNG_IMS_UEBER_100`, `POG_MME`, `POG_VERBRAUCH_IMS_4K_BIS_6K`, `POG_VERBRAUCH_IMS_3K_BIS_4K`, `POG_VERBRAUCH_IMS_2K_BIS_3K`, `POG_VERBRAUCH_IMS_0_BIS_2K`, `POG_ERZEUGUNG_IMS_OPTIONAL`, `ZUSATZLEISTUNG`</Werte> |
| <span className="hbs-f hbs-e1">[preiseinheit](/bo4e/202610/com/Preisposition#preiseinheit)</span> | Festlegung, mit welcher Preiseinheit abgerechnet wird, z.B. Ct. oder €. Details<br/>Waehrungseinheit | [Enum Waehrungseinheit](/bo4e/202610/enum/Waehrungseinheit)<br/><Werte>`EUR`, `CT`</Werte> |
| <span className="hbs-f hbs-e1">[bezugsgroesse](/bo4e/202610/com/Preisposition#bezugsgroesse)</span> | Hier wird festgelegt, auf welche Bezugsgröße sich der Preis bezieht, z.B. kWh oder Stück. Details<br/>Mengeneinheit | [Enum Mengeneinheit](/bo4e/202610/enum/Mengeneinheit)<br/><Werte>`W`, `WH`, `KW`, `KWH`, `KVARH`, `MW`, `MWH`, `STUECK`, `KUBIKMETER`, `STUNDE`, `TAG`, `MONAT`, `JAHR`, `PROZENT`, `ANZAHL`, `VAR`, `KVAR`, `VARH`, `KWHK`, `Z16`, `KWT`, `WATT_PRO_QUADRATMETER`, `METER_PRO_SEKUNDE`</Werte> |
| <span className="hbs-f hbs-e1">[zeitbasis](/bo4e/202610/com/Preisposition#zeitbasis)</span> | Die Zeit(dauer) auf die sich der Preis bezieht. Z.B. ein Jahr für einen Leistungspreis der in €/kW/Jahr<br/>ausgegeben wird. | [Enum Zeiteinheit](/bo4e/202610/enum/Zeiteinheit)<br/><Werte>`SEKUNDE`, `MINUTE`, `STUNDE`, `VIERTEL_STUNDE`, `TAG`, `WOCHE`, `MONAT`, `QUARTAL`, `HALBJAHR`, `JAHR`</Werte> |
| <span className="hbs-f hbs-e1">[tarifzeit](/bo4e/202610/com/Preisposition#tarifzeit)</span> | Festlegung, für welche Tarifzeit der Preis hier festgelegt ist. | [Enum Tarifzeit](/bo4e/202610/enum/Tarifzeit)<br/><Werte>`TZ_STANDARD`, `TZ_HT`, `TZ_NT`</Werte> |
| <span className="hbs-f hbs-e1">[bdewArtikelnummer](/bo4e/202610/com/Preisposition#bdewartikelnummer)</span> | Eine vom BDEW standardisierte Bezeichnung für die abgerechnete Leistungserbringung. Diese Artikelnummer wird<br/>auch im Rechnungsteil der INVOIC verwendet. | [Enum BDEWArtikelnummer](/bo4e/202610/enum/BDEWArtikelnummer)<br/><Werte>`LEISTUNG`, `LEISTUNG_PAUSCHAL`, `GRUNDPREIS`, `REGELENERGIE_ARBEIT`, `REGELENERGIE_LEISTUNG`, `NOTSTROMLIEFERUNG_ARBEIT`, `NOTSTROMLIEFERUNG_LEISTUNG`, `RESERVENETZKAPAZITAET`, `RESERVELEISTUNG`, `ZUSAETZLICHE_ABLESUNG`, `PRUEFGEBUEHREN_AUSSERPLANMAESSIG`, `WIRKARBEIT`, `SINGULAER_GENUTZTE_BETRIEBSMITTEL`, `ABGABE_KWKG`, `ABSCHLAG`, `KONZESSIONSABGABE`, `ENTGELT_FERNAUSLESUNG`, `UNTERMESSUNG`, `BLINDMEHRARBEIT`, `ENTGELT_ABRECHNUNG`, `SPERRKOSTEN`, `ENTSPERRKOSTEN`, `MAHNKOSTEN`, `MEHR_MINDERMENGEN`, `INKASSOKOSTEN`, `BLINDMEHRLEISTUNG`, `ENTGELT_MESSUNG_ABLESUNG`, `ENTGELT_EINBAU_BETRIEB_WARTUNG_MESSTECHNIK`, `AUSGLEICHSENERGIE`, `AUSGLEICHSENERGIE_UNTERDECKUNG`, `ZAEHLEINRICHTUNG`, `WANDLER_MENGENUMWERTER`, `KOMMUNIKATIONSEINRICHTUNG`, `TECHNISCHE_STEUEREINRICHTUNG`, `PARAGRAF_19_STROM_NEV_UMLAGE`, `BEFESTIGUNGSEINRICHTUNG`, `OFFSHORE_HAFTUNGSUMLAGE`, `FIXE_ARBEITSENTGELTKOMPONENTE`, `FIXE_LEISTUNGSENTGELTKOMPONENTE`, `UMLAGE_ABSCHALTBARE_LASTEN`, `MEHRMENGE`, `MINDERMENGE`, `ENERGIESTEUER`, `SMARTMETER_GATEWAY`, `STEUERBOX`, `MSB_INKL_MESSUNG`, `ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_2_1_MSBG`, `ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_2_2_MSBG`, `ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_2_3_MSBG`, `ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_2_4_MSBG`, `ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_2_5_MSBG`, `ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_3_MSBG`, `ENTGELT_KAPAZITAETEN`</Werte> |
| <span className="hbs-f hbs-e1">[zonungsgroesse](/bo4e/202610/com/Preisposition#zonungsgroesse)</span> | Mit der Menge der hier angegebenen Größe wird die Staffelung/Zonung durchgeführt. Z.B. Vollbenutzungsstunden. | [Enum Bemessungsgroesse](/bo4e/202610/enum/Bemessungsgroesse)<br/><Werte>`WIRKARBEIT_EL`, `LEISTUNG_EL`, `BLINDARBEIT_KAP`, `BLINDARBEIT_IND`, `BLINDLEISTUNG_KAP`, `BLINDLEISTUNG_IND`, `WIRKARBEIT_TH`, `LEISTUNG_TH`, `VOLUMEN`, `VOLUMENSTROM`, `BENUTZUNGSDAUER`, `ANZAHL`</Werte> |
| <span className="hbs-f hbs-e1">[preisschluesselstamm](/bo4e/202610/com/Preisposition#preisschluesselstamm)</span> | Preisschlüsselstamm&gt; | string |
| <span className="hbs-f hbs-e1">[positionsnummer](/bo4e/202610/com/Preisposition#positionsnummer)</span> | Fortlaufende Nummer für die Preisposition | integer |
| <span className="hbs-f hbs-e1">[messebene](/bo4e/202610/com/Preisposition#messebene)</span> | Vgl. PRICAT IMD 7009 | [Enum Netzebene](/bo4e/202610/enum/Netzebene)<br/><Werte>`NSP`, `MSP`, `HSP`, `HSS`, `MSP_NSP_UMSP`, `HSP_MSP_UMSP`, `HSS_HSP_UMSP`, `HD`, `MD`, `ND`</Werte> |
| <span className="hbs-f hbs-e1">[beschreibung](/bo4e/202610/com/Preisposition#beschreibung)</span> | Produkt-/Leistungsbeschreibung, wenn IMD+X vorhanden Vgl. PRICAT IMD 7008 | string |
| <span className="hbs-f hbs-e1">[beschreibungsformat](/bo4e/202610/com/Preisposition#beschreibungsformat)</span> | Vgl. PRICAT IMD 7077 | [Enum Beschreibungsformat](/bo4e/202610/enum/Beschreibungsformat)<br/><Werte>`CODE`, `FREIER_TEXT`, `TEILSTRUKTURIERT`</Werte> |
| <span className="hbs-g hbs-e1">[verarbeitungszeitraum](/bo4e/202610/com/Preisposition#verarbeitungszeitraum)</span> | Verarbeitungszeitraum. Details Zeitraum | [Zeitraum](/bo4e/202610/com/Zeitraum) |
| <span className="hbs-f hbs-e2">[zeiteinheit](/bo4e/202610/com/Zeitraum#zeiteinheit)</span> | Zeiteinheit | [Enum Zeiteinheit](/bo4e/202610/enum/Zeiteinheit)<br/><Werte>`SEKUNDE`, `MINUTE`, `STUNDE`, `VIERTEL_STUNDE`, `TAG`, `WOCHE`, `MONAT`, `QUARTAL`, `HALBJAHR`, `JAHR`</Werte> |
| <span className="hbs-f hbs-e2">[dauer](/bo4e/202610/com/Zeitraum#dauer)</span> | dauer | integer |
| <span className="hbs-f hbs-e2">[startdatum](/bo4e/202610/com/Zeitraum#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e2">[enddatum](/bo4e/202610/com/Zeitraum#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-f hbs-e2">[einheit](/bo4e/202610/com/Zeitraum#einheit)</span> | Zeiteinheit | [Enum Zeiteinheit](/bo4e/202610/enum/Zeiteinheit)<br/><Werte>`SEKUNDE`, `MINUTE`, `STUNDE`, `VIERTEL_STUNDE`, `TAG`, `WOCHE`, `MONAT`, `QUARTAL`, `HALBJAHR`, `JAHR`</Werte> |
| <span className="hbs-f hbs-e2">[ableseZeitraum](/bo4e/202610/com/Zeitraum#ablesezeitraum)</span> | ableseZeitraum | string |
| <span className="hbs-f hbs-e2">[abrechnungsZeitraum](/bo4e/202610/com/Zeitraum#abrechnungszeitraum)</span> | abrechnungsZeitraum | string |
| <span className="hbs-f hbs-e2">[zeitraumText](/bo4e/202610/com/Zeitraum#zeitraumtext)</span> | zeitraumText | string |
| <span className="hbs-f hbs-e2">[zeitraumId](/bo4e/202610/com/Zeitraum#zeitraumid)</span> | zeitraumId | integer |
| <span className="hbs-f hbs-e1">[artikelId](/bo4e/202610/com/Preisposition#artikelid)</span> | Die genauen Bedeutungen der einzelnen Artikel-IDs sind in der EDI@Energy Codeliste der Artikelnummern<br/>und Artikel-IDs zu finden, die in der Spalte "PRICAT Codeverwendung" ein X haben | string |
| <span className="hbs-g hbs-e1">[zu_abschlaege](/bo4e/202610/com/Preisposition#zu_abschlaege) <span className="hbs-liste">[ ]</span></span> | Zuschläge oder Abschläge auf die Position. | [PositionsAufAbschlag[]](/bo4e/202610/com/PositionsAufAbschlag) |
| <span className="hbs-f hbs-e2">[bezeichnung](/bo4e/202610/com/PositionsAufAbschlag#bezeichnung)</span> | bezeichnung | string |
| <span className="hbs-f hbs-e2">[beschreibung](/bo4e/202610/com/PositionsAufAbschlag#beschreibung)</span> | beschreibung | string |
| <span className="hbs-f hbs-e2">[aufAbschlagstyp](/bo4e/202610/com/PositionsAufAbschlag#aufabschlagstyp)</span> | Festlegung, ob der Auf- oder Abschlag mit relativen oder absoluten Werten erfolgt | [Enum AufAbschlagstyp](/bo4e/202610/enum/AufAbschlagstyp)<br/><Werte>`RELATIV`, `ABSOLUT`</Werte> |
| <span className="hbs-f hbs-e2">[aufAbschlagswert](/bo4e/202610/com/PositionsAufAbschlag#aufabschlagswert)</span> | aufAbschlagswert | number (float) |
| <span className="hbs-f hbs-e2">[aufAbschlagswaehrung](/bo4e/202610/com/PositionsAufAbschlag#aufabschlagswaehrung)</span> | Waehrungseinheit | [Enum Waehrungseinheit](/bo4e/202610/enum/Waehrungseinheit)<br/><Werte>`EUR`, `CT`</Werte> |
| <span className="hbs-g hbs-e1">[preisstaffeln](/bo4e/202610/com/Preisposition#preisstaffeln) <span className="hbs-liste">[ ]</span></span> | Preisstaffeln, die zu dieser Preisposition gehören. Details Preisstaffel | [Preisstaffel[]](/bo4e/202610/com/Preisstaffel) |
| <span className="hbs-f hbs-e2">[einheitspreis](/bo4e/202610/com/Preisstaffel#einheitspreis)</span> | einheitspreis | number (float) |
| <span className="hbs-f hbs-e2">[zeitbasis](/bo4e/202610/com/Preisstaffel#zeitbasis)</span> | Die Zeit(dauer) auf die sich der Preis bezieht. Z.B. ein Jahr für einen Leistungspreis der in €/kW/Jahr<br/>ausgegeben wird. | [Enum Zeiteinheit](/bo4e/202610/enum/Zeiteinheit)<br/><Werte>`SEKUNDE`, `MINUTE`, `STUNDE`, `VIERTEL_STUNDE`, `TAG`, `WOCHE`, `MONAT`, `QUARTAL`, `HALBJAHR`, `JAHR`</Werte> |
| <span className="hbs-f hbs-e2">[staffelgrenzeVon](/bo4e/202610/com/Preisstaffel#staffelgrenzevon)</span> | staffelgrenzeVon | number (float) |
| <span className="hbs-f hbs-e2">[staffelgrenzeBis](/bo4e/202610/com/Preisstaffel#staffelgrenzebis)</span> | staffelgrenzeBis | number (float) |
| <span className="hbs-g hbs-e2">[sigmoidparameter](/bo4e/202610/com/Preisstaffel#sigmoidparameter)</span> | — | [Sigmoidparameter](/bo4e/202610/com/Sigmoidparameter) |
| <span className="hbs-f hbs-e3">[A](/bo4e/202610/com/Sigmoidparameter#a)</span> | A | number (float) |
| <span className="hbs-f hbs-e3">[B](/bo4e/202610/com/Sigmoidparameter#b)</span> | B | number (float) |
| <span className="hbs-f hbs-e3">[C](/bo4e/202610/com/Sigmoidparameter#c)</span> | C | number (float) |
| <span className="hbs-f hbs-e3">[D](/bo4e/202610/com/Sigmoidparameter#d)</span> | D | number (float) |
| <span className="hbs-f hbs-e2">[einheit](/bo4e/202610/com/Preisstaffel#einheit)</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202610/enum/Mengeneinheit)<br/><Werte>`W`, `WH`, `KW`, `KWH`, `KVARH`, `MW`, `MWH`, `STUECK`, `KUBIKMETER`, `STUNDE`, `TAG`, `MONAT`, `JAHR`, `PROZENT`, `ANZAHL`, `VAR`, `KVAR`, `VARH`, `KWHK`, `Z16`, `KWT`, `WATT_PRO_QUADRATMETER`, `METER_PRO_SEKUNDE`</Werte> |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### preisNetzbetreiberCodenummer

1 Verwendung(en) in den Nachrichtentypen PRICAT.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_27003](/schnittstellen/202610/pruefi/PRICAT/PI_27003) | Prüfi | PRICAT | stammdaten › PREISBLATT |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
