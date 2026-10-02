# Auftrag
<span hidden data-pagefind-meta={"title:Auftrag — BO4E-Geschäftsobjekt (FV 202604)"} />

BO4E-Geschäftsobjekt · 20 Felder · 29 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="botyp"></a>`boTyp` <span className="hbs-pflicht">\*</span> | [Enum BOTyp](/bo4e/202604/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> | Typ des BO |
| <a id="versionstruktur"></a>`versionStruktur` <span className="hbs-pflicht">\*</span> | string | versionStruktur |
| <a id="ausfuehrungsdatum"></a>`ausfuehrungsdatum` | string (date-time) | Das Ausführungsdatum beschreibt zu welchem Zeitpunkt ein Auftrag ausgeführt werden soll. |
| <a id="fertigstellungsdatum"></a>`fertigstellungsdatum` | string (date-time) | Das Fertigstellungsdatum beschreibt zu welchem Zeitpunkt ein Auftrag ausgeführt wurde/wird. |
| <a id="startdatum"></a>`startdatum` | string (date-time) | Das Startdatum beschreibt zu welchem Zeitpunkt ein Auftrag gestartet wurde/wird. |
| <a id="enddatum"></a>`enddatum` | string (date-time) | Das Enddatum beschreibt zu welchem Zeitpunkt ein Auftrag endete oder enden wird. |
| <a id="sparte"></a>`sparte` | [Enum Sparte](/bo4e/202604/enum/Sparte)<br/><Werte>`STROM`, `GAS`, `FERNWAERME`, `NAHWAERME`, `WASSER`, `ABWASSER`</Werte> | Die Sparte in der der Auftrag relevant ist |
| <a id="lieferanschrift"></a>`lieferanschrift` | [Adresse](/bo4e/202604/com/Adresse) | Die Adresse, die sich in Belieferung befindet. |
| <a id="marktlokationsid"></a>`marktlokationsId` | string | Die ID der Marktlokation der der zu sperrende Zähler zugeordnet ist. |
| <a id="mindestpreis"></a>`mindestpreis` | [Preis](/bo4e/202604/com/Preis) | Der Mindestpreis eines Auftrags (z.B. für eine Sperrung) |
| <a id="hoechstpreis"></a>`hoechstpreis` | [Preis](/bo4e/202604/com/Preis) | Der Höchstpreis eines Auftrags (z.B. für eine Sperrung) |
| <a id="energierichtung"></a>`energierichtung` | [Enum Energierichtung](/bo4e/202604/enum/Energierichtung)<br/><Werte>`AUSSP`, `EINSP`</Werte> | Spezifiziert die Energierichtung einer Markt- und/oder Messlokation |
| <a id="berechnungspreis"></a>`berechnungspreis` | number (float) | berechnungspreis |
| <a id="summegesamt"></a>`summeGesamt` | number (float) | summeGesamt |
| <a id="verschobenerabmeldetermin"></a>`verschobenerAbmeldetermin` | string (date-time) | verschobenerAbmeldetermin |
| <a id="behebungszeitpunkt"></a>`behebungsZeitpunkt` | string (date-time) | behebungsZeitpunkt |
| <a id="lieferadressealtgeraete"></a>`lieferadresseAltgeraete` | [Geschaeftspartner](/bo4e/202604/bo/Geschaeftspartner) | — |
| <a id="definitionstyp"></a>`definitionsTyp` | [Enum DefinitionsTyp](/bo4e/202604/enum/DefinitionsTyp)<br/><Werte>`ZAEHLZEIT`, `SCHALTZEIT`, `LEISTUNGSKURVEN`</Werte> | DefinitionsTyp |
| <a id="positionsdaten"></a>`positionsdaten` | [AuftragPosition[]](/bo4e/202604/com/AuftragPosition) | positionsdaten |
| <a id="bemerkungen"></a>`bemerkungen` | string[] | bemerkungen |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[boTyp](/bo4e/202604/bo/Auftrag#botyp) <span className="hbs-pflicht">\*</span></span> | Typ des BO | [Enum BOTyp](/bo4e/202604/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> |
| <span className="hbs-f hbs-e0">[versionStruktur](/bo4e/202604/bo/Auftrag#versionstruktur) <span className="hbs-pflicht">\*</span></span> | versionStruktur | string |
| <span className="hbs-f hbs-e0">[ausfuehrungsdatum](/bo4e/202604/bo/Auftrag#ausfuehrungsdatum)</span> | Das Ausführungsdatum beschreibt zu welchem Zeitpunkt ein Auftrag ausgeführt werden soll. | string (date-time) |
| <span className="hbs-f hbs-e0">[fertigstellungsdatum](/bo4e/202604/bo/Auftrag#fertigstellungsdatum)</span> | Das Fertigstellungsdatum beschreibt zu welchem Zeitpunkt ein Auftrag ausgeführt wurde/wird. | string (date-time) |
| <span className="hbs-f hbs-e0">[startdatum](/bo4e/202604/bo/Auftrag#startdatum)</span> | Das Startdatum beschreibt zu welchem Zeitpunkt ein Auftrag gestartet wurde/wird. | string (date-time) |
| <span className="hbs-f hbs-e0">[enddatum](/bo4e/202604/bo/Auftrag#enddatum)</span> | Das Enddatum beschreibt zu welchem Zeitpunkt ein Auftrag endete oder enden wird. | string (date-time) |
| <span className="hbs-f hbs-e0">[sparte](/bo4e/202604/bo/Auftrag#sparte)</span> | Die Sparte in der der Auftrag relevant ist | [Enum Sparte](/bo4e/202604/enum/Sparte)<br/><Werte>`STROM`, `GAS`, `FERNWAERME`, `NAHWAERME`, `WASSER`, `ABWASSER`</Werte> |
| <span className="hbs-g hbs-e0">[lieferanschrift](/bo4e/202604/bo/Auftrag#lieferanschrift)</span> | Die Adresse, die sich in Belieferung befindet. | [Adresse](/bo4e/202604/com/Adresse) |
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
| <span className="hbs-f hbs-e0">[marktlokationsId](/bo4e/202604/bo/Auftrag#marktlokationsid)</span> | Die ID der Marktlokation der der zu sperrende Zähler zugeordnet ist. | string |
| <span className="hbs-g hbs-e0">[mindestpreis](/bo4e/202604/bo/Auftrag#mindestpreis)</span> | Der Mindestpreis eines Auftrags (z.B. für eine Sperrung) | [Preis](/bo4e/202604/com/Preis) |
| <span className="hbs-f hbs-e1">[wert](/bo4e/202604/com/Preis#wert)</span> | wert | number (float) |
| <span className="hbs-f hbs-e1">[menge](/bo4e/202604/com/Preis#menge)</span> | menge | integer |
| <span className="hbs-f hbs-e1">[minimaleMenge](/bo4e/202604/com/Preis#minimalemenge)</span> | minimale Menge | integer |
| <span className="hbs-f hbs-e1">[maximaleMenge](/bo4e/202604/com/Preis#maximalemenge)</span> | maximale Menge | integer |
| <span className="hbs-f hbs-e1">[einheit](/bo4e/202604/com/Preis#einheit)</span> | Waehrungseinheit | [Enum Waehrungseinheit](/bo4e/202604/enum/Waehrungseinheit)<br/><Werte>`EUR`, `CT`</Werte> |
| <span className="hbs-f hbs-e1">[bezugswert](/bo4e/202604/com/Preis#bezugswert)</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202604/enum/Mengeneinheit)<br/><Werte>`W`, `WH`, `KW`, `KWH`, `KVARH`, `MW`, `MWH`, `STUECK`, `KUBIKMETER`, `STUNDE`, `TAG`, `MONAT`, `JAHR`, `PROZENT`, `ANZAHL`, `VAR`, `KVAR`, `VARH`, `KWHK`, `Z16`, `KWT`, `WATT_PRO_QUADRATMETER`, `METER_PRO_SEKUNDE`</Werte> |
| <span className="hbs-f hbs-e1">[status](/bo4e/202604/com/Preis#status)</span> | Preisstatus | [Enum Preisstatus](/bo4e/202604/enum/Preisstatus)<br/><Werte>`VORLAEUFIG`, `ENDGUELTIG`</Werte> |
| <span className="hbs-f hbs-e1">[preisart](/bo4e/202604/com/Preis#preisart)</span> | Preisart Code | [Enum Preisart](/bo4e/202604/enum/Preisart)<br/><Werte>`EINRICHTUNGSPREIS`, `TRANSAKTIONSPREIS`, `BETRIEBSPREIS`</Werte> |
| <span className="hbs-g hbs-e0">[hoechstpreis](/bo4e/202604/bo/Auftrag#hoechstpreis)</span> | Der Höchstpreis eines Auftrags (z.B. für eine Sperrung) | [Preis](/bo4e/202604/com/Preis) |
| <span className="hbs-f hbs-e1">[wert](/bo4e/202604/com/Preis#wert)</span> | wert | number (float) |
| <span className="hbs-f hbs-e1">[menge](/bo4e/202604/com/Preis#menge)</span> | menge | integer |
| <span className="hbs-f hbs-e1">[minimaleMenge](/bo4e/202604/com/Preis#minimalemenge)</span> | minimale Menge | integer |
| <span className="hbs-f hbs-e1">[maximaleMenge](/bo4e/202604/com/Preis#maximalemenge)</span> | maximale Menge | integer |
| <span className="hbs-f hbs-e1">[einheit](/bo4e/202604/com/Preis#einheit)</span> | Waehrungseinheit | [Enum Waehrungseinheit](/bo4e/202604/enum/Waehrungseinheit)<br/><Werte>`EUR`, `CT`</Werte> |
| <span className="hbs-f hbs-e1">[bezugswert](/bo4e/202604/com/Preis#bezugswert)</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202604/enum/Mengeneinheit)<br/><Werte>`W`, `WH`, `KW`, `KWH`, `KVARH`, `MW`, `MWH`, `STUECK`, `KUBIKMETER`, `STUNDE`, `TAG`, `MONAT`, `JAHR`, `PROZENT`, `ANZAHL`, `VAR`, `KVAR`, `VARH`, `KWHK`, `Z16`, `KWT`, `WATT_PRO_QUADRATMETER`, `METER_PRO_SEKUNDE`</Werte> |
| <span className="hbs-f hbs-e1">[status](/bo4e/202604/com/Preis#status)</span> | Preisstatus | [Enum Preisstatus](/bo4e/202604/enum/Preisstatus)<br/><Werte>`VORLAEUFIG`, `ENDGUELTIG`</Werte> |
| <span className="hbs-f hbs-e1">[preisart](/bo4e/202604/com/Preis#preisart)</span> | Preisart Code | [Enum Preisart](/bo4e/202604/enum/Preisart)<br/><Werte>`EINRICHTUNGSPREIS`, `TRANSAKTIONSPREIS`, `BETRIEBSPREIS`</Werte> |
| <span className="hbs-f hbs-e0">[energierichtung](/bo4e/202604/bo/Auftrag#energierichtung)</span> | Spezifiziert die Energierichtung einer Markt- und/oder Messlokation | [Enum Energierichtung](/bo4e/202604/enum/Energierichtung)<br/><Werte>`AUSSP`, `EINSP`</Werte> |
| <span className="hbs-f hbs-e0">[berechnungspreis](/bo4e/202604/bo/Auftrag#berechnungspreis)</span> | berechnungspreis | number (float) |
| <span className="hbs-f hbs-e0">[summeGesamt](/bo4e/202604/bo/Auftrag#summegesamt)</span> | summeGesamt | number (float) |
| <span className="hbs-f hbs-e0">[verschobenerAbmeldetermin](/bo4e/202604/bo/Auftrag#verschobenerabmeldetermin)</span> | verschobenerAbmeldetermin | string (date-time) |
| <span className="hbs-f hbs-e0">[behebungsZeitpunkt](/bo4e/202604/bo/Auftrag#behebungszeitpunkt)</span> | behebungsZeitpunkt | string (date-time) |
| <span className="hbs-g hbs-e0">[lieferadresseAltgeraete](/bo4e/202604/bo/Auftrag#lieferadressealtgeraete)</span> | — | [Geschaeftspartner](/bo4e/202604/bo/Geschaeftspartner) |
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
| <span className="hbs-f hbs-e0">[definitionsTyp](/bo4e/202604/bo/Auftrag#definitionstyp)</span> | DefinitionsTyp | [Enum DefinitionsTyp](/bo4e/202604/enum/DefinitionsTyp)<br/><Werte>`ZAEHLZEIT`, `SCHALTZEIT`, `LEISTUNGSKURVEN`</Werte> |
| <span className="hbs-g hbs-e0">[positionsdaten](/bo4e/202604/bo/Auftrag#positionsdaten) <span className="hbs-liste">[ ]</span></span> | positionsdaten | [AuftragPosition[]](/bo4e/202604/com/AuftragPosition) |
| <span className="hbs-f hbs-e1">[positionsnummer](/bo4e/202604/com/AuftragPosition#positionsnummer)</span> | Positionsnummer | integer |
| <span className="hbs-f hbs-e1">[positionsnummerAngebot](/bo4e/202604/com/AuftragPosition#positionsnummerangebot)</span> | laufende Positionsnummer des Angebot | string |
| <span className="hbs-f hbs-e1">[energieerfassung](/bo4e/202604/com/AuftragPosition#energieerfassung)</span> | Energieerfassung | [Enum Energieerfassung](/bo4e/202604/enum/Energieerfassung)<br/><Werte>`SEPARAT_ERFASSEN`, `NICHT_SEPARAT_ERFASSEN`</Werte> |
| <span className="hbs-f hbs-e1">[artikelnummer](/bo4e/202604/com/AuftragPosition#artikelnummer)</span> | BDEW Artikelnummer | [Enum BDEWArtikelnummer](/bo4e/202604/enum/BDEWArtikelnummer)<br/><Werte>`LEISTUNG`, `LEISTUNG_PAUSCHAL`, `GRUNDPREIS`, `REGELENERGIE_ARBEIT`, `REGELENERGIE_LEISTUNG`, `NOTSTROMLIEFERUNG_ARBEIT`, `NOTSTROMLIEFERUNG_LEISTUNG`, `RESERVENETZKAPAZITAET`, `RESERVELEISTUNG`, `ZUSAETZLICHE_ABLESUNG`, `PRUEFGEBUEHREN_AUSSERPLANMAESSIG`, `WIRKARBEIT`, `SINGULAER_GENUTZTE_BETRIEBSMITTEL`, `ABGABE_KWKG`, `ABSCHLAG`, `KONZESSIONSABGABE`, `ENTGELT_FERNAUSLESUNG`, `UNTERMESSUNG`, `BLINDMEHRARBEIT`, `ENTGELT_ABRECHNUNG`, `SPERRKOSTEN`, `ENTSPERRKOSTEN`, `MAHNKOSTEN`, `MEHR_MINDERMENGEN`, `INKASSOKOSTEN`, `BLINDMEHRLEISTUNG`, `ENTGELT_MESSUNG_ABLESUNG`, `ENTGELT_EINBAU_BETRIEB_WARTUNG_MESSTECHNIK`, `AUSGLEICHSENERGIE`, `AUSGLEICHSENERGIE_UNTERDECKUNG`, `ZAEHLEINRICHTUNG`, `WANDLER_MENGENUMWERTER`, `KOMMUNIKATIONSEINRICHTUNG`, `TECHNISCHE_STEUEREINRICHTUNG`, `PARAGRAF_19_STROM_NEV_UMLAGE`, `BEFESTIGUNGSEINRICHTUNG`, `OFFSHORE_HAFTUNGSUMLAGE`, `FIXE_ARBEITSENTGELTKOMPONENTE`, `FIXE_LEISTUNGSENTGELTKOMPONENTE`, `UMLAGE_ABSCHALTBARE_LASTEN`, `MEHRMENGE`, `MINDERMENGE`, `ENERGIESTEUER`, `SMARTMETER_GATEWAY`, `STEUERBOX`, `MSB_INKL_MESSUNG`, `ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_2_1_MSBG`, `ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_2_2_MSBG`, `ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_2_3_MSBG`, `ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_2_4_MSBG`, `ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_2_5_MSBG`, `ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_3_MSBG`, `ENTGELT_KAPAZITAETEN`</Werte> |
| <span className="hbs-f hbs-e1">[positionsbetrag](/bo4e/202604/com/AuftragPosition#positionsbetrag)</span> | Betrag der Position | string |
| <span className="hbs-f hbs-e1">[gueltigAb](/bo4e/202604/com/AuftragPosition#gueltigab)</span> | gueltigAb | string (date-time) |
| <span className="hbs-f hbs-e1">[startdatum](/bo4e/202604/com/AuftragPosition#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e1">[enddatum](/bo4e/202604/com/AuftragPosition#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-f hbs-e1">[istBestand](/bo4e/202604/com/AuftragPosition#istbestand)</span> | istBestand | string |
| <span className="hbs-f hbs-e1">[obiskennzahl](/bo4e/202604/com/AuftragPosition#obiskennzahl)</span> | Obis-Kennzahl | string |
| <span className="hbs-f hbs-e1">[anfragegrund](/bo4e/202604/com/AuftragPosition#anfragegrund)</span> | Anfragegrund | [Enum Anfragegrund](/bo4e/202604/enum/Anfragegrund)<br/><Werte>`ABGRENZUNG_VON_ENERGIEMENGEN`, `ABGRENZUNG`, `WECHSELEREIGNIS`, `ZWISCHENABLESUNG`, `DIREKTER_VERTRAG_MSB_AN`, `DIREKTER_VERTRAG_MSB_ANN`, `AENDERUNG_IM_LOKATIONSBUENDEL`, `NEUKONFIGURATION`, `KONFIGURATION_UNVERAENDERT`</Werte> |
| <span className="hbs-g hbs-e1">[allgemeineInformationen](/bo4e/202604/com/AuftragPosition#allgemeineinformationen)</span> | — | [AllgemeineInformationen](/bo4e/202604/com/AllgemeineInformationen) |
| <span className="hbs-f hbs-e2">[info1](/bo4e/202604/com/AllgemeineInformationen#info1)</span> | Allgemeine Info 1 | string |
| <span className="hbs-f hbs-e2">[info2](/bo4e/202604/com/AllgemeineInformationen#info2)</span> | Allgemeine Info 2 | string |
| <span className="hbs-f hbs-e2">[info3](/bo4e/202604/com/AllgemeineInformationen#info3)</span> | Allgemeine Info 3 | string |
| <span className="hbs-f hbs-e2">[info4](/bo4e/202604/com/AllgemeineInformationen#info4)</span> | Allgemeine Info 4 | string |
| <span className="hbs-f hbs-e2">[info5](/bo4e/202604/com/AllgemeineInformationen#info5)</span> | Allgemeine Info 5 | string |
| <span className="hbs-g hbs-e1">[infoAbweichung](/bo4e/202604/com/AuftragPosition#infoabweichung)</span> | — | [InfoAbweichung](/bo4e/202604/com/InfoAbweichung) |
| <span className="hbs-f hbs-e2">[abweichung1](/bo4e/202604/com/InfoAbweichung#abweichung1)</span> | Abweichung Zeile 1 | string |
| <span className="hbs-f hbs-e2">[abweichung2](/bo4e/202604/com/InfoAbweichung#abweichung2)</span> | Abweichung Zeile 2 | string |
| <span className="hbs-f hbs-e2">[abweichung3](/bo4e/202604/com/InfoAbweichung#abweichung3)</span> | Abweichung Zeile 3 | string |
| <span className="hbs-f hbs-e2">[abweichung4](/bo4e/202604/com/InfoAbweichung#abweichung4)</span> | Abweichung Zeile 4 | string |
| <span className="hbs-f hbs-e2">[abweichung5](/bo4e/202604/com/InfoAbweichung#abweichung5)</span> | Abweichung Zeile 5 | string |
| <span className="hbs-f hbs-e1">[definitionsTyp](/bo4e/202604/com/AuftragPosition#definitionstyp)</span> | DefinitionsTyp | [Enum DefinitionsTyp](/bo4e/202604/enum/DefinitionsTyp)<br/><Werte>`ZAEHLZEIT`, `SCHALTZEIT`, `LEISTUNGSKURVEN`</Werte> |
| <span className="hbs-f hbs-e1">[lokationsId](/bo4e/202604/com/AuftragPosition#lokationsid)</span> | lokationsId | string |
| <span className="hbs-f hbs-e1">[zaehlwerk](/bo4e/202604/com/AuftragPosition#zaehlwerk)</span> | Zaehlwerk | integer |
| <span className="hbs-g hbs-e1">[endpunktAdresse](/bo4e/202604/com/AuftragPosition#endpunktadresse)</span> | — | [EndpunktAdresse](/bo4e/202604/com/EndpunktAdresse) |
| <span className="hbs-f hbs-e2">[gwaManagement](/bo4e/202604/com/EndpunktAdresse#gwamanagement)</span> | Endpunktadresse GWA Management | string |
| <span className="hbs-f hbs-e2">[gwaAdminService](/bo4e/202604/com/EndpunktAdresse#gwaadminservice)</span> | Endpunktadresse GWA Admin-Service | string |
| <span className="hbs-f hbs-e2">[gwaNTP](/bo4e/202604/com/EndpunktAdresse#gwantp)</span> | Endpunktadresse GWA NTP (Zeitserver) | string |
| <span className="hbs-g hbs-e1">[zertifikatsInformationen](/bo4e/202604/com/AuftragPosition#zertifikatsinformationen)</span> | — | [Zertifikatsinformationen](/bo4e/202604/com/Zertifikatsinformationen) |
| <span className="hbs-f hbs-e2">[uriSubCA](/bo4e/202604/com/Zertifikatsinformationen#urisubca)</span> | URI der Sub-CA | string |
| <span className="hbs-f hbs-e2">[commonNameZertifikat](/bo4e/202604/com/Zertifikatsinformationen#commonnamezertifikat)</span> | Common Name (CN) des Zertifikats | string |
| <span className="hbs-f hbs-e2">[seriennummerZertifikat](/bo4e/202604/com/Zertifikatsinformationen#seriennummerzertifikat)</span> | Seriennummer des Zertifikats | string |
| <span className="hbs-f hbs-e1">[wakeUpPort](/bo4e/202604/com/AuftragPosition#wakeupport)</span> | Wake-Up-Port der Kommunikationseinheit | string |
| <span className="hbs-f hbs-e1">[apnKommunikationsdaten](/bo4e/202604/com/AuftragPosition#apnkommunikationsdaten)</span> | APN der Kommunikationsdaten | string |
| <span className="hbs-g hbs-e1">[apnKommunikationsdatenZugriffsparameter](/bo4e/202604/com/AuftragPosition#apnkommunikationsdatenzugriffsparameter)</span> | — | [ApnKommunikationsdatenZugriffsparameter](/bo4e/202604/com/ApnKommunikationsdatenZugriffsparameter) |
| <span className="hbs-f hbs-e2">[apnName](/bo4e/202604/com/ApnKommunikationsdatenZugriffsparameter#apnname)</span> | Name des APNs | string |
| <span className="hbs-f hbs-e2">[nutzer](/bo4e/202604/com/ApnKommunikationsdatenZugriffsparameter#nutzer)</span> | Nutzer | string |
| <span className="hbs-f hbs-e2">[passwort](/bo4e/202604/com/ApnKommunikationsdatenZugriffsparameter#passwort)</span> | Passwort | string |
| <span className="hbs-f hbs-e0">[bemerkungen](/bo4e/202604/bo/Auftrag#bemerkungen) <span className="hbs-liste">[ ]</span></span> | bemerkungen | string[] |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### ausfuehrungsdatum

22 Verwendung(en) in den Nachrichtentypen ORDERS, ORDRSP.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_17001](/schnittstellen/202604/pruefi/ORDERS/PI_17001) | Prüfi | ORDERS | stammdaten › AUFTRAG |
| [PI_17003](/schnittstellen/202604/pruefi/ORDERS/PI_17003) | Prüfi | ORDERS | stammdaten › AUFTRAG |
| [PI_17005](/schnittstellen/202604/pruefi/ORDERS/PI_17005) | Prüfi | ORDERS | stammdaten › AUFTRAG |
| [PI_17006](/schnittstellen/202604/pruefi/ORDERS/PI_17006) | Prüfi | ORDERS | stammdaten › AUFTRAG |
| [PI_17009](/schnittstellen/202604/pruefi/ORDERS/PI_17009) | Prüfi | ORDERS | stammdaten › AUFTRAG |
| [PI_17115](/schnittstellen/202604/pruefi/ORDERS/PI_17115) | Prüfi | ORDERS | stammdaten › AUFTRAG |
| [PI_17116](/schnittstellen/202604/pruefi/ORDERS/PI_17116) | Prüfi | ORDERS | stammdaten › AUFTRAG |
| [PI_17118](/schnittstellen/202604/pruefi/ORDERS/PI_17118) | Prüfi | ORDERS | stammdaten › AUFTRAG |
| [PI_17120](/schnittstellen/202604/pruefi/ORDERS/PI_17120) | Prüfi | ORDERS | stammdaten › AUFTRAG |
| [PI_17121](/schnittstellen/202604/pruefi/ORDERS/PI_17121) | Prüfi | ORDERS | stammdaten › AUFTRAG |
| [PI_17123](/schnittstellen/202604/pruefi/ORDERS/PI_17123) | Prüfi | ORDERS | stammdaten › AUFTRAG |
| [PI_17129](/schnittstellen/202604/pruefi/ORDERS/PI_17129) | Prüfi | ORDERS | stammdaten › AUFTRAG |
| [PI_17130](/schnittstellen/202604/pruefi/ORDERS/PI_17130) | Prüfi | ORDERS | stammdaten › AUFTRAG |
| [PI_17133](/schnittstellen/202604/pruefi/ORDERS/PI_17133) | Prüfi | ORDERS | stammdaten › AUFTRAG |
| [PI_17134](/schnittstellen/202604/pruefi/ORDERS/PI_17134) | Prüfi | ORDERS | stammdaten › AUFTRAG |
| [PI_17135](/schnittstellen/202604/pruefi/ORDERS/PI_17135) | Prüfi | ORDERS | stammdaten › AUFTRAG |
| [PI_19001](/schnittstellen/202604/pruefi/ORDRSP/PI_19001) | Prüfi | ORDRSP | stammdaten › AUFTRAG |
| [PI_19002](/schnittstellen/202604/pruefi/ORDRSP/PI_19002) | Prüfi | ORDRSP | stammdaten › AUFTRAG |
| [PI_19005](/schnittstellen/202604/pruefi/ORDRSP/PI_19005) | Prüfi | ORDRSP | stammdaten › AUFTRAG |
| [PI_19006](/schnittstellen/202604/pruefi/ORDRSP/PI_19006) | Prüfi | ORDRSP | stammdaten › AUFTRAG |
| [PI_19009](/schnittstellen/202604/pruefi/ORDRSP/PI_19009) | Prüfi | ORDRSP | stammdaten › AUFTRAG |
| [PI_19010](/schnittstellen/202604/pruefi/ORDRSP/PI_19010) | Prüfi | ORDRSP | stammdaten › AUFTRAG |

### startdatum

3 Verwendung(en) in den Nachrichtentypen ORDERS, ORDRSP.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_17115](/schnittstellen/202604/pruefi/ORDERS/PI_17115) | Prüfi | ORDERS | stammdaten › AUFTRAG |
| [PI_17133](/schnittstellen/202604/pruefi/ORDERS/PI_17133) | Prüfi | ORDERS | stammdaten › AUFTRAG |
| [PI_19006](/schnittstellen/202604/pruefi/ORDRSP/PI_19006) | Prüfi | ORDRSP | stammdaten › AUFTRAG |

### enddatum

1 Verwendung(en) in den Nachrichtentypen ORDRSP.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_19006](/schnittstellen/202604/pruefi/ORDRSP/PI_19006) | Prüfi | ORDRSP | stammdaten › AUFTRAG |

### verschobenerAbmeldetermin

3 Verwendung(en) in den Nachrichtentypen ORDERS, ORDRSP.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_17002](/schnittstellen/202604/pruefi/ORDERS/PI_17002) | Prüfi | ORDERS | stammdaten › AUFTRAG |
| [PI_19003](/schnittstellen/202604/pruefi/ORDRSP/PI_19003) | Prüfi | ORDRSP | stammdaten › AUFTRAG |
| [PI_19004](/schnittstellen/202604/pruefi/ORDRSP/PI_19004) | Prüfi | ORDRSP | stammdaten › AUFTRAG |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
