# Beginn Messstellenbetrieb ( Rolle NB VNB )


![LW24h mit Abhängigkeiten - STROM-Beginn Messstellenbetrieb ( Rolle NB VNB ).png](https://api.apidog.com/api/v1/projects/816353/resources/377811/image-preview)

<Steps>

  <Step title="Prozessauslöser - eingehende EDI">
    <Tabs>
      <Tab title="Übersicht">         
        <CardGroup cols={2}>
          <Card title="55042">
              Anmeldung Messstellenbetrieb MSBN an NB
          </Card>
        </CardGroup>
      </Tab>
      <Tab title="📄55042">
          <Accordion title="PI_55042" defaultOpen={false}>
                

<DataSchema id="5242378" />
          </Accordion> 
      </Tab>
    </Tabs>    
  </Step>

  <Step title="Prozessinitiierung Backend">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Erstellen Prozessdaten für Prüfi 55042"
                href="https://doc.macoapp.de/prozessdaten-erstellen-14666311e0.md">
              Übergabe der initialen Prozessdaten an das Backend
          </Card>
      </Tab>   
      <Tab title="📄55042">
          <Accordion title="PI_55042" defaultOpen={false}>
                <DataSchema id="5242378" />
          </Accordion> 
      </Tab>
    </Tabs>
  </Step>

  <Step title="Schnittstellen lesend für EBD-Prüfungen">
    <Tabs>
      <Tab title="Übersicht">         
        <CardGroup cols={3}>
          <Card title="Marktlokation lesen"
                href="https://doc.macoapp.de/marktlokation-lesen-14017020e0.md">
              LESEN_MARKTLOKATION_BASIS
          </Card>
          <Card title="Messlokation lesen" 
                href="https://doc.macoapp.de/messlokation-lesen-14017024e0.md">
              LESEN_MESSLOKATION_BASIS
          </Card>
          <Card title="Messstellenbetriebsvertrag lesen" 
                href="https://doc.macoapp.de/messstellenbetriebsvertrag-lesen-14017025e0.md">
              LESEN_MESSSTELLENBETRIEBSVERTRAG_BASIS
          </Card>
        </CardGroup>
      </Tab>
      <Tab title="📄Marktlokation">
          <Accordion title="Marktlokation" defaultOpen={false}>
               
<DataSchema id="5241973" />
          </Accordion> 
      </Tab>
      <Tab title="📄Messlokation">
          <Accordion title="Messlokation" defaultOpen={false}>
                
<DataSchema id="5241975" />
          </Accordion> 
      </Tab> 
      <Tab title="📄Messstellenbetriebsvertrag">
          <Accordion title="Messstellenbetriebsvertrag" defaultOpen={false}>
                
          </Accordion> 
      </Tab>
    </Tabs> 
  </Step>

  <Step title="EBD-Prüfung">
    <Tabs>
      <Tab title="Übersicht">
        <CardGroup cols={2}>
          <Card title="E_0201">
              Anmeldung Messstellenbetrieb prüfen
Zugehörige Codelisten S_0055 & S_0056
          </Card>
        
        </CardGroup>
      </Tab>
      <Tab title="✅ S_0055">
        <Accordion title="S_0055 - Bestätigung Anmeldung MSB
" defaultOpen={true}>
          | Code | Antwortgrund |
    |---|---|
    | E15 | **Zustimmung ohne Korrekturen** — Der Absender stimmt der Meldung und den Inhalten des Vorgangs voll zu. Er hat keine Änderungen an den gesendeten Daten vorgenommen. Er kann allerdings Daten gemäß seiner Aufgabe im Prozess vervollständigt haben (z. B. der NB bei einer Anmeldung mit dem Standardlastprofil). In diesen Fällen ist Z44 nicht zu verwenden. |
    | Z01 | **Zustimmung mit Terminänderung** — Der Absender stimmt der Meldung zu einem abweichenden Termin zu. Mit dieser Kennzeichnung übermittelt der Absender dem Sender der ursprünglichen Meldung, dass diese abgelehnt wurde (Ablehnung zum alten Termin), jedoch eine Zustimmung zu einem abweichenden Termin erfolgte. |
    | Z44 | **Zustimmung mit Korrektur von nicht bilanzierungsrel. Daten** — Die Zustimmung erfolgt mit Korrektur von nicht bilanzierungsrelevanten Daten in der Antwortnachricht. Die Bilanzierungsrelevanz leitet sich aus der Übersicht der Änderungsmeldungen ab. |
    
          
        </Accordion>
      </Tab>
      <Tab title="❌ S_0056">
        <Accordion title="S_0056 - Ablehnung Anmeldung MSB" defaultOpen={true}>
          | Code | Antwortgrund |
    |---|---|
    | E11 | **Ablehnung (Messproblem)** — Der Absender lehnt die Transaktion ab. Der Marktpartner fordert ein Messverfahren, was in diesem Fall nicht möglich ist bzw. nicht mit dem Leistungsumfang vereinbar ist. |
    | E17 | **Ablehnung wg. Fristüberschreitung** — Der Absender lehnt die Transaktion ab. Eine einzuhaltende Frist ist überschritten worden. Bei der Übermittlung von bilanzierungsrelevanten Stammdatenänderungen wird auch eine Ablehnung erfolgen, wenn das Änderungsdatum kein Monatserster ist. |
    | Z09 | **Ablehnung (Transaktionsgrund unplausibel)** — Der Absender lehnt die Transaktion ab. Transaktionsgrund und mitgelieferte Daten passen nicht zusammen. |
    | Z29 | **Ablehnung (kein Vertragsverhältnis mehr vorhanden)** — Der Absender lehnt die Transaktion ab. Der Kunde wurde zur betreffenden Marktlokation, Messlokation bzw. Tranche identifiziert, das Vertragsverhältnis wurde bereits zu einem früheren Zeitpunkt schon beendet. |
    | ZB6 | **Erforderliche Versicherung fehlt** |
    | ZC9 | **Ablehnung (keine Zuordnung möglich)** — Zuordnung zu einem Objekt mit den in der Festlegung beschriebenen Identifikationskriterien konnte nicht hergestellt werden. |
    
        </Accordion>
      </Tab>
    </Tabs>
  </Step>

  <Step title="Schnittstelle aktualisieren der Prozessdaten">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Aktualisieren der Prozessdaten bei Ablehnung"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14666382e0.md">
              Übergabe der erzeugten Rückmeldung an das Backend - 55044 (Ablehnung)
          </Card>
      </Tab>   
      <Tab title="📄55044">
          <Accordion title="PI_55044" defaultOpen={false}>
              
<DataSchema id="5242380" />
          </Accordion> 
      </Tab>
    </Tabs>
 
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Aktualisieren der Prozessdaten bei Zustimmung"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14666382e0.md">
              Übergabe der erzeugten Rückmeldung an das Backend - 55043, 21007 (Zustimmung)
          </Card>
      </Tab>   
      <Tab title="📄55043">
          <Accordion title="PI_55043" defaultOpen={false}>
             
<DataSchema id="5242379" />
          </Accordion> 
      </Tab>
      <Tab title="📄21007">
          <Accordion title="PI_21007" defaultOpen={false}>
             
<DataSchema id="8348207" />
          </Accordion> 
      </Tab>
    </Tabs>
  
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Aktualisieren der Prozessdaten bei Fristablauf"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14666382e0.md">
              Übergabe der erzeugten Rückmeldung an das Backend - 21013 (Fristablauf 55043)
          </Card>
      </Tab>   
      <Tab title="📄21013">
          <Accordion title="PI_21013" defaultOpen={false}>
              
<DataSchema id="8348212" />
          </Accordion> 
      </Tab>
    </Tabs>
  </Step>

  <Step title="Prozessauslöser - eingehende EDI (Statusmeldung)">
    <Tabs>
      <Tab title="Übersicht">         
        <CardGroup cols={2}>
          <Card title="21009">
              Scheitern Gesamtvorgang MSBN an NB
          </Card>
          <Card title="21010">
              Erfolgreicher Abschluss Gesamtvorgang MSBN an NB
          </Card>
        </CardGroup>
      </Tab>
      <Tab title="📄21009">
          <Accordion title="PI_21009" defaultOpen={false}>
                
<DataSchema id="8348208" />
          </Accordion> 
      </Tab>
      <Tab title="📄21010">
          <Accordion title="PI_21010" defaultOpen={false}>
                
<DataSchema id="8348209" />
          </Accordion> 
      </Tab>
    </Tabs>    
  </Step>

  <Step title="Schnittstellen lesend">
    <Tabs>
      <Tab title="Übersicht">         
        <CardGroup cols={2}>
          <Card title="Marktlokation lesen"
                href="https://doc.macoapp.de/marktlokation-lesen-14017020e0.md">
              LESEN_MARKTLOKATION_BASIS
          </Card>
          <Card title="Messlokation lesen" 
                href="https://doc.macoapp.de/messlokation-lesen-14017024e0.md">
              LESEN_MESSLOKATION_BASIS
          </Card>
        </CardGroup>
      </Tab>
      <Tab title="📄Marktlokation">
          <Accordion title="Marktlokation" defaultOpen={false}>
                
<DataSchema id="5241973" />
          </Accordion> 
      </Tab>
      <Tab title="📄Messlokation">
          <Accordion title="Messlokation" defaultOpen={false}>
             
<DataSchema id="5241975" />
          </Accordion> 
      </Tab>
    </Tabs> 
  </Step>

 <Step title="EBD-Prüfung">
    <Tabs>
      <Tab title="Übersicht">
        <CardGroup cols={2}>
          <Card title="E_0232">
              Mitteilung über Gesamtvorgang prüfen
              Zugehörige Codeliste S_0057
          </Card>
        </CardGroup>
      </Tab>
      <Tab title="📋 S_0057">
        <Accordion title="S_0057 - Statusmeldung" defaultOpen={true}>
          | Code | Antwortgrund |
          |---|---|
          | Z66 | **MSB-Scheitermeldung liegt vor** |
        </Accordion>
      </Tab>
    </Tabs>
  </Step>

  <Step title="Schnittstelle aktualisieren der Prozessdaten">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Aktualisieren der Prozessdaten"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14666382e0.md">
              Übergabe der erzeugten Rückmeldung an das Backend - 21012 (Erfolg)
          </Card>
      </Tab>   
      <Tab title="📄21012">
          <Accordion title="PI_21012" defaultOpen={false}>
              
<DataSchema id="8348211" />
          </Accordion> 
      </Tab>
    </Tabs>
  
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Aktualisieren der Prozessdaten"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14666382e0.md">
              Übergabe der erzeugten Rückmeldung an das Backend - 21011 (Scheitermeldung)
          </Card>
      </Tab>   
      <Tab title="📄21011">
          <Accordion title="PI_21011" defaultOpen={false}>
              
<DataSchema id="8348210" />
          </Accordion> 
      </Tab>
    </Tabs>
  </Step>

</Steps>
