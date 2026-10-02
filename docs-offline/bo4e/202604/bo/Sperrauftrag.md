# Sperrauftrag
<span hidden data-pagefind-meta={"title:Sperrauftrag — BO4E-Geschäftsobjekt (FV 202604)"} />

BO4E-Geschäftsobjekt · 9 Felder · 0 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="botyp"></a>`boTyp` <span className="hbs-pflicht">\*</span> | [Enum BOTyp](/bo4e/202604/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> | Typ des BO |
| <a id="versionstruktur"></a>`versionStruktur` <span className="hbs-pflicht">\*</span> | string | versionStruktur |
| <a id="treffpunkt"></a>`treffpunkt` | [Adresse](/bo4e/202604/com/Adresse) | — |
| <a id="sperrauftragsart"></a>`sperrauftragsart` | [Enum Sperrauftragsart](/bo4e/202604/enum/Sperrauftragsart)<br/><Werte>`SPERREN`, `ENTSPERREN`</Werte> | Handelt es sich um einen Auftrag zum SPERREN oder ENTSPERREN? |
| <a id="sperrauftragsstatus"></a>`sperrauftragsstatus` | [Enum Auftragsstatus](/bo4e/202604/enum/Auftragsstatus)<br/><Werte>`GESCHEITERT`, `ERFOLGREICH`, `LIEFERUNG_GEPLANT`, `GEPLANT`, `ZUGESTIMMT`, `WIDERSPROCHEN`, `STOERUNGSFREI`, `GESTOERT`, `FESTGESTELLTE_STOERUNG`, `VERMUTETE_STOERUNG`, `ABGELEHNT`, `BEENDET`, `ANTWORT_DRITTER`, `BESTAETIGT`, `UMGESETZT`, `ENFG_STROMSPEICHER_UND_VERLUSTENERGIE`, `ENFG_ELEKTRISCH_ANGETRIEBENE_WAERMEPUMPEN`, `ENFG_UMLAGEERHEBUNG_BEI_ANLAGEN_ZUR_VERSTROMUNG_VON_KUPPELGASEN`, `ENFG_HERSTELLUNG_VON_GRUENEN_WASSERSTOFF`, `ENFG_STROMKOSTENINTENSIVE_UNTERNEHMEN`, `ENFG_HERSTELLUNG_VON_WASSERSTOFF_IN_STROMKOSTENINTENSIVEN_UNTERNEHMEN`, `ENFG_SCHIENENBAHNEN`, `ENFG_ELEKTRISCHE_BETRIEBENE_BUSSEN_IM_LINIENVERKEHR`, `ENFG_LANDSTROMANLAGEN`, `AENDERUNG_DER_DATEN`, `KEINE_AENDERUNG_DER_DATEN`, `ZEITREIHE_AKZEPTIERT`, `ZEITREIHE_NICHT_AKZEPTIERT`</Werte> | Auftragsstatus |
| <a id="sperrauftragsablehngrund"></a>`sperrauftragsablehngrund` | [Enum Sperrauftragsablehngrund](/bo4e/202604/enum/Sperrauftragsablehngrund)<br/><Werte>`DUPLIKAT`, `FALSCHER_MSB`, `FALSCHE_SPANNUNGSEBENE`, `WEITERE_MALO_BETROFFEN`, `ANDERER_ABLEHNGRUND`, `FRISTVERLETZUNG_TERMINGEBUNDEN`, `FRISTVERLETZUNG_NICHT_TERMINGEBUNDEN`, `ANDERER_FEHLER`, `LIEGT_BEREITS_VOR`, `ANDERER_ZUKUENFTIGER_LIEFERANT`, `BESTAETIGTER_LIEFERBEGINN`</Werte> | Falls Sperrauftragsstatus = ABGELEHNT |
| <a id="sperrauftragsverhinderungsgrund"></a>`sperrauftragsverhinderungsgrund` | [Enum Sperrauftragsverhinderungsgrund](/bo4e/202604/enum/Sperrauftragsverhinderungsgrund)<br/><Werte>`RECHTLICHER_GRUND_FEHLT`, `AKTIVE_ZUTRITTSVERWEIGERUNG`, `PASSIVE_ZUTRITTSVERWEIGERUNG`, `ANDERER_VERHINDERUNGSGRUND`, `TATSAECHLICHER_VERHINDERUNGSGRUND`, `TECHNISCHER_VERHINDERUNGSGRUND`, `ANSCHLUSSNUTZER_WURDE_NICHT_ANGETROFFEN`</Werte> | Falls Sperrauftragsstatus = GESCHEITERT |
| <a id="zaehlernummer"></a>`zaehlernummer` | string | Die Nummer des zu sperrenden Zählers |
| <a id="istvomgerichtsvollzieherangeordnet"></a>`istVomGerichtsvollzieherAngeordnet` | boolean | True, falls die Sperrung vom Gerichtsvollzieher angeordnet ist. |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[boTyp](/bo4e/202604/bo/Sperrauftrag#botyp) <span className="hbs-pflicht">\*</span></span> | Typ des BO | [Enum BOTyp](/bo4e/202604/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> |
| <span className="hbs-f hbs-e0">[versionStruktur](/bo4e/202604/bo/Sperrauftrag#versionstruktur) <span className="hbs-pflicht">\*</span></span> | versionStruktur | string |
| <span className="hbs-g hbs-e0">[treffpunkt](/bo4e/202604/bo/Sperrauftrag#treffpunkt)</span> | — | [Adresse](/bo4e/202604/com/Adresse) |
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
| <span className="hbs-f hbs-e0">[sperrauftragsart](/bo4e/202604/bo/Sperrauftrag#sperrauftragsart)</span> | Handelt es sich um einen Auftrag zum SPERREN oder ENTSPERREN? | [Enum Sperrauftragsart](/bo4e/202604/enum/Sperrauftragsart)<br/><Werte>`SPERREN`, `ENTSPERREN`</Werte> |
| <span className="hbs-f hbs-e0">[sperrauftragsstatus](/bo4e/202604/bo/Sperrauftrag#sperrauftragsstatus)</span> | Auftragsstatus | [Enum Auftragsstatus](/bo4e/202604/enum/Auftragsstatus)<br/><Werte>`GESCHEITERT`, `ERFOLGREICH`, `LIEFERUNG_GEPLANT`, `GEPLANT`, `ZUGESTIMMT`, `WIDERSPROCHEN`, `STOERUNGSFREI`, `GESTOERT`, `FESTGESTELLTE_STOERUNG`, `VERMUTETE_STOERUNG`, `ABGELEHNT`, `BEENDET`, `ANTWORT_DRITTER`, `BESTAETIGT`, `UMGESETZT`, `ENFG_STROMSPEICHER_UND_VERLUSTENERGIE`, `ENFG_ELEKTRISCH_ANGETRIEBENE_WAERMEPUMPEN`, `ENFG_UMLAGEERHEBUNG_BEI_ANLAGEN_ZUR_VERSTROMUNG_VON_KUPPELGASEN`, `ENFG_HERSTELLUNG_VON_GRUENEN_WASSERSTOFF`, `ENFG_STROMKOSTENINTENSIVE_UNTERNEHMEN`, `ENFG_HERSTELLUNG_VON_WASSERSTOFF_IN_STROMKOSTENINTENSIVEN_UNTERNEHMEN`, `ENFG_SCHIENENBAHNEN`, `ENFG_ELEKTRISCHE_BETRIEBENE_BUSSEN_IM_LINIENVERKEHR`, `ENFG_LANDSTROMANLAGEN`, `AENDERUNG_DER_DATEN`, `KEINE_AENDERUNG_DER_DATEN`, `ZEITREIHE_AKZEPTIERT`, `ZEITREIHE_NICHT_AKZEPTIERT`</Werte> |
| <span className="hbs-f hbs-e0">[sperrauftragsablehngrund](/bo4e/202604/bo/Sperrauftrag#sperrauftragsablehngrund)</span> | Falls Sperrauftragsstatus = ABGELEHNT | [Enum Sperrauftragsablehngrund](/bo4e/202604/enum/Sperrauftragsablehngrund)<br/><Werte>`DUPLIKAT`, `FALSCHER_MSB`, `FALSCHE_SPANNUNGSEBENE`, `WEITERE_MALO_BETROFFEN`, `ANDERER_ABLEHNGRUND`, `FRISTVERLETZUNG_TERMINGEBUNDEN`, `FRISTVERLETZUNG_NICHT_TERMINGEBUNDEN`, `ANDERER_FEHLER`, `LIEGT_BEREITS_VOR`, `ANDERER_ZUKUENFTIGER_LIEFERANT`, `BESTAETIGTER_LIEFERBEGINN`</Werte> |
| <span className="hbs-f hbs-e0">[sperrauftragsverhinderungsgrund](/bo4e/202604/bo/Sperrauftrag#sperrauftragsverhinderungsgrund)</span> | Falls Sperrauftragsstatus = GESCHEITERT | [Enum Sperrauftragsverhinderungsgrund](/bo4e/202604/enum/Sperrauftragsverhinderungsgrund)<br/><Werte>`RECHTLICHER_GRUND_FEHLT`, `AKTIVE_ZUTRITTSVERWEIGERUNG`, `PASSIVE_ZUTRITTSVERWEIGERUNG`, `ANDERER_VERHINDERUNGSGRUND`, `TATSAECHLICHER_VERHINDERUNGSGRUND`, `TECHNISCHER_VERHINDERUNGSGRUND`, `ANSCHLUSSNUTZER_WURDE_NICHT_ANGETROFFEN`</Werte> |
| <span className="hbs-f hbs-e0">[zaehlernummer](/bo4e/202604/bo/Sperrauftrag#zaehlernummer)</span> | Die Nummer des zu sperrenden Zählers | string |
| <span className="hbs-f hbs-e0">[istVomGerichtsvollzieherAngeordnet](/bo4e/202604/bo/Sperrauftrag#istvomgerichtsvollzieherangeordnet)</span> | True, falls die Sperrung vom Gerichtsvollzieher angeordnet ist. | boolean |

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
