# GAS Informationsmeldung zur Beendigung der Zuordnung NB an LFA (LFA)

# Prozessübersicht


![LW24h mit Abhängigkeiten - GAS Informationsmeldung zur Beendigung der Zuordnung NB an LFA (LFA).png](https://api.apidog.com/api/v1/projects/816353/resources/370907/image-preview)

<Steps>
  <Step title="Prozessauslöser - eingehende EDI">
    <Tabs>
      <Tab title="Übersicht"> 
        <Card title="44037">
          Informationsmeldung zur Beendigung der Zuordnung
        </Card>
      </Tab>        
      <Tab title="44037">
          <Accordion title="44037" defaultOpen={false}>
              <DataSchema id="8347916" />
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
    <Step title="Schnittstelle aktualisieren und erstellen der Prozessdaten">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Aktualisieren der Prozessdaten"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14017182e0.md">
              Übergabe der Nachricht (44037) an das Backend
          </Card>
          <Card title="Erstellen der Prozessdaten"
                href="https://doc.macoapp.de/prozessdaten-erstellen-14017183e0.md">
              Übergabe der Nachricht (44037) an das Backend
          </Card>
      </Tab>        
      <Tab title="44037">
          <Accordion title="44037" defaultOpen={false}>
              <DataSchema id="8347916" />
          </Accordion>
          
          
      </Tab>
    </Tabs>
  </Step>
</Steps>
