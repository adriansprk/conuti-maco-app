# [MSB] START_VERSAND_SDAE
<span hidden data-pagefind-meta={"title:Trigger-Ereignis START_VERSAND_SDAE — Marktrolle MSB (FV 202604)"} />

Marktrolle **MSB** · Formatversion **202604** · BO4E-Schema **1.7.8**

## Stammdaten

Unter diesem Topic ist genau einer der folgenden 21 Prüfidentifikatoren zulässig — welcher, entscheidet der Event-Prozess.

| Prüfi | Scope | Anwendungsfall | Festlegung | Kommunikation |
|---|---|---|---|---|
| [PI_44116](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44116) | UTILMD_GAS | Änderung vom MSB mit Abhängigkeiten | GeLi Gas 2.0 | MSB → NB |
| [PI_44159](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44159) | UTILMD_GAS | Änderung vom MSB ohne Abhängigkeiten | GeLi Gas 2.0 | MSB → NB |
| [PI_55553](/schnittstellen/202604/pruefi/UTILMD/PI_55553) | UTILMD | Daten auf individuelle Bestellung | GPKE Teil 4 | MSB → NB |
| [PI_55557](/schnittstellen/202604/pruefi/UTILMD/PI_55557) | UTILMD | Änderung MSB-Abr.-Daten der MaLo | GPKE Teil 4 | MSB → NB |
| [PI_55639](/schnittstellen/202604/pruefi/UTILMD/PI_55639) | UTILMD | Änderung Daten der NeLo | GPKE Teil 4 | MSB → NB |
| [PI_55640](/schnittstellen/202604/pruefi/UTILMD/PI_55640) | UTILMD | Änderung Daten der MaLo | GPKE Teil 4 | MSB → NB |
| [PI_55641](/schnittstellen/202604/pruefi/UTILMD/PI_55641) | UTILMD | Änderung Daten der SR | GPKE Teil 4 | MSB → NB |
| [PI_55642](/schnittstellen/202604/pruefi/UTILMD/PI_55642) | UTILMD | Änderung Daten der Tranche | GPKE Teil 4 | MSB → NB |
| [PI_55643](/schnittstellen/202604/pruefi/UTILMD/PI_55643) | UTILMD | Änderung Daten der MeLo | GPKE Teil 4 | MSB → NB |
| [PI_55649](/schnittstellen/202604/pruefi/UTILMD/PI_55649) | UTILMD | Änderung Daten der NeLo | GPKE Teil 4 | MSB → LF |
| [PI_55650](/schnittstellen/202604/pruefi/UTILMD/PI_55650) | UTILMD | Änderung Daten der MaLo | GPKE Teil 4 | MSB → LF |
| [PI_55651](/schnittstellen/202604/pruefi/UTILMD/PI_55651) | UTILMD | Änderung Daten der SR | GPKE Teil 4 | MSB → LF |
| [PI_55652](/schnittstellen/202604/pruefi/UTILMD/PI_55652) | UTILMD | Änderung Daten der Tranche | GPKE Teil 4 | MSB → LF |
| [PI_55653](/schnittstellen/202604/pruefi/UTILMD/PI_55653) | UTILMD | Änderung Daten der MeLo | GPKE Teil 4 | MSB → LF |
| [PI_55659](/schnittstellen/202604/pruefi/UTILMD/PI_55659) | UTILMD | Änderung Daten der NeLo | GPKE Teil 4 | MSB → weiterer MSB |
| [PI_55660](/schnittstellen/202604/pruefi/UTILMD/PI_55660) | UTILMD | Änderung Daten der MaLo | GPKE Teil 4 | MSB → weiterer MSB |
| [PI_55661](/schnittstellen/202604/pruefi/UTILMD/PI_55661) | UTILMD | Änderung Daten der SR | GPKE Teil 4 | MSB → weiterer MSB |
| [PI_55662](/schnittstellen/202604/pruefi/UTILMD/PI_55662) | UTILMD | Änderung Daten der Tranche | GPKE Teil 4 | MSB → weiterer MSB |
| [PI_55663](/schnittstellen/202604/pruefi/UTILMD/PI_55663) | UTILMD | Änderung Daten der MeLo | GPKE Teil 4 | MSB → weiterer MSB |
| [PI_55684](/schnittstellen/202604/pruefi/UTILMD/PI_55684) | UTILMD | Änderung Daten der MaLo | GPKE Teil 4 | MSB → ÜNB |
| [PI_55686](/schnittstellen/202604/pruefi/UTILMD/PI_55686) | UTILMD | Änderung Daten der Tranche | GPKE Teil 4 | MSB → ÜNB |

Die Stammdaten der 21 Prüfidentifikatoren in **einer** Struktur — eine Spalte je Prüfidentifikator, wie im Anwendungshandbuch. Ein Wert in der Spalte heißt, dass das Feld zu diesem Prüfidentifikator gehört: **Muss**, wenn seine Spezifikation es verlangt, sonst **Kann**. Eine leere Zelle heißt »gehört nicht dazu«, nicht »unbekannt«. Vorausgewählt ist der erste; die übrigen schaltet die Leiste über der Tabelle zu.

<Handbuchsatz>

<div className="maco-tabellenrahmen">

| Struktur (BO4E) | Beschreibung | Format | <span className="hbs-p" title="Änderung vom MSB mit Abhängigkeiten">44116</span> | <span className="hbs-p" title="Änderung vom MSB ohne Abhängigkeiten">44159</span> | <span className="hbs-p" title="Daten auf individuelle Bestellung">55553</span> | <span className="hbs-p" title="Änderung MSB-Abr.-Daten der MaLo">55557</span> | <span className="hbs-p" title="Änderung Daten der NeLo">55639</span> | <span className="hbs-p" title="Änderung Daten der MaLo">55640</span> | <span className="hbs-p" title="Änderung Daten der SR">55641</span> | <span className="hbs-p" title="Änderung Daten der Tranche">55642</span> | <span className="hbs-p" title="Änderung Daten der MeLo">55643</span> | <span className="hbs-p" title="Änderung Daten der NeLo">55649</span> | <span className="hbs-p" title="Änderung Daten der MaLo">55650</span> | <span className="hbs-p" title="Änderung Daten der SR">55651</span> | <span className="hbs-p" title="Änderung Daten der Tranche">55652</span> | <span className="hbs-p" title="Änderung Daten der MeLo">55653</span> | <span className="hbs-p" title="Änderung Daten der NeLo">55659</span> | <span className="hbs-p" title="Änderung Daten der MaLo">55660</span> | <span className="hbs-p" title="Änderung Daten der SR">55661</span> | <span className="hbs-p" title="Änderung Daten der Tranche">55662</span> | <span className="hbs-p" title="Änderung Daten der MeLo">55663</span> | <span className="hbs-p" title="Änderung Daten der MaLo">55684</span> | <span className="hbs-p" title="Änderung Daten der Tranche">55686</span> | Bedingung |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| <span className="hbs-g hbs-e0">**stammdaten**</span> | — | object | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | — |
| <span className="hbs-g hbs-e1">**MESSLOKATION** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | Muss | — | — | — | — | — | — | Muss | — | — | — | — | Muss | — | — | — | — | Muss | — | — | — |
| <span className="hbs-f hbs-e2">[messlokationsId](/bo4e/202604/bo/Messlokation#messlokationsid) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00010</span> | Die Messlokations-Identifikation. Das ist die frühere Zählpunktbezeichnung,<br/>z.B. DE 47108151234567 | string | Muss | Muss | — | — | — | — | — | — | Muss | — | — | — | — | Muss | — | — | — | — | Muss | — | — | — |
| <span className="hbs-g hbs-e2">**ablesekartenempfaenger**</span> | — | object | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[anrede](/bo4e/202604/bo/Geschaeftspartner#anrede)</span><span className="hbs-nr">00020</span> | Die Anrede für den GePa, Z.B. Herr. | string | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[gewerbekennzeichnung](/bo4e/202604/bo/Geschaeftspartner#gewerbekennzeichnung)</span><span className="hbs-nr">00030</span> | Kennzeichnung ob es sich um einen Gewerbe/Unternehmen (gewerbeKennzeichnung = true)<br/>oder eine Privatperson handelt. (gewerbeKennzeichnung = false) | boolean | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[name1](/bo4e/202604/bo/Geschaeftspartner#name1)</span><span className="hbs-nr">00040</span> | Erster Teil des Namens. Hier kann der Firmenname oder bei Privatpersonen<br/>beispielsweise der Nachname dargestellt werden. Beispiele: Yellow Strom GmbH<br/>oder Hagen | string | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[name2](/bo4e/202604/bo/Geschaeftspartner#name2)</span><span className="hbs-nr">00050</span> | Zweiter Teil des Namens. Hier kann der eine Erweiterung zum Firmennamen oder<br/>bei Privatpersonen beispielsweise der Vorname dargestellt werden. Beispiele:<br/>Bereich Süd oder Nina | string | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[name3](/bo4e/202604/bo/Geschaeftspartner#name3)</span><span className="hbs-nr">00060</span> | Dritter Teil des Namens. Hier können weitere Ergänzungen zum Firmennamen oder<br/>bei Privatpersonen Zusätze zum Namen dargestellt werden. Beispiele: und Afrika<br/>oder Sängerin | string | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[name4](/bo4e/202604/bo/Geschaeftspartner#name4)</span><span className="hbs-nr">00070</span> | name4 | string | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-g hbs-e3">**partneradresse**</span> | — | object | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e4">[hausnummer](/bo4e/202604/com/Adresse#hausnummer)</span><span className="hbs-nr">00080</span> | Hausnummer und Ergänzung | string | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e4">[landescode](/bo4e/202604/com/Adresse#landescode)</span><span className="hbs-nr">00090</span> | Landescode | [Enum Landescode](/bo4e/202604/enum/Landescode) | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AC`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AD`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AE`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AF`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AG`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AI`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AL`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AM`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AN`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AO`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AQ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AR`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AS`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AT`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AU`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AW`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AX`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AZ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BA`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BB`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BD`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BE`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BF`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BG`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BH`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BI`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BJ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BL`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BM`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BN`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BO`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BQ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BR`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BS`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BT`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BU`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BV`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BW`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BY`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BZ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CA`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CC`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CD`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CF`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CG`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CH`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CI`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CK`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CL`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CM`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CN`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CO`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CP`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CR`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CS`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CU`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CV`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CW`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CX`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CY`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CZ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`DE`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`DG`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`DJ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`DK`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`DM`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`DO`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`DZ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`EA`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`EC`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`EE`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`EG`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`EH`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`ER`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`ES`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`ET`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`EU`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`FI`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`FJ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`FK`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`FM`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`FO`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`FR`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`FX`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GA`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GB`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GD`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GE`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GF`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GG`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GH`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GI`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GL`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GM`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GN`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GP`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GQ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GR`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GS`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GT`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GU`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GW`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GY`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`HK`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`HM`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`HN`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`HR`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`HT`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`HU`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`IC`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`ID`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`IE`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`IL`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`IM`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`IN`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`IO`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`IQ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`IR`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`IS`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`IT`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`JE`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`JM`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`JO`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`JP`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`KE`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`KG`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`KH`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`KI`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`KM`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`KN`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`KP`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`KR`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`KW`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`KY`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`KZ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`LA`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`LB`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`LC`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`LI`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`LK`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`LR`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`LS`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`LT`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`LU`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`LV`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`LY`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MA`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MC`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MD`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`ME`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MF`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MG`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MH`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MK`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`ML`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MM`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MN`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MO`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MP`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MQ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MR`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MS`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MT`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MU`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MV`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MW`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MX`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MY`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MZ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`NA`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`NC`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`NE`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`NF`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`NG`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`NI`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`NL`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`NO`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`NP`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`NR`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`NT`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`NU`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`NZ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`OM`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`PA`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`PE`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`PF`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`PG`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`PH`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`PK`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`PL`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`PM`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`PN`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`PR`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`PS`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`PT`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`PW`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`PY`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`QA`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`RE`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`RO`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`RS`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`RU`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`RW`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SA`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SB`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SC`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SD`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SE`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SF`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SG`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SH`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SI`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SJ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SK`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SL`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SM`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SN`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SO`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SR`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SS`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`ST`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SU`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SV`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SX`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SY`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SZ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TA`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TC`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TD`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TF`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TG`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TJ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TK`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TL`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TM`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TN`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TO`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TP`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TR`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TT`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TV`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TW`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TZ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`UA`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`UG`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`UK`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`UM`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`US`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`UY`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`UZ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`VA`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`VC`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`VE`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`VG`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`VI`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`VN`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`VU`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`WF`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`WS`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`XK`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`YE`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`YT`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`YU`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`ZA`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`ZM`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`ZR`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`ZW`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e4">[ort](/bo4e/202604/com/Adresse#ort)</span><span className="hbs-nr">00100</span> | Ort | string | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e4">[ortsteil](/bo4e/202604/com/Adresse#ortsteil)</span><span className="hbs-nr">00110</span> | Ortsteil | string | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e4">[postfach](/bo4e/202604/com/Adresse#postfach)</span><span className="hbs-nr">00120</span> | Postfach | string | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e4">[postleitzahl](/bo4e/202604/com/Adresse#postleitzahl)</span><span className="hbs-nr">00130</span> | Postleitzahl | string | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e4">[strasse](/bo4e/202604/com/Adresse#strasse)</span><span className="hbs-nr">00140</span> | Strasse | string | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-g hbs-e2">**messadresse**</span> | — | object | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[hausnummer](/bo4e/202604/com/Adresse#hausnummer)</span><span className="hbs-nr">00150</span> | Hausnummer und Ergänzung | string | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[landescode](/bo4e/202604/com/Adresse#landescode)</span><span className="hbs-nr">00160</span> | Landescode | [Enum Landescode](/bo4e/202604/enum/Landescode) | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`AC`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`AD`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`AE`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`AF`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`AG`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`AI`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`AL`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`AM`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`AN`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`AO`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`AQ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`AR`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`AS`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`AT`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`AU`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`AW`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`AX`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`AZ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`BA`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`BB`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`BD`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`BE`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`BF`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`BG`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`BH`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`BI`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`BJ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`BL`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`BM`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`BN`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`BO`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`BQ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`BR`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`BS`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`BT`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`BU`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`BV`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`BW`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`BY`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`BZ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`CA`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`CC`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`CD`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`CF`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`CG`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`CH`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`CI`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`CK`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`CL`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`CM`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`CN`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`CO`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`CP`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`CR`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`CS`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`CU`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`CV`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`CW`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`CX`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`CY`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`CZ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`DE`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`DG`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`DJ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`DK`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`DM`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`DO`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`DZ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`EA`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`EC`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`EE`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`EG`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`EH`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`ER`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`ES`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`ET`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`EU`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`FI`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`FJ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`FK`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`FM`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`FO`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`FR`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`FX`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`GA`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`GB`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`GD`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`GE`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`GF`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`GG`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`GH`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`GI`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`GL`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`GM`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`GN`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`GP`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`GQ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`GR`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`GS`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`GT`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`GU`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`GW`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`GY`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`HK`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`HM`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`HN`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`HR`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`HT`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`HU`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`IC`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`ID`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`IE`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`IL`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`IM`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`IN`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`IO`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`IQ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`IR`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`IS`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`IT`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`JE`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`JM`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`JO`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`JP`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`KE`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`KG`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`KH`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`KI`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`KM`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`KN`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`KP`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`KR`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`KW`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`KY`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`KZ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`LA`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`LB`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`LC`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`LI`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`LK`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`LR`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`LS`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`LT`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`LU`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`LV`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`LY`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`MA`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`MC`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`MD`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`ME`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`MF`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`MG`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`MH`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`MK`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`ML`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`MM`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`MN`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`MO`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`MP`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`MQ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`MR`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`MS`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`MT`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`MU`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`MV`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`MW`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`MX`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`MY`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`MZ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`NA`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`NC`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`NE`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`NF`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`NG`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`NI`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`NL`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`NO`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`NP`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`NR`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`NT`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`NU`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`NZ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`OM`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`PA`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`PE`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`PF`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`PG`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`PH`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`PK`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`PL`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`PM`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`PN`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`PR`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`PS`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`PT`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`PW`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`PY`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`QA`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`RE`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`RO`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`RS`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`RU`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`RW`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`SA`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`SB`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`SC`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`SD`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`SE`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`SF`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`SG`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`SH`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`SI`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`SJ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`SK`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`SL`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`SM`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`SN`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`SO`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`SR`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`SS`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`ST`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`SU`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`SV`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`SX`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`SY`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`SZ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`TA`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`TC`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`TD`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`TF`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`TG`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`TJ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`TK`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`TL`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`TM`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`TN`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`TO`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`TP`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`TR`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`TT`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`TV`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`TW`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`TZ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`UA`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`UG`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`UK`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`UM`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`US`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`UY`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`UZ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`VA`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`VC`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`VE`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`VG`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`VI`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`VN`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`VU`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`WF`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`WS`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`XK`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`YE`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`YT`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`YU`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`ZA`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`ZM`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`ZR`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`ZW`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[ort](/bo4e/202604/com/Adresse#ort)</span><span className="hbs-nr">00170</span> | Ort | string | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[ortsteil](/bo4e/202604/com/Adresse#ortsteil)</span><span className="hbs-nr">00180</span> | Ortsteil | string | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[postfach](/bo4e/202604/com/Adresse#postfach)</span><span className="hbs-nr">00190</span> | Postfach | string | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[postleitzahl](/bo4e/202604/com/Adresse#postleitzahl)</span><span className="hbs-nr">00200</span> | Postleitzahl | string | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[strasse](/bo4e/202604/com/Adresse#strasse)</span><span className="hbs-nr">00210</span> | Strasse | string | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-g hbs-e3">**zusatzInformation**</span> | — | object | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e4">[zusatz1](/bo4e/202604/com/AdresszusatzInformation#zusatz1)</span><span className="hbs-nr">00220</span> | Adresszusatz 1 | string | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e4">[zusatz2](/bo4e/202604/com/AdresszusatzInformation#zusatz2)</span><span className="hbs-nr">00230</span> | Adresszusatz 2 | string | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e4">[zusatz3](/bo4e/202604/com/AdresszusatzInformation#zusatz3)</span><span className="hbs-nr">00240</span> | Adresszusatz 3 | string | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e4">[zusatz4](/bo4e/202604/com/AdresszusatzInformation#zusatz4)</span><span className="hbs-nr">00250</span> | Adresszusatz 4 | string | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e4">[zusatz5](/bo4e/202604/com/AdresszusatzInformation#zusatz5)</span><span className="hbs-nr">00260</span> | Adresszusatz 5 | string | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e2">[datenqualitaet](/bo4e/202604/bo/Messlokation#datenqualitaet)</span><span className="hbs-nr">00270</span> | Datenqualitaet | [Enum Datenqualitaet](/bo4e/202604/enum/Datenqualitaet) | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`ERWARTETE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`INFORMATIVE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`GUELTIGE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_KEINE_DATEN_VORHANDEN`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN_ERWARTET`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_ERWARTETE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e2">[netzebenemessung](/bo4e/202604/bo/Messlokation#netzebenemessung)</span><span className="hbs-nr">00280</span> | Netzebene | [Enum Netzebene](/bo4e/202604/enum/Netzebene) | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`NSP`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`MSP`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`HSP`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`HSS`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`MSP_NSP_UMSP`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`HSP_MSP_UMSP`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`HSS_HSP_UMSP`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`HD`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`MD`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`ND`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-g hbs-e2">**gueltigkeitszeitraum**</span> | — | object | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[zeitraumId](/bo4e/202604/com/Zeitraum#zeitraumid)</span><span className="hbs-nr">00290</span> | zeitraumId | integer | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-g hbs-e1">**NETZNUTZUNGSVERTRAG** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[vertragsbeginn](/bo4e/202604/bo/Vertrag#vertragsbeginn)</span><span className="hbs-nr">00300</span> | Gibt an, wann der Vertrag beginnt. | string (date-time) | Kann | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e1">**ZAEHLER** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e2">[befestigungsart](/bo4e/202604/bo/Zaehler#befestigungsart) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00310</span> | Befestigungsart | [Enum Befestigungsart](/bo4e/202604/enum/Befestigungsart) | Muss | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`STECKTECHNIK`</span> | — | — | Muss | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`DREIPUNKT`</span> | — | — | Muss | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`HUTSCHIENE`</span> | — | — | Muss | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`EINSTUTZEN`</span> | — | — | Muss | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`ZWEISTUTZEN`</span> | — | — | Muss | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e2">[messlokationsId](/bo4e/202604/bo/Zaehler#messlokationsid) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00320</span> | messlokationsId | string | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[messwerterfassung](/bo4e/202604/bo/Zaehler#messwerterfassung) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00330</span> | Messwerterfassung am Zählpunkt | [Enum Messwerterfassung](/bo4e/202604/enum/Messwerterfassung) | Muss | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`FERNAUSLESBAR`</span> | — | — | Muss | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`MANUELL_AUSGELESENE`</span> | — | — | Muss | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e2">[volumenerfassung](/bo4e/202604/bo/Zaehler#volumenerfassung)</span><span className="hbs-nr">00340</span> | Volumenerfassung | [Enum Volumenerfassung](/bo4e/202604/enum/Volumenerfassung) | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`HOCHFREQUENZSONDE`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KENNLINIENKORREKTUR`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`SCHLEICHMENGENUNTERDRUECKUNG`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[zaehlergroesse](/bo4e/202604/bo/Zaehler#zaehlergroesse) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00350</span> | Zaehlergroesse | [Enum Geraetemerkmal](/bo4e/202604/enum/Geraetemerkmal) | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`EINTARIF`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`ZWEITARIF`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`MEHRTARIF`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`GAS_G2P5`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`GAS_G4`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`GAS_G6`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`GAS_G10`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`GAS_G16`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`GAS_G25`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`GAS_G40`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`GAS_G65`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`GAS_G100`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`GAS_G160`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`GAS_G250`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`GAS_G350`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`GAS_G400`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`GAS_G4000`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`GAS_G650`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`GAS_G6500`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`GAS_G1000`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`GAS_G10000`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`GAS_G12500`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`GAS_G1600`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`GAS_G16000`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`GAS_G2500`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`IMPULSGEBER_G4_G100`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`IMPULSGEBER_G100`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`MODEM_GSM`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`MODEM_GPRS`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`MODEM_FUNK`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`MODEM_GSM_O_LG`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`MODEM_GSM_M_LG`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`MODEM_FESTNETZ`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`MODEM_GPRS_M_LG`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`PLC_COM`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`ETHERNET_KOM`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`DSL_KOM`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`LTE_KOM`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`RUNDSTEUEREMPFAENGER`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`TARIFSCHALTGERAET`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`ZUSTANDS_MU`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`TEMPERATUR_MU`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KOMPAKT_MU`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`SYSTEM_MU`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`UNBESTIMMT`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`WASSER_MWZW`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`WASSER_WZWW`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`WASSER_WZ01`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`WASSER_WZ02`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`WASSER_WZ03`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`WASSER_WZ04`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`WASSER_WZ05`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`WASSER_WZ06`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`WASSER_WZ07`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`WASSER_WZ08`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`WASSER_WZ09`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`WASSER_WZ10`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`WASSER_VWZ04`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`WASSER_VWZ05`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`WASSER_VWZ06`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`WASSER_VWZ07`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`WASSER_VWZ10`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`DICHTEMENGENUMWERTER`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`TEMPERATURMENGENUMWERTER`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`ZUSTANDSMENGENUMWERTER`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`BLOCKSTROMWANDLER`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`MESSWANDLERSATZ_IMS_MME`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KOMBIMESSWANDLER`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`SPANNUNGSWANDLER`</span> | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[zaehlernummer](/bo4e/202604/bo/Zaehler#zaehlernummer) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00360</span> | Nummerierung des Zählers, vergeben durch den Messstellenbetreiber | string | Muss | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e2">[zaehlertyp](/bo4e/202604/bo/Zaehler#zaehlertyp) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00370</span> | Typisierung des Zählers | [Enum Zaehlertyp](/bo4e/202604/enum/Zaehlertyp) | Muss | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`DREHSTROMZAEHLER`</span> | — | — | Muss | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`BALGENGASZAEHLER`</span> | — | — | Muss | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`DREHKOLBENZAEHLER`</span> | — | — | Muss | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`SMARTMETER`</span> | — | — | Muss | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`LEISTUNGSZAEHLER`</span> | — | — | Muss | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`MAXIMUMZAEHLER`</span> | — | — | Muss | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`TURBINENRADGASZAEHLER`</span> | — | — | Muss | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`ULTRASCHALLGASZAEHLER`</span> | — | — | Muss | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`WECHSELSTROMZAEHLER`</span> | — | — | Muss | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`WIRBELGASZAEHLER`</span> | — | — | Muss | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`MESSDATENREGISTRIERGERAET`</span> | — | — | Muss | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`ELEKTRONISCHERHAUSHALTSZAEHLER`</span> | — | — | Muss | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`SONDERAUSSTATTUNG`</span> | — | — | Muss | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`WASSERZAEHLER`</span> | — | — | Muss | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`MODERNEMESSEINRICHTUNG`</span> | — | — | Muss | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e2">[zaehlertypspezifikation](/bo4e/202604/bo/Zaehler#zaehlertypspezifikation)</span><span className="hbs-nr">00380</span> | Typisierung des Zählers (spezifikation für EHZ und MME) | [Enum ZaehlertypSpezifikation](/bo4e/202604/enum/ZaehlertypSpezifikation) | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`EDL40`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`EDL21`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`SONSTIGER_EHZ`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`MME_STANDARD`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`MME_MEDA`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-g hbs-e2">**geraete** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[geraetenummer](/bo4e/202604/com/Geraet#geraetenummer)</span><span className="hbs-nr">00390</span> | Die auf dem Geräte aufgedruckte Nummer, die vom MSB vergeben wird. | string | Kann | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-g hbs-e3">**geraeteeigenschaften**</span> | — | object | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e4">[geraetemerkmal](/bo4e/202604/com/Geraeteeigenschaften#geraetemerkmal)</span><span className="hbs-nr">00400</span> | Geraetemerkmal | [Enum Geraetemerkmal](/bo4e/202604/enum/Geraetemerkmal) | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`EINTARIF`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`ZWEITARIF`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MEHRTARIF`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GAS_G2P5`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GAS_G4`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GAS_G6`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GAS_G10`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GAS_G16`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GAS_G25`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GAS_G40`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GAS_G65`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GAS_G100`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GAS_G160`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GAS_G250`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GAS_G350`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GAS_G400`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GAS_G4000`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GAS_G650`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GAS_G6500`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GAS_G1000`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GAS_G10000`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GAS_G12500`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GAS_G1600`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GAS_G16000`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GAS_G2500`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`IMPULSGEBER_G4_G100`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`IMPULSGEBER_G100`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MODEM_GSM`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MODEM_GPRS`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MODEM_FUNK`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MODEM_GSM_O_LG`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MODEM_GSM_M_LG`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MODEM_FESTNETZ`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MODEM_GPRS_M_LG`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`PLC_COM`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`ETHERNET_KOM`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`DSL_KOM`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`LTE_KOM`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`RUNDSTEUEREMPFAENGER`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TARIFSCHALTGERAET`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`ZUSTANDS_MU`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TEMPERATUR_MU`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`KOMPAKT_MU`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SYSTEM_MU`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`UNBESTIMMT`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`WASSER_MWZW`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`WASSER_WZWW`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`WASSER_WZ01`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`WASSER_WZ02`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`WASSER_WZ03`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`WASSER_WZ04`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`WASSER_WZ05`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`WASSER_WZ06`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`WASSER_WZ07`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`WASSER_WZ08`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`WASSER_WZ09`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`WASSER_WZ10`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`WASSER_VWZ04`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`WASSER_VWZ05`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`WASSER_VWZ06`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`WASSER_VWZ07`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`WASSER_VWZ10`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`DICHTEMENGENUMWERTER`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TEMPERATURMENGENUMWERTER`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`ZUSTANDSMENGENUMWERTER`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BLOCKSTROMWANDLER`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MESSWANDLERSATZ_IMS_MME`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`KOMBIMESSWANDLER`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SPANNUNGSWANDLER`</span> | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e4">[volumenerfassung](/bo4e/202604/com/Geraeteeigenschaften#volumenerfassung)</span><span className="hbs-nr">00410</span> | Volumenerfassung | [Enum Volumenerfassung](/bo4e/202604/enum/Volumenerfassung) | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`HOCHFREQUENZSONDE`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KENNLINIENKORREKTUR`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SCHLEICHMENGENUNTERDRUECKUNG`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[faktor](/bo4e/202604/com/Geraeteeigenschaften#faktor)</span><span className="hbs-nr">00420</span> | faktor | number (float) | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[geraetetyp](/bo4e/202604/com/Geraet#geraetetyp)</span><span className="hbs-nr">00430</span> | Auflistung möglicher abzurechnender Gerätetypen | [Enum Geraetetyp](/bo4e/202604/enum/Geraetetyp) | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`WECHSELSTROMZAEHLER`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`DREHSTROMZAEHLER`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`ZWEIRICHTUNGSZAEHLER`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`RLM_ZAEHLER`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`IMS_ZAEHLER`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`BALGENGASZAEHLER`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`MAXIMUMZAEHLER`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`MULTIPLEXANLAGE`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`PAUSCHALANLAGE`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`VERSTAERKERANLAGE`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`SUMMATIONSGERAET`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`IMPULSGEBER`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`EDL_21_ZAEHLERAUFSATZ`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`VIER_QUADRANTEN_LASTGANGZAEHLER`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`MENGENUMWERTER`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`STROMWANDLER`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`SPANNUNGSWANDLER`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`DATENLOGGER`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`KOMMUNIKATIONSANSCHLUSS`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`MODEM`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`TELEKOMMUNIKATIONSEINRICHTUNG`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`KOMMUNIKATIONSEINRICHTUNG`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`DREHKOLBENGASZAEHLER`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`TURBINENRADGASZAEHLER`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`ULTRASCHALLZAEHLER`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`WIRBELGASZAEHLER`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`MODERNE_MESSEINRICHTUNG`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`ELEKTRONISCHER_HAUSHALTSZAEHLER`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`STEUEREINRICHTUNG`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`TECHNISCHESTEUEREINRICHTUNG`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`TARIFSCHALTGERAET`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`RUNDSTEUEREMPFAENGER`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`OPTIONALE_ZUS_ZAEHLEINRICHTUNG`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`MESSWANDLERSATZ_IMS_MME`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`KOMBIMESSWANDLER_IMS_MME`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`TARIFSCHALTGERAET_IMS_MME`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`RUNDSTEUEREMPFAENGER_IMS_MME`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`TEMPERATUR_KOMPENSATION`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`HOECHSTBELASTUNGS_ANZEIGER`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`SONSTIGES_GERAET`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`SMARTMETERGATEWAY`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`STEUERBOX`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`BLOCKSTROMWANDLER`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`KOMBIMESSWANDLER`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`MODEM_GSM`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`ETHERNET_KOM`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`PLC_COM`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`MODEM_FESTNETZ`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`DSL_KOM`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`LTE_KOM`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`DICHTEMENGENUMWERTER`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`TEMPERATURMENGENUMWERTER`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`ZUSTANDSMENGENUMWERTER`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`MESSDATENREGISTRIERGERAET`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`WANDLER`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`BEFESTIGUNGSEINRICHTUNG`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[weitereGeraetenummern](/bo4e/202604/com/Geraet#weiteregeraetenummern)</span><span className="hbs-nr">00440</span> | weitereGeraetenummern | array | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-g hbs-e2">**zaehlwerke** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[bezeichnung](/bo4e/202604/com/Zaehlwerk#bezeichnung)</span><span className="hbs-nr">00450</span> | Zusätzliche Bezeichnung, z.B. Zählwerk_Wirkarbeit. | string | Kann | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[nachkommastelle](/bo4e/202604/com/Zaehlwerk#nachkommastelle)</span><span className="hbs-nr">00460</span> | nachkommastelle | integer | Kann | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[obisKennzahl](/bo4e/202604/com/Zaehlwerk#obiskennzahl)</span><span className="hbs-nr">00470</span> | Die OBIS-Kennzahl für das Zählwerk, die festlegt, welche auf die gemessene Größe mit dem Stand gemeldet wird.<br/>Nur Zählwerkstände mit dieser OBIS-Kennzahl werden an diesem Zählwerk registriert. Beispiel:1-0:1.8.1 für<br/>elektrische Wirkarbeit. | string | Kann | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[vorkommastelle](/bo4e/202604/com/Zaehlwerk#vorkommastelle)</span><span className="hbs-nr">00480</span> | vorkommastelle | integer | Kann | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[wertegranularitaet](/bo4e/202604/com/Zaehlwerk#wertegranularitaet)</span><span className="hbs-nr">00490</span> | Wertegranularitaet | [Enum Wertegranularitaet](/bo4e/202604/enum/Wertegranularitaet) | Kann | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`JAEHRLICH`</span> | — | — | Kann | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`HALBJAEHRLICH`</span> | — | — | Kann | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`QUARTALSWEISE`</span> | — | — | Kann | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`MONATLICH`</span> | — | — | Kann | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[konfiguration](/bo4e/202604/com/Zaehlwerk#konfiguration)</span><span className="hbs-nr">00500</span> | Konfiguration (iMSys) des Zählwerks | string | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-g hbs-e3">**zaehlzeiten**</span> | — | object | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e4">[register](/bo4e/202604/com/Zaehlzeitregister#register)</span><span className="hbs-nr">00510</span> | Zählzeitregister | string | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e4">[zaehlzeitDefinition](/bo4e/202604/com/Zaehlzeitregister#zaehlzeitdefinition)</span><span className="hbs-nr">00520</span> | Zählzeitdefinition | string | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[schwachlastfaehig](/bo4e/202604/com/Zaehlwerk#schwachlastfaehig)</span><span className="hbs-nr">00530</span> | schwachlastfaehig | [Enum Schwachlastfaehig](/bo4e/202604/enum/Schwachlastfaehig) | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`SCHWACHLASTFAEHIG`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`NICHT_SCHWACHLASTFAEHIG`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e2">[datenqualitaet](/bo4e/202604/bo/Zaehler#datenqualitaet)</span><span className="hbs-nr">00540</span> | Datenqualitaet | [Enum Datenqualitaet](/bo4e/202604/enum/Datenqualitaet) | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`ERWARTETE_DATEN`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`INFORMATIVE_DATEN`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`GUELTIGE_DATEN`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_KEINE_DATEN_VORHANDEN`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN_ERWARTET`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_DATEN`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_ERWARTETE_DATEN`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e2">[gateway](/bo4e/202604/bo/Zaehler#gateway)</span><span className="hbs-nr">00550</span> | Angabe eines SMGW, mit dem der Zaehler parametrisiert ist | string | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-g hbs-e2">**gueltigkeitszeitraum**</span> | — | object | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[zeitraumId](/bo4e/202604/com/Zeitraum#zeitraumid)</span><span className="hbs-nr">00560</span> | zeitraumId | integer | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e2">[fernschaltung](/bo4e/202604/bo/Zaehler#fernschaltung)</span><span className="hbs-nr">00570</span> | Fernschaltung | [Enum Fernschaltung](/bo4e/202604/enum/Fernschaltung) | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`VORHANDEN`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`NICHT_VORHANDEN`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e2">[tarifart](/bo4e/202604/bo/Zaehler#tarifart)</span><span className="hbs-nr">00580</span> | Spezifikation bezüglich unterstützter Tarifarten. | [Enum Tarifart](/bo4e/202604/enum/Tarifart) | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`EINTARIF`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`ZWEITARIF`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`MEHRTARIF`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`SMART_METER`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`LEISTUNGSGEMESSEN`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e2">[zaehlerauspraegung](/bo4e/202604/bo/Zaehler#zaehlerauspraegung)</span><span className="hbs-nr">00590</span> | Spezifikation die Richtung des Zählers betreffend. | [Enum Zaehlerauspraegung](/bo4e/202604/enum/Zaehlerauspraegung) | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`EINRICHTUNGSZAEHLER`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`ZWEIRICHTUNGSZAEHLER`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-g hbs-e1">**MESSSTELLENBETRIEBSVERTRAG** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | Kann | — | — | — | Kann | — | — | Kann | — | Kann | — | — | — | — | Kann | — | — | Kann | — | — | — |
| <span className="hbs-g hbs-e2">**korrespondenzpartner**</span> | — | object | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[anrede](/bo4e/202604/bo/Geschaeftspartner#anrede)</span><span className="hbs-nr">00600</span> | Die Anrede für den GePa, Z.B. Herr. | string | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[gewerbekennzeichnung](/bo4e/202604/bo/Geschaeftspartner#gewerbekennzeichnung)</span><span className="hbs-nr">00610</span> | Kennzeichnung ob es sich um einen Gewerbe/Unternehmen (gewerbeKennzeichnung = true)<br/>oder eine Privatperson handelt. (gewerbeKennzeichnung = false) | boolean | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[name1](/bo4e/202604/bo/Geschaeftspartner#name1)</span><span className="hbs-nr">00620</span> | Erster Teil des Namens. Hier kann der Firmenname oder bei Privatpersonen<br/>beispielsweise der Nachname dargestellt werden. Beispiele: Yellow Strom GmbH<br/>oder Hagen | string | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[name2](/bo4e/202604/bo/Geschaeftspartner#name2)</span><span className="hbs-nr">00630</span> | Zweiter Teil des Namens. Hier kann der eine Erweiterung zum Firmennamen oder<br/>bei Privatpersonen beispielsweise der Vorname dargestellt werden. Beispiele:<br/>Bereich Süd oder Nina | string | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[name3](/bo4e/202604/bo/Geschaeftspartner#name3)</span><span className="hbs-nr">00640</span> | Dritter Teil des Namens. Hier können weitere Ergänzungen zum Firmennamen oder<br/>bei Privatpersonen Zusätze zum Namen dargestellt werden. Beispiele: und Afrika<br/>oder Sängerin | string | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[name4](/bo4e/202604/bo/Geschaeftspartner#name4)</span><span className="hbs-nr">00650</span> | name4 | string | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-g hbs-e3">**partneradresse**</span> | — | object | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e4">[hausnummer](/bo4e/202604/com/Adresse#hausnummer)</span><span className="hbs-nr">00660</span> | Hausnummer und Ergänzung | string | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e4">[landescode](/bo4e/202604/com/Adresse#landescode)</span><span className="hbs-nr">00670</span> | Landescode | [Enum Landescode](/bo4e/202604/enum/Landescode) | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AC`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AD`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AE`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AF`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AG`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AI`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AL`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AM`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AN`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AO`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AQ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AR`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AS`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AT`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AU`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AW`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AX`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AZ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BA`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BB`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BD`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BE`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BF`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BG`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BH`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BI`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BJ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BL`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BM`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BN`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BO`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BQ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BR`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BS`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BT`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BU`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BV`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BW`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BY`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BZ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CA`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CC`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CD`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CF`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CG`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CH`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CI`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CK`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CL`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CM`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CN`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CO`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CP`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CR`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CS`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CU`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CV`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CW`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CX`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CY`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CZ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`DE`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`DG`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`DJ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`DK`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`DM`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`DO`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`DZ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`EA`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`EC`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`EE`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`EG`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`EH`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`ER`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`ES`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`ET`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`EU`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`FI`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`FJ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`FK`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`FM`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`FO`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`FR`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`FX`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GA`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GB`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GD`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GE`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GF`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GG`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GH`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GI`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GL`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GM`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GN`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GP`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GQ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GR`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GS`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GT`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GU`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GW`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GY`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`HK`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`HM`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`HN`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`HR`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`HT`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`HU`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`IC`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`ID`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`IE`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`IL`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`IM`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`IN`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`IO`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`IQ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`IR`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`IS`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`IT`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`JE`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`JM`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`JO`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`JP`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`KE`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`KG`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`KH`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`KI`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`KM`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`KN`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`KP`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`KR`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`KW`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`KY`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`KZ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`LA`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`LB`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`LC`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`LI`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`LK`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`LR`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`LS`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`LT`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`LU`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`LV`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`LY`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MA`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MC`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MD`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`ME`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MF`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MG`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MH`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MK`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`ML`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MM`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MN`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MO`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MP`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MQ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MR`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MS`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MT`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MU`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MV`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MW`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MX`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MY`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MZ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`NA`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`NC`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`NE`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`NF`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`NG`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`NI`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`NL`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`NO`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`NP`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`NR`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`NT`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`NU`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`NZ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`OM`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`PA`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`PE`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`PF`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`PG`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`PH`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`PK`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`PL`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`PM`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`PN`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`PR`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`PS`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`PT`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`PW`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`PY`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`QA`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`RE`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`RO`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`RS`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`RU`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`RW`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SA`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SB`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SC`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SD`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SE`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SF`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SG`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SH`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SI`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SJ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SK`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SL`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SM`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SN`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SO`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SR`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SS`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`ST`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SU`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SV`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SX`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SY`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SZ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TA`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TC`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TD`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TF`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TG`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TJ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TK`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TL`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TM`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TN`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TO`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TP`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TR`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TT`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TV`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TW`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TZ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`UA`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`UG`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`UK`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`UM`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`US`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`UY`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`UZ`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`VA`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`VC`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`VE`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`VG`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`VI`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`VN`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`VU`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`WF`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`WS`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`XK`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`YE`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`YT`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`YU`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`ZA`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`ZM`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`ZR`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`ZW`</span> | — | — | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e4">[ort](/bo4e/202604/com/Adresse#ort)</span><span className="hbs-nr">00680</span> | Ort | string | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e4">[ortsteil](/bo4e/202604/com/Adresse#ortsteil)</span><span className="hbs-nr">00690</span> | Ortsteil | string | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e4">[postfach](/bo4e/202604/com/Adresse#postfach)</span><span className="hbs-nr">00700</span> | Postfach | string | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e4">[postleitzahl](/bo4e/202604/com/Adresse#postleitzahl)</span><span className="hbs-nr">00710</span> | Postleitzahl | string | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e4">[strasse](/bo4e/202604/com/Adresse#strasse)</span><span className="hbs-nr">00720</span> | Strasse | string | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-g hbs-e2">**vertragspartner2** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[anrede](/bo4e/202604/bo/Geschaeftspartner#anrede)</span><span className="hbs-nr">00730</span> | Die Anrede für den GePa, Z.B. Herr. | string | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[gewerbekennzeichnung](/bo4e/202604/bo/Geschaeftspartner#gewerbekennzeichnung)</span><span className="hbs-nr">00740</span> | Kennzeichnung ob es sich um einen Gewerbe/Unternehmen (gewerbeKennzeichnung = true)<br/>oder eine Privatperson handelt. (gewerbeKennzeichnung = false) | boolean | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[name1](/bo4e/202604/bo/Geschaeftspartner#name1)</span><span className="hbs-nr">00750</span> | Erster Teil des Namens. Hier kann der Firmenname oder bei Privatpersonen<br/>beispielsweise der Nachname dargestellt werden. Beispiele: Yellow Strom GmbH<br/>oder Hagen | string | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[name2](/bo4e/202604/bo/Geschaeftspartner#name2)</span><span className="hbs-nr">00760</span> | Zweiter Teil des Namens. Hier kann der eine Erweiterung zum Firmennamen oder<br/>bei Privatpersonen beispielsweise der Vorname dargestellt werden. Beispiele:<br/>Bereich Süd oder Nina | string | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[name3](/bo4e/202604/bo/Geschaeftspartner#name3)</span><span className="hbs-nr">00770</span> | Dritter Teil des Namens. Hier können weitere Ergänzungen zum Firmennamen oder<br/>bei Privatpersonen Zusätze zum Namen dargestellt werden. Beispiele: und Afrika<br/>oder Sängerin | string | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[name4](/bo4e/202604/bo/Geschaeftspartner#name4)</span><span className="hbs-nr">00780</span> | name4 | string | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[geschaeftspartnerrolle](/bo4e/202604/bo/Geschaeftspartner#geschaeftspartnerrolle)</span><span className="hbs-nr">00790</span> | Rolle, die der Geschäftspartner hat (z.B. Interessent, Kunde). | array | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-g hbs-e2">**vertragskonditionen**</span> | — | object | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-g hbs-e3">**geplanteTurnusablesung**</span> | — | object | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[ableseZeitraum](/bo4e/202604/com/Zeitraum#ablesezeitraum)</span><span className="hbs-nr">00800</span> | ableseZeitraum | string | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[datenqualitaet](/bo4e/202604/bo/Vertrag#datenqualitaet)</span><span className="hbs-nr">00810</span> | Datenqualitaet | [Enum Datenqualitaet](/bo4e/202604/enum/Datenqualitaet) | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`ERWARTETE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`INFORMATIVE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`GUELTIGE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_KEINE_DATEN_VORHANDEN`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN_ERWARTET`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_ERWARTETE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-g hbs-e2">**gueltigkeitszeitraum**</span> | — | object | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[zeitraumId](/bo4e/202604/com/Zeitraum#zeitraumid)</span><span className="hbs-nr">00820</span> | zeitraumId | integer | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-g hbs-e1">**AD_HOC_STEUERKANAL** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**IPAdresseCLSDevice**</span> | — | object | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[IPAdresseCLSDevice1](/bo4e/202604/com/IPAdresseCLSDevice#ipadresseclsdevice1)</span><span className="hbs-nr">00830</span> | IPAdresseCLSDevice1 | string | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[IPAdresseCLSDevice2](/bo4e/202604/com/IPAdresseCLSDevice#ipadresseclsdevice2)</span><span className="hbs-nr">00840</span> | IPAdresseCLSDevice2 | string | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[IPAdresseCLSDevice3](/bo4e/202604/com/IPAdresseCLSDevice#ipadresseclsdevice3)</span><span className="hbs-nr">00850</span> | IPAdresseCLSDevice3 | string | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[IPAdresseCLSDevice4](/bo4e/202604/com/IPAdresseCLSDevice#ipadresseclsdevice4)</span><span className="hbs-nr">00860</span> | IPAdresseCLSDevice4 | string | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[IPAdresseCLSDevice5](/bo4e/202604/com/IPAdresseCLSDevice#ipadresseclsdevice5)</span><span className="hbs-nr">00870</span> | IPAdresseCLSDevice5 | string | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**aussteller**</span> | — | object | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[aussteller1](/bo4e/202604/com/Aussteller#aussteller1)</span><span className="hbs-nr">00880</span> | aussteller1 | string | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[aussteller2](/bo4e/202604/com/Aussteller#aussteller2)</span><span className="hbs-nr">00890</span> | aussteller2 | string | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[aussteller3](/bo4e/202604/com/Aussteller#aussteller3)</span><span className="hbs-nr">00900</span> | aussteller3 | string | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[aussteller4](/bo4e/202604/com/Aussteller#aussteller4)</span><span className="hbs-nr">00910</span> | aussteller4 | string | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[aussteller5](/bo4e/202604/com/Aussteller#aussteller5)</span><span className="hbs-nr">00920</span> | aussteller5 | string | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**zertifikatsNutzer**</span> | — | object | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[zertifikatsNutzer1](/bo4e/202604/com/ZertifikatsNutzer#zertifikatsnutzer1)</span><span className="hbs-nr">00930</span> | zertifikatsNutzer1 | string | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[zertifikatsNutzer2](/bo4e/202604/com/ZertifikatsNutzer#zertifikatsnutzer2)</span><span className="hbs-nr">00940</span> | zertifikatsNutzer2 | string | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[zertifikatsNutzer3](/bo4e/202604/com/ZertifikatsNutzer#zertifikatsnutzer3)</span><span className="hbs-nr">00950</span> | zertifikatsNutzer3 | string | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[zertifikatsNutzer4](/bo4e/202604/com/ZertifikatsNutzer#zertifikatsnutzer4)</span><span className="hbs-nr">00960</span> | zertifikatsNutzer4 | string | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[zertifikatsNutzer5](/bo4e/202604/com/ZertifikatsNutzer#zertifikatsnutzer5)</span><span className="hbs-nr">00970</span> | zertifikatsNutzer5 | string | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**zieladresse**</span> | — | object | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[zieladresse1](/bo4e/202604/com/Zieladresse#zieladresse1)</span><span className="hbs-nr">00980</span> | zieladresse1 | string | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[zieladresse2](/bo4e/202604/com/Zieladresse#zieladresse2)</span><span className="hbs-nr">00990</span> | zieladresse2 | string | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[zieladresse3](/bo4e/202604/com/Zieladresse#zieladresse3)</span><span className="hbs-nr">01000</span> | zieladresse3 | string | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[zieladresse4](/bo4e/202604/com/Zieladresse#zieladresse4)</span><span className="hbs-nr">01010</span> | zieladresse4 | string | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[zieladresse5](/bo4e/202604/com/Zieladresse#zieladresse5)</span><span className="hbs-nr">01020</span> | zieladresse5 | string | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e1">**MARKTLOKATION** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | — | Kann | Muss | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | Kann | — | — |
| <span className="hbs-f hbs-e2">[datenqualitaet](/bo4e/202604/bo/Marktlokation#datenqualitaet)</span><span className="hbs-nr">01030</span> | Datenqualitaet | [Enum Datenqualitaet](/bo4e/202604/enum/Datenqualitaet) | — | — | Kann | Muss | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`ERWARTETE_DATEN`</span> | — | — | — | — | Kann | Muss | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | Kann | Muss | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`INFORMATIVE_DATEN`</span> | — | — | — | — | Kann | Muss | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`GUELTIGE_DATEN`</span> | — | — | — | — | Kann | Muss | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN`</span> | — | — | — | — | Kann | Muss | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_KEINE_DATEN_VORHANDEN`</span> | — | — | — | — | Kann | Muss | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN_ERWARTET`</span> | — | — | — | — | Kann | Muss | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_DATEN`</span> | — | — | — | — | Kann | Muss | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_ERWARTETE_DATEN`</span> | — | — | — | — | Kann | Muss | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | Kann | Muss | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | Kann | — | — |
| <span className="hbs-g hbs-e2">**gueltigkeitszeitraum**</span> | — | object | — | — | Kann | Muss | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | Kann | — | — |
| <span className="hbs-f hbs-e3">[zeitraumId](/bo4e/202604/com/Zeitraum#zeitraumid)</span><span className="hbs-nr">01040</span> | zeitraumId | integer | — | — | Kann | Muss | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | Kann | — | — |
| <span className="hbs-g hbs-e2">**zaehlwerke** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | — | Kann | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | Kann | — | — |
| <span className="hbs-f hbs-e3">[obisKennzahl](/bo4e/202604/com/Zaehlwerk#obiskennzahl)</span><span className="hbs-nr">01050</span> | Die OBIS-Kennzahl für das Zählwerk, die festlegt, welche auf die gemessene Größe mit dem Stand gemeldet wird.<br/>Nur Zählwerkstände mit dieser OBIS-Kennzahl werden an diesem Zählwerk registriert. Beispiel:1-0:1.8.1 für<br/>elektrische Wirkarbeit. | string | — | — | Kann | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | Kann | — | — |
| <span className="hbs-f hbs-e3">[wertegranularitaet](/bo4e/202604/com/Zaehlwerk#wertegranularitaet)</span><span className="hbs-nr">01060</span> | Wertegranularitaet | [Enum Wertegranularitaet](/bo4e/202604/enum/Wertegranularitaet) | — | — | Kann | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`JAEHRLICH`</span> | — | — | — | — | Kann | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`HALBJAEHRLICH`</span> | — | — | — | — | Kann | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`QUARTALSWEISE`</span> | — | — | — | — | Kann | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MONATLICH`</span> | — | — | — | — | Kann | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-g hbs-e3">**zaehlzeiten**</span> | — | object | — | — | Kann | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[register](/bo4e/202604/com/Zaehlzeitregister#register)</span><span className="hbs-nr">01070</span> | Zählzeitregister | string | — | — | Kann | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[zaehlzeitDefinition](/bo4e/202604/com/Zaehlzeitregister#zaehlzeitdefinition)</span><span className="hbs-nr">01080</span> | Zählzeitdefinition | string | — | — | Kann | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-g hbs-e3">**verwendungszwecke** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[marktrolle](/bo4e/202604/com/Verwendungszweck#marktrolle)</span><span className="hbs-nr">01090</span> | Diese Rollen kann ein Marktteilnehmer einnehmen | [Enum Marktrolle](/bo4e/202604/enum/Marktrolle) | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NB`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LF`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MSB`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MSBA`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GMSB`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MDL`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`DL`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BKV`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`UENB`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KUNDE-SELBST-NN`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MGV`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`EIV`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`RB`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KUNDE`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`INTERESSENT`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KN`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`UBA`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BIKO`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ESA`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[zweck](/bo4e/202604/com/Verwendungszweck#zweck)</span><span className="hbs-nr">01100</span> | zweck | array | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[marktlokationsId](/bo4e/202604/bo/Marktlokation#marktlokationsid)</span><span className="hbs-nr">01110</span> | Identifikationsnummer einer Marktlokation, an der Energie entweder<br/>verbraucht, oder erzeugt wird | string | — | — | — | Kann | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | Kann | — | — |
| <span className="hbs-g hbs-e2">**messstellenbetriebsabrechnungsdaten** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[abschlag](/bo4e/202604/com/Messstellenbetriebsabrechnungsdaten#abschlag)</span><span className="hbs-nr">01120</span> | Abschlag | number (float) | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[anzahl](/bo4e/202604/com/Messstellenbetriebsabrechnungsdaten#anzahl)</span><span className="hbs-nr">01130</span> | anzahl | integer | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[artikelId](/bo4e/202604/com/Messstellenbetriebsabrechnungsdaten#artikelid)</span><span className="hbs-nr">01140</span> | BDEWArtikelId | string | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[messstellenbetriebsabrechnung](/bo4e/202604/com/Messstellenbetriebsabrechnungsdaten#messstellenbetriebsabrechnung)</span><span className="hbs-nr">01150</span> | messstellenbetriebsabrechnung | boolean | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[konfigurationsprodukt](/bo4e/202604/bo/Marktlokation#konfigurationsprodukt)</span><span className="hbs-nr">01160</span> | konfigurationsprodukt | string | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[leistungskurvendefinition](/bo4e/202604/bo/Marktlokation#leistungskurvendefinition)</span><span className="hbs-nr">01170</span> | Code der Zugeordnete Leistungskurvendefinition für das Objekt | string | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[produktdatenRelevanteRolle](/bo4e/202604/bo/Marktlokation#produktdatenrelevanterolle)</span><span className="hbs-nr">01180</span> | Diese Rollen kann ein Marktteilnehmer einnehmen | [Enum Marktrolle](/bo4e/202604/enum/Marktrolle) | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`NB`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`LF`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`MSB`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`MSBA`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`GMSB`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`MDL`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`DL`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`BKV`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`UENB`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KUNDE-SELBST-NN`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`MGV`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`EIV`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`RB`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KUNDE`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`INTERESSENT`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KN`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`UBA`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`BIKO`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`ESA`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-g hbs-e1">**VERWENDUNGSZEITRAUM** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | — | — | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | — |
| <span className="hbs-f hbs-e2">[datenqualitaet](/bo4e/202604/bo/Verwendungszeitraum#datenqualitaet) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">01190</span> | Datenqualitaet | [Enum Datenqualitaet](/bo4e/202604/enum/Datenqualitaet) | — | — | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`ERWARTETE_DATEN`</span> | — | — | — | — | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`INFORMATIVE_DATEN`</span> | — | — | — | — | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`GUELTIGE_DATEN`</span> | — | — | — | — | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN`</span> | — | — | — | — | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_KEINE_DATEN_VORHANDEN`</span> | — | — | — | — | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN_ERWARTET`</span> | — | — | — | — | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_DATEN`</span> | — | — | — | — | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_ERWARTETE_DATEN`</span> | — | — | — | — | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | — |
| <span className="hbs-f hbs-e2">[verwendungAb](/bo4e/202604/bo/Verwendungszeitraum#verwendungab) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">01200</span> | verwendungAb | string (date-time) | — | — | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | — |
| <span className="hbs-f hbs-e2">[verwendungBis](/bo4e/202604/bo/Verwendungszeitraum#verwendungbis)</span><span className="hbs-nr">01210</span> | verwendungBis | string (date-time) | — | — | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | — |
| <span className="hbs-f hbs-e2">[zeitraumId](/bo4e/202604/bo/Verwendungszeitraum#zeitraumid) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">01220</span> | zeitraumId | integer | — | — | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | Muss | — |
| <span className="hbs-g hbs-e1">**NETZLOKATION** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | — | — | — | — | Muss | — | — | — | — | Muss | — | — | — | — | Muss | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[datenqualitaet](/bo4e/202604/bo/Netzlokation#datenqualitaet)</span><span className="hbs-nr">01230</span> | Datenqualitaet | [Enum Datenqualitaet](/bo4e/202604/enum/Datenqualitaet) | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`ERWARTETE_DATEN`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`INFORMATIVE_DATEN`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`GUELTIGE_DATEN`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_KEINE_DATEN_VORHANDEN`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN_ERWARTET`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_DATEN`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_ERWARTETE_DATEN`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[keinKonfigurationsprodukt](/bo4e/202604/bo/Netzlokation#keinkonfigurationsprodukt)</span><span className="hbs-nr">01240</span> | keinKonfigurationsprodukt | boolean | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[konfigurationsprodukt](/bo4e/202604/bo/Netzlokation#konfigurationsprodukt)</span><span className="hbs-nr">01250</span> | konfigurationsprodukt | string | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[leistungskurvendefinition](/bo4e/202604/bo/Netzlokation#leistungskurvendefinition)</span><span className="hbs-nr">01260</span> | Code der Zugeordnete Leistungskurvendefinition für das Objekt | string | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[netzlokationsId](/bo4e/202604/bo/Netzlokation#netzlokationsid) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">01270</span> | Identifikationsnummer einer Netzlokation, an der Energie entweder<br/>verbraucht, oder erzeugt wird (Like MarktlokationsId Marktlokation) | string | — | — | — | — | Muss | — | — | — | — | Muss | — | — | — | — | Muss | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[produktdatenRelevanteRolle](/bo4e/202604/bo/Netzlokation#produktdatenrelevanterolle)</span><span className="hbs-nr">01280</span> | Diese Rollen kann ein Marktteilnehmer einnehmen | [Enum Marktrolle](/bo4e/202604/enum/Marktrolle) | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`NB`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`LF`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`MSB`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`MSBA`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`GMSB`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`MDL`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`DL`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`BKV`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`UENB`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KUNDE-SELBST-NN`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`MGV`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`EIV`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`RB`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KUNDE`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`INTERESSENT`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KN`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`UBA`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`BIKO`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`ESA`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[steuerkanal](/bo4e/202604/bo/Netzlokation#steuerkanal)</span><span className="hbs-nr">01290</span> | Ob ein Steuerkanal der Netzlokation zugeordnet ist und somit die Netzlokation gesteuert<br/>werden kann.<br/>ZF2: Kein Steuerkanal vorhanden<br/>ZF3: Steuerkanal vorhanden | boolean | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**auftraggebenderMarktpartner**</span> | — | object | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[marktrolle](/bo4e/202604/bo/Marktteilnehmer#marktrolle)</span><span className="hbs-nr">01300</span> | Gibt im Klartext die Bezeichnung der Marktrolle an. | [Enum Marktrolle](/bo4e/202604/enum/Marktrolle) | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`NB`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`LF`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MSB`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MSBA`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GMSB`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MDL`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`DL`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BKV`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`UENB`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KUNDE-SELBST-NN`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MGV`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`EIV`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`RB`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KUNDE`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`INTERESSENT`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KN`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`UBA`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BIKO`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`ESA`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[rollencodenummer](/bo4e/202604/bo/Marktteilnehmer#rollencodenummer)</span><span className="hbs-nr">01310</span> | Gibt die Codenummer der Marktrolle an. | string | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**gueltigkeitszeitraum**</span> | — | object | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[zeitraumId](/bo4e/202604/com/Zeitraum#zeitraumid)</span><span className="hbs-nr">01320</span> | zeitraumId | integer | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**zaehlwerke** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[obisKennzahl](/bo4e/202604/com/Zaehlwerk#obiskennzahl)</span><span className="hbs-nr">01330</span> | Die OBIS-Kennzahl für das Zählwerk, die festlegt, welche auf die gemessene Größe mit dem Stand gemeldet wird.<br/>Nur Zählwerkstände mit dieser OBIS-Kennzahl werden an diesem Zählwerk registriert. Beispiel:1-0:1.8.1 für<br/>elektrische Wirkarbeit. | string | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e3">**verwendungszwecke** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[marktrolle](/bo4e/202604/com/Verwendungszweck#marktrolle)</span><span className="hbs-nr">01340</span> | Diese Rollen kann ein Marktteilnehmer einnehmen | [Enum Marktrolle](/bo4e/202604/enum/Marktrolle) | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NB`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LF`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MSB`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MSBA`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GMSB`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MDL`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`DL`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BKV`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`UENB`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KUNDE-SELBST-NN`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MGV`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`EIV`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`RB`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KUNDE`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`INTERESSENT`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KN`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`UBA`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BIKO`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ESA`</span> | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[zweck](/bo4e/202604/com/Verwendungszweck#zweck)</span><span className="hbs-nr">01350</span> | zweck | array | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e1">**STEUERBARE_RESSOURCE** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | — | — | — | — | — | — | Muss | — | — | — | — | Muss | — | — | — | — | Muss | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[datenqualitaet](/bo4e/202604/bo/SteuerbareRessource#datenqualitaet)</span><span className="hbs-nr">01360</span> | Datenqualitaet | [Enum Datenqualitaet](/bo4e/202604/enum/Datenqualitaet) | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`ERWARTETE_DATEN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`INFORMATIVE_DATEN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`GUELTIGE_DATEN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_KEINE_DATEN_VORHANDEN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN_ERWARTET`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_DATEN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_ERWARTETE_DATEN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[konfigurationsprodukt](/bo4e/202604/bo/SteuerbareRessource#konfigurationsprodukt)</span><span className="hbs-nr">01370</span> | konfigurationsprodukt | string | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[produktdatenRelevanteRolle](/bo4e/202604/bo/SteuerbareRessource#produktdatenrelevanterolle)</span><span className="hbs-nr">01380</span> | Diese Rollen kann ein Marktteilnehmer einnehmen | [Enum Marktrolle](/bo4e/202604/enum/Marktrolle) | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`NB`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`LF`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`MSB`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`MSBA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`GMSB`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`MDL`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`DL`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`BKV`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`UENB`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KUNDE-SELBST-NN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`MGV`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`EIV`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`RB`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KUNDE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`INTERESSENT`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`UBA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`BIKO`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`ESA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[ressourcenId](/bo4e/202604/bo/SteuerbareRessource#ressourcenid) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">01390</span> | ressourcenId | string | — | — | — | — | — | — | Muss | — | — | — | — | Muss | — | — | — | — | Muss | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[steuerkanal](/bo4e/202604/bo/SteuerbareRessource#steuerkanal)</span><span className="hbs-nr">01400</span> | Steuerkanal | [Enum Steuerkanal](/bo4e/202604/enum/Steuerkanal) | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`AN_AUS`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`GESTUFT`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**auftraggebenderMarktpartner**</span> | — | object | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[marktrolle](/bo4e/202604/bo/Marktteilnehmer#marktrolle)</span><span className="hbs-nr">01410</span> | Gibt im Klartext die Bezeichnung der Marktrolle an. | [Enum Marktrolle](/bo4e/202604/enum/Marktrolle) | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`NB`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`LF`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MSB`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MSBA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GMSB`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MDL`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`DL`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BKV`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`UENB`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KUNDE-SELBST-NN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MGV`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`EIV`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`RB`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KUNDE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`INTERESSENT`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`UBA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BIKO`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`ESA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[rollencodenummer](/bo4e/202604/bo/Marktteilnehmer#rollencodenummer)</span><span className="hbs-nr">01420</span> | Gibt die Codenummer der Marktrolle an. | string | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**gueltigkeitszeitraum**</span> | — | object | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[zeitraumId](/bo4e/202604/com/Zeitraum#zeitraumid)</span><span className="hbs-nr">01430</span> | zeitraumId | integer | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**zugeordneteDefinition**</span> | — | object | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[leistungskurvendefinition](/bo4e/202604/com/ZugeordneteDefinition#leistungskurvendefinition)</span><span className="hbs-nr">01440</span> | leistungskurvendefinition | string | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[schaltzeitdefinition](/bo4e/202604/com/ZugeordneteDefinition#schaltzeitdefinition)</span><span className="hbs-nr">01450</span> | schaltzeitdefinition | string | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-g hbs-e1">**TRANCHE** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | — | — | — | — | — | — | — | Muss | — | — | — | — | Muss | — | — | — | — | Muss | — | — | Muss | — |
| <span className="hbs-f hbs-e2">[datenqualitaet](/bo4e/202604/bo/Tranche#datenqualitaet) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">01460</span> | Datenqualitaet | [Enum Datenqualitaet](/bo4e/202604/enum/Datenqualitaet) | — | — | — | — | — | — | — | Muss | — | — | — | — | Kann | — | — | — | — | Kann | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`ERWARTETE_DATEN`</span> | — | — | — | — | — | — | — | — | — | Muss | — | — | — | — | Kann | — | — | — | — | Kann | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | — | — | — | — | — | Muss | — | — | — | — | Kann | — | — | — | — | Kann | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`INFORMATIVE_DATEN`</span> | — | — | — | — | — | — | — | — | — | Muss | — | — | — | — | Kann | — | — | — | — | Kann | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`GUELTIGE_DATEN`</span> | — | — | — | — | — | — | — | — | — | Muss | — | — | — | — | Kann | — | — | — | — | Kann | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN`</span> | — | — | — | — | — | — | — | — | — | Muss | — | — | — | — | Kann | — | — | — | — | Kann | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_KEINE_DATEN_VORHANDEN`</span> | — | — | — | — | — | — | — | — | — | Muss | — | — | — | — | Kann | — | — | — | — | Kann | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN_ERWARTET`</span> | — | — | — | — | — | — | — | — | — | Muss | — | — | — | — | Kann | — | — | — | — | Kann | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_DATEN`</span> | — | — | — | — | — | — | — | — | — | Muss | — | — | — | — | Kann | — | — | — | — | Kann | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_ERWARTETE_DATEN`</span> | — | — | — | — | — | — | — | — | — | Muss | — | — | — | — | Kann | — | — | — | — | Kann | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | — | — | — | — | — | Muss | — | — | — | — | Kann | — | — | — | — | Kann | — | — | Kann | — |
| <span className="hbs-f hbs-e2">[tranchenId](/bo4e/202604/bo/Tranche#tranchenid) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">01470</span> | tranchenId | string | — | — | — | — | — | — | — | Muss | — | — | — | — | Muss | — | — | — | — | Muss | — | — | Muss | — |
| <span className="hbs-g hbs-e2">**gueltigkeitszeitraum** <span className="hbs-pflicht">\*</span></span> | — | object | — | — | — | — | — | — | — | Muss | — | — | — | — | Kann | — | — | — | — | Kann | — | — | Kann | — |
| <span className="hbs-f hbs-e3">[zeitraumId](/bo4e/202604/com/Zeitraum#zeitraumid) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">01480</span> | zeitraumId | integer | — | — | — | — | — | — | — | Muss | — | — | — | — | Kann | — | — | — | — | Kann | — | — | Kann | — |
| <span className="hbs-g hbs-e2">**zaehlwerke** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | — | — | — | — | — | — | — | Muss | — | — | — | — | Kann | — | — | — | — | Kann | — | — | Kann | — |
| <span className="hbs-f hbs-e3">[obisKennzahl](/bo4e/202604/com/Zaehlwerk#obiskennzahl) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">01490</span> | Die OBIS-Kennzahl für das Zählwerk, die festlegt, welche auf die gemessene Größe mit dem Stand gemeldet wird.<br/>Nur Zählwerkstände mit dieser OBIS-Kennzahl werden an diesem Zählwerk registriert. Beispiel:1-0:1.8.1 für<br/>elektrische Wirkarbeit. | string | — | — | — | — | — | — | — | Muss | — | — | — | — | Kann | — | — | — | — | Kann | — | — | Kann | — |
| <span className="hbs-g hbs-e3">**verwendungszwecke** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-f hbs-e4">[marktrolle](/bo4e/202604/com/Verwendungszweck#marktrolle)</span><span className="hbs-nr">01500</span> | Diese Rollen kann ein Marktteilnehmer einnehmen | [Enum Marktrolle](/bo4e/202604/enum/Marktrolle) | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e5">`NB`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e5">`LF`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e5">`MSB`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e5">`MSBA`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e5">`GMSB`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e5">`MDL`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e5">`DL`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e5">`BKV`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e5">`UENB`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e5">`KUNDE-SELBST-NN`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e5">`MGV`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e5">`EIV`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e5">`RB`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e5">`KUNDE`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e5">`INTERESSENT`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e5">`KN`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e5">`UBA`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e5">`BIKO`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-w hbs-e5">`ESA`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-f hbs-e4">[zweck](/bo4e/202604/com/Verwendungszweck#zweck)</span><span className="hbs-nr">01510</span> | zweck | array | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — |

</div>

</Handbuchsatz>

## Kette dieses Auslösers

Das Ereignis löst die Nachricht aus. Der Marktpartner antwortet mit einer der genannten Antworten, und danach schreibt die MACO APP den Vorgang in Ihr Backendsystem.

| Nachricht | Antworten | Schreibaufruf nach der Antwort |
|---|---|---|
| [44116](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44116) | [44119](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44119) | `POST /updateProcessData` |
| [44159](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44159) | [44161](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44161) | `POST /updateProcessData` |
| [55553](/schnittstellen/202604/pruefi/UTILMD/PI_55553) | — | — |
| [55557](/schnittstellen/202604/pruefi/UTILMD/PI_55557) | — | — |
| [55639](/schnittstellen/202604/pruefi/UTILMD/PI_55639) | — | — |
| [55640](/schnittstellen/202604/pruefi/UTILMD/PI_55640) | — | — |
| [55641](/schnittstellen/202604/pruefi/UTILMD/PI_55641) | — | — |
| [55642](/schnittstellen/202604/pruefi/UTILMD/PI_55642) | — | — |
| [55643](/schnittstellen/202604/pruefi/UTILMD/PI_55643) | — | — |
| [55649](/schnittstellen/202604/pruefi/UTILMD/PI_55649) | — | — |
| [55650](/schnittstellen/202604/pruefi/UTILMD/PI_55650) | — | — |
| [55651](/schnittstellen/202604/pruefi/UTILMD/PI_55651) | — | — |
| [55652](/schnittstellen/202604/pruefi/UTILMD/PI_55652) | — | — |
| [55653](/schnittstellen/202604/pruefi/UTILMD/PI_55653) | — | — |
| [55659](/schnittstellen/202604/pruefi/UTILMD/PI_55659) | — | — |
| [55660](/schnittstellen/202604/pruefi/UTILMD/PI_55660) | — | — |
| [55661](/schnittstellen/202604/pruefi/UTILMD/PI_55661) | — | — |
| [55662](/schnittstellen/202604/pruefi/UTILMD/PI_55662) | — | — |
| [55663](/schnittstellen/202604/pruefi/UTILMD/PI_55663) | — | — |
| [55684](/schnittstellen/202604/pruefi/UTILMD/PI_55684) | — | — |
| [55686](/schnittstellen/202604/pruefi/UTILMD/PI_55686) | — | — |

Dieses Ereignis löst Schritte in diesen Rollensichten aus:

| Prozess | Beteiligter | Regelwerk | Sparte |
|---|---|---|---|
| [Stammdatenänderung vom MSB (verantwortlich) ausgehend](/prozessdoku/202604/MSB/GPKE-Teil4-stammdatenaenderung-vom-msb-verantwortlich-ausgehend) | MSB | GPKE Teil 4 | Strom |
| [Stammdatenänderung vom MSB (verantwortlich) ausgehend](/prozessdoku/202604/MSB/geli-gas-2-0-stammdatenanderung-vom-msb-verantwortlich-ausgehend) | MSB | GeLi Gas 2.0 | Gas |

## Transaktionsdaten

Der Umschlag der Nachricht. Pflichtfelder müssen beim Trigger-Aufruf gesetzt sein.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| [gueltigAb](/bo4e/202604/cdoc/Transaktionsdaten#gueltigab) | string (date-time) | **ja** | Gültigkeitsdatum/-zeit / DTM+7 |
| [kategorie](/bo4e/202604/cdoc/Transaktionsdaten#kategorie) | string | **ja** | Qualifier aus dem Beginn der EDIFact Nachricht / BGM |
| [sparte](/bo4e/202604/cdoc/Transaktionsdaten#sparte) | [Enum Sparte](/bo4e/202604/enum/Sparte) | **ja** | Enthält Informationen über die Sparte Werte: `STROM`, `GAS`, `FERNWAERME`, `NAHWAERME`, `WASSER`, `ABWASSER` |
| [transaktionsgrund](/bo4e/202604/cdoc/Transaktionsdaten#transaktionsgrund) | string | **ja** | Der Transaktionsgrund beschreibt den Geschäftsvorfall zur Kategorie genauer / UTILMD STS+7++###+ZW4+E03 |
| [transaktionsgrundergaenzung](/bo4e/202604/cdoc/Transaktionsdaten#transaktionsgrundergaenzung) | string | **ja** | Ergänzung zum Transaktionsgrund / UTILMD STS+7++E01+###+E03 |
| `pruefidentifikator` | — | nein | Wird dynamisch im Event-Prozess ermittelt (Entscheidungsgrundlage: marktrolleEmpfaenger, transaktionsgrund). Ein vom Sender mitgegebener Wert wird ignoriert. Im Topic mögliche Prüfis — 44116, 44159, 55553, 55557, 55639, 55640, 55641, 55642, 55643, 55649, 55650, 55651, 55652, 55653, 55659, 55660, 55661, 55662, 55663, 55684, 55686. Mögliche Werte: `44116`, `44159`, `55553`, `55557`, `55639`, `55640`, `55641`, `55642`, `55643`, `55649`, `55650`, `55651`, `55652`, `55653`, `55659`, `55660`, `55661`, `55662`, `55663`, `55684`, `55686` |
| [absender › marktrolle](/bo4e/202604/bo/Marktteilnehmer#marktrolle) | [Enum Marktrolle](/bo4e/202604/enum/Marktrolle) | nein | Gibt im Klartext die Bezeichnung der Marktrolle an. Werte: `NB`, `LF`, `MSB`, `MSBA`, `GMSB`, `MDL`, `DL`, `BKV`, `UENB`, `KUNDE-SELBST-NN` … (+9) |
| [absender › rollencodenummer](/bo4e/202604/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |
| [empfaenger › marktrolle](/bo4e/202604/bo/Marktteilnehmer#marktrolle) | [Enum Marktrolle](/bo4e/202604/enum/Marktrolle) | nein | Gibt im Klartext die Bezeichnung der Marktrolle an. Werte: `NB`, `LF`, `MSB`, `MSBA`, `GMSB`, `MDL`, `DL`, `BKV`, `UENB`, `KUNDE-SELBST-NN` … (+9) |
| [empfaenger › rollencodenummer](/bo4e/202604/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |

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
