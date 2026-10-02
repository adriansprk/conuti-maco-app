# [MSB] START_VERSAND_PREISBLATT_IMS
<span hidden data-pagefind-meta={"title:Trigger-Ereignis START_VERSAND_PREISBLATT_IMS — Marktrolle MSB (FV 202610)"} />

Marktrolle **MSB** · Formatversion **202610** · BO4E-Schema **1.7.8**

## Stammdaten

Unter diesem Topic ist genau einer der folgenden 1 Prüfidentifikatoren zulässig — welcher, entscheidet der Event-Prozess.

| Prüfi | Scope | Anwendungsfall | Festlegung | Kommunikation |
|---|---|---|---|---|
| [PI_27002](/schnittstellen/202610/pruefi/PRICAT/PI_27002) | PRICAT | Preisblätter MSB-Leistungen | GPKE Teil 3 | MSB → NB |

Die Stammdaten der 1 Prüfidentifikatoren in **einer** Struktur — eine Spalte je Prüfidentifikator, wie im Anwendungshandbuch. Ein Wert in der Spalte heißt, dass das Feld zu diesem Prüfidentifikator gehört: **Muss**, wenn seine Spezifikation es verlangt, sonst **Kann**. Eine leere Zelle heißt »gehört nicht dazu«, nicht »unbekannt«. Vorausgewählt ist der erste; die übrigen schaltet die Leiste über der Tabelle zu.

<Handbuchsatz>

<div className="maco-tabellenrahmen">

| Struktur (BO4E) | Beschreibung | Format | <span className="hbs-p" title="Preisblätter MSB-Leistungen">27002</span> | Bedingung |
|---|---|---|---|---|
| <span className="hbs-g hbs-e0">**stammdaten**</span> | — | object | Kann | — |
| <span className="hbs-g hbs-e1">**PREISBLATT** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | — |
| <span className="hbs-g hbs-e2">**gueltigkeit** <span className="hbs-pflicht">\*</span></span> | — | object | Muss | — |
| <span className="hbs-f hbs-e3">[startdatum](/bo4e/202610/com/Zeitraum#startdatum) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00010</span> | startdatum | string (date-time) | Muss | — |
| <span className="hbs-g hbs-e2">**preispositionen** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-f hbs-e3">[artikelId](/bo4e/202610/com/Preisposition#artikelid)</span><span className="hbs-nr">00020</span> | Die genauen Bedeutungen der einzelnen Artikel-IDs sind in der EDI@Energy Codeliste der Artikelnummern<br/>und Artikel-IDs zu finden, die in der Spalte "PRICAT Codeverwendung" ein X haben | string | Kann | — |
| <span className="hbs-f hbs-e3">[bdewArtikelnummer](/bo4e/202610/com/Preisposition#bdewartikelnummer)</span><span className="hbs-nr">00030</span> | Eine vom BDEW standardisierte Bezeichnung für die abgerechnete Leistungserbringung. Diese Artikelnummer wird<br/>auch im Rechnungsteil der INVOIC verwendet. | [Enum BDEWArtikelnummer](/bo4e/202610/enum/BDEWArtikelnummer) | Kann | — |
| <span className="hbs-w hbs-e4">`LEISTUNG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`LEISTUNG_PAUSCHAL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`GRUNDPREIS`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`REGELENERGIE_ARBEIT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`REGELENERGIE_LEISTUNG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`NOTSTROMLIEFERUNG_ARBEIT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`NOTSTROMLIEFERUNG_LEISTUNG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`RESERVENETZKAPAZITAET`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`RESERVELEISTUNG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`ZUSAETZLICHE_ABLESUNG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`PRUEFGEBUEHREN_AUSSERPLANMAESSIG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`WIRKARBEIT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`SINGULAER_GENUTZTE_BETRIEBSMITTEL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`ABGABE_KWKG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`ABSCHLAG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`KONZESSIONSABGABE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`ENTGELT_FERNAUSLESUNG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`UNTERMESSUNG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`BLINDMEHRARBEIT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`ENTGELT_ABRECHNUNG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`SPERRKOSTEN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`ENTSPERRKOSTEN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MAHNKOSTEN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MEHR_MINDERMENGEN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`INKASSOKOSTEN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`BLINDMEHRLEISTUNG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`ENTGELT_MESSUNG_ABLESUNG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`ENTGELT_EINBAU_BETRIEB_WARTUNG_MESSTECHNIK`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`AUSGLEICHSENERGIE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`AUSGLEICHSENERGIE_UNTERDECKUNG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`ZAEHLEINRICHTUNG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`WANDLER_MENGENUMWERTER`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`KOMMUNIKATIONSEINRICHTUNG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`TECHNISCHE_STEUEREINRICHTUNG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`PARAGRAF_19_STROM_NEV_UMLAGE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`BEFESTIGUNGSEINRICHTUNG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`OFFSHORE_HAFTUNGSUMLAGE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`FIXE_ARBEITSENTGELTKOMPONENTE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`FIXE_LEISTUNGSENTGELTKOMPONENTE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`UMLAGE_ABSCHALTBARE_LASTEN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MEHRMENGE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MINDERMENGE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`ENERGIESTEUER`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`SMARTMETER_GATEWAY`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`STEUERBOX`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MSB_INKL_MESSUNG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_2_1_MSBG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_2_2_MSBG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_2_3_MSBG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_2_4_MSBG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_2_5_MSBG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_3_MSBG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`ENTGELT_KAPAZITAETEN`</span> | — | — | Kann | — |
| <span className="hbs-f hbs-e3">[beschreibung](/bo4e/202610/com/Preisposition#beschreibung)</span><span className="hbs-nr">00040</span> | Produkt-/Leistungsbeschreibung, wenn IMD+X vorhanden Vgl. PRICAT IMD 7008 | string | Kann | — |
| <span className="hbs-f hbs-e3">[beschreibungsformat](/bo4e/202610/com/Preisposition#beschreibungsformat)</span><span className="hbs-nr">00050</span> | Vgl. PRICAT IMD 7077 | [Enum Beschreibungsformat](/bo4e/202610/enum/Beschreibungsformat) | Kann | — |
| <span className="hbs-w hbs-e4">`CODE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`FREIER_TEXT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`TEILSTRUKTURIERT`</span> | — | — | Kann | — |
| <span className="hbs-f hbs-e3">[leistungsbezeichnung](/bo4e/202610/com/Preisposition#leistungsbezeichnung)</span><span className="hbs-nr">00060</span> | Bezeichnung für die in der Position abgebildete Leistungserbringung | [Enum Leistungsbezeichnung](/bo4e/202610/enum/Leistungsbezeichnung) | Kann | — |
| <span className="hbs-w hbs-e4">`POG_VERBRAUCH_IMS_UEBER_100K`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`POG_VERBRAUCH_IMS_50K_BIS_100K`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`POG_VERBRAUCH_IMS_20K_BIS_50K`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`POG_VERBRAUCH_IMS_10K_BIS_20K`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`POG_VERBRAUCH_IMS_UNTERBRECHBAR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`POG_VERBRAUCH_IMS_6K_BIS_10K`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`POG_ERZEUGUNG_IMS_7_BIS_15`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`POG_ERZEUGUNG_IMS_15_BIS_30`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`POG_ERZEUGUNG_IMS_30_BIS_100`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`POG_ERZEUGUNG_IMS_UEBER_100`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`POG_MME`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`POG_VERBRAUCH_IMS_4K_BIS_6K`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`POG_VERBRAUCH_IMS_3K_BIS_4K`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`POG_VERBRAUCH_IMS_2K_BIS_3K`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`POG_VERBRAUCH_IMS_0_BIS_2K`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`POG_ERZEUGUNG_IMS_OPTIONAL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`ZUSATZLEISTUNG`</span> | — | — | Kann | — |
| <span className="hbs-f hbs-e3">[messebene](/bo4e/202610/com/Preisposition#messebene)</span><span className="hbs-nr">00070</span> | Vgl. PRICAT IMD 7009 | [Enum Netzebene](/bo4e/202610/enum/Netzebene) | Kann | — |
| <span className="hbs-w hbs-e4">`NSP`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MSP`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`HSP`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`HSS`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MSP_NSP_UMSP`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`HSP_MSP_UMSP`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`HSS_HSP_UMSP`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`HD`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MD`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`ND`</span> | — | — | Kann | — |
| <span className="hbs-f hbs-e3">[positionsnummer](/bo4e/202610/com/Preisposition#positionsnummer)</span><span className="hbs-nr">00080</span> | Fortlaufende Nummer für die Preisposition | integer | Kann | — |
| <span className="hbs-f hbs-e3">[preisschluesselstamm](/bo4e/202610/com/Preisposition#preisschluesselstamm)</span><span className="hbs-nr">00090</span> | Preisschlüsselstamm&gt; | string | Kann | — |
| <span className="hbs-f hbs-e3">[zeitbasis](/bo4e/202610/com/Preisposition#zeitbasis)</span><span className="hbs-nr">00100</span> | Die Zeit(dauer) auf die sich der Preis bezieht. Z.B. ein Jahr für einen Leistungspreis der in €/kW/Jahr<br/>ausgegeben wird. | [Enum Zeiteinheit](/bo4e/202610/enum/Zeiteinheit) | Kann | — |
| <span className="hbs-w hbs-e4">`SEKUNDE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MINUTE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`STUNDE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`VIERTEL_STUNDE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`TAG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`WOCHE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MONAT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`QUARTAL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`HALBJAHR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`JAHR`</span> | — | — | Kann | — |
| <span className="hbs-g hbs-e3">**preisstaffeln** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-f hbs-e4">[einheit](/bo4e/202610/com/Preisstaffel#einheit)</span><span className="hbs-nr">00110</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202610/enum/Mengeneinheit) | Kann | — |
| <span className="hbs-w hbs-e5">`W`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`WH`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`KW`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`KWH`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`KVARH`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MW`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MWH`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`STUECK`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`KUBIKMETER`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`STUNDE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`TAG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MONAT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`JAHR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`PROZENT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`ANZAHL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`VAR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`KVAR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`VARH`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`KWHK`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`Z16`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`KWT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`WATT_PRO_QUADRATMETER`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`METER_PRO_SEKUNDE`</span> | — | — | Kann | — |
| <span className="hbs-f hbs-e4">[einheitspreis](/bo4e/202610/com/Preisstaffel#einheitspreis)</span><span className="hbs-nr">00120</span> | einheitspreis | number (float) | Kann | — |
| <span className="hbs-f hbs-e4">[staffelgrenzeBis](/bo4e/202610/com/Preisstaffel#staffelgrenzebis)</span><span className="hbs-nr">00130</span> | staffelgrenzeBis | number (float) | Kann | — |
| <span className="hbs-f hbs-e4">[staffelgrenzeVon](/bo4e/202610/com/Preisstaffel#staffelgrenzevon)</span><span className="hbs-nr">00140</span> | staffelgrenzeVon | number (float) | Kann | — |

</div>

</Handbuchsatz>

## Kette dieses Auslösers

Das Ereignis löst die Nachricht aus.

| Nachricht | Antworten | Schreibaufruf nach der Antwort |
|---|---|---|
| [27002](/schnittstellen/202610/pruefi/PRICAT/PI_27002) | — | — |

Dieses Ereignis löst Schritte in diesen Rollensichten aus:

| Prozess | Beteiligter | Regelwerk | Sparte |
|---|---|---|---|
| [Übermittlung Preisblatt B des MSB vom MSB an NB und LF](/prozessdoku/202610/MSB/awh-prozesse-zur-anderung-der-technik-an-lokationen-ubermittlung-preisblatt-b-des-msb-vom-msb-an-nb-und-lf) | MSB | AWH Prozesse zur Änderung der Technik an Lokationen | Strom |
| [Übermittlung Preisblatt A des MSB vom MSB an NB und LF](/prozessdoku/202610/MSB/GPKE-Teil3-uebermittlung-preisblatt-a-des-msb-vom-msb-an-nb-und-lf) | MSB | GPKE Teil 3 | Strom |
| [Übermittlung Preisblatt MSB an LF](/prozessdoku/202610/MSB/WiM-Teil1-uebermittlung-preisblatt-msb-an-lf) | MSB | WiM Strom Teil 1 | Strom |
| [Übermittlung Preisblatt „Messstellenbetrieb mit iMS gegenüber dem NB“ vom MSB an NB](/prozessdoku/202610/MSB/WiM-Teil1-uebermittlung-preisblatt-messstellenbetrieb-mit-ims-gegenueber-dem-nb-vom-msb-an-nb) | MSB | WiM Strom Teil 1 | Strom |

## Transaktionsdaten

Der Umschlag der Nachricht. Pflichtfelder müssen beim Trigger-Aufruf gesetzt sein.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| [kategorie](/bo4e/202610/cdoc/Transaktionsdaten#kategorie) | string | **ja** | Qualifier aus dem Beginn der EDIFact Nachricht / BGM |
| `pruefidentifikator` | — | **ja** | Wird dynamisch im Event-Prozess ermittelt. Ein vom Sender mitgegebener Wert wird ignoriert. Im Topic mögliche Prüfis — 27002. Mögliche Werte: `27002` |
| [sparte](/bo4e/202610/cdoc/Transaktionsdaten#sparte) | [Enum Sparte](/bo4e/202610/enum/Sparte) | **ja** | Enthält Informationen über die Sparte Werte: `STROM`, `GAS`, `FERNWAERME`, `NAHWAERME`, `WASSER`, `ABWASSER` |
| [absender › marktrolle](/bo4e/202610/bo/Marktteilnehmer#marktrolle) | [Enum Marktrolle](/bo4e/202610/enum/Marktrolle) | nein | Gibt im Klartext die Bezeichnung der Marktrolle an. Werte: `NB`, `LF`, `MSB`, `MSBA`, `GMSB`, `MDL`, `DL`, `BKV`, `UENB`, `KUNDE-SELBST-NN` … (+9) |
| [absender › rollencodenummer](/bo4e/202610/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |
| [empfaenger › marktrolle](/bo4e/202610/bo/Marktteilnehmer#marktrolle) | [Enum Marktrolle](/bo4e/202610/enum/Marktrolle) | nein | Gibt im Klartext die Bezeichnung der Marktrolle an. Werte: `NB`, `LF`, `MSB`, `MSBA`, `GMSB`, `MDL`, `DL`, `BKV`, `UENB`, `KUNDE-SELBST-NN` … (+9) |
| [empfaenger › rollencodenummer](/bo4e/202610/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |

## Zusatzdaten

`eventname` ist auf **START_VERSAND_PREISBLATT_IMS** festgelegt. Dieser Wert bleibt auch in der englischen Fassung deutsch, weil Camunda darüber korreliert.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `prozessId` | string | **ja** | — |
| `eventname` | const `START_VERSAND_PREISBLATT_IMS` | **ja** | — |

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
