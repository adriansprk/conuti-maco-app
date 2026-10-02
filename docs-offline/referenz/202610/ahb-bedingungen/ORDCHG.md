# Bedingungen ORDCHG
<span hidden data-pagefind-meta={"title:Bedingungen ORDCHG — Anwendungshandbuch (FV 202610)"} />

EDIFACT-Nachrichtentyp **ORDCHG** · Formatversion **202610** · 8 Bedingungen · 0 Pakete · 0 UB-Bedingungen · aus 3 Handbuchdatei(en)

## Bedingungen

<div className="maco-tabellenrahmen">

| Marke | Bedingung |
|---|---|
| **[1]** | MP-ID nur aus Sparte Strom |
| **[2]** | Wenn BGM+Z51 (Sperrung) vorhanden |
| **[3]** | Wenn BGM+Z52 (Entsperrung) vorhanden |
| **[494]** | Das hier genannte Datum muss der Zeitpunkt sein, zu dem das Dokument erstellt wurde, oder ein Zeitpunkt, der davor liegt. |
| **[500]** | Hinweis: Dokumentennummer aus BGM DE1004 der ORDERS |
| **[501]** | Hinweis: Wert aus BGM+Z33 DE1004 der IFTSTA mit der die Information über den Entsperrauftrag übermittelt wurde |
| **[502]** | Hinweis: Vorgangsnummer aus CNI DE1490 der IFTSTA mit BGM+Z33 mit der die Information über den Entsperrauftrag übermittelt wurde |
| **[931]** | Format: ZZZ = +00 |

</div>

<Hinweisbereich>

Diese Seite führt den Klartext jeder Bedingung, auf die das Anwendungshandbuch des Nachrichtentyps **ORDCHG** in dieser Formatversion verweist. Eine Zeile des Handbuchs schreibt `Muss [704]`; was [704] verlangt, steht hier.

Die Liste gilt **für den Nachrichtentyp**, nicht für einen einzelnen Prüfidentifikator. Das ist keine Vereinfachung, sondern die Form der Quelle: die Bedingungsliste liegt in jeder Handbuchdatei des Formats identisch vor.

:::caution{title="Warum hier keine Zuordnung zu einzelnen Prüfidentifikatoren steht"}

Das Zwischenformat, aus dem diese Dokumentation die Handbuchzeilen liest, ordnet Bedingungen einer **Spalte** zu — und diese Zuordnung ist gegen das Original verschoben. Gemessen am 05.09.2026 an UTILMD Strom: das Handbuch führt `STS DE9013` als `X [360]` (nur Zustimmungscodes) beim Prüfidentifikator **55017** und `X [359]` (nur Ablehnungscodes) bei **55018**; das Zwischenformat setzt `[360]` auf 55016 und `[359]` auf 55017 **und** 55018. Dasselbe bei `FTX Muss [83]`: im Handbuch bei 55018, im Zwischenformat bei 55017.

Unabhängig bestätigt durch die Änderungslisten der Quelle: die Änderungs-IDs 25242, 25821, 25822, 25445 und 25243 verorten [83], [351] und [352] ausdrücklich beim „Anwendungsfall 55018 Ablehnung Kündigung“. Kein Eintrag ordnet sie 55016 oder 55017 zu.

Deshalb steht hier der **Text** jeder Bedingung und nirgends die Behauptung, welche Bedingung für welchen Prüfidentifikator gilt. Wer das braucht, schlägt im Original-Anwendungshandbuch nach.

:::

</Hinweisbereich>
