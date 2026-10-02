# Beginn der Ersatz-/Grundversorgung (Rolle LF)

# Prozessübersicht
 
![LW24h mit Abhängigkeiten - Beginn der Ersatz-_Grundversorgung (LF).png](https://api.apidog.com/api/v1/projects/816353/resources/352470/image-preview)

<Steps>
  <Step title="Prozessauslöser - eingehende EDI">
    <Tabs>
      <Tab title="Übersicht">         
          <Card title="55013">
              Anmeldung EoG
          </Card>
      </Tab> 
          <Tab title="📄55013">
          <Accordion title="PI_55013" defaultOpen={false}>
                  <DataSchema id="5242362" />
          </Accordion>
         </Tab>
      </Tabs>
  </Step> 

  <Step title="Schnittstellen lesend für APERAK">
      <Tabs>
      <Tab title="Übersicht">         
          
        <Card title="Marktlokation lesen"
                href="https://doc.macoapp.de/marktlokation-lesen-14017020e0.md">
              Lesen einer MaLo mittels LokationsId zu einem bestimmten Zeitpunkt
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
          <Card title="Erstellen Prozessdaten für Prüfi 55013"
                href="https://doc.macoapp.de/prozessdaten-erstellen-14017183e0.md">
              Übergabe der initialen Prozessdaten an das Backend
          </Card>
      </Tab>        
      <Tab title="55013 - Anmeldung EoG">
          <Accordion title="PI_55013" defaultOpen={false}>
                  <DataSchema id="5242362" />    
          </Accordion>
       </Tab> 
    </Tabs>
  </Step> 

<Step title="Schnittstellen lesend für EBD-Prüfungen">
    <Tabs>
      <Tab title="Übersicht">
         
          <Card title="Netznutzungsvertrag lesen" 
                href="https://doc.macoapp.de/netznutzungsvertrag-lesen-14017027e0.md">
              Leses des Netznutzungsvertrags einer Lokation zu einem bestimmten Zeitpunkt
          </Card>
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
          
      <Tab title="📄55015 Ablehnung EOG Anmeldung">
          <Accordion title="PI_55015" defaultOpen={false}>
               <DataSchema id="5242364" />
          </Accordion> 
      </Tab>
        
      <Tab title="📄55014 Bestätigung EOG Anmeldung">
          <Accordion title="PI_55014" defaultOpen={false}>
               <DataSchema id="5242363" />
          </Accordion> 
      </Tab>
      
    </Tabs>
 </Step>    
</Steps>





