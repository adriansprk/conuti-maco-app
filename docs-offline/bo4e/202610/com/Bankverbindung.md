# Bankverbindung
<span hidden data-pagefind-meta={"title:Bankverbindung — BO4E-Komponente (FV 202610)"} />

BO4E-Komponente · 5 Felder · 36 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="verwendungszweck"></a>`verwendungszweck` | [Enum BankverbindungVerwendungszweck](/bo4e/202610/enum/BankverbindungVerwendungszweck)<br/><Werte>`BV_ZAHLUNG_NNA`, `BV_ZAHLUNG_MMMA`, `BV_ZAHLUNG_MSB_ABRECHNNUNG`, `BV_ZAHLUNG_ENT_SPERREN_ABRECHNUNG`, `BV_SONSTIGE`</Werte> | BankverbindungVerwendungszweck |
| <a id="iban"></a>`iban` | string | IBAN |
| <a id="kontoinhaber"></a>`kontoinhaber` | string | Der Kontoinhaber |
| <a id="bic"></a>`bic` | string | BIC Code |
| <a id="kreditinstitut"></a>`kreditinstitut` | string | Name des Kreditinstitut |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[verwendungszweck](/bo4e/202610/com/Bankverbindung#verwendungszweck)</span> | BankverbindungVerwendungszweck | [Enum BankverbindungVerwendungszweck](/bo4e/202610/enum/BankverbindungVerwendungszweck)<br/><Werte>`BV_ZAHLUNG_NNA`, `BV_ZAHLUNG_MMMA`, `BV_ZAHLUNG_MSB_ABRECHNNUNG`, `BV_ZAHLUNG_ENT_SPERREN_ABRECHNUNG`, `BV_SONSTIGE`</Werte> |
| <span className="hbs-f hbs-e0">[iban](/bo4e/202610/com/Bankverbindung#iban)</span> | IBAN | string |
| <span className="hbs-f hbs-e0">[kontoinhaber](/bo4e/202610/com/Bankverbindung#kontoinhaber)</span> | Der Kontoinhaber | string |
| <span className="hbs-f hbs-e0">[bic](/bo4e/202610/com/Bankverbindung#bic)</span> | BIC Code | string |
| <span className="hbs-f hbs-e0">[kreditinstitut](/bo4e/202610/com/Bankverbindung#kreditinstitut)</span> | Name des Kreditinstitut | string |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### iban

9 Verwendung(en) in den Nachrichtentypen PARTIN.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_37000](/schnittstellen/202610/pruefi/PARTIN/PI_37000) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer › bankverbindung |
| [PI_37001](/schnittstellen/202610/pruefi/PARTIN/PI_37001) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer › bankverbindung |
| [PI_37002](/schnittstellen/202610/pruefi/PARTIN/PI_37002) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer › bankverbindung |
| [PI_37008](/schnittstellen/202610/pruefi/PARTIN/PI_37008) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer › bankverbindung |
| [PI_37009](/schnittstellen/202610/pruefi/PARTIN/PI_37009) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer › bankverbindung |
| [PI_37010](/schnittstellen/202610/pruefi/PARTIN/PI_37010) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer › bankverbindung |
| [PI_37012](/schnittstellen/202610/pruefi/PARTIN/PI_37012) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer › bankverbindung |
| [PI_37013](/schnittstellen/202610/pruefi/PARTIN/PI_37013) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer › bankverbindung |
| [PI_37014](/schnittstellen/202610/pruefi/PARTIN/PI_37014) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer › bankverbindung |

### kontoinhaber

9 Verwendung(en) in den Nachrichtentypen PARTIN.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_37000](/schnittstellen/202610/pruefi/PARTIN/PI_37000) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer › bankverbindung |
| [PI_37001](/schnittstellen/202610/pruefi/PARTIN/PI_37001) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer › bankverbindung |
| [PI_37002](/schnittstellen/202610/pruefi/PARTIN/PI_37002) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer › bankverbindung |
| [PI_37008](/schnittstellen/202610/pruefi/PARTIN/PI_37008) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer › bankverbindung |
| [PI_37009](/schnittstellen/202610/pruefi/PARTIN/PI_37009) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer › bankverbindung |
| [PI_37010](/schnittstellen/202610/pruefi/PARTIN/PI_37010) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer › bankverbindung |
| [PI_37012](/schnittstellen/202610/pruefi/PARTIN/PI_37012) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer › bankverbindung |
| [PI_37013](/schnittstellen/202610/pruefi/PARTIN/PI_37013) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer › bankverbindung |
| [PI_37014](/schnittstellen/202610/pruefi/PARTIN/PI_37014) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer › bankverbindung |

### bic

9 Verwendung(en) in den Nachrichtentypen PARTIN.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_37000](/schnittstellen/202610/pruefi/PARTIN/PI_37000) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer › bankverbindung |
| [PI_37001](/schnittstellen/202610/pruefi/PARTIN/PI_37001) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer › bankverbindung |
| [PI_37002](/schnittstellen/202610/pruefi/PARTIN/PI_37002) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer › bankverbindung |
| [PI_37008](/schnittstellen/202610/pruefi/PARTIN/PI_37008) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer › bankverbindung |
| [PI_37009](/schnittstellen/202610/pruefi/PARTIN/PI_37009) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer › bankverbindung |
| [PI_37010](/schnittstellen/202610/pruefi/PARTIN/PI_37010) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer › bankverbindung |
| [PI_37012](/schnittstellen/202610/pruefi/PARTIN/PI_37012) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer › bankverbindung |
| [PI_37013](/schnittstellen/202610/pruefi/PARTIN/PI_37013) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer › bankverbindung |
| [PI_37014](/schnittstellen/202610/pruefi/PARTIN/PI_37014) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer › bankverbindung |

### kreditinstitut

9 Verwendung(en) in den Nachrichtentypen PARTIN.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_37000](/schnittstellen/202610/pruefi/PARTIN/PI_37000) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer › bankverbindung |
| [PI_37001](/schnittstellen/202610/pruefi/PARTIN/PI_37001) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer › bankverbindung |
| [PI_37002](/schnittstellen/202610/pruefi/PARTIN/PI_37002) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer › bankverbindung |
| [PI_37008](/schnittstellen/202610/pruefi/PARTIN/PI_37008) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer › bankverbindung |
| [PI_37009](/schnittstellen/202610/pruefi/PARTIN/PI_37009) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer › bankverbindung |
| [PI_37010](/schnittstellen/202610/pruefi/PARTIN/PI_37010) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer › bankverbindung |
| [PI_37012](/schnittstellen/202610/pruefi/PARTIN/PI_37012) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer › bankverbindung |
| [PI_37013](/schnittstellen/202610/pruefi/PARTIN/PI_37013) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer › bankverbindung |
| [PI_37014](/schnittstellen/202610/pruefi/PARTIN/PI_37014) | Prüfi | PARTIN | stammdaten › KOMMUNIKATIONSDATEN › marktteilnehmer › bankverbindung |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
