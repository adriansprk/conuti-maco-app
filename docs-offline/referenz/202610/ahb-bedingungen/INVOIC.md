# Bedingungen INVOIC
<span hidden data-pagefind-meta={"title:Bedingungen INVOIC — Anwendungshandbuch (FV 202610)"} />

EDIFACT-Nachrichtentyp **INVOIC** · Formatversion **202610** · 132 Bedingungen · 1 Pakete · 3 UB-Bedingungen · aus 11 Handbuchdatei(en)

## Bedingungen

<div className="maco-tabellenrahmen">

| Marke | Bedingung |
|---|---|
| **[1]** | Wenn in zu stornierender Rechnung gefüllt |
| **[2]** | Wenn es sich um eine Nutzungsüberlassung (Pacht) eines Gerätes handelt |
| **[3]** | Wenn es sich um einen Kauf eines Gerätes handelt |
| **[4]** | Wenn Steuerschuldnerschaft des Leistungsempfängers vorliegt |
| **[5]** | Wenn NAD+MR DE3207 &lt;&gt; "DE" |
| **[6]** | Wenn NAD+MR DE3207 = "DE" |
| **[7]** | Sofern keine Großkundenpostleitzahl verwendet wird |
| **[8]** | Bei zeitabhängigen Preisen |
| **[9]** | Wenn SG26 DTM+203 nicht vorhanden |
| **[10]** | Wenn SG26 DTM+155/156 nicht vorhanden |
| **[11]** | Wenn Abschlag anfällt |
| **[12]** | Wenn SG26 QTY+136 vorhanden |
| **[13]** | Wenn vorausbezahlter Betrag vorliegt |
| **[14]** | Wenn in selben SG26 LIN DE7140 = "9990001000748" (Mehrmenge) |
| **[15]** | Wenn eine Bilanzierung erfolgt ist |
| **[16]** | Wenn eine Netznutzung erfolgt ist |
| **[17]** | Wenn DTM+Z11 vorhanden |
| **[18]** | Wenn IMD++WIM nicht vorhanden |
| **[19]** | Wenn IMD++WIM vorhanden |
| **[20]** | Wenn fälliger Betrag (SG50 MOA+9) ≥ 0 |
| **[21]** | Wenn fälliger Betrag (SG50 MOA+9) &lt; 0 |
| **[22]** | Wenn vorhanden |
| **[23]** | Wenn im selben NAD DE3124 nicht vorhanden |
| **[24]** | Wert muss mindestens 10 WT nach Wert aus DTM+137 DE2380 liegen |
| **[25]** | Wert darf maximal 10 WT nach Wert aus DTM+137 DE2380 liegen |
| **[26]** | Wenn SG39 ALC+A+:Z04 vorhanden |
| **[27]** | Wenn SG39 ALC+C vorhanden |
| **[28]** | Wenn Zuschlag anfällt |
| **[29]** | [Wenn DTM+155 (Abrechnungszeitraum Beginn) nicht größer 31.12.2015 |
| **[30]** | Wenn MP-ID in NAD+MR nicht in der Rolle MGV oder KN |
| **[31]** | Wenn MP-ID in NAD+MR in der Rolle MGV |
| **[32]** | Wenn SG39 ALC+A+:Z01 (Gemeinderabatt) vorhanden |
| **[34]** | Wenn in Ursprungsrechnung vorhanden |
| **[36]** | Wenn DTM+156 (Abrechnungszeitraum Ende) ≥ 01.12.2019 |
| **[37]** | Wenn Lieferschein zuvor ausgetauscht wurde |
| **[40]** | Es sind nur die Artikelnummern erlaubt, die in der Codeliste der Artikelnummern und Artikel-ID mit dem entsprechenden Prüfidentifikator versehen sind oder Artikel-ID aus der Codeliste der Artikelnummern und Artikel-ID. |
| **[41]** | Wenn IMD++SOR vorhanden |
| **[42]** | Wenn DTM+155 (Abrechnungszeitraum Beginn) ≥ 1.1.2023 0:00 gesetzlicher deutscher Zeit |
| **[44]** | Wenn IMD++ABS nicht vorhanden |
| **[45]** | Nur MP-ID aus Sparte Strom |
| **[47]** | Wenn IMD++Z43 vorhanden |
| **[48]** | Wenn IMD++Z44 vorhanden |
| **[49]** | Wenn IMD++Z43 und IMD+Z44 nicht vorhanden |
| **[50]** | Wenn IMD++SOR nicht vorhanden |
| **[51]** | Wenn SG26 DTM+156 (Positionsbezogener Abrechnungszeitraum Ende) ≤ 1.1.2023 0:00 gesetzlicher deutscher Zeit |
| **[53]** | Wenn IMD++Z45 vorhanden |
| **[54]** | Wenn IMD++ABR/JVR/ZVR vorhanden |
| **[55]** | Wenn IMD++ABS vorhanden |
| **[56]** | Wenn DTM+137 (Nachrichtendatum) ≥ 1.1.2023 0:00 gesetzlicher deutscher Zeit |
| **[57]** | Wenn DTM+156 (Abrechnungszeitraum Ende) ≤ 1.1.2023 0:00 gesetzlicher deutscher Zeit |
| **[58]** | Wenn in dieser SG52 MOA+113 vorhanden |
| **[59]** | Wenn SG26 DTM+155 (Positionsbezogener Abrechnungszeitraum Beginn) ≥ 1.1.2023 0:00 gesetzlicher deutscher Zeit |
| **[60]** | Wenn DTM+203 DE2379 in demselben Segment mit Wert 303 vorhanden |
| **[61]** | Wenn DTM+203 DE2379 in demselben Segment mit Wert 102 vorhanden |
| **[64]** | Wenn DTM+156 (Abrechnungszeitraum Ende) ≤ 1.1.2024 0:00 gesetzlicher deutscher Zeit |
| **[65]** | Wenn SG26 DTM+155 (Positionsbezogener Abrechnungszeitraum Beginn) ≥ 1.1.2024 0:00 gesetzlicher deutscher Zeit |
| **[66]** | Wenn IMD++KON vorhanden |
| **[67]** | Es sind nur die Artikelnummern erlaubt, die im Kapitel 2 „Codeliste der Artikelnummer“ in der Codeliste der Artikelnummern und Artikel-ID ein „X“ für den entsprechenden Prüfidentifikator haben. |
| **[68]** | Es sind nur die Artikel-ID erlaubt, die im Kapitel 3 „Codeliste der Gruppenartikel-ID und Artikel-ID“ in der Codeliste der Artikelnummern und Artikel-ID ein „X“ in der Spalte „INVOIC Codeverwendung“ haben. |
| **[69]** | Es sind nur die Artikel-ID erlaubt, die im Kapitel 3 „Codeliste der Gruppenartikel-ID und Artikel-ID“ in der Codeliste der Artikelnummern und Artikel-ID ein „SOR“ in der Spalte „INVOIC Codeverwendung“ haben. |
| **[70]** | Wenn IMD++Z45 nicht vorhanden |
| **[71]** | Wenn DTM+155 (Abrechnungszeitraum Beginn) ≥ 1.1.2024 0:00 gesetzlicher deutscher Zeit |
| **[72]** | Wenn MP-ID in NAD+MR in der Rolle LF |
| **[73]** | Wenn IMD++MSB vorhanden |
| **[74]** | wenn im DE3155 in demselben COM der Code EM vorhanden ist |
| **[75]** | wenn im DE3155 in demselben COM der Code TE / FX / AJ / AL vorhanden ist |
| **[76]** | Wenn MP-ID in NAD+MR in der Rolle NB |
| **[77]** | Wenn SG26 DTM+156 (Positionsbezogener Abrechnungszeitraum Ende) ≤ 1.1.2024 0:00 gesetzlicher deutscher Zeit |
| **[78]** | Wenn GEI+Z08 nicht vorhanden |
| **[79]** | Wenn GEI+Z09 nicht vorhanden |
| **[80]** | Wenn GEI+Z01 nicht vorhanden |
| **[81]** | Wenn GEI+Z04 nicht vorhanden |
| **[82]** | Wenn GEI+Z05 nicht vorhanden |
| **[83]** | Wenn GEI+Z10 nicht vorhanden |
| **[84]** | Wenn in dieser SG39 ALC+C+:Z02 / Z03 / Z04 vorhanden |
| **[85]** | Wenn in diesem Segment DE6411 = DAY |
| **[86]** | Wenn in diesem Segment DE6411 = MON/ANN |
| **[87]** | Wenn IMD++TEC vorhanden |
| **[88]** | Wenn DTM+155 (Abrechnungszeitraum Beginn) ≥ 1.1.2026 0:00 gesetzlicher deutscher Zeit |
| **[90]** | Der Wert muss &lt; 01.01.2027 00:00 Uhr gesetzlicher deutscher Zeit sein |
| **[490]** | wenn Wert in diesem DE, an der Stelle CCYYMMDDHHMM ein Zeitpunkt aus dem angegeben Zeitraum der Tabelle Kapitel 3.5 „Übersicht gesetzliche deutsche Sommerzeit (MESZ)“ der Spalten: „Sommerzeit (MESZ) von“ Darstellung in UTC und „Sommerzeit (MESZ) bis“ Darstellung in UTC ist. |
| **[491]** | wenn Wert in diesem DE, an der Stelle CCYYMMDDHHMM ein Zeitpunkt aus dem angegeben Zeitraum der Tabelle Kapitel 3.6 „Übersicht gesetzliche deutsche Zeit (MEZ)“ der Spalten: „Winterzeit (MEZ) von“ Darstellung in UTC und „Winterzeit (MEZ) bis“ Darstellung in UTC ist. |
| **[492]** | Wenn MP-ID in NAD+MR (Nachrichtenempfänger) aus Sparte Strom |
| **[493]** | Wenn MP-ID in NAD+MR (Nachrichtenempfänger) aus Sparte Gas |
| **[501]** | Hinweis: Dokumentennummer der ORDERS |
| **[502]** | Hinweis: Dokumentennummer der Bilanzierungs-MSCONS |
| **[503]** | Hinweis: Ein positiver Betrag ist eine Forderung des Rechnungsstellers. |
| **[504]** | Hinweis: Ein positiver Betrag ist eine Forderung des Rechnungsempfängers. |
| **[507]** | Hinweis: Dokumentennummer der SSQNOT |
| **[508]** | Hinweis: Dokumentennummer der QUOTES |
| **[509]** | Hinweis: Verwendung der ID der Marktlokation |
| **[510]** | Hinweis: Verwendung der ID der Messlokation |
| **[512]** | Hinweis: Hier ist entweder der Betrag aus MOA+203 oder der um den gültigen Steuerbetrag erhöhte Betrag aus MOA+203 anzugeben. |
| **[513]** | Hinweis: Hier ist das Ergebnis der Multiplikation von MOA+25 mit PCD+3 anzugeben. |
| **[514]** | Hinweis: Dokumentennummer der Lieferschein-MSCONS |
| **[515]** | Hinweis: BGM DE1004 aus INVOIC-Nachricht, die storniert werden soll |
| **[516]** | Hinweis: Ein Lieferschein zu einer Rechnung ist für alle Abrechnungszeiträume, die erstmals nach dem 1.12.2019 abgerechnet werden und für alle Abrechnungszeiträume, für die sich nach dem 1.12.2019 geänderte Mengen oder Leistungswerte ergeben, nötig. |
| **[517]** | Hinweis: Dokumentennummer der PDF-Kapazitätsrechnung |
| **[518]** | Hinweis: Im Fall der Stornierung des Auftrags der Unterbrechung: Der Tag an dem der NB die Stornierung empfangen hat Bei erfolgreicher Sperrung: Tag der durchgeführten Sperrung Bei erfolgloser Sperrung: Letzter Sperrversuchstag |
| **[519]** | Hinweis: Stornierte Abschlagsrechnungen sind nicht aufzuführen |
| **[520]** | Hinweis: Es sind nur die Artikel-IDs aus dem Preisblatt erlaubt |
| **[521]** | Hinweis: BGM DE1004 aus der INVOIC-Nachricht, für die Verzugskosten erhoben werden |
| **[522]** | Hinweis: Verwendung der ID der Netzlokation |
| **[523]** | Hinweis: Verwendung der ID der Steuerbaren Ressource |
| **[524]** | Hinweis: Es darf nur eine Information im DE3148 übermittelt werden |
| **[525]** | Hinweis: Verwendung, sofern Netzentgelte geringer als die Pauschale Netzentgeltreduzierung |
| **[526]** | Hinweis: Der hier angegebene Geldbetrag muss mit dem identisch sein, der in SG50 MOA+77 im DE5004 der Abschlagsrechnung steht, die die Rechnungsnummer hat, die in dieser SG50 in SG51-RFF+AFL in DE1154 genannt ist. |
| **[527]** | Hinweis: Es ist die Umsatzsteuer- bzw. Steuernummer anzugeben, die vorher per PARTIN ausgetauscht wurde. |
| **[902]** | Format: Möglicher Wert: ≥ 0 |
| **[903]** | Format: Möglicher Wert: 1 |
| **[906]** | Format: max. 3 Nachkommastellen |
| **[908]** | Format: Mögliche Werte: 1 bis n |
| **[910]** | Format: Möglicher Wert: &lt; 0 oder ≥ 0 |
| **[911]** | Format: Mögliche Werte: 1 bis n, je Nachricht oder Segmentgruppe bei 1 beginnend und fortlaufend aufsteigend |
| **[912]** | Format: max. 6 Nachkommastellen |
| **[914]** | Format: Möglicher Wert: &gt; 0 |
| **[927]** | Format: Möglicher Wert: -1 |
| **[930]** | Format: max. 2 Nachkommastellen |
| **[931]** | Format: ZZZ = +00 |
| **[932]** | Format: HHMM = 2200 |
| **[933]** | Format: HHMM = 2300 |
| **[934]** | Format: HHMM = 0400 |
| **[935]** | Format: HHMM = 0500 |
| **[937]** | Format: keine Nachkommastelle |
| **[939]** | Format: Die Zeichenkette muss die Zeichen @ und . enthalten |
| **[940]** | Format: Die Zeichenkette muss mit dem Zeichen + beginnen und danach dürfen nur noch Ziffern folgen |
| **[946]** | Format: max. 11 Nachkommastellen |
| **[950]** | Format: Marktlokations-ID |
| **[951]** | Format: Zählpunktbezeichnung |
| **[960]** | Format: Netzlokations-ID |
| **[961]** | Format: SR-ID |
| **[2000]** | Segmentgruppe ist genau einmal anzugeben. |

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
| **[1P]** | -- | Hinweis: Das ist das Standardpaket, wenn keine Bedingung zum Tragen kommt, z. B. im COM-Segment. |

</div>

<Hinweisbereich>

Diese Seite führt den Klartext jeder Bedingung, auf die das Anwendungshandbuch des Nachrichtentyps **INVOIC** in dieser Formatversion verweist. Eine Zeile des Handbuchs schreibt `Muss [704]`; was [704] verlangt, steht hier.

Die Liste gilt **für den Nachrichtentyp**, nicht für einen einzelnen Prüfidentifikator. Das ist keine Vereinfachung, sondern die Form der Quelle: die Bedingungsliste liegt in jeder Handbuchdatei des Formats identisch vor.

:::caution{title="Warum hier keine Zuordnung zu einzelnen Prüfidentifikatoren steht"}

Das Zwischenformat, aus dem diese Dokumentation die Handbuchzeilen liest, ordnet Bedingungen einer **Spalte** zu — und diese Zuordnung ist gegen das Original verschoben. Gemessen am 05.09.2026 an UTILMD Strom: das Handbuch führt `STS DE9013` als `X [360]` (nur Zustimmungscodes) beim Prüfidentifikator **55017** und `X [359]` (nur Ablehnungscodes) bei **55018**; das Zwischenformat setzt `[360]` auf 55016 und `[359]` auf 55017 **und** 55018. Dasselbe bei `FTX Muss [83]`: im Handbuch bei 55018, im Zwischenformat bei 55017.

Unabhängig bestätigt durch die Änderungslisten der Quelle: die Änderungs-IDs 25242, 25821, 25822, 25445 und 25243 verorten [83], [351] und [352] ausdrücklich beim „Anwendungsfall 55018 Ablehnung Kündigung“. Kein Eintrag ordnet sie 55016 oder 55017 zu.

Deshalb steht hier der **Text** jeder Bedingung und nirgends die Behauptung, welche Bedingung für welchen Prüfidentifikator gilt. Wer das braucht, schlägt im Original-Anwendungshandbuch nach.

:::

:::note{title="1 Bedingungen stehen nicht in jeder Handbuchdatei"}

Die Bedingungsliste ist formatweit gemeint, ist es aber nicht überall: die folgenden Marken kommen in weniger als allen 11 Dateien dieses Formats vor. Sie stehen trotzdem hier — eine Bedingung wegzulassen, weil eine Datei sie nicht führt, hieße einen Verweis wieder ins Leere zeigen zu lassen.

[UB2]

:::

Gemessen am 05.09.2026 verweist **keine** `ahb_expression` dieser Quelle auf eine Paketmarke — die Bedingungspakete stehen auf dieser Seite, weil die Quelle sie führt, nicht weil eine Handbuchzeile auf sie zeigt.

</Hinweisbereich>
