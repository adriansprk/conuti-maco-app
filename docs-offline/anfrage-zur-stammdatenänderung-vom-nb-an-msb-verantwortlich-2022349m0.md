# Anfrage zur Stammdatenänderung vom NB an MSB (verantwortlich)


![LW24h mit Abhängigkeiten - GAS Anfrage zur Stammdatenänderung vom NB an MSB (verantwortlich).png](https://api.apidog.com/api/v1/projects/816353/resources/373402/image-preview)

<Steps>
   <Step title="Prozessauslöser - eingehende Edifact" defaultOpen={false}>
      <Tabs>
         <Tab title="Übersicht">
            <Card title="44148" defaultOpen={false}>
               <Accordion title="44148 Anfrage an MSB mit Abhängigkeiten" defaultOpen={false}>  
                   <DataSchema id="13005697" />
               </Accordion>
            </Card>
            <Card title="44166" defaultOpen={false}>
               <Accordion title="44166 Nicht bila. rel Anfrage an MSB ohne Abhängigkeiten" defaultOpen={false}>                  
                   <DataSchema id="13005711" />
               </Accordion>
            </Card>
         </Tab>
      </Tabs>
   </Step>
   <Step title="ausgehende Edi" defaultOpen={false}>
      <Tabs>
         <Tab title="Übersicht">
            <Card title="44149 Antwort auf Anfrage" defaultOpen={false}>
               <Accordion title="44149" defaultOpen={false}>
                  <DataSchema id="13005698" />
               </Accordion>
            </Card>
            <Card title="44167 Antwort auf Anfrage" defaultOpen={false}>
               <Accordion title="44167" defaultOpen={false}>
                  <DataSchema id="13005712" />
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
               Erstellen der Prozessdaten mit eingehenden Nachrichten 44148 und 44166
            </Card>
            <Card title="Aktualiseren der Prozessdaten"
               href="https://doc.macoapp.de/prozessdaten-aktualiseren-14017182e0.md">
               Aktualisieren der Prozessdaten mit ausgehenden Nachrichten 44149 und 44167
            </Card>
         </Tab>
      </Tabs>
   </Step>
</Steps>

