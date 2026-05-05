# GAS Stammdatenänderung vom MSB (verantwortlich) (MSB)

![LW24h mit Abhängigkeiten - GAS SDÄ vom MBS (verantwortlich) ausgehend (Rolle MSB).png](https://api.apidog.com/api/v1/projects/816353/resources/372353/image-preview)

<Steps>
  <Step title="Prozessauslöser - Event" defaultOpen={false}>
    <Tabs>
      <Tab title="Übersicht">
 
        <Card title="START_VERSAND_SDAE"
              href="https://doc.macoapp.de/stammdaten%C3%A4nderung-vom-messstellenbetreiber-verantwortlich-15235558e0.md">
            Triggert den Versand von Stammdatenänderungen vom verantwortlichen Messstellenbetreiber an Marktpartner
        </Card>
              
      </Tab>   
          
      <Tab title="📄44116">
          <Accordion title="PI_44116" defaultOpen={false}>
                <DataSchema id="5242481" />
          </Accordion> 
      </Tab>
      <Tab title="📄44159">
          <Accordion title="PI_44159" defaultOpen={false}>
                <DataSchema id="5242482" />
          </Accordion> 
      </Tab>  
     </Tabs>
  </Step>   
  
 <Step title="Schnittstelle aktualisieren der Prozessdaten">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Aktualisieren der Prozessdaten"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14669402e0.md">
              Übergabe der empfangenen (44116, 44119, 44159, 44161) Rückmeldung an das Backend
          </Card>
      </Tab>   
          
     <Tab title="📄44116">
          <Accordion title="PI_44116" defaultOpen={false}>
            
          </Accordion> 
      </Tab>
          
      <Tab title="📄44119">
          <Accordion title="PI_44119" defaultOpen={false}>
               <DataSchema id="8347936" />
          </Accordion> 
      </Tab>  
      

      <Tab title="📄441159">
          <Accordion title="PI_44159" defaultOpen={false}>
            
          </Accordion> 
      </Tab> 
      
      <Tab title="📄44161">
          <Accordion title="PI_44161" defaultOpen={false}>
            
<DataSchema id="8347956" />
          </Accordion> 
      </Tab>
    </Tabs>
 </Step>
</Steps>

