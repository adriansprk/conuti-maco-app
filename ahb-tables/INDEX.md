# AHB Tables Index

Anwendungshandbücher (AHB) for all BDEW Prüfidentifikatoren.
Downloaded from [ahb-tabellen.hochfrequenz.de](https://ahb-tabellen.hochfrequenz.de) (public API, no auth required).

**Refresh:** `python3 scripts/download-ahb-tables.py` then `python3 scripts/generate-ahb-index.py`

## Available Versions

- **FV2510**: 488 Prüfidentifikatoren
- **FV2604**: 495 Prüfidentifikatoren

## How to Use (for Agents)



## Direction Reference (LF perspective)

| Direction | Meaning | LF Role |
|-----------|---------|---------|
| `LF → NB` | Outbound | LF sends to NB |
| `NB → LF` | Inbound | LF receives from NB |
| `LF → MSB` | Outbound | LF sends to MSB |
| `MSB → LF` | Inbound | LF receives from MSB |
| other | varies | check meta.direction |

## FV2510 — All Prüfidentifikatoren

| Prüfi | Description | Direction | Version | Date | Lines |
|-------|-------------|-----------|---------|------|-------|
| 13002 | Zählerstand (Gas) | MSCONS-Nachrichten können von verschiede | 3.1f | 2025-06-23 | 191 |
| 13003 | Summenzeitreihe | MSCONS-Nachrichten können von verschiede | 3.1f | 2025-06-23 | 102 |
| 13005 | EEG-Überführungs-ZR | MSCONS-Nachrichten können von verschiede | 3.1f | 2025-06-23 | 110 |
| 13006 | Messwert Storno | MSCONS-Nachrichten können von verschiede | 3.1f | 2025-06-23 | 84 |
| 13007 | Gasbeschaffenheit | MSCONS-Nachrichten können von verschiede | 3.1f | 2025-06-23 | 167 |
| 13008 | Lastgang (Gas) | MSCONS-Nachrichten können von verschiede | 3.1f | 2025-06-23 | 181 |
| 13009 | Energiemenge (Gas) | MSCONS-Nachrichten können von verschiede | 3.1f | 2025-06-23 | 172 |
| 13010 | normiertes Profil | MSCONS-Nachrichten können von verschiede | 3.1f | 2025-06-23 | 93 |
| 13011 | Profilschar | MSCONS-Nachrichten können von verschiede | 3.1f | 2025-06-23 | 90 |
| 13012 | TEP vergh. Werte Referenzmessung | MSCONS-Nachrichten können von verschiede | 3.1f | 2025-06-23 | 93 |
| 13013 | marktlokations- scharfe Allokationsliste Gas (MMMA | MSCONS-Nachrichten können von verschiede | 3.1f | 2025-06-23 | 99 |
| 13014 | marktlokations- scharfe bilanzierte Menge Strom /  | MSCONS-Nachrichten können von verschiede | 3.1f | 2025-06-23 | 97 |
| 13015 | Arbeit Leistungsmax. Kalenderjahr vor Lieferbeginn | MSCONS-Nachrichten können von verschiede | 3.1f | 2025-06-23 | 104 |
| 13016 | Energiemenge u. Leistungsmax. (Strom) | MSCONS-Nachrichten können von verschiede | 3.1f | 2025-06-23 | 146 |
| 13017 | Zählerstand (Strom) | MSCONS-Nachrichten können von verschiede | 3.1f | 2025-06-23 | 168 |
| 13018 | Lastgang Messlokation, Netzkoppelpunkt, Netzlokati | MSCONS-Nachrichten können von verschiede | 3.1f | 2025-06-23 | 163 |
| 13019 | Energiemenge (Strom) | MSCONS-Nachrichten können von verschiede | 3.1f | 2025-06-23 | 168 |
| 13020 | Ausfallarbeitsüberführungszeitreihe | MSCONS-Nachrichten können von verschiede | 3.1f | 2025-06-23 | 107 |
| 13021 | Übermittlung von meteorologischen Daten | MSCONS-Nachrichten können von verschiede | 3.1f | 2025-06-23 | 103 |
| 13022 | Redispatch 2.0 Einzelzeitreihe Ausfallarbeit | MSCONS-Nachrichten können von verschiede | 3.1f | 2025-06-23 | 107 |
| 13023 | Redispatch 2.0 Ausfallarbeitssummenzeitreihe | MSCONS-Nachrichten können von verschiede | 3.1f | 2025-06-23 | 98 |
| 13025 | Lastgang Marktlokation, Tranche | MSCONS-Nachrichten können von verschiede | 3.1f | 2025-06-23 | 163 |
| 13026 | EEG-Überführungs-ZR aufgrund Ausfallarbeit | MSCONS-Nachrichten können von verschiede | 3.1f | 2025-06-23 | 111 |
| 13027 | Werte nach Typ 2 | MSCONS-Nachrichten können von verschiede | 3.1f | 2025-06-23 | 99 |
| 13028 | Grundlage POG-Ermittlung | MSCONS-Nachrichten können von verschiede | 3.1f | 2025-06-23 | 89 |
| 15001 | Angebot Geräteübernahme | MSBA → MSBN | 1.1 | 2025-04-01 | 221 |
| 15002 | Angebot Abrechnung Messstellenbetrieb MSB | MSB → LF | 1.1 | 2025-04-01 | 93 |
| 15003 | Angebot zur Anfrage von Werten | MSB → ESA | 1.1 | 2025-04-01 | 128 |
| 15004 | Angebot einer Konfiguration | MSB → NB, MSB → LF | 1.1 | 2025-04-01 | 138 |
| 15005 | Angebot Änderung Technik | MSB → NB, MSB → LF | 1.1 | 2025-04-01 | 140 |
| 17001 | Bestellung Geräteübernahmeangebot | MSBN → MSBA | 1.1 | 2025-06-23 | 63 |
| 17002 | Weiterverpflichtung | NB → MSBA | 1.1 | 2025-06-23 | 62 |
| 17003 | Beauftragung Änderung Technik | LF → MSB, NB → MSB | 1.1 | 2025-06-23 | 80 |
| 17004 | Anforderung von Werten | LF → MSB (Strom), LF → , NB → MSB (Strom | 1.1 | 2025-06-23 | 68 |
| 17005 | Bestellung Rechnungsabwicklung MSB über LF | LF → MSB | 1.1 | 2025-06-23 | 62 |
| 17006 | Beendigung Rechnungsabwicklung MSB über LF | LF → MSB, LF → , MSB → LF | 1.1 | 2025-06-23 | 65 |
| 17007 | Bestellung von Werten | ESA → MSB | 1.1 | 2025-06-23 | 57 |
| 17008 | Abbestellung von Werten | ESA → MSB | 1.1 | 2025-06-23 | 56 |
| 17009 | Anzeige Gerätewechselabsicht | MSBN → MSBA | 1.1 | 2025-06-23 | 77 |
| 17011 | Bestellung Angebot Änderung Technik | NB → MSB, LF → MSB | 1.1 | 2025-06-23 | 121 |
| 17101 | Anfrage Stammdaten Marktlokation (Gas) | LF → NB (Gas) | 1.1 | 2025-06-23 | 80 |
| 17102 | Anfrage von Werten | LF → MSB (Strom), LF → , LF → NB (Gas),  | 1.1 | 2025-06-23 | 71 |
| 17103 | Anforderung Brennwert / Zustandszahl | LF → NB | 1.1 | 2025-06-23 | 65 |
| 17104 | Anfrage vom MSB Gas | MSB (Gas) → NB (Strom) | 1.1 | 2025-06-23 | 60 |
| 17110 | Anforderung Allokationsliste | LF → NB | 1.1 | 2025-06-23 | 53 |
| 17111 | Bestellanforderung Änderung Prognosegrundlage/ Ger | LF → NB | 1.1 | 2025-06-23 | 66 |
| 17112 | Bestellanforderung Änderung Gerätekonfiguration | NB → MSB | 1.1 | 2025-06-23 | 86 |
| 17113 | Reklamation von Werten | LF → MSB (Strom), LF → , NB → MSB (Strom | 1.1 | 2025-06-23 | 90 |
| 17114 | Anforderung bilanzierte Menge | NB → ÜNB | 1.1 | 2025-06-23 | 63 |
| 17115 | Sperrauftrag | LF → NB | 1.1 | 2025-06-23 | 76 |
| 17116 | Anfrage Sperrung | NB → MSB | 1.1 | 2025-06-23 | 72 |
| 17117 | Entsperrauftrag | LF → NB | 1.1 | 2025-06-23 | 71 |
| 17118 | Bestellung einer Konfigurationsänderung | MSB → MSB | 1.1 | 2025-06-23 | 88 |
| 17120 | Bestellung Änderung Prognosegrundlage | LF → NB | 1.1 | 2025-06-23 | 65 |
| 17121 | Bestellung Änderung | NB → MSB | 1.1 | 2025-06-23 | 174 |
| 17122 | Reklamation einer Definition | LF → NB, MSB → NB, MSB → LF, NB → LF | 1.1 | 2025-06-23 | 78 |
| 17123 | Bestellung Änderung Zählzeitdefinition | LF → NB, LF → MSB | 1.1 | 2025-06-23 | 73 |
| 17124 | Weiterleitung/Bestellung Änderung Zählzeitdefiniti | NB → MSB | 1.1 | 2025-06-23 | 58 |
| 17125 | Bestellung Konfigurationsänderung aufgrund Änderun | MSB → MSB | 1.1 | 2025-06-23 | 55 |
| 17126 | Anfrage Stammdaten Messlokation (Gas) | MSB → NB (Gas) | 1.1 | 2025-06-23 | 76 |
| 17128 | Reklamation einer Konfiguration | NB → MSB, LF → MSB, MSB → MSB | 1.1 | 2025-06-23 | 148 |
| 17129 | Bestellung Beendigung einer Konfiguration | NB → MSB, LF → MSB, MSB → MSB | 1.1 | 2025-06-23 | 58 |
| 17130 | Bestellung einer Konfiguration | NB → MSB, LF → MSB, MSB → MSB | 1.1 | 2025-06-23 | 135 |
| 17131 | Bestellung Angebot einer Konfiguration | NB → MSB, LF → MSB | 1.1 | 2025-06-23 | 50 |
| 17132 | Anfrage Stammdaten (Strom) | LF → NB, MSB → NB | 1.1 | 2025-06-23 | 52 |
| 17133 | Bestellung Änderung Abrechnungsdaten | LF → NB | 1.1 | 2025-06-23 | 81 |
| 17134 | Einrichtung Konfiguration Zuordnung LF von NB | NB → MSB | 1.1 | 2025-06-23 | 199 |
| 17135 | Einrichtung Konfiguration Zuordnung LF von MSB | MSB → MSB | 1.1 | 2025-06-23 | 112 |
| 17201 | Anforder. normierter Profile und Profilscharen | LF → NB | 1.1 | 2025-06-23 | 58 |
| 17202 | Anforder. Lieferantenclearingliste | LF → NB, LF → ÜNB | 1.1 | 2025-06-23 | 69 |
| 17203 | Anforder. Bilanzkreiszuordnungsliste | BKV → NB, BKV → ÜNB | 1.1 | 2025-06-23 | 69 |
| 17204 | Anforder. Clearingliste BAS | BKV → BIKO | 1.1 | 2025-06-23 | 63 |
| 17205 | Anforder. Clearingliste DZR | NB → BIKO | 1.1 | 2025-06-23 | 63 |
| 17206 | Anforderung Bilanzierungsgebiets clearingliste | NB → ÜNB | 1.1 | 2025-06-23 | 69 |
| 17207 | Ab-/Bestellung BK-SZR auf Aggregationsebene RZ | BKV → ÜNB | 1.1 | 2025-06-23 | 60 |
| 17208 | Anforderung Clearingliste ÜNB-DZR | ÜNB → BIKO | 1.1 | 2025-06-23 | 63 |
| 17209 | Anforderung Ausfallarbeit | anfNB → ANB | 1.1 | 2025-06-23 | 67 |
| 17210 | Anforderung Lieferantenausfallarbeitsclearingliste | LF → NB | 1.1 | 2025-06-23 | 69 |
| 17211 | Reklamation Profile bzw. Profilscharen | LF → NB | 1.1 | 2025-06-23 | 54 |
| 17301 | Anforderung von Stammdaten bzw. Messwerten | UBA → NB | 1.1 | 2025-06-23 | 62 |
| 19001 | Bestätigung Bestellung | MSBA → MSBN | 1.1 | 2025-04-17 | 61 |
| 19002 | Ablehnung Bestellung | MSBA → MSBN | 1.1 | 2025-04-17 | 61 |
| 19003 | Bestätigung Weiterverpflichtung | MSBA → NB | 1.1 | 2025-04-17 | 61 |
| 19004 | Ablehnung Weiterverpflichtung | MSBA → NB | 1.1 | 2025-04-17 | 61 |
| 19005 | Bestätigung Auftrag Änderung Technik | MSB → LF, MSB → NB | 1.1 | 2025-04-17 | 66 |
| 19006 | Ablehnung Auftrag Änderung Technik | MSB → LF, MSB → NB | 1.1 | 2025-04-17 | 81 |
| 19007 | Ablehnung Anforderung Werte | MSB → LF, MSB → NB, MSB → MSB (Strom), M | 1.1 | 2025-04-17 | 61 |
| 19009 | Bestätigung Beendigung Rechnungsabwicklung MSB | LF → MSB, MSB → LF | 1.1 | 2025-04-17 | 61 |
| 19010 | Ablehnung Beendigung Rechnungsabwicklung MSB | LF → MSB, MSB → LF | 1.1 | 2025-04-17 | 61 |
| 19011 | Bestätigung der Ab-/Bestellung von Werten | MSB → ESA | 1.1 | 2025-04-17 | 69 |
| 19012 | Ablehnung der Ab-/Bestellung von Werten | MSB → ESA | 1.1 | 2025-04-17 | 59 |
| 19013 | Bestätigung der Stornierung einer Bestellung | MSB → ESA | 1.1 | 2025-04-17 | 54 |
| 19014 | Ablehnung der Stornierung einer Bestellung | MSB → ESA | 1.1 | 2025-04-17 | 54 |
| 19015 | Bestätigung Gerätewechselabsicht | MSBA → MSBN | 1.1 | 2025-04-17 | 68 |
| 19016 | Ablehnung Gerätewechselabsicht | MSBA → MSBN | 1.1 | 2025-04-17 | 66 |
| 19101 | Ablehnung der Anfrage Stammdaten | NB → LF, NB → MSB | 1.1 | 2025-04-17 | 59 |
| 19102 | Ablehnung der Anfrage Werte | MSB → LF (Strom), MSB → , NB → LF (Gas), | 1.1 | 2025-04-17 | 64 |
| 19103 | Ablehnung der Anfrage Brennwert / Zustandszahl | NB → LF | 1.1 | 2025-04-17 | 56 |
| 19104 | Ablehnung der Anfrage vom MSB Gas | NB (Strom) → MSB (Gas) | 1.1 | 2025-04-17 | 54 |
| 19110 | Ablehnung der Anforderung Allokationsliste | NB → LF | 1.1 | 2025-04-17 | 56 |
| 19114 | Ablehnung Reklamation | MSB → LF, MSB → NB, MSB → ÜNB, MSB → MSB | 1.1 | 2025-04-17 | 64 |
| 19115 | Ablehnung der Anforderung bilanzierte Menge | ÜNB → NB | 1.1 | 2025-04-17 | 54 |
| 19116 | Bestätigung Sperr-/Entsperrauftrag | NB → LF | 1.1 | 2025-04-17 | 77 |
| 19117 | Ablehnung Sperr-/Entsperrauftrag | NB → LF | 1.1 | 2025-04-17 | 63 |
| 19118 | Bestätigung Anfrage Sperrung | MSB → NB | 1.1 | 2025-04-17 | 57 |
| 19119 | Ablehnung Anfrage Sperrung | MSB → NB | 1.1 | 2025-04-17 | 60 |
| 19120 | Mitteilung zur Änderung | MSB → NB | 1.1 | 2025-04-17 | 57 |
| 19121 | Mitteilung zur Änderung Prognosegrundlage | NB → LF | 1.1 | 2025-04-17 | 57 |
| 19123 | Ablehnung Reklamation einer Definition | NB → LF, NB → MSB, LF → MSB, LF → NB | 1.1 | 2025-04-17 | 72 |
| 19124 | Mitteilung zur Änderung Zählzeitdefinition | NB → LF, MSB → LF | 1.1 | 2025-04-17 | 58 |
| 19127 | Mitteilung zur Konfigurationsänderung | MSB → MSB | 1.1 | 2025-04-17 | 58 |
| 19128 | Bestätigung Stornierung Sperr-/Entsperrauftrag | NB → LF | 1.1 | 2025-04-17 | 58 |
| 19129 | Ablehnung Stornierung Sperr-/Entsperrauftrag | NB → LF | 1.1 | 2025-04-17 | 58 |
| 19130 | Bearbeitungsstand Reklamation Konfiguration | MSB → NB, MSB → LF, MSB → MSB | 1.1 | 2025-04-17 | 63 |
| 19131 | Mitteilung zur Beendigung Konfiguration | MSB → NB, MSB → LF, MSB → MSB | 1.1 | 2025-04-17 | 59 |
| 19132 | Mitteilung zur Bestellung Konfiguration | MSB → NB, MSB → LF, MSB → MSB | 1.1 | 2025-04-17 | 60 |
| 19133 | Bearbeitungsstand Bestellung Änderung Abrechnungsd | NB → LF | 1.1 | 2025-04-17 | 57 |
| 19204 | Ablehnung Ab-/Bestellung Aggregationsebene | ÜNB → BKV | 1.1 | 2025-04-17 | 55 |
| 19301 | Abl. der Anforderung | NB → UBA | 1.1 | 2025-04-17 | 61 |
| 19302 | Best. der Anforderung zum Beenden des Abos zur Sta | NB → UBA | 1.1 | 2025-04-17 | 60 |
| 21000 | Statusmeldung | LF → NB, LF → ÜNB | 2.0h | 2025-06-23 | 78 |
| 21001 | Statusmeldung | NB → NB | 2.0h | 2025-06-23 | 74 |
| 21002 | Abweisung | BIKO → NB, BIKO → ÜNB | 2.0h | 2025-06-23 | 73 |
| 21003 | Statusmeldung | BIKO → NB, BIKO → ÜNB | 2.0h | 2025-06-23 | 96 |
| 21004 | Statusmeldung | BIKO → BKV, BIKO → NB | 2.0h | 2025-06-23 | 96 |
| 21005 | Statusmeldung | BKV → BIKO, NB → BIKO | 2.0h | 2025-06-23 | 84 |
| 21007 | Statusmeldung | NB → MSBA, NB → LF | 2.0h | 2025-06-23 | 71 |
| 21009 | Statusmeldung | MSBN → NB | 2.0h | 2025-06-23 | 55 |
| 21010 | Statusmeldung | gMSB → NB, MSBN → NB, MSBN → MSBA | 2.0h | 2025-06-23 | 59 |
| 21011 | Statusmeldung | NB → MSBN, NB → MSBA, NB → LF | 2.0h | 2025-06-23 | 64 |
| 21012 | Statusmeldung | NB → MSBN | 2.0h | 2025-06-23 | 65 |
| 21013 | Statusmeldung | NB → MSBN, NB → MSBA, NB → LF | 2.0h | 2025-06-23 | 56 |
| 21015 | Informationsmeldung | NB → MSBA (nur Gas) | 2.0h | 2025-06-23 | 63 |
| 21018 | Statusmeldung | NB → MSBA | 2.0h | 2025-06-23 | 66 |
| 21024 | Statusmeldung | MSB → LF | 2.0h | 2025-06-23 | 57 |
| 21025 | Statusmeldung | MSB → LF | 2.0h | 2025-06-23 | 64 |
| 21026 | Statusmeldung | MSB → NB | 2.0h | 2025-06-23 | 57 |
| 21027 | Statusmeldung | MSB → NB, MSB → MSB | 2.0h | 2025-06-23 | 64 |
| 21028 | Informationsmeldung | MSB → NB (nur Gas) | 2.0h | 2025-06-23 | 59 |
| 21029 | Vorabinformation | gMSB → MSB, gMSB → LF, gMSB → NB | 2.0h | 2025-06-23 | 84 |
| 21030 | iMS-Ersteinbauzust. | MSB → gMSB | 2.0h | 2025-06-23 | 65 |
| 21031 | Bestandss. / Eigenausbau iMS | MSB → gMSB | 2.0h | 2025-06-23 | 61 |
| 21032 | Antwort auf das Angebot | LF → MSB | 2.0h | 2025-06-23 | 59 |
| 21033 | Ablehnung der Anfrage | MSB → ESA, MSB → LF, MSB → NB | 2.0h | 2025-06-23 | 73 |
| 21035 | Rückmeld. a. Liefers. | LF → NB | 2.0h | 2025-06-23 | 87 |
| 21036 | Gerätestatus | MSB → MSB | 2.0h | 2025-06-23 | 57 |
| 21037 | Ansicht NB | NB → BTR | 2.0h | 2025-06-23 | 145 |
| 21038 | Ansicht BTR | BTR → NB | 2.0h | 2025-06-23 | 119 |
| 21039 | Auftragsstatus (Sperren) | NB → LF, NB → MSB, NB → ÜNB | 2.0h | 2025-06-23 | 95 |
| 21040 | Info Entsperrauftrag | NB → MSB | 2.0h | 2025-06-23 | 59 |
| 21042 | Bestellung (WiM) | MSB → ESA | 2.0h | 2025-06-23 | 57 |
| 21043 | Bestellungsantwort / -mitteilung | MSB → LF, MSB → MSB, MSB → NB, NB → LF | 2.0h | 2025-06-23 | 73 |
| 21044 | Bestellungsbeendigung | MSB → NB, MSB → LF | 2.0h | 2025-06-23 | 57 |
| 21045 | EnFG Informationen | LF → NB | 2.0h | 2025-06-23 | 128 |
| 21047 | Bearbeitungsstandsmeldung | LF → MSB, LF → NB, LF → ÜNB, MSB → LF, M | 2.0h | 2025-06-23 | 85 |
| 23001 | Störungsmeldung | LF → MSB, NB → MSB, MSB → MSB | 1.1g | 2025-12-11 | 92 |
| 23003 | Ablehnung | MSB → LF, MSB → NB, MSB → MSB | 1.1g | 2025-12-11 | 61 |
| 23004 | Bestätigung | MSB → LF, MSB → NB, MSB → MSB | 1.1g | 2025-12-11 | 71 |
| 23005 | Informationsmeldung | MSB → NB (Gas), MSB → MSB (Strom) | 1.1g | 2025-12-11 | 64 |
| 23008 | Ergebnisbericht | MSB → LF, MSB → NB, MSB → MSB | 1.1g | 2025-12-11 | 80 |
| 23009 | Informationsmeldung | MSB → NB (Gas), MSB → MSB (Strom) | 1.1g | 2025-12-11 | 79 |
| 23011 | Informationsmeldung | MSB → NB, MSB → LF, MSB → ÜNB | 1.1g | 2025-12-11 | 65 |
| 23012 | Informationsmeldung | MSB → NB, MSB → LF, MSB → ÜNB | 1.1g | 2025-12-11 | 81 |
| 25001 | Berechnungsformel | NB → MSB, NB → LF, NBA → NBN | 1.0 | 2025-12-11 | 127 |
| 25004 | Übermittlung Übersicht Zählzeitdefinitionen | NB → LF, NB → MSB, LF → MSB | 1.0 | 2025-12-11 | 110 |
| 25005 | Übermittlung einer ausgerollten Zählzeitdefinition | NB → LF, NB → MSB, LF → MSB | 1.0 | 2025-12-11 | 78 |
| 25006 | Übermittlung Übersicht Schaltzeitdefinitionen | NB → LF, NB → MSB, LF → NB, LF → MSB | 1.0 | 2025-12-11 | 79 |
| 25007 | Übermittlung Übersicht Leistungskurvendefinitionen | NB → LF, NB → MSB, LF → NB, LF → MSB | 1.0 | 2025-12-11 | 79 |
| 25008 | Übermittlung einer ausgerollten Schaltzeitdefiniti | NB → LF, NB → MSB, LF → NB, LF → MSB | 1.0 | 2025-12-11 | 80 |
| 25009 | Übermittlung einer ausgerollten Leistungskurvendef | NB → LF, NB → MSB, LF → NB, LF → MSB | 1.0 | 2025-12-11 | 80 |
| 25010 | Antwort auf Berechnungsformel | MSB → NB | 1.0 | 2025-12-11 | 61 |
| 27001 | Übermittlung der Ausgleichsenergiepreise | BIKO → BKV | 2.0f | 2025-12-11 | 74 |
| 27002 | Preisblätter MSB-Leistungen | MSB → LF, MSB → NB | 2.0f | 2025-12-11 | 113 |
| 27003 | Preisblätter NB-Leistungen | NB → LF | 2.0f | 2025-12-11 | 96 |
| 29001 | Ablehnung REMADV | NB → LF, MSB → LF, MSB → NB, MSB → ESA | 1.0g | 2025-04-01 | 83 |
| 29002 | Ablehnung IFTSTA | NB → LF | 1.0g | 2025-04-01 | 54 |
| 31001 | Abschlagsrechnung | ReErst → ReEmpf | 1.0 | 2025-06-23 | 169 |
| 31002 | NN-Rechnung | ReErst → ReEmpf | 1.0 | 2025-06-23 | 271 |
| 31003 | WiM-Rechnung | ReErst → ReEmpf | 1.0 | 2025-06-23 | 190 |
| 31004 | Stornorechnung | ReErst → ReEmpf | 1.0 | 2025-06-23 | 192 |
| 31005 | MMM-Rechnung | ReErst → ReEmpf | 1.0 | 2025-06-23 | 186 |
| 31006 | MMM-selbst ausgest. Rechnung | ReErst → ReEmpf | 1.0 | 2025-06-23 | 183 |
| 31007 | Aggreg. MMM-Rechnung | NB → MGV | 1.0 | 2025-06-23 | 164 |
| 31008 | Aggreg. MMM-selbst ausgest. Rechnung | NB → MGV | 1.0 | 2025-06-23 | 164 |
| 31009 | MSB-Rechnung | ReErst → ReEmpf | 1.0 | 2025-06-23 | 186 |
| 31010 | Kapazitätsrechnung | NB → KN | 1.0 | 2025-06-23 | 162 |
| 31011 | Rechnung Sonstige Leistung | ReErst → ReEmpf | 1.0 | 2025-06-23 | 192 |
| 33001 | Bestätigung | ReEmpf → ReErst | 1.0 | 2025-04-01 | 72 |
| 33002 | Abweisung | ReEmpf → ReErst | 1.0 | 2025-04-01 | 108 |
| 33003 | Strom Abweisung Kopf und Summe | ReEmpf → ReErst | 1.0 | 2025-04-01 | 104 |
| 33004 | Strom Abweisung Position | ReEmpf → ReErst | 1.0 | 2025-04-01 | 105 |
| 35001 | Anfrage Geräteübernahmeangebot | MSBN → MSBA | 1.1 | 2025-04-01 | 61 |
| 35002 | Anfrage Rechnungsabwicklung MSB über LF | LF → MSB | 1.1 | 2025-04-01 | 63 |
| 35003 | Anfrage von Werten | ESA → MSB | 1.1 | 2025-04-01 | 91 |
| 35004 | Anfrage einer Konfiguration | NB → MSB, LF → MSB | 1.1 | 2025-04-01 | 147 |
| 35005 | Anfrage Angebot Änderung Technik | NB → MSB, LF → MSB | 1.1 | 2025-04-01 | 108 |
| 37000 | Übermittlung Kommunikationsdaten des LF | LF → LF, LF → NB, LF → MSB, LF → ÜNB | 1.0e | 2024-10-01 | 309 |
| 37001 | Übermittlung Kommunikationsdaten des NB | NB → LF, NB → MSB, NB → NB, NB → BKV, NB | 1.0e | 2024-10-01 | 300 |
| 37002 | Übermittlung Kommunikationsdaten des MSB | MSB → NB, MSB → LF, MSB → ÜNB, MSB → MSB | 1.0e | 2024-10-01 | 246 |
| 37003 | Übermittlung Kommunikationsdaten des BKV | BKV → NB, BKV → BIKO, BKV → ÜNB | 1.0e | 2024-10-01 | 156 |
| 37004 | Übermittlung Kommunikationsdaten des BIKO | BIKO → NB, BIKO → BKV, BIKO → ÜNB | 1.0e | 2024-10-01 | 138 |
| 37005 | Übermittlung Kommunikationsdaten des ÜNB | ÜNB → NB, ÜNB → LF, ÜNB → BKV, ÜNB → BIK | 1.0e | 2024-10-01 | 228 |
| 37006 | Übermittlung Kommunikationsdaten des ESA | ESA → MSB | 1.0e | 2024-10-01 | 174 |
| 39000 | Stornierung Sperr-/Entsperrauftrag | LF → NB | 1.0a | 2024-10-01 | 54 |
| 39001 | Weiterleitung der Stornierung | NB → MSB | 1.0a | 2024-10-01 | 58 |
| 39002 | Stornierung der Bestellung | ESA → MSB | 1.0a | 2024-10-01 | 51 |
| 44001 | Anmeldung NN | LF → NB | 1.0a | 2024-07-26 | 213 |
| 44002 | Bestätigung Anmeldung | NB → LF | 1.0a | 2024-07-26 | 435 |
| 44003 | Ablehnung Anmeldung | NB → LF | 1.0a | 2024-07-26 | 91 |
| 44004 | Abmeldung NN | LF → NB | 1.0a | 2024-07-26 | 77 |
| 44005 | Bestätigung Abmeldung | NB → LF | 1.0a | 2024-07-26 | 82 |
| 44006 | Ablehnung Abmeldung | NB → LF | 1.0a | 2024-07-26 | 73 |
| 44007 | Abmeldung NN vom NB | NB → LF | 1.0a | 2024-07-26 | 66 |
| 44008 | Bestätigung Abmeldung vom NB | LF → NB | 1.0a | 2024-07-26 | 71 |
| 44009 | Ablehnung Abmeldung vom NB | LF → NB | 1.0a | 2024-07-26 | 66 |
| 44010 | Abmeldeanfrage des NB | NB → LF | 1.0a | 2024-07-26 | 72 |
| 44011 | Bestätigung Abmeldeanfrage | LF → NB | 1.0a | 2024-07-26 | 69 |
| 44012 | Ablehnung Abmeldeanfrage | LF → NB | 1.0a | 2024-07-26 | 65 |
| 44013 | Anmeldung EOG | NB → LF | 1.0a | 2024-07-26 | 467 |
| 44014 | Bestätigung EOG Anmeldung | LF → NB | 1.0a | 2024-07-26 | 437 |
| 44015 | Ablehnung EOG Anmeldung | LF → NB | 1.0a | 2024-07-26 | 78 |
| 44016 | Kündigung beim alten Lieferanten | LFN → LFA | 1.0a | 2024-07-26 | 92 |
| 44017 | Bestätigung Kündigung | LFA → LFN | 1.0a | 2024-07-26 | 96 |
| 44018 | Ablehnung Kündigung | LFA → LFN | 1.0a | 2024-07-26 | 84 |
| 44019 | Bestandsliste zugeordnete Marktlokationenen | NB → LF | 1.0a | 2024-07-26 | 150 |
| 44020 | Änderungsmeldung zur Bestandsliste | LF → NB | 1.0a | 2024-07-26 | 160 |
| 44021 | Antwort auf Änderungsmeldung zur Bestandsliste | NB → LF | 1.0a | 2024-07-26 | 155 |
| 44022 | Anfrage nach Stornierung | MSCONS-Nachrichten können von verschiede | 1.0a | 2024-07-26 | 60 |
| 44023 | Bestätigung Anfrage Stornierung | zurück → den Absender | 1.0a | 2024-07-26 | 61 |
| 44024 | Ablehnung Anfrage Stornierung | zurück → den Absender | 1.0a | 2024-07-26 | 64 |
| 44035 | Antwort auf die Geschäftsdatenanfrage | NB → LF | 1.0a | 2024-07-26 | 373 |
| 44036 | Informationsmeldung über existierende Zuordnung | NB → LF | 1.0a | 2024-07-26 | 65 |
| 44037 | Informationsmeldung zur Beendigung der Zuordnung | NB → LF | 1.0a | 2024-07-26 | 63 |
| 44038 | Informationsmeldung zur Aufhebung einer zuk. Zuord | NB → LF | 1.0a | 2024-07-26 | 71 |
| 44039 | Kündigung MSB | MSBN → MSBA | 1.0a | 2024-07-26 | 87 |
| 44040 | Bestätigung Kündigung MSB | MSBA → MSBN | 1.0a | 2024-07-26 | 98 |
| 44041 | Ablehnung Kündigung MSB | MSBA → MSBN | 1.0a | 2024-07-26 | 77 |
| 44042 | Anmeldung MSB | MSB → NB | 1.0a | 2024-07-26 | 111 |
| 44043 | Bestätigung Anmeldung MSB | NB → MSB | 1.0a | 2024-07-26 | 305 |
| 44044 | Ablehnung Anmeldung MSB | NB → MSB | 1.0a | 2024-07-26 | 65 |
| 44051 | Ende MSB | MSB → NB | 1.0a | 2024-07-26 | 68 |
| 44052 | Bestätigung Ende MSB | NB → MSB | 1.0a | 2024-07-26 | 76 |
| 44053 | Ablehnung Ende MSB | NB → MSB | 1.0a | 2024-07-26 | 68 |
| 44060 | Antwort auf die Geschäftsdatenanfrage | NB → MSB | 1.0a | 2024-07-26 | 261 |
| 44096 | Deklarationsliste | NB → MGV | 1.0a | 2024-07-26 | 63 |
| 44097 | Deklarationsliste | MGV → BKV | 1.0a | 2024-07-26 | 69 |
| 44101 | Stammdaten zur Messlokation | NB → MSB | 1.0a | 2024-07-26 | 75 |
| 44102 | Aktualisierte Stammdaten zur Messlokation | NB → MSB | 1.0a | 2024-07-26 | 75 |
| 44103 | Stammdaten zur Marktlokation | NB → LF | 1.0a | 2024-07-26 | 130 |
| 44104 | Aktualisierte Stammdaten zur Marktlokation | NB → LF | 1.0a | 2024-07-26 | 130 |
| 44105 | Ablehnung auf Stammdaten zur Marktlokation | LF → NB | 1.0a | 2024-07-26 | 70 |
| 44109 | Nicht bila.rel. Änderung vom LF | LF → NB [Berechtigter] | 1.0a | 2024-07-26 | 97 |
| 44110 | #nv# Nicht bila.rel. Änderung vom LF | NB [Verteiler] → MSB | 1.0a | 2024-07-26 | 62 |
| 44111 |  | NB [Berechtigter] → LF | 1.0a | 2024-07-26 | 63 |
| 44112 | Nicht bila.rel. Änderung vom NB | NB → LF | 1.0a | 2024-07-26 | 223 |
| 44113 | Nicht bila.rel. Änderung vom NB | NB → MSB | 1.0a | 2024-07-26 | 132 |
| 44115 | Antwort auf Änderung vom NB | LF → NB, MSB → NB | 1.0a | 2024-07-26 | 64 |
| 44116 | Änderung vom MSB mit Abhängig keiten | MSB → NB [Verteiler] | 1.0a | 2024-07-26 | 215 |
| 44117 | Änderung vom MSB mit Abhängig keiten | NB [Verteiler] → LF | 1.0a | 2024-07-26 | 199 |
| 44119 | Antwort auf Änderung vom MSB | NB [Verteiler] → MSB, LF → NB [Verteiler | 1.0a | 2024-07-26 | 64 |
| 44120 | Bila.rel. Änderung vom LF | LF → NB | 1.0a | 2024-07-26 | 70 |
| 44121 | Antwort auf Änderung vom LF | NB → LF | 1.0a | 2024-07-26 | 63 |
| 44123 | Bila.rel. Änderung vom NB mit Abhängigkeiten | NB → LF | 1.0a | 2024-07-26 | 106 |
| 44124 | Antwort auf Änderung vom NB | LF → NB | 1.0a | 2024-07-26 | 63 |
| 44129 | Korrektur Meldepunkt vom NB | NB → LF, NB → ÜNB | 1.0a | 2024-07-26 | 65 |
| 44130 | Korrektur Meldepunkt vom NB | NB → MSB | 1.0a | 2024-07-26 | 65 |
| 44132 | Antwort auf Änderung vom NB | LF → NB, ÜNB → NB, MSB → NB | 1.0a | 2024-07-26 | 56 |
| 44137 | Nicht bila.rel. Anfrage an LF | NB [Berechtigt] → LF | 1.0a | 2024-07-26 | 97 |
| 44138 | Antwort auf Anfrage | LF → NB [Berechtigt] | 1.0a | 2024-07-26 | 105 |
| 44139 | Nicht bila.rel. Anfrage an NB | LF → NB | 1.0a | 2024-07-26 | 226 |
| 44140 | Nicht bila.rel. Anfrage an NB | MSB → NB | 1.0a | 2024-07-26 | 131 |
| 44142 | Antwort auf Anfrage | NB → LF, NB → MSB | 1.0a | 2024-07-26 | 244 |
| 44143 | Anfrage an MSB mit Abhängigkeiten | LF → NB [Verteiler] | 1.0a | 2024-07-26 | 199 |
| 44145 | Antwort auf Anfrage | NB [Verteiler] → LF | 1.0a | 2024-07-26 | 207 |
| 44146 | Ablehnung der Anfrage | NB [Verteiler] → LF | 1.0a | 2024-07-26 | 63 |
| 44147 | Anfrage an MSB mit Abhängigkeiten | NB [Verteiler] → MSB | 1.0a | 2024-07-26 | 199 |
| 44148 | Anfrage an MSB mit Abhängigkeiten | NB [Berechtigt] → MSB | 1.0a | 2024-07-26 | 215 |
| 44149 | Antwort auf Anfrage | MSB → NB [Verteiler], MSB → NB [Berechti | 1.0a | 2024-07-26 | 223 |
| 44150 | Bila.rel. Anfrage an LF | NB → LF | 1.0a | 2024-07-26 | 70 |
| 44151 | Antwort auf Anfrage | LF → NB | 1.0a | 2024-07-26 | 78 |
| 44152 | Ablehnung der Anfrage | LF → NB | 1.0a | 2024-07-26 | 63 |
| 44156 | Bila.rel. Anfrage an NB mit Abhängigkeiten | LF → NB | 1.0a | 2024-07-26 | 106 |
| 44157 | Antwort auf Anfrage | NB → LF | 1.0a | 2024-07-26 | 114 |
| 44159 | Änderung vom MSB ohne Abhängigkeiten | MSB → NB [Verteiler] | 1.0a | 2024-07-26 | 100 |
| 44160 | Änderung vom MSB ohne Abhängigkeiten | NB [Verteiler] → LF [Berechtigt] | 1.0a | 2024-07-26 | 76 |
| 44161 | Antwort auf Änderung | NB [Verteiler] → MSB, LF [Berechtigt] →  | 1.0a | 2024-07-26 | 64 |
| 44162 | Anfrage an MSB ohne Abhängigkeiten | LF [Berechtigt] → NB [Verteiler] | 1.0a | 2024-07-26 | 76 |
| 44163 | Antwort auf Anfrage | NB [Verteiler] → LF [Berechtigt] | 1.0a | 2024-07-26 | 84 |
| 44164 | Ablehnung Anfrage | NB [Verteiler] → LF [Berechtigt] | 1.0a | 2024-07-26 | 63 |
| 44165 | Nicht bila.rel. Anfrage an MSB ohne Abhängigkeiten | NB [Verteiler] → MSB | 1.0a | 2024-07-26 | 76 |
| 44166 | Nicht bila.rel. Anfrage an MSB ohne Abhängigkeiten | NB [Berechtigt] → MSB | 1.0a | 2024-07-26 | 100 |
| 44167 | Antwort auf Anfrage | MSB → NB | 1.0a | 2024-07-26 | 108 |
| 44168 | Verpflichtungsanfrage / Aufforderung | NB → gMSB | 1.0a | 2024-07-26 | 318 |
| 44169 | Bestätigung Verpflichtungsanfrage | gMSB → NB | 1.0a | 2024-07-26 | 309 |
| 44170 | Ablehnung Verpflichtungsanfrage | gMSB → NB | 1.0a | 2024-07-26 | 65 |
| 44172 | #nv# Anfrage an MSB mit Abhängigkeiten | MSB → NB [Verteiler] | 1.0a | 2024-07-26 | 145 |
| 44175 | Änderung der Marktlokationsstruktur | NB → LF | 1.0a | 2024-07-26 | 63 |
| 44176 | Antwort auf Änderung der Marktlokationsstruktur | LF → NB | 1.0a | 2024-07-26 | 71 |
| 44180 | Anfrage der Marktlokationsstruktur | LF → NB | 1.0a | 2024-07-26 | 63 |
| 44181 | Antwort auf Anfrage der Marktlokationsstruktur | NB → LF | 1.0a | 2024-07-26 | 71 |
| 44182 | Ablehnung der Anfrage der Marktlokationsstruktur | NB → LF | 1.0a | 2024-07-26 | 63 |
| 55001 | Anmeldung verb. MaLo | LF → NB | 2.1 | 2025-12-11 | 146 |
| 55002 | Bestätigung Anmeldung verb. MaLo | NB → LF | 2.1 | 2025-12-11 | 165 |
| 55003 | Ablehnung Anmeldung verb. MaLo | NB → LF | 2.1 | 2025-12-11 | 83 |
| 55004 | Abmeldung | LF → NB | 2.1 | 2025-12-11 | 83 |
| 55005 | Bestätigung Abmeldung | NB → LF | 2.1 | 2025-12-11 | 75 |
| 55006 | Ablehnung Abmeldung | NB → LF | 2.1 | 2025-12-11 | 70 |
| 55007 | Abmeldung / Beendigung der Zuordnung | NB → LF | 2.1 | 2025-12-11 | 82 |
| 55008 | Bestätigung Abmeldung | LF → NB | 2.1 | 2025-12-11 | 69 |
| 55009 | Ablehnung Abmeldung | LF → NB | 2.1 | 2025-12-11 | 64 |
| 55010 | Anfrage zur Beendigung der Zuordnung | NB → LF | 2.1 | 2025-12-11 | 88 |
| 55011 | Bestätigung Beendigung der Zuordnung | LF → NB | 2.1 | 2025-12-11 | 64 |
| 55012 | Ablehnung Beendigung der Zuordnung | LF → NB | 2.1 | 2025-12-11 | 60 |
| 55013 | Anmeldung / Zuordnung EOG | NB → LF | 2.1 | 2025-12-11 | 257 |
| 55014 | Bestätigung EOG Anmeldung | LF → NB | 2.1 | 2025-12-11 | 159 |
| 55015 | Ablehnung EOG Anmeldung | LF → NB | 2.1 | 2025-12-11 | 74 |
| 55016 | Kündigung | LFN → LFA | 2.1 | 2025-12-11 | 73 |
| 55017 | Bestätigung Kündigung | LFA → LFN | 2.1 | 2025-12-11 | 78 |
| 55018 | Ablehnung Kündigung | LFA → LFN | 2.1 | 2025-12-11 | 80 |
| 55022 | Anfrage nach Stornierung | MSCONS-Nachrichten können von verschiede | 2.1 | 2025-12-11 | 60 |
| 55023 | Bestätigung Anfrage Stornierung | zurück → den Absender | 2.1 | 2025-12-11 | 61 |
| 55024 | Ablehnung Anfrage Stornierung | zurück → den Absender | 2.1 | 2025-12-11 | 64 |
| 55035 | Antwort auf GDA verb. MaLo | NB → LF | 2.1 | 2025-12-11 | 531 |
| 55036 | Existierende Zuordnung | NB → LF | 2.1 | 2025-12-11 | 69 |
| 55037 | Beendigung der Zuordnung | NB → LF | 2.1 | 2025-12-11 | 67 |
| 55038 | Aufhebung einer zuk. Zuordnung | NB → LF | 2.1 | 2025-12-11 | 74 |
| 55039 | Kündigung MSB | MSBN → MSBA | 2.1 | 2025-12-11 | 91 |
| 55040 | Bestätigung Kündigung MSB | MSBA → MSBN | 2.1 | 2025-12-11 | 104 |
| 55041 | Ablehnung Kündigung MSB | MSBA → MSBN | 2.1 | 2025-12-11 | 77 |
| 55042 | Anmeldung MSB | MSB → NB | 2.1 | 2025-12-11 | 116 |
| 55043 | Bestätigung Anmeldung MSB | NB → MSB | 2.1 | 2025-12-11 | 909 |
| 55044 | Ablehnung Anmeldung MSB | NB → MSB | 2.1 | 2025-12-11 | 66 |
| 55051 | Ende MSB | MSB → NB | 2.1 | 2025-12-11 | 68 |
| 55052 | Bestätigung Ende MSB | NB → MSB | 2.1 | 2025-12-11 | 98 |
| 55053 | Ablehnung Ende MSB | NB → MSB | 2.1 | 2025-12-11 | 68 |
| 55060 | Antwort auf GDA | NB → MSB | 2.1 | 2025-12-11 | 608 |
| 55062 | Aktivierung von ZP | NB → BIKO, NB → LF, NB → NB, NB → ÜNB, Ü | 2.1 | 2025-12-11 | 125 |
| 55063 | Deaktivierung von ZP | NB → BIKO, NB → LF, NB → NB, NB → ÜNB, Ü | 2.1 | 2025-12-11 | 56 |
| 55064 | Antwort | BIKO → NB, BIKO → ÜNB, NB → NB | 2.1 | 2025-12-11 | 79 |
| 55065 | Lieferantenclearingliste | NB → LF, ÜNB → LF | 2.1 | 2025-12-11 | 192 |
| 55066 | Korrekturliste zur Lieferantenclearingliste | LF → NB, LF → ÜNB | 2.1 | 2025-12-11 | 210 |
| 55067 | Bilanzkreiszuordnungsliste | NB → BKV, ÜNB → BKV | 2.1 | 2025-12-11 | 111 |
| 55069 | Clearingliste DZR | BIKO → NB, BIKO → ÜNB | 2.1 | 2025-12-11 | 116 |
| 55070 | Clearingliste BAS | BIKO → BKV | 2.1 | 2025-12-11 | 168 |
| 55071 | Aktivierung der Zuordnungsermächtigung | BKV → NB | 2.1 | 2025-12-11 | 75 |
| 55072 | Deaktivierung der Zuordnungsermächtigung | BKV → NB | 2.1 | 2025-12-11 | 75 |
| 55073 | Übermittlung der Profildefinitionen | NB → LF, NB → MSB | 2.1 | 2025-12-11 | 212 |
| 55074 | Stammdaten auf eine ORDERS | NB → UBA | 2.1 | 2025-12-11 | 269 |
| 55075 | Stammdaten aufgrund einer Änderung | NB → UBA | 2.1 | 2025-12-11 | 279 |
| 55076 | Antwort auf Stammdatenänderung | UBA → NB | 2.1 | 2025-12-11 | 287 |
| 55077 | Anmeldung erz. MaLo | LF → NB | 2.1 | 2025-12-11 | 111 |
| 55078 | Bestätigung Anmeldung erz. MaLo | NB → LF | 2.1 | 2025-12-11 | 171 |
| 55080 | Ablehnung Anmeldung erz. MaLo | NB → LF | 2.1 | 2025-12-11 | 89 |
| 55095 | Antwort auf GDA erz. MaLo | NB → LF | 2.1 | 2025-12-11 | 465 |
| 55109 | Änderung Daten der MaLo | LF → NB | 2.1 | 2025-12-11 | 129 |
| 55110 | Änderung Daten der MaLo | LF → MSB | 2.1 | 2025-12-11 | 90 |
| 55126 | Abr.-Daten BK-Abr. verb. Malo | NB → LF, NBA → NBN | 2.1 | 2025-12-11 | 156 |
| 55136 | Rückmeldung/Anfrage Daten der MaLo | MSB → LF | 2.1 | 2025-12-11 | 104 |
| 55137 | Rückmeldung/Anfrage Daten der MaLo | NB → LF | 2.1 | 2025-12-11 | 145 |
| 55156 | Rückmeldung/Anfrage Abr.-Daten BK-Abr. verb. MaLo | LF → NB | 2.1 | 2025-12-11 | 171 |
| 55168 | Verpflichtungsanfrage / Aufforderung | NB → gMSB | 2.1 | 2025-12-11 | 927 |
| 55169 | Bestätigung Verpflichtungsanfrage | gMSB → NB | 2.1 | 2025-12-11 | 908 |
| 55170 | Ablehnung Verpflichtungsanfrage | gMSB → NB | 2.1 | 2025-12-11 | 65 |
| 55173 | Änderung der Lokationsbündelstruktur | NB → MSB | 2.1 | 2025-12-11 | 124 |
| 55175 | Änderung der Lokationsbündelstruktur | NB → LF | 2.1 | 2025-12-11 | 124 |
| 55177 | Rückmeldung/Anfrage Lokationsbündelstruktur | MSB → NB | 2.1 | 2025-12-11 | 138 |
| 55180 | Rückmeldung/Anfrage Lokationsbündelstruktur | LF → NB | 2.1 | 2025-12-11 | 138 |
| 55194 | Antwort auf GDA (Strom an Gas) | NB → MSB | 2.1 | 2025-12-11 | 95 |
| 55195 | Bilanzierungsgebietsclearingliste | ÜNB → NB | 2.1 | 2025-12-11 | 199 |
| 55196 | Antwort auf Bilanzierungsgebietsclearingliste | NB → ÜNB | 2.1 | 2025-12-11 | 299 |
| 55197 | Aktivierung ZP tägliche AAÜZ | NB (ANB) → ÜNB | 2.1 | 2025-12-11 | 84 |
| 55198 | Deaktivierung tägliche AAÜZ | NB (ANB) → ÜNB | 2.1 | 2025-12-11 | 56 |
| 55199 | Aktivierung ZP LF-AASZR | NB (ANB) → LF | 2.1 | 2025-12-11 | 84 |
| 55200 | Deaktivierung ZP LF-AASZR | NB (ANB) → LF | 2.1 | 2025-12-11 | 56 |
| 55201 | LF-AACL | NB (ANB) → LF | 2.1 | 2025-12-11 | 114 |
| 55202 | Korrekturliste LF-AACL | LF → NB (ANB) | 2.1 | 2025-12-11 | 128 |
| 55203 | Aktivierung ZP monatliche AAÜZ | NB (ANB) → BIKO | 2.1 | 2025-12-11 | 88 |
| 55204 | Antwort auf Aktivierung ZP | BIKO → NB (ANB) | 2.1 | 2025-12-11 | 64 |
| 55205 | Weiterleitung Aktivierung ZP | BIKO → BKV (des LF) | 2.1 | 2025-12-11 | 88 |
| 55206 | Deaktivierung ZP monatliche AAÜZ | NB (ANB) → BIKO | 2.1 | 2025-12-11 | 56 |
| 55207 | Antwort auf Deaktivierung ZP | BIKO → NB (ANB) | 2.1 | 2025-12-11 | 64 |
| 55208 | Weiterleitung Deaktivierung ZP | BIKO → BKV (des LF) | 2.1 | 2025-12-11 | 56 |
| 55209 | Aktivierung ZP monatliche AAÜZ | NB (ANB) → BIKO | 2.1 | 2025-12-11 | 88 |
| 55210 | Antwort auf Aktivierung ZP | BIKO → NB (ANB) | 2.1 | 2025-12-11 | 64 |
| 55211 | Weiterleitung Aktivierung ZP | BIKO → BKV (des anfNB) | 2.1 | 2025-12-11 | 88 |
| 55212 | Deaktivierung ZP monatliche AAÜZ | NB (ANB) → BIKO | 2.1 | 2025-12-11 | 56 |
| 55213 | Antwort auf Deaktivierung ZP | BIKO → NB (ANB) | 2.1 | 2025-12-11 | 64 |
| 55214 | Weiterleitung Deaktivierung ZP | BIKO → BKV (des anfNB) | 2.1 | 2025-12-11 | 56 |
| 55218 | Abr.-Daten NNA | NB → LF, NBA → NBN | 2.1 | 2025-12-11 | 160 |
| 55220 | Rückmeldung/Anfrage Abr.-Daten NNA | LF → NB | 2.1 | 2025-12-11 | 176 |
| 55223 | DZÜ Liste | ÜNB → NB | 2.1 | 2025-12-11 | 234 |
| 55224 | Antwort auf DZÜ Liste | NB → ÜNB | 2.1 | 2025-12-11 | 143 |
| 55225 | Änderung Blindabr.-Daten der NeLo | NB → LF, NBA → NBN | 2.1 | 2025-12-11 | 87 |
| 55227 | Rückmeldung/Anfrage Blindabr.-Daten der NeLo | LF → NB | 2.1 | 2025-12-11 | 100 |
| 55230 | Änderung Blindabr.-Daten der NeLo | LF → NB | 2.1 | 2025-12-11 | 77 |
| 55232 | Rückmeldung/Anfrage Blindabr.-Daten der NeLo | NB → LF | 2.1 | 2025-12-11 | 90 |
| 55235 | Zuordnung ZP der NGZ zur NZR | NB → NB, NB → ÜNB | 2.1 | 2025-12-11 | 84 |
| 55236 | Beendigung Zuordnung ZP der NGZ zur NZR | NB → NB, NB → ÜNB | 2.1 | 2025-12-11 | 56 |
| 55237 | Antwort | NB → NB | 2.1 | 2025-12-11 | 72 |
| 55238 | Anmeldung in Modell 2 | NB (LPB) → NB (VNB) | 2.1 | 2025-12-11 | 76 |
| 55239 | Antwort auf Anmeldung | NB (VNB) → NB (LPB) | 2.1 | 2025-12-11 | 104 |
| 55240 | Beendigung der Zuordnung zur MaLo | NB (VNB) → LF | 2.1 | 2025-12-11 | 67 |
| 55241 | Antwort auf Beendigung | LF → NB (VNB) | 2.1 | 2025-12-11 | 75 |
| 55242 | Abmeldung aus dem Modell 2 | NB (LPB) → NB (VNB) | 2.1 | 2025-12-11 | 70 |
| 55243 | Antwort auf Abmeldung | NB (VNB) → NB (LPB) | 2.1 | 2025-12-11 | 78 |
| 55553 | Daten auf individuelle Bestellung | MSB → NB, MSB → LF, MSB → MSB | 2.1 | 2025-12-11 | 171 |
| 55555 | Rückmeldung/Anfrage Daten der individuellen Bestel | NB → MSB, LF → MSB, MSB → MSB | 2.1 | 2025-12-11 | 186 |
| 55557 | Änderung MSB-Abr.-Daten der MaLo | MSB → NB | 2.1 | 2025-12-11 | 88 |
| 55559 | Rückmeldung/Anfrage MSB-Abr.-Daten der MaLo | NB → MSB | 2.1 | 2025-12-11 | 101 |
| 55600 | Anmeldung neue verb. MaLo | LF → NB | 2.1 | 2025-12-11 | 153 |
| 55601 | Anmeldung neue erz. MaLo | LF → NB | 2.1 | 2025-12-11 | 154 |
| 55602 | Bestätigung Anmeldung neue verb. MaLo | NB → LF | 2.1 | 2025-12-11 | 159 |
| 55603 | Bestätigung Anmeldung neue erz. MaLo | NB → LF | 2.1 | 2025-12-11 | 170 |
| 55604 | Ablehnung Anmeldung neue verb. MaLo | NB → LF | 2.1 | 2025-12-11 | 73 |
| 55605 | Ablehnung Anmeldung neue erz. MaLo | NB → LF | 2.1 | 2025-12-11 | 73 |
| 55607 | (Ankündigung) Zuordnung des LF zur erz. MaLo/ Tran | NB → LF | 2.1 | 2025-12-11 | 186 |
| 55608 | Bestätigung Zuordnung des LF zur erz. MaLo/ Tranch | LF → NB | 2.1 | 2025-12-11 | 111 |
| 55609 | Ablehnung Zuordnung des LF zur erz. MaLo/ Tranche | LF → NB | 2.1 | 2025-12-11 | 69 |
| 55611 | Beendigung der Zuordnung | NB → MSB, NB → MSBZ | 2.1 | 2025-12-11 | 68 |
| 55613 | Abr.-Daten BK-Abr. verb. MaLo | NB → ÜNB | 2.1 | 2025-12-11 | 131 |
| 55614 | Rückmeldung/Anfrage Abr.-Daten BK-Abr. verb. MaLo | ÜNB → NB | 2.1 | 2025-12-11 | 143 |
| 55615 | Änderung Daten der NeLo | NB → LF, NBA → NBN | 2.1 | 2025-12-11 | 81 |
| 55616 | Änderung Daten der MaLo | NB → LF, NBA → NBN | 2.1 | 2025-12-11 | 229 |
| 55617 | Änderung Daten der TR | NB → LF, NBA → NBN | 2.1 | 2025-12-11 | 142 |
| 55618 | Änderung Daten der SR | NB → LF, NBA → NBN | 2.1 | 2025-12-11 | 81 |
| 55619 | Änderung Daten der Tranche | NB → LF, NBA → NBN | 2.1 | 2025-12-11 | 78 |
| 55620 | Änderung Daten der MeLo | NB → LF, NBA → NBN | 2.1 | 2025-12-11 | 89 |
| 55621 | Rückmeldung/Anfrage Daten zur NeLo | LF → NB | 2.1 | 2025-12-11 | 94 |
| 55622 | Rückmeldung/Anfrage Daten der MaLo | LF → NB | 2.1 | 2025-12-11 | 249 |
| 55623 | Rückmeldung/Anfrage Daten der TR | LF → NB | 2.1 | 2025-12-11 | 155 |
| 55624 | Rückmeldung/Anfrage Daten der SR | LF → NB | 2.1 | 2025-12-11 | 94 |
| 55625 | Rückmeldung/Anfrage Daten der Tranche | LF → NB | 2.1 | 2025-12-11 | 91 |
| 55626 | Rückmeldung/Anfrage Daten der MeLo | LF → NB | 2.1 | 2025-12-11 | 102 |
| 55627 | Änderung Daten der NeLo | NB → MSB | 2.1 | 2025-12-11 | 81 |
| 55628 | Änderung Daten der MaLo | NB → MSB | 2.1 | 2025-12-11 | 223 |
| 55629 | Änderung Daten der TR | NB → MSB | 2.1 | 2025-12-11 | 134 |
| 55630 | Änderung Daten der SR | NB → MSB | 2.1 | 2025-12-11 | 81 |
| 55632 | Änderung Daten der MeLo | NB → MSB | 2.1 | 2025-12-11 | 92 |
| 55633 | Rückmeldung/Anfrage Daten zur NeLo | MSB → NB | 2.1 | 2025-12-11 | 94 |
| 55634 | Rückmeldung/Anfrage Daten der MaLo | MSB → NB | 2.1 | 2025-12-11 | 243 |
| 55635 | Rückmeldung/Anfrage Daten der TR | MSB → NB | 2.1 | 2025-12-11 | 147 |
| 55636 | Rückmeldung/Anfrage Daten der SR | MSB → NB | 2.1 | 2025-12-11 | 94 |
| 55638 | Rückmeldung/Anfrage Daten der MeLo | MSB → NB | 2.1 | 2025-12-11 | 105 |
| 55639 | Änderung Daten der NeLo | MSB → NB | 2.1 | 2025-12-11 | 116 |
| 55640 | Änderung Daten der MaLo | MSB → NB | 2.1 | 2025-12-11 | 131 |
| 55641 | Änderung Daten der SR | MSB → NB | 2.1 | 2025-12-11 | 102 |
| 55642 | Änderung Daten der Tranche | MSB → NB | 2.1 | 2025-12-11 | 82 |
| 55643 | Änderung Daten der MeLo | MSB → NB | 2.1 | 2025-12-11 | 301 |
| 55644 | Rückmeldung/Anfrage Daten der NeLo | NB → MSB | 2.1 | 2025-12-11 | 131 |
| 55645 | Rückmeldung/Anfrage Daten der MaLo | NB → MSB | 2.1 | 2025-12-11 | 146 |
| 55646 | Rückmeldung/Anfrage Daten der SR | NB → MSB | 2.1 | 2025-12-11 | 116 |
| 55647 | Rückmeldung/Anfrage Daten der Tranche | NB → MSB | 2.1 | 2025-12-11 | 95 |
| 55648 | Rückmeldung/Anfrage Daten der MeLo | NB → MSB | 2.1 | 2025-12-11 | 325 |
| 55649 | Änderung Daten der NeLo | MSB → LF | 2.1 | 2025-12-11 | 117 |
| 55650 | Änderung Daten der MaLo | MSB → LF | 2.1 | 2025-12-11 | 131 |
| 55651 | Änderung Daten der SR | MSB → LF | 2.1 | 2025-12-11 | 102 |
| 55652 | Änderung Daten der Tranche | MSB → LF | 2.1 | 2025-12-11 | 82 |
| 55653 | Änderung Daten der MeLo | MSB → LF | 2.1 | 2025-12-11 | 202 |
| 55654 | Rückmeldung/Anfrage Daten der NeLo | LF → MSB | 2.1 | 2025-12-11 | 132 |
| 55655 | Rückmeldung/Anfrage Daten der MaLo | LF → MSB | 2.1 | 2025-12-11 | 146 |
| 55656 | Rückmeldung/Anfrage Daten der SR | LF → MSB | 2.1 | 2025-12-11 | 116 |
| 55657 | Rückmeldung/Anfrage Daten der Tranche | LF → MSB | 2.1 | 2025-12-11 | 95 |
| 55658 | Rückmeldung/Anfrage Daten der MeLo | LF → MSB | 2.1 | 2025-12-11 | 220 |
| 55659 | Änderung Daten der NeLo | MSB → weiteren MSB | 2.1 | 2025-12-11 | 123 |
| 55660 | Änderung Daten der MaLo | MSB → weiteren MSB | 2.1 | 2025-12-11 | 147 |
| 55661 | Änderung Daten der SR | MSB → weiteren MSB | 2.1 | 2025-12-11 | 103 |
| 55662 | Änderung Daten der Tranche | MSB → weiteren MSB | 2.1 | 2025-12-11 | 94 |
| 55663 | Änderung Daten der MeLo | MSB → weiteren MSB | 2.1 | 2025-12-11 | 301 |
| 55664 | Rückmeldung/Anfrage Daten der NeLo | weiterer MSB → MSB | 2.1 | 2025-12-11 | 138 |
| 55665 | Rückmeldung/Anfrage Daten der MaLo | weiteren MSB → MSB | 2.1 | 2025-12-11 | 162 |
| 55666 | Rückmeldung/Anfrage Daten der SR | weiterer MSB → MSB | 2.1 | 2025-12-11 | 117 |
| 55667 | Rückmeldung/Anfrage Daten der Tranche | weiteren MSB → MSB | 2.1 | 2025-12-11 | 107 |
| 55669 | Rückmeldung/Anfrage Daten der MeLo | weiterer MSB → MSB | 2.1 | 2025-12-11 | 329 |
| 55670 | Stammdaten BK-Treue | NB → ÜNB | 2.1 | 2025-12-11 | 121 |
| 55671 | Rückmeldung auf Stammdaten BK-Treue | ÜNB → NB | 2.1 | 2025-12-11 | 128 |
| 55672 | Abr.-Daten BK-Abr. erz. Malo | NB → LF, NBA → NBN | 2.1 | 2025-12-11 | 178 |
| 55673 | Rückmeldung/Anfrage Abr.-Daten BK-Abr. erz. Malo | LF → NB | 2.1 | 2025-12-11 | 195 |
| 55674 | Abr.-Daten BK-Abr. erz. Malo | NB → ÜNB | 2.1 | 2025-12-11 | 133 |
| 55675 | Rückmeldung/Anfrage Abr.-Daten BK-Abr. erz. Malo | ÜNB → NB | 2.1 | 2025-12-11 | 145 |
| 55684 | Änderung Daten der MaLo | MSB → ÜNB | 2.1 | 2025-12-11 | 82 |
| 55685 | Rückmeldung/Anfrage Daten der MaLo | ÜNB → MSB | 2.1 | 2025-12-11 | 95 |
| 55686 | Änderung Daten der Tranche | MSB → ÜNB | 2.1 | 2025-12-11 | 82 |
| 55687 | Rückmeldung/Anfrage Daten der Tranche | ÜNB → MSB | 2.1 | 2025-12-11 | 95 |
| 55688 | Änderung Daten der MaLo | NB → ÜNB | 2.1 | 2025-12-11 | 78 |
| 55689 | Rückmeldung/Anfrage Daten der MaLo | ÜNB → NB | 2.1 | 2025-12-11 | 91 |
| 55690 | Lokationsbündelstruktur und DB | NBA → NBN | 2.1 | 2025-12-11 | 223 |
| 55691 | Änderung Paket-ID der Malo | NBA → LF, NBA → MSB, NBA → NBN, NBA → ÜN | 2.1 | 2025-12-11 | 76 |
| 55692 | Rückmeldung/Anfrage Paket-ID der Malo | LF → NBA, MSB → NBA, ÜNB → NBA | 2.1 | 2025-12-11 | 90 |

## FV2604 — All Prüfidentifikatoren

| Prüfi | Description | Direction | Version | Date | Lines |
|-------|-------------|-----------|---------|------|-------|
| 13002 | Zählerstand (Gas) | MSCONS-Nachrichten können von verschiede | 3.1g | 2025-10-01 | 191 |
| 13003 | Summenzeitreihe | MSCONS-Nachrichten können von verschiede | 3.1g | 2025-10-01 | 102 |
| 13005 | EEG-Überführungs-ZR | MSCONS-Nachrichten können von verschiede | 3.1g | 2025-10-01 | 110 |
| 13006 | Messwert Storno | MSCONS-Nachrichten können von verschiede | 3.1g | 2025-10-01 | 84 |
| 13007 | Gasbeschaffenheit | MSCONS-Nachrichten können von verschiede | 3.1g | 2025-10-01 | 167 |
| 13008 | Lastgang (Gas) | MSCONS-Nachrichten können von verschiede | 3.1g | 2025-10-01 | 181 |
| 13009 | Energiemenge (Gas) | MSCONS-Nachrichten können von verschiede | 3.1g | 2025-10-01 | 177 |
| 13010 | normiertes Profil | MSCONS-Nachrichten können von verschiede | 3.1g | 2025-10-01 | 93 |
| 13011 | Profilschar | MSCONS-Nachrichten können von verschiede | 3.1g | 2025-10-01 | 90 |
| 13012 | TEP vergh. Werte Referenzmessung | MSCONS-Nachrichten können von verschiede | 3.1g | 2025-10-01 | 93 |
| 13013 | marktlokations- scharfe Allokationsliste Gas (MMMA | MSCONS-Nachrichten können von verschiede | 3.1g | 2025-10-01 | 101 |
| 13014 | marktlokations- scharfe bilanzierte Menge Strom /  | MSCONS-Nachrichten können von verschiede | 3.1g | 2025-10-01 | 97 |
| 13015 | Arbeit Leistungsmax. Kalenderjahr vor Lieferbeginn | MSCONS-Nachrichten können von verschiede | 3.1g | 2025-10-01 | 104 |
| 13016 | Energiemenge u. Leistungsmax. (Strom) | MSCONS-Nachrichten können von verschiede | 3.1g | 2025-10-01 | 163 |
| 13017 | Zählerstand (Strom) | MSCONS-Nachrichten können von verschiede | 3.1g | 2025-10-01 | 168 |
| 13018 | Lastgang Messlokation, Netzkoppelpunkt, Netzlokati | MSCONS-Nachrichten können von verschiede | 3.1g | 2025-10-01 | 163 |
| 13019 | Energiemenge (Strom) | MSCONS-Nachrichten können von verschiede | 3.1g | 2025-10-01 | 168 |
| 13020 | Ausfallarbeitsüberführungszeitreihe | MSCONS-Nachrichten können von verschiede | 3.1g | 2025-10-01 | 107 |
| 13021 | Übermittlung von meteorologischen Daten | MSCONS-Nachrichten können von verschiede | 3.1g | 2025-10-01 | 103 |
| 13022 | Redispatch 2.0 Einzelzeitreihe Ausfallarbeit | MSCONS-Nachrichten können von verschiede | 3.1g | 2025-10-01 | 107 |
| 13023 | Redispatch 2.0 Ausfallarbeitssummenzeitreihe | MSCONS-Nachrichten können von verschiede | 3.1g | 2025-10-01 | 98 |
| 13025 | Lastgang Marktlokation, Tranche | MSCONS-Nachrichten können von verschiede | 3.1g | 2025-10-01 | 163 |
| 13026 | EEG-Überführungs-ZR aufgrund Ausfallarbeit | MSCONS-Nachrichten können von verschiede | 3.1g | 2025-10-01 | 111 |
| 13027 | Werte nach Typ 2 | MSCONS-Nachrichten können von verschiede | 3.1g | 2025-10-01 | 99 |
| 13028 | Grundlage POG-Ermittlung | MSCONS-Nachrichten können von verschiede | 3.1g | 2025-10-01 | 89 |
| 15001 | Angebot Geräteübernahme | MSBA → MSBN | 1.1 | 2025-04-01 | 221 |
| 15002 | Angebot Abrechnung Messstellenbetrieb MSB | MSB → LF | 1.1 | 2025-04-01 | 93 |
| 15003 | Angebot zur Anfrage von Werten | MSB → ESA | 1.1 | 2025-04-01 | 128 |
| 15004 | Angebot einer Konfiguration | MSB → NB, MSB → LF | 1.1 | 2025-04-01 | 138 |
| 15005 | Angebot Änderung Technik | MSB → NB, MSB → LF | 1.1 | 2025-04-01 | 140 |
| 17001 | Bestellung Geräteübernahmeangebot | MSBN → MSBA | 1.1a | 2025-10-01 | 63 |
| 17002 | Weiterverpflichtung | NB → MSBA | 1.1a | 2025-10-01 | 62 |
| 17003 | Beauftragung Änderung Technik | LF → MSB, NB → MSB | 1.1a | 2025-10-01 | 78 |
| 17004 | Anforderung von Werten | LF → MSB (Strom), LF → , NB → MSB (Strom | 1.1a | 2025-10-01 | 68 |
| 17005 | Bestellung Rechnungsabwicklung MSB über LF | LF → MSB | 1.1a | 2025-10-01 | 62 |
| 17006 | Beendigung Rechnungsabwicklung MSB über LF | LF → MSB, LF → , MSB → LF | 1.1a | 2025-10-01 | 65 |
| 17007 | Bestellung von Werten | ESA → MSB | 1.1a | 2025-10-01 | 57 |
| 17008 | Abbestellung von Werten | ESA → MSB | 1.1a | 2025-10-01 | 56 |
| 17009 | Anzeige Gerätewechselabsicht | MSBN → MSBA | 1.1a | 2025-10-01 | 77 |
| 17011 | Bestellung Angebot Änderung Technik | NB → MSB, LF → MSB | 1.1a | 2025-10-01 | 125 |
| 17101 | Anfrage Stammdaten Marktlokation (Gas) | LF → NB (Gas) | 1.1a | 2025-10-01 | 80 |
| 17102 | Anfrage von Werten | LF → MSB (Strom), LF → , LF → NB (Gas),  | 1.1a | 2025-10-01 | 71 |
| 17103 | Anforderung Brennwert / Zustandszahl | LF → NB | 1.1a | 2025-10-01 | 65 |
| 17104 | Anfrage vom MSB Gas | MSB (Gas) → NB (Strom) | 1.1a | 2025-10-01 | 60 |
| 17110 | Anforderung Allokationsliste | LF → NB | 1.1a | 2025-10-01 | 53 |
| 17111 | Bestellanforderung Änderung Prognosegrundlage/ Ger | LF → NB | 1.1a | 2025-10-01 | 66 |
| 17112 | Bestellanforderung Änderung Gerätekonfiguration | NB → MSB | 1.1a | 2025-10-01 | 86 |
| 17113 | Reklamation von Werten | LF → MSB (Strom), LF → , NB → MSB (Strom | 1.1a | 2025-10-01 | 90 |
| 17114 | Anforderung bilanzierte Menge | NB → ÜNB | 1.1a | 2025-10-01 | 63 |
| 17115 | Sperrauftrag | LF → NB | 1.1a | 2025-10-01 | 76 |
| 17116 | Anfrage Sperrung | NB → MSB | 1.1a | 2025-10-01 | 72 |
| 17117 | Entsperrauftrag | LF → NB | 1.1a | 2025-10-01 | 71 |
| 17118 | Bestellung einer Konfigurationsänderung | MSB → MSB | 1.1a | 2025-10-01 | 88 |
| 17120 | Bestellung Änderung Prognosegrundlage | LF → NB | 1.1a | 2025-10-01 | 65 |
| 17121 | Bestellung Änderung | NB → MSB | 1.1a | 2025-10-01 | 174 |
| 17122 | Reklamation einer Definition | LF → NB, MSB → NB, MSB → LF, NB → LF | 1.1a | 2025-10-01 | 78 |
| 17123 | Bestellung Änderung Zählzeitdefinition | LF → NB, LF → MSB | 1.1a | 2025-10-01 | 73 |
| 17124 | Weiterleitung/Bestellung Änderung Zählzeitdefiniti | NB → MSB | 1.1a | 2025-10-01 | 58 |
| 17125 | Bestellung Konfigurationsänderung aufgrund Änderun | MSB → MSB | 1.1a | 2025-10-01 | 55 |
| 17126 | Anfrage Stammdaten Messlokation (Gas) | MSB → NB (Gas) | 1.1a | 2025-10-01 | 77 |
| 17128 | Reklamation einer Konfiguration | NB → MSB, LF → MSB, MSB → MSB | 1.1a | 2025-10-01 | 148 |
| 17129 | Bestellung Beendigung einer Konfiguration | NB → MSB, LF → MSB, MSB → MSB | 1.1a | 2025-10-01 | 58 |
| 17130 | Bestellung einer Konfiguration | NB → MSB, LF → MSB, MSB → MSB | 1.1a | 2025-10-01 | 135 |
| 17131 | Bestellung Angebot einer Konfiguration | NB → MSB, LF → MSB | 1.1a | 2025-10-01 | 50 |
| 17132 | Anfrage Stammdaten (Strom) | LF → NB, MSB → NB | 1.1a | 2025-10-01 | 52 |
| 17133 | Bestellung Änderung Abrechnungsdaten | LF → NB | 1.1a | 2025-10-01 | 81 |
| 17134 | Einrichtung Konfiguration Zuordnung LF von NB | NB → MSB | 1.1a | 2025-10-01 | 199 |
| 17135 | Einrichtung Konfiguration Zuordnung LF von MSB | MSB → MSB | 1.1a | 2025-10-01 | 112 |
| 17201 | Anforder. normierter Profile und Profilscharen | LF → NB | 1.1a | 2025-10-01 | 58 |
| 17202 | Anforder. Lieferantenclearingliste | LF → NB, LF → ÜNB | 1.1a | 2025-10-01 | 69 |
| 17203 | Anforder. Bilanzkreiszuordnungsliste | BKV → NB, BKV → ÜNB | 1.1a | 2025-10-01 | 69 |
| 17204 | Anforder. Clearingliste BAS | BKV → BIKO | 1.1a | 2025-10-01 | 63 |
| 17205 | Anforder. Clearingliste DZR | NB → BIKO | 1.1a | 2025-10-01 | 63 |
| 17206 | Anforderung Bilanzierungsgebiets clearingliste | NB → ÜNB | 1.1a | 2025-10-01 | 69 |
| 17207 | Ab-/Bestellung BK-SZR auf Aggregationsebene RZ | BKV → ÜNB | 1.1a | 2025-10-01 | 60 |
| 17208 | Anforderung Clearingliste ÜNB-DZR | ÜNB → BIKO | 1.1a | 2025-10-01 | 63 |
| 17209 | Anforderung Ausfallarbeit | anfNB → ANB | 1.1a | 2025-10-01 | 67 |
| 17210 | Anforderung Lieferantenausfallarbeitsclearingliste | LF → NB | 1.1a | 2025-10-01 | 69 |
| 17211 | Reklamation Profile bzw. Profilscharen | LF → NB | 1.1a | 2025-10-01 | 54 |
| 17301 | Anforderung von Stammdaten bzw. Messwerten | UBA → NB | 1.1a | 2025-10-01 | 62 |
| 19001 | Bestätigung Bestellung | MSBA → MSBN | 1.1a | 2025-10-01 | 61 |
| 19002 | Ablehnung Bestellung | MSBA → MSBN | 1.1a | 2025-10-01 | 61 |
| 19003 | Bestätigung Weiterverpflichtung | MSBA → NB | 1.1a | 2025-10-01 | 61 |
| 19004 | Ablehnung Weiterverpflichtung | MSBA → NB | 1.1a | 2025-10-01 | 61 |
| 19005 | Bestätigung Auftrag Änderung Technik | MSB → LF, MSB → NB | 1.1a | 2025-10-01 | 66 |
| 19006 | Ablehnung Auftrag Änderung Technik | MSB → LF, MSB → NB | 1.1a | 2025-10-01 | 81 |
| 19007 | Ablehnung Anforderung Werte | MSB → LF, MSB → NB, MSB → MSB (Strom), M | 1.1a | 2025-10-01 | 61 |
| 19009 | Bestätigung Beendigung Rechnungsabwicklung MSB | LF → MSB, MSB → LF | 1.1a | 2025-10-01 | 61 |
| 19010 | Ablehnung Beendigung Rechnungsabwicklung MSB | LF → MSB, MSB → LF | 1.1a | 2025-10-01 | 61 |
| 19011 | Bestätigung der Ab-/Bestellung von Werten | MSB → ESA | 1.1a | 2025-10-01 | 69 |
| 19012 | Ablehnung der Ab-/Bestellung von Werten | MSB → ESA | 1.1a | 2025-10-01 | 59 |
| 19013 | Bestätigung der Stornierung einer Bestellung | MSB → ESA | 1.1a | 2025-10-01 | 54 |
| 19014 | Ablehnung der Stornierung einer Bestellung | MSB → ESA | 1.1a | 2025-10-01 | 54 |
| 19015 | Bestätigung Gerätewechselabsicht | MSBA → MSBN | 1.1a | 2025-10-01 | 68 |
| 19016 | Ablehnung Gerätewechselabsicht | MSBA → MSBN | 1.1a | 2025-10-01 | 66 |
| 19101 | Ablehnung der Anfrage Stammdaten | NB → LF, NB → MSB | 1.1a | 2025-10-01 | 59 |
| 19102 | Ablehnung der Anfrage Werte | MSB → LF (Strom), MSB → , NB → LF (Gas), | 1.1a | 2025-10-01 | 64 |
| 19103 | Ablehnung der Anfrage Brennwert / Zustandszahl | NB → LF | 1.1a | 2025-10-01 | 56 |
| 19104 | Ablehnung der Anfrage vom MSB Gas | NB (Strom) → MSB (Gas) | 1.1a | 2025-10-01 | 54 |
| 19110 | Ablehnung der Anforderung Allokationsliste | NB → LF | 1.1a | 2025-10-01 | 56 |
| 19114 | Ablehnung Reklamation | MSB → LF, MSB → NB, MSB → ÜNB, MSB → MSB | 1.1a | 2025-10-01 | 64 |
| 19115 | Ablehnung der Anforderung bilanzierte Menge | ÜNB → NB | 1.1a | 2025-10-01 | 54 |
| 19116 | Bestätigung Sperr-/Entsperrauftrag | NB → LF | 1.1a | 2025-10-01 | 77 |
| 19117 | Ablehnung Sperr-/Entsperrauftrag | NB → LF | 1.1a | 2025-10-01 | 63 |
| 19118 | Bestätigung Anfrage Sperrung | MSB → NB | 1.1a | 2025-10-01 | 57 |
| 19119 | Ablehnung Anfrage Sperrung | MSB → NB | 1.1a | 2025-10-01 | 60 |
| 19120 | Mitteilung zur Änderung | MSB → NB | 1.1a | 2025-10-01 | 57 |
| 19121 | Mitteilung zur Änderung Prognosegrundlage | NB → LF | 1.1a | 2025-10-01 | 57 |
| 19123 | Ablehnung Reklamation einer Definition | NB → LF, NB → MSB, LF → MSB, LF → NB | 1.1a | 2025-10-01 | 72 |
| 19124 | Mitteilung zur Änderung Zählzeitdefinition | NB → LF, MSB → LF | 1.1a | 2025-10-01 | 58 |
| 19127 | Mitteilung zur Konfigurationsänderung | MSB → MSB | 1.1a | 2025-10-01 | 58 |
| 19128 | Bestätigung Stornierung Sperr-/Entsperrauftrag | NB → LF | 1.1a | 2025-10-01 | 58 |
| 19129 | Ablehnung Stornierung Sperr-/Entsperrauftrag | NB → LF | 1.1a | 2025-10-01 | 58 |
| 19130 | Bearbeitungsstand Reklamation Konfiguration | MSB → NB, MSB → LF, MSB → MSB | 1.1a | 2025-10-01 | 63 |
| 19131 | Mitteilung zur Beendigung Konfiguration | MSB → NB, MSB → LF, MSB → MSB | 1.1a | 2025-10-01 | 59 |
| 19132 | Mitteilung zur Bestellung Konfiguration | MSB → NB, MSB → LF, MSB → MSB | 1.1a | 2025-10-01 | 60 |
| 19133 | Bearbeitungsstand Bestellung Änderung Abrechnungsd | NB → LF | 1.1a | 2025-10-01 | 57 |
| 19204 | Ablehnung Ab-/Bestellung Aggregationsebene | ÜNB → BKV | 1.1a | 2025-10-01 | 55 |
| 19301 | Abl. der Anforderung | NB → UBA | 1.1a | 2025-10-01 | 61 |
| 19302 | Best. der Anforderung zum Beenden des Abos zur Sta | NB → UBA | 1.1a | 2025-10-01 | 60 |
| 21000 | Statusmeldung | LF → NB, LF → ÜNB | 2.0h | 2025-06-23 | 78 |
| 21001 | Statusmeldung | NB → NB | 2.0h | 2025-06-23 | 74 |
| 21002 | Abweisung | BIKO → NB, BIKO → ÜNB | 2.0h | 2025-06-23 | 73 |
| 21003 | Statusmeldung | BIKO → NB, BIKO → ÜNB | 2.0h | 2025-06-23 | 96 |
| 21004 | Statusmeldung | BIKO → BKV, BIKO → NB | 2.0h | 2025-06-23 | 96 |
| 21005 | Statusmeldung | BKV → BIKO, NB → BIKO | 2.0h | 2025-06-23 | 84 |
| 21007 | Statusmeldung | NB → MSBA, NB → LF | 2.0h | 2025-06-23 | 71 |
| 21009 | Statusmeldung | MSBN → NB | 2.0h | 2025-06-23 | 55 |
| 21010 | Statusmeldung | gMSB → NB, MSBN → NB, MSBN → MSBA | 2.0h | 2025-06-23 | 59 |
| 21011 | Statusmeldung | NB → MSBN, NB → MSBA, NB → LF | 2.0h | 2025-06-23 | 64 |
| 21012 | Statusmeldung | NB → MSBN | 2.0h | 2025-06-23 | 65 |
| 21013 | Statusmeldung | NB → MSBN, NB → MSBA, NB → LF | 2.0h | 2025-06-23 | 56 |
| 21015 | Informationsmeldung | NB → MSBA (nur Gas) | 2.0h | 2025-06-23 | 63 |
| 21018 | Statusmeldung | NB → MSBA | 2.0h | 2025-06-23 | 66 |
| 21024 | Statusmeldung | MSB → LF | 2.0h | 2025-06-23 | 57 |
| 21025 | Statusmeldung | MSB → LF | 2.0h | 2025-06-23 | 64 |
| 21026 | Statusmeldung | MSB → NB | 2.0h | 2025-06-23 | 57 |
| 21027 | Statusmeldung | MSB → NB, MSB → MSB | 2.0h | 2025-06-23 | 64 |
| 21028 | Informationsmeldung | MSB → NB (nur Gas) | 2.0h | 2025-06-23 | 59 |
| 21029 | Vorabinformation | gMSB → MSB, gMSB → LF, gMSB → NB | 2.0h | 2025-06-23 | 84 |
| 21030 | iMS-Ersteinbauzust. | MSB → gMSB | 2.0h | 2025-06-23 | 65 |
| 21031 | Bestandss. / Eigenausbau iMS | MSB → gMSB | 2.0h | 2025-06-23 | 61 |
| 21032 | Antwort auf das Angebot | LF → MSB | 2.0h | 2025-06-23 | 59 |
| 21033 | Ablehnung der Anfrage | MSB → ESA, MSB → LF, MSB → NB | 2.0h | 2025-06-23 | 73 |
| 21035 | Rückmeld. a. Liefers. | LF → NB | 2.0h | 2025-06-23 | 87 |
| 21036 | Gerätestatus | MSB → MSB | 2.0h | 2025-06-23 | 57 |
| 21037 | Ansicht NB | NB → BTR | 2.0h | 2025-06-23 | 145 |
| 21038 | Ansicht BTR | BTR → NB | 2.0h | 2025-06-23 | 119 |
| 21039 | Auftragsstatus (Sperren) | NB → LF, NB → MSB, NB → ÜNB | 2.0h | 2025-06-23 | 95 |
| 21040 | Info Entsperrauftrag | NB → MSB | 2.0h | 2025-06-23 | 59 |
| 21042 | Bestellung (WiM) | MSB → ESA | 2.0h | 2025-06-23 | 57 |
| 21043 | Bestellungsantwort / -mitteilung | MSB → LF, MSB → MSB, MSB → NB, NB → LF | 2.0h | 2025-06-23 | 73 |
| 21044 | Bestellungsbeendigung | MSB → NB, MSB → LF | 2.0h | 2025-06-23 | 57 |
| 21045 | EnFG Informationen | LF → NB | 2.0h | 2025-06-23 | 128 |
| 21047 | Bearbeitungsstandsmeldung | LF → MSB, LF → NB, LF → ÜNB, MSB → LF, M | 2.0h | 2025-06-23 | 85 |
| 23001 | Störungsmeldung | LF → MSB, NB → MSB, MSB → MSB | 1.1g | 2025-12-11 | 92 |
| 23003 | Ablehnung | MSB → LF, MSB → NB, MSB → MSB | 1.1g | 2025-12-11 | 61 |
| 23004 | Bestätigung | MSB → LF, MSB → NB, MSB → MSB | 1.1g | 2025-12-11 | 71 |
| 23005 | Informationsmeldung | MSB → NB (Gas), MSB → MSB (Strom) | 1.1g | 2025-12-11 | 64 |
| 23008 | Ergebnisbericht | MSB → LF, MSB → NB, MSB → MSB | 1.1g | 2025-12-11 | 80 |
| 23009 | Informationsmeldung | MSB → NB (Gas), MSB → MSB (Strom) | 1.1g | 2025-12-11 | 79 |
| 23011 | Informationsmeldung | MSB → NB, MSB → LF, MSB → ÜNB | 1.1g | 2025-12-11 | 65 |
| 23012 | Informationsmeldung | MSB → NB, MSB → LF, MSB → ÜNB | 1.1g | 2025-12-11 | 81 |
| 25001 | Berechnungsformel | NB → MSB, NB → LF, NBA → NBN | 1.0 | 2025-12-11 | 127 |
| 25004 | Übermittlung Übersicht Zählzeitdefinitionen | NB → LF, NB → MSB, LF → MSB | 1.0 | 2025-12-11 | 110 |
| 25005 | Übermittlung einer ausgerollten Zählzeitdefinition | NB → LF, NB → MSB, LF → MSB | 1.0 | 2025-12-11 | 78 |
| 25006 | Übermittlung Übersicht Schaltzeitdefinitionen | NB → LF, NB → MSB, LF → NB, LF → MSB | 1.0 | 2025-12-11 | 79 |
| 25007 | Übermittlung Übersicht Leistungskurvendefinitionen | NB → LF, NB → MSB, LF → NB, LF → MSB | 1.0 | 2025-12-11 | 79 |
| 25008 | Übermittlung einer ausgerollten Schaltzeitdefiniti | NB → LF, NB → MSB, LF → NB, LF → MSB | 1.0 | 2025-12-11 | 80 |
| 25009 | Übermittlung einer ausgerollten Leistungskurvendef | NB → LF, NB → MSB, LF → NB, LF → MSB | 1.0 | 2025-12-11 | 80 |
| 25010 | Antwort auf Berechnungsformel | MSB → NB | 1.0 | 2025-12-11 | 61 |
| 27001 | Übermittlung der Ausgleichsenergiepreise | BIKO → BKV | 2.0f | 2025-12-11 | 74 |
| 27002 | Preisblätter MSB-Leistungen | MSB → LF, MSB → NB | 2.0f | 2025-12-11 | 113 |
| 27003 | Preisblätter NB-Leistungen | NB → LF | 2.0f | 2025-12-11 | 96 |
| 29001 | Ablehnung REMADV | NB → LF, MSB → LF, MSB → NB, MSB → ESA | 1.0h | 2025-10-01 | 84 |
| 29002 | Ablehnung IFTSTA | NB → LF | 1.0h | 2025-10-01 | 54 |
| 31001 | Abschlagsrechnung | ReErst → ReEmpf | 1.0a | 2025-10-01 | 169 |
| 31002 | NN-Rechnung | ReErst → ReEmpf | 1.0a | 2025-10-01 | 271 |
| 31003 | WiM-Rechnung | ReErst → ReEmpf | 1.0a | 2025-10-01 | 190 |
| 31004 | Stornorechnung | ReErst → ReEmpf | 1.0a | 2025-10-01 | 192 |
| 31005 | MMM-Rechnung | ReErst → ReEmpf | 1.0a | 2025-10-01 | 186 |
| 31006 | MMM-selbst ausgest. Rechnung | ReErst → ReEmpf | 1.0a | 2025-10-01 | 183 |
| 31007 | Aggreg. MMM-Rechnung | NB → MGV | 1.0a | 2025-10-01 | 164 |
| 31008 | Aggreg. MMM-selbst ausgest. Rechnung | NB → MGV | 1.0a | 2025-10-01 | 164 |
| 31009 | MSB-Rechnung | ReErst → ReEmpf | 1.0a | 2025-10-01 | 186 |
| 31010 | Kapazitätsrechnung | NB → KN | 1.0a | 2025-10-01 | 162 |
| 31011 | Rechnung Sonstige Leistung | ReErst → ReEmpf | 1.0a | 2025-10-01 | 192 |
| 33001 | Bestätigung | ReEmpf → ReErst | 1.0a | 2025-10-01 | 72 |
| 33002 | Abweisung | ReEmpf → ReErst | 1.0a | 2025-10-01 | 108 |
| 33003 | Strom Abweisung Kopf und Summe | ReEmpf → ReErst | 1.0a | 2025-10-01 | 104 |
| 33004 | Strom Abweisung Position | ReEmpf → ReErst | 1.0a | 2025-10-01 | 105 |
| 35001 | Anfrage Geräteübernahmeangebot | MSBN → MSBA | 1.1 | 2025-04-01 | 61 |
| 35002 | Anfrage Rechnungsabwicklung MSB über LF | LF → MSB | 1.1 | 2025-04-01 | 63 |
| 35003 | Anfrage von Werten | ESA → MSB | 1.1 | 2025-04-01 | 91 |
| 35004 | Anfrage einer Konfiguration | NB → MSB, LF → MSB | 1.1 | 2025-04-01 | 147 |
| 35005 | Anfrage Angebot Änderung Technik | NB → MSB, LF → MSB | 1.1 | 2025-04-01 | 108 |
| 37000 | Kommunikationsdaten des LF Strom | LF → LF, LF → NB, LF → MSB, LF → ÜNB | 1.0f | 2025-12-11 | 310 |
| 37001 | Kommunikationsdaten des NB Strom | NB → LF, NB → MSB, NB → NB, NB → BKV, NB | 1.0f | 2025-12-11 | 301 |
| 37002 | Kommunikationsdaten des MSB Strom | MSB → NB, MSB → LF, MSB → ÜNB, MSB → MSB | 1.0f | 2025-12-11 | 247 |
| 37003 | Kommunikationsdaten des BKV Strom | BKV → NB, BKV → BIKO, BKV → ÜNB | 1.0f | 2025-12-11 | 157 |
| 37004 | Kommunikationsdaten des BIKO Strom | BIKO → NB, BIKO → BKV, BIKO → ÜNB | 1.0f | 2025-12-11 | 139 |
| 37005 | Kommunikationsdaten des ÜNB Strom | ÜNB → NB, ÜNB → LF, ÜNB → BKV, ÜNB → BIK | 1.0f | 2025-12-11 | 229 |
| 37006 | Kommunikationsdaten des ESA Strom | ESA → MSB | 1.0f | 2025-12-11 | 175 |
| 37008 | Kommunikationsdaten des LF Gas | LF → NB, LF → MSB, LF → LF | 1.0f | 2025-12-11 | 283 |
| 37009 | Kommunikationsdaten des NB Gas | NB → NB, NB → MSB, NB → MGV, NB → LF | 1.0f | 2025-12-11 | 283 |
| 37010 | Kommunikationsdaten des MSB Gas | MSB → NB, MSB → MSB, MSB → LF | 1.0f | 2025-12-11 | 265 |
| 37011 | Kommunikationsdaten des MGV Gas | MGV → NB | 1.0f | 2025-12-11 | 211 |
| 37012 | Spartenüb. Kommunikationsdaten des NB Gas | NB Gas → MSB Strom | 1.0f | 2025-12-11 | 139 |
| 37013 | Spartenüb. Kommunikationsdaten des MSB Gas | MSB Gas → MSB Strom | 1.0f | 2025-12-11 | 139 |
| 37014 | Spartenüb. Kommunikationsdaten des MSB Strom | MSB Strom → NB Gas, MSB Strom → MSB Gas | 1.0f | 2025-12-11 | 139 |
| 39000 | Stornierung Sperr-/Entsperrauftrag | LF → NB | 1.0a | 2024-10-01 | 54 |
| 39001 | Weiterleitung der Stornierung | NB → MSB | 1.0a | 2024-10-01 | 58 |
| 39002 | Stornierung der Bestellung | ESA → MSB | 1.0a | 2024-10-01 | 51 |
| 44001 | Anmeldung NN | LF → NB | 1.1 | 2025-12-11 | 218 |
| 44002 | Bestätigung Anmeldung | NB → LF | 1.1 | 2025-12-11 | 435 |
| 44003 | Ablehnung Anmeldung | NB → LF | 1.1 | 2025-12-11 | 91 |
| 44004 | Abmeldung NN | LF → NB | 1.1 | 2025-12-11 | 77 |
| 44005 | Bestätigung Abmeldung | NB → LF | 1.1 | 2025-12-11 | 83 |
| 44006 | Ablehnung Abmeldung | NB → LF | 1.1 | 2025-12-11 | 74 |
| 44007 | Abmeldung NN vom NB | NB → LF | 1.1 | 2025-12-11 | 66 |
| 44008 | Bestätigung Abmeldung vom NB | LF → NB | 1.1 | 2025-12-11 | 71 |
| 44009 | Ablehnung Abmeldung vom NB | LF → NB | 1.1 | 2025-12-11 | 66 |
| 44010 | Abmeldeanfrage des NB | NB → LF | 1.1 | 2025-12-11 | 73 |
| 44011 | Bestätigung Abmeldeanfrage | LF → NB | 1.1 | 2025-12-11 | 69 |
| 44012 | Ablehnung Abmeldeanfrage | LF → NB | 1.1 | 2025-12-11 | 65 |
| 44013 | Anmeldung EOG | NB → LF | 1.1 | 2025-12-11 | 467 |
| 44014 | Bestätigung EOG Anmeldung | LF → NB | 1.1 | 2025-12-11 | 438 |
| 44015 | Ablehnung EOG Anmeldung | LF → NB | 1.1 | 2025-12-11 | 79 |
| 44016 | Kündigung beim alten Lieferanten | LFN → LFA | 1.1 | 2025-12-11 | 96 |
| 44017 | Bestätigung Kündigung | LFA → LFN | 1.1 | 2025-12-11 | 96 |
| 44018 | Ablehnung Kündigung | LFA → LFN | 1.1 | 2025-12-11 | 84 |
| 44019 | Bestandsliste zugeordnete Marktlokationenen | NB → LF | 1.1 | 2025-12-11 | 152 |
| 44020 | Änderungsmeldung zur Bestandsliste | LF → NB | 1.1 | 2025-12-11 | 160 |
| 44021 | Antwort auf Änderungsmeldung zur Bestandsliste | NB → LF | 1.1 | 2025-12-11 | 155 |
| 44022 | Anfrage nach Stornierung | MSCONS-Nachrichten können von verschiede | 1.1 | 2025-12-11 | 60 |
| 44023 | Bestätigung Anfrage Stornierung | zurück → den Absender | 1.1 | 2025-12-11 | 61 |
| 44024 | Ablehnung Anfrage Stornierung | zurück → den Absender | 1.1 | 2025-12-11 | 64 |
| 44035 | Antwort auf die Geschäftsdatenanfrage | NB → LF | 1.1 | 2025-12-11 | 373 |
| 44036 | Informationsmeldung über existierende Zuordnung | NB → LF | 1.1 | 2025-12-11 | 65 |
| 44037 | Informationsmeldung zur Beendigung der Zuordnung | NB → LF | 1.1 | 2025-12-11 | 63 |
| 44038 | Informationsmeldung zur Aufhebung einer zuk. Zuord | NB → LF | 1.1 | 2025-12-11 | 71 |
| 44039 | Kündigung MSB | MSBN → MSBA | 1.1 | 2025-12-11 | 87 |
| 44040 | Bestätigung Kündigung MSB | MSBA → MSBN | 1.1 | 2025-12-11 | 98 |
| 44041 | Ablehnung Kündigung MSB | MSBA → MSBN | 1.1 | 2025-12-11 | 77 |
| 44042 | Anmeldung MSB | MSB → NB | 1.1 | 2025-12-11 | 111 |
| 44043 | Bestätigung Anmeldung MSB | NB → MSB | 1.1 | 2025-12-11 | 305 |
| 44044 | Ablehnung Anmeldung MSB | NB → MSB | 1.1 | 2025-12-11 | 65 |
| 44051 | Ende MSB | MSB → NB | 1.1 | 2025-12-11 | 68 |
| 44052 | Bestätigung Ende MSB | NB → MSB | 1.1 | 2025-12-11 | 76 |
| 44053 | Ablehnung Ende MSB | NB → MSB | 1.1 | 2025-12-11 | 68 |
| 44060 | Antwort auf die Geschäftsdatenanfrage | NB → MSB (Strom bzw. Gas) | 1.1 | 2025-12-11 | 262 |
| 44096 | Deklarationsliste | NB → MGV | 1.1 | 2025-12-11 | 63 |
| 44097 | Deklarationsliste | MGV → BKV | 1.1 | 2025-12-11 | 69 |
| 44101 | Stammdaten zur Messlokation | NB → MSB | 1.1 | 2025-12-11 | 77 |
| 44102 | Aktualisierte Stammdaten zur Messlokation | NB → MSB | 1.1 | 2025-12-11 | 75 |
| 44103 | Stammdaten zur Marktlokation | NB → LF | 1.1 | 2025-12-11 | 132 |
| 44104 | Aktualisierte Stammdaten zur Marktlokation | NB → LF | 1.1 | 2025-12-11 | 130 |
| 44105 | Ablehnung auf Stammdaten zur Marktlokation | LF → NB | 1.1 | 2025-12-11 | 70 |
| 44109 | Nicht bila.rel. Änderung vom LF | LF → NB [Berechtigter] | 1.1 | 2025-12-11 | 97 |
| 44110 | #nv# Nicht bila.rel. Änderung vom LF | NB [Verteiler] → MSB | 1.1 | 2025-12-11 | 62 |
| 44111 |  | NB [Berechtigter] → LF | 1.1 | 2025-12-11 | 63 |
| 44112 | Nicht bila.rel. Änderung vom NB | NB → LF | 1.1 | 2025-12-11 | 223 |
| 44113 | Nicht bila.rel. Änderung vom NB | NB → MSB | 1.1 | 2025-12-11 | 132 |
| 44115 | Antwort auf Änderung vom NB | LF → NB, MSB → NB | 1.1 | 2025-12-11 | 64 |
| 44116 | Änderung vom MSB mit Abhängig keiten | MSB → NB [Verteiler] | 1.1 | 2025-12-11 | 215 |
| 44117 | Änderung vom MSB mit Abhängig keiten | NB [Verteiler] → LF | 1.1 | 2025-12-11 | 199 |
| 44119 | Antwort auf Änderung vom MSB | NB [Verteiler] → MSB, LF → NB [Verteiler | 1.1 | 2025-12-11 | 64 |
| 44120 | Bila.rel. Änderung vom LF | LF → NB | 1.1 | 2025-12-11 | 70 |
| 44121 | Antwort auf Änderung vom LF | NB → LF | 1.1 | 2025-12-11 | 63 |
| 44123 | Bila.rel. Änderung vom NB mit Abhängigkeiten | NB → LF | 1.1 | 2025-12-11 | 106 |
| 44124 | Antwort auf Änderung vom NB | LF → NB | 1.1 | 2025-12-11 | 63 |
| 44129 | Korrektur Meldepunkt vom NB | NB → LF, NB → ÜNB | 1.1 | 2025-12-11 | 65 |
| 44130 | Korrektur Meldepunkt vom NB | NB → MSB | 1.1 | 2025-12-11 | 65 |
| 44132 | Antwort auf Änderung vom NB | LF → NB, ÜNB → NB, MSB → NB | 1.1 | 2025-12-11 | 56 |
| 44137 | Nicht bila.rel. Anfrage an LF | NB [Berechtigt] → LF | 1.1 | 2025-12-11 | 97 |
| 44138 | Antwort auf Anfrage | LF → NB [Berechtigt] | 1.1 | 2025-12-11 | 105 |
| 44139 | Nicht bila.rel. Anfrage an NB | LF → NB | 1.1 | 2025-12-11 | 226 |
| 44140 | Nicht bila.rel. Anfrage an NB | MSB → NB | 1.1 | 2025-12-11 | 131 |
| 44142 | Antwort auf Anfrage | NB → LF, NB → MSB | 1.1 | 2025-12-11 | 244 |
| 44143 | Anfrage an MSB mit Abhängigkeiten | LF → NB [Verteiler] | 1.1 | 2025-12-11 | 199 |
| 44145 | Antwort auf Anfrage | NB [Verteiler] → LF | 1.1 | 2025-12-11 | 207 |
| 44146 | Ablehnung der Anfrage | NB [Verteiler] → LF | 1.1 | 2025-12-11 | 63 |
| 44147 | Anfrage an MSB mit Abhängigkeiten | NB [Verteiler] → MSB | 1.1 | 2025-12-11 | 199 |
| 44148 | Anfrage an MSB mit Abhängigkeiten | NB [Berechtigt] → MSB | 1.1 | 2025-12-11 | 215 |
| 44149 | Antwort auf Anfrage | MSB → NB [Verteiler], MSB → NB [Berechti | 1.1 | 2025-12-11 | 223 |
| 44150 | Bila.rel. Anfrage an LF | NB → LF | 1.1 | 2025-12-11 | 70 |
| 44151 | Antwort auf Anfrage | LF → NB | 1.1 | 2025-12-11 | 78 |
| 44152 | Ablehnung der Anfrage | LF → NB | 1.1 | 2025-12-11 | 63 |
| 44156 | Bila.rel. Anfrage an NB mit Abhängigkeiten | LF → NB | 1.1 | 2025-12-11 | 106 |
| 44157 | Antwort auf Anfrage | NB → LF | 1.1 | 2025-12-11 | 114 |
| 44159 | Änderung vom MSB ohne Abhängigkeiten | MSB → NB [Verteiler] | 1.1 | 2025-12-11 | 100 |
| 44160 | Änderung vom MSB ohne Abhängigkeiten | NB [Verteiler] → LF [Berechtigt] | 1.1 | 2025-12-11 | 76 |
| 44161 | Antwort auf Änderung | NB [Verteiler] → MSB, LF [Berechtigt] →  | 1.1 | 2025-12-11 | 64 |
| 44162 | Anfrage an MSB ohne Abhängigkeiten | LF [Berechtigt] → NB [Verteiler] | 1.1 | 2025-12-11 | 76 |
| 44163 | Antwort auf Anfrage | NB [Verteiler] → LF [Berechtigt] | 1.1 | 2025-12-11 | 84 |
| 44164 | Ablehnung Anfrage | NB [Verteiler] → LF [Berechtigt] | 1.1 | 2025-12-11 | 63 |
| 44165 | Nicht bila.rel. Anfrage an MSB ohne Abhängigkeiten | NB [Verteiler] → MSB | 1.1 | 2025-12-11 | 76 |
| 44166 | Nicht bila.rel. Anfrage an MSB ohne Abhängigkeiten | NB [Berechtigt] → MSB | 1.1 | 2025-12-11 | 100 |
| 44167 | Antwort auf Anfrage | MSB → NB | 1.1 | 2025-12-11 | 108 |
| 44168 | Verpflichtungsanfrage / Aufforderung | NB → gMSB | 1.1 | 2025-12-11 | 318 |
| 44169 | Bestätigung Verpflichtungsanfrage | gMSB → NB | 1.1 | 2025-12-11 | 309 |
| 44170 | Ablehnung Verpflichtungsanfrage | gMSB → NB | 1.1 | 2025-12-11 | 65 |
| 44172 | #nv# Anfrage an MSB mit Abhängigkeiten | MSB → NB [Verteiler] | 1.1 | 2025-12-11 | 145 |
| 44175 | Änderung der Marktlokationsstruktur | NB → LF | 1.1 | 2025-12-11 | 63 |
| 44176 | Antwort auf Änderung der Marktlokationsstruktur | LF → NB | 1.1 | 2025-12-11 | 71 |
| 44180 | Anfrage der Marktlokationsstruktur | LF → NB | 1.1 | 2025-12-11 | 63 |
| 44181 | Antwort auf Anfrage der Marktlokationsstruktur | NB → LF | 1.1 | 2025-12-11 | 71 |
| 44182 | Ablehnung der Anfrage der Marktlokationsstruktur | NB → LF | 1.1 | 2025-12-11 | 63 |
| 55001 | Anmeldung verb. MaLo | LF → NB | 2.1 | 2025-12-11 | 146 |
| 55002 | Bestätigung Anmeldung verb. MaLo | NB → LF | 2.1 | 2025-12-11 | 165 |
| 55003 | Ablehnung Anmeldung verb. MaLo | NB → LF | 2.1 | 2025-12-11 | 83 |
| 55004 | Abmeldung | LF → NB | 2.1 | 2025-12-11 | 83 |
| 55005 | Bestätigung Abmeldung | NB → LF | 2.1 | 2025-12-11 | 75 |
| 55006 | Ablehnung Abmeldung | NB → LF | 2.1 | 2025-12-11 | 70 |
| 55007 | Abmeldung / Beendigung der Zuordnung | NB → LF | 2.1 | 2025-12-11 | 82 |
| 55008 | Bestätigung Abmeldung | LF → NB | 2.1 | 2025-12-11 | 69 |
| 55009 | Ablehnung Abmeldung | LF → NB | 2.1 | 2025-12-11 | 64 |
| 55010 | Anfrage zur Beendigung der Zuordnung | NB → LF | 2.1 | 2025-12-11 | 88 |
| 55011 | Bestätigung Beendigung der Zuordnung | LF → NB | 2.1 | 2025-12-11 | 64 |
| 55012 | Ablehnung Beendigung der Zuordnung | LF → NB | 2.1 | 2025-12-11 | 60 |
| 55013 | Anmeldung / Zuordnung EOG | NB → LF | 2.1 | 2025-12-11 | 257 |
| 55014 | Bestätigung EOG Anmeldung | LF → NB | 2.1 | 2025-12-11 | 159 |
| 55015 | Ablehnung EOG Anmeldung | LF → NB | 2.1 | 2025-12-11 | 74 |
| 55016 | Kündigung | LFN → LFA | 2.1 | 2025-12-11 | 73 |
| 55017 | Bestätigung Kündigung | LFA → LFN | 2.1 | 2025-12-11 | 78 |
| 55018 | Ablehnung Kündigung | LFA → LFN | 2.1 | 2025-12-11 | 80 |
| 55022 | Anfrage nach Stornierung | MSCONS-Nachrichten können von verschiede | 2.1 | 2025-12-11 | 60 |
| 55023 | Bestätigung Anfrage Stornierung | zurück → den Absender | 2.1 | 2025-12-11 | 61 |
| 55024 | Ablehnung Anfrage Stornierung | zurück → den Absender | 2.1 | 2025-12-11 | 64 |
| 55035 | Antwort auf GDA verb. MaLo | NB → LF | 2.1 | 2025-12-11 | 531 |
| 55036 | Existierende Zuordnung | NB → LF | 2.1 | 2025-12-11 | 69 |
| 55037 | Beendigung der Zuordnung | NB → LF | 2.1 | 2025-12-11 | 67 |
| 55038 | Aufhebung einer zuk. Zuordnung | NB → LF | 2.1 | 2025-12-11 | 74 |
| 55039 | Kündigung MSB | MSBN → MSBA | 2.1 | 2025-12-11 | 91 |
| 55040 | Bestätigung Kündigung MSB | MSBA → MSBN | 2.1 | 2025-12-11 | 104 |
| 55041 | Ablehnung Kündigung MSB | MSBA → MSBN | 2.1 | 2025-12-11 | 77 |
| 55042 | Anmeldung MSB | MSB → NB | 2.1 | 2025-12-11 | 116 |
| 55043 | Bestätigung Anmeldung MSB | NB → MSB | 2.1 | 2025-12-11 | 909 |
| 55044 | Ablehnung Anmeldung MSB | NB → MSB | 2.1 | 2025-12-11 | 66 |
| 55051 | Ende MSB | MSB → NB | 2.1 | 2025-12-11 | 68 |
| 55052 | Bestätigung Ende MSB | NB → MSB | 2.1 | 2025-12-11 | 98 |
| 55053 | Ablehnung Ende MSB | NB → MSB | 2.1 | 2025-12-11 | 68 |
| 55060 | Antwort auf GDA | NB → MSB | 2.1 | 2025-12-11 | 608 |
| 55062 | Aktivierung von ZP | NB → BIKO, NB → LF, NB → NB, NB → ÜNB, Ü | 2.1 | 2025-12-11 | 125 |
| 55063 | Deaktivierung von ZP | NB → BIKO, NB → LF, NB → NB, NB → ÜNB, Ü | 2.1 | 2025-12-11 | 56 |
| 55064 | Antwort | BIKO → NB, BIKO → ÜNB, NB → NB | 2.1 | 2025-12-11 | 79 |
| 55065 | Lieferantenclearingliste | NB → LF, ÜNB → LF | 2.1 | 2025-12-11 | 192 |
| 55066 | Korrekturliste zur Lieferantenclearingliste | LF → NB, LF → ÜNB | 2.1 | 2025-12-11 | 210 |
| 55067 | Bilanzkreiszuordnungsliste | NB → BKV, ÜNB → BKV | 2.1 | 2025-12-11 | 111 |
| 55069 | Clearingliste DZR | BIKO → NB, BIKO → ÜNB | 2.1 | 2025-12-11 | 116 |
| 55070 | Clearingliste BAS | BIKO → BKV | 2.1 | 2025-12-11 | 168 |
| 55071 | Aktivierung der Zuordnungsermächtigung | BKV → NB | 2.1 | 2025-12-11 | 75 |
| 55072 | Deaktivierung der Zuordnungsermächtigung | BKV → NB | 2.1 | 2025-12-11 | 75 |
| 55073 | Übermittlung der Profildefinitionen | NB → LF, NB → MSB | 2.1 | 2025-12-11 | 212 |
| 55074 | Stammdaten auf eine ORDERS | NB → UBA | 2.1 | 2025-12-11 | 269 |
| 55075 | Stammdaten aufgrund einer Änderung | NB → UBA | 2.1 | 2025-12-11 | 279 |
| 55076 | Antwort auf Stammdatenänderung | UBA → NB | 2.1 | 2025-12-11 | 287 |
| 55077 | Anmeldung erz. MaLo | LF → NB | 2.1 | 2025-12-11 | 111 |
| 55078 | Bestätigung Anmeldung erz. MaLo | NB → LF | 2.1 | 2025-12-11 | 171 |
| 55080 | Ablehnung Anmeldung erz. MaLo | NB → LF | 2.1 | 2025-12-11 | 89 |
| 55095 | Antwort auf GDA erz. MaLo | NB → LF | 2.1 | 2025-12-11 | 465 |
| 55109 | Änderung Daten der MaLo | LF → NB | 2.1 | 2025-12-11 | 129 |
| 55110 | Änderung Daten der MaLo | LF → MSB | 2.1 | 2025-12-11 | 90 |
| 55126 | Abr.-Daten BK-Abr. verb. Malo | NB → LF, NBA → NBN | 2.1 | 2025-12-11 | 156 |
| 55136 | Rückmeldung/Anfrage Daten der MaLo | MSB → LF | 2.1 | 2025-12-11 | 104 |
| 55137 | Rückmeldung/Anfrage Daten der MaLo | NB → LF | 2.1 | 2025-12-11 | 145 |
| 55156 | Rückmeldung/Anfrage Abr.-Daten BK-Abr. verb. MaLo | LF → NB | 2.1 | 2025-12-11 | 171 |
| 55168 | Verpflichtungsanfrage / Aufforderung | NB → gMSB | 2.1 | 2025-12-11 | 927 |
| 55169 | Bestätigung Verpflichtungsanfrage | gMSB → NB | 2.1 | 2025-12-11 | 908 |
| 55170 | Ablehnung Verpflichtungsanfrage | gMSB → NB | 2.1 | 2025-12-11 | 65 |
| 55173 | Änderung der Lokationsbündelstruktur | NB → MSB | 2.1 | 2025-12-11 | 124 |
| 55175 | Änderung der Lokationsbündelstruktur | NB → LF | 2.1 | 2025-12-11 | 124 |
| 55177 | Rückmeldung/Anfrage Lokationsbündelstruktur | MSB → NB | 2.1 | 2025-12-11 | 138 |
| 55180 | Rückmeldung/Anfrage Lokationsbündelstruktur | LF → NB | 2.1 | 2025-12-11 | 138 |
| 55194 | Antwort auf GDA (Strom an Gas) | NB → MSB | 2.1 | 2025-12-11 | 95 |
| 55195 | Bilanzierungsgebietsclearingliste | ÜNB → NB | 2.1 | 2025-12-11 | 199 |
| 55196 | Antwort auf Bilanzierungsgebietsclearingliste | NB → ÜNB | 2.1 | 2025-12-11 | 299 |
| 55197 | Aktivierung ZP tägliche AAÜZ | NB (ANB) → ÜNB | 2.1 | 2025-12-11 | 84 |
| 55198 | Deaktivierung tägliche AAÜZ | NB (ANB) → ÜNB | 2.1 | 2025-12-11 | 56 |
| 55199 | Aktivierung ZP LF-AASZR | NB (ANB) → LF | 2.1 | 2025-12-11 | 84 |
| 55200 | Deaktivierung ZP LF-AASZR | NB (ANB) → LF | 2.1 | 2025-12-11 | 56 |
| 55201 | LF-AACL | NB (ANB) → LF | 2.1 | 2025-12-11 | 114 |
| 55202 | Korrekturliste LF-AACL | LF → NB (ANB) | 2.1 | 2025-12-11 | 128 |
| 55203 | Aktivierung ZP monatliche AAÜZ | NB (ANB) → BIKO | 2.1 | 2025-12-11 | 88 |
| 55204 | Antwort auf Aktivierung ZP | BIKO → NB (ANB) | 2.1 | 2025-12-11 | 64 |
| 55205 | Weiterleitung Aktivierung ZP | BIKO → BKV (des LF) | 2.1 | 2025-12-11 | 88 |
| 55206 | Deaktivierung ZP monatliche AAÜZ | NB (ANB) → BIKO | 2.1 | 2025-12-11 | 56 |
| 55207 | Antwort auf Deaktivierung ZP | BIKO → NB (ANB) | 2.1 | 2025-12-11 | 64 |
| 55208 | Weiterleitung Deaktivierung ZP | BIKO → BKV (des LF) | 2.1 | 2025-12-11 | 56 |
| 55209 | Aktivierung ZP monatliche AAÜZ | NB (ANB) → BIKO | 2.1 | 2025-12-11 | 88 |
| 55210 | Antwort auf Aktivierung ZP | BIKO → NB (ANB) | 2.1 | 2025-12-11 | 64 |
| 55211 | Weiterleitung Aktivierung ZP | BIKO → BKV (des anfNB) | 2.1 | 2025-12-11 | 88 |
| 55212 | Deaktivierung ZP monatliche AAÜZ | NB (ANB) → BIKO | 2.1 | 2025-12-11 | 56 |
| 55213 | Antwort auf Deaktivierung ZP | BIKO → NB (ANB) | 2.1 | 2025-12-11 | 64 |
| 55214 | Weiterleitung Deaktivierung ZP | BIKO → BKV (des anfNB) | 2.1 | 2025-12-11 | 56 |
| 55218 | Abr.-Daten NNA | NB → LF, NBA → NBN | 2.1 | 2025-12-11 | 160 |
| 55220 | Rückmeldung/Anfrage Abr.-Daten NNA | LF → NB | 2.1 | 2025-12-11 | 176 |
| 55223 | DZÜ Liste | ÜNB → NB | 2.1 | 2025-12-11 | 234 |
| 55224 | Antwort auf DZÜ Liste | NB → ÜNB | 2.1 | 2025-12-11 | 143 |
| 55225 | Änderung Blindabr.-Daten der NeLo | NB → LF, NBA → NBN | 2.1 | 2025-12-11 | 87 |
| 55227 | Rückmeldung/Anfrage Blindabr.-Daten der NeLo | LF → NB | 2.1 | 2025-12-11 | 100 |
| 55230 | Änderung Blindabr.-Daten der NeLo | LF → NB | 2.1 | 2025-12-11 | 77 |
| 55232 | Rückmeldung/Anfrage Blindabr.-Daten der NeLo | NB → LF | 2.1 | 2025-12-11 | 90 |
| 55235 | Zuordnung ZP der NGZ zur NZR | NB → NB, NB → ÜNB | 2.1 | 2025-12-11 | 84 |
| 55236 | Beendigung Zuordnung ZP der NGZ zur NZR | NB → NB, NB → ÜNB | 2.1 | 2025-12-11 | 56 |
| 55237 | Antwort | NB → NB | 2.1 | 2025-12-11 | 72 |
| 55238 | Anmeldung in Modell 2 | NB (LPB) → NB (VNB) | 2.1 | 2025-12-11 | 76 |
| 55239 | Antwort auf Anmeldung | NB (VNB) → NB (LPB) | 2.1 | 2025-12-11 | 104 |
| 55240 | Beendigung der Zuordnung zur MaLo | NB (VNB) → LF | 2.1 | 2025-12-11 | 67 |
| 55241 | Antwort auf Beendigung | LF → NB (VNB) | 2.1 | 2025-12-11 | 75 |
| 55242 | Abmeldung aus dem Modell 2 | NB (LPB) → NB (VNB) | 2.1 | 2025-12-11 | 70 |
| 55243 | Antwort auf Abmeldung | NB (VNB) → NB (LPB) | 2.1 | 2025-12-11 | 78 |
| 55553 | Daten auf individuelle Bestellung | MSB → NB, MSB → LF, MSB → MSB | 2.1 | 2025-12-11 | 171 |
| 55555 | Rückmeldung/Anfrage Daten der individuellen Bestel | NB → MSB, LF → MSB, MSB → MSB | 2.1 | 2025-12-11 | 186 |
| 55557 | Änderung MSB-Abr.-Daten der MaLo | MSB → NB | 2.1 | 2025-12-11 | 88 |
| 55559 | Rückmeldung/Anfrage MSB-Abr.-Daten der MaLo | NB → MSB | 2.1 | 2025-12-11 | 101 |
| 55600 | Anmeldung neue verb. MaLo | LF → NB | 2.1 | 2025-12-11 | 153 |
| 55601 | Anmeldung neue erz. MaLo | LF → NB | 2.1 | 2025-12-11 | 154 |
| 55602 | Bestätigung Anmeldung neue verb. MaLo | NB → LF | 2.1 | 2025-12-11 | 159 |
| 55603 | Bestätigung Anmeldung neue erz. MaLo | NB → LF | 2.1 | 2025-12-11 | 170 |
| 55604 | Ablehnung Anmeldung neue verb. MaLo | NB → LF | 2.1 | 2025-12-11 | 73 |
| 55605 | Ablehnung Anmeldung neue erz. MaLo | NB → LF | 2.1 | 2025-12-11 | 73 |
| 55607 | (Ankündigung) Zuordnung des LF zur erz. MaLo/ Tran | NB → LF | 2.1 | 2025-12-11 | 186 |
| 55608 | Bestätigung Zuordnung des LF zur erz. MaLo/ Tranch | LF → NB | 2.1 | 2025-12-11 | 111 |
| 55609 | Ablehnung Zuordnung des LF zur erz. MaLo/ Tranche | LF → NB | 2.1 | 2025-12-11 | 69 |
| 55611 | Beendigung der Zuordnung | NB → MSB, NB → MSBZ | 2.1 | 2025-12-11 | 68 |
| 55613 | Abr.-Daten BK-Abr. verb. MaLo | NB → ÜNB | 2.1 | 2025-12-11 | 131 |
| 55614 | Rückmeldung/Anfrage Abr.-Daten BK-Abr. verb. MaLo | ÜNB → NB | 2.1 | 2025-12-11 | 143 |
| 55615 | Änderung Daten der NeLo | NB → LF, NBA → NBN | 2.1 | 2025-12-11 | 81 |
| 55616 | Änderung Daten der MaLo | NB → LF, NBA → NBN | 2.1 | 2025-12-11 | 229 |
| 55617 | Änderung Daten der TR | NB → LF, NBA → NBN | 2.1 | 2025-12-11 | 142 |
| 55618 | Änderung Daten der SR | NB → LF, NBA → NBN | 2.1 | 2025-12-11 | 81 |
| 55619 | Änderung Daten der Tranche | NB → LF, NBA → NBN | 2.1 | 2025-12-11 | 78 |
| 55620 | Änderung Daten der MeLo | NB → LF, NBA → NBN | 2.1 | 2025-12-11 | 89 |
| 55621 | Rückmeldung/Anfrage Daten zur NeLo | LF → NB | 2.1 | 2025-12-11 | 94 |
| 55622 | Rückmeldung/Anfrage Daten der MaLo | LF → NB | 2.1 | 2025-12-11 | 249 |
| 55623 | Rückmeldung/Anfrage Daten der TR | LF → NB | 2.1 | 2025-12-11 | 155 |
| 55624 | Rückmeldung/Anfrage Daten der SR | LF → NB | 2.1 | 2025-12-11 | 94 |
| 55625 | Rückmeldung/Anfrage Daten der Tranche | LF → NB | 2.1 | 2025-12-11 | 91 |
| 55626 | Rückmeldung/Anfrage Daten der MeLo | LF → NB | 2.1 | 2025-12-11 | 102 |
| 55627 | Änderung Daten der NeLo | NB → MSB | 2.1 | 2025-12-11 | 81 |
| 55628 | Änderung Daten der MaLo | NB → MSB | 2.1 | 2025-12-11 | 223 |
| 55629 | Änderung Daten der TR | NB → MSB | 2.1 | 2025-12-11 | 134 |
| 55630 | Änderung Daten der SR | NB → MSB | 2.1 | 2025-12-11 | 81 |
| 55632 | Änderung Daten der MeLo | NB → MSB | 2.1 | 2025-12-11 | 92 |
| 55633 | Rückmeldung/Anfrage Daten zur NeLo | MSB → NB | 2.1 | 2025-12-11 | 94 |
| 55634 | Rückmeldung/Anfrage Daten der MaLo | MSB → NB | 2.1 | 2025-12-11 | 243 |
| 55635 | Rückmeldung/Anfrage Daten der TR | MSB → NB | 2.1 | 2025-12-11 | 147 |
| 55636 | Rückmeldung/Anfrage Daten der SR | MSB → NB | 2.1 | 2025-12-11 | 94 |
| 55638 | Rückmeldung/Anfrage Daten der MeLo | MSB → NB | 2.1 | 2025-12-11 | 105 |
| 55639 | Änderung Daten der NeLo | MSB → NB | 2.1 | 2025-12-11 | 116 |
| 55640 | Änderung Daten der MaLo | MSB → NB | 2.1 | 2025-12-11 | 131 |
| 55641 | Änderung Daten der SR | MSB → NB | 2.1 | 2025-12-11 | 102 |
| 55642 | Änderung Daten der Tranche | MSB → NB | 2.1 | 2025-12-11 | 82 |
| 55643 | Änderung Daten der MeLo | MSB → NB | 2.1 | 2025-12-11 | 301 |
| 55644 | Rückmeldung/Anfrage Daten der NeLo | NB → MSB | 2.1 | 2025-12-11 | 131 |
| 55645 | Rückmeldung/Anfrage Daten der MaLo | NB → MSB | 2.1 | 2025-12-11 | 146 |
| 55646 | Rückmeldung/Anfrage Daten der SR | NB → MSB | 2.1 | 2025-12-11 | 116 |
| 55647 | Rückmeldung/Anfrage Daten der Tranche | NB → MSB | 2.1 | 2025-12-11 | 95 |
| 55648 | Rückmeldung/Anfrage Daten der MeLo | NB → MSB | 2.1 | 2025-12-11 | 325 |
| 55649 | Änderung Daten der NeLo | MSB → LF | 2.1 | 2025-12-11 | 117 |
| 55650 | Änderung Daten der MaLo | MSB → LF | 2.1 | 2025-12-11 | 131 |
| 55651 | Änderung Daten der SR | MSB → LF | 2.1 | 2025-12-11 | 102 |
| 55652 | Änderung Daten der Tranche | MSB → LF | 2.1 | 2025-12-11 | 82 |
| 55653 | Änderung Daten der MeLo | MSB → LF | 2.1 | 2025-12-11 | 202 |
| 55654 | Rückmeldung/Anfrage Daten der NeLo | LF → MSB | 2.1 | 2025-12-11 | 132 |
| 55655 | Rückmeldung/Anfrage Daten der MaLo | LF → MSB | 2.1 | 2025-12-11 | 146 |
| 55656 | Rückmeldung/Anfrage Daten der SR | LF → MSB | 2.1 | 2025-12-11 | 116 |
| 55657 | Rückmeldung/Anfrage Daten der Tranche | LF → MSB | 2.1 | 2025-12-11 | 95 |
| 55658 | Rückmeldung/Anfrage Daten der MeLo | LF → MSB | 2.1 | 2025-12-11 | 220 |
| 55659 | Änderung Daten der NeLo | MSB → weiteren MSB | 2.1 | 2025-12-11 | 123 |
| 55660 | Änderung Daten der MaLo | MSB → weiteren MSB | 2.1 | 2025-12-11 | 147 |
| 55661 | Änderung Daten der SR | MSB → weiteren MSB | 2.1 | 2025-12-11 | 103 |
| 55662 | Änderung Daten der Tranche | MSB → weiteren MSB | 2.1 | 2025-12-11 | 94 |
| 55663 | Änderung Daten der MeLo | MSB → weiteren MSB | 2.1 | 2025-12-11 | 301 |
| 55664 | Rückmeldung/Anfrage Daten der NeLo | weiterer MSB → MSB | 2.1 | 2025-12-11 | 138 |
| 55665 | Rückmeldung/Anfrage Daten der MaLo | weiteren MSB → MSB | 2.1 | 2025-12-11 | 162 |
| 55666 | Rückmeldung/Anfrage Daten der SR | weiterer MSB → MSB | 2.1 | 2025-12-11 | 117 |
| 55667 | Rückmeldung/Anfrage Daten der Tranche | weiteren MSB → MSB | 2.1 | 2025-12-11 | 107 |
| 55669 | Rückmeldung/Anfrage Daten der MeLo | weiterer MSB → MSB | 2.1 | 2025-12-11 | 329 |
| 55670 | Stammdaten BK-Treue | NB → ÜNB | 2.1 | 2025-12-11 | 121 |
| 55671 | Rückmeldung auf Stammdaten BK-Treue | ÜNB → NB | 2.1 | 2025-12-11 | 128 |
| 55672 | Abr.-Daten BK-Abr. erz. Malo | NB → LF, NBA → NBN | 2.1 | 2025-12-11 | 178 |
| 55673 | Rückmeldung/Anfrage Abr.-Daten BK-Abr. erz. Malo | LF → NB | 2.1 | 2025-12-11 | 195 |
| 55674 | Abr.-Daten BK-Abr. erz. Malo | NB → ÜNB | 2.1 | 2025-12-11 | 133 |
| 55675 | Rückmeldung/Anfrage Abr.-Daten BK-Abr. erz. Malo | ÜNB → NB | 2.1 | 2025-12-11 | 145 |
| 55684 | Änderung Daten der MaLo | MSB → ÜNB | 2.1 | 2025-12-11 | 82 |
| 55685 | Rückmeldung/Anfrage Daten der MaLo | ÜNB → MSB | 2.1 | 2025-12-11 | 95 |
| 55686 | Änderung Daten der Tranche | MSB → ÜNB | 2.1 | 2025-12-11 | 82 |
| 55687 | Rückmeldung/Anfrage Daten der Tranche | ÜNB → MSB | 2.1 | 2025-12-11 | 95 |
| 55688 | Änderung Daten der MaLo | NB → ÜNB | 2.1 | 2025-12-11 | 78 |
| 55689 | Rückmeldung/Anfrage Daten der MaLo | ÜNB → NB | 2.1 | 2025-12-11 | 91 |
| 55690 | Lokationsbündelstruktur und DB | NBA → NBN | 2.1 | 2025-12-11 | 223 |
| 55691 | Änderung Paket-ID der Malo | NBA → LF, NBA → MSB, NBA → NBN, NBA → ÜN | 2.1 | 2025-12-11 | 76 |
| 55692 | Rückmeldung/Anfrage Paket-ID der Malo | LF → NBA, MSB → NBA, ÜNB → NBA | 2.1 | 2025-12-11 | 90 |