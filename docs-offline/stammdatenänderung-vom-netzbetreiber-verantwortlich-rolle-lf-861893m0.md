# Stammdatenänderung vom Netzbetreiber (verantwortlich) (Rolle LF)

<Frame caption="Stammdatenänderung vom Netzbetreiber">
  ![](https://api.apidog.com/api/v1/projects/816353/resources/352461/image-preview)
</Frame>

<Steps>
  <Step title="Prozessauslöser - eingehende EDI">
    
  <Tabs>
      <Tab title="Übersicht">         
          
        <CardGroup cols={3}>
          <Card title="55615">
              Daten der NeLo an LF
          </Card>
          <Card title="55616">
              Daten der MaLo an LF
          </Card>
            <Card title="55619">
              Daten der Tranche an LF
          </Card>
            <Card title="55617">
              Daten der TR an LF
          </Card>
            <Card title="55618">
              Daten der SR an LF
          </Card>
            <Card title="55620">
              Daten der MeLo an LF
          </Card>
            <Card title="55225">
              Blindabr. Daten der NeLo an LF
          </Card>
            <Card title="55175">
              Lokationsbündelstruktur an LF
          </Card>
        </CardGroup>
      
      </Tab>   
          
      <Tab title="📄55615">
          <Accordion title="PI_55615" defaultOpen={false}>
                 <DataSchema id="8348045" />
          </Accordion> 
      </Tab>
          
      <Tab title="📄55616">
          <Accordion title="PI_55616" defaultOpen={false}>
                <DataSchema id="8348046" />
          </Accordion> 
      </Tab>  
      
      <Tab title="📄55619">
          <Accordion title="PI_55619" defaultOpen={false}>
                <DataSchema id="8348049" />
          </Accordion> 
      </Tab> 
      
      <Tab title="📄55617">
          <Accordion title="PI_55617" defaultOpen={false}>
                  <DataSchema id="8348047" />      
          </Accordion> 
      </Tab> 
      
      <Tab title="📄55618">
          <Accordion title="PI_55618" defaultOpen={false}>
                <DataSchema id="8348048" />
          </Accordion> 
      </Tab> 
      
      <Tab title="📄55620">
          <Accordion title="PI_55620" defaultOpen={false}>
                <DataSchema id="8348050" />
          </Accordion> 
      </Tab> 
      
      <Tab title="📄55225">
          <Accordion title="PI_55225" defaultOpen={false}>
                  <DataSchema id="5241987" />      
          </Accordion> 
      </Tab> 
      
      <Tab title="📄55175">
          <Accordion title="PI_55175" defaultOpen={false}>
                <DataSchema id="8348019" />
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
         
          <Card title="Erstellen Prozessdaten für Prüfi 55621, 55622, 55625, 55623, 55624, 55626, 55627, 55180"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14017182e0.md">
              Übergabe der initialen Prozessdaten an das Backend
          </Card>
                    
      </Tab>   
          
      <Tab title="📄55621">
          <Accordion title="PI_55621" defaultOpen={false}>
                <DataSchema id="8348051" />
          </Accordion> 
      </Tab>
          
      <Tab title="📄55622">
          <Accordion title="PI_55622" defaultOpen={false}>
                <DataSchema id="8348052" />
          </Accordion> 
      </Tab>  
      
      <Tab title="📄55625">
          <Accordion title="PI_55625" defaultOpen={false}>
                <DataSchema id="8348055" />
          </Accordion> 
      </Tab> 
      
      <Tab title="📄55623">
          <Accordion title="PI_55623" defaultOpen={false}>
                <DataSchema id="8348053" />
          </Accordion> 
      </Tab> 
      
      <Tab title="📄55624">
          <Accordion title="PI_55624" defaultOpen={false}>
                <DataSchema id="8348054" />
          </Accordion> 
      </Tab> 
      
      <Tab title="📄55626">
          <Accordion title="PI_55626" defaultOpen={false}>
                <DataSchema id="8348056" />
          </Accordion> 
      </Tab> 
      
      <Tab title="📄55627">
          <Accordion title="PI_55627" defaultOpen={false}>
                <DataSchema id="8348057" />
          </Accordion> 
      </Tab> 
      
      <Tab title="📄55180">
          <Accordion title="PI_55180" defaultOpen={false}>
                <DataSchema id="5242403" />
          </Accordion> 
      </Tab> 
          
    </Tabs>
  </Step>
 <Step title="Durchführung EBD">
      <Tabs>
          <Tab title="Übersicht">
              <Card title="Entscheidungsbaumdiagramm E_0408"
                    href="https://doc.macoapp.de/861894m0.md">
              </Card>
          </Tab>
      </Tabs>
    </Step>   
    
    <Step title="Schnittstelle aktualisieren der Prozessdaten">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Aktualisieren der Prozessdaten"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14666382e0.md">
              Übergabe der erzeugten (55621, 55622, 55625, 55623, 55624, 55626, 55627, 55180) Rückmeldung an das Backend
          </Card>
      </Tab>   
          
      <Tab title="📄55621">
          <Accordion title="PI_55621" defaultOpen={false}>
                <DataSchema id="8348051" />
          </Accordion> 
      </Tab>
          
      <Tab title="📄55622">
          <Accordion title="PI_55622" defaultOpen={false}>
                <DataSchema id="8348052" />
          </Accordion> 
      </Tab>  
      
      <Tab title="📄55625">
          <Accordion title="PI_55625" defaultOpen={false}>
                <DataSchema id="8348055" />
          </Accordion> 
      </Tab> 
      
      <Tab title="📄55623">
          <Accordion title="PI_55623" defaultOpen={false}>
                <DataSchema id="8348053" />
          </Accordion> 
      </Tab> 
      
      <Tab title="📄55624">
          <Accordion title="PI_55624" defaultOpen={false}>
                <DataSchema id="8348054" />
          </Accordion> 
      </Tab> 
      
      <Tab title="📄55626">
          <Accordion title="PI_55626" defaultOpen={false}>
                <DataSchema id="8348056" />
          </Accordion> 
      </Tab> 
      
      <Tab title="📄55627">
          <Accordion title="PI_55627" defaultOpen={false}>
                <DataSchema id="8348057" />
          </Accordion> 
      </Tab> 
      
      <Tab title="📄55180">
          <Accordion title="PI_55180" defaultOpen={false}>
                <DataSchema id="5242403" />
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







