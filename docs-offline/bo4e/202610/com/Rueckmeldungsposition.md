# Rueckmeldungsposition
<span hidden data-pagefind-meta={"title:Rueckmeldungsposition — BO4E-Komponente (FV 202610)"} />

BO4E-Komponente · 2 Felder · 1 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="positionsnummer"></a>`positionsnummer` | integer | positionsnummer |
| <a id="abweichung"></a>`abweichung` | [Abweichung[]](/bo4e/202610/com/Abweichung) | abweichung |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[positionsnummer](/bo4e/202610/com/Rueckmeldungsposition#positionsnummer)</span> | positionsnummer | integer |
| <span className="hbs-g hbs-e0">[abweichung](/bo4e/202610/com/Rueckmeldungsposition#abweichung) <span className="hbs-liste">[ ]</span></span> | abweichung | [Abweichung[]](/bo4e/202610/com/Abweichung) |
| <span className="hbs-f hbs-e1">[abweichungsgrund](/bo4e/202610/com/Abweichung#abweichungsgrund)</span> | Abweichungsgrund | [Enum Abweichungsgrund](/bo4e/202610/enum/Abweichungsgrund)<br/><Werte>`PREIS_RECHENREGEL_FALSCH`, `FALSCHER_ABRECHNUNGSZEITRAUM`, `UNBEKANNTE_MARKTLOKATION_MESSLOKATION`, `SONSTIGER_ABWEICHUNGSGRUND`, `DOPPELTE_RECHNUNG`, `ABRECHNUNGSBEGINN_UNGLEICH_VERTRAGSBEGINN`, `ABRECHNUNGSENDE_UNGLEICH_VERTRAGSENDE`, `BETRAG_DER_ABSCHLAGSRECHNUNG_FALSCH`, `VORAUSBEZAHLTER_BETRAG_FALSCH`, `ARTIKEL_NICHT_VEREINBART`, `NETZNUTZUNGSMESSWERTE_ENERGIEMENGEN_FEHLEN`, `RECHNUNGSNUMMER_BEREITS_ERHALTEN`, `NETZNUTZUNGSMESSWERTE_ENERGIEMENGEN_FALSCH`, `ZEITLICHE_MENGENANGABE_FEHLERHAFT`, `FALSCHER_BILANZIERUNGSBEGINN`, `FALSCHES_NETZNUTZUNGSENDE`, `BILANZIERTE_MENGE_FEHLT`, `BILANZIERTE_MENGE_FALSCH`, `NETZNUTZUNGSABRECHNUNG_FEHLT`, `REVERSE_CHARGE_ANWENDUNG_FEHLT_ODER_FEHLERHAFT`, `ALLOKATIONSLISTE_FEHLT`, `MEHR_MINDERMENGE_FALSCH`, `UNGUELTIGES_RECHNUNGSDATUM`, `ZEITINTERVALL_DER_BILANZIERTEN_MENGE_INKONSISTENT`, `RECHNUNGSEMPFAENGER_WIDERSPRICHT_DER_STEUERRECHTLICHEN_EINSCHAETZUNG_DES_RECHNUNGSSTELLERS`, `ANGEGEBENE_QUOTES_AN_MARKTLOKATION_NICHT_VORHANDEN`, `RECHNUNGSABWICKLUNG_NICHT_VEREINBART`, `COMDIS_WIRD_ABGELEHNT`</Werte> |
| <span className="hbs-f hbs-e1">[abweichungsgrundBemerkung](/bo4e/202610/com/Abweichung#abweichungsgrundbemerkung)</span> | Bemerkung zum Abweichungsgrund | string |
| <span className="hbs-f hbs-e1">[zugehoerigeRechnung](/bo4e/202610/com/Abweichung#zugehoerigerechnung)</span> | Angabe der Rechnungsnummer, auf die sich diese Abweichung bezieht | string |
| <span className="hbs-f hbs-e1">[zugehoerigeBestellung](/bo4e/202610/com/Abweichung#zugehoerigebestellung)</span> | Angabe der Bestellungsnummer, auf die sich diese Abweichung bezieht | string |
| <span className="hbs-f hbs-e1">[abweichungsgrundCode](/bo4e/202610/com/Abweichung#abweichungsgrundcode)</span> | Code des Abweichungsgrundes | string |
| <span className="hbs-f hbs-e1">[abweichungsgrundCodeliste](/bo4e/202610/com/Abweichung#abweichungsgrundcodeliste)</span> | Codeliste des Abweichungsgrund | string |
| <span className="hbs-f hbs-e1">[fehlendePositionen1](/bo4e/202610/com/Abweichung#fehlendepositionen1)</span> | fehlende Positionen 1 | string |
| <span className="hbs-f hbs-e1">[fehlendePositionen2](/bo4e/202610/com/Abweichung#fehlendepositionen2)</span> | fehlende Positionen 2 | string |
| <span className="hbs-f hbs-e1">[fehlendePositionen3](/bo4e/202610/com/Abweichung#fehlendepositionen3)</span> | fehlende Positionen 3 | string |
| <span className="hbs-f hbs-e1">[fehlendePositionen4](/bo4e/202610/com/Abweichung#fehlendepositionen4)</span> | fehlende Positionen 4 | string |
| <span className="hbs-f hbs-e1">[fehlendePositionen5](/bo4e/202610/com/Abweichung#fehlendepositionen5)</span> | fehlende Positionen 5 | string |
| <span className="hbs-f hbs-e1">[abweichungsgrundBemerkung1](/bo4e/202610/com/Abweichung#abweichungsgrundbemerkung1)</span> | Abweichungsgrund Bemerkung 1 | string |
| <span className="hbs-f hbs-e1">[abweichungsgrundBemerkung2](/bo4e/202610/com/Abweichung#abweichungsgrundbemerkung2)</span> | Abweichungsgrund Bemerkung 2 | string |
| <span className="hbs-f hbs-e1">[abweichungsgrundBemerkung3](/bo4e/202610/com/Abweichung#abweichungsgrundbemerkung3)</span> | Abweichungsgrund Bemerkung 3 | string |
| <span className="hbs-f hbs-e1">[abweichungsgrundBemerkung4](/bo4e/202610/com/Abweichung#abweichungsgrundbemerkung4)</span> | Abweichungsgrund Bemerkung 4 | string |
| <span className="hbs-f hbs-e1">[abweichungsgrundBemerkung5](/bo4e/202610/com/Abweichung#abweichungsgrundbemerkung5)</span> | Abweichungsgrund Bemerkung 5 | string |
| <span className="hbs-f hbs-e1">[referenz](/bo4e/202610/com/Abweichung#referenz)</span> | referenz | string |
| <span className="hbs-f hbs-e1">[abschlagsrechnungen](/bo4e/202610/com/Abweichung#abschlagsrechnungen) <span className="hbs-liste">[ ]</span></span> | Abschlagsrechnungen | string[] |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### positionsnummer

1 Verwendung(en) in den Nachrichtentypen REMADV.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_33004](/schnittstellen/202610/pruefi/REMADV/PI_33004) | Prüfi | REMADV | stammdaten › AVIS › positionen › positionen |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
