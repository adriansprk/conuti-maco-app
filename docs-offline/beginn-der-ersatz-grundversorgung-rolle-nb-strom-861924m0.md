# Beginn der Ersatz-/Grundversorgung (Rolle NB) Strom

# Prozessübersicht
  
![LW24h mit Abhängigkeiten - Beginn der Ersatz-_Grundversorgung (NB).png](https://api.apidog.com/api/v1/projects/816353/resources/352502/image-preview)

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
      <Tab title="📄55013 Anmeldung/ Zuordnung EOG">
          <Accordion title="PI_55013" defaultOpen={false}>
                  <DataSchema id="5242362" />
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




