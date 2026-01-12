# Stornierung Werte vom MSB der Marktlokation (Rolle LF)


![LW24h mit Abhängigkeiten - Stornierung Werte vom MSB der Marktlokation (Rolle LF).png](https://api.apidog.com/api/v1/projects/816353/resources/367341/image-preview)
<Steps>
  <Step title="Prozessauslöser - eingehende EDI" defaultOpen={false}>
    <Tabs>
      <Tab title="Übersicht">
 
        <Card title="13006 Messwert Storno">
              Messwert Storno
          </Card>

      </Tab>        
      
      <Tab title="📄13006 Messwert Storno">
          <Accordion title="PI_13006" defaultOpen={false}>
               
          </Accordion>
      </Tab>
    </Tabs>

  </Step>
  <Step title="Schnittstellen schreibend">
    <Tabs>
      <Tab title="Übersicht">
          <Card title="Erstellen der Prozessdaten"
                href="https://doc.macoapp.de/prozessdaten-erstellen-14017183e0.md">
              Übergabe der initialen Prozessdaten an das Backend
          </Card>    
      </Tab>
       <Tab title="📄13006 Messwert Storno">
          <Accordion title="PI_13006" defaultOpen={false}>
                 <DataSchema id="5562216" />
          </Accordion>
       </Tab>
        
        <Tab title="📄13006 Edi">
          <Accordion title="PI_13006" defaultOpen={false}>
                 ```UNA:+.? '
UNB+UNOC:3+9904446000007:500+9900321000005:500+251010:1301+978509++VL'
UNH+542637+MSCONS:D:04B:UN:2.4c'
BGM+7+542637BGM+1'
DTM+137:202303300908?+00:303'
RFF+ACW:REF123456789'
RFF+Z13:13006'
NAD+MS+9904446000007::293'
CTA+IC+:Max Mustermann'
COM+max@mustermann.de:EM'
COM+?+012345678920:AJ'
COM+?+012345678940:FX'
COM+?+012345678910:TE'
COM+?+012345678930:AL'
NAD+MR+9900321000005::293'
UNS+D'
NAD+DP'
LOC+172'
UNT+17+542637'
UNZ+1+978509'
  ```
          </Accordion>
       </Tab>
        
        <Tab title="📄13006 JSON">
          <Accordion title="13006 JSON" defaultOpen={false}>
               ```{
  "businessKey": "<businessKey>",
  "processDate": null,
  "dataSource": "OUTBOUND",
  "version": 1,
  "edifactVersion": 202510,
  "data": {
    "stammdaten": {},
    "transaktionsdaten": {
      "datenaustauschreferenz": "978509",
      "sparte": "STROM",
      "pruefidentifikator": "13006",
      "absender": {
        "boTyp": "MARKTTEILNEHMER",
        "versionStruktur": "1",
        "rollencodenummer": "9904446000007",
        "rollencodetyp": "BDEW",
        "ansprechpartner": {
          "boTyp": "ANSPRECHPARTNER",
          "versionStruktur": "1",
          "nachname": "Max Mustermann",
          "eMailAdresse": "max@mustermann.de",
          "rufnummern": [
            {
              "nummerntyp": "RUF_ZENTRALE",
              "rufnummer": "+012345678920"
            },
            {
              "nummerntyp": "FAX_DURCHWAHL",
              "rufnummer": "+012345678940"
            },
            {
              "nummerntyp": "RUF_DURCHWAHL",
              "rufnummer": "+012345678910"
            },
            {
              "nummerntyp": "MOBIL_NUMMER",
              "rufnummer": "+012345678930"
            }
          ]
        }
      },
      "empfaenger": {
        "boTyp": "MARKTTEILNEHMER",
        "versionStruktur": "1",
        "rollencodenummer": "9900321000005",
        "rollencodetyp": "BDEW"
      },
      "dokumentennummer": "542637BGM",
      "kategorie": "7",
      "nachrichtenfunktion": "1",
      "nachrichtendatum": "2023-03-30T09:08:00Z",
      "nachrichtenreferenznummer": "542637",
      "vorgangsreferenznummer": "REF123456789",
      "typ": "VL"
    },
    "zusatzdaten": {}
  }
}
  ```  
  </Accordion>
       </Tab>
      
    </Tabs>
  </Step>
  
</Steps>


