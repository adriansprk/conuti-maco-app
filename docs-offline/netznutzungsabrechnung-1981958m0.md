# Netznutzungsabrechnung


![LW24h mit Abhängigkeiten - Netznutzungsabrechnung Strom (Rolle LF)(1).png](https://api.apidog.com/api/v1/projects/816353/resources/372796/image-preview)

<Steps>
  <Step title="Prozessauslöser - Eingehende EDI" defaultOpen={false}>
    <Tabs>
      <Tab title="Übersicht">
 
        <Card title="31001"
          >
            Abschlagsrechnung
        </Card>
                  <Card title="31002"
              >
NN-Rechnung
        </Card>

      </Tab>        
      <Tab title="📄31001">
          <Accordion title="31001 Abschlagsrechnung" defaultOpen={false}>
               
<DataSchema id="8348188" />
          </Accordion>

          
      </Tab>
        <Tab title="📄31002">
          <Accordion title="31002 NN-Rechnung" defaultOpen={false}>
               

<DataSchema id="8348189" />
          </Accordion>

          
      </Tab>
    </Tabs>

  </Step>
     <Step title="Event - START_VERSAND_ANTWORT_NNA" defaultOpen={false}>
    <Tabs>
      <Tab title="Übersicht">
 
        <Card title="START_VERSAND_ANTWORT_NNA"
          >
            Event START_VERSAND_ANTWORT_NNA
        </Card>

      </Tab>
              <Tab title="START_VERSAND_ANTWORT_NNA">
 
<Accordion title="START_VERSAND_ANTWORT_NNA" defaultOpen={false}>
                  
<DataSchema id="13241840" />
          </Accordion>

      </Tab>
    </Tabs>

  </Step>
        <Step title="Schnittstellen lesend">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Lesen der Marktlokationsdaten"
                href="https://doc.macoapp.de/marktlokation-lesen-14017020e0.md">
              LESEN_MARKTLOKATION_BASIS
          </Card>    
      </Tab>        

    </Tabs>
  </Step>
    <Step title="Schnittstellen schreibend">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Erstellen der Prozessdaten"
                href="https://doc.macoapp.de/prozessdaten-erstellen-14017183e0.md">
              Übergabe der eingehenden 31001 und 31002.
          </Card> 
            <Card title="Aktualisieren der Prozessdaten"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14017182e0.md">
              Übergabe der ausgehenden 33001, 33002, 33003, 33004.
                Übergabe der eingehenden 29001 und 31004.
          </Card> 
      </Tab>        
      <Tab title="📄31001 Abschlagsrechnung">
          <Accordion title="31001" defaultOpen={false}>
                  
<DataSchema id="8348188" />
          </Accordion>
          

           </Tab>
              <Tab title="📄31002 NN-Rechnung">
          <Accordion title="31002" defaultOpen={false}>
                  

<DataSchema id="8348189" />
          </Accordion>
          

           </Tab>
                      <Tab title="📄33001 Strom Bestätigung">
          <Accordion title="33001" defaultOpen={false}>
                  


<DataSchema id="8348110" />
          </Accordion>
          

           </Tab>
                              <Tab title="📄33003 Strom Abweisung Kopf und Summe">
          <Accordion title="33003" defaultOpen={false}>
                  


<DataSchema id="8348112" />
          </Accordion>
          

           </Tab>
                           <Tab title="📄33004 Strom Abweisung Position">
          <Accordion title="33004" defaultOpen={false}>
                  

<DataSchema id="8348113" />
          </Accordion>
          

           </Tab>
                                   <Tab title="📄29001 Strom Ablehnung REMADV">
          <Accordion title="29001" defaultOpen={false}>
    
<DataSchema id="13005931" />
          </Accordion>
          

           </Tab>
                                           <Tab title="📄31004 Storno NNA">
          <Accordion title="31004" defaultOpen={false}>
    

<DataSchema id="8348191" />
          </Accordion>
          

           </Tab>
        
                                                   <Tab title="📄33002 Abweisung">
          <Accordion title="33002" defaultOpen={false}>
    

<DataSchema id="8348111" />
          </Accordion>
          

           </Tab>
    </Tabs>
  </Step>
 
  </Steps>        
