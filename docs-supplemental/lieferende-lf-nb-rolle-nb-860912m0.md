# Lieferende LF -> NB (Rolle NB)

# Prozessübersicht

![LW24h mit Abhängigkeiten - Lieferende LF-_NB (NB).png](https://api.apidog.com/api/v1/projects/816353/resources/352500/image-preview)
 
<Steps>
  <Step title="Prozessauslöser - eingehende EDI">
    <Tabs>
      <Tab title="Übersicht">         
          <Card title="55004">
              Abmeldung
          </Card>
      </Tab> 
          <Tab title="📄55004 Abmeldung">
          <Accordion title="PI_55004" defaultOpen={false}>
                  <DataSchema id="5242353" />
          </Accordion>
         </Tab>
      </Tabs>
  </Step> 
        
  <Step title="Schnittstellen lesend für APERAK">
      <Tabs>
      <Tab title="Übersicht">         
          
        <CardGroup cols={2}>
          <Card title="Marktlokation lesen"
                href="https://doc.macoapp.de/marktlokation-lesen-14017020e0.md">
              Lesen einer MaLo mittels LokationsId zu einem bestimmten Zeitpunkt
          </Card>
          <Card title="Tranche lesen" 
                href="https://doc.macoapp.de/tranche-lesen-14017030e0.md">
              Lesen einer Tranche mittels LokationsId zu einem bestimmten Zeitpunkt
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
          
    </Tabs>
  </Step>
    
  <Step title="Prozessinitiierung Backend">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Erstellen Prozessdaten für Prüfi 55004"
                href="https://doc.macoapp.de/prozessdaten-erstellen-14666311e0.md">
              Übergabe der initialen Prozessdaten an das Backend
          </Card>
      </Tab>        
      <Tab title="55004 Abmeldung">
          <Accordion title="PI_55004" defaultOpen={false}>
                  <DataSchema id="5242353" />    
          </Accordion>
       </Tab> 
    </Tabs>
  </Step>  
    
  <Step title="Schnittstellen lesend für EBD-Prüfungen">
    <Tabs>
      <Tab title="Übersicht">
          <CardGroup cols={3}>
                  <Card title="Netznutzungsvertrag lesen" 
                href="https://doc.macoapp.de/netznutzungsvertrag-lesen-14017027e0.md">
              Leses des Netznutzungsvertrags einer Lokation zu einem bestimmten Zeitpunkt
          </Card>
         </CardGroup>
      </Tab>        
        <Tab title="📄Netznutzungsvertrag lesen">
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
              Übergabe der erzeugten Rückmeldung an das Backend - 55005, 55006
          </Card>
      </Tab>   
          
      <Tab title="📄55005 Bestätigung Abmeldung">
          <Accordion title="PI_55005" defaultOpen={false}>
               <DataSchema id="5242354" />
          </Accordion> 
      </Tab>
        
      <Tab title="📄55006 Ablehnung Abmeldung">
          <Accordion title="PI_55006" defaultOpen={false}>
               <DataSchema id="5242355" />
          </Accordion> 
      </Tab>
      
    </Tabs>
 </Step>
</Steps>
