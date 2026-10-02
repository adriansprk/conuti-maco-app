# Steuerbetrag
<span hidden data-pagefind-meta={"title:Steuerbetrag — BO4E-Komponente (FV 202610)"} />

BO4E-Komponente · 6 Felder · 49 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="steuerkennzeichen"></a>`steuerkennzeichen` | string | Kennzeichnung des Steuersatzes, bzw. Verfahrens. Details Steuerkennzeichen |
| <a id="basiswert"></a>`basiswert` | number (float) | Nettobetrag für den die Steuer berechnet wurde. Z.B. 200 |
| <a id="steuerwert"></a>`steuerwert` | number (float) | Aus dem Basiswert berechnete Steuer. Z.B. 38 (bei UST_19), falls Basiswert 200 ist. |
| <a id="waehrung"></a>`waehrung` | string | Währung. Z.B. Euro. |
| <a id="basiswertvorausbezahlt"></a>`basiswertVorausbezahlt` | number (float) | basiswertVorausbezahlt |
| <a id="steuerwertvorausbezahlt"></a>`steuerwertVorausbezahlt` | number (float) | steuerwertVorausbezahlt |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[steuerkennzeichen](/bo4e/202610/com/Steuerbetrag#steuerkennzeichen)</span> | Kennzeichnung des Steuersatzes, bzw. Verfahrens. Details Steuerkennzeichen | string |
| <span className="hbs-f hbs-e0">[basiswert](/bo4e/202610/com/Steuerbetrag#basiswert)</span> | Nettobetrag für den die Steuer berechnet wurde. Z.B. 200 | number (float) |
| <span className="hbs-f hbs-e0">[steuerwert](/bo4e/202610/com/Steuerbetrag#steuerwert)</span> | Aus dem Basiswert berechnete Steuer. Z.B. 38 (bei UST_19), falls Basiswert 200 ist. | number (float) |
| <span className="hbs-f hbs-e0">[waehrung](/bo4e/202610/com/Steuerbetrag#waehrung)</span> | Währung. Z.B. Euro. | string |
| <span className="hbs-f hbs-e0">[basiswertVorausbezahlt](/bo4e/202610/com/Steuerbetrag#basiswertvorausbezahlt)</span> | basiswertVorausbezahlt | number (float) |
| <span className="hbs-f hbs-e0">[steuerwertVorausbezahlt](/bo4e/202610/com/Steuerbetrag#steuerwertvorausbezahlt)</span> | steuerwertVorausbezahlt | number (float) |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### steuerkennzeichen

21 Verwendung(en) in den Nachrichtentypen INVOIC.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_31001](/schnittstellen/202610/pruefi/INVOIC/PI_31001) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen › teilsummeSteuer |
| [PI_31001](/schnittstellen/202610/pruefi/INVOIC/PI_31001) | Prüfi | INVOIC | stammdaten › RECHNUNG › steuerbetraege |
| [PI_31002](/schnittstellen/202610/pruefi/INVOIC/PI_31002) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen › teilsummeSteuer |
| [PI_31002](/schnittstellen/202610/pruefi/INVOIC/PI_31002) | Prüfi | INVOIC | stammdaten › RECHNUNG › steuerbetraege |
| [PI_31003](/schnittstellen/202610/pruefi/INVOIC/PI_31003) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen › teilsummeSteuer |
| [PI_31003](/schnittstellen/202610/pruefi/INVOIC/PI_31003) | Prüfi | INVOIC | stammdaten › RECHNUNG › steuerbetraege |
| [PI_31004](/schnittstellen/202610/pruefi/INVOIC/PI_31004) | Prüfi | INVOIC | stammdaten › RECHNUNG › steuerbetraege |
| [PI_31005](/schnittstellen/202610/pruefi/INVOIC/PI_31005) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen › teilsummeSteuer |
| [PI_31005](/schnittstellen/202610/pruefi/INVOIC/PI_31005) | Prüfi | INVOIC | stammdaten › RECHNUNG › steuerbetraege |
| [PI_31006](/schnittstellen/202610/pruefi/INVOIC/PI_31006) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen › teilsummeSteuer |
| [PI_31006](/schnittstellen/202610/pruefi/INVOIC/PI_31006) | Prüfi | INVOIC | stammdaten › RECHNUNG › steuerbetraege |
| [PI_31007](/schnittstellen/202610/pruefi/INVOIC/PI_31007) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen › teilsummeSteuer |
| [PI_31007](/schnittstellen/202610/pruefi/INVOIC/PI_31007) | Prüfi | INVOIC | stammdaten › RECHNUNG › steuerbetraege |
| [PI_31008](/schnittstellen/202610/pruefi/INVOIC/PI_31008) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen › teilsummeSteuer |
| [PI_31008](/schnittstellen/202610/pruefi/INVOIC/PI_31008) | Prüfi | INVOIC | stammdaten › RECHNUNG › steuerbetraege |
| [PI_31009](/schnittstellen/202610/pruefi/INVOIC/PI_31009) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen › teilsummeSteuer |
| [PI_31009](/schnittstellen/202610/pruefi/INVOIC/PI_31009) | Prüfi | INVOIC | stammdaten › RECHNUNG › steuerbetraege |
| [PI_31010](/schnittstellen/202610/pruefi/INVOIC/PI_31010) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen › teilsummeSteuer |
| [PI_31010](/schnittstellen/202610/pruefi/INVOIC/PI_31010) | Prüfi | INVOIC | stammdaten › RECHNUNG › steuerbetraege |
| [PI_31011](/schnittstellen/202610/pruefi/INVOIC/PI_31011) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen › teilsummeSteuer |
| [PI_31011](/schnittstellen/202610/pruefi/INVOIC/PI_31011) | Prüfi | INVOIC | stammdaten › RECHNUNG › steuerbetraege |

### basiswert

11 Verwendung(en) in den Nachrichtentypen INVOIC.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_31001](/schnittstellen/202610/pruefi/INVOIC/PI_31001) | Prüfi | INVOIC | stammdaten › RECHNUNG › steuerbetraege |
| [PI_31002](/schnittstellen/202610/pruefi/INVOIC/PI_31002) | Prüfi | INVOIC | stammdaten › RECHNUNG › steuerbetraege |
| [PI_31003](/schnittstellen/202610/pruefi/INVOIC/PI_31003) | Prüfi | INVOIC | stammdaten › RECHNUNG › steuerbetraege |
| [PI_31004](/schnittstellen/202610/pruefi/INVOIC/PI_31004) | Prüfi | INVOIC | stammdaten › RECHNUNG › steuerbetraege |
| [PI_31005](/schnittstellen/202610/pruefi/INVOIC/PI_31005) | Prüfi | INVOIC | stammdaten › RECHNUNG › steuerbetraege |
| [PI_31006](/schnittstellen/202610/pruefi/INVOIC/PI_31006) | Prüfi | INVOIC | stammdaten › RECHNUNG › steuerbetraege |
| [PI_31007](/schnittstellen/202610/pruefi/INVOIC/PI_31007) | Prüfi | INVOIC | stammdaten › RECHNUNG › steuerbetraege |
| [PI_31008](/schnittstellen/202610/pruefi/INVOIC/PI_31008) | Prüfi | INVOIC | stammdaten › RECHNUNG › steuerbetraege |
| [PI_31009](/schnittstellen/202610/pruefi/INVOIC/PI_31009) | Prüfi | INVOIC | stammdaten › RECHNUNG › steuerbetraege |
| [PI_31010](/schnittstellen/202610/pruefi/INVOIC/PI_31010) | Prüfi | INVOIC | stammdaten › RECHNUNG › steuerbetraege |
| [PI_31011](/schnittstellen/202610/pruefi/INVOIC/PI_31011) | Prüfi | INVOIC | stammdaten › RECHNUNG › steuerbetraege |

### steuerwert

11 Verwendung(en) in den Nachrichtentypen INVOIC.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_31001](/schnittstellen/202610/pruefi/INVOIC/PI_31001) | Prüfi | INVOIC | stammdaten › RECHNUNG › steuerbetraege |
| [PI_31002](/schnittstellen/202610/pruefi/INVOIC/PI_31002) | Prüfi | INVOIC | stammdaten › RECHNUNG › steuerbetraege |
| [PI_31003](/schnittstellen/202610/pruefi/INVOIC/PI_31003) | Prüfi | INVOIC | stammdaten › RECHNUNG › steuerbetraege |
| [PI_31004](/schnittstellen/202610/pruefi/INVOIC/PI_31004) | Prüfi | INVOIC | stammdaten › RECHNUNG › steuerbetraege |
| [PI_31005](/schnittstellen/202610/pruefi/INVOIC/PI_31005) | Prüfi | INVOIC | stammdaten › RECHNUNG › steuerbetraege |
| [PI_31006](/schnittstellen/202610/pruefi/INVOIC/PI_31006) | Prüfi | INVOIC | stammdaten › RECHNUNG › steuerbetraege |
| [PI_31007](/schnittstellen/202610/pruefi/INVOIC/PI_31007) | Prüfi | INVOIC | stammdaten › RECHNUNG › steuerbetraege |
| [PI_31008](/schnittstellen/202610/pruefi/INVOIC/PI_31008) | Prüfi | INVOIC | stammdaten › RECHNUNG › steuerbetraege |
| [PI_31009](/schnittstellen/202610/pruefi/INVOIC/PI_31009) | Prüfi | INVOIC | stammdaten › RECHNUNG › steuerbetraege |
| [PI_31010](/schnittstellen/202610/pruefi/INVOIC/PI_31010) | Prüfi | INVOIC | stammdaten › RECHNUNG › steuerbetraege |
| [PI_31011](/schnittstellen/202610/pruefi/INVOIC/PI_31011) | Prüfi | INVOIC | stammdaten › RECHNUNG › steuerbetraege |

### basiswertVorausbezahlt

3 Verwendung(en) in den Nachrichtentypen INVOIC.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_31002](/schnittstellen/202610/pruefi/INVOIC/PI_31002) | Prüfi | INVOIC | stammdaten › RECHNUNG › steuerbetraege |
| [PI_31004](/schnittstellen/202610/pruefi/INVOIC/PI_31004) | Prüfi | INVOIC | stammdaten › RECHNUNG › steuerbetraege |
| [PI_31010](/schnittstellen/202610/pruefi/INVOIC/PI_31010) | Prüfi | INVOIC | stammdaten › RECHNUNG › steuerbetraege |

### steuerwertVorausbezahlt

3 Verwendung(en) in den Nachrichtentypen INVOIC.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_31002](/schnittstellen/202610/pruefi/INVOIC/PI_31002) | Prüfi | INVOIC | stammdaten › RECHNUNG › steuerbetraege |
| [PI_31004](/schnittstellen/202610/pruefi/INVOIC/PI_31004) | Prüfi | INVOIC | stammdaten › RECHNUNG › steuerbetraege |
| [PI_31010](/schnittstellen/202610/pruefi/INVOIC/PI_31010) | Prüfi | INVOIC | stammdaten › RECHNUNG › steuerbetraege |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
