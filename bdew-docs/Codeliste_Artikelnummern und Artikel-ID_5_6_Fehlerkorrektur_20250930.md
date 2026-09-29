![edi@energy logo](cpey)

# Konsolidierte Lesefassung mit Fehlerkorrekturen
Stand: 30.09.2025

## Codeliste der Artikelnummern und Artikel-ID

Version: 5.6

Ursprüngliches Publikationsdatum: 01.04.2025

Gültig ab: 01.09.2025

Autor: BDEW

Codeliste der Artikelnummern und Artikel-ID

![edi@energy logo](omeq)

## **Disclaimer**

Die zusätzlich veröffentlichte Word-Datei dient als informatorische Lesefassung und entspricht inhaltlich der PDF-Datei. Die PDF-Datei ist das gültige Dokument. Diese Word-Datei wird bis auf Weiteres rein informatorisch und ergänzend veröffentlicht. Der BDEW behält sich vor, in Zukunft eine kostenpflichtige Veröffentlichung der Word-Datei einzuführen.

Version: 5.6
30.09.2025
Seite 2 von 60

Codeliste der Artikelnummern und Artikel-ID

![edi@energy. Datenformate Strom & Gas](xxzu)

## **Inhaltsverzeichnis**

|1|**Einleitung**|4|
|-|-|-|
|2|**Codeliste der Artikelnummern**|5|
|3|**Codeliste der Gruppenartikel-ID und Artikel-ID**|12|
||**3.1 Netznutzung für Marktlokationen**|13|
||3.1.1 Entgelte des Jahresleistungspreissystems für die Sparte Strom|13|
||3.1.2 Entgelte des Grundpreis-/Arbeitspreissystems für die Sparte Strom|18|
||3.1.3 Entgelte des Monatsleistungspreissystems für die Sparte Strom|21|
||3.1.4 Entgelte des Stromspeichers gemäß § 19 Abs. 4 StromNEV für die Sparte Strom|27|
||3.1.5 Netzreservekapazität für die Sparte Strom|28|
||3.1.6 Entgelte des Messstellenbetriebs bei kME für die Sparte Strom|30|
||3.1.7 Individuelle Netzentgelte für die Sparte Strom|34|
||3.1.8 Konzessionsabgaben für die Sparte Strom|36|
||3.1.9 Entgelte des Tagesleistungspreissystems für die Sparte Strom|40|
||3.1.10 Preisbestandteile, deren Höhe aufgrund gesetzlicher Vorgaben durch Dritte jährlich ermittelt und veröffentlicht werden für die Sparte Strom|41|
||****3.2 Separat bestellbare Einzelleistungen für Marktlokationen und Verzugskosten für** die Sparte Strom und Gas**|47|
||**3.3 Freiwillige Abrechnung sonstiger Leistungen für die Sparte Strom**|48|
||**3.4 Abrechnung beim MSB bestellter Leistungen**|49|
||3.4.1 Regelungen zu den vom MSB verwendeten Artikel-ID|49|
||3.4.2 Artikel-ID für die Bestellprozesse beim MSB|51|
||**3.5 Abrechnung Messstellenbetrieb für die Sparte Strom**|53|
||3.5.1 Abrechnung Messstellenbetrieb vom MSB an LF|53|
||3.5.2 Abrechnung Messstellenbetrieb vom MSB an NB|56|
|4|**Änderungshistorie**|57|


Version: 5.6
30.09.2025
Seite 3 von 60

Codeliste der Artikelnummern und Artikel-ID

![edi@energy. Datenformate Strom & Gas](flkt)

## **1   Einleitung**

Die Codeliste der Artikelnummern, Gruppenartikel-ID und Artikel-ID findet Anwendung in den
Nachrichtenbeschreibungen INVOIC, ORDERS, ORDRSP, PRICAT, QUOTES und UTILMD. Mit der
BNetzA-Festlegung BK6-20-160 zur Weiterentwicklung der Netzzugangsbedingungen Strom
wurden die Artikelnummern in der Sparte Strom für die GPKE von den Artikel-ID aus dem
Preisblatt der Anlage 1b „Netznutzungspreisblatt“ der BNetzA abgelöst. Somit findet
ausschließlich die Codeliste der Artikelnummern und Artikel-ID in der Marktkommunikation
Anwendung.

Im Gasmarkt erfolgt die Abrechnung der Kosten für die Unterbrechung und Wiederherstellung
der Anschlussnutzung auf Anweisung des Lieferanten sowie die Abrechnung der Verzugskosten
unter Nutzung der entsprechenden Artikel-ID. Für alle anderen bisher mittels Artikelnummern
identifizierten und über die INVOIC abgerechneten Leistungen bleiben die entsprechenden
Artikelnummern bestehen.

Die Codeliste der Artikelnummern und Artikel-ID unterliegt dem von der BNetzA vorgegebenen
Änderungsmanagement.

Version: 5.6                                                                 30.09.2025                                                                <page_number>Seite 4 von 60</page_number>

Codeliste der Artikelnummern und Artikel-ID

![edi@energy. Datenformate Strom & Gas](hnnd)

## **2   Codeliste der Artikelnummern**

|Artikel|Artikel-nummer|BDEW-Artikel-nummer¹|Hinweise|Prüfidentifikator: konform zu<br/>A<br/>GPKE|Prüfidentifikator: konform zu<br/>A<br/>GeLi Gas|Prüfidentifikator: konform zu<br/>B<br/>GPKE|Prüfidentifikator: konform zu<br/>B<br/>GeLi Gas|Prüfidentifikator: konform zu<br/>C<br/>MaBiS|Prüfidentifikator: konform zu<br/>H<br/>WiM|Prüfidentifikator: konform zu<br/>D, E,F, G<br/>WiM|Prüfidentifikator: konform zu<br/>I<br/>MMM|Prüfidentifikator: konform zu<br/>J|Mengenangabe<br/>Kapazität|Mengenangabe<br/>Geräteübern.auslaufend|Mengenangabe<br/>(energetischDE6063 = 47)(zeitlichDE6063 =136)|
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|Leistung|5|9990001 00005 3|||X|X|||||||X⁶||KWT DAY / MON / ANN|
|Leistung pauschal|7|9990001 00007 9|Wirkleistung||X||||||||X⁶||KWT DAY / MON / ANN|
|Grundpreis|8|9990001 00008 7|Ist ausschließlich dann ver-<br/>wendbar, wenn der Preis<br/>unabhängig von Arbeit und<br/>Leistung ist. Sie ist nicht zu<br/>verwenden, um die über den<br/>Preis des Sockelbetrags<br/>abgegoltene Arbeit (oder<br/>Leistung) in Rechnung zu<br/>stellen, da dieser Preis von<br/>der Jahresmenge (-leistung)<br/>der jeweiligen Marktlokation<br/>abhängt.||X|X|||||||X⁶||H87 DAY / MON / ANN|
|Reservenetzkapazität|16|9990001 00016 0|||X||||||||X⁶||KWT DAY / MON / ANN|
|Reserveleistung|17|9990001 00017 8|Wirkleistung||X||||||||X⁶||KWT DAY / MON / ANN|
|Zusätzliche Ablesung|18|9990001 00018 6||||X||X|||||||H87 n|
|Wirkarbeit|26|9990001 00026 9|||X|X|||||||X⁶||KWH n|






Seite 5 von 60

Version: 5.6
30.09.2025

Codeliste der Artikelnummern und Artikel-ID

![edi@energy. Datenformate Strom & Gas](dwum)

||Artikel|Artikel-nummer|BDEW-Artikel-nummer¹|Hinweise|Prüfidentifikator:<br/>A|Prüfidentifikator:<br/>A|Prüfidentifikator:<br/>B|Prüfidentifikator:<br/>B|Prüfidentifikator:<br/>C|Prüfidentifikator:<br/>H|Prüfidentifikator:<br/>D, E,<br/>F, G|Prüfidentifikator:<br/>D, E,|Prüfidentifikator:<br/>I|Prüfidentifikator:<br/>J|konform zu<br/>GPKE|konform zu<br/>GeLi Gas|konform zu<br/>GPKE|konform zu<br/>GeLi Gas|konform zu<br/>MaBiS|konform zu<br/>WiM|konform zu<br/>WiM|konform zu<br/>MMM|Kapazität|Geräteübern.|auslaufend|Mengenangabe<br/>(energetischDE6063 = 47)|Mengenangabe<br/>(zeitlichDE6063 =136)|
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|singulär genutzte<br/>Betriebsmittel (z. B.<br/>Trafomiete, Leitungen)|28|9990001 00028 5|Bei Betriebsmitteln wie<br/>Leitungen ist der monatliche<br/>Gesamtbetrag zu ermitteln<br/>(Preis pro km \* Anzahl km)<br/>und dieser im PRI-Segment<br/>zu verwenden.|||||||||||||X|X||||||||X⁶|H87|DAY / MON / ANN|
|Abgabe KWKG|33|9990001 00033 4||||||||||||||X|||||||||X⁶|KWH|n|
|Abschlag|37|9990001 00037 6||X|X|||||||||||||||||||||H87|n|
|Konzessionsabgabe|41|9990001 00041 7||||||||||||||X|X||||||||X⁶|KWH|n|
|Entgelt für Fernauslesung|43|9990001 00043 3||||||||||||||X|X||||||||X⁶|H87|DAY / MON / ANN|
|Untermessung|47|9990001 00047 5||||||||||||||X|X||||||||X⁶|KWH|n|
|Blindmehrarbeit|50|9990001 00050 8||||||||||||||X|||||||||X⁶|K3|n|
|Entgelt für Abrechnung|53|9990001 00053 2|||||||||||||||X|||||||||H87|DAY / MON / ANN|
|Blindmehrleistung|59|9990001 00059 0||||||||||||||X|||||||||X⁶|KVR|DAY / MON / ANN|
|Entgelt für Messung und<br/>Ablesung|61|9990001 00061 5||||||||||||||X||X||||||||H87|DAY / MON / ANN|
|Entgelt für Einbau, Betrieb<br/>und Wartung der<br/>Messtechnik|62|9990001 00062 3||||||||||||||X||X||||||||H87|DAY / MON / ANN|


Version: 5.6                                                                            30.09.2025                                                                            Seite 6 von 60

Codeliste der Artikelnummern und Artikel-ID

![edi@energy. Datenformate Strom & Gas](zsnf)

|Artikel|Artikel-nummer|BDEW-Artikel-nummer¹|Hinweise|Prüfidentifikator: konform zu<br/>A<br/>GPKE|Prüfidentifikator: konform zu<br/>A<br/>GeLi Gas|Prüfidentifikator: konform zu<br/>B<br/>GPKE|Prüfidentifikator: konform zu<br/>B<br/>GeLi Gas|Prüfidentifikator: konform zu<br/>C<br/>MaBiS|Prüfidentifikator: konform zu<br/>H<br/>WiM|Prüfidentifikator: konform zu<br/>D, E, F, G<br/>WiM|Prüfidentifikator: konform zu<br/>I<br/>MMM|Prüfidentifikator: konform zu<br/>J<br/>Kapazität|Prüfidentifikator: konform zuGeräteübern.|Mengenangabe<br/>(energetisch DE6063 = 47)|Mengenangabe<br/>(zeitlich DE6063 = 136)|auslaufend|
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|Ausgleichsenergie Überdeckung|63|9990001 00063 1||||||X|||||||KWH|n|
|Zähleinrichtung|64|9990001 00064 9|||||||X||||X||H87|DAY / MON / ANN²|
|Wandler/Mengenumwerter|65|9990001 00065 7||||X⁶|X||X||||X|X⁶|H87|DAY / MON / ANN²|
|Kommunikationseinrichtung|66|9990001 00066 5|||||||X||||X||H87|DAY / MON / ANN²|
|Technische Steuereinrichtung|67|9990001 00067 3|||||||X||||X||H87|DAY / MON / ANN²|
|§ 19 StromNEV Umlage|68|9990001 00068 1|||||X|||||||X⁶|KWH|n|
|Befestigungseinrichtung (z. B. Zählertafel)|69|9990001 00069 9|||||||X||||X||H87|DAY / MON / ANN²|
|Offshore-Netzumlage|70|9990001 00070 6|||||X|||||||X⁶|KWH|n|
|Fixe Arbeitsentgelt-komponente|71|9990001 00071 4|nur wenn nicht Artikel 8 verwendet wird||||X||||||||H87|DAY / MON / ANN|
|Fixe Leistungsentgelt-komponente|72|9990001 00072 2|nur wenn nicht Artikel 8 verwendet wird||||X||||||||H87|DAY / MON / ANN|
|Umlage abschaltbare Lasten|73|9990001 00073 0|||||X|||||||X⁶|KWH|n|
|Mehrmenge|74|9990001 00074 8||||||||X|||||KWH|n|
|Mindermenge|75|9990001 00075 6||||||||X|||||KWH|n|


Version: 5.6
30.09.2025
Seite 7 von 60

Codeliste der Artikelnummern und Artikel-ID

![edi@energy. Datenformate Strom & Gas](rofw)

|Artikel|Artikel-nummer|BDEW-Artikel-nummer¹|Hinweise|Prüfidentifikator: konform zu<br/>A|Prüfidentifikator: konform zu<br/>A|Prüfidentifikator: konform zu<br/>B|Prüfidentifikator: konform zu<br/>B|Prüfidentifikator: konform zu<br/>C|Prüfidentifikator: konform zu<br/>H|Prüfidentifikator: konform zu<br/>D, E, F, G|Prüfidentifikator: konform zu<br/>I|Prüfidentifikator: konform zu<br/>J|Prüfidentifikator: konform zu|Mengenangabe<br/>Kapazität|Mengenangabe<br/>Geräteübern.|Mengenangabe<br/>auslaufend|GPKE|GeLi Gas|GPKE|GeLi Gas|MaBiS|WiM|WiM|MMM|(energetisch DE6063 = 47)|(zeitlich DE6063 = 136)|
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|Energiesteuer|76|9990001 00076 4|Anzuwenden im Rahmen der<br/>MMM-Abrechnung, wenn<br/>der Erlaubnisschein des<br/>Lieferanten nicht vorliegt.||||||||X|||KWH|n||||||||||||
|Smartmeter-Gateway|77|9990001 00077 2|||||X⁵||X||||X|H87|DAY / MON / ANN²||||||||||||
|Steuerbox|78|9990001 00078 0|||||X⁵||X||||X|H87|DAY / MON / ANN²||||||||||||
|Entgelt für<br/>Messstellenbetrieb|79|9990001 00079 8||||X|X|||X⁷||X|X⁶|H87⁴|DAY / MON / ANN⁴||||||||||||
|Ausgleichsenergie<br/>Unterdeckung|80|9990001 00080 5||||||X||||||KWH|n||||||||||||
|Zusatzdienstleistung nach §<br/>35 Abs. 2 Nr. 1 MsbG|81|9990001 00081 3||||||||X⁷||||H87|DAY / MON / ANN||||||||||||
|Zusatzdienstleistung nach §<br/>35 Abs. 2 Nr. 2 MsbG|82|9990001 00082 1||||||||X⁷||||H87|DAY / MON / ANN||||||||||||
|Zusatzdienstleistung nach §<br/>35 Abs. 2 Nr. 3 MsbG|83|9990001 00083 9||||||||X⁷||||H87|DAY / MON / ANN||||||||||||
|Zusatzdienstleistung nach §<br/>35 Abs. 2 Nr. 4 MsbG|84|9990001 00084 7||||||||X⁷||||H87|DAY / MON / ANN||||||||||||
|Zusatzdienstleistung nach §<br/>35 Abs. 2 Nr. 5 MsbG|85|9990001 00085 5||||||||X⁷||||H87|DAY / MON / ANN||||||||||||
|Zusatzdienstleistung nach §<br/>35 Abs. 3 MsbG|86|9990001 00086 3||||||||X⁷||||H87|DAY / MON / ANN||||||||||||






Seite 8 von 60

Version: 5.6
30.09.2025

Codeliste der Artikelnummern und Artikel-ID

![edi@energy logo](bnin)

|Artikel|Artikel-nummer|BDEW-Artikel-nummer¹|Hinweise|Prüfidentifikator:<br/>A|Prüfidentifikator:<br/>A|Prüfidentifikator:<br/>B|Prüfidentifikator:<br/>B|Prüfidentifikator:<br/>C|Prüfidentifikator:<br/>H|Prüfidentifikator:<br/>D, E,F, G|Prüfidentifikator:<br/>I|Prüfidentifikator:<br/>J|Mengenangabe<br/>konform zu<br/>GPKE|Mengenangabe<br/>konform zu<br/>GeLi Gas|Mengenangabe<br/>konform zu<br/>GPKE|Mengenangabe<br/>konform zu<br/>GeLi Gas|MaBiS|WiM|WiM|MMM|Kapazität|Geräteübern.|auslaufend|(energetischDE6063 = 47)|(zeitlichDE6063 = 136)|
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|Entgelt für Kapazitäten|87|9990001 00087 1|||||||||||||||X|||n|n|||||
|Biogaswälzungsbetrag|88|9990001 00088 9|||||||||||||||X|||n|n|||||
|Umlage für<br/>Marktraumumstellung|89|9990001 00089 7|||||||||||||||X|||n|n|||||
|Aufwandspauschale|90|9990001 00090 4|||||||||||||||X|||n|n|||||
|Messentgelt|91|9990001 00091 2|||||||||||||||X|||n|n|||||


<sup>1</sup> Die Darstellung der **Artikel** **nummer** mit Leerzeichen erfolgt nur zur besseren Lesbarkeit. Beim elektronischen Datenaustausch wird die **Artikel** **nummer** immer ohne Leerzeichen verwendet.

Die Prüfziffer der **Artikel** **nummer** wird nach derselben Rechenregel ermittelt, wie bei den BDEW-Codenummern.

<sup>2</sup> Die Zeitangabe ist nur bei der Nutzungsüberlassung erforderlich.

<sup>4</sup> Nicht zu verwenden bei der Kapazitätsrechnung.

<sup>5</sup> Die Verwendung dieser **Artikel** **nummer** ist lediglich dann zulässig, wenn eine vertragliche Vereinbarung aller beteiligten Unternehmen in den Marktrollen (NB, LF, MSB) vorliegt.

<sup>6</sup> Nur **Hinweise** **GPKE** **GeLi** **Gas** **GPKE** **GeLi** **Gas** **MaBiS** **WiM** **WiM** **MMM** **KapazitätGeräteübern.auslaufend** **(energetisch** **DE6063** **=** **47)** **(zeitlich** **DE6063** **=** **136)**: Nur anzuwenden für Leistungszeiträume bis einschließlich 31.12.2022

Version: 5.6                                          30.09.2025                                          Seite 9 von 60

Codeliste der Artikelnummern und Artikel-ID

![edi@energy. Datenformate Strom & Gas](qrfr)

<sup>7</sup> Nur WiM: Nur anzuwenden für Leistungszeiträume bis einschließlich 31.12.2023

**X:** für die Nutzung in der INVOIC zur Abrechnung im Rahmen der GeLi Gas, GPKE, MaBiS, WiM bzw. MMM freigegeben. Weitergehende Anwendungen der Artikelnummern außerhalb der INVOIC sind in den entsprechenden Anwendungshandbüchern explizit aufgeführt.

**auslaufend:** Darunter wird verstanden, dass die Artikelnummer zukünftig nicht mehr benutzt werden soll. Die Artikelnummer kann so lange genutzt werden, wie der entsprechende Artikel im Preisblatt ausgewiesen ist. Die Artikelnummern können für rückwirkende Korrekturen und Stornierungen von bereits gestellten Rechnungen verwendet werden.

**zeitliche Mengenangabe:**

›   n steht für nicht zu nutzen.

›   Die Angabe DAY/MON/ANN ist bei zeitanteiligen Preisen notwendig. Es ist der passende Zeitqualifier zu verwenden.

30.09.2025

Seite 10 von 60

Version: 5.6

Version: 5.6
30.09.2025
Seite 10 von 60

Codeliste der Artikelnummern und Artikel-ID

![edi@energy logo](qfgt)

## **Bedeutung der Buchstaben in der Zeile Prüfidentifikator:**

A:     Prüfidentifikator 31001 (Abschlagsrechnung)
B:     Prüfidentifikator 31002 (NN-Rechnung)
C:     Prüfidentifikator 31003 (WiM-Rechnung)
D:     Prüfidentifikator 31005 (MMM-Rechnung)
E:     Prüfidentifikator 31006 (MMM-selbst ausg. Rechnung)
F:     Prüfidentifikator 31007 (Aggreg. MMM-Rechnung)
G:     Prüfidentifikator 31008 (Aggreg. MMM-selbst ausg. Rechnung)
H:     Prüfidentifikator 15002 (Angebot zur Abrechnung des Messstellenbetriebs), 31009 (MSB-Rechnung)
I:     Prüfidentifikator 31010 (Kapazitätsrechnung)
J:     Prüfidentifikatoren 15001, 17001, 19001 (Geräteübernahme Angebot, Bestellung und Bestellbestätigung)





Seite 11 von 60

Version: 5.6
30.09.2025

Codeliste der Artikelnummern und Artikel-ID

![edi@energy. Datenformate Strom & Gas](ehyh)

## **3   Codeliste der Gruppenartikel-ID und Artikel-ID**

In der neuen Systematik wird zwischen Gruppenartikel-ID und Artikel-ID unterschieden.

Die Artikel-ID hat das Format n1-n2-n1-n3 oder n1-n2-n1-n8 oder n1-n2-n1-n8-n2 oder n1-n2-n1-n8-n2-n1.

Die Gruppenartikel-ID hat das Format n1-n2-n1 oder n1-n2-n1-n8-n2 und wird am Anfang einer zugehörenden Artikel-ID wiederholt.

So gehört z. B. die Artikel-ID 1-01-1-001 zu der Gruppenartikel-ID 1-01-1. Das bedeutet, wenn es eine Gruppenartikel-ID gibt, muss auch mindestens eine Artikel-ID dazugehören. Dagegen existieren Artikel-ID auch ohne eine Gruppenartikel-ID.

Fachlich gesehen, ist immer dann eine Gruppenartikel-ID vorhanden, wenn der Preis aufgrund verschiedener Mengen variiert. In diesen Fällen wird die Gruppenartikel-ID über die Stammdaten ausgetauscht und ist niemals Bestandteil des Preisblattes.

## **Hinweis zum Aufbau des Formats:**

Die Bestandteile der Formatbeschreibung der Gruppenartikel-ID bzw. Artikel-ID bestehen aus einem Buchstaben, einer Zahl und einem Bindestrich. Der Buchstabe n steht für rein numerische Zeichen, die Zahl gibt die exakte Anzahl der Zeichen an der Stelle an und der Bindestrich "-" trennt die Zahlenblöcke und ist exakt so in der Gruppenartikel-ID bzw. Artikel-ID anzugeben.

Beispiel:

n1 = numerisch einstellig

## **Legende für die Tabellen des Kapitels:**

X     in dem aufgeführten Fall zu nutzen

--     in dem aufgeführten Fall nicht zu nutzen

SOR  darf nur bei dem Rechnungstyp SOR genutzt werden

Version: 5.6

30.09.2025

Seite 12 von 60
Version: 5.6
30.09.2025
Seite 12 von 60

Codeliste der Artikelnummern und Artikel-ID

![edi@energy. Datenformate Strom & Gas](rpbt)

## **3.1 Netznutzung für Marktlokationen**

### **3.1.1 Entgelte des Jahresleistungspreissystems für die Sparte Strom**

|ID|Bezeichnung|Einheit|UTILMD<br/>Codever-wendung|UTILMD<br/>Preis-angabe|PRICAT<br/>Codever-wendung|PRICAT<br/>Preis-angabe|INVOIC<br/>Codever-wendung|INVOIC<br/>Preis-angabe|
|-|-|-|-|-|-|-|-|-|
|1-01-1|Jahresleistungspreissystem Höchstspannung||X|--|--|--|--|--|
|1-01-1-001|Jahresleistungspreissystem Höchstspannung<br/>Jahresbenutzungsdauerstunden <2500 h/a Leistungspreis|€/(kW\*Tag)|--|--|X|X|X|X|
|1-01-1-002|Jahresleistungspreissystem Höchstspannung<br/>Jahresbenutzungsdauerstunden <2500 h/a Arbeitspreis|€/kWh|--|--|X|X|X|X|
|1-01-1-003|Jahresleistungspreissystem Höchstspannung<br/>Jahresbenutzungsdauerstunden >=2500 h/a Leistungspreis|€/(kW\*Tag)|--|--|X|X|X|X|
|1-01-1-004|Jahresleistungspreissystem Höchstspannung<br/>Jahresbenutzungsdauerstunden >=2500 h/a Arbeitspreis|€/kWh|--|--|X|X|X|X|
|1-01-2|Umspannung Höchst-/Hochspannung||X|--|--|--|--|--|
|1-01-2-001|Jahresleistungspreissystem Umspannung Höchst-/Hochspannung<br/>Jahresbenutzungsdauerstunden <2500 h/a Leistungspreis|€/(kW\*Tag)|--|--|X|X|X|X|
|1-01-2-002|Jahresleistungspreissystem Umspannung Höchst-/Hochspannung<br/>Jahresbenutzungsdauerstunden <2500 h/a Arbeitspreis|€/kWh|--|--|X|X|X|X|
|1-01-2-003|Jahresleistungspreissystem Umspannung Höchst-/Hochspannung<br/>Jahresbenutzungsdauerstunden >=2500 h/a Leistungspreis|€/(kW\*Tag)|--|--|X|X|X|X|
|1-01-2-004|Jahresleistungspreissystem Umspannung Höchst-/Hochspannung<br/>Jahresbenutzungsdauerstunden >=2500 h/a Arbeitspreis|€/kWh|--|--|X|X|X|X|


Version: 5.6

30.09.2025

Seite 13 von 60

Version: 5.6
30.09.2025
Seite 13 von 60

Codeliste der Artikelnummern und Artikel-ID

![edi@energy. Datenformate Strom & Gas](nmko)

|ID|Bezeichnung|Einheit|UTILMD<br/>Codever-wendung|UTILMD<br/>Preis-angabe|PRICAT<br/>Codever-wendung|PRICAT<br/>Preis-angabe|INVOIC<br/>Codever-wendung|INVOIC<br/>Preis-angabe|
|-|-|-|-|-|-|-|-|-|
|1-01-3|Hochspannung||X|--|--|--|--|--|
|1-01-3-001|Jahresleistungspreissystem Hochspannung<br/>Jahresbenutzungsdauerstunden <2500 h/a Leistungspreis|€/(kW\*Tag)|--|--|X|X|X|X|
|1-01-3-002|Jahresleistungspreissystem Hochspannung<br/>Jahresbenutzungsdauerstunden <2500 h/a Arbeitspreis|€/kWh|--|--|X|X|X|X|
|1-01-3-003|Jahresleistungspreissystem Hochspannung<br/>Jahresbenutzungsdauerstunden >=2500 h/a Leistungspreis|€/(kW\*Tag)|--|--|X|X|X|X|
|1-01-3-004|Jahresleistungspreissystem Hochspannung<br/>Jahresbenutzungsdauerstunden >=2500 h/a Arbeitspreis|€/kWh|--|--|X|X|X|X|
|1-01-4|Umspannung Hoch-/Mittelspannung||X|--|--|--|--|--|
|1-01-4-001|Jahresleistungspreissystem Umspannung Hoch-/Mittelspannung<br/>Jahresbenutzungsdauerstunden <2500 h/a Leistungspreis|€/(kW\*Tag)|--|--|X|X|X|X|
|1-01-4-002|Jahresleistungspreissystem Umspannung Hoch-/Mittelspannung<br/>Jahresbenutzungsdauerstunden <2500 h/a Arbeitspreis|€/kWh|--|--|X|X|X|X|
|1-01-4-003|Jahresleistungspreissystem Umspannung Hoch-/Mittelspannung<br/>Jahresbenutzungsdauerstunden >=2500 h/a Leistungspreis|€/(kW\*Tag)|--|--|X|X|X|X|
|1-01-4-004|Jahresleistungspreissystem Umspannung Hoch-/Mittelspannung<br/>Jahresbenutzungsdauerstunden >=2500 h/a Arbeitspreis|€/kWh|--|--|X|X|X|X|
|1-01-5|Mittelspannung||X|--|--|--|--|--|
|1-01-5-001|Jahresleistungspreissystem Mittelspannung<br/>Jahresbenutzungsdauerstunden <2500 h/a Leistungspreis|€/(kW\*Tag)|--|--|X|X|X|X|
|1-01-5-002|Jahresleistungspreissystem Mittelspannung<br/>Jahresbenutzungsdauerstunden <2500 h/a Arbeitspreis|€/kWh|--|--|X|X|X|X|


Version: 5.6                                                                    30.09.2025                                                                    Seite 14 von 60

Codeliste der Artikelnummern und Artikel-ID

![edi@energy. Datenformate Strom & Gas](cjhj)

|ID|Bezeichnung|Einheit|UTILMD<br/>Codever-wendung|UTILMD<br/>Preis-angabe|PRICAT<br/>Codever-wendung|PRICAT<br/>Preis-angabe|INVOIC<br/>Codever-wendung|INVOIC<br/>Preis-angabe|
|-|-|-|-|-|-|-|-|-|
|1-01-5-003|Jahresleistungspreissystem Mittelspannung<br/>Jahresbenutzungsdauerstunden >=2500 h/a Leistungspreis|€/(kW\*Tag)|--|--|X|X|X|X|
|1-01-5-004|Jahresleistungspreissystem Mittelspannung<br/>Jahresbenutzungsdauerstunden >=2500 h/a Arbeitspreis|€/kWh|--|--|X|X|X|X|
|1-01-6|Umspannung Mittel-/Niederspannung||X|--|--|--|--|--|
|1-01-6-001|Jahresleistungspreissystem Umspannung Mittel-/Niederspannung<br/>Jahresbenutzungsdauerstunden <2500 h/a Leistungspreis|€/(kW\*Tag)|--|--|X|X|X|X|
|1-01-6-002|Jahresleistungspreissystem Umspannung Mittel-/Niederspannung<br/>Jahresbenutzungsdauerstunden <2500 h/a Arbeitspreis|€/kWh|--|--|X|X|X|X|
|1-01-6-003|Jahresleistungspreissystem Umspannung Mittel-/Niederspannung<br/>Jahresbenutzungsdauerstunden >=2500 h/a Leistungspreis|€/(kW\*Tag)|--|--|X|X|X|X|
|1-01-6-004|Jahresleistungspreissystem Umspannung Mittel-/Niederspannung<br/>Jahresbenutzungsdauerstunden >=2500 h/a Arbeitspreis|€/kWh|--|--|X|X|X|X|
|1-01-6-005⁸|Jahresleistungspreissystem Umspannung Mittel-/Niederspannung<br/>Pauschale Reduzierung nach Modul 1 der Festlegungen zu<br/>Netzentgelten bei Anwendung der netzorientierten Steuerung von<br/>steuerbaren Verbrauchseinrichtungen und steuerbaren<br/>Netzanschlüssen nach § 14a EnWG gem. Festlegungen BK6-22-300<br/>und BK8-22/010-A|€/Tag|X|--|X|X|X|X|


8 Die Artikel-ID ist gültig bis 1.1.2025, 00:00 Uhr.

Version: 5.6

30.09.2025

Seite 15 von 60

Codeliste der Artikelnummern und Artikel-ID

![edi@energy logo](wjog)

|ID|Bezeichnung|Einheit|UTILMD<br/>Codever-wendung|UTILMD<br/>Preis-angabe|PRICAT<br/>Codever-wendung|PRICAT<br/>Preis-angabe|INVOIC<br/>Codever-wendung|INVOIC<br/>Preis-angabe|
|-|-|-|-|-|-|-|-|-|
|1-01-7|Niederspannung||X||||||
|1-01-7-001|Jahresleistungspreissystem Niederspannung<br/>Jahresbenutzungsdauerstunden <2500 h/a Leistungspreis|€/(kW\*Tag)|||X|X|X|X|
|1-01-7-002|Jahresleistungspreissystem Niederspannung<br/>Jahresbenutzungsdauerstunden <2500 h/a Arbeitspreis|€/kWh|||X|X|X|X|
|1-01-7-003|Jahresleistungspreissystem Niederspannung<br/>Jahresbenutzungsdauerstunden >=2500 h/a Leistungspreis|€/(kW\*Tag)|||X|X|X|X|
|1-01-7-004|Jahresleistungspreissystem Niederspannung<br/>Jahresbenutzungsdauerstunden >=2500 h/a Arbeitspreis|€/kWh|||X|X|X|X|
|1-01-8⁹|§ 14a EnWG - Entgelt für RLM-Kunden||X||||||
|1-01-8-001⁹|Jahresleistungspreissystem Niederspannung<br/>Jahresbenutzungsdauerstunden <2500 h/a für Marktlokationen nach<br/>§ 14a EnWG - Entgelt für RLM-Kunden Leistungspreis|€/(kW\*Tag)|||X|X|X|X|
|1-01-8-002⁹|Jahresleistungspreissystem Niederspannung<br/>Jahresbenutzungsdauerstunden <2500 h/a für Marktlokationen nach<br/>§ 14a EnWG - Entgelt für RLM-Kunden Arbeitspreis|€/kWh|||X|X|X|X|
|1-01-8-003⁹|Jahresleistungspreissystem Niederspannung<br/>Jahresbenutzungsdauerstunden >=2500 h/a für Marktlokationen<br/>nach § 14a EnWG - Entgelt für RLM-Kunden Leistungspreis|€/(kW\*Tag)|||X|X|X|X|
|1-01-8-004⁹|Jahresleistungspreissystem Niederspannung<br/>Jahresbenutzungsdauerstunden >=2500 h/a für Marktlokationen<br/>nach § 14a EnWG - Entgelt für RLM-Kunden Arbeitspreis|€/kWh|||X|X|X|X|


<sup>9</sup> Die Einschränkung der Gültigkeit erfolgt durch die Beschlüsse BK6-22-300 und BK8-22/010-A.

Version: 5.6                                                                             30.09.2025                                                                             Seite 16 von 60

Version: 5.6                                                                             30.09.2025                                                                             Seite 16 von 60

Codeliste der Artikelnummern und Artikel-ID

![edi@energy. Datenformate Strom & Gas](dmnx)

|ID|Bezeichnung|Einheit|UTILMD<br/>Codever-wendung|UTILMD<br/>Preis-angabe|PRICAT<br/>Codever-wendung|PRICAT<br/>Preis-angabe|INVOIC<br/>Codever-wendung|INVOIC<br/>Preis-angabe|
|-|-|-|-|-|-|-|-|-|
|1-01-9-001¹⁰|Jahresleistungspreissystem Niederspannung<br/>Pauschale Reduzierung nach Modul 1 der Festlegungen zu<br/>Netzentgelten bei Anwendung der netzorientierten Steuerung von<br/>steuerbaren Verbrauchseinrichtungen und steuerbaren<br/>Netzanschlüssen nach § 14a EnWG gem. Festlegungen BK6-22-300<br/>und BK8-22/010-A|€/Tag|X|--|X|X|X|X|
|1-01-9-002¹¹|Jahresleistungspreissystem Umspannung Mittel-/Niederspannung<br/>Pauschale Reduzierung nach Modul 1 der Festlegungen zu<br/>Netzentgelten bei Anwendung der netzorientierten Steuerung von<br/>steuerbaren Verbrauchseinrichtungen und steuerbaren<br/>Netzanschlüssen nach § 14a EnWG gem. Festlegungen BK6-22-300<br/>und BK8-22/010-A|€/Tag|X|--|X|X|X|X|


10 Die Gültigkeit ergibt sich aus den BNetzA-Festlegungen BK6-22-300 und BK8-22/010-A.

11 Die Artikel-ID ist gültig ab 1.1.2025, 00:00 Uhr.

Version: 5.6 30.09.2025 Seite 17 von 60

Version: 5.6 30.09.2025 Seite 17 von 60

Codeliste der Artikelnummern und Artikel-ID

![edi@energy. Datenformate Strom & Gas](buub)

## **3.1.2    Entgelte des Grundpreis-/Arbeitspreissystems für die Sparte Strom**

|ID|Bezeichnung|Einheit|UTILMD<br/>Codever-wendung|UTILMD<br/>Preis-angabe|PRICAT<br/>Codever-wendung|PRICAT<br/>Preis-angabe|INVOIC<br/>Codever-wendung|INVOIC<br/>Preis-angabe|
|-|-|-|-|-|-|-|-|-|
|1-02-0-001|Grundpreis-/ Arbeitspreissystem Marktlokation Grundpreis für Arbeitspreissystem Grundpreis|€/Tag|X|--|X|X|X|X|
|1-02-0-002|Grundpreis-/ Arbeitspreissystem Marktlokation der Kategorie sonstiger Verbrauch (Marktlokation, die in keine andere Kategorie fällt) sowie für Marktlokationen, die nach Modul 1 und/oder 3 der Festlegungen zu Netzentgelten bei Anwendung der netzorientierten Steuerung von steuerbaren Verbrauchseinrichtungen und steuerbaren Netzanschlüssen nach § 14a EnWG gem. Festlegungen BK6-22-300 und BK8-22/010-A abgerechnet werden Arbeitspreis|€/kWh|X|--|X|X|X|X|
|1-02-0-003⁹|Grundpreis-/ Arbeitspreissystem Marktlokation der Kategorie steuerbare Speicherheizung, insbesondere nach § 14a EnWG Arbeitspreis|€/kWh|X|--|X|X|X|X|
|1-02-0-004⁹|Grundpreis-/ Arbeitspreissystem Marktlokation der Kategorie steuerbare Wärmepumpe, insbesondere nach § 14a EnWG Arbeitspreis|€/kWh|X|--|X|X|X|X|
|1-02-0-005|Grundpreis-/ Arbeitspreissystem Marktlokation der Kategorie öffentlicher Straßenbeleuchtung Arbeitspreis|€/kWh|X|--|X|X|X|X|
|1-02-0-006⁹|Grundpreis-/ Arbeitspreissystem Marktlokationen der Kategorie steuerbare Elektromobilität, insbesondere nach § 14a EnWG Arbeitspreis|€/kWh|X|--|X|X|X|X|
|1-02-0-007⁹|Grundpreis-/ Arbeitspreissystem Marktlokationen der Kategorie steuerbare Verbrauchseinrichtungen nach § 14a EnWG, für die es keine genauer spezifizierte Artikel-ID gibt Arbeitspreis|€/kWh|X|--|X|X|X|X|
|1-02-0-008⁹|Grundpreis-/ Arbeitspreissystem Marktlokation der Kategorie steuerbare Speicherheizung, insbesondere nach § 14a EnWG Grundpreis|€/Tag|X|--|X|X|X|X|
|1-02-0-009⁹|Grundpreis-/ Arbeitspreissystem Marktlokation der Kategorie steuerbare Wärmepumpe, insbesondere nach § 14a EnWG Grundpreis|€/Tag|X|--|X|X|X|X|


Version: 5.6                                                        30.09.2025                                                        Seite 18 von 60

Version: 5.6                                                        30.09.2025                                                        Seite 18 von 60

Codeliste der Artikelnummern und Artikel-ID

![edi@energy. Datenformate Strom & Gas](wvou)

|ID|Bezeichnung|Einheit|UTILMD<br/>Codever-wendung|UTILMD<br/>Preis-angabe|PRICAT<br/>Codever-wendung|PRICAT<br/>Preis-angabe|INVOIC<br/>Codever-wendung|INVOIC<br/>Preis-angabe|
|-|-|-|-|-|-|-|-|-|
|1-02-0-010⁹|Grundpreis-/ Arbeitspreissystem Marktlokationen der Kategorie steuerbare Elektromobilität, insbesondere nach § 14a EnWG Grundpreis|€/Tag|X|--|X|X|X|X|
|1-02-0-011⁹|Grundpreis-/ Arbeitspreissystem Marktlokation der Kategorie steuerbare Speicherheizung mit erweiterter Steuerbarkeit, insbesondere nach § 14a EnWG Arbeitspreis|€/kWh|X|--|X|X|X|X|
|1-02-0-012⁹|Grundpreis-/ Arbeitspreissystem Marktlokation der Kategorie steuerbare Wärmepumpe mit erweiterter Steuerbarkeit, insbesondere nach § 14a EnWG Arbeitspreis|€/kWh|X|--|X|X|X|X|
|1-02-0-013⁹|Grundpreis-/ Arbeitspreissystem Marktlokationen der Kategorie steuerbare Elektromobilität mit erweiterter Steuerbarkeit, insbesondere nach § 14a EnWG Arbeitspreis|€/kWh|X|--|X|X|X|X|
|1-02-0-014⁹|Grundpreis-/ Arbeitspreissystem Marktlokationen der Kategorie steuerbare Verbrauchseinrichtungen nach § 14a EnWG, für die es keine genauer spezifizierte Artikel-ID gibt Grundpreis|€/Tag|X|--|X|X|X|X|
|1-02-0-015¹⁰|Grundpreis-/ Arbeitspreissystem Pauschale Reduzierung nach Modul 1 der Festlegungen zu Netzentgelten bei Anwendung der netzorientierten Steuerung von steuerbaren Verbrauchseinrichtungen und steuerbaren Netzanschlüssen nach § 14a EnWG gem. Festlegungen BK6-22-300 und BK8-22/010-A|€/Tag|X|--|X|X|X|X|
|1-02-0-016¹⁰|Grundpreis-/ Arbeitspreissystem Marktlokation nach Modul 2 der Festlegungen zu Netzentgelten bei Anwendung der netzorientierten Steuerung von steuerbaren Verbrauchseinrichtungen und steuerbaren Netzanschlüssen nach § 14a EnWG gem. Festlegungen BK6-22-300 und BK8-22/010-A Arbeitspreis|€/kWh|X|--|X|X|X|X|






Seite 19 von 60

Version: 5.6
30.09.2025

Codeliste der Artikelnummern und Artikel-ID

![edi@energy. Datenformate Strom & Gas](oadu)

|ID|Bezeichnung|Einheit|UTILMD<br/>Codever-wendung|UTILMD<br/>Preis-angabe|PRICAT<br/>Codever-wendung|PRICAT<br/>Preis-angabe|INVOIC<br/>Codever-wendung|INVOIC<br/>Preis-angabe|
|-|-|-|-|-|-|-|-|-|
|1-02-0-017¹⁰|Grundpreis-/ Arbeitspreissystem Marktlokation nach Modul 3 der Festlegungen zu Netzentgelten bei Anwendung der netzorientierten Steuerung von steuerbaren Verbrauchseinrichtungen und steuerbaren Netzanschlüssen nach § 14a EnWG gem. Festlegungen BK6-22-300 und BK8-22/010-A Arbeitspreis HT|€/kWh|X|--|X|X|X|X|
|1-02-0-018¹⁰|Grundpreis-/ Arbeitspreissystem Marktlokation nach Modul 3 der Festlegungen zu Netzentgelten bei Anwendung der netzorientierten Steuerung von steuerbaren Verbrauchseinrichtungen und steuerbaren Netzanschlüssen nach § 14a EnWG gem. Festlegungen BK6-22-300 und BK8-22/010-A Arbeitspreis NT|€/kWh|X|--|X|X|X|X|


Version: 5.6                                       30.09.2025                                       Seite 20 von 60

Codeliste der Artikelnummern und Artikel-ID

![edi@energy logo](uptz)

## **3.1.3   Entgelte des Monatsleistungspreissystems für die Sparte Strom**

|ID|Bezeichnung|Einheit|UTILMD<br/>Codever-wendung|UTILMD<br/>Preis-angabe|PRICAT<br/>Codever-wendung|PRICAT<br/>Preis-angabe|INVOIC<br/>Codever-wendung|INVOIC<br/>Preis-angabe|
|-|-|-|-|-|-|-|-|-|
|1-03-1|Monatsleistungspreissystem Höchstspannung||X|--|--|--|--|--|
|1-03-1-001|Monatsleistungspreissystem Höchstspannung Leistungspreis für Monate mit 28 Tagen|€/(kW\*Tag)|--|--|X|X|X|X|
|1-03-1-002|Monatsleistungspreissystem Höchstspannung Leistungspreis für Monate mit 29 Tagen|€/(kW\*Tag)|--|--|X|X|X|X|
|1-03-1-003|Monatsleistungspreissystem Höchstspannung Leistungspreis für Monate mit 30 Tagen|€/(kW\*Tag)|--|--|X|X|X|X|
|1-03-1-004|Monatsleistungspreissystem Höchstspannung Leistungspreis für Monate mit 31 Tagen|€/(kW\*Tag)|--|--|X|X|X|X|
|1-03-1-005|Monatsleistungspreissystem Höchstspannung Arbeitspreis|€/kWh|--|--|X|X|X|X|
|1-03-2|Monatsleistungspreissystem Umspannung Höchst-/Hochspannung||X|--|--|--|--|--|
|1-03-2-001|Monatsleistungspreissystem Umspannung Höchst-/Hochspannung Leistungspreis für Monate mit 28 Tagen|€/(kW\*Tag)|--|--|X|X|X|X|
|1-03-2-002|Monatsleistungspreissystem Umspannung Höchst-/Hochspannung Leistungspreis für Monate mit 29 Tagen|€/(kW\*Tag)|--|--|X|X|X|X|
|1-03-2-003|Monatsleistungspreissystem Umspannung Höchst-/Hochspannung Leistungspreis für Monate mit 30 Tagen|€/(kW\*Tag)|--|--|X|X|X|X|
|1-03-2-004|Monatsleistungspreissystem Umspannung Höchst-/Hochspannung Leistungspreis für Monate mit 31 Tagen|€/(kW\*Tag)|--|--|X|X|X|X|
|1-03-2-005|Monatsleistungspreissystem Umspannung Höchst-/Hochspannung Arbeitspreis|€/kWh|--|--|X|X|X|X|


Version: 5.6

30.09.2025

Seite 21 von 60

Version: 5.6                                          30.09.2025                                          Seite 21 von 60

Codeliste der Artikelnummern und Artikel-ID

![edi@energy logo](gazp)

|ID|Bezeichnung|Einheit|UTILMD<br/>Codever-wendung|UTILMD<br/>Preis-angabe|PRICAT<br/>Codever-wendung|PRICAT<br/>Preis-angabe|INVOIC<br/>Codever-wendung|INVOIC<br/>Preis-angabe|
|-|-|-|-|-|-|-|-|-|
|1-03-3|Monatsleistungspreissystem Hochspannung||X|--|--|--|--|--|
|1-03-3-001|Monatsleistungspreissystem Hochspannung Leistungspreis für Monate mit 28 Tagen|€/(kW\*Tag)|--|--|X|X|X|X|
|1-03-3-002|Monatsleistungspreissystem Hochspannung Leistungspreis für Monate mit 29 Tagen|€/(kW\*Tag)|--|--|X|X|X|X|
|1-03-3-003|Monatsleistungspreissystem Hochspannung Leistungspreis für Monate mit 30 Tagen|€/(kW\*Tag)|--|--|X|X|X|X|
|1-03-3-004|Monatsleistungspreissystem Hochspannung Leistungspreis für Monate mit 31 Tagen|€/(kW\*Tag)|--|--|X|X|X|X|
|1-03-3-005|Monatsleistungspreissystem Hochspannung Arbeitspreis|€/kWh|--|--|X|X|X|X|
|1-03-4|Monatsleistungspreissystem Umspannung Hoch-/Mittelspannung||X|--|--|--|--|--|
|1-03-4-001|Monatsleistungspreissystem Umspannung Hoch-/Mittelspannung Leistungspreis für Monate mit 28 Tagen|€/(kW\*Tag)|--|--|X|X|X|X|
|1-03-4-002|Monatsleistungspreissystem Umspannung Hoch-/Mittelspannung Leistungspreis für Monate mit 29 Tagen|€/(kW\*Tag)|--|--|X|X|X|X|
|1-03-4-003|Monatsleistungspreissystem Umspannung Hoch-/Mittelspannung Leistungspreis für Monate mit 30 Tagen|€/(kW\*Tag)|--|--|X|X|X|X|
|1-03-4-004|Monatsleistungspreissystem Umspannung Hoch-/Mittelspannung Leistungspreis für Monate mit 31 Tagen|€/(kW\*Tag)|--|--|X|X|X|X|
|1-03-4-005|Monatsleistungspreissystem Umspannung Hoch-/Mittelspannung Arbeitspreis|€/kWh|--|--|X|X|X|X|


Version: 5.6

30.09.2025

Seite 22 von 60

Version: 5.6
30.09.2025
Seite 22 von 60

Codeliste der Artikelnummern und Artikel-ID

![edi@energy logo](wvwk)

|ID|Bezeichnung|Einheit|UTILMD<br/>Codever-wendung|UTILMD<br/>Preis-angabe|PRICAT<br/>Codever-wendung|PRICAT<br/>Preis-angabe|INVOIC<br/>Codever-wendung|INVOIC<br/>Preis-angabe|
|-|-|-|-|-|-|-|-|-|
|1-03-5|Monatsleistungspreissystem Mittelspannung||X|--|--|--|--|--|
|1-03-5-001|Monatsleistungspreissystem Mittelspannung Leistungspreis für Monate mit 28 Tagen|€/(kW\*Tag)|--|--|X|X|X|X|
|1-03-5-002|Monatsleistungspreissystem Mittelspannung Leistungspreis für Monate mit 29 Tagen|€/(kW\*Tag)|--|--|X|X|X|X|
|1-03-5-003|Monatsleistungspreissystem Mittelspannung Leistungspreis für Monate mit 30 Tagen|€/(kW\*Tag)|--|--|X|X|X|X|
|1-03-5-004|Monatsleistungspreissystem Mittelspannung Leistungspreis für Monate mit 31 Tagen|€/(kW\*Tag)|--|--|X|X|X|X|
|1-03-5-005|Monatsleistungspreissystem Mittelspannung Arbeitspreis|€/kWh|--|--|X|X|X|X|
|1-03-6|Monatsleistungspreissystem Umspannung Mittel-/Niederspannung||X|--|--|--|--|--|
|1-03-6-001|Monatsleistungspreissystem Umspannung Mittel-/Niederspannung Leistungspreis für Monate mit 28 Tagen|€/(kW\*Tag)|--|--|X|X|X|X|
|1-03-6-002|Monatsleistungspreissystem Umspannung Mittel-/Niederspannung Leistungspreis für Monate mit 29 Tagen|€/(kW\*Tag)|--|--|X|X|X|X|
|1-03-6-003|Monatsleistungspreissystem Umspannung Mittel-/Niederspannung Leistungspreis für Monate mit 30 Tagen|€/(kW\*Tag)|--|--|X|X|X|X|
|1-03-6-004|Monatsleistungspreissystem Umspannung Mittel-/Niederspannung Leistungspreis für Monate mit 31 Tagen|€/(kW\*Tag)|--|--|X|X|X|X|
|1-03-6-005|Monatsleistungspreissystem Umspannung Mittel-/Niederspannung Arbeitspreis|€/kWh|--|--|X|X|X|X|


Version: 5.6

30.09.2025

Seite 23 von 60

Version: 5.6
30.09.2025
Seite 23 von 60

Codeliste der Artikelnummern und Artikel-ID

![edi@energy. Datenformate Strom & Gas](zwdd)

|ID|Bezeichnung|Einheit|UTILMD<br/>Codever-wendung|UTILMD<br/>Preis-angabe|PRICAT<br/>Codever-wendung|PRICAT<br/>Preis-angabe|INVOIC<br/>Codever-wendung|INVOIC<br/>Preis-angabe|
|-|-|-|-|-|-|-|-|-|
|1-03-7|Monatsleistungspreissystem Niederspannung||X|--|--|--|--|--|
|1-03-7-001|Monatsleistungspreissystem Niederspannung Leistungspreis für Monate mit 28 Tagen|€/(kW\*Tag)|--|--|X|X|X|X|
|1-03-7-002|Monatsleistungspreissystem Niederspannung Leistungspreis für Monate mit 29 Tagen|€/(kW\*Tag)|--|--|X|X|X|X|
|1-03-7-003|Monatsleistungspreissystem Niederspannung Leistungspreis für Monate mit 30 Tagen|€/(kW\*Tag)|--|--|X|X|X|X|
|1-03-7-004|Monatsleistungspreissystem Niederspannung Leistungspreis für Monate mit 31 Tagen|€/(kW\*Tag)|--|--|X|X|X|X|
|1-03-7-005|Monatsleistungspreissystem Niederspannung Arbeitspreis|€/kWh|--|--|X|X|X|X|
|1-03-8¹⁰|Monatsleistungspreissystem Umspannung Mittel-/Niederspannung<br/>Pauschale Reduzierung nach Modul 1 der Festlegungen zu Netzentgelten<br/>bei Anwendung der netzorientierten Steuerung von steuerbaren<br/>Verbrauchseinrichtungen und steuerbaren Netzanschlüssen nach § 14a<br/>EnWG gem. Festlegungen BK6-22-300 und BK8-22/010-A||X|--|--|--|--|--|
|1-03-8-001¹⁰|Monatsleistungspreissystem Umspannung Mittel-/Niederspannung<br/>Pauschale Reduzierung nach Modul 1 der Festlegungen zu Netzentgelten<br/>bei Anwendung der netzorientierten Steuerung von steuerbaren<br/>Verbrauchseinrichtungen und steuerbaren Netzanschlüssen nach § 14a<br/>EnWG gem. Festlegungen BK6-22-300 und BK8-22/010-A<br/>für Monate mit 28 Tagen|€/Tag|--|--|X|X|X|X|


Version: 5.6

30.09.2025

Seite 24 von 60

Codeliste der Artikelnummern und Artikel-ID

![edi@energy. Datenformate Strom & Gas](brwf)

|ID|Bezeichnung|Einheit|UTILMD<br/>Codever-wendung|UTILMD<br/>Preis-angabe|PRICAT<br/>Codever-wendung|PRICAT<br/>Preis-angabe|INVOIC<br/>Codever-wendung|INVOIC<br/>Preis-angabe|
|-|-|-|-|-|-|-|-|-|
|1-03-8-002¹⁰|Monatsleistungspreissystem Umspannung Mittel-/Niederspannung<br/>Pauschale Reduzierung nach Modul 1 der Festlegungen zu Netzentgelten<br/>bei Anwendung der netzorientierten Steuerung von steuerbaren<br/>Verbrauchseinrichtungen und steuerbaren Netzanschlüssen nach § 14a<br/>EnWG gem. Festlegungen BK6-22-300 und BK8-22/010-A<br/>für Monate mit 29 Tagen|€/Tag|--|--|X|X|X|X|
|1-03-8-003¹⁰|Monatsleistungspreissystem Umspannung Mittel-/Niederspannung<br/>Pauschale Reduzierung nach Modul 1 der Festlegungen zu Netzentgelten<br/>bei Anwendung der netzorientierten Steuerung von steuerbaren<br/>Verbrauchseinrichtungen und steuerbaren Netzanschlüssen nach § 14a<br/>EnWG gem. Festlegungen BK6-22-300 und BK8-22/010-A<br/>für Monate mit 30 Tagen|€/Tag|--|--|X|X|X|X|
|1-03-8-004¹⁰|Monatsleistungspreissystem Umspannung Mittel-/Niederspannung<br/>Pauschale Reduzierung nach Modul 1 der Festlegungen zu Netzentgelten<br/>bei Anwendung der netzorientierten Steuerung von steuerbaren<br/>Verbrauchseinrichtungen und steuerbaren Netzanschlüssen nach § 14a<br/>EnWG gem. Festlegungen BK6-22-300 und BK8-22/010-A<br/>für Monate mit 31 Tagen|€/Tag|--|--|X|X|X|X|
|1-03-9¹⁰|Monatsleistungspreissystem Niederspannung<br/>Pauschale Reduzierung nach Modul 1 der Festlegungen zu Netzentgelten<br/>bei Anwendung der netzorientierten Steuerung von steuerbaren<br/>Verbrauchseinrichtungen und steuerbaren Netzanschlüssen nach § 14a<br/>EnWG gem. Festlegungen BK6-22-300 und BK8-22/010-A||X|--|--|--|--|--|


Version: 5.6

30.09.2025

Seite 25 von 60

Version: 5.6
30.09.2025
Seite 25 von 60

Codeliste der Artikelnummern und Artikel-ID

![edi@energy logo](klpd)

|ID|Bezeichnung|Einheit|UTILMD<br/>Codever-wendung|UTILMD<br/>Preis-angabe|PRICAT<br/>Codever-wendung|PRICAT<br/>Preis-angabe|INVOIC<br/>Codever-wendung|INVOIC<br/>Preis-angabe|
|-|-|-|-|-|-|-|-|-|
|1-03-9-001¹⁰|Monatsleistungspreissystem Niederspannung<br/>Pauschale Reduzierung nach Modul 1 der Festlegungen zu Netzentgelten<br/>bei Anwendung der netzorientierten Steuerung von steuerbaren<br/>Verbrauchseinrichtungen und steuerbaren Netzanschlüssen nach § 14a<br/>EnWG gem. Festlegungen BK6-22-300 und BK8-22/010-A<br/>für Monate mit 28 Tagen|€/Tag|--|--|X|X|X|X|
|1-03-9-002¹⁰|Monatsleistungspreissystem Niederspannung<br/>Pauschale Reduzierung nach Modul 1 der Festlegungen zu Netzentgelten<br/>bei Anwendung der netzorientierten Steuerung von steuerbaren<br/>Verbrauchseinrichtungen und steuerbaren Netzanschlüssen nach § 14a<br/>EnWG gem. Festlegungen BK6-22-300 und BK8-22/010-A<br/>für Monate mit 29 Tagen|€/Tag|--|--|X|X|X|X|
|1-03-9-003¹⁰|Monatsleistungspreissystem Niederspannung<br/>Pauschale Reduzierung nach Modul 1 der Festlegungen zu Netzentgelten<br/>bei Anwendung der netzorientierten Steuerung von steuerbaren<br/>Verbrauchseinrichtungen und steuerbaren Netzanschlüssen nach § 14a<br/>EnWG gem. Festlegungen BK6-22-300 und BK8-22/010-A<br/>für Monate mit 30 Tagen|€/Tag|--|--|X|X|X|X|
|1-03-9-004¹⁰|Monatsleistungspreissystem Niederspannung<br/>Pauschale Reduzierung nach Modul 1 der Festlegungen zu Netzentgelten<br/>bei Anwendung der netzorientierten Steuerung von steuerbaren<br/>Verbrauchseinrichtungen und steuerbaren Netzanschlüssen nach § 14a<br/>EnWG gem. Festlegungen BK6-22-300 und BK8-22/010-A<br/>für Monate mit 31 Tagen|€/Tag|--|--|X|X|X|X|


Version: 5.6

30.09.2025

Seite 26 von 60

Version: 5.6
30.09.2025
Seite 26 von 60

Codeliste der Artikelnummern und Artikel-ID

![edi@energy. Datenformate Strom & Gas](meuy)

## **3.1.4   Entgelte des Stromspeichers gemäß § 19 Abs. 4 StromNEV für die Sparte Strom**

|ID|Bezeichnung|Einheit|UTILMD<br/>Codever-wendung|UTILMD<br/>Preis-angabe|PRICAT<br/>Codever-wendung|PRICAT<br/>Preis-angabe|INVOIC<br/>Codever-wendung|INVOIC<br/>Preis-angabe|
|-|-|-|-|-|-|-|-|-|
|1-04-1-001|Stromspeicherentgelte Höchstspannung Leistungspreis|€/(kW\*Tag)|X|--|X|X|X|X|
|1-04-2-001|Stromspeicherentgelte Umspannung Höchst-/Hochspannung Leistungspreis|€/(kW\*Tag)|X|--|X|X|X|X|
|1-04-3-001|Stromspeicherentgelte Hochspannung Leistungspreis|€/(kW\*Tag)|X|--|X|X|X|X|
|1-04-4-001|Stromspeicherentgelte Umspannung Hoch-/Mittelspannung Leistungspreis|€/(kW\*Tag)|X|--|X|X|X|X|
|1-04-5-001|Stromspeicherentgelte Mittelspannung Leistungspreis|€/(kW\*Tag)|X|--|X|X|X|X|
|1-04-6-001|Stromspeicherentgelte Umspannung Mittel-/Niederspannung Leistungspreis|€/(kW\*Tag)|X|--|X|X|X|X|
|1-04-7-001|Stromspeicherentgelte Niederspannung Leistungspreis|€/(kW\*Tag)|X|--|X|X|X|X|






Seite 27 von 60

Version: 5.6
30.09.2025

Codeliste der Artikelnummern und Artikel-ID

![edi@energy logo](vcks)

## **3.1.5    Netzreservekapazität für die Sparte Strom**

|ID|Bezeichnung|Einheit|UTILMD<br/>Codever-wendung|UTILMD<br/>Preis-angabe|PRICAT<br/>Codever-wendung|PRICAT<br/>Preis-angabe|INVOIC<br/>Codever-wendung|INVOIC<br/>Preis-angabe|
|-|-|-|-|-|-|-|-|-|
|1-05-1|Höchstspannung||X|--|--|--|--|--|
|1-05-1-001|Netzreservekapazität Höchstspannung bis 200 h/a|€/(kW\*Tag)|--|--|X|X|X|X|
|1-05-1-002|Netzreservekapazität Höchstspannung über 200 h/a bis 400 h/a|€/(kW\*Tag)|--|--|X|X|X|X|
|1-05-1-003|Netzreservekapazität Höchstspannung über 400 h/a bis 600 h/a|€/(kW\*Tag)|--|--|X|X|X|X|
|1-05-2|Umspannung Höchst-/Hochspannung||X|--|--|--|--|--|
|1-05-2-001|Netzreservekapazität Umspannung Höchst-/Hochspannung bis 200 h/a|€/(kW\*Tag)|--|--|X|X|X|X|
|1-05-2-002|Netzreservekapazität Umspannung Höchst-/Hochspannung über 200 h/a bis 400 h/a|€/(kW\*Tag)|--|--|X|X|X|X|
|1-05-2-003|Netzreservekapazität Umspannung Höchst-/Hochspannung über 400 h/a bis 600 h/a|€/(kW\*Tag)|--|--|X|X|X|X|
|1-05-3|Hochspannung||X|--|--|--|--|--|
|1-05-3-001|Netzreservekapazität Hochspannung bis 200 h/a|€/(kW\*Tag)|--|--|X|X|X|X|
|1-05-3-002|Netzreservekapazität Hochspannung über 200 h/a bis 400 h/a|€/(kW\*Tag)|--|--|X|X|X|X|
|1-05-3-003|Netzreservekapazität Hochspannung über 400 h/a bis 600 h/a|€/(kW\*Tag)|--|--|X|X|X|X|
|1-05-4|Umspannung Hoch-/Mittelspannung||X|--|--|--|--|--|
|1-05-4-001|Netzreservekapazität Umspannung Hoch-/Mittelspannung bis 200 h/a|€/(kW\*Tag)|--|--|X|X|X|X|
|1-05-4-002|Netzreservekapazität Umspannung Hoch-/Mittelspannung über 200 h/a bis 400 h/a|€/(kW\*Tag)|--|--|X|X|X|X|
|1-05-4-003|Netzreservekapazität Umspannung Hoch-/Mittelspannung über 400 h/a bis 600 h/a|€/(kW\*Tag)|--|--|X|X|X|X|


Version: 5.6                                             30.09.2025                                             Seite 28 von 60

Codeliste der Artikelnummern und Artikel-ID

![edi@energy. Datenformate Strom & Gas](ozvp)

|ID|Bezeichnung|Einheit|UTILMD<br/>Codever-wendung|UTILMD<br/>Preis-angabe|PRICAT<br/>Codever-wendung|PRICAT<br/>Preis-angabe|INVOIC<br/>Codever-wendung|INVOIC<br/>Preis-angabe|
|-|-|-|-|-|-|-|-|-|
|1-05-5|Mittelspannung||X|--|--|--|--|--|
|1-05-5-001|Netzreservekapazität Mittelspannung bis 200 h/a|€/(kW\*Tag)|--|--|X|X|X|X|
|1-05-5-002|Netzreservekapazität Mittelspannung über 200 h/a bis 400 h/a|€/(kW\*Tag)|--|--|X|X|X|X|
|1-05-5-003|Netzreservekapazität Mittelspannung über 400 h/a bis 600 h/a|€/(kW\*Tag)|--|--|X|X|X|X|
|1-05-6|Umspannung Mittel-/Niederspannung||X|--|--|--|--|--|
|1-05-6-001|Netzreservekapazität Umspannung Mittel-/Niederspannung bis 200 h/a|€/(kW\*Tag)|--|--|X|X|X|X|
|1-05-6-002|Netzreservekapazität Umspannung Mittel-/Niederspannung über 200 h/a bis 400 h/a|€/(kW\*Tag)|--|--|X|X|X|X|
|1-05-6-003|Netzreservekapazität Umspannung Mittel-/Niederspannung über 400 h/a bis 600 h/a|€/(kW\*Tag)|--|--|X|X|X|X|
|1-05-7|Niederspannung||X|--|--|--|--|--|
|1-05-7-001|Netzreservekapazität Niederspannung bis 200 h/a|€/(kW\*Tag)|--|--|X|X|X|X|
|1-05-7-002|Netzreservekapazität Niederspannung über 200 h/a bis 400 h/a|€/(kW\*Tag)|--|--|X|X|X|X|
|1-05-7-003|Netzreservekapazität Niederspannung über 400 h/a bis 600 h/a|€/(kW\*Tag)|--|--|X|X|X|X|


Version: 5.6                                                                    30.09.2025                                                                    Seite 29 von 60

Version: 5.6                                                                    30.09.2025                                                                    Seite 29 von 60

Codeliste der Artikelnummern und Artikel-ID

![edi@energy. logo](gufb)

## **3.1.6    Entgelte des Messstellenbetriebs bei kME für die Sparte Strom**

Hinweis: Sobald mME bzw. iMS verbaut ist, erfolgt die Abrechnung über den MSB

|ID|Bezeichnung|Einheit|UTILMD<br/>Codever- wendung|UTILMD<br/>Preis- angabe|PRICAT<br/>Codever- wendung|PRICAT<br/>Preis- angabe|INVOIC<br/>Codever- wendung|INVOIC<br/>Preis- angabe|
|-|-|-|-|-|-|-|-|-|
|1-06-1-001|Messstellenbetrieb bei kME, Höchstspannung, kME mit registrierender Last-<br/>/Einspeisemessung|€/Tag|X|--|X|X|X|X|
|1-06-1-002|Messstellenbetrieb bei kME, Höchstspannung, Wandlersatz für<br/>Messstellenbetrieb bei kME|€/Tag|X|--|X|X|X|X|
|1-06-3-001|Messstellenbetrieb bei kME, Hochspannung, kME mit registrierender Last-<br/>/Einspeisemessung|€/Tag|X|--|X|X|X|X|
|1-06-3-002|Messstellenbetrieb bei kME, Hochspannung, Wandlersatz für<br/>Messstellenbetrieb bei kME|€/Tag|X|--|X|X|X|X|
|1-06-5-001|Messstellenbetrieb bei kME, Mittelspannung, kME mit registrierender Last-<br/>/Einspeisemessung|€/Tag|X|--|X|X|X|X|
|1-06-5-002|Messstellenbetrieb bei kME, Mittelspannung, Wandlersatz für<br/>Messstellenbetrieb bei kME|€/Tag|X|--|X|X|X|X|
|1-06-7-001|Messstellenbetrieb bei kME, Niederspannung, kME mit registrierender Last-<br/>/Einspeisemessung|€/Tag|X|--|X|X|X|X|
|1-06-7-002|Messstellenbetrieb bei kME, Niederspannung, Wandlersatz für<br/>Messstellenbetrieb bei kME|€/Tag|X|--|X|X|X|X|
|1-06-7-003|Messstellenbetrieb bei kME, Niederspannung, Schaltgerät oder<br/>Rundsteuerempfänger|€/Tag|X|--|X|X|X|X|
|1-06-7-004|Messstellenbetrieb bei kME, Niederspannung, bei jährlicher Ablesung kME<br/>Einrichtungszähler Eintarif|€/Tag|X|--|X|X|X|X|


Version: 5.6

30.09.2025

Seite 30 von 60

Version: 5.6
30.09.2025
Seite 30 von 60

Codeliste der Artikelnummern und Artikel-ID

![edi@energy. Datenformate Strom & Gas](vbfq)

|ID|Bezeichnung|Einheit|UTILMD<br/>Codever-wendung|UTILMD<br/>Preis-angabe|PRICAT<br/>Codever-wendung|PRICAT<br/>Preis-angabe|INVOIC<br/>Codever-wendung|INVOIC<br/>Preis-angabe|
|-|-|-|-|-|-|-|-|-|
|1-06-7-005|Messstellenbetrieb bei kME, Niederspannung, bei jährlicher Ablesung kME Einrichtungszähler Zweitarif|€/Tag|X|--|X|X|X|X|
|1-06-7-006|Messstellenbetrieb bei kME, Niederspannung, bei jährlicher Ablesung kME Zweirichtungszähler Eintarif|€/Tag|X|--|X|X|X|X|
|1-06-7-007|Messstellenbetrieb bei kME, Niederspannung, bei jährlicher Ablesung kME Zweirichtungszähler Zweitarif|€/Tag|X|--|X|X|X|X|
|1-06-7-008|Messstellenbetrieb bei kME, Niederspannung, bei jährlicher Ablesung kME Mehrtarifzähler|€/Tag|X|--|X|X|X|X|
|1-06-7-009|Messstellenbetrieb bei kME, Niederspannung, bei jährlicher Ablesung kME Prepaymentzähler|€/Tag|X|--|X|X|X|X|
|1-06-7-010|Messstellenbetrieb bei kME, Niederspannung, bei jährlicher Ablesung kME Maximumzähler|€/Tag|X|--|X|X|X|X|
|1-06-7-011|Messstellenbetrieb bei kME, Niederspannung, bei jährlicher Ablesung kME EDL21 Zähler|€/Tag|X|--|X|X|X|X|
|1-06-7-012|Messstellenbetrieb bei kME, Niederspannung, bei halbjährlicher Ablesung kME Einrichtungszähler Eintarif|€/Tag|X|--|X|X|X|X|
|1-06-7-013|Messstellenbetrieb bei kME, Niederspannung, bei halbjährlicher Ablesung kME Einrichtungszähler Zweitarif|€/Tag|X|--|X|X|X|X|
|1-06-7-014|Messstellenbetrieb bei kME, Niederspannung, bei halbjährlicher Ablesung kME Zweirichtungszähler Eintarif|€/Tag|X|--|X|X|X|X|
|1-06-7-015|Messstellenbetrieb bei kME, Niederspannung, bei halbjährlicher Ablesung kME Zweirichtungszähler Zweitarif|€/Tag|X|--|X|X|X|X|
|1-06-7-016|Messstellenbetrieb bei kME, Niederspannung, bei halbjährlicher Ablesung kME Mehrtarifzähler|€/Tag|X|--|X|X|X|X|


Version: 5.6                                                                    30.09.2025                                                                    Seite 31 von 60

Codeliste der Artikelnummern und Artikel-ID

![edi@energy. Datenformate Strom & Gas](nsij)

|ID|Bezeichnung|Einheit|UTILMD<br/>Codever-wendung|UTILMD<br/>Preis-angabe|PRICAT<br/>Codever-wendung|PRICAT<br/>Preis-angabe|INVOIC<br/>Codever-wendung|INVOIC<br/>Preis-angabe|
|-|-|-|-|-|-|-|-|-|
|1-06-7-017|Messstellenbetrieb bei kME, Niederspannung, bei halbjährlicher Ablesung kME Prepaymentzähler|€/Tag|X|--|X|X|X|X|
|1-06-7-018|Messstellenbetrieb bei kME, Niederspannung, bei halbjährlicher Ablesung kME Maximumzähler|€/Tag|X|--|X|X|X|X|
|1-06-7-019|Messstellenbetrieb bei kME, Niederspannung, bei halbjährlicher Ablesung kME EDL21 Zähler|€/Tag|X|--|X|X|X|X|
|1-06-7-020|Messstellenbetrieb bei kME, Niederspannung, bei vierteljährlicher Ablesung kME Einrichtungszähler Eintarif|€/Tag|X|--|X|X|X|X|
|1-06-7-021|Messstellenbetrieb bei kME, Niederspannung, bei vierteljährlicher Ablesung kME Einrichtungszähler Zweitarif|€/Tag|X|--|X|X|X|X|
|1-06-7-022|Messstellenbetrieb bei kME, Niederspannung, bei vierteljährlicher Ablesung kME Zweirichtungszähler Eintarif|€/Tag|X|--|X|X|X|X|
|1-06-7-023|Messstellenbetrieb bei kME, Niederspannung, bei vierteljährlicher Ablesung kME Zweirichtungszähler Zweitarif|€/Tag|X|--|X|X|X|X|
|1-06-7-024|Messstellenbetrieb bei kME, Niederspannung, bei vierteljährlicher Ablesung kME Mehrtarifzähler|€/Tag|X|--|X|X|X|X|
|1-06-7-025|Messstellenbetrieb bei kME, Niederspannung, bei vierteljährlicher Ablesung kME Prepaymentzähler|€/Tag|X|--|X|X|X|X|
|1-06-7-026|Messstellenbetrieb bei kME, Niederspannung, bei vierteljährlicher Ablesung kME Maximumzähler|€/Tag|X|--|X|X|X|X|
|1-06-7-027|Messstellenbetrieb bei kME, Niederspannung, bei vierteljährlicher Ablesung kME EDL21 Zähler|€/Tag|X|--|X|X|X|X|
|1-06-7-028|Messstellenbetrieb bei kME, Niederspannung, bei monatlicher Ablesung kME Einrichtungszähler Eintarif|€/Tag|X|--|X|X|X|X|


Version: 5.6                                                     30.09.2025                                                          Seite 32 von 60

Version: 5.6                                                                                30.09.2025                                                                              Seite 32 von 60

Codeliste der Artikelnummern und Artikel-ID

![edi@energy logo](udeh)

|ID|Bezeichnung|Einheit|UTILMD<br/>Codever-wendung|UTILMD<br/>Preis-angabe|PRICAT<br/>Codever-wendung|PRICAT<br/>Preis-angabe|INVOIC<br/>Codever-wendung|INVOIC<br/>Preis-angabe|
|-|-|-|-|-|-|-|-|-|
|1-06-7-029|Messstellenbetrieb bei kME, Niederspannung, bei monatlicher Ablesung kME<br/>Einrichtungszähler Zweitarif|€/Tag|X|--|X|X|X|X|
|1-06-7-030|Messstellenbetrieb bei kME, Niederspannung, bei monatlicher Ablesung kME<br/>Zweirichtungszähler Eintarif|€/Tag|X|--|X|X|X|X|
|1-06-7-031|Messstellenbetrieb bei kME, Niederspannung, bei monatlicher Ablesung kME<br/>Zweirichtungszähler Zweitarif|€/Tag|X|--|X|X|X|X|
|1-06-7-032|Messstellenbetrieb bei kME, Niederspannung, bei monatlicher Ablesung kME<br/>Mehrtarifzähler|€/Tag|X|--|X|X|X|X|
|1-06-7-033|Messstellenbetrieb bei kME, Niederspannung, bei monatlicher Ablesung kME<br/>Prepaymentzähler|€/Tag|X|--|X|X|X|X|
|1-06-7-034|Messstellenbetrieb bei kME, Niederspannung, bei monatlicher Ablesung kME<br/>Maximumzähler|€/Tag|X|--|X|X|X|X|
|1-06-7-035|Messstellenbetrieb bei kME, Niederspannung, bei monatlicher Ablesung kME<br/>EDL21 Zähler|€/Tag|X|--|X|X|X|X|
|1-06-0-036|Messstellenbetrieb bei kME, alle Spannungsebenen,<br/>Telekommunikationsanschluss durch NB (Fernauslesung)|€/Tag|X|--|X|X|X|X|
|1-06-0-037|Messstellenbetrieb bei kME, alle Spannungsebenen.<br/>Telekommunikationsanschluss durch AN (Fernauslesung)|€/Tag|X|--|X|X|X|X|
|1-06-0-038|Messstellenbetrieb bei kME, alle Spannungsebenen, manuelle vor Ort<br/>Ablesung bei kME mit registrierender Last-/Einspeisemessung|€/Vorgang|X|--|X|X|X|X|
|1-06-0-039|Entgelt Impulsweitergabe|€/Tag|X|--|X|X|X|X|


Version: 5.6                                                     30.09.2025                                                     Seite 33 von 60

Version: 5.6                                                     30.09.2025                                                     Seite 33 von 60

Codeliste der Artikelnummern und Artikel-ID

![edi@energy. Datenformate Strom & Gas](izwv)

## **3.1.7    Individuelle Netzentgelte für die Sparte Strom**

|ID|Bezeichnung|Einheit|UTILMD<br/>Codever- wendung|UTILMD<br/>Preis- angabe|PRICAT<br/>Codever- wendung|PRICAT<br/>Preis- angabe|INVOIC<br/>Codever- wendung|INVOIC<br/>Preis- angabe|
|-|-|-|-|-|-|-|-|-|
|1-07-1|Individuelle Netzentgelte nach § 19 Abs. 2 Satz 1 StromNEV||X|--|--|--|--|--|
|1-07-1-001|Individuelle Netzentgelte nach § 19 Abs. 2 Satz 1 StromNEV<br/>Jahresbenutzungsdauerstunden <2500 h/a Leistungspreis|€/(kW\*Tag)|--|--|X|--|X|X|
|1-07-1-002|Individuelle Netzentgelte nach § 19 Abs. 2 Satz 1 StromNEV<br/>Jahresbenutzungsdauerstunden <2500 h/a Arbeitspreis|€/kWh|--|--|X|--|X|X|
|1-07-1-003|Individuelle Netzentgelte nach § 19 Abs. 2 Satz 1 StromNEV<br/>Jahresbenutzungsdauerstunden >=2500 h/a Leistungspreis|€/(kW\*Tag)|--|--|X|--|X|X|
|1-07-1-004|Individuelle Netzentgelte nach § 19 Abs. 2 Satz 1 StromNEV<br/>Jahresbenutzungsdauerstunden >=2500 h/a Arbeitspreis|€/kWh|--|--|X|--|X|X|
|1-07-2|Individuelle Netzentgelte nach § 19 Abs. 2 Satz 2 StromNEV||X|--|--|--|--|--|
|1-07-2-001|Individuelle Netzentgelte nach § 19 Abs. 2 Satz 2 StromNEV<br/>Jahresbenutzungsdauerstunden <2500 h/a Leistungspreis|€/(kW\*Tag)|--|--|X|--|X|X|
|1-07-2-002|Individuelle Netzentgelte nach § 19 Abs. 2 Satz 2 StromNEV<br/>Jahresbenutzungsdauerstunden <2500 h/a Arbeitspreis|€/kWh|--|--|X|--|X|X|
|1-07-2-003|Individuelle Netzentgelte nach § 19 Abs. 2 Satz 2 StromNEV<br/>Jahresbenutzungsdauerstunden >=2500 h/a Leistungspreis|€/(kW\*Tag)|--|--|X|--|X|X|
|1-07-2-004|Individuelle Netzentgelte nach § 19 Abs. 2 Satz 2 StromNEV<br/>Jahresbenutzungsdauerstunden >=2500 h/a Arbeitspreis|€/kWh|--|--|X|--|X|X|
|1-07-3-001|Singulär genutzte Betriebsmittel nach § 19 Abs. 3 StromNEV|€/Tag|X|X|X|--|X|X|


Version: 5.6
30.09.2025
Seite 34 von 60

Codeliste der Artikelnummern und Artikel-ID

![edi@energy. Datenformate Strom & Gas](bwvf)

|ID|Bezeichnung|Einheit|UTILMD<br/>Codever- wendung|UTILMD<br/>Preis- angabe|PRICAT<br/>Codever- wendung|PRICAT<br/>Preis- angabe|INVOIC<br/>Codever- wendung|INVOIC<br/>Preis- angabe|
|-|-|-|-|-|-|-|-|-|
|1-07-4-001|Individuelle Netzentgelte nach § 19 StromNEV<br/><br/>Pauschale Reduzierung nach Modul 1 der Festlegungen zu Netzentgelten bei<br/>Anwendung der netzorientierten Steuerung von steuerbaren<br/>Verbrauchseinrichtungen und steuerbaren Netzanschlüssen nach § 14a<br/>EnWG gem. Festlegungen BK6-22-300 und BK8-22/010-A|€/Tag|X||X|X|X|X|


Version: 5.6

30.09.2025

Seite 35 von 60

Version: 5.6
30.09.2025
Seite 35 von 60

Codeliste der Artikelnummern und Artikel-ID

![edi@energy. Datenformate Strom & Gas](nrln)

## **3.1.8   Konzessionsabgaben für die Sparte Strom**

Bei den Konzessionsabgaben gibt es die Besonderheit, dass neben den fest vorgegebenen Artikel-ID auch die Netzbetreiber eigene Artikel-ID
vergeben können. Die fest vorgegebenen Artikel-ID werden genutzt, wenn der Höchstsatz der Konzessionsabgabe in Rechnung gestellt wird. In
diesem Fall (Verwendung des Höchstsatzes der Konzessionsabgabe nach Einwohner der Gemeinde) erfolgt keine Preisangabe in der PRICAT. Wenn
die Konzessionsabgaben nicht dem Höchstsatz (nach Einwohner der Gemeinde) entsprechen, werden vom Netzbetreiber eigene Artikel-ID
erzeugt. Der exakte Aufbau wird nachstehend beschrieben. In diesem Fall ist der individuelle Preis der Konzessionsabgabe in der PRICAT
anzugeben.

Der „Amtlicher Gemeindeschlüssel“ (AGS) ist ein 8-stelliger Schlüssel zur eindeutigen Identifizierung einer Gemeinde mit den Bestandteilen:

›   Bundesland (2 Stellen),

›   Regierungsbezirk (1 Stelle),

›   Kreis (2 Stellen) und

›   Gemeinde (3 Stellen).

Der „Amtlicher Regionalschlüssel“ (ARS) ist ein 12-stelliger Schlüssel zur eindeutigen Identifizierung einer Gemeinde mit den Bestandteilen:

›   Bundesland (2 Stellen),

›   Regierungsbezirk (1 Stelle),

›   Kreis (2 Stellen),

›   Gemeindeverband (4 Stellen) und

Version: 5.6

30.09.2025

Seite 36 von 60

Version: 5.6 30.09.2025 Seite 36 von 60

Codeliste der Artikelnummern und Artikel-ID

![edi@energy. Datenformate Strom & Gas](hpmn)

## ›   Gemeinde (3 Stellen).

Unter dem nachstehenden Link ist die Liste mit dem „Amtlichen Regionalschlüssel“ (ARS) zu finden:

https://www.destatis.de/DE/Themen/Laender-Regionen/Regionales/Gemeindeverzeichnis/Administrativ/Archiv/GVAuszugJ/31122020_Auszug_GV.html;jsessionid=6CB093665A7FBC61E660CB2C7BECBE0D.live712

Durch das Weglassen der Spalte für den Gemeindeverband (VB) wird aus dem ARS der AGS.

|Amtlicher Regionalschlüssel(ARS)<br/>Land|Amtlicher Regionalschlüssel(ARS)<br/>RB|Amtlicher Regionalschlüssel(ARS)<br/>Kreis|Amtlicher Regionalschlüssel(ARS)<br/>VB|Amtlicher Regionalschlüssel(ARS)<br/>Gem|
|-|-|-|-|-|


Z steht für die Zone. Die Zonen mit den Zonengrenzen in kWh/Jahr werden im Rahmen der Marktkommunikation über das elektronische Preisblatt (PRICAT) definiert.

Codes der Kundengruppen (KG)

|Kundengruppe|Code|
|-|-|
|reine Landwirtschaft|01|
|Landwirtschaft in Kombination mit Haushalt|02|
|Sonstige / keine gesonderte Kundengruppe|03|


Version: 5.6                                                 30.09.2025                                                 Seite 37 von 60

Codeliste der Artikelnummern und Artikel-ID

![edi@energy. Datenformate Strom & Gas](rdln)

|ID|Bezeichnung|Einheit|UTILMD<br/>Codever-wendung|UTILMD<br/>Preis-angabe|PRICAT<br/>Codever-wendung|PRICAT<br/>Preis-angabe|INVOIC<br/>Codever-wendung|INVOIC<br/>Preis-angabe|
|-|-|-|-|-|-|-|-|-|
|1-08-1-001|Höchstbetrag der Konzessionsabgabe für Entnahme von<br/>Marktlokationen von Tarifkunden in Schwachlastzeiten gem. § 2 Abs.<br/>2 Satz 1 a) KAV|€/kWh|X|--|X|--|X|X|
|1-08-1-AGS-KG|Gemeindespezifische, kundengruppenindividuelle Konzessionsabgabe<br/>für Entnahme von Marktlokationen von Tarifkunden in<br/>Schwachlastzeiten gem. § 2 Abs. 2 Satz 1 a) KAV<br/>AGS: Amtlicher Gemeindeschlüssel<br/>KG: Kundengruppe; siehe Tabelle oben|€/kWh|X|--|X|X|X|X|
|1-08-2-AGS-KG|Gruppenartikel-ID||X|--|--|--|--|--|
|1-08-2-AGS-KG-Z|Gemeindespezifische, kundengruppenindividuelle, gezonte<br/>Konzessionsabgabe für Entnahme von Marktlokationen von<br/>Tarifkunden in Schwachlastzeiten gem. § 2 Abs. 2 Satz 1 a) KAV<br/>AGS: Amtlicher Gemeindeschlüssel<br/>KG: Kundengruppe; siehe Tabelle oben<br/>Z: Nummer der Zone; mit 1 ≤ Z ≤ 9|€/kWh|--|--|X|X|X|X|
|1-08-3-001|Höchstbetrag der Konzessionsabgabe für Entnahme von<br/>Marktlokationen von Sondervertragskunden gem. § 2 Abs. 3 Satz 1<br/>KAV|€/kWh|X|--|X|--|X|X|
|1-08-3-AGS|Gemeindespezifische Konzessionsabgabe für Entnahme von<br/>Marktlokationen von Sondervertragskunden gem. § 2 Abs. 3 Satz 1<br/>KAV|€/kWh|X|--|X|X|X|X|
|1-08-4-001|Höchstbetrag der Konzessionsabgabe für Entnahme von<br/>Marktlokationen von Tarifkunden gem. § 2 Abs. 2 Satz 1b) KAV<br/>bis 25.000 Einwohner|€/kWh|X|--|X|--|X|X|


Version: 5.6 30.09.2025 Seite 38 von 60

Version: 5.6 30.09.2025 Seite 38 von 60

Codeliste der Artikelnummern und Artikel-ID

![edi@energy. Datenformate Strom & Gas](yfgu)

|ID|Bezeichnung|Einheit|UTILMD<br/>Codever-wendung|UTILMD<br/>Preis-angabe|PRICAT<br/>Codever-wendung|PRICAT<br/>Preis-angabe|INVOIC<br/>Codever-wendung|INVOIC<br/>Preis-angabe|
|-|-|-|-|-|-|-|-|-|
|1-08-4-002|Höchstbetrag der Konzessionsabgabe für Entnahme von<br/>Marktlokationen von Tarifkunden gem. § 2 Abs. 2 Satz 1b) KAV<br/>von 25.000 bis 100.000 Einwohner|€/kWh|X|--|X|--|X|X|
|1-08-4-003|Höchstbetrag der Konzessionsabgabe für Entnahme von<br/>Marktlokationen von Tarifkunden gem. § 2 Abs. 2 Satz 1b) KAV<br/>von 100.000 bis 500.000 Einwohner|€/kWh|X|--|X|--|X|X|
|1-08-4-004|Höchstbetrag der Konzessionsabgabe für Entnahme von<br/>Marktlokationen von Tarifkunden gem. § 2 Abs. 2 Satz 1b) KAV<br/>über 500.000 Einwohner|€/kWh|X|--|X|--|X|X|
|1-08-4-AGS-KG|Gemeindespezifische, kundengruppenindividuelle Konzessionsabgabe<br/>für Entnahme von Marktlokationen von Tarifkunden gem. § 2 Abs. 2<br/>Satz 1b) KAV<br/>AGS: Amtlicher Gemeindeschlüssel<br/>KG: Kundengruppe; siehe Tabelle oben|€/kWh|X|--|X|X|X|X|
|1-08-5-AGS-KG|Gruppenartikel-ID||X|--|--|--|--|--|
|1-08-5-AGS-KG-Z|Gemeindespezifische, kundengruppenindividuelle, gezonte<br/>Konzessionsabgabe für Entnahme von Marktlokationen von<br/>Tarifkunden gem. § 2 Abs. 2 Satz 1b) KAV<br/>AGS: Amtlicher Gemeindeschlüssel<br/>KG: Kundengruppe; siehe Tabelle oben<br/>Z: Nummer der Zone; mit 1 ≤ Z ≤ 9|€/kWh|--|--|X|X|X|X|
|1-08-6-001|Für Marktlokationen deren (Teil-)Menge von der Konzessionsabgabe<br/>befreit ist|€/kWh|--|--|X|--|SOR|X|


Version: 5.6 30.09.2025 Seite 39 von 60

Codeliste der Artikelnummern und Artikel-ID

![edi@energy. Datenformate Strom & Gas](vjcy)

## **3.1.9    Entgelte des Tagesleistungspreissystems für die Sparte Strom**

|ID|Bezeichnung|Einheit|UTILMD<br/>Codever-wendung|UTILMD<br/>Preis-angabe|PRICAT<br/>Codever-wendung|PRICAT<br/>Preis-angabe|INVOIC<br/>Codever-wendung|INVOIC<br/>Preis-angabe|
|-|-|-|-|-|-|-|-|-|
|1-09-1-001|Tagesleistungspreissystem Höchstspannung Leistungspreis|€/(kW\*Tag)|X|--|X|X|X|X|
|1-09-1-002|Tagesleistungspreissystem Höchstspannung Arbeitspreis|€/kWh|X|--|X|X|X|X|
|1-09-2-001|Tagesleistungspreissystem Umspannung Höchst-/Hochspannung<br/>Leistungspreis|€/(kW\*Tag)|X|--|X|X|X|X|
|1-09-2-002|Tagesleistungspreissystem Umspannung Höchst-/Hochspannung Arbeitspreis|€/kWh|X|--|X|X|X|X|
|1-09-3-001|Tagesleistungspreissystem Hochspannung Leistungspreis|€/(kW\*Tag)|X|--|X|X|X|X|
|1-09-3-002|Tagesleistungspreissystem Hochspannung Arbeitspreis|€/kWh|X|--|X|X|X|X|
|1-09-4-001|Tagesleistungspreissystem Umspannung Hoch-/Mittelspannung<br/>Leistungspreis|€/(kW\*Tag)|X|--|X|X|X|X|
|1-09-4-002|Tagesleistungspreissystem Umspannung Hoch-/Mittelspannung Arbeitspreis|€/kWh|X|--|X|X|X|X|
|1-09-5-001|Tagesleistungspreissystem Mittelspannung Leistungspreis|€/(kW\*Tag)|X|--|X|X|X|X|
|1-09-5-002|Tagesleistungspreissystem Mittelspannung Arbeitspreis|€/kWh|X|--|X|X|X|X|


Version: 5.6                                                                                               30.09.2025                                                                                               Seite 40 von 60

Version: 5.6                                                                                               30.09.2025                                                                                               Seite 40 von 60

Codeliste der Artikelnummern und Artikel-ID

![edi@enerGu. Datenformate Strom & Gas](gkxy)

## **3.1.10   Preisbestandteile, deren Höhe aufgrund gesetzlicher Vorgaben durch Dritte jährlich ermittelt und veröffentlicht werden für die Sparte**
## **Strom**

### **Regel für dieses Kapitel:**

In einer Rechnung des Rechnungstyps „SOR" können mehrere ggf. sogar alle Artikel-ID zu einer Gruppenartikel-ID vorhanden sein.

|ID|Bezeichnung|Einheit|UTILMD<br/>Codever- wendung|UTILMD<br/>Preis- angabe|PRICAT<br/>Codever- wendung|PRICAT<br/>Preis- angabe|INVOIC<br/>Codever- wendung|INVOIC<br/>Preis- angabe|
|-|-|-|-|-|-|-|-|-|
|1-10-1|Aufschläge aufgrund des § 26 KWKG||X|--|--|--|--|--|
|1-10-1-001|Aufschläge aufgrund des KWKG für nicht privilegierte Letztverbraucher|€/kWh|--|--|X|--|X|X|
|1-10-1-002|Für Marktlokationen deren (Teil-)Menge von dem Aufschlag des § 26 KWKG befreit ist|€/kWh|--|--|X|--|SOR|X|
|1-10-1-003¹²|100 % Privilegierung nach EnFG des Aufschlags aufgrund des § 26 KWKG|€/kWh|--|--|X|--|X|X|
|1-10-1-004¹²|80 % Privilegierung nach EnFG des Aufschlags aufgrund des § 26 KWKG|€/kWh|--|--|X|--|X|X|
|1-10-2|Aufschläge aufgrund der Offshore-Netzumlage nach § 17f EnWG||X|--|--|--|--|--|
|1-10-2-001|Aufschläge aufgrund der Offshore-Netzumlage für nicht privilegierte Letztverbraucher|€/kWh|--|--|X|--|X|X|
|1-10-2-002|Für Marktlokationen deren (Teil-)Menge von dem Aufschlag der Offshore-Netzumlage nach § 17f EnWG befreit ist|€/kWh|--|--|X|--|SOR|X|
|1-10-2-003¹²|100 % Privilegierung nach EnFG des Aufschlags aufgrund der Offshore-Netzumlage nach § 17f EnWG|€/kWh|--|--|X|--|X|X|


<sup>12</sup> Die Anwendbarkeit von § 22 EnFG ist abhängig von der beihilferechtlichen Genehmigung der EU-Kommission zum EnFG.

Version: 5.6                                                                                               30.09.2025                                                                                               <page_number>Seite 41 von 60</page_number>

Codeliste der Artikelnummern und Artikel-ID

![edi@energy. Datenformate Strom & Gas](szpp)

|ID|Bezeichnung|Einheit|UTILMD<br/>Codever-wendung|UTILMD<br/>Preis-angabe|PRICAT<br/>Codever-wendung|PRICAT<br/>Preis-angabe|INVOIC<br/>Codever-wendung|INVOIC<br/>Preis-angabe|
|-|-|-|-|-|-|-|-|-|
|1-10-2-004¹²|80 % Privilegierung nach EnFG des Aufschlags aufgrund der Offshore-Netzumlage nach § 17f EnWG|€/kWh|--|--|X|--|X|X|
|1-10-3-001¹³|Aufschläge aufgrund der Umlage für abschaltbare Lasten Letztverbrauch je Marktlokation|€/kWh|X|--|X|--|X|X|
|1-10-3-002¹³|Für Marktlokationen deren (Teil-)Menge von dem Aufschlag der Umlage für abschaltbare Lasten befreit ist|€/kWh|--|--|X|--|SOR|X|
|1-10-4|Aufschläge aufgrund individueller Netzentgelte nach § 19 StromNEV (bis 31.12.2024)<br/><br/>Aufschläge für besondere Netznutzung (ab 01.01.2025)||X|--|--|--|--|--|
|1-10-4-001|Aufschläge aufgrund individueller Netzentgelte nach § 19 StromNEV Letztverbrauchergruppe A (Strommengen von Letztverbrauchern für die jeweils ersten 1.000.000 kWh je Marktlokation) (bis 31.12.2024)<br/><br/>Aufschläge für besondere Netznutzung Letztverbrauchergruppe A (Strommengen von Letztverbrauchern für die jeweils ersten 1.000.000 kWh je Marktlokation) (ab 01.01.2025)|€/kWh|--|--|X|--|X|X|


13 Diese Artikel-ID darf nur für Gültigkeitszeiträume bis zum 1.1.2024, 00:00 Uhr in Preisblättern, Stammdaten und Rechnungen enthalten sein.

Version: 5.6

30.09.2025

Seite 42 von 60

Version: 5.6
30.09.2025
<page_number>Seite 42 von 60</page_number>

Codeliste der Artikelnummern und Artikel-ID

![edi@energy logo](muod)

|ID|Bezeichnung|Einheit|UTILMD<br/>Codever-wendung|UTILMD<br/>Preis-angabe|PRICAT<br/>Codever-wendung|PRICAT<br/>Preis-angabe|INVOIC<br/>Codever-wendung|INVOIC<br/>Preis-angabe|
|-|-|-|-|-|-|-|-|-|
|1-10-4-002|Aufschläge aufgrund individueller Netzentgelte nach § 19 StromNEV Letztverbrauchergruppe B (Letztverbraucher, deren Jahresverbrauch an einer Marktlokation 1.000.000 kWh übersteigt, zahlen zusätzlich für über 1.000.000 kWh hinausgehende Strombezüge eine § 19 StromNEV-Umlage) (bis 31.12.2024)<br/><br/>Aufschläge für besondere Netznutzung Letztverbrauchergruppe B (Letztverbraucher, deren Jahresverbrauch an einer Marktlokation 1.000.000 kWh übersteigt, zahlen zusätzlich für über 1.000.000 kWh hinausgehende Strombezüge eine § 19 StromNEVUmlage) (ab 01.01.2025)|€/kWh|--|--|X|--|X|X|
|1-10-4-003|Aufschläge aufgrund individueller Netzentgelte nach § 19 StromNEV Letztverbrauchergruppe C (Letztverbraucher, die dem produzierenden Gewerbe, dem schienengebundenen Verkehr oder der Eisenbahninfrastruktur zuzuordnen sind und deren Stromkosten im vorangegangenen Geschäftsjahr vier Prozent des Umsatzes überstiegen haben, zahlen für über 1.000.000 kWh hinausgehende Strombezüge eine § 19 StromNEV-Umlage)(bis 31.12.2024)<br/><br/>Aufschläge für besondere Netznutzung Letztverbrauchergruppe C (Letztverbraucher, die dem produzierenden Gewerbe, dem schienengebundenen Verkehr oder der Eisenbahninfrastruktur zuzuordnen sind und deren Stromkosten im vorangegangenen Geschäftsjahr vier Prozent des Umsatzes überstiegen haben, zahlen für über 1.000.000 kWh hinausgehende Strombezüge eine § 19 StromNEV-Umlage) (ab 01.01.2025)|€/kWh|--|--|X|--|X|X|


Version: 5.6

30.09.2025

Seite 43 von 60





Seite 43 von 60

Version: 5.6
30.09.2025

Codeliste der Artikelnummern und Artikel-ID

![edi@energy. Datenformate Strom & Gas](nybu)

|ID|Bezeichnung|Einheit|UTILMD<br/>Codever-wendung|UTILMD<br/>Preis-angabe|PRICAT<br/>Codever-wendung|PRICAT<br/>Preis-angabe|INVOIC<br/>Codever-wendung|INVOIC<br/>Preis-angabe|
|-|-|-|-|-|-|-|-|-|
|1-10-4-004|Für Marktlokationen deren (Teil-)Menge von dem Aufschlag der individuellen Netzentgelte nach § 19 StromNEV befreit ist (bis 31.12.2024)<br/><br/>Für Marktlokationen deren (Teil-)Menge von dem Aufschlag für besondere Netznutzung befreit ist (ab 01.01.2025)|€/kWh|||X||SOR|X|
|1-10-5|Aufschläge aufgrund der §§ 26 und 27c KWkG für Schienenbahnen||X||||||
|1-10-5-001|Aufschläge aufgrund des § 26 KWkG, die auch für Schienenbahnen für die jeweils ersten 1.000.000 kWh je Marktlokation gelten.|€/kWh|||X||X|X|
|1-10-5-002|Aufschläge aufgrund des § 27c KWKG für Schienenbahnen<br/>Letztverbrauchergruppe B (Letztverbraucher, die dem schienengebundenen Verkehr zuzuordnen sind und deren Jahresverbrauch an einer Marktlokation (Abnahmestelle) 1.000.000 kWh übersteigt, zahlen zusätzlich für über 1.000.000 kWh hinausgehende Strombezüge eine begrenzte KwkG-Umlage)|€/kWh|||X||X|X|
|1-10-5-003|Aufschläge aufgrund des § 27c KWkG für Schienenbahnen<br/>Letztverbrauchergruppe C (Letztverbraucher, die dem schienengebundenen Verkehr zuzuordnen sind und deren Stromkosten im vorangegangenen Geschäftsjahr vier Prozent des Umsatzes überstiegen haben, zahlen für über 1.000.000 kWh hinausgehende Strombezüge eine begrenzte KwkG-Umlage)|€/kWh|||X||X|X|
|1-10-6|Aufschläge aufgrund der Offshore-Netzumlage für Schienenbahnen nach § 17f EnWG||X||||||
|1-10-6-001|Aufschläge aufgrund der Offshore-Netzumlage nach § 17f EnWG, die auch für Schienenbahnen für die jeweils ersten 1.000.000 kWh je Marktlokation gelten.|€/kWh|||X||X|X|


Version: 5.6                                                                    30.09.2025                                                                    Seite 44 von 60

Version: 5.6                                                                    30.09.2025                                                                    Seite 44 von 60

Codeliste der Artikelnummern und Artikel-ID

![edi@energy logo](iuss)

|ID|Bezeichnung|Einheit|UTILMD<br/>Codeverwendung|UTILMD<br/>Preisangabe|PRICAT<br/>Codeverwendung|PRICAT<br/>Preisangabe|INVOIC<br/>Codeverwendung|INVOIC<br/>Preisangabe|
|-|-|-|-|-|-|-|-|-|
|1-10-6-002|Aufschläge aufgrund der Offshore-Netzumlage für Schienenbahnen nach § 17f Abs. 5 Satz 2 EnWG<br/>Letztverbrauchergruppe B (Letztverbraucher, die dem schienengebundenen Verkehr zuzuordnen sind und deren Jahresverbrauch an einer Marktlokation (Abnahmestelle) 1.000.000 kWh übersteigt, zahlen zusätzlich für über 1.000.000 kWh hinausgehende Strombezüge eine begrenzte Offshore-Netzumlage)|€/kWh|||X||X|X|
|1-10-6-003|Aufschläge aufgrund der Offshore-Netzumlage für Schienenbahnen nach § 17f Abs. 5 Satz 2 EnWG<br/>Letztverbrauchergruppe C (Letztverbraucher, die dem schienengebundenen Verkehr zuzuordnen sind und deren Stromkosten im vorangegangenen Geschäftsjahr vier Prozent des Umsatzes überstiegen haben, zahlen für über 1.000.000 kWh hinausgehende Strombezüge eine begrenzte Offshore-Netzumlage)|€/kWh|||X||X|X|
|1-10-7|Aufschläge aufgrund der §§ 26 und 27a KWkG für Anlagen zur Verstromung von Kuppelgasen||X||||||
|1-10-7-001|Aufschläge aufgrund des § 26 KWkG, die auch für Anlagen zur Verstromung von Kuppelgasen gelten|€/kWh|||X||X|X|
|1-10-7-002|Aufschläge aufgrund des § 27a KWkG für Anlagen zur Verstromung von Kuppelgasen, die eine begrenzte Umlage zahlen|€/kWh|||X||X|X|
|1-10-8|Aufschläge aufgrund der Offshore-Netzumlage nach § 17f EnWG für Anlagen zur Verstromung von Kuppelgasen||X||||||
|1-10-8-001|Aufschläge aufgrund der Offshore-Netzumlage nach § 17f EnWG, die auch für Anlagen zur Verstromung von Kuppelgasen gelten|€/kWh|||X||X|X|


Version: 5.6                                                  30.09.2025                                                  Seite 45 von 60

Version: 5.6                                                  30.09.2025                                                  Seite 45 von 60

Codeliste der Artikelnummern und Artikel-ID

![edi@energy logo](jtny)

|ID|Bezeichnung|Einheit|UTILMD<br/>Codever-wendung|UTILMD<br/>Preis-angabe|PRICAT<br/>Codever-wendung|PRICAT<br/>Preis-angabe|INVOIC<br/>Codever-wendung|INVOIC<br/>Preis-angabe|
|-|-|-|-|-|-|-|-|-|
|1-10-8-002|Aufschläge aufgrund der Offshore-Netzumlage nach § 17f EnWG für<br/>Anlagen zur Verstromung von Kuppelgasen, die nach § 27a KWkG eine<br/>begrenzte Umlage zahlen|€/kWh|||X||X|X|
|1-10-9|Aufschläge aufgrund der §§ 26 und 27b KWkG für Stromspeicher||X||||||
|1-10-9-001|Aufschläge aufgrund des § 26 KWkG, die auch für Stromspeicher gelten|€/kWh|||X||X|X|
|1-10-9-002|Aufschläge aufgrund des § 27b KWkG für Stromspeicher, deren Strom,<br/>der zum Zweck der Zwischenspeicherung in einem elektrischen,<br/>chemischen, mechanischen oder physikalischen Speicher verbraucht<br/>wird, keine Umlage zahlen|€/kWh|||X||X|X|
|1-11-1|Aufschläge aufgrund der Offshore-Netzumlage nach § 17f EnWG für<br/>Stromspeicher||X||||||
|1-11-1-001|Aufschläge aufgrund der Offshore-Netzumlage nach § 17f EnWG, die<br/>auch für Stromspeicher gelten|€/kWh|||X||X|X|
|1-11-1-002|Aufschläge aufgrund der Offshore-Netzumlage nach § 17f EnWG für<br/>Stromspeicher nach § 27b KwkG, deren Strom, der zum Zweck der<br/>Zwischenspeicherung in einem elektrischen, chemischen, mechanischen<br/>oder physikalischen Speicher verbraucht wird, keine Umlage zahlen|€/kWh|||X||X|X|






Seite 46 von 60

Version: 5.6
30.09.2025

Codeliste der Artikelnummern und Artikel-ID

![edi@enerGy. Datenformate Strom & Gas](gvim)

## **3.2 Separat bestellbare Einzelleistungen für Marktlokationen und Verzugskosten für die Sparte Strom und Gas**

|ID|Bezeichnung|Einheit|PRICAT<br/>Codever- wendung|PRICAT<br/>Preis- angabe|INVOIC<br/>Codever- wendung|INVOIC<br/>Preis- angabe|
|-|-|-|-|-|-|-|
|2-01-7-001|Unterbrechung der Anschlussnutzung in der regulären Arbeitszeit|€/Auftrag|X|X|X|X|
|2-01-7-002|Wiederherstellung der Anschlussnutzung in der regulären Arbeitszeit|€/Auftrag|X|X|X|X|
|2-01-7-003|Erfolglose Unterbrechung|€/Auftrag|X|X|X|X|
|2-01-7-004|Stornierung eines Auftrags zur Unterbrechung der Anschlussnutzung bis zum<br/>Vortag der Sperrung|€/Auftrag|X|X|X|X|
|2-01-7-005|Stornierung eines Auftrags zur Unterbrechung der Anschlussnutzung am Tag der<br/>Sperrung|€/Auftrag|X|X|X|X|
|2-01-7-006|Wiederherstellung der Anschlussnutzung außerhalb der regulären Arbeitszeit|€/Auftrag|X|X|X|X|
|2-02-0-001|Verzugskosten pauschal|€/Fall|X|X|X|X|
|2-02-0-002|Verzugskosten variabel|€|X|--|X|X|


Version: 5.6
30.09.2025
Seite 47 von 60

Codeliste der Artikelnummern und Artikel-ID

![edi@energy. Datenformate Strom & Gas](tutm)

## **3.3 Freiwillige Abrechnung sonstiger Leistungen**<sup>14</sup> **für die Sparte Strom**

|ID|Bezeichnung|Einheit|UTILMD<br/>Codever-wendung|UTILMD<br/>Preis-angabe|PRICAT<br/>Codever-wendung|PRICAT<br/>Preis-angabe|INVOIC<br/>Codever-wendung|INVOIC<br/>Preis-angabe|
|-|-|-|-|-|-|-|-|-|
|3-01-0-001|Blindarbeit|€/kvarh|X|--|X|X|X|X|
|3-02-0|Tarifierte Blindarbeit||X|--|--|--|--|--|
|3-02-0-001|Blindarbeit 1|€/kvarh|--|--|X|X|X|X|
|3-02-0-002|Blindarbeit 2|€/kvarh|--|--|X|X|X|X|


<sup>14</sup> nur noch auf freiwilliger Basis mit den Lieferanten abrechenbar ansonsten mit den Anschlussnutzern, s. GPKE-Festlegung BK6

Version: 5.6

30.09.2025

Seite 48 von 60

Version: 5.6
30.09.2025
Seite 48 von 60

Codeliste der Artikelnummern und Artikel-ID

![edi@energy. Datenformate Strom & Gas](snee)

## **3.4 Abrechnung beim MSB bestellter Leistungen**

### **3.4.1 Regelungen zu den vom MSB verwendeten Artikel-ID**

Die jeweiligen Artikel-ID werden unter Nutzung der Codes für Messprodukte, Konfigurationsprodukte bzw. Produkte zur Änderung der Technik an einer Lokation vom MSB erzeugt.

Die nutzbaren Codes für Messprodukte, Konfigurationsprodukte bzw. Produkte zur Änderung der Technik an einer Lokation sind der jeweils aktuell gültigen EDI@Energy-Codeliste der Konfigurationen zu entnehmen.

Die jeweils auf Basis dieser Codes gebildeten Artikel-ID haben das Format: n13-n2. Die Artikel-ID setzt sich fachlich wie folgt zusammen:

Vor dem "-": Produkt-Code und
Nach dem "-": Differenzierungsmerkmal

Dabei ist zu berücksichtigen, dass sich die Detailregeln für das Differenzierungsmerkmal in den Artikel-ID für Messprodukte und Konfigurationsprodukte, von denen in der Artikel-ID für Produkte zur Änderung der Technik an einer Lokation unterscheiden:

›   Das Differenzierungsmerkmal in den Artikel-ID der Mess- und Konfigurationsprodukte dient zur Unterscheidung der jeweils erbrachten Leistung, die mit der Umsetzung des jeweiligen Produkts verbunden ist und der dadurch verursachten Kosten. Die Zahlen für diese Codes, die in diesen Artikel-ID verwendet werden dürfen und welche fachliche Aussage darüber jeweils codiert wird, sind über das Kapitel „Artikel-ID für die Bestellprozesse beim MSB" dieses Dokuments eindeutig festgelegt. Es sind nur die Codes 01, 02 und 03 erlaubt. Zusätzlich zu dieser fachlichen Preisdifferenzierung kann der Preis, der einer so gebildeten Artikel-ID zugeordnet ist, gezont sein. Sollte der Preis zu einer Artikel-ID für ein Mess- oder Konfigurationsprodukt gezont sein, so sind die Grenzen der Preiszonen durch den MSB im zugehörigen RNG-Segment anzugeben.

›   Mittels des Differenzierungsmerkmals in den Artikel-ID der Produkte zur Änderung der Technik an einer Lokation erfolgt die Aussage, ob es sich um keine oder eine Preisstaffelung handelt. In diesem Fall dient das Differenzierungsmerkmal ausschließlich der Preisdifferenzierung. Falls es sich um einen gestaffelten Preis handelt, werden die Grenzen einer Staffel, für die mittels der jeweiligen Artikel-ID der Preis

Version: 5.6 30.09.2025 Seite 49 von 60

Codeliste der Artikelnummern und Artikel-ID

![edi@energy. Datenformate Strom & Gas](oaxz)

ausgetauscht wird, im RNG-Segment angegeben.

Für die aus den Produkt-Codes zur Änderung der Technik an einer Lokation gebildeten Artikel-ID gelten die Vorgaben der Tabelle „Codes der Preisdifferenzierungen (PD) für die Produkt-Codes zur Änderung der Technik an einer Lokation".

### **Zonenpreissystem:**

Ein Preissystem, bei dem die abgenommene Energiemenge in feste Verbrauchsbereiche („Zonen“) unterteilt ist, für die jeweils ein unterschiedlicher Preis gilt. Der Kunde „durchläuft“ bei steigender Abnahmemenge die Zonen – das heißt, jede Verbrauchseinheit wird entsprechend der Zone abgerechnet, in die sie fällt. Die Gesamtmenge wird somit zonenweise bepreist.

### **Staffelpreissystem:**

Ein Preissystem, bei dem ein einheitlicher Preis in Abhängigkeit von der abgenommenen Energiemenge gestaffelt wird. Die gesamte Verbrauchsmenge wird nach derjenigen Staffel abgerechnet, in die der Gesamtverbrauch fällt.

Codes der Preisdifferenzierungen (PD) für die Produkt-Codes zur Änderung der Technik an einer Lokation

|Preisdifferenzierungen|Code|
|-|-|
|Es gibt keine Preisdifferenzierung|01|
|1. Preis bei Preisdifferenzierung|02|
|2. Preis bei Preisdifferenzierung|03|
|3. …|..|


Version: 5.6 30.09.2025 Seite 50 von 60

Version: 5.6 30.09.2025 Seite 50 von 60

Codeliste der Artikelnummern und Artikel-ID

![edi@energy logo](afrh)

## **3.4.2    Artikel-ID für die Bestellprozesse beim MSB**

|ID|Bezeichnung|Einheit|
|-|-|-|
|Messprodukt-Code-01|Kosten für das Einrichten des Messprodukts<br/>Messprodukt-Code: Code des Messprodukts aus der EDI\@Energy Codeliste der Konfigurationen|€/Auftrag|
|Messprodukt-Code-02|Kosten für den Betrieb des Messprodukts<br/>Messprodukt-Code: Code des Messprodukts aus der EDI\@Energy Codeliste der Konfigurationen|€/Tag|
|Messprodukt-Code-03|Kosten für die anfallenden Transaktionen des Messprodukts<br/>Messprodukt-Code: Code des Messprodukts aus der EDI\@Energy Codeliste der Konfigurationen|€/Transaktion|
|Konfigurationsprodukt-Code-01|Kosten für das Einrichten des Konfigurationsprodukts<br/>Konfigurationsprodukt-Code: Code des Konfigurationsprodukts aus der EDI\@Energy Codeliste der Konfigurationen|€/Auftrag|
|Konfigurationsprodukt-Code-02|Kosten für den Betrieb des Konfigurationsprodukts<br/>Konfigurationsprodukt-Code: Code des Konfigurationsprodukts aus der EDI\@Energy Codeliste der Konfigurationen|€/Tag|
|Konfigurationsprodukt-Code-03|Kosten für die anfallenden Transaktionen des Konfigurationsprodukts<br/>Konfigurationsprodukt-Code: Code des Konfigurationsprodukts aus der EDI\@Energy Codeliste der Konfigurationen|€/Transaktion|
|Produkt-Code-PD|Kosten für die Änderung der Technik an einer Lokation<br/>Produkt-Code: Code des Produkts zur Änderung an einer Lokation aus der EDI\@Energy Codeliste der Konfigurationen|€/Auftrag|
|9991000003030-01¹⁵|Pauschale Kosten für das Scheitern der Änderung der Technik an einer Lokation|€/Auftrag|


<sup>15</sup> Hinweis: Für die pauschalen Kosten für das Scheitern der Änderung der Technik an einer Lokation kann ausschließlich ein Preis angegeben werden, d. h. die ersten 13 Stellen dieses Codes können ausschließlich mit dem String „-01“ zu dieser hier angegebenen ID kombiniert werden.

Version: 5.6
30.09.2025
Seite 51 von 60

Codeliste der Artikelnummern und Artikel-ID

![edi@energy. Datenformate Strom & Gas](knjh)

Beispiel für die Artikel-ID zur Einrichtung eines Messproduktes:
**9991000000044-01**

In dem Beispiel besagt die Artikel-ID: Die Einrichtung des Messproduktes „Marktlokation mit Wahlmöglichkeit der Zuordnung einer Zählzeit für
Wirkarbeit Menge jährlich“.

Version: 5.6
30.09.2025
Seite 52 von 60

Codeliste der Artikelnummern und Artikel-ID

![edi@energy.](nodj)

## **3.5 Abrechnung Messstellenbetrieb für die Sparte Strom**

### **3.5.1 Abrechnung Messstellenbetrieb vom MSB an LF**

Hinweis: In der Spalte „Bezeichnung“ wird als Tausendertrennzeichen der übliche „.“ gewählt. Im MsbG wird als Tausendertrennzeichen das Leerzeichen genutzt.

|ID|Bezeichnung|Einheit|Für gMSBnutzbar|Für wMSBnutzbar|
|-|-|-|-|-|
|4-02-0-001|POG bei verbrauchender Marktlokation > 100.000 kWh/a mit iMS|€/Tag|X|--|
|4-02-0-002|POG bei verbrauchender Marktlokation ]50.000 kWh/a; 100.000 kWh/a] mit iMS|€/Tag|X|--|
|4-02-0-003|POG bei verbrauchender Marktlokation ]20.000 kWh/a; 50.000 kWh/a] mit iMS|€/Tag|X|--|
|4-02-0-004|POG bei verbrauchender Marktlokation ]10.000 kWh/a; 20.000 kWh/a] mit iMS|€/Tag|X|--|
|4-02-0-005|POG bei verbrauchender Marktlokation mit einer steuerbaren Verbrauchseinrichtung mit denen eine Vereinbarung nach § 14a des Energiewirtschaftsgesetzes besteht mit iMS|€/Tag|X|--|
|4-02-0-006|POG bei verbrauchender Marktlokation ]6.000 kWh/a; 10.000 kWh/a] mit iMS|€/Tag|X|--|
|4-02-0-007|POG bei erzeugender Marktlokation mit installierter Leistung ]7 kW; 15 kW] mit iMS|€/Tag|X|--|
|4-02-0-008|POG bei erzeugender Marktlokation mit installierter Leistung ]15 kW; 25 kW] mit iMS|€/Tag|X|--|
|4-02-0-009|POG bei erzeugender Marktlokation mit installierter Leistung ]25 kW; 100 kW] mit iMS|€/Tag|X|--|
|4-02-0-010|POG bei erzeugender Marktlokation mit installierter Leistung > 100 kW mit iMS|€/Tag|X|--|
|4-02-0-011|POG bei Marktlokation mit mME|€/Tag|X|--|
|4-02-0-012¹⁶|POG bei verbrauchender Marktlokation ]3.000 kWh/a; 6.000 kWh/a] mit iMS|€/Tag|X|--|
|4-02-0-013¹⁶|POG bei verbrauchender Marktlokation \[0 kWh/a; 3.000 kWh/a] mit iMS|€/Tag|X|--|


<sup>16</sup> Auslaufend zum 01.01.2026, 00:00 Uhr

Version: 5.6                                                                      30.09.2025                                                                   Seite 53 von 60

Codeliste der Artikelnummern und Artikel-ID

![edi@energy. Datenformate Strom & Gas](sjea)

|ID|Bezeichnung|Einheit|Für gMSBnutzbar|Für wMSBnutzbar|
|-|-|-|-|-|
|4-02-0-014|POG bei erzeugender Marktlokation mit einer installierten Leistung \[0 kW; 7 kW] mit iMS|€/Tag|X|--|
|4-02-0-015|Messstellenbetrieb bei mME/iMS, Höchstspannung, Wandlersatz für Messstellenbetrieb bei mME/iMS|€/Tag|X|X|
|4-02-0-016|Messstellenbetrieb bei mME/iMS, Hochspannung, Wandlersatz für Messstellenbetrieb bei mME/iMS|€/Tag|X|X|
|4-02-0-017|Messstellenbetrieb bei mME/iMs, Mittelspannung, Wandlersatz für Messstellenbetrieb bei mME/iMS|€/Tag|X|X|
|4-02-0-018|Messstellenbetrieb bei mME/iMs, Niederspannung, Wandlersatz für Messstellenbetrieb bei mME/iMS|€/Tag|X|X|
|4-02-0-019|Schaltgerät/Tarifschaltung|€/Tag|X|X|
|4-02-0-021|Entgelt für Messstellenbetrieb bei individuellem Angebot|€/Tag|--|X|
|4-02-0-022|Einbau und Betrieb einer Steuereinrichtung am Netzanschlusspunkt|€/Tag|X|X|
|4-02-0-023|Jährliches Zusatzentgelt bei vorzeitiger Ausstattung von optionalen Einbaufällen|€/Tag|X|--|
|4-02-0-024¹⁷|POG bei verbrauchender Marktlokation \[0 kWh/a; 6.000 kWh/a] mit iMS|€/Tag|X||


## Hinweis:

Für Leistungen, wie beispielsweise die Zusatzdienstleistung nach § 34 Abs. 2 Nr. 2a MsbG „Steuerung Verbrauchseinrichtungen / Netzanschlüsse nach § 14a“, sind in dieser Tabelle keine Artikel-ID genannt, da diese Leistungen unter Nutzung der entsprechenden Use-Cases des Abschnitts „Bestellung einer Konfiguration“ der Geschäftsprozesse zur Kundenbelieferung mit Elektrizität (GPKE) bestellt werden und somit für die Abrechnung der durch den MSB erbrachten Leistungen die Artikel-ID nach Kapitel „Artikel-ID für die Bestellprozesse beim MSB“ dieser Codeliste zur Verfügung stehen.

17 Gültig ab 01.01.2026, 00:00 Uhr

Version: 5.6 30.09.2025 Seite 54 von 60

Version: 5.6 30.09.2025 Seite 54 von 60

Codeliste der Artikelnummern und Artikel-ID

![edi@energy logo](wqla)

Leistungen, die nicht im Rahmen der Marktkommunikation bestellt werden können, können auch nicht mittels der durch EDI@Energy zur Verfügung gestellten Dokumente abgerechnet werden. Wie diese abgerechnet werden, ist zwischen den Beteiligten bilateral zu vereinbaren.

Version: 5.6 30.09.2025 Seite 55 von 60

Version: 5.6 30.09.2025 Seite 55 von 60

Codeliste der Artikelnummern und Artikel-ID

![edi@energy. Datenformate Strom & Gas](ecfm)

## **3.5.2   Abrechnung Messstellenbetrieb vom MSB an NB**

Hinweis: In der Spalte „Bezeichnung“ wird als Tausendertrennzeichen der übliche „.“ gewählt. Im MsbG wird als Tausendertrennzeichen das
Leerzeichen genutzt.

|ID|Bezeichnung|Einheit|
|-|-|-|
|4-03-0-001|POG bei verbrauchender Marktlokation > 100.000 kWh/a mit iMS|€/Tag|
|4-03-0-002|POG bei verbrauchender Marktlokation ]50.000 kWh/a; 100.000 kWh/a] mit iMS|€/Tag|
|4-03-0-003|POG bei verbrauchender Marktlokation ]20.000 kWh/a; 50.000 kWh/a] mit iMS|€/Tag|
|4-03-0-004|POG bei verbrauchender Marktlokation ]10.000 kWh/a; 20.000 kWh/a] mit iMS|€/Tag|
|4-03-0-005|POG bei verbrauchender Marktlokation mit einer steuerbaren Verbrauchseinrichtung mit denen eine Vereinbarung nach § 14a des Energiewirtschaftsgesetzes besteht mit iMS|€/Tag|
|4-03-0-006|POG bei verbrauchender Marktlokation ]6.000 kWh/a; 10.000 kWh/a] mit iMS|€/Tag|
|4-03-0-007|POG bei erzeugender Marktlokation mit installierter Leistung ]7 kW; 15 kW] mit iMS|€/Tag|
|4-03-0-008|POG bei erzeugender Marktlokation mit installierter Leistung ]15 kW; 25 kW] mit iMS|€/Tag|
|4-03-0-009|POG bei erzeugender Marktlokation mit installierter Leistung ]25 kW; 100 kW] mit iMS|€/Tag|
|4-03-0-010|POG bei erzeugender Marktlokation mit installierter Leistung > 100 kW mit iMS|€/Tag|
|4-03-0-011¹⁶|POG bei verbrauchender Marktlokation ]3.000 kWh/a; 6.000 kWh/a] mit iMS|€/Tag|
|4-03-0-012¹⁶|POG bei verbrauchender Marktlokation \[0 kWh/a; 3.000 kWh/a] mit iMS|€/Tag|
|4-03-0-013|POG bei erzeugender Marktlokation mit installierter Leistung \[0 kW; 7 kW] mit iMS|€/Tag|
|4-03-0-014|Einbau und Betrieb einer Steuereinrichtung am Netzanschlusspunkt|€/Tag|
|4-03-0-015¹⁷|POG bei verbrauchender Marktlokation \[0 kWh/a; 6.000 kWh/a] mit iMS|€/Tag|


Version: 5.6                                                  30.09.2025                                                  Seite 56 von 60

Version: 5.6                                                  30.09.2025                                                  Seite 56 von 60

Codeliste der Artikelnummern und Artikel-ID

![edi@energy. Datenformate Strom & Gas](utbw)

## **4   Änderungshistorie**

|Änd-ID|Ort|ÄnderungenBisher Neu|ÄnderungenBisher Neu|Grund der Anpassung|Status|
|-|-|-|-|-|-|
|26867|Kapitel 3.4|3.4 Artikel-ID für die Bestellprozesse beim MSB|3.4 Abrechnung beim MSB bestellter Leistungen|Neue Strukturierung und Ergänzung des Kapitels|Fehler (30.09.2025)|


Version: 5.6                                                                    30.09.2025                                                                      Seite 57 von 60

Version: 5.6                                                                    30.09.2025                                                                      Seite 57 von 60

Codeliste der Artikelnummern und Artikel-ID

![edi@energy. Datenformate Strom & Gas](vlwi)

|26912|Kapitel 3.4|3.4 Artikel-ID für die Bestellprozesse beim MSB<br/>Die jeweiligen Artikel-ID werden unter Nutzung der Codes für Messprodukte, Konfigurationsprodukte bzw. Produkte zur Änderung an einer Lokation vom MSB erzeugt.<br/>Die nutzbaren Codes für Messprodukte, Konfigurationsprodukte bzw. Produkte sind der jeweils aktuell gültigen EDI\@Energy-Codeliste der Konfigurationen zu entnehmen.<br/>Die jeweiligen Artikel-ID haben das Format: n13-n2, welche sich wie folgt zusammensetzt:<br/>› Produkt-Code und<br/>› Vom MSB anzugebende Preisdifferenzierungen, welche in der Artikel-ID an der Stelle 2 eindeutig mit zwei Ziffern gekennzeichnet ist<br/><br/>Codes der Preisdifferenzierungen (PD) für die Produkt-Codes<br/>\[Tabelle]|3.4.1 Regelungen zu den vom MSB verwendeten Artikel-ID<br/>Die jeweiligen Artikel-ID werden unter Nutzung der Codes für Messprodukte, Konfigurationsprodukte bzw. Produkte zur Änderung der Technik an einer Lokation vom MSB erzeugt.<br/>Die nutzbaren Codes für Messprodukte, Konfigurationsprodukte bzw. Produkte zur Änderung der Technik an einer Lokation sind der jeweils aktuell gültigen EDI\@Energy-Codeliste der Konfigurationen zu entnehmen.<br/>Die jeweils auf Basis dieser Codes gebildeten Artikel-ID haben das Format: n13-n2. Die Artikel-ID setzt sich fachlich wie folgt zusammen:<br/>› Vor dem "-": Produkt-Code und<br/>› Nach dem "-": Differenzierungsmerkmal<br/>Dabei ist zu berücksichtigen, dass sich die Detailregeln für das Differenzierungsmerkmal in den Artikel-ID für Messprodukte und Konfigurationsprodukte, von denen in der Artikel-ID für Produkte zur Änderung der Technik an einer Lokation unterscheiden:<br/>› Das Differenzierungsmerkmal in den Artikel-ID der Mess- und Konfigurationsprodukte dient zur Unterscheidung der jeweils erbrachten Leistung, die mit der Umsetzung des jeweiligen Produkts verbunden ist und der dadurch verursachten Kosten. Die Zahlen für diese Codes, die in diesen Artikel-ID verwendet werden dürfen und welche fachliche Aussage darüber jeweils codiert wird, sind über das Kapitel „Artikel-ID für die Bestellprozesse beim MSB" dieses Dokuments eindeutig festgelegt. Es sind nur die Codes 01, 02 und 03 erlaubt. Zusätzlich zu dieser fachlichen Preisdifferenzierung kann der Preis, der einer so gebildeten Artikel-ID zugeordnet ist,|Nötige Präzisierung, um die Unterschiede zwischen den Artikel-ID für Messprodukte und Konfigurationsprodukte einerseits und den Artikel-ID für Produkte zur Änderung an einer Lokation andererseits verstehen zu können.|Fehler (30.09.2025)|
|-|-|-|-|-|-|


Version: 5.6 30.09.2025 Seite 58 von 60

Version: 5.6 30.09.2025 Seite 58 von 60

Codeliste der Artikelnummern und Artikel-ID

![edi@energy. Datenformate Strom & Gas](wrjm)

||||gezont sein. Sollte der Preis zu einer Artikel-ID für<br/>ein Mess- oder Konfigurationsprodukt gezont<br/>sein, so sind die Grenzen der Preiszonen durch<br/>den MSB im zugehörigen RNG-Segment<br/>anzugeben.<br/>› Mittels des Differenzierungsmerkmals in<br/>den Artikel-ID der Produkte zur Änderung der<br/>Technik an einer Lokation erfolgt die Aussage, ob<br/>es sich um keine oder eine Preisstaffelung<br/>handelt. In diesem Fall dient das<br/>Differenzierungsmerkmal ausschließlich der<br/>Preisdifferenzierung.<br/>Falls es sich um einen gestaffelten Preis handelt,<br/>werden die Grenzen einer Staffel, für die mittels<br/>der jeweiligen Artikel-ID der Preis ausgetauscht<br/>wird, im RNG-Segment angegeben.<br/>Für die aus den Produkt-Codes zur Änderung der<br/>Technik an einer Lokation gebildeten Artikel-ID<br/>gelten die Vorgaben der Tabelle „Codes der<br/>Preisdifferenzierungen (PD) für die Produkt-<br/>Codes zur Änderung der Technik an einer<br/>Lokation".<br/>****Zonenpreissystem**:**<br/>Ein Preissystem, bei dem die abgenommene<br/>Energiemenge in feste Verbrauchsbereiche<br/>(„Zonen“) unterteilt ist, für die jeweils ein<br/>unterschiedlicher Preis gilt. Der Kunde<br/>„durchläuft“ bei steigender Abnahmemenge die<br/>Zonen – das heißt, jede Verbrauchseinheit wird<br/>entsprechend der Zone abgerechnet, in die sie<br/>fällt. Die Gesamtmenge wird somit zonenweise<br/>bepreist.<br/>****Staffelpreissystem**:**<br/>Ein Preissystem, bei dem ein einheitlicher Preis in<br/>Abhängigkeit von der abgenommenen<br/>Energiemenge gestaffelt wird. Die gesamte<br/>Verbrauchsmenge wird nach derjenigen Staffel||
|-|-|-|-|-|


Version: 5.6 30.09.2025 Seite 59 von 60

Version: 5.6 30.09.2025 Seite 59 von 60

Codeliste der Artikelnummern und Artikel-ID

![edi@energy. Datenformate Strom & Gas](ysup)

|Änd-ID|Ort|Änderungen<br/>Bisher|Änderungen<br/>Neu|Grund der Anpassung|Status|
|-|-|-|-|-|-|
||||abgerechnet, in die der Gesamtverbrauch fällt.<br/><br/>Codes der Preisdifferenzierungen (PD) für die Produkt-Codes zur Änderung der technik an einer Lokation<br/>\[Tabelle]|||
|26087|Kapitel|3.4 Artikel-ID für die Bestellprozesse beim MSB<br/>\[Tabelle]|3.4.2 Artikel-ID für die Bestellprozesse beim MSB<br/><br/>\[Tabelle]|Anpassung an die neue Strukturierung des Kapitels|Fehler (30.09.2025)|


Version: 5.6                                                                                      30.09.2025                                                                                      Seite 60 von 60

Version: 5.6                                                                                      30.09.2025                                                                                      Seite 60 von 60