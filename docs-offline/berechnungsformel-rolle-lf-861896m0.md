# Berechnungsformel (Rolle LF)

# Prozessübersicht 

![LW24h mit Abhängigkeiten - Berechnungsformel an LF aus LB (LF).png](https://api.apidog.com/api/v1/projects/816353/resources/352466/image-preview)


<Steps>
  <Step title="Prozessauslöser - eingehende EDI">
     <Tabs>
      <Tab title="Übersicht"> 
        <Card title="25001">
          Berechnungsformel
        </Card>
      </Tab>         
      <Tab title="PI_25001">
      <Accordion title="PI_25001" defaultOpen={false}>
            <DataSchema id="8347882" />
      </Accordion>
      </Tab> 
    </Tabs>
  </Step>
   
  <Step title="Schnittstellen lesen für APERAK">
   <Tabs>
          <Tab title="Übersicht">
              
           <Card title="Marktlokation lesen"
             href="https://doc.macoapp.de/marktlokation-lesen-14017020e0.md">
             Lesen einer MaLo mittels LokationsId zu einem Zeitpunkt
           </Card>
           
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
         
          <Card title="Erstellen Prozessdaten für Prüfi 25001"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14017182e0.md">
              Übergabe der initialen Prozessdaten an das Backend
          </Card>
                    
      </Tab>   
          
      <Tab title="📄25001">
          <Accordion title="PI_25001" defaultOpen={false}>
            <DataSchema id="8347882" />
         </Accordion>
      </Tab>
    </Tabs>
  </Step>
</Steps>


