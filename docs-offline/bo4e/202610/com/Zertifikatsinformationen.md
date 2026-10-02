# Zertifikatsinformationen
<span hidden data-pagefind-meta={"title:Zertifikatsinformationen — BO4E-Komponente (FV 202610)"} />

BO4E-Komponente · 3 Felder · 3 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="urisubca"></a>`uriSubCA` | string | URI der Sub-CA |
| <a id="commonnamezertifikat"></a>`commonNameZertifikat` | string | Common Name (CN) des Zertifikats |
| <a id="seriennummerzertifikat"></a>`seriennummerZertifikat` | string | Seriennummer des Zertifikats |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[uriSubCA](/bo4e/202610/com/Zertifikatsinformationen#urisubca)</span> | URI der Sub-CA | string |
| <span className="hbs-f hbs-e0">[commonNameZertifikat](/bo4e/202610/com/Zertifikatsinformationen#commonnamezertifikat)</span> | Common Name (CN) des Zertifikats | string |
| <span className="hbs-f hbs-e0">[seriennummerZertifikat](/bo4e/202610/com/Zertifikatsinformationen#seriennummerzertifikat)</span> | Seriennummer des Zertifikats | string |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### uriSubCA

1 Verwendung(en) in den Nachrichtentypen ORDERS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_17001](/schnittstellen/202610/pruefi/ORDERS/PI_17001) | Prüfi | ORDERS | stammdaten › AUFTRAG › positionsdaten › zertifikatsInformationen |

### commonNameZertifikat

1 Verwendung(en) in den Nachrichtentypen ORDERS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_17001](/schnittstellen/202610/pruefi/ORDERS/PI_17001) | Prüfi | ORDERS | stammdaten › AUFTRAG › positionsdaten › zertifikatsInformationen |

### seriennummerZertifikat

1 Verwendung(en) in den Nachrichtentypen ORDERS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_17001](/schnittstellen/202610/pruefi/ORDERS/PI_17001) | Prüfi | ORDERS | stammdaten › AUFTRAG › positionsdaten › zertifikatsInformationen |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
