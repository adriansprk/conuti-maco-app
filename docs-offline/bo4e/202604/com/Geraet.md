# Geraet
<span hidden data-pagefind-meta={"title:Geraet — BO4E-Komponente (FV 202604)"} />

BO4E-Komponente · 7 Felder · 63 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="geraetetyp"></a>`geraetetyp` | [Enum Geraetetyp](/bo4e/202604/enum/Geraetetyp)<br/><Werte>`WECHSELSTROMZAEHLER`, `DREHSTROMZAEHLER`, `ZWEIRICHTUNGSZAEHLER`, `RLM_ZAEHLER`, `IMS_ZAEHLER`, `BALGENGASZAEHLER`, `MAXIMUMZAEHLER`, `MULTIPLEXANLAGE`, `PAUSCHALANLAGE`, `VERSTAERKERANLAGE`, `SUMMATIONSGERAET`, `IMPULSGEBER`, `EDL_21_ZAEHLERAUFSATZ`, `VIER_QUADRANTEN_LASTGANGZAEHLER`, `MENGENUMWERTER`, `STROMWANDLER`, `SPANNUNGSWANDLER`, `DATENLOGGER`, `KOMMUNIKATIONSANSCHLUSS`, `MODEM`, `TELEKOMMUNIKATIONSEINRICHTUNG`, `KOMMUNIKATIONSEINRICHTUNG`, `DREHKOLBENGASZAEHLER`, `TURBINENRADGASZAEHLER`, `ULTRASCHALLZAEHLER`, `WIRBELGASZAEHLER`, `MODERNE_MESSEINRICHTUNG`, `ELEKTRONISCHER_HAUSHALTSZAEHLER`, `STEUEREINRICHTUNG`, `TECHNISCHESTEUEREINRICHTUNG`, `TARIFSCHALTGERAET`, `RUNDSTEUEREMPFAENGER`, `OPTIONALE_ZUS_ZAEHLEINRICHTUNG`, `MESSWANDLERSATZ_IMS_MME`, `KOMBIMESSWANDLER_IMS_MME`, `TARIFSCHALTGERAET_IMS_MME`, `RUNDSTEUEREMPFAENGER_IMS_MME`, `TEMPERATUR_KOMPENSATION`, `HOECHSTBELASTUNGS_ANZEIGER`, `SONSTIGES_GERAET`, `SMARTMETERGATEWAY`, `STEUERBOX`, `BLOCKSTROMWANDLER`, `KOMBIMESSWANDLER`, `MODEM_GSM`, `ETHERNET_KOM`, `PLC_COM`, `MODEM_FESTNETZ`, `DSL_KOM`, `LTE_KOM`, `DICHTEMENGENUMWERTER`, `TEMPERATURMENGENUMWERTER`, `ZUSTANDSMENGENUMWERTER`, `MESSDATENREGISTRIERGERAET`, `WANDLER`, `BEFESTIGUNGSEINRICHTUNG`</Werte> | Auflistung möglicher abzurechnender Gerätetypen |
| <a id="bezeichnung"></a>`bezeichnung` | string | Bezeichnung des Gerätes |
| <a id="geraetenummer"></a>`geraetenummer` | string | Die auf dem Geräte aufgedruckte Nummer, die vom MSB vergeben wird. |
| <a id="geraetereferenz"></a>`geraetereferenz` | string | geraetereferenz |
| <a id="geraeteeigenschaften"></a>`geraeteeigenschaften` | [Geraeteeigenschaften](/bo4e/202604/com/Geraeteeigenschaften) | Festlegung der Eigenschaften des Gerätes. Z.B. Wandler MS/NS. |
| <a id="volumenerfassung"></a>`volumenerfassung` | [Enum Volumenerfassung](/bo4e/202604/enum/Volumenerfassung)<br/><Werte>`HOCHFREQUENZSONDE`, `KENNLINIENKORREKTUR`, `SCHLEICHMENGENUNTERDRUECKUNG`</Werte> | Volumenerfassung |
| <a id="weiteregeraetenummern"></a>`weitereGeraetenummern` | string[] | weitereGeraetenummern |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[geraetetyp](/bo4e/202604/com/Geraet#geraetetyp)</span> | Auflistung möglicher abzurechnender Gerätetypen | [Enum Geraetetyp](/bo4e/202604/enum/Geraetetyp)<br/><Werte>`WECHSELSTROMZAEHLER`, `DREHSTROMZAEHLER`, `ZWEIRICHTUNGSZAEHLER`, `RLM_ZAEHLER`, `IMS_ZAEHLER`, `BALGENGASZAEHLER`, `MAXIMUMZAEHLER`, `MULTIPLEXANLAGE`, `PAUSCHALANLAGE`, `VERSTAERKERANLAGE`, `SUMMATIONSGERAET`, `IMPULSGEBER`, `EDL_21_ZAEHLERAUFSATZ`, `VIER_QUADRANTEN_LASTGANGZAEHLER`, `MENGENUMWERTER`, `STROMWANDLER`, `SPANNUNGSWANDLER`, `DATENLOGGER`, `KOMMUNIKATIONSANSCHLUSS`, `MODEM`, `TELEKOMMUNIKATIONSEINRICHTUNG`, `KOMMUNIKATIONSEINRICHTUNG`, `DREHKOLBENGASZAEHLER`, `TURBINENRADGASZAEHLER`, `ULTRASCHALLZAEHLER`, `WIRBELGASZAEHLER`, `MODERNE_MESSEINRICHTUNG`, `ELEKTRONISCHER_HAUSHALTSZAEHLER`, `STEUEREINRICHTUNG`, `TECHNISCHESTEUEREINRICHTUNG`, `TARIFSCHALTGERAET`, `RUNDSTEUEREMPFAENGER`, `OPTIONALE_ZUS_ZAEHLEINRICHTUNG`, `MESSWANDLERSATZ_IMS_MME`, `KOMBIMESSWANDLER_IMS_MME`, `TARIFSCHALTGERAET_IMS_MME`, `RUNDSTEUEREMPFAENGER_IMS_MME`, `TEMPERATUR_KOMPENSATION`, `HOECHSTBELASTUNGS_ANZEIGER`, `SONSTIGES_GERAET`, `SMARTMETERGATEWAY`, `STEUERBOX`, `BLOCKSTROMWANDLER`, `KOMBIMESSWANDLER`, `MODEM_GSM`, `ETHERNET_KOM`, `PLC_COM`, `MODEM_FESTNETZ`, `DSL_KOM`, `LTE_KOM`, `DICHTEMENGENUMWERTER`, `TEMPERATURMENGENUMWERTER`, `ZUSTANDSMENGENUMWERTER`, `MESSDATENREGISTRIERGERAET`, `WANDLER`, `BEFESTIGUNGSEINRICHTUNG`</Werte> |
| <span className="hbs-f hbs-e0">[bezeichnung](/bo4e/202604/com/Geraet#bezeichnung)</span> | Bezeichnung des Gerätes | string |
| <span className="hbs-f hbs-e0">[geraetenummer](/bo4e/202604/com/Geraet#geraetenummer)</span> | Die auf dem Geräte aufgedruckte Nummer, die vom MSB vergeben wird. | string |
| <span className="hbs-f hbs-e0">[geraetereferenz](/bo4e/202604/com/Geraet#geraetereferenz)</span> | geraetereferenz | string |
| <span className="hbs-g hbs-e0">[geraeteeigenschaften](/bo4e/202604/com/Geraet#geraeteeigenschaften)</span> | Festlegung der Eigenschaften des Gerätes. Z.B. Wandler MS/NS. | [Geraeteeigenschaften](/bo4e/202604/com/Geraeteeigenschaften) |
| <span className="hbs-f hbs-e1">[geraetetyp](/bo4e/202604/com/Geraeteeigenschaften#geraetetyp)</span> | Auflistung möglicher abzurechnender Gerätetypen | [Enum Geraetetyp](/bo4e/202604/enum/Geraetetyp)<br/><Werte>`WECHSELSTROMZAEHLER`, `DREHSTROMZAEHLER`, `ZWEIRICHTUNGSZAEHLER`, `RLM_ZAEHLER`, `IMS_ZAEHLER`, `BALGENGASZAEHLER`, `MAXIMUMZAEHLER`, `MULTIPLEXANLAGE`, `PAUSCHALANLAGE`, `VERSTAERKERANLAGE`, `SUMMATIONSGERAET`, `IMPULSGEBER`, `EDL_21_ZAEHLERAUFSATZ`, `VIER_QUADRANTEN_LASTGANGZAEHLER`, `MENGENUMWERTER`, `STROMWANDLER`, `SPANNUNGSWANDLER`, `DATENLOGGER`, `KOMMUNIKATIONSANSCHLUSS`, `MODEM`, `TELEKOMMUNIKATIONSEINRICHTUNG`, `KOMMUNIKATIONSEINRICHTUNG`, `DREHKOLBENGASZAEHLER`, `TURBINENRADGASZAEHLER`, `ULTRASCHALLZAEHLER`, `WIRBELGASZAEHLER`, `MODERNE_MESSEINRICHTUNG`, `ELEKTRONISCHER_HAUSHALTSZAEHLER`, `STEUEREINRICHTUNG`, `TECHNISCHESTEUEREINRICHTUNG`, `TARIFSCHALTGERAET`, `RUNDSTEUEREMPFAENGER`, `OPTIONALE_ZUS_ZAEHLEINRICHTUNG`, `MESSWANDLERSATZ_IMS_MME`, `KOMBIMESSWANDLER_IMS_MME`, `TARIFSCHALTGERAET_IMS_MME`, `RUNDSTEUEREMPFAENGER_IMS_MME`, `TEMPERATUR_KOMPENSATION`, `HOECHSTBELASTUNGS_ANZEIGER`, `SONSTIGES_GERAET`, `SMARTMETERGATEWAY`, `STEUERBOX`, `BLOCKSTROMWANDLER`, `KOMBIMESSWANDLER`, `MODEM_GSM`, `ETHERNET_KOM`, `PLC_COM`, `MODEM_FESTNETZ`, `DSL_KOM`, `LTE_KOM`, `DICHTEMENGENUMWERTER`, `TEMPERATURMENGENUMWERTER`, `ZUSTANDSMENGENUMWERTER`, `MESSDATENREGISTRIERGERAET`, `WANDLER`, `BEFESTIGUNGSEINRICHTUNG`</Werte> |
| <span className="hbs-f hbs-e1">[geraetemerkmal](/bo4e/202604/com/Geraeteeigenschaften#geraetemerkmal)</span> | Geraetemerkmal | [Enum Geraetemerkmal](/bo4e/202604/enum/Geraetemerkmal)<br/><Werte>`EINTARIF`, `ZWEITARIF`, `MEHRTARIF`, `GAS_G2P5`, `GAS_G4`, `GAS_G6`, `GAS_G10`, `GAS_G16`, `GAS_G25`, `GAS_G40`, `GAS_G65`, `GAS_G100`, `GAS_G160`, `GAS_G250`, `GAS_G350`, `GAS_G400`, `GAS_G4000`, `GAS_G650`, `GAS_G6500`, `GAS_G1000`, `GAS_G10000`, `GAS_G12500`, `GAS_G1600`, `GAS_G16000`, `GAS_G2500`, `IMPULSGEBER_G4_G100`, `IMPULSGEBER_G100`, `MODEM_GSM`, `MODEM_GPRS`, `MODEM_FUNK`, `MODEM_GSM_O_LG`, `MODEM_GSM_M_LG`, `MODEM_FESTNETZ`, `MODEM_GPRS_M_LG`, `PLC_COM`, `ETHERNET_KOM`, `DSL_KOM`, `LTE_KOM`, `RUNDSTEUEREMPFAENGER`, `TARIFSCHALTGERAET`, `ZUSTANDS_MU`, `TEMPERATUR_MU`, `KOMPAKT_MU`, `SYSTEM_MU`, `UNBESTIMMT`, `WASSER_MWZW`, `WASSER_WZWW`, `WASSER_WZ01`, `WASSER_WZ02`, `WASSER_WZ03`, `WASSER_WZ04`, `WASSER_WZ05`, `WASSER_WZ06`, `WASSER_WZ07`, `WASSER_WZ08`, `WASSER_WZ09`, `WASSER_WZ10`, `WASSER_VWZ04`, `WASSER_VWZ05`, `WASSER_VWZ06`, `WASSER_VWZ07`, `WASSER_VWZ10`, `DICHTEMENGENUMWERTER`, `TEMPERATURMENGENUMWERTER`, `ZUSTANDSMENGENUMWERTER`, `BLOCKSTROMWANDLER`, `MESSWANDLERSATZ_IMS_MME`, `KOMBIMESSWANDLER`, `SPANNUNGSWANDLER`</Werte> |
| <span className="hbs-f hbs-e1">[volumenerfassung](/bo4e/202604/com/Geraeteeigenschaften#volumenerfassung)</span> | Volumenerfassung | [Enum Volumenerfassung](/bo4e/202604/enum/Volumenerfassung)<br/><Werte>`HOCHFREQUENZSONDE`, `KENNLINIENKORREKTUR`, `SCHLEICHMENGENUNTERDRUECKUNG`</Werte> |
| <span className="hbs-f hbs-e1">[serialnummer](/bo4e/202604/com/Geraeteeigenschaften#serialnummer)</span> | serialnummer | string |
| <span className="hbs-f hbs-e1">[herstellungsdatum](/bo4e/202604/com/Geraeteeigenschaften#herstellungsdatum)</span> | Produktions-/Herstellungsdatum | string |
| <span className="hbs-f hbs-e1">[baujahr](/bo4e/202604/com/Geraeteeigenschaften#baujahr)</span> | Baujahr/Jahr des in Verkehrs bringens | string |
| <span className="hbs-f hbs-e1">[eichungBis](/bo4e/202604/com/Geraeteeigenschaften#eichungbis)</span> | Eichgültigkeit | string |
| <span className="hbs-f hbs-e1">[faktor](/bo4e/202604/com/Geraeteeigenschaften#faktor)</span> | faktor | number (float) |
| <span className="hbs-f hbs-e1">[firmwareVersion](/bo4e/202604/com/Geraeteeigenschaften#firmwareversion)</span> | Firmware-Version | string |
| <span className="hbs-f hbs-e1">[herstellerTypbezeichnung](/bo4e/202604/com/Geraeteeigenschaften#herstellertypbezeichnung)</span> | Hersteller-Typbezeichnung | string |
| <span className="hbs-f hbs-e1">[simKartenNummer](/bo4e/202604/com/Geraeteeigenschaften#simkartennummer)</span> | SIM-Kartennummer | string |
| <span className="hbs-f hbs-e1">[modemKennungIMSI](/bo4e/202604/com/Geraeteeigenschaften#modemkennungimsi)</span> | Modem-Kennung (IMSI) | string |
| <span className="hbs-f hbs-e1">[tkProvider](/bo4e/202604/com/Geraeteeigenschaften#tkprovider)</span> | Telekommunikationsanbieter | string |
| <span className="hbs-f hbs-e1">[ipVersion](/bo4e/202604/com/Geraeteeigenschaften#ipversion)</span> | IP-Version | string |
| <span className="hbs-f hbs-e0">[volumenerfassung](/bo4e/202604/com/Geraet#volumenerfassung)</span> | Volumenerfassung | [Enum Volumenerfassung](/bo4e/202604/enum/Volumenerfassung)<br/><Werte>`HOCHFREQUENZSONDE`, `KENNLINIENKORREKTUR`, `SCHLEICHMENGENUNTERDRUECKUNG`</Werte> |
| <span className="hbs-f hbs-e0">[weitereGeraetenummern](/bo4e/202604/com/Geraet#weiteregeraetenummern) <span className="hbs-liste">[ ]</span></span> | weitereGeraetenummern | string[] |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### geraetetyp

16 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55035](/schnittstellen/202604/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete |
| [PI_55060](/schnittstellen/202604/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete |
| [PI_55074](/schnittstellen/202604/pruefi/UTILMD/PI_55074) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete |
| [PI_55075](/schnittstellen/202604/pruefi/UTILMD/PI_55075) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete |
| [PI_55095](/schnittstellen/202604/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete |
| [PI_55553](/schnittstellen/202604/pruefi/UTILMD/PI_55553) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete |
| [PI_55555](/schnittstellen/202604/pruefi/UTILMD/PI_55555) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete |
| [PI_55643](/schnittstellen/202604/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete |
| [PI_55648](/schnittstellen/202604/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete |
| [PI_55653](/schnittstellen/202604/pruefi/UTILMD/PI_55653) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete |
| [PI_55658](/schnittstellen/202604/pruefi/UTILMD/PI_55658) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete |
| [PI_55663](/schnittstellen/202604/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete |
| [PI_55669](/schnittstellen/202604/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete |

### geraetenummer

34 Verwendung(en) in den Nachrichtentypen ORDERS, UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_17009](/schnittstellen/202604/pruefi/ORDERS/PI_17009) | Prüfi | ORDERS | stammdaten › ZAEHLER › geraete |
| [PI_17101](/schnittstellen/202604/pruefi/ORDERS/PI_17101) | Prüfi | ORDERS | stammdaten › ZAEHLER › geraete |
| [PI_17126](/schnittstellen/202604/pruefi/ORDERS/PI_17126) | Prüfi | ORDERS | stammdaten › ZAEHLER › geraete |
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › geraete |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › geraete |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › geraete |
| [PI_44035](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44035) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › geraete |
| [PI_44043](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44043) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › geraete |
| [PI_44060](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44060) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › geraete |
| [PI_44116](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44116) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › geraete |
| [PI_44117](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44117) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › geraete |
| [PI_44143](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44143) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › geraete |
| [PI_44145](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44145) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › geraete |
| [PI_44147](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44147) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › geraete |
| [PI_44148](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44148) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › geraete |
| [PI_44149](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44149) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › geraete |
| [PI_44168](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › geraete |
| [PI_55035](/schnittstellen/202604/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete |
| [PI_55060](/schnittstellen/202604/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete |
| [PI_55074](/schnittstellen/202604/pruefi/UTILMD/PI_55074) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete |
| [PI_55075](/schnittstellen/202604/pruefi/UTILMD/PI_55075) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete |
| [PI_55095](/schnittstellen/202604/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete |
| [PI_55194](/schnittstellen/202604/pruefi/UTILMD/PI_55194) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete |
| [PI_55553](/schnittstellen/202604/pruefi/UTILMD/PI_55553) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete |
| [PI_55555](/schnittstellen/202604/pruefi/UTILMD/PI_55555) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete |
| [PI_55643](/schnittstellen/202604/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete |
| [PI_55648](/schnittstellen/202604/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete |
| [PI_55653](/schnittstellen/202604/pruefi/UTILMD/PI_55653) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete |
| [PI_55658](/schnittstellen/202604/pruefi/UTILMD/PI_55658) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete |
| [PI_55663](/schnittstellen/202604/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete |
| [PI_55669](/schnittstellen/202604/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete |

### weitereGeraetenummern

13 Verwendung(en) in den Nachrichtentypen ORDERS, UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_17009](/schnittstellen/202604/pruefi/ORDERS/PI_17009) | Prüfi | ORDERS | stammdaten › ZAEHLER › geraete |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete |
| [PI_55060](/schnittstellen/202604/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete |
| [PI_55074](/schnittstellen/202604/pruefi/UTILMD/PI_55074) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete |
| [PI_55075](/schnittstellen/202604/pruefi/UTILMD/PI_55075) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete |
| [PI_55643](/schnittstellen/202604/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete |
| [PI_55648](/schnittstellen/202604/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete |
| [PI_55653](/schnittstellen/202604/pruefi/UTILMD/PI_55653) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete |
| [PI_55658](/schnittstellen/202604/pruefi/UTILMD/PI_55658) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete |
| [PI_55663](/schnittstellen/202604/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete |
| [PI_55669](/schnittstellen/202604/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | stammdaten › ZAEHLER › geraete |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
