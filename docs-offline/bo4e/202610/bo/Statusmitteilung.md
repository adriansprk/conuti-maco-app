# Statusmitteilung
<span hidden data-pagefind-meta={"title:Statusmitteilung — BO4E-Geschäftsobjekt (FV 202610)"} />

BO4E-Geschäftsobjekt · 6 Felder · 0 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="botyp"></a>`boTyp` <span className="hbs-pflicht">\*</span> | [Enum BOTyp](/bo4e/202610/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> | Typ des BO |
| <a id="versionstruktur"></a>`versionStruktur` <span className="hbs-pflicht">\*</span> | string | versionStruktur |
| <a id="statusobjekt"></a>`statusObjekt` | [Enum Statusobjekt](/bo4e/202610/enum/Statusobjekt)<br/><Werte>`MSBWECHSEL`, `UMBAUMELO`, `ERSTEINBAUIMS`, `ERSTEINBAUMME`, `GERAET`, `ANGEBOTANFRAGE`, `STATUSBESTELLUNG`, `LIEFERSCHEIN`, `SPERREN`, `ENTSPERREN`, `PRIVILEGIERUNG_NACH_ENFG`, `VERAENDERUNGSSTATUS_DER_DATEN`, `TURNUSAUSLESUNG`, `PRUEFSTATUS_ANTWORT_SUMMENZEITREIHEN`, `ABWEISUNG_SUMMENZEITREIHE`, `PRUEFSTATUS_SUMMENZEITREIHE`, `DATENSTATUS_SUMMENZEITREIHE`, `ABWEISUNG_STATUSMELDUNG_AENDERUNG`, `AUSFALLARBEIT`, `FAHRPLANANTEIL`, `GEGENVORSCHLAG_AUSFALLARBEIT`, `GEGENVORSCHLAG_FAHRPLANANTEIL`</Werte> | Statusobjekt |
| <a id="statusanlass"></a>`statusanlass` | [Enum Status](/bo4e/202610/enum/Status)<br/><Werte>`KUNDENSELBSTABLESUNG`, `LEERSTAND`, `REALER_ZAEHLERUEBERLAUF_GEPRUEFT`, `PLAUSIBEL_WG_KONTROLLABLESUNG`, `PLAUSIBEL_WG_KUNDENHINWEIS`, `AUSTAUSCH_DES_ERSATZWERTES`, `RECHENWERT`, `BASIS_MME`, `VERGLEICHSMESSUNG_GEEICHT`, `VERGLEICHSMESSUNG_NICHT_GEEICHT`, `MESSWERTNACHBILDUNG_AUS_GEEICHTEN_WERTEN`, `MESSWERTNACHBILDUNG_AUS_NICHT_GEEICHTEN_WERTEN`, `INTERPOLATION`, `HALTEWERT`, `BILANZIERUNG_NETZABSCHNITT`, `HISTORISCHE_MESSWERTE`, `STATISTISCHE_METHODE`, `AUFTEILUNG`, `VERWENDUNG_VON_WERTEN_DES_STOERMENGENZAEHLWERKS`, `UMGANGS_UND_KORREKTURMENGEN`, `ANGABEN_MESSLOKATION`, `KEIN_ZUGANG`, `KOMMUNIKATIONSSTOERUNG`, `NETZAUSFALL`, `SPANNUNGSAUSFALL`, `STATUS_GERAETEWECHSEL`, `KALIBRIERUNG`, `GERAET_ARBEITET_AUSSERHALB_DER_BETRIEBSBEDINGUNGEN`, `MESSEINRICHTUNG_GESTOERT_DEFEKT`, `UNSICHERHEIT_MESSUNG`, `BERUECKSICHTIGUNG_STOERMENGENZAEHLWERK`, `MENGENUMWERTUNG_VOLLSTAENDIG`, `UHRZEIT_GESTELLT_SYNCHRONISATION`, `MESSWERT_UNPLAUSIBEL`, `FALSCHER_WANDLERFAKTOR`, `FEHLERHAFTE_ABLESUNG`, `AENDERUNG_DER_BERECHNUNG`, `UMBAU_DER_MESSLOKATION`, `DATENBEARBEITUNGSFEHLER`, `BRENNWERTKORREKTUR`, `Z_ZAHL_KORREKTUR`, `STOERUNG_DEFEKT_MESSEINRICHTUNG`, `AENDERUNG_TARIFSCHALTZEITEN`, `TARIFSCHALTGERAET_DEFEKT`, `IMPULSWERTIGKEIT_NICHT_AUSREICHEND`, `ENERGIEMENGE_IN_UNGEMESSENEM_ZEITINTERVALL`, `ENERGIEMENGE_AUS_DEM_UNGEPAIRTEN_ZEITINTERVALL`, `WARTUNGSARBEITEN_AN_GEEICHTEM_MESSGERAET`, `GESTOERTE_WERTE`, `WARTUNGSARBEITEN_AN_EICHRECHTSKONFORMEN_MESSGERAETEN`, `KONSISTENZ_UND_SYNCHRONPRUEFUNG`, `GRUND_ANGABEN_MESSLOKATION`, `ANFORDERUNG_IN_DIE_VERGANGENHEIT_ZUM_ANGEFORDERTEN_ZEITPUNKT_LIEGT_KEIN_WERT_VOR`, `UMSTELLUNG_GASQUALITAET`, `ZAEHLERSTAND_ZUM_BEGINN_DER_ANGEGEBENEN_ENERGIEMENGE_VORHANDEN_UND_KOMMUNIZIERT`, `ZAEHLERSTAND_ZUM_ENDE_DER_ANGEGEBENEN_ENERGIEMENGE_VORHANDEN_UND_KOMMUNIZIERT`, `ZAEHLERSTAND_ZUM_BEGINN_DER_ANGEGEBENEN_ENERGIEMENGE_NICHT_VORHANDEN_DA_MENGENABGRENZUNG`, `ZAEHLERSTAND_ZUM_ENDE_DER_ANGEGEBENEN_ENERGIEMENGE_NICHT_VORHANDEN_DA_MENGENABGRENZUNG`, `GESCHEITERT`, `AUSGEBAUT`</Werte> | Status |
| <a id="auftragsstatus"></a>`auftragsstatus` | [Enum Auftragsstatus](/bo4e/202610/enum/Auftragsstatus)<br/><Werte>`GESCHEITERT`, `ERFOLGREICH`, `LIEFERUNG_GEPLANT`, `GEPLANT`, `ZUGESTIMMT`, `WIDERSPROCHEN`, `STOERUNGSFREI`, `GESTOERT`, `FESTGESTELLTE_STOERUNG`, `VERMUTETE_STOERUNG`, `ABGELEHNT`, `BEENDET`, `ANTWORT_DRITTER`, `BESTAETIGT`, `UMGESETZT`, `ENFG_STROMSPEICHER_UND_VERLUSTENERGIE`, `ENFG_ELEKTRISCH_ANGETRIEBENE_WAERMEPUMPEN`, `ENFG_UMLAGEERHEBUNG_BEI_ANLAGEN_ZUR_VERSTROMUNG_VON_KUPPELGASEN`, `ENFG_HERSTELLUNG_VON_GRUENEN_WASSERSTOFF`, `ENFG_STROMKOSTENINTENSIVE_UNTERNEHMEN`, `ENFG_HERSTELLUNG_VON_WASSERSTOFF_IN_STROMKOSTENINTENSIVEN_UNTERNEHMEN`, `ENFG_SCHIENENBAHNEN`, `ENFG_ELEKTRISCHE_BETRIEBENE_BUSSEN_IM_LINIENVERKEHR`, `ENFG_LANDSTROMANLAGEN`, `AENDERUNG_DER_DATEN`, `KEINE_AENDERUNG_DER_DATEN`, `ZEITREIHE_AKZEPTIERT`, `ZEITREIHE_NICHT_AKZEPTIERT`</Werte> | Auftragsstatus |
| <a id="positionsdaten"></a>`positionsdaten` | [StatusmitteilungPosition[]](/bo4e/202610/com/StatusmitteilungPosition) | positionsdaten |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[boTyp](/bo4e/202610/bo/Statusmitteilung#botyp) <span className="hbs-pflicht">\*</span></span> | Typ des BO | [Enum BOTyp](/bo4e/202610/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> |
| <span className="hbs-f hbs-e0">[versionStruktur](/bo4e/202610/bo/Statusmitteilung#versionstruktur) <span className="hbs-pflicht">\*</span></span> | versionStruktur | string |
| <span className="hbs-f hbs-e0">[statusObjekt](/bo4e/202610/bo/Statusmitteilung#statusobjekt)</span> | Statusobjekt | [Enum Statusobjekt](/bo4e/202610/enum/Statusobjekt)<br/><Werte>`MSBWECHSEL`, `UMBAUMELO`, `ERSTEINBAUIMS`, `ERSTEINBAUMME`, `GERAET`, `ANGEBOTANFRAGE`, `STATUSBESTELLUNG`, `LIEFERSCHEIN`, `SPERREN`, `ENTSPERREN`, `PRIVILEGIERUNG_NACH_ENFG`, `VERAENDERUNGSSTATUS_DER_DATEN`, `TURNUSAUSLESUNG`, `PRUEFSTATUS_ANTWORT_SUMMENZEITREIHEN`, `ABWEISUNG_SUMMENZEITREIHE`, `PRUEFSTATUS_SUMMENZEITREIHE`, `DATENSTATUS_SUMMENZEITREIHE`, `ABWEISUNG_STATUSMELDUNG_AENDERUNG`, `AUSFALLARBEIT`, `FAHRPLANANTEIL`, `GEGENVORSCHLAG_AUSFALLARBEIT`, `GEGENVORSCHLAG_FAHRPLANANTEIL`</Werte> |
| <span className="hbs-f hbs-e0">[statusanlass](/bo4e/202610/bo/Statusmitteilung#statusanlass)</span> | Status | [Enum Status](/bo4e/202610/enum/Status)<br/><Werte>`KUNDENSELBSTABLESUNG`, `LEERSTAND`, `REALER_ZAEHLERUEBERLAUF_GEPRUEFT`, `PLAUSIBEL_WG_KONTROLLABLESUNG`, `PLAUSIBEL_WG_KUNDENHINWEIS`, `AUSTAUSCH_DES_ERSATZWERTES`, `RECHENWERT`, `BASIS_MME`, `VERGLEICHSMESSUNG_GEEICHT`, `VERGLEICHSMESSUNG_NICHT_GEEICHT`, `MESSWERTNACHBILDUNG_AUS_GEEICHTEN_WERTEN`, `MESSWERTNACHBILDUNG_AUS_NICHT_GEEICHTEN_WERTEN`, `INTERPOLATION`, `HALTEWERT`, `BILANZIERUNG_NETZABSCHNITT`, `HISTORISCHE_MESSWERTE`, `STATISTISCHE_METHODE`, `AUFTEILUNG`, `VERWENDUNG_VON_WERTEN_DES_STOERMENGENZAEHLWERKS`, `UMGANGS_UND_KORREKTURMENGEN`, `ANGABEN_MESSLOKATION`, `KEIN_ZUGANG`, `KOMMUNIKATIONSSTOERUNG`, `NETZAUSFALL`, `SPANNUNGSAUSFALL`, `STATUS_GERAETEWECHSEL`, `KALIBRIERUNG`, `GERAET_ARBEITET_AUSSERHALB_DER_BETRIEBSBEDINGUNGEN`, `MESSEINRICHTUNG_GESTOERT_DEFEKT`, `UNSICHERHEIT_MESSUNG`, `BERUECKSICHTIGUNG_STOERMENGENZAEHLWERK`, `MENGENUMWERTUNG_VOLLSTAENDIG`, `UHRZEIT_GESTELLT_SYNCHRONISATION`, `MESSWERT_UNPLAUSIBEL`, `FALSCHER_WANDLERFAKTOR`, `FEHLERHAFTE_ABLESUNG`, `AENDERUNG_DER_BERECHNUNG`, `UMBAU_DER_MESSLOKATION`, `DATENBEARBEITUNGSFEHLER`, `BRENNWERTKORREKTUR`, `Z_ZAHL_KORREKTUR`, `STOERUNG_DEFEKT_MESSEINRICHTUNG`, `AENDERUNG_TARIFSCHALTZEITEN`, `TARIFSCHALTGERAET_DEFEKT`, `IMPULSWERTIGKEIT_NICHT_AUSREICHEND`, `ENERGIEMENGE_IN_UNGEMESSENEM_ZEITINTERVALL`, `ENERGIEMENGE_AUS_DEM_UNGEPAIRTEN_ZEITINTERVALL`, `WARTUNGSARBEITEN_AN_GEEICHTEM_MESSGERAET`, `GESTOERTE_WERTE`, `WARTUNGSARBEITEN_AN_EICHRECHTSKONFORMEN_MESSGERAETEN`, `KONSISTENZ_UND_SYNCHRONPRUEFUNG`, `GRUND_ANGABEN_MESSLOKATION`, `ANFORDERUNG_IN_DIE_VERGANGENHEIT_ZUM_ANGEFORDERTEN_ZEITPUNKT_LIEGT_KEIN_WERT_VOR`, `UMSTELLUNG_GASQUALITAET`, `ZAEHLERSTAND_ZUM_BEGINN_DER_ANGEGEBENEN_ENERGIEMENGE_VORHANDEN_UND_KOMMUNIZIERT`, `ZAEHLERSTAND_ZUM_ENDE_DER_ANGEGEBENEN_ENERGIEMENGE_VORHANDEN_UND_KOMMUNIZIERT`, `ZAEHLERSTAND_ZUM_BEGINN_DER_ANGEGEBENEN_ENERGIEMENGE_NICHT_VORHANDEN_DA_MENGENABGRENZUNG`, `ZAEHLERSTAND_ZUM_ENDE_DER_ANGEGEBENEN_ENERGIEMENGE_NICHT_VORHANDEN_DA_MENGENABGRENZUNG`, `GESCHEITERT`, `AUSGEBAUT`</Werte> |
| <span className="hbs-f hbs-e0">[auftragsstatus](/bo4e/202610/bo/Statusmitteilung#auftragsstatus)</span> | Auftragsstatus | [Enum Auftragsstatus](/bo4e/202610/enum/Auftragsstatus)<br/><Werte>`GESCHEITERT`, `ERFOLGREICH`, `LIEFERUNG_GEPLANT`, `GEPLANT`, `ZUGESTIMMT`, `WIDERSPROCHEN`, `STOERUNGSFREI`, `GESTOERT`, `FESTGESTELLTE_STOERUNG`, `VERMUTETE_STOERUNG`, `ABGELEHNT`, `BEENDET`, `ANTWORT_DRITTER`, `BESTAETIGT`, `UMGESETZT`, `ENFG_STROMSPEICHER_UND_VERLUSTENERGIE`, `ENFG_ELEKTRISCH_ANGETRIEBENE_WAERMEPUMPEN`, `ENFG_UMLAGEERHEBUNG_BEI_ANLAGEN_ZUR_VERSTROMUNG_VON_KUPPELGASEN`, `ENFG_HERSTELLUNG_VON_GRUENEN_WASSERSTOFF`, `ENFG_STROMKOSTENINTENSIVE_UNTERNEHMEN`, `ENFG_HERSTELLUNG_VON_WASSERSTOFF_IN_STROMKOSTENINTENSIVEN_UNTERNEHMEN`, `ENFG_SCHIENENBAHNEN`, `ENFG_ELEKTRISCHE_BETRIEBENE_BUSSEN_IM_LINIENVERKEHR`, `ENFG_LANDSTROMANLAGEN`, `AENDERUNG_DER_DATEN`, `KEINE_AENDERUNG_DER_DATEN`, `ZEITREIHE_AKZEPTIERT`, `ZEITREIHE_NICHT_AKZEPTIERT`</Werte> |
| <span className="hbs-g hbs-e0">[positionsdaten](/bo4e/202610/bo/Statusmitteilung#positionsdaten) <span className="hbs-liste">[ ]</span></span> | positionsdaten | [StatusmitteilungPosition[]](/bo4e/202610/com/StatusmitteilungPosition) |
| <span className="hbs-f hbs-e1">[positionsnummer](/bo4e/202610/com/StatusmitteilungPosition#positionsnummer)</span> | positionsnummer | integer |
| <span className="hbs-f hbs-e1">[bearbeitungsdatum](/bo4e/202610/com/StatusmitteilungPosition#bearbeitungsdatum)</span> | bearbeitungsdatum | string (date-time) |
| <span className="hbs-f hbs-e1">[verwendungAb](/bo4e/202610/com/StatusmitteilungPosition#verwendungab)</span> | verwendungAb | string (date-time) |
| <span className="hbs-f hbs-e1">[verwendungBis](/bo4e/202610/com/StatusmitteilungPosition#verwendungbis)</span> | verwendungBis | string (date-time) |
| <span className="hbs-f hbs-e1">[enddatum](/bo4e/202610/com/StatusmitteilungPosition#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-f hbs-e1">[auftragsstatus](/bo4e/202610/com/StatusmitteilungPosition#auftragsstatus)</span> | Auftragsstatus | [Enum Auftragsstatus](/bo4e/202610/enum/Auftragsstatus)<br/><Werte>`GESCHEITERT`, `ERFOLGREICH`, `LIEFERUNG_GEPLANT`, `GEPLANT`, `ZUGESTIMMT`, `WIDERSPROCHEN`, `STOERUNGSFREI`, `GESTOERT`, `FESTGESTELLTE_STOERUNG`, `VERMUTETE_STOERUNG`, `ABGELEHNT`, `BEENDET`, `ANTWORT_DRITTER`, `BESTAETIGT`, `UMGESETZT`, `ENFG_STROMSPEICHER_UND_VERLUSTENERGIE`, `ENFG_ELEKTRISCH_ANGETRIEBENE_WAERMEPUMPEN`, `ENFG_UMLAGEERHEBUNG_BEI_ANLAGEN_ZUR_VERSTROMUNG_VON_KUPPELGASEN`, `ENFG_HERSTELLUNG_VON_GRUENEN_WASSERSTOFF`, `ENFG_STROMKOSTENINTENSIVE_UNTERNEHMEN`, `ENFG_HERSTELLUNG_VON_WASSERSTOFF_IN_STROMKOSTENINTENSIVEN_UNTERNEHMEN`, `ENFG_SCHIENENBAHNEN`, `ENFG_ELEKTRISCHE_BETRIEBENE_BUSSEN_IM_LINIENVERKEHR`, `ENFG_LANDSTROMANLAGEN`, `AENDERUNG_DER_DATEN`, `KEINE_AENDERUNG_DER_DATEN`, `ZEITREIHE_AKZEPTIERT`, `ZEITREIHE_NICHT_AKZEPTIERT`</Werte> |
| <span className="hbs-f hbs-e1">[statusanlass](/bo4e/202610/com/StatusmitteilungPosition#statusanlass)</span> | Statusanlass | [Enum Statusanlass](/bo4e/202610/enum/Statusanlass)<br/><Werte>`KOMMUNIKATIONSSTOERUNG`, `STATUS_GERAETEWECHSEL`, `MESSEINRICHTUNG_GESTOERT_DEFEKT`, `KEINE_STOERUNG_FESTSTELLBAR`, `STOERUNGSBEHEBUNG_NICHT_MOEGLICH`, `REPARATUR_OHNE_GERAETEWECHSEL`</Werte> |
| <span className="hbs-f hbs-e1">[antwortstatus](/bo4e/202610/com/StatusmitteilungPosition#antwortstatus)</span> | antwortstatus | string |
| <span className="hbs-g hbs-e1">[fehlerbeschreibung](/bo4e/202610/com/StatusmitteilungPosition#fehlerbeschreibung)</span> | — | [Fehlerbeschreibung](/bo4e/202610/com/Fehlerbeschreibung) |
| <span className="hbs-f hbs-e2">[beschreibung1](/bo4e/202610/com/Fehlerbeschreibung#beschreibung1)</span> | Fehler Beschreibung Zeile 1 | string |
| <span className="hbs-f hbs-e2">[beschreibung2](/bo4e/202610/com/Fehlerbeschreibung#beschreibung2)</span> | Fehler Beschreibung Zeile 2 | string |
| <span className="hbs-f hbs-e2">[beschreibung3](/bo4e/202610/com/Fehlerbeschreibung#beschreibung3)</span> | Fehler Beschreibung Zeile 3 | string |
| <span className="hbs-f hbs-e2">[beschreibung4](/bo4e/202610/com/Fehlerbeschreibung#beschreibung4)</span> | Fehler Beschreibung Zeile 4 | string |
| <span className="hbs-f hbs-e2">[beschreibung5](/bo4e/202610/com/Fehlerbeschreibung#beschreibung5)</span> | Fehler Beschreibung Zeile 5 | string |
| <span className="hbs-f hbs-e1">[fehlerbeschreibungText](/bo4e/202610/com/StatusmitteilungPosition#fehlerbeschreibungtext)</span> | Fehlerbeschreibung | string |
| <span className="hbs-g hbs-e1">[begruendung](/bo4e/202610/com/StatusmitteilungPosition#begruendung)</span> | — | [Begruendung](/bo4e/202610/com/Begruendung) |
| <span className="hbs-f hbs-e2">[begruendung1](/bo4e/202610/com/Begruendung#begruendung1)</span> | Begruendung Zeile 1 | string |
| <span className="hbs-f hbs-e2">[begruendung2](/bo4e/202610/com/Begruendung#begruendung2)</span> | Begruendung Zeile 2 | string |
| <span className="hbs-f hbs-e2">[begruendung3](/bo4e/202610/com/Begruendung#begruendung3)</span> | Begruendung Zeile 3 | string |
| <span className="hbs-f hbs-e2">[begruendung4](/bo4e/202610/com/Begruendung#begruendung4)</span> | Begruendung Zeile 4 | string |
| <span className="hbs-f hbs-e2">[begruendung5](/bo4e/202610/com/Begruendung#begruendung5)</span> | Begruendung Zeile 5 | string |
| <span className="hbs-f hbs-e1">[begruendungText](/bo4e/202610/com/StatusmitteilungPosition#begruendungtext)</span> | Begruendung | string |
| <span className="hbs-f hbs-e1">[lokationsId](/bo4e/202610/com/StatusmitteilungPosition#lokationsid)</span> | lokationsId | string |
| <span className="hbs-f hbs-e1">[referenzMelo](/bo4e/202610/com/StatusmitteilungPosition#referenzmelo)</span> | referenzMelo | string |
| <span className="hbs-g hbs-e1">[allgemeineInformationen](/bo4e/202610/com/StatusmitteilungPosition#allgemeineinformationen)</span> | — | [AllgemeineInformationen](/bo4e/202610/com/AllgemeineInformationen) |
| <span className="hbs-f hbs-e2">[info1](/bo4e/202610/com/AllgemeineInformationen#info1)</span> | Allgemeine Info 1 | string |
| <span className="hbs-f hbs-e2">[info2](/bo4e/202610/com/AllgemeineInformationen#info2)</span> | Allgemeine Info 2 | string |
| <span className="hbs-f hbs-e2">[info3](/bo4e/202610/com/AllgemeineInformationen#info3)</span> | Allgemeine Info 3 | string |
| <span className="hbs-f hbs-e2">[info4](/bo4e/202610/com/AllgemeineInformationen#info4)</span> | Allgemeine Info 4 | string |
| <span className="hbs-f hbs-e2">[info5](/bo4e/202610/com/AllgemeineInformationen#info5)</span> | Allgemeine Info 5 | string |
| <span className="hbs-f hbs-e1">[allgemeineInformationenText](/bo4e/202610/com/StatusmitteilungPosition#allgemeineinformationentext)</span> | Allgemeine Informationen | string |
| <span className="hbs-f hbs-e1">[statusVeraenderungsZeitpunkt](/bo4e/202610/com/StatusmitteilungPosition#statusveraenderungszeitpunkt)</span> | statusVeraenderungsZeitpunkt | string (date-time) |
| <span className="hbs-f hbs-e1">[auftragsStatusListe](/bo4e/202610/com/StatusmitteilungPosition#auftragsstatusliste) <span className="hbs-liste">[ ]</span></span> | auftragsStatusListe | [Enum Auftragsstatus[]](/bo4e/202610/enum/Auftragsstatus)<br/><Werte>`GESCHEITERT`, `ERFOLGREICH`, `LIEFERUNG_GEPLANT`, `GEPLANT`, `ZUGESTIMMT`, `WIDERSPROCHEN`, `STOERUNGSFREI`, `GESTOERT`, `FESTGESTELLTE_STOERUNG`, `VERMUTETE_STOERUNG`, `ABGELEHNT`, `BEENDET`, `ANTWORT_DRITTER`, `BESTAETIGT`, `UMGESETZT`, `ENFG_STROMSPEICHER_UND_VERLUSTENERGIE`, `ENFG_ELEKTRISCH_ANGETRIEBENE_WAERMEPUMPEN`, `ENFG_UMLAGEERHEBUNG_BEI_ANLAGEN_ZUR_VERSTROMUNG_VON_KUPPELGASEN`, `ENFG_HERSTELLUNG_VON_GRUENEN_WASSERSTOFF`, `ENFG_STROMKOSTENINTENSIVE_UNTERNEHMEN`, `ENFG_HERSTELLUNG_VON_WASSERSTOFF_IN_STROMKOSTENINTENSIVEN_UNTERNEHMEN`, `ENFG_SCHIENENBAHNEN`, `ENFG_ELEKTRISCHE_BETRIEBENE_BUSSEN_IM_LINIENVERKEHR`, `ENFG_LANDSTROMANLAGEN`, `AENDERUNG_DER_DATEN`, `KEINE_AENDERUNG_DER_DATEN`, `ZEITREIHE_AKZEPTIERT`, `ZEITREIHE_NICHT_AKZEPTIERT`</Werte> |
| <span className="hbs-f hbs-e1">[lokationsTyp](/bo4e/202610/com/StatusmitteilungPosition#lokationstyp)</span> | Gibt an, ob es sich um eine Markt- oder Messlokation handelt | [Enum Lokationstyp](/bo4e/202610/enum/Lokationstyp)<br/><Werte>`MALO`, `MELO`, `NELO`, `TECHNISCHE_RESSOURCE`, `STEUERBARE_RESSOURCE`, `TRANCHE`, `MABIS_ZAEHLPUNKT`</Werte> |
| <span className="hbs-f hbs-e1">[statusObjekt](/bo4e/202610/com/StatusmitteilungPosition#statusobjekt)</span> | Statusobjekt | [Enum Statusobjekt](/bo4e/202610/enum/Statusobjekt)<br/><Werte>`MSBWECHSEL`, `UMBAUMELO`, `ERSTEINBAUIMS`, `ERSTEINBAUMME`, `GERAET`, `ANGEBOTANFRAGE`, `STATUSBESTELLUNG`, `LIEFERSCHEIN`, `SPERREN`, `ENTSPERREN`, `PRIVILEGIERUNG_NACH_ENFG`, `VERAENDERUNGSSTATUS_DER_DATEN`, `TURNUSAUSLESUNG`, `PRUEFSTATUS_ANTWORT_SUMMENZEITREIHEN`, `ABWEISUNG_SUMMENZEITREIHE`, `PRUEFSTATUS_SUMMENZEITREIHE`, `DATENSTATUS_SUMMENZEITREIHE`, `ABWEISUNG_STATUSMELDUNG_AENDERUNG`, `AUSFALLARBEIT`, `FAHRPLANANTEIL`, `GEGENVORSCHLAG_AUSFALLARBEIT`, `GEGENVORSCHLAG_FAHRPLANANTEIL`</Werte> |
| <span className="hbs-f hbs-e1">[antwortstatusCodeliste](/bo4e/202610/com/StatusmitteilungPosition#antwortstatuscodeliste)</span> | antwortstatusCodeliste | string |
| <span className="hbs-f hbs-e1">[vorgangsreferenznummer](/bo4e/202610/com/StatusmitteilungPosition#vorgangsreferenznummer)</span> | vorgangsreferenznummer | string |
| <span className="hbs-f hbs-e1">[mitteilungsnummer](/bo4e/202610/com/StatusmitteilungPosition#mitteilungsnummer)</span> | mitteilungsnummer | string |
| <span className="hbs-f hbs-e1">[anfragereferenznummer](/bo4e/202610/com/StatusmitteilungPosition#anfragereferenznummer)</span> | anfragereferenznummer | string |
| <span className="hbs-f hbs-e1">[fertigstellungsdatum](/bo4e/202610/com/StatusmitteilungPosition#fertigstellungsdatum)</span> | fertigstellungsdatum | string (date-time) |
| <span className="hbs-f hbs-e1">[lieferdatum](/bo4e/202610/com/StatusmitteilungPosition#lieferdatum)</span> | lieferdatum | string |
| <span className="hbs-f hbs-e1">[sendungsposition](/bo4e/202610/com/StatusmitteilungPosition#sendungsposition)</span> | sendungsposition | integer |
| <span className="hbs-f hbs-e1">[gueltigAb](/bo4e/202610/com/StatusmitteilungPosition#gueltigab)</span> | gueltigAb | string (date-time) |
| <span className="hbs-f hbs-e1">[referenzMalo](/bo4e/202610/com/StatusmitteilungPosition#referenzmalo)</span> | referenzMalo | string |
| <span className="hbs-f hbs-e1">[referenzPreisschluesselstamm](/bo4e/202610/com/StatusmitteilungPosition#referenzpreisschluesselstamm)</span> | referenzPreisschluesselstamm | string |
| <span className="hbs-f hbs-e1">[referenzArtikelID](/bo4e/202610/com/StatusmitteilungPosition#referenzartikelid)</span> | referenzArtikelID | string |
| <span className="hbs-f hbs-e1">[startdatum](/bo4e/202610/com/StatusmitteilungPosition#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e1">[angebotsnummer](/bo4e/202610/com/StatusmitteilungPosition#angebotsnummer)</span> | angebotsnummer | string |
| <span className="hbs-f hbs-e1">[anfrageReferenz](/bo4e/202610/com/StatusmitteilungPosition#anfragereferenz)</span> | anfrageReferenz | string |
| <span className="hbs-f hbs-e1">[vertragsende](/bo4e/202610/com/StatusmitteilungPosition#vertragsende)</span> | vertragsende | string (date-time) |
| <span className="hbs-f hbs-e1">[laufendeNummer](/bo4e/202610/com/StatusmitteilungPosition#laufendenummer)</span> | Laufende Nummer | integer |
| <span className="hbs-f hbs-e1">[dokumentenreferenznummer](/bo4e/202610/com/StatusmitteilungPosition#dokumentenreferenznummer)</span> | Dokumentenreferenznummer | string |
| <span className="hbs-g hbs-e1">[ansichtSender](/bo4e/202610/com/StatusmitteilungPosition#ansichtsender) <span className="hbs-liste">[ ]</span></span> | ansichtSender | [AnsichtSender[]](/bo4e/202610/com/AnsichtSender) |
| <span className="hbs-f hbs-e2">[verwendungAb](/bo4e/202610/com/AnsichtSender#verwendungab)</span> | verwendungAb | string (date-time) |
| <span className="hbs-f hbs-e2">[verwendungBis](/bo4e/202610/com/AnsichtSender#verwendungbis)</span> | verwendungBis | string (date-time) |
| <span className="hbs-f hbs-e2">[leistungsperiode](/bo4e/202610/com/AnsichtSender#leistungsperiode)</span> | leistungsperiode | string |
| <span className="hbs-g hbs-e2">[menge](/bo4e/202610/com/AnsichtSender#menge)</span> | — | [Menge](/bo4e/202610/com/Menge) |
| <span className="hbs-f hbs-e3">[wert](/bo4e/202610/com/Menge#wert)</span> | Wert | number (float) |
| <span className="hbs-f hbs-e3">[einheit](/bo4e/202610/com/Menge#einheit)</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202610/enum/Mengeneinheit)<br/><Werte>`W`, `WH`, `KW`, `KWH`, `KVARH`, `MW`, `MWH`, `STUECK`, `KUBIKMETER`, `STUNDE`, `TAG`, `MONAT`, `JAHR`, `PROZENT`, `ANZAHL`, `VAR`, `KVAR`, `VARH`, `KWHK`, `Z16`, `KWT`, `WATT_PRO_QUADRATMETER`, `METER_PRO_SEKUNDE`</Werte> |
| <span className="hbs-f hbs-e3">[startdatum](/bo4e/202610/com/Menge#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e3">[enddatum](/bo4e/202610/com/Menge#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-f hbs-e2">[tarifstufe](/bo4e/202610/com/AnsichtSender#tarifstufe)</span> | Tarifstufe | [Enum Tarifstufe](/bo4e/202610/enum/Tarifstufe)<br/><Werte>`TARIFSTUFE_0`, `TARIFSTUFE_1`, `TARIFSTUFE_2`, `TARIFSTUFE_3`, `TARIFSTUFE_4`, `TARIFSTUFE_5`, `TARIFSTUFE_6`, `TARIFSTUFE_7`, `TARIFSTUFE_8`, `TARIFSTUFE_9`</Werte> |
| <span className="hbs-f hbs-e1">[gueltigkeitsZeitspanne](/bo4e/202610/com/StatusmitteilungPosition#gueltigkeitszeitspanne)</span> | gueltigkeitsZeitspanne | string |
| <span className="hbs-g hbs-e1">[privilegierteEnergiemenge](/bo4e/202610/com/StatusmitteilungPosition#privilegierteenergiemenge)</span> | — | [ZeitintervallMenge](/bo4e/202610/com/ZeitintervallMenge) |
| <span className="hbs-f hbs-e2">[verwendungAb](/bo4e/202610/com/ZeitintervallMenge#verwendungab)</span> | verwendungAb | string (date-time) |
| <span className="hbs-f hbs-e2">[verwendungBis](/bo4e/202610/com/ZeitintervallMenge#verwendungbis)</span> | verwendungBis | string (date-time) |
| <span className="hbs-g hbs-e2">[menge](/bo4e/202610/com/ZeitintervallMenge#menge)</span> | — | [Menge](/bo4e/202610/com/Menge) |
| <span className="hbs-f hbs-e3">[wert](/bo4e/202610/com/Menge#wert)</span> | Wert | number (float) |
| <span className="hbs-f hbs-e3">[einheit](/bo4e/202610/com/Menge#einheit)</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202610/enum/Mengeneinheit)<br/><Werte>`W`, `WH`, `KW`, `KWH`, `KVARH`, `MW`, `MWH`, `STUECK`, `KUBIKMETER`, `STUNDE`, `TAG`, `MONAT`, `JAHR`, `PROZENT`, `ANZAHL`, `VAR`, `KVAR`, `VARH`, `KWHK`, `Z16`, `KWT`, `WATT_PRO_QUADRATMETER`, `METER_PRO_SEKUNDE`</Werte> |
| <span className="hbs-f hbs-e3">[startdatum](/bo4e/202610/com/Menge#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e3">[enddatum](/bo4e/202610/com/Menge#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-g hbs-e1">[ansprechpartner](/bo4e/202610/com/StatusmitteilungPosition#ansprechpartner)</span> | Ansprechpartner | [Ansprechpartner](/bo4e/202610/bo/Ansprechpartner) |
| <span className="hbs-f hbs-e2">[boTyp](/bo4e/202610/bo/Ansprechpartner#botyp) <span className="hbs-pflicht">\*</span></span> | Typ des BO | [Enum BOTyp](/bo4e/202610/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> |
| <span className="hbs-f hbs-e2">[versionStruktur](/bo4e/202610/bo/Ansprechpartner#versionstruktur) <span className="hbs-pflicht">\*</span></span> | versionStruktur | string |
| <span className="hbs-f hbs-e2">[nachname](/bo4e/202610/bo/Ansprechpartner#nachname)</span> | Nachname (Familienname) des Ansprechpartners | string |
| <span className="hbs-f hbs-e2">[eMailAdresse](/bo4e/202610/bo/Ansprechpartner#emailadresse)</span> | E-Mail Adresse | string |
| <span className="hbs-g hbs-e2">[rufnummern](/bo4e/202610/bo/Ansprechpartner#rufnummern) <span className="hbs-liste">[ ]</span></span> | Liste der Telefonnummern, unter denen der Ansprechpartner erreichbar ist. | [Rufnummer[]](/bo4e/202610/com/Rufnummer) |
| <span className="hbs-f hbs-e3">[nummerntyp](/bo4e/202610/com/Rufnummer#nummerntyp)</span> | Rufnummernart | [Enum Rufnummernart](/bo4e/202610/enum/Rufnummernart)<br/><Werte>`RUF_ZENTRALE`, `FAX_ZENTRALE`, `SAMMELRUF`, `SAMMELFAX`, `ABTEILUNGRUF`, `ABTEILUNGFAX`, `RUF_DURCHWAHL`, `FAX_DURCHWAHL`, `MOBIL_NUMMER`</Werte> |
| <span className="hbs-f hbs-e3">[rufnummer](/bo4e/202610/com/Rufnummer#rufnummer)</span> | rufnummer | string |

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
