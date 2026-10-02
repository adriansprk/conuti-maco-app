# Vertragskonditionen
<span hidden data-pagefind-meta={"title:Vertragskonditionen — BO4E-Komponente (FV 202604)"} />

BO4E-Komponente · 22 Felder · 89 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="netznutzungszahler"></a>`netznutzungszahler` | [Enum Netznutzungszahler](/bo4e/202604/enum/Netznutzungszahler)<br/><Werte>`KUNDE`, `LIEFERANT`</Werte> | Netznutzungszahler |
| <a id="netznutzungsvertrag"></a>`netznutzungsvertrag` | [Enum Netznutzungsvertrag](/bo4e/202604/enum/Netznutzungsvertrag)<br/><Werte>`KUNDEN_NB`, `LIEFERANTEN_NB`</Werte> | Netznutzungsvertrag |
| <a id="netznutzungsabrechnung"></a>`netznutzungsabrechnung` | [Zeitraum](/bo4e/202604/com/Zeitraum) | — |
| <a id="beinhaltetsingulaergenutztebetriebsmittel"></a>`beinhaltetSingulaerGenutzteBetriebsmittel` | boolean | Singulär genutzte Betriebsmittel in der Netznutzungsabrechnung Hier wird angegeben, ob in der Netznutzungsabrechnung der verbrauchenden Marktlokation singulär  genutzte Betriebsmittel abgerechnet werden. |
| <a id="netznutzungsabrechnungsgrundlage"></a>`netznutzungsabrechnungsgrundlage` | [Enum Netznutzungsabrechnungsgrundlage](/bo4e/202604/enum/Netznutzungsabrechnungsgrundlage)<br/><Werte>`LIEFERSCHEIN`, `ABWEICHENDE_GRUNDLAGE`</Werte> | Netznutzungsabrechnungsgrundlage |
| <a id="netznutzungsabrechnungsvariante"></a>`netznutzungsabrechnungsvariante` | [Enum Netznutzungsabrechnungsvariante](/bo4e/202604/enum/Netznutzungsabrechnungsvariante)<br/><Werte>`ARBEITSPREIS_GRUNDPREIS`, `ARBEITSPREIS_LEISTUNGSPREIS`</Werte> | Netznutzungsabrechnungsvariante |
| <a id="haushaltskunde"></a>`haushaltskunde` | boolean | haushaltskunde |
| <a id="abrechnunguebernna"></a>`abrechnungUeberNna` | boolean | abrechnungUeberNna |
| <a id="gemeinderabatt"></a>`gemeinderabatt` | [Gemeinderabatt](/bo4e/202604/com/Gemeinderabatt) | — |
| <a id="startabrechnungsjahr"></a>`startAbrechnungsjahr` | string (date-time) | startAbrechnungsjahr |
| <a id="naechstenetznutzungsabrechnung"></a>`naechstenetznutzungsabrechnung` | string | naechstenetznutzungsabrechnung |
| <a id="abrechnungsintervall"></a>`abrechnungsintervall` | integer | abrechnungsintervall |
| <a id="netznutzungsabrechnungintervall"></a>`netznutzungsabrechnungIntervall` | integer | netznutzungsabrechnungIntervall |
| <a id="geplanteturnusablesung"></a>`geplanteTurnusablesung` | [Zeitraum](/bo4e/202604/com/Zeitraum) | — |
| <a id="beauftragungmsb"></a>`beauftragungMsb` | [Enum BeauftragungMsb](/bo4e/202604/enum/BeauftragungMsb)<br/><Werte>`VERTRAG_AN_MSB`, `VERTRAGSBEENDIGUNG_MSB`</Werte> | BeauftragungMsb |
| <a id="kuendigungsfrist"></a>`kuendigungsfrist` | [Zeitraum](/bo4e/202604/com/Zeitraum) | Innerhalb dieser Frist kann der Vertrag gekündigt werden. Details Zeitraum |
| <a id="vertragslaufzeit"></a>`vertragslaufzeit` | [Zeitraum](/bo4e/202604/com/Zeitraum) | Über diesen Zeitraum läuft der Vertrag. Details Zeitraum |
| <a id="kuendigungstermin"></a>`kuendigungstermin` | string | kuendigungstermin |
| <a id="abschlagszyklus"></a>`abschlagszyklus` | [Zeitraum](/bo4e/202604/com/Zeitraum) | In diesen Zyklen werden Abschläge gestellt. Details Zeitraum. Alternativ kann auch die Anzahl in den Konditionen angeben werden." |
| <a id="anzahl_abschlaege"></a>`anzahl_abschlaege` | number (float) | Anzahl der vereinbarten Abschläge pro Jahr, z.B. 12 |
| <a id="beschreibung"></a>`beschreibung` | string | Freitext zur Beschreibung der Konditionen, z.B. "Standardkonditionen Gas" |
| <a id="vertragsverlaengerung"></a>`vertragsverlaengerung` | [Zeitraum](/bo4e/202604/com/Zeitraum) | Falls der Vertrag nicht gekündigt wird, verlängert er sich automatisch um die hier angegebene Zeit. Details Zeitraum |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[netznutzungszahler](/bo4e/202604/com/Vertragskonditionen#netznutzungszahler)</span> | Netznutzungszahler | [Enum Netznutzungszahler](/bo4e/202604/enum/Netznutzungszahler)<br/><Werte>`KUNDE`, `LIEFERANT`</Werte> |
| <span className="hbs-f hbs-e0">[netznutzungsvertrag](/bo4e/202604/com/Vertragskonditionen#netznutzungsvertrag)</span> | Netznutzungsvertrag | [Enum Netznutzungsvertrag](/bo4e/202604/enum/Netznutzungsvertrag)<br/><Werte>`KUNDEN_NB`, `LIEFERANTEN_NB`</Werte> |
| <span className="hbs-g hbs-e0">[netznutzungsabrechnung](/bo4e/202604/com/Vertragskonditionen#netznutzungsabrechnung)</span> | — | [Zeitraum](/bo4e/202604/com/Zeitraum) |
| <span className="hbs-f hbs-e1">[zeiteinheit](/bo4e/202604/com/Zeitraum#zeiteinheit)</span> | Zeiteinheit | [Enum Zeiteinheit](/bo4e/202604/enum/Zeiteinheit)<br/><Werte>`SEKUNDE`, `MINUTE`, `STUNDE`, `VIERTEL_STUNDE`, `TAG`, `WOCHE`, `MONAT`, `QUARTAL`, `HALBJAHR`, `JAHR`</Werte> |
| <span className="hbs-f hbs-e1">[dauer](/bo4e/202604/com/Zeitraum#dauer)</span> | dauer | integer |
| <span className="hbs-f hbs-e1">[startdatum](/bo4e/202604/com/Zeitraum#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e1">[enddatum](/bo4e/202604/com/Zeitraum#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-f hbs-e1">[einheit](/bo4e/202604/com/Zeitraum#einheit)</span> | Zeiteinheit | [Enum Zeiteinheit](/bo4e/202604/enum/Zeiteinheit)<br/><Werte>`SEKUNDE`, `MINUTE`, `STUNDE`, `VIERTEL_STUNDE`, `TAG`, `WOCHE`, `MONAT`, `QUARTAL`, `HALBJAHR`, `JAHR`</Werte> |
| <span className="hbs-f hbs-e1">[ableseZeitraum](/bo4e/202604/com/Zeitraum#ablesezeitraum)</span> | ableseZeitraum | string |
| <span className="hbs-f hbs-e1">[abrechnungsZeitraum](/bo4e/202604/com/Zeitraum#abrechnungszeitraum)</span> | abrechnungsZeitraum | string |
| <span className="hbs-f hbs-e1">[zeitraumText](/bo4e/202604/com/Zeitraum#zeitraumtext)</span> | zeitraumText | string |
| <span className="hbs-f hbs-e1">[zeitraumId](/bo4e/202604/com/Zeitraum#zeitraumid)</span> | zeitraumId | integer |
| <span className="hbs-f hbs-e0">[beinhaltetSingulaerGenutzteBetriebsmittel](/bo4e/202604/com/Vertragskonditionen#beinhaltetsingulaergenutztebetriebsmittel)</span> | Singulär genutzte Betriebsmittel in der Netznutzungsabrechnung<br/>Hier wird angegeben, ob in der Netznutzungsabrechnung der verbrauchenden Marktlokation singulär<br/>genutzte Betriebsmittel abgerechnet werden. | boolean |
| <span className="hbs-f hbs-e0">[netznutzungsabrechnungsgrundlage](/bo4e/202604/com/Vertragskonditionen#netznutzungsabrechnungsgrundlage)</span> | Netznutzungsabrechnungsgrundlage | [Enum Netznutzungsabrechnungsgrundlage](/bo4e/202604/enum/Netznutzungsabrechnungsgrundlage)<br/><Werte>`LIEFERSCHEIN`, `ABWEICHENDE_GRUNDLAGE`</Werte> |
| <span className="hbs-f hbs-e0">[netznutzungsabrechnungsvariante](/bo4e/202604/com/Vertragskonditionen#netznutzungsabrechnungsvariante)</span> | Netznutzungsabrechnungsvariante | [Enum Netznutzungsabrechnungsvariante](/bo4e/202604/enum/Netznutzungsabrechnungsvariante)<br/><Werte>`ARBEITSPREIS_GRUNDPREIS`, `ARBEITSPREIS_LEISTUNGSPREIS`</Werte> |
| <span className="hbs-f hbs-e0">[haushaltskunde](/bo4e/202604/com/Vertragskonditionen#haushaltskunde)</span> | haushaltskunde | boolean |
| <span className="hbs-f hbs-e0">[abrechnungUeberNna](/bo4e/202604/com/Vertragskonditionen#abrechnunguebernna)</span> | abrechnungUeberNna | boolean |
| <span className="hbs-g hbs-e0">[gemeinderabatt](/bo4e/202604/com/Vertragskonditionen#gemeinderabatt)</span> | — | [Gemeinderabatt](/bo4e/202604/com/Gemeinderabatt) |
| <span className="hbs-f hbs-e1">[wert](/bo4e/202604/com/Gemeinderabatt#wert)</span> | Wert | number (float) |
| <span className="hbs-f hbs-e1">[einheit](/bo4e/202604/com/Gemeinderabatt#einheit)</span> | Einheit | string |
| <span className="hbs-f hbs-e1">[typ](/bo4e/202604/com/Gemeinderabatt#typ)</span> | Typ | string |
| <span className="hbs-f hbs-e1">[bemessungsgrundlage](/bo4e/202604/com/Gemeinderabatt#bemessungsgrundlage)</span> | Bemessungsgrundlage | number (float) |
| <span className="hbs-f hbs-e0">[startAbrechnungsjahr](/bo4e/202604/com/Vertragskonditionen#startabrechnungsjahr)</span> | startAbrechnungsjahr | string (date-time) |
| <span className="hbs-f hbs-e0">[naechstenetznutzungsabrechnung](/bo4e/202604/com/Vertragskonditionen#naechstenetznutzungsabrechnung)</span> | naechstenetznutzungsabrechnung | string |
| <span className="hbs-f hbs-e0">[abrechnungsintervall](/bo4e/202604/com/Vertragskonditionen#abrechnungsintervall)</span> | abrechnungsintervall | integer |
| <span className="hbs-f hbs-e0">[netznutzungsabrechnungIntervall](/bo4e/202604/com/Vertragskonditionen#netznutzungsabrechnungintervall)</span> | netznutzungsabrechnungIntervall | integer |
| <span className="hbs-g hbs-e0">[geplanteTurnusablesung](/bo4e/202604/com/Vertragskonditionen#geplanteturnusablesung)</span> | — | [Zeitraum](/bo4e/202604/com/Zeitraum) |
| <span className="hbs-f hbs-e1">[zeiteinheit](/bo4e/202604/com/Zeitraum#zeiteinheit)</span> | Zeiteinheit | [Enum Zeiteinheit](/bo4e/202604/enum/Zeiteinheit)<br/><Werte>`SEKUNDE`, `MINUTE`, `STUNDE`, `VIERTEL_STUNDE`, `TAG`, `WOCHE`, `MONAT`, `QUARTAL`, `HALBJAHR`, `JAHR`</Werte> |
| <span className="hbs-f hbs-e1">[dauer](/bo4e/202604/com/Zeitraum#dauer)</span> | dauer | integer |
| <span className="hbs-f hbs-e1">[startdatum](/bo4e/202604/com/Zeitraum#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e1">[enddatum](/bo4e/202604/com/Zeitraum#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-f hbs-e1">[einheit](/bo4e/202604/com/Zeitraum#einheit)</span> | Zeiteinheit | [Enum Zeiteinheit](/bo4e/202604/enum/Zeiteinheit)<br/><Werte>`SEKUNDE`, `MINUTE`, `STUNDE`, `VIERTEL_STUNDE`, `TAG`, `WOCHE`, `MONAT`, `QUARTAL`, `HALBJAHR`, `JAHR`</Werte> |
| <span className="hbs-f hbs-e1">[ableseZeitraum](/bo4e/202604/com/Zeitraum#ablesezeitraum)</span> | ableseZeitraum | string |
| <span className="hbs-f hbs-e1">[abrechnungsZeitraum](/bo4e/202604/com/Zeitraum#abrechnungszeitraum)</span> | abrechnungsZeitraum | string |
| <span className="hbs-f hbs-e1">[zeitraumText](/bo4e/202604/com/Zeitraum#zeitraumtext)</span> | zeitraumText | string |
| <span className="hbs-f hbs-e1">[zeitraumId](/bo4e/202604/com/Zeitraum#zeitraumid)</span> | zeitraumId | integer |
| <span className="hbs-f hbs-e0">[beauftragungMsb](/bo4e/202604/com/Vertragskonditionen#beauftragungmsb)</span> | BeauftragungMsb | [Enum BeauftragungMsb](/bo4e/202604/enum/BeauftragungMsb)<br/><Werte>`VERTRAG_AN_MSB`, `VERTRAGSBEENDIGUNG_MSB`</Werte> |
| <span className="hbs-g hbs-e0">[kuendigungsfrist](/bo4e/202604/com/Vertragskonditionen#kuendigungsfrist)</span> | Innerhalb dieser Frist kann der Vertrag gekündigt werden. Details Zeitraum | [Zeitraum](/bo4e/202604/com/Zeitraum) |
| <span className="hbs-f hbs-e1">[zeiteinheit](/bo4e/202604/com/Zeitraum#zeiteinheit)</span> | Zeiteinheit | [Enum Zeiteinheit](/bo4e/202604/enum/Zeiteinheit)<br/><Werte>`SEKUNDE`, `MINUTE`, `STUNDE`, `VIERTEL_STUNDE`, `TAG`, `WOCHE`, `MONAT`, `QUARTAL`, `HALBJAHR`, `JAHR`</Werte> |
| <span className="hbs-f hbs-e1">[dauer](/bo4e/202604/com/Zeitraum#dauer)</span> | dauer | integer |
| <span className="hbs-f hbs-e1">[startdatum](/bo4e/202604/com/Zeitraum#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e1">[enddatum](/bo4e/202604/com/Zeitraum#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-f hbs-e1">[einheit](/bo4e/202604/com/Zeitraum#einheit)</span> | Zeiteinheit | [Enum Zeiteinheit](/bo4e/202604/enum/Zeiteinheit)<br/><Werte>`SEKUNDE`, `MINUTE`, `STUNDE`, `VIERTEL_STUNDE`, `TAG`, `WOCHE`, `MONAT`, `QUARTAL`, `HALBJAHR`, `JAHR`</Werte> |
| <span className="hbs-f hbs-e1">[ableseZeitraum](/bo4e/202604/com/Zeitraum#ablesezeitraum)</span> | ableseZeitraum | string |
| <span className="hbs-f hbs-e1">[abrechnungsZeitraum](/bo4e/202604/com/Zeitraum#abrechnungszeitraum)</span> | abrechnungsZeitraum | string |
| <span className="hbs-f hbs-e1">[zeitraumText](/bo4e/202604/com/Zeitraum#zeitraumtext)</span> | zeitraumText | string |
| <span className="hbs-f hbs-e1">[zeitraumId](/bo4e/202604/com/Zeitraum#zeitraumid)</span> | zeitraumId | integer |
| <span className="hbs-g hbs-e0">[vertragslaufzeit](/bo4e/202604/com/Vertragskonditionen#vertragslaufzeit)</span> | Über diesen Zeitraum läuft der Vertrag. Details Zeitraum | [Zeitraum](/bo4e/202604/com/Zeitraum) |
| <span className="hbs-f hbs-e1">[zeiteinheit](/bo4e/202604/com/Zeitraum#zeiteinheit)</span> | Zeiteinheit | [Enum Zeiteinheit](/bo4e/202604/enum/Zeiteinheit)<br/><Werte>`SEKUNDE`, `MINUTE`, `STUNDE`, `VIERTEL_STUNDE`, `TAG`, `WOCHE`, `MONAT`, `QUARTAL`, `HALBJAHR`, `JAHR`</Werte> |
| <span className="hbs-f hbs-e1">[dauer](/bo4e/202604/com/Zeitraum#dauer)</span> | dauer | integer |
| <span className="hbs-f hbs-e1">[startdatum](/bo4e/202604/com/Zeitraum#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e1">[enddatum](/bo4e/202604/com/Zeitraum#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-f hbs-e1">[einheit](/bo4e/202604/com/Zeitraum#einheit)</span> | Zeiteinheit | [Enum Zeiteinheit](/bo4e/202604/enum/Zeiteinheit)<br/><Werte>`SEKUNDE`, `MINUTE`, `STUNDE`, `VIERTEL_STUNDE`, `TAG`, `WOCHE`, `MONAT`, `QUARTAL`, `HALBJAHR`, `JAHR`</Werte> |
| <span className="hbs-f hbs-e1">[ableseZeitraum](/bo4e/202604/com/Zeitraum#ablesezeitraum)</span> | ableseZeitraum | string |
| <span className="hbs-f hbs-e1">[abrechnungsZeitraum](/bo4e/202604/com/Zeitraum#abrechnungszeitraum)</span> | abrechnungsZeitraum | string |
| <span className="hbs-f hbs-e1">[zeitraumText](/bo4e/202604/com/Zeitraum#zeitraumtext)</span> | zeitraumText | string |
| <span className="hbs-f hbs-e1">[zeitraumId](/bo4e/202604/com/Zeitraum#zeitraumid)</span> | zeitraumId | integer |
| <span className="hbs-f hbs-e0">[kuendigungstermin](/bo4e/202604/com/Vertragskonditionen#kuendigungstermin)</span> | kuendigungstermin | string |
| <span className="hbs-g hbs-e0">[abschlagszyklus](/bo4e/202604/com/Vertragskonditionen#abschlagszyklus)</span> | In diesen Zyklen werden Abschläge gestellt. Details Zeitraum. Alternativ kann auch die Anzahl<br/>in den Konditionen angeben werden." | [Zeitraum](/bo4e/202604/com/Zeitraum) |
| <span className="hbs-f hbs-e1">[zeiteinheit](/bo4e/202604/com/Zeitraum#zeiteinheit)</span> | Zeiteinheit | [Enum Zeiteinheit](/bo4e/202604/enum/Zeiteinheit)<br/><Werte>`SEKUNDE`, `MINUTE`, `STUNDE`, `VIERTEL_STUNDE`, `TAG`, `WOCHE`, `MONAT`, `QUARTAL`, `HALBJAHR`, `JAHR`</Werte> |
| <span className="hbs-f hbs-e1">[dauer](/bo4e/202604/com/Zeitraum#dauer)</span> | dauer | integer |
| <span className="hbs-f hbs-e1">[startdatum](/bo4e/202604/com/Zeitraum#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e1">[enddatum](/bo4e/202604/com/Zeitraum#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-f hbs-e1">[einheit](/bo4e/202604/com/Zeitraum#einheit)</span> | Zeiteinheit | [Enum Zeiteinheit](/bo4e/202604/enum/Zeiteinheit)<br/><Werte>`SEKUNDE`, `MINUTE`, `STUNDE`, `VIERTEL_STUNDE`, `TAG`, `WOCHE`, `MONAT`, `QUARTAL`, `HALBJAHR`, `JAHR`</Werte> |
| <span className="hbs-f hbs-e1">[ableseZeitraum](/bo4e/202604/com/Zeitraum#ablesezeitraum)</span> | ableseZeitraum | string |
| <span className="hbs-f hbs-e1">[abrechnungsZeitraum](/bo4e/202604/com/Zeitraum#abrechnungszeitraum)</span> | abrechnungsZeitraum | string |
| <span className="hbs-f hbs-e1">[zeitraumText](/bo4e/202604/com/Zeitraum#zeitraumtext)</span> | zeitraumText | string |
| <span className="hbs-f hbs-e1">[zeitraumId](/bo4e/202604/com/Zeitraum#zeitraumid)</span> | zeitraumId | integer |
| <span className="hbs-f hbs-e0">[anzahl_abschlaege](/bo4e/202604/com/Vertragskonditionen#anzahl_abschlaege)</span> | Anzahl der vereinbarten Abschläge pro Jahr, z.B. 12 | number (float) |
| <span className="hbs-f hbs-e0">[beschreibung](/bo4e/202604/com/Vertragskonditionen#beschreibung)</span> | Freitext zur Beschreibung der Konditionen, z.B. "Standardkonditionen Gas" | string |
| <span className="hbs-g hbs-e0">[vertragsverlaengerung](/bo4e/202604/com/Vertragskonditionen#vertragsverlaengerung)</span> | Falls der Vertrag nicht gekündigt wird, verlängert er sich automatisch um die hier angegebene Zeit. Details<br/>Zeitraum | [Zeitraum](/bo4e/202604/com/Zeitraum) |
| <span className="hbs-f hbs-e1">[zeiteinheit](/bo4e/202604/com/Zeitraum#zeiteinheit)</span> | Zeiteinheit | [Enum Zeiteinheit](/bo4e/202604/enum/Zeiteinheit)<br/><Werte>`SEKUNDE`, `MINUTE`, `STUNDE`, `VIERTEL_STUNDE`, `TAG`, `WOCHE`, `MONAT`, `QUARTAL`, `HALBJAHR`, `JAHR`</Werte> |
| <span className="hbs-f hbs-e1">[dauer](/bo4e/202604/com/Zeitraum#dauer)</span> | dauer | integer |
| <span className="hbs-f hbs-e1">[startdatum](/bo4e/202604/com/Zeitraum#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e1">[enddatum](/bo4e/202604/com/Zeitraum#enddatum)</span> | enddatum | string (date-time) |
| <span className="hbs-f hbs-e1">[einheit](/bo4e/202604/com/Zeitraum#einheit)</span> | Zeiteinheit | [Enum Zeiteinheit](/bo4e/202604/enum/Zeiteinheit)<br/><Werte>`SEKUNDE`, `MINUTE`, `STUNDE`, `VIERTEL_STUNDE`, `TAG`, `WOCHE`, `MONAT`, `QUARTAL`, `HALBJAHR`, `JAHR`</Werte> |
| <span className="hbs-f hbs-e1">[ableseZeitraum](/bo4e/202604/com/Zeitraum#ablesezeitraum)</span> | ableseZeitraum | string |
| <span className="hbs-f hbs-e1">[abrechnungsZeitraum](/bo4e/202604/com/Zeitraum#abrechnungszeitraum)</span> | abrechnungsZeitraum | string |
| <span className="hbs-f hbs-e1">[zeitraumText](/bo4e/202604/com/Zeitraum#zeitraumtext)</span> | zeitraumText | string |
| <span className="hbs-f hbs-e1">[zeitraumId](/bo4e/202604/com/Zeitraum#zeitraumid)</span> | zeitraumId | integer |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### netznutzungszahler

13 Verwendung(en) in den Nachrichtentypen UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_44001](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44001) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_44019](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44019) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_44020](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44020) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_44021](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44021) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_44035](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44035) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_44112](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44112) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_44139](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44139) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_44142](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44142) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_55218](/schnittstellen/202604/pruefi/UTILMD/PI_55218) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_55220](/schnittstellen/202604/pruefi/UTILMD/PI_55220) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |

### netznutzungsvertrag

13 Verwendung(en) in den Nachrichtentypen UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_44001](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44001) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_44019](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44019) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_44020](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44020) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_44021](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44021) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_44035](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44035) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_44112](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44112) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_44139](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44139) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_44142](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44142) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_55218](/schnittstellen/202604/pruefi/UTILMD/PI_55218) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_55220](/schnittstellen/202604/pruefi/UTILMD/PI_55220) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |

### netznutzungsabrechnungsgrundlage

2 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55218](/schnittstellen/202604/pruefi/UTILMD/PI_55218) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_55220](/schnittstellen/202604/pruefi/UTILMD/PI_55220) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |

### netznutzungsabrechnungsvariante

7 Verwendung(en) in den Nachrichtentypen UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_44035](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44035) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_44112](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44112) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_44139](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44139) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_44142](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44142) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |

### haushaltskunde

17 Verwendung(en) in den Nachrichtentypen UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_44001](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44001) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_44019](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44019) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_44020](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44020) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_44021](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44021) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_44035](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44035) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_44109](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44109) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_44137](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44137) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_44138](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44138) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_55001](/schnittstellen/202604/pruefi/UTILMD/PI_55001) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_55013](/schnittstellen/202604/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_55014](/schnittstellen/202604/pruefi/UTILMD/PI_55014) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_55109](/schnittstellen/202604/pruefi/UTILMD/PI_55109) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_55137](/schnittstellen/202604/pruefi/UTILMD/PI_55137) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_55600](/schnittstellen/202604/pruefi/UTILMD/PI_55600) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |

### abrechnungUeberNna

2 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55620](/schnittstellen/202604/pruefi/UTILMD/PI_55620) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragskonditionen |
| [PI_55626](/schnittstellen/202604/pruefi/UTILMD/PI_55626) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragskonditionen |

### startAbrechnungsjahr

7 Verwendung(en) in den Nachrichtentypen UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_44035](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44035) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_44112](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44112) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_44139](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44139) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_44142](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44142) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |

### naechstenetznutzungsabrechnung

8 Verwendung(en) in den Nachrichtentypen UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_44112](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44112) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_44139](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44139) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_44142](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44142) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_55218](/schnittstellen/202604/pruefi/UTILMD/PI_55218) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_55220](/schnittstellen/202604/pruefi/UTILMD/PI_55220) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |

### abrechnungsintervall

6 Verwendung(en) in den Nachrichtentypen UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_44001](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44001) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragskonditionen |
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragskonditionen |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragskonditionen |
| [PI_44109](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44109) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragskonditionen |
| [PI_44137](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44137) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragskonditionen |
| [PI_44138](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44138) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragskonditionen |

### netznutzungsabrechnungIntervall

9 Verwendung(en) in den Nachrichtentypen UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_44035](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44035) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_44112](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44112) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_44139](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44139) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_44142](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44142) | Prüfi | UTILMD_GAS | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_55218](/schnittstellen/202604/pruefi/UTILMD/PI_55218) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |
| [PI_55220](/schnittstellen/202604/pruefi/UTILMD/PI_55220) | Prüfi | UTILMD | stammdaten › NETZNUTZUNGSVERTRAG › vertragskonditionen |

### beauftragungMsb

1 Verwendung(en) in den Nachrichtentypen UTILMD.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_55042](/schnittstellen/202604/pruefi/UTILMD/PI_55042) | Prüfi | UTILMD | stammdaten › MESSSTELLENBETRIEBSVERTRAG › vertragskonditionen |

### kuendigungstermin

4 Verwendung(en) in den Nachrichtentypen UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_44018](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44018) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragskonditionen |
| [PI_44041](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44041) | Prüfi | UTILMD_GAS | stammdaten › ENERGIELIEFERVERTRAG › vertragskonditionen |
| [PI_55018](/schnittstellen/202604/pruefi/UTILMD/PI_55018) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragskonditionen |
| [PI_55041](/schnittstellen/202604/pruefi/UTILMD/PI_55041) | Prüfi | UTILMD | stammdaten › ENERGIELIEFERVERTRAG › vertragskonditionen |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
