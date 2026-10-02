# Geschäftsdatenanfrage LF an NB


![image.png](https://api.apidog.com/api/v1/projects/816353/resources/381648/image-preview)
<Steps>
   <Step title="Prozessauslöser - eingehendes Event" defaultOpen={false}>
      <Tabs>
         <Tab title="Übersicht">
            <Card title="17132 Anfrage Stammdaten (Strom)">
            </Card>
         </Tab>
         <Tab title="📄17132 Anfrage Stammdaten (Strom)">
            <Accordion title="START_GESCHAEFTSDATENANFRAGE" defaultOpen={false}>
                <DataSchema id="17241057" />
            </Accordion>
         </Tab>
      </Tabs>
   </Step>
   <Step title="Schnittstellen schreibend">
      <Tabs>
         <Tab title="Übersicht">
            <Card title="Aktualisieren der Prozessdaten"
               href="https://doc.macoapp.de/prozessdaten-aktualiseren-14017182e0.md">
               Übergabe der ausgehenden Prozessdaten an das Backend
            </Card>
         </Tab>
         <Tab title="📄55035 Antwort auf GDA verb. MaLo">
            <Accordion title="55035 Antwort auf GDA verb. MaLo" defaultOpen={false}>
              
<DataSchema id="13005739" />
            </Accordion>
         </Tab>
         <Tab title="📄55095 Antwort auf GDA erz. MaLo">
            <Accordion title="55095 Antwort auf GDA erz. MaLo" defaultOpen={false}>
         
<DataSchema id="13005758" />
            </Accordion>
         </Tab>
          <Tab title="📄19101 Ablehnung der Anfrage Stammdaten">
            <Accordion title="19101 Ablehnung der Anfrage Stammdaten" defaultOpen={false}>
         

<DataSchema id="13005872" />
            </Accordion>
         </Tab>
      </Tabs>
   </Step>
</Steps>


