# Messstellenbetriebsabrechnungsdaten
<span hidden data-pagefind-meta={"title:Messstellenbetriebsabrechnungsdaten — BO4E-Komponente (FV 202610)"} />

BO4E-Komponente · 6 Felder · 8 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="messstellenbetriebsabrechnung"></a>`messstellenbetriebsabrechnung` | boolean | messstellenbetriebsabrechnung |
| <a id="artikelid"></a>`artikelId` | string | BDEWArtikelId |
| <a id="artikelidtyp"></a>`artikelIdTyp` | [Enum ArtikelIdTyp](/bo4e/202610/enum/ArtikelIdTyp)<br/><Werte>`ARTIKELID`, `GRUPPENARTIKELID`</Werte> | Liste von Artikel-IDs, z.B. für standardisierte vom BDEW herausgegebene Artikel, die im Strommarkt die BDEW-Artikelnummer ablösen |
| <a id="anzahl"></a>`anzahl` | integer | anzahl |
| <a id="zuschlag"></a>`zuschlag` | number (float) | Zuschlag |
| <a id="abschlag"></a>`abschlag` | number (float) | Abschlag |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[messstellenbetriebsabrechnung](/bo4e/202610/com/Messstellenbetriebsabrechnungsdaten#messstellenbetriebsabrechnung)</span> | messstellenbetriebsabrechnung | boolean |
| <span className="hbs-f hbs-e0">[artikelId](/bo4e/202610/com/Messstellenbetriebsabrechnungsdaten#artikelid)</span> | BDEWArtikelId | string |
| <span className="hbs-f hbs-e0">[artikelIdTyp](/bo4e/202610/com/Messstellenbetriebsabrechnungsdaten#artikelidtyp)</span> | Liste von Artikel-IDs, z.B. für standardisierte vom BDEW herausgegebene Artikel, die im Strommarkt die BDEW-Artikelnummer ablösen | [Enum ArtikelIdTyp](/bo4e/202610/enum/ArtikelIdTyp)<br/><Werte>`ARTIKELID`, `GRUPPENARTIKELID`</Werte> |
| <span className="hbs-f hbs-e0">[anzahl](/bo4e/202610/com/Messstellenbetriebsabrechnungsdaten#anzahl)</span> | anzahl | integer |
| <span className="hbs-f hbs-e0">[zuschlag](/bo4e/202610/com/Messstellenbetriebsabrechnungsdaten#zuschlag)</span> | Zuschlag | number (float) |
| <span className="hbs-f hbs-e0">[abschlag](/bo4e/202610/com/Messstellenbetriebsabrechnungsdaten#abschlag)</span> | Abschlag | number (float) |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### messstellenbetriebsabrechnung

2 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55557](/schnittstellen/202610/pruefi/UTILMD/PI_55557) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › messstellenbetriebsabrechnungsdaten |
| [PI_55559](/schnittstellen/202610/pruefi/UTILMD/PI_55559) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › messstellenbetriebsabrechnungsdaten |

### artikelId

2 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55557](/schnittstellen/202610/pruefi/UTILMD/PI_55557) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › messstellenbetriebsabrechnungsdaten |
| [PI_55559](/schnittstellen/202610/pruefi/UTILMD/PI_55559) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › messstellenbetriebsabrechnungsdaten |

### anzahl

2 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55557](/schnittstellen/202610/pruefi/UTILMD/PI_55557) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › messstellenbetriebsabrechnungsdaten |
| [PI_55559](/schnittstellen/202610/pruefi/UTILMD/PI_55559) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › messstellenbetriebsabrechnungsdaten |

### abschlag

2 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55557](/schnittstellen/202610/pruefi/UTILMD/PI_55557) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › messstellenbetriebsabrechnungsdaten |
| [PI_55559](/schnittstellen/202610/pruefi/UTILMD/PI_55559) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › messstellenbetriebsabrechnungsdaten |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
