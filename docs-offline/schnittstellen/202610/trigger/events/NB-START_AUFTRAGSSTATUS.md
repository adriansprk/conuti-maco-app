# [NB] START_AUFTRAGSSTATUS
<span hidden data-pagefind-meta={"title:Trigger-Ereignis START_AUFTRAGSSTATUS — Marktrolle NB (FV 202610)"} />

Marktrolle **NB** · Formatversion **202610** · BO4E-Schema **1.7.8**

## Stammdaten

Unter diesem Topic ist genau einer der folgenden 2 Prüfidentifikatoren zulässig — welcher, entscheidet der Event-Prozess.

| Prüfi | Scope | Anwendungsfall | Festlegung | Kommunikation |
|---|---|---|---|---|
| [PI_21039](/schnittstellen/202610/pruefi/IFTSTA/PI_21039) | IFTSTA | Auftragsstatus (Sperren) | AWH Sperrprozesse Gas | NB → LF |
| [PI_21040](/schnittstellen/202610/pruefi/IFTSTA/PI_21040) | IFTSTA | Info Entsperrauftrag | AWH Sperrprozesse Gas | NB → MSB |

Die Stammdaten der 2 Prüfidentifikatoren in **einer** Struktur — eine Spalte je Prüfidentifikator, wie im Anwendungshandbuch. Ein Wert in der Spalte heißt, dass das Feld zu diesem Prüfidentifikator gehört: **Muss**, wenn seine Spezifikation es verlangt, sonst **Kann**. Eine leere Zelle heißt »gehört nicht dazu«, nicht »unbekannt«. Vorausgewählt ist der erste; die übrigen schaltet die Leiste über der Tabelle zu.

<Handbuchsatz>

<div className="maco-tabellenrahmen">

| Struktur (BO4E) | Beschreibung | Format | <span className="hbs-p" title="Auftragsstatus (Sperren)">21039</span> | <span className="hbs-p" title="Info Entsperrauftrag">21040</span> | Bedingung |
|---|---|---|---|---|---|
| <span className="hbs-g hbs-e0">**stammdaten**</span> | — | object | Kann | Kann | — |
| <span className="hbs-g hbs-e1">**STATUSMITTEILUNG** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | Muss | — |
| <span className="hbs-g hbs-e2">**positionsdaten** <span className="hbs-liste">[ ]</span> <span className="hbs-pflicht">\*</span></span> | — | object[] | Muss | Muss | — |
| <span className="hbs-f hbs-e3">[allgemeineInformationenText](/bo4e/202610/com/StatusmitteilungPosition#allgemeineinformationentext)</span><span className="hbs-nr">00010</span> | Allgemeine Informationen | string | Kann | — | — |
| <span className="hbs-f hbs-e3">[antwortstatus](/bo4e/202610/com/StatusmitteilungPosition#antwortstatus)</span><span className="hbs-nr">00020</span> | antwortstatus | string | Kann | — | — |
| <span className="hbs-f hbs-e3">[antwortstatusCodeliste](/bo4e/202610/com/StatusmitteilungPosition#antwortstatuscodeliste)</span><span className="hbs-nr">00030</span> | antwortstatusCodeliste | string | Kann | — | — |
| <span className="hbs-f hbs-e3">[auftragsstatus](/bo4e/202610/com/StatusmitteilungPosition#auftragsstatus)</span><span className="hbs-nr">00040</span> | Auftragsstatus | [Enum Auftragsstatus](/bo4e/202610/enum/Auftragsstatus) | Kann | Muss | — |
| <span className="hbs-w hbs-e4">`GESCHEITERT`</span> | — | — | Kann | Muss | — |
| <span className="hbs-w hbs-e4">`ERFOLGREICH`</span> | — | — | Kann | Muss | — |
| <span className="hbs-w hbs-e4">`LIEFERUNG_GEPLANT`</span> | — | — | Kann | Muss | — |
| <span className="hbs-w hbs-e4">`GEPLANT`</span> | — | — | Kann | Muss | — |
| <span className="hbs-w hbs-e4">`ZUGESTIMMT`</span> | — | — | Kann | Muss | — |
| <span className="hbs-w hbs-e4">`WIDERSPROCHEN`</span> | — | — | Kann | Muss | — |
| <span className="hbs-w hbs-e4">`STOERUNGSFREI`</span> | — | — | Kann | Muss | — |
| <span className="hbs-w hbs-e4">`GESTOERT`</span> | — | — | Kann | Muss | — |
| <span className="hbs-w hbs-e4">`FESTGESTELLTE_STOERUNG`</span> | — | — | Kann | Muss | — |
| <span className="hbs-w hbs-e4">`VERMUTETE_STOERUNG`</span> | — | — | Kann | Muss | — |
| <span className="hbs-w hbs-e4">`ABGELEHNT`</span> | — | — | Kann | Muss | — |
| <span className="hbs-w hbs-e4">`BEENDET`</span> | — | — | Kann | Muss | — |
| <span className="hbs-w hbs-e4">`ANTWORT_DRITTER`</span> | — | — | Kann | Muss | — |
| <span className="hbs-w hbs-e4">`BESTAETIGT`</span> | — | — | Kann | Muss | — |
| <span className="hbs-w hbs-e4">`UMGESETZT`</span> | — | — | Kann | Muss | — |
| <span className="hbs-w hbs-e4">`ENFG_STROMSPEICHER_UND_VERLUSTENERGIE`</span> | — | — | Kann | Muss | — |
| <span className="hbs-w hbs-e4">`ENFG_ELEKTRISCH_ANGETRIEBENE_WAERMEPUMPEN`</span> | — | — | Kann | Muss | — |
| <span className="hbs-w hbs-e4">`ENFG_UMLAGEERHEBUNG_BEI_ANLAGEN_ZUR_VERSTROMUNG_VON_KUPPELGASEN`</span> | — | — | Kann | Muss | — |
| <span className="hbs-w hbs-e4">`ENFG_HERSTELLUNG_VON_GRUENEN_WASSERSTOFF`</span> | — | — | Kann | Muss | — |
| <span className="hbs-w hbs-e4">`ENFG_STROMKOSTENINTENSIVE_UNTERNEHMEN`</span> | — | — | Kann | Muss | — |
| <span className="hbs-w hbs-e4">`ENFG_HERSTELLUNG_VON_WASSERSTOFF_IN_STROMKOSTENINTENSIVEN_UNTERNEHMEN`</span> | — | — | Kann | Muss | — |
| <span className="hbs-w hbs-e4">`ENFG_SCHIENENBAHNEN`</span> | — | — | Kann | Muss | — |
| <span className="hbs-w hbs-e4">`ENFG_ELEKTRISCHE_BETRIEBENE_BUSSEN_IM_LINIENVERKEHR`</span> | — | — | Kann | Muss | — |
| <span className="hbs-w hbs-e4">`ENFG_LANDSTROMANLAGEN`</span> | — | — | Kann | Muss | — |
| <span className="hbs-w hbs-e4">`AENDERUNG_DER_DATEN`</span> | — | — | Kann | Muss | — |
| <span className="hbs-w hbs-e4">`KEINE_AENDERUNG_DER_DATEN`</span> | — | — | Kann | Muss | — |
| <span className="hbs-w hbs-e4">`ZEITREIHE_AKZEPTIERT`</span> | — | — | Kann | Muss | — |
| <span className="hbs-w hbs-e4">`ZEITREIHE_NICHT_AKZEPTIERT`</span> | — | — | Kann | Muss | — |
| <span className="hbs-f hbs-e3">[fertigstellungsdatum](/bo4e/202610/com/StatusmitteilungPosition#fertigstellungsdatum)</span><span className="hbs-nr">00050</span> | fertigstellungsdatum | string (date-time) | Kann | Muss | — |
| <span className="hbs-f hbs-e3">[lokationsId](/bo4e/202610/com/StatusmitteilungPosition#lokationsid) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00060</span> | lokationsId | string | Muss | Muss | — |
| <span className="hbs-f hbs-e3">[positionsnummer](/bo4e/202610/com/StatusmitteilungPosition#positionsnummer) <span className="hbs-pflicht">\*</span></span><span className="hbs-nr">00070</span> | positionsnummer | integer | Muss | Muss | — |
| <span className="hbs-f hbs-e3">[sendungsposition](/bo4e/202610/com/StatusmitteilungPosition#sendungsposition)</span><span className="hbs-nr">00080</span> | sendungsposition | integer | Kann | — | — |
| <span className="hbs-f hbs-e3">[statusObjekt](/bo4e/202610/com/StatusmitteilungPosition#statusobjekt)</span><span className="hbs-nr">00090</span> | Statusobjekt | [Enum Statusobjekt](/bo4e/202610/enum/Statusobjekt) | Kann | — | — |
| <span className="hbs-w hbs-e4">`MSBWECHSEL`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`UMBAUMELO`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`ERSTEINBAUIMS`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`ERSTEINBAUMME`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`GERAET`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`ANGEBOTANFRAGE`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`STATUSBESTELLUNG`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`LIEFERSCHEIN`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`SPERREN`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`ENTSPERREN`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`PRIVILEGIERUNG_NACH_ENFG`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`VERAENDERUNGSSTATUS_DER_DATEN`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`TURNUSAUSLESUNG`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`PRUEFSTATUS_ANTWORT_SUMMENZEITREIHEN`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`ABWEISUNG_SUMMENZEITREIHE`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`PRUEFSTATUS_SUMMENZEITREIHE`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`DATENSTATUS_SUMMENZEITREIHE`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`ABWEISUNG_STATUSMELDUNG_AENDERUNG`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`AUSFALLARBEIT`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`FAHRPLANANTEIL`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`GEGENVORSCHLAG_AUSFALLARBEIT`</span> | — | — | Kann | — | — |
| <span className="hbs-w hbs-e4">`GEGENVORSCHLAG_FAHRPLANANTEIL`</span> | — | — | Kann | — | — |

</div>

</Handbuchsatz>

## Kette dieses Auslösers

Das Ereignis löst die Nachricht aus.

| Nachricht | Antworten | Schreibaufruf nach der Antwort |
|---|---|---|
| [21039](/schnittstellen/202610/pruefi/IFTSTA/PI_21039) | — | — |
| [21040](/schnittstellen/202610/pruefi/IFTSTA/PI_21040) | — | — |

Dieses Ereignis löst Schritte in diesen Rollensichten aus:

| Prozess | Beteiligter | Regelwerk | Sparte |
|---|---|---|---|
| [Unterbrechung der Anschlussnutzung (Sperren) auf Anweisung des LF](/prozessdoku/202610/NB/awh-sperrprozesse-gas-unterbrechung-der-anschlussnutzung-sperren-auf-anweisung-des-lf) | NB | AWH Sperrprozesse Gas | Gas |
| [Wiederherstellung der Anschlussnutzung (Entsperren) auf Anweisung des LF](/prozessdoku/202610/NB/awh-sperrprozesse-gas-wiederherstellung-der-anschlussnutzung-entsperren-auf-anweisung-des-lf) | NB | AWH Sperrprozesse Gas | Gas |
| [Wiederherstellung der Anschlussnutzung bei Lieferbeginn](/prozessdoku/202610/NB/awh-sperrprozesse-gas-wiederherstellung-der-anschlussnutzung-bei-lieferbeginn) | NB | AWH Sperrprozesse Gas | Gas |
| [Unterbrechung der Anschlussnutzung (Sperren) auf Anweisung des LF](/prozessdoku/202610/NB/GPKE-Teil2-unterbrechung-der-anschlussnutzung-sperren-auf-anweisung-des-lf) | NB | GPKE Teil 2 | Strom |
| [Wiederherstellung der Anschlussnutzung (Entsperren) auf Anweisung des LF](/prozessdoku/202610/NB/GPKE-Teil2-wiederherstellung-der-anschlussnutzung-entsperren-auf-anweisung-des-lf) | NB | GPKE Teil 2 | Strom |
| [Wiederherstellung der Anschlussnutzung bei Lieferbeginn](/prozessdoku/202610/NB/GPKE-Teil2-wiederherstellung-der-anschlussnutzung-bei-lieferbeginn) | NB | GPKE Teil 2 | Strom |

## Transaktionsdaten

Der Umschlag der Nachricht. Pflichtfelder müssen beim Trigger-Aufruf gesetzt sein.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| [sparte](/bo4e/202610/cdoc/Transaktionsdaten#sparte) | [Enum Sparte](/bo4e/202610/enum/Sparte) | **ja** | Enthält Informationen über die Sparte Werte: `STROM`, `GAS`, `FERNWAERME`, `NAHWAERME`, `WASSER`, `ABWASSER` |
| `pruefidentifikator` | — | nein | Wird dynamisch im Event-Prozess ermittelt (Entscheidungsgrundlage: auftragsstatus). Ein vom Sender mitgegebener Wert wird ignoriert. Im Topic mögliche Prüfis — 21039, 21040. Mögliche Werte: `21039`, `21040` |
| [absender › rollencodenummer](/bo4e/202610/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |
| [empfaenger › rollencodenummer](/bo4e/202610/bo/Marktteilnehmer#rollencodenummer) | string | nein | Gibt die Codenummer der Marktrolle an. |

## Zusatzdaten

`eventname` ist auf **START_AUFTRAGSSTATUS** festgelegt. Dieser Wert bleibt auch in der englischen Fassung deutsch, weil Camunda darüber korreliert.

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `prozessId` | string | **ja** | — |
| `eventname` | const `START_AUFTRAGSSTATUS` | **ja** | — |

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
