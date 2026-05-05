# Anfrage zur Stammdatenänderung von Netzbetreiber an Lieferant (verantwortlich) (Rolle LF)


![LW24h mit Abhängigkeiten - GAS Anfrage zur Stammdatenänderung von Messstellenbetreiber an den Lieferanten (verantwortlich) (Rolle LF).png](https://api.apidog.com/api/v1/projects/816353/resources/373055/image-preview)
<Steps>
   <Step title="Prozessauslöser - eingehende Edifact" defaultOpen={false}>
      <Tabs>
         <Tab title="Übersicht">
            <Card title="44137" defaultOpen={false}>
               <Accordion title="44137 Nicht Bila. rel. Anfrage an LF" defaultOpen={false}>
                  <DataSchema id="13005688" />
               </Accordion>
            </Card>
         </Tab>
      </Tabs>
   </Step>
   <Step title="ausgehende Edi" defaultOpen={false}>
      <Tabs>
         <Tab title="Übersicht">
            <Card title="44138" defaultOpen={false}>
               <Accordion title="44138 Antwort auf Anfrage" defaultOpen={false}>
                  <DataSchema id="13005689" />
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
               Erstellen der Prozessdaten mit eingehender Nachricht 44137
            </Card>
            <Card title="Aktualiseren der Prozessdaten"
               href="https://doc.macoapp.de/prozessdaten-aktualiseren-14017182e0.md">
               Aktualisieren der Prozessdaten mit ausgehender Nachricht 44138
            </Card>
         </Tab>
      </Tabs>
   </Step>
</Steps>
