# Netznutzungsabrechnungsdaten
<span hidden data-pagefind-meta={"title:Netznutzungsabrechnungsdaten — BO4E-Komponente (FV 202604)"} />

BO4E-Komponente · 13 Felder · 28 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="artikelid"></a>`artikelId` | string | artikelId |
| <a id="artikelidtyp"></a>`artikelIdTyp` | [Enum ArtikelIdTyp](/bo4e/202604/enum/ArtikelIdTyp)<br/><Werte>`ARTIKELID`, `GRUPPENARTIKELID`</Werte> | Liste von Artikel-IDs, z.B. für standardisierte vom BDEW herausgegebene Artikel, die im Strommarkt die BDEW-Artikelnummer ablösen |
| <a id="anzahl"></a>`anzahl` | integer | Anzahl |
| <a id="gemeinderabatt"></a>`gemeinderabatt` | number (float) | Gemeinderabatt |
| <a id="zuschlag"></a>`zuschlag` | number (float) | Zuschlag |
| <a id="abschlag"></a>`abschlag` | number (float) | Abschlag |
| <a id="singulaerebetriebsmittel"></a>`singulaereBetriebsmittel` | [Menge](/bo4e/202604/com/Menge) | — |
| <a id="preissingulaerebetriebsmittel"></a>`preisSingulaereBetriebsmittel` | [Preis](/bo4e/202604/com/Preis) | — |
| <a id="abrechnungblindarbeit"></a>`abrechnungBlindarbeit` | boolean | abrechnungBlindarbeit |
| <a id="zahlerblindarbeit"></a>`zahlerBlindarbeit` | [Enum ZahlerBlindarbeit](/bo4e/202604/enum/ZahlerBlindarbeit)<br/><Werte>`ANSCHLUSSNUTZER`, `LIEFERANT`, `NICHT_FESTGELEGT`</Werte> | ZahlerBlindarbeit |
| <a id="zahlerblindarbeitlf"></a>`zahlerBlindarbeitLf` | boolean | Zahlung der Blindarbeit durch den Lieferanten |
| <a id="differenzdaten"></a>`differenzDaten` | boolean | differenzDaten |
| <a id="zaehlzeiten"></a>`zaehlzeiten` | [Zaehlzeitregister](/bo4e/202604/com/Zaehlzeitregister) | — |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[artikelId](/bo4e/202604/com/Netznutzungsabrechnungsdaten#artikelid)</span> | artikelId | string |
| <span className="hbs-f hbs-e0">[artikelIdTyp](/bo4e/202604/com/Netznutzungsabrechnungsdaten#artikelidtyp)</span> | Liste von Artikel-IDs, z.B. für standardisierte vom BDEW herausgegebene Artikel, die im Strommarkt die BDEW-Artikelnummer ablösen | [Enum ArtikelIdTyp](/bo4e/202604/enum/ArtikelIdTyp)<br/><Werte>`ARTIKELID`, `GRUPPENARTIKELID`</Werte> |
| <span className="hbs-f hbs-e0">[anzahl](/bo4e/202604/com/Netznutzungsabrechnungsdaten#anzahl)</span> | Anzahl | integer |
| <span className="hbs-f hbs-e0">[gemeinderabatt](/bo4e/202604/com/Netznutzungsabrechnungsdaten#gemeinderabatt)</span> | Gemeinderabatt | number (float) |
| <span className="hbs-f hbs-e0">[zuschlag](/bo4e/202604/com/Netznutzungsabrechnungsdaten#zuschlag)</span> | Zuschlag | number (float) |
| <span className="hbs-f hbs-e0">[abschlag](/bo4e/202604/com/Netznutzungsabrechnungsdaten#abschlag)</span> | Abschlag | number (float) |
| <span className="hbs-g hbs-e0">[singulaereBetriebsmittel](/bo4e/202604/com/Netznutzungsabrechnungsdaten#singulaerebetriebsmittel)</span> | — | [Menge](/bo4e/202604/com/Menge) |
| <span className="hbs-f hbs-e1">[wert](/bo4e/202604/com/Menge#wert)</span> | Wert | number (float) |
| <span className="hbs-f hbs-e1">[einheit](/bo4e/202604/com/Menge#einheit)</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202604/enum/Mengeneinheit)<br/><Werte>`W`, `WH`, `KW`, `KWH`, `KVARH`, `MW`, `MWH`, `STUECK`, `KUBIKMETER`, `STUNDE`, `TAG`, `MONAT`, `JAHR`, `PROZENT`, `ANZAHL`, `VAR`, `KVAR`, `VARH`, `KWHK`, `Z16`, `KWT`, `WATT_PRO_QUADRATMETER`, `METER_PRO_SEKUNDE`</Werte> |
| <span className="hbs-f hbs-e1">[startdatum](/bo4e/202604/com/Menge#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e1">[enddatum](/bo4e/202604/com/Menge#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-g hbs-e0">[preisSingulaereBetriebsmittel](/bo4e/202604/com/Netznutzungsabrechnungsdaten#preissingulaerebetriebsmittel)</span> | — | [Preis](/bo4e/202604/com/Preis) |
| <span className="hbs-f hbs-e1">[wert](/bo4e/202604/com/Preis#wert)</span> | wert | number (float) |
| <span className="hbs-f hbs-e1">[menge](/bo4e/202604/com/Preis#menge)</span> | menge | integer |
| <span className="hbs-f hbs-e1">[minimaleMenge](/bo4e/202604/com/Preis#minimalemenge)</span> | minimale Menge | integer |
| <span className="hbs-f hbs-e1">[maximaleMenge](/bo4e/202604/com/Preis#maximalemenge)</span> | maximale Menge | integer |
| <span className="hbs-f hbs-e1">[einheit](/bo4e/202604/com/Preis#einheit)</span> | Waehrungseinheit | [Enum Waehrungseinheit](/bo4e/202604/enum/Waehrungseinheit)<br/><Werte>`EUR`, `CT`</Werte> |
| <span className="hbs-f hbs-e1">[bezugswert](/bo4e/202604/com/Preis#bezugswert)</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202604/enum/Mengeneinheit)<br/><Werte>`W`, `WH`, `KW`, `KWH`, `KVARH`, `MW`, `MWH`, `STUECK`, `KUBIKMETER`, `STUNDE`, `TAG`, `MONAT`, `JAHR`, `PROZENT`, `ANZAHL`, `VAR`, `KVAR`, `VARH`, `KWHK`, `Z16`, `KWT`, `WATT_PRO_QUADRATMETER`, `METER_PRO_SEKUNDE`</Werte> |
| <span className="hbs-f hbs-e1">[status](/bo4e/202604/com/Preis#status)</span> | Preisstatus | [Enum Preisstatus](/bo4e/202604/enum/Preisstatus)<br/><Werte>`VORLAEUFIG`, `ENDGUELTIG`</Werte> |
| <span className="hbs-f hbs-e1">[preisart](/bo4e/202604/com/Preis#preisart)</span> | Preisart Code | [Enum Preisart](/bo4e/202604/enum/Preisart)<br/><Werte>`EINRICHTUNGSPREIS`, `TRANSAKTIONSPREIS`, `BETRIEBSPREIS`</Werte> |
| <span className="hbs-f hbs-e0">[abrechnungBlindarbeit](/bo4e/202604/com/Netznutzungsabrechnungsdaten#abrechnungblindarbeit)</span> | abrechnungBlindarbeit | boolean |
| <span className="hbs-f hbs-e0">[zahlerBlindarbeit](/bo4e/202604/com/Netznutzungsabrechnungsdaten#zahlerblindarbeit)</span> | ZahlerBlindarbeit | [Enum ZahlerBlindarbeit](/bo4e/202604/enum/ZahlerBlindarbeit)<br/><Werte>`ANSCHLUSSNUTZER`, `LIEFERANT`, `NICHT_FESTGELEGT`</Werte> |
| <span className="hbs-f hbs-e0">[zahlerBlindarbeitLf](/bo4e/202604/com/Netznutzungsabrechnungsdaten#zahlerblindarbeitlf)</span> | Zahlung der Blindarbeit durch den Lieferanten | boolean |
| <span className="hbs-f hbs-e0">[differenzDaten](/bo4e/202604/com/Netznutzungsabrechnungsdaten#differenzdaten)</span> | differenzDaten | boolean |
| <span className="hbs-g hbs-e0">[zaehlzeiten](/bo4e/202604/com/Netznutzungsabrechnungsdaten#zaehlzeiten)</span> | — | [Zaehlzeitregister](/bo4e/202604/com/Zaehlzeitregister) |
| <span className="hbs-f hbs-e1">[register](/bo4e/202604/com/Zaehlzeitregister#register)</span> | Zählzeitregister | string |
| <span className="hbs-f hbs-e1">[zaehlzeitDefinition](/bo4e/202604/com/Zaehlzeitregister#zaehlzeitdefinition)</span> | Zählzeitdefinition | string |
| <span className="hbs-f hbs-e1">[schwachlastfaehig](/bo4e/202604/com/Zaehlzeitregister#schwachlastfaehig)</span> | Schwachlastfähigkeit des Registers | [Enum Schwachlastfaehig](/bo4e/202604/enum/Schwachlastfaehig)<br/><Werte>`SCHWACHLASTFAEHIG`, `NICHT_SCHWACHLASTFAEHIG`</Werte> |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### artikelId

5 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55035](/schnittstellen/202604/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › netznutzungsabrechnungsdaten |
| [PI_55218](/schnittstellen/202604/pruefi/UTILMD/PI_55218) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › netznutzungsabrechnungsdaten |
| [PI_55220](/schnittstellen/202604/pruefi/UTILMD/PI_55220) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › netznutzungsabrechnungsdaten |
| [PI_55225](/schnittstellen/202604/pruefi/UTILMD/PI_55225) | Prüfi | UTILMD | stammdaten › NETZLOKATION › abrechnungsdaten |
| [PI_55227](/schnittstellen/202604/pruefi/UTILMD/PI_55227) | Prüfi | UTILMD | stammdaten › NETZLOKATION › abrechnungsdaten |

### artikelIdTyp

5 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55035](/schnittstellen/202604/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › netznutzungsabrechnungsdaten |
| [PI_55218](/schnittstellen/202604/pruefi/UTILMD/PI_55218) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › netznutzungsabrechnungsdaten |
| [PI_55220](/schnittstellen/202604/pruefi/UTILMD/PI_55220) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › netznutzungsabrechnungsdaten |
| [PI_55225](/schnittstellen/202604/pruefi/UTILMD/PI_55225) | Prüfi | UTILMD | stammdaten › NETZLOKATION › abrechnungsdaten |
| [PI_55227](/schnittstellen/202604/pruefi/UTILMD/PI_55227) | Prüfi | UTILMD | stammdaten › NETZLOKATION › abrechnungsdaten |

### anzahl

3 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55035](/schnittstellen/202604/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › netznutzungsabrechnungsdaten |
| [PI_55218](/schnittstellen/202604/pruefi/UTILMD/PI_55218) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › netznutzungsabrechnungsdaten |
| [PI_55220](/schnittstellen/202604/pruefi/UTILMD/PI_55220) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › netznutzungsabrechnungsdaten |

### gemeinderabatt

3 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55035](/schnittstellen/202604/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › netznutzungsabrechnungsdaten |
| [PI_55218](/schnittstellen/202604/pruefi/UTILMD/PI_55218) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › netznutzungsabrechnungsdaten |
| [PI_55220](/schnittstellen/202604/pruefi/UTILMD/PI_55220) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › netznutzungsabrechnungsdaten |

### zuschlag

3 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55035](/schnittstellen/202604/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › netznutzungsabrechnungsdaten |
| [PI_55218](/schnittstellen/202604/pruefi/UTILMD/PI_55218) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › netznutzungsabrechnungsdaten |
| [PI_55220](/schnittstellen/202604/pruefi/UTILMD/PI_55220) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › netznutzungsabrechnungsdaten |

### abschlag

3 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55035](/schnittstellen/202604/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › netznutzungsabrechnungsdaten |
| [PI_55218](/schnittstellen/202604/pruefi/UTILMD/PI_55218) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › netznutzungsabrechnungsdaten |
| [PI_55220](/schnittstellen/202604/pruefi/UTILMD/PI_55220) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › netznutzungsabrechnungsdaten |

### abrechnungBlindarbeit

2 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55225](/schnittstellen/202604/pruefi/UTILMD/PI_55225) | Prüfi | UTILMD | stammdaten › NETZLOKATION › abrechnungsdaten |
| [PI_55227](/schnittstellen/202604/pruefi/UTILMD/PI_55227) | Prüfi | UTILMD | stammdaten › NETZLOKATION › abrechnungsdaten |

### zahlerBlindarbeit

2 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55225](/schnittstellen/202604/pruefi/UTILMD/PI_55225) | Prüfi | UTILMD | stammdaten › NETZLOKATION › abrechnungsdaten |
| [PI_55227](/schnittstellen/202604/pruefi/UTILMD/PI_55227) | Prüfi | UTILMD | stammdaten › NETZLOKATION › abrechnungsdaten |

### zahlerBlindarbeitLf

2 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55230](/schnittstellen/202604/pruefi/UTILMD/PI_55230) | Prüfi | UTILMD | stammdaten › NETZLOKATION › abrechnungsdaten |
| [PI_55232](/schnittstellen/202604/pruefi/UTILMD/PI_55232) | Prüfi | UTILMD | stammdaten › NETZLOKATION › abrechnungsdaten |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
