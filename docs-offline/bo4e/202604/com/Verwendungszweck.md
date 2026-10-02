# Verwendungszweck
<span hidden data-pagefind-meta={"title:Verwendungszweck — BO4E-Komponente (FV 202604)"} />

BO4E-Komponente · 2 Felder · 64 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="marktrolle"></a>`marktrolle` | [Enum Marktrolle](/bo4e/202604/enum/Marktrolle)<br/><Werte>`NB`, `LF`, `MSB`, `MSBA`, `GMSB`, `MDL`, `DL`, `BKV`, `UENB`, `KUNDE-SELBST-NN`, `MGV`, `EIV`, `RB`, `KUNDE`, `INTERESSENT`, `KN`, `UBA`, `BIKO`, `ESA`</Werte> | Diese Rollen kann ein Marktteilnehmer einnehmen |
| <a id="zweck"></a>`zweck` | [Enum VerwendungszweckValue[]](/bo4e/202604/enum/VerwendungszweckValue)<br/><Werte>`NETZNUTZUNGSABRECHNUNG`, `BILANZKREISABRECHNUNG`, `MEHRMINDERMENGENABRECHNUNG`, `ENDKUNDENABRECHNUNG`, `UEBERMITTLUNG_AN_DAS_HKNR`, `BLINDARBEITSABRECHNUNG`, `ERMITTLUNG_AUSGEGLICHENHEIT_BILANZKREIS`, `BLINDARBEITABRECHNUNG_BETRIEBSFUEHRUNG`, `ES_LIEGT_KEIN_VERWENDUNGSZWECK_VOR`</Werte> | zweck |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[marktrolle](/bo4e/202604/com/Verwendungszweck#marktrolle)</span> | Diese Rollen kann ein Marktteilnehmer einnehmen | [Enum Marktrolle](/bo4e/202604/enum/Marktrolle)<br/><Werte>`NB`, `LF`, `MSB`, `MSBA`, `GMSB`, `MDL`, `DL`, `BKV`, `UENB`, `KUNDE-SELBST-NN`, `MGV`, `EIV`, `RB`, `KUNDE`, `INTERESSENT`, `KN`, `UBA`, `BIKO`, `ESA`</Werte> |
| <span className="hbs-f hbs-e0">[zweck](/bo4e/202604/com/Verwendungszweck#zweck) <span className="hbs-liste">[ ]</span></span> | zweck | [Enum VerwendungszweckValue[]](/bo4e/202604/enum/VerwendungszweckValue)<br/><Werte>`NETZNUTZUNGSABRECHNUNG`, `BILANZKREISABRECHNUNG`, `MEHRMINDERMENGENABRECHNUNG`, `ENDKUNDENABRECHNUNG`, `UEBERMITTLUNG_AN_DAS_HKNR`, `BLINDARBEITSABRECHNUNG`, `ERMITTLUNG_AUSGEGLICHENHEIT_BILANZKREIS`, `BLINDARBEITABRECHNUNG_BETRIEBSFUEHRUNG`, `ES_LIEGT_KEIN_VERWENDUNGSZWECK_VOR`</Werte> |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### marktrolle

32 Verwendung(en) in den Nachrichtentypen ORDERS, UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_17121](/schnittstellen/202604/pruefi/ORDERS/PI_17121) | Prüfi | ORDERS | stammdaten › MARKTLOKATION › zaehlwerke › verwendungszwecke |
| [PI_17121](/schnittstellen/202604/pruefi/ORDERS/PI_17121) | Prüfi | ORDERS | stammdaten › NETZLOKATION › zaehlwerke › verwendungszwecke |
| [PI_17121](/schnittstellen/202604/pruefi/ORDERS/PI_17121) | Prüfi | ORDERS | stammdaten › TRANCHE › zaehlwerke › verwendungszwecke |
| [PI_17134](/schnittstellen/202604/pruefi/ORDERS/PI_17134) | Prüfi | ORDERS | stammdaten › MARKTLOKATION › zaehlwerke › verwendungszwecke |
| [PI_17134](/schnittstellen/202604/pruefi/ORDERS/PI_17134) | Prüfi | ORDERS | stammdaten › TRANCHE › zaehlwerke › verwendungszwecke |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke › verwendungszwecke |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › NETZLOKATION › zaehlwerke › verwendungszwecke |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke › verwendungszwecke |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke › verwendungszwecke |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › NETZLOKATION › zaehlwerke › verwendungszwecke |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke › verwendungszwecke |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke › verwendungszwecke |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › NETZLOKATION › zaehlwerke › verwendungszwecke |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke › verwendungszwecke |
| [PI_55639](/schnittstellen/202604/pruefi/UTILMD/PI_55639) | Prüfi | UTILMD | stammdaten › NETZLOKATION › zaehlwerke › verwendungszwecke |
| [PI_55640](/schnittstellen/202604/pruefi/UTILMD/PI_55640) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke › verwendungszwecke |
| [PI_55642](/schnittstellen/202604/pruefi/UTILMD/PI_55642) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke › verwendungszwecke |
| [PI_55644](/schnittstellen/202604/pruefi/UTILMD/PI_55644) | Prüfi | UTILMD | stammdaten › NETZLOKATION › zaehlwerke › verwendungszwecke |
| [PI_55645](/schnittstellen/202604/pruefi/UTILMD/PI_55645) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke › verwendungszwecke |
| [PI_55647](/schnittstellen/202604/pruefi/UTILMD/PI_55647) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke › verwendungszwecke |
| [PI_55649](/schnittstellen/202604/pruefi/UTILMD/PI_55649) | Prüfi | UTILMD | stammdaten › NETZLOKATION › zaehlwerke › verwendungszwecke |
| [PI_55650](/schnittstellen/202604/pruefi/UTILMD/PI_55650) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke › verwendungszwecke |
| [PI_55652](/schnittstellen/202604/pruefi/UTILMD/PI_55652) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke › verwendungszwecke |
| [PI_55654](/schnittstellen/202604/pruefi/UTILMD/PI_55654) | Prüfi | UTILMD | stammdaten › NETZLOKATION › zaehlwerke › verwendungszwecke |
| [PI_55655](/schnittstellen/202604/pruefi/UTILMD/PI_55655) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke › verwendungszwecke |
| [PI_55657](/schnittstellen/202604/pruefi/UTILMD/PI_55657) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke › verwendungszwecke |
| [PI_55659](/schnittstellen/202604/pruefi/UTILMD/PI_55659) | Prüfi | UTILMD | stammdaten › NETZLOKATION › zaehlwerke › verwendungszwecke |
| [PI_55660](/schnittstellen/202604/pruefi/UTILMD/PI_55660) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke › verwendungszwecke |
| [PI_55662](/schnittstellen/202604/pruefi/UTILMD/PI_55662) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke › verwendungszwecke |
| [PI_55664](/schnittstellen/202604/pruefi/UTILMD/PI_55664) | Prüfi | UTILMD | stammdaten › NETZLOKATION › zaehlwerke › verwendungszwecke |
| [PI_55665](/schnittstellen/202604/pruefi/UTILMD/PI_55665) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke › verwendungszwecke |
| [PI_55667](/schnittstellen/202604/pruefi/UTILMD/PI_55667) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke › verwendungszwecke |

### zweck

32 Verwendung(en) in den Nachrichtentypen ORDERS, UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_17121](/schnittstellen/202604/pruefi/ORDERS/PI_17121) | Prüfi | ORDERS | stammdaten › MARKTLOKATION › zaehlwerke › verwendungszwecke |
| [PI_17121](/schnittstellen/202604/pruefi/ORDERS/PI_17121) | Prüfi | ORDERS | stammdaten › NETZLOKATION › zaehlwerke › verwendungszwecke |
| [PI_17121](/schnittstellen/202604/pruefi/ORDERS/PI_17121) | Prüfi | ORDERS | stammdaten › TRANCHE › zaehlwerke › verwendungszwecke |
| [PI_17134](/schnittstellen/202604/pruefi/ORDERS/PI_17134) | Prüfi | ORDERS | stammdaten › MARKTLOKATION › zaehlwerke › verwendungszwecke |
| [PI_17134](/schnittstellen/202604/pruefi/ORDERS/PI_17134) | Prüfi | ORDERS | stammdaten › TRANCHE › zaehlwerke › verwendungszwecke |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke › verwendungszwecke |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › NETZLOKATION › zaehlwerke › verwendungszwecke |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke › verwendungszwecke |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke › verwendungszwecke |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › NETZLOKATION › zaehlwerke › verwendungszwecke |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke › verwendungszwecke |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke › verwendungszwecke |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › NETZLOKATION › zaehlwerke › verwendungszwecke |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke › verwendungszwecke |
| [PI_55639](/schnittstellen/202604/pruefi/UTILMD/PI_55639) | Prüfi | UTILMD | stammdaten › NETZLOKATION › zaehlwerke › verwendungszwecke |
| [PI_55640](/schnittstellen/202604/pruefi/UTILMD/PI_55640) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke › verwendungszwecke |
| [PI_55642](/schnittstellen/202604/pruefi/UTILMD/PI_55642) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke › verwendungszwecke |
| [PI_55644](/schnittstellen/202604/pruefi/UTILMD/PI_55644) | Prüfi | UTILMD | stammdaten › NETZLOKATION › zaehlwerke › verwendungszwecke |
| [PI_55645](/schnittstellen/202604/pruefi/UTILMD/PI_55645) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke › verwendungszwecke |
| [PI_55647](/schnittstellen/202604/pruefi/UTILMD/PI_55647) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke › verwendungszwecke |
| [PI_55649](/schnittstellen/202604/pruefi/UTILMD/PI_55649) | Prüfi | UTILMD | stammdaten › NETZLOKATION › zaehlwerke › verwendungszwecke |
| [PI_55650](/schnittstellen/202604/pruefi/UTILMD/PI_55650) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke › verwendungszwecke |
| [PI_55652](/schnittstellen/202604/pruefi/UTILMD/PI_55652) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke › verwendungszwecke |
| [PI_55654](/schnittstellen/202604/pruefi/UTILMD/PI_55654) | Prüfi | UTILMD | stammdaten › NETZLOKATION › zaehlwerke › verwendungszwecke |
| [PI_55655](/schnittstellen/202604/pruefi/UTILMD/PI_55655) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke › verwendungszwecke |
| [PI_55657](/schnittstellen/202604/pruefi/UTILMD/PI_55657) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke › verwendungszwecke |
| [PI_55659](/schnittstellen/202604/pruefi/UTILMD/PI_55659) | Prüfi | UTILMD | stammdaten › NETZLOKATION › zaehlwerke › verwendungszwecke |
| [PI_55660](/schnittstellen/202604/pruefi/UTILMD/PI_55660) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke › verwendungszwecke |
| [PI_55662](/schnittstellen/202604/pruefi/UTILMD/PI_55662) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke › verwendungszwecke |
| [PI_55664](/schnittstellen/202604/pruefi/UTILMD/PI_55664) | Prüfi | UTILMD | stammdaten › NETZLOKATION › zaehlwerke › verwendungszwecke |
| [PI_55665](/schnittstellen/202604/pruefi/UTILMD/PI_55665) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › zaehlwerke › verwendungszwecke |
| [PI_55667](/schnittstellen/202604/pruefi/UTILMD/PI_55667) | Prüfi | UTILMD | stammdaten › TRANCHE › zaehlwerke › verwendungszwecke |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
