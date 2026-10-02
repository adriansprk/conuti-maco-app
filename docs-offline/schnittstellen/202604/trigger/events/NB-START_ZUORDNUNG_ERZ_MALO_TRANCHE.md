# [NB] START_ZUORDNUNG_ERZ_MALO_TRANCHE
<span hidden data-pagefind-meta={"title:Trigger-Ereignis START_ZUORDNUNG_ERZ_MALO_TRANCHE — Marktrolle NB (FV 202604)"} />

Marktrolle **NB** · Formatversion **202604** · BO4E-Schema **1.7.8**

## Stammdaten

Unter diesem Topic ist genau einer der folgenden 1 Prüfidentifikatoren zulässig — welcher, entscheidet der Event-Prozess.

| Prüfi | Scope | Anwendungsfall | Festlegung | Kommunikation |
|---|---|---|---|---|
| [PI_55607](/schnittstellen/202604/pruefi/UTILMD/PI_55607) | UTILMD | Ankündigung Zuordnung / Zuordnung des LF zur MaLo/ Tranche | GPKE Teil 2 | NB → LFN (Notiz "LF des Unternehmens Netzbetreiber") |

Die Stammdaten der 1 Prüfidentifikatoren in **einer** Struktur — eine Spalte je Prüfidentifikator, wie im Anwendungshandbuch. Ein Wert in der Spalte heißt, dass das Feld zu diesem Prüfidentifikator gehört: **Muss**, wenn seine Spezifikation es verlangt, sonst **Kann**. Eine leere Zelle heißt »gehört nicht dazu«, nicht »unbekannt«. Vorausgewählt ist der erste; die übrigen schaltet die Leiste über der Tabelle zu.

<Handbuchsatz>

<div className="maco-tabellenrahmen">

| Struktur (BO4E) | Beschreibung | Format | <span className="hbs-p" title="Ankündigung Zuordnung / Zuordnung des LF zur MaLo/ Tranche">55607</span> | Bedingung |
|---|---|---|---|---|
| <span className="hbs-g hbs-e0">**stammdaten**</span> | — | object | Kann | — |
| <span className="hbs-g hbs-e1">**MARKTLOKATION** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | — |
| <span className="hbs-f hbs-e2">[marktlokationsId](/bo4e/202604/bo/Marktlokation#marktlokationsid) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00010</span> | Identifikationsnummer einer Marktlokation, an der Energie entweder<br/>verbraucht, oder erzeugt wird | string | Muss | — |
| <span className="hbs-f hbs-e2">[statusErzeugendeMalo](/bo4e/202604/bo/Marktlokation#statuserzeugendemalo) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00020</span> | StatusErzeugendeMarktlokation | [Enum StatusErzeugendeMarktlokation](/bo4e/202604/enum/StatusErzeugendeMarktlokation) | Muss | — |
| <span className="hbs-w hbs-e3">`EINSPEISEVERGUETUNG_PARAGRAPH_37`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`GEFOERDERTE_DIREKTVERMARKTUNG`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`SONSTIGE_DIREKTVERMARKTUNG`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`VERMARKTUNG_OHNE_GESETZL_VERGUETUNG`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`KWKG_VERGUETUNG`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`EINSPEISEVERGUETUNG_PARAGRAPH_38_AUSFALLVERGUETUNG`</span> | — | — | Muss | — |
| <span className="hbs-g hbs-e2">**energieherkunft** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | — |
| <span className="hbs-f hbs-e3">[erzeugungsart](/bo4e/202604/com/Energieherkunft#erzeugungsart) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00030</span> | Art der Erzeugung | [Enum Erzeugungsart](/bo4e/202604/enum/Erzeugungsart) | Muss | — |
| <span className="hbs-w hbs-e4">`EEG`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`KWK`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`EEG_DV`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`KWK_DV`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`WIND`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`SOLAR`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`KERNKRAFT`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`WASSER`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`GEOTHERMIE`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`BIOMASSE`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`KOHLE`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`GAS`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`SONSTIGE`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`SONSTIGE_EEG`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`SONSTIGE_ERZEUGUNGSART`</span> | — | — | Muss | — |
| <span className="hbs-g hbs-e2">**marktrollen** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | — |
| <span className="hbs-f hbs-e3">[marktrolle](/bo4e/202604/bo/Marktteilnehmer#marktrolle)</span><span className="hbs-nr">00040</span> | Gibt im Klartext die Bezeichnung der Marktrolle an. | [Enum Marktrolle](/bo4e/202604/enum/Marktrolle) | Kann | — |
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
| <span className="hbs-f hbs-e3">[messstellenbetreiberEigenschaft](/bo4e/202604/bo/Marktteilnehmer#messstellenbetreibereigenschaft) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00050</span> | MSBEigenschaft | [Enum MSBEigenschaft](/bo4e/202604/enum/MSBEigenschaft) | Muss | — |
| <span className="hbs-w hbs-e4">`GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`WETTBEWERBLICHER_MESSSTELLENBETREIBER`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`AUFFANGMESSSTELLENBETREIBER`</span> | — | — | Muss | — |
| <span className="hbs-f hbs-e3">[rollencodenummer](/bo4e/202604/bo/Marktteilnehmer#rollencodenummer) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00060</span> | Gibt die Codenummer der Marktrolle an. | string | Muss | — |
| <span className="hbs-f hbs-e3">[weiterverpflichtet](/bo4e/202604/bo/Marktteilnehmer#weiterverpflichtet) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00070</span> | weiterverpflichtet | boolean | Muss | — |
| <span className="hbs-g hbs-e1">**MESSLOKATION** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | — |
| <span className="hbs-f hbs-e2">[messlokationsId](/bo4e/202604/bo/Messlokation#messlokationsid) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00080</span> | Die Messlokations-Identifikation. Das ist die frühere Zählpunktbezeichnung,<br/>z.B. DE 47108151234567 | string | Muss | — |
| <span className="hbs-g hbs-e2">**marktrollen** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-f hbs-e3">[marktrolle](/bo4e/202604/bo/Marktteilnehmer#marktrolle)</span><span className="hbs-nr">00090</span> | Gibt im Klartext die Bezeichnung der Marktrolle an. | [Enum Marktrolle](/bo4e/202604/enum/Marktrolle) | Kann | — |
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
| <span className="hbs-f hbs-e3">[messstellenbetreiberEigenschaft](/bo4e/202604/bo/Marktteilnehmer#messstellenbetreibereigenschaft)</span><span className="hbs-nr">00100</span> | MSBEigenschaft | [Enum MSBEigenschaft](/bo4e/202604/enum/MSBEigenschaft) | Kann | — |
| <span className="hbs-w hbs-e4">`GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`WETTBEWERBLICHER_MESSSTELLENBETREIBER`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`AUFFANGMESSSTELLENBETREIBER`</span> | — | — | Kann | — |
| <span className="hbs-f hbs-e3">[rollencodenummer](/bo4e/202604/bo/Marktteilnehmer#rollencodenummer)</span><span className="hbs-nr">00110</span> | Gibt die Codenummer der Marktrolle an. | string | Kann | — |
| <span className="hbs-f hbs-e3">[weiterverpflichtet](/bo4e/202604/bo/Marktteilnehmer#weiterverpflichtet)</span><span className="hbs-nr">00120</span> | weiterverpflichtet | boolean | Kann | — |
| <span className="hbs-g hbs-e1">**NETZLOKATION** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-f hbs-e2">[netzlokationsId](/bo4e/202604/bo/Netzlokation#netzlokationsid)</span><span className="hbs-nr">00130</span> | Identifikationsnummer einer Netzlokation, an der Energie entweder<br/>verbraucht, oder erzeugt wird (Like MarktlokationsId Marktlokation) | string | Kann | — |
| <span className="hbs-g hbs-e2">**marktrollen** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-f hbs-e3">[marktrolle](/bo4e/202604/bo/Marktteilnehmer#marktrolle)</span><span className="hbs-nr">00140</span> | Gibt im Klartext die Bezeichnung der Marktrolle an. | [Enum Marktrolle](/bo4e/202604/enum/Marktrolle) | Kann | — |
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
| <span className="hbs-f hbs-e3">[messstellenbetreiberEigenschaft](/bo4e/202604/bo/Marktteilnehmer#messstellenbetreibereigenschaft)</span><span className="hbs-nr">00150</span> | MSBEigenschaft | [Enum MSBEigenschaft](/bo4e/202604/enum/MSBEigenschaft) | Kann | — |
| <span className="hbs-w hbs-e4">`GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`WETTBEWERBLICHER_MESSSTELLENBETREIBER`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`AUFFANGMESSSTELLENBETREIBER`</span> | — | — | Kann | — |
| <span className="hbs-f hbs-e3">[rollencodenummer](/bo4e/202604/bo/Marktteilnehmer#rollencodenummer)</span><span className="hbs-nr">00160</span> | Gibt die Codenummer der Marktrolle an. | string | Kann | — |
| <span className="hbs-g hbs-e1">**NETZNUTZUNGSVERTRAG** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-f hbs-e2">[vertragsbeginn](/bo4e/202604/bo/Vertrag#vertragsbeginn)</span><span className="hbs-nr">00170</span> | Gibt an, wann der Vertrag beginnt. | string (date-time) | Kann | — |
| <span className="hbs-f hbs-e2">[vertragsende](/bo4e/202604/bo/Vertrag#vertragsende)</span><span className="hbs-nr">00180</span> | Gibt an, wann der Vertrag (voraussichtlich) endet oder beendet wurde. | string (date-time) | Kann | — |
| <span className="hbs-g hbs-e1">**STEUERBARE_RESSOURCE** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-f hbs-e2">[ressourcenId](/bo4e/202604/bo/SteuerbareRessource#ressourcenid)</span><span className="hbs-nr">00190</span> | ressourcenId | string | Kann | — |
| <span className="hbs-g hbs-e2">**marktrollen** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-f hbs-e3">[marktrolle](/bo4e/202604/bo/Marktteilnehmer#marktrolle)</span><span className="hbs-nr">00200</span> | Gibt im Klartext die Bezeichnung der Marktrolle an. | [Enum Marktrolle](/bo4e/202604/enum/Marktrolle) | Kann | — |
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
| <span className="hbs-f hbs-e3">[messstellenbetreiberEigenschaft](/bo4e/202604/bo/Marktteilnehmer#messstellenbetreibereigenschaft)</span><span className="hbs-nr">00210</span> | MSBEigenschaft | [Enum MSBEigenschaft](/bo4e/202604/enum/MSBEigenschaft) | Kann | — |
| <span className="hbs-w hbs-e4">`GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`WETTBEWERBLICHER_MESSSTELLENBETREIBER`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`AUFFANGMESSSTELLENBETREIBER`</span> | — | — | Kann | — |
| <span className="hbs-f hbs-e3">[rollencodenummer](/bo4e/202604/bo/Marktteilnehmer#rollencodenummer)</span><span className="hbs-nr">00220</span> | Gibt die Codenummer der Marktrolle an. | string | Kann | — |
| <span className="hbs-g hbs-e1">**TECHNISCHE_RESSOURCE** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-f hbs-e2">[ressourcenId](/bo4e/202604/bo/TechnischeRessource#ressourcenid)</span><span className="hbs-nr">00230</span> | ressourcenId | string | Kann | — |
| <span className="hbs-g hbs-e1">**TRANCHE** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-f hbs-e2">[bildungTranchengroesse](/bo4e/202604/bo/Tranche#bildungtranchengroesse)</span><span className="hbs-nr">00240</span> | BildungTranchengroesse | [Enum BildungTranchengroesse](/bo4e/202604/enum/BildungTranchengroesse) | Kann | — |
| <span className="hbs-w hbs-e3">`PROZENTUAL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`AUFTEILUNGSFAKTOR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`AUFTEILUNG_TECHNISCHE_RESSOURCEN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`BERECHNUNGSFORMEL`</span> | — | — | Kann | — |
| <span className="hbs-f hbs-e2">[tranchenId](/bo4e/202604/bo/Tranche#tranchenid)</span><span className="hbs-nr">00250</span> | tranchenId | string | Kann | — |
| <span className="hbs-g hbs-e2">**aufteilungsmenge**</span> | — | object | Kann | — |
| <span className="hbs-f hbs-e3">[einheit](/bo4e/202604/com/Menge#einheit)</span><span className="hbs-nr">00260</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202604/enum/Mengeneinheit) | Kann | — |
| <span className="hbs-w hbs-e4">`W`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`WH`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`KW`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`KWH`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`KVARH`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MW`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MWH`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`STUECK`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`KUBIKMETER`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`STUNDE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`TAG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`MONAT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`JAHR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`PROZENT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`ANZAHL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`VAR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`KVAR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`VARH`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`KWHK`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`Z16`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`KWT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`WATT_PRO_QUADRATMETER`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`METER_PRO_SEKUNDE`</span> | — | — | Kann | — |
| <span className="hbs-f hbs-e3">[wert](/bo4e/202604/com/Menge#wert)</span><span className="hbs-nr">00270</span> | Wert | number (float) | Kann | — |

</div>

</Handbuchsatz>

## Kette dieses Auslösers

Das Ereignis löst die Nachricht aus. Der Marktpartner antwortet mit einer der genannten Antworten, und danach schreibt die MACO APP den Vorgang in Ihr Backendsystem.

| Nachricht | Antworten | Schreibaufruf nach der Antwort |
|---|---|---|
| [55607](/schnittstellen/202604/pruefi/UTILMD/PI_55607) | [55608](/schnittstellen/202604/pruefi/UTILMD/PI_55608), [55609](/schnittstellen/202604/pruefi/UTILMD/PI_55609) | `POST /createProcessData`; `POST /updateProcessData` |

Dieses Ereignis löst Schritte in diesen Rollensichten aus:

| Prozess | Beteiligter | Regelwerk | Sparte |
|---|---|---|---|
| [Fall 1: LF-Zuordnung bei EEG-Marktlokation ohne DV-Pflicht bzw. KWKG-Marktlokation ohne DV-Pflicht](/prozessdoku/202604/NB/GPKE-Teil2-fall-1-lf-zuordnung-bei-eeg-marktlokation-ohne-dv-pflicht-bzw-kwkg-marktlokation-ohne-dv-pflicht) | NB | GPKE Teil 2 | Strom |
| [Fall 2: LF-Zuordnung bei EEG-Marktlokation mit DV-Pflicht](/prozessdoku/202604/NB/GPKE-Teil2-fall-2-lf-zuordnung-bei-eeg-marktlokation-mit-dv-pflicht) | NB | GPKE Teil 2 | Strom |
| [Fall 3: LF-Zuordnung bei KWKG-Marktlokation mit DV-Pflicht bzw. Nicht-EEG-/Nicht-KWKG-Marktlokation und Marktlokation wird nicht-tranchiert abgebildet](/prozessdoku/202604/NB/GPKE-Teil2-fall-3-lf-zuordnung-bei-kwkg-marktlokation-mit-dv-pflicht-bzw-nicht-eeg-nicht-kwkg-marktlokation-und-marktlokation-wird-nicht-tranchiert-abgebildet) | NB | GPKE Teil 2 | Strom |
| [Fall 4: LF-Zuordnung bei KWKG-Marktlokation mit DV-Pflicht bzw. Nicht-EEG-/Nicht-KWKG-Marktlokation und Marktlokation wird tranchiert abgebildet](/prozessdoku/202604/NB/GPKE-Teil2-fall-4-lf-zuordnung-bei-kwkg-marktlokation-mit-dv-pflicht-bzw-nicht-eeg-nicht-kwkg-marktlokation-und-marktlokation-wird-tranchiert-abgebildet) | NB | GPKE Teil 2 | Strom |

## Transaktionsdaten

Der Umschlag der Nachricht. Pflichtfelder müssen beim Trigger-Aufruf gesetzt sein.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| [kategorie](/bo4e/202604/cdoc/Transaktionsdaten#kategorie) | string | **ja** | Qualifier aus dem Beginn der EDIFact Nachricht / BGM |
| [sparte](/bo4e/202604/cdoc/Transaktionsdaten#sparte) | [Enum Sparte](/bo4e/202604/enum/Sparte) | **ja** | Enthält Informationen über die Sparte Werte: `STROM`, `GAS`, `FERNWAERME`, `NAHWAERME`, `WASSER`, `ABWASSER` |
| [transaktionsgrund](/bo4e/202604/cdoc/Transaktionsdaten#transaktionsgrund) | string | **ja** | Der Transaktionsgrund beschreibt den Geschäftsvorfall zur Kategorie genauer / UTILMD STS+7++###+ZW4+E03 |
| [transaktionsgrundergaenzung](/bo4e/202604/cdoc/Transaktionsdaten#transaktionsgrundergaenzung) | string | **ja** | Ergänzung zum Transaktionsgrund / UTILMD STS+7++E01+###+E03 |
| [transaktionsgrundergaenzungBefristeteAnmeldung](/bo4e/202604/cdoc/Transaktionsdaten#transaktionsgrundergaenzungbefristeteanmeldung) | string | **ja** | Ergänzung zum Transaktionsgrund bei befristeten An-/Abmeldungen / UTILMD STS+7++E01+ZW4+### |
| `pruefidentifikator` | — | nein | Wird dynamisch im Event-Prozess ermittelt. Ein vom Sender mitgegebener Wert wird ignoriert. Im Topic mögliche Prüfis — 55607. Mögliche Werte: `55607` |
| [absender › rollencodenummer](/bo4e/202604/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |
| [empfaenger › rollencodenummer](/bo4e/202604/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |

## Zusatzdaten

`eventname` ist auf **START_ZUORDNUNG_ERZ_MALO_TRANCHE** festgelegt. Dieser Wert bleibt auch in der englischen Fassung deutsch, weil Camunda darüber korreliert.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `prozessId` | string | **ja** | — |
| `eventname` | const `START_ZUORDNUNG_ERZ_MALO_TRANCHE` | **ja** | — |

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
