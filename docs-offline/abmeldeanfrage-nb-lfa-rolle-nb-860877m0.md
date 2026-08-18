# Abmeldeanfrage NB -> LFA (Rolle NB)

# Prozessübersicht
![LW24h mit Abhängigkeiten - Abmeldeanfrage (NB).png](https://api.apidog.com/api/v1/projects/816353/resources/352490/image-preview)

<Steps>
  <Step title="Prozessauslöser - Event" defaultOpen={false}>
    <Tabs>
      <Tab title="Übersicht">
 
        <Card title="START_ABMELDEANFRAGE"
              href="https://doc.macoapp.de/anfrage-zur-beendigung-der-zuordnung-des-lfa-zur-marktlokation-bzw-tranche-14992646e0.md">
            Anfrage zur Beendigung der Zuordnung des LFA zur Marktlokation bzw. Tranche
        </Card>

      </Tab>        
      <Tab title="📄START_ABMELDEANFRAGE">
          <Accordion title="ABMELDEANFRAGE" defaultOpen={false}>
                    <DataSchema id="5757038" />
          </Accordion>
          
      </Tab>
        <Tab title="📄55010 Anfrage zur Beendigung der Zuordnung">
          <Accordion title="PI_55010" defaultOpen={false}>
                    <DataSchema id="5242359" />
          </Accordion>
          
      </Tab>
    </Tabs>

  </Step>
  <Step title="Schnittstellen lesend">
    <Tabs>
      <Tab title="Übersicht">
          <CardGroup cols={4}>
          <Card title="Marktlokation lesen"
                href="https://doc.macoapp.de/marktlokation-lesen-14017020e0.md">
              Lesen einer MaLo mittels LokationsId zu einem bestimmten Zeitpunkt
          </Card>
          <Card title="Bilanzierung lesen" 
                href="https://doc.macoapp.de/bilanzierung-lesen-14017013e0.md">
              Lesen einer Bilanzierung mittels LokationsId zu einem bestimmten Zeitpunkt
          </Card>
          <Card title="Energieliefervertrag lesen" 
                href="https://doc.macoapp.de/energieliefervertrag-lesen-14017014e0.md">
              Lesen eines Energieliefervertrages mittels LokationsId zu einem bestimmten Zeitpunkt
          </Card>
          <Card title="Netznutzungsvertrag lesen" 
                href="https://doc.macoapp.de/netznutzungsvertrag-lesen-14017027e0.md">
              Lesen einee Netznutzungsvertrages mittels LokationsId zu einem bestimmten Zeitpunkt
          </Card>
        </CardGroup>    
      </Tab>        
      <Tab title="📄Marktlokation">
          <Accordion title="Marktlokation" defaultOpen={false}>
                    <DataSchema id="5241973" />
          </Accordion>
      </Tab>
      <Tab title="📄Bilanzierung">
          <Accordion title="Bilanzierung" defaultOpen={false}>
                  <DataSchema id="5241965" />
          </Accordion>
      </Tab>
        <Tab title="📄Energieliefervertrag">
          <Accordion title="Energieliefervertrag" defaultOpen={false}>
                  <DataSchema id="5241988" />
          </Accordion>
      </Tab>
        <Tab title="📄Netznutzungsvertrag">
          <Accordion title="Netznutzungsvertrag" defaultOpen={false}>
                  <DataSchema id="5242152" />  
          </Accordion>
      </Tab>
    </Tabs>
  </Step>
  <Step title="Schnittstelle aktualisieren der Prozessdaten">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Aktualisieren der Prozessdaten"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14017182e0.md">
              Übergabe der erzeugten neg. (55012) oder pos. (55011) Rückmeldung an das Backend
          </Card>
      </Tab>        
      <Tab title="55012 - Ablehnung Beendigung der Zuordnung">
          <Accordion title="PI_55012" defaultOpen={false}>
                   <DataSchema id="5242361" />
          </Accordion>
      </Tab>
      <Tab title="55011 - Bestätigung Beendigung der Zuordnung">
          <Accordion title="PI_55011" defaultOpen={false}>
                 <DataSchema id="5242360" />
          </Accordion>
        
      </Tab>        
    </Tabs>
  </Step>  
</Steps>



