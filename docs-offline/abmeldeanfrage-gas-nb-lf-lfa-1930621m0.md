# Abmeldeanfrage GAS NB->LF (LFA)





<Steps>
  <Step title="Prozessauslöser - eingehende EDI">
    <Tabs>
      <Tab title="Übersicht"> 
        <Card title="44010">
          Anfrage zur Beendigung der Zuordnung
        </Card>
      </Tab>        
      <Tab title="44010">
          <Accordion title="PI_44010" defaultOpen={false}>
                   <DataSchema id="8347899" />
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
          <Card title="Erstellen Prozessdaten für Prüfi 44010"
                href="https://doc.macoapp.de/prozessdaten-erstellen-14017183e0.md">
              Übergabe der initialen Prozessdaten an das Backend
          </Card>
      </Tab>        
      <Tab title="44010 - Anfrage zur Beendigung der Zuordnung">
          <Accordion title="PI_44010" defaultOpen={false}>
                  <DataSchema id="8347899" />
          </Accordion>
          
        </Tab> 
    </Tabs>
  </Step>
  <Step title="Schnittstellen lesend für EBD-Prüfungen">
    <Tabs>
      <Tab title="Übersicht">
          <CardGroup cols="2">
              <Card title="Energieliefervertrag lesen" 
                    href="https://doc.macoapp.de/energieliefervertrag-lesen-14017014e0.md">
              Lesen des Energieliefervertrages einer Lokation zu einem bestimmten Zeitpunkt
              </Card>
              <Card title="Netznutzungsvertrag lesen"
                    href="https://doc.macoapp.de/steuerbare-ressource-lesen-14017028e0.md">
                  Lesen des Netzunutzungsvertrages einer Lokation zu einem bestimmten Zeitpunkt
              </Card>
          </CardGroup>  
        </Tab>
        <Tab title="📄Energieliefervertrag lesen">
            <Accordion title="Vertrag" defaultOpen={false}>
                   <DataSchema id="5241988" />
            </Accordion>
       
            
      </Tab>
        <Tab title="📄Netznutzungsvertrag lesen">
            <Accordion title="Vertrag" defaultOpen={false}>
                   <DataSchema id="5241988" />
            </Accordion>
            
        </Tab>
    </Tabs>
  </Step>    
  <Step title="Durchführung EBD">
      <Tabs>
          <Tab title="Übersicht">
              <Card title="Entscheidungsbaumdiagramm E_0624"
                    href="https://doc.macoapp.de/ebd-e-0624-860873m0.md">
              </Card>
          </Tab>
      </Tabs>
    </Step>
    <Step title="Schnittstelle aktualisieren der Prozessdaten">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Aktualisieren der Prozessdaten"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14017182e0.md">
            Übergabe der erzeugten neg. (44012) oder pos. (44011) Rückmeldung an das Backend
          </Card>        
        </Tab>        
      <Tab title="44011 - Bestätigung Beendigung der Zuordnung">
            <Accordion title="PI_44011" defaultOpen={false}>
                 <DataSchema id="8347900" />
            </Accordion>
         
      </Tab>
      <Tab title="44012 - Ablehnung Beendigung der Zuordnung">
        <Accordion title="PI_44012" defaultOpen={false}>
                     <DataSchema id="8347901" />
         </Accordion>
      </Tab>
    </Tabs>
  </Step>
</Steps>
