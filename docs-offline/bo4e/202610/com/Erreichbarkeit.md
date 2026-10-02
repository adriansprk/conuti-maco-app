# Erreichbarkeit
<span hidden data-pagefind-meta={"title:Erreichbarkeit — BO4E-Komponente (FV 202610)"} />

BO4E-Komponente · 2 Felder · 18 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="verfuegbarkeit"></a>`verfuegbarkeit` | [Enum Verfuegbarkeit](/bo4e/202610/enum/Verfuegbarkeit)<br/><Werte>`MONTAG`, `DIENSTAG`, `MITTWOCH`, `DONNERSTAG`, `FREITAG`, `PAUSE`</Werte> | Verfuegbarkeit |
| <a id="zeit"></a>`zeit` | string | Zeit der Erreichbarkeit |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[verfuegbarkeit](/bo4e/202610/com/Erreichbarkeit#verfuegbarkeit)</span> | Verfuegbarkeit | [Enum Verfuegbarkeit](/bo4e/202610/enum/Verfuegbarkeit)<br/><Werte>`MONTAG`, `DIENSTAG`, `MITTWOCH`, `DONNERSTAG`, `FREITAG`, `PAUSE`</Werte> |
| <span className="hbs-f hbs-e0">[zeit](/bo4e/202610/com/Erreichbarkeit#zeit)</span> | Zeit der Erreichbarkeit | string |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### verfuegbarkeit

9 Verwendung(en) in den Nachrichtentypen PARTIN.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_37000](/schnittstellen/202610/pruefi/PARTIN/PI_37000) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer › erreichbarkeit |
| [PI_37001](/schnittstellen/202610/pruefi/PARTIN/PI_37001) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer › erreichbarkeit |
| [PI_37002](/schnittstellen/202610/pruefi/PARTIN/PI_37002) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer › erreichbarkeit |
| [PI_37008](/schnittstellen/202610/pruefi/PARTIN/PI_37008) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer › erreichbarkeit |
| [PI_37009](/schnittstellen/202610/pruefi/PARTIN/PI_37009) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer › erreichbarkeit |
| [PI_37010](/schnittstellen/202610/pruefi/PARTIN/PI_37010) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer › erreichbarkeit |
| [PI_37012](/schnittstellen/202610/pruefi/PARTIN/PI_37012) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer › erreichbarkeit |
| [PI_37013](/schnittstellen/202610/pruefi/PARTIN/PI_37013) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer › erreichbarkeit |
| [PI_37014](/schnittstellen/202610/pruefi/PARTIN/PI_37014) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer › erreichbarkeit |

### zeit

9 Verwendung(en) in den Nachrichtentypen PARTIN.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_37000](/schnittstellen/202610/pruefi/PARTIN/PI_37000) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer › erreichbarkeit |
| [PI_37001](/schnittstellen/202610/pruefi/PARTIN/PI_37001) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer › erreichbarkeit |
| [PI_37002](/schnittstellen/202610/pruefi/PARTIN/PI_37002) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer › erreichbarkeit |
| [PI_37008](/schnittstellen/202610/pruefi/PARTIN/PI_37008) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer › erreichbarkeit |
| [PI_37009](/schnittstellen/202610/pruefi/PARTIN/PI_37009) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer › erreichbarkeit |
| [PI_37010](/schnittstellen/202610/pruefi/PARTIN/PI_37010) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer › erreichbarkeit |
| [PI_37012](/schnittstellen/202610/pruefi/PARTIN/PI_37012) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer › erreichbarkeit |
| [PI_37013](/schnittstellen/202610/pruefi/PARTIN/PI_37013) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer › erreichbarkeit |
| [PI_37014](/schnittstellen/202610/pruefi/PARTIN/PI_37014) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer › erreichbarkeit |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
