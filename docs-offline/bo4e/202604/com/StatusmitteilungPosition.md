# StatusmitteilungPosition
<span hidden data-pagefind-meta={"title:StatusmitteilungPosition — BO4E-Komponente (FV 202604)"} />

BO4E-Komponente · 41 Felder · 76 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="positionsnummer"></a>`positionsnummer` | integer | positionsnummer |
| <a id="bearbeitungsdatum"></a>`bearbeitungsdatum` | string (date-time) | bearbeitungsdatum |
| <a id="verwendungab"></a>`verwendungAb` | string (date-time) | verwendungAb |
| <a id="verwendungbis"></a>`verwendungBis` | string (date-time) | verwendungBis |
| <a id="enddatum"></a>`enddatum` | string (date-time) | enddatum |
| <a id="auftragsstatus"></a>`auftragsstatus` | [Enum Auftragsstatus](/bo4e/202604/enum/Auftragsstatus)<br/><Werte>`GESCHEITERT`, `ERFOLGREICH`, `LIEFERUNG_GEPLANT`, `GEPLANT`, `ZUGESTIMMT`, `WIDERSPROCHEN`, `STOERUNGSFREI`, `GESTOERT`, `FESTGESTELLTE_STOERUNG`, `VERMUTETE_STOERUNG`, `ABGELEHNT`, `BEENDET`, `ANTWORT_DRITTER`, `BESTAETIGT`, `UMGESETZT`, `ENFG_STROMSPEICHER_UND_VERLUSTENERGIE`, `ENFG_ELEKTRISCH_ANGETRIEBENE_WAERMEPUMPEN`, `ENFG_UMLAGEERHEBUNG_BEI_ANLAGEN_ZUR_VERSTROMUNG_VON_KUPPELGASEN`, `ENFG_HERSTELLUNG_VON_GRUENEN_WASSERSTOFF`, `ENFG_STROMKOSTENINTENSIVE_UNTERNEHMEN`, `ENFG_HERSTELLUNG_VON_WASSERSTOFF_IN_STROMKOSTENINTENSIVEN_UNTERNEHMEN`, `ENFG_SCHIENENBAHNEN`, `ENFG_ELEKTRISCHE_BETRIEBENE_BUSSEN_IM_LINIENVERKEHR`, `ENFG_LANDSTROMANLAGEN`, `AENDERUNG_DER_DATEN`, `KEINE_AENDERUNG_DER_DATEN`, `ZEITREIHE_AKZEPTIERT`, `ZEITREIHE_NICHT_AKZEPTIERT`</Werte> | Auftragsstatus |
| <a id="statusanlass"></a>`statusanlass` | [Enum Statusanlass](/bo4e/202604/enum/Statusanlass)<br/><Werte>`KOMMUNIKATIONSSTOERUNG`, `STATUS_GERAETEWECHSEL`, `MESSEINRICHTUNG_GESTOERT_DEFEKT`, `KEINE_STOERUNG_FESTSTELLBAR`, `STOERUNGSBEHEBUNG_NICHT_MOEGLICH`, `REPARATUR_OHNE_GERAETEWECHSEL`</Werte> | Statusanlass |
| <a id="antwortstatus"></a>`antwortstatus` | string | antwortstatus |
| <a id="fehlerbeschreibung"></a>`fehlerbeschreibung` | [Fehlerbeschreibung](/bo4e/202604/com/Fehlerbeschreibung) | — |
| <a id="fehlerbeschreibungtext"></a>`fehlerbeschreibungText` | string | Fehlerbeschreibung |
| <a id="begruendung"></a>`begruendung` | [Begruendung](/bo4e/202604/com/Begruendung) | — |
| <a id="begruendungtext"></a>`begruendungText` | string | Begruendung |
| <a id="lokationsid"></a>`lokationsId` | string | lokationsId |
| <a id="referenzmelo"></a>`referenzMelo` | string | referenzMelo |
| <a id="allgemeineinformationen"></a>`allgemeineInformationen` | [AllgemeineInformationen](/bo4e/202604/com/AllgemeineInformationen) | — |
| <a id="allgemeineinformationentext"></a>`allgemeineInformationenText` | string | Allgemeine Informationen |
| <a id="statusveraenderungszeitpunkt"></a>`statusVeraenderungsZeitpunkt` | string (date-time) | statusVeraenderungsZeitpunkt |
| <a id="auftragsstatusliste"></a>`auftragsStatusListe` | [Enum Auftragsstatus[]](/bo4e/202604/enum/Auftragsstatus)<br/><Werte>`GESCHEITERT`, `ERFOLGREICH`, `LIEFERUNG_GEPLANT`, `GEPLANT`, `ZUGESTIMMT`, `WIDERSPROCHEN`, `STOERUNGSFREI`, `GESTOERT`, `FESTGESTELLTE_STOERUNG`, `VERMUTETE_STOERUNG`, `ABGELEHNT`, `BEENDET`, `ANTWORT_DRITTER`, `BESTAETIGT`, `UMGESETZT`, `ENFG_STROMSPEICHER_UND_VERLUSTENERGIE`, `ENFG_ELEKTRISCH_ANGETRIEBENE_WAERMEPUMPEN`, `ENFG_UMLAGEERHEBUNG_BEI_ANLAGEN_ZUR_VERSTROMUNG_VON_KUPPELGASEN`, `ENFG_HERSTELLUNG_VON_GRUENEN_WASSERSTOFF`, `ENFG_STROMKOSTENINTENSIVE_UNTERNEHMEN`, `ENFG_HERSTELLUNG_VON_WASSERSTOFF_IN_STROMKOSTENINTENSIVEN_UNTERNEHMEN`, `ENFG_SCHIENENBAHNEN`, `ENFG_ELEKTRISCHE_BETRIEBENE_BUSSEN_IM_LINIENVERKEHR`, `ENFG_LANDSTROMANLAGEN`, `AENDERUNG_DER_DATEN`, `KEINE_AENDERUNG_DER_DATEN`, `ZEITREIHE_AKZEPTIERT`, `ZEITREIHE_NICHT_AKZEPTIERT`</Werte> | auftragsStatusListe |
| <a id="lokationstyp"></a>`lokationsTyp` | [Enum Lokationstyp](/bo4e/202604/enum/Lokationstyp)<br/><Werte>`MALO`, `MELO`, `NELO`, `TECHNISCHE_RESSOURCE`, `STEUERBARE_RESSOURCE`, `TRANCHE`, `MABIS_ZAEHLPUNKT`</Werte> | Gibt an, ob es sich um eine Markt- oder Messlokation handelt |
| <a id="statusobjekt"></a>`statusObjekt` | [Enum Statusobjekt](/bo4e/202604/enum/Statusobjekt)<br/><Werte>`MSBWECHSEL`, `UMBAUMELO`, `ERSTEINBAUIMS`, `ERSTEINBAUMME`, `GERAET`, `ANGEBOTANFRAGE`, `STATUSBESTELLUNG`, `LIEFERSCHEIN`, `SPERREN`, `ENTSPERREN`, `PRIVILEGIERUNG_NACH_ENFG`, `VERAENDERUNGSSTATUS_DER_DATEN`, `TURNUSAUSLESUNG`, `PRUEFSTATUS_ANTWORT_SUMMENZEITREIHEN`, `ABWEISUNG_SUMMENZEITREIHE`, `PRUEFSTATUS_SUMMENZEITREIHE`, `DATENSTATUS_SUMMENZEITREIHE`, `ABWEISUNG_STATUSMELDUNG_AENDERUNG`, `AUSFALLARBEIT`, `FAHRPLANANTEIL`, `GEGENVORSCHLAG_AUSFALLARBEIT`, `GEGENVORSCHLAG_FAHRPLANANTEIL`</Werte> | Statusobjekt |
| <a id="antwortstatuscodeliste"></a>`antwortstatusCodeliste` | string | antwortstatusCodeliste |
| <a id="vorgangsreferenznummer"></a>`vorgangsreferenznummer` | string | vorgangsreferenznummer |
| <a id="mitteilungsnummer"></a>`mitteilungsnummer` | string | mitteilungsnummer |
| <a id="anfragereferenznummer"></a>`anfragereferenznummer` | string | anfragereferenznummer |
| <a id="fertigstellungsdatum"></a>`fertigstellungsdatum` | string (date-time) | fertigstellungsdatum |
| <a id="lieferdatum"></a>`lieferdatum` | string | lieferdatum |
| <a id="sendungsposition"></a>`sendungsposition` | integer | sendungsposition |
| <a id="gueltigab"></a>`gueltigAb` | string (date-time) | gueltigAb |
| <a id="referenzmalo"></a>`referenzMalo` | string | referenzMalo |
| <a id="referenzpreisschluesselstamm"></a>`referenzPreisschluesselstamm` | string | referenzPreisschluesselstamm |
| <a id="referenzartikelid"></a>`referenzArtikelID` | string | referenzArtikelID |
| <a id="startdatum"></a>`startdatum` | string (date-time) | startdatum |
| <a id="angebotsnummer"></a>`angebotsnummer` | string | angebotsnummer |
| <a id="anfragereferenz"></a>`anfrageReferenz` | string | anfrageReferenz |
| <a id="vertragsende"></a>`vertragsende` | string (date-time) | vertragsende |
| <a id="laufendenummer"></a>`laufendeNummer` | integer | Laufende Nummer |
| <a id="dokumentenreferenznummer"></a>`dokumentenreferenznummer` | string | Dokumentenreferenznummer |
| <a id="ansichtsender"></a>`ansichtSender` | [AnsichtSender[]](/bo4e/202604/com/AnsichtSender) | ansichtSender |
| <a id="gueltigkeitszeitspanne"></a>`gueltigkeitsZeitspanne` | string | gueltigkeitsZeitspanne |
| <a id="privilegierteenergiemenge"></a>`privilegierteEnergiemenge` | [ZeitintervallMenge](/bo4e/202604/com/ZeitintervallMenge) | — |
| <a id="ansprechpartner"></a>`ansprechpartner` | [Ansprechpartner](/bo4e/202604/bo/Ansprechpartner) | Ansprechpartner |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[positionsnummer](/bo4e/202604/com/StatusmitteilungPosition#positionsnummer)</span> | positionsnummer | integer |
| <span className="hbs-f hbs-e0">[bearbeitungsdatum](/bo4e/202604/com/StatusmitteilungPosition#bearbeitungsdatum)</span> | bearbeitungsdatum | string (date-time) |
| <span className="hbs-f hbs-e0">[verwendungAb](/bo4e/202604/com/StatusmitteilungPosition#verwendungab)</span> | verwendungAb | string (date-time) |
| <span className="hbs-f hbs-e0">[verwendungBis](/bo4e/202604/com/StatusmitteilungPosition#verwendungbis)</span> | verwendungBis | string (date-time) |
| <span className="hbs-f hbs-e0">[enddatum](/bo4e/202604/com/StatusmitteilungPosition#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-f hbs-e0">[auftragsstatus](/bo4e/202604/com/StatusmitteilungPosition#auftragsstatus)</span> | Auftragsstatus | [Enum Auftragsstatus](/bo4e/202604/enum/Auftragsstatus)<br/><Werte>`GESCHEITERT`, `ERFOLGREICH`, `LIEFERUNG_GEPLANT`, `GEPLANT`, `ZUGESTIMMT`, `WIDERSPROCHEN`, `STOERUNGSFREI`, `GESTOERT`, `FESTGESTELLTE_STOERUNG`, `VERMUTETE_STOERUNG`, `ABGELEHNT`, `BEENDET`, `ANTWORT_DRITTER`, `BESTAETIGT`, `UMGESETZT`, `ENFG_STROMSPEICHER_UND_VERLUSTENERGIE`, `ENFG_ELEKTRISCH_ANGETRIEBENE_WAERMEPUMPEN`, `ENFG_UMLAGEERHEBUNG_BEI_ANLAGEN_ZUR_VERSTROMUNG_VON_KUPPELGASEN`, `ENFG_HERSTELLUNG_VON_GRUENEN_WASSERSTOFF`, `ENFG_STROMKOSTENINTENSIVE_UNTERNEHMEN`, `ENFG_HERSTELLUNG_VON_WASSERSTOFF_IN_STROMKOSTENINTENSIVEN_UNTERNEHMEN`, `ENFG_SCHIENENBAHNEN`, `ENFG_ELEKTRISCHE_BETRIEBENE_BUSSEN_IM_LINIENVERKEHR`, `ENFG_LANDSTROMANLAGEN`, `AENDERUNG_DER_DATEN`, `KEINE_AENDERUNG_DER_DATEN`, `ZEITREIHE_AKZEPTIERT`, `ZEITREIHE_NICHT_AKZEPTIERT`</Werte> |
| <span className="hbs-f hbs-e0">[statusanlass](/bo4e/202604/com/StatusmitteilungPosition#statusanlass)</span> | Statusanlass | [Enum Statusanlass](/bo4e/202604/enum/Statusanlass)<br/><Werte>`KOMMUNIKATIONSSTOERUNG`, `STATUS_GERAETEWECHSEL`, `MESSEINRICHTUNG_GESTOERT_DEFEKT`, `KEINE_STOERUNG_FESTSTELLBAR`, `STOERUNGSBEHEBUNG_NICHT_MOEGLICH`, `REPARATUR_OHNE_GERAETEWECHSEL`</Werte> |
| <span className="hbs-f hbs-e0">[antwortstatus](/bo4e/202604/com/StatusmitteilungPosition#antwortstatus)</span> | antwortstatus | string |
| <span className="hbs-g hbs-e0">[fehlerbeschreibung](/bo4e/202604/com/StatusmitteilungPosition#fehlerbeschreibung)</span> | — | [Fehlerbeschreibung](/bo4e/202604/com/Fehlerbeschreibung) |
| <span className="hbs-f hbs-e1">[beschreibung1](/bo4e/202604/com/Fehlerbeschreibung#beschreibung1)</span> | Fehler Beschreibung Zeile 1 | string |
| <span className="hbs-f hbs-e1">[beschreibung2](/bo4e/202604/com/Fehlerbeschreibung#beschreibung2)</span> | Fehler Beschreibung Zeile 2 | string |
| <span className="hbs-f hbs-e1">[beschreibung3](/bo4e/202604/com/Fehlerbeschreibung#beschreibung3)</span> | Fehler Beschreibung Zeile 3 | string |
| <span className="hbs-f hbs-e1">[beschreibung4](/bo4e/202604/com/Fehlerbeschreibung#beschreibung4)</span> | Fehler Beschreibung Zeile 4 | string |
| <span className="hbs-f hbs-e1">[beschreibung5](/bo4e/202604/com/Fehlerbeschreibung#beschreibung5)</span> | Fehler Beschreibung Zeile 5 | string |
| <span className="hbs-f hbs-e0">[fehlerbeschreibungText](/bo4e/202604/com/StatusmitteilungPosition#fehlerbeschreibungtext)</span> | Fehlerbeschreibung | string |
| <span className="hbs-g hbs-e0">[begruendung](/bo4e/202604/com/StatusmitteilungPosition#begruendung)</span> | — | [Begruendung](/bo4e/202604/com/Begruendung) |
| <span className="hbs-f hbs-e1">[begruendung1](/bo4e/202604/com/Begruendung#begruendung1)</span> | Begruendung Zeile 1 | string |
| <span className="hbs-f hbs-e1">[begruendung2](/bo4e/202604/com/Begruendung#begruendung2)</span> | Begruendung Zeile 2 | string |
| <span className="hbs-f hbs-e1">[begruendung3](/bo4e/202604/com/Begruendung#begruendung3)</span> | Begruendung Zeile 3 | string |
| <span className="hbs-f hbs-e1">[begruendung4](/bo4e/202604/com/Begruendung#begruendung4)</span> | Begruendung Zeile 4 | string |
| <span className="hbs-f hbs-e1">[begruendung5](/bo4e/202604/com/Begruendung#begruendung5)</span> | Begruendung Zeile 5 | string |
| <span className="hbs-f hbs-e0">[begruendungText](/bo4e/202604/com/StatusmitteilungPosition#begruendungtext)</span> | Begruendung | string |
| <span className="hbs-f hbs-e0">[lokationsId](/bo4e/202604/com/StatusmitteilungPosition#lokationsid)</span> | lokationsId | string |
| <span className="hbs-f hbs-e0">[referenzMelo](/bo4e/202604/com/StatusmitteilungPosition#referenzmelo)</span> | referenzMelo | string |
| <span className="hbs-g hbs-e0">[allgemeineInformationen](/bo4e/202604/com/StatusmitteilungPosition#allgemeineinformationen)</span> | — | [AllgemeineInformationen](/bo4e/202604/com/AllgemeineInformationen) |
| <span className="hbs-f hbs-e1">[info1](/bo4e/202604/com/AllgemeineInformationen#info1)</span> | Allgemeine Info 1 | string |
| <span className="hbs-f hbs-e1">[info2](/bo4e/202604/com/AllgemeineInformationen#info2)</span> | Allgemeine Info 2 | string |
| <span className="hbs-f hbs-e1">[info3](/bo4e/202604/com/AllgemeineInformationen#info3)</span> | Allgemeine Info 3 | string |
| <span className="hbs-f hbs-e1">[info4](/bo4e/202604/com/AllgemeineInformationen#info4)</span> | Allgemeine Info 4 | string |
| <span className="hbs-f hbs-e1">[info5](/bo4e/202604/com/AllgemeineInformationen#info5)</span> | Allgemeine Info 5 | string |
| <span className="hbs-f hbs-e0">[allgemeineInformationenText](/bo4e/202604/com/StatusmitteilungPosition#allgemeineinformationentext)</span> | Allgemeine Informationen | string |
| <span className="hbs-f hbs-e0">[statusVeraenderungsZeitpunkt](/bo4e/202604/com/StatusmitteilungPosition#statusveraenderungszeitpunkt)</span> | statusVeraenderungsZeitpunkt | string (date-time) |
| <span className="hbs-f hbs-e0">[auftragsStatusListe](/bo4e/202604/com/StatusmitteilungPosition#auftragsstatusliste) <span className="hbs-liste">[ ]</span></span> | auftragsStatusListe | [Enum Auftragsstatus[]](/bo4e/202604/enum/Auftragsstatus)<br/><Werte>`GESCHEITERT`, `ERFOLGREICH`, `LIEFERUNG_GEPLANT`, `GEPLANT`, `ZUGESTIMMT`, `WIDERSPROCHEN`, `STOERUNGSFREI`, `GESTOERT`, `FESTGESTELLTE_STOERUNG`, `VERMUTETE_STOERUNG`, `ABGELEHNT`, `BEENDET`, `ANTWORT_DRITTER`, `BESTAETIGT`, `UMGESETZT`, `ENFG_STROMSPEICHER_UND_VERLUSTENERGIE`, `ENFG_ELEKTRISCH_ANGETRIEBENE_WAERMEPUMPEN`, `ENFG_UMLAGEERHEBUNG_BEI_ANLAGEN_ZUR_VERSTROMUNG_VON_KUPPELGASEN`, `ENFG_HERSTELLUNG_VON_GRUENEN_WASSERSTOFF`, `ENFG_STROMKOSTENINTENSIVE_UNTERNEHMEN`, `ENFG_HERSTELLUNG_VON_WASSERSTOFF_IN_STROMKOSTENINTENSIVEN_UNTERNEHMEN`, `ENFG_SCHIENENBAHNEN`, `ENFG_ELEKTRISCHE_BETRIEBENE_BUSSEN_IM_LINIENVERKEHR`, `ENFG_LANDSTROMANLAGEN`, `AENDERUNG_DER_DATEN`, `KEINE_AENDERUNG_DER_DATEN`, `ZEITREIHE_AKZEPTIERT`, `ZEITREIHE_NICHT_AKZEPTIERT`</Werte> |
| <span className="hbs-f hbs-e0">[lokationsTyp](/bo4e/202604/com/StatusmitteilungPosition#lokationstyp)</span> | Gibt an, ob es sich um eine Markt- oder Messlokation handelt | [Enum Lokationstyp](/bo4e/202604/enum/Lokationstyp)<br/><Werte>`MALO`, `MELO`, `NELO`, `TECHNISCHE_RESSOURCE`, `STEUERBARE_RESSOURCE`, `TRANCHE`, `MABIS_ZAEHLPUNKT`</Werte> |
| <span className="hbs-f hbs-e0">[statusObjekt](/bo4e/202604/com/StatusmitteilungPosition#statusobjekt)</span> | Statusobjekt | [Enum Statusobjekt](/bo4e/202604/enum/Statusobjekt)<br/><Werte>`MSBWECHSEL`, `UMBAUMELO`, `ERSTEINBAUIMS`, `ERSTEINBAUMME`, `GERAET`, `ANGEBOTANFRAGE`, `STATUSBESTELLUNG`, `LIEFERSCHEIN`, `SPERREN`, `ENTSPERREN`, `PRIVILEGIERUNG_NACH_ENFG`, `VERAENDERUNGSSTATUS_DER_DATEN`, `TURNUSAUSLESUNG`, `PRUEFSTATUS_ANTWORT_SUMMENZEITREIHEN`, `ABWEISUNG_SUMMENZEITREIHE`, `PRUEFSTATUS_SUMMENZEITREIHE`, `DATENSTATUS_SUMMENZEITREIHE`, `ABWEISUNG_STATUSMELDUNG_AENDERUNG`, `AUSFALLARBEIT`, `FAHRPLANANTEIL`, `GEGENVORSCHLAG_AUSFALLARBEIT`, `GEGENVORSCHLAG_FAHRPLANANTEIL`</Werte> |
| <span className="hbs-f hbs-e0">[antwortstatusCodeliste](/bo4e/202604/com/StatusmitteilungPosition#antwortstatuscodeliste)</span> | antwortstatusCodeliste | string |
| <span className="hbs-f hbs-e0">[vorgangsreferenznummer](/bo4e/202604/com/StatusmitteilungPosition#vorgangsreferenznummer)</span> | vorgangsreferenznummer | string |
| <span className="hbs-f hbs-e0">[mitteilungsnummer](/bo4e/202604/com/StatusmitteilungPosition#mitteilungsnummer)</span> | mitteilungsnummer | string |
| <span className="hbs-f hbs-e0">[anfragereferenznummer](/bo4e/202604/com/StatusmitteilungPosition#anfragereferenznummer)</span> | anfragereferenznummer | string |
| <span className="hbs-f hbs-e0">[fertigstellungsdatum](/bo4e/202604/com/StatusmitteilungPosition#fertigstellungsdatum)</span> | fertigstellungsdatum | string (date-time) |
| <span className="hbs-f hbs-e0">[lieferdatum](/bo4e/202604/com/StatusmitteilungPosition#lieferdatum)</span> | lieferdatum | string |
| <span className="hbs-f hbs-e0">[sendungsposition](/bo4e/202604/com/StatusmitteilungPosition#sendungsposition)</span> | sendungsposition | integer |
| <span className="hbs-f hbs-e0">[gueltigAb](/bo4e/202604/com/StatusmitteilungPosition#gueltigab)</span> | gueltigAb | string (date-time) |
| <span className="hbs-f hbs-e0">[referenzMalo](/bo4e/202604/com/StatusmitteilungPosition#referenzmalo)</span> | referenzMalo | string |
| <span className="hbs-f hbs-e0">[referenzPreisschluesselstamm](/bo4e/202604/com/StatusmitteilungPosition#referenzpreisschluesselstamm)</span> | referenzPreisschluesselstamm | string |
| <span className="hbs-f hbs-e0">[referenzArtikelID](/bo4e/202604/com/StatusmitteilungPosition#referenzartikelid)</span> | referenzArtikelID | string |
| <span className="hbs-f hbs-e0">[startdatum](/bo4e/202604/com/StatusmitteilungPosition#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e0">[angebotsnummer](/bo4e/202604/com/StatusmitteilungPosition#angebotsnummer)</span> | angebotsnummer | string |
| <span className="hbs-f hbs-e0">[anfrageReferenz](/bo4e/202604/com/StatusmitteilungPosition#anfragereferenz)</span> | anfrageReferenz | string |
| <span className="hbs-f hbs-e0">[vertragsende](/bo4e/202604/com/StatusmitteilungPosition#vertragsende)</span> | vertragsende | string (date-time) |
| <span className="hbs-f hbs-e0">[laufendeNummer](/bo4e/202604/com/StatusmitteilungPosition#laufendenummer)</span> | Laufende Nummer | integer |
| <span className="hbs-f hbs-e0">[dokumentenreferenznummer](/bo4e/202604/com/StatusmitteilungPosition#dokumentenreferenznummer)</span> | Dokumentenreferenznummer | string |
| <span className="hbs-g hbs-e0">[ansichtSender](/bo4e/202604/com/StatusmitteilungPosition#ansichtsender) <span className="hbs-liste">[ ]</span></span> | ansichtSender | [AnsichtSender[]](/bo4e/202604/com/AnsichtSender) |
| <span className="hbs-f hbs-e1">[verwendungAb](/bo4e/202604/com/AnsichtSender#verwendungab)</span> | verwendungAb | string (date-time) |
| <span className="hbs-f hbs-e1">[verwendungBis](/bo4e/202604/com/AnsichtSender#verwendungbis)</span> | verwendungBis | string (date-time) |
| <span className="hbs-f hbs-e1">[leistungsperiode](/bo4e/202604/com/AnsichtSender#leistungsperiode)</span> | leistungsperiode | string |
| <span className="hbs-g hbs-e1">[menge](/bo4e/202604/com/AnsichtSender#menge)</span> | — | [Menge](/bo4e/202604/com/Menge) |
| <span className="hbs-f hbs-e2">[wert](/bo4e/202604/com/Menge#wert)</span> | Wert | number (float) |
| <span className="hbs-f hbs-e2">[einheit](/bo4e/202604/com/Menge#einheit)</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202604/enum/Mengeneinheit)<br/><Werte>`W`, `WH`, `KW`, `KWH`, `KVARH`, `MW`, `MWH`, `STUECK`, `KUBIKMETER`, `STUNDE`, `TAG`, `MONAT`, `JAHR`, `PROZENT`, `ANZAHL`, `VAR`, `KVAR`, `VARH`, `KWHK`, `Z16`, `KWT`, `WATT_PRO_QUADRATMETER`, `METER_PRO_SEKUNDE`</Werte> |
| <span className="hbs-f hbs-e2">[startdatum](/bo4e/202604/com/Menge#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e2">[enddatum](/bo4e/202604/com/Menge#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-f hbs-e1">[tarifstufe](/bo4e/202604/com/AnsichtSender#tarifstufe)</span> | Tarifstufe | [Enum Tarifstufe](/bo4e/202604/enum/Tarifstufe)<br/><Werte>`TARIFSTUFE_0`, `TARIFSTUFE_1`, `TARIFSTUFE_2`, `TARIFSTUFE_3`, `TARIFSTUFE_4`, `TARIFSTUFE_5`, `TARIFSTUFE_6`, `TARIFSTUFE_7`, `TARIFSTUFE_8`, `TARIFSTUFE_9`</Werte> |
| <span className="hbs-f hbs-e0">[gueltigkeitsZeitspanne](/bo4e/202604/com/StatusmitteilungPosition#gueltigkeitszeitspanne)</span> | gueltigkeitsZeitspanne | string |
| <span className="hbs-g hbs-e0">[privilegierteEnergiemenge](/bo4e/202604/com/StatusmitteilungPosition#privilegierteenergiemenge)</span> | — | [ZeitintervallMenge](/bo4e/202604/com/ZeitintervallMenge) |
| <span className="hbs-f hbs-e1">[verwendungAb](/bo4e/202604/com/ZeitintervallMenge#verwendungab)</span> | verwendungAb | string (date-time) |
| <span className="hbs-f hbs-e1">[verwendungBis](/bo4e/202604/com/ZeitintervallMenge#verwendungbis)</span> | verwendungBis | string (date-time) |
| <span className="hbs-g hbs-e1">[menge](/bo4e/202604/com/ZeitintervallMenge#menge)</span> | — | [Menge](/bo4e/202604/com/Menge) |
| <span className="hbs-f hbs-e2">[wert](/bo4e/202604/com/Menge#wert)</span> | Wert | number (float) |
| <span className="hbs-f hbs-e2">[einheit](/bo4e/202604/com/Menge#einheit)</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202604/enum/Mengeneinheit)<br/><Werte>`W`, `WH`, `KW`, `KWH`, `KVARH`, `MW`, `MWH`, `STUECK`, `KUBIKMETER`, `STUNDE`, `TAG`, `MONAT`, `JAHR`, `PROZENT`, `ANZAHL`, `VAR`, `KVAR`, `VARH`, `KWHK`, `Z16`, `KWT`, `WATT_PRO_QUADRATMETER`, `METER_PRO_SEKUNDE`</Werte> |
| <span className="hbs-f hbs-e2">[startdatum](/bo4e/202604/com/Menge#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e2">[enddatum](/bo4e/202604/com/Menge#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-g hbs-e0">[ansprechpartner](/bo4e/202604/com/StatusmitteilungPosition#ansprechpartner)</span> | Ansprechpartner | [Ansprechpartner](/bo4e/202604/bo/Ansprechpartner) |
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

### positionsnummer

34 Verwendung(en) in den Nachrichtentypen IFTSTA, INSRPT.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_21007](/schnittstellen/202604/pruefi/IFTSTA/PI_21007) | Prüfi | IFTSTA | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_21009](/schnittstellen/202604/pruefi/IFTSTA/PI_21009) | Prüfi | IFTSTA | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_21010](/schnittstellen/202604/pruefi/IFTSTA/PI_21010) | Prüfi | IFTSTA | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_21011](/schnittstellen/202604/pruefi/IFTSTA/PI_21011) | Prüfi | IFTSTA | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_21012](/schnittstellen/202604/pruefi/IFTSTA/PI_21012) | Prüfi | IFTSTA | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_21013](/schnittstellen/202604/pruefi/IFTSTA/PI_21013) | Prüfi | IFTSTA | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_21015](/schnittstellen/202604/pruefi/IFTSTA/PI_21015) | Prüfi | IFTSTA | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_21018](/schnittstellen/202604/pruefi/IFTSTA/PI_21018) | Prüfi | IFTSTA | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_21024](/schnittstellen/202604/pruefi/IFTSTA/PI_21024) | Prüfi | IFTSTA | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_21025](/schnittstellen/202604/pruefi/IFTSTA/PI_21025) | Prüfi | IFTSTA | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_21026](/schnittstellen/202604/pruefi/IFTSTA/PI_21026) | Prüfi | IFTSTA | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_21027](/schnittstellen/202604/pruefi/IFTSTA/PI_21027) | Prüfi | IFTSTA | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_21028](/schnittstellen/202604/pruefi/IFTSTA/PI_21028) | Prüfi | IFTSTA | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_21029](/schnittstellen/202604/pruefi/IFTSTA/PI_21029) | Prüfi | IFTSTA | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_21030](/schnittstellen/202604/pruefi/IFTSTA/PI_21030) | Prüfi | IFTSTA | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_21031](/schnittstellen/202604/pruefi/IFTSTA/PI_21031) | Prüfi | IFTSTA | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_21032](/schnittstellen/202604/pruefi/IFTSTA/PI_21032) | Prüfi | IFTSTA | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_21033](/schnittstellen/202604/pruefi/IFTSTA/PI_21033) | Prüfi | IFTSTA | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_21035](/schnittstellen/202604/pruefi/IFTSTA/PI_21035) | Prüfi | IFTSTA | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_21036](/schnittstellen/202604/pruefi/IFTSTA/PI_21036) | Prüfi | IFTSTA | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_21039](/schnittstellen/202604/pruefi/IFTSTA/PI_21039) | Prüfi | IFTSTA | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_21040](/schnittstellen/202604/pruefi/IFTSTA/PI_21040) | Prüfi | IFTSTA | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_21043](/schnittstellen/202604/pruefi/IFTSTA/PI_21043) | Prüfi | IFTSTA | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_21044](/schnittstellen/202604/pruefi/IFTSTA/PI_21044) | Prüfi | IFTSTA | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_21045](/schnittstellen/202604/pruefi/IFTSTA/PI_21045) | Prüfi | IFTSTA | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_21047](/schnittstellen/202604/pruefi/IFTSTA/PI_21047) | Prüfi | IFTSTA | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_23001](/schnittstellen/202604/pruefi/INSRPT/PI_23001) | Prüfi | INSRPT | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_23003](/schnittstellen/202604/pruefi/INSRPT/PI_23003) | Prüfi | INSRPT | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_23004](/schnittstellen/202604/pruefi/INSRPT/PI_23004) | Prüfi | INSRPT | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_23005](/schnittstellen/202604/pruefi/INSRPT/PI_23005) | Prüfi | INSRPT | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_23008](/schnittstellen/202604/pruefi/INSRPT/PI_23008) | Prüfi | INSRPT | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_23009](/schnittstellen/202604/pruefi/INSRPT/PI_23009) | Prüfi | INSRPT | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_23011](/schnittstellen/202604/pruefi/INSRPT/PI_23011) | Prüfi | INSRPT | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_23012](/schnittstellen/202604/pruefi/INSRPT/PI_23012) | Prüfi | INSRPT | stammdaten › STATUSMITTEILUNG › positionsdaten |

### bearbeitungsdatum

3 Verwendung(en) in den Nachrichtentypen INSRPT.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_23008](/schnittstellen/202604/pruefi/INSRPT/PI_23008) | Prüfi | INSRPT | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_23009](/schnittstellen/202604/pruefi/INSRPT/PI_23009) | Prüfi | INSRPT | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_23012](/schnittstellen/202604/pruefi/INSRPT/PI_23012) | Prüfi | INSRPT | stammdaten › STATUSMITTEILUNG › positionsdaten |

### verwendungAb

8 Verwendung(en) in den Nachrichtentypen INSRPT.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_23001](/schnittstellen/202604/pruefi/INSRPT/PI_23001) | Prüfi | INSRPT | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_23003](/schnittstellen/202604/pruefi/INSRPT/PI_23003) | Prüfi | INSRPT | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_23004](/schnittstellen/202604/pruefi/INSRPT/PI_23004) | Prüfi | INSRPT | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_23005](/schnittstellen/202604/pruefi/INSRPT/PI_23005) | Prüfi | INSRPT | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_23008](/schnittstellen/202604/pruefi/INSRPT/PI_23008) | Prüfi | INSRPT | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_23009](/schnittstellen/202604/pruefi/INSRPT/PI_23009) | Prüfi | INSRPT | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_23011](/schnittstellen/202604/pruefi/INSRPT/PI_23011) | Prüfi | INSRPT | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_23012](/schnittstellen/202604/pruefi/INSRPT/PI_23012) | Prüfi | INSRPT | stammdaten › STATUSMITTEILUNG › positionsdaten |

### verwendungBis

3 Verwendung(en) in den Nachrichtentypen INSRPT.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_23008](/schnittstellen/202604/pruefi/INSRPT/PI_23008) | Prüfi | INSRPT | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_23009](/schnittstellen/202604/pruefi/INSRPT/PI_23009) | Prüfi | INSRPT | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_23012](/schnittstellen/202604/pruefi/INSRPT/PI_23012) | Prüfi | INSRPT | stammdaten › STATUSMITTEILUNG › positionsdaten |

### enddatum

3 Verwendung(en) in den Nachrichtentypen INSRPT.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_23004](/schnittstellen/202604/pruefi/INSRPT/PI_23004) | Prüfi | INSRPT | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_23005](/schnittstellen/202604/pruefi/INSRPT/PI_23005) | Prüfi | INSRPT | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_23011](/schnittstellen/202604/pruefi/INSRPT/PI_23011) | Prüfi | INSRPT | stammdaten › STATUSMITTEILUNG › positionsdaten |

### auftragsstatus

7 Verwendung(en) in den Nachrichtentypen INSRPT.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_23001](/schnittstellen/202604/pruefi/INSRPT/PI_23001) | Prüfi | INSRPT | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_23004](/schnittstellen/202604/pruefi/INSRPT/PI_23004) | Prüfi | INSRPT | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_23005](/schnittstellen/202604/pruefi/INSRPT/PI_23005) | Prüfi | INSRPT | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_23008](/schnittstellen/202604/pruefi/INSRPT/PI_23008) | Prüfi | INSRPT | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_23009](/schnittstellen/202604/pruefi/INSRPT/PI_23009) | Prüfi | INSRPT | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_23011](/schnittstellen/202604/pruefi/INSRPT/PI_23011) | Prüfi | INSRPT | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_23012](/schnittstellen/202604/pruefi/INSRPT/PI_23012) | Prüfi | INSRPT | stammdaten › STATUSMITTEILUNG › positionsdaten |

### statusanlass

3 Verwendung(en) in den Nachrichtentypen INSRPT.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_23008](/schnittstellen/202604/pruefi/INSRPT/PI_23008) | Prüfi | INSRPT | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_23009](/schnittstellen/202604/pruefi/INSRPT/PI_23009) | Prüfi | INSRPT | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_23012](/schnittstellen/202604/pruefi/INSRPT/PI_23012) | Prüfi | INSRPT | stammdaten › STATUSMITTEILUNG › positionsdaten |

### antwortstatus

2 Verwendung(en) in den Nachrichtentypen INSRPT.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_23003](/schnittstellen/202604/pruefi/INSRPT/PI_23003) | Prüfi | INSRPT | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_23004](/schnittstellen/202604/pruefi/INSRPT/PI_23004) | Prüfi | INSRPT | stammdaten › STATUSMITTEILUNG › positionsdaten |

### lokationsId

8 Verwendung(en) in den Nachrichtentypen INSRPT.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_23001](/schnittstellen/202604/pruefi/INSRPT/PI_23001) | Prüfi | INSRPT | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_23003](/schnittstellen/202604/pruefi/INSRPT/PI_23003) | Prüfi | INSRPT | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_23004](/schnittstellen/202604/pruefi/INSRPT/PI_23004) | Prüfi | INSRPT | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_23005](/schnittstellen/202604/pruefi/INSRPT/PI_23005) | Prüfi | INSRPT | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_23008](/schnittstellen/202604/pruefi/INSRPT/PI_23008) | Prüfi | INSRPT | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_23009](/schnittstellen/202604/pruefi/INSRPT/PI_23009) | Prüfi | INSRPT | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_23011](/schnittstellen/202604/pruefi/INSRPT/PI_23011) | Prüfi | INSRPT | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_23012](/schnittstellen/202604/pruefi/INSRPT/PI_23012) | Prüfi | INSRPT | stammdaten › STATUSMITTEILUNG › positionsdaten |

### referenzMelo

2 Verwendung(en) in den Nachrichtentypen INSRPT.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_23011](/schnittstellen/202604/pruefi/INSRPT/PI_23011) | Prüfi | INSRPT | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_23012](/schnittstellen/202604/pruefi/INSRPT/PI_23012) | Prüfi | INSRPT | stammdaten › STATUSMITTEILUNG › positionsdaten |

### statusVeraenderungsZeitpunkt

2 Verwendung(en) in den Nachrichtentypen IFTSTA.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_21043](/schnittstellen/202604/pruefi/IFTSTA/PI_21043) | Prüfi | IFTSTA | stammdaten › STATUSMITTEILUNG › positionsdaten |
| [PI_21044](/schnittstellen/202604/pruefi/IFTSTA/PI_21044) | Prüfi | IFTSTA | stammdaten › STATUSMITTEILUNG › positionsdaten |

### auftragsStatusListe

1 Verwendung(en) in den Nachrichtentypen IFTSTA.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_21045](/schnittstellen/202604/pruefi/IFTSTA/PI_21045) | Prüfi | IFTSTA | stammdaten › STATUSMITTEILUNG › positionsdaten |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
