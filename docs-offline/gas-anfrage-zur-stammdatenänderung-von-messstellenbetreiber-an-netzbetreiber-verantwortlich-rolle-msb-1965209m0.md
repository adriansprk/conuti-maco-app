# GAS Anfrage zur Stammdatenänderung von Messstellenbetreiber an Netzbetreiber (verantwortlich) ( Rolle MSB )


![LW24h mit Abhängigkeiten - GAS Anfrage SDÄ von MSB an NB (verantwortlich) (Rolle MSB).png](https://api.apidog.com/api/v1/projects/816353/resources/372354/image-preview)

<Steps>
  <Step title="Prozessauslöser - Event" defaultOpen={false}>
    <Tabs>
      <Tab title="Übersicht">
 
        <Card title="START_VERSAND_SDAE"
              href="https://doc.macoapp.de/stammdaten%C3%A4nderung-vom-messstellenbetreiber-verantwortlich-15235558e0.md">
            Triggert den Versand von Stammdatenänderungen vom verantwortlichen Messstellenbetreiber an Marktpartner
        </Card>
              
      </Tab>   
          
      <Tab title="📄44140">
          <Accordion title="PI_44140" defaultOpen={false}>
             
          </Accordion> 
      </Tab>
     </Tabs>
  </Step>   
  
 <Step title="Schnittstelle aktualisieren der Prozessdaten">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Aktualisieren der Prozessdaten"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14669402e0.md">
              Übergabe der empfangenen (44140, 44142, 44145) Rückmeldung an das Backend
          </Card>
      </Tab>   
          
     <Tab title="📄44140">
          <Accordion title="PI_44140" defaultOpen={false}>
            
          </Accordion> 
      </Tab>
          
      <Tab title="📄44142">
          <Accordion title="PI_44142" defaultOpen={false}>
    
<DataSchema id="8347944" />
          </Accordion> 
      </Tab>  
      

      <Tab title="📄44145">
          <Accordion title="PI_44145" defaultOpen={false}>
            
<DataSchema id="8347946" />
          </Accordion> 
      </Tab> 
      
    </Tabs>
 </Step>
</Steps>

