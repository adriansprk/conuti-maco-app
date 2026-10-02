# Angebotsposition
<span hidden data-pagefind-meta={"title:Angebotsposition — BO4E-Komponente (FV 202604)"} />

BO4E-Komponente · 13 Felder · 8 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="positionsbezeichnung"></a>`positionsbezeichnung` | string | Bezeichnung der Position |
| <a id="positionsmenge"></a>`positionsmenge` | [Menge](/bo4e/202604/com/Menge) | Menge der Position |
| <a id="positionspreis"></a>`positionspreis` | [Preis[]](/bo4e/202604/com/Preis) | Preisangabe zur Position |
| <a id="positionsbetrag"></a>`positionsbetrag` | [Betrag](/bo4e/202604/com/Betrag) | Betrag der Postition |
| <a id="preisschluesselstamm"></a>`preisschluesselstamm` | string | Preisschlüsselstamm |
| <a id="artikelnummer"></a>`artikelnummer` | [Enum BDEWArtikelnummer](/bo4e/202604/enum/BDEWArtikelnummer)<br/><Werte>`LEISTUNG`, `LEISTUNG_PAUSCHAL`, `GRUNDPREIS`, `REGELENERGIE_ARBEIT`, `REGELENERGIE_LEISTUNG`, `NOTSTROMLIEFERUNG_ARBEIT`, `NOTSTROMLIEFERUNG_LEISTUNG`, `RESERVENETZKAPAZITAET`, `RESERVELEISTUNG`, `ZUSAETZLICHE_ABLESUNG`, `PRUEFGEBUEHREN_AUSSERPLANMAESSIG`, `WIRKARBEIT`, `SINGULAER_GENUTZTE_BETRIEBSMITTEL`, `ABGABE_KWKG`, `ABSCHLAG`, `KONZESSIONSABGABE`, `ENTGELT_FERNAUSLESUNG`, `UNTERMESSUNG`, `BLINDMEHRARBEIT`, `ENTGELT_ABRECHNUNG`, `SPERRKOSTEN`, `ENTSPERRKOSTEN`, `MAHNKOSTEN`, `MEHR_MINDERMENGEN`, `INKASSOKOSTEN`, `BLINDMEHRLEISTUNG`, `ENTGELT_MESSUNG_ABLESUNG`, `ENTGELT_EINBAU_BETRIEB_WARTUNG_MESSTECHNIK`, `AUSGLEICHSENERGIE`, `AUSGLEICHSENERGIE_UNTERDECKUNG`, `ZAEHLEINRICHTUNG`, `WANDLER_MENGENUMWERTER`, `KOMMUNIKATIONSEINRICHTUNG`, `TECHNISCHE_STEUEREINRICHTUNG`, `PARAGRAF_19_STROM_NEV_UMLAGE`, `BEFESTIGUNGSEINRICHTUNG`, `OFFSHORE_HAFTUNGSUMLAGE`, `FIXE_ARBEITSENTGELTKOMPONENTE`, `FIXE_LEISTUNGSENTGELTKOMPONENTE`, `UMLAGE_ABSCHALTBARE_LASTEN`, `MEHRMENGE`, `MINDERMENGE`, `ENERGIESTEUER`, `SMARTMETER_GATEWAY`, `STEUERBOX`, `MSB_INKL_MESSUNG`, `ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_2_1_MSBG`, `ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_2_2_MSBG`, `ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_2_3_MSBG`, `ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_2_4_MSBG`, `ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_2_5_MSBG`, `ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_3_MSBG`, `ENTGELT_KAPAZITAETEN`</Werte> | BDEW Artikelnummer |
| <a id="artikelid"></a>`artikelId` | string[] | ArtikelId gem. BDEW |
| <a id="anbietbar"></a>`anbietbar` | boolean | — |
| <a id="freitext"></a>`freitext` | string | Zusätzliche Informationen (für allgemeine Hinweise) |
| <a id="verweiskatalognummer"></a>`verweisKatalognummer` | [Katalogverweis](/bo4e/202604/com/Katalogverweis) | APF Verweis auf Katalognummer |
| <a id="beteiligtermarktpartner"></a>`beteiligterMarktpartner` | [Marktteilnehmer](/bo4e/202604/bo/Marktteilnehmer) | Beteiligter Marktpartner |
| <a id="referenzmarktlokationsids"></a>`referenzMarktlokationsIds` | string[] | Referenz auf ID weiterer Marktlokationen |
| <a id="konfigurationsprodukt"></a>`konfigurationsprodukt` | string | Konfigurationsprodukt |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[positionsbezeichnung](/bo4e/202604/com/Angebotsposition#positionsbezeichnung)</span> | Bezeichnung der Position | string |
| <span className="hbs-g hbs-e0">[positionsmenge](/bo4e/202604/com/Angebotsposition#positionsmenge)</span> | Menge der Position | [Menge](/bo4e/202604/com/Menge) |
| <span className="hbs-f hbs-e1">[wert](/bo4e/202604/com/Menge#wert)</span> | Wert | number (float) |
| <span className="hbs-f hbs-e1">[einheit](/bo4e/202604/com/Menge#einheit)</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202604/enum/Mengeneinheit)<br/><Werte>`W`, `WH`, `KW`, `KWH`, `KVARH`, `MW`, `MWH`, `STUECK`, `KUBIKMETER`, `STUNDE`, `TAG`, `MONAT`, `JAHR`, `PROZENT`, `ANZAHL`, `VAR`, `KVAR`, `VARH`, `KWHK`, `Z16`, `KWT`, `WATT_PRO_QUADRATMETER`, `METER_PRO_SEKUNDE`</Werte> |
| <span className="hbs-f hbs-e1">[startdatum](/bo4e/202604/com/Menge#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e1">[enddatum](/bo4e/202604/com/Menge#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-g hbs-e0">[positionspreis](/bo4e/202604/com/Angebotsposition#positionspreis) <span className="hbs-liste">[ ]</span></span> | Preisangabe zur Position | [Preis[]](/bo4e/202604/com/Preis) |
| <span className="hbs-f hbs-e1">[wert](/bo4e/202604/com/Preis#wert)</span> | wert | number (float) |
| <span className="hbs-f hbs-e1">[menge](/bo4e/202604/com/Preis#menge)</span> | menge | integer |
| <span className="hbs-f hbs-e1">[minimaleMenge](/bo4e/202604/com/Preis#minimalemenge)</span> | minimale Menge | integer |
| <span className="hbs-f hbs-e1">[maximaleMenge](/bo4e/202604/com/Preis#maximalemenge)</span> | maximale Menge | integer |
| <span className="hbs-f hbs-e1">[einheit](/bo4e/202604/com/Preis#einheit)</span> | Waehrungseinheit | [Enum Waehrungseinheit](/bo4e/202604/enum/Waehrungseinheit)<br/><Werte>`EUR`, `CT`</Werte> |
| <span className="hbs-f hbs-e1">[bezugswert](/bo4e/202604/com/Preis#bezugswert)</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202604/enum/Mengeneinheit)<br/><Werte>`W`, `WH`, `KW`, `KWH`, `KVARH`, `MW`, `MWH`, `STUECK`, `KUBIKMETER`, `STUNDE`, `TAG`, `MONAT`, `JAHR`, `PROZENT`, `ANZAHL`, `VAR`, `KVAR`, `VARH`, `KWHK`, `Z16`, `KWT`, `WATT_PRO_QUADRATMETER`, `METER_PRO_SEKUNDE`</Werte> |
| <span className="hbs-f hbs-e1">[status](/bo4e/202604/com/Preis#status)</span> | Preisstatus | [Enum Preisstatus](/bo4e/202604/enum/Preisstatus)<br/><Werte>`VORLAEUFIG`, `ENDGUELTIG`</Werte> |
| <span className="hbs-f hbs-e1">[preisart](/bo4e/202604/com/Preis#preisart)</span> | Preisart Code | [Enum Preisart](/bo4e/202604/enum/Preisart)<br/><Werte>`EINRICHTUNGSPREIS`, `TRANSAKTIONSPREIS`, `BETRIEBSPREIS`</Werte> |
| <span className="hbs-g hbs-e0">[positionsbetrag](/bo4e/202604/com/Angebotsposition#positionsbetrag)</span> | Betrag der Postition | [Betrag](/bo4e/202604/com/Betrag) |
| <span className="hbs-f hbs-e1">[wert](/bo4e/202604/com/Betrag#wert)</span> | Gibt den Betrag des Preises an. | number (float) |
| <span className="hbs-f hbs-e1">[waehrung](/bo4e/202604/com/Betrag#waehrung)</span> | Währung des Preises | string |
| <span className="hbs-f hbs-e0">[preisschluesselstamm](/bo4e/202604/com/Angebotsposition#preisschluesselstamm)</span> | Preisschlüsselstamm | string |
| <span className="hbs-f hbs-e0">[artikelnummer](/bo4e/202604/com/Angebotsposition#artikelnummer)</span> | BDEW Artikelnummer | [Enum BDEWArtikelnummer](/bo4e/202604/enum/BDEWArtikelnummer)<br/><Werte>`LEISTUNG`, `LEISTUNG_PAUSCHAL`, `GRUNDPREIS`, `REGELENERGIE_ARBEIT`, `REGELENERGIE_LEISTUNG`, `NOTSTROMLIEFERUNG_ARBEIT`, `NOTSTROMLIEFERUNG_LEISTUNG`, `RESERVENETZKAPAZITAET`, `RESERVELEISTUNG`, `ZUSAETZLICHE_ABLESUNG`, `PRUEFGEBUEHREN_AUSSERPLANMAESSIG`, `WIRKARBEIT`, `SINGULAER_GENUTZTE_BETRIEBSMITTEL`, `ABGABE_KWKG`, `ABSCHLAG`, `KONZESSIONSABGABE`, `ENTGELT_FERNAUSLESUNG`, `UNTERMESSUNG`, `BLINDMEHRARBEIT`, `ENTGELT_ABRECHNUNG`, `SPERRKOSTEN`, `ENTSPERRKOSTEN`, `MAHNKOSTEN`, `MEHR_MINDERMENGEN`, `INKASSOKOSTEN`, `BLINDMEHRLEISTUNG`, `ENTGELT_MESSUNG_ABLESUNG`, `ENTGELT_EINBAU_BETRIEB_WARTUNG_MESSTECHNIK`, `AUSGLEICHSENERGIE`, `AUSGLEICHSENERGIE_UNTERDECKUNG`, `ZAEHLEINRICHTUNG`, `WANDLER_MENGENUMWERTER`, `KOMMUNIKATIONSEINRICHTUNG`, `TECHNISCHE_STEUEREINRICHTUNG`, `PARAGRAF_19_STROM_NEV_UMLAGE`, `BEFESTIGUNGSEINRICHTUNG`, `OFFSHORE_HAFTUNGSUMLAGE`, `FIXE_ARBEITSENTGELTKOMPONENTE`, `FIXE_LEISTUNGSENTGELTKOMPONENTE`, `UMLAGE_ABSCHALTBARE_LASTEN`, `MEHRMENGE`, `MINDERMENGE`, `ENERGIESTEUER`, `SMARTMETER_GATEWAY`, `STEUERBOX`, `MSB_INKL_MESSUNG`, `ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_2_1_MSBG`, `ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_2_2_MSBG`, `ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_2_3_MSBG`, `ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_2_4_MSBG`, `ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_2_5_MSBG`, `ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_3_MSBG`, `ENTGELT_KAPAZITAETEN`</Werte> |
| <span className="hbs-f hbs-e0">[artikelId](/bo4e/202604/com/Angebotsposition#artikelid) <span className="hbs-liste">[ ]</span></span> | ArtikelId gem. BDEW | string[] |
| <span className="hbs-f hbs-e0">[anbietbar](/bo4e/202604/com/Angebotsposition#anbietbar)</span> | — | boolean |
| <span className="hbs-f hbs-e0">[freitext](/bo4e/202604/com/Angebotsposition#freitext)</span> | Zusätzliche Informationen (für allgemeine Hinweise) | string |
| <span className="hbs-g hbs-e0">[verweisKatalognummer](/bo4e/202604/com/Angebotsposition#verweiskatalognummer)</span> | APF Verweis auf Katalognummer | [Katalogverweis](/bo4e/202604/com/Katalogverweis) |
| <span className="hbs-f hbs-e1">[katalognummer](/bo4e/202604/com/Katalogverweis#katalognummer)</span> | Katalognummer | string |
| <span className="hbs-f hbs-e1">[zeilennummer](/bo4e/202604/com/Katalogverweis#zeilennummer)</span> | Zeilennummer | string |
| <span className="hbs-f hbs-e1">[versionsnummer](/bo4e/202604/com/Katalogverweis#versionsnummer)</span> | Versionsnummer | string |
| <span className="hbs-g hbs-e0">[beteiligterMarktpartner](/bo4e/202604/com/Angebotsposition#beteiligtermarktpartner)</span> | Beteiligter Marktpartner | [Marktteilnehmer](/bo4e/202604/bo/Marktteilnehmer) |
| <span className="hbs-f hbs-e1">[boTyp](/bo4e/202604/bo/Marktteilnehmer#botyp) <span className="hbs-pflicht">\*</span></span> | Typ des BO | [Enum BOTyp](/bo4e/202604/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> |
| <span className="hbs-f hbs-e1">[versionStruktur](/bo4e/202604/bo/Marktteilnehmer#versionstruktur) <span className="hbs-pflicht">\*</span></span> | versionStruktur | string |
| <span className="hbs-f hbs-e1">[geschaeftspartnerrolle](/bo4e/202604/bo/Marktteilnehmer#geschaeftspartnerrolle)</span> | Rolle, die der Geschäftspartner hat (z.B. Interessent, Kunde). | [Enum Geschaeftspartnerrolle](/bo4e/202604/enum/Geschaeftspartnerrolle)<br/><Werte>`KUNDE`, `LIEFERANT`, `DIENSTLEISTER`, `INTERESSENT`, `MARKTPARTNER`, `EIGENTUEMER`, `HAUSVERWALTER`, `KORRESPONDENZEMPFAENGER`, `ABLESEKARTENEMPFAENGER`</Werte> |
| <span className="hbs-f hbs-e1">[anrede](/bo4e/202604/bo/Marktteilnehmer#anrede)</span> | Die Anrede für den GePa, Z.B. Herr. | string |
| <span className="hbs-f hbs-e1">[name1](/bo4e/202604/bo/Marktteilnehmer#name1)</span> | Erster Teil des Namens. Hier kann der Firmenname oder bei Privatpersonen<br/>beispielsweise der Nachname dargestellt werden. Beispiele: Yellow Strom GmbH<br/>oder Hagen | string |
| <span className="hbs-f hbs-e1">[name2](/bo4e/202604/bo/Marktteilnehmer#name2)</span> | Zweiter Teil des Namens. Hier kann der eine Erweiterung zum Firmennamen oder<br/>bei Privatpersonen beispielsweise der Vorname dargestellt werden. Beispiele:<br/>Bereich Süd oder Nina | string |
| <span className="hbs-f hbs-e1">[name3](/bo4e/202604/bo/Marktteilnehmer#name3)</span> | Dritter Teil des Namens. Hier können weitere Ergänzungen zum Firmennamen oder<br/>bei Privatpersonen Zusätze zum Namen dargestellt werden. Beispiele: und Afrika<br/>oder Sängerin | string |
| <span className="hbs-f hbs-e1">[name4](/bo4e/202604/bo/Marktteilnehmer#name4)</span> | name4 | string |
| <span className="hbs-g hbs-e1">[partneradresse](/bo4e/202604/bo/Marktteilnehmer#partneradresse)</span> | Adresse des Geschäftspartners, an der sich der Hauptsitz befindet. Details | [Adresse](/bo4e/202604/com/Adresse) |
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
| <span className="hbs-f hbs-e1">[gewerbekennzeichnung](/bo4e/202604/bo/Marktteilnehmer#gewerbekennzeichnung)</span> | Kennzeichnung ob es sich um einen Gewerbe/Unternehmen (gewerbeKennzeichnung = true)<br/>oder eine Privatperson handelt. (gewerbeKennzeichnung = false) | boolean |
| <span className="hbs-f hbs-e1">[externeKundenummerLieferant](/bo4e/202604/bo/Marktteilnehmer#externekundenummerlieferant)</span> | externeKundenummerLieferant | string |
| <span className="hbs-f hbs-e1">[marktrolle](/bo4e/202604/bo/Marktteilnehmer#marktrolle)</span> | Gibt im Klartext die Bezeichnung der Marktrolle an. | [Enum Marktrolle](/bo4e/202604/enum/Marktrolle)<br/><Werte>`NB`, `LF`, `MSB`, `MSBA`, `GMSB`, `MDL`, `DL`, `BKV`, `UENB`, `KUNDE-SELBST-NN`, `MGV`, `EIV`, `RB`, `KUNDE`, `INTERESSENT`, `KN`, `UBA`, `BIKO`, `ESA`</Werte> |
| <span className="hbs-f hbs-e1">[rollencodenummer](/bo4e/202604/bo/Marktteilnehmer#rollencodenummer)</span> | Gibt die Codenummer der Marktrolle an. | string |
| <span className="hbs-f hbs-e1">[rollencodetyp](/bo4e/202604/bo/Marktteilnehmer#rollencodetyp)</span> | Gibt den Typ des Codes an. | [Enum Rollencodetyp](/bo4e/202604/enum/Rollencodetyp)<br/><Werte>`BDEW`, `GS1`, `GLN`, `DVGW`</Werte> |
| <span className="hbs-f hbs-e1">[umsatzsteuerId](/bo4e/202604/bo/Marktteilnehmer#umsatzsteuerid)</span> | Die Umsatzsteuer-ID des Geschäftspartners. Beispiel: DE 813281825 | string |
| <span className="hbs-f hbs-e1">[steuernummer](/bo4e/202604/bo/Marktteilnehmer#steuernummer)</span> | Die Steuernummer-ID des Geschäftspartners. Beispiel: 30120345678 | string |
| <span className="hbs-g hbs-e1">[ansprechpartner](/bo4e/202604/bo/Marktteilnehmer#ansprechpartner)</span> | Ansprechpartner as in EDIFACT NAD+MS, that includes e.g. the email address of a natural person. | [Ansprechpartner](/bo4e/202604/bo/Ansprechpartner) |
| <span className="hbs-f hbs-e2">[boTyp](/bo4e/202604/bo/Ansprechpartner#botyp) <span className="hbs-pflicht">\*</span></span> | Typ des BO | [Enum BOTyp](/bo4e/202604/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> |
| <span className="hbs-f hbs-e2">[versionStruktur](/bo4e/202604/bo/Ansprechpartner#versionstruktur) <span className="hbs-pflicht">\*</span></span> | versionStruktur | string |
| <span className="hbs-f hbs-e2">[nachname](/bo4e/202604/bo/Ansprechpartner#nachname)</span> | Nachname (Familienname) des Ansprechpartners | string |
| <span className="hbs-f hbs-e2">[eMailAdresse](/bo4e/202604/bo/Ansprechpartner#emailadresse)</span> | E-Mail Adresse | string |
| <span className="hbs-g hbs-e2">[rufnummern](/bo4e/202604/bo/Ansprechpartner#rufnummern) <span className="hbs-liste">[ ]</span></span> | Liste der Telefonnummern, unter denen der Ansprechpartner erreichbar ist. | [Rufnummer[]](/bo4e/202604/com/Rufnummer) |
| <span className="hbs-f hbs-e3">[nummerntyp](/bo4e/202604/com/Rufnummer#nummerntyp)</span> | Rufnummernart | [Enum Rufnummernart](/bo4e/202604/enum/Rufnummernart)<br/><Werte>`RUF_ZENTRALE`, `FAX_ZENTRALE`, `SAMMELRUF`, `SAMMELFAX`, `ABTEILUNGRUF`, `ABTEILUNGFAX`, `RUF_DURCHWAHL`, `FAX_DURCHWAHL`, `MOBIL_NUMMER`</Werte> |
| <span className="hbs-f hbs-e3">[rufnummer](/bo4e/202604/com/Rufnummer#rufnummer)</span> | rufnummer | string |
| <span className="hbs-f hbs-e1">[makoadresse](/bo4e/202604/bo/Marktteilnehmer#makoadresse)</span> | Die 1:1-Kommunikationsadresse des Marktteilnehmers. Diese wird in der<br/>Marktkommunikation verwendet. | string |
| <span className="hbs-f hbs-e1">[downloadlinkZertifikat](/bo4e/202604/bo/Marktteilnehmer#downloadlinkzertifikat)</span> | downloadlinkZertifikat | string |
| <span className="hbs-f hbs-e1">[amtsgericht](/bo4e/202604/bo/Marktteilnehmer#amtsgericht)</span> | Amtsgericht bzw Handelsregistergericht, das die Handelsregisternummer herausgegeben hat | string |
| <span className="hbs-f hbs-e1">[hrnummer](/bo4e/202604/bo/Marktteilnehmer#hrnummer)</span> | Handelsregisternummer des Geschäftspartners | string |
| <span className="hbs-f hbs-e1">[website](/bo4e/202604/bo/Marktteilnehmer#website)</span> | Internetseite des Marktpartners. Beispiel: www.mp-energie.de | string |
| <span className="hbs-f hbs-e1">[faxnummer](/bo4e/202604/bo/Marktteilnehmer#faxnummer)</span> | faxnummer | string |
| <span className="hbs-f hbs-e1">[kommunikationsrolle](/bo4e/202604/bo/Marktteilnehmer#kommunikationsrolle)</span> | Kommunikationsrolle | [Enum Kommunikationsrolle](/bo4e/202604/enum/Kommunikationsrolle)<br/><Werte>`DATENAUSTAUSCH`, `RAHMENVERTRAEGE`, `KUENDIGUNGSPROZESSE`, `WECHSELPROZESSE`, `STAMMDATENPROZESSE`, `EINSPEISEPROZESSE`, `ABRECHNUNGSPROZESSE`, `MMMA_PROZESSE`, `BEWEGUNGSDATEN`, `ENT_SPERR_PROZESSE`, `BILANZIERUNGSPROZESSE`, `NETZANSCHLUSS_ANLAGEN`</Werte> |
| <span className="hbs-f hbs-e1">[weiterverpflichtet](/bo4e/202604/bo/Marktteilnehmer#weiterverpflichtet)</span> | weiterverpflichtet | boolean |
| <span className="hbs-g hbs-e1">[kommunikationsparameter](/bo4e/202604/bo/Marktteilnehmer#kommunikationsparameter)</span> | — | [Kommunikationsparameter](/bo4e/202604/com/Kommunikationsparameter) |
| <span className="hbs-g hbs-e2">[zieladresse](/bo4e/202604/com/Kommunikationsparameter#zieladresse)</span> | — | [Zieladresse](/bo4e/202604/com/Zieladresse) |
| <span className="hbs-f hbs-e3">[zieladresse1](/bo4e/202604/com/Zieladresse#zieladresse1)</span> | zieladresse1 | string |
| <span className="hbs-f hbs-e3">[zieladresse2](/bo4e/202604/com/Zieladresse#zieladresse2)</span> | zieladresse2 | string |
| <span className="hbs-f hbs-e3">[zieladresse3](/bo4e/202604/com/Zieladresse#zieladresse3)</span> | zieladresse3 | string |
| <span className="hbs-f hbs-e3">[zieladresse4](/bo4e/202604/com/Zieladresse#zieladresse4)</span> | zieladresse4 | string |
| <span className="hbs-f hbs-e3">[zieladresse5](/bo4e/202604/com/Zieladresse#zieladresse5)</span> | zieladresse5 | string |
| <span className="hbs-g hbs-e2">[zertifikatsAussteller](/bo4e/202604/com/Kommunikationsparameter#zertifikatsaussteller)</span> | — | [ZertifikatsAussteller](/bo4e/202604/com/ZertifikatsAussteller) |
| <span className="hbs-f hbs-e3">[zertifikatsAussteller1](/bo4e/202604/com/ZertifikatsAussteller#zertifikatsaussteller1)</span> | zertifikatsAussteller1 | string |
| <span className="hbs-f hbs-e3">[zertifikatsAussteller2](/bo4e/202604/com/ZertifikatsAussteller#zertifikatsaussteller2)</span> | zertifikatsAussteller2 | string |
| <span className="hbs-f hbs-e3">[zertifikatsAussteller3](/bo4e/202604/com/ZertifikatsAussteller#zertifikatsaussteller3)</span> | zertifikatsAussteller3 | string |
| <span className="hbs-f hbs-e3">[zertifikatsAussteller4](/bo4e/202604/com/ZertifikatsAussteller#zertifikatsaussteller4)</span> | zertifikatsAussteller4 | string |
| <span className="hbs-f hbs-e3">[zertifikatsAussteller5](/bo4e/202604/com/ZertifikatsAussteller#zertifikatsaussteller5)</span> | zertifikatsAussteller5 | string |
| <span className="hbs-g hbs-e2">[zertifikatsNutzer](/bo4e/202604/com/Kommunikationsparameter#zertifikatsnutzer)</span> | — | [ZertifikatsNutzer](/bo4e/202604/com/ZertifikatsNutzer) |
| <span className="hbs-f hbs-e3">[zertifikatsNutzer1](/bo4e/202604/com/ZertifikatsNutzer#zertifikatsnutzer1)</span> | zertifikatsNutzer1 | string |
| <span className="hbs-f hbs-e3">[zertifikatsNutzer2](/bo4e/202604/com/ZertifikatsNutzer#zertifikatsnutzer2)</span> | zertifikatsNutzer2 | string |
| <span className="hbs-f hbs-e3">[zertifikatsNutzer3](/bo4e/202604/com/ZertifikatsNutzer#zertifikatsnutzer3)</span> | zertifikatsNutzer3 | string |
| <span className="hbs-f hbs-e3">[zertifikatsNutzer4](/bo4e/202604/com/ZertifikatsNutzer#zertifikatsnutzer4)</span> | zertifikatsNutzer4 | string |
| <span className="hbs-f hbs-e3">[zertifikatsNutzer5](/bo4e/202604/com/ZertifikatsNutzer#zertifikatsnutzer5)</span> | zertifikatsNutzer5 | string |
| <span className="hbs-f hbs-e1">[messstellenbetreiberEigenschaft](/bo4e/202604/bo/Marktteilnehmer#messstellenbetreibereigenschaft)</span> | MSBEigenschaft | [Enum MSBEigenschaft](/bo4e/202604/enum/MSBEigenschaft)<br/><Werte>`GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER`, `WETTBEWERBLICHER_MESSSTELLENBETREIBER`, `AUFFANGMESSSTELLENBETREIBER`</Werte> |
| <span className="hbs-g hbs-e1">[bankverbindung](/bo4e/202604/bo/Marktteilnehmer#bankverbindung) <span className="hbs-liste">[ ]</span></span> | Bankverbindung | [Bankverbindung[]](/bo4e/202604/com/Bankverbindung) |
| <span className="hbs-f hbs-e2">[verwendungszweck](/bo4e/202604/com/Bankverbindung#verwendungszweck)</span> | BankverbindungVerwendungszweck | [Enum BankverbindungVerwendungszweck](/bo4e/202604/enum/BankverbindungVerwendungszweck)<br/><Werte>`BV_ZAHLUNG_NNA`, `BV_ZAHLUNG_MMMA`, `BV_ZAHLUNG_MSB_ABRECHNNUNG`, `BV_ZAHLUNG_ENT_SPERREN_ABRECHNUNG`, `BV_SONSTIGE`</Werte> |
| <span className="hbs-f hbs-e2">[iban](/bo4e/202604/com/Bankverbindung#iban)</span> | IBAN | string |
| <span className="hbs-f hbs-e2">[kontoinhaber](/bo4e/202604/com/Bankverbindung#kontoinhaber)</span> | Der Kontoinhaber | string |
| <span className="hbs-f hbs-e2">[bic](/bo4e/202604/com/Bankverbindung#bic)</span> | BIC Code | string |
| <span className="hbs-f hbs-e2">[kreditinstitut](/bo4e/202604/com/Bankverbindung#kreditinstitut)</span> | Name des Kreditinstitut | string |
| <span className="hbs-g hbs-e1">[erreichbarkeit](/bo4e/202604/bo/Marktteilnehmer#erreichbarkeit) <span className="hbs-liste">[ ]</span></span> | Die Erreichbarkeit eines Unternehmens an Werktagen. | [Erreichbarkeit[]](/bo4e/202604/com/Erreichbarkeit) |
| <span className="hbs-f hbs-e2">[verfuegbarkeit](/bo4e/202604/com/Erreichbarkeit#verfuegbarkeit)</span> | Verfuegbarkeit | [Enum Verfuegbarkeit](/bo4e/202604/enum/Verfuegbarkeit)<br/><Werte>`MONTAG`, `DIENSTAG`, `MITTWOCH`, `DONNERSTAG`, `FREITAG`, `PAUSE`</Werte> |
| <span className="hbs-f hbs-e2">[zeit](/bo4e/202604/com/Erreichbarkeit#zeit)</span> | Zeit der Erreichbarkeit | string |
| <span className="hbs-f hbs-e1">[ipAdresse](/bo4e/202604/bo/Marktteilnehmer#ipadresse)</span> | ipAdresse | string |
| <span className="hbs-g hbs-e1">[ipRange](/bo4e/202604/bo/Marktteilnehmer#iprange)</span> | — | [IpRange](/bo4e/202604/com/IpRange) |
| <span className="hbs-f hbs-e2">[untereGrenze](/bo4e/202604/com/IpRange#unteregrenze)</span> | untereGrenze | string |
| <span className="hbs-f hbs-e2">[obereGrenze](/bo4e/202604/com/IpRange#oberegrenze)</span> | obereGrenze | string |
| <span className="hbs-f hbs-e1">[zuordnungVon](/bo4e/202604/bo/Marktteilnehmer#zuordnungvon)</span> | Startdatum der Zuordnung des Marktteilnehmers | string (date-time) |
| <span className="hbs-f hbs-e1">[zuordnungBis](/bo4e/202604/bo/Marktteilnehmer#zuordnungbis)</span> | Enddatum der Zuordnung des Marktteilnehmers | string (date-time) |
| <span className="hbs-f hbs-e1">[bilanzkreis](/bo4e/202604/bo/Marktteilnehmer#bilanzkreis)</span> | Bilanzkreis | string |
| <span className="hbs-f hbs-e1">[verwendungszweckBilanzkreis](/bo4e/202604/bo/Marktteilnehmer#verwendungszweckbilanzkreis)</span> | Verwendungszweck des Bilanzkreises | [Enum VerwendungszweckBilanzkreis](/bo4e/202604/enum/VerwendungszweckBilanzkreis)<br/><Werte>`VERBRAUCHENDE_MARKTLOKATION`, `ERZEUGENDE_MARKTLOKATION_EEG`, `ERZEUGENDE_MARKTLOKATION_KWKG`, `SONSTIGE_ERZEUGENDE_MARKTLOKATION`</Werte> |
| <span className="hbs-f hbs-e0">[referenzMarktlokationsIds](/bo4e/202604/com/Angebotsposition#referenzmarktlokationsids) <span className="hbs-liste">[ ]</span></span> | Referenz auf ID weiterer Marktlokationen | string[] |
| <span className="hbs-f hbs-e0">[konfigurationsprodukt](/bo4e/202604/com/Angebotsposition#konfigurationsprodukt)</span> | Konfigurationsprodukt | string |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### positionsbezeichnung

3 Verwendung(en) in den Nachrichtentypen QUOTES.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_15001](/schnittstellen/202604/pruefi/QUOTES/PI_15001) | Prüfi | QUOTES | stammdaten › ANGEBOT › positionsdaten |
| [PI_15003](/schnittstellen/202604/pruefi/QUOTES/PI_15003) | Prüfi | QUOTES | stammdaten › ANGEBOT › positionsdaten |
| [PI_15004](/schnittstellen/202604/pruefi/QUOTES/PI_15004) | Prüfi | QUOTES | stammdaten › ANGEBOT › positionsdaten |

### artikelnummer

1 Verwendung(en) in den Nachrichtentypen QUOTES.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_15001](/schnittstellen/202604/pruefi/QUOTES/PI_15001) | Prüfi | QUOTES | stammdaten › ANGEBOT › positionsdaten |

### artikelId

2 Verwendung(en) in den Nachrichtentypen QUOTES.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_15003](/schnittstellen/202604/pruefi/QUOTES/PI_15003) | Prüfi | QUOTES | stammdaten › ANGEBOT › positionsdaten |
| [PI_15004](/schnittstellen/202604/pruefi/QUOTES/PI_15004) | Prüfi | QUOTES | stammdaten › ANGEBOT › positionsdaten |

### anbietbar

1 Verwendung(en) in den Nachrichtentypen QUOTES.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_15001](/schnittstellen/202604/pruefi/QUOTES/PI_15001) | Prüfi | QUOTES | stammdaten › ANGEBOT › positionsdaten |

### freitext

1 Verwendung(en) in den Nachrichtentypen QUOTES.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_15001](/schnittstellen/202604/pruefi/QUOTES/PI_15001) | Prüfi | QUOTES | stammdaten › ANGEBOT › positionsdaten |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
