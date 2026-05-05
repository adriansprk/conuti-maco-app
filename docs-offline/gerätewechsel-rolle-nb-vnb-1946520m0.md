# Gerätewechsel ( Rolle NB VNB )


![LW24h mit Abhängigkeiten - Gerätewechsel GAS ( Rolle NB VNB ).png](https://api.apidog.com/api/v1/projects/816353/resources/370912/image-preview)


<Steps>
  <Step title="Prozessauslöser - eingehende EDI" defaultOpen={false}>
    <Tabs>
      <Tab title="Übersicht">
 
        <Card title="13008 Lastgang (Gas)" defaultOpen={false}>          
            <Accordion title="PI_13008" defaultOpen={false}>
            
<DataSchema id="8348179" />
          </Accordion>
          </Card>
           <Card title="13009 Energiemenge (Gas)" defaultOpen={false}>          
            <Accordion title="PI_13009" defaultOpen={false}>
            
<DataSchema id="8348180" />
          </Accordion>
          </Card>
           <Card title="13002 Zählerstand (Gas)" defaultOpen={false}>          
            <Accordion title="PI_13002" defaultOpen={false}>
            
<DataSchema id="8348176" />
          </Accordion>
          </Card>
            <Card title="13007 Gasbeschaffenheit (Gas)" defaultOpen={false}>          
            <Accordion title="PI_13007" defaultOpen={false}>

<DataSchema id="8348178" />
          </Accordion>
          </Card>
           <Card title="13006 Messwert Storno" defaultOpen={false}>          
            <Accordion title="PI_13006" defaultOpen={false}>

<DataSchema id="8348177" />
          </Accordion>
          </Card>

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
          <Card title="Aktualiseren der Prozessdaten"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14017182e0.md">
              Aktualisieren der Prozessdaten anhand des BusinessKey.
          </Card>    
      </Tab>

       <Tab title="📄13008 Lastgang (Gas)">
          <Accordion title="PI_13008" defaultOpen={false}>
                
<DataSchema id="8348179" />
          </Accordion>
       </Tab>
        
        <Tab title="📄13002 Edi">
          <Accordion title="PI_13002" defaultOpen={false}>

<DataSchema id="8348176" />
       </Accordion>
            </Tab>
         <Tab title="📄13007 Edi">
          <Accordion title="PI_13007" defaultOpen={false}>

<DataSchema id="8348178" />
       </Accordion>
            </Tab>
         <Tab title="📄13009 Edi">
          <Accordion title="PI_13009" defaultOpen={false}>

<DataSchema id="8348180" />
       </Accordion>
            </Tab>
                 <Tab title="📄13006 Edi">
          <Accordion title="PI_13006" defaultOpen={false}>

<DataSchema id="8348177" />
       </Accordion>
            </Tab>
     
    </Tabs>
  </Step>
  
</Steps>

