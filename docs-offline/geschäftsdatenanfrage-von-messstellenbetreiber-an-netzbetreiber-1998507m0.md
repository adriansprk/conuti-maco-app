# Geschäftsdatenanfrage von Messstellenbetreiber an Netzbetreiber


![LW24h mit Abhängigkeiten - Geschäftsdatenanfrage von Messstellenbetreiber an Netzbetreiber ( Rolle MSB ).png](https://api.apidog.com/api/v1/projects/816353/resources/372993/image-preview)

<Steps>
  <Step title="Prozessauslöser - eingehende Event" defaultOpen={false}>
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
    <Step title="ausgehende Edis" defaultOpen={false}>
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
     <Step title="Schnittstellen lesend">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Messlokation"
                href="https://doc.macoapp.de/messlokation-lesen-14017024e0.md">
              Lesen der Daten der Messlokation
          </Card>    
          <Card title="Zähler"
                href="https://doc.macoapp.de/z%C3%A4hler-lesen-14017031e0.md">
              Lesen der Daten des Zählers
          </Card>    
                    <Card title="Messstellenbetriebsvertrag"
                href="https://doc.macoapp.de/messstellenbetriebsvertrag-lesen-14017025e0.md">
              Lesen der Daten des MSB-Vertrags
          </Card>  
      </Tab>

      
    </Tabs>
  </Step>
  
  <Step title="Schnittstellen schreibend">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Erstellen der Prozessdaten"
                href="https://doc.macoapp.de/prozessdaten-erstellen-14017183e0.md">
              Übergabe der eingehende Edi 17126
          </Card>    
          <Card title="Aktualiseren der Prozessdaten"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14017182e0.md">
              Aktualisieren der Prozessdaten mit ausgehenden Nachrichten 19101 oder 44060.
          </Card>    
      </Tab>

      
    </Tabs>
  </Step>
  
</Steps>

