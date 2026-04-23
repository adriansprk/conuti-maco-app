# Aufhebung der Zuordnung des LFZ zur Marktlokation bzw. Tranche (Rolle LFZ)

# Prozessübersicht

![LW24h mit Abhängigkeiten - Aufhebung Zuordnung LFZ (LFZ).jpeg](https://api.apidog.com/api/v1/projects/816353/resources/358230/image-preview)

<Steps>
  <Step title="Prozessauslöser - eingehende EDI">
    <Tabs>
      <Tab title="Übersicht"> 
        <Card title="55038">
          Aufhebung der Zuordnung des LFZ zur Marklokation bzw. Tranche
        </Card>
      </Tab>        
      <Tab title="55038">
          <Accordion title="PI_55038" defaultOpen={false}>
              <DataSchema id="5242374" />
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
      <Tab title="📄55038">
          <Accordion title="PI_55038" defaultOpen={false}>
               <DataSchema id="5242374" />
          </Accordion>
      </Tab> 
    </Tabs>
  </Step>
</Steps>

