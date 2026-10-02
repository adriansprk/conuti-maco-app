# Bedingungen REQOTE
<span hidden data-pagefind-meta={"title:Bedingungen REQOTE — Anwendungshandbuch (FV 202604)"} />

EDIFACT-Nachrichtentyp **REQOTE** · Formatversion **202604** · 90 Bedingungen · 1 Pakete · 2 UB-Bedingungen · aus 5 Handbuchdatei(en)

## Bedingungen

<div className="maco-tabellenrahmen">

| Marke | Bedingung |
|---|---|
| **[1]** | Wenn DTM+203 (Ausführungsdatum) nicht vorhanden |
| **[2]** | Wenn DTM+469 (Beginn zum (nächstmöglichen Termin)) nicht vorhanden |
| **[10]** | MP-ID nur aus Sparte Strom |
| **[15]** | Wenn DTM+76 (Datum zum geplanten Leistungsbeginn) nicht vorhanden |
| **[16]** | Wenn SG1 RFF+Z41 (Referenznummer des Vorgangs der Anmeldung nach WiM) nicht vorhanden |
| **[17]** | Wenn SG1 RFF+Z41 (Referenznummer des Vorgangs der Anmeldung nach WiM) vorhanden |
| **[18]** | Wenn IMD++Z55 (Änderung Konfiguration) vorhanden |
| **[19]** | Wenn SG27 LIN++Z64 (Erforderliches Produkt Schaltzeitdefinitionen) vorhanden |
| **[20]** | Wenn SG27 LIN++Z65 (Erforderliches Produkt Leistungskurvendefinitionen) vorhanden |
| **[21]** | Wenn SG27 LIN++Z66 (Erforderliches Produkt Ad-hoc- Steuerkanal) vorhanden |
| **[22]** | Wenn SG27 LIN++Z67 (Erforderliches Messprodukt für Werte nach Typ 2 aus Backend) vorhanden |
| **[23]** | Wenn SG27 LIN++Z68 (Erforderliches Produkt Konfigurationserlaubnis für Werte nach Typ 2 aus SMGW) vorhanden |
| **[24]** | Wenn Produkt bestellt werden soll |
| **[25]** | Wenn in LOC+172 DE3225 (Meldepunkt) die ID einer Marktlokation angegeben ist. |
| **[26]** | Wenn in LOC+172 DE3225 (Meldepunkt) die ID einer Messlokation angegeben ist. |
| **[27]** | Wenn in LOC+172 DE3225 (Meldepunkt) die ID einer Netzlokation angegeben ist. |
| **[28]** | Wenn in LOC+172 DE3225 (Meldepunkt) die ID einer Steuerbaren Ressource angegeben ist. |
| **[29]** | Es sind nur die Konfigurations-Produkte erlaubt, die in der Codeliste der Konfigurationen im Kapitel 4.1 „Konfigurationsprodukte Schaltzeitdefinition“ enthalten sind. |
| **[30]** | Es sind nur die Konfigurations-Produkte erlaubt, die in der Codeliste der Konfigurationen im Kapitel 4.2 „Konfigurationsprodukte Leistungskurvendefinition“ enthalten sind. |
| **[31]** | Es sind nur die Konfigurations-Produkte erlaubt, die in der Codeliste der Konfigurationen im Kapitel 4.3 „Konfigurationsprodukte Ad- Hoc-Steuerkanal“ enthalten sind. |
| **[32]** | Es sind nur die Messprodukte erlaubt, die in der Codeliste der Konfigurationen im Kapitel 4.5 „Messprodukte für Werte nach Typ 2 aus Backend für LF und NB“ enthalten sind. |
| **[33]** | Es sind nur die Messprodukte erlaubt, die in der Codeliste der Konfigurationen im Kapitel 4.4 „Messprodukte mit Konfigurationserlaubnis für Werte nach Typ 2 aus SMGW“ enthalten sind. |
| **[35]** | Wenn MP-ID in SG11 NAD+MS mit Rolle LF vorhanden |
| **[36]** | Wenn MP-ID in SG11 NAD+MS mit Rolle NB vorhanden |
| **[37]** | Es sind nur die Messprodukt-Position-Codes erlaubt, die in der Codeliste der Konfigurationen im Kapitel 4.7 „Art der Werte für Messprodukte nach Typ 2“ enthalten sind. |
| **[38]** | Wenn innerhalb derselben SG27 LIN im PIA+5 DE7140 (Erforderliches Produkt Konfigurationserlaubnis für Werte nach Typ 2 aus SMGW) ein Produkt angegeben ist, das in der Codeliste der Konfigurationen im Kapitel 4.4 „Messprodukte mit Konfigurationserlaubnis für Werte nach Typ 2 aus SMGW“ in der Spalte "Auslöser" mit dem Wert "Bei Schwellwertunter- / - überschreitung" gekennzeichnet ist. |
| **[39]** | wenn im DE3155 in demselben COM der Code EM vorhanden ist |
| **[40]** | wenn im DE3155 in demselben COM der Code TE / FX / AJ / AL vorhanden ist |
| **[41]** | Es sind nur die Messprodukte erlaubt, die in der Codeliste der Konfigurationen im Kapitel 4.6.1 „Werte nach Typ 2 aus Backend“ enthalten sind. |
| **[42]** | Es sind nur die Messprodukte erlaubt, die in der Codeliste der Konfigurationen im Kapitel 4.6.2 „Werte nach Typ 2 aus SMGW“ enthalten sind. |
| **[43]** | Wenn innerhalb derselben SG27 LIN im PIA+5 DE7140 (Erforderliches Produkt Konfigurationserlaubnis für Werte nach Typ 2 aus SMGW) ein Produkt angegeben ist, das in der Codeliste der Konfigurationen im Kapitel 4.6.2 „Werte nach Typ 2 aus SMGW“ in der Spalte "Auslöser" mit dem Wert "Bei Schwellwertunter- / - überschreitung" gekennzeichnet ist. |
| **[44]** | Wenn in SG27 LIN (Erforderliches Produkt der Messlokation) das PIA+5 DE7140 mit einem Produkt-Code vorhanden ist der in der Codeliste der Konfigurationen im Kapitel 7 "Produkte zur Bestellung einer Änderung an einer Lokation" in der "Spalte Bezeichnung" mit dem Wert "weitere Energieflussrichtung" vorhanden ist. |
| **[45]** | Wenn in LOC+172 DE3225 (Meldepunkt) die ID einer Steuerbaren Ressource angegeben ist. |
| **[47]** | Es sind nur die Produkt-Codes erlaubt, die in der Codeliste der Konfigurationen im Kapitel 7 "Produkte zur Bestellung einer Änderung an einer Lokation" die in der Spalte "Ebene" mit dem Wert "Messlokation" vorhanden sind. |
| **[48]** | Es sind weiterhin nur die Produkt-Codes erlaubt, die in der Codeliste der Konfigurationen im Kapitel 7 "Produkte zur Bestellung einer Änderung an einer Lokation" die in der Spalte "Produkt gegenüber MSB von Marktrolle bestellbar" mit einem "X" in der Spalte "NB" gekennzeichnet ist. |
| **[49]** | Es sind weiterhin nur die Produkt-Codes erlaubt, die in der Codeliste der Konfigurationen im Kapitel 7 "Produkte zur Bestellung einer Änderung an einer Lokation" die in der Spalte "Produkt gegenüber MSB von Marktrolle bestellbar" mit einem "X" in der Spalte "LF" gekennzeichnet ist. |
| **[50]** | Es sind nur die Produkt-Codes erlaubt, die in der Codeliste der Konfigurationen im Kapitel 7 "Produkte zur Bestellung einer Änderung an einer Lokation" die in der Spalte "Ebene" mit dem Wert "Netzlokation" vorhanden sind. |
| **[51]** | Es sind nur die Produkt-Codes erlaubt, die in der Codeliste der Konfigurationen im Kapitel 7 "Produkte zur Bestellung einer Änderung an einer Lokation" die in der Spalte "Ebene" mit dem Wert "Steuerbare Ressource" vorhanden sind. |
| **[52]** | wenn im DE3155 in demselben COM der Code TE / AL vorhanden ist |
| **[53]** | wenn der LF der Marktlokation der genannten Lokation im gewünschten Umsetzungszeitraum nicht zugeordnet ist. |
| **[490]** | wenn Wert in diesem DE, an der Stelle CCYYMMDDHHMM ein Zeitpunkt aus dem angegeben Zeitraum der Tabelle Kapitel 3.5 „Übersicht gesetzliche deutsche Sommerzeit (MESZ)“ der Spalten: „Sommerzeit (MESZ) von“ Darstellung in UTC und „Sommerzeit (MESZ) bis“ Darstellung in UTC ist. |
| **[491]** | wenn Wert in diesem DE, an der Stelle CCYYMMDDHHMM ein Zeitpunkt aus dem angegeben Zeitraum der Tabelle Kapitel 3.6 „Übersicht gesetzliche deutsche Zeit (MEZ)“ der Spalten: „Winterzeit (MEZ) von“ Darstellung in UTC und „Winterzeit (MEZ) bis“ Darstellung in UTC ist. |
| **[492]** | wenn MP-ID in NAD+MR aus Sparte Strom |
| **[493]** | wenn MP-ID in NAD+MR aus Sparte Gas |
| **[494]** | Das hier genannte Datum muss der Zeitpunkt sein, zu dem das Dokument erstellt wurde, oder ein Zeitpunkt, der davor liegt. |
| **[500]** | Hinweis: Angabe eines technischen Ansprechpartners für die Geräteübernahme |
| **[501]** | Hinweis: Angabe eines Ansprechpartners für die Rechnungsabwicklung |
| **[502]** | Hinweis: Verwendung der ID der Marktlokation |
| **[503]** | Hinweis: Verwendung der ID der Messlokation |
| **[504]** | Hinweis: Verwendung der ID der Tranche |
| **[507]** | Hinweis: Vorgangsnummer aus SG4 IDE+24 DE7402 der UTILMD mit BGM+E01 mit der die Anmeldung des MSB-Wechsels erfolgt ist. |
| **[508]** | Hinweis: Wert aus BGM+Z73 DE1004 der IFTSTA mit der die Antwort auf die Bestellung der Konfiguration übermittelt wurde |
| **[509]** | Hinweis: Vorgangsnummer aus CNI DE1490 der IFTSTA mit BGM+Z73 mit der die Antwort auf die Bestellung der Konfiguration übermittelt wurde |
| **[510]** | Hinweis: Verwendung der ID der Netzlokation |
| **[511]** | Hinweis: Verwendung der ID der Steuerbaren Ressource |
| **[512]** | Hinweis: Für den Empfang der Werte nach Typ 2 aus dem SMGW. |
| **[514]** | Hinweis: Es darf nur eine Information im DE3148 übermittelt werden |
| **[515]** | Hinweis: Es ist eine URI IPv4 für die Bereitstellung der Werte anzugeben. |
| **[516]** | Hinweis: Es ist eine URI IPv6 für die Bereitstellung der Werte anzugeben. |
| **[517]** | Hinweis: Verwendung der ID der Technischen Ressource |
| **[518]** | Hinweis: zur Angabe von Kontaktdaten des Kunden des Lieferanten um die Änderung an der Technik zu vereinfachen. |
| **[520]** | Hinweis: Angabe des Beginnzeitpunkts des gewünschten Umsetzungstermins aus Sicht des Anfragenden. |
| **[521]** | Hinweis: Angabe des Endezeitpunkts des gewünschten Umsetzungstermins aus Sicht des Anfragenden. |
| **[903]** | Format: Möglicher Wert: 1 |
| **[906]** | Format: max. 3 Nachkommastellen |
| **[911]** | Format: Mögliche Werte: 1 bis n, je Nachricht oder Segmentgruppe bei 1 beginnend und fortlaufend aufsteigend |
| **[922]** | Format: TR-ID |
| **[931]** | Format: ZZZ = +00 |
| **[932]** | Format: HHMM = 2200 |
| **[933]** | Format: HHMM = 2300 |
| **[934]** | Format: HHMM = 0400 |
| **[935]** | Format: HHMM = 0500 |
| **[939]** | Format: Die Zeichenkette muss die Zeichen @ und . enthalten |
| **[940]** | Format: Die Zeichenkette muss mit dem Zeichen + beginnen und danach dürfen nur noch Ziffern folgen |
| **[950]** | Format: Marktlokations-ID |
| **[951]** | Format: Zählpunktbezeichnung |
| **[960]** | Format: Netzlokations-ID |
| **[961]** | Format: SR-ID |
| **[962]** | Format: max. 6 Vorkommastellen |
| **[967]** | Format: Zertifikatskörper gemäß X509.1, BSI TR-03109-4 |
| **[2005]** | Pro Nachricht ist die SG27 genau einmal anzugeben |
| **[2060]** | Pro Nachricht ist die SG27 LIN+Z64 (Erforderliches Produkt Schaltzeitdefinitionen) maximal einmal anzugeben |
| **[2061]** | Pro Nachricht ist die SG27 LIN++Z65 (Erforderliches Produkt Leistungskurvendefinitionen) maximal einmal anzugeben |
| **[2062]** | Pro Nachricht ist die SG27 LIN++Z66 (Erforderliches Produkt Ad-hoc-Steuerkanal) maximal einmal anzugeben |
| **[2063]** | Pro Nachricht ist die SG27 LIN++Z67 (Erforderliches Messprodukt für Werte nach Typ 2 aus Backend) maximal einmal anzugeben |
| **[2064]** | Pro Nachricht ist die SG27 LIN++Z68 (Erforderliches Produkt Konfigurationserlaubnis für Werte nach Typ 2 aus SMGW) maximal einmal anzugeben |
| **[2065]** | Diese SG28 ist so oft zu wiederholen, wie zu den unterschiedlichen Messprodukt- Position-Codes zu dem innerhalb derselben SG27 LIN im PIA+5 DE7140 (Erforderliches Produkt Konfigurationserlaubnis für Werte nach Typ 2 aus SMGW) angegebenen Produkt ein Produkt angegeben ist, das in der Codeliste der Konfigurationen im Kapitel 4.4 „Messprodukte mit Konfigurationserlaubnis für Werte nach Typ 2 aus SMGW“ in der Spalte "Auslöser" mit dem Wert "Bei Schwellwertunter- / - überschreitung" gekennzeichnet ist. |
| **[2066]** | Diese SG28 ist so oft zu wiederholen, wie zu den unterschiedlichen Messprodukt- Position-Codes zu dem innerhalb derselben SG27 LIN im PIA+5 DE7140 (Erforderliches Produkt Konfigurationserlaubnis für Werte nach Typ 2 aus SMGW) angegebenen Produkt ein Produkt angegeben ist, das in der Codeliste der Konfigurationen im Kapitel 4.6.2 „Werte nach Typ 2 aus SMGW“ in der Spalte "Auslöser" mit dem Wert "Bei Schwellwertunter- / - überschreitung" gekennzeichnet ist. |
| **[2067]** | Die SG12 RFF+Z37 Referenz auf ID der Technischen Ressource ist so oft zu wiederholen, bis alle IDs der Technischen Ressourcen angegeben sind, die der Steuerbaren Ressource in LOC+172 DE3225 (Meldepunkt) mit diesem Vorgang zugeordnet werden sollen, genannt sind. |
| **[2068]** | Diese SG27 ist so oft zu wiederholen, dass alle Produkte zur Lokation die innerhalb des gewünschten Umsetzungstermins (Zeitintervall aus DTM+469 (Startdatum oder Zeitpunkt) und DTM+472 (Endedatum oder Zeitpunkt)) aus Sicht des Anfragenden gewünscht sind und deren Kombination gemäß Codeliste der Konfigurationen Kapitel 7 "Produkte zur Bestellung einer Änderung an einer Lokation"möglich sind, genannt sind. |

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

</div>

<Hinweisbereich>

Diese Seite führt den Klartext jeder Bedingung, auf die das Anwendungshandbuch des Nachrichtentyps **REQOTE** in dieser Formatversion verweist. Eine Zeile des Handbuchs schreibt `Muss [704]`; was [704] verlangt, steht hier.

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
