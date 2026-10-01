# Abrechnungsdaten Bilanzkreisabrechnung (Rolle LF)

![LW24h mit Abhängigkeiten - Abr.Da. BKA (LF_MSB)).png](https://api.apidog.com/api/v1/projects/816353/resources/352459/image-preview)

<Steps>
  <Step title="Prozessauslöser - eingehende EDI">
    <Tabs>
      <Tab title="Übersicht"> 
        <Card title="55126">
          Abrechnungsdaten Bilanzkreisabrechnung
        </Card>
      </Tab>        
      <Tab title="55126">    
          <Accordion title="PI_55126" defaultOpen={false}>
                  <DataSchema id="5562241" />
          </Accordion>

      </Tab>
    </Tabs>
  </Step>
    
  <Step title="Schnittstelle lesend für APERAK">
      <Tabs>
      <Tab title="Übersicht">
              <Card title="Marktlokation lesen"
                    href="https://doc.macoapp.de/marktlokation-lesen-14017020e0.md">
                    Lesen einer MaLo mittels LokationsId zu einem bestimmten Zeitpunkt
              </Card>
      </Tab>        
      <Tab title="📄Marktlokation ">
              <Accordion title="Marktlokation" defaultOpen={false}>
                  <DataSchema id="5241973" />
              </Accordion>
       </Tab>
    </Tabs>
  </Step>
  <Step title="Prozessinitiierung Backend">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Erstellen Prozessdaten für Prüfi 55126"
                href="https://doc.macoapp.de/prozessdaten-erstellen-14017183e0.md">
              Übergabe der initialen Prozessdaten an das Backend
          </Card>
      </Tab>        
      <Tab title="55126 - Abrechnungsdaten Bilanzkreisabrechnung">
          <Accordion title="PI_55126" defaultOpen={false}>
                  <DataSchema id="5562241" />
          </Accordion>
        </Tab> 
    </Tabs>
  </Step>  
  <Step title="Durchführung EBD">
      <Tabs>
          <Tab title="Übersicht">
              <Card title="Entscheidungsbaumdiagramm E_0611"
                    href="https://doc.macoapp.de/ebd-e-0624-860873m0.md">
              </Card>
          </Tab>
      </Tabs>
    </Step>
    <Step title="Schnittstelle aktualisieren der Prozessdaten">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Aktualisieren der Prozessdaten"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14017182e0.md">
              Übergabe der erzeugten (55156) Rückmeldung an das Backend
          </Card>
      </Tab>        
      <Tab title="55156">
          <Accordion title="PI_55156" defaultOpen={false}>
           
<DataSchema id="5242396" />
          </Accordion>
      </Tab>
    </Tabs>
  </Step>
        <Step title="Schnittstelle aktualisieren der Prozessdaten">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Aktualisieren der Prozessdaten"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14017182e0.md">
              Übergabe der empfangenen Statusmeldung (21047) an das Backend
          </Card>
      </Tab>        
      <Tab title="21047">
          <Accordion title="PI_21047" defaultOpen={false}>
              <DataSchema id="5718596" />
          </Accordion>
          
      </Tab>
    </Tabs>
  </Step>
</Steps>

