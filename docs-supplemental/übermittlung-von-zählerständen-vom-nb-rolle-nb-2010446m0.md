# Übermittlung von Zählerständen vom NB (Rolle NB)

# Prozessübersicht


![LW24h mit Abhängigkeiten - Übermittlung von  Zählerständen vom NB (Rolle MSB).png](https://api.apidog.com/api/v1/projects/816353/resources/373142/image-preview)


<Steps>
  <Step title="Prozessauslöser - eingehende EDI">
    <Tabs>
      <Tab title="Übersicht">         
          <Card title="13017">
              Übermittlung von  Zählerständen vom NB
          </Card>
      </Tab> 
          <Tab title="📄13017">
          <Accordion title="PI_13017" defaultOpen={false}>
                 <DataSchema id="12586651" />
          </Accordion>
         </Tab>
      </Tabs>
  </Step> 
        
  <Step title="Schnittstellen lesend für APERAK">
      <Tabs>
      <Tab title="Übersicht">         
          
        <CardGroup cols={2}>
          <Card title="Messlokation lesen"
                href="https://doc.macoapp.de/messlokation-lesen-14017024e0.md">
              Lesen einer MeLo mittels LokationsId zu einem bestimmten Zeitpunkt
          </Card>
          <Card title="Zähler lesen" 
                href="https://doc.macoapp.de/z%C3%A4hler-lesen-14017031e0.md">
              Lesen eines Zählers mittels LokationsId zu einem bestimmten Zeitpunkt
          </Card>
<Card title="Marktlokation lesen" 
                href="https://doc.macoapp.de/marktlokation-lesen-14017020e0.md">
              Lesen eines Marktlokation mittels LokationsId zu einem bestimmten Zeitpunkt
          </Card>
        </CardGroup>
          
      </Tab>   
          
      <Tab title="📄Messlokation">
          <Accordion title="Messlokation" defaultOpen={false}>
                  <DataSchema id="5241973" />      
          </Accordion> 
        
          
      </Tab>
          
      <Tab title="📄Zähler">
          <Accordion title="Zähler" defaultOpen={false}>
                       <DataSchema id="5241991" />
          </Accordion> 
        
      </Tab> 
       <Tab title="📄Marktlokation">
          <Accordion title="Marktlokation" defaultOpen={false}>
                       <DataSchema id="5241973" />
          </Accordion> 
        
      </Tab>    
          
    </Tabs>
  </Step>
    
  <Step title="Prozessinitiierung Backend">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Erstellen Prozessdaten für Prüfi 13017"
                href="https://doc.macoapp.de/prozessdaten-erstellen-14017183e0.md">
              Übergabe der initialen Prozessdaten an das Backend
          </Card>
      </Tab>        
      <Tab title="13017 - Zählerstand vom NB (Strom)">
          <Accordion title="PI_13017" defaultOpen={false}>
                     <DataSchema id="12586651" />
          </Accordion>
       </Tab> 
    </Tabs>
  </Step>  
    
 
</Steps>

