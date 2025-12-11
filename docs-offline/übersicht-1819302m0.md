# Übersicht

## 📄 Aufbau der Prozess-Steckbriefe

Um langes Suchen zu vermeiden, folgt unsere Prozessdokumentation einer **"Single Point of Truth"**-Logik. Alle technischen und fachlichen Informationen sind **pro Prozess gebündelt**.

Jede Prozess-Seite enthält standardmäßig folgende Sektionen:

### 1. Visuelle Prozesslandkarte
Ein detailliertes **Swimlane-Diagramm**, das den gesamten Ablauf visualisiert.
* **Beteiligte Komponenten:** Backend, MPS (fachliche MACO), MCS (technische MACO), Marktpartner
* **Kommunikationsfluss:** Wer sendet wann an wen (Marktpartner)?
* **Prüfidentifikatoren:** Welche logischen Prüfungen (z.B. EBD-Checks) werden durchlaufen?

### 2. Prozessauslöser (Event-Trigger)
Die technische Definition des Startpunkts. Hier wird beschrieben, welches Event den Prozess initiiert (z.B. `START_ABMELDEANFRAGE`).
* **Payload-Spezifikation:** Detaillierte Beschreibung der JSON-Struktur, die an die API übergeben werden muss.
* **Pflichtfelder:** Definition der notwendigen Transaktions- und Stammdaten, sowie Zusatzdaten.

### 3. Lesende Schnittstellen (Context Enrichment)
Definition der BO4E-Objektschnittstellen, die die MACO APP während der Verarbeitung anfragt, um das Event mit Daten anzureichern.
* **Beispiel:** Nach dem Trigger `START_ABMELDEANFRAGE` muss die App z.B. die *Marktlokation* oder den *Energieliefervertrag* lesend aus dem Backend abrufen, um die EDIFACT-Nachricht zu bauen.

### 4. Schreibende Schnittstellen (Feedback Loop)
Spezifikation der Rückkanäle in das Backend. Hier wird dokumentiert, wie Antworten des Marktes (z.B. eine Zustimmung, Ablehnung oder APERAK) an das ERP-System zurückgespielt werden.
* **Prozessdaten-Aktualisierung:** Welcher API-Endpunkt wird aufgerufen, um den Status im Backend fortzuschreiben?
* **Marktantworten:** Struktur der Daten, die aus der EDIFACT-Antwort extrahiert und verbucht werden.



## 🏗️ Struktur-Übersicht

Die Prozessdokumentation gegliedert sich in folgende Bereiche :

```mermaid
mindmap
  root((MACO APP))
    Kundenindividuelle Steuerprozesse
      Steuerprozess Lieferbeginn
      Kundenlogik ...
    Standardprozesse nach Marktrolle
      Lieferant
      Netzbetreiber
      Messstellenbetreiber
    CarveOut
      MaLo-Ident
