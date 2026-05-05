# Geschäftsdatenanfrage von Messstellenbetreiber an Netzbetreiber (Rolle NB)


![LW24h mit Abhängigkeiten - Geschäftsdatenanfrage von Messstellenbetreiber an Netzbetreiber (Rolle NB)(1).png](https://api.apidog.com/api/v1/projects/816353/resources/372998/image-preview)

<Steps>
  <Step title="Prozessauslöser - Trigger Event" defaultOpen={false}>
    <Tabs>
      <Tab title="Übersicht">
 
        <Card title="17126 Anfrage Stammdaten Messlokation (Gas)" defaultOpen={false}>          
            <Accordion title="Event START_GESCHAEFTSDATENANFRAGE" defaultOpen={false}>

<DataSchema id="13290775" />
          </Accordion>
          </Card>
          
      </Tab> 
  
    </Tabs>

  </Step>
    <Step title="ausgehende Edi" defaultOpen={false}>
    <Tabs>
      <Tab title="Übersicht">
 
        <Card title="17126 Anfrage Stammdaten Messlokation (Gas)" defaultOpen={false}>          
            <Accordion title="17126" defaultOpen={false}>

<DataSchema id="13005909" />
          </Accordion>
          </Card>
      </Tab> 
  
    </Tabs>

  </Step>
    <Step title="eingehende Edis" defaultOpen={false}>
    <Tabs>
      <Tab title="Übersicht">
 
        <Card title="19101 Ablehnung der Anfrage Stammdaten" defaultOpen={false}>          
            <Accordion title="19101" defaultOpen={false}>

<DataSchema id="13005872" />
          </Accordion>
          </Card>
            <Card title="44060 Antwort auf die Geschäftsdatenanfrage" defaultOpen={false}>          
            <Accordion title="44060" defaultOpen={false}>

<DataSchema id="13005675" />
          </Accordion>
          </Card>
      </Tab> 
  
    </Tabs>

  </Step>
      
  <Step title="Schnittstellen schreibend">
    <Tabs>
      <Tab title="Übersicht"> 
          <Card title="Aktualiseren der Prozessdaten"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14017182e0.md">
              Aktualisieren der Prozessdaten mit ausgehender Nachrichten 17126 und eingehenden Nachrichten 19101 oder 44060
          </Card>    
      </Tab>

      
    </Tabs>
  </Step>
  
</Steps>

