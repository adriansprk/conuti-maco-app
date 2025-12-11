# Übermittlung der bisher gemessenen Arbeits- und Leistungswerte (Rolle LF)


![LW24h mit Abhängigkeiten - Übermittlung der bisher gemessenen Arbeits- und Leistungswerte (Rolle LF).png](https://api.apidog.com/api/v1/projects/816353/resources/367287/image-preview)


<DataSchema id="8348181" />
<Steps>
  <Step title="13015 EDI">
    <Tabs>
  <Tab title="13015 Edi">
    <Accordion title="13015 Edi" defaultOpen>
 
  ```UNA:+,? '
UNB+UNOC:3+9979100000001:500+9904400000002:500+251010:0453+24100204533914++EM'
UNH+UNHM24CGBL4+MSCONS:D:04B:UN:2.4c'
BGM+Z27+BGMM1WGORGW+9'
DTM+137:202410020453?+00:303'
RFF+AGI:PP172409301012154888888888888563413'
RFF+Z13:13015'
NAD+MS+9979100000001::293'
NAD+MR+9904400000002::293'
UNS+D'
NAD+DP'
LOC+172+12345678901'
LIN+1'
PIA+5+1-1?:1.6.0:SRW'
QTY+67:4250,465'
DTM+306:202405:610'
STS+Z32++Z88'
UNT+16+UNHM24CGBL4'
UNZ+1+24100204533914'
  ```
</Accordion>
  </Tab>
</Tabs>
  </Step>
  <Step title="13015 JSON">
    <Tabs>
  <Tab title="13015 JSON">
    <Accordion title="13015 JSON" defaultOpen>
 
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
          "lokationsId": "12345678901",
          "lokationsTyp": "MALO",
          "energieverbrauch": [
            {
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.6.0",
              "wert": 4250.465,
              "position": 1,
              "leistungsperiode": "202405"
            },
            {
              "messwertstatus": "ABGELESEN",
              "obiskennzahl": "1-1:1.6.0",
              "wert": 6677,
              "position": 2,
              "leistungsperiode": "202408"
            }
          ]
        }
      ]
    },
    "transaktionsdaten": {
      "datenaustauschreferenz": "24100204533914",
      "sparte": "STROM",
      "pruefidentifikator": "13015",
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
      "dokumentennummer": "BGMM1WGORGW",
      "kategorie": "Z27",
      "nachrichtenfunktion": "9",
      "nachrichtendatum": "2024-10-02T04:53:00Z",
      "nachrichtenreferenznummer": "UNHM24CGBL4",
      "typ": "EM",
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
