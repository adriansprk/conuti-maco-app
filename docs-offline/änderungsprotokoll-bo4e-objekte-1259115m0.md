# Änderungsprotokoll BO4E Objekte



Alle wesentlichen Änderungen an den BO4E Objekte werden in dieser Datei dokumentiert.


## [1.6.2] - 02. März 2026

### Geändert
- Feld in COM *Steuerbetrag* wurde von "steuerwertVorausbezahhlt" zu "steuerwertVorausbezahlt" korrigiert

## [1.6.1] - 24. Feburar 2026

### Geändert
- BO *Marktlokation* wurde erweiteret um "zugehoerigeMarktlokationen" vom Typ  "MarktlokationsReferenz"

### Hinzugefügt
- COM *MarktlokationsReferenz* erstellt


### Geändert
- Versionierung an Schema Repo angepasst https://github.com/conuti-gmbh/bo4e-schema/releases/tag/1.6.1


## [1.0.61] - 28. Januar 2026

### Hinzugefügt
- ENUM *Sonderrechnungsart* erweitert um PRIVILEGIERUNG_NACH_ENFG, KONZESSIONSABGABE_WEITERGELEITETE_MENGEN

## [1.0.60] - 28. Januar 2026

### Hinzugefügt
- COM *Beschreibungsformat* in COM *Preisposition*

## [1.0.59] - 01. Dezember 2025

### Geändert
- ENUM *verbrauchsart* wurde von Typ "string" zu "array(string)" korrigiert

## [1.0.58] - 16. Juli 2025

### Hinzugefügt
- ENUM *VerwendungszweckBilanzkreis* angelegt

### Geändert
- BO *Marktteilnehmer* wurde um bilanzkreis (string) und verwendungszweckBilanzkreis (enum) erweitert

## [1.0.57] - 16. Juli 2025

### Geändert
- Komponente *Handelsunstimmigkeitsbegruendung* wurde erweitert um *anerkennungsmeldung* (string zur Abbildung der Nachrichtennummer aus der Anerkennungsmeldung (APERAK)

## [1.0.56] - 30. Juni 2025

### Geändert
- Im BO *Marktlokation*, *Tranche* und *TechnischeRessource* wurde die *verbrauchsart* in ein Array geändert um mehrere Verbrauchsarten abbilden zun können
- In der Komponente *Zaehlerwerk* wurde die *verbrauchsart* in ein Array geändert um mehrere Verbrauchsarten abbilden zun können

Das Format basiert auf [Keep a Changelog](https://keepachangelog.com/de/1.1.0/),
und dieses Projekt folgt der [Semantischen Versionierung](https://semver.org/lang/de/).
