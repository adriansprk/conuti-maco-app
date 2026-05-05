# Übermittlung der Berechnungsformel (Rolle MSB)


![LW24h mit Abhängigkeiten - Übermittlung der Berechnungsformel ( Rolle MSB ).png](https://api.apidog.com/api/v1/projects/816353/resources/373410/image-preview)
<Steps>
   <Step title="Prozessauslöser - eingehende Edifact" defaultOpen={false}>
      <Tabs>
         <Tab title="Übersicht">
            <Card title="25001" defaultOpen={false}>
               <Accordion title="25001 Berechnungsformel" defaultOpen={false}>
                  <DataSchema id="8347882" />
               </Accordion>
            </Card>
         </Tab>
      </Tabs>
   </Step>
   <Step title="ausgehende Edi" defaultOpen={false}>
      <Tabs>
         <Tab title="Übersicht">
            <Card title="25010 Antwort auf Berechnungsformel" defaultOpen={false}>
               <Accordion title="25010" defaultOpen={false}>
                  <DataSchema id="8347889" />
               </Accordion>
            </Card>
         </Tab>
      </Tabs>
   </Step>
   <Step title="Schnittstellen schreibend">
      <Tabs>
         <Tab title="Übersicht">
            <Card title="Erstellen der Prozessdaten"
               href="https://doc.macoapp.de/prozessdaten-erstellen-14669391e0.md">
               Erstellen der Prozessdaten mit eingehender Nachrichten 25001
            </Card>
            <Card title="Aktualiseren der Prozessdaten"
               href="https://doc.macoapp.de/prozessdaten-aktualiseren-14017182e0.md">
               Aktualisieren der Prozessdaten mit ausgehender Nachrichten 25010
            </Card>
         </Tab>
      </Tabs>
   </Step>
</Steps>

