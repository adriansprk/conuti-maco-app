# Handelsunstimmigkeitsbegruendung
<span hidden data-pagefind-meta={"title:Handelsunstimmigkeitsbegruendung — BO4E-Komponente (FV 202604)"} />

BO4E-Komponente · 8 Felder · 9 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="richtigkeit"></a>`richtigkeit` | [Enum Handelsunstimmigkeitsrichtigkeit](/bo4e/202604/enum/Handelsunstimmigkeitsrichtigkeit)<br/><Werte>`MSCONS`, `UTILMD`, `INVOIC`, `ORDERS`, `PRICAT`, `IFTSTA`, `ORDCHG`</Werte> | Handelsunstimmigkeitsrichtigkeit |
| <a id="referenzdar"></a>`referenzDar` | string | Referenzierte Datenaustauschreferenz |
| <a id="referenznummer"></a>`referenznummer` | string | Referenznummer der Nachricht |
| <a id="bestaetigungdar"></a>`bestaetigungDar` | string | bestätigte Datenaustauschreferenz |
| <a id="anerkennungsmeldung"></a>`anerkennungsmeldung` | string | Nachrichtennummer aus der Anerkennungsmeldung (APERAK) |
| <a id="grund"></a>`grund` | [Enum Handelsunstimmigkeitsgrund](/bo4e/202604/enum/Handelsunstimmigkeitsgrund)<br/><Werte>`ANMELDUNG_BESTAETIGT`, `ABRECHNUNGSBEGINN_GLEICH_BESTAETIGTEM_VERTRAGSBEGINN`, `ABRECHNUNGSENDE_GLEICH_BESTAETIGTEM_VERTRAGSENDE`, `NN_MSCONS_UEBERSENDET`, `RICHTIGE_MESSWERTE_ENERGIEMENGEN_UEBERSENDET`, `SONSTIGES_SIEHE_BEGRUENDUNG`, `GUELTIGES_PREISBLATT_VERSENDET`, `GUELTIGER_SPERRAUFTRAG_VORHANDEN`, `KORREKTE_ARTIKEL_ID_IN_RECHNUNG`, `KORREKTER_PREIS_ZU_GUELTIGEM_PREISBLATT_IN_RECHNUNG`, `RECHNUNG_KORREKT_A05`, `RECHNUNG_KORREKT_A10`, `RECHNUNG_KORREKT_A11`, `GUELTIGES_PREISBLATT_FRISTGERECHT_VERSENDET`, `GUELTIGE_RECHNUNG_VORHANDEN`, `ARTIKEL_ID_FUER_VERZUGSKOSTEN_VERWENDET`, `KORREKTER_PREIS_IN_RECHNUNG_ABGERECHNET`, `GUELTIGES_PREISBLATT_BLINDARBEIT_VERSENDET`, `KORREKTE_ARTIKEL_ID_IST_ANGEGEBEN`, `RECHNUNG_BREGRUENDET_KORREKT`, `KORREKTE_ARTIKEL_ID_FUER_ABRECHNUNG_STORNIERTER_SPERRAUFTRAG_ANGEGEBEN`, `ABRECHNUNG_BLINDARBEIT_SPARTE_GAS_NICHT_RELEVANT`, `SONSTIGES`</Werte> | Angabe des Handelsunstimmigkeitsgrunds |
| <a id="hinweis"></a>`hinweis` | string | Hinweis zum Grund |
| <a id="referenzen"></a>`referenzen` | string[] | Referenzen auf vorherige Nachrichten |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[richtigkeit](/bo4e/202604/com/Handelsunstimmigkeitsbegruendung#richtigkeit)</span> | Handelsunstimmigkeitsrichtigkeit | [Enum Handelsunstimmigkeitsrichtigkeit](/bo4e/202604/enum/Handelsunstimmigkeitsrichtigkeit)<br/><Werte>`MSCONS`, `UTILMD`, `INVOIC`, `ORDERS`, `PRICAT`, `IFTSTA`, `ORDCHG`</Werte> |
| <span className="hbs-f hbs-e0">[referenzDar](/bo4e/202604/com/Handelsunstimmigkeitsbegruendung#referenzdar)</span> | Referenzierte Datenaustauschreferenz | string |
| <span className="hbs-f hbs-e0">[referenznummer](/bo4e/202604/com/Handelsunstimmigkeitsbegruendung#referenznummer)</span> | Referenznummer der Nachricht | string |
| <span className="hbs-f hbs-e0">[bestaetigungDar](/bo4e/202604/com/Handelsunstimmigkeitsbegruendung#bestaetigungdar)</span> | bestätigte Datenaustauschreferenz | string |
| <span className="hbs-f hbs-e0">[anerkennungsmeldung](/bo4e/202604/com/Handelsunstimmigkeitsbegruendung#anerkennungsmeldung)</span> | Nachrichtennummer aus der Anerkennungsmeldung (APERAK) | string |
| <span className="hbs-f hbs-e0">[grund](/bo4e/202604/com/Handelsunstimmigkeitsbegruendung#grund)</span> | Angabe des Handelsunstimmigkeitsgrunds | [Enum Handelsunstimmigkeitsgrund](/bo4e/202604/enum/Handelsunstimmigkeitsgrund)<br/><Werte>`ANMELDUNG_BESTAETIGT`, `ABRECHNUNGSBEGINN_GLEICH_BESTAETIGTEM_VERTRAGSBEGINN`, `ABRECHNUNGSENDE_GLEICH_BESTAETIGTEM_VERTRAGSENDE`, `NN_MSCONS_UEBERSENDET`, `RICHTIGE_MESSWERTE_ENERGIEMENGEN_UEBERSENDET`, `SONSTIGES_SIEHE_BEGRUENDUNG`, `GUELTIGES_PREISBLATT_VERSENDET`, `GUELTIGER_SPERRAUFTRAG_VORHANDEN`, `KORREKTE_ARTIKEL_ID_IN_RECHNUNG`, `KORREKTER_PREIS_ZU_GUELTIGEM_PREISBLATT_IN_RECHNUNG`, `RECHNUNG_KORREKT_A05`, `RECHNUNG_KORREKT_A10`, `RECHNUNG_KORREKT_A11`, `GUELTIGES_PREISBLATT_FRISTGERECHT_VERSENDET`, `GUELTIGE_RECHNUNG_VORHANDEN`, `ARTIKEL_ID_FUER_VERZUGSKOSTEN_VERWENDET`, `KORREKTER_PREIS_IN_RECHNUNG_ABGERECHNET`, `GUELTIGES_PREISBLATT_BLINDARBEIT_VERSENDET`, `KORREKTE_ARTIKEL_ID_IST_ANGEGEBEN`, `RECHNUNG_BREGRUENDET_KORREKT`, `KORREKTE_ARTIKEL_ID_FUER_ABRECHNUNG_STORNIERTER_SPERRAUFTRAG_ANGEGEBEN`, `ABRECHNUNG_BLINDARBEIT_SPARTE_GAS_NICHT_RELEVANT`, `SONSTIGES`</Werte> |
| <span className="hbs-f hbs-e0">[hinweis](/bo4e/202604/com/Handelsunstimmigkeitsbegruendung#hinweis)</span> | Hinweis zum Grund | string |
| <span className="hbs-f hbs-e0">[referenzen](/bo4e/202604/com/Handelsunstimmigkeitsbegruendung#referenzen) <span className="hbs-liste">[ ]</span></span> | Referenzen auf vorherige Nachrichten | string[] |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### richtigkeit

1 Verwendung(en) in den Nachrichtentypen COMDIS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_29001](/schnittstellen/202604/pruefi/COMDIS/PI_29001) | Prüfi | COMDIS | stammdaten › HANDELSUNSTIMMIGKEIT › begruendung |

### referenzDar

1 Verwendung(en) in den Nachrichtentypen COMDIS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_29001](/schnittstellen/202604/pruefi/COMDIS/PI_29001) | Prüfi | COMDIS | stammdaten › HANDELSUNSTIMMIGKEIT › begruendung |

### referenznummer

1 Verwendung(en) in den Nachrichtentypen COMDIS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_29001](/schnittstellen/202604/pruefi/COMDIS/PI_29001) | Prüfi | COMDIS | stammdaten › HANDELSUNSTIMMIGKEIT › begruendung |

### bestaetigungDar

1 Verwendung(en) in den Nachrichtentypen COMDIS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_29001](/schnittstellen/202604/pruefi/COMDIS/PI_29001) | Prüfi | COMDIS | stammdaten › HANDELSUNSTIMMIGKEIT › begruendung |

### anerkennungsmeldung

1 Verwendung(en) in den Nachrichtentypen COMDIS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_29001](/schnittstellen/202604/pruefi/COMDIS/PI_29001) | Prüfi | COMDIS | stammdaten › HANDELSUNSTIMMIGKEIT › begruendung |

### grund

2 Verwendung(en) in den Nachrichtentypen COMDIS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_29001](/schnittstellen/202604/pruefi/COMDIS/PI_29001) | Prüfi | COMDIS | stammdaten › HANDELSUNSTIMMIGKEIT › begruendung |
| [PI_29002](/schnittstellen/202604/pruefi/COMDIS/PI_29002) | Prüfi | COMDIS | stammdaten › HANDELSUNSTIMMIGKEIT › begruendung |

### hinweis

2 Verwendung(en) in den Nachrichtentypen COMDIS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_29001](/schnittstellen/202604/pruefi/COMDIS/PI_29001) | Prüfi | COMDIS | stammdaten › HANDELSUNSTIMMIGKEIT › begruendung |
| [PI_29002](/schnittstellen/202604/pruefi/COMDIS/PI_29002) | Prüfi | COMDIS | stammdaten › HANDELSUNSTIMMIGKEIT › begruendung |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
