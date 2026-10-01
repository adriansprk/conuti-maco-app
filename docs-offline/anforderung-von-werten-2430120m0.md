# Anforderung von Werten

# Prozessübersicht


![systembild_anforderung_werte_17004_1.png](https://api.apidog.com/api/v1/projects/816353/resources/383378/image-preview)

<Steps>
  <Step title="Prozessauslöser - Event" defaultOpen={false}>
    <Tabs>
      <Tab title="Übersicht">

        <Card title="START_ANFORDERUNG_VON_WERTEN"
              >
            Anforderung von Werten vom MSB der Marktlokation starten
      
        </Card>


      </Tab>
      <Tab title="📄START_ANFORDERUNG_VON_WERTEN">
          <Accordion title="[LF] START_ANFORDERUNG_VON_WERTEN" defaultOpen={false}>
                       <DataSchema id="17720725" />
          </Accordion>


      </Tab>
    </Tabs>

  </Step>
  <Step title="Schnittstellen schreibend">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Aktualisieren der Prozessdaten"
      href="https://doc.macoapp.de/prozessdaten-aktualiseren-14017182e0.md">
              Übergabe der eingehenden Antwortnachrichten des MSB an das Backend des Lieferanten.
          </Card>
      </Tab>
      <Tab title="📄17004 Anforderung von Werten">
          <Accordion title="PI_17004" defaultOpen={false}>
              
<DataSchema id="14434649" />
          </Accordion>


      </Tab>
      <Tab title="📄19007 Antwort auf Anforderung">
          <Accordion title="PI_19007" defaultOpen={false}>
             
<DataSchema id="13005863" />
          </Accordion>


      </Tab>
      <Tab title="📄13019 Übermittlung von Werten">
          <Accordion title="PI_13019" defaultOpen={false}>
                 
<DataSchema id="12612264" />
          </Accordion>


      </Tab>
      <Tab title="📄13025 Übermittlung von Werten">
          <Accordion title="PI_13025" defaultOpen={false}>
                 
<DataSchema id="12615535" />
          </Accordion>


      </Tab>
    </Tabs>
  </Step>
  <Step title="Folgeprozess">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Aufbereitung und Übermittlung von Werten vom MSB der Marktlokation"
              >
              Eingehende Nachrichten mit PI 13019 oder 13025 führen in den Folgeprozess. PI 19007 beendet den Prozess.
              [Aufbereitung und Übermittlung von Werten vom MSB der Marktlokation (Rolle LF)](https://doc.macoapp.de/aufbereitung-und-%C3%BCbermittlung-von-werten-vom-msb-der-marktlokation-rolle-lf-1820159m0.md)
           
          </Card>
      </Tab>
    </Tabs>
  </Step>
</Steps>

