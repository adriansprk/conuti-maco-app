# Prozessübersicht

# Prozessübersicht

![LW24h mit Abhängigkeiten - Storno (alle Rollen)(1).png](https://api.apidog.com/api/v1/projects/816353/resources/367043/image-preview)

<Steps>
  <Step title="Prozessauslöser - Event" defaultOpen={false}>
    <Tabs>
      <Tab title="Übersicht">
 
        <Card title="START_VERSAND_ANF_STORNO"
              href="https://doc.macoapp.de/anfrage-nach-stornierung-21893877e0.md">
            Anfrage nach Stornierung starten
        </Card>

      </Tab>        
      <Tab title="📄START_VERSAND_ANF_STORNO">
          <Accordion title="[NB|LF|MSB] START_VERSAND_ANF_STORNO" defaultOpen={false}>
                 <DataSchema id="9714061" />   
          </Accordion>
      </Tab>
      <Tab title="📄55022 Anfrage nach Stornierung">
          <Accordion title="PI_55022" defaultOpen={false}>
               <DataSchema id="5562216" />
          </Accordion>
      </Tab>
    </Tabs>

  </Step>
  <Step title="Schnittstellen schreibend">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Aktualisieren der Prozessdaten"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14017182e0.md">
              Übergabe der initialen Prozessdaten an das Backend
          </Card>    
      </Tab>
       <Tab title="📄55022 Anfrage nach Stornierung">
          <Accordion title="PI_55022" defaultOpen={false}>
                 <DataSchema id="5562216" />
          </Accordion>
       </Tab>
      
    </Tabs>
  </Step>
  
  <Step title="Prozessinitiierung Backend">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Erstellen Prozessdaten für Prüfi 55022"
                href="https://doc.macoapp.de/prozessdaten-erstellen-14017183e0.md">
              Übergabe der initialen Prozessdaten an das Backend
          </Card>
      </Tab>        
      <Tab title="📄55022 Anfrage nach Stornierung">
          <Accordion title="PI_55022" defaultOpen={false}>
               <DataSchema id="5562216" />
          </Accordion>
      </Tab> 
    </Tabs>
  </Step>
    

    <Step title="Schnittstellen schreibend">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Aktualisieren der Prozessdaten"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14017182e0.md">
              Übergabe der pos. (55023) sowie neg. (55024) Rückmeldung vom Beteiligte aus Ursprungsnachricht.
          </Card>    
      </Tab>        
      <Tab title="📄55023 Bestätigung Anfrage Stornierung">
          <Accordion title="PI_55023" defaultOpen={false}>
                 <DataSchema id="5562217" />
          </Accordion>
          
          
        </Tab>
      <Tab title="📄55024 Ablehnung Anfrage Stornierung">
          <Accordion title="PI_55024" defaultOpen={false}>
                 <DataSchema id="5242370" />
          </Accordion>
          
          
      </Tab>
    </Tabs>
  </Step>
</Steps>





