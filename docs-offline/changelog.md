# Änderungsprotokoll Schnittstellen



Alle wesentlichen Änderungen an den MACO APP Schnittstellen werden in dieser Datei dokumentiert.

Das Format basiert auf [Keep a Changelog](https://keepachangelog.com/de/1.1.0/),
und dieses Projekt folgt der [Semantischen Versionierung](https://semver.org/lang/de/).

## [Unveröffentlicht]
- ...

## [1.3.3] - 02. Juni 2025

### Geändert
- Fehlerkorrektur in Prozessdaten aktualisieren im Maloident (Lieferant) : Unter Zusatzdaten wird die prozessId übergeben, nicht refrenzProzessId

## [1.3.2] - 14. Mai 2025

### Geändert
- MCS Eingang: Beispiele und Beschreibungen erweitert

## [1.3.1] - 10. April 2025

### Hinzugefügt
- MCS Eingang: Empfang einer Marktnachricht

## [1.3.0] - 10. April 2025

### Hinzugefügt
- Authentifizierungsendpunkt

## [1.2.9] - 28. März 2025

### Geändert
- MaloIdent Schnittstellen erweitert um businessKey
- MaloIdent Schnittstellen erweitert um Beispiele

## [1.2.8] - 25. März 2025

### Geändert
- MaloIdent Schnittstellen ergänzt

## [1.2.7] - 19. März 2025
### Hinzugefügt
- Schema Dateien hinzugefügt für Prüfis 17135, 17135, 21047, 25001, 25010.
### Geändert
- Eventnamen korrigiert
- Schema Dateien für jedes Event überarbeitet
- Beschreibungen für Transaktionsdaten und Stammdaten erweitert.

## [1.2.6] - 28. Februar 2025
### Hinzugefügt
- Lesende Prozessdaten Schnittstelle zur Ermittlung der Zuordnungsermächtigung

## [1.2.5] - 20. Januar 2025
### Hinzugefügt
- Erweiterung der Beschreibungen für Transaktions- und Stammdaten.

## [1.2.4] - 10. Januar 2025
### Geändert
- Refactoring der Inbound-Schema-Referenzen und Aktualisierung der Versionierung im Änderungsprotokoll.

## [1.2.3] - 07. Januar 2025
### Hinzugefügt
- Neue Schema-Dateien für verschiedene Transaktionstypen und Marktlokationen.

## [1.2.2] - 07. Januar 2025
### Hinzugefügt
- Beispiele für `START_LIEFERBEGINN`, `START_KUENDIGUNG`, `START_LIEFERENDE`.
- Neues Schema: `ECS_MALOIDENT`.

## [1.2.1] - 07. Januar 2025
### Behoben
- Falsches `data` Root-Element entfernt.
### Hinzugefügt
- Neues Schema: `START_MALOIDENT`.

## [1.2.0] - 16. Dezember 2024
### Geändert
- Entfernung veralteter Event-Schemas.
### Hinzugefügt
- Neue Schemas: `START_LIEFERBEGINN`, `START_KUENDIGUNG`, `START_BESTELLUNG_KONFIGURATION`, `START_STAMMDATENAENDERUNG_MALO_AN_LF`, `START_STAMMDATENAENDERUNG_MALO_AN_MSB`, `START_LIEFERENDE`, `START_AUFHEBUNG_ZUK_ZUORDNUNG_LF`, `START_AUFHEBUNG_ZUK_ZUORDNUNG_MSB`, `START_ABR_NN`, `START_VERSAND_ABR_BILA`, `START_VERSAND_BEARB_MELDUNG`.

## [1.1.4] - 14. November 2024
### Hinzugefügt
- `AKTUALISIEREN_MDOC_BASIS` ergänzt.

## [1.1.3] - 12. November 2024
### Hinzugefügt
- `LESEN_BILANZIERUNG_BASIS` ergänzt.

## [1.1.2] - 24. Oktober 2024
### Hinzugefügt
- `LESEN_BERECHNUNGSFORMEL_BASIS` ergänzt.

## [1.1.1] - 04. Oktober 2024
### Geändert
- Standardparameter angepasst: `parameter1 = LokationsId`, `parameter2 = LokationsTyp`, `parameter3 = gueltigAb/stichtag`.

## [1.1.0] - 26. September 2024
### Geändert
- OpenAPI-Dokument refaktoriert.

## [1.0.5] - 18. September 2024
### Geändert
- Standardbefehl auf `SAP_` anstatt `NOCODB_` geändert.
- Standardbeispiel `MaloId` auf `74018657187` aktualisiert.

## [1.0.4] - 13. September 2024
### Geändert
- Formatierungen überarbeitet.

## [1.0.3] - 28. August 2024
### Geändert
- Parameter für `LESEN`-Schnittstellen aktualisiert.

## [1.0.2] - 20. August 2024
### Hinzugefügt
- Schema ergänzt für `START_N_BILA_REL_AEND_VON_NB`, `START_N_BILA_REL_AEND_VON_LF`, `START_MESSWERTUEBERMITTLUNG`, `START_MALOIDENT`, `START_LIEFERENDE`, `START_KUENDIGUNG`.

## [1.0.1] - 08. August 2024
### Hinzugefügt
- Mehrsprachige Beschreibungen und Changelog.
- Anpassung der Schema-Beschreibungen in Deutsch und Englisch.

## [1.0.0] - 01. August 2024
### Hinzugefügt
- Initiale Version der API-Dokumentation.



