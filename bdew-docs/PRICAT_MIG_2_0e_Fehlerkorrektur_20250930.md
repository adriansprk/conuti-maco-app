![edi@energy logo](vuyv)

# **Konsolidierte Lesefassung mit Fehlerkorrekturen**
**Stand: 30.09.2025**

# **PRICAT** Nachrichtenbeschreibung

auf Basis

## **PRICAT**
**PRICAT**
Preisliste/Katalog

**UN D.20B S3**

Version:                          2.0e
Ursprüngliches Publikationsdatum:  01.04.2025
Autor:                            BDEW

Nachrichtenstruktur......................................................................................................................... 3
Diagramm......................................................................................................................................... 4
Segmentlayout .................................................................................................................................
                                                                                                                                             5
Änderungshistorie.......................................................................................................................... 33

PRICAT MIG

## **Disclaimer**

Die PDF-Datei ist das allein gültige Dokument.
Die zusätzlich veröffentlichte Word-Datei dient als informatorische Lesefassung und entspricht inhaltlich der PDF-Datei. Diese Word-Datei wird bis auf Weiteres rein informatorisch und ergänzend veröffentlicht unter dem Vorbehalt, zukünftig eine kostenpflichtige Veröffentlichung der Word-Datei einzuführen.
Zusätzlich werden zur PDF-Datei auch XML-Dateien als optionale Unterstützung gegen Entgelt veröffentlicht.

Version:  2.0e                                                             30.09.2025                             Seite:    2     /       33

PRICAT MIG

![edi@energy. Datenformate Strom & Gas](vjsv)

## **Nachrichtenstruktur**

|Zähler|Nr|Bez|Sta|BDEW|Sta|BDEW|Ebene|Inhalt|
|-|-|-|-|-|-|-|-|-|
|0010|00001|**UNH**|M|M|1|1|0|Nachrichten-Kopfsegment|
|0020|00002|**BGM**|M|M|1|1|0|Beginn der Nachricht|
|0030|00003|DTM|M|D|35|1|1|Betrachtungszeitintervall|
|0030|00004|DTM|M|M|35|1|1|Nachrichtendatum|
|0030|00005|DTM|M|D|35|1|1|Gültigkeitsbeginn|
|0060||SG1|C|D|99|1|1|Vorgängerversion|
|0070|00006|RFF|M|M|1|1|1|Vorgängerversion|
|0060||SG1|C|D|99|1|1|Preise des Netzbetreibers|
|0070|00007|RFF|M|M|1|1|1|Preise des Netzbetreibers|
|0060||SG1|C|R|99|1|1|Prüfidentifikator|
|0070|00008|RFF|M|M|1|1|1|Prüfidentifikator|
|0090||SG2|C|R|99|1|1|Empfänger-ID|
|0100|00009|NAD|M|M|1|1|1|Empfänger-ID|
|0090||SG2|C|R|99|1|1|Sender-ID|
|0100|00010|NAD|M|M|1|1|1|Sender-ID|
|0110|00011|**LOC**|C|D|25|1|2|Regelzone|
|0150||**SG4**|C|O|5|1|2|CTA-COM|
|0160|00012|CTA|M|M|1|1|2|Ansprechpartner|
|0170|00013|COM|C|R|5|5|3|Kommunikationsverbindung|
|0220||**SG6**|C|D|20|1|1|Währungsangaben|
|0230|00014|**CUX**|M|M|1|1|1|Währungsangaben|
|0590||SG17|C|D|1000|1|1|PGI-SG36|
|0600|00015|PGI|M|M|1|1|1|Produktgruppen-Information|
|1310||SG36|C|R|999999|999999|2|LIN-PIA-IMD-SG40|
|1320|00016|LIN|M|M|1|1|2|Positionsdaten|
|1330|00017|PIA|C|D|99|1|3|Preisschlüsselstamm|
|1340|00018|IMD|C|D|999|1|3|Produktbeschreibung|
|1560||SG40|C|D|100|100|3|Preisangabe|
|1570|00019|PRI|M|M|1|1|3|Preisangaben|
|1600|00020|RNG|C|D|1|1|4|Angaben zum Wertebereich|
|1610|00021|DTM|C|D|5|2|4|Datum/Uhrzeit/Zeitspanne|
|0590||SG17|C|D|1000|1|1|Netzbetreiberindividuelle Artikel-ID|
|0600|00022|PGI|M|M|1|1|1|Netzbetreiberindividuelle Artikel-ID|
|1310||SG36|C|R|999999|999999|2|Positionsdaten|
|1320|00023|LIN|M|R|1|1|2|Positionsdaten|
|1560||SG40|C|R|100|1|3|Preisangabe|
|1570|00024|PRI|M|M|1|1|3|Preisangaben|
|1600|00025|RNG|C|D|1|1|4|Zonenintervallgrenzen|
|2400|00026|**UNT**|M|M|1|1|0|Nachrichten-Endesegment|


Bez = Segment-/Gruppen-Bezeichner
Zähler = Nummer der Segmente/Gruppen im Standard
Nr = Laufende Segmentnummer im Guide
MaxWdh = Maximale Wiederholung der Segmente/Gruppen

Sta = Standard UN/CEFACT
EDIFACT: M=Muss/Mandatory, C=Conditional
Anwendung: R=Erforderlich/Required, O=Optional, D=Abhängig von/
Dependent, N=Nicht benutzt/Not used





Seite: 3 / 33

Version: 2.0e
30.09.2025

PRICAT MIG

![edi@energy. Datenformate Strom & Gas](voja)

## **Diagramm**

graph TD
    subgraph Ebene0 [Ebene 0]
        UNH[UNHM 1]
        BGM[BGMM 1]
        SG1[SG1C 99]
        SG2[SG2C 99]
        SG6[SG6C 20]
        SG17[SG17C 1000]
        UNT[UNTM 1]
    end

    subgraph Ebene1 [Ebene 1]
        DTM1[DTMM 35]
        RFF[RFFM 1]
        NAD[NADM 1]
        CUX[CUXM 1]
        PGI[PGIM 1]
        SG4[SG4C 5]
        SG36[SG36C 99999]
    end

    subgraph Ebene2 [Ebene 2]
        LOC[LOCC 25]
        CTA[CTAM 1]
        LIN[LINM 1]
        SG40[SG40C 100]
    end

    subgraph Ebene3 [Ebene 3]
        COM[COMC 5]
        PIA[PIAC 99]
        IMD[IMDC 999]
        PRI[PRIM 1]
    end

    subgraph Ebene4 [Ebene 4]
        RNG[RNGC 1]
        DTM2[DTMC 5]
    end

    %% Connections
    Root[ ] --- UNH
    Root --- BGM
    Root --- SG1
    Root --- SG2
    Root --- SG6
    Root --- SG17
    Root --- UNT

    SG1 --- DTM1
    SG2 --- RFF
    SG2 --- NAD
    NAD --- LOC
    NAD --- SG4
    SG4 --- CTA
    SG6 --- CUX
    SG17 --- PGI
    PGI --- SG36
    SG36 --- LIN
    CTA --- COM
    LIN --- PIA
    LIN --- IMD
    LIN --- SG40
    SG40 --- PRI
    PRI --- RNG
    PRI --- DTM2

    style Root fill:none,stroke:none

|Bez|Bez|
|-|-|
|St|MaxWdh|


Bez = Segment-/Gruppen-Bezeichner
St = Durch UN/CEFACT definierter Status (M=Muss/Mandatory, C=Conditional)
 MaxWdh = Durch UN/CEFACT definierte maximale Wiederholung der Segmente/Gruppen

Hinweis: Die Darstellung des hier abgebildeten
Branchingdiagramms ist implizit.

Version:  2.0e

30.09.2025

Seite: 4

33

PRICAT MIG

![edi@energy. Datenformate Strom & Gas](xhrs)

## Segmentlayout

|Zähler|Nr|Bez|St|MaxWdh|St|MaxWdh|Ebene|Name|
|-|-|-|-|-|-|-|-|-|
|0010|00001|UNH|M|1|M|1|0|**Nachrichten-Kopfsegment**|


|Bez|Name|Standard<br/>St|Standard<br/>Format|BDEW<br/>St|BDEW<br/>Format|Anwendung / Bemerkung|
|-|-|-|-|-|-|-|
|UNH|||||||
|0062|Nachrichten-Referenznummer|M|an..14|M|an..14|*Eindeutige Nachrichtenreferenz des Absenders. Laufende<br/>Nummer der Nachrichten im Datenaustausch. Identisch mit<br/>DE0062 im UNT, i. d. R. vom sendenden Konverter<br/>vergeben.*|
|S009|Nachrichten-Kennung|M||M|||
|0065|Nachrichtentyp-Kennung|M|an..6|M|an..6|****PRICAT Preisliste/Katalog****|
|0052|Versionsnummer des<br/>Nachrichtentyps|M|an..3|M|an..3|****D Entwurfs-Version****|
|0054|Freigabenummer des<br/>Nachrichtentyps|M|an..3|M|an..3|****20B Ausgabe 2020 - B****|
|0051|Verwaltende Organisation|M|an..2|M|an..2|****UN UN/CEFACT****|
|0057|Anwendungscode der<br/>zuständigen Organisation|C|an..6|R|an..6|****2.0e Versionsnummer der zugrundeliegenden**<br/>**BDEW-Nachrichtenbeschreibung****|


## Bemerkung:

Dieses Segment dient dazu, eine Nachricht zu eröffnen, zu identifizieren und zu spezifizieren.

Die Datenelemente 0065, 0052, 0054 und 0051 deklarieren die Nachricht als UNSM des Verzeichnisses D.20B unter Kontrolle der
Vereinten Nationen.

## Hinweis:

DE0057: Es werden die Versions- und Release-Nummern der Nachrichtenbeschreibungen angegeben.

## Beispiel:

UNH+767097019+PRICAT:D:20B:UN:2.0e'

Bez = Objekt-Bezeichner
Nr = Laufende Segmentnummer im Guide
MaxWdh = Maximale Wiederholung der Segmente/Gruppen
Zähler = Nummer der Segmente/Gruppen im Standard

St = Status
EDIFACT: M=Muss/Mandatory, C=Conditional
Anwendung: R=Erforderlich/Required, O=Optional, D=Abhängig von/
Dependent, N=Nicht benutzt/Not used

Version: 2.0e

30.09.2025

Seite: 5

/ 33

PRICAT MIG

![edi@energy. Datenformate Strom & Gas](sbcc)

## Segmentlayout

|Zähler|Nr|Bez|St|MaxWdh|St|MaxWdh|Ebene|Name|
|-|-|-|-|-|-|-|-|-|
|0020|00002|BGM|M|1|M|1|0|**Beginn der Nachricht**|


|Bez|Name|Standard<br/>St|Standard<br/>Format|BDEW<br/>St|BDEW<br/>Format|Anwendung / Bemerkung|
|-|-|-|-|-|-|-|
|BGM|||||||
|C002|Dokumenten-/<br/>Nachrichtenname|C||R|||
|1001|Dokumentenname, Code|C|an..3|R|an..3|**Z04 Ausgleichsenergiepreis**<br/>**Z32 Preisblatt Messstellenbetrieb**<br/>**Z54 Preisblatt Sperren / Entsperren und**<br/>**Verzugskosten**<br/>**Z64 Preisblatt Netznutzung ohne**<br/>**gemeindespezifische Konzessionsabgaben**<br/>**Z67 Preisblatt Blindarbeit**<br/>**Z70 Preisblatt Netznutzung: Gemeindespezifische**<br/>Konzessionsabgaben<br/>**Z77 Preisblatt Konfigurationen**<br/>**Z94 Preisblatt Technik**|
|C106|Dokumenten-/Nachrichten-<br/>Identifikation|C||R|||
|1004|Dokumentennummer|C|an..70|R|an..70|*EDI-Nachrichtennummer vergeben vom Absender des*<br/>*Dokuments. Eindeutige Referenz zur Identifikation der*<br/>*Nachricht.*|
|1225|Nachrichtenfunktion, Code|C|an..3|N||Nicht benutzt|
|4343|Art der Antwort, Code|C|an..3|N||Nicht benutzt|
|1373|Dokumentenstatus, Code|C|an..3|D|an..3|**11 Dokument nicht verfügbar**|


## Bemerkung:

Dieses Segment dient dazu, Typ und Funktion anzuzeigen und die Identifikationsnummer zu übermitteln.

DE1373: Mit dem Code 11 kann die Aussage getroffen werden, dass das Preisblatt ohne Inhalt übermittelt und somit keine
Leistung dieses Preisblatttyps angeboten wird.

Folgendes Informationstripel stellt eine Eindeutigkeit einer PRICAT zur Übertragung des Ausgleichsenergiepreises her:

Inhalt von DE1004 des BGM-Segments (d. h. die EDI-Nachrichtennummer)
Inhalt von DE2380 des DTM-Segments mit DE2005 = 492 (d. h. das Betrachtungszeitintervall)
Inhalt von DE3039 von SG2-NAD mit DE3035 = MS (d. h. MP-ID des PRICAT-Versenders)

Sollte der Fall eintreten, dass Inhalte einer PRICAT falsch sind, so ändert sich an diesem Informationstripel der neuen, die
korrigierten Daten enthaltenden PRICAT die EDI-Nachrichtennummer. Die Entscheidung welche PRICAT zu verwenden ist, ergibt
sich über das in DE2380 des DTM-Segments mit DE2005 = 137 (d. h. das Dokumentendatum), wobei immer das jüngste Dokument
gültig ist.

Die Eindeutigkeit aller anderen Preisblätter als das zur Übermittlung der Ausgleichsenergiepreise ist durch die EDI-
Nachrichtennummer (Inhalt von DE1004 des BGM-Segments) und der MP-ID des PRICAT-Versenders, d. h. dem Inhalt des DE3039
von SG2-NAD mit DE3035 = MS gegeben.

### Beispiel:

BGM+Z54+1313+++11'

Bez = Objekt-Bezeichner
Nr = Laufende Segmentnummer im Guide
MaxWdh = Maximale Wiederholung der Segmente/Gruppen
Zähler = Nummer der Segmente/Gruppen im Standard
St = Status
EDIFACT: M=Muss/Mandatory, C=Conditional
Anwendung: R=Erforderlich/Required, O=Optional, D=Abhängig von/
Dependent, N=Nicht benutzt/Not used
Version: 2.0e 30.09.2025 Seite: 6 / 33

PRICAT MIG

![edi@energy. Datenformate Strom & Gas](ggde)

## **Segmentlayout**

|Zähler|Nr|Bez|St|MaxWdh|St|MaxWdh|Ebene|Name|
|-|-|-|-|-|-|-|-|-|
|0030|00003|DTM|M|35|D|1|1|Betrachtungszeitintervall|


|Bez|Name|Standard<br/>St|Standard<br/>Format|BDEW<br/>St|BDEW<br/>Format|Anwendung / Bemerkung|
|-|-|-|-|-|-|-|
|DTM|||||||
|C507|Datum/Uhrzeit/Zeitspanne|M||M|||
|2005|Datums- oder Uhrzeit- oder<br/>Zeitspannen-Funktion,<br/>Qualifier|M|an..3|M|an..3|**492 Bilanzierungsdatum, -zeit, -periode**|
|2380|Datum oder Uhrzeit oder<br/>Zeitspanne, Wert|C|an..35|R|an..35||
|2379|Datums- oder Uhrzeit- oder<br/>Zeitspannen-Format, Code|C|an..3|R|an..3|**610 CCYYMM**|


## **Bemerkung:**

Das Segment dient zur Übermittlung des Betrachtungszeitintervalls.
Das **Betrachtungszeitintervall** ist immer ein Kalendermonat.

## **Beispiel:**

DTM+492:201105:610'









Seite: 7

Bez = Objekt-Bezeichner
Nr = Laufende Segmentnummer im Guide
MaxWdh = Maximale Wiederholung der Segmente/Gruppen
Zähler = Nummer der Segmente/Gruppen im Standard
St = Status
EDIFACT: M=Muss/Mandatory, C=Conditional
Anwendung: R=Erforderlich/Required, O=Optional, D=Abhängig von/
Dependent, N=Nicht benutzt/Not used
Version: 2.0e
30.09.2025
/ 33

PRICAT MIG

![edi@energy. Datenformate Strom & Gas](emnt)

## **Segmentlayout**

|Zähler|Nr|Bez|St|MaxWdh|St|MaxWdh|Ebene|Name|
|-|-|-|-|-|-|-|-|-|
|0030|00004|DTM|M|35|M|1|1|Nachrichtendatum|


|Bez|Name|Standard<br/>St|Standard<br/>Format|BDEW<br/>St|BDEW<br/>Format|Anwendung / Bemerkung|
|-|-|-|-|-|-|-|
|DTM|||||||
|C507|Datum/Uhrzeit/Zeitspanne|M||M|||
|2005|Datums- oder Uhrzeit- oder<br/>Zeitspannen-Funktion,<br/>Qualifier|M|an..3|M|an..3|**137 Dokumenten-/Nachrichtendatum/-zeit**|
|2380|Datum oder Uhrzeit oder<br/>Zeitspanne, Wert|C|an..35|R|an..35||
|2379|Datums- oder Uhrzeit- oder<br/>Zeitspannen-Format, Code|C|an..3|R|an..3|**303 CCYYMMDDHHMMZZZ**|


### **Bemerkung:**

Dieses Segment wird zur Angabe des Dokumentendatums verwendet.

### **DE2380:**

Hier ist das Datum der Erstellung der Ausgleichsenergiepreisliste durch den BIKO oder das Datum der Erstellung des Preisblatts durch den MSB bzw. NB anzugeben.

### Im Fall der Ausgleichsenergiepreisliste gilt:

Werden mehrere PRICAT für dasselbe Zeitintervall vom selben BIKO versendet, so ist immer die PRICAT mit dem jüngsten Dokumentendatum gültig.

### **Beispiel:**

DTM+137:201106031826?+00:303'

Bez = Objekt-Bezeichner
Nr = Laufende Segmentnummer im Guide
MaxWdh = Maximale Wiederholung der Segmente/Gruppen
Zähler = Nummer der Segmente/Gruppen im Standard
St = Status
EDIFACT: M=Muss/Mandatory, C=Conditional
Anwendung: R=Erforderlich/Required, O=Optional, D=Abhängig von/
Dependent, N=Nicht benutzt/Not used

Version: 2.0e 30.09.2025 Seite: 8 / 33

PRICAT MIG

![edi@energy. Datenformate Strom & Gas](jmpj)

## **Segmentlayout**

|Zähler|Nr|Bez|St|MaxWdh|St|MaxWdh|Ebene|Name|
|-|-|-|-|-|-|-|-|-|
|0030|00005|DTM|M|35|D|1|1|**Gültigkeitsbeginn**|
|Bez Name|||St|Format|St|Format|Anwendung / Bemerkung||
|DTM|||||||||
|C507|Datum/Uhrzeit/Zeitspanne||M||M||||
|2005|Datums- oder Uhrzeit- oder<br/>Zeitspannen-Funktion,<br/>Qualifier||M|an..3|M|an..3|**157 Gültigkeit, Beginndatum**||
|2380|Datum oder Uhrzeit oder<br/>Zeitspanne, Wert||C|an..35|R|an..35|||
|2379|Datums- oder Uhrzeit- oder<br/>Zeitspannen-Format, Code||C|an..3|R|an..3|**303 CCYYMMDDHHMMZZZ**||


### Bemerkung:

Das Segment dient zur Übermittlung des Zeitpunkts, zu dem das Preisblatt gültig wird.

Zu dem hier angegebenen Zeitpunkt beginnt die Gültigkeit des Preisblatts. Dieser Zeitpunkt stellt gleichzeitig den Zeitpunkt dar, zu dem das diesem Preisblatt vorausgehende Preisblatt seine Gültigkeit verliert. Das heißt, wenn t1 der Zeitpunkt ist, zu dem das Vorgängerpreisblatt gültig wurde und t2 der hier genannte Zeitpunkt ist, und für t2 gilt, dass
t1 < t2, dann ergibt sich als Gültigkeitszeitraum für das Vorgängerpreisblatt der Zeitraum [t1; t2[
t1 = t2, dann ergibt sich, dass das Vorgängerpreisblatt ungültig ist.

### Beispiel:

DTM+157:201801012300?+00:303'

Bez = Objekt-Bezeichner
Nr = Laufende Segmentnummer im Guide
MaxWdh = Maximale Wiederholung der Segmente/Gruppen
Zähler = Nummer der Segmente/Gruppen im Standard
St = Status
EDIFACT: M=Muss/Mandatory, C=Conditional
Anwendung: R=Erforderlich/Required, O=Optional, D=Abhängig von/
Dependent, N=Nicht benutzt/Not used
Version: 2.0e          30.09.2025          <page_number>Seite: 9 / 33</page_number>

PRICAT MIG

![edi@energy. Datenformate Strom & Gas](vkzb)

## **Segmentlayout**

|Zähler|Nr|Bez|St|MaxWdh|St|MaxWdh|Ebene|Name|
|-|-|-|-|-|-|-|-|-|
|0060||**SG1**|C|99|D|1|1|Vorgängerversion|
|0070|00006|RFF|M|1|M|1|1|Vorgängerversion|


|||Standard<br/>Bez|Standard<br/>Name|BDEW<br/>St|BDEW<br/>Format|BDEW<br/>St|Format|Anwendung / Bemerkung|
|-|-|-|-|-|-|-|-|-|
|RFF|||||||||
|C506|Referenz|||M|||||
|1153|Referenz, Qualifier|||M|an..3|M|an..3|**ACW Referenznummer einer vorangegangenen**<br/>Nachricht|
|1154|Referenz, Identifikation|||C|an..70|R|an..70||


## **Bemerkung:**

Dieses Segment dient zur Übermittlung der Dokumentennummer einer vorausgegangenen Meldung.
Es muss die Dokumentennummer der Nachricht angegeben werden, in deren Gültigkeitszeitraum der Gültigkeitsbeginn dieser
Nachricht liegt. Alle Nachrichten mit einem jüngeren Gültigkeitsbeginn werden dadurch ungültig. Werden sie noch benötigt,
müssen sie erneut gesendet werden, wobei die Nachricht, die das Ende der Gültigkeit dieser Nachricht festlegt, in diesem
Segment die Dokumentnummer dieser Nachricht enthalten muss.

## **Beispiel:**

RFF+ACW:123GSDF3434'

Bez = Objekt-Bezeichner
Nr = Laufende Segmentnummer im Guide
MaxWdh = Maximale Wiederholung der Segmente/Gruppen
Zähler = Nummer der Segmente/Gruppen im Standard

St = Status
EDIFACT: M=Muss/Mandatory, C=Conditional
Anwendung: R=Erforderlich/Required, O=Optional, D=Abhängig von/
Dependent, N=Nicht benutzt/Not used

Version: 2.0e

30.09.2025

Seite: 10 / 33

PRICAT MIG

![edi@energy. Datenformate Strom & Gas](cekd)

## **Segmentlayout**

|Zähler|Nr|Bez|St|MaxWdh|St|MaxWdh|Ebene|Name|
|-|-|-|-|-|-|-|-|-|
|0060||**SG1**|C|99|D|1|1|Preise des Netzbetreibers|
|0070|00007|RFF|M|1|M|1|1|Preise des Netzbetreibers|


|Bez|Name|Standard<br/>St|Standard<br/>Format|BDEW<br/>St|BDEW<br/>Format|BDEW<br/>Anwendung / Bemerkung|
|-|-|-|-|-|-|-|
|RFF|||||||
|C506|Referenz|M||M|||
|1153|Referenz, Qualifier|M|an..3|M|an..3|**Z56 Preise des Netzbetreibers**|
|1154|Referenz, Identifikation|C|an..70|R|an..35|MP-ID|


### **Bemerkung:**

In diesem Segment wird die MP-ID des Netzbetreibers genannt, dessen Netzentgelte in der PRICAT ausgetauscht werden.

Hinweis: Hat der NB, der diese PRICAT versendet, ein Konzessionsgebiet nicht zum Beginn eines Kalenderjahres übernommen, so gelten für alle in diesem Konzessionsgebiet befindlichen Marktlokationen bis zum Ende des Kalenderjahres, in dem sie von diesem NB übernommen wurden, die Netznutzungspreise des NB, dem sie noch zu Beginn des Kalenderjahres zugeordnet waren. Damit der NB, der dieses Konzessionsgebiet somit unterjährig übernommen hat, zusätzlich diese Netzentgelte unter Nutzung der Artikel-ID den LF mitteilen kann, muss er in der PRICAT, in der er diese angibt, die MP-ID des NB angeben, von dem er das Konzessionsgebiet übernommen hat.

### **Beispiel:**

RFF+Z56:9907165000001'

Bez = Objekt-Bezeichner
Nr = Laufende Segmentnummer im Guide
MaxWdh = Maximale Wiederholung der Segmente/Gruppen
Zähler = Nummer der Segmente/Gruppen im Standard
St = Status
EDIFACT: M=Muss/Mandatory, C=Conditional
Anwendung: R=Erforderlich/Required, O=Optional, D=Abhängig von/
Dependent, N=Nicht benutzt/Not used
Version: 2.0e    30.09.2025    <page_number>Seite: 11 / 33</page_number>

PRICAT MIG

![edi@energy. Datenformate Strom & Gas](khfn)

## **Segmentlayout**

|Zähler|Nr|Bez|St|MaxWdh|St|MaxWdh|Ebene|Name|
|-|-|-|-|-|-|-|-|-|
|0060||**SG1**|C|99|R|1|1|Prüfidentifikator|
|0070|00008|RFF|M|1|M|1|1|Prüfidentifikator|

|Bez|Name|St|Format|St|Format|Anwendung / Bemerkung|
|-|-|-|-|-|-|-|
|RFF|||||||
|C506|Referenz|M||M|||
|1153|Referenz, Qualifier|M|an..3|M|an..3|**Z13 Prüfidentifikator**|
|1154|Referenz, Identifikation|C|an..70|R|n5|Prüfidentifikator<br/>**27001 Übermittlung der Ausgleichsenergiepreise**<br/>**27002 Preisblatt MSB-Leistungen**<br/>**27003 Preisblatt NB-Leistungen**|


### **Bemerkung:**

Das Segment dient zur Übermittlung des *Prüfidentifikator*s.

**Beispiel:**
RFF+Z13:27001'

Bez = Objekt-Bezeichner
Nr = Laufende Segmentnummer im Guide
MaxWdh = Maximale Wiederholung der Segmente/Gruppen
Zähler = Nummer der Segmente/Gruppen im Standard
St = Status
EDIFACT: M=Muss/Mandatory, C=Conditional
Anwendung: R=Erforderlich/Required, O=Optional, D=Abhängig von/
Dependent, N=Nicht benutzt/Not used

Version: 2.0e
30.09.2025
Seite: 12 / 33

PRICAT MIG

![edi@energy. Datenformate Strom & Gas](ijfd)

## **Segmentlayout**

|Zähler|Nr|Bez|St|MaxWdh|St|MaxWdh|Ebene|Name|
|-|-|-|-|-|-|-|-|-|
|0090||**SG2**|C|99|R|1|1|Empfänger-ID|
|0100|00009|NAD|M|1|M|1|1|Empfänger-ID|

|Bez|Name|St|Format|St|Format|Anwendung / Bemerkung|
|-|-|-|-|-|-|-|
|NAD|||||||
|3035|Beteiligter, Qualifier|M|an..3|M|an..3|**MR Nachrichtenempfänger**|
|C082|Identifikation des Beteiligten|C||R|||
|3039|Beteiligter, Identifikation|M|an..35|M|an..35|MP-ID|
|1131|Codeliste, Code|C|an..17|N||Nicht benutzt|
|3055|Verantwortliche Stelle für die<br/>Codepflege, Code|C|an..3|R|an..3|**9 GS1**<br/>**293 DE, BDEW (Bundesverband der Energie- und**<br/>**Wasserwirtschaft e.V.)**<br/>**332 DE, DVGW Service & Consult GmbH**|


## Bemerkung:

**DE3039:**

Zur Identifikation der Partner wird die *MP-ID* angegeben.

## Beispiel:

NAD+MR+4078901000029::9'

Bez = Objekt-Bezeichner
Nr = Laufende Segmentnummer im Guide
MaxWdh = Maximale Wiederholung der Segmente/Gruppen
Zähler = Nummer der Segmente/Gruppen im Standard

St = Status
EDIFACT: M=Muss/Mandatory, C=Conditional
Anwendung: R=Erforderlich/Required, O=Optional, D=Abhängig von/
Dependent, N=Nicht benutzt/Not used

Version: 2.0e

30.09.2025

Seite: 13 / 33

PRICAT MIG

![edi@energy. Datenformate Strom & Gas](cblb)

## **Segmentlayout**

|Zähler|Nr|Bez|St|MaxWdh|St|MaxWdh|Ebene|Name|
|-|-|-|-|-|-|-|-|-|
|0090||**SG2**|C|99|R|1|1|Sender-ID|
|0100|00010|NAD|M|1|M|1|1|Sender-ID|


|Bez|Name|Standard<br/>St|Standard<br/>Format|BDEW<br/>St|BDEW<br/>Format|Anwendung / Bemerkung|
|-|-|-|-|-|-|-|
|NAD|||||||
|3035|Beteiligter, Qualifier|M|an..3|M|an..3|**MS Dokumenten-/Nachrichtenaussteller bzw. -**<br/>**absender**|
|C082|Identifikation des Beteiligten|C||R|||
|3039|Beteiligter, Identifikation|M|an..35|M|an..35|*MP-ID*|
|1131|Codeliste, Code|C|an..17|N||Nicht benutzt|
|3055|Verantwortliche Stelle für die<br/>Codepflege, Code|C|an..3|R|an..3|**9 GS1**<br/>**293 DE, BDEW (Bundesverband der Energie- und**<br/>**Wasserwirtschaft e.V.)**<br/>**332 DE, DVGW Service & Consult GmbH**|


## **Bemerkung:**

DE3039:
Zur Identifikation der Partner wird die *MP-ID* angegeben.

## **Beispiel:**
NAD+MS+4012345000023::9'

Bez = Objekt-Bezeichner
Nr = Laufende Segmentnummer im Guide
MaxWdh = Maximale Wiederholung der Segmente/Gruppen
Zähler = Nummer der Segmente/Gruppen im Standard

St = Status
EDIFACT: M=Muss/Mandatory, C=Conditional
Anwendung: R=Erforderlich/Required, O=Optional, D=Abhängig von/
Dependent, N=Nicht benutzt/Not used

Version: 2.0e

30.09.2025

Seite: 14 / 33

PRICAT MIG

![edi@energy. Datenformate Strom & Gas](cjow)

# **Segmentlayout**

|Zähler|Nr|Bez|StandardSt MaxWdh|StandardSt MaxWdh|BDEWSt MaxWdh|BDEWSt MaxWdh|Ebene|Name|
|-|-|-|-|-|-|-|-|-|
|0090||**SG2**|C|99|R|1|1|**Sender-ID**|
|0110|00011|LOC|C|25|D|1|2|Regelzone|


|Bez|Name|Standard<br/>St|Standard<br/>Format|BDEW<br/>St|BDEW<br/>Format|Anwendung / Bemerkung|
|-|-|-|-|-|-|-|
|LOC|||||||
|3227|Ortsangabe, Qualifier|M|an..3|M|an..3|****231 Regelzone****|
|C517|Ortsangabe|C||R|||
|3225|Ortsangabe, Nummer|C|an..35|R|an..35|*Regelzone wird als EIC-Code übertragen*|


## **Bemerkung:**

Dieses Segment dient der Angabe von Lokationen.
Im vorliegenden Fall wird die Regelzone angegeben.

## **Beispiel:**

LOC+231+10YDE-VNBNET---9'

Bez = Objekt-Bezeichner
Nr = Laufende Segmentnummer im Guide
MaxWdh = Maximale Wiederholung der Segmente/Gruppen
Zähler = Nummer der Segmente/Gruppen im Standard

St = Status
EDIFACT: M=Muss/Mandatory, C=Conditional
Anwendung: R=Erforderlich/Required, O=Optional, D=Abhängig von/
Dependent, N=Nicht benutzt/Not used

Version: 2.0e

30.09.2025

Seite: 15 / 33

PRICAT MIG

![edi@energy logo](pjla)

## **Segmentlayout**

|Zähler|Nr|Bez|St|MaxWdh|St|MaxWdh|Ebene|Name|
|-|-|-|-|-|-|-|-|-|
|0090||**SG2**|C|99|R|1|1|**Sender-ID**|
|0150||**SG4**|C|5|O|1|2|**CTA-COM**|
|0160|00012|CTA|M|1|M|1|2|**Ansprechpartner**|


|Bez|Name|Standard<br/>St|Standard<br/>Format|BDEW<br/>St|BDEW<br/>Format|Anwendung / Bemerkung|
|-|-|-|-|-|-|-|
|CTA|||||||
|3139|Funktion des<br/>Ansprechpartners, Code|C|an..3|R|an..3|**IC Informationskontakt**|
|C056|Kontaktangaben|C||R|||
|3413|Kontakt, Nummer|C|an..17|N||Nicht benutzt|
|3412|Kontakt|C|an..256|R|an..256||


### **Bemerkung:**

Dieses Segment dient der Identifikation von Ansprechpartnern innerhalb des im vorangegangenen NAD-Segment spezifizierten Unternehmens.

**Beispiel:**

CTA+IC+:B. Zweistein'

Bez = Objekt-Bezeichner
Nr = Laufende Segmentnummer im Guide
MaxWdh = Maximale Wiederholung der Segmente/Gruppen
Zähler = Nummer der Segmente/Gruppen im Standard

St = Status
EDIFACT: M=Muss/Mandatory, C=Conditional
Anwendung: R=Erforderlich/Required, O=Optional, D=Abhängig von/
Dependent, N=Nicht benutzt/Not used

Seite: 16 / 33

Version: 2.0e 30.09.2025

PRICAT MIG

![edi@energy. Datenformate Strom & Gas](rgsb)

## **Segmentlayout**

|Zähler|Nr|Bez|St|MaxWdh|St|MaxWdh|Ebene|Name|
|-|-|-|-|-|-|-|-|-|
|0090||**SG2**|C|99|R|1|1|**Sender-ID**|
|0150||**SG4**|C|5|O|1|2|**CTA-COM**|
|0170|00013|COM|C|5|R|5|3|Kommunikationsverbindung|


|Bez|Name|Standard<br/>St|Standard<br/>Format|BDEW<br/>St|BDEW<br/>Format|BDEW<br/>Anwendung / Bemerkung|
|-|-|-|-|-|-|-|
|COM|||||||
|C076|Kommunikationsverbindung|M||M|||
|3148|Kommunikationsadresse,<br/>Identifikation|M|an..512|M|an..512||
|3155|Art des<br/>Kommunikationsmittels, Code|M|an..3|M|an..3|**EM E-Mail**<br/>**FX Telefax**<br/>**TE Telefon**<br/>**AJ weiteres Telefon**<br/>**AL Handy**|


### **Bemerkung:**

Ein Segment zur Angabe von Kommunikationsnummer und -typ des im vorangegangenen CTA-Segments angegebenen
Sachbearbeiters oder der Abteilung.

### DE3155:

Es ist jeder Qualifier max. einmal zu verwenden.

### **Beispiel:**

COM+b.zweistein@diamagnetischereffekt.de:EM'

Bez = Objekt-Bezeichner
Nr = Laufende Segmentnummer im Guide
MaxWdh = Maximale Wiederholung der Segmente/Gruppen
Zähler = Nummer der Segmente/Gruppen im Standard
St = Status
EDIFACT: M=Muss/Mandatory, C=Conditional
Anwendung: R=Erforderlich/Required, O=Optional, D=Abhängig von/
Dependent, N=Nicht benutzt/Not used

Version: 2.0e

30.09.2025

Seite: 17 / 33

PRICAT MIG

![edi@energy. Datenformate Strom & Gas](vadl)

## **Segmentlayout**

|Zähler|Nr|Bez|St|MaxWdh|St|MaxWdh|Ebene|Name|
|-|-|-|-|-|-|-|-|-|
|0220||**SG6**|C|20|D|1|1|Währungsangaben|
|0230|00014|CUX|M|1|M|1|1|Währungsangaben|


|Bez|Name|Standard<br/>St|Standard<br/>Format|BDEW<br/>St|BDEW<br/>Format|Anwendung / Bemerkung|
|-|-|-|-|-|-|-|
|CUX|||||||
|C504|Währungsangaben|C||R|||
|6347|Währungsverwendung,<br/>Qualifier|M|an..3|M|an..3|**2 Referenzwährung**|
|6345|Währung, Code|C|an..3|R|an..3|**EUR Euro**|
|6343|Währung, Qualifier|C|an..3|R|an..3|**8 Währung der Preisliste**|


## **Bemerkung:**

Dieses Segment wird benutzt, um Währungsangaben für die gesamte Preisliste anzugeben.

## **Beispiel:**

CUX+2:EUR:8'

Bez = Objekt-Bezeichner
Nr = Laufende Segmentnummer im Guide
MaxWdh = Maximale Wiederholung der Segmente/Gruppen
Zähler = Nummer der Segmente/Gruppen im Standard

St = Status
EDIFACT: M=Muss/Mandatory, C=Conditional
Anwendung: R=Erforderlich/Required, O=Optional, D=Abhängig von/
Dependent, N=Nicht benutzt/Not used

Version: 2.0e 30.09.2025 Seite: 18 / 33

PRICAT MIG

![edi@energy. Datenformate Strom & Gas](xflk)

## **Segmentlayout**

|Zähler|Nr|Bez|St|MaxWdh|St|MaxWdh|Ebene|Name|
|-|-|-|-|-|-|-|-|-|
|0590||**SG17**|C|1000|D|1|1|**PGI-SG36**|
|0600|00015|PGI|M|1|M|1|1|**Produktgruppen-Information**|


|Standard<br/>Bez|Standard<br/>Name|Standard<br/>St Format|BDEW<br/>St Format|BDEW<br/>Anwendung / Bemerkung|BDEW<br/>Anwendung / Bemerkung|
|-|-|-|-|-|-|
|PGI||||||
|5379|Produktgruppen-Art, Code|M an..3|M an..3|9|keine Gruppe genutzt|


## **Bemerkung:**

Dieses Segment wird genutzt, um die darunterliegende Segmentgruppe eröffnen zu können.

## **Beispiel:**

PGI+9'

Bez = Objekt-Bezeichner
Nr = Laufende Segmentnummer im Guide
MaxWdh = Maximale Wiederholung der Segmente/Gruppen
Zähler = Nummer der Segmente/Gruppen im Standard

St = Status
EDIFACT: M=Muss/Mandatory, C=Conditional
Anwendung: R=Erforderlich/Required, O=Optional, D=Abhängig von/
Dependent, N=Nicht benutzt/Not used

Version: 2.0e

30.09.2025

Seite: 19     /  33

PRICAT MIG

![edi@energy. Datenformate Strom & Gas](gnwk)

## **Segmentlayout**

|Zähler|Nr|Bez|St|MaxWdh|St|MaxWdh|Ebene|Name|
|-|-|-|-|-|-|-|-|-|
|0590||**SG17**|C|1000|D|1|1|**PGI-SG36**|
|1310||SG36|C|999999|R|999999|2|**LIN-PIA-IMD-SG40**|
|1320|00016|LIN|M|1|M|1|2|**Positionsdaten**|


|Bez|Name|Standard<br/>St|Standard<br/>Format|BDEW<br/>St|BDEW<br/>Format|Anwendung / Bemerkung|
|-|-|-|-|-|-|-|
|LIN|||||||
|1082|Positionsnummer|C|an..6|R|n..6|*Vom Programm vergebene Positionsnummer innerhalb der*<br/>*Nachricht (fortlaufende Nummer von 1 bis n)*|
|1229|Handlung, Code|C|an..3|N||Nicht benutzt|
|C212|Waren-/Leistungsnummer,<br/>Identifikation|C||R|||
|7140|Produkt-/Leistungsnummer|C|an..35|R|an..35|*Artikelnummer des BDEW / Artikel-ID des BDEW*|
|7143|Art der Produkt-/<br/>Leistungsnummer, Code|C|an..3|R|an..3|**Z01 Artikelnummer**<br/>**Z09 Artikel-ID**|


### **Bemerkung:**

Dieses Segment zeigt den Beginn des Positionsteils innerhalb der Nachricht an. Der Positionsteil wird durch Wiederholung von
Segmentgruppen gebildet, die immer mit einem LIN-Segment beginnen.

DE7140: Es sind ausschließlich Codes nutzbar, die in der jeweils gültigen Version der EDI@Energy-Codeliste der Artikelnummern
und Artikel-ID enthalten sind.

**Beispiel:**

LIN+1++9990001000631:Z01'

Bez = Objekt-Bezeichner
Nr = Laufende Segmentnummer im Guide
MaxWdh = Maximale Wiederholung der Segmente/Gruppen
Zähler = Nummer der Segmente/Gruppen im Standard

St = Status
EDIFACT: M=Muss/Mandatory, C=Conditional
Anwendung: R=Erforderlich/Required, O=Optional, D=Abhängig von/
Dependent, N=Nicht benutzt/Not used

Version: 2.0e

30.09.2025

Seite: 20 / 33

PRICAT MIG

![edi@energy. Datenformate Strom & Gas](pkgf)

## **Segmentlayout**

|Zähler|Nr|Bez|St|MaxWdh|St|MaxWdh|Ebene|Name|
|-|-|-|-|-|-|-|-|-|
|0590||**SG17**|C|1000|D|1|1|**PGI-SG36**|
|1310||SG36|C|999999|R|999999|2|**LIN-PIA-IMD-SG40**|
|1330|00017|PIA|C|99|D|1|3|Preisschlüsselstamm|


|Bez|Standard<br/>Name|Standard<br/>St|Standard<br/>Format|BDEW<br/>St|BDEW<br/>Format|BDEW<br/>Anwendung / Bemerkung|
|-|-|-|-|-|-|-|
|PIA|||||||
|4347|Produkt-/Erzeugnisnummer, Qualifier|M|an..3|M|an..3|**1 Zusätzliche Identifikation**|
|C212|Waren-/Leistungsnummer, Identifikation|M||M|||
|7140|Produkt-/Leistungsnummer|C|an..35|R|an..35|Code des Preisschlüsselstamms|
|7143|Art der Produkt-/<br/>Leistungsnummer, Code|C|an..3|R|an..3|**Z06 Preisschlüsselstamm**|


## **Bemerkung:**

Das Segment dient zur Übermittlung des Preisschlüsselstamms.

Der Preisschlüsselstamm wird vom Ersteller der PRICAT vergeben. Ein Preisschlüsselstamm muss je PRICAT-Ersteller eindeutig sein.

## **Beispiel:**

PIA+1+FX12:Z06'

Bez = Objekt-Bezeichner
Nr = Laufende Segmentnummer im Guide
MaxWdh = Maximale Wiederholung der Segmente/Gruppen
Zähler = Nummer der Segmente/Gruppen im Standard

St = Status
EDIFACT: M=Muss/Mandatory, C=Conditional
Anwendung: R=Erforderlich/Required, O=Optional, D=Abhängig von/
Dependent, N=Nicht benutzt/Not used

Version: 2.0e 30.09.2025 Seite: 21 / 33

PRICAT MIG

![edi@energy. Datenformate Strom & Gas](wzbs)

## **Segmentlayout**

|Zähler|Nr|Bez|St|MaxWdh|St|MaxWdh|Ebene|Name|
|-|-|-|-|-|-|-|-|-|
|0590||****SG17****|C|1000|D|1|1|****PGI-SG36****|
|1310||**SG36**|C|999999|R|999999|2|****LIN-PIA-IMD-SG40****|
|1340|00018|**IMD**|C|999|D|1|3|****Produktbeschreibung****|


|Bez|Name|Standard<br/>St|Standard<br/>Format|BDEW<br/>St|BDEW<br/>Format|Anwendung / Bemerkung|
|-|-|-|-|-|-|-|
|IMD|||||||
|7077|Beschreibungsformat, Code|C|an..3|R|an..3|****C Code (aus der Liste einer codepflegenden** **Organisation)****<br/>****F Freier Text****<br/>****X Teilstrukturiert (Code und Text)****|
|C272|Produkt/Leistung|C||D|||
|7081|Produkt/Leistung, Code|C|an..3|R|an..3|****Z15 POG bei verbrauchender Marktlokation >** **100.000 kWh/a mit iMS****<br/>§ 31 MsbG, Abs. 1 Punkt 1<br/>Angemessenes Entgelt für mit iMS ausgestattete Marktlokation mit einem Jahresstromverbrauch von über 100 000 Kilowattstunden|
|||||||**Z16 POG bei verbrauchender Marktlokation ]50.**000 kWh/a; 100.000 kWh/a] mit iMS****<br/>§ 31 MsbG, Abs. 1 Punkt 2<br/>Nicht mehr als 200 Euro brutto jährliches Entgelt für mit iMS ausgestattete Marktlokation mit einem Jahresstromverbrauch von über 50 000 bis einschließlich 100 000 Kilowattstunden|
|||||||**Z17 POG bei verbrauchender Marktlokation ]20.**000 kWh/a; 50.000 kWh/a] mit iMS****<br/>§ 31 MsbG, Abs. 1 Punkt 3<br/>Nicht mehr als 170 Euro brutto jährliches Entgelt für mit iMS ausgestattete Marktlokation mit einem Jahresstromverbrauch von über 20 000 bis einschließlich 50 000 Kilowattstunden|
|||||||**Z18 POG bei verbrauchender Marktlokation ]10.**000 kWh/a; 20.000 kWh/a] mit iMS****<br/>§ 31 MsbG, Abs. 1 Punkt 4<br/>Nicht mehr als 130 Euro brutto jährliches Entgelt für mit iMS ausgestattete Marktlokation mit einem Jahresstromverbrauch von über 10 000 bis einschließlich 20 000 Kilowattstunden|
|||||||****Z19 POG bei verbrauchender Marktlokation mit** unterbrechbaren Verbrauchseinrichtung nach **§ 14a EnWG mit iMS****<br/>§ 31 MsbG, Abs. 1 Punkt 5<br/>Nicht mehr als 100 Euro brutto jährliches Entgelt für mit iMS ausgestattete Marktlokation mit unterbrechbaren Verbrauchseinrichtung nach § 14a EnWG|
|||||||****Z20 POG bei verbrauchender Marktlokation ]6.000** **kWh/a; 10.000 kWh/a] mit iMS****<br/>§ 31 MsbG, Abs. 1 Punkt 6|


Bez = Objekt-Bezeichner
Nr = Laufende Segmentnummer im Guide
MaxWdh = Maximale Wiederholung der Segmente/Gruppen
Zähler = Nummer der Segmente/Gruppen im Standard

St = Status
EDIFACT: M=Muss/Mandatory, C=Conditional
Anwendung: R=Erforderlich/Required, O=Optional, D=Abhängig von/
Dependent, N=Nicht benutzt/Not used

30.09.2025

Seite: 22 / 33

PRICAT MIG

![edi@energy. Datenformate Strom & Gas](swvj)

## **Segmentlayout**

|Bez|Name|St|Standard<br/>Format|Standard<br/>St|BDEW<br/>Format|Anwendung / Bemerkung|
|-|-|-|-|-|-|-|
|||||||Nicht mehr als 100 Euro brutto jährliches<br/>Entgelt für mit iMS ausgestattete Marktlokation<br/>mit einem Jahresstromverbrauch von über 6<br/>000 bis einschließlich 10 000 Kilowattstunden|
|Z21||||||**POG bei erzeugender Marktlokation ]7 kW; 15<br/>kW] mit iMS**<br/>§ 31 MsbG, Abs. 2 Punkt 1<br/>Nicht mehr als 100 Euro brutto jährliches<br/>Entgelt für mit iMS ausgestattete Marktlokation<br/>mit installierter Leistung über 7 bis<br/>einschließlich 15 Kilowatt|
|Z22||||||**POG bei erzeugender Marktlokation ]15 kW;<br/>**30 kW] mit iMS****<br/>§ 31 MsbG, Abs. 2 Punkt 2<br/>Nicht mehr als 130 Euro brutto jährliches<br/>Entgelt für mit iMS ausgestattete Marktlokation<br/>mit installierter Leistung über 15 bis<br/>einschließlich 30 Kilowatt|
|Z23||||||**POG bei erzeugender Marktlokation ]30 kW;<br/>**100 kW] mit iMS****<br/>§ 31 MsbG, Abs. 2 Punkt 3<br/>Nicht mehr als 200 Euro brutto jährliches<br/>Entgelt für mit iMS ausgestattete Marktlokation<br/>mit installierter Leistung über 30 bis<br/>einschließlich 100 Kilowatt|
|Z24||||||**POG bei erzeugender Marktlokation > 100 kW<br/>mit iMS**<br/>§ 31 MsbG, Abs. 2 Punkt 4<br/>angemessenes Entgelt für mit iMS<br/>ausgestattete Marktlokation mit installierter<br/>Leistung über 100 Kilowatt|
|Z25||||||**POG bei Marktlokation mit mME**<br/>§ 32 MsbG,<br/>nicht mehr als 20 Euro brutto jährlich für mit<br/>mME ausgestattete Marktlokation|
|Z28||||||**POG bei verbrauchender Marktlokation ]4.000<br/>**kWh/a; 6.000 kWh/a] mit iMS****<br/>§ 31 MsbG, Abs. 3 Punkt 1<br/>Ab 2020 nicht mehr als 60 Euro brutto<br/>jährliches Entgelt für mit iMS ausgestattete<br/>Marktlokation mit einem Jahresstromverbrauch<br/>von über 4 000 bis einschließlich 6 000<br/>Kilowattstunden|
|Z29||||||**POG bei verbrauchender Marktlokation ]3.000<br/>**kWh/a; 4.000 kWh/a] mit iMS****<br/>§ 31 MsbG, Abs. 3 Punkt 2<br/>Ab 2020 nicht mehr als 40 Euro brutto<br/>jährliches Entgelt für mit iMS ausgestattete<br/>Marktlokation mit einem Jahresstromverbrauch<br/>von über 3 000 bis einschließlich 4 000<br/>Kilowattstunden|
|Z30||||||**POG bei verbrauchender Marktlokation ]2.000<br/>**kWh/a; 3.000 kWh/a] mit iMS****<br/>§ 31 MsbG, Abs. 3 Punkt 3<br/>Ab 2020 nicht mehr als 30 Euro brutto<br/>jährliches Entgelt für mit iMS ausgestattete|


Bez = Objekt-Bezeichner
Nr = Laufende Segmentnummer im Guide
MaxWdh = Maximale Wiederholung der Segmente/Gruppen
Zähler = Nummer der Segmente/Gruppen im Standard

St = Status
EDIFACT: M=Muss/Mandatory, C=Conditional
Anwendung: R=Erforderlich/Required, O=Optional, D=Abhängig von/
Dependent, N=Nicht benutzt/Not used





Seite: 23 / 33

Version: 2.0e
30.09.2025

PRICAT MIG

![edi@energy. Datenformate Strom & Gas](plry)

## **Segmentlayout**

|Bez|Name|Standard<br/>St|Standard<br/>Format|BDEW<br/>St|BDEW<br/>Format|Anwendung / Bemerkung|
|-|-|-|-|-|-|-|
|||||||Marktlokation mit einem Jahresstromverbrauch<br/>von über 2 000 bis einschließlich 3 000<br/>Kilowattstunden<br/>**Z31 POG bei verbrauchender Marktlokation \[0**<br/>**kWh/a; 2.000 kWh/a] mit iMS**<br/>§ 31 MsbG, Abs. 3 Punkt 4<br/>Ab 2020 nicht mehr als 23 Euro brutto<br/>jährliches Entgelt für mit iMS ausgestattete<br/>Marktlokation mit einem Jahresstromverbrauch<br/>bis einschließlich 2 000 Kilowattstunden<br/>**Z32 POG bei optionaler Ausstattung mit iMS von**<br/>**Neuanlagen von erzeugender Marktlokation**<br/>§ 31 MsbG, Abs. 3<br/>Ab 2018 nicht mehr als 60 Euro brutto jährlich<br/>für optional mit iMS ausgestattete Neuanlage<br/>einer Marktlokation<br/>**Z41 Zusatzleistung**|
|C273|Produkt-/<br/>Leistungsbeschreibung|C||D|||
|7009|Produkt-/<br/>Leistungsbeschreibung, Code|C|an..17|D|an..17|*Spannungsebene der Primärwicklung des Wandlers*<br/>**Z08 Höchstspannung**<br/>**Z09 Hochspannung**<br/>**Z10 Mittelspannung**<br/>**Z11 Niederspannung**|
|1131|Codeliste, Code|C|an..17|N||Nicht benutzt|
|3055|Verantwortliche Stelle für die<br/>Codepflege, Code|C|an..3|N||Nicht benutzt|
|7008|Produkt-/<br/>Leistungsbeschreibung|C|an..256|D|an..256||
|7008|Produkt-/<br/>Leistungsbeschreibung|C|an..256|D|an..256||


### **Bemerkung:**

Das Segment dient zur Übermittlung der Produktbeschreibung.

### **Beispiel:**

`IMD+X+Z41+Z11:::Blockstromwandler und weitere Details zu diesem:X'`

Bez = Objekt-Bezeichner
Nr = Laufende Segmentnummer im Guide
MaxWdh = Maximale Wiederholung der Segmente/Gruppen
Zähler = Nummer der Segmente/Gruppen im Standard


St = Status
EDIFACT: M=Muss/Mandatory, C=Conditional
Anwendung: R=Erforderlich/Required, O=Optional, D=Abhängig von/
Dependent, N=Nicht benutzt/Not used
Version: 2.0e          30.09.2025          Seite: 24 / 33

PRICAT MIG

![edi@energy. Datenformate Strom & Gas](xpci)

## **Segmentlayout**

|Zähler|Nr|Bez|St|MaxWdh|St|MaxWdh|Ebene|Name|
|-|-|-|-|-|-|-|-|-|
|0590||**SG17**|C|1000|D|1|1|**PGI-SG36**|
|1310||SG36|C|999999|R|999999|2|**LIN-PIA-IMD-SG40**|
|1560||SG40|C|100|D|100|3|**Preisangabe**|
|1570|00019|PRI|M|1|M|1|3|Preisangaben|


|||Standard<br/>St|Standard<br/>Format|BDEW<br/>St|BDEW<br/>Format|BDEW<br/>Anwendung / Bemerkung|
|-|-|-|-|-|-|-|
|PRI|||||||
|C509|Preisinformation|C||R|||
|5125|Preis, Qualifier|M|an..3|M|an..3|**CAL Berechnungspreis**|
|5118|Preis, Betrag|C|n..15|R|n..15||
|5375|Preisart, Code|C|an..3|N||Nicht benutzt|
|5387|Preisart, Code|C|an..3|N||Nicht benutzt|
|5284|Einzelpreisbasis, Menge|C|n..9|D|n..9||
|6411|Maßeinheit, Code|C|an..8|D|an..8|ANN Jahr|


### **Bemerkung:**

Dieses Segment wird benutzt, um Preisangaben für die aktuelle Position anzugeben.
Es handelt sich um einen Nettopreis ohne USt.-Anteil.

Der hier übertragene Preis muss immer der Logik folgen, dass in der INVOIC wie folgt gerechnet werden kann: Menge (QTY-
Segment) * Preis (PRI-Segment unter Berücksichtigung von DE5284 und DE6411) = Positionsbetrag (MOA-Segment).

Hinweis zu DE5284 und DE6411 im Anwendungsfall "Ausgleichsenergiepreis":
Diese Angaben sind in diesem Fall nötig, um den Umrechnungsfaktor zwischen der im angegebenen Preis benutzen Mengenbasis
und in der MSCONS verwendeten und davon abweichenden Mengenbasis zu übermittelten.

### **Hinweis zum Preisblatt:**

Die Angaben in den Segmenten LIN (ohne den Inhalt des DE1082), PIA und IMD eines Preises müssen sich in mindestens einem
der genutzten Datenelemente von den Inhalten der Datenelemente jedes anderen Preises unterscheiden. Im DE6411 ist die
Maßeinheit **ANN** **Jahr** nur bei zeitabhängigen Preisen zu verwenden.

### **Beispiel:**

PRI+CAL:168.06::::ANN'

Bez = Objekt-Bezeichner
Nr = Laufende Segmentnummer im Guide
MaxWdh = Maximale Wiederholung der Segmente/Gruppen
Zähler = Nummer der Segmente/Gruppen im Standard
St = Status
EDIFACT: M=Muss/Mandatory, C=Conditional
Anwendung: R=Erforderlich/Required, O=Optional, D=Abhängig von/
Dependent, N=Nicht benutzt/Not used
Version: 2.0e 30.09.2025 Seite: 25 / 33

PRICAT MIG

![edi@energy. Datenformate Strom & Gas](kvif)

# **Segmentlayout**

|Zähler|Nr|Bez|St|MaxWdh|St|MaxWdh|Ebene|Name|
|-|-|-|-|-|-|-|-|-|
|0590||****SG17****|C|1000|D|1|1|**PGI-SG36**|
|1310||**SG36**|C|999999|R|999999|2|**LIN-PIA-IMD-SG40**|
|1560||**SG40**|C|100|D|100|3|**Preisangabe**|
|1600|00020|**RNG**|C|1|D|1|4|**Angaben zum Wertebereich**|


|Bez|Name|Standard<br/>St|Standard<br/>Format|BDEW<br/>St|BDEW<br/>Format|Anwendung / Bemerkung|
|-|-|-|-|-|-|-|
|RNG|||||||
|6167|Wertebereich, Qualifier|M|an..3|M|an..3|**10** jährlicher Mengenbereich|
|C280|Wertebereich|C||R|||
|6411|Maßeinheit, Code|M|an..8|M|an..8|**H87** Stück<br/>**DAY** Tag<br/>**KWH** Kilowattstunde|
|6162|Wertebereichsgrenze, untere|C|n..18|R|n..18||
|6152|Wertebereichsgrenze, obere|C|n..18|D|n..18||


## **Bemerkung:**

Wird die Leistung, deren Artikel-ID in LIN-Segment genannt ist, je Zone mit unterschiedlichen Preisen in Rechnung gestellt, so werden in diesem Segment die Zonengrenzen angegeben.

## **Beispiel:**

RNG+10+H87:9:9'

Bez = Objekt-Bezeichner
Nr = Laufende Segmentnummer im Guide
MaxWdh = Maximale Wiederholung der Segmente/Gruppen
Zähler = Nummer der Segmente/Gruppen im Standard
St = Status
EDIFACT: M=Muss/Mandatory, C=Conditional
Anwendung: R=Erforderlich/Required, O=Optional, D=Abhängig von/
Dependent, N=Nicht benutzt/Not used

Version: 2.0e 30.09.2025 Seite: 26 / 33

PRICAT MIG

![edi@energy. Datenformate Strom & Gas](cokm)

## **Segmentlayout**

|Zähler|Nr|Bez|St|MaxWdh|St|MaxWdh|Ebene|Name|
|-|-|-|-|-|-|-|-|-|
|0590||**SG17**|C|1000|D|1|1|**PGI-SG36**|
|1310||SG36|C|999999|R|999999|2|**LIN-PIA-IMD-SG40**|
|1560||SG40|C|100|D|100|3|**Preisangabe**|
|1610|00021|DTM|C|5|D|2|4|Datum/Uhrzeit/Zeitspanne|


|Bez|Name|Standard<br/>St|Standard<br/>Format|BDEW<br/>St|BDEW<br/>Format|Anwendung / Bemerkung|
|-|-|-|-|-|-|-|
|DTM|||||||
|C507|Datum/Uhrzeit/Zeitspanne|M||M|||
|2005|Datums- oder Uhrzeit- oder<br/>Zeitspannen-Funktion,<br/>Qualifier|M|an..3|M|an..3|**163 Verarbeitung, Beginndatum/-zeit**<br/>**164 Verarbeitung, Endedatum/-zeit**|
|2380|Datum oder Uhrzeit oder<br/>Zeitspanne, Wert|C|an..35|R|an..35||
|2379|Datums- oder Uhrzeit- oder<br/>Zeitspannen-Format, Code|C|an..3|R|an..3|**303 CCYYMMDDHHMMZZZ**|


## **Bemerkung:**

Dieses Segment dient der Angabe des Zeitintervalls für das der Preis gilt.

DE2005: Je PRI ist jeder der beiden Qualifier je einmal (in zwei aufeinanderfolgenden QTY-Segmenten) anzugeben.

DE2380: Wie an den Tagen der Umstellung auf Sommer/Winterzeit bzw. Winter/Sommerzeit dieses Segment zu füllen ist, ist dem MSCONS-AHB zu entnehmen.

**Beispiel:**

DTM+163:201104010815?+00:303'

Bez = Objekt-Bezeichner
Nr = Laufende Segmentnummer im Guide
MaxWdh = Maximale Wiederholung der Segmente/Gruppen
Zähler = Nummer der Segmente/Gruppen im Standard
St = Status
EDIFACT: M=Muss/Mandatory, C=Conditional
Anwendung: R=Erforderlich/Required, O=Optional, D=Abhängig von/
Dependent, N=Nicht benutzt/Not used
Version: 2.0e 30.09.2025 Seite: 27 / 33

PRICAT MIG

![edi@energy logo](dfff)

## **Segmentlayout**

|Zähler|Nr|Bez|St|MaxWdh|St|MaxWdh|Ebene|Name|
|-|-|-|-|-|-|-|-|-|
|0590||**SG17**|C|1000|D|1|1|Netzbetreiberindividuelle Artikel-ID|
|0600|00022|PGI|M|1|M|1|1|Netzbetreiberindividuelle Artikel-ID|


|Standard<br/>Bez|Standard<br/>Name|Standard<br/>St Format|BDEW<br/>St Format|BDEW<br/>Anwendung / Bemerkung|
|-|-|-|-|-|
|PGI|||||
|5379|Produktgruppen-Art, Code|M an..3|M an..3|**Z01 Netzbetreiberindividuelle Artikel-ID**|


### **Bemerkung:**

Dieses Segment wird genutzt, um die Preise und Zonen der gezonten Konzessionsabgabe austauschen zu können.

### **Beispiel:**

PGI+Z01'

Bez = Objekt-Bezeichner
Nr = Laufende Segmentnummer im Guide
MaxWdh = Maximale Wiederholung der Segmente/Gruppen
Zähler = Nummer der Segmente/Gruppen im Standard
St = Status
EDIFACT: M=Muss/Mandatory, C=Conditional
Anwendung: R=Erforderlich/Required, O=Optional, D=Abhängig von/
Dependent, N=Nicht benutzt/Not used

Version: 2.0e

30.09.2025

Seite: 28     /  33

PRICAT MIG

![edi@energy. Datenformate Strom & Gas](kraf)

## Segmentlayout

|Zähler|Nr|Bez|St|MaxWdh|St|MaxWdh|Ebene|Name|
|-|-|-|-|-|-|-|-|-|
|0590||**SG17**|C|1000|D|1|1|**Netzbetreiberindividuelle Artikel-ID**|
|1310||****SG36****|C|999999|R|999999|2|**Positionsdaten**|
|1320|00023|**LIN**|M|1|R|1|2|**Positionsdaten**|


|Bez|Name|Standard<br/>St|Standard<br/>Format|BDEW<br/>St|BDEW<br/>Format|Anwendung / Bemerkung|
|-|-|-|-|-|-|-|
|LIN|||||||
|1082|Positionsnummer|C|an..6|R|n..6|*Vom Programm vergebene Positionsnummer innerhalb der*<br/>*Nachricht (fortlaufende Nummer von 1 bis n)*|
|1229|Handlung, Code|C|an..3|N||Nicht benutzt|
|C212|Waren-/Leistungsnummer,<br/>Identifikation|C||R|||
|7140|Produkt-/Leistungsnummer|C|an..35|R|an..35||
|7143|Art der Produkt-/<br/>Leistungsnummer, Code|C|an..3|R|an..3|****Z09 Artikel-ID****|


### Bemerkung:

Dieses Segment zeigt den Beginn des Positionsteils innerhalb der **SG17** **Netzbetreiberindividuelle Artikel-ID** an. Der Positionsteil wird durch Wiederholung von Segmentgruppen gebildet, die immer mit einem **LIN**-Segment beginnen.

DE7140: Die in diesem Datenelement angegebene Artikel-ID enthält den gesamten String der netzbetreiberindividuellen Artikel-ID, der den Bildungsvorgaben genügt, die im Kapitel „Konzessionsabgaben“ der EDI@Energy Codeliste der Artikelnummern und Artikel-ID enthalten sind.

### Beispiel:

LIN+1++1-08-1-03254005-01-3:Z09'

Bez = Objekt-Bezeichner
Nr = Laufende Segmentnummer im Guide
MaxWdh = Maximale Wiederholung der Segmente/Gruppen
Zähler = Nummer der Segmente/Gruppen im Standard

St = Status
EDIFACT: M=Muss/Mandatory, C=Conditional
Anwendung: R=Erforderlich/Required, O=Optional, D=Abhängig von/
Dependent, N=Nicht benutzt/Not used

Version: 2.0e



Seite: 29 / 33

30.09.2025

PRICAT MIG

![edi@energy. Datenformate Strom & Gas](faab)

## **Segmentlayout**

|Zähler|Nr|Bez|St|MaxWdh|St|MaxWdh|Ebene|Name|
|-|-|-|-|-|-|-|-|-|
|0590||**SG17**|C|1000|D|1|1|**Netzbetreiberindividuelle Artikel-ID**|
|1310||**SG36**|C|999999|R|999999|2|**Positionsdaten**|
|1560||**SG40**|C|100|R|1|3|**Preisangabe**|
|1570|00024|PRI|M|1|M|1|3|Preisangaben|


|Standard<br/>Bez|Standard<br/>Name|Standard<br/>St|Standard<br/>Format|BDEW<br/>St|BDEW<br/>Format|BDEW<br/>Anwendung / Bemerkung|
|-|-|-|-|-|-|-|
|PRI|||||||
|C509|Preisinformation|C||R|||
|5125|Preis, Qualifier|M|an..3|M|an..3|**CAL Berechnungspreis**|
|5118|Preis, Betrag|C|n..15|R|n..15||


### **Bemerkung:**

Dieses Segment wird benutzt, um Preisangaben für die aktuelle Position anzugeben.
Es handelt sich um einen Nettopreis ohne USt.-Anteil.

Der hier übertragene Preis muss immer der Logik folgen, dass in der INVOIC wie folgt gerechnet werden kann: Menge (QTY-
Segment) * Preis (PRI-Segment unter Berücksichtigung von E6411) = Positionsbetrag (MOA-Segment).

### **Beispiel:**
PRI+CAL:168.06'

Bez = Objekt-Bezeichner
Nr = Laufende Segmentnummer im Guide
MaxWdh = Maximale Wiederholung der Segmente/Gruppen
Zähler = Nummer der Segmente/Gruppen im Standard

St = Status
EDIFACT: M=Muss/Mandatory, C=Conditional
Anwendung: R=Erforderlich/Required, O=Optional, D=Abhängig von/
Dependent, N=Nicht benutzt/Not used

Version: 2.0e

30.09.2025

Seite: 30 / 33

PRICAT MIG

![edi@energy. Datenformate Strom & Gas](gvce)

## **Segmentlayout**

|Zähler|Nr|Bez|St|MaxWdh|St|MaxWdh|Ebene|Name|
|-|-|-|-|-|-|-|-|-|
|0590||**SG17**|C|1000|D|1|1|**Netzbetreiberindividuelle Artikel-ID**|
|1310||**SG36**|C|999999|R|999999|2|**Positionsdaten**|
|1560||**SG40**|C|100|R|1|3|**Preisangabe**|
|1600|00025|RNG|C|1|D|1|4|**Zonenintervallgrenzen**|


|Bez|Name|Standard<br/>St|Standard<br/>Format|BDEW<br/>St|BDEW<br/>Format|Anwendung / Bemerkung|
|-|-|-|-|-|-|-|
|RNG|||||||
|6167|Wertebereich, Qualifier|M|an..3|M|an..3|**10 jährlicher Mengenbereich**|
|C280|Wertebereich|C||R|||
|6411|Maßeinheit, Code|M|an..8|R|an..8|**KWH Kilowattstunde**|
|6162|Wertebereichsgrenze, untere|C|n..18|R|n..18||
|6152|Wertebereichsgrenze, obere|C|n..18|D|n..18||


## **Bemerkung:**

## **Beispiel:**

RNG+10+KWH:0:12000'

Bez = Objekt-Bezeichner
Nr = Laufende Segmentnummer im Guide
MaxWdh = Maximale Wiederholung der Segmente/Gruppen
Zähler = Nummer der Segmente/Gruppen im Standard

**St = Status**
EDIFACT: M=Muss/Mandatory, C=Conditional
Anwendung: R=Erforderlich/Required, O=Optional, D=Abhängig von/
Dependent, N=Nicht benutzt/Not used

Version: 2.0e

30.09.2025

Seite: 31 / 33

PRICAT    MIG

![edi@energy. Datenformate Strom & Gas](atan)


# **Segmentlayout**

|Zähler|Nr|Bez|St|MaxWdh|St|MaxWdh|Ebene|Name|
|-|-|-|-|-|-|-|-|-|
|2400|00026|**UNT**|M|1|M|1|0|****Nachrichten-Endesegment****|


|Bez|Name|Standard<br/>St|Standard<br/>Format|BDEW<br/>St|BDEW<br/>Format|Anwendung / Bemerkung|
|-|-|-|-|-|-|-|
|UNT|||||||
|0074|Anzahl der Segmente in einer Nachricht|M|n..6|M|n..6|*Hier wird die Gesamtzahl der Segmente einer Nachricht angegeben.*|
|0062|Nachrichten-Referenznummer|M|an..14|M|an..14|*Die Referenznummer aus dem UNH-Segment muss hier wiederholt werden.*|



## **Bemerkung:**


Das UNT-Segment ist ein Muss-Segment in UN/EDIFACT. Es muss immer das letzte Segment in einer Nachricht sein.


## **Beispiel:**


`UNT+26+767097019'`

Bez = Objekt-Bezeichner
Nr = Laufende Segmentnummer im Guide
MaxWdh = Maximale Wiederholung der Segmente/Gruppen
Zähler = Nummer der Segmente/Gruppen im Standard
St = Status
EDIFACT: M=Muss/Mandatory, C=Conditional
Anwendung: R=Erforderlich/Required, O=Optional, D=Abhängig von/
Dependent, N=Nicht benutzt/Not used
Version: 2.0e          30.09.2025          Seite: 32 / 33

PRICAT MIG

![edi@energy. Datenformate Strom & Gas](lrar)

## **Änderungshistorie**

|Änd-ID|Ort|ÄnderungenBisher|ÄnderungenNeu|Grund der Anpassung|Status|
|-|-|-|-|-|-|
|26085|BGM Beginn der<br/>Nachricht|Bemerkung:<br/>\[...]<br/>Die Eindeutigkeit eines Preisblatts für den<br/>Messstellenbetrieb ist durch die EDI-<br/>Nachrichtennummer gegeben, d. h. den Inhalt<br/>von DE1004 des BGM-Segments.<br/>Die Eindeutigkeit eines Preisblatts für das<br/>Sperren / Entsperren, die Verzugskosten, die<br/>Netznutzung ohne gemeindespezifische<br/>Konzessionsabgaben, Netznutzung:<br/>Gemeindespezifische Konzessionsabgaben und<br/>die Blindarbeit ist durch die EDI-<br/>Nachrichtennummer gegeben, d. h. den Inhalt<br/>von DE1004 des BGM-Segments.|Bemerkung:<br/>\[...]<br/>Die Eindeutigkeit aller anderen Preisblätter als<br/>das zur Übermittlung der<br/>Ausgleichsenergiepreise ist durch die EDI-<br/>Nachrichtennummer (Inhalt von DE1004 des<br/>BGM-Segments) und der MP-ID des PRICAT-<br/>Versenders, d. h. dem Inhalt des DE3039 von<br/>SG2-NAD mit DE3035 = MS gegeben.|Nur unter Hinzunahme des<br/>Absenders ist eines dieser<br/>Preisblätter eindeutig<br/>identifizierbar.|Fehler (30.09.2025)|
|26911|SG17 PGI-SG36<br/>SG36 LIN-PIA-IMD-<br/>SG40<br/>SG40 Preisangabe<br/>RNG Angaben zum<br/>Wertebereich<br/>DE6411|Spalte " Anwendung / Bemerkung":<br/><br/>H87 Stück<br/>DAY Tag|Spalte " Anwendung / Bemerkung":<br/><br/>H87 Stück<br/>DAY Tag<br/>KWH Kilowattstunde|Der Code KWH wird benötigt,<br/>um die Preisstaffeln für<br/>Artikel-ID, für Leistungen zur<br/>Änderung der Technik an einer<br/>Lokation in Kilowattstunden<br/>angeben zu können.|Fehler (30.09.2025)|


Version:   2.0e                                                                                                 30.09.2025                                                                                           Seite:        33    /      33