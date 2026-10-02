# Bedingungen COMDIS
<span hidden data-pagefind-meta={"title:Bedingungen COMDIS — Anwendungshandbuch (FV 202604)"} />

EDIFACT-Nachrichtentyp **COMDIS** · Formatversion **202604** · 45 Bedingungen · 1 Pakete · 0 UB-Bedingungen · aus 2 Handbuchdatei(en)

## Bedingungen

<div className="maco-tabellenrahmen">

| Marke | Bedingung |
|---|---|
| **[1]** | wenn SG3 AJT+Z61+S_0109 oder SG3 AJT+Z62+S_0109 vorhanden |
| **[2]** | wenn SG3 AJT+Z58+S_0109 oder SG3 AJT+Z59+S_0109 oder SG3 AJT+Z60+S_0109 vorhanden |
| **[3]** | Nur MP-ID aus Sparte Strom |
| **[4]** | wenn SG3 AJT+Z58/Z59/Z60/Z61/Z62+S_0109 vorhanden |
| **[5]** | wenn SG3 AJT+A01/A02/A03/A04/A06/A07/A09/A12/A15+E_0504 vorhanden |
| **[6]** | wenn SG3 AJT+A07+E_0504 vorhanden |
| **[7]** | wenn SG3 AJT+A02+E_0504 vorhanden |
| **[8]** | wenn SG3 AJT+A01/A04/A06/A09/A12+E_0504 vorhanden |
| **[9]** | wenn SG3 AJT+A05/A10/A11/A14+E_0504 vorhanden |
| **[10]** | wenn SG3 AJT+A03+E_0504 vorhanden |
| **[11]** | wenn SG3 AJT+A15+E_0504 vorhanden |
| **[12]** | wenn SG3 AJT+A99+S_0109 vorhanden |
| **[13]** | wenn SG3 AJT+A07+E_1008 vorhanden |
| **[14]** | wenn SG3 AJT+A02+E_1008 vorhanden |
| **[15]** | wenn SG3 AJT+A01/A04/A06/A09+E_1008 vorhanden |
| **[16]** | wenn SG3 AJT+A03+E_1008 vorhanden |
| **[17]** | wenn SG3 AJT+A15+E_1008 vorhanden |
| **[18]** | wenn SG3 AJT+A05/A10/A11+E_1008 vorhanden |
| **[19]** | wenn SG3 AJT+A99+E_0265/E_0271/E_0274/E_0516/E_0520/E_0567 vorhanden |
| **[20]** | wenn SG3 AJT+A01/A02/A03/A04/A06/A07/A09/A15+E_1008 vorhanden |
| **[21]** | wenn im DE3155 in demselben COM der Code EM vorhanden ist |
| **[22]** | wenn im DE3155 in demselben COM der Code TE / FX / AJ / AL vorhanden ist |
| **[23]** | Wenn MP-ID in NAD+MS (Nachrichtensender) mit Rolle MSB vorhanden |
| **[24]** | Wenn MP-ID in NAD+MR (Nachrichtenempfänger) mit Rolle ESA vorhanden |
| **[25]** | Wenn MP-ID in NAD+MR (Nachrichtenempfänger) mit Rolle LF vorhanden |
| **[26]** | Wenn MP-ID in NAD+MR (Nachrichtenempfänger) mit Rolle NB vorhanden |
| **[27]** | Wenn MP-ID in NAD+MS (Nachrichtensender) mit Rolle NB vorhanden |
| **[28]** | Angabe der Datenaustauschreferenz aus der CONTRL |
| **[29]** | Angabe der Datenaustauschreferenz aus der APERAK |
| **[30]** | Angabe der Nachrichtennummer aus der APERAK |
| **[31]** | wenn SG3 AJT+Z61+G_0089 oder SG3 AJT+Z62+G_0089 vorhanden |
| **[32]** | wenn SG3 AJT+Z58+G_0089 oder SG3 AJT+Z59+G_0089 oder SG3 AJT+Z60+G_0089 vorhanden |
| **[33]** | wenn SG3 AJT+Z58/Z59/Z60/Z61/Z62+G_0089 vorhanden |
| **[34]** | wenn SG3 AJT+A99+G_0089 vorhanden |
| **[492]** | Wenn MP-ID in NAD+MR (Nachrichtenempfänger) aus Sparte Strom |
| **[493]** | Wenn MP-ID in NAD+MR (Nachrichtenempfänger) aus Sparte Gas |
| **[505]** | Hinweis: BGM DE1004 aus der vorher per REMADV abgelehnten INVOIC-Nachricht |
| **[506]** | Hinweis: BGM DE1004 aus der vorher per IFTSTA abgelehnten MSCONS- Nachricht |
| **[508]** | Hinweis: Es darf nur eine Information im DE3148 übermittelt werden |
| **[509]** | Hinweis: Wenn Eingang der zugrundeliegenden Nachricht vor dem 06.06.2025, 00:00 Uhr bestätigt wurde |
| **[510]** | Hinweis: Wenn Eingang der zugrundeliegenden Nachricht nach dem 06.06.2025, 00:00 Uhr bestätigt wurde |
| **[930]** | Format: max. 2 Nachkommastellen |
| **[931]** | Format: ZZZ = +00 |
| **[939]** | Format: Die Zeichenkette muss die Zeichen @ und . enthalten |
| **[940]** | Format: Die Zeichenkette muss mit dem Zeichen + beginnen und danach dürfen nur noch Ziffern folgen |

</div>

## Bedingungspakete

Bedingungspakete bündeln Voraussetzungen.

<div className="maco-tabellenrahmen">

| Paket | Voraussetzungen | Bedingungen |
|---|---|---|
| **[1P]** | -- | Hinweis: Das ist das Standardpaket, wenn keine Bedingung zum Tragen kommt, z. B. im COM-Segment. |

</div>

<Hinweisbereich>

Diese Seite führt den Klartext jeder Bedingung, auf die das Anwendungshandbuch des Nachrichtentyps **COMDIS** in dieser Formatversion verweist. Eine Zeile des Handbuchs schreibt `Muss [704]`; was [704] verlangt, steht hier.

Die Liste gilt **für den Nachrichtentyp**, nicht für einen einzelnen Prüfidentifikator. Das ist keine Vereinfachung, sondern die Form der Quelle: die Bedingungsliste liegt in jeder Handbuchdatei des Formats identisch vor.

:::caution{title="Warum hier keine Zuordnung zu einzelnen Prüfidentifikatoren steht"}

Das Zwischenformat, aus dem diese Dokumentation die Handbuchzeilen liest, ordnet Bedingungen einer **Spalte** zu — und diese Zuordnung ist gegen das Original verschoben. Gemessen am 05.09.2026 an UTILMD Strom: das Handbuch führt `STS DE9013` als `X [360]` (nur Zustimmungscodes) beim Prüfidentifikator **55017** und `X [359]` (nur Ablehnungscodes) bei **55018**; das Zwischenformat setzt `[360]` auf 55016 und `[359]` auf 55017 **und** 55018. Dasselbe bei `FTX Muss [83]`: im Handbuch bei 55018, im Zwischenformat bei 55017.

Unabhängig bestätigt durch die Änderungslisten der Quelle: die Änderungs-IDs 25242, 25821, 25822, 25445 und 25243 verorten [83], [351] und [352] ausdrücklich beim „Anwendungsfall 55018 Ablehnung Kündigung“. Kein Eintrag ordnet sie 55016 oder 55017 zu.

Deshalb steht hier der **Text** jeder Bedingung und nirgends die Behauptung, welche Bedingung für welchen Prüfidentifikator gilt. Wer das braucht, schlägt im Original-Anwendungshandbuch nach.

:::

Gemessen am 05.09.2026 verweist **keine** `ahb_expression` dieser Quelle auf eine Paketmarke — die Bedingungspakete stehen auf dieser Seite, weil die Quelle sie führt, nicht weil eine Handbuchzeile auf sie zeigt.

</Hinweisbereich>
