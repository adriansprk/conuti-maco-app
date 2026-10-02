# Handelsunstimmigkeit
<span hidden data-pagefind-meta={"title:Handelsunstimmigkeit — BO4E-Geschäftsobjekt (FV 202610)"} />

BO4E-Geschäftsobjekt · 6 Felder · 4 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="botyp"></a>`boTyp` <span className="hbs-pflicht">\*</span> | [Enum BOTyp](/bo4e/202610/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> | Typ des BO |
| <a id="versionstruktur"></a>`versionStruktur` <span className="hbs-pflicht">\*</span> | string | versionStruktur |
| <a id="nummer"></a>`nummer` | string | Handelsunstimmigkeitsnummer |
| <a id="typ"></a>`typ` | [Enum Handelsunstimmigkeitstyp](/bo4e/202610/enum/Handelsunstimmigkeitstyp)<br/><Werte>`HANDELSRECHNUNG`, `LIEFERSCHEIN_HANDELSUNSTIMMIGKEITSTYP`, `LIEFERSCHEIN_GRUND_ARBEITSPREIS`, `LIEFERSCHEIN_ARBEITS_LEISTUNGSPREIS`</Werte> | Gibt den Typ der Handelsunstimmigkeit an. |
| <a id="begruendung"></a>`begruendung` | [Handelsunstimmigkeitsbegruendung](/bo4e/202610/com/Handelsunstimmigkeitsbegruendung) | Handelsunstimmigskeitsbegründung |
| <a id="zuzahlen"></a>`zuZahlen` | [Betrag](/bo4e/202610/com/Betrag) | angeforderter Betrag |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[boTyp](/bo4e/202610/bo/Handelsunstimmigkeit#botyp) <span className="hbs-pflicht">\*</span></span> | Typ des BO | [Enum BOTyp](/bo4e/202610/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> |
| <span className="hbs-f hbs-e0">[versionStruktur](/bo4e/202610/bo/Handelsunstimmigkeit#versionstruktur) <span className="hbs-pflicht">\*</span></span> | versionStruktur | string |
| <span className="hbs-f hbs-e0">[nummer](/bo4e/202610/bo/Handelsunstimmigkeit#nummer)</span> | Handelsunstimmigkeitsnummer | string |
| <span className="hbs-f hbs-e0">[typ](/bo4e/202610/bo/Handelsunstimmigkeit#typ)</span> | Gibt den Typ der Handelsunstimmigkeit an. | [Enum Handelsunstimmigkeitstyp](/bo4e/202610/enum/Handelsunstimmigkeitstyp)<br/><Werte>`HANDELSRECHNUNG`, `LIEFERSCHEIN_HANDELSUNSTIMMIGKEITSTYP`, `LIEFERSCHEIN_GRUND_ARBEITSPREIS`, `LIEFERSCHEIN_ARBEITS_LEISTUNGSPREIS`</Werte> |
| <span className="hbs-g hbs-e0">[begruendung](/bo4e/202610/bo/Handelsunstimmigkeit#begruendung)</span> | Handelsunstimmigskeitsbegründung | [Handelsunstimmigkeitsbegruendung](/bo4e/202610/com/Handelsunstimmigkeitsbegruendung) |
| <span className="hbs-f hbs-e1">[richtigkeit](/bo4e/202610/com/Handelsunstimmigkeitsbegruendung#richtigkeit)</span> | Handelsunstimmigkeitsrichtigkeit | [Enum Handelsunstimmigkeitsrichtigkeit](/bo4e/202610/enum/Handelsunstimmigkeitsrichtigkeit)<br/><Werte>`MSCONS`, `UTILMD`, `INVOIC`, `ORDERS`, `PRICAT`, `IFTSTA`, `ORDCHG`</Werte> |
| <span className="hbs-f hbs-e1">[referenzDar](/bo4e/202610/com/Handelsunstimmigkeitsbegruendung#referenzdar)</span> | Referenzierte Datenaustauschreferenz | string |
| <span className="hbs-f hbs-e1">[referenznummer](/bo4e/202610/com/Handelsunstimmigkeitsbegruendung#referenznummer)</span> | Referenznummer der Nachricht | string |
| <span className="hbs-f hbs-e1">[bestaetigungDar](/bo4e/202610/com/Handelsunstimmigkeitsbegruendung#bestaetigungdar)</span> | bestätigte Datenaustauschreferenz | string |
| <span className="hbs-f hbs-e1">[anerkennungsmeldung](/bo4e/202610/com/Handelsunstimmigkeitsbegruendung#anerkennungsmeldung)</span> | Nachrichtennummer aus der Anerkennungsmeldung (APERAK) | string |
| <span className="hbs-f hbs-e1">[grund](/bo4e/202610/com/Handelsunstimmigkeitsbegruendung#grund)</span> | Angabe des Handelsunstimmigkeitsgrunds | [Enum Handelsunstimmigkeitsgrund](/bo4e/202610/enum/Handelsunstimmigkeitsgrund)<br/><Werte>`ANMELDUNG_BESTAETIGT`, `ABRECHNUNGSBEGINN_GLEICH_BESTAETIGTEM_VERTRAGSBEGINN`, `ABRECHNUNGSENDE_GLEICH_BESTAETIGTEM_VERTRAGSENDE`, `NN_MSCONS_UEBERSENDET`, `RICHTIGE_MESSWERTE_ENERGIEMENGEN_UEBERSENDET`, `SONSTIGES_SIEHE_BEGRUENDUNG`, `GUELTIGES_PREISBLATT_VERSENDET`, `GUELTIGER_SPERRAUFTRAG_VORHANDEN`, `KORREKTE_ARTIKEL_ID_IN_RECHNUNG`, `KORREKTER_PREIS_ZU_GUELTIGEM_PREISBLATT_IN_RECHNUNG`, `RECHNUNG_KORREKT_A05`, `RECHNUNG_KORREKT_A10`, `RECHNUNG_KORREKT_A11`, `GUELTIGES_PREISBLATT_FRISTGERECHT_VERSENDET`, `GUELTIGE_RECHNUNG_VORHANDEN`, `ARTIKEL_ID_FUER_VERZUGSKOSTEN_VERWENDET`, `KORREKTER_PREIS_IN_RECHNUNG_ABGERECHNET`, `GUELTIGES_PREISBLATT_BLINDARBEIT_VERSENDET`, `KORREKTE_ARTIKEL_ID_IST_ANGEGEBEN`, `RECHNUNG_BREGRUENDET_KORREKT`, `KORREKTE_ARTIKEL_ID_FUER_ABRECHNUNG_STORNIERTER_SPERRAUFTRAG_ANGEGEBEN`, `ABRECHNUNG_BLINDARBEIT_SPARTE_GAS_NICHT_RELEVANT`, `SONSTIGES`</Werte> |
| <span className="hbs-f hbs-e1">[hinweis](/bo4e/202610/com/Handelsunstimmigkeitsbegruendung#hinweis)</span> | Hinweis zum Grund | string |
| <span className="hbs-f hbs-e1">[referenzen](/bo4e/202610/com/Handelsunstimmigkeitsbegruendung#referenzen) <span className="hbs-liste">[ ]</span></span> | Referenzen auf vorherige Nachrichten | string[] |
| <span className="hbs-g hbs-e0">[zuZahlen](/bo4e/202610/bo/Handelsunstimmigkeit#zuzahlen)</span> | angeforderter Betrag | [Betrag](/bo4e/202610/com/Betrag) |
| <span className="hbs-f hbs-e1">[wert](/bo4e/202610/com/Betrag#wert)</span> | Gibt den Betrag des Preises an. | number (float) |
| <span className="hbs-f hbs-e1">[waehrung](/bo4e/202610/com/Betrag#waehrung)</span> | Währung des Preises | string |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### nummer

2 Verwendung(en) in den Nachrichtentypen COMDIS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_29001](/schnittstellen/202610/pruefi/COMDIS/PI_29001) | Prüfi | COMDIS | stammdaten › HANDELSUNSTIMMIGKEIT |
| [PI_29002](/schnittstellen/202610/pruefi/COMDIS/PI_29002) | Prüfi | COMDIS | stammdaten › HANDELSUNSTIMMIGKEIT |

### typ

2 Verwendung(en) in den Nachrichtentypen COMDIS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_29001](/schnittstellen/202610/pruefi/COMDIS/PI_29001) | Prüfi | COMDIS | stammdaten › HANDELSUNSTIMMIGKEIT |
| [PI_29002](/schnittstellen/202610/pruefi/COMDIS/PI_29002) | Prüfi | COMDIS | stammdaten › HANDELSUNSTIMMIGKEIT |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
