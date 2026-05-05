# Anfrage zur Stammdatenänderung von Lieferant an Netzbetreiber (verantwortlich) (Rolle LF)

![LW24h mit Abhängigkeiten - GAS Anfrage zur Stammdatenänderung von Lieferant an Netzbetreiber (verantwortlich) (Rolle LF) (3).png](https://api.apidog.com/api/v1/projects/816353/resources/373037/image-preview)
<Steps>
   <Step title="Prozessauslöser - Event" defaultOpen={false}>
      <Tabs>
         <Tab title="Übersicht">
            <Card title="START_ANFRAGE_STAMMDATENAENDERUNG"
               >
               START_ANFRAGE_STAMMDATENAENDERUNG
            </Card>
            <Card title="44139"
               >
               Nicht bila.rel. Anfrage an NB
            </Card>
            <Card title="44156"
               >
               Bila.rel. Anfrage an NB mit Abhängigkeiten
            </Card>
            <Card title="44180"
               >
               Anfrage der Marktlokationsstruktur
            </Card>
         </Tab>
         <Tab title="📄Event ">
            <Accordion title="START_ANFRAGE_STAMMDATENAENDERUNG" defaultOpen={false}>
               <DataSchema id="13241832" />
            </Accordion>
         </Tab>
         <Tab title="📄44139 Nicht bila.rel. Anfrage an NB">
            <Accordion title="44139" defaultOpen={false}>
               <DataSchema id="13005690" />
            </Accordion>
         </Tab>
         <Tab title="📄44156 Bila.rel. Anfrage an NB mit Abhängigkeiten">
            <Accordion title="44156" defaultOpen={false}>
               <DataSchema id="13005702" />
            </Accordion>
         </Tab>
         <Tab title="📄44180 Anfrage der Marktlokationsstruktur">
            <Accordion title="44180" defaultOpen={false}>
               <DataSchema id="13005715" />
            </Accordion>
         </Tab>
      </Tabs>
   </Step>
   <Step title="Schnittstelle aktualisieren der Prozessdaten">
      <Tabs>
         <Tab title="Übersicht">
            <Card title="Aktualisieren der Prozessdaten"
               href="https://doc.macoapp.de/prozessdaten-aktualiseren-14017182e0.md">
               ausgehende Nachrichten 44139, 44156. 44180
               eingehende Nachrichten 44142, 44157, 44181, 44182
            </Card>
         </Tab>
         <Tab title="44142 - Antwort auf Anfrage">
            <Accordion title="44142" defaultOpen={false}>
               <DataSchema id="13005692" />
            </Accordion>
         </Tab>
         <Tab title="44157 - Antwort auf Anfrage">
            <Accordion title="44157" defaultOpen={false}>
               <DataSchema id="13005703" />
            </Accordion>
         </Tab>
         <Tab title="44181 - Antwort auf Anfrage der Marktlokationsstruktur">
            <Accordion title="44181" defaultOpen={false}>
               <DataSchema id="13005716" />
            </Accordion>
         </Tab>
         <Tab title="44182 - Ablehnung der Anfrage der Marktlokationsstruktur">
            <Accordion title="44182" defaultOpen={false}>
               <DataSchema id="13005717" />
            </Accordion>
         </Tab>
      </Tabs>
   </Step>
</Steps>
