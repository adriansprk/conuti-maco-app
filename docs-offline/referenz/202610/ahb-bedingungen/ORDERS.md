# Bedingungen ORDERS
<span hidden data-pagefind-meta={"title:Bedingungen ORDERS — Anwendungshandbuch (FV 202610)"} />

EDIFACT-Nachrichtentyp **ORDERS** · Formatversion **202610** · 249 Bedingungen · 3 Pakete · 3 UB-Bedingungen · aus 44 Handbuchdatei(en)

## Bedingungen

<div className="maco-tabellenrahmen">

| Marke | Bedingung |
|---|---|
| **[1]** | Wenn IMD+Z03 vorhanden |
| **[2]** | Wenn BGM+7 vorhanden |
| **[6]** | Wenn MP-ID in SG2 NAD+MS mit Rolle LF vorhanden |
| **[7]** | Wenn MP-ID in SG2 NAD+MS mit Rolle NB vorhanden |
| **[9]** | Wenn bekannt |
| **[12]** | Wenn vorhanden |
| **[13]** | Wenn SG2 LOC+172 nicht vorhanden |
| **[15]** | Wenn MP-ID in SG2 NAD+MS mit Rolle MSB vorhanden |
| **[16]** | Wenn eine untergeordnete SG vorhanden |
| **[17]** | Wenn ein Segment innerhalb der SG vorhanden |
| **[18]** | Wenn IMD++Z11 vorhanden |
| **[19]** | Wenn IMD++Z12 vorhanden |
| **[21]** | Wenn BGM+Z28 vorhanden |
| **[23]** | Wenn MP-ID in SG2 NAD+MR mit Rolle NB vorhanden |
| **[24]** | Wenn IMD++Z35 vorhanden |
| **[26]** | Wenn MP-ID in SG2 NAD+MS mit Rolle ÜNB vorhanden |
| **[27]** | Wenn MP-ID in SG2 NAD+MR mit Rolle MSB vorhanden |
| **[28]** | Wenn MP-ID in SG2 NAD+MR aus Sparte Strom |
| **[29]** | Wenn MP-ID in SG2 NAD+MR aus Sparte Gas |
| **[33]** | Wenn IMD+Z01 vorhanden |
| **[34]** | Wenn IMD+Z02 vorhanden |
| **[36]** | Wenn MP-ID in SG2 NAD+MR mit Rolle NB nicht vorhanden |
| **[38]** | Wenn FTX+Z04/Z05 vorhanden |
| **[45]** | Wenn MP-ID in SG2 NAD+MS mit Rolle MSB nicht vorhanden |
| **[46]** | Wenn SG29 IMD++Z46 vorhanden |
| **[47]** | Wenn SG29 IMD++Z46 nicht vorhanden |
| **[51]** | Wenn BGM+Z48 vorhanden |
| **[54]** | Wenn FTX+Z06 vorhanden |
| **[55]** | Wenn DTM+469 (Beginn zum nächstmöglichen Termin) nicht vorhanden |
| **[56]** | Wenn DTM+203 (Ausführungsdatum) nicht vorhanden |
| **[57]** | Wenn im selben SG2 NAD DE3124 nicht vorhanden |
| **[60]** | MP-ID nur aus Sparte Gas |
| **[61]** | MP-ID nur aus Sparte Strom |
| **[62]** | MP-ID mit Rolle MSB |
| **[63]** | MP-ID mit Rolle NB |
| **[64]** | Wenn SG2 NAD+Z03 nicht vorhanden |
| **[65]** | Wenn FTX+Z08 vorhanden |
| **[67]** | Wenn DTM+163 nicht vorhanden |
| **[68]** | Wenn DTM+7 nicht vorhanden |
| **[69]** | Wenn NAD+Z23 nicht vorhanden |
| **[70]** | Wenn NAD+Z03 nicht vorhanden |
| **[75]** | Wenn für den erforderlichen Wert keine Zählzeit benötigt wird |
| **[76]** | Wenn in derselben SG29 mit Z54 in LIN DE1229 (Erforderliches Produkt der Marktlokation) das PIA+5 DE7140 mit einem Messprodukt aus Codeliste der Konfigurationen Kapitel 2.1.1 "Standard-Messprodukt der Marktlokation mit der Wahlmöglichkeit der Zuordnung einer Zählzeit" vorhanden ist |
| **[77]** | Wenn im selben CCI im DE7059 der Code Z39 (Code der Zählzeitdefinition) vorhanden ist |
| **[86]** | Wenn in derselben SG29 mit Z19 in LIN DE1229 (Erforderliches Produkt der Messlokation) das PIA+5 DE7140 mit einem Messprodukt aus Codeliste der Konfigurationen Kapitel 2.3.1 "Standard-Messprodukt der Messlokation mit der Wahlmöglichkeit der Zuordnung einer Zählzeit" vorhanden ist |
| **[87]** | Wenn FTX+Z09/Z10 vorhanden |
| **[93]** | Wenn in derselben Nachricht eine SG29 mit Z16 in LIN DE1229 (Erforderliches Produkt der Tranche) nicht vorhanden |
| **[94]** | Wenn in derselben Nachricht eine SG29 mit Z54 in LIN DE1229 (Erforderliches Produkt der Marktlokation) nicht vorhanden |
| **[95]** | Messprodukt-Code aus dem Kapitel 2.1 "Standard-Messprodukte der Marktlokation" der Codeliste der Konfigurationen |
| **[96]** | Messprodukt-Code aus dem Kapitel 2.2 "Standard-Messprodukte der Tranche" der Codeliste der Konfigurationen |
| **[97]** | Wenn FTX+Z10 vorhanden |
| **[99]** | Wenn FTX+Z08/Z10 vorhanden |
| **[100]** | Messprodukt-Code aus dem Kapitel 2.3 "Standard-Messprodukte der Messlokation" der Codeliste der Konfigurationen |
| **[101]** | Wenn MP-ID in SG2 NAD+MR mit Rolle MSB in der Sparte Gas nicht vorhanden |
| **[102]** | Wenn in derselben SG29 LIN das CCI+++Z25 (Geräteart Wandler) vorhanden |
| **[103]** | Wenn in derselben SG29 LIN das CCI+++Z25 (Geräteart Wandler) nicht vorhanden |
| **[104]** | Wenn MP-ID in SG2 NAD+VY mit Rolle LF vorhanden |
| **[105]** | Wenn die bisherige Konfiguration mit Zählzeiten des LF vom LF beendet werden soll |
| **[106]** | Wenn IMD++Z60 (Abbestellung Messprodukt mit Zählzeitdefinition des LF) nicht vorhanden |
| **[107]** | Wenn IMD++Z57 (Abbestellung Zählzeitdefinition) nicht vorhanden |
| **[108]** | Wenn RFF+AGK (Konfigurations-ID) nicht vorhanden |
| **[109]** | Wenn LOC+172 (Meldepunkt) nicht vorhanden |
| **[110]** | Wenn DTM+163 (Beginn Zeitraum für Wertanfrage) vorhanden |
| **[113]** | Wenn LIN DE1229 mit Code Z42 (Zählzeitdefinition) vorhanden |
| **[114]** | Wenn LIN DE1229 mit Code Z69 (Schaltzeitdefinition) vorhanden |
| **[115]** | Wenn LIN DE1229 mit Code Z70 (Leistungskurvendefinition) vorhanden |
| **[117]** | Wenn SG29 LIN++Z64 (Erforderliches Produkt Schaltzeitdefinitionen) vorhanden |
| **[118]** | Wenn SG29 LIN++Z65 (Erforderliches Produkt Leistungskurvendefinitionen) vorhanden |
| **[119]** | Wenn SG29 LIN++Z66 (Erforderliches Produkt Ad-hoc-Steuerkanal) vorhanden |
| **[120]** | Wenn SG29 LIN++Z67 (Erforderliches Messprodukt für Werte nach Typ 2 aus Backend) vorhanden |
| **[121]** | Wenn SG29 LIN++Z68 (Erforderliches Produkt Konfigurationserlaubnis für Werte nach Typ 2 aus SMGW) vorhanden |
| **[122]** | Wenn SG1 RFF+Z41 (Referenznummer des Vorgangs der Anmeldung nach WiM) nicht vorhanden |
| **[123]** | Wenn DTM+203 (Ausführungsdatum) nicht vorhanden |
| **[124]** | Wenn SG1 RFF+Z41 (Referenznummer des Vorgangs der Anmeldung nach WiM) vorhanden |
| **[125]** | Es sind nur die Konfigurations-Produkte erlaubt, die in der Codeliste der Konfigurationen im Kapitel 4.1 „Konfigurationsprodukte Schaltzeitdefinition“ enthalten sind. |
| **[126]** | Es sind nur die Konfigurations-Produkte erlaubt, die in der Codeliste der Konfigurationen im Kapitel 4.2 „Konfigurationsprodukte Leistungskurvendefinition“ enthalten sind. |
| **[127]** | Es sind nur die Konfigurations-Produkte erlaubt, die in der Codeliste der Konfigurationen im Kapitel 4.3 „Konfigurationsprodukte Ad-Hoc-Steuerkanal“ enthalten sind. |
| **[128]** | Es sind nur die Messprodukte erlaubt, die in der Codeliste der Konfigurationen im Kapitel 4.5 „Messprodukte für Werte nach Typ 2 aus Backend für LF und NB“ enthalten sind. |
| **[129]** | Es sind nur die Messprodukte erlaubt, die in der Codeliste der Konfigurationen im Kapitel 4.4 „Messprodukte mit Konfigurationserlaubnis für Werte nach Typ 2 aus SMGW“ enthalten sind. |
| **[130]** | Wenn in LOC+172 DE3225 (Meldepunkt) die ID einer Marktlokation angegeben ist |
| **[131]** | Wenn in LOC+172 DE3225 (Meldepunkt) die ID einer Messlokation angegeben ist |
| **[132]** | Wenn in LOC+172 DE3225 (Meldepunkt) die ID einer Netzlokation angegeben ist |
| **[133]** | Wenn in LOC+172 DE3225 (Meldepunkt) die ID einer Steuerbaren Ressource angegeben ist |
| **[134]** | Wenn die Position in der ursprünglichen Antwort auf die Bestellung aus SG1 RFF+Z42 vorhanden war und reklamiert werden soll |
| **[135]** | Wenn SG29 LIN++Z64 (Erforderliches Produkt Schaltzeitdefinitionen) nicht vorhanden |
| **[136]** | Wenn SG29 LIN++Z65 (Erforderliches Produkt Leistungskurvendefinitionen) nicht vorhanden |
| **[137]** | Wenn SG29 LIN++Z66 (Erforderliches Produkt Ad-hoc-Steuerkanal) nicht vorhanden |
| **[138]** | Wenn SG29 LIN++Z67 (Erforderliches Messprodukt für Werte nach Typ 2 aus Backend) nicht vorhanden |
| **[139]** | Wenn SG29 LIN++Z68 (Erforderliches Produkt Konfigurationserlaubnis für Werte nach Typ 2 aus SMGW) nicht vorhanden |
| **[140]** | Messprodukt-Code aus dem Kapitel 2.4 "Standard-Messprodukte der Netzlokation" der Codeliste der Konfigurationen |
| **[141]** | Es sind nur die Messprodukt-Position-Codes erlaubt, die in der Codeliste der Konfigurationen im Kapitel 4.7 „Art der Werte für Messprodukte nach Typ 2“ enthalten sind. |
| **[142]** | Wenn innerhalb derselben SG29 LIN im PIA+5 DE7140 (Erforderliches Produkt Konfigurationserlaubnis für Werte nach Typ 2 aus SMGW) ein Produkt angegeben ist, das in der Codeliste der Konfigurationen im Kapitel 4.4 „Messprodukte mit Konfigurationserlaubnis für Werte nach Typ 2 aus SMGW“ in der Spalte "Auslöser" mit dem Wert "Bei Schwellwertunter- / -überschreitung" gekennzeichnet ist. |
| **[143]** | Wenn in LOC+172 DE3225 (Meldepunkt) die ID einer Steuerbaren Ressource angegeben ist |
| **[147]** | Wenn im DE3155 in demselben COM der Code EM vorhanden ist |
| **[148]** | Wenn im DE3155 in demselben COM der Code TE / FX / AJ / AL vorhanden ist |
| **[152]** | Wenn in SG29 LIN (Erforderliches Produkt der Messlokation) das PIA+5 DE7140 mit einem Produkt-Code vorhanden ist der in der Codeliste der Konfigurationen im Kapitel 7 "Produkte zur Bestellung einer Änderung an einer Lokation" in der "Spalte Bezeichnung" mit dem Wert "weitere Energieflussrichtung" vorhanden ist. |
| **[153]** | Es sind nur die Produkt-Codes erlaubt, die in der Codeliste der Konfigurationen im Kapitel 7 "Produkte zur Bestellung einer Änderung an einer Lokation" die in der Spalte "Ebene" mit dem Wert "Messlokation" vorhanden sind. |
| **[155]** | Es sind nur die Produkt-Codes erlaubt, die in der Codeliste der Konfigurationen im Kapitel 7 "Produkte zur Bestellung einer Änderung an einer Lokation" die in der Spalte "Ebene" mit dem Wert "Steuerbare Ressource" vorhanden sind. |
| **[156]** | Es sind weiterhin nur die Produkt-Codes erlaubt, die in der Codeliste der Konfigurationen im Kapitel 7 "Produkte zur Bestellung einer Änderung an einer Lokation" die in der Spalte "Produkt gegenüber MSB von Marktrolle bestellbar" mit einem "X" in der Spalte "NB" gekennzeichnet ist. |
| **[157]** | Es sind weiterhin nur die Produkt-Codes erlaubt, die in der Codeliste der Konfigurationen im Kapitel 7 "Produkte zur Bestellung einer Änderung an einer Lokation" die in der Spalte "Produkt gegenüber MSB von Marktrolle bestellbar" mit einem "X" in der Spalte "LF" gekennzeichnet ist. |
| **[158]** | Es sind nur die Produkt-Codes erlaubt, die in der Codeliste der Konfigurationen im Kapitel 6.2 "Produkte zur Bestellung einer Änderung von Abrechnungsdaten" genannt sind. |
| **[159]** | Wenn in derselben SG29 LIN im PIA+5 (Erforderliches Produkt Abrechnungsdaten) DE7140 ein Produkt-Code genannt ist, der in der Codeliste der Konfigurationen im Kapitel 6.2 "Produkte zur Bestellung einer Änderung von Abrechnungsdaten" in der Spalte "Code der Produkteigenschaft (Wertebereich)" mit einem Code befüllt ist. |
| **[160]** | Es sind nur die Codes der Produkteigenschaft zu dem in derselben SG29 LIN im PIA+5 (Erforderliches Produkt Abrechnungsdaten) DE7140 erlaubt, die in der Codeliste der Konfigurationen im Kapitel 6.2 "Produkte zur Bestellung einer Änderung von Abrechnungsdaten" in derselben Zeile wie der Produkt-Code stehen und in der Spalte "Code der Produkteigenschaft (Wertebereich)" genannt sind. |
| **[161]** | Wenn in derselben SG29 LIN (Erforderliches Produkt Abrechnungsdaten) das SG30 CAV+ZH9 (Code der Produkteigenschaft) nicht vorhanden ist. |
| **[162]** | Es ist nur der Wertebereich erlaubt, der zu dem in derselben SG29 LIN im PIA+5 (Erforderliches Produkt Abrechnungsdaten) DE7140 genannten Produkt, das in der Codeliste der Konfigurationen im Kapitel 6.2 "Produkte zur Bestellung einer Änderung von Abrechnungsdaten" in derselben Zeile wie der Produkt-Code in der Spalte "Wertedetails für Position" genannt ist. |
| **[163]** | Wenn innerhalb der Nachricht eine SG30 CCI+++ZA9 (Messprodukt für Übertragungsnetzbetreiber relevant) vorhanden ist. |
| **[164]** | Wenn die Konfiguration der in SG34 RFF+Z20 DE1154 (Referenz auf ID der Tranche) genannte Tranche innerhalb derselben SG29 LIN++Z16 (Erforderliches Produkt der Tranche) unverändert bestehen bleibt. |
| **[165]** | Wenn die Konfiguration der in SG34 RFF+Z20 DE1154 (Referenz auf ID der Tranche) genannte Tranche innerhalb derselben SG29 LIN++Z16 (Erforderliches Produkt der Tranche) aufgrund einer Zuordnung eines LF neu konfiguriert werden soll oder die Tranche neu gebildet wurde. |
| **[166]** | Wenn es sich um die Einrichtung der Konfigurationen aufgrund einer Zuordnung eines LF zu einer Tranche handelt |
| **[167]** | Wenn SG2 NAD+DP (Meldepunkt), SG3 RFF+Z20 (Referenz auf ID der Tranche) vorhanden |
| **[168]** | Wenn SG2 NAD+DP (Meldepunkt), SG3 RFF+Z20 (Referenz auf ID der Tranche) nicht vorhanden |
| **[169]** | Wenn in SG29 LIN++Z19 (Erforderliches Produkt der Messlokation) in SG30 CCI (Zugeordnete Zählzeitdefinition) im DE7059 der Code Z39 (Code der Zählzeitdefinition) vorhanden ist |
| **[170]** | Wenn in derselben SG29 LIN die SG30 CCI+Z37++ZD1 (Basis zur Bildung der Tranchengröße) (Prozentual) vorhanden |
| **[171]** | Wenn in derselben SG29 LIN (Erforderliches Produkt der Tranche) das IMD+++Z64 (Leistungsbeschreibung Konfiguration) (Neukonfiguration) vorhanden ist |
| **[172]** | Wenn es sich bei der in SG2 LOC+172 DE3225 genannten Lokation um die Integration in eine Kundenanlage oder Herauslösung aus einer Kundenanlage nach §20 Abs.1d EnWG handelt. Details siehe UTILMD AHB Strom. |
| **[173]** | Wenn IMD++Z66 (Beendigung Konfiguration aufgrund Überführung der Marktlokation zu ruhender Marktlokation) vorhanden |
| **[174]** | Wenn IMD++Z67 (Aktivierung Konfiguration in der derzeit ruhenden Marktlokation) vorhanden |
| **[175]** | Wenn SG2 NAD+DP (Meldepunkt), SG3 RFF+Z59 (Referenz auf die ID der Marktlokation der Kundenanlage) vorhanden |
| **[176]** | Wenn SG2 NAD+DP (Meldepunkt), SG3 RFF+Z59 (Referenz auf die ID der Marktlokation der Kundenanlage) nicht vorhanden |
| **[177]** | Wenn IMD++Z66 (Beendigung Konfiguration aufgrund Überführung der Marktlokation zu ruhender Marktlokation) nicht vorhanden |
| **[178]** | Wenn vom NB eine Abtretungserklärung vom Kunden gewünscht ist. |
| **[179]** | Wenn in derselben SG29 LIN im PIA+5 (Erforderliches Produkt Abrechnungsdaten) DE7140 das Produkt "Empfänger der Vergütung zur Einspeisung" aus der Codeliste der Konfigurationen im Kapitel 6.2 "Produkte zur Bestellung einer Änderung von Abrechnungsdaten" genannt ist und in derselben SG29 LIN im SG30 CAV+ZH9 (Code der Produkteigenschaft) im DE7110 aus der Spalte "Code der Produkteigenschaft (Wertebereich)" mit dem Code "Lieferant" gefüllt ist. |
| **[180]** | Wenn in derselben SG29 LIN im PIA+5 (Erforderliches Produkt Abrechnungsdaten) DE7140 ein Produkt-Code genannt ist der in der Codeliste der Konfigurationen im Kapitel 6.2 "Produkte zur Bestellung einer Änderung von Abrechnungsdaten" in der Spalte „Wertedetails für Position“ die ggf. enthaltene Bedingung erfüllt ist. |
| **[181]** | Wenn BGM+Z93 (Bestellung eines Angebots Änderung der Technik der Lokation) vorhanden |
| **[182]** | Wenn BGM+Z12 (Änderung der Technik der Lokation) vorhanden. |
| **[183]** | Wenn MP-ID in NAD+MS aus Sparte Gas |
| **[184]** | Wenn es sich in der Position (SG34 RFF+Z03 DE1154) die innerhalb dieser SG29 LIN bestellt wird, um die Bestellung des Geräteübernahmeangebotes eines Smartmeter-Gateways handelt. |
| **[185]** | Wenn FTX+Z29 (Endpunkt-Adresse (IP:Port)) vorhanden |
| **[196]** | Zulässig sind ausschließlich Codes aus der Spalte „Code“ der Codeliste der Verwendungszwecke (Kapitel 2), sofern in derselben Zeile sowohl in der Spalte „Lokation/NeLo“ als auch in der Spalte „Verwendbar für Marktrolle/NB“ jeweils ein „X“ gesetzt ist und die Aussagen der Spalte „Erläuterung“ zu dem im DE7140 genannten Produkt-Code desselben PIA passen |
| **[197]** | Zulässig sind ausschließlich Codes aus der Spalte „Code“ der Codeliste der Verwendungszwecke (Kapitel 2), sofern in derselben Zeile sowohl in der Spalte „Lokation/NeLo“ als auch in der Spalte „Verwendbar für Marktrolle/LF“ jeweils ein „X“ gesetzt ist und die Aussagen der Spalte „Erläuterung“ zu dem im DE7140 genannten Produkt-Code desselben PIA passen |
| **[198]** | Zulässig sind ausschließlich Codes aus der Spalte „Code“ der Codeliste der Verwendungszwecke (Kapitel 2), sofern in derselben Zeile sowohl in der Spalte „Lokation/MaLo“ als auch in der Spalte „Verwendbar für Marktrolle/NB“ jeweils ein „X“ gesetzt ist und die Aussagen der Spalte „Erläuterung“ zu dem im DE7140 genannten Produkt-Code desselben PIA passen |
| **[199]** | Zulässig sind ausschließlich Codes aus der Spalte „Code“ der Codeliste der Verwendungszwecke (Kapitel 2), sofern in derselben Zeile sowohl in der Spalte „Lokation/MaLo“ als auch in der Spalte „Verwendbar für Marktrolle/LF“ jeweils ein „X“ gesetzt ist und die Aussagen der Spalte „Erläuterung“ zu dem im DE7140 genannten Produkt-Code desselben PIA passen |
| **[200]** | Zulässig sind ausschließlich Codes aus der Spalte „Code“ der Codeliste der Verwendungszwecke (Kapitel 2), sofern in derselben Zeile sowohl in der Spalte „Lokation/MaLo“ als auch in der Spalte „Verwendbar für Marktrolle/ÜNB“ jeweils ein „X“ gesetzt ist und die Aussagen der Spalte „Erläuterung“ zu dem im DE7140 genannten Produkt-Code desselben PIA passen |
| **[201]** | Zulässig sind ausschließlich Codes aus der Spalte „Code“ der Codeliste der Verwendungszwecke (Kapitel 2), sofern in derselben Zeile sowohl in der Spalte „Lokation/Tranche“ als auch in der Spalte „Verwendbar für Marktrolle/NB“ jeweils ein „X“ gesetzt ist und die Aussagen der Spalte „Erläuterung“ zu dem im DE7140 genannten Produkt-Code desselben PIA passen |
| **[202]** | Zulässig sind ausschließlich Codes aus der Spalte „Code“ der Codeliste der Verwendungszwecke (Kapitel 2), sofern in derselben Zeile sowohl in der Spalte „Lokation/Tranche“ als auch in der Spalte „Verwendbar für Marktrolle/LF“ jeweils ein „X“ gesetzt ist und die Aussagen der Spalte „Erläuterung“ zu dem im DE7140 genannten Produkt-Code desselben PIA passen |
| **[203]** | Zulässig sind ausschließlich Codes aus der Spalte „Code“ der Codeliste der Verwendungszwecke (Kapitel 2), sofern in derselben Zeile sowohl in der Spalte „Lokation/Tranche“ als auch in der Spalte „Verwendbar für Marktrolle/ÜNB“ jeweils ein „X“ gesetzt ist und die Aussagen der Spalte „Erläuterung“ zu dem im DE7140 genannten Produkt-Code desselben PIA passen |
| **[490]** | wenn Wert in diesem DE, an der Stelle CCYYMMDDHHMM ein Zeitpunkt aus dem angegeben Zeitraum der Tabelle Kapitel 3.5 „Übersicht gesetzliche deutsche Sommerzeit (MESZ)“ der Spalten: „Sommerzeit (MESZ) von“ Darstellung in UTC und „Sommerzeit (MESZ) bis“ Darstellung in UTC ist. |
| **[491]** | wenn Wert in diesem DE, an der Stelle CCYYMMDDHHMM ein Zeitpunkt aus dem angegeben Zeitraum der Tabelle Kapitel 3.6 „Übersicht gesetzliche deutsche Zeit (MEZ)“ der Spalten: „Winterzeit (MEZ) von“ Darstellung in UTC und „Winterzeit (MEZ) bis“ Darstellung in UTC ist. |
| **[492]** | Wenn MP-ID in NAD+MR aus Sparte Strom |
| **[493]** | Wenn MP-ID in NAD+MR aus Sparte Gas |
| **[494]** | Das hier genannte Datum muss der Zeitpunkt sein, zu dem das Dokument erstellt wurde, oder ein Zeitpunkt, der davor liegt. |
| **[495]** | Der Zeitpunkt muss ≤ dem Wert im DE2380 des DTM+137 sein |
| **[500]** | Hinweis: Zählpunkt der BAS |
| **[501]** | Hinweis: Zählpunkt der DZR |
| **[503]** | Hinweis: Angabe eines technischen Ansprechpartners für die Geräteübernahme |
| **[506]** | Hinweis: Datum, bis zu dem der MSBA zur Fortführung verpflichtet wird |
| **[514]** | Hinweis: Das Abonnement kann frühestens ab dem aktuellen Liefermonat beim Netzbetreiber gestartet werden. |
| **[515]** | Hinweis: Das angegebene Betrachtungszeitintervall bestimmt beim Start Abo bzw. Ende Abo ab bzw. bis wann (einschließlich) das Abo laufen soll. |
| **[517]** | Hinweis: Zählpunkt der LF-AASZR |
| **[518]** | Hinweis: Das angegebene Ausführungsdatum bestimmt beim Start Abo bzw. Ende Abo ab bzw. bis wann (einschließlich) das Abo laufen soll. |
| **[519]** | Hinweis: Bei Gas bezieht sich die Anforderung immer sowohl auf die vorläufigen Profilwerte als auch auf die endgültigen Profilwerte, falls diese bereits vorliegen. |
| **[521]** | Hinweis: Verwendung der ID der Marktlokation |
| **[522]** | Hinweis: Verwendung der ID der Messlokation |
| **[523]** | Hinweis: Verwendung der ID der Tranche |
| **[525]** | Hinweis: Wert aus BGM DE1004 der MSCONS |
| **[527]** | Hinweis: Zählpunkt der BG-SZR (Kategorie B) |
| **[530]** | Hinweis: Wert aus BGM+310 DE1004 der QUOTES mit der das Angebot erfolgt ist. |
| **[531]** | Hinweis: Wert aus LIN DE1082 der QUOTES, mit der das Angebot erfolgt ist |
| **[532]** | Hinweis: Wert aus BGM+Z29 DE1004 der QUOTES, mit der das Angebot zur Abrechnung des Messstellenbetriebs erfolgt ist. |
| **[533]** | Hinweis: Gerichtsvollzieher hat Termin vorgegeben |
| **[535]** | Hinweis: Verwendung der ID der Messlokation der Sparte Strom |
| **[536]** | Hinweis: Vorgangsnummer aus IDE DE7402 der UTILTS mit BGM+Z59 |
| **[539]** | Hinweis: Es sind nur Codes von Zählzeiten aus Liste des NB anzugeben |
| **[540]** | Hinweis: Es sind nur Codes von Zählzeiten aus Liste des LF anzugeben |
| **[542]** | Hinweis: Wert aus BGM+Z57 DE1004 der QUOTES mit der das Angebot erfolgt ist. |
| **[543]** | Hinweis: Wert aus BGM+Z57 DE1004 der ORDERS mit der die Bestellung der Werte erfolgt ist. |
| **[545]** | Hinweis: Es werden nur die Messprodukte der Messlokationen angegeben, die für die in der SG2 genannte Marktlokation bzw. deren Tranchen erforderlich sind. Messprodukte an der Messlokation für weitere Marktlokationen bleiben unverändert. |
| **[547]** | Hinweis: Dokumentennummer aus BGM+Z60 DE1004 der UTILTS |
| **[548]** | Hinweis: Wenn die Änderung der Gerätekonfiguration mit einer Zählzeit übermittelt wird, ist hier die MP-ID des Eigentümers der Liste der Zählzeit einzutragen. Wenn anstatt der bisherigen Zählzeit keine Zählzeit mehr verwendet werden soll ist hier die MP-ID des Eigentümers der Liste der Zählzeit einzutragen aus welcher bisher die Zählzeit verwendet wurde. |
| **[549]** | Hinweis: Findet bei der Reklamation von Zählerständen immer Anwendung. Einzige Ausnahme ist, wenn es sich um die Reklamation eines fehlenden Zählerstandes aufgrund einer Turnusablesung handelt, bei welcher der MSB am Objekt der Marktlokation die Information zur "geplanten Turnusablesung des MSB (Strom)" in der UTILMD im SG6 DTM+752 als Ablesezeitraum (DE2379 mit Code 104 MMWW-MMWW) in den vorherigen Stammdaten übermittelt hatte, denn dann ist keine Zeitpunktangabe möglich, sondern das Zeitintervall in der Segmentausprägung DTM+163 / DTM+164 zu verwenden. |
| **[550]** | Hinweis: Findet nur dann Anwendung, wenn es sich um die Reklamation eines fehlenden Zählerstandes aufgrund einer Turnusablesung handelt, bei welcher der MSB am Objekt der Marktlokation die Information zur "geplanten Turnusablesung des MSB (Strom)" in der UTILMD im SG6 DTM+752 als Ablesezeitraum (DE2379 mit Code 104 MMWW-MMWW) in den vorherigen Stammdaten übermittelt hatte. |
| **[551]** | Hinweis: Die SG29 ist so oft zu wiederholen, dass alle Messprodukte und Zählzeiten genannt werden, die ab dem in DTM+203 genannten Zeitpunkt auf der Messlokation durch den MSB konfiguriert werden müssen. Nicht genannte Messprodukte sind ab dem Zeitpunkt nicht mehr in der Konfiguration enthalten. |
| **[552]** | Hinweis: Verwendung der ID der Netzlokation |
| **[553]** | Hinweis: Verwendung der ID der Steuerbaren Ressource |
| **[554]** | Hinweis: Wert aus BGM+Z74 DE1004 der QUOTES mit der das Angebot erfolgt ist. |
| **[555]** | Hinweis: Vorgangsnummer aus SG4 IDE+24 DE7402 der UTILMD mit BGM+E01 mit der die Anmeldung des MSB-Wechsels erfolgt ist. |
| **[557]** | Hinweis: Es werden nur die Messprodukte der Messlokationen angegeben, die für die in der SG2 genannte Netzlokation erforderlich sind. Messprodukte an der Messlokation für weitere Netzlokationen oder Marktlokationen bleiben unverändert. |
| **[558]** | Hinweis: Dokumentennummer aus BGM+Z78 DE1004 der UTILTS |
| **[559]** | Hinweis: Dokumentennummer aus BGM+Z79 DE1004 der UTILTS |
| **[560]** | Hinweis: Vorgangsnummer aus IDE DE7402 der UTILTS mit BGM+Z80 |
| **[561]** | Hinweis: Vorgangsnummer aus IDE DE7402 der UTILTS mit BGM+Z81 |
| **[562]** | Hinweis: Wert aus BGM+Z73 DE1004 der IFTSTA mit der die Antwort auf die Bestellung der Konfiguration übermittelt wurde |
| **[563]** | Hinweis: Vorgangsnummer aus CNI DE1490 der IFTSTA mit BGM+Z73 mit der die Antwort auf die Bestellung der Konfiguration übermittelt wurde |
| **[564]** | Hinweis: Für den Empfang der Werte nach Typ 2 aus dem SMGW. |
| **[566]** | Hinweis: Verwendung der ID der Technischen Ressource |
| **[567]** | Hinweis: Es darf nur eine Information im DE3148 übermittelt werden |
| **[568]** | Hinweis: Wenn die Einrichtung der Konfiguration mit einer Zählzeit übermittelt wird, ist hier die MP-ID des NB als Eigentümer der Liste der Zählzeit einzutragen. |
| **[569]** | Hinweis: MaBiS-Zählpunkt der LF-SZR |
| **[570]** | Hinweis: zur Angabe von Kontaktdaten des Kunden des Lieferanten um die Änderung an der Technik zu vereinfachen. |
| **[571]** | Hinweis: MSB der Marktlokation, an den die Werte der weiteren Energieflussrichtung der Messlokation zu übermitteln sind. |
| **[572]** | Hinweis: MSB der Marktlokation der Kundenanlage, in der die betroffene Lokation integriert wird. |
| **[573]** | Hinweis: Es ist eine URI IPv4 für die Bereitstellung der Werte anzugeben. |
| **[574]** | Hinweis: Es ist eine URI IPv6 für die Bereitstellung der Werte anzugeben. |
| **[575]** | Hinweis: Wenn der gewünschte Änderungszeitpunkt ein fixer Zeitpunkt ist. |
| **[576]** | Hinweis: Wenn der gewünschte Änderungszeitpunkt ein nächst möglicher Termin zum oder nach dem angegebenen Zeitpunkt ist. |
| **[577]** | Hinweis: Wert aus BGM+Z93 (Bestellung eines Angebots Änderung der Technik der Lokation) DE1004 der QUOTES mit der das Angebot erfolgt ist. |
| **[578]** | Hinweis: Wert aus BGM DE1004 der PRICAT mit der das Preisblatt B des MSB, auf die aus Sicht des NB das Angebot basiert, übermittelt wurde. |
| **[579]** | Hinweis: Angabe des Beginnzeitpunkts des gewünschten Umsetzungstermins aus Sicht des Bestellers. |
| **[580]** | Hinweis: Angabe des Endezeitpunkts des gewünschten Umsetzungstermins aus Sicht des Bestellers. |
| **[591]** | Hinweis: Wenn es sich um die Bestellung eines vorherigen Angebots im Rahmen der BDEW Anwendungshilfe "Prozesse zur Änderung der Technik an Lokationen" handelt. |
| **[592]** | Hinweis: wenn es sich um die Beauftragung einer Änderung gemäß WiM Teil1 UC "Messlokationsänderung" handelt. |
| **[593]** | Hinweis: Daten des MSBN |
| **[594]** | Hinweis: Wenn die Aufteilung der Tranche prozentual erfolgt. |
| **[595]** | Hinweis: Wenn die Aufteilung auf Basis eines Aufteilungsfaktors wie z.B. der installierten Leistung auf Basis der Technischen Ressourcen erfolgt. Da die Berechnungsformel (UTILTS) derzeit nur für eine Marktlokation und nicht für eine Tranche ausgetauscht werden kann, ist ein bilateraler Austausch der Berechnungsformel initiiert vom NB an den MSB, notwendig. |
| **[903]** | Format: Möglicher Wert: 1 |
| **[906]** | Format: max. 3 Nachkommastellen |
| **[911]** | Format: Mögliche Werte: 1 bis n, je Nachricht oder Segmentgruppe bei 1 beginnend und fortlaufend aufsteigend |
| **[914]** | Format: Möglicher Wert: &gt;0 |
| **[922]** | Format: TR-ID |
| **[930]** | Format: max. 2 Nachkommastellen |
| **[931]** | Format: ZZZ = +00 |
| **[932]** | Format: HHMM = 2200 |
| **[933]** | Format: HHMM = 2300 |
| **[934]** | Format: HHMM = 0400 |
| **[935]** | Format: HHMM = 0500 |
| **[939]** | Format: Die Zeichenkette muss die Zeichen @ und . enthalten |
| **[940]** | Format: Die Zeichenkette muss mit dem Zeichen + beginnen und danach dürfen nur noch Ziffern folgen |
| **[950]** | Format: Marktlokations-ID |
| **[951]** | Format: Zählpunktbezeichnung |
| **[955]** | Format: Möglicher Wert: &lt;100 |
| **[960]** | Format: Netzlokations-ID |
| **[961]** | Format: SR-ID |
| **[962]** | Format: max. 6 Vorkommastellen |
| **[967]** | Format: Zertifikatskörper gemäß X509.1, BSI TR-03109-4 |
| **[2001]** | Die SG29 ist so oft zu wiederholen, wie ab dem DTM+203 (Ausführungsdatum) Tranchen zu der in der SG2 genannten Marktlokation vorhanden sind. |
| **[2002]** | Ist mindestens zwei Mal anzugeben |
| **[2003]** | Die SG29 ist so oft zu wiederholen, wie ab dem DTM+203 (Ausführungsdatum) Messlokationen zu der in der SG2 genannten Marktlokation vorhanden sind und für jede dieser Messlokationen müssen alle Messprodukte genannt sein, die ab dem DTM+203 (Ausführungsdatum) in der SG2 genannten Marktlokation bzw. deren Tranchen vorhanden sind. |
| **[2004]** | Die SG29 ist so oft zu wiederholen, dass alle Geräte der betroffenen Geräteart die im Rahmen des Gerätewechsels aufgrund MSB-Wechsel getauscht werden sollen genannt sind. |
| **[2005]** | Pro SG29 LIN ist die SG34 RFF+Z09 (Gerätenummer) genau einmal anzugeben |
| **[2006]** | Pro SG29 LIN ist die SG34 RFF+Z09 (Gerätenummer) bis zu dreimal anzugeben |
| **[2007]** | Die SG29 ist so oft zu wiederholen, wie ab dem DTM+203 (Ausführungsdatum) Messlokationen zu der in der SG2 genannten Netzlokation vorhanden sind und für jede dieser Messlokationen müssen alle Messprodukte genannt sein, die ab dem DTM+203 (Ausführungsdatum) in der SG2 genannten Netzlokation vorhanden sind. |
| **[2050]** | Pro Nachricht ist die SG29 genau einmal anzugeben |
| **[2060]** | Pro Nachricht ist die SG29 LIN+Z64 (Erforderliches Produkt Schaltzeitdefinitionen) maximal einmal anzugeben |
| **[2061]** | Pro Nachricht ist die SG29 LIN++Z65 (Erforderliches Produkt Leistungskurvendefinitionen) maximal einmal anzugeben |
| **[2062]** | Pro Nachricht ist die SG29 LIN++Z66 (Erforderliches Produkt Ad-hoc-Steuerkanal) maximal einmal anzugeben |
| **[2063]** | Pro Nachricht ist die SG29 LIN++Z67 (Erforderliches Messprodukt für Werte nach Typ 2 aus Backend) maximal einmal anzugeben |
| **[2064]** | Pro Nachricht ist die SG29 LIN++Z68 (Erforderliches Produkt Konfigurationserlaubnis für Werte nach Typ 2 aus SMGW) maximal einmal anzugeben |
| **[2065]** | Diese SG30 ist so oft zu wiederholen, wie zu den unterschiedlichen Messprodukt-Position-Codes zu dem innerhalb derselben SG29 LIN im PIA+5 DE7140 (Erforderliches Produkt Konfigurationserlaubnis für Werte nach Typ 2 aus SMGW) angegebenen Produkt ein Produkt angegeben ist, das in der Codeliste der Konfigurationen im Kapitel 4.4 „Messprodukte mit Konfigurationserlaubnis für Werte nach Typ 2 aus SMGW“ in der Spalte "Auslöser" mit dem Wert "Bei Schwellwertunter- / -überschreitung" gekennzeichnet ist. |
| **[2066]** | Die SG3 RFF+Z37 Referenz auf ID der Technischen Ressource ist so oft zu wiederholen, bis alle IDs der Technischen Ressourcen angegeben sind, die der Steuerbaren Ressource in LOC+172 DE3225 (Meldepunkt) mit diesem Vorgang zugeordnet werden sollen genannt sind. |
| **[2088]** | Die SG29 ist so oft zu wiederholen, dass alle Messprodukte ab dem DTM+203 (Ausführungsdatum) zu der in der SG2 genannten Netzlokation genannt sind. |
| **[2089]** | Die SG29 ist so oft zu wiederholen, dass alle Messprodukte ab dem DTM+203 (Ausführungsdatum) zu der in der SG2 genannten Marktlokation genannt sind. |
| **[2090]** | Für 33-stellige ID im SG2 LOC+172 (Meldepunkt) DE3225 mindestens einmal anzugeben |
| **[2092]** | Pro Nachricht ist die SG29 maximal einmal anzugeben |
| **[2094]** | Pro Nachricht ist die SG29 LIN (Positionsdaten) so oft anzugeben, wie Positionen aus dem Angebot, welches in SG1 RFF+AAG (Referenz Nachrichtennummer), DE1154 angegeben ist, bestellt werden sollen. |
| **[2095]** | Diese SG29 ist so oft zu wiederholen, dass alle Produkte zur Lokation die ab dem DTM+203 (Ausführungsdatum) gewünscht sind und deren Kombination gemäß Codeliste der Konfigurationen Kapitel 7 "Produkte zur Bestellung einer Änderung an einer Lokation"möglich sind, genannt sind. |
| **[2096]** | Die SG3 Referenz auf die ID der Tranche ist so oft zu wiederholen, wie ab dem DTM+203 (Ausführungsdatum) Tranchen zu der in der SG2 genannten Marktlokation vorhanden sind. |
| **[2097]** | Die SG29 ist so oft zu wiederholen, dass für alle in SG3 Referenz auf ID der Tranche genannten Tranchen mindestens eine SG29 vorhanden ist. |
| **[2098]** | Die SG2 Lieferant an der Lokation ist so oft zu wiederholen, dass für alle in SG3 Referenz auf ID der Tranche genannten Tranchen genau eine SG2 Lieferant der Lokation vorhanden ist. |
| **[2099]** | Die SG2 Lieferant an der Lokation ist genau einmal anzugeben. |

</div>

## UB-Bedingungen

UB-Bedingungen fassen mehrere Marken zu einem Ausdruck zusammen. Sie stehen in den Handbuchzeilen wie eine Bedingung, lösen sich aber in die Marken darin auf.

<div className="maco-tabellenrahmen">

| Marke | Ausdruck |
|---|---|
| **[UB1]** | ([931] ∧ [932] [490]) ⊻ ([931] ∧ [933] [491]) |
| **[UB2]** | ([931] ∧ [934] [490]) ⊻ ([931] ∧ [935] [491]) |
| **[UB3]** | ([931] ∧ [932] [492] ∧ [490]) ⊻ ([931] ∧ [933] [492] ∧ [491]) ⊻ ([931] ∧ [934] [493] ∧ [490]) ⊻ ([931] ∧ [935] [493] ∧ [491]) |

</div>

## Bedingungspakete

Bedingungspakete bündeln Voraussetzungen.

<div className="maco-tabellenrahmen">

| Paket | Voraussetzungen | Bedingungen |
|---|---|---|
| **[1P]** | -- | Hinweis: Das ist das Standardpaket, wenn keine Bedingung zum Tragen kommt, z. B. im COM-Segment. |
| **[2P]** | [28] | [28] Wenn MP-ID in SG2 NAD+MR aus Sparte Strom |
| **[3P]** | [29] | [29] Wenn MP-ID in SG2 NAD+MR aus Sparte Gas |

</div>

<Hinweisbereich>

Diese Seite führt den Klartext jeder Bedingung, auf die das Anwendungshandbuch des Nachrichtentyps **ORDERS** in dieser Formatversion verweist. Eine Zeile des Handbuchs schreibt `Muss [704]`; was [704] verlangt, steht hier.

Die Liste gilt **für den Nachrichtentyp**, nicht für einen einzelnen Prüfidentifikator. Das ist keine Vereinfachung, sondern die Form der Quelle: die Bedingungsliste liegt in jeder Handbuchdatei des Formats identisch vor.

:::caution{title="Warum hier keine Zuordnung zu einzelnen Prüfidentifikatoren steht"}

Das Zwischenformat, aus dem diese Dokumentation die Handbuchzeilen liest, ordnet Bedingungen einer **Spalte** zu — und diese Zuordnung ist gegen das Original verschoben. Gemessen am 05.09.2026 an UTILMD Strom: das Handbuch führt `STS DE9013` als `X [360]` (nur Zustimmungscodes) beim Prüfidentifikator **55017** und `X [359]` (nur Ablehnungscodes) bei **55018**; das Zwischenformat setzt `[360]` auf 55016 und `[359]` auf 55017 **und** 55018. Dasselbe bei `FTX Muss [83]`: im Handbuch bei 55018, im Zwischenformat bei 55017.

Unabhängig bestätigt durch die Änderungslisten der Quelle: die Änderungs-IDs 25242, 25821, 25822, 25445 und 25243 verorten [83], [351] und [352] ausdrücklich beim „Anwendungsfall 55018 Ablehnung Kündigung“. Kein Eintrag ordnet sie 55016 oder 55017 zu.

Deshalb steht hier der **Text** jeder Bedingung und nirgends die Behauptung, welche Bedingung für welchen Prüfidentifikator gilt. Wer das braucht, schlägt im Original-Anwendungshandbuch nach.

:::

:::note{title="9 Bedingungen stehen nicht in jeder Handbuchdatei"}

Die Bedingungsliste ist formatweit gemeint, ist es aber nicht überall: die folgenden Marken kommen in weniger als allen 44 Dateien dieses Formats vor. Sie stehen trotzdem hier — eine Bedingung wegzulassen, weil eine Datei sie nicht führt, hieße einen Verweis wieder ins Leere zeigen zu lassen.

[490], [491], [932], [933], [934], [935], [UB1], [UB2], [UB3]

:::

Gemessen am 05.09.2026 verweist **keine** `ahb_expression` dieser Quelle auf eine Paketmarke — die Bedingungspakete stehen auf dieser Seite, weil die Quelle sie führt, nicht weil eine Handbuchzeile auf sie zeigt.

</Hinweisbereich>
