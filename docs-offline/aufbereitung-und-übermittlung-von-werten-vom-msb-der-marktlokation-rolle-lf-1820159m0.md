# Aufbereitung und Übermittlung von Werten vom MSB der Marktlokation (Rolle LF)



![LW24h mit Abhängigkeiten - Aufbereitung und Übermittlung von Werten vom MSB der Marktlokation (Rolle LF)(1).png](https://api.apidog.com/api/v1/projects/816353/resources/367367/image-preview)

<Steps>
  <Step title="Prozessauslöser - eingehende EDI" defaultOpen={false}>
    <Tabs>
      <Tab title="Übersicht">
 
        <CardGroup cols={3}>
                      
          <Card title="13016">
              Übertragung von Energiemenge und Leistungsmaximum Strom
          </Card>
          <Card title="13017">
              Übertragung von Zählerständen Strom
          </Card>
            <Card title="13018">
              Übertragung von Lastgängen Strom
          </Card>
            <Card title="13019">
              Übertragung von Energiemengen Strom
            </Card>
            <Card title="13025">
              Übertragung von Lastgängen, Marktlokation, Tranche Strom
            </Card>
            
        </CardGroup>
      
      </Tab>   
      
      
      <Tab title="📄13016 Energiemengen und Leistungsmaximum">
          <Accordion title="PI_13016" defaultOpen={false}>
               <DataSchema id="12584850" />
          </Accordion>
      </Tab>
      <Tab title="📄13017 Zählerstand">
          <Accordion title="PI_13017" defaultOpen={false}>
               <DataSchema id="12586651" />
          </Accordion>
      </Tab>
      <Tab title="📄13018 Lastgang MeLo, NeLo, Netzkoppelpunkt">
          <Accordion title="PI_13018" defaultOpen={false}>
             
<DataSchema id="12595597" />
          </Accordion>
      </Tab>
      <Tab title="📄13019 Energiemengen">
          <Accordion title="PI_13019" defaultOpen={false}>
               <DataSchema id="12612264" />
          </Accordion>
      </Tab>
      <Tab title="📄13025 Lastgang MaLo, Tranche">
          <Accordion title="PI_13025" defaultOpen={false}>
                <DataSchema id="12615535" />
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
          <Card title="Messlokation lesen"
                href="https://doc.macoapp.de/messlokation-lesen-14017024e0.md">
                Lesen einer MeLo mittels LokationsId zu einem bestimmten Zeitpunkt
          </Card>  
          <Card title="Tranche lesen"
                href="https://doc.macoapp.de/tranche-lesen-14017030e0.md">
                Lesen einer Tranche mittels LokationsId zu einem bestimmten Zeitpunkt
          </Card>  
          <Card title="Netzlokation lesen"
                href="https://doc.macoapp.de/netzlokation-lesen-14017026e0.md">
                Lesen einer NeLo mittels LokationsId zu einem bestimmten Zeitpunkt
          </Card>  
          <Card title="Zähler lesen"
                href="https://doc.macoapp.de/z%C3%A4hler-lesen-14017031e0.md">
                Lesen eines Zählers mittels LokationsId zu einem bestimmten Zeitpunkt
          </Card>  
      </Tab>        
      <Tab title="📄Marktlokation ">
          <Accordion title="Marktlokation" defaultOpen={false}>
              <DataSchema id="5241973" />
          </Accordion>
          </Tab>
          <Tab title="📄Tranche ">
          <Accordion title="Tranche" defaultOpen={false}>
              <DataSchema id="5241987" />
          </Accordion>
          </Tab>
          <Tab title="📄Messlokation ">
          <Accordion title="Messlokation" defaultOpen={false}>
              <DataSchema id="5241975" />
          </Accordion>
          </Tab>
          <Tab title="📄Netzlokation ">
          <Accordion title="Netzlokation" defaultOpen={false}>
              <DataSchema id="5241976" />
          </Accordion>
          </Tab>
          <Tab title="📄Zähler ">
          <Accordion title="Zähler" defaultOpen={false}>
              <DataSchema id="5241991" />
          </Accordion>
          </Tab>
       </Tabs>
    </Step>
    
    <Step title="Schnittstellen schreibend">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Erstellen der Prozessdaten"
                href="https://doc.macoapp.de/prozessdaten-erstellen-14017183e0.md">
              Übergabe der initialen Prozessdaten an das Backend
          </Card>    
      </Tab>
       <Tab title="📄13016 Energiemengen und Leistungsmaximum">
          <Accordion title="PI_13016" defaultOpen={false}>
               
<DataSchema id="12584850" />
          </Accordion>
       </Tab>
       
        <Tab title="📄13017 Zählerständen Strom">
          <Accordion title="PI_13017" defaultOpen={false}>
                 <DataSchema id="12586651" />
          </Accordion>
       </Tab>
       
        
       <Tab title="📄13018 Lastgänge Strom">
          <Accordion title="PI_13018" defaultOpen={false}>
                 
<DataSchema id="12595597" />
          </Accordion>
       </Tab>
       
       
        <Tab title="📄13019 Energiemengen Strom">
          <Accordion title="PI_13019" defaultOpen={false}>
                  <DataSchema id="12612264" />
          </Accordion>
       </Tab>
       
        <Tab title="📄13025 Lastgang MaLo, Tranche">
          <Accordion title="PI_13025" defaultOpen={false}>
                 <DataSchema id="12615535" />
          </Accordion>
       </Tab>
        
  </Tabs>
</Step>
</Steps>
