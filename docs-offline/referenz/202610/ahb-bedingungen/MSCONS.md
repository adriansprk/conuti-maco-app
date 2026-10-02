# Bedingungen MSCONS
<span hidden data-pagefind-meta={"title:Bedingungen MSCONS — Anwendungshandbuch (FV 202610)"} />

EDIFACT-Nachrichtentyp **MSCONS** · Formatversion **202610** · 169 Bedingungen · 5 Pakete · 3 UB-Bedingungen · aus 25 Handbuchdatei(en)

## Bedingungen

<div className="maco-tabellenrahmen">

| Marke | Bedingung |
|---|---|
| **[1]** | Sofern per ORDERS angefordert |
| **[2]** | Wenn das Zeitintervall zwischen ersten SG10 DTM+163 und letzten SG10 DTM+164 mindestens einen Monat umfasst |
| **[11]** | Wenn SG9 PIA+5+7-0?:52.0.22/7-0?:54.0.16/7-0?:54.0.20/7-0?:54.0.22 |
| **[12]** | Wenn nicht SG9 PIA+5+7-0?:52.0.22/7-0?:54.0.16/7-0?:54.0.20/7-0?:54.0.22 |
| **[17]** | Wenn nicht SG9 PIA+5+1-b?:9.99.0 (b= Kanal: Wert gemäß Codeliste der OBIS-Kennzahlen und Medien) |
| **[18]** | Wenn SG9 PIA+5+1-b?:9.99.0 (b= Kanal: Wert gemäß Codeliste der OBIS-Kennzahlen und Medien) |
| **[22]** | Wenn Aufteilung vorhanden |
| **[23]** | Wenn UNH DE0070 mit 1 vorhanden |
| **[24]** | Bei Aufteilung, in der Nachricht mit der höchsten Übermittlungsnummer |
| **[27]** | Wenn SG9 PIA+5+1-1?:1.9.0 vorhanden |
| **[28]** | Wenn SG9 PIA+5+1-1?:1.9.0 nicht vorhanden |
| **[32]** | wenn MP-ID in SG2 NAD+MS in der Rolle NB |
| **[33]** | wenn MP-ID in SG2 NAD+MR in der Rolle LF |
| **[35]** | wenn MP-ID in SG2 NAD+MS in der Rolle MSB |
| **[36]** | wenn MP-ID in SG2 NAD+MR in der Rolle NB |
| **[38]** | wenn in SG6 LOC+172 DE3225 die ID der Messlokation angegeben ist |
| **[42]** | Wenn MP-ID in SG2 NAD+MR in der Rolle MSB |
| **[45]** | Wenn SG9 PIA+5+7-b:99.41.16 (b=Kanal: Wert gemäß Codeliste der OBIS-Kennzahlen und Medien) vorhanden |
| **[46]** | Wenn Wert in SG6 LOC+172 DE3225 genau 11 Stellen |
| **[48]** | Wenn SG9 PIA+5+7-0?:52.0.22 |
| **[49]** | Wenn SG9 PIA+5+7-b?:70.16.16/7-b?:70.16.20/7-b?:70.16.22 (b=Kanal: Wert gemäß Codeliste der OBIS-Kennzahlen und Medien) vorhanden |
| **[50]** | Wenn SG9 PIA+5+7-b?:70.18.16/7-b?:70.18.20/7-b?:70.18.22 (b=Kanal: Wert gemäß Codeliste der OBIS-Kennzahlen und Medien) vorhanden |
| **[51]** | Wenn SG9 PIA+5+7-0?:33.86.0 vorhanden ist, darf mittels Wiederholung SG9 LIN in derselben Nachricht das SG9 PIA+5+7-0?:52.0.22/7-0?:54.0.16/7-0?:54.0.20/7-0?:54.0.22 nicht mehr angegeben werden |
| **[62]** | Wenn Wert in SG6 LOC+172 DE3225 genau 33 Stellen |
| **[67]** | Wenn es sich um die Referenz auf eine ORDERS handelt |
| **[68]** | Wenn BGM+7 vorhanden |
| **[69]** | Wenn BGM+Z28 vorhanden |
| **[70]** | Wenn BGM+BK vorhanden |
| **[71]** | Wenn BGM+Z39 vorhanden |
| **[72]** | Wenn SG9 PIA+5+1-b?:1.6.0/1-b?:3.6.0/1-b?:4.6.0/1-66?:13.6.0/1-66?:14.6.0 (b=Kanal: Wert gemäß Codeliste der OBIS-Kennzahlen und Medien) vorhanden |
| **[73]** | Wenn SG9 PIA+5+1-b?:1.9.e/1-b?:3.9.0/1-b?:4.9.0/1-66?:13.9.0/1-66?:14.9.0 (b=Kanal: Wert gemäß Codeliste der OBIS-Kennzahlen und Medien, e=Tarif: Wert gemäß Codeliste der OBIS-Kennzahlen und Medien) vorhanden |
| **[77]** | Wenn MP-ID in SG2 NAD+MR der RB HKN-R |
| **[78]** | Wenn SG9 PIA+5+1-66?:13.6.0/1-66?:14.6.0/1-66?:13.9.0/1-66?:14.9.0 vorhanden |
| **[79]** | Wenn SG9 PIA+5+1-66?:13.6.0/1-66?:14.6.0/1-66?:13.9.0/1-66?:14.9.0 nicht vorhanden |
| **[80]** | Wenn MP-ID in SG2 NAD+MR in der Rolle ÜNB |
| **[83]** | Wenn in derselben SG9 LIN die Angabe STS+10+Z38 nicht vorhanden |
| **[84]** | Wenn in derselben SG9 LIN die Angabe STS+10+Z39 nicht vorhanden |
| **[85]** | Wenn in derselben SG9 LIN die Angabe STS+10+Z36 nicht vorhanden |
| **[86]** | Wenn in derselben SG9 LIN die Angabe STS+10+Z37 nicht vorhanden |
| **[87]** | Wenn der Wert in DTM+163 DE2380 derselben SG6 LOC+172 mit demselben Wert in SG9 PIA+5 DE7140 der früheste angegebene Zeitpunkt ist |
| **[88]** | Wenn der Wert in DTM+164 DE2380 derselben SG6 LOC+172 mit demselben Wert in SG9 PIA+5 DE7140 der späteste angegebene Zeitpunkt ist |
| **[90]** | Wenn BGM+Z41 vorhanden |
| **[91]** | Wenn BGM+Z42 vorhanden |
| **[92]** | Wenn SG10 QTY DE6063 mit Wert 67 vorhanden |
| **[93]** | Wenn SG10 QTY DE6063 mit Wert 220 vorhanden |
| **[94]** | Wenn SG10 QTY DE6063 mit Wert 201 vorhanden |
| **[95]** | Wenn SG10 QTY DE6063 mit Wert 20 vorhanden |
| **[96]** | Wenn SG10 QTY DE6063 mit Wert Z18 vorhanden |
| **[97]** | Wenn es sich um die Übermittlung eines Wertes aufgrund der Umstellung der Gasqualität handelt |
| **[98]** | Wenn SG9 PIA+5+SOL:Z08 vorhanden |
| **[99]** | Wenn SG9 PIA+5+WID:Z08 vorhanden |
| **[100]** | Wenn in derselben SG9 LIN das PIA+5+AUA:Z08 vorhanden |
| **[101]** | Wenn in derselben SG9 LIN das PIA+5+FPA:Z08 vorhanden |
| **[108]** | wenn SG9 PIA+5+7-b?:99.41.16/7-b?:99.42.16 (b=Kanal: Wert gemäß Codeliste der OBIS-Kennzahlen und Medien) vorhanden |
| **[111]** | Wenn SG10 DTM+9 DE2379 in demselben Segment mit Wert 303 vorhanden |
| **[113]** | wenn SG7 RFF+AGK (Konfigurations-ID) vorhanden |
| **[117]** | Nur MP-ID aus Sparte Strom |
| **[118]** | Nur MP-ID aus Sparte Gas |
| **[119]** | wenn in SG6 LOC+172 DE3225 die ID der Marktlokation angegeben ist |
| **[121]** | wenn BGM+Z43 (Redispatch Ausfallarbeitüberführungszeitreihe) vorhanden |
| **[125]** | wenn SG9 PIA+5+7-0?:52.0.22/7-b?:53.0.16/7-b?:55.0.16/7-b?:55.0.20/7-b?:55.0.22 (b=Kanal: Wert gemäß Codeliste der OBIS-Kennzahlen und Medien) vorhanden |
| **[126]** | wenn Plausibilisierungshinweise vorliegen |
| **[127]** | wenn ein Korrekturgrund anzugeben ist |
| **[128]** | Wenn es sich um eine Ablesung handelt, welche keine Ablesung aufgrund der Änderung an der Messtechnik oder deren Konfiguration ist (z.B. Kundenablesung). |
| **[129]** | Wenn es sich um eine Ablesung aufgrund der Änderung an der Messtechnik oder deren Konfiguration handelt (z.B. Gerätewechsel). |
| **[130]** | Wenn innerhalb desselben LIN-Segments neben diesem Segment (SG10 DTM+7 Nutzungszeitpunkt) noch das SG10 DTM+60 (Ausführungs- / Änderungszeitpunkt) oder das SG10 DTM+9 (Ablesedatum) vorhanden, darf der Wert der Differenz zwischen dem größeren und dem kleineren Zeitpunkt der DTM-Segmente ausschließlich &lt; 24 Stunden sein. Findet zwischen den beiden Zeitpunkten die Sommer/Winter-Zeitumschaltung statt, darf der Wert der Differenz ausschließlich &lt; 25 Stunden sein. Findet zwischen den beiden Zeitpunkten die Winter/Sommer-Zeitumschaltung statt, darf der Wert der Differenz ausschließlich &lt; 23 Stunden sein. |
| **[131]** | wenn RFF+AGK (Konfigurations-ID) nicht vorhanden |
| **[132]** | wenn LOC+172 (Identifikationsangabe) DE3225 nicht vorhanden |
| **[133]** | Wenn innerhalb desselben LIN-Segments neben diesem Segment (SG10 DTM+7 Nutzungszeitpunkt) noch das SG10 DTM+9 (Ablesedatum) mit dem Code 102 im DE2379 vorhanden ist, darf der Wert der Differenz zwischen dem Wert an der Stelle CCYYMMDD des größeren und dem kleineren Zeitpunkt der DTM-Segmente an der Stelle CCYYMMDD ausschließlich 0 oder 1 Tag sein. |
| **[134]** | Wenn SG10 DTM+9 DE2379 in demselben Segment mit Wert 102 vorhanden |
| **[135]** | Der Wert an der Stelle CCYYMMDD muss ≤ dem Wert an der Stelle CCYYMMDD im DE2380 des DTM+137 sein |
| **[138]** | Wenn es sich um eine Korrekturenergiemenge auf einen Wert aus einem iMS handelt |
| **[141]** | Wenn MP-ID in SG2 NAD+MR in der Rolle MGV |
| **[144]** | Wenn Wert in SG7 RFF+AGK DE1154 (Konfigurations-ID) vorhanden |
| **[145]** | Wenn in derselben S9 LIN das SG10 DTM+163 (Beginn Messperiode) nicht vorhanden ist. |
| **[146]** | Wenn es bei dem zu übermittelnden Wert um einen Wert zu einem Zeitpunkt handelt. |
| **[147]** | Wenn in derselben S9 LIN das SG10 DTM+7 (Nutzungszeitpunkt) nicht vorhanden ist. |
| **[148]** | Wenn es bei dem zu übermittelnden Wert um einen Wert in einem Zeitintervall handelt. |
| **[149]** | Wenn in derselben S9 LIN das SG10 DTM+163 (Beginn Messperiode) vorhanden ist. |
| **[150]** | Wenn BGM+Z69 (Redispatch tägliche Ausfallarbeitsüberführungszeitreihe) vorhanden. |
| **[151]** | Wenn BGM+Z27 (Bewegungsdaten im Kalenderjahr vor Lieferbeginn) vorhanden. |
| **[152]** | Wenn BGM+7 (Prozessdatenbericht) vorhanden. |
| **[153]** | Wenn SG9 PIA+5+7-0?:33.86.0 vorhanden |
| **[154]** | Wenn SG9 PIA+5+7-0?:33.47.0 vorhanden |
| **[155]** | Wenn Übertragungsdatei zu Testzwecken ausgetauscht wird. |
| **[490]** | wenn Wert in diesem DE, an der Stelle CCYYMMDDHHMM ein Zeitpunkt aus dem angegeben Zeitraum der Tabelle Kapitel 3.5 „Übersicht gesetzliche deutsche Sommerzeit (MESZ)“ der Spalten: „Sommerzeit (MESZ) von“ Darstellung in UTC und „Sommerzeit (MESZ) bis“ Darstellung in UTC ist. |
| **[491]** | wenn Wert in diesem DE, an der Stelle CCYYMMDDHHMM ein Zeitpunkt aus dem angegeben Zeitraum der Tabelle Kapitel 3.6 „Übersicht gesetzliche deutsche Zeit (MEZ)“ der Spalten: „Winterzeit (MEZ) von“ Darstellung in UTC und „Winterzeit (MEZ) bis“ Darstellung in UTC ist. |
| **[492]** | wenn MP-ID in NAD+MR aus Sparte Strom |
| **[493]** | wenn MP-ID in NAD+MR aus Sparte Gas |
| **[494]** | Das hier genannte Datum muss der Zeitpunkt sein, zu dem das Dokument erstellt wurde, oder ein Zeitpunkt, der davor liegt. |
| **[495]** | Der Zeitpunkt muss ≤ dem Wert im DE2380 des DTM+137 sein |
| **[501]** | Hinweis: Es sind nur die Werte erlaubt, die in der EDI@Energy Codeliste der OBIS-Kennzahlen und Medien mit dem entsprechenden Prüfidentifikator versehen sind. |
| **[502]** | Hinweis: Einmal für die Energiemenge von Beginn des Kalenderjahres bis zum Lieferbeginn und mindestens einmal und bis zu zweimal für die zwei höchsten Monatsleistungswerte (wegen KAV) von Beginn des Kalenderjahres bis zum Lieferbeginn. |
| **[506]** | Hinweis: Nur bei Einspeisemengen und bei Gas zur stündlichen Energiedatenübermittlung |
| **[509]** | Hinweis: Falls es sich um eine Korrekturenergiemenge handelt, ist hier die Referenz auf die MSCONS anzugeben, in der der Zählerstand vorab übermittelt wurde. |
| **[510]** | Hinweis: Verwendung der ID der Messlokation |
| **[511]** | Hinweis: Verwendung der ID des MaBiS-ZP |
| **[512]** | Hinweis: Verwendung der Bilanzkreisbezeichnung |
| **[513]** | Hinweis: Verwendung der Bezeichnung des Bilanzierungsgebietes |
| **[514]** | Hinweis: Verwendung der ID der Marktlokation |
| **[515]** | Hinweis: Verwendung der Profilbezeichnung |
| **[516]** | Hinweis: Verwendung der Bezeichnung der Profilschar |
| **[518]** | Hinweis: Verwendung der ID der Tranche |
| **[519]** | Hinweis: Nur wenn der gemessene Lastgang der Messlokation nicht dem Lastgang der Marktlokation 1:1 entspricht. |
| **[520]** | Hinweis: Wenn es sich um eine 1:1 Beziehung zwischen Messlokation und Marktlokation handelt und der gemessene Lastgang der Messlokation dem Lastgang der Marktlokation 1:1 entspricht, oder wenn der gemessene Lastgang nicht dem Lastgang der Marktlokation entspricht. |
| **[522]** | Hinweis: Nur für die Übermittlung der Korrekturenergiemengen im Zeitintervall zwischen zwei Messwerten. |
| **[523]** | Hinweis: Nur für die Übermittlung der Energiemenge im Zeitintervall zwischen zwei Messwerten vor der Netznutzungsabrechnung. |
| **[524]** | Hinweis: Nur, wenn es sich um die Übermittlung von Abrechnungsbrennwert und Z-Zahl für den vom Lieferanten über eine Geschäftsdatenanfrage angeforderten Zeitraum handelt. |
| **[525]** | Hinweis: Nur für die Übermittlung der Energiemenge im Zeitintervall für eine Marktlokation ohne Messlokation (Pauschalanlage) wenn eines der Ereignisse aus Kapitel 4.2 eingetreten ist. |
| **[526]** | Hinweis: Wert aus BGM+Z24 DE1004 der ORDERS mit der die Allokationsliste bestellt wurde. |
| **[528]** | Hinweis: Wert aus BGM+Z28 DE1004 der ORDERS mit der die Anforderung von Messwerten erfolgt ist. |
| **[529]** | Hinweis: Wert aus BGM+7 DE1004 der ORDERS mit der die Anforderung von Messwerten erfolgt ist. |
| **[530]** | Hinweis: Wert aus SG4 IDE+24 DE7402 der UTILMD mit dem der Sender der MSCONS die vorherigen Stammdaten mittels UTILMD übermittelt hat. |
| **[531]** | Hinweis: Wert aus BGM+7 DE1004 der MSCONS mit der der Zählerstand übermittelt wurde. |
| **[532]** | Hinweis: Wert aus BGM+7/Z27/Z28/270/Z41/Z42/Z85 DE1004 der MSCONS Nachricht, die storniert wird |
| **[535]** | Hinweis: Verwendung der ID des Netzkoppelpunktes Strom/Gas |
| **[538]** | Hinweis: Die Referenz auf die ORDERS ist nur dann anzugeben, wenn diese Werte vom Empfänger auch ursprünglich mittels ORDERS angefragt wurden. |
| **[541]** | Hinweis: Ein Korrekturgrund ist anzugeben, wenn: 1. ein bereits an den MP übermittelter vorläufiger Wert nach Stornierung durch einen Ersatzwert ersetzt wird, oder 2. ein bereits an den MP übermittelter Ersatzwert nach Stornierung durch einen Ersatzwert ersetzt wird, oder 3. ein bereits an den MP übermittelter wahrer Wert nach Stornierung durch einen Ersatzwert ersetzt wird, oder 4. ein bereits an den MP übermittelter wahrer Wert nach Stornierung durch einen wahren Wert ersetzt wird. |
| **[544]** | Hinweis: Bei einer Mengenaufteilung (z. B. Aufgrund einer Abgrenzung) für SG6 LOC+172 muss für den frühesten angegebenen Zeitpunkt zum Beginn des Zeitintervalls (über alle Wiederholungen der LIN-Segmente derselben SG6 LOC+172 hinweg) zu jeder OBIS-Kennziffer ein Zählerstand vorhanden und kommuniziert sein. |
| **[545]** | Hinweis: Bei einer Mengenaufteilung (z. B. Aufgrund einer Abgrenzung) für SG6 LOC+172 muss für den spätesten angegebenen Zeitpunkt zum Ende des Zeitintervalls (über alle Wiederholungen der LIN-Segmente derselben SG6 LOC+172 hinweg) zu jeder OBIS-Kennziffer ein Zählerstand vorhanden und kommuniziert sein. |
| **[546]** | Hinweis: Eine Referenz auf die Stammdatenänderung des Gerätewechsels ist immer anzugeben, wenn diese dem Sender vorliegt. |
| **[547]** | Hinweis: Der Code 270 ist nur zu nutzen, wenn ein Lieferschein, der vor dem 1.4.2021 erstellt wurde, storniert wird. |
| **[551]** | Hinweis: Ein Korrekturgrund ist anzugeben, wenn: 1. ein bereits an den MP übermittelter vorläufiger Wert durch einen Ersatzwert ersetzt wird, oder 2. ein bereits an den MP übermittelter Ersatzwert durch einen Ersatzwert ersetzt wird, oder 3. ein bereits an den MP übermittelter wahrer Wert durch einen Ersatzwert ersetzt wird, oder 4. ein bereits an den MP übermittelter wahrer Wert durch einen wahren Wert ersetzt wird. |
| **[553]** | Hinweis: Wert aus BGM+Z34 DE1004 der ORDERS mit der die Reklamation von Werten erfolgt ist |
| **[554]** | Hinweis: Verwendung der ID der Technischen Ressource |
| **[556]** | Hinweis: Wert aus BGM+Z45 DE1004 der ORDERS mit der die Anforderung der Ausfallarbeit durch den anfNB erfolgt ist. |
| **[557]** | Hinweis: Die Referenz auf die ursprüngliche MSCONS ist anzugeben, wenn es sich um die Übermittlung eines Gegenvorschlags durch den BTR handelt. |
| **[558]** | Hinweis: Wert aus BGM+Z45 DE1004 der MSCONS auf die sich die Übermittlung des Gegenvorschlags durch den BTR bezieht. |
| **[559]** | Hinweis: Ein Korrekturgrund ist anzugeben, wenn: 1. ein bereits an den MP übermittelter vorläufiger Wert nach Stornierung durch einen Ersatzwert ersetzt wird, oder 2. ein bereits an den MP übermittelter Ersatzwert nach Stornierung durch einen Ersatzwert ersetzt wird, oder 3. ein bereits an den MP übermittelter wahrer Wert nach Stornierung durch einen Ersatzwert ersetzt wird, oder 4. ein bereits an den MP übermittelter wahrer Wert nach Stornierung durch einen wahren Wert ersetzt wird. |
| **[560]** | Hinweis: Ein Korrekturgrund ist anzugeben, wenn: 1. ein bereits an den MP übermittelter vorläufiger Wert durch einen Ersatzwert ersetzt wird, oder 2. ein bereits an den MP übermittelter Ersatzwert durch einen Ersatzwert ersetzt wird, oder 3. ein bereits an den MP übermittelter wahrer Wert durch einen Ersatzwert ersetzt wird, oder 4. ein bereits an den MP übermittelter wahrer Wert durch einen wahren Wert ersetzt wird. |
| **[566]** | Hinweis: Es sind nur die Werte erlaubt, die im vorherigen Stammdatenaustausch zu diesem Meldepunkt vom MSB zum Zeitpunkt übermittelt wurden. |
| **[567]** | Hinweis: Es ist die Konfigurations-ID anzugeben, die im vorherigen Stammdatenaustausch kommuniziert wurde. |
| **[568]** | Hinweis: Verwendung ist nur zulässig, wenn es sich um 1:n Beziehung zwischen Markt- und Messlokation handelt und auf Ebene der Messlokation unterschiedliche Ersatzwertbildungsverfahren verwendet und kommuniziert wurden. |
| **[569]** | Hinweis: Bei mehreren Zählerständen einer Messlokation (z. B. HT/NT) ist diese Zeitangabe zu nutzen und eine Wiederholung das SG9 LIN durchzuführen. |
| **[570]** | Hinweis: Verwendung ist nur zulässig, wenn es sich um 1:n Beziehung zwischen Markt- und Messlokation handelt und auf Ebene der Messlokation unterschiedliche Gründe für die Ersatzwertbildung vorliegen und kommuniziert wurden. |
| **[571]** | Hinweis: Verwendung ist nur zulässig, wenn es sich um 1:n Beziehung handelt und auf Ebene der Netzkopplungspunkte unterschiedliche Gründe für die Ersatzwertbildung vorliegen und kommuniziert wurden. |
| **[572]** | Hinweis: Verwendung ist nur zulässig, wenn es sich um 1:n Beziehung handelt und auf Ebene der Netzkopplungspunkte unterschiedliche Ersatzwertbildungsverfahren vorliegen und kommuniziert wurden. |
| **[573]** | Hinweis: Eine Energiemenge in der Sparte Gas ist gemäß DVGW G685 Arbeitsblatt 4 Kapitel 5.3 auf ganze Kilowattstunden zu runden. |
| **[574]** | Hinweis: Wert aus BGM DE1004 der ORDERS mit der die Bestellung der Werte nach Typ 2 erfolg ist |
| **[575]** | Hinweis: Verwendung der ID der Netzlokation |
| **[577]** | Hinweis: Dieser Code ist auch zu verwenden, wenn aufgrund der Beendigung einer Messlokation (Stilllegung) die Beendigung der Marktlokation (Stilllegung) zu unterschiedlichen Zeitpunkten erfolgt, das heißt die Beendigung der Messlokation vor der Beendigung der Marktlokation erfolgt. Die Energiemenge ist bis zum Endezeitpunkt der Marklokation zu übermitteln, wenngleich der letzte Zählerstand der Messlokation zu einem früheren Zeitpunkt liegt. |
| **[578]** | Hinweis: Wenn es sich um die Übermittlung des Leistungswertes für die Netzentgelte mit Jahresleistungspreissystem handelt. |
| **[579]** | Hinweis: Wenn es sich um die Übermittlung des Leistungswertes für die Netzentgelte mit Monatsleistungspreissystem handelt. |
| **[580]** | Hinweis: Wenn es sich um die Übermittlung des Leistungswertes für die Netzentgelte mit Tagesleistungspreissystem handelt. |
| **[581]** | Hinweis: Wenn es sich um die Übermittlung des Monatsmaximum gemäß WiM handelt. |
| **[902]** | Format: Möglicher Wert: ≥ 0 |
| **[904]** | Format: genau 16 Stellen |
| **[905]** | Format: max. 3 Stellen |
| **[906]** | Format: max. 3 Nachkommastellen |
| **[907]** | Format: max. 4 Nachkommastellen |
| **[908]** | Format: Mögliche Werte: 1 bis n |
| **[909]** | Format: Mögliche Werte: 0 bis n |
| **[910]** | Format: Möglicher Wert: &lt; 0 oder ≥ 0 |
| **[917]** | Format: max. 4 Vorkommastellen |
| **[918]** | Format: Zeichen aus dem über UNOC definierten Zeichensatz, wobei von den Buchstaben nur Großbuchstaben erlaubt sind. |
| **[922]** | Format: TR-ID |
| **[925]** | Format: max. 5 Nachkommastellen |
| **[931]** | Format: ZZZ = +00 |
| **[932]** | Format: HHMM = 2200 |
| **[933]** | Format: HHMM = 2300 |
| **[934]** | Format: HHMM = 0400 |
| **[935]** | Format: HHMM = 0500 |
| **[937]** | Format: keine Nachkommastelle |
| **[950]** | Format: Marktlokations-ID |
| **[951]** | Format: Zählpunktbezeichnung |
| **[960]** | Format: Netzlokations-ID |
| **[2001]** | Segmentgruppe ist nur einmal je UNH anzugeben |
| **[2002]** | Segmentgruppe ist mindestens zweimal und maximal dreimal je SG5 NAD+DP anzugeben |
| **[2003]** | Segmentgruppe ist genau zwei Mal je SG9 LIN anzugeben |

</div>

## UB-Bedingungen

UB-Bedingungen fassen mehrere Marken zu einem Ausdruck zusammen. Sie stehen in den Handbuchzeilen wie eine Bedingung, lösen sich aber in die Marken darin auf.

<div className="maco-tabellenrahmen">

| Marke | Ausdruck |
|---|---|
| **[UB1]** | ([931] ∧ [932] [490]) ⊻ ([931] ∧ [933] [491]) |
| **[UB2]** | ([931] ∧ [934] [490]) ⊻ ([931] ∧ [935] [491]) |
| **[UB3]** | ([931] ∧ [932] [492] ∧ [490]) ⊻ ([931] ∧ [933] [492] ∧ [491]) ⊻ ([931] ∧ [934] [493] ∧ [490]) ⊻ ([931] ∧ [935] [493] ∧ [491]) |

</div>

## Bedingungspakete

Bedingungspakete bündeln Voraussetzungen.

<div className="maco-tabellenrahmen">

| Paket | Voraussetzungen | Bedingungen |
|---|---|---|
| **[4P]** | [92] | [92]  W enn SG10 QTY DE6063 mit Wert 67 vorhanden |
| **[5P]** | [93] | [93]  W enn SG10 QTY DE6063 mit Wert 220 vorhanden |
| **[6P]** | [94] | [94]  Wenn SG10 QTY DE6063   mit Wert 201 vorhanden |
| **[7P]** | [95] | [95]  Wenn SG10 QTY DE6063   mit Wert  20  vorhanden |
| **[8P]** | [96] | [96]  Wenn SG10 QTY DE6063   mit Wert Z18 vorhanden |

</div>

<Hinweisbereich>

Diese Seite führt den Klartext jeder Bedingung, auf die das Anwendungshandbuch des Nachrichtentyps **MSCONS** in dieser Formatversion verweist. Eine Zeile des Handbuchs schreibt `Muss [704]`; was [704] verlangt, steht hier.

Die Liste gilt **für den Nachrichtentyp**, nicht für einen einzelnen Prüfidentifikator. Das ist keine Vereinfachung, sondern die Form der Quelle: die Bedingungsliste liegt in jeder Handbuchdatei des Formats identisch vor.

:::caution{title="Warum hier keine Zuordnung zu einzelnen Prüfidentifikatoren steht"}

Das Zwischenformat, aus dem diese Dokumentation die Handbuchzeilen liest, ordnet Bedingungen einer **Spalte** zu — und diese Zuordnung ist gegen das Original verschoben. Gemessen am 05.09.2026 an UTILMD Strom: das Handbuch führt `STS DE9013` als `X [360]` (nur Zustimmungscodes) beim Prüfidentifikator **55017** und `X [359]` (nur Ablehnungscodes) bei **55018**; das Zwischenformat setzt `[360]` auf 55016 und `[359]` auf 55017 **und** 55018. Dasselbe bei `FTX Muss [83]`: im Handbuch bei 55018, im Zwischenformat bei 55017.

Unabhängig bestätigt durch die Änderungslisten der Quelle: die Änderungs-IDs 25242, 25821, 25822, 25445 und 25243 verorten [83], [351] und [352] ausdrücklich beim „Anwendungsfall 55018 Ablehnung Kündigung“. Kein Eintrag ordnet sie 55016 oder 55017 zu.

Deshalb steht hier der **Text** jeder Bedingung und nirgends die Behauptung, welche Bedingung für welchen Prüfidentifikator gilt. Wer das braucht, schlägt im Original-Anwendungshandbuch nach.

:::

:::note{title="6 Bedingungen stehen nicht in jeder Handbuchdatei"}

Die Bedingungsliste ist formatweit gemeint, ist es aber nicht überall: die folgenden Marken kommen in weniger als allen 25 Dateien dieses Formats vor. Sie stehen trotzdem hier — eine Bedingung wegzulassen, weil eine Datei sie nicht führt, hieße einen Verweis wieder ins Leere zeigen zu lassen.

[493], [934], [935], [UB1], [UB2], [UB3]

:::

Gemessen am 05.09.2026 verweist **keine** `ahb_expression` dieser Quelle auf eine Paketmarke — die Bedingungspakete stehen auf dieser Seite, weil die Quelle sie führt, nicht weil eine Handbuchzeile auf sie zeigt.

</Hinweisbereich>
