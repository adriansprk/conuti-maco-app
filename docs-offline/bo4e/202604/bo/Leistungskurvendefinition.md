# Leistungskurvendefinition
<span hidden data-pagefind-meta={"title:Leistungskurvendefinition — BO4E-Geschäftsobjekt (FV 202604)"} />

BO4E-Geschäftsobjekt · 8 Felder · 7 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="botyp"></a>`boTyp` <span className="hbs-pflicht">\*</span> | [Enum BOTyp](/bo4e/202604/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> | Typ des BO |
| <a id="versionstruktur"></a>`versionStruktur` <span className="hbs-pflicht">\*</span> | string | versionStruktur |
| <a id="beginndatum"></a>`beginndatum` | string (date-time) | beginndatum |
| <a id="endedatum"></a>`endedatum` | string (date-time) | endedatum |
| <a id="version"></a>`version` | string (date-time) | version |
| <a id="code"></a>`code` | string | code |
| <a id="notwendigkeit"></a>`notwendigkeit` | [Enum DefinitionenNotwendigkeit](/bo4e/202604/enum/DefinitionenNotwendigkeit)<br/><Werte>`ZAEHLZEITDEFINITIONEN_WERDEN_VERWENDET`, `ZAEHLZEITDEFINITIONEN_WERDEN_NICHT_VERWENDET`, `DEFINITIONEN_WERDEN_VERWENDET`, `DEFINITIONEN_WERDEN_NICHT_VERWENDET`</Werte> | DefinitionenNotwendigkeit |
| <a id="leistungskurven"></a>`leistungskurven` | [Leistungskurve[]](/bo4e/202604/com/Leistungskurve) | leistungskurven |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[boTyp](/bo4e/202604/bo/Leistungskurvendefinition#botyp) <span className="hbs-pflicht">\*</span></span> | Typ des BO | [Enum BOTyp](/bo4e/202604/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> |
| <span className="hbs-f hbs-e0">[versionStruktur](/bo4e/202604/bo/Leistungskurvendefinition#versionstruktur) <span className="hbs-pflicht">\*</span></span> | versionStruktur | string |
| <span className="hbs-f hbs-e0">[beginndatum](/bo4e/202604/bo/Leistungskurvendefinition#beginndatum)</span> | beginndatum | string (date-time) |
| <span className="hbs-f hbs-e0">[endedatum](/bo4e/202604/bo/Leistungskurvendefinition#endedatum)</span> | endedatum | string (date-time) |
| <span className="hbs-f hbs-e0">[version](/bo4e/202604/bo/Leistungskurvendefinition#version)</span> | version | string (date-time) |
| <span className="hbs-f hbs-e0">[code](/bo4e/202604/bo/Leistungskurvendefinition#code)</span> | code | string |
| <span className="hbs-f hbs-e0">[notwendigkeit](/bo4e/202604/bo/Leistungskurvendefinition#notwendigkeit)</span> | DefinitionenNotwendigkeit | [Enum DefinitionenNotwendigkeit](/bo4e/202604/enum/DefinitionenNotwendigkeit)<br/><Werte>`ZAEHLZEITDEFINITIONEN_WERDEN_VERWENDET`, `ZAEHLZEITDEFINITIONEN_WERDEN_NICHT_VERWENDET`, `DEFINITIONEN_WERDEN_VERWENDET`, `DEFINITIONEN_WERDEN_NICHT_VERWENDET`</Werte> |
| <span className="hbs-g hbs-e0">[leistungskurven](/bo4e/202604/bo/Leistungskurvendefinition#leistungskurven) <span className="hbs-liste">[ ]</span></span> | leistungskurven | [Leistungskurve[]](/bo4e/202604/com/Leistungskurve) |
| <span className="hbs-f hbs-e1">[code](/bo4e/202604/com/Leistungskurve#code)</span> | Code der Leistungskurve | string |
| <span className="hbs-f hbs-e1">[aenderungszeitpunkt](/bo4e/202604/com/Leistungskurve#aenderungszeitpunkt)</span> | Änderungszeitpunkt | string (date-time) |
| <span className="hbs-f hbs-e1">[haeufigkeit](/bo4e/202604/com/Leistungskurve#haeufigkeit)</span> | HaeufigkeitLeistungskurve | [Enum HaeufigkeitLeistungskurve](/bo4e/202604/enum/HaeufigkeitLeistungskurve)<br/><Werte>`EINMALIG`, `JAEHRLICH`</Werte> |
| <span className="hbs-f hbs-e1">[uebermittelbarkeit](/bo4e/202604/com/Leistungskurve#uebermittelbarkeit)</span> | UebermittelbarkeitLeistungskurve | [Enum UebermittelbarkeitLeistungskurve](/bo4e/202604/enum/UebermittelbarkeitLeistungskurve)<br/><Werte>`ELEKTRONISCH`, `NICHT_ELEKTRONISCH`</Werte> |
| <span className="hbs-g hbs-e1">[schwellwert](/bo4e/202604/com/Leistungskurve#schwellwert)</span> | — | [Schwellwert](/bo4e/202604/com/Schwellwert) |
| <span className="hbs-f hbs-e2">[obererSchwellwert](/bo4e/202604/com/Schwellwert#obererschwellwert)</span> | obererSchwellwert | number (float) |
| <span className="hbs-f hbs-e2">[untererSchwellwert](/bo4e/202604/com/Schwellwert#untererschwellwert)</span> | untererSchwellwert | number (float) |
| <span className="hbs-f hbs-e2">[konfigurationsprodukt](/bo4e/202604/com/Schwellwert#konfigurationsprodukt)</span> | konfigurationsprodukt | string |
| <span className="hbs-f hbs-e1">[konfigurationsprodukt](/bo4e/202604/com/Leistungskurve#konfigurationsprodukt)</span> | Konfigurationsprodukt | string |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### beginndatum

2 Verwendung(en) in den Nachrichtentypen UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_25007](/schnittstellen/202604/pruefi/UTILTS/PI_25007) | Prüfi | UTILTS | stammdaten › LEISTUNGSKURVENDEFINITION |
| [PI_25009](/schnittstellen/202604/pruefi/UTILTS/PI_25009) | Prüfi | UTILTS | stammdaten › LEISTUNGSKURVENDEFINITION |

### endedatum

1 Verwendung(en) in den Nachrichtentypen UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_25009](/schnittstellen/202604/pruefi/UTILTS/PI_25009) | Prüfi | UTILTS | stammdaten › LEISTUNGSKURVENDEFINITION |

### version

2 Verwendung(en) in den Nachrichtentypen UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_25007](/schnittstellen/202604/pruefi/UTILTS/PI_25007) | Prüfi | UTILTS | stammdaten › LEISTUNGSKURVENDEFINITION |
| [PI_25009](/schnittstellen/202604/pruefi/UTILTS/PI_25009) | Prüfi | UTILTS | stammdaten › LEISTUNGSKURVENDEFINITION |

### code

1 Verwendung(en) in den Nachrichtentypen UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_25009](/schnittstellen/202604/pruefi/UTILTS/PI_25009) | Prüfi | UTILTS | stammdaten › LEISTUNGSKURVENDEFINITION |

### notwendigkeit

1 Verwendung(en) in den Nachrichtentypen UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_25007](/schnittstellen/202604/pruefi/UTILTS/PI_25007) | Prüfi | UTILTS | stammdaten › LEISTUNGSKURVENDEFINITION |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
