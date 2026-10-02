# Bestellung einer Konfiguration vom NB oder LF an MSB ( Rolle MSB )


![LW24h mit Abhängigkeiten - Bestellung einer Konfiguration vom NB oder LF an MSB ( Rolle MSB )(1).png](https://api.apidog.com/api/v1/projects/816353/resources/372947/image-preview)


<Steps>
  <Step title="Prozessauslöser - eingehende EDI">
    <Tabs>
      <Tab title="Übersicht">         
          <Card title="35004">
              Anfrage einer Konfiguration
          </Card>
      </Tab> 
          <Tab title="📄35004">
          <Accordion title="PI_35004" defaultOpen={false}>
         
<DataSchema id="8348109" />
          </Accordion>
         </Tab>
      </Tabs>
  </Step>
    
      <Step title="weitere eingehende Nachrichten">
      <Tabs>
      <Tab title="Übersicht">         
       <Card title="17131">
              Bestellung Angebot einer Konfiguration
          </Card>
          <Card title="17130">
Bestellung einer Konfiguration
          </Card>
                    <Card title="17121">
Bestellung Änderung
           </Card>
          
      </Tab>
            <Tab title="📄17131">
          <Accordion title="17131" defaultOpen={false}>
         

<DataSchema id="13005913" />
          </Accordion>
         </Tab>
                      <Tab title="📄17130">
          <Accordion title="17130" defaultOpen={false}>
  
<DataSchema id="13005912" />
          </Accordion>
         </Tab>
                              <Tab title="📄17121">
          <Accordion title="17121" defaultOpen={false}>

<DataSchema id="13005906" />
          </Accordion>
         </Tab>
          
    </Tabs>
  </Step>
        
  <Step title="Schnittstellen lesend">
      <Tabs>
      <Tab title="Übersicht">         
          
        <CardGroup cols={2}>
          <Card title="Marktlokation lesen"
                href="https://doc.macoapp.de/marktlokation-lesen-14017020e0.md">
              Lesen einer MeLo mittels LokationsId zu einem bestimmten Zeitpunkt
          </Card>
          <Card title="Messlokation lesen"
                href="https://doc.macoapp.de/messlokation-lesen-14017024e0.md">
              Lesen einer MeLo mittels LokationsId zu einem bestimmten Zeitpunkt
          </Card>
                      <Card title="Netzlokation lesen"
                href="https://doc.macoapp.de/netzlokation-lesen-14017026e0.md">
              Lesen einer MeLo mittels LokationsId zu einem bestimmten Zeitpunkt
          </Card>
                                  <Card title="Steuerbare Ressource lesen"
                href="https://doc.macoapp.de/steuerbare-ressource-lesen-14017028e0.md">
              Lesen einer MeLo mittels LokationsId zu einem bestimmten Zeitpunkt
          </Card>
        </CardGroup>
          
      </Tab>     
          <Tab title="📄Marktlokation">
          <Accordion title="Marktlokation" defaultOpen={false}>
                 
<DataSchema id="5241973" />
          </Accordion> 
        
          
      </Tab>
          
      <Tab title="📄Messlokation">
          <Accordion title="Messlokation" defaultOpen={false}>
                  <DataSchema id="5241973" />      
          </Accordion> 
        
          
      </Tab>
          
      <Tab title="📄Netzlokation">
          <Accordion title="Netzlokation" defaultOpen={false}>
                     
<DataSchema id="5241976" />
          </Accordion> 
        
      </Tab>    
                <Tab title="📄Steuerbare Ressource">
          <Accordion title="Steuerbare Ressource" defaultOpen={false}>

<DataSchema id="5241984" />
          </Accordion> 
        
      </Tab>  
          
    </Tabs>
  </Step>
        
       <Step title="Schnittstellen schreibend">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Erstellen der Prozessdaten"
                href="https://doc.macoapp.de/prozessdaten-erstellen-14017183e0.md">
              Übergabe der eingehenden 35004.
          </Card> 
            <Card title="Aktualisieren der Prozessdaten"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14017182e0.md">
              Übergabe der ausgehenden 15004, 21033, 19132, 19120, 17130, 17118, 21043.
                Übergabe der eingehenden 17131, 17130, 17121, 19132, 19127.
          </Card> 
      </Tab>        
      <Tab title="📄15004 Angebot einer Konfiguration">
          <Accordion title="15004" defaultOpen={false}>

<DataSchema id="10270802" />
          </Accordion>
          
           </Tab>
              <Tab title="📄21033 Ablehnung der Anfrage">
          <Accordion title="21033" defaultOpen={false}>

<DataSchema id="8348224" />
          </Accordion>
          
           </Tab>
     <Tab title="📄17131 Bestellung Angebot einer Konfiguration">
          <Accordion title="17131" defaultOpen={false}>

<DataSchema id="13005913" />
          </Accordion>
        
           </Tab>
           <Tab title="📄17130 Bestellung einer Konfiguration">
          <Accordion title="17130" defaultOpen={false}>
 
<DataSchema id="13005912" />
          </Accordion>
          
           </Tab>
            <Tab title="📄17121 Bestellung Änderung">
          <Accordion title="17121" defaultOpen={false}>

<DataSchema id="13005906" />
          </Accordion>
        
           </Tab>
           <Tab title="📄19132 Mitteilung zur Bestellung Konfiguration">
          <Accordion title="19132" defaultOpen={false}>

<DataSchema id="10222259" />
          </Accordion>
          

           </Tab>
            <Tab title="📄19120 Mitteilung zur Änderung">
          <Accordion title="19120" defaultOpen={false}>

          </Accordion>
          

           </Tab>
         <Tab title="📄17118 Bestellung einer Konfigurationsänderung">
          <Accordion title="17118" defaultOpen={false}>
    
<DataSchema id="13005904" />
          </Accordion>
                     </Tab>
                 <Tab title="📄19127 Mitteilung zur Konfigurationsänderung">
          <Accordion title="19127" defaultOpen={false}>

          </Accordion>
                     </Tab>
                         <Tab title="📄21043 Bestellungsantwort / -mitteilung">
          <Accordion title="21043" defaultOpen={false}>

<DataSchema id="8348229" />
          </Accordion>
                     </Tab>
    </Tabs>
  </Step>
</Steps>

