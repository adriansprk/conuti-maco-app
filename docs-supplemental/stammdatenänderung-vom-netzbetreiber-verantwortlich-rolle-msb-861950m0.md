# Stammdatenänderung vom Netzbetreiber (verantwortlich) (Rolle MSB)

# Prozessübersicht

![LW24h mit Abhängigkeiten - SDÄ vom NB (verantw.) (LF_MSB_...).png](https://api.apidog.com/api/v1/projects/816353/resources/352506/image-preview)

<Steps>
  <Step title="Prozessauslöser - eingehende EDI">
    
  <Tabs>
      <Tab title="Übersicht">         
          
        <CardGroup cols={3}>
                 
          <Card title="55627">
              Daten der NeLo
          </Card>
          <Card title="55628">
              Daten der MaLo
          </Card>
            <Card title="55629">
              Daten der TR
          </Card>
            <Card title="55630">
              Daten der SR
          </Card>
            <Card title="55632">
              Daten der MeLo
          </Card>
          <Card title="55173">
              Daten der Lokationsbündel
          </Card>
            
        </CardGroup>
      
      </Tab>   
          
      <Tab title="📄55627">
          <Accordion title="PI_55627" defaultOpen={false}>
                <DataSchema id="5242439" />
          </Accordion> 
      </Tab>
      <Tab title="📄55628">
          <Accordion title="PI_55628" defaultOpen={false}>
               <DataSchema id="5242440" />
          </Accordion> 
      </Tab>  
      <Tab title="📄55629">
          <Accordion title="PI_55629" defaultOpen={false}>
                <DataSchema id="5242441" />
          </Accordion> 
      </Tab>
      <Tab title="📄55630">
          <Accordion title="PI_55630" defaultOpen={false}>
               <DataSchema id="5242442" />
          </Accordion> 
      </Tab>
      <Tab title="📄55632">
          <Accordion title="PI_55632" defaultOpen={false}>
               <DataSchema id="5242443" />
          </Accordion> 
      </Tab>
      <Tab title="📄55173">
          <Accordion title="PI_55173" defaultOpen={false}>
               <DataSchema id="5242400" />
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
         
          <Card title="Erstellen Prozessdaten für Prüfi 55627, 55628, 55629, 55630, 55632, 55173"
                href="https://doc.macoapp.de/prozessdaten-erstellen-14669391e0.md">
              Übergabe der initialen Prozessdaten an das Backend
          </Card>
                    
      </Tab>   
          
      <Tab title="📄55627">
          <Accordion title="PI_55627" defaultOpen={false}>
                <DataSchema id="5242439" />
          </Accordion> 
      </Tab>
      <Tab title="📄55628">
          <Accordion title="PI_55628" defaultOpen={false}>
               <DataSchema id="5242440" />
          </Accordion> 
      </Tab>  
      <Tab title="📄55629">
          <Accordion title="PI_55629" defaultOpen={false}>
                <DataSchema id="5242441" />
          </Accordion> 
      </Tab>
      <Tab title="📄55630">
          <Accordion title="PI_55630" defaultOpen={false}>
               <DataSchema id="5242442" />
          </Accordion> 
      </Tab>
      <Tab title="📄55632">
          <Accordion title="PI_55632" defaultOpen={false}>
               <DataSchema id="5242443" />
          </Accordion> 
      </Tab>
      <Tab title="📄55173">
          <Accordion title="PI_55173" defaultOpen={false}>
               <DataSchema id="5242400" />
          </Accordion> 
      </Tab> 
      </Tabs>
    </Step>   
    
    <Step title="Schnittstelle aktualisieren der Prozessdaten">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Aktualisieren der Prozessdaten"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14669402e0.md">
              Übergabe der erzeugten (55633, 55634, 55635, 55636, 55638, 55177) Rückmeldung an das Backend
          </Card>
      </Tab>   
          
     <Tab title="📄55633">
          <Accordion title="PI_55633" defaultOpen={false}>
               <DataSchema id="5242444" />
          </Accordion> 
      </Tab>
          
      <Tab title="📄55634">
          <Accordion title="PI_55634" defaultOpen={false}>
               <DataSchema id="5242445" />
          </Accordion> 
      </Tab>  
      
      <Tab title="📄55635">
          <Accordion title="PI_55635" defaultOpen={false}>
              <DataSchema id="5242446" />
          </Accordion> 
      </Tab> 
      
      <Tab title="📄55636">
          <Accordion title="PI_55636" defaultOpen={false}>
               <DataSchema id="5242447" />
          </Accordion> 
      </Tab>
      <Tab title="📄55638">
          <Accordion title="PI_55638" defaultOpen={false}>
               <DataSchema id="5242448" />
          </Accordion> 
      </Tab>
        <Tab title="📄55177">
          <Accordion title="PI_55177" defaultOpen={false}>
               <DataSchema id="5242402" />
          </Accordion> 
      </Tab>
    </Tabs>
 </Step>

<Step title="Schnittstelle aktualisieren der Prozessdaten">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Aktualisieren der Prozessdaten"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14669402e0.md">
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



