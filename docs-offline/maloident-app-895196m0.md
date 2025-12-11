# MaloIdent APP

> **SaaS-Lösung für die Ermittlung der MaLo-ID der Marktlokation**

MaloIdent ist eine eigenständige SaaS-Lösung, die den Use-Case "Ermittlung der MaLo-ID der Marktlokation" für die Marktrollen Lieferant und Netzbetreiber umsetzt. Sie kann unabhängig von der bestehenden Infrastruktur betrieben werden und basiert auf dem Framework der MACO APP.

---

### Zusammenfassung

MaloIdent fokussiert sich auf den Prozess zur Ermittlung der MaLo-ID. Die Lösung umfasst:

- Die definierten Prozesse gemäß Beschluss BK6-22-024 GPKE Teil 2
- Das Entscheidungsbaumdiagramm (EBD) E\_0594
- Schnittstellen für Datenermittlung, Prozessanstoß und -abschluss
- Verarbeitung ein- und ausgehender API-Daten (inkl. Mapping in den BO4E-Standard)
- Anbindung an SM-PKI-Infrastrukturen (Standardumsetzung durch Procilon)

MaloIdent wird mandantenfähig (pro ILN) als SaaS bereitgestellt, erfordert minimalen Integrationsaufwand und kann bei Bedarf durch CONUTI in SAP eingebunden werden.

![maloident.png](https://api.apidog.com/api/v1/projects/816353/resources/352697/image-preview)

---


### Verantwortungsbereich Procilon

Procilon betreibt die Sicherheits- und Kommunikationsinfrastuktur:

- **API-Absicherung (Lieferant)**: Absicherung des API-Aufrufes (Nachrichtenformat JSON) mit mTLS-Auth und Signatur mittels SM-PKI Zertifikaten (Rolle Lieferant) in Form eines Forward Proxy
- **API-Absicherung (Netzbetreiber)**: Absicherung eingehender API-Verbindungen mit mTLS-Auth und Signaturprüfung mittels SM-PKI Zertifikaten (Rolle Netzbetreiber) in Form eines Reverse Proxy und Weiterleitung der Anfrage an die MCS
- **Verzeichnisdienst**: Bereitstellung der API-Endpunkte über einen Verzeichnisdienst
- **Web-Oberfläche**: Verwaltung der API-Endpunkte in proTECTr (WebAPI Fachanwendung)
- **REST-API**: Möglichkeit der Registrierung der API-Endpunkte des Fachverfahrens über REST-API
- **Zertifikate**: Bereitstellung der WebAPI-Zertifikate (AS4-Zertifikate sind nicht nutzbar)

---

### Verantwortungsbereich MCS

Die MCS (Market Communication Service) fungiert als monitorbare Datendrehscheibe zwischen MPS und Procilon:

- **Funktionalitäten**: Monitoring, Queue-Verwaltung, Archivierung
- **Mapping**: Microservices sorgen für das Mapping zwischen Bo4E und BDEW Web-Api Schema
- **Datenübertragung**: Absicherung durch API-Key und Token-Mechanismen

---

### Verantwortungsbereich MPS

Im MPS (Market Process Service) wird die fachliche Prozessabbildung vorgenommen:

- **Prozesse (Lieferant)**: Anstoßen der MaloIdent Anfragen aus der Oberfläche oder einem Backend, sowie Zuordnung der Antworten des NB
- **Prozesse (Netzbetreiber)**: Abfrage Malo Liste gemäß Identifikationskriterien aus dem Backend, sowie EBD Prüfung und Erzeugung der marktkonformen Antwort
- **Entscheidungsbaumdiagramm**: Vollumfängliche Abbildung und Visualisierung für Nachvollziehbarkeit
- **Frontend**: Darstellung von Klärfällen, Prozessen und Fristen
- **Standardisierung**: Alle Schnittstellen dokumentiert in Gravitee

---

### Ausschlusskriterien

- Im Standard keine Umsetzung von Klärfällen und Individualprüfungen im EBD.
- Anbindungen an andere Backend-Systeme als SAP sind individuell zu betrachten.
- Anbindung von anderen SM PKI Anbietern als procilon sind individuell zu betrachten.
- Betrieb erfolgt in einem mandantengetrennten Cluster innerhalb der AWS. Ein kundeneigener Cluster ist über eine individuelle Projektplanung möglich.
- Umsetzungen mehrere Backendsysteme pro Mandant werden individuell bewertet.

---

### Glossar

- **MaLo-ID**: Marktlokations-ID, eine eindeutige Kennung für Marktlokationen im Energiesektor.
- **SaaS**: Software as a Service, eine Methode der Softwarebereitstellung über das Internet.
- **SM-PKI**: Smart Meter Public Key Infrastructure, ein Sicherheitsstandard für digitale Signaturen.
- **BO4E**: Business Objects for Energy, ein Datenmodell für die Energiewirtschaft.
- **EBD**: Entscheidungsbaumdiagramm, eine schematische Darstellung von Entscheidungsprozessen.
- **ILN**: Internationale Lokationsnummer, dient zur Identifikation von Marktteilnehmern.
- **GPKE**: Geschäftsprozesse zur Kundenbelieferung mit Elektrizität, regulatorische Vorgaben der Bundesnetzagentur.


