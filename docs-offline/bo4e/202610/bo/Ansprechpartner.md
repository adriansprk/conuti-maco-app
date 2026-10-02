# Ansprechpartner
<span hidden data-pagefind-meta={"title:Ansprechpartner — BO4E-Geschäftsobjekt (FV 202610)"} />

BO4E-Geschäftsobjekt · 5 Felder · 114 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="botyp"></a>`boTyp` <span className="hbs-pflicht">\*</span> | [Enum BOTyp](/bo4e/202610/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> | Typ des BO |
| <a id="versionstruktur"></a>`versionStruktur` <span className="hbs-pflicht">\*</span> | string | versionStruktur |
| <a id="nachname"></a>`nachname` | string | Nachname (Familienname) des Ansprechpartners |
| <a id="emailadresse"></a>`eMailAdresse` | string | E-Mail Adresse |
| <a id="rufnummern"></a>`rufnummern` | [Rufnummer[]](/bo4e/202610/com/Rufnummer) | Liste der Telefonnummern, unter denen der Ansprechpartner erreichbar ist. |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[boTyp](/bo4e/202610/bo/Ansprechpartner#botyp) <span className="hbs-pflicht">\*</span></span> | Typ des BO | [Enum BOTyp](/bo4e/202610/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> |
| <span className="hbs-f hbs-e0">[versionStruktur](/bo4e/202610/bo/Ansprechpartner#versionstruktur) <span className="hbs-pflicht">\*</span></span> | versionStruktur | string |
| <span className="hbs-f hbs-e0">[nachname](/bo4e/202610/bo/Ansprechpartner#nachname)</span> | Nachname (Familienname) des Ansprechpartners | string |
| <span className="hbs-f hbs-e0">[eMailAdresse](/bo4e/202610/bo/Ansprechpartner#emailadresse)</span> | E-Mail Adresse | string |
| <span className="hbs-g hbs-e0">[rufnummern](/bo4e/202610/bo/Ansprechpartner#rufnummern) <span className="hbs-liste">[ ]</span></span> | Liste der Telefonnummern, unter denen der Ansprechpartner erreichbar ist. | [Rufnummer[]](/bo4e/202610/com/Rufnummer) |
| <span className="hbs-f hbs-e1">[nummerntyp](/bo4e/202610/com/Rufnummer#nummerntyp)</span> | Rufnummernart | [Enum Rufnummernart](/bo4e/202610/enum/Rufnummernart)<br/><Werte>`RUF_ZENTRALE`, `FAX_ZENTRALE`, `SAMMELRUF`, `SAMMELFAX`, `ABTEILUNGRUF`, `ABTEILUNGFAX`, `RUF_DURCHWAHL`, `FAX_DURCHWAHL`, `MOBIL_NUMMER`</Werte> |
| <span className="hbs-f hbs-e1">[rufnummer](/bo4e/202610/com/Rufnummer#rufnummer)</span> | rufnummer | string |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### nachname

51 Verwendung(en) in den Nachrichtentypen COMDIS, INSRPT, INVOIC, ORDERS, ORDRSP, PARTIN, QUOTES, REMADV, REQOTE, UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_15001](/schnittstellen/202610/pruefi/QUOTES/PI_15001) | Prüfi | QUOTES | transaktionsdaten › absender › ansprechpartner |
| [PI_15003](/schnittstellen/202610/pruefi/QUOTES/PI_15003) | Prüfi | QUOTES | transaktionsdaten › absender › ansprechpartner |
| [PI_15004](/schnittstellen/202610/pruefi/QUOTES/PI_15004) | Prüfi | QUOTES | transaktionsdaten › absender › ansprechpartner |
| [PI_17001](/schnittstellen/202610/pruefi/ORDERS/PI_17001) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner |
| [PI_17104](/schnittstellen/202610/pruefi/ORDERS/PI_17104) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner |
| [PI_17113](/schnittstellen/202610/pruefi/ORDERS/PI_17113) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner |
| [PI_17115](/schnittstellen/202610/pruefi/ORDERS/PI_17115) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner |
| [PI_17116](/schnittstellen/202610/pruefi/ORDERS/PI_17116) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner |
| [PI_17117](/schnittstellen/202610/pruefi/ORDERS/PI_17117) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner |
| [PI_19001](/schnittstellen/202610/pruefi/ORDRSP/PI_19001) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner |
| [PI_19002](/schnittstellen/202610/pruefi/ORDRSP/PI_19002) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner |
| [PI_19005](/schnittstellen/202610/pruefi/ORDRSP/PI_19005) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner |
| [PI_19006](/schnittstellen/202610/pruefi/ORDRSP/PI_19006) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner |
| [PI_19104](/schnittstellen/202610/pruefi/ORDRSP/PI_19104) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner |
| [PI_19114](/schnittstellen/202610/pruefi/ORDRSP/PI_19114) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner |
| [PI_19301](/schnittstellen/202610/pruefi/ORDRSP/PI_19301) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner |
| [PI_19302](/schnittstellen/202610/pruefi/ORDRSP/PI_19302) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner |
| [PI_23001](/schnittstellen/202610/pruefi/INSRPT/PI_23001) | Prüfi | INSRPT | transaktionsdaten › absender › ansprechpartner |
| [PI_23001](/schnittstellen/202610/pruefi/INSRPT/PI_23001) | Prüfi | INSRPT | transaktionsdaten › ansprechpartnerKunde |
| [PI_25001](/schnittstellen/202610/pruefi/UTILTS/PI_25001) | Prüfi | UTILTS | transaktionsdaten › absender › ansprechpartner |
| [PI_25004](/schnittstellen/202610/pruefi/UTILTS/PI_25004) | Prüfi | UTILTS | transaktionsdaten › absender › ansprechpartner |
| [PI_25010](/schnittstellen/202610/pruefi/UTILTS/PI_25010) | Prüfi | UTILTS | transaktionsdaten › absender › ansprechpartner |
| [PI_29001](/schnittstellen/202610/pruefi/COMDIS/PI_29001) | Prüfi | COMDIS | transaktionsdaten › absender › ansprechpartner |
| [PI_29002](/schnittstellen/202610/pruefi/COMDIS/PI_29002) | Prüfi | COMDIS | transaktionsdaten › absender › ansprechpartner |
| [PI_31001](/schnittstellen/202610/pruefi/INVOIC/PI_31001) | Prüfi | INVOIC | transaktionsdaten › absender › ansprechpartner |
| [PI_31002](/schnittstellen/202610/pruefi/INVOIC/PI_31002) | Prüfi | INVOIC | transaktionsdaten › absender › ansprechpartner |
| [PI_31003](/schnittstellen/202610/pruefi/INVOIC/PI_31003) | Prüfi | INVOIC | transaktionsdaten › absender › ansprechpartner |
| [PI_31004](/schnittstellen/202610/pruefi/INVOIC/PI_31004) | Prüfi | INVOIC | transaktionsdaten › absender › ansprechpartner |
| [PI_31005](/schnittstellen/202610/pruefi/INVOIC/PI_31005) | Prüfi | INVOIC | transaktionsdaten › absender › ansprechpartner |
| [PI_31006](/schnittstellen/202610/pruefi/INVOIC/PI_31006) | Prüfi | INVOIC | transaktionsdaten › absender › ansprechpartner |
| [PI_31007](/schnittstellen/202610/pruefi/INVOIC/PI_31007) | Prüfi | INVOIC | transaktionsdaten › absender › ansprechpartner |
| [PI_31008](/schnittstellen/202610/pruefi/INVOIC/PI_31008) | Prüfi | INVOIC | transaktionsdaten › absender › ansprechpartner |
| [PI_31009](/schnittstellen/202610/pruefi/INVOIC/PI_31009) | Prüfi | INVOIC | transaktionsdaten › absender › ansprechpartner |
| [PI_31010](/schnittstellen/202610/pruefi/INVOIC/PI_31010) | Prüfi | INVOIC | transaktionsdaten › absender › ansprechpartner |
| [PI_31011](/schnittstellen/202610/pruefi/INVOIC/PI_31011) | Prüfi | INVOIC | transaktionsdaten › absender › ansprechpartner |
| [PI_33001](/schnittstellen/202610/pruefi/REMADV/PI_33001) | Prüfi | REMADV | transaktionsdaten › absender › ansprechpartner |
| [PI_33002](/schnittstellen/202610/pruefi/REMADV/PI_33002) | Prüfi | REMADV | transaktionsdaten › absender › ansprechpartner |
| [PI_33003](/schnittstellen/202610/pruefi/REMADV/PI_33003) | Prüfi | REMADV | transaktionsdaten › absender › ansprechpartner |
| [PI_33004](/schnittstellen/202610/pruefi/REMADV/PI_33004) | Prüfi | REMADV | transaktionsdaten › absender › ansprechpartner |
| [PI_35001](/schnittstellen/202610/pruefi/REQOTE/PI_35001) | Prüfi | REQOTE | transaktionsdaten › absender › ansprechpartner |
| [PI_35002](/schnittstellen/202610/pruefi/REQOTE/PI_35002) | Prüfi | REQOTE | transaktionsdaten › absender › ansprechpartner |
| [PI_35004](/schnittstellen/202610/pruefi/REQOTE/PI_35004) | Prüfi | REQOTE | transaktionsdaten › absender › ansprechpartner |
| [PI_37000](/schnittstellen/202610/pruefi/PARTIN/PI_37000) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben › ansprechpartner |
| [PI_37001](/schnittstellen/202610/pruefi/PARTIN/PI_37001) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben › ansprechpartner |
| [PI_37002](/schnittstellen/202610/pruefi/PARTIN/PI_37002) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben › ansprechpartner |
| [PI_37008](/schnittstellen/202610/pruefi/PARTIN/PI_37008) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben › ansprechpartner |
| [PI_37009](/schnittstellen/202610/pruefi/PARTIN/PI_37009) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben › ansprechpartner |
| [PI_37010](/schnittstellen/202610/pruefi/PARTIN/PI_37010) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben › ansprechpartner |
| [PI_37012](/schnittstellen/202610/pruefi/PARTIN/PI_37012) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben › ansprechpartner |
| [PI_37013](/schnittstellen/202610/pruefi/PARTIN/PI_37013) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben › ansprechpartner |
| [PI_37014](/schnittstellen/202610/pruefi/PARTIN/PI_37014) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben › ansprechpartner |

### eMailAdresse

63 Verwendung(en) in den Nachrichtentypen COMDIS, INSRPT, ORDERS, ORDRSP, PARTIN, QUOTES, REMADV, REQOTE, UTILMD, UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_15001](/schnittstellen/202610/pruefi/QUOTES/PI_15001) | Prüfi | QUOTES | transaktionsdaten › absender › ansprechpartner |
| [PI_15003](/schnittstellen/202610/pruefi/QUOTES/PI_15003) | Prüfi | QUOTES | transaktionsdaten › absender › ansprechpartner |
| [PI_15004](/schnittstellen/202610/pruefi/QUOTES/PI_15004) | Prüfi | QUOTES | transaktionsdaten › absender › ansprechpartner |
| [PI_17001](/schnittstellen/202610/pruefi/ORDERS/PI_17001) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner |
| [PI_17104](/schnittstellen/202610/pruefi/ORDERS/PI_17104) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner |
| [PI_17113](/schnittstellen/202610/pruefi/ORDERS/PI_17113) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner |
| [PI_17115](/schnittstellen/202610/pruefi/ORDERS/PI_17115) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner |
| [PI_17116](/schnittstellen/202610/pruefi/ORDERS/PI_17116) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner |
| [PI_17117](/schnittstellen/202610/pruefi/ORDERS/PI_17117) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner |
| [PI_19001](/schnittstellen/202610/pruefi/ORDRSP/PI_19001) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner |
| [PI_19002](/schnittstellen/202610/pruefi/ORDRSP/PI_19002) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner |
| [PI_19005](/schnittstellen/202610/pruefi/ORDRSP/PI_19005) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner |
| [PI_19006](/schnittstellen/202610/pruefi/ORDRSP/PI_19006) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner |
| [PI_19104](/schnittstellen/202610/pruefi/ORDRSP/PI_19104) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner |
| [PI_19114](/schnittstellen/202610/pruefi/ORDRSP/PI_19114) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner |
| [PI_19301](/schnittstellen/202610/pruefi/ORDRSP/PI_19301) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner |
| [PI_19302](/schnittstellen/202610/pruefi/ORDRSP/PI_19302) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner |
| [PI_23001](/schnittstellen/202610/pruefi/INSRPT/PI_23001) | Prüfi | INSRPT | transaktionsdaten › absender › ansprechpartner |
| [PI_23001](/schnittstellen/202610/pruefi/INSRPT/PI_23001) | Prüfi | INSRPT | transaktionsdaten › ansprechpartnerKunde |
| [PI_25001](/schnittstellen/202610/pruefi/UTILTS/PI_25001) | Prüfi | UTILTS | transaktionsdaten › absender › ansprechpartner |
| [PI_25004](/schnittstellen/202610/pruefi/UTILTS/PI_25004) | Prüfi | UTILTS | transaktionsdaten › absender › ansprechpartner |
| [PI_25010](/schnittstellen/202610/pruefi/UTILTS/PI_25010) | Prüfi | UTILTS | transaktionsdaten › absender › ansprechpartner |
| [PI_29001](/schnittstellen/202610/pruefi/COMDIS/PI_29001) | Prüfi | COMDIS | transaktionsdaten › absender › ansprechpartner |
| [PI_29002](/schnittstellen/202610/pruefi/COMDIS/PI_29002) | Prüfi | COMDIS | transaktionsdaten › absender › ansprechpartner |
| [PI_33001](/schnittstellen/202610/pruefi/REMADV/PI_33001) | Prüfi | REMADV | transaktionsdaten › absender › ansprechpartner |
| [PI_33002](/schnittstellen/202610/pruefi/REMADV/PI_33002) | Prüfi | REMADV | transaktionsdaten › absender › ansprechpartner |
| [PI_33003](/schnittstellen/202610/pruefi/REMADV/PI_33003) | Prüfi | REMADV | transaktionsdaten › absender › ansprechpartner |
| [PI_33004](/schnittstellen/202610/pruefi/REMADV/PI_33004) | Prüfi | REMADV | transaktionsdaten › absender › ansprechpartner |
| [PI_35001](/schnittstellen/202610/pruefi/REQOTE/PI_35001) | Prüfi | REQOTE | transaktionsdaten › absender › ansprechpartner |
| [PI_35002](/schnittstellen/202610/pruefi/REQOTE/PI_35002) | Prüfi | REQOTE | transaktionsdaten › absender › ansprechpartner |
| [PI_35004](/schnittstellen/202610/pruefi/REQOTE/PI_35004) | Prüfi | REQOTE | transaktionsdaten › absender › ansprechpartner |
| [PI_37000](/schnittstellen/202610/pruefi/PARTIN/PI_37000) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben › ansprechpartner |
| [PI_37001](/schnittstellen/202610/pruefi/PARTIN/PI_37001) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben › ansprechpartner |
| [PI_37002](/schnittstellen/202610/pruefi/PARTIN/PI_37002) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben › ansprechpartner |
| [PI_37008](/schnittstellen/202610/pruefi/PARTIN/PI_37008) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben › ansprechpartner |
| [PI_37009](/schnittstellen/202610/pruefi/PARTIN/PI_37009) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben › ansprechpartner |
| [PI_37010](/schnittstellen/202610/pruefi/PARTIN/PI_37010) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben › ansprechpartner |
| [PI_37012](/schnittstellen/202610/pruefi/PARTIN/PI_37012) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben › ansprechpartner |
| [PI_37013](/schnittstellen/202610/pruefi/PARTIN/PI_37013) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben › ansprechpartner |
| [PI_37014](/schnittstellen/202610/pruefi/PARTIN/PI_37014) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben › ansprechpartner |
| [PI_55001](/schnittstellen/202610/pruefi/UTILMD/PI_55001) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner › ansprechpartner |
| [PI_55013](/schnittstellen/202610/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner › ansprechpartner |
| [PI_55013](/schnittstellen/202610/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner › ansprechpartner |
| [PI_55014](/schnittstellen/202610/pruefi/UTILMD/PI_55014) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner › ansprechpartner |
| [PI_55042](/schnittstellen/202610/pruefi/UTILMD/PI_55042) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner › ansprechpartner |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner › ansprechpartner |
| [PI_55109](/schnittstellen/202610/pruefi/UTILMD/PI_55109) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner › ansprechpartner |
| [PI_55110](/schnittstellen/202610/pruefi/UTILMD/PI_55110) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner › ansprechpartner |
| [PI_55136](/schnittstellen/202610/pruefi/UTILMD/PI_55136) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner › ansprechpartner |
| [PI_55137](/schnittstellen/202610/pruefi/UTILMD/PI_55137) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner › ansprechpartner |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner › ansprechpartner |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner › ansprechpartner |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner › ansprechpartner |
| [PI_55600](/schnittstellen/202610/pruefi/UTILMD/PI_55600) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner › ansprechpartner |
| [PI_55601](/schnittstellen/202610/pruefi/UTILMD/PI_55601) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner › ansprechpartner |
| [PI_55616](/schnittstellen/202610/pruefi/UTILMD/PI_55616) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner › ansprechpartner |
| [PI_55622](/schnittstellen/202610/pruefi/UTILMD/PI_55622) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner › ansprechpartner |
| [PI_55628](/schnittstellen/202610/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner › ansprechpartner |
| [PI_55634](/schnittstellen/202610/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner › ansprechpartner |
| [PI_55643](/schnittstellen/202610/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner › ansprechpartner |
| [PI_55648](/schnittstellen/202610/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner › ansprechpartner |
| [PI_55663](/schnittstellen/202610/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner › ansprechpartner |
| [PI_55669](/schnittstellen/202610/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner › ansprechpartner |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
