# Preis
<span hidden data-pagefind-meta={"title:Preis — BO4E-Komponente (FV 202604)"} />

BO4E-Komponente · 8 Felder · 14 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="wert"></a>`wert` | number (float) | wert |
| <a id="menge"></a>`menge` | integer | menge |
| <a id="minimalemenge"></a>`minimaleMenge` | integer | minimale Menge |
| <a id="maximalemenge"></a>`maximaleMenge` | integer | maximale Menge |
| <a id="einheit"></a>`einheit` | [Enum Waehrungseinheit](/bo4e/202604/enum/Waehrungseinheit)<br/><Werte>`EUR`, `CT`</Werte> | Waehrungseinheit |
| <a id="bezugswert"></a>`bezugswert` | [Enum Mengeneinheit](/bo4e/202604/enum/Mengeneinheit)<br/><Werte>`W`, `WH`, `KW`, `KWH`, `KVARH`, `MW`, `MWH`, `STUECK`, `KUBIKMETER`, `STUNDE`, `TAG`, `MONAT`, `JAHR`, `PROZENT`, `ANZAHL`, `VAR`, `KVAR`, `VARH`, `KWHK`, `Z16`, `KWT`, `WATT_PRO_QUADRATMETER`, `METER_PRO_SEKUNDE`</Werte> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können |
| <a id="status"></a>`status` | [Enum Preisstatus](/bo4e/202604/enum/Preisstatus)<br/><Werte>`VORLAEUFIG`, `ENDGUELTIG`</Werte> | Preisstatus |
| <a id="preisart"></a>`preisart` | [Enum Preisart](/bo4e/202604/enum/Preisart)<br/><Werte>`EINRICHTUNGSPREIS`, `TRANSAKTIONSPREIS`, `BETRIEBSPREIS`</Werte> | Preisart Code |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[wert](/bo4e/202604/com/Preis#wert)</span> | wert | number (float) |
| <span className="hbs-f hbs-e0">[menge](/bo4e/202604/com/Preis#menge)</span> | menge | integer |
| <span className="hbs-f hbs-e0">[minimaleMenge](/bo4e/202604/com/Preis#minimalemenge)</span> | minimale Menge | integer |
| <span className="hbs-f hbs-e0">[maximaleMenge](/bo4e/202604/com/Preis#maximalemenge)</span> | maximale Menge | integer |
| <span className="hbs-f hbs-e0">[einheit](/bo4e/202604/com/Preis#einheit)</span> | Waehrungseinheit | [Enum Waehrungseinheit](/bo4e/202604/enum/Waehrungseinheit)<br/><Werte>`EUR`, `CT`</Werte> |
| <span className="hbs-f hbs-e0">[bezugswert](/bo4e/202604/com/Preis#bezugswert)</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202604/enum/Mengeneinheit)<br/><Werte>`W`, `WH`, `KW`, `KWH`, `KVARH`, `MW`, `MWH`, `STUECK`, `KUBIKMETER`, `STUNDE`, `TAG`, `MONAT`, `JAHR`, `PROZENT`, `ANZAHL`, `VAR`, `KVAR`, `VARH`, `KWHK`, `Z16`, `KWT`, `WATT_PRO_QUADRATMETER`, `METER_PRO_SEKUNDE`</Werte> |
| <span className="hbs-f hbs-e0">[status](/bo4e/202604/com/Preis#status)</span> | Preisstatus | [Enum Preisstatus](/bo4e/202604/enum/Preisstatus)<br/><Werte>`VORLAEUFIG`, `ENDGUELTIG`</Werte> |
| <span className="hbs-f hbs-e0">[preisart](/bo4e/202604/com/Preis#preisart)</span> | Preisart Code | [Enum Preisart](/bo4e/202604/enum/Preisart)<br/><Werte>`EINRICHTUNGSPREIS`, `TRANSAKTIONSPREIS`, `BETRIEBSPREIS`</Werte> |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### wert

8 Verwendung(en) in den Nachrichtentypen INVOIC, ORDRSP, QUOTES, UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_15001](/schnittstellen/202604/pruefi/QUOTES/PI_15001) | Prüfi | QUOTES | stammdaten › ANGEBOT › positionsdaten › positionspreis |
| [PI_15003](/schnittstellen/202604/pruefi/QUOTES/PI_15003) | Prüfi | QUOTES | stammdaten › ANGEBOT › positionsdaten › positionspreis |
| [PI_19116](/schnittstellen/202604/pruefi/ORDRSP/PI_19116) | Prüfi | ORDRSP | stammdaten › AUFTRAG › hoechstpreis |
| [PI_19116](/schnittstellen/202604/pruefi/ORDRSP/PI_19116) | Prüfi | ORDRSP | stammdaten › AUFTRAG › mindestpreis |
| [PI_31002](/schnittstellen/202604/pruefi/INVOIC/PI_31002) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen › einzelpreis |
| [PI_55035](/schnittstellen/202604/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › netznutzungsabrechnungsdaten › preisSingulaereBetriebsmittel |
| [PI_55218](/schnittstellen/202604/pruefi/UTILMD/PI_55218) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › netznutzungsabrechnungsdaten › preisSingulaereBetriebsmittel |
| [PI_55220](/schnittstellen/202604/pruefi/UTILMD/PI_55220) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › netznutzungsabrechnungsdaten › preisSingulaereBetriebsmittel |

### menge

2 Verwendung(en) in den Nachrichtentypen QUOTES.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_15001](/schnittstellen/202604/pruefi/QUOTES/PI_15001) | Prüfi | QUOTES | stammdaten › ANGEBOT › positionsdaten › positionspreis |
| [PI_15003](/schnittstellen/202604/pruefi/QUOTES/PI_15003) | Prüfi | QUOTES | stammdaten › ANGEBOT › positionsdaten › positionspreis |

### bezugswert

3 Verwendung(en) in den Nachrichtentypen INVOIC, QUOTES.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_15001](/schnittstellen/202604/pruefi/QUOTES/PI_15001) | Prüfi | QUOTES | stammdaten › ANGEBOT › positionsdaten › positionspreis |
| [PI_15003](/schnittstellen/202604/pruefi/QUOTES/PI_15003) | Prüfi | QUOTES | stammdaten › ANGEBOT › positionsdaten › positionspreis |
| [PI_31002](/schnittstellen/202604/pruefi/INVOIC/PI_31002) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen › einzelpreis |

### preisart

1 Verwendung(en) in den Nachrichtentypen QUOTES.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_15003](/schnittstellen/202604/pruefi/QUOTES/PI_15003) | Prüfi | QUOTES | stammdaten › ANGEBOT › positionsdaten › positionspreis |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
