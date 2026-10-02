# Lokationsbuendel
<span hidden data-pagefind-meta={"title:Lokationsbuendel — BO4E-Geschäftsobjekt (FV 202610)"} />

BO4E-Geschäftsobjekt · 8 Felder · 38 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="botyp"></a>`boTyp` <span className="hbs-pflicht">\*</span> | [Enum BOTyp](/bo4e/202610/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> | Typ des BO |
| <a id="versionstruktur"></a>`versionStruktur` <span className="hbs-pflicht">\*</span> | string | versionStruktur |
| <a id="lokationsbuendelstrukturid"></a>`lokationsbuendelstrukturId` | string | lokationsbuendelstrukturId |
| <a id="lokationsbuendelnummer"></a>`lokationsbuendelNummer` | integer | lokationsbuendelNummer |
| <a id="standardisiertelokationsbuendelstruktur"></a>`standardisierteLokationsbuendelstruktur` | boolean | standardisierteLokationsbuendelstruktur |
| <a id="datenqualitaet"></a>`datenqualitaet` | [Enum Datenqualitaet](/bo4e/202610/enum/Datenqualitaet)<br/><Werte>`ERWARTETE_DATEN`, `IM_SYSTEM_VORHANDENE_DATEN`, `INFORMATIVE_DATEN`, `GUELTIGE_DATEN`, `KEINE_DATEN`, `IM_SYSTEM_KEINE_DATEN_VORHANDEN`, `KEINE_DATEN_ERWARTET`, `DIFFERENZ_DATEN`, `DIFFERENZ_ERWARTETE_DATEN`, `DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</Werte> | Datenqualitaet |
| <a id="gueltigkeitszeitraum"></a>`gueltigkeitszeitraum` | [Zeitraum](/bo4e/202610/com/Zeitraum) | — |
| <a id="zuordnungobjectcode"></a>`zuordnungObjectcode` | [ZuordnungObjectcode[]](/bo4e/202610/com/ZuordnungObjectcode) | zuordnungObjectcode |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[boTyp](/bo4e/202610/bo/Lokationsbuendel#botyp) <span className="hbs-pflicht">\*</span></span> | Typ des BO | [Enum BOTyp](/bo4e/202610/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> |
| <span className="hbs-f hbs-e0">[versionStruktur](/bo4e/202610/bo/Lokationsbuendel#versionstruktur) <span className="hbs-pflicht">\*</span></span> | versionStruktur | string |
| <span className="hbs-f hbs-e0">[lokationsbuendelstrukturId](/bo4e/202610/bo/Lokationsbuendel#lokationsbuendelstrukturid)</span> | lokationsbuendelstrukturId | string |
| <span className="hbs-f hbs-e0">[lokationsbuendelNummer](/bo4e/202610/bo/Lokationsbuendel#lokationsbuendelnummer)</span> | lokationsbuendelNummer | integer |
| <span className="hbs-f hbs-e0">[standardisierteLokationsbuendelstruktur](/bo4e/202610/bo/Lokationsbuendel#standardisiertelokationsbuendelstruktur)</span> | standardisierteLokationsbuendelstruktur | boolean |
| <span className="hbs-f hbs-e0">[datenqualitaet](/bo4e/202610/bo/Lokationsbuendel#datenqualitaet)</span> | Datenqualitaet | [Enum Datenqualitaet](/bo4e/202610/enum/Datenqualitaet)<br/><Werte>`ERWARTETE_DATEN`, `IM_SYSTEM_VORHANDENE_DATEN`, `INFORMATIVE_DATEN`, `GUELTIGE_DATEN`, `KEINE_DATEN`, `IM_SYSTEM_KEINE_DATEN_VORHANDEN`, `KEINE_DATEN_ERWARTET`, `DIFFERENZ_DATEN`, `DIFFERENZ_ERWARTETE_DATEN`, `DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</Werte> |
| <span className="hbs-g hbs-e0">[gueltigkeitszeitraum](/bo4e/202610/bo/Lokationsbuendel#gueltigkeitszeitraum)</span> | — | [Zeitraum](/bo4e/202610/com/Zeitraum) |
| <span className="hbs-f hbs-e1">[zeiteinheit](/bo4e/202610/com/Zeitraum#zeiteinheit)</span> | Zeiteinheit | [Enum Zeiteinheit](/bo4e/202610/enum/Zeiteinheit)<br/><Werte>`SEKUNDE`, `MINUTE`, `STUNDE`, `VIERTEL_STUNDE`, `TAG`, `WOCHE`, `MONAT`, `QUARTAL`, `HALBJAHR`, `JAHR`</Werte> |
| <span className="hbs-f hbs-e1">[dauer](/bo4e/202610/com/Zeitraum#dauer)</span> | dauer | integer |
| <span className="hbs-f hbs-e1">[startdatum](/bo4e/202610/com/Zeitraum#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e1">[enddatum](/bo4e/202610/com/Zeitraum#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-f hbs-e1">[einheit](/bo4e/202610/com/Zeitraum#einheit)</span> | Zeiteinheit | [Enum Zeiteinheit](/bo4e/202610/enum/Zeiteinheit)<br/><Werte>`SEKUNDE`, `MINUTE`, `STUNDE`, `VIERTEL_STUNDE`, `TAG`, `WOCHE`, `MONAT`, `QUARTAL`, `HALBJAHR`, `JAHR`</Werte> |
| <span className="hbs-f hbs-e1">[ableseZeitraum](/bo4e/202610/com/Zeitraum#ablesezeitraum)</span> | ableseZeitraum | string |
| <span className="hbs-f hbs-e1">[abrechnungsZeitraum](/bo4e/202610/com/Zeitraum#abrechnungszeitraum)</span> | abrechnungsZeitraum | string |
| <span className="hbs-f hbs-e1">[zeitraumText](/bo4e/202610/com/Zeitraum#zeitraumtext)</span> | zeitraumText | string |
| <span className="hbs-f hbs-e1">[zeitraumId](/bo4e/202610/com/Zeitraum#zeitraumid)</span> | zeitraumId | integer |
| <span className="hbs-g hbs-e0">[zuordnungObjectcode](/bo4e/202610/bo/Lokationsbuendel#zuordnungobjectcode) <span className="hbs-liste">[ ]</span></span> | zuordnungObjectcode | [ZuordnungObjectcode[]](/bo4e/202610/com/ZuordnungObjectcode) |
| <span className="hbs-f hbs-e1">[referenzLokationsTyp](/bo4e/202610/com/ZuordnungObjectcode#referenzlokationstyp)</span> | Gibt an, ob es sich um eine Markt- oder Messlokation handelt | [Enum Lokationstyp](/bo4e/202610/enum/Lokationstyp)<br/><Werte>`MALO`, `MELO`, `NELO`, `TECHNISCHE_RESSOURCE`, `STEUERBARE_RESSOURCE`, `TRANCHE`, `MABIS_ZAEHLPUNKT`</Werte> |
| <span className="hbs-f hbs-e1">[referenzLokationsId](/bo4e/202610/com/ZuordnungObjectcode#referenzlokationsid)</span> | referenzLokationsId | string |
| <span className="hbs-f hbs-e1">[vorgelagerteLokationTyp](/bo4e/202610/com/ZuordnungObjectcode#vorgelagertelokationtyp)</span> | Gibt an, ob es sich um eine Markt- oder Messlokation handelt | [Enum Lokationstyp](/bo4e/202610/enum/Lokationstyp)<br/><Werte>`MALO`, `MELO`, `NELO`, `TECHNISCHE_RESSOURCE`, `STEUERBARE_RESSOURCE`, `TRANCHE`, `MABIS_ZAEHLPUNKT`</Werte> |
| <span className="hbs-f hbs-e1">[vorgelagerteLokationId](/bo4e/202610/com/ZuordnungObjectcode#vorgelagertelokationid)</span> | vorgelagerteLokationId | string |
| <span className="hbs-g hbs-e1">[objectcode](/bo4e/202610/com/ZuordnungObjectcode#objectcode) <span className="hbs-liste">[ ]</span></span> | objectcode | [Objectcode[]](/bo4e/202610/com/Objectcode) |
| <span className="hbs-f hbs-e2">[objectcode](/bo4e/202610/com/Objectcode#objectcode)</span> | objectcode | string |
| <span className="hbs-f hbs-e2">[lokationsbuendelNummer](/bo4e/202610/com/Objectcode#lokationsbuendelnummer)</span> | lokationsbuendelNummer | integer |
| <span className="hbs-f hbs-e1">[referenzMarktlokationTechnischeRessource](/bo4e/202610/com/ZuordnungObjectcode#referenzmarktlokationtechnischeressource) <span className="hbs-liste">[ ]</span></span> | referenzMarktlokationTechnischeRessource | string[] |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### lokationsbuendelstrukturId

11 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55035](/schnittstellen/202610/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL |
| [PI_55060](/schnittstellen/202610/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL |
| [PI_55095](/schnittstellen/202610/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL |
| [PI_55173](/schnittstellen/202610/pruefi/UTILMD/PI_55173) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL |
| [PI_55175](/schnittstellen/202610/pruefi/UTILMD/PI_55175) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL |
| [PI_55177](/schnittstellen/202610/pruefi/UTILMD/PI_55177) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL |
| [PI_55180](/schnittstellen/202610/pruefi/UTILMD/PI_55180) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL |
| [PI_55690](/schnittstellen/202610/pruefi/UTILMD/PI_55690) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL |

### lokationsbuendelNummer

11 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55035](/schnittstellen/202610/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL |
| [PI_55060](/schnittstellen/202610/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL |
| [PI_55095](/schnittstellen/202610/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL |
| [PI_55173](/schnittstellen/202610/pruefi/UTILMD/PI_55173) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL |
| [PI_55175](/schnittstellen/202610/pruefi/UTILMD/PI_55175) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL |
| [PI_55177](/schnittstellen/202610/pruefi/UTILMD/PI_55177) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL |
| [PI_55180](/schnittstellen/202610/pruefi/UTILMD/PI_55180) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL |
| [PI_55690](/schnittstellen/202610/pruefi/UTILMD/PI_55690) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL |

### standardisierteLokationsbuendelstruktur

11 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55035](/schnittstellen/202610/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL |
| [PI_55060](/schnittstellen/202610/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL |
| [PI_55095](/schnittstellen/202610/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL |
| [PI_55173](/schnittstellen/202610/pruefi/UTILMD/PI_55173) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL |
| [PI_55175](/schnittstellen/202610/pruefi/UTILMD/PI_55175) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL |
| [PI_55177](/schnittstellen/202610/pruefi/UTILMD/PI_55177) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL |
| [PI_55180](/schnittstellen/202610/pruefi/UTILMD/PI_55180) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL |
| [PI_55690](/schnittstellen/202610/pruefi/UTILMD/PI_55690) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL |

### datenqualitaet

5 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55173](/schnittstellen/202610/pruefi/UTILMD/PI_55173) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL |
| [PI_55175](/schnittstellen/202610/pruefi/UTILMD/PI_55175) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL |
| [PI_55177](/schnittstellen/202610/pruefi/UTILMD/PI_55177) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL |
| [PI_55180](/schnittstellen/202610/pruefi/UTILMD/PI_55180) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL |
| [PI_55690](/schnittstellen/202610/pruefi/UTILMD/PI_55690) | Prüfi | UTILMD | stammdaten › LOKATIONSBUENDEL |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
