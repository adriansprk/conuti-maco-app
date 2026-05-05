# Anmeldung NN

# Prozessübersicht
![LW24h mit Abhängigkeiten - Lieferbeginn (GAS) LFN.png](https://api.apidog.com/api/v1/projects/816353/resources/370549/image-preview)

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
          <Accordion title="PI_44001" defaultOpen={false}>           
<DataSchema id="8347890" />
          </Accordion>
                    
      </Tab>
        
    </Tabs>

 
  </Step>
  <Step title="Schnittstellen schreibend">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Aktualisieren der Prozessdaten"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14017182e0.md">
              Übergabe ausgehende Nachricht aus Event, Übergabe der Informationsmeldung über bestehende Zuordnung, sowie pos. und neg. Rückmeldung vom Netzbetreiber.
          </Card> 
      </Tab>
        <Tab title="📄44001 Anmeldung NN">
            <Accordion title="PI_44001" defaultOpen={false}>
                <DataSchema id="8347890" />
            </Accordion>
                     
      </Tab>
        <Tab title="📄44036 Info best. Zuordnung">
            <Accordion title="PI_44036" defaultOpen={false}>
                <DataSchema id="8347915" />
            </Accordion>
                     
        </Tab>
      <Tab title="📄44003 neg. Rückmeldung"> 
          <Accordion title="PI_44003" defaultOpen={false}>
                 <DataSchema id="8347892" />
          </Accordion>
        
        </Tab>
      <Tab title="📄44002 pos. Rückmeldung">
          <Accordion title="PI_44002" defaultOpen={false}>
                 <DataSchema id="8347891" />
          </Accordion>
      </Tab>
    </Tabs>
  </Step>
</Steps>



