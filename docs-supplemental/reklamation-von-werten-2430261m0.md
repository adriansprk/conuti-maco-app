# Reklamation von Werten

# Prozessübersicht

![systembild_reklamation_werte_17133.png](https://api.apidog.com/api/v1/projects/816353/resources/383379/image-preview)

<Steps>
  <Step title="Prozessauslöser - Event" defaultOpen={false}>
    <Tabs>
      <Tab title="Übersicht">

        <Card title="START_REKLAMATION_VON_WERTEN"
              href="apidog://link/endpoint/PLATZHALTER_ENDPOINT">
            Reklamation von Werten vom MSB der Messlokation starten
        </Card>

      </Tab>
      <Tab title="📄START_REKLAMATION_VON_WERTEN">
          <Accordion title="[LF] START_REKLAMATION_VON_WERTEN" defaultOpen={false}>
                 

<DataSchema id="17726618" />
          </Accordion>


      </Tab>
    </Tabs>

  </Step>
  <Step title="Schnittstellen schreibend">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Aktualisieren der Prozessdaten"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14017182e0.md" >
              Übergabe der Ablehnung bzw. der übermittelten Werte des MSB an das Backend des Lieferanten.
          </Card>
      </Tab>
      <Tab title="📄17133 Reklamation von Werten">
          <Accordion title="PI_17133" defaultOpen={false}>
                 
<DataSchema id="13005900" />
          </Accordion>


      </Tab>
      <Tab title="📄19114 Ablehnung">
          <Accordion title="PI_19114" defaultOpen={false}>
           
<DataSchema id="13005876" />
          </Accordion>


      </Tab>
      <Tab title="📄13016 Übermittlung von Werten">
          <Accordion title="PI_13016" defaultOpen={false}>
                
<DataSchema id="12584850" />
          </Accordion>


      </Tab>
      <Tab title="📄13017 Übermittlung von Werten">
          <Accordion title="PI_13017" defaultOpen={false}>
                
<DataSchema id="12586651" />
          </Accordion>


      </Tab>
      <Tab title="📄13018 Übermittlung von Werten">
          <Accordion title="PI_13018" defaultOpen={false}>
               
<DataSchema id="12595597" />
          </Accordion>


      </Tab>
      <Tab title="📄13019 Übermittlung von Werten">
          <Accordion title="PI_13019" defaultOpen={false}>
                
<DataSchema id="12612264" />
          </Accordion>


      </Tab>
      <Tab title="📄13025 Übermittlung von Werten">
          <Accordion title="PI_13025" defaultOpen={false}>
         
<DataSchema id="12612264" />
          </Accordion>


      </Tab>
    </Tabs>
  </Step>
  <Step title="Optionaler Folgeprozess">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Aufbereitung und Übermittlung von Werten vom MSB der Messlokation"
                >
              Eingehende Nachrichten mit PI 13016, 13017, 13018, 13019 oder 13025 führen optional in den Folgeprozess. PI 19114 lehnt die Reklamation ab und beendet den Prozess.
          </Card>
      </Tab>
    </Tabs>
  </Step>
</Steps>



