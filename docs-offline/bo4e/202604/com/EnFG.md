# EnFG
<span hidden data-pagefind-meta={"title:EnFG — BO4E-Komponente (FV 202604)"} />

BO4E-Komponente · 2 Felder · 8 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="grundlageverringerungumlagen"></a>`grundlageVerringerungUmlagen` | [Enum GrundlageVerringerungUmlagen](/bo4e/202604/enum/GrundlageVerringerungUmlagen)<br/><Werte>`ERFUELLT_VORAUSSETZUNG_NACH_ENFG`, `ERFUELLT_NICHT_VORAUSSETZUNG_NACH_ENFG`, `KEINE_ANGABE`</Werte> | GrundlageVerringerungUmlagen |
| <a id="grund"></a>`grund` | [Enum GrundlageVerringerungUmlagenGrund[]](/bo4e/202604/enum/GrundlageVerringerungUmlagenGrund)<br/><Werte>`ENFG_STROMSPEICHER_UND_VERLUSTENERGIE`, `ENFG_ELEKTRISCH_ANGETRIEBENE_WAERMEPUMPEN`, `ENFG_UMLAGEERHEBUNG_BEI_ANLAGEN_ZUR_VERSTROMUNG_VON_KUPPELGASEN`, `ENFG_HERSTELLUNG_VON_GRUENEN_WASSERSTOFF`, `ENFG_STROMKOSTENINTENSIVE_UNTERNEHMEN`, `ENFG_HERSTELLUNG_VON_WASSERSTOFF_IN_STROMKOSTENINTENSIVEN_UNTERNEHMEN`, `ENFG_SCHIENENBAHNEN`, `ENFG_ELEKTRISCHE_BETRIEBENE_BUSSEN_IM_LINIENVERKEHR`, `ENFG_LANDSTROMANLAGEN`</Werte> | Grund der Umlagenverringerung |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[grundlageVerringerungUmlagen](/bo4e/202604/com/EnFG#grundlageverringerungumlagen)</span> | GrundlageVerringerungUmlagen | [Enum GrundlageVerringerungUmlagen](/bo4e/202604/enum/GrundlageVerringerungUmlagen)<br/><Werte>`ERFUELLT_VORAUSSETZUNG_NACH_ENFG`, `ERFUELLT_NICHT_VORAUSSETZUNG_NACH_ENFG`, `KEINE_ANGABE`</Werte> |
| <span className="hbs-f hbs-e0">[grund](/bo4e/202604/com/EnFG#grund) <span className="hbs-liste">[ ]</span></span> | Grund der Umlagenverringerung | [Enum GrundlageVerringerungUmlagenGrund[]](/bo4e/202604/enum/GrundlageVerringerungUmlagenGrund)<br/><Werte>`ENFG_STROMSPEICHER_UND_VERLUSTENERGIE`, `ENFG_ELEKTRISCH_ANGETRIEBENE_WAERMEPUMPEN`, `ENFG_UMLAGEERHEBUNG_BEI_ANLAGEN_ZUR_VERSTROMUNG_VON_KUPPELGASEN`, `ENFG_HERSTELLUNG_VON_GRUENEN_WASSERSTOFF`, `ENFG_STROMKOSTENINTENSIVE_UNTERNEHMEN`, `ENFG_HERSTELLUNG_VON_WASSERSTOFF_IN_STROMKOSTENINTENSIVEN_UNTERNEHMEN`, `ENFG_SCHIENENBAHNEN`, `ENFG_ELEKTRISCHE_BETRIEBENE_BUSSEN_IM_LINIENVERKEHR`, `ENFG_LANDSTROMANLAGEN`</Werte> |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### grundlageVerringerungUmlagen

4 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55001](/schnittstellen/202604/pruefi/UTILMD/PI_55001) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › enFG |
| [PI_55014](/schnittstellen/202604/pruefi/UTILMD/PI_55014) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › enFG |
| [PI_55109](/schnittstellen/202604/pruefi/UTILMD/PI_55109) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › enFG |
| [PI_55137](/schnittstellen/202604/pruefi/UTILMD/PI_55137) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › enFG |

### grund

4 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55001](/schnittstellen/202604/pruefi/UTILMD/PI_55001) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › enFG |
| [PI_55014](/schnittstellen/202604/pruefi/UTILMD/PI_55014) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › enFG |
| [PI_55109](/schnittstellen/202604/pruefi/UTILMD/PI_55109) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › enFG |
| [PI_55137](/schnittstellen/202604/pruefi/UTILMD/PI_55137) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › enFG |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
