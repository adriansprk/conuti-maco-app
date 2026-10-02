# Zaehlzeitdefinition
<span hidden data-pagefind-meta={"title:Zaehlzeitdefinition — BO4E-Geschäftsobjekt (FV 202610)"} />

BO4E-Geschäftsobjekt · 10 Felder · 7 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="botyp"></a>`boTyp` <span className="hbs-pflicht">\*</span> | [Enum BOTyp](/bo4e/202610/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> | Typ des BO |
| <a id="versionstruktur"></a>`versionStruktur` <span className="hbs-pflicht">\*</span> | string | versionStruktur |
| <a id="beginndatum"></a>`beginndatum` | string (date-time) | Der inklusive Zeitpunkt ab dem die Zaehlzeitdefinitionen ausgerollt sind |
| <a id="endedatum"></a>`endedatum` | string (date-time) | Der exklusive Zeitpunkt bis zu dem die Zaehlzeitdefinitionen ausgerollt sind |
| <a id="version"></a>`version` | string (date-time) | Version der Zählzeitdefinition als Datum |
| <a id="notwendigkeit"></a>`notwendigkeit` | [Enum DefinitionenNotwendigkeit](/bo4e/202610/enum/DefinitionenNotwendigkeit)<br/><Werte>`ZAEHLZEITDEFINITIONEN_WERDEN_VERWENDET`, `ZAEHLZEITDEFINITIONEN_WERDEN_NICHT_VERWENDET`, `DEFINITIONEN_WERDEN_VERWENDET`, `DEFINITIONEN_WERDEN_NICHT_VERWENDET`</Werte> | Beschreibt ob eine Zaehlzeitdefinitionen notwendig ist |
| <a id="versionsangabe"></a>`versionsangabe` | string | versionsangabe |
| <a id="code"></a>`code` | string | Zählzeitdefinition |
| <a id="zaehlzeiten"></a>`zaehlzeiten` | [Zaehlzeit[]](/bo4e/202610/com/Zaehlzeit) | Liste der Zählzeiten [1 - 99999] |
| <a id="zaehlzeitregister"></a>`zaehlzeitregister` | [Zaehlzeitregister[]](/bo4e/202610/com/Zaehlzeitregister) | Liste der Zählzeitregister |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[boTyp](/bo4e/202610/bo/Zaehlzeitdefinition#botyp) <span className="hbs-pflicht">\*</span></span> | Typ des BO | [Enum BOTyp](/bo4e/202610/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> |
| <span className="hbs-f hbs-e0">[versionStruktur](/bo4e/202610/bo/Zaehlzeitdefinition#versionstruktur) <span className="hbs-pflicht">\*</span></span> | versionStruktur | string |
| <span className="hbs-f hbs-e0">[beginndatum](/bo4e/202610/bo/Zaehlzeitdefinition#beginndatum)</span> | Der inklusive Zeitpunkt ab dem die Zaehlzeitdefinitionen ausgerollt sind | string (date-time) |
| <span className="hbs-f hbs-e0">[endedatum](/bo4e/202610/bo/Zaehlzeitdefinition#endedatum)</span> | Der exklusive Zeitpunkt bis zu dem die Zaehlzeitdefinitionen ausgerollt sind | string (date-time) |
| <span className="hbs-f hbs-e0">[version](/bo4e/202610/bo/Zaehlzeitdefinition#version)</span> | Version der Zählzeitdefinition als Datum | string (date-time) |
| <span className="hbs-f hbs-e0">[notwendigkeit](/bo4e/202610/bo/Zaehlzeitdefinition#notwendigkeit)</span> | Beschreibt ob eine Zaehlzeitdefinitionen notwendig ist | [Enum DefinitionenNotwendigkeit](/bo4e/202610/enum/DefinitionenNotwendigkeit)<br/><Werte>`ZAEHLZEITDEFINITIONEN_WERDEN_VERWENDET`, `ZAEHLZEITDEFINITIONEN_WERDEN_NICHT_VERWENDET`, `DEFINITIONEN_WERDEN_VERWENDET`, `DEFINITIONEN_WERDEN_NICHT_VERWENDET`</Werte> |
| <span className="hbs-f hbs-e0">[versionsangabe](/bo4e/202610/bo/Zaehlzeitdefinition#versionsangabe)</span> | versionsangabe | string |
| <span className="hbs-f hbs-e0">[code](/bo4e/202610/bo/Zaehlzeitdefinition#code)</span> | Zählzeitdefinition | string |
| <span className="hbs-g hbs-e0">[zaehlzeiten](/bo4e/202610/bo/Zaehlzeitdefinition#zaehlzeiten) <span className="hbs-liste">[ ]</span></span> | Liste der Zählzeiten [1 - 99999] | [Zaehlzeit[]](/bo4e/202610/com/Zaehlzeit) |
| <span className="hbs-f hbs-e1">[code](/bo4e/202610/com/Zaehlzeit#code)</span> | Zählzeitdefinition | string |
| <span className="hbs-f hbs-e1">[haeufigkeit](/bo4e/202610/com/Zaehlzeit#haeufigkeit)</span> | Häufigkeit der Übermittlung | [Enum HaeufigkeitZaehlzeit](/bo4e/202610/enum/HaeufigkeitZaehlzeit)<br/><Werte>`EINMALIG`, `JAEHRLICH`</Werte> |
| <span className="hbs-f hbs-e1">[uebermittelbarkeit](/bo4e/202610/com/Zaehlzeit#uebermittelbarkeit)</span> | Art der Übermittlung | [Enum UebermittelbarkeitZaehlzeit](/bo4e/202610/enum/UebermittelbarkeitZaehlzeit)<br/><Werte>`ELEKTRONISCH`, `NICHT_ELEKTRONISCH`</Werte> |
| <span className="hbs-f hbs-e1">[ermittlungLeistungsmaximum](/bo4e/202610/com/Zaehlzeit#ermittlungleistungsmaximum)</span> | Ermittlung Leistungsmaximum | [Enum ErmittlungLeistungsmaximum](/bo4e/202610/enum/ErmittlungLeistungsmaximum)<br/><Werte>`VERWENDUNG_HOCHLASTFENSTER`, `KEINE_VERWENDUNG_HOCHLASTFENSTER`</Werte> |
| <span className="hbs-f hbs-e1">[istBestellbar](/bo4e/202610/com/Zaehlzeit#istbestellbar)</span> | Ist die Zählzeit bestellbar? | boolean |
| <span className="hbs-f hbs-e1">[typ](/bo4e/202610/com/Zaehlzeit#typ)</span> | ZählzeitdefinitionTyp | [Enum ZaehlzeitdefinitionTyp](/bo4e/202610/enum/ZaehlzeitdefinitionTyp)<br/><Werte>`WAERMEPUMPE`, `NACHTSPEICHERHEIZUNG`, `SCHWACHLASTZEITFENSTER`, `SONSTIGE`, `HOCHLASTZEITFENSTER`</Werte> |
| <span className="hbs-f hbs-e1">[beschreibungTyp](/bo4e/202610/com/Zaehlzeit#beschreibungtyp)</span> | Beschreibung des ZählzeitdefinitionTyp | string |
| <span className="hbs-f hbs-e1">[aenderungszeitpunkt](/bo4e/202610/com/Zaehlzeit#aenderungszeitpunkt)</span> | aenderungszeitpunkt | string (date-time) |
| <span className="hbs-f hbs-e1">[register](/bo4e/202610/com/Zaehlzeit#register)</span> | register | string |
| <span className="hbs-g hbs-e0">[zaehlzeitregister](/bo4e/202610/bo/Zaehlzeitdefinition#zaehlzeitregister) <span className="hbs-liste">[ ]</span></span> | Liste der Zählzeitregister | [Zaehlzeitregister[]](/bo4e/202610/com/Zaehlzeitregister) |
| <span className="hbs-f hbs-e1">[register](/bo4e/202610/com/Zaehlzeitregister#register)</span> | Zählzeitregister | string |
| <span className="hbs-f hbs-e1">[zaehlzeitDefinition](/bo4e/202610/com/Zaehlzeitregister#zaehlzeitdefinition)</span> | Zählzeitdefinition | string |
| <span className="hbs-f hbs-e1">[schwachlastfaehig](/bo4e/202610/com/Zaehlzeitregister#schwachlastfaehig)</span> | Schwachlastfähigkeit des Registers | [Enum Schwachlastfaehig](/bo4e/202610/enum/Schwachlastfaehig)<br/><Werte>`SCHWACHLASTFAEHIG`, `NICHT_SCHWACHLASTFAEHIG`</Werte> |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### beginndatum

2 Verwendung(en) in den Nachrichtentypen UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_25004](/schnittstellen/202610/pruefi/UTILTS/PI_25004) | Prüfi | UTILTS | stammdaten › ZAEHLZEITDEFINITION |
| [PI_25005](/schnittstellen/202610/pruefi/UTILTS/PI_25005) | Prüfi | UTILTS | stammdaten › ZAEHLZEITDEFINITION |

### endedatum

1 Verwendung(en) in den Nachrichtentypen UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_25005](/schnittstellen/202610/pruefi/UTILTS/PI_25005) | Prüfi | UTILTS | stammdaten › ZAEHLZEITDEFINITION |

### version

2 Verwendung(en) in den Nachrichtentypen UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_25004](/schnittstellen/202610/pruefi/UTILTS/PI_25004) | Prüfi | UTILTS | stammdaten › ZAEHLZEITDEFINITION |
| [PI_25005](/schnittstellen/202610/pruefi/UTILTS/PI_25005) | Prüfi | UTILTS | stammdaten › ZAEHLZEITDEFINITION |

### notwendigkeit

1 Verwendung(en) in den Nachrichtentypen UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_25004](/schnittstellen/202610/pruefi/UTILTS/PI_25004) | Prüfi | UTILTS | stammdaten › ZAEHLZEITDEFINITION |

### code

1 Verwendung(en) in den Nachrichtentypen UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_25005](/schnittstellen/202610/pruefi/UTILTS/PI_25005) | Prüfi | UTILTS | stammdaten › ZAEHLZEITDEFINITION |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
