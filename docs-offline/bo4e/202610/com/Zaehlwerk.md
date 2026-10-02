# Zaehlwerk
<span hidden data-pagefind-meta={"title:Zaehlwerk — BO4E-Komponente (FV 202610)"} />

BO4E-Komponente · 31 Felder · 366 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="zaehlwerkid"></a>`zaehlwerkId` | string | Identifikation des Zählwerks (Registers) innerhalb des Zählers. Oftmals eine laufende Nummer hinter der Zählernummer. Z.B. 47110815_1 |
| <a id="bezeichnung"></a>`bezeichnung` | string | Zusätzliche Bezeichnung, z.B. Zählwerk_Wirkarbeit. |
| <a id="richtung"></a>`richtung` | [Enum Energierichtung](/bo4e/202610/enum/Energierichtung)<br/><Werte>`AUSSP`, `EINSP`</Werte> | Die Energierichtung, Einspeisung oder Ausspeisung. Details Energierichtung |
| <a id="obiskennzahl"></a>`obisKennzahl` | string | Die OBIS-Kennzahl für das Zählwerk, die festlegt, welche auf die gemessene Größe mit dem Stand gemeldet wird. Nur Zählwerkstände mit dieser OBIS-Kennzahl werden an diesem Zählwerk registriert. Beispiel:1-0:1.8.1 für elektrische Wirkarbeit. |
| <a id="wandlerfaktor"></a>`wandlerfaktor` | number (float) | Mit diesem Faktor wird eine Zählerstandsdifferenz multipliziert, um zum eigentlichen Verbrauch im Zeitraum zu kommen. |
| <a id="einheit"></a>`einheit` | [Enum Mengeneinheit](/bo4e/202610/enum/Mengeneinheit)<br/><Werte>`W`, `WH`, `KW`, `KWH`, `KVARH`, `MW`, `MWH`, `STUECK`, `KUBIKMETER`, `STUNDE`, `TAG`, `MONAT`, `JAHR`, `PROZENT`, `ANZAHL`, `VAR`, `KVAR`, `VARH`, `KWHK`, `Z16`, `KWT`, `WATT_PRO_QUADRATMETER`, `METER_PRO_SEKUNDE`</Werte> | Die Einheit der gemessenen Größe, z.B. kWh. Details Mengeneinheit |
| <a id="schwachlastfaehig"></a>`schwachlastfaehig` | [Enum Schwachlastfaehig](/bo4e/202610/enum/Schwachlastfaehig)<br/><Werte>`SCHWACHLASTFAEHIG`, `NICHT_SCHWACHLASTFAEHIG`</Werte> | schwachlastfaehig |
| <a id="verbrauchsart"></a>`verbrauchsart` | [Enum Verbrauchsart[]](/bo4e/202610/enum/Verbrauchsart)<br/><Werte>`KL`, `W`, `EMOB`, `SB`, `SW`, `WK`</Werte> | Stromverbrauchsart/Verbrauchsart Marktlokation |
| <a id="unterbrechbarkeit"></a>`unterbrechbarkeit` | [Enum Unterbrechbarkeit](/bo4e/202610/enum/Unterbrechbarkeit)<br/><Werte>`UV`, `NUV`</Werte> | Stromverbrauchsart/Unterbrechbarkeit Marktlokation |
| <a id="waermenutzung"></a>`waermenutzung` | [Enum Waermenutzung](/bo4e/202610/enum/Waermenutzung)<br/><Werte>`SPEICHERHEIZUNG`, `WAERMEPUMPE`, `DIREKTHEIZUNG`, `WAERMEPUMPE_WAERME_KAELTE`, `WAERMEPUMPE_KAELTE`, `WAERMEPUMPE_WAERME`</Werte> | Stromverbrauchsart/Wärmenutzung Marktlokation |
| <a id="konzessionsabgabe"></a>`konzessionsabgabe` | [Konzessionsabgabe](/bo4e/202610/com/Konzessionsabgabe) | — |
| <a id="steuerbefreit"></a>`steuerbefreit` | boolean | steuerbefreit |
| <a id="vorkommastelle"></a>`vorkommastelle` | integer | vorkommastelle |
| <a id="nachkommastelle"></a>`nachkommastelle` | integer | nachkommastelle |
| <a id="abrechnungsrelevant"></a>`abrechnungsrelevant` | boolean | abrechnungsrelevant |
| <a id="anzahlablesungen"></a>`anzahlAblesungen` | integer | anzahlAblesungen |
| <a id="zaehlzeiten"></a>`zaehlzeiten` | [Zaehlzeitregister](/bo4e/202610/com/Zaehlzeitregister) | — |
| <a id="konfiguration"></a>`konfiguration` | string | Konfiguration (iMSys) des Zählwerks |
| <a id="messprodukt"></a>`messprodukt` | string | messprodukt |
| <a id="wertegranularitaet"></a>`wertegranularitaet` | [Enum Wertegranularitaet](/bo4e/202610/enum/Wertegranularitaet)<br/><Werte>`JAEHRLICH`, `HALBJAEHRLICH`, `QUARTALSWEISE`, `MONATLICH`</Werte> | Wertegranularitaet |
| <a id="notwendigkeitzweitemessung"></a>`notwendigkeitZweiteMessung` | [Enum NotwendigkeitZweiteMessung](/bo4e/202610/enum/NotwendigkeitZweiteMessung)<br/><Werte>`VORHANDEN`, `NICHT_VORHANDEN`</Werte> | NotwendigkeitZweiteMessung |
| <a id="werteuebermittlungverwendungszweck"></a>`werteuebermittlungVerwendungszweck` | [Enum WerteuebermittlungVerwendungszweck](/bo4e/202610/enum/WerteuebermittlungVerwendungszweck)<br/><Werte>`VORHANDEN`, `NICHT_VORHANDEN`</Werte> | WerteuebermittlungVerwendungszweck |
| <a id="artemobilitaet"></a>`artEMobilitaet` | [Enum ArtEmobilitaet](/bo4e/202610/enum/ArtEmobilitaet)<br/><Werte>`WB`, `LS`, `LP`</Werte> | ArtEmobilitaet |
| <a id="konfigurationsprodukt"></a>`konfigurationsprodukt` | string | konfigurationsprodukt |
| <a id="keinkonfigurationsprodukt"></a>`keinKonfigurationsprodukt` | boolean | keinKonfigurationsprodukt |
| <a id="leistungskurvendefinition"></a>`leistungskurvendefinition` | string | leistungskurvendefinition |
| <a id="verwendungszwecke"></a>`verwendungszwecke` | [Verwendungszweck[]](/bo4e/202610/com/Verwendungszweck) | Verwendungungszweck der Werte Marktlokation |
| <a id="verwendungszwecknb"></a>`verwendungszweckNB` | string | Codes gemäß Codeliste der Verwendungszwecke Verwendungszweck NB |
| <a id="verwendungszwecklf"></a>`verwendungszweckLF` | string | Codes gemäß Codeliste der Verwendungszwecke Verwendungszweck LF |
| <a id="verwendungszweckuenb"></a>`verwendungszweckUENB` | string | Codes gemäß Codeliste der Verwendungszwecke Verwendungszweck ÜNB |
| <a id="keinprodukt"></a>`keinProdukt` | boolean | CCI+11++ZF6: keinProdukt zugeordnet |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[zaehlwerkId](/bo4e/202610/com/Zaehlwerk#zaehlwerkid)</span> | Identifikation des Zählwerks (Registers) innerhalb des Zählers. Oftmals eine laufende Nummer hinter der<br/>Zählernummer. Z.B. 47110815_1 | string |
| <span className="hbs-f hbs-e0">[bezeichnung](/bo4e/202610/com/Zaehlwerk#bezeichnung)</span> | Zusätzliche Bezeichnung, z.B. Zählwerk_Wirkarbeit. | string |
| <span className="hbs-f hbs-e0">[richtung](/bo4e/202610/com/Zaehlwerk#richtung)</span> | Die Energierichtung, Einspeisung oder Ausspeisung. Details Energierichtung | [Enum Energierichtung](/bo4e/202610/enum/Energierichtung)<br/><Werte>`AUSSP`, `EINSP`</Werte> |
| <span className="hbs-f hbs-e0">[obisKennzahl](/bo4e/202610/com/Zaehlwerk#obiskennzahl)</span> | Die OBIS-Kennzahl für das Zählwerk, die festlegt, welche auf die gemessene Größe mit dem Stand gemeldet wird.<br/>Nur Zählwerkstände mit dieser OBIS-Kennzahl werden an diesem Zählwerk registriert. Beispiel:1-0:1.8.1 für<br/>elektrische Wirkarbeit. | string |
| <span className="hbs-f hbs-e0">[wandlerfaktor](/bo4e/202610/com/Zaehlwerk#wandlerfaktor)</span> | Mit diesem Faktor wird eine Zählerstandsdifferenz multipliziert, um zum eigentlichen Verbrauch im Zeitraum zu<br/>kommen. | number (float) |
| <span className="hbs-f hbs-e0">[einheit](/bo4e/202610/com/Zaehlwerk#einheit)</span> | Die Einheit der gemessenen Größe, z.B. kWh. Details Mengeneinheit | [Enum Mengeneinheit](/bo4e/202610/enum/Mengeneinheit)<br/><Werte>`W`, `WH`, `KW`, `KWH`, `KVARH`, `MW`, `MWH`, `STUECK`, `KUBIKMETER`, `STUNDE`, `TAG`, `MONAT`, `JAHR`, `PROZENT`, `ANZAHL`, `VAR`, `KVAR`, `VARH`, `KWHK`, `Z16`, `KWT`, `WATT_PRO_QUADRATMETER`, `METER_PRO_SEKUNDE`</Werte> |
| <span className="hbs-f hbs-e0">[schwachlastfaehig](/bo4e/202610/com/Zaehlwerk#schwachlastfaehig)</span> | schwachlastfaehig | [Enum Schwachlastfaehig](/bo4e/202610/enum/Schwachlastfaehig)<br/><Werte>`SCHWACHLASTFAEHIG`, `NICHT_SCHWACHLASTFAEHIG`</Werte> |
| <span className="hbs-f hbs-e0">[verbrauchsart](/bo4e/202610/com/Zaehlwerk#verbrauchsart) <span className="hbs-liste">[ ]</span></span> | Stromverbrauchsart/Verbrauchsart Marktlokation | [Enum Verbrauchsart[]](/bo4e/202610/enum/Verbrauchsart)<br/><Werte>`KL`, `W`, `EMOB`, `SB`, `SW`, `WK`</Werte> |
| <span className="hbs-f hbs-e0">[unterbrechbarkeit](/bo4e/202610/com/Zaehlwerk#unterbrechbarkeit)</span> | Stromverbrauchsart/Unterbrechbarkeit Marktlokation | [Enum Unterbrechbarkeit](/bo4e/202610/enum/Unterbrechbarkeit)<br/><Werte>`UV`, `NUV`</Werte> |
| <span className="hbs-f hbs-e0">[waermenutzung](/bo4e/202610/com/Zaehlwerk#waermenutzung)</span> | Stromverbrauchsart/Wärmenutzung Marktlokation | [Enum Waermenutzung](/bo4e/202610/enum/Waermenutzung)<br/><Werte>`SPEICHERHEIZUNG`, `WAERMEPUMPE`, `DIREKTHEIZUNG`, `WAERMEPUMPE_WAERME_KAELTE`, `WAERMEPUMPE_KAELTE`, `WAERMEPUMPE_WAERME`</Werte> |
| <span className="hbs-g hbs-e0">[konzessionsabgabe](/bo4e/202610/com/Zaehlwerk#konzessionsabgabe)</span> | — | [Konzessionsabgabe](/bo4e/202610/com/Konzessionsabgabe) |
| <span className="hbs-f hbs-e1">[satz](/bo4e/202610/com/Konzessionsabgabe#satz)</span> | Art der Konzessionsabgabe | [Enum AbgabeArt](/bo4e/202610/enum/AbgabeArt)<br/><Werte>`KAS`, `SA`, `SAS`, `TA`, `TAS`, `TK`, `TKS`, `TS`, `TSS`</Werte> |
| <span className="hbs-f hbs-e1">[kosten](/bo4e/202610/com/Konzessionsabgabe#kosten)</span> | Kosten | number (float) |
| <span className="hbs-f hbs-e1">[kategorie](/bo4e/202610/com/Konzessionsabgabe#kategorie)</span> | Kategorie | string |
| <span className="hbs-f hbs-e0">[steuerbefreit](/bo4e/202610/com/Zaehlwerk#steuerbefreit)</span> | steuerbefreit | boolean |
| <span className="hbs-f hbs-e0">[vorkommastelle](/bo4e/202610/com/Zaehlwerk#vorkommastelle)</span> | vorkommastelle | integer |
| <span className="hbs-f hbs-e0">[nachkommastelle](/bo4e/202610/com/Zaehlwerk#nachkommastelle)</span> | nachkommastelle | integer |
| <span className="hbs-f hbs-e0">[abrechnungsrelevant](/bo4e/202610/com/Zaehlwerk#abrechnungsrelevant)</span> | abrechnungsrelevant | boolean |
| <span className="hbs-f hbs-e0">[anzahlAblesungen](/bo4e/202610/com/Zaehlwerk#anzahlablesungen)</span> | anzahlAblesungen | integer |
| <span className="hbs-g hbs-e0">[zaehlzeiten](/bo4e/202610/com/Zaehlwerk#zaehlzeiten)</span> | — | [Zaehlzeitregister](/bo4e/202610/com/Zaehlzeitregister) |
| <span className="hbs-f hbs-e1">[register](/bo4e/202610/com/Zaehlzeitregister#register)</span> | Zählzeitregister | string |
| <span className="hbs-f hbs-e1">[zaehlzeitDefinition](/bo4e/202610/com/Zaehlzeitregister#zaehlzeitdefinition)</span> | Zählzeitdefinition | string |
| <span className="hbs-f hbs-e1">[schwachlastfaehig](/bo4e/202610/com/Zaehlzeitregister#schwachlastfaehig)</span> | Schwachlastfähigkeit des Registers | [Enum Schwachlastfaehig](/bo4e/202610/enum/Schwachlastfaehig)<br/><Werte>`SCHWACHLASTFAEHIG`, `NICHT_SCHWACHLASTFAEHIG`</Werte> |
| <span className="hbs-f hbs-e0">[konfiguration](/bo4e/202610/com/Zaehlwerk#konfiguration)</span> | Konfiguration (iMSys) des Zählwerks | string |
| <span className="hbs-f hbs-e0">[messprodukt](/bo4e/202610/com/Zaehlwerk#messprodukt)</span> | messprodukt | string |
| <span className="hbs-f hbs-e0">[wertegranularitaet](/bo4e/202610/com/Zaehlwerk#wertegranularitaet)</span> | Wertegranularitaet | [Enum Wertegranularitaet](/bo4e/202610/enum/Wertegranularitaet)<br/><Werte>`JAEHRLICH`, `HALBJAEHRLICH`, `QUARTALSWEISE`, `MONATLICH`</Werte> |
| <span className="hbs-f hbs-e0">[notwendigkeitZweiteMessung](/bo4e/202610/com/Zaehlwerk#notwendigkeitzweitemessung)</span> | NotwendigkeitZweiteMessung | [Enum NotwendigkeitZweiteMessung](/bo4e/202610/enum/NotwendigkeitZweiteMessung)<br/><Werte>`VORHANDEN`, `NICHT_VORHANDEN`</Werte> |
| <span className="hbs-f hbs-e0">[werteuebermittlungVerwendungszweck](/bo4e/202610/com/Zaehlwerk#werteuebermittlungverwendungszweck)</span> | WerteuebermittlungVerwendungszweck | [Enum WerteuebermittlungVerwendungszweck](/bo4e/202610/enum/WerteuebermittlungVerwendungszweck)<br/><Werte>`VORHANDEN`, `NICHT_VORHANDEN`</Werte> |
| <span className="hbs-f hbs-e0">[artEMobilitaet](/bo4e/202610/com/Zaehlwerk#artemobilitaet)</span> | ArtEmobilitaet | [Enum ArtEmobilitaet](/bo4e/202610/enum/ArtEmobilitaet)<br/><Werte>`WB`, `LS`, `LP`</Werte> |
| <span className="hbs-f hbs-e0">[konfigurationsprodukt](/bo4e/202610/com/Zaehlwerk#konfigurationsprodukt)</span> | konfigurationsprodukt | string |
| <span className="hbs-f hbs-e0">[keinKonfigurationsprodukt](/bo4e/202610/com/Zaehlwerk#keinkonfigurationsprodukt)</span> | keinKonfigurationsprodukt | boolean |
| <span className="hbs-f hbs-e0">[leistungskurvendefinition](/bo4e/202610/com/Zaehlwerk#leistungskurvendefinition)</span> | leistungskurvendefinition | string |
| <span className="hbs-g hbs-e0">[verwendungszwecke](/bo4e/202610/com/Zaehlwerk#verwendungszwecke) <span className="hbs-liste">[ ]</span></span> | Verwendungungszweck der Werte Marktlokation | [Verwendungszweck[]](/bo4e/202610/com/Verwendungszweck) |
| <span className="hbs-f hbs-e1">[marktrolle](/bo4e/202610/com/Verwendungszweck#marktrolle)</span> | Diese Rollen kann ein Marktteilnehmer einnehmen | [Enum Marktrolle](/bo4e/202610/enum/Marktrolle)<br/><Werte>`NB`, `LF`, `MSB`, `MSBA`, `GMSB`, `MDL`, `DL`, `BKV`, `UENB`, `KUNDE-SELBST-NN`, `MGV`, `EIV`, `RB`, `KUNDE`, `INTERESSENT`, `KN`, `UBA`, `BIKO`, `ESA`</Werte> |
| <span className="hbs-f hbs-e1">[zweck](/bo4e/202610/com/Verwendungszweck#zweck) <span className="hbs-liste">[ ]</span></span> | zweck | [Enum VerwendungszweckValue[]](/bo4e/202610/enum/VerwendungszweckValue)<br/><Werte>`NETZNUTZUNGSABRECHNUNG`, `BILANZKREISABRECHNUNG`, `MEHRMINDERMENGENABRECHNUNG`, `ENDKUNDENABRECHNUNG`, `UEBERMITTLUNG_AN_DAS_HKNR`, `BLINDARBEITSABRECHNUNG`, `ERMITTLUNG_AUSGEGLICHENHEIT_BILANZKREIS`, `BLINDARBEITABRECHNUNG_BETRIEBSFUEHRUNG`, `ES_LIEGT_KEIN_VERWENDUNGSZWECK_VOR`</Werte> |
| <span className="hbs-f hbs-e0">[verwendungszweckNB](/bo4e/202610/com/Zaehlwerk#verwendungszwecknb)</span> | Codes gemäß Codeliste der Verwendungszwecke Verwendungszweck NB | string |
| <span className="hbs-f hbs-e0">[verwendungszweckLF](/bo4e/202610/com/Zaehlwerk#verwendungszwecklf)</span> | Codes gemäß Codeliste der Verwendungszwecke Verwendungszweck LF | string |
| <span className="hbs-f hbs-e0">[verwendungszweckUENB](/bo4e/202610/com/Zaehlwerk#verwendungszweckuenb)</span> | Codes gemäß Codeliste der Verwendungszwecke Verwendungszweck ÜNB | string |
| <span className="hbs-f hbs-e0">[keinProdukt](/bo4e/202610/com/Zaehlwerk#keinprodukt)</span> | CCI+11++ZF6: keinProdukt zugeordnet | boolean |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### bezeichnung

22 Verwendung(en) in den Nachrichtentypen UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_44002](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_44013](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_44014](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_44035](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44035) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_44060](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44060) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_44116](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44116) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_44117](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44117) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_44143](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44143) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_44145](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44145) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_44147](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44147) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_44149](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44149) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_44168](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55553](/schnittstellen/202610/pruefi/UTILMD/PI_55553) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55555](/schnittstellen/202610/pruefi/UTILMD/PI_55555) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55643](/schnittstellen/202610/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55648](/schnittstellen/202610/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55653](/schnittstellen/202610/pruefi/UTILMD/PI_55653) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55658](/schnittstellen/202610/pruefi/UTILMD/PI_55658) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55663](/schnittstellen/202610/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55669](/schnittstellen/202610/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |

### obisKennzahl

75 Verwendung(en) in den Nachrichtentypen QUOTES, UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_15003](/schnittstellen/202610/pruefi/QUOTES/PI_15003) | Prüfi | QUOTES | stammdaten › WERTE_NACH_TYP2 › zaehlwerke |
| [PI_44002](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_44002](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_44013](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_44013](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_44014](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_44014](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_44035](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44035) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_44035](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44035) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_44043](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44043) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_44060](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44060) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_44112](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44112) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_44116](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44116) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_44117](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44117) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_44139](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44139) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_44142](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44142) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_44143](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44143) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_44145](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44145) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_44147](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44147) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_44149](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44149) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_44168](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55035](/schnittstellen/202610/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55035](/schnittstellen/202610/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › NETZLOKATION › zaehlwerke |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55060](/schnittstellen/202610/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55060](/schnittstellen/202610/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › NETZLOKATION › zaehlwerke |
| [PI_55060](/schnittstellen/202610/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55074](/schnittstellen/202610/pruefi/UTILMD/PI_55074) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55074](/schnittstellen/202610/pruefi/UTILMD/PI_55074) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke |
| [PI_55074](/schnittstellen/202610/pruefi/UTILMD/PI_55074) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55075](/schnittstellen/202610/pruefi/UTILMD/PI_55075) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55075](/schnittstellen/202610/pruefi/UTILMD/PI_55075) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke |
| [PI_55075](/schnittstellen/202610/pruefi/UTILMD/PI_55075) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55095](/schnittstellen/202610/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55095](/schnittstellen/202610/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke |
| [PI_55095](/schnittstellen/202610/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › NETZLOKATION › zaehlwerke |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › NETZLOKATION › zaehlwerke |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55553](/schnittstellen/202610/pruefi/UTILMD/PI_55553) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55553](/schnittstellen/202610/pruefi/UTILMD/PI_55553) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55555](/schnittstellen/202610/pruefi/UTILMD/PI_55555) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55555](/schnittstellen/202610/pruefi/UTILMD/PI_55555) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55622](/schnittstellen/202610/pruefi/UTILMD/PI_55622) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55639](/schnittstellen/202610/pruefi/UTILMD/PI_55639) | Prüfi | UTILMD | stammdaten › NETZLOKATION › zaehlwerke |
| [PI_55640](/schnittstellen/202610/pruefi/UTILMD/PI_55640) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55642](/schnittstellen/202610/pruefi/UTILMD/PI_55642) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke |
| [PI_55643](/schnittstellen/202610/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55644](/schnittstellen/202610/pruefi/UTILMD/PI_55644) | Prüfi | UTILMD | stammdaten › NETZLOKATION › zaehlwerke |
| [PI_55645](/schnittstellen/202610/pruefi/UTILMD/PI_55645) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55647](/schnittstellen/202610/pruefi/UTILMD/PI_55647) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke |
| [PI_55648](/schnittstellen/202610/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55649](/schnittstellen/202610/pruefi/UTILMD/PI_55649) | Prüfi | UTILMD | stammdaten › NETZLOKATION › zaehlwerke |
| [PI_55650](/schnittstellen/202610/pruefi/UTILMD/PI_55650) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55652](/schnittstellen/202610/pruefi/UTILMD/PI_55652) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke |
| [PI_55653](/schnittstellen/202610/pruefi/UTILMD/PI_55653) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55654](/schnittstellen/202610/pruefi/UTILMD/PI_55654) | Prüfi | UTILMD | stammdaten › NETZLOKATION › zaehlwerke |
| [PI_55655](/schnittstellen/202610/pruefi/UTILMD/PI_55655) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55657](/schnittstellen/202610/pruefi/UTILMD/PI_55657) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke |
| [PI_55658](/schnittstellen/202610/pruefi/UTILMD/PI_55658) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55659](/schnittstellen/202610/pruefi/UTILMD/PI_55659) | Prüfi | UTILMD | stammdaten › NETZLOKATION › zaehlwerke |
| [PI_55660](/schnittstellen/202610/pruefi/UTILMD/PI_55660) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55662](/schnittstellen/202610/pruefi/UTILMD/PI_55662) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke |
| [PI_55663](/schnittstellen/202610/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55664](/schnittstellen/202610/pruefi/UTILMD/PI_55664) | Prüfi | UTILMD | stammdaten › NETZLOKATION › zaehlwerke |
| [PI_55665](/schnittstellen/202610/pruefi/UTILMD/PI_55665) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55667](/schnittstellen/202610/pruefi/UTILMD/PI_55667) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke |
| [PI_55669](/schnittstellen/202610/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55684](/schnittstellen/202610/pruefi/UTILMD/PI_55684) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55686](/schnittstellen/202610/pruefi/UTILMD/PI_55686) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke |

### verbrauchsart

1 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55622](/schnittstellen/202610/pruefi/UTILMD/PI_55622) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |

### unterbrechbarkeit

1 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55622](/schnittstellen/202610/pruefi/UTILMD/PI_55622) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |

### waermenutzung

1 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55622](/schnittstellen/202610/pruefi/UTILMD/PI_55622) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |

### vorkommastelle

26 Verwendung(en) in den Nachrichtentypen UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_44002](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_44013](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_44014](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_44035](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44035) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_44043](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44043) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_44060](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44060) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_44116](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44116) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_44117](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44117) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_44143](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44143) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_44145](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44145) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_44147](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44147) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_44149](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44149) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_44168](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55074](/schnittstellen/202610/pruefi/UTILMD/PI_55074) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55075](/schnittstellen/202610/pruefi/UTILMD/PI_55075) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55553](/schnittstellen/202610/pruefi/UTILMD/PI_55553) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55555](/schnittstellen/202610/pruefi/UTILMD/PI_55555) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55643](/schnittstellen/202610/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55648](/schnittstellen/202610/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55653](/schnittstellen/202610/pruefi/UTILMD/PI_55653) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55658](/schnittstellen/202610/pruefi/UTILMD/PI_55658) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55663](/schnittstellen/202610/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55669](/schnittstellen/202610/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |

### nachkommastelle

26 Verwendung(en) in den Nachrichtentypen UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_44002](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_44013](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_44014](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_44035](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44035) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_44043](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44043) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_44060](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44060) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_44116](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44116) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_44117](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44117) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_44143](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44143) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_44145](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44145) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_44147](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44147) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_44149](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44149) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_44168](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55074](/schnittstellen/202610/pruefi/UTILMD/PI_55074) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55075](/schnittstellen/202610/pruefi/UTILMD/PI_55075) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55553](/schnittstellen/202610/pruefi/UTILMD/PI_55553) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55555](/schnittstellen/202610/pruefi/UTILMD/PI_55555) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55643](/schnittstellen/202610/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55648](/schnittstellen/202610/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55653](/schnittstellen/202610/pruefi/UTILMD/PI_55653) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55658](/schnittstellen/202610/pruefi/UTILMD/PI_55658) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55663](/schnittstellen/202610/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55669](/schnittstellen/202610/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |

### konfiguration

16 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55035](/schnittstellen/202610/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55060](/schnittstellen/202610/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55074](/schnittstellen/202610/pruefi/UTILMD/PI_55074) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55075](/schnittstellen/202610/pruefi/UTILMD/PI_55075) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55095](/schnittstellen/202610/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55553](/schnittstellen/202610/pruefi/UTILMD/PI_55553) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55555](/schnittstellen/202610/pruefi/UTILMD/PI_55555) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55643](/schnittstellen/202610/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55648](/schnittstellen/202610/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55653](/schnittstellen/202610/pruefi/UTILMD/PI_55653) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55658](/schnittstellen/202610/pruefi/UTILMD/PI_55658) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55663](/schnittstellen/202610/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55669](/schnittstellen/202610/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |

### messprodukt

25 Verwendung(en) in den Nachrichtentypen ORDERS, UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_17118](/schnittstellen/202610/pruefi/ORDERS/PI_17118) | Prüfi | ORDERS | stammdaten › MESSLOKATION › zaehlwerke |
| [PI_17121](/schnittstellen/202610/pruefi/ORDERS/PI_17121) | Prüfi | ORDERS | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_17121](/schnittstellen/202610/pruefi/ORDERS/PI_17121) | Prüfi | ORDERS | stammdaten › MESSLOKATION › zaehlwerke |
| [PI_17121](/schnittstellen/202610/pruefi/ORDERS/PI_17121) | Prüfi | ORDERS | stammdaten › NETZLOKATION › zaehlwerke |
| [PI_17121](/schnittstellen/202610/pruefi/ORDERS/PI_17121) | Prüfi | ORDERS | stammdaten › TRANCHE › zaehlwerke |
| [PI_17123](/schnittstellen/202610/pruefi/ORDERS/PI_17123) | Prüfi | ORDERS | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_17134](/schnittstellen/202610/pruefi/ORDERS/PI_17134) | Prüfi | ORDERS | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_17134](/schnittstellen/202610/pruefi/ORDERS/PI_17134) | Prüfi | ORDERS | stammdaten › MESSLOKATION › zaehlwerke |
| [PI_17134](/schnittstellen/202610/pruefi/ORDERS/PI_17134) | Prüfi | ORDERS | stammdaten › TRANCHE › zaehlwerke |
| [PI_17135](/schnittstellen/202610/pruefi/ORDERS/PI_17135) | Prüfi | ORDERS | stammdaten › MESSLOKATION › zaehlwerke |
| [PI_44043](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44043) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › zaehlwerke |
| [PI_44060](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44060) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › zaehlwerke |
| [PI_44168](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | stammdaten › MESSLOKATION › zaehlwerke |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › MESSLOKATION › zaehlwerke |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke |
| [PI_55060](/schnittstellen/202610/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55060](/schnittstellen/202610/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › MESSLOKATION › zaehlwerke |
| [PI_55060](/schnittstellen/202610/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › MESSLOKATION › zaehlwerke |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › MESSLOKATION › zaehlwerke |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke |

### wertegranularitaet

50 Verwendung(en) in den Nachrichtentypen UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_44002](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_44002](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_44013](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_44013](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_44014](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_44014](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_44035](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44035) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_44035](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44035) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_44043](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44043) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_44060](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44060) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_44112](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44112) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_44116](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44116) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_44117](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44117) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_44139](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44139) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_44142](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44142) | Prüfi | UTILMD_GAS | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_44143](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44143) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_44145](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44145) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_44147](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44147) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_44149](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44149) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_44168](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44168) | Prüfi | UTILMD_GAS | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55035](/schnittstellen/202610/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55035](/schnittstellen/202610/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55060](/schnittstellen/202610/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55060](/schnittstellen/202610/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55074](/schnittstellen/202610/pruefi/UTILMD/PI_55074) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55075](/schnittstellen/202610/pruefi/UTILMD/PI_55075) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55095](/schnittstellen/202610/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55095](/schnittstellen/202610/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55553](/schnittstellen/202610/pruefi/UTILMD/PI_55553) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55553](/schnittstellen/202610/pruefi/UTILMD/PI_55553) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55555](/schnittstellen/202610/pruefi/UTILMD/PI_55555) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55555](/schnittstellen/202610/pruefi/UTILMD/PI_55555) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55640](/schnittstellen/202610/pruefi/UTILMD/PI_55640) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55643](/schnittstellen/202610/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55645](/schnittstellen/202610/pruefi/UTILMD/PI_55645) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55648](/schnittstellen/202610/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55650](/schnittstellen/202610/pruefi/UTILMD/PI_55650) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55653](/schnittstellen/202610/pruefi/UTILMD/PI_55653) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55655](/schnittstellen/202610/pruefi/UTILMD/PI_55655) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55658](/schnittstellen/202610/pruefi/UTILMD/PI_55658) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55660](/schnittstellen/202610/pruefi/UTILMD/PI_55660) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55663](/schnittstellen/202610/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |
| [PI_55665](/schnittstellen/202610/pruefi/UTILMD/PI_55665) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55669](/schnittstellen/202610/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke |

### notwendigkeitZweiteMessung

6 Verwendung(en) in den Nachrichtentypen ORDERS, UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_17118](/schnittstellen/202610/pruefi/ORDERS/PI_17118) | Prüfi | ORDERS | stammdaten › MESSLOKATION › zaehlwerke |
| [PI_17121](/schnittstellen/202610/pruefi/ORDERS/PI_17121) | Prüfi | ORDERS | stammdaten › MESSLOKATION › zaehlwerke |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › MESSLOKATION › zaehlwerke |
| [PI_55060](/schnittstellen/202610/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › MESSLOKATION › zaehlwerke |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › MESSLOKATION › zaehlwerke |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › MESSLOKATION › zaehlwerke |

### werteuebermittlungVerwendungszweck

6 Verwendung(en) in den Nachrichtentypen ORDERS, UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_17118](/schnittstellen/202610/pruefi/ORDERS/PI_17118) | Prüfi | ORDERS | stammdaten › MESSLOKATION › zaehlwerke |
| [PI_17121](/schnittstellen/202610/pruefi/ORDERS/PI_17121) | Prüfi | ORDERS | stammdaten › MESSLOKATION › zaehlwerke |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › MESSLOKATION › zaehlwerke |
| [PI_55060](/schnittstellen/202610/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › MESSLOKATION › zaehlwerke |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › MESSLOKATION › zaehlwerke |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › MESSLOKATION › zaehlwerke |

### artEMobilitaet

1 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55622](/schnittstellen/202610/pruefi/UTILMD/PI_55622) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |

### verwendungszweckNB

37 Verwendung(en) in den Nachrichtentypen ORDERS, UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_17121](/schnittstellen/202610/pruefi/ORDERS/PI_17121) | Prüfi | ORDERS | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_17121](/schnittstellen/202610/pruefi/ORDERS/PI_17121) | Prüfi | ORDERS | stammdaten › NETZLOKATION › zaehlwerke |
| [PI_17121](/schnittstellen/202610/pruefi/ORDERS/PI_17121) | Prüfi | ORDERS | stammdaten › TRANCHE › zaehlwerke |
| [PI_17134](/schnittstellen/202610/pruefi/ORDERS/PI_17134) | Prüfi | ORDERS | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_17134](/schnittstellen/202610/pruefi/ORDERS/PI_17134) | Prüfi | ORDERS | stammdaten › TRANCHE › zaehlwerke |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › NETZLOKATION › zaehlwerke |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke |
| [PI_55060](/schnittstellen/202610/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55060](/schnittstellen/202610/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › NETZLOKATION › zaehlwerke |
| [PI_55060](/schnittstellen/202610/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › NETZLOKATION › zaehlwerke |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › NETZLOKATION › zaehlwerke |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke |
| [PI_55639](/schnittstellen/202610/pruefi/UTILMD/PI_55639) | Prüfi | UTILMD | stammdaten › NETZLOKATION › zaehlwerke |
| [PI_55640](/schnittstellen/202610/pruefi/UTILMD/PI_55640) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55642](/schnittstellen/202610/pruefi/UTILMD/PI_55642) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke |
| [PI_55644](/schnittstellen/202610/pruefi/UTILMD/PI_55644) | Prüfi | UTILMD | stammdaten › NETZLOKATION › zaehlwerke |
| [PI_55645](/schnittstellen/202610/pruefi/UTILMD/PI_55645) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55647](/schnittstellen/202610/pruefi/UTILMD/PI_55647) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke |
| [PI_55649](/schnittstellen/202610/pruefi/UTILMD/PI_55649) | Prüfi | UTILMD | stammdaten › NETZLOKATION › zaehlwerke |
| [PI_55650](/schnittstellen/202610/pruefi/UTILMD/PI_55650) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55652](/schnittstellen/202610/pruefi/UTILMD/PI_55652) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke |
| [PI_55654](/schnittstellen/202610/pruefi/UTILMD/PI_55654) | Prüfi | UTILMD | stammdaten › NETZLOKATION › zaehlwerke |
| [PI_55655](/schnittstellen/202610/pruefi/UTILMD/PI_55655) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55657](/schnittstellen/202610/pruefi/UTILMD/PI_55657) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke |
| [PI_55659](/schnittstellen/202610/pruefi/UTILMD/PI_55659) | Prüfi | UTILMD | stammdaten › NETZLOKATION › zaehlwerke |
| [PI_55660](/schnittstellen/202610/pruefi/UTILMD/PI_55660) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55662](/schnittstellen/202610/pruefi/UTILMD/PI_55662) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke |
| [PI_55664](/schnittstellen/202610/pruefi/UTILMD/PI_55664) | Prüfi | UTILMD | stammdaten › NETZLOKATION › zaehlwerke |
| [PI_55665](/schnittstellen/202610/pruefi/UTILMD/PI_55665) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55667](/schnittstellen/202610/pruefi/UTILMD/PI_55667) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke |
| [PI_55684](/schnittstellen/202610/pruefi/UTILMD/PI_55684) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55686](/schnittstellen/202610/pruefi/UTILMD/PI_55686) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke |

### verwendungszweckLF

37 Verwendung(en) in den Nachrichtentypen ORDERS, UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_17121](/schnittstellen/202610/pruefi/ORDERS/PI_17121) | Prüfi | ORDERS | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_17121](/schnittstellen/202610/pruefi/ORDERS/PI_17121) | Prüfi | ORDERS | stammdaten › NETZLOKATION › zaehlwerke |
| [PI_17121](/schnittstellen/202610/pruefi/ORDERS/PI_17121) | Prüfi | ORDERS | stammdaten › TRANCHE › zaehlwerke |
| [PI_17134](/schnittstellen/202610/pruefi/ORDERS/PI_17134) | Prüfi | ORDERS | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_17134](/schnittstellen/202610/pruefi/ORDERS/PI_17134) | Prüfi | ORDERS | stammdaten › TRANCHE › zaehlwerke |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › NETZLOKATION › zaehlwerke |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke |
| [PI_55060](/schnittstellen/202610/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55060](/schnittstellen/202610/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › NETZLOKATION › zaehlwerke |
| [PI_55060](/schnittstellen/202610/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › NETZLOKATION › zaehlwerke |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › NETZLOKATION › zaehlwerke |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke |
| [PI_55639](/schnittstellen/202610/pruefi/UTILMD/PI_55639) | Prüfi | UTILMD | stammdaten › NETZLOKATION › zaehlwerke |
| [PI_55640](/schnittstellen/202610/pruefi/UTILMD/PI_55640) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55642](/schnittstellen/202610/pruefi/UTILMD/PI_55642) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke |
| [PI_55644](/schnittstellen/202610/pruefi/UTILMD/PI_55644) | Prüfi | UTILMD | stammdaten › NETZLOKATION › zaehlwerke |
| [PI_55645](/schnittstellen/202610/pruefi/UTILMD/PI_55645) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55647](/schnittstellen/202610/pruefi/UTILMD/PI_55647) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke |
| [PI_55649](/schnittstellen/202610/pruefi/UTILMD/PI_55649) | Prüfi | UTILMD | stammdaten › NETZLOKATION › zaehlwerke |
| [PI_55650](/schnittstellen/202610/pruefi/UTILMD/PI_55650) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55652](/schnittstellen/202610/pruefi/UTILMD/PI_55652) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke |
| [PI_55654](/schnittstellen/202610/pruefi/UTILMD/PI_55654) | Prüfi | UTILMD | stammdaten › NETZLOKATION › zaehlwerke |
| [PI_55655](/schnittstellen/202610/pruefi/UTILMD/PI_55655) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55657](/schnittstellen/202610/pruefi/UTILMD/PI_55657) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke |
| [PI_55659](/schnittstellen/202610/pruefi/UTILMD/PI_55659) | Prüfi | UTILMD | stammdaten › NETZLOKATION › zaehlwerke |
| [PI_55660](/schnittstellen/202610/pruefi/UTILMD/PI_55660) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55662](/schnittstellen/202610/pruefi/UTILMD/PI_55662) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke |
| [PI_55664](/schnittstellen/202610/pruefi/UTILMD/PI_55664) | Prüfi | UTILMD | stammdaten › NETZLOKATION › zaehlwerke |
| [PI_55665](/schnittstellen/202610/pruefi/UTILMD/PI_55665) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55667](/schnittstellen/202610/pruefi/UTILMD/PI_55667) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke |
| [PI_55684](/schnittstellen/202610/pruefi/UTILMD/PI_55684) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55686](/schnittstellen/202610/pruefi/UTILMD/PI_55686) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke |

### verwendungszweckUENB

26 Verwendung(en) in den Nachrichtentypen ORDERS, UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_17121](/schnittstellen/202610/pruefi/ORDERS/PI_17121) | Prüfi | ORDERS | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_17121](/schnittstellen/202610/pruefi/ORDERS/PI_17121) | Prüfi | ORDERS | stammdaten › TRANCHE › zaehlwerke |
| [PI_17134](/schnittstellen/202610/pruefi/ORDERS/PI_17134) | Prüfi | ORDERS | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_17134](/schnittstellen/202610/pruefi/ORDERS/PI_17134) | Prüfi | ORDERS | stammdaten › TRANCHE › zaehlwerke |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke |
| [PI_55060](/schnittstellen/202610/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55060](/schnittstellen/202610/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke |
| [PI_55640](/schnittstellen/202610/pruefi/UTILMD/PI_55640) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55642](/schnittstellen/202610/pruefi/UTILMD/PI_55642) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke |
| [PI_55645](/schnittstellen/202610/pruefi/UTILMD/PI_55645) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55647](/schnittstellen/202610/pruefi/UTILMD/PI_55647) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke |
| [PI_55650](/schnittstellen/202610/pruefi/UTILMD/PI_55650) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55652](/schnittstellen/202610/pruefi/UTILMD/PI_55652) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke |
| [PI_55655](/schnittstellen/202610/pruefi/UTILMD/PI_55655) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55657](/schnittstellen/202610/pruefi/UTILMD/PI_55657) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke |
| [PI_55660](/schnittstellen/202610/pruefi/UTILMD/PI_55660) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55662](/schnittstellen/202610/pruefi/UTILMD/PI_55662) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke |
| [PI_55665](/schnittstellen/202610/pruefi/UTILMD/PI_55665) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55667](/schnittstellen/202610/pruefi/UTILMD/PI_55667) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke |
| [PI_55684](/schnittstellen/202610/pruefi/UTILMD/PI_55684) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke |
| [PI_55686](/schnittstellen/202610/pruefi/UTILMD/PI_55686) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke |

### keinProdukt

10 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › NETZLOKATION › zaehlwerke |
| [PI_55060](/schnittstellen/202610/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › NETZLOKATION › zaehlwerke |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › NETZLOKATION › zaehlwerke |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › NETZLOKATION › zaehlwerke |
| [PI_55639](/schnittstellen/202610/pruefi/UTILMD/PI_55639) | Prüfi | UTILMD | stammdaten › NETZLOKATION › zaehlwerke |
| [PI_55644](/schnittstellen/202610/pruefi/UTILMD/PI_55644) | Prüfi | UTILMD | stammdaten › NETZLOKATION › zaehlwerke |
| [PI_55649](/schnittstellen/202610/pruefi/UTILMD/PI_55649) | Prüfi | UTILMD | stammdaten › NETZLOKATION › zaehlwerke |
| [PI_55654](/schnittstellen/202610/pruefi/UTILMD/PI_55654) | Prüfi | UTILMD | stammdaten › NETZLOKATION › zaehlwerke |
| [PI_55659](/schnittstellen/202610/pruefi/UTILMD/PI_55659) | Prüfi | UTILMD | stammdaten › NETZLOKATION › zaehlwerke |
| [PI_55664](/schnittstellen/202610/pruefi/UTILMD/PI_55664) | Prüfi | UTILMD | stammdaten › NETZLOKATION › zaehlwerke |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
