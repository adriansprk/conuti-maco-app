# Rufnummer
<span hidden data-pagefind-meta={"title:Rufnummer — BO4E-Komponente (FV 202604)"} />

BO4E-Komponente · 2 Felder · 738 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="nummerntyp"></a>`nummerntyp` | [Enum Rufnummernart](/bo4e/202604/enum/Rufnummernart)<br/><Werte>`RUF_ZENTRALE`, `FAX_ZENTRALE`, `SAMMELRUF`, `SAMMELFAX`, `ABTEILUNGRUF`, `ABTEILUNGFAX`, `RUF_DURCHWAHL`, `FAX_DURCHWAHL`, `MOBIL_NUMMER`</Werte> | Rufnummernart |
| <a id="rufnummer"></a>`rufnummer` | string | rufnummer |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[nummerntyp](/bo4e/202604/com/Rufnummer#nummerntyp)</span> | Rufnummernart | [Enum Rufnummernart](/bo4e/202604/enum/Rufnummernart)<br/><Werte>`RUF_ZENTRALE`, `FAX_ZENTRALE`, `SAMMELRUF`, `SAMMELFAX`, `ABTEILUNGRUF`, `ABTEILUNGFAX`, `RUF_DURCHWAHL`, `FAX_DURCHWAHL`, `MOBIL_NUMMER`</Werte> |
| <span className="hbs-f hbs-e0">[rufnummer](/bo4e/202604/com/Rufnummer#rufnummer)</span> | rufnummer | string |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### nummerntyp

369 Verwendung(en) in den Nachrichtentypen APERAK, COMDIS, IFTSTA, INSRPT, MSCONS, ORDCHG, ORDERS, ORDRSP, PARTIN, PRICAT, QUOTES, REMADV, REQOTE, UTILMD, UTILMD_GAS, UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_13002](/schnittstellen/202604/pruefi/MSCONS/PI_13002) | Prüfi | MSCONS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_13006](/schnittstellen/202604/pruefi/MSCONS/PI_13006) | Prüfi | MSCONS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_13007](/schnittstellen/202604/pruefi/MSCONS/PI_13007) | Prüfi | MSCONS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_13008](/schnittstellen/202604/pruefi/MSCONS/PI_13008) | Prüfi | MSCONS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_13009](/schnittstellen/202604/pruefi/MSCONS/PI_13009) | Prüfi | MSCONS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_13015](/schnittstellen/202604/pruefi/MSCONS/PI_13015) | Prüfi | MSCONS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_13016](/schnittstellen/202604/pruefi/MSCONS/PI_13016) | Prüfi | MSCONS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_13017](/schnittstellen/202604/pruefi/MSCONS/PI_13017) | Prüfi | MSCONS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_13018](/schnittstellen/202604/pruefi/MSCONS/PI_13018) | Prüfi | MSCONS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_13019](/schnittstellen/202604/pruefi/MSCONS/PI_13019) | Prüfi | MSCONS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_13025](/schnittstellen/202604/pruefi/MSCONS/PI_13025) | Prüfi | MSCONS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_13027](/schnittstellen/202604/pruefi/MSCONS/PI_13027) | Prüfi | MSCONS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_13028](/schnittstellen/202604/pruefi/MSCONS/PI_13028) | Prüfi | MSCONS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_15001](/schnittstellen/202604/pruefi/QUOTES/PI_15001) | Prüfi | QUOTES | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_15003](/schnittstellen/202604/pruefi/QUOTES/PI_15003) | Prüfi | QUOTES | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_15004](/schnittstellen/202604/pruefi/QUOTES/PI_15004) | Prüfi | QUOTES | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17001](/schnittstellen/202604/pruefi/ORDERS/PI_17001) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17002](/schnittstellen/202604/pruefi/ORDERS/PI_17002) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17003](/schnittstellen/202604/pruefi/ORDERS/PI_17003) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17003](/schnittstellen/202604/pruefi/ORDERS/PI_17003) | Prüfi | ORDERS | transaktionsdaten › ansprechpartnerKunde › rufnummern |
| [PI_17004](/schnittstellen/202604/pruefi/ORDERS/PI_17004) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17005](/schnittstellen/202604/pruefi/ORDERS/PI_17005) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17006](/schnittstellen/202604/pruefi/ORDERS/PI_17006) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17009](/schnittstellen/202604/pruefi/ORDERS/PI_17009) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17101](/schnittstellen/202604/pruefi/ORDERS/PI_17101) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17102](/schnittstellen/202604/pruefi/ORDERS/PI_17102) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17103](/schnittstellen/202604/pruefi/ORDERS/PI_17103) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17104](/schnittstellen/202604/pruefi/ORDERS/PI_17104) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17113](/schnittstellen/202604/pruefi/ORDERS/PI_17113) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17115](/schnittstellen/202604/pruefi/ORDERS/PI_17115) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17116](/schnittstellen/202604/pruefi/ORDERS/PI_17116) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17117](/schnittstellen/202604/pruefi/ORDERS/PI_17117) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17118](/schnittstellen/202604/pruefi/ORDERS/PI_17118) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17120](/schnittstellen/202604/pruefi/ORDERS/PI_17120) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17121](/schnittstellen/202604/pruefi/ORDERS/PI_17121) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17122](/schnittstellen/202604/pruefi/ORDERS/PI_17122) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17123](/schnittstellen/202604/pruefi/ORDERS/PI_17123) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17126](/schnittstellen/202604/pruefi/ORDERS/PI_17126) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17128](/schnittstellen/202604/pruefi/ORDERS/PI_17128) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17129](/schnittstellen/202604/pruefi/ORDERS/PI_17129) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17130](/schnittstellen/202604/pruefi/ORDERS/PI_17130) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17131](/schnittstellen/202604/pruefi/ORDERS/PI_17131) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17132](/schnittstellen/202604/pruefi/ORDERS/PI_17132) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17133](/schnittstellen/202604/pruefi/ORDERS/PI_17133) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17134](/schnittstellen/202604/pruefi/ORDERS/PI_17134) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17135](/schnittstellen/202604/pruefi/ORDERS/PI_17135) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19001](/schnittstellen/202604/pruefi/ORDRSP/PI_19001) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19002](/schnittstellen/202604/pruefi/ORDRSP/PI_19002) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19003](/schnittstellen/202604/pruefi/ORDRSP/PI_19003) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19004](/schnittstellen/202604/pruefi/ORDRSP/PI_19004) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19005](/schnittstellen/202604/pruefi/ORDRSP/PI_19005) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19006](/schnittstellen/202604/pruefi/ORDRSP/PI_19006) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19007](/schnittstellen/202604/pruefi/ORDRSP/PI_19007) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19009](/schnittstellen/202604/pruefi/ORDRSP/PI_19009) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19010](/schnittstellen/202604/pruefi/ORDRSP/PI_19010) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19011](/schnittstellen/202604/pruefi/ORDRSP/PI_19011) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19012](/schnittstellen/202604/pruefi/ORDRSP/PI_19012) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19013](/schnittstellen/202604/pruefi/ORDRSP/PI_19013) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19014](/schnittstellen/202604/pruefi/ORDRSP/PI_19014) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19015](/schnittstellen/202604/pruefi/ORDRSP/PI_19015) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19016](/schnittstellen/202604/pruefi/ORDRSP/PI_19016) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19101](/schnittstellen/202604/pruefi/ORDRSP/PI_19101) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19102](/schnittstellen/202604/pruefi/ORDRSP/PI_19102) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19103](/schnittstellen/202604/pruefi/ORDRSP/PI_19103) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19104](/schnittstellen/202604/pruefi/ORDRSP/PI_19104) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19114](/schnittstellen/202604/pruefi/ORDRSP/PI_19114) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19116](/schnittstellen/202604/pruefi/ORDRSP/PI_19116) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19117](/schnittstellen/202604/pruefi/ORDRSP/PI_19117) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19118](/schnittstellen/202604/pruefi/ORDRSP/PI_19118) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19119](/schnittstellen/202604/pruefi/ORDRSP/PI_19119) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19121](/schnittstellen/202604/pruefi/ORDRSP/PI_19121) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19123](/schnittstellen/202604/pruefi/ORDRSP/PI_19123) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19124](/schnittstellen/202604/pruefi/ORDRSP/PI_19124) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19128](/schnittstellen/202604/pruefi/ORDRSP/PI_19128) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19129](/schnittstellen/202604/pruefi/ORDRSP/PI_19129) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19133](/schnittstellen/202604/pruefi/ORDRSP/PI_19133) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19301](/schnittstellen/202604/pruefi/ORDRSP/PI_19301) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19302](/schnittstellen/202604/pruefi/ORDRSP/PI_19302) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_21007](/schnittstellen/202604/pruefi/IFTSTA/PI_21007) | Prüfi | IFTSTA | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_21009](/schnittstellen/202604/pruefi/IFTSTA/PI_21009) | Prüfi | IFTSTA | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_21010](/schnittstellen/202604/pruefi/IFTSTA/PI_21010) | Prüfi | IFTSTA | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_21011](/schnittstellen/202604/pruefi/IFTSTA/PI_21011) | Prüfi | IFTSTA | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_21012](/schnittstellen/202604/pruefi/IFTSTA/PI_21012) | Prüfi | IFTSTA | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_21013](/schnittstellen/202604/pruefi/IFTSTA/PI_21013) | Prüfi | IFTSTA | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_21015](/schnittstellen/202604/pruefi/IFTSTA/PI_21015) | Prüfi | IFTSTA | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_21018](/schnittstellen/202604/pruefi/IFTSTA/PI_21018) | Prüfi | IFTSTA | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_21024](/schnittstellen/202604/pruefi/IFTSTA/PI_21024) | Prüfi | IFTSTA | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_21025](/schnittstellen/202604/pruefi/IFTSTA/PI_21025) | Prüfi | IFTSTA | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_21026](/schnittstellen/202604/pruefi/IFTSTA/PI_21026) | Prüfi | IFTSTA | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_21027](/schnittstellen/202604/pruefi/IFTSTA/PI_21027) | Prüfi | IFTSTA | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_21028](/schnittstellen/202604/pruefi/IFTSTA/PI_21028) | Prüfi | IFTSTA | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_21029](/schnittstellen/202604/pruefi/IFTSTA/PI_21029) | Prüfi | IFTSTA | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_21030](/schnittstellen/202604/pruefi/IFTSTA/PI_21030) | Prüfi | IFTSTA | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_21031](/schnittstellen/202604/pruefi/IFTSTA/PI_21031) | Prüfi | IFTSTA | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_21032](/schnittstellen/202604/pruefi/IFTSTA/PI_21032) | Prüfi | IFTSTA | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_21033](/schnittstellen/202604/pruefi/IFTSTA/PI_21033) | Prüfi | IFTSTA | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_21035](/schnittstellen/202604/pruefi/IFTSTA/PI_21035) | Prüfi | IFTSTA | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_21036](/schnittstellen/202604/pruefi/IFTSTA/PI_21036) | Prüfi | IFTSTA | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_21039](/schnittstellen/202604/pruefi/IFTSTA/PI_21039) | Prüfi | IFTSTA | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_21040](/schnittstellen/202604/pruefi/IFTSTA/PI_21040) | Prüfi | IFTSTA | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_21043](/schnittstellen/202604/pruefi/IFTSTA/PI_21043) | Prüfi | IFTSTA | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_21044](/schnittstellen/202604/pruefi/IFTSTA/PI_21044) | Prüfi | IFTSTA | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_21045](/schnittstellen/202604/pruefi/IFTSTA/PI_21045) | Prüfi | IFTSTA | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_21047](/schnittstellen/202604/pruefi/IFTSTA/PI_21047) | Prüfi | IFTSTA | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_23001](/schnittstellen/202604/pruefi/INSRPT/PI_23001) | Prüfi | INSRPT | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_23001](/schnittstellen/202604/pruefi/INSRPT/PI_23001) | Prüfi | INSRPT | transaktionsdaten › ansprechpartnerKunde › rufnummern |
| [PI_25001](/schnittstellen/202604/pruefi/UTILTS/PI_25001) | Prüfi | UTILTS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_25004](/schnittstellen/202604/pruefi/UTILTS/PI_25004) | Prüfi | UTILTS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_25005](/schnittstellen/202604/pruefi/UTILTS/PI_25005) | Prüfi | UTILTS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_25006](/schnittstellen/202604/pruefi/UTILTS/PI_25006) | Prüfi | UTILTS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_25007](/schnittstellen/202604/pruefi/UTILTS/PI_25007) | Prüfi | UTILTS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_25008](/schnittstellen/202604/pruefi/UTILTS/PI_25008) | Prüfi | UTILTS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_25009](/schnittstellen/202604/pruefi/UTILTS/PI_25009) | Prüfi | UTILTS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_25010](/schnittstellen/202604/pruefi/UTILTS/PI_25010) | Prüfi | UTILTS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_27002](/schnittstellen/202604/pruefi/PRICAT/PI_27002) | Prüfi | PRICAT | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_27003](/schnittstellen/202604/pruefi/PRICAT/PI_27003) | Prüfi | PRICAT | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_29001](/schnittstellen/202604/pruefi/COMDIS/PI_29001) | Prüfi | COMDIS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_29002](/schnittstellen/202604/pruefi/COMDIS/PI_29002) | Prüfi | COMDIS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_33001](/schnittstellen/202604/pruefi/REMADV/PI_33001) | Prüfi | REMADV | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_33002](/schnittstellen/202604/pruefi/REMADV/PI_33002) | Prüfi | REMADV | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_33003](/schnittstellen/202604/pruefi/REMADV/PI_33003) | Prüfi | REMADV | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_33004](/schnittstellen/202604/pruefi/REMADV/PI_33004) | Prüfi | REMADV | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_35001](/schnittstellen/202604/pruefi/REQOTE/PI_35001) | Prüfi | REQOTE | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_35002](/schnittstellen/202604/pruefi/REQOTE/PI_35002) | Prüfi | REQOTE | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_35004](/schnittstellen/202604/pruefi/REQOTE/PI_35004) | Prüfi | REQOTE | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_37000](/schnittstellen/202604/pruefi/PARTIN/PI_37000) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben › ansprechpartner › rufnummern |
| [PI_37000](/schnittstellen/202604/pruefi/PARTIN/PI_37000) | Prüfi | PARTIN | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_37001](/schnittstellen/202604/pruefi/PARTIN/PI_37001) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben › ansprechpartner › rufnummern |
| [PI_37001](/schnittstellen/202604/pruefi/PARTIN/PI_37001) | Prüfi | PARTIN | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_37002](/schnittstellen/202604/pruefi/PARTIN/PI_37002) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben › ansprechpartner › rufnummern |
| [PI_37002](/schnittstellen/202604/pruefi/PARTIN/PI_37002) | Prüfi | PARTIN | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_37008](/schnittstellen/202604/pruefi/PARTIN/PI_37008) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben › ansprechpartner › rufnummern |
| [PI_37008](/schnittstellen/202604/pruefi/PARTIN/PI_37008) | Prüfi | PARTIN | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_37009](/schnittstellen/202604/pruefi/PARTIN/PI_37009) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben › ansprechpartner › rufnummern |
| [PI_37009](/schnittstellen/202604/pruefi/PARTIN/PI_37009) | Prüfi | PARTIN | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_37010](/schnittstellen/202604/pruefi/PARTIN/PI_37010) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben › ansprechpartner › rufnummern |
| [PI_37010](/schnittstellen/202604/pruefi/PARTIN/PI_37010) | Prüfi | PARTIN | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_37012](/schnittstellen/202604/pruefi/PARTIN/PI_37012) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben › ansprechpartner › rufnummern |
| [PI_37012](/schnittstellen/202604/pruefi/PARTIN/PI_37012) | Prüfi | PARTIN | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_37013](/schnittstellen/202604/pruefi/PARTIN/PI_37013) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben › ansprechpartner › rufnummern |
| [PI_37013](/schnittstellen/202604/pruefi/PARTIN/PI_37013) | Prüfi | PARTIN | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_37014](/schnittstellen/202604/pruefi/PARTIN/PI_37014) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben › ansprechpartner › rufnummern |
| [PI_37014](/schnittstellen/202604/pruefi/PARTIN/PI_37014) | Prüfi | PARTIN | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_39000](/schnittstellen/202604/pruefi/ORDCHG/PI_39000) | Prüfi | ORDCHG | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_39001](/schnittstellen/202604/pruefi/ORDCHG/PI_39001) | Prüfi | ORDCHG | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44001](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44001) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44003](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44003) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44004](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44004) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44005](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44005) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44006](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44006) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44007](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44007) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44008](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44008) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44009](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44009) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44010](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44010) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44011](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44011) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44012](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44012) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44015](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44015) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44016](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44016) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44017](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44017) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44018](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44018) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44019](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44019) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44020](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44020) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44021](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44021) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44022](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44022) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44023](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44023) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44024](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44024) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44035](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44035) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44036](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44036) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44037](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44037) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44038](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44038) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44039](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44039) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44040](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44040) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44041](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44041) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44043](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44043) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44044](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44044) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44052](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44052) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44053](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44053) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44060](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44060) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44101](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44101) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44102](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44102) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44103](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44103) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44104](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44104) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44109](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44109) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44111](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44111) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44112](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44112) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44113](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44113) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44115](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44115) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44116](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44116) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44117](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44117) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44119](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44119) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44120](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44120) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44121](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44121) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44123](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44123) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44124](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44124) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44137](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44137) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44138](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44138) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44139](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44139) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44140](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44140) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44142](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44142) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44143](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44143) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44145](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44145) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44146](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44146) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44147](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44147) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44148](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44148) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44149](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44149) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44150](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44150) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44151](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44151) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44152](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44152) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44156](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44156) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44157](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44157) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44159](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44159) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44160](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44160) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44161](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44161) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44162](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44162) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44163](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44163) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44164](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44164) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44165](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44165) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44166](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44166) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44167](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44167) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44168](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44175](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44175) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44176](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44176) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44180](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44180) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44181](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44181) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44182](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44182) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55001](/schnittstellen/202604/pruefi/UTILMD/PI_55001) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55002](/schnittstellen/202604/pruefi/UTILMD/PI_55002) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55003](/schnittstellen/202604/pruefi/UTILMD/PI_55003) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55004](/schnittstellen/202604/pruefi/UTILMD/PI_55004) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55005](/schnittstellen/202604/pruefi/UTILMD/PI_55005) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55006](/schnittstellen/202604/pruefi/UTILMD/PI_55006) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55007](/schnittstellen/202604/pruefi/UTILMD/PI_55007) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55008](/schnittstellen/202604/pruefi/UTILMD/PI_55008) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55009](/schnittstellen/202604/pruefi/UTILMD/PI_55009) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55010](/schnittstellen/202604/pruefi/UTILMD/PI_55010) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55011](/schnittstellen/202604/pruefi/UTILMD/PI_55011) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55012](/schnittstellen/202604/pruefi/UTILMD/PI_55012) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55013](/schnittstellen/202604/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55014](/schnittstellen/202604/pruefi/UTILMD/PI_55014) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55015](/schnittstellen/202604/pruefi/UTILMD/PI_55015) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55016](/schnittstellen/202604/pruefi/UTILMD/PI_55016) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55017](/schnittstellen/202604/pruefi/UTILMD/PI_55017) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55018](/schnittstellen/202604/pruefi/UTILMD/PI_55018) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55022](/schnittstellen/202604/pruefi/UTILMD/PI_55022) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55023](/schnittstellen/202604/pruefi/UTILMD/PI_55023) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55024](/schnittstellen/202604/pruefi/UTILMD/PI_55024) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55035](/schnittstellen/202604/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55036](/schnittstellen/202604/pruefi/UTILMD/PI_55036) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55037](/schnittstellen/202604/pruefi/UTILMD/PI_55037) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55038](/schnittstellen/202604/pruefi/UTILMD/PI_55038) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55039](/schnittstellen/202604/pruefi/UTILMD/PI_55039) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55040](/schnittstellen/202604/pruefi/UTILMD/PI_55040) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55041](/schnittstellen/202604/pruefi/UTILMD/PI_55041) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55042](/schnittstellen/202604/pruefi/UTILMD/PI_55042) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55044](/schnittstellen/202604/pruefi/UTILMD/PI_55044) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55051](/schnittstellen/202604/pruefi/UTILMD/PI_55051) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55052](/schnittstellen/202604/pruefi/UTILMD/PI_55052) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55053](/schnittstellen/202604/pruefi/UTILMD/PI_55053) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55060](/schnittstellen/202604/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55074](/schnittstellen/202604/pruefi/UTILMD/PI_55074) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55075](/schnittstellen/202604/pruefi/UTILMD/PI_55075) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55077](/schnittstellen/202604/pruefi/UTILMD/PI_55077) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55078](/schnittstellen/202604/pruefi/UTILMD/PI_55078) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55080](/schnittstellen/202604/pruefi/UTILMD/PI_55080) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55095](/schnittstellen/202604/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55109](/schnittstellen/202604/pruefi/UTILMD/PI_55109) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55110](/schnittstellen/202604/pruefi/UTILMD/PI_55110) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55126](/schnittstellen/202604/pruefi/UTILMD/PI_55126) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55136](/schnittstellen/202604/pruefi/UTILMD/PI_55136) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55137](/schnittstellen/202604/pruefi/UTILMD/PI_55137) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55156](/schnittstellen/202604/pruefi/UTILMD/PI_55156) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55170](/schnittstellen/202604/pruefi/UTILMD/PI_55170) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55173](/schnittstellen/202604/pruefi/UTILMD/PI_55173) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55175](/schnittstellen/202604/pruefi/UTILMD/PI_55175) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55177](/schnittstellen/202604/pruefi/UTILMD/PI_55177) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55180](/schnittstellen/202604/pruefi/UTILMD/PI_55180) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55194](/schnittstellen/202604/pruefi/UTILMD/PI_55194) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55218](/schnittstellen/202604/pruefi/UTILMD/PI_55218) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55220](/schnittstellen/202604/pruefi/UTILMD/PI_55220) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55225](/schnittstellen/202604/pruefi/UTILMD/PI_55225) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55227](/schnittstellen/202604/pruefi/UTILMD/PI_55227) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55230](/schnittstellen/202604/pruefi/UTILMD/PI_55230) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55232](/schnittstellen/202604/pruefi/UTILMD/PI_55232) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55553](/schnittstellen/202604/pruefi/UTILMD/PI_55553) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55555](/schnittstellen/202604/pruefi/UTILMD/PI_55555) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55557](/schnittstellen/202604/pruefi/UTILMD/PI_55557) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55559](/schnittstellen/202604/pruefi/UTILMD/PI_55559) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55600](/schnittstellen/202604/pruefi/UTILMD/PI_55600) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55601](/schnittstellen/202604/pruefi/UTILMD/PI_55601) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55602](/schnittstellen/202604/pruefi/UTILMD/PI_55602) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55603](/schnittstellen/202604/pruefi/UTILMD/PI_55603) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55604](/schnittstellen/202604/pruefi/UTILMD/PI_55604) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55605](/schnittstellen/202604/pruefi/UTILMD/PI_55605) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55607](/schnittstellen/202604/pruefi/UTILMD/PI_55607) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55608](/schnittstellen/202604/pruefi/UTILMD/PI_55608) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55609](/schnittstellen/202604/pruefi/UTILMD/PI_55609) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55611](/schnittstellen/202604/pruefi/UTILMD/PI_55611) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55613](/schnittstellen/202604/pruefi/UTILMD/PI_55613) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55614](/schnittstellen/202604/pruefi/UTILMD/PI_55614) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55615](/schnittstellen/202604/pruefi/UTILMD/PI_55615) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55616](/schnittstellen/202604/pruefi/UTILMD/PI_55616) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55617](/schnittstellen/202604/pruefi/UTILMD/PI_55617) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55618](/schnittstellen/202604/pruefi/UTILMD/PI_55618) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55619](/schnittstellen/202604/pruefi/UTILMD/PI_55619) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55620](/schnittstellen/202604/pruefi/UTILMD/PI_55620) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55621](/schnittstellen/202604/pruefi/UTILMD/PI_55621) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55622](/schnittstellen/202604/pruefi/UTILMD/PI_55622) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55623](/schnittstellen/202604/pruefi/UTILMD/PI_55623) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55624](/schnittstellen/202604/pruefi/UTILMD/PI_55624) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55625](/schnittstellen/202604/pruefi/UTILMD/PI_55625) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55626](/schnittstellen/202604/pruefi/UTILMD/PI_55626) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55627](/schnittstellen/202604/pruefi/UTILMD/PI_55627) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55628](/schnittstellen/202604/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55629](/schnittstellen/202604/pruefi/UTILMD/PI_55629) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55630](/schnittstellen/202604/pruefi/UTILMD/PI_55630) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55632](/schnittstellen/202604/pruefi/UTILMD/PI_55632) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55633](/schnittstellen/202604/pruefi/UTILMD/PI_55633) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55634](/schnittstellen/202604/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55635](/schnittstellen/202604/pruefi/UTILMD/PI_55635) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55636](/schnittstellen/202604/pruefi/UTILMD/PI_55636) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55638](/schnittstellen/202604/pruefi/UTILMD/PI_55638) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55639](/schnittstellen/202604/pruefi/UTILMD/PI_55639) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55640](/schnittstellen/202604/pruefi/UTILMD/PI_55640) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55641](/schnittstellen/202604/pruefi/UTILMD/PI_55641) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55642](/schnittstellen/202604/pruefi/UTILMD/PI_55642) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55643](/schnittstellen/202604/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55644](/schnittstellen/202604/pruefi/UTILMD/PI_55644) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55645](/schnittstellen/202604/pruefi/UTILMD/PI_55645) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55646](/schnittstellen/202604/pruefi/UTILMD/PI_55646) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55647](/schnittstellen/202604/pruefi/UTILMD/PI_55647) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55648](/schnittstellen/202604/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55649](/schnittstellen/202604/pruefi/UTILMD/PI_55649) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55650](/schnittstellen/202604/pruefi/UTILMD/PI_55650) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55651](/schnittstellen/202604/pruefi/UTILMD/PI_55651) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55652](/schnittstellen/202604/pruefi/UTILMD/PI_55652) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55653](/schnittstellen/202604/pruefi/UTILMD/PI_55653) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55654](/schnittstellen/202604/pruefi/UTILMD/PI_55654) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55655](/schnittstellen/202604/pruefi/UTILMD/PI_55655) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55656](/schnittstellen/202604/pruefi/UTILMD/PI_55656) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55657](/schnittstellen/202604/pruefi/UTILMD/PI_55657) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55658](/schnittstellen/202604/pruefi/UTILMD/PI_55658) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55659](/schnittstellen/202604/pruefi/UTILMD/PI_55659) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55660](/schnittstellen/202604/pruefi/UTILMD/PI_55660) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55661](/schnittstellen/202604/pruefi/UTILMD/PI_55661) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55662](/schnittstellen/202604/pruefi/UTILMD/PI_55662) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55663](/schnittstellen/202604/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55664](/schnittstellen/202604/pruefi/UTILMD/PI_55664) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55665](/schnittstellen/202604/pruefi/UTILMD/PI_55665) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55666](/schnittstellen/202604/pruefi/UTILMD/PI_55666) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55667](/schnittstellen/202604/pruefi/UTILMD/PI_55667) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55669](/schnittstellen/202604/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55670](/schnittstellen/202604/pruefi/UTILMD/PI_55670) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55672](/schnittstellen/202604/pruefi/UTILMD/PI_55672) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55673](/schnittstellen/202604/pruefi/UTILMD/PI_55673) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55674](/schnittstellen/202604/pruefi/UTILMD/PI_55674) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55684](/schnittstellen/202604/pruefi/UTILMD/PI_55684) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55686](/schnittstellen/202604/pruefi/UTILMD/PI_55686) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55688](/schnittstellen/202604/pruefi/UTILMD/PI_55688) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55690](/schnittstellen/202604/pruefi/UTILMD/PI_55690) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55691](/schnittstellen/202604/pruefi/UTILMD/PI_55691) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55692](/schnittstellen/202604/pruefi/UTILMD/PI_55692) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_66666](/schnittstellen/202604/pruefi/APERAK/PI_66666) | Prüfi | APERAK | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_99999](/schnittstellen/202604/pruefi/APERAK/PI_99999) | Prüfi | APERAK | transaktionsdaten › absender › ansprechpartner › rufnummern |

### rufnummer

369 Verwendung(en) in den Nachrichtentypen APERAK, COMDIS, IFTSTA, INSRPT, MSCONS, ORDCHG, ORDERS, ORDRSP, PARTIN, PRICAT, QUOTES, REMADV, REQOTE, UTILMD, UTILMD_GAS, UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_13002](/schnittstellen/202604/pruefi/MSCONS/PI_13002) | Prüfi | MSCONS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_13006](/schnittstellen/202604/pruefi/MSCONS/PI_13006) | Prüfi | MSCONS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_13007](/schnittstellen/202604/pruefi/MSCONS/PI_13007) | Prüfi | MSCONS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_13008](/schnittstellen/202604/pruefi/MSCONS/PI_13008) | Prüfi | MSCONS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_13009](/schnittstellen/202604/pruefi/MSCONS/PI_13009) | Prüfi | MSCONS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_13015](/schnittstellen/202604/pruefi/MSCONS/PI_13015) | Prüfi | MSCONS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_13016](/schnittstellen/202604/pruefi/MSCONS/PI_13016) | Prüfi | MSCONS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_13017](/schnittstellen/202604/pruefi/MSCONS/PI_13017) | Prüfi | MSCONS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_13018](/schnittstellen/202604/pruefi/MSCONS/PI_13018) | Prüfi | MSCONS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_13019](/schnittstellen/202604/pruefi/MSCONS/PI_13019) | Prüfi | MSCONS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_13025](/schnittstellen/202604/pruefi/MSCONS/PI_13025) | Prüfi | MSCONS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_13027](/schnittstellen/202604/pruefi/MSCONS/PI_13027) | Prüfi | MSCONS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_13028](/schnittstellen/202604/pruefi/MSCONS/PI_13028) | Prüfi | MSCONS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_15001](/schnittstellen/202604/pruefi/QUOTES/PI_15001) | Prüfi | QUOTES | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_15003](/schnittstellen/202604/pruefi/QUOTES/PI_15003) | Prüfi | QUOTES | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_15004](/schnittstellen/202604/pruefi/QUOTES/PI_15004) | Prüfi | QUOTES | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17001](/schnittstellen/202604/pruefi/ORDERS/PI_17001) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17002](/schnittstellen/202604/pruefi/ORDERS/PI_17002) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17003](/schnittstellen/202604/pruefi/ORDERS/PI_17003) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17003](/schnittstellen/202604/pruefi/ORDERS/PI_17003) | Prüfi | ORDERS | transaktionsdaten › ansprechpartnerKunde › rufnummern |
| [PI_17004](/schnittstellen/202604/pruefi/ORDERS/PI_17004) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17005](/schnittstellen/202604/pruefi/ORDERS/PI_17005) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17006](/schnittstellen/202604/pruefi/ORDERS/PI_17006) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17009](/schnittstellen/202604/pruefi/ORDERS/PI_17009) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17101](/schnittstellen/202604/pruefi/ORDERS/PI_17101) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17102](/schnittstellen/202604/pruefi/ORDERS/PI_17102) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17103](/schnittstellen/202604/pruefi/ORDERS/PI_17103) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17104](/schnittstellen/202604/pruefi/ORDERS/PI_17104) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17113](/schnittstellen/202604/pruefi/ORDERS/PI_17113) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17115](/schnittstellen/202604/pruefi/ORDERS/PI_17115) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17116](/schnittstellen/202604/pruefi/ORDERS/PI_17116) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17117](/schnittstellen/202604/pruefi/ORDERS/PI_17117) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17118](/schnittstellen/202604/pruefi/ORDERS/PI_17118) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17120](/schnittstellen/202604/pruefi/ORDERS/PI_17120) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17121](/schnittstellen/202604/pruefi/ORDERS/PI_17121) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17122](/schnittstellen/202604/pruefi/ORDERS/PI_17122) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17123](/schnittstellen/202604/pruefi/ORDERS/PI_17123) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17126](/schnittstellen/202604/pruefi/ORDERS/PI_17126) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17128](/schnittstellen/202604/pruefi/ORDERS/PI_17128) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17129](/schnittstellen/202604/pruefi/ORDERS/PI_17129) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17130](/schnittstellen/202604/pruefi/ORDERS/PI_17130) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17131](/schnittstellen/202604/pruefi/ORDERS/PI_17131) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17132](/schnittstellen/202604/pruefi/ORDERS/PI_17132) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17133](/schnittstellen/202604/pruefi/ORDERS/PI_17133) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17134](/schnittstellen/202604/pruefi/ORDERS/PI_17134) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_17135](/schnittstellen/202604/pruefi/ORDERS/PI_17135) | Prüfi | ORDERS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19001](/schnittstellen/202604/pruefi/ORDRSP/PI_19001) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19002](/schnittstellen/202604/pruefi/ORDRSP/PI_19002) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19003](/schnittstellen/202604/pruefi/ORDRSP/PI_19003) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19004](/schnittstellen/202604/pruefi/ORDRSP/PI_19004) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19005](/schnittstellen/202604/pruefi/ORDRSP/PI_19005) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19006](/schnittstellen/202604/pruefi/ORDRSP/PI_19006) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19007](/schnittstellen/202604/pruefi/ORDRSP/PI_19007) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19009](/schnittstellen/202604/pruefi/ORDRSP/PI_19009) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19010](/schnittstellen/202604/pruefi/ORDRSP/PI_19010) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19011](/schnittstellen/202604/pruefi/ORDRSP/PI_19011) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19012](/schnittstellen/202604/pruefi/ORDRSP/PI_19012) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19013](/schnittstellen/202604/pruefi/ORDRSP/PI_19013) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19014](/schnittstellen/202604/pruefi/ORDRSP/PI_19014) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19015](/schnittstellen/202604/pruefi/ORDRSP/PI_19015) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19016](/schnittstellen/202604/pruefi/ORDRSP/PI_19016) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19101](/schnittstellen/202604/pruefi/ORDRSP/PI_19101) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19102](/schnittstellen/202604/pruefi/ORDRSP/PI_19102) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19103](/schnittstellen/202604/pruefi/ORDRSP/PI_19103) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19104](/schnittstellen/202604/pruefi/ORDRSP/PI_19104) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19114](/schnittstellen/202604/pruefi/ORDRSP/PI_19114) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19116](/schnittstellen/202604/pruefi/ORDRSP/PI_19116) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19117](/schnittstellen/202604/pruefi/ORDRSP/PI_19117) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19118](/schnittstellen/202604/pruefi/ORDRSP/PI_19118) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19119](/schnittstellen/202604/pruefi/ORDRSP/PI_19119) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19121](/schnittstellen/202604/pruefi/ORDRSP/PI_19121) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19123](/schnittstellen/202604/pruefi/ORDRSP/PI_19123) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19124](/schnittstellen/202604/pruefi/ORDRSP/PI_19124) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19128](/schnittstellen/202604/pruefi/ORDRSP/PI_19128) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19129](/schnittstellen/202604/pruefi/ORDRSP/PI_19129) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19133](/schnittstellen/202604/pruefi/ORDRSP/PI_19133) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19301](/schnittstellen/202604/pruefi/ORDRSP/PI_19301) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_19302](/schnittstellen/202604/pruefi/ORDRSP/PI_19302) | Prüfi | ORDRSP | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_21007](/schnittstellen/202604/pruefi/IFTSTA/PI_21007) | Prüfi | IFTSTA | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_21009](/schnittstellen/202604/pruefi/IFTSTA/PI_21009) | Prüfi | IFTSTA | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_21010](/schnittstellen/202604/pruefi/IFTSTA/PI_21010) | Prüfi | IFTSTA | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_21011](/schnittstellen/202604/pruefi/IFTSTA/PI_21011) | Prüfi | IFTSTA | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_21012](/schnittstellen/202604/pruefi/IFTSTA/PI_21012) | Prüfi | IFTSTA | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_21013](/schnittstellen/202604/pruefi/IFTSTA/PI_21013) | Prüfi | IFTSTA | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_21015](/schnittstellen/202604/pruefi/IFTSTA/PI_21015) | Prüfi | IFTSTA | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_21018](/schnittstellen/202604/pruefi/IFTSTA/PI_21018) | Prüfi | IFTSTA | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_21024](/schnittstellen/202604/pruefi/IFTSTA/PI_21024) | Prüfi | IFTSTA | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_21025](/schnittstellen/202604/pruefi/IFTSTA/PI_21025) | Prüfi | IFTSTA | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_21026](/schnittstellen/202604/pruefi/IFTSTA/PI_21026) | Prüfi | IFTSTA | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_21027](/schnittstellen/202604/pruefi/IFTSTA/PI_21027) | Prüfi | IFTSTA | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_21028](/schnittstellen/202604/pruefi/IFTSTA/PI_21028) | Prüfi | IFTSTA | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_21029](/schnittstellen/202604/pruefi/IFTSTA/PI_21029) | Prüfi | IFTSTA | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_21030](/schnittstellen/202604/pruefi/IFTSTA/PI_21030) | Prüfi | IFTSTA | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_21031](/schnittstellen/202604/pruefi/IFTSTA/PI_21031) | Prüfi | IFTSTA | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_21032](/schnittstellen/202604/pruefi/IFTSTA/PI_21032) | Prüfi | IFTSTA | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_21033](/schnittstellen/202604/pruefi/IFTSTA/PI_21033) | Prüfi | IFTSTA | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_21035](/schnittstellen/202604/pruefi/IFTSTA/PI_21035) | Prüfi | IFTSTA | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_21036](/schnittstellen/202604/pruefi/IFTSTA/PI_21036) | Prüfi | IFTSTA | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_21039](/schnittstellen/202604/pruefi/IFTSTA/PI_21039) | Prüfi | IFTSTA | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_21040](/schnittstellen/202604/pruefi/IFTSTA/PI_21040) | Prüfi | IFTSTA | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_21043](/schnittstellen/202604/pruefi/IFTSTA/PI_21043) | Prüfi | IFTSTA | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_21044](/schnittstellen/202604/pruefi/IFTSTA/PI_21044) | Prüfi | IFTSTA | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_21045](/schnittstellen/202604/pruefi/IFTSTA/PI_21045) | Prüfi | IFTSTA | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_21047](/schnittstellen/202604/pruefi/IFTSTA/PI_21047) | Prüfi | IFTSTA | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_23001](/schnittstellen/202604/pruefi/INSRPT/PI_23001) | Prüfi | INSRPT | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_23001](/schnittstellen/202604/pruefi/INSRPT/PI_23001) | Prüfi | INSRPT | transaktionsdaten › ansprechpartnerKunde › rufnummern |
| [PI_25001](/schnittstellen/202604/pruefi/UTILTS/PI_25001) | Prüfi | UTILTS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_25004](/schnittstellen/202604/pruefi/UTILTS/PI_25004) | Prüfi | UTILTS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_25005](/schnittstellen/202604/pruefi/UTILTS/PI_25005) | Prüfi | UTILTS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_25006](/schnittstellen/202604/pruefi/UTILTS/PI_25006) | Prüfi | UTILTS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_25007](/schnittstellen/202604/pruefi/UTILTS/PI_25007) | Prüfi | UTILTS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_25008](/schnittstellen/202604/pruefi/UTILTS/PI_25008) | Prüfi | UTILTS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_25009](/schnittstellen/202604/pruefi/UTILTS/PI_25009) | Prüfi | UTILTS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_25010](/schnittstellen/202604/pruefi/UTILTS/PI_25010) | Prüfi | UTILTS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_27002](/schnittstellen/202604/pruefi/PRICAT/PI_27002) | Prüfi | PRICAT | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_27003](/schnittstellen/202604/pruefi/PRICAT/PI_27003) | Prüfi | PRICAT | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_29001](/schnittstellen/202604/pruefi/COMDIS/PI_29001) | Prüfi | COMDIS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_29002](/schnittstellen/202604/pruefi/COMDIS/PI_29002) | Prüfi | COMDIS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_33001](/schnittstellen/202604/pruefi/REMADV/PI_33001) | Prüfi | REMADV | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_33002](/schnittstellen/202604/pruefi/REMADV/PI_33002) | Prüfi | REMADV | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_33003](/schnittstellen/202604/pruefi/REMADV/PI_33003) | Prüfi | REMADV | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_33004](/schnittstellen/202604/pruefi/REMADV/PI_33004) | Prüfi | REMADV | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_35001](/schnittstellen/202604/pruefi/REQOTE/PI_35001) | Prüfi | REQOTE | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_35002](/schnittstellen/202604/pruefi/REQOTE/PI_35002) | Prüfi | REQOTE | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_35004](/schnittstellen/202604/pruefi/REQOTE/PI_35004) | Prüfi | REQOTE | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_37000](/schnittstellen/202604/pruefi/PARTIN/PI_37000) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben › ansprechpartner › rufnummern |
| [PI_37000](/schnittstellen/202604/pruefi/PARTIN/PI_37000) | Prüfi | PARTIN | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_37001](/schnittstellen/202604/pruefi/PARTIN/PI_37001) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben › ansprechpartner › rufnummern |
| [PI_37001](/schnittstellen/202604/pruefi/PARTIN/PI_37001) | Prüfi | PARTIN | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_37002](/schnittstellen/202604/pruefi/PARTIN/PI_37002) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben › ansprechpartner › rufnummern |
| [PI_37002](/schnittstellen/202604/pruefi/PARTIN/PI_37002) | Prüfi | PARTIN | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_37008](/schnittstellen/202604/pruefi/PARTIN/PI_37008) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben › ansprechpartner › rufnummern |
| [PI_37008](/schnittstellen/202604/pruefi/PARTIN/PI_37008) | Prüfi | PARTIN | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_37009](/schnittstellen/202604/pruefi/PARTIN/PI_37009) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben › ansprechpartner › rufnummern |
| [PI_37009](/schnittstellen/202604/pruefi/PARTIN/PI_37009) | Prüfi | PARTIN | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_37010](/schnittstellen/202604/pruefi/PARTIN/PI_37010) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben › ansprechpartner › rufnummern |
| [PI_37010](/schnittstellen/202604/pruefi/PARTIN/PI_37010) | Prüfi | PARTIN | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_37012](/schnittstellen/202604/pruefi/PARTIN/PI_37012) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben › ansprechpartner › rufnummern |
| [PI_37012](/schnittstellen/202604/pruefi/PARTIN/PI_37012) | Prüfi | PARTIN | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_37013](/schnittstellen/202604/pruefi/PARTIN/PI_37013) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben › ansprechpartner › rufnummern |
| [PI_37013](/schnittstellen/202604/pruefi/PARTIN/PI_37013) | Prüfi | PARTIN | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_37014](/schnittstellen/202604/pruefi/PARTIN/PI_37014) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › kommunikationsangaben › ansprechpartner › rufnummern |
| [PI_37014](/schnittstellen/202604/pruefi/PARTIN/PI_37014) | Prüfi | PARTIN | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_39000](/schnittstellen/202604/pruefi/ORDCHG/PI_39000) | Prüfi | ORDCHG | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_39001](/schnittstellen/202604/pruefi/ORDCHG/PI_39001) | Prüfi | ORDCHG | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44001](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44001) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44003](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44003) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44004](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44004) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44005](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44005) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44006](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44006) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44007](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44007) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44008](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44008) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44009](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44009) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44010](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44010) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44011](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44011) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44012](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44012) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44015](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44015) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44016](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44016) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44017](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44017) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44018](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44018) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44019](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44019) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44020](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44020) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44021](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44021) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44022](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44022) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44023](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44023) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44024](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44024) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44035](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44035) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44036](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44036) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44037](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44037) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44038](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44038) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44039](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44039) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44040](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44040) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44041](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44041) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44043](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44043) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44044](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44044) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44052](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44052) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44053](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44053) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44060](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44060) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44101](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44101) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44102](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44102) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44103](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44103) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44104](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44104) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44109](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44109) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44111](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44111) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44112](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44112) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44113](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44113) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44115](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44115) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44116](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44116) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44117](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44117) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44119](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44119) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44120](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44120) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44121](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44121) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44123](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44123) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44124](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44124) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44137](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44137) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44138](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44138) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44139](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44139) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44140](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44140) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44142](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44142) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44143](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44143) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44145](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44145) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44146](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44146) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44147](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44147) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44148](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44148) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44149](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44149) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44150](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44150) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44151](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44151) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44152](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44152) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44156](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44156) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44157](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44157) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44159](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44159) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44160](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44160) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44161](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44161) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44162](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44162) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44163](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44163) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44164](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44164) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44165](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44165) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44166](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44166) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44167](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44167) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44168](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44175](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44175) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44176](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44176) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44180](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44180) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44181](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44181) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_44182](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44182) | Prüfi | UTILMD_GAS | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55001](/schnittstellen/202604/pruefi/UTILMD/PI_55001) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55002](/schnittstellen/202604/pruefi/UTILMD/PI_55002) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55003](/schnittstellen/202604/pruefi/UTILMD/PI_55003) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55004](/schnittstellen/202604/pruefi/UTILMD/PI_55004) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55005](/schnittstellen/202604/pruefi/UTILMD/PI_55005) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55006](/schnittstellen/202604/pruefi/UTILMD/PI_55006) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55007](/schnittstellen/202604/pruefi/UTILMD/PI_55007) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55008](/schnittstellen/202604/pruefi/UTILMD/PI_55008) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55009](/schnittstellen/202604/pruefi/UTILMD/PI_55009) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55010](/schnittstellen/202604/pruefi/UTILMD/PI_55010) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55011](/schnittstellen/202604/pruefi/UTILMD/PI_55011) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55012](/schnittstellen/202604/pruefi/UTILMD/PI_55012) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55013](/schnittstellen/202604/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55014](/schnittstellen/202604/pruefi/UTILMD/PI_55014) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55015](/schnittstellen/202604/pruefi/UTILMD/PI_55015) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55016](/schnittstellen/202604/pruefi/UTILMD/PI_55016) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55017](/schnittstellen/202604/pruefi/UTILMD/PI_55017) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55018](/schnittstellen/202604/pruefi/UTILMD/PI_55018) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55022](/schnittstellen/202604/pruefi/UTILMD/PI_55022) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55023](/schnittstellen/202604/pruefi/UTILMD/PI_55023) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55024](/schnittstellen/202604/pruefi/UTILMD/PI_55024) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55035](/schnittstellen/202604/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55036](/schnittstellen/202604/pruefi/UTILMD/PI_55036) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55037](/schnittstellen/202604/pruefi/UTILMD/PI_55037) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55038](/schnittstellen/202604/pruefi/UTILMD/PI_55038) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55039](/schnittstellen/202604/pruefi/UTILMD/PI_55039) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55040](/schnittstellen/202604/pruefi/UTILMD/PI_55040) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55041](/schnittstellen/202604/pruefi/UTILMD/PI_55041) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55042](/schnittstellen/202604/pruefi/UTILMD/PI_55042) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55044](/schnittstellen/202604/pruefi/UTILMD/PI_55044) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55051](/schnittstellen/202604/pruefi/UTILMD/PI_55051) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55052](/schnittstellen/202604/pruefi/UTILMD/PI_55052) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55053](/schnittstellen/202604/pruefi/UTILMD/PI_55053) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55060](/schnittstellen/202604/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55074](/schnittstellen/202604/pruefi/UTILMD/PI_55074) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55075](/schnittstellen/202604/pruefi/UTILMD/PI_55075) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55077](/schnittstellen/202604/pruefi/UTILMD/PI_55077) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55078](/schnittstellen/202604/pruefi/UTILMD/PI_55078) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55080](/schnittstellen/202604/pruefi/UTILMD/PI_55080) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55095](/schnittstellen/202604/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55109](/schnittstellen/202604/pruefi/UTILMD/PI_55109) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55110](/schnittstellen/202604/pruefi/UTILMD/PI_55110) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55126](/schnittstellen/202604/pruefi/UTILMD/PI_55126) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55136](/schnittstellen/202604/pruefi/UTILMD/PI_55136) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55137](/schnittstellen/202604/pruefi/UTILMD/PI_55137) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55156](/schnittstellen/202604/pruefi/UTILMD/PI_55156) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55170](/schnittstellen/202604/pruefi/UTILMD/PI_55170) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55173](/schnittstellen/202604/pruefi/UTILMD/PI_55173) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55175](/schnittstellen/202604/pruefi/UTILMD/PI_55175) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55177](/schnittstellen/202604/pruefi/UTILMD/PI_55177) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55180](/schnittstellen/202604/pruefi/UTILMD/PI_55180) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55194](/schnittstellen/202604/pruefi/UTILMD/PI_55194) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55218](/schnittstellen/202604/pruefi/UTILMD/PI_55218) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55220](/schnittstellen/202604/pruefi/UTILMD/PI_55220) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55225](/schnittstellen/202604/pruefi/UTILMD/PI_55225) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55227](/schnittstellen/202604/pruefi/UTILMD/PI_55227) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55230](/schnittstellen/202604/pruefi/UTILMD/PI_55230) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55232](/schnittstellen/202604/pruefi/UTILMD/PI_55232) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55553](/schnittstellen/202604/pruefi/UTILMD/PI_55553) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55555](/schnittstellen/202604/pruefi/UTILMD/PI_55555) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55557](/schnittstellen/202604/pruefi/UTILMD/PI_55557) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55559](/schnittstellen/202604/pruefi/UTILMD/PI_55559) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55600](/schnittstellen/202604/pruefi/UTILMD/PI_55600) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55601](/schnittstellen/202604/pruefi/UTILMD/PI_55601) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55602](/schnittstellen/202604/pruefi/UTILMD/PI_55602) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55603](/schnittstellen/202604/pruefi/UTILMD/PI_55603) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55604](/schnittstellen/202604/pruefi/UTILMD/PI_55604) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55605](/schnittstellen/202604/pruefi/UTILMD/PI_55605) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55607](/schnittstellen/202604/pruefi/UTILMD/PI_55607) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55608](/schnittstellen/202604/pruefi/UTILMD/PI_55608) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55609](/schnittstellen/202604/pruefi/UTILMD/PI_55609) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55611](/schnittstellen/202604/pruefi/UTILMD/PI_55611) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55613](/schnittstellen/202604/pruefi/UTILMD/PI_55613) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55614](/schnittstellen/202604/pruefi/UTILMD/PI_55614) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55615](/schnittstellen/202604/pruefi/UTILMD/PI_55615) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55616](/schnittstellen/202604/pruefi/UTILMD/PI_55616) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55617](/schnittstellen/202604/pruefi/UTILMD/PI_55617) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55618](/schnittstellen/202604/pruefi/UTILMD/PI_55618) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55619](/schnittstellen/202604/pruefi/UTILMD/PI_55619) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55620](/schnittstellen/202604/pruefi/UTILMD/PI_55620) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55621](/schnittstellen/202604/pruefi/UTILMD/PI_55621) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55622](/schnittstellen/202604/pruefi/UTILMD/PI_55622) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55623](/schnittstellen/202604/pruefi/UTILMD/PI_55623) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55624](/schnittstellen/202604/pruefi/UTILMD/PI_55624) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55625](/schnittstellen/202604/pruefi/UTILMD/PI_55625) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55626](/schnittstellen/202604/pruefi/UTILMD/PI_55626) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55627](/schnittstellen/202604/pruefi/UTILMD/PI_55627) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55628](/schnittstellen/202604/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55629](/schnittstellen/202604/pruefi/UTILMD/PI_55629) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55630](/schnittstellen/202604/pruefi/UTILMD/PI_55630) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55632](/schnittstellen/202604/pruefi/UTILMD/PI_55632) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55633](/schnittstellen/202604/pruefi/UTILMD/PI_55633) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55634](/schnittstellen/202604/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55635](/schnittstellen/202604/pruefi/UTILMD/PI_55635) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55636](/schnittstellen/202604/pruefi/UTILMD/PI_55636) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55638](/schnittstellen/202604/pruefi/UTILMD/PI_55638) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55639](/schnittstellen/202604/pruefi/UTILMD/PI_55639) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55640](/schnittstellen/202604/pruefi/UTILMD/PI_55640) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55641](/schnittstellen/202604/pruefi/UTILMD/PI_55641) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55642](/schnittstellen/202604/pruefi/UTILMD/PI_55642) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55643](/schnittstellen/202604/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55644](/schnittstellen/202604/pruefi/UTILMD/PI_55644) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55645](/schnittstellen/202604/pruefi/UTILMD/PI_55645) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55646](/schnittstellen/202604/pruefi/UTILMD/PI_55646) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55647](/schnittstellen/202604/pruefi/UTILMD/PI_55647) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55648](/schnittstellen/202604/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55649](/schnittstellen/202604/pruefi/UTILMD/PI_55649) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55650](/schnittstellen/202604/pruefi/UTILMD/PI_55650) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55651](/schnittstellen/202604/pruefi/UTILMD/PI_55651) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55652](/schnittstellen/202604/pruefi/UTILMD/PI_55652) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55653](/schnittstellen/202604/pruefi/UTILMD/PI_55653) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55654](/schnittstellen/202604/pruefi/UTILMD/PI_55654) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55655](/schnittstellen/202604/pruefi/UTILMD/PI_55655) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55656](/schnittstellen/202604/pruefi/UTILMD/PI_55656) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55657](/schnittstellen/202604/pruefi/UTILMD/PI_55657) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55658](/schnittstellen/202604/pruefi/UTILMD/PI_55658) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55659](/schnittstellen/202604/pruefi/UTILMD/PI_55659) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55660](/schnittstellen/202604/pruefi/UTILMD/PI_55660) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55661](/schnittstellen/202604/pruefi/UTILMD/PI_55661) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55662](/schnittstellen/202604/pruefi/UTILMD/PI_55662) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55663](/schnittstellen/202604/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55664](/schnittstellen/202604/pruefi/UTILMD/PI_55664) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55665](/schnittstellen/202604/pruefi/UTILMD/PI_55665) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55666](/schnittstellen/202604/pruefi/UTILMD/PI_55666) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55667](/schnittstellen/202604/pruefi/UTILMD/PI_55667) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55669](/schnittstellen/202604/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55670](/schnittstellen/202604/pruefi/UTILMD/PI_55670) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55672](/schnittstellen/202604/pruefi/UTILMD/PI_55672) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55673](/schnittstellen/202604/pruefi/UTILMD/PI_55673) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55674](/schnittstellen/202604/pruefi/UTILMD/PI_55674) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55684](/schnittstellen/202604/pruefi/UTILMD/PI_55684) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55686](/schnittstellen/202604/pruefi/UTILMD/PI_55686) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55688](/schnittstellen/202604/pruefi/UTILMD/PI_55688) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55690](/schnittstellen/202604/pruefi/UTILMD/PI_55690) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55691](/schnittstellen/202604/pruefi/UTILMD/PI_55691) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_55692](/schnittstellen/202604/pruefi/UTILMD/PI_55692) | Prüfi | UTILMD | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_66666](/schnittstellen/202604/pruefi/APERAK/PI_66666) | Prüfi | APERAK | transaktionsdaten › absender › ansprechpartner › rufnummern |
| [PI_99999](/schnittstellen/202604/pruefi/APERAK/PI_99999) | Prüfi | APERAK | transaktionsdaten › absender › ansprechpartner › rufnummern |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
