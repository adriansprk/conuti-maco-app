# Prozessübersicht

# Prozessübersicht
![LW24h mit Abhängigkeiten - Lieferbeginn Lieferseite.png](https://api.apidog.com/api/v1/projects/816353/resources/352454/image-preview)


<Steps>
  <Step title="Prozessauslöser - Event" defaultOpen={false}>
    <Tabs>
      <Tab title="Übersicht">
 
        <Card title="START_LIEFERBEGINN"
              href="https://doc.macoapp.de/lieferbeginn-14992210e0.md">
            Lieferbeginn starten
        </Card>

      </Tab>        
      <Tab title="📄START_LIEFERBEGINN">
          <Accordion title="PI_55001" defaultOpen={false}>
                 <DataSchema id="5242350" />   
          </Accordion>
                    
      </Tab>
        
    </Tabs>

 
  </Step>
  <Step title="Schnittstellen schreibend">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Aktualisieren der Prozessdaten"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14017182e0.md">
              Übergabe der Informationsmeldung über bestehende Zuordnung, sowie pos. und neg. Rückmeldung vom Netzbetreiber.
          </Card>    
      </Tab>
        <Tab title="📄55036 Info best. Zuordnung">
            <Accordion title="PI_55036" defaultOpen={false}>
                <DataSchema id="5242372" />
            </Accordion>
                     
        </Tab>
      <Tab title="📄55003 neg. Rückmeldung"> 
          <Accordion title="PI_55003" defaultOpen={false}>
                 <DataSchema id="5242352" />
          </Accordion>
        
        </Tab>
      <Tab title="📄55002 pos. Rückmeldung">
          <Accordion title="PI_55002" defaultOpen={false}>
                 <DataSchema id="5242351" />
          </Accordion>
      </Tab>
    </Tabs>
  </Step>
</Steps>
