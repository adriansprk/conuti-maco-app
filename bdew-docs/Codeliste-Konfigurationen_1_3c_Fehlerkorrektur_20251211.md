edi@energy. Datenformate Strom & Gas logo

**Konsolidierte Lesefassung mit Fehlerkorrekturen**
**Stand: 11.12.2025**

# Codeliste der Konfigurationen

**Version:** 1.3c
**Ursprüngliches Publikationsdatum:** 01.04.2025
**Autor:** BDEW

Codeliste der Konfigurationen

edi@energy. Datenformate Strom & Gas logo

## Disclaimer

Die PDF-Datei ist das allein gültige Dokument.

Die zusätzlich veröffentlichte Word-Datei dient als informatorische Lesefassung und entspricht inhaltlich der PDF-Datei. Diese Word-Datei wird bis auf Weiteres rein informatorisch und ergänzend veröffentlicht unter dem Vorbehalt, zukünftig eine kostenpflichtige Veröffentlichung der Word-Datei einzuführen.

Version: 1.3c

11.12.2025

Seite <page_number>2</page_number> von 58

Codeliste der Konfigurationen

edi@energy. Datenformate Strom & Gas

# Inhaltsverzeichnis

**1 Einleitung** ................................................................................................................... **5**

**2 Codelisten der Standard-Messprodukte Strom für Werte nach Typ 1** ........................... **6**
2.1 Standard-Messprodukte der Marktlokation ............................................................ 7
2.1.1 mit Wahlmöglichkeit der Zuordnung einer Zählzeit ................................................ 7
2.1.2 ohne Wahlmöglichkeit der Zuordnung einer Zählzeit ............................................. 8
2.2 Standard-Messprodukte der Tranche ...................................................................... 9
2.3 Standard-Messprodukte der Messlokation ........................................................... 10
2.3.1 mit Wahlmöglichkeit der Zuordnung einer Zählzeit .............................................. 10
2.3.2 ohne Wahlmöglichkeit der Zuordnung einer Zählzeit ........................................... 12
2.4 Standard-Messprodukte der Netzlokation ............................................................ 14

**3 Codeliste der Standard-Messprodukte Gas** ................................................................ **15**

**4 Codelisten der Konfigurationsprodukte und Messprodukte für Werte nach Typ 2** ...... **17**
4.1 Konfigurationsprodukte Schaltzeitdefinition ......................................................... 17
4.2 Konfigurationsprodukte Leistungskurvendefinition .............................................. 17
4.3 Konfigurationsprodukte Ad-Hoc-Steuerkanal ........................................................ 18
4.4 Messprodukte mit Konfigurationserlaubnis für Werte nach Typ 2 aus SMGW .... 19
4.5 Messprodukte für Werte nach Typ 2 aus Backend für LF und NB ......................... 23
4.6 Codelisten der Messprodukte Strom für ESA ........................................................ 24
4.6.1 Werte nach Typ 2 aus Backend .............................................................................. 24
4.6.2 Werte nach Typ 2 aus SMGW ................................................................................ 29
4.7 Art der Werte für Messprodukte nach Typ 2 ......................................................... 32
4.7.1 Messprodukt-Position-Codes für die Messprodukte Ist-Einspeisung .................... 34
4.7.2 Messprodukt-Position-Codes für die Messprodukte Netzzustandsdaten ............. 35
4.7.3 Messprodukt-Position-Codes für die Messprodukte Mehrwertdienste ............... 36
4.7.4 Messprodukt-Position-Codes für die Messprodukte Netzzustandsdaten
Spannung ................................................................................................................ 37

**5 Mindestumfang der Messprodukte in der UTILMD** .................................................... **38**
5.1 Mindestumfang der Messprodukte in der UTILMD Strom .................................... 38
5.2 Mindestumfang der Messprodukte in der UTILMD Gas ........................................ 43

Version: 1.3c

11.12.2025

Seite <page_number>3</page_number> von 58

Codeliste der Konfigurationen

edi@energy. Datenformate Strom & Gas logo

**6 Produkte zur Bestellung / Änderung von Daten**......................................................... **46**
6.1 Produkte zur Anmeldung einer Zuordnung des LFN (UTILMD) ............................. 46
6.1.1 Verpflichtende Produkte zur Anmeldung einer Zuordnung des LFN
(UTILMD) ................................................................................................................ 46
6.1.2 Optionale Produkte als Voraussetzung in der Anmeldung einer Zuordnung
des LFN (UTILMD)................................................................................................... 48
6.1.3 Optionale Produkte als Erwartung / Änderungswunsch in der Anmeldung
einer Zuordnung des LFN (UTILMD)....................................................................... 49
6.2 Produkte zur Bestellung einer Änderung von Abrechnungsdaten (ORDERS)........ 52
**7 Produkte zur Bestellung einer Änderung an einer Lokation** ....................................... **55**
7.1 Produkte zur Bestellung einer Änderung an einer Lokation in der Sparte Strom . 55
7.2 Produkte zur Bestellung einer Änderung an einer Lokation in der Sparte Gas ..... 56
**8 Änderungshistorie** .................................................................................................... **57**

Version: 1.3c

11.12.2025

Seite <page_number>4</page_number> von 58

Codeliste der Konfigurationen

edi@energy. Datenformate Strom & Gas logo

# 1 Einleitung

Durch den elektronischen Datenaustausch wird die Abwicklung von Geschäftsvorgängen zwischen den beteiligten Unternehmen vereinfacht. Die Implementierungsaufwände sind umso geringer, je standardisierter die einzelnen Nachrichten sind, die den jeweiligen Geschäftsvorgängen zugrunde liegen. Aus diesem Grund wird die Aussage welche Konfigurationen (z. B. Messprodukte oder Konfigurationen) bestellt werden können über Codes ausgetauscht. Die Codeliste für alle im deutschen Energiemarkt fachlich notwendigen Werte sind in diesem Dokument dargestellt.

Die hier beschriebenen Konfigurationen beziehen sich auf Prozesse, die zwischen den Gremien (BNetzA, Verbände) abgestimmt sind, und werden nach Abstimmung neuer bzw. geänderter Prozesse entsprechend angepasst.

Die Messprodukte Strom in Kapitel 4.6, die ausschließlich für die Rolle ESA Anwendung finden, sind nicht Bestandteil des Konsultationsverfahrens der Nachrichtenbeschreibungen und Anwendungshandbücher. Sie wird entsprechend der Marktbedürfnisse aktualisiert. Informationen über neue Versionen erhalten Sie, indem Sie sich im Forum Datenformate für den entsprechenden Newsletter eintragen. Da nach der Veröffentlichung der neuen Messprodukte die beteiligten Marktpartner diese in ihren Systemen umzusetzen müssen, sind die Messprodukte 14 Tage nach Veröffentlichung einer neuen Version nutzbar. Der genaue Nutzungstermin ist in der Tabelle in der Spalte „Nutzbar ab“ angegeben.

Werte aus dem Kapitel 4.6 die dem ESA übermittelt werden, haben keinen Bezug zu Werten aus dem Kapitel 2 Codelisten der Standard-Messprodukte Strom für Werte nach Typ 1 die in der Netznutzungs- oder Bilanzkreisabrechnung verwendet werden. Das heißt, bei Differenzen zwischen Werten aus Messprodukten des Kapitels 4.6, die der ESA erhalten hat zu Werten, die dem Anschlussnutzer in Rechnung gestellt werden, sind ausschließlich die Werte aus Kapitel 2 relevant, die der LF, NB oder ÜNB erhalten haben.

Version: 1.3c 11.12.2025 <page_number>Seite 5 von 58</page_number>

Codeliste der Konfigurationen

edi@energy. Datenformate Strom & Gas

# 2 Codelisten der Standard-Messprodukte Strom für Werte nach Typ 1

Dieses Kapitel enthält die Codelisten der Messprodukte Strom. Die Messprodukte werden per MSCONS in der Wertequalität, dem Übermittlungsintervall und der Frist nach WiM Teil 2, Kap. 2.5.5. bereitgestellt.

Die zulässigen Kombinationen der Messprodukte Strom sowie ggf. relevante Abhängigkeiten, sind als Fußnote in der jeweiligen Codeliste beschrieben.

Der Mindestumfang der Messprodukte in der UTILMD sind im Kapitel 5 Mindestumfang der Messprodukte in der UTILMD, sowie deren Unterkapitel beschrieben.

Version: 1.3c

11.12.2025

Seite <page_number>6</page_number> von 58

Codeliste der Konfigurationen

edi@energy. Datenformate Strom & Gas logo

# 2.1 Standard-Messprodukte der Marktlokation

## 2.1.1 mit Wahlmöglichkeit der Zuordnung einer Zählzeit

Bei einer Marktlokation mit der Lieferrichtung Verbrauch ist bei den in der folgenden Tabelle genannten Messprodukten die Zuordnung einer Zählzeit zu einem Messprodukt möglich. Bei einer Marktlokation mit der Lieferrichtung Erzeugung ist bei den in der folgenden Tabelle genannten Messprodukten keine Zuordnung einer Zählzeit zu einem Messprodukt möglich.

| Messprodukt-Code¹ | Bezeichnung                                                                                            | Wert       | Werteart     | Wertegranularität | Messprodukt gegenüber MSB von Marktrolle bestellbar<br/>NB | Messprodukt gegenüber MSB von Marktrolle bestellbar<br/>LF | Messprodukt gegenüber MSB von Marktrolle bestellbar<br/>MSB |
| ----------------- | ------------------------------------------------------------------------------------------------------ | ---------- | ------------ | ----------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ----------------------------------------------------------- |
| 9991 00000 004 4  | Marktlokation² mit Wahlmöglichkeit der Zuordnung einer Zählzeit<br/>für Wirkarbeit Menge jährlich      | Wirkarbeit | Arbeitsmenge | jährlich          | X                                                          | --                                                         | --                                                          |
| 9991 00000 049 0  | Marktlokation² mit Wahlmöglichkeit der Zuordnung einer Zählzeit<br/>für Wirkarbeit Menge halbjährlich  | Wirkarbeit | Arbeitsmenge | halbjährlich      | X                                                          | --                                                         | --                                                          |
| 9991 00000 005 2  | Marktlokation² mit Wahlmöglichkeit der Zuordnung einer Zählzeit<br/>für Wirkarbeit Menge quartalsweise | Wirkarbeit | Arbeitsmenge | quartalsweise     | X                                                          | --                                                         | --                                                          |
| 9991 00000 006 0  | Marktlokation² mit Wahlmöglichkeit der Zuordnung einer Zählzeit<br/>für Wirkarbeit Menge monatlich     | Wirkarbeit | Arbeitsmenge | monatlich         | X                                                          | --                                                         | --                                                          |
| 9991 00000 149 8  | Marktlokation² mit Wahlmöglichkeit der Zuordnung einer Zählzeit<br/>für Wirkarbeit Menge monatlich     | Wirkarbeit | Arbeitsmenge | monatlich         | --                                                         | X                                                          | --                                                          |


<sup>1</sup>Die Darstellung des Codes mit Leerzeichen erfolgt nur zur besseren Lesbarkeit. Beim elektronischen Datenaustausch wird der Code immer ohne Leerzeichen angegeben.

<sup>2</sup>Bei einer Marktlokation mit der Lieferrichtung Verbrauch ist für dieses Messprodukt die Zuordnung einer Zählzeit zu einem Messprodukt möglich, bei einer Marktlokation mit der Lieferrichtung Erzeugung ist für dieses Messprodukt keine Zuordnung einer Zählzeit möglich.

Version: 1.3c

11.12.2025

Seite 7 von 58
<page_number>7</page_number>

Codeliste der Konfigurationen edi@energy. Datenformate Strom & Gas logo

## 2.1.2 ohne Wahlmöglichkeit der Zuordnung einer Zählzeit

| Messprodukt-Code¹   | Bezeichnung                                                                                                     | Wert        | Werteart                              | Wertegranularität | Messprodukt gegenüber MSB von Marktrolle bestellbar<br/>NB | Messprodukt gegenüber MSB von Marktrolle bestellbar<br/>LF | Messprodukt gegenüber MSB von Marktrolle bestellbar<br/>MSB |
| ------------------- | --------------------------------------------------------------------------------------------------------------- | ----------- | ------------------------------------- | ----------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ----------------------------------------------------------- |
| 9991 00000 007 8    | Marktlokation ohne Wahlmöglichkeit der Zuordnung einer Zählzeit<br/>für Wirkarbeit Lastgang 1/4 stündlich       | Wirkarbeit  | Lastgang                              | 1/4 stündlich     | X                                                          | --                                                         | --                                                          |
| 9991 00000 008 63 4 | Marktlokation ohne Wahlmöglichkeit der Zuordnung einer Zählzeit<br/>für Wirkarbeit höchste 1/4 Stunde im Monat  | Wirkarbeit  | höchste 1/4<br/>Stunde im Mo-<br/>nat | --                | X                                                          | --                                                         | --                                                          |
| 9991 00000 009 4⁵   | Marktlokation ohne Wahlmöglichkeit der Zuordnung einer Zählzeit<br/>für Blindarbeit Lastgang 1/4 stündlich      | Blindarbeit | Lastgang                              | 1/4 stündlich     | X                                                          | --                                                         | --                                                          |
| 9991 00000 010 1⁵   | Marktlokation ohne Wahlmöglichkeit der Zuordnung einer Zählzeit<br/>für Blindarbeit höchste 1/4 Stunde im Monat | Blindarbeit | höchste 1/4<br/>Stunde im Mo-<br/>nat | ---               | X                                                          | --                                                         | --                                                          |
| 9991 00000 011 9⁵   | Marktlokation ohne Wahlmöglichkeit der Zuordnung einer Zählzeit<br/>für Blindarbeit Menge jährlich              | Blindarbeit | Menge                                 | jährlich          | X                                                          | --                                                         | --                                                          |
| 9991 00000 050 7⁵   | Marktlokation ohne Wahlmöglichkeit der Zuordnung einer Zählzeit<br/>für Blindarbeit Menge halbjährlich          | Blindarbeit | Menge                                 | halbjährlich      | X                                                          | --                                                         | --                                                          |
| 9991 00000 012 7⁵   | Marktlokation ohne Wahlmöglichkeit der Zuordnung einer Zählzeit<br/>für Blindarbeit Menge quartalsweise         | Blindarbeit | Menge                                 | quartalsweise     | X                                                          | --                                                         | --                                                          |
| 9991 00000 013 5⁵   | Marktlokation ohne Wahlmöglichkeit der Zuordnung einer Zählzeit<br/>für Blindarbeit Menge monatlich             | Blindarbeit | Menge                                 | monatlich         | X                                                          | --                                                         | --                                                          |


<sup>3</sup>Das Messprodukt mit dem Code 9991 00000 008 6 ist nur bestellbar, wenn zusätzlich eines der Messprodukte mit dem Code 9991 00000 004 4 oder 9991 00000 049 0 oder 9991 00000 005 2 oder 9991 00000 006 0 bestellt wird.

<sup>4</sup> Nur bei einer Marktlokation mit der Lieferrichtung Verbrauch.

<sup>5</sup> Nutzbar bis zum 01.01.2024 00:00 Uhr.

Version: 1.3c 11.12.2025 <page_number>Seite 8 von 58</page_number>

Codeliste der Konfigurationen

edi@energy. Datenformate Strom & Gas logo

## 2.2 Standard-Messprodukte der Tranche

| Messprodukt-Code¹ | Bezeichnung                                                                                     | Wert       | Werteart | Wertegranularität | Messprodukt gegenüber MSB von Marktrolle bestellbar<br/>NB | Messprodukt gegenüber MSB von Marktrolle bestellbar<br/>LF | Messprodukt gegenüber MSB von Marktrolle bestellbar<br/>MSB |
| ----------------- | ----------------------------------------------------------------------------------------------- | ---------- | -------- | ----------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ----------------------------------------------------------- |
| 9991 00000 014 3  | Tranche ohne Wahlmöglichkeit der Zuordnung einer Zählzeit für Wirkarbeit Lastgang 1/4 stündlich | Wirkarbeit | Lastgang | 1/4 stündlich     | X                                                          | --                                                         | --                                                          |
| 9991 00000 064 8  | Tranche ohne Wahlmöglichkeit der Zuordnung einer Zählzeit für Wirkarbeit Menge monatlich        | Wirkarbeit | Menge    | monatlich         | X                                                          | --                                                         | --                                                          |


Version: 1.3c

11.12.2025

Seite 9 von 58
<page_number>9</page_number>

Codeliste der Konfigurationen

edi@energy. Datenformate Strom & Gas logo

# 2.3 Standard-Messprodukte der Messlokation

## 2.3.1 mit Wahlmöglichkeit der Zuordnung einer Zählzeit

| Messprodukt-Code¹   | Bezeichnung                                                                                                       | Wert       | Werteart    | Erfassungs-intervall | Energief-luss-rich-tung / Quadrant | Messprodukt ge-genüber MSB von Marktrolle bestell-bar<br/>NB | Messprodukt ge-genüber MSB von Marktrolle bestell-bar<br/>LF | Messprodukt ge-genüber MSB von Marktrolle bestell-bar<br/>MSB |
| ------------------- | ----------------------------------------------------------------------------------------------------------------- | ---------- | ----------- | -------------------- | ---------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------- |
| 9991 00000 015 1⁶   | Messlokation mit Wahlmöglichkeit der Zuordnung einer Zählzeit für Wirk-arbeit Verbrauch Zählerstand jährlich      | Wirkarbeit | Zählerstand | jährlich             | Verbrauch                          | X                                                            | --                                                           | X                                                             |
| 9991 00000 016 9⁶ ⁷ | Messlokation mit Wahlmöglichkeit der Zuordnung einer Zählzeit für Wirk-arbeit Erzeugung Zählerstand jährlich      | Wirkarbeit | Zählerstand | jährlich             | Erzeugung                          | X                                                            | --                                                           | X                                                             |
| 9991 00000 051 5⁶   | Messlokation mit Wahlmöglichkeit der Zuordnung einer Zählzeit für Wirk-arbeit Verbrauch Zählerstand halbjährlich  | Wirkarbeit | Zählerstand | halbjährlich         | Verbrauch                          | X                                                            | --                                                           | X                                                             |
| 9991 00000 052 3⁶ ⁷ | Messlokation mit Wahlmöglichkeit der Zuordnung einer Zählzeit für Wirk-arbeit Erzeugung Zählerstand halbjährlich  | Wirkarbeit | Zählerstand | halbjährlich         | Erzeugung                          | X                                                            | --                                                           | X                                                             |
| 9991 00000 017 7⁶   | Messlokation mit Wahlmöglichkeit der Zuordnung einer Zählzeit für Wirk-arbeit Verbrauch Zählerstand quartalsweise | Wirkarbeit | Zählerstand | quartals-weise       | Verbrauch                          | X                                                            | --                                                           | X                                                             |
| 9991 00000 018 8⁶ ⁷ | Messlokation mit Wahlmöglichkeit der Zuordnung einer Zählzeit für Wirk-arbeit Erzeugung Zählerstand quartalsweise | Wirkarbeit | Zählerstand | quartals-weise       | Erzeugung                          | X                                                            | --                                                           | X                                                             |


<sup>6</sup>Diese Messprodukte sind nur nutzbar, wenn die messtechnische Einordnung der Marktlokation, für die die Werte benötigt werden „kME/mME“ ist. Ist die messtechnische Einordnung der Marktlokation, für die die Werte benötigt werden, „iMS“ so liegt hier bereits eine Wertegranularität „monatlich“ gemäß WiM Teil 2, Kap. 2.5.5. Darstellung der zu übermittelnden Werte vor, weshalb die gekennzeichneten Messprodukte nicht ver-wendbar sind.

<sup>7</sup>Diesen Messprodukten ist nur dann eine Zählzeit zuordenbar, wenn diese für eine Marktlokation Verbrauch, die ebenfalls tarifiert werden muss benötigt wird. Werden die Messprodukte für eine Marktlokation Erzeugung benötigt, so ist keine Zuordnung einer Zählzeit möglich.

Version: 1.3c

11.12.2025

<page_number>Seite 10 von 58</page_number>

Codeliste der Konfigurationen

edi@energy. Datenformate Strom & Gas logo

| Messprodukt-Code¹ | Bezeichnung                                                                                                   | Wert       | Werteart    | Erfassungs-intervall | Energief-luss-rich-tung / Quadrant | Messprodukt ge-genüber MSB von Marktrolle bestell-bar<br/>NB | Messprodukt ge-genüber MSB von Marktrolle bestell-bar<br/>LF | Messprodukt ge-genüber MSB von Marktrolle bestell-bar<br/>MSB |
| ----------------- | ------------------------------------------------------------------------------------------------------------- | ---------- | ----------- | -------------------- | ---------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------- |
| 9991 00000 019 3  | Messlokation mit Wahlmöglichkeit der Zuordnung einer Zählzeit für Wirk-arbeit Verbrauch Zählerstand monatlich | Wirkarbeit | Zählerstand | monatlich            | Verbrauch                          | X                                                            | --                                                           | X                                                             |
| 9991 00000 020 0⁷ | Messlokation mit Wahlmöglichkeit der Zuordnung einer Zählzeit für Wirk-arbeit Erzeugung Zählerstand monatlich | Wirkarbeit | Zählerstand | monatlich            | Erzeugung                          | X                                                            | --                                                           | X                                                             |


Version: 1.3c

11.12.2025

Seite 11 von 58
<page_number>11</page_number>

Codeliste der Konfigurationen

edi@energy. Datenformate Strom & Gas logo

## 2.3.2 ohne Wahlmöglichkeit der Zuordnung einer Zählzeit

| Messprodukt-Code¹ | Bezeichnung                                                                                                          | Wert        | Werteart                    | Erfassungs-intervall | Energief-luss-rich-tung / Quadrant | Messprodukt gegen-über MSB von Marktrolle bestell-bar<br/>NB | Messprodukt gegen-über MSB von Marktrolle bestell-bar<br/>LF | Messprodukt gegen-über MSB von Marktrolle bestell-bar<br/>MSB |
| ----------------- | -------------------------------------------------------------------------------------------------------------------- | ----------- | --------------------------- | -------------------- | ---------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------- |
| 9991 00000 021 8  | Messlokation ohne Wahlmöglichkeit der Zuordnung einer Zählzeit für Wirkarbeit Verbrauch Lastgang 1/4 stündlich       | Wirkarbeit  | Lastgang                    | 1/4 stünd-lich       | Verbrauch                          | X                                                            | --                                                           | X                                                             |
| 9991 00000 022 6  | Messlokation ohne Wahlmöglichkeit der Zuordnung einer Zählzeit für Wirkarbeit Erzeugung Lastgang 1/4 stündlich       | Wirkarbeit  | Lastgang                    | 1/4 stünd-lich       | Erzeugung                          | X                                                            | --                                                           | X                                                             |
| 9991 00000 023 4  | Messlokation ohne Wahlmöglichkeit der Zuordnung einer Zählzeit für Blindarbeit Verbrauch Lastgang 1/4 stündlich      | Blindarbeit | Lastgang                    | 1/4 stünd-lich       | Q1/Q4                              | X                                                            | --                                                           | X                                                             |
| 9991 00000 024 2  | Messlokation ohne Wahlmöglichkeit der Zuordnung einer Zählzeit für Blindarbeit Erzeugung Lastgang 1/4 stündlich      | Blindarbeit | Lastgang                    | 1/4 stünd-lich       | Q2/Q3                              | X                                                            | --                                                           | X                                                             |
| 9991 00000 025 0⁸ | Messlokation ohne Wahlmöglichkeit der Zuordnung einer Zählzeit für Wirkarbeit Verbrauch höchste 1/4 Stunde im Monat  | Wirkarbeit  | höchste 1/4 Stunde im Monat | --                   | Verbrauch                          | X                                                            | --                                                           | X                                                             |
| 9991 00000 026 8⁹ | Messlokation ohne Wahlmöglichkeit der Zuordnung einer Zählzeit für Wirkarbeit Erzeugung höchste 1/4 Stunde im Monat  | Wirkarbeit  | höchste 1/4 Stunde im Monat | --                   | Erzeugung                          | X                                                            | --                                                           | X                                                             |
| 9991 00000 027 6  | Messlokation ohne Wahlmöglichkeit der Zuordnung einer Zählzeit für Blindarbeit Verbrauch höchste 1/4 Stunde im Monat | Blindarbeit | höchste 1/4 Stunde im Monat | --                   | Q1/Q4                              | X                                                            | --                                                           | X                                                             |
| 9991 00000 028 4  | Messlokation ohne Wahlmöglichkeit der Zuordnung einer Zählzeit für Blindarbeit Erzeugung höchste 1/4 Stunde im Monat | Blindarbeit | höchste 1/4 Stunde im Monat | --                   | Q2/Q3                              | X                                                            | --                                                           | X                                                             |
| 9991 00000 029 2  | Messlokation ohne Wahlmöglichkeit der Zuordnung einer Zählzeit für Blindarbeit Verbrauch Zählerstand jährlich        | Blindarbeit | Zählerstand                 | jährlich             | Q1/Q4                              | X                                                            | --                                                           | X                                                             |


<sup>8</sup>Das Messprodukt mit dem Code 9991 00000 025 0 ist nur bestellbar, wenn zusätzlich eines der Messprodukte mit dem Code 9991 00000 015 1 oder 9991 00000 051 5 oder 9991 00000 017 7 oder 9991 00000 019 3 bestellt wird.

<sup>9</sup>Das Messprodukt mit dem Code 9991 00000 026 8 ist nur bestellbar, wenn zusätzlich eines der Messprodukte mit dem Code 9991 00000 016 9 oder 9991 00000 052 3 oder 9991 00000 018 8 oder 9991 00000 020 0 bestellt wird.

Version: 1.3c

11.12.2025

<page_number>Seite 12 von 58</page_number>

Codeliste der Konfigurationen

edi@energy. Datenformate Strom & Gas logo

| Messprodukt-Code¹ | Bezeichnung                                                                                                        | Wert        | Werteart    | Erfassungs-intervall | Energief-luss-rich-tung / Quadrant | Messprodukt gegen-über MSB von Marktrolle bestell-bar<br/>NB | Messprodukt gegen-über MSB von Marktrolle bestell-bar<br/>LF | Messprodukt gegen-über MSB von Marktrolle bestell-bar<br/>MSB |
| ----------------- | ------------------------------------------------------------------------------------------------------------------ | ----------- | ----------- | -------------------- | ---------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------- |
| 9991 00000 030 9  | Messlokation ohne Wahlmöglichkeit der Zuordnung einer Zählzeit für Blindarbeit Erzeugung Zählerstand jährlich      | Blindarbeit | Zählerstand | jährlich             | Q2/Q3                              | X                                                            | --                                                           | X                                                             |
| 9991 00000 053 1  | Messlokation ohne Wahlmöglichkeit der Zuordnung einer Zählzeit für Blindarbeit Verbrauch Zählerstand halbjährlich  | Blindarbeit | Zählerstand | halbjährlich         | Q1/Q4                              | X                                                            | --                                                           | X                                                             |
| 9991 00000 054 9  | Messlokation ohne Wahlmöglichkeit der Zuordnung einer Zählzeit für Blindarbeit Erzeugung Zählerstand halbjährlich  | Blindarbeit | Zählerstand | halbjährlich         | Q2/Q3                              | X                                                            | --                                                           | X                                                             |
| 9991 00000 031 7  | Messlokation ohne Wahlmöglichkeit der Zuordnung einer Zählzeit für Blindarbeit Verbrauch Zählerstand quartalsweise | Blindarbeit | Zählerstand | quartals-weise       | Q1/Q4                              | X                                                            | --                                                           | X                                                             |
| 9991 00000 032 5  | Messlokation ohne Wahlmöglichkeit der Zuordnung einer Zählzeit für Blindarbeit Erzeugung Zählerstand quartalsweise | Blindarbeit | Zählerstand | quartals-weise       | Q2/Q3                              | X                                                            | --                                                           | X                                                             |
| 9991 00000 033 3  | Messlokation ohne Wahlmöglichkeit der Zuordnung einer Zählzeit für Blindarbeit Verbrauch Zählerstand monatlich     | Blindarbeit | Zählerstand | monatlich            | Q1/Q4                              | X                                                            | --                                                           | X                                                             |
| 9991 00000 034 1  | Messlokation ohne Wahlmöglichkeit der Zuordnung einer Zählzeit für Blindarbeit Erzeugung Zählerstand monatlich     | Blindarbeit | Zählerstand | monatlich            | Q2/Q3                              | X                                                            | --                                                           | X                                                             |


Version: 1.3c

11.12.2025

<page_number>Seite 13 von 58</page_number>

Codeliste der Konfigurationen

edi@energy. Datenformate Strom & Gas logo

# 2.4 Standard-Messprodukte der Netzlokation

| Messprodukt-Code¹ | Bezeichnung                                                                                                | Wert        | Werteart                    | Wertegranularität | Messprodukt gegenüber MSB von Marktrolle bestellbar<br/>NB | Messprodukt gegenüber MSB von Marktrolle bestellbar<br/>LF | Messprodukt gegenüber MSB von Marktrolle bestellbar<br/>MSB |
| ----------------- | ---------------------------------------------------------------------------------------------------------- | ----------- | --------------------------- | ----------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ----------------------------------------------------------- |
| 9991 00000 065 6  | Netzlokation ohne Wahlmöglichkeit der Zuordnung einer Zählzeit für Blindarbeit Lastgang 1/4 stündlich      | Blindarbeit | Lastgang                    | 1/4 stündlich     | X                                                          | --                                                         | --                                                          |
| 9991 00000 066 4  | Netzlokation ohne Wahlmöglichkeit der Zuordnung einer Zählzeit für Blindarbeit höchste 1/4 Stunde im Monat | Blindarbeit | höchste 1/4 Stunde im Monat | ---               | X                                                          | --                                                         | --                                                          |
| 9991 00000 067 2  | Netzlokation ohne Wahlmöglichkeit der Zuordnung einer Zählzeit für Blindarbeit Menge jährlich              | Blindarbeit | Menge                       | jährlich          | X                                                          | --                                                         | --                                                          |
| 9991 00000 068 0  | Netzlokation ohne Wahlmöglichkeit der Zuordnung einer Zählzeit für Blindarbeit Menge halbjährlich          | Blindarbeit | Menge                       | halbjährlich      | X                                                          | --                                                         | --                                                          |
| 9991 00000 069 8  | Netzlokation ohne Wahlmöglichkeit der Zuordnung einer Zählzeit für Blindarbeit Menge quartalsweise         | Blindarbeit | Menge                       | quartalsweise     | X                                                          | --                                                         | --                                                          |
| 9991 00000 070 5  | Netzlokation ohne Wahlmöglichkeit der Zuordnung einer Zählzeit für Blindarbeit Menge monatlich             | Blindarbeit | Menge                       | monatlich         | X                                                          | --                                                         | --                                                          |


Version: 1.3c

11.12.2025

<page_number>Seite 14 von 58</page_number>

Codeliste der Konfigurationen

edi@energy. Datenformate Strom & Gas logo

# 3 Codeliste der Standard-Messprodukte Gas

Dieses Kapitel enthält die Codelisten der Messprodukte Gas. Die Messprodukte werden per MSCONS in der Wertequalität, dem Übermittlungsin-tervall und der Frist nach WiM-Gas bereitgestellt.

| Messprodukt-Code¹  | Beschreibung                                             | Wert            | Werteart     | Wertegranularität /Erfassungsintervall¹⁰ | Energiefluss-richtung | Messprodukt gegenüber MSB von Marktrolle bestellbar<br/>NB | Messprodukt gegenüber MSB von Marktrolle bestellbar<br/>LF |
| ------------------ | -------------------------------------------------------- | --------------- | ------------ | ---------------------------------------- | --------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| 9991 00000 035 9   | Gas, Wirkarbeit Lastgang stündlich Verbrauch             | Wirkarbeit      | Lastgang     | stündlich                                | Verbrauch             | X                                                          | X                                                          |
| 9991 00000 040 8   | Gas, Wirkarbeit Menge jährlich Verbrauch                 | Wirkarbeit      | Arbeitsmenge | jährlich                                 | Verbrauch             | X                                                          | X                                                          |
| 9991 00000 062 2   | Gas, Wirkarbeit Menge halbjährlich Verbrauch             | Wirkarbeit      | Arbeitsmenge | halbjährlich                             | Verbrauch             | X                                                          | X                                                          |
| 9991 00000 063 0   | Gas, Wirkarbeit Menge quartalsweise Verbrauch            | Wirkarbeit      | Arbeitsmenge | quartalsweise                            | Verbrauch             | X                                                          | X                                                          |
| 9991 00000 061 4   | Gas, Wirkarbeit Menge monatlich Verbrauch                | Wirkarbeit      | Arbeitsmenge | monatlich                                | Verbrauch             | X                                                          | X                                                          |
| 9991 00000 038 3¹¹ | Gas, Betriebsvolumen Zählerstand jährlich Verbrauch      | Betriebsvolumen | Zählerstand  | jährlich                                 | Verbrauch             | X                                                          | X                                                          |
| 9991 00000 057 3¹² | Gas, Betriebsvolumen Zählerstand halbjährlich Verbrauch  | Betriebsvolumen | Zählerstand  | halbjährlich                             | Verbrauch             | X                                                          | X                                                          |
| 9991 00000 059 9¹³ | Gas, Betriebsvolumen Zählerstand quartalsweise Verbrauch | Betriebsvolumen | Zählerstand  | quartalsweise                            | Verbrauch             | X                                                          | X                                                          |
| 9991 00000 055 7¹⁴ | Gas, Betriebsvolumen Zählerstand monatlich Verbrauch     | Betriebsvolumen | Zählerstand  | monatlich                                | Verbrauch             | X                                                          | X                                                          |


<sup>10</sup>Wertegranularität bei Lastgang / Arbeitsmenge, Erfassungsintervall bei Zählerständen.

<sup>11</sup>Das Messprodukt mit dem Code 9991 00000 038 3 ist nur bestellbar, wenn das Messprodukt mit dem Code 9991 00000 039 1 nicht bestellt wird.

<sup>12</sup>Das Messprodukt mit dem Code 9991 00000 057 3 ist nur bestellbar, wenn das Messprodukt mit dem Code 9991 00000 058 1 nicht bestellt wird.

<sup>13</sup>Das Messprodukt mit dem Code 9991 00000 059 9 ist nur bestellbar, wenn das Messprodukt mit dem Code 9991 00000 060 6 nicht bestellt wird.

<sup>14</sup>Das Messprodukt mit dem Code 9991 00000 055 7 ist nur bestellbar, wenn das Messprodukt mit dem Code 9991 00000 056 5 nicht bestellt wird.

Version: 1.3c

11.12.2025

Seite 15 von 58
<page_number>15</page_number>

Codeliste der Konfigurationen

edi@energy. Datenformate Strom & Gas logo

| Messprodukt-Code¹  | Beschreibung                                         | Wert        | Werteart    | Wertegranularität / Erfassungsintervall¹⁰ | Energieflussrichtung | Messprodukt gegenüber MSB von Marktrolle bestellbar<br/>NB | Messprodukt gegenüber MSB von Marktrolle bestellbar<br/>LF |
| ------------------ | ---------------------------------------------------- | ----------- | ----------- | ----------------------------------------- | -------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| 9991 00000 039 1¹⁵ | Gas, Normvolumen Zählerstand jährlich Verbrauch      | Normvolumen | Zählerstand | jährlich                                  | Verbrauch            | X                                                          | X                                                          |
| 9991 00000 058 1¹⁶ | Gas, Normvolumen Zählerstand halbjährlich Verbrauch  | Normvolumen | Zählerstand | halbjährlich                              | Verbrauch            | X                                                          | X                                                          |
| 9991 00000 060 6¹⁷ | Gas, Normvolumen Zählerstand quartalsweise Verbrauch | Normvolumen | Zählerstand | quartalsweise                             | Verbrauch            | X                                                          | X                                                          |
| 9991 00000 056 5¹⁸ | Gas, Normvolumen Zählerstand monatlich Verbrauch     | Normvolumen | Zählerstand | monatlich                                 | Verbrauch            | X                                                          | X                                                          |


<sup>15</sup> Das Messprodukt mit dem Code 9991 00000 039 1 ist bestellbar, wenn das Messprodukt mit dem Code 9991 00000 038 3 nicht bestellt wird.

<sup>16</sup>Das Messprodukt mit dem Code 9991 00000 058 1 ist nur bestellbar, wenn das Messprodukt mit dem Code 9991 00000 057 3 nicht bestellt wird.

<sup>17</sup>Das Messprodukt mit dem Code 9991 00000 060 6 ist nur bestellbar, wenn das Messprodukt mit dem Code 9991 00000 059 9 nicht bestellt wird.

<sup>18</sup>Das Messprodukt mit dem Code 9991 00000 056 5 ist nur bestellbar, wenn das Messprodukt mit dem Code 9991 00000 055 7 nicht bestellt wird.

Version: 1.3c

11.12.2025

Seite 16 von 58
<page_number>16</page_number>

Codeliste der Konfigurationen

edi@energy. Datenformate Strom & Gas logo

# 4 Codelisten der Konfigurationsprodukte und Messprodukte für Werte nach Typ 2

Dieses Kapitel enthält die Codelisten der Konfigurations- und Messprodukteprodukte Strom. Die Konfigurationsprodukte Strom werden im Rahmen der Bestellung einer Konfiguration gemäß GPKE Teil 3, Kap. 1.3. bzw. im Rahmen der Anfrage zur Übermittlung von Werten durch den ESA gemäß WiM Teil 2, Kap. 4. verwendet.

## 4.1 Konfigurationsprodukte Schaltzeitdefinition

| Konfigurationsprodukt-Code¹ | Bezeichnung          | Ebene                | Konfigurationsprodukt gegenüber MSB von Marktrolle bestellbar<br/>NB | Konfigurationsprodukt gegenüber MSB von Marktrolle bestellbar<br/>LF | Konfigurationsprodukt gegenüber MSB von Marktrolle bestellbar<br/>MSB |
| --------------------------- | -------------------- | -------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | --------------------------------------------------------------------- |
| 9991 00000 071 3            | Schaltzeitdefinition | Steuerbare Ressource | X                                                                    | X                                                                    | X                                                                     |


## 4.2 Konfigurationsprodukte Leistungskurvendefinition

| Konfigurationsprodukt-Code¹ | Bezeichnung               | Ebene                                                 | Konfigurationsprodukt gegenüber MSB von Marktrolle bestellbar<br/>NB | Konfigurationsprodukt gegenüber MSB von Marktrolle bestellbar<br/>LF | Konfigurationsprodukt gegenüber MSB von Marktrolle bestellbar<br/>MSB |
| --------------------------- | ------------------------- | ----------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | --------------------------------------------------------------------- |
| 9991 00000 072 1            | Leistungskurvendefinition | Marktlokation, Netzlokation,<br/>Steuerbare Ressource | X                                                                    | X                                                                    | X                                                                     |


Version: 1.3c

11.12.2025

<page_number>Seite 17 von 58</page_number>

Codeliste der Konfigurationen

edi@energy. Datenformate Strom & Gas logo

## 4.3 Konfigurationsprodukte Ad-Hoc-Steuerkanal

| Konfigurationsprodukt-Code¹ | Bezeichnung        | Ebene                              | Konfigurationsprodukt gegenüber MSB von Marktrolle bestellbar<br/>NB | Konfigurationsprodukt gegenüber MSB von Marktrolle bestellbar<br/>LF | Konfigurationsprodukt gegenüber MSB von Marktrolle bestellbar<br/>MSB |
| --------------------------- | ------------------ | ---------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | --------------------------------------------------------------------- |
| 9991 00000 073 9            | Ad-Hoc-Steuerkanal | Netzlokation, Steuerbare Ressource | X                                                                    | X                                                                    | X                                                                     |


Version: 1.3c

11.12.2025

<page_number>Seite 18 von 58</page_number>

Codeliste der Konfigurationen

edi@energy. Datenformate Strom & Gas logo

# 4.4 Messprodukte mit Konfigurationserlaubnis für Werte nach Typ 2 aus SMGW

| Messprodukt-Code¹ | Bezeichnung                                                  | Übertragungsweg | Ebene        | Werteart           | Auslöser | Erfassungsintervall | Übermittlungsintervall | Frist            | Zuordnung Zählzeit möglich | Wertequalität | Konfigurations-Priorität¹⁹               | Messprodukt gegenüber MSB von Marktrolle bestellbar<br/>NB | Messprodukt gegenüber MSB von Marktrolle bestellbar<br/>LF | Messprodukt gegenüber MSB von Marktrolle bestellbar<br/>MSB |
| ----------------- | ------------------------------------------------------------ | --------------- | ------------ | ------------------ | -------- | ------------------- | ---------------------- | ---------------- | -------------------------- | ------------- | ---------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ----------------------------------------------------------- |
| 9991 00000 081 2  | Messlokation, Netzzustandsdaten, 1 Min.                      | aus dem SMGW    | Messlokation | Siehe Kap. 4.7.2²⁰ | --       | 1 Min.              | 1 Min.                 | Direktverbindung | nein                       | Werte²¹       | Prio 1: Energiewirtschaftliche Grundlage | X                                                          | --                                                         | --                                                          |
| 9991 00000 082 0  | Messlokation, Netzzustandsdaten, 10 Min.                     | aus dem SMGW    | Messlokation | Siehe Kap. 4.7.2²⁰ | --       | 10 Min.             | 10 Min.                | Direktverbindung | nein                       | Werte²¹       | Prio 1: Energiewirtschaftliche Grundlage | X                                                          | --                                                         | --                                                          |
| 9991 00000 083 8  | Messlokation, Netzzustandsdaten, 15 Min.                     | aus dem SMGW    | Messlokation | Siehe Kap. 4.7.2²⁰ | --       | 15 Min.             | 15 Min.                | Direktverbindung | nein                       | Werte²¹       | Prio 1: Energiewirtschaftliche Grundlage | X                                                          | --                                                         | --                                                          |
| 9991 00000 084 6  | Messlokation, Netzzustandsdaten, zur einmaligen Übermittlung | aus dem SMGW    | Messlokation | Siehe Kap. 4.7.2²⁰ | --       | ad-hoc              | ad-hoc                 | Direktverbindung | nein                       | Werte²¹       | Prio 1: Energiewirtschaftliche Grundlage | X                                                          | --                                                         | --                                                          |
| 9991 00000 085 4  | Messlokation, Netzzustandsdaten, täglich,                    | aus dem SMGW    | Messlokation | Siehe Kap. 4.7.2²⁰ | --       | 1 Min.              | Täglich                | Direktverbindung | nein                       | Werte²¹       | Prio 1: Energiewirtschaftliche Grundlage | X                                                          | --                                                         | --                                                          |


<sup>19</sup> Konfigurations-Priorität wird berücksichtigt, wenn Kapazitätsgrenzen der Messtechnik erreicht wird inkl. Kommunikation.

<sup>20</sup> Die Art der Werte für dieses Messprodukt sind in Kapitel 4.7.2 der Codeliste der Konfigurationen beschrieben.

<sup>21</sup> Rohdatenstand zum Zeitpunkt der Übermittlungsfrist ohne Plausibilisierung, Ersatzwertbildung und Aktualisierung bei Störungsbeseitigung.

Version: 1.3c

11.12.2025

Seite 19 von 58
<page_number>19</page_number>

Codeliste der Konfigurationen

edi@energy. Datenformate Strom & Gas logo

| Messprodukt-Code¹ | Bezeichnung                                                                                          | Übertragungsweg | Ebene        | Werteart           | Auslöser                                | Erfassungsintervall | Übermittlungsintervall | Frist            | Zuordnung Zählzeit möglich | Wertequalität | Konfigurations-Priorität¹⁹                | Messprodukt gegenüber MSB von Marktrolle bestellbar<br/>NB | Messprodukt gegenüber MSB von Marktrolle bestellbar<br/>LF | Messprodukt gegenüber MSB von Marktrolle bestellbar<br/>MSB |
| ----------------- | ---------------------------------------------------------------------------------------------------- | --------------- | ------------ | ------------------ | --------------------------------------- | ------------------- | ---------------------- | ---------------- | -------------------------- | ------------- | ----------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ----------------------------------------------------------- |
| 9991 00000 154 7  | Erfassungsintervall 1 Min.<br/>Messlokation, Netzzustandsdaten, täglich, Erfassungsintervall 15 Min. | aus dem SMGW    | Messlokation | Siehe Kap. 4.7.2²⁰ | --                                      | 15 Min.             | Täglich                | Direktverbindung | nein                       | Werte²¹       | Prio 1: Energiewirtschaftliche Grundlage  | X                                                          | --                                                         | --                                                          |
| 9991 00000 086 2  | Messlokation, Netzzustandsdaten, Spannung                                                            | aus dem SMGW    | Messlokation | Siehe Kap. 4.7.4²² | --                                      | 1 Min.              | 1 Min.                 | Direktverbindung | nein                       | Werte²¹       | Prio 1: Energiewirtschaftliche Grundlage  | X                                                          | --                                                         | --                                                          |
| 9991 00000 087 0  | Messlokation, Netzzustandsdaten, Schwellwert                                                         | aus dem SMGW    | Messlokation | Siehe Kap. 4.7.2²⁰ | Bei Schwellwertunter- / -überschreitung | 1 Min.              | 1 Min.                 | Direktverbindung | nein                       | Werte²¹       | Prio 1: Energiewirtschaftliche Grundlage  | X                                                          | --                                                         | --                                                          |
| 9991 00000 088 8  | Messlokation, Ist-Einspeisung, 1 Min.                                                                | aus dem SMGW    | Messlokation | Siehe Kap. 4.7.1²³ | --                                      | 1 Min.              | 1 Min.                 | Direktverbindung | nein                       | Werte²¹       | Prio 2: Vertragliche Grundlage mit AN/ANN | X                                                          | X                                                          | --                                                          |
| 9991 00000 089 6  | Messlokation, Ist-Einspeisung, 15 Min.                                                               | aus dem SMGW    | Messlokation | Siehe Kap. 4.7.1²³ | --                                      | 15 Min.             | 15 Min.                | Direktverbindung | nein                       | Werte²¹       | Prio 2: Vertragliche Grundlage mit AN/ANN | X                                                          | X                                                          | --                                                          |


<sup>22</sup> Die Art der Werte für dieses Messprodukt sind in Kapitel 4.7.4 der Codeliste der Konfigurationen beschrieben.

<sup>23</sup> Die Art der Werte für dieses Messprodukt sind in Kapitel 4.7.1 der Codeliste der Konfigurationen beschrieben.

Version: 1.3c

11.12.2025

Seite <page_number>20</page_number> von 58

Codeliste der Konfigurationen

edi@energy. Datenformate Strom & Gas logo

| Messprodukt- Code¹ | Bezeichnung                                                      | Übertra- gungsweg | Ebene          | Werteart           | Auslöser                                         | Erfas- sungsin- tervall | Über- mitt- lungsin- tervall | Frist              | Zuord- nung Zählzeit möglich | Wer- tequali- tät | Konfigurations- Priorität¹⁹                 | Messprodukt gegen- über MSB von Markt- rolle bestellbar<br/>NB | Messprodukt gegen- über MSB von Markt- rolle bestellbar<br/>LF | Messprodukt gegen- über MSB von Markt- rolle bestellbar<br/>MSB |
| ------------------ | ---------------------------------------------------------------- | ----------------- | -------------- | ------------------ | ------------------------------------------------ | ----------------------- | ---------------------------- | ------------------ | ---------------------------- | ----------------- | ------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | --------------------------------------------------------------- |
| 9991 00000 090 3   | Messlokation, Ist-Einspei- sung, zur ein- maligen Über- mittlung | aus dem SMGW      | Messlo- kation | Siehe Kap. 4.7.1²³ | --                                               | ad-hoc                  | ad-hoc                       | Direktver- bindung | nein                         | Werte²¹           | Prio 2: Vertragli- che Grundlage mit AN/ANN | X                                                              | X                                                              | --                                                              |
| 9991 00000 091 1   | Messlokation, Ist-Einspei- sung, Schwell- wert                   | aus dem SMGW      | Messlo- kation | Siehe Kap. 4.7.1²³ | Bei Schwell- wertun- ter- / - über- schrei- tung | 1 Min.                  | 1 Min.                       | Direktver- bindung | nein                         | Werte²¹           | Prio 2: Vertragli- che Grundlage mit AN/ANN | X                                                              | X                                                              | --                                                              |
| 9991 00000 092 9   | Messlokation, Mehrwert- dienste, 1 Min.                          | aus dem SMGW      | Messlo- kation | Siehe Kap. 4.7.3²⁴ | --                                               | 1 Min.                  | 1 Min.                       | Direktver- bindung | nein                         | Werte²¹           | Prio 2: Vertragli- che Grundlage mit AN/ANN | X                                                              | X                                                              | X                                                               |
| 9991 00000 093 7   | Messlokation, Mehrwert- dienste, 15 Min.                         | aus dem SMGW      | Messlo- kation | Siehe Kap. 4.7.3²⁴ | --                                               | 15 Min.                 | 15 Min.                      | Direktver- bindung | nein                         | Werte²¹           | Prio 2: Vertragli- che Grundlage mit AN/ANN | X                                                              | X                                                              | X                                                               |


<sup>24</sup> Die Art der Werte für dieses Messprodukt sind in Kapitel 4.7.3 der Codeliste der Konfigurationen beschrieben.

Version: 1.3c

11.12.2025

<page_number>Seite 21 von 58</page_number>

Codeliste der Konfigurationen

edi@energy. Datenformate Strom & Gas logo

| Messprodukt-Code¹ | Bezeichnung                                                | Übertragungsweg         | Ebene               | Werteart           | Auslöser                                | Erfassungsintervall | Übermittlungsintervall | Frist            | Zuordnung Zählzeit möglich | Wertequalität | Konfigurations-Priorität¹⁹                | Messprodukt gegenüber MSB von Marktrolle bestellbar<br/>NB | Messprodukt gegenüber MSB von Marktrolle bestellbar<br/>LF | Messprodukt gegenüber MSB von Marktrolle bestellbar<br/>MSB |
| ----------------- | ---------------------------------------------------------- | ----------------------- | ------------------- | ------------------ | --------------------------------------- | ------------------- | ---------------------- | ---------------- | -------------------------- | ------------- | ----------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ----------------------------------------------------------- |
| 9991 00000 094 5  | Messlokation, Mehrwertdienste, zur einmaligen Übermittlung | aus dem SMGW            | Messlokation        | Siehe Kap. 4.7.3²⁴ | --                                      | ad-hoc              | ad-hoc                 | Direktverbindung | nein                       | Werte²¹       | Prio 2: Vertragliche Grundlage mit AN/ANN | X                                                          | X                                                          | X                                                           |
| 9991 00000 095 3  | Messlokation, Mehrwertdienste, Schwellwert                 | aus dem SMGW            | Messlokation        | Siehe Kap. 4.7.3²⁴ | Bei Schwellwertunter- / -überschreitung | 1 Min.              | 1 Min.                 | Direktverbindung | nein                       | Werte²¹       | Prio 2: Vertragliche Grundlage mit AN/ANN | X                                                          | X                                                          | X                                                           |
| 9991 00000 143 0  | CLS-HKS3                                                   | CLS-Direkt aus dem SMGW | Steuerbare Resource | --                 | --                                      | --                  | ad-hoc                 | Direktverbindung | nein                       | Werte²¹       | Prio 2: Vertragliche Grundlage mit AN/ANN | X                                                          | X                                                          |                                                             |
| 9991 00000 144 8  | CLS-HKS4                                                   | CLS-Direkt aus dem SMGW | Steuerbar Resource  | --                 | --                                      | --                  | ad-hoc                 | Direktverbindung | nein                       | Werte²¹       | Prio 2: Vertragliche Grundlage mit AN/ANN | X                                                          | X                                                          |                                                             |
| 9991 00000 145 6  | CLS-HKS5                                                   | CLS-Direkt aus dem SMGW | Steuerbare Resource | --                 | --                                      | --                  | zyklisch               | Direktverbindung | nein                       | Werte²¹       | Prio 2: Vertragliche Grundlage mit AN/ANN | X                                                          | X                                                          |                                                             |


Version: 1.3c

11.12.2025

<page_number>Seite 22 von 58</page_number>

Codeliste der Konfigurationen

edi@energy. Datenformate Strom & Gas

## 4.5 Messprodukte für Werte nach Typ 2 aus Backend für LF und NB

Derzeit sind keine Messprodukte zur Übermittlung von Werten nach Typ 2 aus dem Backend vorhanden.

Version: 1.3c

11.12.2025

Seite <page_number>23</page_number> von 58

Codeliste der Konfigurationen

edi@energy. Datenformate Strom & Gas logo

# 4.6 Codelisten der Messprodukte Strom für ESA

Die Produkte können ausschließlich von der Marktrolle ESA gegenüber dem MSB bestellt werden.

## 4.6.1 Werte nach Typ 2 aus Backend

| Messprodukt-Code¹ | Bezeichnung                                                                 | Übertragungs-weg | Ebene         | Wert         | Werteart | Werte-granularität | Energief-lussrich-tung / Quadran-ten | Zuord-nung Zählzeit möglich | Über-mitt-lungsin-tervall | Frist                                           | Wer-tequali-tät | Pflicht²⁵ / Op-tional | Nutzbar ab            |
| ----------------- | --------------------------------------------------------------------------- | ---------------- | ------------- | ------------ | -------- | ------------------ | ------------------------------------ | --------------------------- | ------------------------- | ----------------------------------------------- | --------------- | --------------------- | --------------------- |
| 9991 00000 041 6  | ESA, Messlo-kation Wirk-arbeit Last-gang Ver-brauch 1/4 stündlich, Rohdaten | EDIFACT          | Messloka-tion | Wirkarbeit   | Lastgang | 1/4 stünd-lich     | Ver-brauch                           | nein                        | täglich                   | unverzüg-lich, je-doch spä-testens bis 9:30 Uhr | Werte²¹         | Optional              | 01.04.2022, 00:00 Uhr |
| 9991 00000 042 4  | ESA, Messlo-kation Wirk-arbeit Last-gang Erzeu-gung 1/4 stündlich, Rohdaten | EDIFACT          | Messloka-tion | Wirkarbeit   | Lastgang | 1/4 stünd-lich     | Erzeu-gung                           | nein                        | täglich                   | unverzüg-lich, je-doch spä-testens bis 9:30 Uhr | Werte²¹         | Optional              | 01.04.2022, 00:00 Uhr |
| 9991 00000 045 8  | ESA, Messlo-kation Blind-arbeit Last-gang                                   | EDIFACT          | Messloka-tion | Blindar-beit | Lastgang | 1/4 stünd-lich     | Q1/Q4                                | nein                        | täglich                   | unverzüg-lich, je-doch                          | Werte²¹         | Optional              | 01.04.2022, 00:00 Uhr |


<sup>25</sup> Die Pflicht, zur Übermittlung von Messwerten an den ESA auf dessen Verlangen, ergibt sich aus der BNetzA Mitteilung Nr. 3 zur Umsetzung des Beschlusses WiM vom 07.02.2024.

Version: 1.3c

11.12.2025

<page_number>Seite 24 von 58</page_number>

Codeliste der Konfigurationen

edi@energy. Datenformate Strom & Gas logo

| Messprodukt-Code¹ | Bezeichnung                                                                                       | Übertragungs-weg | Ebene         | Wert        | Werteart | Werte-granulari-tät | Energieflussrich-tung / Quadranten | Zuordnung Zählzeit möglich | Übermitt-lungsintervall      | Frist                                        | Wertequali-tät               | Pflicht²⁵ / Optional | Nutzbar ab            |
| ----------------- | ------------------------------------------------------------------------------------------------- | ---------------- | ------------- | ----------- | -------- | ------------------- | ---------------------------------- | -------------------------- | ---------------------------- | -------------------------------------------- | ---------------------------- | -------------------- | --------------------- |
| 9991 00000 046 6  | ESA, Messlokation Blindarbeit Lastgang Erzeugung 1/4 stündlich, Rohdaten                          | EDIFACT          | Messlokation  | Blindarbeit | Lastgang | 1/4 stündlich       | Q2/Q3                              | nein                       | täglich                      | unverzüglich, jedoch spätestens bis 9:30 Uhr | Werte²¹                      | Optional             | 01.04.2022, 00:00 Uhr |
| 9991 00000 074 7  | ESA, Marktlokation Wirkarbeit Lastgang Verbrauch oder Erzeugung 1/4 stündlich, aufbereitete Daten | EDIFACT          | Marktlokation | Wirkarbeit  | Lastgang | 1/4 stündlich       | Verbrauch / Erzeugung              | nein                       | gemäß WiM Teil 2, Kap. 2.5.5 | gemäß WiM Teil 2, Kap. 2.5.5                 | gemäß WiM Teil 2, Kap. 2.5.5 | Optional             | 01.10.2023, 00:00 Uhr |
| 9991 00000 305 6  | ESA, Marktlokation Wirkarbeit Lastgang Verbrauch oder Erzeugung 1/4 stündlich, aufbereitete Daten | EDIFACT          | Marktlokation | Wirkarbeit  | Lastgang | 1/4 stündlich       | Verbrauch / Erzeugung              | nein                       | gemäß WiM Teil 2, Kap. 2.5.5 | gemäß WiM Teil 2, Kap. 2.5.5                 | gemäß WiM Teil 2, Kap. 2.5.5 | Pflicht              | 06.08.2024, 00:00 Uhr |
| 9991 00000 075 5  | ESA, Tranche Wirkarbeit Lastgang                                                                  | EDIFACT          | Tranche       | Wirkarbeit  | Lastgang | 1/4 stündlich       | Erzeugung                          | nein                       | gemäß WiM Teil               | gemäß WiM Teil                               | gemäß WiM Teil               | Optional             | 01.10.2023, 00:00 Uhr |


Version: 1.3c

11.12.2025

<page_number>Seite 25 von 58</page_number>

# Codeliste der Konfigurationen

edi@energy Datenformate Strom & Gas logo

| Messprodukt- Code¹ | Bezeichnung                                                                     | Übertra- gungs- weg | Ebene           | Wert          | Werteart | Werte- granula- rität | Energief- lussrich- tung / Quadran- ten | Zuord- nung Zählzeit möglich | Über- mitt- lungsin- tervall | Frist                        | Wer- tequali- tät            | Pflicht²⁵ / Op- tional                           | Nutzbar ab            |
| ------------------ | ------------------------------------------------------------------------------- | ------------------- | --------------- | ------------- | -------- | --------------------- | --------------------------------------- | ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- | ------------------------------------------------ | --------------------- |
|                    | Erzeugung 1/4 stündlich, aufbereitete Daten                                     |                     |                 |               |          |                       |                                         |                              | 2, Kap. 2.5.5                | 2, Kap. 2.5.5                | 2, Kap. 2.5.5                |                                                  |                       |
| 9991 00000 306 4   | ESA, Tranche Wirkarbeit Lastgang Er- zeugung 1/4 stündlich, aufbereitete Daten  | EDIFACT             | Tranche         | Wirkarbeit    | Lastgang | 1/4 stünd- lich       | Erzeu- gung                             | nein                         | gemäß WiM Teil 2, Kap. 2.5.5 | gemäß WiM Teil 2, Kap. 2.5.5 | gemäß WiM Teil 2, Kap. 2.5.5 | Pflicht                                          | 06.08.2024, 00:00 Uhr |
| 9991 00000 153 9⁵  | ESA, Marktlo- kation Blind- arbeit Last- gang 1/4 stündlich, aufbereitete Daten | EDIFACT             | Marktlo- kation | Blindar- beit | Lastgang | 1/4 stünd- lich       | Ver- brauch / Erzeu- gung               | nein                         | gemäß WiM Teil 2, Kap. 2.5.5 | gemäß WiM Teil 2, Kap. 2.5.5 | gemäß WiM Teil 2, Kap. 2.5.5 | Optional                                         | 01.10.2023, 00:00 Uhr |
| 9991 00000 076 3   | ESA, Netzlo- kation Blind- arbeit Last- gang 1/4 stündlich, aufbereitete Daten  | EDIFACT             | Netzloka- tion  | Blindar- beit | Lastgang | 1/4 stünd- lich       | Ver- brauch / Erzeu- gung               | nein                         | gemäß WiM Teil 2, Kap. 2.5.5 | gemäß WiM Teil 2, Kap. 2.5.5 | gemäß WiM Teil 2, Kap. 2.5.5 | Optional                                         | 01.01.2024, 00:00 Uhr |
| 9991 00000 077 1   | ESA, Messlo- kation Wirk- arbeit Last- gang Ver- brauch 1/4 stündlich,          | EDIFACT             | Messloka- tion  | Wirkarbeit    | Lastgang | 1/4 stünd- lich       | Ver- brauch                             | nein                         | gemäß WiM Teil 2, Kap. 2.5.5 | gemäß WiM Teil 2, Kap. 2.5.5 | gemäß WiM Teil 2, Kap. 2.5.5 | Optional ab 01.10.2023, 00:00 Uhr<br/>Pflicht ab | 01.10.2023, 00:00 Uhr |


Version: 1.3c

11.12.2025

Seite 26 von 58
<page_number>26</page_number>

Codeliste der Konfigurationen

edi@energy. Datenformate Strom & Gas logo

| Messprodukt-Code¹ | Bezeichnung                                                                          | Übertragungs-weg | Ebene        | Wert        | Werteart         | Werte-granulari-tät | Energieflussrich-tung / Quadranten | Zuordnung Zählzeit möglich | Übermittlungsin-tervall      | Frist                                        | Wertequali-tät               | Pflicht²⁵ / Optional                                                  | Nutzbar ab            |
| ----------------- | ------------------------------------------------------------------------------------ | ---------------- | ------------ | ----------- | ---------------- | ------------------- | ---------------------------------- | -------------------------- | ---------------------------- | -------------------------------------------- | ---------------------------- | --------------------------------------------------------------------- | --------------------- |
|                   | aufbereitete Daten                                                                   |                  |              |             |                  |                     |                                    |                            |                              |                                              |                              | 06.08.2024 00:00 Uhr                                                  |                       |
| 9991 00000 078 9  | ESA, Messlokation Wirk-arbeit Lastgang Erzeu-gung 1/4 stündlich, aufbereitete Daten  | EDIFACT          | Messlokation | Wirkarbeit  | Lastgang         | 1/4 stündlich       | Erzeugung                          | nein                       | gemäß WiM Teil 2, Kap. 2.5.5 | gemäß WiM Teil 2, Kap. 2.5.5                 | gemäß WiM Teil 2, Kap. 2.5.5 | Optional ab 01.10.2023, 00:00 Uhr<br/>Pflicht ab 06.08.2024 00:00 Uhr | 01.10.2023, 00:00 Uhr |
| 9991 00000 079 7  | ESA, Messlokation Blind-arbeit Lastgang Ver-brauch 1/4 stündlich, aufbereitete Daten | EDIFACT          | Messlokation | Blindarbeit | Lastgang         | 1/4 stündlich       | Q1/Q4                              | nein                       | gemäß WiM Teil 2, Kap. 2.5.5 | gemäß WiM Teil 2, Kap. 2.5.5                 | gemäß WiM Teil 2, Kap. 2.5.5 | Optional                                                              | 01.10.2023, 00:00 Uhr |
| 9991 00000 080 4  | ESA, Messlokation Blind-arbeit Lastgang Erzeu-gung 1/4 stündlich, aufbereitete Daten | EDIFACT          | Messlokation | Blindarbeit | Lastgang         | 1/4 stündlich       | Q2/Q3                              | nein                       | gemäß WiM Teil 2, Kap. 2.5.5 | gemäß WiM Teil 2, Kap. 2.5.5                 | gemäß WiM Teil 2, Kap. 2.5.5 | Optional                                                              | 01.10.2023, 00:00 Uhr |
| 9991 00000 150 5  | ESA, Messlokation Zähler-standsgang Erzeugung                                        | EDIFACT          | Messlokation | Wirkarbeit  | Zählerstandsgang | 1/4 stündlich       | Erzeugung                          | nein                       | täglich                      | unverzüglich, jedoch spätestens bis 9:30 Uhr | Werte²¹                      | Optional                                                              | 01.08.2023, 00:00 Uhr |


Version: 1.3c

11.12.2025

Seite 27 von 58
<page_number>27</page_number>

Codeliste der Konfigurationen

edi@energy. Datenformate Strom & Gas logo

| Messprodukt-Code¹ | Bezeichnung                                                                                                   | Übertragungsweg | Ebene               | Wert       | Werteart                     | Werte-granulari-tät         | Energieflussrichtung / Quadranten     | Zuordnung Zählzeit möglich | Übermittlungsintervall                   | Frist                                                              | Wertequalität                            | Pflicht²⁵ / Optional | Nutzbar ab                |
| ----------------- | ------------------------------------------------------------------------------------------------------------- | --------------- | ------------------- | ---------- | ---------------------------- | --------------------------- | ------------------------------------- | -------------------------- | ---------------------------------------- | ------------------------------------------------------------------ | ---------------------------------------- | -------------------- | ------------------------- |
| 9991 00000 151 3  | 1/4 stündlich,<br/>Rohdaten<br/>ESA, Marktlo-<br/>kation Zähler-<br/>standsgang<br/>Verbrauch /<br/>Erzeugung | EDIFACT         | Marktlo-<br/>kation | Wirkarbeit | Zähler-<br/>stands-<br/>gang | 1/4<br/>stünd-<br/>lich     | Erzeu-<br/>gung /<br/>Ver-<br/>brauch | nein                       | täglich                                  | unverzüg-<br/>lich, je-<br/>doch spä-<br/>testens bis<br/>9:30 Uhr | Werte²¹                                  | Optional             | 01.08.2023,<br/>00:00 Uhr |
| 9991 00000 152 1  | 1/4 stündlich,<br/>Rohdaten<br/>ESA, Messlo-<br/>kation Zähler-<br/>standsgang<br/>Verbrauch                  | EDIFACT         | Messloka-<br/>tion  | Wirkarbeit | Zähler-<br/>stands-<br/>gang | 1/4<br/>stünd-<br/>lich     | Ver-<br/>brauch                       | nein                       | täglich                                  | unverzüg-<br/>lich, je-<br/>doch spä-<br/>testens bis<br/>9:30 Uhr | Werte²¹                                  | Optional             | 01.08.2023,<br/>00:00 Uhr |
| 9991 00000 314 7  | 1/4 stündlich,<br/>Rohdaten<br/>ESA, Marktlo-<br/>kation, Ener-<br/>giemenge,<br/>aufbereitete<br/>Daten      | EDIFACT         | Marktlo-<br/>kation | Wirkarbeit | Arbeits-<br/>menge           | Zeitin-<br/>ter-<br/>vall²⁶ | Erzeu-<br/>gung /<br/>Ver-<br/>brauch | Nein                       | gemäß<br/>WiM Teil<br/>2, Kap.<br/>2.5.5 | gemäß<br/>WiM Teil<br/>2, Kap.<br/>2.5.5                           | gemäß<br/>WiM Teil<br/>2, Kap.<br/>2.5.5 | Pflicht              | 06.08.2024,<br/>00:00 Uhr |


<sup>26</sup> Identisch zum Zeitintervall für die Bereitstellung von Werten für den Zweck „Endkundenabrechnung/Netznutzungsabrechnung“ an den LF/NB.

Version: 1.3c

11.12.2025

Seite <page_number>28</page_number> von 58

Codeliste der Konfigurationen

edi@energy. Datenformate Strom & Gas

## 4.6.2 Werte nach Typ 2 aus SMGW

| Messprodukt-Code¹ | Bezeichnung                                                                         | Übertragungsweg | Ebene        | Wert       | Werteart | Wertegranularität | Energieflussrichtung / Quadranten | Zuordnung Zählzeit möglich | Übermittlungsintervall | Frist                                        | Wertequalität                 | Pflicht²⁵ / Optional | Nutzbar ab            |
| ----------------- | ----------------------------------------------------------------------------------- | --------------- | ------------ | ---------- | -------- | ----------------- | --------------------------------- | -------------------------- | ---------------------- | -------------------------------------------- | ----------------------------- | -------------------- | --------------------- |
| 9991 00000 043 2  | ESA, Messlokation Wirkarbeit Lastgang Verbrauch 1/4 stündlich aus dem SMGW          | aus dem SMGW    | Messlokation | Wirkarbeit | Lastgang | 1/4 stündlich     | Verbrauch                         | nein                       | täglich                | unverzüglich, jedoch spätestens bis 9:30 Uhr | Werte²¹                       | Optional             | 01.04.2022, 00:00 Uhr |
| 9991 00000 312 1  | ESA, Messlokation Wirkarbeit Lastgang Verbrauch 1/4 stündlich aus dem SMGW Rohdaten | aus dem SMGW    | Messlokation | Wirkarbeit | Lastgang | 1/4 stündlich     | Verbrauch                         | nein                       | täglich                | unverzüglich, jedoch spätestens bis 9:30 Uhr | gemäß WiM Teil 2, Kap. 2.5.5. | Pflicht              | 06.08.2024, 00:00 Uhr |
| 9991 00000 044 0  | ESA, Messlokation Wirkarbeit Lastgang Erzeugung 1/4 stündlich aus dem SMGW          | aus dem SMGW    | Messlokation | Wirkarbeit | Lastgang | 1/4 stündlich     | Erzeugung                         | nein                       | täglich                | unverzüglich, jedoch spätestens bis 9:30 Uhr | Werte²¹                       | Optional             | 01.04.2022, 00:00 Uhr |
| 9991 00000 313 9  | ESA, Messlokation Wirkarbeit Lastgang Erzeugung 1/4 stündlich aus dem SMGW          | aus dem SMGW    | Messlokation | Wirkarbeit | Lastgang | 1/4 stündlich     | Erzeugung                         | nein                       | täglich                | unverzüglich, jedoch spätestens bis 9:30 Uhr | gemäß WiM Teil 2, Kap. 2.5.5. | Pflicht              | 06.08.2024, 00:00 Uhr |


Version: 1.3c

11.12.2025

Seite 29 von 58
<page_number>29</page_number>

Codeliste der Konfigurationen

edi@energy. Datenformate Strom & Gas

| Messprodukt-Code¹ | Bezeichnung                                                                          | Übertragungsweg | Ebene        | Wert        | Werteart | Wertegranularität | Energieflussrichtung / Quadranten | Zuordnung Zählzeit möglich | Übermittlungsintervall | Frist                                        | Wertequalität | Pflicht²⁵ / Optional | Nutzbar ab            |
| ----------------- | ------------------------------------------------------------------------------------ | --------------- | ------------ | ----------- | -------- | ----------------- | --------------------------------- | -------------------------- | ---------------------- | -------------------------------------------- | ------------- | -------------------- | --------------------- |
| 9991 00000 047 4  | ESA, Messlokation Blindarbeit Lastgang Verbrauch 1/4 stündlich aus dem SMGW Rohdaten | aus dem SMGW    | Messlokation | Blindarbeit | Lastgang | 1/4 stündlich     | Q1/Q4                             | nein                       | täglich                | unverzüglich, jedoch spätestens bis 9:30 Uhr | Werte²¹       | Optional             | 01.04.2022, 00:00 Uhr |
| 9991 00000 048 2  | ESA, Messlokation Blindarbeit Lastgang Erzeugung 1/4 stündlich aus dem SMGW          | aus dem SMGW    | Messlokation | Blindarbeit | Lastgang | 1/4 stündlich     | Q2/Q3                             | nein                       | täglich                | unverzüglich, jedoch spätestens bis 9:30 Uhr | Werte²¹       | Optional             | 01.04.2022, 00:00 Uhr |


Version: 1.3c

11.12.2025

Seite 30 von 58
<page_number>30</page_number>

Codeliste der Konfigurationen

edi@energy. Datenformate Strom & Gas logo

| Messprodukt-Code¹ | Bezeichnung                                                  | Übertra-gungs-weg | Ebene         | Werteart           | Auslöser                                   | Erfas-sungs-inter-vall | Über-mitt-lungsin-tervall | Frist              | Zuord-nung Zählzeit möglich | Wer-tequalität | Konfigu-rations-Priori-tät²⁷                | Pflicht²⁵ / Optio-nal | Nutzbar ab            |
| ----------------- | ------------------------------------------------------------ | ----------------- | ------------- | ------------------ | ------------------------------------------ | ---------------------- | ------------------------- | ------------------ | --------------------------- | -------------- | ------------------------------------------- | --------------------- | --------------------- |
| 9991 00000 118 3  | Messloka-tion, Ist-Ein-speisung, 1 Min.                      | aus dem SMGW      | Messloka-tion | Siehe Kap. 4.7.1²³ | --                                         | 1 Min.                 | 1 Min.                    | Direkt-verbin-dung | nein                        | Werte²¹        | Prio 2: Vertrag-liche Grund-lage mit AN/ANN | Optional              | 01.10.2023, 00:00 Uhr |
| 9991 00000 119 1  | Messloka-tion, Ist-Ein-speisung, 15 Min.                     | aus dem SMGW      | Messloka-tion | Siehe Kap. 4.7.1²³ | --                                         | 15 Min.                | 15 Min.                   | Direkt-verbin-dung | nein                        | Werte²¹        | Prio 2: Vertrag-liche Grund-lage mit AN/ANN | Optional              | 01.10.2023, 00:00 Uhr |
| 9991 00000 120 8  | Messloka-tion, Ist-Ein-speisung, zur einmaligen Übermittlung | aus dem SMGW      | Messloka-tion | Siehe Kap. 4.7.1²³ | --                                         | ad-hoc                 | ad-hoc                    | Direkt-verbin-dung | nein                        | Werte²¹        | Prio 2: Vertrag-liche Grund-lage mit AN/ANN | Optional              | 01.10.2023, 00:00 Uhr |
| 9991 00000 121 6  | Messloka-tion, Ist-Ein-speisung, Schwellwert                 | aus dem SMGW      | Messloka-tion | Siehe Kap. 4.7.1²³ | Bei Schwell-wertun-ter- / -über-schreitung | 1 Min.                 | 1 Min.                    | Direkt-verbin-dung | nein                        | Werte²¹        | Prio 2: Vertrag-liche Grund-lage mit AN/ANN | Optional              | 01.10.2023, 00:00 Uhr |
| 9991 00000 122 4  | Messloka-tion,                                               | aus dem SMGW      | Messloka-tion | Siehe Kap. 4.7.3²⁴ | --                                         | 1 Min.                 | 1 Min.                    | Direkt-verbin-dung | nein                        | Werte²¹        | Prio 2: Vertrag-liche                       | Optional              | 01.10.2023, 00:00 Uhr |


<sup>27</sup> Konfigurations-Priorität wird berücksichtigt, wenn Kapazitätsgrenzen der Messtechnik erreicht wird inkl. Kommunikation.

Version: 1.3c

11.12.2025

<page_number>Seite 31 von 58</page_number>

Codeliste der Konfigurationen

edi@energy. Datenformate Strom & Gas logo

| Messprodukt-Code¹ | Bezeichnung                                                    | Übertragungs-weg | Ebene         | Werteart           | Auslöser                                   | Erfassungs-intervall | Übermitt-lungsintervall | Frist              | Zuord-nung Zählzeit möglich | Wer-tequalität | Konfigu-rations-Priori-tät²⁷                | Pflicht²⁵ / Optio-nal | Nutzbar ab            |
| ----------------- | -------------------------------------------------------------- | ---------------- | ------------- | ------------------ | ------------------------------------------ | -------------------- | ----------------------- | ------------------ | --------------------------- | -------------- | ------------------------------------------- | --------------------- | --------------------- |
|                   | Mehrwert-dienste, 1 Min.                                       |                  |               |                    |                                            |                      |                         |                    |                             |                | Grund-lage mit AN/ANN                       |                       |                       |
| 9991 00000 123 2  | Messloka-tion, Mehr-wertdienste, 15 Min.                       | aus dem SMGW     | Messloka-tion | Siehe Kap. 4.7.3²⁴ | --                                         | 15 Min.              | 15 Min.                 | Direkt-verbin-dung | nein                        | Werte²¹        | Prio 2: Vertrag-liche Grund-lage mit AN/ANN | Optional              | 01.10.2023, 00:00 Uhr |
| 9991 00000 124 0  | Messloka-tion, Mehr-wertdienste, zur einmali-gen Über-mittlung | aus dem SMGW     | Messloka-tion | Siehe Kap. 4.7.3²⁴ | --                                         | ad-hoc               | ad-hoc                  | Direkt-verbin-dung | nein                        | Werte²¹        | Prio 2: Vertrag-liche Grund-lage mit AN/ANN | Optional              | 01.10.2023, 00:00 Uhr |
| 9991 00000 125 8  | Messloka-tion, Mehr-wertdienste, Schwellwert                   | aus dem SMGW     | Messloka-tion | Siehe Kap. 4.7.3²⁴ | Bei Schwell-wertun-ter- / -über-schreitung | 1 Min.               | 1 Min.                  | Direkt-verbin-dung | nein                        | Werte²¹        | Prio 2: Vertrag-liche Grund-lage mit AN/ANN | Optional              | 01.10.2023, 00:00 Uhr |


# 4.7 Art der Werte für Messprodukte nach Typ 2

Dieses Kapitel enthält die Codelisten Messprodukt-Positions-Codes Strom. Die Messprodukt-Positions-Codes Strom beschreiben die Art der Werte der Messprodukte, welche auf diese Codeliste verweisen.

Version: 1.3c

11.12.2025

Seite 32 von 58
<page_number>32</page_number>

Codeliste der Konfigurationen

edi@energy. Datenformate Strom & Gas logo

Bei einer Anfrage eines Angebotes bzw. einer Bestellung eines Messproduktes (mit Ausnahme von Messprodukten mit Schwellwerten) genügt die Angabe des Messprodukt-Codes. Die zugeordneten Messprodukt-Positions-Codes beschreiben die Art der Werte, welche für das bestellte Messprodukt nach erfolgreicher Konfiguration übermittelt werden.

Bei einer Anfrage eines Angebotes bzw. einer Bestellung eines Messproduktes mit Schwellwerten ist in der Anfrage eines Angebotes bzw. einer Bestellung neben dem Messprodukt-Code mindestens ein Messprodukt-Positions-Code mit dem oberen und unteren Schwellwert anzugeben, bei dessen Über- / Unterschreitung, alle Werte für das bestellte Messprodukt, die dem Messprodukt-Code zugeordnet sind, übermittelt werden.

Version: 1.3c

11.12.2025

Seite <page_number>33</page_number> von 58

Codeliste der Konfigurationen

edi@energy. Datenformate Strom & Gas logo

## 4.7.1 Messprodukt-Position-Codes für die Messprodukte Ist-Einspeisung

In diesem Kapitel sind die Messprodukt-Position-Codes beschrieben, welche für die Messprodukte „Ist-Einspeisung“ Anwendung finden.

| 9991 00000 127 4 | Momentan-Einspeisewirkleistung P ges | Leistung | kW |
| ---------------- | ------------------------------------ | -------- | -- |
| 9991 00000 128 2 | Momentan-Einspeisewirkleistung P 1   | Leistung | kW |
| 9991 00000 129 0 | Momentan-Einspeisewirkleistung P 2   | Leistung | kW |
| 9991 00000 130 7 | Momentan-Einspeisewirkleistung P 3   | Leistung | kW |


Version: 1.3c

11.12.2025

Seite 34 von 58
<page_number>34</page_number>

Codeliste der Konfigurationen

edi@energy. Datenformate Strom & Gas

## 4.7.2 Messprodukt-Position-Codes für die Messprodukte Netzzustandsdaten

In diesem Kapitel sind die Messprodukt-Position-Codes beschrieben, welche für die Messprodukte „Netzzustandsdaten“ Anwendung finden.

| 9991 00000 096 1 | Momentan-Wirkleistung P ges | Leistung     | kW               |
| ---------------- | --------------------------- | ------------ | ---------------- |
| 9991 00000 097 9 | Momentan-Wirkleistung P 1   | Leistung     | kW               |
| 9991 00000 098 7 | Momentan-Wirkleistung P 2   | Leistung     | kW               |
| 9991 00000 099 5 | Momentan-Wirkleistung P 3   | Leistung     | kW               |
| 9991 00000 100 0 | Strommesswert zu L 1        | Ampere       | A                |
| 9991 00000 101 8 | Strommesswert zu L 2        | Ampere       | A                |
| 9991 00000 102 6 | Strommesswert zu L 3        | Ampere       | A                |
| 9991 00000 103 4 | Frequenz                    | Frequenz     | Hz               |
| 9991 00000 104 2 | Phasenwinkel U-L2 zu U-L1   | Phasenwinkel | Faktor (cos phi) |
| 9991 00000 105 0 | Phasenwinkel U-L3 zu U-L1   | Phasenwinkel | Faktor (cos phi) |
| 9991 00000 106 8 | Phasenwinkel I-L1 zu U-L1   | Phasenwinkel | Faktor (cos phi) |
| 9991 00000 107 6 | Phasenwinkel I-L2 zu U-L2   | Phasenwinkel | Faktor (cos phi) |
| 9991 00000 108 4 | Phasenwinkel I-L3 zu U-L3   | Phasenwinkel | Faktor (cos phi) |
| 9991 00000 109 2 | Spannungsmesswert zu L1     | Spannung     | V                |
| 9991 00000 110 9 | Spannungsmesswert zu L2     | Spannung     | V                |
| 9991 00000 126 6 | Spannungsmesswert zu L3     | Spannung     | V                |


Version: 1.3c

11.12.2025

Seite 35 von 58
<page_number>35</page_number>

Codeliste der Konfigurationen

edi@energy. Datenformate Strom & Gas logo

# 4.7.3 Messprodukt-Position-Codes für die Messprodukte Mehrwertdienste

In diesem Kapitel sind die Messprodukt-Position-Codes beschrieben, welche für die Messprodukte „Mehrwertdienste“ Anwendung finden.

| 9991 00000 096 1 | Momentan-Wirkleistung P ges  | Leistung    | kW    |
| ---------------- | ---------------------------- | ----------- | ----- |
| 9991 00000 097 9 | Momentan-Wirkleistung P 1    | Leistung    | kW    |
| 9991 00000 098 7 | Momentan-Wirkleistung P 2    | Leistung    | kW    |
| 9991 00000 099 5 | Momentan-Wirkleistung P 3    | Leistung    | kW    |
| 9991 00000 131 5 | Wirkarbeit in Richtung A+    | Arbeit      | kWh   |
| 9991 00000 132 3 | Wirkarbeit in Richtung A+ L1 | Arbeit      | kWh   |
| 9991 00000 133 1 | Wirkarbeit in Richtung A+ L2 | Arbeit      | kWh   |
| 9991 00000 134 9 | Wirkarbeit in Richtung A+ L3 | Arbeit      | kWh   |
| 9991 00000 135 7 | Wirkarbeit in Richtung A-    | Arbeit      | kWh   |
| 9991 00000 136 5 | Wirkarbeit in Richtung A- L1 | Arbeit      | kWh   |
| 9991 00000 137 3 | Wirkarbeit in Richtung A- L2 | Arbeit      | kWh   |
| 9991 00000 138 1 | Wirkarbeit in Richtung A- L3 | Arbeit      | kWh   |
| 9991 00000 139 9 | Blindarbeit in Richtung R1   | Blindarbeit | kvarh |
| 9991 00000 140 6 | Blindarbeit in Richtung R2   | Blindarbeit | kvarh |
| 9991 00000 141 4 | Blindarbeit in Richtung R3   | Blindarbeit | kvarh |
| 9991 00000 142 2 | Blindarbeit in Richtung R4   | Blindarbeit | kvarh |


Version: 1.3c <page_number>11.12.2025</page_number> Seite 36 von 58

Codeliste der Konfigurationen

edi@energy. Datenformate Strom & Gas logo

# 4.7.4 Messprodukt-Position-Codes für die Messprodukte Netzzustandsdaten Spannung

In diesem Kapitel sind die Messprodukt-Position-Codes beschrieben, welche für das Messprodukt „Netzzustandsdaten Spannung“ Anwendung finden.

| Messprodukt-Position-Code¹ | Bezeichnung             | Größe    | Einheit |
| -------------------------- | ----------------------- | -------- | ------- |
| 9991 00000 109 2           | Spannungsmesswert zu L1 | Spannung | V       |
| 9991 00000 110 9           | Spannungsmesswert zu L2 | Spannung | V       |
| 9991 00000 126 6           | Spannungsmesswert zu L3 | Spannung | V       |


Version: 1.3c

11.12.2025

Seite 37 von 58
<page_number>37</page_number>

Codeliste der Konfigurationen

edi@energy. Datenformate Strom & Gas

# 5 Mindestumfang der Messprodukte in der UTILMD

## 5.1 Mindestumfang der Messprodukte in der UTILMD Strom

Die Tabellen geben einen Überblick über die Angabe der mindestens notwendigen Messprodukte auf Ebene der Messlokation und Marktlokation.

Der NB bestellt über die vorläufige Anmeldebestätigung die notwendige Wertegranularität auf den Lokationen (Marktlokation, Messlokation und Tranche). Der MSB ist verpflichtet diese notwendige Wertegranularität zu bedienen.

Die Tabelle kann nicht angewendet werden, von Beginn der Änderung einer messtechnischen Einordnung bis zu deren Abschluss, da es aufgrund der bilanzierungsrelevanten Fristen zu Verzögerungen bei der Anpassung der OBIS-Kennzahlen kommt.

Version: 1.3c

11.12.2025

Seite 38 von 58
<page_number>38</page_number>

Codeliste der Konfigurationen

edi@energy. Datenformate Strom & Gas logo

# Mindestumfang der Messprodukte in der UTILMD bei iMS Strom

| Sparte<br/>aus SG2 NAD+MR | Prognosegrundlage der Marktlokation<br/>aus SG10 CCI+++ZC0 /ZA6   | Messtechnische Einordnung der Marktlokation<br/>aus SG10 CCI+++Z83 | Netznutzungsabrechnungsvariante<br/>aus SG10 CCI+++Z88 | Lieferrichtung<br/>aus SG10 CCI+++Z30 | Marktlokation<br/>Messprodukt-Code                         | Messlokation(bei rechnerisch ermittelter Energiemenge der Marktlokation)<br/>Messprodukt-Code | Messlokation(bei nicht rechnerisch ermittelter Energiemenge der Marktlokation)<br/>Messprodukt-Code |
| ------------------------- | ----------------------------------------------------------------- | ------------------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------- | ---------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| Strom                     | Prognose auf Basis von Werten<br/>CCI+++ZC0                       | iMS (Z52)                                                          | Arbeitspreis/Leistungspreis (CAV+ZB1:::Z15)            | Verbrauch (Z07)                       | 9991 00000 006 0<br/>9991 00000 007 8<br/>9991 00000 008 6 | 9991 00000 019 3<br/>9991 00000 021 8<br/>ggf.<br/>9991 00000 020 0<br/>9991 00000 022 6      | 9991 00000 019 3                                                                                    |
| Strom                     | Prognose auf Basis von Werten<br/>CCI+++ZC0                       | iMS (Z52)                                                          | Arbeitspreis/Grundpreis (CAV+ZB1:::Z14)                | Verbrauch (Z07)                       | 9991 00000 006 0<br/>9991 00000 007 8<br/>9991 00000 008 6 | 9991 00000 019 3<br/>9991 00000 021 8<br/>ggf.<br/>9991 00000 020 0<br/>9991 00000 022 6      | 9991 00000 019 3                                                                                    |
| Strom                     | Prognose auf Basis von Profilen<br/>CCI+++ZA6<br/>SLP/SEP CAV+E02 | iMS (Z52)                                                          | Arbeitspreis/Grundpreis (CAV+ZB1:::Z14)                | Verbrauch (Z07)                       | 9991 00000 006 0                                           | 9991 00000 019 3<br/>ggf.<br/>9991 00000 020 0                                                | 9991 00000 019 3                                                                                    |
| Strom                     | Prognose auf Basis von Werten<br/>CCI+++ZC0                       | iMS (Z52)                                                          | --                                                     | Erzeugung (Z06)                       | 9991 00000 006 0<br/>9991 00000 007 8                      | 9991 00000 020 0<br/>9991 00000 022 6<br/>ggf.                                                | 9991 00000 020 0                                                                                    |


Version: 1.3c <page_number>11.12.2025</page_number> Seite 39 von 58

Codeliste der Konfigurationen

edi@energy. Datenformate Strom & Gas

| Sparte | Prognosegrundlageder Marktlokation | Messtechni-sche Einord-nung derMarktlokation | Netznutzungsabrech-nungsvariante | Lieferrichtung | Marktlokation | Messlokation(bei rechnerisch ermittel-ter Energiemenge derMarktlokation) | Messlokation(bei nicht rechnerisch ermit-telter Energiemenge derMarktlokation) |
| ------ | ---------------------------------- | -------------------------------------------- | -------------------------------- | -------------- | ------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
|        |                                    |                                              |                                  |                |               | 9991 00000 019 3<br/>9991 00000 021 8                                    |                                                                                |


Version: 1.3c

11.12.2025

Seite 40 von 58
<page_number>40</page_number>

Codeliste der Konfigurationen

edi@energy. Datenformate Strom & Gas logo

# Mindestumfang der Messprodukte in der UTILMD bei kME / mME Strom

| Sparte<br/>aus SG2 NAD+MR | Prognosegrundlage der Marktlokation<br/>aus SG10 CCI+++ZC0 /ZA6                        | Messtechnische Einordnung der Marktlokation<br/>aus SG10 CCI+++Z83 | Netznutzungsabrechnungsvariante<br/>aus SG10 CCI+++Z88 | Lieferrichtung<br/>aus SG10 CCI+++Z30 | Marktlokation<br/>Messprodukt-Code                                                                         | Messlokation(bei rechnerisch ermittelter Energiemenge der Marktlokation)<br/>Messprodukt-Code                                                                                                                                      | Messlokation(bei nicht rechnerisch ermittelter Energiemenge der Marktlokation)<br/>Messprodukt-Code        |
| ------------------------- | -------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Strom                     | Prognose auf Basis von Profilen<br/>CCI+++ZA6<br/><br/>SLP/SEP TLP/TEP<br/>CAV+E02/E14 | kME/mME (Z53)                                                      | Arbeitspreis/Grundpreis (CAV+ZB1:::Z14)                | Verbrauch (Z07)                       | 9991 00000 004 4<br/>oder<br/>9991 00000 049 0<br/>oder<br/>9991 00000 005 2<br/>oder<br/>9991 00000 006 0 | 9991 00000 015 1<br/>oder<br/>9991 00000 051 5<br/>oder<br/>9991 00000 017 7<br/>oder<br/>9991 00000 019 3<br/>ggf.<br/>9991 00000 016 9<br/>oder<br/>9991 00000 052 3<br/>oder<br/>9991 00000 018 8<br/>oder<br/>9991 00000 020 0 | 9991 00000 015 1<br/>oder<br/>9991 00000 051 5<br/>oder<br/>9991 00000 017 7<br/>oder<br/>9991 00000 019 3 |
| Strom                     | Prognose auf Basis von Werten<br/>CCI+++ZC0                                            | kME (Z53)                                                          | Arbeitspreis/Leistungs-preis (CAV+ZB1:::Z15)           | Verbrauch (Z07)                       | 9991 00000 007 8                                                                                           | 9991 00000 021 8<br/>ggf.<br/>9991 00000 022 6                                                                                                                                                                                     | --                                                                                                         |


Version: 1.3c

11.12.2025

Seite 41 von 58
<page_number>41</page_number>

Codeliste der Konfigurationen

edi@energy. Datenformate Strom & Gas logo

| Sparte | Prognosegrundlage der Marktlokation           | Messtechnische Einordnung der Marktlokation | Netznutzungsabrechnungsvariante | Lieferrichtung  | Marktlokation    | Messlokation(bei rechnerisch ermittelter Energiemenge der Marktlokation) | Messlokation(bei nicht rechnerisch ermittelter Energiemenge der Marktlokation) |
| ------ | --------------------------------------------- | ------------------------------------------- | ------------------------------- | --------------- | ---------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| Strom  | Prognose auf Basis von Profilen<br/>CCI+++ZA6 | kME/mME (Z53)                               | --                              | Erzeugung (Z06) | 9991 00000 004 4 | 9991 00000 016 9<br/>ggf.<br/>9991 00000 015 1                           | 9991 00000 016 9                                                               |
| Strom  | Prognose auf Basis von Werten<br/>CCI+++ZC0   | kME (Z53)                                   | --                              | Erzeugung (Z06) | 9991 00000 007 8 | 9991 00000 022 6<br/>ggf.<br/>9991 00000 021 8                           | --                                                                             |


Version: 1.3c

11.12.2025

<page_number>Seite 42 von 58</page_number>

Codeliste der Konfigurationen

edi@energy. Datenformate Strom & Gas

# Mindestumfang der Messprodukte in der UTILMD bei keiner Messung Strom

| Sparte<br/>aus SG2NAD+MR | Prognosegrundlageder Marktlokation<br/>aus SG10 CCI+++ZC0/ZA6 | Messtechni-sche Einord-nung derMarktlokation<br/>aus SG10CCI+++Z83 | Netznutzungsabrech-nungsvariante<br/>aus SG10 CCI+++Z88 | Lieferrichtung<br/>aus SG10 CCI+++Z30 | Marktlokation<br/>Messprodukt-Code | Messlokation(bei rechnerisch ermittel-ter Energiemenge derMarktlokation)<br/>Messprodukt-Code | Messlokation(bei nicht rechnerisch ermit-telter Energiemenge derMarktlokation)<br/>Messprodukt-Code |
| ------------------------ | ------------------------------------------------------------- | ------------------------------------------------------------------ | ------------------------------------------------------- | ------------------------------------- | ---------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| Strom                    | Prognose auf Basis<br/>von Werten<br/>CCI+++ZC0               | Keine Mes-<br/>sung (Z68)                                          | Arbeitspreis/Leistungs-<br/>preis (CAV+ZB1:::Z15)       | Verbrauch (Z07)                       | --                                 | --                                                                                            | --                                                                                                  |
| Strom                    | Prognose auf Basis<br/>von Profilen<br/>CCI+++ZA6             | Keine Mes-<br/>sung (Z68)                                          | Arbeitspreis/Grundpreis<br/>(CAV+ZB1:::Z14)             | Verbrauch (Z07)                       | --                                 | --                                                                                            | --                                                                                                  |


## 5.2 Mindestumfang der Messprodukte in der UTILMD Gas

Die Tabelle gibt einen Überblick über die Angabe der mindestens notwendigen Messprodukte auf Ebene der Messlokation und Marktlokation.

Der NB bestellt über die vorläufige Anmeldebestätigung die notwendige Wertegranularität auf den Lokationen (Marktlokation, Messlokation). Der MSB ist verpflichtet diese notwendige Wertegranularität zu bedienen.

Version: 1.3c

11.12.2025

Seite 43 von 58
<page_number>

43
</page_number>

Codeliste der Konfigurationen

edi@energy. Datenformate Strom & Gas logo

# Mindestumfang der Messprodukte in der UTILMD bei Gas

| Sparte<br/>aus SG2 NAD+MR | Prognosegrundlage der Marktlokation<br/>aus SG10 CCI+++ZC0 /ZA6 | Messtechnische Einordnung der Marktlokation<br/>aus SG10 CCI+++Z83 | Netznutzungsabrechnungsvariante<br/>aus SG10 CCI+++Z88 | Lieferrichtung<br/>aus SG10 CCI+++Z30 | Marktlokation<br/>Messprodukt-Code                                                                                              | Messlokation(bei rechnerisch ermittelter Energiemenge der Marktlokation)<br/>Messprodukt-Code                                                                                                                                  | Messlokation(bei nicht rechnerisch ermittelter Energiemenge der Marktlokation)<br/>Messprodukt-Code                                                                                                                            |
| ------------------------- | --------------------------------------------------------------- | ------------------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Gas                       | Prognose auf Basis von Profilen<br/>CCI+++ZA6<br/>CAV+E02       | --                                                                 | --                                                     | --                                    | Mindestens eine der folgend genannten:<br/><br/>9991 00000 040 8<br/>9991 00000 062 2<br/>9991 00000 063 0<br/>9991 00000 061 4 | Mindestens eine der folgend genannten Tupel:<br/><br/>9991 00000 038 3<br/>oder<br/>9991 00000 039 1<br/><br/><br/>9991 00000 057 3<br/>oder<br/>9991 00000 058 1<br/><br/><br/>9991 00000 059 9<br/>oder<br/>9991 00000 060 6 | Mindestens eine der folgend genannten Tupel:<br/><br/>9991 00000 038 3<br/>oder<br/>9991 00000 039 1<br/><br/><br/>9991 00000 057 3<br/>oder<br/>9991 00000 058 1<br/><br/><br/>9991 00000 059 9<br/>oder<br/>9991 00000 060 6 |


Version: 1.3c

11.12.2025

Seite 44 von 58
<page_number>44</page_number>

Codeliste der Konfigurationen

edi@energy. Datenformate Strom & Gas logo

| Sparte | Prognosegrundlageder Marktlokation              | Messtechni-sche Einord-nung derMarktlokation | Netznutzungsabrech-nungsvariante | Lieferrichtung | Marktlokation    | Messlokation(bei rechnerisch ermittel-ter Energiemenge derMarktlokation) | Messlokation(bei nicht rechnerisch ermit-telter Energiemenge derMarktlokation) |
| ------ | ----------------------------------------------- | -------------------------------------------- | -------------------------------- | -------------- | ---------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
|        |                                                 |                                              |                                  |                |                  | 9991 00000 055 7<br/>oder<br/>9991 00000 056 5                           | 9991 00000 055 7<br/>oder<br/>9991 00000 056 5                                 |
| Gas    | Prognose auf Basis<br/>von Werten<br/>CCI+++ZC0 | --                                           | --                               | --             | 9991 00000 035 9 | 9991 00000 035 9                                                         | 9991 00000 035 9                                                               |


Version: 1.3c

11.12.2025

Seite 45 von 58
<page_number>45</page_number>

Codeliste der Konfigurationen

edi@energy. Datenformate Strom & Gas logo

# 6 Produkte zur Bestellung / Änderung von Daten

Dieses Kapitel enthält die Codelisten der Produkte von Daten, welche im Rahmen der Zuordnung des LFN (UTILMD) zu einer Marktlokation bzw. Tranche angegeben oder im Rahmen der Bestellung einer Änderung von Abrechnungsdaten (ORDERS) bestellt werden können.

## 6.1 Produkte zur Anmeldung einer Zuordnung des LFN (UTILMD)

Die nachfolgenden Tabellen gelten in der UTILMD je Produktpaket-ID.

### 6.1.1 Verpflichtende Produkte zur Anmeldung einer Zuordnung des LFN (UTILMD)

Die nachfolgende Tabelle enthält die Produkte die je Produktpaket-ID verpflichtend anzugeben sind.

| Produkt-Code¹<br/>PIA+5 DE7140Produkt-Code | Bezeichnung   | Code der Produkteigenschaft(Wertebereich)<br/>CAV+ZH9, DE7110                                                                             | Wertedetails fürPosition<br/>CAV+ZV4, DE7110                                                                                                                                                                                                                                                | Bestellbar überAnwendungsfälle(Prüfidentifikator) | Maximale Wie-derholbarkeit desProdukt-Code jeProduktpaket-ID | Erläuterung                                                                                                                                                                                                                                                                                                                                                  |
| ------------------------------------------ | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 9991 00000<br/>208 2                       | Bilanzkreis   | --                                                                                                                                        | Angabe Bilanzkreis: Muss: max. Wdh1 je Produkt-Code X \[970]                                                                                                                                                                                                                                | 55001, 55077,<br/>55600, 55601,<br/>55014, 55608  | 1                                                            | Dieses Produkt ist je Produktpaket-ID in der UTILMD zwingend anzugeben.<br/><br/>\[970] Format: an..17                                                                                                                                                                                                                                                       |
| 9991 00000<br/>209 0                       | Tranchengröße | 9991 00000 301 4 prozentuale Aufteilung<br/><br/>9991 00000 302 2 Aufteilungsfaktor auf Basis von Referenzenträger/installierter Leistung | Angabe Produkt-Code: Muss wenn STS+7++xxx+ZW2 (Transaktionsgrundergänzung: Geschäftsvorfall 3) vorhanden. Angabe Wertedetails für Position: Muss wenn Code der Produkteigenschaft 9991 00000 301 4 (prozentuale Aufteilung) vorhanden. Je Produkt-Code max. Wdh1 X \[914] ∧ \[930] ∧ \[955] | 55077, 55601                                      | 1                                                            | Im Geschäftsvorfall 3 der Anmeldung einer Zuordnung des LFN STS+7++xxx+ZW2 (Transaktionsgrundergänzung: Geschäftsvorfall 3) ist zwingend dieses Produkt anzugeben, zudem wenn der Code der Produkteigenschaft 9991 00000 301 4 (prozentuale Aufteilung) vorhanden ist müssen die Wertedetails (prozentuale Tranchengröße) für die Position angegeben werden. |


Version: 1.3c

11.12.2025

Seite 46 von 58
<page_number>46</page_number>

Codeliste der Konfigurationen

edi@energy. Datenformate Strom & Gas logo

| Produkt-Code¹<br/>PIA+5 DE7140Produkt-Code | Bezeichnung                                                    | Code der Produkteigenschaft(Wertebereich)<br/>CAV+ZH9, DE7110                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Wertedetails fürPosition<br/>CAV+ZV4, DE7110 | Bestellbar überAnwendungsfälle(Prüfidentifikator) | Maximale Wie-derholbarkeit desProdukt-Code jeProduktpaket-ID | Erläuterung                                                                                                                |
| ------------------------------------------ | -------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- | ------------------------------------------------- | ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------- |
|                                            |                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |                                              |                                                   |                                                              | \[914] Format: Möglicher Wert: > 0<br/>\[930] Format: max. 2<br/>Nachkommastellen<br/>\[955] Format: Möglicher Wert: < 100 |
| 9991 00000<br/>240 4                       | Veräußerungs-<br/>form der er-<br/>zeugenden<br/>Marktlokation | 9991 00000 241 2 Ausfallvergütung (Hinweis:<br/>Verwendung, wenn Rolle LF einem Unternehmen<br/>NB zugeordnet ist)<br/><br/>9991 00000 242 0 Marktprämie (Hinweis: Ver-<br/>wendung, nur wenn die Rolle LF nicht einem Un-<br/>ternehmen NB)<br/><br/>9991 00000 243 8 KWKG-Vergütung (Hinweis:<br/>Verwendung, wenn Rolle LF einem Unternehmen<br/>NB zugeordnet ist)<br/><br/>9991 00000 244 6 Sonstige Direktvermarktung<br/><br/>ohne gesetzliche Vergütung (Hinweis: Verwen-<br/>dung, nur wenn die Rolle LF nicht einem Unter-<br/>nehmen NB) | --                                           | 55077, 55601                                      | 1                                                            | Durch eine Anmeldung veränderbare<br/>Situation, die der LF als Erwartung in<br/>der Anmeldung äußern kann.                |


Version: 1.3c <page_number>11.12.2025</page_number> Seite 47 von 58

Codeliste der Konfigurationen

edi@energy. Datenformate Strom & Gas logo

# 6.1.2 Optionale Produkte als Voraussetzung in der Anmeldung einer Zuordnung des LFN (UTILMD)

Die nachfolgende Tabelle enthält die optionalen Produkte die je Produktpaket-ID durch den LFN als Voraussetzung für eine Zuordnung des LFN angegeben werden können.

| Produkt-Code¹<br/>PIA+5 DE7140Produkt-Code | Bezeichnung<br/>CAV+ZH9, DE7110             | Code der Produkteigenschaft (Wertebereich)<br/>CAV+ZH9, DE7110                                                                                                                                                                                       | Wertedetails für Position<br/>CAV+ZV4, DE7110 | Bestellbar über Anwendungsfälle (Prüfidentifikator) | Maximale Wiederholbarkeit des Produkt-Code je Produktpaket-ID | Erläuterung                                                                                                                                                                                                                                                                                      |
| ------------------------------------------ | ------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- | --------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 9991 00000 200 8                           | Messtechnische Einordnung der Marktlokation | 9991 00000 210 7 iMS<br/>9991 00000 211 5 kME/mME<br/>9991 00000 212 3 keine Messung                                                                                                                                                                 | --                                            | 55001, 55077, 55600, 55601                          | 1                                                             | Nicht durch die Anmeldung veränderbare Situation, die der LF für die Belieferung der Marktlokation erwartet.                                                                                                                                                                                     |
| 9991 00000 272 7                           | Verbrauchsart                               | 9991 00000 278 5 Kraft / Licht<br/>9991 00000 279 3 Wärme /Kälte<br/>9991 00000 280 0 E-Mobilität<br/>9991 00000 281 8 Straßenbeleuchtung                                                                                                            | --                                            | 55001, 55600                                        | 5                                                             | Nicht durch die Anmeldung veränderbare Situation, die der LF für die Belieferung der Marktlokation erwartet. Die der Marktlokation zugeordneten Technischen Ressourcen müssen die genannten Eigenschaften haben unabhängig davon, ob für diese Technischen Ressourcen eine TR-ID vergeben wurde. |
| 9991 00000 273 5                           | Wärmenutzung                                | 9991 00000 283 4 Speicherheizung<br/>9991 00000 284 2 Wärmepumpe unspezifiziert<br/>9991 00000 285 0 Direktheizung<br/>9991 00000 286 8 Wärmepumpe (Wärme und Kälte)<br/>9991 00000 287 6 Wärmepumpe (Kälte)<br/>9991 00000 288 4 Wärmepumpe (Wärme) | --                                            | 55001, 55600                                        | 1                                                             | Nicht durch die Anmeldung veränderbare Situation, die der LF für die Belieferung der Marktlokation erwartet. Die der Marktlokation zugeordneten Technischen Ressourcen müssen die genannten Eigenschaften haben unabhängig davon, ob für diese Technischen Ressourcen eine TR-ID vergeben wurde. |


Version: 1.3c

11.12.2025

Seite 48 von 58
<page_number>48</page_number>

Codeliste der Konfigurationen

edi@energy. Datenformate Strom & Gas logo

| Produkt-Code¹<br/>PIA+5 DE7140 Produkt-Code | Bezeichnung                   | Code der Produkteigenschaft (Wertebereich)<br/>CAV+ZH9, DE7110                                                                | Wertedetails für Position<br/>CAV+ZV4, DE7110 | Bestellbar über Anwendungsfälle (Prüfidentifikator) | Maximale Wiederholbarkeit des Produkt-Code je Produktpaket-ID | Erläuterung                                                                                                                                                                                                                                                                                      |
| ------------------------------------------- | ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- | --------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 9991 00000 274 3                            | Art der E-Mobilität           | 9991 00000 289 2 Wallbox<br/>9991 00000 290 9 E-Mobilitätsladesäule<br/>9991 00000 291 7 Ladepark                             | --                                            | 55001, 55600                                        | 1                                                             | Nicht durch die Anmeldung veränderbare Situation, die der LF für die Belieferung der Marktlokation erwartet. Die der Marktlokation zugeordneten Technischen Ressourcen müssen die genannten Eigenschaften haben unabhängig davon, ob für diese Technischen Ressourcen eine TR-ID vergeben wurde. |
| 9991 00000 275 1                            | Steuerbare Ressource          | 9991 00000 292 5 Steuerbare Ressource vorhanden                                                                               | --                                            | 55001, 55600                                        | 1                                                             | Nicht durch die Anmeldung veränderbare Situation, die der LF für die Belieferung der Marktlokation erwartet. Die der Marktlokation zugeordneten Technischen Ressourcen muss eine Steuerbare Ressource zugeordnet sein.                                                                           |
| 9991 00000 277 7                            | Eigenschaft der Marktlokation | 9991 00000 294 1 Marktlokation stellt eine Kundenanlage dar<br/>9991 00000 302 0: Marktlokation stellt keine Kundenanlage dar | --                                            | 55001, 55600                                        | 1                                                             | Nicht durch die Anmeldung veränderbare Situation, die der LF für die Belieferung der Marktlokation erwartet.                                                                                                                                                                                     |


## 6.1.3 Optionale Produkte als Erwartung / Änderungswunsch in der Anmeldung einer Zuordnung des LFN (UTILMD)

Die nachfolgende Tabelle enthält die optionalen Produkte die je Produktpaket-ID durch den LFN als Erwartung / Änderungswunsch einer Zuordnung des LFN angegeben werden können.

Hinweis: Die vom LFN in der Anmeldung angegebene Erwartung / Änderungswunsch kann nur umgesetzt werden, wenn die vorhandene Technik dies ermöglicht. Es handelt sich hierbei nicht um den Auftrag zur Änderung der Technik.

Version: 1.3c <page_number>Seite 49 von 58</page_number> 11.12.2025

Codeliste der Konfigurationen

edi@energy. Datenformate Strom & Gas logo

| Produkt-Code¹<br/>PIA+5 DE7140 Produkt-Code | Bezeichnung                                      | Code der Produkteigenschaft (Wertebereich)<br/>CAV+ZH9, DE7110                                                                                                                                                                                                           | Wertedetails für Position<br/>CAV+ZV4, DE7110 | Bestellbar über Anwendungsfälle (Prüfidentifikator) | Maximale Wiederholbarkeit des Produkt-Code je Produktpaket-ID | Erläuterung                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------- | ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------- | --------------------------------------------------- | ------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 9991 00000 201 6                            | Netzentgelte aufgrund netzorientierter Steuerung | 9991 00000 213 1 pauschale Netzentgeltreduzierung (Modul 1)<br/>9991 00000 214 9 prozentuale Reduzierung Arbeitspreis (Modul 2)<br/>9991 00000 215 7 Anreizmodul zeitvariables Netzentgelt (Modul 1 und Modul 3)                                                         | --                                            | 55001, 55600                                        | 1                                                             | Durch eine Anmeldung veränderbare Situation, die der LF als Erwartung in der Anmeldung äußern kann.<br/><br/>Hinweis: Eine Überführung einer Bestands 14a-Anlage (Inbetriebnahme vor dem 01.01.2024) in ein neues 14a-Modul (gemäß BK6-22-300/BK8-22/010-A), kann nicht über die Bestellung mittels dieser Produkte erfolgen. |
| 9991 00000 202 4                            | Netzentgelte Preissystem                         | 9991 00000 216 5 Netzentgelte nach Jahresleistungspreissystem<br/>9991 00000 217 3 Netzentgelte nach Monatsleistungspreissystem<br/>9991 00000 218 1 Netzentgelte nach Grundpreis- / Arbeitspreissystem<br/>9991 00000 219 9 Netzentgelte nach Tagesleistungspreissystem | --                                            | 55001, 55600                                        | 1                                                             | Durch eine Anmeldung veränderbare Situation, die der LF als Erwartung in der Anmeldung äußern kann.                                                                                                                                                                                                                           |
| 9991 00000 203 2                            | Konzessionsabgabe                                | 9991 00000 295 9 Tarifkunden-KA<br/>9991 00000 296 7 Sondervertragskunden-KA, gemäß KAV § 2 Abs 3<br/>9991 00000 220 6 Schwachlastkonzessionsabgabe für Energie im Schwachlastzeitraum<br/>9991 00000 297 5 KA-Befreiung                                                 | --                                            | 55001, 55600                                        | 1                                                             | Durch eine Anmeldung veränderbare Situation, die der LF als Erwartung in der Anmeldung äußern kann.                                                                                                                                                                                                                           |
| 9991 00000 204 0                            | Netznutzung / Netznutzungsvertrag                | 9991 00000 222 2 Direkter Vertrag zwischen Kunden und NB                                                                                                                                                                                                                 | --                                            | 55001, 55600                                        | 1                                                             | Durch eine Anmeldung veränderbare Situation, die der LF als Erwartung in der Anmeldung äußern kann.                                                                                                                                                                                                                           |


Version: 1.3c

11.12.2025

Seite 50 von 58
<page_number>50</page_number>

Codeliste der Konfigurationen

edi@energy. Datenformate Strom & Gas logo

| Produkt-Code¹<br/>PIA+5 DE7140 Produkt-Code | Bezeichnung                             | Code der Produkteigenschaft (Wertebereich)<br/>CAV+ZH9, DE7110                                      | Wertedetails für Position<br/>CAV+ZV4, DE7110      | Bestellbar über Anwendungsfälle (Prüfidentifikator) | Maximale Wiederholbarkeit des Produkt-Code je Produktpaket-ID | Erläuterung                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------------------------- | --------------------------------------- | --------------------------------------------------------------------------------------------------- | -------------------------------------------------- | --------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|                                             |                                         | 9991 00000 223 0 Vertrag zwischen Lieferanten und NB                                                |                                                    |                                                     |                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 9991 00000 205 8                            | Netznutzung / Zahler der Netznutzung    | 9991 00000 224 8 Kunde<br/>9991 00000 225 6 Lieferant                                               | --                                                 | 55001, 55600                                        | 1                                                             | Durch eine Anmeldung veränderbare Situation, die der LF als Erwartung in der Anmeldung äußern kann.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 9991 00000 206 6                            | Empfänger der Vergütung zur Einspeisung | 9991 00000 226 4 Kunde<br/>9991 00000 227 2 Lieferant                                               | --                                                 | 55077, 55601                                        | 1                                                             | Durch eine Anmeldung veränderbare Situation, die der LF als Erwartung in der Anmeldung äußern kann.<br/><br/>Angabe: Muss, wenn Produkt „9991 00000 240 4“ Veräußerungsform der erzeugenden Marktlokation mit Position „9991 00000 242 0“ Marktprämie im Produktpaket enthalten ist.<br/><br/>Bei Auswahl des Codes der Produkteigenschaft "Lieferant“ kann vom NB eine Abtretungserklärung des Kunden erwartet werden. Hierzu kann im Anwendungsfall, in dem dieses Produkt ausgewählt wurde, ein „Link zur Abtretungserklärung / Vollmacht vom Kunden“ (zum Download durch den NB) angegeben werden. |
| 9991 00000 207 4                            | Prognosegrundlage                       | 9991 00000 228 0 Prognose auf Basis von Profilen<br/>9991 00000 229 8 Prognose auf Basis von Werten | --                                                 | 55001, 55077, 55600, 55601                          | 1                                                             | Durch eine Anmeldung veränderbare Situation, die der LF als Erwartung in der Anmeldung äußern kann.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 9991 00000 239 7                            | Jahresverbrauchsprognose                | --                                                                                                  | Angabe Jahresverbrauchsprognose: X \[909] ∧ \[937] | 55001, 55077, 55600, 55601                          | 1                                                             | Durch eine Anmeldung veränderbare Situation, die der LF als Erwartung in der Anmeldung äußern kann.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |


Version: 1.3c

11.12.2025

Seite 51 von 58
<page_number>51</page_number>

Codeliste der Konfigurationen

edi@energy. Datenformate Strom & Gas logo

| Produkt-Code¹<br/>PIA+5 DE7140<br/>Produkt-Code | Bezeichnung           | Code der Produkteigenschaft (Wertebereich)<br/>CAV+ZH9, DE7110                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Wertedetails für Position<br/>CAV+ZV4, DE7110 | Bestellbar über Anwendungsfälle (Prüfidentifikator) | Maximale Wiederholbarkeit des Produkt-Code je Produktpaket-ID | Erläuterung                                                                                         |
| ----------------------------------------------- | --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- | --------------------------------------------------- | ------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
|                                                 |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                               |                                                     |                                                               | \[909] Format: Mögliche Werte: 0 bis n<br/>\[937] Format: keine Nachkommastelle                     |
| 9991 00000 276 9                                | Ruhende Marktlokation | 9991 00000 293 3 Marktlokation soll als ruhende Marktlokation zu einer Marktlokation „Kundenanlage“ nach §20 Abs. 1d EnWG (welche in diesem Fall neu auszuprägen ist), hinzugefügt werden (Bildung).<br/><br/>9991 00000 321 2 Marktlokation soll als ruhende Marktlokation zu einer Marktlokation „Kundenanlage“ nach §10c EEG (welche in diesem Fall neu auszuprägen ist), hinzugefügt werden (Bildung).<br/><br/>9991 00000 320 4 Marktlokation soll als ruhende Marktlokation zu einer bestehenden Marktlokation „Kundenanlage“ (welche in diesem Fall bereits existiert), hinzufügt werden (Integration). | --                                            | 55001                                               | 1                                                             | Durch eine Anmeldung veränderbare Situation, die der LF als Erwartung in der Anmeldung äußern kann. |


## 6.2 Produkte zur Bestellung einer Änderung von Abrechnungsdaten (ORDERS)

| Produkt-Code¹<br/>PIA+5 DE7140<br/>Produkt-Code | Bezeichnung                                      | Code der Produkteigenschaft (Wertebereich)<br/>CAV+ZH9, DE7110                                                                  | Wertedetails für Position<br/>CAV+ZV4, DE7110 | Bestellbar über Anwendungsfälle (Prüfidentifikator) | Erläuterung                                                                                                                           |
| ----------------------------------------------- | ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- | --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| 9991 00000 249 6                                | Netzentgelte aufgrund netzorientierter Steuerung | 9991 00000 257 9 pauschale Netzentgeltreduzierung (Modul 1)<br/>9991 00000 258 7 prozentuale Reduzierung Arbeitspreis (Modul 2) | --                                            | 17133                                               | Hinweis: Eine Überführung einer Bestands 14a-Anlage (Inbetriebnahme vor dem 01.01.2024) in ein neues 14a-Modul (gemäß BK6-22-300/BK8- |


Version: 1.3c

11.12.2025

<page_number>Seite 52 von 58</page_number>

Codeliste der Konfigurationen

edi@energy. Datenformate Strom & Gas logo

| Produkt-Code¹<br/>PIA+5 DE7140 Produkt-Code | Bezeichnung                             | Code der Produkteigenschaft (Wertebereich)<br/>CAV+ZH9, DE7110                   | Wertedetails für Position<br/>CAV+ZV4, DE7110 | Bestellbar über Anwendungsfälle<br/>(Prüfidentifikator) | Erläuterung                                                                                                                                                                                                                                              |
| ------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------- | --------------------------------------------- | ------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                             |                                         | 9991 00000 259 5 Anreizmodul zeitvariables Netzentgelt (Modul 1 und Modul 3)     |                                               |                                                         | 22/010-A), kann nicht über die Bestellung mittels dieser Produkte erfolgen.                                                                                                                                                                              |
| 9991 00000 250 3                            | Netzentgelte Preissystem                | 9991 00000 260 2 Netzentgelte nach Jahresleistungspreissystem                    | --                                            | 17133                                                   | --                                                                                                                                                                                                                                                       |
|                                             |                                         | 9991 00000 261 0 Netzentgelte nach Monatsleistungspreissystem                    |                                               |                                                         |                                                                                                                                                                                                                                                          |
|                                             |                                         | 9991 00000 262 8 Netzentgelte nach Grundpreis- / Arbeitspreissystem              |                                               |                                                         |                                                                                                                                                                                                                                                          |
|                                             |                                         | 9991 00000 263 6 Netzentgelte nach Tagesleistungspreissystem                     |                                               |                                                         |                                                                                                                                                                                                                                                          |
| 9991 00000 251 1                            | Konzessionsabgabe                       | 9991 00000 298 3 Tarifkunden-KA                                                  | --                                            | 17133                                                   | --                                                                                                                                                                                                                                                       |
|                                             |                                         | 9991 00000 299 1 Sondervertragskunden-KA, gemäß KAV § 2 Abs 3                    |                                               |                                                         |                                                                                                                                                                                                                                                          |
|                                             |                                         | 9991 00000 264 4 Schwachlastkonzessionsabgabe für Energie im Schwachlastzeitraum |                                               |                                                         |                                                                                                                                                                                                                                                          |
|                                             |                                         | 9991 00000 300 6 KA-Befreiung                                                    |                                               |                                                         |                                                                                                                                                                                                                                                          |
| 9991 00000 252 9                            | Netznutzung / Netznutzungsvertrag       | 9991 00000 266 0 Direkter Vertrag zwischen Kunden und NB                         | --                                            | 17133                                                   | --                                                                                                                                                                                                                                                       |
|                                             |                                         | 9991 00000 267 8 Vertrag zwischen Lieferanten und NB                             |                                               |                                                         |                                                                                                                                                                                                                                                          |
| 9991 00000 253 7                            | Netznutzung / Zahler der Netznutzung    | 9991 00000 268 6 Kunde                                                           | --                                            | 17133                                                   | --                                                                                                                                                                                                                                                       |
|                                             |                                         | 9991 00000 269 4 Lieferant                                                       |                                               |                                                         |                                                                                                                                                                                                                                                          |
| 9991 00000 254 5                            | Empfänger der Vergütung zur Einspeisung | 9991 00000 270 1 Kunde                                                           | --                                            | 17133                                                   | Bei Auswahl des Codes der Produkteigenschaft "Lieferant“ kann vom NB eine Abtretungserklärung des Kunden erwartet werden. Hierzu ist bei der Bestellung der Änderung dieses Produkts im Anwendungsfall ein „Link zur Abtretungserklärung / Vollmacht vom |
|                                             |                                         | 9991 00000 271 9 Lieferant                                                       |                                               |                                                         |                                                                                                                                                                                                                                                          |


Version: 1.3c

11.12.2025

Seite 53 von 58

Codeliste der Konfigurationen

edi@energy. Datenformate Strom & Gas logo

| Produkt-Code¹<br/>PIA+5 DE7140 Produkt-Code | Bezeichnung                                    | Code der Produkteigenschaft (Wertebereich)<br/>CAV+ZH9, DE7110                                                                                                                                                                                                                                                                                                                                                                                                                                     | Wertedetails für Position<br/>CAV+ZV4, DE7110                | Bestellbar über Anwendungsfälle (Prüfidentifikator) | Erläuterung                                                                     |
| ------------------------------------------- | ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ | --------------------------------------------------- | ------------------------------------------------------------------------------- |
|                                             |                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                                                              |                                                     | Kunden“ (zum Download durch den NB) angegeben werden.                           |
| 9991 00000 255 3                            | Bilanzkreis                                    | --                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Angabe Bilanzkreis: Muss: max. Wdh1 je Produkt-Code X \[970] | 17133                                               | \[970] Format: an..17                                                           |
| 9991 00000 256 1                            | Jahresverbrauchsprognose                       | --                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Angabe Jahresverbrauchsprognose: X \[909] ∧ \[937]           | 17133                                               | \[909] Format: Mögliche Werte: 0 bis n<br/>\[937] Format: keine Nachkommastelle |
| 9991 00000 315 5                            | Veräußerungsform der erzeugenden Marktlokation | 9991 00000 316 3 Ausfallvergütung (Hinweis: Verwendung, wenn Rolle LF einem Unternehmen NB zugeordnet ist)<br/><br/>9991 00000 317 1 Marktprämie (Hinweis: Verwendung, nur wenn die Rolle LF nicht einem Unternehmen NB)<br/><br/>9991 00000 318 9 KWKG-Vergütung (Hinweis: Verwendung, wenn Rolle LF einem Unternehmen NB zugeordnet ist)<br/><br/>9991 00000 319 7 Sonstige Direktvermarktung ohne gesetzliche Vergütung (Hinweis: Verwendung, nur wenn die Rolle LF nicht einem Unternehmen NB) | --                                                           | 17133                                               | --                                                                              |


Hinweis: Prognosegrundlage: Die Bestellung einer Änderung der Prognosegrundlage erfolgt im Rahmen der Bestellung einer Konfiguration vom LF an NB mit dem Anwendungsfall dem der Prüfidentifikator 17120 zugeordnet ist.

Version: 1.3c

11.12.2025

Seite 54 von 58
<page_number>54</page_number>

Codeliste der Konfigurationen

edi@energy logo

# 7 Produkte zur Bestellung einer Änderung an einer Lokation

Die in diesem Kapitel genannten Produkte werden in den Anwendungsfällen zur „Bestellung Änderung Technik“ verwendet.

## 7.1 Produkte zur Bestellung einer Änderung an einer Lokation in der Sparte Strom

Dieses Kapitel enthält die Codelisten der Produkte für die Änderung an einer Lokation in der Sparte Strom.

| Produkt-Code¹         | Bezeichnung                                                                        | Ebene                | Produkt gegenüber MSB von Marktrolle bestellbar<br/>NB | Produkt gegenüber MSB von Marktrolle bestellbar<br/>LF |
| --------------------- | ---------------------------------------------------------------------------------- | -------------------- | ------------------------------------------------------ | ------------------------------------------------------ |
| 9991 00000 230 528 29 | Einbau iMS                                                                         | Messlokation         | X                                                      | X                                                      |
| 9991 00000 231 3³⁰    | Einbau kME / rLM                                                                   | Messlokation         | X                                                      | X                                                      |
| 9991 00000 232 1      | Einbau Wandler                                                                     | Messlokation         | X                                                      | --                                                     |
| 9991 00000 233 9      | weitere Energieflussrichtung                                                       | Messlokation         | X                                                      | --                                                     |
| 9991 00000 234 7      | Vergleichsmessung                                                                  | Messlokation         | X                                                      | --                                                     |
| 9991 00000 235 5      | Änderung der Messebene                                                             | Messlokation         | X                                                      | --                                                     |
| 9991 00000 236 3      | Einbau einer Steuerbox                                                             | Steuerbare Ressource | X                                                      | --                                                     |
| 9991 00000 237 1      | Anschluss weiterer Technischer Ressource an die Steuerbare Ressource der Steuerbox | Steuerbare Ressource | X                                                      | --                                                     |
| 9991 00000 238 9      | Einbau einer Steuerbox                                                             | Netzlokation         | X                                                      | --                                                     |


<sup>28</sup> Wenn das Produkt mit dem Code 9991 00000 230 5 durch den NB bestellt wird, können zusätzlich noch die Produkte mit dem Code 9991 00000 232 1 und/oder 9991 00000 233 9 und/oder 9991 00000 234 7 bestellt werden.

<sup>29</sup> Wenn das Produkt mit dem Code 9991 00000 230 5 durch den NB bestellt wird, kann zusätzlich noch das Produkt mit dem Code 9991 00000 231 3 angegeben werden. Dies dient dazu dem MSB mitzuteilen, dass sofern der Einbau iMS nicht möglich ist, stattdessen eine kME / rLM Messung eingebaut werden soll.

<sup>30</sup> Wenn das Produkt mit dem Code 9991 00000 231 3 durch den NB bestellt wird, können zusätzlich noch die Produkte mit dem Code 9991 00000 232 1 und/oder 9991 00000 233 9 und/oder 9991 00000 234 7 bestellt werden.

Version: 1.3c 11.12.2025 <page_number>Seite 55 von 58</page_number>

Codeliste der Konfigurationen

edi@energy. Datenformate Strom & Gas logo

# 7.2 Produkte zur Bestellung einer Änderung an einer Lokation in der Sparte Gas

Dieses Kapitel enthält die Codelisten der Produkte für die Änderung an einer Lokation in der Sparte Gas.

| Produkt-Code¹    | Bezeichnung                                 | Ebene        | Produkt gegenüber MSB von Marktrolle bestellbar<br/>NB | Produkt gegenüber MSB von Marktrolle bestellbar<br/>LF |
| ---------------- | ------------------------------------------- | ------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| 9991 00000 245 4 | Einbau kME / rLM                            | Messlokation | X                                                      | X                                                      |
| 9991 00000 246 2 | Einbau kME / SLP                            | Messlokation | X                                                      | --                                                     |
| 9991 00000 247 0 | Einbau Mengenumwerter/Mengenregistriergerät | Messlokation | X                                                      | --                                                     |
| 9991 00000 248 8 | Änderung der Messdruckebene                 | Messlokation | X                                                      | --                                                     |


Version: 1.3c

11.12.2025

Seite 56 von 58
<page_number>56</page_number>

Codeliste der Konfigurationen

edi@energy. Datenformate Strom & Gas logo

# 8 Änderungshistorie

| Änd-ID | Ort                                                                                                                                                                                                            | Änderungen<br/>Bisher                                                                                                                                                                                                                                                                                                                                                             | Änderungen<br/>Neu                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Grund der Anpassung                                                                                                                                                                                                                                                                                                                                                                                                | Status              |
| ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------- |
| 26662  | Kapitel 6.1.2 Optionale Produkte als Voraussetzung in der Anmeldung einer Zuordnung des LFN (UTILMD), Tabelle, Zeile: 9991 00000 272 7, Verbrauchsart                                                          | \[...]<br/>9991 00000 282 6 Steuerung / Wärmeabgabe                                                                                                                                                                                                                                                                                                                               | \[...]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Die Verbrauchsart Steuerung / Wärmeabgabe ist keine Verbrauchsart einer Technischen Ressource, sondern eine "Altlast" aus der Verbrauchsart des Zählwerks. Daher kann die Verbrauchsart entfallen, da diese durch einen LF weder sinnvoll angegeben noch durch einen NB sinnvoll als Voraussetzung geprüft werden kann.                                                                                            | Fehler (17.04.2025) |
| 26947  | Kapitel 6.1.3 Optionale Produkte als Erwartung / Änderungswunsch in der Anmeldung einer Zuordnung des LFN (UTILMD), Tabelle, Produktcode: 9991 00000 276 9, Ruhende Marktlokation, Code der Produkteigenschaft | 9991 00000 293 3 Marktlokation soll als ruhende Marktlokation zu einer Marktlokation „Kundenanlage“ (welche in diesem Fall neu auszuprägen ist), hinzugefügt werden (Bildung)<br/><br/>9991 00000 320 4 Marktlokation soll als ruhende Marktlokation zu einer bestehenden Marktlokation „Kundenanlage“ (welche in diesem Fall bereits existiert), hinzufügt werden (Integration). | 9991 00000 293 3 Marktlokation soll als ruhende Marktlokation zu einer Marktlokation „Kundenanlage“ nach §20 Abs. 1d EnWG (welche in diesem Fall neu auszuprägen ist), hinzugefügt werden (Bildung).<br/><br/>9991 00000 321 2 Marktlokation soll als ruhende Marktlokation zu einer Marktlokation „Kundenanlage“ nach §10c EEG (welche in diesem Fall neu auszuprägen ist), hinzugefügt werden (Bildung).<br/><br/>9991 00000 320 4 Marktlokation soll als ruhende Marktlokation zu einer bestehenden Marktlokation „Kundenanlage“ (welche in diesem Fall bereits existiert), hinzufügt werden (Integration). | Da im EBD E\_0622\_"Prüfen, ob Anmeldung direkt ablehnbar" unter anderem darauf geprüft wird, ob es sich bei der Neubildung einer Kundenanlage um eine Kundenanlage nach §20 Abs. 1d EnWG handelt, muss auch bei der Produktauswahl für den LF im Lieferbeginn die Unterscheidung erfolgen. Die Voraussetzung der Messtechnischen Einordnung "iMS" existiert lediglich bei §20 Abs. 1 EnWG und nicht bei §10c EEG. | Fehler (11.12.2025) |
| 26981  | Kapitel 4 Codelisten der Konfigurationsprodukte und Messprodukte für Werte nach Typ 2                                                                                                                          | Spalte „Ebene“ in der Tabelle der Unterkapitel<br/>4.1 Konfigurationsprodukte Schaltzeitdefinition                                                                                                                                                                                                                                                                                | Spalte „Ebene“ in der Tabelle der Unterkapitel<br/>4.1 Konfigurationsprodukte Schaltzeitdefinition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | In den Kapiteln 4.1, 4.2 und 4.3 wurde die Spalte "Ebene", äquivalent wie in Kapitel 4.4 ergänzt. Hiermit wird verdeutlicht, auf welcher Ebene die Konfigurationsprodukte eingesetzt werden können.                                                                                                                                                                                                                | Fehler (11.12.2025) |


Version: 1.3c

11.12.2025

Seite 57 von 58
<page_number>57</page_number>

Codeliste der Konfigurationen

edi@energy. Datenformate Strom & Gas

| Änd-ID | Ort | Änderungen<br/>Bisher                                                    | Änderungen<br/>Neu                                                       | Grund der Anpassung | Status |
| ------ | --- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------- | ------ |
|        |     | 4.2 9991000000060 Konfigurationspro-<br/>dukte Leistungskurvendefinition | 4.2 9991000000060 Konfigurationspro-<br/>dukte Leistungskurvendefinition |                     |        |
|        |     | 4.3 Konfigurationsprodukte Ad-Hoc-Steuer-<br/>kanal                      | 4.3 Konfigurationsprodukte Ad-Hoc-Steuer-<br/>kanal                      |                     |        |
|        |     | nicht vorhanden                                                          | vorhanden                                                                |                     |        |


Version: 1.3c

11.12.2025

Seite 58 von 58
<page_number>58</page_number>