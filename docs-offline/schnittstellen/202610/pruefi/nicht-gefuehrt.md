# Nicht geführte Prüfidentifikatoren (202610)

Das Anwendungshandbuch der Formatversion 202610 führt **484 Prüfidentifikatoren**. Die MACO APP implementiert **384** davon; nur deren Seiten tragen die vollständige Datenstruktur mit der Zuordnung zu den Geschäftsobjekten. Die übrigen **100** stehen unten, nach Nachrichtentyp gruppiert. **Jeder von ihnen hat eine eigene Seite aus dem Anwendungshandbuch** — Anwendungsfall, Prozesskontext und Feldliste mit Bedingungen, aber ohne Geschäftsobjekte. Die Nummern unten führen dorthin.

:::info{title="Eine Lücke, die ausgesprochen ist"}

Diese Seite ist die Antwort auf »warum zeigt diese Nummer weniger als ihre Nachbarn?«. Sie steht hier, damit die Antwort nicht Schweigen ist — nachgeprüft am 05.09.2026, erneut zu prüfen bis 05.12.2026.

:::

## Warum diese Seiten weniger zeigen

Nicht, weil der Prüfidentifikator entfallen wäre. Die vollständigen Seiten dieser Ebene entstehen aus den Spezifikationen der MACO APP, und die entstehen aus dem, was die Anwendung **implementiert** — je Prüfidentifikator eine Klasse im `maco-templater-app`. Aus ihnen stammt die Zuordnung zu den Geschäftsobjekten. Der Katalog des Anwendungshandbuchs ist die größere Menge; was hier steht, ist noch nicht implementiert.

Die Kette hat keine Zwischenstufe, an der etwas verloren ginge: aus den Klassen entstehen ebenso viele Spezifikationen und daraus ebenso viele Seiten — für 202610 gemessen 384 zu 384 zu 384.

Die Formatversion 202610 wird laufend ausgebaut, und diese Liste wird deshalb von allein kürzer. Zwischen dem Stand, aus dem die Spezifikationen hier stammen (`392a2eb2`, 26.08.2026), und dem Hauptzweig desselben Repos neun Tage später sind die Prüfi-Klassen von 346 auf 375 gewachsen. Wer eine Nummer hier vermisst, braucht keinen Fehler zu melden, sondern einen neueren Stand der Quellen.

Dieselbe Aufstellung für die andere Fassung: [202604](/schnittstellen/202604/pruefi/nicht-gefuehrt). Die Lücke ist keine Eigenheit dieser Formatversion — beide führen weniger Prüfidentifikatoren, als ihr Handbuch kennt.

## Nicht geführte Prüfidentifikatoren

**CONTRL** (2) — [77777](/schnittstellen/202610/pruefi/CONTRL/PI_77777), [88888](/schnittstellen/202610/pruefi/CONTRL/PI_88888)

**IFTSTA** (9) — [21000](/schnittstellen/202610/pruefi/IFTSTA/PI_21000), [21001](/schnittstellen/202610/pruefi/IFTSTA/PI_21001), [21002](/schnittstellen/202610/pruefi/IFTSTA/PI_21002), [21003](/schnittstellen/202610/pruefi/IFTSTA/PI_21003), [21004](/schnittstellen/202610/pruefi/IFTSTA/PI_21004), [21005](/schnittstellen/202610/pruefi/IFTSTA/PI_21005), [21037](/schnittstellen/202610/pruefi/IFTSTA/PI_21037), [21038](/schnittstellen/202610/pruefi/IFTSTA/PI_21038), [21042](/schnittstellen/202610/pruefi/IFTSTA/PI_21042)

**MSCONS** (9) — [13005](/schnittstellen/202610/pruefi/MSCONS/PI_13005), [13012](/schnittstellen/202610/pruefi/MSCONS/PI_13012), [13013](/schnittstellen/202610/pruefi/MSCONS/PI_13013), [13014](/schnittstellen/202610/pruefi/MSCONS/PI_13014), [13020](/schnittstellen/202610/pruefi/MSCONS/PI_13020), [13021](/schnittstellen/202610/pruefi/MSCONS/PI_13021), [13022](/schnittstellen/202610/pruefi/MSCONS/PI_13022), [13023](/schnittstellen/202610/pruefi/MSCONS/PI_13023), [13026](/schnittstellen/202610/pruefi/MSCONS/PI_13026)

**ORDCHG** (1) — [39002](/schnittstellen/202610/pruefi/ORDCHG/PI_39002)

**ORDERS** (12) — [17007](/schnittstellen/202610/pruefi/ORDERS/PI_17007), [17008](/schnittstellen/202610/pruefi/ORDERS/PI_17008), [17011](/schnittstellen/202610/pruefi/ORDERS/PI_17011), [17110](/schnittstellen/202610/pruefi/ORDERS/PI_17110), [17205](/schnittstellen/202610/pruefi/ORDERS/PI_17205), [17206](/schnittstellen/202610/pruefi/ORDERS/PI_17206), [17207](/schnittstellen/202610/pruefi/ORDERS/PI_17207), [17208](/schnittstellen/202610/pruefi/ORDERS/PI_17208), [17209](/schnittstellen/202610/pruefi/ORDERS/PI_17209), [17210](/schnittstellen/202610/pruefi/ORDERS/PI_17210), [17211](/schnittstellen/202610/pruefi/ORDERS/PI_17211), [17301](/schnittstellen/202610/pruefi/ORDERS/PI_17301)

**ORDRSP** (7) — [19110](/schnittstellen/202610/pruefi/ORDRSP/PI_19110), [19120](/schnittstellen/202610/pruefi/ORDRSP/PI_19120), [19127](/schnittstellen/202610/pruefi/ORDRSP/PI_19127), [19130](/schnittstellen/202610/pruefi/ORDRSP/PI_19130), [19131](/schnittstellen/202610/pruefi/ORDRSP/PI_19131), [19132](/schnittstellen/202610/pruefi/ORDRSP/PI_19132), [19204](/schnittstellen/202610/pruefi/ORDRSP/PI_19204)

**PARTIN** (5) — [37003](/schnittstellen/202610/pruefi/PARTIN/PI_37003), [37004](/schnittstellen/202610/pruefi/PARTIN/PI_37004), [37005](/schnittstellen/202610/pruefi/PARTIN/PI_37005), [37006](/schnittstellen/202610/pruefi/PARTIN/PI_37006), [37011](/schnittstellen/202610/pruefi/PARTIN/PI_37011)

**PRICAT** (1) — [27001](/schnittstellen/202610/pruefi/PRICAT/PI_27001)

**QUOTES** (1) — [15002](/schnittstellen/202610/pruefi/QUOTES/PI_15002)

**REQOTE** (2) — [35003](/schnittstellen/202610/pruefi/REQOTE/PI_35003), [35005](/schnittstellen/202610/pruefi/REQOTE/PI_35005)

**UTILMD** (48) — [55062](/schnittstellen/202610/pruefi/UTILMD/PI_55062), [55063](/schnittstellen/202610/pruefi/UTILMD/PI_55063), [55064](/schnittstellen/202610/pruefi/UTILMD/PI_55064), [55065](/schnittstellen/202610/pruefi/UTILMD/PI_55065), [55066](/schnittstellen/202610/pruefi/UTILMD/PI_55066), [55067](/schnittstellen/202610/pruefi/UTILMD/PI_55067), [55069](/schnittstellen/202610/pruefi/UTILMD/PI_55069), [55070](/schnittstellen/202610/pruefi/UTILMD/PI_55070), [55071](/schnittstellen/202610/pruefi/UTILMD/PI_55071), [55072](/schnittstellen/202610/pruefi/UTILMD/PI_55072), [55073](/schnittstellen/202610/pruefi/UTILMD/PI_55073), [55076](/schnittstellen/202610/pruefi/UTILMD/PI_55076), [55195](/schnittstellen/202610/pruefi/UTILMD/PI_55195), [55196](/schnittstellen/202610/pruefi/UTILMD/PI_55196), [55197](/schnittstellen/202610/pruefi/UTILMD/PI_55197), [55198](/schnittstellen/202610/pruefi/UTILMD/PI_55198), [55199](/schnittstellen/202610/pruefi/UTILMD/PI_55199), [55200](/schnittstellen/202610/pruefi/UTILMD/PI_55200), [55201](/schnittstellen/202610/pruefi/UTILMD/PI_55201), [55202](/schnittstellen/202610/pruefi/UTILMD/PI_55202), [55203](/schnittstellen/202610/pruefi/UTILMD/PI_55203), [55204](/schnittstellen/202610/pruefi/UTILMD/PI_55204), [55205](/schnittstellen/202610/pruefi/UTILMD/PI_55205), [55206](/schnittstellen/202610/pruefi/UTILMD/PI_55206), [55207](/schnittstellen/202610/pruefi/UTILMD/PI_55207), [55208](/schnittstellen/202610/pruefi/UTILMD/PI_55208), [55209](/schnittstellen/202610/pruefi/UTILMD/PI_55209), [55210](/schnittstellen/202610/pruefi/UTILMD/PI_55210), [55211](/schnittstellen/202610/pruefi/UTILMD/PI_55211), [55212](/schnittstellen/202610/pruefi/UTILMD/PI_55212), [55213](/schnittstellen/202610/pruefi/UTILMD/PI_55213), [55214](/schnittstellen/202610/pruefi/UTILMD/PI_55214), [55223](/schnittstellen/202610/pruefi/UTILMD/PI_55223), [55224](/schnittstellen/202610/pruefi/UTILMD/PI_55224), [55235](/schnittstellen/202610/pruefi/UTILMD/PI_55235), [55236](/schnittstellen/202610/pruefi/UTILMD/PI_55236), [55237](/schnittstellen/202610/pruefi/UTILMD/PI_55237), [55238](/schnittstellen/202610/pruefi/UTILMD/PI_55238), [55239](/schnittstellen/202610/pruefi/UTILMD/PI_55239), [55240](/schnittstellen/202610/pruefi/UTILMD/PI_55240), [55241](/schnittstellen/202610/pruefi/UTILMD/PI_55241), [55242](/schnittstellen/202610/pruefi/UTILMD/PI_55242), [55243](/schnittstellen/202610/pruefi/UTILMD/PI_55243), [55671](/schnittstellen/202610/pruefi/UTILMD/PI_55671), [55675](/schnittstellen/202610/pruefi/UTILMD/PI_55675), [55685](/schnittstellen/202610/pruefi/UTILMD/PI_55685), [55687](/schnittstellen/202610/pruefi/UTILMD/PI_55687), [55689](/schnittstellen/202610/pruefi/UTILMD/PI_55689)

**UTILMD_GAS** (3) — [44051](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44051), [44105](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44105), [44169](/schnittstellen/202610/pruefi/UTILMD_GAS/PI_44169)

## Woher die Zahlen kommen

<div className="maco-tabellenrahmen">

| Quelle | Stand |
|---|---|
| Anwendungshandbuch | `ahb/202610/` der Knowledge Collection, 484 Prüfidentifikatoren |
| Spezifikationen | `maco-api-doc-resources`, Zweig `v202610`, 384 Dateien |
| Erzeugt aus | `maco-templater-app@41b3eb8c` |

</div>
