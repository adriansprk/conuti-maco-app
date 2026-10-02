# Abrechnungsdaten Netznutzungsabrechnung (Rolle LF)

![LW24h mit Abhängigkeiten - Abr.Da. NNA (LF_MSB).png](https://api.apidog.com/api/v1/projects/816353/resources/352458/image-preview)

<Steps>
  <Step title="Prozessauslöser - eingehende EDI">
    <Tabs>
      <Tab title="Übersicht"> 
        <Card title="55218">
          Abrechnungsdaten Netznutzungsabrechnung
        </Card>
      </Tab>        
      <Tab title="55218">
          <Accordion title="PI_55218" defaultOpen={false}>
                 <DataSchema id="5242405" />
          </Accordion>
         
          
      </Tab>
    </Tabs>
  </Step>
    
  <Step title="Schnittstelle lesend für APERAK">
      <Tabs>
      <Tab title="Übersicht">
          <CardGroup cols="2">
              <Card title="Marktlokation lesen"
                    href="https://doc.macoapp.de/marktlokation-lesen-14017020e0.md">
                    Lesen einer MaLo mittels LokationsId zu einem bestimmten Zeitpunkt
              </Card>
              <Card title="Netznutzungsvertrag lesen"
                    href="https://doc.macoapp.de/netznutzungsvertrag-lesen-14017027e0.md">
                  Lesen des Netzunutzungsvertrages einer Lokation zu einem bestimmten Zeitpunkt
              </Card>
          </CardGroup>
      </Tab>        
      <Tab title="📄Marktlokation ">
              <Accordion title="Marktlokation" defaultOpen={false}>
                  <DataSchema id="5241973" />      
              </Accordion>
       </Tab>
        <Tab title="📄Netznutzungsvertrag lesen">
            <Accordion title="Netznutzungsvertrag" defaultOpen={false}>
                <DataSchema id="5241988" />
            </Accordion>
        </Tab>
    </Tabs>
  </Step>
  <Step title="Prozessinitiierung Backend">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Erstellen Prozessdaten für Prüfi 55218"
                href="https://doc.macoapp.de/prozessdaten-erstellen-14017183e0.md">
              Übergabe der initialen Porzessdaten an das Backend
          </Card>
      </Tab>        
      <Tab title="55218 - Abrechnungsdaten Netznutzungsabrechnung">
          <Accordion title="PI_55218" defaultOpen={false}>
                <DataSchema id="5242405" />
          </Accordion>
        
      </Tab> 
    </Tabs>
  </Step>  
  <Step title="Durchführung EBD">
      <Tabs>
          <Tab title="Übersicht">
              <Card title="Entscheidungsbaumdiagramm E_0610"
                    href="https://doc.macoapp.de/ebd-e-0610-861884m0.md">
              </Card>
          </Tab>
      </Tabs>
    </Step>
    <Step title="Schnittstelle aktualisieren der Prozessdaten">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Aktualisieren der Prozessdaten"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14017182e0.md">
              Übergabe der erzeugten (55220) Rückmeldung an das Backend
          </Card>
      </Tab>        
      <Tab title="55220 - Bestellung einer Änderung von Abrechnungsdaten">
          <Accordion title="PI_55220" defaultOpen={false}>
                 <DataSchema id="5242406" />
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
      <Tab title="21047 - Bearbeitungsstand zur Rückmeldung">
          <Accordion title="PI_21047" defaultOpen={false}>
                 <DataSchema id="5718596" />
          </Accordion>
          
      </Tab>
    </Tabs>
  </Step>
</Steps>
