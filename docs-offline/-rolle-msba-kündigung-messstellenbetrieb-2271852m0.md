# ( Rolle MSBA ) Kündigung Messstellenbetrieb 


![LW24h mit Abhängigkeiten - STROM Kündigung Messstellenbetrieb ( Rolle MSBA ).png](https://api.apidog.com/api/v1/projects/816353/resources/380234/image-preview)

<Steps>

  <Step title="Prozessauslöser - eingehende EDI">
    <Tabs>
      <Tab title="Übersicht">
        <CardGroup cols={2}>
          <Card title="55039">
              Kündigung Messstellenbetrieb MSBN an MSBA
          </Card>
        </CardGroup>
      </Tab>
      <Tab title="📄55039">
          <Accordion title="PI_55039" defaultOpen={false}>

<DataSchema id="5242375" />
          </Accordion>
      </Tab>
    </Tabs>
  </Step>

  <Step title="Prozessinitiierung Backend">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Erstellen Prozessdaten für Prüfi 55039"
                href="https://doc.macoapp.de/prozessdaten-erstellen-14666311e0.md">
              Übergabe der initialen Prozessdaten an das Backend
          </Card>
      </Tab>
      <Tab title="📄55039">
          <Accordion title="PI_55039" defaultOpen={false}>

<DataSchema id="5242375" />
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
          <Card title="Messstellenbetriebsvertrag lesen"
                href="https://doc.macoapp.de/messstellenbetriebsvertrag-lesen-14017025e0.md">
              LESEN_MESSSTELLENBETRIEBSVERTRAG_BASIS
          </Card>
          <Card title="Zähler lesen"
                href="https://doc.macoapp.de/z%C3%A4hler-lesen-14017031e0.md">
              LESEN_ZAEHLER_BASIS
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

<DataSchema id="5241988" />
          </Accordion>
      </Tab>
      <Tab title="📄Zähler">
          <Accordion title="Zähler" defaultOpen={false}>


<DataSchema id="5241991" />
          </Accordion>
      </Tab>
    </Tabs>
  </Step>

  <Step title="EBD-Prüfung">
    <Tabs>
      <Tab title="Übersicht">
        <CardGroup cols={2}>
          <Card title="E_0200">
              Kündigung Messstellenbetrieb prüfen (Strom)
              Zugehörige Codelisten S_0054 & S_0090
          </Card>
        </CardGroup>
      </Tab>
      <Tab title="✅ S_0090">
        <Accordion title="S_0090 - Bestätigung Kündigung MSBS" defaultOpen={true}>
          | Code | Antwortgrund |
    |---|---|
    | E15 | **Zustimmung ohne Korrekturen** — Der Absender stimmt der Meldung und den Inhalten des Vorgangs voll zu. Er hat keine Änderungen an den gesendeten Daten vorgenommen. Er kann allerdings Daten gemäß seiner Aufgabe im Prozess vervollständigt haben (z. B. der NB bei einer Anmeldung mit dem Standardlastprofil). In diesen Fällen ist Z44 nicht zu verwenden. |
    | Z01 | **Zustimmung mit Terminänderung (Default)** — Der Absender stimmt der Meldung zu einem abweichenden Termin zu. Mit dieser Kennzeichnung übermittelt der Absender dem Sender der ursprünglichen Meldung, dass diese abgelehnt wurde (Ablehnung zum alten Termin), jedoch eine Zustimmung zu einem abweichenden Termin erfolgte.  |
    | Z44 | **Zustimmung mit Korrektur von nicht bilanzierungsrel. Daten (Default)** — Die Zustimmung erfolgt mit Korrektur von nicht bilanzierungsrelevanten Daten in der Antwortnachricht. Die Bilanzierungsrelevanz leitet sich aus der Übersicht der Änderungsmeldungen ab. |
        </Accordion>
      </Tab>
      <Tab title="❌ S_0054">
        <Accordion title="S_0054 - Ablehnung Kündigung MSB" defaultOpen={true}>
          | Code | Antwortgrund |
    |---|---|
    | E11 | **Ablehnung (Messproblem) (Default)** — Der Absender lehnt die Transaktion ab. Der Marktpartner fordert ein Messverfahren, was in diesem Fall nicht möglich ist bzw. nicht mit dem Leistungsumfang vereinbar ist. |
    | Z12 | **Ablehnung Vertragsbindung** — Der Absender lehnt die Transaktion ab. Z. B. einer Kündigung kann nicht entsprochen werden, da der Kunde oder der andere Marktpartner zum Termin noch eine vertragliche Bindung hat. Anm.: Im DTM Segment „Änderung zum, Gültigkeit, Beginndatum" muss dann der nächstmögliche Kündigungszeitpunkt mitgegeben werden. Dies ist aber dann nicht als Zustimmung zum in dem Feld „Änderung zum, Gültigkeit, Beginndatum" angegebenen Termin zu interpretieren!  |
    | Z29 | **Ablehnung (kein Vertragsverhältnis mehr vorhanden)** — Der Absender lehnt die Transaktion ab. Der Kunde wurde zur betreffenden Marktlokation, Messlokation bzw. Tranche identifiziert, das Vertragsverhältnis wurde bereits zu einem früheren Zeitpunkt schon beendet. |
    | Z34 | **Ablehnung (Mehrfachkündigung)** — Gilt nur im Prozess Kündigung. Der Vertrag wurde bereits zum angefragten Kündigungstermin wirksam durch einen anderen Marktpartner oder den Kunden selbst gekündigt. |
    | ZC9 | **Ablehnung (keine Zuordnung möglich)** — Zuordnung zu einem Objekt mit den in der Festlegung beschriebenen Identifizierungskriterien konnte nicht hergestellt werden. |
        </Accordion>
      </Tab>
    </Tabs>
  </Step>

  <Step title="Schnittstelle aktualisieren der Prozessdaten">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Aktualisieren der Prozessdaten bei Zustimmung"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14666382e0.md">
              Übergabe der erzeugten Rückmeldung an das Backend - 55040 (Zustimmung)
          </Card>
      </Tab>
      <Tab title="📄55040">
          <Accordion title="PI_55040" defaultOpen={false}>


<DataSchema id="5242376" />
          </Accordion>
      </Tab>
    </Tabs>

    <Tabs>
      <Tab title="Übersicht">
          <Card title="Aktualisieren der Prozessdaten bei Ablehnung"
                href="https://doc.macoapp.de/prozessdaten-aktualiseren-14666382e0.md">
              Übergabe der erzeugten Rückmeldung an das Backend - 55041 (Ablehnung)
          </Card>
      </Tab>
      <Tab title="📄55041">
          <Accordion title="PI_55041" defaultOpen={false}>


<DataSchema id="5242377" />
          </Accordion>
      </Tab>
    </Tabs>
  </Step>

</Steps>
