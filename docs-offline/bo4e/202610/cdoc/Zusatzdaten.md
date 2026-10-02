# Zusatzdaten
<span hidden data-pagefind-meta={"title:Zusatzdaten — BO4E-Dokumentobjekt (FV 202610)"} />

BO4E-Dokumentobjekt · 10 Felder · 0 Verwendungen in Prüfis und Events · 208 namensgleiche Felder inline definiert

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung | Inline definiert |
|---|---|---|---|
| <a id="prozessid"></a>`prozessId` | string | Id des Dokuments / Beleges im Backend. Wird genutzt um die Antwort zuzuordnen. *(nicht aus der Zeitscheibe; Quelle: api-definitionen/schema-eigen/backend-schreiben-lf.yaml)* Wortgleich in `backend-schreiben-msb.yaml` und `backend-schreiben-nb.yaml`, in den Schemata „ZUSATZDATEN ( SST erstellen)" und „ZUSATZDATEN ( SST Aktualisieren)" als `zusatzdaten.prozessId` (`nullable`, dort nicht Pflicht). Das ist ein namensgleiches Feld in einem API-Schema, keine Verwendung des cdoc-Objekts. In den MaloIdent-Antworten 03002/03003 derselben Datei lautet der Text abweichend „Referenz Id der Anfrage Dokuments / Beleges im Backend. Kann genutzt werden um die Antwort zuzuordnen." und das Feld ist Pflicht. | 104 (inline) |
| <a id="eventname"></a>`eventname` | [EventName](/bo4e/202610/cdoc/EventName)<br/><Werte>`ECS_LIEFERBEGINN`, `START_MALOIDENT`, `START_KUENDIGUNG`, `START_LIEFERBEGINN`, `START_LIEFERENDE`, `START_VERSAND_SDAE`, `START_ABMELDEANFRAGE`, `START_AUFH_ZUK_ZUORDNUNG`, `START_ENDE_ZUORDNUNG`, `START_ABR_NN`, `START_ABR_BK`, `START_EINRICHTUNG_KONFIG`, `START_BERECHNUNGSFORMEL`, `START_WIEDERHERST_LB`, `START_EOG`, `START_ANFORDERUNG_MESSWERTE`, `START_BESTELLUNG_ABRECHNUNGSDATEN`, `START_ERHEBUNG_MESSWERTE`, `START_BESTELLUNG_SDAE`, `START_VERSAND_LIEFERSCHEIN`, `START_VERSAND_ANTWORT_NNA`, `START_ANFRAGE_KONFIGURATION`, `START_BESTELLUNG_KONFIGURATION`, `START_BESTELLUNG_ANGEBOT_KONFIGURATION`, `START_BESTELLUNG_ZAEHLZEITDEFINITION`, `START_VERSAND_BESTANDSLISTE`, `START_VERSAND_ANF_STORNO`, `START_VERSAND_BEST_BEEND_KONFIG`, `START_VERSAND_STORNO_MSCONS`, `START_BEGINN_MSB`, `START_ENDE_MSB`, `START_ENDE_MSB_STILLLEGUNG`, `START_KUENDIGUNG_MSB`, `START_GESCHAEFTSDATENANFRAGE`, `START_VERSAND_PREISBLATT_IMS`, `START_UEBERMITTLUNG_ENFG`, `START_PARTIN`, `START_GERAETEUEBERNAHME`, `START_ANGEBOT_GERAETEUEBERNAHME`, `START_BESTELLUNG_GERAETEUEBERNAHME`, `START_UEBERM_DEFINITION`, `START_UEBERSICHT_LEISTUNGSKURVENDEF`, `START_UEBERSICHT_SCHALTZEITDEF`, `START_UEBERSICHT_ZAEHLZEITDEF`, `START_REKLAMATION_DEFINITION`, `START_VERSAND_STATUSMELDUNG`, `START_GERAETEWECHSEL`, `START_ANTWORT_GERAETEWECHSEL`, `START_ANFORDERUNG_VON_WERTEN`, `START_REKLAMATION_VON_WERTEN`, `START_ABO_PROFILE`</Werte> | Identifikation des Events | 104 (inline) |
| <a id="edityp"></a>`ediTyp` | string | — | — |
| <a id="ediempfangsdatum"></a>`ediEmpfangsDatum` | string (date-time) | — | — |
| <a id="ediversion"></a>`ediVersion` | string | — | — |
| <a id="marktpartnerrolle"></a>`marktpartnerRolle` | [Enum Marktrolle](/bo4e/202610/enum/Marktrolle)<br/><Werte>`NB`, `LF`, `MSB`, `MSBA`, `GMSB`, `MDL`, `DL`, `BKV`, `UENB`, `KUNDE-SELBST-NN`, `MGV`, `EIV`, `RB`, `KUNDE`, `INTERESSENT`, `KN`, `UBA`, `BIKO`, `ESA`</Werte> | Diese Rollen kann ein Marktteilnehmer einnehmen | — |
| <a id="contrlreferenz"></a>`contrlReferenz` | string | Dieses Feld ist ohne Beschreibung, ohne Verwendung. Die Zeitscheibe gibt ihm keinen Text, und in den Schnittstellen-Spezifikationen, die diese Dokumentation liest, kommt es nicht vor. *(nicht aus der Zeitscheibe; Quelle: Messung am 05.09.2026 über site-d/apis/ (16 Spezifikationen), _apidog-export/ (322 Dateien), api-definitionen/ (13 Dateien) und den Testbestand)* 0 Vorkommen in allen vier Beständen; in diesem Repository nur in der BO4E-Definition selbst und im Bundle. Anders als bei `parentBusinessKey` fehlt zusätzlich jede englische Entsprechung. | — |
| <a id="parentbusinesskey"></a>`parentBusinessKey` | string | Dieses Feld ist ohne belegbare Bedeutung in den Quellen. Es steht in der BO4E-Definition; was es tragen soll, sagt keine Quelle, die diese Dokumentation liest. *(nicht aus der Zeitscheibe; Quelle: Messung am 05.09.2026 über site-d/apis/ (16 Spezifikationen), _apidog-export/ (322 Dateien), api-definitionen/ (13 Dateien) und den Testbestand)* 0 Vorkommen in allen vier Beständen. Die einzigen Fundstellen in diesem Repository sind die BO4E-Definition selbst (`_sources/v<fv>/bo4e/cdoc/Zusatzdaten.yaml`, das Feldatom und das Bundle) sowie ihre englische Fassung. Erfundene Bedeutung steht hier ausdrücklich nicht. | — |
| <a id="targetbusinesskey"></a>`targetBusinessKey` | string | Id des initial referenzierenden Prozesses. *(nicht aus der Zeitscheibe; Quelle: api-definitionen/schema-eigen/backend-schreiben-lf.yaml)* Wortgleich in `backend-schreiben-msb.yaml` und `backend-schreiben-nb.yaml` als `zusatzdaten.targetBusinessKey`; Pflicht allein im Schema „ZUSATZDATEN ( SST Aktualisieren)". In den MaloIdent-Antworten 03002/03003 heißt dasselbe Feld „BusinessKey des initialen Prozesses" und ist Pflicht. Auch das sind namensgleiche Felder in API-Schemata, keine Verwendung des cdoc-Objekts. | — |
| <a id="ermaechtigungvorhanden"></a>`ermaechtigungVorhanden` | boolean | Rückmeldung der SST Lesen_Zuordnungsermächtigung mit Information ob Zuordnungsermächtigung vorliegt | — |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[prozessId](/bo4e/202610/cdoc/Zusatzdaten#prozessid)</span> | Id des Dokuments / Beleges im Backend. Wird genutzt um die Antwort zuzuordnen. *(nicht aus der Zeitscheibe; Quelle: api-definitionen/schema-eigen/backend-schreiben-lf.yaml)* Wortgleich in `backend-schreiben-msb.yaml` und `backend-schreiben-nb.yaml`, in den Schemata „ZUSATZDATEN ( SST erstellen)" und „ZUSATZDATEN ( SST Aktualisieren)" als `zusatzdaten.prozessId` (`nullable`, dort nicht Pflicht). Das ist ein namensgleiches Feld in einem API-Schema, keine Verwendung des cdoc-Objekts. In den MaloIdent-Antworten 03002/03003 derselben Datei lautet der Text abweichend „Referenz Id der Anfrage Dokuments / Beleges im Backend. Kann genutzt werden um die Antwort zuzuordnen." und das Feld ist Pflicht. | string |
| <span className="hbs-f hbs-e0">[eventname](/bo4e/202610/cdoc/Zusatzdaten#eventname)</span> | Identifikation des Events | [EventName](/bo4e/202610/cdoc/EventName)<br/><Werte>`ECS_LIEFERBEGINN`, `START_MALOIDENT`, `START_KUENDIGUNG`, `START_LIEFERBEGINN`, `START_LIEFERENDE`, `START_VERSAND_SDAE`, `START_ABMELDEANFRAGE`, `START_AUFH_ZUK_ZUORDNUNG`, `START_ENDE_ZUORDNUNG`, `START_ABR_NN`, `START_ABR_BK`, `START_EINRICHTUNG_KONFIG`, `START_BERECHNUNGSFORMEL`, `START_WIEDERHERST_LB`, `START_EOG`, `START_ANFORDERUNG_MESSWERTE`, `START_BESTELLUNG_ABRECHNUNGSDATEN`, `START_ERHEBUNG_MESSWERTE`, `START_BESTELLUNG_SDAE`, `START_VERSAND_LIEFERSCHEIN`, `START_VERSAND_ANTWORT_NNA`, `START_ANFRAGE_KONFIGURATION`, `START_BESTELLUNG_KONFIGURATION`, `START_BESTELLUNG_ANGEBOT_KONFIGURATION`, `START_BESTELLUNG_ZAEHLZEITDEFINITION`, `START_VERSAND_BESTANDSLISTE`, `START_VERSAND_ANF_STORNO`, `START_VERSAND_BEST_BEEND_KONFIG`, `START_VERSAND_STORNO_MSCONS`, `START_BEGINN_MSB`, `START_ENDE_MSB`, `START_ENDE_MSB_STILLLEGUNG`, `START_KUENDIGUNG_MSB`, `START_GESCHAEFTSDATENANFRAGE`, `START_VERSAND_PREISBLATT_IMS`, `START_UEBERMITTLUNG_ENFG`, `START_PARTIN`, `START_GERAETEUEBERNAHME`, `START_ANGEBOT_GERAETEUEBERNAHME`, `START_BESTELLUNG_GERAETEUEBERNAHME`, `START_UEBERM_DEFINITION`, `START_UEBERSICHT_LEISTUNGSKURVENDEF`, `START_UEBERSICHT_SCHALTZEITDEF`, `START_UEBERSICHT_ZAEHLZEITDEF`, `START_REKLAMATION_DEFINITION`, `START_VERSAND_STATUSMELDUNG`, `START_GERAETEWECHSEL`, `START_ANTWORT_GERAETEWECHSEL`, `START_ANFORDERUNG_VON_WERTEN`, `START_REKLAMATION_VON_WERTEN`, `START_ABO_PROFILE`</Werte> |
| <span className="hbs-f hbs-e0">[ediTyp](/bo4e/202610/cdoc/Zusatzdaten#edityp)</span> | — | string |
| <span className="hbs-f hbs-e0">[ediEmpfangsDatum](/bo4e/202610/cdoc/Zusatzdaten#ediempfangsdatum)</span> | — | string (date-time) |
| <span className="hbs-f hbs-e0">[ediVersion](/bo4e/202610/cdoc/Zusatzdaten#ediversion)</span> | — | string |
| <span className="hbs-f hbs-e0">[marktpartnerRolle](/bo4e/202610/cdoc/Zusatzdaten#marktpartnerrolle)</span> | Diese Rollen kann ein Marktteilnehmer einnehmen | [Enum Marktrolle](/bo4e/202610/enum/Marktrolle)<br/><Werte>`NB`, `LF`, `MSB`, `MSBA`, `GMSB`, `MDL`, `DL`, `BKV`, `UENB`, `KUNDE-SELBST-NN`, `MGV`, `EIV`, `RB`, `KUNDE`, `INTERESSENT`, `KN`, `UBA`, `BIKO`, `ESA`</Werte> |
| <span className="hbs-f hbs-e0">[contrlReferenz](/bo4e/202610/cdoc/Zusatzdaten#contrlreferenz)</span> | Dieses Feld ist ohne Beschreibung, ohne Verwendung. Die Zeitscheibe gibt ihm keinen Text, und in den Schnittstellen-Spezifikationen, die diese Dokumentation liest, kommt es nicht vor. *(nicht aus der Zeitscheibe; Quelle: Messung am 05.09.2026 über site-d/apis/ (16 Spezifikationen), _apidog-export/ (322 Dateien), api-definitionen/ (13 Dateien) und den Testbestand)* 0 Vorkommen in allen vier Beständen; in diesem Repository nur in der BO4E-Definition selbst und im Bundle. Anders als bei `parentBusinessKey` fehlt zusätzlich jede englische Entsprechung. | string |
| <span className="hbs-f hbs-e0">[parentBusinessKey](/bo4e/202610/cdoc/Zusatzdaten#parentbusinesskey)</span> | Dieses Feld ist ohne belegbare Bedeutung in den Quellen. Es steht in der BO4E-Definition; was es tragen soll, sagt keine Quelle, die diese Dokumentation liest. *(nicht aus der Zeitscheibe; Quelle: Messung am 05.09.2026 über site-d/apis/ (16 Spezifikationen), _apidog-export/ (322 Dateien), api-definitionen/ (13 Dateien) und den Testbestand)* 0 Vorkommen in allen vier Beständen. Die einzigen Fundstellen in diesem Repository sind die BO4E-Definition selbst (`_sources/v<fv>/bo4e/cdoc/Zusatzdaten.yaml`, das Feldatom und das Bundle) sowie ihre englische Fassung. Erfundene Bedeutung steht hier ausdrücklich nicht. | string |
| <span className="hbs-f hbs-e0">[targetBusinessKey](/bo4e/202610/cdoc/Zusatzdaten#targetbusinesskey)</span> | Id des initial referenzierenden Prozesses. *(nicht aus der Zeitscheibe; Quelle: api-definitionen/schema-eigen/backend-schreiben-lf.yaml)* Wortgleich in `backend-schreiben-msb.yaml` und `backend-schreiben-nb.yaml` als `zusatzdaten.targetBusinessKey`; Pflicht allein im Schema „ZUSATZDATEN ( SST Aktualisieren)". In den MaloIdent-Antworten 03002/03003 heißt dasselbe Feld „BusinessKey des initialen Prozesses" und ist Pflicht. Auch das sind namensgleiche Felder in API-Schemata, keine Verwendung des cdoc-Objekts. | string |
| <span className="hbs-f hbs-e0">[ermaechtigungVorhanden](/bo4e/202610/cdoc/Zusatzdaten#ermaechtigungvorhanden)</span> | Rückmeldung der SST Lesen_Zuordnungsermächtigung mit Information ob Zuordnungsermächtigung vorliegt | boolean |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Namensgleich inline definiert

### prozessId

104 Quelle(n) definieren ein Feld `prozessId` inline.

| Definiert in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [[LF] START_ABO_PROFILE](/schnittstellen/202610/trigger/events/LF-START_ABO_PROFILE) | Event | — | zusatzdaten |
| [[LF] START_ABR_NN](/schnittstellen/202610/trigger/events/LF-START_ABR_NN) | Event | — | zusatzdaten |
| [[LF] START_ANFORDERUNG_VON_WERTEN](/schnittstellen/202610/trigger/events/LF-START_ANFORDERUNG_VON_WERTEN) | Event | — | zusatzdaten |
| [[LF] START_ANFRAGE_KONFIGURATION](/schnittstellen/202610/trigger/events/LF-START_ANFRAGE_KONFIGURATION) | Event | — | zusatzdaten |
| [[LF] START_ANFRAGE_MESSWERTE](/schnittstellen/202610/trigger/events/LF-START_ANFRAGE_MESSWERTE) | Event | — | zusatzdaten |
| [[LF] START_ANFRAGE_SPERRUNG](/schnittstellen/202610/trigger/events/LF-START_ANFRAGE_SPERRUNG) | Event | — | zusatzdaten |
| [[LF] START_ANFRAGE_STAMMDATENAENDERUNG GAS](/schnittstellen/202610/trigger/events/LF-START_ANFRAGE_STAMMDATENAENDERUNG-GAS) | Event | — | zusatzdaten |
| [[LF] START_ANFRAGE_STAMMDATEN_MALO](/schnittstellen/202610/trigger/events/LF-START_ANFRAGE_STAMMDATEN_MALO) | Event | — | zusatzdaten |
| [[LF] START_ANFRAGE_STAMMDATEN_TRANCHE](/schnittstellen/202610/trigger/events/LF-START_ANFRAGE_STAMMDATEN_TRANCHE) | Event | — | zusatzdaten |
| [[LF] START_ANF_BRENNW_ZUSTANDSZAHL](/schnittstellen/202610/trigger/events/LF-START_ANF_BRENNW_ZUSTANDSZAHL) | Event | — | zusatzdaten |
| [[LF] START_BEENDIGUNG_RECHNUNG_MSB](/schnittstellen/202610/trigger/events/LF-START_BEENDIGUNG_RECHNUNG_MSB) | Event | — | zusatzdaten |
| [[LF] START_BESTELLUNG_ABRECHNUNGSDATEN](/schnittstellen/202610/trigger/events/LF-START_BESTELLUNG_ABRECHNUNGSDATEN) | Event | — | zusatzdaten |
| [[LF] START_BESTELLUNG_AEND_PROGNOSEGRUNDLAGE](/schnittstellen/202610/trigger/events/LF-START_BESTELLUNG_AEND_PROGNOSEGRUNDLAGE) | Event | — | zusatzdaten |
| [[LF] START_BESTELLUNG_ANGEBOT_KONFIGURATION](/schnittstellen/202610/trigger/events/LF-START_BESTELLUNG_ANGEBOT_KONFIGURATION) | Event | — | zusatzdaten |
| [[LF] START_BESTELLUNG_KONFIGURATION](/schnittstellen/202610/trigger/events/LF-START_BESTELLUNG_KONFIGURATION) | Event | — | zusatzdaten |
| [[LF] START_BESTELLUNG_SDAE](/schnittstellen/202610/trigger/events/LF-START_BESTELLUNG_SDAE) | Event | — | zusatzdaten |
| [[LF] START_BESTELLUNG_ZAEHLZEITDEFINITION](/schnittstellen/202610/trigger/events/LF-START_BESTELLUNG_ZAEHLZEITDEFINITION) | Event | — | zusatzdaten |
| [[LF] START_BEST_AEND_ABR_DATEN](/schnittstellen/202610/trigger/events/LF-START_BEST_AEND_ABR_DATEN) | Event | — | zusatzdaten |
| [[LF] START_BEST_AEND_TK](/schnittstellen/202610/trigger/events/LF-START_BEST_AEND_TK) | Event | — | zusatzdaten |
| [[LF] START_ENTSPERRAUFTRAG](/schnittstellen/202610/trigger/events/LF-START_ENTSPERRAUFTRAG) | Event | — | zusatzdaten |
| [[LF] START_ERHEBUNG_MESSWERTE](/schnittstellen/202610/trigger/events/LF-START_ERHEBUNG_MESSWERTE) | Event | — | zusatzdaten |
| [[LF] START_GESCHAEFTSDATENANFRAGE](/schnittstellen/202610/trigger/events/LF-START_GESCHAEFTSDATENANFRAGE) | Event | — | zusatzdaten |
| [[LF] START_KUENDIGUNG](/schnittstellen/202610/trigger/events/LF-START_KUENDIGUNG) | Event | — | zusatzdaten |
| [[LF] START_LIEFERBEGINN](/schnittstellen/202610/trigger/events/LF-START_LIEFERBEGINN) | Event | — | zusatzdaten |
| [[LF] START_LIEFERENDE](/schnittstellen/202610/trigger/events/LF-START_LIEFERENDE) | Event | — | zusatzdaten |
| [[LF] START_MALOIDENT](/schnittstellen/202610/trigger/events/LF-START_MALOIDENT) | Event | — | zusatzdaten |
| [[LF] START_PARTIN](/schnittstellen/202610/trigger/events/LF-START_PARTIN) | Event | — | zusatzdaten |
| [[LF] START_REKLAMATION_DEFINITIONEN](/schnittstellen/202610/trigger/events/LF-START_REKLAMATION_DEFINITIONEN) | Event | — | zusatzdaten |
| [[LF] START_REKLAMATION_VON_WERTEN](/schnittstellen/202610/trigger/events/LF-START_REKLAMATION_VON_WERTEN) | Event | — | zusatzdaten |
| [[LF] START_REKLAMATION_WERTE](/schnittstellen/202610/trigger/events/LF-START_REKLAMATION_WERTE) | Event | — | zusatzdaten |
| [[LF] START_SPERRAUFTRAG](/schnittstellen/202610/trigger/events/LF-START_SPERRAUFTRAG) | Event | — | zusatzdaten |
| [[LF] START_STORNO_AUFTRAG](/schnittstellen/202610/trigger/events/LF-START_STORNO_AUFTRAG) | Event | — | zusatzdaten |
| [[LF] START_STORNO_SE_AUFTRAG](/schnittstellen/202610/trigger/events/LF-START_STORNO_SE_AUFTRAG) | Event | — | zusatzdaten |
| [[LF] START_UEBERMITTLUNG_ENFG](/schnittstellen/202610/trigger/events/LF-START_UEBERMITTLUNG_ENFG) | Event | — | zusatzdaten |
| [[LF] START_UEBERM_DEFINITION](/schnittstellen/202610/trigger/events/LF-START_UEBERM_DEFINITION) | Event | — | zusatzdaten |
| [[LF] START_UEBERSICHT_LEISTUNGSKURVENDEF](/schnittstellen/202610/trigger/events/LF-START_UEBERSICHT_LEISTUNGSKURVENDEF) | Event | — | zusatzdaten |
| [[LF] START_UEBERSICHT_SCHALTZEITDEF](/schnittstellen/202610/trigger/events/LF-START_UEBERSICHT_SCHALTZEITDEF) | Event | — | zusatzdaten |
| [[LF] START_UEBERSICHT_ZAEHLZEITDEF](/schnittstellen/202610/trigger/events/LF-START_UEBERSICHT_ZAEHLZEITDEF) | Event | — | zusatzdaten |
| [[LF] START_VERSAND_ANF_STORNO](/schnittstellen/202610/trigger/events/LF-START_VERSAND_ANF_STORNO) | Event | — | zusatzdaten |
| [[LF] START_VERSAND_ANTWORT_NNA](/schnittstellen/202610/trigger/events/LF-START_VERSAND_ANTWORT_NNA) | Event | — | zusatzdaten |
| [[LF] START_VERSAND_BEST_BEEND_KONFIG](/schnittstellen/202610/trigger/events/LF-START_VERSAND_BEST_BEEND_KONFIG) | Event | — | zusatzdaten |
| [[LF] START_VERSAND_SDAE](/schnittstellen/202610/trigger/events/LF-START_VERSAND_SDAE) | Event | — | zusatzdaten |
| [[LF] START_VERSAND_STOERUNGSMELDUNG](/schnittstellen/202610/trigger/events/LF-START_VERSAND_STOERUNGSMELDUNG) | Event | — | zusatzdaten |
| [[LF] START_VERSAND_STORNO_MSCONS](/schnittstellen/202610/trigger/events/LF-START_VERSAND_STORNO_MSCONS) | Event | — | zusatzdaten |
| [[MSB] START_ANFORDERUNG_MESSWERTE](/schnittstellen/202610/trigger/events/MSB-START_ANFORDERUNG_MESSWERTE) | Event | — | zusatzdaten |
| [[MSB] START_ANGEBOT_GERAETEUEBERNAHME](/schnittstellen/202610/trigger/events/MSB-START_ANGEBOT_GERAETEUEBERNAHME) | Event | — | zusatzdaten |
| [[MSB] START_ANTWORT_GERAETEWECHSEL](/schnittstellen/202610/trigger/events/MSB-START_ANTWORT_GERAETEWECHSEL) | Event | — | zusatzdaten |
| [[MSB] START_BEEND_RE_MSB](/schnittstellen/202610/trigger/events/MSB-START_BEEND_RE_MSB) | Event | — | zusatzdaten |
| [[MSB] START_BEGINN_MSB](/schnittstellen/202610/trigger/events/MSB-START_BEGINN_MSB) | Event | — | zusatzdaten |
| [[MSB] START_BESTELLUNG_GERAETEUEBERNAHME](/schnittstellen/202610/trigger/events/MSB-START_BESTELLUNG_GERAETEUEBERNAHME) | Event | — | zusatzdaten |
| [[MSB] START_BESTELLUNG_SDAE GAS](/schnittstellen/202610/trigger/events/MSB-START_BESTELLUNG_SDAE-GAS) | Event | — | zusatzdaten |
| [[MSB] START_ENDE_MSB](/schnittstellen/202610/trigger/events/MSB-START_ENDE_MSB) | Event | — | zusatzdaten |
| [[MSB] START_ERHEBUNG_MESSWERTE](/schnittstellen/202610/trigger/events/MSB-START_ERHEBUNG_MESSWERTE) | Event | — | zusatzdaten |
| [[MSB] START_GERAETEUEBERNAHME](/schnittstellen/202610/trigger/events/MSB-START_GERAETEUEBERNAHME) | Event | — | zusatzdaten |
| [[MSB] START_GERAETEWECHSEL](/schnittstellen/202610/trigger/events/MSB-START_GERAETEWECHSEL) | Event | — | zusatzdaten |
| [[MSB] START_GESCHAEFTSDATENANFRAGE](/schnittstellen/202610/trigger/events/MSB-START_GESCHAEFTSDATENANFRAGE) | Event | — | zusatzdaten |
| [[MSB] START_KUENDIGUNG_MSB](/schnittstellen/202610/trigger/events/MSB-START_KUENDIGUNG_MSB) | Event | — | zusatzdaten |
| [[MSB] START_MESSWERTUEBERMITTLUNG](/schnittstellen/202610/trigger/events/MSB-START_MESSWERTUEBERMITTLUNG) | Event | — | zusatzdaten |
| [[MSB] START_PARTIN](/schnittstellen/202610/trigger/events/MSB-START_PARTIN) | Event | — | zusatzdaten |
| [[MSB] START_REKLAMATION_DEFINITION](/schnittstellen/202610/trigger/events/MSB-START_REKLAMATION_DEFINITION) | Event | — | zusatzdaten |
| [[MSB] START_VERSAND_ANF_STORNO](/schnittstellen/202610/trigger/events/MSB-START_VERSAND_ANF_STORNO) | Event | — | zusatzdaten |
| [[MSB] START_VERSAND_BEED_WERTE](/schnittstellen/202610/trigger/events/MSB-START_VERSAND_BEED_WERTE) | Event | — | zusatzdaten |
| [[MSB] START_VERSAND_PREISBLATT_IMS](/schnittstellen/202610/trigger/events/MSB-START_VERSAND_PREISBLATT_IMS) | Event | — | zusatzdaten |
| [[MSB] START_VERSAND_RECHNUNG](/schnittstellen/202610/trigger/events/MSB-START_VERSAND_RECHNUNG) | Event | — | zusatzdaten |
| [[MSB] START_VERSAND_SDAE](/schnittstellen/202610/trigger/events/MSB-START_VERSAND_SDAE) | Event | — | zusatzdaten |
| [[MSB] START_VERSAND_STORNO_MSCONS](/schnittstellen/202610/trigger/events/MSB-START_VERSAND_STORNO_MSCONS) | Event | — | zusatzdaten |
| [[NB] START_ABR_BK](/schnittstellen/202610/trigger/events/NB-START_ABR_BK) | Event | — | zusatzdaten |
| [[NB] START_ABR_NN](/schnittstellen/202610/trigger/events/NB-START_ABR_NN) | Event | — | zusatzdaten |
| [[NB] START_ANFORDERUNG_MESSWERTE](/schnittstellen/202610/trigger/events/NB-START_ANFORDERUNG_MESSWERTE) | Event | — | zusatzdaten |
| [[NB] START_ANFRAGE_MESSWERTE_NB](/schnittstellen/202610/trigger/events/NB-START_ANFRAGE_MESSWERTE_NB) | Event | — | zusatzdaten |
| [[NB] START_ANFRAGE_SPERRUNG](/schnittstellen/202610/trigger/events/NB-START_ANFRAGE_SPERRUNG) | Event | — | zusatzdaten |
| [[NB] START_ANFRAGE_STAMMDATENAENDERUNG GAS](/schnittstellen/202610/trigger/events/NB-START_ANFRAGE_STAMMDATENAENDERUNG-GAS) | Event | — | zusatzdaten |
| [[NB] START_AUFH_ZUK_ZUORDNUNG](/schnittstellen/202610/trigger/events/NB-START_AUFH_ZUK_ZUORDNUNG) | Event | — | zusatzdaten |
| [[NB] START_AUFTRAGSSTATUS](/schnittstellen/202610/trigger/events/NB-START_AUFTRAGSSTATUS) | Event | — | zusatzdaten |
| [[NB] START_BERECHNUNGSFORMEL](/schnittstellen/202610/trigger/events/NB-START_BERECHNUNGSFORMEL) | Event | — | zusatzdaten |
| [[NB] START_BESTELLUNG_SDAE](/schnittstellen/202610/trigger/events/NB-START_BESTELLUNG_SDAE) | Event | — | zusatzdaten |
| [[NB] START_BEST_AEND_TK](/schnittstellen/202610/trigger/events/NB-START_BEST_AEND_TK) | Event | — | zusatzdaten |
| [[NB] START_EINRICHTUNG_KONFIG](/schnittstellen/202610/trigger/events/NB-START_EINRICHTUNG_KONFIG) | Event | — | zusatzdaten |
| [[NB] START_EINRICHTUNG_KONFIGURATION_ZUORDNUNG_LF_VON_NB](/schnittstellen/202610/trigger/events/NB-START_EINRICHTUNG_KONFIGURATION_ZUORDNUNG_LF_VON_NB) | Event | — | zusatzdaten |
| [[NB] START_ENDE_MSB_STILLLEGUNG GAS](/schnittstellen/202610/trigger/events/NB-START_ENDE_MSB_STILLLEGUNG-GAS) | Event | — | zusatzdaten |
| [[NB] START_ENDE_ZUORDNUNG](/schnittstellen/202610/trigger/events/NB-START_ENDE_ZUORDNUNG) | Event | — | zusatzdaten |
| [[NB] START_EOG](/schnittstellen/202610/trigger/events/NB-START_EOG) | Event | — | zusatzdaten |
| [[NB] START_ERHEBUNG_MESSWERTE](/schnittstellen/202610/trigger/events/NB-START_ERHEBUNG_MESSWERTE) | Event | — | zusatzdaten |
| [[NB] START_LIEFERENDE](/schnittstellen/202610/trigger/events/NB-START_LIEFERENDE) | Event | — | zusatzdaten |
| [[NB] START_PREISBLATT](/schnittstellen/202610/trigger/events/NB-START_PREISBLATT) | Event | — | zusatzdaten |
| [[NB] START_REKLAMATION_WERTE](/schnittstellen/202610/trigger/events/NB-START_REKLAMATION_WERTE) | Event | — | zusatzdaten |
| [[NB] START_UEBERM_DEFINITION](/schnittstellen/202610/trigger/events/NB-START_UEBERM_DEFINITION) | Event | — | zusatzdaten |
| [[NB] START_UEBERSICHT_LEISTUNGSKURVENDEF](/schnittstellen/202610/trigger/events/NB-START_UEBERSICHT_LEISTUNGSKURVENDEF) | Event | — | zusatzdaten |
| [[NB] START_UEBERSICHT_SCHALTZEITDEF](/schnittstellen/202610/trigger/events/NB-START_UEBERSICHT_SCHALTZEITDEF) | Event | — | zusatzdaten |
| [[NB] START_UEBERSICHT_ZAEHLZEITDEF](/schnittstellen/202610/trigger/events/NB-START_UEBERSICHT_ZAEHLZEITDEF) | Event | — | zusatzdaten |
| [[NB] START_VERSAND_ANF_STORNO](/schnittstellen/202610/trigger/events/NB-START_VERSAND_ANF_STORNO) | Event | — | zusatzdaten |
| [[NB] START_VERSAND_BEARB_MELDUNG](/schnittstellen/202610/trigger/events/NB-START_VERSAND_BEARB_MELDUNG) | Event | — | zusatzdaten |
| [[NB] START_VERSAND_BEENDIGUNG_AGV](/schnittstellen/202610/trigger/events/NB-START_VERSAND_BEENDIGUNG_AGV) | Event | — | zusatzdaten |
| [[NB] START_VERSAND_BESTANDSLISTE GAS](/schnittstellen/202610/trigger/events/NB-START_VERSAND_BESTANDSLISTE-GAS) | Event | — | zusatzdaten |
| [[NB] START_VERSAND_COMDIS](/schnittstellen/202610/trigger/events/NB-START_VERSAND_COMDIS) | Event | — | zusatzdaten |
| [[NB] START_VERSAND_GEMESSENE_ARB_LEIST_WERTE](/schnittstellen/202610/trigger/events/NB-START_VERSAND_GEMESSENE_ARB_LEIST_WERTE) | Event | — | zusatzdaten |
| [[NB] START_VERSAND_LIEFERSCHEIN](/schnittstellen/202610/trigger/events/NB-START_VERSAND_LIEFERSCHEIN) | Event | — | zusatzdaten |
| [[NB] START_VERSAND_SDAE](/schnittstellen/202610/trigger/events/NB-START_VERSAND_SDAE) | Event | — | zusatzdaten |
| [[NB] START_VERSAND_STATUSMELDUNG](/schnittstellen/202610/trigger/events/NB-START_VERSAND_STATUSMELDUNG) | Event | — | zusatzdaten |
| [[NB] START_VERSAND_STOERUNGSMELDUNG_NB](/schnittstellen/202610/trigger/events/NB-START_VERSAND_STOERUNGSMELDUNG_NB) | Event | — | zusatzdaten |
| [[NB] START_VERSAND_STORNO_MSCONS](/schnittstellen/202610/trigger/events/NB-START_VERSAND_STORNO_MSCONS) | Event | — | zusatzdaten |
| [[NB] START_WIEDERHERST_LB](/schnittstellen/202610/trigger/events/NB-START_WIEDERHERST_LB) | Event | — | zusatzdaten |
| [[NB] START_WIEDERSPRUCH_ABLEHNUNG](/schnittstellen/202610/trigger/events/NB-START_WIEDERSPRUCH_ABLEHNUNG) | Event | — | zusatzdaten |
| [[NB] START_ZUORDNUNG_ERZ_MALO_TRANCHE](/schnittstellen/202610/trigger/events/NB-START_ZUORDNUNG_ERZ_MALO_TRANCHE) | Event | — | zusatzdaten |

### eventname

104 Quelle(n) definieren ein Feld `eventname` inline.

| Definiert in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [[LF] START_ABO_PROFILE](/schnittstellen/202610/trigger/events/LF-START_ABO_PROFILE) | Event | — | zusatzdaten |
| [[LF] START_ABR_NN](/schnittstellen/202610/trigger/events/LF-START_ABR_NN) | Event | — | zusatzdaten |
| [[LF] START_ANFORDERUNG_VON_WERTEN](/schnittstellen/202610/trigger/events/LF-START_ANFORDERUNG_VON_WERTEN) | Event | — | zusatzdaten |
| [[LF] START_ANFRAGE_KONFIGURATION](/schnittstellen/202610/trigger/events/LF-START_ANFRAGE_KONFIGURATION) | Event | — | zusatzdaten |
| [[LF] START_ANFRAGE_MESSWERTE](/schnittstellen/202610/trigger/events/LF-START_ANFRAGE_MESSWERTE) | Event | — | zusatzdaten |
| [[LF] START_ANFRAGE_SPERRUNG](/schnittstellen/202610/trigger/events/LF-START_ANFRAGE_SPERRUNG) | Event | — | zusatzdaten |
| [[LF] START_ANFRAGE_STAMMDATENAENDERUNG GAS](/schnittstellen/202610/trigger/events/LF-START_ANFRAGE_STAMMDATENAENDERUNG-GAS) | Event | — | zusatzdaten |
| [[LF] START_ANFRAGE_STAMMDATEN_MALO](/schnittstellen/202610/trigger/events/LF-START_ANFRAGE_STAMMDATEN_MALO) | Event | — | zusatzdaten |
| [[LF] START_ANFRAGE_STAMMDATEN_TRANCHE](/schnittstellen/202610/trigger/events/LF-START_ANFRAGE_STAMMDATEN_TRANCHE) | Event | — | zusatzdaten |
| [[LF] START_ANF_BRENNW_ZUSTANDSZAHL](/schnittstellen/202610/trigger/events/LF-START_ANF_BRENNW_ZUSTANDSZAHL) | Event | — | zusatzdaten |
| [[LF] START_BEENDIGUNG_RECHNUNG_MSB](/schnittstellen/202610/trigger/events/LF-START_BEENDIGUNG_RECHNUNG_MSB) | Event | — | zusatzdaten |
| [[LF] START_BESTELLUNG_ABRECHNUNGSDATEN](/schnittstellen/202610/trigger/events/LF-START_BESTELLUNG_ABRECHNUNGSDATEN) | Event | — | zusatzdaten |
| [[LF] START_BESTELLUNG_AEND_PROGNOSEGRUNDLAGE](/schnittstellen/202610/trigger/events/LF-START_BESTELLUNG_AEND_PROGNOSEGRUNDLAGE) | Event | — | zusatzdaten |
| [[LF] START_BESTELLUNG_ANGEBOT_KONFIGURATION](/schnittstellen/202610/trigger/events/LF-START_BESTELLUNG_ANGEBOT_KONFIGURATION) | Event | — | zusatzdaten |
| [[LF] START_BESTELLUNG_KONFIGURATION](/schnittstellen/202610/trigger/events/LF-START_BESTELLUNG_KONFIGURATION) | Event | — | zusatzdaten |
| [[LF] START_BESTELLUNG_SDAE](/schnittstellen/202610/trigger/events/LF-START_BESTELLUNG_SDAE) | Event | — | zusatzdaten |
| [[LF] START_BESTELLUNG_ZAEHLZEITDEFINITION](/schnittstellen/202610/trigger/events/LF-START_BESTELLUNG_ZAEHLZEITDEFINITION) | Event | — | zusatzdaten |
| [[LF] START_BEST_AEND_ABR_DATEN](/schnittstellen/202610/trigger/events/LF-START_BEST_AEND_ABR_DATEN) | Event | — | zusatzdaten |
| [[LF] START_BEST_AEND_TK](/schnittstellen/202610/trigger/events/LF-START_BEST_AEND_TK) | Event | — | zusatzdaten |
| [[LF] START_ENTSPERRAUFTRAG](/schnittstellen/202610/trigger/events/LF-START_ENTSPERRAUFTRAG) | Event | — | zusatzdaten |
| [[LF] START_ERHEBUNG_MESSWERTE](/schnittstellen/202610/trigger/events/LF-START_ERHEBUNG_MESSWERTE) | Event | — | zusatzdaten |
| [[LF] START_GESCHAEFTSDATENANFRAGE](/schnittstellen/202610/trigger/events/LF-START_GESCHAEFTSDATENANFRAGE) | Event | — | zusatzdaten |
| [[LF] START_KUENDIGUNG](/schnittstellen/202610/trigger/events/LF-START_KUENDIGUNG) | Event | — | zusatzdaten |
| [[LF] START_LIEFERBEGINN](/schnittstellen/202610/trigger/events/LF-START_LIEFERBEGINN) | Event | — | zusatzdaten |
| [[LF] START_LIEFERENDE](/schnittstellen/202610/trigger/events/LF-START_LIEFERENDE) | Event | — | zusatzdaten |
| [[LF] START_MALOIDENT](/schnittstellen/202610/trigger/events/LF-START_MALOIDENT) | Event | — | zusatzdaten |
| [[LF] START_PARTIN](/schnittstellen/202610/trigger/events/LF-START_PARTIN) | Event | — | zusatzdaten |
| [[LF] START_REKLAMATION_DEFINITIONEN](/schnittstellen/202610/trigger/events/LF-START_REKLAMATION_DEFINITIONEN) | Event | — | zusatzdaten |
| [[LF] START_REKLAMATION_VON_WERTEN](/schnittstellen/202610/trigger/events/LF-START_REKLAMATION_VON_WERTEN) | Event | — | zusatzdaten |
| [[LF] START_REKLAMATION_WERTE](/schnittstellen/202610/trigger/events/LF-START_REKLAMATION_WERTE) | Event | — | zusatzdaten |
| [[LF] START_SPERRAUFTRAG](/schnittstellen/202610/trigger/events/LF-START_SPERRAUFTRAG) | Event | — | zusatzdaten |
| [[LF] START_STORNO_AUFTRAG](/schnittstellen/202610/trigger/events/LF-START_STORNO_AUFTRAG) | Event | — | zusatzdaten |
| [[LF] START_STORNO_SE_AUFTRAG](/schnittstellen/202610/trigger/events/LF-START_STORNO_SE_AUFTRAG) | Event | — | zusatzdaten |
| [[LF] START_UEBERMITTLUNG_ENFG](/schnittstellen/202610/trigger/events/LF-START_UEBERMITTLUNG_ENFG) | Event | — | zusatzdaten |
| [[LF] START_UEBERM_DEFINITION](/schnittstellen/202610/trigger/events/LF-START_UEBERM_DEFINITION) | Event | — | zusatzdaten |
| [[LF] START_UEBERSICHT_LEISTUNGSKURVENDEF](/schnittstellen/202610/trigger/events/LF-START_UEBERSICHT_LEISTUNGSKURVENDEF) | Event | — | zusatzdaten |
| [[LF] START_UEBERSICHT_SCHALTZEITDEF](/schnittstellen/202610/trigger/events/LF-START_UEBERSICHT_SCHALTZEITDEF) | Event | — | zusatzdaten |
| [[LF] START_UEBERSICHT_ZAEHLZEITDEF](/schnittstellen/202610/trigger/events/LF-START_UEBERSICHT_ZAEHLZEITDEF) | Event | — | zusatzdaten |
| [[LF] START_VERSAND_ANF_STORNO](/schnittstellen/202610/trigger/events/LF-START_VERSAND_ANF_STORNO) | Event | — | zusatzdaten |
| [[LF] START_VERSAND_ANTWORT_NNA](/schnittstellen/202610/trigger/events/LF-START_VERSAND_ANTWORT_NNA) | Event | — | zusatzdaten |
| [[LF] START_VERSAND_BEST_BEEND_KONFIG](/schnittstellen/202610/trigger/events/LF-START_VERSAND_BEST_BEEND_KONFIG) | Event | — | zusatzdaten |
| [[LF] START_VERSAND_SDAE](/schnittstellen/202610/trigger/events/LF-START_VERSAND_SDAE) | Event | — | zusatzdaten |
| [[LF] START_VERSAND_STOERUNGSMELDUNG](/schnittstellen/202610/trigger/events/LF-START_VERSAND_STOERUNGSMELDUNG) | Event | — | zusatzdaten |
| [[LF] START_VERSAND_STORNO_MSCONS](/schnittstellen/202610/trigger/events/LF-START_VERSAND_STORNO_MSCONS) | Event | — | zusatzdaten |
| [[MSB] START_ANFORDERUNG_MESSWERTE](/schnittstellen/202610/trigger/events/MSB-START_ANFORDERUNG_MESSWERTE) | Event | — | zusatzdaten |
| [[MSB] START_ANGEBOT_GERAETEUEBERNAHME](/schnittstellen/202610/trigger/events/MSB-START_ANGEBOT_GERAETEUEBERNAHME) | Event | — | zusatzdaten |
| [[MSB] START_ANTWORT_GERAETEWECHSEL](/schnittstellen/202610/trigger/events/MSB-START_ANTWORT_GERAETEWECHSEL) | Event | — | zusatzdaten |
| [[MSB] START_BEEND_RE_MSB](/schnittstellen/202610/trigger/events/MSB-START_BEEND_RE_MSB) | Event | — | zusatzdaten |
| [[MSB] START_BEGINN_MSB](/schnittstellen/202610/trigger/events/MSB-START_BEGINN_MSB) | Event | — | zusatzdaten |
| [[MSB] START_BESTELLUNG_GERAETEUEBERNAHME](/schnittstellen/202610/trigger/events/MSB-START_BESTELLUNG_GERAETEUEBERNAHME) | Event | — | zusatzdaten |
| [[MSB] START_BESTELLUNG_SDAE GAS](/schnittstellen/202610/trigger/events/MSB-START_BESTELLUNG_SDAE-GAS) | Event | — | zusatzdaten |
| [[MSB] START_ENDE_MSB](/schnittstellen/202610/trigger/events/MSB-START_ENDE_MSB) | Event | — | zusatzdaten |
| [[MSB] START_ERHEBUNG_MESSWERTE](/schnittstellen/202610/trigger/events/MSB-START_ERHEBUNG_MESSWERTE) | Event | — | zusatzdaten |
| [[MSB] START_GERAETEUEBERNAHME](/schnittstellen/202610/trigger/events/MSB-START_GERAETEUEBERNAHME) | Event | — | zusatzdaten |
| [[MSB] START_GERAETEWECHSEL](/schnittstellen/202610/trigger/events/MSB-START_GERAETEWECHSEL) | Event | — | zusatzdaten |
| [[MSB] START_GESCHAEFTSDATENANFRAGE](/schnittstellen/202610/trigger/events/MSB-START_GESCHAEFTSDATENANFRAGE) | Event | — | zusatzdaten |
| [[MSB] START_KUENDIGUNG_MSB](/schnittstellen/202610/trigger/events/MSB-START_KUENDIGUNG_MSB) | Event | — | zusatzdaten |
| [[MSB] START_MESSWERTUEBERMITTLUNG](/schnittstellen/202610/trigger/events/MSB-START_MESSWERTUEBERMITTLUNG) | Event | — | zusatzdaten |
| [[MSB] START_PARTIN](/schnittstellen/202610/trigger/events/MSB-START_PARTIN) | Event | — | zusatzdaten |
| [[MSB] START_REKLAMATION_DEFINITION](/schnittstellen/202610/trigger/events/MSB-START_REKLAMATION_DEFINITION) | Event | — | zusatzdaten |
| [[MSB] START_VERSAND_ANF_STORNO](/schnittstellen/202610/trigger/events/MSB-START_VERSAND_ANF_STORNO) | Event | — | zusatzdaten |
| [[MSB] START_VERSAND_BEED_WERTE](/schnittstellen/202610/trigger/events/MSB-START_VERSAND_BEED_WERTE) | Event | — | zusatzdaten |
| [[MSB] START_VERSAND_PREISBLATT_IMS](/schnittstellen/202610/trigger/events/MSB-START_VERSAND_PREISBLATT_IMS) | Event | — | zusatzdaten |
| [[MSB] START_VERSAND_RECHNUNG](/schnittstellen/202610/trigger/events/MSB-START_VERSAND_RECHNUNG) | Event | — | zusatzdaten |
| [[MSB] START_VERSAND_SDAE](/schnittstellen/202610/trigger/events/MSB-START_VERSAND_SDAE) | Event | — | zusatzdaten |
| [[MSB] START_VERSAND_STORNO_MSCONS](/schnittstellen/202610/trigger/events/MSB-START_VERSAND_STORNO_MSCONS) | Event | — | zusatzdaten |
| [[NB] START_ABR_BK](/schnittstellen/202610/trigger/events/NB-START_ABR_BK) | Event | — | zusatzdaten |
| [[NB] START_ABR_NN](/schnittstellen/202610/trigger/events/NB-START_ABR_NN) | Event | — | zusatzdaten |
| [[NB] START_ANFORDERUNG_MESSWERTE](/schnittstellen/202610/trigger/events/NB-START_ANFORDERUNG_MESSWERTE) | Event | — | zusatzdaten |
| [[NB] START_ANFRAGE_MESSWERTE_NB](/schnittstellen/202610/trigger/events/NB-START_ANFRAGE_MESSWERTE_NB) | Event | — | zusatzdaten |
| [[NB] START_ANFRAGE_SPERRUNG](/schnittstellen/202610/trigger/events/NB-START_ANFRAGE_SPERRUNG) | Event | — | zusatzdaten |
| [[NB] START_ANFRAGE_STAMMDATENAENDERUNG GAS](/schnittstellen/202610/trigger/events/NB-START_ANFRAGE_STAMMDATENAENDERUNG-GAS) | Event | — | zusatzdaten |
| [[NB] START_AUFH_ZUK_ZUORDNUNG](/schnittstellen/202610/trigger/events/NB-START_AUFH_ZUK_ZUORDNUNG) | Event | — | zusatzdaten |
| [[NB] START_AUFTRAGSSTATUS](/schnittstellen/202610/trigger/events/NB-START_AUFTRAGSSTATUS) | Event | — | zusatzdaten |
| [[NB] START_BERECHNUNGSFORMEL](/schnittstellen/202610/trigger/events/NB-START_BERECHNUNGSFORMEL) | Event | — | zusatzdaten |
| [[NB] START_BESTELLUNG_SDAE](/schnittstellen/202610/trigger/events/NB-START_BESTELLUNG_SDAE) | Event | — | zusatzdaten |
| [[NB] START_BEST_AEND_TK](/schnittstellen/202610/trigger/events/NB-START_BEST_AEND_TK) | Event | — | zusatzdaten |
| [[NB] START_EINRICHTUNG_KONFIG](/schnittstellen/202610/trigger/events/NB-START_EINRICHTUNG_KONFIG) | Event | — | zusatzdaten |
| [[NB] START_EINRICHTUNG_KONFIGURATION_ZUORDNUNG_LF_VON_NB](/schnittstellen/202610/trigger/events/NB-START_EINRICHTUNG_KONFIGURATION_ZUORDNUNG_LF_VON_NB) | Event | — | zusatzdaten |
| [[NB] START_ENDE_MSB_STILLLEGUNG GAS](/schnittstellen/202610/trigger/events/NB-START_ENDE_MSB_STILLLEGUNG-GAS) | Event | — | zusatzdaten |
| [[NB] START_ENDE_ZUORDNUNG](/schnittstellen/202610/trigger/events/NB-START_ENDE_ZUORDNUNG) | Event | — | zusatzdaten |
| [[NB] START_EOG](/schnittstellen/202610/trigger/events/NB-START_EOG) | Event | — | zusatzdaten |
| [[NB] START_ERHEBUNG_MESSWERTE](/schnittstellen/202610/trigger/events/NB-START_ERHEBUNG_MESSWERTE) | Event | — | zusatzdaten |
| [[NB] START_LIEFERENDE](/schnittstellen/202610/trigger/events/NB-START_LIEFERENDE) | Event | — | zusatzdaten |
| [[NB] START_PREISBLATT](/schnittstellen/202610/trigger/events/NB-START_PREISBLATT) | Event | — | zusatzdaten |
| [[NB] START_REKLAMATION_WERTE](/schnittstellen/202610/trigger/events/NB-START_REKLAMATION_WERTE) | Event | — | zusatzdaten |
| [[NB] START_UEBERM_DEFINITION](/schnittstellen/202610/trigger/events/NB-START_UEBERM_DEFINITION) | Event | — | zusatzdaten |
| [[NB] START_UEBERSICHT_LEISTUNGSKURVENDEF](/schnittstellen/202610/trigger/events/NB-START_UEBERSICHT_LEISTUNGSKURVENDEF) | Event | — | zusatzdaten |
| [[NB] START_UEBERSICHT_SCHALTZEITDEF](/schnittstellen/202610/trigger/events/NB-START_UEBERSICHT_SCHALTZEITDEF) | Event | — | zusatzdaten |
| [[NB] START_UEBERSICHT_ZAEHLZEITDEF](/schnittstellen/202610/trigger/events/NB-START_UEBERSICHT_ZAEHLZEITDEF) | Event | — | zusatzdaten |
| [[NB] START_VERSAND_ANF_STORNO](/schnittstellen/202610/trigger/events/NB-START_VERSAND_ANF_STORNO) | Event | — | zusatzdaten |
| [[NB] START_VERSAND_BEARB_MELDUNG](/schnittstellen/202610/trigger/events/NB-START_VERSAND_BEARB_MELDUNG) | Event | — | zusatzdaten |
| [[NB] START_VERSAND_BEENDIGUNG_AGV](/schnittstellen/202610/trigger/events/NB-START_VERSAND_BEENDIGUNG_AGV) | Event | — | zusatzdaten |
| [[NB] START_VERSAND_BESTANDSLISTE GAS](/schnittstellen/202610/trigger/events/NB-START_VERSAND_BESTANDSLISTE-GAS) | Event | — | zusatzdaten |
| [[NB] START_VERSAND_COMDIS](/schnittstellen/202610/trigger/events/NB-START_VERSAND_COMDIS) | Event | — | zusatzdaten |
| [[NB] START_VERSAND_GEMESSENE_ARB_LEIST_WERTE](/schnittstellen/202610/trigger/events/NB-START_VERSAND_GEMESSENE_ARB_LEIST_WERTE) | Event | — | zusatzdaten |
| [[NB] START_VERSAND_LIEFERSCHEIN](/schnittstellen/202610/trigger/events/NB-START_VERSAND_LIEFERSCHEIN) | Event | — | zusatzdaten |
| [[NB] START_VERSAND_SDAE](/schnittstellen/202610/trigger/events/NB-START_VERSAND_SDAE) | Event | — | zusatzdaten |
| [[NB] START_VERSAND_STATUSMELDUNG](/schnittstellen/202610/trigger/events/NB-START_VERSAND_STATUSMELDUNG) | Event | — | zusatzdaten |
| [[NB] START_VERSAND_STOERUNGSMELDUNG_NB](/schnittstellen/202610/trigger/events/NB-START_VERSAND_STOERUNGSMELDUNG_NB) | Event | — | zusatzdaten |
| [[NB] START_VERSAND_STORNO_MSCONS](/schnittstellen/202610/trigger/events/NB-START_VERSAND_STORNO_MSCONS) | Event | — | zusatzdaten |
| [[NB] START_WIEDERHERST_LB](/schnittstellen/202610/trigger/events/NB-START_WIEDERHERST_LB) | Event | — | zusatzdaten |
| [[NB] START_WIEDERSPRUCH_ABLEHNUNG](/schnittstellen/202610/trigger/events/NB-START_WIEDERSPRUCH_ABLEHNUNG) | Event | — | zusatzdaten |
| [[NB] START_ZUORDNUNG_ERZ_MALO_TRANCHE](/schnittstellen/202610/trigger/events/NB-START_ZUORDNUNG_ERZ_MALO_TRANCHE) | Event | — | zusatzdaten |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Die mit *nicht aus der Zeitscheibe* gekennzeichneten Beschreibungen stehen nicht in `_sources/v202610/bo4e`, sondern in der jeweils genannten Quelle; sie sind redaktionell übernommen und nicht aus den Schemata dieser Seite abgeleitet. Im Zusammenhang beschreibt die Schlüssel die Seite [Schlüssel](/schnittstellen/schluessel).

Diese Quellen schreiben ein Feld gleichen Namens **selbst aus**, statt das BO4E-Feldatom zu referenzieren. Der `$ref`-Graph oben sieht diese Stellen nicht, und sie sind auch keine Verwendung des Feldatoms — deshalb stehen sie hier getrennt und werden nirgends zu den Verwendungen addiert.

</Hinweisbereich>
