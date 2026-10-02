# Lieferende NB -> LF (Rolle LF)

# Prozessübersicht

![LW24h mit Abhängigkeiten - Lieferende NB-_LF (LF).png](https://api.apidog.com/api/v1/projects/816353/resources/352469/image-preview)


<Steps>
  <Step title="Prozessauslöser - eingehende EDI">
    <Tabs>
      <Tab title="Übersicht">         
          <Card title="55007">
              Abmeldung / Beendigung der Zuordnung vom NB
          </Card>
      </Tab> 
          <Tab title="📄55007">
          <Accordion title="PI_55007" defaultOpen={false}>
                  <DataSchema id="5242356" />
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
          <Card title="Erstellen Prozessdaten für Prüfi 55007"
                href="https://doc.macoapp.de/prozessdaten-erstellen-14017183e0.md">
              Übergabe der initialen Prozessdaten an das Backend
          </Card>
      </Tab>        
      <Tab title="55007 - Abmeldung / Beendigung der Zuordnung vom NB">
          <Accordion title="PI_55007" defaultOpen={false}>
                  <DataSchema id="5242356" />    
          </Accordion>
       </Tab> 
    </Tabs>
  </Step>  
    
  <Step title="Schnittstellen lesend für EBD-Prüfungen">
    <Tabs>
      <Tab title="Übersicht">
          <CardGroup cols={3}>
          <Card title="Energieliefervertrag lesen" 
                href="https://doc.macoapp.de/energieliefervertrag-lesen-14017014e0.md">
              Lesen des Energieliefervertrages einer Lokation zu einem bestimmten Zeitpunkt
          </Card>
          <Card title="Bilanzierung lesen" 
                href="https://doc.macoapp.de/bilanzierung-lesen-14017013e0.md">
              Lesen einer Bilanzierung mittels LokationsId zu einem bestimmten Zeitpunkt
          </Card>
          <Card title="Netznutzungsvertrag lesen" 
                href="https://doc.macoapp.de/netznutzungsvertrag-lesen-14017027e0.md">
              Leses des Netznutzungsvertrags einer Lokation zu einem bestimmten Zeitpunkt
          </Card>
         </CardGroup>
      </Tab>        

      <Tab title="📄Energieliefervertrag lesen">
            <Accordion title="Vertrag" defaultOpen={false}>
                 <DataSchema id="5241988" />    
            </Accordion>
      </Tab>
        <Tab title="📄Bilanzierung lesen">
            <Accordion title="Bilanzierung" defaultOpen={false}>
                  <DataSchema id="5241965" />
            </Accordion>
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
              Übergabe der erzeugten Rückmeldung an das Backend - 55009, 55008
          </Card>
      </Tab>   
          
      <Tab title="📄55009 Ablehnung Abmeldung">
          <Accordion title="PI_55009" defaultOpen={false}>
               <DataSchema id="5242358" />
          </Accordion> 
      </Tab>
        
      <Tab title="📄55008 Bestätigung Abmeldung">
          <Accordion title="PI_55008" defaultOpen={false}>
               <DataSchema id="5242357" />
          </Accordion> 
      </Tab>
      
    </Tabs>
 </Step>
</Steps>



