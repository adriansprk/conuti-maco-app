# Abrechnungsdaten Bilanzkreisabrechnung (Rolle NB)

# Prozessübersicht

![LW24h mit Abhängigkeiten - Abr.Da. BKA (NB).png](https://api.apidog.com/api/v1/projects/816353/resources/352494/image-preview)

<Steps>
  <Step title="Prozessauslöser - Event" defaultOpen={false}>
    <Tabs>
      <Tab title="Übersicht">
 
        <Card title="Abrechnungsdaten Bilanzkreisabrechnung"
              href="https://doc.macoapp.de/abrechnungsdaten-bilanzkreisabrechnung-versenden-14994259e0.md">
            Triggert den Versand von Abrechnungsdaten Bilanzkreisabrechnung Nachrichten an Marktpartner
        </Card>

      </Tab>        
      <Tab title="📄START_ABR_BK">
          <Accordion title="Abrechnungsdaten Bilanzkreisabrechnung" defaultOpen={false}>
                <DataSchema id="5717780" />
          </Accordion>
      </Tab>
      <Tab title="📄55126 Abrechnungsdaten Bilanzkreisabrechnung verbrauchende Marktlokation">
          <Accordion title="PI_55126" defaultOpen={false}>
              <DataSchema id="5242393" />
          </Accordion>
      </Tab>
    </Tabs>
</Step>
    
<Step title="Schnittstelle aktualisieren der Prozessdaten">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Aktualisieren der Prozessdaten"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14666382e0.md">
              Übergabe der erzeugten Rückmeldung (55156) und der Statusmeldung (21047) an das Backend
          </Card>
      </Tab>        
      <Tab title="55156 Rückmeldung Anfrage Abr.-Daten BK-Abr. verb. MaLo">
          <Accordion title="PI_55156" defaultOpen={false}>
                <DataSchema id="5242396" />
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
