# EndpunktAdresse
<span hidden data-pagefind-meta={"title:EndpunktAdresse — BO4E-Komponente (FV 202610)"} />

BO4E-Komponente · 3 Felder · 3 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="gwamanagement"></a>`gwaManagement` | string | Endpunktadresse GWA Management |
| <a id="gwaadminservice"></a>`gwaAdminService` | string | Endpunktadresse GWA Admin-Service |
| <a id="gwantp"></a>`gwaNTP` | string | Endpunktadresse GWA NTP (Zeitserver) |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[gwaManagement](/bo4e/202610/com/EndpunktAdresse#gwamanagement)</span> | Endpunktadresse GWA Management | string |
| <span className="hbs-f hbs-e0">[gwaAdminService](/bo4e/202610/com/EndpunktAdresse#gwaadminservice)</span> | Endpunktadresse GWA Admin-Service | string |
| <span className="hbs-f hbs-e0">[gwaNTP](/bo4e/202610/com/EndpunktAdresse#gwantp)</span> | Endpunktadresse GWA NTP (Zeitserver) | string |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### gwaManagement

1 Verwendung(en) in den Nachrichtentypen ORDERS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_17001](/schnittstellen/202610/pruefi/ORDERS/PI_17001) | Prüfi | ORDERS | stammdaten › AUFTRAG › positionsdaten › endpunktAdresse |

### gwaAdminService

1 Verwendung(en) in den Nachrichtentypen ORDERS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_17001](/schnittstellen/202610/pruefi/ORDERS/PI_17001) | Prüfi | ORDERS | stammdaten › AUFTRAG › positionsdaten › endpunktAdresse |

### gwaNTP

1 Verwendung(en) in den Nachrichtentypen ORDERS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_17001](/schnittstellen/202610/pruefi/ORDERS/PI_17001) | Prüfi | ORDERS | stammdaten › AUFTRAG › positionsdaten › endpunktAdresse |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
