# Bedingungen PARTIN
<span hidden data-pagefind-meta={"title:Bedingungen PARTIN — Anwendungshandbuch (FV 202604)"} />

EDIFACT-Nachrichtentyp **PARTIN** · Formatversion **202604** · 60 Bedingungen · 4 Pakete · 1 UB-Bedingungen · aus 14 Handbuchdatei(en)

## Bedingungen

<div className="maco-tabellenrahmen">

| Marke | Bedingung |
|---|---|
| **[1]** | Nur MP-ID aus Sparte Strom |
| **[2]** | Wenn der Code im DE3207 in der "EDI@Energy Codeliste der europäischen Ländercodes" in der Spalte "PLZ vorhanden" ein "X" enthält |
| **[3]** | wenn vorhanden |
| **[4]** | Wenn Vorgängerversion vorhanden |
| **[5]** | Wenn MP-ID in SG2 NAD+MR (Nachrichtenempfänger) in der Rolle LF |
| **[6]** | wenn im DE3155 im demselben COM der Code EM vorhanden ist |
| **[7]** | wenn im DE3155 im demselben COM der Code TE / FX / AJ / AL vorhanden ist |
| **[8]** | wenn im DE3155 im demselben COM der Code TE / FX vorhanden ist |
| **[9]** | Wenn die Kommunikationsdaten vom Absender nicht mehr aktiv sind. |
| **[10]** | Wenn BGM DE1373 = 11 (Dokument nicht verfügbar) nicht vorhanden |
| **[11]** | Wenn SG4 NAD+SU (Lieferant) DE3207 mit Code „DE“ vorhanden |
| **[12]** | Wenn SG4 NAD+DDM (Netzbetreiber) DE3207 mit Code „DE“ vorhanden |
| **[13]** | Wenn SG4 NAD+DEB (Messstellenbetreiber) DE3207 mit Code „DE“ vorhanden |
| **[14]** | Wenn SG4 NAD+SU (Lieferant) DE3207 der Code „DE“ nicht vorhanden ist |
| **[15]** | Wenn SG4 NAD+DDM (Netzbetreiber) DE3207 der Code „DE“ nicht vorhanden ist |
| **[16]** | Wenn SG4 NAD+DEB (Messstellenbetreiber) DE3207 der Code „DE“ nicht vorhanden ist |
| **[17]** | Wenn MP-ID in SG2 NAD+MR (Nachrichtenempfänger) in der Rolle LF/NB/MSB |
| **[18]** | Wenn MP-ID in SG2 NAD+MR (Nachrichtenempfänger) in der Rolle LF/MSB |
| **[19]** | Wenn MP-ID in SG2 NAD+MR (Nachrichtenempfänger) in der Rolle LF/MSB/NB/ÜNB |
| **[20]** | Wenn MP-ID in SG2 NAD+MR (Nachrichtenempfänger) in der Rolle LF/MSB/ÜNB |
| **[21]** | Wenn MP-ID in SG2 NAD+MR (Nachrichtenempfänger) in der Rolle LF/NB/ESA |
| **[22]** | Wenn MP-ID in SG2 NAD+MR (Nachrichtenempfänger) in der Rolle MSB |
| **[23]** | Wenn MP-ID in SG2 NAD+MR (Nachrichtenempfänger) in der Rolle NB/ÜNB |
| **[24]** | Wenn MP-ID in SG2 NAD+MR (Nachrichtenempfänger) in der Rolle NB/LF/MSB/ESA |
| **[25]** | Wenn MP-ID in SG2 NAD+MR (Nachrichtenempfänger) in der Rolle NB |
| **[26]** | Wenn MP-ID in SG2 NAD+MR (Nachrichtenempfänger) in der Rolle NB/LF/BKV/BIKO |
| **[27]** | Wenn SG4 NAD+Z31 (Übertragungsnetzbetreiber) DE3207 mit Code „DE“ vorhanden |
| **[28]** | Wenn SG4 NAD+Z34 (Bilanzkoordinator) DE3207 mit Code „DE“ vorhanden |
| **[29]** | Wenn SG4 NAD+Z35 (Bilanzkreisverantwortlicher) DE3207 mit Code „DE“ vorhanden |
| **[30]** | Wenn SG4 NAD+Z36 (Energieserviceanbieter) DE3207 mit Code „DE“ vorhanden |
| **[31]** | Wenn SG4 NAD+Z31 (Übertragungsnetzbetreiber) DE3207 mit Code „DE“ nicht vorhanden |
| **[32]** | Wenn SG4 NAD+Z34 (Bilanzkoordinator) DE3207 mit Code „DE“ nicht vorhanden |
| **[33]** | Wenn SG4 NAD+Z35 (Bilanzkreisverantwortlicher) DE3207 mit Code „DE“ nicht vorhanden |
| **[34]** | Wenn SG4 NAD+Z36 (Energieserviceanbieter) DE3207 mit Code „DE“ nicht vorhanden |
| **[35]** | Wenn MP-ID in SG2 NAD+MR (Nachrichtenempfänger) in der Rolle ÜNB |
| **[36]** | Wenn MP-ID in SG2 NAD+MR (Nachrichtenempfänger) in der Rolle BKV |
| **[41]** | Nur MP-ID aus Sparte Gas |
| **[43]** | Wenn SG4 NAD+Z71 (Marktgebietsverantwortlicher) DE3207 mit Code „DE“ vorhanden |
| **[44]** | Wenn SG4 NAD+Z71 (Marktgebietsverantwortlicher) DE3207 mit Code „DE“ nicht vorhanden |
| **[45]** | Wenn MP-ID in SG2 NAD+MR (Nachrichtenempfänger) in der Rolle LF/NB |
| **[46]** | Wenn MP-ID in SG2 NAD+MR (Nachrichtenempfänger) in der Rolle LF/MSB/MGV |
| **[49]** | Wenn MP-ID in SG2 NAD+MR (Nachrichtenempfänger) in der Rolle LF/MGV |
| **[50]** | Wenn MP-ID in SG2 NAD+MR (Nachrichtenempfänger) in der Rolle LF/MGV/NB |
| **[490]** | wenn Wert in diesem DE, an der Stelle CCYYMMDDHHMM ein Zeitpunkt aus dem angegeben Zeitraum der Tabelle Kapitel 3.5 „Übersicht gesetzliche deutsche Sommerzeit (MESZ)“ der Spalten: „Sommerzeit (MESZ) von“ Darstellung in UTC und „Sommerzeit (MESZ) bis“ Darstellung in UTC ist. |
| **[491]** | wenn Wert in diesem DE, an der Stelle CCYYMMDDHHMM ein Zeitpunkt aus dem angegeben Zeitraum der Tabelle Kapitel 3.6 „Übersicht gesetzliche deutsche Zeit (MEZ)“ der Spalten: „Winterzeit (MEZ) von“ Darstellung in UTC und „Winterzeit (MEZ) bis“ Darstellung in UTC ist. |
| **[494]** | Das hier genannte Datum muss der Zeitpunkt sein, zu dem das Dokument erstellt wurde, oder ein Zeitpunkt, der davor liegt. |
| **[500]** | Hinweis: Es kann der Firmenname eines Dienstleisters oder die identische Firmenbezeichnung aus SG4 NAD+SU / DDM / DEB / Z31 / Z34 / Z35 / Z36 / Z71 eingetragen werden. |
| **[501]** | Hinweis: Es darf kein Name einer natürlichen Person übermittelt werden, stattdessen ist die organisatorische Einheit im Unternehmen zu nennen. |
| **[502]** | Hinweis: Es darf nur eine Information im DE3148 übermittelt werden |
| **[503]** | Hinweis: Angabe erfolgt in gesetzlicher deutscher Zeit |
| **[504]** | Hinweis: Es ist mindestens die Umsatzsteuer- bzw. Steuernummer zu nennen, die in der INVOIC genutzt wird. |
| **[505]** | Wenn eine Vorgängerversion (RFF+ACW) angegeben ist, so muss der Wert in diesem DE1056 mindestens um 1 höher sein, als der Wert aus DE1056 der Vorgängerversion (RFF+ACW). |
| **[506]** | Hinweis: Das Datenelement ist so zu füllen, dass sein Inhalt den Vorgaben des USt.-Gesetzes genügt, so dass der Empfänger diese Daten in einer INVOIC nutzen kann. |
| **[508]** | Hinweis: Der LF in seiner Funktion als Grund- und Ersatzversorger muss den NB, in deren Netzgebiet der LF als Grund- und Ersatzversorger ist, einen Bilanzkreis für verbrauchende Marktlokationen übermitteln, um dem NB die Möglichkeit zu geben, eine Zuordnung bei fehlender Antwort auf die EoG Anmeldung durchführen zu können. |
| **[908]** | Format: Mögliche Werte: 1 bis n |
| **[931]** | Format: ZZZ = +00 |
| **[932]** | Format: HHMM = 2200 |
| **[933]** | Format: HHMM = 2300 |
| **[939]** | Format: Die Zeichenkette muss die Zeichen @ und . enthalten |
| **[940]** | Format: Die Zeichenkette muss mit dem Zeichen + beginnen und danach dürfen nur noch Ziffern folgen |

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
| **[2P]** | [11]   ⊻  [12]  ⊻  [13]   ⊻  [ 27 ]   ⊻  [ 28 ]   ⊻  [ 29 ]   ⊻  [ 30 ]   ⊻  [ 43 ] | [11]  Wenn SG4  NAD+SU (Lieferant) DE3207 mit Code „DE“ vorhanden [12]  Wenn SG4  NAD+DDM (Netzbetreiber) DE3207 mit Code „DE“ vorhanden [13]  Wenn SG4  NAD+DEB (Messstellenbetreiber) DE3207 mit Code „DE“ vorhanden [27]  Wenn SG4 NAD+Z31 (Übertragungsnetzbetreiber) DE3207 mit Code „DE“ vorhanden [28]  Wenn SG4 NAD+Z34 (Bilanzkoordinator) DE3207 mit Code „DE“ vorhanden [29]  Wenn SG4 NAD+Z35 (Bilanzkreisverantwortlicher) DE3207 mit Code „DE“ vorhanden [30]  Wenn SG4 NAD+Z36 (Energieserviceanbieter) DE3207 mit Code „DE“ vorhanden [43]  Wenn SG4 NAD+Z71 (Marktgebietsverantwortlicher) DE3207 mit Code „DE“ vorhanden |
| **[3P]** | [14]   ⊻  [1 5 ]  ⊻  [1 6 ]   ⊻  [ 31 ]   ⊻  [ 32 ]   ⊻  [ 33 ]   ⊻  [ 34 ]   ⊻  [ 44 ] | [14]  Wenn SG4  NAD+SU (Lieferant) DE3207 der Code „DE“ nicht vorhanden ist [15]  Wenn SG4  NAD+DDM (Netzbetreiber) DE3207 der Code „DE“ nicht vorhanden ist [16]  Wenn SG4  NAD+DEB (Messstellenbetreiber) DE3207 der Code „DE“ nicht vorhanden ist [31] Wenn SG4 NAD+Z31 (Übertragungsnetzbetreiber) DE3207 mit Code „DE“ nicht vorhanden [32]   Wenn SG4 NAD+Z34 (Bilanzkoordinator) DE3207 mit Code „DE“ nicht vorhanden [33]   Wenn SG4 NAD+Z35 (Bilanzkreisverantwortlicher) DE3207 mit Code „DE“ nicht vorhanden [34]   Wenn SG4 NAD+Z36 (Energieserviceanbieter) DE3207 mit Code „DE“ nicht vorhanden [44] Wenn SG4 NAD+Z71 (Marktgebietsverantwortlicher) DE3207 mit Code „DE“ nicht vorhanden |
| **[4P]** | [508] | [508] Hinweis: Der LF in seiner Funktion als Grund- und Ersatzversorger muss den NB, in deren Netzgebiet der LF als Grund- und Ersatzversorger ist, einen Bilanzkreis für verbrauchende Marktlokationen übermitteln, um dem NB die Möglichkeit zu geben, eine Zuordnung bei fehlender Antwort auf die EoG Anmeldung durchführen zu können. |

</div>

<Hinweisbereich>

Diese Seite führt den Klartext jeder Bedingung, auf die das Anwendungshandbuch des Nachrichtentyps **PARTIN** in dieser Formatversion verweist. Eine Zeile des Handbuchs schreibt `Muss [704]`; was [704] verlangt, steht hier.

Die Liste gilt **für den Nachrichtentyp**, nicht für einen einzelnen Prüfidentifikator. Das ist keine Vereinfachung, sondern die Form der Quelle: die Bedingungsliste liegt in jeder Handbuchdatei des Formats identisch vor.

:::caution{title="Warum hier keine Zuordnung zu einzelnen Prüfidentifikatoren steht"}

Das Zwischenformat, aus dem diese Dokumentation die Handbuchzeilen liest, ordnet Bedingungen einer **Spalte** zu — und diese Zuordnung ist gegen das Original verschoben. Gemessen am 05.09.2026 an UTILMD Strom: das Handbuch führt `STS DE9013` als `X [360]` (nur Zustimmungscodes) beim Prüfidentifikator **55017** und `X [359]` (nur Ablehnungscodes) bei **55018**; das Zwischenformat setzt `[360]` auf 55016 und `[359]` auf 55017 **und** 55018. Dasselbe bei `FTX Muss [83]`: im Handbuch bei 55018, im Zwischenformat bei 55017.

Unabhängig bestätigt durch die Änderungslisten der Quelle: die Änderungs-IDs 25242, 25821, 25822, 25445 und 25243 verorten [83], [351] und [352] ausdrücklich beim „Anwendungsfall 55018 Ablehnung Kündigung“. Kein Eintrag ordnet sie 55016 oder 55017 zu.

Deshalb steht hier der **Text** jeder Bedingung und nirgends die Behauptung, welche Bedingung für welchen Prüfidentifikator gilt. Wer das braucht, schlägt im Original-Anwendungshandbuch nach.

:::

Gemessen am 05.09.2026 verweist **keine** `ahb_expression` dieser Quelle auf eine Paketmarke — die Bedingungspakete stehen auf dieser Seite, weil die Quelle sie führt, nicht weil eine Handbuchzeile auf sie zeigt.

</Hinweisbereich>
