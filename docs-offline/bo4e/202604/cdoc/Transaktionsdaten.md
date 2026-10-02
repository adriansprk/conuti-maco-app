# Transaktionsdaten
<span hidden data-pagefind-meta={"title:Transaktionsdaten — BO4E-Dokumentobjekt (FV 202604)"} />

BO4E-Dokumentobjekt · 100 Felder · 3272 Verwendungen in Prüfis und Events · 105 namensgleiche Felder inline definiert

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung | Inline definiert |
|---|---|---|---|
| <a id="datenaustauschreferenz"></a>`datenaustauschreferenz` | string | Enthält die eindeutige Datenaustauschreferenz der Nachricht, die in der EDIFact Kommunikation verwendet wird | — |
| <a id="sparte"></a>`sparte` | [Enum Sparte](/bo4e/202604/enum/Sparte)<br/><Werte>`STROM`, `GAS`, `FERNWAERME`, `NAHWAERME`, `WASSER`, `ABWASSER`</Werte> | Enthält Informationen über die Sparte | — |
| <a id="transaktionsgrund"></a>`transaktionsgrund` | string | Der Transaktionsgrund beschreibt den Geschäftsvorfall zur Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | — |
| <a id="transaktionsgrundergaenzung"></a>`transaktionsgrundergaenzung` | string | Ergänzung zum Transaktionsgrund / UTILMD STS+7++E01+###+E03 | — |
| <a id="transaktionsgrundergaenzungbefristeteanmeldung"></a>`transaktionsgrundergaenzungBefristeteAnmeldung` | string | Ergänzung zum Transaktionsgrund bei befristeten An-/Abmeldungen / UTILMD STS+7++E01+ZW4+### | — |
| <a id="lieferrichtung"></a>`lieferrichtung` | string | Gibt an, ob es Erzeugung oder Verbrauch ist / UTILMD CCI+Z30 / ORDERS IMD++Z14 | — |
| <a id="prozessdatum"></a>`prozessdatum` | string (date-time) | Wird intern erzeugt - OBSOLET | — |
| <a id="vorgangsnummer"></a>`vorgangsnummer` | string | Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC | — |
| <a id="idempodenzschluessel"></a>`idempodenzschluessel` | string | Imempodenzschlüssel des Requests | — |
| <a id="pruefidentifikator"></a>`pruefidentifikator` | string | Enthält den Prüfidentifikator aus der EDIFact Kommunikation / RFF+Z13 | 105 (inline) |
| <a id="absender"></a>`absender` | [Marktteilnehmer](/bo4e/202604/bo/Marktteilnehmer) | Marktteilnehmer, der die Nachricht verschickt hat / NAD+MS | — |
| <a id="empfaenger"></a>`empfaenger` | [Marktteilnehmer](/bo4e/202604/bo/Marktteilnehmer) | Marktteilnehmer, der die Nachricht empfangen hat / NAD+MR | — |
| <a id="dokumentennummer"></a>`dokumentennummer` | string | EDIFact Referenz aus dem BGM Segment / BGM | — |
| <a id="dokumentenname"></a>`dokumentenname` | string | Alter FW - OBSOLET | — |
| <a id="kategorie"></a>`kategorie` | string | Qualifier aus dem Beginn der EDIFact Nachricht / BGM | — |
| <a id="nachrichtenfunktion"></a>`nachrichtenfunktion` | string | Nachrichtenfunktionskennzeichen / BGM | — |
| <a id="nachrichtendatum"></a>`nachrichtendatum` | string (date-time) | Erstellungdatum der EDIFact / DTM+137 | — |
| <a id="nachrichtenreferenznummer"></a>`nachrichtenreferenznummer` | string | EDIFact Referenz aus dem UNT Segment / UTILMD UNT+21 | — |
| <a id="anfragereferenznummer"></a>`anfragereferenznummer` | string | Referenz Vorgangsnummer 'aus Anfragenachricht' / ORDERS RFF+TN / IFTSTA RFF+AAV / INSRPT RFF+TN RFF+AAV | — |
| <a id="vorgangsreferenznummer"></a>`vorgangsreferenznummer` | string | Referenznummer des Vorgangs der Anmeldung nach WiM / ORDERS RFF+Z41 / IFTSTA RFF+ACW | — |
| <a id="sendungsposition"></a>`sendungsposition` | string | Sendungsposition / GID | — |
| <a id="positionsnummer"></a>`positionsnummer` | integer | Positionsnummer / LIN | — |
| <a id="mitteilungsnummer"></a>`mitteilungsnummer` | string | Referenz Vorgangsnummer / RFF+ADY | — |
| <a id="netznutzungsabrechnungsintervall"></a>`netznutzungsabrechnungsintervall` | string | Alter FW - OBSOLET | — |
| <a id="typ"></a>`typ` | string | Alter FW - OBSOLET | — |
| <a id="anfragereferenz"></a>`anfrageReferenz` | string | Beantragungsnummer / RFF+AGI | — |
| <a id="auftragsreferenz"></a>`auftragsReferenz` | string | Auftragsnummer 'Einkauf' / RFF+ON | — |
| <a id="vertragsbeginn"></a>`vertragsbeginn` | string (date-time) | Datum Vertragsbeginn / DTM+92 | — |
| <a id="vertragsende"></a>`vertragsende` | string (date-time) | Datum Vertragsende / DTM+93 | — |
| <a id="ausfuehrungsdatum"></a>`ausfuehrungsdatum` | string (date-time) | Ausführungsdatum/-zeit / DTM+203 DTM+469 | — |
| <a id="lieferdatum"></a>`lieferdatum` | string (date-time) | Lieferdatum DTM+76 | — |
| <a id="meldepunkt"></a>`meldepunkt` | string | Alter FW - OBSOLET | — |
| <a id="startdatum"></a>`startdatum` | string (date-time) | Startdatum oder -zeitpunkt, frühestes/r / DTM+469 | — |
| <a id="enddatum"></a>`enddatum` | string (date-time) | Endedatum oder -zeitpunkt, spätestes/r / DTM+472 | — |
| <a id="verwendungab"></a>`verwendungAb` | string (date-time) | Verarbeitung, Beginndatum/-zeit / DTM+163 | — |
| <a id="verwendungbis"></a>`verwendungBis` | string (date-time) | Verarbeitung, Endedatum/-zeit / DTM+164 | — |
| <a id="leistungsperiode"></a>`leistungsperiode` | string | Leistungsperiode / DTM+306 | — |
| <a id="abonnement"></a>`abonnement` | string | Alter FW - OBSOLET | — |
| <a id="produktbeschreibung"></a>`produktbeschreibung` | string | Alter FW - OBSOLET | — |
| <a id="bestellungzaehlzeiten"></a>`bestellungzaehlzeiten` | string | Alter FW - OBSOLET | — |
| <a id="angebotsnummer"></a>`angebotsnummer` | string | Angebotsnummer / RFF+AAG | — |
| <a id="angebotsreferenz"></a>`angebotsreferenz` | string | Referenznummer einer vorangegangenen Nachricht / ORDERS RFF+ACW | — |
| <a id="naechstenetznutzungsabrechnung"></a>`naechsteNetznutzungsabrechnung` | string | Alter FW - OBSOLET | — |
| <a id="naechsteturnusablesungstrom"></a>`naechsteTurnusAblesungStrom` | string | Alter FW - OBSOLET | — |
| <a id="naechsteturnusablesunggas"></a>`naechsteTurnusAblesungGas` | string | Alter FW - OBSOLET | — |
| <a id="identifikationslogik"></a>`identifikationslogik` | string | Alter FW - OBSOLET | — |
| <a id="datumsformat"></a>`datumsformat` | string | Alter FW - OBSOLET | — |
| <a id="antwortstatus"></a>`antwortstatus` | string | Antwortstatus / STS+E01 | — |
| <a id="antwortstatuscodeliste"></a>`antwortstatusCodeliste` | string | Antwortstatus Codeliste / STS+E01 | — |
| <a id="antwortstatusdritter"></a>`antwortstatusdritter` | string | Antwortstatus / STS+Z35 | — |
| <a id="antwortstatusdritterbetroffenelokation"></a>`antwortstatusdritterBetroffeneLokation` | string | Antwortstatus Lokation / STS+Z35 | — |
| <a id="antwortstatusdrittercodeliste"></a>`antwortstatusdritterCodeliste` | string | Antwortstatus Codeliste / STS+Z35 | — |
| <a id="antwortstatusdritterreferenz"></a>`antwortstatusdritterReferenz` | string | Antwortstatus Referenz / STS+Z35 | — |
| <a id="beteiligtermarktpartner"></a>`beteiligterMarktpartner` | [Marktteilnehmer](/bo4e/202604/bo/Marktteilnehmer) | MP-ID des beteiligten Marktteilnehmers / ORDERS NAD+VY NAD+DDM / APERAK RFF+Z08 | — |
| <a id="beteiligtermarktpartnerreferenz"></a>`beteiligterMarktpartnerReferenz` | string | Alter FW - OBSOLET | — |
| <a id="beteiligtermarktpartnerreferenzcode"></a>`beteiligterMarktpartnerReferenzcode` | string | Alter FW - OBSOLET | — |
| <a id="freitext"></a>`freitext` | string | Freitext / FTX+ACB | — |
| <a id="fehlerbeschreibung"></a>`fehlerbeschreibung` | string | Alter FW - OBSOLET | — |
| <a id="begruendung"></a>`begruendung` | string | Alter FW - OBSOLET | — |
| <a id="infoabweichung"></a>`infoAbweichung` | string | Freitext Abweichung / FTX+ABO | — |
| <a id="ergaenztemarktlokation"></a>`ergaenzteMarktlokation` | boolean | Ergänzende Marktlokation im Freitext / FTX+ABO | — |
| <a id="zaehlerstandsinfo"></a>`zaehlerstandsinfo` | boolean | Ankündigung, dass per MSCONS noch der Zählerstand übermittelt wird / FTX+ADM | — |
| <a id="lokationsid"></a>`lokationsId` | string | Referenz auf die Lokation / LOC | — |
| <a id="lokationstyp"></a>`lokationsTyp` | [Enum Lokationstyp](/bo4e/202604/enum/Lokationstyp)<br/><Werte>`MALO`, `MELO`, `NELO`, `TECHNISCHE_RESSOURCE`, `STEUERBARE_RESSOURCE`, `TRANCHE`, `MABIS_ZAEHLPUNKT`</Werte> | Typ der Lokation | — |
| <a id="referenzmalo"></a>`referenzMalo` | string | Marktlokation Referenz / RFF+AVE | — |
| <a id="referenzmelo"></a>`referenzMelo` | string | Messlokation Referenz / RFF+Z21 | — |
| <a id="referenzpreisschluesselstamm"></a>`referenzPreisschluesselstamm` | string | Preisschlüsselstamm Referenz / RFF+Z17 | — |
| <a id="datumleistungsbeginn"></a>`datumleistungsbeginn` | string (date-time) | Datum zum geplanten Leistungsbeginn / DTM+76 | — |
| <a id="endezumtermin"></a>`endezumtermin` | string (date-time) | Kündigungsdatum / DTM+471 | — |
| <a id="naechstebearbeitung"></a>`naechsteBearbeitung` | string (date-time) | Datum für nächste Bearbeitung / DTM+Z08 | — |
| <a id="lieferbeginndatuminbearbeitung"></a>`lieferbeginndatuminbearbeitung` | string (date-time) | Lieferbeginndatum in Bearbeitung / DTM+Z07 | — |
| <a id="angebotsart"></a>`angebotsart` | string | Alter FW - OBSOLET | — |
| <a id="menge"></a>`menge` | [Menge](/bo4e/202604/com/Menge) | Menge / QTY | — |
| <a id="tarifstufe"></a>`tarifstufe` | [Enum Tarifstufe](/bo4e/202604/enum/Tarifstufe)<br/><Werte>`TARIFSTUFE_0`, `TARIFSTUFE_1`, `TARIFSTUFE_2`, `TARIFSTUFE_3`, `TARIFSTUFE_4`, `TARIFSTUFE_5`, `TARIFSTUFE_6`, `TARIFSTUFE_7`, `TARIFSTUFE_8`, `TARIFSTUFE_9`</Werte> | Tarifstufe / QTY | — |
| <a id="bilanzkreiszuordnung"></a>`bilanzkreiszuordnung` | [Enum Bilanzkreiszuordnung](/bo4e/202604/enum/Bilanzkreiszuordnung)<br/><Werte>`ERFOLGREICH`, `GESCHEITERT`</Werte> | Status der Bilanzkreiszuordnung / STS+Z18 | — |
| <a id="anwendungsreferenznummer"></a>`anwendungsreferenznummer` | string | Anwendungsreferenznummer / RFF+AGK | — |
| <a id="fertigstellungsdatum"></a>`fertigstellungsdatum` | string (date-time) | Fertigstellungsdatum / DTM+293 | — |
| <a id="datumuebergabe"></a>`datumuebergabe` | string (date-time) | Datum und Uhrzeit der Übergabe / DTM+294 | — |
| <a id="gueltigab"></a>`gueltigAb` | string (date-time) | Gültigkeitsdatum/-zeit / DTM+7 | — |
| <a id="ablesedatum"></a>`ablesedatum` | string (date-time) | tatsächliches Ablesedatum / DTM+9 | — |
| <a id="verarbeitungsreihenfolge"></a>`verarbeitungsReihenfolge` | string | Alte FW - OBSOLET | — |
| <a id="ansprechpartnerkunde"></a>`ansprechpartnerKunde` | [Ansprechpartner](/bo4e/202604/bo/Ansprechpartner) | Kontaktdaten des Kunden / ORDERS CTA+IC | — |
| <a id="statusveraenderungszeitpunkt"></a>`statusVeraenderungsZeitpunkt` | string (date-time) | Statusveränderung, Datum/Zeit / DTM+334 | — |
| <a id="gueltigkeitszeitspanne"></a>`gueltigkeitsZeitspanne` | string | Gültigkeitszeitspanne / DTM+273 | — |
| <a id="nachrichtenreferenzbestellbestaetigung"></a>`nachrichtenReferenzBestellbestaetigung` | string | Referenznummer der Nachricht der betroffenen Antwort auf Bestellung 'Bestellbestätigung' / ORDERS RFF+Z42 | — |
| <a id="vorgangsreferenzbestellbestaetigung"></a>`vorgangsReferenzBestellbestaetigung` | string | Referenznummer des Vorgangs der betroffenen Antwort auf Bestellung 'Bestellbestätigung' / ORDERS RFF+Z43 | — |
| <a id="datumkuendigungkd"></a>`datumKuendigungKd` | string (date-time) | Kündigungsdatum, was dem Kunden mitgeteilt worden ist / DTM+Z05 | — |
| <a id="datumkuendigunglf"></a>`datumKuendigungLf` | string (date-time) | Kündigungsdatum, was dem Lieferanten mitgeteilt worden ist / DTM+Z06 | — |
| <a id="referenzartikelid"></a>`referenzArtikelID` | string | Referenz auf die Artikel-ID / IFTSTA RFF+Z45 | — |
| <a id="bilanzkreis"></a>`bilanzkreis` | [Bilanzkreis[]](/bo4e/202604/bo/Bilanzkreis) | Angemeldete Bilanzkreise - nur Sparte Gas | — |
| <a id="geplantesproduktpaket"></a>`geplantesProduktpaket` | integer | Informativ zur Umsetzung geplantes Produktpaket / RFF+Z60 | — |
| <a id="abtretungserklaerung"></a>`abtretungserklaerung` | [Abtretungserklaerung](/bo4e/202604/com/Abtretungserklaerung) | Link zur Abtretungserklärung / Vollmacht vom Kunden / ORDERS FTX+Z13 | — |
| <a id="antwortstatuszeitraum"></a>`antwortStatusZeitraum` | [AntwortStatusZeitraum[]](/bo4e/202604/com/AntwortStatusZeitraum) | AntwortstatusZeitraumId aus STS Segment | — |
| <a id="apipath"></a>`apiPath` | string | Internetadresse des API-Webdienstes | — |
| <a id="apikennung"></a>`apiKennung` | string | Identifikator des fachlichen API-Webdienstes | — |
| <a id="annahmedatum"></a>`annahmedatum` | string (date-time) | Annahmedatum eines Dokument / DTM+154 | — |
| <a id="unboutbounddatum"></a>`unbOutboundDatum` | string | Datum und Uhrzeit in Format YYMMDDHHmm, zB 2508211435 für 2025-08-21 14:35 Uhr Systemzeit | — |
| <a id="geraeteausbaudatum"></a>`geraeteausbaudatum` | string (date-time) | Geräteausbaudatum / DTM+206 | — |
| <a id="listennummer"></a>`listennummer` | integer | Listennummer | — |
| <a id="profilbeschreibung"></a>`profilbeschreibung` | string | Profilbeschreibung | — |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[datenaustauschreferenz](/bo4e/202604/cdoc/Transaktionsdaten#datenaustauschreferenz)</span> | Enthält die eindeutige Datenaustauschreferenz der Nachricht, die in der EDIFact Kommunikation verwendet wird | string |
| <span className="hbs-f hbs-e0">[sparte](/bo4e/202604/cdoc/Transaktionsdaten#sparte)</span> | Enthält Informationen über die Sparte | [Enum Sparte](/bo4e/202604/enum/Sparte)<br/><Werte>`STROM`, `GAS`, `FERNWAERME`, `NAHWAERME`, `WASSER`, `ABWASSER`</Werte> |
| <span className="hbs-f hbs-e0">[transaktionsgrund](/bo4e/202604/cdoc/Transaktionsdaten#transaktionsgrund)</span> | Der Transaktionsgrund beschreibt den Geschäftsvorfall zur Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | string |
| <span className="hbs-f hbs-e0">[transaktionsgrundergaenzung](/bo4e/202604/cdoc/Transaktionsdaten#transaktionsgrundergaenzung)</span> | Ergänzung zum Transaktionsgrund / UTILMD STS+7++E01+###+E03 | string |
| <span className="hbs-f hbs-e0">[transaktionsgrundergaenzungBefristeteAnmeldung](/bo4e/202604/cdoc/Transaktionsdaten#transaktionsgrundergaenzungbefristeteanmeldung)</span> | Ergänzung zum Transaktionsgrund bei befristeten An-/Abmeldungen / UTILMD STS+7++E01+ZW4+### | string |
| <span className="hbs-f hbs-e0">[lieferrichtung](/bo4e/202604/cdoc/Transaktionsdaten#lieferrichtung)</span> | Gibt an, ob es Erzeugung oder Verbrauch ist / UTILMD CCI+Z30 / ORDERS IMD++Z14 | string |
| <span className="hbs-f hbs-e0">[prozessdatum](/bo4e/202604/cdoc/Transaktionsdaten#prozessdatum)</span> | Wird intern erzeugt - OBSOLET | string (date-time) |
| <span className="hbs-f hbs-e0">[vorgangsnummer](/bo4e/202604/cdoc/Transaktionsdaten#vorgangsnummer)</span> | Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC | string |
| <span className="hbs-f hbs-e0">[idempodenzschluessel](/bo4e/202604/cdoc/Transaktionsdaten#idempodenzschluessel)</span> | Imempodenzschlüssel des Requests | string |
| <span className="hbs-f hbs-e0">[pruefidentifikator](/bo4e/202604/cdoc/Transaktionsdaten#pruefidentifikator)</span> | Enthält den Prüfidentifikator aus der EDIFact Kommunikation / RFF+Z13 | string |
| <span className="hbs-g hbs-e0">[absender](/bo4e/202604/cdoc/Transaktionsdaten#absender)</span> | Marktteilnehmer, der die Nachricht verschickt hat / NAD+MS | [Marktteilnehmer](/bo4e/202604/bo/Marktteilnehmer) |
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
| <span className="hbs-g hbs-e0">[empfaenger](/bo4e/202604/cdoc/Transaktionsdaten#empfaenger)</span> | Marktteilnehmer, der die Nachricht empfangen hat / NAD+MR | [Marktteilnehmer](/bo4e/202604/bo/Marktteilnehmer) |
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
| <span className="hbs-f hbs-e0">[dokumentennummer](/bo4e/202604/cdoc/Transaktionsdaten#dokumentennummer)</span> | EDIFact Referenz aus dem BGM Segment / BGM | string |
| <span className="hbs-f hbs-e0">[dokumentenname](/bo4e/202604/cdoc/Transaktionsdaten#dokumentenname)</span> | Alter FW - OBSOLET | string |
| <span className="hbs-f hbs-e0">[kategorie](/bo4e/202604/cdoc/Transaktionsdaten#kategorie)</span> | Qualifier aus dem Beginn der EDIFact Nachricht / BGM | string |
| <span className="hbs-f hbs-e0">[nachrichtenfunktion](/bo4e/202604/cdoc/Transaktionsdaten#nachrichtenfunktion)</span> | Nachrichtenfunktionskennzeichen / BGM | string |
| <span className="hbs-f hbs-e0">[nachrichtendatum](/bo4e/202604/cdoc/Transaktionsdaten#nachrichtendatum)</span> | Erstellungdatum der EDIFact / DTM+137 | string (date-time) |
| <span className="hbs-f hbs-e0">[nachrichtenreferenznummer](/bo4e/202604/cdoc/Transaktionsdaten#nachrichtenreferenznummer)</span> | EDIFact Referenz aus dem UNT Segment / UTILMD UNT+21 | string |
| <span className="hbs-f hbs-e0">[anfragereferenznummer](/bo4e/202604/cdoc/Transaktionsdaten#anfragereferenznummer)</span> | Referenz Vorgangsnummer 'aus Anfragenachricht' / ORDERS RFF+TN / IFTSTA RFF+AAV / INSRPT RFF+TN RFF+AAV | string |
| <span className="hbs-f hbs-e0">[vorgangsreferenznummer](/bo4e/202604/cdoc/Transaktionsdaten#vorgangsreferenznummer)</span> | Referenznummer des Vorgangs der Anmeldung nach WiM / ORDERS RFF+Z41 / IFTSTA RFF+ACW | string |
| <span className="hbs-f hbs-e0">[sendungsposition](/bo4e/202604/cdoc/Transaktionsdaten#sendungsposition)</span> | Sendungsposition / GID | string |
| <span className="hbs-f hbs-e0">[positionsnummer](/bo4e/202604/cdoc/Transaktionsdaten#positionsnummer)</span> | Positionsnummer / LIN | integer |
| <span className="hbs-f hbs-e0">[mitteilungsnummer](/bo4e/202604/cdoc/Transaktionsdaten#mitteilungsnummer)</span> | Referenz Vorgangsnummer / RFF+ADY | string |
| <span className="hbs-f hbs-e0">[netznutzungsabrechnungsintervall](/bo4e/202604/cdoc/Transaktionsdaten#netznutzungsabrechnungsintervall)</span> | Alter FW - OBSOLET | string |
| <span className="hbs-f hbs-e0">[typ](/bo4e/202604/cdoc/Transaktionsdaten#typ)</span> | Alter FW - OBSOLET | string |
| <span className="hbs-f hbs-e0">[anfrageReferenz](/bo4e/202604/cdoc/Transaktionsdaten#anfragereferenz)</span> | Beantragungsnummer / RFF+AGI | string |
| <span className="hbs-f hbs-e0">[auftragsReferenz](/bo4e/202604/cdoc/Transaktionsdaten#auftragsreferenz)</span> | Auftragsnummer 'Einkauf' / RFF+ON | string |
| <span className="hbs-f hbs-e0">[vertragsbeginn](/bo4e/202604/cdoc/Transaktionsdaten#vertragsbeginn)</span> | Datum Vertragsbeginn / DTM+92 | string (date-time) |
| <span className="hbs-f hbs-e0">[vertragsende](/bo4e/202604/cdoc/Transaktionsdaten#vertragsende)</span> | Datum Vertragsende / DTM+93 | string (date-time) |
| <span className="hbs-f hbs-e0">[ausfuehrungsdatum](/bo4e/202604/cdoc/Transaktionsdaten#ausfuehrungsdatum)</span> | Ausführungsdatum/-zeit / DTM+203 DTM+469 | string (date-time) |
| <span className="hbs-f hbs-e0">[lieferdatum](/bo4e/202604/cdoc/Transaktionsdaten#lieferdatum)</span> | Lieferdatum DTM+76 | string (date-time) |
| <span className="hbs-f hbs-e0">[meldepunkt](/bo4e/202604/cdoc/Transaktionsdaten#meldepunkt)</span> | Alter FW - OBSOLET | string |
| <span className="hbs-f hbs-e0">[startdatum](/bo4e/202604/cdoc/Transaktionsdaten#startdatum)</span> | Startdatum oder -zeitpunkt, frühestes/r / DTM+469 | string (date-time) |
| <span className="hbs-f hbs-e0">[enddatum](/bo4e/202604/cdoc/Transaktionsdaten#enddatum)</span> | Endedatum oder -zeitpunkt, spätestes/r / DTM+472 | string (date-time) |
| <span className="hbs-f hbs-e0">[verwendungAb](/bo4e/202604/cdoc/Transaktionsdaten#verwendungab)</span> | Verarbeitung, Beginndatum/-zeit / DTM+163 | string (date-time) |
| <span className="hbs-f hbs-e0">[verwendungBis](/bo4e/202604/cdoc/Transaktionsdaten#verwendungbis)</span> | Verarbeitung, Endedatum/-zeit / DTM+164 | string (date-time) |
| <span className="hbs-f hbs-e0">[leistungsperiode](/bo4e/202604/cdoc/Transaktionsdaten#leistungsperiode)</span> | Leistungsperiode / DTM+306 | string |
| <span className="hbs-f hbs-e0">[abonnement](/bo4e/202604/cdoc/Transaktionsdaten#abonnement)</span> | Alter FW - OBSOLET | string |
| <span className="hbs-f hbs-e0">[produktbeschreibung](/bo4e/202604/cdoc/Transaktionsdaten#produktbeschreibung)</span> | Alter FW - OBSOLET | string |
| <span className="hbs-f hbs-e0">[bestellungzaehlzeiten](/bo4e/202604/cdoc/Transaktionsdaten#bestellungzaehlzeiten)</span> | Alter FW - OBSOLET | string |
| <span className="hbs-f hbs-e0">[angebotsnummer](/bo4e/202604/cdoc/Transaktionsdaten#angebotsnummer)</span> | Angebotsnummer / RFF+AAG | string |
| <span className="hbs-f hbs-e0">[angebotsreferenz](/bo4e/202604/cdoc/Transaktionsdaten#angebotsreferenz)</span> | Referenznummer einer vorangegangenen Nachricht / ORDERS RFF+ACW | string |
| <span className="hbs-f hbs-e0">[naechsteNetznutzungsabrechnung](/bo4e/202604/cdoc/Transaktionsdaten#naechstenetznutzungsabrechnung)</span> | Alter FW - OBSOLET | string |
| <span className="hbs-f hbs-e0">[naechsteTurnusAblesungStrom](/bo4e/202604/cdoc/Transaktionsdaten#naechsteturnusablesungstrom)</span> | Alter FW - OBSOLET | string |
| <span className="hbs-f hbs-e0">[naechsteTurnusAblesungGas](/bo4e/202604/cdoc/Transaktionsdaten#naechsteturnusablesunggas)</span> | Alter FW - OBSOLET | string |
| <span className="hbs-f hbs-e0">[identifikationslogik](/bo4e/202604/cdoc/Transaktionsdaten#identifikationslogik)</span> | Alter FW - OBSOLET | string |
| <span className="hbs-f hbs-e0">[datumsformat](/bo4e/202604/cdoc/Transaktionsdaten#datumsformat)</span> | Alter FW - OBSOLET | string |
| <span className="hbs-f hbs-e0">[antwortstatus](/bo4e/202604/cdoc/Transaktionsdaten#antwortstatus)</span> | Antwortstatus / STS+E01 | string |
| <span className="hbs-f hbs-e0">[antwortstatusCodeliste](/bo4e/202604/cdoc/Transaktionsdaten#antwortstatuscodeliste)</span> | Antwortstatus Codeliste / STS+E01 | string |
| <span className="hbs-f hbs-e0">[antwortstatusdritter](/bo4e/202604/cdoc/Transaktionsdaten#antwortstatusdritter)</span> | Antwortstatus / STS+Z35 | string |
| <span className="hbs-f hbs-e0">[antwortstatusdritterBetroffeneLokation](/bo4e/202604/cdoc/Transaktionsdaten#antwortstatusdritterbetroffenelokation)</span> | Antwortstatus Lokation / STS+Z35 | string |
| <span className="hbs-f hbs-e0">[antwortstatusdritterCodeliste](/bo4e/202604/cdoc/Transaktionsdaten#antwortstatusdrittercodeliste)</span> | Antwortstatus Codeliste / STS+Z35 | string |
| <span className="hbs-f hbs-e0">[antwortstatusdritterReferenz](/bo4e/202604/cdoc/Transaktionsdaten#antwortstatusdritterreferenz)</span> | Antwortstatus Referenz / STS+Z35 | string |
| <span className="hbs-g hbs-e0">[beteiligterMarktpartner](/bo4e/202604/cdoc/Transaktionsdaten#beteiligtermarktpartner)</span> | MP-ID des beteiligten Marktteilnehmers / ORDERS NAD+VY NAD+DDM / APERAK RFF+Z08 | [Marktteilnehmer](/bo4e/202604/bo/Marktteilnehmer) |
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
| <span className="hbs-f hbs-e0">[beteiligterMarktpartnerReferenz](/bo4e/202604/cdoc/Transaktionsdaten#beteiligtermarktpartnerreferenz)</span> | Alter FW - OBSOLET | string |
| <span className="hbs-f hbs-e0">[beteiligterMarktpartnerReferenzcode](/bo4e/202604/cdoc/Transaktionsdaten#beteiligtermarktpartnerreferenzcode)</span> | Alter FW - OBSOLET | string |
| <span className="hbs-f hbs-e0">[freitext](/bo4e/202604/cdoc/Transaktionsdaten#freitext)</span> | Freitext / FTX+ACB | string |
| <span className="hbs-f hbs-e0">[fehlerbeschreibung](/bo4e/202604/cdoc/Transaktionsdaten#fehlerbeschreibung)</span> | Alter FW - OBSOLET | string |
| <span className="hbs-f hbs-e0">[begruendung](/bo4e/202604/cdoc/Transaktionsdaten#begruendung)</span> | Alter FW - OBSOLET | string |
| <span className="hbs-f hbs-e0">[infoAbweichung](/bo4e/202604/cdoc/Transaktionsdaten#infoabweichung)</span> | Freitext Abweichung / FTX+ABO | string |
| <span className="hbs-f hbs-e0">[ergaenzteMarktlokation](/bo4e/202604/cdoc/Transaktionsdaten#ergaenztemarktlokation)</span> | Ergänzende Marktlokation im Freitext / FTX+ABO | boolean |
| <span className="hbs-f hbs-e0">[zaehlerstandsinfo](/bo4e/202604/cdoc/Transaktionsdaten#zaehlerstandsinfo)</span> | Ankündigung, dass per MSCONS noch der Zählerstand übermittelt wird / FTX+ADM | boolean |
| <span className="hbs-f hbs-e0">[lokationsId](/bo4e/202604/cdoc/Transaktionsdaten#lokationsid)</span> | Referenz auf die Lokation / LOC | string |
| <span className="hbs-f hbs-e0">[lokationsTyp](/bo4e/202604/cdoc/Transaktionsdaten#lokationstyp)</span> | Typ der Lokation | [Enum Lokationstyp](/bo4e/202604/enum/Lokationstyp)<br/><Werte>`MALO`, `MELO`, `NELO`, `TECHNISCHE_RESSOURCE`, `STEUERBARE_RESSOURCE`, `TRANCHE`, `MABIS_ZAEHLPUNKT`</Werte> |
| <span className="hbs-f hbs-e0">[referenzMalo](/bo4e/202604/cdoc/Transaktionsdaten#referenzmalo)</span> | Marktlokation Referenz / RFF+AVE | string |
| <span className="hbs-f hbs-e0">[referenzMelo](/bo4e/202604/cdoc/Transaktionsdaten#referenzmelo)</span> | Messlokation Referenz / RFF+Z21 | string |
| <span className="hbs-f hbs-e0">[referenzPreisschluesselstamm](/bo4e/202604/cdoc/Transaktionsdaten#referenzpreisschluesselstamm)</span> | Preisschlüsselstamm Referenz / RFF+Z17 | string |
| <span className="hbs-f hbs-e0">[datumleistungsbeginn](/bo4e/202604/cdoc/Transaktionsdaten#datumleistungsbeginn)</span> | Datum zum geplanten Leistungsbeginn / DTM+76 | string (date-time) |
| <span className="hbs-f hbs-e0">[endezumtermin](/bo4e/202604/cdoc/Transaktionsdaten#endezumtermin)</span> | Kündigungsdatum / DTM+471 | string (date-time) |
| <span className="hbs-f hbs-e0">[naechsteBearbeitung](/bo4e/202604/cdoc/Transaktionsdaten#naechstebearbeitung)</span> | Datum für nächste Bearbeitung / DTM+Z08 | string (date-time) |
| <span className="hbs-f hbs-e0">[lieferbeginndatuminbearbeitung](/bo4e/202604/cdoc/Transaktionsdaten#lieferbeginndatuminbearbeitung)</span> | Lieferbeginndatum in Bearbeitung / DTM+Z07 | string (date-time) |
| <span className="hbs-f hbs-e0">[angebotsart](/bo4e/202604/cdoc/Transaktionsdaten#angebotsart)</span> | Alter FW - OBSOLET | string |
| <span className="hbs-g hbs-e0">[menge](/bo4e/202604/cdoc/Transaktionsdaten#menge)</span> | Menge / QTY | [Menge](/bo4e/202604/com/Menge) |
| <span className="hbs-f hbs-e1">[wert](/bo4e/202604/com/Menge#wert)</span> | Wert | number (float) |
| <span className="hbs-f hbs-e1">[einheit](/bo4e/202604/com/Menge#einheit)</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202604/enum/Mengeneinheit)<br/><Werte>`W`, `WH`, `KW`, `KWH`, `KVARH`, `MW`, `MWH`, `STUECK`, `KUBIKMETER`, `STUNDE`, `TAG`, `MONAT`, `JAHR`, `PROZENT`, `ANZAHL`, `VAR`, `KVAR`, `VARH`, `KWHK`, `Z16`, `KWT`, `WATT_PRO_QUADRATMETER`, `METER_PRO_SEKUNDE`</Werte> |
| <span className="hbs-f hbs-e1">[startdatum](/bo4e/202604/com/Menge#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e1">[enddatum](/bo4e/202604/com/Menge#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-f hbs-e0">[tarifstufe](/bo4e/202604/cdoc/Transaktionsdaten#tarifstufe)</span> | Tarifstufe / QTY | [Enum Tarifstufe](/bo4e/202604/enum/Tarifstufe)<br/><Werte>`TARIFSTUFE_0`, `TARIFSTUFE_1`, `TARIFSTUFE_2`, `TARIFSTUFE_3`, `TARIFSTUFE_4`, `TARIFSTUFE_5`, `TARIFSTUFE_6`, `TARIFSTUFE_7`, `TARIFSTUFE_8`, `TARIFSTUFE_9`</Werte> |
| <span className="hbs-f hbs-e0">[bilanzkreiszuordnung](/bo4e/202604/cdoc/Transaktionsdaten#bilanzkreiszuordnung)</span> | Status der Bilanzkreiszuordnung / STS+Z18 | [Enum Bilanzkreiszuordnung](/bo4e/202604/enum/Bilanzkreiszuordnung)<br/><Werte>`ERFOLGREICH`, `GESCHEITERT`</Werte> |
| <span className="hbs-f hbs-e0">[anwendungsreferenznummer](/bo4e/202604/cdoc/Transaktionsdaten#anwendungsreferenznummer)</span> | Anwendungsreferenznummer / RFF+AGK | string |
| <span className="hbs-f hbs-e0">[fertigstellungsdatum](/bo4e/202604/cdoc/Transaktionsdaten#fertigstellungsdatum)</span> | Fertigstellungsdatum / DTM+293 | string (date-time) |
| <span className="hbs-f hbs-e0">[datumuebergabe](/bo4e/202604/cdoc/Transaktionsdaten#datumuebergabe)</span> | Datum und Uhrzeit der Übergabe / DTM+294 | string (date-time) |
| <span className="hbs-f hbs-e0">[gueltigAb](/bo4e/202604/cdoc/Transaktionsdaten#gueltigab)</span> | Gültigkeitsdatum/-zeit / DTM+7 | string (date-time) |
| <span className="hbs-f hbs-e0">[ablesedatum](/bo4e/202604/cdoc/Transaktionsdaten#ablesedatum)</span> | tatsächliches Ablesedatum / DTM+9 | string (date-time) |
| <span className="hbs-f hbs-e0">[verarbeitungsReihenfolge](/bo4e/202604/cdoc/Transaktionsdaten#verarbeitungsreihenfolge)</span> | Alte FW - OBSOLET | string |
| <span className="hbs-g hbs-e0">[ansprechpartnerKunde](/bo4e/202604/cdoc/Transaktionsdaten#ansprechpartnerkunde)</span> | Kontaktdaten des Kunden / ORDERS CTA+IC | [Ansprechpartner](/bo4e/202604/bo/Ansprechpartner) |
| <span className="hbs-f hbs-e1">[boTyp](/bo4e/202604/bo/Ansprechpartner#botyp) <span className="hbs-pflicht">\*</span></span> | Typ des BO | [Enum BOTyp](/bo4e/202604/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> |
| <span className="hbs-f hbs-e1">[versionStruktur](/bo4e/202604/bo/Ansprechpartner#versionstruktur) <span className="hbs-pflicht">\*</span></span> | versionStruktur | string |
| <span className="hbs-f hbs-e1">[nachname](/bo4e/202604/bo/Ansprechpartner#nachname)</span> | Nachname (Familienname) des Ansprechpartners | string |
| <span className="hbs-f hbs-e1">[eMailAdresse](/bo4e/202604/bo/Ansprechpartner#emailadresse)</span> | E-Mail Adresse | string |
| <span className="hbs-g hbs-e1">[rufnummern](/bo4e/202604/bo/Ansprechpartner#rufnummern) <span className="hbs-liste">[ ]</span></span> | Liste der Telefonnummern, unter denen der Ansprechpartner erreichbar ist. | [Rufnummer[]](/bo4e/202604/com/Rufnummer) |
| <span className="hbs-f hbs-e2">[nummerntyp](/bo4e/202604/com/Rufnummer#nummerntyp)</span> | Rufnummernart | [Enum Rufnummernart](/bo4e/202604/enum/Rufnummernart)<br/><Werte>`RUF_ZENTRALE`, `FAX_ZENTRALE`, `SAMMELRUF`, `SAMMELFAX`, `ABTEILUNGRUF`, `ABTEILUNGFAX`, `RUF_DURCHWAHL`, `FAX_DURCHWAHL`, `MOBIL_NUMMER`</Werte> |
| <span className="hbs-f hbs-e2">[rufnummer](/bo4e/202604/com/Rufnummer#rufnummer)</span> | rufnummer | string |
| <span className="hbs-f hbs-e0">[statusVeraenderungsZeitpunkt](/bo4e/202604/cdoc/Transaktionsdaten#statusveraenderungszeitpunkt)</span> | Statusveränderung, Datum/Zeit / DTM+334 | string (date-time) |
| <span className="hbs-f hbs-e0">[gueltigkeitsZeitspanne](/bo4e/202604/cdoc/Transaktionsdaten#gueltigkeitszeitspanne)</span> | Gültigkeitszeitspanne / DTM+273 | string |
| <span className="hbs-f hbs-e0">[nachrichtenReferenzBestellbestaetigung](/bo4e/202604/cdoc/Transaktionsdaten#nachrichtenreferenzbestellbestaetigung)</span> | Referenznummer der Nachricht der betroffenen Antwort auf Bestellung 'Bestellbestätigung' / ORDERS RFF+Z42 | string |
| <span className="hbs-f hbs-e0">[vorgangsReferenzBestellbestaetigung](/bo4e/202604/cdoc/Transaktionsdaten#vorgangsreferenzbestellbestaetigung)</span> | Referenznummer des Vorgangs der betroffenen Antwort auf Bestellung 'Bestellbestätigung' / ORDERS RFF+Z43 | string |
| <span className="hbs-f hbs-e0">[datumKuendigungKd](/bo4e/202604/cdoc/Transaktionsdaten#datumkuendigungkd)</span> | Kündigungsdatum, was dem Kunden mitgeteilt worden ist / DTM+Z05 | string (date-time) |
| <span className="hbs-f hbs-e0">[datumKuendigungLf](/bo4e/202604/cdoc/Transaktionsdaten#datumkuendigunglf)</span> | Kündigungsdatum, was dem Lieferanten mitgeteilt worden ist / DTM+Z06 | string (date-time) |
| <span className="hbs-f hbs-e0">[referenzArtikelID](/bo4e/202604/cdoc/Transaktionsdaten#referenzartikelid)</span> | Referenz auf die Artikel-ID / IFTSTA RFF+Z45 | string |
| <span className="hbs-g hbs-e0">[bilanzkreis](/bo4e/202604/cdoc/Transaktionsdaten#bilanzkreis) <span className="hbs-liste">[ ]</span></span> | Angemeldete Bilanzkreise - nur Sparte Gas | [Bilanzkreis[]](/bo4e/202604/bo/Bilanzkreis) |
| <span className="hbs-f hbs-e0">[geplantesProduktpaket](/bo4e/202604/cdoc/Transaktionsdaten#geplantesproduktpaket)</span> | Informativ zur Umsetzung geplantes Produktpaket / RFF+Z60 | integer |
| <span className="hbs-g hbs-e0">[abtretungserklaerung](/bo4e/202604/cdoc/Transaktionsdaten#abtretungserklaerung)</span> | Link zur Abtretungserklärung / Vollmacht vom Kunden / ORDERS FTX+Z13 | [Abtretungserklaerung](/bo4e/202604/com/Abtretungserklaerung) |
| <span className="hbs-f hbs-e1">[passwort](/bo4e/202604/com/Abtretungserklaerung#passwort)</span> | Passwort zum Abruf | string |
| <span className="hbs-f hbs-e1">[link1](/bo4e/202604/com/Abtretungserklaerung#link1)</span> | Link Zeile 1 | string |
| <span className="hbs-f hbs-e1">[link2](/bo4e/202604/com/Abtretungserklaerung#link2)</span> | Link Zeile 2 | string |
| <span className="hbs-f hbs-e1">[link3](/bo4e/202604/com/Abtretungserklaerung#link3)</span> | Link Zeile 3 | string |
| <span className="hbs-f hbs-e1">[link4](/bo4e/202604/com/Abtretungserklaerung#link4)</span> | Link Zeile 4 | string |
| <span className="hbs-f hbs-e1">[link5](/bo4e/202604/com/Abtretungserklaerung#link5)</span> | Link Zeile 5 | string |
| <span className="hbs-g hbs-e0">[antwortStatusZeitraum](/bo4e/202604/cdoc/Transaktionsdaten#antwortstatuszeitraum) <span className="hbs-liste">[ ]</span></span> | AntwortstatusZeitraumId aus STS Segment | [AntwortStatusZeitraum[]](/bo4e/202604/com/AntwortStatusZeitraum) |
| <span className="hbs-f hbs-e1">[code](/bo4e/202604/com/AntwortStatusZeitraum#code)</span> | code | string |
| <span className="hbs-f hbs-e1">[liste](/bo4e/202604/com/AntwortStatusZeitraum#liste)</span> | liste | string |
| <span className="hbs-f hbs-e1">[zeitraumId](/bo4e/202604/com/AntwortStatusZeitraum#zeitraumid)</span> | zeitraumId | integer |
| <span className="hbs-f hbs-e1">[freitext](/bo4e/202604/com/AntwortStatusZeitraum#freitext)</span> | — | string |
| <span className="hbs-f hbs-e0">[apiPath](/bo4e/202604/cdoc/Transaktionsdaten#apipath)</span> | Internetadresse des API-Webdienstes | string |
| <span className="hbs-f hbs-e0">[apiKennung](/bo4e/202604/cdoc/Transaktionsdaten#apikennung)</span> | Identifikator des fachlichen API-Webdienstes | string |
| <span className="hbs-f hbs-e0">[annahmedatum](/bo4e/202604/cdoc/Transaktionsdaten#annahmedatum)</span> | Annahmedatum eines Dokument / DTM+154 | string (date-time) |
| <span className="hbs-f hbs-e0">[unbOutboundDatum](/bo4e/202604/cdoc/Transaktionsdaten#unboutbounddatum)</span> | Datum und Uhrzeit in Format YYMMDDHHmm, zB 2508211435 für 2025-08-21 14:35 Uhr Systemzeit | string |
| <span className="hbs-f hbs-e0">[geraeteausbaudatum](/bo4e/202604/cdoc/Transaktionsdaten#geraeteausbaudatum)</span> | Geräteausbaudatum / DTM+206 | string (date-time) |
| <span className="hbs-f hbs-e0">[listennummer](/bo4e/202604/cdoc/Transaktionsdaten#listennummer)</span> | Listennummer | integer |
| <span className="hbs-f hbs-e0">[profilbeschreibung](/bo4e/202604/cdoc/Transaktionsdaten#profilbeschreibung)</span> | Profilbeschreibung | string |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### sparte

88 Verwendung(en).

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [[LF] START_ANFORDERUNG_VON_WERTEN](/schnittstellen/202604/trigger/events/LF-START_ANFORDERUNG_VON_WERTEN) | Event | — | transaktionsdaten |
| [[LF] START_ANFRAGE_KONFIGURATION](/schnittstellen/202604/trigger/events/LF-START_ANFRAGE_KONFIGURATION) | Event | — | transaktionsdaten |
| [[LF] START_ANFRAGE_MESSWERTE](/schnittstellen/202604/trigger/events/LF-START_ANFRAGE_MESSWERTE) | Event | — | transaktionsdaten |
| [[LF] START_ANFRAGE_SPERRUNG](/schnittstellen/202604/trigger/events/LF-START_ANFRAGE_SPERRUNG) | Event | — | transaktionsdaten |
| [[LF] START_ANFRAGE_STAMMDATENAENDERUNG GAS](/schnittstellen/202604/trigger/events/LF-START_ANFRAGE_STAMMDATENAENDERUNG-GAS) | Event | — | transaktionsdaten |
| [[LF] START_ANFRAGE_STAMMDATEN_MALO](/schnittstellen/202604/trigger/events/LF-START_ANFRAGE_STAMMDATEN_MALO) | Event | — | transaktionsdaten |
| [[LF] START_ANFRAGE_STAMMDATEN_TRANCHE](/schnittstellen/202604/trigger/events/LF-START_ANFRAGE_STAMMDATEN_TRANCHE) | Event | — | transaktionsdaten |
| [[LF] START_ANF_BRENNW_ZUSTANDSZAHL](/schnittstellen/202604/trigger/events/LF-START_ANF_BRENNW_ZUSTANDSZAHL) | Event | — | transaktionsdaten |
| [[LF] START_BESTELLUNG_ABRECHNUNGSDATEN](/schnittstellen/202604/trigger/events/LF-START_BESTELLUNG_ABRECHNUNGSDATEN) | Event | — | transaktionsdaten |
| [[LF] START_BESTELLUNG_ANGEBOT_KONFIGURATION](/schnittstellen/202604/trigger/events/LF-START_BESTELLUNG_ANGEBOT_KONFIGURATION) | Event | — | transaktionsdaten |
| [[LF] START_BESTELLUNG_KONFIGURATION](/schnittstellen/202604/trigger/events/LF-START_BESTELLUNG_KONFIGURATION) | Event | — | transaktionsdaten |
| [[LF] START_BESTELLUNG_SDAE](/schnittstellen/202604/trigger/events/LF-START_BESTELLUNG_SDAE) | Event | — | transaktionsdaten |
| [[LF] START_BESTELLUNG_ZAEHLZEITDEFINITION](/schnittstellen/202604/trigger/events/LF-START_BESTELLUNG_ZAEHLZEITDEFINITION) | Event | — | transaktionsdaten |
| [[LF] START_BEST_AEND_TK](/schnittstellen/202604/trigger/events/LF-START_BEST_AEND_TK) | Event | — | transaktionsdaten |
| [[LF] START_ENTSPERRAUFTRAG](/schnittstellen/202604/trigger/events/LF-START_ENTSPERRAUFTRAG) | Event | — | transaktionsdaten |
| [[LF] START_ERHEBUNG_MESSWERTE](/schnittstellen/202604/trigger/events/LF-START_ERHEBUNG_MESSWERTE) | Event | — | transaktionsdaten |
| [[LF] START_GESCHAEFTSDATENANFRAGE](/schnittstellen/202604/trigger/events/LF-START_GESCHAEFTSDATENANFRAGE) | Event | — | transaktionsdaten |
| [[LF] START_LIEFERBEGINN](/schnittstellen/202604/trigger/events/LF-START_LIEFERBEGINN) | Event | — | transaktionsdaten |
| [[LF] START_LIEFERENDE](/schnittstellen/202604/trigger/events/LF-START_LIEFERENDE) | Event | — | transaktionsdaten |
| [[LF] START_REKLAMATION_VON_WERTEN](/schnittstellen/202604/trigger/events/LF-START_REKLAMATION_VON_WERTEN) | Event | — | transaktionsdaten |
| [[LF] START_STORNO_AUFTRAG](/schnittstellen/202604/trigger/events/LF-START_STORNO_AUFTRAG) | Event | — | transaktionsdaten |
| [[LF] START_STORNO_SE_AUFTRAG](/schnittstellen/202604/trigger/events/LF-START_STORNO_SE_AUFTRAG) | Event | — | transaktionsdaten |
| [[LF] START_UEBERMITTLUNG_ENFG](/schnittstellen/202604/trigger/events/LF-START_UEBERMITTLUNG_ENFG) | Event | — | transaktionsdaten |
| [[LF] START_UEBERM_DEFINITION](/schnittstellen/202604/trigger/events/LF-START_UEBERM_DEFINITION) | Event | — | transaktionsdaten |
| [[LF] START_UEBERSICHT_LEISTUNGSKURVENDEF](/schnittstellen/202604/trigger/events/LF-START_UEBERSICHT_LEISTUNGSKURVENDEF) | Event | — | transaktionsdaten |
| [[LF] START_UEBERSICHT_SCHALTZEITDEF](/schnittstellen/202604/trigger/events/LF-START_UEBERSICHT_SCHALTZEITDEF) | Event | — | transaktionsdaten |
| [[LF] START_UEBERSICHT_ZAEHLZEITDEF](/schnittstellen/202604/trigger/events/LF-START_UEBERSICHT_ZAEHLZEITDEF) | Event | — | transaktionsdaten |
| [[LF] START_VERSAND_ANF_STORNO](/schnittstellen/202604/trigger/events/LF-START_VERSAND_ANF_STORNO) | Event | — | transaktionsdaten |
| [[LF] START_VERSAND_ANTWORT_NNA](/schnittstellen/202604/trigger/events/LF-START_VERSAND_ANTWORT_NNA) | Event | — | transaktionsdaten |
| [[LF] START_VERSAND_BEST_BEEND_KONFIG](/schnittstellen/202604/trigger/events/LF-START_VERSAND_BEST_BEEND_KONFIG) | Event | — | transaktionsdaten |
| [[LF] START_VERSAND_SDAE](/schnittstellen/202604/trigger/events/LF-START_VERSAND_SDAE) | Event | — | transaktionsdaten |
| [[LF] START_VERSAND_STOERUNGSMELDUNG](/schnittstellen/202604/trigger/events/LF-START_VERSAND_STOERUNGSMELDUNG) | Event | — | transaktionsdaten |
| [[LF] START_VERSAND_STORNO_MSCONS](/schnittstellen/202604/trigger/events/LF-START_VERSAND_STORNO_MSCONS) | Event | — | transaktionsdaten |
| [[MSB] START_ANGEBOT_GERAETEUEBERNAHME](/schnittstellen/202604/trigger/events/MSB-START_ANGEBOT_GERAETEUEBERNAHME) | Event | — | transaktionsdaten |
| [[MSB] START_ANTWORT_GERAETEWECHSEL](/schnittstellen/202604/trigger/events/MSB-START_ANTWORT_GERAETEWECHSEL) | Event | — | transaktionsdaten |
| [[MSB] START_BEGINN_MSB](/schnittstellen/202604/trigger/events/MSB-START_BEGINN_MSB) | Event | — | transaktionsdaten |
| [[MSB] START_BESTELLUNG_GERAETEUEBERNAHME](/schnittstellen/202604/trigger/events/MSB-START_BESTELLUNG_GERAETEUEBERNAHME) | Event | — | transaktionsdaten |
| [[MSB] START_BESTELLUNG_SDAE GAS](/schnittstellen/202604/trigger/events/MSB-START_BESTELLUNG_SDAE-GAS) | Event | — | transaktionsdaten |
| [[MSB] START_ERHEBUNG_MESSWERTE](/schnittstellen/202604/trigger/events/MSB-START_ERHEBUNG_MESSWERTE) | Event | — | transaktionsdaten |
| [[MSB] START_GERAETEUEBERNAHME](/schnittstellen/202604/trigger/events/MSB-START_GERAETEUEBERNAHME) | Event | — | transaktionsdaten |
| [[MSB] START_GERAETEWECHSEL](/schnittstellen/202604/trigger/events/MSB-START_GERAETEWECHSEL) | Event | — | transaktionsdaten |
| [[MSB] START_GESCHAEFTSDATENANFRAGE](/schnittstellen/202604/trigger/events/MSB-START_GESCHAEFTSDATENANFRAGE) | Event | — | transaktionsdaten |
| [[MSB] START_KUENDIGUNG_MSB](/schnittstellen/202604/trigger/events/MSB-START_KUENDIGUNG_MSB) | Event | — | transaktionsdaten |
| [[MSB] START_PARTIN](/schnittstellen/202604/trigger/events/MSB-START_PARTIN) | Event | — | transaktionsdaten |
| [[MSB] START_REKLAMATION_DEFINITION](/schnittstellen/202604/trigger/events/MSB-START_REKLAMATION_DEFINITION) | Event | — | transaktionsdaten |
| [[MSB] START_VERSAND_ANF_STORNO](/schnittstellen/202604/trigger/events/MSB-START_VERSAND_ANF_STORNO) | Event | — | transaktionsdaten |
| [[MSB] START_VERSAND_PREISBLATT_IMS](/schnittstellen/202604/trigger/events/MSB-START_VERSAND_PREISBLATT_IMS) | Event | — | transaktionsdaten |
| [[MSB] START_VERSAND_SDAE](/schnittstellen/202604/trigger/events/MSB-START_VERSAND_SDAE) | Event | — | transaktionsdaten |
| [[MSB] START_VERSAND_STORNO_MSCONS](/schnittstellen/202604/trigger/events/MSB-START_VERSAND_STORNO_MSCONS) | Event | — | transaktionsdaten |
| [[NB] START_ABR_BK](/schnittstellen/202604/trigger/events/NB-START_ABR_BK) | Event | — | transaktionsdaten |
| [[NB] START_ABR_NN](/schnittstellen/202604/trigger/events/NB-START_ABR_NN) | Event | — | transaktionsdaten |
| [[NB] START_ANFORDERUNG_MESSWERTE](/schnittstellen/202604/trigger/events/NB-START_ANFORDERUNG_MESSWERTE) | Event | — | transaktionsdaten |
| [[NB] START_ANFRAGE_MESSWERTE_NB](/schnittstellen/202604/trigger/events/NB-START_ANFRAGE_MESSWERTE_NB) | Event | — | transaktionsdaten |
| [[NB] START_ANFRAGE_SPERRUNG](/schnittstellen/202604/trigger/events/NB-START_ANFRAGE_SPERRUNG) | Event | — | transaktionsdaten |
| [[NB] START_ANFRAGE_STAMMDATENAENDERUNG GAS](/schnittstellen/202604/trigger/events/NB-START_ANFRAGE_STAMMDATENAENDERUNG-GAS) | Event | — | transaktionsdaten |
| [[NB] START_AUFH_ZUK_ZUORDNUNG](/schnittstellen/202604/trigger/events/NB-START_AUFH_ZUK_ZUORDNUNG) | Event | — | transaktionsdaten |
| [[NB] START_AUFTRAGSSTATUS](/schnittstellen/202604/trigger/events/NB-START_AUFTRAGSSTATUS) | Event | — | transaktionsdaten |
| [[NB] START_BERECHNUNGSFORMEL](/schnittstellen/202604/trigger/events/NB-START_BERECHNUNGSFORMEL) | Event | — | transaktionsdaten |
| [[NB] START_BESTELLUNG_SDAE](/schnittstellen/202604/trigger/events/NB-START_BESTELLUNG_SDAE) | Event | — | transaktionsdaten |
| [[NB] START_BEST_AEND_TK](/schnittstellen/202604/trigger/events/NB-START_BEST_AEND_TK) | Event | — | transaktionsdaten |
| [[NB] START_EINRICHTUNG_KONFIG](/schnittstellen/202604/trigger/events/NB-START_EINRICHTUNG_KONFIG) | Event | — | transaktionsdaten |
| [[NB] START_ENDE_MSB_STILLLEGUNG GAS](/schnittstellen/202604/trigger/events/NB-START_ENDE_MSB_STILLLEGUNG-GAS) | Event | — | transaktionsdaten |
| [[NB] START_ENDE_ZUORDNUNG](/schnittstellen/202604/trigger/events/NB-START_ENDE_ZUORDNUNG) | Event | — | transaktionsdaten |
| [[NB] START_EOG](/schnittstellen/202604/trigger/events/NB-START_EOG) | Event | — | transaktionsdaten |
| [[NB] START_ERHEBUNG_MESSWERTE](/schnittstellen/202604/trigger/events/NB-START_ERHEBUNG_MESSWERTE) | Event | — | transaktionsdaten |
| [[NB] START_LIEFERENDE](/schnittstellen/202604/trigger/events/NB-START_LIEFERENDE) | Event | — | transaktionsdaten |
| [[NB] START_PARTIN](/schnittstellen/202604/trigger/events/NB-START_PARTIN) | Event | — | transaktionsdaten |
| [[NB] START_PREISBLATT](/schnittstellen/202604/trigger/events/NB-START_PREISBLATT) | Event | — | transaktionsdaten |
| [[NB] START_REKLAMATION_DEFINITION](/schnittstellen/202604/trigger/events/NB-START_REKLAMATION_DEFINITION) | Event | — | transaktionsdaten |
| [[NB] START_REKLAMATION_WERTE](/schnittstellen/202604/trigger/events/NB-START_REKLAMATION_WERTE) | Event | — | transaktionsdaten |
| [[NB] START_UEBERM_DEFINITION](/schnittstellen/202604/trigger/events/NB-START_UEBERM_DEFINITION) | Event | — | transaktionsdaten |
| [[NB] START_UEBERSICHT_LEISTUNGSKURVENDEF](/schnittstellen/202604/trigger/events/NB-START_UEBERSICHT_LEISTUNGSKURVENDEF) | Event | — | transaktionsdaten |
| [[NB] START_UEBERSICHT_SCHALTZEITDEF](/schnittstellen/202604/trigger/events/NB-START_UEBERSICHT_SCHALTZEITDEF) | Event | — | transaktionsdaten |
| [[NB] START_UEBERSICHT_ZAEHLZEITDEF](/schnittstellen/202604/trigger/events/NB-START_UEBERSICHT_ZAEHLZEITDEF) | Event | — | transaktionsdaten |
| [[NB] START_VERSAND_ANF_STORNO](/schnittstellen/202604/trigger/events/NB-START_VERSAND_ANF_STORNO) | Event | — | transaktionsdaten |
| [[NB] START_VERSAND_BEARB_MELDUNG](/schnittstellen/202604/trigger/events/NB-START_VERSAND_BEARB_MELDUNG) | Event | — | transaktionsdaten |
| [[NB] START_VERSAND_BEENDIGUNG_AGV](/schnittstellen/202604/trigger/events/NB-START_VERSAND_BEENDIGUNG_AGV) | Event | — | transaktionsdaten |
| [[NB] START_VERSAND_BESTANDSLISTE GAS](/schnittstellen/202604/trigger/events/NB-START_VERSAND_BESTANDSLISTE-GAS) | Event | — | transaktionsdaten |
| [[NB] START_VERSAND_COMDIS](/schnittstellen/202604/trigger/events/NB-START_VERSAND_COMDIS) | Event | — | transaktionsdaten |
| [[NB] START_VERSAND_GEMESSENE_ARB_LEIST_WERTE](/schnittstellen/202604/trigger/events/NB-START_VERSAND_GEMESSENE_ARB_LEIST_WERTE) | Event | — | transaktionsdaten |
| [[NB] START_VERSAND_LIEFERSCHEIN](/schnittstellen/202604/trigger/events/NB-START_VERSAND_LIEFERSCHEIN) | Event | — | transaktionsdaten |
| [[NB] START_VERSAND_SDAE](/schnittstellen/202604/trigger/events/NB-START_VERSAND_SDAE) | Event | — | transaktionsdaten |
| [[NB] START_VERSAND_STATUSMELDUNG](/schnittstellen/202604/trigger/events/NB-START_VERSAND_STATUSMELDUNG) | Event | — | transaktionsdaten |
| [[NB] START_VERSAND_STOERUNGSMELDUNG_NB](/schnittstellen/202604/trigger/events/NB-START_VERSAND_STOERUNGSMELDUNG_NB) | Event | — | transaktionsdaten |
| [[NB] START_VERSAND_STORNO_MSCONS](/schnittstellen/202604/trigger/events/NB-START_VERSAND_STORNO_MSCONS) | Event | — | transaktionsdaten |
| [[NB] START_WIEDERHERST_LB](/schnittstellen/202604/trigger/events/NB-START_WIEDERHERST_LB) | Event | — | transaktionsdaten |
| [[NB] START_WIEDERSPRUCH_ABLEHNUNG](/schnittstellen/202604/trigger/events/NB-START_WIEDERSPRUCH_ABLEHNUNG) | Event | — | transaktionsdaten |
| [[NB] START_ZUORDNUNG_ERZ_MALO_TRANCHE](/schnittstellen/202604/trigger/events/NB-START_ZUORDNUNG_ERZ_MALO_TRANCHE) | Event | — | transaktionsdaten |

### transaktionsgrund

242 Verwendung(en) in den Nachrichtentypen UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [[LF] START_ANFRAGE_STAMMDATENAENDERUNG GAS](/schnittstellen/202604/trigger/events/LF-START_ANFRAGE_STAMMDATENAENDERUNG-GAS) | Event | — | transaktionsdaten |
| [[LF] START_BESTELLUNG_SDAE](/schnittstellen/202604/trigger/events/LF-START_BESTELLUNG_SDAE) | Event | — | transaktionsdaten |
| [[LF] START_KUENDIGUNG](/schnittstellen/202604/trigger/events/LF-START_KUENDIGUNG) | Event | — | transaktionsdaten |
| [[LF] START_LIEFERBEGINN](/schnittstellen/202604/trigger/events/LF-START_LIEFERBEGINN) | Event | — | transaktionsdaten |
| [[LF] START_LIEFERENDE](/schnittstellen/202604/trigger/events/LF-START_LIEFERENDE) | Event | — | transaktionsdaten |
| [[LF] START_VERSAND_SDAE](/schnittstellen/202604/trigger/events/LF-START_VERSAND_SDAE) | Event | — | transaktionsdaten |
| [[MSB] START_BEGINN_MSB](/schnittstellen/202604/trigger/events/MSB-START_BEGINN_MSB) | Event | — | transaktionsdaten |
| [[MSB] START_BESTELLUNG_SDAE GAS](/schnittstellen/202604/trigger/events/MSB-START_BESTELLUNG_SDAE-GAS) | Event | — | transaktionsdaten |
| [[MSB] START_KUENDIGUNG_MSB](/schnittstellen/202604/trigger/events/MSB-START_KUENDIGUNG_MSB) | Event | — | transaktionsdaten |
| [[MSB] START_VERSAND_SDAE](/schnittstellen/202604/trigger/events/MSB-START_VERSAND_SDAE) | Event | — | transaktionsdaten |
| [[NB] START_ABR_BK](/schnittstellen/202604/trigger/events/NB-START_ABR_BK) | Event | — | transaktionsdaten |
| [[NB] START_ABR_NN](/schnittstellen/202604/trigger/events/NB-START_ABR_NN) | Event | — | transaktionsdaten |
| [[NB] START_ANFRAGE_STAMMDATENAENDERUNG GAS](/schnittstellen/202604/trigger/events/NB-START_ANFRAGE_STAMMDATENAENDERUNG-GAS) | Event | — | transaktionsdaten |
| [[NB] START_AUFH_ZUK_ZUORDNUNG](/schnittstellen/202604/trigger/events/NB-START_AUFH_ZUK_ZUORDNUNG) | Event | — | transaktionsdaten |
| [[NB] START_BESTELLUNG_SDAE](/schnittstellen/202604/trigger/events/NB-START_BESTELLUNG_SDAE) | Event | — | transaktionsdaten |
| [[NB] START_ENDE_MSB_STILLLEGUNG GAS](/schnittstellen/202604/trigger/events/NB-START_ENDE_MSB_STILLLEGUNG-GAS) | Event | — | transaktionsdaten |
| [[NB] START_ENDE_ZUORDNUNG](/schnittstellen/202604/trigger/events/NB-START_ENDE_ZUORDNUNG) | Event | — | transaktionsdaten |
| [[NB] START_EOG](/schnittstellen/202604/trigger/events/NB-START_EOG) | Event | — | transaktionsdaten |
| [[NB] START_LIEFERENDE](/schnittstellen/202604/trigger/events/NB-START_LIEFERENDE) | Event | — | transaktionsdaten |
| [[NB] START_VERSAND_BEENDIGUNG_AGV](/schnittstellen/202604/trigger/events/NB-START_VERSAND_BEENDIGUNG_AGV) | Event | — | transaktionsdaten |
| [[NB] START_VERSAND_SDAE](/schnittstellen/202604/trigger/events/NB-START_VERSAND_SDAE) | Event | — | transaktionsdaten |
| [[NB] START_ZUORDNUNG_ERZ_MALO_TRANCHE](/schnittstellen/202604/trigger/events/NB-START_ZUORDNUNG_ERZ_MALO_TRANCHE) | Event | — | transaktionsdaten |
| [PI_44001](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44001) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44003](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44003) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44004](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44004) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44005](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44005) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44006](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44006) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44007](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44007) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44008](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44008) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44009](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44009) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44010](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44010) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44011](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44011) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44012](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44012) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44015](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44015) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44016](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44016) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44017](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44017) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44018](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44018) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44020](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44020) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44021](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44021) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44022](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44022) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44023](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44023) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44024](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44024) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44035](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44035) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44036](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44036) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44037](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44037) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44038](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44038) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44039](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44039) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44040](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44040) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44041](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44041) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44043](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44043) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44044](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44044) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44052](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44052) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44053](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44053) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44060](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44060) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44101](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44101) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44102](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44102) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44103](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44103) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44104](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44104) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44109](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44109) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44111](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44111) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44112](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44112) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44113](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44113) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44115](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44115) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44116](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44116) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44117](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44117) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44119](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44119) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44120](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44120) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44121](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44121) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44123](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44123) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44124](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44124) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44137](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44137) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44138](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44138) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44139](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44139) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44140](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44140) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44142](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44142) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44143](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44143) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44145](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44145) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44146](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44146) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44147](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44147) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44148](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44148) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44149](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44149) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44150](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44150) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44151](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44151) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44152](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44152) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44156](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44156) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44157](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44157) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44159](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44159) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44160](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44160) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44161](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44161) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44162](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44162) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44163](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44163) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44164](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44164) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44165](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44165) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44166](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44166) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44167](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44167) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44168](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44175](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44175) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44176](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44176) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44180](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44180) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44181](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44181) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44182](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44182) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_55001](/schnittstellen/202604/pruefi/UTILMD/PI_55001) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55002](/schnittstellen/202604/pruefi/UTILMD/PI_55002) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55003](/schnittstellen/202604/pruefi/UTILMD/PI_55003) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55004](/schnittstellen/202604/pruefi/UTILMD/PI_55004) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55005](/schnittstellen/202604/pruefi/UTILMD/PI_55005) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55006](/schnittstellen/202604/pruefi/UTILMD/PI_55006) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55007](/schnittstellen/202604/pruefi/UTILMD/PI_55007) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55008](/schnittstellen/202604/pruefi/UTILMD/PI_55008) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55009](/schnittstellen/202604/pruefi/UTILMD/PI_55009) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55010](/schnittstellen/202604/pruefi/UTILMD/PI_55010) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55011](/schnittstellen/202604/pruefi/UTILMD/PI_55011) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55012](/schnittstellen/202604/pruefi/UTILMD/PI_55012) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55013](/schnittstellen/202604/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55014](/schnittstellen/202604/pruefi/UTILMD/PI_55014) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55015](/schnittstellen/202604/pruefi/UTILMD/PI_55015) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55016](/schnittstellen/202604/pruefi/UTILMD/PI_55016) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55017](/schnittstellen/202604/pruefi/UTILMD/PI_55017) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55018](/schnittstellen/202604/pruefi/UTILMD/PI_55018) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55022](/schnittstellen/202604/pruefi/UTILMD/PI_55022) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55023](/schnittstellen/202604/pruefi/UTILMD/PI_55023) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55024](/schnittstellen/202604/pruefi/UTILMD/PI_55024) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55035](/schnittstellen/202604/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55036](/schnittstellen/202604/pruefi/UTILMD/PI_55036) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55037](/schnittstellen/202604/pruefi/UTILMD/PI_55037) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55038](/schnittstellen/202604/pruefi/UTILMD/PI_55038) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55039](/schnittstellen/202604/pruefi/UTILMD/PI_55039) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55040](/schnittstellen/202604/pruefi/UTILMD/PI_55040) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55041](/schnittstellen/202604/pruefi/UTILMD/PI_55041) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55042](/schnittstellen/202604/pruefi/UTILMD/PI_55042) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55044](/schnittstellen/202604/pruefi/UTILMD/PI_55044) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55051](/schnittstellen/202604/pruefi/UTILMD/PI_55051) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55052](/schnittstellen/202604/pruefi/UTILMD/PI_55052) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55053](/schnittstellen/202604/pruefi/UTILMD/PI_55053) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55060](/schnittstellen/202604/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55075](/schnittstellen/202604/pruefi/UTILMD/PI_55075) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55077](/schnittstellen/202604/pruefi/UTILMD/PI_55077) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55078](/schnittstellen/202604/pruefi/UTILMD/PI_55078) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55080](/schnittstellen/202604/pruefi/UTILMD/PI_55080) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55095](/schnittstellen/202604/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55109](/schnittstellen/202604/pruefi/UTILMD/PI_55109) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55110](/schnittstellen/202604/pruefi/UTILMD/PI_55110) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55126](/schnittstellen/202604/pruefi/UTILMD/PI_55126) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55136](/schnittstellen/202604/pruefi/UTILMD/PI_55136) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55137](/schnittstellen/202604/pruefi/UTILMD/PI_55137) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55156](/schnittstellen/202604/pruefi/UTILMD/PI_55156) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55170](/schnittstellen/202604/pruefi/UTILMD/PI_55170) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55173](/schnittstellen/202604/pruefi/UTILMD/PI_55173) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55175](/schnittstellen/202604/pruefi/UTILMD/PI_55175) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55177](/schnittstellen/202604/pruefi/UTILMD/PI_55177) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55180](/schnittstellen/202604/pruefi/UTILMD/PI_55180) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55194](/schnittstellen/202604/pruefi/UTILMD/PI_55194) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55218](/schnittstellen/202604/pruefi/UTILMD/PI_55218) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55220](/schnittstellen/202604/pruefi/UTILMD/PI_55220) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55225](/schnittstellen/202604/pruefi/UTILMD/PI_55225) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55227](/schnittstellen/202604/pruefi/UTILMD/PI_55227) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55230](/schnittstellen/202604/pruefi/UTILMD/PI_55230) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55232](/schnittstellen/202604/pruefi/UTILMD/PI_55232) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55553](/schnittstellen/202604/pruefi/UTILMD/PI_55553) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55555](/schnittstellen/202604/pruefi/UTILMD/PI_55555) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55557](/schnittstellen/202604/pruefi/UTILMD/PI_55557) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55559](/schnittstellen/202604/pruefi/UTILMD/PI_55559) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55600](/schnittstellen/202604/pruefi/UTILMD/PI_55600) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55601](/schnittstellen/202604/pruefi/UTILMD/PI_55601) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55602](/schnittstellen/202604/pruefi/UTILMD/PI_55602) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55603](/schnittstellen/202604/pruefi/UTILMD/PI_55603) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55604](/schnittstellen/202604/pruefi/UTILMD/PI_55604) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55605](/schnittstellen/202604/pruefi/UTILMD/PI_55605) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55607](/schnittstellen/202604/pruefi/UTILMD/PI_55607) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55608](/schnittstellen/202604/pruefi/UTILMD/PI_55608) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55609](/schnittstellen/202604/pruefi/UTILMD/PI_55609) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55611](/schnittstellen/202604/pruefi/UTILMD/PI_55611) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55613](/schnittstellen/202604/pruefi/UTILMD/PI_55613) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55614](/schnittstellen/202604/pruefi/UTILMD/PI_55614) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55615](/schnittstellen/202604/pruefi/UTILMD/PI_55615) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55616](/schnittstellen/202604/pruefi/UTILMD/PI_55616) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55617](/schnittstellen/202604/pruefi/UTILMD/PI_55617) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55618](/schnittstellen/202604/pruefi/UTILMD/PI_55618) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55619](/schnittstellen/202604/pruefi/UTILMD/PI_55619) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55620](/schnittstellen/202604/pruefi/UTILMD/PI_55620) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55621](/schnittstellen/202604/pruefi/UTILMD/PI_55621) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55622](/schnittstellen/202604/pruefi/UTILMD/PI_55622) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55623](/schnittstellen/202604/pruefi/UTILMD/PI_55623) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55624](/schnittstellen/202604/pruefi/UTILMD/PI_55624) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55625](/schnittstellen/202604/pruefi/UTILMD/PI_55625) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55626](/schnittstellen/202604/pruefi/UTILMD/PI_55626) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55627](/schnittstellen/202604/pruefi/UTILMD/PI_55627) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55628](/schnittstellen/202604/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55629](/schnittstellen/202604/pruefi/UTILMD/PI_55629) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55630](/schnittstellen/202604/pruefi/UTILMD/PI_55630) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55632](/schnittstellen/202604/pruefi/UTILMD/PI_55632) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55633](/schnittstellen/202604/pruefi/UTILMD/PI_55633) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55634](/schnittstellen/202604/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55635](/schnittstellen/202604/pruefi/UTILMD/PI_55635) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55636](/schnittstellen/202604/pruefi/UTILMD/PI_55636) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55638](/schnittstellen/202604/pruefi/UTILMD/PI_55638) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55639](/schnittstellen/202604/pruefi/UTILMD/PI_55639) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55640](/schnittstellen/202604/pruefi/UTILMD/PI_55640) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55641](/schnittstellen/202604/pruefi/UTILMD/PI_55641) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55642](/schnittstellen/202604/pruefi/UTILMD/PI_55642) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55643](/schnittstellen/202604/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55644](/schnittstellen/202604/pruefi/UTILMD/PI_55644) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55645](/schnittstellen/202604/pruefi/UTILMD/PI_55645) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55646](/schnittstellen/202604/pruefi/UTILMD/PI_55646) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55647](/schnittstellen/202604/pruefi/UTILMD/PI_55647) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55648](/schnittstellen/202604/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55649](/schnittstellen/202604/pruefi/UTILMD/PI_55649) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55650](/schnittstellen/202604/pruefi/UTILMD/PI_55650) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55651](/schnittstellen/202604/pruefi/UTILMD/PI_55651) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55652](/schnittstellen/202604/pruefi/UTILMD/PI_55652) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55653](/schnittstellen/202604/pruefi/UTILMD/PI_55653) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55654](/schnittstellen/202604/pruefi/UTILMD/PI_55654) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55655](/schnittstellen/202604/pruefi/UTILMD/PI_55655) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55656](/schnittstellen/202604/pruefi/UTILMD/PI_55656) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55657](/schnittstellen/202604/pruefi/UTILMD/PI_55657) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55658](/schnittstellen/202604/pruefi/UTILMD/PI_55658) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55659](/schnittstellen/202604/pruefi/UTILMD/PI_55659) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55660](/schnittstellen/202604/pruefi/UTILMD/PI_55660) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55661](/schnittstellen/202604/pruefi/UTILMD/PI_55661) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55662](/schnittstellen/202604/pruefi/UTILMD/PI_55662) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55663](/schnittstellen/202604/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55664](/schnittstellen/202604/pruefi/UTILMD/PI_55664) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55665](/schnittstellen/202604/pruefi/UTILMD/PI_55665) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55666](/schnittstellen/202604/pruefi/UTILMD/PI_55666) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55667](/schnittstellen/202604/pruefi/UTILMD/PI_55667) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55669](/schnittstellen/202604/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55670](/schnittstellen/202604/pruefi/UTILMD/PI_55670) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55672](/schnittstellen/202604/pruefi/UTILMD/PI_55672) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55673](/schnittstellen/202604/pruefi/UTILMD/PI_55673) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55674](/schnittstellen/202604/pruefi/UTILMD/PI_55674) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55684](/schnittstellen/202604/pruefi/UTILMD/PI_55684) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55686](/schnittstellen/202604/pruefi/UTILMD/PI_55686) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55688](/schnittstellen/202604/pruefi/UTILMD/PI_55688) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55690](/schnittstellen/202604/pruefi/UTILMD/PI_55690) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55691](/schnittstellen/202604/pruefi/UTILMD/PI_55691) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55692](/schnittstellen/202604/pruefi/UTILMD/PI_55692) | Prüfi | UTILMD | transaktionsdaten |

### transaktionsgrundergaenzung

60 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [[LF] START_BESTELLUNG_SDAE](/schnittstellen/202604/trigger/events/LF-START_BESTELLUNG_SDAE) | Event | — | transaktionsdaten |
| [[LF] START_LIEFERBEGINN](/schnittstellen/202604/trigger/events/LF-START_LIEFERBEGINN) | Event | — | transaktionsdaten |
| [[LF] START_LIEFERENDE](/schnittstellen/202604/trigger/events/LF-START_LIEFERENDE) | Event | — | transaktionsdaten |
| [[LF] START_VERSAND_SDAE](/schnittstellen/202604/trigger/events/LF-START_VERSAND_SDAE) | Event | — | transaktionsdaten |
| [[MSB] START_BESTELLUNG_SDAE GAS](/schnittstellen/202604/trigger/events/MSB-START_BESTELLUNG_SDAE-GAS) | Event | — | transaktionsdaten |
| [[MSB] START_VERSAND_SDAE](/schnittstellen/202604/trigger/events/MSB-START_VERSAND_SDAE) | Event | — | transaktionsdaten |
| [[NB] START_ABR_BK](/schnittstellen/202604/trigger/events/NB-START_ABR_BK) | Event | — | transaktionsdaten |
| [[NB] START_ABR_NN](/schnittstellen/202604/trigger/events/NB-START_ABR_NN) | Event | — | transaktionsdaten |
| [[NB] START_AUFH_ZUK_ZUORDNUNG](/schnittstellen/202604/trigger/events/NB-START_AUFH_ZUK_ZUORDNUNG) | Event | — | transaktionsdaten |
| [[NB] START_BESTELLUNG_SDAE](/schnittstellen/202604/trigger/events/NB-START_BESTELLUNG_SDAE) | Event | — | transaktionsdaten |
| [[NB] START_ENDE_ZUORDNUNG](/schnittstellen/202604/trigger/events/NB-START_ENDE_ZUORDNUNG) | Event | — | transaktionsdaten |
| [[NB] START_EOG](/schnittstellen/202604/trigger/events/NB-START_EOG) | Event | — | transaktionsdaten |
| [[NB] START_LIEFERENDE](/schnittstellen/202604/trigger/events/NB-START_LIEFERENDE) | Event | — | transaktionsdaten |
| [[NB] START_VERSAND_SDAE](/schnittstellen/202604/trigger/events/NB-START_VERSAND_SDAE) | Event | — | transaktionsdaten |
| [[NB] START_ZUORDNUNG_ERZ_MALO_TRANCHE](/schnittstellen/202604/trigger/events/NB-START_ZUORDNUNG_ERZ_MALO_TRANCHE) | Event | — | transaktionsdaten |
| [PI_55001](/schnittstellen/202604/pruefi/UTILMD/PI_55001) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55002](/schnittstellen/202604/pruefi/UTILMD/PI_55002) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55003](/schnittstellen/202604/pruefi/UTILMD/PI_55003) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55004](/schnittstellen/202604/pruefi/UTILMD/PI_55004) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55007](/schnittstellen/202604/pruefi/UTILMD/PI_55007) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55010](/schnittstellen/202604/pruefi/UTILMD/PI_55010) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55013](/schnittstellen/202604/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55014](/schnittstellen/202604/pruefi/UTILMD/PI_55014) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55015](/schnittstellen/202604/pruefi/UTILMD/PI_55015) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55016](/schnittstellen/202604/pruefi/UTILMD/PI_55016) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55017](/schnittstellen/202604/pruefi/UTILMD/PI_55017) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55035](/schnittstellen/202604/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55037](/schnittstellen/202604/pruefi/UTILMD/PI_55037) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55038](/schnittstellen/202604/pruefi/UTILMD/PI_55038) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55052](/schnittstellen/202604/pruefi/UTILMD/PI_55052) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55077](/schnittstellen/202604/pruefi/UTILMD/PI_55077) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55078](/schnittstellen/202604/pruefi/UTILMD/PI_55078) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55080](/schnittstellen/202604/pruefi/UTILMD/PI_55080) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55109](/schnittstellen/202604/pruefi/UTILMD/PI_55109) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55110](/schnittstellen/202604/pruefi/UTILMD/PI_55110) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55137](/schnittstellen/202604/pruefi/UTILMD/PI_55137) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55600](/schnittstellen/202604/pruefi/UTILMD/PI_55600) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55601](/schnittstellen/202604/pruefi/UTILMD/PI_55601) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55602](/schnittstellen/202604/pruefi/UTILMD/PI_55602) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55603](/schnittstellen/202604/pruefi/UTILMD/PI_55603) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55604](/schnittstellen/202604/pruefi/UTILMD/PI_55604) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55605](/schnittstellen/202604/pruefi/UTILMD/PI_55605) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55607](/schnittstellen/202604/pruefi/UTILMD/PI_55607) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55608](/schnittstellen/202604/pruefi/UTILMD/PI_55608) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55609](/schnittstellen/202604/pruefi/UTILMD/PI_55609) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55613](/schnittstellen/202604/pruefi/UTILMD/PI_55613) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55616](/schnittstellen/202604/pruefi/UTILMD/PI_55616) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55622](/schnittstellen/202604/pruefi/UTILMD/PI_55622) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55628](/schnittstellen/202604/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55634](/schnittstellen/202604/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55640](/schnittstellen/202604/pruefi/UTILMD/PI_55640) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55645](/schnittstellen/202604/pruefi/UTILMD/PI_55645) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55650](/schnittstellen/202604/pruefi/UTILMD/PI_55650) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55655](/schnittstellen/202604/pruefi/UTILMD/PI_55655) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55660](/schnittstellen/202604/pruefi/UTILMD/PI_55660) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55665](/schnittstellen/202604/pruefi/UTILMD/PI_55665) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55670](/schnittstellen/202604/pruefi/UTILMD/PI_55670) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55672](/schnittstellen/202604/pruefi/UTILMD/PI_55672) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55673](/schnittstellen/202604/pruefi/UTILMD/PI_55673) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55674](/schnittstellen/202604/pruefi/UTILMD/PI_55674) | Prüfi | UTILMD | transaktionsdaten |

### transaktionsgrundergaenzungBefristeteAnmeldung

17 Verwendung(en) in den Nachrichtentypen UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [[NB] START_EOG](/schnittstellen/202604/trigger/events/NB-START_EOG) | Event | — | transaktionsdaten |
| [[NB] START_ZUORDNUNG_ERZ_MALO_TRANCHE](/schnittstellen/202604/trigger/events/NB-START_ZUORDNUNG_ERZ_MALO_TRANCHE) | Event | — | transaktionsdaten |
| [PI_44001](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44001) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44003](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44003) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44015](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44015) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_55001](/schnittstellen/202604/pruefi/UTILMD/PI_55001) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55002](/schnittstellen/202604/pruefi/UTILMD/PI_55002) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55013](/schnittstellen/202604/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55014](/schnittstellen/202604/pruefi/UTILMD/PI_55014) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55015](/schnittstellen/202604/pruefi/UTILMD/PI_55015) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55600](/schnittstellen/202604/pruefi/UTILMD/PI_55600) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55602](/schnittstellen/202604/pruefi/UTILMD/PI_55602) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55607](/schnittstellen/202604/pruefi/UTILMD/PI_55607) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55608](/schnittstellen/202604/pruefi/UTILMD/PI_55608) | Prüfi | UTILMD | transaktionsdaten |

### vorgangsnummer

238 Verwendung(en) in den Nachrichtentypen INSRPT, UTILMD, UTILMD_GAS, UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_23001](/schnittstellen/202604/pruefi/INSRPT/PI_23001) | Prüfi | INSRPT | transaktionsdaten |
| [PI_23003](/schnittstellen/202604/pruefi/INSRPT/PI_23003) | Prüfi | INSRPT | transaktionsdaten |
| [PI_23004](/schnittstellen/202604/pruefi/INSRPT/PI_23004) | Prüfi | INSRPT | transaktionsdaten |
| [PI_23005](/schnittstellen/202604/pruefi/INSRPT/PI_23005) | Prüfi | INSRPT | transaktionsdaten |
| [PI_23008](/schnittstellen/202604/pruefi/INSRPT/PI_23008) | Prüfi | INSRPT | transaktionsdaten |
| [PI_23009](/schnittstellen/202604/pruefi/INSRPT/PI_23009) | Prüfi | INSRPT | transaktionsdaten |
| [PI_23011](/schnittstellen/202604/pruefi/INSRPT/PI_23011) | Prüfi | INSRPT | transaktionsdaten |
| [PI_23012](/schnittstellen/202604/pruefi/INSRPT/PI_23012) | Prüfi | INSRPT | transaktionsdaten |
| [PI_25001](/schnittstellen/202604/pruefi/UTILTS/PI_25001) | Prüfi | UTILTS | transaktionsdaten |
| [PI_25004](/schnittstellen/202604/pruefi/UTILTS/PI_25004) | Prüfi | UTILTS | transaktionsdaten |
| [PI_25005](/schnittstellen/202604/pruefi/UTILTS/PI_25005) | Prüfi | UTILTS | transaktionsdaten |
| [PI_25006](/schnittstellen/202604/pruefi/UTILTS/PI_25006) | Prüfi | UTILTS | transaktionsdaten |
| [PI_25007](/schnittstellen/202604/pruefi/UTILTS/PI_25007) | Prüfi | UTILTS | transaktionsdaten |
| [PI_25008](/schnittstellen/202604/pruefi/UTILTS/PI_25008) | Prüfi | UTILTS | transaktionsdaten |
| [PI_25009](/schnittstellen/202604/pruefi/UTILTS/PI_25009) | Prüfi | UTILTS | transaktionsdaten |
| [PI_25010](/schnittstellen/202604/pruefi/UTILTS/PI_25010) | Prüfi | UTILTS | transaktionsdaten |
| [PI_44001](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44001) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44003](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44003) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44004](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44004) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44005](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44005) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44006](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44006) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44007](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44007) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44008](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44008) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44009](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44009) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44010](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44010) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44011](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44011) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44012](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44012) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44015](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44015) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44016](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44016) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44017](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44017) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44018](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44018) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44019](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44019) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44020](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44020) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44021](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44021) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44022](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44022) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44023](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44023) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44024](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44024) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44035](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44035) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44036](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44036) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44037](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44037) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44038](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44038) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44039](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44039) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44040](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44040) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44041](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44041) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44043](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44043) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44044](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44044) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44052](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44052) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44053](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44053) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44060](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44060) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44101](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44101) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44102](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44102) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44103](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44103) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44104](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44104) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44109](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44109) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44111](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44111) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44112](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44112) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44113](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44113) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44115](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44115) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44116](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44116) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44117](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44117) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44119](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44119) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44120](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44120) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44121](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44121) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44123](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44123) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44124](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44124) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44137](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44137) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44138](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44138) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44139](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44139) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44140](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44140) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44142](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44142) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44143](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44143) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44145](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44145) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44146](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44146) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44147](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44147) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44148](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44148) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44149](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44149) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44150](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44150) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44151](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44151) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44152](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44152) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44156](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44156) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44157](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44157) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44159](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44159) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44160](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44160) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44161](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44161) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44162](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44162) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44163](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44163) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44164](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44164) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44165](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44165) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44166](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44166) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44167](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44167) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44168](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44175](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44175) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44176](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44176) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44180](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44180) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44181](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44181) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44182](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44182) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_55001](/schnittstellen/202604/pruefi/UTILMD/PI_55001) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55002](/schnittstellen/202604/pruefi/UTILMD/PI_55002) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55003](/schnittstellen/202604/pruefi/UTILMD/PI_55003) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55004](/schnittstellen/202604/pruefi/UTILMD/PI_55004) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55005](/schnittstellen/202604/pruefi/UTILMD/PI_55005) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55006](/schnittstellen/202604/pruefi/UTILMD/PI_55006) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55007](/schnittstellen/202604/pruefi/UTILMD/PI_55007) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55008](/schnittstellen/202604/pruefi/UTILMD/PI_55008) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55009](/schnittstellen/202604/pruefi/UTILMD/PI_55009) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55010](/schnittstellen/202604/pruefi/UTILMD/PI_55010) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55011](/schnittstellen/202604/pruefi/UTILMD/PI_55011) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55012](/schnittstellen/202604/pruefi/UTILMD/PI_55012) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55013](/schnittstellen/202604/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55014](/schnittstellen/202604/pruefi/UTILMD/PI_55014) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55015](/schnittstellen/202604/pruefi/UTILMD/PI_55015) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55016](/schnittstellen/202604/pruefi/UTILMD/PI_55016) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55017](/schnittstellen/202604/pruefi/UTILMD/PI_55017) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55018](/schnittstellen/202604/pruefi/UTILMD/PI_55018) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55022](/schnittstellen/202604/pruefi/UTILMD/PI_55022) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55023](/schnittstellen/202604/pruefi/UTILMD/PI_55023) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55024](/schnittstellen/202604/pruefi/UTILMD/PI_55024) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55035](/schnittstellen/202604/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55036](/schnittstellen/202604/pruefi/UTILMD/PI_55036) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55037](/schnittstellen/202604/pruefi/UTILMD/PI_55037) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55038](/schnittstellen/202604/pruefi/UTILMD/PI_55038) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55039](/schnittstellen/202604/pruefi/UTILMD/PI_55039) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55040](/schnittstellen/202604/pruefi/UTILMD/PI_55040) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55041](/schnittstellen/202604/pruefi/UTILMD/PI_55041) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55042](/schnittstellen/202604/pruefi/UTILMD/PI_55042) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55044](/schnittstellen/202604/pruefi/UTILMD/PI_55044) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55051](/schnittstellen/202604/pruefi/UTILMD/PI_55051) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55052](/schnittstellen/202604/pruefi/UTILMD/PI_55052) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55053](/schnittstellen/202604/pruefi/UTILMD/PI_55053) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55060](/schnittstellen/202604/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55074](/schnittstellen/202604/pruefi/UTILMD/PI_55074) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55075](/schnittstellen/202604/pruefi/UTILMD/PI_55075) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55077](/schnittstellen/202604/pruefi/UTILMD/PI_55077) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55078](/schnittstellen/202604/pruefi/UTILMD/PI_55078) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55080](/schnittstellen/202604/pruefi/UTILMD/PI_55080) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55095](/schnittstellen/202604/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55109](/schnittstellen/202604/pruefi/UTILMD/PI_55109) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55110](/schnittstellen/202604/pruefi/UTILMD/PI_55110) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55126](/schnittstellen/202604/pruefi/UTILMD/PI_55126) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55136](/schnittstellen/202604/pruefi/UTILMD/PI_55136) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55137](/schnittstellen/202604/pruefi/UTILMD/PI_55137) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55156](/schnittstellen/202604/pruefi/UTILMD/PI_55156) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55170](/schnittstellen/202604/pruefi/UTILMD/PI_55170) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55173](/schnittstellen/202604/pruefi/UTILMD/PI_55173) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55175](/schnittstellen/202604/pruefi/UTILMD/PI_55175) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55177](/schnittstellen/202604/pruefi/UTILMD/PI_55177) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55180](/schnittstellen/202604/pruefi/UTILMD/PI_55180) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55194](/schnittstellen/202604/pruefi/UTILMD/PI_55194) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55218](/schnittstellen/202604/pruefi/UTILMD/PI_55218) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55220](/schnittstellen/202604/pruefi/UTILMD/PI_55220) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55225](/schnittstellen/202604/pruefi/UTILMD/PI_55225) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55227](/schnittstellen/202604/pruefi/UTILMD/PI_55227) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55230](/schnittstellen/202604/pruefi/UTILMD/PI_55230) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55232](/schnittstellen/202604/pruefi/UTILMD/PI_55232) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55553](/schnittstellen/202604/pruefi/UTILMD/PI_55553) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55555](/schnittstellen/202604/pruefi/UTILMD/PI_55555) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55557](/schnittstellen/202604/pruefi/UTILMD/PI_55557) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55559](/schnittstellen/202604/pruefi/UTILMD/PI_55559) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55600](/schnittstellen/202604/pruefi/UTILMD/PI_55600) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55601](/schnittstellen/202604/pruefi/UTILMD/PI_55601) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55602](/schnittstellen/202604/pruefi/UTILMD/PI_55602) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55603](/schnittstellen/202604/pruefi/UTILMD/PI_55603) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55604](/schnittstellen/202604/pruefi/UTILMD/PI_55604) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55605](/schnittstellen/202604/pruefi/UTILMD/PI_55605) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55607](/schnittstellen/202604/pruefi/UTILMD/PI_55607) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55608](/schnittstellen/202604/pruefi/UTILMD/PI_55608) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55609](/schnittstellen/202604/pruefi/UTILMD/PI_55609) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55611](/schnittstellen/202604/pruefi/UTILMD/PI_55611) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55613](/schnittstellen/202604/pruefi/UTILMD/PI_55613) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55614](/schnittstellen/202604/pruefi/UTILMD/PI_55614) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55615](/schnittstellen/202604/pruefi/UTILMD/PI_55615) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55616](/schnittstellen/202604/pruefi/UTILMD/PI_55616) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55617](/schnittstellen/202604/pruefi/UTILMD/PI_55617) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55618](/schnittstellen/202604/pruefi/UTILMD/PI_55618) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55619](/schnittstellen/202604/pruefi/UTILMD/PI_55619) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55620](/schnittstellen/202604/pruefi/UTILMD/PI_55620) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55621](/schnittstellen/202604/pruefi/UTILMD/PI_55621) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55622](/schnittstellen/202604/pruefi/UTILMD/PI_55622) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55623](/schnittstellen/202604/pruefi/UTILMD/PI_55623) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55624](/schnittstellen/202604/pruefi/UTILMD/PI_55624) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55625](/schnittstellen/202604/pruefi/UTILMD/PI_55625) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55626](/schnittstellen/202604/pruefi/UTILMD/PI_55626) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55627](/schnittstellen/202604/pruefi/UTILMD/PI_55627) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55628](/schnittstellen/202604/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55629](/schnittstellen/202604/pruefi/UTILMD/PI_55629) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55630](/schnittstellen/202604/pruefi/UTILMD/PI_55630) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55632](/schnittstellen/202604/pruefi/UTILMD/PI_55632) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55633](/schnittstellen/202604/pruefi/UTILMD/PI_55633) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55634](/schnittstellen/202604/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55635](/schnittstellen/202604/pruefi/UTILMD/PI_55635) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55636](/schnittstellen/202604/pruefi/UTILMD/PI_55636) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55638](/schnittstellen/202604/pruefi/UTILMD/PI_55638) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55639](/schnittstellen/202604/pruefi/UTILMD/PI_55639) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55640](/schnittstellen/202604/pruefi/UTILMD/PI_55640) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55641](/schnittstellen/202604/pruefi/UTILMD/PI_55641) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55642](/schnittstellen/202604/pruefi/UTILMD/PI_55642) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55643](/schnittstellen/202604/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55644](/schnittstellen/202604/pruefi/UTILMD/PI_55644) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55645](/schnittstellen/202604/pruefi/UTILMD/PI_55645) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55646](/schnittstellen/202604/pruefi/UTILMD/PI_55646) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55647](/schnittstellen/202604/pruefi/UTILMD/PI_55647) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55648](/schnittstellen/202604/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55649](/schnittstellen/202604/pruefi/UTILMD/PI_55649) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55650](/schnittstellen/202604/pruefi/UTILMD/PI_55650) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55651](/schnittstellen/202604/pruefi/UTILMD/PI_55651) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55652](/schnittstellen/202604/pruefi/UTILMD/PI_55652) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55653](/schnittstellen/202604/pruefi/UTILMD/PI_55653) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55654](/schnittstellen/202604/pruefi/UTILMD/PI_55654) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55655](/schnittstellen/202604/pruefi/UTILMD/PI_55655) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55656](/schnittstellen/202604/pruefi/UTILMD/PI_55656) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55657](/schnittstellen/202604/pruefi/UTILMD/PI_55657) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55658](/schnittstellen/202604/pruefi/UTILMD/PI_55658) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55659](/schnittstellen/202604/pruefi/UTILMD/PI_55659) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55660](/schnittstellen/202604/pruefi/UTILMD/PI_55660) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55661](/schnittstellen/202604/pruefi/UTILMD/PI_55661) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55662](/schnittstellen/202604/pruefi/UTILMD/PI_55662) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55663](/schnittstellen/202604/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55664](/schnittstellen/202604/pruefi/UTILMD/PI_55664) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55665](/schnittstellen/202604/pruefi/UTILMD/PI_55665) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55666](/schnittstellen/202604/pruefi/UTILMD/PI_55666) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55667](/schnittstellen/202604/pruefi/UTILMD/PI_55667) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55669](/schnittstellen/202604/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55670](/schnittstellen/202604/pruefi/UTILMD/PI_55670) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55672](/schnittstellen/202604/pruefi/UTILMD/PI_55672) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55673](/schnittstellen/202604/pruefi/UTILMD/PI_55673) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55674](/schnittstellen/202604/pruefi/UTILMD/PI_55674) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55684](/schnittstellen/202604/pruefi/UTILMD/PI_55684) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55686](/schnittstellen/202604/pruefi/UTILMD/PI_55686) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55688](/schnittstellen/202604/pruefi/UTILMD/PI_55688) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55690](/schnittstellen/202604/pruefi/UTILMD/PI_55690) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55691](/schnittstellen/202604/pruefi/UTILMD/PI_55691) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55692](/schnittstellen/202604/pruefi/UTILMD/PI_55692) | Prüfi | UTILMD | transaktionsdaten |

### pruefidentifikator

364 Verwendung(en) in den Nachrichtentypen COMDIS, IFTSTA, INSRPT, INVOIC, MSCONS, ORDCHG, ORDERS, ORDRSP, PARTIN, PRICAT, QUOTES, REMADV, REQOTE, UTILMD, UTILMD_GAS, UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_13002](/schnittstellen/202604/pruefi/MSCONS/PI_13002) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13006](/schnittstellen/202604/pruefi/MSCONS/PI_13006) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13007](/schnittstellen/202604/pruefi/MSCONS/PI_13007) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13008](/schnittstellen/202604/pruefi/MSCONS/PI_13008) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13009](/schnittstellen/202604/pruefi/MSCONS/PI_13009) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13015](/schnittstellen/202604/pruefi/MSCONS/PI_13015) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13016](/schnittstellen/202604/pruefi/MSCONS/PI_13016) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13017](/schnittstellen/202604/pruefi/MSCONS/PI_13017) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13018](/schnittstellen/202604/pruefi/MSCONS/PI_13018) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13019](/schnittstellen/202604/pruefi/MSCONS/PI_13019) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13025](/schnittstellen/202604/pruefi/MSCONS/PI_13025) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13027](/schnittstellen/202604/pruefi/MSCONS/PI_13027) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13028](/schnittstellen/202604/pruefi/MSCONS/PI_13028) | Prüfi | MSCONS | transaktionsdaten |
| [PI_15001](/schnittstellen/202604/pruefi/QUOTES/PI_15001) | Prüfi | QUOTES | transaktionsdaten |
| [PI_15003](/schnittstellen/202604/pruefi/QUOTES/PI_15003) | Prüfi | QUOTES | transaktionsdaten |
| [PI_15004](/schnittstellen/202604/pruefi/QUOTES/PI_15004) | Prüfi | QUOTES | transaktionsdaten |
| [PI_17001](/schnittstellen/202604/pruefi/ORDERS/PI_17001) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17002](/schnittstellen/202604/pruefi/ORDERS/PI_17002) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17003](/schnittstellen/202604/pruefi/ORDERS/PI_17003) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17004](/schnittstellen/202604/pruefi/ORDERS/PI_17004) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17005](/schnittstellen/202604/pruefi/ORDERS/PI_17005) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17006](/schnittstellen/202604/pruefi/ORDERS/PI_17006) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17009](/schnittstellen/202604/pruefi/ORDERS/PI_17009) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17101](/schnittstellen/202604/pruefi/ORDERS/PI_17101) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17102](/schnittstellen/202604/pruefi/ORDERS/PI_17102) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17103](/schnittstellen/202604/pruefi/ORDERS/PI_17103) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17104](/schnittstellen/202604/pruefi/ORDERS/PI_17104) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17113](/schnittstellen/202604/pruefi/ORDERS/PI_17113) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17115](/schnittstellen/202604/pruefi/ORDERS/PI_17115) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17116](/schnittstellen/202604/pruefi/ORDERS/PI_17116) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17117](/schnittstellen/202604/pruefi/ORDERS/PI_17117) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17118](/schnittstellen/202604/pruefi/ORDERS/PI_17118) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17120](/schnittstellen/202604/pruefi/ORDERS/PI_17120) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17121](/schnittstellen/202604/pruefi/ORDERS/PI_17121) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17122](/schnittstellen/202604/pruefi/ORDERS/PI_17122) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17123](/schnittstellen/202604/pruefi/ORDERS/PI_17123) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17126](/schnittstellen/202604/pruefi/ORDERS/PI_17126) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17128](/schnittstellen/202604/pruefi/ORDERS/PI_17128) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17129](/schnittstellen/202604/pruefi/ORDERS/PI_17129) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17130](/schnittstellen/202604/pruefi/ORDERS/PI_17130) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17131](/schnittstellen/202604/pruefi/ORDERS/PI_17131) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17132](/schnittstellen/202604/pruefi/ORDERS/PI_17132) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17133](/schnittstellen/202604/pruefi/ORDERS/PI_17133) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17134](/schnittstellen/202604/pruefi/ORDERS/PI_17134) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17135](/schnittstellen/202604/pruefi/ORDERS/PI_17135) | Prüfi | ORDERS | transaktionsdaten |
| [PI_19001](/schnittstellen/202604/pruefi/ORDRSP/PI_19001) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19002](/schnittstellen/202604/pruefi/ORDRSP/PI_19002) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19003](/schnittstellen/202604/pruefi/ORDRSP/PI_19003) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19004](/schnittstellen/202604/pruefi/ORDRSP/PI_19004) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19005](/schnittstellen/202604/pruefi/ORDRSP/PI_19005) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19006](/schnittstellen/202604/pruefi/ORDRSP/PI_19006) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19007](/schnittstellen/202604/pruefi/ORDRSP/PI_19007) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19009](/schnittstellen/202604/pruefi/ORDRSP/PI_19009) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19010](/schnittstellen/202604/pruefi/ORDRSP/PI_19010) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19011](/schnittstellen/202604/pruefi/ORDRSP/PI_19011) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19012](/schnittstellen/202604/pruefi/ORDRSP/PI_19012) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19013](/schnittstellen/202604/pruefi/ORDRSP/PI_19013) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19014](/schnittstellen/202604/pruefi/ORDRSP/PI_19014) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19015](/schnittstellen/202604/pruefi/ORDRSP/PI_19015) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19016](/schnittstellen/202604/pruefi/ORDRSP/PI_19016) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19101](/schnittstellen/202604/pruefi/ORDRSP/PI_19101) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19102](/schnittstellen/202604/pruefi/ORDRSP/PI_19102) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19103](/schnittstellen/202604/pruefi/ORDRSP/PI_19103) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19104](/schnittstellen/202604/pruefi/ORDRSP/PI_19104) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19114](/schnittstellen/202604/pruefi/ORDRSP/PI_19114) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19116](/schnittstellen/202604/pruefi/ORDRSP/PI_19116) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19117](/schnittstellen/202604/pruefi/ORDRSP/PI_19117) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19118](/schnittstellen/202604/pruefi/ORDRSP/PI_19118) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19119](/schnittstellen/202604/pruefi/ORDRSP/PI_19119) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19121](/schnittstellen/202604/pruefi/ORDRSP/PI_19121) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19123](/schnittstellen/202604/pruefi/ORDRSP/PI_19123) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19124](/schnittstellen/202604/pruefi/ORDRSP/PI_19124) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19128](/schnittstellen/202604/pruefi/ORDRSP/PI_19128) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19129](/schnittstellen/202604/pruefi/ORDRSP/PI_19129) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19133](/schnittstellen/202604/pruefi/ORDRSP/PI_19133) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19301](/schnittstellen/202604/pruefi/ORDRSP/PI_19301) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19302](/schnittstellen/202604/pruefi/ORDRSP/PI_19302) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_21007](/schnittstellen/202604/pruefi/IFTSTA/PI_21007) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21009](/schnittstellen/202604/pruefi/IFTSTA/PI_21009) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21010](/schnittstellen/202604/pruefi/IFTSTA/PI_21010) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21011](/schnittstellen/202604/pruefi/IFTSTA/PI_21011) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21012](/schnittstellen/202604/pruefi/IFTSTA/PI_21012) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21013](/schnittstellen/202604/pruefi/IFTSTA/PI_21013) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21015](/schnittstellen/202604/pruefi/IFTSTA/PI_21015) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21018](/schnittstellen/202604/pruefi/IFTSTA/PI_21018) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21024](/schnittstellen/202604/pruefi/IFTSTA/PI_21024) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21025](/schnittstellen/202604/pruefi/IFTSTA/PI_21025) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21026](/schnittstellen/202604/pruefi/IFTSTA/PI_21026) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21027](/schnittstellen/202604/pruefi/IFTSTA/PI_21027) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21028](/schnittstellen/202604/pruefi/IFTSTA/PI_21028) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21029](/schnittstellen/202604/pruefi/IFTSTA/PI_21029) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21030](/schnittstellen/202604/pruefi/IFTSTA/PI_21030) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21031](/schnittstellen/202604/pruefi/IFTSTA/PI_21031) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21032](/schnittstellen/202604/pruefi/IFTSTA/PI_21032) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21033](/schnittstellen/202604/pruefi/IFTSTA/PI_21033) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21035](/schnittstellen/202604/pruefi/IFTSTA/PI_21035) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21036](/schnittstellen/202604/pruefi/IFTSTA/PI_21036) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21039](/schnittstellen/202604/pruefi/IFTSTA/PI_21039) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21040](/schnittstellen/202604/pruefi/IFTSTA/PI_21040) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21043](/schnittstellen/202604/pruefi/IFTSTA/PI_21043) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21044](/schnittstellen/202604/pruefi/IFTSTA/PI_21044) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21045](/schnittstellen/202604/pruefi/IFTSTA/PI_21045) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21047](/schnittstellen/202604/pruefi/IFTSTA/PI_21047) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_23001](/schnittstellen/202604/pruefi/INSRPT/PI_23001) | Prüfi | INSRPT | transaktionsdaten |
| [PI_23003](/schnittstellen/202604/pruefi/INSRPT/PI_23003) | Prüfi | INSRPT | transaktionsdaten |
| [PI_23004](/schnittstellen/202604/pruefi/INSRPT/PI_23004) | Prüfi | INSRPT | transaktionsdaten |
| [PI_23005](/schnittstellen/202604/pruefi/INSRPT/PI_23005) | Prüfi | INSRPT | transaktionsdaten |
| [PI_23008](/schnittstellen/202604/pruefi/INSRPT/PI_23008) | Prüfi | INSRPT | transaktionsdaten |
| [PI_23009](/schnittstellen/202604/pruefi/INSRPT/PI_23009) | Prüfi | INSRPT | transaktionsdaten |
| [PI_23011](/schnittstellen/202604/pruefi/INSRPT/PI_23011) | Prüfi | INSRPT | transaktionsdaten |
| [PI_23012](/schnittstellen/202604/pruefi/INSRPT/PI_23012) | Prüfi | INSRPT | transaktionsdaten |
| [PI_25001](/schnittstellen/202604/pruefi/UTILTS/PI_25001) | Prüfi | UTILTS | transaktionsdaten |
| [PI_25004](/schnittstellen/202604/pruefi/UTILTS/PI_25004) | Prüfi | UTILTS | transaktionsdaten |
| [PI_25005](/schnittstellen/202604/pruefi/UTILTS/PI_25005) | Prüfi | UTILTS | transaktionsdaten |
| [PI_25006](/schnittstellen/202604/pruefi/UTILTS/PI_25006) | Prüfi | UTILTS | transaktionsdaten |
| [PI_25007](/schnittstellen/202604/pruefi/UTILTS/PI_25007) | Prüfi | UTILTS | transaktionsdaten |
| [PI_25008](/schnittstellen/202604/pruefi/UTILTS/PI_25008) | Prüfi | UTILTS | transaktionsdaten |
| [PI_25009](/schnittstellen/202604/pruefi/UTILTS/PI_25009) | Prüfi | UTILTS | transaktionsdaten |
| [PI_25010](/schnittstellen/202604/pruefi/UTILTS/PI_25010) | Prüfi | UTILTS | transaktionsdaten |
| [PI_27002](/schnittstellen/202604/pruefi/PRICAT/PI_27002) | Prüfi | PRICAT | transaktionsdaten |
| [PI_27003](/schnittstellen/202604/pruefi/PRICAT/PI_27003) | Prüfi | PRICAT | transaktionsdaten |
| [PI_29001](/schnittstellen/202604/pruefi/COMDIS/PI_29001) | Prüfi | COMDIS | transaktionsdaten |
| [PI_29002](/schnittstellen/202604/pruefi/COMDIS/PI_29002) | Prüfi | COMDIS | transaktionsdaten |
| [PI_31002](/schnittstellen/202604/pruefi/INVOIC/PI_31002) | Prüfi | INVOIC | transaktionsdaten |
| [PI_33001](/schnittstellen/202604/pruefi/REMADV/PI_33001) | Prüfi | REMADV | transaktionsdaten |
| [PI_33002](/schnittstellen/202604/pruefi/REMADV/PI_33002) | Prüfi | REMADV | transaktionsdaten |
| [PI_33003](/schnittstellen/202604/pruefi/REMADV/PI_33003) | Prüfi | REMADV | transaktionsdaten |
| [PI_33004](/schnittstellen/202604/pruefi/REMADV/PI_33004) | Prüfi | REMADV | transaktionsdaten |
| [PI_35001](/schnittstellen/202604/pruefi/REQOTE/PI_35001) | Prüfi | REQOTE | transaktionsdaten |
| [PI_35002](/schnittstellen/202604/pruefi/REQOTE/PI_35002) | Prüfi | REQOTE | transaktionsdaten |
| [PI_35004](/schnittstellen/202604/pruefi/REQOTE/PI_35004) | Prüfi | REQOTE | transaktionsdaten |
| [PI_37000](/schnittstellen/202604/pruefi/PARTIN/PI_37000) | Prüfi | PARTIN | transaktionsdaten |
| [PI_37001](/schnittstellen/202604/pruefi/PARTIN/PI_37001) | Prüfi | PARTIN | transaktionsdaten |
| [PI_37002](/schnittstellen/202604/pruefi/PARTIN/PI_37002) | Prüfi | PARTIN | transaktionsdaten |
| [PI_37008](/schnittstellen/202604/pruefi/PARTIN/PI_37008) | Prüfi | PARTIN | transaktionsdaten |
| [PI_37009](/schnittstellen/202604/pruefi/PARTIN/PI_37009) | Prüfi | PARTIN | transaktionsdaten |
| [PI_37010](/schnittstellen/202604/pruefi/PARTIN/PI_37010) | Prüfi | PARTIN | transaktionsdaten |
| [PI_37012](/schnittstellen/202604/pruefi/PARTIN/PI_37012) | Prüfi | PARTIN | transaktionsdaten |
| [PI_37013](/schnittstellen/202604/pruefi/PARTIN/PI_37013) | Prüfi | PARTIN | transaktionsdaten |
| [PI_37014](/schnittstellen/202604/pruefi/PARTIN/PI_37014) | Prüfi | PARTIN | transaktionsdaten |
| [PI_39000](/schnittstellen/202604/pruefi/ORDCHG/PI_39000) | Prüfi | ORDCHG | transaktionsdaten |
| [PI_39001](/schnittstellen/202604/pruefi/ORDCHG/PI_39001) | Prüfi | ORDCHG | transaktionsdaten |
| [PI_44001](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44001) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44003](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44003) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44004](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44004) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44005](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44005) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44006](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44006) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44007](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44007) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44008](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44008) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44009](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44009) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44010](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44010) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44011](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44011) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44012](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44012) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44015](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44015) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44016](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44016) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44017](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44017) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44018](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44018) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44019](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44019) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44020](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44020) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44021](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44021) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44022](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44022) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44023](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44023) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44024](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44024) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44035](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44035) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44036](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44036) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44037](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44037) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44038](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44038) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44039](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44039) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44040](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44040) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44041](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44041) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44043](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44043) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44044](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44044) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44052](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44052) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44053](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44053) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44060](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44060) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44101](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44101) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44102](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44102) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44103](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44103) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44104](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44104) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44109](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44109) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44111](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44111) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44112](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44112) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44113](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44113) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44115](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44115) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44116](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44116) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44117](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44117) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44119](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44119) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44120](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44120) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44121](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44121) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44123](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44123) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44124](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44124) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44137](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44137) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44138](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44138) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44139](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44139) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44140](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44140) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44142](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44142) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44143](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44143) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44145](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44145) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44146](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44146) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44147](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44147) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44148](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44148) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44149](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44149) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44150](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44150) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44151](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44151) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44152](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44152) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44156](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44156) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44157](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44157) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44159](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44159) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44160](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44160) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44161](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44161) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44162](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44162) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44163](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44163) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44164](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44164) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44165](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44165) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44166](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44166) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44167](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44167) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44168](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44175](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44175) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44176](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44176) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44180](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44180) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44181](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44181) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44182](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44182) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_55001](/schnittstellen/202604/pruefi/UTILMD/PI_55001) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55002](/schnittstellen/202604/pruefi/UTILMD/PI_55002) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55003](/schnittstellen/202604/pruefi/UTILMD/PI_55003) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55004](/schnittstellen/202604/pruefi/UTILMD/PI_55004) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55005](/schnittstellen/202604/pruefi/UTILMD/PI_55005) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55006](/schnittstellen/202604/pruefi/UTILMD/PI_55006) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55007](/schnittstellen/202604/pruefi/UTILMD/PI_55007) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55008](/schnittstellen/202604/pruefi/UTILMD/PI_55008) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55009](/schnittstellen/202604/pruefi/UTILMD/PI_55009) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55010](/schnittstellen/202604/pruefi/UTILMD/PI_55010) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55011](/schnittstellen/202604/pruefi/UTILMD/PI_55011) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55012](/schnittstellen/202604/pruefi/UTILMD/PI_55012) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55013](/schnittstellen/202604/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55014](/schnittstellen/202604/pruefi/UTILMD/PI_55014) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55015](/schnittstellen/202604/pruefi/UTILMD/PI_55015) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55016](/schnittstellen/202604/pruefi/UTILMD/PI_55016) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55017](/schnittstellen/202604/pruefi/UTILMD/PI_55017) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55018](/schnittstellen/202604/pruefi/UTILMD/PI_55018) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55022](/schnittstellen/202604/pruefi/UTILMD/PI_55022) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55023](/schnittstellen/202604/pruefi/UTILMD/PI_55023) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55024](/schnittstellen/202604/pruefi/UTILMD/PI_55024) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55035](/schnittstellen/202604/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55036](/schnittstellen/202604/pruefi/UTILMD/PI_55036) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55037](/schnittstellen/202604/pruefi/UTILMD/PI_55037) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55038](/schnittstellen/202604/pruefi/UTILMD/PI_55038) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55039](/schnittstellen/202604/pruefi/UTILMD/PI_55039) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55040](/schnittstellen/202604/pruefi/UTILMD/PI_55040) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55041](/schnittstellen/202604/pruefi/UTILMD/PI_55041) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55042](/schnittstellen/202604/pruefi/UTILMD/PI_55042) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55044](/schnittstellen/202604/pruefi/UTILMD/PI_55044) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55051](/schnittstellen/202604/pruefi/UTILMD/PI_55051) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55052](/schnittstellen/202604/pruefi/UTILMD/PI_55052) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55053](/schnittstellen/202604/pruefi/UTILMD/PI_55053) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55060](/schnittstellen/202604/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55074](/schnittstellen/202604/pruefi/UTILMD/PI_55074) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55075](/schnittstellen/202604/pruefi/UTILMD/PI_55075) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55077](/schnittstellen/202604/pruefi/UTILMD/PI_55077) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55078](/schnittstellen/202604/pruefi/UTILMD/PI_55078) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55080](/schnittstellen/202604/pruefi/UTILMD/PI_55080) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55095](/schnittstellen/202604/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55109](/schnittstellen/202604/pruefi/UTILMD/PI_55109) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55110](/schnittstellen/202604/pruefi/UTILMD/PI_55110) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55126](/schnittstellen/202604/pruefi/UTILMD/PI_55126) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55136](/schnittstellen/202604/pruefi/UTILMD/PI_55136) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55137](/schnittstellen/202604/pruefi/UTILMD/PI_55137) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55156](/schnittstellen/202604/pruefi/UTILMD/PI_55156) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55170](/schnittstellen/202604/pruefi/UTILMD/PI_55170) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55173](/schnittstellen/202604/pruefi/UTILMD/PI_55173) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55175](/schnittstellen/202604/pruefi/UTILMD/PI_55175) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55177](/schnittstellen/202604/pruefi/UTILMD/PI_55177) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55180](/schnittstellen/202604/pruefi/UTILMD/PI_55180) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55194](/schnittstellen/202604/pruefi/UTILMD/PI_55194) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55218](/schnittstellen/202604/pruefi/UTILMD/PI_55218) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55220](/schnittstellen/202604/pruefi/UTILMD/PI_55220) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55225](/schnittstellen/202604/pruefi/UTILMD/PI_55225) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55227](/schnittstellen/202604/pruefi/UTILMD/PI_55227) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55230](/schnittstellen/202604/pruefi/UTILMD/PI_55230) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55232](/schnittstellen/202604/pruefi/UTILMD/PI_55232) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55553](/schnittstellen/202604/pruefi/UTILMD/PI_55553) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55555](/schnittstellen/202604/pruefi/UTILMD/PI_55555) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55557](/schnittstellen/202604/pruefi/UTILMD/PI_55557) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55559](/schnittstellen/202604/pruefi/UTILMD/PI_55559) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55600](/schnittstellen/202604/pruefi/UTILMD/PI_55600) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55601](/schnittstellen/202604/pruefi/UTILMD/PI_55601) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55602](/schnittstellen/202604/pruefi/UTILMD/PI_55602) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55603](/schnittstellen/202604/pruefi/UTILMD/PI_55603) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55604](/schnittstellen/202604/pruefi/UTILMD/PI_55604) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55605](/schnittstellen/202604/pruefi/UTILMD/PI_55605) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55607](/schnittstellen/202604/pruefi/UTILMD/PI_55607) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55608](/schnittstellen/202604/pruefi/UTILMD/PI_55608) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55609](/schnittstellen/202604/pruefi/UTILMD/PI_55609) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55611](/schnittstellen/202604/pruefi/UTILMD/PI_55611) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55613](/schnittstellen/202604/pruefi/UTILMD/PI_55613) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55614](/schnittstellen/202604/pruefi/UTILMD/PI_55614) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55615](/schnittstellen/202604/pruefi/UTILMD/PI_55615) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55616](/schnittstellen/202604/pruefi/UTILMD/PI_55616) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55617](/schnittstellen/202604/pruefi/UTILMD/PI_55617) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55618](/schnittstellen/202604/pruefi/UTILMD/PI_55618) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55619](/schnittstellen/202604/pruefi/UTILMD/PI_55619) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55620](/schnittstellen/202604/pruefi/UTILMD/PI_55620) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55621](/schnittstellen/202604/pruefi/UTILMD/PI_55621) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55622](/schnittstellen/202604/pruefi/UTILMD/PI_55622) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55623](/schnittstellen/202604/pruefi/UTILMD/PI_55623) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55624](/schnittstellen/202604/pruefi/UTILMD/PI_55624) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55625](/schnittstellen/202604/pruefi/UTILMD/PI_55625) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55626](/schnittstellen/202604/pruefi/UTILMD/PI_55626) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55627](/schnittstellen/202604/pruefi/UTILMD/PI_55627) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55628](/schnittstellen/202604/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55629](/schnittstellen/202604/pruefi/UTILMD/PI_55629) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55630](/schnittstellen/202604/pruefi/UTILMD/PI_55630) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55632](/schnittstellen/202604/pruefi/UTILMD/PI_55632) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55633](/schnittstellen/202604/pruefi/UTILMD/PI_55633) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55634](/schnittstellen/202604/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55635](/schnittstellen/202604/pruefi/UTILMD/PI_55635) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55636](/schnittstellen/202604/pruefi/UTILMD/PI_55636) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55638](/schnittstellen/202604/pruefi/UTILMD/PI_55638) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55639](/schnittstellen/202604/pruefi/UTILMD/PI_55639) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55640](/schnittstellen/202604/pruefi/UTILMD/PI_55640) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55641](/schnittstellen/202604/pruefi/UTILMD/PI_55641) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55642](/schnittstellen/202604/pruefi/UTILMD/PI_55642) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55643](/schnittstellen/202604/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55644](/schnittstellen/202604/pruefi/UTILMD/PI_55644) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55645](/schnittstellen/202604/pruefi/UTILMD/PI_55645) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55646](/schnittstellen/202604/pruefi/UTILMD/PI_55646) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55647](/schnittstellen/202604/pruefi/UTILMD/PI_55647) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55648](/schnittstellen/202604/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55649](/schnittstellen/202604/pruefi/UTILMD/PI_55649) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55650](/schnittstellen/202604/pruefi/UTILMD/PI_55650) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55651](/schnittstellen/202604/pruefi/UTILMD/PI_55651) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55652](/schnittstellen/202604/pruefi/UTILMD/PI_55652) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55653](/schnittstellen/202604/pruefi/UTILMD/PI_55653) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55654](/schnittstellen/202604/pruefi/UTILMD/PI_55654) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55655](/schnittstellen/202604/pruefi/UTILMD/PI_55655) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55656](/schnittstellen/202604/pruefi/UTILMD/PI_55656) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55657](/schnittstellen/202604/pruefi/UTILMD/PI_55657) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55658](/schnittstellen/202604/pruefi/UTILMD/PI_55658) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55659](/schnittstellen/202604/pruefi/UTILMD/PI_55659) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55660](/schnittstellen/202604/pruefi/UTILMD/PI_55660) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55661](/schnittstellen/202604/pruefi/UTILMD/PI_55661) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55662](/schnittstellen/202604/pruefi/UTILMD/PI_55662) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55663](/schnittstellen/202604/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55664](/schnittstellen/202604/pruefi/UTILMD/PI_55664) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55665](/schnittstellen/202604/pruefi/UTILMD/PI_55665) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55666](/schnittstellen/202604/pruefi/UTILMD/PI_55666) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55667](/schnittstellen/202604/pruefi/UTILMD/PI_55667) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55669](/schnittstellen/202604/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55670](/schnittstellen/202604/pruefi/UTILMD/PI_55670) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55672](/schnittstellen/202604/pruefi/UTILMD/PI_55672) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55673](/schnittstellen/202604/pruefi/UTILMD/PI_55673) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55674](/schnittstellen/202604/pruefi/UTILMD/PI_55674) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55684](/schnittstellen/202604/pruefi/UTILMD/PI_55684) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55686](/schnittstellen/202604/pruefi/UTILMD/PI_55686) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55688](/schnittstellen/202604/pruefi/UTILMD/PI_55688) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55690](/schnittstellen/202604/pruefi/UTILMD/PI_55690) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55691](/schnittstellen/202604/pruefi/UTILMD/PI_55691) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55692](/schnittstellen/202604/pruefi/UTILMD/PI_55692) | Prüfi | UTILMD | transaktionsdaten |

### dokumentennummer

362 Verwendung(en) in den Nachrichtentypen APERAK, COMDIS, IFTSTA, INSRPT, INVOIC, MSCONS, ORDCHG, ORDERS, ORDRSP, PARTIN, PRICAT, QUOTES, REQOTE, UTILMD, UTILMD_GAS, UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_13002](/schnittstellen/202604/pruefi/MSCONS/PI_13002) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13006](/schnittstellen/202604/pruefi/MSCONS/PI_13006) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13007](/schnittstellen/202604/pruefi/MSCONS/PI_13007) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13008](/schnittstellen/202604/pruefi/MSCONS/PI_13008) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13009](/schnittstellen/202604/pruefi/MSCONS/PI_13009) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13015](/schnittstellen/202604/pruefi/MSCONS/PI_13015) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13016](/schnittstellen/202604/pruefi/MSCONS/PI_13016) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13017](/schnittstellen/202604/pruefi/MSCONS/PI_13017) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13018](/schnittstellen/202604/pruefi/MSCONS/PI_13018) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13019](/schnittstellen/202604/pruefi/MSCONS/PI_13019) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13025](/schnittstellen/202604/pruefi/MSCONS/PI_13025) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13027](/schnittstellen/202604/pruefi/MSCONS/PI_13027) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13028](/schnittstellen/202604/pruefi/MSCONS/PI_13028) | Prüfi | MSCONS | transaktionsdaten |
| [PI_15001](/schnittstellen/202604/pruefi/QUOTES/PI_15001) | Prüfi | QUOTES | transaktionsdaten |
| [PI_15003](/schnittstellen/202604/pruefi/QUOTES/PI_15003) | Prüfi | QUOTES | transaktionsdaten |
| [PI_15004](/schnittstellen/202604/pruefi/QUOTES/PI_15004) | Prüfi | QUOTES | transaktionsdaten |
| [PI_17001](/schnittstellen/202604/pruefi/ORDERS/PI_17001) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17002](/schnittstellen/202604/pruefi/ORDERS/PI_17002) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17003](/schnittstellen/202604/pruefi/ORDERS/PI_17003) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17004](/schnittstellen/202604/pruefi/ORDERS/PI_17004) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17005](/schnittstellen/202604/pruefi/ORDERS/PI_17005) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17006](/schnittstellen/202604/pruefi/ORDERS/PI_17006) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17009](/schnittstellen/202604/pruefi/ORDERS/PI_17009) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17101](/schnittstellen/202604/pruefi/ORDERS/PI_17101) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17102](/schnittstellen/202604/pruefi/ORDERS/PI_17102) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17103](/schnittstellen/202604/pruefi/ORDERS/PI_17103) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17104](/schnittstellen/202604/pruefi/ORDERS/PI_17104) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17113](/schnittstellen/202604/pruefi/ORDERS/PI_17113) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17115](/schnittstellen/202604/pruefi/ORDERS/PI_17115) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17116](/schnittstellen/202604/pruefi/ORDERS/PI_17116) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17117](/schnittstellen/202604/pruefi/ORDERS/PI_17117) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17118](/schnittstellen/202604/pruefi/ORDERS/PI_17118) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17120](/schnittstellen/202604/pruefi/ORDERS/PI_17120) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17121](/schnittstellen/202604/pruefi/ORDERS/PI_17121) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17122](/schnittstellen/202604/pruefi/ORDERS/PI_17122) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17123](/schnittstellen/202604/pruefi/ORDERS/PI_17123) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17126](/schnittstellen/202604/pruefi/ORDERS/PI_17126) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17128](/schnittstellen/202604/pruefi/ORDERS/PI_17128) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17129](/schnittstellen/202604/pruefi/ORDERS/PI_17129) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17130](/schnittstellen/202604/pruefi/ORDERS/PI_17130) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17131](/schnittstellen/202604/pruefi/ORDERS/PI_17131) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17132](/schnittstellen/202604/pruefi/ORDERS/PI_17132) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17133](/schnittstellen/202604/pruefi/ORDERS/PI_17133) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17134](/schnittstellen/202604/pruefi/ORDERS/PI_17134) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17135](/schnittstellen/202604/pruefi/ORDERS/PI_17135) | Prüfi | ORDERS | transaktionsdaten |
| [PI_19001](/schnittstellen/202604/pruefi/ORDRSP/PI_19001) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19002](/schnittstellen/202604/pruefi/ORDRSP/PI_19002) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19003](/schnittstellen/202604/pruefi/ORDRSP/PI_19003) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19004](/schnittstellen/202604/pruefi/ORDRSP/PI_19004) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19005](/schnittstellen/202604/pruefi/ORDRSP/PI_19005) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19006](/schnittstellen/202604/pruefi/ORDRSP/PI_19006) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19007](/schnittstellen/202604/pruefi/ORDRSP/PI_19007) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19009](/schnittstellen/202604/pruefi/ORDRSP/PI_19009) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19010](/schnittstellen/202604/pruefi/ORDRSP/PI_19010) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19011](/schnittstellen/202604/pruefi/ORDRSP/PI_19011) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19012](/schnittstellen/202604/pruefi/ORDRSP/PI_19012) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19013](/schnittstellen/202604/pruefi/ORDRSP/PI_19013) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19014](/schnittstellen/202604/pruefi/ORDRSP/PI_19014) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19015](/schnittstellen/202604/pruefi/ORDRSP/PI_19015) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19016](/schnittstellen/202604/pruefi/ORDRSP/PI_19016) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19101](/schnittstellen/202604/pruefi/ORDRSP/PI_19101) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19102](/schnittstellen/202604/pruefi/ORDRSP/PI_19102) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19103](/schnittstellen/202604/pruefi/ORDRSP/PI_19103) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19104](/schnittstellen/202604/pruefi/ORDRSP/PI_19104) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19114](/schnittstellen/202604/pruefi/ORDRSP/PI_19114) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19116](/schnittstellen/202604/pruefi/ORDRSP/PI_19116) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19117](/schnittstellen/202604/pruefi/ORDRSP/PI_19117) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19118](/schnittstellen/202604/pruefi/ORDRSP/PI_19118) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19119](/schnittstellen/202604/pruefi/ORDRSP/PI_19119) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19121](/schnittstellen/202604/pruefi/ORDRSP/PI_19121) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19123](/schnittstellen/202604/pruefi/ORDRSP/PI_19123) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19124](/schnittstellen/202604/pruefi/ORDRSP/PI_19124) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19128](/schnittstellen/202604/pruefi/ORDRSP/PI_19128) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19129](/schnittstellen/202604/pruefi/ORDRSP/PI_19129) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19133](/schnittstellen/202604/pruefi/ORDRSP/PI_19133) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19301](/schnittstellen/202604/pruefi/ORDRSP/PI_19301) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19302](/schnittstellen/202604/pruefi/ORDRSP/PI_19302) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_21007](/schnittstellen/202604/pruefi/IFTSTA/PI_21007) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21009](/schnittstellen/202604/pruefi/IFTSTA/PI_21009) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21010](/schnittstellen/202604/pruefi/IFTSTA/PI_21010) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21011](/schnittstellen/202604/pruefi/IFTSTA/PI_21011) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21012](/schnittstellen/202604/pruefi/IFTSTA/PI_21012) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21013](/schnittstellen/202604/pruefi/IFTSTA/PI_21013) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21015](/schnittstellen/202604/pruefi/IFTSTA/PI_21015) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21018](/schnittstellen/202604/pruefi/IFTSTA/PI_21018) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21024](/schnittstellen/202604/pruefi/IFTSTA/PI_21024) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21025](/schnittstellen/202604/pruefi/IFTSTA/PI_21025) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21026](/schnittstellen/202604/pruefi/IFTSTA/PI_21026) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21027](/schnittstellen/202604/pruefi/IFTSTA/PI_21027) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21028](/schnittstellen/202604/pruefi/IFTSTA/PI_21028) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21029](/schnittstellen/202604/pruefi/IFTSTA/PI_21029) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21030](/schnittstellen/202604/pruefi/IFTSTA/PI_21030) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21031](/schnittstellen/202604/pruefi/IFTSTA/PI_21031) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21032](/schnittstellen/202604/pruefi/IFTSTA/PI_21032) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21033](/schnittstellen/202604/pruefi/IFTSTA/PI_21033) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21035](/schnittstellen/202604/pruefi/IFTSTA/PI_21035) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21036](/schnittstellen/202604/pruefi/IFTSTA/PI_21036) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21039](/schnittstellen/202604/pruefi/IFTSTA/PI_21039) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21040](/schnittstellen/202604/pruefi/IFTSTA/PI_21040) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21043](/schnittstellen/202604/pruefi/IFTSTA/PI_21043) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21044](/schnittstellen/202604/pruefi/IFTSTA/PI_21044) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21045](/schnittstellen/202604/pruefi/IFTSTA/PI_21045) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21047](/schnittstellen/202604/pruefi/IFTSTA/PI_21047) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_23001](/schnittstellen/202604/pruefi/INSRPT/PI_23001) | Prüfi | INSRPT | transaktionsdaten |
| [PI_23003](/schnittstellen/202604/pruefi/INSRPT/PI_23003) | Prüfi | INSRPT | transaktionsdaten |
| [PI_23004](/schnittstellen/202604/pruefi/INSRPT/PI_23004) | Prüfi | INSRPT | transaktionsdaten |
| [PI_23005](/schnittstellen/202604/pruefi/INSRPT/PI_23005) | Prüfi | INSRPT | transaktionsdaten |
| [PI_23008](/schnittstellen/202604/pruefi/INSRPT/PI_23008) | Prüfi | INSRPT | transaktionsdaten |
| [PI_23009](/schnittstellen/202604/pruefi/INSRPT/PI_23009) | Prüfi | INSRPT | transaktionsdaten |
| [PI_23011](/schnittstellen/202604/pruefi/INSRPT/PI_23011) | Prüfi | INSRPT | transaktionsdaten |
| [PI_23012](/schnittstellen/202604/pruefi/INSRPT/PI_23012) | Prüfi | INSRPT | transaktionsdaten |
| [PI_25001](/schnittstellen/202604/pruefi/UTILTS/PI_25001) | Prüfi | UTILTS | transaktionsdaten |
| [PI_25004](/schnittstellen/202604/pruefi/UTILTS/PI_25004) | Prüfi | UTILTS | transaktionsdaten |
| [PI_25005](/schnittstellen/202604/pruefi/UTILTS/PI_25005) | Prüfi | UTILTS | transaktionsdaten |
| [PI_25006](/schnittstellen/202604/pruefi/UTILTS/PI_25006) | Prüfi | UTILTS | transaktionsdaten |
| [PI_25007](/schnittstellen/202604/pruefi/UTILTS/PI_25007) | Prüfi | UTILTS | transaktionsdaten |
| [PI_25008](/schnittstellen/202604/pruefi/UTILTS/PI_25008) | Prüfi | UTILTS | transaktionsdaten |
| [PI_25009](/schnittstellen/202604/pruefi/UTILTS/PI_25009) | Prüfi | UTILTS | transaktionsdaten |
| [PI_25010](/schnittstellen/202604/pruefi/UTILTS/PI_25010) | Prüfi | UTILTS | transaktionsdaten |
| [PI_27002](/schnittstellen/202604/pruefi/PRICAT/PI_27002) | Prüfi | PRICAT | transaktionsdaten |
| [PI_27003](/schnittstellen/202604/pruefi/PRICAT/PI_27003) | Prüfi | PRICAT | transaktionsdaten |
| [PI_29001](/schnittstellen/202604/pruefi/COMDIS/PI_29001) | Prüfi | COMDIS | transaktionsdaten |
| [PI_29002](/schnittstellen/202604/pruefi/COMDIS/PI_29002) | Prüfi | COMDIS | transaktionsdaten |
| [PI_31002](/schnittstellen/202604/pruefi/INVOIC/PI_31002) | Prüfi | INVOIC | transaktionsdaten |
| [PI_35001](/schnittstellen/202604/pruefi/REQOTE/PI_35001) | Prüfi | REQOTE | transaktionsdaten |
| [PI_35002](/schnittstellen/202604/pruefi/REQOTE/PI_35002) | Prüfi | REQOTE | transaktionsdaten |
| [PI_35004](/schnittstellen/202604/pruefi/REQOTE/PI_35004) | Prüfi | REQOTE | transaktionsdaten |
| [PI_37000](/schnittstellen/202604/pruefi/PARTIN/PI_37000) | Prüfi | PARTIN | transaktionsdaten |
| [PI_37001](/schnittstellen/202604/pruefi/PARTIN/PI_37001) | Prüfi | PARTIN | transaktionsdaten |
| [PI_37002](/schnittstellen/202604/pruefi/PARTIN/PI_37002) | Prüfi | PARTIN | transaktionsdaten |
| [PI_37008](/schnittstellen/202604/pruefi/PARTIN/PI_37008) | Prüfi | PARTIN | transaktionsdaten |
| [PI_37009](/schnittstellen/202604/pruefi/PARTIN/PI_37009) | Prüfi | PARTIN | transaktionsdaten |
| [PI_37010](/schnittstellen/202604/pruefi/PARTIN/PI_37010) | Prüfi | PARTIN | transaktionsdaten |
| [PI_37012](/schnittstellen/202604/pruefi/PARTIN/PI_37012) | Prüfi | PARTIN | transaktionsdaten |
| [PI_37013](/schnittstellen/202604/pruefi/PARTIN/PI_37013) | Prüfi | PARTIN | transaktionsdaten |
| [PI_37014](/schnittstellen/202604/pruefi/PARTIN/PI_37014) | Prüfi | PARTIN | transaktionsdaten |
| [PI_39000](/schnittstellen/202604/pruefi/ORDCHG/PI_39000) | Prüfi | ORDCHG | transaktionsdaten |
| [PI_39001](/schnittstellen/202604/pruefi/ORDCHG/PI_39001) | Prüfi | ORDCHG | transaktionsdaten |
| [PI_44001](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44001) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44003](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44003) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44004](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44004) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44005](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44005) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44006](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44006) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44007](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44007) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44008](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44008) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44009](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44009) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44010](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44010) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44011](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44011) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44012](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44012) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44015](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44015) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44016](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44016) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44017](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44017) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44018](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44018) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44019](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44019) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44020](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44020) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44021](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44021) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44022](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44022) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44023](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44023) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44024](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44024) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44035](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44035) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44036](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44036) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44037](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44037) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44038](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44038) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44039](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44039) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44040](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44040) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44041](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44041) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44043](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44043) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44044](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44044) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44052](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44052) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44053](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44053) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44060](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44060) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44101](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44101) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44102](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44102) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44103](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44103) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44104](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44104) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44109](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44109) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44111](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44111) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44112](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44112) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44113](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44113) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44115](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44115) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44116](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44116) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44117](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44117) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44119](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44119) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44120](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44120) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44121](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44121) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44123](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44123) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44124](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44124) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44137](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44137) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44138](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44138) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44139](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44139) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44140](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44140) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44142](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44142) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44143](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44143) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44145](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44145) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44146](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44146) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44147](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44147) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44148](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44148) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44149](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44149) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44150](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44150) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44151](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44151) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44152](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44152) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44156](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44156) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44157](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44157) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44159](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44159) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44160](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44160) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44161](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44161) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44162](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44162) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44163](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44163) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44164](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44164) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44165](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44165) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44166](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44166) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44167](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44167) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44168](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44175](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44175) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44176](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44176) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44180](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44180) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44181](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44181) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44182](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44182) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_55001](/schnittstellen/202604/pruefi/UTILMD/PI_55001) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55002](/schnittstellen/202604/pruefi/UTILMD/PI_55002) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55003](/schnittstellen/202604/pruefi/UTILMD/PI_55003) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55004](/schnittstellen/202604/pruefi/UTILMD/PI_55004) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55005](/schnittstellen/202604/pruefi/UTILMD/PI_55005) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55006](/schnittstellen/202604/pruefi/UTILMD/PI_55006) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55007](/schnittstellen/202604/pruefi/UTILMD/PI_55007) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55008](/schnittstellen/202604/pruefi/UTILMD/PI_55008) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55009](/schnittstellen/202604/pruefi/UTILMD/PI_55009) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55010](/schnittstellen/202604/pruefi/UTILMD/PI_55010) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55011](/schnittstellen/202604/pruefi/UTILMD/PI_55011) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55012](/schnittstellen/202604/pruefi/UTILMD/PI_55012) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55013](/schnittstellen/202604/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55014](/schnittstellen/202604/pruefi/UTILMD/PI_55014) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55015](/schnittstellen/202604/pruefi/UTILMD/PI_55015) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55016](/schnittstellen/202604/pruefi/UTILMD/PI_55016) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55017](/schnittstellen/202604/pruefi/UTILMD/PI_55017) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55018](/schnittstellen/202604/pruefi/UTILMD/PI_55018) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55022](/schnittstellen/202604/pruefi/UTILMD/PI_55022) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55023](/schnittstellen/202604/pruefi/UTILMD/PI_55023) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55024](/schnittstellen/202604/pruefi/UTILMD/PI_55024) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55035](/schnittstellen/202604/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55036](/schnittstellen/202604/pruefi/UTILMD/PI_55036) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55037](/schnittstellen/202604/pruefi/UTILMD/PI_55037) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55038](/schnittstellen/202604/pruefi/UTILMD/PI_55038) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55039](/schnittstellen/202604/pruefi/UTILMD/PI_55039) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55040](/schnittstellen/202604/pruefi/UTILMD/PI_55040) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55041](/schnittstellen/202604/pruefi/UTILMD/PI_55041) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55042](/schnittstellen/202604/pruefi/UTILMD/PI_55042) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55044](/schnittstellen/202604/pruefi/UTILMD/PI_55044) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55051](/schnittstellen/202604/pruefi/UTILMD/PI_55051) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55052](/schnittstellen/202604/pruefi/UTILMD/PI_55052) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55053](/schnittstellen/202604/pruefi/UTILMD/PI_55053) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55060](/schnittstellen/202604/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55074](/schnittstellen/202604/pruefi/UTILMD/PI_55074) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55075](/schnittstellen/202604/pruefi/UTILMD/PI_55075) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55077](/schnittstellen/202604/pruefi/UTILMD/PI_55077) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55078](/schnittstellen/202604/pruefi/UTILMD/PI_55078) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55080](/schnittstellen/202604/pruefi/UTILMD/PI_55080) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55095](/schnittstellen/202604/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55109](/schnittstellen/202604/pruefi/UTILMD/PI_55109) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55110](/schnittstellen/202604/pruefi/UTILMD/PI_55110) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55126](/schnittstellen/202604/pruefi/UTILMD/PI_55126) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55136](/schnittstellen/202604/pruefi/UTILMD/PI_55136) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55137](/schnittstellen/202604/pruefi/UTILMD/PI_55137) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55156](/schnittstellen/202604/pruefi/UTILMD/PI_55156) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55170](/schnittstellen/202604/pruefi/UTILMD/PI_55170) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55173](/schnittstellen/202604/pruefi/UTILMD/PI_55173) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55175](/schnittstellen/202604/pruefi/UTILMD/PI_55175) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55177](/schnittstellen/202604/pruefi/UTILMD/PI_55177) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55180](/schnittstellen/202604/pruefi/UTILMD/PI_55180) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55194](/schnittstellen/202604/pruefi/UTILMD/PI_55194) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55218](/schnittstellen/202604/pruefi/UTILMD/PI_55218) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55220](/schnittstellen/202604/pruefi/UTILMD/PI_55220) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55225](/schnittstellen/202604/pruefi/UTILMD/PI_55225) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55227](/schnittstellen/202604/pruefi/UTILMD/PI_55227) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55230](/schnittstellen/202604/pruefi/UTILMD/PI_55230) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55232](/schnittstellen/202604/pruefi/UTILMD/PI_55232) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55553](/schnittstellen/202604/pruefi/UTILMD/PI_55553) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55555](/schnittstellen/202604/pruefi/UTILMD/PI_55555) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55557](/schnittstellen/202604/pruefi/UTILMD/PI_55557) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55559](/schnittstellen/202604/pruefi/UTILMD/PI_55559) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55600](/schnittstellen/202604/pruefi/UTILMD/PI_55600) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55601](/schnittstellen/202604/pruefi/UTILMD/PI_55601) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55602](/schnittstellen/202604/pruefi/UTILMD/PI_55602) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55603](/schnittstellen/202604/pruefi/UTILMD/PI_55603) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55604](/schnittstellen/202604/pruefi/UTILMD/PI_55604) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55605](/schnittstellen/202604/pruefi/UTILMD/PI_55605) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55607](/schnittstellen/202604/pruefi/UTILMD/PI_55607) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55608](/schnittstellen/202604/pruefi/UTILMD/PI_55608) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55609](/schnittstellen/202604/pruefi/UTILMD/PI_55609) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55611](/schnittstellen/202604/pruefi/UTILMD/PI_55611) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55613](/schnittstellen/202604/pruefi/UTILMD/PI_55613) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55614](/schnittstellen/202604/pruefi/UTILMD/PI_55614) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55615](/schnittstellen/202604/pruefi/UTILMD/PI_55615) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55616](/schnittstellen/202604/pruefi/UTILMD/PI_55616) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55617](/schnittstellen/202604/pruefi/UTILMD/PI_55617) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55618](/schnittstellen/202604/pruefi/UTILMD/PI_55618) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55619](/schnittstellen/202604/pruefi/UTILMD/PI_55619) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55620](/schnittstellen/202604/pruefi/UTILMD/PI_55620) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55621](/schnittstellen/202604/pruefi/UTILMD/PI_55621) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55622](/schnittstellen/202604/pruefi/UTILMD/PI_55622) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55623](/schnittstellen/202604/pruefi/UTILMD/PI_55623) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55624](/schnittstellen/202604/pruefi/UTILMD/PI_55624) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55625](/schnittstellen/202604/pruefi/UTILMD/PI_55625) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55626](/schnittstellen/202604/pruefi/UTILMD/PI_55626) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55627](/schnittstellen/202604/pruefi/UTILMD/PI_55627) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55628](/schnittstellen/202604/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55629](/schnittstellen/202604/pruefi/UTILMD/PI_55629) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55630](/schnittstellen/202604/pruefi/UTILMD/PI_55630) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55632](/schnittstellen/202604/pruefi/UTILMD/PI_55632) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55633](/schnittstellen/202604/pruefi/UTILMD/PI_55633) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55634](/schnittstellen/202604/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55635](/schnittstellen/202604/pruefi/UTILMD/PI_55635) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55636](/schnittstellen/202604/pruefi/UTILMD/PI_55636) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55638](/schnittstellen/202604/pruefi/UTILMD/PI_55638) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55639](/schnittstellen/202604/pruefi/UTILMD/PI_55639) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55640](/schnittstellen/202604/pruefi/UTILMD/PI_55640) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55641](/schnittstellen/202604/pruefi/UTILMD/PI_55641) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55642](/schnittstellen/202604/pruefi/UTILMD/PI_55642) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55643](/schnittstellen/202604/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55644](/schnittstellen/202604/pruefi/UTILMD/PI_55644) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55645](/schnittstellen/202604/pruefi/UTILMD/PI_55645) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55646](/schnittstellen/202604/pruefi/UTILMD/PI_55646) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55647](/schnittstellen/202604/pruefi/UTILMD/PI_55647) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55648](/schnittstellen/202604/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55649](/schnittstellen/202604/pruefi/UTILMD/PI_55649) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55650](/schnittstellen/202604/pruefi/UTILMD/PI_55650) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55651](/schnittstellen/202604/pruefi/UTILMD/PI_55651) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55652](/schnittstellen/202604/pruefi/UTILMD/PI_55652) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55653](/schnittstellen/202604/pruefi/UTILMD/PI_55653) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55654](/schnittstellen/202604/pruefi/UTILMD/PI_55654) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55655](/schnittstellen/202604/pruefi/UTILMD/PI_55655) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55656](/schnittstellen/202604/pruefi/UTILMD/PI_55656) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55657](/schnittstellen/202604/pruefi/UTILMD/PI_55657) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55658](/schnittstellen/202604/pruefi/UTILMD/PI_55658) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55659](/schnittstellen/202604/pruefi/UTILMD/PI_55659) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55660](/schnittstellen/202604/pruefi/UTILMD/PI_55660) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55661](/schnittstellen/202604/pruefi/UTILMD/PI_55661) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55662](/schnittstellen/202604/pruefi/UTILMD/PI_55662) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55663](/schnittstellen/202604/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55664](/schnittstellen/202604/pruefi/UTILMD/PI_55664) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55665](/schnittstellen/202604/pruefi/UTILMD/PI_55665) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55666](/schnittstellen/202604/pruefi/UTILMD/PI_55666) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55667](/schnittstellen/202604/pruefi/UTILMD/PI_55667) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55669](/schnittstellen/202604/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55670](/schnittstellen/202604/pruefi/UTILMD/PI_55670) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55672](/schnittstellen/202604/pruefi/UTILMD/PI_55672) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55673](/schnittstellen/202604/pruefi/UTILMD/PI_55673) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55674](/schnittstellen/202604/pruefi/UTILMD/PI_55674) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55684](/schnittstellen/202604/pruefi/UTILMD/PI_55684) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55686](/schnittstellen/202604/pruefi/UTILMD/PI_55686) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55688](/schnittstellen/202604/pruefi/UTILMD/PI_55688) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55690](/schnittstellen/202604/pruefi/UTILMD/PI_55690) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55691](/schnittstellen/202604/pruefi/UTILMD/PI_55691) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55692](/schnittstellen/202604/pruefi/UTILMD/PI_55692) | Prüfi | UTILMD | transaktionsdaten |
| [PI_66666](/schnittstellen/202604/pruefi/APERAK/PI_66666) | Prüfi | APERAK | transaktionsdaten |
| [PI_99999](/schnittstellen/202604/pruefi/APERAK/PI_99999) | Prüfi | APERAK | transaktionsdaten |

### kategorie

334 Verwendung(en) in den Nachrichtentypen APERAK, COMDIS, MSCONS, PARTIN, PRICAT, QUOTES, REQOTE, UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [[LF] START_ABO_PROFILE](/schnittstellen/202604/trigger/events/LF-START_ABO_PROFILE) | Event | — | transaktionsdaten |
| [[LF] START_ABR_NN](/schnittstellen/202604/trigger/events/LF-START_ABR_NN) | Event | — | transaktionsdaten |
| [[LF] START_ANFORDERUNG_VON_WERTEN](/schnittstellen/202604/trigger/events/LF-START_ANFORDERUNG_VON_WERTEN) | Event | — | transaktionsdaten |
| [[LF] START_ANFRAGE_KONFIGURATION](/schnittstellen/202604/trigger/events/LF-START_ANFRAGE_KONFIGURATION) | Event | — | transaktionsdaten |
| [[LF] START_ANFRAGE_MESSWERTE](/schnittstellen/202604/trigger/events/LF-START_ANFRAGE_MESSWERTE) | Event | — | transaktionsdaten |
| [[LF] START_ANFRAGE_SPERRUNG](/schnittstellen/202604/trigger/events/LF-START_ANFRAGE_SPERRUNG) | Event | — | transaktionsdaten |
| [[LF] START_ANFRAGE_STAMMDATENAENDERUNG GAS](/schnittstellen/202604/trigger/events/LF-START_ANFRAGE_STAMMDATENAENDERUNG-GAS) | Event | — | transaktionsdaten |
| [[LF] START_ANFRAGE_STAMMDATEN_MALO](/schnittstellen/202604/trigger/events/LF-START_ANFRAGE_STAMMDATEN_MALO) | Event | — | transaktionsdaten |
| [[LF] START_ANFRAGE_STAMMDATEN_TRANCHE](/schnittstellen/202604/trigger/events/LF-START_ANFRAGE_STAMMDATEN_TRANCHE) | Event | — | transaktionsdaten |
| [[LF] START_BESTELLUNG_ABRECHNUNGSDATEN](/schnittstellen/202604/trigger/events/LF-START_BESTELLUNG_ABRECHNUNGSDATEN) | Event | — | transaktionsdaten |
| [[LF] START_BESTELLUNG_ANGEBOT_KONFIGURATION](/schnittstellen/202604/trigger/events/LF-START_BESTELLUNG_ANGEBOT_KONFIGURATION) | Event | — | transaktionsdaten |
| [[LF] START_BESTELLUNG_KONFIGURATION](/schnittstellen/202604/trigger/events/LF-START_BESTELLUNG_KONFIGURATION) | Event | — | transaktionsdaten |
| [[LF] START_BESTELLUNG_SDAE](/schnittstellen/202604/trigger/events/LF-START_BESTELLUNG_SDAE) | Event | — | transaktionsdaten |
| [[LF] START_BESTELLUNG_ZAEHLZEITDEFINITION](/schnittstellen/202604/trigger/events/LF-START_BESTELLUNG_ZAEHLZEITDEFINITION) | Event | — | transaktionsdaten |
| [[LF] START_BEST_AEND_TK](/schnittstellen/202604/trigger/events/LF-START_BEST_AEND_TK) | Event | — | transaktionsdaten |
| [[LF] START_ENTSPERRAUFTRAG](/schnittstellen/202604/trigger/events/LF-START_ENTSPERRAUFTRAG) | Event | — | transaktionsdaten |
| [[LF] START_ERHEBUNG_MESSWERTE](/schnittstellen/202604/trigger/events/LF-START_ERHEBUNG_MESSWERTE) | Event | — | transaktionsdaten |
| [[LF] START_GESCHAEFTSDATENANFRAGE](/schnittstellen/202604/trigger/events/LF-START_GESCHAEFTSDATENANFRAGE) | Event | — | transaktionsdaten |
| [[LF] START_KUENDIGUNG](/schnittstellen/202604/trigger/events/LF-START_KUENDIGUNG) | Event | — | transaktionsdaten |
| [[LF] START_LIEFERBEGINN](/schnittstellen/202604/trigger/events/LF-START_LIEFERBEGINN) | Event | — | transaktionsdaten |
| [[LF] START_LIEFERENDE](/schnittstellen/202604/trigger/events/LF-START_LIEFERENDE) | Event | — | transaktionsdaten |
| [[LF] START_PARTIN](/schnittstellen/202604/trigger/events/LF-START_PARTIN) | Event | — | transaktionsdaten |
| [[LF] START_REKLAMATION_VON_WERTEN](/schnittstellen/202604/trigger/events/LF-START_REKLAMATION_VON_WERTEN) | Event | — | transaktionsdaten |
| [[LF] START_SPERRAUFTRAG](/schnittstellen/202604/trigger/events/LF-START_SPERRAUFTRAG) | Event | — | transaktionsdaten |
| [[LF] START_STORNO_AUFTRAG](/schnittstellen/202604/trigger/events/LF-START_STORNO_AUFTRAG) | Event | — | transaktionsdaten |
| [[LF] START_STORNO_SE_AUFTRAG](/schnittstellen/202604/trigger/events/LF-START_STORNO_SE_AUFTRAG) | Event | — | transaktionsdaten |
| [[LF] START_UEBERMITTLUNG_ENFG](/schnittstellen/202604/trigger/events/LF-START_UEBERMITTLUNG_ENFG) | Event | — | transaktionsdaten |
| [[LF] START_UEBERM_DEFINITION](/schnittstellen/202604/trigger/events/LF-START_UEBERM_DEFINITION) | Event | — | transaktionsdaten |
| [[LF] START_UEBERSICHT_LEISTUNGSKURVENDEF](/schnittstellen/202604/trigger/events/LF-START_UEBERSICHT_LEISTUNGSKURVENDEF) | Event | — | transaktionsdaten |
| [[LF] START_UEBERSICHT_SCHALTZEITDEF](/schnittstellen/202604/trigger/events/LF-START_UEBERSICHT_SCHALTZEITDEF) | Event | — | transaktionsdaten |
| [[LF] START_UEBERSICHT_ZAEHLZEITDEF](/schnittstellen/202604/trigger/events/LF-START_UEBERSICHT_ZAEHLZEITDEF) | Event | — | transaktionsdaten |
| [[LF] START_VERSAND_ANF_STORNO](/schnittstellen/202604/trigger/events/LF-START_VERSAND_ANF_STORNO) | Event | — | transaktionsdaten |
| [[LF] START_VERSAND_ANTWORT_NNA](/schnittstellen/202604/trigger/events/LF-START_VERSAND_ANTWORT_NNA) | Event | — | transaktionsdaten |
| [[LF] START_VERSAND_BEST_BEEND_KONFIG](/schnittstellen/202604/trigger/events/LF-START_VERSAND_BEST_BEEND_KONFIG) | Event | — | transaktionsdaten |
| [[LF] START_VERSAND_SDAE](/schnittstellen/202604/trigger/events/LF-START_VERSAND_SDAE) | Event | — | transaktionsdaten |
| [[LF] START_VERSAND_STOERUNGSMELDUNG](/schnittstellen/202604/trigger/events/LF-START_VERSAND_STOERUNGSMELDUNG) | Event | — | transaktionsdaten |
| [[LF] START_VERSAND_STORNO_MSCONS](/schnittstellen/202604/trigger/events/LF-START_VERSAND_STORNO_MSCONS) | Event | — | transaktionsdaten |
| [[MSB] START_ANGEBOT_GERAETEUEBERNAHME](/schnittstellen/202604/trigger/events/MSB-START_ANGEBOT_GERAETEUEBERNAHME) | Event | — | transaktionsdaten |
| [[MSB] START_ANTWORT_GERAETEWECHSEL](/schnittstellen/202604/trigger/events/MSB-START_ANTWORT_GERAETEWECHSEL) | Event | — | transaktionsdaten |
| [[MSB] START_BEGINN_MSB](/schnittstellen/202604/trigger/events/MSB-START_BEGINN_MSB) | Event | — | transaktionsdaten |
| [[MSB] START_BESTELLUNG_GERAETEUEBERNAHME](/schnittstellen/202604/trigger/events/MSB-START_BESTELLUNG_GERAETEUEBERNAHME) | Event | — | transaktionsdaten |
| [[MSB] START_BESTELLUNG_SDAE GAS](/schnittstellen/202604/trigger/events/MSB-START_BESTELLUNG_SDAE-GAS) | Event | — | transaktionsdaten |
| [[MSB] START_ERHEBUNG_MESSWERTE](/schnittstellen/202604/trigger/events/MSB-START_ERHEBUNG_MESSWERTE) | Event | — | transaktionsdaten |
| [[MSB] START_GERAETEUEBERNAHME](/schnittstellen/202604/trigger/events/MSB-START_GERAETEUEBERNAHME) | Event | — | transaktionsdaten |
| [[MSB] START_GERAETEWECHSEL](/schnittstellen/202604/trigger/events/MSB-START_GERAETEWECHSEL) | Event | — | transaktionsdaten |
| [[MSB] START_GESCHAEFTSDATENANFRAGE](/schnittstellen/202604/trigger/events/MSB-START_GESCHAEFTSDATENANFRAGE) | Event | — | transaktionsdaten |
| [[MSB] START_KUENDIGUNG_MSB](/schnittstellen/202604/trigger/events/MSB-START_KUENDIGUNG_MSB) | Event | — | transaktionsdaten |
| [[MSB] START_PARTIN](/schnittstellen/202604/trigger/events/MSB-START_PARTIN) | Event | — | transaktionsdaten |
| [[MSB] START_REKLAMATION_DEFINITION](/schnittstellen/202604/trigger/events/MSB-START_REKLAMATION_DEFINITION) | Event | — | transaktionsdaten |
| [[MSB] START_VERSAND_ANF_STORNO](/schnittstellen/202604/trigger/events/MSB-START_VERSAND_ANF_STORNO) | Event | — | transaktionsdaten |
| [[MSB] START_VERSAND_PREISBLATT_IMS](/schnittstellen/202604/trigger/events/MSB-START_VERSAND_PREISBLATT_IMS) | Event | — | transaktionsdaten |
| [[MSB] START_VERSAND_SDAE](/schnittstellen/202604/trigger/events/MSB-START_VERSAND_SDAE) | Event | — | transaktionsdaten |
| [[MSB] START_VERSAND_STORNO_MSCONS](/schnittstellen/202604/trigger/events/MSB-START_VERSAND_STORNO_MSCONS) | Event | — | transaktionsdaten |
| [[NB] START_ANFRAGE_MESSWERTE_NB](/schnittstellen/202604/trigger/events/NB-START_ANFRAGE_MESSWERTE_NB) | Event | — | transaktionsdaten |
| [[NB] START_ANFRAGE_SPERRUNG](/schnittstellen/202604/trigger/events/NB-START_ANFRAGE_SPERRUNG) | Event | — | transaktionsdaten |
| [[NB] START_ANFRAGE_STAMMDATENAENDERUNG GAS](/schnittstellen/202604/trigger/events/NB-START_ANFRAGE_STAMMDATENAENDERUNG-GAS) | Event | — | transaktionsdaten |
| [[NB] START_BERECHNUNGSFORMEL](/schnittstellen/202604/trigger/events/NB-START_BERECHNUNGSFORMEL) | Event | — | transaktionsdaten |
| [[NB] START_BEST_AEND_TK](/schnittstellen/202604/trigger/events/NB-START_BEST_AEND_TK) | Event | — | transaktionsdaten |
| [[NB] START_EINRICHTUNG_KONFIG](/schnittstellen/202604/trigger/events/NB-START_EINRICHTUNG_KONFIG) | Event | — | transaktionsdaten |
| [[NB] START_ENDE_MSB_STILLLEGUNG GAS](/schnittstellen/202604/trigger/events/NB-START_ENDE_MSB_STILLLEGUNG-GAS) | Event | — | transaktionsdaten |
| [[NB] START_EOG](/schnittstellen/202604/trigger/events/NB-START_EOG) | Event | — | transaktionsdaten |
| [[NB] START_ERHEBUNG_MESSWERTE](/schnittstellen/202604/trigger/events/NB-START_ERHEBUNG_MESSWERTE) | Event | — | transaktionsdaten |
| [[NB] START_LIEFERENDE](/schnittstellen/202604/trigger/events/NB-START_LIEFERENDE) | Event | — | transaktionsdaten |
| [[NB] START_PARTIN](/schnittstellen/202604/trigger/events/NB-START_PARTIN) | Event | — | transaktionsdaten |
| [[NB] START_PREISBLATT](/schnittstellen/202604/trigger/events/NB-START_PREISBLATT) | Event | — | transaktionsdaten |
| [[NB] START_REKLAMATION_DEFINITION](/schnittstellen/202604/trigger/events/NB-START_REKLAMATION_DEFINITION) | Event | — | transaktionsdaten |
| [[NB] START_UEBERM_DEFINITION](/schnittstellen/202604/trigger/events/NB-START_UEBERM_DEFINITION) | Event | — | transaktionsdaten |
| [[NB] START_UEBERSICHT_LEISTUNGSKURVENDEF](/schnittstellen/202604/trigger/events/NB-START_UEBERSICHT_LEISTUNGSKURVENDEF) | Event | — | transaktionsdaten |
| [[NB] START_UEBERSICHT_SCHALTZEITDEF](/schnittstellen/202604/trigger/events/NB-START_UEBERSICHT_SCHALTZEITDEF) | Event | — | transaktionsdaten |
| [[NB] START_UEBERSICHT_ZAEHLZEITDEF](/schnittstellen/202604/trigger/events/NB-START_UEBERSICHT_ZAEHLZEITDEF) | Event | — | transaktionsdaten |
| [[NB] START_VERSAND_ANF_STORNO](/schnittstellen/202604/trigger/events/NB-START_VERSAND_ANF_STORNO) | Event | — | transaktionsdaten |
| [[NB] START_VERSAND_COMDIS](/schnittstellen/202604/trigger/events/NB-START_VERSAND_COMDIS) | Event | — | transaktionsdaten |
| [[NB] START_VERSAND_LIEFERSCHEIN](/schnittstellen/202604/trigger/events/NB-START_VERSAND_LIEFERSCHEIN) | Event | — | transaktionsdaten |
| [[NB] START_VERSAND_SDAE](/schnittstellen/202604/trigger/events/NB-START_VERSAND_SDAE) | Event | — | transaktionsdaten |
| [[NB] START_VERSAND_STOERUNGSMELDUNG_NB](/schnittstellen/202604/trigger/events/NB-START_VERSAND_STOERUNGSMELDUNG_NB) | Event | — | transaktionsdaten |
| [[NB] START_VERSAND_STORNO_MSCONS](/schnittstellen/202604/trigger/events/NB-START_VERSAND_STORNO_MSCONS) | Event | — | transaktionsdaten |
| [[NB] START_WIEDERSPRUCH_ABLEHNUNG](/schnittstellen/202604/trigger/events/NB-START_WIEDERSPRUCH_ABLEHNUNG) | Event | — | transaktionsdaten |
| [[NB] START_ZUORDNUNG_ERZ_MALO_TRANCHE](/schnittstellen/202604/trigger/events/NB-START_ZUORDNUNG_ERZ_MALO_TRANCHE) | Event | — | transaktionsdaten |
| [PI_13002](/schnittstellen/202604/pruefi/MSCONS/PI_13002) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13006](/schnittstellen/202604/pruefi/MSCONS/PI_13006) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13007](/schnittstellen/202604/pruefi/MSCONS/PI_13007) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13008](/schnittstellen/202604/pruefi/MSCONS/PI_13008) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13009](/schnittstellen/202604/pruefi/MSCONS/PI_13009) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13015](/schnittstellen/202604/pruefi/MSCONS/PI_13015) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13016](/schnittstellen/202604/pruefi/MSCONS/PI_13016) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13017](/schnittstellen/202604/pruefi/MSCONS/PI_13017) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13018](/schnittstellen/202604/pruefi/MSCONS/PI_13018) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13019](/schnittstellen/202604/pruefi/MSCONS/PI_13019) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13025](/schnittstellen/202604/pruefi/MSCONS/PI_13025) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13027](/schnittstellen/202604/pruefi/MSCONS/PI_13027) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13028](/schnittstellen/202604/pruefi/MSCONS/PI_13028) | Prüfi | MSCONS | transaktionsdaten |
| [PI_15001](/schnittstellen/202604/pruefi/QUOTES/PI_15001) | Prüfi | QUOTES | transaktionsdaten |
| [PI_15003](/schnittstellen/202604/pruefi/QUOTES/PI_15003) | Prüfi | QUOTES | transaktionsdaten |
| [PI_15004](/schnittstellen/202604/pruefi/QUOTES/PI_15004) | Prüfi | QUOTES | transaktionsdaten |
| [PI_27002](/schnittstellen/202604/pruefi/PRICAT/PI_27002) | Prüfi | PRICAT | transaktionsdaten |
| [PI_27003](/schnittstellen/202604/pruefi/PRICAT/PI_27003) | Prüfi | PRICAT | transaktionsdaten |
| [PI_29001](/schnittstellen/202604/pruefi/COMDIS/PI_29001) | Prüfi | COMDIS | transaktionsdaten |
| [PI_29002](/schnittstellen/202604/pruefi/COMDIS/PI_29002) | Prüfi | COMDIS | transaktionsdaten |
| [PI_35001](/schnittstellen/202604/pruefi/REQOTE/PI_35001) | Prüfi | REQOTE | transaktionsdaten |
| [PI_35002](/schnittstellen/202604/pruefi/REQOTE/PI_35002) | Prüfi | REQOTE | transaktionsdaten |
| [PI_35004](/schnittstellen/202604/pruefi/REQOTE/PI_35004) | Prüfi | REQOTE | transaktionsdaten |
| [PI_37000](/schnittstellen/202604/pruefi/PARTIN/PI_37000) | Prüfi | PARTIN | transaktionsdaten |
| [PI_37001](/schnittstellen/202604/pruefi/PARTIN/PI_37001) | Prüfi | PARTIN | transaktionsdaten |
| [PI_37002](/schnittstellen/202604/pruefi/PARTIN/PI_37002) | Prüfi | PARTIN | transaktionsdaten |
| [PI_37008](/schnittstellen/202604/pruefi/PARTIN/PI_37008) | Prüfi | PARTIN | transaktionsdaten |
| [PI_37009](/schnittstellen/202604/pruefi/PARTIN/PI_37009) | Prüfi | PARTIN | transaktionsdaten |
| [PI_37010](/schnittstellen/202604/pruefi/PARTIN/PI_37010) | Prüfi | PARTIN | transaktionsdaten |
| [PI_37012](/schnittstellen/202604/pruefi/PARTIN/PI_37012) | Prüfi | PARTIN | transaktionsdaten |
| [PI_37013](/schnittstellen/202604/pruefi/PARTIN/PI_37013) | Prüfi | PARTIN | transaktionsdaten |
| [PI_37014](/schnittstellen/202604/pruefi/PARTIN/PI_37014) | Prüfi | PARTIN | transaktionsdaten |
| [PI_44001](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44001) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44003](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44003) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44004](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44004) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44005](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44005) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44006](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44006) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44007](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44007) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44008](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44008) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44009](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44009) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44010](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44010) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44011](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44011) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44012](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44012) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44015](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44015) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44016](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44016) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44017](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44017) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44018](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44018) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44019](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44019) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44020](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44020) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44021](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44021) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44022](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44022) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44023](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44023) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44024](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44024) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44035](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44035) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44036](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44036) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44037](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44037) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44038](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44038) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44039](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44039) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44040](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44040) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44041](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44041) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44043](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44043) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44044](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44044) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44052](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44052) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44053](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44053) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44060](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44060) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44101](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44101) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44102](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44102) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44103](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44103) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44104](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44104) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44109](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44109) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44111](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44111) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44112](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44112) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44113](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44113) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44115](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44115) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44116](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44116) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44117](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44117) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44119](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44119) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44120](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44120) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44121](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44121) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44123](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44123) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44124](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44124) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44137](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44137) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44138](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44138) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44139](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44139) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44140](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44140) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44142](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44142) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44143](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44143) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44145](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44145) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44146](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44146) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44147](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44147) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44148](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44148) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44149](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44149) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44150](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44150) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44151](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44151) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44152](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44152) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44156](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44156) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44157](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44157) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44159](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44159) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44160](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44160) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44161](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44161) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44162](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44162) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44163](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44163) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44164](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44164) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44165](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44165) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44166](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44166) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44167](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44167) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44168](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44175](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44175) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44176](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44176) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44180](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44180) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44181](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44181) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44182](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44182) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_55001](/schnittstellen/202604/pruefi/UTILMD/PI_55001) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55002](/schnittstellen/202604/pruefi/UTILMD/PI_55002) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55003](/schnittstellen/202604/pruefi/UTILMD/PI_55003) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55004](/schnittstellen/202604/pruefi/UTILMD/PI_55004) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55005](/schnittstellen/202604/pruefi/UTILMD/PI_55005) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55006](/schnittstellen/202604/pruefi/UTILMD/PI_55006) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55007](/schnittstellen/202604/pruefi/UTILMD/PI_55007) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55008](/schnittstellen/202604/pruefi/UTILMD/PI_55008) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55009](/schnittstellen/202604/pruefi/UTILMD/PI_55009) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55010](/schnittstellen/202604/pruefi/UTILMD/PI_55010) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55011](/schnittstellen/202604/pruefi/UTILMD/PI_55011) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55012](/schnittstellen/202604/pruefi/UTILMD/PI_55012) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55013](/schnittstellen/202604/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55014](/schnittstellen/202604/pruefi/UTILMD/PI_55014) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55015](/schnittstellen/202604/pruefi/UTILMD/PI_55015) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55016](/schnittstellen/202604/pruefi/UTILMD/PI_55016) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55017](/schnittstellen/202604/pruefi/UTILMD/PI_55017) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55018](/schnittstellen/202604/pruefi/UTILMD/PI_55018) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55022](/schnittstellen/202604/pruefi/UTILMD/PI_55022) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55023](/schnittstellen/202604/pruefi/UTILMD/PI_55023) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55024](/schnittstellen/202604/pruefi/UTILMD/PI_55024) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55035](/schnittstellen/202604/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55036](/schnittstellen/202604/pruefi/UTILMD/PI_55036) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55037](/schnittstellen/202604/pruefi/UTILMD/PI_55037) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55038](/schnittstellen/202604/pruefi/UTILMD/PI_55038) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55039](/schnittstellen/202604/pruefi/UTILMD/PI_55039) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55040](/schnittstellen/202604/pruefi/UTILMD/PI_55040) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55041](/schnittstellen/202604/pruefi/UTILMD/PI_55041) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55042](/schnittstellen/202604/pruefi/UTILMD/PI_55042) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55044](/schnittstellen/202604/pruefi/UTILMD/PI_55044) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55051](/schnittstellen/202604/pruefi/UTILMD/PI_55051) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55052](/schnittstellen/202604/pruefi/UTILMD/PI_55052) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55053](/schnittstellen/202604/pruefi/UTILMD/PI_55053) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55060](/schnittstellen/202604/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55074](/schnittstellen/202604/pruefi/UTILMD/PI_55074) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55075](/schnittstellen/202604/pruefi/UTILMD/PI_55075) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55077](/schnittstellen/202604/pruefi/UTILMD/PI_55077) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55078](/schnittstellen/202604/pruefi/UTILMD/PI_55078) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55080](/schnittstellen/202604/pruefi/UTILMD/PI_55080) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55095](/schnittstellen/202604/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55109](/schnittstellen/202604/pruefi/UTILMD/PI_55109) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55110](/schnittstellen/202604/pruefi/UTILMD/PI_55110) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55126](/schnittstellen/202604/pruefi/UTILMD/PI_55126) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55136](/schnittstellen/202604/pruefi/UTILMD/PI_55136) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55137](/schnittstellen/202604/pruefi/UTILMD/PI_55137) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55156](/schnittstellen/202604/pruefi/UTILMD/PI_55156) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55170](/schnittstellen/202604/pruefi/UTILMD/PI_55170) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55173](/schnittstellen/202604/pruefi/UTILMD/PI_55173) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55175](/schnittstellen/202604/pruefi/UTILMD/PI_55175) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55177](/schnittstellen/202604/pruefi/UTILMD/PI_55177) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55180](/schnittstellen/202604/pruefi/UTILMD/PI_55180) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55194](/schnittstellen/202604/pruefi/UTILMD/PI_55194) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55218](/schnittstellen/202604/pruefi/UTILMD/PI_55218) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55220](/schnittstellen/202604/pruefi/UTILMD/PI_55220) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55225](/schnittstellen/202604/pruefi/UTILMD/PI_55225) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55227](/schnittstellen/202604/pruefi/UTILMD/PI_55227) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55230](/schnittstellen/202604/pruefi/UTILMD/PI_55230) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55232](/schnittstellen/202604/pruefi/UTILMD/PI_55232) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55553](/schnittstellen/202604/pruefi/UTILMD/PI_55553) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55555](/schnittstellen/202604/pruefi/UTILMD/PI_55555) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55557](/schnittstellen/202604/pruefi/UTILMD/PI_55557) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55559](/schnittstellen/202604/pruefi/UTILMD/PI_55559) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55600](/schnittstellen/202604/pruefi/UTILMD/PI_55600) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55601](/schnittstellen/202604/pruefi/UTILMD/PI_55601) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55602](/schnittstellen/202604/pruefi/UTILMD/PI_55602) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55603](/schnittstellen/202604/pruefi/UTILMD/PI_55603) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55604](/schnittstellen/202604/pruefi/UTILMD/PI_55604) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55605](/schnittstellen/202604/pruefi/UTILMD/PI_55605) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55607](/schnittstellen/202604/pruefi/UTILMD/PI_55607) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55608](/schnittstellen/202604/pruefi/UTILMD/PI_55608) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55609](/schnittstellen/202604/pruefi/UTILMD/PI_55609) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55611](/schnittstellen/202604/pruefi/UTILMD/PI_55611) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55613](/schnittstellen/202604/pruefi/UTILMD/PI_55613) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55614](/schnittstellen/202604/pruefi/UTILMD/PI_55614) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55615](/schnittstellen/202604/pruefi/UTILMD/PI_55615) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55616](/schnittstellen/202604/pruefi/UTILMD/PI_55616) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55617](/schnittstellen/202604/pruefi/UTILMD/PI_55617) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55618](/schnittstellen/202604/pruefi/UTILMD/PI_55618) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55619](/schnittstellen/202604/pruefi/UTILMD/PI_55619) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55620](/schnittstellen/202604/pruefi/UTILMD/PI_55620) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55621](/schnittstellen/202604/pruefi/UTILMD/PI_55621) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55622](/schnittstellen/202604/pruefi/UTILMD/PI_55622) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55623](/schnittstellen/202604/pruefi/UTILMD/PI_55623) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55624](/schnittstellen/202604/pruefi/UTILMD/PI_55624) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55625](/schnittstellen/202604/pruefi/UTILMD/PI_55625) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55626](/schnittstellen/202604/pruefi/UTILMD/PI_55626) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55627](/schnittstellen/202604/pruefi/UTILMD/PI_55627) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55628](/schnittstellen/202604/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55629](/schnittstellen/202604/pruefi/UTILMD/PI_55629) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55630](/schnittstellen/202604/pruefi/UTILMD/PI_55630) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55632](/schnittstellen/202604/pruefi/UTILMD/PI_55632) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55633](/schnittstellen/202604/pruefi/UTILMD/PI_55633) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55634](/schnittstellen/202604/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55635](/schnittstellen/202604/pruefi/UTILMD/PI_55635) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55636](/schnittstellen/202604/pruefi/UTILMD/PI_55636) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55638](/schnittstellen/202604/pruefi/UTILMD/PI_55638) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55639](/schnittstellen/202604/pruefi/UTILMD/PI_55639) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55640](/schnittstellen/202604/pruefi/UTILMD/PI_55640) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55641](/schnittstellen/202604/pruefi/UTILMD/PI_55641) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55642](/schnittstellen/202604/pruefi/UTILMD/PI_55642) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55643](/schnittstellen/202604/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55644](/schnittstellen/202604/pruefi/UTILMD/PI_55644) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55645](/schnittstellen/202604/pruefi/UTILMD/PI_55645) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55646](/schnittstellen/202604/pruefi/UTILMD/PI_55646) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55647](/schnittstellen/202604/pruefi/UTILMD/PI_55647) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55648](/schnittstellen/202604/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55649](/schnittstellen/202604/pruefi/UTILMD/PI_55649) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55650](/schnittstellen/202604/pruefi/UTILMD/PI_55650) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55651](/schnittstellen/202604/pruefi/UTILMD/PI_55651) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55652](/schnittstellen/202604/pruefi/UTILMD/PI_55652) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55653](/schnittstellen/202604/pruefi/UTILMD/PI_55653) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55654](/schnittstellen/202604/pruefi/UTILMD/PI_55654) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55655](/schnittstellen/202604/pruefi/UTILMD/PI_55655) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55656](/schnittstellen/202604/pruefi/UTILMD/PI_55656) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55657](/schnittstellen/202604/pruefi/UTILMD/PI_55657) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55658](/schnittstellen/202604/pruefi/UTILMD/PI_55658) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55659](/schnittstellen/202604/pruefi/UTILMD/PI_55659) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55660](/schnittstellen/202604/pruefi/UTILMD/PI_55660) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55661](/schnittstellen/202604/pruefi/UTILMD/PI_55661) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55662](/schnittstellen/202604/pruefi/UTILMD/PI_55662) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55663](/schnittstellen/202604/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55664](/schnittstellen/202604/pruefi/UTILMD/PI_55664) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55665](/schnittstellen/202604/pruefi/UTILMD/PI_55665) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55666](/schnittstellen/202604/pruefi/UTILMD/PI_55666) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55667](/schnittstellen/202604/pruefi/UTILMD/PI_55667) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55669](/schnittstellen/202604/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55670](/schnittstellen/202604/pruefi/UTILMD/PI_55670) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55672](/schnittstellen/202604/pruefi/UTILMD/PI_55672) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55673](/schnittstellen/202604/pruefi/UTILMD/PI_55673) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55674](/schnittstellen/202604/pruefi/UTILMD/PI_55674) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55684](/schnittstellen/202604/pruefi/UTILMD/PI_55684) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55686](/schnittstellen/202604/pruefi/UTILMD/PI_55686) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55688](/schnittstellen/202604/pruefi/UTILMD/PI_55688) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55690](/schnittstellen/202604/pruefi/UTILMD/PI_55690) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55691](/schnittstellen/202604/pruefi/UTILMD/PI_55691) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55692](/schnittstellen/202604/pruefi/UTILMD/PI_55692) | Prüfi | UTILMD | transaktionsdaten |
| [PI_66666](/schnittstellen/202604/pruefi/APERAK/PI_66666) | Prüfi | APERAK | transaktionsdaten |
| [PI_99999](/schnittstellen/202604/pruefi/APERAK/PI_99999) | Prüfi | APERAK | transaktionsdaten |

### nachrichtenfunktion

13 Verwendung(en) in den Nachrichtentypen MSCONS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_13002](/schnittstellen/202604/pruefi/MSCONS/PI_13002) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13006](/schnittstellen/202604/pruefi/MSCONS/PI_13006) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13007](/schnittstellen/202604/pruefi/MSCONS/PI_13007) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13008](/schnittstellen/202604/pruefi/MSCONS/PI_13008) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13009](/schnittstellen/202604/pruefi/MSCONS/PI_13009) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13015](/schnittstellen/202604/pruefi/MSCONS/PI_13015) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13016](/schnittstellen/202604/pruefi/MSCONS/PI_13016) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13017](/schnittstellen/202604/pruefi/MSCONS/PI_13017) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13018](/schnittstellen/202604/pruefi/MSCONS/PI_13018) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13019](/schnittstellen/202604/pruefi/MSCONS/PI_13019) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13025](/schnittstellen/202604/pruefi/MSCONS/PI_13025) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13027](/schnittstellen/202604/pruefi/MSCONS/PI_13027) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13028](/schnittstellen/202604/pruefi/MSCONS/PI_13028) | Prüfi | MSCONS | transaktionsdaten |

### nachrichtendatum

366 Verwendung(en) in den Nachrichtentypen APERAK, COMDIS, IFTSTA, INSRPT, MSCONS, ORDCHG, ORDERS, ORDRSP, PARTIN, PRICAT, QUOTES, REMADV, REQOTE, UTILMD, UTILMD_GAS, UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [[LF] START_VERSAND_ANTWORT_NNA](/schnittstellen/202604/trigger/events/LF-START_VERSAND_ANTWORT_NNA) | Event | — | transaktionsdaten |
| [PI_13002](/schnittstellen/202604/pruefi/MSCONS/PI_13002) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13006](/schnittstellen/202604/pruefi/MSCONS/PI_13006) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13007](/schnittstellen/202604/pruefi/MSCONS/PI_13007) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13008](/schnittstellen/202604/pruefi/MSCONS/PI_13008) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13009](/schnittstellen/202604/pruefi/MSCONS/PI_13009) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13015](/schnittstellen/202604/pruefi/MSCONS/PI_13015) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13016](/schnittstellen/202604/pruefi/MSCONS/PI_13016) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13017](/schnittstellen/202604/pruefi/MSCONS/PI_13017) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13018](/schnittstellen/202604/pruefi/MSCONS/PI_13018) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13019](/schnittstellen/202604/pruefi/MSCONS/PI_13019) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13025](/schnittstellen/202604/pruefi/MSCONS/PI_13025) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13027](/schnittstellen/202604/pruefi/MSCONS/PI_13027) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13028](/schnittstellen/202604/pruefi/MSCONS/PI_13028) | Prüfi | MSCONS | transaktionsdaten |
| [PI_15001](/schnittstellen/202604/pruefi/QUOTES/PI_15001) | Prüfi | QUOTES | transaktionsdaten |
| [PI_15003](/schnittstellen/202604/pruefi/QUOTES/PI_15003) | Prüfi | QUOTES | transaktionsdaten |
| [PI_15004](/schnittstellen/202604/pruefi/QUOTES/PI_15004) | Prüfi | QUOTES | transaktionsdaten |
| [PI_17001](/schnittstellen/202604/pruefi/ORDERS/PI_17001) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17002](/schnittstellen/202604/pruefi/ORDERS/PI_17002) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17003](/schnittstellen/202604/pruefi/ORDERS/PI_17003) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17004](/schnittstellen/202604/pruefi/ORDERS/PI_17004) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17005](/schnittstellen/202604/pruefi/ORDERS/PI_17005) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17006](/schnittstellen/202604/pruefi/ORDERS/PI_17006) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17009](/schnittstellen/202604/pruefi/ORDERS/PI_17009) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17101](/schnittstellen/202604/pruefi/ORDERS/PI_17101) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17102](/schnittstellen/202604/pruefi/ORDERS/PI_17102) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17103](/schnittstellen/202604/pruefi/ORDERS/PI_17103) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17104](/schnittstellen/202604/pruefi/ORDERS/PI_17104) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17113](/schnittstellen/202604/pruefi/ORDERS/PI_17113) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17115](/schnittstellen/202604/pruefi/ORDERS/PI_17115) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17116](/schnittstellen/202604/pruefi/ORDERS/PI_17116) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17117](/schnittstellen/202604/pruefi/ORDERS/PI_17117) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17118](/schnittstellen/202604/pruefi/ORDERS/PI_17118) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17120](/schnittstellen/202604/pruefi/ORDERS/PI_17120) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17121](/schnittstellen/202604/pruefi/ORDERS/PI_17121) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17122](/schnittstellen/202604/pruefi/ORDERS/PI_17122) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17123](/schnittstellen/202604/pruefi/ORDERS/PI_17123) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17126](/schnittstellen/202604/pruefi/ORDERS/PI_17126) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17128](/schnittstellen/202604/pruefi/ORDERS/PI_17128) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17129](/schnittstellen/202604/pruefi/ORDERS/PI_17129) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17130](/schnittstellen/202604/pruefi/ORDERS/PI_17130) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17131](/schnittstellen/202604/pruefi/ORDERS/PI_17131) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17132](/schnittstellen/202604/pruefi/ORDERS/PI_17132) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17133](/schnittstellen/202604/pruefi/ORDERS/PI_17133) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17134](/schnittstellen/202604/pruefi/ORDERS/PI_17134) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17135](/schnittstellen/202604/pruefi/ORDERS/PI_17135) | Prüfi | ORDERS | transaktionsdaten |
| [PI_19001](/schnittstellen/202604/pruefi/ORDRSP/PI_19001) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19002](/schnittstellen/202604/pruefi/ORDRSP/PI_19002) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19003](/schnittstellen/202604/pruefi/ORDRSP/PI_19003) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19004](/schnittstellen/202604/pruefi/ORDRSP/PI_19004) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19005](/schnittstellen/202604/pruefi/ORDRSP/PI_19005) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19006](/schnittstellen/202604/pruefi/ORDRSP/PI_19006) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19007](/schnittstellen/202604/pruefi/ORDRSP/PI_19007) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19009](/schnittstellen/202604/pruefi/ORDRSP/PI_19009) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19010](/schnittstellen/202604/pruefi/ORDRSP/PI_19010) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19011](/schnittstellen/202604/pruefi/ORDRSP/PI_19011) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19012](/schnittstellen/202604/pruefi/ORDRSP/PI_19012) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19013](/schnittstellen/202604/pruefi/ORDRSP/PI_19013) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19014](/schnittstellen/202604/pruefi/ORDRSP/PI_19014) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19015](/schnittstellen/202604/pruefi/ORDRSP/PI_19015) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19016](/schnittstellen/202604/pruefi/ORDRSP/PI_19016) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19101](/schnittstellen/202604/pruefi/ORDRSP/PI_19101) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19102](/schnittstellen/202604/pruefi/ORDRSP/PI_19102) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19103](/schnittstellen/202604/pruefi/ORDRSP/PI_19103) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19104](/schnittstellen/202604/pruefi/ORDRSP/PI_19104) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19114](/schnittstellen/202604/pruefi/ORDRSP/PI_19114) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19116](/schnittstellen/202604/pruefi/ORDRSP/PI_19116) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19117](/schnittstellen/202604/pruefi/ORDRSP/PI_19117) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19118](/schnittstellen/202604/pruefi/ORDRSP/PI_19118) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19119](/schnittstellen/202604/pruefi/ORDRSP/PI_19119) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19121](/schnittstellen/202604/pruefi/ORDRSP/PI_19121) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19123](/schnittstellen/202604/pruefi/ORDRSP/PI_19123) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19124](/schnittstellen/202604/pruefi/ORDRSP/PI_19124) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19128](/schnittstellen/202604/pruefi/ORDRSP/PI_19128) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19129](/schnittstellen/202604/pruefi/ORDRSP/PI_19129) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19133](/schnittstellen/202604/pruefi/ORDRSP/PI_19133) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19301](/schnittstellen/202604/pruefi/ORDRSP/PI_19301) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19302](/schnittstellen/202604/pruefi/ORDRSP/PI_19302) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_21007](/schnittstellen/202604/pruefi/IFTSTA/PI_21007) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21009](/schnittstellen/202604/pruefi/IFTSTA/PI_21009) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21010](/schnittstellen/202604/pruefi/IFTSTA/PI_21010) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21011](/schnittstellen/202604/pruefi/IFTSTA/PI_21011) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21012](/schnittstellen/202604/pruefi/IFTSTA/PI_21012) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21013](/schnittstellen/202604/pruefi/IFTSTA/PI_21013) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21015](/schnittstellen/202604/pruefi/IFTSTA/PI_21015) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21018](/schnittstellen/202604/pruefi/IFTSTA/PI_21018) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21024](/schnittstellen/202604/pruefi/IFTSTA/PI_21024) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21025](/schnittstellen/202604/pruefi/IFTSTA/PI_21025) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21026](/schnittstellen/202604/pruefi/IFTSTA/PI_21026) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21027](/schnittstellen/202604/pruefi/IFTSTA/PI_21027) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21028](/schnittstellen/202604/pruefi/IFTSTA/PI_21028) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21029](/schnittstellen/202604/pruefi/IFTSTA/PI_21029) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21030](/schnittstellen/202604/pruefi/IFTSTA/PI_21030) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21031](/schnittstellen/202604/pruefi/IFTSTA/PI_21031) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21032](/schnittstellen/202604/pruefi/IFTSTA/PI_21032) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21033](/schnittstellen/202604/pruefi/IFTSTA/PI_21033) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21035](/schnittstellen/202604/pruefi/IFTSTA/PI_21035) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21036](/schnittstellen/202604/pruefi/IFTSTA/PI_21036) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21039](/schnittstellen/202604/pruefi/IFTSTA/PI_21039) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21040](/schnittstellen/202604/pruefi/IFTSTA/PI_21040) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21043](/schnittstellen/202604/pruefi/IFTSTA/PI_21043) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21044](/schnittstellen/202604/pruefi/IFTSTA/PI_21044) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21045](/schnittstellen/202604/pruefi/IFTSTA/PI_21045) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21047](/schnittstellen/202604/pruefi/IFTSTA/PI_21047) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_23001](/schnittstellen/202604/pruefi/INSRPT/PI_23001) | Prüfi | INSRPT | transaktionsdaten |
| [PI_23003](/schnittstellen/202604/pruefi/INSRPT/PI_23003) | Prüfi | INSRPT | transaktionsdaten |
| [PI_23004](/schnittstellen/202604/pruefi/INSRPT/PI_23004) | Prüfi | INSRPT | transaktionsdaten |
| [PI_23005](/schnittstellen/202604/pruefi/INSRPT/PI_23005) | Prüfi | INSRPT | transaktionsdaten |
| [PI_23008](/schnittstellen/202604/pruefi/INSRPT/PI_23008) | Prüfi | INSRPT | transaktionsdaten |
| [PI_23009](/schnittstellen/202604/pruefi/INSRPT/PI_23009) | Prüfi | INSRPT | transaktionsdaten |
| [PI_23011](/schnittstellen/202604/pruefi/INSRPT/PI_23011) | Prüfi | INSRPT | transaktionsdaten |
| [PI_23012](/schnittstellen/202604/pruefi/INSRPT/PI_23012) | Prüfi | INSRPT | transaktionsdaten |
| [PI_25001](/schnittstellen/202604/pruefi/UTILTS/PI_25001) | Prüfi | UTILTS | transaktionsdaten |
| [PI_25004](/schnittstellen/202604/pruefi/UTILTS/PI_25004) | Prüfi | UTILTS | transaktionsdaten |
| [PI_25005](/schnittstellen/202604/pruefi/UTILTS/PI_25005) | Prüfi | UTILTS | transaktionsdaten |
| [PI_25006](/schnittstellen/202604/pruefi/UTILTS/PI_25006) | Prüfi | UTILTS | transaktionsdaten |
| [PI_25007](/schnittstellen/202604/pruefi/UTILTS/PI_25007) | Prüfi | UTILTS | transaktionsdaten |
| [PI_25008](/schnittstellen/202604/pruefi/UTILTS/PI_25008) | Prüfi | UTILTS | transaktionsdaten |
| [PI_25009](/schnittstellen/202604/pruefi/UTILTS/PI_25009) | Prüfi | UTILTS | transaktionsdaten |
| [PI_25010](/schnittstellen/202604/pruefi/UTILTS/PI_25010) | Prüfi | UTILTS | transaktionsdaten |
| [PI_27002](/schnittstellen/202604/pruefi/PRICAT/PI_27002) | Prüfi | PRICAT | transaktionsdaten |
| [PI_27003](/schnittstellen/202604/pruefi/PRICAT/PI_27003) | Prüfi | PRICAT | transaktionsdaten |
| [PI_29001](/schnittstellen/202604/pruefi/COMDIS/PI_29001) | Prüfi | COMDIS | transaktionsdaten |
| [PI_29002](/schnittstellen/202604/pruefi/COMDIS/PI_29002) | Prüfi | COMDIS | transaktionsdaten |
| [PI_33001](/schnittstellen/202604/pruefi/REMADV/PI_33001) | Prüfi | REMADV | transaktionsdaten |
| [PI_33002](/schnittstellen/202604/pruefi/REMADV/PI_33002) | Prüfi | REMADV | transaktionsdaten |
| [PI_33003](/schnittstellen/202604/pruefi/REMADV/PI_33003) | Prüfi | REMADV | transaktionsdaten |
| [PI_33004](/schnittstellen/202604/pruefi/REMADV/PI_33004) | Prüfi | REMADV | transaktionsdaten |
| [PI_35001](/schnittstellen/202604/pruefi/REQOTE/PI_35001) | Prüfi | REQOTE | transaktionsdaten |
| [PI_35002](/schnittstellen/202604/pruefi/REQOTE/PI_35002) | Prüfi | REQOTE | transaktionsdaten |
| [PI_35004](/schnittstellen/202604/pruefi/REQOTE/PI_35004) | Prüfi | REQOTE | transaktionsdaten |
| [PI_37000](/schnittstellen/202604/pruefi/PARTIN/PI_37000) | Prüfi | PARTIN | transaktionsdaten |
| [PI_37001](/schnittstellen/202604/pruefi/PARTIN/PI_37001) | Prüfi | PARTIN | transaktionsdaten |
| [PI_37002](/schnittstellen/202604/pruefi/PARTIN/PI_37002) | Prüfi | PARTIN | transaktionsdaten |
| [PI_37008](/schnittstellen/202604/pruefi/PARTIN/PI_37008) | Prüfi | PARTIN | transaktionsdaten |
| [PI_37009](/schnittstellen/202604/pruefi/PARTIN/PI_37009) | Prüfi | PARTIN | transaktionsdaten |
| [PI_37010](/schnittstellen/202604/pruefi/PARTIN/PI_37010) | Prüfi | PARTIN | transaktionsdaten |
| [PI_37012](/schnittstellen/202604/pruefi/PARTIN/PI_37012) | Prüfi | PARTIN | transaktionsdaten |
| [PI_37013](/schnittstellen/202604/pruefi/PARTIN/PI_37013) | Prüfi | PARTIN | transaktionsdaten |
| [PI_37014](/schnittstellen/202604/pruefi/PARTIN/PI_37014) | Prüfi | PARTIN | transaktionsdaten |
| [PI_39000](/schnittstellen/202604/pruefi/ORDCHG/PI_39000) | Prüfi | ORDCHG | transaktionsdaten |
| [PI_39001](/schnittstellen/202604/pruefi/ORDCHG/PI_39001) | Prüfi | ORDCHG | transaktionsdaten |
| [PI_44001](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44001) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44003](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44003) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44004](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44004) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44005](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44005) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44006](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44006) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44007](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44007) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44008](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44008) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44009](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44009) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44010](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44010) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44011](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44011) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44012](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44012) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44015](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44015) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44016](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44016) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44017](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44017) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44018](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44018) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44019](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44019) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44020](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44020) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44021](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44021) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44022](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44022) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44023](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44023) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44024](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44024) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44035](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44035) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44036](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44036) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44037](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44037) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44038](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44038) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44039](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44039) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44040](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44040) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44041](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44041) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44043](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44043) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44044](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44044) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44052](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44052) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44053](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44053) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44060](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44060) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44101](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44101) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44102](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44102) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44103](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44103) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44104](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44104) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44109](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44109) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44111](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44111) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44112](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44112) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44113](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44113) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44115](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44115) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44116](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44116) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44117](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44117) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44119](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44119) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44120](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44120) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44121](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44121) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44123](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44123) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44124](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44124) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44137](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44137) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44138](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44138) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44139](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44139) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44140](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44140) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44142](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44142) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44143](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44143) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44145](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44145) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44146](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44146) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44147](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44147) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44148](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44148) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44149](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44149) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44150](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44150) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44151](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44151) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44152](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44152) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44156](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44156) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44157](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44157) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44159](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44159) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44160](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44160) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44161](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44161) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44162](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44162) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44163](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44163) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44164](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44164) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44165](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44165) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44166](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44166) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44167](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44167) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44168](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44175](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44175) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44176](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44176) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44180](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44180) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44181](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44181) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44182](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44182) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_55001](/schnittstellen/202604/pruefi/UTILMD/PI_55001) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55002](/schnittstellen/202604/pruefi/UTILMD/PI_55002) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55003](/schnittstellen/202604/pruefi/UTILMD/PI_55003) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55004](/schnittstellen/202604/pruefi/UTILMD/PI_55004) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55005](/schnittstellen/202604/pruefi/UTILMD/PI_55005) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55006](/schnittstellen/202604/pruefi/UTILMD/PI_55006) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55007](/schnittstellen/202604/pruefi/UTILMD/PI_55007) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55008](/schnittstellen/202604/pruefi/UTILMD/PI_55008) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55009](/schnittstellen/202604/pruefi/UTILMD/PI_55009) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55010](/schnittstellen/202604/pruefi/UTILMD/PI_55010) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55011](/schnittstellen/202604/pruefi/UTILMD/PI_55011) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55012](/schnittstellen/202604/pruefi/UTILMD/PI_55012) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55013](/schnittstellen/202604/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55014](/schnittstellen/202604/pruefi/UTILMD/PI_55014) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55015](/schnittstellen/202604/pruefi/UTILMD/PI_55015) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55016](/schnittstellen/202604/pruefi/UTILMD/PI_55016) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55017](/schnittstellen/202604/pruefi/UTILMD/PI_55017) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55018](/schnittstellen/202604/pruefi/UTILMD/PI_55018) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55022](/schnittstellen/202604/pruefi/UTILMD/PI_55022) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55023](/schnittstellen/202604/pruefi/UTILMD/PI_55023) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55024](/schnittstellen/202604/pruefi/UTILMD/PI_55024) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55035](/schnittstellen/202604/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55036](/schnittstellen/202604/pruefi/UTILMD/PI_55036) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55037](/schnittstellen/202604/pruefi/UTILMD/PI_55037) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55038](/schnittstellen/202604/pruefi/UTILMD/PI_55038) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55039](/schnittstellen/202604/pruefi/UTILMD/PI_55039) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55040](/schnittstellen/202604/pruefi/UTILMD/PI_55040) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55041](/schnittstellen/202604/pruefi/UTILMD/PI_55041) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55042](/schnittstellen/202604/pruefi/UTILMD/PI_55042) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55044](/schnittstellen/202604/pruefi/UTILMD/PI_55044) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55051](/schnittstellen/202604/pruefi/UTILMD/PI_55051) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55052](/schnittstellen/202604/pruefi/UTILMD/PI_55052) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55053](/schnittstellen/202604/pruefi/UTILMD/PI_55053) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55060](/schnittstellen/202604/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55074](/schnittstellen/202604/pruefi/UTILMD/PI_55074) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55075](/schnittstellen/202604/pruefi/UTILMD/PI_55075) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55077](/schnittstellen/202604/pruefi/UTILMD/PI_55077) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55078](/schnittstellen/202604/pruefi/UTILMD/PI_55078) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55080](/schnittstellen/202604/pruefi/UTILMD/PI_55080) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55095](/schnittstellen/202604/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55109](/schnittstellen/202604/pruefi/UTILMD/PI_55109) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55110](/schnittstellen/202604/pruefi/UTILMD/PI_55110) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55126](/schnittstellen/202604/pruefi/UTILMD/PI_55126) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55136](/schnittstellen/202604/pruefi/UTILMD/PI_55136) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55137](/schnittstellen/202604/pruefi/UTILMD/PI_55137) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55156](/schnittstellen/202604/pruefi/UTILMD/PI_55156) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55170](/schnittstellen/202604/pruefi/UTILMD/PI_55170) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55173](/schnittstellen/202604/pruefi/UTILMD/PI_55173) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55175](/schnittstellen/202604/pruefi/UTILMD/PI_55175) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55177](/schnittstellen/202604/pruefi/UTILMD/PI_55177) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55180](/schnittstellen/202604/pruefi/UTILMD/PI_55180) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55194](/schnittstellen/202604/pruefi/UTILMD/PI_55194) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55218](/schnittstellen/202604/pruefi/UTILMD/PI_55218) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55220](/schnittstellen/202604/pruefi/UTILMD/PI_55220) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55225](/schnittstellen/202604/pruefi/UTILMD/PI_55225) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55227](/schnittstellen/202604/pruefi/UTILMD/PI_55227) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55230](/schnittstellen/202604/pruefi/UTILMD/PI_55230) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55232](/schnittstellen/202604/pruefi/UTILMD/PI_55232) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55553](/schnittstellen/202604/pruefi/UTILMD/PI_55553) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55555](/schnittstellen/202604/pruefi/UTILMD/PI_55555) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55557](/schnittstellen/202604/pruefi/UTILMD/PI_55557) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55559](/schnittstellen/202604/pruefi/UTILMD/PI_55559) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55600](/schnittstellen/202604/pruefi/UTILMD/PI_55600) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55601](/schnittstellen/202604/pruefi/UTILMD/PI_55601) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55602](/schnittstellen/202604/pruefi/UTILMD/PI_55602) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55603](/schnittstellen/202604/pruefi/UTILMD/PI_55603) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55604](/schnittstellen/202604/pruefi/UTILMD/PI_55604) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55605](/schnittstellen/202604/pruefi/UTILMD/PI_55605) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55607](/schnittstellen/202604/pruefi/UTILMD/PI_55607) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55608](/schnittstellen/202604/pruefi/UTILMD/PI_55608) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55609](/schnittstellen/202604/pruefi/UTILMD/PI_55609) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55611](/schnittstellen/202604/pruefi/UTILMD/PI_55611) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55613](/schnittstellen/202604/pruefi/UTILMD/PI_55613) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55614](/schnittstellen/202604/pruefi/UTILMD/PI_55614) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55615](/schnittstellen/202604/pruefi/UTILMD/PI_55615) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55616](/schnittstellen/202604/pruefi/UTILMD/PI_55616) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55617](/schnittstellen/202604/pruefi/UTILMD/PI_55617) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55618](/schnittstellen/202604/pruefi/UTILMD/PI_55618) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55619](/schnittstellen/202604/pruefi/UTILMD/PI_55619) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55620](/schnittstellen/202604/pruefi/UTILMD/PI_55620) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55621](/schnittstellen/202604/pruefi/UTILMD/PI_55621) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55622](/schnittstellen/202604/pruefi/UTILMD/PI_55622) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55623](/schnittstellen/202604/pruefi/UTILMD/PI_55623) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55624](/schnittstellen/202604/pruefi/UTILMD/PI_55624) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55625](/schnittstellen/202604/pruefi/UTILMD/PI_55625) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55626](/schnittstellen/202604/pruefi/UTILMD/PI_55626) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55627](/schnittstellen/202604/pruefi/UTILMD/PI_55627) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55628](/schnittstellen/202604/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55629](/schnittstellen/202604/pruefi/UTILMD/PI_55629) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55630](/schnittstellen/202604/pruefi/UTILMD/PI_55630) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55632](/schnittstellen/202604/pruefi/UTILMD/PI_55632) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55633](/schnittstellen/202604/pruefi/UTILMD/PI_55633) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55634](/schnittstellen/202604/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55635](/schnittstellen/202604/pruefi/UTILMD/PI_55635) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55636](/schnittstellen/202604/pruefi/UTILMD/PI_55636) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55638](/schnittstellen/202604/pruefi/UTILMD/PI_55638) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55639](/schnittstellen/202604/pruefi/UTILMD/PI_55639) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55640](/schnittstellen/202604/pruefi/UTILMD/PI_55640) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55641](/schnittstellen/202604/pruefi/UTILMD/PI_55641) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55642](/schnittstellen/202604/pruefi/UTILMD/PI_55642) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55643](/schnittstellen/202604/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55644](/schnittstellen/202604/pruefi/UTILMD/PI_55644) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55645](/schnittstellen/202604/pruefi/UTILMD/PI_55645) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55646](/schnittstellen/202604/pruefi/UTILMD/PI_55646) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55647](/schnittstellen/202604/pruefi/UTILMD/PI_55647) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55648](/schnittstellen/202604/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55649](/schnittstellen/202604/pruefi/UTILMD/PI_55649) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55650](/schnittstellen/202604/pruefi/UTILMD/PI_55650) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55651](/schnittstellen/202604/pruefi/UTILMD/PI_55651) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55652](/schnittstellen/202604/pruefi/UTILMD/PI_55652) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55653](/schnittstellen/202604/pruefi/UTILMD/PI_55653) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55654](/schnittstellen/202604/pruefi/UTILMD/PI_55654) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55655](/schnittstellen/202604/pruefi/UTILMD/PI_55655) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55656](/schnittstellen/202604/pruefi/UTILMD/PI_55656) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55657](/schnittstellen/202604/pruefi/UTILMD/PI_55657) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55658](/schnittstellen/202604/pruefi/UTILMD/PI_55658) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55659](/schnittstellen/202604/pruefi/UTILMD/PI_55659) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55660](/schnittstellen/202604/pruefi/UTILMD/PI_55660) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55661](/schnittstellen/202604/pruefi/UTILMD/PI_55661) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55662](/schnittstellen/202604/pruefi/UTILMD/PI_55662) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55663](/schnittstellen/202604/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55664](/schnittstellen/202604/pruefi/UTILMD/PI_55664) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55665](/schnittstellen/202604/pruefi/UTILMD/PI_55665) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55666](/schnittstellen/202604/pruefi/UTILMD/PI_55666) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55667](/schnittstellen/202604/pruefi/UTILMD/PI_55667) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55669](/schnittstellen/202604/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55670](/schnittstellen/202604/pruefi/UTILMD/PI_55670) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55672](/schnittstellen/202604/pruefi/UTILMD/PI_55672) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55673](/schnittstellen/202604/pruefi/UTILMD/PI_55673) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55674](/schnittstellen/202604/pruefi/UTILMD/PI_55674) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55684](/schnittstellen/202604/pruefi/UTILMD/PI_55684) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55686](/schnittstellen/202604/pruefi/UTILMD/PI_55686) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55688](/schnittstellen/202604/pruefi/UTILMD/PI_55688) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55690](/schnittstellen/202604/pruefi/UTILMD/PI_55690) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55691](/schnittstellen/202604/pruefi/UTILMD/PI_55691) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55692](/schnittstellen/202604/pruefi/UTILMD/PI_55692) | Prüfi | UTILMD | transaktionsdaten |
| [PI_66666](/schnittstellen/202604/pruefi/APERAK/PI_66666) | Prüfi | APERAK | transaktionsdaten |
| [PI_99999](/schnittstellen/202604/pruefi/APERAK/PI_99999) | Prüfi | APERAK | transaktionsdaten |

### nachrichtenreferenznummer

366 Verwendung(en) in den Nachrichtentypen APERAK, COMDIS, IFTSTA, INSRPT, INVOIC, MSCONS, ORDCHG, ORDERS, ORDRSP, PARTIN, PRICAT, QUOTES, REMADV, REQOTE, UTILMD, UTILMD_GAS, UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_13002](/schnittstellen/202604/pruefi/MSCONS/PI_13002) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13006](/schnittstellen/202604/pruefi/MSCONS/PI_13006) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13007](/schnittstellen/202604/pruefi/MSCONS/PI_13007) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13008](/schnittstellen/202604/pruefi/MSCONS/PI_13008) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13009](/schnittstellen/202604/pruefi/MSCONS/PI_13009) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13015](/schnittstellen/202604/pruefi/MSCONS/PI_13015) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13016](/schnittstellen/202604/pruefi/MSCONS/PI_13016) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13017](/schnittstellen/202604/pruefi/MSCONS/PI_13017) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13018](/schnittstellen/202604/pruefi/MSCONS/PI_13018) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13019](/schnittstellen/202604/pruefi/MSCONS/PI_13019) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13025](/schnittstellen/202604/pruefi/MSCONS/PI_13025) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13027](/schnittstellen/202604/pruefi/MSCONS/PI_13027) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13028](/schnittstellen/202604/pruefi/MSCONS/PI_13028) | Prüfi | MSCONS | transaktionsdaten |
| [PI_15001](/schnittstellen/202604/pruefi/QUOTES/PI_15001) | Prüfi | QUOTES | transaktionsdaten |
| [PI_15003](/schnittstellen/202604/pruefi/QUOTES/PI_15003) | Prüfi | QUOTES | transaktionsdaten |
| [PI_15004](/schnittstellen/202604/pruefi/QUOTES/PI_15004) | Prüfi | QUOTES | transaktionsdaten |
| [PI_17001](/schnittstellen/202604/pruefi/ORDERS/PI_17001) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17002](/schnittstellen/202604/pruefi/ORDERS/PI_17002) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17003](/schnittstellen/202604/pruefi/ORDERS/PI_17003) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17004](/schnittstellen/202604/pruefi/ORDERS/PI_17004) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17005](/schnittstellen/202604/pruefi/ORDERS/PI_17005) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17006](/schnittstellen/202604/pruefi/ORDERS/PI_17006) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17009](/schnittstellen/202604/pruefi/ORDERS/PI_17009) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17101](/schnittstellen/202604/pruefi/ORDERS/PI_17101) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17102](/schnittstellen/202604/pruefi/ORDERS/PI_17102) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17103](/schnittstellen/202604/pruefi/ORDERS/PI_17103) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17104](/schnittstellen/202604/pruefi/ORDERS/PI_17104) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17113](/schnittstellen/202604/pruefi/ORDERS/PI_17113) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17115](/schnittstellen/202604/pruefi/ORDERS/PI_17115) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17116](/schnittstellen/202604/pruefi/ORDERS/PI_17116) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17117](/schnittstellen/202604/pruefi/ORDERS/PI_17117) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17118](/schnittstellen/202604/pruefi/ORDERS/PI_17118) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17120](/schnittstellen/202604/pruefi/ORDERS/PI_17120) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17121](/schnittstellen/202604/pruefi/ORDERS/PI_17121) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17122](/schnittstellen/202604/pruefi/ORDERS/PI_17122) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17123](/schnittstellen/202604/pruefi/ORDERS/PI_17123) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17126](/schnittstellen/202604/pruefi/ORDERS/PI_17126) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17128](/schnittstellen/202604/pruefi/ORDERS/PI_17128) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17129](/schnittstellen/202604/pruefi/ORDERS/PI_17129) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17130](/schnittstellen/202604/pruefi/ORDERS/PI_17130) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17131](/schnittstellen/202604/pruefi/ORDERS/PI_17131) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17132](/schnittstellen/202604/pruefi/ORDERS/PI_17132) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17133](/schnittstellen/202604/pruefi/ORDERS/PI_17133) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17134](/schnittstellen/202604/pruefi/ORDERS/PI_17134) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17135](/schnittstellen/202604/pruefi/ORDERS/PI_17135) | Prüfi | ORDERS | transaktionsdaten |
| [PI_19001](/schnittstellen/202604/pruefi/ORDRSP/PI_19001) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19002](/schnittstellen/202604/pruefi/ORDRSP/PI_19002) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19003](/schnittstellen/202604/pruefi/ORDRSP/PI_19003) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19004](/schnittstellen/202604/pruefi/ORDRSP/PI_19004) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19005](/schnittstellen/202604/pruefi/ORDRSP/PI_19005) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19006](/schnittstellen/202604/pruefi/ORDRSP/PI_19006) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19007](/schnittstellen/202604/pruefi/ORDRSP/PI_19007) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19009](/schnittstellen/202604/pruefi/ORDRSP/PI_19009) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19010](/schnittstellen/202604/pruefi/ORDRSP/PI_19010) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19011](/schnittstellen/202604/pruefi/ORDRSP/PI_19011) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19012](/schnittstellen/202604/pruefi/ORDRSP/PI_19012) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19013](/schnittstellen/202604/pruefi/ORDRSP/PI_19013) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19014](/schnittstellen/202604/pruefi/ORDRSP/PI_19014) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19015](/schnittstellen/202604/pruefi/ORDRSP/PI_19015) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19016](/schnittstellen/202604/pruefi/ORDRSP/PI_19016) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19101](/schnittstellen/202604/pruefi/ORDRSP/PI_19101) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19102](/schnittstellen/202604/pruefi/ORDRSP/PI_19102) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19103](/schnittstellen/202604/pruefi/ORDRSP/PI_19103) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19104](/schnittstellen/202604/pruefi/ORDRSP/PI_19104) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19114](/schnittstellen/202604/pruefi/ORDRSP/PI_19114) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19116](/schnittstellen/202604/pruefi/ORDRSP/PI_19116) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19117](/schnittstellen/202604/pruefi/ORDRSP/PI_19117) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19118](/schnittstellen/202604/pruefi/ORDRSP/PI_19118) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19119](/schnittstellen/202604/pruefi/ORDRSP/PI_19119) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19121](/schnittstellen/202604/pruefi/ORDRSP/PI_19121) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19123](/schnittstellen/202604/pruefi/ORDRSP/PI_19123) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19124](/schnittstellen/202604/pruefi/ORDRSP/PI_19124) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19128](/schnittstellen/202604/pruefi/ORDRSP/PI_19128) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19129](/schnittstellen/202604/pruefi/ORDRSP/PI_19129) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19133](/schnittstellen/202604/pruefi/ORDRSP/PI_19133) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19301](/schnittstellen/202604/pruefi/ORDRSP/PI_19301) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19302](/schnittstellen/202604/pruefi/ORDRSP/PI_19302) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_21007](/schnittstellen/202604/pruefi/IFTSTA/PI_21007) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21009](/schnittstellen/202604/pruefi/IFTSTA/PI_21009) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21010](/schnittstellen/202604/pruefi/IFTSTA/PI_21010) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21011](/schnittstellen/202604/pruefi/IFTSTA/PI_21011) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21012](/schnittstellen/202604/pruefi/IFTSTA/PI_21012) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21013](/schnittstellen/202604/pruefi/IFTSTA/PI_21013) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21015](/schnittstellen/202604/pruefi/IFTSTA/PI_21015) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21018](/schnittstellen/202604/pruefi/IFTSTA/PI_21018) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21024](/schnittstellen/202604/pruefi/IFTSTA/PI_21024) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21025](/schnittstellen/202604/pruefi/IFTSTA/PI_21025) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21026](/schnittstellen/202604/pruefi/IFTSTA/PI_21026) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21027](/schnittstellen/202604/pruefi/IFTSTA/PI_21027) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21028](/schnittstellen/202604/pruefi/IFTSTA/PI_21028) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21029](/schnittstellen/202604/pruefi/IFTSTA/PI_21029) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21030](/schnittstellen/202604/pruefi/IFTSTA/PI_21030) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21031](/schnittstellen/202604/pruefi/IFTSTA/PI_21031) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21032](/schnittstellen/202604/pruefi/IFTSTA/PI_21032) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21033](/schnittstellen/202604/pruefi/IFTSTA/PI_21033) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21035](/schnittstellen/202604/pruefi/IFTSTA/PI_21035) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21036](/schnittstellen/202604/pruefi/IFTSTA/PI_21036) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21039](/schnittstellen/202604/pruefi/IFTSTA/PI_21039) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21040](/schnittstellen/202604/pruefi/IFTSTA/PI_21040) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21043](/schnittstellen/202604/pruefi/IFTSTA/PI_21043) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21044](/schnittstellen/202604/pruefi/IFTSTA/PI_21044) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21045](/schnittstellen/202604/pruefi/IFTSTA/PI_21045) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21047](/schnittstellen/202604/pruefi/IFTSTA/PI_21047) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_23001](/schnittstellen/202604/pruefi/INSRPT/PI_23001) | Prüfi | INSRPT | transaktionsdaten |
| [PI_23003](/schnittstellen/202604/pruefi/INSRPT/PI_23003) | Prüfi | INSRPT | transaktionsdaten |
| [PI_23004](/schnittstellen/202604/pruefi/INSRPT/PI_23004) | Prüfi | INSRPT | transaktionsdaten |
| [PI_23005](/schnittstellen/202604/pruefi/INSRPT/PI_23005) | Prüfi | INSRPT | transaktionsdaten |
| [PI_23008](/schnittstellen/202604/pruefi/INSRPT/PI_23008) | Prüfi | INSRPT | transaktionsdaten |
| [PI_23009](/schnittstellen/202604/pruefi/INSRPT/PI_23009) | Prüfi | INSRPT | transaktionsdaten |
| [PI_23011](/schnittstellen/202604/pruefi/INSRPT/PI_23011) | Prüfi | INSRPT | transaktionsdaten |
| [PI_23012](/schnittstellen/202604/pruefi/INSRPT/PI_23012) | Prüfi | INSRPT | transaktionsdaten |
| [PI_25001](/schnittstellen/202604/pruefi/UTILTS/PI_25001) | Prüfi | UTILTS | transaktionsdaten |
| [PI_25004](/schnittstellen/202604/pruefi/UTILTS/PI_25004) | Prüfi | UTILTS | transaktionsdaten |
| [PI_25005](/schnittstellen/202604/pruefi/UTILTS/PI_25005) | Prüfi | UTILTS | transaktionsdaten |
| [PI_25006](/schnittstellen/202604/pruefi/UTILTS/PI_25006) | Prüfi | UTILTS | transaktionsdaten |
| [PI_25007](/schnittstellen/202604/pruefi/UTILTS/PI_25007) | Prüfi | UTILTS | transaktionsdaten |
| [PI_25008](/schnittstellen/202604/pruefi/UTILTS/PI_25008) | Prüfi | UTILTS | transaktionsdaten |
| [PI_25009](/schnittstellen/202604/pruefi/UTILTS/PI_25009) | Prüfi | UTILTS | transaktionsdaten |
| [PI_25010](/schnittstellen/202604/pruefi/UTILTS/PI_25010) | Prüfi | UTILTS | transaktionsdaten |
| [PI_27002](/schnittstellen/202604/pruefi/PRICAT/PI_27002) | Prüfi | PRICAT | transaktionsdaten |
| [PI_27003](/schnittstellen/202604/pruefi/PRICAT/PI_27003) | Prüfi | PRICAT | transaktionsdaten |
| [PI_29001](/schnittstellen/202604/pruefi/COMDIS/PI_29001) | Prüfi | COMDIS | transaktionsdaten |
| [PI_29002](/schnittstellen/202604/pruefi/COMDIS/PI_29002) | Prüfi | COMDIS | transaktionsdaten |
| [PI_31002](/schnittstellen/202604/pruefi/INVOIC/PI_31002) | Prüfi | INVOIC | transaktionsdaten |
| [PI_33001](/schnittstellen/202604/pruefi/REMADV/PI_33001) | Prüfi | REMADV | transaktionsdaten |
| [PI_33002](/schnittstellen/202604/pruefi/REMADV/PI_33002) | Prüfi | REMADV | transaktionsdaten |
| [PI_33003](/schnittstellen/202604/pruefi/REMADV/PI_33003) | Prüfi | REMADV | transaktionsdaten |
| [PI_33004](/schnittstellen/202604/pruefi/REMADV/PI_33004) | Prüfi | REMADV | transaktionsdaten |
| [PI_35001](/schnittstellen/202604/pruefi/REQOTE/PI_35001) | Prüfi | REQOTE | transaktionsdaten |
| [PI_35002](/schnittstellen/202604/pruefi/REQOTE/PI_35002) | Prüfi | REQOTE | transaktionsdaten |
| [PI_35004](/schnittstellen/202604/pruefi/REQOTE/PI_35004) | Prüfi | REQOTE | transaktionsdaten |
| [PI_37000](/schnittstellen/202604/pruefi/PARTIN/PI_37000) | Prüfi | PARTIN | transaktionsdaten |
| [PI_37001](/schnittstellen/202604/pruefi/PARTIN/PI_37001) | Prüfi | PARTIN | transaktionsdaten |
| [PI_37002](/schnittstellen/202604/pruefi/PARTIN/PI_37002) | Prüfi | PARTIN | transaktionsdaten |
| [PI_37008](/schnittstellen/202604/pruefi/PARTIN/PI_37008) | Prüfi | PARTIN | transaktionsdaten |
| [PI_37009](/schnittstellen/202604/pruefi/PARTIN/PI_37009) | Prüfi | PARTIN | transaktionsdaten |
| [PI_37010](/schnittstellen/202604/pruefi/PARTIN/PI_37010) | Prüfi | PARTIN | transaktionsdaten |
| [PI_37012](/schnittstellen/202604/pruefi/PARTIN/PI_37012) | Prüfi | PARTIN | transaktionsdaten |
| [PI_37013](/schnittstellen/202604/pruefi/PARTIN/PI_37013) | Prüfi | PARTIN | transaktionsdaten |
| [PI_37014](/schnittstellen/202604/pruefi/PARTIN/PI_37014) | Prüfi | PARTIN | transaktionsdaten |
| [PI_39000](/schnittstellen/202604/pruefi/ORDCHG/PI_39000) | Prüfi | ORDCHG | transaktionsdaten |
| [PI_39001](/schnittstellen/202604/pruefi/ORDCHG/PI_39001) | Prüfi | ORDCHG | transaktionsdaten |
| [PI_44001](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44001) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44003](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44003) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44004](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44004) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44005](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44005) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44006](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44006) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44007](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44007) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44008](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44008) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44009](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44009) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44010](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44010) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44011](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44011) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44012](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44012) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44015](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44015) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44016](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44016) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44017](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44017) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44018](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44018) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44019](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44019) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44020](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44020) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44021](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44021) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44022](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44022) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44023](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44023) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44024](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44024) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44035](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44035) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44036](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44036) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44037](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44037) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44038](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44038) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44039](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44039) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44040](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44040) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44041](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44041) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44043](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44043) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44044](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44044) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44052](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44052) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44053](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44053) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44060](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44060) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44101](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44101) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44102](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44102) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44103](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44103) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44104](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44104) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44109](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44109) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44111](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44111) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44112](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44112) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44113](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44113) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44115](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44115) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44116](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44116) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44117](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44117) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44119](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44119) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44120](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44120) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44121](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44121) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44123](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44123) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44124](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44124) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44137](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44137) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44138](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44138) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44139](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44139) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44140](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44140) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44142](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44142) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44143](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44143) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44145](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44145) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44146](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44146) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44147](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44147) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44148](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44148) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44149](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44149) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44150](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44150) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44151](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44151) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44152](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44152) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44156](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44156) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44157](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44157) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44159](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44159) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44160](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44160) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44161](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44161) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44162](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44162) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44163](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44163) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44164](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44164) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44165](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44165) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44166](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44166) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44167](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44167) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44168](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44175](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44175) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44176](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44176) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44180](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44180) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44181](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44181) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44182](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44182) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_55001](/schnittstellen/202604/pruefi/UTILMD/PI_55001) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55002](/schnittstellen/202604/pruefi/UTILMD/PI_55002) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55003](/schnittstellen/202604/pruefi/UTILMD/PI_55003) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55004](/schnittstellen/202604/pruefi/UTILMD/PI_55004) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55005](/schnittstellen/202604/pruefi/UTILMD/PI_55005) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55006](/schnittstellen/202604/pruefi/UTILMD/PI_55006) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55007](/schnittstellen/202604/pruefi/UTILMD/PI_55007) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55008](/schnittstellen/202604/pruefi/UTILMD/PI_55008) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55009](/schnittstellen/202604/pruefi/UTILMD/PI_55009) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55010](/schnittstellen/202604/pruefi/UTILMD/PI_55010) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55011](/schnittstellen/202604/pruefi/UTILMD/PI_55011) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55012](/schnittstellen/202604/pruefi/UTILMD/PI_55012) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55013](/schnittstellen/202604/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55014](/schnittstellen/202604/pruefi/UTILMD/PI_55014) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55015](/schnittstellen/202604/pruefi/UTILMD/PI_55015) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55016](/schnittstellen/202604/pruefi/UTILMD/PI_55016) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55017](/schnittstellen/202604/pruefi/UTILMD/PI_55017) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55018](/schnittstellen/202604/pruefi/UTILMD/PI_55018) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55022](/schnittstellen/202604/pruefi/UTILMD/PI_55022) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55023](/schnittstellen/202604/pruefi/UTILMD/PI_55023) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55024](/schnittstellen/202604/pruefi/UTILMD/PI_55024) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55035](/schnittstellen/202604/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55036](/schnittstellen/202604/pruefi/UTILMD/PI_55036) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55037](/schnittstellen/202604/pruefi/UTILMD/PI_55037) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55038](/schnittstellen/202604/pruefi/UTILMD/PI_55038) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55039](/schnittstellen/202604/pruefi/UTILMD/PI_55039) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55040](/schnittstellen/202604/pruefi/UTILMD/PI_55040) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55041](/schnittstellen/202604/pruefi/UTILMD/PI_55041) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55042](/schnittstellen/202604/pruefi/UTILMD/PI_55042) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55044](/schnittstellen/202604/pruefi/UTILMD/PI_55044) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55051](/schnittstellen/202604/pruefi/UTILMD/PI_55051) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55052](/schnittstellen/202604/pruefi/UTILMD/PI_55052) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55053](/schnittstellen/202604/pruefi/UTILMD/PI_55053) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55060](/schnittstellen/202604/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55074](/schnittstellen/202604/pruefi/UTILMD/PI_55074) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55075](/schnittstellen/202604/pruefi/UTILMD/PI_55075) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55077](/schnittstellen/202604/pruefi/UTILMD/PI_55077) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55078](/schnittstellen/202604/pruefi/UTILMD/PI_55078) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55080](/schnittstellen/202604/pruefi/UTILMD/PI_55080) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55095](/schnittstellen/202604/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55109](/schnittstellen/202604/pruefi/UTILMD/PI_55109) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55110](/schnittstellen/202604/pruefi/UTILMD/PI_55110) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55126](/schnittstellen/202604/pruefi/UTILMD/PI_55126) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55136](/schnittstellen/202604/pruefi/UTILMD/PI_55136) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55137](/schnittstellen/202604/pruefi/UTILMD/PI_55137) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55156](/schnittstellen/202604/pruefi/UTILMD/PI_55156) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55170](/schnittstellen/202604/pruefi/UTILMD/PI_55170) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55173](/schnittstellen/202604/pruefi/UTILMD/PI_55173) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55175](/schnittstellen/202604/pruefi/UTILMD/PI_55175) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55177](/schnittstellen/202604/pruefi/UTILMD/PI_55177) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55180](/schnittstellen/202604/pruefi/UTILMD/PI_55180) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55194](/schnittstellen/202604/pruefi/UTILMD/PI_55194) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55218](/schnittstellen/202604/pruefi/UTILMD/PI_55218) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55220](/schnittstellen/202604/pruefi/UTILMD/PI_55220) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55225](/schnittstellen/202604/pruefi/UTILMD/PI_55225) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55227](/schnittstellen/202604/pruefi/UTILMD/PI_55227) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55230](/schnittstellen/202604/pruefi/UTILMD/PI_55230) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55232](/schnittstellen/202604/pruefi/UTILMD/PI_55232) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55553](/schnittstellen/202604/pruefi/UTILMD/PI_55553) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55555](/schnittstellen/202604/pruefi/UTILMD/PI_55555) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55557](/schnittstellen/202604/pruefi/UTILMD/PI_55557) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55559](/schnittstellen/202604/pruefi/UTILMD/PI_55559) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55600](/schnittstellen/202604/pruefi/UTILMD/PI_55600) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55601](/schnittstellen/202604/pruefi/UTILMD/PI_55601) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55602](/schnittstellen/202604/pruefi/UTILMD/PI_55602) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55603](/schnittstellen/202604/pruefi/UTILMD/PI_55603) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55604](/schnittstellen/202604/pruefi/UTILMD/PI_55604) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55605](/schnittstellen/202604/pruefi/UTILMD/PI_55605) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55607](/schnittstellen/202604/pruefi/UTILMD/PI_55607) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55608](/schnittstellen/202604/pruefi/UTILMD/PI_55608) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55609](/schnittstellen/202604/pruefi/UTILMD/PI_55609) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55611](/schnittstellen/202604/pruefi/UTILMD/PI_55611) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55613](/schnittstellen/202604/pruefi/UTILMD/PI_55613) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55614](/schnittstellen/202604/pruefi/UTILMD/PI_55614) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55615](/schnittstellen/202604/pruefi/UTILMD/PI_55615) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55616](/schnittstellen/202604/pruefi/UTILMD/PI_55616) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55617](/schnittstellen/202604/pruefi/UTILMD/PI_55617) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55618](/schnittstellen/202604/pruefi/UTILMD/PI_55618) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55619](/schnittstellen/202604/pruefi/UTILMD/PI_55619) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55620](/schnittstellen/202604/pruefi/UTILMD/PI_55620) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55621](/schnittstellen/202604/pruefi/UTILMD/PI_55621) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55622](/schnittstellen/202604/pruefi/UTILMD/PI_55622) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55623](/schnittstellen/202604/pruefi/UTILMD/PI_55623) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55624](/schnittstellen/202604/pruefi/UTILMD/PI_55624) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55625](/schnittstellen/202604/pruefi/UTILMD/PI_55625) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55626](/schnittstellen/202604/pruefi/UTILMD/PI_55626) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55627](/schnittstellen/202604/pruefi/UTILMD/PI_55627) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55628](/schnittstellen/202604/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55629](/schnittstellen/202604/pruefi/UTILMD/PI_55629) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55630](/schnittstellen/202604/pruefi/UTILMD/PI_55630) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55632](/schnittstellen/202604/pruefi/UTILMD/PI_55632) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55633](/schnittstellen/202604/pruefi/UTILMD/PI_55633) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55634](/schnittstellen/202604/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55635](/schnittstellen/202604/pruefi/UTILMD/PI_55635) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55636](/schnittstellen/202604/pruefi/UTILMD/PI_55636) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55638](/schnittstellen/202604/pruefi/UTILMD/PI_55638) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55639](/schnittstellen/202604/pruefi/UTILMD/PI_55639) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55640](/schnittstellen/202604/pruefi/UTILMD/PI_55640) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55641](/schnittstellen/202604/pruefi/UTILMD/PI_55641) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55642](/schnittstellen/202604/pruefi/UTILMD/PI_55642) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55643](/schnittstellen/202604/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55644](/schnittstellen/202604/pruefi/UTILMD/PI_55644) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55645](/schnittstellen/202604/pruefi/UTILMD/PI_55645) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55646](/schnittstellen/202604/pruefi/UTILMD/PI_55646) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55647](/schnittstellen/202604/pruefi/UTILMD/PI_55647) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55648](/schnittstellen/202604/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55649](/schnittstellen/202604/pruefi/UTILMD/PI_55649) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55650](/schnittstellen/202604/pruefi/UTILMD/PI_55650) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55651](/schnittstellen/202604/pruefi/UTILMD/PI_55651) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55652](/schnittstellen/202604/pruefi/UTILMD/PI_55652) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55653](/schnittstellen/202604/pruefi/UTILMD/PI_55653) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55654](/schnittstellen/202604/pruefi/UTILMD/PI_55654) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55655](/schnittstellen/202604/pruefi/UTILMD/PI_55655) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55656](/schnittstellen/202604/pruefi/UTILMD/PI_55656) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55657](/schnittstellen/202604/pruefi/UTILMD/PI_55657) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55658](/schnittstellen/202604/pruefi/UTILMD/PI_55658) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55659](/schnittstellen/202604/pruefi/UTILMD/PI_55659) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55660](/schnittstellen/202604/pruefi/UTILMD/PI_55660) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55661](/schnittstellen/202604/pruefi/UTILMD/PI_55661) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55662](/schnittstellen/202604/pruefi/UTILMD/PI_55662) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55663](/schnittstellen/202604/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55664](/schnittstellen/202604/pruefi/UTILMD/PI_55664) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55665](/schnittstellen/202604/pruefi/UTILMD/PI_55665) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55666](/schnittstellen/202604/pruefi/UTILMD/PI_55666) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55667](/schnittstellen/202604/pruefi/UTILMD/PI_55667) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55669](/schnittstellen/202604/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55670](/schnittstellen/202604/pruefi/UTILMD/PI_55670) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55672](/schnittstellen/202604/pruefi/UTILMD/PI_55672) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55673](/schnittstellen/202604/pruefi/UTILMD/PI_55673) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55674](/schnittstellen/202604/pruefi/UTILMD/PI_55674) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55684](/schnittstellen/202604/pruefi/UTILMD/PI_55684) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55686](/schnittstellen/202604/pruefi/UTILMD/PI_55686) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55688](/schnittstellen/202604/pruefi/UTILMD/PI_55688) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55690](/schnittstellen/202604/pruefi/UTILMD/PI_55690) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55691](/schnittstellen/202604/pruefi/UTILMD/PI_55691) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55692](/schnittstellen/202604/pruefi/UTILMD/PI_55692) | Prüfi | UTILMD | transaktionsdaten |
| [PI_66666](/schnittstellen/202604/pruefi/APERAK/PI_66666) | Prüfi | APERAK | transaktionsdaten |
| [PI_99999](/schnittstellen/202604/pruefi/APERAK/PI_99999) | Prüfi | APERAK | transaktionsdaten |

### anfragereferenznummer

136 Verwendung(en) in den Nachrichtentypen IFTSTA, INSRPT, ORDCHG, ORDERS, ORDRSP, UTILMD, UTILMD_GAS, UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [[MSB] START_REKLAMATION_DEFINITION](/schnittstellen/202604/trigger/events/MSB-START_REKLAMATION_DEFINITION) | Event | — | transaktionsdaten |
| [[NB] START_REKLAMATION_DEFINITION](/schnittstellen/202604/trigger/events/NB-START_REKLAMATION_DEFINITION) | Event | — | transaktionsdaten |
| [PI_17122](/schnittstellen/202604/pruefi/ORDERS/PI_17122) | Prüfi | ORDERS | transaktionsdaten |
| [PI_19123](/schnittstellen/202604/pruefi/ORDRSP/PI_19123) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_21007](/schnittstellen/202604/pruefi/IFTSTA/PI_21007) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21033](/schnittstellen/202604/pruefi/IFTSTA/PI_21033) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_23003](/schnittstellen/202604/pruefi/INSRPT/PI_23003) | Prüfi | INSRPT | transaktionsdaten |
| [PI_23004](/schnittstellen/202604/pruefi/INSRPT/PI_23004) | Prüfi | INSRPT | transaktionsdaten |
| [PI_23008](/schnittstellen/202604/pruefi/INSRPT/PI_23008) | Prüfi | INSRPT | transaktionsdaten |
| [PI_23009](/schnittstellen/202604/pruefi/INSRPT/PI_23009) | Prüfi | INSRPT | transaktionsdaten |
| [PI_23012](/schnittstellen/202604/pruefi/INSRPT/PI_23012) | Prüfi | INSRPT | transaktionsdaten |
| [PI_25010](/schnittstellen/202604/pruefi/UTILTS/PI_25010) | Prüfi | UTILTS | transaktionsdaten |
| [PI_39001](/schnittstellen/202604/pruefi/ORDCHG/PI_39001) | Prüfi | ORDCHG | transaktionsdaten |
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44003](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44003) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44005](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44005) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44006](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44006) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44008](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44008) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44009](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44009) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44011](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44011) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44012](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44012) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44015](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44015) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44017](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44017) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44018](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44018) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44020](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44020) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44021](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44021) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44023](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44023) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44024](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44024) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44035](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44035) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44036](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44036) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44040](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44040) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44041](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44041) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44043](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44043) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44044](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44044) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44052](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44052) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44053](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44053) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44060](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44060) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44111](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44111) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44115](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44115) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44119](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44119) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44121](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44121) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44124](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44124) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44138](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44138) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44142](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44142) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44145](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44145) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44146](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44146) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44149](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44149) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44151](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44151) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44152](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44152) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44157](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44157) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44161](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44161) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44163](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44163) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44164](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44164) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44167](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44167) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44176](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44176) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44181](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44181) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44182](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44182) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_55002](/schnittstellen/202604/pruefi/UTILMD/PI_55002) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55003](/schnittstellen/202604/pruefi/UTILMD/PI_55003) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55005](/schnittstellen/202604/pruefi/UTILMD/PI_55005) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55006](/schnittstellen/202604/pruefi/UTILMD/PI_55006) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55007](/schnittstellen/202604/pruefi/UTILMD/PI_55007) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55008](/schnittstellen/202604/pruefi/UTILMD/PI_55008) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55009](/schnittstellen/202604/pruefi/UTILMD/PI_55009) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55011](/schnittstellen/202604/pruefi/UTILMD/PI_55011) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55012](/schnittstellen/202604/pruefi/UTILMD/PI_55012) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55013](/schnittstellen/202604/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55014](/schnittstellen/202604/pruefi/UTILMD/PI_55014) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55015](/schnittstellen/202604/pruefi/UTILMD/PI_55015) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55017](/schnittstellen/202604/pruefi/UTILMD/PI_55017) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55018](/schnittstellen/202604/pruefi/UTILMD/PI_55018) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55023](/schnittstellen/202604/pruefi/UTILMD/PI_55023) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55024](/schnittstellen/202604/pruefi/UTILMD/PI_55024) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55035](/schnittstellen/202604/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55036](/schnittstellen/202604/pruefi/UTILMD/PI_55036) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55040](/schnittstellen/202604/pruefi/UTILMD/PI_55040) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55041](/schnittstellen/202604/pruefi/UTILMD/PI_55041) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55044](/schnittstellen/202604/pruefi/UTILMD/PI_55044) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55052](/schnittstellen/202604/pruefi/UTILMD/PI_55052) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55053](/schnittstellen/202604/pruefi/UTILMD/PI_55053) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55060](/schnittstellen/202604/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55074](/schnittstellen/202604/pruefi/UTILMD/PI_55074) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55078](/schnittstellen/202604/pruefi/UTILMD/PI_55078) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55080](/schnittstellen/202604/pruefi/UTILMD/PI_55080) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55095](/schnittstellen/202604/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55136](/schnittstellen/202604/pruefi/UTILMD/PI_55136) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55137](/schnittstellen/202604/pruefi/UTILMD/PI_55137) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55156](/schnittstellen/202604/pruefi/UTILMD/PI_55156) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55170](/schnittstellen/202604/pruefi/UTILMD/PI_55170) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55177](/schnittstellen/202604/pruefi/UTILMD/PI_55177) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55180](/schnittstellen/202604/pruefi/UTILMD/PI_55180) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55194](/schnittstellen/202604/pruefi/UTILMD/PI_55194) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55220](/schnittstellen/202604/pruefi/UTILMD/PI_55220) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55227](/schnittstellen/202604/pruefi/UTILMD/PI_55227) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55232](/schnittstellen/202604/pruefi/UTILMD/PI_55232) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55555](/schnittstellen/202604/pruefi/UTILMD/PI_55555) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55559](/schnittstellen/202604/pruefi/UTILMD/PI_55559) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55602](/schnittstellen/202604/pruefi/UTILMD/PI_55602) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55603](/schnittstellen/202604/pruefi/UTILMD/PI_55603) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55604](/schnittstellen/202604/pruefi/UTILMD/PI_55604) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55605](/schnittstellen/202604/pruefi/UTILMD/PI_55605) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55607](/schnittstellen/202604/pruefi/UTILMD/PI_55607) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55608](/schnittstellen/202604/pruefi/UTILMD/PI_55608) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55609](/schnittstellen/202604/pruefi/UTILMD/PI_55609) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55614](/schnittstellen/202604/pruefi/UTILMD/PI_55614) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55621](/schnittstellen/202604/pruefi/UTILMD/PI_55621) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55622](/schnittstellen/202604/pruefi/UTILMD/PI_55622) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55623](/schnittstellen/202604/pruefi/UTILMD/PI_55623) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55624](/schnittstellen/202604/pruefi/UTILMD/PI_55624) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55625](/schnittstellen/202604/pruefi/UTILMD/PI_55625) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55626](/schnittstellen/202604/pruefi/UTILMD/PI_55626) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55633](/schnittstellen/202604/pruefi/UTILMD/PI_55633) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55634](/schnittstellen/202604/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55635](/schnittstellen/202604/pruefi/UTILMD/PI_55635) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55636](/schnittstellen/202604/pruefi/UTILMD/PI_55636) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55638](/schnittstellen/202604/pruefi/UTILMD/PI_55638) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55644](/schnittstellen/202604/pruefi/UTILMD/PI_55644) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55645](/schnittstellen/202604/pruefi/UTILMD/PI_55645) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55646](/schnittstellen/202604/pruefi/UTILMD/PI_55646) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55647](/schnittstellen/202604/pruefi/UTILMD/PI_55647) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55648](/schnittstellen/202604/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55654](/schnittstellen/202604/pruefi/UTILMD/PI_55654) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55655](/schnittstellen/202604/pruefi/UTILMD/PI_55655) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55656](/schnittstellen/202604/pruefi/UTILMD/PI_55656) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55657](/schnittstellen/202604/pruefi/UTILMD/PI_55657) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55658](/schnittstellen/202604/pruefi/UTILMD/PI_55658) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55664](/schnittstellen/202604/pruefi/UTILMD/PI_55664) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55665](/schnittstellen/202604/pruefi/UTILMD/PI_55665) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55666](/schnittstellen/202604/pruefi/UTILMD/PI_55666) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55667](/schnittstellen/202604/pruefi/UTILMD/PI_55667) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55669](/schnittstellen/202604/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55673](/schnittstellen/202604/pruefi/UTILMD/PI_55673) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55692](/schnittstellen/202604/pruefi/UTILMD/PI_55692) | Prüfi | UTILMD | transaktionsdaten |

### vorgangsreferenznummer

34 Verwendung(en) in den Nachrichtentypen IFTSTA, MSCONS, ORDERS, ORDRSP, PARTIN, PRICAT, REQOTE, UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [[LF] START_VERSAND_ANF_STORNO](/schnittstellen/202604/trigger/events/LF-START_VERSAND_ANF_STORNO) | Event | — | transaktionsdaten |
| [[LF] START_VERSAND_STORNO_MSCONS](/schnittstellen/202604/trigger/events/LF-START_VERSAND_STORNO_MSCONS) | Event | — | transaktionsdaten |
| [[MSB] START_VERSAND_ANF_STORNO](/schnittstellen/202604/trigger/events/MSB-START_VERSAND_ANF_STORNO) | Event | — | transaktionsdaten |
| [[MSB] START_VERSAND_STORNO_MSCONS](/schnittstellen/202604/trigger/events/MSB-START_VERSAND_STORNO_MSCONS) | Event | — | transaktionsdaten |
| [[NB] START_VERSAND_ANF_STORNO](/schnittstellen/202604/trigger/events/NB-START_VERSAND_ANF_STORNO) | Event | — | transaktionsdaten |
| [[NB] START_VERSAND_STORNO_MSCONS](/schnittstellen/202604/trigger/events/NB-START_VERSAND_STORNO_MSCONS) | Event | — | transaktionsdaten |
| [PI_13006](/schnittstellen/202604/pruefi/MSCONS/PI_13006) | Prüfi | MSCONS | transaktionsdaten |
| [PI_17130](/schnittstellen/202604/pruefi/ORDERS/PI_17130) | Prüfi | ORDERS | transaktionsdaten |
| [PI_19006](/schnittstellen/202604/pruefi/ORDRSP/PI_19006) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19013](/schnittstellen/202604/pruefi/ORDRSP/PI_19013) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19014](/schnittstellen/202604/pruefi/ORDRSP/PI_19014) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19123](/schnittstellen/202604/pruefi/ORDRSP/PI_19123) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19128](/schnittstellen/202604/pruefi/ORDRSP/PI_19128) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19129](/schnittstellen/202604/pruefi/ORDRSP/PI_19129) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_21011](/schnittstellen/202604/pruefi/IFTSTA/PI_21011) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21012](/schnittstellen/202604/pruefi/IFTSTA/PI_21012) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21030](/schnittstellen/202604/pruefi/IFTSTA/PI_21030) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21031](/schnittstellen/202604/pruefi/IFTSTA/PI_21031) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21035](/schnittstellen/202604/pruefi/IFTSTA/PI_21035) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21047](/schnittstellen/202604/pruefi/IFTSTA/PI_21047) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_27002](/schnittstellen/202604/pruefi/PRICAT/PI_27002) | Prüfi | PRICAT | transaktionsdaten |
| [PI_27003](/schnittstellen/202604/pruefi/PRICAT/PI_27003) | Prüfi | PRICAT | transaktionsdaten |
| [PI_35004](/schnittstellen/202604/pruefi/REQOTE/PI_35004) | Prüfi | REQOTE | transaktionsdaten |
| [PI_37000](/schnittstellen/202604/pruefi/PARTIN/PI_37000) | Prüfi | PARTIN | transaktionsdaten |
| [PI_37001](/schnittstellen/202604/pruefi/PARTIN/PI_37001) | Prüfi | PARTIN | transaktionsdaten |
| [PI_37002](/schnittstellen/202604/pruefi/PARTIN/PI_37002) | Prüfi | PARTIN | transaktionsdaten |
| [PI_37008](/schnittstellen/202604/pruefi/PARTIN/PI_37008) | Prüfi | PARTIN | transaktionsdaten |
| [PI_37009](/schnittstellen/202604/pruefi/PARTIN/PI_37009) | Prüfi | PARTIN | transaktionsdaten |
| [PI_37010](/schnittstellen/202604/pruefi/PARTIN/PI_37010) | Prüfi | PARTIN | transaktionsdaten |
| [PI_37012](/schnittstellen/202604/pruefi/PARTIN/PI_37012) | Prüfi | PARTIN | transaktionsdaten |
| [PI_37013](/schnittstellen/202604/pruefi/PARTIN/PI_37013) | Prüfi | PARTIN | transaktionsdaten |
| [PI_37014](/schnittstellen/202604/pruefi/PARTIN/PI_37014) | Prüfi | PARTIN | transaktionsdaten |
| [PI_44022](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44022) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_55022](/schnittstellen/202604/pruefi/UTILMD/PI_55022) | Prüfi | UTILMD | transaktionsdaten |

### sendungsposition

7 Verwendung(en) in den Nachrichtentypen IFTSTA.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_21025](/schnittstellen/202604/pruefi/IFTSTA/PI_21025) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21027](/schnittstellen/202604/pruefi/IFTSTA/PI_21027) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21033](/schnittstellen/202604/pruefi/IFTSTA/PI_21033) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21039](/schnittstellen/202604/pruefi/IFTSTA/PI_21039) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21043](/schnittstellen/202604/pruefi/IFTSTA/PI_21043) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21045](/schnittstellen/202604/pruefi/IFTSTA/PI_21045) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21047](/schnittstellen/202604/pruefi/IFTSTA/PI_21047) | Prüfi | IFTSTA | transaktionsdaten |

### positionsnummer

3 Verwendung(en) in den Nachrichtentypen REQOTE.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_35001](/schnittstellen/202604/pruefi/REQOTE/PI_35001) | Prüfi | REQOTE | transaktionsdaten |
| [PI_35002](/schnittstellen/202604/pruefi/REQOTE/PI_35002) | Prüfi | REQOTE | transaktionsdaten |
| [PI_35004](/schnittstellen/202604/pruefi/REQOTE/PI_35004) | Prüfi | REQOTE | transaktionsdaten |

### mitteilungsnummer

4 Verwendung(en) in den Nachrichtentypen IFTSTA.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_21011](/schnittstellen/202604/pruefi/IFTSTA/PI_21011) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21012](/schnittstellen/202604/pruefi/IFTSTA/PI_21012) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21030](/schnittstellen/202604/pruefi/IFTSTA/PI_21030) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21031](/schnittstellen/202604/pruefi/IFTSTA/PI_21031) | Prüfi | IFTSTA | transaktionsdaten |

### typ

5 Verwendung(en).

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [[LF] START_VERSAND_STORNO_MSCONS](/schnittstellen/202604/trigger/events/LF-START_VERSAND_STORNO_MSCONS) | Event | — | transaktionsdaten |
| [[MSB] START_ERHEBUNG_MESSWERTE](/schnittstellen/202604/trigger/events/MSB-START_ERHEBUNG_MESSWERTE) | Event | — | transaktionsdaten |
| [[MSB] START_VERSAND_STORNO_MSCONS](/schnittstellen/202604/trigger/events/MSB-START_VERSAND_STORNO_MSCONS) | Event | — | transaktionsdaten |
| [[NB] START_ERHEBUNG_MESSWERTE](/schnittstellen/202604/trigger/events/NB-START_ERHEBUNG_MESSWERTE) | Event | — | transaktionsdaten |
| [[NB] START_VERSAND_STORNO_MSCONS](/schnittstellen/202604/trigger/events/NB-START_VERSAND_STORNO_MSCONS) | Event | — | transaktionsdaten |

### anfrageReferenz

31 Verwendung(en) in den Nachrichtentypen IFTSTA, MSCONS, UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [[LF] START_ERHEBUNG_MESSWERTE](/schnittstellen/202604/trigger/events/LF-START_ERHEBUNG_MESSWERTE) | Event | — | transaktionsdaten |
| [[LF] START_UEBERM_DEFINITION](/schnittstellen/202604/trigger/events/LF-START_UEBERM_DEFINITION) | Event | — | transaktionsdaten |
| [[LF] START_UEBERSICHT_LEISTUNGSKURVENDEF](/schnittstellen/202604/trigger/events/LF-START_UEBERSICHT_LEISTUNGSKURVENDEF) | Event | — | transaktionsdaten |
| [[LF] START_UEBERSICHT_SCHALTZEITDEF](/schnittstellen/202604/trigger/events/LF-START_UEBERSICHT_SCHALTZEITDEF) | Event | — | transaktionsdaten |
| [[LF] START_UEBERSICHT_ZAEHLZEITDEF](/schnittstellen/202604/trigger/events/LF-START_UEBERSICHT_ZAEHLZEITDEF) | Event | — | transaktionsdaten |
| [[MSB] START_ERHEBUNG_MESSWERTE](/schnittstellen/202604/trigger/events/MSB-START_ERHEBUNG_MESSWERTE) | Event | — | transaktionsdaten |
| [[NB] START_ERHEBUNG_MESSWERTE](/schnittstellen/202604/trigger/events/NB-START_ERHEBUNG_MESSWERTE) | Event | — | transaktionsdaten |
| [[NB] START_UEBERM_DEFINITION](/schnittstellen/202604/trigger/events/NB-START_UEBERM_DEFINITION) | Event | — | transaktionsdaten |
| [[NB] START_UEBERSICHT_LEISTUNGSKURVENDEF](/schnittstellen/202604/trigger/events/NB-START_UEBERSICHT_LEISTUNGSKURVENDEF) | Event | — | transaktionsdaten |
| [[NB] START_UEBERSICHT_SCHALTZEITDEF](/schnittstellen/202604/trigger/events/NB-START_UEBERSICHT_SCHALTZEITDEF) | Event | — | transaktionsdaten |
| [[NB] START_UEBERSICHT_ZAEHLZEITDEF](/schnittstellen/202604/trigger/events/NB-START_UEBERSICHT_ZAEHLZEITDEF) | Event | — | transaktionsdaten |
| [[NB] START_VERSAND_GEMESSENE_ARB_LEIST_WERTE](/schnittstellen/202604/trigger/events/NB-START_VERSAND_GEMESSENE_ARB_LEIST_WERTE) | Event | — | transaktionsdaten |
| [[NB] START_VERSAND_LIEFERSCHEIN](/schnittstellen/202604/trigger/events/NB-START_VERSAND_LIEFERSCHEIN) | Event | — | transaktionsdaten |
| [PI_13002](/schnittstellen/202604/pruefi/MSCONS/PI_13002) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13008](/schnittstellen/202604/pruefi/MSCONS/PI_13008) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13009](/schnittstellen/202604/pruefi/MSCONS/PI_13009) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13015](/schnittstellen/202604/pruefi/MSCONS/PI_13015) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13016](/schnittstellen/202604/pruefi/MSCONS/PI_13016) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13017](/schnittstellen/202604/pruefi/MSCONS/PI_13017) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13018](/schnittstellen/202604/pruefi/MSCONS/PI_13018) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13019](/schnittstellen/202604/pruefi/MSCONS/PI_13019) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13025](/schnittstellen/202604/pruefi/MSCONS/PI_13025) | Prüfi | MSCONS | transaktionsdaten |
| [PI_13027](/schnittstellen/202604/pruefi/MSCONS/PI_13027) | Prüfi | MSCONS | transaktionsdaten |
| [PI_21043](/schnittstellen/202604/pruefi/IFTSTA/PI_21043) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21044](/schnittstellen/202604/pruefi/IFTSTA/PI_21044) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_25004](/schnittstellen/202604/pruefi/UTILTS/PI_25004) | Prüfi | UTILTS | transaktionsdaten |
| [PI_25005](/schnittstellen/202604/pruefi/UTILTS/PI_25005) | Prüfi | UTILTS | transaktionsdaten |
| [PI_25006](/schnittstellen/202604/pruefi/UTILTS/PI_25006) | Prüfi | UTILTS | transaktionsdaten |
| [PI_25007](/schnittstellen/202604/pruefi/UTILTS/PI_25007) | Prüfi | UTILTS | transaktionsdaten |
| [PI_25008](/schnittstellen/202604/pruefi/UTILTS/PI_25008) | Prüfi | UTILTS | transaktionsdaten |
| [PI_25009](/schnittstellen/202604/pruefi/UTILTS/PI_25009) | Prüfi | UTILTS | transaktionsdaten |

### auftragsReferenz

31 Verwendung(en) in den Nachrichtentypen ORDCHG, ORDRSP.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [[LF] START_STORNO_SE_AUFTRAG](/schnittstellen/202604/trigger/events/LF-START_STORNO_SE_AUFTRAG) | Event | — | transaktionsdaten |
| [PI_19001](/schnittstellen/202604/pruefi/ORDRSP/PI_19001) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19002](/schnittstellen/202604/pruefi/ORDRSP/PI_19002) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19003](/schnittstellen/202604/pruefi/ORDRSP/PI_19003) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19004](/schnittstellen/202604/pruefi/ORDRSP/PI_19004) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19005](/schnittstellen/202604/pruefi/ORDRSP/PI_19005) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19006](/schnittstellen/202604/pruefi/ORDRSP/PI_19006) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19007](/schnittstellen/202604/pruefi/ORDRSP/PI_19007) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19009](/schnittstellen/202604/pruefi/ORDRSP/PI_19009) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19010](/schnittstellen/202604/pruefi/ORDRSP/PI_19010) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19011](/schnittstellen/202604/pruefi/ORDRSP/PI_19011) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19012](/schnittstellen/202604/pruefi/ORDRSP/PI_19012) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19015](/schnittstellen/202604/pruefi/ORDRSP/PI_19015) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19016](/schnittstellen/202604/pruefi/ORDRSP/PI_19016) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19101](/schnittstellen/202604/pruefi/ORDRSP/PI_19101) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19102](/schnittstellen/202604/pruefi/ORDRSP/PI_19102) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19103](/schnittstellen/202604/pruefi/ORDRSP/PI_19103) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19104](/schnittstellen/202604/pruefi/ORDRSP/PI_19104) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19114](/schnittstellen/202604/pruefi/ORDRSP/PI_19114) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19116](/schnittstellen/202604/pruefi/ORDRSP/PI_19116) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19117](/schnittstellen/202604/pruefi/ORDRSP/PI_19117) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19118](/schnittstellen/202604/pruefi/ORDRSP/PI_19118) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19119](/schnittstellen/202604/pruefi/ORDRSP/PI_19119) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19121](/schnittstellen/202604/pruefi/ORDRSP/PI_19121) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19123](/schnittstellen/202604/pruefi/ORDRSP/PI_19123) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19124](/schnittstellen/202604/pruefi/ORDRSP/PI_19124) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19133](/schnittstellen/202604/pruefi/ORDRSP/PI_19133) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19301](/schnittstellen/202604/pruefi/ORDRSP/PI_19301) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19302](/schnittstellen/202604/pruefi/ORDRSP/PI_19302) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_39000](/schnittstellen/202604/pruefi/ORDCHG/PI_39000) | Prüfi | ORDCHG | transaktionsdaten |
| [PI_39001](/schnittstellen/202604/pruefi/ORDCHG/PI_39001) | Prüfi | ORDCHG | transaktionsdaten |

### vertragsbeginn

70 Verwendung(en) in den Nachrichtentypen UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [[LF] START_BESTELLUNG_SDAE](/schnittstellen/202604/trigger/events/LF-START_BESTELLUNG_SDAE) | Event | — | transaktionsdaten |
| [[LF] START_LIEFERBEGINN](/schnittstellen/202604/trigger/events/LF-START_LIEFERBEGINN) | Event | — | transaktionsdaten |
| [[LF] START_VERSAND_SDAE](/schnittstellen/202604/trigger/events/LF-START_VERSAND_SDAE) | Event | — | transaktionsdaten |
| [[NB] START_AUFH_ZUK_ZUORDNUNG](/schnittstellen/202604/trigger/events/NB-START_AUFH_ZUK_ZUORDNUNG) | Event | — | transaktionsdaten |
| [[NB] START_EOG](/schnittstellen/202604/trigger/events/NB-START_EOG) | Event | — | transaktionsdaten |
| [PI_44001](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44001) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44004](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44004) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44005](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44005) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44019](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44019) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44020](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44020) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44021](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44021) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44038](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44038) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44052](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44052) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44101](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44101) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44102](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44102) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44103](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44103) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44104](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44104) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44109](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44109) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44112](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44112) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44113](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44113) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44116](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44116) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44117](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44117) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44120](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44120) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44123](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44123) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44137](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44137) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44138](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44138) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44139](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44139) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44140](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44140) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44142](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44142) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44143](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44143) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44145](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44145) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44147](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44147) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44148](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44148) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44149](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44149) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44150](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44150) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44151](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44151) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44156](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44156) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44157](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44157) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44159](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44159) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44160](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44160) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44162](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44162) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44163](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44163) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44165](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44165) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44166](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44166) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44167](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44167) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44175](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44175) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44176](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44176) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44180](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44180) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44181](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44181) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_55001](/schnittstellen/202604/pruefi/UTILMD/PI_55001) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55002](/schnittstellen/202604/pruefi/UTILMD/PI_55002) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55004](/schnittstellen/202604/pruefi/UTILMD/PI_55004) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55005](/schnittstellen/202604/pruefi/UTILMD/PI_55005) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55013](/schnittstellen/202604/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55014](/schnittstellen/202604/pruefi/UTILMD/PI_55014) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55038](/schnittstellen/202604/pruefi/UTILMD/PI_55038) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55051](/schnittstellen/202604/pruefi/UTILMD/PI_55051) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55052](/schnittstellen/202604/pruefi/UTILMD/PI_55052) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55077](/schnittstellen/202604/pruefi/UTILMD/PI_55077) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55078](/schnittstellen/202604/pruefi/UTILMD/PI_55078) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55600](/schnittstellen/202604/pruefi/UTILMD/PI_55600) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55601](/schnittstellen/202604/pruefi/UTILMD/PI_55601) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55602](/schnittstellen/202604/pruefi/UTILMD/PI_55602) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55603](/schnittstellen/202604/pruefi/UTILMD/PI_55603) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55607](/schnittstellen/202604/pruefi/UTILMD/PI_55607) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55608](/schnittstellen/202604/pruefi/UTILMD/PI_55608) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55611](/schnittstellen/202604/pruefi/UTILMD/PI_55611) | Prüfi | UTILMD | transaktionsdaten |

### vertragsende

46 Verwendung(en) in den Nachrichtentypen UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [[LF] START_ANFRAGE_STAMMDATENAENDERUNG GAS](/schnittstellen/202604/trigger/events/LF-START_ANFRAGE_STAMMDATENAENDERUNG-GAS) | Event | — | transaktionsdaten |
| [PI_44001](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44001) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44004](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44004) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44005](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44005) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44007](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44007) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44008](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44008) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44010](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44010) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44011](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44011) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44016](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44016) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44017](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44017) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44019](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44019) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44020](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44020) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44021](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44021) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44037](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44037) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44039](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44039) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44040](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44040) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44052](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44052) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44101](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44101) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44102](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44102) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44103](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44103) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44104](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44104) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_55001](/schnittstellen/202604/pruefi/UTILMD/PI_55001) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55002](/schnittstellen/202604/pruefi/UTILMD/PI_55002) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55004](/schnittstellen/202604/pruefi/UTILMD/PI_55004) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55005](/schnittstellen/202604/pruefi/UTILMD/PI_55005) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55007](/schnittstellen/202604/pruefi/UTILMD/PI_55007) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55008](/schnittstellen/202604/pruefi/UTILMD/PI_55008) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55010](/schnittstellen/202604/pruefi/UTILMD/PI_55010) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55011](/schnittstellen/202604/pruefi/UTILMD/PI_55011) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55013](/schnittstellen/202604/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55014](/schnittstellen/202604/pruefi/UTILMD/PI_55014) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55016](/schnittstellen/202604/pruefi/UTILMD/PI_55016) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55017](/schnittstellen/202604/pruefi/UTILMD/PI_55017) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55037](/schnittstellen/202604/pruefi/UTILMD/PI_55037) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55039](/schnittstellen/202604/pruefi/UTILMD/PI_55039) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55040](/schnittstellen/202604/pruefi/UTILMD/PI_55040) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55051](/schnittstellen/202604/pruefi/UTILMD/PI_55051) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55052](/schnittstellen/202604/pruefi/UTILMD/PI_55052) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55600](/schnittstellen/202604/pruefi/UTILMD/PI_55600) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55602](/schnittstellen/202604/pruefi/UTILMD/PI_55602) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55607](/schnittstellen/202604/pruefi/UTILMD/PI_55607) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55608](/schnittstellen/202604/pruefi/UTILMD/PI_55608) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55611](/schnittstellen/202604/pruefi/UTILMD/PI_55611) | Prüfi | UTILMD | transaktionsdaten |

### ausfuehrungsdatum

2 Verwendung(en) in den Nachrichtentypen REQOTE.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [[LF] START_MALOIDENT](/schnittstellen/202604/trigger/events/LF-START_MALOIDENT) | Event | — | transaktionsdaten |
| [PI_35002](/schnittstellen/202604/pruefi/REQOTE/PI_35002) | Prüfi | REQOTE | transaktionsdaten |

### lieferdatum

6 Verwendung(en) in den Nachrichtentypen IFTSTA, REQOTE.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [[LF] START_ANFRAGE_KONFIGURATION](/schnittstellen/202604/trigger/events/LF-START_ANFRAGE_KONFIGURATION) | Event | — | transaktionsdaten |
| [PI_21007](/schnittstellen/202604/pruefi/IFTSTA/PI_21007) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21029](/schnittstellen/202604/pruefi/IFTSTA/PI_21029) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21030](/schnittstellen/202604/pruefi/IFTSTA/PI_21030) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_35001](/schnittstellen/202604/pruefi/REQOTE/PI_35001) | Prüfi | REQOTE | transaktionsdaten |
| [PI_35004](/schnittstellen/202604/pruefi/REQOTE/PI_35004) | Prüfi | REQOTE | transaktionsdaten |

### startdatum

4 Verwendung(en) in den Nachrichtentypen IFTSTA, QUOTES, REQOTE.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_15003](/schnittstellen/202604/pruefi/QUOTES/PI_15003) | Prüfi | QUOTES | transaktionsdaten |
| [PI_21029](/schnittstellen/202604/pruefi/IFTSTA/PI_21029) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21033](/schnittstellen/202604/pruefi/IFTSTA/PI_21033) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_35002](/schnittstellen/202604/pruefi/REQOTE/PI_35002) | Prüfi | REQOTE | transaktionsdaten |

### enddatum

1 Verwendung(en) in den Nachrichtentypen IFTSTA.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_21029](/schnittstellen/202604/pruefi/IFTSTA/PI_21029) | Prüfi | IFTSTA | transaktionsdaten |

### verwendungAb

3 Verwendung(en) in den Nachrichtentypen IFTSTA.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [[LF] START_UEBERMITTLUNG_ENFG](/schnittstellen/202604/trigger/events/LF-START_UEBERMITTLUNG_ENFG) | Event | — | transaktionsdaten |
| [PI_21035](/schnittstellen/202604/pruefi/IFTSTA/PI_21035) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21045](/schnittstellen/202604/pruefi/IFTSTA/PI_21045) | Prüfi | IFTSTA | transaktionsdaten |

### verwendungBis

3 Verwendung(en) in den Nachrichtentypen IFTSTA.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [[NB] START_VERSAND_BEENDIGUNG_AGV](/schnittstellen/202604/trigger/events/NB-START_VERSAND_BEENDIGUNG_AGV) | Event | — | transaktionsdaten |
| [PI_21035](/schnittstellen/202604/pruefi/IFTSTA/PI_21035) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21045](/schnittstellen/202604/pruefi/IFTSTA/PI_21045) | Prüfi | IFTSTA | transaktionsdaten |

### leistungsperiode

1 Verwendung(en) in den Nachrichtentypen IFTSTA.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_21035](/schnittstellen/202604/pruefi/IFTSTA/PI_21035) | Prüfi | IFTSTA | transaktionsdaten |

### angebotsnummer

5 Verwendung(en) in den Nachrichtentypen IFTSTA, ORDERS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [[LF] START_BESTELLUNG_ANGEBOT_KONFIGURATION](/schnittstellen/202604/trigger/events/LF-START_BESTELLUNG_ANGEBOT_KONFIGURATION) | Event | — | transaktionsdaten |
| [PI_17001](/schnittstellen/202604/pruefi/ORDERS/PI_17001) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17005](/schnittstellen/202604/pruefi/ORDERS/PI_17005) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17131](/schnittstellen/202604/pruefi/ORDERS/PI_17131) | Prüfi | ORDERS | transaktionsdaten |
| [PI_21032](/schnittstellen/202604/pruefi/IFTSTA/PI_21032) | Prüfi | IFTSTA | transaktionsdaten |

### angebotsreferenz

3 Verwendung(en) in den Nachrichtentypen ORDERS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [[NB] START_REKLAMATION_WERTE](/schnittstellen/202604/trigger/events/NB-START_REKLAMATION_WERTE) | Event | — | transaktionsdaten |
| [PI_17113](/schnittstellen/202604/pruefi/ORDERS/PI_17113) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17122](/schnittstellen/202604/pruefi/ORDERS/PI_17122) | Prüfi | ORDERS | transaktionsdaten |

### identifikationslogik

2 Verwendung(en) in den Nachrichtentypen UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_44001](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44001) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44016](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44016) | Prüfi | UTILMD_GAS | transaktionsdaten |

### antwortstatus

120 Verwendung(en) in den Nachrichtentypen IFTSTA, ORDRSP, UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [[MSB] START_ANTWORT_GERAETEWECHSEL](/schnittstellen/202604/trigger/events/MSB-START_ANTWORT_GERAETEWECHSEL) | Event | — | transaktionsdaten |
| [[NB] START_AUFTRAGSSTATUS](/schnittstellen/202604/trigger/events/NB-START_AUFTRAGSSTATUS) | Event | — | transaktionsdaten |
| [PI_19001](/schnittstellen/202604/pruefi/ORDRSP/PI_19001) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19002](/schnittstellen/202604/pruefi/ORDRSP/PI_19002) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19003](/schnittstellen/202604/pruefi/ORDRSP/PI_19003) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19004](/schnittstellen/202604/pruefi/ORDRSP/PI_19004) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19005](/schnittstellen/202604/pruefi/ORDRSP/PI_19005) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19006](/schnittstellen/202604/pruefi/ORDRSP/PI_19006) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19007](/schnittstellen/202604/pruefi/ORDRSP/PI_19007) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19009](/schnittstellen/202604/pruefi/ORDRSP/PI_19009) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19010](/schnittstellen/202604/pruefi/ORDRSP/PI_19010) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19011](/schnittstellen/202604/pruefi/ORDRSP/PI_19011) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19012](/schnittstellen/202604/pruefi/ORDRSP/PI_19012) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19013](/schnittstellen/202604/pruefi/ORDRSP/PI_19013) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19014](/schnittstellen/202604/pruefi/ORDRSP/PI_19014) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19015](/schnittstellen/202604/pruefi/ORDRSP/PI_19015) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19016](/schnittstellen/202604/pruefi/ORDRSP/PI_19016) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19101](/schnittstellen/202604/pruefi/ORDRSP/PI_19101) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19102](/schnittstellen/202604/pruefi/ORDRSP/PI_19102) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19103](/schnittstellen/202604/pruefi/ORDRSP/PI_19103) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19104](/schnittstellen/202604/pruefi/ORDRSP/PI_19104) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19114](/schnittstellen/202604/pruefi/ORDRSP/PI_19114) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19116](/schnittstellen/202604/pruefi/ORDRSP/PI_19116) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19117](/schnittstellen/202604/pruefi/ORDRSP/PI_19117) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19118](/schnittstellen/202604/pruefi/ORDRSP/PI_19118) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19119](/schnittstellen/202604/pruefi/ORDRSP/PI_19119) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19121](/schnittstellen/202604/pruefi/ORDRSP/PI_19121) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19123](/schnittstellen/202604/pruefi/ORDRSP/PI_19123) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19124](/schnittstellen/202604/pruefi/ORDRSP/PI_19124) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19128](/schnittstellen/202604/pruefi/ORDRSP/PI_19128) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19129](/schnittstellen/202604/pruefi/ORDRSP/PI_19129) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19133](/schnittstellen/202604/pruefi/ORDRSP/PI_19133) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19301](/schnittstellen/202604/pruefi/ORDRSP/PI_19301) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19302](/schnittstellen/202604/pruefi/ORDRSP/PI_19302) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_21007](/schnittstellen/202604/pruefi/IFTSTA/PI_21007) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21011](/schnittstellen/202604/pruefi/IFTSTA/PI_21011) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21013](/schnittstellen/202604/pruefi/IFTSTA/PI_21013) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21025](/schnittstellen/202604/pruefi/IFTSTA/PI_21025) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21027](/schnittstellen/202604/pruefi/IFTSTA/PI_21027) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21028](/schnittstellen/202604/pruefi/IFTSTA/PI_21028) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21030](/schnittstellen/202604/pruefi/IFTSTA/PI_21030) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21031](/schnittstellen/202604/pruefi/IFTSTA/PI_21031) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21032](/schnittstellen/202604/pruefi/IFTSTA/PI_21032) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21033](/schnittstellen/202604/pruefi/IFTSTA/PI_21033) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21035](/schnittstellen/202604/pruefi/IFTSTA/PI_21035) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21039](/schnittstellen/202604/pruefi/IFTSTA/PI_21039) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21043](/schnittstellen/202604/pruefi/IFTSTA/PI_21043) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21047](/schnittstellen/202604/pruefi/IFTSTA/PI_21047) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44003](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44003) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44005](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44005) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44006](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44006) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44008](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44008) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44009](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44009) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44011](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44011) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44012](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44012) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44015](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44015) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44017](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44017) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44018](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44018) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44021](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44021) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44023](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44023) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44024](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44024) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44040](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44040) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44041](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44041) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44043](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44043) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44044](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44044) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44052](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44052) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44053](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44053) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44111](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44111) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44115](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44115) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44119](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44119) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44121](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44121) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44124](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44124) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44138](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44138) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44142](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44142) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44145](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44145) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44146](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44146) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44149](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44149) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44151](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44151) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44152](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44152) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44157](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44157) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44161](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44161) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44163](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44163) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44164](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44164) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44167](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44167) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44176](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44176) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44181](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44181) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44182](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44182) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_55002](/schnittstellen/202604/pruefi/UTILMD/PI_55002) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55003](/schnittstellen/202604/pruefi/UTILMD/PI_55003) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55005](/schnittstellen/202604/pruefi/UTILMD/PI_55005) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55006](/schnittstellen/202604/pruefi/UTILMD/PI_55006) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55008](/schnittstellen/202604/pruefi/UTILMD/PI_55008) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55009](/schnittstellen/202604/pruefi/UTILMD/PI_55009) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55011](/schnittstellen/202604/pruefi/UTILMD/PI_55011) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55012](/schnittstellen/202604/pruefi/UTILMD/PI_55012) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55014](/schnittstellen/202604/pruefi/UTILMD/PI_55014) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55015](/schnittstellen/202604/pruefi/UTILMD/PI_55015) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55017](/schnittstellen/202604/pruefi/UTILMD/PI_55017) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55018](/schnittstellen/202604/pruefi/UTILMD/PI_55018) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55023](/schnittstellen/202604/pruefi/UTILMD/PI_55023) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55024](/schnittstellen/202604/pruefi/UTILMD/PI_55024) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55040](/schnittstellen/202604/pruefi/UTILMD/PI_55040) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55041](/schnittstellen/202604/pruefi/UTILMD/PI_55041) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55044](/schnittstellen/202604/pruefi/UTILMD/PI_55044) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55052](/schnittstellen/202604/pruefi/UTILMD/PI_55052) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55053](/schnittstellen/202604/pruefi/UTILMD/PI_55053) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55078](/schnittstellen/202604/pruefi/UTILMD/PI_55078) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55080](/schnittstellen/202604/pruefi/UTILMD/PI_55080) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55170](/schnittstellen/202604/pruefi/UTILMD/PI_55170) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55602](/schnittstellen/202604/pruefi/UTILMD/PI_55602) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55603](/schnittstellen/202604/pruefi/UTILMD/PI_55603) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55604](/schnittstellen/202604/pruefi/UTILMD/PI_55604) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55605](/schnittstellen/202604/pruefi/UTILMD/PI_55605) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55608](/schnittstellen/202604/pruefi/UTILMD/PI_55608) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55609](/schnittstellen/202604/pruefi/UTILMD/PI_55609) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55692](/schnittstellen/202604/pruefi/UTILMD/PI_55692) | Prüfi | UTILMD | transaktionsdaten |

### antwortstatusCodeliste

120 Verwendung(en) in den Nachrichtentypen COMDIS, IFTSTA, ORDRSP, UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [[MSB] START_ANTWORT_GERAETEWECHSEL](/schnittstellen/202604/trigger/events/MSB-START_ANTWORT_GERAETEWECHSEL) | Event | — | transaktionsdaten |
| [[NB] START_AUFTRAGSSTATUS](/schnittstellen/202604/trigger/events/NB-START_AUFTRAGSSTATUS) | Event | — | transaktionsdaten |
| [PI_19001](/schnittstellen/202604/pruefi/ORDRSP/PI_19001) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19002](/schnittstellen/202604/pruefi/ORDRSP/PI_19002) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19003](/schnittstellen/202604/pruefi/ORDRSP/PI_19003) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19004](/schnittstellen/202604/pruefi/ORDRSP/PI_19004) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19005](/schnittstellen/202604/pruefi/ORDRSP/PI_19005) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19006](/schnittstellen/202604/pruefi/ORDRSP/PI_19006) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19007](/schnittstellen/202604/pruefi/ORDRSP/PI_19007) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19009](/schnittstellen/202604/pruefi/ORDRSP/PI_19009) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19010](/schnittstellen/202604/pruefi/ORDRSP/PI_19010) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19011](/schnittstellen/202604/pruefi/ORDRSP/PI_19011) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19012](/schnittstellen/202604/pruefi/ORDRSP/PI_19012) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19013](/schnittstellen/202604/pruefi/ORDRSP/PI_19013) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19014](/schnittstellen/202604/pruefi/ORDRSP/PI_19014) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19015](/schnittstellen/202604/pruefi/ORDRSP/PI_19015) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19016](/schnittstellen/202604/pruefi/ORDRSP/PI_19016) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19101](/schnittstellen/202604/pruefi/ORDRSP/PI_19101) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19102](/schnittstellen/202604/pruefi/ORDRSP/PI_19102) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19103](/schnittstellen/202604/pruefi/ORDRSP/PI_19103) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19104](/schnittstellen/202604/pruefi/ORDRSP/PI_19104) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19114](/schnittstellen/202604/pruefi/ORDRSP/PI_19114) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19116](/schnittstellen/202604/pruefi/ORDRSP/PI_19116) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19117](/schnittstellen/202604/pruefi/ORDRSP/PI_19117) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19118](/schnittstellen/202604/pruefi/ORDRSP/PI_19118) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19119](/schnittstellen/202604/pruefi/ORDRSP/PI_19119) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19121](/schnittstellen/202604/pruefi/ORDRSP/PI_19121) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19123](/schnittstellen/202604/pruefi/ORDRSP/PI_19123) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19124](/schnittstellen/202604/pruefi/ORDRSP/PI_19124) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19128](/schnittstellen/202604/pruefi/ORDRSP/PI_19128) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19129](/schnittstellen/202604/pruefi/ORDRSP/PI_19129) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19133](/schnittstellen/202604/pruefi/ORDRSP/PI_19133) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19301](/schnittstellen/202604/pruefi/ORDRSP/PI_19301) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19302](/schnittstellen/202604/pruefi/ORDRSP/PI_19302) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_21011](/schnittstellen/202604/pruefi/IFTSTA/PI_21011) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21025](/schnittstellen/202604/pruefi/IFTSTA/PI_21025) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21027](/schnittstellen/202604/pruefi/IFTSTA/PI_21027) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21028](/schnittstellen/202604/pruefi/IFTSTA/PI_21028) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21030](/schnittstellen/202604/pruefi/IFTSTA/PI_21030) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21031](/schnittstellen/202604/pruefi/IFTSTA/PI_21031) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21032](/schnittstellen/202604/pruefi/IFTSTA/PI_21032) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21033](/schnittstellen/202604/pruefi/IFTSTA/PI_21033) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21035](/schnittstellen/202604/pruefi/IFTSTA/PI_21035) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21039](/schnittstellen/202604/pruefi/IFTSTA/PI_21039) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21043](/schnittstellen/202604/pruefi/IFTSTA/PI_21043) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21047](/schnittstellen/202604/pruefi/IFTSTA/PI_21047) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_29001](/schnittstellen/202604/pruefi/COMDIS/PI_29001) | Prüfi | COMDIS | transaktionsdaten |
| [PI_29002](/schnittstellen/202604/pruefi/COMDIS/PI_29002) | Prüfi | COMDIS | transaktionsdaten |
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44003](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44003) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44005](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44005) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44006](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44006) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44008](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44008) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44009](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44009) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44011](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44011) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44012](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44012) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44015](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44015) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44017](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44017) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44018](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44018) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44021](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44021) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44023](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44023) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44024](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44024) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44040](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44040) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44041](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44041) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44043](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44043) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44044](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44044) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44052](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44052) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44053](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44053) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44111](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44111) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44115](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44115) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44119](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44119) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44121](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44121) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44124](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44124) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44138](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44138) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44142](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44142) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44145](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44145) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44146](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44146) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44149](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44149) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44151](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44151) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44152](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44152) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44157](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44157) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44161](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44161) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44163](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44163) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44164](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44164) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44167](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44167) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44176](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44176) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44181](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44181) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44182](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44182) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_55002](/schnittstellen/202604/pruefi/UTILMD/PI_55002) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55003](/schnittstellen/202604/pruefi/UTILMD/PI_55003) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55005](/schnittstellen/202604/pruefi/UTILMD/PI_55005) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55006](/schnittstellen/202604/pruefi/UTILMD/PI_55006) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55008](/schnittstellen/202604/pruefi/UTILMD/PI_55008) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55009](/schnittstellen/202604/pruefi/UTILMD/PI_55009) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55011](/schnittstellen/202604/pruefi/UTILMD/PI_55011) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55012](/schnittstellen/202604/pruefi/UTILMD/PI_55012) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55014](/schnittstellen/202604/pruefi/UTILMD/PI_55014) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55015](/schnittstellen/202604/pruefi/UTILMD/PI_55015) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55017](/schnittstellen/202604/pruefi/UTILMD/PI_55017) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55018](/schnittstellen/202604/pruefi/UTILMD/PI_55018) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55023](/schnittstellen/202604/pruefi/UTILMD/PI_55023) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55024](/schnittstellen/202604/pruefi/UTILMD/PI_55024) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55040](/schnittstellen/202604/pruefi/UTILMD/PI_55040) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55041](/schnittstellen/202604/pruefi/UTILMD/PI_55041) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55044](/schnittstellen/202604/pruefi/UTILMD/PI_55044) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55052](/schnittstellen/202604/pruefi/UTILMD/PI_55052) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55053](/schnittstellen/202604/pruefi/UTILMD/PI_55053) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55078](/schnittstellen/202604/pruefi/UTILMD/PI_55078) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55080](/schnittstellen/202604/pruefi/UTILMD/PI_55080) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55170](/schnittstellen/202604/pruefi/UTILMD/PI_55170) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55602](/schnittstellen/202604/pruefi/UTILMD/PI_55602) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55603](/schnittstellen/202604/pruefi/UTILMD/PI_55603) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55604](/schnittstellen/202604/pruefi/UTILMD/PI_55604) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55605](/schnittstellen/202604/pruefi/UTILMD/PI_55605) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55608](/schnittstellen/202604/pruefi/UTILMD/PI_55608) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55609](/schnittstellen/202604/pruefi/UTILMD/PI_55609) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55692](/schnittstellen/202604/pruefi/UTILMD/PI_55692) | Prüfi | UTILMD | transaktionsdaten |

### antwortstatusdritter

3 Verwendung(en) in den Nachrichtentypen UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_44003](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44003) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_55003](/schnittstellen/202604/pruefi/UTILMD/PI_55003) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55080](/schnittstellen/202604/pruefi/UTILMD/PI_55080) | Prüfi | UTILMD | transaktionsdaten |

### antwortstatusdritterBetroffeneLokation

1 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55080](/schnittstellen/202604/pruefi/UTILMD/PI_55080) | Prüfi | UTILMD | transaktionsdaten |

### antwortstatusdritterCodeliste

3 Verwendung(en) in den Nachrichtentypen UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_44003](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44003) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_55003](/schnittstellen/202604/pruefi/UTILMD/PI_55003) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55080](/schnittstellen/202604/pruefi/UTILMD/PI_55080) | Prüfi | UTILMD | transaktionsdaten |

### antwortstatusdritterReferenz

1 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55080](/schnittstellen/202604/pruefi/UTILMD/PI_55080) | Prüfi | UTILMD | transaktionsdaten |

### freitext

43 Verwendung(en) in den Nachrichtentypen ORDRSP, QUOTES, UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [[LF] START_LIEFERENDE](/schnittstellen/202604/trigger/events/LF-START_LIEFERENDE) | Event | — | transaktionsdaten |
| [[LF] START_VERSAND_ANF_STORNO](/schnittstellen/202604/trigger/events/LF-START_VERSAND_ANF_STORNO) | Event | — | transaktionsdaten |
| [[MSB] START_VERSAND_ANF_STORNO](/schnittstellen/202604/trigger/events/MSB-START_VERSAND_ANF_STORNO) | Event | — | transaktionsdaten |
| [[NB] START_LIEFERENDE](/schnittstellen/202604/trigger/events/NB-START_LIEFERENDE) | Event | — | transaktionsdaten |
| [PI_15003](/schnittstellen/202604/pruefi/QUOTES/PI_15003) | Prüfi | QUOTES | transaktionsdaten |
| [PI_19006](/schnittstellen/202604/pruefi/ORDRSP/PI_19006) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19117](/schnittstellen/202604/pruefi/ORDRSP/PI_19117) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19119](/schnittstellen/202604/pruefi/ORDRSP/PI_19119) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19121](/schnittstellen/202604/pruefi/ORDRSP/PI_19121) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19123](/schnittstellen/202604/pruefi/ORDRSP/PI_19123) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19124](/schnittstellen/202604/pruefi/ORDRSP/PI_19124) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_19133](/schnittstellen/202604/pruefi/ORDRSP/PI_19133) | Prüfi | ORDRSP | transaktionsdaten |
| [PI_44001](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44001) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44003](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44003) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44004](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44004) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44006](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44006) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44007](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44007) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44009](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44009) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44015](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44015) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44016](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44016) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44017](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44017) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44018](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44018) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44022](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44022) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44024](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44024) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44035](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44035) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_55003](/schnittstellen/202604/pruefi/UTILMD/PI_55003) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55006](/schnittstellen/202604/pruefi/UTILMD/PI_55006) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55009](/schnittstellen/202604/pruefi/UTILMD/PI_55009) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55015](/schnittstellen/202604/pruefi/UTILMD/PI_55015) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55016](/schnittstellen/202604/pruefi/UTILMD/PI_55016) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55018](/schnittstellen/202604/pruefi/UTILMD/PI_55018) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55022](/schnittstellen/202604/pruefi/UTILMD/PI_55022) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55024](/schnittstellen/202604/pruefi/UTILMD/PI_55024) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55080](/schnittstellen/202604/pruefi/UTILMD/PI_55080) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55600](/schnittstellen/202604/pruefi/UTILMD/PI_55600) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55601](/schnittstellen/202604/pruefi/UTILMD/PI_55601) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55604](/schnittstellen/202604/pruefi/UTILMD/PI_55604) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55605](/schnittstellen/202604/pruefi/UTILMD/PI_55605) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55609](/schnittstellen/202604/pruefi/UTILMD/PI_55609) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55614](/schnittstellen/202604/pruefi/UTILMD/PI_55614) | Prüfi | UTILMD | transaktionsdaten |

### infoAbweichung

1 Verwendung(en) in den Nachrichtentypen UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_44020](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44020) | Prüfi | UTILMD_GAS | transaktionsdaten |

### ergaenzteMarktlokation

1 Verwendung(en) in den Nachrichtentypen UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_44020](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44020) | Prüfi | UTILMD_GAS | transaktionsdaten |

### lokationsId

2 Verwendung(en) in den Nachrichtentypen UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [[NB] START_BERECHNUNGSFORMEL](/schnittstellen/202604/trigger/events/NB-START_BERECHNUNGSFORMEL) | Event | — | transaktionsdaten |
| [PI_25001](/schnittstellen/202604/pruefi/UTILTS/PI_25001) | Prüfi | UTILTS | transaktionsdaten |

### lokationsTyp

3 Verwendung(en).

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [[MSB] START_ERHEBUNG_MESSWERTE](/schnittstellen/202604/trigger/events/MSB-START_ERHEBUNG_MESSWERTE) | Event | — | transaktionsdaten |
| [[NB] START_BERECHNUNGSFORMEL](/schnittstellen/202604/trigger/events/NB-START_BERECHNUNGSFORMEL) | Event | — | transaktionsdaten |
| [[NB] START_ERHEBUNG_MESSWERTE](/schnittstellen/202604/trigger/events/NB-START_ERHEBUNG_MESSWERTE) | Event | — | transaktionsdaten |

### referenzMalo

1 Verwendung(en) in den Nachrichtentypen IFTSTA.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_21029](/schnittstellen/202604/pruefi/IFTSTA/PI_21029) | Prüfi | IFTSTA | transaktionsdaten |

### referenzPreisschluesselstamm

1 Verwendung(en) in den Nachrichtentypen IFTSTA.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_21029](/schnittstellen/202604/pruefi/IFTSTA/PI_21029) | Prüfi | IFTSTA | transaktionsdaten |

### datumleistungsbeginn

7 Verwendung(en) in den Nachrichtentypen UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [[MSB] START_BEGINN_MSB](/schnittstellen/202604/trigger/events/MSB-START_BEGINN_MSB) | Event | — | transaktionsdaten |
| [PI_44043](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44043) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44168](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_55042](/schnittstellen/202604/pruefi/UTILMD/PI_55042) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | transaktionsdaten |

### endezumtermin

9 Verwendung(en) in den Nachrichtentypen UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [[MSB] START_KUENDIGUNG_MSB](/schnittstellen/202604/trigger/events/MSB-START_KUENDIGUNG_MSB) | Event | — | transaktionsdaten |
| [PI_44016](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44016) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44017](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44017) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44039](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44039) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44040](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44040) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_55016](/schnittstellen/202604/pruefi/UTILMD/PI_55016) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55017](/schnittstellen/202604/pruefi/UTILMD/PI_55017) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55039](/schnittstellen/202604/pruefi/UTILMD/PI_55039) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55040](/schnittstellen/202604/pruefi/UTILMD/PI_55040) | Prüfi | UTILMD | transaktionsdaten |

### naechsteBearbeitung

3 Verwendung(en) in den Nachrichtentypen UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_44003](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44003) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_55003](/schnittstellen/202604/pruefi/UTILMD/PI_55003) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55080](/schnittstellen/202604/pruefi/UTILMD/PI_55080) | Prüfi | UTILMD | transaktionsdaten |

### lieferbeginndatuminbearbeitung

3 Verwendung(en) in den Nachrichtentypen UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_44003](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44003) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_55003](/schnittstellen/202604/pruefi/UTILMD/PI_55003) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55080](/schnittstellen/202604/pruefi/UTILMD/PI_55080) | Prüfi | UTILMD | transaktionsdaten |

### tarifstufe

1 Verwendung(en) in den Nachrichtentypen IFTSTA.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_21035](/schnittstellen/202604/pruefi/IFTSTA/PI_21035) | Prüfi | IFTSTA | transaktionsdaten |

### bilanzkreiszuordnung

2 Verwendung(en) in den Nachrichtentypen UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_44103](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44103) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44104](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44104) | Prüfi | UTILMD_GAS | transaktionsdaten |

### anwendungsreferenznummer

9 Verwendung(en) in den Nachrichtentypen PARTIN.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_37000](/schnittstellen/202604/pruefi/PARTIN/PI_37000) | Prüfi | PARTIN | transaktionsdaten |
| [PI_37001](/schnittstellen/202604/pruefi/PARTIN/PI_37001) | Prüfi | PARTIN | transaktionsdaten |
| [PI_37002](/schnittstellen/202604/pruefi/PARTIN/PI_37002) | Prüfi | PARTIN | transaktionsdaten |
| [PI_37008](/schnittstellen/202604/pruefi/PARTIN/PI_37008) | Prüfi | PARTIN | transaktionsdaten |
| [PI_37009](/schnittstellen/202604/pruefi/PARTIN/PI_37009) | Prüfi | PARTIN | transaktionsdaten |
| [PI_37010](/schnittstellen/202604/pruefi/PARTIN/PI_37010) | Prüfi | PARTIN | transaktionsdaten |
| [PI_37012](/schnittstellen/202604/pruefi/PARTIN/PI_37012) | Prüfi | PARTIN | transaktionsdaten |
| [PI_37013](/schnittstellen/202604/pruefi/PARTIN/PI_37013) | Prüfi | PARTIN | transaktionsdaten |
| [PI_37014](/schnittstellen/202604/pruefi/PARTIN/PI_37014) | Prüfi | PARTIN | transaktionsdaten |

### fertigstellungsdatum

11 Verwendung(en) in den Nachrichtentypen IFTSTA.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [[NB] START_AUFTRAGSSTATUS](/schnittstellen/202604/trigger/events/NB-START_AUFTRAGSSTATUS) | Event | — | transaktionsdaten |
| [[NB] START_WIEDERHERST_LB](/schnittstellen/202604/trigger/events/NB-START_WIEDERHERST_LB) | Event | — | transaktionsdaten |
| [PI_21010](/schnittstellen/202604/pruefi/IFTSTA/PI_21010) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21012](/schnittstellen/202604/pruefi/IFTSTA/PI_21012) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21015](/schnittstellen/202604/pruefi/IFTSTA/PI_21015) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21018](/schnittstellen/202604/pruefi/IFTSTA/PI_21018) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21024](/schnittstellen/202604/pruefi/IFTSTA/PI_21024) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21026](/schnittstellen/202604/pruefi/IFTSTA/PI_21026) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21036](/schnittstellen/202604/pruefi/IFTSTA/PI_21036) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21039](/schnittstellen/202604/pruefi/IFTSTA/PI_21039) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_21040](/schnittstellen/202604/pruefi/IFTSTA/PI_21040) | Prüfi | IFTSTA | transaktionsdaten |

### gueltigAb

55 Verwendung(en) in den Nachrichtentypen IFTSTA, UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [[LF] START_ANFRAGE_STAMMDATENAENDERUNG GAS](/schnittstellen/202604/trigger/events/LF-START_ANFRAGE_STAMMDATENAENDERUNG-GAS) | Event | — | transaktionsdaten |
| [[LF] START_BESTELLUNG_SDAE](/schnittstellen/202604/trigger/events/LF-START_BESTELLUNG_SDAE) | Event | — | transaktionsdaten |
| [[LF] START_VERSAND_SDAE](/schnittstellen/202604/trigger/events/LF-START_VERSAND_SDAE) | Event | — | transaktionsdaten |
| [[MSB] START_BESTELLUNG_SDAE GAS](/schnittstellen/202604/trigger/events/MSB-START_BESTELLUNG_SDAE-GAS) | Event | — | transaktionsdaten |
| [[MSB] START_GERAETEUEBERNAHME](/schnittstellen/202604/trigger/events/MSB-START_GERAETEUEBERNAHME) | Event | — | transaktionsdaten |
| [[MSB] START_KUENDIGUNG_MSB](/schnittstellen/202604/trigger/events/MSB-START_KUENDIGUNG_MSB) | Event | — | transaktionsdaten |
| [[MSB] START_VERSAND_SDAE](/schnittstellen/202604/trigger/events/MSB-START_VERSAND_SDAE) | Event | — | transaktionsdaten |
| [[NB] START_ANFRAGE_STAMMDATENAENDERUNG GAS](/schnittstellen/202604/trigger/events/NB-START_ANFRAGE_STAMMDATENAENDERUNG-GAS) | Event | — | transaktionsdaten |
| [[NB] START_VERSAND_BESTANDSLISTE GAS](/schnittstellen/202604/trigger/events/NB-START_VERSAND_BESTANDSLISTE-GAS) | Event | — | transaktionsdaten |
| [[NB] START_VERSAND_SDAE](/schnittstellen/202604/trigger/events/NB-START_VERSAND_SDAE) | Event | — | transaktionsdaten |
| [PI_21028](/schnittstellen/202604/pruefi/IFTSTA/PI_21028) | Prüfi | IFTSTA | transaktionsdaten |
| [PI_44018](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44018) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44019](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44019) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44020](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44020) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44041](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44041) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44101](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44101) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44102](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44102) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44103](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44103) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44104](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44104) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44109](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44109) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44112](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44112) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44113](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44113) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44116](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44116) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44117](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44117) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44120](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44120) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44123](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44123) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44137](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44137) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44138](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44138) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44139](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44139) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44140](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44140) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44142](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44142) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44143](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44143) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44145](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44145) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44147](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44147) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44148](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44148) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44149](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44149) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44150](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44150) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44151](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44151) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44156](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44156) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44157](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44157) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44159](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44159) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44160](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44160) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44162](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44162) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44163](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44163) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44165](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44165) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44166](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44166) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44167](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44167) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44175](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44175) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44176](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44176) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44180](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44180) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_44181](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44181) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_55018](/schnittstellen/202604/pruefi/UTILMD/PI_55018) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55041](/schnittstellen/202604/pruefi/UTILMD/PI_55041) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55074](/schnittstellen/202604/pruefi/UTILMD/PI_55074) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55075](/schnittstellen/202604/pruefi/UTILMD/PI_55075) | Prüfi | UTILMD | transaktionsdaten |

### gueltigkeitsZeitspanne

1 Verwendung(en) in den Nachrichtentypen IFTSTA.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_21045](/schnittstellen/202604/pruefi/IFTSTA/PI_21045) | Prüfi | IFTSTA | transaktionsdaten |

### nachrichtenReferenzBestellbestaetigung

6 Verwendung(en) in den Nachrichtentypen ORDERS, REQOTE, UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [[LF] START_VERSAND_BEST_BEEND_KONFIG](/schnittstellen/202604/trigger/events/LF-START_VERSAND_BEST_BEEND_KONFIG) | Event | — | transaktionsdaten |
| [PI_17128](/schnittstellen/202604/pruefi/ORDERS/PI_17128) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17129](/schnittstellen/202604/pruefi/ORDERS/PI_17129) | Prüfi | ORDERS | transaktionsdaten |
| [PI_35004](/schnittstellen/202604/pruefi/REQOTE/PI_35004) | Prüfi | REQOTE | transaktionsdaten |
| [PI_55553](/schnittstellen/202604/pruefi/UTILMD/PI_55553) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55555](/schnittstellen/202604/pruefi/UTILMD/PI_55555) | Prüfi | UTILMD | transaktionsdaten |

### vorgangsReferenzBestellbestaetigung

6 Verwendung(en) in den Nachrichtentypen ORDERS, REQOTE, UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [[LF] START_VERSAND_BEST_BEEND_KONFIG](/schnittstellen/202604/trigger/events/LF-START_VERSAND_BEST_BEEND_KONFIG) | Event | — | transaktionsdaten |
| [PI_17128](/schnittstellen/202604/pruefi/ORDERS/PI_17128) | Prüfi | ORDERS | transaktionsdaten |
| [PI_17129](/schnittstellen/202604/pruefi/ORDERS/PI_17129) | Prüfi | ORDERS | transaktionsdaten |
| [PI_35004](/schnittstellen/202604/pruefi/REQOTE/PI_35004) | Prüfi | REQOTE | transaktionsdaten |
| [PI_55553](/schnittstellen/202604/pruefi/UTILMD/PI_55553) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55555](/schnittstellen/202604/pruefi/UTILMD/PI_55555) | Prüfi | UTILMD | transaktionsdaten |

### datumKuendigungKd

2 Verwendung(en) in den Nachrichtentypen UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_44018](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44018) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_55018](/schnittstellen/202604/pruefi/UTILMD/PI_55018) | Prüfi | UTILMD | transaktionsdaten |

### datumKuendigungLf

2 Verwendung(en) in den Nachrichtentypen UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_44018](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44018) | Prüfi | UTILMD_GAS | transaktionsdaten |
| [PI_55018](/schnittstellen/202604/pruefi/UTILMD/PI_55018) | Prüfi | UTILMD | transaktionsdaten |

### referenzArtikelID

1 Verwendung(en) in den Nachrichtentypen IFTSTA.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_21029](/schnittstellen/202604/pruefi/IFTSTA/PI_21029) | Prüfi | IFTSTA | transaktionsdaten |

### geplantesProduktpaket

4 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55002](/schnittstellen/202604/pruefi/UTILMD/PI_55002) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55078](/schnittstellen/202604/pruefi/UTILMD/PI_55078) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55602](/schnittstellen/202604/pruefi/UTILMD/PI_55602) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55603](/schnittstellen/202604/pruefi/UTILMD/PI_55603) | Prüfi | UTILMD | transaktionsdaten |

### annahmedatum

1 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55010](/schnittstellen/202604/pruefi/UTILMD/PI_55010) | Prüfi | UTILMD | transaktionsdaten |

### geraeteausbaudatum

2 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55007](/schnittstellen/202604/pruefi/UTILMD/PI_55007) | Prüfi | UTILMD | transaktionsdaten |
| [PI_55008](/schnittstellen/202604/pruefi/UTILMD/PI_55008) | Prüfi | UTILMD | transaktionsdaten |

## Namensgleich inline definiert

### pruefidentifikator

105 Quelle(n) definieren ein Feld `pruefidentifikator` inline.

| Definiert in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [[LF] START_ABO_PROFILE](/schnittstellen/202604/trigger/events/LF-START_ABO_PROFILE) | Event | — | transaktionsdaten |
| [[LF] START_ABR_NN](/schnittstellen/202604/trigger/events/LF-START_ABR_NN) | Event | — | transaktionsdaten |
| [[LF] START_ANFORDERUNG_VON_WERTEN](/schnittstellen/202604/trigger/events/LF-START_ANFORDERUNG_VON_WERTEN) | Event | — | transaktionsdaten |
| [[LF] START_ANFRAGE_KONFIGURATION](/schnittstellen/202604/trigger/events/LF-START_ANFRAGE_KONFIGURATION) | Event | — | transaktionsdaten |
| [[LF] START_ANFRAGE_MESSWERTE](/schnittstellen/202604/trigger/events/LF-START_ANFRAGE_MESSWERTE) | Event | — | transaktionsdaten |
| [[LF] START_ANFRAGE_SPERRUNG](/schnittstellen/202604/trigger/events/LF-START_ANFRAGE_SPERRUNG) | Event | — | transaktionsdaten |
| [[LF] START_ANFRAGE_STAMMDATENAENDERUNG GAS](/schnittstellen/202604/trigger/events/LF-START_ANFRAGE_STAMMDATENAENDERUNG-GAS) | Event | — | transaktionsdaten |
| [[LF] START_ANFRAGE_STAMMDATEN_MALO](/schnittstellen/202604/trigger/events/LF-START_ANFRAGE_STAMMDATEN_MALO) | Event | — | transaktionsdaten |
| [[LF] START_ANFRAGE_STAMMDATEN_TRANCHE](/schnittstellen/202604/trigger/events/LF-START_ANFRAGE_STAMMDATEN_TRANCHE) | Event | — | transaktionsdaten |
| [[LF] START_ANF_BRENNW_ZUSTANDSZAHL](/schnittstellen/202604/trigger/events/LF-START_ANF_BRENNW_ZUSTANDSZAHL) | Event | — | transaktionsdaten |
| [[LF] START_BEENDIGUNG_RECHNUNG_MSB](/schnittstellen/202604/trigger/events/LF-START_BEENDIGUNG_RECHNUNG_MSB) | Event | — | transaktionsdaten |
| [[LF] START_BESTELLUNG_ABRECHNUNGSDATEN](/schnittstellen/202604/trigger/events/LF-START_BESTELLUNG_ABRECHNUNGSDATEN) | Event | — | transaktionsdaten |
| [[LF] START_BESTELLUNG_AEND_PROGNOSEGRUNDLAGE](/schnittstellen/202604/trigger/events/LF-START_BESTELLUNG_AEND_PROGNOSEGRUNDLAGE) | Event | — | transaktionsdaten |
| [[LF] START_BESTELLUNG_ANGEBOT_KONFIGURATION](/schnittstellen/202604/trigger/events/LF-START_BESTELLUNG_ANGEBOT_KONFIGURATION) | Event | — | transaktionsdaten |
| [[LF] START_BESTELLUNG_KONFIGURATION](/schnittstellen/202604/trigger/events/LF-START_BESTELLUNG_KONFIGURATION) | Event | — | transaktionsdaten |
| [[LF] START_BESTELLUNG_SDAE](/schnittstellen/202604/trigger/events/LF-START_BESTELLUNG_SDAE) | Event | — | transaktionsdaten |
| [[LF] START_BESTELLUNG_ZAEHLZEITDEFINITION](/schnittstellen/202604/trigger/events/LF-START_BESTELLUNG_ZAEHLZEITDEFINITION) | Event | — | transaktionsdaten |
| [[LF] START_BEST_AEND_ABR_DATEN](/schnittstellen/202604/trigger/events/LF-START_BEST_AEND_ABR_DATEN) | Event | — | transaktionsdaten |
| [[LF] START_BEST_AEND_TK](/schnittstellen/202604/trigger/events/LF-START_BEST_AEND_TK) | Event | — | transaktionsdaten |
| [[LF] START_ENTSPERRAUFTRAG](/schnittstellen/202604/trigger/events/LF-START_ENTSPERRAUFTRAG) | Event | — | transaktionsdaten |
| [[LF] START_ERHEBUNG_MESSWERTE](/schnittstellen/202604/trigger/events/LF-START_ERHEBUNG_MESSWERTE) | Event | — | transaktionsdaten |
| [[LF] START_GESCHAEFTSDATENANFRAGE](/schnittstellen/202604/trigger/events/LF-START_GESCHAEFTSDATENANFRAGE) | Event | — | transaktionsdaten |
| [[LF] START_KUENDIGUNG](/schnittstellen/202604/trigger/events/LF-START_KUENDIGUNG) | Event | — | transaktionsdaten |
| [[LF] START_LIEFERBEGINN](/schnittstellen/202604/trigger/events/LF-START_LIEFERBEGINN) | Event | — | transaktionsdaten |
| [[LF] START_LIEFERENDE](/schnittstellen/202604/trigger/events/LF-START_LIEFERENDE) | Event | — | transaktionsdaten |
| [[LF] START_MALOIDENT](/schnittstellen/202604/trigger/events/LF-START_MALOIDENT) | Event | — | transaktionsdaten |
| [[LF] START_PARTIN](/schnittstellen/202604/trigger/events/LF-START_PARTIN) | Event | — | transaktionsdaten |
| [[LF] START_REKLAMATION_VON_WERTEN](/schnittstellen/202604/trigger/events/LF-START_REKLAMATION_VON_WERTEN) | Event | — | transaktionsdaten |
| [[LF] START_SPERRAUFTRAG](/schnittstellen/202604/trigger/events/LF-START_SPERRAUFTRAG) | Event | — | transaktionsdaten |
| [[LF] START_STORNO_AUFTRAG](/schnittstellen/202604/trigger/events/LF-START_STORNO_AUFTRAG) | Event | — | transaktionsdaten |
| [[LF] START_STORNO_SE_AUFTRAG](/schnittstellen/202604/trigger/events/LF-START_STORNO_SE_AUFTRAG) | Event | — | transaktionsdaten |
| [[LF] START_UEBERMITTLUNG_ENFG](/schnittstellen/202604/trigger/events/LF-START_UEBERMITTLUNG_ENFG) | Event | — | transaktionsdaten |
| [[LF] START_UEBERM_DEFINITION](/schnittstellen/202604/trigger/events/LF-START_UEBERM_DEFINITION) | Event | — | transaktionsdaten |
| [[LF] START_UEBERSICHT_LEISTUNGSKURVENDEF](/schnittstellen/202604/trigger/events/LF-START_UEBERSICHT_LEISTUNGSKURVENDEF) | Event | — | transaktionsdaten |
| [[LF] START_UEBERSICHT_SCHALTZEITDEF](/schnittstellen/202604/trigger/events/LF-START_UEBERSICHT_SCHALTZEITDEF) | Event | — | transaktionsdaten |
| [[LF] START_UEBERSICHT_ZAEHLZEITDEF](/schnittstellen/202604/trigger/events/LF-START_UEBERSICHT_ZAEHLZEITDEF) | Event | — | transaktionsdaten |
| [[LF] START_VERSAND_ANF_STORNO](/schnittstellen/202604/trigger/events/LF-START_VERSAND_ANF_STORNO) | Event | — | transaktionsdaten |
| [[LF] START_VERSAND_ANTWORT_NNA](/schnittstellen/202604/trigger/events/LF-START_VERSAND_ANTWORT_NNA) | Event | — | transaktionsdaten |
| [[LF] START_VERSAND_BEST_BEEND_KONFIG](/schnittstellen/202604/trigger/events/LF-START_VERSAND_BEST_BEEND_KONFIG) | Event | — | transaktionsdaten |
| [[LF] START_VERSAND_SDAE](/schnittstellen/202604/trigger/events/LF-START_VERSAND_SDAE) | Event | — | transaktionsdaten |
| [[LF] START_VERSAND_STOERUNGSMELDUNG](/schnittstellen/202604/trigger/events/LF-START_VERSAND_STOERUNGSMELDUNG) | Event | — | transaktionsdaten |
| [[LF] START_VERSAND_STORNO_MSCONS](/schnittstellen/202604/trigger/events/LF-START_VERSAND_STORNO_MSCONS) | Event | — | transaktionsdaten |
| [[MSB] START_ANFORDERUNG_MESSWERTE](/schnittstellen/202604/trigger/events/MSB-START_ANFORDERUNG_MESSWERTE) | Event | — | transaktionsdaten |
| [[MSB] START_ANGEBOT_GERAETEUEBERNAHME](/schnittstellen/202604/trigger/events/MSB-START_ANGEBOT_GERAETEUEBERNAHME) | Event | — | transaktionsdaten |
| [[MSB] START_ANTWORT_GERAETEWECHSEL](/schnittstellen/202604/trigger/events/MSB-START_ANTWORT_GERAETEWECHSEL) | Event | — | transaktionsdaten |
| [[MSB] START_BEEND_RE_MSB](/schnittstellen/202604/trigger/events/MSB-START_BEEND_RE_MSB) | Event | — | transaktionsdaten |
| [[MSB] START_BEGINN_MSB](/schnittstellen/202604/trigger/events/MSB-START_BEGINN_MSB) | Event | — | transaktionsdaten |
| [[MSB] START_BESTELLUNG_GERAETEUEBERNAHME](/schnittstellen/202604/trigger/events/MSB-START_BESTELLUNG_GERAETEUEBERNAHME) | Event | — | transaktionsdaten |
| [[MSB] START_BESTELLUNG_SDAE GAS](/schnittstellen/202604/trigger/events/MSB-START_BESTELLUNG_SDAE-GAS) | Event | — | transaktionsdaten |
| [[MSB] START_ENDE_MSB](/schnittstellen/202604/trigger/events/MSB-START_ENDE_MSB) | Event | — | transaktionsdaten |
| [[MSB] START_ERHEBUNG_MESSWERTE](/schnittstellen/202604/trigger/events/MSB-START_ERHEBUNG_MESSWERTE) | Event | — | transaktionsdaten |
| [[MSB] START_GERAETEUEBERNAHME](/schnittstellen/202604/trigger/events/MSB-START_GERAETEUEBERNAHME) | Event | — | transaktionsdaten |
| [[MSB] START_GERAETEWECHSEL](/schnittstellen/202604/trigger/events/MSB-START_GERAETEWECHSEL) | Event | — | transaktionsdaten |
| [[MSB] START_GESCHAEFTSDATENANFRAGE](/schnittstellen/202604/trigger/events/MSB-START_GESCHAEFTSDATENANFRAGE) | Event | — | transaktionsdaten |
| [[MSB] START_KUENDIGUNG_MSB](/schnittstellen/202604/trigger/events/MSB-START_KUENDIGUNG_MSB) | Event | — | transaktionsdaten |
| [[MSB] START_MESSWERTUEBERMITTLUNG](/schnittstellen/202604/trigger/events/MSB-START_MESSWERTUEBERMITTLUNG) | Event | — | transaktionsdaten |
| [[MSB] START_PARTIN](/schnittstellen/202604/trigger/events/MSB-START_PARTIN) | Event | — | transaktionsdaten |
| [[MSB] START_REKLAMATION_DEFINITION](/schnittstellen/202604/trigger/events/MSB-START_REKLAMATION_DEFINITION) | Event | — | transaktionsdaten |
| [[MSB] START_VERSAND_ANF_STORNO](/schnittstellen/202604/trigger/events/MSB-START_VERSAND_ANF_STORNO) | Event | — | transaktionsdaten |
| [[MSB] START_VERSAND_BEED_WERTE](/schnittstellen/202604/trigger/events/MSB-START_VERSAND_BEED_WERTE) | Event | — | transaktionsdaten |
| [[MSB] START_VERSAND_PREISBLATT_IMS](/schnittstellen/202604/trigger/events/MSB-START_VERSAND_PREISBLATT_IMS) | Event | — | transaktionsdaten |
| [[MSB] START_VERSAND_RECHNUNG](/schnittstellen/202604/trigger/events/MSB-START_VERSAND_RECHNUNG) | Event | — | transaktionsdaten |
| [[MSB] START_VERSAND_SDAE](/schnittstellen/202604/trigger/events/MSB-START_VERSAND_SDAE) | Event | — | transaktionsdaten |
| [[MSB] START_VERSAND_STORNO_MSCONS](/schnittstellen/202604/trigger/events/MSB-START_VERSAND_STORNO_MSCONS) | Event | — | transaktionsdaten |
| [[NB] START_ABR_BK](/schnittstellen/202604/trigger/events/NB-START_ABR_BK) | Event | — | transaktionsdaten |
| [[NB] START_ABR_NN](/schnittstellen/202604/trigger/events/NB-START_ABR_NN) | Event | — | transaktionsdaten |
| [[NB] START_ANFORDERUNG_MESSWERTE](/schnittstellen/202604/trigger/events/NB-START_ANFORDERUNG_MESSWERTE) | Event | — | transaktionsdaten |
| [[NB] START_ANFRAGE_MESSWERTE_NB](/schnittstellen/202604/trigger/events/NB-START_ANFRAGE_MESSWERTE_NB) | Event | — | transaktionsdaten |
| [[NB] START_ANFRAGE_SPERRUNG](/schnittstellen/202604/trigger/events/NB-START_ANFRAGE_SPERRUNG) | Event | — | transaktionsdaten |
| [[NB] START_ANFRAGE_STAMMDATENAENDERUNG GAS](/schnittstellen/202604/trigger/events/NB-START_ANFRAGE_STAMMDATENAENDERUNG-GAS) | Event | — | transaktionsdaten |
| [[NB] START_AUFH_ZUK_ZUORDNUNG](/schnittstellen/202604/trigger/events/NB-START_AUFH_ZUK_ZUORDNUNG) | Event | — | transaktionsdaten |
| [[NB] START_AUFTRAGSSTATUS](/schnittstellen/202604/trigger/events/NB-START_AUFTRAGSSTATUS) | Event | — | transaktionsdaten |
| [[NB] START_BERECHNUNGSFORMEL](/schnittstellen/202604/trigger/events/NB-START_BERECHNUNGSFORMEL) | Event | — | transaktionsdaten |
| [[NB] START_BESTELLUNG_SDAE](/schnittstellen/202604/trigger/events/NB-START_BESTELLUNG_SDAE) | Event | — | transaktionsdaten |
| [[NB] START_BEST_AEND_TK](/schnittstellen/202604/trigger/events/NB-START_BEST_AEND_TK) | Event | — | transaktionsdaten |
| [[NB] START_EINRICHTUNG_KONFIG](/schnittstellen/202604/trigger/events/NB-START_EINRICHTUNG_KONFIG) | Event | — | transaktionsdaten |
| [[NB] START_EINRICHTUNG_KONFIGURATION_ZUORDNUNG_LF_VON_NB](/schnittstellen/202604/trigger/events/NB-START_EINRICHTUNG_KONFIGURATION_ZUORDNUNG_LF_VON_NB) | Event | — | transaktionsdaten |
| [[NB] START_ENDE_MSB_STILLLEGUNG GAS](/schnittstellen/202604/trigger/events/NB-START_ENDE_MSB_STILLLEGUNG-GAS) | Event | — | transaktionsdaten |
| [[NB] START_ENDE_ZUORDNUNG](/schnittstellen/202604/trigger/events/NB-START_ENDE_ZUORDNUNG) | Event | — | transaktionsdaten |
| [[NB] START_EOG](/schnittstellen/202604/trigger/events/NB-START_EOG) | Event | — | transaktionsdaten |
| [[NB] START_ERHEBUNG_MESSWERTE](/schnittstellen/202604/trigger/events/NB-START_ERHEBUNG_MESSWERTE) | Event | — | transaktionsdaten |
| [[NB] START_LIEFERENDE](/schnittstellen/202604/trigger/events/NB-START_LIEFERENDE) | Event | — | transaktionsdaten |
| [[NB] START_PARTIN](/schnittstellen/202604/trigger/events/NB-START_PARTIN) | Event | — | transaktionsdaten |
| [[NB] START_PREISBLATT](/schnittstellen/202604/trigger/events/NB-START_PREISBLATT) | Event | — | transaktionsdaten |
| [[NB] START_REKLAMATION_DEFINITION](/schnittstellen/202604/trigger/events/NB-START_REKLAMATION_DEFINITION) | Event | — | transaktionsdaten |
| [[NB] START_REKLAMATION_WERTE](/schnittstellen/202604/trigger/events/NB-START_REKLAMATION_WERTE) | Event | — | transaktionsdaten |
| [[NB] START_UEBERM_DEFINITION](/schnittstellen/202604/trigger/events/NB-START_UEBERM_DEFINITION) | Event | — | transaktionsdaten |
| [[NB] START_UEBERSICHT_LEISTUNGSKURVENDEF](/schnittstellen/202604/trigger/events/NB-START_UEBERSICHT_LEISTUNGSKURVENDEF) | Event | — | transaktionsdaten |
| [[NB] START_UEBERSICHT_SCHALTZEITDEF](/schnittstellen/202604/trigger/events/NB-START_UEBERSICHT_SCHALTZEITDEF) | Event | — | transaktionsdaten |
| [[NB] START_UEBERSICHT_ZAEHLZEITDEF](/schnittstellen/202604/trigger/events/NB-START_UEBERSICHT_ZAEHLZEITDEF) | Event | — | transaktionsdaten |
| [[NB] START_VERSAND_ANF_STORNO](/schnittstellen/202604/trigger/events/NB-START_VERSAND_ANF_STORNO) | Event | — | transaktionsdaten |
| [[NB] START_VERSAND_BEARB_MELDUNG](/schnittstellen/202604/trigger/events/NB-START_VERSAND_BEARB_MELDUNG) | Event | — | transaktionsdaten |
| [[NB] START_VERSAND_BEENDIGUNG_AGV](/schnittstellen/202604/trigger/events/NB-START_VERSAND_BEENDIGUNG_AGV) | Event | — | transaktionsdaten |
| [[NB] START_VERSAND_BESTANDSLISTE GAS](/schnittstellen/202604/trigger/events/NB-START_VERSAND_BESTANDSLISTE-GAS) | Event | — | transaktionsdaten |
| [[NB] START_VERSAND_COMDIS](/schnittstellen/202604/trigger/events/NB-START_VERSAND_COMDIS) | Event | — | transaktionsdaten |
| [[NB] START_VERSAND_GEMESSENE_ARB_LEIST_WERTE](/schnittstellen/202604/trigger/events/NB-START_VERSAND_GEMESSENE_ARB_LEIST_WERTE) | Event | — | transaktionsdaten |
| [[NB] START_VERSAND_LIEFERSCHEIN](/schnittstellen/202604/trigger/events/NB-START_VERSAND_LIEFERSCHEIN) | Event | — | transaktionsdaten |
| [[NB] START_VERSAND_SDAE](/schnittstellen/202604/trigger/events/NB-START_VERSAND_SDAE) | Event | — | transaktionsdaten |
| [[NB] START_VERSAND_STATUSMELDUNG](/schnittstellen/202604/trigger/events/NB-START_VERSAND_STATUSMELDUNG) | Event | — | transaktionsdaten |
| [[NB] START_VERSAND_STDA_BK_TREUE](/schnittstellen/202604/trigger/events/NB-START_VERSAND_STDA_BK_TREUE) | Event | — | transaktionsdaten |
| [[NB] START_VERSAND_STOERUNGSMELDUNG_NB](/schnittstellen/202604/trigger/events/NB-START_VERSAND_STOERUNGSMELDUNG_NB) | Event | — | transaktionsdaten |
| [[NB] START_VERSAND_STORNO_MSCONS](/schnittstellen/202604/trigger/events/NB-START_VERSAND_STORNO_MSCONS) | Event | — | transaktionsdaten |
| [[NB] START_WIEDERHERST_LB](/schnittstellen/202604/trigger/events/NB-START_WIEDERHERST_LB) | Event | — | transaktionsdaten |
| [[NB] START_WIEDERSPRUCH_ABLEHNUNG](/schnittstellen/202604/trigger/events/NB-START_WIEDERSPRUCH_ABLEHNUNG) | Event | — | transaktionsdaten |
| [[NB] START_ZUORDNUNG_ERZ_MALO_TRANCHE](/schnittstellen/202604/trigger/events/NB-START_ZUORDNUNG_ERZ_MALO_TRANCHE) | Event | — | transaktionsdaten |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

Diese Quellen schreiben ein Feld gleichen Namens **selbst aus**, statt das BO4E-Feldatom zu referenzieren. Der `$ref`-Graph oben sieht diese Stellen nicht, und sie sind auch keine Verwendung des Feldatoms — deshalb stehen sie hier getrennt und werden nirgends zu den Verwendungen addiert.

</Hinweisbereich>
