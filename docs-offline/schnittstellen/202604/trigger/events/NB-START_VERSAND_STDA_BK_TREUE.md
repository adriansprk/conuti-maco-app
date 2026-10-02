# [NB] START_VERSAND_STDA_BK_TREUE
<span hidden data-pagefind-meta={"title:Trigger-Ereignis START_VERSAND_STDA_BK_TREUE — Marktrolle NB (FV 202604)"} />

Marktrolle **NB** · Formatversion **202604** · BO4E-Schema **1.7.8**

## Stammdaten

Unter diesem Topic ist genau einer der folgenden 1 Prüfidentifikatoren zulässig — welcher, entscheidet der Event-Prozess.

| Prüfi | Scope | Anwendungsfall | Festlegung | Kommunikation |
|---|---|---|---|---|
| [PI_55670](/schnittstellen/202604/pruefi/UTILMD/PI_55670) | UTILMD | Stammdaten BK-Treue | GPKE Teil 4 | NB → ÜNB |

Die Stammdaten der 1 Prüfidentifikatoren in **einer** Struktur — eine Spalte je Prüfidentifikator, wie im Anwendungshandbuch. Ein Wert in der Spalte heißt, dass das Feld zu diesem Prüfidentifikator gehört: **Muss**, wenn seine Spezifikation es verlangt, sonst **Kann**. Eine leere Zelle heißt »gehört nicht dazu«, nicht »unbekannt«. Vorausgewählt ist der erste; die übrigen schaltet die Leiste über der Tabelle zu.

<Handbuchsatz>

<div className="maco-tabellenrahmen">

| Struktur (BO4E) | Beschreibung | Format | <span className="hbs-p" title="Stammdaten BK-Treue">55670</span> | Bedingung |
|---|---|---|---|---|
| <span className="hbs-g hbs-e0">**stammdaten**</span> | — | object | Kann | — |
| <span className="hbs-g hbs-e1">**BILANZIERUNG** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-f hbs-e2">[bilanzkreis](/bo4e/202604/bo/Bilanzierung#bilanzkreis)</span><span className="hbs-nr">00010</span> | Bilanzkreis | string | Kann | — |
| <span className="hbs-f hbs-e2">[zeitreihentyp](/bo4e/202604/bo/Bilanzierung#zeitreihentyp)</span><span className="hbs-nr">00020</span> | Zeitreihentyp | [Enum Zeitreihentyp](/bo4e/202604/enum/Zeitreihentyp) | Kann | — |
| <span className="hbs-w hbs-e3">`EGS`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`LGS`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`NZR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`SES`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`SLS`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`TES`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`TLS`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`SLS_TLS`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`SES_TES`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`AUS`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`BAS`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`DBA`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`DZR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`DZÜ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`FPE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`FPI`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`SRE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`SRI`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`VZR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`BIL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`BIP`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`BIT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`GAL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`GAP`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`GAT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`GEL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`GEP`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`GET`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`SOL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`SOP`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`SOT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`WFL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`WFP`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`WNL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`WNP`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`WNT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`WAL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`WAP`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`WAT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`AU1`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`BI1`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`BI2`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`BI3`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`GAA`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`GAB`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`GAC`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`GE1`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`GE2`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`GE3`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`SO1`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`SO2`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`SO3`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`WF1`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`WF2`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`WF3`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`WN1`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`WN2`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`WN3`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`WAA`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`WAB`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`WAC`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`AUSFALLARBEITSSUMME`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`BILANZKREISABWEICHUNGSSALDO`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`DIFFERENZZEITREIHE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`DELTAZEITREIHE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`DELTAZEITREIHENUEBERTRAG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`FAHRPLANENTNAHMESUMME`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`FAHRPLANEINSPEISESUMME`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`UEBERFUEHRUNGSZEITREIHE_SEKUNDAERREGELLEISTUNG_EXPORT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`UEBERFUEHRUNGSZEITREIHE_SEKUNDAERREGELLEISTUNG_IMPORT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`VERLUSTZEITREIHE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_BIOMASSE_BIOGAS_GEMESSEN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_BIOMASSE_BIOGAS_EINSPEISEPROFIL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_BIOMASSE_BIOGAS_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_DEPONIE_KLAER_GRUBENGAS_GEMESSEN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_DEPONIE_KLAER_GRUBENGAS_EINSPEISEPROFIL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_DEPONIE_KLAER_GRUBENGAS_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_GEOTHERMIE_GEMESSEN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_GEOTHERMIE_EINSPEISEPROFIL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_GEOTHERMIE_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_SOLAR_GEMESSEN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_SOLAR_EINSPEISEPROFIL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_SOLAR_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_WIND_OFFSHORE_GEMESSEN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_WIND_OFFSHORE_EINSPEISEPROFIL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_WIND_OFFSHORE_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_WIND_ONSHORE_GEMESSEN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_WIND_ONSHORE_EINSPEISEPROFIL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_WIND_ONSHORE_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_WASSERKRAFT_GEMESSEN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_WASSERKRAFT_EINSPEISEPROFIL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`EE_EINSPEISESUMME_WASSERKRAFT_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_AUSFALLARBEIT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_BIOMASSE_BIOGAS_WERTE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_BIOMASSE_BIOGAS_STANDARDEINSPEISEPROFIL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_BIOMASSE_BIOGAS_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_DEPONIE_KLAER_GRUBENGAS_WERTE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_DEPONIE_KLAER_GRUBENGAS_STANDARDEINSPEISEPROFIL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_DEPONIE_KLAER_GRUBENGAS_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_GEOTHERMIE_WERTE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_GEOTHERMIE_STANDARDEINSPEISEPROFIL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_GEOTHERMIE_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_SOLAR_WERTE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_SOLAR_STANDARDEINSPEISEPROFIL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_SOLAR_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_WIND_OFFSHORE_WERTE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_WIND_OFFSHORE_STANDARDEINSPEISEPROFIL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_WIND_OFFSHORE_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_WIND_ONSHORE_WERTE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_WIND_ONSHORE_STANDARDEINSPEISEPROFIL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_WIND_ONSHORE_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_WASSERKRAFT_WERTE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_WASSERKRAFT_STANDARDEINSPEISEPROFIL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`EEG_UEBERFUEHRUNG_WASSERKRAFT_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL`</span> | — | — | Kann | — |
| <span className="hbs-g hbs-e1">**MARKTLOKATION** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | — |
| <span className="hbs-f hbs-e2">[bilanzierungsgebiet](/bo4e/202604/bo/Marktlokation#bilanzierungsgebiet)</span><span className="hbs-nr">00030</span> | Bilanzierungsgebiet, dem das Netzgebiet zugeordnet ist - im Falle eines Strom Netzes. | string | Kann | — |
| <span className="hbs-f hbs-e2">[datenqualitaet](/bo4e/202604/bo/Marktlokation#datenqualitaet) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00040</span> | Datenqualitaet | [Enum Datenqualitaet](/bo4e/202604/enum/Datenqualitaet) | Muss | — |
| <span className="hbs-w hbs-e3">`ERWARTETE_DATEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`INFORMATIVE_DATEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`GUELTIGE_DATEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_KEINE_DATEN_VORHANDEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN_ERWARTET`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_DATEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_ERWARTETE_DATEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | Muss | — |
| <span className="hbs-f hbs-e2">[marktlokationsId](/bo4e/202604/bo/Marktlokation#marktlokationsid)</span><span className="hbs-nr">00050</span> | Identifikationsnummer einer Marktlokation, an der Energie entweder<br/>verbraucht, oder erzeugt wird | string | Kann | — |
| <span className="hbs-g hbs-e2">**gueltigkeitszeitraum**</span> | — | object | Kann | — |
| <span className="hbs-f hbs-e3">[zeitraumId](/bo4e/202604/com/Zeitraum#zeitraumid)</span><span className="hbs-nr">00060</span> | zeitraumId | integer | Kann | — |
| <span className="hbs-g hbs-e2">**marktrollen** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-f hbs-e3">[marktrolle](/bo4e/202604/bo/Marktteilnehmer#marktrolle)</span><span className="hbs-nr">00070</span> | Gibt im Klartext die Bezeichnung der Marktrolle an. | [Enum Marktrolle](/bo4e/202604/enum/Marktrolle) | Kann | — |
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
| <span className="hbs-f hbs-e3">[rollencodenummer](/bo4e/202604/bo/Marktteilnehmer#rollencodenummer)</span><span className="hbs-nr">00080</span> | Gibt die Codenummer der Marktrolle an. | string | Kann | — |
| <span className="hbs-g hbs-e1">**TRANCHE** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-f hbs-e2">[bilanzkreis](/bo4e/202604/bo/Tranche#bilanzkreis)</span><span className="hbs-nr">00090</span> | bilanzkreis | string | Kann | — |
| <span className="hbs-f hbs-e2">[datenqualitaet](/bo4e/202604/bo/Tranche#datenqualitaet)</span><span className="hbs-nr">00100</span> | Datenqualitaet | [Enum Datenqualitaet](/bo4e/202604/enum/Datenqualitaet) | Kann | — |
| <span className="hbs-w hbs-e3">`ERWARTETE_DATEN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`INFORMATIVE_DATEN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`GUELTIGE_DATEN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_KEINE_DATEN_VORHANDEN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN_ERWARTET`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_DATEN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_ERWARTETE_DATEN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | Kann | — |
| <span className="hbs-f hbs-e2">[tranchenId](/bo4e/202604/bo/Tranche#tranchenid)</span><span className="hbs-nr">00110</span> | tranchenId | string | Kann | — |
| <span className="hbs-g hbs-e2">**gueltigkeitszeitraum**</span> | — | object | Kann | — |
| <span className="hbs-f hbs-e3">[zeitraumId](/bo4e/202604/com/Zeitraum#zeitraumid)</span><span className="hbs-nr">00120</span> | zeitraumId | integer | Kann | — |
| <span className="hbs-g hbs-e2">**marktrollen** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-f hbs-e3">[marktrolle](/bo4e/202604/bo/Marktteilnehmer#marktrolle)</span><span className="hbs-nr">00130</span> | Gibt im Klartext die Bezeichnung der Marktrolle an. | [Enum Marktrolle](/bo4e/202604/enum/Marktrolle) | Kann | — |
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
| <span className="hbs-f hbs-e3">[rollencodenummer](/bo4e/202604/bo/Marktteilnehmer#rollencodenummer)</span><span className="hbs-nr">00140</span> | Gibt die Codenummer der Marktrolle an. | string | Kann | — |
| <span className="hbs-g hbs-e1">**VERWENDUNGSZEITRAUM** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | — |
| <span className="hbs-f hbs-e2">[datenqualitaet](/bo4e/202604/bo/Verwendungszeitraum#datenqualitaet) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00150</span> | Datenqualitaet | [Enum Datenqualitaet](/bo4e/202604/enum/Datenqualitaet) | Muss | — |
| <span className="hbs-w hbs-e3">`ERWARTETE_DATEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`INFORMATIVE_DATEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`GUELTIGE_DATEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`IM_SYSTEM_KEINE_DATEN_VORHANDEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`KEINE_DATEN_ERWARTET`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_DATEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_ERWARTETE_DATEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</span> | — | — | Muss | — |
| <span className="hbs-f hbs-e2">[verwendungAb](/bo4e/202604/bo/Verwendungszeitraum#verwendungab) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00160</span> | verwendungAb | string (date-time) | Muss | — |
| <span className="hbs-f hbs-e2">[verwendungBis](/bo4e/202604/bo/Verwendungszeitraum#verwendungbis)</span><span className="hbs-nr">00170</span> | verwendungBis | string (date-time) | Kann | — |
| <span className="hbs-f hbs-e2">[zeitraumId](/bo4e/202604/bo/Verwendungszeitraum#zeitraumid) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00180</span> | zeitraumId | integer | Muss | — |

</div>

</Handbuchsatz>

## Kette dieses Auslösers

Das Ereignis löst die Nachricht aus.

| Nachricht | Antworten | Schreibaufruf nach der Antwort |
|---|---|---|
| [55670](/schnittstellen/202604/pruefi/UTILMD/PI_55670) | — | — |

Dieses Ereignis löst einen Schritt in dieser Rollensicht aus:

| Prozess | Beteiligter | Regelwerk | Sparte |
|---|---|---|---|
| [Stammdaten zur Bilanzkreistreue](/prozessdoku/202604/NB/GPKE-Teil4-stammdaten-zur-bilanzkreistreue) | NB | GPKE Teil 4 | Strom |

## Transaktionsdaten

Der Umschlag der Nachricht. Pflichtfelder müssen beim Trigger-Aufruf gesetzt sein.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `pruefidentifikator` | — | nein | Wird dynamisch im Event-Prozess ermittelt. Ein vom Sender mitgegebener Wert wird ignoriert. Im Topic mögliche Prüfis — 55670. Mögliche Werte: `55670` |

## Zusatzdaten

`eventname` ist auf **START_VERSAND_STDA_BK_TREUE** festgelegt. Dieser Wert bleibt auch in der englischen Fassung deutsch, weil Camunda darüber korreliert.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `prozessId` | string | **ja** | — |
| `eventname` | const `START_VERSAND_STDA_BK_TREUE` | **ja** | — |

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
