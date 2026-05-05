# GAS Informationsmeldung zur Aufhebung einer zuk. Zuordnung (LFZ)

# Prozessübersicht

![LW24h mit Abhängigkeiten -  GAS Aufhebung der Zuordnung des LFZ (LFZ).png](https://api.apidog.com/api/v1/projects/816353/resources/370894/image-preview)

<Steps>
  <Step title="Prozessauslöser - eingehende EDI">
    <Tabs>
      <Tab title="Übersicht"> 
        <Card title="44038">
          Aufhebung der Zuordnung des LFZ zur Marklokation bzw. Tranche
        </Card>
      </Tab>        
      <Tab title="44038">
          <Accordion title="44038" defaultOpen={false}>
              <DataSchema id="8347917" />
          </Accordion>
          
      </Tab>
    </Tabs>
  </Step>
    <Step title="Schnittstelle lesend für APERAK">
      <Tabs>
      <Tab title="Übersicht">
          <Card title="Marktlokation lesen"
                href="https://doc.macoapp.de/marktlokation-lesen-14017020e0.md">
                Lesen einer MaLo mittels LokationsId zu einem bestimmten Zeitpunkt
          </Card>    
      </Tab>        
      <Tab title="📄Marktlokation ">
          <Accordion title="Marktlokation" defaultOpen={false}>
              <DataSchema id="5241973" />
          </Accordion>
          </Tab>
        </Tabs>
    </Step>
    <Step title="Prozessinitiierung Backend">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Erstellen Prozessdaten für Prüfi 55038"
                href="https://doc.macoapp.de/prozessdaten-erstellen-14017183e0.md">
              Übergabe der initialen Prozessdaten an das Backend
          </Card>
      </Tab>        
      <Tab title="📄44038">
          <Accordion title="44038" defaultOpen={false}>
               <DataSchema id="8347917" />
          </Accordion>
      </Tab> 
    </Tabs>
  </Step>
</Steps>
