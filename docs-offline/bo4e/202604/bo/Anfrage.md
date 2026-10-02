# Anfrage
<span hidden data-pagefind-meta={"title:Anfrage — BO4E-Geschäftsobjekt (FV 202604)"} />

BO4E-Geschäftsobjekt · 12 Felder · 77 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="botyp"></a>`boTyp` <span className="hbs-pflicht">\*</span> | [Enum BOTyp](/bo4e/202604/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> | Typ des BO |
| <a id="versionstruktur"></a>`versionStruktur` <span className="hbs-pflicht">\*</span> | string | versionStruktur |
| <a id="lokationstyp"></a>`lokationsTyp` | [Enum Lokationstyp](/bo4e/202604/enum/Lokationstyp)<br/><Werte>`MALO`, `MELO`, `NELO`, `TECHNISCHE_RESSOURCE`, `STEUERBARE_RESSOURCE`, `TRANCHE`, `MABIS_ZAEHLPUNKT`</Werte> | Gibt an, ob es sich um eine Markt- oder Messlokation handelt |
| <a id="lokationsid"></a>`lokationsId` | string | Für welche Markt- oder Messlokation gilt diese Anfrage. |
| <a id="anfragetyp"></a>`anfragetyp` | [Enum Anfragetyp](/bo4e/202604/enum/Anfragetyp)<br/><Werte>`KAUF`, `NUTZUNGSUEBERLASSUNG`, `ABRECHNUNGSBRENNWERT_UND_ZUSTANDSZAHL`, `LASTGANGDATEN`, `ZAEHLERSTAENDE`, `WERTEERMITTLUNG`, `ENERGIEMENGE_EINZELWERT`, `INNERHALB_DER_ARBEITSZEIT`, `AUCH_AUSSERHALB_DER_ARBEITSZEIT`, `WECHSEL_SAEMTLICHER_EINRICHTUNGEN`, `TEILWEISER_WECHSEL`, `AENDERUNG_ZAEHLZEITDEFINITION`, `ABBESTELLUNG_ZAEHLZEITEN`, `ABBESTELLUNG_MESSPRODUKT`, `ANGEBOT_AUF_BASIS_PREISBLATT`, `INDIVIDUELLES_ANGEBOT`, `AENDERUNG_KONFIGURATION`, `KANN_NICHT_ANGEBOTEN_WERDEN`, `NEUKONFIGURATION`, `BEENDIGUNG_KONFIGURATION`, `AKTIVIERUNG_KONFIGURATION`</Werte> | Typ/Art der Anfrage (ORDERS ORDRSP IMD 7081) |
| <a id="abonnement"></a>`abonnement` | [Enum Abonnement](/bo4e/202604/enum/Abonnement)<br/><Werte>`START_ABO`, `ENDE_ABO`, `OHNE_ABO`</Werte> | Start oder Ende Abo |
| <a id="anfragereferenz"></a>`anfragereferenz` | string | anfragereferenz |
| <a id="allgemeineinformationen"></a>`allgemeineInformationen` | string | allgemeineInformationen |
| <a id="anfragekategorie"></a>`anfragekategorie` | [Enum Anfragekategorie](/bo4e/202604/enum/Anfragekategorie)<br/><Werte>`PROZESSDATENBERICHT`, `GERAETEUEBERNAHME`, `WEITERVERPFLICHTUNG_BETRIEB_MELO`, `AENDERUNG_MELO`, `STAMMDATEN_MALO_ODER_MELO`, `BILANZIERTE_MENGE_MEHR_MINDER_MENGEN`, `ALLOKATIONSLISTE_MEHR_MINDER_MENGEN`, `ENERGIEMENGE_UND_LEISTUNGSMAXIMUM`, `ABRECHNUNG_MESSSTELLENBETRIEB_MSB_AN_LF`, `AENDERUNG_PROGNOSEGRUNDLAGE_GERAETEKONFIGURATION`, `AENDERUNG_GERAETEKONFIGURATION`, `REKLAMATION_VON_WERTEN`, `LASTGANG_MALO_TRANCHE`, `SPERRUNG`, `ENTSPERRUNG`, `REKLAMATION_ZAEHLZEITDEFINITION`, `ZEITREIHEN_IM_RAHMEN_BILANZKREISABRECHNUNG`, `GERAETEWECHSELABSICHT`, `AENDERUNG_KONZESSIONSABGABE`, `AENDERUNG_ZAEHLZEITDEFINITION`, `UEBERMITTLUNG_WERTE_AN_ESA`, `AENDERUNG`, `BILANZKREISZUORDNUNGSLISTE`, `CLEARINGLISTE`, `NORMIERTES_PROFIL_PROFILSCHAR`, `REDISPATCH_EINZELZEITREIHE_AUSFALLARBEIT`, `REKLAMATION_PROFIL_PROFILSCHAR`, `STAMMDATEN_MALO`, `STAMMDATEN_MELO`, `STAMMDATEN_TRANCHE`, `BEENDIGUNG_EINER_KONFIGURATION`, `BESTELLUNG_EINER_KONFIGURATION`, `BESTELLUNG_EINES_ANGEBOTS_EINER_KONFIGURATION`, `REKLAMATION_EINER_KONFIGURATION`, `BESTELLUNG_AENDERUNG_NETZENTGELTE_NETZORIENTIERTER_STEUERUNGSMOEGLICHKEIT`, `AENDERUNG_DER_TECHNIK_DER_LOKATION`, `AENDERUNG_INDIVIDUELLER_KONFIGURATION`, `BESTELLUNG_AENDERUNG_ABRECHNUNGSDATEN`, `EINRICHTUNG_KONFIGURATION_AUFGRUND_ZUORDNUNG_LF`, `REKLAMATION_DEFINITION`, `BESTELLUNG_ANGEBOT_AENDERUNG_TECHNIK_LOKATION`</Werte> | Kategorie der Anfrage (ORDERS ORDRSP BGM 1001) |
| <a id="energierichtung"></a>`energierichtung` | [Enum Energierichtung](/bo4e/202604/enum/Energierichtung)<br/><Werte>`AUSSP`, `EINSP`</Werte> | Spezifiziert die Energierichtung einer Markt- und/oder Messlokation |
| <a id="gueltigkeitszeitspanne"></a>`gueltigkeitszeitspanne` | string | gueltigkeitszeitspanne |
| <a id="gueltigab"></a>`gueltigAb` | string (date-time) | gueltigAb |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[boTyp](/bo4e/202604/bo/Anfrage#botyp) <span className="hbs-pflicht">\*</span></span> | Typ des BO | [Enum BOTyp](/bo4e/202604/enum/BOTyp)<br/><Werte>`ANSPRECHPARTNER`, `AVIS`, `ENERGIEMENGE`, `GESCHAEFTSOBJEKT`, `GESCHAEFTSPARTNER`, `MARKTLOKATION`, `MARKTTEILNEHMER`, `MESSLOKATION`, `ZAEHLER`, `KOSTEN`, `TARIF`, `PREISBLATT`, `PREISBLATTNETZNUTZUNG`, `PREISBLATTMESSUNG`, `PREISBLATTUMLAGEN`, `PREISBLATTDIENSTLEISTUNG`, `PREISBLATTKONZESSIONSABGABE`, `ZEITREIHE`, `LASTGANG`, `HANDELSUNSTIMMIGKEIT`, `ANFRAGE`, `AUFTRAG`, `STATUSMITTEILUNG`, `BERECHNUNGSFORMEL`, `RECHNUNG`, `BILANZIERUNG`, `NETZNUTZUNGSVERTRAG`, `MESSSTELLENBETRIEBSVERTRAG`, `ENERGIELIEFERVERTRAG`, `SPERRAUFTRAG`, `ANGEBOT`, `TRANCHE`, `KOMMUNIKATIONSDATEN`, `ZAEHLZEITDEFINITION`, `SCHALTZEITDEFINITION`, `LEISTUNGSKURVENDEFINITION`, `NETZLOKATION`, `STEUERBARE_RESSOURCE`, `TECHNISCHE_RESSOURCE`, `AD_HOC_STEUERKANAL`, `LOKATIONSBUENDEL`, `WERTE_NACH_TYP2`, `REKLAMATION`, `STATUSBERICHT`, `VERTRAG`, `BILANZKREIS`, `VERWENDUNGSZEITRAUM`, `TARIFINFO`, `SUMMENZEITREIHE`</Werte> |
| <span className="hbs-f hbs-e0">[versionStruktur](/bo4e/202604/bo/Anfrage#versionstruktur) <span className="hbs-pflicht">\*</span></span> | versionStruktur | string |
| <span className="hbs-f hbs-e0">[lokationsTyp](/bo4e/202604/bo/Anfrage#lokationstyp)</span> | Gibt an, ob es sich um eine Markt- oder Messlokation handelt | [Enum Lokationstyp](/bo4e/202604/enum/Lokationstyp)<br/><Werte>`MALO`, `MELO`, `NELO`, `TECHNISCHE_RESSOURCE`, `STEUERBARE_RESSOURCE`, `TRANCHE`, `MABIS_ZAEHLPUNKT`</Werte> |
| <span className="hbs-f hbs-e0">[lokationsId](/bo4e/202604/bo/Anfrage#lokationsid)</span> | Für welche Markt- oder Messlokation gilt diese Anfrage. | string |
| <span className="hbs-f hbs-e0">[anfragetyp](/bo4e/202604/bo/Anfrage#anfragetyp)</span> | Typ/Art der Anfrage (ORDERS ORDRSP IMD 7081) | [Enum Anfragetyp](/bo4e/202604/enum/Anfragetyp)<br/><Werte>`KAUF`, `NUTZUNGSUEBERLASSUNG`, `ABRECHNUNGSBRENNWERT_UND_ZUSTANDSZAHL`, `LASTGANGDATEN`, `ZAEHLERSTAENDE`, `WERTEERMITTLUNG`, `ENERGIEMENGE_EINZELWERT`, `INNERHALB_DER_ARBEITSZEIT`, `AUCH_AUSSERHALB_DER_ARBEITSZEIT`, `WECHSEL_SAEMTLICHER_EINRICHTUNGEN`, `TEILWEISER_WECHSEL`, `AENDERUNG_ZAEHLZEITDEFINITION`, `ABBESTELLUNG_ZAEHLZEITEN`, `ABBESTELLUNG_MESSPRODUKT`, `ANGEBOT_AUF_BASIS_PREISBLATT`, `INDIVIDUELLES_ANGEBOT`, `AENDERUNG_KONFIGURATION`, `KANN_NICHT_ANGEBOTEN_WERDEN`, `NEUKONFIGURATION`, `BEENDIGUNG_KONFIGURATION`, `AKTIVIERUNG_KONFIGURATION`</Werte> |
| <span className="hbs-f hbs-e0">[abonnement](/bo4e/202604/bo/Anfrage#abonnement)</span> | Start oder Ende Abo | [Enum Abonnement](/bo4e/202604/enum/Abonnement)<br/><Werte>`START_ABO`, `ENDE_ABO`, `OHNE_ABO`</Werte> |
| <span className="hbs-f hbs-e0">[anfragereferenz](/bo4e/202604/bo/Anfrage#anfragereferenz)</span> | anfragereferenz | string |
| <span className="hbs-f hbs-e0">[allgemeineInformationen](/bo4e/202604/bo/Anfrage#allgemeineinformationen)</span> | allgemeineInformationen | string |
| <span className="hbs-f hbs-e0">[anfragekategorie](/bo4e/202604/bo/Anfrage#anfragekategorie)</span> | Kategorie der Anfrage (ORDERS ORDRSP BGM 1001) | [Enum Anfragekategorie](/bo4e/202604/enum/Anfragekategorie)<br/><Werte>`PROZESSDATENBERICHT`, `GERAETEUEBERNAHME`, `WEITERVERPFLICHTUNG_BETRIEB_MELO`, `AENDERUNG_MELO`, `STAMMDATEN_MALO_ODER_MELO`, `BILANZIERTE_MENGE_MEHR_MINDER_MENGEN`, `ALLOKATIONSLISTE_MEHR_MINDER_MENGEN`, `ENERGIEMENGE_UND_LEISTUNGSMAXIMUM`, `ABRECHNUNG_MESSSTELLENBETRIEB_MSB_AN_LF`, `AENDERUNG_PROGNOSEGRUNDLAGE_GERAETEKONFIGURATION`, `AENDERUNG_GERAETEKONFIGURATION`, `REKLAMATION_VON_WERTEN`, `LASTGANG_MALO_TRANCHE`, `SPERRUNG`, `ENTSPERRUNG`, `REKLAMATION_ZAEHLZEITDEFINITION`, `ZEITREIHEN_IM_RAHMEN_BILANZKREISABRECHNUNG`, `GERAETEWECHSELABSICHT`, `AENDERUNG_KONZESSIONSABGABE`, `AENDERUNG_ZAEHLZEITDEFINITION`, `UEBERMITTLUNG_WERTE_AN_ESA`, `AENDERUNG`, `BILANZKREISZUORDNUNGSLISTE`, `CLEARINGLISTE`, `NORMIERTES_PROFIL_PROFILSCHAR`, `REDISPATCH_EINZELZEITREIHE_AUSFALLARBEIT`, `REKLAMATION_PROFIL_PROFILSCHAR`, `STAMMDATEN_MALO`, `STAMMDATEN_MELO`, `STAMMDATEN_TRANCHE`, `BEENDIGUNG_EINER_KONFIGURATION`, `BESTELLUNG_EINER_KONFIGURATION`, `BESTELLUNG_EINES_ANGEBOTS_EINER_KONFIGURATION`, `REKLAMATION_EINER_KONFIGURATION`, `BESTELLUNG_AENDERUNG_NETZENTGELTE_NETZORIENTIERTER_STEUERUNGSMOEGLICHKEIT`, `AENDERUNG_DER_TECHNIK_DER_LOKATION`, `AENDERUNG_INDIVIDUELLER_KONFIGURATION`, `BESTELLUNG_AENDERUNG_ABRECHNUNGSDATEN`, `EINRICHTUNG_KONFIGURATION_AUFGRUND_ZUORDNUNG_LF`, `REKLAMATION_DEFINITION`, `BESTELLUNG_ANGEBOT_AENDERUNG_TECHNIK_LOKATION`</Werte> |
| <span className="hbs-f hbs-e0">[energierichtung](/bo4e/202604/bo/Anfrage#energierichtung)</span> | Spezifiziert die Energierichtung einer Markt- und/oder Messlokation | [Enum Energierichtung](/bo4e/202604/enum/Energierichtung)<br/><Werte>`AUSSP`, `EINSP`</Werte> |
| <span className="hbs-f hbs-e0">[gueltigkeitszeitspanne](/bo4e/202604/bo/Anfrage#gueltigkeitszeitspanne)</span> | gueltigkeitszeitspanne | string |
| <span className="hbs-f hbs-e0">[gueltigAb](/bo4e/202604/bo/Anfrage#gueltigab)</span> | gueltigAb | string (date-time) |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### lokationsId

23 Verwendung(en) in den Nachrichtentypen ORDERS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_17002](/schnittstellen/202604/pruefi/ORDERS/PI_17002) | Prüfi | ORDERS | stammdaten › ANFRAGE |
| [PI_17003](/schnittstellen/202604/pruefi/ORDERS/PI_17003) | Prüfi | ORDERS | stammdaten › ANFRAGE |
| [PI_17004](/schnittstellen/202604/pruefi/ORDERS/PI_17004) | Prüfi | ORDERS | stammdaten › ANFRAGE |
| [PI_17005](/schnittstellen/202604/pruefi/ORDERS/PI_17005) | Prüfi | ORDERS | stammdaten › ANFRAGE |
| [PI_17006](/schnittstellen/202604/pruefi/ORDERS/PI_17006) | Prüfi | ORDERS | stammdaten › ANFRAGE |
| [PI_17009](/schnittstellen/202604/pruefi/ORDERS/PI_17009) | Prüfi | ORDERS | stammdaten › ANFRAGE |
| [PI_17101](/schnittstellen/202604/pruefi/ORDERS/PI_17101) | Prüfi | ORDERS | stammdaten › ANFRAGE |
| [PI_17102](/schnittstellen/202604/pruefi/ORDERS/PI_17102) | Prüfi | ORDERS | stammdaten › ANFRAGE |
| [PI_17103](/schnittstellen/202604/pruefi/ORDERS/PI_17103) | Prüfi | ORDERS | stammdaten › ANFRAGE |
| [PI_17104](/schnittstellen/202604/pruefi/ORDERS/PI_17104) | Prüfi | ORDERS | stammdaten › ANFRAGE |
| [PI_17115](/schnittstellen/202604/pruefi/ORDERS/PI_17115) | Prüfi | ORDERS | stammdaten › ANFRAGE |
| [PI_17116](/schnittstellen/202604/pruefi/ORDERS/PI_17116) | Prüfi | ORDERS | stammdaten › ANFRAGE |
| [PI_17117](/schnittstellen/202604/pruefi/ORDERS/PI_17117) | Prüfi | ORDERS | stammdaten › ANFRAGE |
| [PI_17118](/schnittstellen/202604/pruefi/ORDERS/PI_17118) | Prüfi | ORDERS | stammdaten › ANFRAGE |
| [PI_17120](/schnittstellen/202604/pruefi/ORDERS/PI_17120) | Prüfi | ORDERS | stammdaten › ANFRAGE |
| [PI_17121](/schnittstellen/202604/pruefi/ORDERS/PI_17121) | Prüfi | ORDERS | stammdaten › ANFRAGE |
| [PI_17123](/schnittstellen/202604/pruefi/ORDERS/PI_17123) | Prüfi | ORDERS | stammdaten › ANFRAGE |
| [PI_17126](/schnittstellen/202604/pruefi/ORDERS/PI_17126) | Prüfi | ORDERS | stammdaten › ANFRAGE |
| [PI_17130](/schnittstellen/202604/pruefi/ORDERS/PI_17130) | Prüfi | ORDERS | stammdaten › ANFRAGE |
| [PI_17132](/schnittstellen/202604/pruefi/ORDERS/PI_17132) | Prüfi | ORDERS | stammdaten › ANFRAGE |
| [PI_17133](/schnittstellen/202604/pruefi/ORDERS/PI_17133) | Prüfi | ORDERS | stammdaten › ANFRAGE |
| [PI_17134](/schnittstellen/202604/pruefi/ORDERS/PI_17134) | Prüfi | ORDERS | stammdaten › ANFRAGE |
| [PI_17135](/schnittstellen/202604/pruefi/ORDERS/PI_17135) | Prüfi | ORDERS | stammdaten › ANFRAGE |

### anfragetyp

19 Verwendung(en) in den Nachrichtentypen ORDERS, ORDRSP, QUOTES, REQOTE.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_15001](/schnittstellen/202604/pruefi/QUOTES/PI_15001) | Prüfi | QUOTES | stammdaten › ANFRAGE |
| [PI_15004](/schnittstellen/202604/pruefi/QUOTES/PI_15004) | Prüfi | QUOTES | stammdaten › ANFRAGE |
| [PI_17004](/schnittstellen/202604/pruefi/ORDERS/PI_17004) | Prüfi | ORDERS | stammdaten › ANFRAGE |
| [PI_17009](/schnittstellen/202604/pruefi/ORDERS/PI_17009) | Prüfi | ORDERS | stammdaten › ANFRAGE |
| [PI_17102](/schnittstellen/202604/pruefi/ORDERS/PI_17102) | Prüfi | ORDERS | stammdaten › ANFRAGE |
| [PI_17103](/schnittstellen/202604/pruefi/ORDERS/PI_17103) | Prüfi | ORDERS | stammdaten › ANFRAGE |
| [PI_17113](/schnittstellen/202604/pruefi/ORDERS/PI_17113) | Prüfi | ORDERS | stammdaten › ANFRAGE |
| [PI_17117](/schnittstellen/202604/pruefi/ORDERS/PI_17117) | Prüfi | ORDERS | stammdaten › ANFRAGE |
| [PI_17118](/schnittstellen/202604/pruefi/ORDERS/PI_17118) | Prüfi | ORDERS | stammdaten › ANFRAGE |
| [PI_17123](/schnittstellen/202604/pruefi/ORDERS/PI_17123) | Prüfi | ORDERS | stammdaten › ANFRAGE |
| [PI_17134](/schnittstellen/202604/pruefi/ORDERS/PI_17134) | Prüfi | ORDERS | stammdaten › ANFRAGE |
| [PI_17135](/schnittstellen/202604/pruefi/ORDERS/PI_17135) | Prüfi | ORDERS | stammdaten › ANFRAGE |
| [PI_19007](/schnittstellen/202604/pruefi/ORDRSP/PI_19007) | Prüfi | ORDRSP | stammdaten › ANFRAGE |
| [PI_19102](/schnittstellen/202604/pruefi/ORDRSP/PI_19102) | Prüfi | ORDRSP | stammdaten › ANFRAGE |
| [PI_19103](/schnittstellen/202604/pruefi/ORDRSP/PI_19103) | Prüfi | ORDRSP | stammdaten › ANFRAGE |
| [PI_19114](/schnittstellen/202604/pruefi/ORDRSP/PI_19114) | Prüfi | ORDRSP | stammdaten › ANFRAGE |
| [PI_19301](/schnittstellen/202604/pruefi/ORDRSP/PI_19301) | Prüfi | ORDRSP | stammdaten › ANFRAGE |
| [PI_19302](/schnittstellen/202604/pruefi/ORDRSP/PI_19302) | Prüfi | ORDRSP | stammdaten › ANFRAGE |
| [PI_35004](/schnittstellen/202604/pruefi/REQOTE/PI_35004) | Prüfi | REQOTE | stammdaten › ANFRAGE |

### abonnement

8 Verwendung(en) in den Nachrichtentypen ORDERS, ORDRSP.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_17005](/schnittstellen/202604/pruefi/ORDERS/PI_17005) | Prüfi | ORDERS | stammdaten › ANFRAGE |
| [PI_17006](/schnittstellen/202604/pruefi/ORDERS/PI_17006) | Prüfi | ORDERS | stammdaten › ANFRAGE |
| [PI_19009](/schnittstellen/202604/pruefi/ORDRSP/PI_19009) | Prüfi | ORDRSP | stammdaten › ANFRAGE |
| [PI_19010](/schnittstellen/202604/pruefi/ORDRSP/PI_19010) | Prüfi | ORDRSP | stammdaten › ANFRAGE |
| [PI_19011](/schnittstellen/202604/pruefi/ORDRSP/PI_19011) | Prüfi | ORDRSP | stammdaten › ANFRAGE |
| [PI_19012](/schnittstellen/202604/pruefi/ORDRSP/PI_19012) | Prüfi | ORDRSP | stammdaten › ANFRAGE |
| [PI_19301](/schnittstellen/202604/pruefi/ORDRSP/PI_19301) | Prüfi | ORDRSP | stammdaten › ANFRAGE |
| [PI_19302](/schnittstellen/202604/pruefi/ORDRSP/PI_19302) | Prüfi | ORDRSP | stammdaten › ANFRAGE |

### anfragekategorie

23 Verwendung(en) in den Nachrichtentypen ORDCHG, ORDERS, ORDRSP.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_17102](/schnittstellen/202604/pruefi/ORDERS/PI_17102) | Prüfi | ORDERS | stammdaten › ANFRAGE |
| [PI_17103](/schnittstellen/202604/pruefi/ORDERS/PI_17103) | Prüfi | ORDERS | stammdaten › ANFRAGE |
| [PI_19005](/schnittstellen/202604/pruefi/ORDRSP/PI_19005) | Prüfi | ORDRSP | stammdaten › ANFRAGE |
| [PI_19006](/schnittstellen/202604/pruefi/ORDRSP/PI_19006) | Prüfi | ORDRSP | stammdaten › ANFRAGE |
| [PI_19007](/schnittstellen/202604/pruefi/ORDRSP/PI_19007) | Prüfi | ORDRSP | stammdaten › ANFRAGE |
| [PI_19009](/schnittstellen/202604/pruefi/ORDRSP/PI_19009) | Prüfi | ORDRSP | stammdaten › ANFRAGE |
| [PI_19010](/schnittstellen/202604/pruefi/ORDRSP/PI_19010) | Prüfi | ORDRSP | stammdaten › ANFRAGE |
| [PI_19011](/schnittstellen/202604/pruefi/ORDRSP/PI_19011) | Prüfi | ORDRSP | stammdaten › ANFRAGE |
| [PI_19012](/schnittstellen/202604/pruefi/ORDRSP/PI_19012) | Prüfi | ORDRSP | stammdaten › ANFRAGE |
| [PI_19013](/schnittstellen/202604/pruefi/ORDRSP/PI_19013) | Prüfi | ORDRSP | stammdaten › ANFRAGE |
| [PI_19014](/schnittstellen/202604/pruefi/ORDRSP/PI_19014) | Prüfi | ORDRSP | stammdaten › ANFRAGE |
| [PI_19101](/schnittstellen/202604/pruefi/ORDRSP/PI_19101) | Prüfi | ORDRSP | stammdaten › ANFRAGE |
| [PI_19102](/schnittstellen/202604/pruefi/ORDRSP/PI_19102) | Prüfi | ORDRSP | stammdaten › ANFRAGE |
| [PI_19116](/schnittstellen/202604/pruefi/ORDRSP/PI_19116) | Prüfi | ORDRSP | stammdaten › ANFRAGE |
| [PI_19117](/schnittstellen/202604/pruefi/ORDRSP/PI_19117) | Prüfi | ORDRSP | stammdaten › ANFRAGE |
| [PI_19118](/schnittstellen/202604/pruefi/ORDRSP/PI_19118) | Prüfi | ORDRSP | stammdaten › ANFRAGE |
| [PI_19119](/schnittstellen/202604/pruefi/ORDRSP/PI_19119) | Prüfi | ORDRSP | stammdaten › ANFRAGE |
| [PI_19128](/schnittstellen/202604/pruefi/ORDRSP/PI_19128) | Prüfi | ORDRSP | stammdaten › ANFRAGE |
| [PI_19129](/schnittstellen/202604/pruefi/ORDRSP/PI_19129) | Prüfi | ORDRSP | stammdaten › ANFRAGE |
| [PI_19301](/schnittstellen/202604/pruefi/ORDRSP/PI_19301) | Prüfi | ORDRSP | stammdaten › ANFRAGE |
| [PI_19302](/schnittstellen/202604/pruefi/ORDRSP/PI_19302) | Prüfi | ORDRSP | stammdaten › ANFRAGE |
| [PI_39000](/schnittstellen/202604/pruefi/ORDCHG/PI_39000) | Prüfi | ORDCHG | stammdaten › ANFRAGE |
| [PI_39001](/schnittstellen/202604/pruefi/ORDCHG/PI_39001) | Prüfi | ORDCHG | stammdaten › ANFRAGE |

### energierichtung

2 Verwendung(en) in den Nachrichtentypen ORDERS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_17121](/schnittstellen/202604/pruefi/ORDERS/PI_17121) | Prüfi | ORDERS | stammdaten › ANFRAGE |
| [PI_17134](/schnittstellen/202604/pruefi/ORDERS/PI_17134) | Prüfi | ORDERS | stammdaten › ANFRAGE |

### gueltigAb

2 Verwendung(en) in den Nachrichtentypen ORDERS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_17004](/schnittstellen/202604/pruefi/ORDERS/PI_17004) | Prüfi | ORDERS | stammdaten › ANFRAGE |
| [PI_17113](/schnittstellen/202604/pruefi/ORDERS/PI_17113) | Prüfi | ORDERS | stammdaten › ANFRAGE |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
