# AuftragPosition
<span hidden data-pagefind-meta={"title:AuftragPosition — BO4E-Komponente (FV 202604)"} />

BO4E-Komponente · 21 Felder · 17 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="positionsnummer"></a>`positionsnummer` | integer | Positionsnummer |
| <a id="positionsnummerangebot"></a>`positionsnummerAngebot` | string | laufende Positionsnummer des Angebot |
| <a id="energieerfassung"></a>`energieerfassung` | [Enum Energieerfassung](/bo4e/202604/enum/Energieerfassung)<br/><Werte>`SEPARAT_ERFASSEN`, `NICHT_SEPARAT_ERFASSEN`</Werte> | Energieerfassung |
| <a id="artikelnummer"></a>`artikelnummer` | [Enum BDEWArtikelnummer](/bo4e/202604/enum/BDEWArtikelnummer)<br/><Werte>`LEISTUNG`, `LEISTUNG_PAUSCHAL`, `GRUNDPREIS`, `REGELENERGIE_ARBEIT`, `REGELENERGIE_LEISTUNG`, `NOTSTROMLIEFERUNG_ARBEIT`, `NOTSTROMLIEFERUNG_LEISTUNG`, `RESERVENETZKAPAZITAET`, `RESERVELEISTUNG`, `ZUSAETZLICHE_ABLESUNG`, `PRUEFGEBUEHREN_AUSSERPLANMAESSIG`, `WIRKARBEIT`, `SINGULAER_GENUTZTE_BETRIEBSMITTEL`, `ABGABE_KWKG`, `ABSCHLAG`, `KONZESSIONSABGABE`, `ENTGELT_FERNAUSLESUNG`, `UNTERMESSUNG`, `BLINDMEHRARBEIT`, `ENTGELT_ABRECHNUNG`, `SPERRKOSTEN`, `ENTSPERRKOSTEN`, `MAHNKOSTEN`, `MEHR_MINDERMENGEN`, `INKASSOKOSTEN`, `BLINDMEHRLEISTUNG`, `ENTGELT_MESSUNG_ABLESUNG`, `ENTGELT_EINBAU_BETRIEB_WARTUNG_MESSTECHNIK`, `AUSGLEICHSENERGIE`, `AUSGLEICHSENERGIE_UNTERDECKUNG`, `ZAEHLEINRICHTUNG`, `WANDLER_MENGENUMWERTER`, `KOMMUNIKATIONSEINRICHTUNG`, `TECHNISCHE_STEUEREINRICHTUNG`, `PARAGRAF_19_STROM_NEV_UMLAGE`, `BEFESTIGUNGSEINRICHTUNG`, `OFFSHORE_HAFTUNGSUMLAGE`, `FIXE_ARBEITSENTGELTKOMPONENTE`, `FIXE_LEISTUNGSENTGELTKOMPONENTE`, `UMLAGE_ABSCHALTBARE_LASTEN`, `MEHRMENGE`, `MINDERMENGE`, `ENERGIESTEUER`, `SMARTMETER_GATEWAY`, `STEUERBOX`, `MSB_INKL_MESSUNG`, `ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_2_1_MSBG`, `ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_2_2_MSBG`, `ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_2_3_MSBG`, `ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_2_4_MSBG`, `ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_2_5_MSBG`, `ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_3_MSBG`, `ENTGELT_KAPAZITAETEN`</Werte> | BDEW Artikelnummer |
| <a id="positionsbetrag"></a>`positionsbetrag` | string | Betrag der Position |
| <a id="gueltigab"></a>`gueltigAb` | string (date-time) | gueltigAb |
| <a id="startdatum"></a>`startdatum` | string (date-time) | startdatum |
| <a id="enddatum"></a>`enddatum` | string (date-time) | enddatum |
| <a id="istbestand"></a>`istBestand` | string | istBestand |
| <a id="obiskennzahl"></a>`obiskennzahl` | string | Obis-Kennzahl |
| <a id="anfragegrund"></a>`anfragegrund` | [Enum Anfragegrund](/bo4e/202604/enum/Anfragegrund)<br/><Werte>`ABGRENZUNG_VON_ENERGIEMENGEN`, `ABGRENZUNG`, `WECHSELEREIGNIS`, `ZWISCHENABLESUNG`, `DIREKTER_VERTRAG_MSB_AN`, `DIREKTER_VERTRAG_MSB_ANN`, `AENDERUNG_IM_LOKATIONSBUENDEL`, `NEUKONFIGURATION`, `KONFIGURATION_UNVERAENDERT`</Werte> | Anfragegrund |
| <a id="allgemeineinformationen"></a>`allgemeineInformationen` | [AllgemeineInformationen](/bo4e/202604/com/AllgemeineInformationen) | — |
| <a id="infoabweichung"></a>`infoAbweichung` | [InfoAbweichung](/bo4e/202604/com/InfoAbweichung) | — |
| <a id="definitionstyp"></a>`definitionsTyp` | [Enum DefinitionsTyp](/bo4e/202604/enum/DefinitionsTyp)<br/><Werte>`ZAEHLZEIT`, `SCHALTZEIT`, `LEISTUNGSKURVEN`</Werte> | DefinitionsTyp |
| <a id="lokationsid"></a>`lokationsId` | string | lokationsId |
| <a id="zaehlwerk"></a>`zaehlwerk` | integer | Zaehlwerk |
| <a id="endpunktadresse"></a>`endpunktAdresse` | [EndpunktAdresse](/bo4e/202604/com/EndpunktAdresse) | — |
| <a id="zertifikatsinformationen"></a>`zertifikatsInformationen` | [Zertifikatsinformationen](/bo4e/202604/com/Zertifikatsinformationen) | — |
| <a id="wakeupport"></a>`wakeUpPort` | string | Wake-Up-Port der Kommunikationseinheit |
| <a id="apnkommunikationsdaten"></a>`apnKommunikationsdaten` | string | APN der Kommunikationsdaten |
| <a id="apnkommunikationsdatenzugriffsparameter"></a>`apnKommunikationsdatenZugriffsparameter` | [ApnKommunikationsdatenZugriffsparameter](/bo4e/202604/com/ApnKommunikationsdatenZugriffsparameter) | — |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[positionsnummer](/bo4e/202604/com/AuftragPosition#positionsnummer)</span> | Positionsnummer | integer |
| <span className="hbs-f hbs-e0">[positionsnummerAngebot](/bo4e/202604/com/AuftragPosition#positionsnummerangebot)</span> | laufende Positionsnummer des Angebot | string |
| <span className="hbs-f hbs-e0">[energieerfassung](/bo4e/202604/com/AuftragPosition#energieerfassung)</span> | Energieerfassung | [Enum Energieerfassung](/bo4e/202604/enum/Energieerfassung)<br/><Werte>`SEPARAT_ERFASSEN`, `NICHT_SEPARAT_ERFASSEN`</Werte> |
| <span className="hbs-f hbs-e0">[artikelnummer](/bo4e/202604/com/AuftragPosition#artikelnummer)</span> | BDEW Artikelnummer | [Enum BDEWArtikelnummer](/bo4e/202604/enum/BDEWArtikelnummer)<br/><Werte>`LEISTUNG`, `LEISTUNG_PAUSCHAL`, `GRUNDPREIS`, `REGELENERGIE_ARBEIT`, `REGELENERGIE_LEISTUNG`, `NOTSTROMLIEFERUNG_ARBEIT`, `NOTSTROMLIEFERUNG_LEISTUNG`, `RESERVENETZKAPAZITAET`, `RESERVELEISTUNG`, `ZUSAETZLICHE_ABLESUNG`, `PRUEFGEBUEHREN_AUSSERPLANMAESSIG`, `WIRKARBEIT`, `SINGULAER_GENUTZTE_BETRIEBSMITTEL`, `ABGABE_KWKG`, `ABSCHLAG`, `KONZESSIONSABGABE`, `ENTGELT_FERNAUSLESUNG`, `UNTERMESSUNG`, `BLINDMEHRARBEIT`, `ENTGELT_ABRECHNUNG`, `SPERRKOSTEN`, `ENTSPERRKOSTEN`, `MAHNKOSTEN`, `MEHR_MINDERMENGEN`, `INKASSOKOSTEN`, `BLINDMEHRLEISTUNG`, `ENTGELT_MESSUNG_ABLESUNG`, `ENTGELT_EINBAU_BETRIEB_WARTUNG_MESSTECHNIK`, `AUSGLEICHSENERGIE`, `AUSGLEICHSENERGIE_UNTERDECKUNG`, `ZAEHLEINRICHTUNG`, `WANDLER_MENGENUMWERTER`, `KOMMUNIKATIONSEINRICHTUNG`, `TECHNISCHE_STEUEREINRICHTUNG`, `PARAGRAF_19_STROM_NEV_UMLAGE`, `BEFESTIGUNGSEINRICHTUNG`, `OFFSHORE_HAFTUNGSUMLAGE`, `FIXE_ARBEITSENTGELTKOMPONENTE`, `FIXE_LEISTUNGSENTGELTKOMPONENTE`, `UMLAGE_ABSCHALTBARE_LASTEN`, `MEHRMENGE`, `MINDERMENGE`, `ENERGIESTEUER`, `SMARTMETER_GATEWAY`, `STEUERBOX`, `MSB_INKL_MESSUNG`, `ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_2_1_MSBG`, `ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_2_2_MSBG`, `ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_2_3_MSBG`, `ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_2_4_MSBG`, `ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_2_5_MSBG`, `ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_3_MSBG`, `ENTGELT_KAPAZITAETEN`</Werte> |
| <span className="hbs-f hbs-e0">[positionsbetrag](/bo4e/202604/com/AuftragPosition#positionsbetrag)</span> | Betrag der Position | string |
| <span className="hbs-f hbs-e0">[gueltigAb](/bo4e/202604/com/AuftragPosition#gueltigab)</span> | gueltigAb | string (date-time) |
| <span className="hbs-f hbs-e0">[startdatum](/bo4e/202604/com/AuftragPosition#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e0">[enddatum](/bo4e/202604/com/AuftragPosition#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-f hbs-e0">[istBestand](/bo4e/202604/com/AuftragPosition#istbestand)</span> | istBestand | string |
| <span className="hbs-f hbs-e0">[obiskennzahl](/bo4e/202604/com/AuftragPosition#obiskennzahl)</span> | Obis-Kennzahl | string |
| <span className="hbs-f hbs-e0">[anfragegrund](/bo4e/202604/com/AuftragPosition#anfragegrund)</span> | Anfragegrund | [Enum Anfragegrund](/bo4e/202604/enum/Anfragegrund)<br/><Werte>`ABGRENZUNG_VON_ENERGIEMENGEN`, `ABGRENZUNG`, `WECHSELEREIGNIS`, `ZWISCHENABLESUNG`, `DIREKTER_VERTRAG_MSB_AN`, `DIREKTER_VERTRAG_MSB_ANN`, `AENDERUNG_IM_LOKATIONSBUENDEL`, `NEUKONFIGURATION`, `KONFIGURATION_UNVERAENDERT`</Werte> |
| <span className="hbs-g hbs-e0">[allgemeineInformationen](/bo4e/202604/com/AuftragPosition#allgemeineinformationen)</span> | — | [AllgemeineInformationen](/bo4e/202604/com/AllgemeineInformationen) |
| <span className="hbs-f hbs-e1">[info1](/bo4e/202604/com/AllgemeineInformationen#info1)</span> | Allgemeine Info 1 | string |
| <span className="hbs-f hbs-e1">[info2](/bo4e/202604/com/AllgemeineInformationen#info2)</span> | Allgemeine Info 2 | string |
| <span className="hbs-f hbs-e1">[info3](/bo4e/202604/com/AllgemeineInformationen#info3)</span> | Allgemeine Info 3 | string |
| <span className="hbs-f hbs-e1">[info4](/bo4e/202604/com/AllgemeineInformationen#info4)</span> | Allgemeine Info 4 | string |
| <span className="hbs-f hbs-e1">[info5](/bo4e/202604/com/AllgemeineInformationen#info5)</span> | Allgemeine Info 5 | string |
| <span className="hbs-g hbs-e0">[infoAbweichung](/bo4e/202604/com/AuftragPosition#infoabweichung)</span> | — | [InfoAbweichung](/bo4e/202604/com/InfoAbweichung) |
| <span className="hbs-f hbs-e1">[abweichung1](/bo4e/202604/com/InfoAbweichung#abweichung1)</span> | Abweichung Zeile 1 | string |
| <span className="hbs-f hbs-e1">[abweichung2](/bo4e/202604/com/InfoAbweichung#abweichung2)</span> | Abweichung Zeile 2 | string |
| <span className="hbs-f hbs-e1">[abweichung3](/bo4e/202604/com/InfoAbweichung#abweichung3)</span> | Abweichung Zeile 3 | string |
| <span className="hbs-f hbs-e1">[abweichung4](/bo4e/202604/com/InfoAbweichung#abweichung4)</span> | Abweichung Zeile 4 | string |
| <span className="hbs-f hbs-e1">[abweichung5](/bo4e/202604/com/InfoAbweichung#abweichung5)</span> | Abweichung Zeile 5 | string |
| <span className="hbs-f hbs-e0">[definitionsTyp](/bo4e/202604/com/AuftragPosition#definitionstyp)</span> | DefinitionsTyp | [Enum DefinitionsTyp](/bo4e/202604/enum/DefinitionsTyp)<br/><Werte>`ZAEHLZEIT`, `SCHALTZEIT`, `LEISTUNGSKURVEN`</Werte> |
| <span className="hbs-f hbs-e0">[lokationsId](/bo4e/202604/com/AuftragPosition#lokationsid)</span> | lokationsId | string |
| <span className="hbs-f hbs-e0">[zaehlwerk](/bo4e/202604/com/AuftragPosition#zaehlwerk)</span> | Zaehlwerk | integer |
| <span className="hbs-g hbs-e0">[endpunktAdresse](/bo4e/202604/com/AuftragPosition#endpunktadresse)</span> | — | [EndpunktAdresse](/bo4e/202604/com/EndpunktAdresse) |
| <span className="hbs-f hbs-e1">[gwaManagement](/bo4e/202604/com/EndpunktAdresse#gwamanagement)</span> | Endpunktadresse GWA Management | string |
| <span className="hbs-f hbs-e1">[gwaAdminService](/bo4e/202604/com/EndpunktAdresse#gwaadminservice)</span> | Endpunktadresse GWA Admin-Service | string |
| <span className="hbs-f hbs-e1">[gwaNTP](/bo4e/202604/com/EndpunktAdresse#gwantp)</span> | Endpunktadresse GWA NTP (Zeitserver) | string |
| <span className="hbs-g hbs-e0">[zertifikatsInformationen](/bo4e/202604/com/AuftragPosition#zertifikatsinformationen)</span> | — | [Zertifikatsinformationen](/bo4e/202604/com/Zertifikatsinformationen) |
| <span className="hbs-f hbs-e1">[uriSubCA](/bo4e/202604/com/Zertifikatsinformationen#urisubca)</span> | URI der Sub-CA | string |
| <span className="hbs-f hbs-e1">[commonNameZertifikat](/bo4e/202604/com/Zertifikatsinformationen#commonnamezertifikat)</span> | Common Name (CN) des Zertifikats | string |
| <span className="hbs-f hbs-e1">[seriennummerZertifikat](/bo4e/202604/com/Zertifikatsinformationen#seriennummerzertifikat)</span> | Seriennummer des Zertifikats | string |
| <span className="hbs-f hbs-e0">[wakeUpPort](/bo4e/202604/com/AuftragPosition#wakeupport)</span> | Wake-Up-Port der Kommunikationseinheit | string |
| <span className="hbs-f hbs-e0">[apnKommunikationsdaten](/bo4e/202604/com/AuftragPosition#apnkommunikationsdaten)</span> | APN der Kommunikationsdaten | string |
| <span className="hbs-g hbs-e0">[apnKommunikationsdatenZugriffsparameter](/bo4e/202604/com/AuftragPosition#apnkommunikationsdatenzugriffsparameter)</span> | — | [ApnKommunikationsdatenZugriffsparameter](/bo4e/202604/com/ApnKommunikationsdatenZugriffsparameter) |
| <span className="hbs-f hbs-e1">[apnName](/bo4e/202604/com/ApnKommunikationsdatenZugriffsparameter#apnname)</span> | Name des APNs | string |
| <span className="hbs-f hbs-e1">[nutzer](/bo4e/202604/com/ApnKommunikationsdatenZugriffsparameter#nutzer)</span> | Nutzer | string |
| <span className="hbs-f hbs-e1">[passwort](/bo4e/202604/com/ApnKommunikationsdatenZugriffsparameter#passwort)</span> | Passwort | string |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### positionsnummer

8 Verwendung(en) in den Nachrichtentypen ORDERS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_17001](/schnittstellen/202604/pruefi/ORDERS/PI_17001) | Prüfi | ORDERS | stammdaten › AUFTRAG › positionsdaten |
| [PI_17101](/schnittstellen/202604/pruefi/ORDERS/PI_17101) | Prüfi | ORDERS | stammdaten › AUFTRAG › positionsdaten |
| [PI_17113](/schnittstellen/202604/pruefi/ORDERS/PI_17113) | Prüfi | ORDERS | stammdaten › AUFTRAG › positionsdaten |
| [PI_17118](/schnittstellen/202604/pruefi/ORDERS/PI_17118) | Prüfi | ORDERS | stammdaten › AUFTRAG › positionsdaten |
| [PI_17121](/schnittstellen/202604/pruefi/ORDERS/PI_17121) | Prüfi | ORDERS | stammdaten › AUFTRAG › positionsdaten |
| [PI_17122](/schnittstellen/202604/pruefi/ORDERS/PI_17122) | Prüfi | ORDERS | stammdaten › AUFTRAG › positionsdaten |
| [PI_17134](/schnittstellen/202604/pruefi/ORDERS/PI_17134) | Prüfi | ORDERS | stammdaten › AUFTRAG › positionsdaten |
| [PI_17135](/schnittstellen/202604/pruefi/ORDERS/PI_17135) | Prüfi | ORDERS | stammdaten › AUFTRAG › positionsdaten |

### positionsnummerAngebot

1 Verwendung(en) in den Nachrichtentypen ORDERS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_17001](/schnittstellen/202604/pruefi/ORDERS/PI_17001) | Prüfi | ORDERS | stammdaten › AUFTRAG › positionsdaten |

### startdatum

2 Verwendung(en) in den Nachrichtentypen ORDERS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_17102](/schnittstellen/202604/pruefi/ORDERS/PI_17102) | Prüfi | ORDERS | stammdaten › AUFTRAG › positionsdaten |
| [PI_17103](/schnittstellen/202604/pruefi/ORDERS/PI_17103) | Prüfi | ORDERS | stammdaten › AUFTRAG › positionsdaten |

### enddatum

2 Verwendung(en) in den Nachrichtentypen ORDERS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_17102](/schnittstellen/202604/pruefi/ORDERS/PI_17102) | Prüfi | ORDERS | stammdaten › AUFTRAG › positionsdaten |
| [PI_17103](/schnittstellen/202604/pruefi/ORDERS/PI_17103) | Prüfi | ORDERS | stammdaten › AUFTRAG › positionsdaten |

### anfragegrund

3 Verwendung(en) in den Nachrichtentypen ORDERS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_17004](/schnittstellen/202604/pruefi/ORDERS/PI_17004) | Prüfi | ORDERS | stammdaten › AUFTRAG › positionsdaten |
| [PI_17006](/schnittstellen/202604/pruefi/ORDERS/PI_17006) | Prüfi | ORDERS | stammdaten › AUFTRAG › positionsdaten |
| [PI_17134](/schnittstellen/202604/pruefi/ORDERS/PI_17134) | Prüfi | ORDERS | stammdaten › AUFTRAG › positionsdaten |

### definitionsTyp

1 Verwendung(en) in den Nachrichtentypen ORDERS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_17122](/schnittstellen/202604/pruefi/ORDERS/PI_17122) | Prüfi | ORDERS | stammdaten › AUFTRAG › positionsdaten |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
