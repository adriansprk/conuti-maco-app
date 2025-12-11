# Lieferende NB → LF (Rolle NB)

# Prozessübersicht

![LW24h mit Abhängigkeiten - Lieferende NB-_LF (NB).png](https://api.apidog.com/api/v1/projects/816353/resources/352501/image-preview)
<Steps>
  <Step title="Prozessauslöser - Event">
   <Tabs>
      <Tab title="Übersicht">
 
        <Card title="START_LIEFERENDE"
              href="https://doc.macoapp.de/lieferende-von-lieferant-an-netzbetreiber-14992421e0.md">
            Lieferende starten
        </Card>

      </Tab>  
       <Tab title="📄START_LIEFERENDE">
          <Accordion title="START_LIEFERENDE" defaultOpen={false}>
                  <DataSchema id="5854543" />
          </Accordion>
                    
      </Tab>
      <Tab title="📄55007 Abmeldung / Beendigund der Zuordnung ">
          <Accordion title="PI_55007" defaultOpen={false}>
                  <DataSchema id="5242356" />
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
        <Tab title="📄Bestätigung Abmeldung">
            <Accordion title="PI_55008" defaultOpen={false}>
                <DataSchema id="5242357" />
            </Accordion>
        </Tab>
       <Tab title="📄Ablehnung Abmeldung">
            <Accordion title="PI_55009" defaultOpen={false}>
                <DataSchema id="5242358" />
            </Accordion>
       </Tab>
      
    </Tabs>
  </Step>
</Steps>
