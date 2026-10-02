# Schaltzeitdefinition
<span hidden data-pagefind-meta={"title:Schaltzeitdefinition — BO4E-Geschäftsobjekt (FV 202610)"} />

BO4E-Geschäftsobjekt · 8 Felder · 7 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="botyp"></a>`boTyp` <span className="hbs-pflicht">\*</span> | [Enum BOTyp](/bo4e/202610/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> | Typ des BO |
| <a id="versionstruktur"></a>`versionStruktur` <span className="hbs-pflicht">\*</span> | string | versionStruktur |
| <a id="beginndatum"></a>`beginndatum` | string (date-time) | beginndatum |
| <a id="endedatum"></a>`endedatum` | string (date-time) | endedatum |
| <a id="version"></a>`version` | string (date-time) | version |
| <a id="code"></a>`code` | string | code |
| <a id="notwendigkeit"></a>`notwendigkeit` | [Enum DefinitionenNotwendigkeit](/bo4e/202610/enum/DefinitionenNotwendigkeit)<br/><Werte>`ZAEHLZEITDEFINITIONEN_WERDEN_VERWENDET`, `ZAEHLZEITDEFINITIONEN_WERDEN_NICHT_VERWENDET`, `DEFINITIONEN_WERDEN_VERWENDET`, `DEFINITIONEN_WERDEN_NICHT_VERWENDET`</Werte> | DefinitionenNotwendigkeit |
| <a id="schaltzeiten"></a>`schaltzeiten` | [Schaltzeit[]](/bo4e/202610/com/Schaltzeit) | schaltzeiten |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[boTyp](/bo4e/202610/bo/Schaltzeitdefinition#botyp) <span className="hbs-pflicht">\*</span></span> | Typ des BO | [Enum BOTyp](/bo4e/202610/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> |
| <span className="hbs-f hbs-e0">[versionStruktur](/bo4e/202610/bo/Schaltzeitdefinition#versionstruktur) <span className="hbs-pflicht">\*</span></span> | versionStruktur | string |
| <span className="hbs-f hbs-e0">[beginndatum](/bo4e/202610/bo/Schaltzeitdefinition#beginndatum)</span> | beginndatum | string (date-time) |
| <span className="hbs-f hbs-e0">[endedatum](/bo4e/202610/bo/Schaltzeitdefinition#endedatum)</span> | endedatum | string (date-time) |
| <span className="hbs-f hbs-e0">[version](/bo4e/202610/bo/Schaltzeitdefinition#version)</span> | version | string (date-time) |
| <span className="hbs-f hbs-e0">[code](/bo4e/202610/bo/Schaltzeitdefinition#code)</span> | code | string |
| <span className="hbs-f hbs-e0">[notwendigkeit](/bo4e/202610/bo/Schaltzeitdefinition#notwendigkeit)</span> | DefinitionenNotwendigkeit | [Enum DefinitionenNotwendigkeit](/bo4e/202610/enum/DefinitionenNotwendigkeit)<br/><Werte>`ZAEHLZEITDEFINITIONEN_WERDEN_VERWENDET`, `ZAEHLZEITDEFINITIONEN_WERDEN_NICHT_VERWENDET`, `DEFINITIONEN_WERDEN_VERWENDET`, `DEFINITIONEN_WERDEN_NICHT_VERWENDET`</Werte> |
| <span className="hbs-g hbs-e0">[schaltzeiten](/bo4e/202610/bo/Schaltzeitdefinition#schaltzeiten) <span className="hbs-liste">[ ]</span></span> | schaltzeiten | [Schaltzeit[]](/bo4e/202610/com/Schaltzeit) |
| <span className="hbs-f hbs-e1">[code](/bo4e/202610/com/Schaltzeit#code)</span> | code | string |
| <span className="hbs-f hbs-e1">[aenderungszeitpunkt](/bo4e/202610/com/Schaltzeit#aenderungszeitpunkt)</span> | aenderungszeitpunkt | string (date-time) |
| <span className="hbs-f hbs-e1">[haeufigkeit](/bo4e/202610/com/Schaltzeit#haeufigkeit)</span> | HaeufigkeitSchaltzeit | [Enum HaeufigkeitSchaltzeit](/bo4e/202610/enum/HaeufigkeitSchaltzeit)<br/><Werte>`EINMALIG`, `JAEHRLICH`</Werte> |
| <span className="hbs-f hbs-e1">[uebermittelbarkeit](/bo4e/202610/com/Schaltzeit#uebermittelbarkeit)</span> | UebermittelbarkeitSchaltzeit | [Enum UebermittelbarkeitSchaltzeit](/bo4e/202610/enum/UebermittelbarkeitSchaltzeit)<br/><Werte>`ELEKTRONISCH`, `NICHT_ELEKTRONISCH`</Werte> |
| <span className="hbs-f hbs-e1">[schalthandlung](/bo4e/202610/com/Schaltzeit#schalthandlung)</span> | Schalthandlung | [Enum Schalthandlung](/bo4e/202610/enum/Schalthandlung)<br/><Werte>`LEISTUNG_AN`, `LEISTUNG_AUS`</Werte> |
| <span className="hbs-f hbs-e1">[konfigurationsprodukt](/bo4e/202610/com/Schaltzeit#konfigurationsprodukt)</span> | konfigurationsprodukt | string |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### beginndatum

2 Verwendung(en) in den Nachrichtentypen UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_25006](/schnittstellen/202610/pruefi/UTILTS/PI_25006) | Prüfi | UTILTS | stammdaten › SCHALTZEITDEFINITION |
| [PI_25008](/schnittstellen/202610/pruefi/UTILTS/PI_25008) | Prüfi | UTILTS | stammdaten › SCHALTZEITDEFINITION |

### endedatum

1 Verwendung(en) in den Nachrichtentypen UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_25008](/schnittstellen/202610/pruefi/UTILTS/PI_25008) | Prüfi | UTILTS | stammdaten › SCHALTZEITDEFINITION |

### version

2 Verwendung(en) in den Nachrichtentypen UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_25006](/schnittstellen/202610/pruefi/UTILTS/PI_25006) | Prüfi | UTILTS | stammdaten › SCHALTZEITDEFINITION |
| [PI_25008](/schnittstellen/202610/pruefi/UTILTS/PI_25008) | Prüfi | UTILTS | stammdaten › SCHALTZEITDEFINITION |

### code

1 Verwendung(en) in den Nachrichtentypen UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_25008](/schnittstellen/202610/pruefi/UTILTS/PI_25008) | Prüfi | UTILTS | stammdaten › SCHALTZEITDEFINITION |

### notwendigkeit

1 Verwendung(en) in den Nachrichtentypen UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_25006](/schnittstellen/202610/pruefi/UTILTS/PI_25006) | Prüfi | UTILTS | stammdaten › SCHALTZEITDEFINITION |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
