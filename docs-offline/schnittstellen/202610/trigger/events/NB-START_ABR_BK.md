# [NB] START_ABR_BK
<span hidden data-pagefind-meta={"title:Trigger-Ereignis START_ABR_BK — Marktrolle NB (FV 202610)"} />

Marktrolle **NB** · Formatversion **202610** · BO4E-Schema **1.7.8**

## Stammdaten

Unter diesem Topic ist genau einer der folgenden 4 Prüfidentifikatoren zulässig — welcher, entscheidet der Event-Prozess.

| Prüfi | Scope | Anwendungsfall | Festlegung | Kommunikation |
|---|---|---|---|---|
| [PI_55126](/schnittstellen/202610/pruefi/UTILMD/PI_55126) | UTILMD | Abr.-Daten BK-Abr. verb. MaLo | GPKE Teil 2 | NB → LF |
| [PI_55613](/schnittstellen/202610/pruefi/UTILMD/PI_55613) | UTILMD | Abr.-Daten BK-Abr. verb. MaLo | GPKE Teil 2 | NB → ÜNB |
| [PI_55672](/schnittstellen/202610/pruefi/UTILMD/PI_55672) | UTILMD | Abr.-Daten BK-Abr. erz. Malo | GPKE Teil 2 | NB → LF |
| [PI_55674](/schnittstellen/202610/pruefi/UTILMD/PI_55674) | UTILMD | Abr.-Daten BK-Abr. erz. Malo | GPKE Teil 2 | NB → ÜNB |

Die Stammdaten der 8 Prüfidentifikatoren in **einer** Struktur — eine Spalte je Prüfidentifikator, wie im Anwendungshandbuch. Ein Wert in der Spalte heißt, dass das Feld zu diesem Prüfidentifikator gehört: **Muss**, wenn seine Spezifikation es verlangt, sonst **Kann**. Eine leere Zelle heißt »gehört nicht dazu«, nicht »unbekannt«. Vorausgewählt ist der erste; die übrigen schaltet die Leiste über der Tabelle zu.

<Handbuchsatz>

<div className="maco-tabellenrahmen">

| Struktur (BO4E) | Beschreibung | Format | <span className="hbs-p" title="Abr.-Daten BK-Abr. verb. MaLo">55126</span> | <span className="hbs-p" title="Abr.-Daten BK-Abr. verb. MaLo">55613</span> | <span className="hbs-p" title="Abr.-Daten BK-Abr. erz. Malo">55672</span> | <span className="hbs-p" title="Abr.-Daten BK-Abr. erz. Malo">55674</span> | Bedingung |
|---|---|---|---|---|---|---|---|
| <span className="hbs-g hbs-e0">**stammdaten**</span> | — | object | Kann | Kann | Kann | Kann | — |
| <span className="hbs-g hbs-e1">**BILANZIERUNG** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | Kann | Kann | Kann | — |
| <span className="hbs-f hbs-e2">[aggregationsverantwortung](/bo4e/202610/bo/Bilanzierung#aggregationsverantwortung)</span><span className="hbs-nr">00010</span> | Aggregationsverantwortung | [Enum Aggregationsverantwortung](/bo4e/202610/enum/Aggregationsverantwortung) | Kann | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`UENB`</span> | — | — | Kann | — | Kann | — | — |
| <span className="hbs-w hbs-e3">`VNB`</span> | — | — | Kann | — | Kann | — | — |
| <span className="hbs-f hbs-e2">[bilanzkreis](/bo4e/202610/bo/Bilanzierung#bilanzkreis)</span><span className="hbs-nr">00020</span> | Bilanzkreis | string | Kann | Kann | Kann | Kann | — |
| <span className="hbs-f hbs-e2">[datenqualitaet](/bo4e/202610/bo/Bilanzierung#datenqualitaet)</span><span className="hbs-nr">00030</span> | Datenqualität | [Enum Datenqualitaet](/bo4e/202610/enum/Datenqualitaet) | Kann | Kann | Kann | — | — |
| <span className="hbs-w hbs-e3">`ERWARTETE_DATEN`</span> | — | — | Kann | Kann | Kann | — | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | Kann | Kann | Kann | — | — |
| <span className="hbs-w hbs-e3">`INFORMATIVE_DATEN`</span> | — | — | Kann | Kann | Kann | — | — |
| <span className="hbs-w hbs-e3">`GUELTIGE_DATEN`</span> | — | — | Kann | Kann | Kann | — | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN`</span> | — | — | Kann | Kann | Kann | — | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_KEINE_DATEN_VORHANDEN`</span> | — | — | Kann | Kann | Kann | — | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN_ERWARTET`</span> | — | — | Kann | Kann | Kann | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_DATEN`</span> | — | — | Kann | Kann | Kann | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_ERWARTETE_DATEN`</span> | — | — | Kann | Kann | Kann | — | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | Kann | Kann | Kann | — | — |
| <span className="hbs-f hbs-e2">[detailsPrognosegrundlage](/bo4e/202610/bo/Bilanzierung#detailsprognosegrundlage)</span><span className="hbs-nr">00040</span> | Prognosegrundlage - Besteht der Bedarf ein tagesparameteräbhängiges Lastprofil mit gemeinsamer Messung anzugeben, so ist dies über die 2 -malige Wiederholung des CAV Segments mit der Angabe der Codes E02 und E14 möglich. | array | Kann | Kann | Kann | — | — |
| <span className="hbs-f hbs-e2">[prognosegrundlage](/bo4e/202610/bo/Bilanzierung#prognosegrundlage)</span><span className="hbs-nr">00050</span> | Prognosegrundlage | [Enum Prognosegrundlage](/bo4e/202610/enum/Prognosegrundlage) | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`WERTE`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`PROFILE`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-f hbs-e2">[zeitreihentyp](/bo4e/202610/bo/Bilanzierung#zeitreihentyp)</span><span className="hbs-nr">00060</span> | Zeitreihentyp | [Enum Zeitreihentyp](/bo4e/202610/enum/Zeitreihentyp) | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`EGS`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`LGS`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`NZR`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`SES`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`SLS`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`TES`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`TLS`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`SLS_TLS`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`SES_TES`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`AUS`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`BAS`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`DBA`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`DZR`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`DZÜ`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`FPE`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`FPI`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`SRE`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`SRI`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`VZR`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`BIL`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`BIP`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`BIT`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`GAL`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`GAP`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`GAT`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`GEL`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`GEP`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`GET`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`SOL`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`SOP`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`SOT`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`WFL`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`WFP`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`WNL`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`WNP`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`WNT`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`WAL`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`WAP`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`WAT`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`AU1`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`BI1`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`BI2`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`BI3`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`GAA`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`GAB`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`GAC`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`GE1`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`GE2`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`GE3`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`SO1`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`SO2`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`SO3`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`WF1`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`WF2`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`WF3`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`WN1`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`WN2`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`WN3`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`WAA`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`WAB`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`WAC`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`AUSFALLARBEITSSUMME`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`BILANZKREISABWEICHUNGSSALDO`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`DIFFERENZZEITREIHE`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`DELTAZEITREIHE`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`DELTAZEITREIHENUEBERTRAG`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`FAHRPLANENTNAHMESUMME`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`FAHRPLANEINSPEISESUMME`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`UEBERFUEHRUNGSZEITREIHE_SEKUNDAERREGELLEISTUNG_EXPORT`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`UEBERFUEHRUNGSZEITREIHE_SEKUNDAERREGELLEISTUNG_IMPORT`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`VERLUSTZEITREIHE`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_BIOMASSE_BIOGAS_GEMESSEN`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_BIOMASSE_BIOGAS_EINSPEISEPROFIL`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_BIOMASSE_BIOGAS_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_DEPONIE_KLAER_GRUBENGAS_GEMESSEN`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_DEPONIE_KLAER_GRUBENGAS_EINSPEISEPROFIL`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_DEPONIE_KLAER_GRUBENGAS_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_GEOTHERMIE_GEMESSEN`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_GEOTHERMIE_EINSPEISEPROFIL`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_GEOTHERMIE_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_SOLAR_GEMESSEN`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_SOLAR_EINSPEISEPROFIL`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_SOLAR_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_WIND_OFFSHORE_GEMESSEN`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_WIND_OFFSHORE_EINSPEISEPROFIL`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_WIND_OFFSHORE_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_WIND_ONSHORE_GEMESSEN`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_WIND_ONSHORE_EINSPEISEPROFIL`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_WIND_ONSHORE_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_WASSERKRAFT_GEMESSEN`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_WASSERKRAFT_EINSPEISEPROFIL`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_WASSERKRAFT_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_AUSFALLARBEIT`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_BIOMASSE_BIOGAS_WERTE`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_BIOMASSE_BIOGAS_STANDARDEINSPEISEPROFIL`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_BIOMASSE_BIOGAS_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_DEPONIE_KLAER_GRUBENGAS_WERTE`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_DEPONIE_KLAER_GRUBENGAS_STANDARDEINSPEISEPROFIL`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_DEPONIE_KLAER_GRUBENGAS_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_GEOTHERMIE_WERTE`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_GEOTHERMIE_STANDARDEINSPEISEPROFIL`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_GEOTHERMIE_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_SOLAR_WERTE`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_SOLAR_STANDARDEINSPEISEPROFIL`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_SOLAR_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_WIND_OFFSHORE_WERTE`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_WIND_OFFSHORE_STANDARDEINSPEISEPROFIL`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_WIND_OFFSHORE_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_WIND_ONSHORE_WERTE`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_WIND_ONSHORE_STANDARDEINSPEISEPROFIL`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_WIND_ONSHORE_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_WASSERKRAFT_WERTE`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_WASSERKRAFT_STANDARDEINSPEISEPROFIL`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_WASSERKRAFT_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-g hbs-e2">**gueltigkeitszeitraum**</span> | — | object | Kann | Kann | Kann | — | — |
| <span className="hbs-f hbs-e3">[zeitraumId](/bo4e/202610/com/Zeitraum#zeitraumid)</span><span className="hbs-nr">00070</span> | zeitraumId | integer | Kann | Kann | Kann | — | — |
| <span className="hbs-g hbs-e2">**jahresverbrauchsprognose**</span> | — | object | Kann | Kann | Kann | — | — |
| <span className="hbs-f hbs-e3">[einheit](/bo4e/202610/com/Menge#einheit)</span><span className="hbs-nr">00080</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202610/enum/Mengeneinheit) | Kann | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`W`</span> | — | — | Kann | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`WH`</span> | — | — | Kann | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`KW`</span> | — | — | Kann | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`KWH`</span> | — | — | Kann | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`KVARH`</span> | — | — | Kann | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`MW`</span> | — | — | Kann | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`MWH`</span> | — | — | Kann | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`STUECK`</span> | — | — | Kann | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`KUBIKMETER`</span> | — | — | Kann | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`STUNDE`</span> | — | — | Kann | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`TAG`</span> | — | — | Kann | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`MONAT`</span> | — | — | Kann | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`JAHR`</span> | — | — | Kann | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`PROZENT`</span> | — | — | Kann | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`ANZAHL`</span> | — | — | Kann | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`VAR`</span> | — | — | Kann | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`KVAR`</span> | — | — | Kann | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`VARH`</span> | — | — | Kann | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`KWHK`</span> | — | — | Kann | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`Z16`</span> | — | — | Kann | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`KWT`</span> | — | — | Kann | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`WATT_PRO_QUADRATMETER`</span> | — | — | Kann | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`METER_PRO_SEKUNDE`</span> | — | — | Kann | Kann | Kann | — | — |
| <span className="hbs-f hbs-e3">[wert](/bo4e/202610/com/Menge#wert)</span><span className="hbs-nr">00090</span> | Wert | number (float) | Kann | Kann | Kann | — | — |
| <span className="hbs-g hbs-e2">**lastprofile** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | Kann | Kann | — | — |
| <span className="hbs-f hbs-e3">[bezeichnung](/bo4e/202610/com/Lastprofil#bezeichnung)</span><span className="hbs-nr">00100</span> | Bezeichnung des Profils | string | Kann | Kann | Kann | — | — |
| <span className="hbs-f hbs-e3">[einspeisung](/bo4e/202610/com/Lastprofil#einspeisung)</span><span className="hbs-nr">00110</span> | Kennzeichen Einspeisung | boolean | Kann | Kann | Kann | — | — |
| <span className="hbs-f hbs-e3">[profilart](/bo4e/202610/com/Lastprofil#profilart)</span><span className="hbs-nr">00120</span> | Profilart | [Enum Profilart](/bo4e/202610/enum/Profilart) | Kann | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`ART_STANDARDLASTPROFIL`</span> | — | — | Kann | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`ART_TAGESPARAMETERABHAENGIGES_LASTPROFIL`</span> | — | — | Kann | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`ART_LASTPROFIL`</span> | — | — | Kann | Kann | Kann | — | — |
| <span className="hbs-f hbs-e3">[profilschar](/bo4e/202610/com/Lastprofil#profilschar)</span><span className="hbs-nr">00130</span> | Profilschar des Profils | string | Kann | — | Kann | — | — |
| <span className="hbs-f hbs-e3">[verfahren](/bo4e/202610/com/Lastprofil#verfahren)</span><span className="hbs-nr">00140</span> | Profilverfahren | [Enum Profilverfahren](/bo4e/202610/enum/Profilverfahren) | Kann | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`SYNTHETISCH`</span> | — | — | Kann | Kann | Kann | — | — |
| <span className="hbs-w hbs-e4">`ANALYTISCH`</span> | — | — | Kann | Kann | Kann | — | — |
| <span className="hbs-g hbs-e3">**tagesparameter**</span> | — | object | Kann | — | Kann | — | — |
| <span className="hbs-f hbs-e4">[dienstanbieter](/bo4e/202610/com/Tagesparameter#dienstanbieter)</span><span className="hbs-nr">00150</span> | dienstanbieter | string | Kann | — | Kann | — | — |
| <span className="hbs-f hbs-e4">[herausgeber](/bo4e/202610/com/Tagesparameter#herausgeber)</span><span className="hbs-nr">00160</span> | Herausgeber | [Enum Herausgeber](/bo4e/202610/enum/Herausgeber) | Kann | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`NB`</span> | — | — | Kann | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`BDEW`</span> | — | — | Kann | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`TUM`</span> | — | — | Kann | — | Kann | — | — |
| <span className="hbs-f hbs-e4">[klimazone](/bo4e/202610/com/Tagesparameter#klimazone)</span><span className="hbs-nr">00170</span> | klimazone | string | Kann | — | Kann | — | — |
| <span className="hbs-f hbs-e4">[temperaturmessstelle](/bo4e/202610/com/Tagesparameter#temperaturmessstelle)</span><span className="hbs-nr">00180</span> | temperaturmessstelle | string | Kann | — | Kann | — | — |
| <span className="hbs-f hbs-e3">[referenzprofilbezeichnung](/bo4e/202610/com/Lastprofil#referenzprofilbezeichnung)</span><span className="hbs-nr">00190</span> | Bezeichnung des Referenzprofils | string | — | — | Kann | — | — |
| <span className="hbs-g hbs-e2">**temperaturarbeit**</span> | — | object | Kann | — | Kann | — | — |
| <span className="hbs-f hbs-e3">[einheit](/bo4e/202610/com/Menge#einheit)</span><span className="hbs-nr">00200</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202610/enum/Mengeneinheit) | Kann | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`W`</span> | — | — | Kann | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`WH`</span> | — | — | Kann | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`KW`</span> | — | — | Kann | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`KWH`</span> | — | — | Kann | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`KVARH`</span> | — | — | Kann | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`MW`</span> | — | — | Kann | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`MWH`</span> | — | — | Kann | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`STUECK`</span> | — | — | Kann | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`KUBIKMETER`</span> | — | — | Kann | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`STUNDE`</span> | — | — | Kann | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`TAG`</span> | — | — | Kann | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`MONAT`</span> | — | — | Kann | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`JAHR`</span> | — | — | Kann | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`PROZENT`</span> | — | — | Kann | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`ANZAHL`</span> | — | — | Kann | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`VAR`</span> | — | — | Kann | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`KVAR`</span> | — | — | Kann | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`VARH`</span> | — | — | Kann | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`KWHK`</span> | — | — | Kann | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`Z16`</span> | — | — | Kann | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`KWT`</span> | — | — | Kann | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`WATT_PRO_QUADRATMETER`</span> | — | — | Kann | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`METER_PRO_SEKUNDE`</span> | — | — | Kann | — | Kann | — | — |
| <span className="hbs-f hbs-e3">[wert](/bo4e/202610/com/Menge#wert)</span><span className="hbs-nr">00210</span> | Wert | number (float) | Kann | — | Kann | — | — |
| <span className="hbs-g hbs-e1">**MARKTLOKATION** <span className="hbs-liste">[ ]</span></span> | — | object[] | Muss | Muss | Muss | Muss | — |
| <span className="hbs-f hbs-e2">[bilanzierungsgebiet](/bo4e/202610/bo/Marktlokation#bilanzierungsgebiet)</span><span className="hbs-nr">00220</span> | Bilanzierungsgebiet, dem das Netzgebiet zugeordnet ist - im Falle eines Strom Netzes. | string | Kann | Kann | Kann | Kann | — |
| <span className="hbs-f hbs-e2">[datenqualitaet](/bo4e/202610/bo/Marktlokation#datenqualitaet)</span><span className="hbs-nr">00230</span> | Datenqualitaet | [Enum Datenqualitaet](/bo4e/202610/enum/Datenqualitaet) | Kann | Muss | Kann | Muss | — |
| <span className="hbs-w hbs-e3">`ERWARTETE_DATEN`</span> | — | — | Kann | Muss | Kann | Muss | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | Kann | Muss | Kann | Muss | — |
| <span className="hbs-w hbs-e3">`INFORMATIVE_DATEN`</span> | — | — | Kann | Muss | Kann | Muss | — |
| <span className="hbs-w hbs-e3">`GUELTIGE_DATEN`</span> | — | — | Kann | Muss | Kann | Muss | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN`</span> | — | — | Kann | Muss | Kann | Muss | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_KEINE_DATEN_VORHANDEN`</span> | — | — | Kann | Muss | Kann | Muss | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN_ERWARTET`</span> | — | — | Kann | Muss | Kann | Muss | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_DATEN`</span> | — | — | Kann | Muss | Kann | Muss | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_ERWARTETE_DATEN`</span> | — | — | Kann | Muss | Kann | Muss | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | Kann | Muss | Kann | Muss | — |
| <span className="hbs-f hbs-e2">[marktlokationsId](/bo4e/202610/bo/Marktlokation#marktlokationsid)</span><span className="hbs-nr">00240</span> | Identifikationsnummer einer Marktlokation, an der Energie entweder<br/>verbraucht, oder erzeugt wird | string | Kann | Kann | Kann | Kann | — |
| <span className="hbs-f hbs-e2">[regelzone](/bo4e/202610/bo/Marktlokation#regelzone)</span><span className="hbs-nr">00250</span> | für EDIFACT mapping | string | Kann | — | Kann | — | — |
| <span className="hbs-g hbs-e2">**gueltigkeitszeitraum**</span> | — | object | Kann | Kann | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[zeitraumId](/bo4e/202610/com/Zeitraum#zeitraumid)</span><span className="hbs-nr">00260</span> | zeitraumId | integer | Kann | Kann | Kann | Kann | — |
| <span className="hbs-g hbs-e2">**marktrollen** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | Kann | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[marktrolle](/bo4e/202610/bo/Marktteilnehmer#marktrolle)</span><span className="hbs-nr">00270</span> | Gibt im Klartext die Bezeichnung der Marktrolle an. | [Enum Marktrolle](/bo4e/202610/enum/Marktrolle) | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`NB`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`LF`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`MSB`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`MSBA`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`GMSB`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`MDL`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`DL`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`BKV`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`UENB`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`KUNDE-SELBST-NN`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`MGV`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`EIV`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`RB`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`KUNDE`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`INTERESSENT`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`KN`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`UBA`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`BIKO`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-w hbs-e4">`ESA`</span> | — | — | Kann | Kann | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[rollencodenummer](/bo4e/202610/bo/Marktteilnehmer#rollencodenummer)</span><span className="hbs-nr">00280</span> | Gibt die Codenummer der Marktrolle an. | string | Kann | Kann | Kann | Kann | — |
| <span className="hbs-f hbs-e2">[energierichtung](/bo4e/202610/bo/Marktlokation#energierichtung) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00290</span> | Kennzeichnung, ob Energie eingespeist oder entnommen (ausgespeist) wird. | [Enum Energierichtung](/bo4e/202610/enum/Energierichtung) | Muss | Muss | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`AUSSP`</span> | — | — | Muss | Muss | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`EINSP`</span> | — | — | Muss | Muss | Muss | Muss | — |
| <span className="hbs-f hbs-e2">[netzebene](/bo4e/202610/bo/Marktlokation#netzebene)</span><span className="hbs-nr">00300</span> | Netzebene, in der der Bezug der Energie erfolgt. Bei Strom Spannungsebene der<br/>Lieferung, bei Gas Druckstufe. Beispiel Strom: Niederspannung Beispiel Gas:<br/>Niederdruck. | [Enum Netzebene](/bo4e/202610/enum/Netzebene) | — | Kann | — | Kann | — |
| <span className="hbs-w hbs-e3">`NSP`</span> | — | — | — | Kann | — | Kann | — |
| <span className="hbs-w hbs-e3">`MSP`</span> | — | — | — | Kann | — | Kann | — |
| <span className="hbs-w hbs-e3">`HSP`</span> | — | — | — | Kann | — | Kann | — |
| <span className="hbs-w hbs-e3">`HSS`</span> | — | — | — | Kann | — | Kann | — |
| <span className="hbs-w hbs-e3">`MSP_NSP_UMSP`</span> | — | — | — | Kann | — | Kann | — |
| <span className="hbs-w hbs-e3">`HSP_MSP_UMSP`</span> | — | — | — | Kann | — | Kann | — |
| <span className="hbs-w hbs-e3">`HSS_HSP_UMSP`</span> | — | — | — | Kann | — | Kann | — |
| <span className="hbs-w hbs-e3">`HD`</span> | — | — | — | Kann | — | Kann | — |
| <span className="hbs-w hbs-e3">`MD`</span> | — | — | — | Kann | — | Kann | — |
| <span className="hbs-w hbs-e3">`ND`</span> | — | — | — | Kann | — | Kann | — |
| <span className="hbs-f hbs-e2">[umspannung](/bo4e/202610/bo/Marktlokation#umspannung)</span><span className="hbs-nr">00310</span> | Netzebene | [Enum Netzebene](/bo4e/202610/enum/Netzebene) | — | Kann | — | Kann | — |
| <span className="hbs-w hbs-e3">`NSP`</span> | — | — | — | Kann | — | Kann | — |
| <span className="hbs-w hbs-e3">`MSP`</span> | — | — | — | Kann | — | Kann | — |
| <span className="hbs-w hbs-e3">`HSP`</span> | — | — | — | Kann | — | Kann | — |
| <span className="hbs-w hbs-e3">`HSS`</span> | — | — | — | Kann | — | Kann | — |
| <span className="hbs-w hbs-e3">`MSP_NSP_UMSP`</span> | — | — | — | Kann | — | Kann | — |
| <span className="hbs-w hbs-e3">`HSP_MSP_UMSP`</span> | — | — | — | Kann | — | Kann | — |
| <span className="hbs-w hbs-e3">`HSS_HSP_UMSP`</span> | — | — | — | Kann | — | Kann | — |
| <span className="hbs-w hbs-e3">`HD`</span> | — | — | — | Kann | — | Kann | — |
| <span className="hbs-w hbs-e3">`MD`</span> | — | — | — | Kann | — | Kann | — |
| <span className="hbs-w hbs-e3">`ND`</span> | — | — | — | Kann | — | Kann | — |
| <span className="hbs-g hbs-e1">**VERWENDUNGSZEITRAUM** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | Muss | Muss | Muss | — |
| <span className="hbs-f hbs-e2">[datenqualitaet](/bo4e/202610/bo/Verwendungszeitraum#datenqualitaet) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00320</span> | Datenqualitaet | [Enum Datenqualitaet](/bo4e/202610/enum/Datenqualitaet) | Muss | Muss | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`ERWARTETE_DATEN`</span> | — | — | Muss | Muss | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | Muss | Muss | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`INFORMATIVE_DATEN`</span> | — | — | Muss | Muss | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`GUELTIGE_DATEN`</span> | — | — | Muss | Muss | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN`</span> | — | — | Muss | Muss | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_KEINE_DATEN_VORHANDEN`</span> | — | — | Muss | Muss | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN_ERWARTET`</span> | — | — | Muss | Muss | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_DATEN`</span> | — | — | Muss | Muss | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_ERWARTETE_DATEN`</span> | — | — | Muss | Muss | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | Muss | Muss | Muss | Muss | — |
| <span className="hbs-f hbs-e2">[verwendungAb](/bo4e/202610/bo/Verwendungszeitraum#verwendungab) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00330</span> | verwendungAb | string (date-time) | Muss | Muss | Muss | Muss | — |
| <span className="hbs-f hbs-e2">[verwendungBis](/bo4e/202610/bo/Verwendungszeitraum#verwendungbis)</span><span className="hbs-nr">00340</span> | verwendungBis | string (date-time) | Kann | Kann | Kann | Kann | — |
| <span className="hbs-f hbs-e2">[zeitraumId](/bo4e/202610/bo/Verwendungszeitraum#zeitraumid) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00350</span> | zeitraumId | integer | Muss | Muss | Muss | Muss | — |
| <span className="hbs-g hbs-e1">**TRANCHE** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | — | Kann | Kann | — |
| <span className="hbs-f hbs-e2">[bilanzkreis](/bo4e/202610/bo/Tranche#bilanzkreis)</span><span className="hbs-nr">00360</span> | bilanzkreis | string | — | — | Kann | Kann | — |
| <span className="hbs-f hbs-e2">[datenqualitaet](/bo4e/202610/bo/Tranche#datenqualitaet)</span><span className="hbs-nr">00370</span> | Datenqualitaet | [Enum Datenqualitaet](/bo4e/202610/enum/Datenqualitaet) | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`ERWARTETE_DATEN`</span> | — | — | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`INFORMATIVE_DATEN`</span> | — | — | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`GUELTIGE_DATEN`</span> | — | — | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN`</span> | — | — | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_KEINE_DATEN_VORHANDEN`</span> | — | — | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN_ERWARTET`</span> | — | — | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_DATEN`</span> | — | — | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_ERWARTETE_DATEN`</span> | — | — | — | — | Kann | Kann | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | — | — | Kann | Kann | — |
| <span className="hbs-f hbs-e2">[tranchenId](/bo4e/202610/bo/Tranche#tranchenid)</span><span className="hbs-nr">00380</span> | tranchenId | string | — | — | Kann | Kann | — |
| <span className="hbs-g hbs-e2">**gueltigkeitszeitraum**</span> | — | object | — | — | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[zeitraumId](/bo4e/202610/com/Zeitraum#zeitraumid)</span><span className="hbs-nr">00390</span> | zeitraumId | integer | — | — | Kann | Kann | — |
| <span className="hbs-g hbs-e2">**marktrollen** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | — | — | Kann | — |
| <span className="hbs-f hbs-e3">[marktrolle](/bo4e/202610/bo/Marktteilnehmer#marktrolle)</span><span className="hbs-nr">00400</span> | Gibt im Klartext die Bezeichnung der Marktrolle an. | [Enum Marktrolle](/bo4e/202610/enum/Marktrolle) | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`NB`</span> | — | — | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`LF`</span> | — | — | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MSB`</span> | — | — | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MSBA`</span> | — | — | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`GMSB`</span> | — | — | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MDL`</span> | — | — | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`DL`</span> | — | — | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`BKV`</span> | — | — | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`UENB`</span> | — | — | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`KUNDE-SELBST-NN`</span> | — | — | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MGV`</span> | — | — | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`EIV`</span> | — | — | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`RB`</span> | — | — | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`KUNDE`</span> | — | — | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`INTERESSENT`</span> | — | — | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`KN`</span> | — | — | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`UBA`</span> | — | — | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`BIKO`</span> | — | — | — | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`ESA`</span> | — | — | — | — | — | Kann | — |
| <span className="hbs-f hbs-e3">[rollencodenummer](/bo4e/202610/bo/Marktteilnehmer#rollencodenummer)</span><span className="hbs-nr">00410</span> | Gibt die Codenummer der Marktrolle an. | string | — | — | — | Kann | — |

</div>

</Handbuchsatz>

## Kette dieses Auslösers

Das Ereignis löst die Nachricht aus.

| Nachricht | Antworten | Schreibaufruf nach der Antwort |
|---|---|---|
| [55126](/schnittstellen/202610/pruefi/UTILMD/PI_55126) | — | — |
| [55613](/schnittstellen/202610/pruefi/UTILMD/PI_55613) | — | — |
| [55672](/schnittstellen/202610/pruefi/UTILMD/PI_55672) | — | — |
| [55674](/schnittstellen/202610/pruefi/UTILMD/PI_55674) | — | — |

Dieses Ereignis löst Schritte in diesen Rollensichten aus:

| Prozess | Beteiligter | Regelwerk | Sparte |
|---|---|---|---|
| [Ergänzende Daten zum Lokationsbündel von NBA an NBN](/prozessdoku/202610/NB--NBA/awh-netzbetreiberwechsel-erganzende-daten-zum-lokationsbundel-von-nba-an-nbn) | NBA | AWH Netzbetreiberwechsel | Strom |
| [Abrechnungsdaten Bilanzkreisabrechnung](/prozessdoku/202610/NB/GPKE-Teil2-abrechnungsdaten-bilanzkreisabrechnung) | NB | GPKE Teil 2 | Strom |

## Transaktionsdaten

Der Umschlag der Nachricht. Pflichtfelder müssen beim Trigger-Aufruf gesetzt sein.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| [sparte](/bo4e/202610/cdoc/Transaktionsdaten#sparte) | [Enum Sparte](/bo4e/202610/enum/Sparte) | **ja** | Enthält Informationen über die Sparte Werte: `STROM`, `GAS`, `FERNWAERME`, `NAHWAERME`, `WASSER`, `ABWASSER` |
| [transaktionsgrund](/bo4e/202610/cdoc/Transaktionsdaten#transaktionsgrund) | string | **ja** | Der Transaktionsgrund beschreibt den Geschäftsvorfall zur Kategorie genauer / UTILMD STS+7++###+ZW4+E03 |
| [transaktionsgrundergaenzung](/bo4e/202610/cdoc/Transaktionsdaten#transaktionsgrundergaenzung) | string | **ja** | Ergänzung zum Transaktionsgrund / UTILMD STS+7++E01+###+E03 |
| `pruefidentifikator` | — | nein | Wird dynamisch im Event-Prozess ermittelt (Entscheidungsgrundlage: energierichtung, marktrolle). Ein vom Sender mitgegebener Wert wird ignoriert. Im Topic mögliche Prüfis — 55126, 55613, 55672, 55674. Mögliche Werte: `55126`, `55613`, `55672`, `55674` |
| [absender › rollencodenummer](/bo4e/202610/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |
| [empfaenger › marktrolle](/bo4e/202610/bo/Marktteilnehmer#marktrolle) | [Enum Marktrolle](/bo4e/202610/enum/Marktrolle) | nein | Gibt im Klartext die Bezeichnung der Marktrolle an. Werte: `NB`, `LF`, `MSB`, `MSBA`, `GMSB`, `MDL`, `DL`, `BKV`, `UENB`, `KUNDE-SELBST-NN` … (+9) |
| [empfaenger › rollencodenummer](/bo4e/202610/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |

## Zusatzdaten

`eventname` ist auf **START_ABR_BK** festgelegt. Dieser Wert bleibt auch in der englischen Fassung deutsch, weil Camunda darüber korreliert.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `prozessId` | string | **ja** | — |
| `eventname` | const `START_ABR_BK` | **ja** | — |

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
