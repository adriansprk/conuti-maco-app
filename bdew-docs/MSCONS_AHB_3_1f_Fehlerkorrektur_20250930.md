![edi@energy. Datenformate Strom & Gas](image)

# <mark><font color="#C00000">Konsolidierte Lesefassung mit Fehlerkorrekturen</font></mark>

# <mark><font color="#C00000">Stand: 30.09.2025</font></mark>

# <mark><font color="#C00000">MSCONS Anwendungshandbuch</font></mark>

**Version:** 3.1f

**Stand MIG:** MSCONS 2.4c

**Ursprüngliches Publikationsdatum:** 01.10.2024

**Autor:** BDEW

MSCONS Anwendungshandbuch
![edi@energy. Datenformate Strom & Gas](image)

# Disclaimer

Die PDF-Datei ist das allein gültige Dokument.

Die zusätzlich veröffentlichte Word-Datei dient als informatorische Lesefassung und entspricht inhaltlich der PDF-Datei. Diese Word-Datei wird bis auf Weiteres rein informatorisch und ergänzend veröffentlicht unter dem Vorbehalt, zukünftig eine kostenpflichtige Veröffentlichung der Word-Datei einzuführen.

Zusätzlich werden zur PDF-Datei auch XML-Dateien als optionale Unterstützung gegen Entgelt veröffentlicht.

Version: 3.1f 30.09.2025 Seite 2 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

# Inhaltsverzeichnis

**1 Anwendungsbeschreibung** 7

**2 Ausprägungen von MSCONS-Nachrichten** 7

**3 Übersicht der Pakete in der MSCONS** 8

**4 Zeitumschaltung bei Lastgangübertragung** 8
4.1 Sommer / Winter 8
4.1.1 Sparte Strom 8
4.1.2 Sparte Gas 8
4.2 Winter / Sommer 9
4.2.1 Sparte Strom 9
4.2.2 Sparte Gas 9
4.3 Übersicht gesetzliche deutsche Zeit mit Zeitumschaltung 10
4.3.1 Sparte Strom 10
4.3.2 Sparte Gas 11

**5 Versionierung von Zeitreihen und Listen in der MSCONS** 14
5.1 Versionierung von Zeitreihen 14
5.2 Versionierung von Listen 15

**6 Zählerstände und Energiemengen** 16
6.1 Generelles zur Übertragung von Zählerständen 16
6.2 Generelles zur Übertragung von Energiemengen 18
6.3 Übertragung von Zählerständen und Energiemengen Strom 19
6.3.1 Übertragung von Zählerständen Strom 19
6.3.2 Übertragung von Energiemengen Strom 19
6.3.3 Übertragung von Energiemenge und Leistungsmaximum Strom 21
6.3.4 Übertragung Bewegungsdaten im Kalenderjahr vor Lieferbeginn (Strom) 22
6.3.5 Übertragung Energiemengen als Grundlage zur POG-Ermittlung 23
6.3.6 Anwendungsübersicht Zählerstand Strom 24
6.3.7 Anwendungsübersicht Energiemengen Strom 32
6.3.8 Anwendungsübersicht Grundlage POG-Ermittlung 45
6.4 Übertragung von Zählerständen und Energiemengen Gas 48

Version: 3.1f 30.09.2025 Seite 3 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

6.4.1 Übertragung von Zählerständen Gas 48
6.4.2 Übertragung von Energiemengen Gas 48
6.4.3 Anwendungsübersicht Zählerstand und Energiemengen Gas 50

# 7 Lastgänge 62
## 7.1 Generelles zur Übertragung von Lastgängen 62
## 7.2 Lastgang Strom 62
### 7.2.1 Übertragung von Lastgängen Strom 62
### 7.2.2 Anwendungsübersicht Lastgang Strom 66
## 7.3 Lastgang Gas 74
### 7.3.1 Übertragung von Lastgängen Gas 74
### 7.3.2 Anwendungsübersicht Lastgang Gas 75

# 8 Übertragung im Rahmen MaBiS / Redispatch 2.0 82
## 8.1 Normiertes Profil / Profilschar / Vergangenheitswerte TEP mit Referenzmessung 82
### 8.1.1 Übertragung normiertes Profil 82
### 8.1.2 Übertragung Profilschar 82
### 8.1.3 Übertragung Vergangenheitswerte TEP mit Referenzmessung 82
### 8.1.4 Anwendungsübersicht Profil / Profilschar / Vergh. Werte TEP mit Referenzm. 84
## 8.2 Darstellung verwendete Codes zu Summenzeitreihen 88
## 8.3 Summenzeitreihen und Ausfallarbeitssummen 90
### 8.3.1 Übertragung Summenzeitreihe 90
### 8.3.2 Übertragung Ausfallarbeitssummen 91
### 8.3.3 Anwendungsübersicht Summenzeitreihe und Ausfallarbeitssummen 92
## 8.4 Überführungszeitreihen 96
### 8.4.1 Übertragung EEG-Überführungszeitreihen 96
### 8.4.2 Übertragung EEG-Überführungszeitreihe aufgrund von Ausfallarbeit 96
### 8.4.3 Übertragung Ausfallarbeitsüberführungszeitreihe 96
### 8.4.4 Anwendungsübersicht EEG-Überführungszeitreihen 98
### 8.4.5 Anwendungsübersicht Ausfallarbeitsüberführungszeitreihe 102
## 8.5 Lastgang im Rahmen Redispatch 2.0 106

Version: 3.1f 30.09.2025 Seite 4 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

8.5.1 Übermittlung Einzelzeitreihe Ausfallarbeit 106
8.5.2 Anwendungsübersicht Einzelzeitreihe Ausfallarbeit im Rahmen Redispatch 2.0 107
8.6 Meteorologische Daten im Rahmen MaBiS / Redispatch 2.0 111
8.6.1 Übermittlung meteorologischer Daten 111
8.6.2 Anwendungsübersicht meteorolog. Daten im Rahmen MaBiS / Redispatch 2.0 112

# 9 Gasbeschaffenheit 116
9.1 Übertragung Gasbeschaffenheitsdaten 116
9.2 Anwendungsübersicht Gasbeschaffenheitsdaten 117

# 10 Marktlokationsscharfe Allokationsliste Gas / marktlokationsscharfe bilanzierte Menge Strom/Gas 124
10.1 Übertragung marktlokationsscharfe Allokationsliste Gas 124
10.2 Übertragung marktlokationsscharfe bilanzierte Menge Strom/Gas 124
10.3 Anwendungsübersicht Allokationsliste Gas / bilanzierte Menge Strom/Gas 125

# 11 Werte nach Typ 2 130
11.1 Übermittlung Werte nach Typ 2 130
11.2 Anwendungsübersicht Werte nach Typ 2 131

# 12 Stornierung / Korrektur von Werten 135
12.1 Stornierung von Werten 135
12.2 Korrektur von Werten 135
12.3 Übersicht Korrekturvarianten von Werten je ursprünglichem Anwendungsfall 135
12.4 Anwendungsübersicht Stornierung 138

# 13 Übersicht Ereignisse für die Wertbereitstellung und Inhalte bei der Übertragung von Zählerständen 141
13.1 Ereignis aufgrund einer Bestellung 141
13.2 Ereignis aufgrund der Bereitstellung durch den MSB 144
13.3 Ereignis aufgrund einer Änderung der Konfiguration 145
13.4 Ereignis aufgrund eines Gerätewechsels 147
13.5 Ereignis aufgrund einer Geräteübernahme 149

Version: 3.1f 30.09.2025 Seite 5 von 158

MSCONS Anwendungshandbuch
![edi@energy. Datenformate Strom & Gas](image)

13.6 Bereitstellung Werte durch NB / LF an den MSB an der Marktlokation 151

13.7 Ereignis aufgrund einer erforderlichen Abgrenzung 152

# 14 Änderungshistorie 154

Version: 3.1f 30.09.2025 Seite 6 von 158

MSCONS Anwendungshandbuch
![edi@energy Datenformate Strom & Gas](image)

# 1 Anwendungsbeschreibung

EDIFACT-Nachrichten stellen den beteiligten Kommunikationspartnern ein Instrument zur Verfügung über einen normierten, einheitlichen Kommunikationsstandard den zur Abwicklung ihrer Geschäftsprozesse benötigten Informationsaustausch durchzuführen. Dabei treten in der Praxis eine Reihe von verschiedenen Anwendungsmöglichkeiten auf, die mit unterschiedlichen Ausprägungen eines Nachrichtentyps (z. B. Übertragung von Lastgängen oder Zählerständen) mit der EDIFACT-MSCONS Nachricht abgedeckt werden.

Die Anwendungsbeschreibungen zur Nachrichtenbeschreibung BDEW – UN/EDIFACT D.04B – MSCONS stellen neben den dort definierten allgemeinen semantischen und syntaktischen Festlegungen, die im deutschen Energiemarkt auftretenden Anwendungsfälle dar.

In diesem Dokument werden die einzelnen Anwendungsfälle prozessscharf dargestellt. Die Definitionen zur Tabellennotation sind den Allgemeinen Festlegungen zu entnehmen.

# 2 Ausprägungen von MSCONS-Nachrichten

Die Angaben zur Verwendung der einzelnen Segmente haben zum Zwecke des Datenaustausches im deutschen Energiemarkt verbindlichen Charakter.

Im deutschen Energiemarkt wird vorausgesetzt, dass der Prozessverantwortliche (Marktrolle) und der Absender der Nachricht identisch sind.

Der Absender/Prozessverantwortliche identifiziert sich im UNB-Segment über das DE0004 und über das SG2 NAD+MS.

Der Empfänger identifiziert sich im UNB-Segment über das DE0010 und über das SG2 NAD+MR. Die Identifikation wird auch so vorgenommen, falls die Versendung oder der Empfang der Nachricht von einem Dienstleister durchgeführt wird.

In allen Anwendungsfällen sind jeweils nur die OBIS-Kennzahlen/OBIS-ähnliche Kennzahlen/Medien zu verwenden, die in der EDI@Energy Codeliste der OBIS-Kennzahlen und Medien mit dem entsprechenden Prüfidentifikator versehen sind.

Bei Verwendung von UNB DE0026 = „VL“ ist bei der Übertragung von Zählerständen und Leistungswerten für Wandlermessung bei kME ohne RLM, mME und iMS der Wandlerfaktor nicht zu berücksichtigen.

Basis für Bereitstellung der Werte durch den MSB in der Sparte Strom (z. B Auslöser, Kategorie, Art und Umfang der zu übermittelnden Werte, Intervall, Fristen) sind in der WiM Teil 2 – Fokus Übermittlung von Werten, Kapitel 2.5.5. Darstellung der zu übermittelnden Werte in der jeweils gültigen Fassung beschrieben.

Basis für die Netznutzungsabrechnung von Marktlokationen, deren Energie über Zählerstands-mitteilungen auf Ebene der Messlokation ermittelt wird, ist die Energiemenge, die in dem MSCONS-Anwendungsfall Energiemenge (Strom) bzw. Energiemenge u. Leistungsmaximum (Strom) unter Angabe der ID der Marktlokation für den Zeitraum der Netznutzungsabrechnung übermittelt wurde.

Version: 3.1f 30.09.2025 Seite 7 von 158

MSCONS Anwendungshandbuch
![edi@energy Logo](image)

# 3 Übersicht der Pakete in der MSCONS

|Paket|Paketvoraussetzung(en)|Bedingungen|
|-|-|-|
|\[1P]|--|Hinweis: Das ist das Standardpaket, wenn keine Bedingung zum Tragen kommt, z. B. im COM-Segment|
|\[2P]|\[492]|\[492] Wenn MP-ID in NAD+MR (Nachrichtenempfänger) aus Sparte Strom|
|\[3P]|\[493]|\[493] Wenn MP-ID in NAD+MR (Nachrichtenempfänger) aus Sparte Gas|
|\[4P]|\[92]|\[92] Wenn SG10 QTY DE6063 mit Wert 67 vorhanden|
|\[5P]|\[93]|\[93] Wenn SG10 QTY DE6063 mit Wert 220 vorhanden|
|\[6P]|\[94]|\[94] Wenn SG10 QTY DE6063 mit Wert 201 vorhanden|
|\[7P]|\[95]|\[95] Wenn SG10 QTY DE6063 mit Wert 20 vorhanden|
|\[8P]|\[96]|\[96] Wenn SG10 QTY DE6063 mit Wert Z18 vorhanden|


# 4 Zeitumschaltung bei Lastgangübertragung

## 4.1 Sommer / Winter

### 4.1.1 Sparte Strom

Übertragen wird der Lastgang für den 25.10.2020 (gesetzliche deutsche Zeit), d. h. an einem Tag mit Sommer/Winter-Zeitumschaltung. Das bedeutet, an diesem Tag sind in der Sparte Strom 100 1/4h-Werte zu übertragen. In der nachfolgenden Tabelle werden nur die Segmente der SG6 aufgeführt, die bei der Zeitumstellung von Bedeutung sind.

|...|...|...|...|||
|-|-|-|-|-|-|
|SG6|Enthält das Zeitintervall des Übertragungszeitraums des Lastgang Strom (hier: 1 Tag gesetzl. deutsche Zeit)|||||
||DTM|Beginn Messperiode<br/>Übertragungszeitraum|DTM+163:202010242200?+00:303'|von 24.10.2020 22:00 UTC|entspricht: 25.10.2020 00:00 gesetzl. deutscher Zeit MESZ|
||DTM|Ende Messperiode<br/>Übertragungszeitraum|DTM+164:202010252300?+00:303'|bis 25.10.2020 23:00 UTC|entspricht: 26.10.2020 00:00 gesetzl. deutscher Zeit MEZ|


In der SG10 Mengen- und Statusangaben ist für das oben aufgeführte Zeitintervall zu jeder 1/4h ein Wert zu übertragen, wobei die Zeitangaben der DTM-Segmente in dieser Segmentgruppe innerhalb des Zeitintervalls liegen müssen, die sich durch das in SG6 angegebene Zeitintervall ergeben, wobei auch die beiden Intervallgrenzen in diesen DTM-Segmente genutzt werden. Dies ergibt 100 1/4h-Werte.

### 4.1.2 Sparte Gas

Übertragen wird der Lastgang für den Gastag 24.10.2020 06:00 Uhr - 25.10.2020 06:00 Uhr (gesetzlicher deutscher Zeit), d. h. an einem Tag mit Sommer/Winter-Zeitumschaltung. Das

Version: 3.1f 30.09.2025 Seite 8 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

bedeutet, an diesem Tag sind in der Sparte Gas 25 Stunden-Werte zu übertragen. In der nachfolgenden Tabelle werden nur die Segmente der SG6 aufgeführt, die bei der Zeitumstellung von Bedeutung sind.

|...|...|...|...|||
|-|-|-|-|-|-|
|SG6|Enthält das Zeitintervall des Übertragungszeitraums des Lastgang Gas (hier: 1 Tag des Gastages)|||||
||DTM|Beginn Messperiode<br/>Übertragungszeitraum|DTM+163:202010240400?+00:303'|von 24.10.2020<br/>04:00 UTC|entspricht: 24.10.2020<br/>06:00 gesetzl. deutscher<br/>Zeit MESZ|
||DTM|Ende Messperiode<br/>Übertragungszeitraum|DTM+164:202010250500?+00:303'|bis 25.10.2020<br/>05:00 UTC|entspricht: 25.10.2020<br/>06:00 gesetzl. deutscher<br/>Zeit MEZ|


In der SG10 Mengen- und Statusangaben ist für das oben aufgeführte Zeitintervall zu jeder Stunde ein Wert zu übertragen, wobei die Zeitangaben der DTM-Segmente in dieser Segmentgruppe innerhalb des Zeitintervalls liegen müssen, die sich durch das in SG6 angegebene Zeitintervall ergeben, wobei auch die beiden Intervallgrenzen in diesen DTM-Segmente genutzt werden. Dies ergibt 25 Stunden-Werte.

## 4.2 Winter / Sommer

### 4.2.1 Sparte Strom

Übertragen wird der Lastgang für den 28.03.2021 (gesetzliche deutsche Zeit), d. h. an einem Tag mit Winter/Sommer-Zeitumschaltung. Das bedeutet, an diesem Tag sind in der Sparte Strom 92 1/4h-Werte zu übertragen. In der nachfolgenden Tabelle werden nur die Segmente der SG6 aufgeführt, die bei der Zeitumstellung von Bedeutung sind.

|...|...|...|...|||
|-|-|-|-|-|-|
|SG6|Enthält das Zeitintervall des Übertragungszeitraums des Lastgang Strom (hier: 1 Tag gesetzl. deutsche Zeit)|||||
||DTM|Beginn Messperiode<br/>Übertragungszeitraum|DTM+163:202103272300?+00:303'|von 27.03.2021<br/>23:00 UTC|entspricht: 28.03.2021<br/>00:00 gesetzl. deutscher<br/>Zeit MEZ|
||DTM|Ende Messperiode<br/>Übertragungszeitraum|DTM+164:202103282200?+00:303'|bis 28.03.2021<br/>22:00 UTC|entspricht: 29.03.2021<br/>00:00 gesetzl. deutscher<br/>Zeit MESZ|


In der SG10 Mengen- und Statusangaben ist für das oben aufgeführte Zeitintervall zu jeder 1/4h ein Wert zu übertragen, wobei die Zeitangaben der DTM-Segmente in dieser Segmentgruppe innerhalb des Zeitintervalls liegen müssen, die sich durch das in SG6 angegebene Zeitintervall ergeben, wobei auch die beiden Intervallgrenzen in diesen DTM-Segmente genutzt werden. Dies ergibt 92 1/4h-Werte.

### 4.2.2 Sparte Gas

Übertragen wird der Lastgang für den Gastag 27.03.2021 06:00 Uhr - 28.03.2021 06:00 Uhr (gesetzlicher deutscher Zeit), d. h. an einem Tag mit Winter/Sommer-Zeitumschaltung. Das bedeutet, an diesem Tag sind in der Sparte Gas 23 Stunden-Werte zu übertragen. In der nachfolgenden Tabelle werden nur die Segmente der SG6 aufgeführt, die bei der Zeitumstellung von Bedeutung sind.

|...|...|...|...|||
|-|-|-|-|-|-|
|SG6|Enthält das Zeitintervall des Übertragungszeitraums des Lastgang Gas (hier: 1 Tag des Gastages)|||||
||DTM|Beginn Messperiode<br/>Übertragungszeitraum|DTM+163:202103270500?+00:303'|von 27.03.2021<br/>05:00 UTC|entspricht: 27.03.2021<br/>06:00 gesetzl. deutscher<br/>Zeit MEZ|


Version: 3.1f 30.09.2025 Seite 9 von 158

MSCONS Anwendungshandbuch
![edi@energy. Datenformate Strom & Gas](image)

**DTM** Ende Messperiode Übertragungszeitraum DTM+164:202103280400?+00:303' bis 28.03.2021 04:00 UTC entspricht: 28.03.2021 06:00 gesetzl. deutscher Zeit MESZ

In der SG10 Mengen- und Statusangaben ist für das oben aufgeführte Zeitintervall zu jeder Stunde ein Wert zu übertragen, wobei die Zeitangaben der DTM-Segmente in dieser Segmentgruppe innerhalb des Zeitintervalls liegen müssen, die sich durch das in SG6 angegebene Zeitintervall ergeben, wobei auch die beiden Intervallgrenzen in diesen DTM-Segmente genutzt werden. Dies ergibt 23 Stunden-Werte.

## 4.3 Übersicht gesetzliche deutsche Zeit mit Zeitumschaltung

Enthält eine Nachricht Werte zu einem Zeitintervall (Kalendertag oder Gastag oder Bilanzierungsmonat) der einen der Zeiträume aus den unten aufgeführten Tabellen zur Zeitumschaltung umfasst, ist für den entsprechenden Tag (Kalendertag oder Gastag) die angegebene Anzahl an Werten erlaubt.

### 4.3.1 Sparte Strom

Übersicht der Kalendertage mit Winter/Sommer-Zeitumschaltung an denen 92 1/4h-Werte zu übertragen sind:

|Kalendertag von(gesetzlich deutsche Zeit)|Kalendertag bis(gesetzlich deutsche Zeit)|Zeitintervall Übertragungs-zeitraum von:|Zeitintervall Übertragungs-zeitraum bis:|
|-|-|-|-|
|26.03.2000 00:00|27.03.2000 00:00|25.03.2000 23:00 UTC|26.03.2000 22:00 UTC|
|25.03.2001 00:00|26.03.2001 00:00|24.03.2001 23:00 UTC|25.03.2001 22:00 UTC|
|31.03.2002 00:00|01.04.2002 00:00|30.03.2002 23:00 UTC|31.03.2002 22:00 UTC|
|30.03.2003 00:00|31.03.2003 00:00|29.03.2003 23:00 UTC|30.03.2003 22:00 UTC|
|28.03.2004 00:00|29.03.2004 00:00|27.03.2004 23:00 UTC|28.03.2004 22:00 UTC|
|27.03.2005 00:00|28.03.2005 00:00|26.03.2005 23:00 UTC|27.03.2005 22:00 UTC|
|26.03.2006 00:00|27.03.2006 00:00|25.03.2006 23:00 UTC|26.03.2006 22:00 UTC|
|25.03.2007 00:00|26.03.2007 00:00|24.03.2007 23:00 UTC|25.03.2007 22:00 UTC|
|30.03.2008 00:00|31.03.2008 00:00|29.03.2008 23:00 UTC|30.03.2008 22:00 UTC|
|29.03.2009 00:00|30.03.2009 00:00|28.03.2009 23:00 UTC|29.03.2009 22:00 UTC|
|28.03.2010 00:00|29.03.2010 00:00|27.03.2010 23:00 UTC|28.03.2010 22:00 UTC|
|27.03.2011 00:00|28.03.2011 00:00|26.03.2011 23:00 UTC|27.03.2011 22:00 UTC|
|25.03.2012 00:00|26.03.2012 00:00|24.03.2012 23:00 UTC|25.03.2012 22:00 UTC|
|31.03.2013 00:00|01.04.2013 00:00|30.03.2013 23:00 UTC|31.03.2013 22:00 UTC|
|30.03.2014 00:00|31.03.2014 00:00|29.03.2014 23:00 UTC|30.03.2014 22:00 UTC|
|29.03.2015 00:00|30.03.2015 00:00|28.03.2015 23:00 UTC|29.03.2015 22:00 UTC|
|27.03.2016 00:00|28.03.2016 00:00|26.03.2016 23:00 UTC|27.03.2016 22:00 UTC|
|26.03.2017 00:00|27.03.2017 00:00|25.03.2017 23:00 UTC|26.03.2017 22:00 UTC|
|25.03.2018 00:00|26.03.2018 00:00|24.03.2018 23:00 UTC|25.03.2018 22:00 UTC|
|31.03.2019 00:00|01.04.2019 00:00|30.03.2019 23:00 UTC|31.03.2019 22:00 UTC|
|29.03.2020 00:00|30.03.2020 00:00|28.03.2020 23:00 UTC|29.03.2020 22:00 UTC|
|28.03.2021 00:00|29.03.2021 00:00|27.03.2021 23:00 UTC|28.03.2021 22:00 UTC|
|27.03.2022 00:00|28.03.2022 00:00|26.03.2022 23:00 UTC|27.03.2022 22:00 UTC|
|26.03.2023 00:00|27.03.2023 00:00|25.03.2023 23:00 UTC|26.03.2023 22:00 UTC|
|31.03.2024 00:00|01.04.2024 00:00|30.03.2024 23:00 UTC|31.03.2024 22:00 UTC|
|30.03.2025 00:00|31.03.2025 00:00|29.03.2025 23:00 UTC|30.03.2025 22:00 UTC|
|29.03.2026 00:00|30.03.2026 00:00|28.03.2026 23:00 UTC|29.03.2026 22:00 UTC|
|28.03.2027 00:00|29.03.2027 00:00|27.03.2027 23:00 UTC|28.03.2027 22:00 UTC|
|26.03.2028 00:00|27.03.2028 00:00|25.03.2028 23:00 UTC|26.03.2028 22:00 UTC|
|25.03.2029 00:00|26.03.2029 00:00|24.03.2029 23:00 UTC|25.03.2029 22:00 UTC|
|31.03.2030 00:00|01.04.2030 00:00|30.03.2030 23:00 UTC|31.03.2030 22:00 UTC|


Version: 3.1f 30.09.2025 Seite 10 von 158

MSCONS Anwendungshandbuch
![edi@energy. Datenformate Strom & Gas](image)

|Kalendertag von(gesetzlich deutsche Zeit)|Kalendertag bis(gesetzlich deutsche Zeit)|Zeitintervall Übertragungs-zeitraum von:|Zeitintervall Übertragungs-zeitraum bis:|
|-|-|-|-|
|30.03.2031 00:00|31.03.2031 00:00|29.03.2031 23:00 UTC|30.03.2031 22:00 UTC|
|28.03.2032 00:00|29.03.2032 00:00|27.03.2032 23:00 UTC|28.03.2032 22:00 UTC|


### Übersicht der Kalendertage mit Sommer/Winter-Zeitumschaltung an denen 100 1/4h-Werte zu übertragen sind:

|Kalendertag von(gesetzlich deutsche Zeit)|Kalendertag bis(gesetzlich deutsche Zeit)|Zeitintervall Übertragungs-zeitraum von:|Zeitintervall Übertragungs-zeitraum bis:|
|-|-|-|-|
|29.10.2000 00:00|30.10.2000 00:00|28.10.2000 22:00 UTC|29.10.2000 23:00 UTC|
|28.10.2001 00:00|29.10.2001 00:00|27.10.2001 22:00 UTC|28.10.2001 23:00 UTC|
|27.10.2002 00:00|28.10.2002 00:00|26.10.2002 22:00 UTC|27.10.2002 23:00 UTC|
|26.10.2003 00:00|27.10.2003 00:00|25.10.2003 22:00 UTC|26.10.2003 23:00 UTC|
|31.10.2004 00:00|01.11.2004 00:00|30.10.2004 22:00 UTC|31.10.2004 23:00 UTC|
|30.10.2005 00:00|31.10.2005 00:00|29.10.2005 22:00 UTC|30.10.2005 23:00 UTC|
|29.10.2006 00:00|30.10.2006 00:00|28.10.2006 22:00 UTC|29.10.2006 23:00 UTC|
|28.10.2007 00:00|29.10.2007 00:00|27.10.2007 22:00 UTC|28.10.2007 23:00 UTC|
|26.10.2008 00:00|27.10.2008 00:00|25.10.2008 22:00 UTC|26.10.2008 23:00 UTC|
|25.10.2009 00:00|26.10.2009 00:00|24.10.2009 22:00 UTC|25.10.2009 23:00 UTC|
|31.10.2010 00:00|01.11.2010 00:00|30.10.2010 22:00 UTC|31.10.2010 23:00 UTC|
|30.10.2011 00:00|31.10.2011 00:00|29.10.2011 22:00 UTC|30.10.2011 23:00 UTC|
|28.10.2012 00:00|29.10.2012 00:00|27.10.2012 22:00 UTC|28.10.2012 23:00 UTC|
|27.10.2013 00:00|28.10.2013 00:00|26.10.2013 22:00 UTC|27.10.2013 23:00 UTC|
|26.10.2014 00:00|27.10.2014 00:00|25.10.2014 22:00 UTC|26.10.2014 23:00 UTC|
|25.10.2015 00:00|26.10.2015 00:00|24.10.2015 22:00 UTC|25.10.2015 23:00 UTC|
|30.10.2016 00:00|31.10.2016 00:00|29.10.2016 22:00 UTC|30.10.2016 23:00 UTC|
|29.10.2017 00:00|30.10.2017 00:00|28.10.2017 22:00 UTC|29.10.2017 23:00 UTC|
|28.10.2018 00:00|29.10.2018 00:00|27.10.2018 22:00 UTC|28.10.2018 23:00 UTC|
|27.10.2019 00:00|28.10.2019 00:00|26.10.2019 22:00 UTC|27.10.2019 23:00 UTC|
|25.10.2020 00:00|26.10.2020 00:00|24.10.2020 22:00 UTC|25.10.2020 23:00 UTC|
|31.10.2021 00:00|01.11.2021 00:00|30.10.2021 22:00 UTC|31.10.2021 23:00 UTC|
|30.10.2022 00:00|31.10.2022 00:00|29.10.2022 22:00 UTC|30.10.2022 23:00 UTC|
|29.10.2023 00:00|30.10.2023 00:00|28.10.2023 22:00 UTC|29.10.2023 23:00 UTC|
|27.10.2024 00:00|28.10.2024 00:00|26.10.2024 22:00 UTC|27.10.2024 23:00 UTC|
|26.10.2025 00:00|27.10.2025 00:00|25.10.2025 22:00 UTC|26.10.2025 23:00 UTC|
|25.10.2026 00:00|26.10.2026 00:00|24.10.2026 22:00 UTC|25.10.2026 23:00 UTC|
|31.10.2027 00:00|01.11.2027 00:00|30.10.2027 22:00 UTC|31.10.2027 23:00 UTC|
|29.10.2028 00:00|30.11.2028 00:00|28.10.2028 22:00 UTC|29.10.2028 23:00 UTC|
|28.10.2029 00:00|29.10.2029 00:00|27.10.2029 22:00 UTC|28.10.2029 23:00 UTC|
|27.10.2030 00:00|28.10.2030 00:00|26.10.2030 22:00 UTC|27.10.2030 23:00 UTC|
|26.10.2031 00:00|27.10.2031 00:00|25.10.2031 22:00 UTC|26.10.2031 23:00 UTC|
|31.10.2032 00:00|01.11.2032 00:00|30.10.2032 22:00 UTC|31.10.2032 23:00 UTC|


## 4.3.2 Sparte Gas

### Übersicht der Gastage mit Winter/Sommer-Zeitumschaltung an denen 23 Stunden-Werte zu übertragen sind:

|Gastag von(gesetzlich deutsche Zeit)|Gastag bis(gesetzlich deutsche Zeit)|Zeitintervall Übertragungs-zeitraum von:|Zeitintervall Übertragungs-zeitraum bis:|
|-|-|-|-|
|25.03.2000 06:00|26.03.2000 06:00|25.03.2000 05:00 UTC|26.03.2000 04:00 UTC|
|24.03.2001 06:00|25.03.2001 06:00|24.03.2001 05:00 UTC|25.03.2001 04:00 UTC|


Version: 3.1f 30.09.2025 Seite 11 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|Gastag von(gesetzlich deutsche Zeit)|Gastag bis(gesetzlich deutsche Zeit)|Zeitintervall Übertragungs-zeitraum von:|Zeitintervall Übertragungs-zeitraum bis:|
|-|-|-|-|
|30.03.2002 06:00|31.03.2002 06:00|30.03.2002 05:00 UTC|31.03.2002 04:00 UTC|
|29.03.2003 06:00|30.03.2003 06:00|29.03.2003 05:00 UTC|30.03.2003 04:00 UTC|
|27.03.2004 06:00|28.03.2004 06:00|27.03.2004 05:00 UTC|28.03.2004 04:00 UTC|
|26.03.2005 06:00|27.03.2005 06:00|26.03.2005 05:00 UTC|27.03.2005 04:00 UTC|
|25.03.2006 06:00|26.03.2006 06:00|25.03.2006 05:00 UTC|26.03.2006 04:00 UTC|
|24.03.2007 06:00|25.03.2007 06:00|24.03.2007 05:00 UTC|25.03.2007 04:00 UTC|
|29.03.2008 06:00|30.03.2008 06:00|29.03.2008 05:00 UTC|30.03.2008 04:00 UTC|
|28.03.2009 06:00|29.03.2009 06:00|28.03.2009 05:00 UTC|29.03.2009 04:00 UTC|
|27.03.2010 06:00|28.03.2010 06:00|27.03.2010 05:00 UTC|28.03.2010 04:00 UTC|
|26.03.2011 06:00|27.03.2011 06:00|26.03.2011 05:00 UTC|27.03.2011 04:00 UTC|
|24.03.2012 06:00|25.03.2012 06:00|24.03.2012 05:00 UTC|25.03.2012 04:00 UTC|
|30.03.2013 06:00|31.03.2013 06:00|30.03.2013 05:00 UTC|31.03.2013 04:00 UTC|
|29.03.2014 06:00|30.03.2014 06:00|29.03.2014 05:00 UTC|30.03.2014 04:00 UTC|
|28.03.2015 06:00|29.03.2015 06:00|28.03.2015 05:00 UTC|29.03.2015 04:00 UTC|
|26.03.2016 06:00|27.03.2016 06:00|26.03.2016 05:00 UTC|27.03.2016 04:00 UTC|
|25.03.2017 06:00|26.03.2017 06:00|25.03.2017 05:00 UTC|26.03.2017 04:00 UTC|
|24.03.2018 06:00|25.03.2018 06:00|24.03.2018 05:00 UTC|25.03.2018 04:00 UTC|
|30.03.2019 06:00|31.03.2019 06:00|30.03.2019 05:00 UTC|31.03.2019 04:00 UTC|
|28.03.2020 06:00|29.03.2020 06:00|28.03.2020 05:00 UTC|29.03.2020 04:00 UTC|
|27.03.2021 06:00|28.03.2021 06:00|27.03.2021 05:00 UTC|28.03.2021 04:00 UTC|
|26.03.2022 06:00|27.03.2022 06:00|26.03.2022 05:00 UTC|27.03.2022 04:00 UTC|
|25.03.2023 06:00|26.03.2023 06:00|25.03.2023 05:00 UTC|26.03.2023 04:00 UTC|
|30.03.2024 06:00|31.03.2024 06:00|30.03.2024 05:00 UTC|31.03.2024 04:00 UTC|
|29.03.2025 06:00|30.03.2025 06:00|29.03.2025 05:00 UTC|30.03.2025 04:00 UTC|
|28.03.2026 06:00|29.03.2026 06:00|28.03.2026 05:00 UTC|29.03.2026 04:00 UTC|
|27.03.2027 06:00|28.03.2027 06:00|27.03.2027 05:00 UTC|28.03.2027 04:00 UTC|
|25.03.2028 06:00|26.03.2028 06:00|25.03.2028 05:00 UTC|26.03.2028 04:00 UTC|
|24.03.2029 06:00|25.03.2029 06:00|24.03.2029 05:00 UTC|25.03.2029 04:00 UTC|
|30.03.2030 06:00|31.03.2030 06:00|30.03.2030 05:00 UTC|31.03.2030 04:00 UTC|
|29.03.2031 06:00|30.03.2031 06:00|29.03.2031 05:00 UTC|30.03.2031 04:00 UTC|
|27.03.2032 06:00|28.03.2032 06:00|27.03.2032 05:00 UTC|28.03.2032 04:00 UTC|


Übersicht der Gastage mit Sommer/Winter-Zeitumschaltung an denen 25 Stunden-Werte zu übertragen sind:

|Gastag von(gesetzlich deutsche Zeit)|Gastag bis(gesetzlich deutsche Zeit)|Zeitintervall Übertragungs-zeitraum von:|Zeitintervall Übertragungs-zeitraum bis:|
|-|-|-|-|
|28.10.2000 06:00|29.10.2000 06:00|28.10.2000 04:00 UTC|29.10.2000 05:00 UTC|
|27.10.2001 06:00|28.10.2001 06:00|27.10.2001 04:00 UTC|28.10.2001 05:00 UTC|
|26.10.2002 06:00|27.10.2002 06:00|26.10.2002 04:00 UTC|27.10.2002 05:00 UTC|
|25.10.2003 06:00|26.10.2003 06:00|25.10.2003 04:00 UTC|26.10.2003 05:00 UTC|
|30.10.2004 06:00|31.10.2004 06:00|30.10.2004 04:00 UTC|31.10.2004 05:00 UTC|
|29.10.2005 06:00|30.10.2005 06:00|29.10.2005 04:00 UTC|30.10.2005 05:00 UTC|
|28.10.2006 06:00|29.10.2006 06:00|28.10.2006 04:00 UTC|29.10.2006 05:00 UTC|
|27.10.2007 06:00|28.10.2007 06:00|27.10.2007 04:00 UTC|28.10.2007 05:00 UTC|
|25.10.2008 06:00|26.10.2008 06:00|25.10.2008 04:00 UTC|26.10.2008 05:00 UTC|
|24.10.2009 06:00|25.10.2009 06:00|24.10.2009 04:00 UTC|25.10.2009 05:00 UTC|
|30.10.2010 06:00|31.10.2010 06:00|30.10.2010 04:00 UTC|31.10.2010 05:00 UTC|
|29.10.2011 06:00|30.10.2011 06:00|29.10.2011 04:00 UTC|30.10.2011 05:00 UTC|
|27.10.2012 06:00|28.10.2012 06:00|27.10.2012 04:00 UTC|28.10.2012 05:00 UTC|
|26.10.2013 06:00|27.10.2013 06:00|26.10.2013 04:00 UTC|27.10.2013 05:00 UTC|


Version: 3.1f 30.09.2025 Seite 12 von 158

MSCONS Anwendungshandbuch
![edi@energy. Datenformate Strom & Gas](image)

|Gastag von(gesetzlich deutsche Zeit)|Gastag bis(gesetzlich deutsche Zeit)|Zeitintervall Übertragungs-zeitraum von:|Zeitintervall Übertragungs-zeitraum bis:|
|-|-|-|-|
|25.10.2014 06:00|26.10.2014 06:00|25.10.2014 04:00 UTC|26.10.2014 05:00 UTC|
|24.10.2015 06:00|25.10.2015 06:00|24.10.2015 04:00 UTC|25.10.2015 05:00 UTC|
|29.10.2016 06:00|30.10.2016 06:00|29.10.2016 04:00 UTC|30.10.2016 05:00 UTC|
|28.10.2017 06:00|29.10.2017 06:00|28.10.2017 04:00 UTC|29.10.2017 05:00 UTC|
|27.10.2018 06:00|28.10.2018 06:00|27.10.2018 04:00 UTC|28.10.2018 05:00 UTC|
|26.10.2019 06:00|27.10.2019 06:00|26.10.2019 04:00 UTC|27.10.2019 05:00 UTC|
|24.10.2020 06:00|25.10.2020 06:00|24.10.2020 04:00 UTC|25.10.2020 05:00 UTC|
|30.10.2021 06:00|31.10.2021 06:00|30.10.2021 04:00 UTC|31.10.2021 05:00 UTC|
|29.10.2022 06:00|30.10.2022 06:00|29.10.2022 04:00 UTC|30.10.2022 05:00 UTC|
|28.10.2023 06:00|29.10.2023 06:00|28.10.2023 04:00 UTC|29.10.2023 05:00 UTC|
|26.10.2024 06:00|27.10.2024 06:00|26.10.2024 04:00 UTC|27.10.2024 05:00 UTC|
|25.10.2025 06:00|26.10.2025 06:00|25.10.2025 04:00 UTC|26.10.2025 05:00 UTC|
|24.10.2026 06:00|25.10.2026 06:00|24.10.2026 04:00 UTC|25.10.2026 05:00 UTC|
|30.10.2027 06:00|31.10.2027 06:00|30.10.2027 04:00 UTC|31.10.2027 05:00 UTC|
|28.10.2028 06:00|29.10.2028 06:00|28.10.2028 04:00 UTC|29.10.2028 05:00 UTC|
|27.10.2029 06:00|28.10.2029 06:00|27.10.2029 04:00 UTC|28.10.2029 05:00 UTC|
|26.10.2030 06:00|27.10.2030 06:00|26.10.2030 04:00 UTC|27.10.2030 05:00 UTC|
|25.10.2031 06:00|26.10.2031 06:00|25.10.2031 04:00 UTC|26.10.2031 05:00 UTC|
|30.10.2032 06:00|31.10.2032 06:00|30.10.2032 04:00 UTC|31.10.2032 05:00 UTC|


Version: 3.1f	30.09.2025	Seite 13 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

# 5 Versionierung von Zeitreihen und Listen in der MSCONS

## 5.1 Versionierung von Zeitreihen

Die folgende Tabelle beschreibt abschließend, in welchem Anwendungsfall eine Versionierung der Zeitreihe stattfindet und wie sich das Versions-Tupel zusammensetzt. Weiterhin sind in der Tabelle die Inhalte der jeweiligen Zeitreihe beschrieben.

Der Sender der Nachricht ist für die Versionierung verantwortlich.

Sollen Daten mehrerer Zeitbereiche (z. B. Monate), oder von mehreren Meldepunkten in einer Datei übertragen werden, ist die Wiederholung über das UNH-Segment vorzunehmen.

Übersicht der Versions-Tupel und Inhalte von Zeitreihen je Anwendungsfall:

|Anwendungsfall|Versions-Tupel der Zeitreihen|Inhalte der Liste||
|-|-|-|-|
|Summenzeitreihe<br/>(Prüfidentifikator 13003)|Zeitreihen im Rahmen der Bilanzkreisabrechnung<br/>SG6 LOC ID des MaBiS-ZP<br/>SG6 DTM Bilanzierungsmonat<br/>SG6 DTM Versionsangabe|Es ist zu jeder ¼-Stunde der gesetzlichen Zeit, des angegebenen Bilanzierungsmonats genau ein Wert inklusive zugehöriger Zeitangaben in SG10 anzugeben.||
||Tägliche Summenzeitreihen<br/>SG6 LOC ID des MaBiS-ZP<br/>DTM Nachrichtendatum<br/>SG10 DTM Beginn Messperiode<br/>SG10 DTM Ende Messperiode|Es ist zu jeder ¼-Stunde der gesetzlichen Zeit, des angegebenen Zeitintervalls genau ein Wert inklusive zugehöriger Zeitangaben in SG10 anzugeben. Das Zeitintervall aller Positionen in SG9 LIN muss lückenlos sein und genau ein Tag der gesetzlichen Zeit umfassen.||
||EEG-Überführungszeitreihen<br/>(Prüfidentifikator 13005)|SG6 LOC Bilanzkreis von<br/>SG6 LOC Bilanzkreis an<br/>SG6 LOC Bilanzierungsgebiet<br/>SG6 DTM Beginn Messperiode Übertragungszeitraum<br/>SG6 DTM Ende Messperiode Übertragungszeitraum<br/>SG8 CCI Zeitreihentyp<br/>SG6 DTM Versionsangabe|Es ist zu jeder ¼-Stunde der gesetzlichen Zeit, des angegebenen Zeitintervalls des Übertragungszeitraum genau ein Wert inklusive zugehöriger Zeitangaben in SG10 anzugeben.|
|Gasbeschaffenheit<br/>(Prüfidentifikator 13007)|SG6 LOC ID der Messlokation oder ID der Marktlokation<br/>SG6 DTM Beginn Messperiode Übertragungszeitraum<br/>SG6 DTM Ende Messperiode Übertragungszeitraum<br/>SG6 DTM Versionsangabe|Es ist zu jeder Stunde der gesetzlichen Zeit, des angegebenen Zeitintervalls des Übertragungszeitraum genau ein Wert inklusive zugehöriger Zeitangaben in SG10 anzugeben.||
|Lastgang Gas<br/>(Prüfidentifikator 13008)|SG6 LOC ID der Messlokation oder ID der Marktlokation oder ID des Netzkopplungspunktes<br/>SG6 DTM Beginn Messperiode Übertragungszeitraum<br/>SG6 DTM Ende Messperiode Übertragungszeitraum<br/>DTM Nachrichtendatum|Es ist zu jeder Stunde der gesetzlichen Zeit, des angegebenen Zeitintervalls des Übertragungszeitraum genau ein Wert inklusive zugehöriger Zeitangaben in SG10 anzugeben.||
|Normiertes Profil<br/>(Prüfidentifikator 13010)|wenn das Zeitintervall mindestens einen Monat umfasst:<br/>SG2 NAD MP-ID Absender<br/>SG6 LOC Profilbezeichnung<br/>SG6 DTM Versionsangabe<br/>SG10 DTM Beginn Messperiode<br/>SG10 DTM Ende Messperiode|Es ist zu jeder ¼-Stunde der gesetzlichen Zeit, des angegebenen Zeitintervalls genau ein Wert inklusive zugehöriger Zeitangaben in SG10 anzugeben. Das Zeitintervall aller Positionen in SG9 LIN muss lückenlos sein und mindestens einen Monat der gesetzlichen Zeit umfassen.||
||wenn das Zeitintervall nicht mindestens einen Monat umfasst:<br/>SG2 NAD MP-ID Absender<br/>SG6 LOC Profilbezeichnung<br/>SG10 DTM Beginn Messperiode<br/>SG10 DTM Ende Messperiode|Es ist zu jeder ¼-Stunde der gesetzlichen Zeit, des angegebenen Zeitintervalls genau ein Wert inklusive zugehöriger Zeitangaben in SG10 anzugeben. Das Zeitintervall aller Positionen in SG9 LIN muss lückenlos sein und.||
||Profilschar<br/>(Prüfidentifikator 13011)|SG2 NAD MP-ID Absender<br/>SG6 LOC Profilschar<br/>SG6 DTM Gültigkeit, Beginndatum Profilschar<br/>SG6 DTM Versionsangabe|Es wird für jede Temperaturmaßzahl (die in SG9 LIN DE1082 angegeben wird, gemäß Liste der Profildefinitionen) immer alle ¼-Std.-Werte der gesetzlichen Zeit angegeben. Die Viertelstundenwerte sind dabei immer in chronologisch aufsteigender Reihenfolge anzugeben.|
||wenn das Zeitintervall mindestens einen Monat umfasst:|Es ist zu jeder ¼-Stunde der gesetzlichen Zeit, des angegebenen Zeitintervalls genau ein Wert||


Version: 3.1f 30.09.2025 Seite 14 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|Anwendungsfall|Versions-Tupel der Zeitreihen|Inhalte der Liste|
|-|-|-|
|Vergangenheitswerte TEP mit Referenzmessung (Prüfidentifikator 13012)|SG2 NAD MP-ID Absender<br/>SG6 LOC Profilbezeichnung<br/>SG6 DTM Versionsangabe<br/>SG10 DTM Beginn Messperiode<br/>SG10 DTM Ende Messperiode|inklusive zugehöriger Zeitangaben in SG10 anzugeben. Das Zeitintervall aller Positionen in SG9 LIN muss lückenlos sein und mindestens einen Monat der gesetzlichen Zeit umfassen.|
||wenn das Zeitintervall nicht mindestens einen Monat umfasst:<br/>SG2 NAD MP-ID Absender<br/>SG6 LOC Profilbezeichnung<br/>SG10 DTM Beginn Messperiode<br/>SG10 DTM Ende Messperiode|Es ist zu jeder ¼-Stunde der gesetzlichen Zeit, des angegebenen Zeitintervalls genau ein Wert inklusive zugehöriger Zeitangaben in SG10 anzugeben. Das Zeitintervall aller Positionen in SG9 LIN muss lückenlos sein und.|
|Lastgang Messlokation, Netzkoppelpunkt, Netzlokation (Prüfidentifikator 13018)|SG6 LOC ID der Messlokation oder ID des Netzkoppelpunktes<br/>SG6 DTM Beginn Messperiode Übertragungszeitraum<br/>SG6 DTM Ende Messperiode Übertragungszeitraum<br/>DTM Nachrichtendatum|Es ist zu jeder ¼-Stunde der gesetzlichen Zeit, des angegebenen Zeitintervalls des Übertragungszeitraum genau ein Wert inklusive zugehöriger Zeitangaben in SG10 anzugeben.|
|Ausfallarbeitsüberführungs-zeitreihe (Prüfidentifikator 13020)|SG6 LOC ID des MABIS-ZP<br/>SG6 DTM Bilanzierungsmonat<br/>SG6 DTM Versionsangabe|Es ist zu jeder ¼-Stunde der gesetzlichen Zeit, des angegebenen Bilanzierungsmonats genau ein Wert inklusive zugehöriger Zeitangaben in SG10 anzugeben.|
||Tägliche Ausfallarbeitsüberführungszeitreihe<br/>SG6 LOC ID des MaBiS-ZP<br/>DTM Nachrichtendatum<br/>SG10 DTM Beginn Messperiode<br/>SG10 DTM Ende Messperiode|Es ist zu jeder ¼-Stunde der gesetzlichen Zeit, des angegebenen Zeitintervalls genau ein Wert inklusive zugehöriger Zeitangaben in SG10 anzugeben. Das Zeitintervall aller Positionen in SG9 LIN muss lückenlos sein und genau ein Tag der gesetzlichen Zeit umfassen.|
|Meteorologische Daten (Prüfidentifikator 13021)|SG6 LOC ID der Technischen Ressource<br/>SG6 DTM Beginn Messperiode Übertragungszeitraum<br/>SG6 DTM Ende Messperiode Übertragungszeitraum<br/>SG6 DTM Versionsangabe|Es ist zu jeder ¼-Stunde der gesetzlichen Zeit, des angegebenen Zeitintervalls des Übertragungszeitraum genau ein Wert inklusive zugehöriger Zeitangaben in SG10 anzugeben.|
|Redispatch 2.0 Einzelzeitreihe Ausfallarbeit (Prüfidentifikator 13022)|SG6 LOC ID der Technischen Ressource oder ID der Marktlokation<br/>SG6 DTM Beginn Messperiode Übertragungszeitraum<br/>SG6 DTM Ende Messperiode Übertragungszeitraum<br/>SG6 DTM Versionsangabe|Es ist zu jeder ¼-Stunde der gesetzlichen Zeit, des angegebenen Zeitintervalls des Übertragungszeitraum genau ein Wert inklusive zugehöriger Zeitangaben in SG10 anzugeben.|
|Redispatch 2.0 Ausfallarbeits-summenzeitreihe (Prüfidentifikator 13023)|SG6 LOC ID des MABIS-ZP<br/>SG6 DTM Bilanzierungsmonat<br/>SG6 DTM Versionsangabe|Es ist zu jeder ¼-Stunde der gesetzlichen Zeit, des angegebenen Bilanzierungsmonats genau ein Wert inklusive zugehöriger Zeitangaben in SG10 anzugeben.|
|Lastgang Marktlokation, Tranche (Prüfidentifikator 13025)|SG6 LOC ID der Marktlokation oder ID der Tranche<br/>SG6 DTM Beginn Messperiode Übertragungszeitraum<br/>SG6 DTM Ende Messperiode Übertragungszeitraum<br/>DTM Nachrichtendatum|Es ist zu jeder ¼-Stunde der gesetzlichen Zeit, des angegebenen Zeitintervalls des Übertragungszeitraum genau ein Wert inklusive zugehöriger Zeitangaben in SG10 anzugeben.|
|Redispatch EEG-Überführungs-zeitreihe aufgrund Ausfallarbeit (Prüfidentifikator 13026)|SG6 LOC Bilanzkreis von<br/>SG6 LOC Bilanzkreis an<br/>SG6 LOC Bilanzierungsgebiet<br/>SG6 DTM Beginn Messperiode Übertragungszeitraum<br/>SG6 DTM Ende Messperiode Übertragungszeitraum<br/>SG8 CCI Zeitreihentyp<br/>SG6 DTM Versionsangabe|Es ist zu jeder ¼-Stunde der gesetzlichen Zeit, des angegebenen Zeitintervalls des Übertragungszeitraum genau ein Wert inklusive zugehöriger Zeitangaben in SG10 anzugeben.|
|Werte nach Typ 2 (Prüfidentifikator 13027)|SG6 LOC ID des Meldepunktes<br/>DTM Nachrichtendatum<br/>SG10 DTM Beginn Messperiode<br/>SG10 DTM Ende Messperiode|Es ist zu jedem Zeitintervall der gesetzlichen Zeit des bestellten Messproduktes zu der ein Wert übermittelt werden muss die zugehörigen Zeitangaben in SG10 anzugeben.|


## 5.2 Versionierung von Listen

Die folgende Tabelle beschreibt abschließend, in welchem Anwendungsfall eine Versionierung der Liste stattfindet und wie sich das Versions-Tupel zusammensetzt. Weiterhin sind in der Tabelle die Inhalte der jeweiligen Liste beschrieben.

Der Sender der Nachricht ist für die Versionierung verantwortlich.

Version: 3.1f 30.09.2025 Seite 15 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

Sollen Daten mehrerer Zeitbereiche (z. B. Monate) in einer Datei übertragen werden, ist die Wiederholung über das UNH-Segment vorzunehmen. Sollen Daten von mehreren Meldepunkten in einer Datei übertragen werden, ist je Meldepunkt eine SG5 „Liefer-, bzw. Bezugsort“ zu verwenden, d. h. die SG5 ist entsprechend oft zu wiederholen. Eine Liste, auch wenn diese aufgrund Ihrer Größe in mehrere Listen aufgeteilt wurde, enthält immer dieselbe Versionierung.

Übersicht der Versions-Tupel und Inhalte von Listen je Anwendungsfall:

|Anwendungsfall|Versions-Tupel der Listen|Inhalte der Liste|
|-|-|-|
|Marktlokationsscharfe Allokationsliste Gas (MMMA) (Prüfidentifikator 13013)|SG6 LOC ID der Marktlokation<br/>SG6 DTM Bilanzierungsmonat<br/>SG1 DTM Versionsangabe marktlokationsscharfe Allokationsliste Gas (MMA)|Es ist zu jedem Tag der gesetzlichen Zeit, des angegebenen Bilanzierungsmonats genau ein Wert inklusive zugehöriger Zeitangaben in SG10 anzugeben.|


# 6 Zählerstände und Energiemengen

## 6.1 Generelles zur Übertragung von Zählerständen

In SG10 QTY DE6060 werden Zählerstände wie auf dem Messgerät vorhanden angegeben.

Bei den OBIS-Kennzahlen und der maximalen Anzahl an Vor- / Nachkommastellen sind ausschließlich diese zulässig, die im vorherigen Stammdatenaustausch mittels der UTILMD zu diesem Zeitpunkt kommuniziert wurden.

Der Nutzungszeitpunkt für Zählerstände wird verwendet, um einen Zählerstand eindeutig einem Prozesszeitpunkt zuzuordnen. Dieser Prozesszeitpunkt kann entweder ein Zeitpunkt einer Stammdatenänderung sein, bei:

* einem Gerätewechsel,
* einer Geräteparameteränderung,
* einem Geräteeinbau, oder
* einen Geräteausbau,

in der die Änderung vor dem Versand des Zählerstandes übermittelt wurde, oder die Bestellung eines Wertes per ORDERS aufgrund eines eingetretenen Ereignisses, wie:

* Lieferbeginn,
* Beginn der Ersatz-/Grundversorgung
* Lieferende/Abmeldeanfrage
* Zwischenablesung.

Der Nutzungszeitpunkt ist für den Zählerstand der Zeitpunkt, der für die weitere Verarbeitung relevant ist (z. B. Zuordnung bei Empfänger anhand der Zuordnungstupel).

Zu einem Nutzungszeitpunkt kann zu einem Zuordnungstupel immer nur ein Zählerstand vom MSB zugeordnet werden, auch wenn am Vortag und am Folgetag jeweils ein Zählerstand vorliegt.

Version: 3.1f 30.09.2025 Seite 16 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

Der Ausführungs- / Änderungszeitpunkt für Zählerstände wird verwendet, um einen Zählerstand eindeutig einer tatsächlichen Änderung zuzuordnen, z. B. bei einem Gerätewechsel, einer Geräteparameteränderung, einem Geräteeinbau oder Geräteausbau der tatsächliche Zeitpunkt, an dem die Änderung an der Messlokation durchgeführt wurde. Der Nutzungszeitpunkt ist für den Zählerstand der Zeitpunkt, der für die weitere Verarbeitung relevant ist (z. B. Zuordnung bei Empfänger anhand der Zuordnungstupel).

Das Ablesedatum (tages- oder zeitpunktgenau) kann ausschließlich für wahre Werte angegeben werden (z. B. Ablesedatum des Kunden auf der Ablesekarte oder Ablesezeitpunkt bei einer MDE-Ablesung). Liegt die Information zu welcher Uhrzeit der Zählerstand tatsächlich erfasst wurde nicht vor, ist im DE2379 des Segments SG10 DTM+9 (Ablesedatum) der Code 102 zu nutzen. In diesem Fall ist eine Anreicherung einer Uhrzeit (z. B. die pauschale Nutzung von 00:00 Uhr) und somit die Nutzung des Codes 303 im DE2379 nicht erlaubt. Liegt die Information zu welchem Zeitpunkt der Zählerstand erfasst wurde vor, muss der Code 303 im DE2379 des Segments SG10 DTM+9 (Ablesedatum) genutzt und der korrekte Zeitpunkt den Empfängern mitgeteilt werden. Übermittelt ein Berechtigter einen Zählerstand mit einem Ablesedatum ohne Uhrzeit (Code 102), darf das Ablesedatum vom Messwertverantwortlichen nicht verfälscht werden, indem eine Uhrzeit zum Ablesedatum hinzugefügt wird. In diesem Fall hat der Messwertverantwortliche in der Weiterleitung an die berechtigten den Zählerstand ebenfalls ohne eine Zeitangabe (Code 102) zu übermitteln.

Bei Zählerständen die aufgrund:

*   einer Bestellung eines Wertes (z.B. aufgrund Lieferantenwechsel), oder
*   des Erreichens des Turnuszeitpunktes oder
*   aufgrund einer Ablesung wegen Geräteübernahme

übermittelt werden ist, falls es sich:

*   in der Sparte Strom um einen Ersatzwert oder einen vorläufigen Wert handelt, bzw.
*   in der Sparte Gas um einen Ersatzwert, Vorschlagswert, vorläufigen Wert oder nicht verwendbaren Wert

handelt, nur der Nutzungszeitpunkt angegeben. Ein Ablesedatum wird nicht angegeben.

Bei Zählerständen die aufgrund:

*   einer Änderung der Parametrierung oder
*   eines Gerätewechsels

übermittelt werden ist unabhängig von der Qualität des Wertes (SG10 QTY DE6063) zusätzlich zum Nutzungszeitpunkt immer auch ein Ausführungs- /Änderungszeitpunkt anzugeben.

Es ist zu beachten, falls bereits eine Bestellung für einen Wert aufgrund eines Wechselereignisses (Bestellung mit ORDERS BGM+7, IMD+Z13, IMD+Z48 (Wechselereignis)) vorliegt, zwischen dem Nachrichtenzeitpunkt und dem Bestellzeitpunkt noch ein oder mehrere Turnuszeitpunkte liegen, diese Turnuswerte ebenfalls zu übermitteln sind.

Version: 3.1f 30.09.2025 Seite 17 von 158

MSCONS Anwendungshandbuch
![edi@energy. Datenformate Strom & Gas](image)

Sollen mehrere Zählerstände (z. B. HT/NT-Mengen) an einer Messlokation zum selben Nutzungszeitpunkt übertragen werden, ist die Wiederholung über SG9 LIN vorzunehmen.

Sollen Daten von mehreren Messlokationen oder verschiedenen Nutzungszeitpunkten oder mit unterschiedlichen Referenzdaten in einer Datei übertragen werden, ist die Wiederholung über das UNH-Segment vorzunehmen.

## 6.2 Generelles zur Übertragung von Energiemengen

Dient zur Übermittlung im Falle:

* Lieferschein vom NB für Marktlokationen mit Grundpreis/Arbeitspreis (Strom),
* Aufbereitung und Übermittlung von Werten durch den MSB (Strom),
* bei Einzelwerten (z. B. Zählerstandsdifferenz, Energiemenge kWh, Gasmenge m<sup>3</sup>, Brennwert und Z-Zahl ohne Zählerstand) für einen beliebigen Zeitraum.

Sowie der Übertragung von Korrekturenergiemengen zu Messlokationen (z. B. im Falle einer Differenz des Werts des Fehlerregisters aus dem zu übermittelnden Zählerstand und dem Wert des Fehlerregisters zum zuletzt übermittelten Zählerstand). In diesem Fall ist in SG1 RFF+AGI DE1154 die Referenz auf die MSCONS in der der Messwert vorab übermittelt wurde anzugeben.

Weiterhin zur Übertragung von Energiemengen zu Marktlokationen deren Zählerstände und ggf. Korrekturenergiemengen auf Ebene der Messlokation ausgetauscht wurden. Hier ist die Energiemenge für die Marktlokation in kWh als Messwert Energiemenge zu übertragen. Für eine Energiemenge in der Sparte Strom ist maximal die Anzahl an Nachkommastellen zulässig, die im Rahmen des Austausches der Zählerstände vorab kommuniziert werden. Eine Energiemenge in der Sparte Gas wird gemäß G685 auf ganze Kilowattstunden gerundet.

Dabei wird in SG10 DTM+163 (Beginn Messperiode) der Zeitpunkt als Beginn angegeben, zu dem die letzte Energiemenge übermittelt wurde, oder der Zeitpunkt, an dem die Zuordnung an der Marktlokation durch den Empfänger des Zählerstandes begonnen hat.

Für Energiemengen, gilt: In SG10 DTM+164 (Ende Messperiode) wird der Zeitpunkt als Ende angegeben, zu dem der letzte Messwert mit demselben Nutzungszeitpunkt übermittelt wurde. Für Energiemengen auf Ebene der Marktlokation die entstehen, wenn die letzte Messlokation, die der Marktlokation zugeordnet war, beendet wurde (Stilllegung der Messlokation), kann es ein Auseinanderfallen der Zeitpunkte geben, da die Marktlokation in die Zukunft beendet wird und die Messlokation zum Zeitpunkt der tatsächlichen Stilllegung. In diesem Szenario ist in SG10 DTM+164 (Ende Messperiode) der Zeitpunkt als Ende angegeben, zu dem die Marktlokation beendet (stillgelegt) wurde.

Sollen mehrere Werte (z. B. HT/NT-Mengen oder mehrere Zeitbereiche aufgrund von Ablesungen im Zeitraum (insbesondere im Gas)) an einem Meldepunkt übertragen werden, ist die Wiederholung über SG9 LIN vorzunehmen.

Sollen Daten von mehreren Meldepunkten in einer Datei übertragen werden, ist die Wiederholung über das UNH-Segment vorzunehmen.

Version: 3.1f 30.09.2025 Seite 18 von 158

MSCONS Anwendungshandbuch
![edi@energy Datenformate Strom & Gas](image)

## 6.3 Übertragung von Zählerständen und Energiemengen Strom

### 6.3.1 Übertragung von Zählerständen Strom

Tabellenspalte = Zählerstand (Strom) 13017

Dieser Anwendungsfall dient zur Übertragung von Zählerständen in der Sparte Strom.

Bei der Übermittlung von Werten sind ausschließlich die OBIS-Kennzahlen in der Produktidentifikation (SG9 PIA+5 DE7140) zulässig, die im vorherigen Stammdatenaustausch vom MSB übermittelt wurden.

Im Fall der Übermittlung von Werten, die aus einem SMGw stammen, ist die Konfigurations-ID<sup>1</sup> anzugeben, die ebenfalls im vorherigen Stammdatenaustausch vom MSB übermittelt wurde.

Kommunikationspartner, Identifikationsangabe und Art der Werte für diesen Anwendungsfall:

|Sparte|Kommunikation von|Art der Werte|Identifikationsangabe in SG6 LOC|Anmerkung|
|-|-|-|-|-|
|Strom|MSB an MSB|Zählerstand zum Ablesetermin Turnus, Lieferbeginn/Beginn der Ersatz-/Grundversorgung, Lieferende/Abmeldeanfrage, Zwischenablesung, Gerätewechsel, Geräteübernahme und Änderung der Parametrierung|ID der Messlokation (bei kME, mME), bei Werten aus dem iMS erfolgt keine Identifikationsangabe in SG6 LOC, sondern die Angabe der Konfigurations-ID in SG7 RFF+AGK.|--|
|Strom|MSB an NB|Zählerstand zum Ablesetermin Turnus, Lieferbeginn/Beginn der Ersatz-/Grundversorgung, Lieferende/Abmeldeanfrage, Zwischenablesung, Gerätewechsel, Geräteübernahme und Änderung der Parametrierung|ID der Messlokation (bei kME, mME), bei Werten aus dem iMS erfolgt keine Identifikationsangabe in SG6 LOC, sondern die Angabe der Konfigurations-ID in SG7 RFF+AGK.|--|
|Strom|MSB an LF|Zählerstand zum Ablesetermin Turnus, Lieferbeginn/Beginn der Ersatz-/Grundversorgung, Lieferende/Abmeldeanfrage, Zwischenablesung, Gerätewechsel, Geräteübernahme und Änderung der Parametrierung|ID der Messlokation (bei kME, mME), bei Werten aus dem iMS erfolgt keine Identifikationsangabe in SG6 LOC, sondern die Angabe der Konfigurations-ID in SG7 RFF+AGK.|--|
|Strom|NB an MSB|Zählerstand zum Ablesetermin|ID der Messlokation|nur bei kME ohne RLM, mME|
|Strom|LF an MSB|Zählerstand zum Ablesetermin|ID der Messlokation|nur bei kME ohne RLM, mME|
|Strom|NB an RB HKN-R|--|ID der Messlokation|--|


### 6.3.2 Übertragung von Energiemengen Strom

Tabellenspalte = Energiemenge (Strom) 13019

***

<sup>1</sup> Details zur Konfigurations-ID sind im EDI@Energy UTILMD AHB Strom, Kapitel 5 zu finden.

Version: 3.1f 30.09.2025 Seite 19 von 158

MSCONS Anwendungshandbuch
![edi@energy. Datenformate Strom & Gas](image)

Dieser Anwendungsfall dient zur Übertragung von Energiemengen im Falle:

*   Lieferschein vom NB für Marktlokationen mit Grundpreis/Arbeitspreis,
*   Aufbereitung und Übermittlung von Werten durch den MSB.

Bei der Übermittlung von Werten durch den MSB (Strom) an den Empfänger ist im BGM-Segment DE1001 der Qualifier 7 (Prozessdatenbericht) zu verwenden.

Bei der Übermittlung des Lieferscheines vom NB für Marktlokationen mit Grundpreis/Arbeitspreis (Strom) ist im BGM-Segment DE1001 der Qualifier Z41 (Lieferschein Grund-/Arbeitspreis) zu verwenden.

Kommunikationspartner, Identifikationsangabe und Art der Werte für diesen Anwendungsfall:

|Sparte|Kommunikation von|Art der Werte|Identifikationsangabe in SG6 LOC|Anmerkung|
|-|-|-|-|-|
|Strom|MSB an NB|Arbeitsmenge eines Zeitraumes zwischen zwei Messwerten wie Turnus, Lieferbeginn/Beginn der Ersatz-/Grundversorgung, Lieferende/Abmeldeanfrage, Zwischenablesung, Gerätewechsel, Geräteübernahme und Änderung der Parametrierung|ID der Marktlokation|--|
|Strom|MSB an LF|Arbeitsmenge eines Zeitraumes zwischen zwei Messwerten wie Turnus, Lieferbeginn/Beginn der Ersatz-/Grundversorgung, Lieferende/Abmeldeanfrage, Zwischenablesung, Gerätewechsel, Geräteübernahme und Änderung der Parametrierung|ID der Marktlokation|--|
|Strom|MSB an MSB|Korrekturenergiemenge|ID der Messlokation (bei kME, mME), bei Werten aus dem iMS erfolgt keine Identifikationsangabe in SG6 LOC, sondern die Angabe der Konfigurations-ID in SG7 RFF+AGK.|Korrekturenergiemengen im Zeitintervall zwischen zwei Messwerten für rechnerisch ermittelte Messwerte auf Ebene der Messlokation (z. B. bei Zählerdefekt).|
|Strom|MSB an NB|Korrekturenergiemenge|ID der Messlokation (bei kME, mME), bei Werten aus dem iMS erfolgt keine Identifikationsangabe in SG6 LOC, sondern die Angabe der Konfigurations-ID in SG7 RFF+AGK.|Korrekturenergiemengen im Zeitintervall zwischen zwei Messwerten für rechnerisch ermittelte Messwerte auf Ebene der Messlokation (z. B. bei Zählerdefekt).|
|Strom|MSB an LF|Korrekturenergiemenge|ID der Messlokation (bei kME, mME), bei Werten aus dem iMS erfolgt keine Identifikationsangabe in SG6 LOC, sondern die Angabe der Konfigurations-ID in SG7 RFF+AGK.|Korrekturenergiemengen im Zeitintervall zwischen zwei Messwerten für rechnerisch ermittelte Messwerte auf Ebene der Messlokation (z. B. bei Zählerdefekt).|
|Strom|NB an LF|Lieferschein für Marktlokationen mit Grundpreis/Arbeitspreis|ID der Marktlokation|Zur Übermittlung des Lieferscheins zur Netznutzungsabrechnung, wenn nach Grundpreis/Arbeitspreis abgerechnet wird.|
|Strom|NB an RB HKN-R|--|ID der Marktlokation|--|


Version: 3.1f 30.09.2025 Seite 20 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

### 6.3.3 Übertragung von Energiemenge und Leistungsmaximum Strom

Tabellenspalte = Energiemenge u. Leistungsmax. 13016

Dieser Anwendungsfall dient zur Übertragung von Energiemenge und Leistungsmaximum im Falle:

* Lieferschein vom NB für Marktlokationen mit Arbeits- / Leistungspreis (Strom),
* Aufbereitung und Übermittlung von Werten durch den MSB (Strom),
* Energiemenge und Leistungsmaximum.

Bei der Übermittlung des Lieferscheines vom NB für Marktlokationen mit Arbeits-/Leistungspreis (Strom) ist im BGM-Segment DE1001 der Qualifier Z42 (Lieferschein Arbeits- / Leistungspreis) zu verwenden. Bei allen anderen ist im BGM-Segment DE1001 der Qualifier Z28 (Energiemenge und Leistungsmaximum) zu verwenden.

Bei der Übermittlung der Energiemenge und Leistungsmaximum gemäß WiM wird die Arbeit mit Nennung des dafür relevanten Zeitraums übertragen. Weiterhin wird in diesem Zeitraum das angefallene Monatsleistungsmaximum übermittelt.

Bei der Übermittlung des Lieferscheins vom NB für Marktlokation mit Arbeits- / Leistungspreis wird die Arbeit mit Nennung des dafür relevanten Zeitraums übertragen und weiterhin, abhängig vom Leistungspreissystem (Jahresleistungspreissystem, Monatsleistungspreissystem oder Tagesleistungspreissystem) das angefallene Leistungsmaximum. Bei Verwendung des Codes Z42 (Lieferschein Arbeits- / Leistungspreis) im BGM kann das Leistungsmaximum auch außerhalb des betrachtenden Zeitraums liegen.

Bei pauschalen Marktlokationen, für die ein Leistungsmaximum benötigt wird, ist zur Ableitung der Monatsangabe des Lieferscheins das Endedatum SG26 DTM+156 der Rechnungsperiode aus der Rechnungsposition der INVOIC zu verwenden.

Die Angabe des Zeitraumes der Arbeit, für die die jeweilige Menge übertragen wird, erfolgt über SG10 DTM+163 und SG10 DTM+164.

Bei Anwendung des Jahresleistungspreissystem oder des Monatsleistungspreissystem ist zu dem zu übermittelnden Leistungsmaximum der Monat, in dem das Maximum aufgetreten ist im SG10 DTM+306 mit dem Code 610 CCYYMM zu übermitteln.

Bei Anwendung des Tagesleistungspreissystem ist zu dem zu übermittelnden Leistungsmaximum der Tag, in dem das Maximum aufgetreten ist im SG10 DTM+306 mit dem Code 102 CCYYMMDD zu übermitteln.

Sollen Daten von mehreren Marktlokationen in einer Datei übertragen werden, ist die Wiederholung über das UNH-Segment vorzunehmen.

Kommunikationspartner, Identifikationsangabe und Art der Werte für diesen Anwendungsfall:

|Sparte|Kommunikation von|Art der Werte|Identifikationsangabe in SG6 LOC|Anmerkung|
|-|-|-|-|-|
|Strom|MSB an NB|Arbeitsmenge und Maximalleistung eines Zeitraumes zwischen zwei|ID der Marktlokation|--|


Version: 3.1f 30.09.2025 Seite 21 von 158

MSCONS Anwendungshandbuch
![edi@energy. Datenformate Strom & Gas](image)

|Sparte|Kommunikation von|Art der Werte|Identifikationsangabe in SG6 LOC|Anmerkung|||||
|-|-|-|-|-|-|-|-|-|
|||Messwerten wie Turnus, Lieferbeginn/Beginn der Ersatz-/ Grundversorgung, Lieferende/Abmeldeanfrage, Gerätewechsel, Geräteübernahme und Änderung der Parametrierung|||||||
|||Strom|||MSB an LF|Arbeitsmenge und Maximalleistung eines Zeitraumes zwischen zwei Messwerten wie Turnus, Lieferbeginn/Beginn der Ersatz-/ Grundversorgung, Lieferende/Abmeldeanfrage, Gerätewechsel, Geräteübernahme und Änderung der Parametrierung|ID der Marktlokation|--|
|Strom|NB an LF|Lieferschein für Marktlokationen mit Arbeits-/ Leistungspreis|ID der Marktlokation|Zur Übermittlung des Lieferscheins zur Netznutzungsabrechnung, wenn ein Arbeits-/Leistungspreis abgerechnet wird.|||||


### 6.3.4 Übertragung Bewegungsdaten im Kalenderjahr vor Lieferbeginn (Strom)

Tabellenspalte = Arbeit Leistungsmax. Kalenderjahr vor Lieferbeginn 13015

Dieser Anwendungsfall dient zur Übertragung notwendiger Bewegungsdaten gemäß Netznutzungsvertrag und den Umgang mit Arbeit und Leistung bei unterjährigem Lieferantenwechsel von Marktlokationen deren Bilanzierungsgrundlage RLM ist bzw. GPKE Kapitel 6.1 Use-Case: Übermittlung der bisher gemessenen Arbeits- und Leistungswerte.

Übertragen wird die Arbeit mit Nennung des dafür relevanten Abrechnungszeitraums. Weiterhin werden in diesem Zeitraum das höchste, angefallene und abgerechnete Monatsleistungsmaximum sowie das zweithöchste Monatsleistungsmaximum übertragen, sofern es vorliegt. In der Regel umfasst der relevante Abrechnungszeitraum das Zeitintervall vom 1.1. bis zum Lieferbeginn des betroffenen Lieferanten. In Fällen der unterjährigen Inbetriebnahme oder dem unterjährigen Wechsel des Anschlussnutzers inklusive eines Lieferantenwechsels im selben Kalenderjahr, beginnt der Abrechnungszeitraum mit dem Datum der Inbetriebnahme bzw. des Anschlussnutzerwechsels.

Die Angabe des Zeitraumes der Arbeit, für die die jeweilige Menge übertragen wird, erfolgt über SG10 DTM+163 und SG10 DTM+164.

Zu jedem der bis zu zwei zu übermittelnden Monatsmaxima, ist der jeweilige Monat des Maximums über die SG10 DTM+306 zu übermitteln.

Sollen Daten von mehreren Marktlokationen in einer Datei übertragen werden, ist die Wiederholung über das UNH-Segment vorzunehmen.

Kommunikationspartner, Identifikationsangabe und Art der Werte für diesen Anwendungsfall:

|Sparte|Kommunikation von|Art der Werte|Identifikationsangabe in SG6 LOC|Anmerkung|
|-|-|-|-|-|
|Strom|NB an LF|Arbeit im Kalenderjahr vor Lieferbeginn sowie bis zu zwei Monatsmaxima|ID der Marktlokation|---|


Version: 3.1f 30.09.2025 Seite 22 von 158

MSCONS Anwendungshandbuch
![edi@energy. Datenformate Strom & Gas](image)

### 6.3.5 Übertragung Energiemengen als Grundlage zur POG-Ermittlung

Tabellenspalte = Grundlage POG-Ermittlung 13028

Dieser Anwendungsfall dient zur Übertragung der Energiemenge als Grundlage für die korrekte POG-Ermittlung.

Übertragen wird die Arbeit mit Nennung des dazugehörigen Zeitraumes, welcher für den MSB für eine korrekte Ermittlung der POG relevant ist. Die Angabe des Zeitraumes der Arbeit, für die die jeweilige Menge übertragen wird, erfolgt über SG10 DTM+163 und SG10 DTM+164.

Sollen Daten von mehreren Marktlokationen in einer Datei übertragen werden, ist die Wiederholung über das UNH-Segment vorzunehmen.

Kommunikationspartner, Identifikationsangabe und Art der Werte für diesen Anwendungsfall:

|Sparte|Kommunikation von|Art der Werte|Identifikationsangabe in SG6 LOC|Anmerkung|
|-|-|-|-|-|
|Strom|NB an MSB|Energiemenge als Grundlage für die POG-Ermittlung|ID der Marktlokation|---|


Version: 3.1f
30.09.2025
Seite 23 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

### 6.3.6 Anwendungsübersicht Zählerstand Strom

|EDIFACT Struktur|Beschreibung|Zählerstand (Strom)|Bedingung|||
|-|-|-|-|-|-|
||Prüfidentifikator|13017||||
|Nutzdaten-Kopfsegment||||||
|UNB|00002||Muss|||
|UNB|0001|UNOC|UN/ECE-Zeichensatz C|X||
|UNB|0002|3|Version 3|X||
|UNB|0004||MP-ID Absender|X||
|UNB|0007|14|GS1|X||
||500|DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)|X|||
|UNB|0010||MP-ID Empfänger|X||
|UNB|0007|14|GS1|X||
||500|DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)|X|||
|UNB|0017||Datum der Erstellung|X||
|UNB|0019||Uhrzeit der Erstellung|X||
|UNB|0020||Datenaustauschreferenz|X \[918]|\[918] Format: Zeichen aus dem über UNOC definierten Zeichensatz, wobei von den Buchstaben nur Großbuchstaben erlaubt sind.|
|UNB|0026|VL|Verrechnungsliste, Zählerstand|X||
|Nachrichtenkopfsegment||||||
|UNH|00003||Muss|||
|UNH|0062||Nachrichten-Referenznummer|X||
|UNH|0065|MSCON|Bericht über den Verbrauch messbarer Dienstleistungen|X||
||S|||||
|UNH|0052|D|Entwurfs-Version|X||
|UNH|0054|04B|Ausgabe 2004 - B|X||
|UNH|0051|UN|UN/CEFACT|X||
|UNH|0057|2.4c|Versionsnummer der zugrundeliegenden BDEW-Nachrichtenbeschreibung|X||
|Beginn der Nachricht||||||
|BGM|00004||Muss|||
|BGM|1001|7|Prozessdatenbericht|X||
|BGM|1004||Dokumentennummer|X||
|BGM|1225|9|Original|X||
|Nachrichtendatum||||||
|DTM|00005||Muss|||
|DTM|2005|137|Dokumenten- /Nachrichtendatum/-zeit|X||
|DTM|2380||Datum oder Uhrzeit oder Zeitspanne, Wert|X \[931] \[494]|\[494] Das hier genannte Datum muss der Zeitpunkt sein, zu dem das Dokument erstellt wurde, oder ein Zeitpunkt, der davor liegt.<br/>\[931] Format: ZZZ = +00|
|DTM|2379|303|CCYYMMDDHHMMZZZ|X||
|Referenzangaben||||||
|SG1|||Soll \[1] ∧ \[538]|\[1] Sofern per ORDERS angefordert<br/>\[538] Hinweis: Die Referenz auf die ORDERS ist nur dann anzugeben, wenn diese Werte vom Empfänger auch ursprünglich mittels ORDERS angefragt wurden.||
|SG1|RFF|00006||Muss||
|SG1|RFF|1153|AGI|Beantragungsnummer|X|


Version: 3.1f 30.09.2025 Seite 24 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|EDIFACT Struktur|Beschreibung<br/>Prüfidentifikator|Zählerstand (Strom)<br/>13017|Bedingung||||
|-|-|-|-|-|-|-|
|SG1|RFF|1154|Referenznummer|X (\[67] ∧ (\[529] ∨ \[553]))|\[67] Wenn es sich um die Referenz auf eine ORDERS handelt<br/>\[529] Hinweis: Wert aus BGM+7 DE1004 der ORDERS mit der die Anforderung von Messwerten erfolgt ist.<br/>\[553] Hinweis: Wert aus BGM+Z34 DE1004 der ORDERS mit der die Reklamation von Werten erfolgt ist||
|Prüfidentifikator|||||||
|SG1|||Muss||||
|SG1|RFF||00009|Muss|||
|SG1|RFF|1153|Z13|Prüfidentifikator|X||
|SG1|RFF|1154|13017|Messw. Zählerstand (Strom)|X||
|MP-ID Absender|||||||
|SG2|||Muss||||
|SG2|NAD||00010|Muss|||
|SG2|NAD|3035|MS|Dokumenten- /Nachrichtenaussteller bzw. -absender|X||
|SG2|NAD|3039|MP-ID||X \[117]|\[117] Nur MP-ID aus Sparte Strom|
|SG2|NAD|3055|9|GS1|X||
|||293|DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)|X|||
|Ansprechpartner|||||||
|SG4|||Kann||||
|SG4|CTA||00011|Muss|||
|SG4|CTA|3139|IC|Informationsstelle|X||
|SG4|CTA|3412|Abteilung oder Bearbeiter|X|||
|Kommunikationsverbindung|||||||
|SG4|||||||
|SG4|COM||00012|Muss|||
|SG4|COM|3148|Kommunikationsadresse, Identifikation||X ((\[939] \[142]) ∨ (\[940] \[143])) ∧ \[576]|\[142] wenn im DE3155 in demselben COM der Code EM vorhanden ist<br/>\[143] wenn im DE3155 in demselben COM der Code TE / FX / AJ / AL vorhanden ist<br/>\[576] Hinweis: Es darf nur eine Information im DE3148 übermittelt werden<br/>\[939] Format: Die Zeichenkette muss die Zeichen @ und . enthalten<br/>\[940] Format: Die Zeichenkette muss mit dem Zeichen + beginnen und danach dürfen nur noch Ziffern folgen|
|SG4|COM|3155|TE|Telefon|X \[1P0..1]||
|||EM|E-Mail|X \[1P0..1]|||
|||AJ|weiteres Telefon|X \[1P0..1]|||
|||AL|Handy|X \[1P0..1]|||
|||FX|Telefax|X \[1P0..1]|||
|MP-ID Empfänger|||||||
|SG2|||Muss||||
|SG2|NAD||00013|Muss|||
|SG2|NAD|3035|MR|Nachrichtenempfänger|X||
|SG2|NAD|3039|MP-ID||X \[117]|\[117] Nur MP-ID aus Sparte Strom|
|SG2|NAD|3055|9|GS1|X||
|||293|DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)|X|||
|Abschnitts-Kontrollsegment|||||||
|UNS||00014|Muss||||


Version: 3.1f 30.09.2025 Seite 25 von 158

MSCONS Anwendungshandbuch
![edi@energy Datenformate Strom & Gas](image)

|EDIFACT Struktur|Beschreibung<br/>Prüfidentifikator|Zählerstand (Strom)<br/>13017|Bedingung||||
|-|-|-|-|-|-|-|
|UNS|0081||D|Trennung von Kopf- und Positionsteil|X||
|Name und Adresse|||||||
|SG5||||Muss \[2001]|\[2001] Segmentgruppe ist nur einmal je UNH anzugeben||
|SG5|NAD||00015||Muss||
|SG5|NAD|3035|DP|Lieferanschrift|X||
|Identifikationsangabe|||||||
|SG6||||Muss|||
|SG6|LOC||00017||Muss||
|SG6|LOC|3227|172|Meldepunkt|X||
|SG6|LOC|3225|Bezeichnung||M \[131] ∧ (\[951] ∧ \[510])|\[131] wenn RFF+AGK (Konfigurations-ID) nicht vorhanden<br/>\[510] Hinweis: Verwendung der ID der Messlokation<br/>\[951] Format: Zählpunktbezeichnung|
|Gerätenummer|||||||
|SG7||||Muss \[131]|\[131] wenn RFF+AGK (Konfigurations-ID) nicht vorhanden||
|SG7|RFF||00023||Muss||
|SG7|RFF|1153|MG|Gerätenummer|X||
|SG7|RFF|1154|Gerätenummer||X||
|Konfigurations-ID|||||||
|SG7||||Muss \[35] ∧ \[132]|\[35] wenn MP-ID in SG2 NAD+MS in der Rolle MSB<br/>\[132] wenn LOC+172 (Identifikationsangabe) DE3225 nicht vorhanden||
|SG7|RFF||00024||Muss||
|SG7|RFF|1153|AGK|Anwendungsreferenznummer|X||
|SG7|RFF|1154|Konfigurations-ID||X \[567]|\[567] Hinweis: Es ist die Konfigurations-ID anzugeben, die im vorherigen Stammdatenaustausch kommuniziert wurde.|
|lfd. Position|||||||
|SG9||||Muss|||
|SG9|LIN||00026||Muss||
|SG9|LIN|1082|Positionsnummer||X \[908]|\[908] Format: Mögliche Werte: 1 bis n|
|Produktidentifikation|||||||
|SG9|||||||
|SG9|PIA||00027||Muss||
|SG9|PIA|4347|5|Produktidentifikation|X||
|SG9|PIA|7140|Medium / OBIS-Kennzahl||X \[501] ∧ \[566]|\[501] Hinweis: Es sind nur die Werte erlaubt, die in der EDI\@Energy Codeliste der OBIS-Kennzahlen und Medien mit dem entsprechenden Prüfidentifikator versehen sind.<br/>\[566] Hinweis: Es sind nur die Werte erlaubt, die im vorherigen Stammdatenaustausch zu diesem Meldepunkt vom MSB zum Zeitpunkt übermittelt wurden.|
|SG9|PIA|7143|SRW|OBIS-Kennzahl|X||
|Mengenangaben|||||||
|SG10||||Muss|||
|SG10|QTY||00028||Muss||


Version: 3.1f 30.09.2025 Seite 26 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|EDIFACT Struktur|Beschreibung<br/>Prüfidentifikator|Zählerstand (Strom)<br/>13017|Bedingung|
|-|-|-|-|
|SG10 QTY 6063|220 Wahrer Wert<br/>67 Ersatzwert<br/>Z18 Vorläufiger Wert|X<br/>X \[35] ∨ (\[32] ∧ \[77])<br/>X \[35] ∧ \[113]|\[32] wenn MP-ID in SG2 NAD+MS in der Rolle NB<br/>\[35] wenn MP-ID in SG2 NAD+MS in der Rolle MSB<br/>\[77] Wenn MP-ID in SG2 NAD+MR der RB HKN-R<br/>\[113] wenn SG7 RFF+AGK (Konfigurations-ID) vorhanden|
|SG10 QTY 6060|Menge|X \[902] ∧ \[906]|\[902] Format: Möglicher Wert: ≥ 0<br/>\[906] Format: max. 3 Nachkommastellen|
|Ablesedatum||||
|SG10||||
|SG10 DTM 00031||Soll \[93] ∧ \[128] ∧ \[131] ∧ \[569]|\[93] Wenn SG10 QTY DE6063 mit Wert 220 vorhanden<br/>\[128] Wenn es sich um eine Ablesung handelt, welche keine Ablesung aufgrund der Änderung an der Messtechnik oder deren Konfiguration ist (z.B. Kundenablesung).<br/>\[131] wenn RFF+AGK (Konfigurations-ID) nicht vorhanden<br/>\[569] Hinweis: Bei mehreren Zählerständen einer Messlokation (z. B. HT/NT) ist diese Zeitangabe zu nutzen und eine Wiederholung das SG9 LIN durchzuführen.|
|SG10 DTM 2005|9 Bearbeitungs-/Verarbeitungsdatum/-zeit|X||
|SG10 DTM 2380|Datum oder Uhrzeit oder Zeitspanne, Wert|X (\[931] \[111] ∧ \[495]) ⊻ (\[134] ∧ \[135])|\[111] Wenn SG10 DTM+9 DE2379 in demselben Segment mit Wert 303 vorhanden<br/>\[134] Wenn SG10 DTM+9 DE2379 in demselben Segment mit Wert 102 vorhanden<br/>\[135] Der Wert an der Stelle CCYYMMDD muss ≤ dem Wert an der Stelle CCYYMMDD im DE2380 des DTM+137 sein<br/>\[495] Der Zeitpunkt muss ≤ dem Wert im DE2380 des DTM+137 sein<br/>\[931] Format: ZZZ = +00|
|SG10 DTM 2379|102 CCYYMMDD<br/>303 CCYYMMDDHHMMZZZ|X<br/>X||
|Nutzungszeitpunkt||||
|SG10||||
|SG10 DTM 00032||Muss \[569]|\[569] Hinweis: Bei mehreren Zählerständen einer Messlokation (z. B. HT/NT) ist diese Zeitangabe zu nutzen und eine Wiederholung das SG9 LIN durchzuführen.|
|SG10 DTM 2005|7 Gültigkeitsdatum/-zeit|X||


Version: 3.1f 30.09.2025 Seite 27 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|EDIFACT Struktur|Beschreibung|Zählerstand (Strom)|Bedingung|
|-|-|-|-|
||Prüfidentifikator|13017||
|SG10 DTM 2380|Datum oder Uhrzeit oder Zeitspanne, Wert|X \[UB1] ∧ \[495] ∧ (\[130] ∨ \[133])|\[130] Wenn innerhalb desselben LIN-Segments neben diesem Segment (SG10 DTM+7 Nutzungszeitpunkt) noch das SG10 DTM+60 (Ausführungs- / Änderungszeitpunkt) oder das SG10 DTM+9 (Ablesedatum) vorhanden, darf der Wert der Differenz zwischen dem größeren und dem kleineren Zeitpunkt der DTM-Segmente ausschließlich < 24 Stunden sein. Findet zwischen den beiden Zeitpunkten die Sommer/Winter-Zeitumschaltung statt, darf der Wert der Differenz ausschließlich < 25 Stunden sein. Findet zwischen den beiden Zeitpunkten die Winter/Sommer-Zeitumschaltung statt, darf der Wert der Differenz ausschließlich < 23 Stunden sein.<br/>\[133] Wenn innerhalb desselben LIN-Segments neben diesem Segment (SG10 DTM+7 Nutzungszeitpunkt) noch das SG10 DTM+9 (Ablesedatum) mit dem Code 102 im DE2379 vorhanden ist, darf der Wert der Differenz zwischen dem Wert an der Stelle CCYYMMDD des größeren und dem kleineren Zeitpunkt der DTMSegmente an der Stelle CCYYMMDD ausschließlich 0 oder 1 Tag sein.<br/>\[495] Der Zeitpunkt muss ≤ dem Wert im DE2380 des DTM+137 sein|
|SG10 DTM 2379|\*\*303\*\* CCYYMMDDHHMMZZZ|X||
|\*\*Ausführungs- / Änderungszeitpunkt\*\*||||
|\*\*SG10\*\*||Soll \[129] ∧ \[569]|\[129] Wenn es sich um eine Ablesung aufgrund der Änderung an der Messtechnik oder deren Konfiguration handelt (z.B. Gerätewechsel).<br/>\[569] Hinweis: Bei mehreren Zählerständen einer Messlokation (z. B. HT/NT) ist diese Zeitangabe zu nutzen und eine Wiederholung das SG9 LIN durchzuführen.|
|SG10 DTM 00033||||
|SG10 DTM 2005|\*\*60\*\* Konstruktionsänderungsdatum|X||
|SG10 DTM 2380|Datum oder Uhrzeit oder Zeitspanne, Wert|X \[931] \[495]|\[495] Der Zeitpunkt muss ≤ dem Wert im DE2380 des DTM+137 sein<br/>\[931] Format: ZZZ = +00|
|SG10 DTM 2379|\*\*303\*\* CCYYMMDDHHMMZZZ|X||
|\*\*Plausibilisierungshinweis\*\*||||
|\*\*SG10\*\*||Soll (\[92] ⊻ \[93]) ∧ \[126]|\[92] Wenn SG10 QTY DE6063 mit Wert 67 vorhanden<br/>\[93] Wenn SG10 QTY DE6063 mit Wert 220 vorhanden<br/>\[126] wenn Plausibilisierungshinweise vorliegen|
|SG10 STS 00035||||
|SG10 STS 9015|\*\*Z33\*\* Plausibilisierungshinweis|X||


Version: 3.1f 30.09.2025 Seite 28 von 158

MSCONS Anwendungshandbuch
![edi@energy. Datenformate Strom & Gas](image)

|EDIFACT Struktur|Beschreibung|Zählerstand (Strom)|Bedingung||
|-|-|-|-|-|
||Prüfidentifikator|13017|||
|SG10 STS 9013|Z83|Kundenselbstablesung|X \[5P0..1]||
||Z84|Leerstand|X \[4P0..1] ⊻ \[5P0..1]||
||Z85|Realer Zählerüberlauf geprüft|X \[4P0..1] ⊻ \[5P0..1]||
||Z86|Plausibel wg. Kontrollablesung|X \[4P0..1] ⊻ \[5P0..1]||
||Z87|Plausibel wg. Kundenhinweis|X \[4P0..1] ⊻ \[5P0..1]||
||ZC3|Austausch des Ersatzwertes|X \[4P0..1] ⊻ \[5P0..1]||
||ZS2|Wert auf Basis der modernen Messeinrichtung|X \[4P0..1]||
|Ersatzwertbildungsverfahren|||||
|SG10|||||
|SG10 STS 00036||Muss \[92]|\[92] Wenn SG10 QTY DE6063 mit Wert 67 vorhanden||
|SG10 STS 9015|Z32|Ersatzwertbildungsverfahren|X||
|SG10 STS 9013|Z88|Vergleichsmessung (geeicht)|X \[4P0..1]||
||Z89|Vergleichsmessung (nicht geeicht)|X \[4P0..1]||
||Z92|Interpolation|X \[4P0..1]||
||ZJ2|Statistische Methode|X \[4P0..1]||
|Korrekturgrund|||||
|SG10|||||
|SG10 STS 00037||Soll \[127] ∧ \[541]|\[127] wenn ein Korrekturgrund anzugeben ist \[541] Hinweis: Ein Korrekturgrund ist anzugeben, wenn:<br/>1. ein bereits an den MP übermittelter vorläufiger Wert nach Stornierung durch einen Ersatzwert ersetzt wird, oder<br/>2. ein bereits an den MP übermittelter Ersatzwert nach Stornierung durch einen Ersatzwert ersetzt wird, oder<br/>3. ein bereits an den MP übermittelter wahrer Wert nach Stornierung durch einen Ersatzwert ersetzt wird, oder<br/>4. ein bereits an den MP übermittelter wahrer Wert nach Stornierung durch einen wahren Wert ersetzt wird.||
|SG10 STS 9015|Z34|Korrekturgrund|X||


Version: 3.1f 30.09.2025 Seite 29 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|EDIFACT Struktur|Beschreibung|Zählerstand (Strom)|Bedingung||||
|-|-|-|-|-|-|-|
||Prüfidentifikator|13017|||||
|SG10 STS 9013|Z74 kein Zugang|X \[4P0..1]|||||
||Z75 Kommunikationsstörung|X \[4P0..1]|||||
||Z76 Netzausfall|X \[4P0..1]|||||
||Z77 Spannungsausfall|X \[4P0..1]|||||
||Z78 Gerätewechsel|X \[4P0..1]|||||
||Z79 Kalibrierung|X \[4P0..1]|||||
||Z80 Gerät arbeitet außerhalb der Betriebsbedingungen|X \[4P0..1]|||||
||Z81 Messeinrichtung gestört/defekt|X \[4P0..1]|||||
||Z82 Unsicherheit Messung|X \[4P0..1]|||||
||ZA0 Uhrzeit gestellt /Synchronisation|X \[4P0..1]|||||
||ZA1 Messwert unplausibel|X \[4P0..1]|||||
||ZA3 Falscher Wandlerfaktor|X \[4P0..1] ⊻ \[5P0..1]|||||
||ZA4 Fehlerhafte Ablesung|X \[4P0..1] ⊻ \[5P0..1]|||||
||ZA5 Änderung der Berechnung|X \[4P0..1] ⊻ \[5P0..1]|||||
||ZA6 Umbau der Messlokation|X \[4P0..1] ⊻ \[5P0..1]|||||
||ZA7 Datenbearbeitungsfehler|X \[4P0..1] ⊻ \[5P0..1]|||||
||ZB0 Störung / Defekt Messeinrichtung|X \[4P0..1] ⊻ \[5P0..1]|||||
||ZB9 Änderung Tarifschaltzeiten|X \[4P0..1] ⊻ \[5P0..1]|||||
||ZC2 Tarifschaltgerät defekt|X \[4P0..1] ⊻ \[5P0..1]|||||
||ZC4 Impulswertigkeit nicht ausreichend|X \[4P0..1]|||||
|Grund der Ersatzwertbildung SG10|||||||
|SG10 STS 00038||Muss \[92]|\[92] Wenn SG10 QTY DE6063 mit Wert 67 vorhanden||||
|SG10 STS 9015|Z40 Grund der Ersatzwertbildung|X|||||
|SG10 STS 9013|Z74 kein Zugang|X \[4P0..1]|||||
||Z75 Kommunikationsstörung|X \[4P0..1]|||||
||Z76 Netzausfall|X \[4P0..1]|||||
||Z77 Spannungsausfall|X \[4P0..1]|||||
||Z78 Gerätewechsel|X \[4P0..1]|||||
||Z79 Kalibrierung|X \[4P0..1]|||||
||Z80 Gerät arbeitet außerhalb der Betriebsbedingungen|X \[4P0..1]|||||
||Z81 Messeinrichtung gestört/defekt|X \[4P0..1]|||||
||Z82 Unsicherheit Messung|X \[4P0..1]|||||
||ZA0 Uhrzeit gestellt /Synchronisation|X \[4P0..1]|||||
||ZA1 Messwert unplausibel|X \[4P0..1]|||||
||ZA3 Falscher Wandlerfaktor|X \[4P0..1]|||||
||ZA4 Fehlerhafte Ablesung|X \[4P0..1]|||||
||ZA5 Änderung der Berechnung|X \[4P0..1]|||||
||ZA6 Umbau der Messlokation|X \[4P0..1]|||||
||ZA7 Datenbearbeitungsfehler|X \[4P0..1]|||||
||ZB0 Störung / Defekt Messeinrichtung|X \[4P0..1]|||||
||ZB9 Änderung Tarifschaltzeiten|X \[4P0..1]|||||
||ZC2 Tarifschaltgerät defekt|X \[4P0..1]|||||
||ZC4 Impulswertigkeit nicht ausreichend|X \[4P0..1]|||||
||ZT8 Anforderung in die Vergangenheit, zum angeforderten Zeitpunkt liegt kein Wert vor.|X \[4P0..1]|||||
|Nachrichten-Endesegment|||||||
|UNT 00041||Muss|||||


Version: 3.1f 30.09.2025 Seite 30 von 158

MSCONS Anwendungshandbuch
![edi@energy. Datenformate Strom & Gas](image)

|EDIFACT Struktur|Beschreibung|Zählerstand (Strom)|Bedingung||
|-|-|-|-|-|
||Prüfidentifikator|13017|||
|UNT|0074|Anzahl der Segmente in einer Nachricht|X||
|UNT|0062|Nachrichten-Referenznummer|X||
|Nutzdaten-Endesegment|||||
|UNZ|00042||Muss||
|UNZ|0036|Datenaustauschzähler|X||
|UNZ|0020|Datenaustauschreferenz|X||


Version: 3.1f	30.09.2025	Seite 31 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

## 6.3.7 Anwendungsübersicht Energiemengen Strom

|EDIFACT Struktur|Beschreibung<br/>Prüfidentifikator|Energiemenge (Strom)<br/>13019|Energiemenge u. Leistungsmax. (Strom)<br/>13016|Arbeit Leistungsmax. Kalenderjahr vor Lieferbeginn<br/>13015|Bedingung||
|-|-|-|-|-|-|-|
|\*\*Nutzdaten-Kopfsegment\*\*|||||||
|\*\*UNB\*\*|00002||Muss|Muss|Muss||
|\*\*UNB 0001\*\*|\*\*UNOC\*\* UN/ECE-Zeichensatz C|X|X|X|||
|\*\*UNB 0002\*\*|\*\*3\*\* Version 3|X|X|X|||
|\*\*UNB 0004\*\*|MP-ID Absender|X|X|X|||
|\*\*UNB 0007\*\*|\*\*14\*\* GS1<br/>\*\*500\*\* DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)|X|X|X|||
|\*\*UNB 0010\*\*|MP-ID Empfänger|X|X|X|||
|\*\*UNB 0007\*\*|\*\*14\*\* GS1<br/>\*\*500\*\* DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)|X|X|X|||
|\*\*UNB 0017\*\*|Datum der Erstellung|X|X|X|||
|\*\*UNB 0019\*\*|Uhrzeit der Erstellung|X|X|X|||
|\*\*UNB 0020\*\*|Datenaustauschreferenz|X \[918]|X \[918]|X \[918]|\[918] Format: Zeichen aus dem über UNOC definierten Zeichensatz, wobei von den Buchstaben nur Großbuchstaben erlaubt sind.||
|\*\*UNB 0026\*\*|\*\*EM\*\* Energiemenge|X|X|X|||
|\*\*Nachrichtenkopfsegment\*\*|||||||
|\*\*UNH\*\*|00003||Muss|Muss|Muss||
|\*\*UNH 0062\*\*|Nachrichten-Referenznummer|X|X|X|||
|\*\*UNH 0065\*\*|\*\*MSCONS\*\* Bericht über den Verbrauch messbarer Dienstleistungen|X|X|X|||
|\*\*UNH 0052\*\*|\*\*D\*\* Entwurfs-Version|X|X|X|||
|\*\*UNH 0054\*\*|\*\*04B\*\* Ausgabe 2004 - B|X|X|X|||
|\*\*UNH 0051\*\*|\*\*UN\*\* UN/CEFACT|X|X|X|||
|\*\*UNH 0057\*\*|\*\*2.4c\*\* Versionsnummer der zugrundeliegenden BDEW-Nachrichtenbeschreibung|X|X|X|||
|\*\*Beginn der Nachricht\*\*|||||||
|\*\*BGM\*\*|00004||Muss|Muss|Muss||
|\*\*BGM 1001\*\*|\*\*7\*\* Prozessdatenbericht|X|||\[32] wenn MP-ID in SG2 NAD+MS in der Rolle NB<br/>\[33] wenn MP-ID in SG2 NAD+MR in der Rolle LF<br/>\[492] wenn MP-ID in NAD+MR aus Sparte Strom||
||\*\*Z27\*\* Bewegungsdaten im Kalenderjahr vor Lieferbeginn|||X|||
||\*\*Z28\*\* Energiemenge und Leistungsmaximum||X||||
||\*\*Z41\*\* Lieferschein Grund- / Arbeitspreis|X \[492] ∧ \[32] ∧ \[33]|||||
||\*\*Z42\*\* Lieferschein Arbeits- / Leistungspreis||X \[492] ∧ \[32] ∧ \[33]||||
|\*\*BGM 1004\*\*|Dokumentennummer|X|X|X|||
|\*\*BGM 1225\*\*|\*\*9\*\* Original|X|X|X|||
|\*\*Nachrichtendatum\*\*|||||||
|\*\*DTM\*\*|00005||Muss|Muss|Muss||


Version: 3.1f 30.09.2025 Seite 32 von 158

MSCONS Anwendungshandbuch
![edi@energy. Datenformate Strom & Gas](image)

|EDIFACT Struktur||Beschreibung<br/>Prüfidentifikator||Energiemenge (Strom)<br/>13019|Energiemenge u. Leistungsmax. (Strom)<br/>13016|Arbeit Leistungsmax. Kalenderjahr vor Lieferbeginn<br/>13015|Bedingung||
|-|-|-|-|-|-|-|-|-|
|DTM|2005||137|Dokumenten-/Nachrichtendatum/-zeit|X|X|X||
|DTM|2380||Datum oder Uhrzeit oder Zeitspanne, Wert|X \[931] \[494]|X \[931] \[494]|X \[931] \[494]|\[494] Das hier genannte Datum muss der Zeitpunkt sein, zu dem das Dokument erstellt wurde, oder ein Zeitpunkt, der davor liegt.<br/>\[931] Format: ZZZ = +00||
|DTM|2379||303|CCYYMMDDHHMMZZZ|X|X|X||
|Referenzangaben SG1|||||Soll \[1] ∧ \[68] Muss \[35] ∧ (\[38] ⊻ \[113])|Soll \[1] ∧ \[69]|Muss|\[1] Sofern per ORDERS angefordert<br/>\[35] wenn MP-ID in SG2 NAD+MS in der Rolle MSB<br/>\[38] wenn in SG6 LOC+172 DE3225 die ID der Messlokation angegeben ist<br/>\[68] Wenn BGM+7 vorhanden<br/>\[69] Wenn BGM+Z28 vorhanden<br/>\[113] wenn SG7 RFF+AGK (Konfigurations-ID) vorhanden|
|SG1|RFF|00006|||Muss|Muss|Muss||
|SG1|RFF|1153|AGI|Beantragungsnummer|X|X|X||
|SG1|RFF|1154||Referenznummer|X (\[529] ∨ \[553]) ⊻ (\[531] ∧ \[509])|X (\[528] ∨ \[553])|X \[530]|\[509] Hinweis: Falls es sich um eine Korrekturenergiemenge handelt, ist hier die Referenz auf die MSCONS anzugeben, in der der Zählerstand vorab übermittelt wurde.<br/>\[528] Hinweis: Wert aus BGM+Z28 DE1004 der ORDERS mit der die Anforderung von Messwerten erfolgt ist.<br/>\[529] Hinweis: Wert aus BGM+7 DE1004 der ORDERS mit der die Anforderung von Messwerten erfolgt ist.<br/>\[530] Hinweis: Wert aus SG4 IDE+24 DE7402 der UTILMD mit dem der Sender der MSCONS die vorherigen Stammdaten mittels UTILMD übermittelt hat.<br/>\[531] Hinweis: Wert aus BGM+7 DE1004 der MSCONS mit der der Zählerstand übermittelt wurde.<br/>\[553] Hinweis: Wert aus BGM+Z34 DE1004 der ORDERS mit der die Reklamation von Werten erfolgt ist|
|Referenz auf vorherige Stammdatenmeldung des MSB SG1|||||||||
|SG1|RFF|00008|||||||


Version: 3.1f
30.09.2025
Seite 33 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|EDIFACT Struktur|Beschreibung<br/>Prüfidentifikator|Energiemenge (Strom)<br/>13019|Energiemenge u. Leistungsmax. (Strom)<br/>13016|Arbeit Leistungsmax. Kalenderjahr vor Lieferbeginn<br/>13015|Bedingung||||||
|-|-|-|-|-|-|-|-|-|-|-|
|\*\*Prüfidentifikator\*\*|||||||||||
|\*\*SG1\*\*|||\*\*Muss\*\*|\*\*Muss\*\*|\*\*Muss\*\*||||||
|SG1|RFF|00009|||Muss|Muss|Muss||||
|SG1|RFF|1153|\*\*Z13\*\*|Prüfidentifikator|X|X|X||||
|SG1|RFF|1154|\*\*13015\*\*|Bewegungsdaten im Kalenderjahr vor Lieferbeginn|||||X||
|||\*\*13016\*\*|Energiemenge und Leistungsmaximum|||X|||||
|||\*\*13019\*\*|Messwert Energiemenge (Strom)|X|||||||
|\*\*MP-ID Absender\*\*|||||||||||
|\*\*SG2\*\*|||\*\*Muss\*\*|\*\*Muss\*\*|\*\*Muss\*\*||||||
|SG2|NAD|00010|||Muss|Muss|Muss||||
|SG2|NAD|3035|\*\*MS\*\*|Dokumenten-/Nachrichtenaussteller bzw. -absender|X|X|X||||
|SG2|NAD|3039|MP-ID|||X \[117]|X \[117]|X \[117]|\[117] Nur MP-ID aus Sparte Strom||
|SG2|NAD|3055|\*\*9\*\*|GS1|X|X|X||||
|||\*\*293\*\*|DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)|X|X|X|||||
|\*\*Ansprechpartner\*\*|||||||||||
|\*\*SG4\*\*|||\*\*Kann\*\*|\*\*Kann\*\*|\*\*Kann\*\*||||||
|SG4|CTA|00011|||Muss|Muss|Muss||||
|SG4|CTA|3139|\*\*IC\*\*|Informationsstelle|X|X|X||||
|SG4|CTA|3412|Abteilung oder Bearbeiter|X|X|X|||||
|\*\*Kommunikationsverbindung\*\*|||||||||||
|\*\*SG4\*\*|||||||||||
|SG4|COM|00012|||Muss|Muss|Muss||||
|SG4|COM|3148|Kommunikationsadresse, Identifikation|X ((\[939] \[142]) ∨ (\[940] \[143])) ∧ \[576]|X ((\[939] \[142]) ∨ (\[940] \[143])) ∧ \[576]|X ((\[939] \[142]) ∨ (\[940] \[143])) ∧ \[576]|\[142] wenn im DE3155 in demselben COM der Code EM vorhanden ist<br/>\[143] wenn im DE3155 in demselben COM der Code TE / FX / AJ / AL vorhanden ist<br/>\[576] Hinweis: Es darf nur eine Information im DE3148 übermittelt werden<br/>\[939] Format: Die Zeichenkette muss die Zeichen @ und . enthalten<br/>\[940] Format: Die Zeichenkette muss mit dem Zeichen + beginnen und danach dürfen nur noch Ziffern folgen||||
|SG4|COM|3155|\*\*TE\*\*|Telefon|X \[1P0..1]|X \[1P0..1]|X \[1P0..1]||||
|||\*\*EM\*\*|E-Mail|X \[1P0..1]|X \[1P0..1]|X \[1P0..1]|||||
|||\*\*AJ\*\*|weiteres Telefon|X \[1P0..1]|X \[1P0..1]|X \[1P0..1]|||||
|||\*\*AL\*\*|Handy|X \[1P0..1]|X \[1P0..1]|X \[1P0..1]|||||
|||\*\*FX\*\*|Telefax|X \[1P0..1]|X \[1P0..1]|X \[1P0..1]|||||
|\*\*MP-ID Empfänger\*\*|||||||||||
|\*\*SG2\*\*|||\*\*Muss\*\*|\*\*Muss\*\*|\*\*Muss\*\*||||||
|SG2|NAD|00013|||Muss|Muss|Muss||||
|SG2|NAD|3035|\*\*MR\*\*|Nachrichtenempfänger|X|X|X||||


Version: 3.1f 30.09.2025 Seite 34 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|EDIFACT Struktur|Beschreibung<br/>Prüfidentifikator|Energiemenge (Strom)<br/>13019|Energiemenge u. Leistungsmax. (Strom)<br/>13016|Arbeit Leistungsmax. Kalenderjahr vor Lieferbeginn<br/>13015|Bedingung||||
|-|-|-|-|-|-|-|-|-|
|SG2|NAD|3039|MP-ID|X \[117]|X \[117]|X \[117]|\[117] Nur MP-ID aus Sparte Strom||
|SG2|NAD|3055|9|GS1|X|X|X||
|SG2|NAD|3055|293|DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)|X|X|X||
|Abschnitts-Kontrollsegment|||||||||
|UNS||00014||Muss|Muss|Muss|||
|UNS|0081||D|Trennung von Kopf- und Positionsteil|X|X|X||
|Name und Adresse|||||||||
|SG5|||||Muss \[2001]|Muss \[2001]|Muss \[2001]|\[2001] Segmentgruppe ist nur einmal je UNH anzugeben|
|SG5|NAD|00015||Muss|Muss|Muss|||
|SG5|NAD|3035|DP|Lieferanschrift|X|X|X||
|Identifikationsangabe|||||||||
|SG6|||||Muss|Muss|Muss||
|SG6|LOC|00017||Muss|Muss|Muss|||
|SG6|LOC|3227|172|Meldepunkt|X|X|X||
|SG6|LOC|3225|Bezeichnung|M \[131] ∧ ((\[951] ∧ \[510] ∧ \[522]) ⊻ (\[950] ∧ \[514] ∧ (\[523] ∨ \[525])))|X \[950] \[514]|X \[950] \[514]|\[131] wenn RFF+AGK (Konfigurations-ID) nicht vorhanden<br/>\[510] Hinweis: Verwendung der ID der Messlokation<br/>\[514] Hinweis: Verwendung der ID der Marktlokation<br/>\[522] Hinweis: Nur für die Übermittlung der Korrekturenergiemengen im Zeitintervall zwischen zwei Messwerten.<br/>\[523] Hinweis: Nur für die Übermittlung der Energiemenge im Zeitintervall zwischen zwei Messwerten vor der Netznutzungsabrechnung.<br/>\[525] Hinweis: Nur für die Übermittlung der Energiemenge im Zeitintervall für eine Marktlokation ohne Messlokation (Pauschalanlage) wenn eines der Ereignisse aus Kapitel 4.2 eingetreten ist.<br/>\[950] Format: Marktlokations-ID<br/>\[951] Format: Zählpunktbezeichnung||
|Konfigurations-ID|||||||||
|SG7|||||Muss \[35] ∧ \[132] ∧ \[138]|||\[35] wenn MP-ID in SG2 NAD+MS in der Rolle MSB<br/>\[132] wenn LOC+172 (Identifikationsangabe) DE3225 nicht vorhanden<br/>\[138] Wenn es sich um eine Korrekturenergiemenge auf einen Wert aus einem iMS handelt|


Version: 3.1f 30.09.2025 Seite 35 von 158

MSCONS Anwendungshandbuch
edi@energy Datenformate Strom & Gas

|EDIFACT Struktur|Beschreibung|Energiemenge (Strom)|Energiemenge u. Leistungsmax. (Strom)|Arbeit Leistungsmax. Kalenderjahr vor Lieferbeginn|Bedingung||
|-|-|-|-|-|-|-|
||Prüfidentifikator|13019|13016|13015|||
|SG7 RFF|00024||Muss||||
|SG7 RFF|1153|AGK Anwendungsreferenznummer|X||||
|SG7 RFF|1154|Konfigurations-ID|X \[567]|||\[567] Hinweis: Es ist die Konfigurations-ID anzugeben, die im vorherigen Stammdatenaustausch kommuniziert wurde.|
|lfd. Position|||||||
|SG9||Muss|Muss|Muss \[2002] ∧ \[502]|\[502] Hinweis: Einmal für die Energiemenge von Beginn des Kalenderjahres bis zum Lieferbeginn und bis zu zweimal für die zwei höchsten Monatsleistungswerte (wegen KAV) von Beginn des Kalenderjahres bis zum Lieferbeginn<br/>\[2002] Segmentgruppe ist bis zu drei Mal je SG5 NAD+DP anzugeben||
|SG9 LIN|00026||Muss|Muss|Muss||
|SG9 LIN|1082|Positionsnummer|X \[908]|X \[908]|X \[908]|\[908] Format: Mögliche Werte: 1 bis n|
|Produktidentifikation|||||||
|SG9|||||||
|SG9 PIA|00027||Muss|Muss|Muss||
|SG9 PIA|4347|5 Produktidentifikation|X|X|X||
|SG9 PIA|7140|Medium / OBIS-Kennzahl|X (\[68] ∧ \[501] ∧ \[566]) ⊻ (\[90] ∧ \[501])|X (\[69] ∧ \[501] ∧ \[566]) ⊻ (\[91] ∧ \[501])|X \[501]|\[68] Wenn BGM+7 vorhanden<br/>\[69] Wenn BGM+Z28 vorhanden<br/>\[90] Wenn BGM+Z41 vorhanden<br/>\[91] Wenn BGM+Z42 vorhanden<br/>\[501] Hinweis: Es sind nur die Werte erlaubt, die in der EDI\@Energy Codeliste der OBIS-Kennzahlen und Medien mit dem entsprechenden Prüfidentifikator versehen sind.<br/>\[566] Hinweis: Es sind nur die Werte erlaubt, die im vorherigen Stammdatenaustausch zu diesem Meldepunkt vom MSB zum Zeitpunkt übermittelt wurden.|
|SG9 PIA|7143|SRW OBIS-Kennzahl|X|X \[79]|X|\[78] Wenn SG9 PIA+5+1-66?:13.6.0/1-66?:14.6.0/1-66?:13.9.0/1-66?:14.9.0 vorhanden|
|||Z02 BDEW OBIS-ähnliche Kennzahl||X \[78]||\[79] Wenn SG9 PIA+5+1-66?:13.6.0/1-66?:14.6.0/1-66?:13.9.0/1-66?:14.9.0 nicht vorhanden|
|Mengenangaben|||||||
|SG10||Muss|Muss|Muss|||


Version: 3.1f 30.09.2025 Seite 36 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|EDIFACT Struktur|Beschreibung|Energiemenge (Strom)|Energiemenge u. Leistungsmax. (Strom)|Arbeit Leistungsmax. Kalenderjahr vor Lieferbeginn|Bedingung||
|-|-|-|-|-|-|-|
||Prüfidentifikator|13019|13016|13015|||
|SG10 QTY|00028||Muss|Muss|Muss||
|SG10 QTY 6063|220|Wahrer Wert|X \[68]|X \[69]|X|\[32] wenn MP-ID in SG2 NAD+MS in der Rolle NB<br/>\[35] wenn MP-ID in SG2 NAD+MS in der Rolle MSB<br/>\[68] Wenn BGM+7 vorhanden<br/>\[69] Wenn BGM+Z28 vorhanden<br/>\[77] Wenn MP-ID in SG2 NAD+MR der RB HKN-R<br/>\[90] Wenn BGM+Z41 vorhanden<br/>\[91] Wenn BGM+Z42 vorhanden|
||67|Ersatzwert|X \[68] ∧ (\[35] ∨ (\[32] ∧ \[77]))|X \[69]|X||
||Z18|Vorläufiger Wert||X \[35] ∧ \[69]|||
||Z31|Angabe für Lieferschein|X \[90]|X \[91]|||
|SG10 QTY 6060|Menge||X (\[902] ∧ \[906] \[46]) ∨ (\[910] ∧ \[906] \[62]) ∨ (\[910] ∧ \[906] \[144])|X \[902] ∧ \[906]|X \[902] ∧ \[906]|\[46] Wenn Wert in SG6 LOC+172 DE3225 genau 11 Stellen<br/>\[62] Wenn Wert in SG6 LOC+172 DE3225 genau 33 Stellen<br/>\[144] Wenn Wert in SG7 RFF+AGK DE1154 (Konfigurations-ID) vorhanden<br/>\[902] Format: Möglicher Wert: ≥ 0<br/>\[906] Format: max. 3 Nachkommastellen<br/>\[910] Format: Möglicher Wert: < 0 oder ≥ 0|
|Beginn Messperiode SG10|||||||
|SG10 DTM|00029||Muss|Muss \[73]|Muss \[27]|\[27] Wenn SG9 PIA+5+1-1?:1.9.0 vorhanden<br/>\[73] Wenn SG9 PIA+5+1-b?:1.9.e/1-b?:3.9.0/1-b?:4.9.0/1-66?:13.9.0/1-66?:14.9.0 (b=Kanal: Wert gemäß Codeliste der OBIS-Kennzahlen und Medien, e=Tarif: Wert gemäß Codeliste der OBIS-Kennzahlen und Medien) vorhanden|
|SG10 DTM 2005|163|Verarbeitung, Beginndatum/-zeit|X|X|X||
|SG10 DTM 2380|Datum oder Uhrzeit oder Zeitspanne, Wert||X (((\[UB1] ∧ \[119]) ⊻ (\[931] \[38]) ⊻ (\[931] \[144])) ∧ \[495])|X \[UB1] ∧ \[495]|X \[UB1] ∧ \[495]|\[38] wenn in SG6 LOC+172 DE3225 die ID der Messlokation angegeben ist<br/>\[119] wenn in SG6 LOC+172 DE3225 die ID der Marktlokation angegeben ist<br/>\[144] Wenn Wert in SG7 RFF+AGK DE1154 (Konfigurations-ID) vorhanden<br/>\[495] Der Zeitpunkt muss ≤ dem Wert im DE2380 des DTM+137 sein<br/>\[931] Format: ZZZ = +00|
|SG10 DTM 2379|303|CCYYMMDDHHMMZZZ|X|X|X||
|Ende Messperiode SG10|||||||


Version: 3.1f 30.09.2025 Seite 37 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|EDIFACT Struktur||Beschreibung<br/>Prüfidentifikator|Energiemenge (Strom)<br/>13019|Energiemenge u. Leistungsmax. (Strom)<br/>13016|Arbeit Leistungsmax. Kalenderjahr vor Lieferbeginn<br/>13015|Bedingung||
|-|-|-|-|-|-|-|-|
|SG10 DTM|00030||Muss|Muss \[73]|Muss \[27]|\[27] Wenn SG9 PIA+5+1-1?:1.9.0 vorhanden<br/>\[73] Wenn SG9 PIA+5+1-b?:1.9.e/1-b?:3.9.0/1-b?:4.9.0/1-66?:13.9.0/1-66?:14.9.0 (b=Kanal: Wert gemäß Codeliste der OBIS-Kennzahlen und Medien, e=Tarif: Wert gemäß Codeliste der OBIS-Kennzahlen und Medien) vorhanden||
|SG10 DTM 2005||\*\*164\*\*|\*\*Verarbeitung, Endedatum/-zeit\*\*|X|X|X||
|SG10 DTM 2380||Datum oder Uhrzeit oder Zeitspanne, Wert|X (((\[UB1] ∧ \[119]) ⊻ (\[931] \[38]) ⊻ (\[931] \[144])) ∧ \[495])|X \[UB1] ∧ \[495]|X \[UB1] ∧ \[495]|\[38] wenn in SG6 LOC+172 DE3225 die ID der Messlokation angegeben ist<br/>\[119] wenn in SG6 LOC+172 DE3225 die ID der Marktlokation angegeben ist<br/>\[144] Wenn Wert in SG7 RFF+AGK DE1154 (Konfigurations-ID) vorhanden<br/>\[495] Der Zeitpunkt muss ≤ dem Wert im DE2380 des DTM+137 sein<br/>\[931] Format: ZZZ = +00||
|SG10 DTM 2379||\*\*303\*\*|\*\*CCYYMMDDHHMMZZZ\*\*|X|X|X||
|\*\*Leistungsperiode\*\*||||||||
|SG10 DTM|00034|||Muss \[72]|Muss \[28]|\[28] Wenn SG9 PIA+5+1-1?:1.9.0 nicht vorhanden<br/>\[72] Wenn SG9 PIA+5+1-b?:1.6.0/1-b?:3.6.0/1-b?:4.6.0/1-66?:13.6.0/1-66?:14.6.0 (b=Kanal: Wert gemäß Codeliste der OBIS-Kennzahlen und Medien) vorhanden||
|SG10 DTM 2005||\*\*306\*\*|\*\*Leistungsperiode\*\*||X|X||
|SG10 DTM 2380||Datum oder Uhrzeit oder Zeitspanne, Wert||X|X|||


Version: 3.1f 30.09.2025 Seite 38 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|EDIFACT Struktur|Beschreibung<br/>Prüfidentifikator|Energiemenge (Strom)<br/>13019|Energiemenge u. Leistungsmax. (Strom)<br/>13016|Arbeit Leistungsmax. Kalenderjahr vor Lieferbeginn<br/>13015|Bedingung||
|-|-|-|-|-|-|-|
|SG10 DTM \*\*2379\*\*|\*\*102\*\* CCYYMMDD||X (\[91] ∧ \[580])||\[69] Wenn BGM+Z28 vorhanden<br/>\[91] Wenn BGM+Z42 vorhanden<br/>\[578] Hinweis: Wenn es sich um die Übermittlung des Leistungswertes für die Netzentgelte mit Jahresleistungspreissystem handelt.<br/>\[579] Hinweis: Wenn es sich um die Übermittlung des Leistungswertes für die Netzentgelte mit Monatsleistungspreissystem handelt.<br/>\[580] Hinweis: Wenn es sich um die Übermittlung des Leistungswertes für die Netzentgelte mit Tagesleistungspreissystem handelt.<br/>\[581] Hinweis: Wenn es sich um die Übermittlung des Monatsmaximum gemäß WiM handelt.||
||\*\*610\*\* CCYYMM||X (\[69] ∧ \[581]) ⊻ (\[91] ∧ (\[578] ⊻ \[579]))|X|||
|Plausibilisierungshinweis SG10|||||||
|SG10 STS 00035|||Soll (\[92] ⊻ \[93]) ∧ \[126]|Soll (\[92] ⊻ \[93]) ∧ \[126]||\[92] Wenn SG10 QTY DE6063 mit Wert 67 vorhanden<br/>\[93] Wenn SG10 QTY DE6063 mit Wert 220 vorhanden<br/>\[126] wenn Plausibilisierungshinweise vorliegen|
|SG10 STS \*\*9015\*\*|\*\*Z33\*\*|Plausibilisierungshinweis|X|X|||
|SG10 STS \*\*9013\*\*|\*\*Z83\*\*|Kundenselbstablesung|X \[5P0..1]|X \[5P0..1]|||
||\*\*Z84\*\*|Leerstand|X \[4P0..1] ⊻ \[5P0..1]|X \[4P0..1] ⊻ \[5P0..1]|||
||\*\*Z85\*\*|Realer Zählerüberlauf geprüft|X \[4P0..1] ⊻ \[5P0..1]|X \[4P0..1] ⊻ \[5P0..1]|||
||\*\*Z86\*\*|Plausibel wg. Kontrollablesung|X \[4P0..1] ⊻ \[5P0..1]|X \[4P0..1] ⊻ \[5P0..1]|||
||\*\*Z87\*\*|Plausibel wg. Kundenhinweis|X \[4P0..1] ⊻ \[5P0..1]|X \[4P0..1] ⊻ \[5P0..1]|||
||\*\*ZC3\*\*|Austausch des Ersatzwertes|X \[4P0..1] ⊻ \[5P0..1]|X \[4P0..1] ⊻ \[5P0..1]|||
|Ersatzwertbildungsverfahren SG10|||||||
|SG10 STS 00036|||Muss \[92]|Muss \[92]|Muss \[92]|\[92] Wenn SG10 QTY DE6063 mit Wert 67 vorhanden|
|SG10 STS \*\*9015\*\*|\*\*Z32\*\*|Ersatzwertbildungsverfahren|X|X|X||


Version: 3.1f 30.09.2025 Seite 39 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|EDIFACT Struktur|Beschreibung|Energiemenge (Strom)|Energiemenge u. Leistungsmax. (Strom)|Arbeit Leistungsmax. Kalenderjahr vor Lieferbeginn|Bedingung|
|-|-|-|-|-|-|
||Prüfidentifikator|13019|13016|13015||
|SG10 STS \*\*9013\*\*|\*\*Z88\*\* Vergleichsmessung (geeicht)|X \[4P0..1]|X \[4P0..1]|X \[4P0..1]|\[46] Wenn Wert in SG6 LOC+172 DE3225 genau 11 Stellen<br/>\[568] Hinweis: Verwendung ist nur zulässig, wenn es sich um 1:n Beziehung zwischen Markt- und Messlokation handelt und auf Ebene der Messlokation unterschiedliche Ersatzwertbildungsverfahren verwendet und kommuniziert wurden.|
||\*\*Z89\*\* Vergleichsmessung (nicht geeicht)|X \[4P0..1]|X \[4P0..1]|X \[4P0..1]||
||\*\*Z92\*\* Interpolation|X \[4P0..1]|X \[4P0..1]|X \[4P0..1]||
||\*\*ZJ2\*\* Statistische Methode|X \[4P0..1]|X \[4P0..1]|X \[4P0..1]||
||\*\*ZS0\*\* Ersatzwertbildungsverfahren gemäß Angaben auf Ebene der Messlokation|X \[46] ∧ \[568]|X \[46] ∧ \[568]|||
|\*\*Korrekturgrund\*\*||||||
|\*\*SG10\*\*||||||
|SG10 STS 00037||Soll \[127] ∧ \[541]|Soll \[127] ∧ \[541]||\[127] wenn ein Korrekturgrund anzugeben ist \[541] Hinweis: Ein Korrekturgrund ist anzugeben, wenn:<br/>1. ein bereits an den MP übermittelter vorläufiger Wert nach Stornierung durch einen Ersatzwert ersetzt wird, oder<br/>2. ein bereits an den MP übermittelter Ersatzwert nach Stornierung durch einen Ersatzwert ersetzt wird, oder<br/>3. ein bereits an den MP übermittelter wahrer Wert nach Stornierung durch einen Ersatzwert ersetzt wird, oder<br/>4. ein bereits an den MP übermittelter wahrer Wert nach Stornierung durch einen wahren Wert ersetzt wird.|
|SG10 STS \*\*9015\*\*|\*\*Z34\*\* Korrekturgrund|X|X|||


Version: 3.1f 30.09.2025 Seite 40 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|EDIFACT Struktur||Beschreibung<br/>Prüfidentifikator|Energiemenge (Strom)<br/>13019|Energiemenge u. Leistungsmax. (Strom)<br/>13016|Arbeit Leistungsmax. Kalenderjahr vor Lieferbeginn<br/>13015|Bedingung|
|-|-|-|-|-|-|-|
|SG10 STS \*\*9013\*\*||\*\*Z74\*\* kein Zugang|X \[4P0..1]|X \[4P0..1]|||
|||\*\*Z75\*\* Kommunikationsstörung|X \[4P0..1]|X \[4P0..1]|||
|||\*\*Z76\*\* Netzausfall|X \[4P0..1]|X \[4P0..1]|||
|||\*\*Z77\*\* Spannungsausfall|X \[4P0..1]|X \[4P0..1]|||
|||\*\*Z78\*\* Gerätewechsel|X \[4P0..1]|X \[4P0..1]|||
|||\*\*Z79\*\* Kalibrierung|X \[4P0..1]|X \[4P0..1]|||
|||\*\*Z80\*\* Gerät arbeitet außerhalb der Betriebsbedingungen|X \[4P0..1]|X \[4P0..1]|||
|||\*\*Z81\*\* Messeinrichtung gestört/defekt|X \[4P0..1]|X \[4P0..1]|||
|||\*\*Z82\*\* Unsicherheit Messung|X \[4P0..1]|X \[4P0..1]|||
|||\*\*ZA0\*\* Uhrzeit gestellt /Synchronisation|X \[4P0..1]|X \[4P0..1]|||
|||\*\*ZA1\*\* Messwert unplausibel|X \[4P0..1]|X \[4P0..1]|||
|||\*\*ZA3\*\* Falscher Wandlerfaktor|X \[4P0..1] ⊻ \[5P0..1]|X \[4P0..1] ⊻ \[5P0..1]|||
|||\*\*ZA4\*\* Fehlerhafte Ablesung|X \[4P0..1] ⊻ \[5P0..1]|X \[4P0..1] ⊻ \[5P0..1]|||
|||\*\*ZA5\*\* Änderung der Berechnung|X \[4P0..1] ⊻ \[5P0..1]|X \[4P0..1] ⊻ \[5P0..1]|||
|||\*\*ZA6\*\* Umbau der Messlokation|X \[4P0..1] ⊻ \[5P0..1]|X \[4P0..1] ⊻ \[5P0..1]|||
|||\*\*ZA7\*\* Datenbearbeitungsfehler|X \[4P0..1] ⊻ \[5P0..1]|X \[4P0..1] ⊻ \[5P0..1]|||
|||\*\*ZB0\*\* Störung / Defekt Messeinrichtung|X \[4P0..1] ⊻ \[5P0..1]|X \[4P0..1] ⊻ \[5P0..1]|||
|||\*\*ZB9\*\* Änderung Tarifschaltzeiten|X \[4P0..1] ⊻ \[5P0..1]|X \[4P0..1] ⊻ \[5P0..1]|||
|||\*\*ZC2\*\* Tarifschaltgerät defekt|X \[4P0..1] ⊻ \[5P0..1]|X \[4P0..1] ⊻ \[5P0..1]|||
|||\*\*ZC4\*\* Impulswertigkeit nicht ausreichend|X \[4P0..1]|X \[4P0..1]|||
|||\*\*ZJ8\*\* Energiemenge in ungemessenem Zeitintervall|X \[4P0..1]||||
|||\*\*ZJ9\*\* Energiemenge aus dem ungepairten Zeitintervall|X \[4P0..1] ⊻ \[5P0..1]||||
|Grund der Ersatzwertbildung SG10|||||||
|SG10 STS|00038||Muss \[92]|Muss \[92]||\[92] Wenn SG10 QTY DE6063 mit Wert 67 vorhanden|
|SG10 STS \*\*9015\*\*||\*\*Z40\*\* Grund der Ersatzwertbildung|X|X|||


Version: 3.1f 30.09.2025 Seite 41 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|EDIFACT Struktur|Beschreibung|Energiemenge (Strom)|Energiemenge u. Leistungsmax. (Strom)|Arbeit Leistungsmax. Kalenderjahr vor Lieferbeginn|Bedingung|
|-|-|-|-|-|-|
||Prüfidentifikator|13019|13016|13015||
|SG10 STS 9013|Z74 kein Zugang|X \[4P0..1]|X \[4P0..1]||\[46] Wenn Wert in SG6 LOC+172 DE3225 genau 11 Stellen<br/>\[570] Hinweis: Verwendung ist nur zulässig, wenn es sich um 1:n Beziehung zwischen Markt- und Messlokation handelt und auf Ebene der Messlokation unterschiedliche Gründe für die Ersatzwertbildung vorliegen und kommuniziert wurden.|
||Z75 Kommunikationsstörung|X \[4P0..1]|X \[4P0..1]|||
||Z76 Netzausfall|X \[4P0..1]|X \[4P0..1]|||
||Z77 Spannungsausfall|X \[4P0..1]|X \[4P0..1]|||
||Z78 Gerätewechsel|X \[4P0..1]|X \[4P0..1]|||
||Z79 Kalibrierung|X \[4P0..1]|X \[4P0..1]|||
||Z80 Gerät arbeitet außerhalb der Betriebsbedingungen|X \[4P0..1]|X \[4P0..1]|||
||Z81 Messeinrichtung gestört/defekt|X \[4P0..1]|X \[4P0..1]|||
||Z82 Unsicherheit Messung|X \[4P0..1]|X \[4P0..1]|||
||ZA0 Uhrzeit gestellt /Synchronisation|X \[4P0..1]|X \[4P0..1]|||
||ZA1 Messwert unplausibel|X \[4P0..1]|X \[4P0..1]|||
||ZA3 Falscher Wandlerfaktor|X \[4P0..1]|X \[4P0..1]|||
||ZA4 Fehlerhafte Ablesung|X \[4P0..1]|X \[4P0..1]|||
||ZA5 Änderung der Berechnung|X \[4P0..1]|X \[4P0..1]|||
||ZA6 Umbau der Messlokation|X \[4P0..1]|X \[4P0..1]|||
||ZA7 Datenbearbeitungsfehler|X \[4P0..1]|X \[4P0..1]|||
||ZB0 Störung / Defekt Messeinrichtung|X \[4P0..1]|X \[4P0..1]|||
||ZB9 Änderung Tarifschaltzeiten|X \[4P0..1]|X \[4P0..1]|||
||ZC2 Tarifschaltgerät defekt|X \[4P0..1]|X \[4P0..1]|||
||ZC4 Impulswertigkeit nicht ausreichend|X \[4P0..1]|X \[4P0..1]|||
||ZS9 Grund der Ersatzwertbildung gemäß Angaben auf Ebene der Messlokation|X \[46] ∧ \[570]|X \[46] ∧ \[570]|||
|Grundlage der Energiemenge SG10||||||
|SG10 STS 00040||Muss \[68] ∧ \[35] ∧ \[46] ∧ \[2003]|||\[35] wenn MP-ID in SG2 NAD+MS in der Rolle MSB<br/>\[46] Wenn Wert in SG6 LOC+172 DE3225 genau 11 Stellen<br/>\[68] Wenn BGM+7 vorhanden<br/>\[2003] Segmentgruppe ist genau zwei Mal je SG9 LIN anzugeben|
|SG10 STS 9015|10 Messklassifizierung|X||||


Version: 3.1f 30.09.2025 Seite 42 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|SG10Nachrichten-Endesegment<br/>UNT<br/>UNT|STS0074|4405||Z36<br/>Z37<br/>Z38<br/>Z39Anzahl der Segmente in einer|Zählerstand zum Beginn der angegebenen Energiemenge vorhanden und kommuniziert<br/>Zählerstand zum Ende der angegebenen Energiemenge vorhanden und kommuniziert<br/>Zählerstand zum Beginn der angegebenen Energiemenge nicht vorhanden da Mengenabgrenzung<br/>Zählerstand zum Ende der angegebenen Energiemenge nicht vorhanden da Mengenabgrenzung00041<br/>X|X \[83] ∨ (\[87] ∧ \[544])<br/>X \[84] ∨ (\[88] ∧ \[545] ∧ \[577])<br/>X \[85]<br/>X \[86]X|Muss<br/>Muss<br/>X|\[83] Wenn in derselben SG9 LIN die Angabe STS+10+Z38 nicht vorhanden\[84] Wenn in derselben SG9 LIN die Angabe STS+10+Z39 nicht vorhanden\[85] Wenn in derselben SG9 LIN die Angabe STS+10+Z36 nicht vorhanden\[86] Wenn in derselben SG9 LIN die Angabe STS+10+Z37 nicht vorhanden\[87] Wenn der Wert in DTM+163 DE2380 derselben SG6 LOC+172 mit demselben Wert in SG9 PIA+5 DE7140 der früheste angegebene Zeitpunkt ist\[88] Wenn der Wert in DTM+164 DE2380 derselben SG6 LOC+172 mit demselben Wert in SG9 PIA+5 DE7140 der späteste angegebene Zeitpunkt ist\[544] Hinweis: Bei einer Mengenaufteilung (z. B. Aufgrund einer Abgrenzung) für SG6 LOC+172 muss für den frühesten angegebenen Zeitpunkt zum Beginn des Zeitintervalls (über alle Wiederholungen der LIN-Segmente derselben SG6 LOC+172 hinweg) zu jeder OBIS-Kennziffer ein Zählerstand vorhanden und kommuniziert sein.\[545] Hinweis: Bei einer Mengenaufteilung (z. B. Aufgrund einer Abgrenzung) für SG6 LOC+172 muss für den spätesten angegebenen Zeitpunkt zum Ende des Zeitintervalls (über alle Wiederholungen der LIN-Segmente derselben SG6 LOC+172 hinweg) zu jeder OBIS-Kennziffer ein Zählerstand vorhanden und kommuniziert sein.\[577] Hinweis: Dieser Code ist auch zu verwenden, wenn aufgrund der Beendigung einer Messlokation (Stilllegung) die Beendigung der Marktlokation (Stilllegung) zu unterschiedlichen Zeitpunkten erfolgt, das heißt die Beendigung der Messlokation vor der Beendigung der Marktlokation erfolgt. Die Energiemenge ist bis zum Endezeitpunkt der Marklokation zu übermitteln, wenngleich der letzte Zählerstand der Messlokation zu einem früheren Zeitpunkt liegt.Muss<br/>Muss|Muss<br/>Muss|
|-|-|-|-|-|-|-|-|-|-|


Version: 3.1f 30.09.2025 Seite 43 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|EDIFACT Struktur|Beschreibung<br/>Prüfidentifikator|Energiemenge (Strom)<br/>13019|Energiemenge u. Leistungsmax. (Strom)<br/>13016|Arbeit Leistungsmax. Kalenderjahr vor Lieferbeginn<br/>13015|Bedingung||
|-|-|-|-|-|-|-|
||Nachricht||||||
|UNT|0062|Nachrichten-Referenznummer|X|X|X||
|Nutzdaten-Endesegment|||||||
|UNZ|00042||Muss|Muss|Muss||
|UNZ|0036|Datenaustauschzähler|X|X|X||
|UNZ|0020|Datenaustauschreferenz|X|X|X||


Version: 3.1f 30.09.2025 Seite 44 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

### 6.3.8 Anwendungsübersicht Grundlage POG-Ermittlung

|EDIFACT Struktur|Beschreibung<br/>Prüfidentifikator|Grundlage POG-Ermittlung<br/>13028|Bedingung||||
|-|-|-|-|-|-|-|
|Nutzdaten-Kopfsegment|||Muss||||
|\*\*UNB\*\*|00002|||Muss|||
|UNB|0001|\*\*UNOC\*\*|UN/ECE-Zeichensatz C|X|||
|UNB|0002|\*\*3\*\*|Version 3|X|||
|UNB|0004|MP-ID Absender|X||||
|UNB|0007|\*\*14\*\*|GS1|X|||
||\*\*500\*\*|DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)|X||||
|UNB|0010|MP-ID Empfänger|X||||
|UNB|0007|\*\*14\*\*|GS1|X|||
||\*\*500\*\*|DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)|X||||
|UNB|0017|Datum der Erstellung|X||||
|UNB|0019|Uhrzeit der Erstellung|X||||
|UNB|0020|Datenaustauschreferenz|X \[918]|\[918] Format: Zeichen aus dem über UNOC definierten Zeichensatz, wobei von den Buchstaben nur Großbuchstaben erlaubt sind.|||
|UNB|0026|\*\*EM\*\*|Energiemenge|X|||
|Nachrichtenkopfsegment|||Muss||||
|\*\*UNH\*\*|00003|||Muss|||
|UNH|0062|Nachrichten-Referenznummer|X||||
|UNH|0065|\*\*MSCON\*\* Bericht über den Verbrauch messbarer Dienstleistungen|X||||
||\*\*S\*\*||||||
|UNH|0052|\*\*D\*\*|Entwurfs-Version|X|||
|UNH|0054|\*\*04B\*\*|Ausgabe 2004 - B|X|||
|UNH|0051|\*\*UN\*\*|UN/CEFACT|X|||
|UNH|0057|\*\*2.4c\*\*|Versionsnummer der zugrundeliegenden BDEW-Nachrichtenbeschreibung|X|||
|Beginn der Nachricht|||Muss||||
|\*\*BGM\*\*|00004|||Muss|||
|BGM|1001|\*\*Z85\*\*|Grundlage POG-Ermittlung|X|||
|BGM|1004|Dokumentennummer|X||||
|BGM|1225|\*\*9\*\*|Original|X|||
|Nachrichtendatum|||Muss||||
|\*\*DTM\*\*|00005|||Muss|||
|DTM|2005|\*\*137\*\*|Dokumenten-/Nachrichtendatum/-zeit|X|||
|DTM|2380|Datum oder Uhrzeit oder Zeitspanne, Wert|X \[931] \[494]|\[494] Das hier genannte Datum muss der Zeitpunkt sein, zu dem das Dokument erstellt wurde, oder ein Zeitpunkt, der davor liegt.<br/>\[931] Format: ZZZ = +00|||
|DTM|2379|\*\*303\*\*|CCYYMMDDHHMMZZZ|X|||
|Prüfidentifikator|||Muss||||
|\*\*SG1\*\*|||Muss||||
|\*\*SG1\*\*|\*\*RFF\*\*|00009|||Muss||
|SG1|RFF|1153|\*\*Z13\*\*|Prüfidentifikator|X||
|SG1|RFF|1154|\*\*13028\*\*|Grundlage POG-Ermittlung|X||
|MP-ID Absender|||Muss||||
|\*\*SG2\*\*|||Muss||||
|\*\*SG2\*\*|\*\*NAD\*\*|00010|||Muss||
|SG2|NAD|3035|\*\*MS\*\*|Dokumenten-/Nachrichtenaussteller bzw. -absender|X||
|SG2|NAD|3039|MP-ID|X \[117]|\[117] Nur MP-ID aus Sparte Strom||


Version: 3.1f 30.09.2025 Seite 45 von 158

MSCONS Anwendungshandbuch
![edi@energy. Datenformate Strom & Gas](image)

|EDIFACT Struktur||Beschreibung<br/>Prüfidentifikator|Grundlage POG-Ermittlung<br/>13028|Bedingung|||
|-|-|-|-|-|-|-|
|SG2|NAD|3055|9|GS1|X||
||||293|DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)|X||
|Ansprechpartner|||||||
|SG4||||Kann|||
|SG4|CTA||00011||Muss||
|SG4|CTA|3139|IC|Informationsstelle|X||
|SG4|CTA|3412|Abteilung oder Bearbeiter|X|||
|Kommunikationsverbindung|||||||
|SG4|||||||
|SG4|COM||00012||Muss||
|SG4|COM|3148|Kommunikationsadresse, Identifikation|X (((\[939] \[142]) ∨ (\[940] \[143])) ∧ \[576])|\[142] wenn im DE3155 in demselben COM der Code EM vorhanden ist<br/>\[143] wenn im DE3155 in demselben COM der Code TE / FX / AJ / AL vorhanden ist<br/>\[576] Hinweis: Es darf nur eine Information im DE3148 übermittelt werden<br/>\[939] Format: Die Zeichenkette muss die Zeichen @ und . enthalten<br/>\[940] Format: Die Zeichenkette muss mit dem Zeichen + beginnen und danach dürfen nur noch Ziffern folgen||
|SG4|COM|3155|TE|Telefon|X \[1P0..1]||
||||EM|E-Mail|X \[1P0..1]||
||||AJ|weiteres Telefon|X \[1P0..1]||
||||AL|Handy|X \[1P0..1]||
||||FX|Telefax|X \[1P0..1]||
|MP-ID Empfänger|||||||
|SG2||||Muss|||
|SG2|NAD||00013||Muss||
|SG2|NAD|3035|MR|Nachrichtenempfänger|X||
|SG2|NAD|3039|MP-ID|X \[117]|\[117] Nur MP-ID aus Sparte Strom||
|SG2|NAD|3055|9|GS1|X||
||||293|DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)|X||
|Abschnitts-Kontrollsegment|||||||
||UNS||00014||Muss||
||UNS|0081|D|Trennung von Kopf- und Positionsteil|X||
|Name und Adresse|||||||
|SG5||||Muss \[2001]|\[2001] Segmentgruppe ist nur einmal je UNH anzugeben||
|SG5|NAD||00015||Muss||
|SG5|NAD|3035|DP|Lieferanschrift|X||
|Identifikationsangabe|||||||
|SG6||||Muss|||
|SG6|LOC||00017||Muss||
|SG6|LOC|3227|172|Meldepunkt|X||
|SG6|LOC|3225|Bezeichnung|X \[950] \[514]|\[514] Hinweis: Verwendung der ID der Marktlokation<br/>\[950] Format: Marktlokations-ID||
|lfd. Position|||||||
|SG9||||Muss|||
|SG9|LIN||00026||Muss||
|SG9|LIN|1082|Positionsnummer|X \[908]|\[908] Format: Mögliche Werte: 1 bis n||
|Produktidentifikation|||||||
|SG9|||||||
|SG9|PIA||00027||Muss||
|SG9|PIA|4347|5|Produktidentifikation|X||


Version: 3.1f 30.09.2025 Seite 46 von 158

MSCONS Anwendungshandbuch
![edi@energy Datenformate Strom & Gas](image)

|EDIFACT Struktur|Beschreibung<br/>Prüfidentifikator|Grundlage POG-Ermittlung<br/>13028|Bedingung|||
|-|-|-|-|-|-|
|SG9|PIA|7140|Medium / OBIS-Kennzahl|X \[501]|\[501] Hinweis: Es sind nur die Werte erlaubt, die in der EDI\@Energy Codeliste der OBIS-Kennzahlen und Medien mit dem entsprechenden Prüfidentifikator versehen sind.|
|SG9|PIA|7143|\*\*SRW\*\* OBIS-Kennzahl|X||
|Mengenangaben||||||
|\*\*SG10\*\*|||\*\*Muss\*\*|||
|SG10|QTY|00028||Muss||
|SG10|QTY|6063|\*\*Z47\*\* Grundlage POG-Ermittlung|X||
|SG10|QTY|6060|Menge|X \[902] ∧ \[906]|\[902] Format: Möglicher Wert: ≥ 0<br/>\[906] Format: max. 3 Nachkommastellen|
|Beginn Messperiode||||||
|\*\*SG10\*\*||||||
|SG10|DTM|00029||Muss||
|SG10|DTM|2005|\*\*163\*\* Verarbeitung, Beginndatum/-zeit|X||
|SG10|DTM|2380|Datum oder Uhrzeit oder Zeitspanne, Wert|X \[UB1] ∧ \[495]|\[495] Der Zeitpunkt muss ≤ dem Wert im DE2380 des DTM+137 sein|
|SG10|DTM|2379|\*\*303\*\* CCYYMMDDHHMMZZZ|X||
|Ende Messperiode||||||
|\*\*SG10\*\*||||||
|SG10|DTM|00030||Muss||
|SG10|DTM|2005|\*\*164\*\* Verarbeitung, Endedatum/-zeit|X||
|SG10|DTM|2380|Datum oder Uhrzeit oder Zeitspanne, Wert|X \[UB1] ∧ \[495]|\[495] Der Zeitpunkt muss ≤ dem Wert im DE2380 des DTM+137 sein|
|SG10|DTM|2379|\*\*303\*\* CCYYMMDDHHMMZZZ|X||
|Nachrichten-Endesegment||||||
|\*\*UNT\*\*|00041||Muss|||
|UNT|0074|Anzahl der Segmente in einer Nachricht|X|||
|UNT|0062|Nachrichten-Referenznummer|X|||
|Nutzdaten-Endesegment||||||
|\*\*UNZ\*\*|00042||Muss|||
|UNZ|0036|Datenaustauschzähler|X|||
|UNZ|0020|Datenaustauschreferenz|X|||


Version: 3.1f 30.09.2025 Seite 47 von 158

MSCONS Anwendungshandbuch
![edi@energy. Datenformate Strom & Gas](image)

## 6.4 Übertragung von Zählerständen und Energiemengen Gas

### 6.4.1 Übertragung von Zählerständen Gas

Tabellenspalte = Zählerstand (Gas) 13002

Dieser Anwendungsfall dient zur Übertragung von Zählerständen in der Sparte Gas.

Die Übertragung von Zählerstand, Abrechnungsbrennwert und Zustandszahl bei Gaszählern erfolgt gemäß G685-Beiblatt 1. Abrechnungsbrennwert und Zustandszahl werden, über die entsprechenden OBIS-Kennzahlen identifiziert, als abrechnungsfähiger Wert (SG10 QTY DE6063 = 220 – wahrer Wert – Abrechnungsbrennwert) in zusätzlichen LIN-Segmenten angegeben.

Bei der Übertragung von Brennwert und Zustandszahl zu einem Zählerstand gilt bezüglich der Zeitpunkts Angabe:

Der Zeitpunkt in SG10 DTM+163 (Beginn Messperiode) zu Brennwert oder Z-Zahl ist identisch mit dem Zeitpunkt in SG10 DTM+7 (Nutzungszeitpunkt) des unmittelbar vorangegangenen (mit dem Marktpartner ausgetauschten) Zählerstandes der betroffenen Messlokation, wenn es eine zeitpunktbezogene Ablesung war (z. B. Einzug, Einbau).

Der Zeitpunkt in SG10 DTM+163 (Beginn Messperiode) zu Brennwert oder Z-Zahl ist identisch mit dem Zeitpunkt in SG10 DTM+7 (Nutzungszeitpunkt) des unmittelbar vorangegangenen (mit dem Marktpartner ausgetauschten) Zählerstandes der betroffenen Messlokation, wenn es eine zeitraumbezogene Ablesung war (z. B. Turnus, Zwischenablesung).

Der Zeitpunkt in SG10 DTM+164 (Ende Messperiode) zu Brennwert oder Z-Zahl ist identisch mit dem Zeitpunkt in SG10 DTM+7 (Nutzungszeitpunkt) des in dieser Nachricht übermittelten Zählerstandes der betroffenen Messlokation.

Werden Daten vom LF (z. B. aufgrund einer Kundenselbstablesung) oder vom MSB an den NB übertragen, enthalten diese keine Angaben zu Brennwert und Zustandszahl.

Bei Zählerständen aus Betriebsvolumenmessgeräten ist die Zustandszahl anzugeben.

Kommunikationspartner, Identifikationsangabe und Art der Werte für diesen Anwendungsfall:

|Sparte|Kommunikation von|Art der Werte|Identifikationsangabe in SG6 LOC|Anmerkung|
|-|-|-|-|-|
|Gas|MSB an NB|Zählerstand zum Ablesetermin|ID der Messlokation|--|
|Gas|NB an MSB|Zählerstand zum Ablesetermin|ID der Messlokation|--|
|Gas|NB an LF|Zählerstand zum Ablesetermin|ID der Messlokation|--|
|Gas|NB an NB|Zählerstand zum Ablesetermin|ID der Messlokation|--|
|Gas|LF an NB|Zählerstand zum Ablesetermin|ID der Messlokation|--|


### 6.4.2 Übertragung von Energiemengen Gas

Tabellenspalte = Energiemenge (Gas) 13009

Dieser Anwendungsfall dient zur Übertragung von Energiemengen in der Sparte Gas.

Version: 3.1f	30.09.2025	Seite 48 von 158

MSCONS Anwendungshandbuch
![edi@energy. Datenformate Strom & Gas](image)

Für die Übermittlung von Brennwert und Z-Zahl via MSCONS, als Antwort auf eine ORDERS Anforderung sind die Zeitangaben aus der ORDERS (SG29 DTM Messperiodenanfang (163) und -ende (164)) als Ablesetermine im Sinne G685 Beiblatt 1 zu interpretieren. Somit sind genau jene Werte für Brennwert und Z-Zahl zu übertragen, mit welchen die Energiemenge im angegebenen Zeitraum berechnet werden kann. Der Empfänger ist somit nicht auf die Berechnungslogik des Netzbetreibers angewiesen.

Kommunikationspartner, Identifikationsangabe und Art der Werte für diesen Anwendungsfall:

|Sparte|Kommunikation von|Art der Werte|Identifikationsangabe in SG6 LOC|Anmerkung|
|-|-|-|-|-|
|Gas|NB an LF|Energiemenge beliebiger Zeitraum|ID der Marktlokation|für die Übermittlung der Energiemenge im Zeitintervall zwischen zwei Messwerten und für rechnerisch ermittelte Messwerte|
|Gas|NB an LF|Marktlokation ohne Messlokation|ID der Marktlokation|für rechnerisch ermittelte Messwerte|
|Gas|NB an LF|Brennwert und Zustandszahl|ID der Messlokation|Für die Übermittlung von Abrechnungsbrennwert und Z-Zahl für den vom Lieferanten über eine Geschäftsdatenanfrage angeforderten Zeitraum.|
|Gas|NB an LF|Korrekturenergiemenge|ID der Messlokation|Zur Übermittlung der Korrekturenergiemengen im Zeitintervall zwischen zwei Messwerten für rechnerisch ermittelte Messwerte auf Ebene der Messlokation (z. B. bei Zählerdefekt).|


Version: 3.1f 30.09.2025 Seite 49 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

### 6.4.3 Anwendungsübersicht Zählerstand und Energiemengen Gas

|EDIFACT Struktur|Beschreibung<br/>Prüfidentifikator|Zählerstand (Gas)<br/>13002|Energiemenge (Gas)<br/>13009|Bedingung||
|-|-|-|-|-|-|
|Nutzdaten-Kopfsegment||||||
|UNB|00002||Muss|Muss||
|UNB|0001|\*\*UNOC\*\* UN/ECE-Zeichensatz C|X|X||
|UNB|0002|\*\*3\*\* Version 3|X|X||
|UNB|0004|MP-ID Absender|X|X||
|UNB|0007|\*\*14\*\* GS1<br/>\*\*502\*\* DE, DVGW Service & Consult GmbH|X<br/>X|X<br/>X||
|UNB|0010|MP-ID Empfänger|X|X||
|UNB|0007|\*\*14\*\* GS1<br/>\*\*502\*\* DE, DVGW Service & Consult GmbH|X<br/>X|X<br/>X||
|UNB|0017|Datum der Erstellung|X|X||
|UNB|0019|Uhrzeit der Erstellung|X|X||
|UNB|0020|Datenaustauschreferenz|X \[918]|X \[918]|\[918] Format: Zeichen aus dem über UNOC definierten Zeichensatz, wobei von den Buchstaben nur Großbuchstaben erlaubt sind.|
|UNB|0026|\*\*EM\*\* Energiemenge<br/>\*\*VL\*\* Verrechnungsliste, Zählerstand|<br/>X|X<br/>||
|Nachrichtenkopfsegment||||||
|UNH|00003||Muss|Muss||
|UNH|0062|Nachrichten-Referenznummer|X|X||
|UNH|0065|\*\*MSCON\*\* Bericht über den<br/>\*\*S\*\* Verbrauch messbarer Dienstleistungen|X|X||
|UNH|0052|\*\*D\*\* Entwurfs-Version|X|X||
|UNH|0054|\*\*04B\*\* Ausgabe 2004 - B|X|X||
|UNH|0051|\*\*UN\*\* UN/CEFACT|X|X||
|UNH|0057|\*\*2.4c\*\* Versionsnummer der zugrundeliegenden BDEW-Nachrichtenbeschreibung|X|X||
|Beginn der Nachricht||||||
|BGM|00004||Muss|Muss||
|BGM|1001|\*\*7\*\* Prozessdatenbericht|X|X||
|BGM|1004|Dokumentennummer|X|X||
|BGM|1225|\*\*9\*\* Original|X|X||
|Nachrichtendatum||||||
|DTM|00005||Muss|Muss||
|DTM|2005|\*\*137\*\* Dokumenten-/Nachrichtendatum/-zeit|X|X||
|DTM|2380|Datum oder Uhrzeit oder Zeitspanne, Wert|X \[931] \[494]|X \[931] \[494]|\[494] Das hier genannte Datum muss der Zeitpunkt sein, zu dem das Dokument erstellt wurde, oder ein Zeitpunkt, der davor liegt.<br/>\[931] Format: ZZZ = +00|
|DTM|2379|\*\*303\*\* CCYYMMDDHHMMZZZ|X|X||
|Referenzangaben||||||


Version: 3.1f 30.09.2025 Seite 50 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|EDIFACT Struktur|Beschreibung<br/>Prüfidentifikator|Zählerstand (Gas)<br/>13002|Energiemenge (Gas)<br/>13009|Bedingung||||
|-|-|-|-|-|-|-|-|
|SG1||Soll \[1] ∧ \[538]|Soll \[1] Muss \[32] ∧ \[33] ∧ \[38]|\[1] Sofern per ORDERS angefordert<br/>\[32] wenn MP-ID in SG2 NAD+MS in der Rolle NB<br/>\[33] wenn MP-ID in SG2 NAD+MR in der Rolle LF<br/>\[38] wenn in SG6 LOC+172 DE3225 die ID der Messlokation angegeben ist<br/>\[538] Hinweis: Die Referenz auf die ORDERS ist nur dann anzugeben, wenn diese Werte vom Empfänger auch ursprünglich mittels ORDERS angefragt wurden.||||
|SG1|RFF|00006|Muss|Muss||||
|SG1|RFF|1153|AGI|Beantragungsnummer|X|X||
|SG1|RFF|1154|Referenznummer|X \[529]|X \[529] ⊻ (\[531] ∧ \[509])|\[509] Hinweis: Falls es sich um eine Korrekturenergiemenge handelt, ist hier die Referenz auf die MSCONS anzugeben, in der der Zählerstand vorab übermittelt wurde.<br/>\[529] Hinweis: Wert aus BGM+7 DE1004 der ORDERS mit der die Anforderung von Messwerten erfolgt ist.<br/>\[531] Hinweis: Wert aus BGM+7 DE1004 der MSCONS mit der der Zählerstand übermittelt wurde.||
|Referenz auf vorherige Stammdatenmeldung des MSB||||||||
|SG1||Soll \[129] ∧ \[546]||\[129] Wenn es sich um eine Ablesung aufgrund der Änderung an der Messtechnik oder deren Konfiguration handelt (z.B. Gerätewechsel).<br/>\[546] Hinweis: Eine Referenz auf die Stammdatenänderung des Gerätewechsels ist immer anzugeben, wenn diese dem Sender vorliegt.||||
|SG1|RFF|00008|Muss|||||
|SG1|RFF|1153|Z30|Referenz auf vorherige Stammdatenmeldung des MSB|X|||
|SG1|RFF|1154|Referenz, Identifikation|X \[530]||\[530] Hinweis: Wert aus SG4 IDE+24 DE7402 der UTILMD mit dem der Sender der MSCONS die vorherigen Stammdaten mittels UTILMD übermittelt hat.||
|Prüfidentifikator||||||||
|SG1||Muss|Muss|||||
|SG1|RFF|00009|Muss|Muss||||
|SG1|RFF|1153|Z13|Prüfidentifikator|X|X||
|SG1|RFF|1154|13002|Messw. Zählerstand (Gas)|X|||
|SG1|RFF|1154|13009|Messwert Energiemenge (Gas)||X||
|MP-ID Absender||||||||
|SG2||Muss|Muss|||||
|SG2|NAD|00010|Muss|Muss||||
|SG2|NAD|3035|MS|Dokumenten- /Nachrichtenaussteller bzw. -absender|X|X||
|SG2|NAD|3039|MP-ID|X \[118]|X \[118]|\[118] Nur MP-ID aus Sparte Gas||


Version: 3.1f 30.09.2025 Seite 51 von 158

MSCONS Anwendungshandbuch
![edi@energy. Datenformate Strom & Gas](image)

|EDIFACT Struktur|Beschreibung<br/>Prüfidentifikator|Zählerstand (Gas) 13002<br/>13002|Energiemenge (Gas) 13009<br/>13009|Bedingung||||
|-|-|-|-|-|-|-|-|
|SG2|NAD|3055|9|GS1|X|X||
||332|DE, DVGW Service & Consult GmbH|X|X||||
|\*\*Ansprechpartner\*\*||||||||
|SG4|||Kann|Kann||||
|SG4|CTA||00011||Muss|Muss||
|SG4|CTA|3139|IC|Informationsstelle|X|X||
|SG4|CTA|3412|Abteilung oder Bearbeiter|X|X|||
|\*\*Kommunikationsverbindung\*\*||||||||
|SG4||||||||
|SG4|COM||00012||Muss|Muss||
|SG4|COM|3148|Kommunikationsadresse, Identifikation|X ((\[939] \[142]) ∨ (\[940] \[143])) ∧ \[576]|X ((\[939] \[142]) ∨ (\[940] \[143])) ∧ \[576]|\[142] wenn im DE3155 in demselben COM der Code EM vorhanden ist<br/>\[143] wenn im DE3155 in demselben COM der Code TE / FX / AJ / AL vorhanden ist<br/>\[576] Hinweis: Es darf nur eine Information im DE3148 übermittelt werden<br/>\[939] Format: Die Zeichenkette muss die Zeichen @ und . enthalten<br/>\[940] Format: Die Zeichenkette muss mit dem Zeichen + beginnen und danach dürfen nur noch Ziffern folgen||
|SG4|COM|3155|TE|Telefon|X \[1P0..1]|X \[1P0..1]||
||EM|E-Mail|X \[1P0..1]|X \[1P0..1]||||
||AJ|weiteres Telefon|X \[1P0..1]|X \[1P0..1]||||
||AL|Handy|X \[1P0..1]|X \[1P0..1]||||
||FX|Telefax|X \[1P0..1]|X \[1P0..1]||||
|\*\*MP-ID Empfänger\*\*||||||||
|SG2|||Muss|Muss||||
|SG2|NAD||00013||Muss|Muss||
|SG2|NAD|3035|MR|Nachrichtenempfänger|X|X||
|SG2|NAD|3039|MP-ID|X \[118]|X \[118]|\[118] Nur MP-ID aus Sparte Gas||
|SG2|NAD|3055|9|GS1|X|X||
||332|DE, DVGW Service & Consult GmbH|X|X||||
|\*\*Abschnitts-Kontrollsegment\*\*||||||||
|UNS||00014||Muss|Muss|||
|UNS|0081|D|Trennung von Kopf- und Positionsteil|X|X|||
|\*\*Name und Adresse\*\*||||||||
|SG5|||Muss \[2001]|Muss \[2001]|\[2001] Segmentgruppe ist nur einmal je UNH anzugeben|||
|SG5|NAD||00015||Muss|Muss||
|SG5|NAD|3035|DP|Lieferanschrift|X|X||
|\*\*Identifikationsangabe\*\*||||||||
|SG6|||Muss|Muss||||
|SG6|LOC||00017||Muss|Muss||
|SG6|LOC|3227|172|Meldepunkt|X|X||


Version: 3.1f 30.09.2025 Seite 52 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|EDIFACT Struktur|Beschreibung<br/>Prüfidentifikator|Zählerstand (Gas)<br/>13002|Energiemenge (Gas)<br/>13009|Bedingung|
|-|-|-|-|-|
|SG6 LOC 3225|Bezeichnung|X \[951] \[510]|X (\[951] \[510] ∧ (\[522] ∨ \[524])) ∨ (\[950] \[514] ∧ (\[523] ∨ \[525]))|\[510] Hinweis: Verwendung der ID der Messlokation<br/>\[514] Hinweis: Verwendung der ID der Marktlokation<br/>\[522] Hinweis: Nur für die Übermittlung der Korrekturenergiemengen im Zeitintervall zwischen zwei Messwerten.<br/>\[523] Hinweis: Nur für die Übermittlung der Energiemenge im Zeitintervall zwischen zwei Messwerten vor der Netznutzungsabrechnung.<br/>\[524] Hinweis: Nur, wenn es sich um die Übermittlung von Abrechnungsbrennwert und Z-Zahl für den vom Lieferanten über eine Geschäftsdatenanfrage angeforderten Zeitraum handelt.<br/>\[525] Hinweis: Nur für die Übermittlung der Energiemenge im Zeitintervall für eine Marktlokation ohne Messlokation (Pauschalanlage) wenn eines der Ereignisse aus Kapitel 4.2 eingetreten ist.<br/>\[950] Format: Marktlokations-ID<br/>\[951] Format: Zählpunktbezeichnung|
|Gerätenummer|||||
|SG7||Muss|||
|SG7 RFF 00023||Muss|||
|SG7 RFF 1153|MG Gerätenummer|X|||
|SG7 RFF 1154|Gerätenummer|X|||
|lfd. Position|||||
|SG9||Muss|Muss||
|SG9 LIN 00026||Muss|Muss||
|SG9 LIN 1082|Positionsnummer|X \[908]|X \[908]|\[908] Format: Mögliche Werte: 1 bis n|
|Produktidentifikation|||||
|SG9|||||
|SG9 PIA 00027||Muss|Muss||
|SG9 PIA 4347|5 Produktidentifikation|X|X||
|SG9 PIA 7140|Medium / OBIS-Kennzahl|X \[501]|X \[51] ∧ \[501]|\[51] Wenn SG9 PIA+5+7-0?:33.86.0 vorhanden ist, darf mittels Wiederholung SG9 LIN in derselben Nachricht das SG9 PIA+5+7-0?:52.0.22/7-0?:54.0.16/7-0?:54.0.20/7-0?:54.0.22 nicht mehr angegeben werden<br/>\[501] Hinweis: Es sind nur die Werte erlaubt, die in der EDI\@Energy Codeliste der OBIS-Kennzahlen und Medien mit dem entsprechenden Prüfidentifikator versehen sind.|
|SG9 PIA 7143|SRW OBIS-Kennzahl|X|X||
|Mengenangaben|||||
|SG10||Muss|Muss||
|SG10 QTY 00028||Muss|Muss||


Version: 3.1f 30.09.2025 Seite 53 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|EDIFACT Struktur|Beschreibung|Zählerstand (Gas) 13002|Energiemenge (Gas) 13009|Bedingung||
|-|-|-|-|-|-|
|Prüfidentifikator||||||
|SG10 QTY 6063|220|Wahrer Wert|X|X|\[11] Wenn SG9 PIA+5+7-0?:52.0.22/7-0?:54.0.16/7-0?:54.0.20/7-0?:54.0.22<br/>\[12] Wenn nicht SG9 PIA+5+7-0?:52.0.22/7-0?:54.0.16/7-0?:54.0.20/7-0?:54.0.22<br/>\[32] wenn MP-ID in SG2 NAD+MS in der Rolle NB<br/>\[33] wenn MP-ID in SG2 NAD+MR in der Rolle LF<br/>\[35] wenn MP-ID in SG2 NAD+MS in der Rolle MSB<br/>\[36] wenn MP-ID in SG2 NAD+MR in der Rolle NB<br/>\[42] Wenn MP-ID in SG2 NAD+MR in der Rolle MSB|
||67|Ersatzwert|X \[32]|X (\[32] ∧ (\[33] ∨ \[36] ∨ \[42]))||
||201|Vorschlagswert|X \[35] ∧ \[36] ∧ \[12]|X (\[35] ∧ (\[33] ∨ \[36]) ∧ \[12])||
||20|Nicht verwendbarer Wert|X \[35] ∧ \[36] ∧ \[12]|X (\[35] ∧ (\[33] ∨ \[36]))||
||187|Prognosewert||X \[32] ∧ \[33] ∧ \[11]||
||Z18|Vorläufiger Wert|X \[32] ∧ \[12]|||
|SG10 QTY 6060|Menge||X (\[902] ∧ \[906]) ∨ (\[902] ∧ \[907] ∧ \[48])|X (\[902] ∧ \[937] ∧ \[46] ∧ \[573]) ∨ (\[902] ∧ \[907] ∧ \[48] ∧ \[62]) ∨ (\[910] ∧ \[906] ∧ \[62])|\[46] Wenn Wert in SG6 LOC+172 DE3225 genau 11 Stellen<br/>\[48] Wenn SG9 PIA+5+7-0?:52.0.22<br/>\[62] Wenn Wert in SG6 LOC+172 DE3225 genau 33 Stellen<br/>\[573] Hinweis: Eine Energiemenge in der Sparte Gas ist gemäß DVGW G685 Arbeitsblatt 4 Kapitel 5.3 auf ganze Kilowattstunden zu runden.<br/>\[902] Format: Möglicher Wert: ≥ 0<br/>\[906] Format: max. 3 Nachkommastellen<br/>\[907] Format: max. 4 Nachkommastellen<br/>\[910] Format: Möglicher Wert: < 0 oder ≥ 0<br/>\[937] Format: keine Nachkommastelle|
|Beginn Messperiode||||||
|SG10||||||
|SG10 DTM 00029|||Muss \[11]|Muss|\[11] Wenn SG9 PIA+5+7-0?:52.0.22/7-0?:54.0.16/7-0?:54.0.20/7-0?:54.0.22|
|SG10 DTM 2005|163|Verarbeitung, Beginndatum/-zeit|X|X||
|SG10 DTM 2380|Datum oder Uhrzeit oder Zeitspanne, Wert|X \[UB2]|X (((\[UB2] ∧ \[119]) ⊻ (\[931] ∧ \[38])) ∧ \[495])|\[38] wenn in SG6 LOC+172 DE3225 die ID der Messlokation angegeben ist<br/>\[119] wenn in SG6 LOC+172 DE3225 die ID der Marktlokation angegeben ist<br/>\[495] Der Zeitpunkt muss ≤ dem Wert im DE2380 des DTM+137 sein<br/>\[931] Format: ZZZ = +00||
|SG10 DTM 2379|303|CCYYMMDDHHMMZZZ|X|X||
|Ende Messperiode||||||
|SG10||||||
|SG10 DTM 00030|||Muss \[11]|Muss|\[11] Wenn SG9 PIA+5+7-0?:52.0.22/7-0?:54.0.16/7-0?:54.0.20/7-0?:54.0.22|
|SG10 DTM 2005|164|Verarbeitung, Endedatum/-zeit|X|X||


Version: 3.1f    30.09.2025    Seite 54 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|EDIFACT Struktur|Beschreibung<br/>Prüfidentifikator|Zählerstand (Gas)<br/>13002|Energiemenge (Gas)<br/>13009|Bedingung|
|-|-|-|-|-|
|SG10 DTM 2380|Datum oder Uhrzeit oder Zeitspanne, Wert|X \[UB2]|X (((\[UB2] ∧ \[119]) ⊻ (\[931] \[38])) ∧ \[495])|\[38] wenn in SG6 LOC+172 DE3225 die ID der Messlokation angegeben ist<br/>\[119] wenn in SG6 LOC+172 DE3225 die ID der Marktlokation angegeben ist<br/>\[495] Der Zeitpunkt muss ≤ dem Wert im DE2380 des DTM+137 sein<br/>\[931] Format: ZZZ = +00|
|SG10 DTM 2379|303 CCYYMMDDHHMMZZZ|X|X||
|Ablesedatum|||||
|SG10 SG10 DTM 00031||Soll \[12] ∧ \[93] ∧ \[128]||\[12] Wenn nicht SG9 PIA+5+7-0?:52.0.22/7-0?:54.0.16/7-0?:54.0.20/7-0?:54.0.22<br/>\[93] Wenn SG10 QTY DE6063 mit Wert 220 vorhanden<br/>\[128] Wenn es sich um eine Ablesung handelt, welche keine Ablesung aufgrund der Änderung an der Messtechnik oder deren Konfiguration ist (z.B. Kundenablesung).|
|SG10 DTM 2005|9 Bearbeitungs-/Verarbeitungsdatum/-zeit|X|||
|SG10 DTM 2380|Datum oder Uhrzeit oder Zeitspanne, Wert|X (\[931] \[111] ∧ \[495]) ⊻ (\[134] ∧ \[135])||\[111] Wenn SG10 DTM+9 DE2379 in demselben Segment mit Wert 303 vorhanden<br/>\[134] Wenn SG10 DTM+9 DE2379 in demselben Segment mit Wert 102 vorhanden<br/>\[135] Der Wert an der Stelle CCYYMMDD muss ≤ dem Wert an der Stelle CCYYMMDD im DE2380 des DTM+137 sein<br/>\[495] Der Zeitpunkt muss ≤ dem Wert im DE2380 des DTM+137 sein<br/>\[931] Format: ZZZ = +00|
|SG10 DTM 2379|102 CCYYMMDD|X|||
|SG10 DTM 2379|303 CCYYMMDDHHMMZZZ|X|||
|Nutzungszeitpunkt|||||
|SG10 SG10 DTM 00032||Muss \[12]||\[12] Wenn nicht SG9 PIA+5+7-0?:52.0.22/7-0?:54.0.16/7-0?:54.0.20/7-0?:54.0.22|
|SG10 DTM 2005|7 Gültigkeitsdatum/-zeit|X|||


Version: 3.1f 30.09.2025 Seite 55 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|EDIFACT Struktur|Beschreibung<br/>Prüfidentifikator|Zählerstand (Gas)<br/>13002|Energiemenge (Gas)<br/>13009|Bedingung|
|-|-|-|-|-|
|SG10 DTM 2380|Datum oder Uhrzeit oder Zeitspanne, Wert|X \[UB2] ∧ \[495] ∧ (\[130] ∨ \[133])||\[130] Wenn innerhalb desselben LIN-Segments neben diesem Segment (SG10 DTM+7 Nutzungszeitpunkt) noch das SG10 DTM+60 (Ausführungs- / Änderungszeitpunkt) oder das SG10 DTM+9 (Ablesedatum) vorhanden, darf der Wert der Differenz zwischen dem größeren und dem kleineren Zeitpunkt der DTM-Segmente ausschließlich < 24 Stunden sein. Findet zwischen den beiden Zeitpunkten die Sommer/Winter-Zeitumschaltung statt, darf der Wert der Differenz ausschließlich < 25 Stunden sein. Findet zwischen den beiden Zeitpunkten die Winter/Sommer-Zeitumschaltung statt, darf der Wert der Differenz ausschließlich < 23 Stunden sein.<br/>\[133] Wenn innerhalb desselben LIN-Segments neben diesem Segment (SG10 DTM+7 Nutzungszeitpunkt) noch das SG10 DTM+9 (Ablesedatum) mit dem Code 102 im DE2379 vorhanden ist, darf der Wert der Differenz zwischen dem Wert an der Stelle CCYYMMDD des größeren und dem kleineren Zeitpunkt der DTM-Segmente an der Stelle CCYYMMDD ausschließlich 0 oder 1 Tag sein.<br/>\[495] Der Zeitpunkt muss ≤ dem Wert im DE2380 des DTM+137 sein|
|SG10 DTM 2379|303 CCYYMMDDHHMMZZZ|X|||
|Ausführungs- / Änderungszeitpunkt|||||
|SG10|||||
|SG10 DTM 00033||Soll \[12] ∧ \[129]||\[12] Wenn nicht SG9 PIA+5+7-0?:52.0.22/7-0?:54.0.16/7-0?:54.0.20/7-0?:54.0.22<br/>\[129] Wenn es sich um eine Ablesung aufgrund der Änderung an der Messtechnik oder deren Konfiguration handelt (z.B. Gerätewechsel).|
|SG10 DTM 2005|60 Konstruktionsänderungsdatum|X|||
|SG10 DTM 2380|Datum oder Uhrzeit oder Zeitspanne, Wert|X \[931] \[495]||\[495] Der Zeitpunkt muss ≤ dem Wert im DE2380 des DTM+137 sein<br/>\[931] Format: ZZZ = +00|
|SG10 DTM 2379|303 CCYYMMDDHHMMZZZ|X|||
|Plausibilisierungshinweis|||||
|SG10|||||
|SG10 STS 00035||Soll (\[92] ⊻ \[93] ⊻ \[94]) ∧ \[126]|Soll (\[92] ⊻ \[93] ⊻ \[94]) ∧ \[126]|\[92] Wenn SG10 QTY DE6063 mit Wert 67 vorhanden<br/>\[93] Wenn SG10 QTY DE6063 mit Wert 220 vorhanden<br/>\[94] Wenn SG10 QTY DE6063 mit Wert 201 vorhanden<br/>\[126] wenn Plausibilisierungshinweise vorliegen|
|SG10 STS 9015|Z33 Plausibilisierungshinweis|X|X||


Version: 3.1f 30.09.2025 Seite 56 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|EDIFACT Struktur|Beschreibung|Zählerstand (Gas)|Energiemenge (Gas)|Bedingung||
|-|-|-|-|-|-|
||Prüfidentifikator|13002|13009|||
|SG10 STS \*\*9013\*\*|\*\*Z83\*\*|Kundenselbstablesung|X \[5P0..1]|X \[5P0..1]||
||\*\*Z84\*\*|Leerstand|X \[4P0..1] ⊻ \[5P0..1] ⊻ \[6P0..1]|X \[4P0..1] ⊻ \[5P0..1] ⊻ \[6P0..1]||
||\*\*Z85\*\*|Realer Zählerüberlauf geprüft|X \[4P0..1] ⊻ \[5P0..1] ⊻ \[6P0..1]|X \[4P0..1] ⊻ \[5P0..1] ⊻ \[6P0..1]||
||\*\*Z86\*\*|Plausibel wg. Kontrollablesung|X \[4P0..1] ⊻ \[5P0..1] ⊻ \[6P0..1]|X \[4P0..1] ⊻ \[5P0..1] ⊻ \[6P0..1]||
||\*\*Z87\*\*|Plausibel wg. Kundenhinweis|X \[4P0..1] ⊻ \[5P0..1] ⊻ \[6P0..1]|X \[4P0..1] ⊻ \[5P0..1] ⊻ \[6P0..1]||
||\*\*ZC3\*\*|Austausch des Ersatzwertes|X \[5P0..1]|X \[5P0..1]||
||\*\*ZR5\*\*|Rechenwert|X \[4P0..1] ⊻ \[5P0..1] ⊻ \[6P0..1]|X \[4P0..1] ⊻ \[5P0..1] ⊻ \[6P0..1]||
|Ersatzwertbildungsverfahren||||||
|\*\*SG10\*\*||||||
|SG10 STS 00036|||Muss \[92] ⊻ \[94]|Muss \[92] ⊻ \[94]|\[92] Wenn SG10 QTY DE6063 mit Wert 67 vorhanden<br/>\[94] Wenn SG10 QTY DE6063 mit Wert 201 vorhanden|
|SG10 STS \*\*9015\*\*|\*\*Z32\*\*|Ersatzwertbildungsverfahren|X|X||
|SG10 STS \*\*9013\*\*|\*\*Z89\*\*|Vergleichsmessung (nicht geeicht)|X \[4P0..1] ⊻ \[6P0..1]|X \[4P0..1] ⊻ \[6P0..1]|\[46] Wenn Wert in SG6 LOC+172 DE3225 genau 11 Stellen<br/>\[568] Hinweis: Verwendung ist nur zulässig, wenn es sich um 1:n Beziehung zwischen Markt- und Messlokation handelt und auf Ebene der Messlokation unterschiedliche Ersatzwertbildungsverfahren verwendet und kommuniziert wurden.|
||\*\*Z90\*\*|Messwertnachbildung aus geeichten Werten|X \[4P0..1] ⊻ \[6P0..1]|X \[4P0..1] ⊻ \[6P0..1]||
||\*\*Z91\*\*|Messwertnachbildung aus nicht geeichten Werten|X \[4P0..1] ⊻ \[6P0..1]|X \[4P0..1] ⊻ \[6P0..1]||
||\*\*Z92\*\*|Interpolation|X \[4P0..1] ⊻ \[6P0..1]|X \[4P0..1] ⊻ \[6P0..1]||
||\*\*Z93\*\*|Haltewert|X \[4P0..1] ⊻ \[6P0..1]|X \[4P0..1] ⊻ \[6P0..1]||
||\*\*Z94\*\*|Bilanzierung Netzabschnitt|X \[4P0..1] ⊻ \[6P0..1]|X \[4P0..1] ⊻ \[6P0..1]||
||\*\*Z95\*\*|Historische Messwerte|X \[4P0..1] ⊻ \[6P0..1]|X \[4P0..1] ⊻ \[6P0..1]||
||\*\*ZQ8\*\*|Aufteilung|X \[4P0..1] ⊻ \[6P0..1]|X \[4P0..1] ⊻ \[6P0..1]||
||\*\*ZQ9\*\*|Verwendung von Werten des Störmengenzählwerks|X \[4P0..1] ⊻ \[6P0..1]|X \[4P0..1] ⊻ \[6P0..1]||
||\*\*ZR0\*\*|Umgangs- und Korrekturmengen|X \[4P0..1] ⊻ \[6P0..1]|X \[4P0..1] ⊻ \[6P0..1]||
||\*\*ZS0\*\*|Ersatzwertbildungsverfahren gemäß Angaben auf Ebene der Messlokation||X \[46] ∧ \[568]||
|Korrekturgrund||||||
|\*\*SG10\*\*||||||


Version: 3.1f 30.09.2025 Seite 57 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|EDIFACT Struktur||Beschreibung<br/>Prüfidentifikator|Zählerstand (Gas)<br/>13002|Energiemenge (Gas)<br/>13009|Bedingung|
|-|-|-|-|-|-|
|SG10 STS|00037||Soll \[127] ∧ \[559]|Soll \[127] ∧ \[559]|\[127] wenn ein Korrekturgrund anzugeben ist \[559] Hinweis: Ein Korrekturgrund ist anzugeben, wenn:<br/>1. ein bereits an den MP übermittelter vorläufiger Wert nach Stornierung durch einen Ersatzwert ersetzt wird, oder<br/>2. ein bereits an den MP übermittelter Ersatzwert nach Stornierung durch einen Ersatzwert ersetzt wird, oder<br/>3. ein bereits an den MP übermittelter wahrer Wert nach Stornierung durch einen Ersatzwert ersetzt wird, oder<br/>4. ein bereits an den MP übermittelter wahrer Wert nach Stornierung durch einen wahren Wert ersetzt wird.|
|SG10 STS|9015|\*\*Z34\*\* Korrekturgrund|X|X||


Version: 3.1f	30.09.2025	Seite 58 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|SG10|STS|9013|Z74<br/>Z75<br/>Z76<br/>Z78<br/>Z80<br/>Z81<br/>Z82<br/>Z98<br/>Z99<br/>ZA0<br/>ZA1<br/>ZA4<br/>ZA5<br/>ZA6<br/>ZA7<br/>ZA8<br/>ZA9|kein Zugang<br/>Kommunikationsstörung<br/>Netzausfall<br/>Gerätewechsel<br/>Gerät arbeitet außerhalbder Betriebsbedingungen<br/>Messeinrichtunggestört/defekt<br/>Unsicherheit Messung<br/>BerücksichtigungStörmengenzählwerk<br/>Mengenumwertungunvollständig<br/>Uhrzeit gestellt/Synchronisation<br/>Messwert unplausibel<br/>Fehlerhafte Ablesung<br/>Änderung derBerechnung<br/>Umbau der Messlokation<br/>Datenbearbeitungsfehler<br/>Brennwertkorrektur<br/>Z-Zahl-Korrektur|X \[4P0..1] ⊻\[6P0..1] ⊻\[7P0..1] ⊻\[8P0..1]<br/>X \[4P0..1] ⊻\[6P0..1] ⊻\[7P0..1] ⊻\[8P0..1]<br/>X \[4P0..1] ⊻\[6P0..1] ⊻\[7P0..1] ⊻\[8P0..1]<br/>X \[4P0..1] ⊻\[6P0..1] ⊻\[7P0..1] ⊻\[8P0..1]<br/>X \[4P0..1] ⊻\[6P0..1] ⊻\[7P0..1] ⊻\[8P0..1]<br/>X \[4P0..1] ⊻\[6P0..1] ⊻\[7P0..1] ⊻\[8P0..1]<br/>X \[4P0..1] ⊻\[6P0..1] ⊻\[7P0..1] ⊻\[8P0..1]<br/>X \[4P0..1] ⊻\[6P0..1]<br/>X \[6P0..1] ⊻\[7P0..1] ⊻\[8P0..1]<br/>X \[4P0..1] ⊻\[6P0..1] ⊻\[7P0..1] ⊻\[8P0..1]<br/>X \[6P0..1] ⊻\[7P0..1] ⊻\[8P0..1]<br/>X \[4P0..1] ⊻\[5P0..1] ⊻\[6P0..1] ⊻\[7P0..1] ⊻\[8P0..1]<br/>X \[4P0..1] ⊻\[5P0..1] ⊻\[6P0..1] ⊻\[7P0..1] ⊻\[8P0..1]<br/>X \[4P0..1] ⊻\[5P0..1] ⊻\[6P0..1] ⊻\[7P0..1] ⊻\[8P0..1]<br/>X \[4P0..1] ⊻\[5P0..1] ⊻\[6P0..1] ⊻\[7P0..1] ⊻\[8P0..1]<br/>X \[4P0..1] ⊻\[5P0..1] ⊻\[6P0..1] ⊻\[7P0..1] ⊻\[8P0..1]<br/>X \[4P0..1] ⊻|X \[4P0..1] ⊻\[6P0..1] ⊻\[7P0..1] ⊻\[8P0..1]<br/>X \[4P0..1] ⊻\[6P0..1] ⊻\[7P0..1] ⊻\[8P0..1]<br/>X \[4P0..1] ⊻\[6P0..1] ⊻\[7P0..1] ⊻\[8P0..1]<br/>X \[4P0..1] ⊻\[6P0..1] ⊻\[7P0..1] ⊻\[8P0..1]<br/>X \[4P0..1] ⊻\[6P0..1] ⊻\[7P0..1] ⊻\[8P0..1]<br/>X \[4P0..1] ⊻\[6P0..1] ⊻\[7P0..1] ⊻\[8P0..1]<br/>X \[4P0..1] ⊻\[6P0..1] ⊻\[7P0..1] ⊻\[8P0..1]<br/>X \[4P0..1] ⊻\[6P0..1]<br/>X \[6P0..1] ⊻\[7P0..1] ⊻\[8P0..1]<br/>X \[4P0..1] ⊻\[6P0..1] ⊻\[7P0..1] ⊻\[8P0..1]<br/>X \[6P0..1] ⊻\[7P0..1] ⊻\[8P0..1]<br/>X \[4P0..1] ⊻\[5P0..1] ⊻\[6P0..1] ⊻\[7P0..1] ⊻\[8P0..1]<br/>X \[4P0..1] ⊻\[5P0..1] ⊻\[6P0..1] ⊻\[7P0..1] ⊻\[8P0..1]<br/>X \[4P0..1] ⊻\[5P0..1] ⊻\[6P0..1] ⊻\[7P0..1] ⊻\[8P0..1]<br/>X \[4P0..1] ⊻\[5P0..1] ⊻\[6P0..1] ⊻\[7P0..1] ⊻\[8P0..1]<br/>X \[4P0..1] ⊻\[5P0..1] ⊻\[6P0..1] ⊻\[7P0..1] ⊻\[8P0..1]<br/>X \[4P0..1] ⊻|
|-|-|-|-|-|-|-|


Version: 3.1f 30.09.2025 Seite 59 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|EDIFACT Struktur|Beschreibung|Zählerstand (Gas) 13002|Energiemenge (Gas) 13009|Bedingung||
|-|-|-|-|-|-|
||Prüfidentifikator|\[5P0..1] ⊻<br/>\[6P0..1] ⊻<br/>\[7P0..1] ⊻<br/>\[8P0..1]|\[5P0..1] ⊻<br/>\[6P0..1] ⊻<br/>\[7P0..1] ⊻<br/>\[8P0..1]|||
||\*\*ZB0\*\* Störung / Defekt Messeinrichtung|X \[4P0..1] ⊻<br/>\[5P0..1] ⊻<br/>\[6P0..1] ⊻<br/>\[7P0..1] ⊻<br/>\[8P0..1]|X \[4P0..1] ⊻<br/>\[5P0..1] ⊻<br/>\[6P0..1] ⊻<br/>\[7P0..1] ⊻<br/>\[8P0..1]|||
||\*\*ZC4\*\* Impulswertigkeit nicht ausreichend|X \[4P0..1] ⊻<br/>\[7P0..1] ⊻<br/>\[8P0..1]|X \[4P0..1] ⊻<br/>\[7P0..1] ⊻<br/>\[8P0..1]|||
||\*\*ZJ9\*\* Energiemenge aus dem ungepairten Zeitintervall||X \[4P0..1] ⊻<br/>\[5P0..1]|||
||\*\*ZR1\*\* Wartungsarbeiten an geeichtem Messgerät|X \[4P0..1] ⊻<br/>\[6P0..1] ⊻<br/>\[7P0..1] ⊻<br/>\[8P0..1]|X \[4P0..1] ⊻<br/>\[6P0..1] ⊻<br/>\[7P0..1] ⊻<br/>\[8P0..1]|||
||\*\*ZR2\*\* gestörte Werte|X \[4P0..1] ⊻<br/>\[6P0..1] ⊻<br/>\[7P0..1] ⊻<br/>\[8P0..1]|X \[4P0..1] ⊻<br/>\[6P0..1] ⊻<br/>\[7P0..1] ⊻<br/>\[8P0..1]|||
||\*\*ZR3\*\* Wartungsarbeiten an eichrechtskonformen Messgeräten|X \[4P0..1] ⊻<br/>\[6P0..1] ⊻<br/>\[7P0..1] ⊻<br/>\[8P0..1]|X \[4P0..1] ⊻<br/>\[6P0..1] ⊻<br/>\[7P0..1] ⊻<br/>\[8P0..1]|||
||\*\*ZR4\*\* Konsistenz- und Synchronprüfung|X \[4P0..1] ⊻<br/>\[6P0..1] ⊻<br/>\[7P0..1] ⊻<br/>\[8P0..1]|X \[4P0..1] ⊻<br/>\[6P0..1] ⊻<br/>\[7P0..1] ⊻<br/>\[8P0..1]|||
|Grund der Ersatzwertbildung||||||
|\*\*SG10\*\*||||||
|SG10 \*\*STS\*\*|00038||Muss \[92]|Muss \[92]|\[92] Wenn SG10 QTY DE6063 mit Wert 67 vorhanden|
|SG10 \*\*STS\*\* \*\*9015\*\*|\*\*Z40\*\* Grund der Ersatzwertbildung|X|X|||


Version: 3.1f	30.09.2025	Seite 60 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|EDIFACT Struktur|Beschreibung|Zählerstand (Gas) 13002|Energiemenge (Gas) 13009|Bedingung||
|-|-|-|-|-|-|
|SG10 STS 9013|Prüfidentifikator|X \[4P0..1]|X \[4P0..1]|\[46] Wenn Wert in SG6 LOC+172 DE3225 genau 11 Stellen<br/>\[570] Hinweis: Verwendung ist nur zulässig, wenn es sich um 1:n Beziehung zwischen Markt- und Messlokation handelt und auf Ebene der Messlokation unterschiedliche Gründe für die Ersatzwertbildung vorliegen und kommuniziert wurden.||
||Z74|kein Zugang|X \[4P0..1]|X \[4P0..1]||
||Z75|Kommunikationsstörung|X \[4P0..1]|X \[4P0..1]||
||Z76|Netzausfall|X \[4P0..1]|X \[4P0..1]||
||Z78|Gerätewechsel|X \[4P0..1]|X \[4P0..1]||
||Z80|Gerät arbeitet außerhalb der Betriebsbedingungen|X \[4P0..1]|X \[4P0..1]||
||Z81|Messeinrichtung gestört/defekt|X \[4P0..1]|X \[4P0..1]||
||Z82|Unsicherheit Messung|X \[4P0..1]|X \[4P0..1]||
||Z98|Berücksichtigung Störmengenzählwerk|X \[4P0..1]|X \[4P0..1]||
||Z99|Mengenumwertung unvollständig|X \[4P0..1]|X \[4P0..1]||
||ZA0|Uhrzeit gestellt /Synchronisation|X \[4P0..1]|X \[4P0..1]||
||ZA1|Messwert unplausibel|X \[4P0..1]|X \[4P0..1]||
||ZA4|Fehlerhafte Ablesung|X \[4P0..1]|X \[4P0..1]||
||ZA5|Änderung der Berechnung|X \[4P0..1]|X \[4P0..1]||
||ZA6|Umbau der Messlokation|X \[4P0..1]|X \[4P0..1]||
||ZA7|Datenbearbeitungsfehler|X \[4P0..1]|X \[4P0..1]||
||ZB0|Störung / Defekt Messeinrichtung|X \[4P0..1]|X \[4P0..1]||
||ZC4|Impulswertigkeit nicht ausreichend|X \[4P0..1]|X \[4P0..1]||
||ZR1|Wartungsarbeiten an geeichtem Messgerät|X \[4P0..1]|X \[4P0..1]||
||ZR2|gestörte Werte|X \[4P0..1]|X \[4P0..1]||
||ZR3|Wartungsarbeiten an eichrechtskonformen Messgeräten|X \[4P0..1]|X \[4P0..1]||
||ZR4|Konsistenz- und Synchronprüfung|X \[4P0..1]|X \[4P0..1]||
||ZS9|Grund der Ersatzwertbildung gemäß Angaben auf Ebene der Messlokation||X \[46] ∧ \[570]||
||ZT8|Anforderung in die Vergangenheit, zum angeforderten Zeitpunkt liegt kein Wert vor.|X \[4P0..1]|||
|Gasqualität||||||
|SG10||||||
|SG10 STS 00039||Soll \[97]|Soll \[97]|\[97] Wenn es sich um die Übermittlung eines Wertes aufgrund der Umstellung der Gasqualität handelt||
|SG10 STS 9015|Z31|Gasqualität|X|X||
|SG10 STS 9013|ZG3|Umstellung Gasqualität|X|X||
|Nachrichten-Endesegment||||||
|UNT 00041||Muss|Muss|||
|UNT 0074|Anzahl der Segmente in einer Nachricht|X|X|||
|UNT 0062|Nachrichten-Referenznummer|X|X|||
|Nutzdaten-Endesegment||||||
|UNZ 00042||Muss|Muss|||
|UNZ 0036|Datenaustauschzähler|X|X|||
|UNZ 0020|Datenaustauschreferenz|X|X|||


Version: 3.1f 30.09.2025 Seite 61 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

# 7 Lastgänge

## 7.1 Generelles zur Übertragung von Lastgängen

In SG10 QTY DE6060 wird die Energiemenge in kWh angegeben, d. h. Faktoren (Wandlerfaktor, Brennwert) sind mit einzurechnen.

Liegen für einen innerhalb der Übertragung liegenden Zeitraum keine Werte vor sind gemäß den Prozessvorgaben für nicht vorhandene oder nicht verwendbare Werte entsprechende Ersatz- oder vorläufige Werte zu bilden. Vorliegende „0“-Werte sind zu übermitteln.

In SG10 STS DE9013 lassen sich Zusatzinformationen (Plausibilisierungs-/Störungshinweis, Grund) zum Status (in SG10 QTY DE6063: wahrer Wert, Ersatzwert, ...) der angegebenen Energiemenge angeben.

Für den gesamten Lastgang wird in SG9 PIA DE7140 der Tarif für alle zur OBIS-Kennzahl korrespondierenden Werte definiert. Sollten für einzelne Werte eines Lastganges verschiedene Tarifzuordnungen Verwendung finden, kann dem jeweiligen Wert in SG10 QTY DE6060 über die SG10 STS DE4405 ein eigener Tarif zugewiesen werden.

Sollen Daten von mehreren Meldepunkten in einer Datei übertragen werden, ist die Wiederholung über das UNH-Segment vorzunehmen.

Dies betrifft alle in den Prozessvorgaben vorgesehenen Übertragungsintervalle (täglich, monatlich, beliebiger Zeitraum).

## 7.2 Lastgang Strom

### 7.2.1 Übertragung von Lastgängen Strom

Tabellenspalte = Lastgang Messlokation, Netzkoppelpunkt, Netzlokation 13018

Tabellenspalte = Lastgang Marktlokation, Tranche 13025

Dieser Anwendungsfall dient zur Übertragung eines Lastgangs in der Sparte Strom.

Kommunikationspartner, Identifikationsangabe und Art der Werte für diesen Anwendungsfall Prüfidentifikator: 13018

|Sparte|Kommunikation von|Art der Werte|Identifikationsangabe in SG6 LOC|Anmerkung|
|-|-|-|-|-|
|Strom|MSB an MSB|Turnus: Lastgang für den Vortag bzw. die Vortage|ID der Messlokation|--|
|Strom|MSB an NB|Turnus: Lastgang für den Vortag bzw. die Vortage|Für Zeiträume (Messperiode) bis einschließlich 01.01.2024, 00:00 Uhr:<br/>ID der Messlokation<br/>Wenn der gemessene Lastgang der Messlokation nicht dem Lastgang der Marktlokation 1:1 entspricht (z. B. Summierung, Berücksichtigung Trafoverluste) dann ist der/die gemessene/n Lastgang/Lastgänge mit der ID der Messlokation/en und der errech-|Wie bisher ist bei allen Lastgängen der Wandlerfaktor bei der Übermittlung bereits mit eingerechnet.|


Version: 3.1f 30.09.2025 Seite 62 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|Sparte|Kommunikation von|Art der Werte|Identifikationsangabe in SG6 LOC|Anmerkung||||
|-|-|-|-|-|-|-|-|
||||nete Lastgang mit dem Anwendungsfall 13025 und mit der ID der Marktlokation zu nutzen.<br/><br/>Hinweis:<br/>Wenn es sich um eine 1:1-Beziehung zwischen Messlokation und Marktlokation handelt und der gemessene Lastgang der Messlokation dem Lastgang der Marktlokation 1:1 entspricht, dann ist der Anwendungsfall mit dem Prüfidentifikator 13025 mit der ID der Marktlokation zu nutzen.|||||
||||||Für Zeiträume (Messperiode) ab 01.01.2024, 00:00 Uhr, für den Lastgang Wirkarbeit:<br/>ID der Messlokation<br/>Wenn der gemessene Lastgang der Messlokation nicht dem Lastgang der Marktlokation 1:1 entspricht (z. B. Summierung, Berücksichtigung Trafoverluste) dann ist der/die gemessene/n Lastgang/Lastgänge mit der ID der Messlokation/en und der errechnete Lastgang mit dem Anwendungsfall 13025 und mit der ID der Marktlokation zu nutzen.<br/><br/>Hinweis:<br/>Wenn es sich um eine 1:1-Beziehung zwischen Messlokation und Marktlokation handelt und der gemessene Lastgang der Messlokation dem Lastgang der Marktlokation 1:1 entspricht, dann ist der Anwendungsfall mit dem Prüfidentifikator 13025 mit der ID der Marktlokation zu nutzen.|||
||||||Für Zeiträume (Messperiode) ab 01.01.2024, 00:00 Uhr, für den Lastgang Blindarbeit:<br/>ID der Messlokation<br/>Für den Lastgang Blindarbeit auf Ebene der Messlokation<br/><br/>Hinweis:<br/>Für den Lastgang Blindarbeit auf Ebene der Netzlokation ist ebenfalls der Anwendungsfall mit dem Prüfidentifikator 13018 zu nutzen.|||
||||Strom|MSB an LF|Turnus: Lastgang für den Vortag bzw. die Vortage|Für Zeiträume (Messperiode) bis einschließlich 01.01.2024, 00:00 Uhr:<br/>ID der Messlokation<br/>Wenn der gemessene Lastgang der Messlokation nicht dem Lastgang der Marktlokation 1:1 entspricht (z. B. Summierung, Berücksichtigung Trafoverluste) dann ist der/die gemessene/n Lastgang/Lastgänge mit der ID der Messlokation/en und der errechnete Lastgang mit dem Anwendungsfall 13025 und mit der ID der Marktlokation zu nutzen.|Wie bisher ist bei allen Lastgängen der Wandlerfaktor bei der Übermittlung bereits mit eingerechnet.|


Version: 3.1f 30.09.2025 Seite 63 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|Sparte|Kommunikation von|Art der Werte|Identifikationsangabe in SG6 LOC|Anmerkung|||||
|-|-|-|-|-|-|-|-|-|
||||Hinweis:<br/>Wenn es sich um eine 1:1-Beziehung zwischen Messlokation und Marktlokation handelt und der gemessene Lastgang der Messlokation dem Lastgang der Marktlokation 1:1 entspricht, dann ist der Anwendungsfall mit dem Prüfidentifikator 13025 mit der ID der Marktlokation zu nutzen.<br/><br/>Für Zeiträume (Messperiode) ab 01.01.2024, 00:00 Uhr, für den Lastgang Wirkarbeit:<br/>ID der Messlokation<br/>Wenn der gemessene Lastgang der Messlokation nicht dem Lastgang der Marktlokation 1:1 entspricht (z. B. Summierung, Berücksichtigung Trafoverluste) dann ist der/die gemessene/n Lastgang/Lastgänge mit der ID der Messlokation/en und der errechnete Lastgang mit dem Anwendungsfall 13025 und mit der ID der Marktlokation zu nutzen.<br/>Hinweis:<br/>Wenn es sich um eine 1:1-Beziehung zwischen Messlokation und Marktlokation handelt und der gemessene Lastgang der Messlokation dem Lastgang der Marktlokation 1:1 entspricht, dann ist der Anwendungsfall mit dem Prüfidentifikator 13025 mit der ID der Marktlokation zu nutzen.<br/><br/>Für Zeiträume (Messperiode) ab 01.01.2024, 00:00 Uhr, für den Lastgang Blindarbeit:<br/>ID der Messlokation<br/>Für den Lastgang Blindarbeit auf Ebene der Messlokation<br/>Hinweis:<br/>Für den Lastgang Blindarbeit auf Ebene der Netzlokation ist ebenfalls der Anwendungsfall mit dem Prüfidentifikator 13018 zu nutzen.||||||
||||Strom||NB an NB|Turnus: Lastgang für den Vortag bzw. die Vortage|ID des Netzkoppelpunktes bei Strom|Für die Netzgangzeitreihe|
|Strom|NB an ÜNB|Turnus: Lastgang für den Vortag bzw. die Vortage|ID des Netzkoppelpunktes bei Strom|Für die Netzgangzeitreihe|||||
|Strom|MSB an NB|Lastgang zur Bestellung|ID der Netzlokation|--|||||
|Strom|MSB an LF|Lastgang zur Bestellung|ID der Netzlokation|--|||||


### Kommunikationspartner, Identifikationsangabe und Art der Werte für diesen Anwendungsfall Prüfidentifikator: 13025

|Sparte|Kommunikation von|Art der Werte|Identifikationsangabe in SG6 LOC|Anmerkung|
|-|-|-|-|-|
|Strom|MSB an ÜNB|Turnus: Lastgang für den Vortag bzw. die Vortage|ID der Marktlokation<br/>Existiert eine/mehrere Tranche/n, dann wird auf Ebene der Tran-|--|


Version: 3.1f 30.09.2025 Seite 64 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|Sparte|Kommunikation von|Art der Werte|Identifikationsangabe in SG6 LOC|Anmerkung||
|-|-|-|-|-|-|
|||||che/n der/die zugehörige/n Lastgang/Lastgänge mit der ID der jeweiligen Tranche übermittelt.||
|Strom|NB an RB HKN-R|--|ID der Marktlokation<br/>ID der Tranche|--||
|Strom|MSB an NB|Turnus: Lastgang für den Vortag bzw. die Vortage|ID der Marktlokation<br/>Wenn es sich um eine 1:1-Beziehung zwischen Messlokation und Marktlokation handelt und der gemessene Lastgang der Messlokation dem Lastgang der Marktlokation 1:1 entspricht.<br/><br/>ID der Tranche<br/>Existiert eine/mehrere Tranche/n, dann wird zusätzlich auf Ebene der Tranche/n der/die zugehörige/n Lastgang/Lastgänge mit der ID der jeweiligen Tranche übermittelt.|Wie bisher ist bei allen Lastgängen der Wandlerfaktor bei der Übermittlung bereits mit eingerechnet.||
|Strom|MSB an LF|Turnus: Lastgang für den Vortag bzw. die Vortage|ID der Marktlokation<br/>Wenn es sich um eine 1:1-Beziehung zwischen Messlokation und Marktlokation handelt und der gemessene Lastgang der Messlokation dem Lastgang der Marktlokation 1:1 entspricht.<br/><br/>ID der Tranche<br/>Existiert eine/mehrere Tranche/n, dann wird zusätzlich auf Ebene der Tranche/n der/die zugehörige/n Lastgang/Lastgänge mit der ID der jeweiligen Tranche übermittelt.|Wie bisher ist bei allen Lastgängen der Wandlerfaktor bei der Übermittlung bereits mit eingerechnet.||


Version: 3.1f 30.09.2025 Seite 65 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

## 7.2.2 Anwendungsübersicht Lastgang Strom

|EDIFACT Struktur|Beschreibung|Lastgang Messlokation, Netzkoppelpunkt, Netzlokation|Lastgang Marktlokation, Tranche|Bedingung|||
|-|-|-|-|-|-|-|
||Prüfidentifikator|13018|13025||||
|Nutzdaten-Kopfsegment|||||||
|\*\*UNB\*\*|00002||Muss|Muss|||
|UNB|0001|\*\*UNOC\*\*|UN/ECE-Zeichensatz C|X|X||
|UNB|0002|\*\*3\*\*|Version 3|X|X||
|UNB|0004|MP-ID Absender|X|X|||
|UNB|0007|\*\*14\*\*|GS1|X|X||
||\*\*500\*\*|DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)|X|X|||
|UNB|0010|MP-ID Empfänger|X|X|||
|UNB|0007|\*\*14\*\*|GS1|X|X||
||\*\*500\*\*|DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)|X|X|||
|UNB|0017|Datum der Erstellung|X|X|||
|UNB|0019|Uhrzeit der Erstellung|X|X|||
|UNB|0020|Datenaustauschreferenz|X \[918]|X \[918]|\[918] Format: Zeichen aus dem über UNOC definierten Zeichensatz, wobei von den Buchstaben nur Großbuchstaben erlaubt sind.||
|UNB|0026|\*\*TL\*\*|Lastgang, beliebiger Zeitraum|X|X||
|Nachrichtenkopfsegment|||||||
|\*\*UNH\*\*|00003||Muss|Muss|||
|UNH|0062|Nachrichten-Referenznummer|X|X|||
|UNH|0065|\*\*MSCONS\*\*|Bericht über den Verbrauch messbarer Dienstleistungen|X|X||
|UNH|0052|\*\*D\*\*|Entwurfs-Version|X|X||
|UNH|0054|\*\*04B\*\*|Ausgabe 2004 - B|X|X||
|UNH|0051|\*\*UN\*\*|UN/CEFACT|X|X||
|UNH|0057|\*\*2.4c\*\*|Versionsnummer der zugrundeliegenden BDEW-Nachrichtenbeschreibung|X|X||
|Beginn der Nachricht|||||||
|\*\*BGM\*\*|00004||Muss|Muss|||
|BGM|1001|\*\*7\*\*|Prozessdatenbericht|X|||
||\*\*Z48\*\*|Lastgang Marktlokation, Tranche||X|||
|BGM|1004|Dokumentennummer|X|X|||
|BGM|1225|\*\*9\*\*|Original|X|X||
|Nachrichtendatum|||||||
|\*\*DTM\*\*|00005||Muss|Muss|||
|DTM|2005|\*\*137\*\*|Dokumenten-/Nachrichtendatum/-zeit|X|X||
|DTM|2380|Datum oder Uhrzeit oder Zeitspanne, Wert|X \[931] \[494]|X \[931] \[494]|\[494] Das hier genannte Datum muss der Zeitpunkt sein, zu dem das Dokument erstellt wurde, oder ein Zeitpunkt, der davor liegt.<br/>\[931] Format: ZZZ = +00||
|DTM|2379|\*\*303\*\*|CCYYMMDDHHMMZZZ|X|X||


Version: 3.1f
30.09.2025
Seite 66 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|EDIFACT Struktur|Beschreibung<br/>Prüfidentifikator|Lastgang Messlokation, Netzkoppelpunkt, Netzlokation<br/>13018|Lastgang Marktlokation, Tranche<br/>13025|Bedingung||||
|-|-|-|-|-|-|-|-|
|Referenzangaben||||||||
|SG1||Soll \[1] ∧ \[538]|Soll \[1] ∧ \[538]|\[1] Sofern per ORDERS angefordert<br/>\[538] Hinweis: Die Referenz auf die ORDERS ist nur dann anzugeben, wenn diese Werte vom Empfänger auch ursprünglich mittels ORDERS angefragt wurden.||||
|SG1|RFF|00006|Muss|Muss||||
|SG1|RFF|1153|AGI|Beantragungsnummer|X|X||
|SG1|RFF|1154|Referenznummer|X \[529] ∨ \[553]|X \[529] ∨ \[553]|\[529] Hinweis: Wert aus BGM+7 DE1004 der ORDERS mit der die Anforderung von Messwerten erfolgt ist.<br/>\[553] Hinweis: Wert aus BGM+Z34 DE1004 der ORDERS mit der die Reklamation von Werten erfolgt ist||
|Prüfidentifikator||||||||
|SG1||Muss|Muss|||||
|SG1|RFF|00009|Muss|Muss||||
|SG1|RFF|1153|Z13|Prüfidentifikator|X|X||
|SG1|RFF|1154|13018|Lastgang Messlokation, Netzkoppelpunkt|X|||
|||13025|Lastgang Marktlokation, Tranche||X|||
|MP-ID Absender||||||||
|SG2||Muss|Muss|||||
|SG2|NAD|00010|Muss|Muss||||
|SG2|NAD|3035|MS|Dokumenten-/Nachrichtenaussteller bzw. -absender|X|X||
|SG2|NAD|3039|MP-ID|X \[117]|X \[117]|\[117] Nur MP-ID aus Sparte Strom||
|SG2|NAD|3055|9|GS1|X|X||
|||293|DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)|X|X|||
|Ansprechpartner||||||||
|SG4||Kann|Kann|||||
|SG4|CTA|00011|Muss|Muss||||
|SG4|CTA|3139|IC|Informationsstelle|X|X||
|SG4|CTA|3412|Abteilung oder Bearbeiter|X|X|||
|Kommunikationsverbindung||||||||
|SG4||||||||
|SG4|COM|00012|Muss|Muss||||


Version: 3.1f 30.09.2025 Seite 67 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|EDIFACT Struktur|Beschreibung|Lastgang Messlokation, Netzkoppelpunkt, Netzlokation|Lastgang Marktlokation, Tranche|Bedingung|
|-|-|-|-|-|
||Prüfidentifikator|13018|13025||
|SG4 COM 3148|Kommunikationsadresse, Identifikation|X ((\[939] \[142]) ∨ (\[940] \[143])) ∧ \[576]|X ((\[939] \[142]) ∨ (\[940] \[143])) ∧ \[576]|\[142] wenn im DE3155 in demselben COM der Code EM vorhanden ist<br/>\[143] wenn im DE3155 in demselben COM der Code TE / FX / AJ / AL vorhanden ist<br/>\[576] Hinweis: Es darf nur eine Information im DE3148 übermittelt werden<br/>\[939] Format: Die Zeichenkette muss die Zeichen @ und . enthalten<br/>\[940] Format: Die Zeichenkette muss mit dem Zeichen + beginnen und danach dürfen nur noch Ziffern folgen|
|SG4 COM 3155|TE Telefon|X \[1P0..1]|X \[1P0..1]||
|SG4 COM 3155|EM E-Mail|X \[1P0..1]|X \[1P0..1]||
|SG4 COM 3155|AJ weiteres Telefon|X \[1P0..1]|X \[1P0..1]||
|SG4 COM 3155|AL Handy|X \[1P0..1]|X \[1P0..1]||
|SG4 COM 3155|FX Telefax|X \[1P0..1]|X \[1P0..1]||
|MP-ID Empfänger|||||
|SG2||Muss|Muss||
|SG2 NAD 00013||Muss|Muss||
|SG2 NAD 3035|MR Nachrichtenempfänger|X|X||
|SG2 NAD 3039|MP-ID|X \[117]|X \[117]|\[117] Nur MP-ID aus Sparte Strom|
|SG2 NAD 3055|9 GS1|X|X||
|SG2 NAD 3055|293 DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)|X|X||
|Abschnitts-Kontrollsegment|||||
|UNS 00014||Muss|Muss||
|UNS 0081|D Trennung von Kopf- und Positionsteil|X|X||
|Name und Adresse|||||
|SG5||Muss \[2001]|Muss \[2001]|\[2001] Segmentgruppe ist nur einmal je UNH anzugeben|
|SG5 NAD 00015||Muss|Muss||
|SG5 NAD 3035|DP Lieferanschrift|X|X||
|Identifikationsangabe|||||
|SG6||Muss|Muss||
|SG6 LOC 00017||Muss|Muss||
|SG6 LOC 3227|172 Meldepunkt|X|X||


Version: 3.1f 30.09.2025 Seite 68 von 158

MSCONS Anwendungshandbuch
edi@energy. Datenformate Strom & Gas

|EDIFACT Struktur|Beschreibung<br/>Prüfidentifikator|Lastgang Messlokation, Netzkoppelpunkt, Netzlokation<br/>13018|Lastgang Marktlokation, Tranche<br/>13025|Bedingung|
|-|-|-|-|-|
|SG6 LOC 3225|Bezeichnung|X (\[951] (\[510] ∧ \[35]) ∨ (\[535] ∧ (\[32] ∧ (\[36] ∨ \[80])))) ∨ (\[960] \[575] ∧ \[35] ∧ (\[36] ∨ \[33]))|X \[950] ((\[514] ∨ \[518]) ∧ (\[35] ∨ (\[32] ∧ \[77])))|\[32] wenn MP-ID in SG2 NAD+MS in der Rolle NB<br/>\[33] wenn MP-ID in SG2 NAD+MR in der Rolle LF<br/>\[35] wenn MP-ID in SG2 NAD+MS in der Rolle MSB<br/>\[36] wenn MP-ID in SG2 NAD+MR in der Rolle NB<br/>\[77] Wenn MP-ID in SG2 NAD+MR der RB HKN-R<br/>\[80] Wenn MP-ID in SG2 NAD+MR in der Rolle ÜNB<br/>\[510] Hinweis: Verwendung der ID der Messlokation<br/>\[514] Hinweis: Verwendung der ID der Marktlokation<br/>\[518] Hinweis: Verwendung der ID der Tranche<br/>\[535] Hinweis: Verwendung der ID des Netzkoppelpunktes Strom/Gas<br/>\[575] Hinweis: Verwendung der ID der Netzlokation<br/>\[950] Format: Marktlokations-ID<br/>\[951] Format: Zählpunktbezeichnung<br/>\[960] Format: Netzlokations-ID|
|Beginn Messperiode Übertragungszeitraum|||||
|SG6|||||
|SG6 DTM 00018||Muss|Muss||
|SG6 DTM 2005|163 Verarbeitung, Beginndatum/-zeit|X|X||
|SG6 DTM 2380|Datum oder Uhrzeit oder Zeitspanne, Wert|X \[931]|X \[931]|\[931] Format: ZZZ = +00|
|SG6 DTM 2379|303 CCYYMMDDHHMMZZZ|X|X||
|Ende Messperiode Übertragungszeitraum|||||
|SG6|||||
|SG6 DTM 00019||Muss|Muss||
|SG6 DTM 2005|164 Verarbeitung, Endedatum/-zeit|X|X||
|SG6 DTM 2380|Datum oder Uhrzeit oder Zeitspanne, Wert|X \[931]|X \[931]|\[931] Format: ZZZ = +00|
|SG6 DTM 2379|303 CCYYMMDDHHMMZZZ|X|X||
|lfd. Position|||||
|SG9|||||
|SG9 LIN 00026||Muss|Muss||
|SG9 LIN 1082|Positionsnummer|X \[908]|X \[908]|\[908] Format: Mögliche Werte: 1 bis n|
|Produktidentifikation|||||
|SG9|||||
|SG9 PIA 00027||Muss|Muss||
|SG9 PIA 4347|5 Produktidentifikation|X|X||


Version: 3.1f 30.09.2025 Seite 69 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|EDIFACT Struktur|Beschreibung<br/>Prüfidentifikator|Lastgang Messlokation, Netzkoppelpunkt, Netzlokation<br/>13018|Lastgang Marktlokation, Tranche<br/>13025|Bedingung|
|-|-|-|-|-|
|SG9 PIA 7140|Medium / OBIS-Kennzahl|X \[501] ∧ \[566]|X \[501] ∧ \[566]|\[501] Hinweis: Es sind nur die Werte erlaubt, die in der EDI\@Energy Codeliste der OBIS-Kennzahlen und Medien mit dem entsprechenden Prüfidentifikator versehen sind.<br/>\[566] Hinweis: Es sind nur die Werte erlaubt, die im vorherigen Stammdatenaustausch zu diesem Meldepunkt vom MSB zum Zeitpunkt übermittelt wurden.|
|SG9 PIA 7143|SRW OBIS-Kennzahl|X|X||
|Mengenangaben|||||
|SG10||Muss|Muss||
|SG10 QTY 00028||Muss|Muss||
|SG10 QTY 6063|220 Wahrer Wert|X|X|\[32] wenn MP-ID in SG2 NAD+MS in der Rolle NB<br/>\[35] wenn MP-ID in SG2 NAD+MS in der Rolle MSB<br/>\[36] wenn MP-ID in SG2 NAD+MR in der Rolle NB<br/>\[77] Wenn MP-ID in SG2 NAD+MR der RB HKN-R<br/>\[80] Wenn MP-ID in SG2 NAD+MR in der Rolle ÜNB|
||67 Ersatzwert|X \[35] ∨ (\[32] ∧ (\[36] ∨ \[80]))|X \[35] ∨ (\[32] ∧ \[77])||
||Z18 Vorläufiger Wert|X \[35] ∨ (\[32] ∧ (\[36] ∨ \[80]))|X \[35]||
|SG10 QTY 6060|Menge|X \[902] ∧ \[906]|X \[902] ∧ \[906]|\[902] Format: Möglicher Wert: ≥ 0<br/>\[906] Format: max. 3 Nachkommastellen|
|Beginn Messperiode|||||
|SG10||Muss|Muss||
|SG10 DTM 00029||Muss|Muss||
|SG10 DTM 2005|163 Verarbeitung, Beginndatum/-zeit|X|X||
|SG10 DTM 2380|Datum oder Uhrzeit oder Zeitspanne, Wert|X \[931] \[495]|X \[931] \[495]|\[495] Der Zeitpunkt muss ≤ dem Wert im DE2380 des DTM+137 sein<br/>\[931] Format: ZZZ = +00|
|SG10 DTM 2379|303 CCYYMMDDHHMMZZZ|X|X||
|Ende Messperiode|||||
|SG10||Muss|Muss||
|SG10 DTM 00030||Muss|Muss||
|SG10 DTM 2005|164 Verarbeitung, Endedatum/-zeit|X|X||
|SG10 DTM 2380|Datum oder Uhrzeit oder Zeitspanne, Wert|X \[931] \[495]|X \[931] \[495]|\[495] Der Zeitpunkt muss ≤ dem Wert im DE2380 des DTM+137 sein<br/>\[931] Format: ZZZ = +00|
|SG10 DTM 2379|303 CCYYMMDDHHMMZZZ|X|X||
|Plausibilisierungshinweis|||||
|SG10||Soll (\[92] ⊻ \[93]) ∧ \[126]|Soll (\[92] ⊻ \[93]) ∧ \[126]|\[92] Wenn SG10 QTY DE6063 mit Wert 67 vorhanden<br/>\[93] Wenn SG10 QTY DE6063 mit Wert 220 vorhanden<br/>\[126] wenn Plausibilisierungshinweise vorliegen|
|SG10 STS 00035|||||
|SG10 STS 9015|Z33 Plausibilisierungshinweis|X|X||


Version: 3.1f 30.09.2025 Seite 70 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|EDIFACT Struktur|Beschreibung|Lastgang Messlokation, Netzkoppelpunkt, Netzlokation|Lastgang Marktlokation, Tranche|Bedingung||
|-|-|-|-|-|-|
||Prüfidentifikator|13018|13025|||
|SG10 STS 9013|Z83|Kundenselbstablesung|X \[5P0..1]|X \[5P0..1]||
||Z84|Leerstand|X \[4P0..1] ⊻ \[5P0..1]|X \[4P0..1] ⊻ \[5P0..1]||
||Z85|Realer Zählerüberlauf geprüft|X \[4P0..1] ⊻ \[5P0..1]|X \[4P0..1] ⊻ \[5P0..1]||
||Z86|Plausibel wg. Kontrollablesung|X \[4P0..1] ⊻ \[5P0..1]|X \[4P0..1] ⊻ \[5P0..1]||
||Z87|Plausibel wg. Kundenhinweis|X \[4P0..1] ⊻ \[5P0..1]|X \[4P0..1] ⊻ \[5P0..1]||
||ZC3|Austausch des Ersatzwertes|X \[4P0..1] ⊻ \[5P0..1]|X \[4P0..1] ⊻ \[5P0..1]||
|Ersatzwertbildungsverfahren||||||
|SG10||||||
|SG10 STS 00036|||Muss \[92]|Muss \[92]|\[92] Wenn SG10 QTY DE6063 mit Wert 67 vorhanden|
|SG10 STS 9015|Z32|Ersatzwertbildungsverfahren|X|X||
|SG10 STS 9013|Z88|Vergleichsmessung (geeicht)|X \[4P0..1]|X \[4P0..1]|\[46] Wenn Wert in SG6 LOC+172 DE3225 genau 11 Stellen|
||Z89|Vergleichsmessung (nicht geeicht)|X \[4P0..1]|X \[4P0..1]|\[568] Hinweis: Verwendung ist nur zulässig, wenn es sich um 1:n Beziehung zwischen Markt- und Messlokation handelt und auf Ebene der Messlokation unterschiedliche Ersatzwertbildungsverfahren verwendet und kommuniziert wurden.|
||Z92|Interpolation|X \[4P0..1]|X \[4P0..1]||
||ZJ2|Statistische Methode|X \[4P0..1]|X \[4P0..1]||
||ZS0|Ersatzwertbildungsverfahren gemäß Angaben auf Ebene der Messlokation||X \[46] ∧ \[568]||
|Korrekturgrund||||||
|SG10||||||
|SG10 STS 00037|||Soll \[127] ∧ \[551]|Soll \[127] ∧ \[551]|\[127] wenn ein Korrekturgrund anzugeben ist \[551] Hinweis: Ein Korrekturgrund ist anzugeben, wenn:<br/>1. ein bereits an den MP übermittelter vorläufiger Wert durch einen Ersatzwert ersetzt wird, oder<br/>2. ein bereits an den MP übermittelter Ersatzwert durch einen Ersatzwert ersetzt wird, oder<br/>3. ein bereits an den MP übermittelter wahrer Wert durch einen Ersatzwert ersetzt wird, oder<br/>4. ein bereits an den MP übermittelter wahrer Wert durch einen wahren Wert ersetzt wird.|
|SG10 STS 9015|Z34|Korrekturgrund|X|X||


Version: 3.1f 30.09.2025 Seite 71 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|EDIFACT Struktur|Beschreibung|Lastgang Messlokation, Netzkoppelpunkt, Netzlokation|Lastgang Marktlokation, Tranche|Bedingung||
|-|-|-|-|-|-|
||Prüfidentifikator|13018|13025|||
|SG10 STS 9013|Z74|kein Zugang|X \[4P0..1]|X \[4P0..1]||
||Z75|Kommunikationsstörung|X \[4P0..1]|X \[4P0..1]||
||Z76|Netzausfall|X \[4P0..1]|X \[4P0..1]||
||Z77|Spannungsausfall|X \[4P0..1]|X \[4P0..1]||
||Z78|Gerätewechsel|X \[4P0..1]|X \[4P0..1]||
||Z79|Kalibrierung|X \[4P0..1]|X \[4P0..1]||
||Z80|Gerät arbeitet außerhalb der Betriebsbedingungen|X \[4P0..1]|X \[4P0..1]||
||Z81|Messeinrichtung gestört/defekt|X \[4P0..1]|X \[4P0..1]||
||Z82|Unsicherheit Messung|X \[4P0..1]|X \[4P0..1]||
||ZA0|Uhrzeit gestellt /Synchronisation|X \[4P0..1]|X \[4P0..1]||
||ZA1|Messwert unplausibel|X \[4P0..1]|X \[4P0..1]||
||ZA3|Falscher Wandlerfaktor|X \[4P0..1] ⊻ \[5P0..1]|X \[4P0..1] ⊻ \[5P0..1]||
||ZA4|Fehlerhafte Ablesung|X \[4P0..1] ⊻ \[5P0..1]|X \[4P0..1] ⊻ \[5P0..1]||
||ZA5|Änderung der Berechnung|X \[4P0..1] ⊻ \[5P0..1]|X \[4P0..1] ⊻ \[5P0..1]||
||ZA6|Umbau der Messlokation|X \[4P0..1] ⊻ \[5P0..1]|X \[4P0..1] ⊻ \[5P0..1]||
||ZA7|Datenbearbeitungsfehler|X \[4P0..1] ⊻ \[5P0..1]|X \[4P0..1] ⊻ \[5P0..1]||
||ZB0|Störung / Defekt Messeinrichtung|X \[4P0..1] ⊻ \[5P0..1]|X \[4P0..1] ⊻ \[5P0..1]||
||ZB9|Änderung Tarifschaltzeiten|X \[4P0..1] ⊻ \[5P0..1]|X \[4P0..1] ⊻ \[5P0..1]||
||ZC2|Tarifschaltgerät defekt|X \[4P0..1] ⊻ \[5P0..1]|X \[4P0..1] ⊻ \[5P0..1]||
||ZC4|Impulswertigkeit nicht ausreichend|X \[4P0..1]|X \[4P0..1]||
||ZJ8|Energiemenge in ungemessenem Zeitintervall|X \[4P0..1]|||
||ZJ9|Energiemenge aus dem ungepairten Zeitintervall|X \[4P0..1] ⊻ \[5P0..1]|||
|Grund der Ersatzwertbildung||||||
|SG10||||||
|SG10 STS 00038|||Muss \[92]|Muss \[92]|\[92] Wenn SG10 QTY DE6063 mit Wert 67 vorhanden|
|SG10 STS 9015|Z40|Grund der Ersatzwertbildung|X|X||


Version: 3.1f 30.09.2025 Seite 72 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|EDIFACT Struktur|Beschreibung<br/>Prüfidentifikator|Lastgang Messlokation, Netzkoppelpunkt, Netzlokation<br/>13018|Lastgang Marktlokation, Tranche<br/>13025|Bedingung|
|-|-|-|-|-|
|SG10 STS 9013|\*\*Z74\*\* kein Zugang|X \[4P0..1]|X \[4P0..1]|\[46] Wenn Wert in SG6 LOC+172 DE3225 genau 11 Stellen|
||\*\*Z75\*\* Kommunikationsstörung|X \[4P0..1]|X \[4P0..1]|\[570] Hinweis: Verwendung ist nur zulässig, wenn es sich um 1:n Beziehung zwischen Markt- und Messlokation handelt und auf Ebene der Messlokation unterschiedliche Gründe für die Ersatzwertbildung vorliegen und kommuniziert wurden.|
||\*\*Z76\*\* Netzausfall|X \[4P0..1]|X \[4P0..1]||
||\*\*Z77\*\* Spannungsausfall|X \[4P0..1]|X \[4P0..1]||
||\*\*Z78\*\* Gerätewechsel|X \[4P0..1]|X \[4P0..1]||
||\*\*Z79\*\* Kalibrierung|X \[4P0..1]|X \[4P0..1]||
||\*\*Z80\*\* Gerät arbeitet außerhalb der Betriebsbedingungen|X \[4P0..1]|X \[4P0..1]||
||\*\*Z81\*\* Messeinrichtung gestört/defekt|X \[4P0..1]|X \[4P0..1]||
||\*\*Z82\*\* Unsicherheit Messung|X \[4P0..1]|X \[4P0..1]||
||\*\*ZA0\*\* Uhrzeit gestellt /Synchronisation|X \[4P0..1]|X \[4P0..1]||
||\*\*ZA1\*\* Messwert unplausibel|X \[4P0..1]|X \[4P0..1]||
||\*\*ZA3\*\* Falscher Wandlerfaktor|X \[4P0..1]|X \[4P0..1]||
||\*\*ZA4\*\* Fehlerhafte Ablesung|X \[4P0..1]|X \[4P0..1]||
||\*\*ZA5\*\* Änderung der Berechnung|X \[4P0..1]|X \[4P0..1]||
||\*\*ZA6\*\* Umbau der Messlokation|X \[4P0..1]|X \[4P0..1]||
||\*\*ZA7\*\* Datenbearbeitungsfehler|X \[4P0..1]|X \[4P0..1]||
||\*\*ZB0\*\* Störung / Defekt Messeinrichtung|X \[4P0..1]|X \[4P0..1]||
||\*\*ZB9\*\* Änderung Tarifschaltzeiten|X \[4P0..1]|X \[4P0..1]||
||\*\*ZC2\*\* Tarifschaltgerät defekt|X \[4P0..1]|X \[4P0..1]||
||\*\*ZC4\*\* Impulswertigkeit nicht ausreichend|X \[4P0..1]|X \[4P0..1]||
||\*\*ZS9\*\* Grund der Ersatzwertbildung gemäß Angaben auf Ebene der Messlokation||X \[46] ∧ \[570]||
|Nachrichten-Endesegment|||||
|\*\*UNT\*\* 00041||Muss|Muss||
|\*\*UNT 0074\*\*|Anzahl der Segmente in einer Nachricht|X|X||
|\*\*UNT 0062\*\*|Nachrichten-Referenznummer|X|X||
|Nutzdaten-Endesegment|||||
|\*\*UNZ\*\* 00042||Muss|Muss||
|\*\*UNZ 0036\*\*|Datenaustauschzähler|X|X||
|\*\*UNZ 0020\*\*|Datenaustauschreferenz|X|X||


Version: 3.1f 30.09.2025 Seite 73 von 158

MSCONS Anwendungshandbuch
![edi@energy. Datenformate Strom & Gas](image)

## 7.3 Lastgang Gas

### 7.3.1 Übertragung von Lastgängen Gas

Tabellenspalte = Lastgang (Gas) 13008

Dieser Anwendungsfall dient zur Übertragung eines Lastgangs in der Sparte Gas.

Bei Lastgängen von Meldepunkten sind entsprechend der Vorgaben der G685 Brennwert, Zustandszahl und falls vorhanden der K-Zahl-Korrekturfaktor F'korr mit anzugeben. Diese werden über die entsprechenden OBIS-Kennzahlen identifiziert und als abrechnungsfähiger Wert (SG10 QTY DE6063 = 220-wahrer Wert – Abrechnungs-brennwert) oder als Prognosewert (SG10 QTY DE6063 = 187-Prognosewert – Bilanzierungsbrennwert) in zusätzlichen LIN-Segmenten angegeben. In Fällen, dass der Lastgang einer Marktlokation aus den Lastgängen mehrerer Messlokationen gebildet wird, wird der „Summen“-Lastgang lediglich in kWh übermittelt, auf die Angabe von Brennwert, K-Zahl-Korrekturfaktor F'korr und Zustandszahl wird verzichtet.

Bei der Übertragung von Betriebsvolumen und Normvolumen (in der Kommunikation zwischen MSB und NB sowie NB und NB) kann es vorkommen, dass kein Brennwert, kein K-Zahl-Korrekturfaktor F'korr und keine Zustands-zahl vorliegt. Daher ist die Angabe von Brennwert, K-Zahl-Korrekturfaktor F'korr und Zustandszahl in diesen beiden Fällen nicht verpflichtend. Der MSB hat dem NB auch alle zur Plausibilisierung und Ersatzwertbildung notwendigen Informationen (Neben den Volumina und ggf. Energiemengen auch Druck und Temperatur) bereitzustellen.

Kommunikationspartner, Identifikationsangabe und Art der Werte für diesen Anwendungsfall:

|Sparte|Kommunikation von|Art der Werte|Identifikationsangabe in SG6 LOC|Anmerkung|
|-|-|-|-|-|
|Gas|MSB an NB|1 Std.-Lastgänge (Stundenwerte)|ID der Messlokation|--|
|Gas|NB an MSB|1 Std.-Lastgänge (Stundenwerte)|ID der Messlokation|--|
|Gas|NB an LF|1 Std.-Lastgänge (Stundenwerte)|Wenn es sich um eine 1:1-Beziehung zwischen Messlokation und Marktlokation handelt und der gemessene Lastgang der Messlokation dem Lastgang der Marktlokation 1:1 entspricht, dann: ID der Marktlokation.<br/><br/>Wenn der gemessene Lastgang der Messlokation nicht dem Lastgang der Marktlokation 1:1 entspricht (z. B. Summierung), dann: der/die gemessene/n Lastgang/Lastgänge mit der ID der Messlokation/en und der errechnete Lastgang mit der ID der Marktlokation.|--|
|Gas|NB an NB|1 Std.-Lastgänge (Stundenwerte)|ID des Netzkopplungspunktes bei Gas|Zur Abstimmung der Netzzeitreihen|
|Gas|NB an MGV|1 Std.-Lastgänge (Stundenwerte)|ID der Marktlokation|--|


Version: 3.1f 30.09.2025 Seite 74 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

### 7.3.2 Anwendungsübersicht Lastgang Gas

|EDIFACT Struktur||Beschreibung<br/>Prüfidentifikator||Lastgang (Gas) 13008||Bedingung|
|-|-|-|-|-|-|-|
|Nutzdaten-Kopfsegment||||Muss|||
|UNB||00002|||||
|UNB|0001|UNOC|UN/ECE-Zeichensatz C|X|||
|UNB|0002|3|Version 3|X|||
|UNB|0004||MP-ID Absender|X|||
|UNB|0007|14|GS1|X|||
|||502|DE, DVGW Service & Consult GmbH|X|||
|UNB|0010||MP-ID Empfänger|X|||
|UNB|0007|14|GS1|X|||
|||502|DE, DVGW Service & Consult GmbH|X|||
|UNB|0017||Datum der Erstellung|X|||
|UNB|0019||Uhrzeit der Erstellung|X|||
|UNB|0020||Datenaustauschreferenz|X \[918]|\[918] Format: Zeichen aus dem über UNOC definierten Zeichensatz, wobei von den Buchstaben nur Großbuchstaben erlaubt sind.||
|UNB|0026|TL|Lastgang, beliebiger Zeitraum|X|||
|Nachrichtenkopfsegment||||Muss|||
|UNH||00003|||||
|UNH|0062||Nachrichten-Referenznummer|X|||
|UNH|0065|MSCON|Bericht über den Verbrauch messbarer Dienstleistungen|X|||
||S||||||
|UNH|0052|D|Entwurfs-Version|X|||
|UNH|0054|04B|Ausgabe 2004 - B|X|||
|UNH|0051|UN|UN/CEFACT|X|||
|UNH|0057|2.4c|Versionsnummer der zugrundeliegenden BDEW-Nachrichtenbeschreibung|X|||
|Beginn der Nachricht||||Muss|||
|BGM||00004|||||
|BGM|1001|7|Prozessdatenbericht|X|||
|BGM|1004||Dokumentennummer|X|||
|BGM|1225|9|Original|X|||
|Nachrichtendatum||||Muss|||
|DTM||00005|||||
|DTM|2005|137|Dokumenten-/Nachrichtendatum/-zeit|X|||
|DTM|2380||Datum oder Uhrzeit oder Zeitspanne, Wert|X \[931] \[494]|\[494] Das hier genannte Datum muss der Zeitpunkt sein, zu dem das Dokument erstellt wurde, oder ein Zeitpunkt, der davor liegt.<br/>\[931] Format: ZZZ = +00||
|DTM|2379|303|CCYYMMDDHHMMZZZ|X|||
|Referenzangaben||||Soll \[1]|\[1] Sofern per ORDERS angefordert||
|SG1|||||||
|SG1|RFF||00006||Muss||
|SG1|RFF|1153|AGI|Beantragungsnummer|X||
|SG1|RFF|1154||Referenznummer|X \[529] ∨ \[553]|\[529] Hinweis: Wert aus BGM+7 DE1004 der ORDERS mit der die Anforderung von Messwerten erfolgt ist.<br/>\[553] Hinweis: Wert aus BGM+Z34 DE1004 der ORDERS mit der die Reklamation von Werten erfolgt ist|
|Prüfidentifikator|||||||
|SG1||||Muss|||


Version: 3.1f 30.09.2025 Seite 75 von 158

MSCONS Anwendungshandbuch
![edi@energy Datenformate Strom & Gas](image)

|EDIFACT Struktur||Beschreibung<br/>Prüfidentifikator||Lastgang (Gas) 13008<br/>13008|Bedingung|||
|-|-|-|-|-|-|-|-|
|SG1|RFF||00009|||Muss||
|SG1|RFF|1153||Z13|Prüfidentifikator|X||
|SG1|RFF|1154||13008|Messwert Lastgang (Gas)|X||
|MP-ID Absender||||||||
|SG2|||||Muss|||
|SG2|NAD||00010|||Muss||
|SG2|NAD|3035||MS|Dokumenten- /Nachrichtenaussteller bzw. -absender|X||
|SG2|NAD|3039||MP-ID||X \[118]|\[118] Nur MP-ID aus Sparte Gas|
|SG2|NAD|3055||9|GS1|X||
||||332|DE, DVGW Service & Consult GmbH|X|||
|Ansprechpartner||||||||
|SG4|||||Kann|||
|SG4|CTA||00011|||Muss||
|SG4|CTA|3139||IC|Informationsstelle|X||
|SG4|CTA|3412||Abteilung oder Bearbeiter|X|||
|Kommunikationsverbindung||||||||
|SG4||||||||
|SG4|COM||00012|||Muss||
|SG4|COM|3148||Kommunikationsadresse, Identifikation|X ((\[939] \[142]) ∨ (\[940] \[143])) ∧ \[576]|\[142] wenn im DE3155 in demselben COM der Code EM vorhanden ist<br/>\[143] wenn im DE3155 in demselben COM der Code TE / FX / AJ / AL vorhanden ist<br/>\[576] Hinweis: Es darf nur eine Information im DE3148 übermittelt werden<br/>\[939] Format: Die Zeichenkette muss die Zeichen @ und . enthalten<br/>\[940] Format: Die Zeichenkette muss mit dem Zeichen + beginnen und danach dürfen nur noch Ziffern folgen||
|SG4|COM|3155||TE|Telefon|X \[1P0..1]||
||||EM|E-Mail|X \[1P0..1]|||
||||AJ|weiteres Telefon|X \[1P0..1]|||
||||AL|Handy|X \[1P0..1]|||
||||FX|Telefax|X \[1P0..1]|||
|MP-ID Empfänger||||||||
|SG2|||||Muss|||
|SG2|NAD||00013|||Muss||
|SG2|NAD|3035||MR|Nachrichtenempfänger|X||
|SG2|NAD|3039||MP-ID||X \[118]|\[118] Nur MP-ID aus Sparte Gas|
|SG2|NAD|3055||9|GS1|X||
||||332|DE, DVGW Service & Consult GmbH|X|||
|Abschnitts-Kontrollsegment||||||||
||UNS||00014|||Muss||
||UNS|0081||D|Trennung von Kopf- und Positionsteil|X||
|Name und Adresse||||||||
|SG5|||||Muss \[2001]|\[2001] Segmentgruppe ist nur einmal je UNH anzugeben||
|SG5|NAD||00015|||Muss||
|SG5|NAD|3035||DP|Lieferanschrift|X||
|Identifikationsangabe||||||||
|SG6|||||Muss|||
|SG6|LOC||00017|||Muss||
|SG6|LOC|3227||172|Meldepunkt|X||


Version: 3.1f 30.09.2025 Seite 76 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|EDIFACT Struktur|Beschreibung<br/>Prüfidentifikator|Lastgang (Gas)<br/>13008|Bedingung|
|-|-|-|-|
|SG6 LOC 3225|Bezeichnung|X (\[951] ((\[35] ∧ \[36]) ∨ (\[32] ∧ \[42]) ∧ \[510]) ∨ (\[32] ∧ \[36] ∧ \[535]) ∨ (\[32] ∧ \[33] ∧ \[519])) ⊻ (\[950] (\[32] ∧ \[33]) ∧ (\[514] ∧ \[520])) ⊻ (\[950] \[32] ∧ \[141] ∧ \[514])|\[32] wenn MP-ID in SG2 NAD+MS in der Rolle NB<br/>\[33] wenn MP-ID in SG2 NAD+MR in der Rolle LF<br/>\[35] wenn MP-ID in SG2 NAD+MS in der Rolle MSB<br/>\[36] wenn MP-ID in SG2 NAD+MR in der Rolle NB<br/>\[42] Wenn MP-ID in SG2 NAD+MR in der Rolle MSB<br/>\[141] Wenn MP-ID in SG2 NAD+MR in der Rolle MGV<br/>\[510] Hinweis: Verwendung der ID der Messlokation<br/>\[514] Hinweis: Verwendung der ID der Marktlokation<br/>\[519] Hinweis: Nur wenn der gemessene Lastgang der Messlokation nicht dem Lastgang der Marktlokation 1:1 entspricht.<br/>\[520] Hinweis: Wenn es sich um eine 1:1 Beziehung zwischen Messlokation und Marktlokation handelt und der gemessene Lastgang der Messlokation dem Lastgang der Marktlokation 1:1 entspricht, oder wenn der gemessene Lastgang nicht dem Lastgang der Marktlokation entspricht.<br/>\[535] Hinweis: Verwendung der ID des Netzkoppelpunktes Strom/Gas<br/>\[950] Format: Marktlokations-ID<br/>\[951] Format: Zählpunktbezeichnung|
|Beginn Messperiode Übertragungszeitraum||||
|SG6||Muss||
|SG6 DTM 00018||Muss||
|SG6 DTM 2005|163 Verarbeitung, Beginndatum/-zeit|X||
|SG6 DTM 2380|Datum oder Uhrzeit oder Zeitspanne, Wert|X \[931]|\[931] Format: ZZZ = +00|
|SG6 DTM 2379|303 CCYYMMDDHHMMZZZ|X||
|Ende Messperiode Übertragungszeitraum||||
|SG6||Muss||
|SG6 DTM 00019||Muss||
|SG6 DTM 2005|164 Verarbeitung, Endedatum/-zeit|X||
|SG6 DTM 2380|Datum oder Uhrzeit oder Zeitspanne, Wert|X \[931]|\[931] Format: ZZZ = +00|
|SG6 DTM 2379|303 CCYYMMDDHHMMZZZ|X||
|lfd. Position||||
|SG9||Muss||
|SG9 LIN 00026||Muss||
|SG9 LIN 1082|Positionsnummer|X \[908]|\[908] Format: Mögliche Werte: 1 bis n|
|Produktidentifikation||||
|SG9||Muss||
|SG9 PIA 00027||Muss||
|SG9 PIA 4347|5 Produktidentifikation|X||


Version: 3.1f 30.09.2025 Seite 77 von 158

MSCONS Anwendungshandbuch
![edi@energy Datenformate Strom & Gas](image)

|EDIFACT Struktur|Beschreibung<br/>Prüfidentifikator|Lastgang (Gas)<br/>13008|Bedingung|
|-|-|-|-|
|SG9 PIA 7140|Medium / OBIS-Kennzahl|X \[501] ⊻ (\[108] ∧ \[36])|\[36] wenn MP-ID in SG2 NAD+MR in der Rolle NB<br/>\[108] wenn SG9 PIA+5+7-b?:99.41.16/7-b?:99.42.16 (b=Kanal: Wert gemäß Codeliste der OBIS-Kennzahlen und Medien) vorhanden<br/>\[501] Hinweis: Es sind nur die Werte erlaubt, die in der EDI\@Energy Codeliste der OBIS-Kennzahlen und Medien mit dem entsprechenden Prüfidentifikator versehen sind.|
|SG9 PIA 7143|\*\*SRW\*\* OBIS-Kennzahl|X||
|Mengenangaben||||
|\*\*SG10\*\*||\*\*Muss\*\*||
|\*\*SG10 QTY\*\* 00028||\*\*Muss\*\*||
|SG10 QTY 6063|\*\*220\*\* Wahrer Wert|X|\[11] Wenn SG9 PIA+5+7-0?:52.0.22/7-0?:54.0.16/7-0?:54.0.20/7-0?:54.0.22<br/>\[32] wenn MP-ID in SG2 NAD+MS in der Rolle NB<br/>\[33] wenn MP-ID in SG2 NAD+MR in der Rolle LF<br/>\[35] wenn MP-ID in SG2 NAD+MS in der Rolle MSB<br/>\[36] wenn MP-ID in SG2 NAD+MR in der Rolle NB<br/>\[42] Wenn MP-ID in SG2 NAD+MR in der Rolle MSB<br/>\[141] Wenn MP-ID in SG2 NAD+MR in der Rolle MGV<br/>\[506] Hinweis: Nur bei Einspeisemengen und bei Gas zur stündlichen Energiedatenübermittlung|
||\*\*67\*\* Ersatzwert|X (\[32] ∧ (\[33] ∨ \[36] ∨ \[42] ∨ \[141]))||
||\*\*201\*\* Vorschlagswert|X (\[35] ∧ \[36])||
||\*\*20\*\* Nicht verwendbarer Wert|X ((\[35] ∧ \[36]) ∨ (\[32] ∧ \[33] ∧ \[506]))||
||\*\*187\*\* Prognosewert|X \[32] ∧ (\[33] ∨ \[36] ∨ \[141]) ∧ \[11]||
||\*\*Z18\*\* Vorläufiger Wert|X \[32] ∧ (\[33] ∨ \[141])||
|SG10 QTY 6060|Menge|X (\[902] ∧ \[906]) ∨ (\[902] ∧ \[907] \[125]) ∨ (\[910] ∧ \[907] \[45])|\[45] Wenn SG9 PIA+5+7-b:99.41.16 (b=Kanal: Wert gemäß Codeliste der OBIS-Kennzahlen und Medien) vorhanden<br/>\[125] wenn SG9 PIA+5+7-0?:52.0.22/7-b?:53.0.16/7-b?:55.0.16/7-b?:55.0.20/7-b?:55.0.22 (b=Kanal: Wert gemäß Codeliste der OBIS-Kennzahlen und Medien) vorhanden<br/>\[902] Format: Möglicher Wert: ≥ 0<br/>\[906] Format: max. 3 Nachkommastellen<br/>\[907] Format: max. 4 Nachkommastellen<br/>\[910] Format: Möglicher Wert: < 0 oder ≥ 0|
|Beginn Messperiode||||
|\*\*SG10\*\*||||
|\*\*SG10 DTM\*\* 00029||\*\*Muss\*\*||
|SG10 DTM 2005|\*\*163\*\* Verarbeitung, Beginndatum/-zeit|X||
|SG10 DTM 2380|Datum oder Uhrzeit oder Zeitspanne, Wert|X \[931]|\[931] Format: ZZZ = +00|
|SG10 DTM 2379|\*\*303\*\* CCYYMMDDHHMMZZZ|X||
|Ende Messperiode||||
|\*\*SG10\*\*||||
|\*\*SG10 DTM\*\* 00030||\*\*Muss\*\*||
|SG10 DTM 2005|\*\*164\*\* Verarbeitung, Endedatum/-zeit|X||
|SG10 DTM 2380|Datum oder Uhrzeit oder Zeitspanne, Wert|X \[931]|\[931] Format: ZZZ = +00|
|SG10 DTM 2379|\*\*303\*\* CCYYMMDDHHMMZZZ|X||
|Plausibilisierungshinweis||||
|\*\*SG10\*\*||||


Version: 3.1f 30.09.2025 Seite 78 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|EDIFACT Struktur||Beschreibung<br/>Prüfidentifikator|Lastgang (Gas)<br/>13008|Bedingung||
|-|-|-|-|-|-|
|SG10 STS|00035||Soll (\[92] ⊻ \[93] ⊻ \[94]) ∧ \[126]|\[92] Wenn SG10 QTY DE6063 mit Wert 67 vorhanden<br/>\[93] Wenn SG10 QTY DE6063 mit Wert 220 vorhanden<br/>\[94] Wenn SG10 QTY DE6063 mit Wert 201 vorhanden<br/>\[126] wenn Plausibilisierungshinweise vorliegen||
|SG10 STS|9015|Z33|Plausibilisierungshinweis|X||
|SG10 STS|9013|Z83|Kundenselbstablesung|X \[5P0..1]||
|||Z84|Leerstand|X \[4P0..1] ⊻ \[5P0..1] ⊻ \[6P0..1]||
|||Z85|Realer Zählerüberlauf geprüft|X \[4P0..1] ⊻ \[5P0..1] ⊻ \[6P0..1]||
|||Z86|Plausibel wg. Kontrollablesung|X \[4P0..1] ⊻ \[5P0..1] ⊻ \[6P0..1]||
|||Z87|Plausibel wg. Kundenhinweis|X \[4P0..1] ⊻ \[5P0..1] ⊻ \[6P0..1]||
|||ZC3|Austausch des Ersatzwertes|X \[5P0..1]||
|||ZR5|Rechenwert|X \[4P0..1] ⊻ \[5P0..1] ⊻ \[6P0..1]||
|Ersatzwertbildungsverfahren||||||
|SG10||||||
|SG10 STS|00036||Muss \[92] ⊻ \[94]|\[92] Wenn SG10 QTY DE6063 mit Wert 67 vorhanden<br/>\[94] Wenn SG10 QTY DE6063 mit Wert 201 vorhanden||
|SG10 STS|9015|Z32|Ersatzwertbildungsverfahren|X||
|SG10 STS|9013|Z89|Vergleichsmessung (nicht geeicht)|X \[4P0..1] ⊻ \[6P0..1]|\[32] wenn MP-ID in SG2 NAD+MS in der Rolle NB<br/>\[36] wenn MP-ID in SG2 NAD+MR in der Rolle NB<br/>\[46] Wenn Wert in SG6 LOC+172 DE3225 genau 11 Stellen<br/>\[568] Hinweis: Verwendung ist nur zulässig, wenn es sich um 1:n Beziehung zwischen Markt- und Messlokation handelt und auf Ebene der Messlokation unterschiedliche Ersatzwertbildungsverfahren verwendet und kommuniziert wurden.<br/>\[572] Hinweis: Verwendung ist nur zulässig, wenn es sich um 1:n Beziehung handelt und auf Ebene der Netzkopplungspunkte unterschiedliche Ersatzwertbildungsverfahren vorliegen und kommuniziert wurden.|
|||Z90|Messwertnachbildung aus geeichten Werten|X \[4P0..1] ⊻ \[6P0..1]||
|||Z91|Messwertnachbildung aus nicht geeichten Werten|X \[4P0..1] ⊻ \[6P0..1]||
|||Z92|Interpolation|X \[4P0..1] ⊻ \[6P0..1]||
|||Z93|Haltewert|X \[4P0..1] ⊻ \[6P0..1]||
|||Z94|Bilanzierung Netzabschnitt|X \[4P0..1] ⊻ \[6P0..1]||
|||Z95|Historische Messwerte|X \[4P0..1] ⊻ \[6P0..1]||
|||ZQ8|Aufteilung|X \[4P0..1] ⊻ \[6P0..1]||
|||ZQ9|Verwendung von Werten des Störmengenzählwerks|X \[4P0..1] ⊻ \[6P0..1]||
|||ZR0|Umgangs- und Korrekturmengen|X \[4P0..1] ⊻ \[6P0..1]||
|||ZS0|Ersatzwertbildungsverfahren gemäß Angaben auf Ebene der Messlokation|X (\[46] ∧ \[568]) ⊻ (\[32] ∧ \[36] ∧ \[572])||
|Korrekturgrund||||||
|SG10||||||
|SG10 STS|00037||Soll \[127] ∧ \[560]|\[127] wenn ein Korrekturgrund anzugeben ist \[560] Hinweis: Ein Korrekturgrund ist anzugeben, wenn:<br/>1. ein bereits an den MP übermittelter vorläufiger Wert durch einen Ersatzwert ersetzt wird, oder<br/>2. ein bereits an den MP übermittelter Ersatzwert durch einen Ersatzwert ersetzt wird, oder<br/>3. ein bereits an den MP übermittelter wahrer Wert durch einen Ersatzwert ersetzt wird, oder<br/>4. ein bereits an den MP übermittelter wahrer Wert durch einen wahren Wert ersetzt wird.||


Version: 3.1f 30.09.2025 Seite 79 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|EDIFACT Struktur|Beschreibung|Lastgang (Gas)|Bedingung||
|-|-|-|-|-|
||Prüfidentifikator|13008|||
|SG10 STS 9015|Z34|Korrekturgrund|X||
|SG10 STS 9013|Z74|kein Zugang|X \[4P0..1] ⊻ \[6P0..1] ⊻ \[7P0..1] ⊻ \[8P0..1]||
||Z75|Kommunikationsstörung|X \[4P0..1] ⊻ \[6P0..1] ⊻ \[7P0..1] ⊻ \[8P0..1]||
||Z76|Netzausfall|X \[4P0..1] ⊻ \[6P0..1] ⊻ \[7P0..1] ⊻ \[8P0..1]||
||Z78|Gerätewechsel|X \[4P0..1] ⊻ \[6P0..1] ⊻ \[7P0..1] ⊻ \[8P0..1]||
||Z80|Gerät arbeitet außerhalb der Betriebsbedingungen|X \[4P0..1] ⊻ \[6P0..1] ⊻ \[7P0..1] ⊻ \[8P0..1]||
||Z81|Messeinrichtung gestört/defekt|X \[4P0..1] ⊻ \[6P0..1] ⊻ \[7P0..1] ⊻ \[8P0..1]||
||Z82|Unsicherheit Messung|X \[4P0..1] ⊻ \[6P0..1] ⊻ \[7P0..1] ⊻ \[8P0..1]||
||Z98|Berücksichtigung Störmengenzählwerk|X \[4P0..1] ⊻ \[6P0..1]||
||Z99|Mengenumwertung unvollständig|X \[6P0..1] ⊻ \[7P0..1] ⊻ \[8P0..1]||
||ZA0|Uhrzeit gestellt /Synchronisation|X \[4P0..1] ⊻ \[6P0..1] ⊻ \[7P0..1] ⊻ \[8P0..1]||
||ZA1|Messwert unplausibel|X \[6P0..1] ⊻ \[7P0..1] ⊻ \[8P0..1]||
||ZA4|Fehlerhafte Ablesung|X \[4P0..1] ⊻ \[5P0..1] ⊻ \[6P0..1] ⊻ \[7P0..1] ⊻ \[8P0..1]||
||ZA5|Änderung der Berechnung|X \[4P0..1] ⊻ \[5P0..1] ⊻ \[6P0..1] ⊻ \[7P0..1] ⊻ \[8P0..1]||
||ZA6|Umbau der Messlokation|X \[4P0..1] ⊻ \[5P0..1] ⊻ \[6P0..1] ⊻ \[7P0..1] ⊻ \[8P0..1]||
||ZA7|Datenbearbeitungsfehler|X \[4P0..1] ⊻ \[5P0..1] ⊻ \[6P0..1] ⊻ \[7P0..1] ⊻ \[8P0..1]||
||ZA8|Brennwertkorrektur|X \[4P0..1] ⊻ \[5P0..1] ⊻ \[6P0..1] ⊻ \[7P0..1] ⊻ \[8P0..1]||
||ZA9|Z-Zahl-Korrektur|X \[4P0..1] ⊻ \[5P0..1] ⊻ \[6P0..1] ⊻ \[7P0..1] ⊻ \[8P0..1]||
||ZB0|Störung / Defekt Messeinrichtung|X \[4P0..1] ⊻ \[5P0..1] ⊻ \[6P0..1] ⊻ \[7P0..1] ⊻ \[8P0..1]||
||ZC4|Impulswertigkeit nicht ausreichend|X \[4P0..1] ⊻ \[7P0..1] ⊻ \[8P0..1]||
||ZJ9|Energiemenge aus dem ungepairten Zeitintervall|X \[4P0..1] ⊻ \[5P0..1]||
||ZR1|Wartungsarbeiten an geeichtem Messgerät|X \[4P0..1] ⊻ \[6P0..1] ⊻ \[7P0..1] ⊻ \[8P0..1]||
||ZR2|gestörte Werte|X \[4P0..1] ⊻ \[6P0..1] ⊻ \[7P0..1] ⊻ \[8P0..1]||
||ZR3|Wartungsarbeiten an eichrechtskonformen Messgeräten|X \[4P0..1] ⊻ \[6P0..1] ⊻ \[7P0..1] ⊻ \[8P0..1]||
||ZR4|Konsistenz- und Synchronprüfung|X \[4P0..1] ⊻ \[6P0..1] ⊻ \[7P0..1] ⊻ \[8P0..1]||
|Grund der Ersatzwertbildung|||||
|SG10|||||
|SG10 STS|00038||Muss \[92]|\[92] Wenn SG10 QTY DE6063 mit Wert 67 vorhanden|


Version: 3.1f	30.09.2025	Seite 80 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|EDIFACT Struktur||Beschreibung<br/>Prüfidentifikator||Lastgang (Gas)<br/>13008|Bedingung|
|-|-|-|-|-|-|
|SG10 STS \*\*9015\*\*||\*\*Z40\*\*|Grund der Ersatzwertbildung|X||
|SG10 STS \*\*9013\*\*||\*\*Z74\*\*|kein Zugang|X \[4P0..1]|\[32] wenn MP-ID in SG2 NAD+MS in der Rolle NB<br/>\[36] wenn MP-ID in SG2 NAD+MR in der Rolle NB<br/>\[46] Wenn Wert in SG6 LOC+172 DE3225 genau 11 Stellen<br/>\[570] Hinweis: Verwendung ist nur zulässig, wenn es sich um 1:n Beziehung zwischen Markt- und Messlokation handelt und auf Ebene der Messlokation unterschiedliche Gründe für die Ersatzwertbildung vorliegen und kommuniziert wurden.<br/>\[571] Hinweis: Verwendung ist nur zulässig, wenn es sich um 1:n Beziehung handelt und auf Ebene der Netzkopplungspunkte unterschiedliche Gründe für die Ersatzwertbildung vorliegen und kommuniziert wurden.|
|||\*\*Z75\*\*|Kommunikationsstörung|X \[4P0..1]||
|||\*\*Z76\*\*|Netzausfall|X \[4P0..1]||
|||\*\*Z78\*\*|Gerätewechsel|X \[4P0..1]||
|||\*\*Z80\*\*|Gerät arbeitet außerhalb der Betriebsbedingungen|X \[4P0..1]||
|||\*\*Z81\*\*|Messeinrichtung gestört/defekt|X \[4P0..1]||
|||\*\*Z82\*\*|Unsicherheit Messung|X \[4P0..1]||
|||\*\*Z98\*\*|Berücksichtigung Störmengenzählwerk|X \[4P0..1]||
|||\*\*Z99\*\*|Mengenumwertung unvollständig|X \[4P0..1]||
|||\*\*ZA0\*\*|Uhrzeit gestellt /Synchronisation|X \[4P0..1]||
|||\*\*ZA1\*\*|Messwert unplausibel|X \[4P0..1]||
|||\*\*ZA4\*\*|Fehlerhafte Ablesung|X \[4P0..1]||
|||\*\*ZA5\*\*|Änderung der Berechnung|X \[4P0..1]||
|||\*\*ZA6\*\*|Umbau der Messlokation|X \[4P0..1]||
|||\*\*ZA7\*\*|Datenbearbeitungsfehler|X \[4P0..1]||
|||\*\*ZB0\*\*|Störung / Defekt Messeinrichtung|X \[4P0..1]||
|||\*\*ZC4\*\*|Impulswertigkeit nicht ausreichend|X \[4P0..1]||
|||\*\*ZR1\*\*|Wartungsarbeiten an geeichtem Messgerät|X \[4P0..1]||
|||\*\*ZR2\*\*|gestörte Werte|X \[4P0..1]||
|||\*\*ZR3\*\*|Wartungsarbeiten an eichrechtskonformen Messgeräten|X \[4P0..1]||
|||\*\*ZR4\*\*|Konsistenz- und Synchronprüfung|X \[4P0..1]||
|||\*\*ZS9\*\*|Grund der Ersatzwertbildung gemäß Angaben auf Ebene der Messlokation|X ((\[46] ∧ \[570]) ⊻ (\[32] ∧ \[36] ∧ \[571]))||
|Gasqualität||||||
|\*\*SG10\*\*||||||
|SG10 STS 00039|||Soll \[97]|\[97] Wenn es sich um die Übermittlung eines Wertes aufgrund der Umstellung der Gasqualität handelt||
|SG10 STS \*\*9015\*\*||\*\*Z31\*\*|Gasqualität|X||
|SG10 STS \*\*9013\*\*||\*\*ZG3\*\*|Umstellung Gasqualität|X||
|Nachrichten-Endesegment||||||
|\*\*UNT\*\* 00041|||Muss|||
|UNT \*\*0074\*\*||Anzahl der Segmente in einer Nachricht|X|||
|UNT \*\*0062\*\*||Nachrichten-Referenznummer|X|||
|Nutzdaten-Endesegment||||||
|\*\*UNZ\*\* 00042|||Muss|||
|UNZ \*\*0036\*\*||Datenaustauschzähler|X|||
|UNZ \*\*0020\*\*||Datenaustauschreferenz|X|||


Version: 3.1f 30.09.2025 Seite 81 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

# 8 Übertragung im Rahmen MaBiS / Redispatch 2.0

## 8.1 Normiertes Profil / Profilschar / Vergangenheitswerte TEP mit Referenzmessung

### 8.1.1 Übertragung normiertes Profil

Tabellenspalte = normiertes Profil 13010

Dieser Anwendungsfall dient zur Übertragung eines normierten Profils.

Vor der Übermittlung von tagesparameterabhängigen Profilen muss der Netzbetreiber dem Lieferanten die zugehörige Profilschar und die Temperaturmessstelle/Klimazone mitgeteilt haben.

Kommunikationspartner, Identifikationsangabe und Art der Werte für diesen Anwendungsfall:

|Sparte|Kommunikation von|Art der Werte|Identifikationsangabe in SG6 LOC|Anmerkung|
|-|-|-|-|-|
|Strom|NB an LF|Normiertes Profil|Profilbezeichnung|--|
|Strom|NB an MSB|Normiertes Profil|Profilbezeichnung|--|


### 8.1.2 Übertragung Profilschar

Tabellenspalte = Profilschar 13011

Dieser Anwendungsfall dient zur Übertragung der Profilschar.

In SG9 LIN DE1082 wird die Temperaturmaßzahl (TMZ) angegeben. Die Maßeinheit ist gemäß Liste der Profildefinitionen anzugeben.

Kommunikationspartner, Identifikationsangabe und Art der Werte für diesen Anwendungsfall:

|Sparte|Kommunikation von|Art der Werte|Identifikationsangabe in SG6 LOC|Anmerkung|
|-|-|-|-|-|
|Strom|NB an LF|Profilschar|Bezeichnung der Profilschar|--|
|Strom|NB an MSB|Profilschar|Bezeichnung der Profilschar|--|


### 8.1.3 Übertragung Vergangenheitswerte TEP mit Referenzmessung

Tabellenspalte = TEP vergh. Werte Referenzmessung 13012

Dieser Anwendungsfall dient zur Übertragung von Vergangenheitswerte TEP mit Referenzmessung.

Kommunikationspartner, Identifikationsangabe und Art der Werte für diesen Anwendungsfall:

Version: 3.1f 30.09.2025 Seite 82 von 158

MSCONS Anwendungshandbuch
![edi@energy. Datenformate Strom & Gas](image)

|Sparte|Kommunikation von|Art der Werte|Identifikationsangabe in SG6 LOC|Anmerkung|
|-|-|-|-|-|
|Strom|NB an LF|Vergangenheitswerte TEP mit Referenzmessung|Profilbezeichnung|--|
|Strom|NB an MSB|Vergangenheitswerte TEP mit Referenzmessung|Profilbezeichnung|--|


Version: 3.1f	30.09.2025	Seite 83 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

### 8.1.4 Anwendungsübersicht Profil / Profilschar / Vergh. Werte TEP mit Referenzm.

|EDIFACT Struktur|Beschreibung|normiertes Profil|Profilschar|TEP vergh. Werte Referenzmessung|Bedingung|||
|-|-|-|-|-|-|-|-|
||Prüfidentifikator|13010|13011|13012||||
|Nutzdaten-Kopfsegment||Muss|Muss|Muss||||
|UNB|00002||Muss|Muss|Muss|||
|UNB|0001|UNOC|UN/ECE-Zeichensatz C|X|X|X||
|UNB|0002|3|Version 3|X|X|X||
|UNB|0004|MP-ID Absender|X|X|X|||
|UNB|0007|14|GS1|X|X|X||
|||500|DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)|X|X|X||
|UNB|0010|MP-ID Empfänger|X|X|X|||
|UNB|0007|14|GS1|X|X|X||
|||500|DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)|X|X|X||
|UNB|0017|Datum der Erstellung|X|X|X|||
|UNB|0019|Uhrzeit der Erstellung|X|X|X|||
|UNB|0020|Datenaustauschreferenz|X \[918]|X \[918]|X \[918]|\[918] Format: Zeichen aus dem über UNOC definierten Zeichensatz, wobei von den Buchstaben nur Großbuchstaben erlaubt sind.||
|UNB|0026|TL|Lastgang, beliebiger Zeitraum|X|X|X||
|Nachrichtenkopfsegment||Muss|Muss|Muss||||
|UNH|00003||Muss|Muss|Muss|||
|UNH|0062|Nachrichten-Referenznummer|X|X|X|||
|UNH|0065|MSCONS|Bericht über den Verbrauch messbarer Dienstleistungen|X|X|X||
|UNH|0052|D|Entwurfs-Version|X|X|X||
|UNH|0054|04B|Ausgabe 2004 - B|X|X|X||
|UNH|0051|UN|UN/CEFACT|X|X|X||
|UNH|0057|2.4c|Versionsnummer der zugrundeliegenden BDEW-Nachrichtenbeschreibung|X|X|X||
|Beginn der Nachricht||Muss|Muss|Muss||||
|BGM|00004||Muss|Muss|Muss|||
|BGM|1001|Z06|normiertes Profil|X||||
|||Z16|Profilschar||X|||
|||Z20|Vergangenheitswerte für TEP mit Referenzmessung|||X||
|BGM|1004|Dokumentennummer|X|X|X|||
|BGM|1225|9|Original|X|X|X||
|Nachrichtendatum||Muss|Muss|Muss||||
|DTM|00005||Muss|Muss|Muss|||
|DTM|2005|137|Dokumenten-/Nachrichtendatum/-zeit|X|X|X||


Version: 3.1f 30.09.2025 Seite 84 von 158

MSCONS Anwendungshandbuch
![edi@energy. Datenformate Strom & Gas](image)

|EDIFACT Struktur|Beschreibung<br/>Prüfidentifikator|normiertes Profil<br/>13010|Profilschar<br/>13011|TEP vergh. Werte Referenz-messung<br/>13012|Bedingung||||
|-|-|-|-|-|-|-|-|-|
|DTM|2380|Datum oder Uhrzeit oder Zeitspanne, Wert|X \[931] \[494]|X \[931] \[494]|X \[931] \[494]|\[494] Das hier genannte Datum muss der Zeitpunkt sein, zu dem das Dokument erstellt wurde, oder ein Zeitpunkt, der davor liegt.<br/>\[931] Format: ZZZ = +00|||
|DTM|2379|303|CCYYMMDDHHMMZZZ|X|X|X|||
|Prüfidentifikator|||||||||
|SG1||Muss|Muss|Muss|||||
|SG1|RFF|00009|Muss|Muss|Muss||||
|SG1|RFF|1153|Z13|Prüfidentifikator|X|X|X||
|SG1|RFF|1154|13010|Profil|X||||
|||13011|Profilschar||X||||
|||13012|TEP Vergangenheitswerte Referenz-Messung|||X|||
|MP-ID Absender|||||||||
|SG2||Muss|Muss|Muss|||||
|SG2|NAD|00010|Muss|Muss|Muss||||
|SG2|NAD|3035|MS|Dokumenten- /Nachrichtenaussteller bzw. -absender|X|X|X||
|SG2|NAD|3039|MP-ID|X \[117]|X \[117]|X \[117]|\[117] Nur MP-ID aus Sparte Strom||
|SG2|NAD|3055|9|GS1|X|X|X||
|||293|DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)|X|X|X|||
|Ansprechpartner|||||||||
|SG4||Kann|Kann|Kann|||||
|SG4|CTA|00011|Muss|Muss|Muss||||
|SG4|CTA|3139|IC|Informationsstelle|X|X|X||
|SG4|CTA|3412|Abteilung oder Bearbeiter|X|X|X|||
|Kommunikationsverbindung|||||||||
|SG4|||||||||
|SG4|COM|00012|Muss|Muss|Muss||||
|SG4|COM|3148|Kommunikationsadresse, Identifikation|X ((\[939] \[142]) ∨ (\[940] \[143])) ∧ \[576]|X ((\[939] \[142]) ∨ (\[940] \[143])) ∧ \[576]|X ((\[939] \[142]) ∨ (\[940] \[143])) ∧ \[576]|\[142] wenn im DE3155 in demselben COM der Code EM vorhanden ist<br/>\[143] wenn im DE3155 in demselben COM der Code TE / FX / AJ / AL vorhanden ist<br/>\[576] Hinweis: Es darf nur eine Information im DE3148 übermittelt werden<br/>\[939] Format: Die Zeichenkette muss die Zeichen @ und . enthalten<br/>\[940] Format: Die Zeichenkette muss mit dem Zeichen + beginnen und danach dürfen nur noch Ziffern folgen||
|SG4|COM|3155|TE|Telefon|X \[1P0..1]|X \[1P0..1]|X \[1P0..1]||
|||EM|E-Mail|X \[1P0..1]|X \[1P0..1]|X \[1P0..1]|||
|||AJ|weiteres Telefon|X \[1P0..1]|X \[1P0..1]|X \[1P0..1]|||
|||AL|Handy|X \[1P0..1]|X \[1P0..1]|X \[1P0..1]|||
|||FX|Telefax|X \[1P0..1]|X \[1P0..1]|X \[1P0..1]|||
|MP-ID Empfänger|||||||||
|SG2||Muss|Muss|Muss|||||


Version: 3.1f 30.09.2025 Seite 85 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|EDIFACT Struktur||Beschreibung||normiertes Profil<br/>Prüfidentifikator|Profilschar<br/>13010|TEP vergh. Werte Referenzmessung<br/>13011|Bedingung<br/>13012||||
|-|-|-|-|-|-|-|-|-|-|-|
|SG2|NAD||00013||Muss|Muss|Muss||||
|SG2|NAD|3035||MR|Nachrichtenempfänger|X|X|X|||
|SG2|NAD|3039||MP-ID||X \[117]|X \[117]|X \[117]|\[117] Nur MP-ID aus Sparte Strom||
|SG2|NAD|3055||9|GS1|X|X|X|||
|SG2|NAD|3055||293|DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)|X|X|X|||
|Abschnitts-Kontrollsegment|||||||||||
||UNS||00014||Muss|Muss|Muss||||
||UNS|0081||D|Trennung von Kopf- und Positionsteil|X|X|X|||
|Name und Adresse|||||||||||
|SG5||||||Muss \[2001]|Muss \[2001]|Muss \[2001]|\[2001] Segmentgruppe ist nur einmal je UNH anzugeben||
|SG5|NAD||00015||Muss|Muss|Muss||||
|SG5|NAD|3035||DED|Profilerstellung|X|X|X|||
|Identifikationsangabe|||||||||||
|SG6||||||Muss|Muss|Muss|||
|SG6|LOC||00017||Muss|Muss|Muss||||
|SG6|LOC|3227||Z04|Profilbezeichnung|X||X|||
|SG6|LOC|3227||Z06|Profilschar||X||||
|SG6|LOC|3225||Bezeichnung||X \[905] \[515]|X \[905] \[516]|X \[905] \[515]|\[515] Hinweis: Verwendung der Profilbezeichnung<br/>\[516] Hinweis: Verwendung der Bezeichnung der Profilschar<br/>\[905] Format: max. 3 Stellen||
|Versionsangabe|||||||||||
|SG6|||||||||||
|SG6|DTM||00021||Muss \[2]|Muss|Muss \[2]|\[2] Wenn das Zeitintervall zwischen ersten SG10 DTM+163 und letzten SG10 DTM+164 mindestens einen Monat umfasst|||
|SG6|DTM|2005||293|Fertigstellungsdatum/-zeit|X|X|X|||
|SG6|DTM|2380||Datum oder Uhrzeit oder Zeitspanne, Wert|X \[931]|X \[931]|X \[931]|\[931] Format: ZZZ = +00|||
|SG6|DTM|2379||304|CCYYMMDDHHMMSSZZZ|X|X|X|||
|Gültigkeit, Beginndatum Profilschar|||||||||||
|SG6|||||||||||
|SG6|DTM||00022|||Muss|||||
|SG6|DTM|2005||157|Gültigkeit, Beginndatum||X||||
|SG6|DTM|2380||Datum oder Uhrzeit oder Zeitspanne, Wert||X|||||
|SG6|DTM|2379||610|CCYYMM|||X|||
|lfd. Position|||||||||||
|SG9||||||Muss|Muss|Muss|||
|SG9|LIN||00026||Muss|Muss|Muss||||
|SG9|LIN|1082||Positionsnummer||X \[908]|X \[909]|X \[908]|\[908] Format: Mögliche Werte: 1 bis n<br/>\[909] Format: Mögliche Werte: 0 bis n||
|Produktidentifikation|||||||||||
|SG9|||||||||||
|SG9|PIA||00027||Muss|Muss|Muss||||


Version: 3.1f 30.09.2025 Seite 86 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|EDIFACT Struktur|Beschreibung<br/>Prüfidentifikator|normiertes Profil<br/>13010|Profilschar<br/>13011|TEP vergh. Werte Referenzmessung<br/>13012|Bedingung||||
|-|-|-|-|-|-|-|-|-|
|SG9|PIA|4347|5|Produktidentifikation|X|X|X||
|SG9|PIA|7140|Medium / OBIS-Kennzahl|X \[501]|X \[501]|X \[501]|\[501] Hinweis: Es sind nur die Werte erlaubt, die in der EDI\@Energy Codeliste der OBIS-Kennzahlen und Medien mit dem entsprechenden Prüfidentifikator versehen sind.||
|SG9|PIA|7143|SRW|OBIS-Kennzahl|X|X \[17]|X|\[17] Wenn nicht SG9 PIA+5+1-b?:9.99.0 (b= Kanal: Wert gemäß Codeliste der OBIS-Kennzahlen und Medien)<br/>\[18] Wenn SG9 PIA+5+1-b?:9.99.0 (b= Kanal: Wert gemäß Codeliste der OBIS-Kennzahlen und Medien)|
||Z02|BDEW OBIS-ähnliche Kennzahl||X \[18]|||||
|Mengenangaben|||||||||
|SG10|||Muss|Muss|Muss||||
|SG10|QTY|00028||Muss|Muss|Muss|||
|SG10|QTY|6063|187|Prognosewert|X|X|X||
|SG10|QTY|6060|Menge|X \[902] ∧ \[906] ∧ \[917]|X \[902] ∧ \[925]|X \[902] ∧ \[906]|\[902] Format: Möglicher Wert: ≥ 0<br/>\[906] Format: max. 3 Nachkommastellen<br/>\[917] Format: max. 4 Vorkommastellen<br/>\[925] Format: max. 5 Nachkommastellen||
|Beginn Messperiode|||||||||
|SG10|||||||||
|SG10|DTM|00029||Muss||Muss|||
|SG10|DTM|2005|163|Verarbeitung, Beginndatum/-zeit|X||X||
|SG10|DTM|2380|Datum oder Uhrzeit oder Zeitspanne, Wert|X \[931]||X \[931]|\[931] Format: ZZZ = +00||
|SG10|DTM|2379|303|CCYYMMDDHHMMZZZ|X||X||
|Ende Messperiode|||||||||
|SG10|||||||||
|SG10|DTM|00030||Muss||Muss|||
|SG10|DTM|2005|164|Verarbeitung, Endedatum/-zeit|X||X||
|SG10|DTM|2380|Datum oder Uhrzeit oder Zeitspanne, Wert|X \[931]||X \[931]|\[931] Format: ZZZ = +00||
|SG10|DTM|2379|303|CCYYMMDDHHMMZZZ|X||X||
|Nachrichten-Endesegment|||||||||
|UNT|00041||Muss|Muss|Muss||||
|UNT|0074|Anzahl der Segmente in einer Nachricht|X|X|X||||
|UNT|0062|Nachrichten-Referenznummer|X|X|X||||
|Nutzdaten-Endesegment|||||||||
|UNZ|00042||Muss|Muss|Muss||||
|UNZ|0036|Datenaustauschzähler|X|X|X||||
|UNZ|0020|Datenaustauschreferenz|X|X|X||||


Version: 3.1f 30.09.2025 Seite 87 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

## 8.2 Darstellung verwendete Codes zu Summenzeitreihen

### OBIS-Kennzahlen zu Summenzeitreihen (1/2)

```description
Diagram showing the relationship between different market roles (BG, BK, RZ) and the corresponding OBIS codes for energy quantities and balances.
```

|Kategorie|Quelle/Ziel|Flussrichtung & Beschreibung|OBIS-Kennzahl|Ziel/Quelle||
|-|-|-|-|-|-|
|Energiemengen|BG (grün)|← LGS, SLS, TLS, VZR (Entnahmen aus dem BK)|1-1:1.29.0|BK (gelb)||
||BG (grün)|→ EGS, SES, TES, EE-Einspeise-Zeitreihen (Einspeisungen in den BK)|1-1:2.29.0|BK (gelb)||
||RZ (braun)|← LGS, SLS (Entnahmen aus dem BK)|1-1:1.29.0|BK (gelb)||
||RZ (braun)|→ EGS, EE-Einspeise-Zeitreihen (Einspeisungen in den BK)|1-1:2.29.0|BK (gelb)||
||BG (grün)|← LGS, SLS (Entnahmen aus RZ)|1-1:1.29.0|RZ (braun)||
||BG (grün)|→ EGS, gemessene EE-Einspeise-Zeitreihen (Einspeisungen in RZ)|1-1:2.29.0|RZ (braun)||
|Salden|BG des benachbarten NB (grün)|← NZR (Export aus BG des für NZR-Bildung verantwortlichen NB)|1-1:1.29.0|BG des für NZR-Bildung verantwortlicher NB (grün)||
||BG des benachbarten NB (grün)|→ NZR (Import in BG des für NZR-Bildung verantwortlichen NB)|1-1:2.29.0|BG des für NZR-Bildung verantwortlicher NB (grün)||
||BG (grün)|← DBA, NB-DZR (Export aus BK bei Überdeckung im BG)|1-1:1.29.0|BK (gelb)||
||BG (grün)|→ DBA, NB-DZR (Import in BK bei Unterdeckung im BG)|1-1:2.29.0|BK (gelb)||
||RZ (braun)|← ÜNB-DZR (Export aus BK bei Überdeckung in RZ)|1-1:1.29.0|BK (gelb)||
||RZ (braun)|→ ÜNB-DZR (Import in BK bei Unterdeckung in RZ)|1-1:2.29.0|BK (gelb)||


BG = Bilanzierungsgebiet
BK = Bilanzkreis
RZ = Regelzone
U-BK = Unter-Bilanzkreis

Version: 3.1f
30.09.2025
Seite 88 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

# OBIS-Kennzahlen zu Summenzeitreihen (2/2)

|Kategorie|Sender|Richtung / Beschreibung|Kennung|OBIS|Empfänger|
|-|-|-|-|-|-|
|Salden|BG|\<mark style="background-color: red">← DZÜ (Export aus RZ)|DZÜ|1-1:1.29.0|RZ|
|||\<mark style="background-color: blue">→ DZÜ (Import in RZ)|DZÜ|1-1:2.29.0||
||RZ|\<mark style="background-color: red">← BAS (Überdeckung BK)|BAS|1-1:1.29.0|BK|
|||\<mark style="background-color: blue">→ BAS (Unterdeckung BK)|BAS|1-1:2.29.0||
||BK|\<mark style="background-color: red">← BAS (Überdeckung Unter-BK)|BAS|1-1:1.29.0|U-BK|
|||\<mark style="background-color: blue">→ BAS (Unterdeckung Unter-BK)|BAS|1-1:2.29.0||
|Fahrpläne|BK|\<mark style="background-color: red">← 0...n|FPE|1-1:1.29.0|BK|
|||\<mark style="background-color: blue">→ 0...m|FPI|1-1:2.29.0||
||Regelenergie BK ÜNB|\<mark style="background-color: red">←|SRE|1-1:1.29.0|SRL-Erbring. BK|
|||\<mark style="background-color: blue">→|SRI|1-1:2.29.0||
|EEG-Überführungszeitreihen|ÜNB-EEG-BK|\<mark style="background-color: red">← BI1, BI2, BI3, GAA, GAB, GAC, GE1, GE2, GE3, SO1, SO2, SO3, WF1, WF2, WF3, WN1, WN2, WN3, WAA, WAB, WAC||1-1:1.29.0|NB-EEG-BK|


**BG** = Bilanzierungsgebiet | **BK** = Bilanzkreis | **RZ** = Regelzone | **U-BK** = Unter-Bilanzkreis

Version: 3.1f | 30.09.2025 | Seite 89 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

## Medien und Vorzeichen zur Ausfallarbeitsüberführungszeitreihe

|Redispatch 2.0|BK RD-BK des ANB|BK RD-BK des ANB|BK des LF|BK des LF|
|-|-|-|-|-|
|Redispatch 2.0|\<span style="color:red">←\</span>|AUS (bei Überdeckung durch RD)<br/>(Entnahmen aus dem BK)|Vorzeichen (-)||
||\<span style="color:blue">→\</span>|AUS (bei Unterdeckung durch RD)<br/>(Einspeisung in den BK des LF)|Vorzeichen (+)||
|Redispatch 2.0|BK RD-BK des anfNB||BK RD-BK des ANB||
|Redispatch 2.0|\<span style="color:red">←\</span>|AUS (bei Überdeckung durch RD)<br/>(Entnahmen aus dem BK des ANB)|Vorzeichen (-)||
||\<span style="color:blue">→\</span>|AUS (bei Unterdeckung durch RD)<br/>(Einspeisungen in den BK des ANB)|Vorzeichen (+)||


## Medien und Vorzeichen zur EEG-Überführungszeitreihe aufgrund von Ausfallarbeit

|Redispatch 2.0|NB-EEG-BK RD-BK des|NB-EEG-BK RD-BK des|ÜNB-EEG-BK|ÜNB-EEG-BK|
|-|-|-|-|-|
|Redispatch 2.0|\<span style="color:red">←\</span>|AU1 (bei Überdeckung durch RD)<br/>Entnahme aus dem ÜNB-EEG-BK|Vorzeichen (-)||
||\<span style="color:blue">→\</span>|AU1 (bei Unterdeckung durch RD)<br/>Einspeisungen in den ÜNB-EEG-BK|Vorzeichen (+)||


BG = Bilanzierungsgebiet | BK = Bilanzkreis | RZ = Regelzone | U-BK = Unter-Bilanzkreis

### 8.3 Summenzeitreihen und Ausfallarbeitssummen

#### 8.3.1 Übertragung Summenzeitreihe

Tabellenspalte = Summenzeitreihe 13003

Dieser Anwendungsfall dient zur Übertragung von Summenzeitreihen.

Kommunikationspartner, Identifikationsangabe und Art der Werte für diesen Anwendungsfall:

|Sparte|Kommunikation von|Art der Werte|Identifikationsangabe in SG6 LOC|Anmerkung|
|-|-|-|-|-|
|Strom|NB an BIKO|Summenzeitreihe|ID des MaBiS-ZP|--|
|Strom|BIKO an BKV|Summenzeitreihe|ID des MaBiS-ZP|--|
|Strom|BIKO an NB|Summenzeitreihe|ID des MaBiS-ZP|--|
|Strom|BIKO an ÜNB|Summenzeitreihe|ID des MaBiS-ZP|--|
|Strom|NB an LF|Summenzeitreihe|ID des MaBiS-ZP|--|
|Strom|NB an NB|Summenzeitreihe|ID des MaBiS-ZP|--|
|Strom|ÜNB an BIKO|Summenzeitreihe|ID des MaBiS-ZP|--|
|Strom|ÜNB an LF|Summenzeitreihe|ID des MaBiS-ZP|--|
|Strom|ÜNB an NB|Summenzeitreihe|ID des MaBiS-ZP|--|
|Strom|ÜNB an BKV|Summenzeitreihe|ID des MaBiS-ZP|--|
|Strom|NB an NB|--|ID des MaBiS-ZP|Zur Abstimmung der Netzzeitreihen|
|Strom|NB an ÜNB|Summenzeitreihe|ID des MaBiS-ZP|tägliche BK-SZR eMob|


Version: 3.1f 30.09.2025 Seite 90 von 158

MSCONS Anwendungshandbuch
![edi@energy. Datenformate Strom & Gas](image)

### 8.3.2 Übertragung Ausfallarbeitssummen

Tabellenspalte = Redispatch 2.0 Ausfallarbeitssummenzeitreihe 13023

Dieser Anwendungsfall dient zur Übertragung der Ausfallarbeitssummenzeitreihe.

Kommunikationspartner, Identifikationsangabe und Art der Werte für diesen Anwendungsfall:

|Sparte|Kommunikation von|Art der Werte|Identifikationsangabe in SG6 LOC|Anmerkung|
|-|-|-|-|-|
|Strom|NB an LF|LF-AASZR|ID des MaBiS-ZP|--|


Version: 3.1f
30.09.2025
Seite 91 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

### 8.3.3 Anwendungsübersicht Summenzeitreihe und Ausfallarbeitssummen

|EDIFACT Struktur|Beschreibung|Summen-zeitreihe|Redispatch 2.0 Ausfallarbeits-summenzeitreihe|Bedingung||
|-|-|-|-|-|-|
||Prüfidentifikator|13003|13023|||
|Nutzdaten-Kopfsegment||||||
|UNB|00002||Muss|Muss||
|UNB|0001|\*\*UNOC\*\* UN/ECE-Zeichensatz C|X|X||
|UNB|0002|\*\*3\*\* Version 3|X|X||
|UNB|0004|MP-ID Absender|X|X||
|UNB|0007|\*\*14\*\* GS1<br/>\*\*500\*\* DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)|X|X||
|UNB|0010|MP-ID Empfänger|X|X||
|UNB|0007|\*\*14\*\* GS1<br/>\*\*500\*\* DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)|X|X||
|UNB|0017|Datum der Erstellung|X|X||
|UNB|0019|Uhrzeit der Erstellung|X|X||
|UNB|0020|Datenaustauschreferenz|X \[918]|X \[918]|\[918] Format: Zeichen aus dem über UNOC definierten Zeichensatz, wobei von den Buchstaben nur Großbuchstaben erlaubt sind.|
|UNB|0026|\*\*TL\*\* Lastgang, beliebiger Zeitraum|X|X||
|Nachrichtenkopfsegment||||||
|UNH|00003||Muss|Muss||
|UNH|0062|Nachrichten-Referenznummer|X|X||
|UNH|0065|\*\*MSCON\*\* Bericht über den<br/>\*\*S\*\* Verbrauch messbarer Dienstleistungen|X|X||
|UNH|0052|\*\*D\*\* Entwurfs-Version|X|X||
|UNH|0054|\*\*04B\*\* Ausgabe 2004 - B|X|X||
|UNH|0051|\*\*UN\*\* UN/CEFACT|X|X||
|UNH|0057|\*\*2.4c\*\* Versionsnummer der zugrundeliegenden BDEW-Nachrichtenbeschreibung|X|X||
|Beginn der Nachricht||||||
|BGM|00004||Muss|Muss||
|BGM|1001|\*\*BK\*\* Zeitreihen im Rahmen der Bilanzkreisabrechnung|X|||
|BGM|1001|\*\*Z39\*\* Tägliche Summenzeitreihe|X|||
|BGM|1001|\*\*Z46\*\* Redispatch Ausfallarbeitssummenzeitreihe||X||
|BGM|1004|Dokumentennummer|X|X||
|BGM|1225|\*\*9\*\* Original|X|X||
|Nachrichtendatum||||||
|DTM|00005||Muss|Muss||
|DTM|2005|\*\*137\*\* Dokumenten-/Nachrichtendatum/-zeit|X|X||


Version: 3.1f 30.09.2025 Seite 92 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|EDIFACT Struktur||Beschreibung<br/>Prüfidentifikator||Summen-zeitreihe<br/>13003|Redispatch 2.0 Ausfallarbeits-summenzeitreihe<br/>13023|Bedingung||
|-|-|-|-|-|-|-|-|
|DTM|2380||Datum oder Uhrzeit oder Zeitspanne, Wert|X \[931] \[494]|X \[931] \[494]|\[494] Das hier genannte Datum muss der Zeitpunkt sein, zu dem das Dokument erstellt wurde, oder ein Zeitpunkt, der davor liegt.<br/>\[931] Format: ZZZ = +00||
|DTM|2379||303|CCYYMMDDHHMMZZZ|X|X||
|Prüfidentifikator||||||||
|SG1||||Muss|Muss|||
|SG1|RFF||00009||Muss|Muss||
|SG1|RFF|1153|Z13|Prüfidentifikator|X|X||
|SG1|RFF|1154|13003|Summenzeitreihe|X|||
||||13023|Redispatch Ausfallarbeitssummenzeitreihe||X||
|MP-ID Absender||||||||
|SG2||||Muss|Muss|||
|SG2|NAD||00010||Muss|Muss||
|SG2|NAD|3035|MS|Dokumenten-/Nachrichtenaussteller bzw. -absender|X|X||
|SG2|NAD|3039|MP-ID||X \[117]|X \[117]|\[117] Nur MP-ID aus Sparte Strom|
|SG2|NAD|3055|9|GS1|X|X||
||||293|DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)|X|X||
|Ansprechpartner||||||||
|SG4||||Kann|Kann|||
|SG4|CTA||00011||Muss|Muss||
|SG4|CTA|3139|IC|Informationsstelle|X|X||
|SG4|CTA|3412|Abteilung oder Bearbeiter|X|X|||
|Kommunikationsverbindung||||||||
|SG4||||Muss|Muss|||
|SG4|COM||00012||Muss|Muss||
|SG4|COM|3148|Kommunikationsadresse, Identifikation|X ((\[939] \[142]) ∨ (\[940] \[143])) ∧ \[576]|X ((\[939] \[142]) ∨ (\[940] \[143])) ∧ \[576]|\[142] wenn im DE3155 in demselben COM der Code EM vorhanden ist<br/>\[143] wenn im DE3155 in demselben COM der Code TE / FX / AJ / AL vorhanden ist<br/>\[576] Hinweis: Es darf nur eine Information im DE3148 übermittelt werden<br/>\[939] Format: Die Zeichenkette muss die Zeichen @ und . enthalten<br/>\[940] Format: Die Zeichenkette muss mit dem Zeichen + beginnen und danach dürfen nur noch Ziffern folgen||
|SG4|COM|3155|TE|Telefon|X \[1P0..1]|X \[1P0..1]||
||||EM|E-Mail|X \[1P0..1]|X \[1P0..1]||
||||AJ|weiteres Telefon|X \[1P0..1]|X \[1P0..1]||
||||AL|Handy|X \[1P0..1]|X \[1P0..1]||
||||FX|Telefax|X \[1P0..1]|X \[1P0..1]||
|MP-ID Empfänger||||||||
|SG2||||Muss|Muss|||
|SG2|NAD||00013||Muss|Muss||
|SG2|NAD|3035|MR|Nachrichtenempfänger|X|X||
|SG2|NAD|3039|MP-ID||X \[117]|X \[117]|\[117] Nur MP-ID aus Sparte Strom|


Version: 3.1f	30.09.2025	Seite 93 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|EDIFACT Struktur|Beschreibung<br/>Prüfidentifikator|Summen-zeitreihe<br/>13003|Redispatch 2.0 Ausfallarbeits-summenzeitreihe<br/>13023|Bedingung||||
|-|-|-|-|-|-|-|-|
|SG2|NAD|3055|9|GS1|X|X||
||293|DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)|X|X||||
|Abschnitts-Kontrollsegment||||||||
|UNS|00014|Muss|Muss|||||
|UNS|0081|D|Trennung von Kopf- und Positionsteil|X|X|||
|Name und Adresse||||||||
|SG5|Muss \[2001]|Muss \[2001]|\[2001] Segmentgruppe ist nur einmal je UNH anzugeben|||||
|SG5|NAD|00015|Muss|Muss||||
|SG5|NAD|3035|DP|Lieferanschrift|X|X||
|Identifikationsangabe||||||||
|SG6|Muss|Muss||||||
|SG6|LOC|00017|Muss|Muss||||
|SG6|LOC|3227|172|Meldepunkt|X|X||
|SG6|LOC|3225|Bezeichnung|X \[951] \[511]|X \[951] \[511]|\[511] Hinweis: Verwendung der ID des MaBiS-ZP<br/>\[951] Format: Zählpunktbezeichnung||
|Bilanzierungsmonat||||||||
|SG6|Muss \[70]|Muss|\[70] Wenn BGM+BK vorhanden|||||
|SG6|DTM|00020|Muss \[70]|Muss||||
|SG6|DTM|2005|492|Bilanzierungsdatum, -zeit, -periode|X|X||
|SG6|DTM|2380|Datum oder Uhrzeit oder Zeitspanne, Wert|X|X|||
|SG6|DTM|2379|610|CCYYMM|X|X||
|Versionsangabe||||||||
|SG6|Muss \[70]|Muss|\[70] Wenn BGM+BK vorhanden|||||
|SG6|DTM|00021|Muss \[70]|Muss||||
|SG6|DTM|2005|293|Fertigstellungsdatum/-zeit|X|X||
|SG6|DTM|2380|Datum oder Uhrzeit oder Zeitspanne, Wert|X \[931]|X \[931]|\[931] Format: ZZZ = +00||
|SG6|DTM|2379|304|CCYYMMDDHHMMSSZZZ|X|X||
|lfd. Position||||||||
|SG9|Muss|Muss||||||
|SG9|LIN|00026|Muss|Muss||||
|SG9|LIN|1082|Positionsnummer|X \[908]|X \[908]|\[908] Format: Mögliche Werte: 1 bis n||
|Produktidentifikation||||||||
|SG9|Muss|Muss||||||
|SG9|PIA|00027|Muss|Muss||||
|SG9|PIA|4347|5|Produktidentifikation|X|X||
|SG9|PIA|7140|Medium / OBIS-Kennzahl|X \[501]|X \[501]|\[501] Hinweis: Es sind nur die Werte erlaubt, die in der EDI\@Energy Codeliste der OBIS-Kennzahlen und Medien mit dem entsprechenden Prüfidentifikator versehen sind.||
|SG9|PIA|7143|SRW|OBIS-Kennzahl|X|||
||Z08|Medium||X||||
|Mengenangaben||||||||
|SG10|Muss|Muss||||||
|SG10|QTY|00028|Muss|Muss||||


Version: 3.1f 30.09.2025 Seite 94 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|EDIFACT Struktur|Beschreibung<br/>Prüfidentifikator|Summen-zeitreihe<br/>13003|Redispatch 2.0 Ausfallarbeits-summenzeitreihe<br/>13023|Bedingung|
|-|-|-|-|-|
|SG10 QTY 6063|220 Wahrer Wert|X \[71]||\[70] Wenn BGM+BK vorhanden|
|SG10 QTY 6063|67 Ersatzwert|X \[71]||\[71] Wenn BGM+Z39 vorhanden|
|SG10 QTY 6063|79 Energiemenge summiert (Summenwert, Bilanzsumme)|X \[70]|X||
|SG10 QTY 6063|Z18 Vorläufiger Wert|X \[71]|||
|SG10 QTY 6063|Z30 Fehlender Wert|X \[71]|||
|SG10 QTY 6060|Menge|X \[902] ∧ \[906]|X \[910] ∧ \[906]|\[902] Format: Möglicher Wert: ≥ 0<br/>\[906] Format: max. 3 Nachkommastellen<br/>\[910] Format: Möglicher Wert: < 0 oder ≥ 0|
|SG10 QTY 6411|KWH Kilowattstunde||X||
|Beginn Messperiode|||||
|SG10|||||
|SG10 DTM 00029||Muss|Muss||
|SG10 DTM 2005|163 Verarbeitung, Beginndatum/-zeit|X|X||
|SG10 DTM 2380|Datum oder Uhrzeit oder Zeitspanne, Wert|X \[931] \[495]|X \[931] \[495]|\[495] Der Zeitpunkt muss ≤ dem Wert im DE2380 des DTM+137 sein<br/>\[931] Format: ZZZ = +00|
|SG10 DTM 2379|303 CCYYMMDDHHMMZZZ|X|X||
|Ende Messperiode|||||
|SG10|||||
|SG10 DTM 00030||Muss|Muss||
|SG10 DTM 2005|164 Verarbeitung, Endedatum/-zeit|X|X||
|SG10 DTM 2380|Datum oder Uhrzeit oder Zeitspanne, Wert|X \[931] \[495]|X \[931] \[495]|\[495] Der Zeitpunkt muss ≤ dem Wert im DE2380 des DTM+137 sein<br/>\[931] Format: ZZZ = +00|
|SG10 DTM 2379|303 CCYYMMDDHHMMZZZ|X|X||
|Nachrichten-Endesegment|||||
|UNT 00041||Muss|Muss||
|UNT 0074|Anzahl der Segmente in einer Nachricht|X|X||
|UNT 0062|Nachrichten-Referenznummer|X|X||
|Nutzdaten-Endesegment|||||
|UNZ 00042||Muss|Muss||
|UNZ 0036|Datenaustauschzähler|X|X||
|UNZ 0020|Datenaustauschreferenz|X|X||


Version: 3.1f 30.09.2025 Seite 95 von 158

MSCONS Anwendungshandbuch
![edi@energy. Datenformate Strom & Gas](image)

## 8.4 Überführungszeitreihen

### 8.4.1 Übertragung EEG-Überführungszeitreihen

Tabellenspalte = EEG-Überführungs-ZR 13005

Dieser Anwendungsfall dient zur Übertragung der EEG-Überführungs-Zeitreihe.

Kommunikationspartner, Identifikationsangabe und Art der Werte für diesen Anwendungsfall:

|Sparte|Kommunikation von|Art der Werte|Identifikationsangabe in SG6 LOC|Anmerkung|
|-|-|-|-|-|
|Strom|BIKO an NB|EEG-Überführungs-Zeitreihe|Bilanzkreis von<br/>Bilanzkreis an<br/>Bilanzierungsgebiet|--|
|Strom|BIKO an BKV|EEG-Überführungs-Zeitreihe|Bilanzkreis von<br/>Bilanzkreis an<br/>Bilanzierungsgebiet|--|


### 8.4.2 Übertragung EEG-Überführungszeitreihe aufgrund von Ausfallarbeit

Tabellenspalte = EEG-Überführungs-ZR aufgrund Ausfallarbeit 13026

Dieser Anwendungsfall dient zur Übertragung der EEG-Überführungs-Zeitreihe aufgrund von Ausfallarbeit.

Kommunikationspartner, Identifikationsangabe und Art der Werte für diesen Anwendungsfall:

|Sparte|Kommunikation von|Art der Werte|Identifikationsangabe in SG6 LOC|Anmerkung|
|-|-|-|-|-|
|Strom|BIKO an NB|EEG-Überführungs-Zeitreihe aufgrund von Ausfallarbeit|Bilanzkreis von<br/>Bilanzkreis an<br/>Bilanzierungsgebiet|--|
|Strom|BIKO an BKV|EEG-Überführungs-Zeitreihe aufgrund von Ausfallarbeit|Bilanzkreis von<br/>Bilanzkreis an<br/>Bilanzierungsgebiet|--|


### 8.4.3 Übertragung Ausfallarbeitsüberführungszeitreihe

Tabellenspalte = Ausfallarbeitsüberführungszeitreihe 13020

Dieser Anwendungsfall dient zur Übertragung der Ausfallarbeitsüberführungszeitreihe.

Kommunikationspartner, Identifikationsangabe und Art der Werte für diesen Anwendungsfall:

|Sparte|Kommunikation von|Art der Werte|Identifikationsangabe in SG6 LOC|Anmerkung|
|-|-|-|-|-|
|Strom|NB an ÜNB|Tägliche Überführungszeitreihe der Ausfallarbeit|ID des MaBiS-ZP|--|
|Strom|NB an BIKO|Monatliche Überführungszeitreihe der Ausfallarbeit|ID des MaBiS-ZP|--|
|Strom|BIKO an BKV (des LF)|Monatliche Überführungszeitreihe der Ausfallarbeit|ID des MaBiS-ZP|--|


Version: 3.1f 30.09.2025 Seite 96 von 158

MSCONS Anwendungshandbuch
![edi@energy. Datenformate Strom & Gas](image)

|Sparte|Kommunikation von|Art der Werte|Identifikationsangabe in SG6 LOC|Anmerkung|
|-|-|-|-|-|
|Strom|BIKO an BKV<br/>(des anfNB)|Monatliche Überführungszeitreihe der Ausfallarbeit|ID des MaBiS-ZP|--|


Version: 3.1f	30.09.2025	Seite 97 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

## 8.4.4 Anwendungsübersicht EEG-Überführungszeitreihen

|EDIFACT Struktur|Beschreibung<br/>Prüfidentifikator|EEG-Überführungs-ZR<br/>13005|EEG-Überführungs-ZR aufgrund Ausfallarbeit<br/>13026|Bedingung|||
|-|-|-|-|-|-|-|
|Nutzdaten-Kopfsegment|||||||
|UNB|00002|Muss|Muss||||
|UNB|0001|UNOC|UN/ECE-Zeichensatz C|X|X||
|UNB|0002|3|Version 3|X|X||
|UNB|0004|MP-ID Absender|X|X|||
|UNB|0007|14|GS1|X|X||
||500|DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)|X|X|||
|UNB|0010|MP-ID Empfänger|X|X|||
|UNB|0007|14|GS1|X|X||
||500|DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)|X|X|||
|UNB|0017|Datum der Erstellung|X|X|||
|UNB|0019|Uhrzeit der Erstellung|X|X|||
|UNB|0020|Datenaustauschreferenz|X \[918]|X \[918]|\[918] Format: Zeichen aus dem über UNOC definierten Zeichensatz, wobei von den Buchstaben nur Großbuchstaben erlaubt sind.||
|UNB|0026|TL|Lastgang, beliebiger Zeitraum|X|X||
|Nachrichtenkopfsegment|||||||
|UNH|00003|Muss|Muss||||
|UNH|0062|Nachrichten-Referenznummer|X|X|||
|UNH|0065|MSCONS|Bericht über den Verbrauch messbarer Dienstleistungen|X|X||
|UNH|0052|D|Entwurfs-Version|X|X||
|UNH|0054|04B|Ausgabe 2004 - B|X|X||
|UNH|0051|UN|UN/CEFACT|X|X||
|UNH|0057|2.4c|Versionsnummer der zugrundeliegenden BDEW-Nachrichtenbeschreibung|X|X||
|Beginn der Nachricht|||||||
|BGM|00004|Muss|Muss||||
|BGM|1001|Z15|EEG-Überführungszeitreihe|X|||
||Z50|Redispatch EEG-Überführungszeitreihe aufgrund Ausfallarbeit||X|||
|BGM|1004|Dokumentennummer|X|X|||
|BGM|1225|9|Original|X|X||
|Nachrichtendatum|||||||
|DTM|00005|Muss|Muss||||
|DTM|2005|137|Dokumenten-/Nachrichtendatum/-zeit|X|X||
|DTM|2380|Datum oder Uhrzeit oder Zeitspanne, Wert|X \[931] \[494]|X \[931] \[494]|\[494] Das hier genannte Datum muss der Zeitpunkt sein, zu dem das Dokument erstellt wurde, oder ein Zeitpunkt, der davor liegt.<br/>\[931] Format: ZZZ = +00||


Version: 3.1f
30.09.2025
Seite 98 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|EDIFACT Struktur|Beschreibung<br/>Prüfidentifikator|EEG-Überführungs-ZR<br/>13005|EEG-Überführungs-ZR aufgrund Ausfallarbeit<br/>13026|Bedingung||||
|-|-|-|-|-|-|-|-|
|DTM|2379|303|CCYYMMDDHHMMZZZ|X|X|||
|Prüfidentifikator||||||||
|SG1|||Muss|Muss||||
|SG1|RFF|00009|||Muss|Muss||
|SG1|RFF|1153|Z13|Prüfidentifikator|X|X||
|SG1|RFF|1154|13005|EEG-Überf.ZR|X|||
||13026|Redispatch EEG-Überführungszeitreihe aufgrund Ausfallarbeit||X||||
|MP-ID Absender||||||||
|SG2|||Muss|Muss||||
|SG2|NAD|00010|||Muss|Muss||
|SG2|NAD|3035|MS|Dokumenten-/Nachrichtenaussteller bzw. -absender|X|X||
|SG2|NAD|3039|MP-ID||X \[117]|X \[117]|\[117] Nur MP-ID aus Sparte Strom|
|SG2|NAD|3055|9|GS1|X|X||
||293|DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)|X|X||||
|Ansprechpartner||||||||
|SG4|||Kann|Kann||||
|SG4|CTA|00011|||Muss|Muss||
|SG4|CTA|3139|IC|Informationsstelle|X|X||
|SG4|CTA|3412|Abteilung oder Bearbeiter|X|X|||
|Kommunikationsverbindung||||||||
|SG4||||||||
|SG4|COM|00012|||Muss|Muss||
|SG4|COM|3148|Kommunikationsadresse, Identifikation|X ((\[939] \[142]) ∨ (\[940] \[143])) ∧ \[576]|X ((\[939] \[142]) ∨ (\[940] \[143])) ∧ \[576]|\[142] wenn im DE3155 in demselben COM der Code EM vorhanden ist<br/>\[143] wenn im DE3155 in demselben COM der Code TE / FX / AJ / AL vorhanden ist<br/>\[576] Hinweis: Es darf nur eine Information im DE3148 übermittelt werden<br/>\[939] Format: Die Zeichenkette muss die Zeichen @ und . enthalten<br/>\[940] Format: Die Zeichenkette muss mit dem Zeichen + beginnen und danach dürfen nur noch Ziffern folgen||
|SG4|COM|3155|TE|Telefon|X \[1P0..1]|X \[1P0..1]||
||EM|E-Mail|X \[1P0..1]|X \[1P0..1]||||
||AJ|weiteres Telefon|X \[1P0..1]|X \[1P0..1]||||
||AL|Handy|X \[1P0..1]|X \[1P0..1]||||
||FX|Telefax|X \[1P0..1]|X \[1P0..1]||||
|MP-ID Empfänger||||||||
|SG2|||Muss|Muss||||
|SG2|NAD|00013|||Muss|Muss||
|SG2|NAD|3035|MR|Nachrichtenempfänger|X|X||
|SG2|NAD|3039|MP-ID||X \[117]|X \[117]|\[117] Nur MP-ID aus Sparte Strom|
|SG2|NAD|3055|9|GS1|X|X||
||293|DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)|X|X||||


Version: 3.1f 30.09.2025 Seite 99 von 158

MSCONS Anwendungshandbuch
![edi@energy. Datenformate Strom & Gas](image)

|EDIFACT Struktur||Beschreibung<br/>Prüfidentifikator||EEG-Überführungs-ZR<br/>13005||EEG-Überführungs-ZR aufgrund Ausfallarbeit<br/>13026||Bedingung|||
|-|-|-|-|-|-|-|-|-|-|-|
|Abschnitts-Kontrollsegment|||||Muss||Muss||||
|\*\*UNS\*\*||00014|||Muss||Muss||||
|UNS|0081||\*\*D\*\*|Trennung von Kopf- und Positionsteil|X|X|||||
|Name und Adresse|||||Muss \[2001]||Muss \[2001]||\[2001] Segmentgruppe ist nur einmal je UNH anzugeben||
|\*\*SG5\*\*|||||||||||
|SG5|\*\*NAD\*\*||00015|||Muss||Muss|||
|SG5|NAD|3035|\*\*Z15\*\*|Überführungszeitreihe|X|X|||||
|Bilanzkreis|||||Muss||Muss||||
|\*\*SG6\*\*|||||||||||
|SG6|\*\*LOC\*\*||00016|||Muss||Muss|||
|SG6|LOC|3227|\*\*237\*\*|Bilanzkreis|X|X|||||
|SG6|LOC|3225||Bilanzkreis an|X \[904] \[512]|X \[904] \[512]|\[512] Hinweis: Verwendung der Bilanzkreisbezeichnung<br/>\[904] Format: genau 16 Stellen||||
|SG6|LOC|3223||Bilanzkreis von|X \[904] \[512]|X \[904] \[512]|\[512] Hinweis: Verwendung der Bilanzkreisbezeichnung<br/>\[904] Format: genau 16 Stellen||||
|Identifikationsangabe|||||Muss||Muss||||
|\*\*SG6\*\*|||||||||||
|SG6|\*\*LOC\*\*||00017|||Muss||Muss|||
|SG6|LOC|3227|\*\*107\*\*|Bilanzierungsgebiet|X|X|||||
|SG6|LOC|3225||Bezeichnung|X \[904] \[513]|X \[904] \[513]|\[513] Hinweis: Verwendung der Bezeichnung des Bilanzierungsgebietes<br/>\[904] Format: genau 16 Stellen||||
|Beginn Messperiode Übertragungszeitraum|||||Muss||Muss||||
|\*\*SG6\*\*|||||||||||
|SG6|\*\*DTM\*\*||00018|||Muss||Muss|||
|SG6|DTM|2005|\*\*163\*\*|Verarbeitung, Beginndatum/-zeit|X|X|||||
|SG6|DTM|2380||Datum oder Uhrzeit oder Zeitspanne, Wert|X \[931]|X \[931]|\[931] Format: ZZZ = +00||||
|SG6|DTM|2379|\*\*303\*\*|CCYYMMDDHHMMZZZ|X|X|||||
|Ende Messperiode Übertragungszeitraum|||||Muss||Muss||||
|\*\*SG6\*\*|||||||||||
|SG6|\*\*DTM\*\*||00019|||Muss||Muss|||
|SG6|DTM|2005|\*\*164\*\*|Verarbeitung, Endedatum/-zeit|X|X|||||
|SG6|DTM|2380||Datum oder Uhrzeit oder Zeitspanne, Wert|X \[931]|X \[931]|\[931] Format: ZZZ = +00||||
|SG6|DTM|2379|\*\*303\*\*|CCYYMMDDHHMMZZZ|X|X|||||
|Versionsangabe|||||Muss||Muss||||
|\*\*SG6\*\*|||||||||||
|SG6|\*\*DTM\*\*||00021|||Muss||Muss|||
|SG6|DTM|2005|\*\*293\*\*|Fertigstellungsdatum/-zeit|X|X|||||
|SG6|DTM|2380||Datum oder Uhrzeit oder Zeitspanne, Wert|X \[931]|X|\[931] Format: ZZZ = +00||||
|SG6|DTM|2379|\*\*304\*\*|CCYYMMDDHHMMSSZZZ|X|X|||||
|Zeitreihentyp|||||Muss||Muss||||
|\*\*SG8\*\*|||||||||||
|SG8|\*\*CCI\*\*||00025|||Muss||Muss|||
|SG8|CCI|7059|\*\*15\*\*|Struktur|X|X|||||
|SG8|CCI|7037||Zeitreihentyp|X|X|||||
|lfd. Position|||||||||||


Version: 3.1f 30.09.2025 Seite 100 von 158

MSCONS Anwendungshandbuch
![edi@energy Datenformate Strom & Gas](image)

|EDIFACT Struktur||Beschreibung<br/>Prüfidentifikator||EEG-Überführungs-ZR<br/>13005||EEG-Überführungs-ZR aufgrund Ausfallarbeit<br/>13026||Bedingung|||
|-|-|-|-|-|-|-|-|-|-|-|
|\*\*SG9\*\*||||\*\*Muss\*\*||\*\*Muss\*\*|||||
|SG9|LIN||00026|||Muss||Muss|||
|SG9|LIN|1082||Positionsnummer||X \[908]||X \[908]||\[908] Format: Mögliche Werte: 1 bis n|
|Produktidentifikation|||||||||||
|\*\*SG9\*\*||||\*\*Muss\*\*||\*\*Muss\*\*|||||
|SG9|PIA||00027|||Muss||Muss|||
|SG9|PIA|4347||\*\*5\*\*|Produktidentifikation|X||X|||
|SG9|PIA|7140||Medium / OBIS-Kennzahl||X \[501]||X \[501]||\[501] Hinweis: Es sind nur die Werte erlaubt, die in der EDI\@Energy Codeliste der OBIS-Kennzahlen und Medien mit dem entsprechenden Prüfidentifikator versehen sind.|
|SG9|PIA|7143||\*\*SRW\*\*|OBIS-Kennzahl|X|||||
|||\*\*Z08\*\*|Medium|||X|||||
|Mengenangaben|||||||||||
|\*\*SG10\*\*||||\*\*Muss\*\*||\*\*Muss\*\*|||||
|SG10|QTY||00028|||Muss||Muss|||
|SG10|QTY|6063||\*\*79\*\*|Energiemenge summiert (Summenwert, Bilanzsumme)|X||X|||
|SG10|QTY|6060||Menge||X \[902] ∧ \[906]||X \[910] ∧ \[906]||\[902] Format: Möglicher Wert: ≥ 0<br/>\[906] Format: max. 3 Nachkommastellen<br/>\[910] Format: Möglicher Wert: < 0 oder ≥ 0|
|SG10|QTY|6411||\*\*KWH\*\*|Kilowattstunde|||X|||
|Beginn Messperiode|||||||||||
|\*\*SG10\*\*||||\*\*Muss\*\*||\*\*Muss\*\*|||||
|SG10|DTM||00029|||Muss||Muss|||
|SG10|DTM|2005||\*\*163\*\*|Verarbeitung, Beginndatum/-zeit|X||X|||
|SG10|DTM|2380||Datum oder Uhrzeit oder Zeitspanne, Wert||X \[931] \[495]||X \[931] \[495]||\[495] Der Zeitpunkt muss ≤ dem Wert im DE2380 des DTM+137 sein<br/>\[931] Format: ZZZ = +00|
|SG10|DTM|2379||\*\*303\*\*|CCYYMMDDHHMMZZZ|X||X|||
|Ende Messperiode|||||||||||
|\*\*SG10\*\*||||\*\*Muss\*\*||\*\*Muss\*\*|||||
|SG10|DTM||00030|||Muss||Muss|||
|SG10|DTM|2005||\*\*164\*\*|Verarbeitung, Endedatum/-zeit|X||X|||
|SG10|DTM|2380||Datum oder Uhrzeit oder Zeitspanne, Wert||X \[931] \[495]||X \[931] \[495]||\[495] Der Zeitpunkt muss ≤ dem Wert im DE2380 des DTM+137 sein<br/>\[931] Format: ZZZ = +00|
|SG10|DTM|2379||\*\*303\*\*|CCYYMMDDHHMMZZZ|X||X|||
|Nachrichten-Endesegment|||||||||||
|\*\*UNT\*\*||00041|||\*\*Muss\*\*||\*\*Muss\*\*||||
|UNT|0074||Anzahl der Segmente in einer Nachricht||X||X||||
|UNT|0062||Nachrichten-Referenznummer||X||X||||
|Nutzdaten-Endesegment|||||||||||
|\*\*UNZ\*\*||00042|||\*\*Muss\*\*||\*\*Muss\*\*||||
|UNZ|0036||Datenaustauschzähler||X||X||||
|UNZ|0020||Datenaustauschreferenz||X||X||||


Version: 3.1f 30.09.2025 Seite 101 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

### 8.4.5 Anwendungsübersicht Ausfallarbeitsüberführungszeitreihe

|EDIFACT Struktur|Beschreibung<br/>Prüfidentifikator|Ausfallarbeits- überführungszeitreihe<br/>13020|Bedingung|||
|-|-|-|-|-|-|
|Nutzdaten-Kopfsegment||||||
|UNB|00002||Muss|||
|UNB|0001|\*\*UNOC\*\*|UN/ECE-Zeichensatz C|X||
|UNB|0002|\*\*3\*\*|Version 3|X||
|UNB|0004|MP-ID Absender|X|||
|UNB|0007|\*\*14\*\*|GS1|X||
||\*\*500\*\*|DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)|X|||
|UNB|0010|MP-ID Empfänger|X|||
|UNB|0007|\*\*14\*\*|GS1|X||
||\*\*500\*\*|DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)|X|||
|UNB|0017|Datum der Erstellung|X|||
|UNB|0019|Uhrzeit der Erstellung|X|||
|UNB|0020|Datenaustauschreferenz|X \[918]|\[918] Format: Zeichen aus dem über UNOC definierten Zeichensatz, wobei von den Buchstaben nur Großbuchstaben erlaubt sind.||
|UNB|0026|\*\*TL\*\*|Lastgang, beliebiger Zeitraum|X||
|Nachrichtenkopfsegment||||||
|UNH|00003||Muss|||
|UNH|0062|Nachrichten-Referenznummer|X|||
|UNH|0065|\*\*MSCON\*\*|Bericht über den Verbrauch messbarer Dienstleistungen|X||
||\*\*S\*\*|||||
|UNH|0052|\*\*D\*\*|Entwurfs-Version|X||
|UNH|0054|\*\*04B\*\*|Ausgabe 2004 - B|X||
|UNH|0051|\*\*UN\*\*|UN/CEFACT|X||
|UNH|0057|\*\*2.4c\*\*|Versionsnummer der zugrundeliegenden BDEW-Nachrichtenbeschreibung|X||
|Beginn der Nachricht||||||
|BGM|00004||Muss|||
|BGM|1001|\*\*Z43\*\*|Redispatch Ausfallarbeitsüberführungszeitreihe|X||
||\*\*Z69\*\*|Redispatch tägliche Ausfallarbeitsüberführungszeitreihe|X|||
|BGM|1004|Dokumentennummer|X|||
|BGM|1225|\*\*9\*\*|Original|X||
|Nachrichtendatum||||||
|DTM|00005||Muss|||
|DTM|2005|\*\*137\*\*|Dokumenten- /Nachrichtendatum/-zeit|X||
|DTM|2380|Datum oder Uhrzeit oder Zeitspanne, Wert|X \[931] \[494]|\[494] Das hier genannte Datum muss der Zeitpunkt sein, zu dem das Dokument erstellt wurde, oder ein Zeitpunkt, der davor liegt.<br/>\[931] Format: ZZZ = +00||
|DTM|2379|\*\*303\*\*|CCYYMMDDHHMMZZZ|X||
|Prüfidentifikator||||||
|SG1|||Muss|||
|SG1|RFF|00009||Muss||
|SG1|RFF|1153|\*\*Z13\*\*|Prüfidentifikator|X|


Version: 3.1f
30.09.2025
Seite 102 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|EDIFACT Struktur||Beschreibung<br/>Prüfidentifikator||Ausfallarbeits- überführungszeitreihe<br/>13020||Bedingung||
|-|-|-|-|-|-|-|-|
|SG1|RFF|1154||13020|Redispatch Ausfallarbeitsüberführungszeitreihe|X||
|MP-ID Absender||||||||
|SG2||||Muss||||
|SG2|NAD||00010||Muss|||
|SG2|NAD|3035||MS|Dokumenten- /Nachrichtenaussteller bzw. -absender|X||
|SG2|NAD|3039||MP-ID||X \[117]|\[117] Nur MP-ID aus Sparte Strom|
|SG2|NAD|3055||9|GS1|X||
||||293|DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)|X|||
|Ansprechpartner||||||||
|SG4||||Kann||||
|SG4|CTA||00011||Muss|||
|SG4|CTA|3139||IC|Informationsstelle|X||
|SG4|CTA|3412||Abteilung oder Bearbeiter|X|||
|Kommunikationsverbindung||||||||
|SG4||||||||
|SG4|COM||00012||Muss|||
|SG4|COM|3148||Kommunikationsadresse, Identifikation|X ((\[939] \[142]) ∨ (\[940] \[143])) ∧ \[576]|\[142] wenn im DE3155 in demselben COM der Code EM vorhanden ist<br/>\[143] wenn im DE3155 in demselben COM der Code TE / FX / AJ / AL vorhanden ist<br/>\[576] Hinweis: Es darf nur eine Information im DE3148 übermittelt werden<br/>\[939] Format: Die Zeichenkette muss die Zeichen @ und . enthalten<br/>\[940] Format: Die Zeichenkette muss mit dem Zeichen + beginnen und danach dürfen nur noch Ziffern folgen||
|SG4|COM|3155||TE|Telefon|X \[1P0..1]||
||||EM|E-Mail|X \[1P0..1]|||
||||AJ|weiteres Telefon|X \[1P0..1]|||
||||AL|Handy|X \[1P0..1]|||
||||FX|Telefax|X \[1P0..1]|||
|MP-ID Empfänger||||||||
|SG2||||Muss||||
|SG2|NAD||00013||Muss|||
|SG2|NAD|3035||MR|Nachrichtenempfänger|X||
|SG2|NAD|3039||MP-ID||X \[117]|\[117] Nur MP-ID aus Sparte Strom|
|SG2|NAD|3055||9|GS1|X||
||||293|DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)|X|||
|Abschnitts-Kontrollsegment||||||||
||UNS||00014||Muss|||
||UNS|0081||D|Trennung von Kopf- und Positionsteil|X||
|Name und Adresse||||||||
|SG5||||Muss \[2001]|\[2001] Segmentgruppe ist nur einmal je UNH anzugeben|||
|SG5|NAD||00015||Muss|||
|SG5|NAD|3035||Z15|Überführungszeitreihe|X||
|Identifikationsangabe||||||||
|SG6||||Muss||||
|SG6|LOC||00017||Muss|||
|SG6|LOC|3227||172|Meldepunkt|X||


Version: 3.1f 30.09.2025 Seite 103 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|EDIFACT Struktur||Beschreibung<br/>Prüfidentifikator||Ausfallarbeits- überführungszeitreihe<br/>13020||Bedingung|
|-|-|-|-|-|-|-|
|SG6|LOC|3225|Bezeichnung|X \[951] \[511]|\[511] Hinweis: Verwendung der ID des MaBiS-ZP<br/>\[951] Format: Zählpunktbezeichnung||
|Beginn Messperiode Übertragungszeitraum|||||||
|SG6|||||||
|SG6|DTM||00018||Muss \[150]|\[150] Wenn BGM+Z69 (Redispatch tägliche Ausfallarbeitsüberführungszeitreihe) vorhanden.|
|SG6|DTM|2005|163|Verarbeitung, Beginndatum/-zeit|X||
|SG6|DTM|2380|Datum oder Uhrzeit oder Zeitspanne, Wert|X \[931]|\[931] Format: ZZZ = +00||
|SG6|DTM|2379|303|CCYYMMDDHHMMZZZ|X||
|Ende Messperiode Übertragungszeitraum|||||||
|SG6|||||||
|SG6|DTM||00019||Muss \[150]|\[150] Wenn BGM+Z69 (Redispatch tägliche Ausfallarbeitsüberführungszeitreihe) vorhanden.|
|SG6|DTM|2005|164|Verarbeitung, Endedatum/-zeit|X||
|SG6|DTM|2380|Datum oder Uhrzeit oder Zeitspanne, Wert|X \[931]|\[931] Format: ZZZ = +00||
|SG6|DTM|2379|303|CCYYMMDDHHMMZZZ|X||
|Bilanzierungsmonat|||||||
|SG6|||||||
|SG6|DTM||00020||Muss \[121]|\[121] wenn BGM+Z43 (Redispatch Ausfallarbeitüberführungszeitreihe) vorhanden|
|SG6|DTM|2005|492|Bilanzierungsdatum, -zeit, -periode|X||
|SG6|DTM|2380|Datum oder Uhrzeit oder Zeitspanne, Wert|X|||
|SG6|DTM|2379|610|CCYYMM|X||
|Versionsangabe|||||||
|SG6|||||||
|SG6|DTM||00021||Muss \[121]|\[121] wenn BGM+Z43 (Redispatch Ausfallarbeitüberführungszeitreihe) vorhanden|
|SG6|DTM|2005|293|Fertigstellungsdatum/-zeit|X||
|SG6|DTM|2380|Datum oder Uhrzeit oder Zeitspanne, Wert|X \[931]|\[931] Format: ZZZ = +00||
|SG6|DTM|2379|304|CCYYMMDDHHMMSSZZZ|X||
|lfd. Position|||||||
|SG9||||Muss|||
|SG9|LIN||00026||Muss||
|SG9|LIN|1082|Positionsnummer|X \[908]|\[908] Format: Mögliche Werte: 1 bis n||
|Produktidentifikation|||||||
|SG9|||||||
|SG9|PIA||00027||Muss||
|SG9|PIA|4347|5|Produktidentifikation|X||
|SG9|PIA|7140|Medium / OBIS-Kennzahl|X \[501]|\[501] Hinweis: Es sind nur die Werte erlaubt, die in der EDI\@Energy Codeliste der OBIS-Kennzahlen und Medien mit dem entsprechenden Prüfidentifikator versehen sind.||
|SG9|PIA|7143|Z08|Medium|X||
|Mengenangaben|||||||
|SG10||||Muss|||


Version: 3.1f
30.09.2025
Seite 104 von 158

MSCONS Anwendungshandbuch
![edi@energy Datenformate Strom & Gas](image)

|EDIFACT Struktur|Beschreibung|Ausfallarbeits-überführungszeitreihe|Bedingung||
|-|-|-|-|-|
||Prüfidentifikator|13020|||
|SG10 QTY|00028||Muss||
|SG10 QTY 6063|79|Energiemenge summiert (Summenwert, Bilanzsumme)|X||
|SG10 QTY 6060|Menge||X \[910] ∧ \[906]|\[906] Format: max. 3 Nachkommastellen<br/>\[910] Format: Möglicher Wert: < 0 oder ≥ 0|
|SG10 QTY 6411|KWH|Kilowattstunde|X||
|Beginn Messperiode|||||
|SG10|||||
|SG10 DTM|00029||Muss||
|SG10 DTM 2005|163|Verarbeitung, Beginndatum/-zeit|X||
|SG10 DTM 2380|Datum oder Uhrzeit oder Zeitspanne, Wert||X \[931] \[495]|\[495] Der Zeitpunkt muss ≤ dem Wert im DE2380 des DTM+137 sein<br/>\[931] Format: ZZZ = +00|
|SG10 DTM 2379|303|CCYYMMDDHHMMZZZ|X||
|Ende Messperiode|||||
|SG10|||||
|SG10 DTM|00030||Muss||
|SG10 DTM 2005|164|Verarbeitung, Endedatum/-zeit|X||
|SG10 DTM 2380|Datum oder Uhrzeit oder Zeitspanne, Wert||X \[931] \[495]|\[495] Der Zeitpunkt muss ≤ dem Wert im DE2380 des DTM+137 sein<br/>\[931] Format: ZZZ = +00|
|SG10 DTM 2379|303|CCYYMMDDHHMMZZZ|X||
|Nachrichten-Endesegment|||||
|UNT|00041||Muss||
|UNT 0074|Anzahl der Segmente in einer Nachricht||X||
|UNT 0062|Nachrichten-Referenznummer||X||
|Nutzdaten-Endesegment|||||
|UNZ|00042||Muss||
|UNZ 0036|Datenaustauschzähler||X||
|UNZ 0020|Datenaustauschreferenz||X||


Version: 3.1f	30.09.2025	Seite 105 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

## 8.5 Lastgang im Rahmen Redispatch 2.0

### 8.5.1 Übermittlung Einzelzeitreihe Ausfallarbeit

Tabellenspalte = Redispatch 2.0 Einzelzeitreihe Ausfallarbeit 13022

Dieser Anwendungsfall dient zur Übertragung der Ausfallarbeit und ggf. des Fahrplananteils zu einer Technischen Ressource oder einer Marktlokation.

Sollen Ausfallarbeit und Fahrplananteil zu einer Technischen Ressource übermittelt werden, so ist die Wiederholung über das LIN-Segment vorzunehmen.

Kommunikationspartner, Identifikationsangabe und Art der Werte für diesen Anwendungsfall:

|Sparte|Kommunikation von|Art der Werte|Identifikationsangabe in SG6 LOC|Anmerkung|
|-|-|-|-|-|
|Strom|NB an BTR|ermittelte Ausfallarbeit|ID der Technischen Ressource|--|
|Strom|NB an BTR|Gegenvorschlag Ausfallarbeit|ID der Technischen Ressource|--|
|Strom|BTR an NB|Gegenvorschlag Ausfallarbeit|ID der Technischen Ressource|--|
|Strom|BTR an NB|Ausfallarbeit und Fahrplananteil je TR|ID der Technischen Ressource|--|
|Strom|NB an NB|Übermittlung der abgestimmten Ausfallarbeit|ID der Technischen Ressource|--|
|Strom|NB an LF|Monatliche Ausfallarbeitszeitreihe je Marktlokation|ID der Marktlokation|--|
|Strom|NB an NB|Monatliche Ausfallarbeitszeitreihe je Marktlokation|ID der Marktlokation|--|
|Strom|NB an LF|Monatliche Ausfallarbeitszeitreihe je Tranche|ID der Tranche|--|
|Strom|NB an NB|Monatliche Ausfallarbeitszeitreihe je Tranche|ID der Tranche|--|


Version: 3.1f
30.09.2025
Seite 106 von 158

MSCONS Anwendungshandbuch
![edi@energy. Datenformate Strom & Gas](image)

### 8.5.2 Anwendungsübersicht Einzelzeitreihe Ausfallarbeit im Rahmen Redispatch 2.0

|EDIFACT Struktur|Beschreibung|Redispatch 2.0 Einzelzeitreihe Ausfallarbeit|Bedingung|||
|-|-|-|-|-|-|
||Prüfidentifikator|13022||||
|Nutzdaten-Kopfsegment||||||
|\*\*UNB\*\*|00002||Muss|||
|\*\*UNB\*\*|\*\*0001\*\*|\*\*UNOC\*\*|UN/ECE-Zeichensatz C|X||
|\*\*UNB\*\*|\*\*0002\*\*|\*\*3\*\*|Version 3|X||
|\*\*UNB\*\*|\*\*0004\*\*|MP-ID Absender|X|||
|\*\*UNB\*\*|\*\*0007\*\*|\*\*14\*\*|GS1|X||
|||\*\*500\*\*|DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)|X||
|\*\*UNB\*\*|\*\*0010\*\*|MP-ID Empfänger|X|||
|\*\*UNB\*\*|\*\*0007\*\*|\*\*14\*\*|GS1|X||
|||\*\*500\*\*|DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)|X||
|\*\*UNB\*\*|\*\*0017\*\*|Datum der Erstellung|X|||
|\*\*UNB\*\*|\*\*0019\*\*|Uhrzeit der Erstellung|X|||
|\*\*UNB\*\*|\*\*0020\*\*|Datenaustauschreferenz|X \[918]|\[918] Format: Zeichen aus dem über UNOC definierten Zeichensatz, wobei von den Buchstaben nur Großbuchstaben erlaubt sind.||
|\*\*UNB\*\*|\*\*0026\*\*|\*\*TL\*\*|Lastgang, beliebiger Zeitraum|X||
|Nachrichtenkopfsegment||||||
|\*\*UNH\*\*|00003||Muss|||
|\*\*UNH\*\*|\*\*0062\*\*|Nachrichten-Referenznummer|X|||
|\*\*UNH\*\*|\*\*0065\*\*|\*\*MSCON\*\*|Bericht über den Verbrauch messbarer Dienstleistungen|X||
|||\*\*S\*\*||||
|\*\*UNH\*\*|\*\*0052\*\*|\*\*D\*\*|Entwurfs-Version|X||
|\*\*UNH\*\*|\*\*0054\*\*|\*\*04B\*\*|Ausgabe 2004 - B|X||
|\*\*UNH\*\*|\*\*0051\*\*|\*\*UN\*\*|UN/CEFACT|X||
|\*\*UNH\*\*|\*\*0057\*\*|\*\*2.4c\*\*|Versionsnummer der zugrundeliegenden BDEW-Nachrichtenbeschreibung|X||
|Beginn der Nachricht||||||
|\*\*BGM\*\*|00004||Muss|||
|\*\*BGM\*\*|\*\*1001\*\*|\*\*Z45\*\*|Redispatch Einzelzeitreihe Ausfallarbeit|X||
|\*\*BGM\*\*|\*\*1004\*\*|Dokumentennummer|X|||
|\*\*BGM\*\*|\*\*1225\*\*|\*\*9\*\*|Original|X||
|Nachrichtendatum||||||
|\*\*DTM\*\*|00005||Muss|||
|\*\*DTM\*\*|\*\*2005\*\*|\*\*137\*\*|Dokumenten-/Nachrichtendatum/-zeit|X||
|\*\*DTM\*\*|\*\*2380\*\*|Datum oder Uhrzeit oder Zeitspanne, Wert|X \[931] \[494]|\[494] Das hier genannte Datum muss der Zeitpunkt sein, zu dem das Dokument erstellt wurde, oder ein Zeitpunkt, der davor liegt.<br/>\[931] Format: ZZZ = +00||
|\*\*DTM\*\*|\*\*2379\*\*|\*\*303\*\*|CCYYMMDDHHMMZZZ|X||
|Referenzangaben||||||


Version: 3.1f 30.09.2025 Seite 107 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|EDIFACT Struktur|Beschreibung|Redispatch 2.0 Einzelzeitreihe Ausfallarbeit|Bedingung||||
|-|-|-|-|-|-|-|
||Prüfidentifikator||13022||||
|SG1||Soll (\[1] ∧ \[538]) ∨ \[557]|\[1] Sofern per ORDERS angefordert<br/>\[538] Hinweis: Die Referenz auf die ORDERS ist nur dann anzugeben, wenn diese Werte vom Empfänger auch ursprünglich mittels ORDERS angefragt wurden.<br/>\[557] Hinweis: Die Referenz auf die ursprüngliche MSCONS ist anzugeben, wenn es sich um die Übermittlung eines Gegenvorschlags durch den BTR handelt.||||
|SG1|RFF|00006|Muss||||
|SG1|RFF|1153|AGI|Beantragungsnummer|X||
|SG1|RFF|1154|Referenznummer|X \[556] ∨ \[558]|\[556] Hinweis: Wert aus BGM+Z45 DE1004 der ORDERS mit der die Anforderung der Ausfallarbeit durch den anfNB erfolgt ist.<br/>\[558] Hinweis: Wert aus BGM+Z45 DE1004 der MSCONS auf die sich die Übermittlung des Gegenvorschlags durch den BTR bezieht.||
||Prüfidentifikator||||||
|SG1||Muss|||||
|SG1|RFF|00009|Muss||||
|SG1|RFF|1153|Z13|Prüfidentifikator|X||
|SG1|RFF|1154|13022|Redispatch Einzelzeitreihe Ausfallarbeit|X||
||MP-ID Absender||||||
|SG2||Muss|||||
|SG2|NAD|00010|Muss||||
|SG2|NAD|3035|MS|Dokumenten-/Nachrichtenaussteller bzw. -absender|X||
|SG2|NAD|3039|MP-ID|X \[117]|\[117] Nur MP-ID aus Sparte Strom||
|SG2|NAD|3055|9|GS1|X||
|SG2|NAD|3055|293|DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)|X||
||Ansprechpartner||||||
|SG4||Kann|||||
|SG4|CTA|00011|Muss||||
|SG4|CTA|3139|IC|Informationsstelle|X||
|SG4|CTA|3412|Abteilung oder Bearbeiter|X|||
||Kommunikationsverbindung||||||
|SG4||Muss|||||
|SG4|COM|00012|Muss||||
|SG4|COM|3148|Kommunikationsadresse, Identifikation|X ((\[939] \[142]) ∨ (\[940] \[143])) ∧ \[576]|\[142] wenn im DE3155 in demselben COM der Code EM vorhanden ist<br/>\[143] wenn im DE3155 in demselben COM der Code TE / FX / AJ / AL vorhanden ist<br/>\[576] Hinweis: Es darf nur eine Information im DE3148 übermittelt werden<br/>\[939] Format: Die Zeichenkette muss die Zeichen @ und . enthalten<br/>\[940] Format: Die Zeichenkette muss mit dem Zeichen + beginnen und danach dürfen nur noch Ziffern folgen||


Version: 3.1f 30.09.2025 Seite 108 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|EDIFACT Struktur|Beschreibung<br/>Prüfidentifikator|Redispatch 2.0 Einzelzeitreihe Ausfallarbeit<br/>13022|Bedingung||||
|-|-|-|-|-|-|-|
|SG4|COM|3155|TE|Telefon|X \[1P0..1]||
|SG4|COM|3155|EM|E-Mail|X \[1P0..1]||
|SG4|COM|3155|AJ|weiteres Telefon|X \[1P0..1]||
|SG4|COM|3155|AL|Handy|X \[1P0..1]||
|SG4|COM|3155|FX|Telefax|X \[1P0..1]||
|MP-ID Empfänger|||Muss||||
|SG2||||Muss|||
|SG2|NAD||00013||Muss||
|SG2|NAD|3035|MR|Nachrichtenempfänger|X||
|SG2|NAD|3039|MP-ID||X \[117]|\[117] Nur MP-ID aus Sparte Strom|
|SG2|NAD|3055|9|GS1|X||
|SG2|NAD|3055|293|DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)|X||
|Abschnitts-Kontrollsegment|||Muss||||
||UNS||00014||Muss||
||UNS|0081|D|Trennung von Kopf- und Positionsteil|X||
|Name und Adresse|||Muss \[2001]|\[2001] Segmentgruppe ist nur einmal je UNH anzugeben|||
|SG5||||Muss|||
|SG5|NAD||00015||Muss||
|SG5|NAD|3035|DP|Lieferanschrift|X||
|Identifikationsangabe|||Muss||||
|SG6||||Muss|||
|SG6|LOC||00017||Muss||
|SG6|LOC|3227|172|Meldepunkt|X||
|SG6|LOC|3225|Bezeichnung||X (\[950] (\[514] ∨ \[518]) ∧ \[32]) ∨ (\[922] \[554])|\[32] wenn MP-ID in SG2 NAD+MS in der Rolle NB<br/>\[514] Hinweis: Verwendung der ID der Marktlokation<br/>\[518] Hinweis: Verwendung der ID der Tranche<br/>\[554] Hinweis: Verwendung der ID der Technischen Ressource<br/>\[922] Format: TR-ID<br/>\[950] Format: Marktlokations-ID|
|Beginn Messperiode Übertragungszeitraum|||||||
|SG6||||Muss|||
|SG6|DTM||00018||Muss||
|SG6|DTM|2005|163|Verarbeitung, Beginndatum/-zeit|X||
|SG6|DTM|2380|Datum oder Uhrzeit oder Zeitspanne, Wert|X \[931]|\[931] Format: ZZZ = +00||
|SG6|DTM|2379|303|CCYYMMDDHHMMZZZ|X||
|Ende Messperiode Übertragungszeitraum|||||||
|SG6||||Muss|||
|SG6|DTM||00019||Muss||
|SG6|DTM|2005|164|Verarbeitung, Endedatum/-zeit|X||
|SG6|DTM|2380|Datum oder Uhrzeit oder Zeitspanne, Wert|X \[931]|\[931] Format: ZZZ = +00||
|SG6|DTM|2379|303|CCYYMMDDHHMMZZZ|X||
|Versionsangabe|||||||
|SG6||||Muss|||
|SG6|DTM||00021||Muss||
|SG6|DTM|2005|293|Fertigstellungsdatum/-zeit|X||


Version: 3.1f 30.09.2025 Seite 109 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|EDIFACT Struktur||Beschreibung<br/>Prüfidentifikator||Redispatch 2.0 Einzelzeitreihe Ausfallarbeit<br/>13022||Bedingung|
|-|-|-|-|-|-|-|
|SG6|DTM|2380|Datum oder Uhrzeit oder Zeitspanne, Wert|X \[931]|\[931] Format: ZZZ = +00||
|SG6|DTM|2379|304 CCYYMMDDHHMMSSZZZ|X|||
|lfd. Position|||||||
|SG9|||Muss||||
|SG9|LIN||00026||Muss||
|SG9|LIN|1082|Positionsnummer|X \[908]|\[908] Format: Mögliche Werte: 1 bis n||
|Produktidentifikation|||||||
|SG9|||Muss||||
|SG9|PIA||00027||Muss||
|SG9|PIA|4347|5 Produktidentifikation|X|||
|SG9|PIA|7140|Medium / OBIS-Kennzahl|X \[501]|\[501] Hinweis: Es sind nur die Werte erlaubt, die in der EDI\@Energy Codeliste der OBIS-Kennzahlen und Medien mit dem entsprechenden Prüfidentifikator versehen sind.||
|SG9|PIA|7143|Z08 Medium|X|||
|Mengenangaben|||||||
|SG10|||Muss||||
|SG10|QTY||00028||Muss||
|SG10|QTY|6063|220 Wahrer Wert|X|||
|SG10|QTY|6060|Menge|X \[910] ∧ \[906]|\[906] Format: max. 3 Nachkommastellen<br/>\[910] Format: Möglicher Wert: < 0 oder ≥ 0||
|SG10|QTY|6411|KWH Kilowattstunde|X \[100]|\[100] Wenn in derselben SG9 LIN das PIA+5+AUA:Z08 vorhanden||
|SG10|QTY|6411|KWT Kilowatt|X \[101]|\[101] Wenn in derselben SG9 LIN das PIA+5+FPA:Z08 vorhanden||
|Beginn Messperiode|||||||
|SG10|||Muss||||
|SG10|DTM||00029||Muss||
|SG10|DTM|2005|163 Verarbeitung, Beginndatum/-zeit|X|||
|SG10|DTM|2380|Datum oder Uhrzeit oder Zeitspanne, Wert|X \[931] \[495]|\[495] Der Zeitpunkt muss ≤ dem Wert im DE2380 des DTM+137 sein<br/>\[931] Format: ZZZ = +00||
|SG10|DTM|2379|303 CCYYMMDDHHMMZZZ|X|||
|Ende Messperiode|||||||
|SG10|||Muss||||
|SG10|DTM||00030||Muss||
|SG10|DTM|2005|164 Verarbeitung, Endedatum/-zeit|X|||
|SG10|DTM|2380|Datum oder Uhrzeit oder Zeitspanne, Wert|X \[931] \[495]|\[495] Der Zeitpunkt muss ≤ dem Wert im DE2380 des DTM+137 sein<br/>\[931] Format: ZZZ = +00||
|SG10|DTM|2379|303 CCYYMMDDHHMMZZZ|X|||
|Nachrichten-Endesegment|||||||
|UNT||00041||Muss|||
|UNT|0074|Anzahl der Segmente in einer Nachricht|X||||
|UNT|0062|Nachrichten-Referenznummer|X||||
|Nutzdaten-Endesegment|||||||
|UNZ||00042||Muss|||
|UNZ|0036|Datenaustauschzähler|X||||
|UNZ|0020|Datenaustauschreferenz|X||||


Version: 3.1f 30.09.2025 Seite 110 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

## 8.6 Meteorologische Daten im Rahmen MaBiS / Redispatch 2.0

### 8.6.1 Übermittlung meteorologischer Daten

Tabellenspalte = Übermittlung von meteorologischen Daten 13021

Dieser Anwendungsfall dient zur Übertragung der von meteorologischen Daten für eine Technische Ressource.

Kommunikationspartner, Identifikationsangabe und Art der Werte für diesen Anwendungsfall:

|Sparte|Kommunikation von|Art der Werte|Identifikationsangabe in SG6 LOC|Anmerkung|
|-|-|-|-|-|
|Strom|BTR an NB|Meteorologische Daten|ID der Technischen Ressource|--|
|Strom|NB an NB|Weiterleitung meteorologischer Daten|ID der Technischen Ressource|--|


Version: 3.1f
30.09.2025
Seite 111 von 158

MSCONS Anwendungshandbuch
![edi@energy. Datenformate Strom & Gas](image)

## 8.6.2 Anwendungsübersicht meteorolog. Daten im Rahmen MaBiS / Redispatch 2.0

|EDIFACT Struktur|Beschreibung|Übermittlung von meteorologischen Daten|Bedingung||||
|-|-|-|-|-|-|-|
||Prüfidentifikator|13021|||||
|Nutzdaten-Kopfsegment|||||||
|UNB|00002||Muss||||
|UNB|0001|\*\*UNOC\*\*|UN/ECE-Zeichensatz C|X|||
|UNB|0002|\*\*3\*\*|Version 3|X|||
|UNB|0004|MP-ID Absender||X|||
|UNB|0007|\*\*14\*\*|GS1|X|||
||\*\*500\*\*|DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)|X||||
|UNB|0010|MP-ID Empfänger||X|||
|UNB|0007|\*\*14\*\*|GS1|X|||
||\*\*500\*\*|DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)|X||||
|UNB|0017|Datum der Erstellung||X|||
|UNB|0019|Uhrzeit der Erstellung||X|||
|UNB|0020|Datenaustauschreferenz||X \[918]|\[918] Format: Zeichen aus dem über UNOC definierten Zeichensatz, wobei von den Buchstaben nur Großbuchstaben erlaubt sind.||
|UNB|0026|\*\*TL\*\*|Lastgang, beliebiger Zeitraum|X|||
|Nachrichtenkopfsegment|||||||
|UNH|00003||Muss||||
|UNH|0062|Nachrichten-Referenznummer||X|||
|UNH|0065|\*\*MSCON\*\*|Bericht über den Verbrauch|X|||
||\*\*S\*\*|messbarer Dienstleistungen|||||
|UNH|0052|\*\*D\*\*|Entwurfs-Version|X|||
|UNH|0054|\*\*04B\*\*|Ausgabe 2004 - B|X|||
|UNH|0051|\*\*UN\*\*|UN/CEFACT|X|||
|UNH|0057|\*\*2.4c\*\*|Versionsnummer der zugrundeliegenden BDEW-Nachrichtenbeschreibung|X|||
|Beginn der Nachricht|||||||
|BGM|00004||Muss||||
|BGM|1001|\*\*Z44\*\*|Redispatch Übermittlung von meteorologischen Daten|X|||
|BGM|1004|Dokumentennummer||X|||
|BGM|1225|\*\*9\*\*|Original|X|||
|Nachrichtendatum|||||||
|DTM|00005||Muss||||
|DTM|2005|\*\*137\*\*|Dokumenten-/Nachrichtendatum/-zeit|X|||
|DTM|2380|Datum oder Uhrzeit oder Zeitspanne, Wert||X \[931] \[494]|\[494] Das hier genannte Datum muss der Zeitpunkt sein, zu dem das Dokument erstellt wurde, oder ein Zeitpunkt, der davor liegt.<br/>\[931] Format: ZZZ = +00||
|DTM|2379|\*\*303\*\*|CCYYMMDDHHMMZZZ|X|||
|Prüfidentifikator|||||||
|SG1|||Muss||||
|SG1|RFF|00009||Muss|||
|SG1|RFF|1153|\*\*Z13\*\*|Prüfidentifikator|X||
|SG1|RFF|1154|\*\*13021\*\*|Redispatch Übermittlung von meteorologischen Daten|X||
|MP-ID Absender|||||||
|SG2|||Muss||||


Version: 3.1f 30.09.2025 Seite 112 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|EDIFACT Struktur|Beschreibung<br/>Prüfidentifikator|Übermittlung von meteorologischen Daten<br/>13021|Bedingung|||||
|-|-|-|-|-|-|-|-|
|SG2|NAD||00010||Muss|||
|SG2|NAD|3035||MS|Dokumenten- /Nachrichtenaussteller bzw. -absender|X||
|SG2|NAD|3039||MP-ID||X \[117]|\[117] Nur MP-ID aus Sparte Strom|
|SG2|NAD|3055||9|GS1|X||
||||293|DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)|X|||
|Ansprechpartner||||||||
|SG4||||Kann||||
|SG4|CTA||00011||Muss|||
|SG4|CTA|3139||IC|Informationsstelle|X||
|SG4|CTA|3412||Abteilung oder Bearbeiter|X|||
|Kommunikationsverbindung||||||||
|SG4||||||||
|SG4|COM||00012||Muss|||
|SG4|COM|3148||Kommunikationsadresse, Identifikation|X ((\[939] \[142]) ∨ (\[940] \[143])) ∧ \[576]|\[142] wenn im DE3155 in demselben COM der Code EM vorhanden ist<br/>\[143] wenn im DE3155 in demselben COM der Code TE / FX / AJ / AL vorhanden ist<br/>\[576] Hinweis: Es darf nur eine Information im DE3148 übermittelt werden<br/>\[939] Format: Die Zeichenkette muss die Zeichen @ und . enthalten<br/>\[940] Format: Die Zeichenkette muss mit dem Zeichen + beginnen und danach dürfen nur noch Ziffern folgen||
|SG4|COM|3155||TE|Telefon|X \[1P0..1]||
||||EM|E-Mail|X \[1P0..1]|||
||||AJ|weiteres Telefon|X \[1P0..1]|||
||||AL|Handy|X \[1P0..1]|||
||||FX|Telefax|X \[1P0..1]|||
|MP-ID Empfänger||||||||
|SG2||||Muss||||
|SG2|NAD||00013||Muss|||
|SG2|NAD|3035||MR|Nachrichtenempfänger|X||
|SG2|NAD|3039||MP-ID||X \[117]|\[117] Nur MP-ID aus Sparte Strom|
|SG2|NAD|3055||9|GS1|X||
||||293|DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)|X|||
|Abschnitts-Kontrollsegment||||||||
||UNS||00014||Muss|||
||UNS|0081||D|Trennung von Kopf- und Positionsteil|X||
|Name und Adresse||||||||
|SG5||||Muss \[2001]|\[2001] Segmentgruppe ist nur einmal je UNH anzugeben|||
|SG5|NAD||00015||Muss|||
|SG5|NAD|3035||DP|Lieferanschrift|X||
|Identifikationsangabe||||||||
|SG6||||Muss||||
|SG6|LOC||00017||Muss|||
|SG6|LOC|3227||172|Meldepunkt|X||
|SG6|LOC|3225||Bezeichnung||X \[922] \[554]|\[554] Hinweis: Verwendung der ID der Technischen Ressource<br/>\[922] Format: TR-ID|
|Beginn Messperiode<br/>Übertragungszeitraum||||||||


Version: 3.1f 30.09.2025 Seite 113 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|EDIFACT Struktur|Beschreibung<br/>Prüfidentifikator|Übermittlung von meteorologischen Daten<br/>13021|Bedingung||||
|-|-|-|-|-|-|-|
|\*\*SG6\*\*|||\*\*Muss\*\*||||
|SG6|DTM||00018||Muss||
|SG6|DTM|2005|\*\*163\*\*|Verarbeitung, Beginndatum/-zeit|X||
|SG6|DTM|2380|Datum oder Uhrzeit oder Zeitspanne, Wert|X \[931]|\[931] Format: ZZZ = +00||
|SG6|DTM|2379|\*\*303\*\*|CCYYMMDDHHMMZZZ|X||
|\*\*Ende Messperiode Übertragungszeitraum\*\*|||||||
|\*\*SG6\*\*|||\*\*Muss\*\*||||
|SG6|DTM||00019||Muss||
|SG6|DTM|2005|\*\*164\*\*|Verarbeitung, Endedatum/-zeit|X||
|SG6|DTM|2380|Datum oder Uhrzeit oder Zeitspanne, Wert|X \[931]|\[931] Format: ZZZ = +00||
|SG6|DTM|2379|\*\*303\*\*|CCYYMMDDHHMMZZZ|X||
|\*\*Versionsangabe\*\*|||||||
|\*\*SG6\*\*|||\*\*Muss\*\*||||
|SG6|DTM||00021||Muss||
|SG6|DTM|2005|\*\*293\*\*|Fertigstellungsdatum/-zeit|X||
|SG6|DTM|2380|Datum oder Uhrzeit oder Zeitspanne, Wert|X \[931]|\[931] Format: ZZZ = +00||
|SG6|DTM|2379|\*\*304\*\*|CCYYMMDDHHMMSSZZZ|X||
|\*\*lfd. Position\*\*|||||||
|\*\*SG9\*\*|||\*\*Muss\*\*||||
|SG9|LIN||00026||Muss||
|SG9|LIN|1082|Positionsnummer|X \[908]|\[908] Format: Mögliche Werte: 1 bis n||
|\*\*Produktidentifikation\*\*|||||||
|\*\*SG9\*\*|||\*\*Muss\*\*||||
|SG9|PIA||00027||Muss||
|SG9|PIA|4347|\*\*5\*\*|Produktidentifikation|X||
|SG9|PIA|7140|Medium / OBIS-Kennzahl|X \[501]|\[501] Hinweis: Es sind nur die Werte erlaubt, die in der EDI\@Energy Codeliste der OBIS-Kennzahlen und Medien mit dem entsprechenden Prüfidentifikator versehen sind.||
|SG9|PIA|7143|\*\*Z08\*\*|Medium|X||
|\*\*Mengenangaben\*\*|||||||
|\*\*SG10\*\*|||\*\*Muss\*\*||||
|SG10|QTY||00028||Muss||
|SG10|QTY|6063|\*\*220\*\*|Wahrer Wert|X||
|SG10|QTY|6060|Menge|X \[902] ∧ \[906]|\[902] Format: Möglicher Wert: ≥ 0<br/>\[906] Format: max. 3 Nachkommastellen||
|SG10|QTY|6411|\*\*D54\*\*|Watt pro Quadratmeter|X \[98]|\[98] Wenn SG9 PIA+5+SOL:Z08 vorhanden|
|||\*\*MTS\*\*|Meter pro Sekunde|X \[99]|\[99] Wenn SG9 PIA+5+WID:Z08 vorhanden||
|\*\*Beginn Messperiode\*\*|||||||
|\*\*SG10\*\*|||\*\*Muss\*\*||||
|SG10|DTM||00029||Muss||
|SG10|DTM|2005|\*\*163\*\*|Verarbeitung, Beginndatum/-zeit|X||
|SG10|DTM|2380|Datum oder Uhrzeit oder Zeitspanne, Wert|X \[931] \[495]|\[495] Der Zeitpunkt muss ≤ dem Wert im DE2380 des DTM+137 sein<br/>\[931] Format: ZZZ = +00||
|SG10|DTM|2379|\*\*303\*\*|CCYYMMDDHHMMZZZ|X||
|\*\*Ende Messperiode\*\*|||||||
|\*\*SG10\*\*|||\*\*Muss\*\*||||
|SG10|DTM||00030||Muss||


Version: 3.1f 30.09.2025 Seite 114 von 158

MSCONS Anwendungshandbuch
![edi@energy Datenformate Strom & Gas](image)

|EDIFACT Struktur|Beschreibung<br/>Prüfidentifikator|Übermittlung von meteorologischen Daten<br/>13021|Bedingung|
|-|-|-|-|
|SG10 DTM \*\*2005\*\*|\*\*164\*\* Verarbeitung, Endedatum/-zeit|X||
|SG10 DTM \*\*2380\*\*|Datum oder Uhrzeit oder Zeitspanne, Wert|X \[931] \[495]|\[495] Der Zeitpunkt muss ≤ dem Wert im DE2380 des DTM+137 sein<br/>\[931] Format: ZZZ = +00|
|SG10 DTM \*\*2379\*\*|\*\*303\*\* CCYYMMDDHHMMZZZ|X||
|Nachrichten-Endesegment||Muss||
|\*\*UNT\*\* 00041||Muss||
|\*\*UNT 0074\*\*|Anzahl der Segmente in einer Nachricht|X||
|\*\*UNT 0062\*\*|Nachrichten-Referenznummer|X||
|Nutzdaten-Endesegment||Muss||
|\*\*UNZ\*\* 00042||Muss||
|\*\*UNZ 0036\*\*|Datenaustauschzähler|X||
|\*\*UNZ 0020\*\*|Datenaustauschreferenz|X||


Version: 3.1f 30.09.2025 Seite 115 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

# 9 Gasbeschaffenheit

## 9.1 Übertragung Gasbeschaffenheitsdaten

Tabellenspalte = Gasbeschaffenheit 13007

Entsprechend der eichrechtlichen Vorgaben und gem. DVGW-Regelwerk (insbes. G693 und G685) ermittelte Gasbeschaffenheitsdaten werden monatlich als Stunden-, Tages- oder Monatsmittelwerte unter Verwendung der OBIS-Kennzahlen zur Gasbeschaffenheit (Profilwerte, Mittelwerte) übermittelt. Die Anzahl der Nachkommastellen entspricht der für die jeweilige Messgröße vorgegebenen Stellenzahl.

Kommunikationspartner, Identifikationsangabe und Art der Werte für diesen Anwendungsfall:

|Sparte|Kommunikation von|Art der Werte|Identifikationsangabe in SG6 LOC|Anmerkung|
|-|-|-|-|-|
|Gas|NB an NB|Gasbeschaffenheitsdaten|ID der Messlokation|---|
|Gas|NB an LF|Gasbeschaffenheitsdaten|ID der Marktlokation|---|
|Gas|MSB an NB|Gasbeschaffenheitsdaten|ID der Messlokation|---|


Version: 3.1f	30.09.2025	Seite 116 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

## 9.2 Anwendungsübersicht Gasbeschaffenheitsdaten

|EDIFACT Struktur|Beschreibung|Gasbeschaffenheit|Bedingung||||
|-|-|-|-|-|-|-|
||Prüfidentifikator|13007|||||
|Nutzdaten-Kopfsegment|||||||
|UNB|00002||Muss||||
|UNB|0001|UNOC|UN/ECE-Zeichensatz C|X|||
|UNB|0002|3|Version 3|X|||
|UNB|0004||MP-ID Absender|X|||
|UNB|0007|14|GS1|X|||
||502|DE, DVGW Service & Consult GmbH|X||||
|UNB|0010||MP-ID Empfänger|X|||
|UNB|0007|14|GS1|X|||
||502|DE, DVGW Service & Consult GmbH|X||||
|UNB|0017||Datum der Erstellung|X|||
|UNB|0019||Uhrzeit der Erstellung|X|||
|UNB|0020||Datenaustauschreferenz|X \[918]|\[918] Format: Zeichen aus dem über UNOC definierten Zeichensatz, wobei von den Buchstaben nur Großbuchstaben erlaubt sind.||
|UNB|0026|TL|Lastgang, beliebiger Zeitraum|X|||
|Nachrichtenkopfsegment|||||||
|UNH|00003||Muss||||
|UNH|0062||Nachrichten-Referenznummer|X|||
|UNH|0065|MSCON|Bericht über den Verbrauch messbarer Dienstleistungen|X|||
||S||||||
|UNH|0052|D|Entwurfs-Version|X|||
|UNH|0054|04B|Ausgabe 2004 - B|X|||
|UNH|0051|UN|UN/CEFACT|X|||
|UNH|0057|2.4c|Versionsnummer der zugrundeliegenden BDEW-Nachrichtenbeschreibung|X|||
|Beginn der Nachricht|||||||
|BGM|00004||Muss||||
|BGM|1001|Z21|Gasbeschaffenheitsdaten|X|||
|BGM|1004||Dokumentennummer|X|||
|BGM|1225|9|Original|X|||
|Nachrichtendatum|||||||
|DTM|00005||Muss||||
|DTM|2005|137|Dokumenten-/Nachrichtendatum/-zeit|X|||
|DTM|2380||Datum oder Uhrzeit oder Zeitspanne, Wert|X \[931] \[494]|\[494] Das hier genannte Datum muss der Zeitpunkt sein, zu dem das Dokument erstellt wurde, oder ein Zeitpunkt, der davor liegt.<br/>\[931] Format: ZZZ = +00||
|DTM|2379|303|CCYYMMDDHHMMZZZ|X|||
|Prüfidentifikator|||||||
|SG1|||Muss||||
|SG1|RFF|00009||Muss|||
|SG1|RFF|1153|Z13|Prüfidentifikator|X||
|SG1|RFF|1154|13007|Gasbeschaffenheitsdaten|X||
|MP-ID Absender|||||||
|SG2|||Muss||||
|SG2|NAD|00010||Muss|||
|SG2|NAD|3035|MS|Dokumenten-/Nachrichtenaussteller bzw. -absender|X||
|SG2|NAD|3039||MP-ID|X \[118]|\[118] Nur MP-ID aus Sparte Gas|


Version: 3.1f
30.09.2025
Seite 117 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|EDIFACT Struktur|Beschreibung<br/>Prüfidentifikator|Gasbeschaffenheit<br/>13007|Bedingung||||
|-|-|-|-|-|-|-|
|SG2|NAD|3055|9|GS1|X||
|||332|DE, DVGW Service & Consult GmbH|X|||
|Ansprechpartner|||||||
|SG4|||Kann||||
|SG4|CTA||00011||Muss||
|SG4|CTA|3139|IC|Informationsstelle|X||
|SG4|CTA|3412|Abteilung oder Bearbeiter|X|||
|Kommunikationsverbindung|||||||
|SG4|||||||
|SG4|COM||00012||Muss||
|SG4|COM|3148|Kommunikationsadresse, Identifikation|X ((\[939] \[142]) ∨ (\[940] \[143])) ∧ \[576]|\[142] wenn im DE3155 in demselben COM der Code EM vorhanden ist<br/>\[143] wenn im DE3155 in demselben COM der Code TE / FX / AJ / AL vorhanden ist<br/>\[576] Hinweis: Es darf nur eine Information im DE3148 übermittelt werden<br/>\[939] Format: Die Zeichenkette muss die Zeichen @ und . enthalten<br/>\[940] Format: Die Zeichenkette muss mit dem Zeichen + beginnen und danach dürfen nur noch Ziffern folgen||
|SG4|COM|3155|TE|Telefon|X \[1P0..1]||
|||EM|E-Mail|X \[1P0..1]|||
|||AJ|weiteres Telefon|X \[1P0..1]|||
|||AL|Handy|X \[1P0..1]|||
|||FX|Telefax|X \[1P0..1]|||
|MP-ID Empfänger|||||||
|SG2|||Muss||||
|SG2|NAD||00013||Muss||
|SG2|NAD|3035|MR|Nachrichtenempfänger|X||
|SG2|NAD|3039|MP-ID||X \[118]|\[118] Nur MP-ID aus Sparte Gas|
|SG2|NAD|3055|9|GS1|X||
|||332|DE, DVGW Service & Consult GmbH|X|||
|Abschnitts-Kontrollsegment|||||||
||UNS||00014||Muss||
||UNS|0081|D|Trennung von Kopf- und Positionsteil|X||
|Name und Adresse|||||||
|SG5|||Muss \[2001]|\[2001] Segmentgruppe ist nur einmal je UNH anzugeben|||
|SG5|NAD||00015||Muss||
|SG5|NAD|3035|DP|Lieferanschrift|X||
|Identifikationsangabe|||||||
|SG6|||Muss||||
|SG6|LOC||00017||Muss||
|SG6|LOC|3227|172|Meldepunkt|X||
|SG6|LOC|3225|Bezeichnung||X (\[951] ((\[32] ∧ \[36]) ∨ (\[35] ∧ \[36])) ∧ \[510]) ∨ (\[950] (\[32] ∧ \[33]) ∧ \[514])|\[32] wenn MP-ID in SG2 NAD+MS in der Rolle NB<br/>\[33] wenn MP-ID in SG2 NAD+MR in der Rolle LF<br/>\[35] wenn MP-ID in SG2 NAD+MS in der Rolle MSB<br/>\[36] wenn MP-ID in SG2 NAD+MR in der Rolle NB<br/>\[510] Hinweis: Verwendung der ID der Messlokation<br/>\[514] Hinweis: Verwendung der ID der Marktlokation<br/>\[950] Format: Marktlokations-ID<br/>\[951] Format: Zählpunktbezeichnung|


Version: 3.1f
30.09.2025
Seite 118 von 158

MSCONS Anwendungshandbuch
![edi@energy Datenformate Strom & Gas](image)

|EDIFACT Struktur|BeschreibungPrüfidentifikator|Gasbeschaffenheit13007|Bedingung||||
|-|-|-|-|-|-|-|
|Beginn Messperiode Übertragungszeitraum|||||||
|SG6|||Muss||||
|SG6|DTM||00018||Muss||
|SG6|DTM|2005|163|Verarbeitung, Beginndatum/-zeit|X||
|SG6|DTM|2380|Datum oder Uhrzeit oder Zeitspanne, Wert|X \[931]|\[931] Format: ZZZ = +00||
|SG6|DTM|2379|303|CCYYMMDDHHMMZZZ|X||
|Ende Messperiode Übertragungszeitraum|||||||
|SG6|||Muss||||
|SG6|DTM||00019||Muss||
|SG6|DTM|2005|164|Verarbeitung, Endedatum/-zeit|X||
|SG6|DTM|2380|Datum oder Uhrzeit oder Zeitspanne, Wert|X \[931]|\[931] Format: ZZZ = +00||
|SG6|DTM|2379|303|CCYYMMDDHHMMZZZ|X||
|Versionsangabe|||||||
|SG6|||Muss||||
|SG6|DTM||00021||Muss||
|SG6|DTM|2005|293|Fertigstellungsdatum/-zeit|X||
|SG6|DTM|2380|Datum oder Uhrzeit oder Zeitspanne, Wert|X \[931]|\[931] Format: ZZZ = +00||
|SG6|DTM|2379|304|CCYYMMDDHHMMSSZZZ|X||
|lfd. Position|||||||
|SG9|||Muss||||
|SG9|LIN||00026||Muss||
|SG9|LIN|1082|Positionsnummer|X \[908]|\[908] Format: Mögliche Werte: 1 bis n||
|Produktidentifikation|||||||
|SG9|||Muss||||
|SG9|PIA||00027||Muss||
|SG9|PIA|4347|5|Produktidentifikation|X||
|SG9|PIA|7140|Medium / OBIS-Kennzahl|X \[501]|\[501] Hinweis: Es sind nur die Werte erlaubt, die in der EDI\@Energy Codeliste der OBIS-Kennzahlen und Medien mit dem entsprechenden Prüfidentifikator versehen sind.||
|SG9|PIA|7143|SRW|OBIS-Kennzahl|X||
|Mengenangaben|||||||
|SG10|||Muss||||
|SG10|QTY||00028||Muss||
|SG10|QTY|6063|220|Wahrer Wert|X|\[32] wenn MP-ID in SG2 NAD+MS in der Rolle NB<br/>\[33] wenn MP-ID in SG2 NAD+MR in der Rolle LF<br/>\[35] wenn MP-ID in SG2 NAD+MS in der Rolle MSB<br/>\[36] wenn MP-ID in SG2 NAD+MR in der Rolle NB|
|||67|Ersatzwert|X (\[32] ∧ (\[33] ∨ \[36]))|||
|||201|Vorschlagswert|X (\[32] ∧ (\[33] ∨ \[36])) ⊻ (\[35] ∧ \[36])|||
|||20|Nicht verwendbarer Wert|X (\[32] ∧ \[33]) ⊻ (\[35] ∧ \[36])|||


Version: 3.1f
30.09.2025
Seite 119 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|EDIFACT Struktur|Beschreibung|Gasbeschaffenheit|Bedingung|
|-|-|-|-|
||Prüfidentifikator|13007||
|SG10 QTY 6060|Menge|X (\[902] ∧ \[907]) ∨ ((\[910] ∧ \[907]) (\[49] ∨ \[50]))|\[49] Wenn SG9 PIA+5+7-b?:70.16.16/7-b?:70.16.20/7-b?:70.16.22 (b=Kanal: Wert gemäß Codeliste der OBIS-Kennzahlen und Medien) vorhanden<br/>\[50] Wenn SG9 PIA+5+7-b?:70.18.16/7-b?:70.18.20/7-b?:70.18.22 (b=Kanal: Wert gemäß Codeliste der OBIS-Kennzahlen und Medien) vorhanden<br/>\[902] Format: Möglicher Wert: ≥ 0<br/>\[907] Format: max. 4 Nachkommastellen<br/>\[910] Format: Möglicher Wert: < 0 oder ≥ 0|
|Beginn Messperiode||||
|SG10||||
|SG10 DTM 00029||Muss||
|SG10 DTM 2005|163 Verarbeitung, Beginndatum/-zeit|X||
|SG10 DTM 2380|Datum oder Uhrzeit oder Zeitspanne, Wert|X \[931] \[495]|\[495] Der Zeitpunkt muss ≤ dem Wert im DE2380 des DTM+137 sein<br/>\[931] Format: ZZZ = +00|
|SG10 DTM 2379|303 CCYYMMDDHHMMZZZ|X||
|Ende Messperiode||||
|SG10||||
|SG10 DTM 00030||Muss||
|SG10 DTM 2005|164 Verarbeitung, Endedatum/-zeit|X||
|SG10 DTM 2380|Datum oder Uhrzeit oder Zeitspanne, Wert|X \[931] \[495]|\[495] Der Zeitpunkt muss ≤ dem Wert im DE2380 des DTM+137 sein<br/>\[931] Format: ZZZ = +00|
|SG10 DTM 2379|303 CCYYMMDDHHMMZZZ|X||
|Ersatzwertbildungsverfahren||||
|SG10||||
|SG10 STS 00036||Muss \[92] ⊻ \[94]|\[92] Wenn SG10 QTY DE6063 mit Wert 67 vorhanden<br/>\[94] Wenn SG10 QTY DE6063 mit Wert 201 vorhanden|
|SG10 STS 9015|Z32 Ersatzwertbildungsverfahren|X||
|SG10 STS 9013|Z89 Vergleichsmessung (nicht geeicht)|X \[4P0..1] ⊻ \[6P0..1]||
||Z90 Messwertnachbildung aus geeichten Werten|X \[4P0..1] ⊻ \[6P0..1]||
||Z91 Messwertnachbildung aus nicht geeichten Werten|X \[4P0..1] ⊻ \[6P0..1]||
||Z92 Interpolation|X \[4P0..1] ⊻ \[6P0..1]||
||Z93 Haltewert|X \[4P0..1] ⊻ \[6P0..1]||
||Z94 Bilanzierung Netzabschnitt|X \[4P0..1] ⊻ \[6P0..1]||
||Z95 Historische Messwerte|X \[4P0..1] ⊻ \[6P0..1]||
||ZQ8 Aufteilung|X \[4P0..1] ⊻ \[6P0..1]||
||ZQ9 Verwendung von Werten des Störmengenzählwerks|X \[4P0..1] ⊻ \[6P0..1]||
||ZR0 Umgangs- und Korrekturmengen|X \[4P0..1] ⊻ \[6P0..1]||
|Korrekturgrund||||
|SG10||||


Version: 3.1f 30.09.2025 Seite 120 von 158

MSCONS Anwendungshandbuch
![edi@energy. Datenformate Strom & Gas](image)

|EDIFACT Struktur||Beschreibung<br/>Prüfidentifikator|Gasbeschaffenheit<br/>13007|Bedingung|
|-|-|-|-|-|
|SG10 STS|00037||Soll \[127] ∧ \[560]|\[127] wenn ein Korrekturgrund<br/>anzugeben ist \[560] Hinweis: Ein<br/>Korrekturgrund ist anzugeben, wenn:<br/>1. ein bereits an den MP übermittelter<br/>vorläufiger Wert durch einen<br/>Ersatzwert ersetzt wird, oder<br/>2. ein bereits an den MP übermittelter<br/>Ersatzwert durch einen Ersatzwert<br/>ersetzt wird, oder<br/>3. ein bereits an den MP übermittelter<br/>wahrer Wert durch einen Ersatzwert<br/>ersetzt wird, oder<br/>4. ein bereits an den MP übermittelter<br/>wahrer Wert durch einen wahren Wert<br/>ersetzt wird.|
|SG10 STS|\*\*9015\*\*|\*\*Z34\*\*|Korrekturgrund|X|


Version: 3.1f	30.09.2025	Seite 121 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|EDIFACT Struktur|Beschreibung|Gasbeschaffenheit|Bedingung||
|-|-|-|-|-|
||Prüfidentifikator|13007|||
|SG10 STS 9013|Z74|kein Zugang|X \[4P0..1] ⊻ \[6P0..1] ⊻ \[7P0..1] ⊻ \[8P0..1]||
||Z75|Kommunikationsstörung|X \[4P0..1] ⊻ \[6P0..1] ⊻ \[7P0..1] ⊻ \[8P0..1]||
||Z76|Netzausfall|X \[4P0..1] ⊻ \[6P0..1] ⊻ \[7P0..1] ⊻ \[8P0..1]||
||Z78|Gerätewechsel|X \[4P0..1] ⊻ \[6P0..1] ⊻ \[7P0..1] ⊻ \[8P0..1]||
||Z80|Gerät arbeitet außerhalb<br/>der Betriebsbedingungen|X \[4P0..1] ⊻ \[6P0..1] ⊻ \[7P0..1] ⊻ \[8P0..1]||
||Z81|Messeinrichtung<br/>gestört/defekt|X \[4P0..1] ⊻ \[6P0..1] ⊻ \[7P0..1] ⊻ \[8P0..1]||
||Z82|Unsicherheit Messung|X \[4P0..1] ⊻ \[6P0..1] ⊻ \[7P0..1] ⊻ \[8P0..1]||
||Z98|Berücksichtigung<br/>Störmengenzählwerk|X \[4P0..1] ⊻ \[6P0..1]||
||Z99|Mengenumwertung<br/>unvollständig|X \[6P0..1] ⊻ \[7P0..1] ⊻ \[8P0..1]||
||ZA0|Uhrzeit gestellt<br/>/Synchronisation|X \[4P0..1] ⊻ \[6P0..1] ⊻ \[7P0..1] ⊻ \[8P0..1]||
||ZA1|Messwert unplausibel|X \[6P0..1] ⊻ \[7P0..1] ⊻ \[8P0..1]||
||ZA4|Fehlerhafte Ablesung|X \[4P0..1] ⊻ \[5P0..1] ⊻ \[6P0..1] ⊻ \[7P0..1] ⊻ \[8P0..1]||
||ZA5|Änderung der Berechnung|X \[4P0..1] ⊻ \[5P0..1] ⊻ \[6P0..1] ⊻ \[7P0..1] ⊻ \[8P0..1]||
||ZA6|Umbau der Messlokation|X \[4P0..1] ⊻ \[5P0..1] ⊻ \[6P0..1] ⊻ \[7P0..1] ⊻ \[8P0..1]||
||ZA7|Datenbearbeitungsfehler|X \[4P0..1] ⊻ \[5P0..1] ⊻ \[6P0..1] ⊻ \[7P0..1] ⊻ \[8P0..1]||
||ZA8|Brennwertkorrektur|X \[4P0..1] ⊻ \[5P0..1] ⊻ \[6P0..1] ⊻ \[7P0..1] ⊻ \[8P0..1]||
||ZA9|Z-Zahl-Korrektur|X \[4P0..1] ⊻ \[5P0..1] ⊻ \[6P0..1] ⊻ \[7P0..1] ⊻ \[8P0..1]||
||ZB0|Störung / Defekt<br/>Messeinrichtung|X \[4P0..1] ⊻ \[5P0..1] ⊻ \[6P0..1] ⊻ \[7P0..1] ⊻ \[8P0..1]||
||ZC4|Impulswertigkeit nicht<br/>ausreichend|X \[4P0..1] ⊻ \[7P0..1] ⊻ \[8P0..1]||
||ZR1|Wartungsarbeiten an<br/>geeichtem Messgerät|X \[4P0..1] ⊻ \[6P0..1] ⊻ \[7P0..1] ⊻ \[8P0..1]||
||ZR2|gestörte Werte|X \[4P0..1] ⊻ \[6P0..1] ⊻ \[7P0..1] ⊻ \[8P0..1]||
||ZR3|Wartungsarbeiten an<br/>eichrechtskonformen<br/>Messgeräten|X \[4P0..1] ⊻ \[6P0..1] ⊻ \[7P0..1] ⊻ \[8P0..1]||
||ZR4|Konsistenz- und<br/>Synchronprüfung|X \[4P0..1] ⊻ \[6P0..1] ⊻ \[7P0..1] ⊻ \[8P0..1]||
|Grund der<br/>Ersatzwertbildung|||||
|SG10|||||
|SG10 STS 00038|||Muss \[92]|\[92] Wenn SG10 QTY DE6063 mit Wert 67 vorhanden|
|SG10 STS 9015|Z40|Grund der<br/>Ersatzwertbildung|X||


Version: 3.1f 30.09.2025 Seite 122 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|EDIFACT Struktur|Beschreibung|Gasbeschaffenheit|Bedingung|
|-|-|-|-|
||Prüfidentifikator|13007||
|SG10 STS \*\*9013\*\*|\*\*Z74\*\* kein Zugang|X \[4P0..1]||
||\*\*Z75\*\* Kommunikationsstörung|X \[4P0..1]||
||\*\*Z76\*\* Netzausfall|X \[4P0..1]||
||\*\*Z78\*\* Gerätewechsel|X \[4P0..1]||
||\*\*Z80\*\* Gerät arbeitet außerhalb<br/>der Betriebsbedingungen|X \[4P0..1]||
||\*\*Z81\*\* Messeinrichtung<br/>gestört/defekt|X \[4P0..1]||
||\*\*Z82\*\* Unsicherheit Messung|X \[4P0..1]||
||\*\*Z98\*\* Berücksichtigung<br/>Störmengenzählwerk|X \[4P0..1]||
||\*\*Z99\*\* Mengenumwertung<br/>unvollständig|X \[4P0..1]||
||\*\*ZA0\*\* Uhrzeit gestellt<br/>/Synchronisation|X \[4P0..1]||
||\*\*ZA1\*\* Messwert unplausibel|X \[4P0..1]||
||\*\*ZA4\*\* Fehlerhafte Ablesung|X \[4P0..1]||
||\*\*ZA5\*\* Änderung der Berechnung|X \[4P0..1]||
||\*\*ZA6\*\* Umbau der Messlokation|X \[4P0..1]||
||\*\*ZA7\*\* Datenbearbeitungsfehler|X \[4P0..1]||
||\*\*ZB0\*\* Störung / Defekt<br/>Messeinrichtung|X \[4P0..1]||
||\*\*ZC4\*\* Impulswertigkeit nicht<br/>ausreichend|X \[4P0..1]||
||\*\*ZR1\*\* Wartungsarbeiten an<br/>geeichtem Messgerät|X \[4P0..1]||
||\*\*ZR2\*\* gestörte Werte|X \[4P0..1]||
||\*\*ZR3\*\* Wartungsarbeiten an<br/>eichrechtskonformen<br/>Messgeräten|X \[4P0..1]||
||\*\*ZR4\*\* Konsistenz- und<br/>Synchronprüfung|X \[4P0..1]||
|Gasqualität||||
|\*\*SG10\*\*||||
|SG10 STS 00039||Soll \[97]|\[97] Wenn es sich um die<br/>Übermittlung eines Wertes aufgrund<br/>der Umstellung der Gasqualität<br/>handelt|
|SG10 STS \*\*9015\*\*|\*\*Z31\*\* Gasqualität|X||
|SG10 STS \*\*9013\*\*|\*\*ZG3\*\* Umstellung Gasqualität|X||
|Nachrichten-Endesegment||||
|\*\*UNT\*\* 00041||Muss||
|UNT \*\*0074\*\*|Anzahl der Segmente in einer<br/>Nachricht|X||
|UNT \*\*0062\*\*|Nachrichten-Referenznummer|X||
|Nutzdaten-Endesegment||||
|\*\*UNZ\*\* 00042||Muss||
|UNZ \*\*0036\*\*|Datenaustauschzähler|X||
|UNZ \*\*0020\*\*|Datenaustauschreferenz|X||


Version: 3.1f 30.09.2025 Seite 123 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

# 10 Marktlokationsscharfe Allokationsliste Gas / marktlokationsscharfe bilanzierte Menge Strom/Gas

## 10.1 Übertragung marktlokationsscharfe Allokationsliste Gas

Tabellenspalte = marktlokationsscharfe Allokationsliste Gas (MMMA) 13013

Dieser Anwendungsfall dient zur Übertragung der marktlokationsscharfen Allokationsliste Gas für den Liefermonat als Basis für die Mehr- und Mindermengenabrechnung.

Es sind in der marktlokationsscharfen Allokationsliste alle Marktlokationen, die dem LF in dem Liefermonat bilanziell zugeordnet sind, gesamthaft zu übertragen.

Sollen Daten von mehreren Marktlokationen in einer Datei übertragen werden, ist je Marktlokation eine SG5 „Liefer-, bzw. Bezugsort“ zu verwenden, d. h. die SG5 ist entsprechend oft zu wiederholen.

Für Monate, in denen dem LF keine Marktlokationen bilanziell zugeordnet sind, erfolgt keine Übermittlung der marktlokationsscharfen Allokationsliste.

Kommunikationspartner, Identifikationsangabe und Art der Werte für diesen Anwendungsfall:

|Sparte|Kommunikation von|Art der Werte|Identifikationsangabe in SG6 LOC|Anmerkung|
|-|-|-|-|-|
|Gas|NB an LF|marktlokationsscharfe Allokationsliste|ID der Marktlokation|---|


## 10.2 Übertragung marktlokationsscharfe bilanzierte Menge Strom/Gas

Tabellenspalte = marktlokationsscharfe bilanzierte Menge Strom/Gas (MMMA) 13014

Dieser Anwendungsfall dient zur Übertragung der marktlokationsscharfen bilanzierten Menge als Basis für die Mehr- und Mindermengenabrechnung.

Sollen Daten von mehreren Marktlokationen in einer Datei übertragen werden, ist die Wiederholung über das UNH-Segment vorzunehmen.

Kommunikationspartner, Identifikationsangabe und Art der Werte für diesen Anwendungsfall:

|Sparte|Kommunikation von|Art der Werte|Identifikationsangabe in SG6 LOC|Anmerkung|
|-|-|-|-|-|
|Strom/Gas|NB an LF|bilanzierte Menge|ID der Marktlokation|---|
|Strom|ÜNB an NB|bilanzierte Menge|ID der Marktlokation|---|


Version: 3.1f 30.09.2025 Seite 124 von 158

MSCONS Anwendungshandbuch
![edi@energy. Datenformate Strom & Gas](image)

## 10.3 Anwendungsübersicht Allokationsliste Gas / bilanzierte Menge Strom/Gas

|EDIFACT Struktur|Beschreibung|marktlokations- scharfe Allokationsliste Gas (MMMA)|marktlokations- scharfe bilanzierte Menge Strom / Gas (MMMA)|Bedingung|||
|-|-|-|-|-|-|-|
||Prüfidentifikator|13013|13014||||
|Nutzdaten-Kopfsegment|||||||
|UNB|00002||Muss|Muss|||
|UNB|0001|UNOC|UN/ECE-Zeichensatz C|X|X||
|UNB|0002|3|Version 3|X|X||
|UNB|0004|MP-ID Absender|X|X|||
|UNB|0007|14|GS1|X|X||
|||500|DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)||X||
|||502|DE, DVGW Service & Consult GmbH|X|X||
|UNB|0010|MP-ID Empfänger|X|X|||
|UNB|0007|14|GS1|X|X||
|||500|DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)||X||
|||502|DE, DVGW Service & Consult GmbH|X|X||
|UNB|0017|Datum der Erstellung|X|X|||
|UNB|0019|Uhrzeit der Erstellung|X|X|||
|UNB|0020|Datenaustauschreferenz|X \[918]|X \[918]|\[918] Format: Zeichen aus dem über UNOC definierten Zeichensatz, wobei von den Buchstaben nur Großbuchstaben erlaubt sind.||
|UNB|0026|EM|Energiemenge|X|X||
|Nachrichtenkopfsegment|||||||
|UNH|00003||Muss|Muss|||
|UNH|0062|Nachrichten-Referenznummer|X|X|||
|UNH|0065|MSCONS|Bericht über den Verbrauch messbarer Dienstleistungen|X|X||
|UNH|0052|D|Entwurfs-Version|X|X||
|UNH|0054|04B|Ausgabe 2004 - B|X|X||
|UNH|0051|UN|UN/CEFACT|X|X||
|UNH|0057|2.4c|Versionsnummer der zugrundeliegenden BDEW-Nachrichtenbeschreibung|X|X||
|UNH|0068|Allgemeine Zuordnungs-Referenz|Soll \[22]||\[22] Wenn Aufteilung vorhanden||
|UNH|0070|Übermittlungsfolgenummer|X||||
|UNH|0073|C|Beginn|Muss \[23]||\[23] Wenn UNH DE0070 mit 1 vorhanden|
||F|Ende|Soll \[24]||\[24] Bei Aufteilung, in der Nachricht mit der höchsten Übermittlungsnummer||
|Beginn der Nachricht|||||||
|BGM|00004||Muss|Muss|||
|BGM|1001|Z23|Bilanzierte Menge (MMMA)||X||
|||Z24|Allokationsliste (MMMA)|X|||
|BGM|1004|Dokumentennummer|X|X|||
|BGM|1225|9|Original|X|X||


Version: 3.1f
30.09.2025
Seite 125 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|EDIFACT Struktur|Beschreibung<br/>Prüfidentifikator|marktlokations- scharfe Allokationsliste Gas (MMMA)<br/>13013|marktlokations- scharfe bilanzierte Menge Strom / Gas (MMMA)<br/>13014|Bedingung||||
|-|-|-|-|-|-|-|-|
|Nachrichtendatum|||Muss|Muss||||
|DTM|00005||Muss|Muss||||
|DTM|2005|137|Dokumenten- /Nachrichtendatum/-zeit|X|X|||
|DTM|2380||Datum oder Uhrzeit oder Zeitspanne, Wert|X \[931] \[494]|X \[931] \[494]|\[494] Das hier genannte Datum muss der Zeitpunkt sein, zu dem das Dokument erstellt wurde, oder ein Zeitpunkt, der davor liegt.<br/>\[931] Format: ZZZ = +00||
|DTM|2379|303|CCYYMMDDHHMMZZZ|X|X|||
|Referenzangaben||||||||
|SG1|||Muss|Muss \[81] ∧ \[36]|\[36] wenn MP-ID in SG2 NAD+MR in der Rolle NB<br/>\[81] Wenn MP-ID in SG2 NAD+MS in der Rolle ÜNB|||
|SG1|RFF|00006||Muss|Muss|||
|SG1|RFF|1153|AGI|Beantragungsnummer|X|X||
|SG1|RFF|1154||Referenznummer|X \[526]|X \[543]|\[526] Hinweis: Wert aus BGM+Z24 DE1004 der ORDERS mit der die Allokationsliste bestellt wurde.<br/>\[543] Hinweis: Wert aus BGM+Z23 DE1004 der ORDERS mit der die bilanzierte Menge bestellt wurde.|
|Versionsangabe marktlokationsscharfe Allokationsliste Gas (MMMA)||||||||
|SG1||||||||
|SG1|DTM|00007||Muss||||
|SG1|DTM|2005|293|Fertigstellungsdatum/-zeit|X|||
|SG1|DTM|2380||Datum oder Uhrzeit oder Zeitspanne, Wert|X \[931]||\[931] Format: ZZZ = +00|
|SG1|DTM|2379|304|CCYYMMDDHHMMSSZZZ|X|||
|Prüfidentifikator||||||||
|SG1|||Muss|Muss||||
|SG1|RFF|00009||Muss|Muss|||
|SG1|RFF|1153|Z13|Prüfidentifikator|X|X||
|SG1|RFF|1154|13013|Marktlokationsscharfe Allokationsliste Gas (MMMA)|X|||
|||13014|Marktlokationsscharfe bilanzierte Menge (MMMA)||X|||
|MP-ID Absender||||||||
|SG2|||Muss|Muss||||
|SG2|NAD|00010||Muss|Muss|||
|SG2|NAD|3035|MS|Dokumenten- /Nachrichtenaussteller bzw. -absender|X|X||
|SG2|NAD|3039||MP-ID|X \[118]|X|\[118] Nur MP-ID aus Sparte Gas|
|SG2|NAD|3055|9|GS1|X|X||
|||293|DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)||X|||
|||332|DE, DVGW Service & Consult GmbH|X|X|||
|Ansprechpartner||||||||


Version: 3.1f
30.09.2025
Seite 126 von 158

MSCONS Anwendungshandbuch
![edi@energy. Datenformate Strom & Gas](image)

|EDIFACT Struktur|Beschreibung<br/>Prüfidentifikator|marktlokations-scharfe Allokationsliste Gas (MMMA)<br/>13013|marktlokations-scharfe bilanzierte Menge Strom / Gas (MMMA)<br/>13014|Bedingung|||||
|-|-|-|-|-|-|-|-|-|
|\*\*SG4\*\*|||\*\*Kann\*\*|\*\*Kann\*\*|||||
|\*\*SG4\*\*|\*\*CTA\*\*|00011||\*\*Muss\*\*|\*\*Muss\*\*||||
|SG4|CTA|3139||\*\*IC\*\*|Informationsstelle|X|X||
|SG4|CTA|3412||Abteilung oder Bearbeiter|X|X|||
|Kommunikationsverbindung|||||||||
|\*\*SG4\*\*|||||||||
|\*\*SG4\*\*|\*\*COM\*\*|00012||\*\*Muss\*\*|\*\*Muss\*\*||||
|SG4|COM|3148||Kommunikationsadresse, Identifikation|X ((\[939] \[142]) ∨ (\[940] \[143])) ∧ \[576]|X ((\[939] \[142]) ∨ (\[940] \[143])) ∧ \[576]|\[142] wenn im DE3155 in demselben COM der Code EM vorhanden ist<br/>\[143] wenn im DE3155 in demselben COM der Code TE / FX / AJ / AL vorhanden ist<br/>\[576] Hinweis: Es darf nur eine Information im DE3148 übermittelt werden<br/>\[939] Format: Die Zeichenkette muss die Zeichen @ und . enthalten<br/>\[940] Format: Die Zeichenkette muss mit dem Zeichen + beginnen und danach dürfen nur noch Ziffern folgen||
|SG4|COM|3155||\*\*TE\*\*|Telefon|X \[1P0..1]|X \[1P0..1]||
||||\*\*EM\*\*|E-Mail|X \[1P0..1]|X \[1P0..1]|||
||||\*\*AJ\*\*|weiteres Telefon|X \[1P0..1]|X \[1P0..1]|||
||||\*\*AL\*\*|Handy|X \[1P0..1]|X \[1P0..1]|||
||||\*\*FX\*\*|Telefax|X \[1P0..1]|X \[1P0..1]|||
|MP-ID Empfänger|||||||||
|\*\*SG2\*\*|||\*\*Muss\*\*|\*\*Muss\*\*|||||
|\*\*SG2\*\*|\*\*NAD\*\*|00013||\*\*Muss\*\*|\*\*Muss\*\*||||
|SG2|NAD|3035||\*\*MR\*\*|Nachrichtenempfänger|X|X||
|SG2|NAD|3039||MP-ID|X \[118]|X|\[118] Nur MP-ID aus Sparte Gas||
|SG2|NAD|3055||\*\*9\*\*|GS1|X|X||
||||\*\*293\*\*|DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)||X|||
||||\*\*332\*\*|DE, DVGW Service & Consult GmbH|X|X|||
|Abschnitts-Kontrollsegment|||||||||
|\*\*UNS\*\*|00014||\*\*Muss\*\*|\*\*Muss\*\*|||||
|UNS|0081||\*\*D\*\*|Trennung von Kopf- und Positionsteil|X|X|||
|Name und Adresse|||||||||
|\*\*SG5\*\*|||\*\*Muss\*\*|\*\*Muss \[2001]\*\*|\[2001] Segmentgruppe ist nur einmal je UNH anzugeben||||
|\*\*SG5\*\*|\*\*NAD\*\*|00015||\*\*Muss\*\*|\*\*Muss\*\*||||
|SG5|NAD|3035||\*\*DP\*\*|Lieferanschrift|X|X||
|Identifikationsangabe|||||||||
|\*\*SG6\*\*|||\*\*Muss\*\*|\*\*Muss\*\*|||||
|\*\*SG6\*\*|\*\*LOC\*\*|00017||\*\*Muss\*\*|\*\*Muss\*\*||||
|SG6|LOC|3227||\*\*172\*\*|Meldepunkt|X|X||
|SG6|LOC|3225||Bezeichnung|X \[950] \[514]|X \[950] \[514]|\[514] Hinweis: Verwendung der ID der Marktlokation<br/>\[950] Format: Marktlokations-ID||
|Bilanzierungsmonat|||||||||
|\*\*SG6\*\*|||||||||
|\*\*SG6\*\*|\*\*DTM\*\*|00020||\*\*Muss\*\*|||||


Version: 3.1f 30.09.2025 Seite 127 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|EDIFACT Struktur|Beschreibung<br/>Prüfidentifikator|marktlokations-scharfe Allokationsliste Gas (MMMA)<br/>13013|marktlokations-scharfe bilanzierte Menge Strom / Gas (MMMA)<br/>13014|Bedingung||||
|-|-|-|-|-|-|-|-|
|SG6|DTM|2005|\*\*492\*\*|Bilanzierungsdatum, -zeit, -periode|X|||
|SG6|DTM|2380||Datum oder Uhrzeit oder Zeitspanne, Wert|X|||
|SG6|DTM|2379|\*\*610\*\*|CCYYMM|X|||
|lfd. Position||||||||
|SG9|||Muss|Muss||||
|SG9|LIN||00026|Muss|Muss|||
|SG9|LIN|1082|Positionsnummer|X \[908]|X \[908]|\[908] Format: Mögliche Werte: 1 bis n||
|Produktidentifikation||||||||
|SG9|||Muss|Muss||||
|SG9|PIA||00027|Muss|Muss|||
|SG9|PIA|4347|\*\*5\*\*|Produktidentifikation|X|X||
|SG9|PIA|7140||Medium / OBIS-Kennzahl|X \[501]|X \[501]|\[501] Hinweis: Es sind nur die Werte erlaubt, die in der EDI\@Energy Codeliste der OBIS-Kennzahlen und Medien mit dem entsprechenden Prüfidentifikator versehen sind.|
|SG9|PIA|7143|\*\*Z02\*\*|BDEW OBIS-ähnliche Kennzahl|X|X||
|Mengenangaben||||||||
|SG10|||Muss|Muss||||
|SG10|QTY||00028|Muss|Muss|||
|SG10|QTY|6063|\*\*79\*\*|Energiemenge summiert (Summenwert, Bilanzsumme)|X|X||
|SG10|QTY|6060||Menge|X \[902] ∧ \[906]|X \[902] ∧ \[906]|\[902] Format: Möglicher Wert: ≥ 0<br/>\[906] Format: max. 3 Nachkommastellen|
|Beginn Messperiode||||||||
|SG10||||Muss||||
|SG10|DTM||00029||Muss|||
|SG10|DTM|2005|\*\*163\*\*|Verarbeitung, Beginndatum/-zeit||X||
|SG10|DTM|2380||Datum oder Uhrzeit oder Zeitspanne, Wert||X \[UB3] ∧ \[495]|\[495] Der Zeitpunkt muss ≤ dem Wert im DE2380 des DTM+137 sein|
|SG10|DTM|2379|\*\*303\*\*|CCYYMMDDHHMMZZZ||X||
|Ende Messperiode||||||||
|SG10||||Muss||||
|SG10|DTM||00030||Muss|||
|SG10|DTM|2005|\*\*164\*\*|Verarbeitung, Endedatum/-zeit||X||
|SG10|DTM|2380||Datum oder Uhrzeit oder Zeitspanne, Wert||X \[UB3] ∧ \[495]|\[495] Der Zeitpunkt muss ≤ dem Wert im DE2380 des DTM+137 sein|
|SG10|DTM|2379|\*\*303\*\*|CCYYMMDDHHMMZZZ||X||
|Leistungsperiode||||||||
|SG10|||Muss|||||
|SG10|DTM||00034|Muss||||
|SG10|DTM|2005|\*\*306\*\*|Leistungsperiode|X|||
|SG10|DTM|2380||Datum oder Uhrzeit oder Zeitspanne, Wert|X|||
|SG10|DTM|2379|\*\*102\*\*|CCYYMMDD|X|||
|Nachrichten-Endesegment||||||||
|UNT||00041|Muss|Muss||||


Version: 3.1f 30.09.2025 Seite 128 von 158

MSCONS Anwendungshandbuch
![edi@energy. Datenformate Strom & Gas](image)

|EDIFACT Struktur||Beschreibung<br/>Prüfidentifikator|marktlokations-scharfe Allokationsliste Gas (MMMA)<br/>13013|marktlokations-scharfe bilanzierte Menge Strom / Gas (MMMA)<br/>13014|Bedingung||
|-|-|-|-|-|-|-|
|UNT|0074|Anzahl der Segmente in einer Nachricht|X|X|||
|UNT|0062|Nachrichten-Referenznummer|X|X|||
|Nutzdaten-Endesegment|||||||
|UNZ||00042||Muss|Muss||
|UNZ|0036|Datenaustauschzähler|X|X|||
|UNZ|0020|Datenaustauschreferenz|X|X|||


Version: 3.1f	30.09.2025	Seite 129 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

# 11 Werte nach Typ 2

## 11.1 Übermittlung Werte nach Typ 2

Tabellenspalte = Werte nach Typ 2 13027

Dieser Anwendungsfall dient zur Übertragung von Werten nach Typ 2, die vorher bei beim MSB mit dem entsprechenden Messprodukt-Code bestellt wurden.

Kommunikationspartner, Identifikationsangabe und Art der Werte für diesen Anwendungsfall:

|Sparte|Kommunikation von|Art der Werte|Identifikationsangabe in SG6 LOC|Anmerkung|
|-|-|-|-|-|
|Strom|MSB an ESA|Werte nach Typ 2 zur Bestellung|ID der Messlokation<br/>ID der Marktlokation<br/>ID der Netzlokation<br/>ID der Tranche|--|
|Strom|MSB an MSB|Werte nach Typ 2 zur Bestellung|ID der Messlokation<br/>ID der Marktlokation<br/>ID der Netzlokation|--|
|Strom|MSB an NB|Werte nach Typ 2 zur Bestellung|ID der Messlokation<br/>ID der Marktlokation<br/>ID der Netzlokation|--|
|Strom|MSB an LF|Werte nach Typ 2 zur Bestellung|ID der Messlokation<br/>ID der Marktlokation<br/>ID der Netzlokation|--|


Version: 3.1f 30.09.2025 Seite 130 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

## 11.2 Anwendungsübersicht Werte nach Typ 2

|EDIFACT Struktur|Beschreibung<br/>Prüfidentifikator|Werte nach Typ 2<br/>13027|Bedingung||||
|-|-|-|-|-|-|-|
|Nutzdaten-Kopfsegment||Muss|||||
|UNB|00002||Muss||||
|UNB|0001|UNOC|UN/ECE-Zeichensatz C|X|||
|UNB|0002|3|Version 3|X|||
|UNB|0004|MP-ID Absender|X||||
|UNB|0007|14|GS1|X|||
||500|DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)|X||||
|UNB|0010|MP-ID Empfänger|X||||
|UNB|0007|14|GS1|X|||
||500|DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)|X||||
|UNB|0017|Datum der Erstellung|X||||
|UNB|0019|Uhrzeit der Erstellung|X||||
|UNB|0020|Datenaustauschreferenz|X \[918]|\[918] Format: Zeichen aus dem über UNOC definierten Zeichensatz, wobei von den Buchstaben nur Großbuchstaben erlaubt sind.|||
|UNB|0026|TL|Lastgang, beliebiger Zeitraum|X|||
|Nachrichtenkopfsegment||Muss|||||
|UNH|00003||Muss||||
|UNH|0062|Nachrichten-Referenznummer|X||||
|UNH|0065|MSCON Bericht über den Verbrauch messbarer Dienstleistungen|X||||
||S||||||
|UNH|0052|D|Entwurfs-Version|X|||
|UNH|0054|04B|Ausgabe 2004 - B|X|||
|UNH|0051|UN|UN/CEFACT|X|||
|UNH|0057|2.4c|Versionsnummer der zugrundeliegenden BDEW-Nachrichtenbeschreibung|X|||
|Beginn der Nachricht||Muss|||||
|BGM|00004||Muss||||
|BGM|1001|Z83|Werte nach Typ 2|X|||
|BGM|1004|Dokumentennummer|X||||
|BGM|1225|9|Original|X|||
|Nachrichtendatum||Muss|||||
|DTM|00005||Muss||||
|DTM|2005|137|Dokumenten-/Nachrichtendatum/-zeit|X|||
|DTM|2380|Datum oder Uhrzeit oder Zeitspanne, Wert|X \[931] \[494]|\[494] Das hier genannte Datum muss der Zeitpunkt sein, zu dem das Dokument erstellt wurde, oder ein Zeitpunkt, der davor liegt.<br/>\[931] Format: ZZZ = +00|||
|DTM|2379|303|CCYYMMDDHHMMZZZ|X|||
|Referenzangaben||Muss|||||
|SG1||Muss|||||
|SG1|RFF|00006||Muss|||
|SG1|RFF|1153|AGI|Beantragungsnummer|X||
|SG1|RFF|1154|Referenznummer|X \[574]|\[574] Hinweis: Wert aus BGM DE1004 der ORDERS mit der die Bestellung der Werte nach Typ 2 erfolg ist||
|Prüfidentifikator||Muss|||||
|SG1||Muss|||||
|SG1|RFF|00009||Muss|||
|SG1|RFF|1153|Z13|Prüfidentifikator|X||
|SG1|RFF|1154|13027|Werte nach Typ 2|X||


Version: 3.1f
30.09.2025
Seite 131 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|EDIFACT Struktur|Beschreibung<br/>Prüfidentifikator|Werte nach Typ 2<br/>13027|Bedingung|||||
|-|-|-|-|-|-|-|-|
|MP-ID Absender||Muss||||||
|\*\*SG2\*\*|||\*\*Muss\*\*|||||
|SG2|\*\*NAD\*\*||00010||\*\*Muss\*\*|||
|SG2|NAD|\*\*3035\*\*||\*\*MS\*\*|Dokumenten-/Nachrichtenaussteller bzw. -absender|X||
|SG2|NAD|\*\*3039\*\*||MP-ID||X \[117]|\[117] Nur MP-ID aus Sparte Strom|
|SG2|NAD|\*\*3055\*\*||\*\*9\*\*|GS1|X||
||||\*\*293\*\*|DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)|X|||
|Ansprechpartner||Kann||||||
|\*\*SG4\*\*|||\*\*Muss\*\*|||||
|SG4|\*\*CTA\*\*||00011||\*\*Muss\*\*|||
|SG4|CTA|\*\*3139\*\*||\*\*IC\*\*|Informationsstelle|X||
|SG4|CTA|\*\*3412\*\*||Abteilung oder Bearbeiter|X|||
|Kommunikationsverbindung||||||||
|\*\*SG4\*\*||||||||
|SG4|\*\*COM\*\*||00012||\*\*Muss\*\*|||
|SG4|COM|\*\*3148\*\*||Kommunikationsadresse, Identifikation|X ((\[939] \[142]) ∨ (\[940] \[143])) ∧ \[576]|\[142] wenn im DE3155 in demselben COM der Code EM vorhanden ist<br/>\[143] wenn im DE3155 in demselben COM der Code TE / FX / AJ / AL vorhanden ist<br/>\[576] Hinweis: Es darf nur eine Information im DE3148 übermittelt werden<br/>\[939] Format: Die Zeichenkette muss die Zeichen @ und . enthalten<br/>\[940] Format: Die Zeichenkette muss mit dem Zeichen + beginnen und danach dürfen nur noch Ziffern folgen||
|SG4|COM|\*\*3155\*\*||\*\*TE\*\*|Telefon|X \[1P0..1]||
||||\*\*EM\*\*|E-Mail|X \[1P0..1]|||
||||\*\*AJ\*\*|weiteres Telefon|X \[1P0..1]|||
||||\*\*AL\*\*|Handy|X \[1P0..1]|||
||||\*\*FX\*\*|Telefax|X \[1P0..1]|||
|MP-ID Empfänger||Muss||||||
|\*\*SG2\*\*|||\*\*Muss\*\*|||||
|SG2|\*\*NAD\*\*||00013||\*\*Muss\*\*|||
|SG2|NAD|\*\*3035\*\*||\*\*MR\*\*|Nachrichtenempfänger|X||
|SG2|NAD|\*\*3039\*\*||MP-ID||X \[117]|\[117] Nur MP-ID aus Sparte Strom|
|SG2|NAD|\*\*3055\*\*||\*\*9\*\*|GS1|X||
||||\*\*293\*\*|DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)|X|||
|Abschnitts-Kontrollsegment||||||||
||\*\*UNS\*\*||00014||\*\*Muss\*\*|||
||UNS|\*\*0081\*\*||\*\*D\*\*|Trennung von Kopf- und Positionsteil|X||
|Name und Adresse||||||||
|\*\*SG5\*\*|||\*\*Muss \[2001]\*\*|\[2001] Segmentgruppe ist nur einmal je UNH anzugeben||||
|SG5|\*\*NAD\*\*||00015||\*\*Muss\*\*|||
|SG5|NAD|\*\*3035\*\*||\*\*DP\*\*|Lieferanschrift|X||
|Identifikationsangabe||||||||
|\*\*SG6\*\*|||\*\*Muss\*\*|||||
|SG6|\*\*LOC\*\*||00017||\*\*Muss\*\*|||
|SG6|LOC|\*\*3227\*\*||\*\*172\*\*|Meldepunkt|X||


Version: 3.1f 30.09.2025 Seite 132 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|EDIFACT Struktur|Beschreibung|Werte nach Typ 2|Bedingung||||
|-|-|-|-|-|-|-|
|||Prüfidentifikator|13027||||
|SG6|LOC|3225|Bezeichnung|X (\[950] (\[514] ∨ \[518])) ∨ (\[951] \[510]) ∨ (\[960] \[575])|\[510] Hinweis: Verwendung der ID der Messlokation<br/>\[514] Hinweis: Verwendung der ID der Marktlokation<br/>\[518] Hinweis: Verwendung der ID der Tranche<br/>\[575] Hinweis: Verwendung der ID der Netzlokation<br/>\[950] Format: Marktlokations-ID<br/>\[951] Format: Zählpunktbezeichnung<br/>\[960] Format: Netzlokations-ID||
|lfd. Position|||||||
|SG9|||Muss||||
|SG9|LIN||00026|Muss|||
|SG9|LIN|1082|Positionsnummer|X \[908]|\[908] Format: Mögliche Werte: 1 bis n||
|Produktidentifikation|||||||
|SG9|||Muss||||
|SG9|PIA||00027|Muss|||
|SG9|PIA|4347|5|Produktidentifikation|X||
|SG9|PIA|7140|Medium / OBIS-Kennzahl|X \[501]|\[501] Hinweis: Es sind nur die Werte erlaubt, die in der EDI\@Energy Codeliste der OBIS-Kennzahlen und Medien mit dem entsprechenden Prüfidentifikator versehen sind.||
|SG9|PIA|7143|SRW|OBIS-Kennzahl|X||
|Mengenangaben|||||||
|SG10|||Muss||||
|SG10|QTY||00028|Muss|||
|SG10|QTY|6063|220|Wahrer Wert|X||
|||67|Ersatzwert|X|||
|||Z18|Vorläufiger Wert|X|||
|SG10|QTY|6060|Menge|X \[902] ∧ \[906]|\[902] Format: Möglicher Wert: ≥ 0<br/>\[906] Format: max. 3 Nachkommastellen||
|Beginn Messperiode|||||||
|SG10|||||||
|SG10|DTM||00029|Muss \[147] ∧ \[148]|\[147] Wenn in derselben S9 LIN das SG10 DTM+7 (Nutzungszeitpunkt) nicht vorhanden ist.<br/>\[148] Wenn es bei dem zu übermittelnden Wert um einen Wert in einem Zeitintervall handelt.||
|SG10|DTM|2005|163|Verarbeitung, Beginndatum/-zeit|X||
|SG10|DTM|2380|Datum oder Uhrzeit oder Zeitspanne, Wert|X \[931] \[495]|\[495] Der Zeitpunkt muss ≤ dem Wert im DE2380 des DTM+137 sein<br/>\[931] Format: ZZZ = +00||
|SG10|DTM|2379|303|CCYYMMDDHHMMZZZ|X||
|Ende Messperiode|||||||
|SG10|||||||
|SG10|DTM||00030|Muss \[149]|\[149] Wenn in derselben S9 LIN das SG10 DTM+163 (Beginn Messperiode) vorhanden ist.||
|SG10|DTM|2005|164|Verarbeitung, Endedatum/-zeit|X||
|SG10|DTM|2380|Datum oder Uhrzeit oder Zeitspanne, Wert|X \[931] \[495]|\[495] Der Zeitpunkt muss ≤ dem Wert im DE2380 des DTM+137 sein<br/>\[931] Format: ZZZ = +00||
|SG10|DTM|2379|303|CCYYMMDDHHMMZZZ|X||
|Nutzungszeitpunkt|||||||
|SG10|||||||


Version: 3.1f 30.09.2025 Seite 133 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|EDIFACT Struktur|Beschreibung<br/>Prüfidentifikator|Werte nach Typ 2<br/>13027|Bedingung||
|-|-|-|-|-|
|SG10 DTM|00032||Muss \[145] ∧ \[146]|\[145] Wenn in derselben S9 LIN das SG10 DTM+163 (Beginn Messperiode) nicht vorhanden ist.<br/>\[146] Wenn es bei dem zu übermittelnden Wert um einen Wert zu einem Zeitpunkt handelt.|
|SG10 DTM 2005|7 Gültigkeitsdatum/-zeit|X|||
|SG10 DTM 2380|Datum oder Uhrzeit oder Zeitspanne, Wert|X \[931] \[495]|\[495] Der Zeitpunkt muss ≤ dem Wert im DE2380 des DTM+137 sein<br/>\[931] Format: ZZZ = +00||
|SG10 DTM 2379|303 CCYYMMDDHHMMZZZ|X|||
|Nachrichten-Endesegment|||||
|UNT|00041||Muss||
|UNT 0074|Anzahl der Segmente in einer Nachricht|X|||
|UNT 0062|Nachrichten-Referenznummer|X|||
|Nutzdaten-Endesegment|||||
|UNZ|00042||Muss||
|UNZ 0036|Datenaustauschzähler|X|||
|UNZ 0020|Datenaustauschreferenz|X|||


Version: 3.1f 30.09.2025 Seite 134 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

# 12 Stornierung / Korrektur von Werten

## 12.1 Stornierung von Werten

Diese Form wird verwendet, wenn alle zuvor übertragenen Werte einer Nachricht vom ursprünglichen Versender der Nachricht storniert werden sollen. Eine Nachricht kann immer nur Daten eines Meldepunktes, eines Lastprofils oder einer EEG-Überführungszeitreihe zu einem Ablesezeitpunkt/Zeitintervall enthalten.

Die Referenz zur Originalnachricht wird in SG1 RFF+ACW DE1154 (Referenzangaben) angegeben.

## 12.2 Korrektur von Werten

Es gibt drei Arten von Korrekturen:

*   Variante 1: die Stornierung und Neuversand
*   Variante 2: die Überschreibung von Werten
*   Variante 3: den Neuversand von neuen Werten ohne Überschreibung und mit Referenzierung in anderer Nachricht

**Variante 1: Stornierung und Neuversand**

Eine MSCONS-Nachricht wird storniert, wenn mindestens eine Information der MSCONS-Nachricht nicht korrekt war. Eine eventuelle Korrektur erfolgt über die nachfolgende Versendung einer neuen Nachricht. Für die Stornierung von Werten ist immer der Sender der zu stornierenden Nachricht verantwortlich. Gegebenenfalls ist zu jedem korrigierenden Wert ein Korrekturgrund anzugeben, welcher den Grund der Korrektur enthält. Details zu den einzelnen Anwendungsfällen sind der nachstehenden Tabelle zu entnehmen.

**Variante 2: Überschreibung von Werten**

Eine Korrektur erfolgt über die Versionierung der Werte. Der Absender ist für die Versionierung der Werte verantwortlich. Gegebenenfalls ist zu jedem korrigierenden Wert ein Korrekturgrund anzugeben, welcher den Grund der Korrektur enthält. Diese Vorgehensweise entspricht auch dem Kapitel „Prozess Messwertermittlung im Fehlerfall“ der GPKE, GeLi Gas, WiM Strom und WiM Gas. Details zu den einzelnen Anwendungsfällen sind der nachstehenden Tabelle zu entnehmen.

**Variante 3: Neuversand von neuen Werten ohne Überschreibung und mit Referenzierung in anderer Nachricht**

Eine Korrektur erfolgt über den neuen Versand einer MSCONS-Nachricht. Dabei werden die Werte nicht überschrieben.

## 12.3 Übersicht Korrekturvarianten von Werten je ursprünglichem Anwendungsfall

Die folgende Tabelle beschreibt abschließend, in welchem Anwendungsfall der ursprüngliche Wert ausgetauscht wurde und welche Variante der Korrektur durch den Versender der ursprünglichen Nachricht anzuwenden ist.

Version: 3.1f 30.09.2025 Seite 135 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|Anwendungsfall in dem der ursprüngliche Wert ausgetauscht wurde|Korrekturvariante|Korrektur- grund ist anzugeben|Bemerkung|
|-|-|-|-|
|Zählerstand Gas<br/>(Prüfidentifikator 13002)|Stornierung und Neuversand|Ja|--|
|Summenzeitreihen<br/>(Prüfidentifikator 13003)|Überschreibung von Werten|Nein|Eine Korrektur erfolgt über die Versionierung der Zeitreihen. Der Absender ist für die Versionierung der Zeitreihen verantwortlich.|
|EEG-Überführungszeitreihen<br/>(Prüfidentifikator 13005)|Überschreibung von Werten|Nein|Eine Korrektur erfolgt über die Versionierung der Zeitreihen. Der Absender ist für die Versionierung der Zeitreihen verantwortlich.|
|Gasbeschaffenheit<br/>(Prüfidentifikator 13007)|Überschreibung von Werten|Nein|Eine Korrektur erfolgt über die Versionierung der Nachricht. Der Absender ist für die Versionierung der Nachricht verantwortlich.|
|Lastgang Gas<br/>(Prüfidentifikator 13008)|Überschreibung von Werten|Ja|Eine Korrektur erfolgt über die Versionierung der Werte. Der Absender ist für die Versionierung der Werte verantwortlich.|
|Energiemenge Gas<br/>(Prüfidentifikator 13009)|Stornierung und Neuversand|Ja|Auf Ebene der Messlokation:<br/>Bei der Korrektur von „Korrekturenergiemengen“, die auf Ebene der Messlokation übermittelt worden sind.<br/>Hinweis:<br/>Bei „Korrekturenergiemengen“, die auf Ebene der Messlokation übermittelt werden, muss in jedem Fall ein Korrekturgrund mitgegeben werden.|
||Stornierung und Neuversand|Ja|Bei der Korrektur von Energiemengen auf Ebene der Marktlokation, die als Auslöser aufgrund eines Zählerstandes auf Ebene der Messlokation erzeugt wurden, der den Endzeitpunkt einer Rechnung darstellt.|
|Normiertes Profil<br/>(Prüfidentifikator 13010)|Überschreibung von Werten|Nein|Eine Korrektur erfolgt über die Versionierung der Zeitreihen. Der Absender ist für die Versionierung der Zeitreihen verantwortlich.|
|Profilschar<br/>(Prüfidentifikator 13011)|Überschreibung von Werten|Nein|Eine Korrektur erfolgt über die Versionierung der Zeitreihen. Der Absender ist für die Versionierung der Zeitreihen verantwortlich.|
|Vergangenheitswerte TEP mit Referenzmessung<br/>(Prüfidentifikator 13012)|Überschreibung von Werten|Nein|Eine Korrektur erfolgt über die Versionierung der Zeitreihen. Der Absender ist für die Versionierung der Zeitreihen verantwortlich.|
|Marktlokationsscharfe Allokationsliste Gas (MMMA)<br/>(Prüfidentifikator 13013)|Überschreibung von Werten|Nein|Eine Korrektur erfolgt über die Versionierung der Liste. Der Absender ist für die Versionierung der Liste verantwortlich. Eine Liste, auch wenn diese aufgrund Ihrer Größe in mehrere Listen aufgeteilt wurde, enthält immer dieselbe Versionierung.|
|Marktlokationsscharfe bilanzierte Menge (MMMA)<br/>(Prüfidentifikator 13014)|Neuversand von neuen Werten ohne Überschreibung und mit Referenzierung in anderer Nachricht|--|Referenz auf die bilanzierte Energiemenge in der INVOIC|
|Arbeit Leistungsmax. Kalenderjahr vor Lieferbeginn<br/>(Prüfidentifikator 13015)|Stornierung und Neuversand|Nein|--|
|Energiemenge u. Leistungsmaximum<br/>(Prüfidentifikator 13016)|Stornierung und Neuversand|Ja|--|
|Zählerstand Strom<br/>(Prüfidentifikator 13017)|Stornierung und Neuversand|Ja|--|
|Lastgang Messlokation, Netzgangzeitreihe, Netzkoppelpunkt, Netzlokation<br/>(Prüfidentifikator 13018)|Überschreibung von Werten|Ja|Eine Korrektur erfolgt über die Versionierung der Werte. Der Absender ist für die Versionierung der Werte verantwortlich.|
|Energiemenge Strom<br/>(Prüfidentifikator 13019)|Stornierung und Neuversand|Ja|Auf Ebene der Messlokation:|


<sup>2</sup> Die Angabe des Korrekturgrundes erfolgt beim Versand der korrigierten Werte.

Version: 3.1f 30.09.2025 Seite 136 von 158

MSCONS Anwendungshandbuch
![edi@energy. Datenformate Strom & Gas](image)

|Anwendungsfall in dem der ursprüngliche Wert ausgetauscht wurde|Korrekturvariante|Korrektur- grund ist anzugeben|Bemerkung|||
|-|-|-|-|-|-|
||||Bei der Korrektur von „Korrekturenergiemengen“, die auf Ebene der Messlokation übermittelt worden sind.<br/>Hinweis:<br/>Bei „Korrekturenergiemengen“, die auf Ebene der Messlokation übermittelt werden, muss in jedem Fall ein Korrekturgrund mitgegeben werden.|||
||||Stornierung und Neuversand|Ja|Bei der Korrektur von Energiemengen auf Ebene der Marktlokation.|
|Ausfallarbeitsüberführungszeitreihe<br/>(Prüfidentifikator 13020)|Überschreibung von Werten|Nein|Eine Korrektur erfolgt über die Versionierung der Werte. Der Absender ist für die Versionierung der Werte verantwortlich.|||
|Meteorologische Daten<br/>(Prüfidentifikator 13021)|Überschreibung von Werten|Nein|Eine Korrektur erfolgt über die Versionierung der Werte. Der Absender ist für die Versionierung der Werte verantwortlich.|||
|Redispatch 2.0 Einzelzeitreihe Ausfallarbeit<br/>(Prüfidentifikator 13022)|Überschreibung von Werten|Nein|Eine Korrektur erfolgt über die Versionierung der Werte. Der Absender ist für die Versionierung der Werte verantwortlich.|||
|Redispatch 2.0 Ausfallarbeitssummenzeitreihe<br/>(Prüfidentifikator 13023)|Überschreibung von Werten|Nein|Eine Korrektur erfolgt über die Versionierung der Werte. Der Absender ist für die Versionierung der Werte verantwortlich.|||
|Lastgang Marktlokation, Tranche<br/>(Prüfidentifikator) 13025|Überschreibung von Werten|Ja|Eine Korrektur erfolgt über die Versionierung der Werte. Der Absender ist für die Versionierung der Werte verantwortlich.|||
|Redispatch EEG-Überführungszeitreihe aufgrund Ausfallarbeit<br/>(Prüfidentifikator 13026)|Überschreibung von Werten|Nein|Eine Korrektur erfolgt über die Versionierung der Zeitreihen. Der Absender ist für die Versionierung der Zeitreihen verantwortlich.|||
|Werte nach Typ 2<br/>(Prüfidentifikator 13027)|Überschreibung von Werten|Nein|Eine Korrektur erfolgt über die Versionierung der Werte. Der Absender ist für die Versionierung der Werte verantwortlich.|||
|Grundlage POG-Ermittlung<br/>(Prüfidentifikator 13028)|Stornierung und Neuversand|Nein|--|||


Version: 3.1f 30.09.2025 Seite 137 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

## 12.4 Anwendungsübersicht Stornierung

|EDIFACT Struktur|Beschreibung<br/>Prüfidentifikator|Messwert Storno<br/>13006|Bedingung|||
|-|-|-|-|-|-|
|Nutzdaten-Kopfsegment||||||
|UNB|00002||Muss|||
|UNB|0001|UNOC|UN/ECE-Zeichensatz C|X||
|UNB|0002|3|Version 3|X||
|UNB|0004||MP-ID Absender|X||
|UNB|0007|14|GS1|X||
|||500|DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)|X||
|||502|DE, DVGW Service & Consult GmbH|X||
|UNB|0010||MP-ID Empfänger|X||
|UNB|0007|14|GS1|X||
|||500|DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)|X||
|||502|DE, DVGW Service & Consult GmbH|X||
|UNB|0017||Datum der Erstellung|X||
|UNB|0019||Uhrzeit der Erstellung|X||
|UNB|0020||Datenaustauschreferenz|X \[918]|\[918] Format: Zeichen aus dem über UNOC definierten Zeichensatz, wobei von den Buchstaben nur Großbuchstaben erlaubt sind.|
|UNB|0026|EM|Energiemenge|X||
|||VL|Verrechnungsliste, Zählerstand|X||
|Nachrichtenkopfsegment||||||
|UNH|00003||Muss|||
|UNH|0062||Nachrichten-Referenznummer|X||
|UNH|0065|MSCONS|Bericht über den Verbrauch messbarer Dienstleistungen|X||
|UNH|0052|D|Entwurfs-Version|X||
|UNH|0054|04B|Ausgabe 2004 - B|X||
|UNH|0051|UN|UN/CEFACT|X||
|UNH|0057|2.4c|Versionsnummer der zugrundeliegenden BDEW-Nachrichtenbeschreibung|X||
|Beginn der Nachricht||||||
|BGM|00004||Muss|||
|BGM|1001|7|Prozessdatenbericht|X|\[547] Hinweis: Der Code 270 ist nur zu nutzen, wenn ein Lieferschein, der vor dem 1.4.2021 erstellt wurde, storniert wird.|
|||270|Lieferschein|X \[547]||
|||Z27|Bewegungsdaten im Kalenderjahr vor Lieferbeginn|X||
|||Z28|Energiemenge und Leistungsmaximum|X||
|||Z41|Lieferschein Grund- / Arbeitspreis|X||
|||Z42|Lieferschein Arbeits- / Leistungspreis|X||
|||Z85|Grundlage POG-Ermittlung|X||
|BGM|1004||Dokumentennummer|X||
|BGM|1225|1|Storno|X||
|Nachrichtendatum||||||
|DTM|00005||Muss|||
|DTM|2005|137|Dokumenten-/Nachrichtendatum/-zeit|X||


Version: 3.1f	30.09.2025	Seite 138 von 158

MSCONS Anwendungshandbuch
![edi@energy. Datenformate Strom & Gas](image)

|EDIFACT Struktur|Beschreibung<br/>Prüfidentifikator|Messwert Storno<br/>13006|Bedingung||||
|-|-|-|-|-|-|-|
|DTM|2380||Datum oder Uhrzeit oder Zeitspanne, Wert|X \[931] \[494]|\[494] Das hier genannte Datum muss der Zeitpunkt sein, zu dem das Dokument erstellt wurde, oder ein Zeitpunkt, der davor liegt.<br/>\[931] Format: ZZZ = +00||
|DTM|2379||303|CCYYMMDDHHMMZZZ|X||
|Referenzangaben|||||||
|SG1||||Muss|||
|SG1|RFF||00006||Muss||
|SG1|RFF|1153|ACW|Referenznummer einer vorangegangenen Nachricht|X||
|SG1|RFF|1154||Referenznummer|X \[532]|\[532] Hinweis: Wert aus BGM+7/Z27/Z28/270/Z41/Z42/Z85 DE1004 der MSCONS Nachricht, die storniert wird|
|Prüfidentifikator|||||||
|SG1||||Muss|||
|SG1|RFF||00009||Muss||
|SG1|RFF|1153|Z13|Prüfidentifikator|X||
|SG1|RFF|1154|13006|Messw. Storno|X||
|MP-ID Absender|||||||
|SG2||||Muss|||
|SG2|NAD||00010||Muss||
|SG2|NAD|3035|MS|Dokumenten-/Nachrichtenaussteller bzw. -absender|X||
|SG2|NAD|3039||MP-ID|X||
|SG2|NAD|3055|9|GS1|X||
|||293|DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)|X|||
|||332|DE, DVGW Service & Consult GmbH|X|||
|Ansprechpartner|||||||
|SG4||||Kann|||
|SG4|CTA||00011||Muss||
|SG4|CTA|3139|IC|Informationsstelle|X||
|SG4|CTA|3412||Abteilung oder Bearbeiter|X||
|Kommunikationsverbindung|||||||
|SG4|||||||
|SG4|COM||00012||Muss||
|SG4|COM|3148||Kommunikationsadresse, Identifikation|X ((\[939] \[142]) ∨ (\[940] \[143])) ∧ \[576]|\[142] wenn im DE3155 in demselben COM der Code EM vorhanden ist<br/>\[143] wenn im DE3155 in demselben COM der Code TE / FX / AJ / AL vorhanden ist<br/>\[576] Hinweis: Es darf nur eine Information im DE3148 übermittelt werden<br/>\[939] Format: Die Zeichenkette muss die Zeichen @ und . enthalten<br/>\[940] Format: Die Zeichenkette muss mit dem Zeichen + beginnen und danach dürfen nur noch Ziffern folgen|
|SG4|COM|3155|TE|Telefon|X \[1P0..1]||
|||EM|E-Mail|X \[1P0..1]|||
|||AJ|weiteres Telefon|X \[1P0..1]|||
|||AL|Handy|X \[1P0..1]|||
|||FX|Telefax|X \[1P0..1]|||
|MP-ID Empfänger|||||||
|SG2||||Muss|||
|SG2|NAD||00013||Muss||
|SG2|NAD|3035|MR|Nachrichtenempfänger|X||


Version: 3.1f 30.09.2025 Seite 139 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|EDIFACT Struktur|Beschreibung<br/>Prüfidentifikator|Messwert Storno<br/>13006|Bedingung||||
|-|-|-|-|-|-|-|
|SG2|NAD|3039|MP-ID|X|||
|SG2|NAD|3055|9|GS1|X||
|SG2|NAD|3055|293|DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)|X||
|SG2|NAD|3055|332|DE, DVGW Service & Consult GmbH|X||
|Abschnitts-Kontrollsegment|||Muss||||
|UNS||00014||Muss|||
|UNS|0081||D|Trennung von Kopf- und Positionsteil|X||
|Name und Adresse|||Muss \[2001]|\[2001] Segmentgruppe ist nur einmal je UNH anzugeben|||
|SG5||||Muss \[2001]|||
|SG5|NAD||00015||Muss||
|SG5|NAD|3035|DP|Lieferanschrift|X||
|Identifikationsangabe|||Muss||||
|SG6||||Muss|||
|SG6|LOC||00017||Muss||
|SG6|LOC|3227|172|Meldepunkt|X||
|Nachrichten-Endesegment|||Muss||||
|UNT||00041||Muss|||
|UNT|0074||Anzahl der Segmente in einer Nachricht|X|||
|UNT|0062||Nachrichten-Referenznummer|X|||
|Nutzdaten-Endesegment|||Muss||||
|UNZ||00042||Muss|||
|UNZ|0036||Datenaustauschzähler|X|||
|UNZ|0020||Datenaustauschreferenz|X|||


Version: 3.1f	30.09.2025	Seite 140 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

# 13 Übersicht Ereignisse für die Wertbereitstellung und Inhalte bei der Übertragung von Zählerständen

Dieses Kapitel gibt einen Überblick über die verschiedenen Ereignisse gemäß WiM Teil 2 – Fokus Übermittlung von Werten, Kapitel 2.5.5. für die eine Bereitstellung von Werten erfolgt. In den Unterkapiteln wird jeweils zu den Ereignissen:

* in der ersten Tabelle der Auslöser für die Wertbereitstellung beschrieben,
* in der zweiten Tabelle die Inhalte der Nachricht (relevante Auszüge) und
* in der dritten Tabelle die Zuordnung der Nachricht beim Empfänger beschrieben.

Die Tabellen in den Unterkapiteln bauen für das jeweilige Ereignis innerhalb eines Kapitels aufeinander auf, das bedeutet, dass die jeweiligen laufenden Nummern, die in den Tabellen genannt sind, zusammengehören und die Kommunikation gesamthaft betrachtet wird.

## 13.1 Ereignis aufgrund einer Bestellung

In diesem Kapitel wird tabellarisch dargestellt, wie die Kommunikation aufgrund einer Bestellung erfolgt:

### Kommunikation / Aktion welche die Kommunikation der Werte auslöst

|lfd. Nr.|WiM Teil 2 – Fokus Übermittlung von Werten, Kapitel 2.5.5. Darstellung der zu übermittelnden Werte (Tabelle)|Bestellung von³|Ereignis|
|-|-|-|-|
|1|Liefer-beginn/ Neuanlage/ Beginn der Ersatz-/ Grundversorgung/ Herstellung einer 100% LF-Zuordnung zu einer erzeugenden Marktlokation|NB an MSB Marktlokation<br/>falls erforderlich:<br/>MSB an der Marktlokation an MSB an der Messlokation|Bestellung erfolgt im Rahmen des UC Einrichtung der Konfigurationen aufgrund einer Zuordnung eines LF zu einer Marktlokation bzw. Tranche<br/>Bestellung mit ORDERS BGM+Z92 (Einrichtung Konfiguration aufgrund Zuordnung LF|


³ Der NB / LF bestellt den Wert beim MSB an der Marktlokation. Stellt der MSB an der Marktlokation fest, dass für die Ermittlung des Wertes der Marktlokation Werte von Messlokationen notwendig sind, bei denen er nicht der MSB an der Messlokation ist, hat er ebenfalls eine Bestellung ggü. den abweichenden MSB an der Messlokation durchzuführen.

Version: 3.1f	30.09.2025	Seite 141 von 158

MSCONS Anwendungshandbuch
![edi@energy Datenformate Strom & Gas](image)

|lfd. Nr.|WiM Teil 2 – Fokus Übermittlung von Werten, Kapitel 2.5.5. Darstellung der zu übermittelnden Werte (Tabelle)|Bestellung von³|Ereignis|
|-|-|-|-|
|2|Lieferende / Anfrage zur Beendigung der Zuordnung des LFA zur Marktlokation bzw. Tranche|NB an MSB Marktlokation<br/>falls erforderlich:<br/>MSB an der Marktlokation an MSB an der Messlokation|Bestellung erfolgt im Rahmen des UC Einrichtung der Konfigurationen aufgrund einer Zuordnung eines LF zu einer Marktlokation bzw. Tranche<br/>Bestellung mit ORDERS BGM+Z92 (Einrichtung Konfiguration aufgrund Zuordnung LF|
|3|Zwischenablesung|NB/LF/ an MSB Marktlokation<br/>falls erforderlich:<br/>MSB an der Marktlokation an MSB an der Messlokation|Bestellung ORDERS BGM+7, IMD+Z13, IMD+Z49 (Zwischenablesung)|


### Inhalte bei der Übertragung von Zählerständen

#### Inhalte der Nachricht (relevante Auszüge)

|lfd. Nr.|WiM Teil 2 – Fokus Übermittlung von Werten, Kapitel 2.5.5. Darstellung der zu übermittelnden Werte (Tabelle)|Kommunikation des Wertes von⁴|Referenz SG1 RFF+AGI⁵|Ablesedatum (SG10 DTM+9)|Nutzungszeitpunkt (SG10 DTM+7)|Ausführungs- / Änderungszeitpunkt (SG10 DTM+60)|
|-|-|-|-|-|-|-|
|1|Liefer-beginn/ Neuanlage/ Beginn der Ersatz-/ Grundversorgung/ Herstellung einer 100% LF-Zuordnung zu einer erzeugenden Marktlokation|falls erforderlich: MSB der Messlokation an MSB der Marktlokation<br/><br/>MSB der Marktlokation an NB/LF|--|bei wahrem Wert (QTY+220) und wenn ein Ablesedatum vorliegt als Tagesangabe oder Zeitpunktangabe|Zeitpunkt aus der ORDERS DTM+203 (Ausführungsdatum)|--|
|2|Lieferende / Anfrage zur Beendigung der Zuordnung des LFA zur Marktlokation bzw. Tranche|falls erforderlich: MSB der Messlokation an MSB der Marktlokation|--|bei wahrem Wert (QTY+220) und wenn ein Ablesedatum vorliegt als Tagesangabe oder Zeitpunktangabe|Zeitpunkt aus der ORDERS DTM+203 (Ausführungsdatum)|--|


⁴ Der MSB der Messlokation übermittelt die Werte an den MSB an der Marktlokation, sofern diese voneinander abweichen. Der MSB an der Marktlokation übermittelt die Werte an den NB / LF.

⁵ wenn der Wert an den ursprünglichen Besteller übermittelt wird.

Version: 3.1f 30.09.2025 Seite 142 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|lfd. Nr.|WiM Teil 2 – Fokus Übermittlung von Werten, Kapitel 2.5.5. Darstellung der zu übermittelnden Werte (Tabelle)|Kommunikation des Wertes von|Referenz SG1 RFF+AGI|Ablesedatum (SG10 DTM+9)|Nutzungszeitpunkt (SG10 DTM+7)|Ausführungs- / Änderungszeitpunkt (SG10 DTM+60)|||||||
|-|-|-|-|-|-|-|-|-|-|-|-|-|
|||MSB der Marktlokation an NB/LF|||||||||||
|||3|||||Zwischenablesung|falls erforderlich: MSB der Messlokation an MSB der Marktlokation<br/><br/>MSB der Marktlokation an NB/LF|Wert aus BGM+7 DE1004 der ORDERS mit der die Anforderung von Werten erfolgt ist|bei wahrem Wert (QTY+220) und wenn ein Ablesedatum vorliegt als Tagesangabe oder Zeitpunktangabe|Zeitpunkt aus der ORDERS (SG29 DTM+7)|--|


## Verarbeitung beim Empfänger des Wertes

### Verarbeitung beim Empfänger des Wertes LF / NB / MSB

|lfd. Nr.|WiM Teil 2 – Fokus Übermittlung von Werten, Kapitel 2.5.5. Darstellung der zu übermittelnden Werte (Tabelle)|Empfänger ist Besteller (NB/LF/MSB)|Empfänger ist berechtigte Marktrolle (NB/LF/MSB)|Auslöser für die Bereitstellung von Mengen an der Marktlokation?|
|-|-|-|-|-|
|1|Liefer-beginn/ Neuanlage/ Beginn der Ersatz-/ Grundversorgung/ Herstellung einer 100% LF-Zuordnung zu einer erzeugenden Marktlokation|--|Die Zuordnung des Wertes zu einem Ereignis ergibt sich beim Empfänger aufgrund einer Änderung der Stammdaten durch den Verantwortlichen NB (Stammdatenänderung UTILMD BGM+E03, STS+7++ZX6 (Änderung Daten der MaLo)).<br/><br/>Hinweis:<br/>Ist der Empfänger der LF für den die Zuordnung beginnt, erfolgt die Zuordnung des Wertes aufgrund:<br/>einer Bestätigung einer Anmeldung (UTILMD BGM+E01).|--|
|2|Lieferende / Anfrage zur Beendigung der Zuordnung des LFA zur Marktlokation bzw. Tranche|--|Die Zuordnung des Wertes zu einem Ereignis ergibt sich beim Empfänger aufgrund einer Änderung der Stammdaten durch den Verantwortlichen NB (Stammdatenänderung UTILMD BGM+E03, STS+7++ZX6 (Änderung Daten der MaLo)).<br/><br/>Hinweis: Ist der Empfänger der LF für den die Zuordnung endet, erfolgt die Zuordnung des Wertes aufgrund:<br/>Bestätigung Abmeldung (UTILMD BGM+E02) bzw. Beendigung Zuordnung (UTILMD BGM+E02).|ja, Bereitstellung von Werten auf Ebene der Marktlokation|


Version: 3.1f 30.09.2025 Seite 143 von 158

MSCONS Anwendungshandbuch
![edi@energy Logo](image)

|lfd. Nr.|WiM Teil 2 – Fokus Übermittlung von Werten, Kapitel 2.5.5. Darstellung der zu übermittelnden Werte (Tabelle)|Empfänger ist Besteller (NB/LF/MSB)|Empfänger ist berechtigte Marktrolle (NB/LF/MSB)|Auslöser für die Bereitstellung von Mengen an der Marktlokation?|
|-|-|-|-|-|
|3|Zwischenablesung|Auf Basis der Referenzangabe in der Messwertübermittlung (Referenz auf die ORDERS)|Die Zuordnung des Wertes erfolgt anhand des Zuordnungstupels zum angegebenen Objekt ohne Bezug zu einem Ereignis|--|


## 13.2 Ereignis aufgrund der Bereitstellung durch den MSB

In diesem Kapitel wird tabellarisch dargestellt, wie die Kommunikation aufgrund der Bereitstellung durch den MSB erfolgt:

### Kommunikation / Aktion welche die Kommunikation der Werte auslöst

|lfd. Nr.|WiM Teil 2 – Fokus Übermittlung von Werten, Kapitel 2.5.5. Darstellung der zu übermittelnden Werte (Tabelle)|Ereignis|
|-|-|-|
|4|Turnusmäßige/ regelmäßige Ablesung|Auf Basis der bisher ausgetauschten Stammdaten bzw. bei Änderung auf Basis:<br/>Stammdatenänderung des MSB UTILMD BGM+E03, STS+7++ZX6 (Änderung Daten der MaLo), RFF+Z50 (Termindaten der Marktlokation) und der damit einhergehenden Verpflichtung des MSB|


### Inhalte bei der Übertragung von Zählerständen

Inhalte der Nachricht (relevante Auszüge)

|lfd. Nr.|WiM Teil 2 – Fokus Übermittlung von Werten, Kapitel 2.5.5. Darstellung der zu übermittelnden Werte (Tabelle)|Kommunikation des Wertes von⁶|Referenz SG1 RFF+AGI|Ablesedatum (SG10 DTM+9)|Nutzungszeitpunkt (SG10 DTM+7)|Ausführungs- / Änderungszeitpunkt (SG10 DTM+60)|
|-|-|-|-|-|-|-|
|4|Turnusmäßige/ regelmäßige Ablesung|falls erforderlich: MSB der Messlokation an MSB der Marklokation|--|bei wahrem Wert (QTY+220) und wenn|Zeitpunkt zu dem der Messwert zu nutzen ist|--|


⁶ Der MSB der Messlokation übermittelt die Werte an den MSB an der Marktlokation, sofern diese voneinander abweichen. Der MSB an der Marktlokation übermittelt die Werte an den NB / LF.

Version: 3.1f 30.09.2025 Seite 144 von 158

MSCONS Anwendungshandbuch
![edi@energy Datenformate Strom & Gas](image)

|lfd. Nr.|WiM Teil 2 – Fokus Übermittlung von Werten, Kapitel 2.5.5. Darstellung der zu übermittelnden Werte (Tabelle)|Kommunikation des Wertes von⁶|Referenz SG1 RFF+AGI|Ablesedatum (SG10 DTM+9)|Nutzungszeitpunkt (SG10 DTM+7)|Ausführungs- / Änderungszeitpunkt (SG10 DTM+60)|
|-|-|-|-|-|-|-|
|||MSB der Marktlokation an NB/LF||ein Ablesedatum vorliegt als Tagesangabe oder Zeitpunktangabe|Hinweis: Muss einem Zeitpunkt aus "Turnusablesung des MSB und Wertegranularität“ entsprechen.||


### Verarbeitung beim Empfänger des Wertes

#### Verarbeitung beim Empfänger des Wertes LF / NB / MSB

|lfd. Nr.|WiM Teil 2 – Fokus Übermittlung von Werten, Kapitel 2.5.5. Darstellung der zu übermittelnden Werte (Tabelle)|Empfänger ist berechtigte Marktrolle (NB/LF/MSB)|Auslöser für die Bereitstellung von Mengen an der Marktlokation?|
|-|-|-|-|
|4|Turnusmäßige/ regelmäßige Ablesung|Die Zuordnung des Wertes zu einem Ereignis beim Empfänger ergibt sich aus dem ausgetauschten Stammdatum „Turnusablesung des MSB und Wertegranularität“.|ja, Bereitstellung von Werten auf Ebene der Marktlokation|


### 13.3 Ereignis aufgrund einer Änderung der Konfiguration

In diesem Kapitel wird tabellarisch dargestellt, wie die Kommunikation aufgrund einer Änderung der Konfiguration erfolgt:

#### Kommunikation / Aktion welche die Kommunikation der Werte auslöst

|lfd. Nr.|WiM Teil 2 – Fokus Übermittlung von Werten, Kapitel 2.5.5. Darstellung der zu übermittelnden Werte (Tabelle)|Ereignis|
|-|-|-|
|5|Änderung der Konfiguration<br/>(Wert zum \*\*Beginn\*\* der neuen Konfiguration)|Änderung der Konfiguration ist durchgeführt<br/>und:<br/>Stammdatenänderung des MSB UTILMD BGM+E03, STS+7++ZX7 (Änderung Daten der MeLo) versendet.|
|6|Änderung der Konfiguration|Änderung der Konfiguration ist durchgeführt<br/>und:|


Version: 3.1f 30.09.2025 Seite 145 von 158

MSCONS Anwendungshandbuch
![edi@energy Datenformate Strom & Gas](image)

|lfd. Nr.|WiM Teil 2 – Fokus Übermittlung von Werten, Kapitel 2.5.5. Darstellung der zu übermittelnden Werte (Tabelle)|Ereignis|
|-|-|-|
||(Wert zum Ende der bisherigen Konfiguration)|Stammdatenänderung des MSB UTILMD BGM+E03, STS+7++ZX7<br/>(Änderung Daten der MeLo) versendet.|


### Inhalte bei der Übertragung von Zählerständen

#### Inhalte der Nachricht (relevante Auszüge)

|lfd. Nr.|WiM Teil 2 – Fokus Übermittlung von Werten, Kapitel 2.5.5. Darstellung der zu übermittelnden Werte (Tabelle)|Kommunikation des Wertes von|Referenz SG1 RFF+AGI|Ablesedatum (SG10 DTM+9)|Nutzungszeitpunkt (SG10 DTM+7)|Ausführungs- / Änderungszeitpunkt (SG10 DTM+60)|
|-|-|-|-|-|-|-|
|5|Änderung der Konfiguration<br/>(Wert zum Beginn der neuen Konfiguration)|falls erforderlich: MSB der Messlokation an MSB der Marklokation<br/><br/>MSB der Marktlokation an NB/LF|--|--|Zeitpunkt aus der UTLMD (SG6 DTM+Z25) ab dem die geänderten Stammdaten zu verwenden sind|Zeitpunkt zu dem die Änderung der Konfiguration tatsächlich stattgefunden hat|
|6|Änderung der Konfiguration<br/>(Wert zum Ende der bisherigen Konfiguration)|falls erforderlich: MSB der Messlokation an MSB der Marklokation<br/><br/>MSB der Marktlokation an NB/LF|--|--|Zeitpunkt aus der UTLMD (SG6 DTM+Z25) ab dem die geänderten Stammdaten zu verwenden sind|Zeitpunkt zu dem die Änderung der Konfiguration tatsächlich stattgefunden hat|


### Verarbeitung beim Empfänger des Wertes

#### Verarbeitung beim Empfänger des Wertes LF / NB / MSB

***

<sup>7</sup> Der MSB der Messlokation übermittelt die Werte an den MSB an der Marktlokation, sofern diese voneinander abweichen. Der MSB an der Marktlokation übermittelt die Werte an den NB / LF.

Version: 3.1f	30.09.2025	Seite 146 von 158

MSCONS Anwendungshandbuch
![edi@energy Datenformate Strom & Gas](image)

|lfd. Nr.|WiM Teil 2 – Fokus Übermittlung von Werten, Kapitel 2.5.5. Darstellung der zu übermittelnden Werte (Tabelle)|Empfänger ist berechtigte Marktrolle (NB/LF/MSB)|Auslöser für die Bereitstellung von Mengen an der Marktlokation?|
|-|-|-|-|
|5|Änderung der Konfiguration<br/>(Wert zum \*\*Beginn\*\* der neuen Konfiguration)|Die Zuordnung des Wertes zu einem Ereignis ergibt sich beim Empfänger aufgrund einer Änderung der Stammdaten durch den Verantwortlichen MSB (Stammdatenänderung UTILMD BGM+E03, STS+7++ZX7 (Änderung Daten der MeLo)).|--|
|6|Änderung der Konfiguration<br/>(Wert zum \*\*Ende\*\* der bisherigen Konfiguration)|Die Zuordnung des Wertes zu einem Ereignis ergibt sich beim Empfänger aufgrund einer Änderung der Stammdaten durch den Verantwortlichen MSB (Stammdatenänderung UTILMD BGM+E03, STS+7++ZX7 (Änderung Daten der MeLo)).|ja, Bereitstellung von Werten auf Ebene der Marktlokation|


## 13.4 Ereignis aufgrund eines Gerätewechsels

In diesem Kapitel wird tabellarisch dargestellt, wie die Kommunikation aufgrund eines Gerätewechsels erfolgt:

### Kommunikation / Aktion welche die Kommunikation der Werte auslöst

|lfd. Nr.|WiM Teil 2 – Fokus Übermittlung von Werten, Kapitel 2.5.5. Darstellung der zu übermittelnden Werte (Tabelle)|Ereignis|
|-|-|-|
|7|Gerätewechsel<br/>(Wert des eingebauten Gerätes)<br/><br/>Hinweis: Auslöser des Gerätewechsels kann auch ein MSB-Wechsel sein.|Gerätewechsel ist durchgeführt<br/>und:<br/>Stammdatenänderung UTILMD des MSB BGM+E03, STS+7++ZX7 (Änderung Daten der MeLo) versendet|
|8|Gerätewechsel<br/>(Wert des ausgebauten Gerätes)<br/><br/>Hinweis: Auslöser des Gerätewechsels kann auch ein MSB-Wechsel sein.|Gerätewechsel ist durchgeführt<br/>und:<br/>Stammdatenänderung UTILMD des MSB BGM+E03, STS+7++ZX7 (Änderung Daten der MeLo) versendet|


### Inhalte bei der Übertragung von Zählerständen

Version: 3.1f
30.09.2025
Seite 147 von 158

MSCONS Anwendungshandbuch
![edi@energy Datenformate Strom & Gas](image)

## Inhalte der Nachricht (relevante Auszüge)

|lfd. Nr.|WiM Teil 2 – Fokus Übermittlung von Werten, Kapitel 2.5.5. Darstellung der zu übermittelnden Werte (Tabelle)|Kommunikation des Wertes von|Referenz SG1 RFF+AGI|Ablesedatum (SG10 DTM+9)|Nutzungszeitpunkt (SG10 DTM+7)|Ausführungs- / Änderungszeitpunkt (SG10 DTM+60)|
|-|-|-|-|-|-|-|
|7|Gerätewechsel<br/>(Wert des eingebauten Gerätes)<br/><br/>Hinweis: Auslöser des Gerätewechsels kann auch ein MSB-Wechsel sein.|falls erforderlich: MSB der Messlokation an MSB der Marklokation<br/><br/>MSB der Marktlokation an NB/LF|--|--|Zeitpunkt aus der UTILMD (SG6 DTM+Z25) ab dem die geänderten Stammdaten zu verwenden sind|Zeitpunkt zu dem der Einbau des Gerätes tatsächlich stattgefunden hat.|
|8|Gerätewechsel<br/>(Wert des ausgebauten Gerätes)<br/><br/>Hinweis: Auslöser des Gerätewechsels kann auch ein MSB-Wechsel sein.|falls erforderlich: MSB der Messlokation an MSB der Marklokation<br/><br/>MSB der Marktlokation an NB/LF|--|--|Zeitpunkt aus der UTILMD (SG6 DTM+Z25) ab dem die geänderten Stammdaten zu verwenden sind|Zeitpunkt zu dem der Ausbau des Gerätes tatsächlich stattgefunden hat.|


## Verarbeitung beim Empfänger des Wertes

### Verarbeitung beim Empfänger des Wertes LF / NB / MSB

|lfd. Nr.|WiM Teil 2 – Fokus Übermittlung von Werten, Kapitel 2.5.5. Darstellung der zu übermittelnden Werte (Tabelle)|Empfänger ist berechtigte Marktrolle (NB/LF/MSB)|Auslöser für die Bereitstellung von Mengen an der Marktlokation?|
|-|-|-|-|
|7|Gerätewechsel<br/>(Wert des eingebauten Gerätes)|Die Zuordnung des Wertes zu einem Ereignis ergibt sich beim Empfänger aufgrund einer Änderung der Stammdaten durch den Verantwortlichen MSB (Stammdatenänderung UTILMD BGM+E03, STS+7++ZX7 (Änderung Daten der MeLo)).|--|
|8|Gerätewechsel<br/>(Wert des ausgebauten Gerätes)|Die Zuordnung des Wertes zu einem Ereignis ergibt sich beim Empfänger aufgrund einer Änderung der Stammdaten durch den Verantwortlichen MSB|ja, Bereitstellung von Werten auf Ebene der Marktlokation|


***

<sup>8</sup> Der MSB der Messlokation übermittelt die Werte an den MSB an der Marktlokation, sofern diese voneinander abweichen. Der MSB an der Marktlokation übermittelt die Werte an den NB / LF.

Version: 3.1f	30.09.2025	Seite 148 von 158

MSCONS Anwendungshandbuch
![edi@energy Logo](image)

|lfd. Nr.|WiM Teil 2 – Fokus Übermittlung von Werten, Kapitel 2.5.5. Darstellung der zu übermittelnden Werte (Tabelle)|Empfänger ist berechtigte Marktrolle (NB/LF/MSB)|Auslöser für die Bereitstellung von Mengen an der Marktlokation?|
|-|-|-|-|
|||(Stammdatenänderung UTILMD BGM+E03, STS+7++ZX7 (Änderung Daten der MeLo)).||


### 13.5 Ereignis aufgrund einer Geräteübernahme

In diesem Kapitel wird tabellarisch dargestellt, wie die Kommunikation aufgrund einer Geräteübernahme erfolgt:

#### Kommunikation / Aktion welche die Kommunikation der Werte auslöst

|lfd. Nr.|WiM Teil 2 – Fokus Übermittlung von Werten, Kapitel 2.5.5. Darstellung der zu übermittelnden Werte (Tabelle)|Ereignis|
|-|-|-|
|9|Geräteübernahme<br/>(Verteilung der Werte durch den MSBN, da seine Zuordnung zur Lokation beginnt, Wert zum Beginn Zeitpunkt der Zuordnung)<br/><br/>Hinweis: Auslöser der Geräteübernahme ist ein MSB-Wechsel.|MSB-Wechsel erfolgreich durchgeführt<br/>und:<br/>IFTSTA BGM+Z09 SG15 STS+Z10+Z14 zu dem der MSB-Wechsel vollzogen wurde, liegt vor.|
|10|Geräteübernahme<br/>(Verteilung der Werte durch den MSBA, da seine Zuordnung zur Lokation endet, Wert zum Ende Zeitpunkt der Zuordnung))<br/><br/>Hinweis: Auslöser der Geräteübernahme ist ein MSB-Wechsel.|MSB-Wechsel erfolgreich durchgeführt<br/>und:<br/>IFTSTA BGM+Z09 SG15 STS+Z10+Z14 zu dem der MSB-Wechsel vollzogen wurde, liegt vor.|


#### Inhalte bei der Übertragung von Zählerständen

Inhalte der Nachricht (relevante Auszüge)

Version: 3.1f
30.09.2025
Seite 149 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|lfd. Nr.|WiM Teil 2 – Fokus Übermittlung von Werten, Kapitel 2.5.5. Darstellung der zu übermittelnden Werte (Tabelle)|Kommunikation des Wertes von⁹|Referenz SG1 RFF+AGI|Ablesedatum (SG10 DTM+9)|Nutzungszeitpunkt (SG10 DTM+7)|Ausführungs- / Änderungszeitpunkt (SG10 DTM+60)|
|-|-|-|-|-|-|-|
|9|Geräteübernahme<br/>(Verteilung der Werte durch den MSBN, da seine Zuordnung zur Lokation beginnt, Wert zum Beginn Zeitpunkt der Zuordnung)<br/><br/>Hinweis: Auslöser der Geräteübernahme ist ein MSB-Wechsel.|falls erforderlich: MSB der Messlokation an MSB der Marktlokation<br/><br/>MSB der Marktlokation an NB/LF|--|bei wahrem Wert (QTY+220) und wenn ein Ablesedatum vorliegt als Tagesangabe oder Zeitpunktangabe|Zeitpunkt (SG15 DTM+293) aus der IFTSTA BGM+Z09 SG15 STS+Z10+Z14 zu dem der MSB-Wechsel vollzogen wurde.|--|
|10|Geräteübernahme<br/>(Verteilung der Werte durch den MSBA, da seine Zuordnung zur Lokation endet, Wert zum Ende Zeitpunkt der Zuordnung))<br/><br/>Hinweis: Auslöser der Geräteübernahme ist ein MSB-Wechsel.|falls erforderlich: MSB der Messlokation an MSB der Marktlokation<br/><br/>MSB der Marktlokation an NB/LF|--|bei wahrem Wert (QTY+220) und wenn ein Ablesedatum vorliegt als Tagesangabe oder Zeitpunktangabe|Zeitpunkt (SG15 DTM+293) aus der IFTSTA BGM+Z09 SG15 STS+Z10+Z14 zu dem der MSB-Wechsel vollzogen wurde. .|--|


## Verarbeitung beim Empfänger des Wertes

### Verarbeitung beim Empfänger des Wertes LF / NB / MSB

|lfd. Nr.|WiM Teil 2 – Fokus Übermittlung von Werten, Kapitel 2.5.5. Darstellung der zu übermittelnden Werte (Tabelle)|Empfänger ist berechtigte Marktrolle (NB/LF/MSB)|Auslöser für die Bereitstellung von Mengen an der Marktlokation?|
|-|-|-|-|
|9|Geräteübernahme|Die Zuordnung des Wertes zu einem Ereignis ergibt sich beim Empfänger aufgrund einer Änderung der|--|


⁹ Der MSB der Messlokation übermittelt die Werte an den MSB an der Marktlokation, sofern diese voneinander abweichen. Der MSB an der Marktlokation übermittelt die Werte an den NB / LF.

Version: 3.1f 30.09.2025 Seite 150 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|lfd. Nr.|WiM Teil 2 – Fokus Übermittlung von Werten, Kapitel 2.5.5. Darstellung der zu übermittelnden Werte (Tabelle)|Empfänger ist berechtigte Marktrolle (NB/LF/MSB)|Auslöser für die Bereitstellung von Mengen an der Marktlokation?|
|-|-|-|-|
||(Verteilung der Werte durch den MSBN, da seine Zuordnung zur Lokation beginnt, Wert zum Beginn Zeitpunkt der Zuordnung)<br/><br/>Hinweis: Auslöser der Geräteübernahme ist ein MSB-Wechsel.|Stammdaten durch den NB (UTILMD BGM+E03, STS+7++ZX7 (Änderung Daten der MeLo).||
|10|Geräteübernahme<br/>(Verteilung der Werte durch den MSBA, da seine Zuordnung zur Lokation endet, Wert zum Ende Zeitpunkt der Zuordnung))<br/><br/>Hinweis: Auslöser der Geräteübernahme ist ein MSB-Wechsel.|Die Zuordnung des Wertes zu einem Ereignis ergibt sich beim Empfänger aufgrund einer Änderung der Stammdaten durch den NB (UTILMD BGM+E03, STS+7++ZX7 (Änderung Daten der MeLo)).|ja, Bereitstellung von Werten auf Ebene der Marktlokation|


## 13.6 Bereitstellung Werte durch NB / LF an den MSB an der Marktlokation

In diesem Kapitel wird tabellarisch dargestellt, wie die Kommunikation aufgrund einer Bereitstellung von Werten durch den NB / LF an den MSB an der Marktlokation erfolgt:

### Kommunikation / Aktion welche die Kommunikation der Werte auslöst

|lfd. Nr.|Ereignis|Ereignis|
|-|-|-|
|11|Wert<br/><br/>Hinweis: nur bei kME ohne RLM, mME|Wert liegt beim NB / LF vor und soll dem MSB zur Verfügung gestellt werden|


### Inhalte bei der Übertragung von Zählerständen

#### Inhalte der Nachricht (relevante Auszüge)

Version: 3.1f 30.09.2025 Seite 151 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

|lfd. Nr.|Ereignis|Kommunikation des Wertes von|ReferenzSG1 RFF+AGI|Ablesedatum(SG10 DTM+9)|Nutzungszeitpunkt(SG10 DTM+7)|Ausführungs- /Änderungszeitpunkt(SG10 DTM+60)|
|-|-|-|-|-|-|-|
|11|Wert<br/><br/>Hinweis: nur bei kME ohne RLM, mME|NB / LF an MSB an der Marktlokation|--|bei wahrem Wert (QTY+220) und wenn ein Ablesedatum vorliegt als Tagesangabe oder Zeitpunktangabe|Zeitpunkt zu dem der Messwert genutzt werden *soll*<br/><br/>Hinweis:<br/>bei dem angegebenen Nutzungszeitpunkt handelt es sich um einen Vorschlag des Absenders. Gültigkeit hat ausschließlich der Nutzungszeitpunkt, welcher durch den MSB verwendet wird. Die Bereitstellung erfolgt ggf. danach durch den MSB.|--|


### <mark>Verarbeitung beim Empfänger des Wertes</mark>

#### Verarbeitung beim Empfänger des Wertes LF / NB / MSB

|lfd. Nr.|Ereignis|Empfänger ist berechtigte Marktrolle (NB/LF/MSB)|Auslöser für die Bereitstellungvon Mengenan der Marktlokation?|
|-|-|-|-|
|11|Wert<br/><br/>Hinweis: nur bei kME ohne RLM, mME|Die Zuordnung des Wertes erfolgt anhand des Zuordnungstupels zum angegebenen Objekt ohne Bezug zu einem Ereignis, sofern dieser Plausibel ist.|--|


### 13.7 Ereignis aufgrund einer erforderlichen Abgrenzung

In diesem Kapitel wird tabellarisch dargestellt, wie die Kommunikation aufgrund einer erforderlichen Abgrenzung erfolgt:

#### <mark>Kommunikation / Aktion welche die Kommunikation der Werte auslöst</mark>

Version: 3.1f 30.09.2025 Seite 152 von 158

MSCONS Anwendungshandbuch
![edi@energy Logo](image)

|lfd. Nr.|Ereignis|Bestellung von|Ereignis|
|-|-|-|-|
|12|Abgrenzung<br/><br/>Hinweis: vorgelagert ist eine Bestellung einer Abgrenzungsmenge durch den NB an den MSB an der Marktlokation.|MSB an der Marktlokation an MSB an der Messlokation|Bestellung ORDERS BGM+7, IMD+Z13, IMD+Z47 (Abgrenzung)|


## Inhalte bei der Übertragung von Zählerständen

### Inhalte der Nachricht (relevante Auszüge)

|lfd. Nr.|Ereignis|Kommunikation des Wertes von|Referenz SG1 RFF+AGI|Ablesedatum (SG10 DTM+9)|Nutzungszeitpunkt (SG10 DTM+7)|Ausführungs- / Änderungszeitpunkt (SG10 DTM+60)|
|-|-|-|-|-|-|-|
|12|Abgrenzung<br/><br/>Hinweis: vorgelagert ist eine Bestellung einer Abgrenzungsmenge durch den NB an den MSB an der Marktlokation.|MSB an der Messlokation an MSB an der Marktlokation|Wert aus BGM+7 DE1004 der ORDERS mit der die Anforderung von Werten erfolgt ist|bei wahrem Wert (QTY+220) und wenn ein Ablesedatum vorliegt als Tagesangabe oder Zeitpunktangabe|Zeitpunkt aus der ORDERS (SG29 DTM+7)|--|


## Verarbeitung beim Empfänger des Wertes

### Verarbeitung beim Empfänger des Wertes LF / NB / MSB

|lfd. Nr.|Ereignis|Empfänger ist Besteller (NB/LF/MSB)|Empfänger ist berechtigte Marktrolle (NB/LF/MSB)|Auslöser für die Bereitstellung von Mengen an der Marktlokation?|
|-|-|-|-|-|
|12|Abgrenzung<br/><br/>Hinweis: vorgelagert ist eine Bestellung einer Abgrenzungsmenge durch den NB an den MSB an der Marktlokation.|Auf Basis der Referenzangabe in der Messwertübermittlung (Referenz auf die ORDERS)|Die Zuordnung des Wertes erfolgt anhand des Zuordnungstupels zum angegebenen Objekt ohne Bezug zu einem Ereignis|--|


Version: 3.1f 30.09.2025 Seite 153 von 158

MSCONS Anwendungshandbuch
![edi@energy logo](image)

# 14 Änderungshistorie

|Änd-ID|Ort|Änderungen<br/>Bisher|Änderungen<br/>Neu|Grund der Anpassung|Status|
|-|-|-|-|-|-|
|26807|Kapitel 5.1 Versionierung von Zeitreihen, Zeile Anwendungsfall Lastgang Gas (Prüfidentifikator 13008)|Spalte: Inhalt der Liste:<br/>Es ist zu jeder ¼-Stunde der gesetzlichen Zeit, des angegebenen Zeitintervalls des Übertragungszeitraum genau ein Wert inklusive zugehöriger Zeitangaben in SG10 anzugeben.|Spalte: Inhalt der Liste:<br/>Es ist zu jeder Stunde der gesetzlichen Zeit, des angegebenen Zeitintervalls des Übertragungszeitraum genau ein Wert inklusive zugehöriger Zeitangaben in SG10 anzugeben.|Im Gas werden wie üblich nur Stundenlastgänge ausgetauscht. Dieser Copy-Paste Fehler wird hiermit behoben.|Fehler (23.06.2025)|
|26808|Kapitel 5.1 Versionierung von Zeitreihen, Zeile Anwendungsfall Gasbeschaffenheit (Prüfidentifikator 13007)|Spalte: Inhalt der Liste:<br/>Es ist zu jeder ¼-Stunde der gesetzlichen Zeit, des angegebenen Zeitintervalls des Übertragungszeitraum genau ein Wert inklusive zugehöriger Zeitangaben in SG10 anzugeben.|Spalte: Inhalt der Liste:<br/>Es ist zu jeder Stunde der gesetzlichen Zeit, des angegebenen Zeitintervalls des Übertragungszeitraum genau ein Wert inklusive zugehöriger Zeitangaben in SG10 anzugeben.|Im Gas werden wie üblich nur Stundenlastgänge ausgetauscht. Dieser Copy-Paste Fehler wird hiermit behoben.|Fehler (23.06.2025)|
|26663|Kapitel 6.2 Generelles zur Übertragung von Energiemengen|\[...]<br/>Dabei wird in SG10 DTM+163 (Beginn Messperiode) der Zeitpunkt als Beginn angegeben, zu dem die letzte Energiemenge übermittelt wurde, oder der Zeitpunkt, an dem die Zuordnung an der Marktlokation durch den Empfänger des Zählerstandes begonnen hat.<br/><br/>Für Energiemengen, gilt: In SG10 DTM+164 (Ende Messperiode) wird der Zeitpunkt als Ende angegeben, zu dem der letzte Messwert mit demselben Nutzungszeitpunkt übermittelt wurde.<br/>\[...]|\[...]<br/>Dabei wird in SG10 DTM+163 (Beginn Messperiode) der Zeitpunkt als Beginn angegeben, zu dem die letzte Energiemenge übermittelt wurde, oder der Zeitpunkt, an dem die Zuordnung an der Marktlokation durch den Empfänger des Zählerstandes begonnen hat.<br/><br/>Für Energiemengen, gilt: In SG10 DTM+164 (Ende Messperiode) wird der Zeitpunkt als Ende angegeben, zu dem der letzte Messwert mit demselben Nutzungszeitpunkt übermittelt wurde. Für Energiemengen auf Ebene der Marktlokation die entstehen, wenn die letzte Messlokation, die der Marktlokation zugeordnet war, beendet wurde (Stilllegung der Messlokation), kann es ein Auseinanderfallen der Zeitpunkte geben, da die Marktlokation in die Zukunft beendet wird und die Messlokation zum Zeitpunkt der tatsächlichen Stilllegung. In diesem Szenario ist in SG10 DTM+164 (Ende Messperiode) der Zeitpunkt als Ende|Da die Energiemenge der Marktlokation, bei einer bei Außerbetriebnahme der Messlokation (Stilllegung), nicht zum selben Zeitpunkt endet muss, sondern die Zuordnung der Energiemenge der Marktlokation länger sein kann als die auf Ebene der Messlokation ausgetauschten Zählerstände wird dieser entsprechende Hinweis zur Klarstellung aufgenommen.|Fehler (17.04.2025)|


Version: 3.1f
30.09.2025
Seite 154 von 158

MSCONS Anwendungshandbuch
![edi@energy Datenformate Strom & Gas](image)

|Änd-ID|Ort|Änderungen||Grund der Anpassung|Status||||||
|-|-|-|-|-|-|-|-|-|-|-|
|||Bisher|Neu||||||||
||||angegeben, zu dem die Marktlokation beendet (stillgelegt) wurde. \[...]||||||||
||||26666|||Kapitel 6.2 Generelles zur Übertragung von Energiemengen, Unterkapitel Übertragung von Einzelwerten für eine Marktlokation ohne Messlokation (Pauschalanlage) Strom und Gas von NB an LF|Unterkapitel vorhanden|Unterkapitel nicht vorhanden|Die Beschreibung im Kapitel passt nicht mehr zu den aktuellen Nachrichten und dazugehörigen Beschreibungen. Daher wird das Kapitel entfernt.|Fehler (17.04.2025)|
|26083|Kapitel 6.3.3 Übertragung von Energiemenge und Leistungsmaximum Strom|\[...]<br/>Bei der Übermittlung des Lieferscheines vom NB für Marktlokationen mit Arbeits- / Leistungspreis (Strom) ist im BGM-Segment DE1001 der Qualifier Z42 (Lieferschein Arbeits- / Leistungspreis) zu verwenden. Bei allen anderen ist im BGM-Segment DE1001 der Qualifier Z28 (Energiemenge und Leistungsmaximum) zu verwenden.<br/>Übertragen wird die Arbeit mit Nennung des dafür relevanten Zeitraums. Weiterhin wird in diesem Zeitraum das angefallene Monatsleistungsmaximum übertragen. Bei Verwendung des Codes Z42 (Lieferschein Arbeits- / Leistungspreis) im BGM kann das Leistungsmaximum auch außerhalb des betrachtenden Zeitraums liegen.<br/>Bei pauschalen Marktlokationen, für die ein Monatsleistungsmaximum benötigt wird, ist zur Ableitung der Monatsangabe des Lieferscheins das Endedatum SG26 DTM+156 der Rechnungsperiode aus der Rechnungsposition der INVOIC zu verwenden.<br/>Die Angabe des Zeitraumes der Arbeit, für die die jeweilige Menge übertragen wird, erfolgt über SG10 DTM+163 und SG10 DTM+164.|\[...]<br/>Bei der Übermittlung des Lieferscheines vom NB für Marktlokationen mit Arbeits- / Leistungspreis (Strom) ist im BGM-Segment DE1001 der Qualifier Z42 (Lieferschein Arbeits- / Leistungspreis) zu verwenden. Bei allen anderen ist im BGM-Segment DE1001 der Qualifier Z28 (Energiemenge und Leistungsmaximum) zu verwenden.<br/>Bei der Übermittlung der Energiemenge und Leistungsmaximum gemäß WiM wird die Arbeit mit Nennung des dafür relevanten Zeitraums übertragen. Weiterhin wird in diesem Zeitraum das angefallene Monatsleistungsmaximum übermittelt.<br/>Bei der Übermittlung des Lieferscheins vom NB für Marktlokation mit Arbeits- / Leistungspreis wird die Arbeit mit Nennung des dafür relevanten Zeitraums übertragen und weiterhin, abhängig vom Leistungspreissystem (Jahresleistungspreissystem, Monatsleistungspreissystem oder Tagesleistungspreissystem) das angefallene Leistungsmaximum. Bei Verwendung des Codes Z42 (Lieferschein Arbeits- / Leistungspreis) im BGM kann das Leistungsmaximum auch außerhalb des betrachtenden Zeitraums liegen.|Da es auch Netzentgelte mit Tagesleistungspreissystem gibt, muss auch die Übermittlung einer Tagesmaximalleistung im Lieferschein vom NB für Marktlokationen mit Arbeits- / Leistungspreis (Strom) möglich sein.|Fehler (30.09.2025)||||||


Version: 3.1f 30.09.2025 Seite 155 von 158

MSCONS Anwendungshandbuch
![edi@energy Datenformate Strom & Gas](image)

|Änd-ID|Ort|Änderungen||Grund der Anpassung|Status||
|-|-|-|-|-|-|-|
|||Bisher|Neu||||
|||Zu dem zu übermittelnden Monatsmaximum ist der Monat, in dem das Monatsmaximum aufgetreten ist im SG10 DTM+306 zu übermitteln.<br/>\[...]|Bei pauschalen Marktlokationen, für die ein Leistungsmaximum benötigt wird, ist zur Ableitung der Monatsangabe des Lieferscheins das Endedatum SG26 DTM+156 der Rechnungsperiode aus der Rechnungsposition der INVOIC zu verwenden.<br/>Die Angabe des Zeitraumes der Arbeit, für die die jeweilige Menge übertragen wird, erfolgt über SG10 DTM+163 und SG10 DTM+164.<br/>Bei Anwendung des Jahresleistungspreissystem oder des Monatsleistungspreissystem ist zu dem zu übermittelnden Leistungsmaximum der Monat, in dem das Maximum aufgetreten ist im SG10 DTM+306 mit dem Code 610 CCYYMM zu übermitteln.<br/>Bei Anwendung des Tagesleistungspreissystem ist zu dem zu übermittelnden Leistungsmaximum der Tag, in dem das Maximum aufgetreten ist im SG10 DTM+306 mit dem Code 102 CCYYMMDD zu übermitteln.<br/>Sollen Daten von mehreren Marktlokationen in einer Datei übertragen werden, ist die Wiederholung über das UNH-Segment vorzunehmen.<br/>\[...]||||
|26664||Kapitel 6.3.7 Anwendungsübersicht Energiemengen Strom, Prüfidentifikator 13019 Energiemenge (Strom), SG10 STS+10 Grundlage der Energiemenge, DE4405|\[...]<br/>Z37 Zählerstand zum Ende der angegebenen Energiemenge vorhanden und kommuniziert X \[84] ∨ (\[88] ∧ \[545])<br/><br/>Bedingung:<br/>\[84] Wenn in derselben SG9 LIN die Angabe STS+10+Z39 nicht vorhanden<br/>\[88] Wenn der Wert in DTM+164 DE2380 derselben SG6 LOC+172 mit demselben Wert in SG9 PIA+5 DE7140 der späteste angegebene Zeitpunkt ist|\[...]<br/>Z37 Zählerstand zum Ende der angegebenen Energiemenge vorhanden und kommuniziert X \[84] ∨ (\[88] ∧ \[545] ∧ \[577])<br/><br/>Bedingung:<br/>\[84] Wenn in derselben SG9 LIN die Angabe STS+10+Z39 nicht vorhanden<br/>\[88] Wenn der Wert in DTM+164 DE2380 derselben SG6 LOC+172 mit demselben Wert in SG9 PIA+5 DE7140 der späteste angegebene Zeitpunkt ist|Da die Energiemenge der Marktlokation, bei einer bei Außerbetriebnahme der Messlokation (Stilllegung), nicht zum selben Zeitpunkt endet muss, sondern die Zuordnung der Energiemenge der Marktlokation länger sein kann als die auf Ebene der Messlokation ausgetauschten Zählerstände wird dieser entsprechende Hinweis zur Klarstellung aufgenommen.|Fehler (17.04.2025)|


Version: 3.1f 30.09.2025 Seite 156 von 158

MSCONS Anwendungshandbuch
![edi@energy Datenformate Strom & Gas](image)

|Änd-ID|Ort|Änderungen||Grund der Anpassung|Status||
|-|-|-|-|-|-|-|
|||Bisher|Neu||||
|||\[545] Hinweis: Bei einer Mengenaufteilung (z. B. Aufgrund einer Abgrenzung) für SG6 LOC+172 muss für den spätesten angegebenen Zeitpunkt zum Ende des Zeitintervalls (über alle Wiederholungen der LIN-Segmente derselben SG6 LOC+172 hinweg) zu jeder OBIS-Kennziffer ein Zählerstand vorhanden und kommuniziert sein.|\[545] Hinweis: Bei einer Mengenaufteilung (z. B. Aufgrund einer Abgrenzung) für SG6 LOC+172 muss für den spätesten angegebenen Zeitpunkt zum Ende des Zeitintervalls (über alle Wiederholungen der LIN-Segmente derselben SG6 LOC+172 hinweg) zu jeder OBIS-Kennziffer ein Zählerstand vorhanden und kommuniziert sein.<br/><br/>\[577] Hinweis: Dieser Code ist auch zu verwenden, wenn aufgrund der Beendigung einer Messlokation (Stilllegung) die Beendigung der Marktlokation (Stilllegung) zu unterschiedlichen Zeitpunkten erfolgt, das heißt die Beendigung der Messlokation vor der Beendigung der Marktlokation erfolgt. Die Energiemenge ist bis zum Endezeitpunkt der Marklokation zu übermitteln, wenngleich der letzte Zählerstand der Messlokation zu einem früheren Zeitpunkt liegt.||||
|26889||Kapitel 6.3.7 Anwendungsübersicht Energiemengen Strom, Prüfidentifikator 13016 Energiemenge u. Leistungsmax. (Strom), SG10 DTM+306 Leistungsperiode, DE2379|610 CCYYMM X|102 CCYYMMDD X (\[91] ∧ \[580])<br/>610 CCYYMM X (\[69] ∧ \[581]) ⊻ (\[91] ∧ (\[578] ⊻ \[579]))<br/><br/>Bedingung:<br/>\[69] Wenn BGM+Z28 vorhanden<br/>\[91] Wenn BGM+Z42 vorhanden<br/>\[578] Hinweis: Wenn es sich um die Übermittlung des Leistungswertes für die Netzentgelte mit Jahresleistungspreissystem handelt.<br/>\[579] Hinweis: Wenn es sich um die Übermittlung des Leistungswertes für die Netzentgelte mit Monatsleistungspreissystem handelt.<br/>\[580] Hinweis: Wenn es sich um die Übermittlung des Leistungswertes für die Netzentgelte mit Tagesleistungspreissystem handelt.|Da es auch Netzentgelte mit Tagesleistungspreissystem gibt, muss auch die Übermittlung einer Tagesmaximalleistung im Lieferschein vom NB für Marktlokationen mit Arbeits-/Leistungspreis (Strom) möglich sein.|Fehler (30.09.2025)|


Version: 3.1f 30.09.2025 Seite 157 von 158

MSCONS Anwendungshandbuch
![edi@energy Datenformate Strom & Gas](image)

|Änd-ID|Ort|Änderungen||Grund der Anpassung|Status||||||
|-|-|-|-|-|-|-|-|-|-|-|
|||Bisher|Neu||||||||
||||\[581]: Hinweis: Wenn es sich um die Übermittlung des Monatsmaximums gemäß WiM handelt.||||||||
||||26010|||Kapitel 7.3.2 Anwendungsübersicht Lastgang Gas, Prüfidentifikator 13008 Lastgang (Gas), SG10 QTY Mengenangaben, DE6063|\[...]<br/>20 Nicht verwendbarer Wert X (\[35] ∧ \[36])<br/>X (\[32] ∧ \[33] ∧ \[506])<br/>\[...]|\[...]<br/>20 Nicht verwendbarer Wert X (\[35] ∧ \[36])<br/>⊻ (\[32] ∧ \[33] ∧ \[506])<br/>\[...]|Verwendung der korrekten Notation (⊻ statt X) zwischen den Voraussetzungen.|Fehler (20.03.2025)|
|25497|Kapitel 8.1.1 Übertragung normiertes Profil, Tabelle|Zeile:<br/>Sparte: Strom<br/>Kommunikation von: NB an ÜNB<br/>Art der Werte: Normiertes Profil<br/>\[...]<br/><br/>vorhanden|Zeile:<br/>Sparte: Strom<br/>Kommunikation von: NB an ÜNB<br/>Art der Werte: Normiertes Profil<br/>\[...]<br/><br/>nicht vorhanden|Zeile entfernt, da durch das Festlegungsverfahren zur Anpassung der Marktkommunikation zur Realisierung der nach dem Messstellenbetriebsgesetz geforderten Übermittlung von Zählerstandsgängen (Datenübermittlung ZSG) BK6-24-174 die Schritte entfallen sind.|Fehler (18.02.2025)||||||
|26580|Kapitel 9.2 Anwendungsübersicht Gasbeschaffenheitsdaten, Prüfidentifikator 13007 Gasbeschaffenheit, SG10 QTY Mengenangaben, DE6063|\[...]<br/><br/>201 Vorschlagswert X (\[32] ∧ (\[33] ∨ \[36]))<br/>X (\[35] ∧ \[36])<br/><br/>20 Nicht verwendbarer Wert X (\[32] ∧ \[33])<br/>X (\[35] ∧ \[36])|\[...]<br/><br/>201 Vorschlagswert X (\[32] ∧ (\[33] ∨ \[36]))<br/>⊻ (\[35] ∧ \[36])<br/><br/>20 Nicht verwendbarer Wert X (\[32] ∧ \[33])<br/>⊻ (\[35] ∧ \[36])|Verwendung der korrekten Notation (⊻ statt X) zwischen den Voraussetzungen.|Fehler (20.03.2025)||||||


Version: 3.1f
30.09.2025
Seite 158 von 158