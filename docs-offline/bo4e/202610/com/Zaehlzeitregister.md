# Zaehlzeitregister
<span hidden data-pagefind-meta={"title:Zaehlzeitregister — BO4E-Komponente (FV 202610)"} />

BO4E-Komponente · 3 Felder · 62 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="register"></a>`register` | string | Zählzeitregister |
| <a id="zaehlzeitdefinition"></a>`zaehlzeitDefinition` | string | Zählzeitdefinition |
| <a id="schwachlastfaehig"></a>`schwachlastfaehig` | [Enum Schwachlastfaehig](/bo4e/202610/enum/Schwachlastfaehig)<br/><Werte>`SCHWACHLASTFAEHIG`, `NICHT_SCHWACHLASTFAEHIG`</Werte> | Schwachlastfähigkeit des Registers |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[register](/bo4e/202610/com/Zaehlzeitregister#register)</span> | Zählzeitregister | string |
| <span className="hbs-f hbs-e0">[zaehlzeitDefinition](/bo4e/202610/com/Zaehlzeitregister#zaehlzeitdefinition)</span> | Zählzeitdefinition | string |
| <span className="hbs-f hbs-e0">[schwachlastfaehig](/bo4e/202610/com/Zaehlzeitregister#schwachlastfaehig)</span> | Schwachlastfähigkeit des Registers | [Enum Schwachlastfaehig](/bo4e/202610/enum/Schwachlastfaehig)<br/><Werte>`SCHWACHLASTFAEHIG`, `NICHT_SCHWACHLASTFAEHIG`</Werte> |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### register

25 Verwendung(en) in den Nachrichtentypen UTILMD, UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_25004](/schnittstellen/202610/pruefi/UTILTS/PI_25004) | Prüfi | UTILTS | stammdaten › ZAEHLZEITDEFINITION › zaehlzeitregister |
| [PI_55035](/schnittstellen/202610/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › netznutzungsabrechnungsdaten › zaehlzeiten |
| [PI_55035](/schnittstellen/202610/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke › zaehlzeiten |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke › zaehlzeiten |
| [PI_55060](/schnittstellen/202610/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke › zaehlzeiten |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke › zaehlzeiten |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke › zaehlzeiten |
| [PI_55218](/schnittstellen/202610/pruefi/UTILMD/PI_55218) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › netznutzungsabrechnungsdaten › zaehlzeiten |
| [PI_55220](/schnittstellen/202610/pruefi/UTILMD/PI_55220) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › netznutzungsabrechnungsdaten › zaehlzeiten |
| [PI_55553](/schnittstellen/202610/pruefi/UTILMD/PI_55553) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke › zaehlzeiten |
| [PI_55553](/schnittstellen/202610/pruefi/UTILMD/PI_55553) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke › zaehlzeiten |
| [PI_55555](/schnittstellen/202610/pruefi/UTILMD/PI_55555) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke › zaehlzeiten |
| [PI_55555](/schnittstellen/202610/pruefi/UTILMD/PI_55555) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke › zaehlzeiten |
| [PI_55640](/schnittstellen/202610/pruefi/UTILMD/PI_55640) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke › zaehlzeiten |
| [PI_55643](/schnittstellen/202610/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke › zaehlzeiten |
| [PI_55645](/schnittstellen/202610/pruefi/UTILMD/PI_55645) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke › zaehlzeiten |
| [PI_55648](/schnittstellen/202610/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke › zaehlzeiten |
| [PI_55650](/schnittstellen/202610/pruefi/UTILMD/PI_55650) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke › zaehlzeiten |
| [PI_55653](/schnittstellen/202610/pruefi/UTILMD/PI_55653) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke › zaehlzeiten |
| [PI_55655](/schnittstellen/202610/pruefi/UTILMD/PI_55655) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke › zaehlzeiten |
| [PI_55658](/schnittstellen/202610/pruefi/UTILMD/PI_55658) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke › zaehlzeiten |
| [PI_55660](/schnittstellen/202610/pruefi/UTILMD/PI_55660) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke › zaehlzeiten |
| [PI_55663](/schnittstellen/202610/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke › zaehlzeiten |
| [PI_55665](/schnittstellen/202610/pruefi/UTILMD/PI_55665) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke › zaehlzeiten |
| [PI_55669](/schnittstellen/202610/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke › zaehlzeiten |

### zaehlzeitDefinition

36 Verwendung(en) in den Nachrichtentypen ORDERS, UTILMD, UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_17118](/schnittstellen/202610/pruefi/ORDERS/PI_17118) | Prüfi | ORDERS | stammdaten › MESSLOKATION › zaehlwerke › zaehlzeiten |
| [PI_17121](/schnittstellen/202610/pruefi/ORDERS/PI_17121) | Prüfi | ORDERS | stammdaten › MARKTLOKATION › zaehlwerke › zaehlzeiten |
| [PI_17121](/schnittstellen/202610/pruefi/ORDERS/PI_17121) | Prüfi | ORDERS | stammdaten › MESSLOKATION › zaehlwerke › zaehlzeiten |
| [PI_17123](/schnittstellen/202610/pruefi/ORDERS/PI_17123) | Prüfi | ORDERS | stammdaten › MARKTLOKATION › zaehlwerke › zaehlzeiten |
| [PI_17134](/schnittstellen/202610/pruefi/ORDERS/PI_17134) | Prüfi | ORDERS | stammdaten › MARKTLOKATION › zaehlwerke › zaehlzeiten |
| [PI_17134](/schnittstellen/202610/pruefi/ORDERS/PI_17134) | Prüfi | ORDERS | stammdaten › MESSLOKATION › zaehlwerke › zaehlzeiten |
| [PI_17135](/schnittstellen/202610/pruefi/ORDERS/PI_17135) | Prüfi | ORDERS | stammdaten › MESSLOKATION › zaehlwerke › zaehlzeiten |
| [PI_25004](/schnittstellen/202610/pruefi/UTILTS/PI_25004) | Prüfi | UTILTS | stammdaten › ZAEHLZEITDEFINITION › zaehlzeitregister |
| [PI_55035](/schnittstellen/202610/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › netznutzungsabrechnungsdaten › zaehlzeiten |
| [PI_55035](/schnittstellen/202610/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke › zaehlzeiten |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke › zaehlzeiten |
| [PI_55043](/schnittstellen/202610/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › MESSLOKATION › zaehlwerke › zaehlzeiten |
| [PI_55060](/schnittstellen/202610/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke › zaehlzeiten |
| [PI_55060](/schnittstellen/202610/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › MESSLOKATION › zaehlwerke › zaehlzeiten |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke › zaehlzeiten |
| [PI_55168](/schnittstellen/202610/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › MESSLOKATION › zaehlwerke › zaehlzeiten |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke › zaehlzeiten |
| [PI_55169](/schnittstellen/202610/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › MESSLOKATION › zaehlwerke › zaehlzeiten |
| [PI_55218](/schnittstellen/202610/pruefi/UTILMD/PI_55218) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › netznutzungsabrechnungsdaten › zaehlzeiten |
| [PI_55220](/schnittstellen/202610/pruefi/UTILMD/PI_55220) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › netznutzungsabrechnungsdaten › zaehlzeiten |
| [PI_55553](/schnittstellen/202610/pruefi/UTILMD/PI_55553) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke › zaehlzeiten |
| [PI_55553](/schnittstellen/202610/pruefi/UTILMD/PI_55553) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke › zaehlzeiten |
| [PI_55555](/schnittstellen/202610/pruefi/UTILMD/PI_55555) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke › zaehlzeiten |
| [PI_55555](/schnittstellen/202610/pruefi/UTILMD/PI_55555) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke › zaehlzeiten |
| [PI_55640](/schnittstellen/202610/pruefi/UTILMD/PI_55640) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke › zaehlzeiten |
| [PI_55643](/schnittstellen/202610/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke › zaehlzeiten |
| [PI_55645](/schnittstellen/202610/pruefi/UTILMD/PI_55645) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke › zaehlzeiten |
| [PI_55648](/schnittstellen/202610/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke › zaehlzeiten |
| [PI_55650](/schnittstellen/202610/pruefi/UTILMD/PI_55650) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke › zaehlzeiten |
| [PI_55653](/schnittstellen/202610/pruefi/UTILMD/PI_55653) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke › zaehlzeiten |
| [PI_55655](/schnittstellen/202610/pruefi/UTILMD/PI_55655) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke › zaehlzeiten |
| [PI_55658](/schnittstellen/202610/pruefi/UTILMD/PI_55658) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke › zaehlzeiten |
| [PI_55660](/schnittstellen/202610/pruefi/UTILMD/PI_55660) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke › zaehlzeiten |
| [PI_55663](/schnittstellen/202610/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke › zaehlzeiten |
| [PI_55665](/schnittstellen/202610/pruefi/UTILMD/PI_55665) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke › zaehlzeiten |
| [PI_55669](/schnittstellen/202610/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | stammdaten › ZAEHLER › zaehlwerke › zaehlzeiten |

### schwachlastfaehig

1 Verwendung(en) in den Nachrichtentypen UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_25004](/schnittstellen/202610/pruefi/UTILTS/PI_25004) | Prüfi | UTILTS | stammdaten › ZAEHLZEITDEFINITION › zaehlzeitregister |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
