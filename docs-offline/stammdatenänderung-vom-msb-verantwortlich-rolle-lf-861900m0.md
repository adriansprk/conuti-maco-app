# Stammdatenänderung vom MSB (verantwortlich) (Rolle LF)

# Prozessübersicht

![LW24h mit Abhängigkeiten - SDÄ vom MSB (verantw.) (LF_NB_...).png](https://api.apidog.com/api/v1/projects/816353/resources/352504/image-preview)

<Steps>
  <Step title="Prozessauslöser - eingehende EDI">
    
  <Tabs>
      <Tab title="Übersicht">         
          
        <CardGroup cols={3}>
          <Card title="55649">
              Änderung Daten der NeLo an LF
          </Card>
          <Card title="55650">
              Änderung Daten der MaLo an LF
          </Card>
            <Card title="55652">
              Änderung Daten der Tranche an LF
          </Card>
            <Card title="55651">
              Änderung Daten der SR an LF
          </Card>
            <Card title="55653">
              Änderung Daten der MeLo an LF
          </Card>
        </CardGroup>
      
      </Tab>   
          
      <Tab title="📄55649">
          <Accordion title="PI_55649" defaultOpen={false}>
              
<DataSchema id="5242459" />
             
          </Accordion> 
      </Tab>
          
      <Tab title="📄55650">
          <Accordion title="PI_55650" defaultOpen={false}>
              
<DataSchema id="5242460" />
          </Accordion> 
      </Tab>  
      
      <Tab title="📄55652">
          <Accordion title="PI_55652" defaultOpen={false}>
             
<DataSchema id="5242462" />
          </Accordion> 
      </Tab> 
      
      <Tab title="📄55651">
          <Accordion title="PI_55651" defaultOpen={false}>
               
<DataSchema id="5242461" />
          </Accordion> 
      </Tab> 
      
      <Tab title="📄55653">
          <Accordion title="PI_55653" defaultOpen={false}>
              
<DataSchema id="11223118" />
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
         
          <Card title="Erstellen Prozessdaten für Prüfi 55654, 55655, 55657, 55656, 55658"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14017182e0.md">
              Übergabe der initialen Prozessdaten an das Backend
          </Card>
                    
      </Tab>   
          
      <Tab title="📄55654">
          <Accordion title="PI_55654" defaultOpen={false}>
              <DataSchema id="5242463" />
          </Accordion> 
      </Tab>
          

      <Tab title="📄55655">
          <Accordion title="PI_55655" defaultOpen={false}>
               
<DataSchema id="5242464" />
          </Accordion> 
      </Tab>  
      
      <Tab title="📄55657">
          <Accordion title="PI_55657" defaultOpen={false}>
               
<DataSchema id="5242466" />
          </Accordion> 
      </Tab> 
      
      <Tab title="📄55656">
          <Accordion title="PI_55656" defaultOpen={false}>
               
<DataSchema id="5242465" />
          </Accordion> 
      </Tab> 
      
      <Tab title="📄55658">
          <Accordion title="PI_55658" defaultOpen={false}>
                
<DataSchema id="11256232" />
          </Accordion> 
      </Tab> 
         
    </Tabs>
  </Step>
 <Step title="Durchführung EBD">
      <Tabs>
          <Tab title="Übersicht">
              <Card title="Entscheidungsbaumdiagramm E_0412"
                    href="https://doc.macoapp.de/ebd-e-0412-894711m0.md">
              </Card>
          </Tab>
      </Tabs>
    </Step>   
    
    <Step title="Schnittstelle aktualisieren der Prozessdaten">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Aktualisieren der Prozessdaten"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14669402e0.md">
              Übergabe der erzeugten (55654, 55655, 55657, 55656, 55658) Rückmeldung an das Backend
          </Card>
      </Tab>   
          
      <Tab title="📄55654">
          <Accordion title="PI_55654" defaultOpen={false}>
           
<DataSchema id="5242463" />
          </Accordion> 
      </Tab>
          
      <Tab title="📄55655">
          <Accordion title="PI_55655" defaultOpen={false}>
                 <DataSchema id="5242464" />
          </Accordion> 
      </Tab>  
      
![image.png](https://api.apidog.com/api/v1/projects/816353/resources/363738/image-preview)
      <Tab title="📄55657">
          <Accordion title="PI_55657" defaultOpen={false}>
                <DataSchema id="5242466" />
          </Accordion> 
      </Tab> 
      
      <Tab title="📄55656">
          <Accordion title="PI_55656" defaultOpen={false}>
                <DataSchema id="5242465" />
          </Accordion> 
      </Tab> 
      
      <Tab title="📄55658">
          <Accordion title="PI_55658" defaultOpen={false}>
            
<DataSchema id="11256232" />
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
