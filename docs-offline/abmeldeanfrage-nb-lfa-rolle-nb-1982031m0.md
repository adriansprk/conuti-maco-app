# Abmeldeanfrage NB -> LFA (Rolle NB)

# Prozessübersicht

![LW24h mit Abhängigkeiten - Abmeldeanfrage GAS (NB).png](https://api.apidog.com/api/v1/projects/816353/resources/372781/image-preview)

<Steps>
  <Step title="Prozessauslöser - Trigger 44001" defaultOpen={false}>
    <Tabs>
      <Tab title="Übersicht">
 
        <Card title="44010"
             >
            Anfrage zur Beendigung der Zuordnung
        </Card>

      </Tab>        
     
        <Tab title="📄44010 Abmeldungsanfrage">
          <Accordion title="PI_44010" defaultOpen={false}>
                    <DataSchema id="13005659" />
          </Accordion>
          
      </Tab>
    </Tabs>

  </Step>
 
  <Step title="Schnittstelle aktualisieren der Prozessdaten">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Aktualisieren der Prozessdaten"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14017182e0.md">
              Übergabe der erzeugten neg. (44012) oder pos. (44011) Rückmeldung an das Backend
          </Card>
      </Tab>        
      <Tab title="44012 - Ablehnung Abmeldeanfrage">
          <Accordion title="PI_44012" defaultOpen={false}>
                   <DataSchema id="13005661" />
          </Accordion>
      </Tab>
      <Tab title="44011 - Bestätigung Abmeldeanfrage">
          <Accordion title="PI_44011" defaultOpen={false}>
                 <DataSchema id="13005660" />
          </Accordion>
        
      </Tab>    
      <Tab title="44037 - Informationsmeldung zur Beendigung
der Zuordnung">
          <Accordion title="PI_44037" defaultOpen={false}>
                 <DataSchema id="13005673" />
          </Accordion>
        
      </Tab>      
    </Tabs>
  </Step>  
</Steps>



