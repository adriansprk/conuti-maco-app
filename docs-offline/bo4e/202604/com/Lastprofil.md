# Lastprofil
<span hidden data-pagefind-meta={"title:Lastprofil — BO4E-Komponente (FV 202604)"} />

BO4E-Komponente · 13 Felder · 105 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="bezeichnung"></a>`bezeichnung` | string | Bezeichnung des Profils |
| <a id="verfahren"></a>`verfahren` | [Enum Profilverfahren](/bo4e/202604/enum/Profilverfahren)<br/><Werte>`SYNTHETISCH`, `ANALYTISCH`</Werte> | Profilverfahren |
| <a id="profilart"></a>`profilart` | [Enum Profilart](/bo4e/202604/enum/Profilart)<br/><Werte>`ART_STANDARDLASTPROFIL`, `ART_TAGESPARAMETERABHAENGIGES_LASTPROFIL`, `ART_LASTPROFIL`</Werte> | Profilart |
| <a id="profilschar"></a>`profilschar` | string | Profilschar des Profils |
| <a id="einspeisung"></a>`einspeisung` | boolean | Kennzeichen Einspeisung |
| <a id="herausgeber"></a>`herausgeber` | string | Herausgeber des Lastprofils |
| <a id="tagesparameter"></a>`tagesparameter` | [Tagesparameter](/bo4e/202604/com/Tagesparameter) | — |
| <a id="referenzprofilbezeichnung"></a>`referenzprofilbezeichnung` | string | Bezeichnung des Referenzprofils |
| <a id="referenzprofil"></a>`referenzprofil` | string | Referenzprofil |
| <a id="profiltyp"></a>`profiltyp` | [Enum Profiltyp](/bo4e/202604/enum/Profiltyp)<br/><Werte>`SLP_SEP`, `TLP_TEP`, `TEP`, `GEWERBE_ALLGEMEIN`, `GEWERBE_WERKTAGS_8_18_UHR`, `GEWERBE_MIT_STARKEM_BIS_UEBERWIEGENDEM_VERBRAUCH_IN_DEN_ABENDSTUNDEN`, `GEWERBE_DURCHLAUFEND`, `GEWERBE_LADEN_FRISEUR`, `GEWERBE_BAECKEREI_MIT_BACKSTUBE`, `GEWERBE_WOCHENENDBETRIEB`, `LANDWIRTSCHAFTSBETRIEBE_ALLGEMEIN`, `LANDWIRTSCHAFTSBETRIEBE_MIT_MILCHWIRTSCHAFT_NEBENERWERBS_TIERZUCHT`, `LANDWIRTSCHAFT_OHNE_MILCHVIEH`, `HAUSHALT`, `BANDLAST`, `UNTERBRECHBARE_VERBRAUCHSEINRICHTUNG`, `HEIZWAERMESPEICHER`, `STRASSENBELEUCHTUNG`, `PHOTOVOLTAIK_MARKTLOKATION`, `BLOCKHEIZKRAFTWERK`, `SONSTIGE_VERBRAUCHENDE_MARKTLOKATION`, `SONSTIGE_ERZEUGENDE_MARKTLOKATION`, `E_MOBILITAET_LADEPUNKT_IM_OEFFENTLICHEN_BEREICH`, `E_MOBILITAET_LADEPUNKT_EINES_HAUSHALTS`, `E_MOBILITAET_LADEPUNKT_EINES_GEWERBES`</Werte> | Profiltyp |
| <a id="normierungsfaktor"></a>`normierungsfaktor` | [Enum Normierungsfaktor](/bo4e/202604/enum/Normierungsfaktor)<br/><Werte>`NORMIERUNGSFAKTOR_1_000_000_KWH_A`, `NORMIERUNGSFAKTOR_300_KWH_K`, `NORMIERUNGSFAKTOR_1_000_000_KW`</Werte> | Normierungsfaktor |
| <a id="tagesmitteltemperatur"></a>`tagesmitteltemperatur` | [Tagesmitteltemperatur](/bo4e/202604/com/Tagesmitteltemperatur) | — |
| <a id="begrenzungskonstante"></a>`begrenzungskonstante` | [Enum Begrenzungskonstante](/bo4e/202604/enum/Begrenzungskonstante)<br/><Werte>`BEGRENZUNGSKONSTANTE_0`, `BEGRENZUNGSKONSTANTE_1`</Werte> | Begrenzungskonstante |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[bezeichnung](/bo4e/202604/com/Lastprofil#bezeichnung)</span> | Bezeichnung des Profils | string |
| <span className="hbs-f hbs-e0">[verfahren](/bo4e/202604/com/Lastprofil#verfahren)</span> | Profilverfahren | [Enum Profilverfahren](/bo4e/202604/enum/Profilverfahren)<br/><Werte>`SYNTHETISCH`, `ANALYTISCH`</Werte> |
| <span className="hbs-f hbs-e0">[profilart](/bo4e/202604/com/Lastprofil#profilart)</span> | Profilart | [Enum Profilart](/bo4e/202604/enum/Profilart)<br/><Werte>`ART_STANDARDLASTPROFIL`, `ART_TAGESPARAMETERABHAENGIGES_LASTPROFIL`, `ART_LASTPROFIL`</Werte> |
| <span className="hbs-f hbs-e0">[profilschar](/bo4e/202604/com/Lastprofil#profilschar)</span> | Profilschar des Profils | string |
| <span className="hbs-f hbs-e0">[einspeisung](/bo4e/202604/com/Lastprofil#einspeisung)</span> | Kennzeichen Einspeisung | boolean |
| <span className="hbs-f hbs-e0">[herausgeber](/bo4e/202604/com/Lastprofil#herausgeber)</span> | Herausgeber des Lastprofils | string |
| <span className="hbs-g hbs-e0">[tagesparameter](/bo4e/202604/com/Lastprofil#tagesparameter)</span> | — | [Tagesparameter](/bo4e/202604/com/Tagesparameter) |
| <span className="hbs-f hbs-e1">[klimazone](/bo4e/202604/com/Tagesparameter#klimazone)</span> | klimazone | string |
| <span className="hbs-f hbs-e1">[temperaturmessstelle](/bo4e/202604/com/Tagesparameter#temperaturmessstelle)</span> | temperaturmessstelle | string |
| <span className="hbs-f hbs-e1">[dienstanbieter](/bo4e/202604/com/Tagesparameter#dienstanbieter)</span> | dienstanbieter | string |
| <span className="hbs-f hbs-e1">[herausgeber](/bo4e/202604/com/Tagesparameter#herausgeber)</span> | Herausgeber | [Enum Herausgeber](/bo4e/202604/enum/Herausgeber)<br/><Werte>`NB`, `BDEW`, `TUM`</Werte> |
| <span className="hbs-f hbs-e0">[referenzprofilbezeichnung](/bo4e/202604/com/Lastprofil#referenzprofilbezeichnung)</span> | Bezeichnung des Referenzprofils | string |
| <span className="hbs-f hbs-e0">[referenzprofil](/bo4e/202604/com/Lastprofil#referenzprofil)</span> | Referenzprofil | string |
| <span className="hbs-f hbs-e0">[profiltyp](/bo4e/202604/com/Lastprofil#profiltyp)</span> | Profiltyp | [Enum Profiltyp](/bo4e/202604/enum/Profiltyp)<br/><Werte>`SLP_SEP`, `TLP_TEP`, `TEP`, `GEWERBE_ALLGEMEIN`, `GEWERBE_WERKTAGS_8_18_UHR`, `GEWERBE_MIT_STARKEM_BIS_UEBERWIEGENDEM_VERBRAUCH_IN_DEN_ABENDSTUNDEN`, `GEWERBE_DURCHLAUFEND`, `GEWERBE_LADEN_FRISEUR`, `GEWERBE_BAECKEREI_MIT_BACKSTUBE`, `GEWERBE_WOCHENENDBETRIEB`, `LANDWIRTSCHAFTSBETRIEBE_ALLGEMEIN`, `LANDWIRTSCHAFTSBETRIEBE_MIT_MILCHWIRTSCHAFT_NEBENERWERBS_TIERZUCHT`, `LANDWIRTSCHAFT_OHNE_MILCHVIEH`, `HAUSHALT`, `BANDLAST`, `UNTERBRECHBARE_VERBRAUCHSEINRICHTUNG`, `HEIZWAERMESPEICHER`, `STRASSENBELEUCHTUNG`, `PHOTOVOLTAIK_MARKTLOKATION`, `BLOCKHEIZKRAFTWERK`, `SONSTIGE_VERBRAUCHENDE_MARKTLOKATION`, `SONSTIGE_ERZEUGENDE_MARKTLOKATION`, `E_MOBILITAET_LADEPUNKT_IM_OEFFENTLICHEN_BEREICH`, `E_MOBILITAET_LADEPUNKT_EINES_HAUSHALTS`, `E_MOBILITAET_LADEPUNKT_EINES_GEWERBES`</Werte> |
| <span className="hbs-f hbs-e0">[normierungsfaktor](/bo4e/202604/com/Lastprofil#normierungsfaktor)</span> | Normierungsfaktor | [Enum Normierungsfaktor](/bo4e/202604/enum/Normierungsfaktor)<br/><Werte>`NORMIERUNGSFAKTOR_1_000_000_KWH_A`, `NORMIERUNGSFAKTOR_300_KWH_K`, `NORMIERUNGSFAKTOR_1_000_000_KW`</Werte> |
| <span className="hbs-g hbs-e0">[tagesmitteltemperatur](/bo4e/202604/com/Lastprofil#tagesmitteltemperatur)</span> | — | [Tagesmitteltemperatur](/bo4e/202604/com/Tagesmitteltemperatur) |
| <span className="hbs-f hbs-e1">[berechnungTagesmitteltemperatur](/bo4e/202604/com/Tagesmitteltemperatur#berechnungtagesmitteltemperatur)</span> | Berechnungsmethode | [Enum Berechnungsmethode](/bo4e/202604/enum/Berechnungsmethode)<br/><Werte>`24H_MITTELWERT`, `VOM_ANBIETER_ZUR_VERFUEGUNG_GESTELLTE_AEQUIVALENTE_TAGESMITTELTEMPERATUR`, `AEQUIVALENTE_TAGESMITTELTEMPERATUR`</Werte> |
| <span className="hbs-f hbs-e1">[anteilA](/bo4e/202604/com/Tagesmitteltemperatur#anteila)</span> | Anteil A | number (float) |
| <span className="hbs-f hbs-e1">[anteilB](/bo4e/202604/com/Tagesmitteltemperatur#anteilb)</span> | Anteil B | number (float) |
| <span className="hbs-f hbs-e1">[anteilC](/bo4e/202604/com/Tagesmitteltemperatur#anteilc)</span> | Anteil C | number (float) |
| <span className="hbs-f hbs-e1">[anteilD](/bo4e/202604/com/Tagesmitteltemperatur#anteild)</span> | Anteil D | number (float) |
| <span className="hbs-f hbs-e1">[begrenzungstemperatur](/bo4e/202604/com/Tagesmitteltemperatur#begrenzungstemperatur)</span> | Begrenzungstemperatur | string |
| <span className="hbs-f hbs-e0">[begrenzungskonstante](/bo4e/202604/com/Lastprofil#begrenzungskonstante)</span> | Begrenzungskonstante | [Enum Begrenzungskonstante](/bo4e/202604/enum/Begrenzungskonstante)<br/><Werte>`BEGRENZUNGSKONSTANTE_0`, `BEGRENZUNGSKONSTANTE_1`</Werte> |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### bezeichnung

26 Verwendung(en) in den Nachrichtentypen UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_44001](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44001) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › lastprofile |
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › lastprofile |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › lastprofile |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › lastprofile |
| [PI_44019](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44019) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › lastprofile |
| [PI_44020](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44020) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › lastprofile |
| [PI_44021](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44021) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › lastprofile |
| [PI_44035](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44035) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › lastprofile |
| [PI_44103](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44103) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › lastprofile |
| [PI_44104](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44104) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › lastprofile |
| [PI_44123](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44123) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › lastprofile |
| [PI_44156](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44156) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › lastprofile |
| [PI_44157](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44157) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55035](/schnittstellen/202604/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55095](/schnittstellen/202604/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55126](/schnittstellen/202604/pruefi/UTILMD/PI_55126) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55156](/schnittstellen/202604/pruefi/UTILMD/PI_55156) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55613](/schnittstellen/202604/pruefi/UTILMD/PI_55613) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55614](/schnittstellen/202604/pruefi/UTILMD/PI_55614) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55628](/schnittstellen/202604/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55634](/schnittstellen/202604/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55672](/schnittstellen/202604/pruefi/UTILMD/PI_55672) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55673](/schnittstellen/202604/pruefi/UTILMD/PI_55673) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |

### verfahren

26 Verwendung(en) in den Nachrichtentypen UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_44001](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44001) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › lastprofile |
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › lastprofile |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › lastprofile |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › lastprofile |
| [PI_44019](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44019) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › lastprofile |
| [PI_44020](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44020) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › lastprofile |
| [PI_44021](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44021) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › lastprofile |
| [PI_44035](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44035) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › lastprofile |
| [PI_44103](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44103) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › lastprofile |
| [PI_44104](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44104) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › lastprofile |
| [PI_44123](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44123) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › lastprofile |
| [PI_44156](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44156) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › lastprofile |
| [PI_44157](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44157) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55035](/schnittstellen/202604/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55095](/schnittstellen/202604/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55126](/schnittstellen/202604/pruefi/UTILMD/PI_55126) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55156](/schnittstellen/202604/pruefi/UTILMD/PI_55156) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55613](/schnittstellen/202604/pruefi/UTILMD/PI_55613) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55614](/schnittstellen/202604/pruefi/UTILMD/PI_55614) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55628](/schnittstellen/202604/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55634](/schnittstellen/202604/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55672](/schnittstellen/202604/pruefi/UTILMD/PI_55672) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55673](/schnittstellen/202604/pruefi/UTILMD/PI_55673) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |

### profilart

13 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55035](/schnittstellen/202604/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55095](/schnittstellen/202604/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55126](/schnittstellen/202604/pruefi/UTILMD/PI_55126) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55156](/schnittstellen/202604/pruefi/UTILMD/PI_55156) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55613](/schnittstellen/202604/pruefi/UTILMD/PI_55613) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55614](/schnittstellen/202604/pruefi/UTILMD/PI_55614) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55628](/schnittstellen/202604/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55634](/schnittstellen/202604/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55672](/schnittstellen/202604/pruefi/UTILMD/PI_55672) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55673](/schnittstellen/202604/pruefi/UTILMD/PI_55673) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |

### profilschar

6 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55035](/schnittstellen/202604/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55095](/schnittstellen/202604/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55126](/schnittstellen/202604/pruefi/UTILMD/PI_55126) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55156](/schnittstellen/202604/pruefi/UTILMD/PI_55156) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55672](/schnittstellen/202604/pruefi/UTILMD/PI_55672) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55673](/schnittstellen/202604/pruefi/UTILMD/PI_55673) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |

### einspeisung

13 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55035](/schnittstellen/202604/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55095](/schnittstellen/202604/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55126](/schnittstellen/202604/pruefi/UTILMD/PI_55126) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55156](/schnittstellen/202604/pruefi/UTILMD/PI_55156) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55613](/schnittstellen/202604/pruefi/UTILMD/PI_55613) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55614](/schnittstellen/202604/pruefi/UTILMD/PI_55614) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55628](/schnittstellen/202604/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55634](/schnittstellen/202604/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55672](/schnittstellen/202604/pruefi/UTILMD/PI_55672) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55673](/schnittstellen/202604/pruefi/UTILMD/PI_55673) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |

### herausgeber

13 Verwendung(en) in den Nachrichtentypen UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_44001](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44001) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › lastprofile |
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › lastprofile |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › lastprofile |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › lastprofile |
| [PI_44019](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44019) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › lastprofile |
| [PI_44020](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44020) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › lastprofile |
| [PI_44021](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44021) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › lastprofile |
| [PI_44035](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44035) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › lastprofile |
| [PI_44103](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44103) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › lastprofile |
| [PI_44104](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44104) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › lastprofile |
| [PI_44123](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44123) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › lastprofile |
| [PI_44156](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44156) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › lastprofile |
| [PI_44157](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44157) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › lastprofile |

### referenzprofilbezeichnung

8 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55095](/schnittstellen/202604/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55628](/schnittstellen/202604/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55634](/schnittstellen/202604/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55672](/schnittstellen/202604/pruefi/UTILMD/PI_55672) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |
| [PI_55673](/schnittstellen/202604/pruefi/UTILMD/PI_55673) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › lastprofile |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
