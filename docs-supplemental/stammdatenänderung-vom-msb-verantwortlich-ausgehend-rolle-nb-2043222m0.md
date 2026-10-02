# Stammdatenänderung vom MSB (verantwortlich) ausgehend (Rolle NB)


![LW24h mit Abhängigkeiten - GAS Stammdatenänderung vom MSB (verantwortlich) ausgehend (Rolle NB).png](https://api.apidog.com/api/v1/projects/816353/resources/374041/image-preview)

<Steps>
   <Step title="Prozessauslöser - einghende Edi" defaultOpen={false}>
      <Tabs>
         <Tab title="Übersicht">
            <Card title="44116 Änderung vom MSB mit Abhängigkeiten" defaultOpen={false}>
               <Accordion title="44116 " defaultOpen={false}>
             
<DataSchema id="13005681" />
               </Accordion>
            </Card>
               <Card title="44159 Änderung vom MSB ohne Abhängigkeiten" defaultOpen={false}>
               <Accordion title="44159 " defaultOpen={false}>
             

<DataSchema id="13005704" />
               </Accordion>
            </Card>
         </Tab>
      </Tabs>
   </Step>
   <Step title="ausgehende Edi" defaultOpen={false}>
      <Tabs>
         <Tab title="Übersicht">
            <Card title="44117 Änderung vom MSB mit Abhängigkeiten" defaultOpen={false}>
               <Accordion title="44117 an LF" defaultOpen={false}>
            
<DataSchema id="13005682" />
               </Accordion>
            </Card>
            <Card title="44160 Änderung vom MSB ohne
Abhängigkeiten" defaultOpen={false}>
               <Accordion title="44160 an LF" defaultOpen={false}>
                  
<DataSchema id="13005705" />
               </Accordion>
            </Card>
                         <Card title="44119 Änderung vom MSB mit Abhängigkeiten" defaultOpen={false}>
               <Accordion title="44119 an MSB" defaultOpen={false}>
            

<DataSchema id="13005683" />
               </Accordion>
            </Card>
            <Card title="44161 Antwort auf Änderung" defaultOpen={false}>
               <Accordion title="44161 an MSB" defaultOpen={false}>
                  

<DataSchema id="13005706" />
               </Accordion>
            </Card>
         </Tab>
      </Tabs>
   </Step>
   <Step title="eingehende Edis" defaultOpen={false}>
      <Tabs>
         <Tab title="Übersicht">
            <Card title="44119 Antwort auf Änderung vom MSB" defaultOpen={false}>
               <Accordion title="44119 von LF" defaultOpen={false}>
                  <DataSchema id="13005683" />
               </Accordion>
            </Card>
                         <Card title="44161 Antwort auf Änderung" defaultOpen={false}>
               <Accordion title="44161 von LF" defaultOpen={false}>
                  

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

