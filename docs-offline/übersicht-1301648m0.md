# Übersicht

## Was ist BO4E und was bringt der Standard?
Die Business Objects for Energy (BO4E) wurden von einem Vereins‑Konsortium der Energiewirtschaft entwickelt, um den Datenaustausch zu standardisieren. Softwarehäuser und Dienstleister der Energieversorgungsbranche müssen heute für jeden Prozess individuelle Schnittstellen erstellen; Daten werden immer wieder transformiert und es entstehen Zeit‑ und Kostenaufwände. 
BO4E adressiert dieses Problem: Der Standard basiert auf differenzierten Geschäftsobjekten (Business Objects), die als Datentransferobjekte dienen. Ein Geschäftsobjekt stellt einen Gegenstand der energiewirtschaftlichen Welt dar (z. B. eine Lieferstelle oder einen Stromliefervertrag) und wird über klar definierte Strukturen ausgetauscht. Ziel des Standards ist der reibungslose Datenaustausch zwischen beliebigen Systemen ohne Transformationsverluste.

Die Nutzung von BO4E reduziert Implementierungsaufwände und beschleunigt die Realisierung neuer Geschäftsprozesse



## Wie ist BO4E aufgebaut?
BO4E ist modular strukturiert:

Business Objects (BO) – die Kernelemente. Sie repräsentieren komplexe Prozesse oder Gegenstände der Energiewirtschaft, beispielsweise Angebot, Auftrag, Rechnung oder Marktlokation. Ein Business Object enthält Attribute (z. B. Angebotsnummer, Lieferanschrift) und kann andere Objekte referenzieren.

Components (COM) – wiederverwendbare Komponenten. Sie bilden gemeinsame Strukturen wie Adresse, Zeitraum, Preisbestandteil oder Kontaktweg ab. Mehrere BOs greifen auf diese Komponenten zurück.

Enumerations (ENUM) – klar definierte Wertemengen. Enumerationen beschreiben zulässige Ausprägungen von Feldern, z. B. die Sparte (Strom, Gas, Wasser), die Rechnungsart oder die Einheit einer Energiemenge.

Durch diese Aufteilung lassen sich Daten konsistent modellieren. BOs nutzen COM‑Komponenten, und ENUMs sichern die Plausibilität von Feldwerten.

