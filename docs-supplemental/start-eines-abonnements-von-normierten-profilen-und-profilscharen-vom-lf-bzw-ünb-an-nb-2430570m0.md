# Start eines Abonnements von normierten Profilen und Profilscharen vom LF bzw. ÜNB an NB

# Prozessübersicht


![systembild_abo_profile_17201.png](https://api.apidog.com/api/v1/projects/816353/resources/383382/image-preview)
<Steps>
  <Step title="Prozessauslöser - Event" defaultOpen={false}>
    <Tabs>
      <Tab title="Übersicht">

        <Card title="START_ABO_PROFILE"
              href="apidog://link/endpoint/PLATZHALTER_ENDPOINT">
            Abonnement von normierten Profilen und Profilscharen vom LF bzw. ÜNB an den NB starten
        </Card>

      </Tab>
      <Tab title="📄START_ABO_PROFILE">
          <Accordion title="[LF] START_ABO_PROFILE" defaultOpen={false}>
                
              "stammdaten": {
      "ANFRAGE": [
        {
          "boTyp": "ANFRAGE",
          "versionStruktur": "1",
          "anfragekategorie": "NORMIERTES_PROFIL_PROFILSCHAR",
          "abonnement": "START_ABO"
        }
      ],
      "AUFTRAG": [
        {
          "boTyp": "AUFTRAG",
          "versionStruktur": "1",
          "positionsdaten": [
            {
              "positionsnummer": 1
            }
          ]
        }
      ],
      "BILANZIERUNG": [
        {
          "boTyp": "BILANZIERUNG",
          "versionStruktur": "1",
          "lastprofile": [
            {
              "profilart": "ART_STANDARDLASTPROFIL",
              "einspeisung": false
            }
          ]
        }
      ]
    },
    "transaktionsdaten": {
      "datenaustauschreferenz": "MSNEEICP",
      "sparte": "STROM",
      "pruefidentifikator": "17201",
      "absender": {
        "boTyp": "MARKTTEILNEHMER",
        "versionStruktur": "1",
        "gewerbekennzeichnung": true,
        "rollencodenummer": "9903854000005",
        "rollencodetyp": "BDEW"
      },
      "empfaenger": {
        "boTyp": "MARKTTEILNEHMER",
        "versionStruktur": "1",
        "gewerbekennzeichnung": true,
        "rollencodenummer": "9900683000008",
        "rollencodetyp": "BDEW"
      },
      "dokumentennummer": "MS8WHU7G",
      "kategorie": "Z19",
      "nachrichtendatum": "2026-10-02T07:00:00Z",
      "nachrichtenreferenznummer": "MS9W2NNW"
    }
              
          </Accordion>


      </Tab>
    </Tabs>

  </Step>
  <Step title="Schnittstellen schreibend">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Aktualisieren der Prozessdaten"
                  href="https://doc.macoapp.de/prozessdaten-aktualiseren-14017182e0.md"  >
              Übergabe der positiven bzw. negativen APERAK des Netzbetreibers an das Backend des Lieferanten. Eine fachliche Antwortnachricht gibt es in diesem Prozess nicht.
          </Card>
      </Tab>
      <Tab title="📄17201 Start eines Abonnements">
          <Accordion title="PI_17201" defaultOpen={false}>
                 "stammdaten": {
      "ANFRAGE": [
        {
          "boTyp": "ANFRAGE",
          "versionStruktur": "1",
          "anfragekategorie": "NORMIERTES_PROFIL_PROFILSCHAR",
          "abonnement": "START_ABO"
        }
      ],
      "AUFTRAG": [
        {
          "boTyp": "AUFTRAG",
          "versionStruktur": "1",
          "positionsdaten": [
            {
              "positionsnummer": 1
            }
          ]
        }
      ],
      "BILANZIERUNG": [
        {
          "boTyp": "BILANZIERUNG",
          "versionStruktur": "1",
          "lastprofile": [
            {
              "profilart": "ART_STANDARDLASTPROFIL",
              "einspeisung": false
            }
          ]
        }
      ]
    },
    "transaktionsdaten": {
      "datenaustauschreferenz": "MSNEEICP",
      "sparte": "STROM",
      "pruefidentifikator": "17201",
      "absender": {
        "boTyp": "MARKTTEILNEHMER",
        "versionStruktur": "1",
        "gewerbekennzeichnung": true,
        "rollencodenummer": "9903854000005",
        "rollencodetyp": "BDEW"
      },
      "empfaenger": {
        "boTyp": "MARKTTEILNEHMER",
        "versionStruktur": "1",
        "gewerbekennzeichnung": true,
        "rollencodenummer": "9900683000008",
        "rollencodetyp": "BDEW"
      },
      "dokumentennummer": "MS8WHU7G",
      "kategorie": "Z19",
      "nachrichtendatum": "2026-10-02T07:00:00Z",
      "nachrichtenreferenznummer": "MS9W2NNW"
    }
          </Accordion>


      </Tab>
      <Tab title="📄APERAK pos. / neg.">
          <Accordion title="APERAK Negativ" defaultOpen={false}>
               
<DataSchema id="13005934" />
          </Accordion>


          <Accordion title="APERAK Positiv" defaultOpen={false}>
               
<DataSchema id="13005933" />
          </Accordion>

      </Tab>
    </Tabs>
  </Step>
</Steps>

