# Verarbeitung eingehende Aperak


![LW24h mit Abhängigkeiten - Verarbeitung eingehender Aperak.png](https://api.apidog.com/api/v1/projects/816353/resources/370074/image-preview)

<Steps>
  <Step title="Prozessauslöser - eingehende EDI">
    <Tabs>
      <Tab title="Übersicht">         
          <Card title="66666">
              positive APERAK
          </Card>
<Card title="99999">
              negative APERAK
          </Card>
      </Tab> 
          <Tab title="📄66666 pos. APERAK">
          <Accordion title="PI_66666" defaultOpen={false}>
                  <DataSchema id="8348234" />
positive Aperak
          </Accordion>
         </Tab>
         <Tab title="📄99999 neg. APERAK">
          <Accordion title="PI_99999" defaultOpen={false}>
                  <DataSchema id="8348235" />
negative APERAK
          </Accordion>
         </Tab>
      </Tabs>
  </Step> 
<Step title="ERSTELLEN_PROZESSDATEN">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="ERSTELLEN_PROZESSDATEN LF"
                href="https://doc.macoapp.de/prozessdaten-erstellen-14017183e0.md">
              Übergabe der erzeugten Rückmeldung an das Backend LF- 99999
</Card>
            <Card title="ERSTELLEN_PROZESSDATEN NB"
                href="https://doc.macoapp.de/prozessdaten-erstellen-14666311e0.md">
              Übergabe der erzeugten Rückmeldung an das Backend NB- 99999
          </Card>
<Card title="ERSTELLEN_PROZESSDATEN MSB"
                href="https://doc.macoapp.de/prozessdaten-erstellen-14669391e0.md">
              Übergabe der erzeugten Rückmeldung an das Backend MSB- 99999
          </Card>
      </Tab>   
   
      <Tab title="📄99999 negative APERAK">
          <Accordion title="PI_99999" defaultOpen={false}>
               <DataSchema id="8348235" />
übergabe negative APERAK
          </Accordion> 
      </Tab>
    </Tabs>
        </Step>
    </Steps>
