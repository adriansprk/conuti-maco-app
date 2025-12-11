# Einrichtung der Konfigurationen aufgrund einer Zuordnung eines LF (MSB)

# Prozessübersicht

![LW24h mit Abhängigkeiten - Einrichtung Konf. wg. LB (MSB).png](https://api.apidog.com/api/v1/projects/816353/resources/367012/image-preview)

<Steps>
  <Step title="Prozessauslöser - eingehende EDI">
    <Tabs>
      <Tab title="Übersicht">         
          <Card title="21040">
              Info Entsperrauftrag
          </Card>
      </Tab> 
          <Tab title="📄21040 Info Entsperrauftrag">
          <Accordion title="PI_21040" defaultOpen={false}>
                  <DataSchema id="5733515" />
          </Accordion>
         </Tab>
      </Tabs>
  </Step> 

  <Step title="Schnittstellen lesend für APERAK">
      <Tabs>
      <Tab title="Übersicht">         
          
        <Card title="Marktlokation lesen"
                href="https://doc.macoapp.de/marktlokation-lesen-14017020e0.md">
              Lesen einer MaLo mittels LokationsId zu einem bestimmten Zeitpunkt
        </Card>
          <Card title="Messlokation lesen"
                href="https://doc.macoapp.de/messlokation-lesen-14017024e0.md">
              Lesen einer MeLo mittels LokationsId zu einem bestimmten Zeitpunkt
        </Card>
          <Card title="Netzlokation lesen"
                href="https://doc.macoapp.de/netzlokation-lesen-14017026e0.md">
              Lesen einer NeLo mittels LokationsId zu einem bestimmten Zeitpunkt
        </Card>
          
      </Tab>   
          
      <Tab title="📄Marktlokation">
          <Accordion title="Marktlokation" defaultOpen={false}>
                  <DataSchema id="5241973" />      
          </Accordion> 
      </Tab>
          <Tab title="📄Messlokation">
          <Accordion title="Messlokation" defaultOpen={false}>
                  <DataSchema id="5241975" />
          </Accordion> 
      </Tab>
          <Tab title="📄Netzlokation">
          <Accordion title="Netzlokation" defaultOpen={false}>
               <DataSchema id="5241976" />
          </Accordion> 
      </Tab>
    </Tabs>
  </Step>
    
<Step title="Prozessinitiierung Backend">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Erstellen Prozessdaten für Prüfi 17134 und 17135"
                href="https://doc.macoapp.de/prozessdaten-erstellen-14669391e0.md">
              Übergabe der initialen Prozessdaten an das Backend
          </Card>
      </Tab>        
      <Tab title="17134 - Einrichtung der Konfigurationen aufgrund einer Zuordnung eines LF von NB">
          <Accordion title="PI_17134" defaultOpen={false}>
                 <DataSchema id="5662876" />
          </Accordion>
       </Tab> 
       <Tab title="17135 - Einrichtung der Konfigurationen aufgrund einer Zuordnung eines LF von MSB">
          <Accordion title="PI_17135" defaultOpen={false}>
                 <DataSchema id="5718595" />
          </Accordion>
       </Tab>
    </Tabs>
  </Step> 

<Step title="Schnittstelle aktualisieren der Prozessdaten">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Aktualisieren der Prozessdaten"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14669402e0.md">
              Übergabe der empfangenen Rückmeldung an das Backend - 17135
          </Card>
      </Tab>   
          
      <Tab title="📄17135 - Einrichtung der Konfigurationen aufgrund einer Zuordnung eines LF von MSB">
          <Accordion title="PI_17135" defaultOpen={false}>
               <DataSchema id="5718595" />
          </Accordion> 
      </Tab>
      
    </Tabs>
 </Step>    
</Steps>
