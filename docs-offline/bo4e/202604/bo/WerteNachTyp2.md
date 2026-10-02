# WerteNachTyp2
<span hidden data-pagefind-meta={"title:WerteNachTyp2 — BO4E-Geschäftsobjekt (FV 202604)"} />

BO4E-Geschäftsobjekt · 10 Felder · 12 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="botyp"></a>`boTyp` <span className="hbs-pflicht">\*</span> | [Enum BOTyp](/bo4e/202604/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> | Typ des BO |
| <a id="versionstruktur"></a>`versionStruktur` <span className="hbs-pflicht">\*</span> | string | versionStruktur |
| <a id="konfigurationsprodukt"></a>`konfigurationsprodukt` | string | konfigurationsprodukt |
| <a id="messprodukt"></a>`messprodukt` | string | messprodukt |
| <a id="zieladresse"></a>`zieladresse` | [Zieladresse](/bo4e/202604/com/Zieladresse) | — |
| <a id="aussteller"></a>`aussteller` | [Aussteller](/bo4e/202604/com/Aussteller) | — |
| <a id="zertifikatsnutzer"></a>`zertifikatsNutzer` | [ZertifikatsNutzer](/bo4e/202604/com/ZertifikatsNutzer) | — |
| <a id="aenderungsmoeglichkeitkonfiguration"></a>`aenderungsmoeglichkeitKonfiguration` | [Enum AenderungsmoeglichkeitKonfiguration](/bo4e/202604/enum/AenderungsmoeglichkeitKonfiguration)<br/><Werte>`ERFORDERLICH`, `NICHT_ERFORDERLICH`</Werte> | AenderungsmoeglichkeitKonfiguration |
| <a id="schwellwerte"></a>`schwellwerte` | [Schwellwert[]](/bo4e/202604/com/Schwellwert) | schwellwerte |
| <a id="zaehlwerke"></a>`zaehlwerke` | [Zaehlwerk[]](/bo4e/202604/com/Zaehlwerk) | Zählwerke |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[boTyp](/bo4e/202604/bo/WerteNachTyp2#botyp) <span className="hbs-pflicht">\*</span></span> | Typ des BO | [Enum BOTyp](/bo4e/202604/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> |
| <span className="hbs-f hbs-e0">[versionStruktur](/bo4e/202604/bo/WerteNachTyp2#versionstruktur) <span className="hbs-pflicht">\*</span></span> | versionStruktur | string |
| <span className="hbs-f hbs-e0">[konfigurationsprodukt](/bo4e/202604/bo/WerteNachTyp2#konfigurationsprodukt)</span> | konfigurationsprodukt | string |
| <span className="hbs-f hbs-e0">[messprodukt](/bo4e/202604/bo/WerteNachTyp2#messprodukt)</span> | messprodukt | string |
| <span className="hbs-g hbs-e0">[zieladresse](/bo4e/202604/bo/WerteNachTyp2#zieladresse)</span> | — | [Zieladresse](/bo4e/202604/com/Zieladresse) |
| <span className="hbs-f hbs-e1">[zieladresse1](/bo4e/202604/com/Zieladresse#zieladresse1)</span> | zieladresse1 | string |
| <span className="hbs-f hbs-e1">[zieladresse2](/bo4e/202604/com/Zieladresse#zieladresse2)</span> | zieladresse2 | string |
| <span className="hbs-f hbs-e1">[zieladresse3](/bo4e/202604/com/Zieladresse#zieladresse3)</span> | zieladresse3 | string |
| <span className="hbs-f hbs-e1">[zieladresse4](/bo4e/202604/com/Zieladresse#zieladresse4)</span> | zieladresse4 | string |
| <span className="hbs-f hbs-e1">[zieladresse5](/bo4e/202604/com/Zieladresse#zieladresse5)</span> | zieladresse5 | string |
| <span className="hbs-g hbs-e0">[aussteller](/bo4e/202604/bo/WerteNachTyp2#aussteller)</span> | — | [Aussteller](/bo4e/202604/com/Aussteller) |
| <span className="hbs-f hbs-e1">[aussteller1](/bo4e/202604/com/Aussteller#aussteller1)</span> | aussteller1 | string |
| <span className="hbs-f hbs-e1">[aussteller2](/bo4e/202604/com/Aussteller#aussteller2)</span> | aussteller2 | string |
| <span className="hbs-f hbs-e1">[aussteller3](/bo4e/202604/com/Aussteller#aussteller3)</span> | aussteller3 | string |
| <span className="hbs-f hbs-e1">[aussteller4](/bo4e/202604/com/Aussteller#aussteller4)</span> | aussteller4 | string |
| <span className="hbs-f hbs-e1">[aussteller5](/bo4e/202604/com/Aussteller#aussteller5)</span> | aussteller5 | string |
| <span className="hbs-g hbs-e0">[zertifikatsNutzer](/bo4e/202604/bo/WerteNachTyp2#zertifikatsnutzer)</span> | — | [ZertifikatsNutzer](/bo4e/202604/com/ZertifikatsNutzer) |
| <span className="hbs-f hbs-e1">[zertifikatsNutzer1](/bo4e/202604/com/ZertifikatsNutzer#zertifikatsnutzer1)</span> | zertifikatsNutzer1 | string |
| <span className="hbs-f hbs-e1">[zertifikatsNutzer2](/bo4e/202604/com/ZertifikatsNutzer#zertifikatsnutzer2)</span> | zertifikatsNutzer2 | string |
| <span className="hbs-f hbs-e1">[zertifikatsNutzer3](/bo4e/202604/com/ZertifikatsNutzer#zertifikatsnutzer3)</span> | zertifikatsNutzer3 | string |
| <span className="hbs-f hbs-e1">[zertifikatsNutzer4](/bo4e/202604/com/ZertifikatsNutzer#zertifikatsnutzer4)</span> | zertifikatsNutzer4 | string |
| <span className="hbs-f hbs-e1">[zertifikatsNutzer5](/bo4e/202604/com/ZertifikatsNutzer#zertifikatsnutzer5)</span> | zertifikatsNutzer5 | string |
| <span className="hbs-f hbs-e0">[aenderungsmoeglichkeitKonfiguration](/bo4e/202604/bo/WerteNachTyp2#aenderungsmoeglichkeitkonfiguration)</span> | AenderungsmoeglichkeitKonfiguration | [Enum AenderungsmoeglichkeitKonfiguration](/bo4e/202604/enum/AenderungsmoeglichkeitKonfiguration)<br/><Werte>`ERFORDERLICH`, `NICHT_ERFORDERLICH`</Werte> |
| <span className="hbs-g hbs-e0">[schwellwerte](/bo4e/202604/bo/WerteNachTyp2#schwellwerte) <span className="hbs-liste">[ ]</span></span> | schwellwerte | [Schwellwert[]](/bo4e/202604/com/Schwellwert) |
| <span className="hbs-f hbs-e1">[obererSchwellwert](/bo4e/202604/com/Schwellwert#obererschwellwert)</span> | obererSchwellwert | number (float) |
| <span className="hbs-f hbs-e1">[untererSchwellwert](/bo4e/202604/com/Schwellwert#untererschwellwert)</span> | untererSchwellwert | number (float) |
| <span className="hbs-f hbs-e1">[konfigurationsprodukt](/bo4e/202604/com/Schwellwert#konfigurationsprodukt)</span> | konfigurationsprodukt | string |
| <span className="hbs-g hbs-e0">[zaehlwerke](/bo4e/202604/bo/WerteNachTyp2#zaehlwerke) <span className="hbs-liste">[ ]</span></span> | Zählwerke | [Zaehlwerk[]](/bo4e/202604/com/Zaehlwerk) |
| <span className="hbs-f hbs-e1">[zaehlwerkId](/bo4e/202604/com/Zaehlwerk#zaehlwerkid)</span> | Identifikation des Zählwerks (Registers) innerhalb des Zählers. Oftmals eine laufende Nummer hinter der<br/>Zählernummer. Z.B. 47110815_1 | string |
| <span className="hbs-f hbs-e1">[bezeichnung](/bo4e/202604/com/Zaehlwerk#bezeichnung)</span> | Zusätzliche Bezeichnung, z.B. Zählwerk_Wirkarbeit. | string |
| <span className="hbs-f hbs-e1">[richtung](/bo4e/202604/com/Zaehlwerk#richtung)</span> | Die Energierichtung, Einspeisung oder Ausspeisung. Details Energierichtung | [Enum Energierichtung](/bo4e/202604/enum/Energierichtung)<br/><Werte>`AUSSP`, `EINSP`</Werte> |
| <span className="hbs-f hbs-e1">[obisKennzahl](/bo4e/202604/com/Zaehlwerk#obiskennzahl)</span> | Die OBIS-Kennzahl für das Zählwerk, die festlegt, welche auf die gemessene Größe mit dem Stand gemeldet wird.<br/>Nur Zählwerkstände mit dieser OBIS-Kennzahl werden an diesem Zählwerk registriert. Beispiel:1-0:1.8.1 für<br/>elektrische Wirkarbeit. | string |
| <span className="hbs-f hbs-e1">[wandlerfaktor](/bo4e/202604/com/Zaehlwerk#wandlerfaktor)</span> | Mit diesem Faktor wird eine Zählerstandsdifferenz multipliziert, um zum eigentlichen Verbrauch im Zeitraum zu<br/>kommen. | number (float) |
| <span className="hbs-f hbs-e1">[einheit](/bo4e/202604/com/Zaehlwerk#einheit)</span> | Die Einheit der gemessenen Größe, z.B. kWh. Details Mengeneinheit | [Enum Mengeneinheit](/bo4e/202604/enum/Mengeneinheit)<br/><Werte>`W`, `WH`, `KW`, `KWH`, `KVARH`, `MW`, `MWH`, `STUECK`, `KUBIKMETER`, `STUNDE`, `TAG`, `MONAT`, `JAHR`, `PROZENT`, `ANZAHL`, `VAR`, `KVAR`, `VARH`, `KWHK`, `Z16`, `KWT`, `WATT_PRO_QUADRATMETER`, `METER_PRO_SEKUNDE`</Werte> |
| <span className="hbs-f hbs-e1">[schwachlastfaehig](/bo4e/202604/com/Zaehlwerk#schwachlastfaehig)</span> | schwachlastfaehig | [Enum Schwachlastfaehig](/bo4e/202604/enum/Schwachlastfaehig)<br/><Werte>`SCHWACHLASTFAEHIG`, `NICHT_SCHWACHLASTFAEHIG`</Werte> |
| <span className="hbs-f hbs-e1">[verbrauchsart](/bo4e/202604/com/Zaehlwerk#verbrauchsart) <span className="hbs-liste">[ ]</span></span> | Stromverbrauchsart/Verbrauchsart Marktlokation | [Enum Verbrauchsart[]](/bo4e/202604/enum/Verbrauchsart)<br/><Werte>`KL`, `W`, `EMOB`, `SB`, `SW`, `WK`</Werte> |
| <span className="hbs-f hbs-e1">[unterbrechbarkeit](/bo4e/202604/com/Zaehlwerk#unterbrechbarkeit)</span> | Stromverbrauchsart/Unterbrechbarkeit Marktlokation | [Enum Unterbrechbarkeit](/bo4e/202604/enum/Unterbrechbarkeit)<br/><Werte>`UV`, `NUV`</Werte> |
| <span className="hbs-f hbs-e1">[waermenutzung](/bo4e/202604/com/Zaehlwerk#waermenutzung)</span> | Stromverbrauchsart/Wärmenutzung Marktlokation | [Enum Waermenutzung](/bo4e/202604/enum/Waermenutzung)<br/><Werte>`SPEICHERHEIZUNG`, `WAERMEPUMPE`, `DIREKTHEIZUNG`, `WAERMEPUMPE_WAERME_KAELTE`, `WAERMEPUMPE_KAELTE`, `WAERMEPUMPE_WAERME`</Werte> |
| <span className="hbs-g hbs-e1">[konzessionsabgabe](/bo4e/202604/com/Zaehlwerk#konzessionsabgabe)</span> | — | [Konzessionsabgabe](/bo4e/202604/com/Konzessionsabgabe) |
| <span className="hbs-f hbs-e2">[satz](/bo4e/202604/com/Konzessionsabgabe#satz)</span> | Art der Konzessionsabgabe | [Enum AbgabeArt](/bo4e/202604/enum/AbgabeArt)<br/><Werte>`KAS`, `SA`, `SAS`, `TA`, `TAS`, `TK`, `TKS`, `TS`, `TSS`</Werte> |
| <span className="hbs-f hbs-e2">[kosten](/bo4e/202604/com/Konzessionsabgabe#kosten)</span> | Kosten | number (float) |
| <span className="hbs-f hbs-e2">[kategorie](/bo4e/202604/com/Konzessionsabgabe#kategorie)</span> | Kategorie | string |
| <span className="hbs-f hbs-e1">[steuerbefreit](/bo4e/202604/com/Zaehlwerk#steuerbefreit)</span> | steuerbefreit | boolean |
| <span className="hbs-f hbs-e1">[vorkommastelle](/bo4e/202604/com/Zaehlwerk#vorkommastelle)</span> | vorkommastelle | integer |
| <span className="hbs-f hbs-e1">[nachkommastelle](/bo4e/202604/com/Zaehlwerk#nachkommastelle)</span> | nachkommastelle | integer |
| <span className="hbs-f hbs-e1">[abrechnungsrelevant](/bo4e/202604/com/Zaehlwerk#abrechnungsrelevant)</span> | abrechnungsrelevant | boolean |
| <span className="hbs-f hbs-e1">[anzahlAblesungen](/bo4e/202604/com/Zaehlwerk#anzahlablesungen)</span> | anzahlAblesungen | integer |
| <span className="hbs-g hbs-e1">[zaehlzeiten](/bo4e/202604/com/Zaehlwerk#zaehlzeiten)</span> | — | [Zaehlzeitregister](/bo4e/202604/com/Zaehlzeitregister) |
| <span className="hbs-f hbs-e2">[register](/bo4e/202604/com/Zaehlzeitregister#register)</span> | Zählzeitregister | string |
| <span className="hbs-f hbs-e2">[zaehlzeitDefinition](/bo4e/202604/com/Zaehlzeitregister#zaehlzeitdefinition)</span> | Zählzeitdefinition | string |
| <span className="hbs-f hbs-e2">[schwachlastfaehig](/bo4e/202604/com/Zaehlzeitregister#schwachlastfaehig)</span> | Schwachlastfähigkeit des Registers | [Enum Schwachlastfaehig](/bo4e/202604/enum/Schwachlastfaehig)<br/><Werte>`SCHWACHLASTFAEHIG`, `NICHT_SCHWACHLASTFAEHIG`</Werte> |
| <span className="hbs-f hbs-e1">[konfiguration](/bo4e/202604/com/Zaehlwerk#konfiguration)</span> | Konfiguration (iMSys) des Zählwerks | string |
| <span className="hbs-f hbs-e1">[messprodukt](/bo4e/202604/com/Zaehlwerk#messprodukt)</span> | messprodukt | string |
| <span className="hbs-f hbs-e1">[wertegranularitaet](/bo4e/202604/com/Zaehlwerk#wertegranularitaet)</span> | Wertegranularitaet | [Enum Wertegranularitaet](/bo4e/202604/enum/Wertegranularitaet)<br/><Werte>`JAEHRLICH`, `HALBJAEHRLICH`, `QUARTALSWEISE`, `MONATLICH`</Werte> |
| <span className="hbs-f hbs-e1">[notwendigkeitZweiteMessung](/bo4e/202604/com/Zaehlwerk#notwendigkeitzweitemessung)</span> | NotwendigkeitZweiteMessung | [Enum NotwendigkeitZweiteMessung](/bo4e/202604/enum/NotwendigkeitZweiteMessung)<br/><Werte>`VORHANDEN`, `NICHT_VORHANDEN`</Werte> |
| <span className="hbs-f hbs-e1">[werteuebermittlungVerwendungszweck](/bo4e/202604/com/Zaehlwerk#werteuebermittlungverwendungszweck)</span> | WerteuebermittlungVerwendungszweck | [Enum WerteuebermittlungVerwendungszweck](/bo4e/202604/enum/WerteuebermittlungVerwendungszweck)<br/><Werte>`VORHANDEN`, `NICHT_VORHANDEN`</Werte> |
| <span className="hbs-f hbs-e1">[artEMobilitaet](/bo4e/202604/com/Zaehlwerk#artemobilitaet)</span> | ArtEmobilitaet | [Enum ArtEmobilitaet](/bo4e/202604/enum/ArtEmobilitaet)<br/><Werte>`WB`, `LS`, `LP`</Werte> |
| <span className="hbs-f hbs-e1">[konfigurationsprodukt](/bo4e/202604/com/Zaehlwerk#konfigurationsprodukt)</span> | konfigurationsprodukt | string |
| <span className="hbs-f hbs-e1">[keinKonfigurationsprodukt](/bo4e/202604/com/Zaehlwerk#keinkonfigurationsprodukt)</span> | keinKonfigurationsprodukt | boolean |
| <span className="hbs-f hbs-e1">[leistungskurvendefinition](/bo4e/202604/com/Zaehlwerk#leistungskurvendefinition)</span> | leistungskurvendefinition | string |
| <span className="hbs-g hbs-e1">[verwendungszwecke](/bo4e/202604/com/Zaehlwerk#verwendungszwecke) <span className="hbs-liste">[ ]</span></span> | Verwendungungszweck der Werte Marktlokation | [Verwendungszweck[]](/bo4e/202604/com/Verwendungszweck) |
| <span className="hbs-f hbs-e2">[marktrolle](/bo4e/202604/com/Verwendungszweck#marktrolle)</span> | Diese Rollen kann ein Marktteilnehmer einnehmen | [Enum Marktrolle](/bo4e/202604/enum/Marktrolle)<br/><Werte>`NB`, `LF`, `MSB`, `MSBA`, `GMSB`, `MDL`, `DL`, `BKV`, `UENB`, `KUNDE-SELBST-NN`, `MGV`, `EIV`, `RB`, `KUNDE`, `INTERESSENT`, `KN`, `UBA`, `BIKO`, `ESA`</Werte> |
| <span className="hbs-f hbs-e2">[zweck](/bo4e/202604/com/Verwendungszweck#zweck) <span className="hbs-liste">[ ]</span></span> | zweck | [Enum VerwendungszweckValue[]](/bo4e/202604/enum/VerwendungszweckValue)<br/><Werte>`NETZNUTZUNGSABRECHNUNG`, `BILANZKREISABRECHNUNG`, `MEHRMINDERMENGENABRECHNUNG`, `ENDKUNDENABRECHNUNG`, `UEBERMITTLUNG_AN_DAS_HKNR`, `BLINDARBEITSABRECHNUNG`, `ERMITTLUNG_AUSGEGLICHENHEIT_BILANZKREIS`, `BLINDARBEITABRECHNUNG_BETRIEBSFUEHRUNG`, `ES_LIEGT_KEIN_VERWENDUNGSZWECK_VOR`</Werte> |
| <span className="hbs-f hbs-e1">[verwendungszweckNB](/bo4e/202604/com/Zaehlwerk#verwendungszwecknb)</span> | Codes gemäß Codeliste der Verwendungszwecke Verwendungszweck NB | string |
| <span className="hbs-f hbs-e1">[verwendungszweckLF](/bo4e/202604/com/Zaehlwerk#verwendungszwecklf)</span> | Codes gemäß Codeliste der Verwendungszwecke Verwendungszweck LF | string |
| <span className="hbs-f hbs-e1">[verwendungszweckUENB](/bo4e/202604/com/Zaehlwerk#verwendungszweckuenb)</span> | Codes gemäß Codeliste der Verwendungszwecke Verwendungszweck ÜNB | string |
| <span className="hbs-f hbs-e1">[keinProdukt](/bo4e/202604/com/Zaehlwerk#keinprodukt)</span> | CCI+11++ZF6: keinProdukt zugeordnet | boolean |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### konfigurationsprodukt

3 Verwendung(en) in den Nachrichtentypen QUOTES, REQOTE.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_15003](/schnittstellen/202604/pruefi/QUOTES/PI_15003) | Prüfi | QUOTES | stammdaten › WERTE_NACH_TYP2 |
| [PI_15004](/schnittstellen/202604/pruefi/QUOTES/PI_15004) | Prüfi | QUOTES | stammdaten › WERTE_NACH_TYP2 |
| [PI_35004](/schnittstellen/202604/pruefi/REQOTE/PI_35004) | Prüfi | REQOTE | stammdaten › WERTE_NACH_TYP2 |

### messprodukt

5 Verwendung(en) in den Nachrichtentypen ORDERS, QUOTES, REQOTE.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_15003](/schnittstellen/202604/pruefi/QUOTES/PI_15003) | Prüfi | QUOTES | stammdaten › WERTE_NACH_TYP2 |
| [PI_15004](/schnittstellen/202604/pruefi/QUOTES/PI_15004) | Prüfi | QUOTES | stammdaten › WERTE_NACH_TYP2 |
| [PI_17128](/schnittstellen/202604/pruefi/ORDERS/PI_17128) | Prüfi | ORDERS | stammdaten › WERTE_NACH_TYP2 |
| [PI_17130](/schnittstellen/202604/pruefi/ORDERS/PI_17130) | Prüfi | ORDERS | stammdaten › WERTE_NACH_TYP2 |
| [PI_35004](/schnittstellen/202604/pruefi/REQOTE/PI_35004) | Prüfi | REQOTE | stammdaten › WERTE_NACH_TYP2 |

### aenderungsmoeglichkeitKonfiguration

4 Verwendung(en) in den Nachrichtentypen ORDERS, QUOTES, REQOTE.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_15004](/schnittstellen/202604/pruefi/QUOTES/PI_15004) | Prüfi | QUOTES | stammdaten › WERTE_NACH_TYP2 |
| [PI_17128](/schnittstellen/202604/pruefi/ORDERS/PI_17128) | Prüfi | ORDERS | stammdaten › WERTE_NACH_TYP2 |
| [PI_17130](/schnittstellen/202604/pruefi/ORDERS/PI_17130) | Prüfi | ORDERS | stammdaten › WERTE_NACH_TYP2 |
| [PI_35004](/schnittstellen/202604/pruefi/REQOTE/PI_35004) | Prüfi | REQOTE | stammdaten › WERTE_NACH_TYP2 |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
