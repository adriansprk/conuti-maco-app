# Bedingungen IFTSTA
<span hidden data-pagefind-meta={"title:Bedingungen IFTSTA — Anwendungshandbuch (FV 202604)"} />

EDIFACT-Nachrichtentyp **IFTSTA** · Formatversion **202604** · 151 Bedingungen · 1 Pakete · 3 UB-Bedingungen · aus 35 Handbuchdatei(en)

## Bedingungen

<div className="maco-tabellenrahmen">

| Marke | Bedingung |
|---|---|
| **[1]** | Wenn die Übermittlung nicht codierbarer Informationen nötig ist. |
| **[3]** | Wenn SG7 STS+Z01 nicht vorhanden. |
| **[4]** | Wenn SG7 STS+Z02 nicht vorhanden. |
| **[5]** | Wenn SG7 STS+Z03 nicht vorhanden. |
| **[6]** | Wenn für das 3-Tupel (MaBiS-ZP, Betrachtungszeitraum, Version der Summenzeitreihe) dem BIKO der Prüfstatus vorliegt, so ist dieser immer zusammen mit dem Datenstatus zu übertragen. |
| **[7]** | Wenn der Datenstatus "Abgerechnete Daten" bzw. "Abgerechnete Daten Korrektur-BKA" nicht vorhanden. |
| **[8]** | Wenn der Datenstatus einer NZR vom BIKO an NB nicht vorhanden. |
| **[10]** | Wenn Meldung des BKV/NB/ÜNB nach Frist eingeht. |
| **[16]** | Wenn MP-ID in SG1 NAD+MR in der Rolle BKV |
| **[17]** | Wenn Meldung des BKV auf falscher Aggregationsebene eingeht. |
| **[18]** | Wenn SG15 STS+Z19 nicht vorhanden. |
| **[19]** | Wenn SG15 STS+Z24 nicht vorhanden. |
| **[20]** | Wenn MP-ID in SG1 NAD+MR in der Rolle LF |
| **[23]** | Wenn SG15 STS+Z25+Z31+A06 / A09 / A10 / A11 / A13 / A14 / A15 / A16 vorhanden. |
| **[26]** | Wenn MP-ID in SG1 NAD+MR in der Rolle NB |
| **[27]** | Nur MP-ID aus Sparte Strom |
| **[28]** | Nur MP-ID aus Sparte Gas |
| **[29]** | Wenn MP-ID in SG1 NAD+MR in der Rolle ÜNB |
| **[30]** | Wenn in dieser SG15 STS+Z20+Z32+A07:E_0207 vorhanden. |
| **[31]** | Wenn in dieser SG16 in QTY in DE6411 KWH/K3 vorhanden. |
| **[32]** | Wenn in dieser SG16 in QTY in DE6411 KWT/K5 vorhanden. |
| **[33]** | Wenn in dieser SG16 DTM+163 vorhanden. |
| **[43]** | Wenn STS+Z01+Z07 vorhanden, dann sind nur Codes aus dem EBD-Cluster "Zustimmung" möglich. |
| **[44]** | Wenn STS+Z01+Z08 vorhanden, dann sind nur Codes aus dem EBD-Cluster "Ablehnung" möglich. |
| **[45]** | Wenn STS+Z03+Z07 vorhanden, dann sind nur Codes aus dem EBD-Cluster "Zustimmung" möglich. |
| **[46]** | Wenn STS+Z03+Z08 vorhanden, dann sind nur Codes aus dem EBD-Cluster "Ablehnung" möglich. |
| **[47]** | Es sind nur Codes aus dem EBD-Cluster "Ablehnung" möglich. |
| **[48]** | Es sind nur Codes aus dem EBD-Cluster "Zustimmung" möglich. |
| **[49]** | Wenn STS+Z25+Z30 vorhanden, dann sind nur Codes aus dem EBD-Cluster "Zustimmung" möglich. |
| **[50]** | Wenn STS+Z25+Z31 vorhanden, dann sind nur Codes aus dem EBD-Cluster "Ablehnung" möglich. |
| **[51]** | Es sind nur Codes aus dem EBD-Cluster "Abweisung" möglich. |
| **[52]** | Wenn STS+Z27+Z32 vorhanden |
| **[53]** | Wenn STS+Z28+Z32 vorhanden |
| **[54]** | Wenn STS+Z29+Z32 vorhanden |
| **[55]** | Wenn STS+Z30+Z32 vorhanden |
| **[56]** | Wenn in dieser SG15 STS das SG15 RFF+ACW nicht identisch mit dem SG15 RFF+ACW der SG15 STS+Z27 ist |
| **[57]** | Wenn in dieser SG15 STS das SG15 RFF+ACW nicht identisch mit dem SG15 RFF+ACW der SG15 STS+Z28 ist |
| **[58]** | Wenn in dieser SG15 STS das SG15 RFF+ACW nicht identisch mit dem SG15 RFF+ACW der SG15 STS+Z29 ist |
| **[59]** | Wenn in dieser SG15 STS das SG15 RFF+ACW nicht identisch mit dem SG15 RFF+ACW der SG15 STS+Z30 ist |
| **[60]** | Wenn zusätzlich zum Fahrplananteil auch die Ausfallarbeit zu identischem Wert aus RFF+ACW nicht o.k. ist |
| **[61]** | Wenn zusätzlich zur Ausfallarbeit auch der Fahrplananteil zu identischem Wert aus RFF+ACW nicht o.k. ist |
| **[62]** | Wenn STS+Z27+Z30 vorhanden, dann sind nur Codes aus dem EBD-Cluster "Zustimmung" möglich. |
| **[63]** | Wenn STS+Z27+Z32 vorhanden, dann sind nur Codes aus dem EBD-Cluster "Ablehnung" möglich. |
| **[64]** | Wenn STS+Z28+Z30 vorhanden, dann sind nur Codes aus dem EBD-Cluster "Zustimmung" möglich. |
| **[65]** | Wenn STS+Z28+Z32 vorhanden, dann sind nur Codes aus dem EBD-Cluster "Ablehnung" möglich. |
| **[66]** | Wenn STS+Z29+Z30 vorhanden, dann sind nur Codes aus dem EBD-Cluster "Zustimmung" möglich. |
| **[67]** | Wenn STS+Z29+Z32 vorhanden, dann sind nur Codes aus dem EBD-Cluster "Ablehnung" möglich. |
| **[68]** | Wenn STS+Z30+Z30 vorhanden, dann sind nur Codes aus dem EBD-Cluster "Zustimmung" möglich. |
| **[69]** | Wenn STS+Z30+Z32 vorhanden, dann sind nur Codes aus dem EBD-Cluster "Ablehnung" möglich. |
| **[70]** | Wenn zusätzlich zum Gegenvorschlag des Fahrplananteils auch der Gegenvorschlag der Ausfallarbeit zu identischem Wert aus RFF+ACW nicht o.k. ist |
| **[71]** | Wenn zusätzlich zum Gegenvorschlag der Ausfallarbeit auch der Gegenvorschlag des Fahrplananteils zu identischem Wert aus RFF+ACW nicht o.k. ist |
| **[72]** | Wenn Gegenvorschlag erstellt werden kann |
| **[76]** | Wenn MP-ID in SG1 NAD+MR in der Rolle ESA |
| **[77]** | Wenn STS+Z37+Z14 in dieser SG14 vorhanden |
| **[78]** | Wenn STS+Z38 in dieser SG14 nicht vorhanden |
| **[79]** | Wenn STS+Z37 in dieser SG14 nicht vorhanden |
| **[80]** | Wenn STS+Z38+Z14 in dieser SG14 vorhanden |
| **[83]** | Wenn STS+Z37+Z13+A04/A05/A06:E_0472 in dieser SG14 vorhanden |
| **[84]** | Wenn STS+Z38+Z13+A02: E_0499 in dieser SG14 vorhanden |
| **[85]** | Wenn STS+Z37+Z32+A01: E_0501 in dieser SG14 vorhanden |
| **[86]** | Wenn MP-ID in SG1 NAD+MS in der Rolle LF |
| **[91]** | Wenn in diesem STS DE1131 = E_0472 |
| **[92]** | Wenn in diesem STS DE1131 = E_0501 |
| **[93]** | Wenn STS+Z37+Z13 vorhanden, dann sind nur Codes aus dem EBD-Cluster "gescheitert" möglich. |
| **[94]** | Wenn STS+Z37+Z14 vorhanden, dann sind nur Codes aus dem EBD-Cluster "erfolgreich" möglich. |
| **[95]** | Wenn in diesem STS DE1131 = E_0499 |
| **[96]** | Wenn in diesem STS DE1131 = E_0487 |
| **[97]** | Wenn STS+Z38+Z13 vorhanden, dann sind nur Codes aus dem EBD-Cluster "gescheitert" möglich. |
| **[98]** | Wenn STS+Z38+Z14 vorhanden, dann sind nur Codes aus dem EBD-Cluster "erfolgreich" möglich. |
| **[99]** | Wenn in diesem STS DE1131 = E_0487, dann ist nur der Code A01 möglich. |
| **[100]** | Wenn STS+Z43+Z47 vorhanden, dann sind nur Codes aus dem EBD-Cluster "Änderung der Daten" möglich. |
| **[101]** | Wenn STS+Z43+Z48 vorhanden, dann sind nur Codes aus dem EBD-Cluster "keine Änderung der Daten" möglich. |
| **[103]** | Wenn in diesem STS DE1131 nicht vorhanden |
| **[107]** | Wenn STS+Z37+Z32 vorhanden, dann sind nur Codes aus dem EBD-Cluster "Ablehnung" möglich. |
| **[114]** | Wenn MP-ID in SG1 NAD+MS in der Rolle MSB |
| **[115]** | Wenn MP-ID in SG1 NAD+MS in der Rolle NB |
| **[117]** | Wenn MP-ID in SG1 NAD+MR in der Rolle MSB |
| **[118]** | Wenn in diesem STS DE1131 = E_0526 |
| **[119]** | Wenn in diesem STS DE1131 = E_0528 |
| **[120]** | Wenn in diesem STS DE1131 = E_0529 |
| **[121]** | Wenn in diesem STS DE1131 = E_0536 |
| **[129]** | Wenn STS+Z20+Z32+A99:E_0524 in dieser SG14 vorhanden |
| **[130]** | Wenn STS+Z20+Z32+A99:E_0531 in dieser SG14 vorhanden |
| **[131]** | Wenn STS+Z37+Z13+A04/A05/A06:E_1003 in dieser SG14 vorhanden |
| **[132]** | Wenn STS+Z37+Z32+A01: E_1002 in dieser SG14 vorhanden |
| **[133]** | Wenn in diesem STS DE1131 = E_1003 |
| **[134]** | Wenn in diesem STS DE1131 = E_1002 |
| **[135]** | Wenn in dieser SG15 in STS+Z21 DE9013 = A99 |
| **[136]** | Wenn STS+Z38+Z13+A02: E_1005 in dieser SG14 vorhanden |
| **[137]** | Wenn in diesem STS DE1131 = E_1005 |
| **[138]** | Wenn in diesem STS DE1131 = E_1020 |
| **[139]** | Wenn in diesem STS DE1131 = E_1020, dann ist nur der Code A01 möglich. |
| **[140]** | Wenn in diesem STS DE9013 &lt;&gt; A01 |
| **[141]** | Wenn in diesem STS DE9013 = A01 |
| **[142]** | Wenn in diesem STS DE1131 = E_0535 |
| **[143]** | Wenn mehr als ein Grund vorliegt und die voranstehenden DE9013 dieses STS nicht ausreichen |
| **[144]** | Wenn RFF+Z45 in dieser SG15 nicht vorhanden |
| **[145]** | Wenn RFF+Z17 in dieser SG15 nicht vorhanden |
| **[146]** | Wenn im DE3155 in demselben COM der Code EM vorhanden ist |
| **[147]** | Wenn im DE3155 in demselben COM der Code TE / FX / AJ / AL vorhanden ist |
| **[148]** | Wenn in dieser SG15 STS+Z43+Z48+A99:E_0595 vorhanden |
| **[149]** | Wenn in dieser SG14 STS DE1131 &lt;&gt; E_0278 |
| **[150]** | Wenn in dieser SG14 STS DE1131 &lt;&gt; E_0281 |
| **[151]** | Wenn STS+Z20+Z32+A99:E_0278 in dieser SG14 vorhanden |
| **[152]** | Wenn STS+Z20+Z32+A99:E_0281 in dieser SG14 vorhanden |
| **[153]** | Wenn in diesem STS DE1131 = E_0286 |
| **[154]** | Wenn STS+Z15+Z13+A99: E_0286 in dieser SG14 vorhanden |
| **[490]** | wenn Wert in diesem DE, an der Stelle CCYYMMDDHHMM ein Zeitpunkt aus dem angegeben Zeitraum der Tabelle Kapitel 3.5 „Übersicht gesetzliche deutsche Sommerzeit (MESZ)“ der Spalten: „Sommerzeit (MESZ) von“ Darstellung in UTC und „Sommerzeit (MESZ) bis“ Darstellung in UTC ist. |
| **[491]** | wenn Wert in diesem DE, an der Stelle CCYYMMDDHHMM ein Zeitpunkt aus dem angegeben Zeitraum der Tabelle Kapitel 3.6 „Übersicht gesetzliche deutsche Zeit (MEZ)“ der Spalten: „Winterzeit (MEZ) von“ Darstellung in UTC und „Winterzeit (MEZ) bis“ Darstellung in UTC ist. |
| **[492]** | wenn MP-ID in NAD+MR aus Sparte Strom |
| **[493]** | wenn MP-ID in NAD+MR aus Sparte Gas |
| **[494]** | Das hier genannte Datum muss der Zeitpunkt sein, zu dem das Dokument erstellt wurde, oder ein Zeitpunkt, der davor liegt |
| **[495]** | Der Zeitpunkt muss ≤ dem Wert im DE2380 des DTM+137 sein |
| **[496]** | Der Zeitpunkt muss &gt; dem Wert im DE2380 des DTM+137 sein |
| **[501]** | Hinweis: Aus QUOTES BGM DE1004 |
| **[502]** | Hinweis: Aus REQOTE BGM DE1004 |
| **[503]** | Hinweis: Auf Selbsteinbau eines iMS oder einer mME wird verzichtet |
| **[504]** | Hinweis: Verwendung der ID des MaBiS-ZP |
| **[505]** | Hinweis: Verwendung der ID der Messlokation |
| **[506]** | Hinweis: Verwendung der ID der Marktlokation |
| **[510]** | Hinweis: Es ist neben der Information über die Ablehnung auch der unverändert gebliebene Datenstatus informell mitzugeben. |
| **[512]** | Hinweis: Aus MSCONS BGM DE1004 |
| **[519]** | Hinweis: Aus ORDERS BGM DE1004 |
| **[520]** | Hinweis: Zeitpunkt, zu dem der Wechsel erfolgt, falls er zustande kommt |
| **[521]** | Hinweis: Zeitpunkt, ab dem der MSBN tatsächlich den Messstellenbetrieb übernimmt |
| **[522]** | Hinweis: Zeitpunkt, ab dem der gMSB den Messstellenbetrieb übernimmt |
| **[523]** | Hinweis: Wert aus BGM DE1004 der MSCONS, auf die sich die Statusangabe bezieht |
| **[524]** | Hinweis: Wert aus BGM DE1004 der MSCONS, die den Gegenvorschlag enthält |
| **[525]** | Hinweis: Je SG14 sind nur Statusinformationen zu einer MSCONS enthalten |
| **[530]** | Hinweis: Hier ist die Arbeit bzw. Leistung anzugeben, die der Sender der IFTSTA im Lieferschein für den von ihm genannten Zeitraum / Leistungsperiode erwartet hätte. |
| **[531]** | Vom MSBN in Schritt 1 des SD verwendete Vorgangsnummer, damit der LF diese bei der Bestellung einer Konfiguration beim MSBN, unter dem Vorbehalt, dass der MSB-Wechsel an der Messlokation erfolgreich sein wird, verwenden kann. |
| **[532]** | Hinweis: Verwendung der ID der Netzlokation |
| **[533]** | Hinweis: Verwendung der ID der Steuerbaren Ressource |
| **[534]** | Hinweis: Es darf nur eine Information im DE3148 übermittelt werden |
| **[535]** | Hinweis: Aus UTILMD IDE DE7402 |
| **[537]** | Hinweis: Der Code ist nötig, da dieser Anwendungsfall auch in allen Use- Cases zur Anwendung kommt, in denen sich die in diesem Segment zu übertragende Information nicht anhand eines Entscheidungsbaus ergibt. |
| **[902]** | Format: Wert darf nur positiv oder 0 sein |
| **[903]** | Format: Möglicher Wert: 1 |
| **[906]** | Format: max. 3 Nachkommastellen |
| **[911]** | Format: Mögliche Werte: 1 bis n, je Nachricht bei 1 beginnend und fortlaufend aufsteigend |
| **[931]** | Format: ZZZ = +00 |
| **[932]** | Format: HHMM = 2200 |
| **[933]** | Format: HHMM = 2300 |
| **[934]** | Format: HHMM = 0400 |
| **[935]** | Format: HHMM = 0500 |
| **[939]** | Format: Die Zeichenkette muss die Zeichen @ und . enthalten |
| **[940]** | Format: Die Zeichenkette muss mit dem Zeichen + beginnen und danach dürfen nur noch Ziffern folgen |
| **[950]** | Format: Marktlokations-ID |
| **[951]** | Format: Zählpunktbezeichnu ng |
| **[960]** | Format: Netzlokations- ID |
| **[961]** | Format: SR-ID |

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

Diese Seite führt den Klartext jeder Bedingung, auf die das Anwendungshandbuch des Nachrichtentyps **IFTSTA** in dieser Formatversion verweist. Eine Zeile des Handbuchs schreibt `Muss [704]`; was [704] verlangt, steht hier.

Die Liste gilt **für den Nachrichtentyp**, nicht für einen einzelnen Prüfidentifikator. Das ist keine Vereinfachung, sondern die Form der Quelle: die Bedingungsliste liegt in jeder Handbuchdatei des Formats identisch vor.

:::caution{title="Warum hier keine Zuordnung zu einzelnen Prüfidentifikatoren steht"}

Das Zwischenformat, aus dem diese Dokumentation die Handbuchzeilen liest, ordnet Bedingungen einer **Spalte** zu — und diese Zuordnung ist gegen das Original verschoben. Gemessen am 05.09.2026 an UTILMD Strom: das Handbuch führt `STS DE9013` als `X [360]` (nur Zustimmungscodes) beim Prüfidentifikator **55017** und `X [359]` (nur Ablehnungscodes) bei **55018**; das Zwischenformat setzt `[360]` auf 55016 und `[359]` auf 55017 **und** 55018. Dasselbe bei `FTX Muss [83]`: im Handbuch bei 55018, im Zwischenformat bei 55017.

Unabhängig bestätigt durch die Änderungslisten der Quelle: die Änderungs-IDs 25242, 25821, 25822, 25445 und 25243 verorten [83], [351] und [352] ausdrücklich beim „Anwendungsfall 55018 Ablehnung Kündigung“. Kein Eintrag ordnet sie 55016 oder 55017 zu.

Deshalb steht hier der **Text** jeder Bedingung und nirgends die Behauptung, welche Bedingung für welchen Prüfidentifikator gilt. Wer das braucht, schlägt im Original-Anwendungshandbuch nach.

:::

:::note{title="9 Bedingungen stehen nicht in jeder Handbuchdatei"}

Die Bedingungsliste ist formatweit gemeint, ist es aber nicht überall: die folgenden Marken kommen in weniger als allen 35 Dateien dieses Formats vor. Sie stehen trotzdem hier — eine Bedingung wegzulassen, weil eine Datei sie nicht führt, hieße einen Verweis wieder ins Leere zeigen zu lassen.

[490], [491], [932], [933], [934], [935], [UB1], [UB2], [UB3]

:::

Gemessen am 05.09.2026 verweist **keine** `ahb_expression` dieser Quelle auf eine Paketmarke — die Bedingungspakete stehen auf dieser Seite, weil die Quelle sie führt, nicht weil eine Handbuchzeile auf sie zeigt.

</Hinweisbereich>
