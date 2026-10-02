# Rechnung
<span hidden data-pagefind-meta={"title:Rechnung — BO4E-Geschäftsobjekt (FV 202610)"} />

BO4E-Geschäftsobjekt · 30 Felder · 99 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="botyp"></a>`boTyp` <span className="hbs-pflicht">\*</span> | [Enum BOTyp](/bo4e/202610/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> | Typ des BO |
| <a id="versionstruktur"></a>`versionStruktur` <span className="hbs-pflicht">\*</span> | string | versionStruktur |
| <a id="istselbstausgestellt"></a>`istSelbstausgestellt` | boolean | Kennzeichen, ob es sich um eine selbstausgestellte Rechnung handelt |
| <a id="bearbeitungsdatum"></a>`bearbeitungsdatum` | string (date-time) | bearbeitungsdatum |
| <a id="rechnungsdatum"></a>`rechnungsdatum` | string (date-time) | Ausstellungsdatum der Rechnung. |
| <a id="faelligkeitsdatum"></a>`faelligkeitsdatum` | string (date-time) | Zu diesem Datum ist die Zahlung fällig. |
| <a id="rechnungsstatus"></a>`rechnungsstatus` | [Enum Rechnungsstatus](/bo4e/202610/enum/Rechnungsstatus)<br/><Werte>`DUPLIKAT`, `ORIGINAL`, `STORNIERT`</Werte> | Status der Rechnung zur Kennzeichnung des Bearbeitungsstandes. Details siehe ENUM Rechnungsstatus |
| <a id="vorlaeufigerabrechnungszeitraum"></a>`vorlaeufigerAbrechnungszeitraum` | [Zeitraum](/bo4e/202610/com/Zeitraum) | — |
| <a id="rechnungsperiode"></a>`rechnungsperiode` | [Zeitraum](/bo4e/202610/com/Zeitraum) | Der Zeitraum der zugrunde liegenden Lieferung zur Rechnung. In der COM Zeitraum können diese angegeben werden. |
| <a id="rechnungstyp"></a>`rechnungstyp` | [Enum Rechnungstyp](/bo4e/202610/enum/Rechnungstyp)<br/><Werte>`ABSCHLUSSRECHNUNG`, `ABSCHLAGSRECHNUNG`, `TURNUSRECHNUNG`, `MONATSRECHNUNG`, `WIMRECHNUNG`, `ZWISCHENRECHNUNG`, `INTEGRIERTE_13TE_RECHNUNG`, `ZUSAETZLICHE_13TE_RECHNUNG`, `MEHRMINDERMENGENRECHNUNG`, `MSBRECHNUNG`, `KAPAZITAETSRECHNUNG`, `SPERRUNG_INBETRIEBNAHME`, `VERZUGSKOSTEN`, `BLINDARBEIT`, `SONDERRECHNUNG`, `ABRECHNUNG_VON_KONFIGURATIONEN_UNIVERSALBESTELLPROZESS`, `ABRECHNUNG_VON_TECHNIK`</Werte> | Ein kontextbezogender Rechnungstyp, z.B. Netznutzungsrechnung. Details siehe ENUM Rechnungstyp |
| <a id="istreversecharge"></a>`istReverseCharge` | boolean | Kennzeichen, ob bei der Rechnung das Reverse Charge verfahren angewendet wird |
| <a id="gesamtbrutto"></a>`gesamtbrutto` | [Betrag](/bo4e/202610/com/Betrag) | Die Summe aus Netto- und Steuerbetrag. Details Betrag |
| <a id="zuzahlen"></a>`zuZahlen` | [Betrag](/bo4e/202610/com/Betrag) | — |
| <a id="originalrechnungsnummer"></a>`originalRechnungsnummer` | string | Im Falle einer Stornorechnung (storno = true) steht hier die Rechnungsnummer der stornierten Rechnung. |
| <a id="referenznachrichtendatum"></a>`referenzNachrichtendatum` | string | referenzNachrichtendatum |
| <a id="referenzdokumentennummer"></a>`referenzDokumentennummer` | string | referenzDokumentennummer |
| <a id="referenzvorgaengerrechnung"></a>`referenzVorgaengerrechnung` | string | referenzVorgaengerrechnung |
| <a id="datumvorgaengerrechnung"></a>`datumVorgaengerrechnung` | string (date-time) | datumVorgaengerrechnung |
| <a id="preisnetzbetreibercodenummer"></a>`preisNetzbetreiberCodenummer` | string | preisNetzbetreiberCodenummer |
| <a id="netzkonto"></a>`netzkonto` | string | netzkonto |
| <a id="vorausgezahlt"></a>`vorausgezahlt` | [Betrag](/bo4e/202610/com/Betrag) | Die Summe evtl. vorausgezahlter Beträge, z.B. Abschläge. Angabe als Bruttowert. Details Betrag |
| <a id="gemeinderabatt"></a>`gemeinderabatt` | [Gemeinderabatt](/bo4e/202610/com/Gemeinderabatt) | — |
| <a id="ausfuehrungsdatum"></a>`ausfuehrungsdatum` | string (date-time) | Das Datum an dem die Leistung erbracht wurde. |
| <a id="sonderrechnungsart"></a>`sonderrechnungsart` | [Enum SonderrechnungsArt](/bo4e/202610/enum/SonderrechnungsArt)<br/><Werte>`KONZESSIONSABGABE_TESTAT`, `INDIVIDUELL_ATYPISCH`, `INDIVIDUELL_SINGULAER`, `KWKG_UMLAGE`, `OFFSHORE_UMLAGE`, `P19_STROM_NEV_UMLAGE`, `P18_ABLAV`, `KONZESSIONSABGABE_WECHSEL_RLM`, `PRIVILEGIERUNG_NACH_ENFG`, `KONZESSIONSABGABE_WEITERGELEITETE_MENGEN`</Werte> | Sonderrechnungsart |
| <a id="sonderrechnungsarten"></a>`sonderrechnungsarten` | [Enum SonderrechnungsArt[]](/bo4e/202610/enum/SonderrechnungsArt)<br/><Werte>`KONZESSIONSABGABE_TESTAT`, `INDIVIDUELL_ATYPISCH`, `INDIVIDUELL_SINGULAER`, `KWKG_UMLAGE`, `OFFSHORE_UMLAGE`, `P19_STROM_NEV_UMLAGE`, `P18_ABLAV`, `KONZESSIONSABGABE_WECHSEL_RLM`, `PRIVILEGIERUNG_NACH_ENFG`, `KONZESSIONSABGABE_WEITERGELEITETE_MENGEN`</Werte> | Sonderrechnungsart |
| <a id="energierichtung"></a>`energierichtung` | [Enum Energierichtung](/bo4e/202610/enum/Energierichtung)<br/><Werte>`AUSSP`, `EINSP`</Werte> | Spezifiziert die Energierichtung einer Markt- und/oder Messlokation |
| <a id="beginnperiodebilanzierung"></a>`beginnPeriodeBilanzierung` | string (date-time) | beginnPeriodeBilanzierung |
| <a id="endeperiodenetznutzung"></a>`endePeriodeNetznutzung` | string (date-time) | endePeriodeNetznutzung |
| <a id="steuerbetraege"></a>`steuerbetraege` | [Steuerbetrag[]](/bo4e/202610/com/Steuerbetrag) | Eine Liste mit Steuerbeträgen pro Steuerkennzeichen/Steuersatz. Die Summe dieser Beträge ergibt den Wert für gesamtsteuer. Details Steuerbetrag |
| <a id="rechnungspositionen"></a>`rechnungspositionen` | [Rechnungsposition[]](/bo4e/202610/com/Rechnungsposition) | Die Rechnungspositionen. Details siehe Rechnungsposition |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[boTyp](/bo4e/202610/bo/Rechnung#botyp) <span className="hbs-pflicht">\*</span></span> | Typ des BO | [Enum BOTyp](/bo4e/202610/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> |
| <span className="hbs-f hbs-e0">[versionStruktur](/bo4e/202610/bo/Rechnung#versionstruktur) <span className="hbs-pflicht">\*</span></span> | versionStruktur | string |
| <span className="hbs-f hbs-e0">[istSelbstausgestellt](/bo4e/202610/bo/Rechnung#istselbstausgestellt)</span> | Kennzeichen, ob es sich um eine selbstausgestellte Rechnung handelt | boolean |
| <span className="hbs-f hbs-e0">[bearbeitungsdatum](/bo4e/202610/bo/Rechnung#bearbeitungsdatum)</span> | bearbeitungsdatum | string (date-time) |
| <span className="hbs-f hbs-e0">[rechnungsdatum](/bo4e/202610/bo/Rechnung#rechnungsdatum)</span> | Ausstellungsdatum der Rechnung. | string (date-time) |
| <span className="hbs-f hbs-e0">[faelligkeitsdatum](/bo4e/202610/bo/Rechnung#faelligkeitsdatum)</span> | Zu diesem Datum ist die Zahlung fällig. | string (date-time) |
| <span className="hbs-f hbs-e0">[rechnungsstatus](/bo4e/202610/bo/Rechnung#rechnungsstatus)</span> | Status der Rechnung zur Kennzeichnung des Bearbeitungsstandes. Details siehe ENUM Rechnungsstatus | [Enum Rechnungsstatus](/bo4e/202610/enum/Rechnungsstatus)<br/><Werte>`DUPLIKAT`, `ORIGINAL`, `STORNIERT`</Werte> |
| <span className="hbs-g hbs-e0">[vorlaeufigerAbrechnungszeitraum](/bo4e/202610/bo/Rechnung#vorlaeufigerabrechnungszeitraum)</span> | — | [Zeitraum](/bo4e/202610/com/Zeitraum) |
| <span className="hbs-f hbs-e1">[zeiteinheit](/bo4e/202610/com/Zeitraum#zeiteinheit)</span> | Zeiteinheit | [Enum Zeiteinheit](/bo4e/202610/enum/Zeiteinheit)<br/><Werte>`SEKUNDE`, `MINUTE`, `STUNDE`, `VIERTEL_STUNDE`, `TAG`, `WOCHE`, `MONAT`, `QUARTAL`, `HALBJAHR`, `JAHR`</Werte> |
| <span className="hbs-f hbs-e1">[dauer](/bo4e/202610/com/Zeitraum#dauer)</span> | dauer | integer |
| <span className="hbs-f hbs-e1">[startdatum](/bo4e/202610/com/Zeitraum#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e1">[enddatum](/bo4e/202610/com/Zeitraum#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-f hbs-e1">[einheit](/bo4e/202610/com/Zeitraum#einheit)</span> | Zeiteinheit | [Enum Zeiteinheit](/bo4e/202610/enum/Zeiteinheit)<br/><Werte>`SEKUNDE`, `MINUTE`, `STUNDE`, `VIERTEL_STUNDE`, `TAG`, `WOCHE`, `MONAT`, `QUARTAL`, `HALBJAHR`, `JAHR`</Werte> |
| <span className="hbs-f hbs-e1">[ableseZeitraum](/bo4e/202610/com/Zeitraum#ablesezeitraum)</span> | ableseZeitraum | string |
| <span className="hbs-f hbs-e1">[abrechnungsZeitraum](/bo4e/202610/com/Zeitraum#abrechnungszeitraum)</span> | abrechnungsZeitraum | string |
| <span className="hbs-f hbs-e1">[zeitraumText](/bo4e/202610/com/Zeitraum#zeitraumtext)</span> | zeitraumText | string |
| <span className="hbs-f hbs-e1">[zeitraumId](/bo4e/202610/com/Zeitraum#zeitraumid)</span> | zeitraumId | integer |
| <span className="hbs-g hbs-e0">[rechnungsperiode](/bo4e/202610/bo/Rechnung#rechnungsperiode)</span> | Der Zeitraum der zugrunde liegenden Lieferung zur Rechnung. In der COM Zeitraum können diese angegeben werden. | [Zeitraum](/bo4e/202610/com/Zeitraum) |
| <span className="hbs-f hbs-e1">[zeiteinheit](/bo4e/202610/com/Zeitraum#zeiteinheit)</span> | Zeiteinheit | [Enum Zeiteinheit](/bo4e/202610/enum/Zeiteinheit)<br/><Werte>`SEKUNDE`, `MINUTE`, `STUNDE`, `VIERTEL_STUNDE`, `TAG`, `WOCHE`, `MONAT`, `QUARTAL`, `HALBJAHR`, `JAHR`</Werte> |
| <span className="hbs-f hbs-e1">[dauer](/bo4e/202610/com/Zeitraum#dauer)</span> | dauer | integer |
| <span className="hbs-f hbs-e1">[startdatum](/bo4e/202610/com/Zeitraum#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e1">[enddatum](/bo4e/202610/com/Zeitraum#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-f hbs-e1">[einheit](/bo4e/202610/com/Zeitraum#einheit)</span> | Zeiteinheit | [Enum Zeiteinheit](/bo4e/202610/enum/Zeiteinheit)<br/><Werte>`SEKUNDE`, `MINUTE`, `STUNDE`, `VIERTEL_STUNDE`, `TAG`, `WOCHE`, `MONAT`, `QUARTAL`, `HALBJAHR`, `JAHR`</Werte> |
| <span className="hbs-f hbs-e1">[ableseZeitraum](/bo4e/202610/com/Zeitraum#ablesezeitraum)</span> | ableseZeitraum | string |
| <span className="hbs-f hbs-e1">[abrechnungsZeitraum](/bo4e/202610/com/Zeitraum#abrechnungszeitraum)</span> | abrechnungsZeitraum | string |
| <span className="hbs-f hbs-e1">[zeitraumText](/bo4e/202610/com/Zeitraum#zeitraumtext)</span> | zeitraumText | string |
| <span className="hbs-f hbs-e1">[zeitraumId](/bo4e/202610/com/Zeitraum#zeitraumid)</span> | zeitraumId | integer |
| <span className="hbs-f hbs-e0">[rechnungstyp](/bo4e/202610/bo/Rechnung#rechnungstyp)</span> | Ein kontextbezogender Rechnungstyp, z.B. Netznutzungsrechnung. Details siehe ENUM Rechnungstyp | [Enum Rechnungstyp](/bo4e/202610/enum/Rechnungstyp)<br/><Werte>`ABSCHLUSSRECHNUNG`, `ABSCHLAGSRECHNUNG`, `TURNUSRECHNUNG`, `MONATSRECHNUNG`, `WIMRECHNUNG`, `ZWISCHENRECHNUNG`, `INTEGRIERTE_13TE_RECHNUNG`, `ZUSAETZLICHE_13TE_RECHNUNG`, `MEHRMINDERMENGENRECHNUNG`, `MSBRECHNUNG`, `KAPAZITAETSRECHNUNG`, `SPERRUNG_INBETRIEBNAHME`, `VERZUGSKOSTEN`, `BLINDARBEIT`, `SONDERRECHNUNG`, `ABRECHNUNG_VON_KONFIGURATIONEN_UNIVERSALBESTELLPROZESS`, `ABRECHNUNG_VON_TECHNIK`</Werte> |
| <span className="hbs-f hbs-e0">[istReverseCharge](/bo4e/202610/bo/Rechnung#istreversecharge)</span> | Kennzeichen, ob bei der Rechnung das Reverse Charge verfahren angewendet wird | boolean |
| <span className="hbs-g hbs-e0">[gesamtbrutto](/bo4e/202610/bo/Rechnung#gesamtbrutto)</span> | Die Summe aus Netto- und Steuerbetrag. Details Betrag | [Betrag](/bo4e/202610/com/Betrag) |
| <span className="hbs-f hbs-e1">[wert](/bo4e/202610/com/Betrag#wert)</span> | Gibt den Betrag des Preises an. | number (float) |
| <span className="hbs-f hbs-e1">[waehrung](/bo4e/202610/com/Betrag#waehrung)</span> | Währung des Preises | string |
| <span className="hbs-g hbs-e0">[zuZahlen](/bo4e/202610/bo/Rechnung#zuzahlen)</span> | — | [Betrag](/bo4e/202610/com/Betrag) |
| <span className="hbs-f hbs-e1">[wert](/bo4e/202610/com/Betrag#wert)</span> | Gibt den Betrag des Preises an. | number (float) |
| <span className="hbs-f hbs-e1">[waehrung](/bo4e/202610/com/Betrag#waehrung)</span> | Währung des Preises | string |
| <span className="hbs-f hbs-e0">[originalRechnungsnummer](/bo4e/202610/bo/Rechnung#originalrechnungsnummer)</span> | Im Falle einer Stornorechnung (storno = true) steht hier die Rechnungsnummer der stornierten Rechnung. | string |
| <span className="hbs-f hbs-e0">[referenzNachrichtendatum](/bo4e/202610/bo/Rechnung#referenznachrichtendatum)</span> | referenzNachrichtendatum | string |
| <span className="hbs-f hbs-e0">[referenzDokumentennummer](/bo4e/202610/bo/Rechnung#referenzdokumentennummer)</span> | referenzDokumentennummer | string |
| <span className="hbs-f hbs-e0">[referenzVorgaengerrechnung](/bo4e/202610/bo/Rechnung#referenzvorgaengerrechnung)</span> | referenzVorgaengerrechnung | string |
| <span className="hbs-f hbs-e0">[datumVorgaengerrechnung](/bo4e/202610/bo/Rechnung#datumvorgaengerrechnung)</span> | datumVorgaengerrechnung | string (date-time) |
| <span className="hbs-f hbs-e0">[preisNetzbetreiberCodenummer](/bo4e/202610/bo/Rechnung#preisnetzbetreibercodenummer)</span> | preisNetzbetreiberCodenummer | string |
| <span className="hbs-f hbs-e0">[netzkonto](/bo4e/202610/bo/Rechnung#netzkonto)</span> | netzkonto | string |
| <span className="hbs-g hbs-e0">[vorausgezahlt](/bo4e/202610/bo/Rechnung#vorausgezahlt)</span> | Die Summe evtl. vorausgezahlter Beträge, z.B. Abschläge. Angabe als Bruttowert. Details Betrag | [Betrag](/bo4e/202610/com/Betrag) |
| <span className="hbs-f hbs-e1">[wert](/bo4e/202610/com/Betrag#wert)</span> | Gibt den Betrag des Preises an. | number (float) |
| <span className="hbs-f hbs-e1">[waehrung](/bo4e/202610/com/Betrag#waehrung)</span> | Währung des Preises | string |
| <span className="hbs-g hbs-e0">[gemeinderabatt](/bo4e/202610/bo/Rechnung#gemeinderabatt)</span> | — | [Gemeinderabatt](/bo4e/202610/com/Gemeinderabatt) |
| <span className="hbs-f hbs-e1">[wert](/bo4e/202610/com/Gemeinderabatt#wert)</span> | Wert | number (float) |
| <span className="hbs-f hbs-e1">[einheit](/bo4e/202610/com/Gemeinderabatt#einheit)</span> | Einheit | string |
| <span className="hbs-f hbs-e1">[typ](/bo4e/202610/com/Gemeinderabatt#typ)</span> | Typ | string |
| <span className="hbs-f hbs-e1">[bemessungsgrundlage](/bo4e/202610/com/Gemeinderabatt#bemessungsgrundlage)</span> | Bemessungsgrundlage | number (float) |
| <span className="hbs-f hbs-e0">[ausfuehrungsdatum](/bo4e/202610/bo/Rechnung#ausfuehrungsdatum)</span> | Das Datum an dem die Leistung erbracht wurde. | string (date-time) |
| <span className="hbs-f hbs-e0">[sonderrechnungsart](/bo4e/202610/bo/Rechnung#sonderrechnungsart)</span> | Sonderrechnungsart | [Enum SonderrechnungsArt](/bo4e/202610/enum/SonderrechnungsArt)<br/><Werte>`KONZESSIONSABGABE_TESTAT`, `INDIVIDUELL_ATYPISCH`, `INDIVIDUELL_SINGULAER`, `KWKG_UMLAGE`, `OFFSHORE_UMLAGE`, `P19_STROM_NEV_UMLAGE`, `P18_ABLAV`, `KONZESSIONSABGABE_WECHSEL_RLM`, `PRIVILEGIERUNG_NACH_ENFG`, `KONZESSIONSABGABE_WEITERGELEITETE_MENGEN`</Werte> |
| <span className="hbs-f hbs-e0">[sonderrechnungsarten](/bo4e/202610/bo/Rechnung#sonderrechnungsarten) <span className="hbs-liste">[ ]</span></span> | Sonderrechnungsart | [Enum SonderrechnungsArt[]](/bo4e/202610/enum/SonderrechnungsArt)<br/><Werte>`KONZESSIONSABGABE_TESTAT`, `INDIVIDUELL_ATYPISCH`, `INDIVIDUELL_SINGULAER`, `KWKG_UMLAGE`, `OFFSHORE_UMLAGE`, `P19_STROM_NEV_UMLAGE`, `P18_ABLAV`, `KONZESSIONSABGABE_WECHSEL_RLM`, `PRIVILEGIERUNG_NACH_ENFG`, `KONZESSIONSABGABE_WEITERGELEITETE_MENGEN`</Werte> |
| <span className="hbs-f hbs-e0">[energierichtung](/bo4e/202610/bo/Rechnung#energierichtung)</span> | Spezifiziert die Energierichtung einer Markt- und/oder Messlokation | [Enum Energierichtung](/bo4e/202610/enum/Energierichtung)<br/><Werte>`AUSSP`, `EINSP`</Werte> |
| <span className="hbs-f hbs-e0">[beginnPeriodeBilanzierung](/bo4e/202610/bo/Rechnung#beginnperiodebilanzierung)</span> | beginnPeriodeBilanzierung | string (date-time) |
| <span className="hbs-f hbs-e0">[endePeriodeNetznutzung](/bo4e/202610/bo/Rechnung#endeperiodenetznutzung)</span> | endePeriodeNetznutzung | string (date-time) |
| <span className="hbs-g hbs-e0">[steuerbetraege](/bo4e/202610/bo/Rechnung#steuerbetraege) <span className="hbs-liste">[ ]</span></span> | Eine Liste mit Steuerbeträgen pro Steuerkennzeichen/Steuersatz. Die Summe dieser Beträge ergibt den Wert für<br/>gesamtsteuer. Details Steuerbetrag | [Steuerbetrag[]](/bo4e/202610/com/Steuerbetrag) |
| <span className="hbs-f hbs-e1">[steuerkennzeichen](/bo4e/202610/com/Steuerbetrag#steuerkennzeichen)</span> | Kennzeichnung des Steuersatzes, bzw. Verfahrens. Details Steuerkennzeichen | string |
| <span className="hbs-f hbs-e1">[basiswert](/bo4e/202610/com/Steuerbetrag#basiswert)</span> | Nettobetrag für den die Steuer berechnet wurde. Z.B. 200 | number (float) |
| <span className="hbs-f hbs-e1">[steuerwert](/bo4e/202610/com/Steuerbetrag#steuerwert)</span> | Aus dem Basiswert berechnete Steuer. Z.B. 38 (bei UST_19), falls Basiswert 200 ist. | number (float) |
| <span className="hbs-f hbs-e1">[waehrung](/bo4e/202610/com/Steuerbetrag#waehrung)</span> | Währung. Z.B. Euro. | string |
| <span className="hbs-f hbs-e1">[basiswertVorausbezahlt](/bo4e/202610/com/Steuerbetrag#basiswertvorausbezahlt)</span> | basiswertVorausbezahlt | number (float) |
| <span className="hbs-f hbs-e1">[steuerwertVorausbezahlt](/bo4e/202610/com/Steuerbetrag#steuerwertvorausbezahlt)</span> | steuerwertVorausbezahlt | number (float) |
| <span className="hbs-g hbs-e0">[rechnungspositionen](/bo4e/202610/bo/Rechnung#rechnungspositionen) <span className="hbs-liste">[ ]</span></span> | Die Rechnungspositionen. Details siehe Rechnungsposition | [Rechnungsposition[]](/bo4e/202610/com/Rechnungsposition) |
| <span className="hbs-g hbs-e1">[einzelpreis](/bo4e/202610/com/Rechnungsposition#einzelpreis)</span> | Der Preis für eine Einheit der energetischen Menge. Details Preis | [Preis](/bo4e/202610/com/Preis) |
| <span className="hbs-f hbs-e2">[wert](/bo4e/202610/com/Preis#wert)</span> | wert | number (float) |
| <span className="hbs-f hbs-e2">[menge](/bo4e/202610/com/Preis#menge)</span> | menge | integer |
| <span className="hbs-f hbs-e2">[minimaleMenge](/bo4e/202610/com/Preis#minimalemenge)</span> | minimale Menge | integer |
| <span className="hbs-f hbs-e2">[maximaleMenge](/bo4e/202610/com/Preis#maximalemenge)</span> | maximale Menge | integer |
| <span className="hbs-f hbs-e2">[einheit](/bo4e/202610/com/Preis#einheit)</span> | Waehrungseinheit | [Enum Waehrungseinheit](/bo4e/202610/enum/Waehrungseinheit)<br/><Werte>`EUR`, `CT`</Werte> |
| <span className="hbs-f hbs-e2">[bezugswert](/bo4e/202610/com/Preis#bezugswert)</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202610/enum/Mengeneinheit)<br/><Werte>`W`, `WH`, `KW`, `KWH`, `KVARH`, `MW`, `MWH`, `STUECK`, `KUBIKMETER`, `STUNDE`, `TAG`, `MONAT`, `JAHR`, `PROZENT`, `ANZAHL`, `VAR`, `KVAR`, `VARH`, `KWHK`, `Z16`, `KWT`, `WATT_PRO_QUADRATMETER`, `METER_PRO_SEKUNDE`</Werte> |
| <span className="hbs-f hbs-e2">[status](/bo4e/202610/com/Preis#status)</span> | Preisstatus | [Enum Preisstatus](/bo4e/202610/enum/Preisstatus)<br/><Werte>`VORLAEUFIG`, `ENDGUELTIG`</Werte> |
| <span className="hbs-f hbs-e2">[preisart](/bo4e/202610/com/Preis#preisart)</span> | Preisart Code | [Enum Preisart](/bo4e/202610/enum/Preisart)<br/><Werte>`EINRICHTUNGSPREIS`, `TRANSAKTIONSPREIS`, `BETRIEBSPREIS`</Werte> |
| <span className="hbs-f hbs-e1">[lieferungBis](/bo4e/202610/com/Rechnungsposition#lieferungbis)</span> | Ende der Lieferung für die abgerechnete Leistung. | string (date-time) |
| <span className="hbs-f hbs-e1">[lieferungVon](/bo4e/202610/com/Rechnungsposition#lieferungvon)</span> | Start der Lieferung für die abgerechnete Leistung. | string (date-time) |
| <span className="hbs-g hbs-e1">[positionsMenge](/bo4e/202610/com/Rechnungsposition#positionsmenge)</span> | Die abgerechnete Menge mit Einheit. Z.B. 4372 kWh. Details Menge | [Menge](/bo4e/202610/com/Menge) |
| <span className="hbs-f hbs-e2">[wert](/bo4e/202610/com/Menge#wert)</span> | Wert | number (float) |
| <span className="hbs-f hbs-e2">[einheit](/bo4e/202610/com/Menge#einheit)</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202610/enum/Mengeneinheit)<br/><Werte>`W`, `WH`, `KW`, `KWH`, `KVARH`, `MW`, `MWH`, `STUECK`, `KUBIKMETER`, `STUNDE`, `TAG`, `MONAT`, `JAHR`, `PROZENT`, `ANZAHL`, `VAR`, `KVAR`, `VARH`, `KWHK`, `Z16`, `KWT`, `WATT_PRO_QUADRATMETER`, `METER_PRO_SEKUNDE`</Werte> |
| <span className="hbs-f hbs-e2">[startdatum](/bo4e/202610/com/Menge#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e2">[enddatum](/bo4e/202610/com/Menge#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-f hbs-e1">[positionsnummer](/bo4e/202610/com/Rechnungsposition#positionsnummer)</span> | Fortlaufende Nummer für die Rechnungsposition. | integer |
| <span className="hbs-f hbs-e1">[artikelnummer](/bo4e/202610/com/Rechnungsposition#artikelnummer)</span> | Kennzeichnung der Rechnungsposition mit der Standard-Artikelnummer des BDEW. Details<br/>BDEWArtikelnummer | string |
| <span className="hbs-g hbs-e1">[teilsummeNetto](/bo4e/202610/com/Rechnungsposition#teilsummenetto)</span> | Das Ergebnis der Multiplikation aus einzelpreis * positionsMenge * (Faktor aus zeitbezogeneMenge). Z.B. 12,60€<br/>* 120 kW * 3/12 (für 3 Monate). Details Betrag | [Betrag](/bo4e/202610/com/Betrag) |
| <span className="hbs-f hbs-e2">[wert](/bo4e/202610/com/Betrag#wert)</span> | Gibt den Betrag des Preises an. | number (float) |
| <span className="hbs-f hbs-e2">[waehrung](/bo4e/202610/com/Betrag#waehrung)</span> | Währung des Preises | string |
| <span className="hbs-g hbs-e1">[teilsummeSteuer](/bo4e/202610/com/Rechnungsposition#teilsummesteuer)</span> | Auf die Position entfallende Steuer, bestehend aus Steuersatz und Betrag. Details Steuerbetrag | [Steuerbetrag](/bo4e/202610/com/Steuerbetrag) |
| <span className="hbs-f hbs-e2">[steuerkennzeichen](/bo4e/202610/com/Steuerbetrag#steuerkennzeichen)</span> | Kennzeichnung des Steuersatzes, bzw. Verfahrens. Details Steuerkennzeichen | string |
| <span className="hbs-f hbs-e2">[basiswert](/bo4e/202610/com/Steuerbetrag#basiswert)</span> | Nettobetrag für den die Steuer berechnet wurde. Z.B. 200 | number (float) |
| <span className="hbs-f hbs-e2">[steuerwert](/bo4e/202610/com/Steuerbetrag#steuerwert)</span> | Aus dem Basiswert berechnete Steuer. Z.B. 38 (bei UST_19), falls Basiswert 200 ist. | number (float) |
| <span className="hbs-f hbs-e2">[waehrung](/bo4e/202610/com/Steuerbetrag#waehrung)</span> | Währung. Z.B. Euro. | string |
| <span className="hbs-f hbs-e2">[basiswertVorausbezahlt](/bo4e/202610/com/Steuerbetrag#basiswertvorausbezahlt)</span> | basiswertVorausbezahlt | number (float) |
| <span className="hbs-f hbs-e2">[steuerwertVorausbezahlt](/bo4e/202610/com/Steuerbetrag#steuerwertvorausbezahlt)</span> | steuerwertVorausbezahlt | number (float) |
| <span className="hbs-g hbs-e1">[zeitbezogeneMenge](/bo4e/202610/com/Rechnungsposition#zeitbezogenemenge)</span> | Eine auf die Zeiteinheit bezogene Untermenge. Z.B. bei einem Jahrespreis, 3 Monate oder 146 Tage. Basierend<br/>darauf wird der Preis aufgeteilt. Details Menge | [Menge](/bo4e/202610/com/Menge) |
| <span className="hbs-f hbs-e2">[wert](/bo4e/202610/com/Menge#wert)</span> | Wert | number (float) |
| <span className="hbs-f hbs-e2">[einheit](/bo4e/202610/com/Menge#einheit)</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202610/enum/Mengeneinheit)<br/><Werte>`W`, `WH`, `KW`, `KWH`, `KVARH`, `MW`, `MWH`, `STUECK`, `KUBIKMETER`, `STUNDE`, `TAG`, `MONAT`, `JAHR`, `PROZENT`, `ANZAHL`, `VAR`, `KVAR`, `VARH`, `KWHK`, `Z16`, `KWT`, `WATT_PRO_QUADRATMETER`, `METER_PRO_SEKUNDE`</Werte> |
| <span className="hbs-f hbs-e2">[startdatum](/bo4e/202610/com/Menge#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e2">[enddatum](/bo4e/202610/com/Menge#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-g hbs-e1">[abschlag](/bo4e/202610/com/Rechnungsposition#abschlag)</span> | — | [Abschlag](/bo4e/202610/com/Abschlag) |
| <span className="hbs-f hbs-e2">[typ](/bo4e/202610/com/Abschlag#typ)</span> | AbschlagTyp | [Enum AbschlagTyp](/bo4e/202610/enum/AbschlagTyp)<br/><Werte>`GEMEINDERABATT_KAV`, `ANPASSUNG_P19_STROM_NEV`</Werte> |
| <span className="hbs-f hbs-e2">[prozent](/bo4e/202610/com/Abschlag#prozent)</span> | Prozentuale Angabe zum Auf-/Abschlag | number (float) |
| <span className="hbs-g hbs-e1">[zuschlag](/bo4e/202610/com/Rechnungsposition#zuschlag)</span> | — | [Zuschlag](/bo4e/202610/com/Zuschlag) |
| <span className="hbs-f hbs-e2">[typ](/bo4e/202610/com/Zuschlag#typ)</span> | ZuschlagTyp | [Enum ZuschlagTyp](/bo4e/202610/enum/ZuschlagTyp)<br/><Werte>`UMSPANNUNGSZUSCHLAG`, `BETRIEBSMITTEL_P19_STROM_NEV`, `ANPASSUNG_P19_STROM_NEV`, `ANPASSUNG_PAUSCHALE_NETZENTGELTREDUZIERUNG_NACH_P14A_ENWG_AUF_HOEHE_DER_NNE`</Werte> |
| <span className="hbs-f hbs-e2">[prozent](/bo4e/202610/com/Zuschlag#prozent)</span> | prozent | number (float) |
| <span className="hbs-g hbs-e1">[gemeinderabatt](/bo4e/202610/com/Rechnungsposition#gemeinderabatt)</span> | — | [Gemeinderabatt](/bo4e/202610/com/Gemeinderabatt) |
| <span className="hbs-f hbs-e2">[wert](/bo4e/202610/com/Gemeinderabatt#wert)</span> | Wert | number (float) |
| <span className="hbs-f hbs-e2">[einheit](/bo4e/202610/com/Gemeinderabatt#einheit)</span> | Einheit | string |
| <span className="hbs-f hbs-e2">[typ](/bo4e/202610/com/Gemeinderabatt#typ)</span> | Typ | string |
| <span className="hbs-f hbs-e2">[bemessungsgrundlage](/bo4e/202610/com/Gemeinderabatt#bemessungsgrundlage)</span> | Bemessungsgrundlage | number (float) |
| <span className="hbs-f hbs-e1">[gesamtZuAbschlagsbetrag](/bo4e/202610/com/Rechnungsposition#gesamtzuabschlagsbetrag)</span> | gesamtZuAbschlagsbetrag | number (float) |
| <span className="hbs-f hbs-e1">[korrekturfaktor](/bo4e/202610/com/Rechnungsposition#korrekturfaktor)</span> | Gibt ggf. einen Korrekturfaktor für die Menge an. | number (float) |
| <span className="hbs-f hbs-e1">[ausfuehrungsdatum](/bo4e/202610/com/Rechnungsposition#ausfuehrungsdatum)</span> | Das Datum an dem die Leistung erbracht wurde. | string (date-time) |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### istSelbstausgestellt

1 Verwendung(en) in den Nachrichtentypen INVOIC.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_31004](/schnittstellen/202610/pruefi/INVOIC/PI_31004) | Prüfi | INVOIC | stammdaten › RECHNUNG |

### bearbeitungsdatum

11 Verwendung(en) in den Nachrichtentypen INVOIC.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_31001](/schnittstellen/202610/pruefi/INVOIC/PI_31001) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31002](/schnittstellen/202610/pruefi/INVOIC/PI_31002) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31003](/schnittstellen/202610/pruefi/INVOIC/PI_31003) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31004](/schnittstellen/202610/pruefi/INVOIC/PI_31004) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31005](/schnittstellen/202610/pruefi/INVOIC/PI_31005) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31006](/schnittstellen/202610/pruefi/INVOIC/PI_31006) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31007](/schnittstellen/202610/pruefi/INVOIC/PI_31007) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31008](/schnittstellen/202610/pruefi/INVOIC/PI_31008) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31009](/schnittstellen/202610/pruefi/INVOIC/PI_31009) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31010](/schnittstellen/202610/pruefi/INVOIC/PI_31010) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31011](/schnittstellen/202610/pruefi/INVOIC/PI_31011) | Prüfi | INVOIC | stammdaten › RECHNUNG |

### rechnungsdatum

11 Verwendung(en) in den Nachrichtentypen INVOIC.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_31001](/schnittstellen/202610/pruefi/INVOIC/PI_31001) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31002](/schnittstellen/202610/pruefi/INVOIC/PI_31002) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31003](/schnittstellen/202610/pruefi/INVOIC/PI_31003) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31004](/schnittstellen/202610/pruefi/INVOIC/PI_31004) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31005](/schnittstellen/202610/pruefi/INVOIC/PI_31005) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31006](/schnittstellen/202610/pruefi/INVOIC/PI_31006) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31007](/schnittstellen/202610/pruefi/INVOIC/PI_31007) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31008](/schnittstellen/202610/pruefi/INVOIC/PI_31008) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31009](/schnittstellen/202610/pruefi/INVOIC/PI_31009) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31010](/schnittstellen/202610/pruefi/INVOIC/PI_31010) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31011](/schnittstellen/202610/pruefi/INVOIC/PI_31011) | Prüfi | INVOIC | stammdaten › RECHNUNG |

### faelligkeitsdatum

11 Verwendung(en) in den Nachrichtentypen INVOIC.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_31001](/schnittstellen/202610/pruefi/INVOIC/PI_31001) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31002](/schnittstellen/202610/pruefi/INVOIC/PI_31002) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31003](/schnittstellen/202610/pruefi/INVOIC/PI_31003) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31004](/schnittstellen/202610/pruefi/INVOIC/PI_31004) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31005](/schnittstellen/202610/pruefi/INVOIC/PI_31005) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31006](/schnittstellen/202610/pruefi/INVOIC/PI_31006) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31007](/schnittstellen/202610/pruefi/INVOIC/PI_31007) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31008](/schnittstellen/202610/pruefi/INVOIC/PI_31008) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31009](/schnittstellen/202610/pruefi/INVOIC/PI_31009) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31010](/schnittstellen/202610/pruefi/INVOIC/PI_31010) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31011](/schnittstellen/202610/pruefi/INVOIC/PI_31011) | Prüfi | INVOIC | stammdaten › RECHNUNG |

### rechnungsstatus

11 Verwendung(en) in den Nachrichtentypen INVOIC.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_31001](/schnittstellen/202610/pruefi/INVOIC/PI_31001) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31002](/schnittstellen/202610/pruefi/INVOIC/PI_31002) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31003](/schnittstellen/202610/pruefi/INVOIC/PI_31003) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31004](/schnittstellen/202610/pruefi/INVOIC/PI_31004) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31005](/schnittstellen/202610/pruefi/INVOIC/PI_31005) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31006](/schnittstellen/202610/pruefi/INVOIC/PI_31006) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31007](/schnittstellen/202610/pruefi/INVOIC/PI_31007) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31008](/schnittstellen/202610/pruefi/INVOIC/PI_31008) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31009](/schnittstellen/202610/pruefi/INVOIC/PI_31009) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31010](/schnittstellen/202610/pruefi/INVOIC/PI_31010) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31011](/schnittstellen/202610/pruefi/INVOIC/PI_31011) | Prüfi | INVOIC | stammdaten › RECHNUNG |

### rechnungstyp

11 Verwendung(en) in den Nachrichtentypen INVOIC.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_31001](/schnittstellen/202610/pruefi/INVOIC/PI_31001) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31002](/schnittstellen/202610/pruefi/INVOIC/PI_31002) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31003](/schnittstellen/202610/pruefi/INVOIC/PI_31003) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31004](/schnittstellen/202610/pruefi/INVOIC/PI_31004) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31005](/schnittstellen/202610/pruefi/INVOIC/PI_31005) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31006](/schnittstellen/202610/pruefi/INVOIC/PI_31006) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31007](/schnittstellen/202610/pruefi/INVOIC/PI_31007) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31008](/schnittstellen/202610/pruefi/INVOIC/PI_31008) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31009](/schnittstellen/202610/pruefi/INVOIC/PI_31009) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31010](/schnittstellen/202610/pruefi/INVOIC/PI_31010) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31011](/schnittstellen/202610/pruefi/INVOIC/PI_31011) | Prüfi | INVOIC | stammdaten › RECHNUNG |

### istReverseCharge

11 Verwendung(en) in den Nachrichtentypen INVOIC.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_31001](/schnittstellen/202610/pruefi/INVOIC/PI_31001) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31002](/schnittstellen/202610/pruefi/INVOIC/PI_31002) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31003](/schnittstellen/202610/pruefi/INVOIC/PI_31003) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31004](/schnittstellen/202610/pruefi/INVOIC/PI_31004) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31005](/schnittstellen/202610/pruefi/INVOIC/PI_31005) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31006](/schnittstellen/202610/pruefi/INVOIC/PI_31006) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31007](/schnittstellen/202610/pruefi/INVOIC/PI_31007) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31008](/schnittstellen/202610/pruefi/INVOIC/PI_31008) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31009](/schnittstellen/202610/pruefi/INVOIC/PI_31009) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31010](/schnittstellen/202610/pruefi/INVOIC/PI_31010) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31011](/schnittstellen/202610/pruefi/INVOIC/PI_31011) | Prüfi | INVOIC | stammdaten › RECHNUNG |

### originalRechnungsnummer

3 Verwendung(en) in den Nachrichtentypen INVOIC.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_31002](/schnittstellen/202610/pruefi/INVOIC/PI_31002) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31004](/schnittstellen/202610/pruefi/INVOIC/PI_31004) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31011](/schnittstellen/202610/pruefi/INVOIC/PI_31011) | Prüfi | INVOIC | stammdaten › RECHNUNG |

### referenzNachrichtendatum

3 Verwendung(en) in den Nachrichtentypen INVOIC.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_31002](/schnittstellen/202610/pruefi/INVOIC/PI_31002) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31004](/schnittstellen/202610/pruefi/INVOIC/PI_31004) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31011](/schnittstellen/202610/pruefi/INVOIC/PI_31011) | Prüfi | INVOIC | stammdaten › RECHNUNG |

### referenzDokumentennummer

8 Verwendung(en) in den Nachrichtentypen INVOIC.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_31002](/schnittstellen/202610/pruefi/INVOIC/PI_31002) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31003](/schnittstellen/202610/pruefi/INVOIC/PI_31003) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31005](/schnittstellen/202610/pruefi/INVOIC/PI_31005) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31006](/schnittstellen/202610/pruefi/INVOIC/PI_31006) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31007](/schnittstellen/202610/pruefi/INVOIC/PI_31007) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31008](/schnittstellen/202610/pruefi/INVOIC/PI_31008) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31009](/schnittstellen/202610/pruefi/INVOIC/PI_31009) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31011](/schnittstellen/202610/pruefi/INVOIC/PI_31011) | Prüfi | INVOIC | stammdaten › RECHNUNG |

### referenzVorgaengerrechnung

2 Verwendung(en) in den Nachrichtentypen INVOIC.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_31002](/schnittstellen/202610/pruefi/INVOIC/PI_31002) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31010](/schnittstellen/202610/pruefi/INVOIC/PI_31010) | Prüfi | INVOIC | stammdaten › RECHNUNG |

### datumVorgaengerrechnung

2 Verwendung(en) in den Nachrichtentypen INVOIC.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_31002](/schnittstellen/202610/pruefi/INVOIC/PI_31002) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31010](/schnittstellen/202610/pruefi/INVOIC/PI_31010) | Prüfi | INVOIC | stammdaten › RECHNUNG |

### preisNetzbetreiberCodenummer

1 Verwendung(en) in den Nachrichtentypen INVOIC.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_31002](/schnittstellen/202610/pruefi/INVOIC/PI_31002) | Prüfi | INVOIC | stammdaten › RECHNUNG |

### netzkonto

3 Verwendung(en) in den Nachrichtentypen INVOIC.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_31004](/schnittstellen/202610/pruefi/INVOIC/PI_31004) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31007](/schnittstellen/202610/pruefi/INVOIC/PI_31007) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31008](/schnittstellen/202610/pruefi/INVOIC/PI_31008) | Prüfi | INVOIC | stammdaten › RECHNUNG |

### ausfuehrungsdatum

3 Verwendung(en) in den Nachrichtentypen INVOIC.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_31003](/schnittstellen/202610/pruefi/INVOIC/PI_31003) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31004](/schnittstellen/202610/pruefi/INVOIC/PI_31004) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31011](/schnittstellen/202610/pruefi/INVOIC/PI_31011) | Prüfi | INVOIC | stammdaten › RECHNUNG |

### sonderrechnungsarten

1 Verwendung(en) in den Nachrichtentypen INVOIC.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_31002](/schnittstellen/202610/pruefi/INVOIC/PI_31002) | Prüfi | INVOIC | stammdaten › RECHNUNG |

### energierichtung

2 Verwendung(en) in den Nachrichtentypen INVOIC.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_31005](/schnittstellen/202610/pruefi/INVOIC/PI_31005) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31006](/schnittstellen/202610/pruefi/INVOIC/PI_31006) | Prüfi | INVOIC | stammdaten › RECHNUNG |

### beginnPeriodeBilanzierung

2 Verwendung(en) in den Nachrichtentypen INVOIC.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_31005](/schnittstellen/202610/pruefi/INVOIC/PI_31005) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31006](/schnittstellen/202610/pruefi/INVOIC/PI_31006) | Prüfi | INVOIC | stammdaten › RECHNUNG |

### endePeriodeNetznutzung

2 Verwendung(en) in den Nachrichtentypen INVOIC.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_31005](/schnittstellen/202610/pruefi/INVOIC/PI_31005) | Prüfi | INVOIC | stammdaten › RECHNUNG |
| [PI_31006](/schnittstellen/202610/pruefi/INVOIC/PI_31006) | Prüfi | INVOIC | stammdaten › RECHNUNG |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
