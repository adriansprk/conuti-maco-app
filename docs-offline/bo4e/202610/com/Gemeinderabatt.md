# Gemeinderabatt
<span hidden data-pagefind-meta={"title:Gemeinderabatt — BO4E-Komponente (FV 202610)"} />

BO4E-Komponente · 4 Felder · 4 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="wert"></a>`wert` | number (float) | Wert |
| <a id="einheit"></a>`einheit` | string | Einheit |
| <a id="typ"></a>`typ` | string | Typ |
| <a id="bemessungsgrundlage"></a>`bemessungsgrundlage` | number (float) | Bemessungsgrundlage |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[wert](/bo4e/202610/com/Gemeinderabatt#wert)</span> | Wert | number (float) |
| <span className="hbs-f hbs-e0">[einheit](/bo4e/202610/com/Gemeinderabatt#einheit)</span> | Einheit | string |
| <span className="hbs-f hbs-e0">[typ](/bo4e/202610/com/Gemeinderabatt#typ)</span> | Typ | string |
| <span className="hbs-f hbs-e0">[bemessungsgrundlage](/bo4e/202610/com/Gemeinderabatt#bemessungsgrundlage)</span> | Bemessungsgrundlage | number (float) |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### wert

3 Verwendung(en) in den Nachrichtentypen INVOIC.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_31002](/schnittstellen/202610/pruefi/INVOIC/PI_31002) | Prüfi | INVOIC | stammdaten › RECHNUNG › gemeinderabatt |
| [PI_31002](/schnittstellen/202610/pruefi/INVOIC/PI_31002) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen › gemeinderabatt |
| [PI_31004](/schnittstellen/202610/pruefi/INVOIC/PI_31004) | Prüfi | INVOIC | stammdaten › RECHNUNG › gemeinderabatt |

### bemessungsgrundlage

1 Verwendung(en) in den Nachrichtentypen INVOIC.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_31002](/schnittstellen/202610/pruefi/INVOIC/PI_31002) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen › gemeinderabatt |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
