# Bestellung einer Konfiguration vom LF an NB ( LF )


![LW24h mit Abhängigkeiten - Bestellung einer Konfiguration vom LF an NB ( LF ).png](https://api.apidog.com/api/v1/projects/816353/resources/368835/image-preview)

<Steps>
  <Step title="Prozessauslöser - Event">
   <Tabs>
      <Tab title="Übersicht">
 
        <Card title="START_BESTELLUNG_ZAEHLZEITDEFINITION oder 
START_BESTELLUNG_AEND_PROGNOSEGRUNDLAGE"
              href="https://doc.macoapp.de/lieferende-von-lieferant-an-netzbetreiber-14992421e0.md">
            Lieferende starten
        </Card>

      </Tab>        
      <Tab title="📄START_BESTELLUNG_AEND_PROGNOSEGRUNDLAGE">
          <Accordion title="PI_17120" defaultOpen={false}>            <DataSchema id="13005905" /> 
          </Accordion>   
      </Tab>
             <Tab title="📄START_BESTELLUNG_ZAEHLZEITDEFINITION">
          <Accordion title="PI_17123" defaultOpen={false}>            <DataSchema id="10711148" /> 
          </Accordion>   
      </Tab>
    </Tabs>
  </Step>
  <Step title="Schnittstellen schreibend">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Aktualisieren der Prozessdaten"
                href="https://doc.macoapp.de/prozessdaten-erstellen-14017183e0.md">
              Übergabe der Nachrichten (19121,19124,21043) an das Backend.
          </Card>    
      </Tab>
        <Tab title="📄19121 Mitteilung zur Änderung
Prognosegrundlage">
            <Accordion title="PI_19121" defaultOpen={false}>
             
<DataSchema id="13005881" />
            </Accordion>
        </Tab>
       <Tab title="📄19124 Mitteilung zur Änderung
Zählzeitdefinition">
            <Accordion title="PI_19124" defaultOpen={false}>
                
<DataSchema id="10709668" />
            </Accordion>
       </Tab>
       <Tab title="📄21043 Bestellungsantwort / -mitteilung ">
            <Accordion title="PI_21043" defaultOpen={false}>
               <DataSchema id="8348229" />
            </Accordion>
       </Tab>
    </Tabs>
  </Step>
</Steps>



