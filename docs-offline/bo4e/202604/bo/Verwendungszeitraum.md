# Verwendungszeitraum
<span hidden data-pagefind-meta={"title:Verwendungszeitraum — BO4E-Geschäftsobjekt (FV 202604)"} />

BO4E-Geschäftsobjekt · 6 Felder · 336 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="botyp"></a>`boTyp` <span className="hbs-pflicht">\*</span> | [Enum BOTyp](/bo4e/202604/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> | Typ des BO |
| <a id="versionstruktur"></a>`versionStruktur` <span className="hbs-pflicht">\*</span> | string | versionStruktur |
| <a id="verwendungab"></a>`verwendungAb` | string (date-time) | verwendungAb |
| <a id="verwendungbis"></a>`verwendungBis` | string (date-time) | verwendungBis |
| <a id="zeitraumid"></a>`zeitraumId` | integer | zeitraumId |
| <a id="datenqualitaet"></a>`datenqualitaet` | [Enum Datenqualitaet](/bo4e/202604/enum/Datenqualitaet)<br/><Werte>`ERWARTETE_DATEN`, `IM_SYSTEM_VORHANDENE_DATEN`, `INFORMATIVE_DATEN`, `GUELTIGE_DATEN`, `KEINE_DATEN`, `IM_SYSTEM_KEINE_DATEN_VORHANDEN`, `KEINE_DATEN_ERWARTET`, `DIFFERENZ_DATEN`, `DIFFERENZ_ERWARTETE_DATEN`, `DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</Werte> | Datenqualitaet |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[boTyp](/bo4e/202604/bo/Verwendungszeitraum#botyp) <span className="hbs-pflicht">\*</span></span> | Typ des BO | [Enum BOTyp](/bo4e/202604/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> |
| <span className="hbs-f hbs-e0">[versionStruktur](/bo4e/202604/bo/Verwendungszeitraum#versionstruktur) <span className="hbs-pflicht">\*</span></span> | versionStruktur | string |
| <span className="hbs-f hbs-e0">[verwendungAb](/bo4e/202604/bo/Verwendungszeitraum#verwendungab)</span> | verwendungAb | string (date-time) |
| <span className="hbs-f hbs-e0">[verwendungBis](/bo4e/202604/bo/Verwendungszeitraum#verwendungbis)</span> | verwendungBis | string (date-time) |
| <span className="hbs-f hbs-e0">[zeitraumId](/bo4e/202604/bo/Verwendungszeitraum#zeitraumid)</span> | zeitraumId | integer |
| <span className="hbs-f hbs-e0">[datenqualitaet](/bo4e/202604/bo/Verwendungszeitraum#datenqualitaet)</span> | Datenqualitaet | [Enum Datenqualitaet](/bo4e/202604/enum/Datenqualitaet)<br/><Werte>`ERWARTETE_DATEN`, `IM_SYSTEM_VORHANDENE_DATEN`, `INFORMATIVE_DATEN`, `GUELTIGE_DATEN`, `KEINE_DATEN`, `IM_SYSTEM_KEINE_DATEN_VORHANDEN`, `KEINE_DATEN_ERWARTET`, `DIFFERENZ_DATEN`, `DIFFERENZ_ERWARTETE_DATEN`, `DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN`</Werte> |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### verwendungAb

85 Verwendung(en) in den Nachrichtentypen UTILMD, UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_25001](/schnittstellen/202604/pruefi/UTILTS/PI_25001) | Prüfi | UTILTS | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55109](/schnittstellen/202604/pruefi/UTILMD/PI_55109) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55110](/schnittstellen/202604/pruefi/UTILMD/PI_55110) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55126](/schnittstellen/202604/pruefi/UTILMD/PI_55126) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55136](/schnittstellen/202604/pruefi/UTILMD/PI_55136) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55137](/schnittstellen/202604/pruefi/UTILMD/PI_55137) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55156](/schnittstellen/202604/pruefi/UTILMD/PI_55156) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55173](/schnittstellen/202604/pruefi/UTILMD/PI_55173) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55175](/schnittstellen/202604/pruefi/UTILMD/PI_55175) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55177](/schnittstellen/202604/pruefi/UTILMD/PI_55177) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55180](/schnittstellen/202604/pruefi/UTILMD/PI_55180) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55218](/schnittstellen/202604/pruefi/UTILMD/PI_55218) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55220](/schnittstellen/202604/pruefi/UTILMD/PI_55220) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55225](/schnittstellen/202604/pruefi/UTILMD/PI_55225) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55227](/schnittstellen/202604/pruefi/UTILMD/PI_55227) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55230](/schnittstellen/202604/pruefi/UTILMD/PI_55230) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55232](/schnittstellen/202604/pruefi/UTILMD/PI_55232) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55553](/schnittstellen/202604/pruefi/UTILMD/PI_55553) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55555](/schnittstellen/202604/pruefi/UTILMD/PI_55555) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55557](/schnittstellen/202604/pruefi/UTILMD/PI_55557) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55559](/schnittstellen/202604/pruefi/UTILMD/PI_55559) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55613](/schnittstellen/202604/pruefi/UTILMD/PI_55613) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55614](/schnittstellen/202604/pruefi/UTILMD/PI_55614) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55615](/schnittstellen/202604/pruefi/UTILMD/PI_55615) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55616](/schnittstellen/202604/pruefi/UTILMD/PI_55616) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55617](/schnittstellen/202604/pruefi/UTILMD/PI_55617) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55618](/schnittstellen/202604/pruefi/UTILMD/PI_55618) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55619](/schnittstellen/202604/pruefi/UTILMD/PI_55619) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55620](/schnittstellen/202604/pruefi/UTILMD/PI_55620) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55621](/schnittstellen/202604/pruefi/UTILMD/PI_55621) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55622](/schnittstellen/202604/pruefi/UTILMD/PI_55622) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55623](/schnittstellen/202604/pruefi/UTILMD/PI_55623) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55624](/schnittstellen/202604/pruefi/UTILMD/PI_55624) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55625](/schnittstellen/202604/pruefi/UTILMD/PI_55625) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55626](/schnittstellen/202604/pruefi/UTILMD/PI_55626) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55627](/schnittstellen/202604/pruefi/UTILMD/PI_55627) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55628](/schnittstellen/202604/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55629](/schnittstellen/202604/pruefi/UTILMD/PI_55629) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55630](/schnittstellen/202604/pruefi/UTILMD/PI_55630) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55632](/schnittstellen/202604/pruefi/UTILMD/PI_55632) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55633](/schnittstellen/202604/pruefi/UTILMD/PI_55633) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55634](/schnittstellen/202604/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55635](/schnittstellen/202604/pruefi/UTILMD/PI_55635) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55636](/schnittstellen/202604/pruefi/UTILMD/PI_55636) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55638](/schnittstellen/202604/pruefi/UTILMD/PI_55638) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55639](/schnittstellen/202604/pruefi/UTILMD/PI_55639) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55640](/schnittstellen/202604/pruefi/UTILMD/PI_55640) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55641](/schnittstellen/202604/pruefi/UTILMD/PI_55641) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55642](/schnittstellen/202604/pruefi/UTILMD/PI_55642) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55643](/schnittstellen/202604/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55644](/schnittstellen/202604/pruefi/UTILMD/PI_55644) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55645](/schnittstellen/202604/pruefi/UTILMD/PI_55645) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55646](/schnittstellen/202604/pruefi/UTILMD/PI_55646) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55647](/schnittstellen/202604/pruefi/UTILMD/PI_55647) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55648](/schnittstellen/202604/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55649](/schnittstellen/202604/pruefi/UTILMD/PI_55649) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55650](/schnittstellen/202604/pruefi/UTILMD/PI_55650) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55651](/schnittstellen/202604/pruefi/UTILMD/PI_55651) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55652](/schnittstellen/202604/pruefi/UTILMD/PI_55652) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55653](/schnittstellen/202604/pruefi/UTILMD/PI_55653) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55654](/schnittstellen/202604/pruefi/UTILMD/PI_55654) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55655](/schnittstellen/202604/pruefi/UTILMD/PI_55655) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55656](/schnittstellen/202604/pruefi/UTILMD/PI_55656) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55657](/schnittstellen/202604/pruefi/UTILMD/PI_55657) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55658](/schnittstellen/202604/pruefi/UTILMD/PI_55658) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55659](/schnittstellen/202604/pruefi/UTILMD/PI_55659) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55660](/schnittstellen/202604/pruefi/UTILMD/PI_55660) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55661](/schnittstellen/202604/pruefi/UTILMD/PI_55661) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55662](/schnittstellen/202604/pruefi/UTILMD/PI_55662) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55663](/schnittstellen/202604/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55664](/schnittstellen/202604/pruefi/UTILMD/PI_55664) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55665](/schnittstellen/202604/pruefi/UTILMD/PI_55665) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55666](/schnittstellen/202604/pruefi/UTILMD/PI_55666) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55667](/schnittstellen/202604/pruefi/UTILMD/PI_55667) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55669](/schnittstellen/202604/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55670](/schnittstellen/202604/pruefi/UTILMD/PI_55670) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55672](/schnittstellen/202604/pruefi/UTILMD/PI_55672) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55673](/schnittstellen/202604/pruefi/UTILMD/PI_55673) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55674](/schnittstellen/202604/pruefi/UTILMD/PI_55674) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55684](/schnittstellen/202604/pruefi/UTILMD/PI_55684) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55686](/schnittstellen/202604/pruefi/UTILMD/PI_55686) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55688](/schnittstellen/202604/pruefi/UTILMD/PI_55688) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55690](/schnittstellen/202604/pruefi/UTILMD/PI_55690) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55691](/schnittstellen/202604/pruefi/UTILMD/PI_55691) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55692](/schnittstellen/202604/pruefi/UTILMD/PI_55692) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |

### verwendungBis

83 Verwendung(en) in den Nachrichtentypen UTILMD, UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_25001](/schnittstellen/202604/pruefi/UTILTS/PI_25001) | Prüfi | UTILTS | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55109](/schnittstellen/202604/pruefi/UTILMD/PI_55109) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55110](/schnittstellen/202604/pruefi/UTILMD/PI_55110) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55126](/schnittstellen/202604/pruefi/UTILMD/PI_55126) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55136](/schnittstellen/202604/pruefi/UTILMD/PI_55136) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55137](/schnittstellen/202604/pruefi/UTILMD/PI_55137) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55156](/schnittstellen/202604/pruefi/UTILMD/PI_55156) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55173](/schnittstellen/202604/pruefi/UTILMD/PI_55173) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55175](/schnittstellen/202604/pruefi/UTILMD/PI_55175) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55177](/schnittstellen/202604/pruefi/UTILMD/PI_55177) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55180](/schnittstellen/202604/pruefi/UTILMD/PI_55180) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55218](/schnittstellen/202604/pruefi/UTILMD/PI_55218) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55220](/schnittstellen/202604/pruefi/UTILMD/PI_55220) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55225](/schnittstellen/202604/pruefi/UTILMD/PI_55225) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55227](/schnittstellen/202604/pruefi/UTILMD/PI_55227) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55230](/schnittstellen/202604/pruefi/UTILMD/PI_55230) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55232](/schnittstellen/202604/pruefi/UTILMD/PI_55232) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55553](/schnittstellen/202604/pruefi/UTILMD/PI_55553) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55555](/schnittstellen/202604/pruefi/UTILMD/PI_55555) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55557](/schnittstellen/202604/pruefi/UTILMD/PI_55557) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55559](/schnittstellen/202604/pruefi/UTILMD/PI_55559) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55613](/schnittstellen/202604/pruefi/UTILMD/PI_55613) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55614](/schnittstellen/202604/pruefi/UTILMD/PI_55614) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55615](/schnittstellen/202604/pruefi/UTILMD/PI_55615) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55616](/schnittstellen/202604/pruefi/UTILMD/PI_55616) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55617](/schnittstellen/202604/pruefi/UTILMD/PI_55617) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55618](/schnittstellen/202604/pruefi/UTILMD/PI_55618) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55619](/schnittstellen/202604/pruefi/UTILMD/PI_55619) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55620](/schnittstellen/202604/pruefi/UTILMD/PI_55620) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55621](/schnittstellen/202604/pruefi/UTILMD/PI_55621) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55622](/schnittstellen/202604/pruefi/UTILMD/PI_55622) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55623](/schnittstellen/202604/pruefi/UTILMD/PI_55623) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55624](/schnittstellen/202604/pruefi/UTILMD/PI_55624) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55625](/schnittstellen/202604/pruefi/UTILMD/PI_55625) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55626](/schnittstellen/202604/pruefi/UTILMD/PI_55626) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55627](/schnittstellen/202604/pruefi/UTILMD/PI_55627) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55628](/schnittstellen/202604/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55629](/schnittstellen/202604/pruefi/UTILMD/PI_55629) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55630](/schnittstellen/202604/pruefi/UTILMD/PI_55630) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55632](/schnittstellen/202604/pruefi/UTILMD/PI_55632) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55633](/schnittstellen/202604/pruefi/UTILMD/PI_55633) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55634](/schnittstellen/202604/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55635](/schnittstellen/202604/pruefi/UTILMD/PI_55635) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55636](/schnittstellen/202604/pruefi/UTILMD/PI_55636) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55638](/schnittstellen/202604/pruefi/UTILMD/PI_55638) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55639](/schnittstellen/202604/pruefi/UTILMD/PI_55639) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55640](/schnittstellen/202604/pruefi/UTILMD/PI_55640) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55641](/schnittstellen/202604/pruefi/UTILMD/PI_55641) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55642](/schnittstellen/202604/pruefi/UTILMD/PI_55642) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55643](/schnittstellen/202604/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55644](/schnittstellen/202604/pruefi/UTILMD/PI_55644) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55645](/schnittstellen/202604/pruefi/UTILMD/PI_55645) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55646](/schnittstellen/202604/pruefi/UTILMD/PI_55646) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55647](/schnittstellen/202604/pruefi/UTILMD/PI_55647) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55648](/schnittstellen/202604/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55649](/schnittstellen/202604/pruefi/UTILMD/PI_55649) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55650](/schnittstellen/202604/pruefi/UTILMD/PI_55650) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55651](/schnittstellen/202604/pruefi/UTILMD/PI_55651) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55652](/schnittstellen/202604/pruefi/UTILMD/PI_55652) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55653](/schnittstellen/202604/pruefi/UTILMD/PI_55653) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55654](/schnittstellen/202604/pruefi/UTILMD/PI_55654) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55655](/schnittstellen/202604/pruefi/UTILMD/PI_55655) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55656](/schnittstellen/202604/pruefi/UTILMD/PI_55656) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55657](/schnittstellen/202604/pruefi/UTILMD/PI_55657) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55658](/schnittstellen/202604/pruefi/UTILMD/PI_55658) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55659](/schnittstellen/202604/pruefi/UTILMD/PI_55659) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55660](/schnittstellen/202604/pruefi/UTILMD/PI_55660) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55661](/schnittstellen/202604/pruefi/UTILMD/PI_55661) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55662](/schnittstellen/202604/pruefi/UTILMD/PI_55662) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55663](/schnittstellen/202604/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55664](/schnittstellen/202604/pruefi/UTILMD/PI_55664) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55665](/schnittstellen/202604/pruefi/UTILMD/PI_55665) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55666](/schnittstellen/202604/pruefi/UTILMD/PI_55666) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55667](/schnittstellen/202604/pruefi/UTILMD/PI_55667) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55669](/schnittstellen/202604/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55670](/schnittstellen/202604/pruefi/UTILMD/PI_55670) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55672](/schnittstellen/202604/pruefi/UTILMD/PI_55672) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55673](/schnittstellen/202604/pruefi/UTILMD/PI_55673) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55674](/schnittstellen/202604/pruefi/UTILMD/PI_55674) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55684](/schnittstellen/202604/pruefi/UTILMD/PI_55684) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55686](/schnittstellen/202604/pruefi/UTILMD/PI_55686) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55688](/schnittstellen/202604/pruefi/UTILMD/PI_55688) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55690](/schnittstellen/202604/pruefi/UTILMD/PI_55690) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |

### zeitraumId

83 Verwendung(en) in den Nachrichtentypen UTILMD, UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_25001](/schnittstellen/202604/pruefi/UTILTS/PI_25001) | Prüfi | UTILTS | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55109](/schnittstellen/202604/pruefi/UTILMD/PI_55109) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55110](/schnittstellen/202604/pruefi/UTILMD/PI_55110) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55126](/schnittstellen/202604/pruefi/UTILMD/PI_55126) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55136](/schnittstellen/202604/pruefi/UTILMD/PI_55136) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55137](/schnittstellen/202604/pruefi/UTILMD/PI_55137) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55156](/schnittstellen/202604/pruefi/UTILMD/PI_55156) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55173](/schnittstellen/202604/pruefi/UTILMD/PI_55173) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55175](/schnittstellen/202604/pruefi/UTILMD/PI_55175) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55177](/schnittstellen/202604/pruefi/UTILMD/PI_55177) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55180](/schnittstellen/202604/pruefi/UTILMD/PI_55180) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55218](/schnittstellen/202604/pruefi/UTILMD/PI_55218) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55220](/schnittstellen/202604/pruefi/UTILMD/PI_55220) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55225](/schnittstellen/202604/pruefi/UTILMD/PI_55225) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55227](/schnittstellen/202604/pruefi/UTILMD/PI_55227) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55230](/schnittstellen/202604/pruefi/UTILMD/PI_55230) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55232](/schnittstellen/202604/pruefi/UTILMD/PI_55232) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55553](/schnittstellen/202604/pruefi/UTILMD/PI_55553) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55555](/schnittstellen/202604/pruefi/UTILMD/PI_55555) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55557](/schnittstellen/202604/pruefi/UTILMD/PI_55557) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55559](/schnittstellen/202604/pruefi/UTILMD/PI_55559) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55613](/schnittstellen/202604/pruefi/UTILMD/PI_55613) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55614](/schnittstellen/202604/pruefi/UTILMD/PI_55614) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55615](/schnittstellen/202604/pruefi/UTILMD/PI_55615) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55616](/schnittstellen/202604/pruefi/UTILMD/PI_55616) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55617](/schnittstellen/202604/pruefi/UTILMD/PI_55617) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55618](/schnittstellen/202604/pruefi/UTILMD/PI_55618) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55619](/schnittstellen/202604/pruefi/UTILMD/PI_55619) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55620](/schnittstellen/202604/pruefi/UTILMD/PI_55620) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55621](/schnittstellen/202604/pruefi/UTILMD/PI_55621) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55622](/schnittstellen/202604/pruefi/UTILMD/PI_55622) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55623](/schnittstellen/202604/pruefi/UTILMD/PI_55623) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55624](/schnittstellen/202604/pruefi/UTILMD/PI_55624) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55625](/schnittstellen/202604/pruefi/UTILMD/PI_55625) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55626](/schnittstellen/202604/pruefi/UTILMD/PI_55626) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55627](/schnittstellen/202604/pruefi/UTILMD/PI_55627) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55628](/schnittstellen/202604/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55629](/schnittstellen/202604/pruefi/UTILMD/PI_55629) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55630](/schnittstellen/202604/pruefi/UTILMD/PI_55630) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55632](/schnittstellen/202604/pruefi/UTILMD/PI_55632) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55633](/schnittstellen/202604/pruefi/UTILMD/PI_55633) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55634](/schnittstellen/202604/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55635](/schnittstellen/202604/pruefi/UTILMD/PI_55635) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55636](/schnittstellen/202604/pruefi/UTILMD/PI_55636) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55638](/schnittstellen/202604/pruefi/UTILMD/PI_55638) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55639](/schnittstellen/202604/pruefi/UTILMD/PI_55639) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55640](/schnittstellen/202604/pruefi/UTILMD/PI_55640) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55641](/schnittstellen/202604/pruefi/UTILMD/PI_55641) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55642](/schnittstellen/202604/pruefi/UTILMD/PI_55642) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55643](/schnittstellen/202604/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55644](/schnittstellen/202604/pruefi/UTILMD/PI_55644) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55645](/schnittstellen/202604/pruefi/UTILMD/PI_55645) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55646](/schnittstellen/202604/pruefi/UTILMD/PI_55646) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55647](/schnittstellen/202604/pruefi/UTILMD/PI_55647) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55648](/schnittstellen/202604/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55649](/schnittstellen/202604/pruefi/UTILMD/PI_55649) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55650](/schnittstellen/202604/pruefi/UTILMD/PI_55650) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55651](/schnittstellen/202604/pruefi/UTILMD/PI_55651) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55652](/schnittstellen/202604/pruefi/UTILMD/PI_55652) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55653](/schnittstellen/202604/pruefi/UTILMD/PI_55653) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55654](/schnittstellen/202604/pruefi/UTILMD/PI_55654) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55655](/schnittstellen/202604/pruefi/UTILMD/PI_55655) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55656](/schnittstellen/202604/pruefi/UTILMD/PI_55656) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55657](/schnittstellen/202604/pruefi/UTILMD/PI_55657) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55658](/schnittstellen/202604/pruefi/UTILMD/PI_55658) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55659](/schnittstellen/202604/pruefi/UTILMD/PI_55659) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55660](/schnittstellen/202604/pruefi/UTILMD/PI_55660) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55661](/schnittstellen/202604/pruefi/UTILMD/PI_55661) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55662](/schnittstellen/202604/pruefi/UTILMD/PI_55662) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55663](/schnittstellen/202604/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55664](/schnittstellen/202604/pruefi/UTILMD/PI_55664) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55665](/schnittstellen/202604/pruefi/UTILMD/PI_55665) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55666](/schnittstellen/202604/pruefi/UTILMD/PI_55666) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55667](/schnittstellen/202604/pruefi/UTILMD/PI_55667) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55669](/schnittstellen/202604/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55670](/schnittstellen/202604/pruefi/UTILMD/PI_55670) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55672](/schnittstellen/202604/pruefi/UTILMD/PI_55672) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55673](/schnittstellen/202604/pruefi/UTILMD/PI_55673) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55674](/schnittstellen/202604/pruefi/UTILMD/PI_55674) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55684](/schnittstellen/202604/pruefi/UTILMD/PI_55684) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55686](/schnittstellen/202604/pruefi/UTILMD/PI_55686) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55688](/schnittstellen/202604/pruefi/UTILMD/PI_55688) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55690](/schnittstellen/202604/pruefi/UTILMD/PI_55690) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |

### datenqualitaet

85 Verwendung(en) in den Nachrichtentypen UTILMD, UTILTS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_25001](/schnittstellen/202604/pruefi/UTILTS/PI_25001) | Prüfi | UTILTS | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55109](/schnittstellen/202604/pruefi/UTILMD/PI_55109) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55110](/schnittstellen/202604/pruefi/UTILMD/PI_55110) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55126](/schnittstellen/202604/pruefi/UTILMD/PI_55126) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55136](/schnittstellen/202604/pruefi/UTILMD/PI_55136) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55137](/schnittstellen/202604/pruefi/UTILMD/PI_55137) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55156](/schnittstellen/202604/pruefi/UTILMD/PI_55156) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55173](/schnittstellen/202604/pruefi/UTILMD/PI_55173) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55175](/schnittstellen/202604/pruefi/UTILMD/PI_55175) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55177](/schnittstellen/202604/pruefi/UTILMD/PI_55177) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55180](/schnittstellen/202604/pruefi/UTILMD/PI_55180) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55218](/schnittstellen/202604/pruefi/UTILMD/PI_55218) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55220](/schnittstellen/202604/pruefi/UTILMD/PI_55220) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55225](/schnittstellen/202604/pruefi/UTILMD/PI_55225) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55227](/schnittstellen/202604/pruefi/UTILMD/PI_55227) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55230](/schnittstellen/202604/pruefi/UTILMD/PI_55230) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55232](/schnittstellen/202604/pruefi/UTILMD/PI_55232) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55553](/schnittstellen/202604/pruefi/UTILMD/PI_55553) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55555](/schnittstellen/202604/pruefi/UTILMD/PI_55555) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55557](/schnittstellen/202604/pruefi/UTILMD/PI_55557) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55559](/schnittstellen/202604/pruefi/UTILMD/PI_55559) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55613](/schnittstellen/202604/pruefi/UTILMD/PI_55613) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55614](/schnittstellen/202604/pruefi/UTILMD/PI_55614) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55615](/schnittstellen/202604/pruefi/UTILMD/PI_55615) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55616](/schnittstellen/202604/pruefi/UTILMD/PI_55616) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55617](/schnittstellen/202604/pruefi/UTILMD/PI_55617) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55618](/schnittstellen/202604/pruefi/UTILMD/PI_55618) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55619](/schnittstellen/202604/pruefi/UTILMD/PI_55619) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55620](/schnittstellen/202604/pruefi/UTILMD/PI_55620) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55621](/schnittstellen/202604/pruefi/UTILMD/PI_55621) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55622](/schnittstellen/202604/pruefi/UTILMD/PI_55622) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55623](/schnittstellen/202604/pruefi/UTILMD/PI_55623) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55624](/schnittstellen/202604/pruefi/UTILMD/PI_55624) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55625](/schnittstellen/202604/pruefi/UTILMD/PI_55625) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55626](/schnittstellen/202604/pruefi/UTILMD/PI_55626) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55627](/schnittstellen/202604/pruefi/UTILMD/PI_55627) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55628](/schnittstellen/202604/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55629](/schnittstellen/202604/pruefi/UTILMD/PI_55629) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55630](/schnittstellen/202604/pruefi/UTILMD/PI_55630) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55632](/schnittstellen/202604/pruefi/UTILMD/PI_55632) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55633](/schnittstellen/202604/pruefi/UTILMD/PI_55633) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55634](/schnittstellen/202604/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55635](/schnittstellen/202604/pruefi/UTILMD/PI_55635) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55636](/schnittstellen/202604/pruefi/UTILMD/PI_55636) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55638](/schnittstellen/202604/pruefi/UTILMD/PI_55638) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55639](/schnittstellen/202604/pruefi/UTILMD/PI_55639) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55640](/schnittstellen/202604/pruefi/UTILMD/PI_55640) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55641](/schnittstellen/202604/pruefi/UTILMD/PI_55641) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55642](/schnittstellen/202604/pruefi/UTILMD/PI_55642) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55643](/schnittstellen/202604/pruefi/UTILMD/PI_55643) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55644](/schnittstellen/202604/pruefi/UTILMD/PI_55644) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55645](/schnittstellen/202604/pruefi/UTILMD/PI_55645) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55646](/schnittstellen/202604/pruefi/UTILMD/PI_55646) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55647](/schnittstellen/202604/pruefi/UTILMD/PI_55647) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55648](/schnittstellen/202604/pruefi/UTILMD/PI_55648) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55649](/schnittstellen/202604/pruefi/UTILMD/PI_55649) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55650](/schnittstellen/202604/pruefi/UTILMD/PI_55650) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55651](/schnittstellen/202604/pruefi/UTILMD/PI_55651) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55652](/schnittstellen/202604/pruefi/UTILMD/PI_55652) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55653](/schnittstellen/202604/pruefi/UTILMD/PI_55653) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55654](/schnittstellen/202604/pruefi/UTILMD/PI_55654) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55655](/schnittstellen/202604/pruefi/UTILMD/PI_55655) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55656](/schnittstellen/202604/pruefi/UTILMD/PI_55656) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55657](/schnittstellen/202604/pruefi/UTILMD/PI_55657) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55658](/schnittstellen/202604/pruefi/UTILMD/PI_55658) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55659](/schnittstellen/202604/pruefi/UTILMD/PI_55659) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55660](/schnittstellen/202604/pruefi/UTILMD/PI_55660) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55661](/schnittstellen/202604/pruefi/UTILMD/PI_55661) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55662](/schnittstellen/202604/pruefi/UTILMD/PI_55662) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55663](/schnittstellen/202604/pruefi/UTILMD/PI_55663) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55664](/schnittstellen/202604/pruefi/UTILMD/PI_55664) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55665](/schnittstellen/202604/pruefi/UTILMD/PI_55665) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55666](/schnittstellen/202604/pruefi/UTILMD/PI_55666) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55667](/schnittstellen/202604/pruefi/UTILMD/PI_55667) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55669](/schnittstellen/202604/pruefi/UTILMD/PI_55669) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55670](/schnittstellen/202604/pruefi/UTILMD/PI_55670) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55672](/schnittstellen/202604/pruefi/UTILMD/PI_55672) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55673](/schnittstellen/202604/pruefi/UTILMD/PI_55673) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55674](/schnittstellen/202604/pruefi/UTILMD/PI_55674) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55684](/schnittstellen/202604/pruefi/UTILMD/PI_55684) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55686](/schnittstellen/202604/pruefi/UTILMD/PI_55686) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55688](/schnittstellen/202604/pruefi/UTILMD/PI_55688) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55690](/schnittstellen/202604/pruefi/UTILMD/PI_55690) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55691](/schnittstellen/202604/pruefi/UTILMD/PI_55691) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |
| [PI_55692](/schnittstellen/202604/pruefi/UTILMD/PI_55692) | Prüfi | UTILMD | stammdaten › VERWENDUNGSZEITRAUM |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
