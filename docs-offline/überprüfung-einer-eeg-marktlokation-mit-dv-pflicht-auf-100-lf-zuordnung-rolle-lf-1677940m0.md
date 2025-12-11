# Überprüfung einer EEG-Marktlokation mit DV-Pflicht auf 100% LF-Zuordnung ( Rolle LF )

Überprüfung einer EEG-Marktlokation mit DV-Pflicht auf 100% LF-Zuordnung ( Rolle LF )


![LW24h mit Abhängigkeiten - Überprüfung einer EEG-Marktlokation mit DV-Pflicht auf 100_ LF-Zuordnung ( Rolle LF ).png](https://api.apidog.com/api/v1/projects/816353/resources/364102/image-preview)

<Steps>
  <Step title="Prozessauslöser - eingehende EDI">
    <Tabs>
      <Tab title="Übersicht"> 
        <Card title="55607">
          Ankündigung Zuordnung / Zuordnung des LF zur erz. MaLo/ Tranche
        </Card>
      </Tab>        
      <Tab title="55607 Ankündigung Zuordnung / Zuordnung des LF zur erz. MaLo/ Tranche">
          <Accordion title="PI_55607" defaultOpen={false}>
              <DataSchema id="5562269" />
          </Accordion>
          
      </Tab>
    </Tabs>
  </Step>
    
    <Step title="Prozessinitiierung Backend">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Erstellen der Prozessdaten"
                href="https://doc.macoapp.de/prozessdaten-erstellen-14017183e0.md">
              Übergabe der Nachricht (55607) an das Backend
          </Card>
      </Tab>        
      <Tab title="55607 - Ankündigung Zuordnung">
          <Accordion title="PI_55607" defaultOpen={false}>
              <DataSchema id="5562269" />
          </Accordion>
          
      </Tab>
    </Tabs>
  </Step>
    
  <Step title="Prozessinitiierung Backend">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Aktualiesieren der Prozessdaten"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14017182e0.md">
              Übergabe der Nachricht (55608, 55609) an das Backend
          </Card>
      </Tab>        
      <Tab title="55608 - Bestätigung Zuordnung LF zur erz. MaLo/ Tranche">
          <Accordion title="PI_55608" defaultOpen={false}>
              <DataSchema id="5562270" />
          </Accordion>
      </Tab>
        
     <Tab title="55609 - Ablehnung LF zur erz. MaLo/ Tranch">
          <Accordion title="PI_55609" defaultOpen={false}>
              <DataSchema id="5562271" />
          </Accordion>
      </Tab>   
    </Tabs>
  </Step>  
    
 <Step title="Prozessinitiierung Backend">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Aktualiesieren der Prozessdaten"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14017182e0.md">
              Übergabe der Nachricht (55608, 55609) an das Backend
          </Card>
      </Tab>        
      <Tab title="55608 - Bestätigung Zuordnung LF zur erz. MaLo/ Tranche">
          <Accordion title="PI_55608" defaultOpen={false}>
              <DataSchema id="5562270" />
          </Accordion>
      </Tab>
        
     <Tab title="55609 - Ablehnung LF zur erz. MaLo/ Tranch">
          <Accordion title="PI_55609" defaultOpen={false}>
              <DataSchema id="5562271" />
          </Accordion>
      </Tab>   
    </Tabs>
  </Step>  
    
</Steps>



