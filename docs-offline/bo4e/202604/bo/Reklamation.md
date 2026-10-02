# Reklamation
<span hidden data-pagefind-meta={"title:Reklamation — BO4E-Geschäftsobjekt (FV 202604)"} />

BO4E-Geschäftsobjekt · 9 Felder · 6 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="botyp"></a>`boTyp` <span className="hbs-pflicht">\*</span> | [Enum BOTyp](/bo4e/202604/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> | Typ des BO |
| <a id="versionstruktur"></a>`versionStruktur` <span className="hbs-pflicht">\*</span> | string | versionStruktur |
| <a id="lokationsid"></a>`lokationsId` | string | Für welche Markt- oder Messlokation gilt diese Reklamation. |
| <a id="lokationstyp"></a>`lokationsTyp` | [Enum Lokationstyp](/bo4e/202604/enum/Lokationstyp)<br/><Werte>`MALO`, `MELO`, `NELO`, `TECHNISCHE_RESSOURCE`, `STEUERBARE_RESSOURCE`, `TRANCHE`, `MABIS_ZAEHLPUNKT`</Werte> | Gibt an, ob es sich um eine Markt- oder Messlokation handelt. |
| <a id="obiskennzahl"></a>`obiskennzahl` | string | OBIS-Kennzahl |
| <a id="zeitraummesswertanfrage"></a>`zeitraumMesswertanfrage` | [Zeitraum](/bo4e/202604/com/Zeitraum) | — |
| <a id="reklamationsgrund"></a>`reklamationsgrund` | [Enum Reklamationsgrund](/bo4e/202604/enum/Reklamationsgrund)<br/><Werte>`WERTE_ZU_HOCH`, `WERTE_ZU_NIEDRIG`, `WERTE_FEHLEN`, `KONFIGURATION_WIRKT_NICHT`, `KONFIGURATION_WIRKT_TEILWEISE`, `WERTE_WERDEN_NICHT_NACH_VORGABEN_UEBERMITTELT`, `UEBERSICHT_FEHLT`, `UEBERSICHT_UNPLAUSIBEL`, `AUSGEROLLTE_DEFINITION_FEHLT`, `AUSGEROLLTE_DEFINITION_UNPLAUSIBEL`</Werte> | Hier wird für die Reklamation von Werten der Reklamationsgrund angegeben. |
| <a id="reklamationsgrundbemerkung"></a>`reklamationsgrundBemerkung` | [ReklamationsgrundBemerkung](/bo4e/202604/com/ReklamationsgrundBemerkung) | Freitext für eine weitere Beschreibung des Reklamationsgrunds |
| <a id="konfiguration"></a>`konfiguration` | string | konfiguration |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[boTyp](/bo4e/202604/bo/Reklamation#botyp) <span className="hbs-pflicht">\*</span></span> | Typ des BO | [Enum BOTyp](/bo4e/202604/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> |
| <span className="hbs-f hbs-e0">[versionStruktur](/bo4e/202604/bo/Reklamation#versionstruktur) <span className="hbs-pflicht">\*</span></span> | versionStruktur | string |
| <span className="hbs-f hbs-e0">[lokationsId](/bo4e/202604/bo/Reklamation#lokationsid)</span> | Für welche Markt- oder Messlokation gilt diese Reklamation. | string |
| <span className="hbs-f hbs-e0">[lokationsTyp](/bo4e/202604/bo/Reklamation#lokationstyp)</span> | Gibt an, ob es sich um eine Markt- oder Messlokation handelt. | [Enum Lokationstyp](/bo4e/202604/enum/Lokationstyp)<br/><Werte>`MALO`, `MELO`, `NELO`, `TECHNISCHE_RESSOURCE`, `STEUERBARE_RESSOURCE`, `TRANCHE`, `MABIS_ZAEHLPUNKT`</Werte> |
| <span className="hbs-f hbs-e0">[obiskennzahl](/bo4e/202604/bo/Reklamation#obiskennzahl)</span> | OBIS-Kennzahl | string |
| <span className="hbs-g hbs-e0">[zeitraumMesswertanfrage](/bo4e/202604/bo/Reklamation#zeitraummesswertanfrage)</span> | — | [Zeitraum](/bo4e/202604/com/Zeitraum) |
| <span className="hbs-f hbs-e1">[zeiteinheit](/bo4e/202604/com/Zeitraum#zeiteinheit)</span> | Zeiteinheit | [Enum Zeiteinheit](/bo4e/202604/enum/Zeiteinheit)<br/><Werte>`SEKUNDE`, `MINUTE`, `STUNDE`, `VIERTEL_STUNDE`, `TAG`, `WOCHE`, `MONAT`, `QUARTAL`, `HALBJAHR`, `JAHR`</Werte> |
| <span className="hbs-f hbs-e1">[dauer](/bo4e/202604/com/Zeitraum#dauer)</span> | dauer | integer |
| <span className="hbs-f hbs-e1">[startdatum](/bo4e/202604/com/Zeitraum#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e1">[enddatum](/bo4e/202604/com/Zeitraum#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-f hbs-e1">[einheit](/bo4e/202604/com/Zeitraum#einheit)</span> | Zeiteinheit | [Enum Zeiteinheit](/bo4e/202604/enum/Zeiteinheit)<br/><Werte>`SEKUNDE`, `MINUTE`, `STUNDE`, `VIERTEL_STUNDE`, `TAG`, `WOCHE`, `MONAT`, `QUARTAL`, `HALBJAHR`, `JAHR`</Werte> |
| <span className="hbs-f hbs-e1">[ableseZeitraum](/bo4e/202604/com/Zeitraum#ablesezeitraum)</span> | ableseZeitraum | string |
| <span className="hbs-f hbs-e1">[abrechnungsZeitraum](/bo4e/202604/com/Zeitraum#abrechnungszeitraum)</span> | abrechnungsZeitraum | string |
| <span className="hbs-f hbs-e1">[zeitraumText](/bo4e/202604/com/Zeitraum#zeitraumtext)</span> | zeitraumText | string |
| <span className="hbs-f hbs-e1">[zeitraumId](/bo4e/202604/com/Zeitraum#zeitraumid)</span> | zeitraumId | integer |
| <span className="hbs-f hbs-e0">[reklamationsgrund](/bo4e/202604/bo/Reklamation#reklamationsgrund)</span> | Hier wird für die Reklamation von Werten der Reklamationsgrund angegeben. | [Enum Reklamationsgrund](/bo4e/202604/enum/Reklamationsgrund)<br/><Werte>`WERTE_ZU_HOCH`, `WERTE_ZU_NIEDRIG`, `WERTE_FEHLEN`, `KONFIGURATION_WIRKT_NICHT`, `KONFIGURATION_WIRKT_TEILWEISE`, `WERTE_WERDEN_NICHT_NACH_VORGABEN_UEBERMITTELT`, `UEBERSICHT_FEHLT`, `UEBERSICHT_UNPLAUSIBEL`, `AUSGEROLLTE_DEFINITION_FEHLT`, `AUSGEROLLTE_DEFINITION_UNPLAUSIBEL`</Werte> |
| <span className="hbs-g hbs-e0">[reklamationsgrundBemerkung](/bo4e/202604/bo/Reklamation#reklamationsgrundbemerkung)</span> | Freitext für eine weitere Beschreibung des Reklamationsgrunds | [ReklamationsgrundBemerkung](/bo4e/202604/com/ReklamationsgrundBemerkung) |
| <span className="hbs-f hbs-e1">[bemerkung1](/bo4e/202604/com/ReklamationsgrundBemerkung#bemerkung1)</span> | bemerkung1 | string |
| <span className="hbs-f hbs-e1">[bemerkung2](/bo4e/202604/com/ReklamationsgrundBemerkung#bemerkung2)</span> | bemerkung2 | string |
| <span className="hbs-f hbs-e1">[bemerkung3](/bo4e/202604/com/ReklamationsgrundBemerkung#bemerkung3)</span> | bemerkung3 | string |
| <span className="hbs-f hbs-e1">[bemerkung4](/bo4e/202604/com/ReklamationsgrundBemerkung#bemerkung4)</span> | bemerkung4 | string |
| <span className="hbs-f hbs-e1">[bemerkung5](/bo4e/202604/com/ReklamationsgrundBemerkung#bemerkung5)</span> | bemerkung5 | string |
| <span className="hbs-f hbs-e0">[konfiguration](/bo4e/202604/bo/Reklamation#konfiguration)</span> | konfiguration | string |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### lokationsId

1 Verwendung(en) in den Nachrichtentypen ORDERS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_17113](/schnittstellen/202604/pruefi/ORDERS/PI_17113) | Prüfi | ORDERS | stammdaten › REKLAMATION |

### obiskennzahl

1 Verwendung(en) in den Nachrichtentypen ORDERS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_17113](/schnittstellen/202604/pruefi/ORDERS/PI_17113) | Prüfi | ORDERS | stammdaten › REKLAMATION |

### reklamationsgrund

3 Verwendung(en) in den Nachrichtentypen ORDERS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_17113](/schnittstellen/202604/pruefi/ORDERS/PI_17113) | Prüfi | ORDERS | stammdaten › REKLAMATION |
| [PI_17122](/schnittstellen/202604/pruefi/ORDERS/PI_17122) | Prüfi | ORDERS | stammdaten › REKLAMATION |
| [PI_17128](/schnittstellen/202604/pruefi/ORDERS/PI_17128) | Prüfi | ORDERS | stammdaten › REKLAMATION |

### konfiguration

1 Verwendung(en) in den Nachrichtentypen ORDERS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_17113](/schnittstellen/202604/pruefi/ORDERS/PI_17113) | Prüfi | ORDERS | stammdaten › REKLAMATION |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
