# Prozessübersicht


![LW24h mit Abhängigkeiten - MaLo-Ident Netzbetreiber.png](https://api.apidog.com/api/v1/projects/816353/resources/352482/image-preview)


<Steps>
  <Step title="Prozessauslöser - eingehendes Event">
    <Tabs>
      <Tab title="Übersicht"> 
        <Card title="request MaLo-Ident">
          Anfrage MaLo-ID der Marktlokation starten
        </Card>
      </Tab>        
      <Tab title="📄request MaLo-Ident">
          <Accordion title="MaloIdent - request 03001" defaultOpen={false}>
                 <DataSchema id="5818359" />
          </Accordion>
          
      </Tab>
    </Tabs>
  </Step>
    
  <Step title="Ermittlung der MaLo-IDs">
      <Tabs>
      <Tab title="Übersicht">
          <Card title="Ermittlung der MaLo-IDs"
                href="https://doc.macoapp.de/identifizierung-der-malo-14666443e0.md">
                Ermittlung der MaLo-IDs auf Basis der Anfragedaten
          </Card>    
      </Tab>        
      <Tab title="📄Ermittlung MaLo(s)">
          <AccordionGroup>
              <Accordion title="Übergabe Body" defaultOpen={false}>
                  <DataSchema id="5817913" />
              </Accordion>
              <Accordion title="Response Body" defaultOpen={false}>
                  <DataSchema id="5585143" />
              </Accordion>
          </AccordionGroup>
       </Tab>
    </Tabs>
  </Step>
  <Step title="Durchführung EBD">
      <Tabs>
                <Tab title="Übersicht">
          <Card title="Entscheidungsbaumdiagramm E_0594"
                href="https://doc.macoapp.de/ebd-e-0594-894801m0.md">
          </Card>    
      </Tab> 
      </Tabs>
    </Step>
    <Step title="Schnittstelle lesend">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Marktlokationsdaten lesen"
                href="https://doc.macoapp.de/stammdaten-der-identifiz-malo-14666444e0.md">
          </Card>
      </Tab>        
      <Tab title="Marktlokation lesen">
          <Accordion title="MaloIdent Marktlokation" defaultOpen={false}>
                   <DataSchema id="5585144" />
          </Accordion>
         
          
      </Tab>
    </Tabs>
  </Step>
</Steps>

