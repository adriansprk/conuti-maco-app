# GAS Anfrage zur Stammdatenänderung von Netzbetreiber (Rolle NB)


![LW24h mit Abhängigkeiten - GAS Anfrage zur Stammdatenänderung von Netzbetreiber (Rolle NB).png](https://api.apidog.com/api/v1/projects/816353/resources/372949/image-preview)

<Steps>
  <Step title="Prozessauslöser - Event" defaultOpen={false}>
    <Tabs>
      <Tab title="Übersicht">
 <Card title="START_ANFRAGE_STAMMDATENAENDERUNG"
             >
            START_ANFRAGE_STAMMDATENAENDERUNG
        </Card>
          
        <Card title="44113"
             >
            Nicht bila.rel. Änderung vom NB
        </Card>
          <Card title="44137"
             >
            Nicht Bila. rel. Anfrage an LF
        </Card>
                <Card title="44150"
             >
            Bila.-rel. Anfrage an LF
        </Card>


      </Tab>   
        <Tab title="📄Event ">
          <Accordion title="START_ANFRAGE_STAMMDATENAENDERUNG" defaultOpen={false}>
                

<DataSchema id="13241832" />
          </Accordion>
          
      </Tab>
     
        <Tab title="📄44113 Nicht bila.rel. Änderung vom NB">
          <Accordion title="44113" defaultOpen={false}>
                
<DataSchema id="13005679" />
          </Accordion>
          
      </Tab>
                <Tab title="📄44137 Nicht Bila. rel. Anfrage an LF">
          <Accordion title="44137" defaultOpen={false}>

<DataSchema id="13005688" />
          </Accordion>
          
      </Tab>
                        <Tab title="📄44150 Bila.-rel. Anfrage an LF">
          <Accordion title="44150" defaultOpen={false}>

<DataSchema id="13005699" />
          </Accordion>
          
      </Tab>
    </Tabs>

  </Step>
 
  <Step title="Schnittstelle aktualisieren der Prozessdaten">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Aktualisieren der Prozessdaten"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14017182e0.md">
              ausgehende Nachrichten 44113, 44137, 44150
              eingehende Nachrichten 44115, 44138, 44151, 44152
          </Card>
      </Tab>        
      <Tab title="44115 - Antwort auf Änderung vom NB">
          <Accordion title="44115" defaultOpen={false}>
                 
<DataSchema id="13005680" />
          </Accordion>
      </Tab>
      <Tab title="44138 - Antwort auf Anfrage">
          <Accordion title="44138" defaultOpen={false}>
           
<DataSchema id="13005689" />
          </Accordion>
        
      </Tab>    
      <Tab title="44151 - Antwort auf Anfrage">
          <Accordion title="44151" defaultOpen={false}>
                
<DataSchema id="13005700" />
          </Accordion>
        
      </Tab>    
              <Tab title="44152 - Ablehnung der Anfrage">
          <Accordion title="44152" defaultOpen={false}>

<DataSchema id="13005701" />
          </Accordion>
        
      </Tab>    
    </Tabs>
  </Step>  
</Steps>



