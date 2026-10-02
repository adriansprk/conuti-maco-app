# Bedingungen QUOTES
<span hidden data-pagefind-meta={"title:Bedingungen QUOTES — Anwendungshandbuch (FV 202610)"} />

EDIFACT-Nachrichtentyp **QUOTES** · Formatversion **202610** · 129 Bedingungen · 5 Pakete · 2 UB-Bedingungen · aus 5 Handbuchdatei(en)

## Bedingungen

<div className="maco-tabellenrahmen">

| Marke | Bedingung |
|---|---|
| **[1]** | Wenn Position nicht angeboten werden kann, weil rechtliche Regelungen oder Rechte Dritter dem entgegenstehen |
| **[2]** | Wenn in derselben SG27 LIN IMD DE7081 (Produkt-/Leistungsbeschreibung) mit Code Z09 (Kann nicht angeboten werden) nicht vorhanden. |
| **[3]** | Wenn CCI+++Z64 vorhanden ist |
| **[4]** | Wenn am Gerät vorhanden und abweichend von Gerätenummer |
| **[5]** | Wenn in derselben SG27 LIN die Artikelnummer 9990001000649 vorhanden ist |
| **[8]** | Wenn SG28 CCI+++E13 CAV+EHZ vorhanden |
| **[9]** | Wenn in derselben SG27 LIN die Artikelnummer 9990001000657 vorhanden ist |
| **[10]** | Wenn SG28 CAV+MIW/MPW/MBW vorhanden |
| **[11]** | Wenn in derselben SG27 LIN die Artikelnummer 9990001000665 vorhanden ist |
| **[12]** | Wenn in derselben SG27 LIN die Artikelnummer 9990001000673 vorhanden ist |
| **[13]** | Wenn am Gerät vorhanden |
| **[15]** | Wenn in derselben SG27 LIN die Artikelnummer 9990001000772 vorhanden ist |
| **[16]** | Wenn in derselben SG27 LIN die Artikelnummer 9990001000780 vorhanden ist |
| **[17]** | Wenn das Angebot per REQOTE angefragt wurde |
| **[18]** | Wenn Angebot mehrere Marktlokationen abdeckt, an welchen der identische Anschlussnutzer vorhanden ist und deren messtechnische Einordnung iMS ist (Marktlokation aus SG11 LOC+172 und alle Marktlokationen, die in einem SG29 RFF+Z18 aufgeführt sind). |
| **[20]** | Wenn IMD++Z33 vorhanden |
| **[21]** | Wenn IMD++Z34 vorhanden |
| **[22]** | Wenn CCI+++Z75 vorhanden ist |
| **[25]** | Wenn SG28 CCI+++E13 CAV+MME vorhanden |
| **[26]** | Wenn DTM+203 nicht vorhanden |
| **[27]** | Wenn DTM+469 nicht vorhanden |
| **[28]** | Wenn RFF+AAV vorhanden |
| **[29]** | Wenn DTM+469 in Anfrage (REQOTE) vorhanden war |
| **[30]** | Wenn SG27 IMD+Z09 vorhanden |
| **[31]** | Es sind nur die Artikelnummern erlaubt, die in der Codeliste der Artikelnummern des BDEW mit dem entsprechenden Prüfidentifikator versehen sind. |
| **[39]** | MP-ID nur aus Sparte Strom |
| **[44]** | Wenn MSBA nicht Eigentümer des Gerätes/der Geräte ist |
| **[49]** | Wenn SG27 LIN++Z64 (Erforderliches Produkt Schaltzeitdefinitionen) vorhanden |
| **[50]** | Wenn SG27 LIN++Z65 (Erforderliches Produkt Leistungskurvendefinitionen) vorhanden |
| **[51]** | Wenn SG27 LIN++Z66 (Erforderliches Produkt Ad-hoc-Steuerkanal) vorhanden |
| **[52]** | Wenn SG27 LIN++Z67 (Erforderliches Messprodukt für Werte nach Typ 2 aus Backend) vorhanden |
| **[53]** | Wenn SG27 LIN++Z68 (Erforderliches Produkt Konfigurationserlaubnis für Werte nach Typ2 aus SMGW) vorhanden |
| **[54]** | Wenn in der Anfrage zum Angebot einer Konfiguration vorhanden |
| **[55]** | Wenn in LOC+172 DE3225 (Meldepunkt) die ID einer Marktlokation angegeben ist. |
| **[56]** | Wenn in LOC+172 DE3225 (Meldepunkt) die ID einer Messlokation angegeben ist. |
| **[57]** | Wenn in LOC+172 DE3225 (Meldepunkt) die ID einer Netzlokation angegeben ist. |
| **[58]** | Wenn in LOC+172 DE3225 (Meldepunkt) die ID einer Steuerbaren Ressource angegeben ist. |
| **[59]** | Es sind nur die Konfigurations-Produkte erlaubt, die in der Codeliste der Konfigurationen im Kapitel 4.1 „Konfigurationsprodukte Schaltzeitdefinition“ enthalten sind. |
| **[60]** | Es sind nur die Konfigurations-Produkte erlaubt, die in der Codeliste der Konfigurationen im Kapitel 4.2 „Konfigurationsprodukte Leistungskurvendefinition“ enthalten sind. |
| **[61]** | Es sind nur die Konfigurations-Produkte erlaubt, die in der Codeliste der Konfigurationen im Kapitel 4.3 „Konfigurationsprodukte Ad-hoc-Steuerkanal“ enthalten sind. |
| **[62]** | Es sind nur die Messprodukte erlaubt, die in der Codeliste der Konfigurationen im Kapitel 4.5 „Messprodukte für Werte nach Typ 2 aus Backend für LF und NB“ enthalten sind. |
| **[63]** | Es sind nur die Messprodukte erlaubt, die in der Codeliste der Konfigurationen im Kapitel 4.4 „Messprodukte mit Konfigurationserlaubnis für Werte nach Typ 2 aus SMGW“ enthalten sind. |
| **[65]** | Wenn DTM+203 (Ausführungsdatum) im DE2380 &lt; 202312312300?+00 |
| **[66]** | Wenn DTM+469 (Beginn zum (nächstmöglichen Termin)) im DE2380 &lt; 202312312300?+00 |
| **[67]** | Wenn DTM+203 (Ausführungsdatum) im DE2380 ≥ 202312312300?+00 |
| **[68]** | Wenn DTM+469 (Beginn zum (nächstmöglichen Termin)) im DE2380 ≥ 202312312300?+00 |
| **[69]** | Es sind nur Werte aus der EDI@Energy Codeliste der Artikelnummern und Artikel-ID erlaubt, die im Kapitel 3.5 "Abrechnung Messstellenbetrieb für die Sparte Strom" genannt sind. |
| **[70]** | Es sind nur die Messprodukt-Position-Codes erlaubt, die in der Codeliste der Konfigurationen im Kapitel 4.7 „Art der Werte für Messprodukte nach Typ 2“ enthalten sind. |
| **[71]** | Wenn innerhalb derselben SG27 LIN im PIA+5 DE7140 (Erforderliches Produkt Konfigurationserlaubnis für Werte nach Typ 2 aus SMGW) ein Produkt angegeben ist, das in der Codeliste der Konfigurationen im Kapitel 4.4 „Messprodukte mit Konfigurationserlaubnis für Werte nach Typ 2 aus SMGW“ in der Spalte "Auslöser" mit dem Wert "Bei Schwellwertunter- / -überschreitung" gekennzeichnet ist. |
| **[72]** | wenn im DE3155 in demselben COM der Code EM vorhanden ist |
| **[73]** | wenn im DE3155 in demselben COM der Code TE / FX / AJ / AL vorhanden ist |
| **[74]** | Es sind nur die Messprodukte erlaubt, die in der Codeliste der Konfigurationen im Kapitel 4.6.1 "Werte nach Typ 2 aus Backend" enthalten sind. |
| **[75]** | Es sind nur die Messprodukte erlaubt, die in der Codeliste der Konfigurationen im Kapitel 4.6.2 "Werte nach Typ 2 aus SMGW" enthalten sind. |
| **[77]** | Wenn in der Anfrage nach Werten ein Messprodukt enthalten war, das in der Codeliste der Konfigurationen im Kapitel 4.6.1 "Werte nach Typ 2 aus Backend" enthalten ist. |
| **[78]** | Wenn in der Anfrage nach Werten ein Messprodukt enthalten war, das in der Codeliste der Konfigurationen im Kapitel 4.6.2 "Werte nach Typ 2 aus SMWG" enthalten ist. |
| **[79]** | Wenn IMD DE7081 (Produkt-/Leistungsbeschreibung) mit Wert Z07 (Kauf) vorhanden. |
| **[80]** | Wenn IMD DE7081 (Produkt-/Leistungsbeschreibung) mit Wert Z08 (Nutzungsüberlassung) vorhanden. |
| **[81]** | Wenn IMD DE7081 (Produkt-/Leistungsbeschreibung) mit Wert Z33 (Angebot auf Basis Preisblatt) vorhanden. |
| **[82]** | Wenn IMD DE7081 (Produkt-/Leistungsbeschreibung) mit Wert Z34 (Individuelles Angebot) vorhanden. |
| **[83]** | Wenn in derselben SG27 LIN ein PIA+Z02 (Artikel-ID) mit einer Artikel-ID im DE7140 bei der die letzten beiden Stellen mit dem Wert "01" (Kosten für das Einrichten des Messprodukts) vorhanden ist. |
| **[84]** | Wenn in derselben SG27 LIN ein PIA+Z02 (Artikel-ID) mit einer Artikel-ID im DE7140 bei der die letzten beiden Stellen mit dem Wert "02" (Kosten für den Betrieb des Messprodukts) vorhanden ist. |
| **[85]** | Wenn in derselben SG27 LIN ein PIA+Z02 (Artikel-ID) mit einer Artikel-ID im DE7140 bei der die letzten beiden Stellen mit dem Wert "03" (Kosten für die anfallenden Transaktionen des Messprodukts) vorhanden ist. |
| **[86]** | Wenn in derselben SG31 PRI (Preisangabe zur Position) das DE5387 mit dem Wert Z01 (Einrichtungspreis) vorhanden ist. |
| **[87]** | Wenn in derselben SG31 PRI (Preisangabe zur Position) das DE5387 mit dem Wert Z02 (Transaktionspreis) vorhanden ist. |
| **[88]** | Wenn in derselben SG31 PRI (Preisangabe zur Position) das DE5387 mit dem Wert Z03 (Betriebspreis) vorhanden ist. |
| **[90]** | Es sind nur die Produkt-Codes erlaubt, die in der Codeliste der Konfigurationen im Kapitel 7 "Produkte zur Bestellung einer Änderung an einer Lokation" die in der Spalte "Ebene" mit dem Wert "Messlokation" vorhanden sind. |
| **[91]** | Es sind nur die Produkt-Codes erlaubt, die in der Codeliste der Konfigurationen im Kapitel 7 "Produkte zur Bestellung einer Änderung an einer Lokation" die in der Spalte "Ebene" mit dem Wert "Netzlokation" vorhanden sind. |
| **[92]** | Es sind nur die Produkt-Codes erlaubt, die in der Codeliste der Konfigurationen im Kapitel 7 "Produkte zur Bestellung einer Änderung an einer Lokation" die in der Spalte "Ebene" mit dem Wert "Steuerbare Ressource" vorhanden sind. |
| **[93]** | Wenn RNG+Z03 (verbindliche Mengenangabe) in dieser SG31 nicht vorhanden |
| **[94]** | Wenn RNG+Z04 (unverbindliche Mengenangabe) in dieser SG31 nicht vorhanden |
| **[490]** | wenn Wert in diesem DE, an der Stelle CCYYMMDDHHMM ein Zeitpunkt aus dem angegeben Zeitraum der Tabelle Kapitel 3.5 „Übersicht gesetzliche deutsche Sommerzeit (MESZ)“ der Spalten: „Sommerzeit (MESZ) von“ Darstellung in UTC und „Sommerzeit (MESZ) bis“ Darstellung in UTC ist. |
| **[491]** | wenn Wert in diesem DE, an der Stelle CCYYMMDDHHMM ein Zeitpunkt aus dem angegeben Zeitraum der Tabelle Kapitel 3.6 „Übersicht gesetzliche deutsche Zeit (MEZ)“ der Spalten: „Winterzeit (MEZ) von“ Darstellung in UTC und „Winterzeit (MEZ) bis“ Darstellung in UTC ist. |
| **[492]** | wenn MP-ID in NAD+MR aus Sparte Strom |
| **[493]** | wenn MP-ID in NAD+MR aus Sparte Gas |
| **[494]** | Das hier genannte Datum muss der Zeitpunkt sein, zu dem das Dokument erstellt wurde, oder ein Zeitpunkt, der davor liegt. |
| **[500]** | Hinweis: Angabe eines technischen Ansprechpartners für die Geräteübernahme |
| **[501]** | Hinweis: Verwendung der ID der Marktlokation |
| **[502]** | Hinweis: Verwendung der ID der Messlokation |
| **[503]** | Hinweis: Es ist die MP-ID des Eigentümers (MSB) zur bilateralen Klärung anzugeben, wenn z. B. der MSBA das Gerät / die Geräte selbst gepachtet hat. |
| **[504]** | Hinweis: Wert aus BGM+311 DE1004 der REQOTE mit der die Angebotsanfrage erfolgt ist. |
| **[505]** | Hinweis: Wert aus BGM+Z29 DE1004 der REQOTE, mit der die Anfrage Rechnungsabwicklung erfolgt ist. |
| **[506]** | Hinweis: Wenn zu einer Position (z. B. Messwandlersatz) mehrere Gerätenummern existieren, sind die Gerätenummern in derselben Position (LIN-Segment) mittels Wiederholung der SG32 RFF+Z09 anzugeben |
| **[507]** | Hinweis: Verwendung der ID der Tranche |
| **[511]** | Hinweis: Wert aus BGM+Z74 (Bestellung eines Angebots einer Konfiguration) DE1004 der REQOTE mit der die Anfrage einer Konfiguration erfolgt ist. |
| **[512]** | Hinweis: Verwendung der ID der Netzlokation |
| **[513]** | Hinweis: Verwendung der ID der Steuerbaren Ressource |
| **[514]** | Hinweis: Angabe gemäß Preisblatt des MSB. Bis zu einmal für die Parametrierung, bis zu einmal für den Betrieb und bis zu einmal für die Transaktion, sofern im Preisblatt des MSB vorhanden. |
| **[516]** | Hinweis: Es darf nur eine Information im DE3148 übermittelt werden |
| **[517]** | Hinweis: Wert aus BGM+Z93 (Bestellung eines Angebots Änderung der Technik der Lokation) DE1004 der REQOTE mit der die Anfrage Angebot Änderung Technik erfolgt ist. |
| **[518]** | Hinweis: Angabe gemäß Preisblatt B des MSB. |
| **[519]** | Hinweis: Wert aus BGM DE1004 der PRICAT mit der das Preisblatt B des MSB, auf dem dieses Angebot basiert, übermittelt wurde. |
| **[520]** | Hinweis: Angabe des Beginnzeitpunkts des voraussichtlich frühesten Umsetzungstermins, der zum Zeitpunkt der Angebotserstellung ermittelt werden kann. |
| **[521]** | Hinweis: Angabe des Endezeitpunkts des voraussichtlich frühesten Umsetzungstermins, der zum Zeitpunkt der Angebotserstellung ermittelt werden kann.. |
| **[903]** | Format: Möglicher Wert: 1 |
| **[906]** | Format: max. 3 Nachkommastellen |
| **[908]** | Format: Mögliche Werte: 1 bis n |
| **[911]** | Format: Mögliche Werte: 1 bis n, je Nachricht oder Segmentgruppe bei 1 beginnend und fortlaufend aufsteigend |
| **[912]** | Format: max. 6 Nachkommastellen |
| **[914]** | Format: Möglicher Wert: &gt; 0 |
| **[931]** | Format: ZZZ = +00 |
| **[932]** | Format: HHMM = 2200 |
| **[933]** | Format: HHMM = 2300 |
| **[934]** | Format: HHMM = 0400 |
| **[935]** | Format: HHMM = 0500 |
| **[939]** | Format: Die Zeichenkette muss die Zeichen @ und . enthalten |
| **[940]** | Format: Die Zeichenkette muss mit dem Zeichen + beginnen und danach dürfen nur noch Ziffern folgen |
| **[942]** | Format: n1-n2-n1-n3 |
| **[950]** | Format: Marktlokations-ID |
| **[951]** | Format: Zählpunktbezeichnung |
| **[959]** | Format: n13-n2 |
| **[960]** | Format: Netzlokations-ID |
| **[961]** | Format: SR-ID |
| **[962]** | Format: max. 6 Vorkommastellen |
| **[2042]** | Innerhalb dieser LIN-Position muss das PIA+Z02 (Artikel-ID) mindestens ein Mal angegeben werden und kann bis zu drei Mal angegeben werden. |
| **[2060]** | Pro Nachricht ist die SG27 LIN+Z64 (Erforderliches Produkt Schaltzeitdefinitionen) maximal einmal anzugeben. |
| **[2061]** | Pro Nachricht ist die SG27 LIN++Z65 (Erforderliches Produkt Leistungskurvendefinitionen) maximal einmal anzugeben. |
| **[2062]** | Pro Nachricht ist die SG27 LIN++Z66 (Erforderliches Produkt Ad-hoc-Steuerkanal) maximal einmal anzugeben. |
| **[2063]** | Pro Nachricht ist die SG27 LIN++Z67 (Erforderliches Messprodukt für Werte nach Typ 2 aus Backend) maximal einmal anzugeben. |
| **[2064]** | Pro Nachricht ist die SG27 LIN++Z68 (Erforderliches Produkt Konfigurationserlaubnis für Werte nach Typ 2 aus SMGW) maximal einmal anzugeben. |
| **[2066]** | Diese SG28 ist so oft zu wiederholen, wie zu den unterschiedlichen Messprodukt-Position-Codes zu dem innerhalb derselben SG27 LIN im PIA+5 DE7140 (Erforderliches Produkt Konfigurationserlaubnis für Werte nach Typ 2 aus SMGW) angegebenen Produkt ein Produkt angegeben ist, das in der Codeliste der Konfigurationen im Kapitel 4.4 „Messprodukte mit Konfigurationserlaubnis für Werte nach Typ 2 aus SMGW“ in der Spalte "Auslöser" mit dem Wert "Bei Schwellwertunter- / -überschreitung" gekennzeichnet ist. |
| **[2068]** | Pro SG27 LIN ist die SG31 PRI genau einmal anzugeben. |
| **[2069]** | Pro SG27 LIN ist die SG31 PRI genau einmal anzugeben. Dabei muss in der SG31 PRI im DE5284 eine Mengenangabe mit dem Code H87 (Stück) im DE6411 angegeben sein. |
| **[2070]** | Pro SG27 LIN ist die SG31 PRI zweimal anzugeben. Dabei muss genau eine SG31 PRI mit Preis- und Mengenangabe und dem Code H87 (Stück) im DE6411 und genau eine SG31 PRI mit Preis- und Mengenangabe und dem Code DAY (Tag) im DE6411 vorhanden sein. |
| **[2071]** | Diese SG31 PRI (Preisangabe zur Position) ist bis zu dreimal anzugeben. Es ist so oft anzugeben, wie innerhalb derselben SG27 LIN (Erforderliches Messprodukt für Werte nach Typ2 aus Backend) das PIA+Z02 (Artikel-ID) vorhanden ist. |
| **[2072]** | Diese SG31 PRI (Preisangabe zur Position) ist bis zu dreimal anzugeben. Es ist so oft anzugeben, wie innerhalb derselben SG27 LIN (Erforderliches Produkt Konfigurationserlaubnis für Werte nach Typ 2 aus SMGW) das PIA+Z02 (Artikel-ID) vorhanden ist. |
| **[2073]** | Das PIA (OBIS-Kennzahl für Werte nach Typ 2 Backend) ist mindestens einmal anzugeben. Es kann in Abhängigkeit zu den anderen PIA Segmenten innerhalb derselben SG27 LIN (Erforderliches Messprodukt für Werte nach Typ2 aus Backend) maximal bis zu 23 mal angegeben werden sofern die anderen PIA Segmente innerhalb derselben SG27 LIN nicht mehr als einmal angegeben werden. Die maximale Anzahl an PIA-Segmenten je SG27 LIN ist 25. |
| **[2074]** | Pro Nachricht ist diese SG27 so oft zu wiederholen, bis für jedes angefragte Produkt derselben SG27 aus der Anfrage eine Angebotsposition angegeben wurde. |
| **[2075]** | Pro SG27 LIN kann die SG27 PIA+Z02 (Artikel-ID) bis zu zweimal angegeben werden. Einmal für die Artikel-ID gemäß Preisblatt B des MSB und einmal für die Artikel-ID "9991000003030-01" (Pauschale Kosten für das Scheitern der Änderung der Technik an einer Lokation) gemäß Preisblatt B des MSB. Hat der MSB in der angegebenen Version des Preisblatt B keine Artikel-ID für "9991000003030-01" (Pauschale Kosten für das Scheitern der Änderung der Technik einer Lokation) angegeben, kann die SG27 PIA+Z02 (Artikel-ID) nur einmal angegeben werden. |
| **[2076]** | Pro SG27 LIN kann die SG31 Preisangabe zur Position nur einmal angegeben werden. Die Angabe der Preisangaben zur Position bezieht sich auf die Artikel-ID bei der es sich nicht um die Artikel-ID "9991000003030-01" (Pauschale Kosten für das Scheitern der Änderung der Technik an einer Lokation) gemäß Preisblatt B des MSB handelt. |

</div>

## UB-Bedingungen

UB-Bedingungen fassen mehrere Marken zu einem Ausdruck zusammen. Sie stehen in den Handbuchzeilen wie eine Bedingung, lösen sich aber in die Marken darin auf.

<div className="maco-tabellenrahmen">

| Marke | Ausdruck |
|---|---|
| **[UB1]** | ([931] ∧ [932] [490]) ⊻ ([931] ∧ [933] [491]) |
| **[UB3]** | ([931] ∧ [932] [492] ∧ [490]) ⊻ ([931] ∧ [933] [492] ∧ [491]) ⊻ ([931] ∧ [934] [493] ∧ [490]) ⊻ ([931] ∧ [935] [493] ∧ [491]) |

</div>

## Bedingungspakete

Bedingungspakete bündeln Voraussetzungen.

<div className="maco-tabellenrahmen">

| Paket | Voraussetzungen | Bedingungen |
|---|---|---|
| **[1P]** | -- | Hinweis: Das ist das Standardpaket, wenn keine Bedingung zum Tragen kommt, z. B. im COM-Segment. |
| **[2P]** | [8] | [8] Wenn SG28 CCI+++E13 CAV+EHZ vorhanden |
| **[3P]** | [25] | [25] Wenn SG28 CCI+++E13 CAV+MME vorhanden |
| **[4P]** | [492] | [492 ]  wenn MP-ID in NAD+MR aus Sparte Strom |
| **[5P]** | [493] | [493 ]  wenn MP-ID in NAD+MR aus Sparte Gas |

</div>

<Hinweisbereich>

Diese Seite führt den Klartext jeder Bedingung, auf die das Anwendungshandbuch des Nachrichtentyps **QUOTES** in dieser Formatversion verweist. Eine Zeile des Handbuchs schreibt `Muss [704]`; was [704] verlangt, steht hier.

Die Liste gilt **für den Nachrichtentyp**, nicht für einen einzelnen Prüfidentifikator. Das ist keine Vereinfachung, sondern die Form der Quelle: die Bedingungsliste liegt in jeder Handbuchdatei des Formats identisch vor.

:::caution{title="Warum hier keine Zuordnung zu einzelnen Prüfidentifikatoren steht"}

Das Zwischenformat, aus dem diese Dokumentation die Handbuchzeilen liest, ordnet Bedingungen einer **Spalte** zu — und diese Zuordnung ist gegen das Original verschoben. Gemessen am 05.09.2026 an UTILMD Strom: das Handbuch führt `STS DE9013` als `X [360]` (nur Zustimmungscodes) beim Prüfidentifikator **55017** und `X [359]` (nur Ablehnungscodes) bei **55018**; das Zwischenformat setzt `[360]` auf 55016 und `[359]` auf 55017 **und** 55018. Dasselbe bei `FTX Muss [83]`: im Handbuch bei 55018, im Zwischenformat bei 55017.

Unabhängig bestätigt durch die Änderungslisten der Quelle: die Änderungs-IDs 25242, 25821, 25822, 25445 und 25243 verorten [83], [351] und [352] ausdrücklich beim „Anwendungsfall 55018 Ablehnung Kündigung“. Kein Eintrag ordnet sie 55016 oder 55017 zu.

Deshalb steht hier der **Text** jeder Bedingung und nirgends die Behauptung, welche Bedingung für welchen Prüfidentifikator gilt. Wer das braucht, schlägt im Original-Anwendungshandbuch nach.

:::

:::note{title="2 Bedingungen stehen nicht in jeder Handbuchdatei"}

Die Bedingungsliste ist formatweit gemeint, ist es aber nicht überall: die folgenden Marken kommen in weniger als allen 5 Dateien dieses Formats vor. Sie stehen trotzdem hier — eine Bedingung wegzulassen, weil eine Datei sie nicht führt, hieße einen Verweis wieder ins Leere zeigen zu lassen.

[UB1], [UB3]

:::

Gemessen am 05.09.2026 verweist **keine** `ahb_expression` dieser Quelle auf eine Paketmarke — die Bedingungspakete stehen auf dieser Seite, weil die Quelle sie führt, nicht weil eine Handbuchzeile auf sie zeigt.

</Hinweisbereich>
