# FehlerDetail
<span hidden data-pagefind-meta={"title:FehlerDetail — BO4E-Komponente (FV 202604)"} />

BO4E-Komponente · 3 Felder · 0 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="code"></a>`code` | [Enum FehlerCode](/bo4e/202604/enum/FehlerCode)<br/><Werte>`ID_UNBEKANNT`, `ABSENDER_NICHT_ZUGEORDNET`, `EMPFAENGER_NICHT_ZUGEORDNET`, `GERAET_UNBEKANNT`, `OBIS_UNBEKANNT`, `REFERENZIERUNG_FEHLERHAFT`, `TUPEL_UNBEKANNT`, `ABSENDER_TUPEL_NICHT_ZUGEORDNET`, `EMPFAENGER_TUPEL_NICHT_ZUGEORDNET`, `VORKOMMA_ZU_VIELE_STELLEN`, `ZEITREIHE_UNVOLLSTAENDIG`, `REFERENZIERTES_TUPEL_UNBEKANNT`, `MARKTLOKATION_UNBEKANNT`, `MESSLOKATION_UNBEKANNT`, `MELDEPUNKT_NICHT_MEHR_IM_NETZ`, `ERFORDERLICHE_ANGABE_FEHLT`, `GESCHAEFTSVORFALL_ZURUECKGEWIESEN`, `ZEITINTERVALL_NEGATIV`, `FORMAT_NICHT_EINGEHALTEN`, `GESCHAEFTSVORFALL_ABSENDER`, `KONFIGURATIONSID_UNBEKANNT`, `SEGMENTWIEDERHOLUNG_UEBERSCHRITTEN`, `ANZAHLCODES_UEBERSCHRITTEN`, `ZEITANGABE_UNPLAUSIBEL`, `CODE_NICHT_ERLAUBT`, `OBJEKT_NICHT_GEFUNDEN`, `OBJEKT_NICHT_EINDEUTIG`, `GESCHAEFTSVORFALL_OBJEKT_EIGENSCHAFT_NICHT_ERLAUBT`, `EIGENSCHAFT_OBJEKT_WEICHT_VON_GESCHAEFTSVORFALL_CODIERTEN_EIGENSCHAFT_AB`</Werte> | FehlerCode |
| <a id="ursache"></a>`ursache` | [FehlerUrsache](/bo4e/202604/com/FehlerUrsache) | — |
| <a id="beschreibung"></a>`beschreibung` | [Beschreibung](/bo4e/202604/com/Beschreibung) | — |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[code](/bo4e/202604/com/FehlerDetail#code)</span> | FehlerCode | [Enum FehlerCode](/bo4e/202604/enum/FehlerCode)<br/><Werte>`ID_UNBEKANNT`, `ABSENDER_NICHT_ZUGEORDNET`, `EMPFAENGER_NICHT_ZUGEORDNET`, `GERAET_UNBEKANNT`, `OBIS_UNBEKANNT`, `REFERENZIERUNG_FEHLERHAFT`, `TUPEL_UNBEKANNT`, `ABSENDER_TUPEL_NICHT_ZUGEORDNET`, `EMPFAENGER_TUPEL_NICHT_ZUGEORDNET`, `VORKOMMA_ZU_VIELE_STELLEN`, `ZEITREIHE_UNVOLLSTAENDIG`, `REFERENZIERTES_TUPEL_UNBEKANNT`, `MARKTLOKATION_UNBEKANNT`, `MESSLOKATION_UNBEKANNT`, `MELDEPUNKT_NICHT_MEHR_IM_NETZ`, `ERFORDERLICHE_ANGABE_FEHLT`, `GESCHAEFTSVORFALL_ZURUECKGEWIESEN`, `ZEITINTERVALL_NEGATIV`, `FORMAT_NICHT_EINGEHALTEN`, `GESCHAEFTSVORFALL_ABSENDER`, `KONFIGURATIONSID_UNBEKANNT`, `SEGMENTWIEDERHOLUNG_UEBERSCHRITTEN`, `ANZAHLCODES_UEBERSCHRITTEN`, `ZEITANGABE_UNPLAUSIBEL`, `CODE_NICHT_ERLAUBT`, `OBJEKT_NICHT_GEFUNDEN`, `OBJEKT_NICHT_EINDEUTIG`, `GESCHAEFTSVORFALL_OBJEKT_EIGENSCHAFT_NICHT_ERLAUBT`, `EIGENSCHAFT_OBJEKT_WEICHT_VON_GESCHAEFTSVORFALL_CODIERTEN_EIGENSCHAFT_AB`</Werte> |
| <span className="hbs-g hbs-e0">[ursache](/bo4e/202604/com/FehlerDetail#ursache)</span> | — | [FehlerUrsache](/bo4e/202604/com/FehlerUrsache) |
| <span className="hbs-f hbs-e1">[dokument](/bo4e/202604/com/FehlerUrsache#dokument)</span> | dokument | string |
| <span className="hbs-f hbs-e1">[nachricht](/bo4e/202604/com/FehlerUrsache#nachricht)</span> | nachricht | string |
| <span className="hbs-f hbs-e1">[transaktion](/bo4e/202604/com/FehlerUrsache#transaktion)</span> | transaktion | string |
| <span className="hbs-g hbs-e1">[gruppe](/bo4e/202604/com/FehlerUrsache#gruppe)</span> | — | [Gruppe](/bo4e/202604/com/Gruppe) |
| <span className="hbs-f hbs-e2">[gruppe1](/bo4e/202604/com/Gruppe#gruppe1)</span> | Gruppe Zeile 1 | string |
| <span className="hbs-f hbs-e2">[gruppe2](/bo4e/202604/com/Gruppe#gruppe2)</span> | Gruppe Zeile 2 | string |
| <span className="hbs-f hbs-e1">[segment](/bo4e/202604/com/FehlerUrsache#segment)</span> | segment | string |
| <span className="hbs-g hbs-e1">[beschreibung](/bo4e/202604/com/FehlerUrsache#beschreibung)</span> | — | [Beschreibung](/bo4e/202604/com/Beschreibung) |
| <span className="hbs-f hbs-e2">[beschreibung1](/bo4e/202604/com/Beschreibung#beschreibung1)</span> | Beschreibung Zeile 1 | string |
| <span className="hbs-f hbs-e2">[beschreibung2](/bo4e/202604/com/Beschreibung#beschreibung2)</span> | Beschreibung Zeile 2 | string |
| <span className="hbs-g hbs-e0">[beschreibung](/bo4e/202604/com/FehlerDetail#beschreibung)</span> | — | [Beschreibung](/bo4e/202604/com/Beschreibung) |
| <span className="hbs-f hbs-e1">[beschreibung1](/bo4e/202604/com/Beschreibung#beschreibung1)</span> | Beschreibung Zeile 1 | string |
| <span className="hbs-f hbs-e1">[beschreibung2](/bo4e/202604/com/Beschreibung#beschreibung2)</span> | Beschreibung Zeile 2 | string |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

:::note{title="Keine Verwendung gefunden"}

Kein Feld dieses Objekts wird in den Prüfi- oder Event-Spezifikationen dieser Formatversion referenziert. Das Objekt gehört zum BO4E-Schema, ist in der Marktkommunikation dieser Formatversion aber nicht im Einsatz.

:::

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

</Hinweisbereich>
