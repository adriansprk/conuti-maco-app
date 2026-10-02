# Bedingungen INSRPT
<span hidden data-pagefind-meta={"title:Bedingungen INSRPT — Anwendungshandbuch (FV 202610)"} />

EDIFACT-Nachrichtentyp **INSRPT** · Formatversion **202610** · 31 Bedingungen · 4 Pakete · 0 UB-Bedingungen · aus 8 Handbuchdatei(en)

## Bedingungen

<div className="maco-tabellenrahmen">

| Marke | Bedingung |
|---|---|
| **[1]** | Wenn Nachrichtenabsender vom Kunden informiert wurde. |
| **[2]** | Wenn SG7 STS+Z06+Z10+ZC1 vorhanden. |
| **[3]** | Wenn vorhanden. |
| **[4]** | Wenn MP-ID in SG2 NAD+MR in der Rolle NB |
| **[5]** | Wenn MP-ID in SG2 NAD+MR in der Rolle LF |
| **[6]** | Wenn keine Störung festgestellt werden konnte. |
| **[7]** | Wenn keine weitere SG7 mit demselben Meldepunkt und DTM+9 vorhanden |
| **[8]** | Wenn in dieser SG7 STS+Z06+Z10 vorhanden |
| **[9]** | Wenn eine Störung festgestellt wurde, die durch den MSB selbständig und unverschuldet nicht behoben werden konnte. |
| **[10]** | Wenn in diesem STS DE4405 = Z09 |
| **[11]** | Wenn in diesem STS DE4405 = Z10 |
| **[12]** | Wenn eine Störung festgestellt wurde, die durch den MSB behoben wurde. |
| **[13]** | Wenn DE2379 = 303 |
| **[14]** | Nur MP-ID aus Sparte Strom |
| **[494]** | Das hier genannte Datum muss der Zeitpunkt sein, zu dem das Dokument erstellt wurde, oder ein Zeitpunkt, der davor liegt |
| **[495]** | Der Zeitpunkt muss ≤ dem Wert im DE2380 des DTM+137 sein |
| **[500]** | Hinweis: Vorgangsnummer (DOC DE1004) aus Prozessschritt 4b „Bestätigung der Störungsmeldung“ (Gas) bzw. Prozessschritt 2 „Antwort“ (Strom). |
| **[506]** | Hinweis: Zu nutzen, wenn Behebung der Störung durch den MSB selbständig und unverschuldet nicht möglich ist. |
| **[507]** | Hinweis: In SG7 FTX+AAO ist anzugeben, was die übergeordnete Ursache ist, aufgrund derer der MSB nicht in der Lage ist die Störung zu beheben. |
| **[508]** | Hinweis: Vorgangsnummer aus DOC DE1004. |
| **[509]** | Hinweis: Verwendung der ID der Messlokation |
| **[510]** | Hinweis: Verwendung der ID der Marktlokation |
| **[511]** | Hinweis: Die Nummerierung beginnt in jedem Dokument bei 1 |
| **[512]** | Hinweis: Wurde eine Störung festgestellt und durch den MSB behoben, ist die Segmentgruppe mit demselben Meldepunkt zweimal anzugeben |
| **[513]** | Hinweis: Wurde keine Störung festgestellt, ist die Segmentgruppe genau einmal anzugeben |
| **[514]** | Hinweis: Wurde eine Störung festgestellt, die nicht durch den MSB behoben werden konnte, ist die Segmentgruppe genau einmal anzugeben |
| **[515]** | Hinweis: "≤ dem Wert im DE2380 des DTM+137" bedeutet, dass der dort genannte Tag ≥ dem in diesem DTM genannten Tag sein muss, wenn in DE2379 der Code 102 steht. |
| **[908]** | Format: Mögliche Werte: 1 bis n |
| **[931]** | Format: ZZZ = +00 |
| **[950]** | Format: Marktlokations-ID |
| **[951]** | Format: Zählpunktbezeichnung |

</div>

## Bedingungspakete

Bedingungspakete bündeln Voraussetzungen.

<div className="maco-tabellenrahmen">

| Paket | Voraussetzungen | Bedingungen |
|---|---|---|
| **[1P]** | -- | Hinweis: Das ist das Standardpaket, wenn keine Bedingung zum Tragen kommt, z. B. im COM-Segment. |
| **[2P]** | [6] | Wenn keine Störung festgestellt werden konnte . |
| **[3P]** | [12] | Wenn eine Störung festgestellt wurde, die durch den MSB behoben wurde . |
| **[4P]** | [9] | Wenn eine Störung festgestellt wurde, die durch den MSB selbständig und unverschuldet nicht behoben werden konnte . |

</div>

<Hinweisbereich>

Diese Seite führt den Klartext jeder Bedingung, auf die das Anwendungshandbuch des Nachrichtentyps **INSRPT** in dieser Formatversion verweist. Eine Zeile des Handbuchs schreibt `Muss [704]`; was [704] verlangt, steht hier.

Die Liste gilt **für den Nachrichtentyp**, nicht für einen einzelnen Prüfidentifikator. Das ist keine Vereinfachung, sondern die Form der Quelle: die Bedingungsliste liegt in jeder Handbuchdatei des Formats identisch vor.

:::caution{title="Warum hier keine Zuordnung zu einzelnen Prüfidentifikatoren steht"}

Das Zwischenformat, aus dem diese Dokumentation die Handbuchzeilen liest, ordnet Bedingungen einer **Spalte** zu — und diese Zuordnung ist gegen das Original verschoben. Gemessen am 05.09.2026 an UTILMD Strom: das Handbuch führt `STS DE9013` als `X [360]` (nur Zustimmungscodes) beim Prüfidentifikator **55017** und `X [359]` (nur Ablehnungscodes) bei **55018**; das Zwischenformat setzt `[360]` auf 55016 und `[359]` auf 55017 **und** 55018. Dasselbe bei `FTX Muss [83]`: im Handbuch bei 55018, im Zwischenformat bei 55017.

Unabhängig bestätigt durch die Änderungslisten der Quelle: die Änderungs-IDs 25242, 25821, 25822, 25445 und 25243 verorten [83], [351] und [352] ausdrücklich beim „Anwendungsfall 55018 Ablehnung Kündigung“. Kein Eintrag ordnet sie 55016 oder 55017 zu.

Deshalb steht hier der **Text** jeder Bedingung und nirgends die Behauptung, welche Bedingung für welchen Prüfidentifikator gilt. Wer das braucht, schlägt im Original-Anwendungshandbuch nach.

:::

Gemessen am 05.09.2026 verweist **keine** `ahb_expression` dieser Quelle auf eine Paketmarke — die Bedingungspakete stehen auf dieser Seite, weil die Quelle sie führt, nicht weil eine Handbuchzeile auf sie zeigt.

</Hinweisbereich>
