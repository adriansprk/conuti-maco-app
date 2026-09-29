![edi@energy. Datenformate Strom & Gas](vtnb)

# Konsolidierte Lesefassung mit Fehlerkorrekturen

## Stand: 11.12.2025

# PRICAT Anwendungshandbuch

|Version:|2.0f|
|-|-|
|Stand MIG:|PRICAT 2.0e|
|Ursprüngliches Publikationsdatum:|01.04.2025|
|Autor:|BDEW|


PRICAT Anwendungshandbuch

![edi@energy. Datenformate Strom & Gas](bucb)

## **Disclaimer**

Die PDF-Datei ist das allein gültige Dokument.

Die zusätzlich veröffentlichte Word-Datei dient als informatorische Lesefassung und entspricht
inhaltlich der PDF-Datei. Diese Word-Datei wird bis auf Weiteres rein informatorisch und
ergänzend veröffentlicht unter dem Vorbehalt, zukünftig eine kostenpflichtige Veröffentlichung
der Word-Datei einzuführen.

Zusätzlich werden zur PDF-Datei auch XML-Dateien als optionale Unterstützung gegen Entgelt
veröffentlicht.

Version: 2.0f
11.12.2025
Seite 2 von 29

PRICAT Anwendungshandbuch

![edi@energy. Datenformate Strom & Gas](fjaj)

## Inhaltsverzeichnis

|1|Vorwort|4|
|-|-|-|
|2|Aufbau des Dokumentes|4|
|3|Übersicht der Pakete in der PRICAT|4|
|4|Erläuterung zur Nutzung des RFF-Segments „Vorgängerversion“|5|
|5|PRICAT Anwendungsfälle|6|
||5.1 Preisblätter Ausgleichsenergiepreis und MSB-Leistungen|7|
||5.2 Preisblätter NB-Leistungen|18|
|6|Änderungshistorie|23|






Seite 3 von 29

Version: 2.0f
11.12.2025

PRICAT Anwendungshandbuch

![edi@energy. Datenformate Strom & Gas](uzwb)

## **1   Vorwort**

Das Anwendungshandbuch beschreibt die von dem BDEW für den deutschen Markt
festgelegten Ausprägungen der PRICAT für standardisierte Geschäftsprozesse.

Allgemein ist in der UN/EDIFACT Beschreibung zur PRICAT eine Wiederholung des UNH-Seg-
mentes erlaubt. Auch für den deutschen Markt können je Übertragungsdatei mehrere
Nachrichten ausgetauscht werden, wenn sich diese in der Nachrichten-Referenznummer
(DE0062) des UNH-Segments und im Code des DE1001 des BGM-Segments unterscheiden.

Die Nachricht PRICAT wird entsprechend den Anforderungen der festgelegten
Geschäftsprozesse ausgeprägt.

Das vorliegende Anwendungshandbuch ist immer in Verbindung mit der Nachrichtenbeschrei-
bung des Nachrichtentyps zu interpretieren, da nur alle Dokumente im Zusammenhang und im
Gesamtkontext mit den Prozessen eine Implementierung ermöglichen.

Die Nachricht wird durch den BDEW gepflegt.

## **2   Aufbau des Dokumentes**

In diesem Dokument werden die einzelnen Anwendungsfälle prozessscharf dargestellt. Die
Definition zur Tabellennotation ist den Allgemeinen Festlegungen zu entnehmen.

## **3   Übersicht der Pakete in der PRICAT**

|Paket|Paketvoraussetzung(en)|Bedingungen|
|-|-|-|
|\[1P]|--|Hinweis: Das ist das Standardpaket, wenn keine Bedingung zum Tragen kommt, z. B.<br/>im COM-Segment.|


Version: 2.0f
11.12.2025
Seite 4 von 29

PRICAT Anwendungshandbuch

![edi@energy. Datenformate Strom & Gas](oxml)

## **4   Erläuterung zur Nutzung des RFF-Segments „Vorgängerversion“**

Nachfolgend ist dargestellt, auf welche Vorgängerversion sich eine PRICAT zu beziehen hat, um
die Gültigkeit der entsprechenden Preise zu beenden. Die zeitliche Abfolge des Versands der
PRICAT ist zum einen über die Nummern und zum andern über die senkrechte Zeitachse
dargestellt: Je weiter unten eine PRICAT dargestellt ist, um so später wurde diese erzeugt und
versendet. Der Zeitraum, für den eine PRICAT-Version gültig ist, ist über die waagerechte Achse
dargestellt. Eine PRICAT ist von ihrem Gültigkeitsbeginn immer so lange gültig, bis eine
nachfolgende PRICAT diesen Zeitraum beendet mit dem Beginn des neuen Gültigkeitsbeginns.

### Legende:

| Symbol | Beschreibung |
| :--- | :--- |
| 📄 | PRICAT |
| 🔴—>🔴 | Zeigt auf, wie sich auf Basis des Gültigkeitsbeginns der zu versendenden aktualisierten PRICAT (Pfeilanfang) die Nachricht bestimmen lässt, die im Segment "Vorgängerversion" anzugeben ist (Pfeilspitze). |
| —> | Gibt an, auf welche Nachricht (Pfeilspitze) sich die Nachricht (Pfeilanfang) bezieht. |
| ▭ | Stellt den Gültigkeitszeitraum der Nachricht dar, die in derselben Farbe gehalten ist. |





Seite 5 von 29

Version: 2.0f
11.12.2025

PRICAT Anwendungshandbuch

![edi@energy. Datenformate Strom & Gas](orhq)

## **5   PRICAT Anwendungsfälle**

Der nachfolgenden Tabelle ist zu entnehmen, wie die PRICAT in den jeweiligen
Anwendungsfällen prinzipiell auszuprägen ist.
Die Einheit des Nenners des jeweiligen Preises ergibt sich aus der Artikelnummer bzw. Artikel-
ID. Die physikalische Arbeit wird immer in kWh, die physikalische Leistung in kW angegeben. Bei
Artikeln, die eine Zeitkomponente beinhalten, wird die Einheit des Zeitintervalls, für das der im
PRI-Segment genannte Preis gilt, genannt.

Die in der PRICAT übermittelten Preise sind ausnahmslos Nettopreise.

Die durch das MsbG vorgegebenen Preisobergrenzen sind Jahresbruttopreise. Erfolgt
unterjährig eine Veränderung an der Messlokation, so dass der Messstellenbetrieb zeitanteilig
abzurechnen ist, so erfolgt dies tagesscharf unter Berücksichtigung der Zahl der Tage des
jeweiligen Kalenderjahres. Das bedeutet, dass in einem Schaltjahr der Nenner 366 und nicht
365 Tage beträgt.

Bei der Kalkulation der Nettopreise für die jeweiligen POG-Intervalle wird empfohlen, diese so
festzulegen, dass sichergestellt ist, dass unabhängig davon, in welche Zeitscheiben der Mess-
stellenbetrieb in einem Kalenderjahr aufgeteilt werden muss, die Summe der Bruttopreise für
alle Zeitscheiben eines Jahres immer unterhalb der gesetzlich festgelegten
Bruttopreisobergrenze bleibt.

Version: 2.0f                                                                11.12.2025                                                                Seite 6 von 29

PRICAT Anwendungshandbuch

![edi@energy. Datenformate Strom & Gas](atft)

## **5.1 Preisblätter Ausgleichsenergiepreis und MSB-Leistungen**

|EDIFACT Struktur|Beschreibung|Übermittlungder Ausgleichs-energiepreiseBIKO an BKV27001|PreisblätterMSB-LeistungenMSB an LF / NB27002|Bedingung|
|-|-|-|-|-|
|Nachrichten-Kopfsegment|||||
|**UNH** 00001|Kommunikation von<br/>Prüfidentifikator|Muss \[12]|Muss \[14]|\[12] je UNB ist nur eine<br/>Nachricht mit BGM+Z04 in der<br/>Übertragungsdatei erlaubt<br/>(nur eine Nachricht je<br/>Übertragungsdatei)<br/>\[14] je UNB ist maximal je<br/>Code aus DE1001 eine<br/>Nachricht in der<br/>Übertragungsdatei erlaubt|
|UNH **0062**|Nachrichten-Referenznummer|X|X||
|UNH **0065**|**PRICAT** Preisliste/Katalog|X|X||
|UNH **0052**|**D** Entwurfs-Version|X|X||
|UNH **0054**|**20B** Ausgabe 2020 - B|X|X||
|UNH **0051**|**UN** UN/CEFACT|X|X||
|UNH **0057**|**2.0e** Versionsnummer der<br/>zugrundeliegenden<br/>BDEW-<br/>Nachrichtenbeschreibun<br/>g|X|X||
|Beginn der Nachricht|||||
|**BGM** 00002||Muss|Muss||
|BGM **1001**|**Z04** Ausgleichsenergiepreis<br/>****Z32**** Preisblatt<br/>Messstellenbetrieb<br/>****Z77**** Preisblatt<br/>Konfigurationen<br/>****Z94**** Preisblatt Technik|X|X \[30] ∨ (\[36] ∧<br/>\[33])<br/>X<br/>X|\[30] wenn MP-ID in SG2<br/>NAD+MR in der Rolle LF<br/>\[33] wenn der Zeitpunkt im<br/>DTM+157 DE2380 ≥<br/>01.01.2024 00:00 Uhr<br/>gesetzlicher deutscher Zeit<br/>\[36] Wenn MP-ID in SG2<br/>NAD+MR in der Rolle NB|
|BGM **1004**|Dokumentennummer|X|X||
|BGM **1373**|**11** Dokument nicht<br/>verfügbar||S \[35]|\[35] Wenn das in DE1001<br/>angegebene Preisblatt vom<br/>MSB nicht genutzt wird.|
|Betrachtungszeitintervall|||||
|**DTM** 00003||Muss|||
|DTM **2005**|**492** Bilanzierungsdatum, -<br/>zeit, -periode|X|||
|DTM **2380**|Datum oder Uhrzeit oder<br/>Zeitspanne, Wert|X|||
|DTM **2379**|**610** CCYYMM|X|||
|Nachrichtendatum|||||
|**DTM** 00004||Muss|Muss||
|DTM **2005**|**137** Dokumenten-<br/>/Nachrichtendatum/-zeit|X|X||
|DTM **2380**|Datum oder Uhrzeit oder<br/>Zeitspanne, Wert|X \[931] \[494]|X \[931] \[494]|\[494] Das hier genannte<br/>Datum muss der Zeitpunkt<br/>sein, zu dem das Dokument<br/>erstellt wurde, oder ein<br/>Zeitpunkt, der davor liegt<br/>\[931] Format: ZZZ = +00|
|DTM **2379**|**303** CCYYMMDDHHMMZZZ|X|X||
|Gültigkeitsbeginn|||||
|**DTM** 00005|||Muss||
|DTM **2005**|**157** Gültigkeit, Beginndatum||X||






Seite 7 von 29

Version: 2.0f
11.12.2025

PRICAT Anwendungshandbuch

![edi@energy. Datenformate Strom & Gas](hpxi)

|EDIFACT Struktur|Beschreibung|Übermittlung der Ausgleichs-energiepreise BIKO an BKV 27001|Preisblätter MSB-Leistungen MSB an LF / NB 27002|Bedingung|
|-|-|-|-|-|
|DTM 2380|Datum oder Uhrzeit oder Zeitspanne, Wert||X \[UB1] ∧ (\[43] ∨ \[47] ∨ \[44] ∨ \[56])|\[43] Wenn BGM DE1001 = Z32 und LIN DE7140 im Format n1-n2-n1-n3, dann muss der hier genannte Zeitpunkt ≥ 01.01.2024 00:00 Uhr gesetzlicher deutscher Zeit sein<br/>\[44] Wenn BGM DE1001 = Z77, dann muss der hier genannte Zeitpunkt ≥ 01.10.2023 00:00 Uhr gesetzlicher deutscher Zeit sein<br/>\[47] Wenn BGM DE1001 = Z32 und LIN DE7140 im Format n13, dann muss der hier genannte Zeitpunkt < 01.01.2024 00:00 Uhr gesetzlicher deutscher Zeit sein<br/>\[56] Wenn BGM DE1001 = Z94, dann muss der hier genannte Zeitpunkt ≥ 01.10.2025 00:00 Uhr gesetzlicher deutscher Zeit sein|
|DTM 2379|303 CCYYMMDDHHMMZZZ||X||
|Vorgängerversion<br/>SG1|||**Soll \[1]**|\[1] Wenn Vorgängerversion vorhanden|
|SG1 RFF 00006|||Muss||
|SG1 RFF 1153|ACW Referenznummer einer vorangegangenen Nachricht||X||
|SG1 RFF 1154|Referenz, Identifikation||X \[504]|\[504] Hinweis: Dokumentennummer der PRICAT|
|Prüfidentifikator<br/>SG1||Muss|Muss||
|SG1 RFF 00008||Muss|Muss||
|SG1 RFF 1153|Z13 Prüfidentifikator|X|X||
|SG1 RFF 1154|27001 Übermittlung der Ausgleichsenergiepreise<br/>27002 Preisblatt MSB-Leistungen|X<br/>|<br/>X||
|Empfänger-ID<br/>SG2||Muss|Muss||
|SG2 NAD 00009||Muss|Muss||
|SG2 NAD 3035|MR Nachrichtenempfänger|X|X||
|SG2 NAD 3039|Beteiligter, Identifikation|X \[19]|X \[19]|\[19] Nur MP-ID aus Sparte Strom|
|SG2 NAD 3055|9 GS1<br/>293 DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)|X<br/>X|X<br/>X||
|Sender-ID<br/>SG2||Muss|Muss||
|SG2 NAD 00010||Muss|Muss||






Seite 8 von 29

Version: 2.0f
11.12.2025

PRICAT Anwendungshandbuch

![edi@energy. Datenformate Strom & Gas](mikt)

|EDIFACT Struktur|Beschreibung|Übermittlung der Ausgleichs- energiepreiseBIKO an BKV27001|Preisblätter MSB-LeistungenMSB an LF / NB27002|Bedingung|
|-|-|-|-|-|
|SG2 NAD 3035|MS Dokumenten-/Nachrichtenaussteller bzw. -absender|X|X||
|SG2 NAD 3039|Beteiligter, Identifikation|X \[19]|X \[19]|\[19] Nur MP-ID aus Sparte Strom|
|SG2 NAD 3055|9 GS1<br/>293 DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)|X<br/>X|X<br/>X||
|Regelzone|||||
|SG2|||||
|SG2 LOC 00011||Muss|||
|SG2 LOC 3227|231 Regelzone|X|||
|SG2 LOC 3225|Ortsangabe, Nummer|X|||
|Ansprechpartner|||||
|SG4||Kann|Kann||
|SG4 CTA 00012||Muss|Muss||
|SG4 CTA 3139|IC Informationskontakt|X|X||
|SG4 CTA 3412|Kontakt|X|X||
|Kommunikationsverbindung|||||
|SG4|||||
|SG4 COM 00013||Muss|Muss||
|SG4 COM 3148|Kommunikationsadresse, Identifikation|X ((\[939]\[37]) V (\[940]\[38])) ^ \[519]|X ((\[939]\[37]) V (\[940]\[38])) ^ \[519]|\[37] Wenn im DE3155 in demselben COM der Code EM vorhanden ist<br/>\[38] Wenn im DE3155 in demselben COM der Code TE / FX / AJ / AL vorhanden ist<br/>\[519] Hinweis: Es darf nur eine Information im DE3148 übermittelt werden<br/>\[939] Format: Die Zeichenkette muss die Zeichen @ und . enthalten<br/>\[940] Format: Die Zeichenkette muss mit dem Zeichen + beginnen und danach dürfen nur noch Ziffern folgen|
|SG4 COM 3155|EM E-Mail<br/>FX Telefax<br/>TE Telefon<br/>AJ weiteres Telefon<br/>AL Handy|X \[1P0..1]<br/>X \[1P0..1]<br/>X \[1P0..1]<br/>X \[1P0..1]<br/>X \[1P0..1]|X \[1P0..1]<br/>X \[1P0..1]<br/>X \[1P0..1]<br/>X \[1P0..1]<br/>X \[1P0..1]||
|Währungsangaben|||||
|SG6||Muss|Muss \[9]|\[9] Wenn BGM DE1373 =11 nicht vorhanden|
|SG6 CUX 00014||Muss|Muss||
|SG6 CUX 6347|2 Referenzwährung|X|X||
|SG6 CUX 6345|EUR Euro|X|X||
|SG6 CUX 6343|8 Währung der Preisliste|X|X||
|Produktgruppen-Information|||||
|SG17||Muss|Muss \[9]|\[9] Wenn BGM DE1373 =11 nicht vorhanden|
|SG17 PGI 00015||Muss|Muss||
|SG17 PGI 5379|9 keine Gruppe genutzt|X|X||






Seite 9 von 29

<sub>Version:</sub> 2.0f
11.12.2025

PRICAT Anwendungshandbuch

![edi@energy. Datenformate Strom & Gas](qrra)

|EDIFACT Struktur|Beschreibung|Übermittlungder Ausgleichs-energiepreiseBIKO an BKV27001|PreisblätterMSB-LeistungenMSB an LF / NB27002|Bedingung|
|-|-|-|-|-|
|Positionsdaten|||||
|**SG36**||Muss|Muss||
|SG36 LIN 00016||Muss|Muss||
|SG36 LIN **1082**|Positionsnummer|X \[911]|X \[911]|\[911] Format: Mögliche Werte:<br/>1 bis n, je Nachricht oder<br/>Segmentgruppe bei 1<br/>beginnend und fortlaufend<br/>aufsteigend|


Version: 2.0f                                                              11.12.2025                                                              Seite 10 von 29

PRICAT Anwendungshandbuch

![edi@energy. Datenformate Strom & Gas](oszd)

|EDIFACT Struktur|Beschreibung|Übermittlungder Ausgleichs-energiepreiseBIKO an BKV27001|PreisblätterMSB-LeistungenMSB an LF / NB27002|Bedingung|
|-|-|-|-|-|
|SG36 LIN 7140|Produkt-/Leistungsnummer<br/>Kommunikation von<br/>Prüfidentifikator|X \[941] \[39]|X (\[941] (\[31] \[32] \[40])) (\[942] (\[31] \[33] \[45])) (\[959] (\[34] \[46] \[68] \[69]))) (\[57] ((\[46] *\[70]) \[71])))*|\[31] wenn BGM DE1001 = Z32<br/>(Preisblatt Messstellenbetrieb)<br/>\[32] wenn der Zeitpunkt im<br/>DTM+157 DE2380 <<br/>01.01.2024 00:00 Uhr<br/>gesetzlicher deutscher Zeit<br/>\[33] wenn der Zeitpunkt im<br/>DTM+157 DE2380 ≥<br/>01.01.2024 00:00 Uhr<br/>gesetzlicher deutscher Zeit<br/>\[34] wenn BGM DE1001 = Z77<br/>(Preisblatt Konfigurationen)<br/>\[39] Es sind nur Werte aus der<br/>EDI\@Energy Codeliste der<br/>Artikelnummern und Artikel-ID<br/>erlaubt, die in der Spalte<br/>MaBiS ein X haben<br/>\[40] Es sind nur Werte aus der<br/>EDI\@Energy Codeliste der<br/>Artikelnummern und Artikel-ID<br/>erlaubt, die in der Spalte H ein<br/>X haben<br/>\[45] Es sind nur Werte aus der<br/>EDI\@Energy Codeliste der<br/>Artikelnummern und Artikel-ID<br/>erlaubt, die in dieser in Kapitel<br/>"Abrechnung<br/>Messstellenbetrieb für die<br/>Sparte Strom" für die jeweilige<br/>Marktrolle genannt sind<br/>\[46] Es sind nur Werte aus der<br/>EDI\@Energy Codeliste der<br/>Artikelnummern und Artikel-ID<br/>erlaubt, die in dieser in Kapitel<br/>"Artikel-ID für die<br/>Bestellprozesse beim MSB"<br/>genannt sind<br/>\[57] wenn BGM DE1001 = Z94<br/>(Preisblatt Technik)<br/>\[68] Der Teil des Codes vor<br/>dem "-" muss ein<br/>Messprodukt-Code sein<br/>\[69] Der Teil des Codes vor<br/>dem "-" muss ein<br/>Konfigurationsprodukt-Code<br/>sein<br/>\[70] Der Teil des Codes vor<br/>dem "-" muss ein Produkt-<br/>Code sein<br/>\[71] Es muss der Code<br/>9991000003030-01 sein<br/>\[941] Format: Artikelnummer<br/>\[942] Format: n1-n2-n1-n3<br/>\[959] Format: n13-n2|


Seite 11 von 29

Version: 2.0f
11.12.2025

PRICAT Anwendungshandbuch

![edi@energy. Datenformate Strom & Gas](djpa)

|EDIFACT Struktur|Beschreibung|Übermittlung der Ausgleichs-energiepreise BIKO an BKV 27001|Preisblätter MSB-Leistungen MSB an LF / NB 27002|Bedingung|
|-|-|-|-|-|
|SG36 LIN 7143|Z01 Artikelnummer<br/>**Z09** Artikel-ID|X|X \[31] ∧ \[32]<br/>X (\[31] ∧ \[33]) ∨ \[34] ∨ \[57]|\[31] wenn BGM DE1001 = Z32 (Preisblatt Messstellenbetrieb)<br/>\[32] wenn der Zeitpunkt im DTM+157 DE2380 < 01.01.2024 00:00 Uhr gesetzlicher deutscher Zeit<br/>\[33] wenn der Zeitpunkt im DTM+157 DE2380 ≥ 01.01.2024 00:00 Uhr gesetzlicher deutscher Zeit<br/>\[34] wenn BGM DE1001 = Z77 (Preisblatt Konfigurationen)<br/>\[57] wenn BGM DE1001 = Z94 (Preisblatt Technik)|
|Preisschlüsselstamm<br/>SG36<br/>SG36 PIA 00017|||Muss \[31] ∧ \[32]|\[31] wenn BGM DE1001 = Z32 (Preisblatt Messstellenbetrieb)<br/>\[32] wenn der Zeitpunkt im DTM+157 DE2380 < 01.01.2024 00:00 Uhr gesetzlicher deutscher Zeit|
|SG36 PIA 4347|1 Zusätzliche Identifikation||X||
|SG36 PIA 7140|Code des Preisschlüsselstamms||X||
|SG36 PIA 7143|Z06 Preisschlüsselstamm||X||
|Produktbeschreibung<br/>SG36<br/>SG36 **IMD** 00018|||Muss (\[31] ∧ \[32]) ∨ (\[57] ∧ \[60] ∧ \[61])|\[31] wenn BGM DE1001 = Z32 (Preisblatt Messstellenbetrieb)<br/>\[32] wenn der Zeitpunkt im DTM+157 DE2380 < 01.01.2024 00:00 Uhr gesetzlicher deutscher Zeit<br/>\[57] wenn BGM DE1001 = Z94 (Preisblatt Technik)<br/>\[60] Wenn in dieser SG36 der Teil vor dem "-" aus LIN DE7140 aus der Tabelle des Kapitels "Produkte zur Bestellung einer Änderung an einer Lokation in der Sparte Strom" der EDI\@Energy Codeliste der Konfigurationen<br/>\[61] Wenn in dieser SG36 der Wert der Zahl nach dem "-" aus LIN DE7140 > 01|






Seite 12 von 29

Version: 2.0f
11.12.2025

PRICAT Anwendungshandbuch

![edi@energy. Datenformate Strom & Gas](qidg)

|EDIFACT Struktur|BeschreibungKommunikation vonPrüfidentifikator|Übermittlungder Ausgleichs-energiepreiseBIKO an BKV27001|PreisblätterMSB-LeistungenMSB an LF / NB27002|Bedingung|
|-|-|-|-|-|
|SG36 IMD 7077|C Code (aus der Liste einer<br/>codepflegenden<br/>Organisation)||X (\[31] ∧ \[6])|\[6] Wenn in dieser SG36 LIN in<br/>DE7140 9990001000798<br/>vorhanden|
||F Freier Text||X (\[57] ∧ \[60])|\[7] Wenn in dieser SG36 LIN in<br/>DE7140 9990001000798 nicht<br/>vorhanden<br/>\[31] wenn BGM DE1001 = Z32<br/>(Preisblatt Messstellenbetrieb)<br/>\[57] wenn BGM DE1001 = Z94<br/>(Preisblatt Technik)<br/>\[60] Wenn in dieser SG36 der<br/>Teil vor dem "-" aus LIN<br/>DE7140 aus der Tabelle des<br/>Kapitels "Produkte zur<br/>Bestellung einer Änderung an<br/>einer Lokation in der Sparte<br/>Strom" der EDI\@Energy<br/>Codeliste der Konfigurationen|
||X Teilstrukturiert (Code<br/>und Text)||X (\[31] ∧ \[7])||


Version: 2.0f                                                              11.12.2025                                                              Seite 13 von 29

PRICAT Anwendungshandbuch

![edi@energy. Datenformate Strom & Gas](adni)

|EDIFACT Struktur|BeschreibungKommunikation vonPrüfidentifikator|Übermittlungder Ausgleichs-energiepreiseBIKO an BKV27001|PreisblätterMSB-LeistungenMSB an LF / NB27002|Bedingung|
|-|-|-|-|-|
|SG36 IMD **7081**|**Z15** POG bei verbrauchender<br/>Marktlokation > 100.000<br/>kWh/a mit iMS||X \[4]|\[4] Wenn SG36 IMD+C in<br/>diesem IMD vorhanden<br/>\[5] Wenn SG36 IMD+X in<br/>diesem IMD vorhanden|
||****Z16**** POG bei verbrauchender<br/>Marktlokation \[50.000<br/>kWh/a; 100.000 kWh/a]<br/>mit iMS||X \[4]||
||****Z17**** POG bei verbrauchender<br/>Marktlokation ]20.000<br/>kWh/a; 50.000 kWh/a]<br/>mit iMS||X \[4]||
||****Z18**** POG bei verbrauchender<br/>Marktlokation ]10.000<br/>kWh/a; 20.000 kWh/a]<br/>mit iMS||X \[4]||
||****Z19**** POG bei verbrauchender<br/>Marktlokation mit<br/>unterbrechbaren<br/>Verbrauchseinrichtung<br/>nach § 14a EnWG mit<br/>iMS||X \[4]||
||****Z20**** POG bei verbrauchender<br/>Marktlokation ]6.000<br/>kWh/a; 10.000 kWh/a]<br/>mit iMS||X \[4]||
||****Z21**** POG bei erzeugender<br/>Marktlokation ]7 kW; 15<br/>kW] mit iMS||X \[4]||
||****Z22**** POG bei erzeugender<br/>Marktlokation ]15 kW;<br/>30 kW] mit iMS||X \[4]||
||****Z23**** POG bei erzeugender<br/>Marktlokation ]30 kW;<br/>100 kW] mit iMS||X \[4]||
||****Z24**** POG bei erzeugender<br/>Marktlokation > 100 kW<br/>mit iMS||X \[4]||
||****Z25**** POG bei Marktlokation<br/>mit mME||X \[4]||
||****Z28**** POG bei verbrauchender<br/>Marktlokation ]4.000<br/>kWh/a; 6.000 kWh/a] mit<br/>iMS||X \[4]||
||****Z29**** POG bei verbrauchender<br/>Marktlokation \[3.000<br/>kWh/a; 4.000 kWh/a] mit<br/>iMS||X \[4]||
||****Z30**** POG bei verbrauchender<br/>Marktlokation ]2.000<br/>kWh/a; 3.000 kWh/a] mit<br/>iMS||X \[4]||
||****Z31**** POG bei verbrauchender<br/>Marktlokation \[0 kWh/a;<br/>2.000 kWh/a] mit iMS||X \[4]||
||****Z32**** POG bei optionaler<br/>Ausstattung mit iMS von<br/>Neuanlagen von<br/>erzeugender<br/>Marktlokation||X \[4]||
||****Z41**** Zusatzleistung||X \[5]||






Seite 14 von 29

Version: 2.0f
11.12.2025

PRICAT Anwendungshandbuch

![edi@energy. Datenformate Strom & Gas](gwtq)

|EDIFACT Struktur|Beschreibung|Übermittlung der Ausgleichs-energiepreiseBIKO an BKV27001|Preisblätter MSB-LeistungenMSB an LF / NB27002|Bedingung|
|-|-|-|-|-|
|SG36 IMD **7009**|Kommunikation von Prüfidentifikator<br/>Produkt-/Leistungsbeschreibung, Code<br/>**Z08** Höchstspannung<br/>**Z09** Hochspannung<br/>**Z10** Mittelspannung<br/>**Z11** Niederspannung||M \[2]<br/>X<br/>X<br/>X<br/>X|\[2] Wenn in dieser SG36 LIN in DE7140 9990001000813 vorhanden|
|SG36 IMD **7008**|Produkt-/Leistungsbeschreibung||M \[3] ∨ (\[62] ∧ \[522])|\[3] Wenn IMD+X vorhanden<br/>\[62] Wenn IMD+F vorhanden<br/>\[522] Hinweis: Hier ist die Leistung zu beschreiben, die mit dieser Artikel-ID in Rechnung gestellt wird, wobei darauf zu achten ist, dass zu erkennen ist, wie sich diese von den Leistungen unterscheiden, bei denen die ersten 13 Stellen der Artikel-ID mit den ersten 13 Stellen dieser Artikel-ID identisch sind|
|SG36 IMD **7008**|Produkt-/Leistungsbeschreibung||S \[63]|\[63] Wenn vorheriges DE7008 zur Beschreibung der Leistung dieser Artikel-ID nicht ausreicht|
|**Preisangaben**<br/>SG40||Muss \[53]|Muss (\[520] ∧ **\[34])** ∨ **(\[53]** ∧ *(\[31]* ∨ *\[57]))*|\[31] wenn BGM DE1001 = Z32 (Preisblatt Messstellenbetrieb)<br/>\[34] wenn BGM DE1001 = Z77 (Preisblatt Konfigurationen)<br/>\[53] Diese SG40 darf genau einmal in der SG36 angegeben werden<br/>\[57] wenn BGM DE1001 = Z94 (Preisblatt Technik)<br/>\[520] Hinweis: Falls der Preis des Artikels gezont ist, ist diese SG40 so oft zu wiederholen, bis alle Preise zu diesem Artikel genannt sind|
|SG40 PRI 00019||Muss|Muss||
|SG40 PRI **5125**|CAL Berechnungspreis|X|X||
|SG40 PRI **5118**|Preis, Betrag|X \[912] \[502]|X \[912] \[513]|\[502] Hinweis: Preis in Euro je MWh<br/>\[513] Hinweis: Die zum Preis gehörende Einheit ist in der Codeliste definiert<br/>\[912] Format: max. 6 Nachkommastellen|
|SG40 PRI **5284**|Einzelpreisbasis, Menge|X \[929] \[503]||\[503] Hinweis: Hier ist immer der Wert 1000 einzutragen, da in DE5118 der Preis in €/MWh angegeben wird.<br/>\[929] Format: Möglicher Wert: 1000|
|SG40 PRI **6411**|ANN Jahr||X \[31] ∧ \[32]|\[31] wenn BGM DE1001 = Z32 (Preisblatt Messstellenbetrieb)<br/>\[32] wenn der Zeitpunkt im DTM+157 DE2380 < 01.01.2024 00:00 Uhr gesetzlicher deutscher Zeit|






Seite 15 von 29

Version: 2.0f
11.12.2025

PRICAT Anwendungshandbuch

![edi@energy. Datenformate Strom & Gas](bfwh)

|EDIFACT Struktur|Beschreibung|Übermittlungder Ausgleichs-energiepreiseBIKO an BKV27001|PreisblätterMSB-LeistungenMSB an LF / NB27002|Bedingung|
|-|-|-|-|-|
|Angaben zum Wertebereich|||||
|SG40<br/>SG40 RNG 00020||||Muss \[57] \[65] \[34] wenn BGM DE1001 = Z77<br/>*Soll \[54] \[34]* (Preisblatt Konfigurationen)<br/>\[54] Falls der Preis des Artikels<br/>gezont ist<br/>\[57] wenn BGM DE1001 = Z94<br/>(Preisblatt Technik)<br/>\[65] wenn in dieser SG36 der<br/>Teil des Codes in LIN DE7140<br/>nach dem "-" von "01"<br/>abweicht|
|SG40 RNG 6167|10 jährlicher<br/>Mengenbereich||X||
|SG40 RNG 6411|H87 Stück<br/>**DAY** Tag<br/>**KWH** Kilowattstunde||X<br/>X<br/>X \[57]|\[57] wenn BGM DE1001 = Z94<br/>(Preisblatt Technik)|
|SG40 RNG 6162|Wertebereichsgrenze, untere||X (\[909] \[937])<br/>((\[521] \[34])<br/>*(\[66] \[57]))*|\[34] wenn BGM DE1001 = Z77<br/>(Preisblatt Konfigurationen)<br/>\[57] wenn BGM DE1001 = Z94<br/>(Preisblatt Technik)<br/>\[66] wenn im DE7140 des LIN<br/>dieser SG36 der Teil des Codes<br/>nach dem "-" den Wert 02 hat,<br/>muss dieses DE = 0 sein und in<br/>allen anderen RNG zu Artikel-<br/>ID, bei denen der Teil des<br/>Codes vor dem "-" mit dem<br/>DE7140 des LIN dieser SG36<br/>übereinstimmt, muss der Wert<br/>dieses DE mit dem Wert des<br/>DE6152 eines anderen RNG zu<br/>einer Artikel-ID bei dem der<br/>Teil des Codes vor dem "-" mit<br/>dem DE7140 des LIN dieser<br/>SG36 übereinstimmt, identisch<br/>sein<br/>\[521] Hinweis: Je Artikel-ID<br/>muss in einem RNG der Wert<br/>dieses DE = 0 sein und in allen<br/>anderen RNG zu dieser Artikel-<br/>ID muss der Wert dieses DE<br/>mit dem Wert des DE6152<br/>eines anderen RNG zu dieser<br/>Artikel-ID identisch sein<br/>\[909] Format: Mögliche Werte:<br/>0 bis n<br/>\[937] Format: keine<br/>Nachkommastelle|






Seite 16 von 29

Version: 2.0f
11.12.2025

PRICAT Anwendungshandbuch

![edi@energy. Datenformate Strom & Gas](fktz)

|EDIFACT Struktur|BeschreibungKommunikation vonPrüfidentifikator|Übermittlungder Ausgleichs-energiepreiseBIKO an BKV27001|PreisblätterMSB-LeistungenMSB an LF / NB27002|Bedingung|
|-|-|-|-|-|
|SG40 RNG 6152|Wertebereichsgrenze, obere||M ((\[34] ∧ \[55]) ∨ (\[57] ∧ \[67])) ∧ \[512] (\[908] ∧ *\[937])*|\[34] wenn BGM DE1001 = Z77 (Preisblatt Konfigurationen)<br/>\[55] Wenn in dieser SG36 ein weiteres RNG (d. h. eine weitere Zone) vorhanden ist, in der der Wert des DE6162 (Wertebereichsgrenze, untere) größer ist als der Wert des DE6162 in diesem RNG<br/>\[57] wenn BGM DE1001 = Z94 (Preisblatt Technik)<br/>\[67] wenn in dieser SG17 ein weiteres LIN vorhanden ist, in dem der Teil des Codes vor dem "-" des DE7140 mit dem des DE7140 des LIN dieser SG36 identisch ist und in dem der Wert nach dem "-" um eins größer ist, als der Wert nach dem "-" im DE7140 des LIN dieser SG36<br/>\[512] Hinweis: Der genannte Wert gehört zum Intervall<br/>\[908] Format: Mögliche Werte: 1 bis n<br/>\[937] Format: keine Nachkommastelle|
|Datum/Uhrzeit/Zeitspanne<br/>SG40|||||
|SG40 DTM 00021||Muss|||
|SG40 DTM 2005|163 Verarbeitung,<br/>Beginndatum/-zeit|X|||
||164 Verarbeitung,<br/>Endedatum/-zeit|X|||
|SG40 DTM 2380|Datum oder Uhrzeit oder<br/>Zeitspanne, Wert|X \[931] \[495]||\[495] Der Zeitpunkt muss ≤ dem Wert im DE2380 des DTM+137 sein<br/>\[931] Format: ZZZ = +00|
|SG40 DTM 2379|303 CCYYMMDDHHMMZZZ|X|||
|Nachrichten-Endesegment<br/>UNT 00026||Muss|Muss||
|UNT 0074|Anzahl der Segmente in einer<br/>Nachricht|X|X||
|UNT 0062|Nachrichten-Referenznummer|X|X||


Seite 17 von 29

Version: 2.0f
11.12.2025

PRICAT Anwendungshandbuch

![edi@energy. Datenformate Strom & Gas](yfjr)

## **5.2 Preisblätter NB-Leistungen**

|EDIFACT Struktur|BeschreibungKommunikation vonPrüfidentifikator|Preisblätter NB-LeistungenNB an LF27003|Bedingung|
|-|-|-|-|
|Nachrichten-Kopfsegment||||
|UNH 00001||Muss \[14]|\[14] je UNB ist maximal je Code aus<br/>DE1001 eine Nachricht in der<br/>Übertragungsdatei erlaubt|
|UNH 0062|Nachrichten-Referenznummer|X||
|UNH 0065|PRICAT Preisliste/Katalog|X||
|UNH 0052|D Entwurfs-Version|X||
|UNH 0054|20B Ausgabe 2020 - B|X||
|UNH 0051|UN UN/CEFACT|X||
|UNH 0057|2.0e Versionsnummer der<br/>zugrundeliegenden BDEW-<br/>Nachrichtenbeschreibung|X||
|Beginn der Nachricht||||
|BGM 00002||Muss||
|BGM 1001|Z54 Preisblatt Sperren /<br/>Entsperren und<br/>Verzugskosten|X \[492]|\[492] wenn MP-ID in NAD+MR aus<br/>Sparte Strom|
|BGM 1001|**Z64** Preisblatt Netznutzung<br/>ohne gemeindespezifische<br/>Konzessionsabgaben|X \[492]||
|BGM 1001|**Z67** Preisblatt Blindarbeit|X \[492]||
|BGM 1001|**Z70** Preisblatt Netznutzung:<br/>Gemeindespezifische<br/>Konzessionsabgaben|X \[492]||
|BGM 1004|Dokumentennummer|X||
|BGM 1373|11 Dokument nicht verfügbar|S \[8]|\[8] Wenn das in DE1001 angegebene<br/>Preisblatt vom NB nicht genutzt wird.|
|Nachrichtendatum||||
|DTM 00004||Muss||
|DTM 2005|137 Dokumenten-<br/>/Nachrichtendatum/-zeit|X||
|DTM 2380|Datum oder Uhrzeit oder<br/>Zeitspanne, Wert|X \[931] \[494]|\[494] Das hier genannte Datum muss<br/>der Zeitpunkt sein, zu dem das<br/>Dokument erstellt wurde, oder ein<br/>Zeitpunkt, der davor liegt<br/>\[931] Format: ZZZ = +00|
|DTM 2379|303 CCYYMMDDHHMMZZZ|X||
|Gültigkeitsbeginn||||
|DTM 00005||Muss||
|DTM 2005|157 Gültigkeit, Beginndatum|X||
|DTM 2380|Datum oder Uhrzeit oder<br/>Zeitspanne, Wert|X \[UB1]||
|DTM 2379|303 CCYYMMDDHHMMZZZ|X||
|Vorgängerversion||||
|SG1||**Soll \[1]** ∧ **((\[50]** ∧ **\[52])** ∨<br/>**\[51])**|\[1] Wenn Vorgängerversion vorhanden<br/>\[50] Wenn MP-ID aus RFF+Z56 mit MP-<br/>ID aus NAD+MS identisch ist<br/>\[51] Wenn BGM+Z54 vorhanden<br/>\[52] Wenn BGM+Z54 nicht vorhanden|
|SG1 RFF 00006||Muss||
|SG1 RFF 1153|ACW Referenznummer einer<br/>vorangegangenen<br/>Nachricht|X||
|SG1 RFF 1154|Referenz, Identifikation|X \[504]|\[504] Hinweis: Dokumentennummer<br/>der PRICAT|


Seite 18 von 29

Version: 2.0f
11.12.2025

PRICAT Anwendungshandbuch

![edi@energy. Datenformate Strom & Gas](ftxj)

|EDIFACT Struktur|BeschreibungKommunikation vonPrüfidentifikator|Preisblätter NB-LeistungenNB an LF27003|Bedingung|
|-|-|-|-|
|Preise des Netzbetreibers||||
|SG1||**Muss \[52]** ∧ \[64]|\[52] Wenn BGM+Z54 nicht vorhanden<br/>\[64] Wenn der Zeitpunkt im DTM+157<br/>DE2380 ≥ 01.01.2026, 00:00 Uhr<br/>gesetzlicher deutscher Zeit|
|SG1 RFF 00007||Muss||
|SG1 RFF 1153|Z56 Preise des Netzbetreibers|X||
|SG1 RFF 1154|MP-ID|X||
|Prüfidentifikator||||
|SG1||Muss||
|SG1 RFF 00008||Muss||
|SG1 RFF 1153|Z13 Prüfidentifikator|X||
|SG1 RFF 1154|27003 Preisblatt NB-Leistungen|X||
|Empfänger-ID||||
|SG2||Muss||
|SG2 NAD 00009||Muss||
|SG2 NAD 3035|MR Nachrichtenempfänger|X||
|SG2 NAD 3039|Beteiligter, Identifikation|X||
|SG2 NAD 3055|9 GS1|X||
||293 DE, BDEW (Bundesverband<br/>der Energie- und<br/>Wasserwirtschaft e.V.)|X||
||332 DE, DVGW Service &<br/>Consult GmbH|X||
|Sender-ID||||
|SG2||Muss||
|SG2 NAD 00010||Muss||
|SG2 NAD 3035|MS Dokumenten-<br/>/Nachrichtenaussteller<br/>bzw. -absender|X||
|SG2 NAD 3039|Beteiligter, Identifikation|X||
|SG2 NAD 3055|9 GS1|X||
||293 DE, BDEW (Bundesverband<br/>der Energie- und<br/>Wasserwirtschaft e.V.)|X||
||332 DE, DVGW Service &<br/>Consult GmbH|X||
|Ansprechpartner||||
|SG4||**Kann**||
|SG4 CTA 00012||Muss||
|SG4 CTA 3139|IC Informationskontakt|X||
|SG4 CTA 3412|Kontakt|X||
|Kommunikationsverbindung||||
|SG4||Muss||
|SG4 COM 00013||Muss||
|SG4 COM 3148|Kommunikationsadresse,<br/>Identifikation|X ((\[939]\[37]) V<br/>(\[940]\[38])) ∧ \[519]|\[37] Wenn im DE3155 in demselben<br/>COM der Code EM vorhanden ist<br/>\[38] Wenn im DE3155 in demselben<br/>COM der Code TE / FX / AJ / AL<br/>vorhanden ist<br/>\[519] Hinweis: Es darf nur eine<br/>Information im DE3148 übermittelt<br/>werden<br/>\[939] Format: Die Zeichenkette muss<br/>die Zeichen @ und . enthalten<br/>\[940] Format: Die Zeichenkette muss<br/>mit dem Zeichen + beginnen und<br/>danach dürfen nur noch Ziffern folgen|






Seite 19 von 29

Version: 2.0f
11.12.2025

PRICAT Anwendungshandbuch

![edi@energy logo](xobv)

|EDIFACT Struktur|BeschreibungKommunikation vonPrüfidentifikator|Preisblätter NB-LeistungenNB an LF27003|Bedingung|
|-|-|-|-|
|SG4 COM **3155**|**EM** E-Mail<br/>**FX** Telefax<br/>**TE** Telefon<br/>**AJ** weiteres Telefon<br/>**AL** Handy|X \[1P0..1]<br/>X \[1P0..1]<br/>X \[1P0..1]<br/>X \[1P0..1]<br/>X \[1P0..1]||
|Währungsangaben<br/>SG6||Muss \[9]|\[9] Wenn BGM DE1373 =11 nicht<br/>vorhanden|
|SG6 CUX 00014||Muss||
|SG6 CUX **6347**|**2** Referenzwährung|X||
|SG6 CUX **6345**|**EUR** Euro|X||
|SG6 CUX **6343**|**8** Währung der Preisliste|X||
|Produktgruppen-<br/>Information<br/>SG17||Muss \[9] ∧ \[27]|\[9] Wenn BGM DE1373 =11 nicht<br/>vorhanden<br/>\[27] Wenn BGM DE1001 = Z70 nicht<br/>vorhanden|
|SG17 PGI 00015||Muss||
|SG17 PGI **5379**|**9** keine Gruppe genutzt|X||
|Positionsdaten<br/>SG36||Muss||
|SG36 LIN 00016||Muss||
|SG36 LIN **1082**|Positionsnummer|X \[911]|\[911] Format: Mögliche Werte: 1 bis n,<br/>je Nachricht oder Segmentgruppe bei<br/>1 beginnend und fortlaufend<br/>aufsteigend|
|SG36 LIN **7140**|Produkt-/Leistungsnummer|X \[942] ∧ \[41]|\[41] Es sind nur Werte aus der<br/>EDI\@Energy Codeliste der<br/>Artikelnummern und Artikel-ID<br/>erlaubt, die in der Spalte "PRICAT<br/>Codeverwendung" ein X haben<br/>\[942] Format: n1-n2-n1-n3|
|SG36 LIN **7143**|**Z09** Artikel-ID|X||
|Preisangaben<br/>SG40||**Muss \[22]** ∧ \[53]|\[22] Wenn die Artikel-ID aus dieser<br/>SG36 LIN DE7140 in der EDI\@Energy<br/>Codeliste der Artikelnummern und<br/>Artikel-ID in der Spalte "PRICAT<br/>Preisangabe" ein X hat<br/>\[53] Diese SG40 darf genau einmal in<br/>der SG36 angegeben werden|
|SG40 PRI 00019||Muss||
|SG40 PRI **5125**|**CAL** Berechnungspreis|X||
|SG40 PRI **5118**|Preis, Betrag|X (\[946] \[513]) ∧ ((\[968] \[48]) ∨ (\[902] \[49]))|\[48] Wenn in dieser SG36 LIN in<br/>DE7140 einer der Codes 1-01-6-005 /<br/>1-01-9-001 / 1-01-9-002 / 1-02-0-015 /<br/>1-03-8-001 / 1-03-8-002 / 1-03-8-003 /<br/>1-03-8-004 / 1-03-9-001 / 1-03-9-002 /<br/>1-03-9-003 / 1-03-9-004 / 1-07-4-001<br/>vorhanden<br/>\[49] Wenn in dieser SG36 LIN in<br/>DE7140 keiner der Codes 1-01-6-005 /<br/>1-01-9-001 / 1-01-9-002 / 1-02-0-015 /<br/>1-03-8-001 / 1-03-8-002 / 1-03-8-003 /<br/>1-03-8-004 / 1-03-9-001 / 1-03-9-002 /<br/>1-03-9-003 / 1-03-9-004 / 1-07-4-001<br/>vorhanden<br/><br/>\[513] Hinweis: Die zum Preis<br/>gehörende Einheit ist in der Codeliste<br/>definiert<br/>\[902] Format: Möglicher Wert: ≥ 0<br/>\[946] Format: max. 11<br/>Nachkommastellen<br/>\[968] Format: Möglicher Wert: ≤ 0|






Seite 20 von 29

Version: 2.0f
11.12.2025

PRICAT Anwendungshandbuch

![edi@energy logo](colj)

|EDIFACT Struktur|BeschreibungKommunikation vonPrüfidentifikator|Preisblätter NB-LeistungenNB an LF27003|Bedingung|
|-|-|-|-|
|Netzbetreiberindividuelle<br/>Artikel-ID<br/>SG17||**Muss \[9]** \[26]|\[9] Wenn BGM DE1373 =11 nicht<br/>vorhanden<br/>\[26] Wenn BGM DE1001 = Z70<br/>vorhanden|
|SG17 PGI 00022||Muss||
|SG17 PGI 5379|Z01 Netzbetreiberindividuelle<br/>Artikel-ID|X||
|Positionsdaten<br/>SG36||Muss||
|SG36 LIN 00023||Muss||
|SG36 LIN 1082|Positionsnummer|X \[911]|\[911] Format: Mögliche Werte: 1 bis n,<br/>je Nachricht oder Segmentgruppe bei<br/>1 beginnend und fortlaufend<br/>aufsteigend|
|SG36 LIN 7140|Produkt-/Leistungsnummer|X (\[948] \[949] \[957])<br/>\[42]|\[42] Es sind nur Werte erlaubt, die die<br/>Bildungsvorschrift der EDI\@Energy<br/>Codeliste der Artikelnummern und<br/>Artikel-ID erfüllen, und die in der<br/>Spalte "PRiCAT Codeverwendung" ein<br/>X haben<br/>\[948] Format: n1-n2-n1-n8-n2<br/>\[949] Format: n1-n2-n1-n8-n2-n1<br/>\[957] Format: n1-n2-n1-n8|
|SG36 LIN 7143|Z09 Artikel-ID|X||
|Preisangaben<br/>SG40||Muss||
|SG40 PRI 00024||Muss||
|SG40 PRI 5125|CAL Berechnungspreis|X||
|SG40 PRI 5118|Preis, Betrag|X \[946]|\[946] Format: max. 11<br/>Nachkommastellen|
|Zonenintervallgrenzen<br/>SG40||||
|SG40 RNG 00025||Muss \[24]|\[24] Wenn in dieser SG36 Wert von LIN<br/>DE7140 im Format n1-n2-n1-n8-n2-n1|
|SG40 RNG 6167|10 jährlicher Mengenbereich|X||
|SG40 RNG 6411|KWH Kilowattstunde|X||
|SG40 RNG 6162|Wertebereichsgrenze, untere|X (\[926] \[28] \[908] \[29])<br/>\[72] \[511]|\[28] Wenn die zugehörige Artikel-ID in<br/>der letzten Stelle eine 1 ist<br/>\[29] Wenn die zugehörige Artikel-ID in<br/>der letzten Stelle > 1 ist<br/>\[72] Wenn in dieser SG36 die letzte<br/>Ziffer von LIN DE7140 >1 ist, dann<br/>muss es eine SG36 geben dessen<br/>Inhalt von LIN DE7140 sich von dem in<br/>dieser SG36 nur in der letzten Ziffer<br/>unterscheidet und in der der Wert von<br/>RNG DE6152 mit dem Wert dieses<br/>DE6162 übereinstimmt<br/>\[511] Hinweis: 1. Der genannte Wert<br/>gehört nicht zum Intervall.<br/>2. Die untere Wertegrenze zu der<br/>Artikel-ID, deren Zahl an der letzten<br/>Stelle den Wert n hat, muss kleiner<br/>sein, als die untere Wertegrenze zu<br/>der Artikel-ID, deren Zahl an der<br/>letzten Stelle den Wert n+1 hat.<br/>\[908] Format: Mögliche Werte: 1 bis n<br/>\[926] Format: Möglicher Wert: 0|






Seite 21 von 29

Version: 2.0f
11.12.2025

PRICAT Anwendungshandbuch

![edi@energy. Datenformate Strom & Gas](zfgf)

|EDIFACT Struktur|BeschreibungKommunikation vonPrüfidentifikator|Preisblätter NB-LeistungenNB an LF27003|Bedingung|
|-|-|-|-|
|SG40 RNG 6152|Wertebereichsgrenze, obere|M \[10] ∧ \[512]|\[10] Wenn eine weitere SG36<br/>vorhanden ist, bei der sich der Inhalt<br/>von LIN DE7140 von LIN DE7140 dieser<br/>SG36 nur in der Ziffer nach dem<br/>letzten "-" unterscheidet und die Ziffer<br/>dort größer ist als in dieser SG36 (also<br/>eine Artikel-ID zur selben<br/>Gruppenartikel-ID vorhanden ist)<br/>\[512] Hinweis: Der genannte Wert<br/>gehört zum Intervall|
|Nachrichten-Endesegment||||
|UNT 00026||Muss||
|UNT 0074|Anzahl der Segmente in einer<br/>Nachricht|X||
|UNT 0062|Nachrichten-Referenznummer|X||






Seite 22 von 29

Version: 2.0f
11.12.2025

PRICAT Anwendungshandbuch

![edi@energy. Datenformate Strom & Gas](tbcf)

## **6 Änderungshistorie**

Version: 2.0f                                                                                                        11.12.2025                                                                                                        Seite 23 von 29

PRICAT Anwendungshandbuch

![edi@energy logo](nzvw)

|Änd-ID|Ort|Bisher|Neu|Grund der Anpassung|Status|
|-|-|-|-|-|-|
|26806|SG1 Preise des Netzbetreibers Anwendungsfall Preisblätter NB-Leistungen, dem der PID 27003 zugeordnet ist|Muss \[52]<br/><br/>\[52] Wenn BGM+Z54 nicht vorhanden|Muss \[52] ∧ \[64]<br/><br/>\[52] Wenn BGM+Z54 nicht vorhanden<br/>\[64] Wenn der Zeitpunkt im DTM+157 DE2380 ≥ 01.01.2026, 00:00 Uhr gesetzlicher deutscher Zeit|Die für 2025 versandten Preisblätter (im Nachrichtentyp PRICAT) können diese Information erst ab dem 06. 06.2025 enthalten, was aber zu spät ist, da diese Information bereits bei Eintreffen der ersten Rechnung mit dieser Information abgeprüft wird. Darüber hinaus würde, sobald sich eine Rechnung, die vor dem 06.06.2025 ausgestellt wurde, die sich nach dem 06. 06.2025 als falsch herausstellt dazu führen, dass diese storniert werden muss und dass die neu ausgestellte nun richtige Rechnung auch diese Segmentgruppe enthalten müsste, so dass für eine Vielzahl an Jahren vor dem Jahr 2025 ebenfalls Preisblätter mit dieser Segmentgruppe vorliegen müssten. Dies würde bedeuten, dass alle bisher versandten Preisblätter erneut versandt werden müssten. Dieser Aufwand, der so nicht vorgesehen war, wird durch diese Fehlerkorrektur vermieden.|Fehler (23.06.2025)|
|26992|SG17 PGI-SG36 SG36 LIN-PIA-IMD-SG40 LIN Positionsdaten DE7140 Anwendungsfall "Preisblätter NB-Leistungen", dem der PID 27002 zugeordnet ist.|\[...] ∨ (\[942] (\[31] ∧ \[33] ∧ \[45])) ∨ \[...]<br/>\[31] wenn BGM DE1001 = Z32<br/>\[33] wenn der Zeitpunkt im DTM+157 DE2380 ≥ 01.01. 2024 00:00 Uhr gesetzlicher deutscher Zeit<br/>\[45] Es sind nur Werte aus der EDI\@Energy Codeliste der Artikelnummern und Artikel-ID erlaubt, die in dieser in Kapitel "Abrechnung Messstellenbetrieb für die Sparte Strom" genannt sind|\[...] ∨ (\[942] (\[31] ∧ \[33] ∧ \[45])) ∨ \[...]<br/>\[31] wenn BGM DE1001 = Z32 (Preisblatt Messstellenbetrieb)<br/>\[33] wenn der Zeitpunkt im DTM+157 DE2380 ≥ 01.01. 2024 00:00 Uhr gesetzlicher deutscher Zeit<br/>\[45] Es sind nur Werte aus der EDi\@Energy Codeliste der Artikelnummern und Artikel-ID erlaubt, die in dieser in Kapitel "Abrechnung Messstellenbetrieb für die Sparte Strom" für die|Präzisierung der Bedingung 45: Der Anwendungsfall sieht als Empfänger den NB oder LF vor. Das genannte Kapitel der Codeliste enthält zwei Codelisten. Diese sind getrennt für Empfänger NB / LF. Die Bedingung wurde dahingehend präzisiert, dass in dem Anwendungsfall auch nur die|Fehler (11.12.2025)|


Version: 2.0f

11.12.2025

Seite 24 von 29

PRICAT Anwendungshandbuch

![edi@energy logo](hpnz)

|Änd-ID|Ort|Änderungen<br/>Bisher|Änderungen<br/>Neu|Grund der Anpassung|Status|
|-|-|-|-|-|-|
|||\[942] Format: n1-n2-n1-n3|jeweilige Marktrolle genannt sind<br/>\[942] Format: n1-n2-n1-n3|Artikel-ID für die jeweilige,<br/>empfangende Marktrolle<br/>genutzt werden können.||
|26962|Kapitel 5.1<br/>Preisblätter<br/>Ausgleichsenergiepre<br/>is und MSB-<br/>Leistungen<br/>SG17 PGI-SG36<br/>SG36 LIN-PIA-IMD-<br/>SG40<br/>LIN Positionsdaten<br/>Produkt-/<br/>Leistungsnummer<br/>DE7140<br/>Anwendungsfall,<br/>dem der PID 27002<br/>zugeordnet ist|X \[...] ⊻ (\[959] (\[34] ∧ \[46] ∧ \[58])) ⊻ (\[959] (\[57]<br/>∧ \[46] ∧ \[59]))<br/><br/>\[34] wenn BGM DE1001 = Z77 (Preisblatt<br/>Konfigurationen)<br/>\[46] Es sind nur Werte aus der EDI\@Energy<br/>Codeliste der Artikelnummern und Artikel-ID<br/>erlaubt, die in dieser in Kapitel "Artikel-ID für die<br/>Bestellprozesse beim MsB" genannt sind<br/>\[57] wenn BGM DE1001 = Z94 (Preisblatt<br/>Technik)<br/>\[58] Der Teil des Codes vor dem "-" muss mit<br/>einem der Codes aus der EDI\@Energy Codeliste<br/>der Konfigurationen übereinstimmen, die nicht<br/>im Kapitel Produkte zur Bestellung einer<br/>Änderung an einer Lokation in der Sparte Strom<br/>genannt sind<br/>\[59] Der Teil des Codes vor dem "-" muss mit<br/>einem der Codes aus der EDI\@Energy Codeliste<br/>der Konfigurationen übereinstimmen, die im<br/>Kapitel Produkte zur Bestellung einer Änderung<br/>an einer Lokation in der Sparte Strom genannt<br/>sind<br/>\[959] Format: n13-n2|X \[...] ⊻ (\[959] (\[34] ∧ \[46] ∧ (\[68] ∧ \[69]))) ⊻<br/>(\[959] (\[57] ∧ ((\[46] ∧ \[70]) ∧ \[71])))<br/><br/>\[34] wenn BGM DE1001 = Z77 (Preisblatt<br/>Konfigurationen)<br/>\[46] Es sind nur Werte aus der EDI\@Energy<br/>Codeliste der Artikelnummern und Artikel-ID<br/>erlaubt, die in dieser in Kapitel "Artikel-ID für die<br/>Bestellprozesse beim MsB" genannt sind<br/>\[57] wenn BGM DE1001 = Z94 (Preisblatt<br/>Technik)<br/>\[68] Der Teil des Codes vor dem "-" muss ein<br/>Messprodukt-Code sein<br/>\[69] Der Teil des Codes vor dem "-" muss ein<br/>Konfigurationsprodukt-Code sein<br/>\[70] Der Teil des Codes vor dem "-" muss ein<br/>Produkt-Code sein<br/>\[71] Es muss der Code 9991000003030-01 sein<br/>\[959] Format: n13-n2|Die bisherige Formulierung<br/>verhindert, dass die Artikel-ID<br/>9991000003030-01 "Pauschale<br/>Kosten für das Scheitern der<br/>Änderung der Technik an einer<br/>Lokation" verwendet werden<br/>könnte.|Fehler (11.12.2025)|
|26903|SG17 PGI-SG36<br/>SG36 LIN-PIA-IMD-<br/>SG40<br/>IMD<br/>Produktbeschreibung<br/>Anwendungsfall<br/>Preisblätter MSB-<br/>Leistungen, dem der<br/>PID 27002<br/>zugeordnet ist|Muss (\[31] ∧ \[32]) ⊻ (\[60] ∧ \[61])<br/><br/>\[31] wenn BGM DE1001 = Z32<br/>\[32] wenn der Zeitpunkt im DTM+157 DE2380 <<br/>01.01.2024 00:00 Uhr gesetzlicher deutscher Zeit<br/>\[60] Wenn in dieser SG36 der Teil vor dem "-"<br/>aus LIN DE7140 aus der Tabelle des Kapitels<br/>"Produkte zur Bestellung einer Änderung an<br/>einer Lokation in der Sparte Strom" der<br/>EDI\@Energy Codeliste der Konfigurationen<br/>\[61] Wenn in dieser SG36 der Wert der Zahl nach<br/>dem "-" aus LIN DE7140 >01|Muss (\[31] ∧ \[32]) ⊻ (\[57] ∧ \[60] ∧ \[61])<br/><br/>\[31] wenn BGM DE1001 = Z32 (Preisblatt<br/>Messstellenbetrieb)<br/>\[32] wenn der Zeitpunkt im DTM+157 DE2380 <<br/>01.01.2024 00:00 Uhr gesetzlicher deutscher<br/>Zeit<br/>\[57] wenn BGM DE1001 = Z94 (Preisblatt<br/>Technik)<br/>\[60] Wenn in dieser SG36 der Teil vor dem "-"<br/>aus LIN DE7140 aus der Tabelle des Kapitels<br/>"Produkte zur Bestellung einer Änderung an<br/>einer Lokation in der Sparte Strom" der|Ergänzung um eine redundante<br/>Bedingung zur Vereinfachung<br/>des fachlichen Verständnisses|Fehler (30.09.2025)|






Seite 25 von 29

Version: 2.0f
11.12.2025

PRICAT Anwendungshandbuch

![edi@energy logo](uzuo)

|Änd-ID|Ort|ÄnderungenBisher|ÄnderungenNeu|Grund der Anpassung|Status|
|-|-|-|-|-|-|
||||EDI\@Energy Codeliste der Konfigurationen<br/>\[61] Wenn in dieser SG36 der Wert der Zahl<br/>nach dem "\_" aus LIN DE7140 > 01|||
|26904|SG17 PGI-SG36<br/>SG36 LIN-PIA-IMD-<br/>SG40<br/>IMD<br/>Produktbeschreibung<br/>DE7077<br/>Anwendungsfall<br/>Preisblätter MSB-<br/>Leistungen, dem der<br/>PID 27002<br/>zugeordnet ist|C Code (aus der Liste einer codepflegenden<br/>Organisation) X \[6]<br/>F Freier Text X \[60]<br/>X Teilstrukturiert (Code und Text) X \[7]<br/><br/>\[6] Wenn in dieser SG36 LIN in DE7140<br/>9990001000798 vorhanden<br/>\[7] Wenn in dieser SG36 LIN in DE7140<br/>9990001000798 nicht vorhanden<br/>\[60] Wenn in dieser SG36 der Teil vor dem "-"<br/>aus LIN DE7140 aus der Tabelle des Kapitels<br/>"Produkte zur Bestellung einer Änderung an<br/>einer Lokation in der Sparte Strom" der<br/>EDI\@Energy Codeliste der Konfigurationen|C Code (aus der Liste einer codepflegenden<br/>Organisation) X (\[31] ∧ \[6])<br/>F Freier Text X (\[57] ∧ \[60])<br/>X Teilstrukturiert (Code und Text) X (\[31] ∧ \[7])<br/><br/>\[6] Wenn in dieser SG36 LIN in DE7140<br/>9990001000798 vorhanden<br/>\[7] Wenn in dieser SG36 LIN in DE7140<br/>9990001000798 nicht vorhanden<br/>\[31] wenn BGM DE1001 = Z32 (Preisblatt<br/>Messstellenbetrieb)<br/>\[57] wenn BGM DE1001 = Z94 (Preisblatt<br/>Technik)<br/>\[60] Wenn in dieser SG36 der Teil vor dem "-"<br/>aus LIN DE7140 aus der Tabelle des Kapitels<br/>"Produkte zur Bestellung einer Änderung an<br/>einer Lokation in der Sparte Strom" der<br/>EDI\@Energy Codeliste der Konfigurationen|Präzisierung, dass im Preisblatt<br/>Technik ausschließlich der<br/>Code F verwendet werden<br/>kann. Diese Präzisierung<br/>erfolgte auf diese mit gewissen<br/>Redundanzen verbundene Art<br/>und Weise, um die<br/>dahinterliegende Fachlichkeit<br/>leichter verständlich<br/>darzustellen.|Fehler (30.09.2025)|
|26906|SG17 PGI-SG36<br/>SG36 LIN-PIA-IMD-<br/>SG40<br/>SG40 Preisangabe<br/>Anwendungsfall<br/>"Preisblätter MSB-<br/>Leistungen", dem der<br/>PID 27002<br/>zugeordnet ist|Muss \[520]<br/><br/>\[520] Hinweis: Falls der Preis des Artikels gezont<br/>ist, ist diese SG40 so oft zu wiederholen, bis alle<br/>Preise zu diesem Artikel genannt sind|Muss (\[520] ∧ \[34] ∨ (\[53] ∧ (\[31] ∨ \[57])))<br/><br/>\[31] wenn BGM DE1001 = Z32 (Preisblatt<br/>Messstellenbetrieb)<br/>\[34] wenn BGM DE1001 = Z77 (Preisblatt<br/>Konfigurationen)<br/>\[53] Diese SG40 darf genau einmal in der SG36<br/>angegeben werden<br/>\[57] wenn BGM DE1001 = Z94 (Preisblatt<br/>Technik)<br/>\[520] Hinweis: Falls der Preis des Artikels gezont<br/>ist, ist diese SG40 so oft zu wiederholen, bis alle<br/>Preise zu diesem Artikel genannt sind|Anpassung, um die<br/>Unterschiede der<br/>Preisgestaltungsmöglichkeiten<br/>im Rahmen der<br/>Konfigurationsprodukten von<br/>denen im Rahmen der<br/>Änderung der Technik an einer<br/>Lokation in Bedingungen zu<br/>überführen|Fehler (30.09.2025)|
|26907|SG17 PGI-SG36<br/>SG36 LIN-PIA-IMD-<br/>SG40<br/>SG40 Preisangabe<br/>RNG Angaben zum|Soll \[54] ∧ (\[34] ∨ \[57])<br/><br/>\[34] wenn BGM DE1001 = Z77<br/>\[54] Falls der Preis des Artikels gezont ist<br/>\[57] wenn BGM DE1001 = Z94|Muss \[57] ∧ \[65]<br/>Soll \[54] ∧ \[34]<br/><br/>\[34] wenn BGM DE1001 = Z77 (Preisblatt<br/>Konfigurationen)|Anpassung, um die<br/>Unterschiede der<br/>Preisgestaltungsmöglichkeiten<br/>im Rahmen der<br/>Konfigurationsprodukten von|Fehler (30.09.2025)|


Version: 2.0f
11.12.2025
Seite 26 von 29

PRICAT Anwendungshandbuch

![edi@energy. Datenformate Strom & Gas](lesr)

|Änd-ID|Ort|Änderungen<br/>Bisher|Änderungen<br/>Neu|Grund der Anpassung|Status|
|-|-|-|-|-|-|
||Wertebereich<br/>Anwendungsfall<br/>"Preisblätter MSB-<br/>Leistungen", dem der<br/>PID 27002<br/>zugeordnet ist||\[54] Falls der Preis des Artikels gezont ist<br/>\[57] wenn BGM DE1001 = Z94 (Preisblatt<br/>Technik)<br/>\[65] wenn in dieser SG36 der Teil des Codes in<br/>LIN DE7140 nach dem "-" von "01" abweicht|denen im Rahmen der<br/>Änderung der Technik an einer<br/>Lokation in Bedingungen zu<br/>überführen||
|26908|SG17 PGI-SG36<br/>SG36 LIN-PIA-IMD-<br/>SG40<br/>SG40 Preisangabe<br/>RNG Angaben zum<br/>Wertebereich<br/>DE6411<br/>Anwendungsfall<br/>"Preisblätter MSB-<br/>Leistungen", dem der<br/>PID 27002<br/>zugeordnet ist|H87 Stück X<br/>DAY Tag X|H87 Stück X<br/>DAY Tag X<br/>KWH Kilowattstunde X \[57]<br/><br/>\[57] wenn BGM DE1001 = Z94 (Preisblatt<br/>Technik)|Anpassung, um die<br/>Unterschiede der<br/>Preisgestaltungsmöglichkeiten<br/>im Rahmen der<br/>Konfigurationsprodukten von<br/>denen im Rahmen der<br/>Änderung der Technik an einer<br/>Lokation in Bedingungen zu<br/>überführen|Fehler (30.09.2025)|
|26909|SG17 PGI-SG36<br/>SG36 LIN-PIA-IMD-<br/>SG40<br/>SG40 Preisangabe<br/>RNG Angaben zum<br/>Wertebereich<br/>DE6162<br/>Anwendungsfall<br/>"Preisblätter MSB-<br/>Leistungen", dem der<br/>PID 27002<br/>zugeordnet ist|X (\[909] ∧ \[937]) \[521]<br/><br/>\[521] Hinweis: Je Artikel-ID muss in einem RNG<br/>der Wert dieses DE = 0 sein und in allen anderen<br/>RNG zu dieser Artikel-ID muss der Wert dieses<br/>DE mit dem Wert des DE6152 eines anderen<br/>RNG zu dieser Artikel-ID identisch sein<br/>\[909] Format: Mögliche Werte: 0 bis n<br/>\[937] Format: keine Nachkommastelle|X (\[909] ∧ \[937]) ((\[521] ∧ \[34]) ∨ (\[66] ∧ \[57]))<br/><br/>\[34] wenn BGM DE1001 = Z77 (Preisblatt<br/>Konfigurationen)<br/>\[521] Hinweis: Je Artikel-ID muss in einem RNG<br/>der Wert dieses DE = 0 sein und in allen anderen<br/>RNG zu dieser Artikel-ID muss der Wert dieses<br/>DE mit dem Wert des DE6152 eines anderen<br/>RNG zu dieser Artikel-ID identisch sein<br/>\[57] wenn BGM DE1001 = Z94 (Preisblatt<br/>Technik)<br/>\[66] wenn im DE7140 des LIN dieser SG36 der<br/>Teil des Codes nach dem "-" den Wert 02 hat,<br/>muss dieses DE = 0 sein und in allen anderen<br/>RNG zu Artikel-ID, bei denen der Teil des Codes<br/>vor dem "\_" mit dem DE7140 des LIN dieser<br/>SG36 übereinstimmt, muss der Wert dieses DE<br/>mit dem Wert des DE6152 eines anderen RNG<br/>zu einer Artikel-ID bei dem der Teil des Codes<br/>vor dem "-" mit dem DE7140 des LIN dieser<br/>SG36 übereinstimmt, identisch sein<br/>\[909] Format: Mögliche Werte: 0 bis n|Anpassung, um die<br/>Unterschiede der<br/>Preisgestaltungsmöglichkeiten<br/>im Rahmen der<br/>Konfigurationsprodukten von<br/>denen im Rahmen der<br/>Änderung der Technik an einer<br/>Lokation in Bedingungen zu<br/>überführen|Fehler (30.09.2025)|






Seite 27 von 29

Version: 2.0f
11.12.2025

PRICAT Anwendungshandbuch

![edi@energy. Datenformate Strom & Gas](zbxk)

|Änd-ID|Ort|Änderungen<br/>Bisher|Änderungen<br/>Neu|Grund der Anpassung|Status|
|-|-|-|-|-|-|
||||\[937] Format: keine Nachkommastelle|||
|26910|SG17 PGI-SG36<br/>SG36 LIN-PIA-IMD-SG40<br/>SG40 Preisangabe<br/>RNG Angaben zum Wertebereich<br/>DE6152<br/>Anwendungsfall<br/>"Preisblätter MSB-Leistungen", dem der PID 27002 zugeordnet ist|M \[55] (\[512] (\[908] \[937]))<br/><br/>\[55] Wenn in dieser SG36 ein weiteres RNG (d. h. eine weitere Zone) vorhanden ist, in der der Wert des DE6162 (Wertebereichsgrenze, untere) größer ist als der Wert des DE6162 in diesem RNG<br/>\[512] Hinweis: Der genannte Wert gehört zum Intervall<br/>\[908] Format: Mögliche Werte: 1 bis n<br/>\[937] Format: keine Nachkommastelle|M ((\[34] \[55]) (\[57] \[67])) \[512] (\[908] \[937])<br/><br/>\[34] wenn BGM DE1001 = Z77 (Preisblatt Konfigurationen)<br/>\[55] Wenn in dieser SG36 ein weiteres RNG (d. h. eine weitere Zone) vorhanden ist, in der der Wert des DE6162 (Wertebereichsgrenze, untere) größer ist als der Wert des DE6162 in diesem RNG<br/>\[57] wenn BGM DE1001 = Z94 (Preisblatt Technik)<br/>\[67] wenn in dieser SG17 ein weiteres LIN vorhanden ist, in dem der Teil des Codes vor dem "-" des DE7140 mit dem des DE7140 des LIN dieser SG36 identisch ist und in dem der Wert nach dem "-" um eins größer ist, als der Wert nach dem "\_" im DE7140 des LIN dieser SG36<br/>\[512] Hinweis: Der genannte Wert gehört zum Intervall<br/>\[908] Format: Mögliche Werte: 1 bis n<br/>\[937] Format: keine Nachkommastelle|Anpassung, um die Unterschiede der Preisgestaltungsmöglichkeiten im Rahmen der Konfigurationsprodukten von denen im Rahmen der Änderung der Technik an einer Lokation in Bedingungen zu überführen|Fehler (30.09.2025)|
|26967|SG17<br/>Netzbetreiberindividuelle Artikel-ID<br/>SG36 Positionsdaten<br/>SG40 Preisangabe<br/>RNG<br/>Zonenintervallgrenzen<br/>DE6152<br/><br/>Anwendungsfall<br/>"Preisblätter NB-Leistungen", dem der PID 27003 zugeordnet ist|X (\[926] \[28] \[908] \[29]) \[511]<br/><br/>\[28] Wenn die zugehörige Artikel-ID in der letzten Stelle eine 1 ist<br/>\[29] Wenn die zugehörige Artikel-ID in der letzten Stelle > 1 ist<br/>\[511] Hinweis: 1. Der genannte Wert gehört nicht zum Intervall.<br/>2. Wenn in dieser SG36 die letzte Ziffer von LIN DE7140 >1, dann ist der Wert identisch mit dem Wert des DE6152 im RNG-Segment, in der SG36, in der die letzte Ziffer von LIN DE7140 um 1 kleiner ist, als die letzte Ziffer von LIN DE7140 in dieser SG36.<br/>3. Die untere Wertegrenze zu der Artikel-ID, deren Zahl an der letzten Stelle den Wert n hat,|X (\[926] \[28] \[908] \[29]) \[72] \[511]<br/><br/>\[28] Wenn die zugehörige Artikel-ID in der letzten Stelle eine 1 ist<br/>\[29] Wenn die zugehörige Artikel-ID in der letzten Stelle > 1 ist<br/>\[72] Wenn in dieser SG36 die letzte Ziffer von LIN DE7140 >1 ist, dann muss es eine SG36 geben, dessen Inhalt von LIN DE7140 sich von dem in dieser SG36 nur in der letzten Ziffer unterscheidet und in der der Wert von RNG DE6152 mit dem Wert dieses DE6162 übereinstimmt.<br/>\[511] Hinweis:<br/>1. Der genannte Wert gehört nicht zum Intervall.<br/>2. Die untere Wertegrenze zu der Artikel-ID,|Zonenintervallgrenzen zur selben Gruppenartikel-ID bilden zusammen Zonen|Fehler (11.12.2025)|






Seite 28 von 29

Version: 2.0f
11.12.2025

PRICAT Anwendungshandbuch

![edi@energy logo](vwdy)

|Änd-ID|Ort|Änderungen<br/>Bisher|Änderungen<br/>Neu|Grund der Anpassung|Status|
|-|-|-|-|-|-|
|||muss kleiner sein, als die untere Wertegrenze zu der Artikel-ID, deren Zahl an der letzten Stelle den Wert n+1 hat.<br/>\[908] Format: Mögliche Werte: 1 bis n<br/>\[926] Format: Möglicher Wert: 0|deren Zahl an der letzten Stelle den Wert n hat, muss kleiner sein, als die untere Wertegrenze zu der Artikel-ID, deren Zahl an der letzten Stelle den Wert n+1 hat.<br/>\[908] Format: Mögliche Werte: 1 bis n<br/>\[926] Format: Möglicher Wert: 0|||
|26966|SG17<br/>Netzbetreiberindivid<br/>uelle Artikel-ID<br/>SG36 Positionsdaten<br/>SG40 Preisangabe<br/>RNG<br/>Zonenintervallgrenze<br/>n<br/>DE6152<br/><br/>Anwendungsfall<br/>"Preisblätter NB-<br/>Leistungen", dem der<br/>PID 27003<br/>zugeordnet ist|S \[10] ∧ \[512]<br/><br/>\[10] Wenn in dieser SG36 ein weiteres RNG (d. h.<br/>für diese Gruppenartikel-ID eine weitere Zone)<br/>vorhanden ist, in der der Wert des DE6162<br/>(Wertebereichsgrenze, untere) größer ist als der<br/>Wert des DE6162 in diesem RNG<br/>\[512] Hinweis: Der genannte Wert gehört zum<br/>Intervall|S \[10] ∧ \[512]<br/><br/>\[10] Wenn eine weitere SG36 vorhanden ist, bei<br/>der sich der Inhalt von LIN DE7140 von LIN<br/>DE7140 dieser SG36 nur in der Ziffer nach dem<br/>letzten "-" unterscheidet und die Ziffer dort<br/>größer ist als in dieser SG36 (also eine Artikel-ID<br/>zur selben Gruppenartikel-ID vorhanden ist)<br/>\[512] Hinweis: Der genannte Wert gehört zum<br/>Intervall|Das RNG<br/>Zonenintervallgrenzen ist nicht<br/>wiederholbar.<br/>Zusätzlich erfolgte eine<br/>Präzisierung der Bedingung.|Fehler (11.12.2025)|






Seite 29 von 29

Version: 2.0f
11.12.2025