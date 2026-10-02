# Zeitraum
<span hidden data-pagefind-meta={"title:Zeitraum — BO4E-Komponente (FV 202610)"} />

BO4E-Komponente · 9 Felder · 201 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="zeiteinheit"></a>`zeiteinheit` | [Enum Zeiteinheit](/bo4e/202610/enum/Zeiteinheit)<br/><Werte>`SEKUNDE`, `MINUTE`, `STUNDE`, `VIERTEL_STUNDE`, `TAG`, `WOCHE`, `MONAT`, `QUARTAL`, `HALBJAHR`, `JAHR`</Werte> | Zeiteinheit |
| <a id="dauer"></a>`dauer` | integer | dauer |
| <a id="startdatum"></a>`startdatum` | string (date-time) | startdatum |
| <a id="enddatum"></a>`enddatum` | string (date-time) | enddatum |
| <a id="einheit"></a>`einheit` | [Enum Zeiteinheit](/bo4e/202610/enum/Zeiteinheit)<br/><Werte>`SEKUNDE`, `MINUTE`, `STUNDE`, `VIERTEL_STUNDE`, `TAG`, `WOCHE`, `MONAT`, `QUARTAL`, `HALBJAHR`, `JAHR`</Werte> | Zeiteinheit |
| <a id="ablesezeitraum"></a>`ableseZeitraum` | string | ableseZeitraum |
| <a id="abrechnungszeitraum"></a>`abrechnungsZeitraum` | string | abrechnungsZeitraum |
| <a id="zeitraumtext"></a>`zeitraumText` | string | zeitraumText |
| <a id="zeitraumid"></a>`zeitraumId` | integer | zeitraumId |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[zeiteinheit](/bo4e/202610/com/Zeitraum#zeiteinheit)</span> | Zeiteinheit | [Enum Zeiteinheit](/bo4e/202610/enum/Zeiteinheit)<br/><Werte>`SEKUNDE`, `MINUTE`, `STUNDE`, `VIERTEL_STUNDE`, `TAG`, `WOCHE`, `MONAT`, `QUARTAL`, `HALBJAHR`, `JAHR`</Werte> |
| <span className="hbs-f hbs-e0">[dauer](/bo4e/202610/com/Zeitraum#dauer)</span> | dauer | integer |
| <span className="hbs-f hbs-e0">[startdatum](/bo4e/202610/com/Zeitraum#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e0">[enddatum](/bo4e/202610/com/Zeitraum#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-f hbs-e0">[einheit](/bo4e/202610/com/Zeitraum#einheit)</span> | Zeiteinheit | [Enum Zeiteinheit](/bo4e/202610/enum/Zeiteinheit)<br/><Werte>`SEKUNDE`, `MINUTE`, `STUNDE`, `VIERTEL_STUNDE`, `TAG`, `WOCHE`, `MONAT`, `QUARTAL`, `HALBJAHR`, `JAHR`</Werte> |
| <span className="hbs-f hbs-e0">[ableseZeitraum](/bo4e/202610/com/Zeitraum#ablesezeitraum)</span> | ableseZeitraum | string |
| <span className="hbs-f hbs-e0">[abrechnungsZeitraum](/bo4e/202610/com/Zeitraum#abrechnungszeitraum)</span> | abrechnungsZeitraum | string |
| <span className="hbs-f hbs-e0">[zeitraumText](/bo4e/202610/com/Zeitraum#zeitraumtext)</span> | zeitraumText | string |
| <span className="hbs-f hbs-e0">[zeitraumId](/bo4e/202610/com/Zeitraum#zeitraumid)</span> | zeitraumId | integer |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### dauer

2 Verwendung(en) in den Nachrichtentypen QUOTES.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_15003](/schnittstellen/202610/pruefi/QUOTES/PI_15003) | Prüfi | QUOTES | stammdaten › ANGEBOT › bindefristAngebot |
| [PI_15003](/schnittstellen/202610/pruefi/QUOTES/PI_15003) | Prüfi | QUOTES | stammdaten › ANGEBOT › zeitspanneEinrichtungUebermittlungWerte |

### startdatum

15 Verwendung(en) in den Nachrichtentypen INVOIC, ORDERS, PRICAT.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_17113](/schnittstellen/202610/pruefi/ORDERS/PI_17113) | Prüfi | ORDERS | stammdaten › REKLAMATION › zeitraumMesswertanfrage |
| [PI_27002](/schnittstellen/202610/pruefi/PRICAT/PI_27002) | Prüfi | PRICAT | stammdaten › PREISBLATT › gueltigkeit |
| [PI_27003](/schnittstellen/202610/pruefi/PRICAT/PI_27003) | Prüfi | PRICAT | stammdaten › PREISBLATT › gueltigkeit |
| [PI_31001](/schnittstellen/202610/pruefi/INVOIC/PI_31001) | Prüfi | INVOIC | stammdaten › RECHNUNG › vorlaeufigerAbrechnungszeitraum |
| [PI_31002](/schnittstellen/202610/pruefi/INVOIC/PI_31002) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungsperiode |
| [PI_31003](/schnittstellen/202610/pruefi/INVOIC/PI_31003) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungsperiode |
| [PI_31004](/schnittstellen/202610/pruefi/INVOIC/PI_31004) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungsperiode |
| [PI_31004](/schnittstellen/202610/pruefi/INVOIC/PI_31004) | Prüfi | INVOIC | stammdaten › RECHNUNG › vorlaeufigerAbrechnungszeitraum |
| [PI_31005](/schnittstellen/202610/pruefi/INVOIC/PI_31005) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungsperiode |
| [PI_31006](/schnittstellen/202610/pruefi/INVOIC/PI_31006) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungsperiode |
| [PI_31007](/schnittstellen/202610/pruefi/INVOIC/PI_31007) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungsperiode |
| [PI_31008](/schnittstellen/202610/pruefi/INVOIC/PI_31008) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungsperiode |
| [PI_31009](/schnittstellen/202610/pruefi/INVOIC/PI_31009) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungsperiode |
| [PI_31010](/schnittstellen/202610/pruefi/INVOIC/PI_31010) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungsperiode |
| [PI_31011](/schnittstellen/202610/pruefi/INVOIC/PI_31011) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungsperiode |

### enddatum

13 Verwendung(en) in den Nachrichtentypen INVOIC, ORDERS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_17113](/schnittstellen/202610/pruefi/ORDERS/PI_17113) | Prüfi | ORDERS | stammdaten › REKLAMATION › zeitraumMesswertanfrage |
| [PI_31001](/schnittstellen/202610/pruefi/INVOIC/PI_31001) | Prüfi | INVOIC | stammdaten › RECHNUNG › vorlaeufigerAbrechnungszeitraum |
| [PI_31002](/schnittstellen/202610/pruefi/INVOIC/PI_31002) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungsperiode |
| [PI_31003](/schnittstellen/202610/pruefi/INVOIC/PI_31003) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungsperiode |
| [PI_31004](/schnittstellen/202610/pruefi/INVOIC/PI_31004) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungsperiode |
| [PI_31004](/schnittstellen/202610/pruefi/INVOIC/PI_31004) | Prüfi | INVOIC | stammdaten › RECHNUNG › vorlaeufigerAbrechnungszeitraum |
| [PI_31005](/schnittstellen/202610/pruefi/INVOIC/PI_31005) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungsperiode |
| [PI_31006](/schnittstellen/202610/pruefi/INVOIC/PI_31006) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungsperiode |
| [PI_31007](/schnittstellen/202610/pruefi/INVOIC/PI_31007) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungsperiode |
| [PI_31008](/schnittstellen/202610/pruefi/INVOIC/PI_31008) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungsperiode |
| [PI_31009](/schnittstellen/202610/pruefi/INVOIC/PI_31009) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungsperiode |
| [PI_31010](/schnittstellen/202610/pruefi/INVOIC/PI_31010) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungsperiode |
| [PI_31011](/schnittstellen/202610/pruefi/INVOIC/PI_31011) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungsperiode |

### einheit

2 Verwendung(en) in den Nachrichtentypen QUOTES.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_15003](/schnittstellen/202610/pruefi/QUOTES/PI_15003) | Prüfi | QUOTES | stammdaten › ANGEBOT › bindefristAngebot |
| [PI_15003](/schnittstellen/202610/pruefi/QUOTES/PI_15003) | Prüfi | QUOTES | stammdaten › ANGEBOT › zeitspanneEinrichtungUebermittlungWerte |

### ableseZeitraum

15 Verwendung(en) in den Nachrichtentypen UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_44043](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44043) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragskonditionen › geplanteTurnusablesung |
| [PI_44060](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44060) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragskonditionen › geplanteTurnusablesung |
| [PI_44113](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44113) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragskonditionen › geplanteTurnusablesung |
| [PI_44140](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44140) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragskonditionen › geplanteTurnusablesung |
| [PI_44142](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44142) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragskonditionen › geplanteTurnusablesung |
| [PI_44168](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragskonditionen › geplanteTurnusablesung |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragskonditionen › geplanteTurnusablesung |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragskonditionen › geplanteTurnusablesung |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragskonditionen › geplanteTurnusablesung |
| [PI_55640](/schnittstellen/202610/pruefi/UTILMD/PI_55640) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragskonditionen › geplanteTurnusablesung |
| [PI_55645](/schnittstellen/202610/pruefi/UTILMD/PI_55645) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragskonditionen › geplanteTurnusablesung |
| [PI_55650](/schnittstellen/202610/pruefi/UTILMD/PI_55650) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragskonditionen › geplanteTurnusablesung |
| [PI_55655](/schnittstellen/202610/pruefi/UTILMD/PI_55655) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragskonditionen › geplanteTurnusablesung |
| [PI_55660](/schnittstellen/202610/pruefi/UTILMD/PI_55660) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragskonditionen › geplanteTurnusablesung |
| [PI_55665](/schnittstellen/202610/pruefi/UTILMD/PI_55665) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragskonditionen › geplanteTurnusablesung |

### abrechnungsZeitraum

9 Verwendung(en) in den Nachrichtentypen UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_44002](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen › netznutzungsabrechnung |
| [PI_44013](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen › netznutzungsabrechnung |
| [PI_44014](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen › netznutzungsabrechnung |
| [PI_44035](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44035) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen › netznutzungsabrechnung |
| [PI_44112](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44112) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen › netznutzungsabrechnung |
| [PI_44139](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44139) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen › netznutzungsabrechnung |
| [PI_44142](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44142) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen › netznutzungsabrechnung |
| [PI_55218](/schnittstellen/202610/pruefi/UTILMD/PI_55218) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen › netznutzungsabrechnung |
| [PI_55220](/schnittstellen/202610/pruefi/UTILMD/PI_55220) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen › netznutzungsabrechnung |

### zeitraumText

4 Verwendung(en) in den Nachrichtentypen UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_44018](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44018) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragskonditionen › kuendigungsfrist |
| [PI_44041](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44041) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragskonditionen › kuendigungsfrist |
| [PI_55018](/schnittstellen/202610/pruefi/UTILMD/PI_55018) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragskonditionen › kuendigungsfrist |
| [PI_55041](/schnittstellen/202610/pruefi/UTILMD/PI_55041) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragskonditionen › kuendigungsfrist |

### zeitraumId

141 Verwendung(en) in den Nachrichtentypen UTILMD, UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_25001](/schnittstellen/202610/pruefi/UTILTS/PI_25001) | Prüfi | UTILTS | stammdaten › BERECHNUNGSFORMEL › gueltigkeitszeitraum |
| [PI_55109](/schnittstellen/202610/pruefi/UTILMD/PI_55109) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › gueltigkeitszeitraum |
| [PI_55109](/schnittstellen/202610/pruefi/UTILMD/PI_55109) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › gueltigkeitszeitraum |
| [PI_55110](/schnittstellen/202610/pruefi/UTILMD/PI_55110) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › gueltigkeitszeitraum |
| [PI_55126](/schnittstellen/202610/pruefi/UTILMD/PI_55126) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › gueltigkeitszeitraum |
| [PI_55126](/schnittstellen/202610/pruefi/UTILMD/PI_55126) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › gueltigkeitszeitraum |
| [PI_55136](/schnittstellen/202610/pruefi/UTILMD/PI_55136) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › gueltigkeitszeitraum |
| [PI_55137](/schnittstellen/202610/pruefi/UTILMD/PI_55137) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › gueltigkeitszeitraum |
| [PI_55137](/schnittstellen/202610/pruefi/UTILMD/PI_55137) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › gueltigkeitszeitraum |
| [PI_55156](/schnittstellen/202610/pruefi/UTILMD/PI_55156) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › gueltigkeitszeitraum |
| [PI_55156](/schnittstellen/202610/pruefi/UTILMD/PI_55156) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › gueltigkeitszeitraum |
| [PI_55173](/schnittstellen/202610/pruefi/UTILMD/PI_55173) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › gueltigkeitszeitraum |
| [PI_55173](/schnittstellen/202610/pruefi/UTILMD/PI_55173) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › gueltigkeitszeitraum |
| [PI_55173](/schnittstellen/202610/pruefi/UTILMD/PI_55173) | Prüfi | UTILMD | stammdaten › MESSLOKATION › gueltigkeitszeitraum |
| [PI_55173](/schnittstellen/202610/pruefi/UTILMD/PI_55173) | Prüfi | UTILMD | stammdaten › NETZLOKATION › gueltigkeitszeitraum |
| [PI_55173](/schnittstellen/202610/pruefi/UTILMD/PI_55173) | Prüfi | UTILMD | stammdaten › STEUERBARE_RESSOURCE › gueltigkeitszeitraum |
| [PI_55173](/schnittstellen/202610/pruefi/UTILMD/PI_55173) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE › gueltigkeitszeitraum |
| [PI_55175](/schnittstellen/202610/pruefi/UTILMD/PI_55175) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › gueltigkeitszeitraum |
| [PI_55175](/schnittstellen/202610/pruefi/UTILMD/PI_55175) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › gueltigkeitszeitraum |
| [PI_55175](/schnittstellen/202610/pruefi/UTILMD/PI_55175) | Prüfi | UTILMD | stammdaten › MESSLOKATION › gueltigkeitszeitraum |
| [PI_55175](/schnittstellen/202610/pruefi/UTILMD/PI_55175) | Prüfi | UTILMD | stammdaten › NETZLOKATION › gueltigkeitszeitraum |
| [PI_55175](/schnittstellen/202610/pruefi/UTILMD/PI_55175) | Prüfi | UTILMD | stammdaten › STEUERBARE_RESSOURCE › gueltigkeitszeitraum |
| [PI_55175](/schnittstellen/202610/pruefi/UTILMD/PI_55175) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE › gueltigkeitszeitraum |
| [PI_55177](/schnittstellen/202610/pruefi/UTILMD/PI_55177) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › gueltigkeitszeitraum |
| [PI_55177](/schnittstellen/202610/pruefi/UTILMD/PI_55177) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › gueltigkeitszeitraum |
| [PI_55177](/schnittstellen/202610/pruefi/UTILMD/PI_55177) | Prüfi | UTILMD | stammdaten › MESSLOKATION › gueltigkeitszeitraum |
| [PI_55177](/schnittstellen/202610/pruefi/UTILMD/PI_55177) | Prüfi | UTILMD | stammdaten › NETZLOKATION › gueltigkeitszeitraum |
| [PI_55177](/schnittstellen/202610/pruefi/UTILMD/PI_55177) | Prüfi | UTILMD | stammdaten › STEUERBARE_RESSOURCE › gueltigkeitszeitraum |
| [PI_55177](/schnittstellen/202610/pruefi/UTILMD/PI_55177) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE › gueltigkeitszeitraum |
| [PI_55180](/schnittstellen/202610/pruefi/UTILMD/PI_55180) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › gueltigkeitszeitraum |
| [PI_55180](/schnittstellen/202610/pruefi/UTILMD/PI_55180) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › gueltigkeitszeitraum |
| [PI_55180](/schnittstellen/202610/pruefi/UTILMD/PI_55180) | Prüfi | UTILMD | stammdaten › MESSLOKATION › gueltigkeitszeitraum |
| [PI_55180](/schnittstellen/202610/pruefi/UTILMD/PI_55180) | Prüfi | UTILMD | stammdaten › NETZLOKATION › gueltigkeitszeitraum |
| [PI_55180](/schnittstellen/202610/pruefi/UTILMD/PI_55180) | Prüfi | UTILMD | stammdaten › STEUERBARE_RESSOURCE › gueltigkeitszeitraum |
| [PI_55180](/schnittstellen/202610/pruefi/UTILMD/PI_55180) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE › gueltigkeitszeitraum |
| [PI_55218](/schnittstellen/202610/pruefi/UTILMD/PI_55218) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › gueltigkeitszeitraum |
| [PI_55220](/schnittstellen/202610/pruefi/UTILMD/PI_55220) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › gueltigkeitszeitraum |
| [PI_55225](/schnittstellen/202610/pruefi/UTILMD/PI_55225) | Prüfi | UTILMD | stammdaten › NETZLOKATION › gueltigkeitszeitraum |
| [PI_55227](/schnittstellen/202610/pruefi/UTILMD/PI_55227) | Prüfi | UTILMD | stammdaten › NETZLOKATION › gueltigkeitszeitraum |
| [PI_55230](/schnittstellen/202610/pruefi/UTILMD/PI_55230) | Prüfi | UTILMD | stammdaten › NETZLOKATION › gueltigkeitszeitraum |
| [PI_55232](/schnittstellen/202610/pruefi/UTILMD/PI_55232) | Prüfi | UTILMD | stammdaten › NETZLOKATION › gueltigkeitszeitraum |
| [PI_55553](/schnittstellen/202610/pruefi/UTILMD/PI_55553) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › gueltigkeitszeitraum |
| [PI_55553](/schnittstellen/202610/pruefi/UTILMD/PI_55553) | Prüfi | UTILMD | stammdaten › ZAEHLER › gueltigkeitszeitraum |
| [PI_55555](/schnittstellen/202610/pruefi/UTILMD/PI_55555) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › gueltigkeitszeitraum |
| [PI_55555](/schnittstellen/202610/pruefi/UTILMD/PI_55555) | Prüfi | UTILMD | stammdaten › ZAEHLER › gueltigkeitszeitraum |
| [PI_55557](/schnittstellen/202610/pruefi/UTILMD/PI_55557) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › gueltigkeitszeitraum |
| [PI_55559](/schnittstellen/202610/pruefi/UTILMD/PI_55559) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › gueltigkeitszeitraum |
| [PI_55613](/schnittstellen/202610/pruefi/UTILMD/PI_55613) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › gueltigkeitszeitraum |
| [PI_55613](/schnittstellen/202610/pruefi/UTILMD/PI_55613) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › gueltigkeitszeitraum |
| [PI_55614](/schnittstellen/202610/pruefi/UTILMD/PI_55614) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › gueltigkeitszeitraum |
| [PI_55614](/schnittstellen/202610/pruefi/UTILMD/PI_55614) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › gueltigkeitszeitraum |
| [PI_55615](/schnittstellen/202610/pruefi/UTILMD/PI_55615) | Prüfi | UTILMD | stammdaten › NETZLOKATION › gueltigkeitszeitraum |
| [PI_55616](/schnittstellen/202610/pruefi/UTILMD/PI_55616) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › gueltigkeitszeitraum |
| [PI_55616](/schnittstellen/202610/pruefi/UTILMD/PI_55616) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › gueltigkeitszeitraum |
| [PI_55617](/schnittstellen/202610/pruefi/UTILMD/PI_55617) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE › gueltigkeitszeitraum |
| [PI_55618](/schnittstellen/202610/pruefi/UTILMD/PI_55618) | Prüfi | UTILMD | stammdaten › STEUERBARE_RESSOURCE › gueltigkeitszeitraum |
| [PI_55619](/schnittstellen/202610/pruefi/UTILMD/PI_55619) | Prüfi | UTILMD | stammdaten › TRANCHE › gueltigkeitszeitraum |
| [PI_55620](/schnittstellen/202610/pruefi/UTILMD/PI_55620) | Prüfi | UTILMD | stammdaten › MESSLOKATION › gueltigkeitszeitraum |
| [PI_55621](/schnittstellen/202610/pruefi/UTILMD/PI_55621) | Prüfi | UTILMD | stammdaten › NETZLOKATION › gueltigkeitszeitraum |
| [PI_55622](/schnittstellen/202610/pruefi/UTILMD/PI_55622) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › gueltigkeitszeitraum |
| [PI_55622](/schnittstellen/202610/pruefi/UTILMD/PI_55622) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › gueltigkeitszeitraum |
| [PI_55623](/schnittstellen/202610/pruefi/UTILMD/PI_55623) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE › gueltigkeitszeitraum |
| [PI_55624](/schnittstellen/202610/pruefi/UTILMD/PI_55624) | Prüfi | UTILMD | stammdaten › STEUERBARE_RESSOURCE › gueltigkeitszeitraum |
| [PI_55625](/schnittstellen/202610/pruefi/UTILMD/PI_55625) | Prüfi | UTILMD | stammdaten › TRANCHE › gueltigkeitszeitraum |
| [PI_55626](/schnittstellen/202610/pruefi/UTILMD/PI_55626) | Prüfi | UTILMD | stammdaten › MESSLOKATION › gueltigkeitszeitraum |
| [PI_55627](/schnittstellen/202610/pruefi/UTILMD/PI_55627) | Prüfi | UTILMD | stammdaten › NETZLOKATION › gueltigkeitszeitraum |
| [PI_55628](/schnittstellen/202610/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › gueltigkeitszeitraum |
| [PI_55628](/schnittstellen/202610/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › gueltigkeitszeitraum |
| [PI_55628](/schnittstellen/202610/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › gueltigkeitszeitraum |
| [PI_55629](/schnittstellen/202610/pruefi/UTILMD/PI_55629) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE › gueltigkeitszeitraum |
| [PI_55630](/schnittstellen/202610/pruefi/UTILMD/PI_55630) | Prüfi | UTILMD | stammdaten › STEUERBARE_RESSOURCE › gueltigkeitszeitraum |
| [PI_55632](/schnittstellen/202610/pruefi/UTILMD/PI_55632) | Prüfi | UTILMD | stammdaten › MESSLOKATION › gueltigkeitszeitraum |
| [PI_55633](/schnittstellen/202610/pruefi/UTILMD/PI_55633) | Prüfi | UTILMD | stammdaten › NETZLOKATION › gueltigkeitszeitraum |
| [PI_55634](/schnittstellen/202610/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › gueltigkeitszeitraum |
| [PI_55634](/schnittstellen/202610/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › gueltigkeitszeitraum |
| [PI_55634](/schnittstellen/202610/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › gueltigkeitszeitraum |
| [PI_55635](/schnittstellen/202610/pruefi/UTILMD/PI_55635) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE › gueltigkeitszeitraum |
| [PI_55636](/schnittstellen/202610/pruefi/UTILMD/PI_55636) | Prüfi | UTILMD | stammdaten › STEUERBARE_RESSOURCE › gueltigkeitszeitraum |
| [PI_55638](/schnittstellen/202610/pruefi/UTILMD/PI_55638) | Prüfi | UTILMD | stammdaten › MESSLOKATION › gueltigkeitszeitraum |
| [PI_55639](/schnittstellen/202610/pruefi/UTILMD/PI_55639) | Prüfi | UTILMD | stammdaten › NETZLOKATION › gueltigkeitszeitraum |
| [PI_55640](/schnittstellen/202610/pruefi/UTILMD/PI_55640) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › gueltigkeitszeitraum |
| [PI_55641](/schnittstellen/202610/pruefi/UTILMD/PI_55641) | Prüfi | UTILMD | stammdaten › STEUERBARE_RESSOURCE › gueltigkeitszeitraum |
| [PI_55642](/schnittstellen/202610/pruefi/UTILMD/PI_55642) | Prüfi | UTILMD | stammdaten › TRANCHE › gueltigkeitszeitraum |
| [PI_55643](/schnittstellen/202610/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | stammdaten › MESSLOKATION › gueltigkeitszeitraum |
| [PI_55643](/schnittstellen/202610/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › gueltigkeitszeitraum |
| [PI_55643](/schnittstellen/202610/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | stammdaten › ZAEHLER › gueltigkeitszeitraum |
| [PI_55644](/schnittstellen/202610/pruefi/UTILMD/PI_55644) | Prüfi | UTILMD | stammdaten › NETZLOKATION › gueltigkeitszeitraum |
| [PI_55645](/schnittstellen/202610/pruefi/UTILMD/PI_55645) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › gueltigkeitszeitraum |
| [PI_55646](/schnittstellen/202610/pruefi/UTILMD/PI_55646) | Prüfi | UTILMD | stammdaten › STEUERBARE_RESSOURCE › gueltigkeitszeitraum |
| [PI_55647](/schnittstellen/202610/pruefi/UTILMD/PI_55647) | Prüfi | UTILMD | stammdaten › TRANCHE › gueltigkeitszeitraum |
| [PI_55648](/schnittstellen/202610/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | stammdaten › MESSLOKATION › gueltigkeitszeitraum |
| [PI_55648](/schnittstellen/202610/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › gueltigkeitszeitraum |
| [PI_55648](/schnittstellen/202610/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | stammdaten › ZAEHLER › gueltigkeitszeitraum |
| [PI_55649](/schnittstellen/202610/pruefi/UTILMD/PI_55649) | Prüfi | UTILMD | stammdaten › NETZLOKATION › gueltigkeitszeitraum |
| [PI_55650](/schnittstellen/202610/pruefi/UTILMD/PI_55650) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › gueltigkeitszeitraum |
| [PI_55651](/schnittstellen/202610/pruefi/UTILMD/PI_55651) | Prüfi | UTILMD | stammdaten › STEUERBARE_RESSOURCE › gueltigkeitszeitraum |
| [PI_55652](/schnittstellen/202610/pruefi/UTILMD/PI_55652) | Prüfi | UTILMD | stammdaten › TRANCHE › gueltigkeitszeitraum |
| [PI_55653](/schnittstellen/202610/pruefi/UTILMD/PI_55653) | Prüfi | UTILMD | stammdaten › MESSLOKATION › gueltigkeitszeitraum |
| [PI_55653](/schnittstellen/202610/pruefi/UTILMD/PI_55653) | Prüfi | UTILMD | stammdaten › ZAEHLER › gueltigkeitszeitraum |
| [PI_55654](/schnittstellen/202610/pruefi/UTILMD/PI_55654) | Prüfi | UTILMD | stammdaten › NETZLOKATION › gueltigkeitszeitraum |
| [PI_55655](/schnittstellen/202610/pruefi/UTILMD/PI_55655) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › gueltigkeitszeitraum |
| [PI_55656](/schnittstellen/202610/pruefi/UTILMD/PI_55656) | Prüfi | UTILMD | stammdaten › STEUERBARE_RESSOURCE › gueltigkeitszeitraum |
| [PI_55657](/schnittstellen/202610/pruefi/UTILMD/PI_55657) | Prüfi | UTILMD | stammdaten › TRANCHE › gueltigkeitszeitraum |
| [PI_55658](/schnittstellen/202610/pruefi/UTILMD/PI_55658) | Prüfi | UTILMD | stammdaten › MESSLOKATION › gueltigkeitszeitraum |
| [PI_55658](/schnittstellen/202610/pruefi/UTILMD/PI_55658) | Prüfi | UTILMD | stammdaten › ZAEHLER › gueltigkeitszeitraum |
| [PI_55659](/schnittstellen/202610/pruefi/UTILMD/PI_55659) | Prüfi | UTILMD | stammdaten › NETZLOKATION › gueltigkeitszeitraum |
| [PI_55660](/schnittstellen/202610/pruefi/UTILMD/PI_55660) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › gueltigkeitszeitraum |
| [PI_55661](/schnittstellen/202610/pruefi/UTILMD/PI_55661) | Prüfi | UTILMD | stammdaten › STEUERBARE_RESSOURCE › gueltigkeitszeitraum |
| [PI_55662](/schnittstellen/202610/pruefi/UTILMD/PI_55662) | Prüfi | UTILMD | stammdaten › TRANCHE › gueltigkeitszeitraum |
| [PI_55663](/schnittstellen/202610/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | stammdaten › MESSLOKATION › gueltigkeitszeitraum |
| [PI_55663](/schnittstellen/202610/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › gueltigkeitszeitraum |
| [PI_55663](/schnittstellen/202610/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | stammdaten › ZAEHLER › gueltigkeitszeitraum |
| [PI_55664](/schnittstellen/202610/pruefi/UTILMD/PI_55664) | Prüfi | UTILMD | stammdaten › NETZLOKATION › gueltigkeitszeitraum |
| [PI_55665](/schnittstellen/202610/pruefi/UTILMD/PI_55665) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › gueltigkeitszeitraum |
| [PI_55666](/schnittstellen/202610/pruefi/UTILMD/PI_55666) | Prüfi | UTILMD | stammdaten › STEUERBARE_RESSOURCE › gueltigkeitszeitraum |
| [PI_55667](/schnittstellen/202610/pruefi/UTILMD/PI_55667) | Prüfi | UTILMD | stammdaten › TRANCHE › gueltigkeitszeitraum |
| [PI_55669](/schnittstellen/202610/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | stammdaten › MESSLOKATION › gueltigkeitszeitraum |
| [PI_55669](/schnittstellen/202610/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › gueltigkeitszeitraum |
| [PI_55669](/schnittstellen/202610/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | stammdaten › ZAEHLER › gueltigkeitszeitraum |
| [PI_55670](/schnittstellen/202610/pruefi/UTILMD/PI_55670) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › gueltigkeitszeitraum |
| [PI_55670](/schnittstellen/202610/pruefi/UTILMD/PI_55670) | Prüfi | UTILMD | stammdaten › TRANCHE › gueltigkeitszeitraum |
| [PI_55672](/schnittstellen/202610/pruefi/UTILMD/PI_55672) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › gueltigkeitszeitraum |
| [PI_55672](/schnittstellen/202610/pruefi/UTILMD/PI_55672) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › gueltigkeitszeitraum |
| [PI_55672](/schnittstellen/202610/pruefi/UTILMD/PI_55672) | Prüfi | UTILMD | stammdaten › TRANCHE › gueltigkeitszeitraum |
| [PI_55673](/schnittstellen/202610/pruefi/UTILMD/PI_55673) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › gueltigkeitszeitraum |
| [PI_55673](/schnittstellen/202610/pruefi/UTILMD/PI_55673) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › gueltigkeitszeitraum |
| [PI_55673](/schnittstellen/202610/pruefi/UTILMD/PI_55673) | Prüfi | UTILMD | stammdaten › TRANCHE › gueltigkeitszeitraum |
| [PI_55674](/schnittstellen/202610/pruefi/UTILMD/PI_55674) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › gueltigkeitszeitraum |
| [PI_55674](/schnittstellen/202610/pruefi/UTILMD/PI_55674) | Prüfi | UTILMD | stammdaten › TRANCHE › gueltigkeitszeitraum |
| [PI_55684](/schnittstellen/202610/pruefi/UTILMD/PI_55684) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › gueltigkeitszeitraum |
| [PI_55686](/schnittstellen/202610/pruefi/UTILMD/PI_55686) | Prüfi | UTILMD | stammdaten › TRANCHE › gueltigkeitszeitraum |
| [PI_55688](/schnittstellen/202610/pruefi/UTILMD/PI_55688) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › gueltigkeitszeitraum |
| [PI_55690](/schnittstellen/202610/pruefi/UTILMD/PI_55690) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL › gueltigkeitszeitraum |
| [PI_55690](/schnittstellen/202610/pruefi/UTILMD/PI_55690) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › gueltigkeitszeitraum |
| [PI_55690](/schnittstellen/202610/pruefi/UTILMD/PI_55690) | Prüfi | UTILMD | stammdaten › MESSLOKATION › gueltigkeitszeitraum |
| [PI_55690](/schnittstellen/202610/pruefi/UTILMD/PI_55690) | Prüfi | UTILMD | stammdaten › NETZLOKATION › gueltigkeitszeitraum |
| [PI_55690](/schnittstellen/202610/pruefi/UTILMD/PI_55690) | Prüfi | UTILMD | stammdaten › STEUERBARE_RESSOURCE › gueltigkeitszeitraum |
| [PI_55690](/schnittstellen/202610/pruefi/UTILMD/PI_55690) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE › gueltigkeitszeitraum |
| [PI_55690](/schnittstellen/202610/pruefi/UTILMD/PI_55690) | Prüfi | UTILMD | stammdaten › TRANCHE › gueltigkeitszeitraum |
| [PI_55693](/schnittstellen/202610/pruefi/UTILMD/PI_55693) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE › gueltigkeitszeitraum |
| [PI_55694](/schnittstellen/202610/pruefi/UTILMD/PI_55694) | Prüfi | UTILMD | stammdaten › TECHNISCHE_RESSOURCE › gueltigkeitszeitraum |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
