# Bestellung einer Konfiguration vom LF an MSB ( LF )

Bestellung einer Konfiguration vom LF an MSB ( LF )


![LW24h mit Abhängigkeiten - Bestellung einer Konfiguration vom LF an MSB ( LF )(2).png](https://api.apidog.com/api/v1/projects/816353/resources/374557/image-preview)

<Steps>
  <Step title="Prozessauslöser - Event">
   <Tabs>
      <Tab title="Übersicht">
 
        <Card title="START_ANFRAGE_KONFIGURATION 35004"
         > 

        </Card>
             <Card title="START_BESTELLUNG_KONFIGURATION 17130"
             >
 
        </Card>
                       <Card title="START_BESTELLUNG_ANGEBOT_KONFIGURATION 17131"
                           >
 
        </Card>
                                 <Card title="START_BESTELLUNG_ZAEHLZEITDEFINITION"
        >
  
        </Card>

      </Tab> 
             <Tab title="35004">
 
        <Card title="START_ANFRAGE_KONFIGURATION"
         >
     <Accordion title="35004" defaultOpen>

<DataSchema id="13853759" />
</Accordion>
        </Card>
          
      </Tab> 
        <Tab title="17130">
 
                    <Card title="START_BESTELLUNG_KONFIGURATION 17123"
             ><Accordion title="17130" defaultOpen>

<DataSchema id="13853761" />

</Accordion>

        </Card>
          
      </Tab> 
              <Tab title="17131">
 
                                 <Card title="START_BESTELLUNG_ANGEBOT_KONFIGURATION 17131"
                           >
               <Accordion title="17131" defaultOpen>

<DataSchema id="13853762" />
</Accordion>
        </Card>
        
      </Tab> 
                     <Tab title="17123">
 
                                 <Card title="START_BESTELLUNG_ZAEHLZEITDEFINITION 17123"
                           >
               <Accordion title="17123" defaultOpen>

<DataSchema id="13853763" />
</Accordion>
        </Card>
        
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

