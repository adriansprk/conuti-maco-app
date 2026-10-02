# Geschaeftspartner
<span hidden data-pagefind-meta={"title:Geschaeftspartner — BO4E-Geschäftsobjekt (FV 202604)"} />

BO4E-Geschäftsobjekt · 20 Felder · 883 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="botyp"></a>`boTyp` <span className="hbs-pflicht">\*</span> | [Enum BOTyp](/bo4e/202604/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> | Typ des BO |
| <a id="versionstruktur"></a>`versionStruktur` <span className="hbs-pflicht">\*</span> | string | versionStruktur |
| <a id="anrede"></a>`anrede` | string | Die Anrede für den GePa, Z.B. Herr. |
| <a id="name1"></a>`name1` | string | Erster Teil des Namens. Hier kann der Firmenname oder bei Privatpersonen beispielsweise der Nachname dargestellt werden. Beispiele: Yellow Strom GmbH oder Hagen |
| <a id="name2"></a>`name2` | string | Zweiter Teil des Namens. Hier kann der eine Erweiterung zum Firmennamen oder bei Privatpersonen beispielsweise der Vorname dargestellt werden. Beispiele: Bereich Süd oder Nina |
| <a id="name3"></a>`name3` | string | Dritter Teil des Namens. Hier können weitere Ergänzungen zum Firmennamen oder bei Privatpersonen Zusätze zum Namen dargestellt werden. Beispiele: und Afrika oder Sängerin |
| <a id="name4"></a>`name4` | string | name4 |
| <a id="umsatzsteuerid"></a>`umsatzsteuerId` | string | Die Umsatzsteuer-ID des Geschäftspartners. Beispiel: DE 813281825 |
| <a id="glaeubigerid"></a>`glaeubigerId` | string | * Die Gläubiger-ID welche im Zahlungsverkehr verwendet wird- Z.B. DE 47116789 |
| <a id="emailadresse"></a>`emailAdresse` | string | emailAdresse |
| <a id="website"></a>`website` | string | Internetseite des Marktpartners. Beispiel: www.mp-energie.de |
| <a id="gewerbekennzeichnung"></a>`gewerbekennzeichnung` | boolean | Kennzeichnung ob es sich um einen Gewerbe/Unternehmen (gewerbeKennzeichnung = true) oder eine Privatperson handelt. (gewerbeKennzeichnung = false) |
| <a id="hrnummer"></a>`hrnummer` | string | Handelsregisternummer des Geschäftspartners |
| <a id="amtsgericht"></a>`amtsgericht` | string | Amtsgericht bzw Handelsregistergericht, das die Handelsregisternummer herausgegeben hat |
| <a id="partneradresse"></a>`partneradresse` | [Adresse](/bo4e/202604/com/Adresse) | Adresse des Geschäftspartners, an der sich der Hauptsitz befindet. Details |
| <a id="externekundenummerlieferant"></a>`externeKundenummerLieferant` | string | externeKundenummerLieferant |
| <a id="externereferenzen"></a>`externeReferenzen` | [ExterneReferenz[]](/bo4e/202604/com/ExterneReferenz) | Hier können IDs anderer Systeme hinterlegt werden (z.B. eine SAP-GP-Nummer) (Details siehe ExterneReferenz) |
| <a id="geschaeftspartnerrolle"></a>`geschaeftspartnerrolle` | [Enum Geschaeftspartnerrolle[]](/bo4e/202604/enum/Geschaeftspartnerrolle)<br/><Werte>`KUNDE`, `LIEFERANT`, `DIENSTLEISTER`, `INTERESSENT`, `MARKTPARTNER`, `EIGENTUEMER`, `HAUSVERWALTER`, `KORRESPONDENZEMPFAENGER`, `ABLESEKARTENEMPFAENGER`</Werte> | Rolle, die der Geschäftspartner hat (z.B. Interessent, Kunde). |
| <a id="kontaktweg"></a>`kontaktweg` | [Enum Kontaktart[]](/bo4e/202604/enum/Kontaktart)<br/><Werte>`ANSCHREIBEN`, `TELEFONAT`, `FAX`, `E_MAIL`, `SMS`</Werte> | Bevorzugter Kontaktweg des Geschäftspartners. |
| <a id="ansprechpartner"></a>`ansprechpartner` | [Ansprechpartner](/bo4e/202604/bo/Ansprechpartner) | Ansprechpartner as in EDIFACT CTA+IC' COM+?+3222271020:TE', that includes e.g. the phone number of customer. |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[boTyp](/bo4e/202604/bo/Geschaeftspartner#botyp) <span className="hbs-pflicht">\*</span></span> | Typ des BO | [Enum BOTyp](/bo4e/202604/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> |
| <span className="hbs-f hbs-e0">[versionStruktur](/bo4e/202604/bo/Geschaeftspartner#versionstruktur) <span className="hbs-pflicht">\*</span></span> | versionStruktur | string |
| <span className="hbs-f hbs-e0">[anrede](/bo4e/202604/bo/Geschaeftspartner#anrede)</span> | Die Anrede für den GePa, Z.B. Herr. | string |
| <span className="hbs-f hbs-e0">[name1](/bo4e/202604/bo/Geschaeftspartner#name1)</span> | Erster Teil des Namens. Hier kann der Firmenname oder bei Privatpersonen<br/>beispielsweise der Nachname dargestellt werden. Beispiele: Yellow Strom GmbH<br/>oder Hagen | string |
| <span className="hbs-f hbs-e0">[name2](/bo4e/202604/bo/Geschaeftspartner#name2)</span> | Zweiter Teil des Namens. Hier kann der eine Erweiterung zum Firmennamen oder<br/>bei Privatpersonen beispielsweise der Vorname dargestellt werden. Beispiele:<br/>Bereich Süd oder Nina | string |
| <span className="hbs-f hbs-e0">[name3](/bo4e/202604/bo/Geschaeftspartner#name3)</span> | Dritter Teil des Namens. Hier können weitere Ergänzungen zum Firmennamen oder<br/>bei Privatpersonen Zusätze zum Namen dargestellt werden. Beispiele: und Afrika<br/>oder Sängerin | string |
| <span className="hbs-f hbs-e0">[name4](/bo4e/202604/bo/Geschaeftspartner#name4)</span> | name4 | string |
| <span className="hbs-f hbs-e0">[umsatzsteuerId](/bo4e/202604/bo/Geschaeftspartner#umsatzsteuerid)</span> | Die Umsatzsteuer-ID des Geschäftspartners. Beispiel: DE 813281825 | string |
| <span className="hbs-f hbs-e0">[glaeubigerId](/bo4e/202604/bo/Geschaeftspartner#glaeubigerid)</span> | * Die Gläubiger-ID welche im Zahlungsverkehr verwendet wird- Z.B. DE 47116789 | string |
| <span className="hbs-f hbs-e0">[emailAdresse](/bo4e/202604/bo/Geschaeftspartner#emailadresse)</span> | emailAdresse | string |
| <span className="hbs-f hbs-e0">[website](/bo4e/202604/bo/Geschaeftspartner#website)</span> | Internetseite des Marktpartners. Beispiel: www.mp-energie.de | string |
| <span className="hbs-f hbs-e0">[gewerbekennzeichnung](/bo4e/202604/bo/Geschaeftspartner#gewerbekennzeichnung)</span> | Kennzeichnung ob es sich um einen Gewerbe/Unternehmen (gewerbeKennzeichnung = true)<br/>oder eine Privatperson handelt. (gewerbeKennzeichnung = false) | boolean |
| <span className="hbs-f hbs-e0">[hrnummer](/bo4e/202604/bo/Geschaeftspartner#hrnummer)</span> | Handelsregisternummer des Geschäftspartners | string |
| <span className="hbs-f hbs-e0">[amtsgericht](/bo4e/202604/bo/Geschaeftspartner#amtsgericht)</span> | Amtsgericht bzw Handelsregistergericht, das die Handelsregisternummer herausgegeben hat | string |
| <span className="hbs-g hbs-e0">[partneradresse](/bo4e/202604/bo/Geschaeftspartner#partneradresse)</span> | Adresse des Geschäftspartners, an der sich der Hauptsitz befindet. Details | [Adresse](/bo4e/202604/com/Adresse) |
| <span className="hbs-f hbs-e1">[postleitzahl](/bo4e/202604/com/Adresse#postleitzahl)</span> | Postleitzahl | string |
| <span className="hbs-f hbs-e1">[ort](/bo4e/202604/com/Adresse#ort)</span> | Ort | string |
| <span className="hbs-f hbs-e1">[strasse](/bo4e/202604/com/Adresse#strasse)</span> | Strasse | string |
| <span className="hbs-f hbs-e1">[hausnummer](/bo4e/202604/com/Adresse#hausnummer)</span> | Hausnummer und Ergänzung | string |
| <span className="hbs-f hbs-e1">[postfach](/bo4e/202604/com/Adresse#postfach)</span> | Postfach | string |
| <span className="hbs-f hbs-e1">[adresszusatz](/bo4e/202604/com/Adresse#adresszusatz)</span> | Adresszusatz | string |
| <span className="hbs-f hbs-e1">[coErgaenzung](/bo4e/202604/com/Adresse#coergaenzung)</span> | coErgaenzung | string |
| <span className="hbs-f hbs-e1">[landescode](/bo4e/202604/com/Adresse#landescode)</span> | Landescode | [Enum Landescode](/bo4e/202604/enum/Landescode)<br/><Werte>`AC`, `AD`, `AE`, `AF`, `AG`, `AI`, `AL`, `AM`, `AN`, `AO`, `AQ`, `AR`, `AS`, `AT`, `AU`, `AW`, `AX`, `AZ`, `BA`, `BB`, `BD`, `BE`, `BF`, `BG`, `BH`, `BI`, `BJ`, `BL`, `BM`, `BN`, `BO`, `BQ`, `BR`, `BS`, `BT`, `BU`, `BV`, `BW`, `BY`, `BZ`, `CA`, `CC`, `CD`, `CF`, `CG`, `CH`, `CI`, `CK`, `CL`, `CM`, `CN`, `CO`, `CP`, `CR`, `CS`, `CU`, `CV`, `CW`, `CX`, `CY`, `CZ`, `DE`, `DG`, `DJ`, `DK`, `DM`, `DO`, `DZ`, `EA`, `EC`, `EE`, `EG`, `EH`, `ER`, `ES`, `ET`, `EU`, `FI`, `FJ`, `FK`, `FM`, `FO`, `FR`, `FX`, `GA`, `GB`, `GD`, `GE`, `GF`, `GG`, `GH`, `GI`, `GL`, `GM`, `GN`, `GP`, `GQ`, `GR`, `GS`, `GT`, `GU`, `GW`, `GY`, `HK`, `HM`, `HN`, `HR`, `HT`, `HU`, `IC`, `ID`, `IE`, `IL`, `IM`, `IN`, `IO`, `IQ`, `IR`, `IS`, `IT`, `JE`, `JM`, `JO`, `JP`, `KE`, `KG`, `KH`, `KI`, `KM`, `KN`, `KP`, `KR`, `KW`, `KY`, `KZ`, `LA`, `LB`, `LC`, `LI`, `LK`, `LR`, `LS`, `LT`, `LU`, `LV`, `LY`, `MA`, `MC`, `MD`, `ME`, `MF`, `MG`, `MH`, `MK`, `ML`, `MM`, `MN`, `MO`, `MP`, `MQ`, `MR`, `MS`, `MT`, `MU`, `MV`, `MW`, `MX`, `MY`, `MZ`, `NA`, `NC`, `NE`, `NF`, `NG`, `NI`, `NL`, `NO`, `NP`, `NR`, `NT`, `NU`, `NZ`, `OM`, `PA`, `PE`, `PF`, `PG`, `PH`, `PK`, `PL`, `PM`, `PN`, `PR`, `PS`, `PT`, `PW`, `PY`, `QA`, `RE`, `RO`, `RS`, `RU`, `RW`, `SA`, `SB`, `SC`, `SD`, `SE`, `SF`, `SG`, `SH`, `SI`, `SJ`, `SK`, `SL`, `SM`, `SN`, `SO`, `SR`, `SS`, `ST`, `SU`, `SV`, `SX`, `SY`, `SZ`, `TA`, `TC`, `TD`, `TF`, `TG`, `TJ`, `TK`, `TL`, `TM`, `TN`, `TO`, `TP`, `TR`, `TT`, `TV`, `TW`, `TZ`, `UA`, `UG`, `UK`, `UM`, `US`, `UY`, `UZ`, `VA`, `VC`, `VE`, `VG`, `VI`, `VN`, `VU`, `WF`, `WS`, `XK`, `YE`, `YT`, `YU`, `ZA`, `ZM`, `ZR`, `ZW`</Werte> |
| <span className="hbs-f hbs-e1">[ortsteil](/bo4e/202604/com/Adresse#ortsteil)</span> | Ortsteil | string |
| <span className="hbs-g hbs-e1">[zusatzInformation](/bo4e/202604/com/Adresse#zusatzinformation)</span> | — | [AdresszusatzInformation](/bo4e/202604/com/AdresszusatzInformation) |
| <span className="hbs-f hbs-e2">[zusatz1](/bo4e/202604/com/AdresszusatzInformation#zusatz1)</span> | Adresszusatz 1 | string |
| <span className="hbs-f hbs-e2">[zusatz2](/bo4e/202604/com/AdresszusatzInformation#zusatz2)</span> | Adresszusatz 2 | string |
| <span className="hbs-f hbs-e2">[zusatz3](/bo4e/202604/com/AdresszusatzInformation#zusatz3)</span> | Adresszusatz 3 | string |
| <span className="hbs-f hbs-e2">[zusatz4](/bo4e/202604/com/AdresszusatzInformation#zusatz4)</span> | Adresszusatz 4 | string |
| <span className="hbs-f hbs-e2">[zusatz5](/bo4e/202604/com/AdresszusatzInformation#zusatz5)</span> | Adresszusatz 5 | string |
| <span className="hbs-f hbs-e0">[externeKundenummerLieferant](/bo4e/202604/bo/Geschaeftspartner#externekundenummerlieferant)</span> | externeKundenummerLieferant | string |
| <span className="hbs-g hbs-e0">[externeReferenzen](/bo4e/202604/bo/Geschaeftspartner#externereferenzen) <span className="hbs-liste">[ ]</span></span> | Hier können IDs anderer Systeme hinterlegt werden (z.B. eine SAP-GP-Nummer) (Details siehe<br/>ExterneReferenz) | [ExterneReferenz[]](/bo4e/202604/com/ExterneReferenz) |
| <span className="hbs-f hbs-e1">[exRefName](/bo4e/202604/com/ExterneReferenz#exrefname)</span> | Bezeichnung der externen Referenz (z.B. "hochfrequenz integration services") | string<br/><Werte>`Kundennummer beim Lieferanten`, `Kundennummer beim Altlieferanten`</Werte> |
| <span className="hbs-f hbs-e1">[exRefWert](/bo4e/202604/com/ExterneReferenz#exrefwert)</span> | Wert der externen Referenz (z.B. "123456"; "4711") | string |
| <span className="hbs-f hbs-e0">[geschaeftspartnerrolle](/bo4e/202604/bo/Geschaeftspartner#geschaeftspartnerrolle) <span className="hbs-liste">[ ]</span></span> | Rolle, die der Geschäftspartner hat (z.B. Interessent, Kunde). | [Enum Geschaeftspartnerrolle[]](/bo4e/202604/enum/Geschaeftspartnerrolle)<br/><Werte>`KUNDE`, `LIEFERANT`, `DIENSTLEISTER`, `INTERESSENT`, `MARKTPARTNER`, `EIGENTUEMER`, `HAUSVERWALTER`, `KORRESPONDENZEMPFAENGER`, `ABLESEKARTENEMPFAENGER`</Werte> |
| <span className="hbs-f hbs-e0">[kontaktweg](/bo4e/202604/bo/Geschaeftspartner#kontaktweg) <span className="hbs-liste">[ ]</span></span> | Bevorzugter Kontaktweg des Geschäftspartners. | [Enum Kontaktart[]](/bo4e/202604/enum/Kontaktart)<br/><Werte>`ANSCHREIBEN`, `TELEFONAT`, `FAX`, `E_MAIL`, `SMS`</Werte> |
| <span className="hbs-g hbs-e0">[ansprechpartner](/bo4e/202604/bo/Geschaeftspartner#ansprechpartner)</span> | Ansprechpartner as in EDIFACT CTA+IC' COM+?+3222271020:TE', that includes e.g. the phone number of customer. | [Ansprechpartner](/bo4e/202604/bo/Ansprechpartner) |
| <span className="hbs-f hbs-e1">[boTyp](/bo4e/202604/bo/Ansprechpartner#botyp) <span className="hbs-pflicht">\*</span></span> | Typ des BO | [Enum BOTyp](/bo4e/202604/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> |
| <span className="hbs-f hbs-e1">[versionStruktur](/bo4e/202604/bo/Ansprechpartner#versionstruktur) <span className="hbs-pflicht">\*</span></span> | versionStruktur | string |
| <span className="hbs-f hbs-e1">[nachname](/bo4e/202604/bo/Ansprechpartner#nachname)</span> | Nachname (Familienname) des Ansprechpartners | string |
| <span className="hbs-f hbs-e1">[eMailAdresse](/bo4e/202604/bo/Ansprechpartner#emailadresse)</span> | E-Mail Adresse | string |
| <span className="hbs-g hbs-e1">[rufnummern](/bo4e/202604/bo/Ansprechpartner#rufnummern) <span className="hbs-liste">[ ]</span></span> | Liste der Telefonnummern, unter denen der Ansprechpartner erreichbar ist. | [Rufnummer[]](/bo4e/202604/com/Rufnummer) |
| <span className="hbs-f hbs-e2">[nummerntyp](/bo4e/202604/com/Rufnummer#nummerntyp)</span> | Rufnummernart | [Enum Rufnummernart](/bo4e/202604/enum/Rufnummernart)<br/><Werte>`RUF_ZENTRALE`, `FAX_ZENTRALE`, `SAMMELRUF`, `SAMMELFAX`, `ABTEILUNGRUF`, `ABTEILUNGFAX`, `RUF_DURCHWAHL`, `FAX_DURCHWAHL`, `MOBIL_NUMMER`</Werte> |
| <span className="hbs-f hbs-e2">[rufnummer](/bo4e/202604/com/Rufnummer#rufnummer)</span> | rufnummer | string |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### anrede

151 Verwendung(en) in den Nachrichtentypen IFTSTA, ORDERS, ORDRSP, UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_17101](/schnittstellen/202604/pruefi/ORDERS/PI_17101) | Prüfi | ORDERS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_17126](/schnittstellen/202604/pruefi/ORDERS/PI_17126) | Prüfi | ORDERS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_19015](/schnittstellen/202604/pruefi/ORDRSP/PI_19015) | Prüfi | ORDRSP | stammdaten › AUFTRAG › lieferadresseAltgeraete |
| [PI_21045](/schnittstellen/202604/pruefi/IFTSTA/PI_21045) | Prüfi | IFTSTA | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44001](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44001) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_44001](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44001) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44001](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44001) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44010](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44010) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44016](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44016) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44017](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44017) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44019](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44019) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44020](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44020) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44021](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44021) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44035](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44035) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44039](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44039) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_44040](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44040) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_44043](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44043) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44043](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44043) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_44043](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44043) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_44109](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44109) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_44109](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44109) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44112](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44112) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_44112](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44112) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_44112](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44112) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_44112](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44112) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_44113](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44113) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_44113](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44113) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_44113](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44113) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_44113](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44113) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_44137](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44137) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_44137](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44137) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44138](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44138) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_44138](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44138) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44139](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44139) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_44139](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44139) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_44139](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44139) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_44139](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44139) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_44140](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44140) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_44140](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44140) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_44140](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44140) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_44140](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44140) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_44142](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44142) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_44142](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44142) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_44142](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44142) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_44142](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44142) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_44159](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44159) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44159](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44159) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_44159](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44159) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_44160](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44160) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44162](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44162) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44163](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44163) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44165](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44165) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44166](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44166) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44166](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44166) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_44166](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44166) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_44167](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44167) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44167](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44167) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_44167](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44167) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_44168](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44168](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_44168](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_44168](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_44168](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_55001](/schnittstellen/202604/pruefi/UTILMD/PI_55001) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55001](/schnittstellen/202604/pruefi/UTILMD/PI_55001) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55010](/schnittstellen/202604/pruefi/UTILMD/PI_55010) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55013](/schnittstellen/202604/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55013](/schnittstellen/202604/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55013](/schnittstellen/202604/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_55013](/schnittstellen/202604/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_55013](/schnittstellen/202604/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_55013](/schnittstellen/202604/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_55014](/schnittstellen/202604/pruefi/UTILMD/PI_55014) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55014](/schnittstellen/202604/pruefi/UTILMD/PI_55014) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55039](/schnittstellen/202604/pruefi/UTILMD/PI_55039) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_55040](/schnittstellen/202604/pruefi/UTILMD/PI_55040) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_55042](/schnittstellen/202604/pruefi/UTILMD/PI_55042) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_55042](/schnittstellen/202604/pruefi/UTILMD/PI_55042) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_55042](/schnittstellen/202604/pruefi/UTILMD/PI_55042) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_55109](/schnittstellen/202604/pruefi/UTILMD/PI_55109) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55109](/schnittstellen/202604/pruefi/UTILMD/PI_55109) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55110](/schnittstellen/202604/pruefi/UTILMD/PI_55110) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55110](/schnittstellen/202604/pruefi/UTILMD/PI_55110) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55136](/schnittstellen/202604/pruefi/UTILMD/PI_55136) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55136](/schnittstellen/202604/pruefi/UTILMD/PI_55136) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55137](/schnittstellen/202604/pruefi/UTILMD/PI_55137) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55137](/schnittstellen/202604/pruefi/UTILMD/PI_55137) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_55600](/schnittstellen/202604/pruefi/UTILMD/PI_55600) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55600](/schnittstellen/202604/pruefi/UTILMD/PI_55600) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55601](/schnittstellen/202604/pruefi/UTILMD/PI_55601) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55601](/schnittstellen/202604/pruefi/UTILMD/PI_55601) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55616](/schnittstellen/202604/pruefi/UTILMD/PI_55616) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_55616](/schnittstellen/202604/pruefi/UTILMD/PI_55616) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_55616](/schnittstellen/202604/pruefi/UTILMD/PI_55616) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_55616](/schnittstellen/202604/pruefi/UTILMD/PI_55616) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_55622](/schnittstellen/202604/pruefi/UTILMD/PI_55622) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_55622](/schnittstellen/202604/pruefi/UTILMD/PI_55622) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_55622](/schnittstellen/202604/pruefi/UTILMD/PI_55622) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_55622](/schnittstellen/202604/pruefi/UTILMD/PI_55622) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_55628](/schnittstellen/202604/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_55628](/schnittstellen/202604/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_55628](/schnittstellen/202604/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_55628](/schnittstellen/202604/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_55634](/schnittstellen/202604/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_55634](/schnittstellen/202604/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_55634](/schnittstellen/202604/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_55634](/schnittstellen/202604/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_55643](/schnittstellen/202604/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_55643](/schnittstellen/202604/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_55643](/schnittstellen/202604/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_55648](/schnittstellen/202604/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_55648](/schnittstellen/202604/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_55648](/schnittstellen/202604/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_55653](/schnittstellen/202604/pruefi/UTILMD/PI_55653) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_55658](/schnittstellen/202604/pruefi/UTILMD/PI_55658) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_55663](/schnittstellen/202604/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_55663](/schnittstellen/202604/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_55663](/schnittstellen/202604/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_55669](/schnittstellen/202604/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_55669](/schnittstellen/202604/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_55669](/schnittstellen/202604/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |

### name1

151 Verwendung(en) in den Nachrichtentypen IFTSTA, ORDERS, ORDRSP, UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_17101](/schnittstellen/202604/pruefi/ORDERS/PI_17101) | Prüfi | ORDERS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_17126](/schnittstellen/202604/pruefi/ORDERS/PI_17126) | Prüfi | ORDERS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_19015](/schnittstellen/202604/pruefi/ORDRSP/PI_19015) | Prüfi | ORDRSP | stammdaten › AUFTRAG › lieferadresseAltgeraete |
| [PI_21045](/schnittstellen/202604/pruefi/IFTSTA/PI_21045) | Prüfi | IFTSTA | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44001](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44001) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_44001](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44001) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44001](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44001) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44010](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44010) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44016](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44016) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44017](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44017) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44019](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44019) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44020](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44020) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44021](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44021) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44035](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44035) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44039](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44039) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_44040](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44040) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_44043](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44043) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44043](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44043) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_44043](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44043) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_44109](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44109) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_44109](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44109) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44112](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44112) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_44112](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44112) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_44112](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44112) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_44112](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44112) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_44113](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44113) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_44113](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44113) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_44113](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44113) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_44113](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44113) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_44137](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44137) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_44137](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44137) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44138](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44138) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_44138](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44138) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44139](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44139) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_44139](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44139) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_44139](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44139) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_44139](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44139) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_44140](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44140) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_44140](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44140) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_44140](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44140) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_44140](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44140) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_44142](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44142) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_44142](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44142) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_44142](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44142) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_44142](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44142) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_44159](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44159) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44159](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44159) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_44159](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44159) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_44160](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44160) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44162](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44162) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44163](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44163) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44165](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44165) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44166](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44166) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44166](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44166) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_44166](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44166) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_44167](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44167) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44167](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44167) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_44167](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44167) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_44168](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44168](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_44168](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_44168](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_44168](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_55001](/schnittstellen/202604/pruefi/UTILMD/PI_55001) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55001](/schnittstellen/202604/pruefi/UTILMD/PI_55001) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55010](/schnittstellen/202604/pruefi/UTILMD/PI_55010) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55013](/schnittstellen/202604/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55013](/schnittstellen/202604/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55013](/schnittstellen/202604/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_55013](/schnittstellen/202604/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_55013](/schnittstellen/202604/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_55013](/schnittstellen/202604/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_55014](/schnittstellen/202604/pruefi/UTILMD/PI_55014) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55014](/schnittstellen/202604/pruefi/UTILMD/PI_55014) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55039](/schnittstellen/202604/pruefi/UTILMD/PI_55039) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_55040](/schnittstellen/202604/pruefi/UTILMD/PI_55040) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_55042](/schnittstellen/202604/pruefi/UTILMD/PI_55042) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_55042](/schnittstellen/202604/pruefi/UTILMD/PI_55042) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_55042](/schnittstellen/202604/pruefi/UTILMD/PI_55042) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_55109](/schnittstellen/202604/pruefi/UTILMD/PI_55109) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55109](/schnittstellen/202604/pruefi/UTILMD/PI_55109) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55110](/schnittstellen/202604/pruefi/UTILMD/PI_55110) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55110](/schnittstellen/202604/pruefi/UTILMD/PI_55110) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55136](/schnittstellen/202604/pruefi/UTILMD/PI_55136) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55136](/schnittstellen/202604/pruefi/UTILMD/PI_55136) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55137](/schnittstellen/202604/pruefi/UTILMD/PI_55137) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55137](/schnittstellen/202604/pruefi/UTILMD/PI_55137) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_55600](/schnittstellen/202604/pruefi/UTILMD/PI_55600) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55600](/schnittstellen/202604/pruefi/UTILMD/PI_55600) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55601](/schnittstellen/202604/pruefi/UTILMD/PI_55601) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55601](/schnittstellen/202604/pruefi/UTILMD/PI_55601) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55616](/schnittstellen/202604/pruefi/UTILMD/PI_55616) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_55616](/schnittstellen/202604/pruefi/UTILMD/PI_55616) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_55616](/schnittstellen/202604/pruefi/UTILMD/PI_55616) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_55616](/schnittstellen/202604/pruefi/UTILMD/PI_55616) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_55622](/schnittstellen/202604/pruefi/UTILMD/PI_55622) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_55622](/schnittstellen/202604/pruefi/UTILMD/PI_55622) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_55622](/schnittstellen/202604/pruefi/UTILMD/PI_55622) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_55622](/schnittstellen/202604/pruefi/UTILMD/PI_55622) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_55628](/schnittstellen/202604/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_55628](/schnittstellen/202604/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_55628](/schnittstellen/202604/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_55628](/schnittstellen/202604/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_55634](/schnittstellen/202604/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_55634](/schnittstellen/202604/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_55634](/schnittstellen/202604/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_55634](/schnittstellen/202604/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_55643](/schnittstellen/202604/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_55643](/schnittstellen/202604/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_55643](/schnittstellen/202604/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_55648](/schnittstellen/202604/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_55648](/schnittstellen/202604/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_55648](/schnittstellen/202604/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_55653](/schnittstellen/202604/pruefi/UTILMD/PI_55653) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_55658](/schnittstellen/202604/pruefi/UTILMD/PI_55658) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_55663](/schnittstellen/202604/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_55663](/schnittstellen/202604/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_55663](/schnittstellen/202604/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_55669](/schnittstellen/202604/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_55669](/schnittstellen/202604/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_55669](/schnittstellen/202604/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |

### name2

151 Verwendung(en) in den Nachrichtentypen IFTSTA, ORDERS, ORDRSP, UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_17101](/schnittstellen/202604/pruefi/ORDERS/PI_17101) | Prüfi | ORDERS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_17126](/schnittstellen/202604/pruefi/ORDERS/PI_17126) | Prüfi | ORDERS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_19015](/schnittstellen/202604/pruefi/ORDRSP/PI_19015) | Prüfi | ORDRSP | stammdaten › AUFTRAG › lieferadresseAltgeraete |
| [PI_21045](/schnittstellen/202604/pruefi/IFTSTA/PI_21045) | Prüfi | IFTSTA | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44001](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44001) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_44001](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44001) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44001](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44001) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44010](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44010) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44016](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44016) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44017](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44017) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44019](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44019) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44020](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44020) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44021](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44021) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44035](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44035) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44039](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44039) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_44040](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44040) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_44043](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44043) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44043](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44043) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_44043](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44043) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_44109](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44109) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_44109](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44109) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44112](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44112) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_44112](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44112) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_44112](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44112) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_44112](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44112) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_44113](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44113) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_44113](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44113) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_44113](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44113) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_44113](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44113) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_44137](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44137) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_44137](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44137) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44138](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44138) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_44138](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44138) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44139](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44139) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_44139](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44139) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_44139](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44139) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_44139](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44139) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_44140](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44140) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_44140](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44140) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_44140](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44140) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_44140](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44140) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_44142](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44142) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_44142](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44142) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_44142](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44142) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_44142](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44142) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_44159](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44159) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44159](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44159) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_44159](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44159) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_44160](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44160) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44162](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44162) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44163](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44163) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44165](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44165) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44166](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44166) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44166](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44166) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_44166](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44166) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_44167](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44167) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44167](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44167) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_44167](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44167) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_44168](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44168](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_44168](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_44168](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_44168](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_55001](/schnittstellen/202604/pruefi/UTILMD/PI_55001) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55001](/schnittstellen/202604/pruefi/UTILMD/PI_55001) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55010](/schnittstellen/202604/pruefi/UTILMD/PI_55010) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55013](/schnittstellen/202604/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55013](/schnittstellen/202604/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55013](/schnittstellen/202604/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_55013](/schnittstellen/202604/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_55013](/schnittstellen/202604/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_55013](/schnittstellen/202604/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_55014](/schnittstellen/202604/pruefi/UTILMD/PI_55014) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55014](/schnittstellen/202604/pruefi/UTILMD/PI_55014) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55039](/schnittstellen/202604/pruefi/UTILMD/PI_55039) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_55040](/schnittstellen/202604/pruefi/UTILMD/PI_55040) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_55042](/schnittstellen/202604/pruefi/UTILMD/PI_55042) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_55042](/schnittstellen/202604/pruefi/UTILMD/PI_55042) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_55042](/schnittstellen/202604/pruefi/UTILMD/PI_55042) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_55109](/schnittstellen/202604/pruefi/UTILMD/PI_55109) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55109](/schnittstellen/202604/pruefi/UTILMD/PI_55109) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55110](/schnittstellen/202604/pruefi/UTILMD/PI_55110) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55110](/schnittstellen/202604/pruefi/UTILMD/PI_55110) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55136](/schnittstellen/202604/pruefi/UTILMD/PI_55136) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55136](/schnittstellen/202604/pruefi/UTILMD/PI_55136) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55137](/schnittstellen/202604/pruefi/UTILMD/PI_55137) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55137](/schnittstellen/202604/pruefi/UTILMD/PI_55137) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_55600](/schnittstellen/202604/pruefi/UTILMD/PI_55600) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55600](/schnittstellen/202604/pruefi/UTILMD/PI_55600) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55601](/schnittstellen/202604/pruefi/UTILMD/PI_55601) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55601](/schnittstellen/202604/pruefi/UTILMD/PI_55601) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55616](/schnittstellen/202604/pruefi/UTILMD/PI_55616) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_55616](/schnittstellen/202604/pruefi/UTILMD/PI_55616) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_55616](/schnittstellen/202604/pruefi/UTILMD/PI_55616) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_55616](/schnittstellen/202604/pruefi/UTILMD/PI_55616) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_55622](/schnittstellen/202604/pruefi/UTILMD/PI_55622) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_55622](/schnittstellen/202604/pruefi/UTILMD/PI_55622) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_55622](/schnittstellen/202604/pruefi/UTILMD/PI_55622) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_55622](/schnittstellen/202604/pruefi/UTILMD/PI_55622) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_55628](/schnittstellen/202604/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_55628](/schnittstellen/202604/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_55628](/schnittstellen/202604/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_55628](/schnittstellen/202604/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_55634](/schnittstellen/202604/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_55634](/schnittstellen/202604/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_55634](/schnittstellen/202604/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_55634](/schnittstellen/202604/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_55643](/schnittstellen/202604/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_55643](/schnittstellen/202604/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_55643](/schnittstellen/202604/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_55648](/schnittstellen/202604/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_55648](/schnittstellen/202604/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_55648](/schnittstellen/202604/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_55653](/schnittstellen/202604/pruefi/UTILMD/PI_55653) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_55658](/schnittstellen/202604/pruefi/UTILMD/PI_55658) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_55663](/schnittstellen/202604/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_55663](/schnittstellen/202604/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_55663](/schnittstellen/202604/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_55669](/schnittstellen/202604/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_55669](/schnittstellen/202604/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_55669](/schnittstellen/202604/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |

### name3

151 Verwendung(en) in den Nachrichtentypen IFTSTA, ORDERS, ORDRSP, UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_17101](/schnittstellen/202604/pruefi/ORDERS/PI_17101) | Prüfi | ORDERS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_17126](/schnittstellen/202604/pruefi/ORDERS/PI_17126) | Prüfi | ORDERS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_19015](/schnittstellen/202604/pruefi/ORDRSP/PI_19015) | Prüfi | ORDRSP | stammdaten › AUFTRAG › lieferadresseAltgeraete |
| [PI_21045](/schnittstellen/202604/pruefi/IFTSTA/PI_21045) | Prüfi | IFTSTA | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44001](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44001) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_44001](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44001) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44001](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44001) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44010](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44010) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44016](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44016) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44017](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44017) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44019](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44019) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44020](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44020) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44021](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44021) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44035](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44035) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44039](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44039) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_44040](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44040) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_44043](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44043) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44043](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44043) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_44043](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44043) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_44109](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44109) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_44109](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44109) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44112](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44112) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_44112](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44112) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_44112](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44112) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_44112](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44112) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_44113](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44113) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_44113](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44113) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_44113](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44113) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_44113](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44113) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_44137](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44137) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_44137](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44137) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44138](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44138) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_44138](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44138) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44139](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44139) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_44139](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44139) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_44139](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44139) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_44139](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44139) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_44140](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44140) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_44140](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44140) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_44140](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44140) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_44140](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44140) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_44142](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44142) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_44142](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44142) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_44142](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44142) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_44142](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44142) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_44159](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44159) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44159](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44159) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_44159](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44159) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_44160](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44160) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44162](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44162) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44163](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44163) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44165](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44165) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44166](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44166) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44166](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44166) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_44166](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44166) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_44167](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44167) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44167](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44167) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_44167](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44167) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_44168](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44168](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_44168](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_44168](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_44168](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_55001](/schnittstellen/202604/pruefi/UTILMD/PI_55001) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55001](/schnittstellen/202604/pruefi/UTILMD/PI_55001) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55010](/schnittstellen/202604/pruefi/UTILMD/PI_55010) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55013](/schnittstellen/202604/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55013](/schnittstellen/202604/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55013](/schnittstellen/202604/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_55013](/schnittstellen/202604/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_55013](/schnittstellen/202604/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_55013](/schnittstellen/202604/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_55014](/schnittstellen/202604/pruefi/UTILMD/PI_55014) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55014](/schnittstellen/202604/pruefi/UTILMD/PI_55014) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55039](/schnittstellen/202604/pruefi/UTILMD/PI_55039) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_55040](/schnittstellen/202604/pruefi/UTILMD/PI_55040) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_55042](/schnittstellen/202604/pruefi/UTILMD/PI_55042) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_55042](/schnittstellen/202604/pruefi/UTILMD/PI_55042) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_55042](/schnittstellen/202604/pruefi/UTILMD/PI_55042) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_55109](/schnittstellen/202604/pruefi/UTILMD/PI_55109) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55109](/schnittstellen/202604/pruefi/UTILMD/PI_55109) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55110](/schnittstellen/202604/pruefi/UTILMD/PI_55110) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55110](/schnittstellen/202604/pruefi/UTILMD/PI_55110) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55136](/schnittstellen/202604/pruefi/UTILMD/PI_55136) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55136](/schnittstellen/202604/pruefi/UTILMD/PI_55136) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55137](/schnittstellen/202604/pruefi/UTILMD/PI_55137) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55137](/schnittstellen/202604/pruefi/UTILMD/PI_55137) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_55600](/schnittstellen/202604/pruefi/UTILMD/PI_55600) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55600](/schnittstellen/202604/pruefi/UTILMD/PI_55600) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55601](/schnittstellen/202604/pruefi/UTILMD/PI_55601) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55601](/schnittstellen/202604/pruefi/UTILMD/PI_55601) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55616](/schnittstellen/202604/pruefi/UTILMD/PI_55616) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_55616](/schnittstellen/202604/pruefi/UTILMD/PI_55616) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_55616](/schnittstellen/202604/pruefi/UTILMD/PI_55616) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_55616](/schnittstellen/202604/pruefi/UTILMD/PI_55616) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_55622](/schnittstellen/202604/pruefi/UTILMD/PI_55622) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_55622](/schnittstellen/202604/pruefi/UTILMD/PI_55622) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_55622](/schnittstellen/202604/pruefi/UTILMD/PI_55622) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_55622](/schnittstellen/202604/pruefi/UTILMD/PI_55622) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_55628](/schnittstellen/202604/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_55628](/schnittstellen/202604/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_55628](/schnittstellen/202604/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_55628](/schnittstellen/202604/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_55634](/schnittstellen/202604/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_55634](/schnittstellen/202604/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_55634](/schnittstellen/202604/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_55634](/schnittstellen/202604/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_55643](/schnittstellen/202604/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_55643](/schnittstellen/202604/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_55643](/schnittstellen/202604/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_55648](/schnittstellen/202604/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_55648](/schnittstellen/202604/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_55648](/schnittstellen/202604/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_55653](/schnittstellen/202604/pruefi/UTILMD/PI_55653) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_55658](/schnittstellen/202604/pruefi/UTILMD/PI_55658) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_55663](/schnittstellen/202604/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_55663](/schnittstellen/202604/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_55663](/schnittstellen/202604/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_55669](/schnittstellen/202604/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_55669](/schnittstellen/202604/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_55669](/schnittstellen/202604/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |

### name4

151 Verwendung(en) in den Nachrichtentypen IFTSTA, ORDERS, ORDRSP, UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_17101](/schnittstellen/202604/pruefi/ORDERS/PI_17101) | Prüfi | ORDERS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_17126](/schnittstellen/202604/pruefi/ORDERS/PI_17126) | Prüfi | ORDERS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_19015](/schnittstellen/202604/pruefi/ORDRSP/PI_19015) | Prüfi | ORDRSP | stammdaten › AUFTRAG › lieferadresseAltgeraete |
| [PI_21045](/schnittstellen/202604/pruefi/IFTSTA/PI_21045) | Prüfi | IFTSTA | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44001](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44001) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_44001](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44001) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44001](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44001) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44010](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44010) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44016](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44016) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44017](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44017) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44019](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44019) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44020](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44020) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44021](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44021) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44035](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44035) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44039](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44039) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_44040](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44040) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_44043](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44043) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44043](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44043) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_44043](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44043) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_44109](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44109) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_44109](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44109) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44112](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44112) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_44112](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44112) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_44112](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44112) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_44112](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44112) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_44113](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44113) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_44113](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44113) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_44113](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44113) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_44113](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44113) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_44137](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44137) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_44137](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44137) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44138](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44138) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_44138](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44138) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44139](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44139) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_44139](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44139) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_44139](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44139) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_44139](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44139) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_44140](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44140) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_44140](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44140) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_44140](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44140) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_44140](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44140) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_44142](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44142) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_44142](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44142) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_44142](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44142) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_44142](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44142) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_44159](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44159) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44159](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44159) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_44159](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44159) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_44160](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44160) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44162](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44162) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44163](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44163) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44165](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44165) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44166](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44166) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44166](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44166) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_44166](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44166) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_44167](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44167) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44167](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44167) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_44167](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44167) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_44168](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44168](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_44168](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_44168](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_44168](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_55001](/schnittstellen/202604/pruefi/UTILMD/PI_55001) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55001](/schnittstellen/202604/pruefi/UTILMD/PI_55001) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55010](/schnittstellen/202604/pruefi/UTILMD/PI_55010) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55013](/schnittstellen/202604/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55013](/schnittstellen/202604/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55013](/schnittstellen/202604/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_55013](/schnittstellen/202604/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_55013](/schnittstellen/202604/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_55013](/schnittstellen/202604/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_55014](/schnittstellen/202604/pruefi/UTILMD/PI_55014) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55014](/schnittstellen/202604/pruefi/UTILMD/PI_55014) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55039](/schnittstellen/202604/pruefi/UTILMD/PI_55039) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_55040](/schnittstellen/202604/pruefi/UTILMD/PI_55040) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_55042](/schnittstellen/202604/pruefi/UTILMD/PI_55042) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_55042](/schnittstellen/202604/pruefi/UTILMD/PI_55042) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_55042](/schnittstellen/202604/pruefi/UTILMD/PI_55042) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_55109](/schnittstellen/202604/pruefi/UTILMD/PI_55109) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55109](/schnittstellen/202604/pruefi/UTILMD/PI_55109) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55110](/schnittstellen/202604/pruefi/UTILMD/PI_55110) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55110](/schnittstellen/202604/pruefi/UTILMD/PI_55110) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55136](/schnittstellen/202604/pruefi/UTILMD/PI_55136) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55136](/schnittstellen/202604/pruefi/UTILMD/PI_55136) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55137](/schnittstellen/202604/pruefi/UTILMD/PI_55137) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55137](/schnittstellen/202604/pruefi/UTILMD/PI_55137) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_55600](/schnittstellen/202604/pruefi/UTILMD/PI_55600) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55600](/schnittstellen/202604/pruefi/UTILMD/PI_55600) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55601](/schnittstellen/202604/pruefi/UTILMD/PI_55601) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_55601](/schnittstellen/202604/pruefi/UTILMD/PI_55601) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55616](/schnittstellen/202604/pruefi/UTILMD/PI_55616) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_55616](/schnittstellen/202604/pruefi/UTILMD/PI_55616) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_55616](/schnittstellen/202604/pruefi/UTILMD/PI_55616) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_55616](/schnittstellen/202604/pruefi/UTILMD/PI_55616) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_55622](/schnittstellen/202604/pruefi/UTILMD/PI_55622) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_55622](/schnittstellen/202604/pruefi/UTILMD/PI_55622) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_55622](/schnittstellen/202604/pruefi/UTILMD/PI_55622) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_55622](/schnittstellen/202604/pruefi/UTILMD/PI_55622) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_55628](/schnittstellen/202604/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_55628](/schnittstellen/202604/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_55628](/schnittstellen/202604/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_55628](/schnittstellen/202604/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_55634](/schnittstellen/202604/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_55634](/schnittstellen/202604/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_55634](/schnittstellen/202604/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_55634](/schnittstellen/202604/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_55643](/schnittstellen/202604/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_55643](/schnittstellen/202604/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_55643](/schnittstellen/202604/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_55648](/schnittstellen/202604/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_55648](/schnittstellen/202604/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_55648](/schnittstellen/202604/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_55653](/schnittstellen/202604/pruefi/UTILMD/PI_55653) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_55658](/schnittstellen/202604/pruefi/UTILMD/PI_55658) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_55663](/schnittstellen/202604/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_55663](/schnittstellen/202604/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_55663](/schnittstellen/202604/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_55669](/schnittstellen/202604/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_55669](/schnittstellen/202604/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_55669](/schnittstellen/202604/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |

### gewerbekennzeichnung

96 Verwendung(en) in den Nachrichtentypen IFTSTA, ORDERS, ORDRSP, UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_17101](/schnittstellen/202604/pruefi/ORDERS/PI_17101) | Prüfi | ORDERS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_17126](/schnittstellen/202604/pruefi/ORDERS/PI_17126) | Prüfi | ORDERS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_19015](/schnittstellen/202604/pruefi/ORDRSP/PI_19015) | Prüfi | ORDRSP | stammdaten › AUFTRAG › lieferadresseAltgeraete |
| [PI_21045](/schnittstellen/202604/pruefi/IFTSTA/PI_21045) | Prüfi | IFTSTA | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44001](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44001) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_44001](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44001) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44001](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44001) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44010](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44010) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44016](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44016) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44017](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44017) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44019](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44019) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44020](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44020) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44021](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44021) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44035](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44035) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44039](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44039) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_44040](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44040) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_44043](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44043) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44043](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44043) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_44043](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44043) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_44109](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44109) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_44109](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44109) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44112](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44112) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_44112](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44112) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_44112](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44112) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_44112](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44112) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_44113](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44113) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_44113](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44113) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_44113](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44113) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_44113](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44113) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_44137](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44137) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_44137](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44137) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44138](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44138) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner |
| [PI_44138](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44138) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_44139](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44139) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_44139](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44139) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_44139](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44139) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_44139](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44139) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_44140](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44140) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_44140](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44140) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_44140](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44140) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_44140](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44140) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_44142](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44142) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_44142](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44142) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_44142](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44142) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_44142](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44142) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_44159](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44159) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44159](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44159) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_44159](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44159) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_44160](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44160) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44162](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44162) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44163](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44163) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44165](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44165) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44166](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44166) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44166](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44166) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_44166](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44166) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_44167](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44167) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44167](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44167) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_44167](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44167) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_44168](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_44168](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner |
| [PI_44168](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_44168](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner |
| [PI_44168](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_55013](/schnittstellen/202604/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_55013](/schnittstellen/202604/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_55042](/schnittstellen/202604/pruefi/UTILMD/PI_55042) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_55616](/schnittstellen/202604/pruefi/UTILMD/PI_55616) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_55616](/schnittstellen/202604/pruefi/UTILMD/PI_55616) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_55622](/schnittstellen/202604/pruefi/UTILMD/PI_55622) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_55622](/schnittstellen/202604/pruefi/UTILMD/PI_55622) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_55628](/schnittstellen/202604/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_55628](/schnittstellen/202604/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_55634](/schnittstellen/202604/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › eigentuemer |
| [PI_55634](/schnittstellen/202604/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › hausverwalter |
| [PI_55643](/schnittstellen/202604/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_55648](/schnittstellen/202604/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_55653](/schnittstellen/202604/pruefi/UTILMD/PI_55653) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_55658](/schnittstellen/202604/pruefi/UTILMD/PI_55658) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_55663](/schnittstellen/202604/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |
| [PI_55669](/schnittstellen/202604/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | stammdaten › MESSLOKATION › ablesekartenempfaenger |

### geschaeftspartnerrolle

32 Verwendung(en) in den Nachrichtentypen IFTSTA, ORDERS, UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_17101](/schnittstellen/202604/pruefi/ORDERS/PI_17101) | Prüfi | ORDERS | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_17126](/schnittstellen/202604/pruefi/ORDERS/PI_17126) | Prüfi | ORDERS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_21045](/schnittstellen/202604/pruefi/IFTSTA/PI_21045) | Prüfi | IFTSTA | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55001](/schnittstellen/202604/pruefi/UTILMD/PI_55001) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55010](/schnittstellen/202604/pruefi/UTILMD/PI_55010) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55013](/schnittstellen/202604/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55013](/schnittstellen/202604/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_55014](/schnittstellen/202604/pruefi/UTILMD/PI_55014) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55039](/schnittstellen/202604/pruefi/UTILMD/PI_55039) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_55040](/schnittstellen/202604/pruefi/UTILMD/PI_55040) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_55042](/schnittstellen/202604/pruefi/UTILMD/PI_55042) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_55109](/schnittstellen/202604/pruefi/UTILMD/PI_55109) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55110](/schnittstellen/202604/pruefi/UTILMD/PI_55110) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55136](/schnittstellen/202604/pruefi/UTILMD/PI_55136) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55137](/schnittstellen/202604/pruefi/UTILMD/PI_55137) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_55600](/schnittstellen/202604/pruefi/UTILMD/PI_55600) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55601](/schnittstellen/202604/pruefi/UTILMD/PI_55601) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragspartner2 |
| [PI_55616](/schnittstellen/202604/pruefi/UTILMD/PI_55616) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_55622](/schnittstellen/202604/pruefi/UTILMD/PI_55622) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_55628](/schnittstellen/202604/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_55634](/schnittstellen/202604/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › vertragspartner2 |
| [PI_55643](/schnittstellen/202604/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_55648](/schnittstellen/202604/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_55663](/schnittstellen/202604/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |
| [PI_55669](/schnittstellen/202604/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragspartner2 |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
