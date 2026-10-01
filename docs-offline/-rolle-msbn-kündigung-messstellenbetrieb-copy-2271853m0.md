# ( Rolle MSBN ) Kündigung Messstellenbetrieb  Copy


![LW24h mit Abhängigkeiten - STROM Kündigung Messstellenbetrieb ( Rolle MSBN ).png](https://api.apidog.com/api/v1/projects/816353/resources/380237/image-preview)

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
          <Accordion title="PI_55039" defaultOpen={false}>
                  

<DataSchema id="5562223" />
          </Accordion>
                    
      </Tab>
    </Tabs>
  </Step>

  <Step title="Prozessinitiierung Backend">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Erstellen Prozessdaten für Prüfi 55039"
                href="https://doc.macoapp.de/prozessdaten-erstellen-14666311e0.md">
              Übergabe der initialen Prozessdaten an das Backend
          </Card>
      </Tab>
      <Tab title="📄55039">
          <Accordion title="PI_55039" defaultOpen={false}>

<DataSchema id="5562223" />
          </Accordion>
      </Tab>
    </Tabs>
  </Step>

  <Step title="Prozessausgang - ausgehende EDI">
    <Tabs>
      <Tab title="Übersicht">
        <CardGroup cols={2}>
          <Card title="55039">
              Kündigung Messstellenbetrieb MSBN an MSBA
          </Card>
        </CardGroup>
      </Tab>
      <Tab title="📄55039">
          <Accordion title="PI_55039" defaultOpen={false}>

<DataSchema id="5562223" />
          </Accordion>
      </Tab>
    </Tabs>
  </Step>

  <Step title="Prozessauslöser - eingehende EDI">
    <Tabs>
      <Tab title="Übersicht">
        <CardGroup cols={2}>
          <Card title="55040">
              Antwort der Kündigung MSBA an MSBN (Zustimmung)
          </Card>
          <Card title="55041">
              Antwort der Kündigung MSBA an MSBN (Ablehnung)
          </Card>
        </CardGroup>
      </Tab>
      <Tab title="📄55040">
          <Accordion title="PI_55040" defaultOpen={false}>


<DataSchema id="13005744" />
          </Accordion>
      </Tab>
      <Tab title="📄55041">
          <Accordion title="PI_55041" defaultOpen={false}>

          </Accordion>
      </Tab>
    </Tabs>
  </Step>

<DataSchema id="13005745" />
  <Step title="Schnittstelle aktualisieren der Prozessdaten">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Aktualisieren der Prozessdaten bei Zustimmung"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14666382e0.md">
              Übergabe der empfangenen Rückmeldung an das Backend - 55040 (Zustimmung)
          </Card>
      </Tab>
      <Tab title="📄55040">
          <Accordion title="PI_55040" defaultOpen={false}>

<DataSchema id="13005744" />
          </Accordion>
      </Tab>
    </Tabs>

    <Tabs>
      <Tab title="Übersicht">
          <Card title="Aktualisieren der Prozessdaten bei Ablehnung"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14666382e0.md">
              Übergabe der empfangenen Rückmeldung an das Backend - 55041 (Ablehnung)
          </Card>
      </Tab>
      <Tab title="📄55041">
          <Accordion title="PI_55041" defaultOpen={false}>

<DataSchema id="13005745" />
          </Accordion>
      </Tab>
    </Tabs>
  </Step>

</Steps>
