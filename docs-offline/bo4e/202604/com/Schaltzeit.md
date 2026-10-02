# Schaltzeit
<span hidden data-pagefind-meta={"title:Schaltzeit — BO4E-Komponente (FV 202604)"} />

BO4E-Komponente · 6 Felder · 13 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="code"></a>`code` | string | code |
| <a id="aenderungszeitpunkt"></a>`aenderungszeitpunkt` | string (date-time) | aenderungszeitpunkt |
| <a id="haeufigkeit"></a>`haeufigkeit` | [Enum HaeufigkeitSchaltzeit](/bo4e/202604/enum/HaeufigkeitSchaltzeit)<br/><Werte>`EINMALIG`, `JAEHRLICH`</Werte> | HaeufigkeitSchaltzeit |
| <a id="uebermittelbarkeit"></a>`uebermittelbarkeit` | [Enum UebermittelbarkeitSchaltzeit](/bo4e/202604/enum/UebermittelbarkeitSchaltzeit)<br/><Werte>`ELEKTRONISCH`, `NICHT_ELEKTRONISCH`</Werte> | UebermittelbarkeitSchaltzeit |
| <a id="schalthandlung"></a>`schalthandlung` | [Enum Schalthandlung](/bo4e/202604/enum/Schalthandlung)<br/><Werte>`LEISTUNG_AN`, `LEISTUNG_AUS`</Werte> | Schalthandlung |
| <a id="konfigurationsprodukt"></a>`konfigurationsprodukt` | string | konfigurationsprodukt |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[code](/bo4e/202604/com/Schaltzeit#code)</span> | code | string |
| <span className="hbs-f hbs-e0">[aenderungszeitpunkt](/bo4e/202604/com/Schaltzeit#aenderungszeitpunkt)</span> | aenderungszeitpunkt | string (date-time) |
| <span className="hbs-f hbs-e0">[haeufigkeit](/bo4e/202604/com/Schaltzeit#haeufigkeit)</span> | HaeufigkeitSchaltzeit | [Enum HaeufigkeitSchaltzeit](/bo4e/202604/enum/HaeufigkeitSchaltzeit)<br/><Werte>`EINMALIG`, `JAEHRLICH`</Werte> |
| <span className="hbs-f hbs-e0">[uebermittelbarkeit](/bo4e/202604/com/Schaltzeit#uebermittelbarkeit)</span> | UebermittelbarkeitSchaltzeit | [Enum UebermittelbarkeitSchaltzeit](/bo4e/202604/enum/UebermittelbarkeitSchaltzeit)<br/><Werte>`ELEKTRONISCH`, `NICHT_ELEKTRONISCH`</Werte> |
| <span className="hbs-f hbs-e0">[schalthandlung](/bo4e/202604/com/Schaltzeit#schalthandlung)</span> | Schalthandlung | [Enum Schalthandlung](/bo4e/202604/enum/Schalthandlung)<br/><Werte>`LEISTUNG_AN`, `LEISTUNG_AUS`</Werte> |
| <span className="hbs-f hbs-e0">[konfigurationsprodukt](/bo4e/202604/com/Schaltzeit#konfigurationsprodukt)</span> | konfigurationsprodukt | string |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### code

5 Verwendung(en) in den Nachrichtentypen ORDERS, QUOTES, REQOTE, UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_15004](/schnittstellen/202604/pruefi/QUOTES/PI_15004) | Prüfi | QUOTES | stammdaten › SCHALTZEITDEFINITION › schaltzeiten |
| [PI_17122](/schnittstellen/202604/pruefi/ORDERS/PI_17122) | Prüfi | ORDERS | stammdaten › SCHALTZEITDEFINITION › schaltzeiten |
| [PI_17128](/schnittstellen/202604/pruefi/ORDERS/PI_17128) | Prüfi | ORDERS | stammdaten › SCHALTZEITDEFINITION › schaltzeiten |
| [PI_25006](/schnittstellen/202604/pruefi/UTILTS/PI_25006) | Prüfi | UTILTS | stammdaten › SCHALTZEITDEFINITION › schaltzeiten |
| [PI_35004](/schnittstellen/202604/pruefi/REQOTE/PI_35004) | Prüfi | REQOTE | stammdaten › SCHALTZEITDEFINITION › schaltzeiten |

### aenderungszeitpunkt

1 Verwendung(en) in den Nachrichtentypen UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_25008](/schnittstellen/202604/pruefi/UTILTS/PI_25008) | Prüfi | UTILTS | stammdaten › SCHALTZEITDEFINITION › schaltzeiten |

### haeufigkeit

2 Verwendung(en) in den Nachrichtentypen UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_25006](/schnittstellen/202604/pruefi/UTILTS/PI_25006) | Prüfi | UTILTS | stammdaten › SCHALTZEITDEFINITION › schaltzeiten |
| [PI_25008](/schnittstellen/202604/pruefi/UTILTS/PI_25008) | Prüfi | UTILTS | stammdaten › SCHALTZEITDEFINITION › schaltzeiten |

### uebermittelbarkeit

1 Verwendung(en) in den Nachrichtentypen UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_25006](/schnittstellen/202604/pruefi/UTILTS/PI_25006) | Prüfi | UTILTS | stammdaten › SCHALTZEITDEFINITION › schaltzeiten |

### schalthandlung

1 Verwendung(en) in den Nachrichtentypen UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_25008](/schnittstellen/202604/pruefi/UTILTS/PI_25008) | Prüfi | UTILTS | stammdaten › SCHALTZEITDEFINITION › schaltzeiten |

### konfigurationsprodukt

3 Verwendung(en) in den Nachrichtentypen ORDERS, QUOTES, REQOTE.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_15004](/schnittstellen/202604/pruefi/QUOTES/PI_15004) | Prüfi | QUOTES | stammdaten › SCHALTZEITDEFINITION › schaltzeiten |
| [PI_17128](/schnittstellen/202604/pruefi/ORDERS/PI_17128) | Prüfi | ORDERS | stammdaten › SCHALTZEITDEFINITION › schaltzeiten |
| [PI_35004](/schnittstellen/202604/pruefi/REQOTE/PI_35004) | Prüfi | REQOTE | stammdaten › SCHALTZEITDEFINITION › schaltzeiten |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
