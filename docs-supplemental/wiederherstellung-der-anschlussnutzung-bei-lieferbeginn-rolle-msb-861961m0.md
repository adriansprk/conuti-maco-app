# Wiederherstellung der Anschlussnutzung bei Lieferbeginn (Rolle MSB)

# Prozessübersicht

![LW24h mit Abhängigkeiten - Wiederherstellung Anschluss bei LB (MSB).png](https://api.apidog.com/api/v1/projects/816353/resources/352509/image-preview)

<Steps>
  <Step title="Prozessauslöser - eingehende EDI">
    <Tabs>
      <Tab title="Übersicht"> 
        <Card title="21040">
          Info Entsperrauftrag
        </Card>
      </Tab>        
      <Tab title="21040 Info Entsperrauftrag">
          <Accordion title="PI_21040" defaultOpen={false}>
                <DataSchema id="11310439" />
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
          <Card title="Erstellen Prozessdaten für Prüfi 21040"
                href="https://doc.macoapp.de/prozessdaten-erstellen-14669391e0.md">
              Übergabe der initialen Porzessdaten an das Backend
          </Card>
      </Tab>        
      <Tab title="21040 - Info Entsperrauftrag">
          <Accordion title="PI_21040" defaultOpen={false}>
                <DataSchema id="11310439" />
          </Accordion>
          
        </Tab> 
    </Tabs>
  </Step>
  <Step title="eingehende EDI">
    <Tabs>
      <Tab title="Übersicht"> 
        <Card title="21039">
          Auftragsstatus (Sperren)
        </Card>
      </Tab>        
      <Tab title="21039 Auftragsstatus (Sperren)">
          <Accordion title="PI_21039" defaultOpen={false}>
                <DataSchema id="11289126" />
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
          <Card title="Aktualisieren Prozessdaten für Prüfi 21039"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14669402e0.md">
              Übergabe der initialen Porzessdaten an das Backend
          </Card>
      </Tab>        
      <Tab title="21039 - Info Entsperrauftrag">
          <Accordion title="PI_21039" defaultOpen={false}>
                 <DataSchema id="11289126" />
          </Accordion>
          
        </Tab> 
    </Tabs>
  </Step>
</Steps>



