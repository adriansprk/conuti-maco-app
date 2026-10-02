# Bedingungen ORDCHG
<span hidden data-pagefind-meta={"title:Bedingungen ORDCHG — Anwendungshandbuch (FV 202604)"} />

EDIFACT-Nachrichtentyp **ORDCHG** · Formatversion **202604** · 12 Bedingungen · 1 Pakete · 0 UB-Bedingungen · aus 3 Handbuchdatei(en)

## Bedingungen

<div className="maco-tabellenrahmen">

| Marke | Bedingung |
|---|---|
| **[2]** | Wenn BGM+Z51 (Sperrung) vorhanden |
| **[3]** | Wenn BGM+Z52 (Entsperrung) vorhanden |
| **[4]** | wenn im DE3155 in demselben COM der Code EM vorhanden ist |
| **[5]** | wenn im DE3155 in demselben COM der Code TE / FX / AJ / AL vorhanden ist |
| **[494]** | Das hier genannte Datum muss der Zeitpunkt sein, zu dem das Dokument erstellt wurde, oder ein Zeitpunkt, der davor liegt. |
| **[500]** | Hinweis: Dokumentennummer aus BGM DE1004 der ORDERS |
| **[501]** | Hinweis: Wert aus BGM+Z33 DE1004 der IFTSTA mit der die Information über den Entsperrauftrag übermittelt wurde |
| **[502]** | Hinweis: Vorgangsnummer aus CNI DE1490 der IFTSTA mit BGM+Z33 mit der die Information über den Entsperrauftrag übermittelt wurde |
| **[503]** | Hinweis: Es darf nur eine Information im DE3148 übermittelt werden |
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

Diese Seite führt den Klartext jeder Bedingung, auf die das Anwendungshandbuch des Nachrichtentyps **ORDCHG** in dieser Formatversion verweist. Eine Zeile des Handbuchs schreibt `Muss [704]`; was [704] verlangt, steht hier.

Die Liste gilt **für den Nachrichtentyp**, nicht für einen einzelnen Prüfidentifikator. Das ist keine Vereinfachung, sondern die Form der Quelle: die Bedingungsliste liegt in jeder Handbuchdatei des Formats identisch vor.

:::caution{title="Warum hier keine Zuordnung zu einzelnen Prüfidentifikatoren steht"}

Das Zwischenformat, aus dem diese Dokumentation die Handbuchzeilen liest, ordnet Bedingungen einer **Spalte** zu — und diese Zuordnung ist gegen das Original verschoben. Gemessen am 05.09.2026 an UTILMD Strom: das Handbuch führt `STS DE9013` als `X [360]` (nur Zustimmungscodes) beim Prüfidentifikator **55017** und `X [359]` (nur Ablehnungscodes) bei **55018**; das Zwischenformat setzt `[360]` auf 55016 und `[359]` auf 55017 **und** 55018. Dasselbe bei `FTX Muss [83]`: im Handbuch bei 55018, im Zwischenformat bei 55017.

Unabhängig bestätigt durch die Änderungslisten der Quelle: die Änderungs-IDs 25242, 25821, 25822, 25445 und 25243 verorten [83], [351] und [352] ausdrücklich beim „Anwendungsfall 55018 Ablehnung Kündigung“. Kein Eintrag ordnet sie 55016 oder 55017 zu.

Deshalb steht hier der **Text** jeder Bedingung und nirgends die Behauptung, welche Bedingung für welchen Prüfidentifikator gilt. Wer das braucht, schlägt im Original-Anwendungshandbuch nach.

:::

:::caution{title="1 Bedingungen werden verwiesen, ohne dass die Quelle ihren Text führt"}

Diese Marken stehen in mindestens einer Handbuchzeile dieses Nachrichtentyps, aber in keiner der drei Listen der Quelle. Der Verweis zeigt also ins Leere, und das steht hier, statt die Marke stillschweigend wegzulassen — eine weggelassene Lücke sieht aus wie keine.

[1]

Gemessen am 05.09.2026, nach dem positionstreuen Neuexport der Quelle. Über beide Fassungen und alle Nachrichtentypen sind es 22 Marken, alle in der Fassung 202604.

:::

Gemessen am 05.09.2026 verweist **keine** `ahb_expression` dieser Quelle auf eine Paketmarke — die Bedingungspakete stehen auf dieser Seite, weil die Quelle sie führt, nicht weil eine Handbuchzeile auf sie zeigt.

</Hinweisbereich>
