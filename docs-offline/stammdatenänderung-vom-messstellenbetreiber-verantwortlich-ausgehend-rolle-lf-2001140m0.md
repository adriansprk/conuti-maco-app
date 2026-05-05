# Stammdatenänderung vom Messstellenbetreiber (verantwortlich) ausgehend ( Rolle LF )

![LW24h mit Abhängigkeiten - Stammdatenänderung vom Messstellenbetreiber (verantwortlich) ausgehend ( Rolle LF ).png](https://api.apidog.com/api/v1/projects/816353/resources/373029/image-preview)
<Steps>
   <Step title="Prozessauslöser - eingehende Edifact" defaultOpen={false}>
      <Tabs>
         <Tab title="Übersicht">
            <Card title="44117" defaultOpen={false}>
               <Accordion title="44117 Änderung vom MSB mit Abhängigkeiten" defaultOpen={false}>
                  <DataSchema id="13005682" />
               </Accordion>
            </Card>
            <Card title="44160" defaultOpen={false}>
               <Accordion title="44160 Änderung vom MSB ohne
                  Abhängigkeiten" defaultOpen={false}>
                  <DataSchema id="13005705" />
               </Accordion>
            </Card>
         </Tab>
      </Tabs>
   </Step>
   <Step title="ausgehende Edi" defaultOpen={false}>
      <Tabs>
         <Tab title="Übersicht">
            <Card title="44119" defaultOpen={false}>
               <Accordion title="44119 Antwort auf Änderung vom MSB" defaultOpen={false}>
                  <DataSchema id="13005683" />
               </Accordion>
            </Card>
            <Card title="44161" defaultOpen={false}>
               <Accordion title="44161 Antwort auf Änderung" defaultOpen={false}>
                  <DataSchema id="13005706" />
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
               Erstellen der Prozessdaten mit eingehender Nachrichten 44117 / 44160
            </Card>
            <Card title="Aktualiseren der Prozessdaten"
               href="https://doc.macoapp.de/prozessdaten-aktualiseren-14017182e0.md">
               Aktualisieren der Prozessdaten mit ausgehender Nachrichten 44119 / 44161
            </Card>
         </Tab>
      </Tabs>
   </Step>
</Steps>
