# Lieferende LF -> NB (Rolle LF)

# Prozessübersicht
 
![LW24h mit Abhängigkeiten - Lieferende LF-_NB (LF).png](https://api.apidog.com/api/v1/projects/816353/resources/352467/image-preview)

 
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
          <Accordion title="PI_55004" defaultOpen={false}>
                  <DataSchema id="5242353" />
          </Accordion>
                    
      </Tab>
    </Tabs>
  </Step>
  <Step title="Schnittstellen schreibend">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Aktualisieren der Prozessdaten"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14017182e0.md">
              Übergabe der Informationsmeldung über bestehende Zuordnung, sowie pos. (55005)und neg. (55006)Rückmeldung vom Netzbetreiber.
          </Card>    
      </Tab>
              <Tab title="📄55004 Abmeldung">
          <Accordion title="PI_55004" defaultOpen={false}>
                  <DataSchema id="5242353" />
          </Accordion>
                    
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


