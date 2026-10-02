# Vertrag
<span hidden data-pagefind-meta={"title:Vertrag — BO4E-Geschäftsobjekt (FV 202610)"} />

BO4E-Geschäftsobjekt · 20 Felder · 151 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="botyp"></a>`boTyp` <span className="hbs-pflicht">\*</span> | [Enum BOTyp](/bo4e/202610/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> | Typ des BO |
| <a id="versionstruktur"></a>`versionStruktur` <span className="hbs-pflicht">\*</span> | string | obligatory version of the BO4E definition. Currently hard coded to 1 |
| <a id="sparte"></a>`sparte` | [Enum Sparte](/bo4e/202610/enum/Sparte)<br/><Werte>`STROM`, `GAS`, `FERNWAERME`, `NAHWAERME`, `WASSER`, `ABWASSER`</Werte> | Unterscheidungsmöglichkeiten für die Sparte. Siehe ENUM Sparte |
| <a id="vertragsart"></a>`vertragsart` | string | Hier ist festgelegt, um welche Art von Vertrag es sich handelt. Z.B. Netznutzungvertrag. Details siehe ENUM Vertragsart |
| <a id="vertragsnummer"></a>`vertragsnummer` | string | Eine im Verwendungskontext eindeutige Nummer für den Vertrag |
| <a id="beschreibung"></a>`beschreibung` | string | Freitext zur Beschreibung der Konditionen, z.B. "Standardkonditionen Gas" |
| <a id="lokationsid"></a>`lokationsId` | string | lokationsId |
| <a id="lokationstyp"></a>`lokationsTyp` | [Enum Lokationstyp](/bo4e/202610/enum/Lokationstyp)<br/><Werte>`MALO`, `MELO`, `NELO`, `TECHNISCHE_RESSOURCE`, `STEUERBARE_RESSOURCE`, `TRANCHE`, `MABIS_ZAEHLPUNKT`</Werte> | Gibt an, ob es sich um eine Markt- oder Messlokation handelt |
| <a id="vertragsstatus"></a>`vertragsstatus` | [Enum Vertragstatus](/bo4e/202610/enum/Vertragstatus)<br/><Werte>`IN_ARBEIT`, `UEBERMITTELT`, `ANGENOMMEN`, `AKTIV`, `ABGELEHNT`, `WIDERRUFEN`, `STORNIERT`, `GEKUENDIGT`, `BEENDET`</Werte> | Vertragstatus |
| <a id="vertragsbeginn"></a>`vertragsbeginn` | string (date-time) | Gibt an, wann der Vertrag beginnt. |
| <a id="vertragsende"></a>`vertragsende` | string (date-time) | Gibt an, wann der Vertrag (voraussichtlich) endet oder beendet wurde. |
| <a id="gemeinderabatt"></a>`gemeinderabatt` | integer | gemeinderabatt für EDIFACT mapping. |
| <a id="vertragskonditionen"></a>`vertragskonditionen` | [Vertragskonditionen](/bo4e/202610/com/Vertragskonditionen) | Festlegungen zu Laufzeiten und Kündigungsfristen. Details siehe COM Vertragskonditionen |
| <a id="korrespondenzpartner"></a>`korrespondenzpartner` | [Geschaeftspartner](/bo4e/202610/bo/Geschaeftspartner) | korrespondenzpartner für EDIFACT mapping |
| <a id="abrechnunguebernna"></a>`abrechnungUeberNna` | boolean | abrechnungUeberNna |
| <a id="datenqualitaet"></a>`datenqualitaet` | [Enum Datenqualitaet](/bo4e/202610/enum/Datenqualitaet)<br/><Werte>`ERWARTETE_DATEN`, `IM_SYSTEM_VORHANDENE_DATEN`, `INFORMATIVE_DATEN`, `GUELTIGE_DATEN`, `KEINE_DATEN`, `IM_SYSTEM_KEINE_DATEN_VORHANDEN`, `KEINE_DATEN_ERWARTET`, `DIFFERENZ_DATEN`, `DIFFERENZ_ERWARTETE_DATEN`, `DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</Werte> | Datenqualitaet |
| <a id="gueltigkeitszeitraum"></a>`gueltigkeitszeitraum` | [Zeitraum](/bo4e/202610/com/Zeitraum) | — |
| <a id="vertragspartner1"></a>`vertragspartner1` | [Geschaeftspartner[]](/bo4e/202610/bo/Geschaeftspartner) | Der "erstgenannte" Vertragspartner. In der Regel der Aussteller des Vertrags. Beispiel: "Vertrag zwischen Vertagspartner 1 ..." Siehe BO Geschaeftspartner |
| <a id="vertragspartner2"></a>`vertragspartner2` | [Geschaeftspartner[]](/bo4e/202610/bo/Geschaeftspartner) | Der "zweitgenannte" Vertragspartner. In der Regel der Empfänger des Vertrags. Beispiel "Vertrag zwischen Vertagspartner 1 und Vertragspartner 2". Siehe BO Geschaeftspartner |
| <a id="enfg"></a>`enFG` | [EnFG[]](/bo4e/202610/com/EnFG) | enFG |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[boTyp](/bo4e/202610/bo/Vertrag#botyp) <span className="hbs-pflicht">\*</span></span> | Typ des BO | [Enum BOTyp](/bo4e/202610/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> |
| <span className="hbs-f hbs-e0">[versionStruktur](/bo4e/202610/bo/Vertrag#versionstruktur) <span className="hbs-pflicht">\*</span></span> | obligatory version of the BO4E definition. Currently hard coded to 1 | string |
| <span className="hbs-f hbs-e0">[sparte](/bo4e/202610/bo/Vertrag#sparte)</span> | Unterscheidungsmöglichkeiten für die Sparte. Siehe ENUM Sparte | [Enum Sparte](/bo4e/202610/enum/Sparte)<br/><Werte>`STROM`, `GAS`, `FERNWAERME`, `NAHWAERME`, `WASSER`, `ABWASSER`</Werte> |
| <span className="hbs-f hbs-e0">[vertragsart](/bo4e/202610/bo/Vertrag#vertragsart)</span> | Hier ist festgelegt, um welche Art von Vertrag es sich handelt. Z.B. Netznutzungvertrag. Details siehe ENUM<br/>Vertragsart | string |
| <span className="hbs-f hbs-e0">[vertragsnummer](/bo4e/202610/bo/Vertrag#vertragsnummer)</span> | Eine im Verwendungskontext eindeutige Nummer für den Vertrag | string |
| <span className="hbs-f hbs-e0">[beschreibung](/bo4e/202610/bo/Vertrag#beschreibung)</span> | Freitext zur Beschreibung der Konditionen, z.B. "Standardkonditionen Gas" | string |
| <span className="hbs-f hbs-e0">[lokationsId](/bo4e/202610/bo/Vertrag#lokationsid)</span> | lokationsId | string |
| <span className="hbs-f hbs-e0">[lokationsTyp](/bo4e/202610/bo/Vertrag#lokationstyp)</span> | Gibt an, ob es sich um eine Markt- oder Messlokation handelt | [Enum Lokationstyp](/bo4e/202610/enum/Lokationstyp)<br/><Werte>`MALO`, `MELO`, `NELO`, `TECHNISCHE_RESSOURCE`, `STEUERBARE_RESSOURCE`, `TRANCHE`, `MABIS_ZAEHLPUNKT`</Werte> |
| <span className="hbs-f hbs-e0">[vertragsstatus](/bo4e/202610/bo/Vertrag#vertragsstatus)</span> | Vertragstatus | [Enum Vertragstatus](/bo4e/202610/enum/Vertragstatus)<br/><Werte>`IN_ARBEIT`, `UEBERMITTELT`, `ANGENOMMEN`, `AKTIV`, `ABGELEHNT`, `WIDERRUFEN`, `STORNIERT`, `GEKUENDIGT`, `BEENDET`</Werte> |
| <span className="hbs-f hbs-e0">[vertragsbeginn](/bo4e/202610/bo/Vertrag#vertragsbeginn)</span> | Gibt an, wann der Vertrag beginnt. | string (date-time) |
| <span className="hbs-f hbs-e0">[vertragsende](/bo4e/202610/bo/Vertrag#vertragsende)</span> | Gibt an, wann der Vertrag (voraussichtlich) endet oder beendet wurde. | string (date-time) |
| <span className="hbs-f hbs-e0">[gemeinderabatt](/bo4e/202610/bo/Vertrag#gemeinderabatt)</span> | gemeinderabatt für EDIFACT mapping. | integer |
| <span className="hbs-g hbs-e0">[vertragskonditionen](/bo4e/202610/bo/Vertrag#vertragskonditionen)</span> | Festlegungen zu Laufzeiten und Kündigungsfristen. Details siehe COM Vertragskonditionen | [Vertragskonditionen](/bo4e/202610/com/Vertragskonditionen) |
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
| <span className="hbs-g hbs-e0">[korrespondenzpartner](/bo4e/202610/bo/Vertrag#korrespondenzpartner)</span> | korrespondenzpartner für EDIFACT mapping | [Geschaeftspartner](/bo4e/202610/bo/Geschaeftspartner) |
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
| <span className="hbs-f hbs-e0">[abrechnungUeberNna](/bo4e/202610/bo/Vertrag#abrechnunguebernna)</span> | abrechnungUeberNna | boolean |
| <span className="hbs-f hbs-e0">[datenqualitaet](/bo4e/202610/bo/Vertrag#datenqualitaet)</span> | Datenqualitaet | [Enum Datenqualitaet](/bo4e/202610/enum/Datenqualitaet)<br/><Werte>`ERWARTETE_DATEN`, `IM_SYSTEM_VORHANDENE_DATEN`, `INFORMATIVE_DATEN`, `GUELTIGE_DATEN`, `KEINE_DATEN`, `IM_SYSTEM_KEINE_DATEN_VORHANDEN`, `KEINE_DATEN_ERWARTET`, `DIFFERENZ_DATEN`, `DIFFERENZ_ERWARTETE_DATEN`, `DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</Werte> |
| <span className="hbs-g hbs-e0">[gueltigkeitszeitraum](/bo4e/202610/bo/Vertrag#gueltigkeitszeitraum)</span> | — | [Zeitraum](/bo4e/202610/com/Zeitraum) |
| <span className="hbs-f hbs-e1">[zeiteinheit](/bo4e/202610/com/Zeitraum#zeiteinheit)</span> | Zeiteinheit | [Enum Zeiteinheit](/bo4e/202610/enum/Zeiteinheit)<br/><Werte>`SEKUNDE`, `MINUTE`, `STUNDE`, `VIERTEL_STUNDE`, `TAG`, `WOCHE`, `MONAT`, `QUARTAL`, `HALBJAHR`, `JAHR`</Werte> |
| <span className="hbs-f hbs-e1">[dauer](/bo4e/202610/com/Zeitraum#dauer)</span> | dauer | integer |
| <span className="hbs-f hbs-e1">[startdatum](/bo4e/202610/com/Zeitraum#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e1">[enddatum](/bo4e/202610/com/Zeitraum#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-f hbs-e1">[einheit](/bo4e/202610/com/Zeitraum#einheit)</span> | Zeiteinheit | [Enum Zeiteinheit](/bo4e/202610/enum/Zeiteinheit)<br/><Werte>`SEKUNDE`, `MINUTE`, `STUNDE`, `VIERTEL_STUNDE`, `TAG`, `WOCHE`, `MONAT`, `QUARTAL`, `HALBJAHR`, `JAHR`</Werte> |
| <span className="hbs-f hbs-e1">[ableseZeitraum](/bo4e/202610/com/Zeitraum#ablesezeitraum)</span> | ableseZeitraum | string |
| <span className="hbs-f hbs-e1">[abrechnungsZeitraum](/bo4e/202610/com/Zeitraum#abrechnungszeitraum)</span> | abrechnungsZeitraum | string |
| <span className="hbs-f hbs-e1">[zeitraumText](/bo4e/202610/com/Zeitraum#zeitraumtext)</span> | zeitraumText | string |
| <span className="hbs-f hbs-e1">[zeitraumId](/bo4e/202610/com/Zeitraum#zeitraumid)</span> | zeitraumId | integer |
| <span className="hbs-g hbs-e0">[vertragspartner1](/bo4e/202610/bo/Vertrag#vertragspartner1) <span className="hbs-liste">[ ]</span></span> | Der "erstgenannte" Vertragspartner. In der Regel der Aussteller des Vertrags. Beispiel: "Vertrag zwischen<br/>Vertagspartner 1 ..." Siehe BO Geschaeftspartner | [Geschaeftspartner[]](/bo4e/202610/bo/Geschaeftspartner) |
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
| <span className="hbs-g hbs-e0">[vertragspartner2](/bo4e/202610/bo/Vertrag#vertragspartner2) <span className="hbs-liste">[ ]</span></span> | Der "zweitgenannte" Vertragspartner. In der Regel der Empfänger des Vertrags. Beispiel "Vertrag zwischen<br/>Vertagspartner 1 und Vertragspartner 2". Siehe BO Geschaeftspartner | [Geschaeftspartner[]](/bo4e/202610/bo/Geschaeftspartner) |
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
| <span className="hbs-g hbs-e0">[enFG](/bo4e/202610/bo/Vertrag#enfg) <span className="hbs-liste">[ ]</span></span> | enFG | [EnFG[]](/bo4e/202610/com/EnFG) |
| <span className="hbs-f hbs-e1">[grundlageVerringerungUmlagen](/bo4e/202610/com/EnFG#grundlageverringerungumlagen)</span> | GrundlageVerringerungUmlagen | [Enum GrundlageVerringerungUmlagen](/bo4e/202610/enum/GrundlageVerringerungUmlagen)<br/><Werte>`ERFUELLT_VORAUSSETZUNG_NACH_ENFG`, `ERFUELLT_NICHT_VORAUSSETZUNG_NACH_ENFG`, `KEINE_ANGABE`</Werte> |
| <span className="hbs-f hbs-e1">[grund](/bo4e/202610/com/EnFG#grund) <span className="hbs-liste">[ ]</span></span> | Grund der Umlagenverringerung | [Enum GrundlageVerringerungUmlagenGrund[]](/bo4e/202610/enum/GrundlageVerringerungUmlagenGrund)<br/><Werte>`ENFG_STROMSPEICHER_UND_VERLUSTENERGIE`, `ENFG_ELEKTRISCH_ANGETRIEBENE_WAERMEPUMPEN`, `ENFG_UMLAGEERHEBUNG_BEI_ANLAGEN_ZUR_VERSTROMUNG_VON_KUPPELGASEN`, `ENFG_HERSTELLUNG_VON_GRUENEN_WASSERSTOFF`, `ENFG_STROMKOSTENINTENSIVE_UNTERNEHMEN`, `ENFG_HERSTELLUNG_VON_WASSERSTOFF_IN_STROMKOSTENINTENSIVEN_UNTERNEHMEN`, `ENFG_SCHIENENBAHNEN`, `ENFG_ELEKTRISCHE_BETRIEBENE_BUSSEN_IM_LINIENVERKEHR`, `ENFG_LANDSTROMANLAGEN`</Werte> |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### lokationsId

12 Verwendung(en) in den Nachrichtentypen UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_44043](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44043) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG |
| [PI_44060](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44060) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG |
| [PI_44113](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44113) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG |
| [PI_44142](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44142) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG |
| [PI_44168](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG |

### lokationsTyp

8 Verwendung(en) in den Nachrichtentypen UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_44043](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44043) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG |
| [PI_44060](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44060) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG |
| [PI_44113](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44113) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG |
| [PI_44142](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44142) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG |
| [PI_44168](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG |

### vertragsbeginn

65 Verwendung(en) in den Nachrichtentypen UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_44001](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44001) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44002](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44004](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44004) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44005](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44005) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44013](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44014](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44019](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44019) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44020](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44020) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44021](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44021) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44038](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44038) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44052](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44052) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44101](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44101) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44102](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44102) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44103](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44103) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44104](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44104) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44109](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44109) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44112](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44112) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44113](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44113) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44116](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44116) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44117](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44117) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44120](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44120) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44123](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44123) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44137](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44137) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44138](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44138) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44139](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44139) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44140](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44140) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44142](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44142) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44143](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44143) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44145](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44145) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44147](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44147) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44148](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44148) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44149](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44149) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44150](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44150) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44151](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44151) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44156](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44156) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44157](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44157) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44159](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44159) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44160](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44160) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44162](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44162) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44163](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44163) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44165](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44165) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44166](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44166) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44167](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44167) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44175](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44175) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44176](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44176) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44180](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44180) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44181](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44181) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_55001](/schnittstellen/202610/pruefi/UTILMD/PI_55001) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_55002](/schnittstellen/202610/pruefi/UTILMD/PI_55002) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_55004](/schnittstellen/202610/pruefi/UTILMD/PI_55004) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_55005](/schnittstellen/202610/pruefi/UTILMD/PI_55005) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_55013](/schnittstellen/202610/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_55014](/schnittstellen/202610/pruefi/UTILMD/PI_55014) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_55038](/schnittstellen/202610/pruefi/UTILMD/PI_55038) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_55051](/schnittstellen/202610/pruefi/UTILMD/PI_55051) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_55052](/schnittstellen/202610/pruefi/UTILMD/PI_55052) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_55077](/schnittstellen/202610/pruefi/UTILMD/PI_55077) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_55078](/schnittstellen/202610/pruefi/UTILMD/PI_55078) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_55600](/schnittstellen/202610/pruefi/UTILMD/PI_55600) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_55601](/schnittstellen/202610/pruefi/UTILMD/PI_55601) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_55602](/schnittstellen/202610/pruefi/UTILMD/PI_55602) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_55603](/schnittstellen/202610/pruefi/UTILMD/PI_55603) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_55607](/schnittstellen/202610/pruefi/UTILMD/PI_55607) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_55608](/schnittstellen/202610/pruefi/UTILMD/PI_55608) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_55611](/schnittstellen/202610/pruefi/UTILMD/PI_55611) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG |

### vertragsende

46 Verwendung(en) in den Nachrichtentypen UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_44001](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44001) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44002](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44004](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44004) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44005](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44005) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44007](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44007) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44008](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44008) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44010](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44010) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44011](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44011) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44013](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44014](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44016](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44016) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44017](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44017) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44019](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44019) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44020](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44020) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44021](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44021) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44037](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44037) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44039](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44039) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44040](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44040) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44052](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44052) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44101](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44101) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44102](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44102) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44103](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44103) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44104](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44104) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44183](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44183) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_55001](/schnittstellen/202610/pruefi/UTILMD/PI_55001) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_55002](/schnittstellen/202610/pruefi/UTILMD/PI_55002) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_55004](/schnittstellen/202610/pruefi/UTILMD/PI_55004) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_55005](/schnittstellen/202610/pruefi/UTILMD/PI_55005) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_55007](/schnittstellen/202610/pruefi/UTILMD/PI_55007) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_55008](/schnittstellen/202610/pruefi/UTILMD/PI_55008) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_55010](/schnittstellen/202610/pruefi/UTILMD/PI_55010) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_55011](/schnittstellen/202610/pruefi/UTILMD/PI_55011) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_55013](/schnittstellen/202610/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_55014](/schnittstellen/202610/pruefi/UTILMD/PI_55014) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_55016](/schnittstellen/202610/pruefi/UTILMD/PI_55016) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_55017](/schnittstellen/202610/pruefi/UTILMD/PI_55017) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_55037](/schnittstellen/202610/pruefi/UTILMD/PI_55037) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_55039](/schnittstellen/202610/pruefi/UTILMD/PI_55039) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_55040](/schnittstellen/202610/pruefi/UTILMD/PI_55040) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_55051](/schnittstellen/202610/pruefi/UTILMD/PI_55051) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_55052](/schnittstellen/202610/pruefi/UTILMD/PI_55052) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_55600](/schnittstellen/202610/pruefi/UTILMD/PI_55600) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_55602](/schnittstellen/202610/pruefi/UTILMD/PI_55602) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_55607](/schnittstellen/202610/pruefi/UTILMD/PI_55607) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_55608](/schnittstellen/202610/pruefi/UTILMD/PI_55608) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_55611](/schnittstellen/202610/pruefi/UTILMD/PI_55611) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG |

### gemeinderabatt

8 Verwendung(en) in den Nachrichtentypen UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_44001](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44001) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44002](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44013](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44014](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44035](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44035) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44112](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44112) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44139](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44139) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_44142](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44142) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG |

### datenqualitaet

12 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55109](/schnittstellen/202610/pruefi/UTILMD/PI_55109) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG |
| [PI_55110](/schnittstellen/202610/pruefi/UTILMD/PI_55110) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG |
| [PI_55136](/schnittstellen/202610/pruefi/UTILMD/PI_55136) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG |
| [PI_55137](/schnittstellen/202610/pruefi/UTILMD/PI_55137) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG |
| [PI_55616](/schnittstellen/202610/pruefi/UTILMD/PI_55616) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_55622](/schnittstellen/202610/pruefi/UTILMD/PI_55622) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_55628](/schnittstellen/202610/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_55634](/schnittstellen/202610/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG |
| [PI_55643](/schnittstellen/202610/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG |
| [PI_55648](/schnittstellen/202610/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG |
| [PI_55663](/schnittstellen/202610/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG |
| [PI_55669](/schnittstellen/202610/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
