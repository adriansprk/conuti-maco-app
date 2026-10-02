# Abweichung
<span hidden data-pagefind-meta={"title:Abweichung — BO4E-Komponente (FV 202610)"} />

BO4E-Komponente · 18 Felder · 30 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="abweichungsgrund"></a>`abweichungsgrund` | [Enum Abweichungsgrund](/bo4e/202610/enum/Abweichungsgrund)<br/><Werte>`PREIS_RECHENREGEL_FALSCH`, `FALSCHER_ABRECHNUNGSZEITRAUM`, `UNBEKANNTE_MARKTLOKATION_MESSLOKATION`, `SONSTIGER_ABWEICHUNGSGRUND`, `DOPPELTE_RECHNUNG`, `ABRECHNUNGSBEGINN_UNGLEICH_VERTRAGSBEGINN`, `ABRECHNUNGSENDE_UNGLEICH_VERTRAGSENDE`, `BETRAG_DER_ABSCHLAGSRECHNUNG_FALSCH`, `VORAUSBEZAHLTER_BETRAG_FALSCH`, `ARTIKEL_NICHT_VEREINBART`, `NETZNUTZUNGSMESSWERTE_ENERGIEMENGEN_FEHLEN`, `RECHNUNGSNUMMER_BEREITS_ERHALTEN`, `NETZNUTZUNGSMESSWERTE_ENERGIEMENGEN_FALSCH`, `ZEITLICHE_MENGENANGABE_FEHLERHAFT`, `FALSCHER_BILANZIERUNGSBEGINN`, `FALSCHES_NETZNUTZUNGSENDE`, `BILANZIERTE_MENGE_FEHLT`, `BILANZIERTE_MENGE_FALSCH`, `NETZNUTZUNGSABRECHNUNG_FEHLT`, `REVERSE_CHARGE_ANWENDUNG_FEHLT_ODER_FEHLERHAFT`, `ALLOKATIONSLISTE_FEHLT`, `MEHR_MINDERMENGE_FALSCH`, `UNGUELTIGES_RECHNUNGSDATUM`, `ZEITINTERVALL_DER_BILANZIERTEN_MENGE_INKONSISTENT`, `RECHNUNGSEMPFAENGER_WIDERSPRICHT_DER_STEUERRECHTLICHEN_EINSCHAETZUNG_DES_RECHNUNGSSTELLERS`, `ANGEGEBENE_QUOTES_AN_MARKTLOKATION_NICHT_VORHANDEN`, `RECHNUNGSABWICKLUNG_NICHT_VEREINBART`, `COMDIS_WIRD_ABGELEHNT`</Werte> | Abweichungsgrund |
| <a id="abweichungsgrundbemerkung"></a>`abweichungsgrundBemerkung` | string | Bemerkung zum Abweichungsgrund |
| <a id="zugehoerigerechnung"></a>`zugehoerigeRechnung` | string | Angabe der Rechnungsnummer, auf die sich diese Abweichung bezieht |
| <a id="zugehoerigebestellung"></a>`zugehoerigeBestellung` | string | Angabe der Bestellungsnummer, auf die sich diese Abweichung bezieht |
| <a id="abweichungsgrundcode"></a>`abweichungsgrundCode` | string | Code des Abweichungsgrundes |
| <a id="abweichungsgrundcodeliste"></a>`abweichungsgrundCodeliste` | string | Codeliste des Abweichungsgrund |
| <a id="fehlendepositionen1"></a>`fehlendePositionen1` | string | fehlende Positionen 1 |
| <a id="fehlendepositionen2"></a>`fehlendePositionen2` | string | fehlende Positionen 2 |
| <a id="fehlendepositionen3"></a>`fehlendePositionen3` | string | fehlende Positionen 3 |
| <a id="fehlendepositionen4"></a>`fehlendePositionen4` | string | fehlende Positionen 4 |
| <a id="fehlendepositionen5"></a>`fehlendePositionen5` | string | fehlende Positionen 5 |
| <a id="abweichungsgrundbemerkung1"></a>`abweichungsgrundBemerkung1` | string | Abweichungsgrund Bemerkung 1 |
| <a id="abweichungsgrundbemerkung2"></a>`abweichungsgrundBemerkung2` | string | Abweichungsgrund Bemerkung 2 |
| <a id="abweichungsgrundbemerkung3"></a>`abweichungsgrundBemerkung3` | string | Abweichungsgrund Bemerkung 3 |
| <a id="abweichungsgrundbemerkung4"></a>`abweichungsgrundBemerkung4` | string | Abweichungsgrund Bemerkung 4 |
| <a id="abweichungsgrundbemerkung5"></a>`abweichungsgrundBemerkung5` | string | Abweichungsgrund Bemerkung 5 |
| <a id="referenz"></a>`referenz` | string | referenz |
| <a id="abschlagsrechnungen"></a>`abschlagsrechnungen` | string[] | Abschlagsrechnungen |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[abweichungsgrund](/bo4e/202610/com/Abweichung#abweichungsgrund)</span> | Abweichungsgrund | [Enum Abweichungsgrund](/bo4e/202610/enum/Abweichungsgrund)<br/><Werte>`PREIS_RECHENREGEL_FALSCH`, `FALSCHER_ABRECHNUNGSZEITRAUM`, `UNBEKANNTE_MARKTLOKATION_MESSLOKATION`, `SONSTIGER_ABWEICHUNGSGRUND`, `DOPPELTE_RECHNUNG`, `ABRECHNUNGSBEGINN_UNGLEICH_VERTRAGSBEGINN`, `ABRECHNUNGSENDE_UNGLEICH_VERTRAGSENDE`, `BETRAG_DER_ABSCHLAGSRECHNUNG_FALSCH`, `VORAUSBEZAHLTER_BETRAG_FALSCH`, `ARTIKEL_NICHT_VEREINBART`, `NETZNUTZUNGSMESSWERTE_ENERGIEMENGEN_FEHLEN`, `RECHNUNGSNUMMER_BEREITS_ERHALTEN`, `NETZNUTZUNGSMESSWERTE_ENERGIEMENGEN_FALSCH`, `ZEITLICHE_MENGENANGABE_FEHLERHAFT`, `FALSCHER_BILANZIERUNGSBEGINN`, `FALSCHES_NETZNUTZUNGSENDE`, `BILANZIERTE_MENGE_FEHLT`, `BILANZIERTE_MENGE_FALSCH`, `NETZNUTZUNGSABRECHNUNG_FEHLT`, `REVERSE_CHARGE_ANWENDUNG_FEHLT_ODER_FEHLERHAFT`, `ALLOKATIONSLISTE_FEHLT`, `MEHR_MINDERMENGE_FALSCH`, `UNGUELTIGES_RECHNUNGSDATUM`, `ZEITINTERVALL_DER_BILANZIERTEN_MENGE_INKONSISTENT`, `RECHNUNGSEMPFAENGER_WIDERSPRICHT_DER_STEUERRECHTLICHEN_EINSCHAETZUNG_DES_RECHNUNGSSTELLERS`, `ANGEGEBENE_QUOTES_AN_MARKTLOKATION_NICHT_VORHANDEN`, `RECHNUNGSABWICKLUNG_NICHT_VEREINBART`, `COMDIS_WIRD_ABGELEHNT`</Werte> |
| <span className="hbs-f hbs-e0">[abweichungsgrundBemerkung](/bo4e/202610/com/Abweichung#abweichungsgrundbemerkung)</span> | Bemerkung zum Abweichungsgrund | string |
| <span className="hbs-f hbs-e0">[zugehoerigeRechnung](/bo4e/202610/com/Abweichung#zugehoerigerechnung)</span> | Angabe der Rechnungsnummer, auf die sich diese Abweichung bezieht | string |
| <span className="hbs-f hbs-e0">[zugehoerigeBestellung](/bo4e/202610/com/Abweichung#zugehoerigebestellung)</span> | Angabe der Bestellungsnummer, auf die sich diese Abweichung bezieht | string |
| <span className="hbs-f hbs-e0">[abweichungsgrundCode](/bo4e/202610/com/Abweichung#abweichungsgrundcode)</span> | Code des Abweichungsgrundes | string |
| <span className="hbs-f hbs-e0">[abweichungsgrundCodeliste](/bo4e/202610/com/Abweichung#abweichungsgrundcodeliste)</span> | Codeliste des Abweichungsgrund | string |
| <span className="hbs-f hbs-e0">[fehlendePositionen1](/bo4e/202610/com/Abweichung#fehlendepositionen1)</span> | fehlende Positionen 1 | string |
| <span className="hbs-f hbs-e0">[fehlendePositionen2](/bo4e/202610/com/Abweichung#fehlendepositionen2)</span> | fehlende Positionen 2 | string |
| <span className="hbs-f hbs-e0">[fehlendePositionen3](/bo4e/202610/com/Abweichung#fehlendepositionen3)</span> | fehlende Positionen 3 | string |
| <span className="hbs-f hbs-e0">[fehlendePositionen4](/bo4e/202610/com/Abweichung#fehlendepositionen4)</span> | fehlende Positionen 4 | string |
| <span className="hbs-f hbs-e0">[fehlendePositionen5](/bo4e/202610/com/Abweichung#fehlendepositionen5)</span> | fehlende Positionen 5 | string |
| <span className="hbs-f hbs-e0">[abweichungsgrundBemerkung1](/bo4e/202610/com/Abweichung#abweichungsgrundbemerkung1)</span> | Abweichungsgrund Bemerkung 1 | string |
| <span className="hbs-f hbs-e0">[abweichungsgrundBemerkung2](/bo4e/202610/com/Abweichung#abweichungsgrundbemerkung2)</span> | Abweichungsgrund Bemerkung 2 | string |
| <span className="hbs-f hbs-e0">[abweichungsgrundBemerkung3](/bo4e/202610/com/Abweichung#abweichungsgrundbemerkung3)</span> | Abweichungsgrund Bemerkung 3 | string |
| <span className="hbs-f hbs-e0">[abweichungsgrundBemerkung4](/bo4e/202610/com/Abweichung#abweichungsgrundbemerkung4)</span> | Abweichungsgrund Bemerkung 4 | string |
| <span className="hbs-f hbs-e0">[abweichungsgrundBemerkung5](/bo4e/202610/com/Abweichung#abweichungsgrundbemerkung5)</span> | Abweichungsgrund Bemerkung 5 | string |
| <span className="hbs-f hbs-e0">[referenz](/bo4e/202610/com/Abweichung#referenz)</span> | referenz | string |
| <span className="hbs-f hbs-e0">[abschlagsrechnungen](/bo4e/202610/com/Abweichung#abschlagsrechnungen) <span className="hbs-liste">[ ]</span></span> | Abschlagsrechnungen | string[] |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### zugehoerigeRechnung

2 Verwendung(en) in den Nachrichtentypen REMADV.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_33003](/schnittstellen/202610/pruefi/REMADV/PI_33003) | Prüfi | REMADV | stammdaten › AVIS › positionen › abweichung |
| [PI_33004](/schnittstellen/202610/pruefi/REMADV/PI_33004) | Prüfi | REMADV | stammdaten › AVIS › positionen › positionen › abweichung |

### abweichungsgrundCode

3 Verwendung(en) in den Nachrichtentypen REMADV.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_33002](/schnittstellen/202610/pruefi/REMADV/PI_33002) | Prüfi | REMADV | stammdaten › AVIS › positionen › abweichung |
| [PI_33003](/schnittstellen/202610/pruefi/REMADV/PI_33003) | Prüfi | REMADV | stammdaten › AVIS › positionen › abweichung |
| [PI_33004](/schnittstellen/202610/pruefi/REMADV/PI_33004) | Prüfi | REMADV | stammdaten › AVIS › positionen › positionen › abweichung |

### abweichungsgrundCodeliste

3 Verwendung(en) in den Nachrichtentypen REMADV.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_33002](/schnittstellen/202610/pruefi/REMADV/PI_33002) | Prüfi | REMADV | stammdaten › AVIS › positionen › abweichung |
| [PI_33003](/schnittstellen/202610/pruefi/REMADV/PI_33003) | Prüfi | REMADV | stammdaten › AVIS › positionen › abweichung |
| [PI_33004](/schnittstellen/202610/pruefi/REMADV/PI_33004) | Prüfi | REMADV | stammdaten › AVIS › positionen › positionen › abweichung |

### fehlendePositionen1

1 Verwendung(en) in den Nachrichtentypen REMADV.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_33003](/schnittstellen/202610/pruefi/REMADV/PI_33003) | Prüfi | REMADV | stammdaten › AVIS › positionen › abweichung |

### fehlendePositionen2

1 Verwendung(en) in den Nachrichtentypen REMADV.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_33003](/schnittstellen/202610/pruefi/REMADV/PI_33003) | Prüfi | REMADV | stammdaten › AVIS › positionen › abweichung |

### fehlendePositionen3

1 Verwendung(en) in den Nachrichtentypen REMADV.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_33003](/schnittstellen/202610/pruefi/REMADV/PI_33003) | Prüfi | REMADV | stammdaten › AVIS › positionen › abweichung |

### fehlendePositionen4

1 Verwendung(en) in den Nachrichtentypen REMADV.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_33003](/schnittstellen/202610/pruefi/REMADV/PI_33003) | Prüfi | REMADV | stammdaten › AVIS › positionen › abweichung |

### fehlendePositionen5

1 Verwendung(en) in den Nachrichtentypen REMADV.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_33003](/schnittstellen/202610/pruefi/REMADV/PI_33003) | Prüfi | REMADV | stammdaten › AVIS › positionen › abweichung |

### abweichungsgrundBemerkung1

3 Verwendung(en) in den Nachrichtentypen REMADV.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_33002](/schnittstellen/202610/pruefi/REMADV/PI_33002) | Prüfi | REMADV | stammdaten › AVIS › positionen › abweichung |
| [PI_33003](/schnittstellen/202610/pruefi/REMADV/PI_33003) | Prüfi | REMADV | stammdaten › AVIS › positionen › abweichung |
| [PI_33004](/schnittstellen/202610/pruefi/REMADV/PI_33004) | Prüfi | REMADV | stammdaten › AVIS › positionen › positionen › abweichung |

### abweichungsgrundBemerkung2

3 Verwendung(en) in den Nachrichtentypen REMADV.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_33002](/schnittstellen/202610/pruefi/REMADV/PI_33002) | Prüfi | REMADV | stammdaten › AVIS › positionen › abweichung |
| [PI_33003](/schnittstellen/202610/pruefi/REMADV/PI_33003) | Prüfi | REMADV | stammdaten › AVIS › positionen › abweichung |
| [PI_33004](/schnittstellen/202610/pruefi/REMADV/PI_33004) | Prüfi | REMADV | stammdaten › AVIS › positionen › positionen › abweichung |

### abweichungsgrundBemerkung3

3 Verwendung(en) in den Nachrichtentypen REMADV.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_33002](/schnittstellen/202610/pruefi/REMADV/PI_33002) | Prüfi | REMADV | stammdaten › AVIS › positionen › abweichung |
| [PI_33003](/schnittstellen/202610/pruefi/REMADV/PI_33003) | Prüfi | REMADV | stammdaten › AVIS › positionen › abweichung |
| [PI_33004](/schnittstellen/202610/pruefi/REMADV/PI_33004) | Prüfi | REMADV | stammdaten › AVIS › positionen › positionen › abweichung |

### abweichungsgrundBemerkung4

3 Verwendung(en) in den Nachrichtentypen REMADV.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_33002](/schnittstellen/202610/pruefi/REMADV/PI_33002) | Prüfi | REMADV | stammdaten › AVIS › positionen › abweichung |
| [PI_33003](/schnittstellen/202610/pruefi/REMADV/PI_33003) | Prüfi | REMADV | stammdaten › AVIS › positionen › abweichung |
| [PI_33004](/schnittstellen/202610/pruefi/REMADV/PI_33004) | Prüfi | REMADV | stammdaten › AVIS › positionen › positionen › abweichung |

### abweichungsgrundBemerkung5

3 Verwendung(en) in den Nachrichtentypen REMADV.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_33002](/schnittstellen/202610/pruefi/REMADV/PI_33002) | Prüfi | REMADV | stammdaten › AVIS › positionen › abweichung |
| [PI_33003](/schnittstellen/202610/pruefi/REMADV/PI_33003) | Prüfi | REMADV | stammdaten › AVIS › positionen › abweichung |
| [PI_33004](/schnittstellen/202610/pruefi/REMADV/PI_33004) | Prüfi | REMADV | stammdaten › AVIS › positionen › positionen › abweichung |

### referenz

1 Verwendung(en) in den Nachrichtentypen REMADV.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_33004](/schnittstellen/202610/pruefi/REMADV/PI_33004) | Prüfi | REMADV | stammdaten › AVIS › positionen › positionen › abweichung |

### abschlagsrechnungen

1 Verwendung(en) in den Nachrichtentypen REMADV.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_33003](/schnittstellen/202610/pruefi/REMADV/PI_33003) | Prüfi | REMADV | stammdaten › AVIS › positionen › abweichung |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
