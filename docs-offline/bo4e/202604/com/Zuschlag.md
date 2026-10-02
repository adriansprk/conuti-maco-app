# Zuschlag
<span hidden data-pagefind-meta={"title:Zuschlag — BO4E-Komponente (FV 202604)"} />

BO4E-Komponente · 2 Felder · 2 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="typ"></a>`typ` | [Enum ZuschlagTyp](/bo4e/202604/enum/ZuschlagTyp)<br/><Werte>`UMSPANNUNGSZUSCHLAG`, `BETRIEBSMITTEL_P19_STROM_NEV`, `ANPASSUNG_P19_STROM_NEV`, `ANPASSUNG_PAUSCHALE_NETZENTGELTREDUZIERUNG_NACH_P14A_ENWG_AUF_HOEHE_DER_NNE`</Werte> | ZuschlagTyp |
| <a id="prozent"></a>`prozent` | number (float) | prozent |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[typ](/bo4e/202604/com/Zuschlag#typ)</span> | ZuschlagTyp | [Enum ZuschlagTyp](/bo4e/202604/enum/ZuschlagTyp)<br/><Werte>`UMSPANNUNGSZUSCHLAG`, `BETRIEBSMITTEL_P19_STROM_NEV`, `ANPASSUNG_P19_STROM_NEV`, `ANPASSUNG_PAUSCHALE_NETZENTGELTREDUZIERUNG_NACH_P14A_ENWG_AUF_HOEHE_DER_NNE`</Werte> |
| <span className="hbs-f hbs-e0">[prozent](/bo4e/202604/com/Zuschlag#prozent)</span> | prozent | number (float) |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### typ

1 Verwendung(en) in den Nachrichtentypen INVOIC.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_31002](/schnittstellen/202604/pruefi/INVOIC/PI_31002) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen › zuschlag |

### prozent

1 Verwendung(en) in den Nachrichtentypen INVOIC.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_31002](/schnittstellen/202604/pruefi/INVOIC/PI_31002) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen › zuschlag |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
