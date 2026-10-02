# Datenstand
<span hidden data-pagefind-meta={"title:Datenstand — BO4E-Komponente (FV 202604)"} />

BO4E-Komponente · 7 Felder · 0 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="jahresverbrauchsprognose"></a>`jahresverbrauchsprognose` | [Menge](/bo4e/202604/com/Menge) | — |
| <a id="tatsaechlichbilanzierteenergiemenge"></a>`tatsaechlichBilanzierteEnergiemenge` | [Menge](/bo4e/202604/com/Menge) | — |
| <a id="zubilanzierendeenergiemenge"></a>`zuBilanzierendeEnergiemenge` | [Menge](/bo4e/202604/com/Menge) | — |
| <a id="bilanzkreis"></a>`bilanzkreis` | string | Bilanzkreis |
| <a id="bilanzierungsgebiet"></a>`bilanzierungsgebiet` | string | Bilanzierungsgebiet |
| <a id="lastprofile"></a>`lastprofile` | [Lastprofil[]](/bo4e/202604/com/Lastprofil) | Eine Liste der verwendeten Lastprofile (SLP, SLP/TLP, ALP etc.) |
| <a id="aggregationsverantwortung"></a>`aggregationsverantwortung` | [Enum Aggregationsverantwortung](/bo4e/202604/enum/Aggregationsverantwortung)<br/><Werte>`UENB`, `VNB`</Werte> | Aggregationsverantwortung |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-g hbs-e0">[jahresverbrauchsprognose](/bo4e/202604/com/Datenstand#jahresverbrauchsprognose)</span> | — | [Menge](/bo4e/202604/com/Menge) |
| <span className="hbs-f hbs-e1">[wert](/bo4e/202604/com/Menge#wert)</span> | Wert | number (float) |
| <span className="hbs-f hbs-e1">[einheit](/bo4e/202604/com/Menge#einheit)</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202604/enum/Mengeneinheit)<br/><Werte>`W`, `WH`, `KW`, `KWH`, `KVARH`, `MW`, `MWH`, `STUECK`, `KUBIKMETER`, `STUNDE`, `TAG`, `MONAT`, `JAHR`, `PROZENT`, `ANZAHL`, `VAR`, `KVAR`, `VARH`, `KWHK`, `Z16`, `KWT`, `WATT_PRO_QUADRATMETER`, `METER_PRO_SEKUNDE`</Werte> |
| <span className="hbs-f hbs-e1">[startdatum](/bo4e/202604/com/Menge#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e1">[enddatum](/bo4e/202604/com/Menge#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-g hbs-e0">[tatsaechlichBilanzierteEnergiemenge](/bo4e/202604/com/Datenstand#tatsaechlichbilanzierteenergiemenge)</span> | — | [Menge](/bo4e/202604/com/Menge) |
| <span className="hbs-f hbs-e1">[wert](/bo4e/202604/com/Menge#wert)</span> | Wert | number (float) |
| <span className="hbs-f hbs-e1">[einheit](/bo4e/202604/com/Menge#einheit)</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202604/enum/Mengeneinheit)<br/><Werte>`W`, `WH`, `KW`, `KWH`, `KVARH`, `MW`, `MWH`, `STUECK`, `KUBIKMETER`, `STUNDE`, `TAG`, `MONAT`, `JAHR`, `PROZENT`, `ANZAHL`, `VAR`, `KVAR`, `VARH`, `KWHK`, `Z16`, `KWT`, `WATT_PRO_QUADRATMETER`, `METER_PRO_SEKUNDE`</Werte> |
| <span className="hbs-f hbs-e1">[startdatum](/bo4e/202604/com/Menge#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e1">[enddatum](/bo4e/202604/com/Menge#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-g hbs-e0">[zuBilanzierendeEnergiemenge](/bo4e/202604/com/Datenstand#zubilanzierendeenergiemenge)</span> | — | [Menge](/bo4e/202604/com/Menge) |
| <span className="hbs-f hbs-e1">[wert](/bo4e/202604/com/Menge#wert)</span> | Wert | number (float) |
| <span className="hbs-f hbs-e1">[einheit](/bo4e/202604/com/Menge#einheit)</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202604/enum/Mengeneinheit)<br/><Werte>`W`, `WH`, `KW`, `KWH`, `KVARH`, `MW`, `MWH`, `STUECK`, `KUBIKMETER`, `STUNDE`, `TAG`, `MONAT`, `JAHR`, `PROZENT`, `ANZAHL`, `VAR`, `KVAR`, `VARH`, `KWHK`, `Z16`, `KWT`, `WATT_PRO_QUADRATMETER`, `METER_PRO_SEKUNDE`</Werte> |
| <span className="hbs-f hbs-e1">[startdatum](/bo4e/202604/com/Menge#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e1">[enddatum](/bo4e/202604/com/Menge#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-f hbs-e0">[bilanzkreis](/bo4e/202604/com/Datenstand#bilanzkreis)</span> | Bilanzkreis | string |
| <span className="hbs-f hbs-e0">[bilanzierungsgebiet](/bo4e/202604/com/Datenstand#bilanzierungsgebiet)</span> | Bilanzierungsgebiet | string |
| <span className="hbs-g hbs-e0">[lastprofile](/bo4e/202604/com/Datenstand#lastprofile) <span className="hbs-liste">[ ]</span></span> | Eine Liste der verwendeten Lastprofile (SLP, SLP/TLP, ALP etc.) | [Lastprofil[]](/bo4e/202604/com/Lastprofil) |
| <span className="hbs-f hbs-e1">[bezeichnung](/bo4e/202604/com/Lastprofil#bezeichnung)</span> | Bezeichnung des Profils | string |
| <span className="hbs-f hbs-e1">[verfahren](/bo4e/202604/com/Lastprofil#verfahren)</span> | Profilverfahren | [Enum Profilverfahren](/bo4e/202604/enum/Profilverfahren)<br/><Werte>`SYNTHETISCH`, `ANALYTISCH`</Werte> |
| <span className="hbs-f hbs-e1">[profilart](/bo4e/202604/com/Lastprofil#profilart)</span> | Profilart | [Enum Profilart](/bo4e/202604/enum/Profilart)<br/><Werte>`ART_STANDARDLASTPROFIL`, `ART_TAGESPARAMETERABHAENGIGES_LASTPROFIL`, `ART_LASTPROFIL`</Werte> |
| <span className="hbs-f hbs-e1">[profilschar](/bo4e/202604/com/Lastprofil#profilschar)</span> | Profilschar des Profils | string |
| <span className="hbs-f hbs-e1">[einspeisung](/bo4e/202604/com/Lastprofil#einspeisung)</span> | Kennzeichen Einspeisung | boolean |
| <span className="hbs-f hbs-e1">[herausgeber](/bo4e/202604/com/Lastprofil#herausgeber)</span> | Herausgeber des Lastprofils | string |
| <span className="hbs-g hbs-e1">[tagesparameter](/bo4e/202604/com/Lastprofil#tagesparameter)</span> | — | [Tagesparameter](/bo4e/202604/com/Tagesparameter) |
| <span className="hbs-f hbs-e2">[klimazone](/bo4e/202604/com/Tagesparameter#klimazone)</span> | klimazone | string |
| <span className="hbs-f hbs-e2">[temperaturmessstelle](/bo4e/202604/com/Tagesparameter#temperaturmessstelle)</span> | temperaturmessstelle | string |
| <span className="hbs-f hbs-e2">[dienstanbieter](/bo4e/202604/com/Tagesparameter#dienstanbieter)</span> | dienstanbieter | string |
| <span className="hbs-f hbs-e2">[herausgeber](/bo4e/202604/com/Tagesparameter#herausgeber)</span> | Herausgeber | [Enum Herausgeber](/bo4e/202604/enum/Herausgeber)<br/><Werte>`NB`, `BDEW`, `TUM`</Werte> |
| <span className="hbs-f hbs-e1">[referenzprofilbezeichnung](/bo4e/202604/com/Lastprofil#referenzprofilbezeichnung)</span> | Bezeichnung des Referenzprofils | string |
| <span className="hbs-f hbs-e1">[referenzprofil](/bo4e/202604/com/Lastprofil#referenzprofil)</span> | Referenzprofil | string |
| <span className="hbs-f hbs-e1">[profiltyp](/bo4e/202604/com/Lastprofil#profiltyp)</span> | Profiltyp | [Enum Profiltyp](/bo4e/202604/enum/Profiltyp)<br/><Werte>`SLP_SEP`, `TLP_TEP`, `TEP`, `GEWERBE_ALLGEMEIN`, `GEWERBE_WERKTAGS_8_18_UHR`, `GEWERBE_MIT_STARKEM_BIS_UEBERWIEGENDEM_VERBRAUCH_IN_DEN_ABENDSTUNDEN`, `GEWERBE_DURCHLAUFEND`, `GEWERBE_LADEN_FRISEUR`, `GEWERBE_BAECKEREI_MIT_BACKSTUBE`, `GEWERBE_WOCHENENDBETRIEB`, `LANDWIRTSCHAFTSBETRIEBE_ALLGEMEIN`, `LANDWIRTSCHAFTSBETRIEBE_MIT_MILCHWIRTSCHAFT_NEBENERWERBS_TIERZUCHT`, `LANDWIRTSCHAFT_OHNE_MILCHVIEH`, `HAUSHALT`, `BANDLAST`, `UNTERBRECHBARE_VERBRAUCHSEINRICHTUNG`, `HEIZWAERMESPEICHER`, `STRASSENBELEUCHTUNG`, `PHOTOVOLTAIK_MARKTLOKATION`, `BLOCKHEIZKRAFTWERK`, `SONSTIGE_VERBRAUCHENDE_MARKTLOKATION`, `SONSTIGE_ERZEUGENDE_MARKTLOKATION`, `E_MOBILITAET_LADEPUNKT_IM_OEFFENTLICHEN_BEREICH`, `E_MOBILITAET_LADEPUNKT_EINES_HAUSHALTS`, `E_MOBILITAET_LADEPUNKT_EINES_GEWERBES`</Werte> |
| <span className="hbs-f hbs-e1">[normierungsfaktor](/bo4e/202604/com/Lastprofil#normierungsfaktor)</span> | Normierungsfaktor | [Enum Normierungsfaktor](/bo4e/202604/enum/Normierungsfaktor)<br/><Werte>`NORMIERUNGSFAKTOR_1_000_000_KWH_A`, `NORMIERUNGSFAKTOR_300_KWH_K`, `NORMIERUNGSFAKTOR_1_000_000_KW`</Werte> |
| <span className="hbs-g hbs-e1">[tagesmitteltemperatur](/bo4e/202604/com/Lastprofil#tagesmitteltemperatur)</span> | — | [Tagesmitteltemperatur](/bo4e/202604/com/Tagesmitteltemperatur) |
| <span className="hbs-f hbs-e2">[berechnungTagesmitteltemperatur](/bo4e/202604/com/Tagesmitteltemperatur#berechnungtagesmitteltemperatur)</span> | Berechnungsmethode | [Enum Berechnungsmethode](/bo4e/202604/enum/Berechnungsmethode)<br/><Werte>`24H_MITTELWERT`, `VOM_ANBIETER_ZUR_VERFUEGUNG_GESTELLTE_AEQUIVALENTE_TAGESMITTELTEMPERATUR`, `AEQUIVALENTE_TAGESMITTELTEMPERATUR`</Werte> |
| <span className="hbs-f hbs-e2">[anteilA](/bo4e/202604/com/Tagesmitteltemperatur#anteila)</span> | Anteil A | number (float) |
| <span className="hbs-f hbs-e2">[anteilB](/bo4e/202604/com/Tagesmitteltemperatur#anteilb)</span> | Anteil B | number (float) |
| <span className="hbs-f hbs-e2">[anteilC](/bo4e/202604/com/Tagesmitteltemperatur#anteilc)</span> | Anteil C | number (float) |
| <span className="hbs-f hbs-e2">[anteilD](/bo4e/202604/com/Tagesmitteltemperatur#anteild)</span> | Anteil D | number (float) |
| <span className="hbs-f hbs-e2">[begrenzungstemperatur](/bo4e/202604/com/Tagesmitteltemperatur#begrenzungstemperatur)</span> | Begrenzungstemperatur | string |
| <span className="hbs-f hbs-e1">[begrenzungskonstante](/bo4e/202604/com/Lastprofil#begrenzungskonstante)</span> | Begrenzungskonstante | [Enum Begrenzungskonstante](/bo4e/202604/enum/Begrenzungskonstante)<br/><Werte>`BEGRENZUNGSKONSTANTE_0`, `BEGRENZUNGSKONSTANTE_1`</Werte> |
| <span className="hbs-f hbs-e0">[aggregationsverantwortung](/bo4e/202604/com/Datenstand#aggregationsverantwortung)</span> | Aggregationsverantwortung | [Enum Aggregationsverantwortung](/bo4e/202604/enum/Aggregationsverantwortung)<br/><Werte>`UENB`, `VNB`</Werte> |

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
