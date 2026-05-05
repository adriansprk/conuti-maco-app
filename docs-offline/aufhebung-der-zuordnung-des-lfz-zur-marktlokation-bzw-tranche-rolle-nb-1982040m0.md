# Aufhebung der Zuordnung des LFZ zur Marktlokation bzw. Tranche (Rolle NB)

# Prozessübersicht


![LW24h mit Abhängigkeiten - GAS Aufhebung Zuordnung LFZ (NB).png](https://api.apidog.com/api/v1/projects/816353/resources/372790/image-preview)
<Steps>
  <Step title="Prozessauslöser - Event" defaultOpen={false}>
    <Tabs>
      <Tab title="Übersicht">
 
        <Card title="START_AUFH_ZUK_ZUORDNUNG"
              href="https://doc.macoapp.de/aufhebung-der-zuordnung-des-lfz-zur-marklokation-bzw-tranche-versenden-14333135e0.md">
            Versand von Aufhebung der Zuordnung des LFZ zur Marklokation an Marktpartner durch die MACO APP
        </Card>

      </Tab>        
      <Tab title="📄START_AUFH_ZUK_ZUORDNUNG">
          <Accordion title="Aufhebung der Zuordnung des LFZ zur Marklokation" defaultOpen={false}>
                    <DataSchema id="5242224" />
          </Accordion>
      </Tab>
      <Tab title="📄Aufhebung einer zuk. Zuordnung">
          <Accordion title="PI_44038" defaultOpen={false}>
               <DataSchema id="13005674" />
          </Accordion>
      </Tab>
    </Tabs>

  </Step>
<Step title="Schnittstelle aktualisieren der Prozessdaten">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Aktualisieren der Prozessdaten"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14017182e0.md">
              Übergabe der erzeugten 44038 Rückmeldung an das Backend
          </Card>
      </Tab>        
      
      <Tab title="44038 - Informationsmeldung zur Aufhebung
einer zuk. Zuordnung">
          <Accordion title="PI_44038" defaultOpen={false}>
                 <DataSchema id="13005674" />
          </Accordion>
        
      </Tab>      
    </Tabs>
  </Step>  
</Steps>



