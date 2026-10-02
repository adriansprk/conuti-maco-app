# Abkürzungsverzeichnis

## #

### 24hLW / LFW24
**24-Stunden-Lieferantenwechsel**
> Ein beschleunigter Marktprozess, der es ermöglicht, den Stromlieferanten innerhalb eines Tages zu wechseln; die MACO APP automatisiert diesen zeitkritischen Ablauf.

## A

### APERAK
**Application Error and Acknowledgement**
> Eine EDIFACT-Nachricht, die als "Empfangsbestätigung" dient oder fachliche Fehler meldet, wenn der Inhalt einer Nachricht vom Empfängersystem abgelehnt wurde.

### AS2
**Applicability Statement 2**
> Ein älteres, aber noch weit verbreitetes Übertragungsprotokoll für EDI-Nachrichten, das oft in bestehenden Integrationslandschaften (wie Seeburger BIS) neben dem modernen AS4 koexistiert.

### AS4
**Applicability Statement 4**
> Der aktuelle, verschlüsselte Übertragungsstandard für die Marktkommunikation, der die unsichere E-Mail-Kommunikation abgelöst hat und von der MACO APP nativ unterstützt wird.

### AWS
**Amazon Web Services**
> Die Cloud-Infrastruktur, auf der die MACO APP als Software-as-a-Service (SaaS) gehostet wird, um Skalierbarkeit und Ausfallsicherheit zu gewährleisten.

## B

### B2BbP
**B2B by Practice**
> Eine Open-Source-Lösung für Enterprise Application Integration Herausforderungen, die als technisches Fundament der Conuti Plattform MCS mit erweitertem und optimiertem Funktionsumfang dient.

### BDEW WebApi
**BDEW Web API**
> Eine spezifische Schnittstellendefinition des Bundesverbands der Energie- und Wasserwirtschaft, die z.B. für den MaLo-Ident-Prozess genutzt wird, um Anfragen standardisiert zu versenden.

### BO4E
**Business Objects for Energy**
> Ein standardisiertes, modernes Datenformat (oft JSON-basiert), das als "gemeinsame Sprache" dient, um die kryptischen EDIFACT-Daten in verständliche Geschäftsobjekte für das Backend zu übersetzen.

### BPO
**Business Process Outsourcing**
> Ein Modell, bei dem die MACO APP bzw. Conuti nicht nur die Software stellt, sondern auch die operative Abwicklung der Marktkommunikation als Dienstleistung übernimmt.

### BSFZ
**Bescheinigungsstelle Forschungszulage**
> Ein Siegel, das bestätigt, dass hinter der Entwicklung der App anerkannte Forschungs- und Innovationsarbeit steckt – gut für das Vertrauen in die Zukunftsfähigkeit.

## C

### COMDIS
**Commercial Dispute**
> Die Nachricht für kaufmännische Beanstandungen. Wird genutzt, wenn eine Rechnung (INVOIC) falsch ist oder Messwerte nicht passen, um einen Klärfall zu eröffnen.

### CONTRL
**Control Message**
> Die "Türsteher"-Nachricht im EDIFACT-Verkehr, die sofort prüft und meldet, ob eine empfangene Datei syntaktisch korrekt ist oder Strukturfehler aufweist.

### CRM
**Customer Relationship Management**
> Das Kundenverwaltungssystem (z.B. Salesforce, SAP CRM), das oft der Startpunkt für Prozesse wie den Lieferantenwechsel ist und via Trigger die MACO APP anstößt.

## E

### E_0621 / E_0622 / E_0623
**Entscheidungsbaum-Prüfcodes**
> Spezifische Prüfschritte aus den Entscheidungsbaum-Diagrammen (EBD) der BNetzA, die z.B. bei der Prüfung einer Anmeldung (E_0621) durchlaufen werden müssen und Fehler oder Zustimmung signalisieren.

### EAI
**Enterprise Application Integration**
> Das Konzept der nahtlosen Verknüpfung verschiedener Unternehmensanwendungen, hier konkret die Anbindung der MACO APP an das ERP-Backend (z.B. SAP) und andere Systeme.

### EBD
**Entscheidungsbaum-Diagramm**
> Die strikten logischen Regelwerke der BNetzA, die genau vorgeben, wie auf eine Marktnachricht (z.B. als Netzbetreiber) zu reagieren ist.

### ECS
**Energy Communication System**
> Eine klassische Komponente im SAP IS-U Umfeld zur Marktkommunikation, die durch moderne Lösungen wie die MACO APP ergänzt oder teilweise abgelöst werden kann.

### EDIFACT
**Electronic Data Interchange for Administration, Commerce and Transport**
> Das weltweite, aber extrem sperrige Standardformat für den Datenaustausch, das die MACO APP im Hintergrund generiert, damit die Systeme der Marktpartner sich verstehen.

## F

### FUM
**Formatanpassung**
> Die gesetzlich vorgeschriebenen, regelmäßigen Updates der Datenformate (meist zum 1.4. und 1.10.), die von der MACO APP zentral eingespielt werden, um das Backend zu entlasten.

## G

### GeLi
**Geschäftsprozesse Lieferantenwechsel Gas**
> Das Regelwerk der Bundesnetzagentur, das beschreibt, wie der Lieferantenwechsel und die Stammdatenänderung im Gasmarkt abzulaufen haben.

### GPKE
**Geschäftsprozesse zur Kundenbelieferung mit Elektrizität**
> Das Pendant zur GeLi für den Strommarkt; die "Bibel" für alle Prozesse rund um An- und Abmeldung von Stromkunden.

## I

### IDEX
**Intercompany Data Exchange**
> Eine klassische SAP-Lösungskomponente für den Datenaustausch, die ab 2027 von der SAP abgekündigt ist. Die MACO APP dient hier als moderner Ersatz, um die Marktkommunikation weiter abzuwickeln zu können.

### IDOCXML
**Intermediate Document in XML**
> Ein SAP-internes Datenformat, das oft als Zwischenschritt genutzt wird, bevor die Daten in das offizielle EDIFACT-Format konvertiert werden.

### IFTSTA
**International Multimodal Status Report**
> Ein Statusbericht, der im deutschen Markt oft genutzt wird, um den Status von Geschäftsdatenanfragen zu melden oder im Bereich Einspeisemanagement.

### INVOIC
**Invoice message**
> Die elektronische Rechnung oder Gutschrift für Netznutzungsentgelte, Messentgelte oder Mehr-/Mindermengen.

## L

### LF
**Lieferant**
> Die Marktrolle des Energieversorgers, der den Endkunden beliefert und für den die MACO APP spezifische Prozesssichten bereitstellt.

### LFA
**Lieferant Alt**
> Bezeichnet im Wechselprozess den bisherigen Versorger, dessen Vertragsverhältnis durch eine Kündigung beendet wird.

### LFZ
**Lieferant Zukunft**
> Bezeichnet den neuen Versorger, der den Kunden übernimmt und den Wechselprozess durch Anmeldung bei Netzbetreiber initiiert.

## M

### MaBiS
**Marktregeln für die Durchführung der Bilanzkreisabrechnung Strom**
> Regelt den Austausch von Zählpunkten und Energiemengen zwischen Netzbetreibern und Bilanzkreisverantwortlichen, um das Stromnetz bilanziell im Gleichgewicht zu halten.

### MACO
**Marktkommunikation**
> Der Sammelbegriff für den gesamten Datenaustausch im Energiemarkt; die App heißt so, weil sie genau diesen komplexen Teilbereich kapselt.

### MaLo
**Marktlokation**
> Das rein bilanzielle Konstrukt (früher Zählpunkt), an dem Energie verbraucht oder eingespeist wird – unabhängig von der technischen Messung.

### MaLo-Ident
**Marktlokations-Identifikation**
> Ein spezifischer Prozess (und Modul der App), um unbekannte Marktlokationen via API (oft beim Netzbetreiber) zu identifizieren, was für den 24h-Wechsel kritisch ist.

### MaLo-ID
**Marktlokations-Identifikationsnummer**
> Die eindeutige, 11-stellige Nummer zur Identifikation einer Marktlokation, die im Rahmen der Marktkommunikation zwingend ausgetauscht werden muss.

### MCS
**Market Communication System**
> Die von Conuti auf Basis der Open-Source-Lösung B2BbP entwickelte Plattform, die den Kern der MACO APP bildet und durch erweiterte Funktionen optimiert wurde.

### MeLo
**Messlokation**
> Der technische Ort, an dem die physikalische Messung stattfindet (also dort, wo der Zähler tatsächlich an der Wand hängt).

### Meter2Cash
**Meter-to-Cash**
> Der gesamte Geschäftsprozess von der Ablesung des Zählers bis zum Geldeingang beim Versorger; die MACO APP deckt hier den kritischen Teil der Datenübermittlung ab.

### MFT
**Managed File Transfer**
> Sichere und verwaltete Dateiübertragung, oft ein Teil der Integrationsplattform, um Massendaten sicher zwischen Systemen zu bewegen.

### MSB
**Messstellenbetreiber**
> Die Marktrolle, die für den Einbau, den Betrieb und die Wartung der Zähler (Smart Meter) sowie die Messwertübermittlung verantwortlich ist.

### MSCONS
**Metered Services Consumption Report**
> Das Standardformat für die Übermittlung von Messwerten (Zählerstände, Lastgänge) und Energiemengen.

## N

### NB
**Netzbetreiber**
> Das Unternehmen, dem die Leitungen und Rohre gehören und das für die physische Durchleitung der Energie sowie die Verwaltung der Lokationen zuständig ist.

## O

### ORDERS
**Purchase Order**
> Eine Bestellung, die im Messwesen (WiM) genutzt wird, um Leistungen (z.B. Gerätewechsel) zu beauftragen oder Verträge anzubahnen.

### ORDRSP
**Purchase Order Response**
> Die Antwort auf eine Bestellung (ORDERS); bestätigt oder lehnt die angeforderte Leistung oder das Vertragsangebot ab.

## P

### PARTIN
**Party Information**
> Dient dem Austausch von Kommunikationsdaten der Marktpartner (z.B. Änderung von E-Mail-Adressen oder Zertifikaten).

### PI / PO
**Process Integration / Process Orchestration**
> Ältere, aber sehr verbreitete SAP-Middleware-Plattformen ("On-Premise"), die oft als Brücke zwischen dem SAP IS-U und externen Lösungen wie der MACO APP dienen.

### PRICAT
**Price Catalogue**
> Die Preisliste. Wird genutzt, um Preisblätter (z.B. für Netznutzung oder Messstellenbetrieb) elektronisch auszutauschen.

## Q

### QUOTES
**Quote**
> Das Angebot. Die Antwortnachricht auf eine Preisanfrage (REQOTE).

## R

### REMADV
**Remittance Advice**
> Das Zahlungsavis. Schlüsselt auf, welche Rechnungen (INVOIC) mit einer getätigten Sammelüberweisung beglichen wurden.

### REQOTE
**Request for Quote**
> Die Preisanfrage oder Angebotsanforderung, oft genutzt im Messwesen für individuelle Angebote.

### REST-API
**Representational State Transfer Application Programming Interface**
> Eine moderne Schnittstellentechnologie, die es externen Systemen erlaubt, einfach und in Echtzeit Daten mit der MACO APP auszutauschen.

## S

### SaaS
**Software as a Service**
> Ein Vertriebsmodell, bei dem die Software nicht gekauft und installiert wird, sondern als Dienstleistung über das Internet genutzt und nach Nutzung bezahlt wird.

### SCM
**Supply Chain Management**
> Lieferkettenmanagement; im Energiekontext oft relevant für die Beschaffung und Prognose von Energiemengen.

### Seeburger BIS
**Seeburger Business Integration Server**
> Eine weit verbreitete Konverter- und Integrationsplattform im Energiemarkt, zu der die Conuti Alternativen oder Ergänzungen bietet.

### SFTP
**Secure File Transfer Protocol**
> Ein Standardprotokoll zur sicheren Dateiübertragung, das oft für den Batch-Austausch von Daten zwischen der MACO APP und älteren Legacy-Systemen genutzt wird.

### SM PKI
**Smart Meter Public Key Infrastructure**
> Die hochsichere Infrastruktur zur Verwaltung digitaler Zertifikate, die notwendig ist, um die Kommunikation intelligenter Messsysteme abzusichern.

## U

### UTILMD
**Utilities Master Data**
> Das wichtigste Format für Stammdaten- und Wechselprozesse (Anmeldung, Kündigung, Stammdatenänderung). Es deckt den Großteil der GPKE/GeLi-Prozesse ab.

### UTILTS
**Utilities Time Series**
> Ein Format speziell für den Austausch von Zeitreihen wie Prognose- und Fahrplandaten.

## W

### WiM
**Wechselprozesse im Messwesen**
> Das Regelwerk für alle Prozesse, die den Austausch oder die Änderung des Messstellenbetreibers und der Gerätetechnik betreffen.
