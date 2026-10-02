# [MSB] START_PARTIN
<span hidden data-pagefind-meta={"title:Trigger-Ereignis START_PARTIN — Marktrolle MSB (FV 202610)"} />

Marktrolle **MSB** · Formatversion **202610** · BO4E-Schema **1.7.8**

## Stammdaten

Unter diesem Topic ist genau einer der folgenden 1 Prüfidentifikatoren zulässig — welcher, entscheidet der Event-Prozess.

| Prüfi | Scope | Anwendungsfall | Festlegung | Kommunikation |
|---|---|---|---|---|
| [PI_37002](/schnittstellen/202610/pruefi/PARTIN/PI_37002) | PARTIN | Kommunikationsdaten des MSB Strom | GPKE Teil 4 | MSB → NB |

Die Stammdaten der 1 Prüfidentifikatoren in **einer** Struktur — eine Spalte je Prüfidentifikator, wie im Anwendungshandbuch. Ein Wert in der Spalte heißt, dass das Feld zu diesem Prüfidentifikator gehört: **Muss**, wenn seine Spezifikation es verlangt, sonst **Kann**. Eine leere Zelle heißt »gehört nicht dazu«, nicht »unbekannt«. Vorausgewählt ist der erste; die übrigen schaltet die Leiste über der Tabelle zu.

<Handbuchsatz>

<div className="maco-tabellenrahmen">

| Struktur (BO4E) | Beschreibung | Format | <span className="hbs-p" title="Kommunikationsdaten des MSB Strom">37002</span> | Bedingung |
|---|---|---|---|---|
| <span className="hbs-g hbs-e0">**stammdaten**</span> | — | object | Kann | — |
| <span className="hbs-g hbs-e1">**KOMMUNIKATIONSDATEN** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-f hbs-e2">[gueltigkeit](/bo4e/202610/bo/Kommunikationsdaten#gueltigkeit)</span><span className="hbs-nr">00010</span> | gueltigkeit | string (date-time) | Kann | — |
| <span className="hbs-f hbs-e2">[kommunikationsDatenBlattInaktiv](/bo4e/202610/bo/Kommunikationsdaten#kommunikationsdatenblattinaktiv)</span><span className="hbs-nr">00020</span> | kommunikationsDatenBlattInaktiv | boolean | Kann | — |
| <span className="hbs-g hbs-e2">**kommunikationsangaben** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-f hbs-e3">[anrede](/bo4e/202610/bo/Marktteilnehmer#anrede)</span><span className="hbs-nr">00030</span> | Die Anrede für den GePa, Z.B. Herr. | string | Kann | — |
| <span className="hbs-f hbs-e3">[kommunikationsrolle](/bo4e/202610/bo/Marktteilnehmer#kommunikationsrolle)</span><span className="hbs-nr">00040</span> | Kommunikationsrolle | [Enum Kommunikationsrolle](/bo4e/202610/enum/Kommunikationsrolle) | Kann | — |
| <span className="hbs-w hbs-e4">`DATENAUSTAUSCH`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`RAHMENVERTRAEGE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`KUENDIGUNGSPROZESSE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`WECHSELPROZESSE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`STAMMDATENPROZESSE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`EINSPEISEPROZESSE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`ABRECHNUNGSPROZESSE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MMMA_PROZESSE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`BEWEGUNGSDATEN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`ENT_SPERR_PROZESSE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`BILANZIERUNGSPROZESSE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`NETZANSCHLUSS_ANLAGEN`</span> | — | — | Kann | — |
| <span className="hbs-f hbs-e3">[name1](/bo4e/202610/bo/Marktteilnehmer#name1)</span><span className="hbs-nr">00050</span> | Erster Teil des Namens. Hier kann der Firmenname oder bei Privatpersonen<br/>beispielsweise der Nachname dargestellt werden. Beispiele: Yellow Strom GmbH<br/>oder Hagen | string | Kann | — |
| <span className="hbs-f hbs-e3">[name2](/bo4e/202610/bo/Marktteilnehmer#name2)</span><span className="hbs-nr">00060</span> | Zweiter Teil des Namens. Hier kann der eine Erweiterung zum Firmennamen oder<br/>bei Privatpersonen beispielsweise der Vorname dargestellt werden. Beispiele:<br/>Bereich Süd oder Nina | string | Kann | — |
| <span className="hbs-f hbs-e3">[name3](/bo4e/202610/bo/Marktteilnehmer#name3)</span><span className="hbs-nr">00070</span> | Dritter Teil des Namens. Hier können weitere Ergänzungen zum Firmennamen oder<br/>bei Privatpersonen Zusätze zum Namen dargestellt werden. Beispiele: und Afrika<br/>oder Sängerin | string | Kann | — |
| <span className="hbs-f hbs-e3">[name4](/bo4e/202610/bo/Marktteilnehmer#name4)</span><span className="hbs-nr">00080</span> | name4 | string | Kann | — |
| <span className="hbs-g hbs-e3">**ansprechpartner**</span> | — | object | Kann | — |
| <span className="hbs-f hbs-e4">[eMailAdresse](/bo4e/202610/bo/Ansprechpartner#emailadresse)</span><span className="hbs-nr">00090</span> | E-Mail Adresse | string | Kann | — |
| <span className="hbs-f hbs-e4">[nachname](/bo4e/202610/bo/Ansprechpartner#nachname)</span><span className="hbs-nr">00100</span> | Nachname (Familienname) des Ansprechpartners | string | Kann | — |
| <span className="hbs-g hbs-e4">**rufnummern** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-f hbs-e5">[nummerntyp](/bo4e/202610/com/Rufnummer#nummerntyp)</span><span className="hbs-nr">00110</span> | Rufnummernart | [Enum Rufnummernart](/bo4e/202610/enum/Rufnummernart) | Kann | — |
| <span className="hbs-w hbs-e5">`RUF_ZENTRALE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`FAX_ZENTRALE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`SAMMELRUF`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`SAMMELFAX`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`ABTEILUNGRUF`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`ABTEILUNGFAX`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`RUF_DURCHWAHL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`FAX_DURCHWAHL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MOBIL_NUMMER`</span> | — | — | Kann | — |
| <span className="hbs-f hbs-e5">[rufnummer](/bo4e/202610/com/Rufnummer#rufnummer)</span><span className="hbs-nr">00120</span> | rufnummer | string | Kann | — |
| <span className="hbs-g hbs-e3">**partneradresse**</span> | — | object | Kann | — |
| <span className="hbs-f hbs-e4">[hausnummer](/bo4e/202610/com/Adresse#hausnummer)</span><span className="hbs-nr">00130</span> | Hausnummer und Ergänzung | string | Kann | — |
| <span className="hbs-f hbs-e4">[landescode](/bo4e/202610/com/Adresse#landescode)</span><span className="hbs-nr">00140</span> | Landescode | [Enum Landescode](/bo4e/202610/enum/Landescode) | Kann | — |
| <span className="hbs-w hbs-e5">`AC`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`AD`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`AE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`AF`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`AG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`AI`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`AL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`AM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`AN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`AO`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`AQ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`AR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`AS`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`AT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`AU`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`AW`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`AX`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`AZ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`BA`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`BB`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`BD`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`BE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`BF`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`BG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`BH`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`BI`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`BJ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`BL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`BM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`BN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`BO`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`BQ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`BR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`BS`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`BT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`BU`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`BV`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`BW`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`BY`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`BZ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`CA`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`CC`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`CD`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`CF`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`CG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`CH`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`CI`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`CK`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`CL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`CM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`CN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`CO`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`CP`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`CR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`CS`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`CU`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`CV`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`CW`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`CX`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`CY`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`CZ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`DE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`DG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`DJ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`DK`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`DM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`DO`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`DZ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`EA`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`EC`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`EE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`EG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`EH`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`ER`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`ES`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`ET`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`EU`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`FI`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`FJ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`FK`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`FM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`FO`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`FR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`FX`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GA`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GB`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GD`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GF`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GH`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GI`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GP`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GQ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GS`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GU`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GW`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GY`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`HK`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`HM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`HN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`HR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`HT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`HU`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`IC`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`ID`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`IE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`IL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`IM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`IN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`IO`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`IQ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`IR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`IS`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`IT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`JE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`JM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`JO`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`JP`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`KE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`KG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`KH`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`KI`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`KM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`KN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`KP`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`KR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`KW`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`KY`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`KZ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`LA`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`LB`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`LC`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`LI`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`LK`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`LR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`LS`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`LT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`LU`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`LV`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`LY`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MA`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MC`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MD`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`ME`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MF`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MH`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MK`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`ML`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MO`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MP`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MQ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MS`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MU`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MV`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MW`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MX`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MY`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MZ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`NA`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`NC`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`NE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`NF`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`NG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`NI`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`NL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`NO`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`NP`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`NR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`NT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`NU`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`NZ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`OM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`PA`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`PE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`PF`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`PG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`PH`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`PK`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`PL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`PM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`PN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`PR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`PS`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`PT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`PW`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`PY`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`QA`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`RE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`RO`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`RS`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`RU`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`RW`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`SA`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`SB`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`SC`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`SD`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`SE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`SF`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`SG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`SH`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`SI`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`SJ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`SK`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`SL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`SM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`SN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`SO`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`SR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`SS`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`ST`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`SU`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`SV`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`SX`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`SY`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`SZ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`TA`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`TC`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`TD`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`TF`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`TG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`TJ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`TK`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`TL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`TM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`TN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`TO`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`TP`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`TR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`TT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`TV`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`TW`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`TZ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`UA`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`UG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`UK`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`UM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`US`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`UY`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`UZ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`VA`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`VC`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`VE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`VG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`VI`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`VN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`VU`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`WF`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`WS`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`XK`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`YE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`YT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`YU`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`ZA`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`ZM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`ZR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`ZW`</span> | — | — | Kann | — |
| <span className="hbs-f hbs-e4">[ort](/bo4e/202610/com/Adresse#ort)</span><span className="hbs-nr">00150</span> | Ort | string | Kann | — |
| <span className="hbs-f hbs-e4">[ortsteil](/bo4e/202610/com/Adresse#ortsteil)</span><span className="hbs-nr">00160</span> | Ortsteil | string | Kann | — |
| <span className="hbs-f hbs-e4">[postfach](/bo4e/202610/com/Adresse#postfach)</span><span className="hbs-nr">00170</span> | Postfach | string | Kann | — |
| <span className="hbs-f hbs-e4">[postleitzahl](/bo4e/202610/com/Adresse#postleitzahl)</span><span className="hbs-nr">00180</span> | Postleitzahl | string | Kann | — |
| <span className="hbs-f hbs-e4">[strasse](/bo4e/202610/com/Adresse#strasse)</span><span className="hbs-nr">00190</span> | Strasse | string | Kann | — |
| <span className="hbs-g hbs-e2">**marktteilnehmer**</span> | — | object | Kann | — |
| <span className="hbs-f hbs-e3">[amtsgericht](/bo4e/202610/bo/Marktteilnehmer#amtsgericht)</span><span className="hbs-nr">00200</span> | Amtsgericht bzw Handelsregistergericht, das die Handelsregisternummer herausgegeben hat | string | Kann | — |
| <span className="hbs-f hbs-e3">[anrede](/bo4e/202610/bo/Marktteilnehmer#anrede)</span><span className="hbs-nr">00210</span> | Die Anrede für den GePa, Z.B. Herr. | string | Kann | — |
| <span className="hbs-f hbs-e3">[faxnummer](/bo4e/202610/bo/Marktteilnehmer#faxnummer)</span><span className="hbs-nr">00220</span> | faxnummer | string | Kann | — |
| <span className="hbs-f hbs-e3">[gewerbekennzeichnung](/bo4e/202610/bo/Marktteilnehmer#gewerbekennzeichnung)</span><span className="hbs-nr">00230</span> | Kennzeichnung ob es sich um einen Gewerbe/Unternehmen (gewerbeKennzeichnung = true)<br/>oder eine Privatperson handelt. (gewerbeKennzeichnung = false) | boolean | Kann | — |
| <span className="hbs-f hbs-e3">[hrnummer](/bo4e/202610/bo/Marktteilnehmer#hrnummer)</span><span className="hbs-nr">00240</span> | Handelsregisternummer des Geschäftspartners | string | Kann | — |
| <span className="hbs-f hbs-e3">[marktrolle](/bo4e/202610/bo/Marktteilnehmer#marktrolle)</span><span className="hbs-nr">00250</span> | Gibt im Klartext die Bezeichnung der Marktrolle an. | [Enum Marktrolle](/bo4e/202610/enum/Marktrolle) | Kann | — |
| <span className="hbs-w hbs-e4">`NB`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`LF`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MSB`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MSBA`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`GMSB`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MDL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`DL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`BKV`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`UENB`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`KUNDE-SELBST-NN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MGV`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`EIV`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`RB`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`KUNDE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`INTERESSENT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`KN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`UBA`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`BIKO`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`ESA`</span> | — | — | Kann | — |
| <span className="hbs-f hbs-e3">[name1](/bo4e/202610/bo/Marktteilnehmer#name1)</span><span className="hbs-nr">00260</span> | Erster Teil des Namens. Hier kann der Firmenname oder bei Privatpersonen<br/>beispielsweise der Nachname dargestellt werden. Beispiele: Yellow Strom GmbH<br/>oder Hagen | string | Kann | — |
| <span className="hbs-f hbs-e3">[name2](/bo4e/202610/bo/Marktteilnehmer#name2)</span><span className="hbs-nr">00270</span> | Zweiter Teil des Namens. Hier kann der eine Erweiterung zum Firmennamen oder<br/>bei Privatpersonen beispielsweise der Vorname dargestellt werden. Beispiele:<br/>Bereich Süd oder Nina | string | Kann | — |
| <span className="hbs-f hbs-e3">[name3](/bo4e/202610/bo/Marktteilnehmer#name3)</span><span className="hbs-nr">00280</span> | Dritter Teil des Namens. Hier können weitere Ergänzungen zum Firmennamen oder<br/>bei Privatpersonen Zusätze zum Namen dargestellt werden. Beispiele: und Afrika<br/>oder Sängerin | string | Kann | — |
| <span className="hbs-f hbs-e3">[name4](/bo4e/202610/bo/Marktteilnehmer#name4)</span><span className="hbs-nr">00290</span> | name4 | string | Kann | — |
| <span className="hbs-f hbs-e3">[steuernummer](/bo4e/202610/bo/Marktteilnehmer#steuernummer)</span><span className="hbs-nr">00300</span> | Die Steuernummer-ID des Geschäftspartners. Beispiel: 30120345678 | string | Kann | — |
| <span className="hbs-f hbs-e3">[umsatzsteuerId](/bo4e/202610/bo/Marktteilnehmer#umsatzsteuerid)</span><span className="hbs-nr">00310</span> | Die Umsatzsteuer-ID des Geschäftspartners. Beispiel: DE 813281825 | string | Kann | — |
| <span className="hbs-f hbs-e3">[website](/bo4e/202610/bo/Marktteilnehmer#website)</span><span className="hbs-nr">00320</span> | Internetseite des Marktpartners. Beispiel: www.mp-energie.de | string | Kann | — |
| <span className="hbs-g hbs-e3">**bankverbindung** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-f hbs-e4">[bic](/bo4e/202610/com/Bankverbindung#bic)</span><span className="hbs-nr">00330</span> | BIC Code | string | Kann | — |
| <span className="hbs-f hbs-e4">[iban](/bo4e/202610/com/Bankverbindung#iban)</span><span className="hbs-nr">00340</span> | IBAN | string | Kann | — |
| <span className="hbs-f hbs-e4">[kontoinhaber](/bo4e/202610/com/Bankverbindung#kontoinhaber)</span><span className="hbs-nr">00350</span> | Der Kontoinhaber | string | Kann | — |
| <span className="hbs-f hbs-e4">[kreditinstitut](/bo4e/202610/com/Bankverbindung#kreditinstitut)</span><span className="hbs-nr">00360</span> | Name des Kreditinstitut | string | Kann | — |
| <span className="hbs-g hbs-e3">**erreichbarkeit** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-f hbs-e4">[verfuegbarkeit](/bo4e/202610/com/Erreichbarkeit#verfuegbarkeit)</span><span className="hbs-nr">00370</span> | Verfuegbarkeit | [Enum Verfuegbarkeit](/bo4e/202610/enum/Verfuegbarkeit) | Kann | — |
| <span className="hbs-w hbs-e5">`MONTAG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`DIENSTAG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MITTWOCH`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`DONNERSTAG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`FREITAG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`PAUSE`</span> | — | — | Kann | — |
| <span className="hbs-f hbs-e4">[zeit](/bo4e/202610/com/Erreichbarkeit#zeit)</span><span className="hbs-nr">00380</span> | Zeit der Erreichbarkeit | string | Kann | — |
| <span className="hbs-g hbs-e3">**partneradresse**</span> | — | object | Kann | — |
| <span className="hbs-f hbs-e4">[hausnummer](/bo4e/202610/com/Adresse#hausnummer)</span><span className="hbs-nr">00390</span> | Hausnummer und Ergänzung | string | Kann | — |
| <span className="hbs-f hbs-e4">[landescode](/bo4e/202610/com/Adresse#landescode)</span><span className="hbs-nr">00400</span> | Landescode | [Enum Landescode](/bo4e/202610/enum/Landescode) | Kann | — |
| <span className="hbs-w hbs-e5">`AC`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`AD`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`AE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`AF`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`AG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`AI`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`AL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`AM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`AN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`AO`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`AQ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`AR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`AS`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`AT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`AU`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`AW`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`AX`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`AZ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`BA`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`BB`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`BD`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`BE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`BF`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`BG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`BH`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`BI`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`BJ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`BL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`BM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`BN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`BO`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`BQ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`BR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`BS`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`BT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`BU`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`BV`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`BW`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`BY`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`BZ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`CA`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`CC`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`CD`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`CF`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`CG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`CH`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`CI`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`CK`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`CL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`CM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`CN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`CO`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`CP`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`CR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`CS`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`CU`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`CV`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`CW`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`CX`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`CY`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`CZ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`DE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`DG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`DJ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`DK`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`DM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`DO`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`DZ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`EA`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`EC`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`EE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`EG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`EH`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`ER`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`ES`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`ET`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`EU`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`FI`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`FJ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`FK`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`FM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`FO`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`FR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`FX`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GA`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GB`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GD`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GF`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GH`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GI`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GP`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GQ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GS`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GU`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GW`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GY`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`HK`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`HM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`HN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`HR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`HT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`HU`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`IC`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`ID`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`IE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`IL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`IM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`IN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`IO`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`IQ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`IR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`IS`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`IT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`JE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`JM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`JO`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`JP`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`KE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`KG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`KH`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`KI`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`KM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`KN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`KP`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`KR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`KW`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`KY`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`KZ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`LA`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`LB`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`LC`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`LI`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`LK`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`LR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`LS`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`LT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`LU`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`LV`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`LY`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MA`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MC`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MD`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`ME`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MF`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MH`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MK`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`ML`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MO`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MP`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MQ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MS`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MU`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MV`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MW`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MX`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MY`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MZ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`NA`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`NC`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`NE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`NF`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`NG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`NI`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`NL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`NO`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`NP`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`NR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`NT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`NU`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`NZ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`OM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`PA`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`PE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`PF`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`PG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`PH`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`PK`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`PL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`PM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`PN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`PR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`PS`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`PT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`PW`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`PY`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`QA`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`RE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`RO`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`RS`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`RU`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`RW`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`SA`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`SB`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`SC`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`SD`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`SE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`SF`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`SG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`SH`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`SI`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`SJ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`SK`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`SL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`SM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`SN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`SO`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`SR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`SS`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`ST`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`SU`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`SV`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`SX`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`SY`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`SZ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`TA`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`TC`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`TD`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`TF`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`TG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`TJ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`TK`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`TL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`TM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`TN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`TO`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`TP`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`TR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`TT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`TV`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`TW`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`TZ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`UA`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`UG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`UK`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`UM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`US`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`UY`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`UZ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`VA`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`VC`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`VE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`VG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`VI`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`VN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`VU`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`WF`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`WS`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`XK`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`YE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`YT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`YU`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`ZA`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`ZM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`ZR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`ZW`</span> | — | — | Kann | — |
| <span className="hbs-f hbs-e4">[ort](/bo4e/202610/com/Adresse#ort)</span><span className="hbs-nr">00410</span> | Ort | string | Kann | — |
| <span className="hbs-f hbs-e4">[ortsteil](/bo4e/202610/com/Adresse#ortsteil)</span><span className="hbs-nr">00420</span> | Ortsteil | string | Kann | — |
| <span className="hbs-f hbs-e4">[postfach](/bo4e/202610/com/Adresse#postfach)</span><span className="hbs-nr">00430</span> | Postfach | string | Kann | — |
| <span className="hbs-f hbs-e4">[postleitzahl](/bo4e/202610/com/Adresse#postleitzahl)</span><span className="hbs-nr">00440</span> | Postleitzahl | string | Kann | — |
| <span className="hbs-f hbs-e4">[strasse](/bo4e/202610/com/Adresse#strasse)</span><span className="hbs-nr">00450</span> | Strasse | string | Kann | — |

</div>

</Handbuchsatz>

## Kette dieses Auslösers

Das Ereignis löst die Nachricht aus.

| Nachricht | Antworten | Schreibaufruf nach der Antwort |
|---|---|---|
| [37002](/schnittstellen/202610/pruefi/PARTIN/PI_37002) | — | — |

## Transaktionsdaten

Der Umschlag der Nachricht. Pflichtfelder müssen beim Trigger-Aufruf gesetzt sein.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `pruefidentifikator` | — | nein | Wird dynamisch im Event-Prozess ermittelt. Ein vom Sender mitgegebener Wert wird ignoriert. Im Topic mögliche Prüfis — 37002. Mögliche Werte: `37002` |

## Zusatzdaten

`eventname` ist auf **START_PARTIN** festgelegt. Dieser Wert bleibt auch in der englischen Fassung deutsch, weil Camunda darüber korreliert.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `prozessId` | string | **ja** | — |
| `eventname` | const `START_PARTIN` | **ja** | — |

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
