# Mehr-/Mindermengenabrechnung zwischen NB und LF ( Rolle LF )


![LW24h mit Abhängigkeiten - Mehr-_Mindermengenabrechnung zwischen NB und LF ( Rolle LF ).png](https://api.apidog.com/api/v1/projects/816353/resources/375813/image-preview)


<Steps>
  <Step title="Prozessauslöser - Eingehende EDI" defaultOpen={false}>
    <Tabs>
      <Tab title="Übersicht">
 
        <Card title="13014"
          >
            Marktlokationsscharfe bilanzierte
Menge Strom/Gas (MMMA)
        </Card>
                  <Card title="31005"
          >
            MMM-Rechnung
        </Card>
                            <Card title="31006"
          >
            MMM-selbst ausgest. Rechnung
        </Card>
                  <Card title="31004"
          >
            Stornorechnung
        </Card>
      </Tab>      
         <Tab title="📄13014">
          <Accordion title="13014 Marktlokationsscharfe bilanzierte
Menge Strom/Gas (MMMA)" defaultOpen={false}>
               

<DataSchema id="14576986" />
          </Accordion>

          
      </Tab>
      <Tab title="📄31005">
          <Accordion title="31005 MMM-Rechnung" defaultOpen={false}>
               

<DataSchema id="8348192" />
          </Accordion>

          
      </Tab>
             <Tab title="📄31006">
          <Accordion title="31006 MMM-selbst ausgest. Rechnung" defaultOpen={false}>
               

<DataSchema id="8348193" />
          </Accordion>

          
      </Tab>
          <Tab title="📄31004">
          <Accordion title="31004 Stornorechnung" defaultOpen={false}>
               

<DataSchema id="8348191" />
          </Accordion>

          
      </Tab>
    </Tabs>

  </Step>
    
     <Step title="ausgehende Edis" defaultOpen={false}>
    <Tabs>
      <Tab title="Übersicht">
 
        <Card title="33001"
          >
            Bestätigung
        </Card>
                  <Card title="33002"
          >
            Abweisung
        </Card>
      </Tab>        
      <Tab title="📄33001">
          <Accordion title="33001 Bestätigung" defaultOpen={false}>
               

<DataSchema id="8348110" />
          </Accordion>

          
      </Tab>
             <Tab title="📄33002">
          <Accordion title="33002 Abweisung" defaultOpen={false}>
               

<DataSchema id="8348111" />
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
          <Card title="Lesen des Energieliefervertrags"
                href="https://doc.macoapp.de/energieliefervertrag-lesen-14017014e0.md">
              LESEN_ENERGIELIEFERVERTRAG_BASIS
          </Card>  
                    <Card title="Lesen der Energiemengen"
                href="https://doc.macoapp.de/energiemengen-aus-abrechnungskontext-lesen-14017015e0.md">
              LESEN_ENERGIEMENGE_ENERGIEMENGE
          </Card>  
                              <Card title="Lesen der Rechnungen"
                >
              LESEN_RECHNUNG_BASIS
          </Card> 
                              <Card title="Lesen der Bilanzierung"
                href="https://doc.macoapp.de/bilanzierung-lesen-14017013e0.md">
              LESEN_BILANZIERUNG_BASIS
          </Card>  
      </Tab>        

    </Tabs>
  </Step>
    <Step title="Schnittstellen schreibend">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Erstellen der Prozessdaten"
                href="https://doc.macoapp.de/prozessdaten-erstellen-14017183e0.md">
              Übergabe der eingehenden 13014, 31005, 31006.
          </Card> 
            <Card title="Aktualisieren der Prozessdaten"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14017182e0.md">
              Übergabe der ausgehenden 33001, 33002.
                Übergabe der eingehenden 31004.
          </Card> 
      </Tab>        
      
    </Tabs>
  </Step>
 
  </Steps>        
