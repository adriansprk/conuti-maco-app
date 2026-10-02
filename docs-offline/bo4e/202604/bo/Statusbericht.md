# Statusbericht
<span hidden data-pagefind-meta={"title:Statusbericht — BO4E-Geschäftsobjekt (FV 202604)"} />

BO4E-Geschäftsobjekt · 8 Felder · 4 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="botyp"></a>`boTyp` <span className="hbs-pflicht">\*</span> | [Enum BOTyp](/bo4e/202604/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> | Typ des BO |
| <a id="versionstruktur"></a>`versionStruktur` <span className="hbs-pflicht">\*</span> | string | versionStruktur |
| <a id="status"></a>`status` | [Enum BerichtStatus](/bo4e/202604/enum/BerichtStatus)<br/><Werte>`ERFOLGREICH`, `FEHLER`</Werte> | Status des Berichtes (Fehlerhaft, Erfolgreich) |
| <a id="pruefgegenstand"></a>`pruefgegenstand` | string | Das geprüfte Dokument, z.B. die Referenz auf die EDIFACT-Nachricht die geprüft / beanstandet wurde |
| <a id="datumpruefung"></a>`datumPruefung` | string (date-time) | Pruefdatum (wann wurde der Pruefgegenstand geprüft) |
| <a id="fehler"></a>`fehler` | [Fehler](/bo4e/202604/com/Fehler) | Liste der Fehler |
| <a id="absenderreferenz"></a>`absenderreferenz` | string | absenderreferenz |
| <a id="transaktionsreferenznummer"></a>`transaktionsReferenznummer` | string | transaktionsReferenznummer |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[boTyp](/bo4e/202604/bo/Statusbericht#botyp) <span className="hbs-pflicht">\*</span></span> | Typ des BO | [Enum BOTyp](/bo4e/202604/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> |
| <span className="hbs-f hbs-e0">[versionStruktur](/bo4e/202604/bo/Statusbericht#versionstruktur) <span className="hbs-pflicht">\*</span></span> | versionStruktur | string |
| <span className="hbs-f hbs-e0">[status](/bo4e/202604/bo/Statusbericht#status)</span> | Status des Berichtes (Fehlerhaft, Erfolgreich) | [Enum BerichtStatus](/bo4e/202604/enum/BerichtStatus)<br/><Werte>`ERFOLGREICH`, `FEHLER`</Werte> |
| <span className="hbs-f hbs-e0">[pruefgegenstand](/bo4e/202604/bo/Statusbericht#pruefgegenstand)</span> | Das geprüfte Dokument, z.B. die Referenz auf die EDIFACT-Nachricht die geprüft / beanstandet wurde | string |
| <span className="hbs-f hbs-e0">[datumPruefung](/bo4e/202604/bo/Statusbericht#datumpruefung)</span> | Pruefdatum (wann wurde der Pruefgegenstand geprüft) | string (date-time) |
| <span className="hbs-g hbs-e0">[fehler](/bo4e/202604/bo/Statusbericht#fehler)</span> | Liste der Fehler | [Fehler](/bo4e/202604/com/Fehler) |
| <span className="hbs-f hbs-e1">[typ](/bo4e/202604/com/Fehler#typ)</span> | Gibt den Typ des Fehlers an. | [Enum FehlerTyp](/bo4e/202604/enum/FehlerTyp)<br/><Werte>`VERARBEITUNG`, `SYNTAX`</Werte> |
| <span className="hbs-g hbs-e1">[fehlerDetails](/bo4e/202604/com/Fehler#fehlerdetails) <span className="hbs-liste">[ ]</span></span> | Fehlerdetails | [FehlerDetail[]](/bo4e/202604/com/FehlerDetail) |
| <span className="hbs-f hbs-e2">[code](/bo4e/202604/com/FehlerDetail#code)</span> | FehlerCode | [Enum FehlerCode](/bo4e/202604/enum/FehlerCode)<br/><Werte>`ID_UNBEKANNT`, `ABSENDER_NICHT_ZUGEORDNET`, `EMPFAENGER_NICHT_ZUGEORDNET`, `GERAET_UNBEKANNT`, `OBIS_UNBEKANNT`, `REFERENZIERUNG_FEHLERHAFT`, `TUPEL_UNBEKANNT`, `ABSENDER_TUPEL_NICHT_ZUGEORDNET`, `EMPFAENGER_TUPEL_NICHT_ZUGEORDNET`, `VORKOMMA_ZU_VIELE_STELLEN`, `ZEITREIHE_UNVOLLSTAENDIG`, `REFERENZIERTES_TUPEL_UNBEKANNT`, `MARKTLOKATION_UNBEKANNT`, `MESSLOKATION_UNBEKANNT`, `MELDEPUNKT_NICHT_MEHR_IM_NETZ`, `ERFORDERLICHE_ANGABE_FEHLT`, `GESCHAEFTSVORFALL_ZURUECKGEWIESEN`, `ZEITINTERVALL_NEGATIV`, `FORMAT_NICHT_EINGEHALTEN`, `GESCHAEFTSVORFALL_ABSENDER`, `KONFIGURATIONSID_UNBEKANNT`, `SEGMENTWIEDERHOLUNG_UEBERSCHRITTEN`, `ANZAHLCODES_UEBERSCHRITTEN`, `ZEITANGABE_UNPLAUSIBEL`, `CODE_NICHT_ERLAUBT`, `OBJEKT_NICHT_GEFUNDEN`, `OBJEKT_NICHT_EINDEUTIG`, `GESCHAEFTSVORFALL_OBJEKT_EIGENSCHAFT_NICHT_ERLAUBT`, `EIGENSCHAFT_OBJEKT_WEICHT_VON_GESCHAEFTSVORFALL_CODIERTEN_EIGENSCHAFT_AB`</Werte> |
| <span className="hbs-g hbs-e2">[ursache](/bo4e/202604/com/FehlerDetail#ursache)</span> | — | [FehlerUrsache](/bo4e/202604/com/FehlerUrsache) |
| <span className="hbs-f hbs-e3">[dokument](/bo4e/202604/com/FehlerUrsache#dokument)</span> | dokument | string |
| <span className="hbs-f hbs-e3">[nachricht](/bo4e/202604/com/FehlerUrsache#nachricht)</span> | nachricht | string |
| <span className="hbs-f hbs-e3">[transaktion](/bo4e/202604/com/FehlerUrsache#transaktion)</span> | transaktion | string |
| <span className="hbs-g hbs-e3">[gruppe](/bo4e/202604/com/FehlerUrsache#gruppe)</span> | — | [Gruppe](/bo4e/202604/com/Gruppe) |
| <span className="hbs-f hbs-e4">[gruppe1](/bo4e/202604/com/Gruppe#gruppe1)</span> | Gruppe Zeile 1 | string |
| <span className="hbs-f hbs-e4">[gruppe2](/bo4e/202604/com/Gruppe#gruppe2)</span> | Gruppe Zeile 2 | string |
| <span className="hbs-f hbs-e3">[segment](/bo4e/202604/com/FehlerUrsache#segment)</span> | segment | string |
| <span className="hbs-g hbs-e3">[beschreibung](/bo4e/202604/com/FehlerUrsache#beschreibung)</span> | — | [Beschreibung](/bo4e/202604/com/Beschreibung) |
| <span className="hbs-f hbs-e4">[beschreibung1](/bo4e/202604/com/Beschreibung#beschreibung1)</span> | Beschreibung Zeile 1 | string |
| <span className="hbs-f hbs-e4">[beschreibung2](/bo4e/202604/com/Beschreibung#beschreibung2)</span> | Beschreibung Zeile 2 | string |
| <span className="hbs-g hbs-e2">[beschreibung](/bo4e/202604/com/FehlerDetail#beschreibung)</span> | — | [Beschreibung](/bo4e/202604/com/Beschreibung) |
| <span className="hbs-f hbs-e3">[beschreibung1](/bo4e/202604/com/Beschreibung#beschreibung1)</span> | Beschreibung Zeile 1 | string |
| <span className="hbs-f hbs-e3">[beschreibung2](/bo4e/202604/com/Beschreibung#beschreibung2)</span> | Beschreibung Zeile 2 | string |
| <span className="hbs-f hbs-e0">[absenderreferenz](/bo4e/202604/bo/Statusbericht#absenderreferenz)</span> | absenderreferenz | string |
| <span className="hbs-f hbs-e0">[transaktionsReferenznummer](/bo4e/202604/bo/Statusbericht#transaktionsreferenznummer)</span> | transaktionsReferenznummer | string |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### pruefgegenstand

2 Verwendung(en) in den Nachrichtentypen APERAK.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_66666](/schnittstellen/202604/pruefi/APERAK/PI_66666) | Prüfi | APERAK | stammdaten › STATUSBERICHT |
| [PI_99999](/schnittstellen/202604/pruefi/APERAK/PI_99999) | Prüfi | APERAK | stammdaten › STATUSBERICHT |

### datumPruefung

2 Verwendung(en) in den Nachrichtentypen APERAK.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_66666](/schnittstellen/202604/pruefi/APERAK/PI_66666) | Prüfi | APERAK | stammdaten › STATUSBERICHT |
| [PI_99999](/schnittstellen/202604/pruefi/APERAK/PI_99999) | Prüfi | APERAK | stammdaten › STATUSBERICHT |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
