# Prozessübersicht


<Frame caption="Kündigung (Lieferant alt)">
  ![](https://api.apidog.com/api/v1/projects/816353/resources/352449/image-preview)
</Frame>

<Steps>
  <Step title="Prozessauslöser - eingehende EDI"> 
      
      <Tabs>
      <Tab title="Übersicht"> 
          
        <Card title="55016">
          LFN an LFA - Kündigung.
        </Card>
          
      </Tab>        
      <Tab title="55016">
          <Accordion title="PI_55016" defaultOpen={false}>
                  <DataSchema id="5242365" />      
          </Accordion>       
         
      </Tab>
      </Tabs>
      
  </Step>
    
  <Step title="Schnittstellen lesend für APERAK">
      <Tabs>
      <Tab title="Übersicht">         
          
        <CardGroup cols={2}>
          <Card title="Marktlokation lesen"
                href="https://doc.macoapp.de/marktlokation-lesen-14017020e0.md">
              Lesen einer MaLo mittels LokationsId zu einem bestimmten Zeitpunkt
          </Card>
          <Card title="Tranche lesen" 
                href="https://doc.macoapp.de/tranche-lesen-14017030e0.md">
              Lesen einer Tranche mittels LokationsId zu einem bestimmten Zeitpunkt
          </Card>
        </CardGroup>
          
      </Tab>   
          
      <Tab title="📄Marktlokation">
          <Accordion title="Marktlokation" defaultOpen={false}>
                  <DataSchema id="5241973" />      
          </Accordion> 
         
          
      </Tab>
          
      <Tab title="📄Tranche">
          <Accordion title="Tranche" defaultOpen={false}>
                  <DataSchema id="5241987" />      
          </Accordion> 
        
      </Tab>    
          
    </Tabs>
  </Step>
    
  <Step title="Prozessinitiierung Backend">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Erstellen Prozessdaten für Prüfi 55016"
                href="https://doc.macoapp.de/prozessdaten-erstellen-14017183e0.md">
              Übergabe der initialen Prozessdaten an das Backend
          </Card>
      </Tab>        
      <Tab title="55016 - Kündigung zwischen Lieferanten">
          <Accordion title="PI_55016" defaultOpen={false}>
                  <DataSchema id="5242365" />    
          </Accordion>
          
          
        </Tab> 
    </Tabs>
  </Step>
  <Step title="Schnittstellen lesend für EBD-Prüfungen">
    <Tabs>
      <Tab title="Übersicht">
                    <Card title="Energieliefervertrag lesen" 
                href="https://doc.macoapp.de/energieliefervertrag-lesen-14017014e0.md">
              Lesen des Energieliefervertrages einer Lokation zu einem bestimmten Zeitpunkt
          </Card>
      </Tab>        

      <Tab title="📄Energieliefervertrag lesen">
            <Accordion title="Vertrag" defaultOpen={false}>
                 <DataSchema id="5241988" />    
            </Accordion>
      </Tab>        
    </Tabs>
  </Step>
  <Step title="Durchführung EBD">
          <Tabs>
                <Tab title="Übersicht">
          <Card title="Entscheidungsbaumdiagramm E_0614"
                href="https://doc.macoapp.de/lf_0614.md">
          </Card>    
      </Tab> 
      </Tabs>
    </Step>
  <Step title="Schnittstelle aktualisieren der Prozessdaten">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Aktualisieren der Prozessdaten"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14017182e0.md">
              Übergabe der erzeugten neg. (55018) oder pos. (55017) Rückmeldung an das Backend
          </Card>
      </Tab>        
      <Tab title="55017 - Bestätigung Kündigung">
          <Accordion title="PI_55017" defaultOpen={false}>
                 <DataSchema id="5242366" />    
          </Accordion>
      </Tab>
      <Tab title="55018 - Ablehnung Kündigung">
          <Accordion title="PI_55018" defaultOpen={false}>
                 <DataSchema id="5242367" /> 
          </Accordion>
        
      </Tab>        
    </Tabs>
  </Step>    
</Steps>
