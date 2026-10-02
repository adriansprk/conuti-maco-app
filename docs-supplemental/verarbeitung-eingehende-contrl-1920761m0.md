# Verarbeitung eingehende Contrl


![LW24h mit Abhängigkeiten - Verarbeitung eingehender Contrl.png](https://api.apidog.com/api/v1/projects/816353/resources/370072/image-preview)

<Steps>
  <Step title="Prozessauslöser - eingehende EDI">
    <Tabs>
      <Tab title="Übersicht">         
          <Card title="77777">
              positive CONTRL
          </Card>
<Card title="88888">
              negative CONTRL
          </Card>
      </Tab> 
          <Tab title="📄77777 pos. CONTRL">
          <Accordion title="PI_77777 - anpassen wenn PI angelegt" defaultOpen={false}>
                  <DataSchema id="5242353" />
Hier bitte Schema anpassen wenn PI angelegt
          </Accordion>
         </Tab>
         <Tab title="📄88888 neg. CONTRL">
          <Accordion title="PI_88888 - anpassen wenn PI angelegt" defaultOpen={false}>
                  <DataSchema id="5242353" />
Hier bitte Schema anpassen wenn PI angelegt
          </Accordion>
         </Tab>
      </Tabs>
  </Step> 
<Step title="ERSTELLEN_PROZESSDATEN">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="ERSTELLEN_PROZESSDATEN LF"
                href="https://doc.macoapp.de/prozessdaten-erstellen-14017183e0.md">
              Übergabe der erzeugten Rückmeldung an das Backend LF- 88888
</Card>
            <Card title="ERSTELLEN_PROZESSDATEN NB"
                href="https://doc.macoapp.de/prozessdaten-erstellen-14666311e0.md">
              Übergabe der erzeugten Rückmeldung an das Backend NB- 88888
          </Card>
<Card title="ERSTELLEN_PROZESSDATEN MSB"
                href="https://doc.macoapp.de/prozessdaten-erstellen-14669391e0.md">
              Übergabe der erzeugten Rückmeldung an das Backend MSB- 88888
          </Card>
      </Tab>   
          
      <Tab title="📄88888 negative CONTRL">
          <Accordion title="PI_88888 - anpassen wenn PI angelegt" defaultOpen={false}>
               <DataSchema id="5242354" />
Hier bitte Schema anpassen wenn PI angelegt
          </Accordion> 
      </Tab>
    </Tabs>
        </Step>
    </Steps>
