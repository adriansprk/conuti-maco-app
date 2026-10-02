# Rechnungsposition
<span hidden data-pagefind-meta={"title:Rechnungsposition — BO4E-Komponente (FV 202610)"} />

BO4E-Komponente · 15 Felder · 45 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="einzelpreis"></a>`einzelpreis` | [Preis](/bo4e/202610/com/Preis) | Der Preis für eine Einheit der energetischen Menge. Details Preis |
| <a id="lieferungbis"></a>`lieferungBis` | string (date-time) | Ende der Lieferung für die abgerechnete Leistung. |
| <a id="lieferungvon"></a>`lieferungVon` | string (date-time) | Start der Lieferung für die abgerechnete Leistung. |
| <a id="positionsmenge"></a>`positionsMenge` | [Menge](/bo4e/202610/com/Menge) | Die abgerechnete Menge mit Einheit. Z.B. 4372 kWh. Details Menge |
| <a id="positionsnummer"></a>`positionsnummer` | integer | Fortlaufende Nummer für die Rechnungsposition. |
| <a id="artikelnummer"></a>`artikelnummer` | string | Kennzeichnung der Rechnungsposition mit der Standard-Artikelnummer des BDEW. Details BDEWArtikelnummer |
| <a id="teilsummenetto"></a>`teilsummeNetto` | [Betrag](/bo4e/202610/com/Betrag) | Das Ergebnis der Multiplikation aus einzelpreis * positionsMenge * (Faktor aus zeitbezogeneMenge). Z.B. 12,60€ * 120 kW * 3/12 (für 3 Monate). Details Betrag |
| <a id="teilsummesteuer"></a>`teilsummeSteuer` | [Steuerbetrag](/bo4e/202610/com/Steuerbetrag) | Auf die Position entfallende Steuer, bestehend aus Steuersatz und Betrag. Details Steuerbetrag |
| <a id="zeitbezogenemenge"></a>`zeitbezogeneMenge` | [Menge](/bo4e/202610/com/Menge) | Eine auf die Zeiteinheit bezogene Untermenge. Z.B. bei einem Jahrespreis, 3 Monate oder 146 Tage. Basierend darauf wird der Preis aufgeteilt. Details Menge |
| <a id="abschlag"></a>`abschlag` | [Abschlag](/bo4e/202610/com/Abschlag) | — |
| <a id="zuschlag"></a>`zuschlag` | [Zuschlag](/bo4e/202610/com/Zuschlag) | — |
| <a id="gemeinderabatt"></a>`gemeinderabatt` | [Gemeinderabatt](/bo4e/202610/com/Gemeinderabatt) | — |
| <a id="gesamtzuabschlagsbetrag"></a>`gesamtZuAbschlagsbetrag` | number (float) | gesamtZuAbschlagsbetrag |
| <a id="korrekturfaktor"></a>`korrekturfaktor` | number (float) | Gibt ggf. einen Korrekturfaktor für die Menge an. |
| <a id="ausfuehrungsdatum"></a>`ausfuehrungsdatum` | string (date-time) | Das Datum an dem die Leistung erbracht wurde. |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-g hbs-e0">[einzelpreis](/bo4e/202610/com/Rechnungsposition#einzelpreis)</span> | Der Preis für eine Einheit der energetischen Menge. Details Preis | [Preis](/bo4e/202610/com/Preis) |
| <span className="hbs-f hbs-e1">[wert](/bo4e/202610/com/Preis#wert)</span> | wert | number (float) |
| <span className="hbs-f hbs-e1">[menge](/bo4e/202610/com/Preis#menge)</span> | menge | integer |
| <span className="hbs-f hbs-e1">[minimaleMenge](/bo4e/202610/com/Preis#minimalemenge)</span> | minimale Menge | integer |
| <span className="hbs-f hbs-e1">[maximaleMenge](/bo4e/202610/com/Preis#maximalemenge)</span> | maximale Menge | integer |
| <span className="hbs-f hbs-e1">[einheit](/bo4e/202610/com/Preis#einheit)</span> | Waehrungseinheit | [Enum Waehrungseinheit](/bo4e/202610/enum/Waehrungseinheit)<br/><Werte>`EUR`, `CT`</Werte> |
| <span className="hbs-f hbs-e1">[bezugswert](/bo4e/202610/com/Preis#bezugswert)</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202610/enum/Mengeneinheit)<br/><Werte>`W`, `WH`, `KW`, `KWH`, `KVARH`, `MW`, `MWH`, `STUECK`, `KUBIKMETER`, `STUNDE`, `TAG`, `MONAT`, `JAHR`, `PROZENT`, `ANZAHL`, `VAR`, `KVAR`, `VARH`, `KWHK`, `Z16`, `KWT`, `WATT_PRO_QUADRATMETER`, `METER_PRO_SEKUNDE`</Werte> |
| <span className="hbs-f hbs-e1">[status](/bo4e/202610/com/Preis#status)</span> | Preisstatus | [Enum Preisstatus](/bo4e/202610/enum/Preisstatus)<br/><Werte>`VORLAEUFIG`, `ENDGUELTIG`</Werte> |
| <span className="hbs-f hbs-e1">[preisart](/bo4e/202610/com/Preis#preisart)</span> | Preisart Code | [Enum Preisart](/bo4e/202610/enum/Preisart)<br/><Werte>`EINRICHTUNGSPREIS`, `TRANSAKTIONSPREIS`, `BETRIEBSPREIS`</Werte> |
| <span className="hbs-f hbs-e0">[lieferungBis](/bo4e/202610/com/Rechnungsposition#lieferungbis)</span> | Ende der Lieferung für die abgerechnete Leistung. | string (date-time) |
| <span className="hbs-f hbs-e0">[lieferungVon](/bo4e/202610/com/Rechnungsposition#lieferungvon)</span> | Start der Lieferung für die abgerechnete Leistung. | string (date-time) |
| <span className="hbs-g hbs-e0">[positionsMenge](/bo4e/202610/com/Rechnungsposition#positionsmenge)</span> | Die abgerechnete Menge mit Einheit. Z.B. 4372 kWh. Details Menge | [Menge](/bo4e/202610/com/Menge) |
| <span className="hbs-f hbs-e1">[wert](/bo4e/202610/com/Menge#wert)</span> | Wert | number (float) |
| <span className="hbs-f hbs-e1">[einheit](/bo4e/202610/com/Menge#einheit)</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202610/enum/Mengeneinheit)<br/><Werte>`W`, `WH`, `KW`, `KWH`, `KVARH`, `MW`, `MWH`, `STUECK`, `KUBIKMETER`, `STUNDE`, `TAG`, `MONAT`, `JAHR`, `PROZENT`, `ANZAHL`, `VAR`, `KVAR`, `VARH`, `KWHK`, `Z16`, `KWT`, `WATT_PRO_QUADRATMETER`, `METER_PRO_SEKUNDE`</Werte> |
| <span className="hbs-f hbs-e1">[startdatum](/bo4e/202610/com/Menge#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e1">[enddatum](/bo4e/202610/com/Menge#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-f hbs-e0">[positionsnummer](/bo4e/202610/com/Rechnungsposition#positionsnummer)</span> | Fortlaufende Nummer für die Rechnungsposition. | integer |
| <span className="hbs-f hbs-e0">[artikelnummer](/bo4e/202610/com/Rechnungsposition#artikelnummer)</span> | Kennzeichnung der Rechnungsposition mit der Standard-Artikelnummer des BDEW. Details<br/>BDEWArtikelnummer | string |
| <span className="hbs-g hbs-e0">[teilsummeNetto](/bo4e/202610/com/Rechnungsposition#teilsummenetto)</span> | Das Ergebnis der Multiplikation aus einzelpreis * positionsMenge * (Faktor aus zeitbezogeneMenge). Z.B. 12,60€<br/>* 120 kW * 3/12 (für 3 Monate). Details Betrag | [Betrag](/bo4e/202610/com/Betrag) |
| <span className="hbs-f hbs-e1">[wert](/bo4e/202610/com/Betrag#wert)</span> | Gibt den Betrag des Preises an. | number (float) |
| <span className="hbs-f hbs-e1">[waehrung](/bo4e/202610/com/Betrag#waehrung)</span> | Währung des Preises | string |
| <span className="hbs-g hbs-e0">[teilsummeSteuer](/bo4e/202610/com/Rechnungsposition#teilsummesteuer)</span> | Auf die Position entfallende Steuer, bestehend aus Steuersatz und Betrag. Details Steuerbetrag | [Steuerbetrag](/bo4e/202610/com/Steuerbetrag) |
| <span className="hbs-f hbs-e1">[steuerkennzeichen](/bo4e/202610/com/Steuerbetrag#steuerkennzeichen)</span> | Kennzeichnung des Steuersatzes, bzw. Verfahrens. Details Steuerkennzeichen | string |
| <span className="hbs-f hbs-e1">[basiswert](/bo4e/202610/com/Steuerbetrag#basiswert)</span> | Nettobetrag für den die Steuer berechnet wurde. Z.B. 200 | number (float) |
| <span className="hbs-f hbs-e1">[steuerwert](/bo4e/202610/com/Steuerbetrag#steuerwert)</span> | Aus dem Basiswert berechnete Steuer. Z.B. 38 (bei UST_19), falls Basiswert 200 ist. | number (float) |
| <span className="hbs-f hbs-e1">[waehrung](/bo4e/202610/com/Steuerbetrag#waehrung)</span> | Währung. Z.B. Euro. | string |
| <span className="hbs-f hbs-e1">[basiswertVorausbezahlt](/bo4e/202610/com/Steuerbetrag#basiswertvorausbezahlt)</span> | basiswertVorausbezahlt | number (float) |
| <span className="hbs-f hbs-e1">[steuerwertVorausbezahlt](/bo4e/202610/com/Steuerbetrag#steuerwertvorausbezahlt)</span> | steuerwertVorausbezahlt | number (float) |
| <span className="hbs-g hbs-e0">[zeitbezogeneMenge](/bo4e/202610/com/Rechnungsposition#zeitbezogenemenge)</span> | Eine auf die Zeiteinheit bezogene Untermenge. Z.B. bei einem Jahrespreis, 3 Monate oder 146 Tage. Basierend<br/>darauf wird der Preis aufgeteilt. Details Menge | [Menge](/bo4e/202610/com/Menge) |
| <span className="hbs-f hbs-e1">[wert](/bo4e/202610/com/Menge#wert)</span> | Wert | number (float) |
| <span className="hbs-f hbs-e1">[einheit](/bo4e/202610/com/Menge#einheit)</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202610/enum/Mengeneinheit)<br/><Werte>`W`, `WH`, `KW`, `KWH`, `KVARH`, `MW`, `MWH`, `STUECK`, `KUBIKMETER`, `STUNDE`, `TAG`, `MONAT`, `JAHR`, `PROZENT`, `ANZAHL`, `VAR`, `KVAR`, `VARH`, `KWHK`, `Z16`, `KWT`, `WATT_PRO_QUADRATMETER`, `METER_PRO_SEKUNDE`</Werte> |
| <span className="hbs-f hbs-e1">[startdatum](/bo4e/202610/com/Menge#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e1">[enddatum](/bo4e/202610/com/Menge#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-g hbs-e0">[abschlag](/bo4e/202610/com/Rechnungsposition#abschlag)</span> | — | [Abschlag](/bo4e/202610/com/Abschlag) |
| <span className="hbs-f hbs-e1">[typ](/bo4e/202610/com/Abschlag#typ)</span> | AbschlagTyp | [Enum AbschlagTyp](/bo4e/202610/enum/AbschlagTyp)<br/><Werte>`GEMEINDERABATT_KAV`, `ANPASSUNG_P19_STROM_NEV`</Werte> |
| <span className="hbs-f hbs-e1">[prozent](/bo4e/202610/com/Abschlag#prozent)</span> | Prozentuale Angabe zum Auf-/Abschlag | number (float) |
| <span className="hbs-g hbs-e0">[zuschlag](/bo4e/202610/com/Rechnungsposition#zuschlag)</span> | — | [Zuschlag](/bo4e/202610/com/Zuschlag) |
| <span className="hbs-f hbs-e1">[typ](/bo4e/202610/com/Zuschlag#typ)</span> | ZuschlagTyp | [Enum ZuschlagTyp](/bo4e/202610/enum/ZuschlagTyp)<br/><Werte>`UMSPANNUNGSZUSCHLAG`, `BETRIEBSMITTEL_P19_STROM_NEV`, `ANPASSUNG_P19_STROM_NEV`, `ANPASSUNG_PAUSCHALE_NETZENTGELTREDUZIERUNG_NACH_P14A_ENWG_AUF_HOEHE_DER_NNE`</Werte> |
| <span className="hbs-f hbs-e1">[prozent](/bo4e/202610/com/Zuschlag#prozent)</span> | prozent | number (float) |
| <span className="hbs-g hbs-e0">[gemeinderabatt](/bo4e/202610/com/Rechnungsposition#gemeinderabatt)</span> | — | [Gemeinderabatt](/bo4e/202610/com/Gemeinderabatt) |
| <span className="hbs-f hbs-e1">[wert](/bo4e/202610/com/Gemeinderabatt#wert)</span> | Wert | number (float) |
| <span className="hbs-f hbs-e1">[einheit](/bo4e/202610/com/Gemeinderabatt#einheit)</span> | Einheit | string |
| <span className="hbs-f hbs-e1">[typ](/bo4e/202610/com/Gemeinderabatt#typ)</span> | Typ | string |
| <span className="hbs-f hbs-e1">[bemessungsgrundlage](/bo4e/202610/com/Gemeinderabatt#bemessungsgrundlage)</span> | Bemessungsgrundlage | number (float) |
| <span className="hbs-f hbs-e0">[gesamtZuAbschlagsbetrag](/bo4e/202610/com/Rechnungsposition#gesamtzuabschlagsbetrag)</span> | gesamtZuAbschlagsbetrag | number (float) |
| <span className="hbs-f hbs-e0">[korrekturfaktor](/bo4e/202610/com/Rechnungsposition#korrekturfaktor)</span> | Gibt ggf. einen Korrekturfaktor für die Menge an. | number (float) |
| <span className="hbs-f hbs-e0">[ausfuehrungsdatum](/bo4e/202610/com/Rechnungsposition#ausfuehrungsdatum)</span> | Das Datum an dem die Leistung erbracht wurde. | string (date-time) |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### lieferungBis

10 Verwendung(en) in den Nachrichtentypen INVOIC.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_31001](/schnittstellen/202610/pruefi/INVOIC/PI_31001) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen |
| [PI_31002](/schnittstellen/202610/pruefi/INVOIC/PI_31002) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen |
| [PI_31003](/schnittstellen/202610/pruefi/INVOIC/PI_31003) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen |
| [PI_31005](/schnittstellen/202610/pruefi/INVOIC/PI_31005) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen |
| [PI_31006](/schnittstellen/202610/pruefi/INVOIC/PI_31006) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen |
| [PI_31007](/schnittstellen/202610/pruefi/INVOIC/PI_31007) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen |
| [PI_31008](/schnittstellen/202610/pruefi/INVOIC/PI_31008) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen |
| [PI_31009](/schnittstellen/202610/pruefi/INVOIC/PI_31009) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen |
| [PI_31010](/schnittstellen/202610/pruefi/INVOIC/PI_31010) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen |
| [PI_31011](/schnittstellen/202610/pruefi/INVOIC/PI_31011) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen |

### lieferungVon

10 Verwendung(en) in den Nachrichtentypen INVOIC.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_31001](/schnittstellen/202610/pruefi/INVOIC/PI_31001) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen |
| [PI_31002](/schnittstellen/202610/pruefi/INVOIC/PI_31002) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen |
| [PI_31003](/schnittstellen/202610/pruefi/INVOIC/PI_31003) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen |
| [PI_31005](/schnittstellen/202610/pruefi/INVOIC/PI_31005) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen |
| [PI_31006](/schnittstellen/202610/pruefi/INVOIC/PI_31006) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen |
| [PI_31007](/schnittstellen/202610/pruefi/INVOIC/PI_31007) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen |
| [PI_31008](/schnittstellen/202610/pruefi/INVOIC/PI_31008) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen |
| [PI_31009](/schnittstellen/202610/pruefi/INVOIC/PI_31009) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen |
| [PI_31010](/schnittstellen/202610/pruefi/INVOIC/PI_31010) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen |
| [PI_31011](/schnittstellen/202610/pruefi/INVOIC/PI_31011) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen |

### positionsnummer

10 Verwendung(en) in den Nachrichtentypen INVOIC.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_31001](/schnittstellen/202610/pruefi/INVOIC/PI_31001) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen |
| [PI_31002](/schnittstellen/202610/pruefi/INVOIC/PI_31002) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen |
| [PI_31003](/schnittstellen/202610/pruefi/INVOIC/PI_31003) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen |
| [PI_31005](/schnittstellen/202610/pruefi/INVOIC/PI_31005) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen |
| [PI_31006](/schnittstellen/202610/pruefi/INVOIC/PI_31006) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen |
| [PI_31007](/schnittstellen/202610/pruefi/INVOIC/PI_31007) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen |
| [PI_31008](/schnittstellen/202610/pruefi/INVOIC/PI_31008) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen |
| [PI_31009](/schnittstellen/202610/pruefi/INVOIC/PI_31009) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen |
| [PI_31010](/schnittstellen/202610/pruefi/INVOIC/PI_31010) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen |
| [PI_31011](/schnittstellen/202610/pruefi/INVOIC/PI_31011) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen |

### artikelnummer

10 Verwendung(en) in den Nachrichtentypen INVOIC.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_31001](/schnittstellen/202610/pruefi/INVOIC/PI_31001) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen |
| [PI_31002](/schnittstellen/202610/pruefi/INVOIC/PI_31002) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen |
| [PI_31003](/schnittstellen/202610/pruefi/INVOIC/PI_31003) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen |
| [PI_31005](/schnittstellen/202610/pruefi/INVOIC/PI_31005) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen |
| [PI_31006](/schnittstellen/202610/pruefi/INVOIC/PI_31006) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen |
| [PI_31007](/schnittstellen/202610/pruefi/INVOIC/PI_31007) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen |
| [PI_31008](/schnittstellen/202610/pruefi/INVOIC/PI_31008) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen |
| [PI_31009](/schnittstellen/202610/pruefi/INVOIC/PI_31009) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen |
| [PI_31010](/schnittstellen/202610/pruefi/INVOIC/PI_31010) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen |
| [PI_31011](/schnittstellen/202610/pruefi/INVOIC/PI_31011) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen |

### gesamtZuAbschlagsbetrag

1 Verwendung(en) in den Nachrichtentypen INVOIC.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_31002](/schnittstellen/202610/pruefi/INVOIC/PI_31002) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen |

### korrekturfaktor

1 Verwendung(en) in den Nachrichtentypen INVOIC.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_31005](/schnittstellen/202610/pruefi/INVOIC/PI_31005) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen |

### ausfuehrungsdatum

3 Verwendung(en) in den Nachrichtentypen INVOIC.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_31003](/schnittstellen/202610/pruefi/INVOIC/PI_31003) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen |
| [PI_31009](/schnittstellen/202610/pruefi/INVOIC/PI_31009) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen |
| [PI_31011](/schnittstellen/202610/pruefi/INVOIC/PI_31011) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
