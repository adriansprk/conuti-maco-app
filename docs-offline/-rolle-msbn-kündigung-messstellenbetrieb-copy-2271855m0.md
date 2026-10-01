# ( Rolle MSBN ) Kündigung Messstellenbetrieb  Copy


![LW24h mit Abhängigkeiten - GAS Kündigung Messstellenbetrieb ( Rolle MSBN ).png](https://api.apidog.com/api/v1/projects/816353/resources/380236/image-preview)

<Steps>

  <Step title="Prozessauslöser - Start Event">
    <Tabs>
      <Tab title="Übersicht">
        <CardGroup cols={2}>
          <Card title="START_KUENDIGUNG_MSB">
              Interner Prozessstart der Kündigung Messstellenbetrieb (MSBN)
          </Card>
        </CardGroup>
      </Tab>
 <Tab title="📄START_KUENDIGUNG_MSB">
          <Accordion title="PI_44039" defaultOpen={false}>
                  
<DataSchema id="8347918" />
          </Accordion>
                    
      </Tab>
    </Tabs>
  </Step>

  <Step title="Prozessinitiierung Backend">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Erstellen Prozessdaten für Prüfi 44039"
                href="https://doc.macoapp.de/prozessdaten-erstellen-14666311e0.md">
              Übergabe der initialen Prozessdaten an das Backend
          </Card>
      </Tab>
      <Tab title="📄44039">
          <Accordion title="PI_44039" defaultOpen={false}>

<DataSchema id="8347918" />
          </Accordion>
      </Tab>
    </Tabs>
  </Step>

  <Step title="Prozessausgang - ausgehende EDI">
    <Tabs>
      <Tab title="Übersicht">
        <CardGroup cols={2}>
          <Card title="44039">
              Kündigung Messstellenbetrieb MSBN an MSBA
          </Card>
        </CardGroup>
      </Tab>
      <Tab title="📄44039">
          <Accordion title="PI_44039" defaultOpen={false}>

<DataSchema id="8347918" />
          </Accordion>
      </Tab>
    </Tabs>
  </Step>

  <Step title="Prozessauslöser - eingehende EDI">
    <Tabs>
      <Tab title="Übersicht">
        <CardGroup cols={2}>
          <Card title="44040">
              Bestätigung der Kündigung MSBA an MSBN (Zustimmung)
          </Card>
          <Card title="44041">
              Ablehnung der Kündigung MSBA an MSBN
          </Card>
        </CardGroup>
      </Tab>
      <Tab title="📄44040">
          <Accordion title="PI_44040" defaultOpen={false}>


<DataSchema id="8347919" />
          </Accordion>
      </Tab>
      <Tab title="📄44041">
          <Accordion title="PI_44041" defaultOpen={false}>


<DataSchema id="8347920" />
          </Accordion>
      </Tab>
    </Tabs>
  </Step>

  <Step title="Schnittstelle aktualisieren der Prozessdaten">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Aktualisieren der Prozessdaten bei Zustimmung"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14666382e0.md">
              Übergabe der empfangenen Rückmeldung an das Backend - 44040 (Zustimmung)
          </Card>
      </Tab>
      <Tab title="📄44040">
          <Accordion title="PI_44040" defaultOpen={false}>

<DataSchema id="8347919" />
          </Accordion>
      </Tab>
    </Tabs>

    <Tabs>
      <Tab title="Übersicht">
          <Card title="Aktualisieren der Prozessdaten bei Ablehnung"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14666382e0.md">
              Übergabe der empfangenen Rückmeldung an das Backend - 44041 (Ablehnung)
          </Card>
      </Tab>
      <Tab title="📄44041">
          <Accordion title="PI_44041" defaultOpen={false}>

<DataSchema id="8347920" />
          </Accordion>
      </Tab>
    </Tabs>
  </Step>

</Steps>
