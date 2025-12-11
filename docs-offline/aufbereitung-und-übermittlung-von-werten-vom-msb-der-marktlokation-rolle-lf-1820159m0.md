# Aufbereitung und Übermittlung von Werten vom MSB der Marktlokation (Rolle LF)



![LW24h mit Abhängigkeiten - Aufbereitung und Übermittlung von Werten vom MSB der Marktlokation (Rolle LF)(1).png](https://api.apidog.com/api/v1/projects/816353/resources/367367/image-preview)

<DataSchema id="8348182" />
    <Steps>
  <Step title="13016 EDI">
    <Tabs>
  <Tab title="13016 Edi">
    <Accordion title="13016 Edi" defaultOpen>
  
  ```UNA:+,? '
UNB+UNOC:3+9903000000001:500+9903000000002:500+251010:1148+DAOSVPKMWRQLGA++EM'
UNH+UNHM23DNH3R+MSCONS:D:04B:UN:2.4c'
BGM+Z28+BGMM28EY1DG+9'
DTM+137:202410031148?+00:303'
RFF+AGI:PP172409301012154888888888888563413'
RFF+Z13:13016'
NAD+MS+9903000000001::293'
NAD+MR+9903000000002::293'
UNS+D'
NAD+DP'
LOC+172+12345678901'
LIN+1'
PIA+5+1-1?:1.9.0:SRW'
QTY+67:10123'
DTM+163:202405012200?+00:303'
DTM+164:202406012200?+00:303'
STS+Z33++Z84'
STS+Z32++Z88'
STS+Z34++Z74'
STS+Z40++Z74'
UNT+20+UNHM23DNH3R'
UNZ+1+DAOSVPKMWRQLGA'
  ```
</Accordion>
  </Tab>
</Tabs>
  </Step>
  <Step title="13016 JSON">
    <Tabs>
  <Tab title="13016 JSON">
    <Accordion title="13016 JSON" defaultOpen>
  
  ```{
  "businessKey": "<businessKey>",
  "processDate": null,
  "dataSource": "INBOUND",
  "version": 1,
  "edifactVersion": 202510,
  "data": {
    "stammdaten": {
      "ENERGIEMENGE": [
        {
          "boTyp": "ENERGIEMENGE",
          "versionStruktur": "1",
          "lokationsId": "50375312838",
          "lokationsTyp": "MALO",
          "energieverbrauch": [
            {
              "startdatum": "2023-12-22T05:00:00Z",
              "enddatum": "2024-08-02T04:00:00Z",
              "messwertstatus": "ERSATZWERT",
              "obiskennzahl": "1-0:1.29.0",
              "wert": 1223,
              "nutzungszeitpunkt": "2024-08-02T04:00:00Z",
              "position": 1
            }
          ]
        }
      ]
    },
    "transaktionsdaten": {
      "datenaustauschreferenz": "P1001099269230",
      "sparte": "STROM",
      "pruefidentifikator": "13027",
      "absender": {
        "boTyp": "MARKTTEILNEHMER",
        "versionStruktur": "1",
        "gewerbekennzeichnung": true,
        "rollencodenummer": "9979100000001",
        "rollencodetyp": "BDEW"
      },
      "empfaenger": {
        "boTyp": "MARKTTEILNEHMER",
        "versionStruktur": "1",
        "gewerbekennzeichnung": true,
        "rollencodenummer": "9904400000002",
        "rollencodetyp": "BDEW"
      },
      "dokumentennummer": "BGMM2B120EC",
      "kategorie": "Z83",
      "nachrichtenfunktion": "9",
      "nachrichtendatum": "2024-10-01T06:07:00Z",
      "nachrichtenreferenznummer": "UNHM2BQ4A83",
      "typ": "TL",
      "anfrageReferenz": "PP172409301012154888888888888563413"
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
        
<DataSchema id="8348183" />
    <Steps>
  <Step title="13017 EDI">
    <Tabs>
  <Tab title="13017 Edi">
    <Accordion title="13017 Edi" defaultOpen>

  ```UNB+UNOC:3+9904079000002:500+9900051000002:500+251010:1341+141757++VL'
UNH+137826+MSCONS:D:04B:UN:2.4c'
BGM+7+137826BGM+9'
DTM+137:202404011241?+00:303'
RFF+AGI:REF12345678910'
RFF+Z13:13017'
NAD+MS+9904079000002::293'
CTA+IC+:Max Mustermann'
COM+?+12345678910:TE'
COM+?+12345678910:AJ'
COM+?+12345678910:FX'
COM+?+12345678910:AL'
COM+max@mustermann.de:EM'
NAD+MR+9900051000002::293'
UNS+D'
NAD+DP'
LOC+172+DE0073395252733953513649640711234'
RFF+MG:G12345678910'
LIN+1'
PIA+5+1-1?:1.8.0:SRW'
QTY+220:1234567.357'
DTM+9:202403011100?+00:303'
DTM+7:202403012300?+00:303'
STS+Z33++Z83'
UNT+24+137826'
UNZ+1+141757'
  ```
</Accordion>
  </Tab>
</Tabs>
  </Step>
  <Step title="13017 JSON">
    <Tabs>
  <Tab title="13017 JSON">
    <Accordion title="13017 JSON" defaultOpen>
 
  ```{
  "businessKey": "<businessKey>",
  "processDate": null,
  "dataSource": "INBOUND",
  "version": 1,
  "edifactVersion": 202510,
  "data": {
    "stammdaten": {
      "ZAEHLER": [
        {
          "boTyp": "ZAEHLER",
          "versionStruktur": "1",
          "zaehlernummer": "G12345678910",
          "sparte": "STROM"
        }
      ],
      "ENERGIEMENGE": [
        {
          "boTyp": "ENERGIEMENGE",
          "versionStruktur": "1",
          "lokationsId": "DE0073395252733953513649640711234",
          "lokationsTyp": "MELO",
          "energieverbrauch": [
            {
              "messwertstatus": "ABGELESEN",
              "statuszusatzinformationen": [
                {
                  "art": "PLAUSIBILISIERUNGSHINWEIS",
                  "status": "KUNDENSELBSTABLESUNG"
                }
              ],
              "obiskennzahl": "1-1:1.8.0",
              "wert": 1234567.357,
              "nutzungszeitpunkt": "2024-03-01T23:00:00Z",
              "position": 1,
              "ablesedatum": "2024-03-01T11:00:00Z"
            }
          ]
        }
      ]
    },
    "transaktionsdaten": {
      "datenaustauschreferenz": "141757",
      "sparte": "STROM",
      "pruefidentifikator": "13017",
      "absender": {
        "boTyp": "MARKTTEILNEHMER",
        "versionStruktur": "1",
        "gewerbekennzeichnung": true,
        "rollencodenummer": "9904079000002",
        "rollencodetyp": "BDEW",
        "ansprechpartner": {
          "boTyp": "ANSPRECHPARTNER",
          "versionStruktur": "1",
          "nachname": "Max Mustermann",
          "eMailAdresse": "max@mustermann.de",
          "rufnummern": [
            {
              "nummerntyp": "RUF_ZENTRALE",
              "rufnummer": "+12345678910"
            },
            {
              "nummerntyp": "FAX_DURCHWAHL",
              "rufnummer": "+12345678910"
            },
            {
              "nummerntyp": "RUF_DURCHWAHL",
              "rufnummer": "+12345678910"
            },
            {
              "nummerntyp": "MOBIL_NUMMER",
              "rufnummer": "+12345678910"
            }
          ]
        }
      },
      "empfaenger": {
        "boTyp": "MARKTTEILNEHMER",
        "versionStruktur": "1",
        "gewerbekennzeichnung": true,
        "rollencodenummer": "9900051000002",
        "rollencodetyp": "BDEW"
      },
      "dokumentennummer": "137826BGM",
      "kategorie": "7",
      "nachrichtenfunktion": "9",
      "nachrichtendatum": "2024-04-01T12:41:00Z",
      "nachrichtenreferenznummer": "137826",
      "typ": "VL",
      "anfrageReferenz": "REF12345678910"
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

        
<DataSchema id="8348184" />
    <Steps>
  <Step title="13018 EDI">
    <Tabs>
  <Tab title="13018 Edi">
    <Accordion title="13018 Edi" defaultOpen>

  ```UNA:+,? '
UNB+UNOC:3+9979100000001:500+9904400000002:500+251010:0453+P1001099269230++TL'
UNH+UNHM2A21HUI+MSCONS:D:04B:UN:2.4c'
BGM+7+BGMM2OK54U5+9'
DTM+137:202410020453?+00:303'
RFF+AGI:AFN9523'
RFF+Z13:13018'
NAD+MS+9979100000001::293'
NAD+MR+9904400000002::293'
UNS+D'
NAD+DP'
LOC+172+DE0004962684900000000000010571835'
DTM+163:202312220500?+00:303'
DTM+164:202408020400?+00:303'
LIN+1'
PIA+5+1-0?:5.29.0:SRW'
QTY+Z18:4250.465'
DTM+163:202312220500?+00:303'
DTM+164:202408020400?+00:303'
STS+Z34++Z78'
UNT+19+UNHM2A21HUI'
UNZ+1+P1001099269230'
  ```
</Accordion>
  </Tab>
</Tabs>
  </Step>
  <Step title="13018 JSON">
    <Tabs>
  <Tab title="13018 JSON">
    <Accordion title="13018 JSON" defaultOpen>

  ```{
  "businessKey": "<businessKey>",
  "processDate": null,
  "dataSource": "INBOUND",
  "version": 1,
  "edifactVersion": 202510,
  "data": {
    "stammdaten": {
      "ENERGIEMENGE": [
        {
          "boTyp": "ENERGIEMENGE",
          "versionStruktur": "1",
          "lokationsId": "DE0004962684900000000000010571835",
          "lokationsTyp": "MELO",
          "energieverbrauch": [
            {
              "startdatum": "2023-12-22T05:00:00Z",
              "enddatum": "2024-08-02T04:00:00Z",
              "messwertstatus": "VOLAEUFIGERWERT",
              "statuszusatzinformationen": [
                {
                  "art": "KORREKTURGRUND",
                  "status": "STATUS_GERAETEWECHSEL"
                }
              ],
              "obiskennzahl": "1-0:5.29.0",
              "wert": 4250.465,
              "position": 1
            }
          ],
          "startdatum": "2023-12-22T05:00:00Z",
          "enddatum": "2024-08-02T04:00:00Z"
        }
      ]
    },
    "transaktionsdaten": {
      "datenaustauschreferenz": "P1001099269230",
      "sparte": "STROM",
      "pruefidentifikator": "13018",
      "absender": {
        "boTyp": "MARKTTEILNEHMER",
        "versionStruktur": "1",
        "gewerbekennzeichnung": true,
        "rollencodenummer": "9979100000001",
        "rollencodetyp": "BDEW"
      },
      "empfaenger": {
        "boTyp": "MARKTTEILNEHMER",
        "versionStruktur": "1",
        "gewerbekennzeichnung": true,
        "rollencodenummer": "9904400000002",
        "rollencodetyp": "BDEW"
      },
      "dokumentennummer": "BGMM2OK54U5",
      "kategorie": "7",
      "nachrichtenfunktion": "9",
      "nachrichtendatum": "2024-10-02T04:53:00Z",
      "nachrichtenreferenznummer": "UNHM2A21HUI",
      "typ": "TL",
      "anfrageReferenz": "AFN9523"
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
        
<DataSchema id="8348185" />
        <Steps>
  <Step title="13019 EDI">
    <Tabs>
  <Tab title="13019 Edi">
    <Accordion title="13019 Edi" defaultOpen>
  
  ```UNA:+.? '
UNB+UNOC:3+9900321000005:500+9903790000002:500+251010:1338+510029++EM'
UNH+621092+MSCONS:D:04B:UN:2.4c'
BGM+Z41+621092BGM+9'
DTM+137:202303291313?+00:303'
RFF+Z13:13019'
NAD+MS+9900321000005::293'
CTA+IC+:Max Mustermann'
COM+max@mustermann.de:EM'
COM+?+012345678920:AJ'
COM+?+012345678940:FX'
COM+?+012345678910:TE'
COM+?+012345678930:AL'
NAD+MR+9903790000002::293'
UNS+D'
NAD+DP'
LOC+172+50074561188'
LIN+1'
PIA+5+1-0?:1.9.0:SRW'
QTY+Z31:2000'
DTM+163:202212312300?+00:303'
DTM+164:202303152300?+00:303'
UNT+21+621092'
UNZ+1+510029'
  ```
</Accordion>
  </Tab>
</Tabs>
  </Step>
  <Step title="13019 JSON">
    <Tabs>
  <Tab title="13019 JSON">
    <Accordion title="13019 JSON" defaultOpen>

  ```{
  "businessKey": "<businessKey>",
  "processDate": null,
  "dataSource": "OUTBOUND",
  "version": 1,
  "edifactVersion": 202510,
  "data": {
    "stammdaten": {
      "ENERGIEMENGE": [
        {
          "boTyp": "ENERGIEMENGE",
          "versionStruktur": "1",
          "lokationsId": "50074561188",
          "lokationsTyp": "MALO",
          "energieverbrauch": [
            {
              "startdatum": "2022-12-31T23:00:00Z",
              "enddatum": "2023-03-15T23:00:00Z",
              "messwertstatus": "ANGABE_FUER_LIEFERSCHEIN",
              "obiskennzahl": "1-0:1.9.0",
              "wert": 2000,
              "position": 1
            }
          ]
        }
      ]
    },
    "transaktionsdaten": {
      "datenaustauschreferenz": "510029",
      "sparte": "STROM",
      "pruefidentifikator": "13019",
      "absender": {
        "boTyp": "MARKTTEILNEHMER",
        "versionStruktur": "1",
        "marktrolle": "NB",
        "rollencodenummer": "9900321000005",
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
        "marktrolle": "LF",
        "rollencodenummer": "9903790000002",
        "rollencodetyp": "BDEW"
      },
      "dokumentennummer": "621092BGM",
      "kategorie": "Z41",
      "nachrichtenfunktion": "9",
      "nachrichtendatum": "2023-03-29T13:13:00Z",
      "nachrichtenreferenznummer": "621092",
      "typ": "EM"
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
            
           
<DataSchema id="8348186" />
        <Steps>
  <Step title="13025 EDI">
    <Tabs>
  <Tab title="13025 Edi">
    <Accordion title="13025 Edi" defaultOpen>

  ```UNA:+.? '
UNB+UNOC:3+9904545000007:500+9911694000002:500+251010:0553+K21E0D864ED9++TL'
UNH+1+MSCONS:D:04B:UN:2.4c'
BGM+Z48+K21E0D864ED90+9'
DTM+137:202404030553?+00:303'
RFF+Z13:13025'
NAD+MS+9904545000007::293'
NAD+MR+9911694000002::293'
UNS+D'
NAD+DP'
LOC+172+51580175011'
DTM+163:202310052200?+00:303'
DTM+164:202310062200?+00:303'
LIN+1'
PIA+5+1-1?:3.29.0:SRW'
QTY+220:0'
DTM+163:202310052200?+00:303'
DTM+164:202310052215?+00:303'
QTY+220:0'
DTM+163:202310052215?+00:303'
DTM+164:202310052230?+00:303'
QTY+220:0'
DTM+163:202310052230?+00:303'
DTM+164:202310052245?+00:303'
QTY+220:0'
DTM+163:202310052245?+00:303'
DTM+164:202310052300?+00:303'
QTY+220:0'
DTM+163:202310052300?+00:303'
DTM+164:202310052315?+00:303'
QTY+220:0'
DTM+163:202310052315?+00:303'
DTM+164:202310052330?+00:303'
QTY+220:0'
DTM+163:202310052330?+00:303'
DTM+164:202310052345?+00:303'
QTY+220:0'
DTM+163:202310052345?+00:303'
DTM+164:202310060000?+00:303'
QTY+220:0'
DTM+163:202310060000?+00:303'
DTM+164:202310060015?+00:303'
QTY+220:0'
DTM+163:202310060015?+00:303'
DTM+164:202310060030?+00:303'
QTY+220:0'
DTM+163:202310060030?+00:303'
DTM+164:202310060045?+00:303'
QTY+220:0'
DTM+163:202310060045?+00:303'
DTM+164:202310060100?+00:303'
QTY+220:0'
DTM+163:202310060100?+00:303'
DTM+164:202310060115?+00:303'
QTY+220:0'
DTM+163:202310060115?+00:303'
DTM+164:202310060130?+00:303'
QTY+220:0'
DTM+163:202310060130?+00:303'
DTM+164:202310060145?+00:303'
QTY+220:0'
DTM+163:202310060145?+00:303'
DTM+164:202310060200?+00:303'
QTY+220:0'
DTM+163:202310060200?+00:303'
DTM+164:202310060215?+00:303'
QTY+220:0'
DTM+163:202310060215?+00:303'
DTM+164:202310060230?+00:303'
QTY+220:0'
DTM+163:202310060230?+00:303'
DTM+164:202310060245?+00:303'
QTY+220:0'
DTM+163:202310060245?+00:303'
DTM+164:202310060300?+00:303'
QTY+220:0'
DTM+163:202310060300?+00:303'
DTM+164:202310060315?+00:303'
QTY+220:0'
DTM+163:202310060315?+00:303'
DTM+164:202310060330?+00:303'
QTY+220:0'
DTM+163:202310060330?+00:303'
DTM+164:202310060345?+00:303'
QTY+220:0'
DTM+163:202310060345?+00:303'
DTM+164:202310060400?+00:303'
QTY+220:0'
DTM+163:202310060400?+00:303'
DTM+164:202310060415?+00:303'
QTY+220:0'
DTM+163:202310060415?+00:303'
DTM+164:202310060430?+00:303'
QTY+220:0.012'
DTM+163:202310060430?+00:303'
DTM+164:202310060445?+00:303'
QTY+220:0'
DTM+163:202310060445?+00:303'
DTM+164:202310060500?+00:303'
QTY+220:0.188'
DTM+163:202310060500?+00:303'
DTM+164:202310060515?+00:303'
QTY+220:0.388'
DTM+163:202310060515?+00:303'
DTM+164:202310060530?+00:303'
QTY+220:0'
DTM+163:202310060530?+00:303'
DTM+164:202310060545?+00:303'
QTY+220:0.075'
DTM+163:202310060545?+00:303'
DTM+164:202310060600?+00:303'
QTY+220:0.012'
DTM+163:202310060600?+00:303'
DTM+164:202310060615?+00:303'
QTY+220:0'
DTM+163:202310060615?+00:303'
DTM+164:202310060630?+00:303'
QTY+220:0'
DTM+163:202310060630?+00:303'
DTM+164:202310060645?+00:303'
QTY+220:0'
DTM+163:202310060645?+00:303'
DTM+164:202310060700?+00:303'
QTY+220:0'
DTM+163:202310060700?+00:303'
DTM+164:202310060715?+00:303'
QTY+220:0.088'
DTM+163:202310060715?+00:303'
DTM+164:202310060730?+00:303'
QTY+220:0.975'
DTM+163:202310060730?+00:303'
DTM+164:202310060745?+00:303'
QTY+220:0.175'
DTM+163:202310060745?+00:303'
DTM+164:202310060800?+00:303'
QTY+220:0.162'
DTM+163:202310060800?+00:303'
DTM+164:202310060815?+00:303'
QTY+220:0'
DTM+163:202310060815?+00:303'
DTM+164:202310060830?+00:303'
QTY+220:0'
DTM+163:202310060830?+00:303'
DTM+164:202310060845?+00:303'
QTY+220:0.088'
DTM+163:202310060845?+00:303'
DTM+164:202310060900?+00:303'
QTY+220:0.175'
DTM+163:202310060900?+00:303'
DTM+164:202310060915?+00:303'
QTY+220:0.3'
DTM+163:202310060915?+00:303'
DTM+164:202310060930?+00:303'
QTY+220:0.225'
DTM+163:202310060930?+00:303'
DTM+164:202310060945?+00:303'
QTY+220:0.375'
DTM+163:202310060945?+00:303'
DTM+164:202310061000?+00:303'
QTY+220:0'
DTM+163:202310061000?+00:303'
DTM+164:202310061015?+00:303'
QTY+220:0'
DTM+163:202310061015?+00:303'
DTM+164:202310061030?+00:303'
QTY+220:0'
DTM+163:202310061030?+00:303'
DTM+164:202310061045?+00:303'
QTY+220:0.012'
DTM+163:202310061045?+00:303'
DTM+164:202310061100?+00:303'
QTY+220:0'
DTM+163:202310061100?+00:303'
DTM+164:202310061115?+00:303'
QTY+220:0'
DTM+163:202310061115?+00:303'
DTM+164:202310061130?+00:303'
QTY+220:0'
DTM+163:202310061130?+00:303'
DTM+164:202310061145?+00:303'
QTY+220:0.125'
DTM+163:202310061145?+00:303'
DTM+164:202310061200?+00:303'
QTY+220:0.138'
DTM+163:202310061200?+00:303'
DTM+164:202310061215?+00:303'
QTY+220:0'
DTM+163:202310061215?+00:303'
DTM+164:202310061230?+00:303'
QTY+220:0'
DTM+163:202310061230?+00:303'
DTM+164:202310061245?+00:303'
QTY+220:0'
DTM+163:202310061245?+00:303'
DTM+164:202310061300?+00:303'
QTY+220:0'
DTM+163:202310061300?+00:303'
DTM+164:202310061315?+00:303'
QTY+220:0'
DTM+163:202310061315?+00:303'
DTM+164:202310061330?+00:303'
QTY+220:0'
DTM+163:202310061330?+00:303'
DTM+164:202310061345?+00:303'
QTY+220:0'
DTM+163:202310061345?+00:303'
DTM+164:202310061400?+00:303'
QTY+220:0'
DTM+163:202310061400?+00:303'
DTM+164:202310061415?+00:303'
QTY+220:0'
DTM+163:202310061415?+00:303'
DTM+164:202310061430?+00:303'
QTY+220:0'
DTM+163:202310061430?+00:303'
DTM+164:202310061445?+00:303'
QTY+220:0'
DTM+163:202310061445?+00:303'
DTM+164:202310061500?+00:303'
QTY+220:0'
DTM+163:202310061500?+00:303'
DTM+164:202310061515?+00:303'
QTY+220:0'
DTM+163:202310061515?+00:303'
DTM+164:202310061530?+00:303'
QTY+220:0'
DTM+163:202310061530?+00:303'
DTM+164:202310061545?+00:303'
QTY+220:0'
DTM+163:202310061545?+00:303'
DTM+164:202310061600?+00:303'
QTY+220:0'
DTM+163:202310061600?+00:303'
DTM+164:202310061615?+00:303'
QTY+220:0'
DTM+163:202310061615?+00:303'
DTM+164:202310061630?+00:303'
QTY+220:0'
DTM+163:202310061630?+00:303'
DTM+164:202310061645?+00:303'
QTY+220:0'
DTM+163:202310061645?+00:303'
DTM+164:202310061700?+00:303'
QTY+220:0'
DTM+163:202310061700?+00:303'
DTM+164:202310061715?+00:303'
QTY+220:0'
DTM+163:202310061715?+00:303'
DTM+164:202310061730?+00:303'
QTY+220:0'
DTM+163:202310061730?+00:303'
DTM+164:202310061745?+00:303'
QTY+220:0'
DTM+163:202310061745?+00:303'
DTM+164:202310061800?+00:303'
QTY+220:0'
DTM+163:202310061800?+00:303'
DTM+164:202310061815?+00:303'
QTY+220:0'
DTM+163:202310061815?+00:303'
DTM+164:202310061830?+00:303'
QTY+220:0'
DTM+163:202310061830?+00:303'
DTM+164:202310061845?+00:303'
QTY+220:0'
DTM+163:202310061845?+00:303'
DTM+164:202310061900?+00:303'
QTY+220:0'
DTM+163:202310061900?+00:303'
DTM+164:202310061915?+00:303'
QTY+220:0'
DTM+163:202310061915?+00:303'
DTM+164:202310061930?+00:303'
QTY+220:0'
DTM+163:202310061930?+00:303'
DTM+164:202310061945?+00:303'
QTY+220:0'
DTM+163:202310061945?+00:303'
DTM+164:202310062000?+00:303'
QTY+220:0'
DTM+163:202310062000?+00:303'
DTM+164:202310062015?+00:303'
QTY+220:0'
DTM+163:202310062015?+00:303'
DTM+164:202310062030?+00:303'
QTY+220:0'
DTM+163:202310062030?+00:303'
DTM+164:202310062045?+00:303'
QTY+220:0'
DTM+163:202310062045?+00:303'
DTM+164:202310062100?+00:303'
QTY+220:0'
DTM+163:202310062100?+00:303'
DTM+164:202310062115?+00:303'
QTY+220:0'
DTM+163:202310062115?+00:303'
DTM+164:202310062130?+00:303'
QTY+220:0'
DTM+163:202310062130?+00:303'
DTM+164:202310062145?+00:303'
QTY+220:0'
DTM+163:202310062145?+00:303'
DTM+164:202310062200?+00:303'
LIN+2'
PIA+5+1-1?:1.29.0:SRW'
QTY+220:0.725'
DTM+163:202310052200?+00:303'
DTM+164:202310052215?+00:303'
QTY+220:0.75'
DTM+163:202310052215?+00:303'
DTM+164:202310052230?+00:303'
QTY+220:0.738'
DTM+163:202310052230?+00:303'
DTM+164:202310052245?+00:303'
QTY+220:1.388'
DTM+163:202310052245?+00:303'
DTM+164:202310052300?+00:303'
QTY+220:1.175'
DTM+163:202310052300?+00:303'
DTM+164:202310052315?+00:303'
QTY+220:0.762'
DTM+163:202310052315?+00:303'
DTM+164:202310052330?+00:303'
QTY+220:0.75'
DTM+163:202310052330?+00:303'
DTM+164:202310052345?+00:303'
QTY+220:0.725'
DTM+163:202310052345?+00:303'
DTM+164:202310060000?+00:303'
QTY+220:0.738'
DTM+163:202310060000?+00:303'
DTM+164:202310060015?+00:303'
QTY+220:0.762'
DTM+163:202310060015?+00:303'
DTM+164:202310060030?+00:303'
QTY+220:0.762'
DTM+163:202310060030?+00:303'
DTM+164:202310060045?+00:303'
QTY+220:0.8'
DTM+163:202310060045?+00:303'
DTM+164:202310060100?+00:303'
QTY+220:0.75'
DTM+163:202310060100?+00:303'
DTM+164:202310060115?+00:303'
QTY+220:0.738'
DTM+163:202310060115?+00:303'
DTM+164:202310060130?+00:303'
QTY+220:0.788'
DTM+163:202310060130?+00:303'
DTM+164:202310060145?+00:303'
QTY+220:0.738'
DTM+163:202310060145?+00:303'
DTM+164:202310060200?+00:303'
QTY+220:0.712'
DTM+163:202310060200?+00:303'
DTM+164:202310060215?+00:303'
QTY+220:0.825'
DTM+163:202310060215?+00:303'
DTM+164:202310060230?+00:303'
QTY+220:0.838'
DTM+163:202310060230?+00:303'
DTM+164:202310060245?+00:303'
QTY+220:1.112'
DTM+163:202310060245?+00:303'
DTM+164:202310060300?+00:303'
QTY+220:5.038'
DTM+163:202310060300?+00:303'
DTM+164:202310060315?+00:303'
QTY+220:3.5'
DTM+163:202310060315?+00:303'
DTM+164:202310060330?+00:303'
QTY+220:4.2'
DTM+163:202310060330?+00:303'
DTM+164:202310060345?+00:303'
QTY+220:1.388'
DTM+163:202310060345?+00:303'
DTM+164:202310060400?+00:303'
QTY+220:1.575'
DTM+163:202310060400?+00:303'
DTM+164:202310060415?+00:303'
QTY+220:1.475'
DTM+163:202310060415?+00:303'
DTM+164:202310060430?+00:303'
QTY+220:2.638'
DTM+163:202310060430?+00:303'
DTM+164:202310060445?+00:303'
QTY+220:3.712'
DTM+163:202310060445?+00:303'
DTM+164:202310060500?+00:303'
QTY+220:3.538'
DTM+163:202310060500?+00:303'
DTM+164:202310060515?+00:303'
QTY+220:2.5'
DTM+163:202310060515?+00:303'
DTM+164:202310060530?+00:303'
QTY+220:1.888'
DTM+163:202310060530?+00:303'
DTM+164:202310060545?+00:303'
QTY+220:2.062'
DTM+163:202310060545?+00:303'
DTM+164:202310060600?+00:303'
QTY+220:1.9'
DTM+163:202310060600?+00:303'
DTM+164:202310060615?+00:303'
QTY+220:1.912'
DTM+163:202310060615?+00:303'
DTM+164:202310060630?+00:303'
QTY+220:1.65'
DTM+163:202310060630?+00:303'
DTM+164:202310060645?+00:303'
QTY+220:1.788'
DTM+163:202310060645?+00:303'
DTM+164:202310060700?+00:303'
QTY+220:1.325'
DTM+163:202310060700?+00:303'
DTM+164:202310060715?+00:303'
QTY+220:2.262'
DTM+163:202310060715?+00:303'
DTM+164:202310060730?+00:303'
QTY+220:5.375'
DTM+163:202310060730?+00:303'
DTM+164:202310060745?+00:303'
QTY+220:3.962'
DTM+163:202310060745?+00:303'
DTM+164:202310060800?+00:303'
QTY+220:4.338'
DTM+163:202310060800?+00:303'
DTM+164:202310060815?+00:303'
QTY+220:2.388'
DTM+163:202310060815?+00:303'
DTM+164:202310060830?+00:303'
QTY+220:1.962'
DTM+163:202310060830?+00:303'
DTM+164:202310060845?+00:303'
QTY+220:3.6'
DTM+163:202310060845?+00:303'
DTM+164:202310060900?+00:303'
QTY+220:6.162'
DTM+163:202310060900?+00:303'
DTM+164:202310060915?+00:303'
QTY+220:7.05'
DTM+163:202310060915?+00:303'
DTM+164:202310060930?+00:303'
QTY+220:5.062'
DTM+163:202310060930?+00:303'
DTM+164:202310060945?+00:303'
QTY+220:6.262'
DTM+163:202310060945?+00:303'
DTM+164:202310061000?+00:303'
QTY+220:2.275'
DTM+163:202310061000?+00:303'
DTM+164:202310061015?+00:303'
QTY+220:2.912'
DTM+163:202310061015?+00:303'
DTM+164:202310061030?+00:303'
QTY+220:1.525'
DTM+163:202310061030?+00:303'
DTM+164:202310061045?+00:303'
QTY+220:4.262'
DTM+163:202310061045?+00:303'
DTM+164:202310061100?+00:303'
QTY+220:2.712'
DTM+163:202310061100?+00:303'
DTM+164:202310061115?+00:303'
QTY+220:2.962'
DTM+163:202310061115?+00:303'
DTM+164:202310061130?+00:303'
QTY+220:2.438'
DTM+163:202310061130?+00:303'
DTM+164:202310061145?+00:303'
QTY+220:3.338'
DTM+163:202310061145?+00:303'
DTM+164:202310061200?+00:303'
QTY+220:1.938'
DTM+163:202310061200?+00:303'
DTM+164:202310061215?+00:303'
QTY+220:1.125'
DTM+163:202310061215?+00:303'
DTM+164:202310061230?+00:303'
QTY+220:1.1'
DTM+163:202310061230?+00:303'
DTM+164:202310061245?+00:303'
QTY+220:1.038'
DTM+163:202310061245?+00:303'
DTM+164:202310061300?+00:303'
QTY+220:1.062'
DTM+163:202310061300?+00:303'
DTM+164:202310061315?+00:303'
QTY+220:1.262'
DTM+163:202310061315?+00:303'
DTM+164:202310061330?+00:303'
QTY+220:1.1'
DTM+163:202310061330?+00:303'
DTM+164:202310061345?+00:303'
QTY+220:1.25'
DTM+163:202310061345?+00:303'
DTM+164:202310061400?+00:303'
QTY+220:3.038'
DTM+163:202310061400?+00:303'
DTM+164:202310061415?+00:303'
QTY+220:1.062'
DTM+163:202310061415?+00:303'
DTM+164:202310061430?+00:303'
QTY+220:0.675'
DTM+163:202310061430?+00:303'
DTM+164:202310061445?+00:303'
QTY+220:0.562'
DTM+163:202310061445?+00:303'
DTM+164:202310061500?+00:303'
QTY+220:0.575'
DTM+163:202310061500?+00:303'
DTM+164:202310061515?+00:303'
QTY+220:0.525'
DTM+163:202310061515?+00:303'
DTM+164:202310061530?+00:303'
QTY+220:0.588'
DTM+163:202310061530?+00:303'
DTM+164:202310061545?+00:303'
QTY+220:0.562'
DTM+163:202310061545?+00:303'
DTM+164:202310061600?+00:303'
QTY+220:0.575'
DTM+163:202310061600?+00:303'
DTM+164:202310061615?+00:303'
QTY+220:0.55'
DTM+163:202310061615?+00:303'
DTM+164:202310061630?+00:303'
QTY+220:0.562'
DTM+163:202310061630?+00:303'
DTM+164:202310061645?+00:303'
QTY+220:0.7'
DTM+163:202310061645?+00:303'
DTM+164:202310061700?+00:303'
QTY+220:0.662'
DTM+163:202310061700?+00:303'
DTM+164:202310061715?+00:303'
QTY+220:0.7'
DTM+163:202310061715?+00:303'
DTM+164:202310061730?+00:303'
QTY+220:0.662'
DTM+163:202310061730?+00:303'
DTM+164:202310061745?+00:303'
QTY+220:0.712'
DTM+163:202310061745?+00:303'
DTM+164:202310061800?+00:303'
QTY+220:0.662'
DTM+163:202310061800?+00:303'
DTM+164:202310061815?+00:303'
QTY+220:0.712'
DTM+163:202310061815?+00:303'
DTM+164:202310061830?+00:303'
QTY+220:0.688'
DTM+163:202310061830?+00:303'
DTM+164:202310061845?+00:303'
QTY+220:0.7'
DTM+163:202310061845?+00:303'
DTM+164:202310061900?+00:303'
QTY+220:0.662'
DTM+163:202310061900?+00:303'
DTM+164:202310061915?+00:303'
QTY+220:0.7'
DTM+163:202310061915?+00:303'
DTM+164:202310061930?+00:303'
QTY+220:0.725'
DTM+163:202310061930?+00:303'
DTM+164:202310061945?+00:303'
QTY+220:0.675'
DTM+163:202310061945?+00:303'
DTM+164:202310062000?+00:303'
QTY+220:0.662'
DTM+163:202310062000?+00:303'
DTM+164:202310062015?+00:303'
QTY+220:0.662'
DTM+163:202310062015?+00:303'
DTM+164:202310062030?+00:303'
QTY+220:0.7'
DTM+163:202310062030?+00:303'
DTM+164:202310062045?+00:303'
QTY+220:0.688'
DTM+163:202310062045?+00:303'
DTM+164:202310062100?+00:303'
QTY+220:0.7'
DTM+163:202310062100?+00:303'
DTM+164:202310062115?+00:303'
QTY+220:0.638'
DTM+163:202310062115?+00:303'
DTM+164:202310062130?+00:303'
QTY+220:0.788'
DTM+163:202310062130?+00:303'
DTM+164:202310062145?+00:303'
QTY+220:0.638'
DTM+163:202310062145?+00:303'
DTM+164:202310062200?+00:303'
UNT+592+1'
UNZ+1+K21E0D864ED9'
  ```
</Accordion>
  </Tab>
</Tabs>
  </Step>
  <Step title="13025 JSON">
    <Tabs>
  <Tab title="13025 JSON">
    <Accordion title="13025 JSON" defaultOpen>
 
  ```{
  "businessKey": "<businessKey>",
  "processDate": null,
  "dataSource": "OUTBOUND",
  "version": 1,
  "edifactVersion": 202510,
  "data": {
    "stammdaten": {
      "ENERGIEMENGE": [
        {
          "boTyp": "ENERGIEMENGE",
          "versionStruktur": "1",
          "lokationsId": "51580175011",
          "lokationsTyp": "MALO",
          "energieverbrauch": [
            {
              "startdatum": "2023-10-05T22:00:00Z",
              "enddatum": "2023-10-05T22:15:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-05T22:15:00Z",
              "enddatum": "2023-10-05T22:30:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-05T22:30:00Z",
              "enddatum": "2023-10-05T22:45:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-05T22:45:00Z",
              "enddatum": "2023-10-05T23:00:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-05T23:00:00Z",
              "enddatum": "2023-10-05T23:15:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-05T23:15:00Z",
              "enddatum": "2023-10-05T23:30:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-05T23:30:00Z",
              "enddatum": "2023-10-05T23:45:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-05T23:45:00Z",
              "enddatum": "2023-10-06T00:00:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T00:00:00Z",
              "enddatum": "2023-10-06T00:15:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T00:15:00Z",
              "enddatum": "2023-10-06T00:30:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T00:30:00Z",
              "enddatum": "2023-10-06T00:45:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T00:45:00Z",
              "enddatum": "2023-10-06T01:00:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T01:00:00Z",
              "enddatum": "2023-10-06T01:15:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T01:15:00Z",
              "enddatum": "2023-10-06T01:30:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T01:30:00Z",
              "enddatum": "2023-10-06T01:45:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T01:45:00Z",
              "enddatum": "2023-10-06T02:00:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T02:00:00Z",
              "enddatum": "2023-10-06T02:15:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T02:15:00Z",
              "enddatum": "2023-10-06T02:30:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T02:30:00Z",
              "enddatum": "2023-10-06T02:45:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T02:45:00Z",
              "enddatum": "2023-10-06T03:00:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T03:00:00Z",
              "enddatum": "2023-10-06T03:15:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T03:15:00Z",
              "enddatum": "2023-10-06T03:30:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T03:30:00Z",
              "enddatum": "2023-10-06T03:45:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T03:45:00Z",
              "enddatum": "2023-10-06T04:00:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T04:00:00Z",
              "enddatum": "2023-10-06T04:15:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T04:15:00Z",
              "enddatum": "2023-10-06T04:30:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T04:30:00Z",
              "enddatum": "2023-10-06T04:45:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0.012,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T04:45:00Z",
              "enddatum": "2023-10-06T05:00:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T05:00:00Z",
              "enddatum": "2023-10-06T05:15:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0.188,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T05:15:00Z",
              "enddatum": "2023-10-06T05:30:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0.388,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T05:30:00Z",
              "enddatum": "2023-10-06T05:45:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T05:45:00Z",
              "enddatum": "2023-10-06T06:00:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0.075,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T06:00:00Z",
              "enddatum": "2023-10-06T06:15:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0.012,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T06:15:00Z",
              "enddatum": "2023-10-06T06:30:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T06:30:00Z",
              "enddatum": "2023-10-06T06:45:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T06:45:00Z",
              "enddatum": "2023-10-06T07:00:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T07:00:00Z",
              "enddatum": "2023-10-06T07:15:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T07:15:00Z",
              "enddatum": "2023-10-06T07:30:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0.088,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T07:30:00Z",
              "enddatum": "2023-10-06T07:45:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0.975,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T07:45:00Z",
              "enddatum": "2023-10-06T08:00:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0.175,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T08:00:00Z",
              "enddatum": "2023-10-06T08:15:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0.162,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T08:15:00Z",
              "enddatum": "2023-10-06T08:30:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T08:30:00Z",
              "enddatum": "2023-10-06T08:45:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T08:45:00Z",
              "enddatum": "2023-10-06T09:00:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0.088,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T09:00:00Z",
              "enddatum": "2023-10-06T09:15:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0.175,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T09:15:00Z",
              "enddatum": "2023-10-06T09:30:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0.3,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T09:30:00Z",
              "enddatum": "2023-10-06T09:45:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0.225,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T09:45:00Z",
              "enddatum": "2023-10-06T10:00:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0.375,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T10:00:00Z",
              "enddatum": "2023-10-06T10:15:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T10:15:00Z",
              "enddatum": "2023-10-06T10:30:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T10:30:00Z",
              "enddatum": "2023-10-06T10:45:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T10:45:00Z",
              "enddatum": "2023-10-06T11:00:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0.012,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T11:00:00Z",
              "enddatum": "2023-10-06T11:15:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T11:15:00Z",
              "enddatum": "2023-10-06T11:30:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T11:30:00Z",
              "enddatum": "2023-10-06T11:45:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T11:45:00Z",
              "enddatum": "2023-10-06T12:00:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0.125,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T12:00:00Z",
              "enddatum": "2023-10-06T12:15:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0.138,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T12:15:00Z",
              "enddatum": "2023-10-06T12:30:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T12:30:00Z",
              "enddatum": "2023-10-06T12:45:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T12:45:00Z",
              "enddatum": "2023-10-06T13:00:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T13:00:00Z",
              "enddatum": "2023-10-06T13:15:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T13:15:00Z",
              "enddatum": "2023-10-06T13:30:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T13:30:00Z",
              "enddatum": "2023-10-06T13:45:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T13:45:00Z",
              "enddatum": "2023-10-06T14:00:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T14:00:00Z",
              "enddatum": "2023-10-06T14:15:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T14:15:00Z",
              "enddatum": "2023-10-06T14:30:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T14:30:00Z",
              "enddatum": "2023-10-06T14:45:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T14:45:00Z",
              "enddatum": "2023-10-06T15:00:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T15:00:00Z",
              "enddatum": "2023-10-06T15:15:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T15:15:00Z",
              "enddatum": "2023-10-06T15:30:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T15:30:00Z",
              "enddatum": "2023-10-06T15:45:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T15:45:00Z",
              "enddatum": "2023-10-06T16:00:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T16:00:00Z",
              "enddatum": "2023-10-06T16:15:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T16:15:00Z",
              "enddatum": "2023-10-06T16:30:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T16:30:00Z",
              "enddatum": "2023-10-06T16:45:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T16:45:00Z",
              "enddatum": "2023-10-06T17:00:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T17:00:00Z",
              "enddatum": "2023-10-06T17:15:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T17:15:00Z",
              "enddatum": "2023-10-06T17:30:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T17:30:00Z",
              "enddatum": "2023-10-06T17:45:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T17:45:00Z",
              "enddatum": "2023-10-06T18:00:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T18:00:00Z",
              "enddatum": "2023-10-06T18:15:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T18:15:00Z",
              "enddatum": "2023-10-06T18:30:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T18:30:00Z",
              "enddatum": "2023-10-06T18:45:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T18:45:00Z",
              "enddatum": "2023-10-06T19:00:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T19:00:00Z",
              "enddatum": "2023-10-06T19:15:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T19:15:00Z",
              "enddatum": "2023-10-06T19:30:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T19:30:00Z",
              "enddatum": "2023-10-06T19:45:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T19:45:00Z",
              "enddatum": "2023-10-06T20:00:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T20:00:00Z",
              "enddatum": "2023-10-06T20:15:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T20:15:00Z",
              "enddatum": "2023-10-06T20:30:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T20:30:00Z",
              "enddatum": "2023-10-06T20:45:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T20:45:00Z",
              "enddatum": "2023-10-06T21:00:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T21:00:00Z",
              "enddatum": "2023-10-06T21:15:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T21:15:00Z",
              "enddatum": "2023-10-06T21:30:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T21:30:00Z",
              "enddatum": "2023-10-06T21:45:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-06T21:45:00Z",
              "enddatum": "2023-10-06T22:00:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:3.29.0",
              "wert": 0,
              "position": 1
            },
            {
              "startdatum": "2023-10-05T22:00:00Z",
              "enddatum": "2023-10-05T22:15:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 0.725,
              "position": 2
            },
            {
              "startdatum": "2023-10-05T22:15:00Z",
              "enddatum": "2023-10-05T22:30:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 0.75,
              "position": 2
            },
            {
              "startdatum": "2023-10-05T22:30:00Z",
              "enddatum": "2023-10-05T22:45:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 0.738,
              "position": 2
            },
            {
              "startdatum": "2023-10-05T22:45:00Z",
              "enddatum": "2023-10-05T23:00:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 1.388,
              "position": 2
            },
            {
              "startdatum": "2023-10-05T23:00:00Z",
              "enddatum": "2023-10-05T23:15:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 1.175,
              "position": 2
            },
            {
              "startdatum": "2023-10-05T23:15:00Z",
              "enddatum": "2023-10-05T23:30:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 0.762,
              "position": 2
            },
            {
              "startdatum": "2023-10-05T23:30:00Z",
              "enddatum": "2023-10-05T23:45:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 0.75,
              "position": 2
            },
            {
              "startdatum": "2023-10-05T23:45:00Z",
              "enddatum": "2023-10-06T00:00:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 0.725,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T00:00:00Z",
              "enddatum": "2023-10-06T00:15:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 0.738,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T00:15:00Z",
              "enddatum": "2023-10-06T00:30:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 0.762,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T00:30:00Z",
              "enddatum": "2023-10-06T00:45:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 0.762,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T00:45:00Z",
              "enddatum": "2023-10-06T01:00:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 0.8,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T01:00:00Z",
              "enddatum": "2023-10-06T01:15:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 0.75,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T01:15:00Z",
              "enddatum": "2023-10-06T01:30:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 0.738,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T01:30:00Z",
              "enddatum": "2023-10-06T01:45:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 0.788,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T01:45:00Z",
              "enddatum": "2023-10-06T02:00:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 0.738,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T02:00:00Z",
              "enddatum": "2023-10-06T02:15:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 0.712,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T02:15:00Z",
              "enddatum": "2023-10-06T02:30:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 0.825,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T02:30:00Z",
              "enddatum": "2023-10-06T02:45:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 0.838,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T02:45:00Z",
              "enddatum": "2023-10-06T03:00:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 1.112,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T03:00:00Z",
              "enddatum": "2023-10-06T03:15:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 5.038,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T03:15:00Z",
              "enddatum": "2023-10-06T03:30:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 3.5,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T03:30:00Z",
              "enddatum": "2023-10-06T03:45:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 4.2,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T03:45:00Z",
              "enddatum": "2023-10-06T04:00:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 1.388,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T04:00:00Z",
              "enddatum": "2023-10-06T04:15:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 1.575,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T04:15:00Z",
              "enddatum": "2023-10-06T04:30:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 1.475,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T04:30:00Z",
              "enddatum": "2023-10-06T04:45:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 2.638,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T04:45:00Z",
              "enddatum": "2023-10-06T05:00:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 3.712,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T05:00:00Z",
              "enddatum": "2023-10-06T05:15:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 3.538,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T05:15:00Z",
              "enddatum": "2023-10-06T05:30:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 2.5,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T05:30:00Z",
              "enddatum": "2023-10-06T05:45:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 1.888,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T05:45:00Z",
              "enddatum": "2023-10-06T06:00:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 2.062,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T06:00:00Z",
              "enddatum": "2023-10-06T06:15:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 1.9,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T06:15:00Z",
              "enddatum": "2023-10-06T06:30:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 1.912,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T06:30:00Z",
              "enddatum": "2023-10-06T06:45:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 1.65,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T06:45:00Z",
              "enddatum": "2023-10-06T07:00:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 1.788,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T07:00:00Z",
              "enddatum": "2023-10-06T07:15:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 1.325,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T07:15:00Z",
              "enddatum": "2023-10-06T07:30:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 2.262,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T07:30:00Z",
              "enddatum": "2023-10-06T07:45:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 5.375,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T07:45:00Z",
              "enddatum": "2023-10-06T08:00:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 3.962,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T08:00:00Z",
              "enddatum": "2023-10-06T08:15:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 4.338,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T08:15:00Z",
              "enddatum": "2023-10-06T08:30:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 2.388,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T08:30:00Z",
              "enddatum": "2023-10-06T08:45:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 1.962,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T08:45:00Z",
              "enddatum": "2023-10-06T09:00:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 3.6,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T09:00:00Z",
              "enddatum": "2023-10-06T09:15:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 6.162,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T09:15:00Z",
              "enddatum": "2023-10-06T09:30:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 7.05,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T09:30:00Z",
              "enddatum": "2023-10-06T09:45:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 5.062,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T09:45:00Z",
              "enddatum": "2023-10-06T10:00:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 6.262,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T10:00:00Z",
              "enddatum": "2023-10-06T10:15:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 2.275,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T10:15:00Z",
              "enddatum": "2023-10-06T10:30:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 2.912,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T10:30:00Z",
              "enddatum": "2023-10-06T10:45:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 1.525,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T10:45:00Z",
              "enddatum": "2023-10-06T11:00:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 4.262,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T11:00:00Z",
              "enddatum": "2023-10-06T11:15:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 2.712,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T11:15:00Z",
              "enddatum": "2023-10-06T11:30:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 2.962,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T11:30:00Z",
              "enddatum": "2023-10-06T11:45:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 2.438,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T11:45:00Z",
              "enddatum": "2023-10-06T12:00:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 3.338,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T12:00:00Z",
              "enddatum": "2023-10-06T12:15:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 1.938,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T12:15:00Z",
              "enddatum": "2023-10-06T12:30:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 1.125,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T12:30:00Z",
              "enddatum": "2023-10-06T12:45:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 1.1,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T12:45:00Z",
              "enddatum": "2023-10-06T13:00:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 1.038,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T13:00:00Z",
              "enddatum": "2023-10-06T13:15:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 1.062,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T13:15:00Z",
              "enddatum": "2023-10-06T13:30:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 1.262,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T13:30:00Z",
              "enddatum": "2023-10-06T13:45:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 1.1,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T13:45:00Z",
              "enddatum": "2023-10-06T14:00:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 1.25,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T14:00:00Z",
              "enddatum": "2023-10-06T14:15:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 3.038,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T14:15:00Z",
              "enddatum": "2023-10-06T14:30:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 1.062,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T14:30:00Z",
              "enddatum": "2023-10-06T14:45:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 0.675,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T14:45:00Z",
              "enddatum": "2023-10-06T15:00:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 0.562,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T15:00:00Z",
              "enddatum": "2023-10-06T15:15:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 0.575,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T15:15:00Z",
              "enddatum": "2023-10-06T15:30:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 0.525,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T15:30:00Z",
              "enddatum": "2023-10-06T15:45:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 0.588,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T15:45:00Z",
              "enddatum": "2023-10-06T16:00:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 0.562,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T16:00:00Z",
              "enddatum": "2023-10-06T16:15:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 0.575,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T16:15:00Z",
              "enddatum": "2023-10-06T16:30:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 0.55,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T16:30:00Z",
              "enddatum": "2023-10-06T16:45:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 0.562,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T16:45:00Z",
              "enddatum": "2023-10-06T17:00:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 0.7,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T17:00:00Z",
              "enddatum": "2023-10-06T17:15:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 0.662,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T17:15:00Z",
              "enddatum": "2023-10-06T17:30:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 0.7,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T17:30:00Z",
              "enddatum": "2023-10-06T17:45:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 0.662,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T17:45:00Z",
              "enddatum": "2023-10-06T18:00:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 0.712,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T18:00:00Z",
              "enddatum": "2023-10-06T18:15:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 0.662,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T18:15:00Z",
              "enddatum": "2023-10-06T18:30:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 0.712,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T18:30:00Z",
              "enddatum": "2023-10-06T18:45:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 0.688,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T18:45:00Z",
              "enddatum": "2023-10-06T19:00:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 0.7,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T19:00:00Z",
              "enddatum": "2023-10-06T19:15:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 0.662,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T19:15:00Z",
              "enddatum": "2023-10-06T19:30:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 0.7,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T19:30:00Z",
              "enddatum": "2023-10-06T19:45:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 0.725,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T19:45:00Z",
              "enddatum": "2023-10-06T20:00:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 0.675,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T20:00:00Z",
              "enddatum": "2023-10-06T20:15:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 0.662,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T20:15:00Z",
              "enddatum": "2023-10-06T20:30:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 0.662,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T20:30:00Z",
              "enddatum": "2023-10-06T20:45:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 0.7,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T20:45:00Z",
              "enddatum": "2023-10-06T21:00:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 0.688,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T21:00:00Z",
              "enddatum": "2023-10-06T21:15:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 0.7,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T21:15:00Z",
              "enddatum": "2023-10-06T21:30:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 0.638,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T21:30:00Z",
              "enddatum": "2023-10-06T21:45:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 0.788,
              "position": 2
            },
            {
              "startdatum": "2023-10-06T21:45:00Z",
              "enddatum": "2023-10-06T22:00:00Z",
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.29.0",
              "wert": 0.638,
              "position": 2
            }
          ],
          "startdatum": "2023-10-05T22:00:00Z",
          "enddatum": "2023-10-06T22:00:00Z"
        }
      ]
    },
    "transaktionsdaten": {
      "datenaustauschreferenz": "K21E0D864ED9",
      "sparte": "STROM",
      "pruefidentifikator": "13025",
      "absender": {
        "boTyp": "MARKTTEILNEHMER",
        "versionStruktur": "1",
        "marktrolle": "MSB",
        "rollencodenummer": "9904545000007",
        "rollencodetyp": "BDEW"
      },
      "empfaenger": {
        "boTyp": "MARKTTEILNEHMER",
        "versionStruktur": "1",
        "marktrolle": "LF",
        "rollencodenummer": "9911694000002",
        "rollencodetyp": "BDEW"
      },
      "dokumentennummer": "K21E0D864ED90",
      "kategorie": "Z48",
      "nachrichtenfunktion": "9",
      "nachrichtendatum": "2024-04-03T05:53:00Z",
      "nachrichtenreferenznummer": "1",
      "typ": "TL"
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
