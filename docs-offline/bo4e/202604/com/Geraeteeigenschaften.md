# Geraeteeigenschaften
<span hidden data-pagefind-meta={"title:Geraeteeigenschaften — BO4E-Komponente (FV 202604)"} />

BO4E-Komponente · 14 Felder · 47 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="geraetetyp"></a>`geraetetyp` | [Enum Geraetetyp](/bo4e/202604/enum/Geraetetyp)<br/><Werte>`WECHSELSTROMZAEHLER`, `DREHSTROMZAEHLER`, `ZWEIRICHTUNGSZAEHLER`, `RLM_ZAEHLER`, `IMS_ZAEHLER`, `BALGENGASZAEHLER`, `MAXIMUMZAEHLER`, `MULTIPLEXANLAGE`, `PAUSCHALANLAGE`, `VERSTAERKERANLAGE`, `SUMMATIONSGERAET`, `IMPULSGEBER`, `EDL_21_ZAEHLERAUFSATZ`, `VIER_QUADRANTEN_LASTGANGZAEHLER`, `MENGENUMWERTER`, `STROMWANDLER`, `SPANNUNGSWANDLER`, `DATENLOGGER`, `KOMMUNIKATIONSANSCHLUSS`, `MODEM`, `TELEKOMMUNIKATIONSEINRICHTUNG`, `KOMMUNIKATIONSEINRICHTUNG`, `DREHKOLBENGASZAEHLER`, `TURBINENRADGASZAEHLER`, `ULTRASCHALLZAEHLER`, `WIRBELGASZAEHLER`, `MODERNE_MESSEINRICHTUNG`, `ELEKTRONISCHER_HAUSHALTSZAEHLER`, `STEUEREINRICHTUNG`, `TECHNISCHESTEUEREINRICHTUNG`, `TARIFSCHALTGERAET`, `RUNDSTEUEREMPFAENGER`, `OPTIONALE_ZUS_ZAEHLEINRICHTUNG`, `MESSWANDLERSATZ_IMS_MME`, `KOMBIMESSWANDLER_IMS_MME`, `TARIFSCHALTGERAET_IMS_MME`, `RUNDSTEUEREMPFAENGER_IMS_MME`, `TEMPERATUR_KOMPENSATION`, `HOECHSTBELASTUNGS_ANZEIGER`, `SONSTIGES_GERAET`, `SMARTMETERGATEWAY`, `STEUERBOX`, `BLOCKSTROMWANDLER`, `KOMBIMESSWANDLER`, `MODEM_GSM`, `ETHERNET_KOM`, `PLC_COM`, `MODEM_FESTNETZ`, `DSL_KOM`, `LTE_KOM`, `DICHTEMENGENUMWERTER`, `TEMPERATURMENGENUMWERTER`, `ZUSTANDSMENGENUMWERTER`, `MESSDATENREGISTRIERGERAET`, `WANDLER`, `BEFESTIGUNGSEINRICHTUNG`</Werte> | Auflistung möglicher abzurechnender Gerätetypen |
| <a id="geraetemerkmal"></a>`geraetemerkmal` | [Enum Geraetemerkmal](/bo4e/202604/enum/Geraetemerkmal)<br/><Werte>`EINTARIF`, `ZWEITARIF`, `MEHRTARIF`, `GAS_G2P5`, `GAS_G4`, `GAS_G6`, `GAS_G10`, `GAS_G16`, `GAS_G25`, `GAS_G40`, `GAS_G65`, `GAS_G100`, `GAS_G160`, `GAS_G250`, `GAS_G350`, `GAS_G400`, `GAS_G4000`, `GAS_G650`, `GAS_G6500`, `GAS_G1000`, `GAS_G10000`, `GAS_G12500`, `GAS_G1600`, `GAS_G16000`, `GAS_G2500`, `IMPULSGEBER_G4_G100`, `IMPULSGEBER_G100`, `MODEM_GSM`, `MODEM_GPRS`, `MODEM_FUNK`, `MODEM_GSM_O_LG`, `MODEM_GSM_M_LG`, `MODEM_FESTNETZ`, `MODEM_GPRS_M_LG`, `PLC_COM`, `ETHERNET_KOM`, `DSL_KOM`, `LTE_KOM`, `RUNDSTEUEREMPFAENGER`, `TARIFSCHALTGERAET`, `ZUSTANDS_MU`, `TEMPERATUR_MU`, `KOMPAKT_MU`, `SYSTEM_MU`, `UNBESTIMMT`, `WASSER_MWZW`, `WASSER_WZWW`, `WASSER_WZ01`, `WASSER_WZ02`, `WASSER_WZ03`, `WASSER_WZ04`, `WASSER_WZ05`, `WASSER_WZ06`, `WASSER_WZ07`, `WASSER_WZ08`, `WASSER_WZ09`, `WASSER_WZ10`, `WASSER_VWZ04`, `WASSER_VWZ05`, `WASSER_VWZ06`, `WASSER_VWZ07`, `WASSER_VWZ10`, `DICHTEMENGENUMWERTER`, `TEMPERATURMENGENUMWERTER`, `ZUSTANDSMENGENUMWERTER`, `BLOCKSTROMWANDLER`, `MESSWANDLERSATZ_IMS_MME`, `KOMBIMESSWANDLER`, `SPANNUNGSWANDLER`</Werte> | Geraetemerkmal |
| <a id="volumenerfassung"></a>`volumenerfassung` | [Enum Volumenerfassung](/bo4e/202604/enum/Volumenerfassung)<br/><Werte>`HOCHFREQUENZSONDE`, `KENNLINIENKORREKTUR`, `SCHLEICHMENGENUNTERDRUECKUNG`</Werte> | Volumenerfassung |
| <a id="serialnummer"></a>`serialnummer` | string | serialnummer |
| <a id="herstellungsdatum"></a>`herstellungsdatum` | string | Produktions-/Herstellungsdatum |
| <a id="baujahr"></a>`baujahr` | string | Baujahr/Jahr des in Verkehrs bringens |
| <a id="eichungbis"></a>`eichungBis` | string | Eichgültigkeit |
| <a id="faktor"></a>`faktor` | number (float) | faktor |
| <a id="firmwareversion"></a>`firmwareVersion` | string | Firmware-Version |
| <a id="herstellertypbezeichnung"></a>`herstellerTypbezeichnung` | string | Hersteller-Typbezeichnung |
| <a id="simkartennummer"></a>`simKartenNummer` | string | SIM-Kartennummer |
| <a id="modemkennungimsi"></a>`modemKennungIMSI` | string | Modem-Kennung (IMSI) |
| <a id="tkprovider"></a>`tkProvider` | string | Telekommunikationsanbieter |
| <a id="ipversion"></a>`ipVersion` | string | IP-Version |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[geraetetyp](/bo4e/202604/com/Geraeteeigenschaften#geraetetyp)</span> | Auflistung möglicher abzurechnender Gerätetypen | [Enum Geraetetyp](/bo4e/202604/enum/Geraetetyp)<br/><Werte>`WECHSELSTROMZAEHLER`, `DREHSTROMZAEHLER`, `ZWEIRICHTUNGSZAEHLER`, `RLM_ZAEHLER`, `IMS_ZAEHLER`, `BALGENGASZAEHLER`, `MAXIMUMZAEHLER`, `MULTIPLEXANLAGE`, `PAUSCHALANLAGE`, `VERSTAERKERANLAGE`, `SUMMATIONSGERAET`, `IMPULSGEBER`, `EDL_21_ZAEHLERAUFSATZ`, `VIER_QUADRANTEN_LASTGANGZAEHLER`, `MENGENUMWERTER`, `STROMWANDLER`, `SPANNUNGSWANDLER`, `DATENLOGGER`, `KOMMUNIKATIONSANSCHLUSS`, `MODEM`, `TELEKOMMUNIKATIONSEINRICHTUNG`, `KOMMUNIKATIONSEINRICHTUNG`, `DREHKOLBENGASZAEHLER`, `TURBINENRADGASZAEHLER`, `ULTRASCHALLZAEHLER`, `WIRBELGASZAEHLER`, `MODERNE_MESSEINRICHTUNG`, `ELEKTRONISCHER_HAUSHALTSZAEHLER`, `STEUEREINRICHTUNG`, `TECHNISCHESTEUEREINRICHTUNG`, `TARIFSCHALTGERAET`, `RUNDSTEUEREMPFAENGER`, `OPTIONALE_ZUS_ZAEHLEINRICHTUNG`, `MESSWANDLERSATZ_IMS_MME`, `KOMBIMESSWANDLER_IMS_MME`, `TARIFSCHALTGERAET_IMS_MME`, `RUNDSTEUEREMPFAENGER_IMS_MME`, `TEMPERATUR_KOMPENSATION`, `HOECHSTBELASTUNGS_ANZEIGER`, `SONSTIGES_GERAET`, `SMARTMETERGATEWAY`, `STEUERBOX`, `BLOCKSTROMWANDLER`, `KOMBIMESSWANDLER`, `MODEM_GSM`, `ETHERNET_KOM`, `PLC_COM`, `MODEM_FESTNETZ`, `DSL_KOM`, `LTE_KOM`, `DICHTEMENGENUMWERTER`, `TEMPERATURMENGENUMWERTER`, `ZUSTANDSMENGENUMWERTER`, `MESSDATENREGISTRIERGERAET`, `WANDLER`, `BEFESTIGUNGSEINRICHTUNG`</Werte> |
| <span className="hbs-f hbs-e0">[geraetemerkmal](/bo4e/202604/com/Geraeteeigenschaften#geraetemerkmal)</span> | Geraetemerkmal | [Enum Geraetemerkmal](/bo4e/202604/enum/Geraetemerkmal)<br/><Werte>`EINTARIF`, `ZWEITARIF`, `MEHRTARIF`, `GAS_G2P5`, `GAS_G4`, `GAS_G6`, `GAS_G10`, `GAS_G16`, `GAS_G25`, `GAS_G40`, `GAS_G65`, `GAS_G100`, `GAS_G160`, `GAS_G250`, `GAS_G350`, `GAS_G400`, `GAS_G4000`, `GAS_G650`, `GAS_G6500`, `GAS_G1000`, `GAS_G10000`, `GAS_G12500`, `GAS_G1600`, `GAS_G16000`, `GAS_G2500`, `IMPULSGEBER_G4_G100`, `IMPULSGEBER_G100`, `MODEM_GSM`, `MODEM_GPRS`, `MODEM_FUNK`, `MODEM_GSM_O_LG`, `MODEM_GSM_M_LG`, `MODEM_FESTNETZ`, `MODEM_GPRS_M_LG`, `PLC_COM`, `ETHERNET_KOM`, `DSL_KOM`, `LTE_KOM`, `RUNDSTEUEREMPFAENGER`, `TARIFSCHALTGERAET`, `ZUSTANDS_MU`, `TEMPERATUR_MU`, `KOMPAKT_MU`, `SYSTEM_MU`, `UNBESTIMMT`, `WASSER_MWZW`, `WASSER_WZWW`, `WASSER_WZ01`, `WASSER_WZ02`, `WASSER_WZ03`, `WASSER_WZ04`, `WASSER_WZ05`, `WASSER_WZ06`, `WASSER_WZ07`, `WASSER_WZ08`, `WASSER_WZ09`, `WASSER_WZ10`, `WASSER_VWZ04`, `WASSER_VWZ05`, `WASSER_VWZ06`, `WASSER_VWZ07`, `WASSER_VWZ10`, `DICHTEMENGENUMWERTER`, `TEMPERATURMENGENUMWERTER`, `ZUSTANDSMENGENUMWERTER`, `BLOCKSTROMWANDLER`, `MESSWANDLERSATZ_IMS_MME`, `KOMBIMESSWANDLER`, `SPANNUNGSWANDLER`</Werte> |
| <span className="hbs-f hbs-e0">[volumenerfassung](/bo4e/202604/com/Geraeteeigenschaften#volumenerfassung)</span> | Volumenerfassung | [Enum Volumenerfassung](/bo4e/202604/enum/Volumenerfassung)<br/><Werte>`HOCHFREQUENZSONDE`, `KENNLINIENKORREKTUR`, `SCHLEICHMENGENUNTERDRUECKUNG`</Werte> |
| <span className="hbs-f hbs-e0">[serialnummer](/bo4e/202604/com/Geraeteeigenschaften#serialnummer)</span> | serialnummer | string |
| <span className="hbs-f hbs-e0">[herstellungsdatum](/bo4e/202604/com/Geraeteeigenschaften#herstellungsdatum)</span> | Produktions-/Herstellungsdatum | string |
| <span className="hbs-f hbs-e0">[baujahr](/bo4e/202604/com/Geraeteeigenschaften#baujahr)</span> | Baujahr/Jahr des in Verkehrs bringens | string |
| <span className="hbs-f hbs-e0">[eichungBis](/bo4e/202604/com/Geraeteeigenschaften#eichungbis)</span> | Eichgültigkeit | string |
| <span className="hbs-f hbs-e0">[faktor](/bo4e/202604/com/Geraeteeigenschaften#faktor)</span> | faktor | number (float) |
| <span className="hbs-f hbs-e0">[firmwareVersion](/bo4e/202604/com/Geraeteeigenschaften#firmwareversion)</span> | Firmware-Version | string |
| <span className="hbs-f hbs-e0">[herstellerTypbezeichnung](/bo4e/202604/com/Geraeteeigenschaften#herstellertypbezeichnung)</span> | Hersteller-Typbezeichnung | string |
| <span className="hbs-f hbs-e0">[simKartenNummer](/bo4e/202604/com/Geraeteeigenschaften#simkartennummer)</span> | SIM-Kartennummer | string |
| <span className="hbs-f hbs-e0">[modemKennungIMSI](/bo4e/202604/com/Geraeteeigenschaften#modemkennungimsi)</span> | Modem-Kennung (IMSI) | string |
| <span className="hbs-f hbs-e0">[tkProvider](/bo4e/202604/com/Geraeteeigenschaften#tkprovider)</span> | Telekommunikationsanbieter | string |
| <span className="hbs-f hbs-e0">[ipVersion](/bo4e/202604/com/Geraeteeigenschaften#ipversion)</span> | IP-Version | string |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### geraetetyp

1 Verwendung(en) in den Nachrichtentypen ORDERS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_17009](/schnittstellen/202604/pruefi/ORDERS/PI_17009) | Prüfi | ORDERS | stammdaten › ZAEHLER › geraete › geraeteeigenschaften |

### geraetemerkmal

27 Verwendung(en) in den Nachrichtentypen QUOTES, UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_15001](/schnittstellen/202604/pruefi/QUOTES/PI_15001) | Prüfi | QUOTES | stammdaten › ZAEHLER › geraete › geraeteeigenschaften |
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › geraete › geraeteeigenschaften |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › geraete › geraeteeigenschaften |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › geraete › geraeteeigenschaften |
| [PI_44035](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44035) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › geraete › geraeteeigenschaften |
| [PI_44043](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44043) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › geraete › geraeteeigenschaften |
| [PI_44060](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44060) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › geraete › geraeteeigenschaften |
| [PI_44116](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44116) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › geraete › geraeteeigenschaften |
| [PI_44117](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44117) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › geraete › geraeteeigenschaften |
| [PI_44143](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44143) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › geraete › geraeteeigenschaften |
| [PI_44145](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44145) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › geraete › geraeteeigenschaften |
| [PI_44147](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44147) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › geraete › geraeteeigenschaften |
| [PI_44148](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44148) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › geraete › geraeteeigenschaften |
| [PI_44149](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44149) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › geraete › geraeteeigenschaften |
| [PI_44168](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › geraete › geraeteeigenschaften |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete › geraeteeigenschaften |
| [PI_55060](/schnittstellen/202604/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete › geraeteeigenschaften |
| [PI_55074](/schnittstellen/202604/pruefi/UTILMD/PI_55074) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete › geraeteeigenschaften |
| [PI_55075](/schnittstellen/202604/pruefi/UTILMD/PI_55075) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete › geraeteeigenschaften |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete › geraeteeigenschaften |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete › geraeteeigenschaften |
| [PI_55643](/schnittstellen/202604/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete › geraeteeigenschaften |
| [PI_55648](/schnittstellen/202604/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete › geraeteeigenschaften |
| [PI_55653](/schnittstellen/202604/pruefi/UTILMD/PI_55653) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete › geraeteeigenschaften |
| [PI_55658](/schnittstellen/202604/pruefi/UTILMD/PI_55658) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete › geraeteeigenschaften |
| [PI_55663](/schnittstellen/202604/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete › geraeteeigenschaften |
| [PI_55669](/schnittstellen/202604/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete › geraeteeigenschaften |

### volumenerfassung

6 Verwendung(en) in den Nachrichtentypen UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_44043](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44043) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › geraete › geraeteeigenschaften |
| [PI_44060](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44060) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › geraete › geraeteeigenschaften |
| [PI_44116](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44116) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › geraete › geraeteeigenschaften |
| [PI_44148](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44148) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › geraete › geraeteeigenschaften |
| [PI_44149](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44149) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › geraete › geraeteeigenschaften |
| [PI_44168](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › geraete › geraeteeigenschaften |

### faktor

13 Verwendung(en) in den Nachrichtentypen QUOTES, UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_15001](/schnittstellen/202604/pruefi/QUOTES/PI_15001) | Prüfi | QUOTES | stammdaten › ZAEHLER › geraete › geraeteeigenschaften |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete › geraeteeigenschaften |
| [PI_55060](/schnittstellen/202604/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete › geraeteeigenschaften |
| [PI_55074](/schnittstellen/202604/pruefi/UTILMD/PI_55074) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete › geraeteeigenschaften |
| [PI_55075](/schnittstellen/202604/pruefi/UTILMD/PI_55075) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete › geraeteeigenschaften |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete › geraeteeigenschaften |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete › geraeteeigenschaften |
| [PI_55643](/schnittstellen/202604/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete › geraeteeigenschaften |
| [PI_55648](/schnittstellen/202604/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete › geraeteeigenschaften |
| [PI_55653](/schnittstellen/202604/pruefi/UTILMD/PI_55653) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete › geraeteeigenschaften |
| [PI_55658](/schnittstellen/202604/pruefi/UTILMD/PI_55658) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete › geraeteeigenschaften |
| [PI_55663](/schnittstellen/202604/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete › geraeteeigenschaften |
| [PI_55669](/schnittstellen/202604/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete › geraeteeigenschaften |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
