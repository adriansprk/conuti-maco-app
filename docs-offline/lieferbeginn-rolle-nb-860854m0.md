# Lieferbeginn (Rolle NB)

# Prozessübersicht

![LW24h mit Abhängigkeiten - Lieferbeginn Netzbetreiber.png](https://api.apidog.com/api/v1/projects/816353/resources/352484/image-preview)


<Steps>
    
<Step title="Prozessauslöser - eingehende EDI">
    <Tabs>
        <Tab title="Übersicht">         
          
        <CardGroup cols={2}>
          <Card title="55001">
              Anmeldung verbr. MaLo
          </Card>
          
              
        </CardGroup>
      
     </Tab>
        
     <Tab title="📄55001">
          <Accordion title="PI_55001" defaultOpen={false}>
                 <DataSchema id="5242350" />
          </Accordion> 
      </Tab>
      
    </Tabs>    
  </Step>   
          
   <Step title="Schnittstellen lesen für APERAK">
   <Tabs>
      <Tab title="Übersicht">         
          
        <CardGroup cols={2}>
          <Card title="Marktlokation lesen"
                href="https://doc.macoapp.de/marktlokation-lesen-14017020e0.md">
              Lesen einer MaLo mittels LokationsId zu einem Zeitpunkt
          </Card>
          
            <Card title="Lokationsbündel lesen" 
                href="https://doc.macoapp.de/lokationsb%C3%BCndel-lesen-14017019e0.md">
              Lesen eines Lokationsbündels mittels LokationsId zu einem bestimmten Zeitpunkt
          </Card>
            
        </CardGroup>
      
      </Tab>   
          
      <Tab title="📄Marktlokation">
          <Accordion title="Marktlokation" defaultOpen={false}>
                <DataSchema id="5241973" />
          </Accordion> 
      </Tab>
      
      <Tab title="📄Lokationsbündel">
          <Accordion title="Lokationsbündel" defaultOpen={false}>
                <DataSchema id="5241972" />
          </Accordion> 
     </Tab> 
      
    </Tabs> 
  </Step> 
          
 <Step title="Prozessinitiierung Backend">
    
      <Tabs>
      <Tab title="Übersicht">         
         
          <Card title="Erstellen Prozessdaten für Prüfi 55003"
                href="https://doc.macoapp.de/prozessdaten-erstellen-14666311e0.md">
              Übergabe der initialen Prozessdaten an das Backend
          </Card>
                    
      </Tab>   
          
      <Tab title="📄55003">
          <Accordion title="PI_55003" defaultOpen={false}>
                <DataSchema id="5242352" />
          </Accordion> 
      </Tab>
      
    </Tabs>
  </Step>   
 
    <Step title="Schnittstellen lesend für EBD-Prüfungen">
   <Tabs>
      <Tab title="Übersicht">         
          
        <CardGroup cols={3}>
          <Card title="Bilanzierung lesen"
                href="https://doc.macoapp.de/bilanzierung-lesen-14017013e0.md">
              Lesen einer Bilanzierung mittels LokationsId zu einem bestimmten Zeitpunkt
          </Card>
          
            <Card title="Energieliefervertrag lesen" 
                href="https://doc.macoapp.de/energieliefervertrag-lesen-14017014e0.md">
              Lesen eines Energieliefervertrages mittels LokationsId zu einem bestimmten Zeitpunkt
            </Card>
         
            <Card title="Netznutzungsvertrag lesen" 
                href="https://doc.macoapp.de/netznutzungsvertrag-lesen-14017027e0.md">
              Lesen eines Netznutzungsvertrages mittels LokationsId zu einem bestimmten Zeitpunkt
            </Card>
            
        </CardGroup>
      
      </Tab>   
          
      <Tab title="📄Bilanzierung">
          <Accordion title="Bilanzierung" defaultOpen={false}>
                <DataSchema id="5241965" />
          </Accordion> 
      </Tab>
      
      <Tab title="📄Energieliefervertrag">
          <Accordion title="Energieliefervertrag" defaultOpen={false}>
                <DataSchema id="5241988" />
          </Accordion> 
      </Tab> 
      
      <Tab title="📄Netznutzungsvertrag">
          <Accordion title="Netznutzungsvertrag" defaultOpen={false}>
                <DataSchema id="5242152" />
          </Accordion> 
      </Tab>
    </Tabs> 
  </Step>
<Step title="Schnittstelle aktualisieren der Prozessdaten">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Aktualisieren der Prozessdaten"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14666382e0.md">
              Übergabe der erzeugten Rückmeldung an das Backend - 55036
          </Card>
      </Tab>   
          
      <Tab title="📄55036">
          <Accordion title="PI_55036" defaultOpen={false}>
              <DataSchema id="5242372" />
          </Accordion> 
      </Tab>
      
    </Tabs>
 </Step>
    
    <Step title="Schnittstelle aktualisieren der Prozessdaten">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Aktualisieren der Prozessdaten"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14666382e0.md">
              Übergabe der erzeugten Rückmeldung an das Backend - 55003, 55080
          </Card>
      </Tab>   
          
      <Tab title="📄55003">
          <Accordion title="PI_55003" defaultOpen={false}>
              <DataSchema id="5242352" />
          </Accordion> 
      </Tab>
     </Tabs>
 </Step>
    
    <Step title="Schnittstelle aktualisieren der Prozessdaten">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Aktualisieren der Prozessdaten"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14666382e0.md">
              Übergabe der erzeugten Rückmeldung an das Backend - 55002, 55078
          </Card>
      </Tab>   
          
      <Tab title="📄55002">
          <Accordion title="PI_55002" defaultOpen={false}>
              <DataSchema id="5242351" />
          </Accordion> 
      </Tab>
            
    </Tabs>
 </Step>

</Steps>



