# Preisstaffel
<span hidden data-pagefind-meta={"title:Preisstaffel — BO4E-Komponente (FV 202604)"} />

BO4E-Komponente · 6 Felder · 7 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="einheitspreis"></a>`einheitspreis` | number (float) | einheitspreis |
| <a id="zeitbasis"></a>`zeitbasis` | [Enum Zeiteinheit](/bo4e/202604/enum/Zeiteinheit)<br/><Werte>`SEKUNDE`, `MINUTE`, `STUNDE`, `VIERTEL_STUNDE`, `TAG`, `WOCHE`, `MONAT`, `QUARTAL`, `HALBJAHR`, `JAHR`</Werte> | Die Zeit(dauer) auf die sich der Preis bezieht. Z.B. ein Jahr für einen Leistungspreis der in €/kW/Jahr ausgegeben wird. |
| <a id="staffelgrenzevon"></a>`staffelgrenzeVon` | number (float) | staffelgrenzeVon |
| <a id="staffelgrenzebis"></a>`staffelgrenzeBis` | number (float) | staffelgrenzeBis |
| <a id="sigmoidparameter"></a>`sigmoidparameter` | [Sigmoidparameter](/bo4e/202604/com/Sigmoidparameter) | — |
| <a id="einheit"></a>`einheit` | [Enum Mengeneinheit](/bo4e/202604/enum/Mengeneinheit)<br/><Werte>`W`, `WH`, `KW`, `KWH`, `KVARH`, `MW`, `MWH`, `STUECK`, `KUBIKMETER`, `STUNDE`, `TAG`, `MONAT`, `JAHR`, `PROZENT`, `ANZAHL`, `VAR`, `KVAR`, `VARH`, `KWHK`, `Z16`, `KWT`, `WATT_PRO_QUADRATMETER`, `METER_PRO_SEKUNDE`</Werte> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[einheitspreis](/bo4e/202604/com/Preisstaffel#einheitspreis)</span> | einheitspreis | number (float) |
| <span className="hbs-f hbs-e0">[zeitbasis](/bo4e/202604/com/Preisstaffel#zeitbasis)</span> | Die Zeit(dauer) auf die sich der Preis bezieht. Z.B. ein Jahr für einen Leistungspreis der in €/kW/Jahr<br/>ausgegeben wird. | [Enum Zeiteinheit](/bo4e/202604/enum/Zeiteinheit)<br/><Werte>`SEKUNDE`, `MINUTE`, `STUNDE`, `VIERTEL_STUNDE`, `TAG`, `WOCHE`, `MONAT`, `QUARTAL`, `HALBJAHR`, `JAHR`</Werte> |
| <span className="hbs-f hbs-e0">[staffelgrenzeVon](/bo4e/202604/com/Preisstaffel#staffelgrenzevon)</span> | staffelgrenzeVon | number (float) |
| <span className="hbs-f hbs-e0">[staffelgrenzeBis](/bo4e/202604/com/Preisstaffel#staffelgrenzebis)</span> | staffelgrenzeBis | number (float) |
| <span className="hbs-g hbs-e0">[sigmoidparameter](/bo4e/202604/com/Preisstaffel#sigmoidparameter)</span> | — | [Sigmoidparameter](/bo4e/202604/com/Sigmoidparameter) |
| <span className="hbs-f hbs-e1">[A](/bo4e/202604/com/Sigmoidparameter#a)</span> | A | number (float) |
| <span className="hbs-f hbs-e1">[B](/bo4e/202604/com/Sigmoidparameter#b)</span> | B | number (float) |
| <span className="hbs-f hbs-e1">[C](/bo4e/202604/com/Sigmoidparameter#c)</span> | C | number (float) |
| <span className="hbs-f hbs-e1">[D](/bo4e/202604/com/Sigmoidparameter#d)</span> | D | number (float) |
| <span className="hbs-f hbs-e0">[einheit](/bo4e/202604/com/Preisstaffel#einheit)</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202604/enum/Mengeneinheit)<br/><Werte>`W`, `WH`, `KW`, `KWH`, `KVARH`, `MW`, `MWH`, `STUECK`, `KUBIKMETER`, `STUNDE`, `TAG`, `MONAT`, `JAHR`, `PROZENT`, `ANZAHL`, `VAR`, `KVAR`, `VARH`, `KWHK`, `Z16`, `KWT`, `WATT_PRO_QUADRATMETER`, `METER_PRO_SEKUNDE`</Werte> |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### einheitspreis

2 Verwendung(en) in den Nachrichtentypen PRICAT.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_27002](/schnittstellen/202604/pruefi/PRICAT/PI_27002) | Prüfi | PRICAT | stammdaten › PREISBLATT › preispositionen › preisstaffeln |
| [PI_27003](/schnittstellen/202604/pruefi/PRICAT/PI_27003) | Prüfi | PRICAT | stammdaten › PREISBLATT › preispositionen › preisstaffeln |

### staffelgrenzeVon

2 Verwendung(en) in den Nachrichtentypen PRICAT.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_27002](/schnittstellen/202604/pruefi/PRICAT/PI_27002) | Prüfi | PRICAT | stammdaten › PREISBLATT › preispositionen › preisstaffeln |
| [PI_27003](/schnittstellen/202604/pruefi/PRICAT/PI_27003) | Prüfi | PRICAT | stammdaten › PREISBLATT › preispositionen › preisstaffeln |

### staffelgrenzeBis

2 Verwendung(en) in den Nachrichtentypen PRICAT.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_27002](/schnittstellen/202604/pruefi/PRICAT/PI_27002) | Prüfi | PRICAT | stammdaten › PREISBLATT › preispositionen › preisstaffeln |
| [PI_27003](/schnittstellen/202604/pruefi/PRICAT/PI_27003) | Prüfi | PRICAT | stammdaten › PREISBLATT › preispositionen › preisstaffeln |

### einheit

1 Verwendung(en) in den Nachrichtentypen PRICAT.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_27002](/schnittstellen/202604/pruefi/PRICAT/PI_27002) | Prüfi | PRICAT | stammdaten › PREISBLATT › preispositionen › preisstaffeln |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
