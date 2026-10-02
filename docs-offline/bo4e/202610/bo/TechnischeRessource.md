# TechnischeRessource
<span hidden data-pagefind-meta={"title:TechnischeRessource — BO4E-Geschäftsobjekt (FV 202610)"} />

BO4E-Geschäftsobjekt · 27 Felder · 151 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="botyp"></a>`boTyp` <span className="hbs-pflicht">\*</span> | [Enum BOTyp](/bo4e/202610/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> | Typ des BO |
| <a id="versionstruktur"></a>`versionStruktur` <span className="hbs-pflicht">\*</span> | string | versionStruktur |
| <a id="ressourcenid"></a>`ressourcenId` | string | ressourcenId |
| <a id="sparte"></a>`sparte` | [Enum Sparte](/bo4e/202610/enum/Sparte)<br/><Werte>`STROM`, `GAS`, `FERNWAERME`, `NAHWAERME`, `WASSER`, `ABWASSER`</Werte> | Sparte |
| <a id="lokationszuordnung"></a>`lokationszuordnung` | [Enum Lokationszuordnung](/bo4e/202610/enum/Lokationszuordnung)<br/><Werte>`UNVERAENDERT`, `BEGINNT`, `ENDET`</Werte> | Lokationszuordnung |
| <a id="referenzmesslokation"></a>`referenzMesslokation` | string | referenzMesslokation |
| <a id="referenzmarktlokation"></a>`referenzMarktlokation` | string | referenzMarktlokation |
| <a id="referenznetzlokation"></a>`referenzNetzlokation` | string | referenzNetzlokation |
| <a id="referenzsteuerbareressource"></a>`referenzSteuerbareRessource` | string | referenzSteuerbareRessource |
| <a id="referenztranche"></a>`referenzTranche` | string | referenzTranche |
| <a id="nennleistung"></a>`nennleistung` | [Nennleistung](/bo4e/202610/com/Nennleistung) | — |
| <a id="speicherkapazitaet"></a>`speicherkapazitaet` | number (float) | Speicherkapazität Beispiel: QTY+Z42:100:KWH' |
| <a id="verbrauchsart"></a>`verbrauchsart` | [Enum Verbrauchsart[]](/bo4e/202610/enum/Verbrauchsart)<br/><Werte>`KL`, `W`, `EMOB`, `SB`, `SW`, `WK`</Werte> | Verbrauchsart der Technischen Ressource Beispiel: CAV+Z64'     Z64: Kraft/Licht     Z65: Wärme     ZE5: E-Mobilität     ZA8: Straßenbeleuchtung |
| <a id="waermenutzung"></a>`waermenutzung` | [Enum Waermenutzung](/bo4e/202610/enum/Waermenutzung)<br/><Werte>`SPEICHERHEIZUNG`, `WAERMEPUMPE`, `DIREKTHEIZUNG`, `WAERMEPUMPE_WAERME_KAELTE`, `WAERMEPUMPE_KAELTE`, `WAERMEPUMPE_WAERME`</Werte> | Wärmenutzung Beispiel: CAV+Z56'     Z56: Speicherheizung     Z57: Wärmepumpe     Z61: Direktheizung |
| <a id="artemobilitaet"></a>`artEMobilitaet` | [Enum ArtEmobilitaet](/bo4e/202610/enum/ArtEmobilitaet)<br/><Werte>`WB`, `LS`, `LP`</Werte> | ArtEmobilitaet |
| <a id="erzeugungsart"></a>`erzeugungsart` | [Enum Erzeugungsart](/bo4e/202610/enum/Erzeugungsart)<br/><Werte>`EEG`, `KWK`, `EEG_DV`, `KWK_DV`, `WIND`, `SOLAR`, `KERNKRAFT`, `WASSER`, `GEOTHERMIE`, `BIOMASSE`, `KOHLE`, `GAS`, `SONSTIGE`, `SONSTIGE_EEG`, `SONSTIGE_ERZEUGUNGSART`</Werte> | Art der Erzeugung der Energie. Details Erzeugungsart Beispiel: CAV+ZF5' Erzeugungsart:     ZF5: Solar     ZF6: Wind     ZG0: Gas     ZG1: Wasser     ZG5: Sonstige Erzeugungsart |
| <a id="speicherart"></a>`speicherart` | [Enum Speicherart](/bo4e/202610/enum/Speicherart)<br/><Werte>`WASSERSTOFFSPEICHER`, `PUMPSPEICHER`, `BATTERIESPEICHER`, `SONSTIGE_SPEICHERART`</Werte> | Art der speicher. Details Speicherart Beispiel: CAV+ZF7' Speicherart:     ZF7: Wasserstoffspeicher     ZF8: Pumpspeicher     ZF9: Batteriespeicher     ZG6: Sonstige Speicherart |
| <a id="enwg"></a>`enwg` | boolean | enwg |
| <a id="inbetriebsetzungsdatum"></a>`inbetriebsetzungsdatum` | [Enum Inbetriebsetzung](/bo4e/202610/enum/Inbetriebsetzung)<br/><Werte>`INBETRIEBSETZUNG_NACH_2023`, `INBETRIEBSETZUNG_VOR_2024`</Werte> | Inbetriebsetzung |
| <a id="einordnung"></a>`einordnung` | [Enum RessourceWechselmoeglichkeit](/bo4e/202610/enum/RessourceWechselmoeglichkeit)<br/><Werte>`WECHSELMOEGLICHKEIT_EINMALIG_NOCH_MOEGLICH`, `WECHSELMOEGLICHKEIT_NICHT_MOEGLICH`, `BEFRISTET_OHNE_WECHSELMOEGLICHKEIT`, `WECHSEL_WURDE_DURCHGEFUEHRT`</Werte> | RessourceWechselmoeglichkeit |
| <a id="weitereeinrichtung"></a>`weitereEinrichtung` | boolean | weitereEinrichtung |
| <a id="art"></a>`art` | [Enum TechnischeRessourceArt](/bo4e/202610/enum/TechnischeRessourceArt)<br/><Werte>`STROMERZEUGUNG`, `STROMVERBRAUCH`, `SPEICHER`</Werte> | TechnischeRessourceArt |
| <a id="datenqualitaet"></a>`datenqualitaet` | [Enum Datenqualitaet](/bo4e/202610/enum/Datenqualitaet)<br/><Werte>`ERWARTETE_DATEN`, `IM_SYSTEM_VORHANDENE_DATEN`, `INFORMATIVE_DATEN`, `GUELTIGE_DATEN`, `KEINE_DATEN`, `IM_SYSTEM_KEINE_DATEN_VORHANDEN`, `KEINE_DATEN_ERWARTET`, `DIFFERENZ_DATEN`, `DIFFERENZ_ERWARTETE_DATEN`, `DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</Werte> | Datenqualitaet |
| <a id="gueltigkeitszeitraum"></a>`gueltigkeitszeitraum` | [Zeitraum](/bo4e/202610/com/Zeitraum) | — |
| <a id="erforderlicheprodukte"></a>`erforderlicheProdukte` | [Produkt[]](/bo4e/202610/com/Produkt) | erforderlicheProdukte |
| <a id="fernsteuerbarkeit"></a>`fernsteuerbarkeit` | boolean | fernsteuerbarkeit |
| <a id="verguetungsverpflichtung"></a>`verguetungsverpflichtung` | boolean | verguetungsverpflichtung |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[boTyp](/bo4e/202610/bo/TechnischeRessource#botyp) <span className="hbs-pflicht">\*</span></span> | Typ des BO | [Enum BOTyp](/bo4e/202610/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> |
| <span className="hbs-f hbs-e0">[versionStruktur](/bo4e/202610/bo/TechnischeRessource#versionstruktur) <span className="hbs-pflicht">\*</span></span> | versionStruktur | string |
| <span className="hbs-f hbs-e0">[ressourcenId](/bo4e/202610/bo/TechnischeRessource#ressourcenid)</span> | ressourcenId | string |
| <span className="hbs-f hbs-e0">[sparte](/bo4e/202610/bo/TechnischeRessource#sparte)</span> | Sparte | [Enum Sparte](/bo4e/202610/enum/Sparte)<br/><Werte>`STROM`, `GAS`, `FERNWAERME`, `NAHWAERME`, `WASSER`, `ABWASSER`</Werte> |
| <span className="hbs-f hbs-e0">[lokationszuordnung](/bo4e/202610/bo/TechnischeRessource#lokationszuordnung)</span> | Lokationszuordnung | [Enum Lokationszuordnung](/bo4e/202610/enum/Lokationszuordnung)<br/><Werte>`UNVERAENDERT`, `BEGINNT`, `ENDET`</Werte> |
| <span className="hbs-f hbs-e0">[referenzMesslokation](/bo4e/202610/bo/TechnischeRessource#referenzmesslokation)</span> | referenzMesslokation | string |
| <span className="hbs-f hbs-e0">[referenzMarktlokation](/bo4e/202610/bo/TechnischeRessource#referenzmarktlokation)</span> | referenzMarktlokation | string |
| <span className="hbs-f hbs-e0">[referenzNetzlokation](/bo4e/202610/bo/TechnischeRessource#referenznetzlokation)</span> | referenzNetzlokation | string |
| <span className="hbs-f hbs-e0">[referenzSteuerbareRessource](/bo4e/202610/bo/TechnischeRessource#referenzsteuerbareressource)</span> | referenzSteuerbareRessource | string |
| <span className="hbs-f hbs-e0">[referenzTranche](/bo4e/202610/bo/TechnischeRessource#referenztranche)</span> | referenzTranche | string |
| <span className="hbs-g hbs-e0">[nennleistung](/bo4e/202610/bo/TechnischeRessource#nennleistung)</span> | — | [Nennleistung](/bo4e/202610/com/Nennleistung) |
| <span className="hbs-f hbs-e1">[aufnahme](/bo4e/202610/com/Nennleistung#aufnahme)</span> | Aufnahme der Nennleistung | number (float) |
| <span className="hbs-f hbs-e1">[abgabe](/bo4e/202610/com/Nennleistung#abgabe)</span> | Abgabe der Nennleistung | number (float) |
| <span className="hbs-f hbs-e0">[speicherkapazitaet](/bo4e/202610/bo/TechnischeRessource#speicherkapazitaet)</span> | Speicherkapazität<br/>Beispiel: QTY+Z42:100:KWH' | number (float) |
| <span className="hbs-f hbs-e0">[verbrauchsart](/bo4e/202610/bo/TechnischeRessource#verbrauchsart) <span className="hbs-liste">[ ]</span></span> | Verbrauchsart der Technischen Ressource<br/>Beispiel: CAV+Z64'<br/>Z64: Kraft/Licht<br/>Z65: Wärme<br/>ZE5: E-Mobilität<br/>ZA8: Straßenbeleuchtung | [Enum Verbrauchsart[]](/bo4e/202610/enum/Verbrauchsart)<br/><Werte>`KL`, `W`, `EMOB`, `SB`, `SW`, `WK`</Werte> |
| <span className="hbs-f hbs-e0">[waermenutzung](/bo4e/202610/bo/TechnischeRessource#waermenutzung)</span> | Wärmenutzung<br/>Beispiel: CAV+Z56'<br/>Z56: Speicherheizung<br/>Z57: Wärmepumpe<br/>Z61: Direktheizung | [Enum Waermenutzung](/bo4e/202610/enum/Waermenutzung)<br/><Werte>`SPEICHERHEIZUNG`, `WAERMEPUMPE`, `DIREKTHEIZUNG`, `WAERMEPUMPE_WAERME_KAELTE`, `WAERMEPUMPE_KAELTE`, `WAERMEPUMPE_WAERME`</Werte> |
| <span className="hbs-f hbs-e0">[artEMobilitaet](/bo4e/202610/bo/TechnischeRessource#artemobilitaet)</span> | ArtEmobilitaet | [Enum ArtEmobilitaet](/bo4e/202610/enum/ArtEmobilitaet)<br/><Werte>`WB`, `LS`, `LP`</Werte> |
| <span className="hbs-f hbs-e0">[erzeugungsart](/bo4e/202610/bo/TechnischeRessource#erzeugungsart)</span> | Art der Erzeugung der Energie. Details Erzeugungsart<br/>Beispiel: CAV+ZF5'<br/>Erzeugungsart:<br/>ZF5: Solar<br/>ZF6: Wind<br/>ZG0: Gas<br/>ZG1: Wasser<br/>ZG5: Sonstige Erzeugungsart | [Enum Erzeugungsart](/bo4e/202610/enum/Erzeugungsart)<br/><Werte>`EEG`, `KWK`, `EEG_DV`, `KWK_DV`, `WIND`, `SOLAR`, `KERNKRAFT`, `WASSER`, `GEOTHERMIE`, `BIOMASSE`, `KOHLE`, `GAS`, `SONSTIGE`, `SONSTIGE_EEG`, `SONSTIGE_ERZEUGUNGSART`</Werte> |
| <span className="hbs-f hbs-e0">[speicherart](/bo4e/202610/bo/TechnischeRessource#speicherart)</span> | Art der speicher. Details Speicherart<br/>Beispiel: CAV+ZF7'<br/>Speicherart:<br/>ZF7: Wasserstoffspeicher<br/>ZF8: Pumpspeicher<br/>ZF9: Batteriespeicher<br/>ZG6: Sonstige Speicherart | [Enum Speicherart](/bo4e/202610/enum/Speicherart)<br/><Werte>`WASSERSTOFFSPEICHER`, `PUMPSPEICHER`, `BATTERIESPEICHER`, `SONSTIGE_SPEICHERART`</Werte> |
| <span className="hbs-f hbs-e0">[enwg](/bo4e/202610/bo/TechnischeRessource#enwg)</span> | enwg | boolean |
| <span className="hbs-f hbs-e0">[inbetriebsetzungsdatum](/bo4e/202610/bo/TechnischeRessource#inbetriebsetzungsdatum)</span> | Inbetriebsetzung | [Enum Inbetriebsetzung](/bo4e/202610/enum/Inbetriebsetzung)<br/><Werte>`INBETRIEBSETZUNG_NACH_2023`, `INBETRIEBSETZUNG_VOR_2024`</Werte> |
| <span className="hbs-f hbs-e0">[einordnung](/bo4e/202610/bo/TechnischeRessource#einordnung)</span> | RessourceWechselmoeglichkeit | [Enum RessourceWechselmoeglichkeit](/bo4e/202610/enum/RessourceWechselmoeglichkeit)<br/><Werte>`WECHSELMOEGLICHKEIT_EINMALIG_NOCH_MOEGLICH`, `WECHSELMOEGLICHKEIT_NICHT_MOEGLICH`, `BEFRISTET_OHNE_WECHSELMOEGLICHKEIT`, `WECHSEL_WURDE_DURCHGEFUEHRT`</Werte> |
| <span className="hbs-f hbs-e0">[weitereEinrichtung](/bo4e/202610/bo/TechnischeRessource#weitereeinrichtung)</span> | weitereEinrichtung | boolean |
| <span className="hbs-f hbs-e0">[art](/bo4e/202610/bo/TechnischeRessource#art)</span> | TechnischeRessourceArt | [Enum TechnischeRessourceArt](/bo4e/202610/enum/TechnischeRessourceArt)<br/><Werte>`STROMERZEUGUNG`, `STROMVERBRAUCH`, `SPEICHER`</Werte> |
| <span className="hbs-f hbs-e0">[datenqualitaet](/bo4e/202610/bo/TechnischeRessource#datenqualitaet)</span> | Datenqualitaet | [Enum Datenqualitaet](/bo4e/202610/enum/Datenqualitaet)<br/><Werte>`ERWARTETE_DATEN`, `IM_SYSTEM_VORHANDENE_DATEN`, `INFORMATIVE_DATEN`, `GUELTIGE_DATEN`, `KEINE_DATEN`, `IM_SYSTEM_KEINE_DATEN_VORHANDEN`, `KEINE_DATEN_ERWARTET`, `DIFFERENZ_DATEN`, `DIFFERENZ_ERWARTETE_DATEN`, `DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</Werte> |
| <span className="hbs-g hbs-e0">[gueltigkeitszeitraum](/bo4e/202610/bo/TechnischeRessource#gueltigkeitszeitraum)</span> | — | [Zeitraum](/bo4e/202610/com/Zeitraum) |
| <span className="hbs-f hbs-e1">[zeiteinheit](/bo4e/202610/com/Zeitraum#zeiteinheit)</span> | Zeiteinheit | [Enum Zeiteinheit](/bo4e/202610/enum/Zeiteinheit)<br/><Werte>`SEKUNDE`, `MINUTE`, `STUNDE`, `VIERTEL_STUNDE`, `TAG`, `WOCHE`, `MONAT`, `QUARTAL`, `HALBJAHR`, `JAHR`</Werte> |
| <span className="hbs-f hbs-e1">[dauer](/bo4e/202610/com/Zeitraum#dauer)</span> | dauer | integer |
| <span className="hbs-f hbs-e1">[startdatum](/bo4e/202610/com/Zeitraum#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e1">[enddatum](/bo4e/202610/com/Zeitraum#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-f hbs-e1">[einheit](/bo4e/202610/com/Zeitraum#einheit)</span> | Zeiteinheit | [Enum Zeiteinheit](/bo4e/202610/enum/Zeiteinheit)<br/><Werte>`SEKUNDE`, `MINUTE`, `STUNDE`, `VIERTEL_STUNDE`, `TAG`, `WOCHE`, `MONAT`, `QUARTAL`, `HALBJAHR`, `JAHR`</Werte> |
| <span className="hbs-f hbs-e1">[ableseZeitraum](/bo4e/202610/com/Zeitraum#ablesezeitraum)</span> | ableseZeitraum | string |
| <span className="hbs-f hbs-e1">[abrechnungsZeitraum](/bo4e/202610/com/Zeitraum#abrechnungszeitraum)</span> | abrechnungsZeitraum | string |
| <span className="hbs-f hbs-e1">[zeitraumText](/bo4e/202610/com/Zeitraum#zeitraumtext)</span> | zeitraumText | string |
| <span className="hbs-f hbs-e1">[zeitraumId](/bo4e/202610/com/Zeitraum#zeitraumid)</span> | zeitraumId | integer |
| <span className="hbs-g hbs-e0">[erforderlicheProdukte](/bo4e/202610/bo/TechnischeRessource#erforderlicheprodukte) <span className="hbs-liste">[ ]</span></span> | erforderlicheProdukte | [Produkt[]](/bo4e/202610/com/Produkt) |
| <span className="hbs-f hbs-e1">[produktCode](/bo4e/202610/com/Produkt#produktcode)</span> | produktCode | string |
| <span className="hbs-f hbs-e1">[codeProdukteigenschaft](/bo4e/202610/com/Produkt#codeprodukteigenschaft)</span> | codeProdukteigenschaft | string |
| <span className="hbs-f hbs-e1">[wertedetails](/bo4e/202610/com/Produkt#wertedetails)</span> | wertedetails | string |
| <span className="hbs-f hbs-e0">[fernsteuerbarkeit](/bo4e/202610/bo/TechnischeRessource#fernsteuerbarkeit)</span> | fernsteuerbarkeit | boolean |
| <span className="hbs-f hbs-e0">[verguetungsverpflichtung](/bo4e/202610/bo/TechnischeRessource#verguetungsverpflichtung)</span> | verguetungsverpflichtung | boolean |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### ressourcenId

32 Verwendung(en) in den Nachrichtentypen INVOIC, REQOTE, UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_31004](/schnittstellen/202610/pruefi/INVOIC/PI_31004) | Prüfi | INVOIC | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_31005](/schnittstellen/202610/pruefi/INVOIC/PI_31005) | Prüfi | INVOIC | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_31006](/schnittstellen/202610/pruefi/INVOIC/PI_31006) | Prüfi | INVOIC | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_31009](/schnittstellen/202610/pruefi/INVOIC/PI_31009) | Prüfi | INVOIC | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_31011](/schnittstellen/202610/pruefi/INVOIC/PI_31011) | Prüfi | INVOIC | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_35004](/schnittstellen/202610/pruefi/REQOTE/PI_35004) | Prüfi | REQOTE | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55002](/schnittstellen/202610/pruefi/UTILMD/PI_55002) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55013](/schnittstellen/202610/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55035](/schnittstellen/202610/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55052](/schnittstellen/202610/pruefi/UTILMD/PI_55052) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55060](/schnittstellen/202610/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55078](/schnittstellen/202610/pruefi/UTILMD/PI_55078) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55095](/schnittstellen/202610/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55173](/schnittstellen/202610/pruefi/UTILMD/PI_55173) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55175](/schnittstellen/202610/pruefi/UTILMD/PI_55175) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55177](/schnittstellen/202610/pruefi/UTILMD/PI_55177) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55180](/schnittstellen/202610/pruefi/UTILMD/PI_55180) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55600](/schnittstellen/202610/pruefi/UTILMD/PI_55600) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55601](/schnittstellen/202610/pruefi/UTILMD/PI_55601) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55602](/schnittstellen/202610/pruefi/UTILMD/PI_55602) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55603](/schnittstellen/202610/pruefi/UTILMD/PI_55603) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55607](/schnittstellen/202610/pruefi/UTILMD/PI_55607) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55617](/schnittstellen/202610/pruefi/UTILMD/PI_55617) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55623](/schnittstellen/202610/pruefi/UTILMD/PI_55623) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55629](/schnittstellen/202610/pruefi/UTILMD/PI_55629) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55635](/schnittstellen/202610/pruefi/UTILMD/PI_55635) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55690](/schnittstellen/202610/pruefi/UTILMD/PI_55690) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55693](/schnittstellen/202610/pruefi/UTILMD/PI_55693) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55694](/schnittstellen/202610/pruefi/UTILMD/PI_55694) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |

### referenzNetzlokation

10 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55035](/schnittstellen/202610/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55060](/schnittstellen/202610/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55095](/schnittstellen/202610/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55617](/schnittstellen/202610/pruefi/UTILMD/PI_55617) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55623](/schnittstellen/202610/pruefi/UTILMD/PI_55623) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55629](/schnittstellen/202610/pruefi/UTILMD/PI_55629) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55635](/schnittstellen/202610/pruefi/UTILMD/PI_55635) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |

### referenzSteuerbareRessource

10 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55035](/schnittstellen/202610/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55060](/schnittstellen/202610/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55095](/schnittstellen/202610/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55617](/schnittstellen/202610/pruefi/UTILMD/PI_55617) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55623](/schnittstellen/202610/pruefi/UTILMD/PI_55623) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55629](/schnittstellen/202610/pruefi/UTILMD/PI_55629) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55635](/schnittstellen/202610/pruefi/UTILMD/PI_55635) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |

### referenzTranche

8 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55060](/schnittstellen/202610/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55617](/schnittstellen/202610/pruefi/UTILMD/PI_55617) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55623](/schnittstellen/202610/pruefi/UTILMD/PI_55623) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55629](/schnittstellen/202610/pruefi/UTILMD/PI_55629) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55635](/schnittstellen/202610/pruefi/UTILMD/PI_55635) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |

### speicherkapazitaet

10 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55035](/schnittstellen/202610/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55060](/schnittstellen/202610/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55095](/schnittstellen/202610/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55617](/schnittstellen/202610/pruefi/UTILMD/PI_55617) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55623](/schnittstellen/202610/pruefi/UTILMD/PI_55623) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55629](/schnittstellen/202610/pruefi/UTILMD/PI_55629) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55635](/schnittstellen/202610/pruefi/UTILMD/PI_55635) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |

### verbrauchsart

9 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55035](/schnittstellen/202610/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55060](/schnittstellen/202610/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55617](/schnittstellen/202610/pruefi/UTILMD/PI_55617) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55623](/schnittstellen/202610/pruefi/UTILMD/PI_55623) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55629](/schnittstellen/202610/pruefi/UTILMD/PI_55629) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55635](/schnittstellen/202610/pruefi/UTILMD/PI_55635) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |

### waermenutzung

9 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55035](/schnittstellen/202610/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55060](/schnittstellen/202610/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55617](/schnittstellen/202610/pruefi/UTILMD/PI_55617) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55623](/schnittstellen/202610/pruefi/UTILMD/PI_55623) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55629](/schnittstellen/202610/pruefi/UTILMD/PI_55629) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55635](/schnittstellen/202610/pruefi/UTILMD/PI_55635) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |

### artEMobilitaet

9 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55035](/schnittstellen/202610/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55060](/schnittstellen/202610/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55617](/schnittstellen/202610/pruefi/UTILMD/PI_55617) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55623](/schnittstellen/202610/pruefi/UTILMD/PI_55623) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55629](/schnittstellen/202610/pruefi/UTILMD/PI_55629) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55635](/schnittstellen/202610/pruefi/UTILMD/PI_55635) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |

### erzeugungsart

9 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55060](/schnittstellen/202610/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55095](/schnittstellen/202610/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55617](/schnittstellen/202610/pruefi/UTILMD/PI_55617) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55623](/schnittstellen/202610/pruefi/UTILMD/PI_55623) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55629](/schnittstellen/202610/pruefi/UTILMD/PI_55629) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55635](/schnittstellen/202610/pruefi/UTILMD/PI_55635) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |

### speicherart

10 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55035](/schnittstellen/202610/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55060](/schnittstellen/202610/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55095](/schnittstellen/202610/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55617](/schnittstellen/202610/pruefi/UTILMD/PI_55617) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55623](/schnittstellen/202610/pruefi/UTILMD/PI_55623) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55629](/schnittstellen/202610/pruefi/UTILMD/PI_55629) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55635](/schnittstellen/202610/pruefi/UTILMD/PI_55635) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |

### enwg

9 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55035](/schnittstellen/202610/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55060](/schnittstellen/202610/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55617](/schnittstellen/202610/pruefi/UTILMD/PI_55617) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55623](/schnittstellen/202610/pruefi/UTILMD/PI_55623) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55629](/schnittstellen/202610/pruefi/UTILMD/PI_55629) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55635](/schnittstellen/202610/pruefi/UTILMD/PI_55635) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |

### inbetriebsetzungsdatum

3 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55035](/schnittstellen/202610/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55617](/schnittstellen/202610/pruefi/UTILMD/PI_55617) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55623](/schnittstellen/202610/pruefi/UTILMD/PI_55623) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |

### einordnung

3 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55035](/schnittstellen/202610/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55617](/schnittstellen/202610/pruefi/UTILMD/PI_55617) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55623](/schnittstellen/202610/pruefi/UTILMD/PI_55623) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |

### art

10 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55035](/schnittstellen/202610/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55060](/schnittstellen/202610/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55095](/schnittstellen/202610/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55617](/schnittstellen/202610/pruefi/UTILMD/PI_55617) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55623](/schnittstellen/202610/pruefi/UTILMD/PI_55623) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55629](/schnittstellen/202610/pruefi/UTILMD/PI_55629) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55635](/schnittstellen/202610/pruefi/UTILMD/PI_55635) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |

### datenqualitaet

6 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55617](/schnittstellen/202610/pruefi/UTILMD/PI_55617) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55623](/schnittstellen/202610/pruefi/UTILMD/PI_55623) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55629](/schnittstellen/202610/pruefi/UTILMD/PI_55629) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55635](/schnittstellen/202610/pruefi/UTILMD/PI_55635) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55693](/schnittstellen/202610/pruefi/UTILMD/PI_55693) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55694](/schnittstellen/202610/pruefi/UTILMD/PI_55694) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |

### fernsteuerbarkeit

2 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55693](/schnittstellen/202610/pruefi/UTILMD/PI_55693) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55694](/schnittstellen/202610/pruefi/UTILMD/PI_55694) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |

### verguetungsverpflichtung

2 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55617](/schnittstellen/202610/pruefi/UTILMD/PI_55617) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |
| [PI_55623](/schnittstellen/202610/pruefi/UTILMD/PI_55623) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
