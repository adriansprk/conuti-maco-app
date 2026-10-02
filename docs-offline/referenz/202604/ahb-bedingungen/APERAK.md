# Bedingungen APERAK
<span hidden data-pagefind-meta={"title:Bedingungen APERAK — Anwendungshandbuch (FV 202604)"} />

EDIFACT-Nachrichtentyp **APERAK** · Formatversion **202604** · 23 Bedingungen · 1 Pakete · 0 UB-Bedingungen · aus 2 Handbuchdatei(en)

## Bedingungen

<div className="maco-tabellenrahmen">

| Marke | Bedingung |
|---|---|
| **[1]** | Wenn SG3 CTA+IC vorhanden. |
| **[2]** | Wenn fehlerhafter Inhalt vorhanden. |
| **[3]** | Wenn für weitere Fehlerangabe benötigt. |
| **[4]** | Wenn in dieser SG4, RFF+TN nicht vorhanden. |
| **[5]** | Wenn SG4 ERC+Z29 vorhanden. |
| **[6]** | Wenn Fehler innerhalb der Vorgangsebene von IFTSTA, INSRPT, UTILMD oder UTILTS vorhanden. |
| **[7]** | Wenn SG4 ERC+Z21 vorhanden. |
| **[8]** | Wenn SG4 ERC+Z16 vorhanden. |
| **[9]** | Wenn SG4 ERC+Z35 vorhanden. |
| **[10]** | Wenn SG4 ERC+Z38 vorhanden. |
| **[11]** | Wenn SG4 ERC+Z39 vorhanden. |
| **[12]** | Wenn SG4 ERC+Z41 vorhanden. |
| **[13]** | Wenn SG4 ERC+Z40 vorhanden. |
| **[14]** | Wenn im DE3155 in demselben COM der Code EM vorhanden ist |
| **[15]** | Wenn im DE3155 in demselben COM der Code TE / FX / AJ / AL vorhanden ist |
| **[16]** | Wenn der referenzierte Nachrichtentyp IFTSTA, INSRPT, UTILMD oder UTILTS ist. |
| **[494]** | Das hier genannte Datum muss der Zeitpunkt sein, zu dem das Dokument erstellt wurde, oder ein Zeitpunkt, der davor liegt |
| **[500]** | Hinweis: Für Folgeprozesse. |
| **[501]** | Hinweis: Für Initialprozesse. |
| **[502]** | Hinweis: Es darf nur eine Information im DE3148 übermittelt werden |
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

Diese Seite führt den Klartext jeder Bedingung, auf die das Anwendungshandbuch des Nachrichtentyps **APERAK** in dieser Formatversion verweist. Eine Zeile des Handbuchs schreibt `Muss [704]`; was [704] verlangt, steht hier.

Die Liste gilt **für den Nachrichtentyp**, nicht für einen einzelnen Prüfidentifikator. Das ist keine Vereinfachung, sondern die Form der Quelle: die Bedingungsliste liegt in jeder Handbuchdatei des Formats identisch vor.

:::caution{title="Warum hier keine Zuordnung zu einzelnen Prüfidentifikatoren steht"}

Das Zwischenformat, aus dem diese Dokumentation die Handbuchzeilen liest, ordnet Bedingungen einer **Spalte** zu — und diese Zuordnung ist gegen das Original verschoben. Gemessen am 05.09.2026 an UTILMD Strom: das Handbuch führt `STS DE9013` als `X [360]` (nur Zustimmungscodes) beim Prüfidentifikator **55017** und `X [359]` (nur Ablehnungscodes) bei **55018**; das Zwischenformat setzt `[360]` auf 55016 und `[359]` auf 55017 **und** 55018. Dasselbe bei `FTX Muss [83]`: im Handbuch bei 55018, im Zwischenformat bei 55017.

Unabhängig bestätigt durch die Änderungslisten der Quelle: die Änderungs-IDs 25242, 25821, 25822, 25445 und 25243 verorten [83], [351] und [352] ausdrücklich beim „Anwendungsfall 55018 Ablehnung Kündigung“. Kein Eintrag ordnet sie 55016 oder 55017 zu.

Deshalb steht hier der **Text** jeder Bedingung und nirgends die Behauptung, welche Bedingung für welchen Prüfidentifikator gilt. Wer das braucht, schlägt im Original-Anwendungshandbuch nach.

:::

Gemessen am 05.09.2026 verweist **keine** `ahb_expression` dieser Quelle auf eine Paketmarke — die Bedingungspakete stehen auf dieser Seite, weil die Quelle sie führt, nicht weil eine Handbuchzeile auf sie zeigt.

</Hinweisbereich>
