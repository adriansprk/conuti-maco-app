# Stammdatenänderung vom Netzbetreiber (verantwortlich) ausgehend (Rolle LF)


![LW24h mit Abhängigkeiten - GAS Stammdatenänderung vom Netzbetreiber (verantwortlich) ausgehend (Rolle LF).png](https://api.apidog.com/api/v1/projects/816353/resources/373038/image-preview)
<Steps>
   <Step title="Prozessauslöser - eingehende Edifact" defaultOpen={false}>
      <Tabs>
         <Tab title="Übersicht">
            <Card title="44112" defaultOpen={false}>
               <Accordion title="44112 Nicht bila.rel. Änderung vom NB" defaultOpen={false}>
                  <DataSchema id="13005678" />
               </Accordion>
            </Card>
            <Card title="44123" defaultOpen={false}>
               <Accordion title="44123 Bila.rel. Änderung vom NB mit Abhängigkeiten" defaultOpen={false}>
                  <DataSchema id="13005686" />
               </Accordion>
            </Card>
         </Tab>
      </Tabs>
   </Step>
   <Step title="ausgehende Edi" defaultOpen={false}>
      <Tabs>
         <Tab title="Übersicht">
            <Card title="44115" defaultOpen={false}>
               <Accordion title="44115 Antwort auf Änderung vom NB" defaultOpen={false}>
                  <DataSchema id="13005680" />
               </Accordion>
            </Card>
            <Card title="44124" defaultOpen={false}>
               <Accordion title="44124 Antwort auf Änderung vom NB" defaultOpen={false}>
                  <DataSchema id="13005687" />
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
               Erstellen der Prozessdaten mit eingehender Nachrichten 44112 / 44123
            </Card>
            <Card title="Aktualiseren der Prozessdaten"
               href="https://doc.macoapp.de/prozessdaten-aktualiseren-14017182e0.md">
               Aktualisieren der Prozessdaten mit ausgehender Nachrichten 44115 / 44124
            </Card>
         </Tab>
      </Tabs>
   </Step>
</Steps>
