# Leistungskurve
<span hidden data-pagefind-meta={"title:Leistungskurve — BO4E-Komponente (FV 202610)"} />

BO4E-Komponente · 6 Felder · 12 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="code"></a>`code` | string | Code der Leistungskurve |
| <a id="aenderungszeitpunkt"></a>`aenderungszeitpunkt` | string (date-time) | Änderungszeitpunkt |
| <a id="haeufigkeit"></a>`haeufigkeit` | [Enum HaeufigkeitLeistungskurve](/bo4e/202610/enum/HaeufigkeitLeistungskurve)<br/><Werte>`EINMALIG`, `JAEHRLICH`</Werte> | HaeufigkeitLeistungskurve |
| <a id="uebermittelbarkeit"></a>`uebermittelbarkeit` | [Enum UebermittelbarkeitLeistungskurve](/bo4e/202610/enum/UebermittelbarkeitLeistungskurve)<br/><Werte>`ELEKTRONISCH`, `NICHT_ELEKTRONISCH`</Werte> | UebermittelbarkeitLeistungskurve |
| <a id="schwellwert"></a>`schwellwert` | [Schwellwert](/bo4e/202610/com/Schwellwert) | — |
| <a id="konfigurationsprodukt"></a>`konfigurationsprodukt` | string | Konfigurationsprodukt |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[code](/bo4e/202610/com/Leistungskurve#code)</span> | Code der Leistungskurve | string |
| <span className="hbs-f hbs-e0">[aenderungszeitpunkt](/bo4e/202610/com/Leistungskurve#aenderungszeitpunkt)</span> | Änderungszeitpunkt | string (date-time) |
| <span className="hbs-f hbs-e0">[haeufigkeit](/bo4e/202610/com/Leistungskurve#haeufigkeit)</span> | HaeufigkeitLeistungskurve | [Enum HaeufigkeitLeistungskurve](/bo4e/202610/enum/HaeufigkeitLeistungskurve)<br/><Werte>`EINMALIG`, `JAEHRLICH`</Werte> |
| <span className="hbs-f hbs-e0">[uebermittelbarkeit](/bo4e/202610/com/Leistungskurve#uebermittelbarkeit)</span> | UebermittelbarkeitLeistungskurve | [Enum UebermittelbarkeitLeistungskurve](/bo4e/202610/enum/UebermittelbarkeitLeistungskurve)<br/><Werte>`ELEKTRONISCH`, `NICHT_ELEKTRONISCH`</Werte> |
| <span className="hbs-g hbs-e0">[schwellwert](/bo4e/202610/com/Leistungskurve#schwellwert)</span> | — | [Schwellwert](/bo4e/202610/com/Schwellwert) |
| <span className="hbs-f hbs-e1">[obererSchwellwert](/bo4e/202610/com/Schwellwert#obererschwellwert)</span> | obererSchwellwert | number (float) |
| <span className="hbs-f hbs-e1">[untererSchwellwert](/bo4e/202610/com/Schwellwert#untererschwellwert)</span> | untererSchwellwert | number (float) |
| <span className="hbs-f hbs-e1">[konfigurationsprodukt](/bo4e/202610/com/Schwellwert#konfigurationsprodukt)</span> | konfigurationsprodukt | string |
| <span className="hbs-f hbs-e0">[konfigurationsprodukt](/bo4e/202610/com/Leistungskurve#konfigurationsprodukt)</span> | Konfigurationsprodukt | string |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### code

5 Verwendung(en) in den Nachrichtentypen ORDERS, QUOTES, REQOTE, UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_15004](/schnittstellen/202610/pruefi/QUOTES/PI_15004) | Prüfi | QUOTES | stammdaten › LEISTUNGSKURVENDEFINITION › leistungskurven |
| [PI_17122](/schnittstellen/202610/pruefi/ORDERS/PI_17122) | Prüfi | ORDERS | stammdaten › LEISTUNGSKURVENDEFINITION › leistungskurven |
| [PI_17128](/schnittstellen/202610/pruefi/ORDERS/PI_17128) | Prüfi | ORDERS | stammdaten › LEISTUNGSKURVENDEFINITION › leistungskurven |
| [PI_25007](/schnittstellen/202610/pruefi/UTILTS/PI_25007) | Prüfi | UTILTS | stammdaten › LEISTUNGSKURVENDEFINITION › leistungskurven |
| [PI_35004](/schnittstellen/202610/pruefi/REQOTE/PI_35004) | Prüfi | REQOTE | stammdaten › LEISTUNGSKURVENDEFINITION › leistungskurven |

### aenderungszeitpunkt

1 Verwendung(en) in den Nachrichtentypen UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_25009](/schnittstellen/202610/pruefi/UTILTS/PI_25009) | Prüfi | UTILTS | stammdaten › LEISTUNGSKURVENDEFINITION › leistungskurven |

### haeufigkeit

2 Verwendung(en) in den Nachrichtentypen UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_25007](/schnittstellen/202610/pruefi/UTILTS/PI_25007) | Prüfi | UTILTS | stammdaten › LEISTUNGSKURVENDEFINITION › leistungskurven |
| [PI_25009](/schnittstellen/202610/pruefi/UTILTS/PI_25009) | Prüfi | UTILTS | stammdaten › LEISTUNGSKURVENDEFINITION › leistungskurven |

### uebermittelbarkeit

1 Verwendung(en) in den Nachrichtentypen UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_25007](/schnittstellen/202610/pruefi/UTILTS/PI_25007) | Prüfi | UTILTS | stammdaten › LEISTUNGSKURVENDEFINITION › leistungskurven |

### konfigurationsprodukt

3 Verwendung(en) in den Nachrichtentypen ORDERS, QUOTES, REQOTE.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_15004](/schnittstellen/202610/pruefi/QUOTES/PI_15004) | Prüfi | QUOTES | stammdaten › LEISTUNGSKURVENDEFINITION › leistungskurven |
| [PI_17128](/schnittstellen/202610/pruefi/ORDERS/PI_17128) | Prüfi | ORDERS | stammdaten › LEISTUNGSKURVENDEFINITION › leistungskurven |
| [PI_35004](/schnittstellen/202610/pruefi/REQOTE/PI_35004) | Prüfi | REQOTE | stammdaten › LEISTUNGSKURVENDEFINITION › leistungskurven |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
