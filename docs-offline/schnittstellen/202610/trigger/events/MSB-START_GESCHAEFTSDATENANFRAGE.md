# [MSB] START_GESCHAEFTSDATENANFRAGE
<span hidden data-pagefind-meta={"title:Trigger-Ereignis START_GESCHAEFTSDATENANFRAGE — Marktrolle MSB (FV 202610)"} />

Marktrolle **MSB** · Formatversion **202610** · BO4E-Schema **1.7.8**

## Stammdaten

Unter diesem Topic ist genau einer der folgenden 3 Prüfidentifikatoren zulässig — welcher, entscheidet der Event-Prozess.

| Prüfi | Scope | Anwendungsfall | Festlegung | Kommunikation |
|---|---|---|---|---|
| [PI_17104](/schnittstellen/202610/pruefi/ORDERS/PI_17104) | ORDERS | Anfrage vom MSB Gas | GPKE Teil 4 | MSB (Gas) → NB (Strom) |
| [PI_17126](/schnittstellen/202610/pruefi/ORDERS/PI_17126) | ORDERS | Anfrage Stammdaten Messlokation (Gas) | GeLi Gas 2.0 | MSB (Strom / Gas) → NB |
| [PI_17132](/schnittstellen/202610/pruefi/ORDERS/PI_17132) | ORDERS | Anfrage Stammdaten (Strom) | GPKE Teil 4 | LF → NB |

Die Stammdaten der 3 Prüfidentifikatoren in **einer** Struktur — eine Spalte je Prüfidentifikator, wie im Anwendungshandbuch. Ein Wert in der Spalte heißt, dass das Feld zu diesem Prüfidentifikator gehört: **Muss**, wenn seine Spezifikation es verlangt, sonst **Kann**. Eine leere Zelle heißt »gehört nicht dazu«, nicht »unbekannt«. Vorausgewählt ist der erste; die übrigen schaltet die Leiste über der Tabelle zu.

<Handbuchsatz>

<div className="maco-tabellenrahmen">

| Struktur (BO4E) | Beschreibung | Format | <span className="hbs-p" title="Anfrage vom MSB Gas">17104</span> | <span className="hbs-p" title="Anfrage Stammdaten Messlokation (Gas)">17126</span> | <span className="hbs-p" title="Anfrage Stammdaten (Strom)">17132</span> | Bedingung |
|---|---|---|---|---|---|---|
| <span className="hbs-g hbs-e0">**stammdaten**</span> | — | object | Kann | Kann | Kann | — |
| <span className="hbs-g hbs-e1">**ANFRAGE** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | Kann | Muss | — |
| <span className="hbs-f hbs-e2">[lokationsId](/bo4e/202610/bo/Anfrage#lokationsid)</span><span className="hbs-nr">00010</span> | Für welche Markt- oder Messlokation gilt diese Anfrage. | string | Kann | Kann | Muss | — |
| <span className="hbs-g hbs-e1">**MESSLOKATION** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | Kann | — | — |
| <span className="hbs-g hbs-e2">**messadresse**</span> | — | object | Kann | Kann | — | — |
| <span className="hbs-f hbs-e3">[hausnummer](/bo4e/202610/com/Adresse#hausnummer)</span><span className="hbs-nr">00020</span> | Hausnummer und Ergänzung | string | Kann | Kann | — | — |
| <span className="hbs-f hbs-e3">[landescode](/bo4e/202610/com/Adresse#landescode)</span><span className="hbs-nr">00030</span> | Landescode | [Enum Landescode](/bo4e/202610/enum/Landescode) | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`AC`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`AD`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`AE`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`AF`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`AG`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`AI`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`AL`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`AM`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`AN`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`AO`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`AQ`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`AR`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`AS`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`AT`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`AU`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`AW`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`AX`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`AZ`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`BA`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`BB`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`BD`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`BE`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`BF`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`BG`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`BH`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`BI`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`BJ`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`BL`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`BM`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`BN`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`BO`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`BQ`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`BR`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`BS`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`BT`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`BU`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`BV`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`BW`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`BY`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`BZ`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`CA`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`CC`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`CD`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`CF`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`CG`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`CH`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`CI`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`CK`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`CL`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`CM`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`CN`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`CO`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`CP`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`CR`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`CS`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`CU`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`CV`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`CW`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`CX`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`CY`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`CZ`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`DE`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`DG`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`DJ`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`DK`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`DM`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`DO`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`DZ`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`EA`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`EC`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`EE`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`EG`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`EH`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`ER`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`ES`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`ET`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`EU`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`FI`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`FJ`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`FK`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`FM`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`FO`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`FR`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`FX`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`GA`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`GB`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`GD`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`GE`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`GF`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`GG`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`GH`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`GI`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`GL`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`GM`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`GN`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`GP`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`GQ`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`GR`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`GS`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`GT`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`GU`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`GW`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`GY`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`HK`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`HM`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`HN`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`HR`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`HT`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`HU`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`IC`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`ID`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`IE`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`IL`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`IM`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`IN`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`IO`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`IQ`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`IR`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`IS`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`IT`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`JE`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`JM`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`JO`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`JP`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`KE`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`KG`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`KH`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`KI`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`KM`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`KN`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`KP`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`KR`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`KW`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`KY`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`KZ`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`LA`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`LB`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`LC`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`LI`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`LK`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`LR`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`LS`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`LT`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`LU`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`LV`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`LY`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`MA`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`MC`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`MD`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`ME`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`MF`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`MG`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`MH`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`MK`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`ML`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`MM`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`MN`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`MO`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`MP`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`MQ`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`MR`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`MS`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`MT`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`MU`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`MV`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`MW`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`MX`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`MY`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`MZ`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`NA`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`NC`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`NE`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`NF`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`NG`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`NI`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`NL`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`NO`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`NP`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`NR`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`NT`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`NU`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`NZ`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`OM`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`PA`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`PE`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`PF`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`PG`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`PH`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`PK`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`PL`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`PM`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`PN`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`PR`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`PS`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`PT`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`PW`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`PY`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`QA`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`RE`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`RO`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`RS`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`RU`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`RW`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`SA`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`SB`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`SC`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`SD`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`SE`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`SF`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`SG`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`SH`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`SI`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`SJ`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`SK`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`SL`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`SM`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`SN`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`SO`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`SR`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`SS`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`ST`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`SU`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`SV`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`SX`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`SY`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`SZ`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`TA`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`TC`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`TD`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`TF`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`TG`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`TJ`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`TK`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`TL`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`TM`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`TN`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`TO`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`TP`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`TR`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`TT`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`TV`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`TW`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`TZ`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`UA`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`UG`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`UK`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`UM`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`US`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`UY`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`UZ`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`VA`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`VC`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`VE`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`VG`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`VI`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`VN`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`VU`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`WF`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`WS`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`XK`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`YE`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`YT`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`YU`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`ZA`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`ZM`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`ZR`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`ZW`</span> | — | — | Kann | Kann | — | — |
| <span className="hbs-f hbs-e3">[ort](/bo4e/202610/com/Adresse#ort)</span><span className="hbs-nr">00040</span> | Ort | string | Kann | Kann | — | — |
| <span className="hbs-f hbs-e3">[ortsteil](/bo4e/202610/com/Adresse#ortsteil)</span><span className="hbs-nr">00050</span> | Ortsteil | string | Kann | Kann | — | — |
| <span className="hbs-f hbs-e3">[postfach](/bo4e/202610/com/Adresse#postfach)</span><span className="hbs-nr">00060</span> | Postfach | string | Kann | Kann | — | — |
| <span className="hbs-f hbs-e3">[postleitzahl](/bo4e/202610/com/Adresse#postleitzahl)</span><span className="hbs-nr">00070</span> | Postleitzahl | string | Kann | Kann | — | — |
| <span className="hbs-f hbs-e3">[strasse](/bo4e/202610/com/Adresse#strasse)</span><span className="hbs-nr">00080</span> | Strasse | string | Kann | Kann | — | — |
| <span className="hbs-g hbs-e3">**zusatzInformation**</span> | — | object | Kann | Kann | — | — |
| <span className="hbs-f hbs-e4">[zusatz1](/bo4e/202610/com/AdresszusatzInformation#zusatz1)</span><span className="hbs-nr">00090</span> | Adresszusatz 1 | string | Kann | Kann | — | — |
| <span className="hbs-f hbs-e4">[zusatz2](/bo4e/202610/com/AdresszusatzInformation#zusatz2)</span><span className="hbs-nr">00100</span> | Adresszusatz 2 | string | Kann | Kann | — | — |
| <span className="hbs-f hbs-e4">[zusatz3](/bo4e/202610/com/AdresszusatzInformation#zusatz3)</span><span className="hbs-nr">00110</span> | Adresszusatz 3 | string | Kann | Kann | — | — |
| <span className="hbs-f hbs-e4">[zusatz4](/bo4e/202610/com/AdresszusatzInformation#zusatz4)</span><span className="hbs-nr">00120</span> | Adresszusatz 4 | string | Kann | Kann | — | — |
| <span className="hbs-f hbs-e4">[zusatz5](/bo4e/202610/com/AdresszusatzInformation#zusatz5)</span><span className="hbs-nr">00130</span> | Adresszusatz 5 | string | Kann | Kann | — | — |
| <span className="hbs-g hbs-e1">**AUFTRAG** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | Kann | — | — |
| <span className="hbs-g hbs-e2">**positionsdaten** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | Kann | — | — |
| <span className="hbs-g hbs-e3">**allgemeineInformationen**</span> | — | object | — | Kann | — | — |
| <span className="hbs-f hbs-e4">[info1](/bo4e/202610/com/AllgemeineInformationen#info1)</span><span className="hbs-nr">00140</span> | Allgemeine Info 1 | string | — | Kann | — | — |
| <span className="hbs-f hbs-e4">[info2](/bo4e/202610/com/AllgemeineInformationen#info2)</span><span className="hbs-nr">00150</span> | Allgemeine Info 2 | string | — | Kann | — | — |
| <span className="hbs-f hbs-e4">[info3](/bo4e/202610/com/AllgemeineInformationen#info3)</span><span className="hbs-nr">00160</span> | Allgemeine Info 3 | string | — | Kann | — | — |
| <span className="hbs-f hbs-e4">[info4](/bo4e/202610/com/AllgemeineInformationen#info4)</span><span className="hbs-nr">00170</span> | Allgemeine Info 4 | string | — | Kann | — | — |
| <span className="hbs-f hbs-e4">[info5](/bo4e/202610/com/AllgemeineInformationen#info5)</span><span className="hbs-nr">00180</span> | Allgemeine Info 5 | string | — | Kann | — | — |
| <span className="hbs-g hbs-e1">**MESSSTELLENBETRIEBSVERTRAG** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | Kann | — | — |
| <span className="hbs-g hbs-e2">**vertragspartner2** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | Kann | — | — |
| <span className="hbs-f hbs-e3">[anrede](/bo4e/202610/bo/Geschaeftspartner#anrede)</span><span className="hbs-nr">00190</span> | Die Anrede für den GePa, Z.B. Herr. | string | — | Kann | — | — |
| <span className="hbs-f hbs-e3">[geschaeftspartnerrolle](/bo4e/202610/bo/Geschaeftspartner#geschaeftspartnerrolle)</span><span className="hbs-nr">00200</span> | Rolle, die der Geschäftspartner hat (z.B. Interessent, Kunde). | array | — | Kann | — | — |
| <span className="hbs-f hbs-e3">[gewerbekennzeichnung](/bo4e/202610/bo/Geschaeftspartner#gewerbekennzeichnung)</span><span className="hbs-nr">00210</span> | Kennzeichnung ob es sich um einen Gewerbe/Unternehmen (gewerbeKennzeichnung = true)<br/>oder eine Privatperson handelt. (gewerbeKennzeichnung = false) | boolean | — | Kann | — | — |
| <span className="hbs-f hbs-e3">[name1](/bo4e/202610/bo/Geschaeftspartner#name1)</span><span className="hbs-nr">00220</span> | Erster Teil des Namens. Hier kann der Firmenname oder bei Privatpersonen<br/>beispielsweise der Nachname dargestellt werden. Beispiele: Yellow Strom GmbH<br/>oder Hagen | string | — | Kann | — | — |
| <span className="hbs-f hbs-e3">[name2](/bo4e/202610/bo/Geschaeftspartner#name2)</span><span className="hbs-nr">00230</span> | Zweiter Teil des Namens. Hier kann der eine Erweiterung zum Firmennamen oder<br/>bei Privatpersonen beispielsweise der Vorname dargestellt werden. Beispiele:<br/>Bereich Süd oder Nina | string | — | Kann | — | — |
| <span className="hbs-f hbs-e3">[name3](/bo4e/202610/bo/Geschaeftspartner#name3)</span><span className="hbs-nr">00240</span> | Dritter Teil des Namens. Hier können weitere Ergänzungen zum Firmennamen oder<br/>bei Privatpersonen Zusätze zum Namen dargestellt werden. Beispiele: und Afrika<br/>oder Sängerin | string | — | Kann | — | — |
| <span className="hbs-f hbs-e3">[name4](/bo4e/202610/bo/Geschaeftspartner#name4)</span><span className="hbs-nr">00250</span> | name4 | string | — | Kann | — | — |
| <span className="hbs-g hbs-e1">**ZAEHLER** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | Kann | — | — |
| <span className="hbs-g hbs-e2">**geraete** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | Kann | — | — |
| <span className="hbs-f hbs-e3">[geraetenummer](/bo4e/202610/com/Geraet#geraetenummer)</span><span className="hbs-nr">00260</span> | Die auf dem Geräte aufgedruckte Nummer, die vom MSB vergeben wird. | string | — | Kann | — | — |

</div>

</Handbuchsatz>

## Kette dieses Auslösers

Das Ereignis löst die Nachricht aus. Der Marktpartner antwortet mit einer der genannten Antworten, und danach schreibt die MACO APP den Vorgang in Ihr Backendsystem.

| Nachricht | Antworten | Schreibaufruf nach der Antwort |
|---|---|---|
| [17104](/schnittstellen/202610/pruefi/ORDERS/PI_17104) | — | — |
| [17126](/schnittstellen/202610/pruefi/ORDERS/PI_17126) | [44060](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44060) | `POST /updateProcessData` |
| [17132](/schnittstellen/202610/pruefi/ORDERS/PI_17132) | — | — |

Dieses Ereignis löst einen Schritt in dieser Rollensicht aus:

| Prozess | Beteiligter | Regelwerk | Sparte |
|---|---|---|---|
| [Geschäftsdatenanfrage vom MSB an NB](/prozessdoku/202610/MSB/geli-gas-2-0-geschaftsdatenanfrage-vom-msb-an-nb) | MSB | GeLi Gas 2.0 | Gas |

## Transaktionsdaten

Der Umschlag der Nachricht. Pflichtfelder müssen beim Trigger-Aufruf gesetzt sein.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| [kategorie](/bo4e/202610/cdoc/Transaktionsdaten#kategorie) | string | **ja** | Qualifier aus dem Beginn der EDIFact Nachricht / BGM |
| [sparte](/bo4e/202610/cdoc/Transaktionsdaten#sparte) | [Enum Sparte](/bo4e/202610/enum/Sparte) | **ja** | Enthält Informationen über die Sparte Werte: `STROM`, `GAS`, `FERNWAERME`, `NAHWAERME`, `WASSER`, `ABWASSER` |
| `pruefidentifikator` | — | nein | Wird dynamisch im Event-Prozess ermittelt (Entscheidungsgrundlage: kategorie, sparte). Ein vom Sender mitgegebener Wert wird ignoriert. Im Topic mögliche Prüfis — 17104, 17126, 17132. Mögliche Werte: `17104`, `17126`, `17132` |
| [absender › rollencodenummer](/bo4e/202610/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |
| [empfaenger › rollencodenummer](/bo4e/202610/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |

## Zusatzdaten

`eventname` ist auf **START_GESCHAEFTSDATENANFRAGE** festgelegt. Dieser Wert bleibt auch in der englischen Fassung deutsch, weil Camunda darüber korreliert.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `prozessId` | string | **ja** | — |
| `eventname` | const `START_GESCHAEFTSDATENANFRAGE` | **ja** | — |

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
