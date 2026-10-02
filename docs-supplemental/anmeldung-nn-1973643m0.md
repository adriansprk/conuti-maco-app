# Anmeldung NN

# Prozessübersicht

![LW24h mit Abhängigkeiten - Lieferbeginn NB (GAS).png](https://api.apidog.com/api/v1/projects/816353/resources/372565/image-preview)

<Steps>
    
<Step title="Prozessauslöser - eingehende EDI">
    <Tabs>
        <Tab title="Übersicht">         
          
        <CardGroup cols={2}>
          <Card title="44001">
              Anmeldung
          </Card>
          
              
        </CardGroup>
      
     </Tab>
        
     <Tab title="📄44001">
          <Accordion title="PI_44001" defaultOpen={false}>
                 <DataSchema id="13005650" />
          </Accordion> 
        </Tab>

    </Tabs>    
  </Step>   

 <Step title="Prozessinitiierung Backend">
    
      <Tabs>
      <Tab title="Übersicht">         
         
          <Card title="Erstellen Prozessdaten für Prüfi 44001"
                href="https://doc.macoapp.de/prozessdaten-erstellen-14666311e0.md">
              Übergabe der initialen Prozessdaten an das Backend
          </Card>
                    
      </Tab>   
          
      <Tab title="📄44001">
          <Accordion title="PI_44001" defaultOpen={false}>
               <DataSchema id="13005650" />
          </Accordion> 
      </Tab>
      
    </Tabs>
  </Step>   
          
   <Step title="Schnittstellen lesen für Lokation identifizieren">
   <Tabs>
      <Tab title="Übersicht">         
          
        <CardGroup cols={2}>
          <Card title="Marktlokation lesen"
                href="https://doc.macoapp.de/marktlokation-lesen-14017020e0.md">
              Lesen einer MaLo mittels LokationsId oder Zähler oder Adresse zu einem Zeitpunkt
          </Card>
         
            
        </CardGroup>
      
      </Tab>   
          
      <Tab title="📄Marktlokation">
          <Accordion title="Marktlokation" defaultOpen={false}>
                <DataSchema id="5241973" />
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
          
            <Card title="Messlokation lesen" 
                href="https://doc.macoapp.de/messlokation-lesen-14017024e0.md">
              Lesen einer Messlokation mittels LokationsId zu einem bestimmten Zeitpunkt
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
      
      <Tab title="📄Messlokation">
          <Accordion title="Messlokation" defaultOpen={false}>
                <DataSchema id="5241975" />
          </Accordion> 
      </Tab> 
      
      <Tab title="📄Netznutzungsvertrag">
          <Accordion title="Netznutzungsvertrag" defaultOpen={false}>
                <DataSchema id="5242152" />
          </Accordion> 
      </Tab>
    </Tabs> 
  </Step>


 <Step title="Schnittstellen lesend für Prozessdaten">
   <Tabs>
      <Tab title="Übersicht">         
<Card title="Zuordnungsermaechtigung prüfen" 
                href="https://doc.macoapp.de/zuordnungsem%C3%A4chtigung-lesen-14665842e0.md">
              Lesen einer Zuordnungsermaechtigung mittels LokationsId, Absender und Bilanzkreis zu einem bestimmten Zeitpunkt
            </Card>
</Tab> 
      
      <Tab title="📄Zuordnungsermächtigung">
          <Accordion title="Zuordnungsermächtigung" defaultOpen={false}>
                <DataSchema id="5584997" />
          </Accordion> 
      </Tab>
    </Tabs> 
  </Step>

<Step title="Schnittstelle aktualisieren der Prozessdaten">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Aktualisieren der Prozessdaten"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14666382e0.md">
              Übergabe der erzeugten Rückmeldung an das Backend - 44036
          </Card>
      </Tab>   
          
      <Tab title="📄44036">
          <Accordion title="PI_44036" defaultOpen={false}>
              <DataSchema id="13005672" />
          </Accordion> 
      </Tab>
      
    </Tabs>
 </Step>
    
    <Step title="Schnittstelle aktualisieren der Prozessdaten">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Aktualisieren der Prozessdaten"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14666382e0.md">
              Übergabe der erzeugten Rückmeldung an das Backend - 44003
          </Card>
      </Tab>   
          
      <Tab title="📄44003">
          <Accordion title="PI_44003" defaultOpen={false}>
              <DataSchema id="13005652" />
          </Accordion> 
      </Tab>
     </Tabs>
 </Step>

 <Step title="Schnittstellen lesend für Versand 44002">
   <Tabs>
      <Tab title="Übersicht">         
          
        <CardGroup cols={3}>
          <Card title="Zähler lesen"
                href="https://doc.macoapp.de/z%C3%A4hler-lesen-14017031e0.md">
              Lesen eines Zählers mittels LokationsId zu einem bestimmten Zeitpunkt
          </Card>
          <Card title="Marktlokation lesen"
                href="https://doc.macoapp.de/marktlokation-lesen-14017020e0.md">
              Lesen einer Marktlokation mittels LokationsId zu einem bestimmten Zeitpunkt
          </Card>

          <Card title="Energieliefervertrag lesen"
                href="https://doc.macoapp.de/energieliefervertrag-lesen-14017014e0.md">
              Lesen eines Energieliefervertrages mittels LokationsId zu einem bestimmten Zeitpunkt
          </Card>

          <Card title="Bilanzierung lesen"
                href="https://doc.macoapp.de/bilanzierung-lesen-14017013e0.md">
              Lesen einer Bilanzierung mittels LokationsId zu einem bestimmten Zeitpunkt
          </Card>
          
            <Card title="Messlokation lesen" 
                href="https://doc.macoapp.de/messlokation-lesen-14017024e0.md">
              Lesen einer Messlokation mittels LokationsId zu einem bestimmten Zeitpunkt
            </Card>
         
            <Card title="Netznutzungsvertrag lesen" 
                href="https://doc.macoapp.de/netznutzungsvertrag-lesen-14017027e0.md">
              Lesen eines Netznutzungsvertrages mittels LokationsId zu einem bestimmten Zeitpunkt
            </Card>
            
        </CardGroup>
      
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
      
      <Tab title="📄Energieliefervertrag">
          <Accordion title="Energieliefervertrag" defaultOpen={false}>
                <DataSchema id="5241988" />
          </Accordion> 
      </Tab>
       
      <Tab title="📄Bilanzierung">
          <Accordion title="Bilanzierung" defaultOpen={false}>
                <DataSchema id="5241965" />
          </Accordion> 
      </Tab>
      
      <Tab title="📄Messlokation">
          <Accordion title="Messlokation" defaultOpen={false}>
                <DataSchema id="5241975" />
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
              Übergabe der erzeugten Rückmeldung an das Backend - 44002
          </Card>
      </Tab>   
          
      <Tab title="📄44002">
          <Accordion title="PI_44002" defaultOpen={false}>
             <DataSchema id="13005651" />
          </Accordion> 
      </Tab>
            
    </Tabs>
 </Step>

</Steps>



