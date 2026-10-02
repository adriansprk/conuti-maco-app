# Bilanzkreis
<span hidden data-pagefind-meta={"title:Bilanzkreis — BO4E-Geschäftsobjekt (FV 202610)"} />

BO4E-Geschäftsobjekt · 4 Felder · 11 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="botyp"></a>`boTyp` | [Enum BOTyp](/bo4e/202610/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> | Typ des BO |
| <a id="versionstruktur"></a>`versionStruktur` | string | versionStruktur |
| <a id="bezeichnung"></a>`bezeichnung` | string | Externe Bezeichnung |
| <a id="prioritaet"></a>`prioritaet` | integer | prioritaet |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[boTyp](/bo4e/202610/bo/Bilanzkreis#botyp)</span> | Typ des BO | [Enum BOTyp](/bo4e/202610/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> |
| <span className="hbs-f hbs-e0">[versionStruktur](/bo4e/202610/bo/Bilanzkreis#versionstruktur)</span> | versionStruktur | string |
| <span className="hbs-f hbs-e0">[bezeichnung](/bo4e/202610/bo/Bilanzkreis#bezeichnung)</span> | Externe Bezeichnung | string |
| <span className="hbs-f hbs-e0">[prioritaet](/bo4e/202610/bo/Bilanzkreis#prioritaet)</span> | prioritaet | integer |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### bezeichnung

10 Verwendung(en) in den Nachrichtentypen UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_44001](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44001) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › bilanzkreise |
| [PI_44002](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › bilanzkreise |
| [PI_44013](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › bilanzkreise |
| [PI_44014](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › bilanzkreise |
| [PI_44019](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44019) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › bilanzkreise |
| [PI_44020](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44020) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › bilanzkreise |
| [PI_44021](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44021) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › bilanzkreise |
| [PI_44120](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44120) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › bilanzkreise |
| [PI_44150](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44150) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › bilanzkreise |
| [PI_44151](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44151) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › bilanzkreise |

### prioritaet

1 Verwendung(en) in den Nachrichtentypen UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_44001](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44001) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › bilanzkreise |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
