# Menge
<span hidden data-pagefind-meta={"title:Menge — BO4E-Komponente (FV 202604)"} />

BO4E-Komponente · 4 Felder · 132 Verwendungen in Prüfis und Events

## Felder

<Feldansicht>

<div data-ansicht-teil="tabelle">

<div className="maco-tabellenrahmen maco-bo4e-felder" data-maco="bo4e-tabelle">

| Feld | Typ | Beschreibung |
|---|---|---|
| <a id="wert"></a>`wert` | number (float) | Wert |
| <a id="einheit"></a>`einheit` | [Enum Mengeneinheit](/bo4e/202604/enum/Mengeneinheit)<br/><Werte>`W`, `WH`, `KW`, `KWH`, `KVARH`, `MW`, `MWH`, `STUECK`, `KUBIKMETER`, `STUNDE`, `TAG`, `MONAT`, `JAHR`, `PROZENT`, `ANZAHL`, `VAR`, `KVAR`, `VARH`, `KWHK`, `Z16`, `KWT`, `WATT_PRO_QUADRATMETER`, `METER_PRO_SEKUNDE`</Werte> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können |
| <a id="startdatum"></a>`startdatum` | string (date-time) | startdatum |
| <a id="enddatum"></a>`enddatum` | string (date-time) | enddatum |

</div>

</div>

<div data-ansicht-teil="baum" data-pagefind-ignore="all">

<Handbuchsatz art="struktur" start="zu">

<div className="maco-tabellenrahmen" data-maco="bo4e-baum">

| Struktur (BO4E) | Beschreibung | Format |
|---|---|---|
| <span className="hbs-f hbs-e0">[wert](/bo4e/202604/com/Menge#wert)</span> | Wert | number (float) |
| <span className="hbs-f hbs-e0">[einheit](/bo4e/202604/com/Menge#einheit)</span> | Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können | [Enum Mengeneinheit](/bo4e/202604/enum/Mengeneinheit)<br/><Werte>`W`, `WH`, `KW`, `KWH`, `KVARH`, `MW`, `MWH`, `STUECK`, `KUBIKMETER`, `STUNDE`, `TAG`, `MONAT`, `JAHR`, `PROZENT`, `ANZAHL`, `VAR`, `KVAR`, `VARH`, `KWHK`, `Z16`, `KWT`, `WATT_PRO_QUADRATMETER`, `METER_PRO_SEKUNDE`</Werte> |
| <span className="hbs-f hbs-e0">[startdatum](/bo4e/202604/com/Menge#startdatum)</span> | startdatum | string (date-time) |
| <span className="hbs-f hbs-e0">[enddatum](/bo4e/202604/com/Menge#enddatum)</span> | enddatum | string (date-time) |

</div>

</Handbuchsatz>

</div>

</Feldansicht>

## Verwendet in

### wert

74 Verwendung(en) in den Nachrichtentypen IFTSTA, INVOIC, ORDERS, UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_17134](/schnittstellen/202604/pruefi/ORDERS/PI_17134) | Prüfi | ORDERS | stammdaten › TRANCHE › aufteilungsmenge |
| [PI_21035](/schnittstellen/202604/pruefi/IFTSTA/PI_21035) | Prüfi | IFTSTA | transaktionsdaten › menge |
| [PI_31002](/schnittstellen/202604/pruefi/INVOIC/PI_31002) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen › positionsMenge |
| [PI_31002](/schnittstellen/202604/pruefi/INVOIC/PI_31002) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen › zeitbezogeneMenge |
| [PI_44001](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44001) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › jahresverbrauchsprognose |
| [PI_44001](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44001) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › kundenwert |
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › jahresverbrauchsprognose |
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › kundenwert |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › jahresverbrauchsprognose |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › kundenwert |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › jahresverbrauchsprognose |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › kundenwert |
| [PI_44017](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44017) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › vorjahresverbrauch |
| [PI_44019](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44019) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › jahresverbrauchsprognose |
| [PI_44019](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44019) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › kundenwert |
| [PI_44020](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44020) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › jahresverbrauchsprognose |
| [PI_44020](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44020) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › kundenwert |
| [PI_44021](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44021) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › jahresverbrauchsprognose |
| [PI_44021](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44021) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › kundenwert |
| [PI_44035](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44035) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › jahresverbrauchsprognose |
| [PI_44035](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44035) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › kundenwert |
| [PI_44103](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44103) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › jahresverbrauchsprognose |
| [PI_44103](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44103) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › kundenwert |
| [PI_44104](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44104) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › jahresverbrauchsprognose |
| [PI_44104](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44104) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › kundenwert |
| [PI_44123](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44123) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › jahresverbrauchsprognose |
| [PI_44123](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44123) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › kundenwert |
| [PI_44156](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44156) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › jahresverbrauchsprognose |
| [PI_44156](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44156) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › kundenwert |
| [PI_44157](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44157) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › jahresverbrauchsprognose |
| [PI_44157](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44157) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › kundenwert |
| [PI_55013](/schnittstellen/202604/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › jahresverbrauchsprognose |
| [PI_55013](/schnittstellen/202604/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › temperaturarbeit |
| [PI_55017](/schnittstellen/202604/pruefi/UTILMD/PI_55017) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › vorjahresverbrauch |
| [PI_55035](/schnittstellen/202604/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › jahresverbrauchsprognose |
| [PI_55035](/schnittstellen/202604/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › temperaturarbeit |
| [PI_55035](/schnittstellen/202604/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › netznutzungsabrechnungsdaten › singulaereBetriebsmittel |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › jahresverbrauchsprognose |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › temperaturarbeit |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › TRANCHE › aufteilungsmenge |
| [PI_55060](/schnittstellen/202604/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › jahresverbrauchsprognose |
| [PI_55060](/schnittstellen/202604/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › temperaturarbeit |
| [PI_55060](/schnittstellen/202604/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › TRANCHE › aufteilungsmenge |
| [PI_55074](/schnittstellen/202604/pruefi/UTILMD/PI_55074) | Prüfi | UTILMD | stammdaten › TRANCHE › aufteilungsmenge |
| [PI_55075](/schnittstellen/202604/pruefi/UTILMD/PI_55075) | Prüfi | UTILMD | stammdaten › TRANCHE › aufteilungsmenge |
| [PI_55078](/schnittstellen/202604/pruefi/UTILMD/PI_55078) | Prüfi | UTILMD | stammdaten › TRANCHE › aufteilungsmenge |
| [PI_55095](/schnittstellen/202604/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › jahresverbrauchsprognose |
| [PI_55095](/schnittstellen/202604/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › temperaturarbeit |
| [PI_55126](/schnittstellen/202604/pruefi/UTILMD/PI_55126) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › jahresverbrauchsprognose |
| [PI_55126](/schnittstellen/202604/pruefi/UTILMD/PI_55126) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › temperaturarbeit |
| [PI_55156](/schnittstellen/202604/pruefi/UTILMD/PI_55156) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › jahresverbrauchsprognose |
| [PI_55156](/schnittstellen/202604/pruefi/UTILMD/PI_55156) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › temperaturarbeit |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › jahresverbrauchsprognose |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › temperaturarbeit |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › TRANCHE › aufteilungsmenge |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › jahresverbrauchsprognose |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › temperaturarbeit |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › TRANCHE › aufteilungsmenge |
| [PI_55218](/schnittstellen/202604/pruefi/UTILMD/PI_55218) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › verbrauchsaufteilung |
| [PI_55218](/schnittstellen/202604/pruefi/UTILMD/PI_55218) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › netznutzungsabrechnungsdaten › singulaereBetriebsmittel |
| [PI_55220](/schnittstellen/202604/pruefi/UTILMD/PI_55220) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › verbrauchsaufteilung |
| [PI_55220](/schnittstellen/202604/pruefi/UTILMD/PI_55220) | Prüfi | UTILMD | stammdaten › MARKTLOKATION › netznutzungsabrechnungsdaten › singulaereBetriebsmittel |
| [PI_55603](/schnittstellen/202604/pruefi/UTILMD/PI_55603) | Prüfi | UTILMD | stammdaten › TRANCHE › aufteilungsmenge |
| [PI_55607](/schnittstellen/202604/pruefi/UTILMD/PI_55607) | Prüfi | UTILMD | stammdaten › TRANCHE › aufteilungsmenge |
| [PI_55613](/schnittstellen/202604/pruefi/UTILMD/PI_55613) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › jahresverbrauchsprognose |
| [PI_55614](/schnittstellen/202604/pruefi/UTILMD/PI_55614) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › jahresverbrauchsprognose |
| [PI_55628](/schnittstellen/202604/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › jahresverbrauchsprognose |
| [PI_55628](/schnittstellen/202604/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › temperaturarbeit |
| [PI_55634](/schnittstellen/202604/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › jahresverbrauchsprognose |
| [PI_55634](/schnittstellen/202604/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › temperaturarbeit |
| [PI_55672](/schnittstellen/202604/pruefi/UTILMD/PI_55672) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › jahresverbrauchsprognose |
| [PI_55672](/schnittstellen/202604/pruefi/UTILMD/PI_55672) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › temperaturarbeit |
| [PI_55673](/schnittstellen/202604/pruefi/UTILMD/PI_55673) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › jahresverbrauchsprognose |
| [PI_55673](/schnittstellen/202604/pruefi/UTILMD/PI_55673) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › temperaturarbeit |

### einheit

58 Verwendung(en) in den Nachrichtentypen IFTSTA, INVOIC, ORDERS, UTILMD, UTILMD_GAS.

| Verwendet in | Art | Nachrichtentyp | Container |
|---|---|---|---|
| [PI_17134](/schnittstellen/202604/pruefi/ORDERS/PI_17134) | Prüfi | ORDERS | stammdaten › TRANCHE › aufteilungsmenge |
| [PI_21035](/schnittstellen/202604/pruefi/IFTSTA/PI_21035) | Prüfi | IFTSTA | transaktionsdaten › menge |
| [PI_31002](/schnittstellen/202604/pruefi/INVOIC/PI_31002) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen › positionsMenge |
| [PI_31002](/schnittstellen/202604/pruefi/INVOIC/PI_31002) | Prüfi | INVOIC | stammdaten › RECHNUNG › rechnungspositionen › zeitbezogeneMenge |
| [PI_44001](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44001) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › jahresverbrauchsprognose |
| [PI_44002](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44002) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › jahresverbrauchsprognose |
| [PI_44013](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44013) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › jahresverbrauchsprognose |
| [PI_44014](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44014) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › jahresverbrauchsprognose |
| [PI_44017](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44017) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › vorjahresverbrauch |
| [PI_44019](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44019) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › jahresverbrauchsprognose |
| [PI_44020](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44020) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › jahresverbrauchsprognose |
| [PI_44021](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44021) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › jahresverbrauchsprognose |
| [PI_44035](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44035) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › jahresverbrauchsprognose |
| [PI_44103](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44103) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › jahresverbrauchsprognose |
| [PI_44104](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44104) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › jahresverbrauchsprognose |
| [PI_44123](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44123) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › jahresverbrauchsprognose |
| [PI_44156](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44156) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › jahresverbrauchsprognose |
| [PI_44157](/schnittstellen/202604/pruefi/UTILMD_GAS/PI_44157) | Prüfi | UTILMD_GAS | stammdaten › BILANZIERUNG › jahresverbrauchsprognose |
| [PI_55013](/schnittstellen/202604/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › jahresverbrauchsprognose |
| [PI_55013](/schnittstellen/202604/pruefi/UTILMD/PI_55013) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › temperaturarbeit |
| [PI_55017](/schnittstellen/202604/pruefi/UTILMD/PI_55017) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › vorjahresverbrauch |
| [PI_55035](/schnittstellen/202604/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › jahresverbrauchsprognose |
| [PI_55035](/schnittstellen/202604/pruefi/UTILMD/PI_55035) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › temperaturarbeit |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › jahresverbrauchsprognose |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › temperaturarbeit |
| [PI_55043](/schnittstellen/202604/pruefi/UTILMD/PI_55043) | Prüfi | UTILMD | stammdaten › TRANCHE › aufteilungsmenge |
| [PI_55060](/schnittstellen/202604/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › jahresverbrauchsprognose |
| [PI_55060](/schnittstellen/202604/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › temperaturarbeit |
| [PI_55060](/schnittstellen/202604/pruefi/UTILMD/PI_55060) | Prüfi | UTILMD | stammdaten › TRANCHE › aufteilungsmenge |
| [PI_55074](/schnittstellen/202604/pruefi/UTILMD/PI_55074) | Prüfi | UTILMD | stammdaten › TRANCHE › aufteilungsmenge |
| [PI_55075](/schnittstellen/202604/pruefi/UTILMD/PI_55075) | Prüfi | UTILMD | stammdaten › TRANCHE › aufteilungsmenge |
| [PI_55078](/schnittstellen/202604/pruefi/UTILMD/PI_55078) | Prüfi | UTILMD | stammdaten › TRANCHE › aufteilungsmenge |
| [PI_55095](/schnittstellen/202604/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › jahresverbrauchsprognose |
| [PI_55095](/schnittstellen/202604/pruefi/UTILMD/PI_55095) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › temperaturarbeit |
| [PI_55126](/schnittstellen/202604/pruefi/UTILMD/PI_55126) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › jahresverbrauchsprognose |
| [PI_55126](/schnittstellen/202604/pruefi/UTILMD/PI_55126) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › temperaturarbeit |
| [PI_55156](/schnittstellen/202604/pruefi/UTILMD/PI_55156) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › jahresverbrauchsprognose |
| [PI_55156](/schnittstellen/202604/pruefi/UTILMD/PI_55156) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › temperaturarbeit |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › jahresverbrauchsprognose |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › temperaturarbeit |
| [PI_55168](/schnittstellen/202604/pruefi/UTILMD/PI_55168) | Prüfi | UTILMD | stammdaten › TRANCHE › aufteilungsmenge |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › jahresverbrauchsprognose |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › temperaturarbeit |
| [PI_55169](/schnittstellen/202604/pruefi/UTILMD/PI_55169) | Prüfi | UTILMD | stammdaten › TRANCHE › aufteilungsmenge |
| [PI_55218](/schnittstellen/202604/pruefi/UTILMD/PI_55218) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › verbrauchsaufteilung |
| [PI_55220](/schnittstellen/202604/pruefi/UTILMD/PI_55220) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › verbrauchsaufteilung |
| [PI_55603](/schnittstellen/202604/pruefi/UTILMD/PI_55603) | Prüfi | UTILMD | stammdaten › TRANCHE › aufteilungsmenge |
| [PI_55607](/schnittstellen/202604/pruefi/UTILMD/PI_55607) | Prüfi | UTILMD | stammdaten › TRANCHE › aufteilungsmenge |
| [PI_55613](/schnittstellen/202604/pruefi/UTILMD/PI_55613) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › jahresverbrauchsprognose |
| [PI_55614](/schnittstellen/202604/pruefi/UTILMD/PI_55614) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › jahresverbrauchsprognose |
| [PI_55628](/schnittstellen/202604/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › jahresverbrauchsprognose |
| [PI_55628](/schnittstellen/202604/pruefi/UTILMD/PI_55628) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › temperaturarbeit |
| [PI_55634](/schnittstellen/202604/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › jahresverbrauchsprognose |
| [PI_55634](/schnittstellen/202604/pruefi/UTILMD/PI_55634) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › temperaturarbeit |
| [PI_55672](/schnittstellen/202604/pruefi/UTILMD/PI_55672) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › jahresverbrauchsprognose |
| [PI_55672](/schnittstellen/202604/pruefi/UTILMD/PI_55672) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › temperaturarbeit |
| [PI_55673](/schnittstellen/202604/pruefi/UTILMD/PI_55673) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › jahresverbrauchsprognose |
| [PI_55673](/schnittstellen/202604/pruefi/UTILMD/PI_55673) | Prüfi | UTILMD | stammdaten › BILANZIERUNG › temperaturarbeit |

<Hinweisbereich>

Ein **\*** hinter einem Feldnamen kennzeichnet ein **Pflichtfeld**; das BO4E-Schema führt es unter `required`.

Diese Übersicht wird aus dem `$ref`-Graph über alle Prüfi- und Event-Spezifikationen erzeugt. Sie beantwortet die Frage, in welchen Nachrichten ein Feld tatsächlich vorkommt — eine Information, die in der bisherigen Dokumentation nicht verfügbar war.

</Hinweisbereich>
