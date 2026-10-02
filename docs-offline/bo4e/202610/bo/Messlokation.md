# Messlokation
<span hidden data-pagefind-meta={"title:Messlokation — BO4E-Geschäftsobjekt (FV 202610)"} />

BO4E-Geschäftsobjekt · 27 Felder · 158 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="botyp"></a>`boTyp` <span className="hbs-pflicht">\*</span> | [Enum BOTyp](/bo4e/202610/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> | Typ des BO |
| <a id="versionstruktur"></a>`versionStruktur` <span className="hbs-pflicht">\*</span> | string | versionStruktur |
| <a id="messlokationsid"></a>`messlokationsId` | string | Die Messlokations-Identifikation. Das ist die frühere Zählpunktbezeichnung, z.B. DE 47108151234567 |
| <a id="sparte"></a>`sparte` | [Enum Sparte](/bo4e/202610/enum/Sparte)<br/><Werte>`STROM`, `GAS`, `FERNWAERME`, `NAHWAERME`, `WASSER`, `ABWASSER`</Werte> | Strom oder Gas. |
| <a id="energierichtung"></a>`energierichtung` | [Enum Energierichtung](/bo4e/202610/enum/Energierichtung)<br/><Werte>`AUSSP`, `EINSP`</Werte> | Spezifiziert die Energierichtung einer Markt- und/oder Messlokation |
| <a id="netzebenemessung"></a>`netzebenemessung` | [Enum Netzebene](/bo4e/202610/enum/Netzebene)<br/><Werte>`NSP`, `MSP`, `HSP`, `HSS`, `MSP_NSP_UMSP`, `HSP_MSP_UMSP`, `HSS_HSP_UMSP`, `HD`, `MD`, `ND`</Werte> | Netzebene |
| <a id="messgebietnr"></a>`messgebietNr` | string | Die Nummer des Messgebietes in der ene't-Datenbank. |
| <a id="grundzustaendigermsbcodenr"></a>`grundzustaendigerMSBCodeNr` | string | Codenummer des grundzuständigen Messstellenbetreibers, der für diese Messlokation zuständig ist.( Dieser ist immer dann Messstellenbetreiber, wenn kein anderer MSB die Einrichtungen an der Messlokation betreibt.) |
| <a id="messadresse"></a>`messadresse` | [Adresse](/bo4e/202610/com/Adresse) | Die Adresse, an der die Messeinrichtungen zu finden sind.( Nur angeben, wenn diese von der Adresse der Marktlokation abweicht.) Achtung: Es darf immer nur eine Art der Ortsangabe vorhanden sein (entweder eine Adresse oder eine GeoKoordinate oder eine Katasteradresse. |
| <a id="bilanzierungsmethode"></a>`bilanzierungsmethode` | [Enum Bilanzierungsmethode](/bo4e/202610/enum/Bilanzierungsmethode)<br/><Werte>`RLM`, `SLP`, `TLP_GEMEINSAM`, `TLP_GETRENNT`, `PAUSCHAL`, `IMS`</Werte> | Bilanzierungsmethode |
| <a id="abrechnungmessstellenbetriebnna"></a>`abrechnungmessstellenbetriebnna` | boolean | Dieser Wert ist true, falls die Abrechnungs des Messstellenbetriebs die Netznutzungsabrechnung enthält. false andernfalls |
| <a id="gasqualitaet"></a>`gasqualitaet` | [Enum Gasqualitaet](/bo4e/202610/enum/Gasqualitaet)<br/><Werte>`H_GAS`, `L_GAS`</Werte> | gasqualitaet für EDIFACT mapping |
| <a id="verlustfaktor"></a>`verlustfaktor` | number (float) | verlustfaktor für EDIFACT mapping |
| <a id="betriebszustand"></a>`betriebszustand` | [Enum Betriebszustand](/bo4e/202610/enum/Betriebszustand)<br/><Werte>`GESPERRT_NICHT_ENTSPERREN`, `GESPERRT`, `REGELBETRIEB`, `AUSSERHALB_REGELBETRIEB`</Werte> | Betriebszustand |
| <a id="ablesekartenempfaenger"></a>`ablesekartenempfaenger` | [Geschaeftspartner](/bo4e/202610/bo/Geschaeftspartner) | — |
| <a id="referenzmarktlokationsid"></a>`referenzMarktlokationsId` | string | referenzMarktlokationsId |
| <a id="verwendungsumfang"></a>`verwendungsumfang` | [Enum Verwendungsumfang](/bo4e/202610/enum/Verwendungsumfang)<br/><Werte>`MESSLOKATION_PROZESSUAL_BEHANDELT`, `MESSLOKATION_LOKATIONSBUENDEL`</Werte> | Verwendungsumfang |
| <a id="zukuenftigermeldepunkt"></a>`zukuenftigerMeldepunkt` | boolean | zukuenftigerMeldepunkt |
| <a id="lokationszuordnung"></a>`lokationszuordnung` | [Enum Lokationszuordnung](/bo4e/202610/enum/Lokationszuordnung)<br/><Werte>`UNVERAENDERT`, `BEGINNT`, `ENDET`</Werte> | Lokationszuordnung |
| <a id="beteiligtermarktpartner"></a>`beteiligterMarktpartner` | [Marktteilnehmer](/bo4e/202610/bo/Marktteilnehmer) | — |
| <a id="geraete"></a>`geraete` | [Geraet[]](/bo4e/202610/com/Geraet) | Liste der Geräte, die zu diesem Zähler gehören. |
| <a id="messdienstleistung"></a>`messdienstleistung` | [Dienstleistung[]](/bo4e/202610/com/Dienstleistung) | Liste der Messdienstleistungen, die zu dieser Messstelle gehört. |
| <a id="messlokationszaehler"></a>`messlokationszaehler` | string[] | Zähler, die zu dieser Messlokation gehören. Details |
| <a id="zaehlwerke"></a>`zaehlwerke` | [Zaehlwerk[]](/bo4e/202610/com/Zaehlwerk) | Die Zählwerke des Zählers. |
| <a id="marktrollen"></a>`marktrollen` | [Marktteilnehmer[]](/bo4e/202610/bo/Marktteilnehmer) | marktrollen für EDIFACT mapping |
| <a id="datenqualitaet"></a>`datenqualitaet` | [Enum Datenqualitaet](/bo4e/202610/enum/Datenqualitaet)<br/><Werte>`ERWARTETE_DATEN`, `IM_SYSTEM_VORHANDENE_DATEN`, `INFORMATIVE_DATEN`, `GUELTIGE_DATEN`, `KEINE_DATEN`, `IM_SYSTEM_KEINE_DATEN_VORHANDEN`, `KEINE_DATEN_ERWARTET`, `DIFFERENZ_DATEN`, `DIFFERENZ_ERWARTETE_DATEN`, `DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</Werte> | Datenqualitaet |
| <a id="gueltigkeitszeitraum"></a>`gueltigkeitszeitraum` | [Zeitraum](/bo4e/202610/com/Zeitraum) | — |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[boTyp](/bo4e/202610/bo/Messlokation#botyp) <span className="hbs-pflicht">\*</span></span> | Typ des BO | [Enum BOTyp](/bo4e/202610/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> |
| <span className="hbs-f hbs-e0">[versionStruktur](/bo4e/202610/bo/Messlokation#versionstruktur) <span className="hbs-pflicht">\*</span></span> | versionStruktur | string |
| <span className="hbs-f hbs-e0">[messlokationsId](/bo4e/202610/bo/Messlokation#messlokationsid)</span> | Die Messlokations-Identifikation. Das ist die frühere Zählpunktbezeichnung,<br/>z.B. DE 47108151234567 | string |
| <span className="hbs-f hbs-e0">[sparte](/bo4e/202610/bo/Messlokation#sparte)</span> | Strom oder Gas. | [Enum Sparte](/bo4e/202610/enum/Sparte)<br/><Werte>`STROM`, `GAS`, `FERNWAERME`, `NAHWAERME`, `WASSER`, `ABWASSER`</Werte> |
| <span className="hbs-f hbs-e0">[energierichtung](/bo4e/202610/bo/Messlokation#energierichtung)</span> | Spezifiziert die Energierichtung einer Markt- und/oder Messlokation | [Enum Energierichtung](/bo4e/202610/enum/Energierichtung)<br/><Werte>`AUSSP`, `EINSP`</Werte> |
| <span className="hbs-f hbs-e0">[netzebenemessung](/bo4e/202610/bo/Messlokation#netzebenemessung)</span> | Netzebene | [Enum Netzebene](/bo4e/202610/enum/Netzebene)<br/><Werte>`NSP`, `MSP`, `HSP`, `HSS`, `MSP_NSP_UMSP`, `HSP_MSP_UMSP`, `HSS_HSP_UMSP`, `HD`, `MD`, `ND`</Werte> |
| <span className="hbs-f hbs-e0">[messgebietNr](/bo4e/202610/bo/Messlokation#messgebietnr)</span> | Die Nummer des Messgebietes in der ene't-Datenbank. | string |
| <span className="hbs-f hbs-e0">[grundzustaendigerMSBCodeNr](/bo4e/202610/bo/Messlokation#grundzustaendigermsbcodenr)</span> | Codenummer des grundzuständigen Messstellenbetreibers, der für diese<br/>Messlokation zuständig ist.( Dieser ist immer dann Messstellenbetreiber, wenn<br/>kein anderer MSB die Einrichtungen an der Messlokation betreibt.) | string |
| <span className="hbs-g hbs-e0">[messadresse](/bo4e/202610/bo/Messlokation#messadresse)</span> | Die Adresse, an der die Messeinrichtungen zu finden sind.( Nur angeben, wenn<br/>diese von der Adresse der Marktlokation abweicht.)<br/>Achtung: Es darf immer nur eine Art der Ortsangabe vorhanden sein (entweder<br/>eine Adresse oder eine GeoKoordinate oder eine Katasteradresse. | [Adresse](/bo4e/202610/com/Adresse) |
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
| <span className="hbs-f hbs-e0">[bilanzierungsmethode](/bo4e/202610/bo/Messlokation#bilanzierungsmethode)</span> | Bilanzierungsmethode | [Enum Bilanzierungsmethode](/bo4e/202610/enum/Bilanzierungsmethode)<br/><Werte>`RLM`, `SLP`, `TLP_GEMEINSAM`, `TLP_GETRENNT`, `PAUSCHAL`, `IMS`</Werte> |
| <span className="hbs-f hbs-e0">[abrechnungmessstellenbetriebnna](/bo4e/202610/bo/Messlokation#abrechnungmessstellenbetriebnna)</span> | Dieser Wert ist true, falls die Abrechnungs des Messstellenbetriebs die Netznutzungsabrechnung enthält. false<br/>andernfalls | boolean |
| <span className="hbs-f hbs-e0">[gasqualitaet](/bo4e/202610/bo/Messlokation#gasqualitaet)</span> | gasqualitaet für EDIFACT mapping | [Enum Gasqualitaet](/bo4e/202610/enum/Gasqualitaet)<br/><Werte>`H_GAS`, `L_GAS`</Werte> |
| <span className="hbs-f hbs-e0">[verlustfaktor](/bo4e/202610/bo/Messlokation#verlustfaktor)</span> | verlustfaktor für EDIFACT mapping | number (float) |
| <span className="hbs-f hbs-e0">[betriebszustand](/bo4e/202610/bo/Messlokation#betriebszustand)</span> | Betriebszustand | [Enum Betriebszustand](/bo4e/202610/enum/Betriebszustand)<br/><Werte>`GESPERRT_NICHT_ENTSPERREN`, `GESPERRT`, `REGELBETRIEB`, `AUSSERHALB_REGELBETRIEB`</Werte> |
| <span className="hbs-g hbs-e0">[ablesekartenempfaenger](/bo4e/202610/bo/Messlokation#ablesekartenempfaenger)</span> | — | [Geschaeftspartner](/bo4e/202610/bo/Geschaeftspartner) |
| <span className="hbs-f hbs-e1">[boTyp](/bo4e/202610/bo/Geschaeftspartner#botyp) <span className="hbs-pflicht">\*</span></span> | Typ des BO | [Enum BOTyp](/bo4e/202610/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> |
| <span className="hbs-f hbs-e1">[versionStruktur](/bo4e/202610/bo/Geschaeftspartner#versionstruktur) <span className="hbs-pflicht">\*</span></span> | versionStruktur | string |
| <span className="hbs-f hbs-e1">[anrede](/bo4e/202610/bo/Geschaeftspartner#anrede)</span> | Die Anrede für den GePa, Z.B. Herr. | string |
| <span className="hbs-f hbs-e1">[name1](/bo4e/202610/bo/Geschaeftspartner#name1)</span> | Erster Teil des Namens. Hier kann der Firmenname oder bei Privatpersonen<br/>beispielsweise der Nachname dargestellt werden. Beispiele: Yellow Strom GmbH<br/>oder Hagen | string |
| <span className="hbs-f hbs-e1">[name2](/bo4e/202610/bo/Geschaeftspartner#name2)</span> | Zweiter Teil des Namens. Hier kann der eine Erweiterung zum Firmennamen oder<br/>bei Privatpersonen beispielsweise der Vorname dargestellt werden. Beispiele:<br/>Bereich Süd oder Nina | string |
| <span className="hbs-f hbs-e1">[name3](/bo4e/202610/bo/Geschaeftspartner#name3)</span> | Dritter Teil des Namens. Hier können weitere Ergänzungen zum Firmennamen oder<br/>bei Privatpersonen Zusätze zum Namen dargestellt werden. Beispiele: und Afrika<br/>oder Sängerin | string |
| <span className="hbs-f hbs-e1">[name4](/bo4e/202610/bo/Geschaeftspartner#name4)</span> | name4 | string |
| <span className="hbs-f hbs-e1">[umsatzsteuerId](/bo4e/202610/bo/Geschaeftspartner#umsatzsteuerid)</span> | Die Umsatzsteuer-ID des Geschäftspartners. Beispiel: DE 813281825 | string |
| <span className="hbs-f hbs-e1">[glaeubigerId](/bo4e/202610/bo/Geschaeftspartner#glaeubigerid)</span> | * Die Gläubiger-ID welche im Zahlungsverkehr verwendet wird- Z.B. DE 47116789 | string |
| <span className="hbs-f hbs-e1">[emailAdresse](/bo4e/202610/bo/Geschaeftspartner#emailadresse)</span> | emailAdresse | string |
| <span className="hbs-f hbs-e1">[website](/bo4e/202610/bo/Geschaeftspartner#website)</span> | Internetseite des Marktpartners. Beispiel: www.mp-energie.de | string |
| <span className="hbs-f hbs-e1">[gewerbekennzeichnung](/bo4e/202610/bo/Geschaeftspartner#gewerbekennzeichnung)</span> | Kennzeichnung ob es sich um einen Gewerbe/Unternehmen (gewerbeKennzeichnung = true)<br/>oder eine Privatperson handelt. (gewerbeKennzeichnung = false) | boolean |
| <span className="hbs-f hbs-e1">[hrnummer](/bo4e/202610/bo/Geschaeftspartner#hrnummer)</span> | Handelsregisternummer des Geschäftspartners | string |
| <span className="hbs-f hbs-e1">[amtsgericht](/bo4e/202610/bo/Geschaeftspartner#amtsgericht)</span> | Amtsgericht bzw Handelsregistergericht, das die Handelsregisternummer herausgegeben hat | string |
| <span className="hbs-g hbs-e1">[partneradresse](/bo4e/202610/bo/Geschaeftspartner#partneradresse)</span> | Adresse des Geschäftspartners, an der sich der Hauptsitz befindet. Details | [Adresse](/bo4e/202610/com/Adresse) |
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
| <span className="hbs-f hbs-e1">[externeKundenummerLieferant](/bo4e/202610/bo/Geschaeftspartner#externekundenummerlieferant)</span> | externeKundenummerLieferant | string |
| <span className="hbs-g hbs-e1">[externeReferenzen](/bo4e/202610/bo/Geschaeftspartner#externereferenzen) <span className="hbs-liste">[ ]</span></span> | Hier können IDs anderer Systeme hinterlegt werden (z.B. eine SAP-GP-Nummer) (Details siehe<br/>ExterneReferenz) | [ExterneReferenz[]](/bo4e/202610/com/ExterneReferenz) |
| <span className="hbs-f hbs-e2">[exRefName](/bo4e/202610/com/ExterneReferenz#exrefname)</span> | Bezeichnung der externen Referenz (z.B. "hochfrequenz integration services") | string<br/><Werte>`Kundennummer beim Lieferanten`, `Kundennummer beim Altlieferanten`</Werte> |
| <span className="hbs-f hbs-e2">[exRefWert](/bo4e/202610/com/ExterneReferenz#exrefwert)</span> | Wert der externen Referenz (z.B. "123456"; "4711") | string |
| <span className="hbs-f hbs-e1">[geschaeftspartnerrolle](/bo4e/202610/bo/Geschaeftspartner#geschaeftspartnerrolle) <span className="hbs-liste">[ ]</span></span> | Rolle, die der Geschäftspartner hat (z.B. Interessent, Kunde). | [Enum Geschaeftspartnerrolle[]](/bo4e/202610/enum/Geschaeftspartnerrolle)<br/><Werte>`KUNDE`, `LIEFERANT`, `DIENSTLEISTER`, `INTERESSENT`, `MARKTPARTNER`, `EIGENTUEMER`, `HAUSVERWALTER`, `KORRESPONDENZEMPFAENGER`, `ABLESEKARTENEMPFAENGER`</Werte> |
| <span className="hbs-f hbs-e1">[kontaktweg](/bo4e/202610/bo/Geschaeftspartner#kontaktweg) <span className="hbs-liste">[ ]</span></span> | Bevorzugter Kontaktweg des Geschäftspartners. | [Enum Kontaktart[]](/bo4e/202610/enum/Kontaktart)<br/><Werte>`ANSCHREIBEN`, `TELEFONAT`, `FAX`, `E_MAIL`, `SMS`</Werte> |
| <span className="hbs-g hbs-e1">[ansprechpartner](/bo4e/202610/bo/Geschaeftspartner#ansprechpartner)</span> | Ansprechpartner as in EDIFACT CTA+IC' COM+?+3222271020:TE', that includes e.g. the phone number of customer. | [Ansprechpartner](/bo4e/202610/bo/Ansprechpartner) |
| <span className="hbs-f hbs-e2">[boTyp](/bo4e/202610/bo/Ansprechpartner#botyp) <span className="hbs-pflicht">\*</span></span> | Typ des BO | [Enum BOTyp](/bo4e/202610/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> |
| <span className="hbs-f hbs-e2">[versionStruktur](/bo4e/202610/bo/Ansprechpartner#versionstruktur) <span className="hbs-pflicht">\*</span></span> | versionStruktur | string |
| <span className="hbs-f hbs-e2">[nachname](/bo4e/202610/bo/Ansprechpartner#nachname)</span> | Nachname (Familienname) des Ansprechpartners | string |
| <span className="hbs-f hbs-e2">[eMailAdresse](/bo4e/202610/bo/Ansprechpartner#emailadresse)</span> | E-Mail Adresse | string |
| <span className="hbs-g hbs-e2">[rufnummern](/bo4e/202610/bo/Ansprechpartner#rufnummern) <span className="hbs-liste">[ ]</span></span> | Liste der Telefonnummern, unter denen der Ansprechpartner erreichbar ist. | [Rufnummer[]](/bo4e/202610/com/Rufnummer) |
| <span className="hbs-f hbs-e3">[nummerntyp](/bo4e/202610/com/Rufnummer#nummerntyp)</span> | Rufnummernart | [Enum Rufnummernart](/bo4e/202610/enum/Rufnummernart)<br/><Werte>`RUF_ZENTRALE`, `FAX_ZENTRALE`, `SAMMELRUF`, `SAMMELFAX`, `ABTEILUNGRUF`, `ABTEILUNGFAX`, `RUF_DURCHWAHL`, `FAX_DURCHWAHL`, `MOBIL_NUMMER`</Werte> |
| <span className="hbs-f hbs-e3">[rufnummer](/bo4e/202610/com/Rufnummer#rufnummer)</span> | rufnummer | string |
| <span className="hbs-f hbs-e0">[referenzMarktlokationsId](/bo4e/202610/bo/Messlokation#referenzmarktlokationsid)</span> | referenzMarktlokationsId | string |
| <span className="hbs-f hbs-e0">[verwendungsumfang](/bo4e/202610/bo/Messlokation#verwendungsumfang)</span> | Verwendungsumfang | [Enum Verwendungsumfang](/bo4e/202610/enum/Verwendungsumfang)<br/><Werte>`MESSLOKATION_PROZESSUAL_BEHANDELT`, `MESSLOKATION_LOKATIONSBUENDEL`</Werte> |
| <span className="hbs-f hbs-e0">[zukuenftigerMeldepunkt](/bo4e/202610/bo/Messlokation#zukuenftigermeldepunkt)</span> | zukuenftigerMeldepunkt | boolean |
| <span className="hbs-f hbs-e0">[lokationszuordnung](/bo4e/202610/bo/Messlokation#lokationszuordnung)</span> | Lokationszuordnung | [Enum Lokationszuordnung](/bo4e/202610/enum/Lokationszuordnung)<br/><Werte>`UNVERAENDERT`, `BEGINNT`, `ENDET`</Werte> |
| <span className="hbs-g hbs-e0">[beteiligterMarktpartner](/bo4e/202610/bo/Messlokation#beteiligtermarktpartner)</span> | — | [Marktteilnehmer](/bo4e/202610/bo/Marktteilnehmer) |
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
| <span className="hbs-g hbs-e0">[geraete](/bo4e/202610/bo/Messlokation#geraete) <span className="hbs-liste">[ ]</span></span> | Liste der Geräte, die zu diesem Zähler gehören. | [Geraet[]](/bo4e/202610/com/Geraet) |
| <span className="hbs-f hbs-e1">[geraetetyp](/bo4e/202610/com/Geraet#geraetetyp)</span> | Auflistung möglicher abzurechnender Gerätetypen | [Enum Geraetetyp](/bo4e/202610/enum/Geraetetyp)<br/><Werte>`WECHSELSTROMZAEHLER`, `DREHSTROMZAEHLER`, `ZWEIRICHTUNGSZAEHLER`, `RLM_ZAEHLER`, `IMS_ZAEHLER`, `BALGENGASZAEHLER`, `MAXIMUMZAEHLER`, `MULTIPLEXANLAGE`, `PAUSCHALANLAGE`, `VERSTAERKERANLAGE`, `SUMMATIONSGERAET`, `IMPULSGEBER`, `EDL_21_ZAEHLERAUFSATZ`, `VIER_QUADRANTEN_LASTGANGZAEHLER`, `MENGENUMWERTER`, `STROMWANDLER`, `SPANNUNGSWANDLER`, `DATENLOGGER`, `KOMMUNIKATIONSANSCHLUSS`, `MODEM`, `TELEKOMMUNIKATIONSEINRICHTUNG`, `KOMMUNIKATIONSEINRICHTUNG`, `DREHKOLBENGASZAEHLER`, `TURBINENRADGASZAEHLER`, `ULTRASCHALLZAEHLER`, `WIRBELGASZAEHLER`, `MODERNE_MESSEINRICHTUNG`, `ELEKTRONISCHER_HAUSHALTSZAEHLER`, `STEUEREINRICHTUNG`, `TECHNISCHESTEUEREINRICHTUNG`, `TARIFSCHALTGERAET`, `RUNDSTEUEREMPFAENGER`, `OPTIONALE_ZUS_ZAEHLEINRICHTUNG`, `MESSWANDLERSATZ_IMS_MME`, `KOMBIMESSWANDLER_IMS_MME`, `TARIFSCHALTGERAET_IMS_MME`, `RUNDSTEUEREMPFAENGER_IMS_MME`, `TEMPERATUR_KOMPENSATION`, `HOECHSTBELASTUNGS_ANZEIGER`, `SONSTIGES_GERAET`, `SMARTMETERGATEWAY`, `STEUERBOX`, `BLOCKSTROMWANDLER`, `KOMBIMESSWANDLER`, `MODEM_GSM`, `ETHERNET_KOM`, `PLC_COM`, `MODEM_FESTNETZ`, `DSL_KOM`, `LTE_KOM`, `DICHTEMENGENUMWERTER`, `TEMPERATURMENGENUMWERTER`, `ZUSTANDSMENGENUMWERTER`, `MESSDATENREGISTRIERGERAET`, `WANDLER`, `BEFESTIGUNGSEINRICHTUNG`</Werte> |
| <span className="hbs-f hbs-e1">[bezeichnung](/bo4e/202610/com/Geraet#bezeichnung)</span> | Bezeichnung des Gerätes | string |
| <span className="hbs-f hbs-e1">[geraetenummer](/bo4e/202610/com/Geraet#geraetenummer)</span> | Die auf dem Geräte aufgedruckte Nummer, die vom MSB vergeben wird. | string |
| <span className="hbs-f hbs-e1">[geraetereferenz](/bo4e/202610/com/Geraet#geraetereferenz)</span> | geraetereferenz | string |
| <span className="hbs-g hbs-e1">[geraeteeigenschaften](/bo4e/202610/com/Geraet#geraeteeigenschaften)</span> | Festlegung der Eigenschaften des Gerätes. Z.B. Wandler MS/NS. | [Geraeteeigenschaften](/bo4e/202610/com/Geraeteeigenschaften) |
| <span className="hbs-f hbs-e2">[geraetetyp](/bo4e/202610/com/Geraeteeigenschaften#geraetetyp)</span> | Auflistung möglicher abzurechnender Gerätetypen | [Enum Geraetetyp](/bo4e/202610/enum/Geraetetyp)<br/><Werte>`WECHSELSTROMZAEHLER`, `DREHSTROMZAEHLER`, `ZWEIRICHTUNGSZAEHLER`, `RLM_ZAEHLER`, `IMS_ZAEHLER`, `BALGENGASZAEHLER`, `MAXIMUMZAEHLER`, `MULTIPLEXANLAGE`, `PAUSCHALANLAGE`, `VERSTAERKERANLAGE`, `SUMMATIONSGERAET`, `IMPULSGEBER`, `EDL_21_ZAEHLERAUFSATZ`, `VIER_QUADRANTEN_LASTGANGZAEHLER`, `MENGENUMWERTER`, `STROMWANDLER`, `SPANNUNGSWANDLER`, `DATENLOGGER`, `KOMMUNIKATIONSANSCHLUSS`, `MODEM`, `TELEKOMMUNIKATIONSEINRICHTUNG`, `KOMMUNIKATIONSEINRICHTUNG`, `DREHKOLBENGASZAEHLER`, `TURBINENRADGASZAEHLER`, `ULTRASCHALLZAEHLER`, `WIRBELGASZAEHLER`, `MODERNE_MESSEINRICHTUNG`, `ELEKTRONISCHER_HAUSHALTSZAEHLER`, `STEUEREINRICHTUNG`, `TECHNISCHESTEUEREINRICHTUNG`, `TARIFSCHALTGERAET`, `RUNDSTEUEREMPFAENGER`, `OPTIONALE_ZUS_ZAEHLEINRICHTUNG`, `MESSWANDLERSATZ_IMS_MME`, `KOMBIMESSWANDLER_IMS_MME`, `TARIFSCHALTGERAET_IMS_MME`, `RUNDSTEUEREMPFAENGER_IMS_MME`, `TEMPERATUR_KOMPENSATION`, `HOECHSTBELASTUNGS_ANZEIGER`, `SONSTIGES_GERAET`, `SMARTMETERGATEWAY`, `STEUERBOX`, `BLOCKSTROMWANDLER`, `KOMBIMESSWANDLER`, `MODEM_GSM`, `ETHERNET_KOM`, `PLC_COM`, `MODEM_FESTNETZ`, `DSL_KOM`, `LTE_KOM`, `DICHTEMENGENUMWERTER`, `TEMPERATURMENGENUMWERTER`, `ZUSTANDSMENGENUMWERTER`, `MESSDATENREGISTRIERGERAET`, `WANDLER`, `BEFESTIGUNGSEINRICHTUNG`</Werte> |
| <span className="hbs-f hbs-e2">[geraetemerkmal](/bo4e/202610/com/Geraeteeigenschaften#geraetemerkmal)</span> | Geraetemerkmal | [Enum Geraetemerkmal](/bo4e/202610/enum/Geraetemerkmal)<br/><Werte>`EINTARIF`, `ZWEITARIF`, `MEHRTARIF`, `GAS_G2P5`, `GAS_G4`, `GAS_G6`, `GAS_G10`, `GAS_G16`, `GAS_G25`, `GAS_G40`, `GAS_G65`, `GAS_G100`, `GAS_G160`, `GAS_G250`, `GAS_G350`, `GAS_G400`, `GAS_G4000`, `GAS_G650`, `GAS_G6500`, `GAS_G1000`, `GAS_G10000`, `GAS_G12500`, `GAS_G1600`, `GAS_G16000`, `GAS_G2500`, `IMPULSGEBER_G4_G100`, `IMPULSGEBER_G100`, `MODEM_GSM`, `MODEM_GPRS`, `MODEM_FUNK`, `MODEM_GSM_O_LG`, `MODEM_GSM_M_LG`, `MODEM_FESTNETZ`, `MODEM_GPRS_M_LG`, `PLC_COM`, `ETHERNET_KOM`, `DSL_KOM`, `LTE_KOM`, `RUNDSTEUEREMPFAENGER`, `TARIFSCHALTGERAET`, `ZUSTANDS_MU`, `TEMPERATUR_MU`, `KOMPAKT_MU`, `SYSTEM_MU`, `UNBESTIMMT`, `WASSER_MWZW`, `WASSER_WZWW`, `WASSER_WZ01`, `WASSER_WZ02`, `WASSER_WZ03`, `WASSER_WZ04`, `WASSER_WZ05`, `WASSER_WZ06`, `WASSER_WZ07`, `WASSER_WZ08`, `WASSER_WZ09`, `WASSER_WZ10`, `WASSER_VWZ04`, `WASSER_VWZ05`, `WASSER_VWZ06`, `WASSER_VWZ07`, `WASSER_VWZ10`, `DICHTEMENGENUMWERTER`, `TEMPERATURMENGENUMWERTER`, `ZUSTANDSMENGENUMWERTER`, `BLOCKSTROMWANDLER`, `MESSWANDLERSATZ_IMS_MME`, `KOMBIMESSWANDLER`, `SPANNUNGSWANDLER`</Werte> |
| <span className="hbs-f hbs-e2">[volumenerfassung](/bo4e/202610/com/Geraeteeigenschaften#volumenerfassung)</span> | Volumenerfassung | [Enum Volumenerfassung](/bo4e/202610/enum/Volumenerfassung)<br/><Werte>`HOCHFREQUENZSONDE`, `KENNLINIENKORREKTUR`, `SCHLEICHMENGENUNTERDRUECKUNG`</Werte> |
| <span className="hbs-f hbs-e2">[serialnummer](/bo4e/202610/com/Geraeteeigenschaften#serialnummer)</span> | serialnummer | string |
| <span className="hbs-f hbs-e2">[herstellungsdatum](/bo4e/202610/com/Geraeteeigenschaften#herstellungsdatum)</span> | Produktions-/Herstellungsdatum | string |
| <span className="hbs-f hbs-e2">[baujahr](/bo4e/202610/com/Geraeteeigenschaften#baujahr)</span> | Baujahr/Jahr des in Verkehrs bringens | string |
| <span className="hbs-f hbs-e2">[eichungBis](/bo4e/202610/com/Geraeteeigenschaften#eichungbis)</span> | Eichgültigkeit | string |
| <span className="hbs-f hbs-e2">[faktor](/bo4e/202610/com/Geraeteeigenschaften#faktor)</span> | faktor | number (float) |
| <span className="hbs-f hbs-e2">[firmwareVersion](/bo4e/202610/com/Geraeteeigenschaften#firmwareversion)</span> | Firmware-Version | string |
| <span className="hbs-f hbs-e2">[herstellerTypbezeichnung](/bo4e/202610/com/Geraeteeigenschaften#herstellertypbezeichnung)</span> | Hersteller-Typbezeichnung | string |
| <span className="hbs-f hbs-e2">[simKartenNummer](/bo4e/202610/com/Geraeteeigenschaften#simkartennummer)</span> | SIM-Kartennummer | string |
| <span className="hbs-f hbs-e2">[modemKennungIMSI](/bo4e/202610/com/Geraeteeigenschaften#modemkennungimsi)</span> | Modem-Kennung (IMSI) | string |
| <span className="hbs-f hbs-e2">[tkProvider](/bo4e/202610/com/Geraeteeigenschaften#tkprovider)</span> | Telekommunikationsanbieter | string |
| <span className="hbs-f hbs-e2">[ipVersion](/bo4e/202610/com/Geraeteeigenschaften#ipversion)</span> | IP-Version | string |
| <span className="hbs-f hbs-e1">[volumenerfassung](/bo4e/202610/com/Geraet#volumenerfassung)</span> | Volumenerfassung | [Enum Volumenerfassung](/bo4e/202610/enum/Volumenerfassung)<br/><Werte>`HOCHFREQUENZSONDE`, `KENNLINIENKORREKTUR`, `SCHLEICHMENGENUNTERDRUECKUNG`</Werte> |
| <span className="hbs-f hbs-e1">[weitereGeraetenummern](/bo4e/202610/com/Geraet#weiteregeraetenummern) <span className="hbs-liste">[ ]</span></span> | weitereGeraetenummern | string[] |
| <span className="hbs-g hbs-e0">[messdienstleistung](/bo4e/202610/bo/Messlokation#messdienstleistung) <span className="hbs-liste">[ ]</span></span> | Liste der Messdienstleistungen, die zu dieser Messstelle gehört. | [Dienstleistung[]](/bo4e/202610/com/Dienstleistung) |
| <span className="hbs-f hbs-e1">[dienstleistungstyp](/bo4e/202610/com/Dienstleistung#dienstleistungstyp)</span> | Eindeutige Nummer der Dienstleistung. Details Dienstleistungstyp | [Enum Dienstleistungstyp](/bo4e/202610/enum/Dienstleistungstyp)<br/><Werte>`DATENBEREITSTELLUNG_TAEGLICH`, `DATENBEREITSTELLUNG_WOECHENTLICH`, `DATENBEREITSTELLUNG_MONATLICH`, `DATENBEREITSTELLUNG_JAEHRLICH`, `DATENBEREITSTELLUNG_HISTORISCHE_LG`, `DATENBEREITSTELLUNG_STUENDLICH`, `DATENBEREITSTELLUNG_VIERTELJAEHRLICH`, `DATENBEREITSTELLUNG_HALBJAEHRLICH`, `DATENBEREITSTELLUNG_MONATLICH_ZUSAETZLICH`, `DATENBEREITSTELLUNG_EINMALIG`, `AUSLESUNG_2X_TAEGLICH_FERNAUSLESUNG`, `AUSLESUNG_TAEGLICH_FERNAUSLESUNG`, `AUSLESUNG_LGK_MANUELL_MSB`, `AUSLESUNG_MONATLICH_SLP_FERNAUSLESUNG`, `AUSLESUNG_JAEHRLICH_SLP_FERNAUSLESUNG`, `AUSLESUNG_MDE_SLP`, `ABLESUNG_MONATLICH_SLP`, `ABLESUNG_VIERTELJAEHRLICH_SLP`, `ABLESUNG_HALBJAEHRLICH_SLP`, `ABLESUNG_JAEHRLICH_SLP`, `AUSLESUNG_SLP_FERNAUSLESUNG`, `ABLESUNG_SLP_ZUSAETZLICH_MSB`, `ABLESUNG_SLP_ZUSAETZLICH_KUNDE`, `AUSLESUNG_LGK_FERNAUSLESUNG_ZUSAETZLICH_MSB`, `AUSLESUNG_MOATLICH_FERNAUSLESUNG`, `AUSLESUNG_STUENDLICH_FERNAUSLESUNG`, `ABLESUNG_MONATLICH_LGK`, `AUSLESUNG_TEMERATURMENGENUMWERTER`, `AUSLESUNG_ZUSTANDSMENGENUMWERTER`, `AUSLESUNG_SYSTEMMENGENUMWERTER`, `AUSLESUNG_VORGANG_SLP`, `AUSLESUUNG_KOMPAKTMENGENUMWERTER`, `AUSLESUNG_MDE_LGK`, `SPERRUNG_SLP`, `ENTSPERRUNG_SLP`, `SPERRUNG_RLM`, `ENTSPERRUNG_RLM`, `MAHNKOSTEN`, `INKASSOKOSTEN`</Werte> |
| <span className="hbs-f hbs-e1">[bezeichnung](/bo4e/202610/com/Dienstleistung#bezeichnung)</span> | Bezeichnung der Dienstleistung. | string |
| <span className="hbs-f hbs-e0">[messlokationszaehler](/bo4e/202610/bo/Messlokation#messlokationszaehler) <span className="hbs-liste">[ ]</span></span> | Zähler, die zu dieser Messlokation gehören. Details | string[] |
| <span className="hbs-g hbs-e0">[zaehlwerke](/bo4e/202610/bo/Messlokation#zaehlwerke) <span className="hbs-liste">[ ]</span></span> | Die Zählwerke des Zählers. | [Zaehlwerk[]](/bo4e/202610/com/Zaehlwerk) |
| <span className="hbs-f hbs-e1">[zaehlwerkId](/bo4e/202610/com/Zaehlwerk#zaehlwerkid)</span> | Identifikation des Zählwerks (Registers) innerhalb des Zählers. Oftmals eine laufende Nummer hinter der<br/>Zählernummer. Z.B. 47110815_1 | string |
| <span className="hbs-f hbs-e1">[bezeichnung](/bo4e/202610/com/Zaehlwerk#bezeichnung)</span> | Zusätzliche Bezeichnung, z.B. Zählwerk_Wirkarbeit. | string |
| <span className="hbs-f hbs-e1">[richtung](/bo4e/202610/com/Zaehlwerk#richtung)</span> | Die Energierichtung, Einspeisung oder Ausspeisung. Details Energierichtung | [Enum Energierichtung](/bo4e/202610/enum/Energierichtung)<br/><Werte>`AUSSP`, `EINSP`</Werte> |
| <span className="hbs-f hbs-e1">[obisKennzahl](/bo4e/202610/com/Zaehlwerk#obiskennzahl)</span> | Die OBIS-Kennzahl für das Zählwerk, die festlegt, welche auf die gemessene Größe mit dem Stand gemeldet wird.<br/>Nur Zählwerkstände mit dieser OBIS-Kennzahl werden an diesem Zählwerk registriert. Beispiel:1-0:1.8.1 für<br/>elektrische Wirkarbeit. | string |
| <span className="hbs-f hbs-e1">[wandlerfaktor](/bo4e/202610/com/Zaehlwerk#wandlerfaktor)</span> | Mit diesem Faktor wird eine Zählerstandsdifferenz multipliziert, um zum eigentlichen Verbrauch im Zeitraum zu<br/>kommen. | number (float) |
| <span className="hbs-f hbs-e1">[einheit](/bo4e/202610/com/Zaehlwerk#einheit)</span> | Die Einheit der gemessenen Größe, z.B. kWh. Details Mengeneinheit | [Enum Mengeneinheit](/bo4e/202610/enum/Mengeneinheit)<br/><Werte>`W`, `WH`, `KW`, `KWH`, `KVARH`, `MW`, `MWH`, `STUECK`, `KUBIKMETER`, `STUNDE`, `TAG`, `MONAT`, `JAHR`, `PROZENT`, `ANZAHL`, `VAR`, `KVAR`, `VARH`, `KWHK`, `Z16`, `KWT`, `WATT_PRO_QUADRATMETER`, `METER_PRO_SEKUNDE`</Werte> |
| <span className="hbs-f hbs-e1">[schwachlastfaehig](/bo4e/202610/com/Zaehlwerk#schwachlastfaehig)</span> | schwachlastfaehig | [Enum Schwachlastfaehig](/bo4e/202610/enum/Schwachlastfaehig)<br/><Werte>`SCHWACHLASTFAEHIG`, `NICHT_SCHWACHLASTFAEHIG`</Werte> |
| <span className="hbs-f hbs-e1">[verbrauchsart](/bo4e/202610/com/Zaehlwerk#verbrauchsart) <span className="hbs-liste">[ ]</span></span> | Stromverbrauchsart/Verbrauchsart Marktlokation | [Enum Verbrauchsart[]](/bo4e/202610/enum/Verbrauchsart)<br/><Werte>`KL`, `W`, `EMOB`, `SB`, `SW`, `WK`</Werte> |
| <span className="hbs-f hbs-e1">[unterbrechbarkeit](/bo4e/202610/com/Zaehlwerk#unterbrechbarkeit)</span> | Stromverbrauchsart/Unterbrechbarkeit Marktlokation | [Enum Unterbrechbarkeit](/bo4e/202610/enum/Unterbrechbarkeit)<br/><Werte>`UV`, `NUV`</Werte> |
| <span className="hbs-f hbs-e1">[waermenutzung](/bo4e/202610/com/Zaehlwerk#waermenutzung)</span> | Stromverbrauchsart/Wärmenutzung Marktlokation | [Enum Waermenutzung](/bo4e/202610/enum/Waermenutzung)<br/><Werte>`SPEICHERHEIZUNG`, `WAERMEPUMPE`, `DIREKTHEIZUNG`, `WAERMEPUMPE_WAERME_KAELTE`, `WAERMEPUMPE_KAELTE`, `WAERMEPUMPE_WAERME`</Werte> |
| <span className="hbs-g hbs-e1">[konzessionsabgabe](/bo4e/202610/com/Zaehlwerk#konzessionsabgabe)</span> | — | [Konzessionsabgabe](/bo4e/202610/com/Konzessionsabgabe) |
| <span className="hbs-f hbs-e2">[satz](/bo4e/202610/com/Konzessionsabgabe#satz)</span> | Art der Konzessionsabgabe | [Enum AbgabeArt](/bo4e/202610/enum/AbgabeArt)<br/><Werte>`KAS`, `SA`, `SAS`, `TA`, `TAS`, `TK`, `TKS`, `TS`, `TSS`</Werte> |
| <span className="hbs-f hbs-e2">[kosten](/bo4e/202610/com/Konzessionsabgabe#kosten)</span> | Kosten | number (float) |
| <span className="hbs-f hbs-e2">[kategorie](/bo4e/202610/com/Konzessionsabgabe#kategorie)</span> | Kategorie | string |
| <span className="hbs-f hbs-e1">[steuerbefreit](/bo4e/202610/com/Zaehlwerk#steuerbefreit)</span> | steuerbefreit | boolean |
| <span className="hbs-f hbs-e1">[vorkommastelle](/bo4e/202610/com/Zaehlwerk#vorkommastelle)</span> | vorkommastelle | integer |
| <span className="hbs-f hbs-e1">[nachkommastelle](/bo4e/202610/com/Zaehlwerk#nachkommastelle)</span> | nachkommastelle | integer |
| <span className="hbs-f hbs-e1">[abrechnungsrelevant](/bo4e/202610/com/Zaehlwerk#abrechnungsrelevant)</span> | abrechnungsrelevant | boolean |
| <span className="hbs-f hbs-e1">[anzahlAblesungen](/bo4e/202610/com/Zaehlwerk#anzahlablesungen)</span> | anzahlAblesungen | integer |
| <span className="hbs-g hbs-e1">[zaehlzeiten](/bo4e/202610/com/Zaehlwerk#zaehlzeiten)</span> | — | [Zaehlzeitregister](/bo4e/202610/com/Zaehlzeitregister) |
| <span className="hbs-f hbs-e2">[register](/bo4e/202610/com/Zaehlzeitregister#register)</span> | Zählzeitregister | string |
| <span className="hbs-f hbs-e2">[zaehlzeitDefinition](/bo4e/202610/com/Zaehlzeitregister#zaehlzeitdefinition)</span> | Zählzeitdefinition | string |
| <span className="hbs-f hbs-e2">[schwachlastfaehig](/bo4e/202610/com/Zaehlzeitregister#schwachlastfaehig)</span> | Schwachlastfähigkeit des Registers | [Enum Schwachlastfaehig](/bo4e/202610/enum/Schwachlastfaehig)<br/><Werte>`SCHWACHLASTFAEHIG`, `NICHT_SCHWACHLASTFAEHIG`</Werte> |
| <span className="hbs-f hbs-e1">[konfiguration](/bo4e/202610/com/Zaehlwerk#konfiguration)</span> | Konfiguration (iMSys) des Zählwerks | string |
| <span className="hbs-f hbs-e1">[messprodukt](/bo4e/202610/com/Zaehlwerk#messprodukt)</span> | messprodukt | string |
| <span className="hbs-f hbs-e1">[wertegranularitaet](/bo4e/202610/com/Zaehlwerk#wertegranularitaet)</span> | Wertegranularitaet | [Enum Wertegranularitaet](/bo4e/202610/enum/Wertegranularitaet)<br/><Werte>`JAEHRLICH`, `HALBJAEHRLICH`, `QUARTALSWEISE`, `MONATLICH`</Werte> |
| <span className="hbs-f hbs-e1">[notwendigkeitZweiteMessung](/bo4e/202610/com/Zaehlwerk#notwendigkeitzweitemessung)</span> | NotwendigkeitZweiteMessung | [Enum NotwendigkeitZweiteMessung](/bo4e/202610/enum/NotwendigkeitZweiteMessung)<br/><Werte>`VORHANDEN`, `NICHT_VORHANDEN`</Werte> |
| <span className="hbs-f hbs-e1">[werteuebermittlungVerwendungszweck](/bo4e/202610/com/Zaehlwerk#werteuebermittlungverwendungszweck)</span> | WerteuebermittlungVerwendungszweck | [Enum WerteuebermittlungVerwendungszweck](/bo4e/202610/enum/WerteuebermittlungVerwendungszweck)<br/><Werte>`VORHANDEN`, `NICHT_VORHANDEN`</Werte> |
| <span className="hbs-f hbs-e1">[artEMobilitaet](/bo4e/202610/com/Zaehlwerk#artemobilitaet)</span> | ArtEmobilitaet | [Enum ArtEmobilitaet](/bo4e/202610/enum/ArtEmobilitaet)<br/><Werte>`WB`, `LS`, `LP`</Werte> |
| <span className="hbs-f hbs-e1">[konfigurationsprodukt](/bo4e/202610/com/Zaehlwerk#konfigurationsprodukt)</span> | konfigurationsprodukt | string |
| <span className="hbs-f hbs-e1">[keinKonfigurationsprodukt](/bo4e/202610/com/Zaehlwerk#keinkonfigurationsprodukt)</span> | keinKonfigurationsprodukt | boolean |
| <span className="hbs-f hbs-e1">[leistungskurvendefinition](/bo4e/202610/com/Zaehlwerk#leistungskurvendefinition)</span> | leistungskurvendefinition | string |
| <span className="hbs-g hbs-e1">[verwendungszwecke](/bo4e/202610/com/Zaehlwerk#verwendungszwecke) <span className="hbs-liste">[ ]</span></span> | Verwendungungszweck der Werte Marktlokation | [Verwendungszweck[]](/bo4e/202610/com/Verwendungszweck) |
| <span className="hbs-f hbs-e2">[marktrolle](/bo4e/202610/com/Verwendungszweck#marktrolle)</span> | Diese Rollen kann ein Marktteilnehmer einnehmen | [Enum Marktrolle](/bo4e/202610/enum/Marktrolle)<br/><Werte>`NB`, `LF`, `MSB`, `MSBA`, `GMSB`, `MDL`, `DL`, `BKV`, `UENB`, `KUNDE-SELBST-NN`, `MGV`, `EIV`, `RB`, `KUNDE`, `INTERESSENT`, `KN`, `UBA`, `BIKO`, `ESA`</Werte> |
| <span className="hbs-f hbs-e2">[zweck](/bo4e/202610/com/Verwendungszweck#zweck) <span className="hbs-liste">[ ]</span></span> | zweck | [Enum VerwendungszweckValue[]](/bo4e/202610/enum/VerwendungszweckValue)<br/><Werte>`NETZNUTZUNGSABRECHNUNG`, `BILANZKREISABRECHNUNG`, `MEHRMINDERMENGENABRECHNUNG`, `ENDKUNDENABRECHNUNG`, `UEBERMITTLUNG_AN_DAS_HKNR`, `BLINDARBEITSABRECHNUNG`, `ERMITTLUNG_AUSGEGLICHENHEIT_BILANZKREIS`, `BLINDARBEITABRECHNUNG_BETRIEBSFUEHRUNG`, `ES_LIEGT_KEIN_VERWENDUNGSZWECK_VOR`</Werte> |
| <span className="hbs-f hbs-e1">[verwendungszweckNB](/bo4e/202610/com/Zaehlwerk#verwendungszwecknb)</span> | Codes gemäß Codeliste der Verwendungszwecke Verwendungszweck NB | string |
| <span className="hbs-f hbs-e1">[verwendungszweckLF](/bo4e/202610/com/Zaehlwerk#verwendungszwecklf)</span> | Codes gemäß Codeliste der Verwendungszwecke Verwendungszweck LF | string |
| <span className="hbs-f hbs-e1">[verwendungszweckUENB](/bo4e/202610/com/Zaehlwerk#verwendungszweckuenb)</span> | Codes gemäß Codeliste der Verwendungszwecke Verwendungszweck ÜNB | string |
| <span className="hbs-f hbs-e1">[keinProdukt](/bo4e/202610/com/Zaehlwerk#keinprodukt)</span> | CCI+11++ZF6: keinProdukt zugeordnet | boolean |
| <span className="hbs-g hbs-e0">[marktrollen](/bo4e/202610/bo/Messlokation#marktrollen) <span className="hbs-liste">[ ]</span></span> | marktrollen für EDIFACT mapping | [Marktteilnehmer[]](/bo4e/202610/bo/Marktteilnehmer) |
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
| <span className="hbs-f hbs-e0">[datenqualitaet](/bo4e/202610/bo/Messlokation#datenqualitaet)</span> | Datenqualitaet | [Enum Datenqualitaet](/bo4e/202610/enum/Datenqualitaet)<br/><Werte>`ERWARTETE_DATEN`, `IM_SYSTEM_VORHANDENE_DATEN`, `INFORMATIVE_DATEN`, `GUELTIGE_DATEN`, `KEINE_DATEN`, `IM_SYSTEM_KEINE_DATEN_VORHANDEN`, `KEINE_DATEN_ERWARTET`, `DIFFERENZ_DATEN`, `DIFFERENZ_ERWARTETE_DATEN`, `DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</Werte> |
| <span className="hbs-g hbs-e0">[gueltigkeitszeitraum](/bo4e/202610/bo/Messlokation#gueltigkeitszeitraum)</span> | — | [Zeitraum](/bo4e/202610/com/Zeitraum) |
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

## Verwendet in

### messlokationsId

104 Verwendung(en) in den Nachrichtentypen INVOIC, ORDERS, QUOTES, REQOTE, UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_15001](/schnittstellen/202610/pruefi/QUOTES/PI_15001) | Prüfi | QUOTES | stammdaten › MESSLOKATION |
| [PI_15003](/schnittstellen/202610/pruefi/QUOTES/PI_15003) | Prüfi | QUOTES | stammdaten › MESSLOKATION |
| [PI_15004](/schnittstellen/202610/pruefi/QUOTES/PI_15004) | Prüfi | QUOTES | stammdaten › MESSLOKATION |
| [PI_15005](/schnittstellen/202610/pruefi/QUOTES/PI_15005) | Prüfi | QUOTES | stammdaten › MESSLOKATION |
| [PI_17121](/schnittstellen/202610/pruefi/ORDERS/PI_17121) | Prüfi | ORDERS | stammdaten › MESSLOKATION |
| [PI_17134](/schnittstellen/202610/pruefi/ORDERS/PI_17134) | Prüfi | ORDERS | stammdaten › MESSLOKATION |
| [PI_31003](/schnittstellen/202610/pruefi/INVOIC/PI_31003) | Prüfi | INVOIC | stammdaten › MESSLOKATION |
| [PI_31004](/schnittstellen/202610/pruefi/INVOIC/PI_31004) | Prüfi | INVOIC | stammdaten › MESSLOKATION |
| [PI_31005](/schnittstellen/202610/pruefi/INVOIC/PI_31005) | Prüfi | INVOIC | stammdaten › MESSLOKATION |
| [PI_31006](/schnittstellen/202610/pruefi/INVOIC/PI_31006) | Prüfi | INVOIC | stammdaten › MESSLOKATION |
| [PI_31009](/schnittstellen/202610/pruefi/INVOIC/PI_31009) | Prüfi | INVOIC | stammdaten › MESSLOKATION |
| [PI_31011](/schnittstellen/202610/pruefi/INVOIC/PI_31011) | Prüfi | INVOIC | stammdaten › MESSLOKATION |
| [PI_35001](/schnittstellen/202610/pruefi/REQOTE/PI_35001) | Prüfi | REQOTE | stammdaten › MESSLOKATION |
| [PI_35004](/schnittstellen/202610/pruefi/REQOTE/PI_35004) | Prüfi | REQOTE | stammdaten › MESSLOKATION |
| [PI_44001](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44001) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_44002](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_44013](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_44014](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_44016](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44016) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_44035](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44035) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_44039](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44039) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_44040](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44040) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_44041](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44041) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_44042](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44042) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_44043](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44043) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_44044](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44044) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_44052](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44052) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_44053](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44053) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_44060](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44060) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_44101](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44101) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_44102](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44102) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_44112](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44112) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_44113](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44113) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_44115](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44115) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_44116](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44116) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_44117](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44117) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_44119](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44119) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_44139](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44139) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_44140](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44140) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_44142](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44142) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_44143](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44143) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_44145](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44145) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_44146](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44146) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_44147](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44147) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_44148](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44148) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_44149](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44149) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_44159](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44159) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_44160](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44160) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_44161](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44161) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_44162](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44162) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_44163](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44163) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_44164](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44164) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_44165](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44165) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_44166](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44166) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_44167](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44167) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_44168](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_44175](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44175) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_44176](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44176) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_44180](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44180) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_44181](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44181) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_44182](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44182) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_44183](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44183) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_55002](/schnittstellen/202610/pruefi/UTILMD/PI_55002) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55013](/schnittstellen/202610/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55035](/schnittstellen/202610/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55039](/schnittstellen/202610/pruefi/UTILMD/PI_55039) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55040](/schnittstellen/202610/pruefi/UTILMD/PI_55040) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55041](/schnittstellen/202610/pruefi/UTILMD/PI_55041) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55042](/schnittstellen/202610/pruefi/UTILMD/PI_55042) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55044](/schnittstellen/202610/pruefi/UTILMD/PI_55044) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55051](/schnittstellen/202610/pruefi/UTILMD/PI_55051) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55052](/schnittstellen/202610/pruefi/UTILMD/PI_55052) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55053](/schnittstellen/202610/pruefi/UTILMD/PI_55053) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55060](/schnittstellen/202610/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55074](/schnittstellen/202610/pruefi/UTILMD/PI_55074) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55075](/schnittstellen/202610/pruefi/UTILMD/PI_55075) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55078](/schnittstellen/202610/pruefi/UTILMD/PI_55078) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55095](/schnittstellen/202610/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55170](/schnittstellen/202610/pruefi/UTILMD/PI_55170) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55173](/schnittstellen/202610/pruefi/UTILMD/PI_55173) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55175](/schnittstellen/202610/pruefi/UTILMD/PI_55175) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55177](/schnittstellen/202610/pruefi/UTILMD/PI_55177) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55180](/schnittstellen/202610/pruefi/UTILMD/PI_55180) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55194](/schnittstellen/202610/pruefi/UTILMD/PI_55194) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55600](/schnittstellen/202610/pruefi/UTILMD/PI_55600) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55601](/schnittstellen/202610/pruefi/UTILMD/PI_55601) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55602](/schnittstellen/202610/pruefi/UTILMD/PI_55602) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55603](/schnittstellen/202610/pruefi/UTILMD/PI_55603) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55607](/schnittstellen/202610/pruefi/UTILMD/PI_55607) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55611](/schnittstellen/202610/pruefi/UTILMD/PI_55611) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55620](/schnittstellen/202610/pruefi/UTILMD/PI_55620) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55626](/schnittstellen/202610/pruefi/UTILMD/PI_55626) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55632](/schnittstellen/202610/pruefi/UTILMD/PI_55632) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55638](/schnittstellen/202610/pruefi/UTILMD/PI_55638) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55643](/schnittstellen/202610/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55648](/schnittstellen/202610/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55653](/schnittstellen/202610/pruefi/UTILMD/PI_55653) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55658](/schnittstellen/202610/pruefi/UTILMD/PI_55658) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55663](/schnittstellen/202610/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55669](/schnittstellen/202610/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55690](/schnittstellen/202610/pruefi/UTILMD/PI_55690) | Prüfi | UTILMD | stammdaten › MESSLOKATION |

### netzebenemessung

10 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55060](/schnittstellen/202610/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55643](/schnittstellen/202610/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55648](/schnittstellen/202610/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55653](/schnittstellen/202610/pruefi/UTILMD/PI_55653) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55658](/schnittstellen/202610/pruefi/UTILMD/PI_55658) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55663](/schnittstellen/202610/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55669](/schnittstellen/202610/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | stammdaten › MESSLOKATION |

### messadresse

1 Verwendung(en) in den Nachrichtentypen INVOIC.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_31003](/schnittstellen/202610/pruefi/INVOIC/PI_31003) | Prüfi | INVOIC | stammdaten › MESSLOKATION |

### gasqualitaet

12 Verwendung(en) in den Nachrichtentypen UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_44002](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_44013](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_44014](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_44035](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44035) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_44043](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44043) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_44060](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44060) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_44112](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44112) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_44113](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44113) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_44139](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44139) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_44140](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44140) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_44142](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44142) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_44168](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |

### betriebszustand

7 Verwendung(en) in den Nachrichtentypen UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_44043](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44043) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_44168](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55632](/schnittstellen/202610/pruefi/UTILMD/PI_55632) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55638](/schnittstellen/202610/pruefi/UTILMD/PI_55638) | Prüfi | UTILMD | stammdaten › MESSLOKATION |

### referenzMarktlokationsId

3 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › MESSLOKATION |

### verwendungsumfang

4 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55060](/schnittstellen/202610/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › MESSLOKATION |

### datenqualitaet

17 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55039](/schnittstellen/202610/pruefi/UTILMD/PI_55039) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55042](/schnittstellen/202610/pruefi/UTILMD/PI_55042) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55194](/schnittstellen/202610/pruefi/UTILMD/PI_55194) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55620](/schnittstellen/202610/pruefi/UTILMD/PI_55620) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55626](/schnittstellen/202610/pruefi/UTILMD/PI_55626) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55632](/schnittstellen/202610/pruefi/UTILMD/PI_55632) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55638](/schnittstellen/202610/pruefi/UTILMD/PI_55638) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55643](/schnittstellen/202610/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55648](/schnittstellen/202610/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55653](/schnittstellen/202610/pruefi/UTILMD/PI_55653) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55658](/schnittstellen/202610/pruefi/UTILMD/PI_55658) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55663](/schnittstellen/202610/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55669](/schnittstellen/202610/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | stammdaten › MESSLOKATION |
| [PI_55690](/schnittstellen/202610/pruefi/UTILMD/PI_55690) | Prüfi | UTILMD | stammdaten › MESSLOKATION |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
