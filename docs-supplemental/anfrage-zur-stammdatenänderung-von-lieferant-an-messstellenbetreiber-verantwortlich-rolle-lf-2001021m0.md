# Anfrage zur Stammdatenänderung von Lieferant an Messstellenbetreiber (verantwortlich) (Rolle LF)

![LW24h mit Abhängigkeiten - Anfrage zur Stammdatenänderung von Lieferant an Messstellenbetreiber (verantwortlich) .png](https://api.apidog.com/api/v1/projects/816353/resources/373021/image-preview)
<Steps>
   <Step title="Prozessauslöser - Event" defaultOpen={false}>
      <Tabs>
         <Tab title="Übersicht">
            <Card title="START_ANFRAGE_STAMMDATENAENDERUNG"
               >
               START_ANFRAGE_STAMMDATENAENDERUNG
            </Card>
            <Card title="44143"
               >
               Anfrage an MSB mit Abhängigkeiten
            </Card>
            <Card title="44162"
               >
               Anfrage an MSB ohne Abhängigkeiten
            </Card>
         </Tab>
         <Tab title="📄Event ">
            <Accordion title="START_ANFRAGE_STAMMDATENAENDERUNG" defaultOpen={false}>
               <DataSchema id="13241832" />
            </Accordion>
         </Tab>
         <Tab title="📄44143 Anfrage an MSB mit Abhängigkeiten">
            <Accordion title="44143" defaultOpen={false}>
               <DataSchema id="13005693" />
            </Accordion>
         </Tab>
         <Tab title="📄44162  Anfrage an MSB ohne Abhängigkeiten">
            <Accordion title="44162" defaultOpen={false}>
               <DataSchema id="13005707" />
            </Accordion>
         </Tab>
      </Tabs>
   </Step>
   <Step title="Schnittstelle aktualisieren der Prozessdaten">
      <Tabs>
         <Tab title="Übersicht">
            <Card title="Aktualisieren der Prozessdaten"
               href="https://doc.macoapp.de/prozessdaten-aktualiseren-14017182e0.md">
               ausgehende Nachrichten 44143, 44162
               eingehende Nachrichten 44145, 44146, 44163, 44164
            </Card>
         </Tab>
         <Tab title="44145 - Antwort auf Anfrage">
            <Accordion title="44145" defaultOpen={false}>
               <DataSchema id="13005694" />
            </Accordion>
         </Tab>
         <Tab title="44146 - Ablehnung der Anfrage">
            <Accordion title="44146" defaultOpen={false}>
               <DataSchema id="13005695" />
            </Accordion>
         </Tab>
         <Tab title="44163 - Antwort auf Anfrage">
            <Accordion title="44163" defaultOpen={false}>
               <DataSchema id="13005708" />
            </Accordion>
         </Tab>
         <Tab title="44164 - Ablehnung der Anfrage">
            <Accordion title="44164" defaultOpen={false}>
               <DataSchema id="13005709" />
            </Accordion>
         </Tab>
      </Tabs>
   </Step>
</Steps>
