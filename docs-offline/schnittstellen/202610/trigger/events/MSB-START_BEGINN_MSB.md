# [MSB] START_BEGINN_MSB
<span hidden data-pagefind-meta={"title:Trigger-Ereignis START_BEGINN_MSB — Marktrolle MSB (FV 202610)"} />

Marktrolle **MSB** · Formatversion **202610** · BO4E-Schema **1.7.8**

## Stammdaten

Unter diesem Topic ist genau einer der folgenden 2 Prüfidentifikatoren zulässig — welcher, entscheidet der Event-Prozess.

| Prüfi | Scope | Anwendungsfall | Festlegung | Kommunikation |
|---|---|---|---|---|
| [PI_44042](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44042) | UTILMD_GAS | Anmeldung MSB | AWH WiM Gas 2.0 | MSBN → NB |
| [PI_55042](/schnittstellen/202610/pruefi/UTILMD/PI_55042) | UTILMD | Anmeldung MSB | WiM Strom Teil 1 | MSBN → NB |

Die Stammdaten der 2 Prüfidentifikatoren in **einer** Struktur — eine Spalte je Prüfidentifikator, wie im Anwendungshandbuch. Ein Wert in der Spalte heißt, dass das Feld zu diesem Prüfidentifikator gehört: **Muss**, wenn seine Spezifikation es verlangt, sonst **Kann**. Eine leere Zelle heißt »gehört nicht dazu«, nicht »unbekannt«. Vorausgewählt ist der erste; die übrigen schaltet die Leiste über der Tabelle zu.

<Handbuchsatz>

<div className="maco-tabellenrahmen">

| Struktur (BO4E) | Beschreibung | Format | <span className="hbs-p" title="Anmeldung MSB">44042</span> | <span className="hbs-p" title="Anmeldung MSB">55042</span> | Bedingung |
|---|---|---|---|---|---|
| <span className="hbs-g hbs-e0">**stammdaten**</span> | — | object | Kann | Kann | — |
| <span className="hbs-g hbs-e1">**MESSLOKATION** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | Muss | — |
| <span className="hbs-f hbs-e2">[messlokationsId](/bo4e/202610/bo/Messlokation#messlokationsid)</span><span className="hbs-nr">00010</span> | Die Messlokations-Identifikation. Das ist die frühere Zählpunktbezeichnung,<br/>z.B. DE 47108151234567 | string | Kann | Kann | — |
| <span className="hbs-g hbs-e2">**ablesekartenempfaenger** <span className="hbs-pflicht">\*</span></span> | — | object | Muss | Muss | — |
| <span className="hbs-f hbs-e3">[anrede](/bo4e/202610/bo/Geschaeftspartner#anrede)</span><span className="hbs-nr">00020</span> | Die Anrede für den GePa, Z.B. Herr. | string | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[gewerbekennzeichnung](/bo4e/202610/bo/Geschaeftspartner#gewerbekennzeichnung)</span><span className="hbs-nr">00030</span> | Kennzeichnung ob es sich um einen Gewerbe/Unternehmen (gewerbeKennzeichnung = true)<br/>oder eine Privatperson handelt. (gewerbeKennzeichnung = false) | boolean | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[name1](/bo4e/202610/bo/Geschaeftspartner#name1) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00040</span> | Erster Teil des Namens. Hier kann der Firmenname oder bei Privatpersonen<br/>beispielsweise der Nachname dargestellt werden. Beispiele: Yellow Strom GmbH<br/>oder Hagen | string | Muss | Muss | — |
| <span className="hbs-f hbs-e3">[name2](/bo4e/202610/bo/Geschaeftspartner#name2)</span><span className="hbs-nr">00050</span> | Zweiter Teil des Namens. Hier kann der eine Erweiterung zum Firmennamen oder<br/>bei Privatpersonen beispielsweise der Vorname dargestellt werden. Beispiele:<br/>Bereich Süd oder Nina | string | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[name3](/bo4e/202610/bo/Geschaeftspartner#name3)</span><span className="hbs-nr">00060</span> | Dritter Teil des Namens. Hier können weitere Ergänzungen zum Firmennamen oder<br/>bei Privatpersonen Zusätze zum Namen dargestellt werden. Beispiele: und Afrika<br/>oder Sängerin | string | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[name4](/bo4e/202610/bo/Geschaeftspartner#name4)</span><span className="hbs-nr">00070</span> | name4 | string | Kann | Kann | — |
| <span className="hbs-g hbs-e3">**partneradresse**</span> | — | object | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[hausnummer](/bo4e/202610/com/Adresse#hausnummer)</span><span className="hbs-nr">00080</span> | Hausnummer und Ergänzung | string | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[landescode](/bo4e/202610/com/Adresse#landescode)</span><span className="hbs-nr">00090</span> | Landescode | [Enum Landescode](/bo4e/202610/enum/Landescode) | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`AC`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`AD`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`AE`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`AF`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`AG`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`AI`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`AL`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`AM`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`AN`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`AO`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`AQ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`AR`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`AS`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`AT`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`AU`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`AW`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`AX`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`AZ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BA`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BB`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BD`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BE`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BF`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BG`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BH`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BI`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BJ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BL`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BM`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BN`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BO`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BQ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BR`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BS`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BT`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BU`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BV`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BW`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BY`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BZ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CA`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CC`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CD`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CF`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CG`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CH`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CI`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CK`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CL`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CM`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CN`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CO`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CP`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CR`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CS`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CU`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CV`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CW`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CX`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CY`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CZ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`DE`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`DG`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`DJ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`DK`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`DM`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`DO`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`DZ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`EA`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`EC`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`EE`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`EG`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`EH`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`ER`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`ES`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`ET`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`EU`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`FI`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`FJ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`FK`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`FM`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`FO`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`FR`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`FX`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GA`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GB`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GD`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GE`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GF`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GG`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GH`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GI`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GL`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GM`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GN`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GP`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GQ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GR`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GS`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GT`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GU`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GW`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GY`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`HK`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`HM`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`HN`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`HR`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`HT`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`HU`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`IC`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`ID`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`IE`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`IL`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`IM`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`IN`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`IO`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`IQ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`IR`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`IS`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`IT`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`JE`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`JM`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`JO`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`JP`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`KE`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`KG`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`KH`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`KI`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`KM`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`KN`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`KP`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`KR`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`KW`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`KY`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`KZ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`LA`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`LB`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`LC`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`LI`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`LK`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`LR`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`LS`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`LT`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`LU`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`LV`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`LY`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MA`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MC`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MD`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`ME`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MF`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MG`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MH`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MK`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`ML`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MM`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MN`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MO`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MP`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MQ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MR`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MS`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MT`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MU`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MV`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MW`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MX`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MY`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MZ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`NA`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`NC`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`NE`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`NF`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`NG`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`NI`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`NL`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`NO`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`NP`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`NR`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`NT`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`NU`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`NZ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`OM`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`PA`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`PE`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`PF`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`PG`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`PH`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`PK`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`PL`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`PM`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`PN`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`PR`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`PS`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`PT`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`PW`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`PY`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`QA`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`RE`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`RO`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`RS`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`RU`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`RW`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SA`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SB`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SC`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SD`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SE`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SF`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SG`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SH`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SI`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SJ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SK`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SL`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SM`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SN`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SO`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SR`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SS`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`ST`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SU`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SV`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SX`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SY`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SZ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`TA`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`TC`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`TD`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`TF`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`TG`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`TJ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`TK`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`TL`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`TM`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`TN`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`TO`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`TP`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`TR`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`TT`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`TV`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`TW`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`TZ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`UA`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`UG`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`UK`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`UM`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`US`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`UY`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`UZ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`VA`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`VC`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`VE`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`VG`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`VI`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`VN`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`VU`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`WF`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`WS`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`XK`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`YE`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`YT`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`YU`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`ZA`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`ZM`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`ZR`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`ZW`</span> | — | — | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[ort](/bo4e/202610/com/Adresse#ort)</span><span className="hbs-nr">00100</span> | Ort | string | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[ortsteil](/bo4e/202610/com/Adresse#ortsteil)</span><span className="hbs-nr">00110</span> | Ortsteil | string | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[postfach](/bo4e/202610/com/Adresse#postfach)</span><span className="hbs-nr">00120</span> | Postfach | string | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[postleitzahl](/bo4e/202610/com/Adresse#postleitzahl)</span><span className="hbs-nr">00130</span> | Postleitzahl | string | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[strasse](/bo4e/202610/com/Adresse#strasse)</span><span className="hbs-nr">00140</span> | Strasse | string | Kann | Kann | — |
| <span className="hbs-g hbs-e2">**messadresse**</span> | — | object | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[hausnummer](/bo4e/202610/com/Adresse#hausnummer)</span><span className="hbs-nr">00150</span> | Hausnummer und Ergänzung | string | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[landescode](/bo4e/202610/com/Adresse#landescode)</span><span className="hbs-nr">00160</span> | Landescode | [Enum Landescode](/bo4e/202610/enum/Landescode) | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`AC`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`AD`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`AE`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`AF`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`AG`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`AI`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`AL`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`AM`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`AN`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`AO`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`AQ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`AR`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`AS`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`AT`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`AU`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`AW`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`AX`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`AZ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`BA`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`BB`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`BD`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`BE`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`BF`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`BG`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`BH`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`BI`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`BJ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`BL`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`BM`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`BN`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`BO`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`BQ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`BR`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`BS`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`BT`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`BU`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`BV`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`BW`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`BY`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`BZ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`CA`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`CC`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`CD`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`CF`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`CG`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`CH`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`CI`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`CK`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`CL`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`CM`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`CN`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`CO`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`CP`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`CR`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`CS`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`CU`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`CV`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`CW`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`CX`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`CY`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`CZ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`DE`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`DG`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`DJ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`DK`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`DM`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`DO`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`DZ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`EA`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`EC`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`EE`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`EG`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`EH`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`ER`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`ES`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`ET`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`EU`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`FI`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`FJ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`FK`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`FM`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`FO`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`FR`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`FX`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`GA`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`GB`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`GD`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`GE`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`GF`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`GG`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`GH`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`GI`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`GL`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`GM`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`GN`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`GP`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`GQ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`GR`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`GS`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`GT`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`GU`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`GW`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`GY`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`HK`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`HM`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`HN`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`HR`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`HT`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`HU`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`IC`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`ID`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`IE`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`IL`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`IM`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`IN`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`IO`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`IQ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`IR`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`IS`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`IT`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`JE`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`JM`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`JO`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`JP`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`KE`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`KG`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`KH`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`KI`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`KM`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`KN`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`KP`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`KR`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`KW`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`KY`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`KZ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`LA`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`LB`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`LC`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`LI`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`LK`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`LR`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`LS`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`LT`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`LU`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`LV`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`LY`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`MA`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`MC`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`MD`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`ME`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`MF`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`MG`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`MH`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`MK`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`ML`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`MM`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`MN`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`MO`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`MP`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`MQ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`MR`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`MS`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`MT`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`MU`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`MV`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`MW`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`MX`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`MY`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`MZ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`NA`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`NC`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`NE`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`NF`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`NG`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`NI`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`NL`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`NO`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`NP`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`NR`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`NT`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`NU`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`NZ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`OM`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`PA`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`PE`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`PF`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`PG`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`PH`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`PK`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`PL`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`PM`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`PN`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`PR`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`PS`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`PT`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`PW`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`PY`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`QA`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`RE`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`RO`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`RS`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`RU`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`RW`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`SA`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`SB`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`SC`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`SD`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`SE`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`SF`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`SG`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`SH`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`SI`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`SJ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`SK`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`SL`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`SM`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`SN`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`SO`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`SR`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`SS`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`ST`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`SU`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`SV`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`SX`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`SY`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`SZ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`TA`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`TC`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`TD`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`TF`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`TG`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`TJ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`TK`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`TL`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`TM`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`TN`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`TO`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`TP`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`TR`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`TT`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`TV`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`TW`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`TZ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`UA`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`UG`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`UK`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`UM`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`US`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`UY`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`UZ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`VA`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`VC`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`VE`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`VG`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`VI`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`VN`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`VU`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`WF`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`WS`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`XK`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`YE`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`YT`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`YU`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`ZA`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`ZM`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`ZR`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`ZW`</span> | — | — | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[ort](/bo4e/202610/com/Adresse#ort)</span><span className="hbs-nr">00170</span> | Ort | string | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[ortsteil](/bo4e/202610/com/Adresse#ortsteil)</span><span className="hbs-nr">00180</span> | Ortsteil | string | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[postfach](/bo4e/202610/com/Adresse#postfach)</span><span className="hbs-nr">00190</span> | Postfach | string | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[postleitzahl](/bo4e/202610/com/Adresse#postleitzahl)</span><span className="hbs-nr">00200</span> | Postleitzahl | string | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[strasse](/bo4e/202610/com/Adresse#strasse)</span><span className="hbs-nr">00210</span> | Strasse | string | Kann | Kann | — |
| <span className="hbs-g hbs-e3">**zusatzInformation**</span> | — | object | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[zusatz1](/bo4e/202610/com/AdresszusatzInformation#zusatz1)</span><span className="hbs-nr">00220</span> | Adresszusatz 1 | string | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[zusatz2](/bo4e/202610/com/AdresszusatzInformation#zusatz2)</span><span className="hbs-nr">00230</span> | Adresszusatz 2 | string | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[zusatz3](/bo4e/202610/com/AdresszusatzInformation#zusatz3)</span><span className="hbs-nr">00240</span> | Adresszusatz 3 | string | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[zusatz4](/bo4e/202610/com/AdresszusatzInformation#zusatz4)</span><span className="hbs-nr">00250</span> | Adresszusatz 4 | string | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[zusatz5](/bo4e/202610/com/AdresszusatzInformation#zusatz5)</span><span className="hbs-nr">00260</span> | Adresszusatz 5 | string | Kann | Kann | — |
| <span className="hbs-f hbs-e2">[datenqualitaet](/bo4e/202610/bo/Messlokation#datenqualitaet)</span><span className="hbs-nr">00270</span> | Datenqualitaet | [Enum Datenqualitaet](/bo4e/202610/enum/Datenqualitaet) | — | Kann | — |
| <span className="hbs-w hbs-e3">`ERWARTETE_DATEN`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`INFORMATIVE_DATEN`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`GUELTIGE_DATEN`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_KEINE_DATEN_VORHANDEN`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN_ERWARTET`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_DATEN`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_ERWARTETE_DATEN`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | Kann | — |
| <span className="hbs-g hbs-e1">**MESSSTELLENBETRIEBSVERTRAG** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | Muss | — |
| <span className="hbs-g hbs-e2">**korrespondenzpartner** <span className="hbs-pflicht">\*</span></span> | — | object | Muss | Muss | — |
| <span className="hbs-f hbs-e3">[anrede](/bo4e/202610/bo/Geschaeftspartner#anrede)</span><span className="hbs-nr">00280</span> | Die Anrede für den GePa, Z.B. Herr. | string | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[gewerbekennzeichnung](/bo4e/202610/bo/Geschaeftspartner#gewerbekennzeichnung)</span><span className="hbs-nr">00290</span> | Kennzeichnung ob es sich um einen Gewerbe/Unternehmen (gewerbeKennzeichnung = true)<br/>oder eine Privatperson handelt. (gewerbeKennzeichnung = false) | boolean | Kann | — | — |
| <span className="hbs-f hbs-e3">[name1](/bo4e/202610/bo/Geschaeftspartner#name1) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00300</span> | Erster Teil des Namens. Hier kann der Firmenname oder bei Privatpersonen<br/>beispielsweise der Nachname dargestellt werden. Beispiele: Yellow Strom GmbH<br/>oder Hagen | string | Muss | Muss | — |
| <span className="hbs-f hbs-e3">[name2](/bo4e/202610/bo/Geschaeftspartner#name2)</span><span className="hbs-nr">00310</span> | Zweiter Teil des Namens. Hier kann der eine Erweiterung zum Firmennamen oder<br/>bei Privatpersonen beispielsweise der Vorname dargestellt werden. Beispiele:<br/>Bereich Süd oder Nina | string | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[name3](/bo4e/202610/bo/Geschaeftspartner#name3)</span><span className="hbs-nr">00320</span> | Dritter Teil des Namens. Hier können weitere Ergänzungen zum Firmennamen oder<br/>bei Privatpersonen Zusätze zum Namen dargestellt werden. Beispiele: und Afrika<br/>oder Sängerin | string | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[name4](/bo4e/202610/bo/Geschaeftspartner#name4)</span><span className="hbs-nr">00330</span> | name4 | string | Kann | Kann | — |
| <span className="hbs-g hbs-e3">**partneradresse**</span> | — | object | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[hausnummer](/bo4e/202610/com/Adresse#hausnummer)</span><span className="hbs-nr">00340</span> | Hausnummer und Ergänzung | string | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[landescode](/bo4e/202610/com/Adresse#landescode)</span><span className="hbs-nr">00350</span> | Landescode | [Enum Landescode](/bo4e/202610/enum/Landescode) | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`AC`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`AD`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`AE`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`AF`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`AG`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`AI`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`AL`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`AM`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`AN`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`AO`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`AQ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`AR`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`AS`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`AT`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`AU`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`AW`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`AX`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`AZ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BA`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BB`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BD`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BE`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BF`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BG`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BH`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BI`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BJ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BL`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BM`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BN`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BO`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BQ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BR`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BS`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BT`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BU`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BV`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BW`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BY`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BZ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CA`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CC`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CD`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CF`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CG`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CH`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CI`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CK`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CL`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CM`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CN`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CO`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CP`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CR`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CS`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CU`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CV`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CW`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CX`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CY`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CZ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`DE`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`DG`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`DJ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`DK`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`DM`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`DO`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`DZ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`EA`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`EC`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`EE`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`EG`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`EH`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`ER`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`ES`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`ET`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`EU`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`FI`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`FJ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`FK`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`FM`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`FO`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`FR`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`FX`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GA`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GB`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GD`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GE`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GF`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GG`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GH`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GI`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GL`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GM`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GN`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GP`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GQ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GR`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GS`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GT`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GU`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GW`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GY`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`HK`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`HM`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`HN`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`HR`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`HT`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`HU`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`IC`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`ID`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`IE`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`IL`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`IM`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`IN`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`IO`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`IQ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`IR`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`IS`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`IT`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`JE`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`JM`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`JO`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`JP`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`KE`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`KG`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`KH`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`KI`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`KM`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`KN`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`KP`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`KR`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`KW`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`KY`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`KZ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`LA`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`LB`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`LC`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`LI`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`LK`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`LR`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`LS`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`LT`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`LU`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`LV`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`LY`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MA`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MC`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MD`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`ME`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MF`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MG`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MH`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MK`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`ML`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MM`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MN`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MO`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MP`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MQ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MR`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MS`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MT`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MU`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MV`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MW`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MX`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MY`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MZ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`NA`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`NC`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`NE`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`NF`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`NG`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`NI`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`NL`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`NO`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`NP`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`NR`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`NT`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`NU`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`NZ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`OM`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`PA`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`PE`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`PF`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`PG`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`PH`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`PK`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`PL`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`PM`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`PN`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`PR`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`PS`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`PT`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`PW`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`PY`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`QA`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`RE`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`RO`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`RS`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`RU`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`RW`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SA`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SB`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SC`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SD`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SE`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SF`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SG`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SH`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SI`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SJ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SK`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SL`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SM`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SN`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SO`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SR`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SS`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`ST`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SU`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SV`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SX`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SY`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SZ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`TA`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`TC`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`TD`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`TF`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`TG`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`TJ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`TK`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`TL`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`TM`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`TN`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`TO`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`TP`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`TR`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`TT`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`TV`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`TW`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`TZ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`UA`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`UG`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`UK`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`UM`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`US`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`UY`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`UZ`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`VA`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`VC`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`VE`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`VG`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`VI`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`VN`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`VU`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`WF`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`WS`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`XK`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`YE`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`YT`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`YU`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`ZA`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`ZM`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`ZR`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`ZW`</span> | — | — | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[ort](/bo4e/202610/com/Adresse#ort)</span><span className="hbs-nr">00360</span> | Ort | string | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[ortsteil](/bo4e/202610/com/Adresse#ortsteil)</span><span className="hbs-nr">00370</span> | Ortsteil | string | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[postfach](/bo4e/202610/com/Adresse#postfach)</span><span className="hbs-nr">00380</span> | Postfach | string | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[postleitzahl](/bo4e/202610/com/Adresse#postleitzahl)</span><span className="hbs-nr">00390</span> | Postleitzahl | string | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[strasse](/bo4e/202610/com/Adresse#strasse)</span><span className="hbs-nr">00400</span> | Strasse | string | Kann | Kann | — |
| <span className="hbs-g hbs-e3">**ansprechpartner**</span> | — | object | — | Kann | — |
| <span className="hbs-f hbs-e4">[eMailAdresse](/bo4e/202610/bo/Ansprechpartner#emailadresse)</span><span className="hbs-nr">00410</span> | E-Mail Adresse | string | — | Kann | — |
| <span className="hbs-g hbs-e4">**rufnummern** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | Kann | — |
| <span className="hbs-f hbs-e5">[nummerntyp](/bo4e/202610/com/Rufnummer#nummerntyp)</span><span className="hbs-nr">00420</span> | Rufnummernart | [Enum Rufnummernart](/bo4e/202610/enum/Rufnummernart) | — | Kann | — |
| <span className="hbs-w hbs-e5">`RUF_ZENTRALE`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`FAX_ZENTRALE`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`SAMMELRUF`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`SAMMELFAX`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`ABTEILUNGRUF`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`ABTEILUNGFAX`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`RUF_DURCHWAHL`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`FAX_DURCHWAHL`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MOBIL_NUMMER`</span> | — | — | — | Kann | — |
| <span className="hbs-f hbs-e5">[rufnummer](/bo4e/202610/com/Rufnummer#rufnummer)</span><span className="hbs-nr">00430</span> | rufnummer | string | — | Kann | — |
| <span className="hbs-g hbs-e2">**vertragskonditionen**</span> | — | object | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[beauftragungMsb](/bo4e/202610/com/Vertragskonditionen#beauftragungmsb)</span><span className="hbs-nr">00440</span> | BeauftragungMsb | [Enum BeauftragungMsb](/bo4e/202610/enum/BeauftragungMsb) | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`VERTRAG_AN_MSB`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`VERTRAGSBEENDIGUNG_MSB`</span> | — | — | Kann | Kann | — |
| <span className="hbs-g hbs-e2">**vertragspartner2** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | Muss | — |
| <span className="hbs-f hbs-e3">[anrede](/bo4e/202610/bo/Geschaeftspartner#anrede)</span><span className="hbs-nr">00450</span> | Die Anrede für den GePa, Z.B. Herr. | string | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[gewerbekennzeichnung](/bo4e/202610/bo/Geschaeftspartner#gewerbekennzeichnung)</span><span className="hbs-nr">00460</span> | Kennzeichnung ob es sich um einen Gewerbe/Unternehmen (gewerbeKennzeichnung = true)<br/>oder eine Privatperson handelt. (gewerbeKennzeichnung = false) | boolean | Kann | — | — |
| <span className="hbs-f hbs-e3">[name1](/bo4e/202610/bo/Geschaeftspartner#name1) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00470</span> | Erster Teil des Namens. Hier kann der Firmenname oder bei Privatpersonen<br/>beispielsweise der Nachname dargestellt werden. Beispiele: Yellow Strom GmbH<br/>oder Hagen | string | Muss | Muss | — |
| <span className="hbs-f hbs-e3">[name2](/bo4e/202610/bo/Geschaeftspartner#name2)</span><span className="hbs-nr">00480</span> | Zweiter Teil des Namens. Hier kann der eine Erweiterung zum Firmennamen oder<br/>bei Privatpersonen beispielsweise der Vorname dargestellt werden. Beispiele:<br/>Bereich Süd oder Nina | string | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[name3](/bo4e/202610/bo/Geschaeftspartner#name3)</span><span className="hbs-nr">00490</span> | Dritter Teil des Namens. Hier können weitere Ergänzungen zum Firmennamen oder<br/>bei Privatpersonen Zusätze zum Namen dargestellt werden. Beispiele: und Afrika<br/>oder Sängerin | string | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[name4](/bo4e/202610/bo/Geschaeftspartner#name4)</span><span className="hbs-nr">00500</span> | name4 | string | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[geschaeftspartnerrolle](/bo4e/202610/bo/Geschaeftspartner#geschaeftspartnerrolle)</span><span className="hbs-nr">00510</span> | Rolle, die der Geschäftspartner hat (z.B. Interessent, Kunde). | array | — | Kann | — |
| <span className="hbs-g hbs-e1">**ZAEHLER** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | Kann | — |
| <span className="hbs-f hbs-e2">[zaehlernummer](/bo4e/202610/bo/Zaehler#zaehlernummer)</span><span className="hbs-nr">00520</span> | Nummerierung des Zählers, vergeben durch den Messstellenbetreiber | string | Kann | Kann | — |
| <span className="hbs-g hbs-e1">**MARKTLOKATION** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | Kann | — |
| <span className="hbs-f hbs-e2">[marktlokationsId](/bo4e/202610/bo/Marktlokation#marktlokationsid)</span><span className="hbs-nr">00530</span> | Identifikationsnummer einer Marktlokation, an der Energie entweder<br/>verbraucht, oder erzeugt wird | string | — | Kann | — |

</div>

</Handbuchsatz>

## Kette dieses Auslösers

Das Ereignis löst die Nachricht aus. Der Marktpartner antwortet mit einer der genannten Antworten, und danach schreibt die MACO APP den Vorgang in Ihr Backendsystem.

| Nachricht | Antworten | Schreibaufruf nach der Antwort |
|---|---|---|
| [44042](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44042) | [44043](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44043), [44044](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44044) | `POST /updateProcessData` |
| [55042](/schnittstellen/202610/pruefi/UTILMD/PI_55042) | [55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043), [55044](/schnittstellen/202610/pruefi/UTILMD/PI_55044) | `POST /updateProcessData` |

Dieses Ereignis löst Schritte in diesen Rollensichten aus:

| Prozess | Beteiligter | Regelwerk | Sparte |
|---|---|---|---|
| [Beginn Messstellenbetrieb](/prozessdoku/202610/MSB--MSBN/awh-wim-gas-2-0-beginn-messstellenbetrieb) | MSBN | AWH WiM Gas 2.0 | Gas |
| [Beginn Messstellenbetrieb](/prozessdoku/202610/MSB--MSBN/WiM-Teil1-beginn-messstellenbetrieb) | MSBN | WiM Strom Teil 1 | Strom |

## Transaktionsdaten

Der Umschlag der Nachricht. Pflichtfelder müssen beim Trigger-Aufruf gesetzt sein.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| [datumleistungsbeginn](/bo4e/202610/cdoc/Transaktionsdaten#datumleistungsbeginn) | string (date-time) | **ja** | Datum zum geplanten Leistungsbeginn / DTM+76 |
| [kategorie](/bo4e/202610/cdoc/Transaktionsdaten#kategorie) | string | **ja** | Qualifier aus dem Beginn der EDIFact Nachricht / BGM |
| [sparte](/bo4e/202610/cdoc/Transaktionsdaten#sparte) | [Enum Sparte](/bo4e/202610/enum/Sparte) | **ja** | Enthält Informationen über die Sparte Werte: `STROM`, `GAS`, `FERNWAERME`, `NAHWAERME`, `WASSER`, `ABWASSER` |
| [transaktionsgrund](/bo4e/202610/cdoc/Transaktionsdaten#transaktionsgrund) | string | **ja** | Der Transaktionsgrund beschreibt den Geschäftsvorfall zur Kategorie genauer / UTILMD STS+7++###+ZW4+E03 |
| `pruefidentifikator` | — | nein | Wird dynamisch im Event-Prozess ermittelt (Entscheidungsgrundlage: sparte). Ein vom Sender mitgegebener Wert wird ignoriert. Im Topic mögliche Prüfis — 44042, 55042. Mögliche Werte: `44042`, `55042` |
| [absender › marktrolle](/bo4e/202610/bo/Marktteilnehmer#marktrolle) | [Enum Marktrolle](/bo4e/202610/enum/Marktrolle) | nein | Gibt im Klartext die Bezeichnung der Marktrolle an. Werte: `NB`, `LF`, `MSB`, `MSBA`, `GMSB`, `MDL`, `DL`, `BKV`, `UENB`, `KUNDE-SELBST-NN` … (+9) |
| [absender › rollencodenummer](/bo4e/202610/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |
| [empfaenger › marktrolle](/bo4e/202610/bo/Marktteilnehmer#marktrolle) | [Enum Marktrolle](/bo4e/202610/enum/Marktrolle) | nein | Gibt im Klartext die Bezeichnung der Marktrolle an. Werte: `NB`, `LF`, `MSB`, `MSBA`, `GMSB`, `MDL`, `DL`, `BKV`, `UENB`, `KUNDE-SELBST-NN` … (+9) |
| [empfaenger › rollencodenummer](/bo4e/202610/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |

## Zusatzdaten

`eventname` ist auf **START_BEGINN_MSB** festgelegt. Dieser Wert bleibt auch in der englischen Fassung deutsch, weil Camunda darüber korreliert.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `prozessId` | string | **ja** | — |
| `eventname` | const `START_BEGINN_MSB` | **ja** | — |

## Antwort

**Der Auslöser vergibt einen eigenen `businessKey`.** Die MACO APP übernimmt **weder** den `businessKey` **noch** die `prozessId` des aufrufenden Systems als Kennung der Prozessinstanz. Der `businessKey` der Antwort entsteht beim Start des Prozesses und ist neu. Der Rumpf dieses Aufrufs führt kein Feld `businessKey`; es gibt also keine Stelle, an der ein eigener Schlüssel mitgegeben werden könnte. Die mitgegebene `prozessId` (Pflichtfeld dieses Aufrufs) bleibt die Belegnummer des Backends: sie kommt in `zusatzdaten.prozessId` der Callbacks zurück — dort Pflicht nur bei MaloIdent (03002/03003), sonst optional.

**201 — Erfolg.** Erfolgsmeldung auf Prozessdaten API Aufruf.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `businessKey` | string (uuid) | **ja** | Einzigartige Kennung des Geschäftsprozesses |
| `message` | string | **ja** | Nachricht mit Details zum ausgelösten Event — Beispiel der Quelle: `received event XXXXXXXXXXXX with id at 2024-08-08T12:58:22Z and started process with businessKey 4c7170ed-3518-41ee-8582-39ab65b00107` |

**400 — Fehler.** Fehlermeldung auf Prozessdaten API Aufruf.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `errorCode` | string | nein | Error identifier — Beispiel der Quelle: `400` |
| `message` | string | nein | Technische Meldung — Beispiel der Quelle: `Validation Failed` |

Die Antwortschemata (`event_responses_success`, `event_response_fail`) stammen aus `macoapp-trigger.json`, Fassung 1.2.5 (20. Januar 2025), außerhalb der Zeitscheibe: die Datei wird nicht je Formatversion geführt, beide Fassungen lesen dieselbe.

Welchen Rumpf die Callbacks `updateProcessData` und `createProcessData` senden, ist am NiFi-Fluss der MACO APP gemessen: `{stammdaten, transaktionsdaten, zusatzdaten}` ohne Umschlag, der `businessKey` innerhalb von `zusatzdaten`. Nicht gemessen ist das an einem mitgeschnittenen Aufruf, und nicht für MaloIdent (03002/03003).

Was `businessKey`, `prozessId` und `targetBusinessKey` unterscheidet, steht auf [Schlüssel und Zuordnung](/schnittstellen/schluessel).
