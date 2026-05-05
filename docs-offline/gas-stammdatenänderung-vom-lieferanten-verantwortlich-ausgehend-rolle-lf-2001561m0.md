# GAS Stammdatenänderung vom Lieferanten (verantwortlich) ausgehend (Rolle LF)

![LW24h mit Abhängigkeiten - Anfrage zur Stammdatenänderung von Lieferant an Messstellenbetreiber (verantwortlich) .png](https://api.apidog.com/api/v1/projects/816353/resources/373021/image-preview)
<Steps>
   <Step title="Prozessauslöser - Event" defaultOpen={false}>
      <Tabs>
         <Tab title="Übersicht">
            <Card title="START_ANFRAGE_STAMMDATENAENDERUNG"
               >
               START_ANFRAGE_STAMMDATENAENDERUNG
            </Card>
            <Card title="44109"
               >
               Nicht bila.rel Änderung vom LF
            </Card>
            <Card title="44120"
               >
               Bila.rel. Änderung vom LF
            </Card>
         </Tab>
         <Tab title="📄Event ">
            <Accordion title="START_VERSAND_SDAE" defaultOpen={false}>
               <DataSchema id="5854731" />
            </Accordion>
         </Tab>
         <Tab title="📄44109 Nicht bila.rel Änderung vom LF">
            <Accordion title="44109" defaultOpen={false}>
               <DataSchema id="13005676" />
            </Accordion>
         </Tab>
         <Tab title="📄44120 Bila.rel. Änderung vom LF">
            <Accordion title="44120" defaultOpen={false}>
               <DataSchema id="13005684" />
            </Accordion>
         </Tab>
      </Tabs>
   </Step>
   <Step title="Schnittstelle aktualisieren der Prozessdaten">
      <Tabs>
         <Tab title="Übersicht">
            <Card title="Aktualisieren der Prozessdaten"
               href="https://doc.macoapp.de/prozessdaten-aktualiseren-14017182e0.md">
               ausgehende Nachrichten 44109, 44120
               eingehende Nachrichten 44111, 44121
            </Card>
         </Tab>
         <Tab title="44111 Antwort auf Änderung vom LF">
            <Accordion title="44111" defaultOpen={false}>
               <DataSchema id="13005677" />
            </Accordion>
         </Tab>
         <Tab title="44121 Antwort auf Änderung vom LF">
            <Accordion title="44121" defaultOpen={false}>
               <DataSchema id="13005685" />
            </Accordion>
         </Tab>
      </Tabs>
   </Step>
</Steps>
