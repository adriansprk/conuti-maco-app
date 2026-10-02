# Energiemix
<span hidden data-pagefind-meta={"title:Energiemix — BO4E-Komponente (FV 202610)"} />

BO4E-Komponente · 12 Felder · 0 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="anteil"></a>`anteil` | [Energieherkunft[]](/bo4e/202610/com/Energieherkunft) | Anteile der jeweiligen Erzeugungsart |
| <a id="atommuell"></a>`atommuell` | number (float) | Höhe des erzeugten Atommülls in g/kWh |
| <a id="bemerkung"></a>`bemerkung` | string | Bemerkung zum Energiemix |
| <a id="bezeichnung"></a>`bezeichnung` | string | Bezeichnung des Energiemix |
| <a id="co2_emission"></a>`co2_emission` | number (float) | Höhe des erzeugten CO2-Ausstosses in g/kWh |
| <a id="energieart"></a>`energieart` | [Enum Sparte](/bo4e/202610/enum/Sparte)<br/><Werte>`STROM`, `GAS`, `FERNWAERME`, `NAHWAERME`, `WASSER`, `ABWASSER`</Werte> | Strom oder Gas etc. |
| <a id="energiemixnummer"></a>`energiemixnummer` | integer | Eindeutige Nummer zur Identifizierung des Energiemixes |
| <a id="gueltigkeitsjahr"></a>`gueltigkeitsjahr` | integer | Jahr, für das der Energiemix gilt |
| <a id="ist_in_oeko_top_ten"></a>`ist_in_oeko_top_ten` | boolean | Kennzeichen, ob der Versorger zu den Öko Top Ten gehört |
| <a id="oekolabel"></a>`oekolabel` | [Enum Oekolabel[]](/bo4e/202610/enum/Oekolabel)<br/><Werte>`ENERGREEN`, `GASGREEN`, `GASGREEN_GRUENER_STROM`, `GRUENER_STROM`, `GRUENER_STROM_GOLD`, `GRUENER_STROM_SILBER`, `GRUENES_GAS`, `NATURWATT_STROM`, `OK_POWER`, `RENEWABLE_PLUS`, `WATERGREEN`, `WATERGREEN_PLUS`</Werte> | Ökolabel für den Energiemix |
| <a id="oekozertifikate"></a>`oekozertifikate` | [Enum Oekozertifikat[]](/bo4e/202610/enum/Oekozertifikat)<br/><Werte>`BET`, `CMS_EE01`, `CMS_EE02`, `EECS`, `FRAUNHOFER`, `FREIBERG`, `KLIMA_INVEST`, `LGA`, `RECS`, `REGS_EGL`, `TUEV`, `TUEV_HESSEN`, `TUEV_NORD`, `TUEV_RHEINLAND`, `TUEV_SUED`, `TUEV_SUED_EE01`, `TUEV_SUED_EE02`</Werte> | Zertifikate für den Energiemix |
| <a id="website"></a>`website` | string | Internetseite, auf der die Strommixdaten veröffentlicht sind |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-g hbs-e0">[anteil](/bo4e/202610/com/Energiemix#anteil) <span className="hbs-liste">[ ]</span></span> | Anteile der jeweiligen Erzeugungsart | [Energieherkunft[]](/bo4e/202610/com/Energieherkunft) |
| <span className="hbs-f hbs-e1">[erzeugungsart](/bo4e/202610/com/Energieherkunft#erzeugungsart)</span> | Art der Erzeugung | [Enum Erzeugungsart](/bo4e/202610/enum/Erzeugungsart)<br/><Werte>`EEG`, `KWK`, `EEG_DV`, `KWK_DV`, `WIND`, `SOLAR`, `KERNKRAFT`, `WASSER`, `GEOTHERMIE`, `BIOMASSE`, `KOHLE`, `GAS`, `SONSTIGE`, `SONSTIGE_EEG`, `SONSTIGE_ERZEUGUNGSART`</Werte> |
| <span className="hbs-f hbs-e1">[anteilProzent](/bo4e/202610/com/Energieherkunft#anteilprozent)</span> | Prozentualer Anteil der Erzeugung | number (float) |
| <span className="hbs-f hbs-e0">[atommuell](/bo4e/202610/com/Energiemix#atommuell)</span> | Höhe des erzeugten Atommülls in g/kWh | number (float) |
| <span className="hbs-f hbs-e0">[bemerkung](/bo4e/202610/com/Energiemix#bemerkung)</span> | Bemerkung zum Energiemix | string |
| <span className="hbs-f hbs-e0">[bezeichnung](/bo4e/202610/com/Energiemix#bezeichnung)</span> | Bezeichnung des Energiemix | string |
| <span className="hbs-f hbs-e0">[co2_emission](/bo4e/202610/com/Energiemix#co2_emission)</span> | Höhe des erzeugten CO2-Ausstosses in g/kWh | number (float) |
| <span className="hbs-f hbs-e0">[energieart](/bo4e/202610/com/Energiemix#energieart)</span> | Strom oder Gas etc. | [Enum Sparte](/bo4e/202610/enum/Sparte)<br/><Werte>`STROM`, `GAS`, `FERNWAERME`, `NAHWAERME`, `WASSER`, `ABWASSER`</Werte> |
| <span className="hbs-f hbs-e0">[energiemixnummer](/bo4e/202610/com/Energiemix#energiemixnummer)</span> | Eindeutige Nummer zur Identifizierung des Energiemixes | integer |
| <span className="hbs-f hbs-e0">[gueltigkeitsjahr](/bo4e/202610/com/Energiemix#gueltigkeitsjahr)</span> | Jahr, für das der Energiemix gilt | integer |
| <span className="hbs-f hbs-e0">[ist_in_oeko_top_ten](/bo4e/202610/com/Energiemix#ist_in_oeko_top_ten)</span> | Kennzeichen, ob der Versorger zu den Öko Top Ten gehört | boolean |
| <span className="hbs-f hbs-e0">[oekolabel](/bo4e/202610/com/Energiemix#oekolabel) <span className="hbs-liste">[ ]</span></span> | Ökolabel für den Energiemix | [Enum Oekolabel[]](/bo4e/202610/enum/Oekolabel)<br/><Werte>`ENERGREEN`, `GASGREEN`, `GASGREEN_GRUENER_STROM`, `GRUENER_STROM`, `GRUENER_STROM_GOLD`, `GRUENER_STROM_SILBER`, `GRUENES_GAS`, `NATURWATT_STROM`, `OK_POWER`, `RENEWABLE_PLUS`, `WATERGREEN`, `WATERGREEN_PLUS`</Werte> |
| <span className="hbs-f hbs-e0">[oekozertifikate](/bo4e/202610/com/Energiemix#oekozertifikate) <span className="hbs-liste">[ ]</span></span> | Zertifikate für den Energiemix | [Enum Oekozertifikat[]](/bo4e/202610/enum/Oekozertifikat)<br/><Werte>`BET`, `CMS_EE01`, `CMS_EE02`, `EECS`, `FRAUNHOFER`, `FREIBERG`, `KLIMA_INVEST`, `LGA`, `RECS`, `REGS_EGL`, `TUEV`, `TUEV_HESSEN`, `TUEV_NORD`, `TUEV_RHEINLAND`, `TUEV_SUED`, `TUEV_SUED_EE01`, `TUEV_SUED_EE02`</Werte> |
| <span className="hbs-f hbs-e0">[website](/bo4e/202610/com/Energiemix#website)</span> | Internetseite, auf der die Strommixdaten veröffentlicht sind | string |

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
