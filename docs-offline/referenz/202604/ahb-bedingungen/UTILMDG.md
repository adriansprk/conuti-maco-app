# Bedingungen UTILMDG
<span hidden data-pagefind-meta={"title:Bedingungen UTILMDG — Anwendungshandbuch (FV 202604)"} />

EDIFACT-Nachrichtentyp **UTILMDG** · Formatversion **202604** · 148 Bedingungen · 1 Pakete · 1 UB-Bedingungen · aus 86 Handbuchdatei(en)

## Bedingungen

<div className="maco-tabellenrahmen">

| Marke | Bedingung |
|---|---|
| **[1]** | Wenn Aufteilung vorhanden |
| **[2]** | Wenn UNH DE0070 (Übermittlungsfolgenum mer) mit 1 vorhanden |
| **[3]** | Bei Aufteilung, in der Nachricht mit der höchsten Übermittlungsfolgenum mer |
| **[4]** | Wenn MP-ID in SG2 NAD+MR (Nachrichtenempfänger) in der Rolle LF |
| **[5]** | Wenn MP-ID in SG2 NAD+MS (Nachrichtenabsender) in der Rolle LF |
| **[7]** | Wenn SG4 STS+7++ZG9/ZH1/ZH2 (Transaktionsgrund: Aufhebung einer zukünftigen Zuordnung wegen Auszug des Kunden / -wegen Stilllegung / -wegen aufgehobenem Vertragsverhältnis) vorhanden |
| **[9]** | Wenn SG4 STS+7++ZE4 (Transaktionsgrund: Weggefallene Markt- bzw. Messlokation) nicht vorhanden |
| **[10]** | Wenn SG4 STS+Z17 (Transaktionsgrund für befristete Anmeldung) vorhanden |
| **[11]** | Wenn SG4 STS+7++ZG9/ZH1/ZH2 (Transaktionsgrund: Aufhebung einer zukünftigen Zuordnung wegen Auszug des Kunden / -wegen Stilllegung / -wegen aufgehobenem Vertragsverhältnis) nicht vorhanden |
| **[12]** | Wenn SG4 DTM+471 (Ende zum nächstmöglichem Termin) nicht vorhanden |
| **[13]** | Wenn SG4 STS+E01++Z01 (Status der Antwort: Zustimmung mit Terminänderung) nicht vorhanden |
| **[14]** | Wenn Datum bekannt |
| **[15]** | Wenn SG4 STS+E01++Z34 (Status der Antwort: Ablehnung Mehrfachkündigung) vorhanden |
| **[16]** | Wenn SG4 STS+E01++Z12 (Status der Antwort: Ablehnung Vertragsbindung) vorhanden |
| **[17]** | Wenn bereits eine bestätigte Kündigung durch Kunde oder MP vorhanden |
| **[18]** | Wenn SG4 DTM+93 (Ende zum) nicht vorhanden |
| **[19]** | Wenn SG8 SEQ+Z01 (Daten der Marktlokation) SG10 CCI+++ZC0 (Prognose auf Basis von Werten) vorhanden |
| **[24]** | Wenn SG6 DTM+Z21 (Termin der Netznutzungsabrechnun g) vorhanden |
| **[25]** | Wenn der Meldepunkt im SG5 LOC+172 (Meldepunkt) DE3225 das Format der Marktlokations-ID hat |
| **[26]** | Wenn der Meldepunkt im SG5 LOC+172 (Meldepunkt) DE3225 das Format der Zählpunktbezeichnung hat |
| **[28]** | Wenn SG4 DTM+93 (Ende zum) vorhanden |
| **[29]** | Wenn eine Bilanzierung stattfindet |
| **[32]** | Wenn BGM+E03 (Änderungsmeldungen) vorhanden |
| **[33]** | Wenn in Abmeldung ein Bilanzierungsende vorhanden |
| **[35]** | Wenn das DE2380 von SG4 DTM+Z01 (Kündigungsfrist des Vertrags) an vierter Stelle T (Termin) enthält |
| **[36]** | Wenn SG4 STS+E01++ZC5 (Status der Antwort: Ablehnung andere Anmeldung in Bearbeitung) vorhanden |
| **[37]** | Wenn Anmeldung/Änderung befristet |
| **[39]** | Wenn LF beabsichtigt Zählerstand zu übermitteln |
| **[46]** | Wenn in SG8 SEQ+Z35 ein SG10 CCI+Z12 (Lastprofil) CAV (Lastprofil) DE3055 der Wert 293 enthalten ist |
| **[47]** | Wenn in SG8 SEQ+Z35 ein SG10 CCI+Z12 (Lastprofil) CAV (Lastprofil) DE3055 der Wert 293 nicht enthalten ist |
| **[48]** | Wenn in dieser SG4 das STS+E01++E14 (Status der Antwort: Ablehnung Sonstiges) vorhanden |
| **[51]** | Bei rückwirkendem Lieferende/Lieferbeginn |
| **[58]** | Wenn in diesem CCI das DE3055 mit dem Code 293 vorhanden |
| **[64]** | Wenn SG4 DTM+158 (Bilanzierungsbeginn) vorhanden |
| **[65]** | Wenn Marktgebietsüber- lappung besteht, sind alle Bilanzkreise des LF zu melden in denen freie Kapazitäten beim NB bestehen |
| **[66]** | Wenn SG10 CCI+Z19 (Bilanzkreis) im Vorgang mehr als einmal vorhanden |
| **[68]** | Wenn SG10 CCI+Z19 (Bilanzkreis) im Vorgang mehr als zweimal vorhanden |
| **[69]** | Wenn SG10 CCI+Z19 (Bilanzkreis) im Vorgang mehr als dreimal vorhanden |
| **[70]** | Wenn SG10 CCI+Z19 (Bilanzkreis) im Vorgang fünfmal vorhanden |
| **[77]** | Wenn SG8 SEQ+Z03 (Zähleinrichtungsdaten) CAV+Z30 (Identifikation/Nummer des Gerätes) nicht vorhanden |
| **[78]** | Wenn SG4 STS+7++E02 (Transaktionsgrund: Einzug in Neuanlage) nicht vorhanden |
| **[81]** | Wenn SG4 FTX+ABO+Z05 (Beschreibung der Abweichung zur übermittelten Liste: Änderung vorhanden) vorhanden |
| **[84]** | Wenn SG4 STS+E01++Z35 (Status der Antwort: Ablehnung der Abmeldeanfrage) vorhanden |
| **[92]** | Wenn Wert innerhalb SG bzw. Segment geändert wird |
| **[98]** | Wenn MP-ID in SG2 NAD+MS (Nachrichtenabsender) in der Rolle NB |
| **[106]** | Wenn in dieser SG8 SEQ+Z01 SG10 CCI+++ZA6 (Prognosegrundlage der Marktlokation: Prognose auf Basis von Profilen) vorhanden |
| **[108]** | Wenn Kundenwertverfahren (z. B. TU München) |
| **[123]** | Wenn noch mindestens eine weitere SG8 SEQ+Z20 (OBIS- Daten der Zähleinrichtung / Mengenumwerter) mit dem SG8 RFF+MG / Z11 (Gerätenummer des Zählers / Mengenumwerters) auf die gleiche Identifikation/Nummer des Gerätes referenziert |
| **[127]** | Hat der Lieferant auf Grund seines Vertrags Kenntnis, dass der Kunde keine hohe KA hat so muss er dies dem NB mitteilen |
| **[128]** | Wenn SG10 CAV+TAS/TKS/SAS/KAS vorhanden |
| **[129]** | Hat der Lieferant auf Grund seines Vertrags Kenntnis über die Höhe der Sonder-KA, so muss er diesen dem NB mitteilen |
| **[130]** | Wenn an Messlokation vorhanden |
| **[133]** | Wenn an der übermittelten Marktlokation / Messlokation vorhanden |
| **[137]** | Nicht bei Neuanlage |
| **[138]** | Wenn SG5 LOC+172 (Meldepunkt) nicht vorhanden |
| **[147]** | Wenn in Anfrage vorhanden |
| **[165]** | Wenn bekannt |
| **[166]** | Wenn vorhanden |
| **[200]** | Wenn BGM+Z26 (Vorläufige Meldung zur Marktraumumstellung) vorhanden |
| **[202]** | Wenn SG4 STS+E01+ZG2 (Status der Antwort: Gültiges Ergebnis nach der Datenprüfung) vorhanden |
| **[203]** | Wenn STS+7++E06 / Z39 / ZC6 / ZC7 / ZT6 / ZT7 |
| **[205]** | Wenn SG9 QTY+Y02 (TUM Kundenwert) nicht vorhanden |
| **[209]** | Wenn im selben Segment im DE2379 der Code 303 vorhanden ist |
| **[212]** | Wenn im selben SG12 NAD DE3124 nicht vorhanden |
| **[213]** | Wenn SG12 NAD+Z09 (Kunde des Lieferanten) vorhanden |
| **[216]** | Wenn CCI+++Z88 (Netznutzung) CAV+Z74:::Z08 (Netznutzungsvertrag: Direkter Vertrag zwischen Kunden und NB) vorhanden |
| **[219]** | Wenn an Marktlokation vorhanden |
| **[230]** | Sich ergebendes Datum/bzw. Endedatum des Turnuszeitraums aus DTM+Z21 (Termin der Netznutzungsabrechnun g) und DTM+Z09 (Nächste Netznutzungsabrechnun g) muss &gt;= DTM+92 (Beginn zum) sein |
| **[241]** | Wenn MP-ID in SG2 NAD+MR (Nachrichtenempfänger) in der Rolle MSB |
| **[249]** | Innerhalb eines SG4 IDE müssen alle DE1131 der SG4 STS+E01 den identischen Wert enthalten |
| **[252]** | Wenn DE0068 vorhanden |
| **[257]** | Wenn in derselben SG8 SEQ+Z02 (OBIS- Daten der Marktlokation) das PIA+5+7-0?:33.86.0 vorhanden |
| **[268]** | Wenn der Code im DE3207 in der "EDI@Energy Codeliste der europäischen Ländercodes" in der Spalte "PLZ vorhanden" ein "X" aufgeführt ist |
| **[274]** | Wenn in derselben SG8 SEQ+Z20 (OBIS-Daten der Zähleinrichtung / Mengenumwerter) das PIA+5+7- b?:3.0.0 / 7-b?:6.0.0 / 7-b?:3.1.0 / 7-b?:6.1.0 / 7-b?:3.2.0 / 7-b?:6.2.0 / 7-b?:13.2.0 / 7-b?:16.2.0 / 7- b?:1.0.0 / 7-b?:2.0.0 / 7-b?:4.0.0 / 7-b?:5.0.0 / 7-b?:11.2.0 / 7-b?: 12.2.0 / 7-b?:14.2.0 / 7-b?:15.2.0 vorhanden |
| **[283]** | Wenn Empfänger der Nachricht der zum Nachrichtendatum aktuell zugeordnete Lieferant ist |
| **[315]** | Es sind alle OBISKennzahlen gem. EDI@Energy Codeliste der OBIS-Kennzahlen und Medien für den deutschen Energiemarkt Kap. 4 anzugeben welche an der Marktlokation erforderlich sind, dabei muss der Mindestumfang aus Kap. 4.6 eingehalten werden. Der Mindestumfang der OBIS- Kennzahlen ergibt sich aus den genannten Messprodukt-Codes dem Kap. 5.2 des Dokumentes "Codeliste der Konfigurationen" |
| **[324]** | Es sind alle OBIS- Kennzahlen gem. EDI@Energy Codeliste der OBIS Kennzahlen Kap. 4. anzugeben welche an der Zähleinrichtung genutzt werden. Der Mindestumfang der OBIS-Kennzahlen ergibt sich aus den genannten Messprodukt-Codes dem Kap. 5.2 des Dokumentes "Codeliste der Konfigurationen" |
| **[328]** | Wenn IMD++Z36+Z12 (Identifikationslogik: Marktlokations-ID) vorhanden |
| **[333]** | Wenn IMD+Z36+Z13 (Identifikationslogik: Alle Identifikationsdaten) vorhanden |
| **[336]** | Wenn in Änderungsmeldung gefüllt |
| **[345]** | Wenn 33-stelliger Meldepunkt im SG5 LOC+172 (Meldepunkt) vorhanden |
| **[361]** | Wenn STS+E01++A03/A04 nicht vorhanden |
| **[362]** | Wenn STS+E01++A03/A17 nicht vorhanden |
| **[367]** | Wenn SG4 STS+E01++A04 vorhanden |
| **[368]** | Es sind alle Codes aus der Codeliste G_0009 erlaubt |
| **[427]** | Messprodukt-Code aus Kapitel 3 "Codeliste der Standard- Messprodukte Gas" der Codeliste der Konfigurationen |
| **[442]** | Wenn in keinem SG8+SEQ+Z09 Mengenumwerterdaten das RFF+MG (Referenz auf die Gerätenummer) der in diesem RFF DE1154 genannte Gerätenummer des Zählers vorhanden ist |
| **[490]** | wenn Wert in diesem DE, an der Stelle CCYYMMDDHHMM ein Zeitpunkt aus dem angegeben Zeitraum der Tabelle Kapitel 3.5 „Übersicht gesetzliche deutsche Sommerzeit (MESZ)“ der Spalten: „Sommerzeit (MESZ) von“ Darstellung in UTC und „Sommerzeit (MESZ) bis“ Darstellung in UTC ist. |
| **[491]** | wenn Wert in diesem DE, an der Stelle CCYYMMDDHHMM ein Zeitpunkt aus dem angegeben Zeitraum der Tabelle Kapitel 3.6 „Übersicht gesetzliche deutsche Zeit (MEZ)“ der Spalten: „Winterzeit (MEZ) von“ Darstellung in UTC und „Winterzeit (MEZ) bis“ Darstellung in UTC ist. |
| **[494]** | Das hier genannte Datum muss der Zeitpunkt sein, zu dem das Dokument erstellt wurde, oder ein Zeitpunkt, der davor liegt |
| **[500]** | Hinweis: Code ist gemäß der Kategorie der zu stornierenden Meldung zu wählen |
| **[501]** | Hinweis: Die Angabe wird aus dem DTM+157 (Änderung zum) der Zuordnungsliste übernommen |
| **[502]** | Hinweis: Ersatzbelieferung gibt es nur bei - Marktlokationen in der Niederdruckebene, die kein Haushaltskunde gem. EnWG sind und die nicht mehr der gesetzlichen Ersatzversorgung (drei Monate) unterliegen und - für Marktlokationen, die in Mitteldruck einer Versorgung zugeführt werden sollen. Grundlage für eine Ersatzbelieferung ist die bilaterale Vereinbarung. |
| **[504]** | Hinweis: Der Code Z22 wird auch in der Sparte Strom genutzt. Der Verweis auf den Einspeisevergütungsinter vall ist in der Sparte Gas nicht relevant. |
| **[507]** | Hinweis: Ursprünglich vom NB bestätigtes Beginndatum |
| **[508]** | Hinweis: Beginndatum beim neuen NB |
| **[510]** | Hinweis: Zu verwenden bei der Abmeldung der ESV |
| **[513]** | Hinweis: Ist SG9 QTY+Y02 (TUM Kundenwert) vorhanden, dann ist ausschließlich SG9 QTY+Y02, unabhängig von SG9 QTY+31 (Veranschlagte Jahresmenge gesamt), für die Bilanzierung und MMM- Abrechnung zu nutzen |
| **[527]** | Hinweis: Es ist die ID der Marktlokation und alle Identifikatoren der Messlokationen anzugeben |
| **[528]** | Hinweis: Es ist das Datum/Daten aus der Anfrage zu verwenden |
| **[530]** | Hinweis: Es sind alle an dem Meldepunkt vorhandenen Daten, die mit dieser Segmentgruppe übermittelt werden und zum Datum „Änderung zum“ Gültigkeit haben, anzugeben. Dies kann zur Folge haben, dass Segmentgruppen bzw. Segmente zu wiederholen sind |
| **[556]** | Hinweis: Wenn keine Korrespondenzanschrift des Endverbrauchers/Kunden vorliegt, ist die Anschrift der Marktlokation zu übermitteln |
| **[558]** | Hinweis: Diese Information kann freiwillig ausgetauscht werden |
| **[559]** | Hinweis: Die Korrespondenzanschrift des Endverbrauchers/Kunden wird nicht zur Identifikation genutzt |
| **[560]** | Hinweis: Die Angabe Name und Adresse für die Ablesekarte wird nicht zur Identifikation genutzt |
| **[566]** | Hinweis: Altlieferant |
| **[567]** | Hinweis: Neulieferant |
| **[570]** | Hinweis: Netzbetreiber Alt |
| **[571]** | Hinweis: Auslösender Marktpartner (LFA bei STS+7++ZG9, LFN bei STS+7++ZH0, NB bei STS+7++ZH1) |
| **[572]** | Hinweis: Kundenname aus Anmeldung Lieferant neu |
| **[573]** | Hinweis: Wenn keine andere Information für „Name und Adresse für die Ablesekarte“ vorliegt, wird das Segment aus dem Kundennamen im NAD+Z09 und der Adresse aus der Korrespondenzanschrift NAD+Z04 zusammengesetzt |
| **[576]** | Hinweis: Stammdaten des bisherigen Messstellenbetreibers |
| **[577]** | Hinweis: Wird mit dem ursprünglich vom NB bestätigten Beginndatum gefüllt |
| **[581]** | Hinweis: Es ist das nächst mögliche Kündigungsdatum anzugeben |
| **[583]** | Hinweis: Verwendung der ID der Marktlokation |
| **[584]** | Hinweis: Verwendung der ID der Messlokation |
| **[590]** | Hinweis: Es ist die ID der Marktlokation, welche dem LF zugeordnet sind, sowie alle Identifikatoren der Messlokationen anzugeben |
| **[601]** | Hinweis: Es ist die ID der Marktlokation und alle Identifikatoren der Messlokationen anzugeben. |
| **[621]** | Hinweis: Es ist der MSB anzugeben, welcher ab dem Zeitpunkt der Lokation zugeordnet ist, der in DTM+76 (Datum zum geplanten Leistungsbeginn) genannt ist. |
| **[622]** | Hinweis: Falls die OBIS-Kennzahl für mehrere Marktrollen relevant ist, so muss die Segmentgruppe pro Marktrolle wiederholt werden |
| **[636]** | Hinweis: Dieses RFF klassifiziert mit einem Code im DE1153 die in derselben Segmentgruppe enthaltenen DTM zu einem Markt- bzw. Messlokation relevanten Inhalt |
| **[637]** | Hinweis: Bei Verpflichtungsanfrage |
| **[638]** | Hinweis: Bei Aufforderung zur Übernahme der einzelnen Messlokation durch den gMSB |
| **[643]** | Hinweis: Nachfolgender Netzbetreiber |
| **[644]** | Hinweis: Wenn in der zugehörigen Anmeldung (44001) in diesem Segmente "Einzug in Neuanlage" (SG4 STS+7++E02) enthalten ist, wird in diesem Geschäftsvorfall der Code E01 verwendet |
| **[651]** | Hinweis: Bei einer Marktraumumstellung (Gas) ist zu beachten, dass die tatsächliche Meldung zur Marktraumumstellung auf Ebene der Messlokation durch Angabe der Gasqualität erfolgt. Die betroffene Marktlokation ist vom LF und MSB selbst festzustellen |
| **[654]** | Hinweis: Es sind ausschließlich die Daten zum Meldepunkt anzugeben, die für den in NAD+MR (Nachrichtenempfänger) adressierten Marktpartner relevant ist |
| **[655]** | Hinweis: Wenn ein Zähler an einen Mengenumwerter angeschlossen ist werden an dem Zähler keine OBIS-Kennzahlen angegeben Hier gibt es nur OBIS Kennzahlen vom Mengenumwerter |
| **[902]** | Format: Möglicher Wert: ≥ 0 |
| **[907]** | Format: max. 4 Nachkommastellen |
| **[912]** | Format: max. 6 Nachkommastellen |
| **[930]** | Format: max. 2 Nachkommastellen |
| **[931]** | Format: ZZZ = +00 |
| **[934]** | Format: HHMM = 0400 |
| **[935]** | Format: HHMM = 0500 |
| **[937]** | Format: keine Nachkommastelle |
| **[938]** | Format: Möglicher Wert: &lt;= 10 |
| **[950]** | Format: Marktlokations-ID |
| **[951]** | Format: Zählpunktbezeichnung |
| **[952]** | Format: Gerätenummer nach DIN 43863-5 |
| **[953]** | Format: Marktlokations-ID oder Zählpunktbezeichnung |
| **[2061]** | Segment bzw. Segmentgruppe ist genau einmal je SG4 IDE (Vorgang) anzugeben |
| **[2119]** | Je SG8 SEQ+Z13 (Smartmeter-Gateway) ist genau einmal die Segmentgruppe anzugeben |
| **[2284]** | Für jede Messlokations-ID im SG5 LOC+172 (Meldepunkt) DE3225 genau einmal anzugeben |
| **[2286]** | Für jede SEQ+Z18 (Daten der Messlokation) mindestens einmal anzugeben |
| **[2287]** | Für jede SEQ+Z03 (Zähleinrichtungsdaten) mindestens einmal anzugeben |
| **[2335]** | Für jede SEQ+Z02 (OBIS- Daten der Marktlokation), welche im PIA+5 die OBIS-Kennzahl 7- 20:99.33.17/7-0:33.86.0 übermittelt, genau einmal anzugeben |
| **[2353]** | Für jede SEQ+Z09 (Mengenumwerter- Daten) mindestens einmal anzugeben |

</div>

## UB-Bedingungen

UB-Bedingungen fassen mehrere Marken zu einem Ausdruck zusammen. Sie stehen in den Handbuchzeilen wie eine Bedingung, lösen sich aber in die Marken darin auf.

<div className="maco-tabellenrahmen">

| Marke | Ausdruck |
|---|---|
| **[UB2]** | ([931] ∧ [934] [490]) ⊻ ([931] ∧ [935] [491]) |

</div>

## Bedingungspakete

Bedingungspakete bündeln Voraussetzungen.

<div className="maco-tabellenrahmen">

| Paket | Voraussetzungen | Bedingungen |
|---|---|---|
| **[1P]** | -- | Hinweis: Das ist das Standardpaket, wenn keine Bedingung zum Tragen kommt, z. B. im COM-Segment. |

</div>

<Hinweisbereich>

Diese Seite führt den Klartext jeder Bedingung, auf die das Anwendungshandbuch des Nachrichtentyps **UTILMDG** in dieser Formatversion verweist. Eine Zeile des Handbuchs schreibt `Muss [704]`; was [704] verlangt, steht hier.

Die Liste gilt **für den Nachrichtentyp**, nicht für einen einzelnen Prüfidentifikator. Das ist keine Vereinfachung, sondern die Form der Quelle: die Bedingungsliste liegt in jeder Handbuchdatei des Formats identisch vor.

:::caution{title="Warum hier keine Zuordnung zu einzelnen Prüfidentifikatoren steht"}

Das Zwischenformat, aus dem diese Dokumentation die Handbuchzeilen liest, ordnet Bedingungen einer **Spalte** zu — und diese Zuordnung ist gegen das Original verschoben. Gemessen am 05.09.2026 an UTILMD Strom: das Handbuch führt `STS DE9013` als `X [360]` (nur Zustimmungscodes) beim Prüfidentifikator **55017** und `X [359]` (nur Ablehnungscodes) bei **55018**; das Zwischenformat setzt `[360]` auf 55016 und `[359]` auf 55017 **und** 55018. Dasselbe bei `FTX Muss [83]`: im Handbuch bei 55018, im Zwischenformat bei 55017.

Unabhängig bestätigt durch die Änderungslisten der Quelle: die Änderungs-IDs 25242, 25821, 25822, 25445 und 25243 verorten [83], [351] und [352] ausdrücklich beim „Anwendungsfall 55018 Ablehnung Kündigung“. Kein Eintrag ordnet sie 55016 oder 55017 zu.

Deshalb steht hier der **Text** jeder Bedingung und nirgends die Behauptung, welche Bedingung für welchen Prüfidentifikator gilt. Wer das braucht, schlägt im Original-Anwendungshandbuch nach.

:::

:::note{title="1 Bedingungen stehen nicht in jeder Handbuchdatei"}

Die Bedingungsliste ist formatweit gemeint, ist es aber nicht überall: die folgenden Marken kommen in weniger als allen 86 Dateien dieses Formats vor. Sie stehen trotzdem hier — eine Bedingung wegzulassen, weil eine Datei sie nicht führt, hieße einen Verweis wieder ins Leere zeigen zu lassen.

[UB2]

:::

Gemessen am 05.09.2026 verweist **keine** `ahb_expression` dieser Quelle auf eine Paketmarke — die Bedingungspakete stehen auf dieser Seite, weil die Quelle sie führt, nicht weil eine Handbuchzeile auf sie zeigt.

</Hinweisbereich>
