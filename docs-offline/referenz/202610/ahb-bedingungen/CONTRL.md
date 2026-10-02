# Bedingungen CONTRL
<span hidden data-pagefind-meta={"title:Bedingungen CONTRL — Anwendungshandbuch (FV 202610)"} />

EDIFACT-Nachrichtentyp **CONTRL** · Formatversion **202610** · 7 Bedingungen · 0 Pakete · 0 UB-Bedingungen · aus 2 Handbuchdatei(en)

## Bedingungen

<div className="maco-tabellenrahmen">

| Marke | Bedingung |
|---|---|
| **[1]** | Wenn Angabe möglich. |
| **[2]** | Wenn Syntaxfehler in UNH vorhanden. |
| **[3]** | Wenn Syntaxfehler in UNT vorhanden. |
| **[5]** | Wenn Fehler auf Segment(gruppen)ebene vorhanden. |
| **[6]** | Wenn Fehler auf Datenelement-, Gruppendatenelement- oder Datengruppenebene vorhanden. |
| **[8]** | Wenn SG1 UCM DE0013 vorhanden. |
| **[9]** | Wenn SG1 UCM DE0013 nicht vorhanden. |

</div>

<Hinweisbereich>

Diese Seite führt den Klartext jeder Bedingung, auf die das Anwendungshandbuch des Nachrichtentyps **CONTRL** in dieser Formatversion verweist. Eine Zeile des Handbuchs schreibt `Muss [704]`; was [704] verlangt, steht hier.

Die Liste gilt **für den Nachrichtentyp**, nicht für einen einzelnen Prüfidentifikator. Das ist keine Vereinfachung, sondern die Form der Quelle: die Bedingungsliste liegt in jeder Handbuchdatei des Formats identisch vor.

:::caution{title="Warum hier keine Zuordnung zu einzelnen Prüfidentifikatoren steht"}

Das Zwischenformat, aus dem diese Dokumentation die Handbuchzeilen liest, ordnet Bedingungen einer **Spalte** zu — und diese Zuordnung ist gegen das Original verschoben. Gemessen am 05.09.2026 an UTILMD Strom: das Handbuch führt `STS DE9013` als `X [360]` (nur Zustimmungscodes) beim Prüfidentifikator **55017** und `X [359]` (nur Ablehnungscodes) bei **55018**; das Zwischenformat setzt `[360]` auf 55016 und `[359]` auf 55017 **und** 55018. Dasselbe bei `FTX Muss [83]`: im Handbuch bei 55018, im Zwischenformat bei 55017.

Unabhängig bestätigt durch die Änderungslisten der Quelle: die Änderungs-IDs 25242, 25821, 25822, 25445 und 25243 verorten [83], [351] und [352] ausdrücklich beim „Anwendungsfall 55018 Ablehnung Kündigung“. Kein Eintrag ordnet sie 55016 oder 55017 zu.

Deshalb steht hier der **Text** jeder Bedingung und nirgends die Behauptung, welche Bedingung für welchen Prüfidentifikator gilt. Wer das braucht, schlägt im Original-Anwendungshandbuch nach.

:::

</Hinweisbereich>
