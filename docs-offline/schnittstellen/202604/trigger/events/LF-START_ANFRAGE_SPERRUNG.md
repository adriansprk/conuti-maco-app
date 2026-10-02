# [LF] START_ANFRAGE_SPERRUNG
<span hidden data-pagefind-meta={"title:Trigger-Ereignis START_ANFRAGE_SPERRUNG — Marktrolle LF (FV 202604)"} />

Marktrolle **LF** · Formatversion **202604** · BO4E-Schema **1.7.8**

## Stammdaten

Unter diesem Topic ist genau einer der folgenden 1 Prüfidentifikatoren zulässig — welcher, entscheidet der Event-Prozess.

| Prüfi | Scope | Anwendungsfall | Festlegung | Kommunikation |
|---|---|---|---|---|
| [PI_17115](/schnittstellen/202604/pruefi/ORDERS/PI_17115) | ORDERS | Sperrauftrag | AWH Sperrprozesse Gas | LF → NB |

Die Stammdaten der 1 Prüfidentifikatoren in **einer** Struktur — eine Spalte je Prüfidentifikator, wie im Anwendungshandbuch. Ein Wert in der Spalte heißt, dass das Feld zu diesem Prüfidentifikator gehört: **Muss**, wenn seine Spezifikation es verlangt, sonst **Kann**. Eine leere Zelle heißt »gehört nicht dazu«, nicht »unbekannt«. Vorausgewählt ist der erste; die übrigen schaltet die Leiste über der Tabelle zu.

<Handbuchsatz>

<div className="maco-tabellenrahmen">

| Struktur (BO4E) | Beschreibung | Format | <span className="hbs-p" title="Sperrauftrag">17115</span> | Bedingung |
|---|---|---|---|---|
| <span className="hbs-g hbs-e0">**stammdaten**</span> | — | object | Kann | — |
| <span className="hbs-g hbs-e1">**ANFRAGE** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | — |
| <span className="hbs-f hbs-e2">[lokationsId](/bo4e/202604/bo/Anfrage#lokationsid) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00010</span> | Für welche Markt- oder Messlokation gilt diese Anfrage. | string | Muss | — |
| <span className="hbs-g hbs-e1">**AUFTRAG** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-f hbs-e2">[ausfuehrungsdatum](/bo4e/202604/bo/Auftrag#ausfuehrungsdatum)</span><span className="hbs-nr">00020</span> | Das Ausführungsdatum beschreibt zu welchem Zeitpunkt ein Auftrag ausgeführt werden soll. | string (date-time) | Kann | — |
| <span className="hbs-f hbs-e2">[startdatum](/bo4e/202604/bo/Auftrag#startdatum)</span><span className="hbs-nr">00030</span> | Das Startdatum beschreibt zu welchem Zeitpunkt ein Auftrag gestartet wurde/wird. | string (date-time) | Kann | — |
| <span className="hbs-g hbs-e2">**positionsdaten** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-g hbs-e3">**allgemeineInformationen**</span> | — | object | Kann | — |
| <span className="hbs-f hbs-e4">[info1](/bo4e/202604/com/AllgemeineInformationen#info1)</span><span className="hbs-nr">00040</span> | Allgemeine Info 1 | string | Kann | — |
| <span className="hbs-f hbs-e4">[info2](/bo4e/202604/com/AllgemeineInformationen#info2)</span><span className="hbs-nr">00050</span> | Allgemeine Info 2 | string | Kann | — |
| <span className="hbs-f hbs-e4">[info3](/bo4e/202604/com/AllgemeineInformationen#info3)</span><span className="hbs-nr">00060</span> | Allgemeine Info 3 | string | Kann | — |
| <span className="hbs-f hbs-e4">[info4](/bo4e/202604/com/AllgemeineInformationen#info4)</span><span className="hbs-nr">00070</span> | Allgemeine Info 4 | string | Kann | — |
| <span className="hbs-f hbs-e4">[info5](/bo4e/202604/com/AllgemeineInformationen#info5)</span><span className="hbs-nr">00080</span> | Allgemeine Info 5 | string | Kann | — |
| <span className="hbs-g hbs-e1">**SPERRAUFTRAG** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-g hbs-e2">**treffpunkt**</span> | — | object | Kann | — |
| <span className="hbs-f hbs-e3">[hausnummer](/bo4e/202604/com/Adresse#hausnummer)</span><span className="hbs-nr">00090</span> | Hausnummer und Ergänzung | string | Kann | — |
| <span className="hbs-f hbs-e3">[landescode](/bo4e/202604/com/Adresse#landescode)</span><span className="hbs-nr">00100</span> | Landescode | [Enum Landescode](/bo4e/202604/enum/Landescode) | Kann | — |
| <span className="hbs-w hbs-e4">`AC`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`AD`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`AE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`AF`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`AG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`AI`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`AL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`AM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`AN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`AO`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`AQ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`AR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`AS`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`AT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`AU`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`AW`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`AX`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`AZ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`BA`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`BB`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`BD`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`BE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`BF`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`BG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`BH`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`BI`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`BJ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`BL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`BM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`BN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`BO`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`BQ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`BR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`BS`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`BT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`BU`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`BV`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`BW`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`BY`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`BZ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`CA`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`CC`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`CD`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`CF`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`CG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`CH`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`CI`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`CK`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`CL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`CM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`CN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`CO`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`CP`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`CR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`CS`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`CU`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`CV`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`CW`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`CX`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`CY`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`CZ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`DE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`DG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`DJ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`DK`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`DM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`DO`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`DZ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`EA`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`EC`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`EE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`EG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`EH`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`ER`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`ES`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`ET`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`EU`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`FI`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`FJ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`FK`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`FM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`FO`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`FR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`FX`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`GA`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`GB`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`GD`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`GE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`GF`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`GG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`GH`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`GI`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`GL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`GM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`GN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`GP`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`GQ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`GR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`GS`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`GT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`GU`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`GW`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`GY`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`HK`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`HM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`HN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`HR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`HT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`HU`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`IC`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`ID`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`IE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`IL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`IM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`IN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`IO`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`IQ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`IR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`IS`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`IT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`JE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`JM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`JO`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`JP`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`KE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`KG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`KH`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`KI`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`KM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`KN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`KP`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`KR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`KW`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`KY`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`KZ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`LA`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`LB`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`LC`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`LI`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`LK`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`LR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`LS`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`LT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`LU`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`LV`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`LY`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MA`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MC`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MD`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`ME`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MF`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MH`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MK`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`ML`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MO`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MP`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MQ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MS`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MU`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MV`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MW`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MX`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MY`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MZ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`NA`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`NC`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`NE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`NF`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`NG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`NI`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`NL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`NO`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`NP`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`NR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`NT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`NU`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`NZ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`OM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`PA`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`PE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`PF`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`PG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`PH`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`PK`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`PL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`PM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`PN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`PR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`PS`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`PT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`PW`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`PY`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`QA`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`RE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`RO`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`RS`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`RU`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`RW`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`SA`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`SB`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`SC`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`SD`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`SE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`SF`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`SG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`SH`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`SI`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`SJ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`SK`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`SL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`SM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`SN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`SO`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`SR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`SS`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`ST`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`SU`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`SV`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`SX`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`SY`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`SZ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`TA`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`TC`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`TD`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`TF`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`TG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`TJ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`TK`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`TL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`TM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`TN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`TO`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`TP`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`TR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`TT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`TV`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`TW`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`TZ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`UA`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`UG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`UK`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`UM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`US`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`UY`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`UZ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`VA`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`VC`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`VE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`VG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`VI`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`VN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`VU`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`WF`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`WS`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`XK`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`YE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`YT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`YU`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`ZA`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`ZM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`ZR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`ZW`</span> | — | — | Kann | — |
| <span className="hbs-f hbs-e3">[ort](/bo4e/202604/com/Adresse#ort)</span><span className="hbs-nr">00110</span> | Ort | string | Kann | — |
| <span className="hbs-f hbs-e3">[ortsteil](/bo4e/202604/com/Adresse#ortsteil)</span><span className="hbs-nr">00120</span> | Ortsteil | string | Kann | — |
| <span className="hbs-f hbs-e3">[postfach](/bo4e/202604/com/Adresse#postfach)</span><span className="hbs-nr">00130</span> | Postfach | string | Kann | — |
| <span className="hbs-f hbs-e3">[postleitzahl](/bo4e/202604/com/Adresse#postleitzahl)</span><span className="hbs-nr">00140</span> | Postleitzahl | string | Kann | — |
| <span className="hbs-f hbs-e3">[strasse](/bo4e/202604/com/Adresse#strasse)</span><span className="hbs-nr">00150</span> | Strasse | string | Kann | — |
| <span className="hbs-g hbs-e3">**zusatzInformation**</span> | — | object | Kann | — |
| <span className="hbs-f hbs-e4">[zusatz1](/bo4e/202604/com/AdresszusatzInformation#zusatz1)</span><span className="hbs-nr">00160</span> | Adresszusatz 1 | string | Kann | — |
| <span className="hbs-f hbs-e4">[zusatz2](/bo4e/202604/com/AdresszusatzInformation#zusatz2)</span><span className="hbs-nr">00170</span> | Adresszusatz 2 | string | Kann | — |
| <span className="hbs-f hbs-e4">[zusatz3](/bo4e/202604/com/AdresszusatzInformation#zusatz3)</span><span className="hbs-nr">00180</span> | Adresszusatz 3 | string | Kann | — |
| <span className="hbs-f hbs-e4">[zusatz4](/bo4e/202604/com/AdresszusatzInformation#zusatz4)</span><span className="hbs-nr">00190</span> | Adresszusatz 4 | string | Kann | — |
| <span className="hbs-f hbs-e4">[zusatz5](/bo4e/202604/com/AdresszusatzInformation#zusatz5)</span><span className="hbs-nr">00200</span> | Adresszusatz 5 | string | Kann | — |

</div>

</Handbuchsatz>

## Kette dieses Auslösers

Das Ereignis löst die Nachricht aus. Der Marktpartner antwortet mit einer der genannten Antworten, und danach schreibt die MACO APP den Vorgang in Ihr Backendsystem.

| Nachricht | Antworten | Schreibaufruf nach der Antwort |
|---|---|---|
| [17115](/schnittstellen/202604/pruefi/ORDERS/PI_17115) | [19116](/schnittstellen/202604/pruefi/ORDRSP/PI_19116), [19117](/schnittstellen/202604/pruefi/ORDRSP/PI_19117) | `POST /updateProcessData` (abgeleitet) |

Dieses Ereignis löst Schritte in diesen Rollensichten aus:

| Prozess | Beteiligter | Regelwerk | Sparte |
|---|---|---|---|
| [Unterbrechung der Anschlussnutzung (Sperren) auf Anweisung des LF](/prozessdoku/202604/LF/awh-sperrprozesse-gas-unterbrechung-der-anschlussnutzung-sperren-auf-anweisung-des-lf) | LF | AWH Sperrprozesse Gas | Gas |
| [Unterbrechung der Anschlussnutzung (Sperren) auf Anweisung des LF](/prozessdoku/202604/LF/GPKE-Teil2-unterbrechung-der-anschlussnutzung-sperren-auf-anweisung-des-lf) | LF | GPKE Teil 2 | Strom |

## Transaktionsdaten

Der Umschlag der Nachricht. Pflichtfelder müssen beim Trigger-Aufruf gesetzt sein.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| [kategorie](/bo4e/202604/cdoc/Transaktionsdaten#kategorie) | string | **ja** | Qualifier aus dem Beginn der EDIFact Nachricht / BGM |
| [sparte](/bo4e/202604/cdoc/Transaktionsdaten#sparte) | [Enum Sparte](/bo4e/202604/enum/Sparte) | **ja** | Enthält Informationen über die Sparte Werte: `STROM`, `GAS`, `FERNWAERME`, `NAHWAERME`, `WASSER`, `ABWASSER` |
| `pruefidentifikator` | — | nein | Wird dynamisch im Event-Prozess ermittelt. Ein vom Sender mitgegebener Wert wird ignoriert. Im Topic mögliche Prüfis — 17115. Mögliche Werte: `17115` |
| [absender › rollencodenummer](/bo4e/202604/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |
| [empfaenger › rollencodenummer](/bo4e/202604/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |

## Zusatzdaten

`eventname` ist auf **START_ANFRAGE_SPERRUNG** festgelegt. Dieser Wert bleibt auch in der englischen Fassung deutsch, weil Camunda darüber korreliert.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `prozessId` | string | **ja** | — |
| `eventname` | const `START_ANFRAGE_SPERRUNG` | **ja** | — |

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
