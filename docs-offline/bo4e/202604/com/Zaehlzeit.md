# Zaehlzeit
<span hidden data-pagefind-meta={"title:Zaehlzeit — BO4E-Komponente (FV 202604)"} />

BO4E-Komponente · 9 Felder · 11 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="code"></a>`code` | string | Zählzeitdefinition |
| <a id="haeufigkeit"></a>`haeufigkeit` | [Enum HaeufigkeitZaehlzeit](/bo4e/202604/enum/HaeufigkeitZaehlzeit)<br/><Werte>`EINMALIG`, `JAEHRLICH`</Werte> | Häufigkeit der Übermittlung |
| <a id="uebermittelbarkeit"></a>`uebermittelbarkeit` | [Enum UebermittelbarkeitZaehlzeit](/bo4e/202604/enum/UebermittelbarkeitZaehlzeit)<br/><Werte>`ELEKTRONISCH`, `NICHT_ELEKTRONISCH`</Werte> | Art der Übermittlung |
| <a id="ermittlungleistungsmaximum"></a>`ermittlungLeistungsmaximum` | [Enum ErmittlungLeistungsmaximum](/bo4e/202604/enum/ErmittlungLeistungsmaximum)<br/><Werte>`VERWENDUNG_HOCHLASTFENSTER`, `KEINE_VERWENDUNG_HOCHLASTFENSTER`</Werte> | Ermittlung Leistungsmaximum |
| <a id="istbestellbar"></a>`istBestellbar` | boolean | Ist die Zählzeit bestellbar? |
| <a id="typ"></a>`typ` | [Enum ZaehlzeitdefinitionTyp](/bo4e/202604/enum/ZaehlzeitdefinitionTyp)<br/><Werte>`WAERMEPUMPE`, `NACHTSPEICHERHEIZUNG`, `SCHWACHLASTZEITFENSTER`, `SONSTIGE`, `HOCHLASTZEITFENSTER`</Werte> | ZählzeitdefinitionTyp |
| <a id="beschreibungtyp"></a>`beschreibungTyp` | string | Beschreibung des ZählzeitdefinitionTyp |
| <a id="aenderungszeitpunkt"></a>`aenderungszeitpunkt` | string (date-time) | aenderungszeitpunkt |
| <a id="register"></a>`register` | string | register |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[code](/bo4e/202604/com/Zaehlzeit#code)</span> | Zählzeitdefinition | string |
| <span className="hbs-f hbs-e0">[haeufigkeit](/bo4e/202604/com/Zaehlzeit#haeufigkeit)</span> | Häufigkeit der Übermittlung | [Enum HaeufigkeitZaehlzeit](/bo4e/202604/enum/HaeufigkeitZaehlzeit)<br/><Werte>`EINMALIG`, `JAEHRLICH`</Werte> |
| <span className="hbs-f hbs-e0">[uebermittelbarkeit](/bo4e/202604/com/Zaehlzeit#uebermittelbarkeit)</span> | Art der Übermittlung | [Enum UebermittelbarkeitZaehlzeit](/bo4e/202604/enum/UebermittelbarkeitZaehlzeit)<br/><Werte>`ELEKTRONISCH`, `NICHT_ELEKTRONISCH`</Werte> |
| <span className="hbs-f hbs-e0">[ermittlungLeistungsmaximum](/bo4e/202604/com/Zaehlzeit#ermittlungleistungsmaximum)</span> | Ermittlung Leistungsmaximum | [Enum ErmittlungLeistungsmaximum](/bo4e/202604/enum/ErmittlungLeistungsmaximum)<br/><Werte>`VERWENDUNG_HOCHLASTFENSTER`, `KEINE_VERWENDUNG_HOCHLASTFENSTER`</Werte> |
| <span className="hbs-f hbs-e0">[istBestellbar](/bo4e/202604/com/Zaehlzeit#istbestellbar)</span> | Ist die Zählzeit bestellbar? | boolean |
| <span className="hbs-f hbs-e0">[typ](/bo4e/202604/com/Zaehlzeit#typ)</span> | ZählzeitdefinitionTyp | [Enum ZaehlzeitdefinitionTyp](/bo4e/202604/enum/ZaehlzeitdefinitionTyp)<br/><Werte>`WAERMEPUMPE`, `NACHTSPEICHERHEIZUNG`, `SCHWACHLASTZEITFENSTER`, `SONSTIGE`, `HOCHLASTZEITFENSTER`</Werte> |
| <span className="hbs-f hbs-e0">[beschreibungTyp](/bo4e/202604/com/Zaehlzeit#beschreibungtyp)</span> | Beschreibung des ZählzeitdefinitionTyp | string |
| <span className="hbs-f hbs-e0">[aenderungszeitpunkt](/bo4e/202604/com/Zaehlzeit#aenderungszeitpunkt)</span> | aenderungszeitpunkt | string (date-time) |
| <span className="hbs-f hbs-e0">[register](/bo4e/202604/com/Zaehlzeit#register)</span> | register | string |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### code

2 Verwendung(en) in den Nachrichtentypen ORDERS, UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_17122](/schnittstellen/202604/pruefi/ORDERS/PI_17122) | Prüfi | ORDERS | stammdaten › ZAEHLZEITDEFINITION › zaehlzeiten |
| [PI_25004](/schnittstellen/202604/pruefi/UTILTS/PI_25004) | Prüfi | UTILTS | stammdaten › ZAEHLZEITDEFINITION › zaehlzeiten |

### haeufigkeit

2 Verwendung(en) in den Nachrichtentypen UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_25004](/schnittstellen/202604/pruefi/UTILTS/PI_25004) | Prüfi | UTILTS | stammdaten › ZAEHLZEITDEFINITION › zaehlzeiten |
| [PI_25005](/schnittstellen/202604/pruefi/UTILTS/PI_25005) | Prüfi | UTILTS | stammdaten › ZAEHLZEITDEFINITION › zaehlzeiten |

### uebermittelbarkeit

1 Verwendung(en) in den Nachrichtentypen UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_25004](/schnittstellen/202604/pruefi/UTILTS/PI_25004) | Prüfi | UTILTS | stammdaten › ZAEHLZEITDEFINITION › zaehlzeiten |

### ermittlungLeistungsmaximum

1 Verwendung(en) in den Nachrichtentypen UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_25004](/schnittstellen/202604/pruefi/UTILTS/PI_25004) | Prüfi | UTILTS | stammdaten › ZAEHLZEITDEFINITION › zaehlzeiten |

### istBestellbar

1 Verwendung(en) in den Nachrichtentypen UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_25004](/schnittstellen/202604/pruefi/UTILTS/PI_25004) | Prüfi | UTILTS | stammdaten › ZAEHLZEITDEFINITION › zaehlzeiten |

### typ

1 Verwendung(en) in den Nachrichtentypen UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_25004](/schnittstellen/202604/pruefi/UTILTS/PI_25004) | Prüfi | UTILTS | stammdaten › ZAEHLZEITDEFINITION › zaehlzeiten |

### beschreibungTyp

1 Verwendung(en) in den Nachrichtentypen UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_25004](/schnittstellen/202604/pruefi/UTILTS/PI_25004) | Prüfi | UTILTS | stammdaten › ZAEHLZEITDEFINITION › zaehlzeiten |

### aenderungszeitpunkt

1 Verwendung(en) in den Nachrichtentypen UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_25005](/schnittstellen/202604/pruefi/UTILTS/PI_25005) | Prüfi | UTILTS | stammdaten › ZAEHLZEITDEFINITION › zaehlzeiten |

### register

1 Verwendung(en) in den Nachrichtentypen UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_25005](/schnittstellen/202604/pruefi/UTILTS/PI_25005) | Prüfi | UTILTS | stammdaten › ZAEHLZEITDEFINITION › zaehlzeiten |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
