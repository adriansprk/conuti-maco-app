# Bedingungen UTILTS
<span hidden data-pagefind-meta={"title:Bedingungen UTILTS — Anwendungshandbuch (FV 202604)"} />

EDIFACT-Nachrichtentyp **UTILTS** · Formatversion **202604** · 107 Bedingungen · 3 Pakete · 1 UB-Bedingungen · aus 8 Handbuchdatei(en)

## Bedingungen

<div className="maco-tabellenrahmen">

| Marke | Bedingung |
|---|---|
| **[1]** | Nur MP-ID aus Sparte Strom |
| **[2]** | Wenn SG5 STS+Z23+Z34 (Berechnungsformel muss beim Absender angefragt werden) in einem SG5 IDE vorhanden |
| **[5]** | Wenn das SG8 RFF+Z19 (Referenz auf eine Messlokation) in derselben SG8 SEQ+Z37 nicht vorhanden |
| **[6]** | Wenn das SG8 RFF+Z23 (Referenz auf Rechenschritt) in derselben SG8 SEQ+Z37 nicht vorhanden |
| **[7]** | Wenn in derselben SG8 SEQ+Z37 das SG8 RFF+Z19 (Referenz auf eine Messlokation) vorhanden |
| **[8]** | Rechenschrittidentifikator aus einem SG8 SEQ+Z37 (Bestandteil des Rechenschritts) DE1050 desselben SG5 IDE+24 und derselben Zeitraum-ID wie bei diesem SG8 |
| **[9]** | Der hier angegebene Rechenschrittidentifikator darf nicht identisch mit dem Rechenschrittidentifikator aus diesem SG8 SEQ+Z37 DE1050 sein |
| **[10]** | wenn vorhanden |
| **[11]** | Wenn in SG8 SEQ+Z37 SG9 CCI+++Z86 CAV+Z69/Z70 (Addition / Subtraktion) vorhanden, darf es in dem Vorgang beliebig viele weitere SG8 SEQ+Z37 mit identischem Rechenschrittidentifikator mit derselben Zeitraum-ID geben, die jedoch ausschließlich die Operatoren Z69/Z70 enthalten dürfen |
| **[12]** | Wenn in SG8 SEQ+Z37 SG9 CCI+++Z86 CAV+Z83 (Positivwert) vorhanden, darf es in dem Vorgang keine weitere SG8 SEQ+Z37 mit identischem Rechenschrittidentifikator und derselben Zeitraum-ID geben |
| **[13]** | Wenn in SG8 SEQ+Z37 SG9 CCI+++Z86 CAV+Z80/Z81 (Divisor / Dividend) vorhanden, muss in diesem Vorgang genau eine zweite SG8 SEQ+Z37 mit identischen Rechenschrittidentifikator und derselben Zeitraum-ID vorhanden sein, sodass das eine SG8 SEQ+Z37 den Operator Z80 (Divisor) und das andere SG8 SEQ+Z37 den Operator Z81 (Dividend) enthält |
| **[14]** | Wenn in SG8 SEQ+Z37 SG9 CCI+++Z86 CAV+Z82 (Faktor) vorhanden, darf es in dem Vorgang beliebig viele weitere SG8 SEQ+Z37 mit identischem Rechenschrittidentifikator und derselben Zeitraum-ID geben, die jedoch ausschließlich CAV+Z82 enthalten |
| **[15]** | Wenn in einem SG5 IDE+24 nur eine SEQ+Z37 mit einer SG8 RFF+Z19 (Messlokation) und der selben Zeitraum-ID vorhanden ist |
| **[21]** | Wenn in dieser CAV+ZD3 der Wert im DE7110 mit Z32 (sonstiger Zählzeitdefinitionstyp) vorhanden ist |
| **[22]** | Wenn MP-ID in SG2 NAD+MS (Nachrichtenabsender) in der Rolle NB |
| **[24]** | Wenn SG5 STS+Z36+Z45 (Definitionen werden verwendet) vorhanden |
| **[25]** | Wenn MP-ID in SG2 NAD+MR (Nachrichtenempfänger) in der Rolle LF |
| **[26]** | sofern per ORDERS reklamiert |
| **[27]** | Wenn in SG9 CAV+ZD4+Z26 (keine Verwendung des Hochlastzeitfensters) vorhanden |
| **[29]** | Wenn in SG8 SEQ+Z43 DTM+Z33 (Zählzeitänderungszeitpunkt) im DE2379 der Code 303 vorhanden |
| **[30]** | Der Wert von CCYY in diesem DE muss genau um eins höher sein, als der Wert CCYY des SG5 DTM+Z34 (Gültigkeitsbeginn) DE2380 |
| **[31]** | Wenn im DE2379 dieses Segments der Code 303 vorhanden |
| **[32]** | Der Zeitpunkt in diesem DE muss ≥ dem Zeitpunkt aus dem DE2380 des Gültigkeitsbeginn der ausgerollten Definition (SG5 DTM+Z34) sein |
| **[33]** | Der Zeitpunkt in diesem DE muss ≤ dem Zeitpunkt aus dem DE2380 des Gültigkeitsende der ausgerollten Definition (SG5 DTM+Z35) sein |
| **[34]** | Wenn im DE2379 dieses Segments der Code 401 vorhanden |
| **[36]** | Wenn in SG8 SEQ+Z43 DTM+Z33 (Zählzeitänderungszeitpunkt) im DE2379 der Code 401 vorhanden |
| **[37]** | Wenn ein Gültigkeitsende bereits angegeben werden kann. |
| **[41]** | Wenn SG8 SEQ+Z42 (Zählzeitdefinition) vorhanden |
| **[42]** | Der in diesem Datenlement angegebene Code der Schaltzeitdefinition muss innerhalb eines Vorgangs (IDE) eindeutig sein. |
| **[43]** | Der in diesem Datenlement angegebene Code der Leistungskurvendefinition muss innerhalb eines Vorgangs (IDE) eindeutig sein. |
| **[44]** | Der in diesem Datenlement angegebene Code der Zählzeitdefinition muss innerhalb eines Vorgangs (IDE) eindeutig sein. |
| **[46]** | Wenn in SG8 SEQ+Z73 DTM+Z44 (Schaltzeitänderungszeitpunkt) im DE2379 der Code 303 vorhanden |
| **[47]** | Wenn in SG8 SEQ+Z73 DTM+Z44 (Schaltzeitänderungszeitpunkt) im DE2379 der Code 401 vorhanden |
| **[48]** | Wenn in SG8 SEQ+Z74 DTM+Z45 (Leistungskurvenänderungszeitpunkt) im DE2379 der Code 303 vorhanden |
| **[49]** | Wenn in SG8 SEQ+Z74 DTM+Z45 (Leistungskurvenänderungszeitpunkt) im DE2379 der Code 401 vorhanden |
| **[50]** | In jedem DE2379 dieses DTM-Segments innerhalb eines IDE+24 (Vorgangs) muss der gleiche Code angegeben werden |
| **[53]** | Wenn im DE3155 in demselben COM der Code EM vorhanden ist |
| **[54]** | Wenn im DE3155 in demselben COM der Code TE / FX / AJ / AL vorhanden ist |
| **[55]** | Es ist der Wert einzutragen, der sich aus der Wiederholungshäufigkeit des SG6 RFF+Z49/Z53 (Verwendungszeitraum der Daten: Gültige Daten/Keine Daten) ergibt. Bedeutet: Das erste SG6 RFF+Z49/Z53 hat somit die „1“, das zweite die „2“, das dritte die „3“ usw. |
| **[56]** | Wenn dieses DTM+Z25 (Verwendung der Daten ab) im SG6 RFF (Verwendungszeitraum der Daten) mit der Zeitraum ID "1" im DE1156 ist, muss das Datum der darauffolgende oder ein älterer Tag 0:00 Uhr deutscher Zeit vom DTM+137 DE2380 (Nachrichtendatum) entsprechen |
| **[57]** | Wenn dieses DTM+Z25 (Verwendung der Daten ab) nicht im SG6 RFF+Z49/Z53 (Verwendungszeitraum der Daten: Gültige Daten/Keine Daten) mit der Zeitraum ID "1" im DE1156 ist, muss das Datum dem DTM+Z26 (Verwendung der Daten bis) des SG6 RFF+Z49/Z53 (Verwendungszeitraum der Daten: Gültige Daten/Keine Daten) mit der nächst niedrigeren Zeitraum ID im DE1156 entsprechen |
| **[58]** | Wenn im selben SG6 RFF+Z49/Z53 (Verwendungszeitraum der Daten: Gültige Daten/Keine Daten) im DE1156 (Zeitraum-ID) eine Zeitraum ID genannt ist, die kleiner ist als in einem anderen SG6 RFF+Z49/Z53 (Verwendungszeitraum der Daten: Gültige Daten/Keine Daten) DE1156 (Zeitraum-ID) |
| **[59]** | Es ist die Zeitraum-ID vom DE1156 aus einem passenden SG6 RFF+Z49 (Verwendungszeitraum der Daten) einzutragen |
| **[61]** | Wenn in einem STS+E01 im DE9013 (Status der Antwort) ein Antwortcode aus dem Cluster Ablehnung vorhanden ist |
| **[62]** | Wenn MP-ID in SG2 NAD+MR (Nachrichtenempfänger) in der Rolle MSB |
| **[63]** | Wenn MP-ID in SG2 NAD+MR (Nachrichtenempfänger) in der Rolle NB |
| **[490]** | wenn Wert in diesem DE, an der Stelle CCYYMMDDHHMM ein Zeitpunkt aus dem angegeben Zeitraum der Tabelle Kapitel 3.5 „Übersicht gesetzliche deutsche Sommerzeit (MESZ)“ der Spalten: „Sommerzeit (MESZ) von“ Darstellung in UTC und „Sommerzeit (MESZ) bis“ Darstellung in UTC ist. |
| **[491]** | wenn Wert in diesem DE, an der Stelle CCYYMMDDHHMM ein Zeitpunkt aus dem angegeben Zeitraum der Tabelle Kapitel 3.6 „Übersicht gesetzliche deutsche Zeit (MEZ)“ der Spalten: „Winterzeit (MEZ) von“ Darstellung in UTC und „Winterzeit (MEZ) bis“ Darstellung in UTC ist. |
| **[494]** | Das hier genannte Datum muss der Zeitpunkt sein, zu dem das Dokument erstellt wurde, oder ein Zeitpunkt, der davor liegt. |
| **[501]** | Hinweis: Verwendung der ID der Marktlokation |
| **[502]** | Hinweis: Verwendung der ID der Messlokation |
| **[504]** | Hinweis: Wert aus BGM+Z55 DE1004 der ORDERS mit der die Reklamation einer Definition erfolgt ist |
| **[505]** | Hinweis: Jede ausgerollte Zählzeitdefinition ist in einem eigenen IDE anzugeben |
| **[506]** | Hinweis: Zeitpunkt, ab dem die Übersicht der Zählzeitdefinitionen gültig ist |
| **[507]** | Hinweis: Es ist die Zeit nach der deutschen gesetzlichen Zeit anzugeben |
| **[508]** | Hinweis: Zeitpunkt, ab dem die Übersicht der Schaltzeitdefinitionen gültig ist |
| **[509]** | Hinweis: Zeitpunkt, ab dem die Übersicht der Leistungskurvendefinition gültig ist |
| **[510]** | Hinweis: Für jeden Zählzeitänderungszeitpunkt (SG8 DTM+Z33) ist diese Sementgruppe einmal anzugeben |
| **[511]** | Hinweis: Der Zählzeitänderungszeitpunkt (SG8DTM+Z33) dieser SG8 darf in keiner anderen SG8 „Zählzeitdefinition“ wiederholt werden |
| **[512]** | Hinweis: Wenn der Code 303 im DE2379 des Zählzeitänderungszeitpunkt (SG8 DTM+Z33) genutzt wird, muss genau ein Wert im DE2380 des Zählzeitänderungszeitpunkt (SG8 DTM+Z33) identisch mit dem Wert aus DE2380 des Gültigkeitsbeginn der ausgerollten Definition (SG5 DTM+Z34) sein |
| **[513]** | Hinweis: Wenn der Code 401 im DE2379 des Zählzeitänderungszeitpunkt (SG8 DTM+Z33) genutzt wird, muss genau ein Wert = 0000 im DE2380 des Zählzeitänderungszeitpunkt (SG8 DTM+Z33) sein |
| **[514]** | Hinweis: Für jeden Schaltzeitänderungszeitpunkt (SG8 DTM+Z44) ist diese Sementgruppe einmal anzugeben |
| **[515]** | Hinweis: Kein Schaltzeitänderungszeitpunkt (SG8 DTM+Z44) darf mehrfach vorkommen |
| **[516]** | Hinweis: Wenn der Code 303 im DE2379 des Schaltzeitänderungszeitpunkt (SG8 DTM+Z44) genutzt wird, muss genau ein Wert im DE2380 des Schaltzeitänderungszeitpunkt (SG8 DTM+Z44) identisch mit dem Wert aus DE2380 des Gültigkeitsbeginn der ausgerollten Definition (SG5 DTM+Z34) sein |
| **[517]** | Hinweis: Wenn der Code 401 im DE2379 des Schaltzeitänderungszeitpunkt (SG8 DTM+Z44) genutzt wird, muss genau ein Wert = 0000 im DE2380 des Schaltzeitänderungszeitpunkt (SG8 DTM+Z44) sein |
| **[518]** | Hinweis: Für jeden Leistungskurvenänderungszeitpunkt (SG8 DTM+Z45) ist diese Sementgruppe einmal anzugeben |
| **[519]** | Hinweis: Kein Leistungskurvenänderungszeitpunkt (SG8 DTM+Z45) darf mehrfach vorkommen |
| **[520]** | Hinweis: Wenn der Code 303 im DE2379 des Leistungskurvenänderungszeitpunkt (SG8 DTM+Z45) genutzt wird, muss genau ein Wert im DE2380 des Leistungskurvenänderungszeitpunkt (SG8 DTM+Z45) identisch mit dem Wert aus DE2380 des Gültigkeitsbeginn der ausgerollten Definition (SG5 DTM+Z34) sein |
| **[521]** | Hinweis: Wenn der Code 401 im DE2379 des Leistungskurvenänderungszeitpunkt (SG8 DTM+Z45) |
| **[522]** | Hinweis: Jede ausgerollte Schaltzeitdefinition ist in einem eigenen IDE anzugeben |
| **[523]** | Hinweis: Jede ausgerollte Leistungskurvendefinition ist in einem eigenen IDE anzugeben |
| **[524]** | Hinweis: Es ist der Code einer Zählzeitdefinition anzugeben |
| **[525]** | Hinweis: Es ist der Code einer Schaltzeitdefinition anzugeben |
| **[526]** | Hinweis: Es ist der Code einer Leistungskurvendefinition anzugeben |
| **[527]** | Hinweis: Dieser Code ist anzugeben, wenn es sich um eine einmalig zu übermittelnde Definition handelt |
| **[528]** | Hinweis: Dieser Code ist anzugeben, wenn es sich um eine jährlich zu übermittelnde Definition handelt |
| **[529]** | Hinweis: Verwendung der ID der Netzlokation |
| **[530]** | Hinweis: Es darf nur eine Information im DE3148 übermittelt werden |
| **[531]** | Hinweis: Für weitere Details siehe Kapitel 4.1 "Übermittlung einer Vielzahl von Berechnungsformeln in einem Vorgang" |
| **[532]** | Hinweis: Es ist die Zeitraum-ID vom DE1156 aus einem passenden SG6 RFF+Z49/Z53 (Verwendungszeitraum der Daten: "Gültige Daten", "Keine Daten") aus der Übermittlung der Berechnungsformel aus SG6 RFF+TN DE1154 (Referenz Vorgangsnummer (aus Berechnungsformel)) einzutragen |
| **[533]** | Hinweis: Für jeden übermittelten Zeitraum aus der Übermittlung der Berechnungsformel ist genau einmal das Segement anzugeben |
| **[534]** | Hinweis: Wert aus SG5 IDE+24 DE7402 mit der die Übermitt-lung der Berechnungsformel erfolgt ist. |
| **[912]** | Format: Wert kann mit maximal 6 Nachkommastellen angegeben werden |
| **[913]** | Format: Mögliche Werte: 1 bis 99999 |
| **[914]** | Format: Möglicher Wert: &gt; 0 |
| **[915]** | Format: Möglicher Wert: ≠ 1 |
| **[930]** | Format: max. 2 Nachkommastellen |
| **[931]** | Format: ZZZ = +00 |
| **[932]** | Format: HHMM = 2200 |
| **[933]** | Format: HHMM = 2300 |
| **[937]** | Format: keine Nachkommastelle |
| **[939]** | Format: Die Zeichenkette muss die Zeichen @ und . enthalten |
| **[940]** | Format: Die Zeichenkette muss mit dem Zeichen + beginnen und danach dürfen nur noch Ziffern folgen |
| **[947]** | Format: MMDDHHMM = 12312300 |
| **[950]** | Format: Marktlokations-ID |
| **[951]** | Format: Zählpunktbezeichnung |
| **[960]** | Format: Netzlokations-ID |
| **[963]** | Format: Möglicher Wert: ≤ 100 |
| **[964]** | Format: HHMM ≥ 0000 |
| **[965]** | Format: HHMM ≤ 2359 |
| **[969]** | Format: Möglicher Wer: ≤ 1 |
| **[2001]** | Segment bzw. Segmentgruppe ist genau einmal anzugeben |
| **[2002]** | Für jeden Code der Zählzeit aus SG8 SEQ+Z42 (Zählzeitdefinition) SG9 CCI+Z39 (Code der Zählzeitdefinition) sind mindestens zwei Register anzugeben, bei denen in dieser SG8 das SG8 RFF+Z27 mit diesem Code gefüllt ist |
| **[2004]** | Segment ist genau einmal für jede Zeitraum-ID aus dem DE1156 der SG6 RFF+Z49 (Verwendungszeitraum der Daten: "Gültige Daten") anzugeben |
| **[2005]** | Segment ist genau einmal für jede Zeitraum-ID aus dem DE9012 der SG5 STS+E01 ("Status der Antwort") anzugeben, wenn im selben SG5 STS+E01 im DE9013 der Code A99 ("Sonstiges") enthalten ist |
| **[2006]** | Segmentgruppe ist mindestens einmal für jede Zeitraum-ID aus dem DE9013 der SG5 STS+Z23+Z33 (Berechnungsformel angefügt) anzugeben |
| **[2007]** | Segmentgruppe ist genau einmal für jede Zeitraum-ID aus dem DE9013 der SG5 STS+Z23+Z33 (Berechnungsformel angefügt) anzugeben |

</div>

## UB-Bedingungen

UB-Bedingungen fassen mehrere Marken zu einem Ausdruck zusammen. Sie stehen in den Handbuchzeilen wie eine Bedingung, lösen sich aber in die Marken darin auf.

<div className="maco-tabellenrahmen">

| Marke | Ausdruck |
|---|---|
| **[UB1]** | ([931] ∧ [932] [490]) ⊻ ([931] ∧ [933] [491]) |

</div>

## Bedingungspakete

Bedingungspakete bündeln Voraussetzungen.

<div className="maco-tabellenrahmen">

| Paket | Voraussetzungen | Bedingungen |
|---|---|---|
| **[1P]** | -- | Hinweis: Das ist das Standardpaket, wenn keine Bedingung zum Tragen kommt, z. B. im COM-Segment. |
| **[2P]** | [25]   ⊻  [62]  ⊻  [6 3 ] | [25] Wenn MP-ID in SG2 NAD+MR (Nachrichtenempfänger) in der Rolle LF [62]  Wenn MP-ID in SG2 NAD+MR (Nachrichtenempfänger) in der Rolle MSB [63]  Wenn MP-ID in SG2 NAD+MR (Nachrichtenempfänger) in der Rolle  NB |
| **[3P]** | [25]  ⊻  [6 3 ] | [25] Wenn MP-ID in SG2 NAD+MR (Nachrichtenempfänger) in der Rolle LF [63]  Wenn MP-ID in SG2 NAD+MR (Nachrichtenempfänger) in der Rolle  NB |

</div>

<Hinweisbereich>

Diese Seite führt den Klartext jeder Bedingung, auf die das Anwendungshandbuch des Nachrichtentyps **UTILTS** in dieser Formatversion verweist. Eine Zeile des Handbuchs schreibt `Muss [704]`; was [704] verlangt, steht hier.

Die Liste gilt **für den Nachrichtentyp**, nicht für einen einzelnen Prüfidentifikator. Das ist keine Vereinfachung, sondern die Form der Quelle: die Bedingungsliste liegt in jeder Handbuchdatei des Formats identisch vor.

:::caution{title="Warum hier keine Zuordnung zu einzelnen Prüfidentifikatoren steht"}

Das Zwischenformat, aus dem diese Dokumentation die Handbuchzeilen liest, ordnet Bedingungen einer **Spalte** zu — und diese Zuordnung ist gegen das Original verschoben. Gemessen am 05.09.2026 an UTILMD Strom: das Handbuch führt `STS DE9013` als `X [360]` (nur Zustimmungscodes) beim Prüfidentifikator **55017** und `X [359]` (nur Ablehnungscodes) bei **55018**; das Zwischenformat setzt `[360]` auf 55016 und `[359]` auf 55017 **und** 55018. Dasselbe bei `FTX Muss [83]`: im Handbuch bei 55018, im Zwischenformat bei 55017.

Unabhängig bestätigt durch die Änderungslisten der Quelle: die Änderungs-IDs 25242, 25821, 25822, 25445 und 25243 verorten [83], [351] und [352] ausdrücklich beim „Anwendungsfall 55018 Ablehnung Kündigung“. Kein Eintrag ordnet sie 55016 oder 55017 zu.

Deshalb steht hier der **Text** jeder Bedingung und nirgends die Behauptung, welche Bedingung für welchen Prüfidentifikator gilt. Wer das braucht, schlägt im Original-Anwendungshandbuch nach.

:::

:::note{title="1 Bedingungen stehen nicht in jeder Handbuchdatei"}

Die Bedingungsliste ist formatweit gemeint, ist es aber nicht überall: die folgenden Marken kommen in weniger als allen 8 Dateien dieses Formats vor. Sie stehen trotzdem hier — eine Bedingung wegzulassen, weil eine Datei sie nicht führt, hieße einen Verweis wieder ins Leere zeigen zu lassen.

[UB1]

:::

Gemessen am 05.09.2026 verweist **keine** `ahb_expression` dieser Quelle auf eine Paketmarke — die Bedingungspakete stehen auf dieser Seite, weil die Quelle sie führt, nicht weil eine Handbuchzeile auf sie zeigt.

</Hinweisbereich>
