# Stammdatenänderung vom Lieferant (verantwortlich) ausgehend

# Prozessübersicht

![Stammdatenänderung vom Lieferanten (verantwortlich) (Lieferant).png](https://api.apidog.com/api/v1/projects/816353/resources/379789/image-preview)
<Steps>
  <Step title="Prozessauslöser - Event">
    
  <Tabs>
      <Tab title="Übersicht">         
          
        <CardGroup cols={3}>
           <Card title="Stammdatenänderung vom Lieferanten"
              href="https://doc.macoapp.de/stammdaten%C3%A4nderung-vom-netzbetreiber-verantwortlich-14994280e0.md">
            Triggert den Versand von Stammdatenänderungen vom verantwortlichen Lieferanten an Marktpartner
        </Card> 
            
          <Card title="55109">
              Daten der MaLo an NB
          </Card>
          <Card title="55230">
              Daten der NeLo an NB
          </Card>
          <Card title="55110">
              Daten der MaLo an MSB
          </Card>
          <Card title="55693">
              Daten der TR an NB
          </Card>
        </CardGroup>
      
      </Tab>   
          
      
      <Tab title="START_VERSAND_SDAE">
          <Accordion title="START_VERSAND_SDAE" defaultOpen={false}>
              

<DataSchema id="5854731" />
          </Accordion>
       </Tab>
      <Tab title="📄55109">
          <Accordion title="PI_55109" defaultOpen={false}>
                 
<DataSchema id="5562239" />
          </Accordion> 
      </Tab>    
      <Tab title="📄55230">
          <Accordion title="PI_55230" defaultOpen={false}>
               
<DataSchema id="5562257" />
          </Accordion> 
      </Tab>  
      <Tab title="📄55110">
          <Accordion title="PI_55110" defaultOpen={false}>
                
<DataSchema id="5562240" />
          </Accordion> 
      </Tab>
      <Tab title="📄55693">
          <Accordion title="PI_55693" defaultOpen={false}>
            
<DataSchema id="16611140" />
          </Accordion> 
      </Tab>
          
    </Tabs>
  </Step>   
  
   
    
    <Step title="Schnittstelle aktualisieren der Prozessdaten">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Aktualisieren der Prozessdaten"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14666382e0.md">
              Übergabe der empfangenen (55137, 55232, 55136, 55694) Rückmeldung an das Backend
          </Card>
      </Tab>   
          
      <Tab title="📄55137">
          <Accordion title="PI_55137" defaultOpen={false}>
             
<DataSchema id="5562243" />
          </Accordion> 
      </Tab>
      <Tab title="📄55232">
          <Accordion title="PI_55232" defaultOpen={false}>
             
<DataSchema id="5562258" />
          </Accordion> 
      </Tab>  
      <Tab title="📄55136">
          <Accordion title="PI_55136" defaultOpen={false}>
               
<DataSchema id="5562242" />
          </Accordion> 
      </Tab>      
      <Tab title="📄55694">
          <Accordion title="PI_55694" defaultOpen={false}>
                
<DataSchema id="16611142" />


          </Accordion> 
      </Tab>  
          
    </Tabs>
 </Step>
<Step title="Schnittstelle aktualisieren der Prozessdaten">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Aktualisieren der Prozessdaten"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14017182e0.md">
              Übergabe der empfangenen Statusmeldung (21047) an das Backend
          </Card>
      </Tab>        
      <Tab title="21047">
          <Accordion title="PI_21047" defaultOpen={false}>
              <DataSchema id="5718596" />
          </Accordion>
          
      </Tab>
    </Tabs>
  </Step>
</Steps>

