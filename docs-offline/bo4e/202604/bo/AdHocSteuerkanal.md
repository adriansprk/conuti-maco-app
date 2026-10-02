# AdHocSteuerkanal
<span hidden data-pagefind-meta={"title:AdHocSteuerkanal — BO4E-Geschäftsobjekt (FV 202604)"} />

BO4E-Geschäftsobjekt · 7 Felder · 3 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="botyp"></a>`boTyp` <span className="hbs-pflicht">\*</span> | [Enum BOTyp](/bo4e/202604/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> | Typ des BO |
| <a id="versionstruktur"></a>`versionStruktur` <span className="hbs-pflicht">\*</span> | string | versionStruktur |
| <a id="konfigurationsprodukt"></a>`konfigurationsprodukt` | string | konfigurationsprodukt |
| <a id="zieladresse"></a>`zieladresse` | [Zieladresse](/bo4e/202604/com/Zieladresse) | — |
| <a id="aussteller"></a>`aussteller` | [Aussteller](/bo4e/202604/com/Aussteller) | — |
| <a id="zertifikatsnutzer"></a>`zertifikatsNutzer` | [ZertifikatsNutzer](/bo4e/202604/com/ZertifikatsNutzer) | — |
| <a id="ipadresseclsdevice"></a>`IPAdresseCLSDevice` | [IPAdresseCLSDevice](/bo4e/202604/com/IPAdresseCLSDevice) | — |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[boTyp](/bo4e/202604/bo/AdHocSteuerkanal#botyp) <span className="hbs-pflicht">\*</span></span> | Typ des BO | [Enum BOTyp](/bo4e/202604/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> |
| <span className="hbs-f hbs-e0">[versionStruktur](/bo4e/202604/bo/AdHocSteuerkanal#versionstruktur) <span className="hbs-pflicht">\*</span></span> | versionStruktur | string |
| <span className="hbs-f hbs-e0">[konfigurationsprodukt](/bo4e/202604/bo/AdHocSteuerkanal#konfigurationsprodukt)</span> | konfigurationsprodukt | string |
| <span className="hbs-g hbs-e0">[zieladresse](/bo4e/202604/bo/AdHocSteuerkanal#zieladresse)</span> | — | [Zieladresse](/bo4e/202604/com/Zieladresse) |
| <span className="hbs-f hbs-e1">[zieladresse1](/bo4e/202604/com/Zieladresse#zieladresse1)</span> | zieladresse1 | string |
| <span className="hbs-f hbs-e1">[zieladresse2](/bo4e/202604/com/Zieladresse#zieladresse2)</span> | zieladresse2 | string |
| <span className="hbs-f hbs-e1">[zieladresse3](/bo4e/202604/com/Zieladresse#zieladresse3)</span> | zieladresse3 | string |
| <span className="hbs-f hbs-e1">[zieladresse4](/bo4e/202604/com/Zieladresse#zieladresse4)</span> | zieladresse4 | string |
| <span className="hbs-f hbs-e1">[zieladresse5](/bo4e/202604/com/Zieladresse#zieladresse5)</span> | zieladresse5 | string |
| <span className="hbs-g hbs-e0">[aussteller](/bo4e/202604/bo/AdHocSteuerkanal#aussteller)</span> | — | [Aussteller](/bo4e/202604/com/Aussteller) |
| <span className="hbs-f hbs-e1">[aussteller1](/bo4e/202604/com/Aussteller#aussteller1)</span> | aussteller1 | string |
| <span className="hbs-f hbs-e1">[aussteller2](/bo4e/202604/com/Aussteller#aussteller2)</span> | aussteller2 | string |
| <span className="hbs-f hbs-e1">[aussteller3](/bo4e/202604/com/Aussteller#aussteller3)</span> | aussteller3 | string |
| <span className="hbs-f hbs-e1">[aussteller4](/bo4e/202604/com/Aussteller#aussteller4)</span> | aussteller4 | string |
| <span className="hbs-f hbs-e1">[aussteller5](/bo4e/202604/com/Aussteller#aussteller5)</span> | aussteller5 | string |
| <span className="hbs-g hbs-e0">[zertifikatsNutzer](/bo4e/202604/bo/AdHocSteuerkanal#zertifikatsnutzer)</span> | — | [ZertifikatsNutzer](/bo4e/202604/com/ZertifikatsNutzer) |
| <span className="hbs-f hbs-e1">[zertifikatsNutzer1](/bo4e/202604/com/ZertifikatsNutzer#zertifikatsnutzer1)</span> | zertifikatsNutzer1 | string |
| <span className="hbs-f hbs-e1">[zertifikatsNutzer2](/bo4e/202604/com/ZertifikatsNutzer#zertifikatsnutzer2)</span> | zertifikatsNutzer2 | string |
| <span className="hbs-f hbs-e1">[zertifikatsNutzer3](/bo4e/202604/com/ZertifikatsNutzer#zertifikatsnutzer3)</span> | zertifikatsNutzer3 | string |
| <span className="hbs-f hbs-e1">[zertifikatsNutzer4](/bo4e/202604/com/ZertifikatsNutzer#zertifikatsnutzer4)</span> | zertifikatsNutzer4 | string |
| <span className="hbs-f hbs-e1">[zertifikatsNutzer5](/bo4e/202604/com/ZertifikatsNutzer#zertifikatsnutzer5)</span> | zertifikatsNutzer5 | string |
| <span className="hbs-g hbs-e0">[IPAdresseCLSDevice](/bo4e/202604/bo/AdHocSteuerkanal#ipadresseclsdevice)</span> | — | [IPAdresseCLSDevice](/bo4e/202604/com/IPAdresseCLSDevice) |
| <span className="hbs-f hbs-e1">[IPAdresseCLSDevice1](/bo4e/202604/com/IPAdresseCLSDevice#ipadresseclsdevice1)</span> | IPAdresseCLSDevice1 | string |
| <span className="hbs-f hbs-e1">[IPAdresseCLSDevice2](/bo4e/202604/com/IPAdresseCLSDevice#ipadresseclsdevice2)</span> | IPAdresseCLSDevice2 | string |
| <span className="hbs-f hbs-e1">[IPAdresseCLSDevice3](/bo4e/202604/com/IPAdresseCLSDevice#ipadresseclsdevice3)</span> | IPAdresseCLSDevice3 | string |
| <span className="hbs-f hbs-e1">[IPAdresseCLSDevice4](/bo4e/202604/com/IPAdresseCLSDevice#ipadresseclsdevice4)</span> | IPAdresseCLSDevice4 | string |
| <span className="hbs-f hbs-e1">[IPAdresseCLSDevice5](/bo4e/202604/com/IPAdresseCLSDevice#ipadresseclsdevice5)</span> | IPAdresseCLSDevice5 | string |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### konfigurationsprodukt

3 Verwendung(en) in den Nachrichtentypen ORDERS, QUOTES, REQOTE.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_15004](/schnittstellen/202604/pruefi/QUOTES/PI_15004) | Prüfi | QUOTES | stammdaten › AD_HOC_STEUERKANAL |
| [PI_17128](/schnittstellen/202604/pruefi/ORDERS/PI_17128) | Prüfi | ORDERS | stammdaten › AD_HOC_STEUERKANAL |
| [PI_35004](/schnittstellen/202604/pruefi/REQOTE/PI_35004) | Prüfi | REQOTE | stammdaten › AD_HOC_STEUERKANAL |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
