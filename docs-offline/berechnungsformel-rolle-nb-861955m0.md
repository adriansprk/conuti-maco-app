# Berechnungsformel (Rolle NB)

# Prozessübersicht
<Columns>
    <Column className="bg-gray-100 p-3 rounded">
        <p className="text-center">
            Berechnungsformel an LF aus LB
        </p>
        ![LW24h mit Abhängigkeiten - Berechnungsformel an LF aus LB (NB).png](https://api.apidog.com/api/v1/projects/816353/resources/352497/image-preview)
    </Column>
    <Column className="bg-gray-100 p-3 rounded">
        <p class="text-center">
            Berechnungsformel vom NB an MSB
        </p>
![LW24h mit Abhängigkeiten - Berechnungsformel vom NB an MSB (NB).png](https://api.apidog.com/api/v1/projects/816353/resources/352498/image-preview)
    </Column>
</Columns>

<Steps>
  <Step title="Prozessauslöser - Event an LF" defaultOpen={false}>
    <Tabs>
      <Tab title="Übersicht">
 
        <Card title="START_UEBERMITTLUNG_BERECHNUNGSFORMEL"
              href="https://doc.macoapp.de/%C3%BCbermittlung-der-berechnungsformel-15090201e0.md">
            Versand der Berechnungsformel nach Abschluss des Lieferbeginn an den Lieferant oder als Einzelevent an den Messstellenbetreiber
        </Card>

      </Tab>        
      <Tab title="📄START_UEBERMITTLUNG_BERECHNUNGSFORMEL">
          <Accordion title="START_BERECHNUNGSFORMEL" defaultOpen={false}>
                    <DataSchema id="5652589" />
          </Accordion>
       </Tab>
      <Tab title="📄25001 Berechnungsformel">
          <Accordion title="PI_25001" defaultOpen={false}>
               <DataSchema id="5718597" />
          </Accordion>
      </Tab>
    </Tabs>

  </Step>
</Steps>

<Steps>
  <Step title="Prozessauslöser - Event an MSB" defaultOpen={false}>
    <Tabs>
      <Tab title="Übersicht">
 
        <Card title="START_UEBERMITTLUNG_BERECHNUNGSFORMEL"
              href="https://doc.macoapp.de/%C3%BCbermittlung-der-berechnungsformel-15090201e0.md">
            Versand der Berechnungsformel nach Abschluss des Lieferbeginn an den Lieferant oder als Einzelevent an den Messstellenbetreiber
        </Card>

      </Tab>        
      <Tab title="📄START_BERECHNUNGSFORMEL">
          <Accordion title="START_BERECHNUNGSFORMEL" defaultOpen={false}>
                    <DataSchema id="5652589" />
          </Accordion>
       </Tab>
      <Tab title="📄Berechnungsformel">
          <Accordion title="PI_25001" defaultOpen={false}>
               <DataSchema id="5718597" />
          </Accordion>
      </Tab>
    </Tabs>

  </Step>
  <Step title="Schnittstelle aktualisieren der Prozessdaten">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Aktualisieren der Prozessdaten"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14666382e0.md">
              Übergabe der empfangenen Antwort (25010) an das Backend
          </Card>
      </Tab>        
      <Tab title="25010 Antwort auf Berechnungsformel">
          <Accordion title="PI_25010" defaultOpen={false}>
              <DataSchema id="5718598" />
          </Accordion>
          
      </Tab>
    </Tabs>
  </Step>

</Steps>
