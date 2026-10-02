# [LF] START_VERSAND_SDAE
<span hidden data-pagefind-meta={"title:Trigger-Ereignis START_VERSAND_SDAE — Marktrolle LF (FV 202610)"} />

Marktrolle **LF** · Formatversion **202610** · BO4E-Schema **1.7.8**

## Stammdaten

Unter diesem Topic ist genau einer der folgenden 6 Prüfidentifikatoren zulässig — welcher, entscheidet der Event-Prozess.

| Prüfi | Scope | Anwendungsfall | Festlegung | Kommunikation |
|---|---|---|---|---|
| [PI_44109](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44109) | UTILMD_GAS | Nicht bila.rel Änderung vom LF | GeLi Gas 2.0 | LF → NB |
| [PI_44120](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44120) | UTILMD_GAS | Bila.rel. Änderung vom LF | Marktraumumstellung | LF → NB |
| [PI_55109](/schnittstellen/202610/pruefi/UTILMD/PI_55109) | UTILMD | Änderung Daten der MaLo | GPKE Teil 4 | LF → NB |
| [PI_55110](/schnittstellen/202610/pruefi/UTILMD/PI_55110) | UTILMD | Änderung Daten der MaLo | GPKE Teil 4 | LF → MSB |
| [PI_55230](/schnittstellen/202610/pruefi/UTILMD/PI_55230) | UTILMD | Änderung Blindabr.-Daten der NeLo | GPKE Teil 4 | LF → NB |
| [PI_55693](/schnittstellen/202610/pruefi/UTILMD/PI_55693) | UTILMD | Änderung Daten der TR | GPKE Teil 4 | LF → NB |

Die Stammdaten der 6 Prüfidentifikatoren in **einer** Struktur — eine Spalte je Prüfidentifikator, wie im Anwendungshandbuch. Ein Wert in der Spalte heißt, dass das Feld zu diesem Prüfidentifikator gehört: **Muss**, wenn seine Spezifikation es verlangt, sonst **Kann**. Eine leere Zelle heißt »gehört nicht dazu«, nicht »unbekannt«. Vorausgewählt ist der erste; die übrigen schaltet die Leiste über der Tabelle zu.

<Handbuchsatz>

<div className="maco-tabellenrahmen">

| Struktur (BO4E) | Beschreibung | Format | <span className="hbs-p" title="Nicht bila.rel Änderung vom LF">44109</span> | <span className="hbs-p" title="Bila.rel. Änderung vom LF">44120</span> | <span className="hbs-p" title="Änderung Daten der MaLo">55109</span> | <span className="hbs-p" title="Änderung Daten der MaLo">55110</span> | <span className="hbs-p" title="Änderung Blindabr.-Daten der NeLo">55230</span> | <span className="hbs-p" title="Änderung Daten der TR">55693</span> | Bedingung |
|---|---|---|---|---|---|---|---|---|---|
| <span className="hbs-g hbs-e0">**stammdaten**</span> | — | object | Kann | Kann | Kann | Kann | Kann | Kann | — |
| <span className="hbs-g hbs-e1">**ENERGIELIEFERVERTRAG** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-g hbs-e2">**korrespondenzpartner**</span> | — | object | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[anrede](/bo4e/202610/bo/Geschaeftspartner#anrede)</span><span className="hbs-nr">00010</span> | Die Anrede für den GePa, Z.B. Herr. | string | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[gewerbekennzeichnung](/bo4e/202610/bo/Geschaeftspartner#gewerbekennzeichnung)</span><span className="hbs-nr">00020</span> | Kennzeichnung ob es sich um einen Gewerbe/Unternehmen (gewerbeKennzeichnung = true)<br/>oder eine Privatperson handelt. (gewerbeKennzeichnung = false) | boolean | Kann | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[name1](/bo4e/202610/bo/Geschaeftspartner#name1)</span><span className="hbs-nr">00030</span> | Erster Teil des Namens. Hier kann der Firmenname oder bei Privatpersonen<br/>beispielsweise der Nachname dargestellt werden. Beispiele: Yellow Strom GmbH<br/>oder Hagen | string | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[name2](/bo4e/202610/bo/Geschaeftspartner#name2)</span><span className="hbs-nr">00040</span> | Zweiter Teil des Namens. Hier kann der eine Erweiterung zum Firmennamen oder<br/>bei Privatpersonen beispielsweise der Vorname dargestellt werden. Beispiele:<br/>Bereich Süd oder Nina | string | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[name3](/bo4e/202610/bo/Geschaeftspartner#name3)</span><span className="hbs-nr">00050</span> | Dritter Teil des Namens. Hier können weitere Ergänzungen zum Firmennamen oder<br/>bei Privatpersonen Zusätze zum Namen dargestellt werden. Beispiele: und Afrika<br/>oder Sängerin | string | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[name4](/bo4e/202610/bo/Geschaeftspartner#name4)</span><span className="hbs-nr">00060</span> | name4 | string | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-g hbs-e3">**partneradresse**</span> | — | object | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-f hbs-e4">[hausnummer](/bo4e/202610/com/Adresse#hausnummer)</span><span className="hbs-nr">00070</span> | Hausnummer und Ergänzung | string | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-f hbs-e4">[landescode](/bo4e/202610/com/Adresse#landescode)</span><span className="hbs-nr">00080</span> | Landescode | [Enum Landescode](/bo4e/202610/enum/Landescode) | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AC`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AD`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AE`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AF`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AG`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AI`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AL`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AM`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AN`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AO`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AQ`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AR`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AS`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AT`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AU`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AW`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AX`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AZ`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BA`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BB`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BD`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BE`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BF`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BG`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BH`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BI`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BJ`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BL`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BM`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BN`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BO`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BQ`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BR`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BS`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BT`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BU`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BV`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BW`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BY`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BZ`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CA`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CC`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CD`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CF`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CG`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CH`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CI`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CK`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CL`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CM`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CN`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CO`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CP`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CR`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CS`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CU`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CV`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CW`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CX`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CY`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CZ`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`DE`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`DG`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`DJ`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`DK`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`DM`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`DO`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`DZ`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`EA`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`EC`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`EE`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`EG`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`EH`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`ER`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`ES`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`ET`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`EU`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`FI`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`FJ`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`FK`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`FM`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`FO`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`FR`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`FX`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GA`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GB`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GD`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GE`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GF`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GG`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GH`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GI`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GL`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GM`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GN`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GP`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GQ`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GR`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GS`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GT`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GU`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GW`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GY`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`HK`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`HM`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`HN`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`HR`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`HT`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`HU`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`IC`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`ID`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`IE`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`IL`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`IM`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`IN`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`IO`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`IQ`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`IR`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`IS`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`IT`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`JE`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`JM`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`JO`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`JP`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`KE`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`KG`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`KH`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`KI`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`KM`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`KN`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`KP`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`KR`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`KW`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`KY`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`KZ`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`LA`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`LB`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`LC`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`LI`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`LK`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`LR`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`LS`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`LT`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`LU`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`LV`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`LY`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MA`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MC`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MD`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`ME`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MF`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MG`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MH`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MK`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`ML`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MM`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MN`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MO`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MP`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MQ`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MR`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MS`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MT`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MU`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MV`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MW`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MX`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MY`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MZ`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`NA`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`NC`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`NE`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`NF`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`NG`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`NI`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`NL`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`NO`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`NP`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`NR`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`NT`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`NU`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`NZ`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`OM`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`PA`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`PE`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`PF`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`PG`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`PH`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`PK`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`PL`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`PM`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`PN`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`PR`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`PS`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`PT`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`PW`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`PY`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`QA`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`RE`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`RO`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`RS`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`RU`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`RW`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SA`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SB`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SC`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SD`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SE`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SF`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SG`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SH`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SI`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SJ`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SK`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SL`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SM`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SN`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SO`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SR`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SS`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`ST`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SU`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SV`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SX`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SY`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SZ`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TA`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TC`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TD`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TF`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TG`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TJ`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TK`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TL`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TM`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TN`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TO`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TP`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TR`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TT`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TV`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TW`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TZ`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`UA`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`UG`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`UK`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`UM`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`US`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`UY`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`UZ`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`VA`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`VC`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`VE`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`VG`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`VI`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`VN`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`VU`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`WF`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`WS`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`XK`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`YE`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`YT`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`YU`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`ZA`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`ZM`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`ZR`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`ZW`</span> | — | — | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-f hbs-e4">[ort](/bo4e/202610/com/Adresse#ort)</span><span className="hbs-nr">00090</span> | Ort | string | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-f hbs-e4">[ortsteil](/bo4e/202610/com/Adresse#ortsteil)</span><span className="hbs-nr">00100</span> | Ortsteil | string | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-f hbs-e4">[postfach](/bo4e/202610/com/Adresse#postfach)</span><span className="hbs-nr">00110</span> | Postfach | string | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-f hbs-e4">[postleitzahl](/bo4e/202610/com/Adresse#postleitzahl)</span><span className="hbs-nr">00120</span> | Postleitzahl | string | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-f hbs-e4">[strasse](/bo4e/202610/com/Adresse#strasse)</span><span className="hbs-nr">00130</span> | Strasse | string | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-g hbs-e3">**ansprechpartner**</span> | — | object | — | — | Kann | Kann | — | — | — |
| <span className="hbs-f hbs-e4">[eMailAdresse](/bo4e/202610/bo/Ansprechpartner#emailadresse)</span><span className="hbs-nr">00140</span> | E-Mail Adresse | string | — | — | Kann | Kann | — | — | — |
| <span className="hbs-g hbs-e4">**rufnummern** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | — | Kann | Kann | — | — | — |
| <span className="hbs-f hbs-e5">[nummerntyp](/bo4e/202610/com/Rufnummer#nummerntyp)</span><span className="hbs-nr">00150</span> | Rufnummernart | [Enum Rufnummernart](/bo4e/202610/enum/Rufnummernart) | — | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`RUF_ZENTRALE`</span> | — | — | — | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`FAX_ZENTRALE`</span> | — | — | — | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SAMMELRUF`</span> | — | — | — | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SAMMELFAX`</span> | — | — | — | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`ABTEILUNGRUF`</span> | — | — | — | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`ABTEILUNGFAX`</span> | — | — | — | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`RUF_DURCHWAHL`</span> | — | — | — | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`FAX_DURCHWAHL`</span> | — | — | — | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MOBIL_NUMMER`</span> | — | — | — | — | Kann | Kann | — | — | — |
| <span className="hbs-f hbs-e5">[rufnummer](/bo4e/202610/com/Rufnummer#rufnummer)</span><span className="hbs-nr">00160</span> | rufnummer | string | — | — | Kann | Kann | — | — | — |
| <span className="hbs-g hbs-e2">**vertragskonditionen**</span> | — | object | Kann | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[abrechnungsintervall](/bo4e/202610/com/Vertragskonditionen#abrechnungsintervall)</span><span className="hbs-nr">00170</span> | abrechnungsintervall | integer | Kann | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**vertragspartner2** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[anrede](/bo4e/202610/bo/Geschaeftspartner#anrede)</span><span className="hbs-nr">00180</span> | Die Anrede für den GePa, Z.B. Herr. | string | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[gewerbekennzeichnung](/bo4e/202610/bo/Geschaeftspartner#gewerbekennzeichnung)</span><span className="hbs-nr">00190</span> | Kennzeichnung ob es sich um einen Gewerbe/Unternehmen (gewerbeKennzeichnung = true)<br/>oder eine Privatperson handelt. (gewerbeKennzeichnung = false) | boolean | Kann | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[name1](/bo4e/202610/bo/Geschaeftspartner#name1)</span><span className="hbs-nr">00200</span> | Erster Teil des Namens. Hier kann der Firmenname oder bei Privatpersonen<br/>beispielsweise der Nachname dargestellt werden. Beispiele: Yellow Strom GmbH<br/>oder Hagen | string | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[name2](/bo4e/202610/bo/Geschaeftspartner#name2)</span><span className="hbs-nr">00210</span> | Zweiter Teil des Namens. Hier kann der eine Erweiterung zum Firmennamen oder<br/>bei Privatpersonen beispielsweise der Vorname dargestellt werden. Beispiele:<br/>Bereich Süd oder Nina | string | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[name3](/bo4e/202610/bo/Geschaeftspartner#name3)</span><span className="hbs-nr">00220</span> | Dritter Teil des Namens. Hier können weitere Ergänzungen zum Firmennamen oder<br/>bei Privatpersonen Zusätze zum Namen dargestellt werden. Beispiele: und Afrika<br/>oder Sängerin | string | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[name4](/bo4e/202610/bo/Geschaeftspartner#name4)</span><span className="hbs-nr">00230</span> | name4 | string | Kann | — | Kann | Kann | — | — | — |
| <span className="hbs-g hbs-e3">**externeReferenzen** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — | Kann | — | — | — | — |
| <span className="hbs-f hbs-e4">[exRefName](/bo4e/202610/com/ExterneReferenz#exrefname)</span><span className="hbs-nr">00240</span> | Bezeichnung der externen Referenz (z.B. "hochfrequenz integration services") | string | Kann | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e5">`Kundennummer beim Lieferanten`</span> | — | — | Kann | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e5">`Kundennummer beim Altlieferanten`</span> | — | — | Kann | — | Kann | — | — | — | — |
| <span className="hbs-f hbs-e4">[exRefWert](/bo4e/202610/com/ExterneReferenz#exrefwert)</span><span className="hbs-nr">00250</span> | Wert der externen Referenz (z.B. "123456"; "4711") | string | Kann | — | Kann | — | — | — | — |
| <span className="hbs-f hbs-e3">[geschaeftspartnerrolle](/bo4e/202610/bo/Geschaeftspartner#geschaeftspartnerrolle)</span><span className="hbs-nr">00260</span> | Rolle, die der Geschäftspartner hat (z.B. Interessent, Kunde). | array | — | — | Kann | Kann | — | — | — |
| <span className="hbs-f hbs-e2">[datenqualitaet](/bo4e/202610/bo/Vertrag#datenqualitaet)</span><span className="hbs-nr">00270</span> | Datenqualitaet | [Enum Datenqualitaet](/bo4e/202610/enum/Datenqualitaet) | — | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`ERWARTETE_DATEN`</span> | — | — | — | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`INFORMATIVE_DATEN`</span> | — | — | — | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`GUELTIGE_DATEN`</span> | — | — | — | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN`</span> | — | — | — | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_KEINE_DATEN_VORHANDEN`</span> | — | — | — | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN_ERWARTET`</span> | — | — | — | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_DATEN`</span> | — | — | — | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_ERWARTETE_DATEN`</span> | — | — | — | — | Kann | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | Kann | Kann | — | — | — |
| <span className="hbs-g hbs-e2">**enFG** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | — | Kann | — | — | — | — |
| <span className="hbs-f hbs-e3">[grund](/bo4e/202610/com/EnFG#grund)</span><span className="hbs-nr">00280</span> | Grund der Umlagenverringerung | array | — | — | Kann | — | — | — | — |
| <span className="hbs-f hbs-e3">[grundlageVerringerungUmlagen](/bo4e/202610/com/EnFG#grundlageverringerungumlagen)</span><span className="hbs-nr">00290</span> | GrundlageVerringerungUmlagen | [Enum GrundlageVerringerungUmlagen](/bo4e/202610/enum/GrundlageVerringerungUmlagen) | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e4">`ERFUELLT_VORAUSSETZUNG_NACH_ENFG`</span> | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e4">`ERFUELLT_NICHT_VORAUSSETZUNG_NACH_ENFG`</span> | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e4">`KEINE_ANGABE`</span> | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-g hbs-e2">**gueltigkeitszeitraum**</span> | — | object | — | — | Kann | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[zeitraumId](/bo4e/202610/com/Zeitraum#zeitraumid)</span><span className="hbs-nr">00300</span> | zeitraumId | integer | — | — | Kann | Kann | — | — | — |
| <span className="hbs-g hbs-e1">**MARKTLOKATION** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | Muss | Kann | Kann | — | — | — |
| <span className="hbs-f hbs-e2">[marktlokationsId](/bo4e/202610/bo/Marktlokation#marktlokationsid) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00310</span> | Identifikationsnummer einer Marktlokation, an der Energie entweder<br/>verbraucht, oder erzeugt wird | string | Muss | Muss | Kann | Kann | — | — | — |
| <span className="hbs-f hbs-e2">[datenqualitaet](/bo4e/202610/bo/Marktlokation#datenqualitaet)</span><span className="hbs-nr">00320</span> | Datenqualitaet | [Enum Datenqualitaet](/bo4e/202610/enum/Datenqualitaet) | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e3">`ERWARTETE_DATEN`</span> | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e3">`INFORMATIVE_DATEN`</span> | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e3">`GUELTIGE_DATEN`</span> | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN`</span> | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_KEINE_DATEN_VORHANDEN`</span> | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN_ERWARTET`</span> | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_DATEN`</span> | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_ERWARTETE_DATEN`</span> | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-f hbs-e2">[foerderungsLand](/bo4e/202610/bo/Marktlokation#foerderungsland)</span><span className="hbs-nr">00330</span> | foerderungsLand | string | — | — | Kann | — | — | — | — |
| <span className="hbs-g hbs-e2">**gueltigkeitszeitraum**</span> | — | object | — | — | Kann | — | — | — | — |
| <span className="hbs-f hbs-e3">[zeitraumId](/bo4e/202610/com/Zeitraum#zeitraumid)</span><span className="hbs-nr">00340</span> | zeitraumId | integer | — | — | Kann | — | — | — | — |
| <span className="hbs-g hbs-e1">**NETZNUTZUNGSVERTRAG** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | Kann | Kann | — | — | — | — |
| <span className="hbs-f hbs-e2">[vertragsbeginn](/bo4e/202610/bo/Vertrag#vertragsbeginn)</span><span className="hbs-nr">00350</span> | Gibt an, wann der Vertrag beginnt. | string (date-time) | Kann | Kann | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**vertragskonditionen**</span> | — | object | Kann | — | Kann | — | — | — | — |
| <span className="hbs-f hbs-e3">[haushaltskunde](/bo4e/202610/com/Vertragskonditionen#haushaltskunde)</span><span className="hbs-nr">00360</span> | haushaltskunde | boolean | Kann | — | Kann | — | — | — | — |
| <span className="hbs-g hbs-e1">**BILANZIERUNG** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | — | Muss | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**bilanzkreise** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | — | Muss | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[bezeichnung](/bo4e/202610/bo/Bilanzkreis#bezeichnung) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00370</span> | Externe Bezeichnung | string | — | Muss | — | — | — | — | — |
| <span className="hbs-g hbs-e1">**VERWENDUNGSZEITRAUM** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | — | — | Muss | Muss | Muss | Muss | — |
| <span className="hbs-f hbs-e2">[datenqualitaet](/bo4e/202610/bo/Verwendungszeitraum#datenqualitaet) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00380</span> | Datenqualitaet | [Enum Datenqualitaet](/bo4e/202610/enum/Datenqualitaet) | — | — | Muss | Muss | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`ERWARTETE_DATEN`</span> | — | — | — | — | Muss | Muss | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | Muss | Muss | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`INFORMATIVE_DATEN`</span> | — | — | — | — | Muss | Muss | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`GUELTIGE_DATEN`</span> | — | — | — | — | Muss | Muss | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN`</span> | — | — | — | — | Muss | Muss | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_KEINE_DATEN_VORHANDEN`</span> | — | — | — | — | Muss | Muss | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN_ERWARTET`</span> | — | — | — | — | Muss | Muss | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_DATEN`</span> | — | — | — | — | Muss | Muss | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_ERWARTETE_DATEN`</span> | — | — | — | — | Muss | Muss | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | Muss | Muss | Muss | Muss | — |
| <span className="hbs-f hbs-e2">[verwendungAb](/bo4e/202610/bo/Verwendungszeitraum#verwendungab) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00390</span> | verwendungAb | string (date-time) | — | — | Muss | Muss | Muss | Muss | — |
| <span className="hbs-f hbs-e2">[verwendungBis](/bo4e/202610/bo/Verwendungszeitraum#verwendungbis)</span><span className="hbs-nr">00400</span> | verwendungBis | string (date-time) | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-f hbs-e2">[zeitraumId](/bo4e/202610/bo/Verwendungszeitraum#zeitraumid) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00410</span> | zeitraumId | integer | — | — | Muss | Muss | Muss | Muss | — |
| <span className="hbs-g hbs-e1">**NETZLOKATION** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | — | — | — | — | Muss | — | — |
| <span className="hbs-f hbs-e2">[datenqualitaet](/bo4e/202610/bo/Netzlokation#datenqualitaet)</span><span className="hbs-nr">00420</span> | Datenqualitaet | [Enum Datenqualitaet](/bo4e/202610/enum/Datenqualitaet) | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`ERWARTETE_DATEN`</span> | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`INFORMATIVE_DATEN`</span> | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`GUELTIGE_DATEN`</span> | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN`</span> | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_KEINE_DATEN_VORHANDEN`</span> | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN_ERWARTET`</span> | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_DATEN`</span> | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_ERWARTETE_DATEN`</span> | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-f hbs-e2">[netzlokationsId](/bo4e/202610/bo/Netzlokation#netzlokationsid) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00430</span> | Identifikationsnummer einer Netzlokation, an der Energie entweder<br/>verbraucht, oder erzeugt wird (Like MarktlokationsId Marktlokation) | string | — | — | — | — | Muss | — | — |
| <span className="hbs-g hbs-e2">**abrechnungsdaten** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | — | — | — | Kann | — | — |
| <span className="hbs-f hbs-e3">[zahlerBlindarbeitLf](/bo4e/202610/com/Netznutzungsabrechnungsdaten#zahlerblindarbeitlf)</span><span className="hbs-nr">00440</span> | Zahlung der Blindarbeit durch den Lieferanten | boolean | — | — | — | — | Kann | — | — |
| <span className="hbs-g hbs-e2">**gueltigkeitszeitraum**</span> | — | object | — | — | — | — | Kann | — | — |
| <span className="hbs-f hbs-e3">[zeitraumId](/bo4e/202610/com/Zeitraum#zeitraumid)</span><span className="hbs-nr">00450</span> | zeitraumId | integer | — | — | — | — | Kann | — | — |
| <span className="hbs-g hbs-e1">**TECHNISCHE_RESSOURCE** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | — | — | — | — | — | Muss | — |
| <span className="hbs-f hbs-e2">[datenqualitaet](/bo4e/202610/bo/TechnischeRessource#datenqualitaet)</span><span className="hbs-nr">00460</span> | Datenqualitaet | [Enum Datenqualitaet](/bo4e/202610/enum/Datenqualitaet) | — | — | — | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`ERWARTETE_DATEN`</span> | — | — | — | — | — | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | — | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`INFORMATIVE_DATEN`</span> | — | — | — | — | — | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`GUELTIGE_DATEN`</span> | — | — | — | — | — | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN`</span> | — | — | — | — | — | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_KEINE_DATEN_VORHANDEN`</span> | — | — | — | — | — | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN_ERWARTET`</span> | — | — | — | — | — | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_DATEN`</span> | — | — | — | — | — | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_ERWARTETE_DATEN`</span> | — | — | — | — | — | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | — | — | — | Kann | — |
| <span className="hbs-f hbs-e2">[fernsteuerbarkeit](/bo4e/202610/bo/TechnischeRessource#fernsteuerbarkeit)</span><span className="hbs-nr">00470</span> | fernsteuerbarkeit | boolean | — | — | — | — | — | Kann | — |
| <span className="hbs-f hbs-e2">[ressourcenId](/bo4e/202610/bo/TechnischeRessource#ressourcenid) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00480</span> | ressourcenId | string | — | — | — | — | — | Muss | — |
| <span className="hbs-g hbs-e2">**gueltigkeitszeitraum**</span> | — | object | — | — | — | — | — | Kann | — |
| <span className="hbs-f hbs-e3">[zeitraumId](/bo4e/202610/com/Zeitraum#zeitraumid)</span><span className="hbs-nr">00490</span> | zeitraumId | integer | — | — | — | — | — | Kann | — |

</div>

</Handbuchsatz>

## Kette dieses Auslösers

Das Ereignis löst die Nachricht aus. Der Marktpartner antwortet mit einer der genannten Antworten, und danach schreibt die MACO APP den Vorgang in Ihr Backendsystem.

| Nachricht | Antworten | Schreibaufruf nach der Antwort |
|---|---|---|
| [44109](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44109) | [44111](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44111) | `POST /updateProcessData` |
| [44120](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44120) | [44121](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44121) | `POST /updateProcessData` |
| [55109](/schnittstellen/202610/pruefi/UTILMD/PI_55109) | — | — |
| [55110](/schnittstellen/202610/pruefi/UTILMD/PI_55110) | — | — |
| [55230](/schnittstellen/202610/pruefi/UTILMD/PI_55230) | — | — |
| [55693](/schnittstellen/202610/pruefi/UTILMD/PI_55693) | — | — |

Dieses Ereignis löst Schritte in diesen Rollensichten aus:

| Prozess | Beteiligter | Regelwerk | Sparte |
|---|---|---|---|
| [Stammdatenänderung vom LF (verantwortlich) ausgehend](/prozessdoku/202610/LF/GPKE-Teil4-stammdatenaenderung-vom-lf-verantwortlich-ausgehend) | LF | GPKE Teil 4 | Strom |
| [Stammdatenänderung vom LF (verantwortlich) ausgehend](/prozessdoku/202610/LF/geli-gas-2-0-stammdatenanderung-vom-lf-verantwortlich-ausgehend) | LF | GeLi Gas 2.0 | Gas |

## Transaktionsdaten

Der Umschlag der Nachricht. Pflichtfelder müssen beim Trigger-Aufruf gesetzt sein.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| [gueltigAb](/bo4e/202610/cdoc/Transaktionsdaten#gueltigab) | string (date-time) | **ja** | Gültigkeitsdatum/-zeit / DTM+7 |
| [kategorie](/bo4e/202610/cdoc/Transaktionsdaten#kategorie) | string | **ja** | Qualifier aus dem Beginn der EDIFact Nachricht / BGM |
| [sparte](/bo4e/202610/cdoc/Transaktionsdaten#sparte) | [Enum Sparte](/bo4e/202610/enum/Sparte) | **ja** | Enthält Informationen über die Sparte Werte: `STROM`, `GAS`, `FERNWAERME`, `NAHWAERME`, `WASSER`, `ABWASSER` |
| [transaktionsgrund](/bo4e/202610/cdoc/Transaktionsdaten#transaktionsgrund) | string | **ja** | Der Transaktionsgrund beschreibt den Geschäftsvorfall zur Kategorie genauer / UTILMD STS+7++###+ZW4+E03 |
| [transaktionsgrundergaenzung](/bo4e/202610/cdoc/Transaktionsdaten#transaktionsgrundergaenzung) | string | **ja** | Ergänzung zum Transaktionsgrund / UTILMD STS+7++E01+###+E03 |
| [vertragsbeginn](/bo4e/202610/cdoc/Transaktionsdaten#vertragsbeginn) | string (date-time) | **ja** | Datum Vertragsbeginn / DTM+92 |
| `pruefidentifikator` | — | nein | Wird dynamisch im Event-Prozess ermittelt (Entscheidungsgrundlage: marktrolle, sparte, transaktionsgrund). Ein vom Sender mitgegebener Wert wird ignoriert. Im Topic mögliche Prüfis — 44109, 44120, 55109, 55110, 55230, 55693. Mögliche Werte: `44109`, `44120`, `55109`, `55110`, `55230`, `55693` |
| [absender › rollencodenummer](/bo4e/202610/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |
| [empfaenger › marktrolle](/bo4e/202610/bo/Marktteilnehmer#marktrolle) | [Enum Marktrolle](/bo4e/202610/enum/Marktrolle) | nein | Gibt im Klartext die Bezeichnung der Marktrolle an. Werte: `NB`, `LF`, `MSB`, `MSBA`, `GMSB`, `MDL`, `DL`, `BKV`, `UENB`, `KUNDE-SELBST-NN` … (+9) |
| [empfaenger › rollencodenummer](/bo4e/202610/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |

## Zusatzdaten

`eventname` ist auf **START_VERSAND_SDAE** festgelegt. Dieser Wert bleibt auch in der englischen Fassung deutsch, weil Camunda darüber korreliert.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `prozessId` | string | **ja** | — |
| `eventname` | const `START_VERSAND_SDAE` | **ja** | — |

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
