# Anfrage zur Stammdatenänderung von Lieferant an Messstellenbetreiber (verantwortlich) ( Rolle MSB )


![LW24h mit Abhängigkeiten - Anfrage zur Stammdatenänderung von Lieferant an Messstellenbetreiber (verantwortlich) ( Rolle MSB )(1).png](https://api.apidog.com/api/v1/projects/816353/resources/373016/image-preview)

<Steps>
  <Step title="Prozessauslöser - eingehende Edifact" defaultOpen={false}>
    <Tabs>
      <Tab title="Übersicht">
 
        <Card title="44147" defaultOpen={false}>          
            <Accordion title="44147 Anfrage an MSB mit Abhängigkeiten" defaultOpen={false}>


<DataSchema id="13005696" />
          </Accordion>
          </Card>
                  <Card title="44165" defaultOpen={false}>          
            <Accordion title="44165 Nicht bila. rel Anfrage an MSB ohne Abhängigkeiten" defaultOpen={false}>


<DataSchema id="13005710" />
          </Accordion>
          </Card>
          
      </Tab> 
  
    </Tabs>

  </Step>
    <Step title="ausgehende Edi" defaultOpen={false}>
    <Tabs>
      <Tab title="Übersicht">
 
        <Card title="44149 Antwort auf Anfrage" defaultOpen={false}>          
            <Accordion title="44149" defaultOpen={false}>

<DataSchema id="13005698" />
          </Accordion>
          </Card>
                  <Card title="44167 Antwort auf Anfrage" defaultOpen={false}>          
            <Accordion title="44167" defaultOpen={false}>

<DataSchema id="13005712" />
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
              Erstellen der Prozessdaten mit eingehenden Nachrichten 44147 und 44165
          </Card>    
          <Card title="Aktualiseren der Prozessdaten"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14017182e0.md">
              Aktualisieren der Prozessdaten mit ausgehenden Nachrichten 44149 und 44167
          </Card>    
      </Tab>

      
    </Tabs>
  </Step>
  
</Steps>

