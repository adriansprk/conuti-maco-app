# Änderungsprotokoll BO4E Objekte



Alle wesentlichen Änderungen an den BO4E Objekte werden in dieser Datei dokumentiert.

:::info[]
*Hinweis: Schnittstellen und Datenobjekte werden getrennt dokumentiert. Dieses Protokoll beschreibt ausschließlich Änderungen an den BO4E-Geschäftsobjekten und Komponenten – neue oder umbenannte Felder, erweiterte Enums.
Änderungen an den an den Schnittstellen (Endpunkte, Parameter, Verhalten) – sind im [Änderungsprotokoll Schnittstellen](https://doc.macoapp.de/changelog.md) dokumentiert.*
:::

## [1.6.17] - 25. August 2026
### Hinzugefügt
- COM *StatusmitteilungPosition* wurde erweitert um die Freitextfelder "fehlerbeschreibungText", "begruendungText" und "allgemeineInformationenText" vom Typ "string"

## [1.6.16] - 24. August 2026
### Hinzugefügt
- BO *Berechnungsformel* wurde erweitert um "berechnungsformel" (string), "datenqualitaet" vom Typ ENUM "Datenqualitaet", "parameterIDs" (Array of string) und "aufteilungsfaktoren" (Array of COM "Aufteilungsfaktor")
- COM *Aufteilungsfaktor* wurde neu angelegt mit den Feldern "bezeichnungAufteilungsfaktor" (string) und "faktor" (float)
- COM *Rechenschritt* wurde erweitert um "marktlokationsId" und "bezeichnungOperanden" vom Typ "string"

## [1.6.15] - 12. August 2026
### Hinzugefügt
- COM *ApnKommunikationsdatenZugriffsparameter* wurde neu angelegt mit den Feldern "apnName", "nutzer" und "passwort" vom Typ "string"
- COM *AuftragPosition* wurde erweitert um "apnKommunikationsdatenZugriffsparameter" vom Typ "ApnKommunikationsdatenZugriffsparameter"
- ENUM *EventName* wurde erweitert um den Wert "START_GERAETEWECHSEL"

## [1.6.14] - 07. August 2026
### Hinzugefügt
- ENUM *EventName* wurde erweitert um die Werte "START_UEBERM_DEFINITION", "START_UEBERSICHT_LEISTUNGSKURVENDEF", "START_UEBERSICHT_SCHALTZEITDEF", "START_UEBERSICHT_ZAEHLZEITDEF", "START_REKLAMATION_DEFINITION" und "START_VERSAND_STATUSMELDUNG"

## [1.6.13] - 07. Juli 2026
### Hinzugefügt
- ENUM *EventName* wurde erweitert um die Werte "START_GERAETEUEBERNAHME", "START_ANGEBOT_GERAETEUEBERNAHME" und "START_BESTELLUNG_GERAETEUEBERNAHME"
- COM *AuftragPosition* wurde erweitert um "gueltigAb" vom Typ "date-time"

## [1.6.12] - 29. Juni 2026
### Hinzugefügt
- ENUM *EventName* wurde erweitert um den Wert "START_PARTIN"

## [1.6.11] - 23. Juni 2026
### Hinzugefügt
- COM *Preisstaffel* wurde erweitert um "zeitbasis" vom Typ ENUM "Zeiteinheit" (Zeitdauer, auf die sich der Preis bezieht)

## [1.6.10] - 19. Juni 2026
### Hinzugefügt
- ENUM *EventName* wurde erweitert um den Wert "START_UEBERMITTLUNG_ENFG"

## [1.6.9] - 17. Juni 2026
### Hinzugefügt
- COM *AnsichtSender* wurde neu angelegt mit den Feldern "verwendungAb", "verwendungBis" (date-time), "leistungsperiode" (string), "menge" (COM "Menge") und "tarifstufe" (ENUM "Tarifstufe")
- COM *ZeitintervallMenge* wurde neu angelegt mit den Feldern "verwendungAb", "verwendungBis" (date-time) und "menge" (COM "Menge")
- COM *StatusmitteilungPosition* wurde erweitert um "lokationsTyp" (ENUM "Lokationstyp"), "statusObjekt" (ENUM "Statusobjekt"), "antwortstatusCodeliste", "vorgangsreferenznummer", "mitteilungsnummer", "anfragereferenznummer", "fertigstellungsdatum", "lieferdatum", "sendungsposition", "gueltigAb", "referenzMalo", "referenzPreisschluesselstamm", "referenzArtikelID", "startdatum", "angebotsnummer", "anfrageReferenz", "vertragsende", "gueltigkeitsZeitspanne", "ansichtSender" (Array of COM "AnsichtSender") und "privilegierteEnergiemenge" (COM "ZeitintervallMenge")
- ENUM *EventName* wurde erweitert um den Wert "START_ENDE_MSB_STILLLEGUNG"

## [1.6.8] - 08. Juni 2026
### Hinzugefügt
- CDOC *Transaktionsdaten* wurde erweitert um "lokationsTyp" vom Typ ENUM "Lokationstyp"

## [1.6.7] - 03. Juni 2026
### Hinzugefügt
- COM *Angebotsposition* wurde erweitert um "konfigurationsprodukt" vom Typ "string"
- COM *Geraeteeigenschaften* wurde erweitert um "firmwareVersion", "herstellerTypbezeichnung", "simKartenNummer", "modemKennungIMSI", "tkProvider" und "ipVersion" vom Typ "string"
- COM *Preis* wurde erweitert um "minimaleMenge" und "maximaleMenge" vom Typ "integer"

## [1.6.6] - 01. Juni 2026
### Hinzugefügt
- COM *AuftragPosition* wurde erweitert um "endpunktAdresse" (COM "EndpunktAdresse"), "zertifikatsInformationen" (COM "Zertifikatsinformationen"), "wakeUpPort" (string) und "apnKommunikationsdaten" (string)
- COM *EndpunktAdresse* wurde neu angelegt mit den Feldern "gwaManagement", "gwaAdminService" und "gwaNTP" vom Typ "string"
- COM *Zertifikatsinformationen* wurde neu angelegt mit den Feldern "uriSubCA", "commonNameZertifikat" und "seriennummerZertifikat" vom Typ "string"
- ENUM *BildungTranchengroesse* wurde erweitert um den Wert "BERECHNUNGSFORMEL"
- BO *TechnischeRessource* wurde erweitert um "referenzTranche" vom Typ "string"

## [1.6.5] - 28. Mai 2026
### Geändert
- Feld in COM *Angebotsposition* wurde von "positionsbezeichung" zu "positionsbezeichnung" korrigiert

## [1.6.4] - 29. April 2026
### Hinzugefügt
- ENUM *EventName* wurde erweitert um die Werte "START_ANFORDERUNG_MESSWERTE", "START_BESTELLUNG_ABRECHNUNGSDATEN", "START_ERHEBUNG_MESSWERTE", "START_BESTELLUNG_SDAE", "START_VERSAND_LIEFERSCHEIN", "START_VERSAND_ANTWORT_NNA", "START_ANFRAGE_KONFIGURATION", "START_BESTELLUNG_KONFIGURATION", "START_BESTELLUNG_ANGEBOT_KONFIGURATION", "START_BESTELLUNG_ZAEHLZEITDEFINITION", "START_VERSAND_BESTANDSLISTE", "START_VERSAND_ANF_STORNO", "START_VERSAND_BEST_BEEND_KONFIG", "START_VERSAND_STORNO_MSCONS", "START_BEGINN_MSB", "START_ENDE_MSB", "START_KUENDIGUNG_MSB", "START_GESCHAEFTSDATENANFRAGE" und "START_VERSAND_PREISBLATT_IMS"

## [1.6.3] - 22. April 2026
### Hinzugefügt
- BO *Geschaeftspartner* wurde erweitert um "ansprechpartner" vom Typ BO "Ansprechpartner"
- BO *Marktlokation* wurde erweitert um "technischeEinrichtungen" vom Typ Array of COM "TechnischeEinrichtung"
- BO *SteuerbareRessource* wurde erweitert um "keinKonfigurationsprodukt" vom Typ "boolean"
- BO *TechnischeRessource* wurde erweitert um "fernsteuerbarkeit" und "verguetungsverpflichtung" vom Typ "boolean"
- COM *TechnischeEinrichtung* wurde neu angelegt mit den Feldern "technischeEinrichtungenVorhanden" (boolean) und "verbrauchsart" (ENUM "Verbrauchsart")
- COM *Zaehlwerk* wurde erweitert um "verwendungszweckNB", "verwendungszweckLF", "verwendungszweckUENB" (string) und "keinProdukt" (boolean)
- ENUM *BildungTranchengroesse* wurde erweitert um den Wert "AUFTEILUNG_TECHNISCHE_RESSOURCEN"

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
