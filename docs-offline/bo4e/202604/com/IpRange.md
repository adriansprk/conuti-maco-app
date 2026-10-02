# IpRange
<span hidden data-pagefind-meta={"title:IpRange — BO4E-Komponente (FV 202604)"} />

BO4E-Komponente · 2 Felder · 6 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="unteregrenze"></a>`untereGrenze` | string | untereGrenze |
| <a id="oberegrenze"></a>`obereGrenze` | string | obereGrenze |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[untereGrenze](/bo4e/202604/com/IpRange#unteregrenze)</span> | untereGrenze | string |
| <span className="hbs-f hbs-e0">[obereGrenze](/bo4e/202604/com/IpRange#oberegrenze)</span> | obereGrenze | string |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### untereGrenze

3 Verwendung(en) in den Nachrichtentypen ORDRSP, UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_19011](/schnittstellen/202604/pruefi/ORDRSP/PI_19011) | Prüfi | ORDRSP | transaktionsdaten › absender › ipRange |
| [PI_55553](/schnittstellen/202604/pruefi/UTILMD/PI_55553) | Prüfi | UTILMD | transaktionsdaten › absender › ipRange |
| [PI_55555](/schnittstellen/202604/pruefi/UTILMD/PI_55555) | Prüfi | UTILMD | transaktionsdaten › absender › ipRange |

### obereGrenze

3 Verwendung(en) in den Nachrichtentypen ORDRSP, UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_19011](/schnittstellen/202604/pruefi/ORDRSP/PI_19011) | Prüfi | ORDRSP | transaktionsdaten › absender › ipRange |
| [PI_55553](/schnittstellen/202604/pruefi/UTILMD/PI_55553) | Prüfi | UTILMD | transaktionsdaten › absender › ipRange |
| [PI_55555](/schnittstellen/202604/pruefi/UTILMD/PI_55555) | Prüfi | UTILMD | transaktionsdaten › absender › ipRange |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
