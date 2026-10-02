# Anfrage zur Stammdatenänderung vom MSB an NB (verantwortlich) (Rolle NB)


![LW24h mit Abhängigkeiten - GAS Anfrage zur Stammdatenänderung vom MSB an NB (verantwortlich) (Rolle NB).png](https://api.apidog.com/api/v1/projects/816353/resources/373077/image-preview)

<Steps>
   <Step title="Prozessauslöser - einghende Edi" defaultOpen={false}>
      <Tabs>
         <Tab title="Übersicht">
            <Card title="44140 Nicht bila.rel. Anfrage an NB (Gas)" defaultOpen={false}>
               <Accordion title="44140 Nicht bila.rel. Anfrage an NB (Gas)" defaultOpen={false}>
                  <DataSchema id="13005691" />
               </Accordion>
            </Card>
         </Tab>
      </Tabs>
   </Step>
   <Step title="ausgehende Edi" defaultOpen={false}>
      <Tabs>
         <Tab title="Übersicht">
            <Card title="44142 Antwort auf Anfrage (Gas)" defaultOpen={false}>
               <Accordion title="44142" defaultOpen={false}>
                  <DataSchema id="13005692" />
               </Accordion>
            </Card>
            <Card title="44117 Änderung vom MSB mit Abhängigkeiten an LF(Gas)" defaultOpen={false}>
               <Accordion title="44117 an LF" defaultOpen={false}>
                  <DataSchema id="13005682" />
               </Accordion>
            </Card>
         </Tab>
      </Tabs>
   </Step>
   <Step title="eingehende Edis" defaultOpen={false}>
      <Tabs>
         <Tab title="Übersicht">
            <Card title="44119 Antwort auf Änderung vom MSB" defaultOpen={false}>
               <Accordion title="44119" defaultOpen={false}>
                  <DataSchema id="13005683" />
               </Accordion>
            </Card>
         </Tab>
      </Tabs>
   </Step>
   <Step title="Schnittstellen schreibend">
      <Tabs>
         <Tab title="Übersicht">
            <Card title="Erstellen der Prozessdaten"
               href="https://doc.macoapp.de/prozessdaten-erstellen-14666311e0.md">
               Aktualisieren der Prozessdaten mit eingehender Nachricht 44140
            </Card>
            <Card title="Aktualiseren der Prozessdaten"
               href="https://doc.macoapp.de/prozessdaten-aktualiseren-14666382e0.md">
               Aktualisieren der Prozessdaten mit ausgehenden Nachrichten 44142 und 44117 und eingehender Nachricht 44119
            </Card>
         </Tab>
      </Tabs>
   </Step>
</Steps>


