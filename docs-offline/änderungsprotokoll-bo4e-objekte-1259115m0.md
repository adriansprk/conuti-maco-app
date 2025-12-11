# Änderungsprotokoll BO4E Objekte



Alle wesentlichen Änderungen an den BO4E Objekte werden in dieser Datei dokumentiert.



## [Unveröffentlicht]
- ...

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
