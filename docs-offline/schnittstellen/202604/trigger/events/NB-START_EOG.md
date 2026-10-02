# [NB] START_EOG
<span hidden data-pagefind-meta={"title:Trigger-Ereignis START_EOG — Marktrolle NB (FV 202604)"} />

Marktrolle **NB** · Formatversion **202604** · BO4E-Schema **1.7.8**

## Stammdaten

Unter diesem Topic ist genau einer der folgenden 2 Prüfidentifikatoren zulässig — welcher, entscheidet der Event-Prozess.

| Prüfi | Scope | Anwendungsfall | Festlegung | Kommunikation |
|---|---|---|---|---|
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | UTILMD_GAS | Anmeldung EoG | GeLi Gas 2.0 | NB → LF (entspricht E/G) |
| [PI_55013](/schnittstellen/202604/pruefi/UTILMD/PI_55013) | UTILMD | Anmeldung / Zuordnung EOG | GPKE Teil 2 | NB → LF (Notiz "entspricht E/G") |

Die Stammdaten der 2 Prüfidentifikatoren in **einer** Struktur — eine Spalte je Prüfidentifikator, wie im Anwendungshandbuch. Ein Wert in der Spalte heißt, dass das Feld zu diesem Prüfidentifikator gehört: **Muss**, wenn seine Spezifikation es verlangt, sonst **Kann**. Eine leere Zelle heißt »gehört nicht dazu«, nicht »unbekannt«. Vorausgewählt ist der erste; die übrigen schaltet die Leiste über der Tabelle zu.

<Handbuchsatz>

<div className="maco-tabellenrahmen">

| Struktur (BO4E) | Beschreibung | Format | <span className="hbs-p" title="Anmeldung EoG">44013</span> | <span className="hbs-p" title="Anmeldung / Zuordnung EOG">55013</span> | Bedingung |
|---|---|---|---|---|---|
| <span className="hbs-g hbs-e0">**stammdaten**</span> | — | object | Kann | Kann | — |
| <span className="hbs-g hbs-e1">**BILANZIERUNG** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | Muss | — |
| <span className="hbs-f hbs-e2">[bilanzierungsbeginn](/bo4e/202604/bo/Bilanzierung#bilanzierungsbeginn)</span><span className="hbs-nr">00010</span> | Inklusiver Start der Bilanzierung | string (date-time) | Kann | — | — |
| <span className="hbs-f hbs-e2">[bilanzierungsende](/bo4e/202604/bo/Bilanzierung#bilanzierungsende)</span><span className="hbs-nr">00020</span> | Exklusives Ende der Bilanzierung | string (date-time) | Kann | — | — |
| <span className="hbs-f hbs-e2">[fallgruppenzuordnung](/bo4e/202604/bo/Bilanzierung#fallgruppenzuordnung)</span><span className="hbs-nr">00030</span> | Fallgruppenzuordnung (für gas RLM) | [Enum Fallgruppenzuordnung](/bo4e/202604/enum/Fallgruppenzuordnung) | Kann | — | — |
| <span className="hbs-w hbs-e3">`GABI_RLMmT`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`GABI_RLMoT`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`GABI_RLMNEV`</span> | — | — | Kann | — | — |
| <span className="hbs-f hbs-e2">[prognosegrundlage](/bo4e/202604/bo/Bilanzierung#prognosegrundlage) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00040</span> | Prognosegrundlage | [Enum Prognosegrundlage](/bo4e/202604/enum/Prognosegrundlage) | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`WERTE`</span> | — | — | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`PROFILE`</span> | — | — | Muss | Muss | — |
| <span className="hbs-g hbs-e2">**bilanzkreise** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — | — |
| <span className="hbs-f hbs-e3">[bezeichnung](/bo4e/202604/bo/Bilanzkreis#bezeichnung)</span><span className="hbs-nr">00050</span> | Externe Bezeichnung | string | Kann | — | — |
| <span className="hbs-g hbs-e2">**jahresverbrauchsprognose**</span> | — | object | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[einheit](/bo4e/202604/com/Menge#einheit)</span><span className="hbs-nr">00060</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202604/enum/Mengeneinheit) | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`W`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`WH`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`KW`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`KWH`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`KVARH`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`MW`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`MWH`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`STUECK`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`KUBIKMETER`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`STUNDE`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`TAG`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`MONAT`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`JAHR`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`PROZENT`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`ANZAHL`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`VAR`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`KVAR`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`VARH`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`KWHK`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`Z16`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`KWT`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`WATT_PRO_QUADRATMETER`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`METER_PRO_SEKUNDE`</span> | — | — | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[wert](/bo4e/202604/com/Menge#wert)</span><span className="hbs-nr">00070</span> | Wert | number (float) | Kann | Kann | — |
| <span className="hbs-g hbs-e2">**kundenwert**</span> | — | object | Kann | — | — |
| <span className="hbs-f hbs-e3">[wert](/bo4e/202604/com/Menge#wert)</span><span className="hbs-nr">00080</span> | Wert | number (float) | Kann | — | — |
| <span className="hbs-g hbs-e2">**lastprofile** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — | — |
| <span className="hbs-f hbs-e3">[bezeichnung](/bo4e/202604/com/Lastprofil#bezeichnung)</span><span className="hbs-nr">00090</span> | Bezeichnung des Profils | string | Kann | — | — |
| <span className="hbs-f hbs-e3">[herausgeber](/bo4e/202604/com/Lastprofil#herausgeber)</span><span className="hbs-nr">00100</span> | Herausgeber des Lastprofils | string | Kann | — | — |
| <span className="hbs-f hbs-e3">[verfahren](/bo4e/202604/com/Lastprofil#verfahren)</span><span className="hbs-nr">00110</span> | Profilverfahren | [Enum Profilverfahren](/bo4e/202604/enum/Profilverfahren) | Kann | — | — |
| <span className="hbs-w hbs-e4">`SYNTHETISCH`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`ANALYTISCH`</span> | — | — | Kann | — | — |
| <span className="hbs-g hbs-e3">**tagesparameter**</span> | — | object | Kann | — | — |
| <span className="hbs-f hbs-e4">[dienstanbieter](/bo4e/202604/com/Tagesparameter#dienstanbieter)</span><span className="hbs-nr">00120</span> | dienstanbieter | string | Kann | — | — |
| <span className="hbs-f hbs-e4">[herausgeber](/bo4e/202604/com/Tagesparameter#herausgeber)</span><span className="hbs-nr">00130</span> | Herausgeber | [Enum Herausgeber](/bo4e/202604/enum/Herausgeber) | Kann | — | — |
| <span className="hbs-w hbs-e5">`NB`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`BDEW`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`TUM`</span> | — | — | Kann | — | — |
| <span className="hbs-f hbs-e4">[klimazone](/bo4e/202604/com/Tagesparameter#klimazone)</span><span className="hbs-nr">00140</span> | klimazone | string | Kann | — | — |
| <span className="hbs-f hbs-e4">[temperaturmessstelle](/bo4e/202604/com/Tagesparameter#temperaturmessstelle)</span><span className="hbs-nr">00150</span> | temperaturmessstelle | string | Kann | — | — |
| <span className="hbs-f hbs-e2">[detailsPrognosegrundlage](/bo4e/202604/bo/Bilanzierung#detailsprognosegrundlage)</span><span className="hbs-nr">00160</span> | Prognosegrundlage - Besteht der Bedarf ein tagesparameteräbhängiges Lastprofil mit gemeinsamer Messung anzugeben, so ist dies über die 2 -malige Wiederholung des CAV Segments mit der Angabe der Codes E02 und E14 möglich. | array | — | Kann | — |
| <span className="hbs-g hbs-e2">**temperaturarbeit**</span> | — | object | — | Kann | — |
| <span className="hbs-f hbs-e3">[einheit](/bo4e/202604/com/Menge#einheit)</span><span className="hbs-nr">00170</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202604/enum/Mengeneinheit) | — | Kann | — |
| <span className="hbs-w hbs-e4">`W`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`WH`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`KW`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`KWH`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`KVARH`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MW`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MWH`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`STUECK`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`KUBIKMETER`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`STUNDE`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`TAG`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MONAT`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`JAHR`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`PROZENT`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`ANZAHL`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`VAR`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`KVAR`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`VARH`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`KWHK`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`Z16`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`KWT`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`WATT_PRO_QUADRATMETER`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`METER_PRO_SEKUNDE`</span> | — | — | — | Kann | — |
| <span className="hbs-f hbs-e3">[wert](/bo4e/202604/com/Menge#wert)</span><span className="hbs-nr">00180</span> | Wert | number (float) | — | Kann | — |
| <span className="hbs-g hbs-e1">**ENERGIELIEFERVERTRAG** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | Kann | — |
| <span className="hbs-g hbs-e2">**korrespondenzpartner**</span> | — | object | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[anrede](/bo4e/202604/bo/Geschaeftspartner#anrede)</span><span className="hbs-nr">00190</span> | Die Anrede für den GePa, Z.B. Herr. | string | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[gewerbekennzeichnung](/bo4e/202604/bo/Geschaeftspartner#gewerbekennzeichnung)</span><span className="hbs-nr">00200</span> | Kennzeichnung ob es sich um einen Gewerbe/Unternehmen (gewerbeKennzeichnung = true)<br/>oder eine Privatperson handelt. (gewerbeKennzeichnung = false) | boolean | Kann | — | — |
| <span className="hbs-f hbs-e3">[name1](/bo4e/202604/bo/Geschaeftspartner#name1)</span><span className="hbs-nr">00210</span> | Erster Teil des Namens. Hier kann der Firmenname oder bei Privatpersonen<br/>beispielsweise der Nachname dargestellt werden. Beispiele: Yellow Strom GmbH<br/>oder Hagen | string | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[name2](/bo4e/202604/bo/Geschaeftspartner#name2)</span><span className="hbs-nr">00220</span> | Zweiter Teil des Namens. Hier kann der eine Erweiterung zum Firmennamen oder<br/>bei Privatpersonen beispielsweise der Vorname dargestellt werden. Beispiele:<br/>Bereich Süd oder Nina | string | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[name3](/bo4e/202604/bo/Geschaeftspartner#name3)</span><span className="hbs-nr">00230</span> | Dritter Teil des Namens. Hier können weitere Ergänzungen zum Firmennamen oder<br/>bei Privatpersonen Zusätze zum Namen dargestellt werden. Beispiele: und Afrika<br/>oder Sängerin | string | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[name4](/bo4e/202604/bo/Geschaeftspartner#name4)</span><span className="hbs-nr">00240</span> | name4 | string | Kann | Kann | — |
| <span className="hbs-g hbs-e3">**partneradresse**</span> | — | object | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[hausnummer](/bo4e/202604/com/Adresse#hausnummer)</span><span className="hbs-nr">00250</span> | Hausnummer und Ergänzung | string | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[landescode](/bo4e/202604/com/Adresse#landescode)</span><span className="hbs-nr">00260</span> | Landescode | [Enum Landescode](/bo4e/202604/enum/Landescode) | Kann | Kann | — |
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
| <span className="hbs-f hbs-e4">[ort](/bo4e/202604/com/Adresse#ort)</span><span className="hbs-nr">00270</span> | Ort | string | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[ortsteil](/bo4e/202604/com/Adresse#ortsteil)</span><span className="hbs-nr">00280</span> | Ortsteil | string | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[postfach](/bo4e/202604/com/Adresse#postfach)</span><span className="hbs-nr">00290</span> | Postfach | string | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[postleitzahl](/bo4e/202604/com/Adresse#postleitzahl)</span><span className="hbs-nr">00300</span> | Postleitzahl | string | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[strasse](/bo4e/202604/com/Adresse#strasse)</span><span className="hbs-nr">00310</span> | Strasse | string | Kann | Kann | — |
| <span className="hbs-g hbs-e2">**vertragspartner2** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[anrede](/bo4e/202604/bo/Geschaeftspartner#anrede)</span><span className="hbs-nr">00320</span> | Die Anrede für den GePa, Z.B. Herr. | string | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[gewerbekennzeichnung](/bo4e/202604/bo/Geschaeftspartner#gewerbekennzeichnung)</span><span className="hbs-nr">00330</span> | Kennzeichnung ob es sich um einen Gewerbe/Unternehmen (gewerbeKennzeichnung = true)<br/>oder eine Privatperson handelt. (gewerbeKennzeichnung = false) | boolean | Kann | — | — |
| <span className="hbs-f hbs-e3">[name1](/bo4e/202604/bo/Geschaeftspartner#name1)</span><span className="hbs-nr">00340</span> | Erster Teil des Namens. Hier kann der Firmenname oder bei Privatpersonen<br/>beispielsweise der Nachname dargestellt werden. Beispiele: Yellow Strom GmbH<br/>oder Hagen | string | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[name2](/bo4e/202604/bo/Geschaeftspartner#name2)</span><span className="hbs-nr">00350</span> | Zweiter Teil des Namens. Hier kann der eine Erweiterung zum Firmennamen oder<br/>bei Privatpersonen beispielsweise der Vorname dargestellt werden. Beispiele:<br/>Bereich Süd oder Nina | string | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[name3](/bo4e/202604/bo/Geschaeftspartner#name3)</span><span className="hbs-nr">00360</span> | Dritter Teil des Namens. Hier können weitere Ergänzungen zum Firmennamen oder<br/>bei Privatpersonen Zusätze zum Namen dargestellt werden. Beispiele: und Afrika<br/>oder Sängerin | string | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[name4](/bo4e/202604/bo/Geschaeftspartner#name4)</span><span className="hbs-nr">00370</span> | name4 | string | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[geschaeftspartnerrolle](/bo4e/202604/bo/Geschaeftspartner#geschaeftspartnerrolle)</span><span className="hbs-nr">00380</span> | Rolle, die der Geschäftspartner hat (z.B. Interessent, Kunde). | array | — | Kann | — |
| <span className="hbs-g hbs-e1">**MARKTLOKATION** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | Muss | — |
| <span className="hbs-f hbs-e2">[marktgebiet](/bo4e/202604/bo/Marktlokation#marktgebiet) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00390</span> | für EDIFACT mapping | string | Muss | — | — |
| <span className="hbs-f hbs-e2">[marktlokationsId](/bo4e/202604/bo/Marktlokation#marktlokationsid) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00400</span> | Identifikationsnummer einer Marktlokation, an der Energie entweder<br/>verbraucht, oder erzeugt wird | string | Muss | Muss | — |
| <span className="hbs-f hbs-e2">[netzebene](/bo4e/202604/bo/Marktlokation#netzebene) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00410</span> | Netzebene, in der der Bezug der Energie erfolgt. Bei Strom Spannungsebene der<br/>Lieferung, bei Gas Druckstufe. Beispiel Strom: Niederspannung Beispiel Gas:<br/>Niederdruck. | [Enum Netzebene](/bo4e/202604/enum/Netzebene) | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`NSP`</span> | — | — | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`MSP`</span> | — | — | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`HSP`</span> | — | — | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`HSS`</span> | — | — | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`MSP_NSP_UMSP`</span> | — | — | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`HSP_MSP_UMSP`</span> | — | — | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`HSS_HSP_UMSP`</span> | — | — | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`HD`</span> | — | — | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`MD`</span> | — | — | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`ND`</span> | — | — | Muss | Muss | — |
| <span className="hbs-f hbs-e2">[sperrstatus](/bo4e/202604/bo/Marktlokation#sperrstatus) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00420</span> | Sperrstatus | [Enum Sperrstatus](/bo4e/202604/enum/Sperrstatus) | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`ENTSPERRT`</span> | — | — | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`GESPERRT`</span> | — | — | Muss | Muss | — |
| <span className="hbs-g hbs-e2">**eigentuemer**</span> | — | object | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[anrede](/bo4e/202604/bo/Geschaeftspartner#anrede)</span><span className="hbs-nr">00430</span> | Die Anrede für den GePa, Z.B. Herr. | string | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[gewerbekennzeichnung](/bo4e/202604/bo/Geschaeftspartner#gewerbekennzeichnung)</span><span className="hbs-nr">00440</span> | Kennzeichnung ob es sich um einen Gewerbe/Unternehmen (gewerbeKennzeichnung = true)<br/>oder eine Privatperson handelt. (gewerbeKennzeichnung = false) | boolean | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[name1](/bo4e/202604/bo/Geschaeftspartner#name1)</span><span className="hbs-nr">00450</span> | Erster Teil des Namens. Hier kann der Firmenname oder bei Privatpersonen<br/>beispielsweise der Nachname dargestellt werden. Beispiele: Yellow Strom GmbH<br/>oder Hagen | string | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[name2](/bo4e/202604/bo/Geschaeftspartner#name2)</span><span className="hbs-nr">00460</span> | Zweiter Teil des Namens. Hier kann der eine Erweiterung zum Firmennamen oder<br/>bei Privatpersonen beispielsweise der Vorname dargestellt werden. Beispiele:<br/>Bereich Süd oder Nina | string | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[name3](/bo4e/202604/bo/Geschaeftspartner#name3)</span><span className="hbs-nr">00470</span> | Dritter Teil des Namens. Hier können weitere Ergänzungen zum Firmennamen oder<br/>bei Privatpersonen Zusätze zum Namen dargestellt werden. Beispiele: und Afrika<br/>oder Sängerin | string | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[name4](/bo4e/202604/bo/Geschaeftspartner#name4)</span><span className="hbs-nr">00480</span> | name4 | string | Kann | Kann | — |
| <span className="hbs-g hbs-e3">**partneradresse**</span> | — | object | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[hausnummer](/bo4e/202604/com/Adresse#hausnummer)</span><span className="hbs-nr">00490</span> | Hausnummer und Ergänzung | string | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[landescode](/bo4e/202604/com/Adresse#landescode)</span><span className="hbs-nr">00500</span> | Landescode | [Enum Landescode](/bo4e/202604/enum/Landescode) | Kann | Kann | — |
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
| <span className="hbs-f hbs-e4">[ort](/bo4e/202604/com/Adresse#ort)</span><span className="hbs-nr">00510</span> | Ort | string | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[ortsteil](/bo4e/202604/com/Adresse#ortsteil)</span><span className="hbs-nr">00520</span> | Ortsteil | string | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[postfach](/bo4e/202604/com/Adresse#postfach)</span><span className="hbs-nr">00530</span> | Postfach | string | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[postleitzahl](/bo4e/202604/com/Adresse#postleitzahl)</span><span className="hbs-nr">00540</span> | Postleitzahl | string | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[strasse](/bo4e/202604/com/Adresse#strasse)</span><span className="hbs-nr">00550</span> | Strasse | string | Kann | Kann | — |
| <span className="hbs-g hbs-e2">**hausverwalter**</span> | — | object | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[anrede](/bo4e/202604/bo/Geschaeftspartner#anrede)</span><span className="hbs-nr">00560</span> | Die Anrede für den GePa, Z.B. Herr. | string | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[gewerbekennzeichnung](/bo4e/202604/bo/Geschaeftspartner#gewerbekennzeichnung)</span><span className="hbs-nr">00570</span> | Kennzeichnung ob es sich um einen Gewerbe/Unternehmen (gewerbeKennzeichnung = true)<br/>oder eine Privatperson handelt. (gewerbeKennzeichnung = false) | boolean | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[name1](/bo4e/202604/bo/Geschaeftspartner#name1)</span><span className="hbs-nr">00580</span> | Erster Teil des Namens. Hier kann der Firmenname oder bei Privatpersonen<br/>beispielsweise der Nachname dargestellt werden. Beispiele: Yellow Strom GmbH<br/>oder Hagen | string | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[name2](/bo4e/202604/bo/Geschaeftspartner#name2)</span><span className="hbs-nr">00590</span> | Zweiter Teil des Namens. Hier kann der eine Erweiterung zum Firmennamen oder<br/>bei Privatpersonen beispielsweise der Vorname dargestellt werden. Beispiele:<br/>Bereich Süd oder Nina | string | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[name3](/bo4e/202604/bo/Geschaeftspartner#name3)</span><span className="hbs-nr">00600</span> | Dritter Teil des Namens. Hier können weitere Ergänzungen zum Firmennamen oder<br/>bei Privatpersonen Zusätze zum Namen dargestellt werden. Beispiele: und Afrika<br/>oder Sängerin | string | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[name4](/bo4e/202604/bo/Geschaeftspartner#name4)</span><span className="hbs-nr">00610</span> | name4 | string | Kann | Kann | — |
| <span className="hbs-g hbs-e3">**partneradresse**</span> | — | object | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[hausnummer](/bo4e/202604/com/Adresse#hausnummer)</span><span className="hbs-nr">00620</span> | Hausnummer und Ergänzung | string | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[landescode](/bo4e/202604/com/Adresse#landescode)</span><span className="hbs-nr">00630</span> | Landescode | [Enum Landescode](/bo4e/202604/enum/Landescode) | Kann | Kann | — |
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
| <span className="hbs-f hbs-e4">[ort](/bo4e/202604/com/Adresse#ort)</span><span className="hbs-nr">00640</span> | Ort | string | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[ortsteil](/bo4e/202604/com/Adresse#ortsteil)</span><span className="hbs-nr">00650</span> | Ortsteil | string | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[postfach](/bo4e/202604/com/Adresse#postfach)</span><span className="hbs-nr">00660</span> | Postfach | string | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[postleitzahl](/bo4e/202604/com/Adresse#postleitzahl)</span><span className="hbs-nr">00670</span> | Postleitzahl | string | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[strasse](/bo4e/202604/com/Adresse#strasse)</span><span className="hbs-nr">00680</span> | Strasse | string | Kann | Kann | — |
| <span className="hbs-g hbs-e2">**lokationsadresse**</span> | — | object | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[hausnummer](/bo4e/202604/com/Adresse#hausnummer)</span><span className="hbs-nr">00690</span> | Hausnummer und Ergänzung | string | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[landescode](/bo4e/202604/com/Adresse#landescode)</span><span className="hbs-nr">00700</span> | Landescode | [Enum Landescode](/bo4e/202604/enum/Landescode) | Kann | Kann | — |
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
| <span className="hbs-f hbs-e3">[ort](/bo4e/202604/com/Adresse#ort)</span><span className="hbs-nr">00710</span> | Ort | string | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[ortsteil](/bo4e/202604/com/Adresse#ortsteil)</span><span className="hbs-nr">00720</span> | Ortsteil | string | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[postfach](/bo4e/202604/com/Adresse#postfach)</span><span className="hbs-nr">00730</span> | Postfach | string | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[postleitzahl](/bo4e/202604/com/Adresse#postleitzahl)</span><span className="hbs-nr">00740</span> | Postleitzahl | string | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[strasse](/bo4e/202604/com/Adresse#strasse)</span><span className="hbs-nr">00750</span> | Strasse | string | Kann | Kann | — |
| <span className="hbs-g hbs-e3">**zusatzInformation**</span> | — | object | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[zusatz1](/bo4e/202604/com/AdresszusatzInformation#zusatz1)</span><span className="hbs-nr">00760</span> | Adresszusatz 1 | string | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[zusatz2](/bo4e/202604/com/AdresszusatzInformation#zusatz2)</span><span className="hbs-nr">00770</span> | Adresszusatz 2 | string | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[zusatz3](/bo4e/202604/com/AdresszusatzInformation#zusatz3)</span><span className="hbs-nr">00780</span> | Adresszusatz 3 | string | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[zusatz4](/bo4e/202604/com/AdresszusatzInformation#zusatz4)</span><span className="hbs-nr">00790</span> | Adresszusatz 4 | string | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[zusatz5](/bo4e/202604/com/AdresszusatzInformation#zusatz5)</span><span className="hbs-nr">00800</span> | Adresszusatz 5 | string | Kann | Kann | — |
| <span className="hbs-g hbs-e2">**zaehlwerke** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | — | — |
| <span className="hbs-f hbs-e3">[obisKennzahl](/bo4e/202604/com/Zaehlwerk#obiskennzahl) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00810</span> | Die OBIS-Kennzahl für das Zählwerk, die festlegt, welche auf die gemessene Größe mit dem Stand gemeldet wird.<br/>Nur Zählwerkstände mit dieser OBIS-Kennzahl werden an diesem Zählwerk registriert. Beispiel:1-0:1.8.1 für<br/>elektrische Wirkarbeit. | string | Muss | — | — |
| <span className="hbs-f hbs-e3">[wertegranularitaet](/bo4e/202604/com/Zaehlwerk#wertegranularitaet)</span><span className="hbs-nr">00820</span> | Wertegranularitaet | [Enum Wertegranularitaet](/bo4e/202604/enum/Wertegranularitaet) | Kann | — | — |
| <span className="hbs-w hbs-e4">`JAEHRLICH`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`HALBJAEHRLICH`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`QUARTALSWEISE`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`MONATLICH`</span> | — | — | Kann | — | — |
| <span className="hbs-g hbs-e3">**konzessionsabgabe**</span> | — | object | Kann | — | — |
| <span className="hbs-f hbs-e4">[kategorie](/bo4e/202604/com/Konzessionsabgabe#kategorie)</span><span className="hbs-nr">00830</span> | Kategorie | string | Kann | — | — |
| <span className="hbs-f hbs-e4">[kosten](/bo4e/202604/com/Konzessionsabgabe#kosten)</span><span className="hbs-nr">00840</span> | Kosten | number (float) | Kann | — | — |
| <span className="hbs-f hbs-e4">[satz](/bo4e/202604/com/Konzessionsabgabe#satz)</span><span className="hbs-nr">00850</span> | Art der Konzessionsabgabe | [Enum AbgabeArt](/bo4e/202604/enum/AbgabeArt) | Kann | — | — |
| <span className="hbs-w hbs-e5">`KAS`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`SA`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`SAS`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`TA`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`TAS`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`TK`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`TKS`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`TS`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`TSS`</span> | — | — | Kann | — | — |
| <span className="hbs-g hbs-e2">**marktrollen** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | Kann | — |
| <span className="hbs-f hbs-e3">[marktrolle](/bo4e/202604/bo/Marktteilnehmer#marktrolle)</span><span className="hbs-nr">00860</span> | Gibt im Klartext die Bezeichnung der Marktrolle an. | [Enum Marktrolle](/bo4e/202604/enum/Marktrolle) | — | Kann | — |
| <span className="hbs-w hbs-e4">`NB`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`LF`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MSB`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MSBA`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`GMSB`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MDL`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`DL`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`BKV`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`UENB`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`KUNDE-SELBST-NN`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MGV`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`EIV`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`RB`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`KUNDE`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`INTERESSENT`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`KN`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`UBA`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`BIKO`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`ESA`</span> | — | — | — | Kann | — |
| <span className="hbs-f hbs-e3">[messstellenbetreiberEigenschaft](/bo4e/202604/bo/Marktteilnehmer#messstellenbetreibereigenschaft)</span><span className="hbs-nr">00870</span> | MSBEigenschaft | [Enum MSBEigenschaft](/bo4e/202604/enum/MSBEigenschaft) | — | Kann | — |
| <span className="hbs-w hbs-e4">`GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`WETTBEWERBLICHER_MESSSTELLENBETREIBER`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`AUFFANGMESSSTELLENBETREIBER`</span> | — | — | — | Kann | — |
| <span className="hbs-f hbs-e3">[rollencodenummer](/bo4e/202604/bo/Marktteilnehmer#rollencodenummer)</span><span className="hbs-nr">00880</span> | Gibt die Codenummer der Marktrolle an. | string | — | Kann | — |
| <span className="hbs-f hbs-e3">[weiterverpflichtet](/bo4e/202604/bo/Marktteilnehmer#weiterverpflichtet)</span><span className="hbs-nr">00890</span> | weiterverpflichtet | boolean | — | Kann | — |
| <span className="hbs-g hbs-e1">**MESSLOKATION** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | Kann | — |
| <span className="hbs-f hbs-e2">[gasqualitaet](/bo4e/202604/bo/Messlokation#gasqualitaet)</span><span className="hbs-nr">00900</span> | gasqualitaet für EDIFACT mapping | [Enum Gasqualitaet](/bo4e/202604/enum/Gasqualitaet) | Kann | — | — |
| <span className="hbs-w hbs-e3">`H_GAS`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`L_GAS`</span> | — | — | Kann | — | — |
| <span className="hbs-f hbs-e2">[messlokationsId](/bo4e/202604/bo/Messlokation#messlokationsid) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00910</span> | Die Messlokations-Identifikation. Das ist die frühere Zählpunktbezeichnung,<br/>z.B. DE 47108151234567 | string | Muss | Kann | — |
| <span className="hbs-g hbs-e2">**ablesekartenempfaenger**</span> | — | object | Kann | — | — |
| <span className="hbs-f hbs-e3">[anrede](/bo4e/202604/bo/Geschaeftspartner#anrede)</span><span className="hbs-nr">00920</span> | Die Anrede für den GePa, Z.B. Herr. | string | Kann | — | — |
| <span className="hbs-f hbs-e3">[gewerbekennzeichnung](/bo4e/202604/bo/Geschaeftspartner#gewerbekennzeichnung)</span><span className="hbs-nr">00930</span> | Kennzeichnung ob es sich um einen Gewerbe/Unternehmen (gewerbeKennzeichnung = true)<br/>oder eine Privatperson handelt. (gewerbeKennzeichnung = false) | boolean | Kann | — | — |
| <span className="hbs-f hbs-e3">[name1](/bo4e/202604/bo/Geschaeftspartner#name1)</span><span className="hbs-nr">00940</span> | Erster Teil des Namens. Hier kann der Firmenname oder bei Privatpersonen<br/>beispielsweise der Nachname dargestellt werden. Beispiele: Yellow Strom GmbH<br/>oder Hagen | string | Kann | — | — |
| <span className="hbs-f hbs-e3">[name2](/bo4e/202604/bo/Geschaeftspartner#name2)</span><span className="hbs-nr">00950</span> | Zweiter Teil des Namens. Hier kann der eine Erweiterung zum Firmennamen oder<br/>bei Privatpersonen beispielsweise der Vorname dargestellt werden. Beispiele:<br/>Bereich Süd oder Nina | string | Kann | — | — |
| <span className="hbs-f hbs-e3">[name3](/bo4e/202604/bo/Geschaeftspartner#name3)</span><span className="hbs-nr">00960</span> | Dritter Teil des Namens. Hier können weitere Ergänzungen zum Firmennamen oder<br/>bei Privatpersonen Zusätze zum Namen dargestellt werden. Beispiele: und Afrika<br/>oder Sängerin | string | Kann | — | — |
| <span className="hbs-f hbs-e3">[name4](/bo4e/202604/bo/Geschaeftspartner#name4)</span><span className="hbs-nr">00970</span> | name4 | string | Kann | — | — |
| <span className="hbs-g hbs-e3">**partneradresse**</span> | — | object | Kann | — | — |
| <span className="hbs-f hbs-e4">[hausnummer](/bo4e/202604/com/Adresse#hausnummer)</span><span className="hbs-nr">00980</span> | Hausnummer und Ergänzung | string | Kann | — | — |
| <span className="hbs-f hbs-e4">[landescode](/bo4e/202604/com/Adresse#landescode)</span><span className="hbs-nr">00990</span> | Landescode | [Enum Landescode](/bo4e/202604/enum/Landescode) | Kann | — | — |
| <span className="hbs-w hbs-e5">`AC`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`AD`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`AE`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`AF`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`AG`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`AI`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`AL`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`AM`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`AN`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`AO`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`AQ`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`AR`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`AS`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`AT`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`AU`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`AW`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`AX`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`AZ`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`BA`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`BB`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`BD`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`BE`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`BF`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`BG`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`BH`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`BI`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`BJ`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`BL`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`BM`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`BN`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`BO`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`BQ`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`BR`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`BS`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`BT`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`BU`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`BV`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`BW`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`BY`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`BZ`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`CA`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`CC`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`CD`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`CF`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`CG`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`CH`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`CI`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`CK`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`CL`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`CM`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`CN`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`CO`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`CP`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`CR`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`CS`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`CU`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`CV`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`CW`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`CX`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`CY`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`CZ`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`DE`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`DG`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`DJ`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`DK`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`DM`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`DO`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`DZ`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`EA`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`EC`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`EE`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`EG`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`EH`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`ER`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`ES`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`ET`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`EU`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`FI`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`FJ`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`FK`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`FM`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`FO`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`FR`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`FX`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`GA`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`GB`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`GD`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`GE`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`GF`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`GG`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`GH`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`GI`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`GL`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`GM`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`GN`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`GP`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`GQ`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`GR`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`GS`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`GT`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`GU`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`GW`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`GY`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`HK`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`HM`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`HN`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`HR`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`HT`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`HU`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`IC`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`ID`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`IE`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`IL`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`IM`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`IN`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`IO`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`IQ`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`IR`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`IS`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`IT`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`JE`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`JM`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`JO`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`JP`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`KE`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`KG`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`KH`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`KI`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`KM`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`KN`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`KP`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`KR`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`KW`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`KY`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`KZ`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`LA`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`LB`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`LC`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`LI`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`LK`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`LR`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`LS`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`LT`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`LU`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`LV`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`LY`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`MA`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`MC`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`MD`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`ME`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`MF`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`MG`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`MH`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`MK`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`ML`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`MM`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`MN`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`MO`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`MP`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`MQ`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`MR`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`MS`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`MT`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`MU`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`MV`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`MW`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`MX`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`MY`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`MZ`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`NA`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`NC`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`NE`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`NF`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`NG`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`NI`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`NL`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`NO`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`NP`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`NR`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`NT`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`NU`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`NZ`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`OM`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`PA`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`PE`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`PF`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`PG`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`PH`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`PK`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`PL`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`PM`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`PN`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`PR`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`PS`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`PT`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`PW`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`PY`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`QA`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`RE`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`RO`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`RS`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`RU`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`RW`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`SA`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`SB`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`SC`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`SD`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`SE`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`SF`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`SG`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`SH`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`SI`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`SJ`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`SK`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`SL`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`SM`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`SN`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`SO`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`SR`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`SS`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`ST`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`SU`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`SV`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`SX`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`SY`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`SZ`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`TA`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`TC`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`TD`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`TF`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`TG`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`TJ`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`TK`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`TL`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`TM`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`TN`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`TO`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`TP`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`TR`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`TT`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`TV`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`TW`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`TZ`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`UA`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`UG`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`UK`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`UM`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`US`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`UY`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`UZ`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`VA`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`VC`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`VE`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`VG`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`VI`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`VN`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`VU`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`WF`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`WS`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`XK`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`YE`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`YT`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`YU`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`ZA`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`ZM`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`ZR`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`ZW`</span> | — | — | Kann | — | — |
| <span className="hbs-f hbs-e4">[ort](/bo4e/202604/com/Adresse#ort)</span><span className="hbs-nr">01000</span> | Ort | string | Kann | — | — |
| <span className="hbs-f hbs-e4">[ortsteil](/bo4e/202604/com/Adresse#ortsteil)</span><span className="hbs-nr">01010</span> | Ortsteil | string | Kann | — | — |
| <span className="hbs-f hbs-e4">[postfach](/bo4e/202604/com/Adresse#postfach)</span><span className="hbs-nr">01020</span> | Postfach | string | Kann | — | — |
| <span className="hbs-f hbs-e4">[postleitzahl](/bo4e/202604/com/Adresse#postleitzahl)</span><span className="hbs-nr">01030</span> | Postleitzahl | string | Kann | — | — |
| <span className="hbs-f hbs-e4">[strasse](/bo4e/202604/com/Adresse#strasse)</span><span className="hbs-nr">01040</span> | Strasse | string | Kann | — | — |
| <span className="hbs-g hbs-e2">**marktrollen** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[marktrolle](/bo4e/202604/bo/Marktteilnehmer#marktrolle)</span><span className="hbs-nr">01050</span> | Gibt im Klartext die Bezeichnung der Marktrolle an. | [Enum Marktrolle](/bo4e/202604/enum/Marktrolle) | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`NB`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`LF`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`MSB`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`MSBA`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`GMSB`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`MDL`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`DL`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`BKV`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`UENB`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`KUNDE-SELBST-NN`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`MGV`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`EIV`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`RB`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`KUNDE`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`INTERESSENT`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`KN`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`UBA`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`BIKO`</span> | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`ESA`</span> | — | — | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[rollencodenummer](/bo4e/202604/bo/Marktteilnehmer#rollencodenummer)</span><span className="hbs-nr">01060</span> | Gibt die Codenummer der Marktrolle an. | string | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[weiterverpflichtet](/bo4e/202604/bo/Marktteilnehmer#weiterverpflichtet)</span><span className="hbs-nr">01070</span> | weiterverpflichtet | boolean | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[messstellenbetreiberEigenschaft](/bo4e/202604/bo/Marktteilnehmer#messstellenbetreibereigenschaft)</span><span className="hbs-nr">01080</span> | MSBEigenschaft | [Enum MSBEigenschaft](/bo4e/202604/enum/MSBEigenschaft) | — | Kann | — |
| <span className="hbs-w hbs-e4">`GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`WETTBEWERBLICHER_MESSSTELLENBETREIBER`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`AUFFANGMESSSTELLENBETREIBER`</span> | — | — | — | Kann | — |
| <span className="hbs-g hbs-e1">**NETZNUTZUNGSVERTRAG** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | Muss | — |
| <span className="hbs-f hbs-e2">[gemeinderabatt](/bo4e/202604/bo/Vertrag#gemeinderabatt) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">01090</span> | gemeinderabatt für EDIFACT mapping. | integer | Muss | — | — |
| <span className="hbs-f hbs-e2">[vertragsbeginn](/bo4e/202604/bo/Vertrag#vertragsbeginn)</span><span className="hbs-nr">01100</span> | Gibt an, wann der Vertrag beginnt. | string (date-time) | Kann | Kann | — |
| <span className="hbs-f hbs-e2">[vertragsende](/bo4e/202604/bo/Vertrag#vertragsende)</span><span className="hbs-nr">01110</span> | Gibt an, wann der Vertrag (voraussichtlich) endet oder beendet wurde. | string (date-time) | Kann | Kann | — |
| <span className="hbs-g hbs-e2">**korrespondenzpartner**</span> | — | object | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[anrede](/bo4e/202604/bo/Geschaeftspartner#anrede)</span><span className="hbs-nr">01120</span> | Die Anrede für den GePa, Z.B. Herr. | string | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[gewerbekennzeichnung](/bo4e/202604/bo/Geschaeftspartner#gewerbekennzeichnung)</span><span className="hbs-nr">01130</span> | Kennzeichnung ob es sich um einen Gewerbe/Unternehmen (gewerbeKennzeichnung = true)<br/>oder eine Privatperson handelt. (gewerbeKennzeichnung = false) | boolean | Kann | — | — |
| <span className="hbs-f hbs-e3">[name1](/bo4e/202604/bo/Geschaeftspartner#name1)</span><span className="hbs-nr">01140</span> | Erster Teil des Namens. Hier kann der Firmenname oder bei Privatpersonen<br/>beispielsweise der Nachname dargestellt werden. Beispiele: Yellow Strom GmbH<br/>oder Hagen | string | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[name2](/bo4e/202604/bo/Geschaeftspartner#name2)</span><span className="hbs-nr">01150</span> | Zweiter Teil des Namens. Hier kann der eine Erweiterung zum Firmennamen oder<br/>bei Privatpersonen beispielsweise der Vorname dargestellt werden. Beispiele:<br/>Bereich Süd oder Nina | string | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[name3](/bo4e/202604/bo/Geschaeftspartner#name3)</span><span className="hbs-nr">01160</span> | Dritter Teil des Namens. Hier können weitere Ergänzungen zum Firmennamen oder<br/>bei Privatpersonen Zusätze zum Namen dargestellt werden. Beispiele: und Afrika<br/>oder Sängerin | string | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[name4](/bo4e/202604/bo/Geschaeftspartner#name4)</span><span className="hbs-nr">01170</span> | name4 | string | Kann | Kann | — |
| <span className="hbs-g hbs-e3">**partneradresse**</span> | — | object | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[hausnummer](/bo4e/202604/com/Adresse#hausnummer)</span><span className="hbs-nr">01180</span> | Hausnummer und Ergänzung | string | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[landescode](/bo4e/202604/com/Adresse#landescode)</span><span className="hbs-nr">01190</span> | Landescode | [Enum Landescode](/bo4e/202604/enum/Landescode) | Kann | Kann | — |
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
| <span className="hbs-f hbs-e4">[ort](/bo4e/202604/com/Adresse#ort)</span><span className="hbs-nr">01200</span> | Ort | string | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[ortsteil](/bo4e/202604/com/Adresse#ortsteil)</span><span className="hbs-nr">01210</span> | Ortsteil | string | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[postfach](/bo4e/202604/com/Adresse#postfach)</span><span className="hbs-nr">01220</span> | Postfach | string | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[postleitzahl](/bo4e/202604/com/Adresse#postleitzahl)</span><span className="hbs-nr">01230</span> | Postleitzahl | string | Kann | Kann | — |
| <span className="hbs-f hbs-e4">[strasse](/bo4e/202604/com/Adresse#strasse)</span><span className="hbs-nr">01240</span> | Strasse | string | Kann | Kann | — |
| <span className="hbs-g hbs-e2">**vertragskonditionen** <span className="hbs-pflicht">\*</span></span> | — | object | Muss | Muss | — |
| <span className="hbs-f hbs-e3">[haushaltskunde](/bo4e/202604/com/Vertragskonditionen#haushaltskunde) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">01250</span> | haushaltskunde | boolean | Muss | Muss | — |
| <span className="hbs-f hbs-e3">[naechstenetznutzungsabrechnung](/bo4e/202604/com/Vertragskonditionen#naechstenetznutzungsabrechnung) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">01260</span> | naechstenetznutzungsabrechnung | string | Muss | — | — |
| <span className="hbs-f hbs-e3">[netznutzungsabrechnungIntervall](/bo4e/202604/com/Vertragskonditionen#netznutzungsabrechnungintervall) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">01270</span> | netznutzungsabrechnungIntervall | integer | Muss | — | — |
| <span className="hbs-f hbs-e3">[netznutzungsabrechnungsvariante](/bo4e/202604/com/Vertragskonditionen#netznutzungsabrechnungsvariante) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">01280</span> | Netznutzungsabrechnungsvariante | [Enum Netznutzungsabrechnungsvariante](/bo4e/202604/enum/Netznutzungsabrechnungsvariante) | Muss | — | — |
| <span className="hbs-w hbs-e4">`ARBEITSPREIS_GRUNDPREIS`</span> | — | — | Muss | — | — |
| <span className="hbs-w hbs-e4">`ARBEITSPREIS_LEISTUNGSPREIS`</span> | — | — | Muss | — | — |
| <span className="hbs-f hbs-e3">[netznutzungsvertrag](/bo4e/202604/com/Vertragskonditionen#netznutzungsvertrag) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">01290</span> | Netznutzungsvertrag | [Enum Netznutzungsvertrag](/bo4e/202604/enum/Netznutzungsvertrag) | Muss | — | — |
| <span className="hbs-w hbs-e4">`KUNDEN_NB`</span> | — | — | Muss | — | — |
| <span className="hbs-w hbs-e4">`LIEFERANTEN_NB`</span> | — | — | Muss | — | — |
| <span className="hbs-f hbs-e3">[netznutzungszahler](/bo4e/202604/com/Vertragskonditionen#netznutzungszahler) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">01300</span> | Netznutzungszahler | [Enum Netznutzungszahler](/bo4e/202604/enum/Netznutzungszahler) | Muss | — | — |
| <span className="hbs-w hbs-e4">`KUNDE`</span> | — | — | Muss | — | — |
| <span className="hbs-w hbs-e4">`LIEFERANT`</span> | — | — | Muss | — | — |
| <span className="hbs-f hbs-e3">[startAbrechnungsjahr](/bo4e/202604/com/Vertragskonditionen#startabrechnungsjahr)</span><span className="hbs-nr">01310</span> | startAbrechnungsjahr | string (date-time) | Kann | — | — |
| <span className="hbs-g hbs-e3">**netznutzungsabrechnung** <span className="hbs-pflicht">\*</span></span> | — | object | Muss | — | — |
| <span className="hbs-f hbs-e4">[abrechnungsZeitraum](/bo4e/202604/com/Zeitraum#abrechnungszeitraum) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">01320</span> | abrechnungsZeitraum | string | Muss | — | — |
| <span className="hbs-g hbs-e2">**vertragspartner2** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[anrede](/bo4e/202604/bo/Geschaeftspartner#anrede)</span><span className="hbs-nr">01330</span> | Die Anrede für den GePa, Z.B. Herr. | string | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[gewerbekennzeichnung](/bo4e/202604/bo/Geschaeftspartner#gewerbekennzeichnung)</span><span className="hbs-nr">01340</span> | Kennzeichnung ob es sich um einen Gewerbe/Unternehmen (gewerbeKennzeichnung = true)<br/>oder eine Privatperson handelt. (gewerbeKennzeichnung = false) | boolean | Kann | — | — |
| <span className="hbs-f hbs-e3">[name1](/bo4e/202604/bo/Geschaeftspartner#name1)</span><span className="hbs-nr">01350</span> | Erster Teil des Namens. Hier kann der Firmenname oder bei Privatpersonen<br/>beispielsweise der Nachname dargestellt werden. Beispiele: Yellow Strom GmbH<br/>oder Hagen | string | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[name2](/bo4e/202604/bo/Geschaeftspartner#name2)</span><span className="hbs-nr">01360</span> | Zweiter Teil des Namens. Hier kann der eine Erweiterung zum Firmennamen oder<br/>bei Privatpersonen beispielsweise der Vorname dargestellt werden. Beispiele:<br/>Bereich Süd oder Nina | string | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[name3](/bo4e/202604/bo/Geschaeftspartner#name3)</span><span className="hbs-nr">01370</span> | Dritter Teil des Namens. Hier können weitere Ergänzungen zum Firmennamen oder<br/>bei Privatpersonen Zusätze zum Namen dargestellt werden. Beispiele: und Afrika<br/>oder Sängerin | string | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[name4](/bo4e/202604/bo/Geschaeftspartner#name4)</span><span className="hbs-nr">01380</span> | name4 | string | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[geschaeftspartnerrolle](/bo4e/202604/bo/Geschaeftspartner#geschaeftspartnerrolle)</span><span className="hbs-nr">01390</span> | Rolle, die der Geschäftspartner hat (z.B. Interessent, Kunde). | array | — | Kann | — |
| <span className="hbs-g hbs-e1">**ZAEHLER** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — | — |
| <span className="hbs-f hbs-e2">[messlokationsId](/bo4e/202604/bo/Zaehler#messlokationsid)</span><span className="hbs-nr">01400</span> | messlokationsId | string | Kann | — | — |
| <span className="hbs-f hbs-e2">[messwerterfassung](/bo4e/202604/bo/Zaehler#messwerterfassung)</span><span className="hbs-nr">01410</span> | Messwerterfassung am Zählpunkt | [Enum Messwerterfassung](/bo4e/202604/enum/Messwerterfassung) | Kann | — | — |
| <span className="hbs-w hbs-e3">`FERNAUSLESBAR`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`MANUELL_AUSGELESENE`</span> | — | — | Kann | — | — |
| <span className="hbs-f hbs-e2">[zaehlergroesse](/bo4e/202604/bo/Zaehler#zaehlergroesse)</span><span className="hbs-nr">01420</span> | Zaehlergroesse | [Enum Geraetemerkmal](/bo4e/202604/enum/Geraetemerkmal) | Kann | — | — |
| <span className="hbs-w hbs-e3">`EINTARIF`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`ZWEITARIF`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`MEHRTARIF`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`GAS_G2P5`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`GAS_G4`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`GAS_G6`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`GAS_G10`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`GAS_G16`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`GAS_G25`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`GAS_G40`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`GAS_G65`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`GAS_G100`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`GAS_G160`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`GAS_G250`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`GAS_G350`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`GAS_G400`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`GAS_G4000`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`GAS_G650`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`GAS_G6500`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`GAS_G1000`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`GAS_G10000`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`GAS_G12500`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`GAS_G1600`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`GAS_G16000`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`GAS_G2500`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`IMPULSGEBER_G4_G100`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`IMPULSGEBER_G100`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`MODEM_GSM`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`MODEM_GPRS`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`MODEM_FUNK`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`MODEM_GSM_O_LG`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`MODEM_GSM_M_LG`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`MODEM_FESTNETZ`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`MODEM_GPRS_M_LG`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`PLC_COM`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`ETHERNET_KOM`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`DSL_KOM`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`LTE_KOM`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`RUNDSTEUEREMPFAENGER`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`TARIFSCHALTGERAET`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`ZUSTANDS_MU`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`TEMPERATUR_MU`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`KOMPAKT_MU`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`SYSTEM_MU`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`UNBESTIMMT`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`WASSER_MWZW`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`WASSER_WZWW`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`WASSER_WZ01`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`WASSER_WZ02`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`WASSER_WZ03`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`WASSER_WZ04`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`WASSER_WZ05`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`WASSER_WZ06`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`WASSER_WZ07`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`WASSER_WZ08`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`WASSER_WZ09`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`WASSER_WZ10`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`WASSER_VWZ04`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`WASSER_VWZ05`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`WASSER_VWZ06`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`WASSER_VWZ07`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`WASSER_VWZ10`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`DICHTEMENGENUMWERTER`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`TEMPERATURMENGENUMWERTER`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`ZUSTANDSMENGENUMWERTER`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`BLOCKSTROMWANDLER`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`MESSWANDLERSATZ_IMS_MME`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`KOMBIMESSWANDLER`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`SPANNUNGSWANDLER`</span> | — | — | Kann | — | — |
| <span className="hbs-f hbs-e2">[zaehlernummer](/bo4e/202604/bo/Zaehler#zaehlernummer)</span><span className="hbs-nr">01430</span> | Nummerierung des Zählers, vergeben durch den Messstellenbetreiber | string | Kann | — | — |
| <span className="hbs-f hbs-e2">[zaehlertyp](/bo4e/202604/bo/Zaehler#zaehlertyp)</span><span className="hbs-nr">01440</span> | Typisierung des Zählers | [Enum Zaehlertyp](/bo4e/202604/enum/Zaehlertyp) | Kann | — | — |
| <span className="hbs-w hbs-e3">`DREHSTROMZAEHLER`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`BALGENGASZAEHLER`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`DREHKOLBENZAEHLER`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`SMARTMETER`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`LEISTUNGSZAEHLER`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`MAXIMUMZAEHLER`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`TURBINENRADGASZAEHLER`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`ULTRASCHALLGASZAEHLER`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`WECHSELSTROMZAEHLER`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`WIRBELGASZAEHLER`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`MESSDATENREGISTRIERGERAET`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`ELEKTRONISCHERHAUSHALTSZAEHLER`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`SONDERAUSSTATTUNG`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`WASSERZAEHLER`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`MODERNEMESSEINRICHTUNG`</span> | — | — | Kann | — | — |
| <span className="hbs-f hbs-e2">[zaehlertypspezifikation](/bo4e/202604/bo/Zaehler#zaehlertypspezifikation)</span><span className="hbs-nr">01450</span> | Typisierung des Zählers (spezifikation für EHZ und MME) | [Enum ZaehlertypSpezifikation](/bo4e/202604/enum/ZaehlertypSpezifikation) | Kann | — | — |
| <span className="hbs-w hbs-e3">`EDL40`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`EDL21`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`SONSTIGER_EHZ`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`MME_STANDARD`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`MME_MEDA`</span> | — | — | Kann | — | — |
| <span className="hbs-g hbs-e2">**geraete** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — | — |
| <span className="hbs-f hbs-e3">[geraetenummer](/bo4e/202604/com/Geraet#geraetenummer)</span><span className="hbs-nr">01460</span> | Die auf dem Geräte aufgedruckte Nummer, die vom MSB vergeben wird. | string | Kann | — | — |
| <span className="hbs-g hbs-e3">**geraeteeigenschaften**</span> | — | object | Kann | — | — |
| <span className="hbs-f hbs-e4">[geraetemerkmal](/bo4e/202604/com/Geraeteeigenschaften#geraetemerkmal)</span><span className="hbs-nr">01470</span> | Geraetemerkmal | [Enum Geraetemerkmal](/bo4e/202604/enum/Geraetemerkmal) | Kann | — | — |
| <span className="hbs-w hbs-e5">`EINTARIF`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`ZWEITARIF`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`MEHRTARIF`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`GAS_G2P5`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`GAS_G4`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`GAS_G6`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`GAS_G10`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`GAS_G16`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`GAS_G25`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`GAS_G40`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`GAS_G65`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`GAS_G100`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`GAS_G160`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`GAS_G250`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`GAS_G350`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`GAS_G400`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`GAS_G4000`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`GAS_G650`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`GAS_G6500`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`GAS_G1000`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`GAS_G10000`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`GAS_G12500`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`GAS_G1600`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`GAS_G16000`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`GAS_G2500`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`IMPULSGEBER_G4_G100`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`IMPULSGEBER_G100`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`MODEM_GSM`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`MODEM_GPRS`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`MODEM_FUNK`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`MODEM_GSM_O_LG`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`MODEM_GSM_M_LG`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`MODEM_FESTNETZ`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`MODEM_GPRS_M_LG`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`PLC_COM`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`ETHERNET_KOM`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`DSL_KOM`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`LTE_KOM`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`RUNDSTEUEREMPFAENGER`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`TARIFSCHALTGERAET`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`ZUSTANDS_MU`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`TEMPERATUR_MU`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`KOMPAKT_MU`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`SYSTEM_MU`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`UNBESTIMMT`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`WASSER_MWZW`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`WASSER_WZWW`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`WASSER_WZ01`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`WASSER_WZ02`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`WASSER_WZ03`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`WASSER_WZ04`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`WASSER_WZ05`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`WASSER_WZ06`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`WASSER_WZ07`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`WASSER_WZ08`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`WASSER_WZ09`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`WASSER_WZ10`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`WASSER_VWZ04`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`WASSER_VWZ05`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`WASSER_VWZ06`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`WASSER_VWZ07`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`WASSER_VWZ10`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`DICHTEMENGENUMWERTER`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`TEMPERATURMENGENUMWERTER`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`ZUSTANDSMENGENUMWERTER`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`BLOCKSTROMWANDLER`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`MESSWANDLERSATZ_IMS_MME`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`KOMBIMESSWANDLER`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`SPANNUNGSWANDLER`</span> | — | — | Kann | — | — |
| <span className="hbs-g hbs-e2">**zaehlwerke** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — | — |
| <span className="hbs-f hbs-e3">[bezeichnung](/bo4e/202604/com/Zaehlwerk#bezeichnung)</span><span className="hbs-nr">01480</span> | Zusätzliche Bezeichnung, z.B. Zählwerk_Wirkarbeit. | string | Kann | — | — |
| <span className="hbs-f hbs-e3">[nachkommastelle](/bo4e/202604/com/Zaehlwerk#nachkommastelle)</span><span className="hbs-nr">01490</span> | nachkommastelle | integer | Kann | — | — |
| <span className="hbs-f hbs-e3">[obisKennzahl](/bo4e/202604/com/Zaehlwerk#obiskennzahl)</span><span className="hbs-nr">01500</span> | Die OBIS-Kennzahl für das Zählwerk, die festlegt, welche auf die gemessene Größe mit dem Stand gemeldet wird.<br/>Nur Zählwerkstände mit dieser OBIS-Kennzahl werden an diesem Zählwerk registriert. Beispiel:1-0:1.8.1 für<br/>elektrische Wirkarbeit. | string | Kann | — | — |
| <span className="hbs-f hbs-e3">[vorkommastelle](/bo4e/202604/com/Zaehlwerk#vorkommastelle)</span><span className="hbs-nr">01510</span> | vorkommastelle | integer | Kann | — | — |
| <span className="hbs-f hbs-e3">[wertegranularitaet](/bo4e/202604/com/Zaehlwerk#wertegranularitaet)</span><span className="hbs-nr">01520</span> | Wertegranularitaet | [Enum Wertegranularitaet](/bo4e/202604/enum/Wertegranularitaet) | Kann | — | — |
| <span className="hbs-w hbs-e4">`JAEHRLICH`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`HALBJAEHRLICH`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`QUARTALSWEISE`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`MONATLICH`</span> | — | — | Kann | — | — |
| <span className="hbs-g hbs-e1">**NETZLOKATION** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | Kann | — |
| <span className="hbs-f hbs-e2">[netzlokationsId](/bo4e/202604/bo/Netzlokation#netzlokationsid)</span><span className="hbs-nr">01530</span> | Identifikationsnummer einer Netzlokation, an der Energie entweder<br/>verbraucht, oder erzeugt wird (Like MarktlokationsId Marktlokation) | string | — | Kann | — |
| <span className="hbs-g hbs-e2">**marktrollen** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | Kann | — |
| <span className="hbs-f hbs-e3">[marktrolle](/bo4e/202604/bo/Marktteilnehmer#marktrolle)</span><span className="hbs-nr">01540</span> | Gibt im Klartext die Bezeichnung der Marktrolle an. | [Enum Marktrolle](/bo4e/202604/enum/Marktrolle) | — | Kann | — |
| <span className="hbs-w hbs-e4">`NB`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`LF`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MSB`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MSBA`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`GMSB`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MDL`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`DL`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`BKV`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`UENB`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`KUNDE-SELBST-NN`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MGV`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`EIV`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`RB`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`KUNDE`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`INTERESSENT`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`KN`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`UBA`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`BIKO`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`ESA`</span> | — | — | — | Kann | — |
| <span className="hbs-f hbs-e3">[messstellenbetreiberEigenschaft](/bo4e/202604/bo/Marktteilnehmer#messstellenbetreibereigenschaft)</span><span className="hbs-nr">01550</span> | MSBEigenschaft | [Enum MSBEigenschaft](/bo4e/202604/enum/MSBEigenschaft) | — | Kann | — |
| <span className="hbs-w hbs-e4">`GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`WETTBEWERBLICHER_MESSSTELLENBETREIBER`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`AUFFANGMESSSTELLENBETREIBER`</span> | — | — | — | Kann | — |
| <span className="hbs-f hbs-e3">[rollencodenummer](/bo4e/202604/bo/Marktteilnehmer#rollencodenummer)</span><span className="hbs-nr">01560</span> | Gibt die Codenummer der Marktrolle an. | string | — | Kann | — |
| <span className="hbs-g hbs-e1">**STEUERBARE_RESSOURCE** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | Kann | — |
| <span className="hbs-f hbs-e2">[ressourcenId](/bo4e/202604/bo/SteuerbareRessource#ressourcenid)</span><span className="hbs-nr">01570</span> | ressourcenId | string | — | Kann | — |
| <span className="hbs-g hbs-e2">**marktrollen** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | Kann | — |
| <span className="hbs-f hbs-e3">[marktrolle](/bo4e/202604/bo/Marktteilnehmer#marktrolle)</span><span className="hbs-nr">01580</span> | Gibt im Klartext die Bezeichnung der Marktrolle an. | [Enum Marktrolle](/bo4e/202604/enum/Marktrolle) | — | Kann | — |
| <span className="hbs-w hbs-e4">`NB`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`LF`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MSB`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MSBA`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`GMSB`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MDL`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`DL`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`BKV`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`UENB`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`KUNDE-SELBST-NN`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MGV`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`EIV`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`RB`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`KUNDE`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`INTERESSENT`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`KN`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`UBA`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`BIKO`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`ESA`</span> | — | — | — | Kann | — |
| <span className="hbs-f hbs-e3">[messstellenbetreiberEigenschaft](/bo4e/202604/bo/Marktteilnehmer#messstellenbetreibereigenschaft)</span><span className="hbs-nr">01590</span> | MSBEigenschaft | [Enum MSBEigenschaft](/bo4e/202604/enum/MSBEigenschaft) | — | Kann | — |
| <span className="hbs-w hbs-e4">`GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`WETTBEWERBLICHER_MESSSTELLENBETREIBER`</span> | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`AUFFANGMESSSTELLENBETREIBER`</span> | — | — | — | Kann | — |
| <span className="hbs-f hbs-e3">[rollencodenummer](/bo4e/202604/bo/Marktteilnehmer#rollencodenummer)</span><span className="hbs-nr">01600</span> | Gibt die Codenummer der Marktrolle an. | string | — | Kann | — |
| <span className="hbs-g hbs-e1">**TECHNISCHE_RESSOURCE** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | Kann | — |
| <span className="hbs-f hbs-e2">[ressourcenId](/bo4e/202604/bo/TechnischeRessource#ressourcenid)</span><span className="hbs-nr">01610</span> | ressourcenId | string | — | Kann | — |

</div>

</Handbuchsatz>

## Kette dieses Auslösers

Das Ereignis löst die Nachricht aus. Der Marktpartner antwortet mit einer der genannten Antworten, und danach schreibt die MACO APP den Vorgang in Ihr Backendsystem.

| Nachricht | Antworten | Schreibaufruf nach der Antwort |
|---|---|---|
| [44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | [44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014), [44015](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44015) | `POST /updateProcessData` |
| [55013](/schnittstellen/202604/pruefi/UTILMD/PI_55013) | [55014](/schnittstellen/202604/pruefi/UTILMD/PI_55014), [55015](/schnittstellen/202604/pruefi/UTILMD/PI_55015) | `POST /updateProcessData` |

Dieses Ereignis löst Schritte in diesen Rollensichten aus:

| Prozess | Beteiligter | Regelwerk | Sparte |
|---|---|---|---|
| [Beginn der Ersatz-/Grundversorgung](/prozessdoku/202604/NB/GPKE-Teil2-beginn-der-ersatz-grundversorgung) | NB | GPKE Teil 2 | Strom |
| [Beginn der Ersatz- / Grundversorgung](/prozessdoku/202604/NB/geli-gas-2-0-beginn-der-ersatz-grundversorgung) | NB | GeLi Gas 2.0 | Gas |

## Transaktionsdaten

Der Umschlag der Nachricht. Pflichtfelder müssen beim Trigger-Aufruf gesetzt sein.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| [kategorie](/bo4e/202604/cdoc/Transaktionsdaten#kategorie) | string | **ja** | Qualifier aus dem Beginn der EDIFact Nachricht / BGM |
| [sparte](/bo4e/202604/cdoc/Transaktionsdaten#sparte) | [Enum Sparte](/bo4e/202604/enum/Sparte) | **ja** | Enthält Informationen über die Sparte Werte: `STROM`, `GAS`, `FERNWAERME`, `NAHWAERME`, `WASSER`, `ABWASSER` |
| [transaktionsgrund](/bo4e/202604/cdoc/Transaktionsdaten#transaktionsgrund) | string | **ja** | Der Transaktionsgrund beschreibt den Geschäftsvorfall zur Kategorie genauer / UTILMD STS+7++###+ZW4+E03 |
| [transaktionsgrundergaenzung](/bo4e/202604/cdoc/Transaktionsdaten#transaktionsgrundergaenzung) | string | **ja** | Ergänzung zum Transaktionsgrund / UTILMD STS+7++E01+###+E03 |
| [transaktionsgrundergaenzungBefristeteAnmeldung](/bo4e/202604/cdoc/Transaktionsdaten#transaktionsgrundergaenzungbefristeteanmeldung) | string | **ja** | Ergänzung zum Transaktionsgrund bei befristeten An-/Abmeldungen / UTILMD STS+7++E01+ZW4+### |
| [vertragsbeginn](/bo4e/202604/cdoc/Transaktionsdaten#vertragsbeginn) | string (date-time) | **ja** | Datum Vertragsbeginn / DTM+92 |
| `pruefidentifikator` | — | nein | Wird dynamisch im Event-Prozess ermittelt (Entscheidungsgrundlage: sparte). Ein vom Sender mitgegebener Wert wird ignoriert. Im Topic mögliche Prüfis — 44013, 55013. Mögliche Werte: `44013`, `55013` |
| [absender › rollencodenummer](/bo4e/202604/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |
| [empfaenger › rollencodenummer](/bo4e/202604/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |

## Zusatzdaten

`eventname` ist auf **START_EOG** festgelegt. Dieser Wert bleibt auch in der englischen Fassung deutsch, weil Camunda darüber korreliert.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `prozessId` | string | **ja** | — |
| `eventname` | const `START_EOG` | **ja** | — |

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
