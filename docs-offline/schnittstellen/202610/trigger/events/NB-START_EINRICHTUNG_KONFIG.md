# [NB] START_EINRICHTUNG_KONFIG
<span hidden data-pagefind-meta={"title:Trigger-Ereignis START_EINRICHTUNG_KONFIG — Marktrolle NB (FV 202610)"} />

Marktrolle **NB** · Formatversion **202610** · BO4E-Schema **1.7.8**

## Stammdaten

Unter diesem Topic ist genau einer der folgenden 1 Prüfidentifikatoren zulässig — welcher, entscheidet der Event-Prozess.

| Prüfi | Scope | Anwendungsfall | Festlegung | Kommunikation |
|---|---|---|---|---|
| [PI_17134](/schnittstellen/202610/pruefi/ORDERS/PI_17134) | ORDERS | Einrichtung Konfiguration Zuordnung LF von NB | GPKE Teil 3 | NB → MSB |

Die Stammdaten der 1 Prüfidentifikatoren in **einer** Struktur — eine Spalte je Prüfidentifikator, wie im Anwendungshandbuch. Ein Wert in der Spalte heißt, dass das Feld zu diesem Prüfidentifikator gehört: **Muss**, wenn seine Spezifikation es verlangt, sonst **Kann**. Eine leere Zelle heißt »gehört nicht dazu«, nicht »unbekannt«. Vorausgewählt ist der erste; die übrigen schaltet die Leiste über der Tabelle zu.

<Handbuchsatz>

<div className="maco-tabellenrahmen">

| Struktur (BO4E) | Beschreibung | Format | <span className="hbs-p" title="Einrichtung Konfiguration Zuordnung LF von NB">17134</span> | Bedingung |
|---|---|---|---|---|
| <span className="hbs-g hbs-e0">**stammdaten**</span> | — | object | Kann | — |
| <span className="hbs-g hbs-e1">**ANFRAGE** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | — |
| <span className="hbs-f hbs-e2">[anfragetyp](/bo4e/202610/bo/Anfrage#anfragetyp)</span><span className="hbs-nr">00010</span> | Typ/Art der Anfrage (ORDERS ORDRSP IMD 7081) | [Enum Anfragetyp](/bo4e/202610/enum/Anfragetyp) | Kann | — |
| <span className="hbs-w hbs-e3">`KAUF`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`NUTZUNGSUEBERLASSUNG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`ABRECHNUNGSBRENNWERT_UND_ZUSTANDSZAHL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`LASTGANGDATEN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`ZAEHLERSTAENDE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`WERTEERMITTLUNG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`ENERGIEMENGE_EINZELWERT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`INNERHALB_DER_ARBEITSZEIT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`AUCH_AUSSERHALB_DER_ARBEITSZEIT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`WECHSEL_SAEMTLICHER_EINRICHTUNGEN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`TEILWEISER_WECHSEL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`AENDERUNG_ZAEHLZEITDEFINITION`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`ABBESTELLUNG_ZAEHLZEITEN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`ABBESTELLUNG_MESSPRODUKT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`ANGEBOT_AUF_BASIS_PREISBLATT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`INDIVIDUELLES_ANGEBOT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`AENDERUNG_KONFIGURATION`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`KANN_NICHT_ANGEBOTEN_WERDEN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`NEUKONFIGURATION`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`BEENDIGUNG_KONFIGURATION`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`AKTIVIERUNG_KONFIGURATION`</span> | — | — | Kann | — |
| <span className="hbs-f hbs-e2">[energierichtung](/bo4e/202610/bo/Anfrage#energierichtung) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00020</span> | Spezifiziert die Energierichtung einer Markt- und/oder Messlokation | [Enum Energierichtung](/bo4e/202610/enum/Energierichtung) | Muss | — |
| <span className="hbs-w hbs-e3">`AUSSP`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`EINSP`</span> | — | — | Muss | — |
| <span className="hbs-f hbs-e2">[lokationsId](/bo4e/202610/bo/Anfrage#lokationsid) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00030</span> | Für welche Markt- oder Messlokation gilt diese Anfrage. | string | Muss | — |
| <span className="hbs-g hbs-e1">**AUFTRAG** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | — |
| <span className="hbs-f hbs-e2">[ausfuehrungsdatum](/bo4e/202610/bo/Auftrag#ausfuehrungsdatum) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00040</span> | Das Ausführungsdatum beschreibt zu welchem Zeitpunkt ein Auftrag ausgeführt werden soll. | string (date-time) | Muss | — |
| <span className="hbs-g hbs-e2">**positionsdaten** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-f hbs-e3">[anfragegrund](/bo4e/202610/com/AuftragPosition#anfragegrund)</span><span className="hbs-nr">00050</span> | Anfragegrund | [Enum Anfragegrund](/bo4e/202610/enum/Anfragegrund) | Kann | — |
| <span className="hbs-w hbs-e4">`ABGRENZUNG_VON_ENERGIEMENGEN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`ABGRENZUNG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`WECHSELEREIGNIS`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`ZWISCHENABLESUNG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`DIREKTER_VERTRAG_MSB_AN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`DIREKTER_VERTRAG_MSB_ANN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`AENDERUNG_IM_LOKATIONSBUENDEL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`NEUKONFIGURATION`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`KONFIGURATION_UNVERAENDERT`</span> | — | — | Kann | — |
| <span className="hbs-f hbs-e3">[positionsnummer](/bo4e/202610/com/AuftragPosition#positionsnummer)</span><span className="hbs-nr">00060</span> | Positionsnummer | integer | Kann | — |
| <span className="hbs-g hbs-e1">**MARKTLOKATION** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-f hbs-e2">[marktlokationsId](/bo4e/202610/bo/Marktlokation#marktlokationsid)</span><span className="hbs-nr">00070</span> | Identifikationsnummer einer Marktlokation, an der Energie entweder<br/>verbraucht, oder erzeugt wird | string | Kann | — |
| <span className="hbs-g hbs-e2">**marktrollen** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-f hbs-e3">[marktrolle](/bo4e/202610/bo/Marktteilnehmer#marktrolle)</span><span className="hbs-nr">00080</span> | Gibt im Klartext die Bezeichnung der Marktrolle an. | [Enum Marktrolle](/bo4e/202610/enum/Marktrolle) | Kann | — |
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
| <span className="hbs-f hbs-e3">[rollencodenummer](/bo4e/202610/bo/Marktteilnehmer#rollencodenummer)</span><span className="hbs-nr">00090</span> | Gibt die Codenummer der Marktrolle an. | string | Kann | — |
| <span className="hbs-f hbs-e3">[rollencodetyp](/bo4e/202610/bo/Marktteilnehmer#rollencodetyp)</span><span className="hbs-nr">00100</span> | Gibt den Typ des Codes an. | [Enum Rollencodetyp](/bo4e/202610/enum/Rollencodetyp) | Kann | — |
| <span className="hbs-w hbs-e4">`BDEW`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`GS1`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`GLN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`DVGW`</span> | — | — | Kann | — |
| <span className="hbs-f hbs-e3">[weiterverpflichtet](/bo4e/202610/bo/Marktteilnehmer#weiterverpflichtet)</span><span className="hbs-nr">00110</span> | weiterverpflichtet | boolean | Kann | — |
| <span className="hbs-g hbs-e2">**zaehlwerke** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-f hbs-e3">[messprodukt](/bo4e/202610/com/Zaehlwerk#messprodukt)</span><span className="hbs-nr">00120</span> | messprodukt | string | Kann | — |
| <span className="hbs-f hbs-e3">[verwendungszweckLF](/bo4e/202610/com/Zaehlwerk#verwendungszwecklf)</span><span className="hbs-nr">00130</span> | Codes gemäß Codeliste der Verwendungszwecke Verwendungszweck LF | string | Kann | — |
| <span className="hbs-f hbs-e3">[verwendungszweckNB](/bo4e/202610/com/Zaehlwerk#verwendungszwecknb)</span><span className="hbs-nr">00140</span> | Codes gemäß Codeliste der Verwendungszwecke Verwendungszweck NB | string | Kann | — |
| <span className="hbs-f hbs-e3">[verwendungszweckUENB](/bo4e/202610/com/Zaehlwerk#verwendungszweckuenb)</span><span className="hbs-nr">00150</span> | Codes gemäß Codeliste der Verwendungszwecke Verwendungszweck ÜNB | string | Kann | — |
| <span className="hbs-g hbs-e3">**zaehlzeiten**</span> | — | object | Kann | — |
| <span className="hbs-f hbs-e4">[zaehlzeitDefinition](/bo4e/202610/com/Zaehlzeitregister#zaehlzeitdefinition)</span><span className="hbs-nr">00160</span> | Zählzeitdefinition | string | Kann | — |
| <span className="hbs-g hbs-e1">**MESSLOKATION** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-f hbs-e2">[messlokationsId](/bo4e/202610/bo/Messlokation#messlokationsid)</span><span className="hbs-nr">00170</span> | Die Messlokations-Identifikation. Das ist die frühere Zählpunktbezeichnung,<br/>z.B. DE 47108151234567 | string | Kann | — |
| <span className="hbs-g hbs-e2">**zaehlwerke** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-f hbs-e3">[messprodukt](/bo4e/202610/com/Zaehlwerk#messprodukt)</span><span className="hbs-nr">00180</span> | messprodukt | string | Kann | — |
| <span className="hbs-g hbs-e3">**zaehlzeiten**</span> | — | object | Kann | — |
| <span className="hbs-f hbs-e4">[zaehlzeitDefinition](/bo4e/202610/com/Zaehlzeitregister#zaehlzeitdefinition)</span><span className="hbs-nr">00190</span> | Zählzeitdefinition | string | Kann | — |
| <span className="hbs-g hbs-e1">**TRANCHE** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-f hbs-e2">[bildungTranchengroesse](/bo4e/202610/bo/Tranche#bildungtranchengroesse)</span><span className="hbs-nr">00200</span> | BildungTranchengroesse | [Enum BildungTranchengroesse](/bo4e/202610/enum/BildungTranchengroesse) | Kann | — |
| <span className="hbs-w hbs-e3">`PROZENTUAL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`AUFTEILUNGSFAKTOR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`AUFTEILUNG_TECHNISCHE_RESSOURCEN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`BERECHNUNGSFORMEL`</span> | — | — | Kann | — |
| <span className="hbs-f hbs-e2">[tranchenId](/bo4e/202610/bo/Tranche#tranchenid)</span><span className="hbs-nr">00210</span> | tranchenId | string | Kann | — |
| <span className="hbs-g hbs-e2">**aufteilungsmenge**</span> | — | object | Kann | — |
| <span className="hbs-f hbs-e3">[einheit](/bo4e/202610/com/Menge#einheit)</span><span className="hbs-nr">00220</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202610/enum/Mengeneinheit) | Kann | — |
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
| <span className="hbs-f hbs-e3">[wert](/bo4e/202610/com/Menge#wert)</span><span className="hbs-nr">00230</span> | Wert | number (float) | Kann | — |
| <span className="hbs-g hbs-e2">**marktrollen** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-f hbs-e3">[marktrolle](/bo4e/202610/bo/Marktteilnehmer#marktrolle)</span><span className="hbs-nr">00240</span> | Gibt im Klartext die Bezeichnung der Marktrolle an. | [Enum Marktrolle](/bo4e/202610/enum/Marktrolle) | Kann | — |
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
| <span className="hbs-f hbs-e3">[rollencodenummer](/bo4e/202610/bo/Marktteilnehmer#rollencodenummer)</span><span className="hbs-nr">00250</span> | Gibt die Codenummer der Marktrolle an. | string | Kann | — |
| <span className="hbs-f hbs-e3">[rollencodetyp](/bo4e/202610/bo/Marktteilnehmer#rollencodetyp)</span><span className="hbs-nr">00260</span> | Gibt den Typ des Codes an. | [Enum Rollencodetyp](/bo4e/202610/enum/Rollencodetyp) | Kann | — |
| <span className="hbs-w hbs-e4">`BDEW`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`GS1`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`GLN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e4">`DVGW`</span> | — | — | Kann | — |
| <span className="hbs-g hbs-e2">**zaehlwerke** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-f hbs-e3">[messprodukt](/bo4e/202610/com/Zaehlwerk#messprodukt)</span><span className="hbs-nr">00270</span> | messprodukt | string | Kann | — |
| <span className="hbs-f hbs-e3">[verwendungszweckLF](/bo4e/202610/com/Zaehlwerk#verwendungszwecklf)</span><span className="hbs-nr">00280</span> | Codes gemäß Codeliste der Verwendungszwecke Verwendungszweck LF | string | Kann | — |
| <span className="hbs-f hbs-e3">[verwendungszweckNB](/bo4e/202610/com/Zaehlwerk#verwendungszwecknb)</span><span className="hbs-nr">00290</span> | Codes gemäß Codeliste der Verwendungszwecke Verwendungszweck NB | string | Kann | — |
| <span className="hbs-f hbs-e3">[verwendungszweckUENB](/bo4e/202610/com/Zaehlwerk#verwendungszweckuenb)</span><span className="hbs-nr">00300</span> | Codes gemäß Codeliste der Verwendungszwecke Verwendungszweck ÜNB | string | Kann | — |

</div>

</Handbuchsatz>

## Kette dieses Auslösers

Das Ereignis löst die Nachricht aus.

| Nachricht | Antworten | Schreibaufruf nach der Antwort |
|---|---|---|
| [17134](/schnittstellen/202610/pruefi/ORDERS/PI_17134) | — | — |

Dieses Ereignis löst einen Schritt in dieser Rollensicht aus:

| Prozess | Beteiligter | Regelwerk | Sparte |
|---|---|---|---|
| [Einrichtung der Konfigurationen aufgrund einer Zuordnung eines LF zu einer Marktlokation bzw. Tranche](/prozessdoku/202610/NB/GPKE-Teil3-einrichtung-der-konfigurationen-aufgrund-einer-zuordnung-eines-lf-zu-einer-marktlokation-bzw-tranche) | NB | GPKE Teil 3 | Strom |

## Transaktionsdaten

Der Umschlag der Nachricht. Pflichtfelder müssen beim Trigger-Aufruf gesetzt sein.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| [kategorie](/bo4e/202610/cdoc/Transaktionsdaten#kategorie) | string | **ja** | Qualifier aus dem Beginn der EDIFact Nachricht / BGM |
| [sparte](/bo4e/202610/cdoc/Transaktionsdaten#sparte) | [Enum Sparte](/bo4e/202610/enum/Sparte) | **ja** | Enthält Informationen über die Sparte Werte: `STROM`, `GAS`, `FERNWAERME`, `NAHWAERME`, `WASSER`, `ABWASSER` |
| `pruefidentifikator` | — | nein | Wird dynamisch im Event-Prozess ermittelt. Ein vom Sender mitgegebener Wert wird ignoriert. Im Topic mögliche Prüfis — 17134. Mögliche Werte: `17134` |
| [absender › rollencodenummer](/bo4e/202610/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |
| [empfaenger › rollencodenummer](/bo4e/202610/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |

## Zusatzdaten

`eventname` ist auf **START_EINRICHTUNG_KONFIG** festgelegt. Dieser Wert bleibt auch in der englischen Fassung deutsch, weil Camunda darüber korreliert.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `prozessId` | string | **ja** | — |
| `eventname` | const `START_EINRICHTUNG_KONFIG` | **ja** | — |

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
