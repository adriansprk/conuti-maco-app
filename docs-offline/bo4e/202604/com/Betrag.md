# Betrag
<span hidden data-pagefind-meta={"title:Betrag — BO4E-Komponente (FV 202604)"} />

BO4E-Komponente · 2 Felder · 21 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="wert"></a>`wert` | number (float) | Gibt den Betrag des Preises an. |
| <a id="waehrung"></a>`waehrung` | string | Währung des Preises |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[wert](/bo4e/202604/com/Betrag#wert)</span> | Gibt den Betrag des Preises an. | number (float) |
| <span className="hbs-f hbs-e0">[waehrung](/bo4e/202604/com/Betrag#waehrung)</span> | Währung des Preises | string |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### wert

17 Verwendung(en) in den Nachrichtentypen COMDIS, INVOIC, REMADV.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_29001](/schnittstellen/202604/pruefi/COMDIS/PI_29001) | Prüfi | COMDIS | stammdaten › HANDELSUNSTIMMIGKEIT › zuZahlen |
| [PI_31002](/schnittstellen/202604/pruefi/INVOIC/PI_31002) | Prüfi | INVOIC | stammdaten › RECHNUNG › gesamtbrutto |
| [PI_31002](/schnittstellen/202604/pruefi/INVOIC/PI_31002) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen › teilsummeNetto |
| [PI_31002](/schnittstellen/202604/pruefi/INVOIC/PI_31002) | Prüfi | INVOIC | stammdaten › RECHNUNG › vorausgezahlt |
| [PI_31002](/schnittstellen/202604/pruefi/INVOIC/PI_31002) | Prüfi | INVOIC | stammdaten › RECHNUNG › zuZahlen |
| [PI_33001](/schnittstellen/202604/pruefi/REMADV/PI_33001) | Prüfi | REMADV | stammdaten › AVIS › positionen › gesamtBrutto |
| [PI_33001](/schnittstellen/202604/pruefi/REMADV/PI_33001) | Prüfi | REMADV | stammdaten › AVIS › positionen › zuZahlen |
| [PI_33001](/schnittstellen/202604/pruefi/REMADV/PI_33001) | Prüfi | REMADV | stammdaten › AVIS › zuZahlen |
| [PI_33002](/schnittstellen/202604/pruefi/REMADV/PI_33002) | Prüfi | REMADV | stammdaten › AVIS › positionen › gesamtBrutto |
| [PI_33002](/schnittstellen/202604/pruefi/REMADV/PI_33002) | Prüfi | REMADV | stammdaten › AVIS › positionen › zuZahlen |
| [PI_33002](/schnittstellen/202604/pruefi/REMADV/PI_33002) | Prüfi | REMADV | stammdaten › AVIS › zuZahlen |
| [PI_33003](/schnittstellen/202604/pruefi/REMADV/PI_33003) | Prüfi | REMADV | stammdaten › AVIS › positionen › gesamtBrutto |
| [PI_33003](/schnittstellen/202604/pruefi/REMADV/PI_33003) | Prüfi | REMADV | stammdaten › AVIS › positionen › zuZahlen |
| [PI_33003](/schnittstellen/202604/pruefi/REMADV/PI_33003) | Prüfi | REMADV | stammdaten › AVIS › zuZahlen |
| [PI_33004](/schnittstellen/202604/pruefi/REMADV/PI_33004) | Prüfi | REMADV | stammdaten › AVIS › positionen › gesamtBrutto |
| [PI_33004](/schnittstellen/202604/pruefi/REMADV/PI_33004) | Prüfi | REMADV | stammdaten › AVIS › positionen › zuZahlen |
| [PI_33004](/schnittstellen/202604/pruefi/REMADV/PI_33004) | Prüfi | REMADV | stammdaten › AVIS › zuZahlen |

### waehrung

4 Verwendung(en) in den Nachrichtentypen REMADV.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_33001](/schnittstellen/202604/pruefi/REMADV/PI_33001) | Prüfi | REMADV | stammdaten › AVIS › zuZahlen |
| [PI_33002](/schnittstellen/202604/pruefi/REMADV/PI_33002) | Prüfi | REMADV | stammdaten › AVIS › zuZahlen |
| [PI_33003](/schnittstellen/202604/pruefi/REMADV/PI_33003) | Prüfi | REMADV | stammdaten › AVIS › zuZahlen |
| [PI_33004](/schnittstellen/202604/pruefi/REMADV/PI_33004) | Prüfi | REMADV | stammdaten › AVIS › zuZahlen |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
