# TechnischeEinrichtung
<span hidden data-pagefind-meta={"title:TechnischeEinrichtung — BO4E-Komponente (FV 202610)"} />

BO4E-Komponente · 2 Felder · 8 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="technischeeinrichtungenvorhanden"></a>`technischeEinrichtungenVorhanden` | boolean | true =&gt; ZH7, false =&gt; ZH8 |
| <a id="verbrauchsart"></a>`verbrauchsart` | [Enum Verbrauchsart](/bo4e/202610/enum/Verbrauchsart)<br/><Werte>`KL`, `W`, `EMOB`, `SB`, `SW`, `WK`</Werte> | Verbrauchsart |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[technischeEinrichtungenVorhanden](/bo4e/202610/com/TechnischeEinrichtung#technischeeinrichtungenvorhanden)</span> | true =&gt; ZH7, false =&gt; ZH8 | boolean |
| <span className="hbs-f hbs-e0">[verbrauchsart](/bo4e/202610/com/TechnischeEinrichtung#verbrauchsart)</span> | Verbrauchsart | [Enum Verbrauchsart](/bo4e/202610/enum/Verbrauchsart)<br/><Werte>`KL`, `W`, `EMOB`, `SB`, `SW`, `WK`</Werte> |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### technischeEinrichtungenVorhanden

4 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55035](/schnittstellen/202610/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › technischeEinrichtungen |
| [PI_55060](/schnittstellen/202610/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › technischeEinrichtungen |
| [PI_55616](/schnittstellen/202610/pruefi/UTILMD/PI_55616) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › technischeEinrichtungen |
| [PI_55622](/schnittstellen/202610/pruefi/UTILMD/PI_55622) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › technischeEinrichtungen |

### verbrauchsart

4 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55035](/schnittstellen/202610/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › technischeEinrichtungen |
| [PI_55060](/schnittstellen/202610/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › technischeEinrichtungen |
| [PI_55616](/schnittstellen/202610/pruefi/UTILMD/PI_55616) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › technischeEinrichtungen |
| [PI_55622](/schnittstellen/202610/pruefi/UTILMD/PI_55622) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › technischeEinrichtungen |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
