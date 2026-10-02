# Anfrage zur Stammdatenänderung von Lieferant an Netzbetreiber (verantwortlich) ( Rolle MSB )




![LW24h mit Abhängigkeiten - Anfrage zur Stammdatenänderung von Netzbetreiber an Lieferant (verantwortlich) ( Rolle MSB ).png](https://api.apidog.com/api/v1/projects/816353/resources/373148/image-preview)

<Steps>
  <Step title="Prozessauslöser - eingehende Edifact" defaultOpen={false}>
    <Tabs>
      <Tab title="Übersicht">
 
        <Card title="44113" defaultOpen={false}>          
            <Accordion title="44113 Nicht bila.rel. Änderung vom NB" defaultOpen={false}>

<DataSchema id="13005679" />
          </Accordion>
          </Card>
          
      </Tab> 
  
    </Tabs>

  </Step>
    <Step title="ausgehende Edi" defaultOpen={false}>
    <Tabs>
      <Tab title="Übersicht">
 
        <Card title="44115 Antwort auf Änderung vom NB" defaultOpen={false}>          
            <Accordion title="44115" defaultOpen={false}>

<DataSchema id="13005680" />
          </Accordion>
          </Card>
      </Tab> 
  
    </Tabs>

  </Step>
      
  <Step title="Schnittstellen schreibend">
    <Tabs>
      <Tab title="Übersicht"> 
                    <Card title="Erstellen der Prozessdaten"
                href="https://doc.macoapp.de/prozessdaten-erstellen-14669391e0.md">
              Erstellen der Prozessdaten mit eingehender Nachrichten 44113
          </Card>    
          <Card title="Aktualiseren der Prozessdaten"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14017182e0.md">
              Aktualisieren der Prozessdaten mit ausgehender Nachrichten 44115
          </Card>    
      </Tab>

      
    </Tabs>
  </Step>
  
</Steps>

