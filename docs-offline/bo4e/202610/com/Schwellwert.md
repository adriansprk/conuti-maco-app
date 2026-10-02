# Schwellwert
<span hidden data-pagefind-meta={"title:Schwellwert — BO4E-Komponente (FV 202610)"} />

BO4E-Komponente · 3 Felder · 13 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="obererschwellwert"></a>`obererSchwellwert` | number (float) | obererSchwellwert |
| <a id="untererschwellwert"></a>`untererSchwellwert` | number (float) | untererSchwellwert |
| <a id="konfigurationsprodukt"></a>`konfigurationsprodukt` | string | konfigurationsprodukt |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[obererSchwellwert](/bo4e/202610/com/Schwellwert#obererschwellwert)</span> | obererSchwellwert | number (float) |
| <span className="hbs-f hbs-e0">[untererSchwellwert](/bo4e/202610/com/Schwellwert#untererschwellwert)</span> | untererSchwellwert | number (float) |
| <span className="hbs-f hbs-e0">[konfigurationsprodukt](/bo4e/202610/com/Schwellwert#konfigurationsprodukt)</span> | konfigurationsprodukt | string |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### obererSchwellwert

5 Verwendung(en) in den Nachrichtentypen ORDERS, QUOTES, REQOTE, UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_15004](/schnittstellen/202610/pruefi/QUOTES/PI_15004) | Prüfi | QUOTES | stammdaten › WERTE_NACH_TYP2 › schwellwerte |
| [PI_17128](/schnittstellen/202610/pruefi/ORDERS/PI_17128) | Prüfi | ORDERS | stammdaten › WERTE_NACH_TYP2 › schwellwerte |
| [PI_17130](/schnittstellen/202610/pruefi/ORDERS/PI_17130) | Prüfi | ORDERS | stammdaten › WERTE_NACH_TYP2 › schwellwerte |
| [PI_25009](/schnittstellen/202610/pruefi/UTILTS/PI_25009) | Prüfi | UTILTS | stammdaten › LEISTUNGSKURVENDEFINITION › leistungskurven › schwellwert |
| [PI_35004](/schnittstellen/202610/pruefi/REQOTE/PI_35004) | Prüfi | REQOTE | stammdaten › WERTE_NACH_TYP2 › schwellwerte |

### untererSchwellwert

4 Verwendung(en) in den Nachrichtentypen ORDERS, QUOTES, REQOTE.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_15004](/schnittstellen/202610/pruefi/QUOTES/PI_15004) | Prüfi | QUOTES | stammdaten › WERTE_NACH_TYP2 › schwellwerte |
| [PI_17128](/schnittstellen/202610/pruefi/ORDERS/PI_17128) | Prüfi | ORDERS | stammdaten › WERTE_NACH_TYP2 › schwellwerte |
| [PI_17130](/schnittstellen/202610/pruefi/ORDERS/PI_17130) | Prüfi | ORDERS | stammdaten › WERTE_NACH_TYP2 › schwellwerte |
| [PI_35004](/schnittstellen/202610/pruefi/REQOTE/PI_35004) | Prüfi | REQOTE | stammdaten › WERTE_NACH_TYP2 › schwellwerte |

### konfigurationsprodukt

4 Verwendung(en) in den Nachrichtentypen ORDERS, QUOTES, REQOTE.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_15004](/schnittstellen/202610/pruefi/QUOTES/PI_15004) | Prüfi | QUOTES | stammdaten › WERTE_NACH_TYP2 › schwellwerte |
| [PI_17128](/schnittstellen/202610/pruefi/ORDERS/PI_17128) | Prüfi | ORDERS | stammdaten › WERTE_NACH_TYP2 › schwellwerte |
| [PI_17130](/schnittstellen/202610/pruefi/ORDERS/PI_17130) | Prüfi | ORDERS | stammdaten › WERTE_NACH_TYP2 › schwellwerte |
| [PI_35004](/schnittstellen/202610/pruefi/REQOTE/PI_35004) | Prüfi | REQOTE | stammdaten › WERTE_NACH_TYP2 › schwellwerte |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
