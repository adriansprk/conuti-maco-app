# [MSB] START_VERSAND_RECHNUNG
<span hidden data-pagefind-meta={"title:Trigger-Ereignis START_VERSAND_RECHNUNG — Marktrolle MSB (FV 202610)"} />

Marktrolle **MSB** · Formatversion **202610** · BO4E-Schema **1.7.8**

## Stammdaten

Unter diesem Topic ist genau einer der folgenden 2 Prüfidentifikatoren zulässig — welcher, entscheidet der Event-Prozess.

| Prüfi | Scope | Anwendungsfall | Festlegung | Kommunikation |
|---|---|---|---|---|
| [PI_31003](/schnittstellen/202610/pruefi/INVOIC/PI_31003) | INVOIC | WiM-Rechnung | WiM Strom Teil 1 | MSB (entspricht MSBA am Objekt Messlokation) → MSB (entspricht MSBN am Objekt Messlokation oder gMSB am Objekt Messlokation) |
| [PI_31004](/schnittstellen/202610/pruefi/INVOIC/PI_31004) | INVOIC | Stornorechnung | Prozessbeschreibung zur Kapazitätsabrechnung an Ausspeisepunkten zu Letztverbrauchern | NB → TK (KN) |

Die Stammdaten der 2 Prüfidentifikatoren in **einer** Struktur — eine Spalte je Prüfidentifikator, wie im Anwendungshandbuch. Ein Wert in der Spalte heißt, dass das Feld zu diesem Prüfidentifikator gehört: **Muss**, wenn seine Spezifikation es verlangt, sonst **Kann**. Eine leere Zelle heißt »gehört nicht dazu«, nicht »unbekannt«. Vorausgewählt ist der erste; die übrigen schaltet die Leiste über der Tabelle zu.

<Handbuchsatz>

<div className="maco-tabellenrahmen">

| Struktur (BO4E) | Beschreibung | Format | <span className="hbs-p" title="WiM-Rechnung">31003</span> | <span className="hbs-p" title="Stornorechnung">31004</span> | Bedingung |
|---|---|---|---|---|---|
| <span className="hbs-g hbs-e0">**stammdaten**</span> | — | object | Kann | Kann | — |
| <span className="hbs-g hbs-e1">**MESSLOKATION** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | Kann | — |
| <span className="hbs-f hbs-e2">[messadresse](/bo4e/202610/bo/Messlokation#messadresse) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00010</span> | Die Adresse, an der die Messeinrichtungen zu finden sind.( Nur angeben, wenn<br/>diese von der Adresse der Marktlokation abweicht.)<br/>Achtung: Es darf immer nur eine Art der Ortsangabe vorhanden sein (entweder<br/>eine Adresse oder eine GeoKoordinate oder eine Katasteradresse. | [Adresse](/bo4e/202610/com/Adresse) | Muss | — | — |
| <span className="hbs-f hbs-e2">[messlokationsId](/bo4e/202610/bo/Messlokation#messlokationsid) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00020</span> | Die Messlokations-Identifikation. Das ist die frühere Zählpunktbezeichnung,<br/>z.B. DE 47108151234567 | string | Muss | Kann | — |
| <span className="hbs-g hbs-e1">**RECHNUNG** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | Muss | — |
| <span className="hbs-f hbs-e2">[ausfuehrungsdatum](/bo4e/202610/bo/Rechnung#ausfuehrungsdatum)</span><span className="hbs-nr">00030</span> | Das Datum an dem die Leistung erbracht wurde. | string (date-time) | Kann | Kann | — |
| <span className="hbs-f hbs-e2">[bearbeitungsdatum](/bo4e/202610/bo/Rechnung#bearbeitungsdatum) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00040</span> | bearbeitungsdatum | string (date-time) | Muss | Muss | — |
| <span className="hbs-f hbs-e2">[faelligkeitsdatum](/bo4e/202610/bo/Rechnung#faelligkeitsdatum) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00050</span> | Zu diesem Datum ist die Zahlung fällig. | string (date-time) | Muss | Muss | — |
| <span className="hbs-f hbs-e2">[istReverseCharge](/bo4e/202610/bo/Rechnung#istreversecharge)</span><span className="hbs-nr">00060</span> | Kennzeichen, ob bei der Rechnung das Reverse Charge verfahren angewendet wird | boolean | Kann | Kann | — |
| <span className="hbs-f hbs-e2">[rechnungsdatum](/bo4e/202610/bo/Rechnung#rechnungsdatum) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00070</span> | Ausstellungsdatum der Rechnung. | string (date-time) | Muss | Muss | — |
| <span className="hbs-f hbs-e2">[rechnungsstatus](/bo4e/202610/bo/Rechnung#rechnungsstatus) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00080</span> | Status der Rechnung zur Kennzeichnung des Bearbeitungsstandes. Details siehe ENUM Rechnungsstatus | [Enum Rechnungsstatus](/bo4e/202610/enum/Rechnungsstatus) | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`DUPLIKAT`</span> | — | — | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`ORIGINAL`</span> | — | — | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`STORNIERT`</span> | — | — | Muss | Muss | — |
| <span className="hbs-f hbs-e2">[rechnungstyp](/bo4e/202610/bo/Rechnung#rechnungstyp) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00090</span> | Ein kontextbezogender Rechnungstyp, z.B. Netznutzungsrechnung. Details siehe ENUM Rechnungstyp | [Enum Rechnungstyp](/bo4e/202610/enum/Rechnungstyp) | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`ABSCHLUSSRECHNUNG`</span> | — | — | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`ABSCHLAGSRECHNUNG`</span> | — | — | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`TURNUSRECHNUNG`</span> | — | — | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`MONATSRECHNUNG`</span> | — | — | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`WIMRECHNUNG`</span> | — | — | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`ZWISCHENRECHNUNG`</span> | — | — | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`INTEGRIERTE_13TE_RECHNUNG`</span> | — | — | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`ZUSAETZLICHE_13TE_RECHNUNG`</span> | — | — | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`MEHRMINDERMENGENRECHNUNG`</span> | — | — | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`MSBRECHNUNG`</span> | — | — | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`KAPAZITAETSRECHNUNG`</span> | — | — | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`SPERRUNG_INBETRIEBNAHME`</span> | — | — | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`VERZUGSKOSTEN`</span> | — | — | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`BLINDARBEIT`</span> | — | — | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`SONDERRECHNUNG`</span> | — | — | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`ABRECHNUNG_VON_KONFIGURATIONEN_UNIVERSALBESTELLPROZESS`</span> | — | — | Muss | Muss | — |
| <span className="hbs-w hbs-e3">`ABRECHNUNG_VON_TECHNIK`</span> | — | — | Muss | Muss | — |
| <span className="hbs-f hbs-e2">[referenzDokumentennummer](/bo4e/202610/bo/Rechnung#referenzdokumentennummer) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00100</span> | referenzDokumentennummer | string | Muss | — | — |
| <span className="hbs-g hbs-e2">**gesamtbrutto** <span className="hbs-pflicht">\*</span></span> | — | object | Muss | Muss | — |
| <span className="hbs-f hbs-e3">[wert](/bo4e/202610/com/Betrag#wert) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00110</span> | Gibt den Betrag des Preises an. | number (float) | Muss | Muss | — |
| <span className="hbs-g hbs-e2">**rechnungsperiode**</span> | — | object | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[enddatum](/bo4e/202610/com/Zeitraum#enddatum)</span><span className="hbs-nr">00120</span> | enddatum | string (date-time) | Kann | Kann | — |
| <span className="hbs-f hbs-e3">[startdatum](/bo4e/202610/com/Zeitraum#startdatum)</span><span className="hbs-nr">00130</span> | startdatum | string (date-time) | Kann | Kann | — |
| <span className="hbs-g hbs-e2">**rechnungspositionen** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | — | — |
| <span className="hbs-f hbs-e3">[artikelnummer](/bo4e/202610/com/Rechnungsposition#artikelnummer) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00140</span> | Kennzeichnung der Rechnungsposition mit der Standard-Artikelnummer des BDEW. Details<br/>BDEWArtikelnummer | string | Muss | — | — |
| <span className="hbs-f hbs-e3">[ausfuehrungsdatum](/bo4e/202610/com/Rechnungsposition#ausfuehrungsdatum)</span><span className="hbs-nr">00150</span> | Das Datum an dem die Leistung erbracht wurde. | string (date-time) | Kann | — | — |
| <span className="hbs-f hbs-e3">[lieferungBis](/bo4e/202610/com/Rechnungsposition#lieferungbis)</span><span className="hbs-nr">00160</span> | Ende der Lieferung für die abgerechnete Leistung. | string (date-time) | Kann | — | — |
| <span className="hbs-f hbs-e3">[lieferungVon](/bo4e/202610/com/Rechnungsposition#lieferungvon)</span><span className="hbs-nr">00170</span> | Start der Lieferung für die abgerechnete Leistung. | string (date-time) | Kann | — | — |
| <span className="hbs-f hbs-e3">[positionsnummer](/bo4e/202610/com/Rechnungsposition#positionsnummer) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00180</span> | Fortlaufende Nummer für die Rechnungsposition. | integer | Muss | — | — |
| <span className="hbs-g hbs-e3">**einzelpreis** <span className="hbs-pflicht">\*</span></span> | — | object | Muss | — | — |
| <span className="hbs-f hbs-e4">[bezugswert](/bo4e/202610/com/Preis#bezugswert)</span><span className="hbs-nr">00190</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202610/enum/Mengeneinheit) | Kann | — | — |
| <span className="hbs-w hbs-e5">`W`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`WH`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`KW`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`KWH`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`KVARH`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`MW`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`MWH`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`STUECK`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`KUBIKMETER`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`STUNDE`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`TAG`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`MONAT`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`JAHR`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`PROZENT`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`ANZAHL`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`VAR`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`KVAR`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`VARH`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`KWHK`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`Z16`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`KWT`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`WATT_PRO_QUADRATMETER`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`METER_PRO_SEKUNDE`</span> | — | — | Kann | — | — |
| <span className="hbs-f hbs-e4">[wert](/bo4e/202610/com/Preis#wert) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00200</span> | wert | number (float) | Muss | — | — |
| <span className="hbs-g hbs-e3">**positionsMenge** <span className="hbs-pflicht">\*</span></span> | — | object | Muss | — | — |
| <span className="hbs-f hbs-e4">[einheit](/bo4e/202610/com/Menge#einheit) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00210</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202610/enum/Mengeneinheit) | Muss | — | — |
| <span className="hbs-w hbs-e5">`W`</span> | — | — | Muss | — | — |
| <span className="hbs-w hbs-e5">`WH`</span> | — | — | Muss | — | — |
| <span className="hbs-w hbs-e5">`KW`</span> | — | — | Muss | — | — |
| <span className="hbs-w hbs-e5">`KWH`</span> | — | — | Muss | — | — |
| <span className="hbs-w hbs-e5">`KVARH`</span> | — | — | Muss | — | — |
| <span className="hbs-w hbs-e5">`MW`</span> | — | — | Muss | — | — |
| <span className="hbs-w hbs-e5">`MWH`</span> | — | — | Muss | — | — |
| <span className="hbs-w hbs-e5">`STUECK`</span> | — | — | Muss | — | — |
| <span className="hbs-w hbs-e5">`KUBIKMETER`</span> | — | — | Muss | — | — |
| <span className="hbs-w hbs-e5">`STUNDE`</span> | — | — | Muss | — | — |
| <span className="hbs-w hbs-e5">`TAG`</span> | — | — | Muss | — | — |
| <span className="hbs-w hbs-e5">`MONAT`</span> | — | — | Muss | — | — |
| <span className="hbs-w hbs-e5">`JAHR`</span> | — | — | Muss | — | — |
| <span className="hbs-w hbs-e5">`PROZENT`</span> | — | — | Muss | — | — |
| <span className="hbs-w hbs-e5">`ANZAHL`</span> | — | — | Muss | — | — |
| <span className="hbs-w hbs-e5">`VAR`</span> | — | — | Muss | — | — |
| <span className="hbs-w hbs-e5">`KVAR`</span> | — | — | Muss | — | — |
| <span className="hbs-w hbs-e5">`VARH`</span> | — | — | Muss | — | — |
| <span className="hbs-w hbs-e5">`KWHK`</span> | — | — | Muss | — | — |
| <span className="hbs-w hbs-e5">`Z16`</span> | — | — | Muss | — | — |
| <span className="hbs-w hbs-e5">`KWT`</span> | — | — | Muss | — | — |
| <span className="hbs-w hbs-e5">`WATT_PRO_QUADRATMETER`</span> | — | — | Muss | — | — |
| <span className="hbs-w hbs-e5">`METER_PRO_SEKUNDE`</span> | — | — | Muss | — | — |
| <span className="hbs-f hbs-e4">[wert](/bo4e/202610/com/Menge#wert) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00220</span> | Wert | number (float) | Muss | — | — |
| <span className="hbs-g hbs-e3">**teilsummeNetto** <span className="hbs-pflicht">\*</span></span> | — | object | Muss | — | — |
| <span className="hbs-f hbs-e4">[wert](/bo4e/202610/com/Betrag#wert) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00230</span> | Gibt den Betrag des Preises an. | number (float) | Muss | — | — |
| <span className="hbs-g hbs-e3">**teilsummeSteuer** <span className="hbs-pflicht">\*</span></span> | — | object | Muss | — | — |
| <span className="hbs-f hbs-e4">[steuerkennzeichen](/bo4e/202610/com/Steuerbetrag#steuerkennzeichen) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00240</span> | Kennzeichnung des Steuersatzes, bzw. Verfahrens. Details Steuerkennzeichen | string | Muss | — | — |
| <span className="hbs-g hbs-e3">**zeitbezogeneMenge**</span> | — | object | Kann | — | — |
| <span className="hbs-f hbs-e4">[einheit](/bo4e/202610/com/Menge#einheit)</span><span className="hbs-nr">00250</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202610/enum/Mengeneinheit) | Kann | — | — |
| <span className="hbs-w hbs-e5">`W`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`WH`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`KW`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`KWH`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`KVARH`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`MW`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`MWH`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`STUECK`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`KUBIKMETER`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`STUNDE`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`TAG`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`MONAT`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`JAHR`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`PROZENT`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`ANZAHL`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`VAR`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`KVAR`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`VARH`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`KWHK`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`Z16`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`KWT`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`WATT_PRO_QUADRATMETER`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e5">`METER_PRO_SEKUNDE`</span> | — | — | Kann | — | — |
| <span className="hbs-f hbs-e4">[wert](/bo4e/202610/com/Menge#wert)</span><span className="hbs-nr">00260</span> | Wert | number (float) | Kann | — | — |
| <span className="hbs-g hbs-e2">**steuerbetraege** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | Muss | — |
| <span className="hbs-f hbs-e3">[basiswert](/bo4e/202610/com/Steuerbetrag#basiswert) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00270</span> | Nettobetrag für den die Steuer berechnet wurde. Z.B. 200 | number (float) | Muss | Muss | — |
| <span className="hbs-f hbs-e3">[steuerkennzeichen](/bo4e/202610/com/Steuerbetrag#steuerkennzeichen) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00280</span> | Kennzeichnung des Steuersatzes, bzw. Verfahrens. Details Steuerkennzeichen | string | Muss | Muss | — |
| <span className="hbs-f hbs-e3">[steuerwert](/bo4e/202610/com/Steuerbetrag#steuerwert) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00290</span> | Aus dem Basiswert berechnete Steuer. Z.B. 38 (bei UST_19), falls Basiswert 200 ist. | number (float) | Muss | Muss | — |
| <span className="hbs-f hbs-e3">[basiswertVorausbezahlt](/bo4e/202610/com/Steuerbetrag#basiswertvorausbezahlt)</span><span className="hbs-nr">00300</span> | basiswertVorausbezahlt | number (float) | — | Kann | — |
| <span className="hbs-f hbs-e3">[steuerwertVorausbezahlt](/bo4e/202610/com/Steuerbetrag#steuerwertvorausbezahlt)</span><span className="hbs-nr">00310</span> | steuerwertVorausbezahlt | number (float) | — | Kann | — |
| <span className="hbs-g hbs-e2">**zuZahlen** <span className="hbs-pflicht">\*</span></span> | — | object | Muss | Muss | — |
| <span className="hbs-f hbs-e3">[wert](/bo4e/202610/com/Betrag#wert) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00320</span> | Gibt den Betrag des Preises an. | number (float) | Muss | Muss | — |
| <span className="hbs-f hbs-e2">[istSelbstausgestellt](/bo4e/202610/bo/Rechnung#istselbstausgestellt) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00330</span> | Kennzeichen, ob es sich um eine selbstausgestellte Rechnung handelt | boolean | — | Muss | — |
| <span className="hbs-f hbs-e2">[netzkonto](/bo4e/202610/bo/Rechnung#netzkonto)</span><span className="hbs-nr">00340</span> | netzkonto | string | — | Kann | — |
| <span className="hbs-f hbs-e2">[originalRechnungsnummer](/bo4e/202610/bo/Rechnung#originalrechnungsnummer) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00350</span> | Im Falle einer Stornorechnung (storno = true) steht hier die Rechnungsnummer der stornierten Rechnung. | string | — | Muss | — |
| <span className="hbs-f hbs-e2">[referenzNachrichtendatum](/bo4e/202610/bo/Rechnung#referenznachrichtendatum) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00360</span> | referenzNachrichtendatum | string | — | Muss | — |
| <span className="hbs-g hbs-e2">**gemeinderabatt**</span> | — | object | — | Kann | — |
| <span className="hbs-f hbs-e3">[wert](/bo4e/202610/com/Gemeinderabatt#wert)</span><span className="hbs-nr">00370</span> | Wert | number (float) | — | Kann | — |
| <span className="hbs-g hbs-e2">**vorausgezahlt**</span> | — | object | — | Kann | — |
| <span className="hbs-f hbs-e3">[wert](/bo4e/202610/com/Betrag#wert)</span><span className="hbs-nr">00380</span> | Gibt den Betrag des Preises an. | number (float) | — | Kann | — |
| <span className="hbs-g hbs-e2">**vorlaeufigerAbrechnungszeitraum**</span> | — | object | — | Kann | — |
| <span className="hbs-f hbs-e3">[enddatum](/bo4e/202610/com/Zeitraum#enddatum)</span><span className="hbs-nr">00390</span> | enddatum | string (date-time) | — | Kann | — |
| <span className="hbs-f hbs-e3">[startdatum](/bo4e/202610/com/Zeitraum#startdatum)</span><span className="hbs-nr">00400</span> | startdatum | string (date-time) | — | Kann | — |
| <span className="hbs-g hbs-e1">**MARKTLOKATION** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | Kann | — |
| <span className="hbs-f hbs-e2">[lokationsadresse](/bo4e/202610/bo/Marktlokation#lokationsadresse)</span><span className="hbs-nr">00410</span> | Die Adresse, an der die Energie-Lieferung oder -Einspeisung erfolgt. | [Adresse](/bo4e/202610/com/Adresse) | — | Kann | — |
| <span className="hbs-f hbs-e2">[marktlokationsId](/bo4e/202610/bo/Marktlokation#marktlokationsid)</span><span className="hbs-nr">00420</span> | Identifikationsnummer einer Marktlokation, an der Energie entweder<br/>verbraucht, oder erzeugt wird | string | — | Kann | — |
| <span className="hbs-g hbs-e1">**NETZLOKATION** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | Kann | — |
| <span className="hbs-f hbs-e2">[netzlokationsId](/bo4e/202610/bo/Netzlokation#netzlokationsid)</span><span className="hbs-nr">00430</span> | Identifikationsnummer einer Netzlokation, an der Energie entweder<br/>verbraucht, oder erzeugt wird (Like MarktlokationsId Marktlokation) | string | — | Kann | — |
| <span className="hbs-g hbs-e1">**STEUERBARE_RESSOURCE** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | Kann | — |
| <span className="hbs-f hbs-e2">[ressourcenId](/bo4e/202610/bo/SteuerbareRessource#ressourcenid)</span><span className="hbs-nr">00440</span> | ressourcenId | string | — | Kann | — |
| <span className="hbs-g hbs-e1">**TECHNISCHE_RESSOURCE** <span className="hbs-liste">[ ]</span></span> | — | object[] | — | Kann | — |
| <span className="hbs-f hbs-e2">[ressourcenId](/bo4e/202610/bo/TechnischeRessource#ressourcenid)</span><span className="hbs-nr">00450</span> | ressourcenId | string | — | Kann | — |

</div>

</Handbuchsatz>

## Kette dieses Auslösers

Das Ereignis löst die Nachricht aus. Der Marktpartner antwortet mit einer der genannten Antworten, und danach schreibt die MACO APP den Vorgang in Ihr Backendsystem.

| Nachricht | Antworten | Schreibaufruf nach der Antwort |
|---|---|---|
| [31003](/schnittstellen/202610/pruefi/INVOIC/PI_31003) | [33001](/schnittstellen/202610/pruefi/REMADV/PI_33001), [33002](/schnittstellen/202610/pruefi/REMADV/PI_33002), [33003](/schnittstellen/202610/pruefi/REMADV/PI_33003), [33004](/schnittstellen/202610/pruefi/REMADV/PI_33004) | `POST /updateProcessData` (abgeleitet) |
| [31004](/schnittstellen/202610/pruefi/INVOIC/PI_31004) | [33001](/schnittstellen/202610/pruefi/REMADV/PI_33001), [33002](/schnittstellen/202610/pruefi/REMADV/PI_33002) | `POST /updateProcessData` (abgeleitet) |

Dieses Ereignis löst Schritte in diesen Rollensichten aus:

| Prozess | Beteiligter | Regelwerk | Sparte |
|---|---|---|---|
| [Abrechnung Leistungen des Preisblatts B des MSB zwischen MSB und LF](/prozessdoku/202610/MSB/awh-prozesse-zur-anderung-der-technik-an-lokationen-abrechnung-leistungen-des-preisblatts-b-des-msb-zwischen-msb-und-lf) | MSB | AWH Prozesse zur Änderung der Technik an Lokationen | Strom |
| [Abrechnung Leistungen des Preisblatts B des MSB zwischen MSB und NB](/prozessdoku/202610/MSB/awh-prozesse-zur-anderung-der-technik-an-lokationen-abrechnung-leistungen-des-preisblatts-b-des-msb-zwischen-msb-und-nb) | MSB | AWH Prozesse zur Änderung der Technik an Lokationen | Strom |
| [Abrechnung von Dienstleistungen im Messwesen](/prozessdoku/202610/MSB--MSBA/awh-wim-gas-2-0-abrechnung-von-dienstleistungen-im-messwesen) | MSBA | AWH WiM Gas 2.0 | Gas |
| [Abrechnung Leistungen des Preisblatts A des MSB zwischen MSB und LF](/prozessdoku/202610/MSB/GPKE-Teil3-abrechnung-leistungen-des-preisblatts-a-des-msb-zwischen-msb-und-lf) | MSB | GPKE Teil 3 | Strom |
| [Abrechnung Leistungen des Preisblatts A des MSB zwischen MSB und NB](/prozessdoku/202610/MSB/GPKE-Teil3-abrechnung-leistungen-des-preisblatts-a-des-msb-zwischen-msb-und-nb) | MSB | GPKE Teil 3 | Strom |
| [Abrechnung Messstellenbetrieb gegenüber dem LF](/prozessdoku/202610/MSB/WiM-Teil1-abrechnung-messstellenbetrieb-gegenueber-dem-lf) | MSB-MALO | WiM Strom Teil 1 | Strom |
| [Abrechnung Messstellenbetrieb mit iMS gegenüber dem NB](/prozessdoku/202610/MSB/WiM-Teil1-abrechnung-messstellenbetrieb-mit-ims-gegenueber-dem-nb) | MSB-MALO | WiM Strom Teil 1 | Strom |
| [Abrechnung von Dienstleistungen](/prozessdoku/202610/MSB--MSBA/WiM-Teil1-abrechnung-von-dienstleistungen) | MSBA | WiM Strom Teil 1 | Strom |
| [Abrechnung einer für den ESA erbrachten Leistung](/prozessdoku/202610/MSB/WiM-Teil2-abrechnung-einer-fuer-den-esa-erbrachten-leistung) | MSB | WiM Strom Teil 2 | Strom |

## Transaktionsdaten

Der Umschlag der Nachricht. Pflichtfelder müssen beim Trigger-Aufruf gesetzt sein.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `pruefidentifikator` | — | nein | Wird dynamisch im Event-Prozess ermittelt (Entscheidungsgrundlage: rechnungstyp). Ein vom Sender mitgegebener Wert wird ignoriert. Im Topic mögliche Prüfis — 31003, 31004. Mögliche Werte: `31003`, `31004` |

## Zusatzdaten

`eventname` ist auf **START_VERSAND_RECHNUNG** festgelegt. Dieser Wert bleibt auch in der englischen Fassung deutsch, weil Camunda darüber korreliert.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `prozessId` | string | **ja** | — |
| `eventname` | const `START_VERSAND_RECHNUNG` | **ja** | — |

## Antwort

**Der Auslöser vergibt einen eigenen `businessKey`.** Die MACO APP übernimmt **weder** den `businessKey` **noch** die `prozessId` des aufrufenden Systems als Kennung der Prozessinstanz. Der `businessKey` der Antwort entsteht beim Start des Prozesses und ist neu. Der Rumpf dieses Aufrufs führt kein Feld `businessKey`; es gibt also keine Stelle, an der ein eigener Schlüssel mitgegeben werden könnte. Die mitgegebene `prozessId` (Pflichtfeld dieses Aufrufs) bleibt die Belegnummer des Backends: sie kommt in `zusatzdaten.prozessId` der Callbacks zurück — dort Pflicht nur bei MaloIdent (03002/03003), sonst optional.

**201 — Erfolg.** Erfolgsmeldung auf Prozessdaten API Aufruf.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `businessKey` | string (uuid) | **ja** | Einzigartige Kennung des Geschäftsprozesses |
| `message` | string | **ja** | Nachricht mit Details zum ausgelösten Event — Beispiel der Quelle: `received event XXXXXXXXXXXX with id at 2024-08-08T12:58:22Z and started process with businessKey 4c7170ed-3518-41ee-8582-39ab65b00107` |

**400 — Fehler.** Fehlermeldung auf Prozessdaten API Aufruf.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `errorCode` | string | nein | Error identifier — Beispiel der Quelle: `400` |
| `message` | string | nein | Technische Meldung — Beispiel der Quelle: `Validation Failed` |

Die Antwortschemata (`event_responses_success`, `event_response_fail`) stammen aus `macoapp-trigger.json`, Fassung 1.2.5 (20. Januar 2025), außerhalb der Zeitscheibe: die Datei wird nicht je Formatversion geführt, beide Fassungen lesen dieselbe.

Welchen Rumpf die Callbacks `updateProcessData` und `createProcessData` senden, ist am NiFi-Fluss der MACO APP gemessen: `{stammdaten, transaktionsdaten, zusatzdaten}` ohne Umschlag, der `businessKey` innerhalb von `zusatzdaten`. Nicht gemessen ist das an einem mitgeschnittenen Aufruf, und nicht für MaloIdent (03002/03003).

Was `businessKey`, `prozessId` und `targetBusinessKey` unterscheidet, steht auf [Schlüssel und Zuordnung](/schnittstellen/schluessel).
