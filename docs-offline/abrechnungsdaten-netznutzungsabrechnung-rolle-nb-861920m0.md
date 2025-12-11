# Abrechnungsdaten Netznutzungsabrechnung (Rolle NB)

# Prozessübersicht

![LW24h mit Abhängigkeiten - Abr.Da. NNA (NB).png](https://api.apidog.com/api/v1/projects/816353/resources/352493/image-preview)

<Steps>
  <Step title="Prozessauslöser - Event" defaultOpen={false}>
    <Tabs>
      <Tab title="Übersicht">
 
        <Card title="Abrechnungsdaten Netznutzungsabrechnung"
              href="https://doc.macoapp.de/abrechnungsdaten-netznutzungsabrechnung-versenden-14333071e0.md">
            Triggert den Versand von Abrechnungsdaten Netznutzungsabrechnung Nachrichten an Marktpartner
        </Card>

      </Tab>        
      <Tab title="📄START_ABR_NN">
          <Accordion title="Abrechnungsdaten Netznutzungsabrechnung" defaultOpen={false}>
                    <DataSchema id="5244395" />
          </Accordion>
      </Tab>
      <Tab title="📄55218 Abr.-Daten NNA">
          <Accordion title="PI_55218" defaultOpen={false}>
                    <DataSchema id="5242405" />
      </Accordion>
      </Tab>
    </Tabs>
</Step>
    
<Step title="Schnittstelle aktualisieren der Prozessdaten">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Aktualisieren der Prozessdaten"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14666382e0.md">
              Übergabe der erzeugten (55220) Rückmeldung und der Statusmeldung (21047) an das Backend
          </Card>
      </Tab>        
      <Tab title="55220 Rückmeldung Anfrage Abr.-Daten NNA">
          <Accordion title="PI_55220" defaultOpen={false}>
                     <DataSchema id="5242406" />
          </Accordion>
      </Tab>
      <Tab title="21047 Bearbeitungsstand zur Rückmeldung">
          <Accordion title="PI_21047" defaultOpen={false}>
                  <DataSchema id="5718596" />
          </Accordion>
      </Tab>
    </Tabs>
  </Step> 
    
    
</Steps>

