# ApnKommunikationsdatenZugriffsparameter
<span hidden data-pagefind-meta={"title:ApnKommunikationsdatenZugriffsparameter — BO4E-Komponente (FV 202610)"} />

BO4E-Komponente · 3 Felder · 3 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="apnname"></a>`apnName` | string | Name des APNs |
| <a id="nutzer"></a>`nutzer` | string | Nutzer |
| <a id="passwort"></a>`passwort` | string | Passwort |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[apnName](/bo4e/202610/com/ApnKommunikationsdatenZugriffsparameter#apnname)</span> | Name des APNs | string |
| <span className="hbs-f hbs-e0">[nutzer](/bo4e/202610/com/ApnKommunikationsdatenZugriffsparameter#nutzer)</span> | Nutzer | string |
| <span className="hbs-f hbs-e0">[passwort](/bo4e/202610/com/ApnKommunikationsdatenZugriffsparameter#passwort)</span> | Passwort | string |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### apnName

1 Verwendung(en) in den Nachrichtentypen ORDRSP.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_19001](/schnittstellen/202610/pruefi/ORDRSP/PI_19001) | Prüfi | ORDRSP | stammdaten › AUFTRAG › positionsdaten › apnKommunikationsdatenZugriffsparameter |

### nutzer

1 Verwendung(en) in den Nachrichtentypen ORDRSP.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_19001](/schnittstellen/202610/pruefi/ORDRSP/PI_19001) | Prüfi | ORDRSP | stammdaten › AUFTRAG › positionsdaten › apnKommunikationsdatenZugriffsparameter |

### passwort

1 Verwendung(en) in den Nachrichtentypen ORDRSP.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_19001](/schnittstellen/202610/pruefi/ORDRSP/PI_19001) | Prüfi | ORDRSP | stammdaten › AUFTRAG › positionsdaten › apnKommunikationsdatenZugriffsparameter |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
