# Überprüfung einer EEG-Marktlokation mit DV-Pflicht auf 100% LF-Zuordnung ( Rolle NB VNB )

Überprüfung einer EEG-Marktlokation mit DV-Pflicht auf 100% LF-Zuordnung ( Rolle NB VNB )

![LW24h mit Abhängigkeiten - Überprüfung einer EEG-Marktlokation mit DV-Pflicht auf 100_ LF-Zuordnung ( Rolle NB VNB ).png](https://api.apidog.com/api/v1/projects/816353/resources/364110/image-preview)

<Steps>
  <Step title="Prozessauslöser - Event" defaultOpen={false}>
    <Tabs>
      <Tab title="Übersicht">
 
        <Card title="START_ZUORDNUNG_ERZ_MALO_TRANCHE"
              href="https://doc.macoapp.de/%C3%BCberpr%C3%BCfung-einner-eeg-marklokation-mit-dv-pflicht-auf-100-lf-zuordnung-rolle-nb-25151089e0.md">
            Anfrage nach Stornierung starten
        </Card>

      </Tab>        
      <Tab title="📄START_ZUORDNUNG_ERZ_MALO_TRANCHE">
          <Accordion title="[NB|LF|MSB] START_VERSAND_ANF_STORNO" defaultOpen={false}>
                   <DataSchema id="11408604" />
          </Accordion>
      </Tab>
      <Tab title="📄55607 Ankündigung Zuordnung / Zuordnung des LF zur erz. MaLo/ Tranche">
          <Accordion title="PI_55607" defaultOpen={false}>
               <DataSchema id="5242421" />
          </Accordion>
      </Tab>
    </Tabs>

  </Step>
  <Step title="Schnittstellen schreibend">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Aktualisieren der Prozessdaten"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14017182e0.md">
              Übergabe der initialen Prozessdaten an das Backend - 21039
          </Card>    
      </Tab>
       <Tab title="📄21039 Auftragsstatus">
          <Accordion title="PI_21039" defaultOpen={false}>
                 <DataSchema id="11289126" />
          </Accordion>
       </Tab>
      
    </Tabs>
  </Step>
  
  
</Steps>


