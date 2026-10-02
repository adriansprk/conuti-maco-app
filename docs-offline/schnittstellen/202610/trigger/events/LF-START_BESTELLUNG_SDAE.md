# [LF] START_BESTELLUNG_SDAE
<span hidden data-pagefind-meta={"title:Trigger-Ereignis START_BESTELLUNG_SDAE — Marktrolle LF (FV 202610)"} />

Marktrolle **LF** · Formatversion **202610** · BO4E-Schema **1.7.8**

## Stammdaten

Unter diesem Topic ist genau einer der folgenden 18 Prüfidentifikatoren zulässig — welcher, entscheidet der Event-Prozess.

| Prüfi | Scope | Anwendungsfall | Festlegung | Kommunikation |
|---|---|---|---|---|
| [PI_55156](/schnittstellen/202610/pruefi/UTILMD/PI_55156) | UTILMD | Rückmeldung/Anfrage Abr.-Daten BK-Abr. verb. MaLo | GPKE Teil 2 | LF → NB |
| [PI_55180](/schnittstellen/202610/pruefi/UTILMD/PI_55180) | UTILMD | Rückmeldung/Anfrage Lokationsbündelstruktur | GPKE Teil 4 | LF → NB |
| [PI_55220](/schnittstellen/202610/pruefi/UTILMD/PI_55220) | UTILMD | Rückmeldung/Anfrage Abr.-Daten NNA | GPKE Teil 2 | LF → NB |
| [PI_55227](/schnittstellen/202610/pruefi/UTILMD/PI_55227) | UTILMD | Rückmeldung/Anfrage Blindabr.-Daten der NeLo | GPKE Teil 4 | LF → NB |
| [PI_55555](/schnittstellen/202610/pruefi/UTILMD/PI_55555) | UTILMD | Anfrage Daten der individuellen Bestellung | GPKE Teil 4 | NB → MSB |
| [PI_55621](/schnittstellen/202610/pruefi/UTILMD/PI_55621) | UTILMD | Rückmeldung/Anfrage Daten zur NeLo | GPKE Teil 4 | LF → NB |
| [PI_55622](/schnittstellen/202610/pruefi/UTILMD/PI_55622) | UTILMD | Rückmeldung/Anfrage Daten der MaLo | GPKE Teil 4 | LF → NB |
| [PI_55623](/schnittstellen/202610/pruefi/UTILMD/PI_55623) | UTILMD | Rückmeldung/Anfrage Daten der TR | GPKE Teil 4 | LF → NB |
| [PI_55624](/schnittstellen/202610/pruefi/UTILMD/PI_55624) | UTILMD | Rückmeldung/Anfrage Daten der SR | GPKE Teil 4 | LF → NB |
| [PI_55625](/schnittstellen/202610/pruefi/UTILMD/PI_55625) | UTILMD | Rückmeldung/Anfrage Daten der Tranche | GPKE Teil 4 | LF → NB |
| [PI_55626](/schnittstellen/202610/pruefi/UTILMD/PI_55626) | UTILMD | Rückmeldung/Anfrage Daten der MeLo | GPKE Teil 4 | LF → NB |
| [PI_55654](/schnittstellen/202610/pruefi/UTILMD/PI_55654) | UTILMD | Rückmeldung/Anfrage Daten der NeLo | GPKE Teil 4 | LF → MSB |
| [PI_55655](/schnittstellen/202610/pruefi/UTILMD/PI_55655) | UTILMD | Rückmeldung/Anfrage Daten der MaLo | GPKE Teil 4 | LF → MSB |
| [PI_55656](/schnittstellen/202610/pruefi/UTILMD/PI_55656) | UTILMD | Rückmeldung/Anfrage Daten der SR | GPKE Teil 4 | LF → MSB |
| [PI_55657](/schnittstellen/202610/pruefi/UTILMD/PI_55657) | UTILMD | Rückmeldung/Anfrage Daten der Tranche | GPKE Teil 4 | LF → MSB |
| [PI_55658](/schnittstellen/202610/pruefi/UTILMD/PI_55658) | UTILMD | Rückmeldung/Anfrage Daten der MeLo | GPKE Teil 4 | LF → MSB |
| [PI_55673](/schnittstellen/202610/pruefi/UTILMD/PI_55673) | UTILMD | Rückmeldung/Anfrage Abr.-Daten BK-Abr. erz. Malo | GPKE Teil 2 | LF → NB |
| [PI_55692](/schnittstellen/202610/pruefi/UTILMD/PI_55692) | UTILMD | Rückmeldung/Anfrage Paket-ID der MaLo | GPKE Teil 4 | LF → NB |

Die Stammdaten der 18 Prüfidentifikatoren in **einer** Struktur — eine Spalte je Prüfidentifikator, wie im Anwendungshandbuch. Ein Wert in der Spalte heißt, dass das Feld zu diesem Prüfidentifikator gehört: **Muss**, wenn seine Spezifikation es verlangt, sonst **Kann**. Eine leere Zelle heißt »gehört nicht dazu«, nicht »unbekannt«. Vorausgewählt ist der erste; die übrigen schaltet die Leiste über der Tabelle zu.

<Handbuchsatz>

<div className="maco-tabellenrahmen">

| Struktur (BO4E) | Beschreibung | Format | <span className="hbs-p" title="Rückmeldung/Anfrage Abr.-Daten BK-Abr. verb. MaLo">55156</span> | <span className="hbs-p" title="Rückmeldung/Anfrage Lokationsbündelstruktur">55180</span> | <span className="hbs-p" title="Rückmeldung/Anfrage Abr.-Daten NNA">55220</span> | <span className="hbs-p" title="Rückmeldung/Anfrage Blindabr.-Daten der NeLo">55227</span> | <span className="hbs-p" title="Anfrage Daten der individuellen Bestellung">55555</span> | <span className="hbs-p" title="Rückmeldung/Anfrage Daten zur NeLo">55621</span> | <span className="hbs-p" title="Rückmeldung/Anfrage Daten der MaLo">55622</span> | <span className="hbs-p" title="Rückmeldung/Anfrage Daten der TR">55623</span> | <span className="hbs-p" title="Rückmeldung/Anfrage Daten der SR">55624</span> | <span className="hbs-p" title="Rückmeldung/Anfrage Daten der Tranche">55625</span> | <span className="hbs-p" title="Rückmeldung/Anfrage Daten der MeLo">55626</span> | <span className="hbs-p" title="Rückmeldung/Anfrage Daten der NeLo">55654</span> | <span className="hbs-p" title="Rückmeldung/Anfrage Daten der MaLo">55655</span> | <span className="hbs-p" title="Rückmeldung/Anfrage Daten der SR">55656</span> | <span className="hbs-p" title="Rückmeldung/Anfrage Daten der Tranche">55657</span> | <span className="hbs-p" title="Rückmeldung/Anfrage Daten der MeLo">55658</span> | <span className="hbs-p" title="Rückmeldung/Anfrage Abr.-Daten BK-Abr. erz. Malo">55673</span> | <span className="hbs-p" title="Rückmeldung/Anfrage Paket-ID der MaLo">55692</span> | Bedingung |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| <span className="hbs-g hbs-e0">**stammdaten**</span> | — | object | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | — |
| <span className="hbs-g hbs-e1">**BILANZIERUNG** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-f hbs-e2">[aggregationsverantwortung](/bo4e/202610/bo/Bilanzierung#aggregationsverantwortung)</span><span className="hbs-nr">00010</span> | Aggregationsverantwortung | [Enum Aggregationsverantwortung](/bo4e/202610/enum/Aggregationsverantwortung) | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`UENB`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`VNB`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-f hbs-e2">[bilanzkreis](/bo4e/202610/bo/Bilanzierung#bilanzkreis)</span><span className="hbs-nr">00020</span> | Bilanzkreis | string | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-f hbs-e2">[datenqualitaet](/bo4e/202610/bo/Bilanzierung#datenqualitaet)</span><span className="hbs-nr">00030</span> | Datenqualität | [Enum Datenqualitaet](/bo4e/202610/enum/Datenqualitaet) | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`ERWARTETE_DATEN`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`INFORMATIVE_DATEN`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`GUELTIGE_DATEN`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_KEINE_DATEN_VORHANDEN`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN_ERWARTET`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_DATEN`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_ERWARTETE_DATEN`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-f hbs-e2">[detailsPrognosegrundlage](/bo4e/202610/bo/Bilanzierung#detailsprognosegrundlage)</span><span className="hbs-nr">00040</span> | Prognosegrundlage - Besteht der Bedarf ein tagesparameteräbhängiges Lastprofil mit gemeinsamer Messung anzugeben, so ist dies über die 2 -malige Wiederholung des CAV Segments mit der Angabe der Codes E02 und E14 möglich. | array | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-f hbs-e2">[prognosegrundlage](/bo4e/202610/bo/Bilanzierung#prognosegrundlage)</span><span className="hbs-nr">00050</span> | Prognosegrundlage | [Enum Prognosegrundlage](/bo4e/202610/enum/Prognosegrundlage) | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`WERTE`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`PROFILE`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-f hbs-e2">[zeitreihentyp](/bo4e/202610/bo/Bilanzierung#zeitreihentyp)</span><span className="hbs-nr">00060</span> | Zeitreihentyp | [Enum Zeitreihentyp](/bo4e/202610/enum/Zeitreihentyp) | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`EGS`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`LGS`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`NZR`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`SES`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`SLS`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`TES`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`TLS`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`SLS_TLS`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`SES_TES`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`AUS`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`BAS`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`DBA`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`DZR`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`DZÜ`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`FPE`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`FPI`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`SRE`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`SRI`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`VZR`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`BIL`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`BIP`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`BIT`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`GAL`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`GAP`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`GAT`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`GEL`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`GEP`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`GET`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`SOL`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`SOP`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`SOT`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`WFL`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`WFP`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`WNL`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`WNP`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`WNT`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`WAL`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`WAP`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`WAT`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`AU1`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`BI1`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`BI2`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`BI3`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`GAA`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`GAB`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`GAC`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`GE1`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`GE2`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`GE3`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`SO1`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`SO2`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`SO3`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`WF1`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`WF2`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`WF3`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`WN1`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`WN2`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`WN3`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`WAA`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`WAB`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`WAC`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`AUSFALLARBEITSSUMME`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`BILANZKREISABWEICHUNGSSALDO`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZZEITREIHE`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`DELTAZEITREIHE`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`DELTAZEITREIHENUEBERTRAG`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`FAHRPLANENTNAHMESUMME`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`FAHRPLANEINSPEISESUMME`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`UEBERFUEHRUNGSZEITREIHE_SEKUNDAERREGELLEISTUNG_EXPORT`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`UEBERFUEHRUNGSZEITREIHE_SEKUNDAERREGELLEISTUNG_IMPORT`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`VERLUSTZEITREIHE`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_BIOMASSE_BIOGAS_GEMESSEN`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_BIOMASSE_BIOGAS_EINSPEISEPROFIL`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_BIOMASSE_BIOGAS_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_DEPONIE_KLAER_GRUBENGAS_GEMESSEN`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_DEPONIE_KLAER_GRUBENGAS_EINSPEISEPROFIL`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_DEPONIE_KLAER_GRUBENGAS_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_GEOTHERMIE_GEMESSEN`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_GEOTHERMIE_EINSPEISEPROFIL`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_GEOTHERMIE_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_SOLAR_GEMESSEN`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_SOLAR_EINSPEISEPROFIL`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_SOLAR_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_WIND_OFFSHORE_GEMESSEN`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_WIND_OFFSHORE_EINSPEISEPROFIL`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_WIND_OFFSHORE_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_WIND_ONSHORE_GEMESSEN`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_WIND_ONSHORE_EINSPEISEPROFIL`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_WIND_ONSHORE_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_WASSERKRAFT_GEMESSEN`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_WASSERKRAFT_EINSPEISEPROFIL`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_WASSERKRAFT_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_AUSFALLARBEIT`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_BIOMASSE_BIOGAS_WERTE`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_BIOMASSE_BIOGAS_STANDARDEINSPEISEPROFIL`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_BIOMASSE_BIOGAS_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_DEPONIE_KLAER_GRUBENGAS_WERTE`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_DEPONIE_KLAER_GRUBENGAS_STANDARDEINSPEISEPROFIL`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_DEPONIE_KLAER_GRUBENGAS_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_GEOTHERMIE_WERTE`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_GEOTHERMIE_STANDARDEINSPEISEPROFIL`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_GEOTHERMIE_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_SOLAR_WERTE`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_SOLAR_STANDARDEINSPEISEPROFIL`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_SOLAR_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_WIND_OFFSHORE_WERTE`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_WIND_OFFSHORE_STANDARDEINSPEISEPROFIL`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_WIND_OFFSHORE_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_WIND_ONSHORE_WERTE`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_WIND_ONSHORE_STANDARDEINSPEISEPROFIL`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_WIND_ONSHORE_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_WASSERKRAFT_WERTE`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_WASSERKRAFT_STANDARDEINSPEISEPROFIL`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_WASSERKRAFT_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-g hbs-e2">**gueltigkeitszeitraum**</span> | — | object | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-f hbs-e3">[zeitraumId](/bo4e/202610/com/Zeitraum#zeitraumid)</span><span className="hbs-nr">00070</span> | zeitraumId | integer | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-g hbs-e2">**jahresverbrauchsprognose**</span> | — | object | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-f hbs-e3">[einheit](/bo4e/202610/com/Menge#einheit)</span><span className="hbs-nr">00080</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202610/enum/Mengeneinheit) | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`W`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`WH`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`KW`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`KWH`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`KVARH`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`MW`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`MWH`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`STUECK`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`KUBIKMETER`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`STUNDE`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`TAG`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`MONAT`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`JAHR`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`PROZENT`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`ANZAHL`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`VAR`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`KVAR`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`VARH`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`KWHK`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`Z16`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`KWT`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`WATT_PRO_QUADRATMETER`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`METER_PRO_SEKUNDE`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-f hbs-e3">[wert](/bo4e/202610/com/Menge#wert)</span><span className="hbs-nr">00090</span> | Wert | number (float) | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-g hbs-e2">**lastprofile** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-f hbs-e3">[bezeichnung](/bo4e/202610/com/Lastprofil#bezeichnung)</span><span className="hbs-nr">00100</span> | Bezeichnung des Profils | string | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-f hbs-e3">[einspeisung](/bo4e/202610/com/Lastprofil#einspeisung)</span><span className="hbs-nr">00110</span> | Kennzeichen Einspeisung | boolean | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-f hbs-e3">[profilart](/bo4e/202610/com/Lastprofil#profilart)</span><span className="hbs-nr">00120</span> | Profilart | [Enum Profilart](/bo4e/202610/enum/Profilart) | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`ART_STANDARDLASTPROFIL`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`ART_TAGESPARAMETERABHAENGIGES_LASTPROFIL`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`ART_LASTPROFIL`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-f hbs-e3">[profilschar](/bo4e/202610/com/Lastprofil#profilschar)</span><span className="hbs-nr">00130</span> | Profilschar des Profils | string | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-f hbs-e3">[verfahren](/bo4e/202610/com/Lastprofil#verfahren)</span><span className="hbs-nr">00140</span> | Profilverfahren | [Enum Profilverfahren](/bo4e/202610/enum/Profilverfahren) | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`SYNTHETISCH`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`ANALYTISCH`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-g hbs-e3">**tagesparameter**</span> | — | object | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-f hbs-e4">[dienstanbieter](/bo4e/202610/com/Tagesparameter#dienstanbieter)</span><span className="hbs-nr">00150</span> | dienstanbieter | string | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-f hbs-e4">[herausgeber](/bo4e/202610/com/Tagesparameter#herausgeber)</span><span className="hbs-nr">00160</span> | Herausgeber | [Enum Herausgeber](/bo4e/202610/enum/Herausgeber) | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`NB`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`BDEW`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`TUM`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-f hbs-e4">[klimazone](/bo4e/202610/com/Tagesparameter#klimazone)</span><span className="hbs-nr">00170</span> | klimazone | string | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-f hbs-e4">[temperaturmessstelle](/bo4e/202610/com/Tagesparameter#temperaturmessstelle)</span><span className="hbs-nr">00180</span> | temperaturmessstelle | string | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-f hbs-e3">[referenzprofilbezeichnung](/bo4e/202610/com/Lastprofil#referenzprofilbezeichnung)</span><span className="hbs-nr">00190</span> | Bezeichnung des Referenzprofils | string | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-g hbs-e2">**temperaturarbeit**</span> | — | object | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-f hbs-e3">[einheit](/bo4e/202610/com/Menge#einheit)</span><span className="hbs-nr">00200</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202610/enum/Mengeneinheit) | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`W`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`WH`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`KW`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`KWH`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`KVARH`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`MW`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`MWH`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`STUECK`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`KUBIKMETER`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`STUNDE`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`TAG`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`MONAT`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`JAHR`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`PROZENT`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`ANZAHL`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`VAR`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`KVAR`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`VARH`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`KWHK`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`Z16`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`KWT`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`WATT_PRO_QUADRATMETER`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`METER_PRO_SEKUNDE`</span> | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-f hbs-e3">[wert](/bo4e/202610/com/Menge#wert)</span><span className="hbs-nr">00210</span> | Wert | number (float) | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-g hbs-e2">**verbrauchsaufteilung**</span> | — | object | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[einheit](/bo4e/202610/com/Menge#einheit)</span><span className="hbs-nr">00220</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202610/enum/Mengeneinheit) | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`W`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`WH`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KW`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KWH`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KVARH`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MW`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MWH`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`STUECK`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KUBIKMETER`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`STUNDE`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`TAG`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MONAT`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`JAHR`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`PROZENT`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`ANZAHL`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`VAR`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KVAR`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`VARH`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KWHK`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`Z16`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KWT`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`WATT_PRO_QUADRATMETER`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`METER_PRO_SEKUNDE`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[wert](/bo4e/202610/com/Menge#wert)</span><span className="hbs-nr">00230</span> | Wert | number (float) | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e1">**MARKTLOKATION** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | Kann | Kann | — | Kann | — | Kann | — | — | — | — | — | Kann | — | — | — | Kann | Kann | — |
| <span className="hbs-f hbs-e2">[bilanzierungsgebiet](/bo4e/202610/bo/Marktlokation#bilanzierungsgebiet)</span><span className="hbs-nr">00240</span> | Bilanzierungsgebiet, dem das Netzgebiet zugeordnet ist - im Falle eines Strom Netzes. | string | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-f hbs-e2">[datenqualitaet](/bo4e/202610/bo/Marktlokation#datenqualitaet)</span><span className="hbs-nr">00250</span> | Datenqualitaet | [Enum Datenqualitaet](/bo4e/202610/enum/Datenqualitaet) | Kann | — | Kann | — | Kann | — | Kann | — | — | — | — | — | Kann | — | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`ERWARTETE_DATEN`</span> | — | — | Kann | — | Kann | — | Kann | — | Kann | — | — | — | — | — | Kann | — | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | Kann | — | Kann | — | Kann | — | Kann | — | — | — | — | — | Kann | — | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`INFORMATIVE_DATEN`</span> | — | — | Kann | — | Kann | — | Kann | — | Kann | — | — | — | — | — | Kann | — | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`GUELTIGE_DATEN`</span> | — | — | Kann | — | Kann | — | Kann | — | Kann | — | — | — | — | — | Kann | — | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN`</span> | — | — | Kann | — | Kann | — | Kann | — | Kann | — | — | — | — | — | Kann | — | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_KEINE_DATEN_VORHANDEN`</span> | — | — | Kann | — | Kann | — | Kann | — | Kann | — | — | — | — | — | Kann | — | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN_ERWARTET`</span> | — | — | Kann | — | Kann | — | Kann | — | Kann | — | — | — | — | — | Kann | — | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_DATEN`</span> | — | — | Kann | — | Kann | — | Kann | — | Kann | — | — | — | — | — | Kann | — | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_ERWARTETE_DATEN`</span> | — | — | Kann | — | Kann | — | Kann | — | Kann | — | — | — | — | — | Kann | — | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | Kann | — | Kann | — | Kann | — | Kann | — | — | — | — | — | Kann | — | — | — | Kann | Kann | — |
| <span className="hbs-f hbs-e2">[marktlokationsId](/bo4e/202610/bo/Marktlokation#marktlokationsid)</span><span className="hbs-nr">00260</span> | Identifikationsnummer einer Marktlokation, an der Energie entweder<br/>verbraucht, oder erzeugt wird | string | Kann | Kann | Kann | — | — | — | Kann | — | — | — | — | — | Kann | — | — | — | Kann | Kann | — |
| <span className="hbs-f hbs-e2">[regelzone](/bo4e/202610/bo/Marktlokation#regelzone)</span><span className="hbs-nr">00270</span> | für EDIFACT mapping | string | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-g hbs-e2">**gueltigkeitszeitraum**</span> | — | object | Kann | Kann | Kann | — | Kann | — | Kann | — | — | — | — | — | Kann | — | — | — | Kann | — | — |
| <span className="hbs-f hbs-e3">[zeitraumId](/bo4e/202610/com/Zeitraum#zeitraumid)</span><span className="hbs-nr">00280</span> | zeitraumId | integer | Kann | Kann | Kann | — | Kann | — | Kann | — | — | — | — | — | Kann | — | — | — | Kann | — | — |
| <span className="hbs-g hbs-e2">**marktrollen** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-f hbs-e3">[marktrolle](/bo4e/202610/bo/Marktteilnehmer#marktrolle)</span><span className="hbs-nr">00290</span> | Gibt im Klartext die Bezeichnung der Marktrolle an. | [Enum Marktrolle](/bo4e/202610/enum/Marktrolle) | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`NB`</span> | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`LF`</span> | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`MSB`</span> | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`MSBA`</span> | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`GMSB`</span> | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`MDL`</span> | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`DL`</span> | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`BKV`</span> | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`UENB`</span> | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`KUNDE-SELBST-NN`</span> | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`MGV`</span> | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`EIV`</span> | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`RB`</span> | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`KUNDE`</span> | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`INTERESSENT`</span> | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`KN`</span> | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`UBA`</span> | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`BIKO`</span> | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`ESA`</span> | — | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-f hbs-e3">[rollencodenummer](/bo4e/202610/bo/Marktteilnehmer#rollencodenummer)</span><span className="hbs-nr">00300</span> | Gibt die Codenummer der Marktrolle an. | string | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-f hbs-e3">[messstellenbetreiberEigenschaft](/bo4e/202610/bo/Marktteilnehmer#messstellenbetreibereigenschaft)</span><span className="hbs-nr">00310</span> | MSBEigenschaft | [Enum MSBEigenschaft](/bo4e/202610/enum/MSBEigenschaft) | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`WETTBEWERBLICHER_MESSSTELLENBETREIBER`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`AUFFANGMESSSTELLENBETREIBER`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[weiterverpflichtet](/bo4e/202610/bo/Marktteilnehmer#weiterverpflichtet)</span><span className="hbs-nr">00320</span> | weiterverpflichtet | boolean | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[netzbetreiberCodeNr](/bo4e/202610/bo/Marktlokation#netzbetreibercodenr)</span><span className="hbs-nr">00330</span> | Codenummer des Netzbetreibers, an dessen Netz diese Marktlokation<br/>angeschlossen ist. | string | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**netznutzungsabrechnungsdaten** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[abschlag](/bo4e/202610/com/Netznutzungsabrechnungsdaten#abschlag)</span><span className="hbs-nr">00340</span> | Abschlag | number (float) | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[anzahl](/bo4e/202610/com/Netznutzungsabrechnungsdaten#anzahl)</span><span className="hbs-nr">00350</span> | Anzahl | integer | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[artikelId](/bo4e/202610/com/Netznutzungsabrechnungsdaten#artikelid)</span><span className="hbs-nr">00360</span> | artikelId | string | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[artikelIdTyp](/bo4e/202610/com/Netznutzungsabrechnungsdaten#artikelidtyp)</span><span className="hbs-nr">00370</span> | Liste von Artikel-IDs, z.B. für standardisierte vom BDEW herausgegebene Artikel, die im Strommarkt die BDEW-Artikelnummer ablösen | [Enum ArtikelIdTyp](/bo4e/202610/enum/ArtikelIdTyp) | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`ARTIKELID`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GRUPPENARTIKELID`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[gemeinderabatt](/bo4e/202610/com/Netznutzungsabrechnungsdaten#gemeinderabatt)</span><span className="hbs-nr">00380</span> | Gemeinderabatt | number (float) | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[zuschlag](/bo4e/202610/com/Netznutzungsabrechnungsdaten#zuschlag)</span><span className="hbs-nr">00390</span> | Zuschlag | number (float) | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e3">**preisSingulaereBetriebsmittel**</span> | — | object | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[wert](/bo4e/202610/com/Preis#wert)</span><span className="hbs-nr">00400</span> | wert | number (float) | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e3">**singulaereBetriebsmittel**</span> | — | object | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[wert](/bo4e/202610/com/Menge#wert)</span><span className="hbs-nr">00410</span> | Wert | number (float) | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e3">**zaehlzeiten**</span> | — | object | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[register](/bo4e/202610/com/Zaehlzeitregister#register)</span><span className="hbs-nr">00420</span> | Zählzeitregister | string | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[zaehlzeitDefinition](/bo4e/202610/com/Zaehlzeitregister#zaehlzeitdefinition)</span><span className="hbs-nr">00430</span> | Zählzeitdefinition | string | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**zaehlwerke** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | — | — | — | Kann | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[obisKennzahl](/bo4e/202610/com/Zaehlwerk#obiskennzahl)</span><span className="hbs-nr">00440</span> | Die OBIS-Kennzahl für das Zählwerk, die festlegt, welche auf die gemessene Größe mit dem Stand gemeldet wird.<br/>Nur Zählwerkstände mit dieser OBIS-Kennzahl werden an diesem Zählwerk registriert. Beispiel:1-0:1.8.1 für<br/>elektrische Wirkarbeit. | string | — | — | — | — | Kann | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[wertegranularitaet](/bo4e/202610/com/Zaehlwerk#wertegranularitaet)</span><span className="hbs-nr">00450</span> | Wertegranularitaet | [Enum Wertegranularitaet](/bo4e/202610/enum/Wertegranularitaet) | — | — | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`JAEHRLICH`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`HALBJAEHRLICH`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`QUARTALSWEISE`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MONATLICH`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-g hbs-e3">**zaehlzeiten**</span> | — | object | — | — | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[register](/bo4e/202610/com/Zaehlzeitregister#register)</span><span className="hbs-nr">00460</span> | Zählzeitregister | string | — | — | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[zaehlzeitDefinition](/bo4e/202610/com/Zaehlzeitregister#zaehlzeitdefinition)</span><span className="hbs-nr">00470</span> | Zählzeitdefinition | string | — | — | — | — | Kann | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[artEMobilitaet](/bo4e/202610/com/Zaehlwerk#artemobilitaet)</span><span className="hbs-nr">00480</span> | ArtEmobilitaet | [Enum ArtEmobilitaet](/bo4e/202610/enum/ArtEmobilitaet) | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`WB`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`LS`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`LP`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[unterbrechbarkeit](/bo4e/202610/com/Zaehlwerk#unterbrechbarkeit)</span><span className="hbs-nr">00490</span> | Stromverbrauchsart/Unterbrechbarkeit Marktlokation | [Enum Unterbrechbarkeit](/bo4e/202610/enum/Unterbrechbarkeit) | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`UV`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`NUV`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[verbrauchsart](/bo4e/202610/com/Zaehlwerk#verbrauchsart)</span><span className="hbs-nr">00500</span> | Stromverbrauchsart/Verbrauchsart Marktlokation | array | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[waermenutzung](/bo4e/202610/com/Zaehlwerk#waermenutzung)</span><span className="hbs-nr">00510</span> | Stromverbrauchsart/Wärmenutzung Marktlokation | [Enum Waermenutzung](/bo4e/202610/enum/Waermenutzung) | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`SPEICHERHEIZUNG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`WAERMEPUMPE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`DIREKTHEIZUNG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`WAERMEPUMPE_WAERME_KAELTE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`WAERMEPUMPE_KAELTE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`WAERMEPUMPE_WAERME`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[verwendungszweckLF](/bo4e/202610/com/Zaehlwerk#verwendungszwecklf)</span><span className="hbs-nr">00520</span> | Codes gemäß Codeliste der Verwendungszwecke Verwendungszweck LF | string | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[verwendungszweckNB](/bo4e/202610/com/Zaehlwerk#verwendungszwecknb)</span><span className="hbs-nr">00530</span> | Codes gemäß Codeliste der Verwendungszwecke Verwendungszweck NB | string | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[verwendungszweckUENB](/bo4e/202610/com/Zaehlwerk#verwendungszweckuenb)</span><span className="hbs-nr">00540</span> | Codes gemäß Codeliste der Verwendungszwecke Verwendungszweck ÜNB | string | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[fernsteuerbarkeit](/bo4e/202610/bo/Marktlokation#fernsteuerbarkeit)</span><span className="hbs-nr">00550</span> | Fernsteuerbarkeit | [Enum Fernsteuerbarkeit](/bo4e/202610/enum/Fernsteuerbarkeit) | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`TECHNISCH_NICHT_FERNSTEUERBAR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`TECHNISCH_FERNSTEUERBAR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`DURCH_LF_FERNSTEUERBAR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[messtechnischeEinordnung](/bo4e/202610/bo/Marktlokation#messtechnischeeinordnung)</span><span className="hbs-nr">00560</span> | Messtechnische Einordnung aus der UTILMD (IMS, KME_MME, KEINE_MESSUNG) | [Enum MesstechnischeEinordnung](/bo4e/202610/enum/MesstechnischeEinordnung) | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`IMS`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KME_MME`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KEINE_MESSUNG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[netzebene](/bo4e/202610/bo/Marktlokation#netzebene)</span><span className="hbs-nr">00570</span> | Netzebene, in der der Bezug der Energie erfolgt. Bei Strom Spannungsebene der<br/>Lieferung, bei Gas Druckstufe. Beispiel Strom: Niederspannung Beispiel Gas:<br/>Niederdruck. | [Enum Netzebene](/bo4e/202610/enum/Netzebene) | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`NSP`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`MSP`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`HSP`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`HSS`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`MSP_NSP_UMSP`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`HSP_MSP_UMSP`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`HSS_HSP_UMSP`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`HD`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`MD`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`ND`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[redispatch](/bo4e/202610/bo/Marktlokation#redispatch)</span><span className="hbs-nr">00580</span> | redispatch | boolean | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[statusErzeugendeMalo](/bo4e/202610/bo/Marktlokation#statuserzeugendemalo)</span><span className="hbs-nr">00590</span> | StatusErzeugendeMarktlokation | [Enum StatusErzeugendeMarktlokation](/bo4e/202610/enum/StatusErzeugendeMarktlokation) | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`EINSPEISEVERGUETUNG_PARAGRAPH_37`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`GEFOERDERTE_DIREKTVERMARKTUNG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`SONSTIGE_DIREKTVERMARKTUNG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`VERMARKTUNG_OHNE_GESETZL_VERGUETUNG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KWKG_VERGUETUNG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`EINSPEISEVERGUETUNG_PARAGRAPH_38_AUSFALLVERGUETUNG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[umspannung](/bo4e/202610/bo/Marktlokation#umspannung)</span><span className="hbs-nr">00600</span> | Netzebene | [Enum Netzebene](/bo4e/202610/enum/Netzebene) | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`NSP`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`MSP`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`HSP`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`HSS`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`MSP_NSP_UMSP`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`HSP_MSP_UMSP`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`HSS_HSP_UMSP`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`HD`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`MD`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`ND`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[verguetungEmpfaenger](/bo4e/202610/bo/Marktlokation#verguetungempfaenger)</span><span className="hbs-nr">00610</span> | VerguetungEmpfaenger | [Enum VerguetungEmpfaenger](/bo4e/202610/enum/VerguetungEmpfaenger) | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KUNDE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`LIEFERANT`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**eigentuemer**</span> | — | object | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[anrede](/bo4e/202610/bo/Geschaeftspartner#anrede)</span><span className="hbs-nr">00620</span> | Die Anrede für den GePa, Z.B. Herr. | string | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[gewerbekennzeichnung](/bo4e/202610/bo/Geschaeftspartner#gewerbekennzeichnung)</span><span className="hbs-nr">00630</span> | Kennzeichnung ob es sich um einen Gewerbe/Unternehmen (gewerbeKennzeichnung = true)<br/>oder eine Privatperson handelt. (gewerbeKennzeichnung = false) | boolean | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[name1](/bo4e/202610/bo/Geschaeftspartner#name1)</span><span className="hbs-nr">00640</span> | Erster Teil des Namens. Hier kann der Firmenname oder bei Privatpersonen<br/>beispielsweise der Nachname dargestellt werden. Beispiele: Yellow Strom GmbH<br/>oder Hagen | string | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[name2](/bo4e/202610/bo/Geschaeftspartner#name2)</span><span className="hbs-nr">00650</span> | Zweiter Teil des Namens. Hier kann der eine Erweiterung zum Firmennamen oder<br/>bei Privatpersonen beispielsweise der Vorname dargestellt werden. Beispiele:<br/>Bereich Süd oder Nina | string | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[name3](/bo4e/202610/bo/Geschaeftspartner#name3)</span><span className="hbs-nr">00660</span> | Dritter Teil des Namens. Hier können weitere Ergänzungen zum Firmennamen oder<br/>bei Privatpersonen Zusätze zum Namen dargestellt werden. Beispiele: und Afrika<br/>oder Sängerin | string | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[name4](/bo4e/202610/bo/Geschaeftspartner#name4)</span><span className="hbs-nr">00670</span> | name4 | string | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e3">**partneradresse**</span> | — | object | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[hausnummer](/bo4e/202610/com/Adresse#hausnummer)</span><span className="hbs-nr">00680</span> | Hausnummer und Ergänzung | string | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[landescode](/bo4e/202610/com/Adresse#landescode)</span><span className="hbs-nr">00690</span> | Landescode | [Enum Landescode](/bo4e/202610/enum/Landescode) | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AC`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AD`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AF`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AI`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AL`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AO`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AQ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AS`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AT`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AU`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AW`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AX`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AZ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BB`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BD`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BF`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BH`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BI`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BJ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BL`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BO`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BQ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BS`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BT`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BU`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BV`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BW`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BY`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BZ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CC`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CD`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CF`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CH`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CI`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CK`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CL`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CO`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CP`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CS`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CU`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CV`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CW`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CX`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CY`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CZ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`DE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`DG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`DJ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`DK`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`DM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`DO`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`DZ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`EA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`EC`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`EE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`EG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`EH`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ER`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ES`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ET`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`EU`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`FI`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`FJ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`FK`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`FM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`FO`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`FR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`FX`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GB`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GD`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GF`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GH`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GI`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GL`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GP`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GQ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GS`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GT`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GU`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GW`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GY`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`HK`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`HM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`HN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`HR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`HT`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`HU`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IC`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ID`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IL`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IO`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IQ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IS`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IT`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`JE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`JM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`JO`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`JP`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KH`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KI`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KP`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KW`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KY`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KZ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LB`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LC`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LI`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LK`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LS`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LT`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LU`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LV`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LY`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MC`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MD`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ME`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MF`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MH`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MK`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ML`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MO`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MP`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MQ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MS`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MT`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MU`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MV`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MW`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MX`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MY`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MZ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NC`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NF`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NI`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NL`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NO`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NP`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NT`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NU`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NZ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`OM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PF`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PH`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PK`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PL`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PS`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PT`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PW`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PY`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`QA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`RE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`RO`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`RS`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`RU`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`RW`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SB`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SC`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SD`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SF`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SH`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SI`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SJ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SK`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SL`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SO`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SS`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ST`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SU`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SV`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SX`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SY`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SZ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TC`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TD`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TF`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TJ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TK`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TL`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TO`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TP`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TT`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TV`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TW`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TZ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`UA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`UG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`UK`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`UM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`US`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`UY`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`UZ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`VA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`VC`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`VE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`VG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`VI`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`VN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`VU`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`WF`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`WS`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`XK`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`YE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`YT`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`YU`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ZA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ZM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ZR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ZW`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[ort](/bo4e/202610/com/Adresse#ort)</span><span className="hbs-nr">00700</span> | Ort | string | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[ortsteil](/bo4e/202610/com/Adresse#ortsteil)</span><span className="hbs-nr">00710</span> | Ortsteil | string | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[postfach](/bo4e/202610/com/Adresse#postfach)</span><span className="hbs-nr">00720</span> | Postfach | string | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[postleitzahl](/bo4e/202610/com/Adresse#postleitzahl)</span><span className="hbs-nr">00730</span> | Postleitzahl | string | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[strasse](/bo4e/202610/com/Adresse#strasse)</span><span className="hbs-nr">00740</span> | Strasse | string | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**energieherkunft** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[erzeugungsart](/bo4e/202610/com/Energieherkunft#erzeugungsart)</span><span className="hbs-nr">00750</span> | Art der Erzeugung | [Enum Erzeugungsart](/bo4e/202610/enum/Erzeugungsart) | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`EEG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KWK`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`EEG_DV`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KWK_DV`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`WIND`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`SOLAR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KERNKRAFT`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`WASSER`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GEOTHERMIE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BIOMASSE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KOHLE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GAS`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`SONSTIGE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`SONSTIGE_EEG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`SONSTIGE_ERZEUGUNGSART`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**hausverwalter**</span> | — | object | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[anrede](/bo4e/202610/bo/Geschaeftspartner#anrede)</span><span className="hbs-nr">00760</span> | Die Anrede für den GePa, Z.B. Herr. | string | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[gewerbekennzeichnung](/bo4e/202610/bo/Geschaeftspartner#gewerbekennzeichnung)</span><span className="hbs-nr">00770</span> | Kennzeichnung ob es sich um einen Gewerbe/Unternehmen (gewerbeKennzeichnung = true)<br/>oder eine Privatperson handelt. (gewerbeKennzeichnung = false) | boolean | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[name1](/bo4e/202610/bo/Geschaeftspartner#name1)</span><span className="hbs-nr">00780</span> | Erster Teil des Namens. Hier kann der Firmenname oder bei Privatpersonen<br/>beispielsweise der Nachname dargestellt werden. Beispiele: Yellow Strom GmbH<br/>oder Hagen | string | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[name2](/bo4e/202610/bo/Geschaeftspartner#name2)</span><span className="hbs-nr">00790</span> | Zweiter Teil des Namens. Hier kann der eine Erweiterung zum Firmennamen oder<br/>bei Privatpersonen beispielsweise der Vorname dargestellt werden. Beispiele:<br/>Bereich Süd oder Nina | string | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[name3](/bo4e/202610/bo/Geschaeftspartner#name3)</span><span className="hbs-nr">00800</span> | Dritter Teil des Namens. Hier können weitere Ergänzungen zum Firmennamen oder<br/>bei Privatpersonen Zusätze zum Namen dargestellt werden. Beispiele: und Afrika<br/>oder Sängerin | string | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[name4](/bo4e/202610/bo/Geschaeftspartner#name4)</span><span className="hbs-nr">00810</span> | name4 | string | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e3">**partneradresse**</span> | — | object | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[hausnummer](/bo4e/202610/com/Adresse#hausnummer)</span><span className="hbs-nr">00820</span> | Hausnummer und Ergänzung | string | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[landescode](/bo4e/202610/com/Adresse#landescode)</span><span className="hbs-nr">00830</span> | Landescode | [Enum Landescode](/bo4e/202610/enum/Landescode) | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AC`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AD`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AF`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AI`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AL`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AO`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AQ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AS`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AT`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AU`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AW`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AX`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AZ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BB`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BD`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BF`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BH`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BI`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BJ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BL`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BO`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BQ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BS`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BT`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BU`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BV`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BW`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BY`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BZ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CC`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CD`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CF`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CH`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CI`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CK`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CL`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CO`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CP`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CS`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CU`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CV`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CW`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CX`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CY`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CZ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`DE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`DG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`DJ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`DK`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`DM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`DO`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`DZ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`EA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`EC`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`EE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`EG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`EH`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ER`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ES`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ET`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`EU`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`FI`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`FJ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`FK`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`FM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`FO`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`FR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`FX`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GB`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GD`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GF`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GH`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GI`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GL`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GP`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GQ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GS`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GT`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GU`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GW`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GY`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`HK`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`HM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`HN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`HR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`HT`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`HU`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IC`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ID`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IL`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IO`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IQ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IS`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IT`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`JE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`JM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`JO`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`JP`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KH`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KI`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KP`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KW`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KY`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KZ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LB`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LC`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LI`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LK`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LS`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LT`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LU`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LV`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LY`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MC`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MD`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ME`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MF`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MH`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MK`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ML`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MO`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MP`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MQ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MS`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MT`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MU`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MV`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MW`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MX`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MY`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MZ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NC`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NF`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NI`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NL`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NO`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NP`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NT`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NU`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NZ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`OM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PF`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PH`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PK`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PL`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PS`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PT`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PW`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PY`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`QA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`RE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`RO`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`RS`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`RU`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`RW`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SB`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SC`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SD`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SF`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SH`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SI`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SJ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SK`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SL`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SO`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SS`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ST`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SU`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SV`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SX`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SY`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SZ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TC`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TD`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TF`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TJ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TK`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TL`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TO`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TP`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TT`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TV`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TW`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TZ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`UA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`UG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`UK`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`UM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`US`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`UY`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`UZ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`VA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`VC`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`VE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`VG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`VI`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`VN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`VU`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`WF`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`WS`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`XK`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`YE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`YT`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`YU`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ZA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ZM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ZR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ZW`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[ort](/bo4e/202610/com/Adresse#ort)</span><span className="hbs-nr">00840</span> | Ort | string | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[ortsteil](/bo4e/202610/com/Adresse#ortsteil)</span><span className="hbs-nr">00850</span> | Ortsteil | string | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[postfach](/bo4e/202610/com/Adresse#postfach)</span><span className="hbs-nr">00860</span> | Postfach | string | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[postleitzahl](/bo4e/202610/com/Adresse#postleitzahl)</span><span className="hbs-nr">00870</span> | Postleitzahl | string | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[strasse](/bo4e/202610/com/Adresse#strasse)</span><span className="hbs-nr">00880</span> | Strasse | string | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**lokationsadresse**</span> | — | object | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[hausnummer](/bo4e/202610/com/Adresse#hausnummer)</span><span className="hbs-nr">00890</span> | Hausnummer und Ergänzung | string | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[landescode](/bo4e/202610/com/Adresse#landescode)</span><span className="hbs-nr">00900</span> | Landescode | [Enum Landescode](/bo4e/202610/enum/Landescode) | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`AC`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`AD`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`AE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`AF`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`AG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`AI`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`AL`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`AM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`AN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`AO`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`AQ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`AR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`AS`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`AT`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`AU`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`AW`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`AX`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`AZ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BB`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BD`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BF`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BH`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BI`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BJ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BL`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BO`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BQ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BS`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BT`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BU`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BV`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BW`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BY`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BZ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`CA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`CC`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`CD`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`CF`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`CG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`CH`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`CI`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`CK`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`CL`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`CM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`CN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`CO`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`CP`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`CR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`CS`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`CU`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`CV`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`CW`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`CX`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`CY`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`CZ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`DE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`DG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`DJ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`DK`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`DM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`DO`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`DZ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`EA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`EC`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`EE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`EG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`EH`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`ER`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`ES`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`ET`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`EU`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`FI`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`FJ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`FK`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`FM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`FO`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`FR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`FX`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GB`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GD`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GF`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GH`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GI`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GL`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GP`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GQ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GS`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GT`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GU`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GW`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GY`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`HK`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`HM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`HN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`HR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`HT`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`HU`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`IC`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`ID`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`IE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`IL`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`IM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`IN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`IO`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`IQ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`IR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`IS`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`IT`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`JE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`JM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`JO`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`JP`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KH`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KI`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KP`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KW`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KY`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KZ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`LA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`LB`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`LC`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`LI`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`LK`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`LR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`LS`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`LT`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`LU`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`LV`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`LY`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MC`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MD`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`ME`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MF`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MH`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MK`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`ML`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MO`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MP`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MQ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MS`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MT`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MU`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MV`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MW`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MX`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MY`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MZ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`NA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`NC`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`NE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`NF`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`NG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`NI`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`NL`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`NO`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`NP`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`NR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`NT`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`NU`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`NZ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`OM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`PA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`PE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`PF`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`PG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`PH`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`PK`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`PL`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`PM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`PN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`PR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`PS`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`PT`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`PW`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`PY`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`QA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`RE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`RO`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`RS`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`RU`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`RW`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`SA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`SB`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`SC`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`SD`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`SE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`SF`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`SG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`SH`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`SI`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`SJ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`SK`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`SL`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`SM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`SN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`SO`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`SR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`SS`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`ST`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`SU`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`SV`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`SX`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`SY`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`SZ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`TA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`TC`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`TD`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`TF`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`TG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`TJ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`TK`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`TL`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`TM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`TN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`TO`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`TP`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`TR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`TT`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`TV`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`TW`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`TZ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`UA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`UG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`UK`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`UM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`US`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`UY`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`UZ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`VA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`VC`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`VE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`VG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`VI`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`VN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`VU`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`WF`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`WS`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`XK`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`YE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`YT`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`YU`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`ZA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`ZM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`ZR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`ZW`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[ort](/bo4e/202610/com/Adresse#ort)</span><span className="hbs-nr">00910</span> | Ort | string | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[ortsteil](/bo4e/202610/com/Adresse#ortsteil)</span><span className="hbs-nr">00920</span> | Ortsteil | string | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[postfach](/bo4e/202610/com/Adresse#postfach)</span><span className="hbs-nr">00930</span> | Postfach | string | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[postleitzahl](/bo4e/202610/com/Adresse#postleitzahl)</span><span className="hbs-nr">00940</span> | Postleitzahl | string | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[strasse](/bo4e/202610/com/Adresse#strasse)</span><span className="hbs-nr">00950</span> | Strasse | string | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e3">**zusatzInformation**</span> | — | object | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[zusatz1](/bo4e/202610/com/AdresszusatzInformation#zusatz1)</span><span className="hbs-nr">00960</span> | Adresszusatz 1 | string | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[zusatz2](/bo4e/202610/com/AdresszusatzInformation#zusatz2)</span><span className="hbs-nr">00970</span> | Adresszusatz 2 | string | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[zusatz3](/bo4e/202610/com/AdresszusatzInformation#zusatz3)</span><span className="hbs-nr">00980</span> | Adresszusatz 3 | string | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[zusatz4](/bo4e/202610/com/AdresszusatzInformation#zusatz4)</span><span className="hbs-nr">00990</span> | Adresszusatz 4 | string | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[zusatz5](/bo4e/202610/com/AdresszusatzInformation#zusatz5)</span><span className="hbs-nr">01000</span> | Adresszusatz 5 | string | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**technischeEinrichtungen** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[technischeEinrichtungenVorhanden](/bo4e/202610/com/TechnischeEinrichtung#technischeeinrichtungenvorhanden)</span><span className="hbs-nr">01010</span> | true =&gt; ZH7, false =&gt; ZH8 | boolean | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[verbrauchsart](/bo4e/202610/com/TechnischeEinrichtung#verbrauchsart)</span><span className="hbs-nr">01020</span> | Verbrauchsart | [Enum Verbrauchsart](/bo4e/202610/enum/Verbrauchsart) | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KL`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`W`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`EMOB`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`SB`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`SW`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`WK`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[paketId](/bo4e/202610/bo/Marktlokation#paketid)</span><span className="hbs-nr">01030</span> | paketId | string | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — |
| <span className="hbs-g hbs-e1">**VERWENDUNGSZEITRAUM** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | — |
| <span className="hbs-f hbs-e2">[datenqualitaet](/bo4e/202610/bo/Verwendungszeitraum#datenqualitaet)</span><span className="hbs-nr">01040</span> | Datenqualitaet | [Enum Datenqualitaet](/bo4e/202610/enum/Datenqualitaet) | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`ERWARTETE_DATEN`</span> | — | — | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`INFORMATIVE_DATEN`</span> | — | — | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`GUELTIGE_DATEN`</span> | — | — | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN`</span> | — | — | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_KEINE_DATEN_VORHANDEN`</span> | — | — | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN_ERWARTET`</span> | — | — | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_DATEN`</span> | — | — | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_ERWARTETE_DATEN`</span> | — | — | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | — |
| <span className="hbs-f hbs-e2">[verwendungAb](/bo4e/202610/bo/Verwendungszeitraum#verwendungab)</span><span className="hbs-nr">01050</span> | verwendungAb | string (date-time) | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | — |
| <span className="hbs-f hbs-e2">[verwendungBis](/bo4e/202610/bo/Verwendungszeitraum#verwendungbis)</span><span className="hbs-nr">01060</span> | verwendungBis | string (date-time) | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | — | — |
| <span className="hbs-f hbs-e2">[zeitraumId](/bo4e/202610/bo/Verwendungszeitraum#zeitraumid)</span><span className="hbs-nr">01070</span> | zeitraumId | integer | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | Kann | — | — |
| <span className="hbs-g hbs-e1">**LOKATIONSBUENDEL** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[datenqualitaet](/bo4e/202610/bo/Lokationsbuendel#datenqualitaet)</span><span className="hbs-nr">01080</span> | Datenqualitaet | [Enum Datenqualitaet](/bo4e/202610/enum/Datenqualitaet) | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`ERWARTETE_DATEN`</span> | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`INFORMATIVE_DATEN`</span> | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`GUELTIGE_DATEN`</span> | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN`</span> | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_KEINE_DATEN_VORHANDEN`</span> | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN_ERWARTET`</span> | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_DATEN`</span> | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_ERWARTETE_DATEN`</span> | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[lokationsbuendelNummer](/bo4e/202610/bo/Lokationsbuendel#lokationsbuendelnummer)</span><span className="hbs-nr">01090</span> | lokationsbuendelNummer | integer | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[lokationsbuendelstrukturId](/bo4e/202610/bo/Lokationsbuendel#lokationsbuendelstrukturid)</span><span className="hbs-nr">01100</span> | lokationsbuendelstrukturId | string | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[standardisierteLokationsbuendelstruktur](/bo4e/202610/bo/Lokationsbuendel#standardisiertelokationsbuendelstruktur)</span><span className="hbs-nr">01110</span> | standardisierteLokationsbuendelstruktur | boolean | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**gueltigkeitszeitraum**</span> | — | object | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[zeitraumId](/bo4e/202610/com/Zeitraum#zeitraumid)</span><span className="hbs-nr">01120</span> | zeitraumId | integer | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**zuordnungObjectcode** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[referenzLokationsId](/bo4e/202610/com/ZuordnungObjectcode#referenzlokationsid)</span><span className="hbs-nr">01130</span> | referenzLokationsId | string | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[referenzLokationsTyp](/bo4e/202610/com/ZuordnungObjectcode#referenzlokationstyp)</span><span className="hbs-nr">01140</span> | Gibt an, ob es sich um eine Markt- oder Messlokation handelt | [Enum Lokationstyp](/bo4e/202610/enum/Lokationstyp) | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MALO`</span> | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MELO`</span> | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`NELO`</span> | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`TECHNISCHE_RESSOURCE`</span> | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`STEUERBARE_RESSOURCE`</span> | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`TRANCHE`</span> | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MABIS_ZAEHLPUNKT`</span> | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[referenzMarktlokationTechnischeRessource](/bo4e/202610/com/ZuordnungObjectcode#referenzmarktlokationtechnischeressource)</span><span className="hbs-nr">01150</span> | referenzMarktlokationTechnischeRessource | array | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[vorgelagerteLokationId](/bo4e/202610/com/ZuordnungObjectcode#vorgelagertelokationid)</span><span className="hbs-nr">01160</span> | vorgelagerteLokationId | string | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[vorgelagerteLokationTyp](/bo4e/202610/com/ZuordnungObjectcode#vorgelagertelokationtyp)</span><span className="hbs-nr">01170</span> | Gibt an, ob es sich um eine Markt- oder Messlokation handelt | [Enum Lokationstyp](/bo4e/202610/enum/Lokationstyp) | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MALO`</span> | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MELO`</span> | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`NELO`</span> | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`TECHNISCHE_RESSOURCE`</span> | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`STEUERBARE_RESSOURCE`</span> | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`TRANCHE`</span> | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MABIS_ZAEHLPUNKT`</span> | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e3">**objectcode** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[lokationsbuendelNummer](/bo4e/202610/com/Objectcode#lokationsbuendelnummer)</span><span className="hbs-nr">01180</span> | lokationsbuendelNummer | integer | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[objectcode](/bo4e/202610/com/Objectcode#objectcode)</span><span className="hbs-nr">01190</span> | objectcode | string | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e1">**MESSLOKATION** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | Kann | — | — | — | — | — | — | — | — | Muss | — | — | — | — | Muss | — | — | — |
| <span className="hbs-f hbs-e2">[messlokationsId](/bo4e/202610/bo/Messlokation#messlokationsid)</span><span className="hbs-nr">01200</span> | Die Messlokations-Identifikation. Das ist die frühere Zählpunktbezeichnung,<br/>z.B. DE 47108151234567 | string | — | Kann | — | — | — | — | — | — | — | — | Muss | — | — | — | — | Muss | — | — | — |
| <span className="hbs-g hbs-e2">**gueltigkeitszeitraum**</span> | — | object | — | Kann | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[zeitraumId](/bo4e/202610/com/Zeitraum#zeitraumid)</span><span className="hbs-nr">01210</span> | zeitraumId | integer | — | Kann | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e2">[datenqualitaet](/bo4e/202610/bo/Messlokation#datenqualitaet)</span><span className="hbs-nr">01220</span> | Datenqualitaet | [Enum Datenqualitaet](/bo4e/202610/enum/Datenqualitaet) | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`ERWARTETE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`INFORMATIVE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`GUELTIGE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_KEINE_DATEN_VORHANDEN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN_ERWARTET`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_ERWARTETE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — |
| <span className="hbs-g hbs-e2">**marktrollen** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[marktrolle](/bo4e/202610/bo/Marktteilnehmer#marktrolle)</span><span className="hbs-nr">01230</span> | Gibt im Klartext die Bezeichnung der Marktrolle an. | [Enum Marktrolle](/bo4e/202610/enum/Marktrolle) | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`NB`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`LF`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MSB`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MSBA`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GMSB`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MDL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`DL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BKV`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`UENB`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KUNDE-SELBST-NN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MGV`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`EIV`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`RB`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KUNDE`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`INTERESSENT`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`UBA`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BIKO`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`ESA`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[messstellenbetreiberEigenschaft](/bo4e/202610/bo/Marktteilnehmer#messstellenbetreibereigenschaft)</span><span className="hbs-nr">01240</span> | MSBEigenschaft | [Enum MSBEigenschaft](/bo4e/202610/enum/MSBEigenschaft) | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`WETTBEWERBLICHER_MESSSTELLENBETREIBER`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`AUFFANGMESSSTELLENBETREIBER`</span> | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[rollencodenummer](/bo4e/202610/bo/Marktteilnehmer#rollencodenummer)</span><span className="hbs-nr">01250</span> | Gibt die Codenummer der Marktrolle an. | string | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[weiterverpflichtet](/bo4e/202610/bo/Marktteilnehmer#weiterverpflichtet)</span><span className="hbs-nr">01260</span> | weiterverpflichtet | boolean | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[netzebenemessung](/bo4e/202610/bo/Messlokation#netzebenemessung)</span><span className="hbs-nr">01270</span> | Netzebene | [Enum Netzebene](/bo4e/202610/enum/Netzebene) | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`NSP`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`MSP`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`HSP`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`HSS`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`MSP_NSP_UMSP`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`HSP_MSP_UMSP`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`HSS_HSP_UMSP`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`HD`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`MD`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`ND`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-g hbs-e2">**ablesekartenempfaenger**</span> | — | object | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[anrede](/bo4e/202610/bo/Geschaeftspartner#anrede)</span><span className="hbs-nr">01280</span> | Die Anrede für den GePa, Z.B. Herr. | string | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[gewerbekennzeichnung](/bo4e/202610/bo/Geschaeftspartner#gewerbekennzeichnung)</span><span className="hbs-nr">01290</span> | Kennzeichnung ob es sich um einen Gewerbe/Unternehmen (gewerbeKennzeichnung = true)<br/>oder eine Privatperson handelt. (gewerbeKennzeichnung = false) | boolean | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[name1](/bo4e/202610/bo/Geschaeftspartner#name1)</span><span className="hbs-nr">01300</span> | Erster Teil des Namens. Hier kann der Firmenname oder bei Privatpersonen<br/>beispielsweise der Nachname dargestellt werden. Beispiele: Yellow Strom GmbH<br/>oder Hagen | string | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[name2](/bo4e/202610/bo/Geschaeftspartner#name2)</span><span className="hbs-nr">01310</span> | Zweiter Teil des Namens. Hier kann der eine Erweiterung zum Firmennamen oder<br/>bei Privatpersonen beispielsweise der Vorname dargestellt werden. Beispiele:<br/>Bereich Süd oder Nina | string | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[name3](/bo4e/202610/bo/Geschaeftspartner#name3)</span><span className="hbs-nr">01320</span> | Dritter Teil des Namens. Hier können weitere Ergänzungen zum Firmennamen oder<br/>bei Privatpersonen Zusätze zum Namen dargestellt werden. Beispiele: und Afrika<br/>oder Sängerin | string | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[name4](/bo4e/202610/bo/Geschaeftspartner#name4)</span><span className="hbs-nr">01330</span> | name4 | string | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-g hbs-e3">**partneradresse**</span> | — | object | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e4">[hausnummer](/bo4e/202610/com/Adresse#hausnummer)</span><span className="hbs-nr">01340</span> | Hausnummer und Ergänzung | string | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e4">[landescode](/bo4e/202610/com/Adresse#landescode)</span><span className="hbs-nr">01350</span> | Landescode | [Enum Landescode](/bo4e/202610/enum/Landescode) | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AC`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AD`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AE`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AF`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AG`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AI`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AM`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AO`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AQ`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AR`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AS`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AT`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AU`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AW`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AX`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`AZ`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BA`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BB`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BD`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BE`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BF`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BG`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BH`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BI`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BJ`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BM`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BO`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BQ`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BR`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BS`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BT`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BU`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BV`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BW`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BY`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BZ`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CA`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CC`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CD`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CF`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CG`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CH`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CI`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CK`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CM`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CO`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CP`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CR`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CS`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CU`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CV`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CW`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CX`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CY`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`CZ`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`DE`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`DG`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`DJ`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`DK`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`DM`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`DO`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`DZ`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`EA`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`EC`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`EE`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`EG`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`EH`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`ER`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`ES`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`ET`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`EU`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`FI`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`FJ`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`FK`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`FM`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`FO`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`FR`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`FX`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GA`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GB`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GD`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GE`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GF`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GG`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GH`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GI`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GM`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GP`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GQ`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GR`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GS`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GT`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GU`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GW`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GY`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`HK`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`HM`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`HN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`HR`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`HT`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`HU`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`IC`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`ID`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`IE`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`IL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`IM`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`IN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`IO`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`IQ`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`IR`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`IS`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`IT`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`JE`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`JM`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`JO`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`JP`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`KE`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`KG`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`KH`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`KI`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`KM`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`KN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`KP`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`KR`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`KW`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`KY`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`KZ`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`LA`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`LB`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`LC`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`LI`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`LK`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`LR`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`LS`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`LT`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`LU`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`LV`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`LY`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MA`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MC`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MD`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`ME`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MF`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MG`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MH`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MK`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`ML`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MM`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MO`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MP`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MQ`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MR`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MS`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MT`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MU`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MV`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MW`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MX`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MY`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MZ`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`NA`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`NC`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`NE`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`NF`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`NG`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`NI`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`NL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`NO`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`NP`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`NR`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`NT`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`NU`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`NZ`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`OM`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`PA`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`PE`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`PF`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`PG`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`PH`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`PK`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`PL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`PM`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`PN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`PR`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`PS`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`PT`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`PW`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`PY`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`QA`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`RE`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`RO`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`RS`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`RU`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`RW`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SA`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SB`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SC`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SD`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SE`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SF`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SG`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SH`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SI`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SJ`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SK`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SM`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SO`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SR`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SS`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`ST`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SU`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SV`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SX`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SY`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SZ`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TA`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TC`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TD`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TF`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TG`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TJ`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TK`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TM`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TO`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TP`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TR`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TT`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TV`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TW`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TZ`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`UA`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`UG`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`UK`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`UM`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`US`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`UY`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`UZ`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`VA`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`VC`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`VE`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`VG`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`VI`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`VN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`VU`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`WF`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`WS`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`XK`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`YE`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`YT`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`YU`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`ZA`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`ZM`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`ZR`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`ZW`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e4">[ort](/bo4e/202610/com/Adresse#ort)</span><span className="hbs-nr">01360</span> | Ort | string | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e4">[ortsteil](/bo4e/202610/com/Adresse#ortsteil)</span><span className="hbs-nr">01370</span> | Ortsteil | string | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e4">[postfach](/bo4e/202610/com/Adresse#postfach)</span><span className="hbs-nr">01380</span> | Postfach | string | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e4">[postleitzahl](/bo4e/202610/com/Adresse#postleitzahl)</span><span className="hbs-nr">01390</span> | Postleitzahl | string | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e4">[strasse](/bo4e/202610/com/Adresse#strasse)</span><span className="hbs-nr">01400</span> | Strasse | string | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-g hbs-e1">**NETZLOKATION** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | Kann | — | Muss | — | Muss | — | — | — | — | — | Muss | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[netzlokationsId](/bo4e/202610/bo/Netzlokation#netzlokationsid)</span><span className="hbs-nr">01410</span> | Identifikationsnummer einer Netzlokation, an der Energie entweder<br/>verbraucht, oder erzeugt wird (Like MarktlokationsId Marktlokation) | string | — | Kann | — | Muss | — | Muss | — | — | — | — | — | Muss | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**gueltigkeitszeitraum**</span> | — | object | — | Kann | — | Kann | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[zeitraumId](/bo4e/202610/com/Zeitraum#zeitraumid)</span><span className="hbs-nr">01420</span> | zeitraumId | integer | — | Kann | — | Kann | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[datenqualitaet](/bo4e/202610/bo/Netzlokation#datenqualitaet)</span><span className="hbs-nr">01430</span> | Datenqualitaet | [Enum Datenqualitaet](/bo4e/202610/enum/Datenqualitaet) | — | — | — | Kann | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`ERWARTETE_DATEN`</span> | — | — | — | — | — | Kann | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | — | Kann | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`INFORMATIVE_DATEN`</span> | — | — | — | — | — | Kann | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`GUELTIGE_DATEN`</span> | — | — | — | — | — | Kann | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN`</span> | — | — | — | — | — | Kann | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_KEINE_DATEN_VORHANDEN`</span> | — | — | — | — | — | Kann | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN_ERWARTET`</span> | — | — | — | — | — | Kann | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_DATEN`</span> | — | — | — | — | — | Kann | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_ERWARTETE_DATEN`</span> | — | — | — | — | — | Kann | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | — | Kann | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**abrechnungsdaten** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[abrechnungBlindarbeit](/bo4e/202610/com/Netznutzungsabrechnungsdaten#abrechnungblindarbeit)</span><span className="hbs-nr">01440</span> | abrechnungBlindarbeit | boolean | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[artikelId](/bo4e/202610/com/Netznutzungsabrechnungsdaten#artikelid)</span><span className="hbs-nr">01450</span> | artikelId | string | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[artikelIdTyp](/bo4e/202610/com/Netznutzungsabrechnungsdaten#artikelidtyp)</span><span className="hbs-nr">01460</span> | Liste von Artikel-IDs, z.B. für standardisierte vom BDEW herausgegebene Artikel, die im Strommarkt die BDEW-Artikelnummer ablösen | [Enum ArtikelIdTyp](/bo4e/202610/enum/ArtikelIdTyp) | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`ARTIKELID`</span> | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GRUPPENARTIKELID`</span> | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[zahlerBlindarbeit](/bo4e/202610/com/Netznutzungsabrechnungsdaten#zahlerblindarbeit)</span><span className="hbs-nr">01470</span> | ZahlerBlindarbeit | [Enum ZahlerBlindarbeit](/bo4e/202610/enum/ZahlerBlindarbeit) | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`ANSCHLUSSNUTZER`</span> | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`LIEFERANT`</span> | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`NICHT_FESTGELEGT`</span> | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**marktrollen** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[marktrolle](/bo4e/202610/bo/Marktteilnehmer#marktrolle)</span><span className="hbs-nr">01480</span> | Gibt im Klartext die Bezeichnung der Marktrolle an. | [Enum Marktrolle](/bo4e/202610/enum/Marktrolle) | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`NB`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`LF`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MSB`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MSBA`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GMSB`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MDL`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`DL`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BKV`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`UENB`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KUNDE-SELBST-NN`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MGV`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`EIV`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`RB`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KUNDE`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`INTERESSENT`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KN`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`UBA`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BIKO`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`ESA`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[messstellenbetreiberEigenschaft](/bo4e/202610/bo/Marktteilnehmer#messstellenbetreibereigenschaft)</span><span className="hbs-nr">01490</span> | MSBEigenschaft | [Enum MSBEigenschaft](/bo4e/202610/enum/MSBEigenschaft) | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`WETTBEWERBLICHER_MESSSTELLENBETREIBER`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`AUFFANGMESSSTELLENBETREIBER`</span> | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[rollencodenummer](/bo4e/202610/bo/Marktteilnehmer#rollencodenummer)</span><span className="hbs-nr">01500</span> | Gibt die Codenummer der Marktrolle an. | string | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[keinKonfigurationsprodukt](/bo4e/202610/bo/Netzlokation#keinkonfigurationsprodukt)</span><span className="hbs-nr">01510</span> | keinKonfigurationsprodukt | boolean | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[konfigurationsprodukt](/bo4e/202610/bo/Netzlokation#konfigurationsprodukt)</span><span className="hbs-nr">01520</span> | konfigurationsprodukt | string | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[leistungskurvendefinition](/bo4e/202610/bo/Netzlokation#leistungskurvendefinition)</span><span className="hbs-nr">01530</span> | Code der Zugeordnete Leistungskurvendefinition für das Objekt | string | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[produktdatenRelevanteRolle](/bo4e/202610/bo/Netzlokation#produktdatenrelevanterolle)</span><span className="hbs-nr">01540</span> | Diese Rollen kann ein Marktteilnehmer einnehmen | [Enum Marktrolle](/bo4e/202610/enum/Marktrolle) | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`NB`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`LF`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`MSB`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`MSBA`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`GMSB`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`MDL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`DL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`BKV`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`UENB`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KUNDE-SELBST-NN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`MGV`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`EIV`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`RB`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KUNDE`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`INTERESSENT`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`UBA`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`BIKO`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`ESA`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[steuerkanal](/bo4e/202610/bo/Netzlokation#steuerkanal)</span><span className="hbs-nr">01550</span> | Ob ein Steuerkanal der Netzlokation zugeordnet ist und somit die Netzlokation gesteuert<br/>werden kann.<br/>ZF2: Kein Steuerkanal vorhanden<br/>ZF3: Steuerkanal vorhanden | boolean | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**auftraggebenderMarktpartner**</span> | — | object | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[marktrolle](/bo4e/202610/bo/Marktteilnehmer#marktrolle)</span><span className="hbs-nr">01560</span> | Gibt im Klartext die Bezeichnung der Marktrolle an. | [Enum Marktrolle](/bo4e/202610/enum/Marktrolle) | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`NB`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`LF`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MSB`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MSBA`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GMSB`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MDL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`DL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BKV`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`UENB`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KUNDE-SELBST-NN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MGV`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`EIV`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`RB`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KUNDE`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`INTERESSENT`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`UBA`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BIKO`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`ESA`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[rollencodenummer](/bo4e/202610/bo/Marktteilnehmer#rollencodenummer)</span><span className="hbs-nr">01570</span> | Gibt die Codenummer der Marktrolle an. | string | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**zaehlwerke** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[keinProdukt](/bo4e/202610/com/Zaehlwerk#keinprodukt)</span><span className="hbs-nr">01580</span> | CCI+11++ZF6: keinProdukt zugeordnet | boolean | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[obisKennzahl](/bo4e/202610/com/Zaehlwerk#obiskennzahl)</span><span className="hbs-nr">01590</span> | Die OBIS-Kennzahl für das Zählwerk, die festlegt, welche auf die gemessene Größe mit dem Stand gemeldet wird.<br/>Nur Zählwerkstände mit dieser OBIS-Kennzahl werden an diesem Zählwerk registriert. Beispiel:1-0:1.8.1 für<br/>elektrische Wirkarbeit. | string | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[verwendungszweckLF](/bo4e/202610/com/Zaehlwerk#verwendungszwecklf)</span><span className="hbs-nr">01600</span> | Codes gemäß Codeliste der Verwendungszwecke Verwendungszweck LF | string | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[verwendungszweckNB](/bo4e/202610/com/Zaehlwerk#verwendungszwecknb)</span><span className="hbs-nr">01610</span> | Codes gemäß Codeliste der Verwendungszwecke Verwendungszweck NB | string | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e1">**STEUERBARE_RESSOURCE** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | Kann | — | — | — | — | — | — | Muss | — | — | — | — | Muss | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[ressourcenId](/bo4e/202610/bo/SteuerbareRessource#ressourcenid)</span><span className="hbs-nr">01620</span> | ressourcenId | string | — | Kann | — | — | — | — | — | — | Muss | — | — | — | — | Muss | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**gueltigkeitszeitraum**</span> | — | object | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[zeitraumId](/bo4e/202610/com/Zeitraum#zeitraumid)</span><span className="hbs-nr">01630</span> | zeitraumId | integer | — | Kann | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[datenqualitaet](/bo4e/202610/bo/SteuerbareRessource#datenqualitaet)</span><span className="hbs-nr">01640</span> | Datenqualitaet | [Enum Datenqualitaet](/bo4e/202610/enum/Datenqualitaet) | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`ERWARTETE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`INFORMATIVE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`GUELTIGE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_KEINE_DATEN_VORHANDEN`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN_ERWARTET`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_ERWARTETE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**marktrollen** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[marktrolle](/bo4e/202610/bo/Marktteilnehmer#marktrolle)</span><span className="hbs-nr">01650</span> | Gibt im Klartext die Bezeichnung der Marktrolle an. | [Enum Marktrolle](/bo4e/202610/enum/Marktrolle) | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`NB`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`LF`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MSB`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MSBA`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GMSB`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MDL`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`DL`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BKV`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`UENB`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KUNDE-SELBST-NN`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MGV`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`EIV`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`RB`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KUNDE`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`INTERESSENT`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KN`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`UBA`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BIKO`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`ESA`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[messstellenbetreiberEigenschaft](/bo4e/202610/bo/Marktteilnehmer#messstellenbetreibereigenschaft)</span><span className="hbs-nr">01660</span> | MSBEigenschaft | [Enum MSBEigenschaft](/bo4e/202610/enum/MSBEigenschaft) | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`WETTBEWERBLICHER_MESSSTELLENBETREIBER`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`AUFFANGMESSSTELLENBETREIBER`</span> | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[rollencodenummer](/bo4e/202610/bo/Marktteilnehmer#rollencodenummer)</span><span className="hbs-nr">01670</span> | Gibt die Codenummer der Marktrolle an. | string | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[keinKonfigurationsprodukt](/bo4e/202610/bo/SteuerbareRessource#keinkonfigurationsprodukt)</span><span className="hbs-nr">01680</span> | keinKonfigurationsprodukt | boolean | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[konfigurationsprodukt](/bo4e/202610/bo/SteuerbareRessource#konfigurationsprodukt)</span><span className="hbs-nr">01690</span> | konfigurationsprodukt | string | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[produktdatenRelevanteRolle](/bo4e/202610/bo/SteuerbareRessource#produktdatenrelevanterolle)</span><span className="hbs-nr">01700</span> | Diese Rollen kann ein Marktteilnehmer einnehmen | [Enum Marktrolle](/bo4e/202610/enum/Marktrolle) | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`NB`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`LF`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`MSB`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`MSBA`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`GMSB`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`MDL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`DL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`BKV`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`UENB`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KUNDE-SELBST-NN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`MGV`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`EIV`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`RB`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KUNDE`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`INTERESSENT`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`UBA`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`BIKO`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`ESA`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[steuerkanal](/bo4e/202610/bo/SteuerbareRessource#steuerkanal)</span><span className="hbs-nr">01710</span> | Steuerkanal | [Enum Steuerkanal](/bo4e/202610/enum/Steuerkanal) | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`AN_AUS`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`GESTUFT`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**auftraggebenderMarktpartner**</span> | — | object | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[marktrolle](/bo4e/202610/bo/Marktteilnehmer#marktrolle)</span><span className="hbs-nr">01720</span> | Gibt im Klartext die Bezeichnung der Marktrolle an. | [Enum Marktrolle](/bo4e/202610/enum/Marktrolle) | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`NB`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`LF`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MSB`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MSBA`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`GMSB`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MDL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`DL`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BKV`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`UENB`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KUNDE-SELBST-NN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`MGV`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`EIV`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`RB`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KUNDE`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`INTERESSENT`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`UBA`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`BIKO`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`ESA`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[rollencodenummer](/bo4e/202610/bo/Marktteilnehmer#rollencodenummer)</span><span className="hbs-nr">01730</span> | Gibt die Codenummer der Marktrolle an. | string | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**zugeordneteDefinition**</span> | — | object | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[leistungskurvendefinition](/bo4e/202610/com/ZugeordneteDefinition#leistungskurvendefinition)</span><span className="hbs-nr">01740</span> | leistungskurvendefinition | string | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[schaltzeitdefinition](/bo4e/202610/com/ZugeordneteDefinition#schaltzeitdefinition)</span><span className="hbs-nr">01750</span> | schaltzeitdefinition | string | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — |
| <span className="hbs-g hbs-e1">**TECHNISCHE_RESSOURCE** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | Kann | — | — | — | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[ressourcenId](/bo4e/202610/bo/TechnischeRessource#ressourcenid)</span><span className="hbs-nr">01760</span> | ressourcenId | string | — | Kann | — | — | — | — | — | Muss | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**gueltigkeitszeitraum**</span> | — | object | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[zeitraumId](/bo4e/202610/com/Zeitraum#zeitraumid)</span><span className="hbs-nr">01770</span> | zeitraumId | integer | — | Kann | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[art](/bo4e/202610/bo/TechnischeRessource#art)</span><span className="hbs-nr">01780</span> | TechnischeRessourceArt | [Enum TechnischeRessourceArt](/bo4e/202610/enum/TechnischeRessourceArt) | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`STROMERZEUGUNG`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`STROMVERBRAUCH`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`SPEICHER`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[artEMobilitaet](/bo4e/202610/bo/TechnischeRessource#artemobilitaet)</span><span className="hbs-nr">01790</span> | ArtEmobilitaet | [Enum ArtEmobilitaet](/bo4e/202610/enum/ArtEmobilitaet) | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`WB`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`LS`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`LP`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[datenqualitaet](/bo4e/202610/bo/TechnischeRessource#datenqualitaet)</span><span className="hbs-nr">01800</span> | Datenqualitaet | [Enum Datenqualitaet](/bo4e/202610/enum/Datenqualitaet) | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`ERWARTETE_DATEN`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`INFORMATIVE_DATEN`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`GUELTIGE_DATEN`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_KEINE_DATEN_VORHANDEN`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN_ERWARTET`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_DATEN`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_ERWARTETE_DATEN`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[einordnung](/bo4e/202610/bo/TechnischeRessource#einordnung)</span><span className="hbs-nr">01810</span> | RessourceWechselmoeglichkeit | [Enum RessourceWechselmoeglichkeit](/bo4e/202610/enum/RessourceWechselmoeglichkeit) | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`WECHSELMOEGLICHKEIT_EINMALIG_NOCH_MOEGLICH`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`WECHSELMOEGLICHKEIT_NICHT_MOEGLICH`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`BEFRISTET_OHNE_WECHSELMOEGLICHKEIT`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`WECHSEL_WURDE_DURCHGEFUEHRT`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[enwg](/bo4e/202610/bo/TechnischeRessource#enwg)</span><span className="hbs-nr">01820</span> | enwg | boolean | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[erzeugungsart](/bo4e/202610/bo/TechnischeRessource#erzeugungsart)</span><span className="hbs-nr">01830</span> | Art der Erzeugung der Energie. Details Erzeugungsart<br/>Beispiel: CAV+ZF5'<br/>Erzeugungsart:<br/>ZF5: Solar<br/>ZF6: Wind<br/>ZG0: Gas<br/>ZG1: Wasser<br/>ZG5: Sonstige Erzeugungsart | [Enum Erzeugungsart](/bo4e/202610/enum/Erzeugungsart) | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`EEG`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KWK`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`EEG_DV`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KWK_DV`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`WIND`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`SOLAR`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KERNKRAFT`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`WASSER`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`GEOTHERMIE`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`BIOMASSE`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KOHLE`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`GAS`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`SONSTIGE`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`SONSTIGE_EEG`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`SONSTIGE_ERZEUGUNGSART`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[inbetriebsetzungsdatum](/bo4e/202610/bo/TechnischeRessource#inbetriebsetzungsdatum)</span><span className="hbs-nr">01840</span> | Inbetriebsetzung | [Enum Inbetriebsetzung](/bo4e/202610/enum/Inbetriebsetzung) | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`INBETRIEBSETZUNG_NACH_2023`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`INBETRIEBSETZUNG_VOR_2024`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[referenzNetzlokation](/bo4e/202610/bo/TechnischeRessource#referenznetzlokation)</span><span className="hbs-nr">01850</span> | referenzNetzlokation | string | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[referenzSteuerbareRessource](/bo4e/202610/bo/TechnischeRessource#referenzsteuerbareressource)</span><span className="hbs-nr">01860</span> | referenzSteuerbareRessource | string | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[referenzTranche](/bo4e/202610/bo/TechnischeRessource#referenztranche)</span><span className="hbs-nr">01870</span> | referenzTranche | string | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[speicherart](/bo4e/202610/bo/TechnischeRessource#speicherart)</span><span className="hbs-nr">01880</span> | Art der speicher. Details Speicherart<br/>Beispiel: CAV+ZF7'<br/>Speicherart:<br/>ZF7: Wasserstoffspeicher<br/>ZF8: Pumpspeicher<br/>ZF9: Batteriespeicher<br/>ZG6: Sonstige Speicherart | [Enum Speicherart](/bo4e/202610/enum/Speicherart) | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`WASSERSTOFFSPEICHER`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`PUMPSPEICHER`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`BATTERIESPEICHER`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`SONSTIGE_SPEICHERART`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[speicherkapazitaet](/bo4e/202610/bo/TechnischeRessource#speicherkapazitaet)</span><span className="hbs-nr">01890</span> | Speicherkapazität<br/>Beispiel: QTY+Z42:100:KWH' | number (float) | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[verbrauchsart](/bo4e/202610/bo/TechnischeRessource#verbrauchsart)</span><span className="hbs-nr">01900</span> | Verbrauchsart der Technischen Ressource<br/>Beispiel: CAV+Z64'<br/>Z64: Kraft/Licht<br/>Z65: Wärme<br/>ZE5: E-Mobilität<br/>ZA8: Straßenbeleuchtung | array | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[verguetungsverpflichtung](/bo4e/202610/bo/TechnischeRessource#verguetungsverpflichtung)</span><span className="hbs-nr">01910</span> | verguetungsverpflichtung | boolean | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[waermenutzung](/bo4e/202610/bo/TechnischeRessource#waermenutzung)</span><span className="hbs-nr">01920</span> | Wärmenutzung<br/>Beispiel: CAV+Z56'<br/>Z56: Speicherheizung<br/>Z57: Wärmepumpe<br/>Z61: Direktheizung | [Enum Waermenutzung](/bo4e/202610/enum/Waermenutzung) | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`SPEICHERHEIZUNG`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`WAERMEPUMPE`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`DIREKTHEIZUNG`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`WAERMEPUMPE_WAERME_KAELTE`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`WAERMEPUMPE_KAELTE`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`WAERMEPUMPE_WAERME`</span> | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**nennleistung**</span> | — | object | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[abgabe](/bo4e/202610/com/Nennleistung#abgabe)</span><span className="hbs-nr">01930</span> | Abgabe der Nennleistung | number (float) | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[aufnahme](/bo4e/202610/com/Nennleistung#aufnahme)</span><span className="hbs-nr">01940</span> | Aufnahme der Nennleistung | number (float) | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e1">**NETZNUTZUNGSVERTRAG** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | — | Kann | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**vertragskonditionen**</span> | — | object | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[naechstenetznutzungsabrechnung](/bo4e/202610/com/Vertragskonditionen#naechstenetznutzungsabrechnung)</span><span className="hbs-nr">01950</span> | naechstenetznutzungsabrechnung | string | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[netznutzungsabrechnungIntervall](/bo4e/202610/com/Vertragskonditionen#netznutzungsabrechnungintervall)</span><span className="hbs-nr">01960</span> | netznutzungsabrechnungIntervall | integer | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[netznutzungsabrechnungsgrundlage](/bo4e/202610/com/Vertragskonditionen#netznutzungsabrechnungsgrundlage)</span><span className="hbs-nr">01970</span> | Netznutzungsabrechnungsgrundlage | [Enum Netznutzungsabrechnungsgrundlage](/bo4e/202610/enum/Netznutzungsabrechnungsgrundlage) | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`LIEFERSCHEIN`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`ABWEICHENDE_GRUNDLAGE`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[netznutzungsvertrag](/bo4e/202610/com/Vertragskonditionen#netznutzungsvertrag)</span><span className="hbs-nr">01980</span> | Netznutzungsvertrag | [Enum Netznutzungsvertrag](/bo4e/202610/enum/Netznutzungsvertrag) | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KUNDEN_NB`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`LIEFERANTEN_NB`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[netznutzungszahler](/bo4e/202610/com/Vertragskonditionen#netznutzungszahler)</span><span className="hbs-nr">01990</span> | Netznutzungszahler | [Enum Netznutzungszahler](/bo4e/202610/enum/Netznutzungszahler) | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`KUNDE`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e4">`LIEFERANT`</span> | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e3">**netznutzungsabrechnung**</span> | — | object | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[abrechnungsZeitraum](/bo4e/202610/com/Zeitraum#abrechnungszeitraum)</span><span className="hbs-nr">02000</span> | abrechnungsZeitraum | string | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e2">[datenqualitaet](/bo4e/202610/bo/Vertrag#datenqualitaet)</span><span className="hbs-nr">02010</span> | Datenqualitaet | [Enum Datenqualitaet](/bo4e/202610/enum/Datenqualitaet) | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`ERWARTETE_DATEN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`INFORMATIVE_DATEN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`GUELTIGE_DATEN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_KEINE_DATEN_VORHANDEN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN_ERWARTET`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_DATEN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_ERWARTETE_DATEN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**gueltigkeitszeitraum**</span> | — | object | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[zeitraumId](/bo4e/202610/com/Zeitraum#zeitraumid)</span><span className="hbs-nr">02020</span> | zeitraumId | integer | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**korrespondenzpartner**</span> | — | object | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[anrede](/bo4e/202610/bo/Geschaeftspartner#anrede)</span><span className="hbs-nr">02030</span> | Die Anrede für den GePa, Z.B. Herr. | string | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[name1](/bo4e/202610/bo/Geschaeftspartner#name1)</span><span className="hbs-nr">02040</span> | Erster Teil des Namens. Hier kann der Firmenname oder bei Privatpersonen<br/>beispielsweise der Nachname dargestellt werden. Beispiele: Yellow Strom GmbH<br/>oder Hagen | string | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[name2](/bo4e/202610/bo/Geschaeftspartner#name2)</span><span className="hbs-nr">02050</span> | Zweiter Teil des Namens. Hier kann der eine Erweiterung zum Firmennamen oder<br/>bei Privatpersonen beispielsweise der Vorname dargestellt werden. Beispiele:<br/>Bereich Süd oder Nina | string | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[name3](/bo4e/202610/bo/Geschaeftspartner#name3)</span><span className="hbs-nr">02060</span> | Dritter Teil des Namens. Hier können weitere Ergänzungen zum Firmennamen oder<br/>bei Privatpersonen Zusätze zum Namen dargestellt werden. Beispiele: und Afrika<br/>oder Sängerin | string | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[name4](/bo4e/202610/bo/Geschaeftspartner#name4)</span><span className="hbs-nr">02070</span> | name4 | string | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e3">**ansprechpartner**</span> | — | object | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[eMailAdresse](/bo4e/202610/bo/Ansprechpartner#emailadresse)</span><span className="hbs-nr">02080</span> | E-Mail Adresse | string | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e4">**rufnummern** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e5">[nummerntyp](/bo4e/202610/com/Rufnummer#nummerntyp)</span><span className="hbs-nr">02090</span> | Rufnummernart | [Enum Rufnummernart](/bo4e/202610/enum/Rufnummernart) | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`RUF_ZENTRALE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`FAX_ZENTRALE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SAMMELRUF`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SAMMELFAX`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ABTEILUNGRUF`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ABTEILUNGFAX`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`RUF_DURCHWAHL`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`FAX_DURCHWAHL`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MOBIL_NUMMER`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e5">[rufnummer](/bo4e/202610/com/Rufnummer#rufnummer)</span><span className="hbs-nr">02100</span> | rufnummer | string | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e3">**partneradresse**</span> | — | object | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[hausnummer](/bo4e/202610/com/Adresse#hausnummer)</span><span className="hbs-nr">02110</span> | Hausnummer und Ergänzung | string | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[landescode](/bo4e/202610/com/Adresse#landescode)</span><span className="hbs-nr">02120</span> | Landescode | [Enum Landescode](/bo4e/202610/enum/Landescode) | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AC`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AD`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AF`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AI`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AL`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AO`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AQ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AS`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AT`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AU`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AW`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AX`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`AZ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BB`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BD`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BF`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BH`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BI`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BJ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BL`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BO`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BQ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BS`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BT`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BU`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BV`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BW`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BY`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`BZ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CC`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CD`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CF`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CH`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CI`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CK`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CL`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CO`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CP`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CS`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CU`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CV`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CW`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CX`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CY`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`CZ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`DE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`DG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`DJ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`DK`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`DM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`DO`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`DZ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`EA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`EC`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`EE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`EG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`EH`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ER`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ES`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ET`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`EU`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`FI`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`FJ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`FK`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`FM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`FO`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`FR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`FX`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GB`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GD`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GF`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GH`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GI`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GL`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GP`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GQ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GS`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GT`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GU`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GW`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`GY`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`HK`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`HM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`HN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`HR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`HT`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`HU`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IC`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ID`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IL`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IO`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IQ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IS`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`IT`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`JE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`JM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`JO`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`JP`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KH`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KI`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KP`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KW`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KY`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`KZ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LB`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LC`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LI`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LK`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LS`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LT`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LU`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LV`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`LY`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MC`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MD`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ME`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MF`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MH`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MK`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ML`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MO`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MP`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MQ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MS`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MT`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MU`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MV`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MW`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MX`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MY`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`MZ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NC`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NF`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NI`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NL`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NO`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NP`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NT`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NU`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`NZ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`OM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PF`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PH`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PK`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PL`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PS`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PT`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PW`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`PY`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`QA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`RE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`RO`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`RS`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`RU`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`RW`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SB`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SC`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SD`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SF`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SH`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SI`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SJ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SK`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SL`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SO`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SS`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ST`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SU`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SV`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SX`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SY`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`SZ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TC`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TD`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TF`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TJ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TK`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TL`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TO`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TP`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TT`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TV`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TW`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`TZ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`UA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`UG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`UK`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`UM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`US`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`UY`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`UZ`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`VA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`VC`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`VE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`VG`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`VI`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`VN`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`VU`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`WF`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`WS`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`XK`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`YE`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`YT`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`YU`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ZA`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ZM`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ZR`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e5">`ZW`</span> | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[ort](/bo4e/202610/com/Adresse#ort)</span><span className="hbs-nr">02130</span> | Ort | string | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[ortsteil](/bo4e/202610/com/Adresse#ortsteil)</span><span className="hbs-nr">02140</span> | Ortsteil | string | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[postfach](/bo4e/202610/com/Adresse#postfach)</span><span className="hbs-nr">02150</span> | Postfach | string | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[postleitzahl](/bo4e/202610/com/Adresse#postleitzahl)</span><span className="hbs-nr">02160</span> | Postleitzahl | string | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[strasse](/bo4e/202610/com/Adresse#strasse)</span><span className="hbs-nr">02170</span> | Strasse | string | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**vertragspartner2** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[anrede](/bo4e/202610/bo/Geschaeftspartner#anrede)</span><span className="hbs-nr">02180</span> | Die Anrede für den GePa, Z.B. Herr. | string | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[geschaeftspartnerrolle](/bo4e/202610/bo/Geschaeftspartner#geschaeftspartnerrolle)</span><span className="hbs-nr">02190</span> | Rolle, die der Geschäftspartner hat (z.B. Interessent, Kunde). | array | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[name1](/bo4e/202610/bo/Geschaeftspartner#name1)</span><span className="hbs-nr">02200</span> | Erster Teil des Namens. Hier kann der Firmenname oder bei Privatpersonen<br/>beispielsweise der Nachname dargestellt werden. Beispiele: Yellow Strom GmbH<br/>oder Hagen | string | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[name2](/bo4e/202610/bo/Geschaeftspartner#name2)</span><span className="hbs-nr">02210</span> | Zweiter Teil des Namens. Hier kann der eine Erweiterung zum Firmennamen oder<br/>bei Privatpersonen beispielsweise der Vorname dargestellt werden. Beispiele:<br/>Bereich Süd oder Nina | string | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[name3](/bo4e/202610/bo/Geschaeftspartner#name3)</span><span className="hbs-nr">02220</span> | Dritter Teil des Namens. Hier können weitere Ergänzungen zum Firmennamen oder<br/>bei Privatpersonen Zusätze zum Namen dargestellt werden. Beispiele: und Afrika<br/>oder Sängerin | string | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[name4](/bo4e/202610/bo/Geschaeftspartner#name4)</span><span className="hbs-nr">02230</span> | name4 | string | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e1">**AD_HOC_STEUERKANAL** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**IPAdresseCLSDevice**</span> | — | object | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[IPAdresseCLSDevice1](/bo4e/202610/com/IPAdresseCLSDevice#ipadresseclsdevice1)</span><span className="hbs-nr">02240</span> | IPAdresseCLSDevice1 | string | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[IPAdresseCLSDevice2](/bo4e/202610/com/IPAdresseCLSDevice#ipadresseclsdevice2)</span><span className="hbs-nr">02250</span> | IPAdresseCLSDevice2 | string | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[IPAdresseCLSDevice3](/bo4e/202610/com/IPAdresseCLSDevice#ipadresseclsdevice3)</span><span className="hbs-nr">02260</span> | IPAdresseCLSDevice3 | string | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[IPAdresseCLSDevice4](/bo4e/202610/com/IPAdresseCLSDevice#ipadresseclsdevice4)</span><span className="hbs-nr">02270</span> | IPAdresseCLSDevice4 | string | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[IPAdresseCLSDevice5](/bo4e/202610/com/IPAdresseCLSDevice#ipadresseclsdevice5)</span><span className="hbs-nr">02280</span> | IPAdresseCLSDevice5 | string | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**aussteller**</span> | — | object | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[aussteller1](/bo4e/202610/com/Aussteller#aussteller1)</span><span className="hbs-nr">02290</span> | aussteller1 | string | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[aussteller2](/bo4e/202610/com/Aussteller#aussteller2)</span><span className="hbs-nr">02300</span> | aussteller2 | string | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[aussteller3](/bo4e/202610/com/Aussteller#aussteller3)</span><span className="hbs-nr">02310</span> | aussteller3 | string | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[aussteller4](/bo4e/202610/com/Aussteller#aussteller4)</span><span className="hbs-nr">02320</span> | aussteller4 | string | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[aussteller5](/bo4e/202610/com/Aussteller#aussteller5)</span><span className="hbs-nr">02330</span> | aussteller5 | string | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**zertifikatsNutzer**</span> | — | object | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[zertifikatsNutzer1](/bo4e/202610/com/ZertifikatsNutzer#zertifikatsnutzer1)</span><span className="hbs-nr">02340</span> | zertifikatsNutzer1 | string | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[zertifikatsNutzer2](/bo4e/202610/com/ZertifikatsNutzer#zertifikatsnutzer2)</span><span className="hbs-nr">02350</span> | zertifikatsNutzer2 | string | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[zertifikatsNutzer3](/bo4e/202610/com/ZertifikatsNutzer#zertifikatsnutzer3)</span><span className="hbs-nr">02360</span> | zertifikatsNutzer3 | string | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[zertifikatsNutzer4](/bo4e/202610/com/ZertifikatsNutzer#zertifikatsnutzer4)</span><span className="hbs-nr">02370</span> | zertifikatsNutzer4 | string | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[zertifikatsNutzer5](/bo4e/202610/com/ZertifikatsNutzer#zertifikatsnutzer5)</span><span className="hbs-nr">02380</span> | zertifikatsNutzer5 | string | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**zieladresse**</span> | — | object | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[zieladresse1](/bo4e/202610/com/Zieladresse#zieladresse1)</span><span className="hbs-nr">02390</span> | zieladresse1 | string | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[zieladresse2](/bo4e/202610/com/Zieladresse#zieladresse2)</span><span className="hbs-nr">02400</span> | zieladresse2 | string | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[zieladresse3](/bo4e/202610/com/Zieladresse#zieladresse3)</span><span className="hbs-nr">02410</span> | zieladresse3 | string | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[zieladresse4](/bo4e/202610/com/Zieladresse#zieladresse4)</span><span className="hbs-nr">02420</span> | zieladresse4 | string | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[zieladresse5](/bo4e/202610/com/Zieladresse#zieladresse5)</span><span className="hbs-nr">02430</span> | zieladresse5 | string | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e1">**ZAEHLER** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e2">[datenqualitaet](/bo4e/202610/bo/Zaehler#datenqualitaet)</span><span className="hbs-nr">02440</span> | Datenqualitaet | [Enum Datenqualitaet](/bo4e/202610/enum/Datenqualitaet) | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`ERWARTETE_DATEN`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`INFORMATIVE_DATEN`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`GUELTIGE_DATEN`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_KEINE_DATEN_VORHANDEN`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN_ERWARTET`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_DATEN`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_ERWARTETE_DATEN`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e2">[gateway](/bo4e/202610/bo/Zaehler#gateway)</span><span className="hbs-nr">02450</span> | Angabe eines SMGW, mit dem der Zaehler parametrisiert ist | string | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e2">[zaehlernummer](/bo4e/202610/bo/Zaehler#zaehlernummer)</span><span className="hbs-nr">02460</span> | Nummerierung des Zählers, vergeben durch den Messstellenbetreiber | string | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-g hbs-e2">**geraete** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[geraetenummer](/bo4e/202610/com/Geraet#geraetenummer)</span><span className="hbs-nr">02470</span> | Die auf dem Geräte aufgedruckte Nummer, die vom MSB vergeben wird. | string | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[geraetetyp](/bo4e/202610/com/Geraet#geraetetyp)</span><span className="hbs-nr">02480</span> | Auflistung möglicher abzurechnender Gerätetypen | [Enum Geraetetyp](/bo4e/202610/enum/Geraetetyp) | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`WECHSELSTROMZAEHLER`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`DREHSTROMZAEHLER`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`ZWEIRICHTUNGSZAEHLER`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`RLM_ZAEHLER`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`IMS_ZAEHLER`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`BALGENGASZAEHLER`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`MAXIMUMZAEHLER`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`MULTIPLEXANLAGE`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`PAUSCHALANLAGE`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`VERSTAERKERANLAGE`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`SUMMATIONSGERAET`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`IMPULSGEBER`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`EDL_21_ZAEHLERAUFSATZ`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`VIER_QUADRANTEN_LASTGANGZAEHLER`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`MENGENUMWERTER`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`STROMWANDLER`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`SPANNUNGSWANDLER`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`DATENLOGGER`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`KOMMUNIKATIONSANSCHLUSS`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`MODEM`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`TELEKOMMUNIKATIONSEINRICHTUNG`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`KOMMUNIKATIONSEINRICHTUNG`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`DREHKOLBENGASZAEHLER`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`TURBINENRADGASZAEHLER`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`ULTRASCHALLZAEHLER`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`WIRBELGASZAEHLER`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`MODERNE_MESSEINRICHTUNG`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`ELEKTRONISCHER_HAUSHALTSZAEHLER`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`STEUEREINRICHTUNG`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`TECHNISCHESTEUEREINRICHTUNG`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`TARIFSCHALTGERAET`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`RUNDSTEUEREMPFAENGER`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`OPTIONALE_ZUS_ZAEHLEINRICHTUNG`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`MESSWANDLERSATZ_IMS_MME`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`KOMBIMESSWANDLER_IMS_MME`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`TARIFSCHALTGERAET_IMS_MME`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`RUNDSTEUEREMPFAENGER_IMS_MME`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`TEMPERATUR_KOMPENSATION`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`HOECHSTBELASTUNGS_ANZEIGER`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`SONSTIGES_GERAET`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`SMARTMETERGATEWAY`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`STEUERBOX`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`BLOCKSTROMWANDLER`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`KOMBIMESSWANDLER`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`MODEM_GSM`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`ETHERNET_KOM`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`PLC_COM`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`MODEM_FESTNETZ`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`DSL_KOM`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`LTE_KOM`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`DICHTEMENGENUMWERTER`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`TEMPERATURMENGENUMWERTER`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`ZUSTANDSMENGENUMWERTER`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`MESSDATENREGISTRIERGERAET`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`WANDLER`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`BEFESTIGUNGSEINRICHTUNG`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[weitereGeraetenummern](/bo4e/202610/com/Geraet#weiteregeraetenummern)</span><span className="hbs-nr">02490</span> | weitereGeraetenummern | array | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-g hbs-e3">**geraeteeigenschaften**</span> | — | object | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e4">[faktor](/bo4e/202610/com/Geraeteeigenschaften#faktor)</span><span className="hbs-nr">02500</span> | faktor | number (float) | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e4">[geraetemerkmal](/bo4e/202610/com/Geraeteeigenschaften#geraetemerkmal)</span><span className="hbs-nr">02510</span> | Geraetemerkmal | [Enum Geraetemerkmal](/bo4e/202610/enum/Geraetemerkmal) | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`EINTARIF`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`ZWEITARIF`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MEHRTARIF`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GAS_G2P5`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GAS_G4`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GAS_G6`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GAS_G10`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GAS_G16`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GAS_G25`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GAS_G40`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GAS_G65`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GAS_G100`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GAS_G160`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GAS_G250`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GAS_G350`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GAS_G400`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GAS_G4000`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GAS_G650`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GAS_G6500`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GAS_G1000`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GAS_G10000`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GAS_G12500`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GAS_G1600`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GAS_G16000`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`GAS_G2500`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`IMPULSGEBER_G4_G100`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`IMPULSGEBER_G100`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MODEM_GSM`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MODEM_GPRS`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MODEM_FUNK`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MODEM_GSM_O_LG`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MODEM_GSM_M_LG`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MODEM_FESTNETZ`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MODEM_GPRS_M_LG`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`PLC_COM`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`ETHERNET_KOM`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`DSL_KOM`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`LTE_KOM`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`RUNDSTEUEREMPFAENGER`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TARIFSCHALTGERAET`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`ZUSTANDS_MU`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TEMPERATUR_MU`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`KOMPAKT_MU`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SYSTEM_MU`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`UNBESTIMMT`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`WASSER_MWZW`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`WASSER_WZWW`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`WASSER_WZ01`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`WASSER_WZ02`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`WASSER_WZ03`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`WASSER_WZ04`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`WASSER_WZ05`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`WASSER_WZ06`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`WASSER_WZ07`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`WASSER_WZ08`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`WASSER_WZ09`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`WASSER_WZ10`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`WASSER_VWZ04`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`WASSER_VWZ05`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`WASSER_VWZ06`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`WASSER_VWZ07`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`WASSER_VWZ10`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`DICHTEMENGENUMWERTER`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`TEMPERATURMENGENUMWERTER`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`ZUSTANDSMENGENUMWERTER`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`BLOCKSTROMWANDLER`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`MESSWANDLERSATZ_IMS_MME`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`KOMBIMESSWANDLER`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e5">`SPANNUNGSWANDLER`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-g hbs-e2">**gueltigkeitszeitraum**</span> | — | object | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[zeitraumId](/bo4e/202610/com/Zeitraum#zeitraumid)</span><span className="hbs-nr">02520</span> | zeitraumId | integer | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-g hbs-e2">**zaehlwerke** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[bezeichnung](/bo4e/202610/com/Zaehlwerk#bezeichnung)</span><span className="hbs-nr">02530</span> | Zusätzliche Bezeichnung, z.B. Zählwerk_Wirkarbeit. | string | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[konfiguration](/bo4e/202610/com/Zaehlwerk#konfiguration)</span><span className="hbs-nr">02540</span> | Konfiguration (iMSys) des Zählwerks | string | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[nachkommastelle](/bo4e/202610/com/Zaehlwerk#nachkommastelle)</span><span className="hbs-nr">02550</span> | nachkommastelle | integer | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[obisKennzahl](/bo4e/202610/com/Zaehlwerk#obiskennzahl)</span><span className="hbs-nr">02560</span> | Die OBIS-Kennzahl für das Zählwerk, die festlegt, welche auf die gemessene Größe mit dem Stand gemeldet wird.<br/>Nur Zählwerkstände mit dieser OBIS-Kennzahl werden an diesem Zählwerk registriert. Beispiel:1-0:1.8.1 für<br/>elektrische Wirkarbeit. | string | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[vorkommastelle](/bo4e/202610/com/Zaehlwerk#vorkommastelle)</span><span className="hbs-nr">02570</span> | vorkommastelle | integer | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e3">[wertegranularitaet](/bo4e/202610/com/Zaehlwerk#wertegranularitaet)</span><span className="hbs-nr">02580</span> | Wertegranularitaet | [Enum Wertegranularitaet](/bo4e/202610/enum/Wertegranularitaet) | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`JAEHRLICH`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`HALBJAEHRLICH`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`QUARTALSWEISE`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e4">`MONATLICH`</span> | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-g hbs-e3">**zaehlzeiten**</span> | — | object | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e4">[register](/bo4e/202610/com/Zaehlzeitregister#register)</span><span className="hbs-nr">02590</span> | Zählzeitregister | string | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e4">[zaehlzeitDefinition](/bo4e/202610/com/Zaehlzeitregister#zaehlzeitdefinition)</span><span className="hbs-nr">02600</span> | Zählzeitdefinition | string | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e2">[tarifart](/bo4e/202610/bo/Zaehler#tarifart)</span><span className="hbs-nr">02610</span> | Spezifikation bezüglich unterstützter Tarifarten. | [Enum Tarifart](/bo4e/202610/enum/Tarifart) | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`EINTARIF`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`ZWEITARIF`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`MEHRTARIF`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`SMART_METER`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`LEISTUNGSGEMESSEN`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e2">[zaehlerauspraegung](/bo4e/202610/bo/Zaehler#zaehlerauspraegung)</span><span className="hbs-nr">02620</span> | Spezifikation die Richtung des Zählers betreffend. | [Enum Zaehlerauspraegung](/bo4e/202610/enum/Zaehlerauspraegung) | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`EINRICHTUNGSZAEHLER`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`ZWEIRICHTUNGSZAEHLER`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e2">[zaehlertyp](/bo4e/202610/bo/Zaehler#zaehlertyp)</span><span className="hbs-nr">02630</span> | Typisierung des Zählers | [Enum Zaehlertyp](/bo4e/202610/enum/Zaehlertyp) | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`DREHSTROMZAEHLER`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`BALGENGASZAEHLER`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`DREHKOLBENZAEHLER`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`SMARTMETER`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`LEISTUNGSZAEHLER`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`MAXIMUMZAEHLER`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`TURBINENRADGASZAEHLER`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`ULTRASCHALLGASZAEHLER`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`WECHSELSTROMZAEHLER`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`WIRBELGASZAEHLER`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`MESSDATENREGISTRIERGERAET`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`ELEKTRONISCHERHAUSHALTSZAEHLER`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`SONDERAUSSTATTUNG`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`WASSERZAEHLER`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`MODERNEMESSEINRICHTUNG`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-f hbs-e2">[zaehlertypspezifikation](/bo4e/202610/bo/Zaehler#zaehlertypspezifikation)</span><span className="hbs-nr">02640</span> | Typisierung des Zählers (spezifikation für EHZ und MME) | [Enum ZaehlertypSpezifikation](/bo4e/202610/enum/ZaehlertypSpezifikation) | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`EDL40`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`EDL21`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`SONSTIGER_EHZ`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`MME_STANDARD`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-w hbs-e3">`MME_MEDA`</span> | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — |
| <span className="hbs-g hbs-e1">**TRANCHE** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | — | — | — | — | — | — | — | — | — | Muss | — | — | — | — | Muss | — | Kann | — | — |
| <span className="hbs-f hbs-e2">[datenqualitaet](/bo4e/202610/bo/Tranche#datenqualitaet)</span><span className="hbs-nr">02650</span> | Datenqualitaet | [Enum Datenqualitaet](/bo4e/202610/enum/Datenqualitaet) | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`ERWARTETE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`INFORMATIVE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`GUELTIGE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_KEINE_DATEN_VORHANDEN`</span> | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN_ERWARTET`</span> | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_ERWARTETE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | Kann | — | — |
| <span className="hbs-f hbs-e2">[tranchenId](/bo4e/202610/bo/Tranche#tranchenid) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">02660</span> | tranchenId | string | — | — | — | — | — | — | — | — | — | Muss | — | — | — | — | Muss | — | Kann | — | — |
| <span className="hbs-f hbs-e2">[verguetungEmpfaenger](/bo4e/202610/bo/Tranche#verguetungempfaenger)</span><span className="hbs-nr">02670</span> | VerguetungEmpfaenger | [Enum VerguetungEmpfaenger](/bo4e/202610/enum/VerguetungEmpfaenger) | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`KUNDE`</span> | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — |
| <span className="hbs-w hbs-e3">`LIEFERANT`</span> | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**gueltigkeitszeitraum**</span> | — | object | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | Kann | — | — |
| <span className="hbs-f hbs-e3">[zeitraumId](/bo4e/202610/com/Zeitraum#zeitraumid)</span><span className="hbs-nr">02680</span> | zeitraumId | integer | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | Kann | — | Kann | — | — |
| <span className="hbs-g hbs-e2">**zaehlwerke** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-f hbs-e3">[obisKennzahl](/bo4e/202610/com/Zaehlwerk#obiskennzahl)</span><span className="hbs-nr">02690</span> | Die OBIS-Kennzahl für das Zählwerk, die festlegt, welche auf die gemessene Größe mit dem Stand gemeldet wird.<br/>Nur Zählwerkstände mit dieser OBIS-Kennzahl werden an diesem Zählwerk registriert. Beispiel:1-0:1.8.1 für<br/>elektrische Wirkarbeit. | string | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-f hbs-e3">[verwendungszweckLF](/bo4e/202610/com/Zaehlwerk#verwendungszwecklf)</span><span className="hbs-nr">02700</span> | Codes gemäß Codeliste der Verwendungszwecke Verwendungszweck LF | string | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-f hbs-e3">[verwendungszweckNB](/bo4e/202610/com/Zaehlwerk#verwendungszwecknb)</span><span className="hbs-nr">02710</span> | Codes gemäß Codeliste der Verwendungszwecke Verwendungszweck NB | string | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-f hbs-e3">[verwendungszweckUENB](/bo4e/202610/com/Zaehlwerk#verwendungszweckuenb)</span><span className="hbs-nr">02720</span> | Codes gemäß Codeliste der Verwendungszwecke Verwendungszweck ÜNB | string | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — |
| <span className="hbs-f hbs-e2">[bilanzkreis](/bo4e/202610/bo/Tranche#bilanzkreis)</span><span className="hbs-nr">02730</span> | bilanzkreis | string | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — |
| <span className="hbs-g hbs-e1">**MESSSTELLENBETRIEBSVERTRAG** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | — | — | — | — | — | — | — | — | — | Kann | — | Kann | — | — | — | — | — | — |
| <span className="hbs-g hbs-e2">**vertragskonditionen**</span> | — | object | — | — | — | — | — | — | — | — | — | — | Kann | — | Kann | — | — | — | — | — | — |
| <span className="hbs-f hbs-e3">[abrechnungUeberNna](/bo4e/202610/com/Vertragskonditionen#abrechnunguebernna)</span><span className="hbs-nr">02740</span> | abrechnungUeberNna | boolean | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — | — | — |
| <span className="hbs-g hbs-e3">**geplanteTurnusablesung**</span> | — | object | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — |
| <span className="hbs-f hbs-e4">[ableseZeitraum](/bo4e/202610/com/Zeitraum#ablesezeitraum)</span><span className="hbs-nr">02750</span> | ableseZeitraum | string | — | — | — | — | — | — | — | — | — | — | — | — | Kann | — | — | — | — | — | — |

</div>

</Handbuchsatz>

## Kette dieses Auslösers

Das Ereignis löst die Nachricht aus.

| Nachricht | Antworten | Schreibaufruf nach der Antwort |
|---|---|---|
| [55156](/schnittstellen/202610/pruefi/UTILMD/PI_55156) | — | — |
| [55180](/schnittstellen/202610/pruefi/UTILMD/PI_55180) | — | — |
| [55220](/schnittstellen/202610/pruefi/UTILMD/PI_55220) | — | — |
| [55227](/schnittstellen/202610/pruefi/UTILMD/PI_55227) | — | — |
| [55555](/schnittstellen/202610/pruefi/UTILMD/PI_55555) | — | — |
| [55621](/schnittstellen/202610/pruefi/UTILMD/PI_55621) | — | — |
| [55622](/schnittstellen/202610/pruefi/UTILMD/PI_55622) | — | — |
| [55623](/schnittstellen/202610/pruefi/UTILMD/PI_55623) | — | — |
| [55624](/schnittstellen/202610/pruefi/UTILMD/PI_55624) | — | — |
| [55625](/schnittstellen/202610/pruefi/UTILMD/PI_55625) | — | — |
| [55626](/schnittstellen/202610/pruefi/UTILMD/PI_55626) | — | — |
| [55654](/schnittstellen/202610/pruefi/UTILMD/PI_55654) | — | — |
| [55655](/schnittstellen/202610/pruefi/UTILMD/PI_55655) | — | — |
| [55656](/schnittstellen/202610/pruefi/UTILMD/PI_55656) | — | — |
| [55657](/schnittstellen/202610/pruefi/UTILMD/PI_55657) | — | — |
| [55658](/schnittstellen/202610/pruefi/UTILMD/PI_55658) | — | — |
| [55673](/schnittstellen/202610/pruefi/UTILMD/PI_55673) | — | — |
| [55692](/schnittstellen/202610/pruefi/UTILMD/PI_55692) | — | — |

Dieses Ereignis löst Schritte in diesen Rollensichten aus:

| Prozess | Beteiligter | Regelwerk | Sparte |
|---|---|---|---|
| [Abrechnungsdaten Bilanzkreisabrechnung](/prozessdoku/202610/LF/GPKE-Teil2-abrechnungsdaten-bilanzkreisabrechnung) | LF | GPKE Teil 2 | Strom |
| [Abrechnungsdaten Netznutzungsabrechnung](/prozessdoku/202610/LF/GPKE-Teil2-abrechnungsdaten-netznutzungsabrechnung) | LF | GPKE Teil 2 | Strom |
| [Bestellung einer Änderung von Abrechnungsdaten von LF an NB](/prozessdoku/202610/LF/GPKE-Teil2-bestellung-einer-aenderung-von-abrechnungsdaten-von-lf-an-nb) | LF | GPKE Teil 2 | Strom |
| [Bestellung zur Stammdatenänderung an MSB (verantwortlich)](/prozessdoku/202610/LF/GPKE-Teil4-bestellung-zur-stammdatenaenderung-an-msb-verantwortlich) | LF | GPKE Teil 4 | Strom |
| [Bestellung zur Stammdatenänderung an NB (verantwortlich)](/prozessdoku/202610/LF/GPKE-Teil4-bestellung-zur-stammdatenaenderung-an-nb-verantwortlich) | LF | GPKE Teil 4 | Strom |
| [Stammdatenänderung vom MSB (verantwortlich) ausgehend](/prozessdoku/202610/LF/GPKE-Teil4-stammdatenaenderung-vom-msb-verantwortlich-ausgehend) | LF | GPKE Teil 4 | Strom |
| [Stammdatenänderung vom NB (verantwortlich) ausgehend](/prozessdoku/202610/LF/GPKE-Teil4-stammdatenaenderung-vom-nb-verantwortlich-ausgehend) | LF | GPKE Teil 4 | Strom |

## Transaktionsdaten

Der Umschlag der Nachricht. Pflichtfelder müssen beim Trigger-Aufruf gesetzt sein.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| [kategorie](/bo4e/202610/cdoc/Transaktionsdaten#kategorie) | string | **ja** | Qualifier aus dem Beginn der EDIFact Nachricht / BGM |
| [sparte](/bo4e/202610/cdoc/Transaktionsdaten#sparte) | [Enum Sparte](/bo4e/202610/enum/Sparte) | **ja** | Enthält Informationen über die Sparte Werte: `STROM`, `GAS`, `FERNWAERME`, `NAHWAERME`, `WASSER`, `ABWASSER` |
| [transaktionsgrund](/bo4e/202610/cdoc/Transaktionsdaten#transaktionsgrund) | string | **ja** | Der Transaktionsgrund beschreibt den Geschäftsvorfall zur Kategorie genauer / UTILMD STS+7++###+ZW4+E03 |
| [transaktionsgrundergaenzung](/bo4e/202610/cdoc/Transaktionsdaten#transaktionsgrundergaenzung) | string | **ja** | Ergänzung zum Transaktionsgrund / UTILMD STS+7++E01+###+E03 |
| [vertragsbeginn](/bo4e/202610/cdoc/Transaktionsdaten#vertragsbeginn) | string (date-time) | **ja** | Datum Vertragsbeginn / DTM+92 |
| `pruefidentifikator` | — | nein | Wird dynamisch im Event-Prozess ermittelt (Entscheidungsgrundlage: marktrolle, transaktionsgrund). Ein vom Sender mitgegebener Wert wird ignoriert. Im Topic mögliche Prüfis — 55156, 55180, 55220, 55227, 55555, 55621, 55622, 55623, 55624, 55625, 55626, 55654, 55655, 55656, 55657, 55658, 55673, 55692. Mögliche Werte: `55156`, `55180`, `55220`, `55227`, `55555`, `55621`, `55622`, `55623`, `55624`, `55625`, `55626`, `55654`, `55655`, `55656`, `55657`, `55658`, `55673`, `55692` |
| [absender › rollencodenummer](/bo4e/202610/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |
| [empfaenger › marktrolle](/bo4e/202610/bo/Marktteilnehmer#marktrolle) | [Enum Marktrolle](/bo4e/202610/enum/Marktrolle) | nein | Gibt im Klartext die Bezeichnung der Marktrolle an. Werte: `NB`, `LF`, `MSB`, `MSBA`, `GMSB`, `MDL`, `DL`, `BKV`, `UENB`, `KUNDE-SELBST-NN` … (+9) |
| [empfaenger › rollencodenummer](/bo4e/202610/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |

## Zusatzdaten

`eventname` ist auf **START_BESTELLUNG_SDAE** festgelegt. Dieser Wert bleibt auch in der englischen Fassung deutsch, weil Camunda darüber korreliert.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `prozessId` | string | **ja** | — |
| `eventname` | const `START_BESTELLUNG_SDAE` | **ja** | — |

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
