# Bedingungen PRICAT
<span hidden data-pagefind-meta={"title:Bedingungen PRICAT — Anwendungshandbuch (FV 202604)"} />

EDIFACT-Nachrichtentyp **PRICAT** · Formatversion **202604** · 96 Bedingungen · 1 Pakete · 1 UB-Bedingungen · aus 3 Handbuchdatei(en)

## Bedingungen

<div className="maco-tabellenrahmen">

| Marke | Bedingung |
|---|---|
| **[1]** | Wenn Vorgängerversion vorhanden |
| **[2]** | Wenn in dieser SG36 LIN in DE7140 9990001000813 vorhanden |
| **[3]** | Wenn IMD+X vorhanden |
| **[4]** | Wenn SG36 IMD+C in diesem IMD vorhanden |
| **[5]** | Wenn SG36 IMD+X in diesem IMD vorhanden |
| **[6]** | Wenn in dieser SG36 LIN in DE7140 9990001000798 vorhanden |
| **[7]** | Wenn in dieser SG36 LIN in DE7140 9990001000798 nicht vorhanden |
| **[8]** | Wenn das in DE1001 angegebene Preisblatt vom NB nicht genutzt wird. |
| **[9]** | Wenn BGM DE1373 =11 nicht vorhanden |
| **[10]** | Wenn eine weitere SG36 vorhanden ist, bei der sich der Inhalt von LIN DE7140 von LIN DE7140 dieser SG36 nur in der Ziffer nach dem letzten "-" unterscheidet und die Ziffer dort größer ist als in dieser SG36 (also eine Artikel-ID zur selben Gruppenartikel-ID vorhanden ist) |
| **[12]** | je UNB ist nur eine Nachricht mit BGM+Z04 in der Übertragungsdatei erlaubt (nur eine Nachricht je Übertragungsdatei) |
| **[14]** | je UNB ist maximal je Code aus DE1001 eine Nachricht in der Übertragungsdatei erlaubt |
| **[19]** | Nur MP-ID aus Sparte Strom |
| **[22]** | Wenn die Artikel-ID aus dieser SG36 LIN DE7140 in der EDI@Energy Codeliste der Artikelnummern und Artikel-ID in der Spalte "PRICAT Preisangabe" ein X hat |
| **[24]** | Wenn in dieser SG36 Wert von LIN DE7140 im Format n1-n2-n1-n8-n2-n1 |
| **[26]** | Wenn BGM DE1001 = Z70 vorhanden |
| **[27]** | Wenn BGM DE1001 = Z70 nicht vorhanden |
| **[28]** | Wenn die zugehörige Artikel-ID in der letzten Stelle eine 1 ist |
| **[29]** | Wenn die zugehörige Artikel-ID in der letzten Stelle &gt; 1 ist |
| **[30]** | wenn MP-ID in SG2 NAD+MR in der Rolle LF |
| **[31]** | wenn BGM DE1001 = Z32 (Preisblatt Messstellenbetrieb) |
| **[32]** | wenn der Zeitpunkt im DTM+157 DE2380 &lt; 01.01.2024 00:00 Uhr gesetzlicher deutscher Zeit |
| **[33]** | wenn der Zeitpunkt im DTM+157 DE2380 ≥ 01.01.2024 00:00 Uhr gesetzlicher deutscher Zeit |
| **[34]** | wenn BGM DE1001 = Z77 (Preisblatt Konfigurationen) |
| **[35]** | Wenn das in DE1001 angegebene Preisblatt vom MSB nicht genutzt wird. |
| **[36]** | Wenn MP-ID in SG2 NAD+MR in der Rolle NB |
| **[37]** | Wenn im DE3155 in demselben COM der Code EM vorhanden ist |
| **[38]** | Wenn im DE3155 in demselben COM der Code TE / FX / AJ / AL vorhanden ist |
| **[39]** | Es sind nur Werte aus der EDI@Energy Codeliste der Artikelnummern und Artikel-ID erlaubt, die in der Spalte MaBiS ein X haben |
| **[40]** | Es sind nur Werte aus der EDI@Energy Codeliste der Artikelnummern und Artikel-ID erlaubt, die in der Spalte H ein X haben |
| **[41]** | Es sind nur Werte aus der EDI@Energy Codeliste der Artikelnummern und Artikel-ID erlaubt, die in der Spalte "PRICAT Codeverwendung" ein X haben |
| **[42]** | Es sind nur Werte erlaubt, die die Bildungsvorschrift der EDI@Energy Codeliste der Artikelnummern und Artikel-ID erfüllen, und die in der Spalte "PRICAT Codeverwendung" ein X haben |
| **[43]** | Wenn BGM DE1001 = Z32 und LIN DE7140 im Format n1-n2-n1-n3, dann muss der hier genannte Zeitpunkt ≥ 01.01.2024 00:00 Uhr gesetzlicher deutscher Zeit sein |
| **[44]** | Wenn BGM DE1001 = Z77, dann muss der hier genannte Zeitpunkt ≥ 01.10.2023 00:00 Uhr gesetzlicher deutscher Zeit sein |
| **[45]** | Es sind nur Werte aus der EDI@Energy Codeliste der Artikelnummern und Artikel-ID erlaubt, die in dieser in Kapitel "Abrechnung Messstellenbetrieb für die Sparte Strom" für die jeweilige Marktrolle genannt sind |
| **[46]** | Es sind nur Werte aus der EDI@Energy Codeliste der Artikelnummern und Artikel-ID erlaubt, die in dieser in Kapitel "Artikel-ID für die Bestellprozesse beim MSB" genannt sind |
| **[47]** | Wenn BGM DE1001 = Z32 und LIN DE7140 im Format n13, dann muss der hier genannte Zeitpunkt &lt; 01.01.2024 00:00 Uhr gesetzlicher deutscher Zeit sein |
| **[48]** | Wenn in dieser SG36 LIN in DE7140 einer der Codes 1-01-6-005 / 1-01-9-001 / 1-01-9-002 / 1-02-0-015 / 1-03-8-001 / 1-03-8-002 / 1-03-8-003 / 1-03-8-004 / 1-03-9-001 / 1-03-9-002 / 1-03-9-003 / 1-03-9-004 / 1-07-4-001 vorhanden |
| **[49]** | Wenn in dieser SG36 LIN in DE7140 keiner der Codes 1-01-6-005 / 1-01-9-001 / 1-01-9-002 / 1-02-0-015 / 1-03-8-001 / 1-03-8-002 / 1-03-8-003 / 1-03-8-004 / 1-03-9-001 / 1-03-9-002 / 1-03-9-003 / 1-03-9-004 / 1-07-4-001 vorhanden |
| **[50]** | Wenn MP-ID aus RFF+Z56 mit MP-ID aus NAD+MS identisch ist |
| **[51]** | Wenn BGM+Z54 vorhanden |
| **[52]** | Wenn BGM+Z54 nicht vorhanden |
| **[53]** | Diese SG40 darf genau einmal in der SG36 angegeben werden |
| **[54]** | Falls der Preis des Artikels gezont ist |
| **[55]** | Wenn in dieser SG36 ein weiteres RNG (d. h. eine weitere Zone) vorhanden ist, in der der Wert des DE6162 (Wertebereichsgrenze, untere) größer ist als der Wert des DE6162 in diesem RNG |
| **[56]** | Wenn BGM DE1001 = Z94, dann muss der hier genannte Zeitpunkt ≥ 01.10.2025 00:00 Uhr gesetzlicher deutscher Zeit sein |
| **[57]** | wenn BGM DE1001 = Z94 (Preisblatt Technik) |
| **[60]** | Wenn in dieser SG36 der Teil vor dem "-" aus LIN DE7140 aus der Tabelle des Kapitels "Produkte zur Bestellung einer Änderung an einer Lokation in der Sparte Strom" der EDI@Energy Codeliste der Konfigurationen |
| **[61]** | Wenn in dieser SG36 der Wert der Zahl nach dem "-" aus LIN DE7140 &gt; 01 |
| **[62]** | Wenn IMD+F vorhanden |
| **[63]** | Wenn vorheriges DE7008 zur Beschreibung der Leistung dieser Artikel-ID nicht ausreicht |
| **[64]** | Wenn der Zeitpunkt im DTM+157 DE2380 ≥ 01.01.2026, 00:00 Uhr gesetzlicher deutscher Zeit |
| **[65]** | wenn in dieser SG36 der Teil des Codes in LIN DE7140 nach dem "-" von "01" abweicht |
| **[66]** | wenn im DE7140 des LIN dieser SG36 der Teil des Codes nach dem "-" den Wert 02 hat, muss dieses DE = 0 sein und in allen anderen RNG zu Artikel-ID, bei denen der Teil des Codes vor dem "-" mit dem DE7140 des LIN dieser SG36 übereinstimmt, muss der Wert dieses DE mit dem Wert des DE6152 eines anderen RNG zu einer Artikel-ID bei dem der Teil des Codes vor dem "-" mit dem DE7140 des LIN dieser SG36 übereinstimmt, identisch sein |
| **[67]** | wenn in dieser SG17 ein weiteres LIN vorhanden ist, in dem der Teil des Codes vor dem "-" des DE7140 mit dem des DE7140 des LIN dieser SG36 identisch ist und in dem der Wert nach dem "-" um eins größer ist, als der Wert nach dem "-" im DE7140 des LIN dieser SG36 |
| **[68]** | Der Teil des Codes vor dem "-" muss ein Messprodukt-Code sein |
| **[69]** | Der Teil des Codes vor dem "-" muss ein Konfigurationsprodukt-Code sein |
| **[70]** | Der Teil des Codes vor dem "-" muss ein Produkt-Code sein |
| **[71]** | Es muss der Code 9991000003030-01 sein |
| **[72]** | Wenn in dieser SG36 die letzte Ziffer von LIN DE7140 &gt;1 ist, dann muss es eine SG36 geben dessen Inhalt von LIN DE7140 sich von dem in dieser SG36 nur in der letzten Ziffer unterscheidet und in der der Wert von RNG DE6152 mit dem Wert dieses DE6162 übereinstimmt |
| **[490]** | wenn Wert in diesem DE, an der Stelle CCYYMMDDHHMM ein Zeitpunkt aus dem angegeben Zeitraum der Tabelle Kapitel 3.5 „Übersicht gesetzliche deutsche Sommerzeit (MESZ)“ der Spalten: „Sommerzeit (MESZ) von“ Darstellung in UTC und „Sommerzeit (MESZ) bis“ Darstellung in UTC ist. |
| **[491]** | wenn Wert in diesem DE, an der Stelle CCYYMMDDHHMM ein Zeitpunkt aus dem angegeben Zeitraum der Tabelle Kapitel 3.6 „Übersicht gesetzliche deutsche Zeit (MEZ)“ der Spalten: „Winterzeit (MEZ) von“ Darstellung in UTC und „Winterzeit (MEZ) bis“ Darstellung in UTC ist. |
| **[492]** | wenn MP-ID in NAD+MR aus Sparte Strom |
| **[494]** | Das hier genannte Datum muss der Zeitpunkt sein, zu dem das Dokument erstellt wurde, oder ein Zeitpunkt, der davor liegt |
| **[495]** | Der Zeitpunkt muss ≤ dem Wert im DE2380 des DTM+137 sein |
| **[502]** | Hinweis: Preis in Euro je MWh |
| **[503]** | Hinweis: Hier ist immer der Wert 1000 einzutragen, da in DE5118 der Preis in €/MWh angegeben wird. |
| **[504]** | Hinweis: Dokumentennummer der PRICAT |
| **[511]** | Hinweis: 1. Der genannte Wert gehört nicht zum Intervall. 2. Die untere Wertegrenze zu der Artikel-ID, deren Zahl an der letzten Stelle den Wert n hat, muss kleiner sein, als die untere Wertegrenze zu der Artikel-ID, deren Zahl an der letzten Stelle den Wert n+1 hat. |
| **[512]** | Hinweis: Der genannte Wert gehört zum Intervall |
| **[513]** | Hinweis: Die zum Preis gehörende Einheit ist in der Codeliste definiert |
| **[519]** | Hinweis: Es darf nur eine Information im DE3148 übermittelt werden |
| **[520]** | Hinweis: Falls der Preis des Artikels gezont ist, ist diese SG40 so oft zu wiederholen, bis alle Preise zu diesem Artikel genannt sind |
| **[521]** | Hinweis: Je Artikel-ID muss in einem RNG der Wert dieses DE = 0 sein und in allen anderen RNG zu dieser Artikel-ID muss der Wert dieses DE mit dem Wert des DE6152 eines anderen RNG zu dieser Artikel-ID identisch sein |
| **[522]** | Hinweis: Hier ist die Leistung zu beschreiben, die mit dieser Artikel-ID in Rechnung gestellt wird, wobei darauf zu achten ist, dass zu erkennen ist, wie sich diese von den Leistungen unterscheiden, bei denen die ersten 13 Stellen der Artikel-ID mit den ersten 13 Stellen dieser Artikel-ID identisch sind |
| **[902]** | Format: Möglicher Wert: ≥ 0 |
| **[908]** | Format: Mögliche Werte: 1 bis n |
| **[909]** | Format: Mögliche Werte: 0 bis n |
| **[911]** | Format: Mögliche Werte: 1 bis n, je Nachricht oder Segmentgruppe bei 1 beginnend und fortlaufend aufsteigend |
| **[912]** | Format: max. 6 Nachkommastellen |
| **[926]** | Format: Möglicher Wert: 0 |
| **[929]** | Format: Möglicher Wert: 1000 |
| **[931]** | Format: ZZZ = +00 |
| **[932]** | Format: HHMM = 2200 |
| **[933]** | Format: HHMM = 2300 |
| **[937]** | Format: keine Nachkommastelle |
| **[939]** | Format: Die Zeichenkette muss die Zeichen @ und . enthalten |
| **[940]** | Format: Die Zeichenkette muss mit dem Zeichen + beginnen und danach dürfen nur noch Ziffern folgen |
| **[941]** | Format: Artikelnummer |
| **[942]** | Format: n1-n2-n1-n3 |
| **[946]** | Format: max. 11 Nachkommastellen |
| **[948]** | Format: n1-n2-n1-n8-n2 |
| **[949]** | Format: n1-n2-n1-n8-n2-n1 |
| **[957]** | Format: n1-n2-n1-n8 |
| **[959]** | Format: n13-n2 |
| **[968]** | Format: Möglicher Wert: ≤ 0 |

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

</div>

<Hinweisbereich>

Diese Seite führt den Klartext jeder Bedingung, auf die das Anwendungshandbuch des Nachrichtentyps **PRICAT** in dieser Formatversion verweist. Eine Zeile des Handbuchs schreibt `Muss [704]`; was [704] verlangt, steht hier.

Die Liste gilt **für den Nachrichtentyp**, nicht für einen einzelnen Prüfidentifikator. Das ist keine Vereinfachung, sondern die Form der Quelle: die Bedingungsliste liegt in jeder Handbuchdatei des Formats identisch vor.

:::caution{title="Warum hier keine Zuordnung zu einzelnen Prüfidentifikatoren steht"}

Das Zwischenformat, aus dem diese Dokumentation die Handbuchzeilen liest, ordnet Bedingungen einer **Spalte** zu — und diese Zuordnung ist gegen das Original verschoben. Gemessen am 05.09.2026 an UTILMD Strom: das Handbuch führt `STS DE9013` als `X [360]` (nur Zustimmungscodes) beim Prüfidentifikator **55017** und `X [359]` (nur Ablehnungscodes) bei **55018**; das Zwischenformat setzt `[360]` auf 55016 und `[359]` auf 55017 **und** 55018. Dasselbe bei `FTX Muss [83]`: im Handbuch bei 55018, im Zwischenformat bei 55017.

Unabhängig bestätigt durch die Änderungslisten der Quelle: die Änderungs-IDs 25242, 25821, 25822, 25445 und 25243 verorten [83], [351] und [352] ausdrücklich beim „Anwendungsfall 55018 Ablehnung Kündigung“. Kein Eintrag ordnet sie 55016 oder 55017 zu.

Deshalb steht hier der **Text** jeder Bedingung und nirgends die Behauptung, welche Bedingung für welchen Prüfidentifikator gilt. Wer das braucht, schlägt im Original-Anwendungshandbuch nach.

:::

:::note{title="5 Bedingungen stehen nicht in jeder Handbuchdatei"}

Die Bedingungsliste ist formatweit gemeint, ist es aber nicht überall: die folgenden Marken kommen in weniger als allen 3 Dateien dieses Formats vor. Sie stehen trotzdem hier — eine Bedingung wegzulassen, weil eine Datei sie nicht führt, hieße einen Verweis wieder ins Leere zeigen zu lassen.

[490], [491], [932], [933], [UB1]

:::

Gemessen am 05.09.2026 verweist **keine** `ahb_expression` dieser Quelle auf eine Paketmarke — die Bedingungspakete stehen auf dieser Seite, weil die Quelle sie führt, nicht weil eine Handbuchzeile auf sie zeigt.

</Hinweisbereich>
