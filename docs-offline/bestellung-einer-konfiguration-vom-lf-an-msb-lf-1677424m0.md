# Bestellung einer Konfiguration vom LF an MSB ( LF )

Bestellung einer Konfiguration vom LF an MSB ( LF )


![LW24h mit Abhängigkeiten - Bestellung einer Konfiguration vom LF an MSB ( LF ).png](https://api.apidog.com/api/v1/projects/816353/resources/363944/image-preview)

<Steps>
  <Step title="Prozessauslöser - Event">
   <Tabs>
      <Tab title="Übersicht">
 
        <Card title="START_LIEFERENDE"
              href="https://doc.macoapp.de/lieferende-von-lieferant-an-netzbetreiber-14992421e0.md">
            Lieferende starten
        </Card>

      </Tab>        
      <Tab title="📄START_LIEFERENDE">
          <Accordion title="PI_35004" defaultOpen={false}>
               <DataSchema id="10740352" />
          </Accordion>
          
          <Accordion title="PI_17130" defaultOpen={false}>
                  <DataSchema id="5665542" />
          </Accordion>
          
          <Accordion title="PI_17131" defaultOpen={false}>
              <DataSchema id="10710206" />
          </Accordion>
          
          <Accordion title="PI_17123" defaultOpen={false}>
                  <DataSchema id="10711148" />
          </Accordion>
                    
      </Tab>
    </Tabs>
  </Step>
  <Step title="Schnittstellen schreibend">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Aktualisieren der Prozessdaten"
                href="https://doc.macoapp.de/prozessdaten-erstellen-14017183e0.md">
              Übergabe der Nachrichten (15004, 21033, 19132, 19124, 21043) an das Backend.
          </Card>    
      </Tab>
        <Tab title="📄15004 Angebot einer Konfiguration">
            <Accordion title="PI_15004" defaultOpen={false}>
                <DataSchema id="10270802" />
            </Accordion>
        </Tab>
       <Tab title="📄21033 Ablehnung der Anfrage">
            <Accordion title="PI_21033" defaultOpen={false}>
                <DataSchema id="10706853" />
            </Accordion>
       </Tab>
       <Tab title="📄19132 Mitteilung zur Bestellung einer Konfiguration">
            <Accordion title="PI_19132" defaultOpen={false}>
                <DataSchema id="10222259" />
            </Accordion>
       </Tab>
       <Tab title="📄19124 Mitteilung zur Änderung einer Zählzeitdefinition">
            <Accordion title="PI_19124" defaultOpen={false}>
               <DataSchema id="10709668" />
            </Accordion>
       </Tab>
       <Tab title="📄21043 Bestellungsantwort einer Konfiguration">
            <Accordion title="PI_21043" defaultOpen={false}>
                   <DataSchema id="10725055" />
            </Accordion>
       </Tab>
      
    </Tabs>
  </Step>
</Steps>

