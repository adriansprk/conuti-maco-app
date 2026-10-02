# [LF] START_LIEFERBEGINN
<span hidden data-pagefind-meta={"title:Trigger-Ereignis START_LIEFERBEGINN — Marktrolle LF (FV 202610)"} />

Marktrolle **LF** · Formatversion **202610** · BO4E-Schema **1.7.8**

## Stammdaten

Unter diesem Topic ist genau einer der folgenden 5 Prüfidentifikatoren zulässig — welcher, entscheidet der Event-Prozess.

| Prüfi | Scope | Anwendungsfall | Festlegung | Kommunikation |
|---|---|---|---|---|
| [PI_44001](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44001) | UTILMD_GAS | Anmeldung NN | GeLi Gas 2.0 | LF (entspricht LFN) → NB |
| [PI_55001](/schnittstellen/202610/pruefi/UTILMD/PI_55001) | UTILMD | Anmeldung verb. MaLo | GPKE Teil 2 | LFN → NB |
| [PI_55077](/schnittstellen/202610/pruefi/UTILMD/PI_55077) | UTILMD | Anmeldung erz. MaLo | GPKE Teil 2 | LFN → NB |
| [PI_55600](/schnittstellen/202610/pruefi/UTILMD/PI_55600) | UTILMD | Anmeldung neuer verb. MaLo | GPKE Teil 2 | LF → NB |
| [PI_55601](/schnittstellen/202610/pruefi/UTILMD/PI_55601) | UTILMD | Anmeldung neuer erz. MaLo | GPKE Teil 2 | LF → NB |

Die Stammdaten der 9 Prüfidentifikatoren in **einer** Struktur — eine Spalte je Prüfidentifikator, wie im Anwendungshandbuch. Ein Wert in der Spalte heißt, dass das Feld zu diesem Prüfidentifikator gehört: **Muss**, wenn seine Spezifikation es verlangt, sonst **Kann**. Eine leere Zelle heißt »gehört nicht dazu«, nicht »unbekannt«. Vorausgewählt ist der erste; die übrigen schaltet die Leiste über der Tabelle zu.

<Handbuchsatz>

<div className="maco-tabellenrahmen">

| Struktur (BO4E) | Beschreibung | Format | <span className="hbs-p" title="Anmeldung NN">44001</span> | <span className="hbs-p" title="Anmeldung verb. MaLo">55001</span> | <span className="hbs-p" title="Anmeldung erz. MaLo">55077</span> | <span className="hbs-p" title="Anmeldung neuer verb. MaLo">55600</span> | <span className="hbs-p" title="Anmeldung neuer erz. MaLo">55601</span> | Bedingung |
|---|---|---|---|---|---|---|---|---|
| <span className="hbs-g hbs-e0">**stammdaten**</span> | — | object | Kann | Kann | Kann | Kann | Kann | — |
| <span className="hbs-g hbs-e1">**BILANZIERUNG** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[fallgruppenzuordnung](/bo4e/202610/bo/Bilanzierung#fallgruppenzuordnung)</span><span className="hbs-nr">00010</span> | Fallgruppenzuordnung (für gas RLM) | [Enum Fallgruppenzuordnung](/bo4e/202610/enum/Fallgruppenzuordnung) | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`GABI_RLMmT`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`GABI_RLMoT`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`GABI_RLMNEV`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**bilanzkreise** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[bezeichnung](/bo4e/202610/bo/Bilanzkreis#bezeichnung) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00020</span> | Externe Bezeichnung | string | Muss | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[prioritaet](/bo4e/202610/bo/Bilanzkreis#prioritaet)</span><span className="hbs-nr">00030</span> | prioritaet | integer | Kann | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**jahresverbrauchsprognose**</span> | — | object | Kann | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[einheit](/bo4e/202610/com/Menge#einheit)</span><span className="hbs-nr">00040</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202610/enum/Mengeneinheit) | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`W`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`WH`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KW`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KWH`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KVARH`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MW`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MWH`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`STUECK`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KUBIKMETER`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`STUNDE`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`TAG`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MONAT`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`JAHR`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`PROZENT`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`ANZAHL`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`VAR`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KVAR`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`VARH`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KWHK`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`Z16`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KWT`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`WATT_PRO_QUADRATMETER`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`METER_PRO_SEKUNDE`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[wert](/bo4e/202610/com/Menge#wert)</span><span className="hbs-nr">00050</span> | Wert | number (float) | Kann | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**kundenwert**</span> | — | object | Kann | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[wert](/bo4e/202610/com/Menge#wert)</span><span className="hbs-nr">00060</span> | Wert | number (float) | Kann | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**lastprofile** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[bezeichnung](/bo4e/202610/com/Lastprofil#bezeichnung)</span><span className="hbs-nr">00070</span> | Bezeichnung des Profils | string | Kann | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[herausgeber](/bo4e/202610/com/Lastprofil#herausgeber)</span><span className="hbs-nr">00080</span> | Herausgeber des Lastprofils | string | Kann | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[verfahren](/bo4e/202610/com/Lastprofil#verfahren)</span><span className="hbs-nr">00090</span> | Profilverfahren | [Enum Profilverfahren](/bo4e/202610/enum/Profilverfahren) | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`SYNTHETISCH`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`ANALYTISCH`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-g hbs-e1">**ENERGIELIEFERVERTRAG** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | Muss | — | Muss | Kann | — |
| <span className="hbs-g hbs-e2">**korrespondenzpartner** <span className="hbs-pflicht">\*</span></span> | — | object | Muss | Muss | — | Muss | Kann | — |
| <span className="hbs-f hbs-e3">[anrede](/bo4e/202610/bo/Geschaeftspartner#anrede)</span><span className="hbs-nr">00100</span> | Die Anrede für den GePa, Z.B. Herr. | string | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[gewerbekennzeichnung](/bo4e/202610/bo/Geschaeftspartner#gewerbekennzeichnung)</span><span className="hbs-nr">00110</span> | Kennzeichnung ob es sich um einen Gewerbe/Unternehmen (gewerbeKennzeichnung = true)<br/>oder eine Privatperson handelt. (gewerbeKennzeichnung = false) | boolean | Kann | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[name1](/bo4e/202610/bo/Geschaeftspartner#name1) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00120</span> | Erster Teil des Namens. Hier kann der Firmenname oder bei Privatpersonen<br/>beispielsweise der Nachname dargestellt werden. Beispiele: Yellow Strom GmbH<br/>oder Hagen | string | Muss | Muss | — | Muss | Kann | — |
| <span className="hbs-f hbs-e3">[name2](/bo4e/202610/bo/Geschaeftspartner#name2)</span><span className="hbs-nr">00130</span> | Zweiter Teil des Namens. Hier kann der eine Erweiterung zum Firmennamen oder<br/>bei Privatpersonen beispielsweise der Vorname dargestellt werden. Beispiele:<br/>Bereich Süd oder Nina | string | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[name3](/bo4e/202610/bo/Geschaeftspartner#name3)</span><span className="hbs-nr">00140</span> | Dritter Teil des Namens. Hier können weitere Ergänzungen zum Firmennamen oder<br/>bei Privatpersonen Zusätze zum Namen dargestellt werden. Beispiele: und Afrika<br/>oder Sängerin | string | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[name4](/bo4e/202610/bo/Geschaeftspartner#name4)</span><span className="hbs-nr">00150</span> | name4 | string | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-g hbs-e3">**partneradresse**</span> | — | object | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[hausnummer](/bo4e/202610/com/Adresse#hausnummer)</span><span className="hbs-nr">00160</span> | Hausnummer und Ergänzung | string | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[landescode](/bo4e/202610/com/Adresse#landescode)</span><span className="hbs-nr">00170</span> | Landescode | [Enum Landescode](/bo4e/202610/enum/Landescode) | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`AC`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`AD`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`AE`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`AF`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`AG`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`AI`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`AL`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`AM`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`AN`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`AO`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`AQ`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`AR`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`AS`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`AT`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`AU`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`AW`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`AX`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`AZ`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BA`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BB`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BD`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BE`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BF`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BG`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BH`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BI`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BJ`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BL`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BM`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BN`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BO`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BQ`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BR`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BS`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BT`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BU`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BV`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BW`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BY`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`BZ`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CA`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CC`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CD`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CF`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CG`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CH`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CI`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CK`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CL`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CM`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CN`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CO`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CP`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CR`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CS`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CU`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CV`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CW`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CX`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CY`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`CZ`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`DE`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`DG`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`DJ`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`DK`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`DM`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`DO`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`DZ`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`EA`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`EC`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`EE`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`EG`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`EH`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`ER`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`ES`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`ET`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`EU`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`FI`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`FJ`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`FK`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`FM`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`FO`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`FR`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`FX`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GA`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GB`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GD`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GE`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GF`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GG`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GH`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GI`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GL`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GM`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GN`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GP`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GQ`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GR`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GS`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GT`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GU`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GW`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`GY`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`HK`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`HM`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`HN`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`HR`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`HT`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`HU`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`IC`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`ID`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`IE`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`IL`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`IM`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`IN`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`IO`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`IQ`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`IR`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`IS`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`IT`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`JE`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`JM`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`JO`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`JP`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`KE`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`KG`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`KH`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`KI`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`KM`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`KN`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`KP`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`KR`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`KW`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`KY`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`KZ`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`LA`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`LB`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`LC`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`LI`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`LK`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`LR`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`LS`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`LT`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`LU`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`LV`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`LY`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MA`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MC`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MD`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`ME`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MF`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MG`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MH`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MK`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`ML`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MM`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MN`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MO`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MP`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MQ`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MR`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MS`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MT`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MU`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MV`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MW`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MX`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MY`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MZ`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`NA`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`NC`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`NE`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`NF`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`NG`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`NI`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`NL`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`NO`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`NP`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`NR`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`NT`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`NU`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`NZ`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`OM`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`PA`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`PE`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`PF`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`PG`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`PH`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`PK`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`PL`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`PM`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`PN`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`PR`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`PS`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`PT`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`PW`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`PY`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`QA`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`RE`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`RO`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`RS`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`RU`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`RW`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SA`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SB`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SC`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SD`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SE`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SF`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SG`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SH`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SI`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SJ`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SK`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SL`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SM`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SN`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SO`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SR`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SS`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`ST`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SU`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SV`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SX`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SY`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SZ`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`TA`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`TC`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`TD`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`TF`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`TG`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`TJ`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`TK`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`TL`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`TM`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`TN`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`TO`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`TP`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`TR`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`TT`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`TV`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`TW`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`TZ`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`UA`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`UG`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`UK`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`UM`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`US`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`UY`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`UZ`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`VA`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`VC`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`VE`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`VG`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`VI`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`VN`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`VU`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`WF`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`WS`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`XK`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`YE`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`YT`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`YU`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`ZA`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`ZM`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`ZR`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`ZW`</span> | — | — | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[ort](/bo4e/202610/com/Adresse#ort)</span><span className="hbs-nr">00180</span> | Ort | string | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[ortsteil](/bo4e/202610/com/Adresse#ortsteil)</span><span className="hbs-nr">00190</span> | Ortsteil | string | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[postfach](/bo4e/202610/com/Adresse#postfach)</span><span className="hbs-nr">00200</span> | Postfach | string | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[postleitzahl](/bo4e/202610/com/Adresse#postleitzahl)</span><span className="hbs-nr">00210</span> | Postleitzahl | string | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[strasse](/bo4e/202610/com/Adresse#strasse)</span><span className="hbs-nr">00220</span> | Strasse | string | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-g hbs-e3">**ansprechpartner**</span> | — | object | — | Kann | — | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[eMailAdresse](/bo4e/202610/bo/Ansprechpartner#emailadresse)</span><span className="hbs-nr">00230</span> | E-Mail Adresse | string | — | Kann | — | Kann | Kann | — |
| <span className="hbs-g hbs-e4">**rufnummern** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | Kann | — | Kann | Kann | — |
| <span className="hbs-f hbs-e5">[nummerntyp](/bo4e/202610/com/Rufnummer#nummerntyp)</span><span className="hbs-nr">00240</span> | Rufnummernart | [Enum Rufnummernart](/bo4e/202610/enum/Rufnummernart) | — | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`RUF_ZENTRALE`</span> | — | — | — | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`FAX_ZENTRALE`</span> | — | — | — | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SAMMELRUF`</span> | — | — | — | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`SAMMELFAX`</span> | — | — | — | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`ABTEILUNGRUF`</span> | — | — | — | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`ABTEILUNGFAX`</span> | — | — | — | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`RUF_DURCHWAHL`</span> | — | — | — | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`FAX_DURCHWAHL`</span> | — | — | — | Kann | — | Kann | Kann | — |
| <span className="hbs-w hbs-e5">`MOBIL_NUMMER`</span> | — | — | — | Kann | — | Kann | Kann | — |
| <span className="hbs-f hbs-e5">[rufnummer](/bo4e/202610/com/Rufnummer#rufnummer)</span><span className="hbs-nr">00250</span> | rufnummer | string | — | Kann | — | Kann | Kann | — |
| <span className="hbs-g hbs-e2">**vertragskonditionen** <span className="hbs-pflicht">\*</span></span> | — | object | Muss | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[abrechnungsintervall](/bo4e/202610/com/Vertragskonditionen#abrechnungsintervall) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00260</span> | abrechnungsintervall | integer | Muss | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**vertragspartner2** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | Muss | — | Muss | Kann | — |
| <span className="hbs-f hbs-e3">[anrede](/bo4e/202610/bo/Geschaeftspartner#anrede)</span><span className="hbs-nr">00270</span> | Die Anrede für den GePa, Z.B. Herr. | string | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[gewerbekennzeichnung](/bo4e/202610/bo/Geschaeftspartner#gewerbekennzeichnung)</span><span className="hbs-nr">00280</span> | Kennzeichnung ob es sich um einen Gewerbe/Unternehmen (gewerbeKennzeichnung = true)<br/>oder eine Privatperson handelt. (gewerbeKennzeichnung = false) | boolean | Kann | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[name1](/bo4e/202610/bo/Geschaeftspartner#name1) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00290</span> | Erster Teil des Namens. Hier kann der Firmenname oder bei Privatpersonen<br/>beispielsweise der Nachname dargestellt werden. Beispiele: Yellow Strom GmbH<br/>oder Hagen | string | Muss | Muss | — | Muss | Kann | — |
| <span className="hbs-f hbs-e3">[name2](/bo4e/202610/bo/Geschaeftspartner#name2)</span><span className="hbs-nr">00300</span> | Zweiter Teil des Namens. Hier kann der eine Erweiterung zum Firmennamen oder<br/>bei Privatpersonen beispielsweise der Vorname dargestellt werden. Beispiele:<br/>Bereich Süd oder Nina | string | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[name3](/bo4e/202610/bo/Geschaeftspartner#name3)</span><span className="hbs-nr">00310</span> | Dritter Teil des Namens. Hier können weitere Ergänzungen zum Firmennamen oder<br/>bei Privatpersonen Zusätze zum Namen dargestellt werden. Beispiele: und Afrika<br/>oder Sängerin | string | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[name4](/bo4e/202610/bo/Geschaeftspartner#name4)</span><span className="hbs-nr">00320</span> | name4 | string | Kann | Kann | — | Kann | Kann | — |
| <span className="hbs-g hbs-e3">**externeReferenzen** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[exRefName](/bo4e/202610/com/ExterneReferenz#exrefname)</span><span className="hbs-nr">00330</span> | Bezeichnung der externen Referenz (z.B. "hochfrequenz integration services") | string | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`Kundennummer beim Lieferanten`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`Kundennummer beim Altlieferanten`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[exRefWert](/bo4e/202610/com/ExterneReferenz#exrefwert)</span><span className="hbs-nr">00340</span> | Wert der externen Referenz (z.B. "123456"; "4711") | string | Kann | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[geschaeftspartnerrolle](/bo4e/202610/bo/Geschaeftspartner#geschaeftspartnerrolle)</span><span className="hbs-nr">00350</span> | Rolle, die der Geschäftspartner hat (z.B. Interessent, Kunde). | array | — | Kann | — | Kann | Kann | — |
| <span className="hbs-g hbs-e2">**enFG** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | — | Muss | — | — | — | — |
| <span className="hbs-f hbs-e3">[grund](/bo4e/202610/com/EnFG#grund)</span><span className="hbs-nr">00360</span> | Grund der Umlagenverringerung | array | — | Kann | — | — | — | — |
| <span className="hbs-f hbs-e3">[grundlageVerringerungUmlagen](/bo4e/202610/com/EnFG#grundlageverringerungumlagen) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00370</span> | GrundlageVerringerungUmlagen | [Enum GrundlageVerringerungUmlagen](/bo4e/202610/enum/GrundlageVerringerungUmlagen) | — | Muss | — | — | — | — |
| <span className="hbs-w hbs-e4">`ERFUELLT_VORAUSSETZUNG_NACH_ENFG`</span> | — | — | — | Muss | — | — | — | — |
| <span className="hbs-w hbs-e4">`ERFUELLT_NICHT_VORAUSSETZUNG_NACH_ENFG`</span> | — | — | — | Muss | — | — | — | — |
| <span className="hbs-w hbs-e4">`KEINE_ANGABE`</span> | — | — | — | Muss | — | — | — | — |
| <span className="hbs-g hbs-e1">**MARKTLOKATION** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | Muss | Muss | Muss | Muss | — |
| <span className="hbs-f hbs-e2">[marktlokationsId](/bo4e/202610/bo/Marktlokation#marktlokationsid)</span><span className="hbs-nr">00380</span> | Identifikationsnummer einer Marktlokation, an der Energie entweder<br/>verbraucht, oder erzeugt wird | string | Kann | Kann | Kann | Kann | Kann | — |
| <span className="hbs-g hbs-e2">**lokationsadresse**</span> | — | object | Kann | — | — | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[hausnummer](/bo4e/202610/com/Adresse#hausnummer)</span><span className="hbs-nr">00390</span> | Hausnummer und Ergänzung | string | Kann | — | — | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[landescode](/bo4e/202610/com/Adresse#landescode)</span><span className="hbs-nr">00400</span> | Landescode | [Enum Landescode](/bo4e/202610/enum/Landescode) | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`AC`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`AD`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`AE`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`AF`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`AG`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`AI`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`AL`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`AM`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`AN`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`AO`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`AQ`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`AR`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`AS`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`AT`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`AU`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`AW`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`AX`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`AZ`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`BA`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`BB`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`BD`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`BE`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`BF`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`BG`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`BH`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`BI`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`BJ`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`BL`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`BM`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`BN`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`BO`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`BQ`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`BR`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`BS`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`BT`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`BU`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`BV`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`BW`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`BY`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`BZ`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`CA`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`CC`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`CD`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`CF`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`CG`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`CH`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`CI`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`CK`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`CL`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`CM`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`CN`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`CO`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`CP`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`CR`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`CS`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`CU`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`CV`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`CW`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`CX`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`CY`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`CZ`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`DE`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`DG`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`DJ`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`DK`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`DM`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`DO`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`DZ`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`EA`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`EC`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`EE`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`EG`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`EH`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`ER`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`ES`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`ET`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`EU`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`FI`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`FJ`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`FK`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`FM`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`FO`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`FR`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`FX`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`GA`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`GB`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`GD`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`GE`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`GF`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`GG`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`GH`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`GI`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`GL`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`GM`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`GN`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`GP`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`GQ`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`GR`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`GS`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`GT`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`GU`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`GW`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`GY`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`HK`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`HM`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`HN`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`HR`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`HT`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`HU`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`IC`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`ID`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`IE`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`IL`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`IM`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`IN`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`IO`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`IQ`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`IR`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`IS`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`IT`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`JE`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`JM`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`JO`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`JP`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`KE`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`KG`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`KH`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`KI`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`KM`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`KN`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`KP`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`KR`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`KW`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`KY`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`KZ`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`LA`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`LB`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`LC`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`LI`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`LK`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`LR`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`LS`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`LT`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`LU`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`LV`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`LY`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`MA`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`MC`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`MD`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`ME`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`MF`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`MG`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`MH`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`MK`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`ML`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`MM`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`MN`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`MO`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`MP`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`MQ`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`MR`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`MS`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`MT`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`MU`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`MV`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`MW`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`MX`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`MY`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`MZ`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`NA`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`NC`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`NE`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`NF`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`NG`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`NI`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`NL`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`NO`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`NP`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`NR`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`NT`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`NU`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`NZ`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`OM`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`PA`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`PE`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`PF`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`PG`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`PH`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`PK`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`PL`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`PM`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`PN`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`PR`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`PS`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`PT`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`PW`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`PY`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`QA`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`RE`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`RO`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`RS`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`RU`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`RW`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`SA`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`SB`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`SC`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`SD`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`SE`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`SF`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`SG`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`SH`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`SI`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`SJ`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`SK`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`SL`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`SM`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`SN`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`SO`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`SR`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`SS`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`ST`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`SU`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`SV`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`SX`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`SY`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`SZ`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`TA`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`TC`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`TD`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`TF`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`TG`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`TJ`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`TK`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`TL`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`TM`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`TN`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`TO`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`TP`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`TR`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`TT`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`TV`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`TW`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`TZ`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`UA`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`UG`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`UK`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`UM`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`US`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`UY`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`UZ`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`VA`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`VC`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`VE`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`VG`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`VI`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`VN`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`VU`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`WF`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`WS`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`XK`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`YE`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`YT`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`YU`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`ZA`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`ZM`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`ZR`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`ZW`</span> | — | — | Kann | — | — | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[ort](/bo4e/202610/com/Adresse#ort)</span><span className="hbs-nr">00410</span> | Ort | string | Kann | — | — | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[ortsteil](/bo4e/202610/com/Adresse#ortsteil)</span><span className="hbs-nr">00420</span> | Ortsteil | string | Kann | — | — | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[postfach](/bo4e/202610/com/Adresse#postfach)</span><span className="hbs-nr">00430</span> | Postfach | string | Kann | — | — | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[postleitzahl](/bo4e/202610/com/Adresse#postleitzahl)</span><span className="hbs-nr">00440</span> | Postleitzahl | string | Kann | — | — | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[strasse](/bo4e/202610/com/Adresse#strasse)</span><span className="hbs-nr">00450</span> | Strasse | string | Kann | — | — | Kann | Kann | — |
| <span className="hbs-g hbs-e3">**zusatzInformation**</span> | — | object | Kann | — | — | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[zusatz1](/bo4e/202610/com/AdresszusatzInformation#zusatz1)</span><span className="hbs-nr">00460</span> | Adresszusatz 1 | string | Kann | — | — | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[zusatz2](/bo4e/202610/com/AdresszusatzInformation#zusatz2)</span><span className="hbs-nr">00470</span> | Adresszusatz 2 | string | Kann | — | — | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[zusatz3](/bo4e/202610/com/AdresszusatzInformation#zusatz3)</span><span className="hbs-nr">00480</span> | Adresszusatz 3 | string | Kann | — | — | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[zusatz4](/bo4e/202610/com/AdresszusatzInformation#zusatz4)</span><span className="hbs-nr">00490</span> | Adresszusatz 4 | string | Kann | — | — | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[zusatz5](/bo4e/202610/com/AdresszusatzInformation#zusatz5)</span><span className="hbs-nr">00500</span> | Adresszusatz 5 | string | Kann | — | — | Kann | Kann | — |
| <span className="hbs-g hbs-e2">**zaehlwerke** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — | — | — | — | — |
| <span className="hbs-g hbs-e3">**konzessionsabgabe**</span> | — | object | Kann | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[kategorie](/bo4e/202610/com/Konzessionsabgabe#kategorie)</span><span className="hbs-nr">00510</span> | Kategorie | string | Kann | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[kosten](/bo4e/202610/com/Konzessionsabgabe#kosten)</span><span className="hbs-nr">00520</span> | Kosten | number (float) | Kann | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[satz](/bo4e/202610/com/Konzessionsabgabe#satz)</span><span className="hbs-nr">00530</span> | Art der Konzessionsabgabe | [Enum AbgabeArt](/bo4e/202610/enum/AbgabeArt) | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KAS`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SA`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SAS`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TA`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TAS`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TK`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TKS`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TS`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TSS`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**erforderlichesProduktpaket** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | — | Muss | Muss | Muss | Muss | — |
| <span className="hbs-f hbs-e3">[priorisierung](/bo4e/202610/com/Produktpaket#priorisierung)</span><span className="hbs-nr">00540</span> | Priorisierung | [Enum Priorisierung](/bo4e/202610/enum/Priorisierung) | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`PRIORITAET1`</span> | — | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`PRIORITAET2`</span> | — | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`PRIORITAET3`</span> | — | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`PRIORITAET4`</span> | — | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`PRIORITAET5`</span> | — | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[produktpaketId](/bo4e/202610/com/Produktpaket#produktpaketid) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00550</span> | produktpaketId | integer | — | Muss | Muss | Muss | Muss | — |
| <span className="hbs-f hbs-e3">[umsetzungsgradvorgabe](/bo4e/202610/com/Produktpaket#umsetzungsgradvorgabe)</span><span className="hbs-nr">00560</span> | Umsetzungsgradvorgabe | [Enum Umsetzungsgradvorgabe](/bo4e/202610/enum/Umsetzungsgradvorgabe) | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`ZUORDNUNG_NUR_WENN_PRODUKTPAKET_UMSETZBAR`</span> | — | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`ZUORDNUNG_AUCH_WENN_PRODUKTPAKET_NICHT_UMSETZBAR`</span> | — | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-g hbs-e3">**produkt** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | — | Muss | Muss | Muss | Muss | — |
| <span className="hbs-f hbs-e4">[codeProdukteigenschaft](/bo4e/202610/com/Produkt#codeprodukteigenschaft)</span><span className="hbs-nr">00570</span> | codeProdukteigenschaft | string | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[produktCode](/bo4e/202610/com/Produkt#produktcode) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00580</span> | produktCode | string | — | Muss | Muss | Muss | Muss | — |
| <span className="hbs-f hbs-e4">[wertedetails](/bo4e/202610/com/Produkt#wertedetails)</span><span className="hbs-nr">00590</span> | wertedetails | string | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-g hbs-e2">**marktlokationsTyp** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | Kann | — | — | — | — |
| <span className="hbs-f hbs-e3">[typ](/bo4e/202610/com/MarktlokationsTypisierung#typ)</span><span className="hbs-nr">00600</span> | Typisierung der Marktlokation als standard Marktlokation, ruhende Marktlokation oder Kundenanlage | [Enum MarktlokationsTyp](/bo4e/202610/enum/MarktlokationsTyp) | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e4">`STANDARD_MARKTLOKATION`</span> | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e4">`RUHENDE_MARKTLOKATION`</span> | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e4">`KUNDENANLAGE`</span> | — | — | — | Kann | — | — | — | — |
| <span className="hbs-f hbs-e2">[energierichtung](/bo4e/202610/bo/Marktlokation#energierichtung) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00610</span> | Kennzeichnung, ob Energie eingespeist oder entnommen (ausgespeist) wird. | [Enum Energierichtung](/bo4e/202610/enum/Energierichtung) | — | Muss | Muss | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`AUSSP`</span> | — | — | — | Muss | Muss | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`EINSP`</span> | — | — | — | Muss | Muss | Muss | Muss | — |
| <span className="hbs-f hbs-e2">[foerderungsLand](/bo4e/202610/bo/Marktlokation#foerderungsland)</span><span className="hbs-nr">00620</span> | foerderungsLand | string | — | — | Kann | — | Kann | — |
| <span className="hbs-f hbs-e2">[datenqualitaet](/bo4e/202610/bo/Marktlokation#datenqualitaet)</span><span className="hbs-nr">00630</span> | Datenqualitaet | [Enum Datenqualitaet](/bo4e/202610/enum/Datenqualitaet) | — | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`ERWARTETE_DATEN`</span> | — | — | — | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`INFORMATIVE_DATEN`</span> | — | — | — | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`GUELTIGE_DATEN`</span> | — | — | — | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN`</span> | — | — | — | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_KEINE_DATEN_VORHANDEN`</span> | — | — | — | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN_ERWARTET`</span> | — | — | — | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_DATEN`</span> | — | — | — | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_ERWARTETE_DATEN`</span> | — | — | — | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | — | Kann | Kann | — |
| <span className="hbs-g hbs-e1">**MESSLOKATION** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | — | — | Kann | Kann | — |
| <span className="hbs-f hbs-e2">[messlokationsId](/bo4e/202610/bo/Messlokation#messlokationsid)</span><span className="hbs-nr">00640</span> | Die Messlokations-Identifikation. Das ist die frühere Zählpunktbezeichnung,<br/>z.B. DE 47108151234567 | string | Kann | — | — | Kann | Kann | — |
| <span className="hbs-g hbs-e2">**ablesekartenempfaenger** <span className="hbs-pflicht">\*</span></span> | — | object | Muss | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[anrede](/bo4e/202610/bo/Geschaeftspartner#anrede)</span><span className="hbs-nr">00650</span> | Die Anrede für den GePa, Z.B. Herr. | string | Kann | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[gewerbekennzeichnung](/bo4e/202610/bo/Geschaeftspartner#gewerbekennzeichnung)</span><span className="hbs-nr">00660</span> | Kennzeichnung ob es sich um einen Gewerbe/Unternehmen (gewerbeKennzeichnung = true)<br/>oder eine Privatperson handelt. (gewerbeKennzeichnung = false) | boolean | Kann | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[name1](/bo4e/202610/bo/Geschaeftspartner#name1) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00670</span> | Erster Teil des Namens. Hier kann der Firmenname oder bei Privatpersonen<br/>beispielsweise der Nachname dargestellt werden. Beispiele: Yellow Strom GmbH<br/>oder Hagen | string | Muss | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[name2](/bo4e/202610/bo/Geschaeftspartner#name2)</span><span className="hbs-nr">00680</span> | Zweiter Teil des Namens. Hier kann der eine Erweiterung zum Firmennamen oder<br/>bei Privatpersonen beispielsweise der Vorname dargestellt werden. Beispiele:<br/>Bereich Süd oder Nina | string | Kann | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[name3](/bo4e/202610/bo/Geschaeftspartner#name3)</span><span className="hbs-nr">00690</span> | Dritter Teil des Namens. Hier können weitere Ergänzungen zum Firmennamen oder<br/>bei Privatpersonen Zusätze zum Namen dargestellt werden. Beispiele: und Afrika<br/>oder Sängerin | string | Kann | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[name4](/bo4e/202610/bo/Geschaeftspartner#name4)</span><span className="hbs-nr">00700</span> | name4 | string | Kann | — | — | — | — | — |
| <span className="hbs-g hbs-e3">**partneradresse**</span> | — | object | Kann | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[hausnummer](/bo4e/202610/com/Adresse#hausnummer)</span><span className="hbs-nr">00710</span> | Hausnummer und Ergänzung | string | Kann | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[landescode](/bo4e/202610/com/Adresse#landescode)</span><span className="hbs-nr">00720</span> | Landescode | [Enum Landescode](/bo4e/202610/enum/Landescode) | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AC`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AD`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AE`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AF`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AG`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AI`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AL`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AM`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AN`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AO`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AQ`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AR`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AS`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AT`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AU`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AW`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AX`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AZ`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BA`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BB`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BD`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BE`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BF`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BG`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BH`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BI`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BJ`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BL`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BM`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BN`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BO`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BQ`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BR`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BS`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BT`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BU`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BV`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BW`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BY`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BZ`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CA`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CC`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CD`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CF`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CG`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CH`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CI`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CK`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CL`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CM`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CN`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CO`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CP`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CR`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CS`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CU`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CV`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CW`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CX`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CY`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CZ`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`DE`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`DG`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`DJ`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`DK`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`DM`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`DO`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`DZ`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`EA`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`EC`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`EE`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`EG`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`EH`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ER`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ES`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ET`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`EU`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`FI`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`FJ`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`FK`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`FM`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`FO`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`FR`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`FX`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GA`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GB`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GD`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GE`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GF`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GG`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GH`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GI`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GL`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GM`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GN`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GP`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GQ`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GR`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GS`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GT`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GU`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GW`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GY`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`HK`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`HM`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`HN`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`HR`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`HT`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`HU`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IC`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ID`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IE`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IL`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IM`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IN`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IO`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IQ`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IR`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IS`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IT`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`JE`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`JM`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`JO`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`JP`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KE`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KG`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KH`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KI`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KM`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KN`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KP`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KR`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KW`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KY`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KZ`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LA`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LB`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LC`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LI`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LK`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LR`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LS`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LT`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LU`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LV`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LY`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MA`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MC`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MD`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ME`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MF`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MG`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MH`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MK`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ML`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MM`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MN`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MO`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MP`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MQ`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MR`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MS`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MT`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MU`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MV`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MW`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MX`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MY`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MZ`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NA`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NC`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NE`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NF`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NG`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NI`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NL`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NO`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NP`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NR`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NT`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NU`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NZ`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`OM`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PA`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PE`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PF`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PG`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PH`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PK`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PL`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PM`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PN`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PR`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PS`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PT`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PW`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PY`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`QA`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`RE`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`RO`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`RS`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`RU`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`RW`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SA`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SB`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SC`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SD`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SE`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SF`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SG`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SH`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SI`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SJ`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SK`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SL`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SM`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SN`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SO`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SR`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SS`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ST`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SU`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SV`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SX`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SY`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SZ`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TA`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TC`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TD`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TF`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TG`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TJ`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TK`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TL`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TM`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TN`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TO`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TP`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TR`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TT`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TV`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TW`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TZ`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`UA`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`UG`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`UK`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`UM`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`US`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`UY`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`UZ`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`VA`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`VC`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`VE`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`VG`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`VI`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`VN`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`VU`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`WF`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`WS`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`XK`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`YE`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`YT`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`YU`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ZA`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ZM`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ZR`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ZW`</span> | — | — | Kann | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[ort](/bo4e/202610/com/Adresse#ort)</span><span className="hbs-nr">00730</span> | Ort | string | Kann | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[ortsteil](/bo4e/202610/com/Adresse#ortsteil)</span><span className="hbs-nr">00740</span> | Ortsteil | string | Kann | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[postfach](/bo4e/202610/com/Adresse#postfach)</span><span className="hbs-nr">00750</span> | Postfach | string | Kann | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[postleitzahl](/bo4e/202610/com/Adresse#postleitzahl)</span><span className="hbs-nr">00760</span> | Postleitzahl | string | Kann | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[strasse](/bo4e/202610/com/Adresse#strasse)</span><span className="hbs-nr">00770</span> | Strasse | string | Kann | — | — | — | — | — |
| <span className="hbs-g hbs-e1">**NETZNUTZUNGSVERTRAG** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | Kann | Kann | Muss | Kann | — |
| <span className="hbs-f hbs-e2">[gemeinderabatt](/bo4e/202610/bo/Vertrag#gemeinderabatt) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00780</span> | gemeinderabatt für EDIFACT mapping. | integer | Muss | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[vertragsbeginn](/bo4e/202610/bo/Vertrag#vertragsbeginn)</span><span className="hbs-nr">00790</span> | Gibt an, wann der Vertrag beginnt. | string (date-time) | Kann | Kann | Kann | Kann | Kann | — |
| <span className="hbs-f hbs-e2">[vertragsende](/bo4e/202610/bo/Vertrag#vertragsende)</span><span className="hbs-nr">00800</span> | Gibt an, wann der Vertrag (voraussichtlich) endet oder beendet wurde. | string (date-time) | Kann | Kann | — | Kann | — | — |
| <span className="hbs-g hbs-e2">**vertragskonditionen** <span className="hbs-pflicht">\*</span></span> | — | object | Muss | Kann | — | Muss | — | — |
| <span className="hbs-f hbs-e3">[haushaltskunde](/bo4e/202610/com/Vertragskonditionen#haushaltskunde) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00810</span> | haushaltskunde | boolean | Muss | Kann | — | Muss | — | — |
| <span className="hbs-f hbs-e3">[netznutzungsvertrag](/bo4e/202610/com/Vertragskonditionen#netznutzungsvertrag) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00820</span> | Netznutzungsvertrag | [Enum Netznutzungsvertrag](/bo4e/202610/enum/Netznutzungsvertrag) | Muss | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KUNDEN_NB`</span> | — | — | Muss | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`LIEFERANTEN_NB`</span> | — | — | Muss | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[netznutzungszahler](/bo4e/202610/com/Vertragskonditionen#netznutzungszahler) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00830</span> | Netznutzungszahler | [Enum Netznutzungszahler](/bo4e/202610/enum/Netznutzungszahler) | Muss | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KUNDE`</span> | — | — | Muss | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`LIEFERANT`</span> | — | — | Muss | — | — | — | — | — |
| <span className="hbs-g hbs-e1">**ZAEHLER** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — | — | Kann | Kann | — |
| <span className="hbs-f hbs-e2">[zaehlernummer](/bo4e/202610/bo/Zaehler#zaehlernummer)</span><span className="hbs-nr">00840</span> | Nummerierung des Zählers, vergeben durch den Messstellenbetreiber | string | Kann | — | — | Kann | Kann | — |
| <span className="hbs-g hbs-e1">**TRANCHE** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e2">[tranchenId](/bo4e/202610/bo/Tranche#tranchenid)</span><span className="hbs-nr">00850</span> | tranchenId | string | — | — | Kann | — | — | — |
| <span className="hbs-g hbs-e1">**STEUERBARE_RESSOURCE** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | — | — | Kann | Kann | — |
| <span className="hbs-f hbs-e2">[ressourcenId](/bo4e/202610/bo/SteuerbareRessource#ressourcenid)</span><span className="hbs-nr">00860</span> | ressourcenId | string | — | — | — | Kann | Kann | — |
| <span className="hbs-g hbs-e1">**TECHNISCHE_RESSOURCE** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | — | — | Kann | Kann | — |
| <span className="hbs-f hbs-e2">[ressourcenId](/bo4e/202610/bo/TechnischeRessource#ressourcenid)</span><span className="hbs-nr">00870</span> | ressourcenId | string | — | — | — | Kann | Kann | — |

</div>

</Handbuchsatz>

## Kette dieses Auslösers

Das Ereignis löst die Nachricht aus. Der Marktpartner antwortet mit einer der genannten Antworten, und danach schreibt die MACO APP den Vorgang in Ihr Backendsystem.

| Nachricht | Antworten | Schreibaufruf nach der Antwort |
|---|---|---|
| [44001](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44001) | — | — |
| [55001](/schnittstellen/202610/pruefi/UTILMD/PI_55001) | [55002](/schnittstellen/202610/pruefi/UTILMD/PI_55002), [55003](/schnittstellen/202610/pruefi/UTILMD/PI_55003) | `POST /updateProcessData` |
| [55077](/schnittstellen/202610/pruefi/UTILMD/PI_55077) | [55078](/schnittstellen/202610/pruefi/UTILMD/PI_55078), [55080](/schnittstellen/202610/pruefi/UTILMD/PI_55080) | `POST /updateProcessData` |
| [55600](/schnittstellen/202610/pruefi/UTILMD/PI_55600) | [55602](/schnittstellen/202610/pruefi/UTILMD/PI_55602), [55604](/schnittstellen/202610/pruefi/UTILMD/PI_55604) | `POST /updateProcessData` |
| [55601](/schnittstellen/202610/pruefi/UTILMD/PI_55601) | [55603](/schnittstellen/202610/pruefi/UTILMD/PI_55603), [55605](/schnittstellen/202610/pruefi/UTILMD/PI_55605) | `POST /updateProcessData` |

Dieses Ereignis löst Schritte in diesen Rollensichten aus:

| Prozess | Beteiligter | Regelwerk | Sparte |
|---|---|---|---|
| [Lieferbeginn](/prozessdoku/202610/LF--LFN/GPKE-Teil2-lieferbeginn) | LFN | GPKE Teil 2 | Strom |
| [Neuanlage](/prozessdoku/202610/LF/GPKE-Teil2-neuanlage) | LF | GPKE Teil 2 | Strom |
| [Lieferbeginn](/prozessdoku/202610/LF--LFN/geli-gas-2-0-lieferbeginn) | LFN | GeLi Gas 2.0 | Gas |

## Transaktionsdaten

Der Umschlag der Nachricht. Pflichtfelder müssen beim Trigger-Aufruf gesetzt sein.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| [kategorie](/bo4e/202610/cdoc/Transaktionsdaten#kategorie) | string | **ja** | Qualifier aus dem Beginn der EDIFact Nachricht / BGM |
| [sparte](/bo4e/202610/cdoc/Transaktionsdaten#sparte) | [Enum Sparte](/bo4e/202610/enum/Sparte) | **ja** | Enthält Informationen über die Sparte Werte: `STROM`, `GAS`, `FERNWAERME`, `NAHWAERME`, `WASSER`, `ABWASSER` |
| [transaktionsgrund](/bo4e/202610/cdoc/Transaktionsdaten#transaktionsgrund) | string | **ja** | Der Transaktionsgrund beschreibt den Geschäftsvorfall zur Kategorie genauer / UTILMD STS+7++###+ZW4+E03 |
| [transaktionsgrundergaenzung](/bo4e/202610/cdoc/Transaktionsdaten#transaktionsgrundergaenzung) | string | **ja** | Ergänzung zum Transaktionsgrund / UTILMD STS+7++E01+###+E03 |
| [vertragsbeginn](/bo4e/202610/cdoc/Transaktionsdaten#vertragsbeginn) | string (date-time) | **ja** | Datum Vertragsbeginn / DTM+92 |
| `pruefidentifikator` | — | nein | Wird dynamisch im Event-Prozess ermittelt (Entscheidungsgrundlage: energierichtung, sparte, transaktionsgrund). Ein vom Sender mitgegebener Wert wird ignoriert. Im Topic mögliche Prüfis — 44001, 55001, 55077, 55600, 55601. Mögliche Werte: `44001`, `55001`, `55077`, `55600`, `55601` |
| [absender › rollencodenummer](/bo4e/202610/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |
| [empfaenger › marktrolle](/bo4e/202610/bo/Marktteilnehmer#marktrolle) | [Enum Marktrolle](/bo4e/202610/enum/Marktrolle) | nein | Gibt im Klartext die Bezeichnung der Marktrolle an. Werte: `NB`, `LF`, `MSB`, `MSBA`, `GMSB`, `MDL`, `DL`, `BKV`, `UENB`, `KUNDE-SELBST-NN` … (+9) |
| [empfaenger › rollencodenummer](/bo4e/202610/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |

## Zusatzdaten

`eventname` ist auf **START_LIEFERBEGINN** festgelegt. Dieser Wert bleibt auch in der englischen Fassung deutsch, weil Camunda darüber korreliert.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `prozessId` | string | **ja** | — |
| `eventname` | const `START_LIEFERBEGINN` | **ja** | — |

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
