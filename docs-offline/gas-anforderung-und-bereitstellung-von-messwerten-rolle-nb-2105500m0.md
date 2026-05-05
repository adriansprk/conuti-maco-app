# GAS Anforderung und Bereitstellung von Messwerten (Rolle NB)

![LW24h mit Abhängigkeiten - GAS Anforderung und Bereitstellung von Messwerten ( Rolle NB VNB ).png](https://api.apidog.com/api/v1/projects/816353/resources/375624/image-preview)
<Steps>
   <Step title="Prozessauslöser - Event" defaultOpen={false}>
      <Tabs>
         <Tab title="Übersicht">
            <Card title="START_ANFORDERUNG_MESSWERTE"
               >
               START_ANFORDERUNG_MESSWERTE
            </Card>
            <Card title="17004"
               >
               Anforderung von Werten
            </Card>
            <Card title="START_ERHEBUNG_MESSWERTE"
               >
               START_ERHEBUNG_MESSWERTE
            </Card>
            <Card title="13002"
               >
               Zählerstand (Gas)
            </Card>
            <Card title="13008"
               >
               Lastgang (Gas)
            </Card>
            <Card title="13009"
               >
               Energiemenge (Gas)
            </Card>
         </Tab>
         <Tab title="📄Event ">
            <Accordion title="START_ANFORDERUNG_MESSWERTE" defaultOpen={false}>
               <DataSchema id="14434632" />
            </Accordion>
            <Accordion title="START_ERHEBUNG_MESSWERTE" defaultOpen={false}>
               <DataSchema id="14445758" />
            </Accordion>
         </Tab>
         <Tab title="📄13002 Zählerstand (Gas)">
            <Accordion title="13002" defaultOpen={false}>
               <DataSchema id="13005918" />
            </Accordion>
         </Tab>
         <Tab title="📄13008 Lastgang (Gas)">
            <Accordion title="13008" defaultOpen={false}>
               <DataSchema id="13005921" />
            </Accordion>
         </Tab>
         <Tab title="📄13009 Energiemenge (Gas)">
            <Accordion title="13009" defaultOpen={false}>
               <DataSchema id="13005922" />
            </Accordion>
         </Tab>
      </Tabs>
   </Step>
   <Step title="Schnittstelle aktualisieren der Prozessdaten">
      <Tabs>
         <Tab title="Übersicht">
            <Card title="Aktualisieren der Prozessdaten"
               href="https://doc.macoapp.de/prozessdaten-aktualiseren-14017182e0.md">
               ausgehende Nachrichten 17004, 13002, 13008, 13009
               eingehende Nachrichten 19007, 21028, 13002, 13008, 13009
            </Card>
         </Tab>
         <Tab title="19007 - Ablehnung Anforderung Werte">
            <Accordion title="19007" defaultOpen={false}>
               <DataSchema id="13005863" />
            </Accordion>
         </Tab>
         <Tab title="21028 - Informationsmeldung">
            <Accordion title="21028" defaultOpen={false}>
               <DataSchema id="8348219" />
            </Accordion>
         </Tab>
         <Tab title="📄13002 Zählerstand (Gas)">
            <Accordion title="13002" defaultOpen={false}>
               <DataSchema id="13005918" />
            </Accordion>
         </Tab>
         <Tab title="📄13008 Lastgang (Gas)">
            <Accordion title="13008" defaultOpen={false}>
               <DataSchema id="13005921" />
            </Accordion>
         </Tab>
         <Tab title="📄13009 Energiemenge (Gas)">
            <Accordion title="13009" defaultOpen={false}>
               <DataSchema id="13005922" />
            </Accordion>
         </Tab>
      </Tabs>
   </Step>
</Steps>
