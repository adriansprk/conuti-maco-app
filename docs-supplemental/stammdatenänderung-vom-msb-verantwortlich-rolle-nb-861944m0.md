# Stammdatenänderung vom MSB (verantwortlich) (Rolle NB)

# Prozessübersicht
![LW24h mit Abhängigkeiten - SDÄ vom MSB (verantw.) (LF_NB_...).png](https://api.apidog.com/api/v1/projects/816353/resources/352505/image-preview)

<Steps>
  <Step title="Prozessauslöser - eingehende EDI">
    
  <Tabs>
      <Tab title="Übersicht">         
          
        <CardGroup cols={3}>
                 
          <Card title="55639">
              Daten der NeLo
          </Card>
          <Card title="55640">
              Daten der MaLo
          </Card>
            <Card title="55642">
              Daten der Tranche
          </Card>
            <Card title="55641">
              Daten der SR
          </Card>
            <Card title="55643">
              Daten der MeLo
          </Card>
            
        </CardGroup>
      
      </Tab>   
          
      <Tab title="📄55639">
          <Accordion title="PI_55639" defaultOpen={false}>
                <DataSchema id="5242449" />
          </Accordion> 
      </Tab>
      <Tab title="📄55640">
          <Accordion title="PI_55640" defaultOpen={false}>
               <DataSchema id="5242450" />
          </Accordion> 
      </Tab>  
      <Tab title="📄55642">
          <Accordion title="PI_55642" defaultOpen={false}>
                <DataSchema id="5242452" />
          </Accordion> 
      </Tab>
      <Tab title="📄55641">
          <Accordion title="PI_55641" defaultOpen={false}>
               <DataSchema id="5242451" />
          </Accordion> 
      </Tab>
      <Tab title="📄55643">
          <Accordion title="PI_55643" defaultOpen={false}>
               <DataSchema id="5242453" />
          </Accordion> 
      </Tab>
      <Tab title="📄55619">
          <Accordion title="PI_55619" defaultOpen={false}>
                <DataSchema id="5242431" />
          </Accordion> 
      </Tab> 
     </Tabs>
  </Step>   
  
  <Step title="Schnittstellen lesen für APERAK">
   <Tabs>
      <Tab title="Übersicht">         
          
        <CardGroup cols={3}>
          <Card title="Marktlokation lesen"
                href="https://doc.macoapp.de/marktlokation-lesen-14017020e0.md">
              Lesen einer MaLo mittels LokationsId zu einem Zeitpunkt
          </Card>
          <Card title="Tranche lesen" 
                href="https://doc.macoapp.de/tranche-lesen-14017030e0.md">
              Lesen einer Tranche mittels LokationsId zu einem bestimmten Zeitpunkt
          </Card>
            <Card title="Netzlokation lesen" 
                href="https://doc.macoapp.de/netzlokation-lesen-14017026e0.md">
              Lesen einer NeLo mittels LokationsId zu einem bestimmten Stichtag
          </Card>
            <Card title="Technische Ressource lesen" 
                href="https://doc.macoapp.de/technische-ressource-lesen-14017029e0.md">
              Lesen einer technischen Ressource mittels LokationsId zu einem bestimmten Zeitpunkt
          </Card>
            <Card title="Steuerbare Ressource lesen" 
                href="https://doc.macoapp.de/steuerbare-ressource-lesen-14017028e0.md">
              Lesen einer steuerbaren Ressource mittels LokationsId zu einem bestimmten Zeitpunkt
          </Card>
            <Card title="Messlokation lesen" 
                href="https://doc.macoapp.de/messlokation-lesen-14017024e0.md">
              Lesen einer MeLo mittels LokationsId zu einem bestimmten Zeitpunkt
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
          
      <Tab title="📄Tranche">
          <Accordion title="Tranche" defaultOpen={false}>
                <DataSchema id="5241987" />
          </Accordion> 
      </Tab>  
      
      <Tab title="📄Netzlokation">
          <Accordion title="Netzlokation" defaultOpen={false}>
                <DataSchema id="5241976" />
          </Accordion> 
      </Tab> 
      
      <Tab title="📄Technische Ressource">
          <Accordion title="Technische Ressource" defaultOpen={false}>
                <DataSchema id="5241986" />
          </Accordion> 
      </Tab> 
      
      <Tab title="📄Steuerbare Ressource">
          <Accordion title="Steuerbare Ressource" defaultOpen={false}>
                <DataSchema id="5241984" />
          </Accordion> 
      </Tab> 
      
      <Tab title="📄Messlokation">
          <Accordion title="Messlokation" defaultOpen={false}>
               <DataSchema id="5241975" />
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
         
          <Card title="Erstellen Prozessdaten für Prüfi 55645, 55647, 55646, 55648"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14669402e0.md">
              Übergabe der initialen Prozessdaten an das Backend
          </Card>
                    
      </Tab>   
          
      <Tab title="📄55645">
          <Accordion title="PI_55645" defaultOpen={false}>
               <DataSchema id="5242455" />
          </Accordion> 
      </Tab>
          
      <Tab title="📄55647">
          <Accordion title="PI_55647" defaultOpen={false}>
               <DataSchema id="5242457" />
          </Accordion> 
      </Tab>  
      
      <Tab title="📄55646">
          <Accordion title="PI_55646" defaultOpen={false}>
               <DataSchema id="5242456" />
          </Accordion> 
      </Tab> 
      
      <Tab title="📄55648">
          <Accordion title="PI_55648" defaultOpen={false}>
               <DataSchema id="5242458" />
          </Accordion> 
      </Tab> 
        
    </Tabs>
  </Step>
 
   <Step title="Durchführung EBD">
      <Tabs>
          <Tab title="Übersicht">
              <Card title="Entscheidungsbaumdiagramm E_0583"
                    href="https://doc.macoapp.de/894682m0.md"> 
              </Card>
          </Tab>
      </Tabs>
    </Step>   
    
    <Step title="Schnittstelle aktualisieren der Prozessdaten">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Aktualisieren der Prozessdaten"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14669402e0.md">
              Übergabe der erzeugten (55645, 55647, 55646, 55648) Rückmeldung an das Backend
          </Card>
      </Tab>   
          
     <Tab title="📄55645">
          <Accordion title="PI_55645" defaultOpen={false}>
               <DataSchema id="5242455" />
          </Accordion> 
      </Tab>
          
      <Tab title="📄55647">
          <Accordion title="PI_55647" defaultOpen={false}>
               <DataSchema id="5242457" />
          </Accordion> 
      </Tab>  
      
      <Tab title="📄55646">
          <Accordion title="PI_55646" defaultOpen={false}>
               <DataSchema id="5242456" />
          </Accordion> 
      </Tab> 
      
      <Tab title="📄55648">
          <Accordion title="PI_55648" defaultOpen={false}>
               <DataSchema id="5242458" />
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



