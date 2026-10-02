# Netzlokation
<span hidden data-pagefind-meta={"title:Netzlokation — BO4E-Geschäftsobjekt (FV 202604)"} />

BO4E-Geschäftsobjekt · 18 Felder · 104 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="botyp"></a>`boTyp` <span className="hbs-pflicht">\*</span> | [Enum BOTyp](/bo4e/202604/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> | Typ des BO |
| <a id="versionstruktur"></a>`versionStruktur` <span className="hbs-pflicht">\*</span> | string | versionStruktur |
| <a id="netzlokationsid"></a>`netzlokationsId` | string | Identifikationsnummer einer Netzlokation, an der Energie entweder verbraucht, oder erzeugt wird (Like MarktlokationsId Marktlokation) |
| <a id="sparte"></a>`sparte` | [Enum Sparte](/bo4e/202604/enum/Sparte)<br/><Werte>`STROM`, `GAS`, `FERNWAERME`, `NAHWAERME`, `WASSER`, `ABWASSER`</Werte> | Sparte der Netzlokation, z.B. Gas oder Strom. |
| <a id="netzanschlussleistung"></a>`netzanschlussleistung` | string | Netzanschlussleistungsmenge der Netzlokation |
| <a id="grundzustaendigermsbcodenr"></a>`grundzustaendigerMSBCodeNr` | string | Codenummer des grundzuständigen Messstellenbetreibers, der für diese Netzlokation zuständig ist. |
| <a id="steuerkanal"></a>`steuerkanal` | boolean | Ob ein Steuerkanal der Netzlokation zugeordnet ist und somit die Netzlokation gesteuert werden kann. ZF2: Kein Steuerkanal vorhanden ZF3: Steuerkanal vorhanden |
| <a id="lokationszuordnung"></a>`lokationszuordnung` | [Enum Lokationszuordnung](/bo4e/202604/enum/Lokationszuordnung)<br/><Werte>`UNVERAENDERT`, `BEGINNT`, `ENDET`</Werte> | Lokationszuordnung |
| <a id="produktdatenrelevanterolle"></a>`produktdatenRelevanteRolle` | [Enum Marktrolle](/bo4e/202604/enum/Marktrolle)<br/><Werte>`NB`, `LF`, `MSB`, `MSBA`, `GMSB`, `MDL`, `DL`, `BKV`, `UENB`, `KUNDE-SELBST-NN`, `MGV`, `EIV`, `RB`, `KUNDE`, `INTERESSENT`, `KN`, `UBA`, `BIKO`, `ESA`</Werte> | Diese Rollen kann ein Marktteilnehmer einnehmen |
| <a id="auftraggebendermarktpartner"></a>`auftraggebenderMarktpartner` | [Marktteilnehmer](/bo4e/202604/bo/Marktteilnehmer) | — |
| <a id="konfigurationsprodukt"></a>`konfigurationsprodukt` | string | konfigurationsprodukt |
| <a id="keinkonfigurationsprodukt"></a>`keinKonfigurationsprodukt` | boolean | keinKonfigurationsprodukt |
| <a id="leistungskurvendefinition"></a>`leistungskurvendefinition` | string | Code der Zugeordnete Leistungskurvendefinition für das Objekt |
| <a id="marktrollen"></a>`marktrollen` | [Marktteilnehmer[]](/bo4e/202604/bo/Marktteilnehmer) | marktrollen |
| <a id="zaehlwerke"></a>`zaehlwerke` | [Zaehlwerk[]](/bo4e/202604/com/Zaehlwerk) | zaehlwerke |
| <a id="abrechnungsdaten"></a>`abrechnungsdaten` | [Netznutzungsabrechnungsdaten[]](/bo4e/202604/com/Netznutzungsabrechnungsdaten) | abrechnungsdaten |
| <a id="datenqualitaet"></a>`datenqualitaet` | [Enum Datenqualitaet](/bo4e/202604/enum/Datenqualitaet)<br/><Werte>`ERWARTETE_DATEN`, `IM_SYSTEM_VORHANDENE_DATEN`, `INFORMATIVE_DATEN`, `GUELTIGE_DATEN`, `KEINE_DATEN`, `IM_SYSTEM_KEINE_DATEN_VORHANDEN`, `KEINE_DATEN_ERWARTET`, `DIFFERENZ_DATEN`, `DIFFERENZ_ERWARTETE_DATEN`, `DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</Werte> | Datenqualitaet |
| <a id="gueltigkeitszeitraum"></a>`gueltigkeitszeitraum` | [Zeitraum](/bo4e/202604/com/Zeitraum) | — |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[boTyp](/bo4e/202604/bo/Netzlokation#botyp) <span className="hbs-pflicht">\*</span></span> | Typ des BO | [Enum BOTyp](/bo4e/202604/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> |
| <span className="hbs-f hbs-e0">[versionStruktur](/bo4e/202604/bo/Netzlokation#versionstruktur) <span className="hbs-pflicht">\*</span></span> | versionStruktur | string |
| <span className="hbs-f hbs-e0">[netzlokationsId](/bo4e/202604/bo/Netzlokation#netzlokationsid)</span> | Identifikationsnummer einer Netzlokation, an der Energie entweder<br/>verbraucht, oder erzeugt wird (Like MarktlokationsId Marktlokation) | string |
| <span className="hbs-f hbs-e0">[sparte](/bo4e/202604/bo/Netzlokation#sparte)</span> | Sparte der Netzlokation, z.B. Gas oder Strom. | [Enum Sparte](/bo4e/202604/enum/Sparte)<br/><Werte>`STROM`, `GAS`, `FERNWAERME`, `NAHWAERME`, `WASSER`, `ABWASSER`</Werte> |
| <span className="hbs-f hbs-e0">[netzanschlussleistung](/bo4e/202604/bo/Netzlokation#netzanschlussleistung)</span> | Netzanschlussleistungsmenge der Netzlokation | string |
| <span className="hbs-f hbs-e0">[grundzustaendigerMSBCodeNr](/bo4e/202604/bo/Netzlokation#grundzustaendigermsbcodenr)</span> | Codenummer des grundzuständigen Messstellenbetreibers, der für diese<br/>Netzlokation zuständig ist. | string |
| <span className="hbs-f hbs-e0">[steuerkanal](/bo4e/202604/bo/Netzlokation#steuerkanal)</span> | Ob ein Steuerkanal der Netzlokation zugeordnet ist und somit die Netzlokation gesteuert<br/>werden kann.<br/>ZF2: Kein Steuerkanal vorhanden<br/>ZF3: Steuerkanal vorhanden | boolean |
| <span className="hbs-f hbs-e0">[lokationszuordnung](/bo4e/202604/bo/Netzlokation#lokationszuordnung)</span> | Lokationszuordnung | [Enum Lokationszuordnung](/bo4e/202604/enum/Lokationszuordnung)<br/><Werte>`UNVERAENDERT`, `BEGINNT`, `ENDET`</Werte> |
| <span className="hbs-f hbs-e0">[produktdatenRelevanteRolle](/bo4e/202604/bo/Netzlokation#produktdatenrelevanterolle)</span> | Diese Rollen kann ein Marktteilnehmer einnehmen | [Enum Marktrolle](/bo4e/202604/enum/Marktrolle)<br/><Werte>`NB`, `LF`, `MSB`, `MSBA`, `GMSB`, `MDL`, `DL`, `BKV`, `UENB`, `KUNDE-SELBST-NN`, `MGV`, `EIV`, `RB`, `KUNDE`, `INTERESSENT`, `KN`, `UBA`, `BIKO`, `ESA`</Werte> |
| <span className="hbs-g hbs-e0">[auftraggebenderMarktpartner](/bo4e/202604/bo/Netzlokation#auftraggebendermarktpartner)</span> | — | [Marktteilnehmer](/bo4e/202604/bo/Marktteilnehmer) |
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
| <span className="hbs-f hbs-e0">[konfigurationsprodukt](/bo4e/202604/bo/Netzlokation#konfigurationsprodukt)</span> | konfigurationsprodukt | string |
| <span className="hbs-f hbs-e0">[keinKonfigurationsprodukt](/bo4e/202604/bo/Netzlokation#keinkonfigurationsprodukt)</span> | keinKonfigurationsprodukt | boolean |
| <span className="hbs-f hbs-e0">[leistungskurvendefinition](/bo4e/202604/bo/Netzlokation#leistungskurvendefinition)</span> | Code der Zugeordnete Leistungskurvendefinition für das Objekt | string |
| <span className="hbs-g hbs-e0">[marktrollen](/bo4e/202604/bo/Netzlokation#marktrollen) <span className="hbs-liste">[ ]</span></span> | marktrollen | [Marktteilnehmer[]](/bo4e/202604/bo/Marktteilnehmer) |
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
| <span className="hbs-g hbs-e0">[zaehlwerke](/bo4e/202604/bo/Netzlokation#zaehlwerke) <span className="hbs-liste">[ ]</span></span> | zaehlwerke | [Zaehlwerk[]](/bo4e/202604/com/Zaehlwerk) |
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
| <span className="hbs-g hbs-e0">[abrechnungsdaten](/bo4e/202604/bo/Netzlokation#abrechnungsdaten) <span className="hbs-liste">[ ]</span></span> | abrechnungsdaten | [Netznutzungsabrechnungsdaten[]](/bo4e/202604/com/Netznutzungsabrechnungsdaten) |
| <span className="hbs-f hbs-e1">[artikelId](/bo4e/202604/com/Netznutzungsabrechnungsdaten#artikelid)</span> | artikelId | string |
| <span className="hbs-f hbs-e1">[artikelIdTyp](/bo4e/202604/com/Netznutzungsabrechnungsdaten#artikelidtyp)</span> | Liste von Artikel-IDs, z.B. für standardisierte vom BDEW herausgegebene Artikel, die im Strommarkt die BDEW-Artikelnummer ablösen | [Enum ArtikelIdTyp](/bo4e/202604/enum/ArtikelIdTyp)<br/><Werte>`ARTIKELID`, `GRUPPENARTIKELID`</Werte> |
| <span className="hbs-f hbs-e1">[anzahl](/bo4e/202604/com/Netznutzungsabrechnungsdaten#anzahl)</span> | Anzahl | integer |
| <span className="hbs-f hbs-e1">[gemeinderabatt](/bo4e/202604/com/Netznutzungsabrechnungsdaten#gemeinderabatt)</span> | Gemeinderabatt | number (float) |
| <span className="hbs-f hbs-e1">[zuschlag](/bo4e/202604/com/Netznutzungsabrechnungsdaten#zuschlag)</span> | Zuschlag | number (float) |
| <span className="hbs-f hbs-e1">[abschlag](/bo4e/202604/com/Netznutzungsabrechnungsdaten#abschlag)</span> | Abschlag | number (float) |
| <span className="hbs-g hbs-e1">[singulaereBetriebsmittel](/bo4e/202604/com/Netznutzungsabrechnungsdaten#singulaerebetriebsmittel)</span> | — | [Menge](/bo4e/202604/com/Menge) |
| <span className="hbs-f hbs-e2">[wert](/bo4e/202604/com/Menge#wert)</span> | Wert | number (float) |
| <span className="hbs-f hbs-e2">[einheit](/bo4e/202604/com/Menge#einheit)</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202604/enum/Mengeneinheit)<br/><Werte>`W`, `WH`, `KW`, `KWH`, `KVARH`, `MW`, `MWH`, `STUECK`, `KUBIKMETER`, `STUNDE`, `TAG`, `MONAT`, `JAHR`, `PROZENT`, `ANZAHL`, `VAR`, `KVAR`, `VARH`, `KWHK`, `Z16`, `KWT`, `WATT_PRO_QUADRATMETER`, `METER_PRO_SEKUNDE`</Werte> |
| <span className="hbs-f hbs-e2">[startdatum](/bo4e/202604/com/Menge#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e2">[enddatum](/bo4e/202604/com/Menge#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-g hbs-e1">[preisSingulaereBetriebsmittel](/bo4e/202604/com/Netznutzungsabrechnungsdaten#preissingulaerebetriebsmittel)</span> | — | [Preis](/bo4e/202604/com/Preis) |
| <span className="hbs-f hbs-e2">[wert](/bo4e/202604/com/Preis#wert)</span> | wert | number (float) |
| <span className="hbs-f hbs-e2">[menge](/bo4e/202604/com/Preis#menge)</span> | menge | integer |
| <span className="hbs-f hbs-e2">[minimaleMenge](/bo4e/202604/com/Preis#minimalemenge)</span> | minimale Menge | integer |
| <span className="hbs-f hbs-e2">[maximaleMenge](/bo4e/202604/com/Preis#maximalemenge)</span> | maximale Menge | integer |
| <span className="hbs-f hbs-e2">[einheit](/bo4e/202604/com/Preis#einheit)</span> | Waehrungseinheit | [Enum Waehrungseinheit](/bo4e/202604/enum/Waehrungseinheit)<br/><Werte>`EUR`, `CT`</Werte> |
| <span className="hbs-f hbs-e2">[bezugswert](/bo4e/202604/com/Preis#bezugswert)</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202604/enum/Mengeneinheit)<br/><Werte>`W`, `WH`, `KW`, `KWH`, `KVARH`, `MW`, `MWH`, `STUECK`, `KUBIKMETER`, `STUNDE`, `TAG`, `MONAT`, `JAHR`, `PROZENT`, `ANZAHL`, `VAR`, `KVAR`, `VARH`, `KWHK`, `Z16`, `KWT`, `WATT_PRO_QUADRATMETER`, `METER_PRO_SEKUNDE`</Werte> |
| <span className="hbs-f hbs-e2">[status](/bo4e/202604/com/Preis#status)</span> | Preisstatus | [Enum Preisstatus](/bo4e/202604/enum/Preisstatus)<br/><Werte>`VORLAEUFIG`, `ENDGUELTIG`</Werte> |
| <span className="hbs-f hbs-e2">[preisart](/bo4e/202604/com/Preis#preisart)</span> | Preisart Code | [Enum Preisart](/bo4e/202604/enum/Preisart)<br/><Werte>`EINRICHTUNGSPREIS`, `TRANSAKTIONSPREIS`, `BETRIEBSPREIS`</Werte> |
| <span className="hbs-f hbs-e1">[abrechnungBlindarbeit](/bo4e/202604/com/Netznutzungsabrechnungsdaten#abrechnungblindarbeit)</span> | abrechnungBlindarbeit | boolean |
| <span className="hbs-f hbs-e1">[zahlerBlindarbeit](/bo4e/202604/com/Netznutzungsabrechnungsdaten#zahlerblindarbeit)</span> | ZahlerBlindarbeit | [Enum ZahlerBlindarbeit](/bo4e/202604/enum/ZahlerBlindarbeit)<br/><Werte>`ANSCHLUSSNUTZER`, `LIEFERANT`, `NICHT_FESTGELEGT`</Werte> |
| <span className="hbs-f hbs-e1">[zahlerBlindarbeitLf](/bo4e/202604/com/Netznutzungsabrechnungsdaten#zahlerblindarbeitlf)</span> | Zahlung der Blindarbeit durch den Lieferanten | boolean |
| <span className="hbs-f hbs-e1">[differenzDaten](/bo4e/202604/com/Netznutzungsabrechnungsdaten#differenzdaten)</span> | differenzDaten | boolean |
| <span className="hbs-g hbs-e1">[zaehlzeiten](/bo4e/202604/com/Netznutzungsabrechnungsdaten#zaehlzeiten)</span> | — | [Zaehlzeitregister](/bo4e/202604/com/Zaehlzeitregister) |
| <span className="hbs-f hbs-e2">[register](/bo4e/202604/com/Zaehlzeitregister#register)</span> | Zählzeitregister | string |
| <span className="hbs-f hbs-e2">[zaehlzeitDefinition](/bo4e/202604/com/Zaehlzeitregister#zaehlzeitdefinition)</span> | Zählzeitdefinition | string |
| <span className="hbs-f hbs-e2">[schwachlastfaehig](/bo4e/202604/com/Zaehlzeitregister#schwachlastfaehig)</span> | Schwachlastfähigkeit des Registers | [Enum Schwachlastfaehig](/bo4e/202604/enum/Schwachlastfaehig)<br/><Werte>`SCHWACHLASTFAEHIG`, `NICHT_SCHWACHLASTFAEHIG`</Werte> |
| <span className="hbs-f hbs-e0">[datenqualitaet](/bo4e/202604/bo/Netzlokation#datenqualitaet)</span> | Datenqualitaet | [Enum Datenqualitaet](/bo4e/202604/enum/Datenqualitaet)<br/><Werte>`ERWARTETE_DATEN`, `IM_SYSTEM_VORHANDENE_DATEN`, `INFORMATIVE_DATEN`, `GUELTIGE_DATEN`, `KEINE_DATEN`, `IM_SYSTEM_KEINE_DATEN_VORHANDEN`, `KEINE_DATEN_ERWARTET`, `DIFFERENZ_DATEN`, `DIFFERENZ_ERWARTETE_DATEN`, `DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</Werte> |
| <span className="hbs-g hbs-e0">[gueltigkeitszeitraum](/bo4e/202604/bo/Netzlokation#gueltigkeitszeitraum)</span> | — | [Zeitraum](/bo4e/202604/com/Zeitraum) |
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

### netzlokationsId

38 Verwendung(en) in den Nachrichtentypen IFTSTA, QUOTES, REQOTE, UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_15003](/schnittstellen/202604/pruefi/QUOTES/PI_15003) | Prüfi | QUOTES | stammdaten › NETZLOKATION |
| [PI_15004](/schnittstellen/202604/pruefi/QUOTES/PI_15004) | Prüfi | QUOTES | stammdaten › NETZLOKATION |
| [PI_21025](/schnittstellen/202604/pruefi/IFTSTA/PI_21025) | Prüfi | IFTSTA | stammdaten › NETZLOKATION |
| [PI_21027](/schnittstellen/202604/pruefi/IFTSTA/PI_21027) | Prüfi | IFTSTA | stammdaten › NETZLOKATION |
| [PI_21033](/schnittstellen/202604/pruefi/IFTSTA/PI_21033) | Prüfi | IFTSTA | stammdaten › NETZLOKATION |
| [PI_35004](/schnittstellen/202604/pruefi/REQOTE/PI_35004) | Prüfi | REQOTE | stammdaten › NETZLOKATION |
| [PI_55002](/schnittstellen/202604/pruefi/UTILMD/PI_55002) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55013](/schnittstellen/202604/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55035](/schnittstellen/202604/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55052](/schnittstellen/202604/pruefi/UTILMD/PI_55052) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55060](/schnittstellen/202604/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55078](/schnittstellen/202604/pruefi/UTILMD/PI_55078) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55095](/schnittstellen/202604/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55173](/schnittstellen/202604/pruefi/UTILMD/PI_55173) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55175](/schnittstellen/202604/pruefi/UTILMD/PI_55175) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55177](/schnittstellen/202604/pruefi/UTILMD/PI_55177) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55180](/schnittstellen/202604/pruefi/UTILMD/PI_55180) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55225](/schnittstellen/202604/pruefi/UTILMD/PI_55225) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55227](/schnittstellen/202604/pruefi/UTILMD/PI_55227) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55230](/schnittstellen/202604/pruefi/UTILMD/PI_55230) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55232](/schnittstellen/202604/pruefi/UTILMD/PI_55232) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55602](/schnittstellen/202604/pruefi/UTILMD/PI_55602) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55603](/schnittstellen/202604/pruefi/UTILMD/PI_55603) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55607](/schnittstellen/202604/pruefi/UTILMD/PI_55607) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55615](/schnittstellen/202604/pruefi/UTILMD/PI_55615) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55621](/schnittstellen/202604/pruefi/UTILMD/PI_55621) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55627](/schnittstellen/202604/pruefi/UTILMD/PI_55627) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55633](/schnittstellen/202604/pruefi/UTILMD/PI_55633) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55639](/schnittstellen/202604/pruefi/UTILMD/PI_55639) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55644](/schnittstellen/202604/pruefi/UTILMD/PI_55644) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55649](/schnittstellen/202604/pruefi/UTILMD/PI_55649) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55654](/schnittstellen/202604/pruefi/UTILMD/PI_55654) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55659](/schnittstellen/202604/pruefi/UTILMD/PI_55659) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55664](/schnittstellen/202604/pruefi/UTILMD/PI_55664) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55690](/schnittstellen/202604/pruefi/UTILMD/PI_55690) | Prüfi | UTILMD | stammdaten › NETZLOKATION |

### steuerkanal

12 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55035](/schnittstellen/202604/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55060](/schnittstellen/202604/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55095](/schnittstellen/202604/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55639](/schnittstellen/202604/pruefi/UTILMD/PI_55639) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55644](/schnittstellen/202604/pruefi/UTILMD/PI_55644) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55649](/schnittstellen/202604/pruefi/UTILMD/PI_55649) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55654](/schnittstellen/202604/pruefi/UTILMD/PI_55654) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55659](/schnittstellen/202604/pruefi/UTILMD/PI_55659) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55664](/schnittstellen/202604/pruefi/UTILMD/PI_55664) | Prüfi | UTILMD | stammdaten › NETZLOKATION |

### produktdatenRelevanteRolle

9 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55639](/schnittstellen/202604/pruefi/UTILMD/PI_55639) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55644](/schnittstellen/202604/pruefi/UTILMD/PI_55644) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55649](/schnittstellen/202604/pruefi/UTILMD/PI_55649) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55654](/schnittstellen/202604/pruefi/UTILMD/PI_55654) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55659](/schnittstellen/202604/pruefi/UTILMD/PI_55659) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55664](/schnittstellen/202604/pruefi/UTILMD/PI_55664) | Prüfi | UTILMD | stammdaten › NETZLOKATION |

### konfigurationsprodukt

12 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55035](/schnittstellen/202604/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55060](/schnittstellen/202604/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55095](/schnittstellen/202604/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55639](/schnittstellen/202604/pruefi/UTILMD/PI_55639) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55644](/schnittstellen/202604/pruefi/UTILMD/PI_55644) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55649](/schnittstellen/202604/pruefi/UTILMD/PI_55649) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55654](/schnittstellen/202604/pruefi/UTILMD/PI_55654) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55659](/schnittstellen/202604/pruefi/UTILMD/PI_55659) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55664](/schnittstellen/202604/pruefi/UTILMD/PI_55664) | Prüfi | UTILMD | stammdaten › NETZLOKATION |

### keinKonfigurationsprodukt

6 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55639](/schnittstellen/202604/pruefi/UTILMD/PI_55639) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55644](/schnittstellen/202604/pruefi/UTILMD/PI_55644) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55649](/schnittstellen/202604/pruefi/UTILMD/PI_55649) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55654](/schnittstellen/202604/pruefi/UTILMD/PI_55654) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55659](/schnittstellen/202604/pruefi/UTILMD/PI_55659) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55664](/schnittstellen/202604/pruefi/UTILMD/PI_55664) | Prüfi | UTILMD | stammdaten › NETZLOKATION |

### leistungskurvendefinition

12 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55035](/schnittstellen/202604/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55060](/schnittstellen/202604/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55095](/schnittstellen/202604/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55639](/schnittstellen/202604/pruefi/UTILMD/PI_55639) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55644](/schnittstellen/202604/pruefi/UTILMD/PI_55644) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55649](/schnittstellen/202604/pruefi/UTILMD/PI_55649) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55654](/schnittstellen/202604/pruefi/UTILMD/PI_55654) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55659](/schnittstellen/202604/pruefi/UTILMD/PI_55659) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55664](/schnittstellen/202604/pruefi/UTILMD/PI_55664) | Prüfi | UTILMD | stammdaten › NETZLOKATION |

### datenqualitaet

15 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55225](/schnittstellen/202604/pruefi/UTILMD/PI_55225) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55227](/schnittstellen/202604/pruefi/UTILMD/PI_55227) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55230](/schnittstellen/202604/pruefi/UTILMD/PI_55230) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55232](/schnittstellen/202604/pruefi/UTILMD/PI_55232) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55615](/schnittstellen/202604/pruefi/UTILMD/PI_55615) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55621](/schnittstellen/202604/pruefi/UTILMD/PI_55621) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55627](/schnittstellen/202604/pruefi/UTILMD/PI_55627) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55633](/schnittstellen/202604/pruefi/UTILMD/PI_55633) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55639](/schnittstellen/202604/pruefi/UTILMD/PI_55639) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55644](/schnittstellen/202604/pruefi/UTILMD/PI_55644) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55649](/schnittstellen/202604/pruefi/UTILMD/PI_55649) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55654](/schnittstellen/202604/pruefi/UTILMD/PI_55654) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55659](/schnittstellen/202604/pruefi/UTILMD/PI_55659) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55664](/schnittstellen/202604/pruefi/UTILMD/PI_55664) | Prüfi | UTILMD | stammdaten › NETZLOKATION |
| [PI_55690](/schnittstellen/202604/pruefi/UTILMD/PI_55690) | Prüfi | UTILMD | stammdaten › NETZLOKATION |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
