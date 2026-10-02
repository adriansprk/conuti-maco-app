# [MSB] START_ANGEBOT_GERAETEUEBERNAHME
<span hidden data-pagefind-meta={"title:Trigger-Ereignis START_ANGEBOT_GERAETEUEBERNAHME — Marktrolle MSB (FV 202610)"} />

Marktrolle **MSB** · Formatversion **202610** · BO4E-Schema **1.7.8**

## Stammdaten

Unter diesem Topic ist genau einer der folgenden 1 Prüfidentifikatoren zulässig — welcher, entscheidet der Event-Prozess.

| Prüfi | Scope | Anwendungsfall | Festlegung | Kommunikation |
|---|---|---|---|---|
| [PI_15001](/schnittstellen/202610/pruefi/QUOTES/PI_15001) | QUOTES | Angebot Geräteübernahme | WiM Strom Teil 1 | MSB (entspricht MSBA am Objekt Messlokation) → MSB (entspricht MSBN am Objekt Messlokation) |

Die Stammdaten der 1 Prüfidentifikatoren in **einer** Struktur — eine Spalte je Prüfidentifikator, wie im Anwendungshandbuch. Ein Wert in der Spalte heißt, dass das Feld zu diesem Prüfidentifikator gehört: **Muss**, wenn seine Spezifikation es verlangt, sonst **Kann**. Eine leere Zelle heißt »gehört nicht dazu«, nicht »unbekannt«. Vorausgewählt ist der erste; die übrigen schaltet die Leiste über der Tabelle zu.

<Handbuchsatz>

<div className="maco-tabellenrahmen">

| Struktur (BO4E) | Beschreibung | Format | <span className="hbs-p" title="Angebot Geräteübernahme">15001</span> | Bedingung |
|---|---|---|---|---|
| <span className="hbs-g hbs-e0">**stammdaten**</span> | — | object | Kann | — |
| <span className="hbs-g hbs-e1">**ANFRAGE** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | — |
| <span className="hbs-f hbs-e2">[anfragetyp](/bo4e/202610/bo/Anfrage#anfragetyp) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00010</span> | Typ/Art der Anfrage (ORDERS ORDRSP IMD 7081) | [Enum Anfragetyp](/bo4e/202610/enum/Anfragetyp) | Muss | — |
| <span className="hbs-w hbs-e3">`KAUF`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`NUTZUNGSUEBERLASSUNG`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`ABRECHNUNGSBRENNWERT_UND_ZUSTANDSZAHL`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`LASTGANGDATEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`ZAEHLERSTAENDE`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`WERTEERMITTLUNG`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`ENERGIEMENGE_EINZELWERT`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`INNERHALB_DER_ARBEITSZEIT`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`AUCH_AUSSERHALB_DER_ARBEITSZEIT`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`WECHSEL_SAEMTLICHER_EINRICHTUNGEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`TEILWEISER_WECHSEL`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`AENDERUNG_ZAEHLZEITDEFINITION`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`ABBESTELLUNG_ZAEHLZEITEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`ABBESTELLUNG_MESSPRODUKT`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`ANGEBOT_AUF_BASIS_PREISBLATT`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`INDIVIDUELLES_ANGEBOT`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`AENDERUNG_KONFIGURATION`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`KANN_NICHT_ANGEBOTEN_WERDEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`NEUKONFIGURATION`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`BEENDIGUNG_KONFIGURATION`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e3">`AKTIVIERUNG_KONFIGURATION`</span> | — | — | Muss | — |
| <span className="hbs-g hbs-e1">**ANGEBOT** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | — |
| <span className="hbs-f hbs-e2">[anfragereferenz](/bo4e/202610/bo/Angebot#anfragereferenz) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00020</span> | Referenz auf eine Anfrage oder Ausschreibung. Kann dem Empfänger des Angebotes bei Zuordnung des Angebotes zur Anfrage bzw.Ausschreibung helfen. | string | Muss | — |
| <span className="hbs-f hbs-e2">[angebotsdatum](/bo4e/202610/bo/Angebot#angebotsdatum) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00030</span> | Erstellungsdatum des Angebots | string (date-time) | Muss | — |
| <span className="hbs-g hbs-e2">**positionsdaten** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | — |
| <span className="hbs-f hbs-e3">[anbietbar](/bo4e/202610/com/Angebotsposition#anbietbar)</span><span className="hbs-nr">00040</span> | — | boolean | Kann | — |
| <span className="hbs-f hbs-e3">[artikelnummer](/bo4e/202610/com/Angebotsposition#artikelnummer) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00050</span> | BDEW Artikelnummer | [Enum BDEWArtikelnummer](/bo4e/202610/enum/BDEWArtikelnummer) | Muss | — |
| <span className="hbs-w hbs-e4">`LEISTUNG`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`LEISTUNG_PAUSCHAL`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`GRUNDPREIS`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`REGELENERGIE_ARBEIT`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`REGELENERGIE_LEISTUNG`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`NOTSTROMLIEFERUNG_ARBEIT`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`NOTSTROMLIEFERUNG_LEISTUNG`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`RESERVENETZKAPAZITAET`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`RESERVELEISTUNG`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`ZUSAETZLICHE_ABLESUNG`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`PRUEFGEBUEHREN_AUSSERPLANMAESSIG`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`WIRKARBEIT`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`SINGULAER_GENUTZTE_BETRIEBSMITTEL`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`ABGABE_KWKG`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`ABSCHLAG`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`KONZESSIONSABGABE`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`ENTGELT_FERNAUSLESUNG`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`UNTERMESSUNG`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`BLINDMEHRARBEIT`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`ENTGELT_ABRECHNUNG`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`SPERRKOSTEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`ENTSPERRKOSTEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`MAHNKOSTEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`MEHR_MINDERMENGEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`INKASSOKOSTEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`BLINDMEHRLEISTUNG`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`ENTGELT_MESSUNG_ABLESUNG`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`ENTGELT_EINBAU_BETRIEB_WARTUNG_MESSTECHNIK`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`AUSGLEICHSENERGIE`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`AUSGLEICHSENERGIE_UNTERDECKUNG`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`ZAEHLEINRICHTUNG`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`WANDLER_MENGENUMWERTER`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`KOMMUNIKATIONSEINRICHTUNG`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`TECHNISCHE_STEUEREINRICHTUNG`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`PARAGRAF_19_STROM_NEV_UMLAGE`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`BEFESTIGUNGSEINRICHTUNG`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`OFFSHORE_HAFTUNGSUMLAGE`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`FIXE_ARBEITSENTGELTKOMPONENTE`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`FIXE_LEISTUNGSENTGELTKOMPONENTE`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`UMLAGE_ABSCHALTBARE_LASTEN`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`MEHRMENGE`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`MINDERMENGE`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`ENERGIESTEUER`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`SMARTMETER_GATEWAY`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`STEUERBOX`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`MSB_INKL_MESSUNG`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_2_1_MSBG`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_2_2_MSBG`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_2_3_MSBG`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_2_4_MSBG`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_2_5_MSBG`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_3_MSBG`</span> | — | — | Muss | — |
| <span className="hbs-w hbs-e4">`ENTGELT_KAPAZITAETEN`</span> | — | — | Muss | — |
| <span className="hbs-f hbs-e3">[freitext](/bo4e/202610/com/Angebotsposition#freitext)</span><span className="hbs-nr">00060</span> | Zusätzliche Informationen (für allgemeine Hinweise) | string | Kann | — |
| <span className="hbs-f hbs-e3">[positionsbezeichnung](/bo4e/202610/com/Angebotsposition#positionsbezeichnung) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00070</span> | Bezeichnung der Position | string | Muss | — |
| <span className="hbs-g hbs-e3">**beteiligterMarktpartner**</span> | — | object | Kann | — |
| <span className="hbs-f hbs-e4">[rollencodenummer](/bo4e/202610/bo/Marktteilnehmer#rollencodenummer)</span><span className="hbs-nr">00080</span> | Gibt die Codenummer der Marktrolle an. | string | Kann | — |
| <span className="hbs-f hbs-e4">[rollencodetyp](/bo4e/202610/bo/Marktteilnehmer#rollencodetyp)</span><span className="hbs-nr">00090</span> | Gibt den Typ des Codes an. | [Enum Rollencodetyp](/bo4e/202610/enum/Rollencodetyp) | Kann | — |
| <span className="hbs-w hbs-e5">`BDEW`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GS1`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GLN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`DVGW`</span> | — | — | Kann | — |
| <span className="hbs-g hbs-e3">**positionspreis** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-f hbs-e4">[bezugswert](/bo4e/202610/com/Preis#bezugswert)</span><span className="hbs-nr">00100</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202610/enum/Mengeneinheit) | Kann | — |
| <span className="hbs-w hbs-e5">`W`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`WH`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`KW`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`KWH`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`KVARH`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MW`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MWH`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`STUECK`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`KUBIKMETER`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`STUNDE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`TAG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MONAT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`JAHR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`PROZENT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`ANZAHL`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`VAR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`KVAR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`VARH`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`KWHK`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`Z16`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`KWT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`WATT_PRO_QUADRATMETER`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`METER_PRO_SEKUNDE`</span> | — | — | Kann | — |
| <span className="hbs-f hbs-e4">[menge](/bo4e/202610/com/Preis#menge)</span><span className="hbs-nr">00110</span> | menge | integer | Kann | — |
| <span className="hbs-f hbs-e4">[wert](/bo4e/202610/com/Preis#wert)</span><span className="hbs-nr">00120</span> | wert | number (float) | Kann | — |
| <span className="hbs-g hbs-e3">**verweisKatalognummer**</span> | — | object | Kann | — |
| <span className="hbs-f hbs-e4">[katalognummer](/bo4e/202610/com/Katalogverweis#katalognummer)</span><span className="hbs-nr">00130</span> | Katalognummer | string | Kann | — |
| <span className="hbs-f hbs-e4">[versionsnummer](/bo4e/202610/com/Katalogverweis#versionsnummer)</span><span className="hbs-nr">00140</span> | Versionsnummer | string | Kann | — |
| <span className="hbs-f hbs-e4">[zeilennummer](/bo4e/202610/com/Katalogverweis#zeilennummer)</span><span className="hbs-nr">00150</span> | Zeilennummer | string | Kann | — |
| <span className="hbs-g hbs-e1">**MESSLOKATION** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | — |
| <span className="hbs-f hbs-e2">[messlokationsId](/bo4e/202610/bo/Messlokation#messlokationsid) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00160</span> | Die Messlokations-Identifikation. Das ist die frühere Zählpunktbezeichnung,<br/>z.B. DE 47108151234567 | string | Muss | — |
| <span className="hbs-g hbs-e1">**ZAEHLER** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-f hbs-e2">[befestigungsart](/bo4e/202610/bo/Zaehler#befestigungsart)</span><span className="hbs-nr">00170</span> | Befestigungsart | [Enum Befestigungsart](/bo4e/202610/enum/Befestigungsart) | Kann | — |
| <span className="hbs-w hbs-e3">`STECKTECHNIK`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`DREIPUNKT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`HUTSCHIENE`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`EINSTUTZEN`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`ZWEISTUTZEN`</span> | — | — | Kann | — |
| <span className="hbs-f hbs-e2">[eichungBis](/bo4e/202610/bo/Zaehler#eichungbis)</span><span className="hbs-nr">00180</span> | Bis zu diesem Datum ist der Zähler geeicht. | string | Kann | — |
| <span className="hbs-f hbs-e2">[messwerterfassung](/bo4e/202610/bo/Zaehler#messwerterfassung)</span><span className="hbs-nr">00190</span> | Messwerterfassung am Zählpunkt | [Enum Messwerterfassung](/bo4e/202610/enum/Messwerterfassung) | Kann | — |
| <span className="hbs-w hbs-e3">`FERNAUSLESBAR`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`MANUELL_AUSGELESENE`</span> | — | — | Kann | — |
| <span className="hbs-f hbs-e2">[tarifart](/bo4e/202610/bo/Zaehler#tarifart)</span><span className="hbs-nr">00200</span> | Spezifikation bezüglich unterstützter Tarifarten. | [Enum Tarifart](/bo4e/202610/enum/Tarifart) | Kann | — |
| <span className="hbs-w hbs-e3">`EINTARIF`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`ZWEITARIF`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`MEHRTARIF`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`SMART_METER`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`LEISTUNGSGEMESSEN`</span> | — | — | Kann | — |
| <span className="hbs-f hbs-e2">[zaehlerauspraegung](/bo4e/202610/bo/Zaehler#zaehlerauspraegung)</span><span className="hbs-nr">00210</span> | Spezifikation die Richtung des Zählers betreffend. | [Enum Zaehlerauspraegung](/bo4e/202610/enum/Zaehlerauspraegung) | Kann | — |
| <span className="hbs-w hbs-e3">`EINRICHTUNGSZAEHLER`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`ZWEIRICHTUNGSZAEHLER`</span> | — | — | Kann | — |
| <span className="hbs-f hbs-e2">[zaehlergroesse](/bo4e/202610/bo/Zaehler#zaehlergroesse)</span><span className="hbs-nr">00220</span> | Zaehlergroesse | [Enum Geraetemerkmal](/bo4e/202610/enum/Geraetemerkmal) | Kann | — |
| <span className="hbs-w hbs-e3">`EINTARIF`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`ZWEITARIF`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`MEHRTARIF`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`GAS_G2P5`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`GAS_G4`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`GAS_G6`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`GAS_G10`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`GAS_G16`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`GAS_G25`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`GAS_G40`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`GAS_G65`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`GAS_G100`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`GAS_G160`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`GAS_G250`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`GAS_G350`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`GAS_G400`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`GAS_G4000`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`GAS_G650`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`GAS_G6500`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`GAS_G1000`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`GAS_G10000`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`GAS_G12500`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`GAS_G1600`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`GAS_G16000`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`GAS_G2500`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`IMPULSGEBER_G4_G100`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`IMPULSGEBER_G100`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`MODEM_GSM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`MODEM_GPRS`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`MODEM_FUNK`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`MODEM_GSM_O_LG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`MODEM_GSM_M_LG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`MODEM_FESTNETZ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`MODEM_GPRS_M_LG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`PLC_COM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`ETHERNET_KOM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`DSL_KOM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`LTE_KOM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`RUNDSTEUEREMPFAENGER`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`TARIFSCHALTGERAET`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`ZUSTANDS_MU`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`TEMPERATUR_MU`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`KOMPAKT_MU`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`SYSTEM_MU`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`UNBESTIMMT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`WASSER_MWZW`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`WASSER_WZWW`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`WASSER_WZ01`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`WASSER_WZ02`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`WASSER_WZ03`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`WASSER_WZ04`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`WASSER_WZ05`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`WASSER_WZ06`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`WASSER_WZ07`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`WASSER_WZ08`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`WASSER_WZ09`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`WASSER_WZ10`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`WASSER_VWZ04`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`WASSER_VWZ05`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`WASSER_VWZ06`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`WASSER_VWZ07`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`WASSER_VWZ10`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`DICHTEMENGENUMWERTER`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`TEMPERATURMENGENUMWERTER`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`ZUSTANDSMENGENUMWERTER`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`BLOCKSTROMWANDLER`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`MESSWANDLERSATZ_IMS_MME`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`KOMBIMESSWANDLER`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`SPANNUNGSWANDLER`</span> | — | — | Kann | — |
| <span className="hbs-f hbs-e2">[zaehlertyp](/bo4e/202610/bo/Zaehler#zaehlertyp)</span><span className="hbs-nr">00230</span> | Typisierung des Zählers | [Enum Zaehlertyp](/bo4e/202610/enum/Zaehlertyp) | Kann | — |
| <span className="hbs-w hbs-e3">`DREHSTROMZAEHLER`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`BALGENGASZAEHLER`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`DREHKOLBENZAEHLER`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`SMARTMETER`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`LEISTUNGSZAEHLER`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`MAXIMUMZAEHLER`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`TURBINENRADGASZAEHLER`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`ULTRASCHALLGASZAEHLER`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`WECHSELSTROMZAEHLER`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`WIRBELGASZAEHLER`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`MESSDATENREGISTRIERGERAET`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`ELEKTRONISCHERHAUSHALTSZAEHLER`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`SONDERAUSSTATTUNG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`WASSERZAEHLER`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`MODERNEMESSEINRICHTUNG`</span> | — | — | Kann | — |
| <span className="hbs-f hbs-e2">[zaehlertypspezifikation](/bo4e/202610/bo/Zaehler#zaehlertypspezifikation)</span><span className="hbs-nr">00240</span> | Typisierung des Zählers (spezifikation für EHZ und MME) | [Enum ZaehlertypSpezifikation](/bo4e/202610/enum/ZaehlertypSpezifikation) | Kann | — |
| <span className="hbs-w hbs-e3">`EDL40`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`EDL21`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`SONSTIGER_EHZ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`MME_STANDARD`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e3">`MME_MEDA`</span> | — | — | Kann | — |
| <span className="hbs-g hbs-e2">**geraete** <span className="hbs-liste">[ ]</span></span> | — | object[] | Kann | — |
| <span className="hbs-g hbs-e3">**geraeteeigenschaften**</span> | — | object | Kann | — |
| <span className="hbs-f hbs-e4">[faktor](/bo4e/202610/com/Geraeteeigenschaften#faktor)</span><span className="hbs-nr">00250</span> | faktor | number (float) | Kann | — |
| <span className="hbs-f hbs-e4">[firmwareVersion](/bo4e/202610/com/Geraeteeigenschaften#firmwareversion)</span><span className="hbs-nr">00260</span> | Firmware-Version | string | Kann | — |
| <span className="hbs-f hbs-e4">[geraetemerkmal](/bo4e/202610/com/Geraeteeigenschaften#geraetemerkmal)</span><span className="hbs-nr">00270</span> | Geraetemerkmal | [Enum Geraetemerkmal](/bo4e/202610/enum/Geraetemerkmal) | Kann | — |
| <span className="hbs-w hbs-e5">`EINTARIF`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`ZWEITARIF`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MEHRTARIF`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GAS_G2P5`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GAS_G4`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GAS_G6`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GAS_G10`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GAS_G16`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GAS_G25`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GAS_G40`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GAS_G65`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GAS_G100`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GAS_G160`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GAS_G250`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GAS_G350`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GAS_G400`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GAS_G4000`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GAS_G650`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GAS_G6500`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GAS_G1000`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GAS_G10000`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GAS_G12500`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GAS_G1600`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GAS_G16000`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`GAS_G2500`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`IMPULSGEBER_G4_G100`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`IMPULSGEBER_G100`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MODEM_GSM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MODEM_GPRS`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MODEM_FUNK`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MODEM_GSM_O_LG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MODEM_GSM_M_LG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MODEM_FESTNETZ`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MODEM_GPRS_M_LG`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`PLC_COM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`ETHERNET_KOM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`DSL_KOM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`LTE_KOM`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`RUNDSTEUEREMPFAENGER`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`TARIFSCHALTGERAET`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`ZUSTANDS_MU`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`TEMPERATUR_MU`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`KOMPAKT_MU`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`SYSTEM_MU`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`UNBESTIMMT`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`WASSER_MWZW`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`WASSER_WZWW`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`WASSER_WZ01`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`WASSER_WZ02`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`WASSER_WZ03`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`WASSER_WZ04`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`WASSER_WZ05`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`WASSER_WZ06`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`WASSER_WZ07`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`WASSER_WZ08`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`WASSER_WZ09`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`WASSER_WZ10`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`WASSER_VWZ04`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`WASSER_VWZ05`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`WASSER_VWZ06`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`WASSER_VWZ07`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`WASSER_VWZ10`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`DICHTEMENGENUMWERTER`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`TEMPERATURMENGENUMWERTER`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`ZUSTANDSMENGENUMWERTER`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`BLOCKSTROMWANDLER`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`MESSWANDLERSATZ_IMS_MME`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`KOMBIMESSWANDLER`</span> | — | — | Kann | — |
| <span className="hbs-w hbs-e5">`SPANNUNGSWANDLER`</span> | — | — | Kann | — |
| <span className="hbs-f hbs-e4">[herstellerTypbezeichnung](/bo4e/202610/com/Geraeteeigenschaften#herstellertypbezeichnung)</span><span className="hbs-nr">00280</span> | Hersteller-Typbezeichnung | string | Kann | — |
| <span className="hbs-f hbs-e4">[ipVersion](/bo4e/202610/com/Geraeteeigenschaften#ipversion)</span><span className="hbs-nr">00290</span> | IP-Version | string | Kann | — |
| <span className="hbs-f hbs-e4">[modemKennungIMSI](/bo4e/202610/com/Geraeteeigenschaften#modemkennungimsi)</span><span className="hbs-nr">00300</span> | Modem-Kennung (IMSI) | string | Kann | — |
| <span className="hbs-f hbs-e4">[simKartenNummer](/bo4e/202610/com/Geraeteeigenschaften#simkartennummer)</span><span className="hbs-nr">00310</span> | SIM-Kartennummer | string | Kann | — |
| <span className="hbs-f hbs-e4">[tkProvider](/bo4e/202610/com/Geraeteeigenschaften#tkprovider)</span><span className="hbs-nr">00320</span> | Telekommunikationsanbieter | string | Kann | — |

</div>

</Handbuchsatz>

## Kette dieses Auslösers

Das Ereignis löst die Nachricht aus.

| Nachricht | Antworten | Schreibaufruf nach der Antwort |
|---|---|---|
| [15001](/schnittstellen/202610/pruefi/QUOTES/PI_15001) | — | — |

Dieses Ereignis löst Schritte in diesen Rollensichten aus:

| Prozess | Beteiligter | Regelwerk | Sparte |
|---|---|---|---|
| [Geräteübernahme](/prozessdoku/202610/MSB--MSBA/awh-wim-gas-2-0-gerateubernahme) | MSBA | AWH WiM Gas 2.0 | Gas |
| [Geräteübernahme](/prozessdoku/202610/MSB--MSBA/WiM-Teil1-geraeteuebernahme) | MSBA | WiM Strom Teil 1 | Strom |

## Transaktionsdaten

Der Umschlag der Nachricht. Pflichtfelder müssen beim Trigger-Aufruf gesetzt sein.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| [kategorie](/bo4e/202610/cdoc/Transaktionsdaten#kategorie) | string | **ja** | Qualifier aus dem Beginn der EDIFact Nachricht / BGM |
| [sparte](/bo4e/202610/cdoc/Transaktionsdaten#sparte) | [Enum Sparte](/bo4e/202610/enum/Sparte) | **ja** | Enthält Informationen über die Sparte Werte: `STROM`, `GAS`, `FERNWAERME`, `NAHWAERME`, `WASSER`, `ABWASSER` |
| `pruefidentifikator` | — | nein | Wird dynamisch im Event-Prozess ermittelt. Ein vom Sender mitgegebener Wert wird ignoriert. Im Topic mögliche Prüfis — 15001. Mögliche Werte: `15001` |
| [absender › marktrolle](/bo4e/202610/bo/Marktteilnehmer#marktrolle) | [Enum Marktrolle](/bo4e/202610/enum/Marktrolle) | nein | Gibt im Klartext die Bezeichnung der Marktrolle an. Werte: `NB`, `LF`, `MSB`, `MSBA`, `GMSB`, `MDL`, `DL`, `BKV`, `UENB`, `KUNDE-SELBST-NN` … (+9) |
| [absender › rollencodenummer](/bo4e/202610/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |
| [empfaenger › marktrolle](/bo4e/202610/bo/Marktteilnehmer#marktrolle) | [Enum Marktrolle](/bo4e/202610/enum/Marktrolle) | nein | Gibt im Klartext die Bezeichnung der Marktrolle an. Werte: `NB`, `LF`, `MSB`, `MSBA`, `GMSB`, `MDL`, `DL`, `BKV`, `UENB`, `KUNDE-SELBST-NN` … (+9) |
| [empfaenger › rollencodenummer](/bo4e/202610/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |

## Zusatzdaten

`eventname` ist auf **START_ANGEBOT_GERAETEUEBERNAHME** festgelegt. Dieser Wert bleibt auch in der englischen Fassung deutsch, weil Camunda darüber korreliert.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `prozessId` | string | **ja** | — |
| `eventname` | const `START_ANGEBOT_GERAETEUEBERNAHME` | **ja** | — |

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
