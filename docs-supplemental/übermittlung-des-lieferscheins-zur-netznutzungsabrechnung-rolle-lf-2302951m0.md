# Übermittlung des Lieferscheins zur Netznutzungsabrechnung (Rolle LF)


![image.png](https://api.apidog.com/api/v1/projects/816353/resources/381503/image-preview)


<Steps>
  <Step title="Prozessauslöser - eingehende EDI"> 
      
      <Tabs>
      <Tab title="Übersicht"> 
          
        <Card title="13016">
          Energiemenge u. Leistungsmax. (Strom)
        </Card>
             <Card title="13019">
          Energiemenge (Strom)
        </Card>
          
      </Tab>        
      <Tab title="13016">
          <Accordion title="PI_13016" defaultOpen={false}>
                  
<DataSchema id="13005924" />
          </Accordion>       
         
      </Tab>
          <Tab title="13019">
          <Accordion title="PI_13019" defaultOpen={false}>
    
<DataSchema id="12612264" />
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
          <Card title="Zähler lesen" 
                href="https://doc.macoapp.de/z%C3%A4hler-lesen-14017031e0.md">
              Lesen eines Zählers mittels LokationsId zu einem bestimmten Zeitpunkt
          </Card>
                      <Card title="Messlokation lesen" 
                href="https://doc.macoapp.de/messlokation-lesen-14017024e0.md">
              Lesen einer Messlokation mittels LokationsId zu einem bestimmten Zeitpunkt
          </Card>
        </CardGroup>
          
      </Tab>   
          
      <Tab title="📄Marktlokation">
          <Accordion title="Marktlokation" defaultOpen={false}>
                  <DataSchema id="5241973" />      
          </Accordion> 
         
          
      </Tab>
          
      <Tab title="📄Zähler">
          <Accordion title="Zähler" defaultOpen={false}>
                    
<DataSchema id="5241991" />
          </Accordion> 
        
      </Tab>    
               <Tab title="📄Messlokation">
          <Accordion title="Messlokation" defaultOpen={false}>
                    

<DataSchema id="5241975" />
          </Accordion> 
        
      </Tab> 
    </Tabs>
  </Step>
    
  <Step title="Prozessinitiierung Backend">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Erstellen Prozessdaten für Prüfi 13016 oder 13019"
                href="https://doc.macoapp.de/prozessdaten-erstellen-14017183e0.md">
              Übergabe der initialen Prozessdaten an das Backend
          </Card>
      </Tab>        
      <Tab title="13016 - Energiemenge u. Leistungsmax. (Strom)">
          <Accordion title="PI_13016" defaultOpen={false}>
                    
<DataSchema id="13005924" />
          </Accordion>
          
          
        </Tab> 
          <Tab title="13019 - Energiemenge (Strom)">
          <Accordion title="PI_13019" defaultOpen={false}>

<DataSchema id="12612264" />
          </Accordion>
          
          
        </Tab> 
    </Tabs>
  </Step>
  <Step title="Schnittstellen lesend für EBD-Prüfungen">
    <Tabs>
      <Tab title="Übersicht">
                    <Card title="Netznutzungsvertrag lesen" 
                href="https://doc.macoapp.de/netznutzungsvertrag-lesen-14017027e0.md">
              Lesen des Netznutzungsvertrag einer Lokation zu einem bestimmten Zeitpunkt
          </Card>
                    <Card title="Energiemengen lesen" 
                href="https://doc.macoapp.de/energiemengen-aus-abrechnungskontext-lesen-14017015e0.md">
              Lesen der Energiemengen einer Lokation zu einem bestimmten Zeitpunkt
          </Card>
      </Tab>        

      <Tab title="📄Netznutzungsvertrag lesen">
            <Accordion title="Vertrag" defaultOpen={false}>
                 <DataSchema id="5241988" />    
            </Accordion>
      </Tab>   
             <Tab title="📄Energiemengen lesen">
            <Accordion title="Vertrag" defaultOpen={false}>
           
<DataSchema id="5241967" />
            </Accordion>
      </Tab>  
    </Tabs>
  </Step>
  <Step title="Durchführung EBD">
          <Tabs>
                <Tab title="Übersicht">
          <Card title="Entscheidungsbaumdiagramm E_0456"
                href="https://doc.macoapp.de/816353m0.md">
             
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
      <Tab title="21035 - Rückmeld. a. Liefers.">
          <Accordion title="PI_21035" defaultOpen={false}>

<DataSchema id="8348225" />
          </Accordion>
      </Tab>
        <Tab title="29002 - Ablehnung IFTSTA">
          <Accordion title="PI_29002" defaultOpen={false}>

<DataSchema id="13005932" />
          </Accordion>
      </Tab>
                <Tab title="13006 - Messwert Storno">
          <Accordion title="PI_13006" defaultOpen={false}>


<DataSchema id="13005919" />
          </Accordion>
      </Tab>
           
    </Tabs>
  </Step>    
</Steps>
