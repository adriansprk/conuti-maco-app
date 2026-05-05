# GAS Anforderung und Bereitstellung von Messwerten (Rolle LF)


![LW24h mit Abhängigkeiten - GAS Anforderung und Bereitstellung von Messwerten (Rolle LF).png](https://api.apidog.com/api/v1/projects/816353/resources/375629/image-preview)
<Steps>
   <Step title="Prozessauslöser - eingehende Edifact" defaultOpen={false}>
      <Tabs>
         <Tab title="Übersicht">
            <Card title="13002" defaultOpen={false}>
               <Accordion title="13002 Zählerstand (Gas)" defaultOpen={false}>
                  <DataSchema id="13005918" />
               </Accordion>
            </Card>
            <Card title="13008" defaultOpen={false}>
               <Accordion title="13008 Lastgang (Gas)" defaultOpen={false}>
                  <DataSchema id="13005921" />
               </Accordion>
            </Card>
            <Card title="13009" defaultOpen={false}>
               <Accordion title="13009 Energiemenge (Gas)" defaultOpen={false}>
                  <DataSchema id="13005922" />
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
               Erstellen der Prozessdaten mit eingehender Nachrichten 13002 / 13008 / 13009
            </Card>
         </Tab>
      </Tabs>
   </Step>
</Steps>
