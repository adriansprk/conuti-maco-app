# ZuordnungObjectcode
<span hidden data-pagefind-meta={"title:ZuordnungObjectcode — BO4E-Komponente (FV 202610)"} />

BO4E-Komponente · 6 Felder · 55 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="referenzlokationstyp"></a>`referenzLokationsTyp` | [Enum Lokationstyp](/bo4e/202610/enum/Lokationstyp)<br/><Werte>`MALO`, `MELO`, `NELO`, `TECHNISCHE_RESSOURCE`, `STEUERBARE_RESSOURCE`, `TRANCHE`, `MABIS_ZAEHLPUNKT`</Werte> | Gibt an, ob es sich um eine Markt- oder Messlokation handelt |
| <a id="referenzlokationsid"></a>`referenzLokationsId` | string | referenzLokationsId |
| <a id="vorgelagertelokationtyp"></a>`vorgelagerteLokationTyp` | [Enum Lokationstyp](/bo4e/202610/enum/Lokationstyp)<br/><Werte>`MALO`, `MELO`, `NELO`, `TECHNISCHE_RESSOURCE`, `STEUERBARE_RESSOURCE`, `TRANCHE`, `MABIS_ZAEHLPUNKT`</Werte> | Gibt an, ob es sich um eine Markt- oder Messlokation handelt |
| <a id="vorgelagertelokationid"></a>`vorgelagerteLokationId` | string | vorgelagerteLokationId |
| <a id="objectcode"></a>`objectcode` | [Objectcode[]](/bo4e/202610/com/Objectcode) | objectcode |
| <a id="referenzmarktlokationtechnischeressource"></a>`referenzMarktlokationTechnischeRessource` | string[] | referenzMarktlokationTechnischeRessource |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[referenzLokationsTyp](/bo4e/202610/com/ZuordnungObjectcode#referenzlokationstyp)</span> | Gibt an, ob es sich um eine Markt- oder Messlokation handelt | [Enum Lokationstyp](/bo4e/202610/enum/Lokationstyp)<br/><Werte>`MALO`, `MELO`, `NELO`, `TECHNISCHE_RESSOURCE`, `STEUERBARE_RESSOURCE`, `TRANCHE`, `MABIS_ZAEHLPUNKT`</Werte> |
| <span className="hbs-f hbs-e0">[referenzLokationsId](/bo4e/202610/com/ZuordnungObjectcode#referenzlokationsid)</span> | referenzLokationsId | string |
| <span className="hbs-f hbs-e0">[vorgelagerteLokationTyp](/bo4e/202610/com/ZuordnungObjectcode#vorgelagertelokationtyp)</span> | Gibt an, ob es sich um eine Markt- oder Messlokation handelt | [Enum Lokationstyp](/bo4e/202610/enum/Lokationstyp)<br/><Werte>`MALO`, `MELO`, `NELO`, `TECHNISCHE_RESSOURCE`, `STEUERBARE_RESSOURCE`, `TRANCHE`, `MABIS_ZAEHLPUNKT`</Werte> |
| <span className="hbs-f hbs-e0">[vorgelagerteLokationId](/bo4e/202610/com/ZuordnungObjectcode#vorgelagertelokationid)</span> | vorgelagerteLokationId | string |
| <span className="hbs-g hbs-e0">[objectcode](/bo4e/202610/com/ZuordnungObjectcode#objectcode) <span className="hbs-liste">[ ]</span></span> | objectcode | [Objectcode[]](/bo4e/202610/com/Objectcode) |
| <span className="hbs-f hbs-e1">[objectcode](/bo4e/202610/com/Objectcode#objectcode)</span> | objectcode | string |
| <span className="hbs-f hbs-e1">[lokationsbuendelNummer](/bo4e/202610/com/Objectcode#lokationsbuendelnummer)</span> | lokationsbuendelNummer | integer |
| <span className="hbs-f hbs-e0">[referenzMarktlokationTechnischeRessource](/bo4e/202610/com/ZuordnungObjectcode#referenzmarktlokationtechnischeressource) <span className="hbs-liste">[ ]</span></span> | referenzMarktlokationTechnischeRessource | string[] |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### referenzLokationsTyp

11 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55035](/schnittstellen/202610/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › zuordnungObjectcode |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › zuordnungObjectcode |
| [PI_55060](/schnittstellen/202610/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › zuordnungObjectcode |
| [PI_55095](/schnittstellen/202610/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › zuordnungObjectcode |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › zuordnungObjectcode |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › zuordnungObjectcode |
| [PI_55173](/schnittstellen/202610/pruefi/UTILMD/PI_55173) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › zuordnungObjectcode |
| [PI_55175](/schnittstellen/202610/pruefi/UTILMD/PI_55175) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › zuordnungObjectcode |
| [PI_55177](/schnittstellen/202610/pruefi/UTILMD/PI_55177) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › zuordnungObjectcode |
| [PI_55180](/schnittstellen/202610/pruefi/UTILMD/PI_55180) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › zuordnungObjectcode |
| [PI_55690](/schnittstellen/202610/pruefi/UTILMD/PI_55690) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › zuordnungObjectcode |

### referenzLokationsId

11 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55035](/schnittstellen/202610/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › zuordnungObjectcode |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › zuordnungObjectcode |
| [PI_55060](/schnittstellen/202610/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › zuordnungObjectcode |
| [PI_55095](/schnittstellen/202610/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › zuordnungObjectcode |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › zuordnungObjectcode |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › zuordnungObjectcode |
| [PI_55173](/schnittstellen/202610/pruefi/UTILMD/PI_55173) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › zuordnungObjectcode |
| [PI_55175](/schnittstellen/202610/pruefi/UTILMD/PI_55175) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › zuordnungObjectcode |
| [PI_55177](/schnittstellen/202610/pruefi/UTILMD/PI_55177) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › zuordnungObjectcode |
| [PI_55180](/schnittstellen/202610/pruefi/UTILMD/PI_55180) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › zuordnungObjectcode |
| [PI_55690](/schnittstellen/202610/pruefi/UTILMD/PI_55690) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › zuordnungObjectcode |

### vorgelagerteLokationTyp

11 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55035](/schnittstellen/202610/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › zuordnungObjectcode |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › zuordnungObjectcode |
| [PI_55060](/schnittstellen/202610/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › zuordnungObjectcode |
| [PI_55095](/schnittstellen/202610/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › zuordnungObjectcode |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › zuordnungObjectcode |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › zuordnungObjectcode |
| [PI_55173](/schnittstellen/202610/pruefi/UTILMD/PI_55173) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › zuordnungObjectcode |
| [PI_55175](/schnittstellen/202610/pruefi/UTILMD/PI_55175) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › zuordnungObjectcode |
| [PI_55177](/schnittstellen/202610/pruefi/UTILMD/PI_55177) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › zuordnungObjectcode |
| [PI_55180](/schnittstellen/202610/pruefi/UTILMD/PI_55180) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › zuordnungObjectcode |
| [PI_55690](/schnittstellen/202610/pruefi/UTILMD/PI_55690) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › zuordnungObjectcode |

### vorgelagerteLokationId

11 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55035](/schnittstellen/202610/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › zuordnungObjectcode |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › zuordnungObjectcode |
| [PI_55060](/schnittstellen/202610/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › zuordnungObjectcode |
| [PI_55095](/schnittstellen/202610/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › zuordnungObjectcode |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › zuordnungObjectcode |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › zuordnungObjectcode |
| [PI_55173](/schnittstellen/202610/pruefi/UTILMD/PI_55173) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › zuordnungObjectcode |
| [PI_55175](/schnittstellen/202610/pruefi/UTILMD/PI_55175) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › zuordnungObjectcode |
| [PI_55177](/schnittstellen/202610/pruefi/UTILMD/PI_55177) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › zuordnungObjectcode |
| [PI_55180](/schnittstellen/202610/pruefi/UTILMD/PI_55180) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › zuordnungObjectcode |
| [PI_55690](/schnittstellen/202610/pruefi/UTILMD/PI_55690) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › zuordnungObjectcode |

### referenzMarktlokationTechnischeRessource

11 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55035](/schnittstellen/202610/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › zuordnungObjectcode |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › zuordnungObjectcode |
| [PI_55060](/schnittstellen/202610/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › zuordnungObjectcode |
| [PI_55095](/schnittstellen/202610/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › zuordnungObjectcode |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › zuordnungObjectcode |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › zuordnungObjectcode |
| [PI_55173](/schnittstellen/202610/pruefi/UTILMD/PI_55173) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › zuordnungObjectcode |
| [PI_55175](/schnittstellen/202610/pruefi/UTILMD/PI_55175) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › zuordnungObjectcode |
| [PI_55177](/schnittstellen/202610/pruefi/UTILMD/PI_55177) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › zuordnungObjectcode |
| [PI_55180](/schnittstellen/202610/pruefi/UTILMD/PI_55180) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › zuordnungObjectcode |
| [PI_55690](/schnittstellen/202610/pruefi/UTILMD/PI_55690) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › zuordnungObjectcode |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
