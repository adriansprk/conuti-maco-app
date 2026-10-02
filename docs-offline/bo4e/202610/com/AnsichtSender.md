# AnsichtSender
<span hidden data-pagefind-meta={"title:AnsichtSender — BO4E-Komponente (FV 202610)"} />

BO4E-Komponente · 5 Felder · 4 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="verwendungab"></a>`verwendungAb` | string (date-time) | verwendungAb |
| <a id="verwendungbis"></a>`verwendungBis` | string (date-time) | verwendungBis |
| <a id="leistungsperiode"></a>`leistungsperiode` | string | leistungsperiode |
| <a id="menge"></a>`menge` | [Menge](/bo4e/202610/com/Menge) | — |
| <a id="tarifstufe"></a>`tarifstufe` | [Enum Tarifstufe](/bo4e/202610/enum/Tarifstufe)<br/><Werte>`TARIFSTUFE_0`, `TARIFSTUFE_1`, `TARIFSTUFE_2`, `TARIFSTUFE_3`, `TARIFSTUFE_4`, `TARIFSTUFE_5`, `TARIFSTUFE_6`, `TARIFSTUFE_7`, `TARIFSTUFE_8`, `TARIFSTUFE_9`</Werte> | Tarifstufe |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[verwendungAb](/bo4e/202610/com/AnsichtSender#verwendungab)</span> | verwendungAb | string (date-time) |
| <span className="hbs-f hbs-e0">[verwendungBis](/bo4e/202610/com/AnsichtSender#verwendungbis)</span> | verwendungBis | string (date-time) |
| <span className="hbs-f hbs-e0">[leistungsperiode](/bo4e/202610/com/AnsichtSender#leistungsperiode)</span> | leistungsperiode | string |
| <span className="hbs-g hbs-e0">[menge](/bo4e/202610/com/AnsichtSender#menge)</span> | — | [Menge](/bo4e/202610/com/Menge) |
| <span className="hbs-f hbs-e1">[wert](/bo4e/202610/com/Menge#wert)</span> | Wert | number (float) |
| <span className="hbs-f hbs-e1">[einheit](/bo4e/202610/com/Menge#einheit)</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202610/enum/Mengeneinheit)<br/><Werte>`W`, `WH`, `KW`, `KWH`, `KVARH`, `MW`, `MWH`, `STUECK`, `KUBIKMETER`, `STUNDE`, `TAG`, `MONAT`, `JAHR`, `PROZENT`, `ANZAHL`, `VAR`, `KVAR`, `VARH`, `KWHK`, `Z16`, `KWT`, `WATT_PRO_QUADRATMETER`, `METER_PRO_SEKUNDE`</Werte> |
| <span className="hbs-f hbs-e1">[startdatum](/bo4e/202610/com/Menge#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e1">[enddatum](/bo4e/202610/com/Menge#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-f hbs-e0">[tarifstufe](/bo4e/202610/com/AnsichtSender#tarifstufe)</span> | Tarifstufe | [Enum Tarifstufe](/bo4e/202610/enum/Tarifstufe)<br/><Werte>`TARIFSTUFE_0`, `TARIFSTUFE_1`, `TARIFSTUFE_2`, `TARIFSTUFE_3`, `TARIFSTUFE_4`, `TARIFSTUFE_5`, `TARIFSTUFE_6`, `TARIFSTUFE_7`, `TARIFSTUFE_8`, `TARIFSTUFE_9`</Werte> |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### verwendungAb

1 Verwendung(en) in den Nachrichtentypen IFTSTA.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_21035](/schnittstellen/202610/pruefi/IFTSTA/PI_21035) | Prüfi | IFTSTA | stammdaten › STATUSMITTEILUNG › positionsdaten › ansichtSender |

### verwendungBis

1 Verwendung(en) in den Nachrichtentypen IFTSTA.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_21035](/schnittstellen/202610/pruefi/IFTSTA/PI_21035) | Prüfi | IFTSTA | stammdaten › STATUSMITTEILUNG › positionsdaten › ansichtSender |

### leistungsperiode

1 Verwendung(en) in den Nachrichtentypen IFTSTA.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_21035](/schnittstellen/202610/pruefi/IFTSTA/PI_21035) | Prüfi | IFTSTA | stammdaten › STATUSMITTEILUNG › positionsdaten › ansichtSender |

### tarifstufe

1 Verwendung(en) in den Nachrichtentypen IFTSTA.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_21035](/schnittstellen/202610/pruefi/IFTSTA/PI_21035) | Prüfi | IFTSTA | stammdaten › STATUSMITTEILUNG › positionsdaten › ansichtSender |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
