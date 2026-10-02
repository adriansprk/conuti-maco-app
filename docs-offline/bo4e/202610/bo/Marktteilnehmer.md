# Marktteilnehmer
<span hidden data-pagefind-meta={"title:Marktteilnehmer — BO4E-Geschäftsobjekt (FV 202610)"} />

BO4E-Geschäftsobjekt · 35 Felder · 2395 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="botyp"></a>`boTyp` <span className="hbs-pflicht">\*</span> | [Enum BOTyp](/bo4e/202610/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> | Typ des BO |
| <a id="versionstruktur"></a>`versionStruktur` <span className="hbs-pflicht">\*</span> | string | versionStruktur |
| <a id="geschaeftspartnerrolle"></a>`geschaeftspartnerrolle` | [Enum Geschaeftspartnerrolle](/bo4e/202610/enum/Geschaeftspartnerrolle)<br/><Werte>`KUNDE`, `LIEFERANT`, `DIENSTLEISTER`, `INTERESSENT`, `MARKTPARTNER`, `EIGENTUEMER`, `HAUSVERWALTER`, `KORRESPONDENZEMPFAENGER`, `ABLESEKARTENEMPFAENGER`</Werte> | Rolle, die der Geschäftspartner hat (z.B. Interessent, Kunde). |
| <a id="anrede"></a>`anrede` | string | Die Anrede für den GePa, Z.B. Herr. |
| <a id="name1"></a>`name1` | string | Erster Teil des Namens. Hier kann der Firmenname oder bei Privatpersonen beispielsweise der Nachname dargestellt werden. Beispiele: Yellow Strom GmbH oder Hagen |
| <a id="name2"></a>`name2` | string | Zweiter Teil des Namens. Hier kann der eine Erweiterung zum Firmennamen oder bei Privatpersonen beispielsweise der Vorname dargestellt werden. Beispiele: Bereich Süd oder Nina |
| <a id="name3"></a>`name3` | string | Dritter Teil des Namens. Hier können weitere Ergänzungen zum Firmennamen oder bei Privatpersonen Zusätze zum Namen dargestellt werden. Beispiele: und Afrika oder Sängerin |
| <a id="name4"></a>`name4` | string | name4 |
| <a id="partneradresse"></a>`partneradresse` | [Adresse](/bo4e/202610/com/Adresse) | Adresse des Geschäftspartners, an der sich der Hauptsitz befindet. Details |
| <a id="gewerbekennzeichnung"></a>`gewerbekennzeichnung` | boolean | Kennzeichnung ob es sich um einen Gewerbe/Unternehmen (gewerbeKennzeichnung = true) oder eine Privatperson handelt. (gewerbeKennzeichnung = false) |
| <a id="externekundenummerlieferant"></a>`externeKundenummerLieferant` | string | externeKundenummerLieferant |
| <a id="marktrolle"></a>`marktrolle` | [Enum Marktrolle](/bo4e/202610/enum/Marktrolle)<br/><Werte>`NB`, `LF`, `MSB`, `MSBA`, `GMSB`, `MDL`, `DL`, `BKV`, `UENB`, `KUNDE-SELBST-NN`, `MGV`, `EIV`, `RB`, `KUNDE`, `INTERESSENT`, `KN`, `UBA`, `BIKO`, `ESA`</Werte> | Gibt im Klartext die Bezeichnung der Marktrolle an. |
| <a id="rollencodenummer"></a>`rollencodenummer` | string | Gibt die Codenummer der Marktrolle an. |
| <a id="rollencodetyp"></a>`rollencodetyp` | [Enum Rollencodetyp](/bo4e/202610/enum/Rollencodetyp)<br/><Werte>`BDEW`, `GS1`, `GLN`, `DVGW`</Werte> | Gibt den Typ des Codes an. |
| <a id="umsatzsteuerid"></a>`umsatzsteuerId` | string | Die Umsatzsteuer-ID des Geschäftspartners. Beispiel: DE 813281825 |
| <a id="steuernummer"></a>`steuernummer` | string | Die Steuernummer-ID des Geschäftspartners. Beispiel: 30120345678 |
| <a id="ansprechpartner"></a>`ansprechpartner` | [Ansprechpartner](/bo4e/202610/bo/Ansprechpartner) | Ansprechpartner as in EDIFACT NAD+MS, that includes e.g. the email address of a natural person. |
| <a id="makoadresse"></a>`makoadresse` | string | Die 1:1-Kommunikationsadresse des Marktteilnehmers. Diese wird in der Marktkommunikation verwendet. |
| <a id="downloadlinkzertifikat"></a>`downloadlinkZertifikat` | string | downloadlinkZertifikat |
| <a id="amtsgericht"></a>`amtsgericht` | string | Amtsgericht bzw Handelsregistergericht, das die Handelsregisternummer herausgegeben hat |
| <a id="hrnummer"></a>`hrnummer` | string | Handelsregisternummer des Geschäftspartners |
| <a id="website"></a>`website` | string | Internetseite des Marktpartners. Beispiel: www.mp-energie.de |
| <a id="faxnummer"></a>`faxnummer` | string | faxnummer |
| <a id="kommunikationsrolle"></a>`kommunikationsrolle` | [Enum Kommunikationsrolle](/bo4e/202610/enum/Kommunikationsrolle)<br/><Werte>`DATENAUSTAUSCH`, `RAHMENVERTRAEGE`, `KUENDIGUNGSPROZESSE`, `WECHSELPROZESSE`, `STAMMDATENPROZESSE`, `EINSPEISEPROZESSE`, `ABRECHNUNGSPROZESSE`, `MMMA_PROZESSE`, `BEWEGUNGSDATEN`, `ENT_SPERR_PROZESSE`, `BILANZIERUNGSPROZESSE`, `NETZANSCHLUSS_ANLAGEN`</Werte> | Kommunikationsrolle |
| <a id="weiterverpflichtet"></a>`weiterverpflichtet` | boolean | weiterverpflichtet |
| <a id="kommunikationsparameter"></a>`kommunikationsparameter` | [Kommunikationsparameter](/bo4e/202610/com/Kommunikationsparameter) | — |
| <a id="messstellenbetreibereigenschaft"></a>`messstellenbetreiberEigenschaft` | [Enum MSBEigenschaft](/bo4e/202610/enum/MSBEigenschaft)<br/><Werte>`GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER`, `WETTBEWERBLICHER_MESSSTELLENBETREIBER`, `AUFFANGMESSSTELLENBETREIBER`</Werte> | MSBEigenschaft |
| <a id="bankverbindung"></a>`bankverbindung` | [Bankverbindung[]](/bo4e/202610/com/Bankverbindung) | Bankverbindung |
| <a id="erreichbarkeit"></a>`erreichbarkeit` | [Erreichbarkeit[]](/bo4e/202610/com/Erreichbarkeit) | Die Erreichbarkeit eines Unternehmens an Werktagen. |
| <a id="ipadresse"></a>`ipAdresse` | string | ipAdresse |
| <a id="iprange"></a>`ipRange` | [IpRange](/bo4e/202610/com/IpRange) | — |
| <a id="zuordnungvon"></a>`zuordnungVon` | string (date-time) | Startdatum der Zuordnung des Marktteilnehmers |
| <a id="zuordnungbis"></a>`zuordnungBis` | string (date-time) | Enddatum der Zuordnung des Marktteilnehmers |
| <a id="bilanzkreis"></a>`bilanzkreis` | string | Bilanzkreis |
| <a id="verwendungszweckbilanzkreis"></a>`verwendungszweckBilanzkreis` | [Enum VerwendungszweckBilanzkreis](/bo4e/202610/enum/VerwendungszweckBilanzkreis)<br/><Werte>`VERBRAUCHENDE_MARKTLOKATION`, `ERZEUGENDE_MARKTLOKATION_EEG`, `ERZEUGENDE_MARKTLOKATION_KWKG`, `SONSTIGE_ERZEUGENDE_MARKTLOKATION`</Werte> | Verwendungszweck des Bilanzkreises |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[boTyp](/bo4e/202610/bo/Marktteilnehmer#botyp) <span className="hbs-pflicht">\*</span></span> | Typ des BO | [Enum BOTyp](/bo4e/202610/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> |
| <span className="hbs-f hbs-e0">[versionStruktur](/bo4e/202610/bo/Marktteilnehmer#versionstruktur) <span className="hbs-pflicht">\*</span></span> | versionStruktur | string |
| <span className="hbs-f hbs-e0">[geschaeftspartnerrolle](/bo4e/202610/bo/Marktteilnehmer#geschaeftspartnerrolle)</span> | Rolle, die der Geschäftspartner hat (z.B. Interessent, Kunde). | [Enum Geschaeftspartnerrolle](/bo4e/202610/enum/Geschaeftspartnerrolle)<br/><Werte>`KUNDE`, `LIEFERANT`, `DIENSTLEISTER`, `INTERESSENT`, `MARKTPARTNER`, `EIGENTUEMER`, `HAUSVERWALTER`, `KORRESPONDENZEMPFAENGER`, `ABLESEKARTENEMPFAENGER`</Werte> |
| <span className="hbs-f hbs-e0">[anrede](/bo4e/202610/bo/Marktteilnehmer#anrede)</span> | Die Anrede für den GePa, Z.B. Herr. | string |
| <span className="hbs-f hbs-e0">[name1](/bo4e/202610/bo/Marktteilnehmer#name1)</span> | Erster Teil des Namens. Hier kann der Firmenname oder bei Privatpersonen<br/>beispielsweise der Nachname dargestellt werden. Beispiele: Yellow Strom GmbH<br/>oder Hagen | string |
| <span className="hbs-f hbs-e0">[name2](/bo4e/202610/bo/Marktteilnehmer#name2)</span> | Zweiter Teil des Namens. Hier kann der eine Erweiterung zum Firmennamen oder<br/>bei Privatpersonen beispielsweise der Vorname dargestellt werden. Beispiele:<br/>Bereich Süd oder Nina | string |
| <span className="hbs-f hbs-e0">[name3](/bo4e/202610/bo/Marktteilnehmer#name3)</span> | Dritter Teil des Namens. Hier können weitere Ergänzungen zum Firmennamen oder<br/>bei Privatpersonen Zusätze zum Namen dargestellt werden. Beispiele: und Afrika<br/>oder Sängerin | string |
| <span className="hbs-f hbs-e0">[name4](/bo4e/202610/bo/Marktteilnehmer#name4)</span> | name4 | string |
| <span className="hbs-g hbs-e0">[partneradresse](/bo4e/202610/bo/Marktteilnehmer#partneradresse)</span> | Adresse des Geschäftspartners, an der sich der Hauptsitz befindet. Details | [Adresse](/bo4e/202610/com/Adresse) |
| <span className="hbs-f hbs-e1">[postleitzahl](/bo4e/202610/com/Adresse#postleitzahl)</span> | Postleitzahl | string |
| <span className="hbs-f hbs-e1">[ort](/bo4e/202610/com/Adresse#ort)</span> | Ort | string |
| <span className="hbs-f hbs-e1">[strasse](/bo4e/202610/com/Adresse#strasse)</span> | Strasse | string |
| <span className="hbs-f hbs-e1">[hausnummer](/bo4e/202610/com/Adresse#hausnummer)</span> | Hausnummer und Ergänzung | string |
| <span className="hbs-f hbs-e1">[postfach](/bo4e/202610/com/Adresse#postfach)</span> | Postfach | string |
| <span className="hbs-f hbs-e1">[adresszusatz](/bo4e/202610/com/Adresse#adresszusatz)</span> | Adresszusatz | string |
| <span className="hbs-f hbs-e1">[coErgaenzung](/bo4e/202610/com/Adresse#coergaenzung)</span> | coErgaenzung | string |
| <span className="hbs-f hbs-e1">[landescode](/bo4e/202610/com/Adresse#landescode)</span> | Landescode | [Enum Landescode](/bo4e/202610/enum/Landescode)<br/><Werte>`AC`, `AD`, `AE`, `AF`, `AG`, `AI`, `AL`, `AM`, `AN`, `AO`, `AQ`, `AR`, `AS`, `AT`, `AU`, `AW`, `AX`, `AZ`, `BA`, `BB`, `BD`, `BE`, `BF`, `BG`, `BH`, `BI`, `BJ`, `BL`, `BM`, `BN`, `BO`, `BQ`, `BR`, `BS`, `BT`, `BU`, `BV`, `BW`, `BY`, `BZ`, `CA`, `CC`, `CD`, `CF`, `CG`, `CH`, `CI`, `CK`, `CL`, `CM`, `CN`, `CO`, `CP`, `CR`, `CS`, `CU`, `CV`, `CW`, `CX`, `CY`, `CZ`, `DE`, `DG`, `DJ`, `DK`, `DM`, `DO`, `DZ`, `EA`, `EC`, `EE`, `EG`, `EH`, `ER`, `ES`, `ET`, `EU`, `FI`, `FJ`, `FK`, `FM`, `FO`, `FR`, `FX`, `GA`, `GB`, `GD`, `GE`, `GF`, `GG`, `GH`, `GI`, `GL`, `GM`, `GN`, `GP`, `GQ`, `GR`, `GS`, `GT`, `GU`, `GW`, `GY`, `HK`, `HM`, `HN`, `HR`, `HT`, `HU`, `IC`, `ID`, `IE`, `IL`, `IM`, `IN`, `IO`, `IQ`, `IR`, `IS`, `IT`, `JE`, `JM`, `JO`, `JP`, `KE`, `KG`, `KH`, `KI`, `KM`, `KN`, `KP`, `KR`, `KW`, `KY`, `KZ`, `LA`, `LB`, `LC`, `LI`, `LK`, `LR`, `LS`, `LT`, `LU`, `LV`, `LY`, `MA`, `MC`, `MD`, `ME`, `MF`, `MG`, `MH`, `MK`, `ML`, `MM`, `MN`, `MO`, `MP`, `MQ`, `MR`, `MS`, `MT`, `MU`, `MV`, `MW`, `MX`, `MY`, `MZ`, `NA`, `NC`, `NE`, `NF`, `NG`, `NI`, `NL`, `NO`, `NP`, `NR`, `NT`, `NU`, `NZ`, `OM`, `PA`, `PE`, `PF`, `PG`, `PH`, `PK`, `PL`, `PM`, `PN`, `PR`, `PS`, `PT`, `PW`, `PY`, `QA`, `RE`, `RO`, `RS`, `RU`, `RW`, `SA`, `SB`, `SC`, `SD`, `SE`, `SF`, `SG`, `SH`, `SI`, `SJ`, `SK`, `SL`, `SM`, `SN`, `SO`, `SR`, `SS`, `ST`, `SU`, `SV`, `SX`, `SY`, `SZ`, `TA`, `TC`, `TD`, `TF`, `TG`, `TJ`, `TK`, `TL`, `TM`, `TN`, `TO`, `TP`, `TR`, `TT`, `TV`, `TW`, `TZ`, `UA`, `UG`, `UK`, `UM`, `US`, `UY`, `UZ`, `VA`, `VC`, `VE`, `VG`, `VI`, `VN`, `VU`, `WF`, `WS`, `XK`, `YE`, `YT`, `YU`, `ZA`, `ZM`, `ZR`, `ZW`</Werte> |
| <span className="hbs-f hbs-e1">[ortsteil](/bo4e/202610/com/Adresse#ortsteil)</span> | Ortsteil | string |
| <span className="hbs-g hbs-e1">[zusatzInformation](/bo4e/202610/com/Adresse#zusatzinformation)</span> | — | [AdresszusatzInformation](/bo4e/202610/com/AdresszusatzInformation) |
| <span className="hbs-f hbs-e2">[zusatz1](/bo4e/202610/com/AdresszusatzInformation#zusatz1)</span> | Adresszusatz 1 | string |
| <span className="hbs-f hbs-e2">[zusatz2](/bo4e/202610/com/AdresszusatzInformation#zusatz2)</span> | Adresszusatz 2 | string |
| <span className="hbs-f hbs-e2">[zusatz3](/bo4e/202610/com/AdresszusatzInformation#zusatz3)</span> | Adresszusatz 3 | string |
| <span className="hbs-f hbs-e2">[zusatz4](/bo4e/202610/com/AdresszusatzInformation#zusatz4)</span> | Adresszusatz 4 | string |
| <span className="hbs-f hbs-e2">[zusatz5](/bo4e/202610/com/AdresszusatzInformation#zusatz5)</span> | Adresszusatz 5 | string |
| <span className="hbs-f hbs-e0">[gewerbekennzeichnung](/bo4e/202610/bo/Marktteilnehmer#gewerbekennzeichnung)</span> | Kennzeichnung ob es sich um einen Gewerbe/Unternehmen (gewerbeKennzeichnung = true)<br/>oder eine Privatperson handelt. (gewerbeKennzeichnung = false) | boolean |
| <span className="hbs-f hbs-e0">[externeKundenummerLieferant](/bo4e/202610/bo/Marktteilnehmer#externekundenummerlieferant)</span> | externeKundenummerLieferant | string |
| <span className="hbs-f hbs-e0">[marktrolle](/bo4e/202610/bo/Marktteilnehmer#marktrolle)</span> | Gibt im Klartext die Bezeichnung der Marktrolle an. | [Enum Marktrolle](/bo4e/202610/enum/Marktrolle)<br/><Werte>`NB`, `LF`, `MSB`, `MSBA`, `GMSB`, `MDL`, `DL`, `BKV`, `UENB`, `KUNDE-SELBST-NN`, `MGV`, `EIV`, `RB`, `KUNDE`, `INTERESSENT`, `KN`, `UBA`, `BIKO`, `ESA`</Werte> |
| <span className="hbs-f hbs-e0">[rollencodenummer](/bo4e/202610/bo/Marktteilnehmer#rollencodenummer)</span> | Gibt die Codenummer der Marktrolle an. | string |
| <span className="hbs-f hbs-e0">[rollencodetyp](/bo4e/202610/bo/Marktteilnehmer#rollencodetyp)</span> | Gibt den Typ des Codes an. | [Enum Rollencodetyp](/bo4e/202610/enum/Rollencodetyp)<br/><Werte>`BDEW`, `GS1`, `GLN`, `DVGW`</Werte> |
| <span className="hbs-f hbs-e0">[umsatzsteuerId](/bo4e/202610/bo/Marktteilnehmer#umsatzsteuerid)</span> | Die Umsatzsteuer-ID des Geschäftspartners. Beispiel: DE 813281825 | string |
| <span className="hbs-f hbs-e0">[steuernummer](/bo4e/202610/bo/Marktteilnehmer#steuernummer)</span> | Die Steuernummer-ID des Geschäftspartners. Beispiel: 30120345678 | string |
| <span className="hbs-g hbs-e0">[ansprechpartner](/bo4e/202610/bo/Marktteilnehmer#ansprechpartner)</span> | Ansprechpartner as in EDIFACT NAD+MS, that includes e.g. the email address of a natural person. | [Ansprechpartner](/bo4e/202610/bo/Ansprechpartner) |
| <span className="hbs-f hbs-e1">[boTyp](/bo4e/202610/bo/Ansprechpartner#botyp) <span className="hbs-pflicht">\*</span></span> | Typ des BO | [Enum BOTyp](/bo4e/202610/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> |
| <span className="hbs-f hbs-e1">[versionStruktur](/bo4e/202610/bo/Ansprechpartner#versionstruktur) <span className="hbs-pflicht">\*</span></span> | versionStruktur | string |
| <span className="hbs-f hbs-e1">[nachname](/bo4e/202610/bo/Ansprechpartner#nachname)</span> | Nachname (Familienname) des Ansprechpartners | string |
| <span className="hbs-f hbs-e1">[eMailAdresse](/bo4e/202610/bo/Ansprechpartner#emailadresse)</span> | E-Mail Adresse | string |
| <span className="hbs-g hbs-e1">[rufnummern](/bo4e/202610/bo/Ansprechpartner#rufnummern) <span className="hbs-liste">[ ]</span></span> | Liste der Telefonnummern, unter denen der Ansprechpartner erreichbar ist. | [Rufnummer[]](/bo4e/202610/com/Rufnummer) |
| <span className="hbs-f hbs-e2">[nummerntyp](/bo4e/202610/com/Rufnummer#nummerntyp)</span> | Rufnummernart | [Enum Rufnummernart](/bo4e/202610/enum/Rufnummernart)<br/><Werte>`RUF_ZENTRALE`, `FAX_ZENTRALE`, `SAMMELRUF`, `SAMMELFAX`, `ABTEILUNGRUF`, `ABTEILUNGFAX`, `RUF_DURCHWAHL`, `FAX_DURCHWAHL`, `MOBIL_NUMMER`</Werte> |
| <span className="hbs-f hbs-e2">[rufnummer](/bo4e/202610/com/Rufnummer#rufnummer)</span> | rufnummer | string |
| <span className="hbs-f hbs-e0">[makoadresse](/bo4e/202610/bo/Marktteilnehmer#makoadresse)</span> | Die 1:1-Kommunikationsadresse des Marktteilnehmers. Diese wird in der<br/>Marktkommunikation verwendet. | string |
| <span className="hbs-f hbs-e0">[downloadlinkZertifikat](/bo4e/202610/bo/Marktteilnehmer#downloadlinkzertifikat)</span> | downloadlinkZertifikat | string |
| <span className="hbs-f hbs-e0">[amtsgericht](/bo4e/202610/bo/Marktteilnehmer#amtsgericht)</span> | Amtsgericht bzw Handelsregistergericht, das die Handelsregisternummer herausgegeben hat | string |
| <span className="hbs-f hbs-e0">[hrnummer](/bo4e/202610/bo/Marktteilnehmer#hrnummer)</span> | Handelsregisternummer des Geschäftspartners | string |
| <span className="hbs-f hbs-e0">[website](/bo4e/202610/bo/Marktteilnehmer#website)</span> | Internetseite des Marktpartners. Beispiel: www.mp-energie.de | string |
| <span className="hbs-f hbs-e0">[faxnummer](/bo4e/202610/bo/Marktteilnehmer#faxnummer)</span> | faxnummer | string |
| <span className="hbs-f hbs-e0">[kommunikationsrolle](/bo4e/202610/bo/Marktteilnehmer#kommunikationsrolle)</span> | Kommunikationsrolle | [Enum Kommunikationsrolle](/bo4e/202610/enum/Kommunikationsrolle)<br/><Werte>`DATENAUSTAUSCH`, `RAHMENVERTRAEGE`, `KUENDIGUNGSPROZESSE`, `WECHSELPROZESSE`, `STAMMDATENPROZESSE`, `EINSPEISEPROZESSE`, `ABRECHNUNGSPROZESSE`, `MMMA_PROZESSE`, `BEWEGUNGSDATEN`, `ENT_SPERR_PROZESSE`, `BILANZIERUNGSPROZESSE`, `NETZANSCHLUSS_ANLAGEN`</Werte> |
| <span className="hbs-f hbs-e0">[weiterverpflichtet](/bo4e/202610/bo/Marktteilnehmer#weiterverpflichtet)</span> | weiterverpflichtet | boolean |
| <span className="hbs-g hbs-e0">[kommunikationsparameter](/bo4e/202610/bo/Marktteilnehmer#kommunikationsparameter)</span> | — | [Kommunikationsparameter](/bo4e/202610/com/Kommunikationsparameter) |
| <span className="hbs-g hbs-e1">[zieladresse](/bo4e/202610/com/Kommunikationsparameter#zieladresse)</span> | — | [Zieladresse](/bo4e/202610/com/Zieladresse) |
| <span className="hbs-f hbs-e2">[zieladresse1](/bo4e/202610/com/Zieladresse#zieladresse1)</span> | zieladresse1 | string |
| <span className="hbs-f hbs-e2">[zieladresse2](/bo4e/202610/com/Zieladresse#zieladresse2)</span> | zieladresse2 | string |
| <span className="hbs-f hbs-e2">[zieladresse3](/bo4e/202610/com/Zieladresse#zieladresse3)</span> | zieladresse3 | string |
| <span className="hbs-f hbs-e2">[zieladresse4](/bo4e/202610/com/Zieladresse#zieladresse4)</span> | zieladresse4 | string |
| <span className="hbs-f hbs-e2">[zieladresse5](/bo4e/202610/com/Zieladresse#zieladresse5)</span> | zieladresse5 | string |
| <span className="hbs-g hbs-e1">[zertifikatsAussteller](/bo4e/202610/com/Kommunikationsparameter#zertifikatsaussteller)</span> | — | [ZertifikatsAussteller](/bo4e/202610/com/ZertifikatsAussteller) |
| <span className="hbs-f hbs-e2">[zertifikatsAussteller1](/bo4e/202610/com/ZertifikatsAussteller#zertifikatsaussteller1)</span> | zertifikatsAussteller1 | string |
| <span className="hbs-f hbs-e2">[zertifikatsAussteller2](/bo4e/202610/com/ZertifikatsAussteller#zertifikatsaussteller2)</span> | zertifikatsAussteller2 | string |
| <span className="hbs-f hbs-e2">[zertifikatsAussteller3](/bo4e/202610/com/ZertifikatsAussteller#zertifikatsaussteller3)</span> | zertifikatsAussteller3 | string |
| <span className="hbs-f hbs-e2">[zertifikatsAussteller4](/bo4e/202610/com/ZertifikatsAussteller#zertifikatsaussteller4)</span> | zertifikatsAussteller4 | string |
| <span className="hbs-f hbs-e2">[zertifikatsAussteller5](/bo4e/202610/com/ZertifikatsAussteller#zertifikatsaussteller5)</span> | zertifikatsAussteller5 | string |
| <span className="hbs-g hbs-e1">[zertifikatsNutzer](/bo4e/202610/com/Kommunikationsparameter#zertifikatsnutzer)</span> | — | [ZertifikatsNutzer](/bo4e/202610/com/ZertifikatsNutzer) |
| <span className="hbs-f hbs-e2">[zertifikatsNutzer1](/bo4e/202610/com/ZertifikatsNutzer#zertifikatsnutzer1)</span> | zertifikatsNutzer1 | string |
| <span className="hbs-f hbs-e2">[zertifikatsNutzer2](/bo4e/202610/com/ZertifikatsNutzer#zertifikatsnutzer2)</span> | zertifikatsNutzer2 | string |
| <span className="hbs-f hbs-e2">[zertifikatsNutzer3](/bo4e/202610/com/ZertifikatsNutzer#zertifikatsnutzer3)</span> | zertifikatsNutzer3 | string |
| <span className="hbs-f hbs-e2">[zertifikatsNutzer4](/bo4e/202610/com/ZertifikatsNutzer#zertifikatsnutzer4)</span> | zertifikatsNutzer4 | string |
| <span className="hbs-f hbs-e2">[zertifikatsNutzer5](/bo4e/202610/com/ZertifikatsNutzer#zertifikatsnutzer5)</span> | zertifikatsNutzer5 | string |
| <span className="hbs-f hbs-e0">[messstellenbetreiberEigenschaft](/bo4e/202610/bo/Marktteilnehmer#messstellenbetreibereigenschaft)</span> | MSBEigenschaft | [Enum MSBEigenschaft](/bo4e/202610/enum/MSBEigenschaft)<br/><Werte>`GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER`, `WETTBEWERBLICHER_MESSSTELLENBETREIBER`, `AUFFANGMESSSTELLENBETREIBER`</Werte> |
| <span className="hbs-g hbs-e0">[bankverbindung](/bo4e/202610/bo/Marktteilnehmer#bankverbindung) <span className="hbs-liste">[ ]</span></span> | Bankverbindung | [Bankverbindung[]](/bo4e/202610/com/Bankverbindung) |
| <span className="hbs-f hbs-e1">[verwendungszweck](/bo4e/202610/com/Bankverbindung#verwendungszweck)</span> | BankverbindungVerwendungszweck | [Enum BankverbindungVerwendungszweck](/bo4e/202610/enum/BankverbindungVerwendungszweck)<br/><Werte>`BV_ZAHLUNG_NNA`, `BV_ZAHLUNG_MMMA`, `BV_ZAHLUNG_MSB_ABRECHNNUNG`, `BV_ZAHLUNG_ENT_SPERREN_ABRECHNUNG`, `BV_SONSTIGE`</Werte> |
| <span className="hbs-f hbs-e1">[iban](/bo4e/202610/com/Bankverbindung#iban)</span> | IBAN | string |
| <span className="hbs-f hbs-e1">[kontoinhaber](/bo4e/202610/com/Bankverbindung#kontoinhaber)</span> | Der Kontoinhaber | string |
| <span className="hbs-f hbs-e1">[bic](/bo4e/202610/com/Bankverbindung#bic)</span> | BIC Code | string |
| <span className="hbs-f hbs-e1">[kreditinstitut](/bo4e/202610/com/Bankverbindung#kreditinstitut)</span> | Name des Kreditinstitut | string |
| <span className="hbs-g hbs-e0">[erreichbarkeit](/bo4e/202610/bo/Marktteilnehmer#erreichbarkeit) <span className="hbs-liste">[ ]</span></span> | Die Erreichbarkeit eines Unternehmens an Werktagen. | [Erreichbarkeit[]](/bo4e/202610/com/Erreichbarkeit) |
| <span className="hbs-f hbs-e1">[verfuegbarkeit](/bo4e/202610/com/Erreichbarkeit#verfuegbarkeit)</span> | Verfuegbarkeit | [Enum Verfuegbarkeit](/bo4e/202610/enum/Verfuegbarkeit)<br/><Werte>`MONTAG`, `DIENSTAG`, `MITTWOCH`, `DONNERSTAG`, `FREITAG`, `PAUSE`</Werte> |
| <span className="hbs-f hbs-e1">[zeit](/bo4e/202610/com/Erreichbarkeit#zeit)</span> | Zeit der Erreichbarkeit | string |
| <span className="hbs-f hbs-e0">[ipAdresse](/bo4e/202610/bo/Marktteilnehmer#ipadresse)</span> | ipAdresse | string |
| <span className="hbs-g hbs-e0">[ipRange](/bo4e/202610/bo/Marktteilnehmer#iprange)</span> | — | [IpRange](/bo4e/202610/com/IpRange) |
| <span className="hbs-f hbs-e1">[untereGrenze](/bo4e/202610/com/IpRange#unteregrenze)</span> | untereGrenze | string |
| <span className="hbs-f hbs-e1">[obereGrenze](/bo4e/202610/com/IpRange#oberegrenze)</span> | obereGrenze | string |
| <span className="hbs-f hbs-e0">[zuordnungVon](/bo4e/202610/bo/Marktteilnehmer#zuordnungvon)</span> | Startdatum der Zuordnung des Marktteilnehmers | string (date-time) |
| <span className="hbs-f hbs-e0">[zuordnungBis](/bo4e/202610/bo/Marktteilnehmer#zuordnungbis)</span> | Enddatum der Zuordnung des Marktteilnehmers | string (date-time) |
| <span className="hbs-f hbs-e0">[bilanzkreis](/bo4e/202610/bo/Marktteilnehmer#bilanzkreis)</span> | Bilanzkreis | string |
| <span className="hbs-f hbs-e0">[verwendungszweckBilanzkreis](/bo4e/202610/bo/Marktteilnehmer#verwendungszweckbilanzkreis)</span> | Verwendungszweck des Bilanzkreises | [Enum VerwendungszweckBilanzkreis](/bo4e/202610/enum/VerwendungszweckBilanzkreis)<br/><Werte>`VERBRAUCHENDE_MARKTLOKATION`, `ERZEUGENDE_MARKTLOKATION_EEG`, `ERZEUGENDE_MARKTLOKATION_KWKG`, `SONSTIGE_ERZEUGENDE_MARKTLOKATION`</Werte> |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### anrede

18 Verwendung(en) in den Nachrichtentypen PARTIN.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_37000](/schnittstellen/202610/pruefi/PARTIN/PI_37000) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben |
| [PI_37000](/schnittstellen/202610/pruefi/PARTIN/PI_37000) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37001](/schnittstellen/202610/pruefi/PARTIN/PI_37001) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben |
| [PI_37001](/schnittstellen/202610/pruefi/PARTIN/PI_37001) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37002](/schnittstellen/202610/pruefi/PARTIN/PI_37002) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben |
| [PI_37002](/schnittstellen/202610/pruefi/PARTIN/PI_37002) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37008](/schnittstellen/202610/pruefi/PARTIN/PI_37008) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben |
| [PI_37008](/schnittstellen/202610/pruefi/PARTIN/PI_37008) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37009](/schnittstellen/202610/pruefi/PARTIN/PI_37009) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben |
| [PI_37009](/schnittstellen/202610/pruefi/PARTIN/PI_37009) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37010](/schnittstellen/202610/pruefi/PARTIN/PI_37010) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben |
| [PI_37010](/schnittstellen/202610/pruefi/PARTIN/PI_37010) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37012](/schnittstellen/202610/pruefi/PARTIN/PI_37012) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben |
| [PI_37012](/schnittstellen/202610/pruefi/PARTIN/PI_37012) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37013](/schnittstellen/202610/pruefi/PARTIN/PI_37013) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben |
| [PI_37013](/schnittstellen/202610/pruefi/PARTIN/PI_37013) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37014](/schnittstellen/202610/pruefi/PARTIN/PI_37014) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben |
| [PI_37014](/schnittstellen/202610/pruefi/PARTIN/PI_37014) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |

### name1

40 Verwendung(en) in den Nachrichtentypen INVOIC, PARTIN.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_31001](/schnittstellen/202610/pruefi/INVOIC/PI_31001) | Prüfi | INVOIC | transaktionsdaten › absender |
| [PI_31001](/schnittstellen/202610/pruefi/INVOIC/PI_31001) | Prüfi | INVOIC | transaktionsdaten › empfaenger |
| [PI_31002](/schnittstellen/202610/pruefi/INVOIC/PI_31002) | Prüfi | INVOIC | transaktionsdaten › absender |
| [PI_31002](/schnittstellen/202610/pruefi/INVOIC/PI_31002) | Prüfi | INVOIC | transaktionsdaten › empfaenger |
| [PI_31003](/schnittstellen/202610/pruefi/INVOIC/PI_31003) | Prüfi | INVOIC | transaktionsdaten › absender |
| [PI_31003](/schnittstellen/202610/pruefi/INVOIC/PI_31003) | Prüfi | INVOIC | transaktionsdaten › empfaenger |
| [PI_31004](/schnittstellen/202610/pruefi/INVOIC/PI_31004) | Prüfi | INVOIC | transaktionsdaten › absender |
| [PI_31004](/schnittstellen/202610/pruefi/INVOIC/PI_31004) | Prüfi | INVOIC | transaktionsdaten › empfaenger |
| [PI_31005](/schnittstellen/202610/pruefi/INVOIC/PI_31005) | Prüfi | INVOIC | transaktionsdaten › absender |
| [PI_31005](/schnittstellen/202610/pruefi/INVOIC/PI_31005) | Prüfi | INVOIC | transaktionsdaten › empfaenger |
| [PI_31006](/schnittstellen/202610/pruefi/INVOIC/PI_31006) | Prüfi | INVOIC | transaktionsdaten › absender |
| [PI_31006](/schnittstellen/202610/pruefi/INVOIC/PI_31006) | Prüfi | INVOIC | transaktionsdaten › empfaenger |
| [PI_31007](/schnittstellen/202610/pruefi/INVOIC/PI_31007) | Prüfi | INVOIC | transaktionsdaten › absender |
| [PI_31007](/schnittstellen/202610/pruefi/INVOIC/PI_31007) | Prüfi | INVOIC | transaktionsdaten › empfaenger |
| [PI_31008](/schnittstellen/202610/pruefi/INVOIC/PI_31008) | Prüfi | INVOIC | transaktionsdaten › absender |
| [PI_31008](/schnittstellen/202610/pruefi/INVOIC/PI_31008) | Prüfi | INVOIC | transaktionsdaten › empfaenger |
| [PI_31009](/schnittstellen/202610/pruefi/INVOIC/PI_31009) | Prüfi | INVOIC | transaktionsdaten › absender |
| [PI_31009](/schnittstellen/202610/pruefi/INVOIC/PI_31009) | Prüfi | INVOIC | transaktionsdaten › empfaenger |
| [PI_31010](/schnittstellen/202610/pruefi/INVOIC/PI_31010) | Prüfi | INVOIC | transaktionsdaten › absender |
| [PI_31010](/schnittstellen/202610/pruefi/INVOIC/PI_31010) | Prüfi | INVOIC | transaktionsdaten › empfaenger |
| [PI_31011](/schnittstellen/202610/pruefi/INVOIC/PI_31011) | Prüfi | INVOIC | transaktionsdaten › absender |
| [PI_31011](/schnittstellen/202610/pruefi/INVOIC/PI_31011) | Prüfi | INVOIC | transaktionsdaten › empfaenger |
| [PI_37000](/schnittstellen/202610/pruefi/PARTIN/PI_37000) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben |
| [PI_37000](/schnittstellen/202610/pruefi/PARTIN/PI_37000) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37001](/schnittstellen/202610/pruefi/PARTIN/PI_37001) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben |
| [PI_37001](/schnittstellen/202610/pruefi/PARTIN/PI_37001) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37002](/schnittstellen/202610/pruefi/PARTIN/PI_37002) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben |
| [PI_37002](/schnittstellen/202610/pruefi/PARTIN/PI_37002) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37008](/schnittstellen/202610/pruefi/PARTIN/PI_37008) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben |
| [PI_37008](/schnittstellen/202610/pruefi/PARTIN/PI_37008) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37009](/schnittstellen/202610/pruefi/PARTIN/PI_37009) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben |
| [PI_37009](/schnittstellen/202610/pruefi/PARTIN/PI_37009) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37010](/schnittstellen/202610/pruefi/PARTIN/PI_37010) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben |
| [PI_37010](/schnittstellen/202610/pruefi/PARTIN/PI_37010) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37012](/schnittstellen/202610/pruefi/PARTIN/PI_37012) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben |
| [PI_37012](/schnittstellen/202610/pruefi/PARTIN/PI_37012) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37013](/schnittstellen/202610/pruefi/PARTIN/PI_37013) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben |
| [PI_37013](/schnittstellen/202610/pruefi/PARTIN/PI_37013) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37014](/schnittstellen/202610/pruefi/PARTIN/PI_37014) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben |
| [PI_37014](/schnittstellen/202610/pruefi/PARTIN/PI_37014) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |

### name2

18 Verwendung(en) in den Nachrichtentypen PARTIN.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_37000](/schnittstellen/202610/pruefi/PARTIN/PI_37000) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben |
| [PI_37000](/schnittstellen/202610/pruefi/PARTIN/PI_37000) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37001](/schnittstellen/202610/pruefi/PARTIN/PI_37001) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben |
| [PI_37001](/schnittstellen/202610/pruefi/PARTIN/PI_37001) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37002](/schnittstellen/202610/pruefi/PARTIN/PI_37002) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben |
| [PI_37002](/schnittstellen/202610/pruefi/PARTIN/PI_37002) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37008](/schnittstellen/202610/pruefi/PARTIN/PI_37008) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben |
| [PI_37008](/schnittstellen/202610/pruefi/PARTIN/PI_37008) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37009](/schnittstellen/202610/pruefi/PARTIN/PI_37009) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben |
| [PI_37009](/schnittstellen/202610/pruefi/PARTIN/PI_37009) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37010](/schnittstellen/202610/pruefi/PARTIN/PI_37010) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben |
| [PI_37010](/schnittstellen/202610/pruefi/PARTIN/PI_37010) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37012](/schnittstellen/202610/pruefi/PARTIN/PI_37012) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben |
| [PI_37012](/schnittstellen/202610/pruefi/PARTIN/PI_37012) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37013](/schnittstellen/202610/pruefi/PARTIN/PI_37013) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben |
| [PI_37013](/schnittstellen/202610/pruefi/PARTIN/PI_37013) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37014](/schnittstellen/202610/pruefi/PARTIN/PI_37014) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben |
| [PI_37014](/schnittstellen/202610/pruefi/PARTIN/PI_37014) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |

### name3

18 Verwendung(en) in den Nachrichtentypen PARTIN.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_37000](/schnittstellen/202610/pruefi/PARTIN/PI_37000) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben |
| [PI_37000](/schnittstellen/202610/pruefi/PARTIN/PI_37000) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37001](/schnittstellen/202610/pruefi/PARTIN/PI_37001) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben |
| [PI_37001](/schnittstellen/202610/pruefi/PARTIN/PI_37001) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37002](/schnittstellen/202610/pruefi/PARTIN/PI_37002) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben |
| [PI_37002](/schnittstellen/202610/pruefi/PARTIN/PI_37002) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37008](/schnittstellen/202610/pruefi/PARTIN/PI_37008) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben |
| [PI_37008](/schnittstellen/202610/pruefi/PARTIN/PI_37008) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37009](/schnittstellen/202610/pruefi/PARTIN/PI_37009) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben |
| [PI_37009](/schnittstellen/202610/pruefi/PARTIN/PI_37009) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37010](/schnittstellen/202610/pruefi/PARTIN/PI_37010) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben |
| [PI_37010](/schnittstellen/202610/pruefi/PARTIN/PI_37010) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37012](/schnittstellen/202610/pruefi/PARTIN/PI_37012) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben |
| [PI_37012](/schnittstellen/202610/pruefi/PARTIN/PI_37012) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37013](/schnittstellen/202610/pruefi/PARTIN/PI_37013) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben |
| [PI_37013](/schnittstellen/202610/pruefi/PARTIN/PI_37013) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37014](/schnittstellen/202610/pruefi/PARTIN/PI_37014) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben |
| [PI_37014](/schnittstellen/202610/pruefi/PARTIN/PI_37014) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |

### name4

18 Verwendung(en) in den Nachrichtentypen PARTIN.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_37000](/schnittstellen/202610/pruefi/PARTIN/PI_37000) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben |
| [PI_37000](/schnittstellen/202610/pruefi/PARTIN/PI_37000) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37001](/schnittstellen/202610/pruefi/PARTIN/PI_37001) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben |
| [PI_37001](/schnittstellen/202610/pruefi/PARTIN/PI_37001) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37002](/schnittstellen/202610/pruefi/PARTIN/PI_37002) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben |
| [PI_37002](/schnittstellen/202610/pruefi/PARTIN/PI_37002) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37008](/schnittstellen/202610/pruefi/PARTIN/PI_37008) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben |
| [PI_37008](/schnittstellen/202610/pruefi/PARTIN/PI_37008) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37009](/schnittstellen/202610/pruefi/PARTIN/PI_37009) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben |
| [PI_37009](/schnittstellen/202610/pruefi/PARTIN/PI_37009) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37010](/schnittstellen/202610/pruefi/PARTIN/PI_37010) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben |
| [PI_37010](/schnittstellen/202610/pruefi/PARTIN/PI_37010) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37012](/schnittstellen/202610/pruefi/PARTIN/PI_37012) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben |
| [PI_37012](/schnittstellen/202610/pruefi/PARTIN/PI_37012) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37013](/schnittstellen/202610/pruefi/PARTIN/PI_37013) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben |
| [PI_37013](/schnittstellen/202610/pruefi/PARTIN/PI_37013) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37014](/schnittstellen/202610/pruefi/PARTIN/PI_37014) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben |
| [PI_37014](/schnittstellen/202610/pruefi/PARTIN/PI_37014) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |

### gewerbekennzeichnung

9 Verwendung(en) in den Nachrichtentypen PARTIN.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_37000](/schnittstellen/202610/pruefi/PARTIN/PI_37000) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37001](/schnittstellen/202610/pruefi/PARTIN/PI_37001) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37002](/schnittstellen/202610/pruefi/PARTIN/PI_37002) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37008](/schnittstellen/202610/pruefi/PARTIN/PI_37008) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37009](/schnittstellen/202610/pruefi/PARTIN/PI_37009) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37010](/schnittstellen/202610/pruefi/PARTIN/PI_37010) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37012](/schnittstellen/202610/pruefi/PARTIN/PI_37012) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37013](/schnittstellen/202610/pruefi/PARTIN/PI_37013) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37014](/schnittstellen/202610/pruefi/PARTIN/PI_37014) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |

### marktrolle

166 Verwendung(en) in den Nachrichtentypen ORDERS, PARTIN, UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [[LF] START_ANFRAGE_STAMMDATENAENDERUNG GAS](/schnittstellen/202610/trigger/events/LF-START_ANFRAGE_STAMMDATENAENDERUNG-GAS) | Event | — | transaktionsdaten › empfaenger |
| [[LF] START_BESTELLUNG_SDAE](/schnittstellen/202610/trigger/events/LF-START_BESTELLUNG_SDAE) | Event | — | transaktionsdaten › empfaenger |
| [[LF] START_KUENDIGUNG](/schnittstellen/202610/trigger/events/LF-START_KUENDIGUNG) | Event | — | transaktionsdaten › empfaenger |
| [[LF] START_LIEFERBEGINN](/schnittstellen/202610/trigger/events/LF-START_LIEFERBEGINN) | Event | — | transaktionsdaten › empfaenger |
| [[LF] START_LIEFERENDE](/schnittstellen/202610/trigger/events/LF-START_LIEFERENDE) | Event | — | transaktionsdaten › empfaenger |
| [[LF] START_MALOIDENT](/schnittstellen/202610/trigger/events/LF-START_MALOIDENT) | Event | — | transaktionsdaten › empfaenger |
| [[LF] START_PARTIN](/schnittstellen/202610/trigger/events/LF-START_PARTIN) | Event | — | transaktionsdaten › empfaenger |
| [[LF] START_SPERRAUFTRAG](/schnittstellen/202610/trigger/events/LF-START_SPERRAUFTRAG) | Event | — | transaktionsdaten › empfaenger |
| [[LF] START_STORNO_SE_AUFTRAG](/schnittstellen/202610/trigger/events/LF-START_STORNO_SE_AUFTRAG) | Event | — | transaktionsdaten › empfaenger |
| [[LF] START_VERSAND_ANTWORT_NNA](/schnittstellen/202610/trigger/events/LF-START_VERSAND_ANTWORT_NNA) | Event | — | transaktionsdaten › empfaenger |
| [[LF] START_VERSAND_SDAE](/schnittstellen/202610/trigger/events/LF-START_VERSAND_SDAE) | Event | — | transaktionsdaten › empfaenger |
| [[MSB] START_ANGEBOT_GERAETEUEBERNAHME](/schnittstellen/202610/trigger/events/MSB-START_ANGEBOT_GERAETEUEBERNAHME) | Event | — | transaktionsdaten › absender |
| [[MSB] START_ANGEBOT_GERAETEUEBERNAHME](/schnittstellen/202610/trigger/events/MSB-START_ANGEBOT_GERAETEUEBERNAHME) | Event | — | transaktionsdaten › empfaenger |
| [[MSB] START_ANTWORT_GERAETEWECHSEL](/schnittstellen/202610/trigger/events/MSB-START_ANTWORT_GERAETEWECHSEL) | Event | — | transaktionsdaten › absender |
| [[MSB] START_ANTWORT_GERAETEWECHSEL](/schnittstellen/202610/trigger/events/MSB-START_ANTWORT_GERAETEWECHSEL) | Event | — | transaktionsdaten › empfaenger |
| [[MSB] START_BEGINN_MSB](/schnittstellen/202610/trigger/events/MSB-START_BEGINN_MSB) | Event | — | transaktionsdaten › absender |
| [[MSB] START_BEGINN_MSB](/schnittstellen/202610/trigger/events/MSB-START_BEGINN_MSB) | Event | — | transaktionsdaten › empfaenger |
| [[MSB] START_BESTELLUNG_GERAETEUEBERNAHME](/schnittstellen/202610/trigger/events/MSB-START_BESTELLUNG_GERAETEUEBERNAHME) | Event | — | transaktionsdaten › absender |
| [[MSB] START_BESTELLUNG_GERAETEUEBERNAHME](/schnittstellen/202610/trigger/events/MSB-START_BESTELLUNG_GERAETEUEBERNAHME) | Event | — | transaktionsdaten › empfaenger |
| [[MSB] START_BESTELLUNG_SDAE GAS](/schnittstellen/202610/trigger/events/MSB-START_BESTELLUNG_SDAE-GAS) | Event | — | transaktionsdaten › absender |
| [[MSB] START_BESTELLUNG_SDAE GAS](/schnittstellen/202610/trigger/events/MSB-START_BESTELLUNG_SDAE-GAS) | Event | — | transaktionsdaten › empfaenger |
| [[MSB] START_GERAETEUEBERNAHME](/schnittstellen/202610/trigger/events/MSB-START_GERAETEUEBERNAHME) | Event | — | transaktionsdaten › absender |
| [[MSB] START_GERAETEUEBERNAHME](/schnittstellen/202610/trigger/events/MSB-START_GERAETEUEBERNAHME) | Event | — | transaktionsdaten › empfaenger |
| [[MSB] START_GERAETEWECHSEL](/schnittstellen/202610/trigger/events/MSB-START_GERAETEWECHSEL) | Event | — | transaktionsdaten › absender |
| [[MSB] START_GERAETEWECHSEL](/schnittstellen/202610/trigger/events/MSB-START_GERAETEWECHSEL) | Event | — | transaktionsdaten › empfaenger |
| [[MSB] START_VERSAND_PREISBLATT_IMS](/schnittstellen/202610/trigger/events/MSB-START_VERSAND_PREISBLATT_IMS) | Event | — | transaktionsdaten › absender |
| [[MSB] START_VERSAND_PREISBLATT_IMS](/schnittstellen/202610/trigger/events/MSB-START_VERSAND_PREISBLATT_IMS) | Event | — | transaktionsdaten › empfaenger |
| [[MSB] START_VERSAND_SDAE](/schnittstellen/202610/trigger/events/MSB-START_VERSAND_SDAE) | Event | — | transaktionsdaten › absender |
| [[MSB] START_VERSAND_SDAE](/schnittstellen/202610/trigger/events/MSB-START_VERSAND_SDAE) | Event | — | transaktionsdaten › empfaenger |
| [[NB] START_ABR_BK](/schnittstellen/202610/trigger/events/NB-START_ABR_BK) | Event | — | transaktionsdaten › empfaenger |
| [[NB] START_ABR_NN](/schnittstellen/202610/trigger/events/NB-START_ABR_NN) | Event | — | transaktionsdaten › empfaenger |
| [[NB] START_BESTELLUNG_SDAE](/schnittstellen/202610/trigger/events/NB-START_BESTELLUNG_SDAE) | Event | — | transaktionsdaten › empfaenger |
| [[NB] START_ENDE_ZUORDNUNG](/schnittstellen/202610/trigger/events/NB-START_ENDE_ZUORDNUNG) | Event | — | transaktionsdaten › empfaenger |
| [[NB] START_VERSAND_SDAE](/schnittstellen/202610/trigger/events/NB-START_VERSAND_SDAE) | Event | — | transaktionsdaten › empfaenger |
| [PI_17134](/schnittstellen/202610/pruefi/ORDERS/PI_17134) | Prüfi | ORDERS | stammdaten › MARKTLOKATION › marktrollen |
| [PI_17134](/schnittstellen/202610/pruefi/ORDERS/PI_17134) | Prüfi | ORDERS | stammdaten › TRANCHE › marktrollen |
| [PI_17135](/schnittstellen/202610/pruefi/ORDERS/PI_17135) | Prüfi | ORDERS | stammdaten › MARKTLOKATION › marktrollen |
| [PI_17135](/schnittstellen/202610/pruefi/ORDERS/PI_17135) | Prüfi | ORDERS | stammdaten › TRANCHE › marktrollen |
| [PI_37000](/schnittstellen/202610/pruefi/PARTIN/PI_37000) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37001](/schnittstellen/202610/pruefi/PARTIN/PI_37001) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37002](/schnittstellen/202610/pruefi/PARTIN/PI_37002) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37008](/schnittstellen/202610/pruefi/PARTIN/PI_37008) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37009](/schnittstellen/202610/pruefi/PARTIN/PI_37009) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37010](/schnittstellen/202610/pruefi/PARTIN/PI_37010) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37012](/schnittstellen/202610/pruefi/PARTIN/PI_37012) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37013](/schnittstellen/202610/pruefi/PARTIN/PI_37013) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37014](/schnittstellen/202610/pruefi/PARTIN/PI_37014) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_44002](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › marktrollen |
| [PI_44013](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › marktrollen |
| [PI_44014](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › marktrollen |
| [PI_44035](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44035) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › marktrollen |
| [PI_44043](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44043) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › marktrollen |
| [PI_44060](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44060) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › marktrollen |
| [PI_44112](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44112) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › marktrollen |
| [PI_44113](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44113) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › marktrollen |
| [PI_44139](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44139) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › marktrollen |
| [PI_44140](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44140) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › marktrollen |
| [PI_44142](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44142) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › marktrollen |
| [PI_44168](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › marktrollen |
| [PI_55002](/schnittstellen/202610/pruefi/UTILMD/PI_55002) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55002](/schnittstellen/202610/pruefi/UTILMD/PI_55002) | Prüfi | UTILMD | stammdaten › MESSLOKATION › marktrollen |
| [PI_55002](/schnittstellen/202610/pruefi/UTILMD/PI_55002) | Prüfi | UTILMD | stammdaten › NETZLOKATION › marktrollen |
| [PI_55002](/schnittstellen/202610/pruefi/UTILMD/PI_55002) | Prüfi | UTILMD | stammdaten › STEUERBARE_RESSOURCE › marktrollen |
| [PI_55013](/schnittstellen/202610/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55013](/schnittstellen/202610/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › MESSLOKATION › marktrollen |
| [PI_55013](/schnittstellen/202610/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › NETZLOKATION › marktrollen |
| [PI_55013](/schnittstellen/202610/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › STEUERBARE_RESSOURCE › marktrollen |
| [PI_55035](/schnittstellen/202610/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55035](/schnittstellen/202610/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › MESSLOKATION › marktrollen |
| [PI_55035](/schnittstellen/202610/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › NETZLOKATION › marktrollen |
| [PI_55035](/schnittstellen/202610/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › STEUERBARE_RESSOURCE › marktrollen |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › MESSLOKATION › marktrollen |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › NETZLOKATION › auftraggebenderMarktpartner |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › NETZLOKATION › marktrollen |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › STEUERBARE_RESSOURCE › auftraggebenderMarktpartner |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › STEUERBARE_RESSOURCE › marktrollen |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › TRANCHE › marktrollen |
| [PI_55060](/schnittstellen/202610/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55060](/schnittstellen/202610/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › MESSLOKATION › marktrollen |
| [PI_55060](/schnittstellen/202610/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › NETZLOKATION › marktrollen |
| [PI_55060](/schnittstellen/202610/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › STEUERBARE_RESSOURCE › marktrollen |
| [PI_55060](/schnittstellen/202610/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › TRANCHE › marktrollen |
| [PI_55074](/schnittstellen/202610/pruefi/UTILMD/PI_55074) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55074](/schnittstellen/202610/pruefi/UTILMD/PI_55074) | Prüfi | UTILMD | stammdaten › TRANCHE › marktrollen |
| [PI_55075](/schnittstellen/202610/pruefi/UTILMD/PI_55075) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55075](/schnittstellen/202610/pruefi/UTILMD/PI_55075) | Prüfi | UTILMD | stammdaten › TRANCHE › marktrollen |
| [PI_55078](/schnittstellen/202610/pruefi/UTILMD/PI_55078) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55078](/schnittstellen/202610/pruefi/UTILMD/PI_55078) | Prüfi | UTILMD | stammdaten › MESSLOKATION › marktrollen |
| [PI_55078](/schnittstellen/202610/pruefi/UTILMD/PI_55078) | Prüfi | UTILMD | stammdaten › NETZLOKATION › marktrollen |
| [PI_55078](/schnittstellen/202610/pruefi/UTILMD/PI_55078) | Prüfi | UTILMD | stammdaten › STEUERBARE_RESSOURCE › marktrollen |
| [PI_55095](/schnittstellen/202610/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55095](/schnittstellen/202610/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | stammdaten › MESSLOKATION › marktrollen |
| [PI_55095](/schnittstellen/202610/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | stammdaten › NETZLOKATION › marktrollen |
| [PI_55095](/schnittstellen/202610/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | stammdaten › STEUERBARE_RESSOURCE › marktrollen |
| [PI_55126](/schnittstellen/202610/pruefi/UTILMD/PI_55126) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55156](/schnittstellen/202610/pruefi/UTILMD/PI_55156) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › MESSLOKATION › marktrollen |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › NETZLOKATION › auftraggebenderMarktpartner |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › NETZLOKATION › marktrollen |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › STEUERBARE_RESSOURCE › auftraggebenderMarktpartner |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › STEUERBARE_RESSOURCE › marktrollen |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › TRANCHE › marktrollen |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › MESSLOKATION › marktrollen |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › NETZLOKATION › auftraggebenderMarktpartner |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › NETZLOKATION › marktrollen |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › STEUERBARE_RESSOURCE › auftraggebenderMarktpartner |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › STEUERBARE_RESSOURCE › marktrollen |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › TRANCHE › marktrollen |
| [PI_55194](/schnittstellen/202610/pruefi/UTILMD/PI_55194) | Prüfi | UTILMD | stammdaten › MESSLOKATION › marktrollen |
| [PI_55602](/schnittstellen/202610/pruefi/UTILMD/PI_55602) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55602](/schnittstellen/202610/pruefi/UTILMD/PI_55602) | Prüfi | UTILMD | stammdaten › MESSLOKATION › marktrollen |
| [PI_55602](/schnittstellen/202610/pruefi/UTILMD/PI_55602) | Prüfi | UTILMD | stammdaten › NETZLOKATION › marktrollen |
| [PI_55602](/schnittstellen/202610/pruefi/UTILMD/PI_55602) | Prüfi | UTILMD | stammdaten › STEUERBARE_RESSOURCE › marktrollen |
| [PI_55603](/schnittstellen/202610/pruefi/UTILMD/PI_55603) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55603](/schnittstellen/202610/pruefi/UTILMD/PI_55603) | Prüfi | UTILMD | stammdaten › MESSLOKATION › marktrollen |
| [PI_55603](/schnittstellen/202610/pruefi/UTILMD/PI_55603) | Prüfi | UTILMD | stammdaten › NETZLOKATION › marktrollen |
| [PI_55603](/schnittstellen/202610/pruefi/UTILMD/PI_55603) | Prüfi | UTILMD | stammdaten › STEUERBARE_RESSOURCE › marktrollen |
| [PI_55607](/schnittstellen/202610/pruefi/UTILMD/PI_55607) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55607](/schnittstellen/202610/pruefi/UTILMD/PI_55607) | Prüfi | UTILMD | stammdaten › MESSLOKATION › marktrollen |
| [PI_55607](/schnittstellen/202610/pruefi/UTILMD/PI_55607) | Prüfi | UTILMD | stammdaten › NETZLOKATION › marktrollen |
| [PI_55607](/schnittstellen/202610/pruefi/UTILMD/PI_55607) | Prüfi | UTILMD | stammdaten › STEUERBARE_RESSOURCE › marktrollen |
| [PI_55613](/schnittstellen/202610/pruefi/UTILMD/PI_55613) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55614](/schnittstellen/202610/pruefi/UTILMD/PI_55614) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55615](/schnittstellen/202610/pruefi/UTILMD/PI_55615) | Prüfi | UTILMD | stammdaten › NETZLOKATION › marktrollen |
| [PI_55616](/schnittstellen/202610/pruefi/UTILMD/PI_55616) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55618](/schnittstellen/202610/pruefi/UTILMD/PI_55618) | Prüfi | UTILMD | stammdaten › STEUERBARE_RESSOURCE › marktrollen |
| [PI_55620](/schnittstellen/202610/pruefi/UTILMD/PI_55620) | Prüfi | UTILMD | stammdaten › MESSLOKATION › marktrollen |
| [PI_55621](/schnittstellen/202610/pruefi/UTILMD/PI_55621) | Prüfi | UTILMD | stammdaten › NETZLOKATION › marktrollen |
| [PI_55622](/schnittstellen/202610/pruefi/UTILMD/PI_55622) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55624](/schnittstellen/202610/pruefi/UTILMD/PI_55624) | Prüfi | UTILMD | stammdaten › STEUERBARE_RESSOURCE › marktrollen |
| [PI_55626](/schnittstellen/202610/pruefi/UTILMD/PI_55626) | Prüfi | UTILMD | stammdaten › MESSLOKATION › marktrollen |
| [PI_55627](/schnittstellen/202610/pruefi/UTILMD/PI_55627) | Prüfi | UTILMD | stammdaten › NETZLOKATION › marktrollen |
| [PI_55628](/schnittstellen/202610/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55630](/schnittstellen/202610/pruefi/UTILMD/PI_55630) | Prüfi | UTILMD | stammdaten › STEUERBARE_RESSOURCE › marktrollen |
| [PI_55632](/schnittstellen/202610/pruefi/UTILMD/PI_55632) | Prüfi | UTILMD | stammdaten › MESSLOKATION › marktrollen |
| [PI_55633](/schnittstellen/202610/pruefi/UTILMD/PI_55633) | Prüfi | UTILMD | stammdaten › NETZLOKATION › marktrollen |
| [PI_55634](/schnittstellen/202610/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55636](/schnittstellen/202610/pruefi/UTILMD/PI_55636) | Prüfi | UTILMD | stammdaten › STEUERBARE_RESSOURCE › marktrollen |
| [PI_55638](/schnittstellen/202610/pruefi/UTILMD/PI_55638) | Prüfi | UTILMD | stammdaten › MESSLOKATION › marktrollen |
| [PI_55639](/schnittstellen/202610/pruefi/UTILMD/PI_55639) | Prüfi | UTILMD | stammdaten › NETZLOKATION › auftraggebenderMarktpartner |
| [PI_55641](/schnittstellen/202610/pruefi/UTILMD/PI_55641) | Prüfi | UTILMD | stammdaten › STEUERBARE_RESSOURCE › auftraggebenderMarktpartner |
| [PI_55644](/schnittstellen/202610/pruefi/UTILMD/PI_55644) | Prüfi | UTILMD | stammdaten › NETZLOKATION › auftraggebenderMarktpartner |
| [PI_55646](/schnittstellen/202610/pruefi/UTILMD/PI_55646) | Prüfi | UTILMD | stammdaten › STEUERBARE_RESSOURCE › auftraggebenderMarktpartner |
| [PI_55649](/schnittstellen/202610/pruefi/UTILMD/PI_55649) | Prüfi | UTILMD | stammdaten › NETZLOKATION › auftraggebenderMarktpartner |
| [PI_55651](/schnittstellen/202610/pruefi/UTILMD/PI_55651) | Prüfi | UTILMD | stammdaten › STEUERBARE_RESSOURCE › auftraggebenderMarktpartner |
| [PI_55654](/schnittstellen/202610/pruefi/UTILMD/PI_55654) | Prüfi | UTILMD | stammdaten › NETZLOKATION › auftraggebenderMarktpartner |
| [PI_55656](/schnittstellen/202610/pruefi/UTILMD/PI_55656) | Prüfi | UTILMD | stammdaten › STEUERBARE_RESSOURCE › auftraggebenderMarktpartner |
| [PI_55659](/schnittstellen/202610/pruefi/UTILMD/PI_55659) | Prüfi | UTILMD | stammdaten › NETZLOKATION › auftraggebenderMarktpartner |
| [PI_55661](/schnittstellen/202610/pruefi/UTILMD/PI_55661) | Prüfi | UTILMD | stammdaten › STEUERBARE_RESSOURCE › auftraggebenderMarktpartner |
| [PI_55664](/schnittstellen/202610/pruefi/UTILMD/PI_55664) | Prüfi | UTILMD | stammdaten › NETZLOKATION › auftraggebenderMarktpartner |
| [PI_55666](/schnittstellen/202610/pruefi/UTILMD/PI_55666) | Prüfi | UTILMD | stammdaten › STEUERBARE_RESSOURCE › auftraggebenderMarktpartner |
| [PI_55670](/schnittstellen/202610/pruefi/UTILMD/PI_55670) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55670](/schnittstellen/202610/pruefi/UTILMD/PI_55670) | Prüfi | UTILMD | stammdaten › TRANCHE › marktrollen |
| [PI_55672](/schnittstellen/202610/pruefi/UTILMD/PI_55672) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55673](/schnittstellen/202610/pruefi/UTILMD/PI_55673) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55674](/schnittstellen/202610/pruefi/UTILMD/PI_55674) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55674](/schnittstellen/202610/pruefi/UTILMD/PI_55674) | Prüfi | UTILMD | stammdaten › TRANCHE › marktrollen |
| [PI_55688](/schnittstellen/202610/pruefi/UTILMD/PI_55688) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55690](/schnittstellen/202610/pruefi/UTILMD/PI_55690) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55690](/schnittstellen/202610/pruefi/UTILMD/PI_55690) | Prüfi | UTILMD | stammdaten › MESSLOKATION › marktrollen |
| [PI_55690](/schnittstellen/202610/pruefi/UTILMD/PI_55690) | Prüfi | UTILMD | stammdaten › NETZLOKATION › marktrollen |
| [PI_55690](/schnittstellen/202610/pruefi/UTILMD/PI_55690) | Prüfi | UTILMD | stammdaten › STEUERBARE_RESSOURCE › marktrollen |
| [PI_55690](/schnittstellen/202610/pruefi/UTILMD/PI_55690) | Prüfi | UTILMD | stammdaten › TRANCHE › marktrollen |

### rollencodenummer

1084 Verwendung(en) in den Nachrichtentypen APERAK, COMDIS, IFTSTA, INSRPT, INVOIC, MSCONS, ORDCHG, ORDERS, ORDRSP, PARTIN, PRICAT, QUOTES, REMADV, REQOTE, UTILMD, UTILMD_GAS, UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [[LF] START_ABO_PROFILE](/schnittstellen/202610/trigger/events/LF-START_ABO_PROFILE) | Event | — | transaktionsdaten › absender |
| [[LF] START_ABO_PROFILE](/schnittstellen/202610/trigger/events/LF-START_ABO_PROFILE) | Event | — | transaktionsdaten › empfaenger |
| [[LF] START_ABR_NN](/schnittstellen/202610/trigger/events/LF-START_ABR_NN) | Event | — | transaktionsdaten › absender |
| [[LF] START_ABR_NN](/schnittstellen/202610/trigger/events/LF-START_ABR_NN) | Event | — | transaktionsdaten › empfaenger |
| [[LF] START_ANFORDERUNG_VON_WERTEN](/schnittstellen/202610/trigger/events/LF-START_ANFORDERUNG_VON_WERTEN) | Event | — | transaktionsdaten › absender |
| [[LF] START_ANFORDERUNG_VON_WERTEN](/schnittstellen/202610/trigger/events/LF-START_ANFORDERUNG_VON_WERTEN) | Event | — | transaktionsdaten › empfaenger |
| [[LF] START_ANFRAGE_KONFIGURATION](/schnittstellen/202610/trigger/events/LF-START_ANFRAGE_KONFIGURATION) | Event | — | transaktionsdaten › absender |
| [[LF] START_ANFRAGE_KONFIGURATION](/schnittstellen/202610/trigger/events/LF-START_ANFRAGE_KONFIGURATION) | Event | — | transaktionsdaten › empfaenger |
| [[LF] START_ANFRAGE_MESSWERTE](/schnittstellen/202610/trigger/events/LF-START_ANFRAGE_MESSWERTE) | Event | — | transaktionsdaten › absender |
| [[LF] START_ANFRAGE_MESSWERTE](/schnittstellen/202610/trigger/events/LF-START_ANFRAGE_MESSWERTE) | Event | — | transaktionsdaten › empfaenger |
| [[LF] START_ANFRAGE_SPERRUNG](/schnittstellen/202610/trigger/events/LF-START_ANFRAGE_SPERRUNG) | Event | — | transaktionsdaten › absender |
| [[LF] START_ANFRAGE_SPERRUNG](/schnittstellen/202610/trigger/events/LF-START_ANFRAGE_SPERRUNG) | Event | — | transaktionsdaten › empfaenger |
| [[LF] START_ANFRAGE_STAMMDATENAENDERUNG GAS](/schnittstellen/202610/trigger/events/LF-START_ANFRAGE_STAMMDATENAENDERUNG-GAS) | Event | — | transaktionsdaten › absender |
| [[LF] START_ANFRAGE_STAMMDATENAENDERUNG GAS](/schnittstellen/202610/trigger/events/LF-START_ANFRAGE_STAMMDATENAENDERUNG-GAS) | Event | — | transaktionsdaten › empfaenger |
| [[LF] START_ANFRAGE_STAMMDATEN_MALO](/schnittstellen/202610/trigger/events/LF-START_ANFRAGE_STAMMDATEN_MALO) | Event | — | transaktionsdaten › absender |
| [[LF] START_ANFRAGE_STAMMDATEN_MALO](/schnittstellen/202610/trigger/events/LF-START_ANFRAGE_STAMMDATEN_MALO) | Event | — | transaktionsdaten › empfaenger |
| [[LF] START_ANFRAGE_STAMMDATEN_TRANCHE](/schnittstellen/202610/trigger/events/LF-START_ANFRAGE_STAMMDATEN_TRANCHE) | Event | — | transaktionsdaten › absender |
| [[LF] START_ANFRAGE_STAMMDATEN_TRANCHE](/schnittstellen/202610/trigger/events/LF-START_ANFRAGE_STAMMDATEN_TRANCHE) | Event | — | transaktionsdaten › empfaenger |
| [[LF] START_ANF_BRENNW_ZUSTANDSZAHL](/schnittstellen/202610/trigger/events/LF-START_ANF_BRENNW_ZUSTANDSZAHL) | Event | — | transaktionsdaten › absender |
| [[LF] START_ANF_BRENNW_ZUSTANDSZAHL](/schnittstellen/202610/trigger/events/LF-START_ANF_BRENNW_ZUSTANDSZAHL) | Event | — | transaktionsdaten › empfaenger |
| [[LF] START_BESTELLUNG_ABRECHNUNGSDATEN](/schnittstellen/202610/trigger/events/LF-START_BESTELLUNG_ABRECHNUNGSDATEN) | Event | — | transaktionsdaten › absender |
| [[LF] START_BESTELLUNG_ABRECHNUNGSDATEN](/schnittstellen/202610/trigger/events/LF-START_BESTELLUNG_ABRECHNUNGSDATEN) | Event | — | transaktionsdaten › empfaenger |
| [[LF] START_BESTELLUNG_ANGEBOT_KONFIGURATION](/schnittstellen/202610/trigger/events/LF-START_BESTELLUNG_ANGEBOT_KONFIGURATION) | Event | — | transaktionsdaten › absender |
| [[LF] START_BESTELLUNG_ANGEBOT_KONFIGURATION](/schnittstellen/202610/trigger/events/LF-START_BESTELLUNG_ANGEBOT_KONFIGURATION) | Event | — | transaktionsdaten › empfaenger |
| [[LF] START_BESTELLUNG_KONFIGURATION](/schnittstellen/202610/trigger/events/LF-START_BESTELLUNG_KONFIGURATION) | Event | — | transaktionsdaten › absender |
| [[LF] START_BESTELLUNG_KONFIGURATION](/schnittstellen/202610/trigger/events/LF-START_BESTELLUNG_KONFIGURATION) | Event | — | transaktionsdaten › empfaenger |
| [[LF] START_BESTELLUNG_SDAE](/schnittstellen/202610/trigger/events/LF-START_BESTELLUNG_SDAE) | Event | — | transaktionsdaten › absender |
| [[LF] START_BESTELLUNG_SDAE](/schnittstellen/202610/trigger/events/LF-START_BESTELLUNG_SDAE) | Event | — | transaktionsdaten › empfaenger |
| [[LF] START_BESTELLUNG_ZAEHLZEITDEFINITION](/schnittstellen/202610/trigger/events/LF-START_BESTELLUNG_ZAEHLZEITDEFINITION) | Event | — | transaktionsdaten › absender |
| [[LF] START_BESTELLUNG_ZAEHLZEITDEFINITION](/schnittstellen/202610/trigger/events/LF-START_BESTELLUNG_ZAEHLZEITDEFINITION) | Event | — | transaktionsdaten › empfaenger |
| [[LF] START_BEST_AEND_TK](/schnittstellen/202610/trigger/events/LF-START_BEST_AEND_TK) | Event | — | transaktionsdaten › absender |
| [[LF] START_BEST_AEND_TK](/schnittstellen/202610/trigger/events/LF-START_BEST_AEND_TK) | Event | — | transaktionsdaten › empfaenger |
| [[LF] START_ENTSPERRAUFTRAG](/schnittstellen/202610/trigger/events/LF-START_ENTSPERRAUFTRAG) | Event | — | transaktionsdaten › absender |
| [[LF] START_ENTSPERRAUFTRAG](/schnittstellen/202610/trigger/events/LF-START_ENTSPERRAUFTRAG) | Event | — | transaktionsdaten › empfaenger |
| [[LF] START_ERHEBUNG_MESSWERTE](/schnittstellen/202610/trigger/events/LF-START_ERHEBUNG_MESSWERTE) | Event | — | transaktionsdaten › absender |
| [[LF] START_ERHEBUNG_MESSWERTE](/schnittstellen/202610/trigger/events/LF-START_ERHEBUNG_MESSWERTE) | Event | — | transaktionsdaten › empfaenger |
| [[LF] START_GESCHAEFTSDATENANFRAGE](/schnittstellen/202610/trigger/events/LF-START_GESCHAEFTSDATENANFRAGE) | Event | — | transaktionsdaten › absender |
| [[LF] START_GESCHAEFTSDATENANFRAGE](/schnittstellen/202610/trigger/events/LF-START_GESCHAEFTSDATENANFRAGE) | Event | — | transaktionsdaten › empfaenger |
| [[LF] START_KUENDIGUNG](/schnittstellen/202610/trigger/events/LF-START_KUENDIGUNG) | Event | — | transaktionsdaten › absender |
| [[LF] START_KUENDIGUNG](/schnittstellen/202610/trigger/events/LF-START_KUENDIGUNG) | Event | — | transaktionsdaten › empfaenger |
| [[LF] START_LIEFERBEGINN](/schnittstellen/202610/trigger/events/LF-START_LIEFERBEGINN) | Event | — | transaktionsdaten › absender |
| [[LF] START_LIEFERBEGINN](/schnittstellen/202610/trigger/events/LF-START_LIEFERBEGINN) | Event | — | transaktionsdaten › empfaenger |
| [[LF] START_LIEFERENDE](/schnittstellen/202610/trigger/events/LF-START_LIEFERENDE) | Event | — | transaktionsdaten › absender |
| [[LF] START_LIEFERENDE](/schnittstellen/202610/trigger/events/LF-START_LIEFERENDE) | Event | — | transaktionsdaten › empfaenger |
| [[LF] START_MALOIDENT](/schnittstellen/202610/trigger/events/LF-START_MALOIDENT) | Event | — | transaktionsdaten › absender |
| [[LF] START_MALOIDENT](/schnittstellen/202610/trigger/events/LF-START_MALOIDENT) | Event | — | transaktionsdaten › empfaenger |
| [[LF] START_PARTIN](/schnittstellen/202610/trigger/events/LF-START_PARTIN) | Event | — | transaktionsdaten › absender |
| [[LF] START_PARTIN](/schnittstellen/202610/trigger/events/LF-START_PARTIN) | Event | — | transaktionsdaten › empfaenger |
| [[LF] START_REKLAMATION_DEFINITIONEN](/schnittstellen/202610/trigger/events/LF-START_REKLAMATION_DEFINITIONEN) | Event | — | transaktionsdaten › absender |
| [[LF] START_REKLAMATION_DEFINITIONEN](/schnittstellen/202610/trigger/events/LF-START_REKLAMATION_DEFINITIONEN) | Event | — | transaktionsdaten › empfaenger |
| [[LF] START_REKLAMATION_VON_WERTEN](/schnittstellen/202610/trigger/events/LF-START_REKLAMATION_VON_WERTEN) | Event | — | transaktionsdaten › absender |
| [[LF] START_REKLAMATION_VON_WERTEN](/schnittstellen/202610/trigger/events/LF-START_REKLAMATION_VON_WERTEN) | Event | — | transaktionsdaten › empfaenger |
| [[LF] START_SPERRAUFTRAG](/schnittstellen/202610/trigger/events/LF-START_SPERRAUFTRAG) | Event | — | transaktionsdaten › absender |
| [[LF] START_SPERRAUFTRAG](/schnittstellen/202610/trigger/events/LF-START_SPERRAUFTRAG) | Event | — | transaktionsdaten › empfaenger |
| [[LF] START_STORNO_AUFTRAG](/schnittstellen/202610/trigger/events/LF-START_STORNO_AUFTRAG) | Event | — | transaktionsdaten › absender |
| [[LF] START_STORNO_AUFTRAG](/schnittstellen/202610/trigger/events/LF-START_STORNO_AUFTRAG) | Event | — | transaktionsdaten › empfaenger |
| [[LF] START_STORNO_SE_AUFTRAG](/schnittstellen/202610/trigger/events/LF-START_STORNO_SE_AUFTRAG) | Event | — | transaktionsdaten › absender |
| [[LF] START_STORNO_SE_AUFTRAG](/schnittstellen/202610/trigger/events/LF-START_STORNO_SE_AUFTRAG) | Event | — | transaktionsdaten › empfaenger |
| [[LF] START_UEBERMITTLUNG_ENFG](/schnittstellen/202610/trigger/events/LF-START_UEBERMITTLUNG_ENFG) | Event | — | transaktionsdaten › absender |
| [[LF] START_UEBERMITTLUNG_ENFG](/schnittstellen/202610/trigger/events/LF-START_UEBERMITTLUNG_ENFG) | Event | — | transaktionsdaten › empfaenger |
| [[LF] START_UEBERM_DEFINITION](/schnittstellen/202610/trigger/events/LF-START_UEBERM_DEFINITION) | Event | — | transaktionsdaten › absender |
| [[LF] START_UEBERM_DEFINITION](/schnittstellen/202610/trigger/events/LF-START_UEBERM_DEFINITION) | Event | — | transaktionsdaten › empfaenger |
| [[LF] START_UEBERSICHT_LEISTUNGSKURVENDEF](/schnittstellen/202610/trigger/events/LF-START_UEBERSICHT_LEISTUNGSKURVENDEF) | Event | — | transaktionsdaten › absender |
| [[LF] START_UEBERSICHT_LEISTUNGSKURVENDEF](/schnittstellen/202610/trigger/events/LF-START_UEBERSICHT_LEISTUNGSKURVENDEF) | Event | — | transaktionsdaten › empfaenger |
| [[LF] START_UEBERSICHT_SCHALTZEITDEF](/schnittstellen/202610/trigger/events/LF-START_UEBERSICHT_SCHALTZEITDEF) | Event | — | transaktionsdaten › absender |
| [[LF] START_UEBERSICHT_SCHALTZEITDEF](/schnittstellen/202610/trigger/events/LF-START_UEBERSICHT_SCHALTZEITDEF) | Event | — | transaktionsdaten › empfaenger |
| [[LF] START_UEBERSICHT_ZAEHLZEITDEF](/schnittstellen/202610/trigger/events/LF-START_UEBERSICHT_ZAEHLZEITDEF) | Event | — | transaktionsdaten › absender |
| [[LF] START_UEBERSICHT_ZAEHLZEITDEF](/schnittstellen/202610/trigger/events/LF-START_UEBERSICHT_ZAEHLZEITDEF) | Event | — | transaktionsdaten › empfaenger |
| [[LF] START_VERSAND_ANF_STORNO](/schnittstellen/202610/trigger/events/LF-START_VERSAND_ANF_STORNO) | Event | — | transaktionsdaten › absender |
| [[LF] START_VERSAND_ANF_STORNO](/schnittstellen/202610/trigger/events/LF-START_VERSAND_ANF_STORNO) | Event | — | transaktionsdaten › empfaenger |
| [[LF] START_VERSAND_ANTWORT_NNA](/schnittstellen/202610/trigger/events/LF-START_VERSAND_ANTWORT_NNA) | Event | — | transaktionsdaten › absender |
| [[LF] START_VERSAND_ANTWORT_NNA](/schnittstellen/202610/trigger/events/LF-START_VERSAND_ANTWORT_NNA) | Event | — | transaktionsdaten › empfaenger |
| [[LF] START_VERSAND_BEST_BEEND_KONFIG](/schnittstellen/202610/trigger/events/LF-START_VERSAND_BEST_BEEND_KONFIG) | Event | — | transaktionsdaten › absender |
| [[LF] START_VERSAND_BEST_BEEND_KONFIG](/schnittstellen/202610/trigger/events/LF-START_VERSAND_BEST_BEEND_KONFIG) | Event | — | transaktionsdaten › empfaenger |
| [[LF] START_VERSAND_SDAE](/schnittstellen/202610/trigger/events/LF-START_VERSAND_SDAE) | Event | — | transaktionsdaten › absender |
| [[LF] START_VERSAND_SDAE](/schnittstellen/202610/trigger/events/LF-START_VERSAND_SDAE) | Event | — | transaktionsdaten › empfaenger |
| [[LF] START_VERSAND_STOERUNGSMELDUNG](/schnittstellen/202610/trigger/events/LF-START_VERSAND_STOERUNGSMELDUNG) | Event | — | transaktionsdaten › absender |
| [[LF] START_VERSAND_STOERUNGSMELDUNG](/schnittstellen/202610/trigger/events/LF-START_VERSAND_STOERUNGSMELDUNG) | Event | — | transaktionsdaten › empfaenger |
| [[LF] START_VERSAND_STORNO_MSCONS](/schnittstellen/202610/trigger/events/LF-START_VERSAND_STORNO_MSCONS) | Event | — | transaktionsdaten › absender |
| [[LF] START_VERSAND_STORNO_MSCONS](/schnittstellen/202610/trigger/events/LF-START_VERSAND_STORNO_MSCONS) | Event | — | transaktionsdaten › empfaenger |
| [[MSB] START_ANGEBOT_GERAETEUEBERNAHME](/schnittstellen/202610/trigger/events/MSB-START_ANGEBOT_GERAETEUEBERNAHME) | Event | — | transaktionsdaten › absender |
| [[MSB] START_ANGEBOT_GERAETEUEBERNAHME](/schnittstellen/202610/trigger/events/MSB-START_ANGEBOT_GERAETEUEBERNAHME) | Event | — | transaktionsdaten › empfaenger |
| [[MSB] START_ANTWORT_GERAETEWECHSEL](/schnittstellen/202610/trigger/events/MSB-START_ANTWORT_GERAETEWECHSEL) | Event | — | transaktionsdaten › absender |
| [[MSB] START_ANTWORT_GERAETEWECHSEL](/schnittstellen/202610/trigger/events/MSB-START_ANTWORT_GERAETEWECHSEL) | Event | — | transaktionsdaten › empfaenger |
| [[MSB] START_BEGINN_MSB](/schnittstellen/202610/trigger/events/MSB-START_BEGINN_MSB) | Event | — | transaktionsdaten › absender |
| [[MSB] START_BEGINN_MSB](/schnittstellen/202610/trigger/events/MSB-START_BEGINN_MSB) | Event | — | transaktionsdaten › empfaenger |
| [[MSB] START_BESTELLUNG_GERAETEUEBERNAHME](/schnittstellen/202610/trigger/events/MSB-START_BESTELLUNG_GERAETEUEBERNAHME) | Event | — | transaktionsdaten › absender |
| [[MSB] START_BESTELLUNG_GERAETEUEBERNAHME](/schnittstellen/202610/trigger/events/MSB-START_BESTELLUNG_GERAETEUEBERNAHME) | Event | — | transaktionsdaten › empfaenger |
| [[MSB] START_BESTELLUNG_SDAE GAS](/schnittstellen/202610/trigger/events/MSB-START_BESTELLUNG_SDAE-GAS) | Event | — | transaktionsdaten › absender |
| [[MSB] START_BESTELLUNG_SDAE GAS](/schnittstellen/202610/trigger/events/MSB-START_BESTELLUNG_SDAE-GAS) | Event | — | transaktionsdaten › empfaenger |
| [[MSB] START_ERHEBUNG_MESSWERTE](/schnittstellen/202610/trigger/events/MSB-START_ERHEBUNG_MESSWERTE) | Event | — | transaktionsdaten › absender |
| [[MSB] START_ERHEBUNG_MESSWERTE](/schnittstellen/202610/trigger/events/MSB-START_ERHEBUNG_MESSWERTE) | Event | — | transaktionsdaten › empfaenger |
| [[MSB] START_GERAETEUEBERNAHME](/schnittstellen/202610/trigger/events/MSB-START_GERAETEUEBERNAHME) | Event | — | transaktionsdaten › absender |
| [[MSB] START_GERAETEUEBERNAHME](/schnittstellen/202610/trigger/events/MSB-START_GERAETEUEBERNAHME) | Event | — | transaktionsdaten › empfaenger |
| [[MSB] START_GERAETEWECHSEL](/schnittstellen/202610/trigger/events/MSB-START_GERAETEWECHSEL) | Event | — | transaktionsdaten › absender |
| [[MSB] START_GERAETEWECHSEL](/schnittstellen/202610/trigger/events/MSB-START_GERAETEWECHSEL) | Event | — | transaktionsdaten › empfaenger |
| [[MSB] START_GESCHAEFTSDATENANFRAGE](/schnittstellen/202610/trigger/events/MSB-START_GESCHAEFTSDATENANFRAGE) | Event | — | transaktionsdaten › absender |
| [[MSB] START_GESCHAEFTSDATENANFRAGE](/schnittstellen/202610/trigger/events/MSB-START_GESCHAEFTSDATENANFRAGE) | Event | — | transaktionsdaten › empfaenger |
| [[MSB] START_VERSAND_ANF_STORNO](/schnittstellen/202610/trigger/events/MSB-START_VERSAND_ANF_STORNO) | Event | — | transaktionsdaten › absender |
| [[MSB] START_VERSAND_ANF_STORNO](/schnittstellen/202610/trigger/events/MSB-START_VERSAND_ANF_STORNO) | Event | — | transaktionsdaten › empfaenger |
| [[MSB] START_VERSAND_PREISBLATT_IMS](/schnittstellen/202610/trigger/events/MSB-START_VERSAND_PREISBLATT_IMS) | Event | — | transaktionsdaten › absender |
| [[MSB] START_VERSAND_PREISBLATT_IMS](/schnittstellen/202610/trigger/events/MSB-START_VERSAND_PREISBLATT_IMS) | Event | — | transaktionsdaten › empfaenger |
| [[MSB] START_VERSAND_SDAE](/schnittstellen/202610/trigger/events/MSB-START_VERSAND_SDAE) | Event | — | transaktionsdaten › absender |
| [[MSB] START_VERSAND_SDAE](/schnittstellen/202610/trigger/events/MSB-START_VERSAND_SDAE) | Event | — | transaktionsdaten › empfaenger |
| [[MSB] START_VERSAND_STORNO_MSCONS](/schnittstellen/202610/trigger/events/MSB-START_VERSAND_STORNO_MSCONS) | Event | — | transaktionsdaten › absender |
| [[MSB] START_VERSAND_STORNO_MSCONS](/schnittstellen/202610/trigger/events/MSB-START_VERSAND_STORNO_MSCONS) | Event | — | transaktionsdaten › empfaenger |
| [[NB] START_ABR_BK](/schnittstellen/202610/trigger/events/NB-START_ABR_BK) | Event | — | transaktionsdaten › absender |
| [[NB] START_ABR_BK](/schnittstellen/202610/trigger/events/NB-START_ABR_BK) | Event | — | transaktionsdaten › empfaenger |
| [[NB] START_ABR_NN](/schnittstellen/202610/trigger/events/NB-START_ABR_NN) | Event | — | transaktionsdaten › absender |
| [[NB] START_ABR_NN](/schnittstellen/202610/trigger/events/NB-START_ABR_NN) | Event | — | transaktionsdaten › empfaenger |
| [[NB] START_ANFORDERUNG_MESSWERTE](/schnittstellen/202610/trigger/events/NB-START_ANFORDERUNG_MESSWERTE) | Event | — | transaktionsdaten › absender |
| [[NB] START_ANFORDERUNG_MESSWERTE](/schnittstellen/202610/trigger/events/NB-START_ANFORDERUNG_MESSWERTE) | Event | — | transaktionsdaten › empfaenger |
| [[NB] START_ANFRAGE_MESSWERTE_NB](/schnittstellen/202610/trigger/events/NB-START_ANFRAGE_MESSWERTE_NB) | Event | — | transaktionsdaten › absender |
| [[NB] START_ANFRAGE_MESSWERTE_NB](/schnittstellen/202610/trigger/events/NB-START_ANFRAGE_MESSWERTE_NB) | Event | — | transaktionsdaten › empfaenger |
| [[NB] START_ANFRAGE_SPERRUNG](/schnittstellen/202610/trigger/events/NB-START_ANFRAGE_SPERRUNG) | Event | — | transaktionsdaten › absender |
| [[NB] START_ANFRAGE_SPERRUNG](/schnittstellen/202610/trigger/events/NB-START_ANFRAGE_SPERRUNG) | Event | — | transaktionsdaten › empfaenger |
| [[NB] START_ANFRAGE_STAMMDATENAENDERUNG GAS](/schnittstellen/202610/trigger/events/NB-START_ANFRAGE_STAMMDATENAENDERUNG-GAS) | Event | — | transaktionsdaten › absender |
| [[NB] START_ANFRAGE_STAMMDATENAENDERUNG GAS](/schnittstellen/202610/trigger/events/NB-START_ANFRAGE_STAMMDATENAENDERUNG-GAS) | Event | — | transaktionsdaten › empfaenger |
| [[NB] START_AUFH_ZUK_ZUORDNUNG](/schnittstellen/202610/trigger/events/NB-START_AUFH_ZUK_ZUORDNUNG) | Event | — | transaktionsdaten › absender |
| [[NB] START_AUFH_ZUK_ZUORDNUNG](/schnittstellen/202610/trigger/events/NB-START_AUFH_ZUK_ZUORDNUNG) | Event | — | transaktionsdaten › empfaenger |
| [[NB] START_AUFTRAGSSTATUS](/schnittstellen/202610/trigger/events/NB-START_AUFTRAGSSTATUS) | Event | — | transaktionsdaten › absender |
| [[NB] START_AUFTRAGSSTATUS](/schnittstellen/202610/trigger/events/NB-START_AUFTRAGSSTATUS) | Event | — | transaktionsdaten › empfaenger |
| [[NB] START_BERECHNUNGSFORMEL](/schnittstellen/202610/trigger/events/NB-START_BERECHNUNGSFORMEL) | Event | — | transaktionsdaten › absender |
| [[NB] START_BERECHNUNGSFORMEL](/schnittstellen/202610/trigger/events/NB-START_BERECHNUNGSFORMEL) | Event | — | transaktionsdaten › empfaenger |
| [[NB] START_BESTELLUNG_SDAE](/schnittstellen/202610/trigger/events/NB-START_BESTELLUNG_SDAE) | Event | — | transaktionsdaten › absender |
| [[NB] START_BESTELLUNG_SDAE](/schnittstellen/202610/trigger/events/NB-START_BESTELLUNG_SDAE) | Event | — | transaktionsdaten › empfaenger |
| [[NB] START_BEST_AEND_TK](/schnittstellen/202610/trigger/events/NB-START_BEST_AEND_TK) | Event | — | transaktionsdaten › absender |
| [[NB] START_BEST_AEND_TK](/schnittstellen/202610/trigger/events/NB-START_BEST_AEND_TK) | Event | — | transaktionsdaten › empfaenger |
| [[NB] START_EINRICHTUNG_KONFIG](/schnittstellen/202610/trigger/events/NB-START_EINRICHTUNG_KONFIG) | Event | — | transaktionsdaten › absender |
| [[NB] START_EINRICHTUNG_KONFIG](/schnittstellen/202610/trigger/events/NB-START_EINRICHTUNG_KONFIG) | Event | — | transaktionsdaten › empfaenger |
| [[NB] START_ENDE_MSB_STILLLEGUNG GAS](/schnittstellen/202610/trigger/events/NB-START_ENDE_MSB_STILLLEGUNG-GAS) | Event | — | transaktionsdaten › absender |
| [[NB] START_ENDE_MSB_STILLLEGUNG GAS](/schnittstellen/202610/trigger/events/NB-START_ENDE_MSB_STILLLEGUNG-GAS) | Event | — | transaktionsdaten › empfaenger |
| [[NB] START_ENDE_ZUORDNUNG](/schnittstellen/202610/trigger/events/NB-START_ENDE_ZUORDNUNG) | Event | — | transaktionsdaten › absender |
| [[NB] START_ENDE_ZUORDNUNG](/schnittstellen/202610/trigger/events/NB-START_ENDE_ZUORDNUNG) | Event | — | transaktionsdaten › empfaenger |
| [[NB] START_EOG](/schnittstellen/202610/trigger/events/NB-START_EOG) | Event | — | transaktionsdaten › absender |
| [[NB] START_EOG](/schnittstellen/202610/trigger/events/NB-START_EOG) | Event | — | transaktionsdaten › empfaenger |
| [[NB] START_ERHEBUNG_MESSWERTE](/schnittstellen/202610/trigger/events/NB-START_ERHEBUNG_MESSWERTE) | Event | — | transaktionsdaten › absender |
| [[NB] START_ERHEBUNG_MESSWERTE](/schnittstellen/202610/trigger/events/NB-START_ERHEBUNG_MESSWERTE) | Event | — | transaktionsdaten › empfaenger |
| [[NB] START_LIEFERENDE](/schnittstellen/202610/trigger/events/NB-START_LIEFERENDE) | Event | — | transaktionsdaten › absender |
| [[NB] START_LIEFERENDE](/schnittstellen/202610/trigger/events/NB-START_LIEFERENDE) | Event | — | transaktionsdaten › empfaenger |
| [[NB] START_PREISBLATT](/schnittstellen/202610/trigger/events/NB-START_PREISBLATT) | Event | — | transaktionsdaten › absender |
| [[NB] START_PREISBLATT](/schnittstellen/202610/trigger/events/NB-START_PREISBLATT) | Event | — | transaktionsdaten › empfaenger |
| [[NB] START_REKLAMATION_WERTE](/schnittstellen/202610/trigger/events/NB-START_REKLAMATION_WERTE) | Event | — | transaktionsdaten › absender |
| [[NB] START_REKLAMATION_WERTE](/schnittstellen/202610/trigger/events/NB-START_REKLAMATION_WERTE) | Event | — | transaktionsdaten › empfaenger |
| [[NB] START_VERSAND_ANF_STORNO](/schnittstellen/202610/trigger/events/NB-START_VERSAND_ANF_STORNO) | Event | — | transaktionsdaten › absender |
| [[NB] START_VERSAND_ANF_STORNO](/schnittstellen/202610/trigger/events/NB-START_VERSAND_ANF_STORNO) | Event | — | transaktionsdaten › empfaenger |
| [[NB] START_VERSAND_BEARB_MELDUNG](/schnittstellen/202610/trigger/events/NB-START_VERSAND_BEARB_MELDUNG) | Event | — | transaktionsdaten › absender |
| [[NB] START_VERSAND_BEARB_MELDUNG](/schnittstellen/202610/trigger/events/NB-START_VERSAND_BEARB_MELDUNG) | Event | — | transaktionsdaten › empfaenger |
| [[NB] START_VERSAND_BEENDIGUNG_AGV](/schnittstellen/202610/trigger/events/NB-START_VERSAND_BEENDIGUNG_AGV) | Event | — | transaktionsdaten › absender |
| [[NB] START_VERSAND_BEENDIGUNG_AGV](/schnittstellen/202610/trigger/events/NB-START_VERSAND_BEENDIGUNG_AGV) | Event | — | transaktionsdaten › empfaenger |
| [[NB] START_VERSAND_BESTANDSLISTE GAS](/schnittstellen/202610/trigger/events/NB-START_VERSAND_BESTANDSLISTE-GAS) | Event | — | transaktionsdaten › absender |
| [[NB] START_VERSAND_BESTANDSLISTE GAS](/schnittstellen/202610/trigger/events/NB-START_VERSAND_BESTANDSLISTE-GAS) | Event | — | transaktionsdaten › empfaenger |
| [[NB] START_VERSAND_COMDIS](/schnittstellen/202610/trigger/events/NB-START_VERSAND_COMDIS) | Event | — | transaktionsdaten › absender |
| [[NB] START_VERSAND_COMDIS](/schnittstellen/202610/trigger/events/NB-START_VERSAND_COMDIS) | Event | — | transaktionsdaten › empfaenger |
| [[NB] START_VERSAND_GEMESSENE_ARB_LEIST_WERTE](/schnittstellen/202610/trigger/events/NB-START_VERSAND_GEMESSENE_ARB_LEIST_WERTE) | Event | — | transaktionsdaten › absender |
| [[NB] START_VERSAND_GEMESSENE_ARB_LEIST_WERTE](/schnittstellen/202610/trigger/events/NB-START_VERSAND_GEMESSENE_ARB_LEIST_WERTE) | Event | — | transaktionsdaten › empfaenger |
| [[NB] START_VERSAND_LIEFERSCHEIN](/schnittstellen/202610/trigger/events/NB-START_VERSAND_LIEFERSCHEIN) | Event | — | transaktionsdaten › absender |
| [[NB] START_VERSAND_LIEFERSCHEIN](/schnittstellen/202610/trigger/events/NB-START_VERSAND_LIEFERSCHEIN) | Event | — | transaktionsdaten › empfaenger |
| [[NB] START_VERSAND_SDAE](/schnittstellen/202610/trigger/events/NB-START_VERSAND_SDAE) | Event | — | transaktionsdaten › absender |
| [[NB] START_VERSAND_SDAE](/schnittstellen/202610/trigger/events/NB-START_VERSAND_SDAE) | Event | — | transaktionsdaten › empfaenger |
| [[NB] START_VERSAND_STATUSMELDUNG](/schnittstellen/202610/trigger/events/NB-START_VERSAND_STATUSMELDUNG) | Event | — | transaktionsdaten › absender |
| [[NB] START_VERSAND_STATUSMELDUNG](/schnittstellen/202610/trigger/events/NB-START_VERSAND_STATUSMELDUNG) | Event | — | transaktionsdaten › empfaenger |
| [[NB] START_VERSAND_STOERUNGSMELDUNG_NB](/schnittstellen/202610/trigger/events/NB-START_VERSAND_STOERUNGSMELDUNG_NB) | Event | — | transaktionsdaten › absender |
| [[NB] START_VERSAND_STOERUNGSMELDUNG_NB](/schnittstellen/202610/trigger/events/NB-START_VERSAND_STOERUNGSMELDUNG_NB) | Event | — | transaktionsdaten › empfaenger |
| [[NB] START_VERSAND_STORNO_MSCONS](/schnittstellen/202610/trigger/events/NB-START_VERSAND_STORNO_MSCONS) | Event | — | transaktionsdaten › absender |
| [[NB] START_VERSAND_STORNO_MSCONS](/schnittstellen/202610/trigger/events/NB-START_VERSAND_STORNO_MSCONS) | Event | — | transaktionsdaten › empfaenger |
| [[NB] START_WIEDERHERST_LB](/schnittstellen/202610/trigger/events/NB-START_WIEDERHERST_LB) | Event | — | transaktionsdaten › absender |
| [[NB] START_WIEDERHERST_LB](/schnittstellen/202610/trigger/events/NB-START_WIEDERHERST_LB) | Event | — | transaktionsdaten › empfaenger |
| [[NB] START_WIEDERSPRUCH_ABLEHNUNG](/schnittstellen/202610/trigger/events/NB-START_WIEDERSPRUCH_ABLEHNUNG) | Event | — | transaktionsdaten › absender |
| [[NB] START_WIEDERSPRUCH_ABLEHNUNG](/schnittstellen/202610/trigger/events/NB-START_WIEDERSPRUCH_ABLEHNUNG) | Event | — | transaktionsdaten › empfaenger |
| [[NB] START_ZUORDNUNG_ERZ_MALO_TRANCHE](/schnittstellen/202610/trigger/events/NB-START_ZUORDNUNG_ERZ_MALO_TRANCHE) | Event | — | transaktionsdaten › absender |
| [[NB] START_ZUORDNUNG_ERZ_MALO_TRANCHE](/schnittstellen/202610/trigger/events/NB-START_ZUORDNUNG_ERZ_MALO_TRANCHE) | Event | — | transaktionsdaten › empfaenger |
| [PI_13002](/schnittstellen/202610/pruefi/MSCONS/PI_13002) | Prüfi | MSCONS | transaktionsdaten › absender |
| [PI_13002](/schnittstellen/202610/pruefi/MSCONS/PI_13002) | Prüfi | MSCONS | transaktionsdaten › empfaenger |
| [PI_13003](/schnittstellen/202610/pruefi/MSCONS/PI_13003) | Prüfi | MSCONS | transaktionsdaten › absender |
| [PI_13003](/schnittstellen/202610/pruefi/MSCONS/PI_13003) | Prüfi | MSCONS | transaktionsdaten › empfaenger |
| [PI_13006](/schnittstellen/202610/pruefi/MSCONS/PI_13006) | Prüfi | MSCONS | transaktionsdaten › absender |
| [PI_13006](/schnittstellen/202610/pruefi/MSCONS/PI_13006) | Prüfi | MSCONS | transaktionsdaten › empfaenger |
| [PI_13007](/schnittstellen/202610/pruefi/MSCONS/PI_13007) | Prüfi | MSCONS | transaktionsdaten › absender |
| [PI_13007](/schnittstellen/202610/pruefi/MSCONS/PI_13007) | Prüfi | MSCONS | transaktionsdaten › empfaenger |
| [PI_13008](/schnittstellen/202610/pruefi/MSCONS/PI_13008) | Prüfi | MSCONS | transaktionsdaten › absender |
| [PI_13008](/schnittstellen/202610/pruefi/MSCONS/PI_13008) | Prüfi | MSCONS | transaktionsdaten › empfaenger |
| [PI_13009](/schnittstellen/202610/pruefi/MSCONS/PI_13009) | Prüfi | MSCONS | transaktionsdaten › absender |
| [PI_13009](/schnittstellen/202610/pruefi/MSCONS/PI_13009) | Prüfi | MSCONS | transaktionsdaten › empfaenger |
| [PI_13010](/schnittstellen/202610/pruefi/MSCONS/PI_13010) | Prüfi | MSCONS | transaktionsdaten › absender |
| [PI_13010](/schnittstellen/202610/pruefi/MSCONS/PI_13010) | Prüfi | MSCONS | transaktionsdaten › empfaenger |
| [PI_13011](/schnittstellen/202610/pruefi/MSCONS/PI_13011) | Prüfi | MSCONS | transaktionsdaten › absender |
| [PI_13011](/schnittstellen/202610/pruefi/MSCONS/PI_13011) | Prüfi | MSCONS | transaktionsdaten › empfaenger |
| [PI_13015](/schnittstellen/202610/pruefi/MSCONS/PI_13015) | Prüfi | MSCONS | transaktionsdaten › absender |
| [PI_13015](/schnittstellen/202610/pruefi/MSCONS/PI_13015) | Prüfi | MSCONS | transaktionsdaten › empfaenger |
| [PI_13016](/schnittstellen/202610/pruefi/MSCONS/PI_13016) | Prüfi | MSCONS | transaktionsdaten › absender |
| [PI_13016](/schnittstellen/202610/pruefi/MSCONS/PI_13016) | Prüfi | MSCONS | transaktionsdaten › empfaenger |
| [PI_13017](/schnittstellen/202610/pruefi/MSCONS/PI_13017) | Prüfi | MSCONS | transaktionsdaten › absender |
| [PI_13017](/schnittstellen/202610/pruefi/MSCONS/PI_13017) | Prüfi | MSCONS | transaktionsdaten › empfaenger |
| [PI_13018](/schnittstellen/202610/pruefi/MSCONS/PI_13018) | Prüfi | MSCONS | transaktionsdaten › absender |
| [PI_13018](/schnittstellen/202610/pruefi/MSCONS/PI_13018) | Prüfi | MSCONS | transaktionsdaten › empfaenger |
| [PI_13019](/schnittstellen/202610/pruefi/MSCONS/PI_13019) | Prüfi | MSCONS | transaktionsdaten › absender |
| [PI_13019](/schnittstellen/202610/pruefi/MSCONS/PI_13019) | Prüfi | MSCONS | transaktionsdaten › empfaenger |
| [PI_13025](/schnittstellen/202610/pruefi/MSCONS/PI_13025) | Prüfi | MSCONS | transaktionsdaten › absender |
| [PI_13025](/schnittstellen/202610/pruefi/MSCONS/PI_13025) | Prüfi | MSCONS | transaktionsdaten › empfaenger |
| [PI_13027](/schnittstellen/202610/pruefi/MSCONS/PI_13027) | Prüfi | MSCONS | transaktionsdaten › absender |
| [PI_13027](/schnittstellen/202610/pruefi/MSCONS/PI_13027) | Prüfi | MSCONS | transaktionsdaten › empfaenger |
| [PI_13028](/schnittstellen/202610/pruefi/MSCONS/PI_13028) | Prüfi | MSCONS | transaktionsdaten › absender |
| [PI_13028](/schnittstellen/202610/pruefi/MSCONS/PI_13028) | Prüfi | MSCONS | transaktionsdaten › empfaenger |
| [PI_15001](/schnittstellen/202610/pruefi/QUOTES/PI_15001) | Prüfi | QUOTES | stammdaten › ANGEBOT › positionsdaten › beteiligterMarktpartner |
| [PI_15001](/schnittstellen/202610/pruefi/QUOTES/PI_15001) | Prüfi | QUOTES | transaktionsdaten › absender |
| [PI_15001](/schnittstellen/202610/pruefi/QUOTES/PI_15001) | Prüfi | QUOTES | transaktionsdaten › empfaenger |
| [PI_15003](/schnittstellen/202610/pruefi/QUOTES/PI_15003) | Prüfi | QUOTES | transaktionsdaten › absender |
| [PI_15003](/schnittstellen/202610/pruefi/QUOTES/PI_15003) | Prüfi | QUOTES | transaktionsdaten › empfaenger |
| [PI_15004](/schnittstellen/202610/pruefi/QUOTES/PI_15004) | Prüfi | QUOTES | transaktionsdaten › absender |
| [PI_15004](/schnittstellen/202610/pruefi/QUOTES/PI_15004) | Prüfi | QUOTES | transaktionsdaten › empfaenger |
| [PI_15005](/schnittstellen/202610/pruefi/QUOTES/PI_15005) | Prüfi | QUOTES | transaktionsdaten › absender |
| [PI_15005](/schnittstellen/202610/pruefi/QUOTES/PI_15005) | Prüfi | QUOTES | transaktionsdaten › empfaenger |
| [PI_17001](/schnittstellen/202610/pruefi/ORDERS/PI_17001) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17001](/schnittstellen/202610/pruefi/ORDERS/PI_17001) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17002](/schnittstellen/202610/pruefi/ORDERS/PI_17002) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17002](/schnittstellen/202610/pruefi/ORDERS/PI_17002) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17004](/schnittstellen/202610/pruefi/ORDERS/PI_17004) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17004](/schnittstellen/202610/pruefi/ORDERS/PI_17004) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17005](/schnittstellen/202610/pruefi/ORDERS/PI_17005) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17005](/schnittstellen/202610/pruefi/ORDERS/PI_17005) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17006](/schnittstellen/202610/pruefi/ORDERS/PI_17006) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17006](/schnittstellen/202610/pruefi/ORDERS/PI_17006) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17009](/schnittstellen/202610/pruefi/ORDERS/PI_17009) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17009](/schnittstellen/202610/pruefi/ORDERS/PI_17009) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17101](/schnittstellen/202610/pruefi/ORDERS/PI_17101) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17101](/schnittstellen/202610/pruefi/ORDERS/PI_17101) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17102](/schnittstellen/202610/pruefi/ORDERS/PI_17102) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17102](/schnittstellen/202610/pruefi/ORDERS/PI_17102) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17103](/schnittstellen/202610/pruefi/ORDERS/PI_17103) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17103](/schnittstellen/202610/pruefi/ORDERS/PI_17103) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17104](/schnittstellen/202610/pruefi/ORDERS/PI_17104) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17104](/schnittstellen/202610/pruefi/ORDERS/PI_17104) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17113](/schnittstellen/202610/pruefi/ORDERS/PI_17113) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17113](/schnittstellen/202610/pruefi/ORDERS/PI_17113) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17115](/schnittstellen/202610/pruefi/ORDERS/PI_17115) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17115](/schnittstellen/202610/pruefi/ORDERS/PI_17115) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17116](/schnittstellen/202610/pruefi/ORDERS/PI_17116) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17116](/schnittstellen/202610/pruefi/ORDERS/PI_17116) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17117](/schnittstellen/202610/pruefi/ORDERS/PI_17117) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17117](/schnittstellen/202610/pruefi/ORDERS/PI_17117) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17118](/schnittstellen/202610/pruefi/ORDERS/PI_17118) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17118](/schnittstellen/202610/pruefi/ORDERS/PI_17118) | Prüfi | ORDERS | transaktionsdaten › beteiligterMarktpartner |
| [PI_17118](/schnittstellen/202610/pruefi/ORDERS/PI_17118) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17120](/schnittstellen/202610/pruefi/ORDERS/PI_17120) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17120](/schnittstellen/202610/pruefi/ORDERS/PI_17120) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17121](/schnittstellen/202610/pruefi/ORDERS/PI_17121) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17121](/schnittstellen/202610/pruefi/ORDERS/PI_17121) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17122](/schnittstellen/202610/pruefi/ORDERS/PI_17122) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17122](/schnittstellen/202610/pruefi/ORDERS/PI_17122) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17123](/schnittstellen/202610/pruefi/ORDERS/PI_17123) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17123](/schnittstellen/202610/pruefi/ORDERS/PI_17123) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17126](/schnittstellen/202610/pruefi/ORDERS/PI_17126) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17126](/schnittstellen/202610/pruefi/ORDERS/PI_17126) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17128](/schnittstellen/202610/pruefi/ORDERS/PI_17128) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17128](/schnittstellen/202610/pruefi/ORDERS/PI_17128) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17129](/schnittstellen/202610/pruefi/ORDERS/PI_17129) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17129](/schnittstellen/202610/pruefi/ORDERS/PI_17129) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17130](/schnittstellen/202610/pruefi/ORDERS/PI_17130) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17130](/schnittstellen/202610/pruefi/ORDERS/PI_17130) | Prüfi | ORDERS | transaktionsdaten › beteiligterMarktpartner |
| [PI_17130](/schnittstellen/202610/pruefi/ORDERS/PI_17130) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17131](/schnittstellen/202610/pruefi/ORDERS/PI_17131) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17131](/schnittstellen/202610/pruefi/ORDERS/PI_17131) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17132](/schnittstellen/202610/pruefi/ORDERS/PI_17132) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17132](/schnittstellen/202610/pruefi/ORDERS/PI_17132) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17133](/schnittstellen/202610/pruefi/ORDERS/PI_17133) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17133](/schnittstellen/202610/pruefi/ORDERS/PI_17133) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17134](/schnittstellen/202610/pruefi/ORDERS/PI_17134) | Prüfi | ORDERS | stammdaten › MARKTLOKATION › marktrollen |
| [PI_17134](/schnittstellen/202610/pruefi/ORDERS/PI_17134) | Prüfi | ORDERS | stammdaten › TRANCHE › marktrollen |
| [PI_17134](/schnittstellen/202610/pruefi/ORDERS/PI_17134) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17134](/schnittstellen/202610/pruefi/ORDERS/PI_17134) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17135](/schnittstellen/202610/pruefi/ORDERS/PI_17135) | Prüfi | ORDERS | stammdaten › MARKTLOKATION › marktrollen |
| [PI_17135](/schnittstellen/202610/pruefi/ORDERS/PI_17135) | Prüfi | ORDERS | stammdaten › TRANCHE › marktrollen |
| [PI_17135](/schnittstellen/202610/pruefi/ORDERS/PI_17135) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17135](/schnittstellen/202610/pruefi/ORDERS/PI_17135) | Prüfi | ORDERS | transaktionsdaten › beteiligterMarktpartner |
| [PI_17135](/schnittstellen/202610/pruefi/ORDERS/PI_17135) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17201](/schnittstellen/202610/pruefi/ORDERS/PI_17201) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17201](/schnittstellen/202610/pruefi/ORDERS/PI_17201) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17202](/schnittstellen/202610/pruefi/ORDERS/PI_17202) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17202](/schnittstellen/202610/pruefi/ORDERS/PI_17202) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17203](/schnittstellen/202610/pruefi/ORDERS/PI_17203) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17203](/schnittstellen/202610/pruefi/ORDERS/PI_17203) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17204](/schnittstellen/202610/pruefi/ORDERS/PI_17204) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17204](/schnittstellen/202610/pruefi/ORDERS/PI_17204) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_19001](/schnittstellen/202610/pruefi/ORDRSP/PI_19001) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19001](/schnittstellen/202610/pruefi/ORDRSP/PI_19001) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19002](/schnittstellen/202610/pruefi/ORDRSP/PI_19002) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19002](/schnittstellen/202610/pruefi/ORDRSP/PI_19002) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19003](/schnittstellen/202610/pruefi/ORDRSP/PI_19003) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19003](/schnittstellen/202610/pruefi/ORDRSP/PI_19003) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19004](/schnittstellen/202610/pruefi/ORDRSP/PI_19004) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19004](/schnittstellen/202610/pruefi/ORDRSP/PI_19004) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19005](/schnittstellen/202610/pruefi/ORDRSP/PI_19005) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19005](/schnittstellen/202610/pruefi/ORDRSP/PI_19005) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19006](/schnittstellen/202610/pruefi/ORDRSP/PI_19006) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19006](/schnittstellen/202610/pruefi/ORDRSP/PI_19006) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19007](/schnittstellen/202610/pruefi/ORDRSP/PI_19007) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19007](/schnittstellen/202610/pruefi/ORDRSP/PI_19007) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19009](/schnittstellen/202610/pruefi/ORDRSP/PI_19009) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19009](/schnittstellen/202610/pruefi/ORDRSP/PI_19009) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19010](/schnittstellen/202610/pruefi/ORDRSP/PI_19010) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19010](/schnittstellen/202610/pruefi/ORDRSP/PI_19010) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19011](/schnittstellen/202610/pruefi/ORDRSP/PI_19011) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19011](/schnittstellen/202610/pruefi/ORDRSP/PI_19011) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19012](/schnittstellen/202610/pruefi/ORDRSP/PI_19012) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19012](/schnittstellen/202610/pruefi/ORDRSP/PI_19012) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19013](/schnittstellen/202610/pruefi/ORDRSP/PI_19013) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19013](/schnittstellen/202610/pruefi/ORDRSP/PI_19013) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19014](/schnittstellen/202610/pruefi/ORDRSP/PI_19014) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19014](/schnittstellen/202610/pruefi/ORDRSP/PI_19014) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19015](/schnittstellen/202610/pruefi/ORDRSP/PI_19015) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19015](/schnittstellen/202610/pruefi/ORDRSP/PI_19015) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19016](/schnittstellen/202610/pruefi/ORDRSP/PI_19016) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19016](/schnittstellen/202610/pruefi/ORDRSP/PI_19016) | Prüfi | ORDRSP | transaktionsdaten › beteiligterMarktpartner |
| [PI_19016](/schnittstellen/202610/pruefi/ORDRSP/PI_19016) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19101](/schnittstellen/202610/pruefi/ORDRSP/PI_19101) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19101](/schnittstellen/202610/pruefi/ORDRSP/PI_19101) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19102](/schnittstellen/202610/pruefi/ORDRSP/PI_19102) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19102](/schnittstellen/202610/pruefi/ORDRSP/PI_19102) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19103](/schnittstellen/202610/pruefi/ORDRSP/PI_19103) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19103](/schnittstellen/202610/pruefi/ORDRSP/PI_19103) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19104](/schnittstellen/202610/pruefi/ORDRSP/PI_19104) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19104](/schnittstellen/202610/pruefi/ORDRSP/PI_19104) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19114](/schnittstellen/202610/pruefi/ORDRSP/PI_19114) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19114](/schnittstellen/202610/pruefi/ORDRSP/PI_19114) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19116](/schnittstellen/202610/pruefi/ORDRSP/PI_19116) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19116](/schnittstellen/202610/pruefi/ORDRSP/PI_19116) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19117](/schnittstellen/202610/pruefi/ORDRSP/PI_19117) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19117](/schnittstellen/202610/pruefi/ORDRSP/PI_19117) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19118](/schnittstellen/202610/pruefi/ORDRSP/PI_19118) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19118](/schnittstellen/202610/pruefi/ORDRSP/PI_19118) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19119](/schnittstellen/202610/pruefi/ORDRSP/PI_19119) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19119](/schnittstellen/202610/pruefi/ORDRSP/PI_19119) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19121](/schnittstellen/202610/pruefi/ORDRSP/PI_19121) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19121](/schnittstellen/202610/pruefi/ORDRSP/PI_19121) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19123](/schnittstellen/202610/pruefi/ORDRSP/PI_19123) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19123](/schnittstellen/202610/pruefi/ORDRSP/PI_19123) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19124](/schnittstellen/202610/pruefi/ORDRSP/PI_19124) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19124](/schnittstellen/202610/pruefi/ORDRSP/PI_19124) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19128](/schnittstellen/202610/pruefi/ORDRSP/PI_19128) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19128](/schnittstellen/202610/pruefi/ORDRSP/PI_19128) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19129](/schnittstellen/202610/pruefi/ORDRSP/PI_19129) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19129](/schnittstellen/202610/pruefi/ORDRSP/PI_19129) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19133](/schnittstellen/202610/pruefi/ORDRSP/PI_19133) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19133](/schnittstellen/202610/pruefi/ORDRSP/PI_19133) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19301](/schnittstellen/202610/pruefi/ORDRSP/PI_19301) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19301](/schnittstellen/202610/pruefi/ORDRSP/PI_19301) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19302](/schnittstellen/202610/pruefi/ORDRSP/PI_19302) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19302](/schnittstellen/202610/pruefi/ORDRSP/PI_19302) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_21007](/schnittstellen/202610/pruefi/IFTSTA/PI_21007) | Prüfi | IFTSTA | stammdaten › MESSLOKATION › marktrollen |
| [PI_21007](/schnittstellen/202610/pruefi/IFTSTA/PI_21007) | Prüfi | IFTSTA | transaktionsdaten › absender |
| [PI_21007](/schnittstellen/202610/pruefi/IFTSTA/PI_21007) | Prüfi | IFTSTA | transaktionsdaten › empfaenger |
| [PI_21009](/schnittstellen/202610/pruefi/IFTSTA/PI_21009) | Prüfi | IFTSTA | transaktionsdaten › absender |
| [PI_21009](/schnittstellen/202610/pruefi/IFTSTA/PI_21009) | Prüfi | IFTSTA | transaktionsdaten › empfaenger |
| [PI_21010](/schnittstellen/202610/pruefi/IFTSTA/PI_21010) | Prüfi | IFTSTA | transaktionsdaten › absender |
| [PI_21010](/schnittstellen/202610/pruefi/IFTSTA/PI_21010) | Prüfi | IFTSTA | transaktionsdaten › empfaenger |
| [PI_21011](/schnittstellen/202610/pruefi/IFTSTA/PI_21011) | Prüfi | IFTSTA | transaktionsdaten › absender |
| [PI_21011](/schnittstellen/202610/pruefi/IFTSTA/PI_21011) | Prüfi | IFTSTA | transaktionsdaten › empfaenger |
| [PI_21012](/schnittstellen/202610/pruefi/IFTSTA/PI_21012) | Prüfi | IFTSTA | transaktionsdaten › absender |
| [PI_21012](/schnittstellen/202610/pruefi/IFTSTA/PI_21012) | Prüfi | IFTSTA | transaktionsdaten › empfaenger |
| [PI_21013](/schnittstellen/202610/pruefi/IFTSTA/PI_21013) | Prüfi | IFTSTA | transaktionsdaten › absender |
| [PI_21013](/schnittstellen/202610/pruefi/IFTSTA/PI_21013) | Prüfi | IFTSTA | transaktionsdaten › empfaenger |
| [PI_21018](/schnittstellen/202610/pruefi/IFTSTA/PI_21018) | Prüfi | IFTSTA | stammdaten › MESSLOKATION › marktrollen |
| [PI_21018](/schnittstellen/202610/pruefi/IFTSTA/PI_21018) | Prüfi | IFTSTA | transaktionsdaten › absender |
| [PI_21018](/schnittstellen/202610/pruefi/IFTSTA/PI_21018) | Prüfi | IFTSTA | transaktionsdaten › empfaenger |
| [PI_21025](/schnittstellen/202610/pruefi/IFTSTA/PI_21025) | Prüfi | IFTSTA | transaktionsdaten › absender |
| [PI_21025](/schnittstellen/202610/pruefi/IFTSTA/PI_21025) | Prüfi | IFTSTA | transaktionsdaten › empfaenger |
| [PI_21027](/schnittstellen/202610/pruefi/IFTSTA/PI_21027) | Prüfi | IFTSTA | transaktionsdaten › absender |
| [PI_21027](/schnittstellen/202610/pruefi/IFTSTA/PI_21027) | Prüfi | IFTSTA | transaktionsdaten › empfaenger |
| [PI_21028](/schnittstellen/202610/pruefi/IFTSTA/PI_21028) | Prüfi | IFTSTA | transaktionsdaten › absender |
| [PI_21028](/schnittstellen/202610/pruefi/IFTSTA/PI_21028) | Prüfi | IFTSTA | transaktionsdaten › empfaenger |
| [PI_21029](/schnittstellen/202610/pruefi/IFTSTA/PI_21029) | Prüfi | IFTSTA | transaktionsdaten › absender |
| [PI_21029](/schnittstellen/202610/pruefi/IFTSTA/PI_21029) | Prüfi | IFTSTA | transaktionsdaten › empfaenger |
| [PI_21030](/schnittstellen/202610/pruefi/IFTSTA/PI_21030) | Prüfi | IFTSTA | transaktionsdaten › absender |
| [PI_21030](/schnittstellen/202610/pruefi/IFTSTA/PI_21030) | Prüfi | IFTSTA | transaktionsdaten › empfaenger |
| [PI_21031](/schnittstellen/202610/pruefi/IFTSTA/PI_21031) | Prüfi | IFTSTA | transaktionsdaten › absender |
| [PI_21031](/schnittstellen/202610/pruefi/IFTSTA/PI_21031) | Prüfi | IFTSTA | transaktionsdaten › empfaenger |
| [PI_21032](/schnittstellen/202610/pruefi/IFTSTA/PI_21032) | Prüfi | IFTSTA | transaktionsdaten › absender |
| [PI_21032](/schnittstellen/202610/pruefi/IFTSTA/PI_21032) | Prüfi | IFTSTA | transaktionsdaten › empfaenger |
| [PI_21033](/schnittstellen/202610/pruefi/IFTSTA/PI_21033) | Prüfi | IFTSTA | transaktionsdaten › absender |
| [PI_21033](/schnittstellen/202610/pruefi/IFTSTA/PI_21033) | Prüfi | IFTSTA | transaktionsdaten › empfaenger |
| [PI_21035](/schnittstellen/202610/pruefi/IFTSTA/PI_21035) | Prüfi | IFTSTA | transaktionsdaten › absender |
| [PI_21035](/schnittstellen/202610/pruefi/IFTSTA/PI_21035) | Prüfi | IFTSTA | transaktionsdaten › empfaenger |
| [PI_21036](/schnittstellen/202610/pruefi/IFTSTA/PI_21036) | Prüfi | IFTSTA | transaktionsdaten › absender |
| [PI_21036](/schnittstellen/202610/pruefi/IFTSTA/PI_21036) | Prüfi | IFTSTA | transaktionsdaten › empfaenger |
| [PI_21039](/schnittstellen/202610/pruefi/IFTSTA/PI_21039) | Prüfi | IFTSTA | transaktionsdaten › absender |
| [PI_21039](/schnittstellen/202610/pruefi/IFTSTA/PI_21039) | Prüfi | IFTSTA | transaktionsdaten › empfaenger |
| [PI_21040](/schnittstellen/202610/pruefi/IFTSTA/PI_21040) | Prüfi | IFTSTA | transaktionsdaten › absender |
| [PI_21040](/schnittstellen/202610/pruefi/IFTSTA/PI_21040) | Prüfi | IFTSTA | transaktionsdaten › empfaenger |
| [PI_21043](/schnittstellen/202610/pruefi/IFTSTA/PI_21043) | Prüfi | IFTSTA | transaktionsdaten › absender |
| [PI_21043](/schnittstellen/202610/pruefi/IFTSTA/PI_21043) | Prüfi | IFTSTA | transaktionsdaten › empfaenger |
| [PI_21044](/schnittstellen/202610/pruefi/IFTSTA/PI_21044) | Prüfi | IFTSTA | transaktionsdaten › absender |
| [PI_21044](/schnittstellen/202610/pruefi/IFTSTA/PI_21044) | Prüfi | IFTSTA | transaktionsdaten › empfaenger |
| [PI_21045](/schnittstellen/202610/pruefi/IFTSTA/PI_21045) | Prüfi | IFTSTA | transaktionsdaten › absender |
| [PI_21045](/schnittstellen/202610/pruefi/IFTSTA/PI_21045) | Prüfi | IFTSTA | transaktionsdaten › empfaenger |
| [PI_21047](/schnittstellen/202610/pruefi/IFTSTA/PI_21047) | Prüfi | IFTSTA | transaktionsdaten › absender |
| [PI_21047](/schnittstellen/202610/pruefi/IFTSTA/PI_21047) | Prüfi | IFTSTA | transaktionsdaten › empfaenger |
| [PI_23001](/schnittstellen/202610/pruefi/INSRPT/PI_23001) | Prüfi | INSRPT | transaktionsdaten › absender |
| [PI_23001](/schnittstellen/202610/pruefi/INSRPT/PI_23001) | Prüfi | INSRPT | transaktionsdaten › empfaenger |
| [PI_23003](/schnittstellen/202610/pruefi/INSRPT/PI_23003) | Prüfi | INSRPT | transaktionsdaten › absender |
| [PI_23003](/schnittstellen/202610/pruefi/INSRPT/PI_23003) | Prüfi | INSRPT | transaktionsdaten › empfaenger |
| [PI_23004](/schnittstellen/202610/pruefi/INSRPT/PI_23004) | Prüfi | INSRPT | transaktionsdaten › absender |
| [PI_23004](/schnittstellen/202610/pruefi/INSRPT/PI_23004) | Prüfi | INSRPT | transaktionsdaten › empfaenger |
| [PI_23005](/schnittstellen/202610/pruefi/INSRPT/PI_23005) | Prüfi | INSRPT | transaktionsdaten › absender |
| [PI_23005](/schnittstellen/202610/pruefi/INSRPT/PI_23005) | Prüfi | INSRPT | transaktionsdaten › empfaenger |
| [PI_23008](/schnittstellen/202610/pruefi/INSRPT/PI_23008) | Prüfi | INSRPT | transaktionsdaten › absender |
| [PI_23008](/schnittstellen/202610/pruefi/INSRPT/PI_23008) | Prüfi | INSRPT | transaktionsdaten › empfaenger |
| [PI_23009](/schnittstellen/202610/pruefi/INSRPT/PI_23009) | Prüfi | INSRPT | transaktionsdaten › absender |
| [PI_23009](/schnittstellen/202610/pruefi/INSRPT/PI_23009) | Prüfi | INSRPT | transaktionsdaten › empfaenger |
| [PI_23011](/schnittstellen/202610/pruefi/INSRPT/PI_23011) | Prüfi | INSRPT | transaktionsdaten › absender |
| [PI_23011](/schnittstellen/202610/pruefi/INSRPT/PI_23011) | Prüfi | INSRPT | transaktionsdaten › empfaenger |
| [PI_23012](/schnittstellen/202610/pruefi/INSRPT/PI_23012) | Prüfi | INSRPT | transaktionsdaten › absender |
| [PI_23012](/schnittstellen/202610/pruefi/INSRPT/PI_23012) | Prüfi | INSRPT | transaktionsdaten › empfaenger |
| [PI_25001](/schnittstellen/202610/pruefi/UTILTS/PI_25001) | Prüfi | UTILTS | transaktionsdaten › absender |
| [PI_25001](/schnittstellen/202610/pruefi/UTILTS/PI_25001) | Prüfi | UTILTS | transaktionsdaten › empfaenger |
| [PI_25004](/schnittstellen/202610/pruefi/UTILTS/PI_25004) | Prüfi | UTILTS | transaktionsdaten › absender |
| [PI_25004](/schnittstellen/202610/pruefi/UTILTS/PI_25004) | Prüfi | UTILTS | transaktionsdaten › empfaenger |
| [PI_25005](/schnittstellen/202610/pruefi/UTILTS/PI_25005) | Prüfi | UTILTS | transaktionsdaten › absender |
| [PI_25005](/schnittstellen/202610/pruefi/UTILTS/PI_25005) | Prüfi | UTILTS | transaktionsdaten › empfaenger |
| [PI_25006](/schnittstellen/202610/pruefi/UTILTS/PI_25006) | Prüfi | UTILTS | transaktionsdaten › absender |
| [PI_25006](/schnittstellen/202610/pruefi/UTILTS/PI_25006) | Prüfi | UTILTS | transaktionsdaten › empfaenger |
| [PI_25007](/schnittstellen/202610/pruefi/UTILTS/PI_25007) | Prüfi | UTILTS | transaktionsdaten › absender |
| [PI_25007](/schnittstellen/202610/pruefi/UTILTS/PI_25007) | Prüfi | UTILTS | transaktionsdaten › empfaenger |
| [PI_25008](/schnittstellen/202610/pruefi/UTILTS/PI_25008) | Prüfi | UTILTS | transaktionsdaten › absender |
| [PI_25008](/schnittstellen/202610/pruefi/UTILTS/PI_25008) | Prüfi | UTILTS | transaktionsdaten › empfaenger |
| [PI_25009](/schnittstellen/202610/pruefi/UTILTS/PI_25009) | Prüfi | UTILTS | transaktionsdaten › absender |
| [PI_25009](/schnittstellen/202610/pruefi/UTILTS/PI_25009) | Prüfi | UTILTS | transaktionsdaten › empfaenger |
| [PI_25010](/schnittstellen/202610/pruefi/UTILTS/PI_25010) | Prüfi | UTILTS | transaktionsdaten › absender |
| [PI_25010](/schnittstellen/202610/pruefi/UTILTS/PI_25010) | Prüfi | UTILTS | transaktionsdaten › empfaenger |
| [PI_27002](/schnittstellen/202610/pruefi/PRICAT/PI_27002) | Prüfi | PRICAT | transaktionsdaten › absender |
| [PI_27002](/schnittstellen/202610/pruefi/PRICAT/PI_27002) | Prüfi | PRICAT | transaktionsdaten › empfaenger |
| [PI_27003](/schnittstellen/202610/pruefi/PRICAT/PI_27003) | Prüfi | PRICAT | transaktionsdaten › absender |
| [PI_27003](/schnittstellen/202610/pruefi/PRICAT/PI_27003) | Prüfi | PRICAT | transaktionsdaten › empfaenger |
| [PI_29001](/schnittstellen/202610/pruefi/COMDIS/PI_29001) | Prüfi | COMDIS | transaktionsdaten › absender |
| [PI_29001](/schnittstellen/202610/pruefi/COMDIS/PI_29001) | Prüfi | COMDIS | transaktionsdaten › empfaenger |
| [PI_29002](/schnittstellen/202610/pruefi/COMDIS/PI_29002) | Prüfi | COMDIS | transaktionsdaten › absender |
| [PI_29002](/schnittstellen/202610/pruefi/COMDIS/PI_29002) | Prüfi | COMDIS | transaktionsdaten › empfaenger |
| [PI_31001](/schnittstellen/202610/pruefi/INVOIC/PI_31001) | Prüfi | INVOIC | transaktionsdaten › absender |
| [PI_31001](/schnittstellen/202610/pruefi/INVOIC/PI_31001) | Prüfi | INVOIC | transaktionsdaten › empfaenger |
| [PI_31002](/schnittstellen/202610/pruefi/INVOIC/PI_31002) | Prüfi | INVOIC | transaktionsdaten › absender |
| [PI_31002](/schnittstellen/202610/pruefi/INVOIC/PI_31002) | Prüfi | INVOIC | transaktionsdaten › empfaenger |
| [PI_31003](/schnittstellen/202610/pruefi/INVOIC/PI_31003) | Prüfi | INVOIC | transaktionsdaten › absender |
| [PI_31003](/schnittstellen/202610/pruefi/INVOIC/PI_31003) | Prüfi | INVOIC | transaktionsdaten › empfaenger |
| [PI_31004](/schnittstellen/202610/pruefi/INVOIC/PI_31004) | Prüfi | INVOIC | transaktionsdaten › absender |
| [PI_31004](/schnittstellen/202610/pruefi/INVOIC/PI_31004) | Prüfi | INVOIC | transaktionsdaten › empfaenger |
| [PI_31005](/schnittstellen/202610/pruefi/INVOIC/PI_31005) | Prüfi | INVOIC | transaktionsdaten › absender |
| [PI_31005](/schnittstellen/202610/pruefi/INVOIC/PI_31005) | Prüfi | INVOIC | transaktionsdaten › empfaenger |
| [PI_31006](/schnittstellen/202610/pruefi/INVOIC/PI_31006) | Prüfi | INVOIC | transaktionsdaten › absender |
| [PI_31006](/schnittstellen/202610/pruefi/INVOIC/PI_31006) | Prüfi | INVOIC | transaktionsdaten › empfaenger |
| [PI_31007](/schnittstellen/202610/pruefi/INVOIC/PI_31007) | Prüfi | INVOIC | transaktionsdaten › absender |
| [PI_31007](/schnittstellen/202610/pruefi/INVOIC/PI_31007) | Prüfi | INVOIC | transaktionsdaten › empfaenger |
| [PI_31008](/schnittstellen/202610/pruefi/INVOIC/PI_31008) | Prüfi | INVOIC | transaktionsdaten › absender |
| [PI_31008](/schnittstellen/202610/pruefi/INVOIC/PI_31008) | Prüfi | INVOIC | transaktionsdaten › empfaenger |
| [PI_31009](/schnittstellen/202610/pruefi/INVOIC/PI_31009) | Prüfi | INVOIC | transaktionsdaten › absender |
| [PI_31009](/schnittstellen/202610/pruefi/INVOIC/PI_31009) | Prüfi | INVOIC | transaktionsdaten › empfaenger |
| [PI_31010](/schnittstellen/202610/pruefi/INVOIC/PI_31010) | Prüfi | INVOIC | transaktionsdaten › absender |
| [PI_31010](/schnittstellen/202610/pruefi/INVOIC/PI_31010) | Prüfi | INVOIC | transaktionsdaten › empfaenger |
| [PI_31011](/schnittstellen/202610/pruefi/INVOIC/PI_31011) | Prüfi | INVOIC | transaktionsdaten › absender |
| [PI_31011](/schnittstellen/202610/pruefi/INVOIC/PI_31011) | Prüfi | INVOIC | transaktionsdaten › empfaenger |
| [PI_33001](/schnittstellen/202610/pruefi/REMADV/PI_33001) | Prüfi | REMADV | transaktionsdaten › absender |
| [PI_33001](/schnittstellen/202610/pruefi/REMADV/PI_33001) | Prüfi | REMADV | transaktionsdaten › empfaenger |
| [PI_33002](/schnittstellen/202610/pruefi/REMADV/PI_33002) | Prüfi | REMADV | transaktionsdaten › absender |
| [PI_33002](/schnittstellen/202610/pruefi/REMADV/PI_33002) | Prüfi | REMADV | transaktionsdaten › empfaenger |
| [PI_33003](/schnittstellen/202610/pruefi/REMADV/PI_33003) | Prüfi | REMADV | transaktionsdaten › absender |
| [PI_33003](/schnittstellen/202610/pruefi/REMADV/PI_33003) | Prüfi | REMADV | transaktionsdaten › empfaenger |
| [PI_33004](/schnittstellen/202610/pruefi/REMADV/PI_33004) | Prüfi | REMADV | transaktionsdaten › absender |
| [PI_33004](/schnittstellen/202610/pruefi/REMADV/PI_33004) | Prüfi | REMADV | transaktionsdaten › empfaenger |
| [PI_35001](/schnittstellen/202610/pruefi/REQOTE/PI_35001) | Prüfi | REQOTE | transaktionsdaten › absender |
| [PI_35001](/schnittstellen/202610/pruefi/REQOTE/PI_35001) | Prüfi | REQOTE | transaktionsdaten › empfaenger |
| [PI_35002](/schnittstellen/202610/pruefi/REQOTE/PI_35002) | Prüfi | REQOTE | transaktionsdaten › absender |
| [PI_35002](/schnittstellen/202610/pruefi/REQOTE/PI_35002) | Prüfi | REQOTE | transaktionsdaten › empfaenger |
| [PI_35004](/schnittstellen/202610/pruefi/REQOTE/PI_35004) | Prüfi | REQOTE | transaktionsdaten › absender |
| [PI_35004](/schnittstellen/202610/pruefi/REQOTE/PI_35004) | Prüfi | REQOTE | transaktionsdaten › beteiligterMarktpartner |
| [PI_35004](/schnittstellen/202610/pruefi/REQOTE/PI_35004) | Prüfi | REQOTE | transaktionsdaten › empfaenger |
| [PI_37000](/schnittstellen/202610/pruefi/PARTIN/PI_37000) | Prüfi | PARTIN | transaktionsdaten › absender |
| [PI_37000](/schnittstellen/202610/pruefi/PARTIN/PI_37000) | Prüfi | PARTIN | transaktionsdaten › empfaenger |
| [PI_37001](/schnittstellen/202610/pruefi/PARTIN/PI_37001) | Prüfi | PARTIN | transaktionsdaten › absender |
| [PI_37001](/schnittstellen/202610/pruefi/PARTIN/PI_37001) | Prüfi | PARTIN | transaktionsdaten › empfaenger |
| [PI_37002](/schnittstellen/202610/pruefi/PARTIN/PI_37002) | Prüfi | PARTIN | transaktionsdaten › absender |
| [PI_37002](/schnittstellen/202610/pruefi/PARTIN/PI_37002) | Prüfi | PARTIN | transaktionsdaten › empfaenger |
| [PI_37008](/schnittstellen/202610/pruefi/PARTIN/PI_37008) | Prüfi | PARTIN | transaktionsdaten › absender |
| [PI_37008](/schnittstellen/202610/pruefi/PARTIN/PI_37008) | Prüfi | PARTIN | transaktionsdaten › empfaenger |
| [PI_37009](/schnittstellen/202610/pruefi/PARTIN/PI_37009) | Prüfi | PARTIN | transaktionsdaten › absender |
| [PI_37009](/schnittstellen/202610/pruefi/PARTIN/PI_37009) | Prüfi | PARTIN | transaktionsdaten › empfaenger |
| [PI_37010](/schnittstellen/202610/pruefi/PARTIN/PI_37010) | Prüfi | PARTIN | transaktionsdaten › absender |
| [PI_37010](/schnittstellen/202610/pruefi/PARTIN/PI_37010) | Prüfi | PARTIN | transaktionsdaten › empfaenger |
| [PI_37012](/schnittstellen/202610/pruefi/PARTIN/PI_37012) | Prüfi | PARTIN | transaktionsdaten › absender |
| [PI_37012](/schnittstellen/202610/pruefi/PARTIN/PI_37012) | Prüfi | PARTIN | transaktionsdaten › empfaenger |
| [PI_37013](/schnittstellen/202610/pruefi/PARTIN/PI_37013) | Prüfi | PARTIN | transaktionsdaten › absender |
| [PI_37013](/schnittstellen/202610/pruefi/PARTIN/PI_37013) | Prüfi | PARTIN | transaktionsdaten › empfaenger |
| [PI_37014](/schnittstellen/202610/pruefi/PARTIN/PI_37014) | Prüfi | PARTIN | transaktionsdaten › absender |
| [PI_37014](/schnittstellen/202610/pruefi/PARTIN/PI_37014) | Prüfi | PARTIN | transaktionsdaten › empfaenger |
| [PI_39000](/schnittstellen/202610/pruefi/ORDCHG/PI_39000) | Prüfi | ORDCHG | transaktionsdaten › absender |
| [PI_39000](/schnittstellen/202610/pruefi/ORDCHG/PI_39000) | Prüfi | ORDCHG | transaktionsdaten › empfaenger |
| [PI_39001](/schnittstellen/202610/pruefi/ORDCHG/PI_39001) | Prüfi | ORDCHG | transaktionsdaten › absender |
| [PI_39001](/schnittstellen/202610/pruefi/ORDCHG/PI_39001) | Prüfi | ORDCHG | transaktionsdaten › empfaenger |
| [PI_44001](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44001) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44001](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44001) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44002](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › marktrollen |
| [PI_44002](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |

*Weitere Verwendungen sind aus Platzgründen nicht aufgeführt.*

### rollencodetyp

793 Verwendung(en) in den Nachrichtentypen APERAK, COMDIS, IFTSTA, INSRPT, INVOIC, MSCONS, ORDCHG, ORDERS, ORDRSP, PARTIN, PRICAT, QUOTES, REMADV, REQOTE, UTILMD, UTILMD_GAS, UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_13002](/schnittstellen/202610/pruefi/MSCONS/PI_13002) | Prüfi | MSCONS | transaktionsdaten › absender |
| [PI_13002](/schnittstellen/202610/pruefi/MSCONS/PI_13002) | Prüfi | MSCONS | transaktionsdaten › empfaenger |
| [PI_13003](/schnittstellen/202610/pruefi/MSCONS/PI_13003) | Prüfi | MSCONS | transaktionsdaten › absender |
| [PI_13003](/schnittstellen/202610/pruefi/MSCONS/PI_13003) | Prüfi | MSCONS | transaktionsdaten › empfaenger |
| [PI_13006](/schnittstellen/202610/pruefi/MSCONS/PI_13006) | Prüfi | MSCONS | transaktionsdaten › absender |
| [PI_13006](/schnittstellen/202610/pruefi/MSCONS/PI_13006) | Prüfi | MSCONS | transaktionsdaten › empfaenger |
| [PI_13007](/schnittstellen/202610/pruefi/MSCONS/PI_13007) | Prüfi | MSCONS | transaktionsdaten › absender |
| [PI_13007](/schnittstellen/202610/pruefi/MSCONS/PI_13007) | Prüfi | MSCONS | transaktionsdaten › empfaenger |
| [PI_13008](/schnittstellen/202610/pruefi/MSCONS/PI_13008) | Prüfi | MSCONS | transaktionsdaten › absender |
| [PI_13008](/schnittstellen/202610/pruefi/MSCONS/PI_13008) | Prüfi | MSCONS | transaktionsdaten › empfaenger |
| [PI_13009](/schnittstellen/202610/pruefi/MSCONS/PI_13009) | Prüfi | MSCONS | transaktionsdaten › absender |
| [PI_13009](/schnittstellen/202610/pruefi/MSCONS/PI_13009) | Prüfi | MSCONS | transaktionsdaten › empfaenger |
| [PI_13010](/schnittstellen/202610/pruefi/MSCONS/PI_13010) | Prüfi | MSCONS | transaktionsdaten › absender |
| [PI_13010](/schnittstellen/202610/pruefi/MSCONS/PI_13010) | Prüfi | MSCONS | transaktionsdaten › empfaenger |
| [PI_13011](/schnittstellen/202610/pruefi/MSCONS/PI_13011) | Prüfi | MSCONS | transaktionsdaten › absender |
| [PI_13011](/schnittstellen/202610/pruefi/MSCONS/PI_13011) | Prüfi | MSCONS | transaktionsdaten › empfaenger |
| [PI_13015](/schnittstellen/202610/pruefi/MSCONS/PI_13015) | Prüfi | MSCONS | transaktionsdaten › absender |
| [PI_13015](/schnittstellen/202610/pruefi/MSCONS/PI_13015) | Prüfi | MSCONS | transaktionsdaten › empfaenger |
| [PI_13016](/schnittstellen/202610/pruefi/MSCONS/PI_13016) | Prüfi | MSCONS | transaktionsdaten › absender |
| [PI_13016](/schnittstellen/202610/pruefi/MSCONS/PI_13016) | Prüfi | MSCONS | transaktionsdaten › empfaenger |
| [PI_13017](/schnittstellen/202610/pruefi/MSCONS/PI_13017) | Prüfi | MSCONS | transaktionsdaten › absender |
| [PI_13017](/schnittstellen/202610/pruefi/MSCONS/PI_13017) | Prüfi | MSCONS | transaktionsdaten › empfaenger |
| [PI_13018](/schnittstellen/202610/pruefi/MSCONS/PI_13018) | Prüfi | MSCONS | transaktionsdaten › absender |
| [PI_13018](/schnittstellen/202610/pruefi/MSCONS/PI_13018) | Prüfi | MSCONS | transaktionsdaten › empfaenger |
| [PI_13019](/schnittstellen/202610/pruefi/MSCONS/PI_13019) | Prüfi | MSCONS | transaktionsdaten › absender |
| [PI_13019](/schnittstellen/202610/pruefi/MSCONS/PI_13019) | Prüfi | MSCONS | transaktionsdaten › empfaenger |
| [PI_13025](/schnittstellen/202610/pruefi/MSCONS/PI_13025) | Prüfi | MSCONS | transaktionsdaten › absender |
| [PI_13025](/schnittstellen/202610/pruefi/MSCONS/PI_13025) | Prüfi | MSCONS | transaktionsdaten › empfaenger |
| [PI_13027](/schnittstellen/202610/pruefi/MSCONS/PI_13027) | Prüfi | MSCONS | transaktionsdaten › absender |
| [PI_13027](/schnittstellen/202610/pruefi/MSCONS/PI_13027) | Prüfi | MSCONS | transaktionsdaten › empfaenger |
| [PI_13028](/schnittstellen/202610/pruefi/MSCONS/PI_13028) | Prüfi | MSCONS | transaktionsdaten › absender |
| [PI_13028](/schnittstellen/202610/pruefi/MSCONS/PI_13028) | Prüfi | MSCONS | transaktionsdaten › empfaenger |
| [PI_15001](/schnittstellen/202610/pruefi/QUOTES/PI_15001) | Prüfi | QUOTES | stammdaten › ANGEBOT › positionsdaten › beteiligterMarktpartner |
| [PI_15001](/schnittstellen/202610/pruefi/QUOTES/PI_15001) | Prüfi | QUOTES | transaktionsdaten › absender |
| [PI_15001](/schnittstellen/202610/pruefi/QUOTES/PI_15001) | Prüfi | QUOTES | transaktionsdaten › empfaenger |
| [PI_15003](/schnittstellen/202610/pruefi/QUOTES/PI_15003) | Prüfi | QUOTES | transaktionsdaten › absender |
| [PI_15003](/schnittstellen/202610/pruefi/QUOTES/PI_15003) | Prüfi | QUOTES | transaktionsdaten › empfaenger |
| [PI_15004](/schnittstellen/202610/pruefi/QUOTES/PI_15004) | Prüfi | QUOTES | transaktionsdaten › absender |
| [PI_15004](/schnittstellen/202610/pruefi/QUOTES/PI_15004) | Prüfi | QUOTES | transaktionsdaten › empfaenger |
| [PI_15005](/schnittstellen/202610/pruefi/QUOTES/PI_15005) | Prüfi | QUOTES | transaktionsdaten › absender |
| [PI_15005](/schnittstellen/202610/pruefi/QUOTES/PI_15005) | Prüfi | QUOTES | transaktionsdaten › empfaenger |
| [PI_17001](/schnittstellen/202610/pruefi/ORDERS/PI_17001) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17001](/schnittstellen/202610/pruefi/ORDERS/PI_17001) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17002](/schnittstellen/202610/pruefi/ORDERS/PI_17002) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17002](/schnittstellen/202610/pruefi/ORDERS/PI_17002) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17004](/schnittstellen/202610/pruefi/ORDERS/PI_17004) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17004](/schnittstellen/202610/pruefi/ORDERS/PI_17004) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17005](/schnittstellen/202610/pruefi/ORDERS/PI_17005) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17005](/schnittstellen/202610/pruefi/ORDERS/PI_17005) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17006](/schnittstellen/202610/pruefi/ORDERS/PI_17006) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17006](/schnittstellen/202610/pruefi/ORDERS/PI_17006) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17009](/schnittstellen/202610/pruefi/ORDERS/PI_17009) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17009](/schnittstellen/202610/pruefi/ORDERS/PI_17009) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17101](/schnittstellen/202610/pruefi/ORDERS/PI_17101) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17101](/schnittstellen/202610/pruefi/ORDERS/PI_17101) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17102](/schnittstellen/202610/pruefi/ORDERS/PI_17102) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17102](/schnittstellen/202610/pruefi/ORDERS/PI_17102) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17103](/schnittstellen/202610/pruefi/ORDERS/PI_17103) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17103](/schnittstellen/202610/pruefi/ORDERS/PI_17103) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17104](/schnittstellen/202610/pruefi/ORDERS/PI_17104) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17104](/schnittstellen/202610/pruefi/ORDERS/PI_17104) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17113](/schnittstellen/202610/pruefi/ORDERS/PI_17113) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17113](/schnittstellen/202610/pruefi/ORDERS/PI_17113) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17115](/schnittstellen/202610/pruefi/ORDERS/PI_17115) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17115](/schnittstellen/202610/pruefi/ORDERS/PI_17115) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17116](/schnittstellen/202610/pruefi/ORDERS/PI_17116) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17116](/schnittstellen/202610/pruefi/ORDERS/PI_17116) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17117](/schnittstellen/202610/pruefi/ORDERS/PI_17117) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17117](/schnittstellen/202610/pruefi/ORDERS/PI_17117) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17118](/schnittstellen/202610/pruefi/ORDERS/PI_17118) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17118](/schnittstellen/202610/pruefi/ORDERS/PI_17118) | Prüfi | ORDERS | transaktionsdaten › beteiligterMarktpartner |
| [PI_17118](/schnittstellen/202610/pruefi/ORDERS/PI_17118) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17120](/schnittstellen/202610/pruefi/ORDERS/PI_17120) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17120](/schnittstellen/202610/pruefi/ORDERS/PI_17120) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17121](/schnittstellen/202610/pruefi/ORDERS/PI_17121) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17121](/schnittstellen/202610/pruefi/ORDERS/PI_17121) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17122](/schnittstellen/202610/pruefi/ORDERS/PI_17122) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17122](/schnittstellen/202610/pruefi/ORDERS/PI_17122) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17123](/schnittstellen/202610/pruefi/ORDERS/PI_17123) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17123](/schnittstellen/202610/pruefi/ORDERS/PI_17123) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17126](/schnittstellen/202610/pruefi/ORDERS/PI_17126) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17126](/schnittstellen/202610/pruefi/ORDERS/PI_17126) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17128](/schnittstellen/202610/pruefi/ORDERS/PI_17128) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17128](/schnittstellen/202610/pruefi/ORDERS/PI_17128) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17129](/schnittstellen/202610/pruefi/ORDERS/PI_17129) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17129](/schnittstellen/202610/pruefi/ORDERS/PI_17129) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17130](/schnittstellen/202610/pruefi/ORDERS/PI_17130) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17130](/schnittstellen/202610/pruefi/ORDERS/PI_17130) | Prüfi | ORDERS | transaktionsdaten › beteiligterMarktpartner |
| [PI_17130](/schnittstellen/202610/pruefi/ORDERS/PI_17130) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17131](/schnittstellen/202610/pruefi/ORDERS/PI_17131) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17131](/schnittstellen/202610/pruefi/ORDERS/PI_17131) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17132](/schnittstellen/202610/pruefi/ORDERS/PI_17132) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17132](/schnittstellen/202610/pruefi/ORDERS/PI_17132) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17133](/schnittstellen/202610/pruefi/ORDERS/PI_17133) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17133](/schnittstellen/202610/pruefi/ORDERS/PI_17133) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17134](/schnittstellen/202610/pruefi/ORDERS/PI_17134) | Prüfi | ORDERS | stammdaten › MARKTLOKATION › marktrollen |
| [PI_17134](/schnittstellen/202610/pruefi/ORDERS/PI_17134) | Prüfi | ORDERS | stammdaten › TRANCHE › marktrollen |
| [PI_17134](/schnittstellen/202610/pruefi/ORDERS/PI_17134) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17134](/schnittstellen/202610/pruefi/ORDERS/PI_17134) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17135](/schnittstellen/202610/pruefi/ORDERS/PI_17135) | Prüfi | ORDERS | stammdaten › MARKTLOKATION › marktrollen |
| [PI_17135](/schnittstellen/202610/pruefi/ORDERS/PI_17135) | Prüfi | ORDERS | stammdaten › TRANCHE › marktrollen |
| [PI_17135](/schnittstellen/202610/pruefi/ORDERS/PI_17135) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17135](/schnittstellen/202610/pruefi/ORDERS/PI_17135) | Prüfi | ORDERS | transaktionsdaten › beteiligterMarktpartner |
| [PI_17135](/schnittstellen/202610/pruefi/ORDERS/PI_17135) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17201](/schnittstellen/202610/pruefi/ORDERS/PI_17201) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17201](/schnittstellen/202610/pruefi/ORDERS/PI_17201) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17202](/schnittstellen/202610/pruefi/ORDERS/PI_17202) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17202](/schnittstellen/202610/pruefi/ORDERS/PI_17202) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17203](/schnittstellen/202610/pruefi/ORDERS/PI_17203) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17203](/schnittstellen/202610/pruefi/ORDERS/PI_17203) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_17204](/schnittstellen/202610/pruefi/ORDERS/PI_17204) | Prüfi | ORDERS | transaktionsdaten › absender |
| [PI_17204](/schnittstellen/202610/pruefi/ORDERS/PI_17204) | Prüfi | ORDERS | transaktionsdaten › empfaenger |
| [PI_19001](/schnittstellen/202610/pruefi/ORDRSP/PI_19001) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19001](/schnittstellen/202610/pruefi/ORDRSP/PI_19001) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19002](/schnittstellen/202610/pruefi/ORDRSP/PI_19002) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19002](/schnittstellen/202610/pruefi/ORDRSP/PI_19002) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19003](/schnittstellen/202610/pruefi/ORDRSP/PI_19003) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19003](/schnittstellen/202610/pruefi/ORDRSP/PI_19003) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19004](/schnittstellen/202610/pruefi/ORDRSP/PI_19004) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19004](/schnittstellen/202610/pruefi/ORDRSP/PI_19004) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19005](/schnittstellen/202610/pruefi/ORDRSP/PI_19005) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19005](/schnittstellen/202610/pruefi/ORDRSP/PI_19005) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19006](/schnittstellen/202610/pruefi/ORDRSP/PI_19006) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19006](/schnittstellen/202610/pruefi/ORDRSP/PI_19006) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19007](/schnittstellen/202610/pruefi/ORDRSP/PI_19007) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19007](/schnittstellen/202610/pruefi/ORDRSP/PI_19007) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19009](/schnittstellen/202610/pruefi/ORDRSP/PI_19009) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19009](/schnittstellen/202610/pruefi/ORDRSP/PI_19009) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19010](/schnittstellen/202610/pruefi/ORDRSP/PI_19010) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19010](/schnittstellen/202610/pruefi/ORDRSP/PI_19010) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19011](/schnittstellen/202610/pruefi/ORDRSP/PI_19011) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19011](/schnittstellen/202610/pruefi/ORDRSP/PI_19011) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19012](/schnittstellen/202610/pruefi/ORDRSP/PI_19012) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19012](/schnittstellen/202610/pruefi/ORDRSP/PI_19012) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19013](/schnittstellen/202610/pruefi/ORDRSP/PI_19013) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19013](/schnittstellen/202610/pruefi/ORDRSP/PI_19013) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19014](/schnittstellen/202610/pruefi/ORDRSP/PI_19014) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19014](/schnittstellen/202610/pruefi/ORDRSP/PI_19014) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19015](/schnittstellen/202610/pruefi/ORDRSP/PI_19015) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19015](/schnittstellen/202610/pruefi/ORDRSP/PI_19015) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19016](/schnittstellen/202610/pruefi/ORDRSP/PI_19016) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19016](/schnittstellen/202610/pruefi/ORDRSP/PI_19016) | Prüfi | ORDRSP | transaktionsdaten › beteiligterMarktpartner |
| [PI_19016](/schnittstellen/202610/pruefi/ORDRSP/PI_19016) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19101](/schnittstellen/202610/pruefi/ORDRSP/PI_19101) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19101](/schnittstellen/202610/pruefi/ORDRSP/PI_19101) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19102](/schnittstellen/202610/pruefi/ORDRSP/PI_19102) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19102](/schnittstellen/202610/pruefi/ORDRSP/PI_19102) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19103](/schnittstellen/202610/pruefi/ORDRSP/PI_19103) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19103](/schnittstellen/202610/pruefi/ORDRSP/PI_19103) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19104](/schnittstellen/202610/pruefi/ORDRSP/PI_19104) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19104](/schnittstellen/202610/pruefi/ORDRSP/PI_19104) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19114](/schnittstellen/202610/pruefi/ORDRSP/PI_19114) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19114](/schnittstellen/202610/pruefi/ORDRSP/PI_19114) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19116](/schnittstellen/202610/pruefi/ORDRSP/PI_19116) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19116](/schnittstellen/202610/pruefi/ORDRSP/PI_19116) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19117](/schnittstellen/202610/pruefi/ORDRSP/PI_19117) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19117](/schnittstellen/202610/pruefi/ORDRSP/PI_19117) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19118](/schnittstellen/202610/pruefi/ORDRSP/PI_19118) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19118](/schnittstellen/202610/pruefi/ORDRSP/PI_19118) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19119](/schnittstellen/202610/pruefi/ORDRSP/PI_19119) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19119](/schnittstellen/202610/pruefi/ORDRSP/PI_19119) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19121](/schnittstellen/202610/pruefi/ORDRSP/PI_19121) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19121](/schnittstellen/202610/pruefi/ORDRSP/PI_19121) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19123](/schnittstellen/202610/pruefi/ORDRSP/PI_19123) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19123](/schnittstellen/202610/pruefi/ORDRSP/PI_19123) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19124](/schnittstellen/202610/pruefi/ORDRSP/PI_19124) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19124](/schnittstellen/202610/pruefi/ORDRSP/PI_19124) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19128](/schnittstellen/202610/pruefi/ORDRSP/PI_19128) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19128](/schnittstellen/202610/pruefi/ORDRSP/PI_19128) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19129](/schnittstellen/202610/pruefi/ORDRSP/PI_19129) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19129](/schnittstellen/202610/pruefi/ORDRSP/PI_19129) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19133](/schnittstellen/202610/pruefi/ORDRSP/PI_19133) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19133](/schnittstellen/202610/pruefi/ORDRSP/PI_19133) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19301](/schnittstellen/202610/pruefi/ORDRSP/PI_19301) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19301](/schnittstellen/202610/pruefi/ORDRSP/PI_19301) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_19302](/schnittstellen/202610/pruefi/ORDRSP/PI_19302) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19302](/schnittstellen/202610/pruefi/ORDRSP/PI_19302) | Prüfi | ORDRSP | transaktionsdaten › empfaenger |
| [PI_21007](/schnittstellen/202610/pruefi/IFTSTA/PI_21007) | Prüfi | IFTSTA | stammdaten › MESSLOKATION › marktrollen |
| [PI_21007](/schnittstellen/202610/pruefi/IFTSTA/PI_21007) | Prüfi | IFTSTA | transaktionsdaten › absender |
| [PI_21007](/schnittstellen/202610/pruefi/IFTSTA/PI_21007) | Prüfi | IFTSTA | transaktionsdaten › empfaenger |
| [PI_21009](/schnittstellen/202610/pruefi/IFTSTA/PI_21009) | Prüfi | IFTSTA | transaktionsdaten › absender |
| [PI_21009](/schnittstellen/202610/pruefi/IFTSTA/PI_21009) | Prüfi | IFTSTA | transaktionsdaten › empfaenger |
| [PI_21010](/schnittstellen/202610/pruefi/IFTSTA/PI_21010) | Prüfi | IFTSTA | transaktionsdaten › absender |
| [PI_21010](/schnittstellen/202610/pruefi/IFTSTA/PI_21010) | Prüfi | IFTSTA | transaktionsdaten › empfaenger |
| [PI_21011](/schnittstellen/202610/pruefi/IFTSTA/PI_21011) | Prüfi | IFTSTA | transaktionsdaten › absender |
| [PI_21011](/schnittstellen/202610/pruefi/IFTSTA/PI_21011) | Prüfi | IFTSTA | transaktionsdaten › empfaenger |
| [PI_21012](/schnittstellen/202610/pruefi/IFTSTA/PI_21012) | Prüfi | IFTSTA | transaktionsdaten › absender |
| [PI_21012](/schnittstellen/202610/pruefi/IFTSTA/PI_21012) | Prüfi | IFTSTA | transaktionsdaten › empfaenger |
| [PI_21013](/schnittstellen/202610/pruefi/IFTSTA/PI_21013) | Prüfi | IFTSTA | transaktionsdaten › absender |
| [PI_21013](/schnittstellen/202610/pruefi/IFTSTA/PI_21013) | Prüfi | IFTSTA | transaktionsdaten › empfaenger |
| [PI_21018](/schnittstellen/202610/pruefi/IFTSTA/PI_21018) | Prüfi | IFTSTA | stammdaten › MESSLOKATION › marktrollen |
| [PI_21018](/schnittstellen/202610/pruefi/IFTSTA/PI_21018) | Prüfi | IFTSTA | transaktionsdaten › absender |
| [PI_21018](/schnittstellen/202610/pruefi/IFTSTA/PI_21018) | Prüfi | IFTSTA | transaktionsdaten › empfaenger |
| [PI_21025](/schnittstellen/202610/pruefi/IFTSTA/PI_21025) | Prüfi | IFTSTA | transaktionsdaten › absender |
| [PI_21025](/schnittstellen/202610/pruefi/IFTSTA/PI_21025) | Prüfi | IFTSTA | transaktionsdaten › empfaenger |
| [PI_21027](/schnittstellen/202610/pruefi/IFTSTA/PI_21027) | Prüfi | IFTSTA | transaktionsdaten › absender |
| [PI_21027](/schnittstellen/202610/pruefi/IFTSTA/PI_21027) | Prüfi | IFTSTA | transaktionsdaten › empfaenger |
| [PI_21028](/schnittstellen/202610/pruefi/IFTSTA/PI_21028) | Prüfi | IFTSTA | transaktionsdaten › absender |
| [PI_21028](/schnittstellen/202610/pruefi/IFTSTA/PI_21028) | Prüfi | IFTSTA | transaktionsdaten › empfaenger |
| [PI_21029](/schnittstellen/202610/pruefi/IFTSTA/PI_21029) | Prüfi | IFTSTA | transaktionsdaten › absender |
| [PI_21029](/schnittstellen/202610/pruefi/IFTSTA/PI_21029) | Prüfi | IFTSTA | transaktionsdaten › empfaenger |
| [PI_21030](/schnittstellen/202610/pruefi/IFTSTA/PI_21030) | Prüfi | IFTSTA | transaktionsdaten › absender |
| [PI_21030](/schnittstellen/202610/pruefi/IFTSTA/PI_21030) | Prüfi | IFTSTA | transaktionsdaten › empfaenger |
| [PI_21031](/schnittstellen/202610/pruefi/IFTSTA/PI_21031) | Prüfi | IFTSTA | transaktionsdaten › absender |
| [PI_21031](/schnittstellen/202610/pruefi/IFTSTA/PI_21031) | Prüfi | IFTSTA | transaktionsdaten › empfaenger |
| [PI_21032](/schnittstellen/202610/pruefi/IFTSTA/PI_21032) | Prüfi | IFTSTA | transaktionsdaten › absender |
| [PI_21032](/schnittstellen/202610/pruefi/IFTSTA/PI_21032) | Prüfi | IFTSTA | transaktionsdaten › empfaenger |
| [PI_21033](/schnittstellen/202610/pruefi/IFTSTA/PI_21033) | Prüfi | IFTSTA | transaktionsdaten › absender |
| [PI_21033](/schnittstellen/202610/pruefi/IFTSTA/PI_21033) | Prüfi | IFTSTA | transaktionsdaten › empfaenger |
| [PI_21035](/schnittstellen/202610/pruefi/IFTSTA/PI_21035) | Prüfi | IFTSTA | transaktionsdaten › absender |
| [PI_21035](/schnittstellen/202610/pruefi/IFTSTA/PI_21035) | Prüfi | IFTSTA | transaktionsdaten › empfaenger |
| [PI_21036](/schnittstellen/202610/pruefi/IFTSTA/PI_21036) | Prüfi | IFTSTA | transaktionsdaten › absender |
| [PI_21036](/schnittstellen/202610/pruefi/IFTSTA/PI_21036) | Prüfi | IFTSTA | transaktionsdaten › empfaenger |
| [PI_21039](/schnittstellen/202610/pruefi/IFTSTA/PI_21039) | Prüfi | IFTSTA | transaktionsdaten › absender |
| [PI_21039](/schnittstellen/202610/pruefi/IFTSTA/PI_21039) | Prüfi | IFTSTA | transaktionsdaten › empfaenger |
| [PI_21040](/schnittstellen/202610/pruefi/IFTSTA/PI_21040) | Prüfi | IFTSTA | transaktionsdaten › absender |
| [PI_21040](/schnittstellen/202610/pruefi/IFTSTA/PI_21040) | Prüfi | IFTSTA | transaktionsdaten › empfaenger |
| [PI_21043](/schnittstellen/202610/pruefi/IFTSTA/PI_21043) | Prüfi | IFTSTA | transaktionsdaten › absender |
| [PI_21043](/schnittstellen/202610/pruefi/IFTSTA/PI_21043) | Prüfi | IFTSTA | transaktionsdaten › empfaenger |
| [PI_21044](/schnittstellen/202610/pruefi/IFTSTA/PI_21044) | Prüfi | IFTSTA | transaktionsdaten › absender |
| [PI_21044](/schnittstellen/202610/pruefi/IFTSTA/PI_21044) | Prüfi | IFTSTA | transaktionsdaten › empfaenger |
| [PI_21045](/schnittstellen/202610/pruefi/IFTSTA/PI_21045) | Prüfi | IFTSTA | transaktionsdaten › absender |
| [PI_21045](/schnittstellen/202610/pruefi/IFTSTA/PI_21045) | Prüfi | IFTSTA | transaktionsdaten › empfaenger |
| [PI_21047](/schnittstellen/202610/pruefi/IFTSTA/PI_21047) | Prüfi | IFTSTA | transaktionsdaten › absender |
| [PI_21047](/schnittstellen/202610/pruefi/IFTSTA/PI_21047) | Prüfi | IFTSTA | transaktionsdaten › empfaenger |
| [PI_23001](/schnittstellen/202610/pruefi/INSRPT/PI_23001) | Prüfi | INSRPT | transaktionsdaten › absender |
| [PI_23001](/schnittstellen/202610/pruefi/INSRPT/PI_23001) | Prüfi | INSRPT | transaktionsdaten › empfaenger |
| [PI_23003](/schnittstellen/202610/pruefi/INSRPT/PI_23003) | Prüfi | INSRPT | transaktionsdaten › absender |
| [PI_23003](/schnittstellen/202610/pruefi/INSRPT/PI_23003) | Prüfi | INSRPT | transaktionsdaten › empfaenger |
| [PI_23004](/schnittstellen/202610/pruefi/INSRPT/PI_23004) | Prüfi | INSRPT | transaktionsdaten › absender |
| [PI_23004](/schnittstellen/202610/pruefi/INSRPT/PI_23004) | Prüfi | INSRPT | transaktionsdaten › empfaenger |
| [PI_23005](/schnittstellen/202610/pruefi/INSRPT/PI_23005) | Prüfi | INSRPT | transaktionsdaten › absender |
| [PI_23005](/schnittstellen/202610/pruefi/INSRPT/PI_23005) | Prüfi | INSRPT | transaktionsdaten › empfaenger |
| [PI_23008](/schnittstellen/202610/pruefi/INSRPT/PI_23008) | Prüfi | INSRPT | transaktionsdaten › absender |
| [PI_23008](/schnittstellen/202610/pruefi/INSRPT/PI_23008) | Prüfi | INSRPT | transaktionsdaten › empfaenger |
| [PI_23009](/schnittstellen/202610/pruefi/INSRPT/PI_23009) | Prüfi | INSRPT | transaktionsdaten › absender |
| [PI_23009](/schnittstellen/202610/pruefi/INSRPT/PI_23009) | Prüfi | INSRPT | transaktionsdaten › empfaenger |
| [PI_23011](/schnittstellen/202610/pruefi/INSRPT/PI_23011) | Prüfi | INSRPT | transaktionsdaten › absender |
| [PI_23011](/schnittstellen/202610/pruefi/INSRPT/PI_23011) | Prüfi | INSRPT | transaktionsdaten › empfaenger |
| [PI_23012](/schnittstellen/202610/pruefi/INSRPT/PI_23012) | Prüfi | INSRPT | transaktionsdaten › absender |
| [PI_23012](/schnittstellen/202610/pruefi/INSRPT/PI_23012) | Prüfi | INSRPT | transaktionsdaten › empfaenger |
| [PI_25001](/schnittstellen/202610/pruefi/UTILTS/PI_25001) | Prüfi | UTILTS | transaktionsdaten › absender |
| [PI_25001](/schnittstellen/202610/pruefi/UTILTS/PI_25001) | Prüfi | UTILTS | transaktionsdaten › empfaenger |
| [PI_25004](/schnittstellen/202610/pruefi/UTILTS/PI_25004) | Prüfi | UTILTS | transaktionsdaten › absender |
| [PI_25004](/schnittstellen/202610/pruefi/UTILTS/PI_25004) | Prüfi | UTILTS | transaktionsdaten › empfaenger |
| [PI_25005](/schnittstellen/202610/pruefi/UTILTS/PI_25005) | Prüfi | UTILTS | transaktionsdaten › absender |
| [PI_25005](/schnittstellen/202610/pruefi/UTILTS/PI_25005) | Prüfi | UTILTS | transaktionsdaten › empfaenger |
| [PI_25006](/schnittstellen/202610/pruefi/UTILTS/PI_25006) | Prüfi | UTILTS | transaktionsdaten › absender |
| [PI_25006](/schnittstellen/202610/pruefi/UTILTS/PI_25006) | Prüfi | UTILTS | transaktionsdaten › empfaenger |
| [PI_25007](/schnittstellen/202610/pruefi/UTILTS/PI_25007) | Prüfi | UTILTS | transaktionsdaten › absender |
| [PI_25007](/schnittstellen/202610/pruefi/UTILTS/PI_25007) | Prüfi | UTILTS | transaktionsdaten › empfaenger |
| [PI_25008](/schnittstellen/202610/pruefi/UTILTS/PI_25008) | Prüfi | UTILTS | transaktionsdaten › absender |
| [PI_25008](/schnittstellen/202610/pruefi/UTILTS/PI_25008) | Prüfi | UTILTS | transaktionsdaten › empfaenger |
| [PI_25009](/schnittstellen/202610/pruefi/UTILTS/PI_25009) | Prüfi | UTILTS | transaktionsdaten › absender |
| [PI_25009](/schnittstellen/202610/pruefi/UTILTS/PI_25009) | Prüfi | UTILTS | transaktionsdaten › empfaenger |
| [PI_25010](/schnittstellen/202610/pruefi/UTILTS/PI_25010) | Prüfi | UTILTS | transaktionsdaten › absender |
| [PI_25010](/schnittstellen/202610/pruefi/UTILTS/PI_25010) | Prüfi | UTILTS | transaktionsdaten › empfaenger |
| [PI_27002](/schnittstellen/202610/pruefi/PRICAT/PI_27002) | Prüfi | PRICAT | transaktionsdaten › absender |
| [PI_27002](/schnittstellen/202610/pruefi/PRICAT/PI_27002) | Prüfi | PRICAT | transaktionsdaten › empfaenger |
| [PI_27003](/schnittstellen/202610/pruefi/PRICAT/PI_27003) | Prüfi | PRICAT | transaktionsdaten › absender |
| [PI_27003](/schnittstellen/202610/pruefi/PRICAT/PI_27003) | Prüfi | PRICAT | transaktionsdaten › empfaenger |
| [PI_29001](/schnittstellen/202610/pruefi/COMDIS/PI_29001) | Prüfi | COMDIS | transaktionsdaten › absender |
| [PI_29001](/schnittstellen/202610/pruefi/COMDIS/PI_29001) | Prüfi | COMDIS | transaktionsdaten › empfaenger |
| [PI_29002](/schnittstellen/202610/pruefi/COMDIS/PI_29002) | Prüfi | COMDIS | transaktionsdaten › absender |
| [PI_29002](/schnittstellen/202610/pruefi/COMDIS/PI_29002) | Prüfi | COMDIS | transaktionsdaten › empfaenger |
| [PI_31001](/schnittstellen/202610/pruefi/INVOIC/PI_31001) | Prüfi | INVOIC | transaktionsdaten › absender |
| [PI_31001](/schnittstellen/202610/pruefi/INVOIC/PI_31001) | Prüfi | INVOIC | transaktionsdaten › empfaenger |
| [PI_31002](/schnittstellen/202610/pruefi/INVOIC/PI_31002) | Prüfi | INVOIC | transaktionsdaten › absender |
| [PI_31002](/schnittstellen/202610/pruefi/INVOIC/PI_31002) | Prüfi | INVOIC | transaktionsdaten › empfaenger |
| [PI_31003](/schnittstellen/202610/pruefi/INVOIC/PI_31003) | Prüfi | INVOIC | transaktionsdaten › absender |
| [PI_31003](/schnittstellen/202610/pruefi/INVOIC/PI_31003) | Prüfi | INVOIC | transaktionsdaten › empfaenger |
| [PI_31004](/schnittstellen/202610/pruefi/INVOIC/PI_31004) | Prüfi | INVOIC | transaktionsdaten › absender |
| [PI_31004](/schnittstellen/202610/pruefi/INVOIC/PI_31004) | Prüfi | INVOIC | transaktionsdaten › empfaenger |
| [PI_31005](/schnittstellen/202610/pruefi/INVOIC/PI_31005) | Prüfi | INVOIC | transaktionsdaten › absender |
| [PI_31005](/schnittstellen/202610/pruefi/INVOIC/PI_31005) | Prüfi | INVOIC | transaktionsdaten › empfaenger |
| [PI_31006](/schnittstellen/202610/pruefi/INVOIC/PI_31006) | Prüfi | INVOIC | transaktionsdaten › absender |
| [PI_31006](/schnittstellen/202610/pruefi/INVOIC/PI_31006) | Prüfi | INVOIC | transaktionsdaten › empfaenger |
| [PI_31007](/schnittstellen/202610/pruefi/INVOIC/PI_31007) | Prüfi | INVOIC | transaktionsdaten › absender |
| [PI_31007](/schnittstellen/202610/pruefi/INVOIC/PI_31007) | Prüfi | INVOIC | transaktionsdaten › empfaenger |
| [PI_31008](/schnittstellen/202610/pruefi/INVOIC/PI_31008) | Prüfi | INVOIC | transaktionsdaten › absender |
| [PI_31008](/schnittstellen/202610/pruefi/INVOIC/PI_31008) | Prüfi | INVOIC | transaktionsdaten › empfaenger |
| [PI_31009](/schnittstellen/202610/pruefi/INVOIC/PI_31009) | Prüfi | INVOIC | transaktionsdaten › absender |
| [PI_31009](/schnittstellen/202610/pruefi/INVOIC/PI_31009) | Prüfi | INVOIC | transaktionsdaten › empfaenger |
| [PI_31010](/schnittstellen/202610/pruefi/INVOIC/PI_31010) | Prüfi | INVOIC | transaktionsdaten › absender |
| [PI_31010](/schnittstellen/202610/pruefi/INVOIC/PI_31010) | Prüfi | INVOIC | transaktionsdaten › empfaenger |
| [PI_31011](/schnittstellen/202610/pruefi/INVOIC/PI_31011) | Prüfi | INVOIC | transaktionsdaten › absender |
| [PI_31011](/schnittstellen/202610/pruefi/INVOIC/PI_31011) | Prüfi | INVOIC | transaktionsdaten › empfaenger |
| [PI_33001](/schnittstellen/202610/pruefi/REMADV/PI_33001) | Prüfi | REMADV | transaktionsdaten › absender |
| [PI_33001](/schnittstellen/202610/pruefi/REMADV/PI_33001) | Prüfi | REMADV | transaktionsdaten › empfaenger |
| [PI_33002](/schnittstellen/202610/pruefi/REMADV/PI_33002) | Prüfi | REMADV | transaktionsdaten › absender |
| [PI_33002](/schnittstellen/202610/pruefi/REMADV/PI_33002) | Prüfi | REMADV | transaktionsdaten › empfaenger |
| [PI_33003](/schnittstellen/202610/pruefi/REMADV/PI_33003) | Prüfi | REMADV | transaktionsdaten › absender |
| [PI_33003](/schnittstellen/202610/pruefi/REMADV/PI_33003) | Prüfi | REMADV | transaktionsdaten › empfaenger |
| [PI_33004](/schnittstellen/202610/pruefi/REMADV/PI_33004) | Prüfi | REMADV | transaktionsdaten › absender |
| [PI_33004](/schnittstellen/202610/pruefi/REMADV/PI_33004) | Prüfi | REMADV | transaktionsdaten › empfaenger |
| [PI_35001](/schnittstellen/202610/pruefi/REQOTE/PI_35001) | Prüfi | REQOTE | transaktionsdaten › absender |
| [PI_35001](/schnittstellen/202610/pruefi/REQOTE/PI_35001) | Prüfi | REQOTE | transaktionsdaten › empfaenger |
| [PI_35002](/schnittstellen/202610/pruefi/REQOTE/PI_35002) | Prüfi | REQOTE | transaktionsdaten › absender |
| [PI_35002](/schnittstellen/202610/pruefi/REQOTE/PI_35002) | Prüfi | REQOTE | transaktionsdaten › empfaenger |
| [PI_35004](/schnittstellen/202610/pruefi/REQOTE/PI_35004) | Prüfi | REQOTE | transaktionsdaten › absender |
| [PI_35004](/schnittstellen/202610/pruefi/REQOTE/PI_35004) | Prüfi | REQOTE | transaktionsdaten › beteiligterMarktpartner |
| [PI_35004](/schnittstellen/202610/pruefi/REQOTE/PI_35004) | Prüfi | REQOTE | transaktionsdaten › empfaenger |
| [PI_37000](/schnittstellen/202610/pruefi/PARTIN/PI_37000) | Prüfi | PARTIN | transaktionsdaten › absender |
| [PI_37000](/schnittstellen/202610/pruefi/PARTIN/PI_37000) | Prüfi | PARTIN | transaktionsdaten › empfaenger |
| [PI_37001](/schnittstellen/202610/pruefi/PARTIN/PI_37001) | Prüfi | PARTIN | transaktionsdaten › absender |
| [PI_37001](/schnittstellen/202610/pruefi/PARTIN/PI_37001) | Prüfi | PARTIN | transaktionsdaten › empfaenger |
| [PI_37002](/schnittstellen/202610/pruefi/PARTIN/PI_37002) | Prüfi | PARTIN | transaktionsdaten › absender |
| [PI_37002](/schnittstellen/202610/pruefi/PARTIN/PI_37002) | Prüfi | PARTIN | transaktionsdaten › empfaenger |
| [PI_37008](/schnittstellen/202610/pruefi/PARTIN/PI_37008) | Prüfi | PARTIN | transaktionsdaten › absender |
| [PI_37008](/schnittstellen/202610/pruefi/PARTIN/PI_37008) | Prüfi | PARTIN | transaktionsdaten › empfaenger |
| [PI_37009](/schnittstellen/202610/pruefi/PARTIN/PI_37009) | Prüfi | PARTIN | transaktionsdaten › absender |
| [PI_37009](/schnittstellen/202610/pruefi/PARTIN/PI_37009) | Prüfi | PARTIN | transaktionsdaten › empfaenger |
| [PI_37010](/schnittstellen/202610/pruefi/PARTIN/PI_37010) | Prüfi | PARTIN | transaktionsdaten › absender |
| [PI_37010](/schnittstellen/202610/pruefi/PARTIN/PI_37010) | Prüfi | PARTIN | transaktionsdaten › empfaenger |
| [PI_37012](/schnittstellen/202610/pruefi/PARTIN/PI_37012) | Prüfi | PARTIN | transaktionsdaten › absender |
| [PI_37012](/schnittstellen/202610/pruefi/PARTIN/PI_37012) | Prüfi | PARTIN | transaktionsdaten › empfaenger |
| [PI_37013](/schnittstellen/202610/pruefi/PARTIN/PI_37013) | Prüfi | PARTIN | transaktionsdaten › absender |
| [PI_37013](/schnittstellen/202610/pruefi/PARTIN/PI_37013) | Prüfi | PARTIN | transaktionsdaten › empfaenger |
| [PI_37014](/schnittstellen/202610/pruefi/PARTIN/PI_37014) | Prüfi | PARTIN | transaktionsdaten › absender |
| [PI_37014](/schnittstellen/202610/pruefi/PARTIN/PI_37014) | Prüfi | PARTIN | transaktionsdaten › empfaenger |
| [PI_39000](/schnittstellen/202610/pruefi/ORDCHG/PI_39000) | Prüfi | ORDCHG | transaktionsdaten › absender |
| [PI_39000](/schnittstellen/202610/pruefi/ORDCHG/PI_39000) | Prüfi | ORDCHG | transaktionsdaten › empfaenger |
| [PI_39001](/schnittstellen/202610/pruefi/ORDCHG/PI_39001) | Prüfi | ORDCHG | transaktionsdaten › absender |
| [PI_39001](/schnittstellen/202610/pruefi/ORDCHG/PI_39001) | Prüfi | ORDCHG | transaktionsdaten › empfaenger |
| [PI_44001](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44001) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44001](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44001) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44002](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44002](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44003](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44003) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44003](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44003) | Prüfi | UTILMD_GAS | transaktionsdaten › beteiligterMarktpartner |
| [PI_44003](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44003) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44004](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44004) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44004](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44004) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44005](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44005) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44005](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44005) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44006](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44006) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44006](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44006) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44007](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44007) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44007](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44007) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44008](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44008) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44008](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44008) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44009](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44009) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44009](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44009) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44010](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44010) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44010](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44010) | Prüfi | UTILMD_GAS | transaktionsdaten › beteiligterMarktpartner |
| [PI_44010](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44010) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44011](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44011) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44011](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44011) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44012](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44012) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44012](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44012) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44013](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44013](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44014](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44014](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44015](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44015) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44015](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44015) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44016](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44016) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44016](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44016) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44017](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44017) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44017](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44017) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44018](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44018) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44018](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44018) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44019](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44019) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44019](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44019) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44020](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44020) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44020](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44020) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44021](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44021) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44021](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44021) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44022](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44022) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44022](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44022) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44023](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44023) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44023](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44023) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44024](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44024) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44024](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44024) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44035](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44035) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44035](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44035) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44036](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44036) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44036](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44036) | Prüfi | UTILMD_GAS | transaktionsdaten › beteiligterMarktpartner |
| [PI_44036](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44036) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44037](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44037) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44037](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44037) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44038](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44038) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44038](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44038) | Prüfi | UTILMD_GAS | transaktionsdaten › beteiligterMarktpartner |
| [PI_44038](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44038) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44039](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44039) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44039](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44039) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44040](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44040) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44040](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44040) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44041](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44041) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44041](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44041) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44042](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44042) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44042](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44042) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44043](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44043) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44043](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44043) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44044](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44044) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44044](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44044) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44052](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44052) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44052](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44052) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44053](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44053) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44053](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44053) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44060](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44060) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44060](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44060) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44101](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44101) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44101](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44101) | Prüfi | UTILMD_GAS | transaktionsdaten › beteiligterMarktpartner |
| [PI_44101](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44101) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44102](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44102) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44102](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44102) | Prüfi | UTILMD_GAS | transaktionsdaten › beteiligterMarktpartner |
| [PI_44102](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44102) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44103](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44103) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44103](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44103) | Prüfi | UTILMD_GAS | transaktionsdaten › beteiligterMarktpartner |
| [PI_44103](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44103) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44104](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44104) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44104](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44104) | Prüfi | UTILMD_GAS | transaktionsdaten › beteiligterMarktpartner |
| [PI_44104](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44104) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44109](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44109) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44109](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44109) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44111](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44111) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44111](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44111) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44112](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44112) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44112](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44112) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44113](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44113) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44113](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44113) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44115](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44115) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44115](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44115) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44116](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44116) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44116](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44116) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44117](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44117) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44117](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44117) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44119](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44119) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44119](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44119) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44120](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44120) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44120](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44120) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44121](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44121) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44121](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44121) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44123](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44123) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44123](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44123) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44124](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44124) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44124](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44124) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44137](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44137) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44137](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44137) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44138](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44138) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44138](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44138) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44139](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44139) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44139](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44139) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44140](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44140) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44140](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44140) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44142](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44142) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44142](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44142) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44143](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44143) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44143](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44143) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44145](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44145) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44145](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44145) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44146](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44146) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44146](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44146) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44147](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44147) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44147](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44147) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44148](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44148) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44148](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44148) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44149](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44149) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44149](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44149) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44150](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44150) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44150](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44150) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44151](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44151) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44151](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44151) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44152](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44152) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44152](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44152) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44156](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44156) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44156](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44156) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44157](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44157) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44157](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44157) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44159](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44159) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44159](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44159) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44160](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44160) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44160](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44160) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44161](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44161) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44161](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44161) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44162](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44162) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44162](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44162) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44163](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44163) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44163](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44163) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44164](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44164) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44164](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44164) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44165](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44165) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44165](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44165) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44166](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44166) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44166](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44166) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44167](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44167) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44167](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44167) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44168](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44168](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44175](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44175) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44175](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44175) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44176](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44176) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44176](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44176) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44180](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44180) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44180](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44180) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44181](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44181) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44181](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44181) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |
| [PI_44182](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44182) | Prüfi | UTILMD_GAS | transaktionsdaten › absender |
| [PI_44182](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44182) | Prüfi | UTILMD_GAS | transaktionsdaten › empfaenger |

*Weitere Verwendungen sind aus Platzgründen nicht aufgeführt.*

### umsatzsteuerId

31 Verwendung(en) in den Nachrichtentypen INVOIC, PARTIN.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_31001](/schnittstellen/202610/pruefi/INVOIC/PI_31001) | Prüfi | INVOIC | transaktionsdaten › absender |
| [PI_31001](/schnittstellen/202610/pruefi/INVOIC/PI_31001) | Prüfi | INVOIC | transaktionsdaten › empfaenger |
| [PI_31002](/schnittstellen/202610/pruefi/INVOIC/PI_31002) | Prüfi | INVOIC | transaktionsdaten › absender |
| [PI_31002](/schnittstellen/202610/pruefi/INVOIC/PI_31002) | Prüfi | INVOIC | transaktionsdaten › empfaenger |
| [PI_31003](/schnittstellen/202610/pruefi/INVOIC/PI_31003) | Prüfi | INVOIC | transaktionsdaten › absender |
| [PI_31003](/schnittstellen/202610/pruefi/INVOIC/PI_31003) | Prüfi | INVOIC | transaktionsdaten › empfaenger |
| [PI_31004](/schnittstellen/202610/pruefi/INVOIC/PI_31004) | Prüfi | INVOIC | transaktionsdaten › absender |
| [PI_31004](/schnittstellen/202610/pruefi/INVOIC/PI_31004) | Prüfi | INVOIC | transaktionsdaten › empfaenger |
| [PI_31005](/schnittstellen/202610/pruefi/INVOIC/PI_31005) | Prüfi | INVOIC | transaktionsdaten › absender |
| [PI_31005](/schnittstellen/202610/pruefi/INVOIC/PI_31005) | Prüfi | INVOIC | transaktionsdaten › empfaenger |
| [PI_31006](/schnittstellen/202610/pruefi/INVOIC/PI_31006) | Prüfi | INVOIC | transaktionsdaten › absender |
| [PI_31006](/schnittstellen/202610/pruefi/INVOIC/PI_31006) | Prüfi | INVOIC | transaktionsdaten › empfaenger |
| [PI_31007](/schnittstellen/202610/pruefi/INVOIC/PI_31007) | Prüfi | INVOIC | transaktionsdaten › absender |
| [PI_31007](/schnittstellen/202610/pruefi/INVOIC/PI_31007) | Prüfi | INVOIC | transaktionsdaten › empfaenger |
| [PI_31008](/schnittstellen/202610/pruefi/INVOIC/PI_31008) | Prüfi | INVOIC | transaktionsdaten › absender |
| [PI_31008](/schnittstellen/202610/pruefi/INVOIC/PI_31008) | Prüfi | INVOIC | transaktionsdaten › empfaenger |
| [PI_31009](/schnittstellen/202610/pruefi/INVOIC/PI_31009) | Prüfi | INVOIC | transaktionsdaten › absender |
| [PI_31009](/schnittstellen/202610/pruefi/INVOIC/PI_31009) | Prüfi | INVOIC | transaktionsdaten › empfaenger |
| [PI_31010](/schnittstellen/202610/pruefi/INVOIC/PI_31010) | Prüfi | INVOIC | transaktionsdaten › absender |
| [PI_31010](/schnittstellen/202610/pruefi/INVOIC/PI_31010) | Prüfi | INVOIC | transaktionsdaten › empfaenger |
| [PI_31011](/schnittstellen/202610/pruefi/INVOIC/PI_31011) | Prüfi | INVOIC | transaktionsdaten › absender |
| [PI_31011](/schnittstellen/202610/pruefi/INVOIC/PI_31011) | Prüfi | INVOIC | transaktionsdaten › empfaenger |
| [PI_37000](/schnittstellen/202610/pruefi/PARTIN/PI_37000) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37001](/schnittstellen/202610/pruefi/PARTIN/PI_37001) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37002](/schnittstellen/202610/pruefi/PARTIN/PI_37002) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37008](/schnittstellen/202610/pruefi/PARTIN/PI_37008) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37009](/schnittstellen/202610/pruefi/PARTIN/PI_37009) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37010](/schnittstellen/202610/pruefi/PARTIN/PI_37010) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37012](/schnittstellen/202610/pruefi/PARTIN/PI_37012) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37013](/schnittstellen/202610/pruefi/PARTIN/PI_37013) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37014](/schnittstellen/202610/pruefi/PARTIN/PI_37014) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |

### steuernummer

31 Verwendung(en) in den Nachrichtentypen INVOIC, PARTIN.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_31001](/schnittstellen/202610/pruefi/INVOIC/PI_31001) | Prüfi | INVOIC | transaktionsdaten › absender |
| [PI_31001](/schnittstellen/202610/pruefi/INVOIC/PI_31001) | Prüfi | INVOIC | transaktionsdaten › empfaenger |
| [PI_31002](/schnittstellen/202610/pruefi/INVOIC/PI_31002) | Prüfi | INVOIC | transaktionsdaten › absender |
| [PI_31002](/schnittstellen/202610/pruefi/INVOIC/PI_31002) | Prüfi | INVOIC | transaktionsdaten › empfaenger |
| [PI_31003](/schnittstellen/202610/pruefi/INVOIC/PI_31003) | Prüfi | INVOIC | transaktionsdaten › absender |
| [PI_31003](/schnittstellen/202610/pruefi/INVOIC/PI_31003) | Prüfi | INVOIC | transaktionsdaten › empfaenger |
| [PI_31004](/schnittstellen/202610/pruefi/INVOIC/PI_31004) | Prüfi | INVOIC | transaktionsdaten › absender |
| [PI_31004](/schnittstellen/202610/pruefi/INVOIC/PI_31004) | Prüfi | INVOIC | transaktionsdaten › empfaenger |
| [PI_31005](/schnittstellen/202610/pruefi/INVOIC/PI_31005) | Prüfi | INVOIC | transaktionsdaten › absender |
| [PI_31005](/schnittstellen/202610/pruefi/INVOIC/PI_31005) | Prüfi | INVOIC | transaktionsdaten › empfaenger |
| [PI_31006](/schnittstellen/202610/pruefi/INVOIC/PI_31006) | Prüfi | INVOIC | transaktionsdaten › absender |
| [PI_31006](/schnittstellen/202610/pruefi/INVOIC/PI_31006) | Prüfi | INVOIC | transaktionsdaten › empfaenger |
| [PI_31007](/schnittstellen/202610/pruefi/INVOIC/PI_31007) | Prüfi | INVOIC | transaktionsdaten › absender |
| [PI_31007](/schnittstellen/202610/pruefi/INVOIC/PI_31007) | Prüfi | INVOIC | transaktionsdaten › empfaenger |
| [PI_31008](/schnittstellen/202610/pruefi/INVOIC/PI_31008) | Prüfi | INVOIC | transaktionsdaten › absender |
| [PI_31008](/schnittstellen/202610/pruefi/INVOIC/PI_31008) | Prüfi | INVOIC | transaktionsdaten › empfaenger |
| [PI_31009](/schnittstellen/202610/pruefi/INVOIC/PI_31009) | Prüfi | INVOIC | transaktionsdaten › absender |
| [PI_31009](/schnittstellen/202610/pruefi/INVOIC/PI_31009) | Prüfi | INVOIC | transaktionsdaten › empfaenger |
| [PI_31010](/schnittstellen/202610/pruefi/INVOIC/PI_31010) | Prüfi | INVOIC | transaktionsdaten › absender |
| [PI_31010](/schnittstellen/202610/pruefi/INVOIC/PI_31010) | Prüfi | INVOIC | transaktionsdaten › empfaenger |
| [PI_31011](/schnittstellen/202610/pruefi/INVOIC/PI_31011) | Prüfi | INVOIC | transaktionsdaten › absender |
| [PI_31011](/schnittstellen/202610/pruefi/INVOIC/PI_31011) | Prüfi | INVOIC | transaktionsdaten › empfaenger |
| [PI_37000](/schnittstellen/202610/pruefi/PARTIN/PI_37000) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37001](/schnittstellen/202610/pruefi/PARTIN/PI_37001) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37002](/schnittstellen/202610/pruefi/PARTIN/PI_37002) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37008](/schnittstellen/202610/pruefi/PARTIN/PI_37008) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37009](/schnittstellen/202610/pruefi/PARTIN/PI_37009) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37010](/schnittstellen/202610/pruefi/PARTIN/PI_37010) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37012](/schnittstellen/202610/pruefi/PARTIN/PI_37012) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37013](/schnittstellen/202610/pruefi/PARTIN/PI_37013) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37014](/schnittstellen/202610/pruefi/PARTIN/PI_37014) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |

### amtsgericht

9 Verwendung(en) in den Nachrichtentypen PARTIN.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_37000](/schnittstellen/202610/pruefi/PARTIN/PI_37000) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37001](/schnittstellen/202610/pruefi/PARTIN/PI_37001) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37002](/schnittstellen/202610/pruefi/PARTIN/PI_37002) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37008](/schnittstellen/202610/pruefi/PARTIN/PI_37008) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37009](/schnittstellen/202610/pruefi/PARTIN/PI_37009) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37010](/schnittstellen/202610/pruefi/PARTIN/PI_37010) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37012](/schnittstellen/202610/pruefi/PARTIN/PI_37012) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37013](/schnittstellen/202610/pruefi/PARTIN/PI_37013) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37014](/schnittstellen/202610/pruefi/PARTIN/PI_37014) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |

### hrnummer

9 Verwendung(en) in den Nachrichtentypen PARTIN.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_37000](/schnittstellen/202610/pruefi/PARTIN/PI_37000) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37001](/schnittstellen/202610/pruefi/PARTIN/PI_37001) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37002](/schnittstellen/202610/pruefi/PARTIN/PI_37002) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37008](/schnittstellen/202610/pruefi/PARTIN/PI_37008) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37009](/schnittstellen/202610/pruefi/PARTIN/PI_37009) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37010](/schnittstellen/202610/pruefi/PARTIN/PI_37010) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37012](/schnittstellen/202610/pruefi/PARTIN/PI_37012) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37013](/schnittstellen/202610/pruefi/PARTIN/PI_37013) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37014](/schnittstellen/202610/pruefi/PARTIN/PI_37014) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |

### website

9 Verwendung(en) in den Nachrichtentypen PARTIN.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_37000](/schnittstellen/202610/pruefi/PARTIN/PI_37000) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37001](/schnittstellen/202610/pruefi/PARTIN/PI_37001) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37002](/schnittstellen/202610/pruefi/PARTIN/PI_37002) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37008](/schnittstellen/202610/pruefi/PARTIN/PI_37008) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37009](/schnittstellen/202610/pruefi/PARTIN/PI_37009) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37010](/schnittstellen/202610/pruefi/PARTIN/PI_37010) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37012](/schnittstellen/202610/pruefi/PARTIN/PI_37012) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37013](/schnittstellen/202610/pruefi/PARTIN/PI_37013) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37014](/schnittstellen/202610/pruefi/PARTIN/PI_37014) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |

### faxnummer

9 Verwendung(en) in den Nachrichtentypen PARTIN.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_37000](/schnittstellen/202610/pruefi/PARTIN/PI_37000) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37001](/schnittstellen/202610/pruefi/PARTIN/PI_37001) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37002](/schnittstellen/202610/pruefi/PARTIN/PI_37002) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37008](/schnittstellen/202610/pruefi/PARTIN/PI_37008) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37009](/schnittstellen/202610/pruefi/PARTIN/PI_37009) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37010](/schnittstellen/202610/pruefi/PARTIN/PI_37010) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37012](/schnittstellen/202610/pruefi/PARTIN/PI_37012) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37013](/schnittstellen/202610/pruefi/PARTIN/PI_37013) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |
| [PI_37014](/schnittstellen/202610/pruefi/PARTIN/PI_37014) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |

### kommunikationsrolle

9 Verwendung(en) in den Nachrichtentypen PARTIN.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_37000](/schnittstellen/202610/pruefi/PARTIN/PI_37000) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben |
| [PI_37001](/schnittstellen/202610/pruefi/PARTIN/PI_37001) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben |
| [PI_37002](/schnittstellen/202610/pruefi/PARTIN/PI_37002) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben |
| [PI_37008](/schnittstellen/202610/pruefi/PARTIN/PI_37008) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben |
| [PI_37009](/schnittstellen/202610/pruefi/PARTIN/PI_37009) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben |
| [PI_37010](/schnittstellen/202610/pruefi/PARTIN/PI_37010) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben |
| [PI_37012](/schnittstellen/202610/pruefi/PARTIN/PI_37012) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben |
| [PI_37013](/schnittstellen/202610/pruefi/PARTIN/PI_37013) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben |
| [PI_37014](/schnittstellen/202610/pruefi/PARTIN/PI_37014) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben |

### weiterverpflichtet

49 Verwendung(en) in den Nachrichtentypen ORDERS, UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_17134](/schnittstellen/202610/pruefi/ORDERS/PI_17134) | Prüfi | ORDERS | stammdaten › MARKTLOKATION › marktrollen |
| [PI_17135](/schnittstellen/202610/pruefi/ORDERS/PI_17135) | Prüfi | ORDERS | stammdaten › MARKTLOKATION › marktrollen |
| [PI_44002](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › marktrollen |
| [PI_44013](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › marktrollen |
| [PI_44014](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › marktrollen |
| [PI_44035](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44035) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › marktrollen |
| [PI_44043](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44043) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › marktrollen |
| [PI_44060](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44060) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › marktrollen |
| [PI_44112](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44112) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › marktrollen |
| [PI_44113](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44113) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › marktrollen |
| [PI_44139](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44139) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › marktrollen |
| [PI_44140](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44140) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › marktrollen |
| [PI_44142](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44142) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › marktrollen |
| [PI_44168](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › marktrollen |
| [PI_55002](/schnittstellen/202610/pruefi/UTILMD/PI_55002) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55002](/schnittstellen/202610/pruefi/UTILMD/PI_55002) | Prüfi | UTILMD | stammdaten › MESSLOKATION › marktrollen |
| [PI_55013](/schnittstellen/202610/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55013](/schnittstellen/202610/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › MESSLOKATION › marktrollen |
| [PI_55035](/schnittstellen/202610/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55035](/schnittstellen/202610/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › MESSLOKATION › marktrollen |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › MESSLOKATION › marktrollen |
| [PI_55060](/schnittstellen/202610/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55060](/schnittstellen/202610/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › MESSLOKATION › marktrollen |
| [PI_55078](/schnittstellen/202610/pruefi/UTILMD/PI_55078) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55078](/schnittstellen/202610/pruefi/UTILMD/PI_55078) | Prüfi | UTILMD | stammdaten › MESSLOKATION › marktrollen |
| [PI_55095](/schnittstellen/202610/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55095](/schnittstellen/202610/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | stammdaten › MESSLOKATION › marktrollen |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › MESSLOKATION › marktrollen |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › MESSLOKATION › marktrollen |
| [PI_55194](/schnittstellen/202610/pruefi/UTILMD/PI_55194) | Prüfi | UTILMD | stammdaten › MESSLOKATION › marktrollen |
| [PI_55602](/schnittstellen/202610/pruefi/UTILMD/PI_55602) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55602](/schnittstellen/202610/pruefi/UTILMD/PI_55602) | Prüfi | UTILMD | stammdaten › MESSLOKATION › marktrollen |
| [PI_55603](/schnittstellen/202610/pruefi/UTILMD/PI_55603) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55603](/schnittstellen/202610/pruefi/UTILMD/PI_55603) | Prüfi | UTILMD | stammdaten › MESSLOKATION › marktrollen |
| [PI_55607](/schnittstellen/202610/pruefi/UTILMD/PI_55607) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55607](/schnittstellen/202610/pruefi/UTILMD/PI_55607) | Prüfi | UTILMD | stammdaten › MESSLOKATION › marktrollen |
| [PI_55616](/schnittstellen/202610/pruefi/UTILMD/PI_55616) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55620](/schnittstellen/202610/pruefi/UTILMD/PI_55620) | Prüfi | UTILMD | stammdaten › MESSLOKATION › marktrollen |
| [PI_55622](/schnittstellen/202610/pruefi/UTILMD/PI_55622) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55626](/schnittstellen/202610/pruefi/UTILMD/PI_55626) | Prüfi | UTILMD | stammdaten › MESSLOKATION › marktrollen |
| [PI_55628](/schnittstellen/202610/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55632](/schnittstellen/202610/pruefi/UTILMD/PI_55632) | Prüfi | UTILMD | stammdaten › MESSLOKATION › marktrollen |
| [PI_55634](/schnittstellen/202610/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55638](/schnittstellen/202610/pruefi/UTILMD/PI_55638) | Prüfi | UTILMD | stammdaten › MESSLOKATION › marktrollen |
| [PI_55690](/schnittstellen/202610/pruefi/UTILMD/PI_55690) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55690](/schnittstellen/202610/pruefi/UTILMD/PI_55690) | Prüfi | UTILMD | stammdaten › MESSLOKATION › marktrollen |

### messstellenbetreiberEigenschaft

69 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55002](/schnittstellen/202610/pruefi/UTILMD/PI_55002) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55002](/schnittstellen/202610/pruefi/UTILMD/PI_55002) | Prüfi | UTILMD | stammdaten › MESSLOKATION › marktrollen |
| [PI_55002](/schnittstellen/202610/pruefi/UTILMD/PI_55002) | Prüfi | UTILMD | stammdaten › NETZLOKATION › marktrollen |
| [PI_55002](/schnittstellen/202610/pruefi/UTILMD/PI_55002) | Prüfi | UTILMD | stammdaten › STEUERBARE_RESSOURCE › marktrollen |
| [PI_55013](/schnittstellen/202610/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55013](/schnittstellen/202610/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › MESSLOKATION › marktrollen |
| [PI_55013](/schnittstellen/202610/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › NETZLOKATION › marktrollen |
| [PI_55013](/schnittstellen/202610/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › STEUERBARE_RESSOURCE › marktrollen |
| [PI_55035](/schnittstellen/202610/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55035](/schnittstellen/202610/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › MESSLOKATION › marktrollen |
| [PI_55035](/schnittstellen/202610/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › NETZLOKATION › marktrollen |
| [PI_55035](/schnittstellen/202610/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › STEUERBARE_RESSOURCE › marktrollen |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › MESSLOKATION › marktrollen |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › NETZLOKATION › marktrollen |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › STEUERBARE_RESSOURCE › marktrollen |
| [PI_55060](/schnittstellen/202610/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55060](/schnittstellen/202610/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › MESSLOKATION › marktrollen |
| [PI_55060](/schnittstellen/202610/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › NETZLOKATION › marktrollen |
| [PI_55060](/schnittstellen/202610/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › STEUERBARE_RESSOURCE › marktrollen |
| [PI_55078](/schnittstellen/202610/pruefi/UTILMD/PI_55078) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55078](/schnittstellen/202610/pruefi/UTILMD/PI_55078) | Prüfi | UTILMD | stammdaten › MESSLOKATION › marktrollen |
| [PI_55078](/schnittstellen/202610/pruefi/UTILMD/PI_55078) | Prüfi | UTILMD | stammdaten › NETZLOKATION › marktrollen |
| [PI_55078](/schnittstellen/202610/pruefi/UTILMD/PI_55078) | Prüfi | UTILMD | stammdaten › STEUERBARE_RESSOURCE › marktrollen |
| [PI_55095](/schnittstellen/202610/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55095](/schnittstellen/202610/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | stammdaten › MESSLOKATION › marktrollen |
| [PI_55095](/schnittstellen/202610/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | stammdaten › NETZLOKATION › marktrollen |
| [PI_55095](/schnittstellen/202610/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | stammdaten › STEUERBARE_RESSOURCE › marktrollen |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › MESSLOKATION › marktrollen |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › NETZLOKATION › marktrollen |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › STEUERBARE_RESSOURCE › marktrollen |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › MESSLOKATION › marktrollen |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › NETZLOKATION › marktrollen |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › STEUERBARE_RESSOURCE › marktrollen |
| [PI_55194](/schnittstellen/202610/pruefi/UTILMD/PI_55194) | Prüfi | UTILMD | stammdaten › MESSLOKATION › marktrollen |
| [PI_55602](/schnittstellen/202610/pruefi/UTILMD/PI_55602) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55602](/schnittstellen/202610/pruefi/UTILMD/PI_55602) | Prüfi | UTILMD | stammdaten › MESSLOKATION › marktrollen |
| [PI_55602](/schnittstellen/202610/pruefi/UTILMD/PI_55602) | Prüfi | UTILMD | stammdaten › NETZLOKATION › marktrollen |
| [PI_55602](/schnittstellen/202610/pruefi/UTILMD/PI_55602) | Prüfi | UTILMD | stammdaten › STEUERBARE_RESSOURCE › marktrollen |
| [PI_55603](/schnittstellen/202610/pruefi/UTILMD/PI_55603) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55603](/schnittstellen/202610/pruefi/UTILMD/PI_55603) | Prüfi | UTILMD | stammdaten › MESSLOKATION › marktrollen |
| [PI_55603](/schnittstellen/202610/pruefi/UTILMD/PI_55603) | Prüfi | UTILMD | stammdaten › NETZLOKATION › marktrollen |
| [PI_55603](/schnittstellen/202610/pruefi/UTILMD/PI_55603) | Prüfi | UTILMD | stammdaten › STEUERBARE_RESSOURCE › marktrollen |
| [PI_55607](/schnittstellen/202610/pruefi/UTILMD/PI_55607) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55607](/schnittstellen/202610/pruefi/UTILMD/PI_55607) | Prüfi | UTILMD | stammdaten › MESSLOKATION › marktrollen |
| [PI_55607](/schnittstellen/202610/pruefi/UTILMD/PI_55607) | Prüfi | UTILMD | stammdaten › NETZLOKATION › marktrollen |
| [PI_55607](/schnittstellen/202610/pruefi/UTILMD/PI_55607) | Prüfi | UTILMD | stammdaten › STEUERBARE_RESSOURCE › marktrollen |
| [PI_55615](/schnittstellen/202610/pruefi/UTILMD/PI_55615) | Prüfi | UTILMD | stammdaten › NETZLOKATION › marktrollen |
| [PI_55616](/schnittstellen/202610/pruefi/UTILMD/PI_55616) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55618](/schnittstellen/202610/pruefi/UTILMD/PI_55618) | Prüfi | UTILMD | stammdaten › STEUERBARE_RESSOURCE › marktrollen |
| [PI_55620](/schnittstellen/202610/pruefi/UTILMD/PI_55620) | Prüfi | UTILMD | stammdaten › MESSLOKATION › marktrollen |
| [PI_55621](/schnittstellen/202610/pruefi/UTILMD/PI_55621) | Prüfi | UTILMD | stammdaten › NETZLOKATION › marktrollen |
| [PI_55622](/schnittstellen/202610/pruefi/UTILMD/PI_55622) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55624](/schnittstellen/202610/pruefi/UTILMD/PI_55624) | Prüfi | UTILMD | stammdaten › STEUERBARE_RESSOURCE › marktrollen |
| [PI_55626](/schnittstellen/202610/pruefi/UTILMD/PI_55626) | Prüfi | UTILMD | stammdaten › MESSLOKATION › marktrollen |
| [PI_55627](/schnittstellen/202610/pruefi/UTILMD/PI_55627) | Prüfi | UTILMD | stammdaten › NETZLOKATION › marktrollen |
| [PI_55628](/schnittstellen/202610/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55630](/schnittstellen/202610/pruefi/UTILMD/PI_55630) | Prüfi | UTILMD | stammdaten › STEUERBARE_RESSOURCE › marktrollen |
| [PI_55632](/schnittstellen/202610/pruefi/UTILMD/PI_55632) | Prüfi | UTILMD | stammdaten › MESSLOKATION › marktrollen |
| [PI_55633](/schnittstellen/202610/pruefi/UTILMD/PI_55633) | Prüfi | UTILMD | stammdaten › NETZLOKATION › marktrollen |
| [PI_55634](/schnittstellen/202610/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55636](/schnittstellen/202610/pruefi/UTILMD/PI_55636) | Prüfi | UTILMD | stammdaten › STEUERBARE_RESSOURCE › marktrollen |
| [PI_55638](/schnittstellen/202610/pruefi/UTILMD/PI_55638) | Prüfi | UTILMD | stammdaten › MESSLOKATION › marktrollen |
| [PI_55690](/schnittstellen/202610/pruefi/UTILMD/PI_55690) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › marktrollen |
| [PI_55690](/schnittstellen/202610/pruefi/UTILMD/PI_55690) | Prüfi | UTILMD | stammdaten › MESSLOKATION › marktrollen |
| [PI_55690](/schnittstellen/202610/pruefi/UTILMD/PI_55690) | Prüfi | UTILMD | stammdaten › NETZLOKATION › marktrollen |
| [PI_55690](/schnittstellen/202610/pruefi/UTILMD/PI_55690) | Prüfi | UTILMD | stammdaten › STEUERBARE_RESSOURCE › marktrollen |

### ipAdresse

4 Verwendung(en) in den Nachrichtentypen ORDRSP, UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_19001](/schnittstellen/202610/pruefi/ORDRSP/PI_19001) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_19011](/schnittstellen/202610/pruefi/ORDRSP/PI_19011) | Prüfi | ORDRSP | transaktionsdaten › absender |
| [PI_55553](/schnittstellen/202610/pruefi/UTILMD/PI_55553) | Prüfi | UTILMD | transaktionsdaten › absender |
| [PI_55555](/schnittstellen/202610/pruefi/UTILMD/PI_55555) | Prüfi | UTILMD | transaktionsdaten › absender |

### bilanzkreis

1 Verwendung(en) in den Nachrichtentypen PARTIN.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_37000](/schnittstellen/202610/pruefi/PARTIN/PI_37000) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |

### verwendungszweckBilanzkreis

1 Verwendung(en) in den Nachrichtentypen PARTIN.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_37000](/schnittstellen/202610/pruefi/PARTIN/PI_37000) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
