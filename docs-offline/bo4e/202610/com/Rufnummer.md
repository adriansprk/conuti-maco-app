# Rufnummer
<span hidden data-pagefind-meta={"title:Rufnummer — BO4E-Komponente (FV 202610)"} />

BO4E-Komponente · 2 Felder · 126 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="nummerntyp"></a>`nummerntyp` | [Enum Rufnummernart](/bo4e/202610/enum/Rufnummernart)<br/><Werte>`RUF_ZENTRALE`, `FAX_ZENTRALE`, `SAMMELRUF`, `SAMMELFAX`, `ABTEILUNGRUF`, `ABTEILUNGFAX`, `RUF_DURCHWAHL`, `FAX_DURCHWAHL`, `MOBIL_NUMMER`</Werte> | Rufnummernart |
| <a id="rufnummer"></a>`rufnummer` | string | rufnummer |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[nummerntyp](/bo4e/202610/com/Rufnummer#nummerntyp)</span> | Rufnummernart | [Enum Rufnummernart](/bo4e/202610/enum/Rufnummernart)<br/><Werte>`RUF_ZENTRALE`, `FAX_ZENTRALE`, `SAMMELRUF`, `SAMMELFAX`, `ABTEILUNGRUF`, `ABTEILUNGFAX`, `RUF_DURCHWAHL`, `FAX_DURCHWAHL`, `MOBIL_NUMMER`</Werte> |
| <span className="hbs-f hbs-e0">[rufnummer](/bo4e/202610/com/Rufnummer#rufnummer)</span> | rufnummer | string |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### nummerntyp

63 Verwendung(en) in den Nachrichtentypen COMDIS, INSRPT, ORDERS, ORDRSP, PARTIN, QUOTES, REMADV, REQOTE, UTILMD, UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_15001](/schnittstellen/202610/pruefi/QUOTES/PI_15001) | Prüfi | QUOTES | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_15003](/schnittstellen/202610/pruefi/QUOTES/PI_15003) | Prüfi | QUOTES | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_15004](/schnittstellen/202610/pruefi/QUOTES/PI_15004) | Prüfi | QUOTES | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17001](/schnittstellen/202610/pruefi/ORDERS/PI_17001) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17104](/schnittstellen/202610/pruefi/ORDERS/PI_17104) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17113](/schnittstellen/202610/pruefi/ORDERS/PI_17113) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17115](/schnittstellen/202610/pruefi/ORDERS/PI_17115) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17116](/schnittstellen/202610/pruefi/ORDERS/PI_17116) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17117](/schnittstellen/202610/pruefi/ORDERS/PI_17117) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19001](/schnittstellen/202610/pruefi/ORDRSP/PI_19001) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19002](/schnittstellen/202610/pruefi/ORDRSP/PI_19002) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19005](/schnittstellen/202610/pruefi/ORDRSP/PI_19005) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19006](/schnittstellen/202610/pruefi/ORDRSP/PI_19006) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19104](/schnittstellen/202610/pruefi/ORDRSP/PI_19104) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19114](/schnittstellen/202610/pruefi/ORDRSP/PI_19114) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19301](/schnittstellen/202610/pruefi/ORDRSP/PI_19301) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19302](/schnittstellen/202610/pruefi/ORDRSP/PI_19302) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_23001](/schnittstellen/202610/pruefi/INSRPT/PI_23001) | Prüfi | INSRPT | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_23001](/schnittstellen/202610/pruefi/INSRPT/PI_23001) | Prüfi | INSRPT | transaktionsdaten › ansprechpartnerKunde › rufnummern |
| [PI_25001](/schnittstellen/202610/pruefi/UTILTS/PI_25001) | Prüfi | UTILTS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_25004](/schnittstellen/202610/pruefi/UTILTS/PI_25004) | Prüfi | UTILTS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_25010](/schnittstellen/202610/pruefi/UTILTS/PI_25010) | Prüfi | UTILTS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_29001](/schnittstellen/202610/pruefi/COMDIS/PI_29001) | Prüfi | COMDIS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_29002](/schnittstellen/202610/pruefi/COMDIS/PI_29002) | Prüfi | COMDIS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_33001](/schnittstellen/202610/pruefi/REMADV/PI_33001) | Prüfi | REMADV | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_33002](/schnittstellen/202610/pruefi/REMADV/PI_33002) | Prüfi | REMADV | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_33003](/schnittstellen/202610/pruefi/REMADV/PI_33003) | Prüfi | REMADV | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_33004](/schnittstellen/202610/pruefi/REMADV/PI_33004) | Prüfi | REMADV | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_35001](/schnittstellen/202610/pruefi/REQOTE/PI_35001) | Prüfi | REQOTE | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_35002](/schnittstellen/202610/pruefi/REQOTE/PI_35002) | Prüfi | REQOTE | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_35004](/schnittstellen/202610/pruefi/REQOTE/PI_35004) | Prüfi | REQOTE | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_37000](/schnittstellen/202610/pruefi/PARTIN/PI_37000) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben › ansprechpartner › rufnummern |
| [PI_37001](/schnittstellen/202610/pruefi/PARTIN/PI_37001) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben › ansprechpartner › rufnummern |
| [PI_37002](/schnittstellen/202610/pruefi/PARTIN/PI_37002) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben › ansprechpartner › rufnummern |
| [PI_37008](/schnittstellen/202610/pruefi/PARTIN/PI_37008) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben › ansprechpartner › rufnummern |
| [PI_37009](/schnittstellen/202610/pruefi/PARTIN/PI_37009) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben › ansprechpartner › rufnummern |
| [PI_37010](/schnittstellen/202610/pruefi/PARTIN/PI_37010) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben › ansprechpartner › rufnummern |
| [PI_37012](/schnittstellen/202610/pruefi/PARTIN/PI_37012) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben › ansprechpartner › rufnummern |
| [PI_37013](/schnittstellen/202610/pruefi/PARTIN/PI_37013) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben › ansprechpartner › rufnummern |
| [PI_37014](/schnittstellen/202610/pruefi/PARTIN/PI_37014) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben › ansprechpartner › rufnummern |
| [PI_55001](/schnittstellen/202610/pruefi/UTILMD/PI_55001) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner › ansprechpartner › rufnummern |
| [PI_55013](/schnittstellen/202610/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner › ansprechpartner › rufnummern |
| [PI_55013](/schnittstellen/202610/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner › ansprechpartner › rufnummern |
| [PI_55014](/schnittstellen/202610/pruefi/UTILMD/PI_55014) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner › ansprechpartner › rufnummern |
| [PI_55042](/schnittstellen/202610/pruefi/UTILMD/PI_55042) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner › ansprechpartner › rufnummern |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner › ansprechpartner › rufnummern |
| [PI_55109](/schnittstellen/202610/pruefi/UTILMD/PI_55109) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner › ansprechpartner › rufnummern |
| [PI_55110](/schnittstellen/202610/pruefi/UTILMD/PI_55110) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner › ansprechpartner › rufnummern |
| [PI_55136](/schnittstellen/202610/pruefi/UTILMD/PI_55136) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner › ansprechpartner › rufnummern |
| [PI_55137](/schnittstellen/202610/pruefi/UTILMD/PI_55137) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner › ansprechpartner › rufnummern |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner › ansprechpartner › rufnummern |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner › ansprechpartner › rufnummern |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner › ansprechpartner › rufnummern |
| [PI_55600](/schnittstellen/202610/pruefi/UTILMD/PI_55600) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner › ansprechpartner › rufnummern |
| [PI_55601](/schnittstellen/202610/pruefi/UTILMD/PI_55601) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner › ansprechpartner › rufnummern |
| [PI_55616](/schnittstellen/202610/pruefi/UTILMD/PI_55616) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner › ansprechpartner › rufnummern |
| [PI_55622](/schnittstellen/202610/pruefi/UTILMD/PI_55622) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner › ansprechpartner › rufnummern |
| [PI_55628](/schnittstellen/202610/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner › ansprechpartner › rufnummern |
| [PI_55634](/schnittstellen/202610/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner › ansprechpartner › rufnummern |
| [PI_55643](/schnittstellen/202610/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner › ansprechpartner › rufnummern |
| [PI_55648](/schnittstellen/202610/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner › ansprechpartner › rufnummern |
| [PI_55663](/schnittstellen/202610/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner › ansprechpartner › rufnummern |
| [PI_55669](/schnittstellen/202610/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner › ansprechpartner › rufnummern |

### rufnummer

63 Verwendung(en) in den Nachrichtentypen COMDIS, INSRPT, ORDERS, ORDRSP, PARTIN, QUOTES, REMADV, REQOTE, UTILMD, UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_15001](/schnittstellen/202610/pruefi/QUOTES/PI_15001) | Prüfi | QUOTES | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_15003](/schnittstellen/202610/pruefi/QUOTES/PI_15003) | Prüfi | QUOTES | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_15004](/schnittstellen/202610/pruefi/QUOTES/PI_15004) | Prüfi | QUOTES | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17001](/schnittstellen/202610/pruefi/ORDERS/PI_17001) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17104](/schnittstellen/202610/pruefi/ORDERS/PI_17104) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17113](/schnittstellen/202610/pruefi/ORDERS/PI_17113) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17115](/schnittstellen/202610/pruefi/ORDERS/PI_17115) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17116](/schnittstellen/202610/pruefi/ORDERS/PI_17116) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17117](/schnittstellen/202610/pruefi/ORDERS/PI_17117) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19001](/schnittstellen/202610/pruefi/ORDRSP/PI_19001) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19002](/schnittstellen/202610/pruefi/ORDRSP/PI_19002) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19005](/schnittstellen/202610/pruefi/ORDRSP/PI_19005) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19006](/schnittstellen/202610/pruefi/ORDRSP/PI_19006) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19104](/schnittstellen/202610/pruefi/ORDRSP/PI_19104) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19114](/schnittstellen/202610/pruefi/ORDRSP/PI_19114) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19301](/schnittstellen/202610/pruefi/ORDRSP/PI_19301) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19302](/schnittstellen/202610/pruefi/ORDRSP/PI_19302) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_23001](/schnittstellen/202610/pruefi/INSRPT/PI_23001) | Prüfi | INSRPT | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_23001](/schnittstellen/202610/pruefi/INSRPT/PI_23001) | Prüfi | INSRPT | transaktionsdaten › ansprechpartnerKunde › rufnummern |
| [PI_25001](/schnittstellen/202610/pruefi/UTILTS/PI_25001) | Prüfi | UTILTS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_25004](/schnittstellen/202610/pruefi/UTILTS/PI_25004) | Prüfi | UTILTS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_25010](/schnittstellen/202610/pruefi/UTILTS/PI_25010) | Prüfi | UTILTS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_29001](/schnittstellen/202610/pruefi/COMDIS/PI_29001) | Prüfi | COMDIS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_29002](/schnittstellen/202610/pruefi/COMDIS/PI_29002) | Prüfi | COMDIS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_33001](/schnittstellen/202610/pruefi/REMADV/PI_33001) | Prüfi | REMADV | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_33002](/schnittstellen/202610/pruefi/REMADV/PI_33002) | Prüfi | REMADV | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_33003](/schnittstellen/202610/pruefi/REMADV/PI_33003) | Prüfi | REMADV | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_33004](/schnittstellen/202610/pruefi/REMADV/PI_33004) | Prüfi | REMADV | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_35001](/schnittstellen/202610/pruefi/REQOTE/PI_35001) | Prüfi | REQOTE | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_35002](/schnittstellen/202610/pruefi/REQOTE/PI_35002) | Prüfi | REQOTE | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_35004](/schnittstellen/202610/pruefi/REQOTE/PI_35004) | Prüfi | REQOTE | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_37000](/schnittstellen/202610/pruefi/PARTIN/PI_37000) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben › ansprechpartner › rufnummern |
| [PI_37001](/schnittstellen/202610/pruefi/PARTIN/PI_37001) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben › ansprechpartner › rufnummern |
| [PI_37002](/schnittstellen/202610/pruefi/PARTIN/PI_37002) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben › ansprechpartner › rufnummern |
| [PI_37008](/schnittstellen/202610/pruefi/PARTIN/PI_37008) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben › ansprechpartner › rufnummern |
| [PI_37009](/schnittstellen/202610/pruefi/PARTIN/PI_37009) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben › ansprechpartner › rufnummern |
| [PI_37010](/schnittstellen/202610/pruefi/PARTIN/PI_37010) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben › ansprechpartner › rufnummern |
| [PI_37012](/schnittstellen/202610/pruefi/PARTIN/PI_37012) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben › ansprechpartner › rufnummern |
| [PI_37013](/schnittstellen/202610/pruefi/PARTIN/PI_37013) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben › ansprechpartner › rufnummern |
| [PI_37014](/schnittstellen/202610/pruefi/PARTIN/PI_37014) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben › ansprechpartner › rufnummern |
| [PI_55001](/schnittstellen/202610/pruefi/UTILMD/PI_55001) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner › ansprechpartner › rufnummern |
| [PI_55013](/schnittstellen/202610/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner › ansprechpartner › rufnummern |
| [PI_55013](/schnittstellen/202610/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner › ansprechpartner › rufnummern |
| [PI_55014](/schnittstellen/202610/pruefi/UTILMD/PI_55014) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner › ansprechpartner › rufnummern |
| [PI_55042](/schnittstellen/202610/pruefi/UTILMD/PI_55042) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner › ansprechpartner › rufnummern |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner › ansprechpartner › rufnummern |
| [PI_55109](/schnittstellen/202610/pruefi/UTILMD/PI_55109) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner › ansprechpartner › rufnummern |
| [PI_55110](/schnittstellen/202610/pruefi/UTILMD/PI_55110) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner › ansprechpartner › rufnummern |
| [PI_55136](/schnittstellen/202610/pruefi/UTILMD/PI_55136) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner › ansprechpartner › rufnummern |
| [PI_55137](/schnittstellen/202610/pruefi/UTILMD/PI_55137) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner › ansprechpartner › rufnummern |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner › ansprechpartner › rufnummern |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner › ansprechpartner › rufnummern |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner › ansprechpartner › rufnummern |
| [PI_55600](/schnittstellen/202610/pruefi/UTILMD/PI_55600) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner › ansprechpartner › rufnummern |
| [PI_55601](/schnittstellen/202610/pruefi/UTILMD/PI_55601) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › korrespondenzpartner › ansprechpartner › rufnummern |
| [PI_55616](/schnittstellen/202610/pruefi/UTILMD/PI_55616) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner › ansprechpartner › rufnummern |
| [PI_55622](/schnittstellen/202610/pruefi/UTILMD/PI_55622) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner › ansprechpartner › rufnummern |
| [PI_55628](/schnittstellen/202610/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner › ansprechpartner › rufnummern |
| [PI_55634](/schnittstellen/202610/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › korrespondenzpartner › ansprechpartner › rufnummern |
| [PI_55643](/schnittstellen/202610/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner › ansprechpartner › rufnummern |
| [PI_55648](/schnittstellen/202610/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner › ansprechpartner › rufnummern |
| [PI_55663](/schnittstellen/202610/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner › ansprechpartner › rufnummern |
| [PI_55669](/schnittstellen/202610/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › korrespondenzpartner › ansprechpartner › rufnummern |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
