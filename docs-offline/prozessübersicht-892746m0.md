# Prozessübersicht


![LW24h mit Abhängigkeiten - MaLo-Ident Lieferant.png](https://api.apidog.com/api/v1/projects/816353/resources/352689/image-preview)

<Steps>
  <Step title="Prozessauslöser - Event" defaultOpen={false}>
    <Tabs>
      <Tab title="Übersicht">
 
        <Card title="START_MALOIDENT"
              href="https://doc.macoapp.de/15144286e0.md">
          Anfrage MaLo-ID der Marktlokation starten
        </Card>

      </Tab>        
      <Tab title="📄START_MALOIDENT">
         <Accordion title="[LF] START_MALOIDENT" defaultOpen={false}>
                <DataSchema id="5242230" />
         </Accordion> 
        
     </Tab>
    </Tabs>

  </Step>
  <Step title="Schnittstellen schreibend">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Aktualisieren der Prozessdaten"
                href="https://doc.macoapp.de/15144289e0.md">
                Übergabe der pos. sowie neg. Rückmeldung vom Netzbetreiber.
          </Card>    
      </Tab>        
      <Tab title="📄neg. Rückmeldung">
          <Accordion title="MaloIdent - negative Antwort 03003" defaultOpen={false}>
                <DataSchema id="5585136" />
          </Accordion> 
          
      </Tab>
      <Tab title="📄pos. Rückmeldung">
          <Accordion title="MaloIdent - positive Antwort 03002" defaultOpen={false}>
               <DataSchema id="5585135" />
          </Accordion> 
          
      </Tab>
    </Tabs>
  </Step>
</Steps>
