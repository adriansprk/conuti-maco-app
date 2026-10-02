# Berechnungsformel
<span hidden data-pagefind-meta={"title:Berechnungsformel — BO4E-Geschäftsobjekt (FV 202604)"} />

BO4E-Geschäftsobjekt · 16 Felder · 2 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="botyp"></a>`boTyp` <span className="hbs-pflicht">\*</span> | [Enum BOTyp](/bo4e/202604/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> | Typ des BO |
| <a id="versionstruktur"></a>`versionStruktur` <span className="hbs-pflicht">\*</span> | string | versionStruktur |
| <a id="beginndatum"></a>`beginndatum` | string (date-time) | Der inklusive Zeitpunkt ab dem die Berechnungsformel gültig ist |
| <a id="notwendigkeit"></a>`notwendigkeit` | [Enum BerechnungsformelNotwendigkeit](/bo4e/202604/enum/BerechnungsformelNotwendigkeit)<br/><Werte>`BERECHNUNGSFORMEL_NOTWENDIG`, `BERECHNUNGSFORMEL_MUSS_ANGEFRAGT_WERDEN`, `BERECHNUNGSFORMEL_TRIVIAL`, `BERECHNUNGSFORMEL_NICHT_NOTWENDIG`</Werte> | Beschreibt ob eine Berechnungsformel notwendig ist |
| <a id="lieferrichtung"></a>`lieferrichtung` | [Enum Energierichtung](/bo4e/202604/enum/Energierichtung)<br/><Werte>`AUSSP`, `EINSP`</Werte> | The UTILTS 'Lieferrichtung der Marktlokation' is contained in the marktlokations-bo also the relation between Berechnungsformel↔ Marktlokation is modelled as 'link' |
| <a id="rechenschrittid"></a>`rechenschrittId` | integer | ID des Rechenschritts [1 - 99999] |
| <a id="rechenschritt"></a>`rechenschritt` | [Rechenschritt](/bo4e/202604/com/Rechenschritt) | — |
| <a id="rechenschritte"></a>`rechenschritte` | [Rechenschritt[]](/bo4e/202604/com/Rechenschritt) | Eine Berechnungsformel enthält, falls sie notwendig ist, einen oder mehrere Berechnungschritte, die hier rekursiv abgebildet werden. |
| <a id="verwendungszweck"></a>`verwendungszweck` | [Verwendungszweck[]](/bo4e/202604/com/Verwendungszweck) | Verwendungszweck der Werte |
| <a id="gueltigkeitszeitraum"></a>`gueltigkeitszeitraum` | [Zeitraum](/bo4e/202604/com/Zeitraum) | Gültigkeitszeitraum der Werte |
| <a id="lokationsid"></a>`lokationsId` | string | Eindeutige Nummer der Lokation, zu der die Berechnungsformel gehört. Verwendung für notwendige interne Zuordnungen. |
| <a id="lokationstyp"></a>`lokationsTyp` | [Enum Lokationstyp](/bo4e/202604/enum/Lokationstyp)<br/><Werte>`MALO`, `MELO`, `NELO`, `TECHNISCHE_RESSOURCE`, `STEUERBARE_RESSOURCE`, `TRANCHE`, `MABIS_ZAEHLPUNKT`</Werte> | Gibt an,um welchen Lokationstyp es sich handelt. Verwendung für notwendige interne Zuordnungen. |
| <a id="berechnungsformel"></a>`berechnungsformel` | string | Berechnungsformel |
| <a id="datenqualitaet"></a>`datenqualitaet` | [Enum Datenqualitaet](/bo4e/202604/enum/Datenqualitaet)<br/><Werte>`ERWARTETE_DATEN`, `IM_SYSTEM_VORHANDENE_DATEN`, `INFORMATIVE_DATEN`, `GUELTIGE_DATEN`, `KEINE_DATEN`, `IM_SYSTEM_KEINE_DATEN_VORHANDEN`, `KEINE_DATEN_ERWARTET`, `DIFFERENZ_DATEN`, `DIFFERENZ_ERWARTETE_DATEN`, `DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</Werte> | Datenqualitaet |
| <a id="parameterids"></a>`parameterIDs` | string[] | Parameter IDs |
| <a id="aufteilungsfaktoren"></a>`aufteilungsfaktoren` | [Aufteilungsfaktor[]](/bo4e/202604/com/Aufteilungsfaktor) | Aufteilungsfaktor |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[boTyp](/bo4e/202604/bo/Berechnungsformel#botyp) <span className="hbs-pflicht">\*</span></span> | Typ des BO | [Enum BOTyp](/bo4e/202604/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> |
| <span className="hbs-f hbs-e0">[versionStruktur](/bo4e/202604/bo/Berechnungsformel#versionstruktur) <span className="hbs-pflicht">\*</span></span> | versionStruktur | string |
| <span className="hbs-f hbs-e0">[beginndatum](/bo4e/202604/bo/Berechnungsformel#beginndatum)</span> | Der inklusive Zeitpunkt ab dem die Berechnungsformel gültig ist | string (date-time) |
| <span className="hbs-f hbs-e0">[notwendigkeit](/bo4e/202604/bo/Berechnungsformel#notwendigkeit)</span> | Beschreibt ob eine Berechnungsformel notwendig ist | [Enum BerechnungsformelNotwendigkeit](/bo4e/202604/enum/BerechnungsformelNotwendigkeit)<br/><Werte>`BERECHNUNGSFORMEL_NOTWENDIG`, `BERECHNUNGSFORMEL_MUSS_ANGEFRAGT_WERDEN`, `BERECHNUNGSFORMEL_TRIVIAL`, `BERECHNUNGSFORMEL_NICHT_NOTWENDIG`</Werte> |
| <span className="hbs-f hbs-e0">[lieferrichtung](/bo4e/202604/bo/Berechnungsformel#lieferrichtung)</span> | The UTILTS 'Lieferrichtung der Marktlokation' is contained in the marktlokations-bo also the relation between Berechnungsformel↔ Marktlokation is modelled as 'link' | [Enum Energierichtung](/bo4e/202604/enum/Energierichtung)<br/><Werte>`AUSSP`, `EINSP`</Werte> |
| <span className="hbs-f hbs-e0">[rechenschrittId](/bo4e/202604/bo/Berechnungsformel#rechenschrittid)</span> | ID des Rechenschritts [1 - 99999] | integer |
| <span className="hbs-g hbs-e0">[rechenschritt](/bo4e/202604/bo/Berechnungsformel#rechenschritt)</span> | — | [Rechenschritt](/bo4e/202604/com/Rechenschritt) |
| <span className="hbs-f hbs-e1">[rechenschrittBestandteilId](/bo4e/202604/com/Rechenschritt#rechenschrittbestandteilid)</span> | rechenschrittBestandteilId | integer |
| <span className="hbs-f hbs-e1">[referenzRechenschrittId](/bo4e/202604/com/Rechenschritt#referenzrechenschrittid)</span> | referenzRechenschrittId | integer |
| <span className="hbs-f hbs-e1">[operation](/bo4e/202604/com/Rechenschritt#operation)</span> | Mit dieser Aufzählung können arithmetische Operationen festgelegt werden | [Enum ArithmetischeOperation](/bo4e/202604/enum/ArithmetischeOperation)<br/><Werte>`ADDITION`, `SUBTRAKTION`, `DIVISION`, `DIVIDEND`, `MULTIPLIKATION`, `POSITIVWERT`</Werte> |
| <span className="hbs-f hbs-e1">[verlustfaktorTrafo](/bo4e/202604/com/Rechenschritt#verlustfaktortrafo)</span> | verlustfaktorTrafo | number (float) |
| <span className="hbs-f hbs-e1">[verlustfaktorLeitung](/bo4e/202604/com/Rechenschritt#verlustfaktorleitung)</span> | verlustfaktorLeitung | number (float) |
| <span className="hbs-f hbs-e1">[aufteilungsfaktorEnergiemenge](/bo4e/202604/com/Rechenschritt#aufteilungsfaktorenergiemenge)</span> | aufteilungsfaktorEnergiemenge | number (float) |
| <span className="hbs-f hbs-e1">[messlokationsId](/bo4e/202604/com/Rechenschritt#messlokationsid)</span> | messlokationsId | string |
| <span className="hbs-f hbs-e1">[marktlokationsId](/bo4e/202604/com/Rechenschritt#marktlokationsid)</span> | marktlokationsId | string |
| <span className="hbs-f hbs-e1">[energieflussrichtung](/bo4e/202604/com/Rechenschritt#energieflussrichtung)</span> | Spezifiziert die Energierichtung einer Markt- und/oder Messlokation | [Enum Energierichtung](/bo4e/202604/enum/Energierichtung)<br/><Werte>`AUSSP`, `EINSP`</Werte> |
| <span className="hbs-f hbs-e1">[bezeichnungOperanden](/bo4e/202604/com/Rechenschritt#bezeichnungoperanden)</span> | Bezeichnung der Operanden | string |
| <span className="hbs-g hbs-e0">[rechenschritte](/bo4e/202604/bo/Berechnungsformel#rechenschritte) <span className="hbs-liste">[ ]</span></span> | Eine Berechnungsformel enthält, falls sie notwendig ist, einen oder mehrere Berechnungschritte, die hier rekursiv abgebildet werden. | [Rechenschritt[]](/bo4e/202604/com/Rechenschritt) |
| <span className="hbs-f hbs-e1">[rechenschrittBestandteilId](/bo4e/202604/com/Rechenschritt#rechenschrittbestandteilid)</span> | rechenschrittBestandteilId | integer |
| <span className="hbs-f hbs-e1">[referenzRechenschrittId](/bo4e/202604/com/Rechenschritt#referenzrechenschrittid)</span> | referenzRechenschrittId | integer |
| <span className="hbs-f hbs-e1">[operation](/bo4e/202604/com/Rechenschritt#operation)</span> | Mit dieser Aufzählung können arithmetische Operationen festgelegt werden | [Enum ArithmetischeOperation](/bo4e/202604/enum/ArithmetischeOperation)<br/><Werte>`ADDITION`, `SUBTRAKTION`, `DIVISION`, `DIVIDEND`, `MULTIPLIKATION`, `POSITIVWERT`</Werte> |
| <span className="hbs-f hbs-e1">[verlustfaktorTrafo](/bo4e/202604/com/Rechenschritt#verlustfaktortrafo)</span> | verlustfaktorTrafo | number (float) |
| <span className="hbs-f hbs-e1">[verlustfaktorLeitung](/bo4e/202604/com/Rechenschritt#verlustfaktorleitung)</span> | verlustfaktorLeitung | number (float) |
| <span className="hbs-f hbs-e1">[aufteilungsfaktorEnergiemenge](/bo4e/202604/com/Rechenschritt#aufteilungsfaktorenergiemenge)</span> | aufteilungsfaktorEnergiemenge | number (float) |
| <span className="hbs-f hbs-e1">[messlokationsId](/bo4e/202604/com/Rechenschritt#messlokationsid)</span> | messlokationsId | string |
| <span className="hbs-f hbs-e1">[marktlokationsId](/bo4e/202604/com/Rechenschritt#marktlokationsid)</span> | marktlokationsId | string |
| <span className="hbs-f hbs-e1">[energieflussrichtung](/bo4e/202604/com/Rechenschritt#energieflussrichtung)</span> | Spezifiziert die Energierichtung einer Markt- und/oder Messlokation | [Enum Energierichtung](/bo4e/202604/enum/Energierichtung)<br/><Werte>`AUSSP`, `EINSP`</Werte> |
| <span className="hbs-f hbs-e1">[bezeichnungOperanden](/bo4e/202604/com/Rechenschritt#bezeichnungoperanden)</span> | Bezeichnung der Operanden | string |
| <span className="hbs-g hbs-e0">[verwendungszweck](/bo4e/202604/bo/Berechnungsformel#verwendungszweck) <span className="hbs-liste">[ ]</span></span> | Verwendungszweck der Werte | [Verwendungszweck[]](/bo4e/202604/com/Verwendungszweck) |
| <span className="hbs-f hbs-e1">[marktrolle](/bo4e/202604/com/Verwendungszweck#marktrolle)</span> | Diese Rollen kann ein Marktteilnehmer einnehmen | [Enum Marktrolle](/bo4e/202604/enum/Marktrolle)<br/><Werte>`NB`, `LF`, `MSB`, `MSBA`, `GMSB`, `MDL`, `DL`, `BKV`, `UENB`, `KUNDE-SELBST-NN`, `MGV`, `EIV`, `RB`, `KUNDE`, `INTERESSENT`, `KN`, `UBA`, `BIKO`, `ESA`</Werte> |
| <span className="hbs-f hbs-e1">[zweck](/bo4e/202604/com/Verwendungszweck#zweck) <span className="hbs-liste">[ ]</span></span> | zweck | [Enum VerwendungszweckValue[]](/bo4e/202604/enum/VerwendungszweckValue)<br/><Werte>`NETZNUTZUNGSABRECHNUNG`, `BILANZKREISABRECHNUNG`, `MEHRMINDERMENGENABRECHNUNG`, `ENDKUNDENABRECHNUNG`, `UEBERMITTLUNG_AN_DAS_HKNR`, `BLINDARBEITSABRECHNUNG`, `ERMITTLUNG_AUSGEGLICHENHEIT_BILANZKREIS`, `BLINDARBEITABRECHNUNG_BETRIEBSFUEHRUNG`, `ES_LIEGT_KEIN_VERWENDUNGSZWECK_VOR`</Werte> |
| <span className="hbs-g hbs-e0">[gueltigkeitszeitraum](/bo4e/202604/bo/Berechnungsformel#gueltigkeitszeitraum)</span> | Gültigkeitszeitraum der Werte | [Zeitraum](/bo4e/202604/com/Zeitraum) |
| <span className="hbs-f hbs-e1">[zeiteinheit](/bo4e/202604/com/Zeitraum#zeiteinheit)</span> | Zeiteinheit | [Enum Zeiteinheit](/bo4e/202604/enum/Zeiteinheit)<br/><Werte>`SEKUNDE`, `MINUTE`, `STUNDE`, `VIERTEL_STUNDE`, `TAG`, `WOCHE`, `MONAT`, `QUARTAL`, `HALBJAHR`, `JAHR`</Werte> |
| <span className="hbs-f hbs-e1">[dauer](/bo4e/202604/com/Zeitraum#dauer)</span> | dauer | integer |
| <span className="hbs-f hbs-e1">[startdatum](/bo4e/202604/com/Zeitraum#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e1">[enddatum](/bo4e/202604/com/Zeitraum#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-f hbs-e1">[einheit](/bo4e/202604/com/Zeitraum#einheit)</span> | Zeiteinheit | [Enum Zeiteinheit](/bo4e/202604/enum/Zeiteinheit)<br/><Werte>`SEKUNDE`, `MINUTE`, `STUNDE`, `VIERTEL_STUNDE`, `TAG`, `WOCHE`, `MONAT`, `QUARTAL`, `HALBJAHR`, `JAHR`</Werte> |
| <span className="hbs-f hbs-e1">[ableseZeitraum](/bo4e/202604/com/Zeitraum#ablesezeitraum)</span> | ableseZeitraum | string |
| <span className="hbs-f hbs-e1">[abrechnungsZeitraum](/bo4e/202604/com/Zeitraum#abrechnungszeitraum)</span> | abrechnungsZeitraum | string |
| <span className="hbs-f hbs-e1">[zeitraumText](/bo4e/202604/com/Zeitraum#zeitraumtext)</span> | zeitraumText | string |
| <span className="hbs-f hbs-e1">[zeitraumId](/bo4e/202604/com/Zeitraum#zeitraumid)</span> | zeitraumId | integer |
| <span className="hbs-f hbs-e0">[lokationsId](/bo4e/202604/bo/Berechnungsformel#lokationsid)</span> | Eindeutige Nummer der Lokation, zu der die Berechnungsformel gehört. Verwendung für notwendige interne Zuordnungen. | string |
| <span className="hbs-f hbs-e0">[lokationsTyp](/bo4e/202604/bo/Berechnungsformel#lokationstyp)</span> | Gibt an,um welchen Lokationstyp es sich handelt. Verwendung für notwendige interne Zuordnungen. | [Enum Lokationstyp](/bo4e/202604/enum/Lokationstyp)<br/><Werte>`MALO`, `MELO`, `NELO`, `TECHNISCHE_RESSOURCE`, `STEUERBARE_RESSOURCE`, `TRANCHE`, `MABIS_ZAEHLPUNKT`</Werte> |
| <span className="hbs-f hbs-e0">[berechnungsformel](/bo4e/202604/bo/Berechnungsformel#berechnungsformel)</span> | Berechnungsformel | string |
| <span className="hbs-f hbs-e0">[datenqualitaet](/bo4e/202604/bo/Berechnungsformel#datenqualitaet)</span> | Datenqualitaet | [Enum Datenqualitaet](/bo4e/202604/enum/Datenqualitaet)<br/><Werte>`ERWARTETE_DATEN`, `IM_SYSTEM_VORHANDENE_DATEN`, `INFORMATIVE_DATEN`, `GUELTIGE_DATEN`, `KEINE_DATEN`, `IM_SYSTEM_KEINE_DATEN_VORHANDEN`, `KEINE_DATEN_ERWARTET`, `DIFFERENZ_DATEN`, `DIFFERENZ_ERWARTETE_DATEN`, `DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</Werte> |
| <span className="hbs-f hbs-e0">[parameterIDs](/bo4e/202604/bo/Berechnungsformel#parameterids) <span className="hbs-liste">[ ]</span></span> | Parameter IDs | string[] |
| <span className="hbs-g hbs-e0">[aufteilungsfaktoren](/bo4e/202604/bo/Berechnungsformel#aufteilungsfaktoren) <span className="hbs-liste">[ ]</span></span> | Aufteilungsfaktor | [Aufteilungsfaktor[]](/bo4e/202604/com/Aufteilungsfaktor) |
| <span className="hbs-f hbs-e1">[bezeichnungAufteilungsfaktor](/bo4e/202604/com/Aufteilungsfaktor#bezeichnungaufteilungsfaktor)</span> | Bezeichnung des Aufteilungsfaktors | string |
| <span className="hbs-f hbs-e1">[faktor](/bo4e/202604/com/Aufteilungsfaktor#faktor)</span> | Faktor | number (float) |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### notwendigkeit

1 Verwendung(en) in den Nachrichtentypen UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_25001](/schnittstellen/202604/pruefi/UTILTS/PI_25001) | Prüfi | UTILTS | stammdaten › BERECHNUNGSFORMEL |

### rechenschrittId

1 Verwendung(en) in den Nachrichtentypen UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_25001](/schnittstellen/202604/pruefi/UTILTS/PI_25001) | Prüfi | UTILTS | stammdaten › BERECHNUNGSFORMEL |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
