# [NB] START_VERSAND_SDAE
<span hidden data-pagefind-meta={"title:Trigger-Ereignis START_VERSAND_SDAE — Marktrolle NB (FV 202610)"} />

Marktrolle **NB** · Formatversion **202610** · BO4E-Schema **1.7.8**

## Stammdaten

Unter diesem Topic ist genau einer der folgenden 21 Prüfidentifikatoren zulässig — welcher, entscheidet der Event-Prozess.

| Prüfi | Scope | Anwendungsfall | Festlegung | Kommunikation |
|---|---|---|---|---|
| [PI_44112](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44112) | UTILMD_GAS | Nicht bila.rel. Änderung vom NB | Marktraumumstellung | NB → LF |
| [PI_44113](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44113) | UTILMD_GAS | Nicht bila.rel. Änderung vom NB | Marktraumumstellung | NB → MSB |
| [PI_44123](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44123) | UTILMD_GAS | Bila.rel. Änderung vom NB mit Abhängigkeiten | GeLi Gas 2.0 | NB → LF |
| [PI_44175](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44175) | UTILMD_GAS | Änderung der Marktlokationsstruktur | GeLi Gas 2.0 | NB → LF |
| [PI_55173](/schnittstellen/202610/pruefi/UTILMD/PI_55173) | UTILMD | Änderung der Lokationsbündelstruktur | GPKE Teil 4 | NB → MSB |
| [PI_55175](/schnittstellen/202610/pruefi/UTILMD/PI_55175) | UTILMD | Änderung der Lokationsbündelstruktur | GPKE Teil 4 | NB → LF |
| [PI_55225](/schnittstellen/202610/pruefi/UTILMD/PI_55225) | UTILMD | Änderung Blindabr.-Daten der NeLo | GPKE Teil 4 | NB → LF |
| [PI_55615](/schnittstellen/202610/pruefi/UTILMD/PI_55615) | UTILMD | Änderung Daten der NeLo | GPKE Teil 4 | NB → LF |
| [PI_55616](/schnittstellen/202610/pruefi/UTILMD/PI_55616) | UTILMD | Änderung Daten der MaLo | GPKE Teil 4 | NB → LF |
| [PI_55617](/schnittstellen/202610/pruefi/UTILMD/PI_55617) | UTILMD | Änderung Daten der TR | GPKE Teil 4 | NB → LF |
| [PI_55618](/schnittstellen/202610/pruefi/UTILMD/PI_55618) | UTILMD | Änderung Daten der SR | GPKE Teil 4 | NB → LF |
| [PI_55619](/schnittstellen/202610/pruefi/UTILMD/PI_55619) | UTILMD | Änderung Daten der Tranche | GPKE Teil 4 | NB → LF |
| [PI_55620](/schnittstellen/202610/pruefi/UTILMD/PI_55620) | UTILMD | Änderung Daten der MeLo | GPKE Teil 4 | NB → LF |
| [PI_55627](/schnittstellen/202610/pruefi/UTILMD/PI_55627) | UTILMD | Änderung Daten der NeLo | GPKE Teil 4 | NB → MSB |
| [PI_55628](/schnittstellen/202610/pruefi/UTILMD/PI_55628) | UTILMD | Änderung Daten der MaLo | GPKE Teil 4 | NB → MSB |
| [PI_55629](/schnittstellen/202610/pruefi/UTILMD/PI_55629) | UTILMD | Änderung Daten der TR | GPKE Teil 4 | NB → MSB |
| [PI_55630](/schnittstellen/202610/pruefi/UTILMD/PI_55630) | UTILMD | Änderung Daten der SR | GPKE Teil 4 | NB → MSB |
| [PI_55632](/schnittstellen/202610/pruefi/UTILMD/PI_55632) | UTILMD | Änderung Daten der MeLo | GPKE Teil 4 | NB → MSB |
| [PI_55670](/schnittstellen/202610/pruefi/UTILMD/PI_55670) | UTILMD | Stammdaten BK-Treue | GPKE Teil 4 | NB → ÜNB |
| [PI_55688](/schnittstellen/202610/pruefi/UTILMD/PI_55688) | UTILMD | Änderung Daten der MaLo | GPKE Teil 4 | NB → ÜNB |
| [PI_55691](/schnittstellen/202610/pruefi/UTILMD/PI_55691) | UTILMD | Änderung Paket-ID der MaLo | GPKE Teil 4 | NB → LF |

Die Stammdaten der 21 Prüfidentifikatoren in **einer** Struktur — eine Spalte je Prüfidentifikator, wie im Anwendungshandbuch. Ein Wert in der Spalte heißt, dass das Feld zu diesem Prüfidentifikator gehört: **Muss**, wenn seine Spezifikation es verlangt, sonst **Kann**. Eine leere Zelle heißt »gehört nicht dazu«, nicht »unbekannt«. Vorausgewählt ist der erste; die übrigen schaltet die Leiste über der Tabelle zu.

<Handbuchsatz>

<div className="maco-tabellenrahmen">

| Struktur (BO4E) | Beschreibung | Format | <span className="hbs-p" title="Nicht bila.rel. Änderung vom NB">44112</span> | <span className="hbs-p" title="Nicht bila.rel. Änderung vom NB">44113</span> | <span className="hbs-p" title="Bila.rel. Änderung vom NB mit Abhängigkeiten">44123</span> | <span className="hbs-p" title="Änderung der Marktlokationsstruktur">44175</span> | <span className="hbs-p" title="Änderung der Lokationsbündelstruktur">55173</span> | <span className="hbs-p" title="Änderung der Lokationsbündelstruktur">55175</span> | <span className="hbs-p" title="Änderung Blindabr.-Daten der NeLo">55225</span> | <span className="hbs-p" title="Änderung Daten der NeLo">55615</span> | <span className="hbs-p" title="Änderung Daten der MaLo">55616</span> | <span className="hbs-p" title="Änderung Daten der TR">55617</span> | <span className="hbs-p" title="Änderung Daten der SR">55618</span> | <span className="hbs-p" title="Änderung Daten der Tranche">55619</span> | <span className="hbs-p" title="Änderung Daten der MeLo">55620</span> | <span className="hbs-p" title="Änderung Daten der NeLo">55627</span> | <span className="hbs-p" title="Änderung Daten der MaLo">55628</span> | <span className="hbs-p" title="Änderung Daten der TR">55629</span> | <span className="hbs-p" title="Änderung Daten der SR">55630</span> | <span className="hbs-p" title="Änderung Daten der MeLo">55632</span> | <span className="hbs-p" title="Stammdaten BK-Treue">55670</span> | <span className="hbs-p" title="Änderung Daten der MaLo">55688</span> | <span className="hbs-p" title="Änderung Paket-ID der MaLo">55691</span> | Bedingung |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| <span className="hbs-g hbs-e0">**stammdaten**</span> | — | object | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | — |
| <span className="hbs-g hbs-e1">**MARKTLOKATION** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | Kann | Muss | Muss | Muss | Kann | — | — | Kann | — | — | — | — | — | Kann | — | — | — | Muss | Kann | Muss | — |
| <span className="hbs-f hbs-e2">[marktgebiet](/bo4e/202610/bo/Marktlokation#marktgebiet)</span><span className="hbs-nr">00010</span> | für EDIFACT mapping | string | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[marktlokationsId](/bo4e/202610/bo/Marktlokation#marktlokationsid)</span><span className="hbs-nr">00020</span> | Identifikationsnummer einer Marktlokation, an der Energie entweder<br/>verbraucht, oder erzeugt wird | string | Kann | Kann | Muss | Muss | Muss | Kann | — | — | Kann | — | — | — | — | — | Kann | — | — | — | Kann | Kann | Muss | — |
| <span className="hbs-f hbs-e2">[netzebene](/bo4e/202610/bo/Marktlokation#netzebene)</span><span className="hbs-nr">00030</span> | Netzebene, in der der Bezug der Energie erfolgt. Bei Strom Spannungsebene der<br/>Lieferung, bei Gas Druckstufe. Beispiel Strom: Niederspannung Beispiel Gas:<br/>Niederdruck. | [Enum Netzebene](/bo4e/202610/enum/Netzebene) | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`NSP`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`MSP`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`HSP`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`HSS`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`MSP_NSP_UMSP`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`HSP_MSP_UMSP`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`HSS_HSP_UMSP`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`HD`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`MD`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`ND`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**eigentuemer**</span> | — | object | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[anrede](/bo4e/202610/bo/Geschaeftspartner#anrede)</span><span className="hbs-nr">00040</span> | Die Anrede für den GePa, Z.B. Herr. | string | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[gewerbekennzeichnung](/bo4e/202610/bo/Geschaeftspartner#gewerbekennzeichnung)</span><span className="hbs-nr">00050</span> | Kennzeichnung ob es sich um einen Gewerbe/Unternehmen (gewerbeKennzeichnung = true)<br/>oder eine Privatperson handelt. (gewerbeKennzeichnung = false) | boolean | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[name1](/bo4e/202610/bo/Geschaeftspartner#name1)</span><span className="hbs-nr">00060</span> | Erster Teil des Namens. Hier kann der Firmenname oder bei Privatpersonen<br/>beispielsweise der Nachname dargestellt werden. Beispiele: Yellow Strom GmbH<br/>oder Hagen | string | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[name2](/bo4e/202610/bo/Geschaeftspartner#name2)</span><span className="hbs-nr">00070</span> | Zweiter Teil des Namens. Hier kann der eine Erweiterung zum Firmennamen oder<br/>bei Privatpersonen beispielsweise der Vorname dargestellt werden. Beispiele:<br/>Bereich Süd oder Nina | string | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[name3](/bo4e/202610/bo/Geschaeftspartner#name3)</span><span className="hbs-nr">00080</span> | Dritter Teil des Namens. Hier können weitere Ergänzungen zum Firmennamen oder<br/>bei Privatpersonen Zusätze zum Namen dargestellt werden. Beispiele: und Afrika<br/>oder Sängerin | string | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[name4](/bo4e/202610/bo/Geschaeftspartner#name4)</span><span className="hbs-nr">00090</span> | name4 | string | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e3">**partneradresse**</span> | — | object | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[hausnummer](/bo4e/202610/com/Adresse#hausnummer)</span><span className="hbs-nr">00100</span> | Hausnummer und Ergänzung | string | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[landescode](/bo4e/202610/com/Adresse#landescode)</span><span className="hbs-nr">00110</span> | Landescode | [Enum Landescode](/bo4e/202610/enum/Landescode) | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AC`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AD`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AE`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AF`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AG`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AI`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AL`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AM`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AN`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AO`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AQ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AR`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AS`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AT`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AU`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AW`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AX`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AZ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BA`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BB`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BD`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BE`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BF`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BG`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BH`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BI`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BJ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BL`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BM`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BN`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BO`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BQ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BR`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BS`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BT`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BU`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BV`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BW`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BY`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BZ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CA`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CC`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CD`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CF`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CG`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CH`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CI`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CK`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CL`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CM`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CN`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CO`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CP`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CR`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CS`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CU`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CV`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CW`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CX`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CY`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CZ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`DE`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`DG`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`DJ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`DK`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`DM`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`DO`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`DZ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`EA`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`EC`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`EE`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`EG`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`EH`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ER`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ES`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ET`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`EU`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`FI`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`FJ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`FK`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`FM`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`FO`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`FR`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`FX`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GA`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GB`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GD`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GE`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GF`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GG`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GH`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GI`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GL`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GM`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GN`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GP`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GQ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GR`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GS`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GT`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GU`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GW`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GY`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`HK`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`HM`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`HN`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`HR`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`HT`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`HU`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IC`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ID`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IE`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IL`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IM`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IN`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IO`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IQ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IR`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IS`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IT`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`JE`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`JM`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`JO`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`JP`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KE`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KG`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KH`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KI`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KM`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KN`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KP`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KR`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KW`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KY`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KZ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LA`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LB`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LC`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LI`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LK`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LR`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LS`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LT`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LU`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LV`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LY`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MA`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MC`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MD`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ME`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MF`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MG`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MH`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MK`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ML`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MM`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MN`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MO`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MP`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MQ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MR`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MS`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MT`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MU`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MV`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MW`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MX`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MY`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MZ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NA`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NC`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NE`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NF`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NG`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NI`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NL`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NO`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NP`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NR`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NT`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NU`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NZ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`OM`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PA`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PE`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PF`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PG`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PH`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PK`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PL`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PM`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PN`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PR`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PS`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PT`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PW`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PY`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`QA`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`RE`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`RO`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`RS`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`RU`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`RW`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SA`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SB`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SC`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SD`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SE`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SF`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SG`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SH`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SI`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SJ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SK`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SL`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SM`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SN`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SO`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SR`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SS`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ST`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SU`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SV`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SX`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SY`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SZ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TA`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TC`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TD`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TF`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TG`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TJ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TK`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TL`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TM`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TN`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TO`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TP`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TR`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TT`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TV`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TW`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TZ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`UA`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`UG`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`UK`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`UM`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`US`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`UY`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`UZ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`VA`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`VC`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`VE`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`VG`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`VI`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`VN`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`VU`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`WF`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`WS`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`XK`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`YE`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`YT`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`YU`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ZA`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ZM`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ZR`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ZW`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[ort](/bo4e/202610/com/Adresse#ort)</span><span className="hbs-nr">00120</span> | Ort | string | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[ortsteil](/bo4e/202610/com/Adresse#ortsteil)</span><span className="hbs-nr">00130</span> | Ortsteil | string | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[postfach](/bo4e/202610/com/Adresse#postfach)</span><span className="hbs-nr">00140</span> | Postfach | string | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[postleitzahl](/bo4e/202610/com/Adresse#postleitzahl)</span><span className="hbs-nr">00150</span> | Postleitzahl | string | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[strasse](/bo4e/202610/com/Adresse#strasse)</span><span className="hbs-nr">00160</span> | Strasse | string | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**hausverwalter**</span> | — | object | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[anrede](/bo4e/202610/bo/Geschaeftspartner#anrede)</span><span className="hbs-nr">00170</span> | Die Anrede für den GePa, Z.B. Herr. | string | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[gewerbekennzeichnung](/bo4e/202610/bo/Geschaeftspartner#gewerbekennzeichnung)</span><span className="hbs-nr">00180</span> | Kennzeichnung ob es sich um einen Gewerbe/Unternehmen (gewerbeKennzeichnung = true)<br/>oder eine Privatperson handelt. (gewerbeKennzeichnung = false) | boolean | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[name1](/bo4e/202610/bo/Geschaeftspartner#name1)</span><span className="hbs-nr">00190</span> | Erster Teil des Namens. Hier kann der Firmenname oder bei Privatpersonen<br/>beispielsweise der Nachname dargestellt werden. Beispiele: Yellow Strom GmbH<br/>oder Hagen | string | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[name2](/bo4e/202610/bo/Geschaeftspartner#name2)</span><span className="hbs-nr">00200</span> | Zweiter Teil des Namens. Hier kann der eine Erweiterung zum Firmennamen oder<br/>bei Privatpersonen beispielsweise der Vorname dargestellt werden. Beispiele:<br/>Bereich Süd oder Nina | string | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[name3](/bo4e/202610/bo/Geschaeftspartner#name3)</span><span className="hbs-nr">00210</span> | Dritter Teil des Namens. Hier können weitere Ergänzungen zum Firmennamen oder<br/>bei Privatpersonen Zusätze zum Namen dargestellt werden. Beispiele: und Afrika<br/>oder Sängerin | string | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[name4](/bo4e/202610/bo/Geschaeftspartner#name4)</span><span className="hbs-nr">00220</span> | name4 | string | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e3">**partneradresse**</span> | — | object | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[hausnummer](/bo4e/202610/com/Adresse#hausnummer)</span><span className="hbs-nr">00230</span> | Hausnummer und Ergänzung | string | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[landescode](/bo4e/202610/com/Adresse#landescode)</span><span className="hbs-nr">00240</span> | Landescode | [Enum Landescode](/bo4e/202610/enum/Landescode) | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AC`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AD`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AE`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AF`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AG`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AI`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AL`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AM`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AN`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AO`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AQ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AR`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AS`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AT`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AU`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AW`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AX`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AZ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BA`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BB`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BD`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BE`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BF`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BG`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BH`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BI`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BJ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BL`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BM`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BN`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BO`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BQ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BR`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BS`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BT`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BU`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BV`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BW`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BY`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BZ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CA`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CC`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CD`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CF`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CG`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CH`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CI`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CK`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CL`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CM`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CN`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CO`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CP`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CR`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CS`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CU`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CV`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CW`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CX`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CY`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CZ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`DE`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`DG`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`DJ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`DK`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`DM`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`DO`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`DZ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`EA`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`EC`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`EE`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`EG`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`EH`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ER`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ES`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ET`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`EU`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`FI`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`FJ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`FK`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`FM`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`FO`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`FR`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`FX`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GA`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GB`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GD`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GE`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GF`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GG`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GH`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GI`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GL`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GM`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GN`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GP`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GQ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GR`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GS`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GT`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GU`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GW`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GY`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`HK`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`HM`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`HN`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`HR`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`HT`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`HU`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IC`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ID`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IE`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IL`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IM`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IN`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IO`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IQ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IR`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IS`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IT`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`JE`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`JM`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`JO`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`JP`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KE`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KG`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KH`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KI`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KM`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KN`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KP`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KR`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KW`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KY`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KZ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LA`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LB`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LC`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LI`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LK`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LR`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LS`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LT`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LU`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LV`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LY`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MA`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MC`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MD`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ME`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MF`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MG`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MH`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MK`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ML`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MM`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MN`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MO`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MP`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MQ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MR`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MS`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MT`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MU`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MV`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MW`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MX`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MY`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MZ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NA`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NC`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NE`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NF`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NG`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NI`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NL`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NO`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NP`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NR`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NT`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NU`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NZ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`OM`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PA`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PE`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PF`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PG`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PH`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PK`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PL`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PM`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PN`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PR`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PS`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PT`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PW`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PY`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`QA`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`RE`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`RO`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`RS`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`RU`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`RW`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SA`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SB`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SC`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SD`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SE`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SF`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SG`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SH`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SI`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SJ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SK`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SL`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SM`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SN`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SO`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SR`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SS`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ST`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SU`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SV`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SX`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SY`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SZ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TA`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TC`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TD`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TF`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TG`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TJ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TK`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TL`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TM`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TN`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TO`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TP`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TR`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TT`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TV`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TW`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TZ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`UA`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`UG`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`UK`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`UM`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`US`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`UY`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`UZ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`VA`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`VC`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`VE`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`VG`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`VI`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`VN`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`VU`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`WF`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`WS`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`XK`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`YE`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`YT`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`YU`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ZA`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ZM`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ZR`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ZW`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[ort](/bo4e/202610/com/Adresse#ort)</span><span className="hbs-nr">00250</span> | Ort | string | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[ortsteil](/bo4e/202610/com/Adresse#ortsteil)</span><span className="hbs-nr">00260</span> | Ortsteil | string | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[postfach](/bo4e/202610/com/Adresse#postfach)</span><span className="hbs-nr">00270</span> | Postfach | string | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[postleitzahl](/bo4e/202610/com/Adresse#postleitzahl)</span><span className="hbs-nr">00280</span> | Postleitzahl | string | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[strasse](/bo4e/202610/com/Adresse#strasse)</span><span className="hbs-nr">00290</span> | Strasse | string | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**lokationsadresse**</span> | — | object | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[hausnummer](/bo4e/202610/com/Adresse#hausnummer)</span><span className="hbs-nr">00300</span> | Hausnummer und Ergänzung | string | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[landescode](/bo4e/202610/com/Adresse#landescode)</span><span className="hbs-nr">00310</span> | Landescode | [Enum Landescode](/bo4e/202610/enum/Landescode) | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`AC`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`AD`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`AE`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`AF`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`AG`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`AI`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`AL`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`AM`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`AN`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`AO`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`AQ`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`AR`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`AS`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`AT`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`AU`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`AW`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`AX`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`AZ`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BA`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BB`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BD`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BE`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BF`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BG`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BH`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BI`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BJ`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BL`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BM`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BN`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BO`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BQ`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BR`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BS`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BT`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BU`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BV`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BW`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BY`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BZ`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`CA`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`CC`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`CD`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`CF`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`CG`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`CH`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`CI`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`CK`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`CL`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`CM`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`CN`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`CO`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`CP`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`CR`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`CS`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`CU`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`CV`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`CW`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`CX`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`CY`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`CZ`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`DE`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`DG`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`DJ`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`DK`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`DM`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`DO`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`DZ`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`EA`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`EC`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`EE`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`EG`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`EH`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`ER`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`ES`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`ET`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`EU`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`FI`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`FJ`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`FK`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`FM`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`FO`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`FR`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`FX`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GA`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GB`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GD`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GE`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GF`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GG`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GH`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GI`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GL`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GM`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GN`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GP`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GQ`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GR`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GS`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GT`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GU`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GW`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GY`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`HK`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`HM`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`HN`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`HR`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`HT`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`HU`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`IC`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`ID`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`IE`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`IL`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`IM`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`IN`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`IO`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`IQ`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`IR`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`IS`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`IT`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`JE`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`JM`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`JO`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`JP`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KE`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KG`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KH`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KI`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KM`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KN`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KP`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KR`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KW`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KY`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KZ`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`LA`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`LB`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`LC`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`LI`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`LK`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`LR`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`LS`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`LT`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`LU`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`LV`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`LY`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MA`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MC`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MD`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`ME`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MF`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MG`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MH`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MK`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`ML`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MM`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MN`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MO`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MP`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MQ`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MR`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MS`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MT`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MU`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MV`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MW`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MX`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MY`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MZ`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`NA`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`NC`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`NE`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`NF`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`NG`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`NI`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`NL`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`NO`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`NP`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`NR`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`NT`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`NU`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`NZ`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`OM`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`PA`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`PE`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`PF`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`PG`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`PH`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`PK`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`PL`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`PM`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`PN`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`PR`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`PS`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`PT`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`PW`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`PY`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`QA`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`RE`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`RO`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`RS`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`RU`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`RW`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`SA`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`SB`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`SC`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`SD`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`SE`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`SF`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`SG`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`SH`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`SI`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`SJ`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`SK`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`SL`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`SM`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`SN`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`SO`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`SR`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`SS`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`ST`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`SU`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`SV`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`SX`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`SY`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`SZ`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`TA`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`TC`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`TD`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`TF`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`TG`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`TJ`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`TK`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`TL`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`TM`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`TN`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`TO`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`TP`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`TR`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`TT`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`TV`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`TW`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`TZ`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`UA`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`UG`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`UK`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`UM`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`US`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`UY`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`UZ`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`VA`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`VC`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`VE`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`VG`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`VI`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`VN`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`VU`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`WF`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`WS`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`XK`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`YE`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`YT`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`YU`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`ZA`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`ZM`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`ZR`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`ZW`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[ort](/bo4e/202610/com/Adresse#ort)</span><span className="hbs-nr">00320</span> | Ort | string | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[ortsteil](/bo4e/202610/com/Adresse#ortsteil)</span><span className="hbs-nr">00330</span> | Ortsteil | string | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[postfach](/bo4e/202610/com/Adresse#postfach)</span><span className="hbs-nr">00340</span> | Postfach | string | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[postleitzahl](/bo4e/202610/com/Adresse#postleitzahl)</span><span className="hbs-nr">00350</span> | Postleitzahl | string | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[strasse](/bo4e/202610/com/Adresse#strasse)</span><span className="hbs-nr">00360</span> | Strasse | string | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e3">**zusatzInformation**</span> | — | object | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[zusatz1](/bo4e/202610/com/AdresszusatzInformation#zusatz1)</span><span className="hbs-nr">00370</span> | Adresszusatz 1 | string | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[zusatz2](/bo4e/202610/com/AdresszusatzInformation#zusatz2)</span><span className="hbs-nr">00380</span> | Adresszusatz 2 | string | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[zusatz3](/bo4e/202610/com/AdresszusatzInformation#zusatz3)</span><span className="hbs-nr">00390</span> | Adresszusatz 3 | string | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[zusatz4](/bo4e/202610/com/AdresszusatzInformation#zusatz4)</span><span className="hbs-nr">00400</span> | Adresszusatz 4 | string | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[zusatz5](/bo4e/202610/com/AdresszusatzInformation#zusatz5)</span><span className="hbs-nr">00410</span> | Adresszusatz 5 | string | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**zaehlwerke** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[obisKennzahl](/bo4e/202610/com/Zaehlwerk#obiskennzahl)</span><span className="hbs-nr">00420</span> | Die OBIS-Kennzahl für das Zählwerk, die festlegt, welche auf die gemessene Größe mit dem Stand gemeldet wird.<br/>Nur Zählwerkstände mit dieser OBIS-Kennzahl werden an diesem Zählwerk registriert. Beispiel:1-0:1.8.1 für<br/>elektrische Wirkarbeit. | string | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[wertegranularitaet](/bo4e/202610/com/Zaehlwerk#wertegranularitaet)</span><span className="hbs-nr">00430</span> | Wertegranularitaet | [Enum Wertegranularitaet](/bo4e/202610/enum/Wertegranularitaet) | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`JAEHRLICH`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`HALBJAEHRLICH`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`QUARTALSWEISE`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MONATLICH`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e3">**konzessionsabgabe**</span> | — | object | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[kategorie](/bo4e/202610/com/Konzessionsabgabe#kategorie)</span><span className="hbs-nr">00440</span> | Kategorie | string | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[kosten](/bo4e/202610/com/Konzessionsabgabe#kosten)</span><span className="hbs-nr">00450</span> | Kosten | number (float) | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[satz](/bo4e/202610/com/Konzessionsabgabe#satz)</span><span className="hbs-nr">00460</span> | Art der Konzessionsabgabe | [Enum AbgabeArt](/bo4e/202610/enum/AbgabeArt) | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KAS`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SA`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SAS`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TA`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TAS`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TK`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TKS`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TS`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TSS`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**gueltigkeitszeitraum** <span className="hbs-pflicht">\*</span></span> | — | object | — | — | — | — | Muss | Kann | — | — | Kann | — | — | — | — | — | Kann | — | — | — | Kann | Kann | — | — |
| <span className="hbs-f hbs-e3">[zeitraumId](/bo4e/202610/com/Zeitraum#zeitraumid) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00470</span> | zeitraumId | integer | — | — | — | — | Muss | Kann | — | — | Kann | — | — | — | — | — | Kann | — | — | — | Kann | Kann | — | — |
| <span className="hbs-f hbs-e2">[datenqualitaet](/bo4e/202610/bo/Marktlokation#datenqualitaet)</span><span className="hbs-nr">00480</span> | Datenqualitaet | [Enum Datenqualitaet](/bo4e/202610/enum/Datenqualitaet) | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | Muss | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`ERWARTETE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | Muss | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | Muss | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`INFORMATIVE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | Muss | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`GUELTIGE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | Muss | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | Muss | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_KEINE_DATEN_VORHANDEN`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | Muss | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN_ERWARTET`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | Muss | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | Muss | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_ERWARTETE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | Muss | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | Muss | Kann | Kann | — |
| <span className="hbs-f hbs-e2">[fernsteuerbarkeit](/bo4e/202610/bo/Marktlokation#fernsteuerbarkeit)</span><span className="hbs-nr">00490</span> | Fernsteuerbarkeit | [Enum Fernsteuerbarkeit](/bo4e/202610/enum/Fernsteuerbarkeit) | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`TECHNISCH_NICHT_FERNSTEUERBAR`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`TECHNISCH_FERNSTEUERBAR`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`DURCH_LF_FERNSTEUERBAR`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[messtechnischeEinordnung](/bo4e/202610/bo/Marktlokation#messtechnischeeinordnung)</span><span className="hbs-nr">00500</span> | Messtechnische Einordnung aus der UTILMD (IMS, KME_MME, KEINE_MESSUNG) | [Enum MesstechnischeEinordnung](/bo4e/202610/enum/MesstechnischeEinordnung) | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`IMS`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KME_MME`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KEINE_MESSUNG`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[redispatch](/bo4e/202610/bo/Marktlokation#redispatch)</span><span className="hbs-nr">00510</span> | redispatch | boolean | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[statusErzeugendeMalo](/bo4e/202610/bo/Marktlokation#statuserzeugendemalo)</span><span className="hbs-nr">00520</span> | StatusErzeugendeMarktlokation | [Enum StatusErzeugendeMarktlokation](/bo4e/202610/enum/StatusErzeugendeMarktlokation) | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`EINSPEISEVERGUETUNG_PARAGRAPH_37`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`GEFOERDERTE_DIREKTVERMARKTUNG`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`SONSTIGE_DIREKTVERMARKTUNG`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`VERMARKTUNG_OHNE_GESETZL_VERGUETUNG`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KWKG_VERGUETUNG`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`EINSPEISEVERGUETUNG_PARAGRAPH_38_AUSFALLVERGUETUNG`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[umspannung](/bo4e/202610/bo/Marktlokation#umspannung)</span><span className="hbs-nr">00530</span> | Netzebene | [Enum Netzebene](/bo4e/202610/enum/Netzebene) | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`NSP`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`MSP`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`HSP`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`HSS`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`MSP_NSP_UMSP`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`HSP_MSP_UMSP`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`HSS_HSP_UMSP`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`HD`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`MD`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`ND`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[verguetungEmpfaenger](/bo4e/202610/bo/Marktlokation#verguetungempfaenger)</span><span className="hbs-nr">00540</span> | VerguetungEmpfaenger | [Enum VerguetungEmpfaenger](/bo4e/202610/enum/VerguetungEmpfaenger) | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KUNDE`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`LIEFERANT`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**energieherkunft** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[erzeugungsart](/bo4e/202610/com/Energieherkunft#erzeugungsart)</span><span className="hbs-nr">00550</span> | Art der Erzeugung | [Enum Erzeugungsart](/bo4e/202610/enum/Erzeugungsart) | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`EEG`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KWK`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`EEG_DV`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KWK_DV`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`WIND`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`SOLAR`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KERNKRAFT`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`WASSER`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GEOTHERMIE`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BIOMASSE`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KOHLE`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GAS`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`SONSTIGE`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`SONSTIGE_EEG`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`SONSTIGE_ERZEUGUNGSART`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**marktrollen** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | Kann | Kann | — | — |
| <span className="hbs-f hbs-e3">[marktrolle](/bo4e/202610/bo/Marktteilnehmer#marktrolle)</span><span className="hbs-nr">00560</span> | Gibt im Klartext die Bezeichnung der Marktrolle an. | [Enum Marktrolle](/bo4e/202610/enum/Marktrolle) | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`NB`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`LF`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`MSB`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`MSBA`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`GMSB`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`MDL`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`DL`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`BKV`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`UENB`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`KUNDE-SELBST-NN`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`MGV`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`EIV`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`RB`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`KUNDE`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`INTERESSENT`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`KN`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`UBA`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`BIKO`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`ESA`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | Kann | Kann | — | — |
| <span className="hbs-f hbs-e3">[messstellenbetreiberEigenschaft](/bo4e/202610/bo/Marktteilnehmer#messstellenbetreibereigenschaft)</span><span className="hbs-nr">00570</span> | MSBEigenschaft | [Enum MSBEigenschaft](/bo4e/202610/enum/MSBEigenschaft) | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`WETTBEWERBLICHER_MESSSTELLENBETREIBER`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`AUFFANGMESSSTELLENBETREIBER`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[rollencodenummer](/bo4e/202610/bo/Marktteilnehmer#rollencodenummer)</span><span className="hbs-nr">00580</span> | Gibt die Codenummer der Marktrolle an. | string | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | Kann | Kann | — | — |
| <span className="hbs-f hbs-e3">[weiterverpflichtet](/bo4e/202610/bo/Marktteilnehmer#weiterverpflichtet)</span><span className="hbs-nr">00590</span> | weiterverpflichtet | boolean | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**technischeEinrichtungen** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[technischeEinrichtungenVorhanden](/bo4e/202610/com/TechnischeEinrichtung#technischeeinrichtungenvorhanden)</span><span className="hbs-nr">00600</span> | true =&gt; ZH7, false =&gt; ZH8 | boolean | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[verbrauchsart](/bo4e/202610/com/TechnischeEinrichtung#verbrauchsart)</span><span className="hbs-nr">00610</span> | Verbrauchsart | [Enum Verbrauchsart](/bo4e/202610/enum/Verbrauchsart) | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KL`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`W`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`EMOB`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`SB`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`SW`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`WK`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[bilanzierungsgebiet](/bo4e/202610/bo/Marktlokation#bilanzierungsgebiet)</span><span className="hbs-nr">00620</span> | Bilanzierungsgebiet, dem das Netzgebiet zugeordnet ist - im Falle eines Strom Netzes. | string | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e2">[paketId](/bo4e/202610/bo/Marktlokation#paketid)</span><span className="hbs-nr">00630</span> | paketId | string | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — |
| <span className="hbs-g hbs-e1">**MESSLOKATION** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | Kann | — | Muss | Kann | Kann | — | — | — | — | — | — | Muss | — | — | — | — | Muss | — | — | — | — |
| <span className="hbs-f hbs-e2">[gasqualitaet](/bo4e/202610/bo/Messlokation#gasqualitaet)</span><span className="hbs-nr">00640</span> | gasqualitaet für EDIFACT mapping | [Enum Gasqualitaet](/bo4e/202610/enum/Gasqualitaet) | Kann | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`H_GAS`</span> | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`L_GAS`</span> | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[messlokationsId](/bo4e/202610/bo/Messlokation#messlokationsid)</span><span className="hbs-nr">00650</span> | Die Messlokations-Identifikation. Das ist die frühere Zählpunktbezeichnung,<br/>z.B. DE 47108151234567 | string | Kann | Kann | — | Muss | Kann | Kann | — | — | — | — | — | — | Muss | — | — | — | — | Muss | — | — | — | — |
| <span className="hbs-g hbs-e2">**marktrollen** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-f hbs-e3">[marktrolle](/bo4e/202610/bo/Marktteilnehmer#marktrolle)</span><span className="hbs-nr">00660</span> | Gibt im Klartext die Bezeichnung der Marktrolle an. | [Enum Marktrolle](/bo4e/202610/enum/Marktrolle) | Kann | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e4">`NB`</span> | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e4">`LF`</span> | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e4">`MSB`</span> | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e4">`MSBA`</span> | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e4">`GMSB`</span> | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e4">`MDL`</span> | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e4">`DL`</span> | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e4">`BKV`</span> | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e4">`UENB`</span> | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e4">`KUNDE-SELBST-NN`</span> | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e4">`MGV`</span> | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e4">`EIV`</span> | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e4">`RB`</span> | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e4">`KUNDE`</span> | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e4">`INTERESSENT`</span> | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e4">`KN`</span> | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e4">`UBA`</span> | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e4">`BIKO`</span> | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e4">`ESA`</span> | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-f hbs-e3">[rollencodenummer](/bo4e/202610/bo/Marktteilnehmer#rollencodenummer)</span><span className="hbs-nr">00670</span> | Gibt die Codenummer der Marktrolle an. | string | Kann | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-f hbs-e3">[weiterverpflichtet](/bo4e/202610/bo/Marktteilnehmer#weiterverpflichtet)</span><span className="hbs-nr">00680</span> | weiterverpflichtet | boolean | Kann | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-f hbs-e3">[messstellenbetreiberEigenschaft](/bo4e/202610/bo/Marktteilnehmer#messstellenbetreibereigenschaft)</span><span className="hbs-nr">00690</span> | MSBEigenschaft | [Enum MSBEigenschaft](/bo4e/202610/enum/MSBEigenschaft) | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e4">`GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e4">`WETTBEWERBLICHER_MESSSTELLENBETREIBER`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e4">`AUFFANGMESSSTELLENBETREIBER`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-g hbs-e2">**gueltigkeitszeitraum**</span> | — | object | — | — | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-f hbs-e3">[zeitraumId](/bo4e/202610/com/Zeitraum#zeitraumid)</span><span className="hbs-nr">00700</span> | zeitraumId | integer | — | — | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-f hbs-e2">[datenqualitaet](/bo4e/202610/bo/Messlokation#datenqualitaet)</span><span className="hbs-nr">00710</span> | Datenqualitaet | [Enum Datenqualitaet](/bo4e/202610/enum/Datenqualitaet) | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e3">`ERWARTETE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e3">`INFORMATIVE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e3">`GUELTIGE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_KEINE_DATEN_VORHANDEN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN_ERWARTET`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_ERWARTETE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-f hbs-e2">[betriebszustand](/bo4e/202610/bo/Messlokation#betriebszustand)</span><span className="hbs-nr">00720</span> | Betriebszustand | [Enum Betriebszustand](/bo4e/202610/enum/Betriebszustand) | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e3">`GESPERRT_NICHT_ENTSPERREN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e3">`GESPERRT`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e3">`REGELBETRIEB`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e3">`AUSSERHALB_REGELBETRIEB`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-g hbs-e1">**NETZNUTZUNGSVERTRAG** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | Kann | Kann | Kann | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[gemeinderabatt](/bo4e/202610/bo/Vertrag#gemeinderabatt)</span><span className="hbs-nr">00730</span> | gemeinderabatt für EDIFACT mapping. | integer | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[vertragsbeginn](/bo4e/202610/bo/Vertrag#vertragsbeginn)</span><span className="hbs-nr">00740</span> | Gibt an, wann der Vertrag beginnt. | string (date-time) | Kann | Kann | Kann | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**korrespondenzpartner**</span> | — | object | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[anrede](/bo4e/202610/bo/Geschaeftspartner#anrede)</span><span className="hbs-nr">00750</span> | Die Anrede für den GePa, Z.B. Herr. | string | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[gewerbekennzeichnung](/bo4e/202610/bo/Geschaeftspartner#gewerbekennzeichnung)</span><span className="hbs-nr">00760</span> | Kennzeichnung ob es sich um einen Gewerbe/Unternehmen (gewerbeKennzeichnung = true)<br/>oder eine Privatperson handelt. (gewerbeKennzeichnung = false) | boolean | Kann | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[name1](/bo4e/202610/bo/Geschaeftspartner#name1)</span><span className="hbs-nr">00770</span> | Erster Teil des Namens. Hier kann der Firmenname oder bei Privatpersonen<br/>beispielsweise der Nachname dargestellt werden. Beispiele: Yellow Strom GmbH<br/>oder Hagen | string | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[name2](/bo4e/202610/bo/Geschaeftspartner#name2)</span><span className="hbs-nr">00780</span> | Zweiter Teil des Namens. Hier kann der eine Erweiterung zum Firmennamen oder<br/>bei Privatpersonen beispielsweise der Vorname dargestellt werden. Beispiele:<br/>Bereich Süd oder Nina | string | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[name3](/bo4e/202610/bo/Geschaeftspartner#name3)</span><span className="hbs-nr">00790</span> | Dritter Teil des Namens. Hier können weitere Ergänzungen zum Firmennamen oder<br/>bei Privatpersonen Zusätze zum Namen dargestellt werden. Beispiele: und Afrika<br/>oder Sängerin | string | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[name4](/bo4e/202610/bo/Geschaeftspartner#name4)</span><span className="hbs-nr">00800</span> | name4 | string | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e3">**partneradresse**</span> | — | object | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[hausnummer](/bo4e/202610/com/Adresse#hausnummer)</span><span className="hbs-nr">00810</span> | Hausnummer und Ergänzung | string | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[landescode](/bo4e/202610/com/Adresse#landescode)</span><span className="hbs-nr">00820</span> | Landescode | [Enum Landescode](/bo4e/202610/enum/Landescode) | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AC`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AD`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AE`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AF`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AG`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AI`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AL`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AM`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AN`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AO`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AQ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AR`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AS`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AT`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AU`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AW`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AX`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AZ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BA`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BB`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BD`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BE`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BF`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BG`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BH`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BI`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BJ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BL`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BM`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BN`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BO`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BQ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BR`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BS`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BT`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BU`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BV`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BW`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BY`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BZ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CA`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CC`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CD`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CF`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CG`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CH`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CI`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CK`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CL`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CM`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CN`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CO`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CP`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CR`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CS`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CU`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CV`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CW`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CX`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CY`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CZ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`DE`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`DG`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`DJ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`DK`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`DM`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`DO`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`DZ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`EA`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`EC`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`EE`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`EG`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`EH`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ER`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ES`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ET`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`EU`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`FI`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`FJ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`FK`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`FM`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`FO`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`FR`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`FX`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GA`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GB`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GD`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GE`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GF`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GG`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GH`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GI`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GL`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GM`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GN`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GP`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GQ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GR`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GS`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GT`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GU`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GW`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GY`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`HK`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`HM`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`HN`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`HR`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`HT`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`HU`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IC`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ID`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IE`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IL`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IM`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IN`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IO`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IQ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IR`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IS`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IT`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`JE`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`JM`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`JO`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`JP`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KE`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KG`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KH`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KI`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KM`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KN`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KP`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KR`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KW`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KY`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KZ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LA`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LB`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LC`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LI`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LK`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LR`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LS`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LT`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LU`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LV`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LY`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MA`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MC`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MD`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ME`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MF`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MG`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MH`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MK`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ML`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MM`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MN`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MO`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MP`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MQ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MR`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MS`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MT`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MU`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MV`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MW`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MX`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MY`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MZ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NA`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NC`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NE`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NF`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NG`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NI`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NL`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NO`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NP`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NR`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NT`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NU`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NZ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`OM`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PA`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PE`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PF`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PG`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PH`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PK`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PL`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PM`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PN`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PR`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PS`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PT`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PW`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PY`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`QA`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`RE`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`RO`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`RS`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`RU`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`RW`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SA`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SB`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SC`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SD`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SE`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SF`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SG`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SH`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SI`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SJ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SK`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SL`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SM`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SN`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SO`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SR`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SS`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ST`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SU`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SV`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SX`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SY`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SZ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TA`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TC`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TD`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TF`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TG`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TJ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TK`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TL`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TM`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TN`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TO`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TP`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TR`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TT`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TV`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TW`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TZ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`UA`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`UG`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`UK`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`UM`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`US`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`UY`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`UZ`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`VA`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`VC`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`VE`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`VG`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`VI`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`VN`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`VU`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`WF`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`WS`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`XK`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`YE`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`YT`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`YU`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ZA`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ZM`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ZR`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ZW`</span> | — | — | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[ort](/bo4e/202610/com/Adresse#ort)</span><span className="hbs-nr">00830</span> | Ort | string | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[ortsteil](/bo4e/202610/com/Adresse#ortsteil)</span><span className="hbs-nr">00840</span> | Ortsteil | string | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[postfach](/bo4e/202610/com/Adresse#postfach)</span><span className="hbs-nr">00850</span> | Postfach | string | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[postleitzahl](/bo4e/202610/com/Adresse#postleitzahl)</span><span className="hbs-nr">00860</span> | Postleitzahl | string | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[strasse](/bo4e/202610/com/Adresse#strasse)</span><span className="hbs-nr">00870</span> | Strasse | string | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e3">**ansprechpartner**</span> | — | object | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[eMailAdresse](/bo4e/202610/bo/Ansprechpartner#emailadresse)</span><span className="hbs-nr">00880</span> | E-Mail Adresse | string | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e4">**rufnummern** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e5">[nummerntyp](/bo4e/202610/com/Rufnummer#nummerntyp)</span><span className="hbs-nr">00890</span> | Rufnummernart | [Enum Rufnummernart](/bo4e/202610/enum/Rufnummernart) | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`RUF_ZENTRALE`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`FAX_ZENTRALE`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SAMMELRUF`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SAMMELFAX`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ABTEILUNGRUF`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ABTEILUNGFAX`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`RUF_DURCHWAHL`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`FAX_DURCHWAHL`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MOBIL_NUMMER`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e5">[rufnummer](/bo4e/202610/com/Rufnummer#rufnummer)</span><span className="hbs-nr">00900</span> | rufnummer | string | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**vertragskonditionen**</span> | — | object | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[naechstenetznutzungsabrechnung](/bo4e/202610/com/Vertragskonditionen#naechstenetznutzungsabrechnung)</span><span className="hbs-nr">00910</span> | naechstenetznutzungsabrechnung | string | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[netznutzungsabrechnungIntervall](/bo4e/202610/com/Vertragskonditionen#netznutzungsabrechnungintervall)</span><span className="hbs-nr">00920</span> | netznutzungsabrechnungIntervall | integer | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[netznutzungsabrechnungsvariante](/bo4e/202610/com/Vertragskonditionen#netznutzungsabrechnungsvariante)</span><span className="hbs-nr">00930</span> | Netznutzungsabrechnungsvariante | [Enum Netznutzungsabrechnungsvariante](/bo4e/202610/enum/Netznutzungsabrechnungsvariante) | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`ARBEITSPREIS_GRUNDPREIS`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`ARBEITSPREIS_LEISTUNGSPREIS`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[netznutzungsvertrag](/bo4e/202610/com/Vertragskonditionen#netznutzungsvertrag)</span><span className="hbs-nr">00940</span> | Netznutzungsvertrag | [Enum Netznutzungsvertrag](/bo4e/202610/enum/Netznutzungsvertrag) | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KUNDEN_NB`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`LIEFERANTEN_NB`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[netznutzungszahler](/bo4e/202610/com/Vertragskonditionen#netznutzungszahler)</span><span className="hbs-nr">00950</span> | Netznutzungszahler | [Enum Netznutzungszahler](/bo4e/202610/enum/Netznutzungszahler) | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KUNDE`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`LIEFERANT`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e3">**netznutzungsabrechnung**</span> | — | object | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[abrechnungsZeitraum](/bo4e/202610/com/Zeitraum#abrechnungszeitraum)</span><span className="hbs-nr">00960</span> | abrechnungsZeitraum | string | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**vertragspartner2** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[anrede](/bo4e/202610/bo/Geschaeftspartner#anrede)</span><span className="hbs-nr">00970</span> | Die Anrede für den GePa, Z.B. Herr. | string | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[gewerbekennzeichnung](/bo4e/202610/bo/Geschaeftspartner#gewerbekennzeichnung)</span><span className="hbs-nr">00980</span> | Kennzeichnung ob es sich um einen Gewerbe/Unternehmen (gewerbeKennzeichnung = true)<br/>oder eine Privatperson handelt. (gewerbeKennzeichnung = false) | boolean | Kann | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[name1](/bo4e/202610/bo/Geschaeftspartner#name1)</span><span className="hbs-nr">00990</span> | Erster Teil des Namens. Hier kann der Firmenname oder bei Privatpersonen<br/>beispielsweise der Nachname dargestellt werden. Beispiele: Yellow Strom GmbH<br/>oder Hagen | string | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[name2](/bo4e/202610/bo/Geschaeftspartner#name2)</span><span className="hbs-nr">01000</span> | Zweiter Teil des Namens. Hier kann der eine Erweiterung zum Firmennamen oder<br/>bei Privatpersonen beispielsweise der Vorname dargestellt werden. Beispiele:<br/>Bereich Süd oder Nina | string | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[name3](/bo4e/202610/bo/Geschaeftspartner#name3)</span><span className="hbs-nr">01010</span> | Dritter Teil des Namens. Hier können weitere Ergänzungen zum Firmennamen oder<br/>bei Privatpersonen Zusätze zum Namen dargestellt werden. Beispiele: und Afrika<br/>oder Sängerin | string | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[name4](/bo4e/202610/bo/Geschaeftspartner#name4)</span><span className="hbs-nr">01020</span> | name4 | string | Kann | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[geschaeftspartnerrolle](/bo4e/202610/bo/Geschaeftspartner#geschaeftspartnerrolle)</span><span className="hbs-nr">01030</span> | Rolle, die der Geschäftspartner hat (z.B. Interessent, Kunde). | array | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[datenqualitaet](/bo4e/202610/bo/Vertrag#datenqualitaet)</span><span className="hbs-nr">01040</span> | Datenqualitaet | [Enum Datenqualitaet](/bo4e/202610/enum/Datenqualitaet) | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`ERWARTETE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`INFORMATIVE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`GUELTIGE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_KEINE_DATEN_VORHANDEN`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN_ERWARTET`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_ERWARTETE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**gueltigkeitszeitraum**</span> | — | object | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[zeitraumId](/bo4e/202610/com/Zeitraum#zeitraumid)</span><span className="hbs-nr">01050</span> | zeitraumId | integer | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e1">**MESSSTELLENBETRIEBSVERTRAG** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[lokationsId](/bo4e/202610/bo/Vertrag#lokationsid)</span><span className="hbs-nr">01060</span> | lokationsId | string | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[lokationsTyp](/bo4e/202610/bo/Vertrag#lokationstyp)</span><span className="hbs-nr">01070</span> | Gibt an, ob es sich um eine Markt- oder Messlokation handelt | [Enum Lokationstyp](/bo4e/202610/enum/Lokationstyp) | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`MALO`</span> | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`MELO`</span> | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`NELO`</span> | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`TECHNISCHE_RESSOURCE`</span> | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`STEUERBARE_RESSOURCE`</span> | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`TRANCHE`</span> | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`MABIS_ZAEHLPUNKT`</span> | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**vertragskonditionen**</span> | — | object | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e3">**geplanteTurnusablesung**</span> | — | object | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[ableseZeitraum](/bo4e/202610/com/Zeitraum#ablesezeitraum)</span><span className="hbs-nr">01080</span> | ableseZeitraum | string | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[abrechnungUeberNna](/bo4e/202610/com/Vertragskonditionen#abrechnunguebernna)</span><span className="hbs-nr">01090</span> | abrechnungUeberNna | boolean | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e1">**BILANZIERUNG** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e2">[fallgruppenzuordnung](/bo4e/202610/bo/Bilanzierung#fallgruppenzuordnung)</span><span className="hbs-nr">01100</span> | Fallgruppenzuordnung (für gas RLM) | [Enum Fallgruppenzuordnung](/bo4e/202610/enum/Fallgruppenzuordnung) | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`GABI_RLMmT`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`GABI_RLMoT`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`GABI_RLMNEV`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[prognosegrundlage](/bo4e/202610/bo/Bilanzierung#prognosegrundlage) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">01110</span> | Prognosegrundlage | [Enum Prognosegrundlage](/bo4e/202610/enum/Prognosegrundlage) | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`WERTE`</span> | — | — | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`PROFILE`</span> | — | — | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**jahresverbrauchsprognose**</span> | — | object | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[einheit](/bo4e/202610/com/Menge#einheit)</span><span className="hbs-nr">01120</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202610/enum/Mengeneinheit) | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`W`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`WH`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KW`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KWH`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KVARH`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MW`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MWH`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`STUECK`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KUBIKMETER`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`STUNDE`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`TAG`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MONAT`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`JAHR`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`PROZENT`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`ANZAHL`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`VAR`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KVAR`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`VARH`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KWHK`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`Z16`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KWT`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`WATT_PRO_QUADRATMETER`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`METER_PRO_SEKUNDE`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[wert](/bo4e/202610/com/Menge#wert)</span><span className="hbs-nr">01130</span> | Wert | number (float) | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**kundenwert**</span> | — | object | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[wert](/bo4e/202610/com/Menge#wert)</span><span className="hbs-nr">01140</span> | Wert | number (float) | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**lastprofile** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[bezeichnung](/bo4e/202610/com/Lastprofil#bezeichnung)</span><span className="hbs-nr">01150</span> | Bezeichnung des Profils | string | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[herausgeber](/bo4e/202610/com/Lastprofil#herausgeber)</span><span className="hbs-nr">01160</span> | Herausgeber des Lastprofils | string | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[verfahren](/bo4e/202610/com/Lastprofil#verfahren)</span><span className="hbs-nr">01170</span> | Profilverfahren | [Enum Profilverfahren](/bo4e/202610/enum/Profilverfahren) | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`SYNTHETISCH`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`ANALYTISCH`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e3">**tagesparameter**</span> | — | object | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[dienstanbieter](/bo4e/202610/com/Tagesparameter#dienstanbieter)</span><span className="hbs-nr">01180</span> | dienstanbieter | string | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[herausgeber](/bo4e/202610/com/Tagesparameter#herausgeber)</span><span className="hbs-nr">01190</span> | Herausgeber | [Enum Herausgeber](/bo4e/202610/enum/Herausgeber) | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NB`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BDEW`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TUM`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[klimazone](/bo4e/202610/com/Tagesparameter#klimazone)</span><span className="hbs-nr">01200</span> | klimazone | string | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[temperaturmessstelle](/bo4e/202610/com/Tagesparameter#temperaturmessstelle)</span><span className="hbs-nr">01210</span> | temperaturmessstelle | string | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[einspeisung](/bo4e/202610/com/Lastprofil#einspeisung)</span><span className="hbs-nr">01220</span> | Kennzeichen Einspeisung | boolean | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[profilart](/bo4e/202610/com/Lastprofil#profilart)</span><span className="hbs-nr">01230</span> | Profilart | [Enum Profilart](/bo4e/202610/enum/Profilart) | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`ART_STANDARDLASTPROFIL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`ART_TAGESPARAMETERABHAENGIGES_LASTPROFIL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`ART_LASTPROFIL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[referenzprofilbezeichnung](/bo4e/202610/com/Lastprofil#referenzprofilbezeichnung)</span><span className="hbs-nr">01240</span> | Bezeichnung des Referenzprofils | string | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[abwicklungsmodell](/bo4e/202610/bo/Bilanzierung#abwicklungsmodell)</span><span className="hbs-nr">01250</span> | Abwicklungsmodell | [Enum Abwicklungsmodell](/bo4e/202610/enum/Abwicklungsmodell) | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`MODELL_1_BILANZIERUNG_AN_MARKTLOKATION`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`MODELL_2_BILANZIERUNG_IM_BILANZIERUNGSGEBIET`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[datenqualitaet](/bo4e/202610/bo/Bilanzierung#datenqualitaet)</span><span className="hbs-nr">01260</span> | Datenqualität | [Enum Datenqualitaet](/bo4e/202610/enum/Datenqualitaet) | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`ERWARTETE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`INFORMATIVE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`GUELTIGE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_KEINE_DATEN_VORHANDEN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN_ERWARTET`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_ERWARTETE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[detailsPrognosegrundlage](/bo4e/202610/bo/Bilanzierung#detailsprognosegrundlage)</span><span className="hbs-nr">01270</span> | Prognosegrundlage - Besteht der Bedarf ein tagesparameteräbhängiges Lastprofil mit gemeinsamer Messung anzugeben, so ist dies über die 2 -malige Wiederholung des CAV Segments mit der Angabe der Codes E02 und E14 möglich. | array | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**gueltigkeitszeitraum**</span> | — | object | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[zeitraumId](/bo4e/202610/com/Zeitraum#zeitraumid)</span><span className="hbs-nr">01280</span> | zeitraumId | integer | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**temperaturarbeit**</span> | — | object | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[einheit](/bo4e/202610/com/Menge#einheit)</span><span className="hbs-nr">01290</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202610/enum/Mengeneinheit) | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`W`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`WH`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KW`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KWH`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KVARH`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MW`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MWH`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`STUECK`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KUBIKMETER`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`STUNDE`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`TAG`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MONAT`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`JAHR`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`PROZENT`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`ANZAHL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`VAR`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KVAR`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`VARH`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KWHK`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`Z16`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KWT`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`WATT_PRO_QUADRATMETER`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`METER_PRO_SEKUNDE`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[wert](/bo4e/202610/com/Menge#wert)</span><span className="hbs-nr">01300</span> | Wert | number (float) | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[bilanzkreis](/bo4e/202610/bo/Bilanzierung#bilanzkreis)</span><span className="hbs-nr">01310</span> | Bilanzkreis | string | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e2">[zeitreihentyp](/bo4e/202610/bo/Bilanzierung#zeitreihentyp)</span><span className="hbs-nr">01320</span> | Zeitreihentyp | [Enum Zeitreihentyp](/bo4e/202610/enum/Zeitreihentyp) | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`EGS`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`LGS`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`NZR`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`SES`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`SLS`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`TES`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`TLS`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`SLS_TLS`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`SES_TES`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`AUS`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`BAS`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`DBA`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`DZR`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`DZÜ`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`FPE`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`FPI`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`SRE`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`SRI`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`VZR`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`BIL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`BIP`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`BIT`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`GAL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`GAP`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`GAT`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`GEL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`GEP`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`GET`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`SOL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`SOP`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`SOT`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`WFL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`WFP`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`WNL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`WNP`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`WNT`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`WAL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`WAP`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`WAT`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`AU1`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`BI1`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`BI2`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`BI3`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`GAA`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`GAB`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`GAC`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`GE1`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`GE2`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`GE3`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`SO1`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`SO2`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`SO3`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`WF1`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`WF2`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`WF3`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`WN1`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`WN2`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`WN3`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`WAA`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`WAB`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`WAC`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`AUSFALLARBEITSSUMME`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`BILANZKREISABWEICHUNGSSALDO`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZZEITREIHE`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`DELTAZEITREIHE`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`DELTAZEITREIHENUEBERTRAG`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`FAHRPLANENTNAHMESUMME`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`FAHRPLANEINSPEISESUMME`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`UEBERFUEHRUNGSZEITREIHE_SEKUNDAERREGELLEISTUNG_EXPORT`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`UEBERFUEHRUNGSZEITREIHE_SEKUNDAERREGELLEISTUNG_IMPORT`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`VERLUSTZEITREIHE`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_BIOMASSE_BIOGAS_GEMESSEN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_BIOMASSE_BIOGAS_EINSPEISEPROFIL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_BIOMASSE_BIOGAS_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_DEPONIE_KLAER_GRUBENGAS_GEMESSEN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_DEPONIE_KLAER_GRUBENGAS_EINSPEISEPROFIL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_DEPONIE_KLAER_GRUBENGAS_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_GEOTHERMIE_GEMESSEN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_GEOTHERMIE_EINSPEISEPROFIL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_GEOTHERMIE_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_SOLAR_GEMESSEN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_SOLAR_EINSPEISEPROFIL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_SOLAR_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_WIND_OFFSHORE_GEMESSEN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_WIND_OFFSHORE_EINSPEISEPROFIL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_WIND_OFFSHORE_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_WIND_ONSHORE_GEMESSEN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_WIND_ONSHORE_EINSPEISEPROFIL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_WIND_ONSHORE_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_WASSERKRAFT_GEMESSEN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_WASSERKRAFT_EINSPEISEPROFIL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_WASSERKRAFT_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_AUSFALLARBEIT`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_BIOMASSE_BIOGAS_WERTE`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_BIOMASSE_BIOGAS_STANDARDEINSPEISEPROFIL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_BIOMASSE_BIOGAS_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_DEPONIE_KLAER_GRUBENGAS_WERTE`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_DEPONIE_KLAER_GRUBENGAS_STANDARDEINSPEISEPROFIL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_DEPONIE_KLAER_GRUBENGAS_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_GEOTHERMIE_WERTE`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_GEOTHERMIE_STANDARDEINSPEISEPROFIL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_GEOTHERMIE_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_SOLAR_WERTE`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_SOLAR_STANDARDEINSPEISEPROFIL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_SOLAR_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_WIND_OFFSHORE_WERTE`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_WIND_OFFSHORE_STANDARDEINSPEISEPROFIL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_WIND_OFFSHORE_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_WIND_ONSHORE_WERTE`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_WIND_ONSHORE_STANDARDEINSPEISEPROFIL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_WIND_ONSHORE_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_WASSERKRAFT_WERTE`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_WASSERKRAFT_STANDARDEINSPEISEPROFIL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_WASSERKRAFT_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-g hbs-e1">**LOKATIONSBUENDEL** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | — | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[datenqualitaet](/bo4e/202610/bo/Lokationsbuendel#datenqualitaet)</span><span className="hbs-nr">01330</span> | Datenqualitaet | [Enum Datenqualitaet](/bo4e/202610/enum/Datenqualitaet) | — | — | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`ERWARTETE_DATEN`</span> | — | — | — | — | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`INFORMATIVE_DATEN`</span> | — | — | — | — | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`GUELTIGE_DATEN`</span> | — | — | — | — | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN`</span> | — | — | — | — | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_KEINE_DATEN_VORHANDEN`</span> | — | — | — | — | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN_ERWARTET`</span> | — | — | — | — | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_DATEN`</span> | — | — | — | — | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_ERWARTETE_DATEN`</span> | — | — | — | — | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[lokationsbuendelNummer](/bo4e/202610/bo/Lokationsbuendel#lokationsbuendelnummer)</span><span className="hbs-nr">01340</span> | lokationsbuendelNummer | integer | — | — | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[lokationsbuendelstrukturId](/bo4e/202610/bo/Lokationsbuendel#lokationsbuendelstrukturid)</span><span className="hbs-nr">01350</span> | lokationsbuendelstrukturId | string | — | — | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[standardisierteLokationsbuendelstruktur](/bo4e/202610/bo/Lokationsbuendel#standardisiertelokationsbuendelstruktur)</span><span className="hbs-nr">01360</span> | standardisierteLokationsbuendelstruktur | boolean | — | — | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**gueltigkeitszeitraum**</span> | — | object | — | — | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[zeitraumId](/bo4e/202610/com/Zeitraum#zeitraumid)</span><span className="hbs-nr">01370</span> | zeitraumId | integer | — | — | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**zuordnungObjectcode** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | — | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[referenzLokationsId](/bo4e/202610/com/ZuordnungObjectcode#referenzlokationsid)</span><span className="hbs-nr">01380</span> | referenzLokationsId | string | — | — | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[referenzLokationsTyp](/bo4e/202610/com/ZuordnungObjectcode#referenzlokationstyp)</span><span className="hbs-nr">01390</span> | Gibt an, ob es sich um eine Markt- oder Messlokation handelt | [Enum Lokationstyp](/bo4e/202610/enum/Lokationstyp) | — | — | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MALO`</span> | — | — | — | — | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MELO`</span> | — | — | — | — | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`NELO`</span> | — | — | — | — | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`TECHNISCHE_RESSOURCE`</span> | — | — | — | — | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`STEUERBARE_RESSOURCE`</span> | — | — | — | — | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`TRANCHE`</span> | — | — | — | — | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MABIS_ZAEHLPUNKT`</span> | — | — | — | — | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[referenzMarktlokationTechnischeRessource](/bo4e/202610/com/ZuordnungObjectcode#referenzmarktlokationtechnischeressource)</span><span className="hbs-nr">01400</span> | referenzMarktlokationTechnischeRessource | array | — | — | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[vorgelagerteLokationId](/bo4e/202610/com/ZuordnungObjectcode#vorgelagertelokationid)</span><span className="hbs-nr">01410</span> | vorgelagerteLokationId | string | — | — | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[vorgelagerteLokationTyp](/bo4e/202610/com/ZuordnungObjectcode#vorgelagertelokationtyp)</span><span className="hbs-nr">01420</span> | Gibt an, ob es sich um eine Markt- oder Messlokation handelt | [Enum Lokationstyp](/bo4e/202610/enum/Lokationstyp) | — | — | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MALO`</span> | — | — | — | — | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MELO`</span> | — | — | — | — | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`NELO`</span> | — | — | — | — | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`TECHNISCHE_RESSOURCE`</span> | — | — | — | — | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`STEUERBARE_RESSOURCE`</span> | — | — | — | — | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`TRANCHE`</span> | — | — | — | — | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MABIS_ZAEHLPUNKT`</span> | — | — | — | — | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e3">**objectcode** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | — | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[lokationsbuendelNummer](/bo4e/202610/com/Objectcode#lokationsbuendelnummer)</span><span className="hbs-nr">01430</span> | lokationsbuendelNummer | integer | — | — | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[objectcode](/bo4e/202610/com/Objectcode#objectcode)</span><span className="hbs-nr">01440</span> | objectcode | string | — | — | — | — | Kann | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e1">**NETZLOKATION** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | — | — | — | Kann | Kann | Muss | Muss | — | — | — | — | — | Muss | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[netzlokationsId](/bo4e/202610/bo/Netzlokation#netzlokationsid)</span><span className="hbs-nr">01450</span> | Identifikationsnummer einer Netzlokation, an der Energie entweder<br/>verbraucht, oder erzeugt wird (Like MarktlokationsId Marktlokation) | string | — | — | — | — | Kann | Kann | Muss | Muss | — | — | — | — | — | Muss | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**gueltigkeitszeitraum**</span> | — | object | — | — | — | — | Kann | Kann | Kann | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[zeitraumId](/bo4e/202610/com/Zeitraum#zeitraumid)</span><span className="hbs-nr">01460</span> | zeitraumId | integer | — | — | — | — | Kann | Kann | Kann | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[datenqualitaet](/bo4e/202610/bo/Netzlokation#datenqualitaet)</span><span className="hbs-nr">01470</span> | Datenqualitaet | [Enum Datenqualitaet](/bo4e/202610/enum/Datenqualitaet) | — | — | — | — | — | — | Kann | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`ERWARTETE_DATEN`</span> | — | — | — | — | — | — | — | — | Kann | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | — | — | — | — | Kann | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`INFORMATIVE_DATEN`</span> | — | — | — | — | — | — | — | — | Kann | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`GUELTIGE_DATEN`</span> | — | — | — | — | — | — | — | — | Kann | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN`</span> | — | — | — | — | — | — | — | — | Kann | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_KEINE_DATEN_VORHANDEN`</span> | — | — | — | — | — | — | — | — | Kann | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN_ERWARTET`</span> | — | — | — | — | — | — | — | — | Kann | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_DATEN`</span> | — | — | — | — | — | — | — | — | Kann | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_ERWARTETE_DATEN`</span> | — | — | — | — | — | — | — | — | Kann | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | — | — | — | — | Kann | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**abrechnungsdaten** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[abrechnungBlindarbeit](/bo4e/202610/com/Netznutzungsabrechnungsdaten#abrechnungblindarbeit)</span><span className="hbs-nr">01480</span> | abrechnungBlindarbeit | boolean | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[artikelId](/bo4e/202610/com/Netznutzungsabrechnungsdaten#artikelid)</span><span className="hbs-nr">01490</span> | artikelId | string | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[artikelIdTyp](/bo4e/202610/com/Netznutzungsabrechnungsdaten#artikelidtyp)</span><span className="hbs-nr">01500</span> | Liste von Artikel-IDs, z.B. für standardisierte vom BDEW herausgegebene Artikel, die im Strommarkt die BDEW-Artikelnummer ablösen | [Enum ArtikelIdTyp](/bo4e/202610/enum/ArtikelIdTyp) | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`ARTIKELID`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GRUPPENARTIKELID`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[zahlerBlindarbeit](/bo4e/202610/com/Netznutzungsabrechnungsdaten#zahlerblindarbeit)</span><span className="hbs-nr">01510</span> | ZahlerBlindarbeit | [Enum ZahlerBlindarbeit](/bo4e/202610/enum/ZahlerBlindarbeit) | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`ANSCHLUSSNUTZER`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`LIEFERANT`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`NICHT_FESTGELEGT`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**marktrollen** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[marktrolle](/bo4e/202610/bo/Marktteilnehmer#marktrolle)</span><span className="hbs-nr">01520</span> | Gibt im Klartext die Bezeichnung der Marktrolle an. | [Enum Marktrolle](/bo4e/202610/enum/Marktrolle) | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`NB`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`LF`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MSB`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MSBA`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GMSB`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MDL`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`DL`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BKV`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`UENB`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KUNDE-SELBST-NN`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MGV`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`EIV`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`RB`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KUNDE`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`INTERESSENT`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KN`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`UBA`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BIKO`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`ESA`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[messstellenbetreiberEigenschaft](/bo4e/202610/bo/Marktteilnehmer#messstellenbetreibereigenschaft)</span><span className="hbs-nr">01530</span> | MSBEigenschaft | [Enum MSBEigenschaft](/bo4e/202610/enum/MSBEigenschaft) | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`WETTBEWERBLICHER_MESSSTELLENBETREIBER`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`AUFFANGMESSSTELLENBETREIBER`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[rollencodenummer](/bo4e/202610/bo/Marktteilnehmer#rollencodenummer)</span><span className="hbs-nr">01540</span> | Gibt die Codenummer der Marktrolle an. | string | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e1">**STEUERBARE_RESSOURCE** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | — | — | — | Kann | Kann | — | — | — | — | Muss | — | — | — | — | — | Muss | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[ressourcenId](/bo4e/202610/bo/SteuerbareRessource#ressourcenid)</span><span className="hbs-nr">01550</span> | ressourcenId | string | — | — | — | — | Kann | Kann | — | — | — | — | Muss | — | — | — | — | — | Muss | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**gueltigkeitszeitraum**</span> | — | object | — | — | — | — | Kann | Kann | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[zeitraumId](/bo4e/202610/com/Zeitraum#zeitraumid)</span><span className="hbs-nr">01560</span> | zeitraumId | integer | — | — | — | — | Kann | Kann | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[datenqualitaet](/bo4e/202610/bo/SteuerbareRessource#datenqualitaet)</span><span className="hbs-nr">01570</span> | Datenqualitaet | [Enum Datenqualitaet](/bo4e/202610/enum/Datenqualitaet) | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`ERWARTETE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`INFORMATIVE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`GUELTIGE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_KEINE_DATEN_VORHANDEN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN_ERWARTET`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_ERWARTETE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**marktrollen** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[marktrolle](/bo4e/202610/bo/Marktteilnehmer#marktrolle)</span><span className="hbs-nr">01580</span> | Gibt im Klartext die Bezeichnung der Marktrolle an. | [Enum Marktrolle](/bo4e/202610/enum/Marktrolle) | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`NB`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`LF`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MSB`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MSBA`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GMSB`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MDL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`DL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BKV`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`UENB`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KUNDE-SELBST-NN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MGV`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`EIV`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`RB`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KUNDE`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`INTERESSENT`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`UBA`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BIKO`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`ESA`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[messstellenbetreiberEigenschaft](/bo4e/202610/bo/Marktteilnehmer#messstellenbetreibereigenschaft)</span><span className="hbs-nr">01590</span> | MSBEigenschaft | [Enum MSBEigenschaft](/bo4e/202610/enum/MSBEigenschaft) | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`WETTBEWERBLICHER_MESSSTELLENBETREIBER`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`AUFFANGMESSSTELLENBETREIBER`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[rollencodenummer](/bo4e/202610/bo/Marktteilnehmer#rollencodenummer)</span><span className="hbs-nr">01600</span> | Gibt die Codenummer der Marktrolle an. | string | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-g hbs-e1">**TECHNISCHE_RESSOURCE** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | — | — | — | Kann | Kann | — | — | — | Muss | — | — | — | — | — | Muss | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[ressourcenId](/bo4e/202610/bo/TechnischeRessource#ressourcenid)</span><span className="hbs-nr">01610</span> | ressourcenId | string | — | — | — | — | Kann | Kann | — | — | — | Muss | — | — | — | — | — | Muss | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**gueltigkeitszeitraum**</span> | — | object | — | — | — | — | Kann | Kann | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[zeitraumId](/bo4e/202610/com/Zeitraum#zeitraumid)</span><span className="hbs-nr">01620</span> | zeitraumId | integer | — | — | — | — | Kann | Kann | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[art](/bo4e/202610/bo/TechnischeRessource#art)</span><span className="hbs-nr">01630</span> | TechnischeRessourceArt | [Enum TechnischeRessourceArt](/bo4e/202610/enum/TechnischeRessourceArt) | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`STROMERZEUGUNG`</span> | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`STROMVERBRAUCH`</span> | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`SPEICHER`</span> | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[artEMobilitaet](/bo4e/202610/bo/TechnischeRessource#artemobilitaet)</span><span className="hbs-nr">01640</span> | ArtEmobilitaet | [Enum ArtEmobilitaet](/bo4e/202610/enum/ArtEmobilitaet) | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`WB`</span> | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`LS`</span> | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`LP`</span> | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[datenqualitaet](/bo4e/202610/bo/TechnischeRessource#datenqualitaet)</span><span className="hbs-nr">01650</span> | Datenqualitaet | [Enum Datenqualitaet](/bo4e/202610/enum/Datenqualitaet) | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`ERWARTETE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`INFORMATIVE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`GUELTIGE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_KEINE_DATEN_VORHANDEN`</span> | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN_ERWARTET`</span> | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_ERWARTETE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[einordnung](/bo4e/202610/bo/TechnischeRessource#einordnung)</span><span className="hbs-nr">01660</span> | RessourceWechselmoeglichkeit | [Enum RessourceWechselmoeglichkeit](/bo4e/202610/enum/RessourceWechselmoeglichkeit) | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`WECHSELMOEGLICHKEIT_EINMALIG_NOCH_MOEGLICH`</span> | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`WECHSELMOEGLICHKEIT_NICHT_MOEGLICH`</span> | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`BEFRISTET_OHNE_WECHSELMOEGLICHKEIT`</span> | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`WECHSEL_WURDE_DURCHGEFUEHRT`</span> | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[enwg](/bo4e/202610/bo/TechnischeRessource#enwg)</span><span className="hbs-nr">01670</span> | enwg | boolean | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[erzeugungsart](/bo4e/202610/bo/TechnischeRessource#erzeugungsart)</span><span className="hbs-nr">01680</span> | Art der Erzeugung der Energie. Details Erzeugungsart<br/>Beispiel: CAV+ZF5'<br/>Erzeugungsart:<br/>ZF5: Solar<br/>ZF6: Wind<br/>ZG0: Gas<br/>ZG1: Wasser<br/>ZG5: Sonstige Erzeugungsart | [Enum Erzeugungsart](/bo4e/202610/enum/Erzeugungsart) | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`EEG`</span> | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KWK`</span> | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`EEG_DV`</span> | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KWK_DV`</span> | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`WIND`</span> | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`SOLAR`</span> | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KERNKRAFT`</span> | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`WASSER`</span> | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`GEOTHERMIE`</span> | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`BIOMASSE`</span> | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KOHLE`</span> | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`GAS`</span> | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`SONSTIGE`</span> | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`SONSTIGE_EEG`</span> | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`SONSTIGE_ERZEUGUNGSART`</span> | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[inbetriebsetzungsdatum](/bo4e/202610/bo/TechnischeRessource#inbetriebsetzungsdatum)</span><span className="hbs-nr">01690</span> | Inbetriebsetzung | [Enum Inbetriebsetzung](/bo4e/202610/enum/Inbetriebsetzung) | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`INBETRIEBSETZUNG_NACH_2023`</span> | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`INBETRIEBSETZUNG_VOR_2024`</span> | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[referenzNetzlokation](/bo4e/202610/bo/TechnischeRessource#referenznetzlokation)</span><span className="hbs-nr">01700</span> | referenzNetzlokation | string | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[referenzSteuerbareRessource](/bo4e/202610/bo/TechnischeRessource#referenzsteuerbareressource)</span><span className="hbs-nr">01710</span> | referenzSteuerbareRessource | string | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[referenzTranche](/bo4e/202610/bo/TechnischeRessource#referenztranche)</span><span className="hbs-nr">01720</span> | referenzTranche | string | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[speicherart](/bo4e/202610/bo/TechnischeRessource#speicherart)</span><span className="hbs-nr">01730</span> | Art der speicher. Details Speicherart<br/>Beispiel: CAV+ZF7'<br/>Speicherart:<br/>ZF7: Wasserstoffspeicher<br/>ZF8: Pumpspeicher<br/>ZF9: Batteriespeicher<br/>ZG6: Sonstige Speicherart | [Enum Speicherart](/bo4e/202610/enum/Speicherart) | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`WASSERSTOFFSPEICHER`</span> | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`PUMPSPEICHER`</span> | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`BATTERIESPEICHER`</span> | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`SONSTIGE_SPEICHERART`</span> | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[speicherkapazitaet](/bo4e/202610/bo/TechnischeRessource#speicherkapazitaet)</span><span className="hbs-nr">01740</span> | Speicherkapazität<br/>Beispiel: QTY+Z42:100:KWH' | number (float) | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[verbrauchsart](/bo4e/202610/bo/TechnischeRessource#verbrauchsart)</span><span className="hbs-nr">01750</span> | Verbrauchsart der Technischen Ressource<br/>Beispiel: CAV+Z64'<br/>Z64: Kraft/Licht<br/>Z65: Wärme<br/>ZE5: E-Mobilität<br/>ZA8: Straßenbeleuchtung | array | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[verguetungsverpflichtung](/bo4e/202610/bo/TechnischeRessource#verguetungsverpflichtung)</span><span className="hbs-nr">01760</span> | verguetungsverpflichtung | boolean | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[waermenutzung](/bo4e/202610/bo/TechnischeRessource#waermenutzung)</span><span className="hbs-nr">01770</span> | Wärmenutzung<br/>Beispiel: CAV+Z56'<br/>Z56: Speicherheizung<br/>Z57: Wärmepumpe<br/>Z61: Direktheizung | [Enum Waermenutzung](/bo4e/202610/enum/Waermenutzung) | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`SPEICHERHEIZUNG`</span> | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`WAERMEPUMPE`</span> | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`DIREKTHEIZUNG`</span> | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`WAERMEPUMPE_WAERME_KAELTE`</span> | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`WAERMEPUMPE_KAELTE`</span> | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`WAERMEPUMPE_WAERME`</span> | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**nennleistung**</span> | — | object | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[abgabe](/bo4e/202610/com/Nennleistung#abgabe)</span><span className="hbs-nr">01780</span> | Abgabe der Nennleistung | number (float) | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[aufnahme](/bo4e/202610/com/Nennleistung#aufnahme)</span><span className="hbs-nr">01790</span> | Aufnahme der Nennleistung | number (float) | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-g hbs-e1">**VERWENDUNGSZEITRAUM** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | — | — | — | — | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | — |
| <span className="hbs-f hbs-e2">[datenqualitaet](/bo4e/202610/bo/Verwendungszeitraum#datenqualitaet) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">01800</span> | Datenqualitaet | [Enum Datenqualitaet](/bo4e/202610/enum/Datenqualitaet) | — | — | — | — | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`ERWARTETE_DATEN`</span> | — | — | — | — | — | — | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | — | — | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`INFORMATIVE_DATEN`</span> | — | — | — | — | — | — | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`GUELTIGE_DATEN`</span> | — | — | — | — | — | — | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN`</span> | — | — | — | — | — | — | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_KEINE_DATEN_VORHANDEN`</span> | — | — | — | — | — | — | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN_ERWARTET`</span> | — | — | — | — | — | — | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_DATEN`</span> | — | — | — | — | — | — | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_ERWARTETE_DATEN`</span> | — | — | — | — | — | — | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | — | — | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | — |
| <span className="hbs-f hbs-e2">[verwendungAb](/bo4e/202610/bo/Verwendungszeitraum#verwendungab) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">01810</span> | verwendungAb | string (date-time) | — | — | — | — | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | — |
| <span className="hbs-f hbs-e2">[verwendungBis](/bo4e/202610/bo/Verwendungszeitraum#verwendungbis)</span><span className="hbs-nr">01820</span> | verwendungBis | string (date-time) | — | — | — | — | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | — | — |
| <span className="hbs-f hbs-e2">[zeitraumId](/bo4e/202610/bo/Verwendungszeitraum#zeitraumid) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">01830</span> | zeitraumId | integer | — | — | — | — | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | — | — |
| <span className="hbs-g hbs-e1">**TRANCHE** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | — | — | — | — | — | — | — | — | — | — | — | Muss | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e2">[datenqualitaet](/bo4e/202610/bo/Tranche#datenqualitaet)</span><span className="hbs-nr">01840</span> | Datenqualitaet | [Enum Datenqualitaet](/bo4e/202610/enum/Datenqualitaet) | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`ERWARTETE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`INFORMATIVE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`GUELTIGE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_KEINE_DATEN_VORHANDEN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN_ERWARTET`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_ERWARTETE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e2">[tranchenId](/bo4e/202610/bo/Tranche#tranchenid) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">01850</span> | tranchenId | string | — | — | — | — | — | — | — | — | — | — | — | Muss | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e2">[verguetungEmpfaenger](/bo4e/202610/bo/Tranche#verguetungempfaenger)</span><span className="hbs-nr">01860</span> | VerguetungEmpfaenger | [Enum VerguetungEmpfaenger](/bo4e/202610/enum/VerguetungEmpfaenger) | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KUNDE`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`LIEFERANT`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**gueltigkeitszeitraum**</span> | — | object | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[zeitraumId](/bo4e/202610/com/Zeitraum#zeitraumid)</span><span className="hbs-nr">01870</span> | zeitraumId | integer | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e2">[bilanzkreis](/bo4e/202610/bo/Tranche#bilanzkreis)</span><span className="hbs-nr">01880</span> | bilanzkreis | string | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-g hbs-e2">**marktrollen** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[marktrolle](/bo4e/202610/bo/Marktteilnehmer#marktrolle)</span><span className="hbs-nr">01890</span> | Gibt im Klartext die Bezeichnung der Marktrolle an. | [Enum Marktrolle](/bo4e/202610/enum/Marktrolle) | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`NB`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`LF`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`MSB`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`MSBA`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`GMSB`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`MDL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`DL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`BKV`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`UENB`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`KUNDE-SELBST-NN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`MGV`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`EIV`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`RB`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`KUNDE`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`INTERESSENT`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`KN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`UBA`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`BIKO`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`ESA`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[rollencodenummer](/bo4e/202610/bo/Marktteilnehmer#rollencodenummer)</span><span className="hbs-nr">01900</span> | Gibt die Codenummer der Marktrolle an. | string | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |

</div>

</Handbuchsatz>

## Kette dieses Auslösers

Das Ereignis löst die Nachricht aus. Der Marktpartner antwortet mit einer der genannten Antworten, und danach schreibt die MACO APP den Vorgang in Ihr Backendsystem.

| Nachricht | Antworten | Schreibaufruf nach der Antwort |
|---|---|---|
| [44112](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44112) | [44115](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44115) | `POST /updateProcessData` |
| [44113](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44113) | [44115](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44115) | `POST /updateProcessData` |
| [44123](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44123) | [44124](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44124) | `POST /updateProcessData` |
| [44175](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44175) | [44176](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44176) | `POST /updateProcessData` |
| [55173](/schnittstellen/202610/pruefi/UTILMD/PI_55173) | — | — |
| [55175](/schnittstellen/202610/pruefi/UTILMD/PI_55175) | — | — |
| [55225](/schnittstellen/202610/pruefi/UTILMD/PI_55225) | — | — |
| [55615](/schnittstellen/202610/pruefi/UTILMD/PI_55615) | — | — |
| [55616](/schnittstellen/202610/pruefi/UTILMD/PI_55616) | — | — |
| [55617](/schnittstellen/202610/pruefi/UTILMD/PI_55617) | — | — |
| [55618](/schnittstellen/202610/pruefi/UTILMD/PI_55618) | — | — |
| [55619](/schnittstellen/202610/pruefi/UTILMD/PI_55619) | — | — |
| [55620](/schnittstellen/202610/pruefi/UTILMD/PI_55620) | — | — |
| [55627](/schnittstellen/202610/pruefi/UTILMD/PI_55627) | — | — |
| [55628](/schnittstellen/202610/pruefi/UTILMD/PI_55628) | — | — |
| [55629](/schnittstellen/202610/pruefi/UTILMD/PI_55629) | — | — |
| [55630](/schnittstellen/202610/pruefi/UTILMD/PI_55630) | — | — |
| [55632](/schnittstellen/202610/pruefi/UTILMD/PI_55632) | — | — |
| [55670](/schnittstellen/202610/pruefi/UTILMD/PI_55670) | — | — |
| [55688](/schnittstellen/202610/pruefi/UTILMD/PI_55688) | — | — |
| [55691](/schnittstellen/202610/pruefi/UTILMD/PI_55691) | [55692](/schnittstellen/202610/pruefi/UTILMD/PI_55692) | `POST /createProcessData`; `POST /updateProcessData` |

Dieses Ereignis löst Schritte in diesen Rollensichten aus:

| Prozess | Beteiligter | Regelwerk | Sparte |
|---|---|---|---|
| [Ergänzende Daten zum Lokationsbündel von NBA an NBN](/prozessdoku/202610/NB--NBA/awh-netzbetreiberwechsel-erganzende-daten-zum-lokationsbundel-von-nba-an-nbn) | NBA | AWH Netzbetreiberwechsel | Strom |
| [Stammdaten zur Bilanzkreistreue](/prozessdoku/202610/NB/GPKE-Teil4-stammdaten-zur-bilanzkreistreue) | NB | GPKE Teil 4 | Strom |
| [Stammdatenänderung vom NB (verantwortlich) ausgehend](/prozessdoku/202610/NB/GPKE-Teil4-stammdatenaenderung-vom-nb-verantwortlich-ausgehend) | NB | GPKE Teil 4 | Strom |
| [Anfrage zur Stammdatenänderung vom LF an NB (verantwortlich)](/prozessdoku/202610/NB/geli-gas-2-0-anfrage-zur-stammdatenanderung-vom-lf-an-nb-verantwortlich) | NBV | GeLi Gas 2.0 | Gas |
| [Stammdatenänderung vom NB (verantwortlich) ausgehend](/prozessdoku/202610/NB/geli-gas-2-0-stammdatenanderung-vom-nb-verantwortlich-ausgehend) | NB | GeLi Gas 2.0 | Gas |

## Transaktionsdaten

Der Umschlag der Nachricht. Pflichtfelder müssen beim Trigger-Aufruf gesetzt sein.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| [gueltigAb](/bo4e/202610/cdoc/Transaktionsdaten#gueltigab) | string (date-time) | **ja** | Gültigkeitsdatum/-zeit / DTM+7 |
| [kategorie](/bo4e/202610/cdoc/Transaktionsdaten#kategorie) | string | **ja** | Qualifier aus dem Beginn der EDIFact Nachricht / BGM |
| [sparte](/bo4e/202610/cdoc/Transaktionsdaten#sparte) | [Enum Sparte](/bo4e/202610/enum/Sparte) | **ja** | Enthält Informationen über die Sparte Werte: `STROM`, `GAS`, `FERNWAERME`, `NAHWAERME`, `WASSER`, `ABWASSER` |
| [transaktionsgrund](/bo4e/202610/cdoc/Transaktionsdaten#transaktionsgrund) | string | **ja** | Der Transaktionsgrund beschreibt den Geschäftsvorfall zur Kategorie genauer / UTILMD STS+7++###+ZW4+E03 |
| [transaktionsgrundergaenzung](/bo4e/202610/cdoc/Transaktionsdaten#transaktionsgrundergaenzung) | string | **ja** | Ergänzung zum Transaktionsgrund / UTILMD STS+7++E01+###+E03 |
| `pruefidentifikator` | — | nein | Wird dynamisch im Event-Prozess ermittelt (Entscheidungsgrundlage: marktrolle, sparte, transaktionsgrund). Ein vom Sender mitgegebener Wert wird ignoriert. Im Topic mögliche Prüfis — 44112, 44113, 44123, 44175, 55173, 55175, 55225, 55615, 55616, 55617, 55618, 55619, 55620, 55627, 55628, 55629, 55630, 55632, 55670, 55688, 55691. Mögliche Werte: `44112`, `44113`, `44123`, `44175`, `55173`, `55175`, `55225`, `55615`, `55616`, `55617`, `55618`, `55619`, `55620`, `55627`, `55628`, `55629`, `55630`, `55632`, `55670`, `55688`, `55691` |
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
