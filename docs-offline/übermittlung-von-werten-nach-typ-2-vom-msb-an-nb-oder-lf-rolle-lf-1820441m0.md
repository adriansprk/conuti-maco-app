# Übermittlung von Werten nach Typ 2 vom MSB an NB oder LF (Rolle LF)



![LW24h mit Abhängigkeiten - Übermittlung von Werten nach Typ 2 vom MSB an NB oder LF (Rolle LF)(1).png](https://api.apidog.com/api/v1/projects/816353/resources/367368/image-preview)

<Steps>
  <Step title="13027 EDI">
    <Tabs>
  <Tab title="13027 Edi">
    <Accordion title="13027 Edi" defaultOpen>

  ```UNA:+,? '
UNB+UNOC:3+9979100000001:500+9904400000002:500+251010:0806+P1001099269230++TL'
UNH+UNHM2BQ4A83+MSCONS:D:04B:UN:2.4c'
BGM+Z83+BGMM2B120EC+9'
DTM+137:202410010607?+00:303'
RFF+AGI:PP172409301012154888888888888563413'
RFF+Z13:13027'
NAD+MS+9979100000001::293'
NAD+MR+9904400000002::293'
UNS+D'
NAD+DP'
LOC+172+50375312838'
LIN+1'
PIA+5+1-0?:1.29.0:SRW'
QTY+67:1223'
DTM+163:202312220500?+00:303'
DTM+164:202408020400?+00:303'
DTM+7:202408020400?+00:303'
UNT+17+UNHM2BQ4A83'
UNZ+1+P1001099269230'
  ```
</Accordion>
  </Tab>
</Tabs>
  </Step>
  <Step title="13027 JSON">
    <Tabs>
  <Tab title="13027 JSON">
    <Accordion title="13027 JSON" defaultOpen>

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







