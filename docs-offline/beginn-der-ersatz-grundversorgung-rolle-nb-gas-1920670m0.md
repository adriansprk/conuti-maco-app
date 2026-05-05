# Beginn der Ersatz-/Grundversorgung (Rolle NB) Gas

# Prozessübersicht
  

![LW24h mit Abhängigkeiten - Beginn der Ersatz-_Grundversorgung Gas ( Rolle NB NVB ).png](https://api.apidog.com/api/v1/projects/816353/resources/370067/image-preview)

<Steps>
  <Step title="Prozessauslöser - Event">
   <Tabs>
      <Tab title="Übersicht">
 
        <Card title="START_EOG"
              href="https://doc.macoapp.de/ersatz-grundversorgung-14984068e0.md">
            Ersatz-/Grundversorgung


        </Card>

      </Tab>        
      <Tab title="📄START_EOG">
          <Accordion title="START_EOG" defaultOpen={false}>
                 <DataSchema id="5637367" />
          </Accordion>
                    
      </Tab>
      <Tab title="📄44013 Anmeldung/ Zuordnung EOG">
          <Accordion title="PI_44013" defaultOpen={false}>
                  <DataSchema id="5242362" />
dieses Schema anpassen wenn Prüfi da 
          </Accordion>
                    
      </Tab>
    </Tabs>
  </Step>
  <Step title="Schnittstellen schreibend">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Aktualisieren der Prozessdaten"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14666382e0.md">
              Übergabe der Informationsmeldung über bestehende Zuordnung, sowie pos. und neg. Rückmeldung vom Netzbetreiber.
          </Card>    
      </Tab>
        <Tab title="📄44015 Ablehnung EOG Anmeldung">
            <Accordion title="PI_44015" defaultOpen={false}>
                <DataSchema id="8347904" />
            </Accordion>
        </Tab>
       <Tab title="📄44014 Bestätigung EOG Anmeldung">
            <Accordion title="PI_44014" defaultOpen={false}>
                <DataSchema id="8347903" />
            </Accordion>
       </Tab>
     

  <Tab title="AKTUALISIEREN_PROZESSDATEN">
    

<Card title="AKTUALISIEREN_PROZESSDATEN" 
      href="https://doc.macoapp.de/21698135e0.md">
  
    
</Card>


  </Tab>
 

    </Tabs>
  </Step>
</Steps>




