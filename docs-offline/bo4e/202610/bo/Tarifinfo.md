# Tarifinfo
<span hidden data-pagefind-meta={"title:Tarifinfo — BO4E-Geschäftsobjekt (FV 202610)"} />

BO4E-Geschäftsobjekt · 16 Felder · 0 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="botyp"></a>`boTyp` <span className="hbs-pflicht">\*</span> | [Enum BOTyp](/bo4e/202610/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> | Typ des BO |
| <a id="versionstruktur"></a>`versionStruktur` <span className="hbs-pflicht">\*</span> | string | versionStruktur |
| <a id="anbieter"></a>`anbieter` | [Marktteilnehmer](/bo4e/202610/bo/Marktteilnehmer) | Der Marktteilnehmer (Lieferant), der diesen Tarif anbietet |
| <a id="anbietername"></a>`anbietername` | string | Der Name des Marktpartners, der den Tarif anbietet |
| <a id="anwendung_von"></a>`anwendung_von` | string (date-time) | Angabe des inklusiven Zeitpunkts, ab dem der Tarif bzw. der Preis angewendet und abgerechnet wird |
| <a id="bemerkung"></a>`bemerkung` | string | Freitext |
| <a id="bezeichnung"></a>`bezeichnung` | string | Name des Tarifs |
| <a id="energiemix"></a>`energiemix` | [Energiemix](/bo4e/202610/com/Energiemix) | Der Energiemix, der für diesen Tarif gilt |
| <a id="kundentypen"></a>`kundentypen` | [Enum Kundentyp[]](/bo4e/202610/enum/Kundentyp)<br/><Werte>`BELEUCHTUNG_OEFFENTLICH`, `BELEUCHTUNG_STRASSE`, `DIREKTHEIZUNG`, `GEMEINSCHAFT_MFH`, `GEWERBE`, `HAUSHALT`, `KIRCHE`, `KWK`, `LADESAEULE`, `LANDWIRT`, `PRIVAT`, `SONSTIGE`, `SPEICHERHEIZUNG`, `UNTERBR_EINRICHTUNG`, `WAERMEPUMPE`</Werte> | Kundentypen für den der Tarif gilt, z.B. Privatkunden |
| <a id="registeranzahl"></a>`registeranzahl` | [Enum Registeranzahl](/bo4e/202610/enum/Registeranzahl)<br/><Werte>`EINTARIF`, `MEHRTARIF`, `ZWEITARIF`</Werte> | Die Art des Tarifes, z.B. Eintarif oder Mehrtarif |
| <a id="sparte"></a>`sparte` | [Enum Sparte](/bo4e/202610/enum/Sparte)<br/><Werte>`STROM`, `GAS`, `FERNWAERME`, `NAHWAERME`, `WASSER`, `ABWASSER`</Werte> | Strom oder Gas, etc. |
| <a id="tarifmerkmale"></a>`tarifmerkmale` | [Enum Tarifmerkmal[]](/bo4e/202610/enum/Tarifmerkmal)<br/><Werte>`BAUSTROM`, `FESTPREIS`, `HAUSLICHT`, `HEIZSTROM`, `KOMBI`, `ONLINE`, `PAKET`, `STANDARD`, `VORKASSE`</Werte> | Weitere Merkmale des Tarifs, z.B. Festpreis oder Vorkasse |
| <a id="tariftyp"></a>`tariftyp` | [Enum Tariftyp](/bo4e/202610/enum/Tariftyp)<br/><Werte>`ERSATZVERSORGUNG`, `GRUNDVERSORGUNG`, `GRUND_ERSATZVERSORGUNG`, `SONDERTARIF`</Werte> | Hinweis auf den Tariftyp, z.B. Grundversorgung oder Sondertarif |
| <a id="vertragskonditionen"></a>`vertragskonditionen` | [Vertragskonditionen](/bo4e/202610/com/Vertragskonditionen) | Mindestlaufzeiten und Kündigungsfristen zusammengefasst |
| <a id="website"></a>`website` | string | Internetseite auf dem der Tarif zu finden ist |
| <a id="zeitliche_gueltigkeit"></a>`zeitliche_gueltigkeit` | [Zeitraum](/bo4e/202610/com/Zeitraum) | Angabe, in welchem Zeitraum der Tarif gültig ist |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[boTyp](/bo4e/202610/bo/Tarifinfo#botyp) <span className="hbs-pflicht">\*</span></span> | Typ des BO | [Enum BOTyp](/bo4e/202610/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> |
| <span className="hbs-f hbs-e0">[versionStruktur](/bo4e/202610/bo/Tarifinfo#versionstruktur) <span className="hbs-pflicht">\*</span></span> | versionStruktur | string |
| <span className="hbs-g hbs-e0">[anbieter](/bo4e/202610/bo/Tarifinfo#anbieter)</span> | Der Marktteilnehmer (Lieferant), der diesen Tarif anbietet | [Marktteilnehmer](/bo4e/202610/bo/Marktteilnehmer) |
| <span className="hbs-f hbs-e1">[boTyp](/bo4e/202610/bo/Marktteilnehmer#botyp) <span className="hbs-pflicht">\*</span></span> | Typ des BO | [Enum BOTyp](/bo4e/202610/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> |
| <span className="hbs-f hbs-e1">[versionStruktur](/bo4e/202610/bo/Marktteilnehmer#versionstruktur) <span className="hbs-pflicht">\*</span></span> | versionStruktur | string |
| <span className="hbs-f hbs-e1">[geschaeftspartnerrolle](/bo4e/202610/bo/Marktteilnehmer#geschaeftspartnerrolle)</span> | Rolle, die der Geschäftspartner hat (z.B. Interessent, Kunde). | [Enum Geschaeftspartnerrolle](/bo4e/202610/enum/Geschaeftspartnerrolle)<br/><Werte>`KUNDE`, `LIEFERANT`, `DIENSTLEISTER`, `INTERESSENT`, `MARKTPARTNER`, `EIGENTUEMER`, `HAUSVERWALTER`, `KORRESPONDENZEMPFAENGER`, `ABLESEKARTENEMPFAENGER`</Werte> |
| <span className="hbs-f hbs-e1">[anrede](/bo4e/202610/bo/Marktteilnehmer#anrede)</span> | Die Anrede für den GePa, Z.B. Herr. | string |
| <span className="hbs-f hbs-e1">[name1](/bo4e/202610/bo/Marktteilnehmer#name1)</span> | Erster Teil des Namens. Hier kann der Firmenname oder bei Privatpersonen<br/>beispielsweise der Nachname dargestellt werden. Beispiele: Yellow Strom GmbH<br/>oder Hagen | string |
| <span className="hbs-f hbs-e1">[name2](/bo4e/202610/bo/Marktteilnehmer#name2)</span> | Zweiter Teil des Namens. Hier kann der eine Erweiterung zum Firmennamen oder<br/>bei Privatpersonen beispielsweise der Vorname dargestellt werden. Beispiele:<br/>Bereich Süd oder Nina | string |
| <span className="hbs-f hbs-e1">[name3](/bo4e/202610/bo/Marktteilnehmer#name3)</span> | Dritter Teil des Namens. Hier können weitere Ergänzungen zum Firmennamen oder<br/>bei Privatpersonen Zusätze zum Namen dargestellt werden. Beispiele: und Afrika<br/>oder Sängerin | string |
| <span className="hbs-f hbs-e1">[name4](/bo4e/202610/bo/Marktteilnehmer#name4)</span> | name4 | string |
| <span className="hbs-g hbs-e1">[partneradresse](/bo4e/202610/bo/Marktteilnehmer#partneradresse)</span> | Adresse des Geschäftspartners, an der sich der Hauptsitz befindet. Details | [Adresse](/bo4e/202610/com/Adresse) |
| <span className="hbs-f hbs-e2">[postleitzahl](/bo4e/202610/com/Adresse#postleitzahl)</span> | Postleitzahl | string |
| <span className="hbs-f hbs-e2">[ort](/bo4e/202610/com/Adresse#ort)</span> | Ort | string |
| <span className="hbs-f hbs-e2">[strasse](/bo4e/202610/com/Adresse#strasse)</span> | Strasse | string |
| <span className="hbs-f hbs-e2">[hausnummer](/bo4e/202610/com/Adresse#hausnummer)</span> | Hausnummer und Ergänzung | string |
| <span className="hbs-f hbs-e2">[postfach](/bo4e/202610/com/Adresse#postfach)</span> | Postfach | string |
| <span className="hbs-f hbs-e2">[adresszusatz](/bo4e/202610/com/Adresse#adresszusatz)</span> | Adresszusatz | string |
| <span className="hbs-f hbs-e2">[coErgaenzung](/bo4e/202610/com/Adresse#coergaenzung)</span> | coErgaenzung | string |
| <span className="hbs-f hbs-e2">[landescode](/bo4e/202610/com/Adresse#landescode)</span> | Landescode | [Enum Landescode](/bo4e/202610/enum/Landescode)<br/><Werte>`AC`, `AD`, `AE`, `AF`, `AG`, `AI`, `AL`, `AM`, `AN`, `AO`, `AQ`, `AR`, `AS`, `AT`, `AU`, `AW`, `AX`, `AZ`, `BA`, `BB`, `BD`, `BE`, `BF`, `BG`, `BH`, `BI`, `BJ`, `BL`, `BM`, `BN`, `BO`, `BQ`, `BR`, `BS`, `BT`, `BU`, `BV`, `BW`, `BY`, `BZ`, `CA`, `CC`, `CD`, `CF`, `CG`, `CH`, `CI`, `CK`, `CL`, `CM`, `CN`, `CO`, `CP`, `CR`, `CS`, `CU`, `CV`, `CW`, `CX`, `CY`, `CZ`, `DE`, `DG`, `DJ`, `DK`, `DM`, `DO`, `DZ`, `EA`, `EC`, `EE`, `EG`, `EH`, `ER`, `ES`, `ET`, `EU`, `FI`, `FJ`, `FK`, `FM`, `FO`, `FR`, `FX`, `GA`, `GB`, `GD`, `GE`, `GF`, `GG`, `GH`, `GI`, `GL`, `GM`, `GN`, `GP`, `GQ`, `GR`, `GS`, `GT`, `GU`, `GW`, `GY`, `HK`, `HM`, `HN`, `HR`, `HT`, `HU`, `IC`, `ID`, `IE`, `IL`, `IM`, `IN`, `IO`, `IQ`, `IR`, `IS`, `IT`, `JE`, `JM`, `JO`, `JP`, `KE`, `KG`, `KH`, `KI`, `KM`, `KN`, `KP`, `KR`, `KW`, `KY`, `KZ`, `LA`, `LB`, `LC`, `LI`, `LK`, `LR`, `LS`, `LT`, `LU`, `LV`, `LY`, `MA`, `MC`, `MD`, `ME`, `MF`, `MG`, `MH`, `MK`, `ML`, `MM`, `MN`, `MO`, `MP`, `MQ`, `MR`, `MS`, `MT`, `MU`, `MV`, `MW`, `MX`, `MY`, `MZ`, `NA`, `NC`, `NE`, `NF`, `NG`, `NI`, `NL`, `NO`, `NP`, `NR`, `NT`, `NU`, `NZ`, `OM`, `PA`, `PE`, `PF`, `PG`, `PH`, `PK`, `PL`, `PM`, `PN`, `PR`, `PS`, `PT`, `PW`, `PY`, `QA`, `RE`, `RO`, `RS`, `RU`, `RW`, `SA`, `SB`, `SC`, `SD`, `SE`, `SF`, `SG`, `SH`, `SI`, `SJ`, `SK`, `SL`, `SM`, `SN`, `SO`, `SR`, `SS`, `ST`, `SU`, `SV`, `SX`, `SY`, `SZ`, `TA`, `TC`, `TD`, `TF`, `TG`, `TJ`, `TK`, `TL`, `TM`, `TN`, `TO`, `TP`, `TR`, `TT`, `TV`, `TW`, `TZ`, `UA`, `UG`, `UK`, `UM`, `US`, `UY`, `UZ`, `VA`, `VC`, `VE`, `VG`, `VI`, `VN`, `VU`, `WF`, `WS`, `XK`, `YE`, `YT`, `YU`, `ZA`, `ZM`, `ZR`, `ZW`</Werte> |
| <span className="hbs-f hbs-e2">[ortsteil](/bo4e/202610/com/Adresse#ortsteil)</span> | Ortsteil | string |
| <span className="hbs-g hbs-e2">[zusatzInformation](/bo4e/202610/com/Adresse#zusatzinformation)</span> | — | [AdresszusatzInformation](/bo4e/202610/com/AdresszusatzInformation) |
| <span className="hbs-f hbs-e3">[zusatz1](/bo4e/202610/com/AdresszusatzInformation#zusatz1)</span> | Adresszusatz 1 | string |
| <span className="hbs-f hbs-e3">[zusatz2](/bo4e/202610/com/AdresszusatzInformation#zusatz2)</span> | Adresszusatz 2 | string |
| <span className="hbs-f hbs-e3">[zusatz3](/bo4e/202610/com/AdresszusatzInformation#zusatz3)</span> | Adresszusatz 3 | string |
| <span className="hbs-f hbs-e3">[zusatz4](/bo4e/202610/com/AdresszusatzInformation#zusatz4)</span> | Adresszusatz 4 | string |
| <span className="hbs-f hbs-e3">[zusatz5](/bo4e/202610/com/AdresszusatzInformation#zusatz5)</span> | Adresszusatz 5 | string |
| <span className="hbs-f hbs-e1">[gewerbekennzeichnung](/bo4e/202610/bo/Marktteilnehmer#gewerbekennzeichnung)</span> | Kennzeichnung ob es sich um einen Gewerbe/Unternehmen (gewerbeKennzeichnung = true)<br/>oder eine Privatperson handelt. (gewerbeKennzeichnung = false) | boolean |
| <span className="hbs-f hbs-e1">[externeKundenummerLieferant](/bo4e/202610/bo/Marktteilnehmer#externekundenummerlieferant)</span> | externeKundenummerLieferant | string |
| <span className="hbs-f hbs-e1">[marktrolle](/bo4e/202610/bo/Marktteilnehmer#marktrolle)</span> | Gibt im Klartext die Bezeichnung der Marktrolle an. | [Enum Marktrolle](/bo4e/202610/enum/Marktrolle)<br/><Werte>`NB`, `LF`, `MSB`, `MSBA`, `GMSB`, `MDL`, `DL`, `BKV`, `UENB`, `KUNDE-SELBST-NN`, `MGV`, `EIV`, `RB`, `KUNDE`, `INTERESSENT`, `KN`, `UBA`, `BIKO`, `ESA`</Werte> |
| <span className="hbs-f hbs-e1">[rollencodenummer](/bo4e/202610/bo/Marktteilnehmer#rollencodenummer)</span> | Gibt die Codenummer der Marktrolle an. | string |
| <span className="hbs-f hbs-e1">[rollencodetyp](/bo4e/202610/bo/Marktteilnehmer#rollencodetyp)</span> | Gibt den Typ des Codes an. | [Enum Rollencodetyp](/bo4e/202610/enum/Rollencodetyp)<br/><Werte>`BDEW`, `GS1`, `GLN`, `DVGW`</Werte> |
| <span className="hbs-f hbs-e1">[umsatzsteuerId](/bo4e/202610/bo/Marktteilnehmer#umsatzsteuerid)</span> | Die Umsatzsteuer-ID des Geschäftspartners. Beispiel: DE 813281825 | string |
| <span className="hbs-f hbs-e1">[steuernummer](/bo4e/202610/bo/Marktteilnehmer#steuernummer)</span> | Die Steuernummer-ID des Geschäftspartners. Beispiel: 30120345678 | string |
| <span className="hbs-g hbs-e1">[ansprechpartner](/bo4e/202610/bo/Marktteilnehmer#ansprechpartner)</span> | Ansprechpartner as in EDIFACT NAD+MS, that includes e.g. the email address of a natural person. | [Ansprechpartner](/bo4e/202610/bo/Ansprechpartner) |
| <span className="hbs-f hbs-e2">[boTyp](/bo4e/202610/bo/Ansprechpartner#botyp) <span className="hbs-pflicht">\*</span></span> | Typ des BO | [Enum BOTyp](/bo4e/202610/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> |
| <span className="hbs-f hbs-e2">[versionStruktur](/bo4e/202610/bo/Ansprechpartner#versionstruktur) <span className="hbs-pflicht">\*</span></span> | versionStruktur | string |
| <span className="hbs-f hbs-e2">[nachname](/bo4e/202610/bo/Ansprechpartner#nachname)</span> | Nachname (Familienname) des Ansprechpartners | string |
| <span className="hbs-f hbs-e2">[eMailAdresse](/bo4e/202610/bo/Ansprechpartner#emailadresse)</span> | E-Mail Adresse | string |
| <span className="hbs-g hbs-e2">[rufnummern](/bo4e/202610/bo/Ansprechpartner#rufnummern) <span className="hbs-liste">[ ]</span></span> | Liste der Telefonnummern, unter denen der Ansprechpartner erreichbar ist. | [Rufnummer[]](/bo4e/202610/com/Rufnummer) |
| <span className="hbs-f hbs-e3">[nummerntyp](/bo4e/202610/com/Rufnummer#nummerntyp)</span> | Rufnummernart | [Enum Rufnummernart](/bo4e/202610/enum/Rufnummernart)<br/><Werte>`RUF_ZENTRALE`, `FAX_ZENTRALE`, `SAMMELRUF`, `SAMMELFAX`, `ABTEILUNGRUF`, `ABTEILUNGFAX`, `RUF_DURCHWAHL`, `FAX_DURCHWAHL`, `MOBIL_NUMMER`</Werte> |
| <span className="hbs-f hbs-e3">[rufnummer](/bo4e/202610/com/Rufnummer#rufnummer)</span> | rufnummer | string |
| <span className="hbs-f hbs-e1">[makoadresse](/bo4e/202610/bo/Marktteilnehmer#makoadresse)</span> | Die 1:1-Kommunikationsadresse des Marktteilnehmers. Diese wird in der<br/>Marktkommunikation verwendet. | string |
| <span className="hbs-f hbs-e1">[downloadlinkZertifikat](/bo4e/202610/bo/Marktteilnehmer#downloadlinkzertifikat)</span> | downloadlinkZertifikat | string |
| <span className="hbs-f hbs-e1">[amtsgericht](/bo4e/202610/bo/Marktteilnehmer#amtsgericht)</span> | Amtsgericht bzw Handelsregistergericht, das die Handelsregisternummer herausgegeben hat | string |
| <span className="hbs-f hbs-e1">[hrnummer](/bo4e/202610/bo/Marktteilnehmer#hrnummer)</span> | Handelsregisternummer des Geschäftspartners | string |
| <span className="hbs-f hbs-e1">[website](/bo4e/202610/bo/Marktteilnehmer#website)</span> | Internetseite des Marktpartners. Beispiel: www.mp-energie.de | string |
| <span className="hbs-f hbs-e1">[faxnummer](/bo4e/202610/bo/Marktteilnehmer#faxnummer)</span> | faxnummer | string |
| <span className="hbs-f hbs-e1">[kommunikationsrolle](/bo4e/202610/bo/Marktteilnehmer#kommunikationsrolle)</span> | Kommunikationsrolle | [Enum Kommunikationsrolle](/bo4e/202610/enum/Kommunikationsrolle)<br/><Werte>`DATENAUSTAUSCH`, `RAHMENVERTRAEGE`, `KUENDIGUNGSPROZESSE`, `WECHSELPROZESSE`, `STAMMDATENPROZESSE`, `EINSPEISEPROZESSE`, `ABRECHNUNGSPROZESSE`, `MMMA_PROZESSE`, `BEWEGUNGSDATEN`, `ENT_SPERR_PROZESSE`, `BILANZIERUNGSPROZESSE`, `NETZANSCHLUSS_ANLAGEN`</Werte> |
| <span className="hbs-f hbs-e1">[weiterverpflichtet](/bo4e/202610/bo/Marktteilnehmer#weiterverpflichtet)</span> | weiterverpflichtet | boolean |
| <span className="hbs-g hbs-e1">[kommunikationsparameter](/bo4e/202610/bo/Marktteilnehmer#kommunikationsparameter)</span> | — | [Kommunikationsparameter](/bo4e/202610/com/Kommunikationsparameter) |
| <span className="hbs-g hbs-e2">[zieladresse](/bo4e/202610/com/Kommunikationsparameter#zieladresse)</span> | — | [Zieladresse](/bo4e/202610/com/Zieladresse) |
| <span className="hbs-f hbs-e3">[zieladresse1](/bo4e/202610/com/Zieladresse#zieladresse1)</span> | zieladresse1 | string |
| <span className="hbs-f hbs-e3">[zieladresse2](/bo4e/202610/com/Zieladresse#zieladresse2)</span> | zieladresse2 | string |
| <span className="hbs-f hbs-e3">[zieladresse3](/bo4e/202610/com/Zieladresse#zieladresse3)</span> | zieladresse3 | string |
| <span className="hbs-f hbs-e3">[zieladresse4](/bo4e/202610/com/Zieladresse#zieladresse4)</span> | zieladresse4 | string |
| <span className="hbs-f hbs-e3">[zieladresse5](/bo4e/202610/com/Zieladresse#zieladresse5)</span> | zieladresse5 | string |
| <span className="hbs-g hbs-e2">[zertifikatsAussteller](/bo4e/202610/com/Kommunikationsparameter#zertifikatsaussteller)</span> | — | [ZertifikatsAussteller](/bo4e/202610/com/ZertifikatsAussteller) |
| <span className="hbs-f hbs-e3">[zertifikatsAussteller1](/bo4e/202610/com/ZertifikatsAussteller#zertifikatsaussteller1)</span> | zertifikatsAussteller1 | string |
| <span className="hbs-f hbs-e3">[zertifikatsAussteller2](/bo4e/202610/com/ZertifikatsAussteller#zertifikatsaussteller2)</span> | zertifikatsAussteller2 | string |
| <span className="hbs-f hbs-e3">[zertifikatsAussteller3](/bo4e/202610/com/ZertifikatsAussteller#zertifikatsaussteller3)</span> | zertifikatsAussteller3 | string |
| <span className="hbs-f hbs-e3">[zertifikatsAussteller4](/bo4e/202610/com/ZertifikatsAussteller#zertifikatsaussteller4)</span> | zertifikatsAussteller4 | string |
| <span className="hbs-f hbs-e3">[zertifikatsAussteller5](/bo4e/202610/com/ZertifikatsAussteller#zertifikatsaussteller5)</span> | zertifikatsAussteller5 | string |
| <span className="hbs-g hbs-e2">[zertifikatsNutzer](/bo4e/202610/com/Kommunikationsparameter#zertifikatsnutzer)</span> | — | [ZertifikatsNutzer](/bo4e/202610/com/ZertifikatsNutzer) |
| <span className="hbs-f hbs-e3">[zertifikatsNutzer1](/bo4e/202610/com/ZertifikatsNutzer#zertifikatsnutzer1)</span> | zertifikatsNutzer1 | string |
| <span className="hbs-f hbs-e3">[zertifikatsNutzer2](/bo4e/202610/com/ZertifikatsNutzer#zertifikatsnutzer2)</span> | zertifikatsNutzer2 | string |
| <span className="hbs-f hbs-e3">[zertifikatsNutzer3](/bo4e/202610/com/ZertifikatsNutzer#zertifikatsnutzer3)</span> | zertifikatsNutzer3 | string |
| <span className="hbs-f hbs-e3">[zertifikatsNutzer4](/bo4e/202610/com/ZertifikatsNutzer#zertifikatsnutzer4)</span> | zertifikatsNutzer4 | string |
| <span className="hbs-f hbs-e3">[zertifikatsNutzer5](/bo4e/202610/com/ZertifikatsNutzer#zertifikatsnutzer5)</span> | zertifikatsNutzer5 | string |
| <span className="hbs-f hbs-e1">[messstellenbetreiberEigenschaft](/bo4e/202610/bo/Marktteilnehmer#messstellenbetreibereigenschaft)</span> | MSBEigenschaft | [Enum MSBEigenschaft](/bo4e/202610/enum/MSBEigenschaft)<br/><Werte>`GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER`, `WETTBEWERBLICHER_MESSSTELLENBETREIBER`, `AUFFANGMESSSTELLENBETREIBER`</Werte> |
| <span className="hbs-g hbs-e1">[bankverbindung](/bo4e/202610/bo/Marktteilnehmer#bankverbindung) <span className="hbs-liste">[ ]</span></span> | Bankverbindung | [Bankverbindung[]](/bo4e/202610/com/Bankverbindung) |
| <span className="hbs-f hbs-e2">[verwendungszweck](/bo4e/202610/com/Bankverbindung#verwendungszweck)</span> | BankverbindungVerwendungszweck | [Enum BankverbindungVerwendungszweck](/bo4e/202610/enum/BankverbindungVerwendungszweck)<br/><Werte>`BV_ZAHLUNG_NNA`, `BV_ZAHLUNG_MMMA`, `BV_ZAHLUNG_MSB_ABRECHNNUNG`, `BV_ZAHLUNG_ENT_SPERREN_ABRECHNUNG`, `BV_SONSTIGE`</Werte> |
| <span className="hbs-f hbs-e2">[iban](/bo4e/202610/com/Bankverbindung#iban)</span> | IBAN | string |
| <span className="hbs-f hbs-e2">[kontoinhaber](/bo4e/202610/com/Bankverbindung#kontoinhaber)</span> | Der Kontoinhaber | string |
| <span className="hbs-f hbs-e2">[bic](/bo4e/202610/com/Bankverbindung#bic)</span> | BIC Code | string |
| <span className="hbs-f hbs-e2">[kreditinstitut](/bo4e/202610/com/Bankverbindung#kreditinstitut)</span> | Name des Kreditinstitut | string |
| <span className="hbs-g hbs-e1">[erreichbarkeit](/bo4e/202610/bo/Marktteilnehmer#erreichbarkeit) <span className="hbs-liste">[ ]</span></span> | Die Erreichbarkeit eines Unternehmens an Werktagen. | [Erreichbarkeit[]](/bo4e/202610/com/Erreichbarkeit) |
| <span className="hbs-f hbs-e2">[verfuegbarkeit](/bo4e/202610/com/Erreichbarkeit#verfuegbarkeit)</span> | Verfuegbarkeit | [Enum Verfuegbarkeit](/bo4e/202610/enum/Verfuegbarkeit)<br/><Werte>`MONTAG`, `DIENSTAG`, `MITTWOCH`, `DONNERSTAG`, `FREITAG`, `PAUSE`</Werte> |
| <span className="hbs-f hbs-e2">[zeit](/bo4e/202610/com/Erreichbarkeit#zeit)</span> | Zeit der Erreichbarkeit | string |
| <span className="hbs-f hbs-e1">[ipAdresse](/bo4e/202610/bo/Marktteilnehmer#ipadresse)</span> | ipAdresse | string |
| <span className="hbs-g hbs-e1">[ipRange](/bo4e/202610/bo/Marktteilnehmer#iprange)</span> | — | [IpRange](/bo4e/202610/com/IpRange) |
| <span className="hbs-f hbs-e2">[untereGrenze](/bo4e/202610/com/IpRange#unteregrenze)</span> | untereGrenze | string |
| <span className="hbs-f hbs-e2">[obereGrenze](/bo4e/202610/com/IpRange#oberegrenze)</span> | obereGrenze | string |
| <span className="hbs-f hbs-e1">[zuordnungVon](/bo4e/202610/bo/Marktteilnehmer#zuordnungvon)</span> | Startdatum der Zuordnung des Marktteilnehmers | string (date-time) |
| <span className="hbs-f hbs-e1">[zuordnungBis](/bo4e/202610/bo/Marktteilnehmer#zuordnungbis)</span> | Enddatum der Zuordnung des Marktteilnehmers | string (date-time) |
| <span className="hbs-f hbs-e1">[bilanzkreis](/bo4e/202610/bo/Marktteilnehmer#bilanzkreis)</span> | Bilanzkreis | string |
| <span className="hbs-f hbs-e1">[verwendungszweckBilanzkreis](/bo4e/202610/bo/Marktteilnehmer#verwendungszweckbilanzkreis)</span> | Verwendungszweck des Bilanzkreises | [Enum VerwendungszweckBilanzkreis](/bo4e/202610/enum/VerwendungszweckBilanzkreis)<br/><Werte>`VERBRAUCHENDE_MARKTLOKATION`, `ERZEUGENDE_MARKTLOKATION_EEG`, `ERZEUGENDE_MARKTLOKATION_KWKG`, `SONSTIGE_ERZEUGENDE_MARKTLOKATION`</Werte> |
| <span className="hbs-f hbs-e0">[anbietername](/bo4e/202610/bo/Tarifinfo#anbietername)</span> | Der Name des Marktpartners, der den Tarif anbietet | string |
| <span className="hbs-f hbs-e0">[anwendung_von](/bo4e/202610/bo/Tarifinfo#anwendung_von)</span> | Angabe des inklusiven Zeitpunkts, ab dem der Tarif bzw. der Preis angewendet und abgerechnet wird | string (date-time) |
| <span className="hbs-f hbs-e0">[bemerkung](/bo4e/202610/bo/Tarifinfo#bemerkung)</span> | Freitext | string |
| <span className="hbs-f hbs-e0">[bezeichnung](/bo4e/202610/bo/Tarifinfo#bezeichnung)</span> | Name des Tarifs | string |
| <span className="hbs-g hbs-e0">[energiemix](/bo4e/202610/bo/Tarifinfo#energiemix)</span> | Der Energiemix, der für diesen Tarif gilt | [Energiemix](/bo4e/202610/com/Energiemix) |
| <span className="hbs-g hbs-e1">[anteil](/bo4e/202610/com/Energiemix#anteil) <span className="hbs-liste">[ ]</span></span> | Anteile der jeweiligen Erzeugungsart | [Energieherkunft[]](/bo4e/202610/com/Energieherkunft) |
| <span className="hbs-f hbs-e2">[erzeugungsart](/bo4e/202610/com/Energieherkunft#erzeugungsart)</span> | Art der Erzeugung | [Enum Erzeugungsart](/bo4e/202610/enum/Erzeugungsart)<br/><Werte>`EEG`, `KWK`, `EEG_DV`, `KWK_DV`, `WIND`, `SOLAR`, `KERNKRAFT`, `WASSER`, `GEOTHERMIE`, `BIOMASSE`, `KOHLE`, `GAS`, `SONSTIGE`, `SONSTIGE_EEG`, `SONSTIGE_ERZEUGUNGSART`</Werte> |
| <span className="hbs-f hbs-e2">[anteilProzent](/bo4e/202610/com/Energieherkunft#anteilprozent)</span> | Prozentualer Anteil der Erzeugung | number (float) |
| <span className="hbs-f hbs-e1">[atommuell](/bo4e/202610/com/Energiemix#atommuell)</span> | Höhe des erzeugten Atommülls in g/kWh | number (float) |
| <span className="hbs-f hbs-e1">[bemerkung](/bo4e/202610/com/Energiemix#bemerkung)</span> | Bemerkung zum Energiemix | string |
| <span className="hbs-f hbs-e1">[bezeichnung](/bo4e/202610/com/Energiemix#bezeichnung)</span> | Bezeichnung des Energiemix | string |
| <span className="hbs-f hbs-e1">[co2_emission](/bo4e/202610/com/Energiemix#co2_emission)</span> | Höhe des erzeugten CO2-Ausstosses in g/kWh | number (float) |
| <span className="hbs-f hbs-e1">[energieart](/bo4e/202610/com/Energiemix#energieart)</span> | Strom oder Gas etc. | [Enum Sparte](/bo4e/202610/enum/Sparte)<br/><Werte>`STROM`, `GAS`, `FERNWAERME`, `NAHWAERME`, `WASSER`, `ABWASSER`</Werte> |
| <span className="hbs-f hbs-e1">[energiemixnummer](/bo4e/202610/com/Energiemix#energiemixnummer)</span> | Eindeutige Nummer zur Identifizierung des Energiemixes | integer |
| <span className="hbs-f hbs-e1">[gueltigkeitsjahr](/bo4e/202610/com/Energiemix#gueltigkeitsjahr)</span> | Jahr, für das der Energiemix gilt | integer |
| <span className="hbs-f hbs-e1">[ist_in_oeko_top_ten](/bo4e/202610/com/Energiemix#ist_in_oeko_top_ten)</span> | Kennzeichen, ob der Versorger zu den Öko Top Ten gehört | boolean |
| <span className="hbs-f hbs-e1">[oekolabel](/bo4e/202610/com/Energiemix#oekolabel) <span className="hbs-liste">[ ]</span></span> | Ökolabel für den Energiemix | [Enum Oekolabel[]](/bo4e/202610/enum/Oekolabel)<br/><Werte>`ENERGREEN`, `GASGREEN`, `GASGREEN_GRUENER_STROM`, `GRUENER_STROM`, `GRUENER_STROM_GOLD`, `GRUENER_STROM_SILBER`, `GRUENES_GAS`, `NATURWATT_STROM`, `OK_POWER`, `RENEWABLE_PLUS`, `WATERGREEN`, `WATERGREEN_PLUS`</Werte> |
| <span className="hbs-f hbs-e1">[oekozertifikate](/bo4e/202610/com/Energiemix#oekozertifikate) <span className="hbs-liste">[ ]</span></span> | Zertifikate für den Energiemix | [Enum Oekozertifikat[]](/bo4e/202610/enum/Oekozertifikat)<br/><Werte>`BET`, `CMS_EE01`, `CMS_EE02`, `EECS`, `FRAUNHOFER`, `FREIBERG`, `KLIMA_INVEST`, `LGA`, `RECS`, `REGS_EGL`, `TUEV`, `TUEV_HESSEN`, `TUEV_NORD`, `TUEV_RHEINLAND`, `TUEV_SUED`, `TUEV_SUED_EE01`, `TUEV_SUED_EE02`</Werte> |
| <span className="hbs-f hbs-e1">[website](/bo4e/202610/com/Energiemix#website)</span> | Internetseite, auf der die Strommixdaten veröffentlicht sind | string |
| <span className="hbs-f hbs-e0">[kundentypen](/bo4e/202610/bo/Tarifinfo#kundentypen) <span className="hbs-liste">[ ]</span></span> | Kundentypen für den der Tarif gilt, z.B. Privatkunden | [Enum Kundentyp[]](/bo4e/202610/enum/Kundentyp)<br/><Werte>`BELEUCHTUNG_OEFFENTLICH`, `BELEUCHTUNG_STRASSE`, `DIREKTHEIZUNG`, `GEMEINSCHAFT_MFH`, `GEWERBE`, `HAUSHALT`, `KIRCHE`, `KWK`, `LADESAEULE`, `LANDWIRT`, `PRIVAT`, `SONSTIGE`, `SPEICHERHEIZUNG`, `UNTERBR_EINRICHTUNG`, `WAERMEPUMPE`</Werte> |
| <span className="hbs-f hbs-e0">[registeranzahl](/bo4e/202610/bo/Tarifinfo#registeranzahl)</span> | Die Art des Tarifes, z.B. Eintarif oder Mehrtarif | [Enum Registeranzahl](/bo4e/202610/enum/Registeranzahl)<br/><Werte>`EINTARIF`, `MEHRTARIF`, `ZWEITARIF`</Werte> |
| <span className="hbs-f hbs-e0">[sparte](/bo4e/202610/bo/Tarifinfo#sparte)</span> | Strom oder Gas, etc. | [Enum Sparte](/bo4e/202610/enum/Sparte)<br/><Werte>`STROM`, `GAS`, `FERNWAERME`, `NAHWAERME`, `WASSER`, `ABWASSER`</Werte> |
| <span className="hbs-f hbs-e0">[tarifmerkmale](/bo4e/202610/bo/Tarifinfo#tarifmerkmale) <span className="hbs-liste">[ ]</span></span> | Weitere Merkmale des Tarifs, z.B. Festpreis oder Vorkasse | [Enum Tarifmerkmal[]](/bo4e/202610/enum/Tarifmerkmal)<br/><Werte>`BAUSTROM`, `FESTPREIS`, `HAUSLICHT`, `HEIZSTROM`, `KOMBI`, `ONLINE`, `PAKET`, `STANDARD`, `VORKASSE`</Werte> |
| <span className="hbs-f hbs-e0">[tariftyp](/bo4e/202610/bo/Tarifinfo#tariftyp)</span> | Hinweis auf den Tariftyp, z.B. Grundversorgung oder Sondertarif | [Enum Tariftyp](/bo4e/202610/enum/Tariftyp)<br/><Werte>`ERSATZVERSORGUNG`, `GRUNDVERSORGUNG`, `GRUND_ERSATZVERSORGUNG`, `SONDERTARIF`</Werte> |
| <span className="hbs-g hbs-e0">[vertragskonditionen](/bo4e/202610/bo/Tarifinfo#vertragskonditionen)</span> | Mindestlaufzeiten und Kündigungsfristen zusammengefasst | [Vertragskonditionen](/bo4e/202610/com/Vertragskonditionen) |
| <span className="hbs-f hbs-e1">[netznutzungszahler](/bo4e/202610/com/Vertragskonditionen#netznutzungszahler)</span> | Netznutzungszahler | [Enum Netznutzungszahler](/bo4e/202610/enum/Netznutzungszahler)<br/><Werte>`KUNDE`, `LIEFERANT`</Werte> |
| <span className="hbs-f hbs-e1">[netznutzungsvertrag](/bo4e/202610/com/Vertragskonditionen#netznutzungsvertrag)</span> | Netznutzungsvertrag | [Enum Netznutzungsvertrag](/bo4e/202610/enum/Netznutzungsvertrag)<br/><Werte>`KUNDEN_NB`, `LIEFERANTEN_NB`</Werte> |
| <span className="hbs-g hbs-e1">[netznutzungsabrechnung](/bo4e/202610/com/Vertragskonditionen#netznutzungsabrechnung)</span> | — | [Zeitraum](/bo4e/202610/com/Zeitraum) |
| <span className="hbs-f hbs-e2">[zeiteinheit](/bo4e/202610/com/Zeitraum#zeiteinheit)</span> | Zeiteinheit | [Enum Zeiteinheit](/bo4e/202610/enum/Zeiteinheit)<br/><Werte>`SEKUNDE`, `MINUTE`, `STUNDE`, `VIERTEL_STUNDE`, `TAG`, `WOCHE`, `MONAT`, `QUARTAL`, `HALBJAHR`, `JAHR`</Werte> |
| <span className="hbs-f hbs-e2">[dauer](/bo4e/202610/com/Zeitraum#dauer)</span> | dauer | integer |
| <span className="hbs-f hbs-e2">[startdatum](/bo4e/202610/com/Zeitraum#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e2">[enddatum](/bo4e/202610/com/Zeitraum#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-f hbs-e2">[einheit](/bo4e/202610/com/Zeitraum#einheit)</span> | Zeiteinheit | [Enum Zeiteinheit](/bo4e/202610/enum/Zeiteinheit)<br/><Werte>`SEKUNDE`, `MINUTE`, `STUNDE`, `VIERTEL_STUNDE`, `TAG`, `WOCHE`, `MONAT`, `QUARTAL`, `HALBJAHR`, `JAHR`</Werte> |
| <span className="hbs-f hbs-e2">[ableseZeitraum](/bo4e/202610/com/Zeitraum#ablesezeitraum)</span> | ableseZeitraum | string |
| <span className="hbs-f hbs-e2">[abrechnungsZeitraum](/bo4e/202610/com/Zeitraum#abrechnungszeitraum)</span> | abrechnungsZeitraum | string |
| <span className="hbs-f hbs-e2">[zeitraumText](/bo4e/202610/com/Zeitraum#zeitraumtext)</span> | zeitraumText | string |
| <span className="hbs-f hbs-e2">[zeitraumId](/bo4e/202610/com/Zeitraum#zeitraumid)</span> | zeitraumId | integer |
| <span className="hbs-f hbs-e1">[beinhaltetSingulaerGenutzteBetriebsmittel](/bo4e/202610/com/Vertragskonditionen#beinhaltetsingulaergenutztebetriebsmittel)</span> | Singulär genutzte Betriebsmittel in der Netznutzungsabrechnung<br/>Hier wird angegeben, ob in der Netznutzungsabrechnung der verbrauchenden Marktlokation singulär<br/>genutzte Betriebsmittel abgerechnet werden. | boolean |
| <span className="hbs-f hbs-e1">[netznutzungsabrechnungsgrundlage](/bo4e/202610/com/Vertragskonditionen#netznutzungsabrechnungsgrundlage)</span> | Netznutzungsabrechnungsgrundlage | [Enum Netznutzungsabrechnungsgrundlage](/bo4e/202610/enum/Netznutzungsabrechnungsgrundlage)<br/><Werte>`LIEFERSCHEIN`, `ABWEICHENDE_GRUNDLAGE`</Werte> |
| <span className="hbs-f hbs-e1">[netznutzungsabrechnungsvariante](/bo4e/202610/com/Vertragskonditionen#netznutzungsabrechnungsvariante)</span> | Netznutzungsabrechnungsvariante | [Enum Netznutzungsabrechnungsvariante](/bo4e/202610/enum/Netznutzungsabrechnungsvariante)<br/><Werte>`ARBEITSPREIS_GRUNDPREIS`, `ARBEITSPREIS_LEISTUNGSPREIS`</Werte> |
| <span className="hbs-f hbs-e1">[haushaltskunde](/bo4e/202610/com/Vertragskonditionen#haushaltskunde)</span> | haushaltskunde | boolean |
| <span className="hbs-f hbs-e1">[abrechnungUeberNna](/bo4e/202610/com/Vertragskonditionen#abrechnunguebernna)</span> | abrechnungUeberNna | boolean |
| <span className="hbs-g hbs-e1">[gemeinderabatt](/bo4e/202610/com/Vertragskonditionen#gemeinderabatt)</span> | — | [Gemeinderabatt](/bo4e/202610/com/Gemeinderabatt) |
| <span className="hbs-f hbs-e2">[wert](/bo4e/202610/com/Gemeinderabatt#wert)</span> | Wert | number (float) |
| <span className="hbs-f hbs-e2">[einheit](/bo4e/202610/com/Gemeinderabatt#einheit)</span> | Einheit | string |
| <span className="hbs-f hbs-e2">[typ](/bo4e/202610/com/Gemeinderabatt#typ)</span> | Typ | string |
| <span className="hbs-f hbs-e2">[bemessungsgrundlage](/bo4e/202610/com/Gemeinderabatt#bemessungsgrundlage)</span> | Bemessungsgrundlage | number (float) |
| <span className="hbs-f hbs-e1">[startAbrechnungsjahr](/bo4e/202610/com/Vertragskonditionen#startabrechnungsjahr)</span> | startAbrechnungsjahr | string (date-time) |
| <span className="hbs-f hbs-e1">[naechstenetznutzungsabrechnung](/bo4e/202610/com/Vertragskonditionen#naechstenetznutzungsabrechnung)</span> | naechstenetznutzungsabrechnung | string |
| <span className="hbs-f hbs-e1">[abrechnungsintervall](/bo4e/202610/com/Vertragskonditionen#abrechnungsintervall)</span> | abrechnungsintervall | integer |
| <span className="hbs-f hbs-e1">[netznutzungsabrechnungIntervall](/bo4e/202610/com/Vertragskonditionen#netznutzungsabrechnungintervall)</span> | netznutzungsabrechnungIntervall | integer |
| <span className="hbs-g hbs-e1">[geplanteTurnusablesung](/bo4e/202610/com/Vertragskonditionen#geplanteturnusablesung)</span> | — | [Zeitraum](/bo4e/202610/com/Zeitraum) |
| <span className="hbs-f hbs-e2">[zeiteinheit](/bo4e/202610/com/Zeitraum#zeiteinheit)</span> | Zeiteinheit | [Enum Zeiteinheit](/bo4e/202610/enum/Zeiteinheit)<br/><Werte>`SEKUNDE`, `MINUTE`, `STUNDE`, `VIERTEL_STUNDE`, `TAG`, `WOCHE`, `MONAT`, `QUARTAL`, `HALBJAHR`, `JAHR`</Werte> |
| <span className="hbs-f hbs-e2">[dauer](/bo4e/202610/com/Zeitraum#dauer)</span> | dauer | integer |
| <span className="hbs-f hbs-e2">[startdatum](/bo4e/202610/com/Zeitraum#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e2">[enddatum](/bo4e/202610/com/Zeitraum#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-f hbs-e2">[einheit](/bo4e/202610/com/Zeitraum#einheit)</span> | Zeiteinheit | [Enum Zeiteinheit](/bo4e/202610/enum/Zeiteinheit)<br/><Werte>`SEKUNDE`, `MINUTE`, `STUNDE`, `VIERTEL_STUNDE`, `TAG`, `WOCHE`, `MONAT`, `QUARTAL`, `HALBJAHR`, `JAHR`</Werte> |
| <span className="hbs-f hbs-e2">[ableseZeitraum](/bo4e/202610/com/Zeitraum#ablesezeitraum)</span> | ableseZeitraum | string |
| <span className="hbs-f hbs-e2">[abrechnungsZeitraum](/bo4e/202610/com/Zeitraum#abrechnungszeitraum)</span> | abrechnungsZeitraum | string |
| <span className="hbs-f hbs-e2">[zeitraumText](/bo4e/202610/com/Zeitraum#zeitraumtext)</span> | zeitraumText | string |
| <span className="hbs-f hbs-e2">[zeitraumId](/bo4e/202610/com/Zeitraum#zeitraumid)</span> | zeitraumId | integer |
| <span className="hbs-f hbs-e1">[beauftragungMsb](/bo4e/202610/com/Vertragskonditionen#beauftragungmsb)</span> | BeauftragungMsb | [Enum BeauftragungMsb](/bo4e/202610/enum/BeauftragungMsb)<br/><Werte>`VERTRAG_AN_MSB`, `VERTRAGSBEENDIGUNG_MSB`</Werte> |
| <span className="hbs-g hbs-e1">[kuendigungsfrist](/bo4e/202610/com/Vertragskonditionen#kuendigungsfrist)</span> | Innerhalb dieser Frist kann der Vertrag gekündigt werden. Details Zeitraum | [Zeitraum](/bo4e/202610/com/Zeitraum) |
| <span className="hbs-f hbs-e2">[zeiteinheit](/bo4e/202610/com/Zeitraum#zeiteinheit)</span> | Zeiteinheit | [Enum Zeiteinheit](/bo4e/202610/enum/Zeiteinheit)<br/><Werte>`SEKUNDE`, `MINUTE`, `STUNDE`, `VIERTEL_STUNDE`, `TAG`, `WOCHE`, `MONAT`, `QUARTAL`, `HALBJAHR`, `JAHR`</Werte> |
| <span className="hbs-f hbs-e2">[dauer](/bo4e/202610/com/Zeitraum#dauer)</span> | dauer | integer |
| <span className="hbs-f hbs-e2">[startdatum](/bo4e/202610/com/Zeitraum#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e2">[enddatum](/bo4e/202610/com/Zeitraum#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-f hbs-e2">[einheit](/bo4e/202610/com/Zeitraum#einheit)</span> | Zeiteinheit | [Enum Zeiteinheit](/bo4e/202610/enum/Zeiteinheit)<br/><Werte>`SEKUNDE`, `MINUTE`, `STUNDE`, `VIERTEL_STUNDE`, `TAG`, `WOCHE`, `MONAT`, `QUARTAL`, `HALBJAHR`, `JAHR`</Werte> |
| <span className="hbs-f hbs-e2">[ableseZeitraum](/bo4e/202610/com/Zeitraum#ablesezeitraum)</span> | ableseZeitraum | string |
| <span className="hbs-f hbs-e2">[abrechnungsZeitraum](/bo4e/202610/com/Zeitraum#abrechnungszeitraum)</span> | abrechnungsZeitraum | string |
| <span className="hbs-f hbs-e2">[zeitraumText](/bo4e/202610/com/Zeitraum#zeitraumtext)</span> | zeitraumText | string |
| <span className="hbs-f hbs-e2">[zeitraumId](/bo4e/202610/com/Zeitraum#zeitraumid)</span> | zeitraumId | integer |
| <span className="hbs-g hbs-e1">[vertragslaufzeit](/bo4e/202610/com/Vertragskonditionen#vertragslaufzeit)</span> | Über diesen Zeitraum läuft der Vertrag. Details Zeitraum | [Zeitraum](/bo4e/202610/com/Zeitraum) |
| <span className="hbs-f hbs-e2">[zeiteinheit](/bo4e/202610/com/Zeitraum#zeiteinheit)</span> | Zeiteinheit | [Enum Zeiteinheit](/bo4e/202610/enum/Zeiteinheit)<br/><Werte>`SEKUNDE`, `MINUTE`, `STUNDE`, `VIERTEL_STUNDE`, `TAG`, `WOCHE`, `MONAT`, `QUARTAL`, `HALBJAHR`, `JAHR`</Werte> |
| <span className="hbs-f hbs-e2">[dauer](/bo4e/202610/com/Zeitraum#dauer)</span> | dauer | integer |
| <span className="hbs-f hbs-e2">[startdatum](/bo4e/202610/com/Zeitraum#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e2">[enddatum](/bo4e/202610/com/Zeitraum#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-f hbs-e2">[einheit](/bo4e/202610/com/Zeitraum#einheit)</span> | Zeiteinheit | [Enum Zeiteinheit](/bo4e/202610/enum/Zeiteinheit)<br/><Werte>`SEKUNDE`, `MINUTE`, `STUNDE`, `VIERTEL_STUNDE`, `TAG`, `WOCHE`, `MONAT`, `QUARTAL`, `HALBJAHR`, `JAHR`</Werte> |
| <span className="hbs-f hbs-e2">[ableseZeitraum](/bo4e/202610/com/Zeitraum#ablesezeitraum)</span> | ableseZeitraum | string |
| <span className="hbs-f hbs-e2">[abrechnungsZeitraum](/bo4e/202610/com/Zeitraum#abrechnungszeitraum)</span> | abrechnungsZeitraum | string |
| <span className="hbs-f hbs-e2">[zeitraumText](/bo4e/202610/com/Zeitraum#zeitraumtext)</span> | zeitraumText | string |
| <span className="hbs-f hbs-e2">[zeitraumId](/bo4e/202610/com/Zeitraum#zeitraumid)</span> | zeitraumId | integer |
| <span className="hbs-f hbs-e1">[kuendigungstermin](/bo4e/202610/com/Vertragskonditionen#kuendigungstermin)</span> | kuendigungstermin | string |
| <span className="hbs-g hbs-e1">[abschlagszyklus](/bo4e/202610/com/Vertragskonditionen#abschlagszyklus)</span> | In diesen Zyklen werden Abschläge gestellt. Details Zeitraum. Alternativ kann auch die Anzahl<br/>in den Konditionen angeben werden." | [Zeitraum](/bo4e/202610/com/Zeitraum) |
| <span className="hbs-f hbs-e2">[zeiteinheit](/bo4e/202610/com/Zeitraum#zeiteinheit)</span> | Zeiteinheit | [Enum Zeiteinheit](/bo4e/202610/enum/Zeiteinheit)<br/><Werte>`SEKUNDE`, `MINUTE`, `STUNDE`, `VIERTEL_STUNDE`, `TAG`, `WOCHE`, `MONAT`, `QUARTAL`, `HALBJAHR`, `JAHR`</Werte> |
| <span className="hbs-f hbs-e2">[dauer](/bo4e/202610/com/Zeitraum#dauer)</span> | dauer | integer |
| <span className="hbs-f hbs-e2">[startdatum](/bo4e/202610/com/Zeitraum#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e2">[enddatum](/bo4e/202610/com/Zeitraum#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-f hbs-e2">[einheit](/bo4e/202610/com/Zeitraum#einheit)</span> | Zeiteinheit | [Enum Zeiteinheit](/bo4e/202610/enum/Zeiteinheit)<br/><Werte>`SEKUNDE`, `MINUTE`, `STUNDE`, `VIERTEL_STUNDE`, `TAG`, `WOCHE`, `MONAT`, `QUARTAL`, `HALBJAHR`, `JAHR`</Werte> |
| <span className="hbs-f hbs-e2">[ableseZeitraum](/bo4e/202610/com/Zeitraum#ablesezeitraum)</span> | ableseZeitraum | string |
| <span className="hbs-f hbs-e2">[abrechnungsZeitraum](/bo4e/202610/com/Zeitraum#abrechnungszeitraum)</span> | abrechnungsZeitraum | string |
| <span className="hbs-f hbs-e2">[zeitraumText](/bo4e/202610/com/Zeitraum#zeitraumtext)</span> | zeitraumText | string |
| <span className="hbs-f hbs-e2">[zeitraumId](/bo4e/202610/com/Zeitraum#zeitraumid)</span> | zeitraumId | integer |
| <span className="hbs-f hbs-e1">[anzahl_abschlaege](/bo4e/202610/com/Vertragskonditionen#anzahl_abschlaege)</span> | Anzahl der vereinbarten Abschläge pro Jahr, z.B. 12 | number (float) |
| <span className="hbs-f hbs-e1">[beschreibung](/bo4e/202610/com/Vertragskonditionen#beschreibung)</span> | Freitext zur Beschreibung der Konditionen, z.B. "Standardkonditionen Gas" | string |
| <span className="hbs-g hbs-e1">[vertragsverlaengerung](/bo4e/202610/com/Vertragskonditionen#vertragsverlaengerung)</span> | Falls der Vertrag nicht gekündigt wird, verlängert er sich automatisch um die hier angegebene Zeit. Details<br/>Zeitraum | [Zeitraum](/bo4e/202610/com/Zeitraum) |
| <span className="hbs-f hbs-e2">[zeiteinheit](/bo4e/202610/com/Zeitraum#zeiteinheit)</span> | Zeiteinheit | [Enum Zeiteinheit](/bo4e/202610/enum/Zeiteinheit)<br/><Werte>`SEKUNDE`, `MINUTE`, `STUNDE`, `VIERTEL_STUNDE`, `TAG`, `WOCHE`, `MONAT`, `QUARTAL`, `HALBJAHR`, `JAHR`</Werte> |
| <span className="hbs-f hbs-e2">[dauer](/bo4e/202610/com/Zeitraum#dauer)</span> | dauer | integer |
| <span className="hbs-f hbs-e2">[startdatum](/bo4e/202610/com/Zeitraum#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e2">[enddatum](/bo4e/202610/com/Zeitraum#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-f hbs-e2">[einheit](/bo4e/202610/com/Zeitraum#einheit)</span> | Zeiteinheit | [Enum Zeiteinheit](/bo4e/202610/enum/Zeiteinheit)<br/><Werte>`SEKUNDE`, `MINUTE`, `STUNDE`, `VIERTEL_STUNDE`, `TAG`, `WOCHE`, `MONAT`, `QUARTAL`, `HALBJAHR`, `JAHR`</Werte> |
| <span className="hbs-f hbs-e2">[ableseZeitraum](/bo4e/202610/com/Zeitraum#ablesezeitraum)</span> | ableseZeitraum | string |
| <span className="hbs-f hbs-e2">[abrechnungsZeitraum](/bo4e/202610/com/Zeitraum#abrechnungszeitraum)</span> | abrechnungsZeitraum | string |
| <span className="hbs-f hbs-e2">[zeitraumText](/bo4e/202610/com/Zeitraum#zeitraumtext)</span> | zeitraumText | string |
| <span className="hbs-f hbs-e2">[zeitraumId](/bo4e/202610/com/Zeitraum#zeitraumid)</span> | zeitraumId | integer |
| <span className="hbs-f hbs-e0">[website](/bo4e/202610/bo/Tarifinfo#website)</span> | Internetseite auf dem der Tarif zu finden ist | string |
| <span className="hbs-g hbs-e0">[zeitliche_gueltigkeit](/bo4e/202610/bo/Tarifinfo#zeitliche_gueltigkeit)</span> | Angabe, in welchem Zeitraum der Tarif gültig ist | [Zeitraum](/bo4e/202610/com/Zeitraum) |
| <span className="hbs-f hbs-e1">[zeiteinheit](/bo4e/202610/com/Zeitraum#zeiteinheit)</span> | Zeiteinheit | [Enum Zeiteinheit](/bo4e/202610/enum/Zeiteinheit)<br/><Werte>`SEKUNDE`, `MINUTE`, `STUNDE`, `VIERTEL_STUNDE`, `TAG`, `WOCHE`, `MONAT`, `QUARTAL`, `HALBJAHR`, `JAHR`</Werte> |
| <span className="hbs-f hbs-e1">[dauer](/bo4e/202610/com/Zeitraum#dauer)</span> | dauer | integer |
| <span className="hbs-f hbs-e1">[startdatum](/bo4e/202610/com/Zeitraum#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e1">[enddatum](/bo4e/202610/com/Zeitraum#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-f hbs-e1">[einheit](/bo4e/202610/com/Zeitraum#einheit)</span> | Zeiteinheit | [Enum Zeiteinheit](/bo4e/202610/enum/Zeiteinheit)<br/><Werte>`SEKUNDE`, `MINUTE`, `STUNDE`, `VIERTEL_STUNDE`, `TAG`, `WOCHE`, `MONAT`, `QUARTAL`, `HALBJAHR`, `JAHR`</Werte> |
| <span className="hbs-f hbs-e1">[ableseZeitraum](/bo4e/202610/com/Zeitraum#ablesezeitraum)</span> | ableseZeitraum | string |
| <span className="hbs-f hbs-e1">[abrechnungsZeitraum](/bo4e/202610/com/Zeitraum#abrechnungszeitraum)</span> | abrechnungsZeitraum | string |
| <span className="hbs-f hbs-e1">[zeitraumText](/bo4e/202610/com/Zeitraum#zeitraumtext)</span> | zeitraumText | string |
| <span className="hbs-f hbs-e1">[zeitraumId](/bo4e/202610/com/Zeitraum#zeitraumid)</span> | zeitraumId | integer |

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
