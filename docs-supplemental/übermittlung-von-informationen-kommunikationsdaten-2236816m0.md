# Übermittlung von Informationen - Kommunikationsdaten

<Frame caption="Prozess 37000–37002">
  ![]
</Frame>
<Steps>
  <Step title="Prozessauslöser - ausgehende EDI">

    <Tabs>
      <Tab title="Übersicht">

          
        <CardGroup cols={4}>
             <Card title="Event">
            Ausgehendes Event START_PARTIN
          </Card>
          <Card title="37000 – LF">
            Ausgehende Nachricht des Lieferanten (LF)
          </Card>
          <Card title="37001 – NB">
            Ausgehende Nachricht des Netzbetreibers (NB)
          </Card>
          <Card title="37002 – MSB">
            Ausgehende Nachricht des Messstellenbetreibers (MSB)
          </Card>
        </CardGroup>

          
      </Tab>
        <Tab title="Event">
        <Accordion title="Event START_PARTIN" defaultOpen={false}>
          

<DataSchema id="16135766" />
        </Accordion>
      </Tab>
      <Tab title="37000 – LF">
        <Accordion title="PI_37000" defaultOpen={false}>
          
<DataSchema id="8348114" />
        </Accordion>
      </Tab>
      <Tab title="37001 – NB">
        <Accordion title="PI_37001" defaultOpen={false}>
          
<DataSchema id="8348115" />
        </Accordion>
      </Tab>
      <Tab title="37002 – MSB">
        <Accordion title="PI_37002" defaultOpen={false}>
         
<DataSchema id="8348116" />
        </Accordion>
      </Tab>
    </Tabs>

  </Step>



 

 

  <Step title="Eingehende Nachrichten (potenziell)">
    <Tabs>
      <Tab title="Übersicht">

        <CardGroup cols={3}>
          <Card title="37000">Potenzielle eingehende Nachricht</Card>
          <Card title="37001">Potenzielle eingehende Nachricht</Card>
          <Card title="37002">Potenzielle eingehende Nachricht</Card>
          <Card title="37003">Potenzielle eingehende Nachricht</Card>
          <Card title="37004">Potenzielle eingehende Nachricht</Card>
          <Card title="37005">Potenzielle eingehende Nachricht</Card>
          <Card title="37006">Potenzielle eingehende Nachricht</Card>
        </CardGroup>

      </Tab>
      <Tab title="37000">
        <Accordion title="PI_37000" defaultOpen={false}>
    <DataSchema id="8348114" />
        </Accordion>
      </Tab>
      <Tab title="37001">
        <Accordion title="PI_37001" defaultOpen={false}>
                 
<DataSchema id="8348115" />
        </Accordion>
      </Tab>
      <Tab title="37002">
        <Accordion title="PI_37002" defaultOpen={false}>
        <DataSchema id="8348116" />
        </Accordion>
      </Tab>
      <Tab title="37003">
        <Accordion title="PI_37003" defaultOpen={false}>
          <DataSchema id="" />
        </Accordion>
      </Tab>
      <Tab title="37004">
        <Accordion title="PI_37004" defaultOpen={false}>
            <DataSchema id="" />
        </Accordion>
      </Tab>
      <Tab title="37005">
        <Accordion title="PI_37005" defaultOpen={false}>
          <DataSchema id="" />
        </Accordion>
      </Tab>
      <Tab title="37006">
        <Accordion title="PI_37006" defaultOpen={false}>
          <DataSchema id="" />
        </Accordion>
      </Tab>
    </Tabs>
  </Step>

  <Step title="Schnittstelle aktualisieren der Prozessdaten">
    <Tabs>
      <Tab title="Übersicht">
        <Card title="Aktualisieren der Prozessdaten"
              href="https://doc.macoapp.de/prozessdaten-aktualiseren-14017182e0.md">
          Übergabe der verarbeiteten eingehenden Nachricht an das Backend
        </Card>
      </Tab>
      <Tab title="37000">
        <Accordion title="PI_37000" defaultOpen={false}>
         
<DataSchema id="8348114" />
        </Accordion>
      </Tab>
      <Tab title="37001">
        <Accordion title="PI_37001" defaultOpen={false}>

<DataSchema id="8348115" />
        </Accordion>
      </Tab>
      <Tab title="37002">
        <Accordion title="PI_37002" defaultOpen={false}>
     
<DataSchema id="8348116" />
        </Accordion>
      </Tab>
      <Tab title="37003">
        <Accordion title="PI_37003" defaultOpen={false}>
         
        </Accordion>
      </Tab>
      <Tab title="37004">
        <Accordion title="PI_37004" defaultOpen={false}>
          <DataSchema id="" />
        </Accordion>
      </Tab>
      <Tab title="37005">
        <Accordion title="PI_37005" defaultOpen={false}>
          <DataSchema id="" />
        </Accordion>
      </Tab>
      <Tab title="37006">
        <Accordion title="PI_37006" defaultOpen={false}>
          <DataSchema id="" />
        </Accordion>
      </Tab>
    </Tabs>
  </Step>

<DataSchema id="8348114" />
</Steps>

