# Energieherkunft
<span hidden data-pagefind-meta={"title:Energieherkunft — BO4E-Komponente (FV 202604)"} />

BO4E-Komponente · 2 Felder · 12 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="erzeugungsart"></a>`erzeugungsart` | [Enum Erzeugungsart](/bo4e/202604/enum/Erzeugungsart)<br/><Werte>`EEG`, `KWK`, `EEG_DV`, `KWK_DV`, `WIND`, `SOLAR`, `KERNKRAFT`, `WASSER`, `GEOTHERMIE`, `BIOMASSE`, `KOHLE`, `GAS`, `SONSTIGE`, `SONSTIGE_EEG`, `SONSTIGE_ERZEUGUNGSART`</Werte> | Art der Erzeugung |
| <a id="anteilprozent"></a>`anteilProzent` | number (float) | Prozentualer Anteil der Erzeugung |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[erzeugungsart](/bo4e/202604/com/Energieherkunft#erzeugungsart)</span> | Art der Erzeugung | [Enum Erzeugungsart](/bo4e/202604/enum/Erzeugungsart)<br/><Werte>`EEG`, `KWK`, `EEG_DV`, `KWK_DV`, `WIND`, `SOLAR`, `KERNKRAFT`, `WASSER`, `GEOTHERMIE`, `BIOMASSE`, `KOHLE`, `GAS`, `SONSTIGE`, `SONSTIGE_EEG`, `SONSTIGE_ERZEUGUNGSART`</Werte> |
| <span className="hbs-f hbs-e0">[anteilProzent](/bo4e/202604/com/Energieherkunft#anteilprozent)</span> | Prozentualer Anteil der Erzeugung | number (float) |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### erzeugungsart

12 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › energieherkunft |
| [PI_55060](/schnittstellen/202604/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › energieherkunft |
| [PI_55074](/schnittstellen/202604/pruefi/UTILMD/PI_55074) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › energieherkunft |
| [PI_55075](/schnittstellen/202604/pruefi/UTILMD/PI_55075) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › energieherkunft |
| [PI_55095](/schnittstellen/202604/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › energieherkunft |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › energieherkunft |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › energieherkunft |
| [PI_55607](/schnittstellen/202604/pruefi/UTILMD/PI_55607) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › energieherkunft |
| [PI_55616](/schnittstellen/202604/pruefi/UTILMD/PI_55616) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › energieherkunft |
| [PI_55622](/schnittstellen/202604/pruefi/UTILMD/PI_55622) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › energieherkunft |
| [PI_55628](/schnittstellen/202604/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › energieherkunft |
| [PI_55634](/schnittstellen/202604/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › energieherkunft |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
